"""Lectura de canales RSS/Atom (§1).

Sólo se usa `url_rss` cuando está verificada: una ruta de canal supuesta que
devuelve 404 produciría un falso vacío de cobertura, que es peor que no tener
canal. Sin canal verificado, el rastreo cae a la vía de búsqueda.
"""

from __future__ import annotations

import feedparser

from .base import Respuesta, dentro_de_ventana, normalizar_fecha, obtener


def entradas(url_rss: str, limite: int, ventana_dias: int | None = None) -> tuple[list[dict], Respuesta]:
    respuesta = obtener(url_rss)
    if not respuesta.ok:
        return [], respuesta
    canal = feedparser.parse(respuesta.contenido or respuesta.texto)
    salida: list[dict] = []
    for entrada in canal.entries[: limite * 3]:
        enlace = (entrada.get("link") or "").strip()
        titulo = (entrada.get("title") or "").strip()
        if not enlace or not titulo:
            continue
        fecha = normalizar_fecha(
            entrada.get("published_parsed") or entrada.get("updated_parsed")
            or entrada.get("published") or entrada.get("updated")
        )
        if not dentro_de_ventana(fecha, ventana_dias):
            continue
        resumen = (entrada.get("summary") or "").strip()
        salida.append({
            "url": enlace,
            "titulo": titulo,
            "resumen": _sin_etiquetas(resumen)[:1500],
            "fecha_publicacion": fecha,
            "medio": (canal.feed.get("title") or "").strip() or None,
        })
        if len(salida) >= limite:
            break
    return salida, respuesta


def _sin_etiquetas(html: str) -> str:
    if "<" not in html:
        return html
    from bs4 import BeautifulSoup

    return BeautifulSoup(html, "html.parser").get_text(" ", strip=True)


def verificar_canal(url_rss: str) -> dict:
    """Sondea un canal y dice qué devolvió. No supone nada."""
    respuesta = obtener(url_rss)
    if not respuesta.ok:
        return {"verificado": False, "estado": respuesta.estado, "codigo": respuesta.codigo,
                "error": respuesta.error}
    canal = feedparser.parse(respuesta.contenido or respuesta.texto)
    n = len(canal.entries)
    return {
        "verificado": n > 0,
        "estado": "OK" if n else "SIN ENTRADAS",
        "codigo": respuesta.codigo,
        "entradas": n,
        "titulo_canal": (canal.feed.get("title") or "").strip() or None,
    }
