"""Eventos y fichas (§10, §13, §24)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from ..core import eventos as core
from ..core import seguridad
from .comun import paginacion, usuario_actual

router = APIRouter(tags=["eventos"])


class PeticionEdicion(BaseModel):
    cambios: dict = Field(..., description=f"Campos editables: {', '.join(sorted(core.CAMPOS_EDITABLES))}")
    motivo: str = Field(..., min_length=3)


class PeticionEstado(BaseModel):
    estado: str = Field(..., pattern="^(ACTIVO|DESCARTADO|DUPLICADO|FUSIONADO|ACTUALIZADO)$")
    motivo: str = Field(..., min_length=3)
    fusionado_en: str | None = None


class PeticionFusion(BaseModel):
    folio_destino: str
    motivo: str = Field(..., min_length=3)


class PeticionAtribucion(BaseModel):
    texto: str = Field(..., min_length=3)
    atribuido_por: str = Field(..., min_length=3, description="Quién hizo la atribución (§21).")
    url: str = Field(..., min_length=8, description="Dónde consta (§21).")


@router.get("/api/events")
def listar(
    entidad: str | None = None,
    categoria: str | None = None,
    nivel: str | None = Query(default=None, pattern="^[ABCD]$"),
    estado: str | None = "ACTIVO",
    desde: str | None = None,
    hasta: str | None = None,
    q: str | None = None,
    limite: int = Query(default=200, ge=1, le=1000),
    desplazamiento: int = Query(default=0, ge=0),
) -> dict:
    limite, desplazamiento = paginacion(limite, desplazamiento)
    return core.listar(
        entidad_iso=entidad, categoria=categoria, nivel=nivel, estado=estado,
        desde=desde, hasta=hasta, q=q, limite=limite, desplazamiento=desplazamiento,
    )


@router.get("/api/events/{folio}")
def ficha(folio: str) -> dict:
    resultado = core.ficha(folio)
    if not resultado:
        raise HTTPException(status_code=404, detail=f"No existe el evento {folio}.")
    return resultado


@router.patch("/api/events/{folio}")
def editar(folio: str, peticion: PeticionEdicion, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return core.actualizar_ficha(folio, peticion.cambios, usuario=usuario, motivo=peticion.motivo)
    except core.ErrorEvento as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/events/{folio}/state")
def cambiar_estado(folio: str, peticion: PeticionEstado, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return core.cambiar_estado(
            folio, peticion.estado, usuario=usuario, motivo=peticion.motivo, fusionado_en=peticion.fusionado_en
        )
    except core.ErrorEvento as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/events/{folio}/merge")
def fusionar(folio: str, peticion: PeticionFusion, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return core.fusionar(folio, peticion.folio_destino, usuario=usuario, motivo=peticion.motivo)
    except core.ErrorEvento as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/events/{folio}/attribution")
def atribuir(folio: str, peticion: PeticionAtribucion, usuario: str = Depends(usuario_actual)) -> dict:
    """§21: el sistema nunca infiere autoría; sólo registra atribuciones ajenas con su fuente."""
    try:
        return core.agregar_atribucion(folio, peticion.model_dump(), usuario=usuario)
    except seguridad.AtribucionInvalida as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except core.ErrorEvento as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/api/events/{folio}/sources")
def fuentes(folio: str) -> dict:
    if not core.obtener(folio):
        raise HTTPException(status_code=404, detail=f"No existe el evento {folio}.")
    return {"folio": folio, "fuentes": core.fuentes(folio)}


@router.post("/api/events/{folio}/recompute-level")
def recalcular(folio: str, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return core.recalcular_nivel(folio, usuario=usuario, motivo="Recálculo solicitado")
    except core.ErrorEvento as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
