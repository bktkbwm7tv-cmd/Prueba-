"""Configuración de ARGOS FORENSE.

Todo valor operativo se lee del entorno con un valor por omisión explícito. Los
intervalos del programador (§26) además son configurables en caliente desde la
tabla `config`, que tiene prioridad sobre el entorno.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from zoneinfo import ZoneInfo

BASE_DIR = Path(__file__).resolve().parent
RAIZ_DIR = BASE_DIR.parent
DATOS_DIR = BASE_DIR / "datos"
WEB_DIR = RAIZ_DIR / "web"

# Hora de Ciudad de México: toda marca temporal del producto se escribe en esta
# zona, nunca en la del servidor.
TZ = ZoneInfo(os.environ.get("ARGOS_TZ", "America/Mexico_City"))


def _int(nombre: str, por_omision: int) -> int:
    try:
        return int(os.environ.get(nombre, por_omision))
    except (TypeError, ValueError):
        return por_omision


def _bool(nombre: str, por_omision: bool) -> bool:
    valor = os.environ.get(nombre)
    if valor is None:
        return por_omision
    return valor.strip().lower() in {"1", "true", "si", "sí", "yes", "on"}


@dataclass(frozen=True)
class Config:
    # --- Base de datos -----------------------------------------------------
    # DSN sqlite por omisión. La capa de repositorio está aislada para que la
    # migración a PostgreSQL/PostGIS sea un cambio de dialecto, no de código de
    # negocio (ver app/db.py y docs/migracion-postgis.md).
    db_path: Path = field(
        default_factory=lambda: Path(
            os.environ.get("ARGOS_DB", str(RAIZ_DIR / "datos" / "argos_forense.sqlite3"))
        )
    )
    almacen_evidencia: Path = field(
        default_factory=lambda: Path(
            os.environ.get("ARGOS_EVIDENCIA", str(RAIZ_DIR / "datos" / "evidencia"))
        )
    )

    # --- Programador (§26) -------------------------------------------------
    rastreo_minutos: int = field(default_factory=lambda: _int("ARGOS_RASTREO_MIN", 60))
    corte_horas: int = field(default_factory=lambda: _int("ARGOS_CORTE_HORAS", 72))
    scheduler_activo: bool = field(default_factory=lambda: _bool("ARGOS_SCHEDULER", True))
    # El corte se genera como BORRADOR y espera publicación humana salvo que se
    # active expresamente la publicación automática: un corte publicado es
    # inmutable (§16) y no debe nacer de un proceso desatendido por omisión.
    corte_autopublica: bool = field(default_factory=lambda: _bool("ARGOS_CORTE_AUTOPUBLICA", False))

    # --- Recolección -------------------------------------------------------
    http_timeout: int = field(default_factory=lambda: _int("ARGOS_HTTP_TIMEOUT", 20))
    http_reintentos: int = field(default_factory=lambda: _int("ARGOS_HTTP_REINTENTOS", 2))
    # Cortesía entre peticiones al mismo host, en segundos.
    pausa_por_host: float = field(default_factory=lambda: float(os.environ.get("ARGOS_PAUSA_HOST", "1.5")))
    respetar_robots: bool = field(default_factory=lambda: _bool("ARGOS_RESPETAR_ROBOTS", True))
    user_agent: str = field(
        default_factory=lambda: os.environ.get(
            "ARGOS_UA",
            "ARGOS-FORENSE/2.0 (rastreo OSINT institucional; contacto: administrador de la instancia)",
        )
    )
    max_items_por_fuente: int = field(default_factory=lambda: _int("ARGOS_MAX_ITEMS_FUENTE", 40))
    # Ventana en días para considerar "del corte" una publicación.
    ventana_dias: int = field(default_factory=lambda: _int("ARGOS_VENTANA_DIAS", 7))

    # --- Seguridad (§20) ---------------------------------------------------
    # Precisión máxima que la API expone sin autorización explícita. El punto
    # exacto nunca se publica automáticamente.
    exponer_punto_exacto: bool = field(default_factory=lambda: _bool("ARGOS_PUNTO_EXACTO", False))
    decimales_publicos: int = field(default_factory=lambda: _int("ARGOS_DECIMALES_PUBLICOS", 2))

    # --- Deduplicación (§12) ----------------------------------------------
    umbral_duplicado: int = field(default_factory=lambda: _int("ARGOS_UMBRAL_DUP", 60))

    # --- Servidor ----------------------------------------------------------
    host: str = field(default_factory=lambda: os.environ.get("ARGOS_HOST", "127.0.0.1"))
    port: int = field(default_factory=lambda: _int("ARGOS_PORT", 8000))


CONFIG = Config()

# Categorías del sistema (§9).
CATEGORIAS = {
    "FOS": "Fosas clandestinas",
    "CAM": "Campamentos vinculados públicamente con delincuencia organizada",
    "CSE": "Casas de seguridad",
}

# Niveles de corroboración (§11).
NIVELES_CORROBORACION = {
    "A": "CONFIRMADO — fuente institucional competente",
    "B": "ALTAMENTE CORROBORADO — dos o más fuentes independientes coincidentes",
    "C": "REPORTADO — una fuente periodística identificable",
    "D": "POR VERIFICAR — reporte inicial, colectivo o publicación sin corroboración adicional",
}

# Estados de registro (§14).
ESTADOS = ("ACTIVO", "DESCARTADO", "DUPLICADO", "FUSIONADO", "ACTUALIZADO")

NIVELES_FUENTE = {
    1: "Institucional",
    2: "Prensa nacional",
    3: "Prensa estatal",
    4: "Prensa regional y municipal",
    5: "Colectivos buscadores",
}
