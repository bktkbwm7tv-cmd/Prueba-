"""Bandeja de validación (§8, §24).

Endpoints:
  POST /api/collect
  GET  /api/inbox
  GET  /api/inbox/{id}
  GET  /api/inbox/{id}/duplicates
  POST /api/inbox/{id}/validate
  POST /api/inbox/{id}/reject
  POST /api/inbox/{id}/link
  POST /api/inbox/duplicates/{id}/resolve
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from ..colectores import runner
from ..core import bandeja as bandeja_core
from ..core import eventos as eventos_core
from ..core import folio as folio_mod
from .comun import paginacion, usuario_actual

router = APIRouter(tags=["bandeja"])


class PeticionRastreo(BaseModel):
    incluir_rss: bool = True
    incluir_busqueda: bool = True
    incluir_portales: bool = Field(
        default=False,
        description="Lectura directa de portales institucionales. Cara y dependiente del egreso de red.",
    )
    entidades: list[str] | None = Field(default=None, description="ISO 3166-2, p. ej. MX-JAL.")
    categorias: list[str] | None = Field(default=None, description="FOS, CAM y/o CSE.")
    limite_consultas: int | None = Field(default=None, ge=1, le=2000)


class PeticionValidar(BaseModel):
    entidad_iso: str | None = None
    categoria: str | None = None
    municipio: str | None = None
    localidad: str | None = None
    subcategoria: str | None = None
    resumen_factual: str | None = None
    fecha_probable_evento: str | None = None
    motivo: str = "Validado en bandeja"


class PeticionDescartar(BaseModel):
    motivo: str = Field(..., min_length=3)


class PeticionVincular(BaseModel):
    folio: str
    tipo_aporte: str = Field(default="CORROBORACION", pattern="^(ORIGEN|CORROBORACION|ACTUALIZACION)$")
    motivo: str = "Vinculado desde bandeja"


class PeticionDuplicado(BaseModel):
    decision: str = Field(..., pattern="^(FUSIONAR|MANTENER_SEPARADOS|VINCULAR)$")
    motivo: str = Field(..., min_length=3)


@router.post("/api/collect")
def collect(peticion: PeticionRastreo | None = None, usuario: str = Depends(usuario_actual)) -> dict:
    """Dispara una vuelta de rastreo. Nada de lo recogido se convierte en evento (§4)."""
    p = peticion or PeticionRastreo()
    return runner.rastrear(
        usuario=usuario,
        incluir_rss=p.incluir_rss,
        incluir_busqueda=p.incluir_busqueda,
        incluir_portales=p.incluir_portales,
        entidades_iso=tuple(p.entidades) if p.entidades else None,
        categorias=tuple(c.upper() for c in p.categorias) if p.categorias else None,
        limite_consultas=p.limite_consultas,
    )


@router.get("/api/inbox")
def inbox(
    estado: str | None = Query(default="PENDIENTE"),
    categoria: str | None = None,
    entidad: str | None = None,
    confianza_min: int | None = Query(default=None, ge=0, le=100),
    q: str | None = None,
    limite: int = Query(default=100, ge=1, le=1000),
    desplazamiento: int = Query(default=0, ge=0),
) -> dict:
    limite, desplazamiento = paginacion(limite, desplazamiento)
    return bandeja_core.listar(
        estado=estado, categoria=categoria, entidad_iso=entidad,
        confianza_min=confianza_min, q=q, limite=limite, desplazamiento=desplazamiento,
    )


@router.get("/api/inbox/{raw_id}")
def inbox_detalle(raw_id: int) -> dict:
    item = bandeja_core.obtener(raw_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"No existe el registro {raw_id} en la bandeja.")
    return item


@router.get("/api/inbox/{raw_id}/duplicates")
def inbox_duplicados(raw_id: int, umbral: int | None = Query(default=None, ge=0, le=100)) -> dict:
    try:
        return bandeja_core.duplicados(raw_id, umbral=umbral)
    except bandeja_core.ErrorBandeja as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/api/inbox/{raw_id}/validate")
def inbox_validar(raw_id: int, peticion: PeticionValidar, usuario: str = Depends(usuario_actual)) -> dict:
    datos = peticion.model_dump(exclude_none=True)
    motivo = datos.pop("motivo", "Validado en bandeja")
    try:
        return bandeja_core.validar(raw_id, usuario=usuario, motivo=motivo, **datos)
    except (bandeja_core.ErrorBandeja, eventos_core.ErrorEvento, folio_mod.FolioInvalido) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/inbox/{raw_id}/reject")
def inbox_descartar(raw_id: int, peticion: PeticionDescartar, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return bandeja_core.descartar(raw_id, usuario=usuario, motivo=peticion.motivo)
    except bandeja_core.ErrorBandeja as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/inbox/{raw_id}/link")
def inbox_vincular(raw_id: int, peticion: PeticionVincular, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return bandeja_core.vincular(
            raw_id, peticion.folio, usuario=usuario, motivo=peticion.motivo, tipo_aporte=peticion.tipo_aporte
        )
    except (bandeja_core.ErrorBandeja, eventos_core.ErrorEvento) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/inbox/{raw_id}/possible-duplicate")
def inbox_posible_duplicado(raw_id: int, peticion: PeticionDescartar, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return bandeja_core.marcar_posible_duplicado(raw_id, usuario=usuario, motivo=peticion.motivo)
    except bandeja_core.ErrorBandeja as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/api/inbox/duplicates/{candidato_id}/resolve")
def resolver_duplicado(candidato_id: int, peticion: PeticionDuplicado, usuario: str = Depends(usuario_actual)) -> dict:
    try:
        return bandeja_core.resolver_duplicado(
            candidato_id, peticion.decision, usuario=usuario, motivo=peticion.motivo
        )
    except bandeja_core.ErrorBandeja as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
