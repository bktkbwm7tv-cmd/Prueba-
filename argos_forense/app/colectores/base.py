"""Cliente HTTP común: cortesía, robots.txt y registro honesto del fallo.

Dos decisiones que no son de conveniencia:
  · se respeta `robots.txt` salvo que se desactive expresamente por
    configuración («scraping únicamente cuando esté permitido», §1);
  · un fallo de red se **registra tal cual** en el catálogo de fuentes. Un
    portal que no se pudo consultar no es un portal sin novedades.
"""

from __future__ import annotations

import threading
import time
import urllib.robotparser
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urljoin, urlparse

import requests

from ..config import CONFIG, TZ

_ultimo_acceso: dict[str, float] = {}
_robots: dict[str, tuple[urllib.robotparser.RobotFileParser | None, float]] = {}
_candado = threading.Lock()

# Diagnósticos que el sistema distingue: no es lo mismo un portal sin novedades
# que uno inaccesible, y no es lo mismo un 404 que un bloqueo de egreso.
SIN_NOVEDAD = "SIN RESULTADO EN VENTANA"
EGRESO_BLOQUEADO = "EGRESO BLOQUEADO POR POLÍTICA DE RED"
PORTAL_NO_DISPONIBLE = "PORTAL NO DISPONIBLE"
ROBOTS_PROHIBE = "ROBOTS.TXT PROHÍBE LA CONSULTA"


@dataclass
class Respuesta:
    ok: bool
    url: str
    estado: str
    texto: str = ""
    contenido: bytes = b""
    codigo: int | None = None
    error: str | None = None
    diagnostico: str | None = None


def _host(url: str) -> str:
    return (urlparse(url).netloc or "").lower()


def _sesion() -> requests.Session:
    sesion = getattr(_sesion, "_s", None)
    if sesion is None:
        sesion = requests.Session()
        sesion.headers.update({
            "User-Agent": CONFIG.user_agent,
            "Accept-Language": "es-MX,es;q=0.9",
        })
        _sesion._s = sesion  # type: ignore[attr-defined]
    return sesion


def permitido_por_robots(url: str) -> tuple[bool, str]:
    """Consulta robots.txt del host. Si no se puede leer, se permite y se anota.

    Un robots.txt inalcanzable no es una prohibición; tratarlo como tal
    paralizaría el rastreo por un fallo de red ajeno al permiso.
    """
    if not CONFIG.respetar_robots:
        return True, "verificación de robots desactivada por configuración"
    host = _host(url)
    if not host:
        return False, "URL sin host"
    with _candado:
        cacheado = _robots.get(host)
    ahora = time.time()
    if cacheado and ahora - cacheado[1] < 3600:
        parser = cacheado[0]
    else:
        parser = urllib.robotparser.RobotFileParser()
        robots_url = urljoin(f"{urlparse(url).scheme}://{host}", "/robots.txt")
        try:
            r = _sesion().get(robots_url, timeout=CONFIG.http_timeout)
            if r.status_code >= 400:
                parser = None
            else:
                parser.parse(r.text.splitlines())
        except requests.RequestException:
            parser = None
        with _candado:
            _robots[host] = (parser, ahora)
    if parser is None:
        return True, "robots.txt no disponible; se procede con cortesía"
    permitido = parser.can_fetch(CONFIG.user_agent, url)
    return permitido, "robots.txt consultado"


def _esperar_turno(host: str) -> None:
    with _candado:
        ultimo = _ultimo_acceso.get(host, 0.0)
        espera = CONFIG.pausa_por_host - (time.time() - ultimo)
    if espera > 0:
        time.sleep(espera)
    with _candado:
        _ultimo_acceso[host] = time.time()


def _diagnosticar(exc: Exception) -> str:
    texto = f"{type(exc).__name__}: {exc}"
    marcas = ("407", "403 Forbidden", "CONNECT tunnel failed", "ProxyError", "Tunnel connection failed")
    if any(m.lower() in texto.lower() for m in marcas):
        return EGRESO_BLOQUEADO
    return PORTAL_NO_DISPONIBLE


def obtener(url: str, *, binario: bool = False) -> Respuesta:
    """GET con reintentos, cortesía por host y comprobación de robots."""
    permitido, nota = permitido_por_robots(url)
    if not permitido:
        return Respuesta(ok=False, url=url, estado=ROBOTS_PROHIBE, diagnostico=nota,
                         error="La consulta está prohibida por robots.txt del sitio.")
    host = _host(url)
    ultimo_error: Exception | None = None
    for intento in range(CONFIG.http_reintentos + 1):
        _esperar_turno(host)
        try:
            r = _sesion().get(url, timeout=CONFIG.http_timeout, allow_redirects=True)
            if r.status_code >= 500 and intento < CONFIG.http_reintentos:
                time.sleep(1.5 * (intento + 1))
                continue
            if r.status_code >= 400:
                return Respuesta(ok=False, url=url, estado=PORTAL_NO_DISPONIBLE, codigo=r.status_code,
                                 error=f"HTTP {r.status_code}", diagnostico=nota)
            return Respuesta(ok=True, url=r.url, estado="OK", codigo=r.status_code,
                             texto="" if binario else r.text, contenido=r.content, diagnostico=nota)
        except requests.RequestException as exc:
            ultimo_error = exc
            if intento < CONFIG.http_reintentos:
                time.sleep(1.5 * (intento + 1))
    diag = _diagnosticar(ultimo_error) if ultimo_error else PORTAL_NO_DISPONIBLE
    return Respuesta(ok=False, url=url, estado=diag, error=str(ultimo_error)[:300], diagnostico=nota)


# ------------------------------------------------------------------ fechas --
def normalizar_fecha(valor) -> str | None:
    """Devuelve ISO-8601 en hora de CDMX, o None. Nunca inventa una fecha."""
    if not valor:
        return None
    if isinstance(valor, datetime):
        dt = valor
    elif isinstance(valor, time.struct_time):
        dt = datetime(*valor[:6], tzinfo=timezone.utc)
    else:
        texto = str(valor).strip()
        dt = None
        try:
            dt = parsedate_to_datetime(texto)
        except (TypeError, ValueError):
            pass
        if dt is None:
            for formato in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                try:
                    dt = datetime.strptime(texto[:len("2026-08-29T00:00:00+0000")], formato)
                    break
                except ValueError:
                    continue
        if dt is None:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(TZ).isoformat(timespec="seconds")


def dentro_de_ventana(fecha_iso: str | None, dias: int | None = None) -> bool:
    """Sin fecha, se acepta: la ausencia de fecha es un problema de la fuente,
    no motivo para descartar un hallazgo. La bandeja lo verá sin fecha."""
    if not fecha_iso:
        return True
    dias = CONFIG.ventana_dias if dias is None else dias
    try:
        dt = datetime.fromisoformat(fecha_iso)
    except ValueError:
        return True
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TZ)
    return dt >= datetime.now(TZ) - timedelta(days=dias)
