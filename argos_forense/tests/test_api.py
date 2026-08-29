"""Pruebas de la API de §24 y del flujo completo de la plataforma."""

from __future__ import annotations


def test_health(cliente):
    r = cliente.get("/api/health")
    assert r.status_code == 200
    datos = r.json()
    assert datos["sistema"] == "ARGOS FORENSE"
    assert datos["estado"] == "OK"
    assert set(datos["catalogos"]["categorias"]) == {"FOS", "CAM", "CSE"}
    assert datos["seguridad"]["expone_punto_exacto"] is False


def test_endpoints_de_la_instruccion_maestra_existen(cliente):
    from app.main import app

    rutas = set(app.openapi()["paths"])
    exigidos = {
        "/api/health", "/api/collect", "/api/inbox", "/api/inbox/{raw_id}/duplicates",
        "/api/inbox/{raw_id}/validate", "/api/inbox/{raw_id}/reject", "/api/inbox/{raw_id}/link",
        "/api/events", "/api/events/{folio}", "/api/cuts", "/api/cuts/publish",
        "/api/audit", "/api/sources", "/api/collectives",
    }
    assert exigidos <= rutas, exigidos - rutas


def test_catalogos_traen_las_32_entidades(cliente):
    datos = cliente.get("/api/catalogs").json()
    assert len(datos["entidades"]) == 32
    assert len(datos["niveles_fuente"]) == 5
    assert set(datos["niveles_corroboracion"]) == {"A", "B", "C", "D"}


def test_geojson_de_entidades_es_valido(cliente):
    datos = cliente.get("/api/geo/entidades.geojson").json()
    assert datos["type"] == "FeatureCollection"
    assert len(datos["features"]) == 32
    props = datos["features"][0]["properties"]
    assert {"id", "nombre", "region", "total", "fosas", "campamentos", "casas_de_seguridad"} <= set(props)


def test_flujo_completo_de_bandeja_a_corte(cliente, hallazgo):
    raw = hallazgo()

    # 1. La bandeja lo muestra pendiente, con lo que exige §8.
    inbox = cliente.get("/api/inbox").json()
    assert inbox["total"] == 1
    item = inbox["items"][0]
    for campo in ("titulo", "medio", "url", "fecha_publicacion", "categoria_detectada",
                  "entidad_iso", "resumen", "confianza_pct", "duplicados_abiertos"):
        assert campo in item

    # 2. Los duplicados se consultan, no se aplican.
    dup = cliente.get(f"/api/inbox/{raw}/duplicates").json()
    assert "nunca fusiona" in dup["nota"]

    # 3. Validar emite folio.
    r = cliente.post(f"/api/inbox/{raw}/validate", json={"motivo": "corroborado por el analista"},
                     headers={"X-ARGOS-Usuario": "ana"})
    assert r.status_code == 200, r.text
    folio = r.json()["folio"]
    assert folio.startswith("AF-") and folio.endswith("-0001")

    # 4. La ficha trae los campos de §10.
    ficha = cliente.get(f"/api/events/{folio}").json()
    for campo in ("folio", "categoria", "subcategoria", "fecha_deteccion", "hora_deteccion",
                  "fecha_probable_evento", "entidad", "municipio", "localidad", "resumen_factual",
                  "nivel_corroboracion", "fuentes", "ultima_actualizacion", "corte_aparicion",
                  "historial"):
        assert campo in ficha, campo
    assert ficha["fuentes"][0]["clase"] in {
        "PUBLICACIÓN PERIODÍSTICA", "CONFIRMACIÓN INSTITUCIONAL", "REPORTE DE COLECTIVO"
    }

    # 5. El tablero cuenta lo que hay.
    tablero = cliente.get("/api/dashboard").json()
    assert tablero["fosas_detectadas"] == 1
    assert tablero["entidades_con_actividad"] == 1
    assert tablero["registros_pendientes_de_validacion"] == 0

    # 6. Corte, publicación y sello.
    corte = cliente.post("/api/cuts/generate", json={}, headers={"X-ARGOS-Usuario": "ana"}).json()
    assert corte["estado"] == "BORRADOR"
    publicado = cliente.post("/api/cuts/publish", json={}, headers={"X-ARGOS-Usuario": "ana"}).json()
    assert publicado["estado"] == "PUBLICADO" and publicado["sha256"]
    assert cliente.post("/api/cuts/publish", json={"numero": corte["numero"]},
                        headers={"X-ARGOS-Usuario": "ana"}).status_code == 409
    assert cliente.get(f"/api/cuts/{corte['numero']}/verify").json()["integro"] is True

    # 7. El corte trae los dieciséis apartados de §17.
    snapshot = cliente.get(f"/api/cuts/{corte['numero']}").json()["snapshot"]
    for apartado in ("resumen_ejecutivo", "total_nacional", "categorias", "nuevos_eventos",
                     "actualizaciones", "eventos_confirmados", "eventos_por_verificar",
                     "desglose_por_entidad", "mapa_nacional", "comparacion", "fuentes_utilizadas",
                     "pendientes_de_corroboracion", "metodologia", "bitacora_integridad"):
        assert apartado in snapshot, apartado
    assert len(snapshot["desglose_por_entidad"]) == 32

    # 8. La bitácora registró todo el recorrido.
    bitacora = cliente.get("/api/audit", params={"evento": folio}).json()
    assert bitacora["total"] >= 2
    assert all(m["usuario"] and m["ts"] for m in bitacora["movimientos"])


