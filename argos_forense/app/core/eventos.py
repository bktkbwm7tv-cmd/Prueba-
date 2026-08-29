"""Ciclo de vida del evento: alta desde la bandeja, fuentes, nivel y ficha.

Reglas que este módulo hace cumplir:
  · nada llega al registro definitivo sin pasar por validación humana (§4);
  · el folio se emite una vez y no se modifica (§9);
  · un evento tiene muchas fuentes y sigue siendo un evento (§13);
  · el nivel de corroboración se deriva de las fuentes, nunca se teclea (§11);
  · cada cambio queda en la bitácora (§14) y nada se borra (§14);
  · la ubicación fina no se publica sola (§20) y no se atribuye autoría (§21).
"""

from __future__ import annotations

from typing import Any

from .. import db
from ..config import CATEGORIAS, CONFIG
from . import auditoria, corroboracion, folio as folio_mod, geo, seguridad

CAMPOS_FICHA = (
    "folio", "categoria", "subcategoria", "fecha_deteccion", "hora_deteccion",
    "fecha_probable_evento", "precision_fecha", "entidad_iso", "municipio", "localidad",
    "resumen_factual", "nivel_corroboracion", "estado", "num_cuerpos", "num_restos",
    "personas_liberadas", "personas_detenidas", "autoridad", "corte_alta",
    "ultima_actualizacion", "creado_en",
)

# Campos que un analista puede corregir en una ficha ya creada. `folio`,
# `creado_en` y `categoria` no están: el folio es inmutable (§9) y cambiar la
# categoría cambiaría el folio.
CAMPOS_EDITABLES = {
    "subcategoria", "fecha_probable_evento", "precision_fecha", "municipio", "localidad",
    "resumen_factual", "num_cuerpos", "num_restos", "personas_liberadas",
    "personas_detenidas", "autoridad", "reserva_operativa", "latitud", "longitud",
    "precision_geo",
}


class ErrorEvento(ValueError):
    pass


# ------------------------------------------------------------------ lectura --
def obtener(folio: str) -> dict | None:
    return db.consultar_uno("SELECT * FROM events WHERE folio = ?", (folio,))


def fuentes(folio: str) -> list[dict]:
    return db.consultar(
        """
        SELECT es.*, s.ambito AS ambito, s.entidad_iso AS fuente_entidad_iso, s.nombre AS fuente_nombre
        FROM event_sources es
        LEFT JOIN sources s ON s.id = es.source_id
        WHERE es.folio = ?
        ORDER BY es.nivel ASC, es.fecha_publicacion ASC, es.id ASC
        """,
        (folio,),
    )


def ficha(folio: str, exponer_exacto: bool | None = None) -> dict | None:
    """Ficha completa del evento (§10), ya con las reservas de §20 aplicadas."""
    ev = obtener(folio)
    if not ev:
        return None
    exponer = CONFIG.exponer_punto_exacto if exponer_exacto is None else exponer_exacto
    srcs = fuentes(folio)
    nivel = corroboracion.evaluar(srcs, ev["entidad_iso"])
    lat, lon, precision = seguridad.generalizar_punto(
        ev["latitud"], ev["longitud"], ev["precision_geo"], exponer, CONFIG.decimales_publicos
    )
    ent = geo.entidad(ev["entidad_iso"]) or {}
    salida = {c: ev[c] for c in CAMPOS_FICHA}
    salida.update({
        "categoria_nombre": CATEGORIAS.get(ev["categoria"], ev["categoria"]),
        "entidad": ent.get("nombre", ev["entidad_iso"]),
        "region": ent.get("region"),
        "nivel_corroboracion_etiqueta": corroboracion.ETIQUETAS.get(ev["nivel_corroboracion"], ""),
        "nivel_corroboracion_motivo": nivel["motivo"],
        "es_hecho_confirmado": corroboracion.es_hecho_confirmado(ev["nivel_corroboracion"]),
        "ubicacion": {"latitud": lat, "longitud": lon, "precision": precision},
        "reserva_operativa": bool(ev["reserva_operativa"]),
        "atribucion": db.dejs(ev["atribucion"], []),
        "fuentes": [
            {
                "id": f["id"], "nivel": f["nivel"], "medio": f["medio"] or f["fuente_nombre"],
                "titulo": f["titulo"], "url": f["url"],
                "fecha_publicacion": f["fecha_publicacion"], "fecha_consulta": f["fecha_consulta"],
                "tipo_aporte": f["tipo_aporte"],
                "es_institucional": bool(f["es_institucional"]),
                "es_colectivo": bool(f["es_colectivo"]),
                "clase": "REPORTE DE COLECTIVO" if f["es_colectivo"] else (
                    "CONFIRMACIÓN INSTITUCIONAL" if f["es_institucional"] else "PUBLICACIÓN PERIODÍSTICA"
                ),
                "sha256": f["sha256"],
            }
            for f in srcs
        ],
        "total_fuentes": len(srcs),
        "historial": auditoria.historial_evento(folio),
    })
    corte = db.consultar_uno("SELECT numero, etiqueta FROM cuts WHERE id = ?", (ev["corte_alta"],)) if ev["corte_alta"] else None
    salida["corte_aparicion"] = corte
    return salida


