"""Métricas del DASHBOARD (§2) y del módulo Tendencias (§23).

Todos los números salen de una consulta a la base; ninguno se estima ni se
arrastra de una lectura anterior.
"""

from __future__ import annotations

from datetime import timedelta

from .. import db
from ..config import CATEGORIAS, NIVELES_CORROBORACION
from . import cortes, geo


def _en_ventana() -> tuple[str, str]:
    corte = cortes.borrador_abierto() or cortes.ultimo_publicado()
    if corte:
        return corte["ventana_inicio"], corte["ventana_fin"]
    fin = db.ahora()
    return (fin - timedelta(hours=72)).isoformat(timespec="seconds"), fin.isoformat(timespec="seconds")


def tablero() -> dict:
    inicio, fin = _en_ventana()
    activos = "estado = 'ACTIVO'"
    por_categoria = {
        c: db.escalar(f"SELECT COUNT(*) FROM events WHERE {activos} AND categoria = ?", (c,))
        for c in CATEGORIAS
    }
    por_nivel = {
        n: db.escalar(f"SELECT COUNT(*) FROM events WHERE {activos} AND nivel_corroboracion = ?", (n,))
        for n in NIVELES_CORROBORACION
    }
    corte = cortes.borrador_abierto() or cortes.ultimo_publicado()
    return {
        "generado_en": db.ahora_iso(),
        "ventana": {"inicio": inicio, "fin": fin},
        "corte_vigente": (
            {"numero": corte["numero"], "etiqueta": corte["etiqueta"], "estado": corte["estado"]}
            if corte else None
        ),
        # Los nueve indicadores que pide §2.
        "fosas_detectadas": por_categoria.get("FOS", 0),
        "campamentos": por_categoria.get("CAM", 0),
        "casas_de_seguridad": por_categoria.get("CSE", 0),
        "eventos_nuevos": db.escalar(
            f"SELECT COUNT(*) FROM events WHERE {activos} AND creado_en >= ? AND creado_en <= ?", (inicio, fin)
        ),
        "eventos_actualizados": db.escalar(
            f"SELECT COUNT(*) FROM events WHERE {activos} AND ultima_actualizacion >= ? "
            f"AND ultima_actualizacion <= ? AND creado_en < ?",
            (inicio, fin, inicio),
        ),
        "eventos_confirmados": por_nivel.get("A", 0),
        "eventos_por_verificar": por_nivel.get("D", 0),
        "entidades_con_actividad": db.escalar(
            f"SELECT COUNT(DISTINCT entidad_iso) FROM events WHERE {activos}"
        ),
        "fuentes_analizadas": db.escalar(
            "SELECT COUNT(*) FROM sources WHERE activo = 1"
        ) + db.escalar("SELECT COUNT(*) FROM collectives WHERE activo = 1"),
        "registros_pendientes_de_validacion": db.escalar(
            "SELECT COUNT(*) FROM raw_items WHERE estado = 'PENDIENTE'"
        ),
        # Contexto adicional, útil pero claramente separado de los nueve.
        "detalle": {
            "por_categoria": por_categoria,
            "por_nivel": por_nivel,
            "total_activos": db.escalar(f"SELECT COUNT(*) FROM events WHERE {activos}"),
            "registros_en_bandeja": {
                e: db.escalar("SELECT COUNT(*) FROM raw_items WHERE estado = ?", (e,))
                for e in ("PENDIENTE", "VALIDADO", "DESCARTADO", "DUPLICADO", "VINCULADO")
            },
            "duplicados_abiertos": db.escalar(
                "SELECT COUNT(*) FROM duplicate_candidates WHERE estado = 'ABIERTO'"
            ),
            "fuentes_por_nivel": {
                n: db.escalar("SELECT COUNT(*) FROM sources WHERE nivel = ? AND activo = 1", (n,))
                for n in (1, 2, 3, 4)
            },
            "colectivos_registrados": db.escalar("SELECT COUNT(*) FROM collectives WHERE activo = 1"),
            "ultimo_rastreo": db.config_get("ultimo_rastreo"),
            "cortes_publicados": db.escalar("SELECT COUNT(*) FROM cuts WHERE estado = 'PUBLICADO'"),
        },
    }