def test_exportaciones(cliente, hallazgo):
    raw = hallazgo()
    folio = cliente.post(f"/api/inbox/{raw}/validate", json={"motivo": "ok"}).json()["folio"]

    assert cliente.get("/api/export/events.json").json()["total"] == 1
    csv = cliente.get("/api/export/events.csv").text
    assert "folio" in csv.splitlines()[0] and folio in csv
    geo = cliente.get("/api/export/events.geojson").json()
    assert geo["type"] == "FeatureCollection" and len(geo["features"]) == 1
    assert "no exporta ubicación táctica" in geo["nota_seguridad"]

    cliente.post("/api/cuts/generate", json={})
    cliente.post("/api/cuts/publish", json={})
    pdf = cliente.get("/api/cuts/1/export.pdf")
    assert pdf.status_code == 200
    assert pdf.content[:5] == b"%PDF-"
    assert len(pdf.content) > 3000

    assert cliente.get("/api/export/events.xml").status_code == 400


def test_atribucion_por_api(cliente, hallazgo):
    raw = hallazgo()
    folio = cliente.post(f"/api/inbox/{raw}/validate", json={"motivo": "ok"}).json()["folio"]
    incompleta = cliente.post(f"/api/events/{folio}/attribution",
                              json={"texto": "una organización", "atribuido_por": "", "url": ""})
    assert incompleta.status_code == 422
    valida = cliente.post(f"/api/events/{folio}/attribution", json={
        "texto": "el sitio a un grupo delictivo local",
        "atribuido_por": "La Fiscalía General del Estado de Jalisco",
        "url": "https://fiscalia.jalisco.gob.mx/boletin/1",
    })
    assert valida.status_code == 200
    assert cliente.get(f"/api/events/{folio}").json()["atribucion"][0]["atribuido_por"]


def test_fuentes_y_colectivos(cliente):
    fuentes = cliente.get("/api/sources").json()
    assert fuentes["total"] >= 130
    assert fuentes["por_nivel"]["1"] >= 96  # 32 entidades × 3 emisores + federales
    assert fuentes["verificadas"] == 0, "ninguna fuente se da por verificada sin sondeo real"

    colectivos = cliente.get("/api/collectives").json()
    assert colectivos["total"] >= 1
    assert "REPORTE DE COLECTIVO" in colectivos["distincion"]
    assert all(c["estatus_fuente"] == "SIN VERIFICAR" for c in colectivos["colectivos"])
    # §20: el módulo no tiene siquiera dónde guardar un domicilio o un teléfono.
    assert not {"domicilio", "telefono"} & set(colectivos["colectivos"][0])

    nuevo = cliente.post("/api/collectives", json={
        "nombre": "Colectivo de prueba", "entidad_iso": "MX-JAL", "municipio_base": "Guadalajara",
    }, headers={"X-ARGOS-Usuario": "ana"})
    assert nuevo.status_code == 201
    assert cliente.get("/api/audit", params={"entidad_tipo": "collective"}).json()["total"] >= 1


def test_estados_y_tendencias(cliente, hallazgo):
    cliente.post(f"/api/inbox/{hallazgo()}/validate", json={"motivo": "ok"})
    estados = cliente.get("/api/states").json()["entidades"]
    assert len(estados) == 32
    jal = next(e for e in estados if e["iso"] == "MX-JAL")
    assert jal["fosas"] == 1 and jal["nivel_corroboracion_max"] == "C"

    detalle = cliente.get("/api/states/MX-JAL").json()
    assert detalle["entidad"] == "Jalisco" and len(detalle["eventos"]) == 1
    assert cliente.get("/api/states/MX-XXX").status_code == 404

    tendencias = cliente.get("/api/trends").json()
    assert tendencias["serie"] == [] and "no se rellena" in tendencias["nota"]


def test_programador_configurable(cliente):
    estado = cliente.get("/api/scheduler").json()
    assert estado["rastreo_minutos"] == 60 and estado["corte_horas"] == 72
    cambiado = cliente.post("/api/scheduler", json={"rastreo_minutos": 30, "corte_horas": 48},
                            headers={"X-ARGOS-Usuario": "ana"}).json()
    assert cambiado["rastreo_minutos"] == 30 and cambiado["corte_horas"] == 48
    assert cliente.get("/api/config").json()["valores_persistidos"]["rastreo_minutos"] == 30


def test_descartar_conserva_el_registro(cliente, hallazgo):
    raw = hallazgo()
    assert cliente.post(f"/api/inbox/{raw}/reject", json={"motivo": "no"}).status_code == 422
    r = cliente.post(f"/api/inbox/{raw}/reject", json={"motivo": "La nota no describe un hecho de las tres categorías."})
    assert r.status_code == 200
    detalle = cliente.get(f"/api/inbox/{raw}").json()
    assert detalle["estado"] == "DESCARTADO" and detalle["motivo"]
