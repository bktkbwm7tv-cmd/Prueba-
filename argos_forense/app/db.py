"""Acceso a datos de ARGOS FORENSE.

Toda consulta SQL del sistema pasa por aquí. Es deliberado: el motor inicial es
SQLite (§1) y la migración prevista es PostgreSQL/PostGIS, así que el resto del
código no debe conocer el dialecto. Lo específico del motor vive en tres sitios
y sólo en tres: `conectar()`, `adaptar_sql()` y `ahora_iso()`.
"""

from __future__ import annotations

import json
import re
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

from .config import CONFIG, TZ

_local = threading.local()
_ESQUEMA = Path(__file__).resolve().parent / "schema.sql"


# --------------------------------------------------------------------- tiempo
def ahora() -> datetime:
    """Hora de Ciudad de México. Ninguna marca del sistema usa otra."""
    return datetime.now(TZ)


def ahora_iso() -> str:
    return ahora().isoformat(timespec="seconds")


def hoy_iso() -> str:
    return ahora().date().isoformat()


# ---------------------------------------------------------------- dialecto --
DIALECTO = "sqlite"


def adaptar_sql(sql: str) -> str:
    """Punto único de traducción de dialecto.

    Con SQLite devuelve el SQL tal cual. Al migrar, aquí se convierten los
    marcadores `?` en `%s` y se ajustan las funciones de fecha; el código de
    negocio no cambia.
    """
    if DIALECTO == "sqlite":
        return sql
    return re.sub(r"\?", "%s", sql)  # pragma: no cover - ruta de migración


# --------------------------------------------------------------- conexión ---
def _crear_conexion() -> sqlite3.Connection:
    ruta = Path(CONFIG.db_path)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(ruta, timeout=30, check_same_thread=False)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA journal_mode = WAL")
    con.execute("PRAGMA synchronous = NORMAL")
    return con


def conectar() -> sqlite3.Connection:
    """Conexión por hilo. FastAPI atiende en varios hilos y el scheduler en uno propio."""
    con = getattr(_local, "con", None)
    if con is None:
        con = _crear_conexion()
        _local.con = con
    return con


def cerrar() -> None:
    con = getattr(_local, "con", None)
    if con is not None:
        con.close()
        _local.con = None


@contextmanager
def transaccion() -> Iterator[sqlite3.Connection]:
    con = conectar()
    try:
        yield con
    except Exception:
        con.rollback()
        raise
    else:
        con.commit()


# ------------------------------------------------------------------ helpers --
def consultar(sql: str, params: Sequence[Any] = ()) -> list[dict]:
    cur = conectar().execute(adaptar_sql(sql), tuple(params))
    filas = [dict(f) for f in cur.fetchall()]
    cur.close()
    return filas


def consultar_uno(sql: str, params: Sequence[Any] = ()) -> dict | None:
    filas = consultar(sql, params)
    return filas[0] if filas else None


def escalar(sql: str, params: Sequence[Any] = (), por_omision: Any = 0) -> Any:
    fila = consultar_uno(sql, params)
    if not fila:
        return por_omision
    valor = next(iter(fila.values()))
    return por_omision if valor is None else valor


def ejecutar(sql: str, params: Sequence[Any] = ()) -> int:
    """INSERT/UPDATE. Devuelve el id insertado o el número de filas afectadas."""
    with transaccion() as con:
        cur = con.execute(adaptar_sql(sql), tuple(params))
        resultado = cur.lastrowid if cur.lastrowid else cur.rowcount
        cur.close()
        return int(resultado or 0)


def ejecutar_muchos(sql: str, filas: Iterable[Sequence[Any]]) -> int:
    with transaccion() as con:
        cur = con.executemany(adaptar_sql(sql), [tuple(f) for f in filas])
        n = cur.rowcount
        cur.close()
        return int(n or 0)


def insertar(tabla: str, datos: dict) -> int:
    campos = list(datos)
    marcadores = ", ".join("?" for _ in campos)
    sql = f"INSERT INTO {tabla} ({', '.join(campos)}) VALUES ({marcadores})"
    return ejecutar(sql, [datos[c] for c in campos])


def actualizar(tabla: str, datos: dict, donde: str, params: Sequence[Any]) -> int:
    asignaciones = ", ".join(f"{c} = ?" for c in datos)
    sql = f"UPDATE {tabla} SET {asignaciones} WHERE {donde}"
    return ejecutar(sql, [*datos.values(), *params])


def js(valor: Any) -> str | None:
    """Serializa a JSON para columnas TEXT. En PostgreSQL pasarían a JSONB."""
    if valor is None:
        return None
    return json.dumps(valor, ensure_ascii=False)


def dejs(valor: Any, por_omision: Any = None) -> Any:
    if not valor:
        return por_omision
    if isinstance(valor, (dict, list)):
        return valor
    try:
        return json.loads(valor)
    except (TypeError, ValueError):
        return por_omision


# ------------------------------------------------------------------ esquema --
def inicializar() -> None:
    con = conectar()
    con.executescript(_ESQUEMA.read_text(encoding="utf-8"))
    con.commit()


def config_get(clave: str, por_omision: Any = None) -> Any:
    fila = consultar_uno("SELECT valor FROM config WHERE clave = ?", (clave,))
    if fila is None:
        return por_omision
    return dejs(fila["valor"], fila["valor"])


def config_set(clave: str, valor: Any, usuario: str = "sistema") -> None:
    ejecutar(
        "INSERT INTO config (clave, valor, actualizado_en, actualizado_por) VALUES (?,?,?,?) "
        "ON CONFLICT(clave) DO UPDATE SET valor = excluded.valor, "
        "actualizado_en = excluded.actualizado_en, actualizado_por = excluded.actualizado_por",
        (clave, js(valor), ahora_iso(), usuario),
    )