# --------------------------------------------------------------------- alta --
def crear_desde_raw(
    raw: dict,
    *,
    usuario: str,
    entidad_iso: str | None = None,
    categoria: str | None = None,
    municipio: str | None = None,
    localidad: str | None = None,
    resumen_factual: str | None = None,
    fecha_probable_evento: str | None = None,
    subcategoria: str | None = None,
    motivo: str | None = None,
) -> str:
    """Crea el evento definitivo a partir de un registro validado de la bandeja."""
    entidad_iso = entidad_iso or raw.get("entidad_iso")
    categoria = (categoria or raw.get("categoria_detectada") or "").upper()
    if not geo.iso_valido(entidad_iso):
        raise ErrorEvento(
            "No se puede emitir folio sin entidad federativa determinada. "
            "Asigne la entidad en la bandeja antes de validar (§9)."
        )
    if categoria not in CATEGORIAS:
        raise ErrorEvento(f"Categoría inválida: {categoria!r}. Válidas: {', '.join(CATEGORIAS)}")

    resumen = resumen_factual or raw.get("resumen") or raw.get("titulo") or ""
    resumen = seguridad.redactar(resumen)
    revision = seguridad.revisar(raw.get("titulo") or "", raw.get("resumen") or "")

    ahora = db.ahora()
    nuevo = folio_mod.siguiente(entidad_iso, categoria)
    centro = geo.centroide(entidad_iso) or [None, None]
    corte_abierto = db.consultar_uno(
        "SELECT id FROM cuts WHERE estado = 'BORRADOR' ORDER BY numero DESC LIMIT 1"
    )

    db.insertar("events", {
        "folio": nuevo,
        "categoria": categoria,
        "subcategoria": subcategoria or raw.get("subcategoria"),
        "fecha_deteccion": ahora.date().isoformat(),
        "hora_deteccion": ahora.strftime("%H:%M"),
        "fecha_probable_evento": fecha_probable_evento or (raw.get("fecha_publicacion") or "")[:10] or None,
        "precision_fecha": "DIA" if (fecha_probable_evento or raw.get("fecha_publicacion")) else "INDETERMINADA",
        "entidad_iso": entidad_iso,
        "municipio": municipio or raw.get("municipio"),
        "localidad": localidad,
        "resumen_factual": resumen,
        "nivel_corroboracion": "D",
        "estado": "ACTIVO",
        "latitud": centro[0],
        "longitud": centro[1],
        "precision_geo": "CENTROIDE_ENTIDAD",
        "geom_wkt": f"POINT({centro[1]} {centro[0]})" if centro[0] is not None else None,
        "reserva_operativa": 1 if revision.reserva_operativa else 0,
        "atribucion": db.js([]),
        "corte_alta": corte_abierto["id"] if corte_abierto else None,
        "creado_en": ahora.isoformat(timespec="seconds"),
        "ultima_actualizacion": ahora.isoformat(timespec="seconds"),
    })

    auditoria.registrar(
        usuario=usuario, proceso="alta_evento", entidad_tipo="event", entidad_id=nuevo,
        evento=nuevo, campo="folio", valor_anterior=None, valor_nuevo=nuevo,
        motivo=motivo or "Validación en bandeja", fuente_origen=raw.get("url"),
    )
    if revision.hallazgos:
        auditoria.registrar(
            usuario="sistema", proceso="opsec", entidad_tipo="event", entidad_id=nuevo, evento=nuevo,
            campo="reserva_operativa", valor_anterior="0",
            valor_nuevo="1" if revision.reserva_operativa else "0",
            motivo="§20 " + ", ".join(revision.tipos), fuente_origen=raw.get("url"),
        )

    ligar_fuente(nuevo, raw, usuario=usuario, tipo_aporte="ORIGEN", motivo=motivo)
    return nuevo