def por_entidad(iso: str | None = None) -> list[dict]:
    """Lectura por entidad para el mapa nacional (§3)."""
    inicio, fin = _en_ventana()
    salida = []
    for ent in geo.entidades():
        if iso and ent["iso"] != iso:
            continue
        base = "FROM events WHERE estado = 'ACTIVO' AND entidad_iso = ?"
        fila = {
            "iso": ent["iso"],
            "entidad": ent["nombre"],
            "region": ent["region"],
            "centroide": ent["centroide"],
            "fosas": db.escalar(f"SELECT COUNT(*) {base} AND categoria = 'FOS'", (ent["iso"],)),
            "campamentos": db.escalar(f"SELECT COUNT(*) {base} AND categoria = 'CAM'", (ent["iso"],)),
            "casas_de_seguridad": db.escalar(f"SELECT COUNT(*) {base} AND categoria = 'CSE'", (ent["iso"],)),
            "eventos_nuevos": db.escalar(
                f"SELECT COUNT(*) {base} AND creado_en >= ? AND creado_en <= ?", (ent["iso"], inicio, fin)
            ),
            "actualizaciones": db.escalar(
                f"SELECT COUNT(*) {base} AND ultima_actualizacion >= ? AND ultima_actualizacion <= ? "
                f"AND creado_en < ?", (ent["iso"], inicio, fin, inicio)
            ),
            "por_nivel": {
                n: db.escalar(f"SELECT COUNT(*) {base} AND nivel_corroboracion = ?", (ent["iso"], n))
                for n in NIVELES_CORROBORACION
            },
            "pendientes_en_bandeja": db.escalar(
                "SELECT COUNT(*) FROM raw_items WHERE estado = 'PENDIENTE' AND entidad_iso = ?", (ent["iso"],)
            ),
        }
        fila["total"] = fila["fosas"] + fila["campamentos"] + fila["casas_de_seguridad"]
        # Nivel de corroboración predominante de la entidad: el mejor sostenido.
        for n in ("A", "B", "C", "D"):
            if fila["por_nivel"][n]:
                fila["nivel_corroboracion_max"] = n
                break
        else:
            fila["nivel_corroboracion_max"] = None
        salida.append(fila)
    return salida


def tendencias(cortes_atras: int = 12) -> dict:
    """Serie por corte publicado. Sin corte publicado, la serie está vacía y se dice."""
    filas = db.consultar(
        "SELECT id, numero, etiqueta, ventana_fin FROM cuts WHERE estado = 'PUBLICADO' "
        "ORDER BY numero DESC LIMIT ?", (cortes_atras,)
    )
    filas.reverse()
    serie = []
    for c in filas:
        conteos = db.consultar(
            "SELECT categoria, COUNT(*) AS n FROM cut_events WHERE cut_id = ? GROUP BY categoria", (c["id"],)
        )
        niveles = db.consultar(
            "SELECT nivel_corroboracion AS nivel, COUNT(*) AS n FROM cut_events WHERE cut_id = ? "
            "GROUP BY nivel_corroboracion", (c["id"],)
        )
        serie.append({
            "corte": c["numero"],
            "etiqueta": c["etiqueta"],
            "cierre": c["ventana_fin"],
            "por_categoria": {**{k: 0 for k in CATEGORIAS}, **{f["categoria"]: f["n"] for f in conteos}},
            "por_nivel": {**{k: 0 for k in NIVELES_CORROBORACION}, **{f["nivel"]: f["n"] for f in niveles}},
            "nuevos": db.escalar("SELECT COUNT(*) FROM cut_events WHERE cut_id = ? AND es_nuevo = 1", (c["id"],)),
            "entidades": db.escalar("SELECT COUNT(DISTINCT entidad_iso) FROM cut_events WHERE cut_id = ?", (c["id"],)),
        })
    return {
        "serie": serie,
        "nota": (
            "Serie construida sobre cortes publicados. Sin cortes publicados no hay serie: "
            "no se rellena con estimaciones."
            if not serie else ""
        ),
    }
