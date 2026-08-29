"""Deduplicación (§12).

El sistema **puntúa**; la persona decide. No existe en este módulo ninguna vía
que fusione dos registros: la fusión es una acción de la bandeja, con usuario,
motivo y bitácora.

Los criterios son los que fija §12 y cada uno aporta su peso al porcentaje que
se muestra («POSIBLE DUPLICIDAD: 91 %»), junto con el desglose que lo explica.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime

from .clasificador import extraer_cifras
from .geo import normalizar

# Peso de cada criterio de §12. Suman 100.
PESOS = {
    "entidad": 16,
    "municipio": 14,
    "fecha": 12,
    "categoria": 10,
    "localidad": 8,
    "predio": 8,
    "carretera": 5,
    "colonia": 5,
    "cuerpos": 8,
    "restos": 4,
    "autoridad": 4,
    "texto": 6,
}

# Palabras vacías: no aportan a la similitud textual de un titular.
VACIAS = {
    "de", "del", "la", "las", "el", "los", "un", "una", "y", "en", "con", "por", "para",
    "que", "se", "al", "a", "su", "sus", "tras", "sobre", "entre", "hasta", "desde",
    "es", "son", "fue", "fueron", "ha", "han", "no", "mas", "muy", "este", "esta",
}

RE_PREDIO = re.compile(
    r"\b(?:predio|rancho|finca|parcela|ejido|terreno|bodega|lote)\s+(?:denominad[oa]\s+)?"
    r"(?:\"|«|el |la |los |las )?([A-ZÁÉÍÓÚÑ][\wÁÉÍÓÚÑáéíóúñ]*(?:\s+[\wÁÉÍÓÚÑáéíóúñ]+){0,3})"
)
RE_CARRETERA = re.compile(
    r"\b(?:carretera|autopista|libramiento|tramo)\s+([\wÁÉÍÓÚÑáéíóúñ.\-]+(?:\s*[-–]\s*[\wÁÉÍÓÚÑáéíóúñ.\-]+)?"
    r"(?:\s+[\wÁÉÍÓÚÑáéíóúñ]+){0,2})",
    re.IGNORECASE,
)
RE_COLONIA = re.compile(
    r"\b(?:colonia|col\.|fraccionamiento|fracc\.|barrio|unidad habitacional)\s+"
    r"([\wÁÉÍÓÚÑáéíóúñ]+(?:\s+[\wÁÉÍÓÚÑáéíóúñ]+){0,2})",
    re.IGNORECASE,
)
RE_LOCALIDAD = re.compile(
    r"\b(?:localidad|comunidad|poblado|ejido|rancher[íi]a)\s+(?:de\s+)?"
    r"([\wÁÉÍÓÚÑáéíóúñ]+(?:\s+[\wÁÉÍÓÚÑáéíóúñ]+){0,2})",
    re.IGNORECASE,
)
AUTORIDADES = (
    "fiscalia", "fge", "fgr", "sedena", "semar", "guardia nacional", "sspc",
    "policia estatal", "policia municipal", "ejercito", "marina", "comision de busqueda",
    "fuerza civil", "guardia civil", "policia ministerial", "semefo",
)


def _terminos_geograficos(texto: str) -> dict[str, set[str]]:
    return {
        "predio": {normalizar(m) for m in RE_PREDIO.findall(texto)},
        "carretera": {normalizar(m) for m in RE_CARRETERA.findall(texto)},
        "colonia": {normalizar(m) for m in RE_COLONIA.findall(texto)},
        "localidad": {normalizar(m) for m in RE_LOCALIDAD.findall(texto)},
    }


def _autoridades(texto: str) -> set[str]:
    plano = normalizar(texto)
    return {a for a in AUTORIDADES if a in plano}


def _tokens(texto: str) -> set[str]:
    return {t for t in normalizar(texto).split() if len(t) > 3 and t not in VACIAS}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _fecha(valor) -> date | None:
    if not valor:
        return None
    if isinstance(valor, date) and not isinstance(valor, datetime):
        return valor
    if isinstance(valor, datetime):
        return valor.date()
    try:
        return datetime.fromisoformat(str(valor)[:19]).date()
    except ValueError:
        try:
            return datetime.strptime(str(valor)[:10], "%Y-%m-%d").date()
        except ValueError:
            return None


@dataclass
class Comparacion:
    puntaje: int = 0
    desglose: dict = field(default_factory=dict)

    @property
    def etiqueta(self) -> str:
        return f"POSIBLE DUPLICIDAD: {self.puntaje} %"


def _texto_de(registro: dict) -> str:
    partes = [registro.get("titulo"), registro.get("resumen"), registro.get("texto"), registro.get("resumen_factual")]
    return " ".join(p for p in partes if p)


def comparar(a: dict, b: dict) -> Comparacion:
    """Compara dos registros (raw_item o evento) según los criterios de §12.

    Los criterios que ninguno de los dos registros aporta **no puntúan ni
    penalizan**: el porcentaje se calcula sobre los criterios efectivamente
    comparables y se declara cuáles fueron. Un 91 % obtenido sobre tres campos
    no es lo mismo que uno obtenido sobre diez, y el desglose lo muestra.
    """
    texto_a, texto_b = _texto_de(a), _texto_de(b)
    geo_a, geo_b = _terminos_geograficos(texto_a), _terminos_geograficos(texto_b)

    desglose: dict[str, dict] = {}
    obtenido = 0
    posible = 0

    def anotar(criterio: str, comparable: bool, coincide: float, detalle: str) -> None:
        nonlocal obtenido, posible
        peso = PESOS[criterio]
        if not comparable:
            desglose[criterio] = {"comparable": False, "detalle": detalle, "aporta": 0, "peso": peso}
            return
        aporta = round(peso * coincide, 2)
        obtenido += aporta
        posible += peso
        desglose[criterio] = {
            "comparable": True,
            "coincidencia": round(coincide, 3),
            "aporta": aporta,
            "peso": peso,
            "detalle": detalle,
        }

    # --- entidad
    ea, eb = a.get("entidad_iso"), b.get("entidad_iso")
    anotar("entidad", bool(ea and eb), 1.0 if ea == eb else 0.0, f"{ea or '—'} / {eb or '—'}")

    # --- municipio
    ma, mb = normalizar(a.get("municipio") or ""), normalizar(b.get("municipio") or "")
    anotar("municipio", bool(ma and mb), 1.0 if ma == mb else 0.0, f"{ma or '—'} / {mb or '—'}")

    # --- fecha (del hecho si existe; si no, la de publicación)
    fa = _fecha(a.get("fecha_probable_evento") or a.get("fecha_publicacion"))
    fb = _fecha(b.get("fecha_probable_evento") or b.get("fecha_publicacion"))
    if fa and fb:
        dias = abs((fa - fb).days)
        # Un mismo hecho se publica a lo largo de varios días: 0-1 día pleno,
        # hasta 3 días decayendo, más allá no aporta.
        coincide = 1.0 if dias <= 1 else (0.6 if dias <= 3 else 0.0)
        anotar("fecha", True, coincide, f"{fa} / {fb} · {dias} día(s)")
    else:
        anotar("fecha", False, 0.0, "sin fecha en alguno de los dos")

    # --- categoría
    ca = (a.get("categoria") or a.get("categoria_detectada") or "").upper()
    cb = (b.get("categoria") or b.get("categoria_detectada") or "").upper()
    anotar("categoria", bool(ca and cb), 1.0 if ca == cb else 0.0, f"{ca or '—'} / {cb or '—'}")

    # --- términos geográficos de §12
    for criterio in ("localidad", "predio", "carretera", "colonia"):
        sa = set(geo_a[criterio])
        sb = set(geo_b[criterio])
        if criterio == "localidad":
            if a.get("localidad"):
                sa.add(normalizar(a["localidad"]))
            if b.get("localidad"):
                sb.add(normalizar(b["localidad"]))
        anotar(
            criterio,
            bool(sa and sb),
            jaccard(sa, sb),
            f"{sorted(sa) or '—'} / {sorted(sb) or '—'}",
        )

    # --- número de cuerpos / restos
    cif_a = {**extraer_cifras(texto_a), **{k: v for k, v in a.items() if k in ("num_cuerpos",) and v}}
    cif_b = {**extraer_cifras(texto_b), **{k: v for k, v in b.items() if k in ("num_cuerpos",) and v}}
    na, nb = cif_a.get("num_cuerpos"), cif_b.get("num_cuerpos")
    anotar("cuerpos", na is not None and nb is not None, 1.0 if na == nb else 0.0, f"{na} / {nb}")

    ra, rb = cif_a.get("num_bolsas"), cif_b.get("num_bolsas")
    anotar("restos", ra is not None and rb is not None, 1.0 if ra == rb else 0.0, f"{ra} / {rb}")

    # --- autoridad participante
    aa, ab = _autoridades(texto_a), _autoridades(texto_b)
    anotar("autoridad", bool(aa and ab), jaccard(aa, ab), f"{sorted(aa) or '—'} / {sorted(ab) or '—'}")

    # --- similitud textual
    ta, tb = _tokens(texto_a), _tokens(texto_b)
    sim = jaccard(ta, tb)
    anotar("texto", bool(ta and tb), sim, f"jaccard {sim:.2f} sobre {len(ta)}/{len(tb)} términos")

    puntaje = int(round(100 * obtenido / posible)) if posible else 0
    desglose["_meta"] = {
        "peso_comparable": posible,
        "peso_total": sum(PESOS.values()),
        "criterios_comparados": sorted(k for k, v in desglose.items() if isinstance(v, dict) and v.get("comparable")),
        "advertencia": (
            "Porcentaje calculado sólo sobre los criterios comparables."
            if posible < sum(PESOS.values())
            else ""
        ),
    }
    return Comparacion(puntaje=puntaje, desglose=desglose)


def candidatos(registro: dict, universo: list[dict], umbral: int = 60, tope: int = 10) -> list[dict]:
    """Devuelve los posibles duplicados por encima del umbral, del más alto al más bajo.

    Nunca fusiona ni marca nada: sólo propone (§12).
    """
    salida = []
    for otro in universo:
        if otro is registro:
            continue
        if registro.get("id") and otro.get("id") == registro.get("id"):
            continue
        if registro.get("folio") and otro.get("folio") == registro.get("folio"):
            continue
        cmp_ = comparar(registro, otro)
        if cmp_.puntaje >= umbral:
            salida.append({
                "referencia": otro.get("folio") or otro.get("id"),
                "tipo": "evento" if otro.get("folio") else "raw_item",
                "titulo": otro.get("titulo") or otro.get("resumen_factual"),
                "puntaje": cmp_.puntaje,
                "etiqueta": cmp_.etiqueta,
                "desglose": cmp_.desglose,
            })
    salida.sort(key=lambda d: d["puntaje"], reverse=True)
    return salida[:tope]