# ------------------------------------------------------------------ fuentes --
def ligar_fuente(
    folio: str,
    raw: dict,
    *,
    usuario: str,
    tipo_aporte: str = "CORROBORACION",
    motivo: str | None = None,
) -> dict:
    """Añade una fuente al evento y recalcula el nivel (§13, §11)."""
    ev = obtener(folio)
    if not ev:
        raise ErrorEvento(f"Evento inexistente: {folio}")
    if ev["estado"] in ("DESCARTADO", "FUSIONADO"):
        raise ErrorEvento(f"El evento {folio} está en estado {ev['estado']}: no admite fuentes nuevas.")

    fuente_cat = None
    if raw.get("source_id"):
        fuente_cat = db.consultar_uno("SELECT * FROM sources WHERE id = ?", (raw["source_id"],))
    nivel_fuente = int(
        raw.get("nivel_fuente")
        or (fuente_cat or {}).get("nivel")
        or (5 if raw.get("collective_id") else 4)
    )
    # El nivel 5 del catálogo es, por definición de §7, el de los colectivos
    # buscadores: una fuente de ese nivel es un REPORTE DE COLECTIVO aunque el
    # hallazgo no traiga todavía el colectivo identificado.
    es_colectivo = 1 if (raw.get("collective_id") or nivel_fuente == 5) else 0
    es_institucional = 1 if nivel_fuente == 1 else 0

    ya = db.consultar_uno("SELECT id FROM event_sources WHERE folio = ? AND url = ?", (folio, raw.get("url")))
    if ya:
        return {"folio": folio, "duplicada": True, "event_source_id": ya["id"]}

    ahora = db.ahora_iso()
    id_fuente = db.insertar("event_sources", {
        "folio": folio,
        "raw_item_id": raw.get("id"),
        "source_id": raw.get("source_id"),
        "collective_id": raw.get("collective_id"),
        "nivel": nivel_fuente,
        "medio": raw.get("medio") or (fuente_cat or {}).get("nombre"),
        "titulo": raw.get("titulo"),
        "url": raw.get("url"),
        "fecha_publicacion": raw.get("fecha_publicacion"),
        "fecha_consulta": raw.get("fecha_deteccion") or ahora,
        "tipo_aporte": tipo_aporte,
        "es_institucional": es_institucional,
        "es_colectivo": es_colectivo,
        "sha256": raw.get("url_hash"),
        "creado_en": ahora,
    })
    auditoria.registrar(
        usuario=usuario, proceso="ligar_fuente", entidad_tipo="event", entidad_id=folio, evento=folio,
        campo="fuentes", valor_anterior=None, valor_nuevo=raw.get("url"),
        motivo=motivo or f"Fuente añadida como {tipo_aporte}", fuente_origen=raw.get("url"),
    )
    cambio = recalcular_nivel(folio, usuario=usuario, motivo="Alta de fuente")
    return {"folio": folio, "event_source_id": id_fuente, "nivel": cambio}


def recalcular_nivel(folio: str, *, usuario: str = "sistema", motivo: str | None = None) -> dict:
    ev = obtener(folio)
    if not ev:
        raise ErrorEvento(f"Evento inexistente: {folio}")
    calculo = corroboracion.evaluar(fuentes(folio), ev["entidad_iso"])
    anterior = ev["nivel_corroboracion"]
    if calculo["nivel"] != anterior:
        db.actualizar(
            "events",
            {"nivel_corroboracion": calculo["nivel"], "ultima_actualizacion": db.ahora_iso()},
            "folio = ?", (folio,),
        )
        auditoria.registrar(
            usuario=usuario, proceso="corroboracion", entidad_tipo="event", entidad_id=folio, evento=folio,
            campo="nivel_corroboracion", valor_anterior=anterior, valor_nuevo=calculo["nivel"],
            motivo=f"{motivo + ' — ' if motivo else ''}{calculo['motivo']}",
        )
    return {"anterior": anterior, "actual": calculo["nivel"], **calculo}


