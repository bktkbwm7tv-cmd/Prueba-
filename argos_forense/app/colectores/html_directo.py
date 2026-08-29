"""Conector directo a páginas públicas (§1).

Sólo se usa cuando `robots.txt` lo permite — la comprobación vive en
`base.obtener()`. Extrae enlaces de la sala de prensa y, para cada uno, el
título, la fecha y el texto, que es lo que §15 exige archivar.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Respuesta, normalizar_fecha, obtener

RE_FECHA_EN_RUTA = re.compile(r"/(20\d{2})[/-](\d{1,2})[/-](\d{1,2})(?:/|$)")


def fecha_en_ruta(url: str) -> str | None:
    """La fecha de la URL fija la **publicación**, no el hecho.

    Se devuelve como fecha de publicación y así se almacena; la fecha del hecho
    es un campo distinto de la ficha y lo fija la persona que valida.
    """
    m = RE_FECHA_EN_RUTA.search(url)
    if not m:
        return None
    anio, mes, dia = (int(g) for g in m.groups())
    if not (1 <= mes <= 12 and 1 <= dia <= 31):
        return None
    return f"{anio:04d}-{mes:02d}-{dia:02d}"


def _texto_limpio(sopa: BeautifulSoup) -> str:
    for etiqueta in sopa(["script", "style", "nav", "footer", "header", "form", "noscript"]):
        etiqueta.decompose()
    return re.sub(r"\n{3,}", "\n\n", sopa.get_text("\n", strip=True))


def listar_enlaces(url_portal: str, limite: int = 40) -> tuple[list[dict], Respuesta]:
    """Enlaces del listado de boletines de un portal, sin suponer su estructura."""
    respuesta = obtener(url_portal)
    if not respuesta.ok:
        return [], respuesta
    sopa = BeautifulSoup(respuesta.texto, "html.parser")
    base_host = urlparse(respuesta.url).netloc
    vistos: set[str] = set()
    salida: list[dict] = []
    for a in sopa.find_all("a", href=True):
        href = urljoin(respuesta.url, a["href"].strip())
        if urlparse(href).netloc != base_host:
            continue
        if href in vistos or href.rstrip("/") == respuesta.url.rstrip("/"):
            continue
        titulo = a.get_text(" ", strip=True)
        if len(titulo) < 25:  # menús y paginadores
            continue
        vistos.add(href)
        salida.append({
            "url": href,
            "titulo": titulo[:400],
            "fecha_publicacion": normalizar_fecha(fecha_en_ruta(href)),
            "medio": None,
        })
        if len(salida) >= limite:
            break
    return salida, respuesta


def leer_nota(url: str) -> dict:
    """Descarga una nota y devuelve título, fecha, texto y HTML para la evidencia (§15)."""
    respuesta = obtener(url)
    if not respuesta.ok:
        return {"ok": False, "url": url, "estado": respuesta.estado, "error": respuesta.error}
    sopa = BeautifulSoup(respuesta.texto, "html.parser")
    titulo = None
    if sopa.title and sopa.title.string:
        titulo = sopa.title.string.strip()
    h1 = sopa.find("h1")
    if h1:
        titulo = h1.get_text(" ", strip=True) or titulo

    fecha = None
    for selector, atributo in (
        ({"property": "article:published_time"}, "content"),
        ({"name": "date"}, "content"),
        ({"itemprop": "datePublished"}, "content"),
    ):
        etiqueta = sopa.find("meta", attrs=selector)
        if etiqueta and etiqueta.get(atributo):
            fecha = normalizar_fecha(etiqueta[atributo])
            break
    if not fecha:
        tiempo = sopa.find("time")
        if tiempo:
            fecha = normalizar_fecha(tiempo.get("datetime") or tiempo.get_text(strip=True))
    if not fecha:
        fecha = normalizar_fecha(fecha_en_ruta(respuesta.url))

    return {
        "ok": True,
        "url": respuesta.url,
        "titulo": (titulo or "").strip()[:500],
        "fecha_publicacion": fecha,
        "texto": _texto_limpio(sopa)[:60000],
        "html": respuesta.texto,
    }
