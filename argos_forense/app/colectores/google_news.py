"""Consultas a Google News RSS (§1, §5, §6).

Se usa como vía de búsqueda dirigida cuando un portal no tiene canal propio
verificado. Produce el cruce de §6: cada término de categoría por cada entidad.
"""

from __future__ import annotations

from urllib.parse import quote_plus

from ..core.clasificador import TERMINOS
from ..core.geo import entidades
from .rss import entradas

BASE = "https://news.google.com/rss/search?q={consulta}&hl=es-419&gl=MX&ceid=MX:es-419"

# Términos con los que se lanza la búsqueda nacional y por entidad. Se usa un
# subconjunto de los núcleos de §5: los más discriminantes, para no gastar el
# presupuesto de consultas en términos que devuelven ruido.
TERMINOS_CONSULTA = {
    "FOS": ("fosa clandestina", "restos óseos", "entierro clandestino", "punto positivo de búsqueda"),
    "CAM": ("campamento criminal", "campo de entrenamiento criminal", "centro de adiestramiento", "campamento clandestino"),
    "CSE": ("casa de seguridad", "inmueble utilizado para cautiverio", "personas privadas de la libertad"),
}


def url_consulta(termino: str, entidad: str | None = None, dias: int = 7) -> str:
    partes = [f'"{termino}"']
    if entidad:
        partes.append(f'"{entidad}"')
    partes.append(f"when:{dias}d")
    return BASE.format(consulta=quote_plus(" ".join(partes)))


def consultas_nacionales(dias: int = 7) -> list[dict]:
    return [
        {"categoria": cat, "termino": t, "entidad_iso": None, "entidad": None, "url": url_consulta(t, None, dias)}
        for cat, terminos in TERMINOS_CONSULTA.items()
        for t in terminos
    ]


def consultas_por_entidad(dias: int = 7, categorias: tuple[str, ...] | None = None,
                          isos: tuple[str, ...] | None = None) -> list[dict]:
    """Cruce de §6: las 32 entidades por cada categoría."""
    salida = []
    for ent in entidades():
        if isos and ent["iso"] not in isos:
            continue
        for cat, terminos in TERMINOS_CONSULTA.items():
            if categorias and cat not in categorias:
                continue
            # Un término por categoría y entidad: el cruce completo son 32×3
            # consultas por vuelta, no 32×12.
            termino = terminos[0]
            salida.append({
                "categoria": cat,
                "termino": termino,
                "entidad_iso": ent["iso"],
                "entidad": ent["nombre"],
                "url": url_consulta(termino, ent["nombre"], dias),
            })
    return salida


def buscar(termino: str, entidad: str | None = None, dias: int = 7, limite: int = 25):
    return entradas(url_consulta(termino, entidad, dias), limite=limite, ventana_dias=dias)


assert set(TERMINOS_CONSULTA) == set(TERMINOS), "Las categorías de consulta deben ser las de §5."
