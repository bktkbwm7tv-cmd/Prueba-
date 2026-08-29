"""Siembra idempotente del catálogo de fuentes y colectivos.

Sólo da de alta lo que falta; nunca sobrescribe lo que un analista haya
corregido en la aplicación, porque eso perdería trabajo humano sin dejar rastro.
Cada alta queda en la bitácora (§14).
"""

from __future__ import annotations

import json

from . import db
from .config import DATOS_DIR
from .core import auditoria


def _sembrar_usuario_sistema() -> None:
    if db.consultar_uno("SELECT id FROM users WHERE usuario = ?", ("sistema",)):
        return
    db.insertar("users", {
        "usuario": "sistema", "nombre": "Proceso automático ARGOS FORENSE",
        "rol": "SISTEMA", "activo": 1, "creado_en": db.ahora_iso(),
    })


def sembrar_fuentes() -> dict:
    datos = json.loads((DATOS_DIR / "fuentes.json").read_text(encoding="utf-8"))
    altas = 0
    for f in datos["fuentes"]:
        existe = db.consultar_uno(
            "SELECT id FROM sources WHERE nombre = ? AND nivel = ? AND "
            + ("entidad_iso IS NULL" if f["entidad_iso"] is None else "entidad_iso = ?"),
            (f["nombre"], f["nivel"]) + ((f["entidad_iso"],) if f["entidad_iso"] else ()),
        )
        if existe:
            continue
        ahora = db.ahora_iso()
        sid = db.insertar("sources", {
            "nivel": f["nivel"], "nombre": f["nombre"], "ambito": f["ambito"],
            "entidad_iso": f["entidad_iso"], "tipo": f["tipo"], "url_sitio": f["url_sitio"],
            "url_rss": f["url_rss"], "dominio": f["dominio"], "clase_url": f["clase_url"],
            "verificado": 0, "rss_verificado": 0, "activo": 1,
            "estatus": "SIN VERIFICAR" if f["dominio"] else "SIN DOMINIO CANÓNICO REGISTRADO",
            "origen_registro": f["origen_registro"], "notas": f["notas"],
            "creado_en": ahora, "actualizado_en": ahora,
        })
        auditoria.registrar(
            usuario="sistema", proceso="siembra", entidad_tipo="source", entidad_id=sid,
            campo="alta", valor_anterior=None, valor_nuevo=f["nombre"],
            motivo=f"Catálogo semilla nivel {f['nivel']}", fuente_origen=f["origen_registro"],
        )
        altas += 1
    return {"altas": altas, "total": db.escalar("SELECT COUNT(*) FROM sources")}


def sembrar_colectivos() -> dict:
    datos = json.loads((DATOS_DIR / "colectivos.json").read_text(encoding="utf-8"))
    altas = 0
    for c in datos["colectivos"]:
        existe = db.consultar_uno("SELECT id FROM collectives WHERE nombre = ?", (c["nombre"],))
        if existe:
            continue
        ahora = db.ahora_iso()
        cid = db.insertar("collectives", {
            "nombre": c["nombre"], "entidad_iso": c["entidad_iso"], "municipio_base": c["municipio_base"],
            "url_web": None, "url_facebook": None, "url_instagram": None, "url_x": None, "url_tiktok": None,
            "otras_paginas": db.js([]), "fecha_ultima_revision": None,
            "estatus_fuente": "SIN VERIFICAR",
            "activo": 1,
            "notas": "Alta semilla: confirme nombre, entidad, municipio base y páginas públicas antes de "
                     "usarlo como fuente. §20: no se registran domicilios ni teléfonos.",
            "creado_en": ahora, "actualizado_en": ahora,
        })
        auditoria.registrar(
            usuario="sistema", proceso="siembra", entidad_tipo="collective", entidad_id=cid,
            campo="alta", valor_anterior=None, valor_nuevo=c["nombre"],
            motivo="Catálogo semilla nivel 5 — sin verificar",
        )
        altas += 1
    return {"altas": altas, "total": db.escalar("SELECT COUNT(*) FROM collectives")}


def sembrar_todo() -> dict:
    db.inicializar()
    _sembrar_usuario_sistema()
    return {"fuentes": sembrar_fuentes(), "colectivos": sembrar_colectivos()}


if __name__ == "__main__":  # pragma: no cover
    print(json.dumps(sembrar_todo(), ensure_ascii=False, indent=2))
