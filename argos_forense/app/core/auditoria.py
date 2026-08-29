"""Bitácora AUDIT_LOG (§14).

Regla: cada modificación se registra, y **nada se borra físicamente**. Las
funciones de este módulo sólo insertan.
"""

from __future__ import annotations

from typing import Any, Iterable

from .. import db

PROCESO_SISTEMA = "sistema"


def registrar(
    *,
    usuario: str,
    proceso: str,
    entidad_tipo: str,
    entidad_id: Any,
    campo: str | None = None,
    valor_anterior: Any = None,
    valor_nuevo: Any = None,
    motivo: str | None = None,
    fuente_origen: str | None = None,
    evento: str | None = None,
) -> int:
    ahora = db.ahora()
    return db.insertar(
        "audit",
        {
            "ts": ahora.isoformat(timespec="seconds"),
            "fecha": ahora.date().isoformat(),
            "hora": ahora.strftime("%H:%M:%S"),
            "usuario": usuario or "desconocido",
            "proceso": proceso,
            "entidad_tipo": entidad_tipo,
            "entidad_id": str(entidad_id),
            "evento": evento,
            "campo": campo,
            "valor_anterior": None if valor_anterior is None else str(valor_anterior),
            "valor_nuevo": None if valor_nuevo is None else str(valor_nuevo),
            "motivo": motivo,
            "fuente_origen": fuente_origen,
        },
    )


def registrar_cambios(
    *,
    usuario: str,
    proceso: str,
    entidad_tipo: str,
    entidad_id: Any,
    antes: dict,
    despues: dict,
    campos: Iterable[str] | None = None,
    motivo: str | None = None,
    fuente_origen: str | None = None,
    evento: str | None = None,
) -> int:
    """Registra un renglón por campo efectivamente modificado. Devuelve cuántos."""
    campos = list(campos) if campos is not None else sorted(set(antes) | set(despues))
    n = 0
    for campo in campos:
        anterior = antes.get(campo)
        nuevo = despues.get(campo)
        if anterior == nuevo:
            continue
        registrar(
            usuario=usuario,
            proceso=proceso,
            entidad_tipo=entidad_tipo,
            entidad_id=entidad_id,
            campo=campo,
            valor_anterior=anterior,
            valor_nuevo=nuevo,
            motivo=motivo,
            fuente_origen=fuente_origen,
            evento=evento,
        )
        n += 1
    return n


def historial(entidad_tipo: str, entidad_id: Any, limite: int = 500) -> list[dict]:
    return db.consultar(
        "SELECT * FROM audit WHERE entidad_tipo = ? AND entidad_id = ? ORDER BY id DESC LIMIT ?",
        (entidad_tipo, str(entidad_id), limite),
    )


def historial_evento(folio: str, limite: int = 500) -> list[dict]:
    return db.consultar(
        "SELECT * FROM audit WHERE evento = ? OR (entidad_tipo = 'event' AND entidad_id = ?) "
        "ORDER BY id DESC LIMIT ?",
        (folio, folio, limite),
    )
