"""Orquestador del rastreo (§4, §26).

Recorre las fuentes activas, clasifica lo que encuentra y lo deja en la bandeja
de validación. **No crea ningún evento**: la única vía al registro definitivo es
la validación humana (§4, §8).

Lo que no se pudo consultar se registra como tal en el catálogo de fuentes: un
portal inaccesible nunca se reporta como portal sin novedades.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .. import db
from ..config import CONFIG
from ..core import auditoria, bandeja, clasificador, geo
from . import google_news, html_directo, rss
from .base import Respuesta


@dataclass
class ResultadoRastreo:
    inicio: str = ""
    fin: str = ""
    consultas: int = 0
    publicaciones_vistas: int = 0
    altas_en_bandeja: int = 0
    ya_conocidas: int = 0
    descartadas_por_clasificacion: int = 0
    fuentes_ok: int = 0
    fuentes_con_error: int = 0
    detalle_fuentes: list[dict] = field(default_factory=list)
    errores: list[dict] = field(default_factory=list)

    def como_dict(self) -> dict:
        return {
            "inicio": self.inicio,
            "fin": self.fin,
            "consultas": self.consultas,
            "publicaciones_vistas": self.publicaciones_vistas,
            "altas_en_bandeja": self.altas_en_bandeja,
            "ya_conocidas": self.ya_conocidas,
            "descartadas_por_clasificacion": self.descartadas_por_clasificacion,
            "fuentes_ok": self.fuentes_ok,
            "fuentes_con_error": self.fuentes_con_error,
            "detalle_fuentes": self.detalle_fuentes,
            "errores": self.errores,
            "nota": (
                "Todo lo dado de alta queda PENDIENTE en la bandeja de validación. "
                "El rastreo no crea eventos (§4)."
            ),
        }


def _registrar_estado_fuente(source_id: int | None, respuesta: Respuesta, encontradas: int) -> None:
    if not source_id:
        return
    estatus = "ACTIVA" if respuesta.ok else respuesta.estado
    db.actualizar(
        "sources",
        {
            "ultimo_estado_http": str(respuesta.codigo) if respuesta.codigo else respuesta.estado,
            "ultimo_error": None if respuesta.ok else (respuesta.error or respuesta.estado),
            "ultima_revision": db.ahora_iso(),
            "estatus": estatus,
            "verificado": 1 if respuesta.ok else 0,
            "actualizado_en": db.ahora_iso(),
        },
        "id = ?", (source_id,),
    )


def _procesar_publicacion(
    pub: dict,
    *,
    source_id: int | None,
    collective_id: int | None,
    nivel_fuente: int,
    entidad_sugerida: str | None,
    categoria_sugerida: str | None,
    resultado: ResultadoRastreo,
) -> None:
    resultado.publicaciones_vistas += 1
    clasificacion = clasificador.clasificar(pub.get("titulo", ""), pub.get("resumen", ""))
    if not clasificacion.clasificado:
        resultado.descartadas_por_clasificacion += 1
        return

    texto = f"{pub.get('titulo','')} {pub.get('resumen','')}"
    iso, confianza_ent, alias = geo.detectar_entidad(texto)
    if not iso and entidad_sugerida:
        # La consulta se lanzó contra una entidad concreta: se propone, con
        # confianza baja, para que la bandeja la arbitre.
        iso, confianza_ent, alias = entidad_sugerida, 30, ["consulta dirigida a la entidad"]

    # La confianza mostrada en la bandeja combina la de categoría y la de
    # entidad: un hallazgo bien clasificado pero sin lugar no es explotable.
    confianza = int(round(0.65 * clasificacion.confianza + 0.35 * confianza_ent))

    raw_id = bandeja.registrar_hallazgo({
        "source_id": source_id,
        "collective_id": collective_id,
        "url": pub["url"],
        "titulo": pub.get("titulo"),
        "medio": pub.get("medio"),
        "nivel_fuente": nivel_fuente,
        "fecha_publicacion": pub.get("fecha_publicacion"),
        "categoria_detectada": clasificacion.categoria,
        "subcategoria": clasificacion.subcategoria,
        "entidad_iso": iso,
        "entidad_confianza": confianza_ent,
        "resumen": pub.get("resumen"),
        "texto": pub.get("texto"),
        "terminos": clasificacion.terminos + [f"entidad: {a}" for a in alias],
        "confianza_pct": confianza,
    })
    if raw_id is None:
        resultado.ya_conocidas += 1
    else:
        resultado.altas_en_bandeja += 1


def _fuentes_activas(niveles: tuple[int, ...] | None = None) -> list[dict]:
    condicion = "WHERE activo = 1"
    params: list = []
    if niveles:
        condicion += f" AND nivel IN ({','.join('?' * len(niveles))})"
        params += list(niveles)
    return db.consultar(f"SELECT * FROM sources {condicion} ORDER BY nivel, nombre", params)


def rastrear(
    *,
    usuario: str = "sistema",
    incluir_rss: bool = True,
    incluir_busqueda: bool = True,
    incluir_portales: bool = False,
    entidades_iso: tuple[str, ...] | None = None,
    categorias: tuple[str, ...] | None = None,
    limite_consultas: int | None = None,
) -> dict:
    """Una vuelta completa de rastreo.

    `incluir_portales` está desactivado por omisión: la lectura directa de
    portales institucionales es la vía más cara y la que más depende de que el
    egreso esté abierto. Se activa expresamente cuando el entorno lo permite.
    """
    resultado = ResultadoRastreo(inicio=db.ahora_iso())
    consultas_hechas = 0

    def tope_alcanzado() -> bool:
        return limite_consultas is not None and consultas_hechas >= limite_consultas

    # --- 1. Canales RSS verificados del catálogo ----------------------------
    if incluir_rss:
        for fuente in _fuentes_activas():
            if tope_alcanzado():
                break
            if not fuente["url_rss"] or not fuente["rss_verificado"]:
                continue
            publicaciones, respuesta = rss.entradas(fuente["url_rss"], CONFIG.max_items_por_fuente)
            consultas_hechas += 1
            resultado.consultas += 1
            _registrar_estado_fuente(fuente["id"], respuesta, len(publicaciones))
            if respuesta.ok:
                resultado.fuentes_ok += 1
            else:
                resultado.fuentes_con_error += 1
                resultado.errores.append({"fuente": fuente["nombre"], "url": fuente["url_rss"],
                                          "estado": respuesta.estado, "error": respuesta.error})
            resultado.detalle_fuentes.append({
                "fuente": fuente["nombre"], "nivel": fuente["nivel"], "via": "RSS",
                "estado": respuesta.estado, "publicaciones": len(publicaciones),
            })
            for pub in publicaciones:
                pub.setdefault("medio", fuente["nombre"])
                _procesar_publicacion(
                    pub, source_id=fuente["id"], collective_id=None, nivel_fuente=fuente["nivel"],
                    entidad_sugerida=fuente["entidad_iso"], categoria_sugerida=None, resultado=resultado,
                )

    # --- 2. Búsqueda dirigida: cruce de §5 × §6 -----------------------------
    if incluir_busqueda:
        consultas = google_news.consultas_nacionales(CONFIG.ventana_dias)
        consultas += google_news.consultas_por_entidad(
            CONFIG.ventana_dias, categorias=categorias, isos=entidades_iso
        )
        fuente_busqueda = db.consultar_uno(
            "SELECT * FROM sources WHERE tipo = 'GOOGLE_NEWS' ORDER BY id LIMIT 1"
        )
        for consulta in consultas:
            if tope_alcanzado():
                break
            publicaciones, respuesta = rss.entradas(consulta["url"], CONFIG.max_items_por_fuente)
            consultas_hechas += 1
            resultado.consultas += 1
            if respuesta.ok:
                resultado.fuentes_ok += 1
            else:
                resultado.fuentes_con_error += 1
                resultado.errores.append({
                    "fuente": f"Búsqueda «{consulta['termino']}»"
                              + (f" · {consulta['entidad']}" if consulta["entidad"] else " · nacional"),
                    "url": consulta["url"], "estado": respuesta.estado, "error": respuesta.error,
                })
            resultado.detalle_fuentes.append({
                "fuente": f"Búsqueda: {consulta['termino']}",
                "entidad": consulta["entidad"], "via": "GOOGLE_NEWS",
                "estado": respuesta.estado, "publicaciones": len(publicaciones),
            })
            for pub in publicaciones:
                _procesar_publicacion(
                    pub,
                    source_id=(fuente_busqueda or {}).get("id"),
                    collective_id=None,
                    nivel_fuente=(fuente_busqueda or {}).get("nivel", 4),
                    entidad_sugerida=consulta["entidad_iso"],
                    categoria_sugerida=consulta["categoria"],
                    resultado=resultado,
                )

    # --- 3. Lectura directa de portales -------------------------------------
    if incluir_portales:
        for fuente in _fuentes_activas(niveles=(1,)):
            if tope_alcanzado() or not fuente["url_sitio"]:
                continue
            enlaces, respuesta = html_directo.listar_enlaces(fuente["url_sitio"], CONFIG.max_items_por_fuente)
            consultas_hechas += 1
            resultado.consultas += 1
            _registrar_estado_fuente(fuente["id"], respuesta, len(enlaces))
            if respuesta.ok:
                resultado.fuentes_ok += 1
            else:
                resultado.fuentes_con_error += 1
                resultado.errores.append({"fuente": fuente["nombre"], "url": fuente["url_sitio"],
                                          "estado": respuesta.estado, "error": respuesta.error})
            resultado.detalle_fuentes.append({
                "fuente": fuente["nombre"], "nivel": 1, "via": "PORTAL",
                "estado": respuesta.estado, "publicaciones": len(enlaces),
            })
            for enlace in enlaces:
                enlace.setdefault("medio", fuente["nombre"])
                _procesar_publicacion(
                    enlace, source_id=fuente["id"], collective_id=None, nivel_fuente=1,
                    entidad_sugerida=fuente["entidad_iso"], categoria_sugerida=None, resultado=resultado,
                )

    resultado.fin = db.ahora_iso()
    db.config_set("ultimo_rastreo", resultado.como_dict(), usuario=usuario)
    auditoria.registrar(
        usuario=usuario, proceso="rastreo", entidad_tipo="config", entidad_id="ultimo_rastreo",
        campo="rastreo", valor_anterior=None,
        valor_nuevo=f"{resultado.altas_en_bandeja} alta(s) en bandeja de {resultado.publicaciones_vistas} publicación(es)",
        motivo=f"Rastreo automático · {resultado.consultas} consulta(s), "
               f"{resultado.fuentes_con_error} fuente(s) con error",
    )
    return resultado.como_dict()
