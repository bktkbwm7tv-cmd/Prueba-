"""Cada prueba corre sobre una base propia y vacía: nunca sobre la del sistema."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[1]
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))


@pytest.fixture()
def entorno(tmp_path, monkeypatch):
    monkeypatch.setenv("ARGOS_DB", str(tmp_path / "prueba.sqlite3"))
    monkeypatch.setenv("ARGOS_EVIDENCIA", str(tmp_path / "evidencia"))
    monkeypatch.setenv("ARGOS_SCHEDULER", "0")

    from app import config as config_mod
    importlib.reload(config_mod)
    from app import db as db_mod
    importlib.reload(db_mod)
    for nombre in list(sys.modules):
        if nombre.startswith("app.") and nombre not in ("app.config", "app.db"):
            importlib.reload(sys.modules[nombre])

    db_mod.cerrar()
    db_mod.inicializar()
    from app import siembra
    siembra.sembrar_todo()
    yield db_mod
    db_mod.cerrar()


@pytest.fixture()
def cliente(entorno):
    from fastapi.testclient import TestClient
    from app import main
    import importlib
    importlib.reload(main)
    with TestClient(main.app) as c:
        yield c


@pytest.fixture()
def hallazgo(entorno):
    """Un registro en bandeja, como lo dejaría el rastreo."""
    from app.core import bandeja

    def crear(**kwargs):
        datos = {
            "url": "https://ejemplo.mx/nota/fosa-tlajomulco",
            "titulo": "Localizan fosa clandestina con tres cuerpos en Tlajomulco, Jalisco",
            "medio": "Medio de prueba",
            "nivel_fuente": 3,
            "fecha_publicacion": "2026-08-28T10:00:00-06:00",
            "categoria_detectada": "FOS",
            "entidad_iso": "MX-JAL",
            "municipio": "Tlajomulco de Zúñiga",
            "resumen": "Un colectivo de búsqueda localizó restos óseos en un predio.",
            "confianza_pct": 70,
        }
        datos.update(kwargs)
        return bandeja.registrar_hallazgo(datos)

    return crear
