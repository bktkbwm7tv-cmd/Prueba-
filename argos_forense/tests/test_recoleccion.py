"""Pruebas del rastreo, la evidencia digital y el catálogo de fuentes."""

from __future__ import annotations



def test_el_rastreo_registra_el_fallo_sin_disfrazarlo(entorno, monkeypatch):
    """Un portal que no se pudo consultar no es un portal sin novedades."""
    from app.colectores import base, runner

    def falla(url, **kwargs):
        return base.Respuesta(ok=False, url=url, estado=base.EGRESO_BLOQUEADO,
                              error="CONNECT tunnel failed, response 403")

    monkeypatch.setattr(base, "obtener", falla)
    monkeypatch.setattr("app.colectores.rss.obtener", falla)

    resultado = runner.rastrear(usuario="prueba", incluir_rss=False, limite_consultas=3)
    assert resultado["altas_en_bandeja"] == 0
    assert resultado["fuentes_con_error"] == 3
    assert all(e["estado"] == base.EGRESO_BLOQUEADO for e in resultado["errores"])
    # Y el diagnóstico queda guardado, no sólo devuelto.
    guardado = entorno.config_get("ultimo_rastreo")
    assert guardado["fuentes_con_error"] == 3


def test_el_rastreo_clasifica_y_no_duplica(entorno, monkeypatch):
    from app.colectores import base, runner

    publicaciones = [{
        "url": "https://medio.invalid/nota-1",
        "titulo": "Localizan fosa clandestina con restos óseos en Tlajomulco, Jalisco",
        "resumen": "Un colectivo de búsqueda halló el predio.",
        "fecha_publicacion": entorno.ahora_iso(), "medio": "Medio de prueba",
    }, {
        "url": "https://medio.invalid/nota-2",
        "titulo": "Inauguran un parque en la colonia centro",
        "resumen": "Nota sin relación con las tres categorías.",
        "fecha_publicacion": entorno.ahora_iso(), "medio": "Medio de prueba",
    }]

    def canal(url, limite, ventana_dias=None):
        return publicaciones, base.Respuesta(ok=True, url=url, estado="OK", codigo=200)

    monkeypatch.setattr("app.colectores.rss.entradas", canal)
    primero = runner.rastrear(usuario="prueba", incluir_rss=False, limite_consultas=1)
    assert primero["altas_en_bandeja"] == 1
    assert primero["descartadas_por_clasificacion"] == 1

    # La misma URL en la vuelta siguiente no se vuelve a dar de alta.
    segundo = runner.rastrear(usuario="prueba", incluir_rss=False, limite_consultas=1)
    assert segundo["altas_en_bandeja"] == 0
    assert segundo["ya_conocidas"] == 1

    item = entorno.consultar_uno("SELECT * FROM raw_items WHERE url = ?", ("https://medio.invalid/nota-1",))
    assert item["categoria_detectada"] == "FOS"
    assert item["entidad_iso"] == "MX-JAL"
    assert item["estado"] == "PENDIENTE"


def test_evidencia_guarda_hash_y_permite_verificarlo(entorno, hallazgo):
    from app.core import evidencia

    raw_id = hallazgo()
    texto = "Texto extraído de la publicación consultada."
    html = "<html><body>Texto extraído de la publicación consultada.</body></html>"
    ev_id = evidencia.guardar(
        raw_item_id=raw_id, url="https://ejemplo.mx/nota", titulo="Título",
        fecha_publicacion="2026-08-28", texto=texto, html=html,
        estado_captura="CAPTURA_NO_DISPONIBLE — Playwright no instalado",
    )
    verificacion = evidencia.verificar(ev_id)
    assert verificacion["integro"] is True
    assert verificacion["comprobaciones"][0]["hash_registrado"] == evidencia.sha256_texto(texto)

    fila = entorno.consultar_uno("SELECT * FROM evidence WHERE id = ?", (ev_id,))
    assert fila["fecha_consulta"] and fila["sha256_html"]
    # La captura no se inventa: se declara por qué no existe.
    assert "NO_DISPONIBLE" in fila["estado_captura"]


def test_robots_se_respeta_por_omision(entorno, monkeypatch):
    from app.colectores import base

    monkeypatch.setattr(base, "permitido_por_robots", lambda url: (False, "robots.txt lo prohíbe"))
    respuesta = base.obtener("https://ejemplo.invalid/algo")
    assert respuesta.ok is False
    assert respuesta.estado == base.ROBOTS_PROHIBE


def test_una_fuente_no_se_da_por_verificada_sin_sondeo(entorno):
    filas = entorno.consultar("SELECT verificado, estatus FROM sources")
    assert filas, "el catálogo semilla debe existir"
    assert all(f["verificado"] == 0 for f in filas)
    assert all(f["estatus"] in ("SIN VERIFICAR", "SIN DOMINIO CANÓNICO REGISTRADO") for f in filas)


def test_el_catalogo_cubre_las_32_entidades_en_nivel_1(entorno):
    from app.core import geo

    cubiertas = {
        f["entidad_iso"]
        for f in entorno.consultar("SELECT DISTINCT entidad_iso FROM sources WHERE nivel = 1 AND entidad_iso IS NOT NULL")
    }
    assert cubiertas == {e["iso"] for e in geo.entidades()}


def test_fecha_en_ruta_no_es_fecha_del_hecho(entorno):
    from app.colectores import html_directo

    # La fecha de la URL fija la publicación. El sistema la guarda como
    # fecha_publicacion, nunca como fecha del hecho.
    assert html_directo.fecha_en_ruta("https://x.gob.mx/2026/08/17/boletin/") == "2026-08-17"
    assert html_directo.fecha_en_ruta("https://x.gob.mx/boletin/12345") is None
    assert html_directo.fecha_en_ruta("https://x.gob.mx/2026/13/40/boletin/") is None