# ------------------------------------------------------------- modificación --
def actualizar_ficha(folio: str, cambios: dict, *, usuario: str, motivo: str) -> dict:
    ev = obtener(folio)
    if not ev:
        raise ErrorEvento(f"Evento inexistente: {folio}")
    if not motivo or not motivo.strip():
        raise ErrorEvento("Toda modificación exige motivo (§14).")

    aplicables = {k: v for k, v in cambios.items() if k in CAMPOS_EDITABLES}
    rechazados = sorted(set(cambios) - set(aplicables))
    if not aplicables:
        return {"folio": folio, "modificados": 0, "rechazados": rechazados}

    if "resumen_factual" in aplicables:
        aplicables["resumen_factual"] = seguridad.redactar(str(aplicables["resumen_factual"]))
    if {"latitud", "longitud"} & set(aplicables):
        lat = aplicables.get("latitud", ev["latitud"])
        lon = aplicables.get("longitud", ev["longitud"])
        if lat is not None and lon is not None:
            aplicables["geom_wkt"] = f"POINT({lon} {lat})"

    aplicables["ultima_actualizacion"] = db.ahora_iso()
    db.actualizar("events", aplicables, "folio = ?", (folio,))
    n = auditoria.registrar_cambios(
        usuario=usuario, proceso="edicion_ficha", entidad_tipo="event", entidad_id=folio, evento=folio,
        antes=dict(ev), despues=aplicables,
        campos=[c for c in aplicables if c != "ultima_actualizacion"], motivo=motivo,
    )
    return {"folio": folio, "modificados": n, "rechazados": rechazados}


def agregar_atribucion(folio: str, atribucion: dict, *, usuario: str) -> dict:
    """§21: sólo se guarda si viene con atribuyente y fuente."""
    ev = obtener(folio)
    if not ev:
        raise ErrorEvento(f"Evento inexistente: {folio}")
    validada = seguridad.atribucion_valida(atribucion)
    lista = db.dejs(ev["atribucion"], []) or []
    lista.append({**validada, "registrada_en": db.ahora_iso(), "registrada_por": usuario})
    db.actualizar("events", {"atribucion": db.js(lista), "ultima_actualizacion": db.ahora_iso()}, "folio = ?", (folio,))
    auditoria.registrar(
        usuario=usuario, proceso="atribucion", entidad_tipo="event", entidad_id=folio, evento=folio,
        campo="atribucion", valor_anterior=None, valor_nuevo=validada["formato"],
        motivo="§21 atribución ligada a fuente identificable", fuente_origen=validada["url"],
    )
    return {"folio": folio, "atribuciones": lista}


def cambiar_estado(folio: str, estado: str, *, usuario: str, motivo: str, fusionado_en: str | None = None) -> dict:
    """§14: los registros no se borran, cambian de estado."""
    from ..config import ESTADOS

    if estado not in ESTADOS:
        raise ErrorEvento(f"Estado inválido: {estado!r}. Válidos: {', '.join(ESTADOS)}")
    ev = obtener(folio)
    if not ev:
        raise ErrorEvento(f"Evento inexistente: {folio}")
    if not motivo or not motivo.strip():
        raise ErrorEvento("Todo cambio de estado exige motivo (§14).")
    datos: dict[str, Any] = {"estado": estado, "ultima_actualizacion": db.ahora_iso()}
    if estado == "FUSIONADO":
        if not fusionado_en:
            raise ErrorEvento("Una fusión debe declarar en qué folio queda absorbido el evento.")
        if not obtener(fusionado_en):
            raise ErrorEvento(f"El folio destino {fusionado_en} no existe.")
        datos["fusionado_en"] = fusionado_en
    db.actualizar("events", datos, "folio = ?", (folio,))
    auditoria.registrar(
        usuario=usuario, proceso="cambio_estado", entidad_tipo="event", entidad_id=folio, evento=folio,
        campo="estado", valor_anterior=ev["estado"], valor_nuevo=estado, motivo=motivo,
        fuente_origen=fusionado_en,
    )
    return {"folio": folio, "estado": estado, "fusionado_en": fusionado_en}


