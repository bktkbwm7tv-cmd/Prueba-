"""Aplicación FastAPI de ARGOS FORENSE.

Sirve la API de §24 y el frontend responsive de §22-§23 desde el mismo puerto,
para que la plataforma se abra en móvil, tableta o escritorio sin montar nada
más.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from . import __version__, db, scheduler, siembra
from .config import CONFIG, WEB_DIR
from .api import bandeja, catalogos, configuracion, cortes, eventos, health

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s · %(message)s",
)
log = logging.getLogger("argos")

DESCRIPCION = """
Rastreo nacional OSINT de **fosas clandestinas**, **campamentos vinculados
públicamente con delincuencia organizada** y **casas de seguridad**, con cortes
históricos cada 72 horas.

Tres reglas gobiernan toda la API:

* **Nada detectado llega solo al registro definitivo.** El rastreo deja los
  hallazgos en la bandeja de validación; el folio forense se emite al validar.
* **Nada se borra.** Los registros cambian de estado y cada movimiento queda en
  la bitácora, con usuario, motivo y fuente.
* **Lo público y lo operativo van separados.** La API no publica coordenadas
  precisas, domicilios ni datos personales, y no atribuye ningún sitio a una
  organización que ninguna fuente identificable haya nombrado.
"""


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    db.inicializar()
    resumen = siembra.sembrar_todo()
    log.info("Catálogos: %s fuente(s) y %s colectivo(s) en total.",
             resumen["fuentes"]["total"], resumen["colectivos"]["total"])
    scheduler.iniciar()
    try:
        yield
    finally:
        scheduler.detener()
        db.cerrar()


app = FastAPI(
    title="ARGOS FORENSE",
    version=__version__,
    description=DESCRIPCION,
    lifespan=ciclo_de_vida,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

for router in (health.router, bandeja.router, eventos.router, cortes.router,
               catalogos.router, configuracion.router):
    app.include_router(router)


@app.exception_handler(ValueError)
async def error_de_valor(request, exc: ValueError):  # pragma: no cover - red de seguridad
    return JSONResponse(status_code=400, content={"detail": str(exc)})


# --- Frontend ---------------------------------------------------------------
if WEB_DIR.exists():
    app.mount("/css", StaticFiles(directory=WEB_DIR / "css"), name="css")
    app.mount("/js", StaticFiles(directory=WEB_DIR / "js"), name="js")
    app.mount("/vendor", StaticFiles(directory=WEB_DIR / "vendor"), name="vendor")

    @app.get("/", include_in_schema=False)
    def inicio():
        return FileResponse(WEB_DIR / "index.html")

    @app.get("/manifest.webmanifest", include_in_schema=False)
    def manifiesto():
        return FileResponse(WEB_DIR / "manifest.webmanifest", media_type="application/manifest+json")


def ejecutar() -> None:  # pragma: no cover
    import uvicorn

    uvicorn.run("app.main:app", host=CONFIG.host, port=CONFIG.port, reload=False)


if __name__ == "__main__":  # pragma: no cover
    ejecutar()
