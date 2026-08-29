"""Niveles de corroboración A/B/C/D (§11).

El nivel no se escribe a mano: se **deriva** de las fuentes efectivamente
ligadas al evento, y se recalcula cada vez que se añade una. Un cambio de nivel
siempre queda en la bitácora con el motivo que lo produjo.
"""

from __future__ import annotations

from urllib.parse import urlparse

NIVEL_ORDEN = {"A": 3, "B": 2, "C": 1, "D": 0}

ETIQUETAS = {
    "A": "CONFIRMADO",
    "B": "ALTAMENTE CORROBORADO",
    "C": "REPORTADO",
    "D": "POR VERIFICAR",
}

DESCRIPCIONES = {
    "A": "Fuente institucional competente.",
    "B": "Dos o más fuentes independientes coincidentes.",
    "C": "Una fuente periodística identificable.",
    "D": "Reporte inicial, colectivo o publicación sin corroboración adicional.",
}


def dominio(url: str | None) -> str:
    if not url:
        return ""
    host = (urlparse(url).netloc or "").lower()
    return host[4:] if host.startswith("www.") else host


def _institucional_competente(fuente: dict, entidad_iso: str | None) -> bool:
    """Nivel 1 **y competente** sobre el hecho.

    Competente = federal, o estatal de la misma entidad del evento. Una fiscalía
    de otro estado es fuente institucional, pero no confirma un hecho ajeno a su
    jurisdicción: eso sería confirmar con autoridad incompetente.
    """
    if int(fuente.get("nivel") or 0) != 1:
        return False
    ambito = (fuente.get("ambito") or "").upper()
    if ambito in {"FEDERAL", "NACIONAL"}:
        return True
    fuente_iso = fuente.get("fuente_entidad_iso") or fuente.get("entidad_iso")
    if not fuente_iso:
        # Institucional sin ámbito declarado: cuenta como institucional, y la
        # ficha lo muestra; no se le niega el nivel A por un campo vacío del
        # catálogo, pero sí se anota en el motivo.
        return True
    return fuente_iso == entidad_iso


def evaluar(fuentes: list[dict], entidad_iso: str | None = None) -> dict:
    """Calcula el nivel a partir de las fuentes ligadas al evento.

    `fuentes` son filas de event_sources (con `nivel`, `url`, `es_colectivo`,
    `ambito` y, si se conoce, la entidad de la fuente).
    """
    if not fuentes:
        return {
            "nivel": "D",
            "etiqueta": ETIQUETAS["D"],
            "motivo": "Sin fuentes ligadas.",
            "institucionales": 0,
            "independientes": 0,
            "colectivos": 0,
        }

    institucionales = [f for f in fuentes if _institucional_competente(f, entidad_iso)]
    colectivos = [f for f in fuentes if int(f.get("es_colectivo") or 0) == 1]
    periodisticas = [
        f for f in fuentes
        if int(f.get("nivel") or 0) in (2, 3, 4) and int(f.get("es_colectivo") or 0) == 0
    ]
    # Una institución sin competencia sobre el hecho no lo confirma, pero sí es
    # una fuente identificable: cuenta para B/C como cualquier otra.
    institucionales_ajenas = [
        f for f in fuentes
        if int(f.get("nivel") or 0) == 1 and f not in institucionales
    ]
    identificables = periodisticas + institucionales_ajenas
    # Independencia por dominio: dos réplicas del mismo medio no son dos fuentes.
    dominios = {dominio(f.get("url")) for f in identificables if dominio(f.get("url"))}
    medios = {(f.get("medio") or "").strip().lower() for f in identificables if f.get("medio")}
    independientes = max(len(dominios), len(medios)) if identificables else 0

    if institucionales:
        nivel = "A"
        motivo = (
            f"Confirmado por {len(institucionales)} fuente(s) institucional(es) competente(s): "
            + ", ".join(sorted({(f.get("medio") or dominio(f.get("url")) or "institucional") for f in institucionales}))
        )
    elif independientes >= 2:
        nivel = "B"
        motivo = f"{independientes} fuentes periodísticas independientes coincidentes."
    elif identificables:
        nivel = "C"
        motivo = "Una fuente identificable, sin corroboración adicional."
    else:
        nivel = "D"
        motivo = (
            "Reporte de colectivo sin corroboración institucional ni periodística."
            if colectivos
            else "Publicación sin corroboración adicional."
        )

    return {
        "nivel": nivel,
        "etiqueta": ETIQUETAS[nivel],
        "descripcion": DESCRIPCIONES[nivel],
        "motivo": motivo,
        "institucionales": len(institucionales),
        "independientes": independientes,
        "colectivos": len(colectivos),
        "periodisticas": len(periodisticas),
        "identificables": len(identificables),
    }


def es_hecho_confirmado(nivel: str) -> bool:
    """§11: «Un nivel D no deberá mostrarse como hecho confirmado.»"""
    return nivel == "A"


def subio(anterior: str, actual: str) -> bool:
    return NIVEL_ORDEN.get(actual, 0) > NIVEL_ORDEN.get(anterior, 0)
