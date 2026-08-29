"""GET /api/health — estado del sistema, sin adornos."""

from __future__ import annotations

from fastapi import APIRouter

from .. import __version__, db
from ..config import CATEGORIAS, CONFIG, NIVELES_CORROBORACION
from ..core import cortes

router = APIRouter(tags=["salud"])


@router.get("/api/health")
def health() -> dict:
    try:
        db.escalar("SELECT 1")
        base_ok = True
        detalle_base = None
    except Exception as exc:  # pragma: no cover - sólo si la base está rota
        base_ok, detalle_base = False, f"{type(exc).__name__}: {exc}"

    borrador = cortes.borrador_abierto()
    publicado = cortes.ultimo_publicado()
    return {
        "sistema": "ARGOS FORENSE",
        "version": __version__,
        "estado": "OK" if base_ok else "DEGRADADO",
        "hora_cdmx": db.ahora_iso(),
        "base_de_datos": {
            "motor": db.DIALECTO,
            "ruta": str(CONFIG.db_path),
            "accesible": base_ok,
            "detalle": detalle_base,
            "eventos": db.escalar("SELECT COUNT(*) FROM events") if base_ok else None,
            "bandeja_pendiente": db.escalar("SELECT COUNT(*) FROM raw_items WHERE estado='PENDIENTE'") if base_ok else None,
        },
        "programador": {
            "activo": CONFIG.scheduler_activo,
            "rastreo_minutos": int(db.config_get("rastreo_minutos", CONFIG.rastreo_minutos)) if base_ok else CONFIG.rastreo_minutos,
            "corte_horas": int(db.config_get("corte_horas", CONFIG.corte_horas)) if base_ok else CONFIG.corte_horas,
            "corte_autopublica": CONFIG.corte_autopublica,
            "ultimo_rastreo": (db.config_get("ultimo_rastreo") or {}).get("fin") if base_ok else None,
        },
        "cortes": {
            "borrador_abierto": borrador["etiqueta"] if borrador else None,
            "ultimo_publicado": publicado["etiqueta"] if publicado else None,
        },
        "catalogos": {"categorias": CATEGORIAS, "niveles_corroboracion": NIVELES_CORROBORACION},
        "seguridad": {
            "expone_punto_exacto": CONFIG.exponer_punto_exacto,
            "nota": "Por omisión la API no publica coordenadas precisas ni datos personales (§20).",
        },
    }
