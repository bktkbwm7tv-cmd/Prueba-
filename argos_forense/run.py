#!/usr/bin/env python3
"""Arranque de ARGOS FORENSE.

    python run.py                      # servidor en 127.0.0.1:8000
    python run.py --host 0.0.0.0 --port 8080
    python run.py --sembrar            # sólo crea la base y siembra catálogos
    python run.py --rastrear           # una vuelta de rastreo, sin servidor
    python run.py --corte              # genera el corte y termina
"""

from __future__ import annotations

import argparse
import json
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="ARGOS FORENSE")
    parser.add_argument("--host", default=None)
    parser.add_argument("--port", type=int, default=None)
    parser.add_argument("--sembrar", action="store_true", help="Crear la base y sembrar los catálogos.")
    parser.add_argument("--rastrear", action="store_true", help="Ejecutar una vuelta de rastreo y salir.")
    parser.add_argument("--corte", action="store_true", help="Generar el corte de 72 horas y salir.")
    parser.add_argument("--publicar", type=int, metavar="N", help="Publicar (sellar) el corte N.")
    args = parser.parse_args()

    from app import db, siembra
    from app.config import CONFIG

    db.inicializar()

    if args.sembrar:
        print(json.dumps(siembra.sembrar_todo(), ensure_ascii=False, indent=2))
        return 0
    if args.rastrear:
        siembra.sembrar_todo()
        from app.colectores import runner
        print(json.dumps(runner.rastrear(usuario="cli"), ensure_ascii=False, indent=2))
        return 0
    if args.corte:
        from app.core import cortes
        print(json.dumps(cortes.generar(usuario="cli"), ensure_ascii=False, indent=2)[:4000])
        return 0
    if args.publicar is not None:
        from app.core import cortes
        print(json.dumps(cortes.publicar(args.publicar, usuario="cli"), ensure_ascii=False, indent=2))
        return 0

    import uvicorn

    host = args.host or CONFIG.host
    port = args.port or CONFIG.port
    print(f"ARGOS FORENSE · http://{host}:{port}  ·  API: http://{host}:{port}/api/docs")
    uvicorn.run("app.main:app", host=host, port=port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
