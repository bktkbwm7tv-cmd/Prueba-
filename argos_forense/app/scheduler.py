"""Programador automático (§26).

Dos tareas, ambas con intervalo configurable en caliente:
  · RASTREO cada 60 minutos;
  · CORTE cada 72 horas.

El corte se **genera**; publicarlo es un acto humano salvo que se active
`ARGOS_CORTE_AUTOPUBLICA`. Un corte publicado es inmutable (§16) y no debe nacer
de un proceso desatendido por omisión.
"""

from __future__ import annotations

import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from . import db
from .colectores import runner
from .config import CONFIG, TZ
from .core import auditoria, cortes

log = logging.getLogger("argos.scheduler")

_scheduler: BackgroundScheduler | None = None
ID_RASTREO = "rastreo"
ID_CORTE = "corte"


def _intervalo_rastreo() -> int:
    return max(1, int(db.config_get("rastreo_minutos", CONFIG.rastreo_minutos)))


def _intervalo_corte() -> int:
    return max(1, int(db.config_get("corte_horas", CONFIG.corte_horas)))


def tarea_rastreo() -> None:
    try:
        resultado = runner.rastrear(usuario="sistema")
        log.info(
            "Rastreo: %s consulta(s), %s alta(s) en bandeja, %s fuente(s) con error",
            resultado["consultas"], resultado["altas_en_bandeja"], resultado["fuentes_con_error"],
        )
    except Exception as exc:  # pragma: no cover - el programador no debe morir
        log.exception("Rastreo fallido: %s", exc)
        auditoria.registrar(
            usuario="sistema", proceso="rastreo", entidad_tipo="config", entidad_id="scheduler",
            campo="error", valor_nuevo=f"{type(exc).__name__}: {exc}"[:500],
            motivo="Fallo del rastreo programado",
        )


def tarea_corte() -> None:
    try:
        if cortes.borrador_abierto():
            log.info("Corte no generado: ya existe un borrador sin publicar.")
            auditoria.registrar(
                usuario="sistema", proceso="corte", entidad_tipo="cut", entidad_id="programado",
                campo="generacion", valor_nuevo="omitida",
                motivo="Ya existe un corte en borrador sin publicar; no se genera otro encima.",
            )
            return
        corte = cortes.generar(usuario="sistema")
        log.info("Corte generado: %s (borrador)", corte["etiqueta"])
        if CONFIG.corte_autopublica:
            cortes.publicar(corte["numero"], usuario="sistema")
            log.info("Corte %s publicado automáticamente y sellado.", corte["numero"])
    except Exception as exc:  # pragma: no cover
        log.exception("Corte fallido: %s", exc)
        auditoria.registrar(
            usuario="sistema", proceso="corte", entidad_tipo="cut", entidad_id="programado",
            campo="error", valor_nuevo=f"{type(exc).__name__}: {exc}"[:500],
            motivo="Fallo de la generación programada del corte",
        )


def iniciar() -> BackgroundScheduler | None:
    global _scheduler
    if not CONFIG.scheduler_activo:
        log.info("Programador desactivado por configuración (ARGOS_SCHEDULER=0).")
        return None
    if _scheduler is not None:
        return _scheduler
    _scheduler = BackgroundScheduler(timezone=TZ)
    _scheduler.add_job(
        tarea_rastreo, IntervalTrigger(minutes=_intervalo_rastreo()), id=ID_RASTREO,
        name="Rastreo OSINT", max_instances=1, coalesce=True, replace_existing=True,
    )
    _scheduler.add_job(
        tarea_corte, IntervalTrigger(hours=_intervalo_corte()), id=ID_CORTE,
        name="Generación del corte de 72 horas", max_instances=1, coalesce=True, replace_existing=True,
    )
    _scheduler.start()
    log.info("Programador iniciado: rastreo cada %s min, corte cada %s h",
             _intervalo_rastreo(), _intervalo_corte())
    return _scheduler


def detener() -> None:
    global _scheduler
    if _scheduler is not None:
        _scheduler.shutdown(wait=False)
        _scheduler = None


def reprogramar(*, rastreo_minutos: int | None = None, corte_horas: int | None = None,
                usuario: str = "sistema") -> dict:
    """Cambia los intervalos en caliente y los persiste (§26)."""
    if rastreo_minutos is not None:
        db.config_set("rastreo_minutos", int(rastreo_minutos), usuario)
        auditoria.registrar(
            usuario=usuario, proceso="configuracion", entidad_tipo="config", entidad_id="rastreo_minutos",
            campo="rastreo_minutos", valor_nuevo=str(rastreo_minutos), motivo="Cambio de intervalo de rastreo",
        )
    if corte_horas is not None:
        db.config_set("corte_horas", int(corte_horas), usuario)
        auditoria.registrar(
            usuario=usuario, proceso="configuracion", entidad_tipo="config", entidad_id="corte_horas",
            campo="corte_horas", valor_nuevo=str(corte_horas), motivo="Cambio de periodicidad del corte",
        )
    if _scheduler is not None:
        if rastreo_minutos is not None:
            _scheduler.reschedule_job(ID_RASTREO, trigger=IntervalTrigger(minutes=int(rastreo_minutos)))
        if corte_horas is not None:
            _scheduler.reschedule_job(ID_CORTE, trigger=IntervalTrigger(hours=int(corte_horas)))
    return estado()


def estado() -> dict:
    if _scheduler is None:
        return {
            "activo": False,
            "rastreo_minutos": _intervalo_rastreo(),
            "corte_horas": _intervalo_corte(),
            "tareas": [],
            "nota": "El programador no está corriendo en este proceso.",
        }
    return {
        "activo": True,
        "rastreo_minutos": _intervalo_rastreo(),
        "corte_horas": _intervalo_corte(),
        "corte_autopublica": CONFIG.corte_autopublica,
        "tareas": [
            {"id": j.id, "nombre": j.name,
             "proxima_ejecucion": j.next_run_time.isoformat() if j.next_run_time else None}
            for j in _scheduler.get_jobs()
        ],
    }
