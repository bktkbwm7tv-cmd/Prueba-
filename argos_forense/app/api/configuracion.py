"""Configuración y programador (§26, menú «Configuración» de §23)."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from .. import db, scheduler
from ..config import CONFIG
from .comun import usuario_actual

router = APIRouter(tags=["configuración"])


class PeticionIntervalos(BaseModel):
    rastreo_minutos: int | None = Field(default=None, ge=5, le=1440)
    corte_horas: int | None = Field(default=None, ge=1, le=720)


@router.get("/api/scheduler")
def estado_programador() -> dict:
    return scheduler.estado()


@router.post("/api/scheduler")
def reprogramar(peticion: PeticionIntervalos, usuario: str = Depends(usuario_actual)) -> dict:
    return scheduler.reprogramar(
        rastreo_minutos=peticion.rastreo_minutos, corte_horas=peticion.corte_horas, usuario=usuario
    )


@router.get("/api/config")
def configuracion() -> dict:
    return {
        "programador": scheduler.estado(),
        "recoleccion": {
            "ventana_dias": CONFIG.ventana_dias,
            "max_items_por_fuente": CONFIG.max_items_por_fuente,
            "respetar_robots": CONFIG.respetar_robots,
            "http_timeout": CONFIG.http_timeout,
            "user_agent": CONFIG.user_agent,
        },
        "deduplicacion": {"umbral_duplicado": CONFIG.umbral_duplicado},
        "seguridad": {
            "exponer_punto_exacto": CONFIG.exponer_punto_exacto,
            "decimales_publicos": CONFIG.decimales_publicos,
            "nota": "Sólo se cambia por variable de entorno: no es un ajuste de pantalla (§20).",
        },
        "almacenamiento": {
            "base_de_datos": str(CONFIG.db_path),
            "evidencia": str(CONFIG.almacen_evidencia),
        },
        "valores_persistidos": {
            "rastreo_minutos": db.config_get("rastreo_minutos", CONFIG.rastreo_minutos),
            "corte_horas": db.config_get("corte_horas", CONFIG.corte_horas),
        },
    }
