"""Piezas compartidas por los routers: identidad del operador y errores."""

from __future__ import annotations

from fastapi import Header, HTTPException
from pydantic import BaseModel, Field

from .. import db


class ErrorRespuesta(BaseModel):
    detalle: str


def usuario_actual(
    x_argos_usuario: str | None = Header(default=None, alias="X-ARGOS-Usuario"),
    x_argos_token: str | None = Header(default=None, alias="X-ARGOS-Token"),
) -> str:
    """Identidad del operador para la bitácora (§14).

    Si hay usuarios con token registrados, el token manda. Si no hay ninguno
    —instalación de un solo puesto—, se acepta la cabecera de usuario y, en su
    defecto, se registra `anonimo`: la bitácora nunca queda sin autor.
    """
    if x_argos_token:
        fila = db.consultar_uno(
            "SELECT usuario FROM users WHERE token = ? AND activo = 1", (x_argos_token,)
        )
        if not fila:
            raise HTTPException(status_code=401, detail="Token no reconocido.")
        return fila["usuario"]
    if db.escalar("SELECT COUNT(*) FROM users WHERE token IS NOT NULL AND activo = 1"):
        raise HTTPException(
            status_code=401,
            detail="Esta instalación exige token: envíe la cabecera X-ARGOS-Token.",
        )
    nombre = (x_argos_usuario or "").strip()
    return nombre or "anonimo"


class ConMotivo(BaseModel):
    motivo: str = Field(..., min_length=3, description="Obligatorio: queda en la bitácora (§14).")


def paginacion(limite: int, desplazamiento: int, tope: int = 1000) -> tuple[int, int]:
    return max(1, min(limite, tope)), max(0, desplazamiento)