def fusionar(folio_origen: str, folio_destino: str, *, usuario: str, motivo: str) -> dict:
    """Fusión decidida por una persona (§12): las fuentes migran, el folio origen se conserva."""
    if folio_origen == folio_destino:
        raise ErrorEvento("Un evento no se fusiona consigo mismo.")
    origen, destino = obtener(folio_origen), obtener(folio_destino)
    if not origen or not destino:
        raise ErrorEvento("Alguno de los dos folios no existe.")
    movidas = 0
    for f in fuentes(folio_origen):
        existe = db.consultar_uno(
            "SELECT id FROM event_sources WHERE folio = ? AND url = ?", (folio_destino, f["url"])
        )
        if existe:
            continue
        db.insertar("event_sources", {
            "folio": folio_destino, "raw_item_id": f["raw_item_id"], "source_id": f["source_id"],
            "collective_id": f["collective_id"], "nivel": f["nivel"], "medio": f["medio"],
            "titulo": f["titulo"], "url": f["url"], "fecha_publicacion": f["fecha_publicacion"],
            "fecha_consulta": f["fecha_consulta"], "tipo_aporte": "CORROBORACION",
            "es_institucional": f["es_institucional"], "es_colectivo": f["es_colectivo"],
            "sha256": f["sha256"], "creado_en": db.ahora_iso(),
        })
        movidas += 1
    cambiar_estado(folio_origen, "FUSIONADO", usuario=usuario, motivo=motivo, fusionado_en=folio_destino)
    nivel = recalcular_nivel(folio_destino, usuario=usuario, motivo=f"Fusión de {folio_origen}")
    auditoria.registrar(
        usuario=usuario, proceso="fusion", entidad_tipo="event", entidad_id=folio_destino, evento=folio_destino,
        campo="fuentes", valor_anterior=None, valor_nuevo=f"{movidas} fuente(s) de {folio_origen}", motivo=motivo,
    )
    return {"origen": folio_origen, "destino": folio_destino, "fuentes_migradas": movidas, "nivel": nivel}


# ------------------------------------------------------------------ listado --
def listar(
    *,
    entidad_iso: str | None = None,
    categoria: str | None = None,
    nivel: str | None = None,
    estado: str | None = "ACTIVO",
    desde: str | None = None,
    hasta: str | None = None,
    q: str | None = None,
    limite: int = 200,
    desplazamiento: int = 0,
) -> dict:
    condiciones, params = [], []
    if entidad_iso:
        condiciones.append("e.entidad_iso = ?"); params.append(entidad_iso)
    if categoria:
        condiciones.append("e.categoria = ?"); params.append(categoria.upper())
    if nivel:
        condiciones.append("e.nivel_corroboracion = ?"); params.append(nivel.upper())
    if estado:
        condiciones.append("e.estado = ?"); params.append(estado.upper())
    if desde:
        condiciones.append("e.fecha_deteccion >= ?"); params.append(desde)
    if hasta:
        condiciones.append("e.fecha_deteccion <= ?"); params.append(hasta)
    if q:
        condiciones.append("(e.resumen_factual LIKE ? OR e.municipio LIKE ? OR e.folio LIKE ?)")
        params += [f"%{q}%"] * 3
    donde = ("WHERE " + " AND ".join(condiciones)) if condiciones else ""
    total = db.escalar(f"SELECT COUNT(*) FROM events e {donde}", params)
    filas = db.consultar(
        f"""
        SELECT e.*, (SELECT COUNT(*) FROM event_sources s WHERE s.folio = e.folio) AS total_fuentes
        FROM events e {donde}
        ORDER BY e.fecha_deteccion DESC, e.folio DESC
        LIMIT ? OFFSET ?
        """,
        [*params, limite, desplazamiento],
    )
    for f in filas:
        ent = geo.entidad(f["entidad_iso"]) or {}
        f["entidad"] = ent.get("nombre", f["entidad_iso"])
        f["region"] = ent.get("region")
        f["categoria_nombre"] = CATEGORIAS.get(f["categoria"], f["categoria"])
        f["nivel_etiqueta"] = corroboracion.ETIQUETAS.get(f["nivel_corroboracion"], "")
        f["es_hecho_confirmado"] = corroboracion.es_hecho_confirmado(f["nivel_corroboracion"])
        lat, lon, precision = seguridad.generalizar_punto(
            f["latitud"], f["longitud"], f["precision_geo"], CONFIG.exponer_punto_exacto, CONFIG.decimales_publicos
        )
        f["latitud"], f["longitud"], f["precision_geo"] = lat, lon, precision
        f["atribucion"] = db.dejs(f["atribucion"], [])
        f.pop("geom_wkt", None)
    return {"total": total, "limite": limite, "desplazamiento": desplazamiento, "eventos": filas}
