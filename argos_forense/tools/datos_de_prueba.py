#!/usr/bin/env python3
"""Carga registros FICTICIOS para probar la interfaz.

ADVERTENCIA — leer antes de usar:

    Todo lo que este script inserta es **inventado** y está marcado como tal en
    el propio texto de cada registro. Sirve para revisar la interfaz y los
    cálculos con datos a la vista; **jamás** debe ejecutarse sobre la base de
    una instalación real, porque contaminaría el acervo con hechos que no
    existen.

Por eso exige una base de datos distinta de la de producción:

    ARGOS_DB=/tmp/demo.sqlite3 python tools/datos_de_prueba.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

MARCA = "[EJEMPLO DE PRUEBA — DATO FICTICIO]"

REGISTROS = [
    {
        "url": "https://ejemplo.invalid/prueba/1",
        "titulo": f"{MARCA} Localizan fosa clandestina con tres cuerpos en el predio de prueba",
        "medio": "Medio de prueba nacional", "nivel_fuente": 2, "entidad_iso": "MX-JAL",
        "municipio": "Tlajomulco de Zúñiga", "categoria_detectada": "FOS", "confianza_pct": 72,
        "resumen": f"{MARCA} Registro sintético para revisar la interfaz. No corresponde a ningún hecho real.",
        "fecha_publicacion": "2026-08-27T09:00:00-06:00",
    },
    {
        "url": "https://ejemplo.invalid/prueba/2",
        "titulo": f"{MARCA} Fiscalía confirma el hallazgo de restos óseos en el mismo predio",
        "medio": "Fiscalía de prueba", "nivel_fuente": 1, "entidad_iso": "MX-JAL",
        "municipio": "Tlajomulco de Zúñiga", "categoria_detectada": "FOS", "confianza_pct": 88,
        "resumen": f"{MARCA} Segunda publicación sintética del mismo hecho, para probar corroboración.",
        "fecha_publicacion": "2026-08-28T11:00:00-06:00",
    },
    {
        "url": "https://ejemplo.invalid/prueba/3",
        "titulo": f"{MARCA} Aseguran campamento con parapetos en zona serrana",
        "medio": "Medio de prueba estatal", "nivel_fuente": 3, "entidad_iso": "MX-MIC",
        "municipio": "Apatzingán", "categoria_detectada": "CAM", "confianza_pct": 61,
        "resumen": f"{MARCA} Registro sintético de campamento para revisar la categoría CAM.",
        "fecha_publicacion": "2026-08-28T08:30:00-06:00",
    },
    {
        "url": "https://ejemplo.invalid/prueba/4",
        "titulo": f"{MARCA} Liberan a cinco personas de una casa de seguridad",
        "medio": "Medio de prueba regional", "nivel_fuente": 4, "entidad_iso": "MX-SIN",
        "municipio": "Culiacán", "categoria_detectada": "CSE", "confianza_pct": 66,
        "resumen": f"{MARCA} Registro sintético de casa de seguridad para revisar la categoría CSE.",
        "fecha_publicacion": "2026-08-28T18:10:00-06:00",
    },
    {
        "url": "https://ejemplo.invalid/prueba/5",
        "titulo": f"{MARCA} Colectivo reporta un punto positivo de búsqueda",
        "medio": "Colectivo de prueba", "nivel_fuente": 5, "entidad_iso": "MX-VER",
        "municipio": "Veracruz", "categoria_detectada": "FOS", "confianza_pct": 44,
        "resumen": f"{MARCA} Reporte sintético de colectivo: debe quedar en nivel D.",
        "fecha_publicacion": "2026-08-29T07:00:00-06:00",
    },
    {
        "url": "https://ejemplo.invalid/prueba/6",
        "titulo": f"{MARCA} Reportan inmueble asegurado con personas privadas de la libertad",
        "medio": "Medio de prueba nacional", "nivel_fuente": 2, "entidad_iso": "MX-TAM",
        "municipio": "Reynosa", "categoria_detectada": "CSE", "confianza_pct": 58,
        "resumen": f"{MARCA} Registro sintético pendiente de validación en la bandeja.",
        "fecha_publicacion": "2026-08-29T09:15:00-06:00",
    },
]


def main() -> int:
    ruta = os.environ.get("ARGOS_DB", "")
    if not ruta or "demo" not in ruta and "prueba" not in ruta and "test" not in ruta:
        print(
            "Rechazado: fije ARGOS_DB a una base de pruebas cuyo nombre contenga "
            "«demo», «prueba» o «test». Este script inserta datos ficticios y no "
            "debe tocar una base real.",
            file=sys.stderr,
        )
        return 2

    from app import db, siembra
    from app.core import bandeja, eventos

    db.inicializar()
    siembra.sembrar_todo()

    ids = [bandeja.registrar_hallazgo(r) for r in REGISTROS]
    ids = [i for i in ids if i]
    print(f"{len(ids)} registro(s) ficticio(s) en bandeja.")

    if len(ids) >= 5:
        # Un evento con dos fuentes (medio + fiscalía) que llega a nivel A.
        r = bandeja.validar(ids[0], usuario="demo", motivo=f"{MARCA} validación de prueba")
        bandeja.vincular(ids[1], r["folio"], usuario="demo", motivo=f"{MARCA} corroboración institucional")
        eventos.actualizar_ficha(
            r["folio"], {"num_cuerpos": 3, "autoridad": "Autoridad de prueba"},
            usuario="demo", motivo=f"{MARCA} captura de cifras publicadas",
        )
        eventos.agregar_atribucion(
            r["folio"],
            {"texto": "el predio a un grupo delictivo de la región",
             "atribuido_por": "La autoridad de prueba",
             "url": "https://ejemplo.invalid/prueba/2"},
            usuario="demo",
        )
        bandeja.validar(ids[2], usuario="demo", motivo=f"{MARCA} validación de prueba")
        bandeja.validar(ids[3], usuario="demo", motivo=f"{MARCA} validación de prueba")
        bandeja.validar(ids[4], usuario="demo", motivo=f"{MARCA} validación de prueba")

    print("Eventos:", db.escalar("SELECT COUNT(*) FROM events"))
    print("Pendientes en bandeja:", db.escalar("SELECT COUNT(*) FROM raw_items WHERE estado='PENDIENTE'"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
