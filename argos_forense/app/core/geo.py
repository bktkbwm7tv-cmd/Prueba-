"""Catálogo de las 32 entidades federativas y detección de entidad en texto (§6).

La geometría procede de un GeoJSON público de las 32 entidades (CRS84). Los
centroides y las cajas envolventes son **cálculo propio** derivado de esa
geometría, no dato de fuente, y así se declaran en el propio archivo de datos.
"""

from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache

from ..config import DATOS_DIR

_ARCHIVO_ENTIDADES = DATOS_DIR / "entidades.json"
_ARCHIVO_GEOJSON = DATOS_DIR / "mexico-entidades.geojson"

REGIONES = (
    "Noroeste",
    "Noreste",
    "Occidente",
    "Centro",
    "Golfo",
    "Pacífico Sur",
    "Sureste",
)


def normalizar(texto: str) -> str:
    """Minúsculas sin acentos ni signos: la forma en que se comparan los nombres."""
    if not texto:
        return ""
    sin_acentos = unicodedata.normalize("NFD", texto)
    sin_acentos = "".join(c for c in sin_acentos if unicodedata.category(c) != "Mn")
    sin_acentos = sin_acentos.lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9ñ ]+", " ", sin_acentos)).strip()


@lru_cache(maxsize=1)
def entidades() -> list[dict]:
    datos = json.loads(_ARCHIVO_ENTIDADES.read_text(encoding="utf-8"))
    return datos["entidades"]


@lru_cache(maxsize=1)
def _por_iso() -> dict[str, dict]:
    return {e["iso"]: e for e in entidades()}


@lru_cache(maxsize=1)
def _por_clave() -> dict[str, dict]:
    return {e["clave_folio"]: e for e in entidades()}


def entidad(iso_o_clave: str | None) -> dict | None:
    if not iso_o_clave:
        return None
    clave = iso_o_clave.strip().upper()
    return _por_iso().get(clave) or _por_clave().get(clave)


def iso_valido(iso: str | None) -> bool:
    return entidad(iso) is not None


def nombre(iso: str) -> str:
    ent = entidad(iso)
    return ent["nombre"] if ent else iso


def region(iso: str) -> str | None:
    ent = entidad(iso)
    return ent["region"] if ent else None


def centroide(iso: str) -> list[float] | None:
    ent = entidad(iso)
    return list(ent["centroide"]) if ent else None


@lru_cache(maxsize=1)
def geojson() -> dict:
    return json.loads(_ARCHIVO_GEOJSON.read_text(encoding="utf-8"))


# --------------------------------------------------- detección en texto ------
@lru_cache(maxsize=1)
def _indice_alias() -> list[tuple[str, str, int]]:
    """(alias normalizado, iso, peso). Peso mayor = señal más específica.

    Un municipio inequívoco pesa más que el nombre del estado porque una nota
    puede citar varios estados y sólo ocurrir en uno.
    """
    indice: list[tuple[str, str, int]] = []
    for ent in entidades():
        indice.append((normalizar(ent["nombre"]), ent["iso"], 3))
        if ent["nombre_oficial"] != ent["nombre"]:
            indice.append((normalizar(ent["nombre_oficial"]), ent["iso"], 3))
        indice.append((normalizar(ent["capital"]), ent["iso"], 2))
        for a in ent["alias"]:
            indice.append((normalizar(a), ent["iso"], 2))
    # Alias más largos primero: "baja california sur" antes que "baja california".
    indice.sort(key=lambda t: len(t[0]), reverse=True)
    return indice


# Nombres que existen en más de una entidad: por sí solos no deciden nada.
AMBIGUOS = {normalizar(x) for x in ("juarez", "guadalupe", "victoria", "cuauhtemoc", "morelos", "hidalgo", "mexico")}


def detectar_entidad(texto: str) -> tuple[str | None, int, list[str]]:
    """Devuelve (iso probable, confianza 0-100, alias encontrados).

    No inventa: si el texto no nombra ninguna entidad reconocible devuelve
    (None, 0, []) y el registro entra a la bandeja sin entidad asignada.
    """
    plano = f" {normalizar(texto)} "
    puntajes: dict[str, int] = {}
    encontrados: list[str] = []
    consumido: list[tuple[int, int]] = []

    for alias, iso, peso in _indice_alias():
        if not alias or alias in AMBIGUOS:
            continue
        pos = plano.find(f" {alias} ")
        if pos < 0:
            continue
        # Evitar contar dos veces un tramo ya consumido por un alias más largo
        # ("baja california" dentro de "baja california sur").
        fin = pos + len(alias) + 2
        if any(pos >= a and fin <= b for a, b in consumido):
            continue
        consumido.append((pos, fin))
        puntajes[iso] = puntajes.get(iso, 0) + peso
        encontrados.append(alias)

    if not puntajes:
        return None, 0, []

    orden = sorted(puntajes.items(), key=lambda kv: kv[1], reverse=True)
    mejor_iso, mejor = orden[0]
    segundo = orden[1][1] if len(orden) > 1 else 0
    # Confianza: cuánto destaca la mejor señal sobre la siguiente.
    if segundo == 0:
        confianza = min(95, 55 + mejor * 10)
    elif mejor > segundo:
        confianza = min(85, 45 + (mejor - segundo) * 10)
    else:
        confianza = 35  # empate: se propone, pero la bandeja debe arbitrar
    return mejor_iso, int(confianza), encontrados
