"""Evidencia digital (§15).

Se guarda, cuando técnicamente es posible: URL, título, fecha de publicación,
fecha de consulta, texto extraído, HTML, captura y hash SHA-256. Lo que no se
pueda obtener se declara — nunca se rellena.
"""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

from .. import db
from ..config import CONFIG


def sha256_texto(texto: str | bytes | None) -> str | None:
    if texto is None:
        return None
    datos = texto.encode("utf-8") if isinstance(texto, str) else texto
    return hashlib.sha256(datos).hexdigest()


def hash_url(url: str) -> str:
    """Hash de la URL normalizada: identidad estable de una publicación."""
    normalizada = (url or "").strip().rstrip("/").lower()
    return hashlib.sha256(normalizada.encode("utf-8")).hexdigest()


def _directorio(raw_item_id: int) -> Path:
    ruta = Path(CONFIG.almacen_evidencia) / f"{raw_item_id // 1000:04d}" / str(raw_item_id)
    ruta.mkdir(parents=True, exist_ok=True)
    return ruta


def guardar(
    *,
    raw_item_id: int,
    url: str,
    titulo: str | None,
    fecha_publicacion: str | None,
    texto: str | None,
    html: str | None,
    captura: bytes | None = None,
    estado_captura: str = "NO_INTENTADA",
) -> int:
    """Congela lo consultado. El HTML y la captura van a disco; los hashes, a la base."""
    ruta_html = None
    ruta_captura = None
    if html or captura:
        destino = _directorio(raw_item_id)
        if html:
            archivo = destino / "pagina.html"
            archivo.write_text(html, encoding="utf-8", errors="replace")
            ruta_html = str(archivo)
        if captura:
            archivo = destino / "captura.png"
            archivo.write_bytes(captura)
            ruta_captura = str(archivo)

    return db.insertar(
        "evidence",
        {
            "raw_item_id": raw_item_id,
            "url": url,
            "titulo": titulo,
            "fecha_publicacion": fecha_publicacion,
            "fecha_consulta": db.ahora_iso(),
            "texto": texto,
            "ruta_html": ruta_html,
            "ruta_captura": ruta_captura,
            "sha256_texto": sha256_texto(texto),
            "sha256_html": sha256_texto(html),
            "sha256_captura": sha256_texto(captura),
            "estado_captura": estado_captura,
            "creado_en": db.ahora_iso(),
        },
    )


def verificar(evidencia_id: int) -> dict:
    """Recomprueba que lo archivado en disco sigue coincidiendo con su hash."""
    fila = db.consultar_uno("SELECT * FROM evidence WHERE id = ?", (evidencia_id,))
    if not fila:
        return {"existe": False}
    resultado = {"existe": True, "id": evidencia_id, "url": fila["url"], "comprobaciones": []}
    resultado["comprobaciones"].append({
        "artefacto": "texto",
        "hash_registrado": fila["sha256_texto"],
        "hash_actual": sha256_texto(fila["texto"]),
        "integro": sha256_texto(fila["texto"]) == fila["sha256_texto"],
    })
    for artefacto, ruta_col, hash_col in (("html", "ruta_html", "sha256_html"), ("captura", "ruta_captura", "sha256_captura")):
        ruta = fila[ruta_col]
        if not ruta:
            resultado["comprobaciones"].append({"artefacto": artefacto, "estado": "NO_ARCHIVADO"})
            continue
        p = Path(ruta)
        if not p.exists():
            resultado["comprobaciones"].append({"artefacto": artefacto, "estado": "ARCHIVO_AUSENTE", "integro": False})
            continue
        actual = sha256_texto(p.read_bytes())
        resultado["comprobaciones"].append({
            "artefacto": artefacto,
            "hash_registrado": fila[hash_col],
            "hash_actual": actual,
            "integro": actual == fila[hash_col],
        })
    resultado["integro"] = all(c.get("integro", True) for c in resultado["comprobaciones"])
    return resultado


def capturar_pantalla(url: str) -> tuple[bytes | None, str]:
    """Captura con Playwright si está disponible; si no, lo declara y sigue.

    Nunca se inventa una captura ni se sustituye por otra imagen.
    """
    try:  # pragma: no cover - depende del entorno
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None, "CAPTURA_NO_DISPONIBLE — Playwright no instalado"
    if not shutil.which("chromium") and not Path("/opt/pw-browsers").exists():  # pragma: no cover
        return None, "CAPTURA_NO_DISPONIBLE — navegador no encontrado"
    try:  # pragma: no cover
        with sync_playwright() as pw:
            navegador = pw.chromium.launch()
            pagina = navegador.new_page(viewport={"width": 1280, "height": 1600})
            pagina.goto(url, timeout=CONFIG.http_timeout * 1000, wait_until="domcontentloaded")
            datos = pagina.screenshot(full_page=True)
            navegador.close()
            return datos, "CAPTURADA"
    except Exception as exc:  # pragma: no cover
        return None, f"CAPTURA_FALLIDA — {type(exc).__name__}: {exc}"[:200]
