"""Folio forense AF-AAAA-EST-CAT-NNNN (§9).

Reglas duras:
  · el consecutivo es por (año, entidad, categoría);
  · el folio se genera **al validar**, nunca al detectar;
  · una vez emitido no se modifica jamás — no existe función para cambiarlo.
"""

from __future__ import annotations

import re

from ..config import CATEGORIAS
from .. import db
from . import geo

PATRON = re.compile(r"^AF-(\d{4})-([A-Z]{3})-(FOS|CAM|CSE)-(\d{4,})$")


class FolioInvalido(ValueError):
    pass


def componer(anio: int, clave_entidad: str, categoria: str, consecutivo: int) -> str:
    return f"AF-{anio:04d}-{clave_entidad.upper()}-{categoria.upper()}-{consecutivo:04d}"


def descomponer(folio: str) -> dict:
    m = PATRON.match(folio.strip().upper())
    if not m:
        raise FolioInvalido(f"Folio fuera de formato AF-AAAA-EST-CAT-NNNN: {folio!r}")
    anio, clave, categoria, consecutivo = m.groups()
    return {
        "anio": int(anio),
        "clave_entidad": clave,
        "categoria": categoria,
        "consecutivo": int(consecutivo),
        "entidad_iso": f"MX-{clave}",
    }


def valido(folio: str) -> bool:
    try:
        descomponer(folio)
    except FolioInvalido:
        return False
    return True


def siguiente(entidad_iso: str, categoria: str, anio: int | None = None) -> str:
    """Emite el folio siguiente para esa entidad, categoría y año.

    Se apoya en el máximo consecutivo ya registrado, no en un contador aparte:
    un contador podría desincronizarse y reemitir un folio, que es justamente lo
    que §9 prohíbe.
    """
    categoria = categoria.upper()
    if categoria not in CATEGORIAS:
        raise FolioInvalido(f"Categoría desconocida: {categoria!r}. Válidas: {', '.join(CATEGORIAS)}")
    ent = geo.entidad(entidad_iso)
    if ent is None:
        raise FolioInvalido(f"Entidad desconocida: {entidad_iso!r}")

    anio = anio or int(db.ahora().year)
    clave = ent["clave_folio"]
    prefijo = f"AF-{anio:04d}-{clave}-{categoria}-"
    filas = db.consultar(
        "SELECT folio FROM events WHERE folio LIKE ? ORDER BY folio DESC LIMIT 1",
        (prefijo + "%",),
    )
    consecutivo = 1
    if filas:
        consecutivo = descomponer(filas[0]["folio"])["consecutivo"] + 1
    return componer(anio, clave, categoria, consecutivo)
