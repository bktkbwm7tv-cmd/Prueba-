"""Cortes de 72 horas (§16, §17, §18, §24)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from pydantic import BaseModel, Field

from ..core import cortes as core
from ..core import exportacion
from .comun import usuario_actual

router = APIRouter(tags=["cortes"])


class PeticionGenerar(BaseModel):
    horas: int | None = Field(default=None, ge=1, le=720)


class PeticionPublicar(BaseModel):
    numero: int | None = Field(default=None, description="Si se omite, se publica el borrador abierto.")


@router.get("/api/cuts")
def listar(limite: int = Query(default=100, ge=1, le=500)) -> dict:
    return {"cortes": core.listar(limite)}


@router.get("/api/cuts/{numero}")
def obtener(numero: int) -> dict:
    corte = core.obtener(numero)
    if not corte:
        raise HTTPException(status_code=404, detail=f"No existe el corte {numero}.")
    return corte


@router.post("/api/cuts/generate")
def generar(peticion: PeticionGenerar | None = None, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return core.generar(usuario=usuario, horas=(peticion.horas if peticion else None))
    except core.ErrorCorte as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.post("/api/cuts/publish")
def publicar(peticion: PeticionPublicar | None = None, usuario: str = Depends(usuario_actual)) -> dict:
    numero = peticion.numero if peticion and peticion.numero else None
    if numero is None:
        borrador = core.borrador_abierto()
        if not borrador:
            raise HTTPException(status_code=404, detail="No hay ningún corte en borrador que publicar.")
        numero = borrador["numero"]
    try:
        return core.publicar(numero, usuario=usuario)
    except core.CorteInmutable as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except core.ErrorCorte as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/api/cuts/{numero}/verify")
def verificar(numero: int) -> dict:
    try:
        return core.verificar_sello(numero)
    except core.ErrorCorte as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/api/cuts/{numero}/compare/{otro}")
def comparar(numero: int, otro: int) -> dict:
    try:
        return core.comparar_cortes(numero, otro)
    except core.ErrorCorte as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/api/cuts/{numero}/export.pdf")
def exportar_pdf(numero: int) -> Response:
    try:
        pdf = exportacion.corte_a_pdf(numero)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=501, detail=str(exc)) from exc
    return Response(
        content=pdf, media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="argos-forense-corte-{numero:03d}.pdf"'},
    )
