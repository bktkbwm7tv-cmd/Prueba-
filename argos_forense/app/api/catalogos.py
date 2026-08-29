"""Fuentes, colectivos, entidades, bitácora, tablero, mapa y exportaciones (§24)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from pydantic import BaseModel, Field

from .. import db
from ..colectores import rss as rss_col
from ..colectores.base import obtener as http_obtener
from ..config import CATEGORIAS, NIVELES_CORROBORACION, NIVELES_FUENTE
from ..core import auditoria, exportacion, geo, tablero
from .comun import paginacion, usuario_actual

router = APIRouter(tags=["catálogos"])


# --------------------------------------------------------------- fuentes ----
class FuenteNueva(BaseModel):
    nivel: int = Field(..., ge=1, le=5)
    nombre: str = Field(..., min_length=3)
    ambito: str = Field(default="NACIONAL", pattern="^(FEDERAL|ESTATAL|REGIONAL|MUNICIPAL|NACIONAL)$")
    entidad_iso: str | None = None
    tipo: str = Field(default="PORTAL", pattern="^(PORTAL|RSS|GOOGLE_NEWS|REDES)$")
    url_sitio: str | None = None
    url_rss: str | None = None
    clase_url: str | None = Field(default=None, pattern="^[ABC]$")
    notas: str | None = None


class FuenteEdicion(BaseModel):
    url_sitio: str | None = None
    url_rss: str | None = None
    clase_url: str | None = Field(default=None, pattern="^[ABC]$")
    activo: bool | None = None
    notas: str | None = None
    motivo: str = Field(..., min_length=3)


@router.get("/api/sources")
def listar_fuentes(
    nivel: int | None = Query(default=None, ge=1, le=5),
    entidad: str | None = None,
    activo: bool | None = None,
    q: str | None = None,
    limite: int = Query(default=500, ge=1, le=1000),
    desplazamiento: int = Query(default=0, ge=0),
) -> dict:
    limite, desplazamiento = paginacion(limite, desplazamiento)
    condiciones, params = [], []
    if nivel:
        condiciones.append("nivel = ?"); params.append(nivel)
    if entidad:
        condiciones.append("entidad_iso = ?"); params.append(entidad)
    if activo is not None:
        condiciones.append("activo = ?"); params.append(1 if activo else 0)
    if q:
        condiciones.append("(nombre LIKE ? OR dominio LIKE ?)"); params += [f"%{q}%"] * 2
    donde = ("WHERE " + " AND ".join(condiciones)) if condiciones else ""
    total = db.escalar(f"SELECT COUNT(*) FROM sources {donde}", params)
    filas = db.consultar(
        f"SELECT * FROM sources {donde} ORDER BY nivel, entidad_iso IS NULL DESC, nombre LIMIT ? OFFSET ?",
        [*params, limite, desplazamiento],
    )
    for f in filas:
        f["nivel_nombre"] = NIVELES_FUENTE.get(f["nivel"], "")
        f["entidad"] = geo.nombre(f["entidad_iso"]) if f["entidad_iso"] else None
    return {
        "total": total, "limite": limite, "desplazamiento": desplazamiento,
        "niveles": NIVELES_FUENTE,
        "por_nivel": {n: db.escalar("SELECT COUNT(*) FROM sources WHERE nivel = ?", (n,)) for n in NIVELES_FUENTE},
        "sin_dominio_registrado": db.escalar("SELECT COUNT(*) FROM sources WHERE dominio IS NULL"),
        "verificadas": db.escalar("SELECT COUNT(*) FROM sources WHERE verificado = 1"),
        "fuentes": filas,
    }


@router.post("/api/sources", status_code=201)
def crear_fuente(peticion: FuenteNueva, usuario: str = Depends(usuario_actual)) -> dict:
    if peticion.entidad_iso and not geo.iso_valido(peticion.entidad_iso):
        raise HTTPException(status_code=422, detail=f"Entidad desconocida: {peticion.entidad_iso}")
    ahora = db.ahora_iso()
    dominio = None
    if peticion.url_sitio or peticion.url_rss:
        from urllib.parse import urlparse
        dominio = urlparse(peticion.url_sitio or peticion.url_rss).netloc or None
    sid = db.insertar("sources", {
        **peticion.model_dump(),
        "dominio": dominio, "verificado": 0, "rss_verificado": 0, "activo": 1,
        "estatus": "SIN VERIFICAR", "origen_registro": f"Alta manual de {usuario}",
        "creado_en": ahora, "actualizado_en": ahora,
    })
    auditoria.registrar(
        usuario=usuario, proceso="catalogo_fuentes", entidad_tipo="source", entidad_id=sid,
        campo="alta", valor_anterior=None, valor_nuevo=peticion.nombre, motivo="Alta manual de fuente",
    )
    return {"id": sid, **peticion.model_dump()}


@router.patch("/api/sources/{source_id}")
def editar_fuente(source_id: int, peticion: FuenteEdicion, usuario: str = Depends(usuario_actual)) -> dict:
    antes = db.consultar_uno("SELECT * FROM sources WHERE id = ?", (source_id,))
    if not antes:
        raise HTTPException(status_code=404, detail=f"No existe la fuente {source_id}.")
    cambios = {k: v for k, v in peticion.model_dump(exclude={"motivo"}).items() if v is not None}
    if "activo" in cambios:
        cambios["activo"] = 1 if cambios["activo"] else 0
    if not cambios:
        return {"id": source_id, "modificados": 0}
    cambios["actualizado_en"] = db.ahora_iso()
    db.actualizar("sources", cambios, "id = ?", (source_id,))
    n = auditoria.registrar_cambios(
        usuario=usuario, proceso="catalogo_fuentes", entidad_tipo="source", entidad_id=source_id,
        antes=antes, despues=cambios, campos=[c for c in cambios if c != "actualizado_en"],
        motivo=peticion.motivo,
    )
    return {"id": source_id, "modificados": n}


@router.post("/api/sources/{source_id}/verify")
def verificar_fuente(source_id: int, usuario: str = Depends(usuario_actual)) -> dict:
    """Sondea la fuente de verdad y escribe lo que devolvió. `verificado` sólo lo pone este sondeo."""
    fuente = db.consultar_uno("SELECT * FROM sources WHERE id = ?", (source_id,))
    if not fuente:
        raise HTTPException(status_code=404, detail=f"No existe la fuente {source_id}.")
    resultado: dict = {"id": source_id, "nombre": fuente["nombre"]}

    if fuente["url_rss"]:
        rss_estado = rss_col.verificar_canal(fuente["url_rss"])
        resultado["rss"] = rss_estado
        db.actualizar("sources", {"rss_verificado": 1 if rss_estado["verificado"] else 0,
                                  "actualizado_en": db.ahora_iso()}, "id = ?", (source_id,))
    if fuente["url_sitio"]:
        respuesta = http_obtener(fuente["url_sitio"])
        resultado["sitio"] = {"ok": respuesta.ok, "estado": respuesta.estado,
                              "codigo": respuesta.codigo, "error": respuesta.error}
        db.actualizar("sources", {
            "verificado": 1 if respuesta.ok else 0,
            "ultimo_estado_http": str(respuesta.codigo) if respuesta.codigo else respuesta.estado,
            "ultimo_error": None if respuesta.ok else (respuesta.error or respuesta.estado),
            "ultima_revision": db.ahora_iso(),
            "estatus": "ACTIVA" if respuesta.ok else respuesta.estado,
            "actualizado_en": db.ahora_iso(),
        }, "id = ?", (source_id,))
    if not fuente["url_rss"] and not fuente["url_sitio"]:
        resultado["nota"] = "SIN DOMINIO CANÓNICO REGISTRADO: no hay nada que sondear."
    auditoria.registrar(
        usuario=usuario, proceso="verificacion_fuente", entidad_tipo="source", entidad_id=source_id,
        campo="verificado", valor_anterior=str(fuente["verificado"]),
        valor_nuevo=str(resultado.get("sitio", {}).get("ok", "")),
        motivo="Sondeo de la fuente", fuente_origen=fuente["url_sitio"] or fuente["url_rss"],
    )
    return resultado


# ------------------------------------------------------------ colectivos ----
class ColectivoNuevo(BaseModel):
    nombre: str = Field(..., min_length=3)
    entidad_iso: str | None = None
    municipio_base: str | None = None
    url_web: str | None = None
    url_facebook: str | None = None
    url_instagram: str | None = None
    url_x: str | None = None
    url_tiktok: str | None = None
    otras_paginas: list[dict] = Field(default_factory=list)
    estatus_fuente: str = Field(default="SIN VERIFICAR")
    notas: str | None = None


class ColectivoEdicion(ColectivoNuevo):
    nombre: str | None = None  # type: ignore[assignment]
    motivo: str = Field(..., min_length=3)


@router.get("/api/collectives")
def listar_colectivos(entidad: str | None = None, activo: bool | None = True) -> dict:
    condiciones, params = [], []
    if entidad:
        condiciones.append("entidad_iso = ?"); params.append(entidad)
    if activo is not None:
        condiciones.append("activo = ?"); params.append(1 if activo else 0)
    donde = ("WHERE " + " AND ".join(condiciones)) if condiciones else ""
    filas = db.consultar(f"SELECT * FROM collectives {donde} ORDER BY entidad_iso, nombre", params)
    for f in filas:
        f["otras_paginas"] = db.dejs(f["otras_paginas"], [])
        f["entidad"] = geo.nombre(f["entidad_iso"]) if f["entidad_iso"] else "Nacional"
    return {
        "total": len(filas),
        "distincion": {
            "REPORTE DE COLECTIVO": "Aporta un reporte. Por sí solo deja el evento en nivel D (§11).",
            "CONFIRMACIÓN INSTITUCIONAL": "Sólo una fuente institucional competente lleva un evento al nivel A.",
        },
        "nota_seguridad": "§20: este módulo no almacena domicilios ni teléfonos de colectivos ni de familias.",
        "colectivos": filas,
    }


@router.post("/api/collectives", status_code=201)
def crear_colectivo(peticion: ColectivoNuevo, usuario: str = Depends(usuario_actual)) -> dict:
    if peticion.entidad_iso and not geo.iso_valido(peticion.entidad_iso):
        raise HTTPException(status_code=422, detail=f"Entidad desconocida: {peticion.entidad_iso}")
    ahora = db.ahora_iso()
    datos = peticion.model_dump()
    datos["otras_paginas"] = db.js(datos["otras_paginas"])
    cid = db.insertar("collectives", {
        **datos, "fecha_ultima_revision": ahora, "activo": 1, "creado_en": ahora, "actualizado_en": ahora,
    })
    auditoria.registrar(
        usuario=usuario, proceso="catalogo_colectivos", entidad_tipo="collective", entidad_id=cid,
        campo="alta", valor_anterior=None, valor_nuevo=peticion.nombre, motivo="Alta manual de colectivo",
    )
    return {"id": cid, **peticion.model_dump()}


@router.patch("/api/collectives/{collective_id}")
def editar_colectivo(collective_id: int, peticion: ColectivoEdicion, usuario: str = Depends(usuario_actual)) -> dict:
    antes = db.consultar_uno("SELECT * FROM collectives WHERE id = ?", (collective_id,))
    if not antes:
        raise HTTPException(status_code=404, detail=f"No existe el colectivo {collective_id}.")
    cambios = {k: v for k, v in peticion.model_dump(exclude={"motivo"}).items() if v not in (None, [])}
    if "otras_paginas" in cambios:
        cambios["otras_paginas"] = db.js(cambios["otras_paginas"])
    if not cambios:
        return {"id": collective_id, "modificados": 0}
    cambios["fecha_ultima_revision"] = db.ahora_iso()
    cambios["actualizado_en"] = db.ahora_iso()
    db.actualizar("collectives", cambios, "id = ?", (collective_id,))
    n = auditoria.registrar_cambios(
        usuario=usuario, proceso="catalogo_colectivos", entidad_tipo="collective", entidad_id=collective_id,
        antes=antes, despues=cambios,
        campos=[c for c in cambios if c not in ("actualizado_en", "fecha_ultima_revision")],
        motivo=peticion.motivo,
    )
    return {"id": collective_id, "modificados": n}


# --------------------------------------------------------------- bitácora ---
@router.get("/api/audit")
def bitacora(
    entidad_tipo: str | None = None,
    entidad_id: str | None = None,
    evento: str | None = None,
    usuario_filtro: str | None = Query(default=None, alias="usuario"),
    proceso: str | None = None,
    desde: str | None = None,
    hasta: str | None = None,
    limite: int = Query(default=200, ge=1, le=2000),
    desplazamiento: int = Query(default=0, ge=0),
) -> dict:
    limite, desplazamiento = paginacion(limite, desplazamiento, tope=2000)
    condiciones, params = [], []
    for campo, valor in (("entidad_tipo", entidad_tipo), ("entidad_id", entidad_id),
                         ("evento", evento), ("usuario", usuario_filtro), ("proceso", proceso)):
        if valor:
            condiciones.append(f"{campo} = ?"); params.append(valor)
    if desde:
        condiciones.append("ts >= ?"); params.append(desde)
    if hasta:
        condiciones.append("ts <= ?"); params.append(hasta)
    donde = ("WHERE " + " AND ".join(condiciones)) if condiciones else ""
    return {
        "total": db.escalar(f"SELECT COUNT(*) FROM audit {donde}", params),
        "limite": limite, "desplazamiento": desplazamiento,
        "nota": "§14: la bitácora sólo admite altas. Ningún registro se borra ni se edita.",
        "movimientos": db.consultar(
            f"SELECT * FROM audit {donde} ORDER BY id DESC LIMIT ? OFFSET ?", [*params, limite, desplazamiento]
        ),
    }


# ------------------------------------------------- tablero, mapa y estados --
@router.get("/api/dashboard")
def dashboard() -> dict:
    return tablero.tablero()


@router.get("/api/states")
def estados() -> dict:
    return {"entidades": tablero.por_entidad()}


@router.get("/api/states/{iso}")
def estado(iso: str) -> dict:
    from ..core import eventos as eventos_core

    datos = tablero.por_entidad(iso)
    if not datos:
        raise HTTPException(status_code=404, detail=f"Entidad desconocida: {iso}")
    resumen = datos[0]
    resumen["eventos"] = eventos_core.listar(entidad_iso=iso, limite=500)["eventos"]
    return resumen


@router.get("/api/geo/entidades.geojson")
def entidades_geojson() -> dict:
    return exportacion.entidades_geojson(tablero.por_entidad())


@router.get("/api/trends")
def tendencias(cortes: int = Query(default=12, ge=1, le=60)) -> dict:
    return tablero.tendencias(cortes)


@router.get("/api/catalogs")
def catalogos() -> dict:
    return {
        "categorias": CATEGORIAS,
        "niveles_corroboracion": NIVELES_CORROBORACION,
        "niveles_fuente": NIVELES_FUENTE,
        "regiones": list(geo.REGIONES),
        "entidades": [
            {"iso": e["iso"], "clave_folio": e["clave_folio"], "nombre": e["nombre"],
             "region": e["region"], "capital": e["capital"], "centroide": e["centroide"]}
            for e in geo.entidades()
        ],
    }


# ----------------------------------------------------------- exportaciones --
@router.get("/api/export/events.{formato}")
def exportar(
    formato: str,
    entidad: str | None = None,
    categoria: str | None = None,
    nivel: str | None = Query(default=None, pattern="^[ABCD]$"),
    estado: str | None = "ACTIVO",
    desde: str | None = None,
    hasta: str | None = None,
) -> Response:
    filtros = {"entidad_iso": entidad, "categoria": categoria, "nivel": nivel,
               "estado": estado, "desde": desde, "hasta": hasta}
    formato = formato.lower()
    if formato == "json":
        return Response(exportacion.a_json(filtros), media_type="application/json; charset=utf-8")
    if formato == "csv":
        return Response(
            exportacion.a_csv(filtros), media_type="text/csv; charset=utf-8",
            headers={"Content-Disposition": 'attachment; filename="argos-forense-eventos.csv"'},
        )
    if formato == "geojson":
        return Response(exportacion.a_geojson(filtros), media_type="application/geo+json; charset=utf-8")
    raise HTTPException(status_code=400, detail="Formatos disponibles: json, csv, geojson. Para PDF: /api/cuts/{n}/export.pdf")
