"""Pruebas de las reglas que no pueden romperse sin romper el producto."""

from __future__ import annotations

import pytest


# --- §9 folio ---------------------------------------------------------------
def test_folio_formato_y_consecutivo_por_entidad_y_categoria(entorno, hallazgo):
    from app.core import bandeja, folio

    a = bandeja.validar(hallazgo(), usuario="analista", motivo="prueba")["folio"]
    b = bandeja.validar(
        hallazgo(url="https://ejemplo.mx/nota/2", titulo="Otra fosa clandestina en Zapopan, Jalisco"),
        usuario="analista", motivo="prueba",
    )["folio"]
    anio = entorno.ahora().year
    assert a == f"AF-{anio}-JAL-FOS-0001"
    assert b == f"AF-{anio}-JAL-FOS-0002"
    # Otra entidad y otra categoría arrancan su propio consecutivo.
    c = bandeja.validar(
        hallazgo(url="https://ejemplo.mx/nota/3",
                 titulo="Aseguran casa de seguridad en Culiacán, Sinaloa",
                 categoria_detectada="CSE", entidad_iso="MX-SIN", municipio="Culiacán"),
        usuario="analista", motivo="prueba",
    )["folio"]
    assert c == f"AF-{anio}-SIN-CSE-0001"
    assert folio.descomponer(c)["entidad_iso"] == "MX-SIN"


def test_folio_no_es_editable(entorno, hallazgo):
    from app.core import bandeja, eventos

    f = bandeja.validar(hallazgo(), usuario="analista")["folio"]
    resultado = eventos.actualizar_ficha(f, {"folio": "AF-2026-JAL-FOS-9999"}, usuario="analista", motivo="intento")
    assert resultado["modificados"] == 0
    assert "folio" in resultado["rechazados"]
    assert eventos.obtener(f) is not None


def test_no_se_emite_folio_sin_entidad(entorno, hallazgo):
    from app.core import bandeja, eventos

    raw = hallazgo(url="https://ejemplo.mx/nota/sin-entidad", entidad_iso=None)
    with pytest.raises(eventos.ErrorEvento, match="entidad federativa"):
        bandeja.validar(raw, usuario="analista")


# --- §4/§8 la bandeja es obligatoria ----------------------------------------
def test_el_rastreo_no_crea_eventos(entorno, hallazgo):
    hallazgo()
    hallazgo(url="https://ejemplo.mx/nota/otra")
    assert entorno.escalar("SELECT COUNT(*) FROM events") == 0
    assert entorno.escalar("SELECT COUNT(*) FROM raw_items WHERE estado='PENDIENTE'") == 2


def test_un_registro_no_se_valida_dos_veces(entorno, hallazgo):
    from app.core import bandeja

    raw = hallazgo()
    bandeja.validar(raw, usuario="analista")
    with pytest.raises(bandeja.ErrorBandeja, match="ya fue resuelto"):
        bandeja.validar(raw, usuario="analista")


# --- §11 corroboración ------------------------------------------------------
def test_nivel_sube_de_D_a_A_al_llegar_la_fuente_institucional(entorno, hallazgo):
    from app.core import bandeja, corroboracion, eventos

    # Reporte de colectivo (nivel 5) -> D
    raw = hallazgo(nivel_fuente=5)
    f = bandeja.validar(raw, usuario="analista")["folio"]
    assert eventos.obtener(f)["nivel_corroboracion"] == "D"

    # Una fuente periodística identificable -> C
    prensa = hallazgo(url="https://unmedio.mx/nota", medio="Un medio", nivel_fuente=3)
    bandeja.vincular(prensa, f, usuario="analista")
    assert eventos.obtener(f)["nivel_corroboracion"] == "C"

    # Segundo medio independiente -> B
    otro = hallazgo(url="https://otromedio.mx/nota", medio="Otro medio", nivel_fuente=2)
    bandeja.vincular(otro, f, usuario="analista")
    assert eventos.obtener(f)["nivel_corroboracion"] == "B"

    # Fiscalía competente -> A
    fuente_jal = entorno.consultar_uno(
        "SELECT id FROM sources WHERE entidad_iso='MX-JAL' AND nivel=1 AND nombre LIKE 'Fiscal%'"
    )
    inst = hallazgo(url="https://fiscalia.jalisco.gob.mx/boletin/1", medio="FGE Jalisco",
                    nivel_fuente=1, source_id=fuente_jal["id"])
    bandeja.vincular(inst, f, usuario="analista")
    ev = eventos.obtener(f)
    assert ev["nivel_corroboracion"] == "A"
    assert corroboracion.es_hecho_confirmado(ev["nivel_corroboracion"])


def test_un_reporte_de_colectivo_solo_no_confirma(entorno):
    from app.core import corroboracion

    calculo = corroboracion.evaluar(
        [{"nivel": 5, "es_colectivo": 1, "url": "https://facebook.com/colectivo/1", "medio": "Colectivo"}]
    )
    assert calculo["nivel"] == "D"
    assert not corroboracion.es_hecho_confirmado(calculo["nivel"])


def test_institucion_de_otra_entidad_no_confirma(entorno):
    from app.core import corroboracion

    calculo = corroboracion.evaluar(
        [{"nivel": 1, "ambito": "ESTATAL", "entidad_iso": "MX-SIN",
          "url": "https://fiscalia.sinaloa.gob.mx/x", "medio": "FGE Sinaloa"}],
        "MX-JAL",
    )
    assert calculo["nivel"] == "C"


# --- §12 deduplicación ------------------------------------------------------
def test_duplicidad_se_propone_pero_nunca_se_fusiona_sola(entorno, hallazgo):
    from app.core import bandeja

    hallazgo()  # primer registro del mismo hecho
    b = hallazgo(url="https://otromedio.mx/nota-fosa",
                 titulo="FGE confirma tres cuerpos en fosa clandestina de Tlajomulco, Jalisco")
    resultado = bandeja.duplicados(b)
    assert resultado["candidatos"], "debería proponer al menos un candidato"
    assert resultado["candidatos"][0]["puntaje"] >= 60
    assert all(c["estado"] == "ABIERTO" for c in resultado["candidatos"])
    assert entorno.escalar("SELECT COUNT(*) FROM events") == 0


def test_fusion_migra_fuentes_y_conserva_los_dos_folios(entorno, hallazgo):
    from app.core import bandeja, eventos

    f1 = bandeja.validar(hallazgo(), usuario="analista")["folio"]
    f2 = bandeja.validar(
        hallazgo(url="https://otromedio.mx/nota-2", titulo="Fosa clandestina en Tlajomulco, Jalisco"),
        usuario="analista",
    )["folio"]
    resultado = eventos.fusionar(f2, f1, usuario="analista", motivo="Mismo hecho, dos publicaciones")
    assert resultado["fuentes_migradas"] == 1
    assert eventos.obtener(f2)["estado"] == "FUSIONADO"
    assert eventos.obtener(f2)["fusionado_en"] == f1
    assert len(eventos.fuentes(f1)) == 2


# --- §13 un evento, muchas fuentes -----------------------------------------
def test_muchas_fuentes_un_solo_evento(entorno, hallazgo):
    from app.core import bandeja, eventos

    f = bandeja.validar(hallazgo(), usuario="analista")["folio"]
    for i in range(4):
        bandeja.vincular(hallazgo(url=f"https://medio{i}.mx/nota", medio=f"Medio {i}"), f, usuario="analista")
    assert entorno.escalar("SELECT COUNT(*) FROM events") == 1
    assert len(eventos.fuentes(f)) == 5


# --- §14 trazabilidad -------------------------------------------------------
def test_cada_movimiento_deja_bitacora_y_nada_se_borra(entorno, hallazgo):
    from app.core import auditoria, bandeja, eventos

    raw = hallazgo()
    f = bandeja.validar(raw, usuario="ana", motivo="prueba")["folio"]
    eventos.actualizar_ficha(f, {"municipio": "Tlajomulco"}, usuario="ana", motivo="corrección de municipio")
    eventos.cambiar_estado(f, "DESCARTADO", usuario="ana", motivo="descartado tras revisión")

    historial = auditoria.historial_evento(f)
    campos = {h["campo"] for h in historial}
    assert {"folio", "municipio", "estado"} <= campos
    assert all(h["usuario"] for h in historial)
    # El evento sigue existiendo: cambió de estado, no se borró.
    assert eventos.obtener(f)["estado"] == "DESCARTADO"
    assert entorno.escalar("SELECT COUNT(*) FROM events") == 1


def test_editar_sin_motivo_se_rechaza(entorno, hallazgo):
    from app.core import bandeja, eventos

    f = bandeja.validar(hallazgo(), usuario="ana")["folio"]
    with pytest.raises(eventos.ErrorEvento, match="motivo"):
        eventos.actualizar_ficha(f, {"municipio": "X"}, usuario="ana", motivo="  ")


# --- §16 inmutabilidad del corte -------------------------------------------
def test_corte_publicado_no_se_modifica(entorno, hallazgo):
    from app.core import bandeja, cortes

    bandeja.validar(hallazgo(), usuario="ana")
    corte = cortes.generar(usuario="ana")
    publicado = cortes.publicar(corte["numero"], usuario="ana")
    assert publicado["sha256"]
    with pytest.raises(cortes.CorteInmutable):
        cortes.publicar(corte["numero"], usuario="ana")
    assert cortes.verificar_sello(corte["numero"])["integro"] is True


def test_evento_posterior_no_entra_en_el_corte_publicado(entorno, hallazgo):
    from app.core import bandeja, cortes

    bandeja.validar(hallazgo(), usuario="ana")
    c1 = cortes.generar(usuario="ana")
    cortes.publicar(c1["numero"], usuario="ana")
    snapshot_1 = cortes.obtener(c1["numero"])["snapshot"]
    total_1 = snapshot_1["total_nacional"]["total"]

    bandeja.validar(
        hallazgo(url="https://ejemplo.mx/posterior", titulo="Fosa clandestina en Zapopan, Jalisco"),
        usuario="ana",
    )
    # El corte ya publicado no cambia.
    assert cortes.obtener(c1["numero"])["snapshot"]["total_nacional"]["total"] == total_1
    c2 = cortes.generar(usuario="ana")
    assert c2["snapshot"]["total_nacional"]["total"] == total_1 + 1


def test_comparacion_entre_cortes_declara_el_cambio_de_nivel(entorno, hallazgo):
    from app.core import bandeja, cortes

    f = bandeja.validar(hallazgo(nivel_fuente=3), usuario="ana")["folio"]
    c1 = cortes.generar(usuario="ana")
    cortes.publicar(c1["numero"], usuario="ana")

    fuente_jal = entorno.consultar_uno(
        "SELECT id FROM sources WHERE entidad_iso='MX-JAL' AND nivel=1 AND nombre LIKE 'Fiscal%'"
    )
    bandeja.vincular(
        hallazgo(url="https://fiscalia.jalisco.gob.mx/b/1", medio="FGE Jalisco",
                 nivel_fuente=1, source_id=fuente_jal["id"]),
        f, usuario="ana",
    )
    c2 = cortes.generar(usuario="ana")
    cortes.publicar(c2["numero"], usuario="ana")
    comparacion = cortes.comparar_cortes(c2["numero"], c1["numero"])
    cambios = comparacion["cambios_de_nivel"]
    assert cambios and cambios[0]["folio"] == f
    assert cambios[0][f"corte_{c1['numero']:03d}"] == "C"
    assert cambios[0][f"corte_{c2['numero']:03d}"] == "A"
    assert cambios[0]["motivo"]


# --- §20 seguridad ----------------------------------------------------------
def test_no_se_publica_el_punto_exacto(entorno, hallazgo):
    from app.core import bandeja, eventos

    f = bandeja.validar(hallazgo(), usuario="ana")["folio"]
    eventos.actualizar_ficha(
        f, {"latitud": 20.512345, "longitud": -103.412345, "precision_geo": "PUNTO"},
        usuario="ana", motivo="georreferencia fina de trabajo",
    )
    ficha = eventos.ficha(f, exponer_exacto=False)
    assert ficha["ubicacion"]["precision"] == "APROXIMADO_GENERALIZADO"
    assert ficha["ubicacion"]["latitud"] == 20.51
    # El dato fino sigue en la base para uso interno: se reserva, no se pierde.
    assert eventos.obtener(f)["latitud"] == 20.512345


def test_datos_sensibles_se_marcan_y_se_reservan(entorno, hallazgo):
    from app.core import bandeja, eventos

    raw = hallazgo(
        url="https://ejemplo.mx/nota/sensible",
        titulo="Localizan fosa clandestina en Tlajomulco, Jalisco",
        resumen="El predio está en 20.123456, -103.987654; contacto 33 1234 5678. Operativo en curso.",
    )
    item = bandeja.obtener(raw)
    assert "COORDENADA_PRECISA" in item["riesgo_opsec"]["tipos"]
    assert "TELEFONO" in item["riesgo_opsec"]["tipos"]

    f = bandeja.validar(raw, usuario="ana", resumen_factual=item["resumen"])["folio"]
    ficha = eventos.ficha(f)
    assert "20.123456" not in ficha["resumen_factual"]
    assert "RESERVAD" in ficha["resumen_factual"]
    assert ficha["reserva_operativa"] is True


# --- §21 atribución ---------------------------------------------------------
def test_atribucion_exige_quien_la_hizo_y_donde_consta(entorno, hallazgo):
    from app.core import bandeja, eventos, seguridad

    f = bandeja.validar(hallazgo(), usuario="ana")["folio"]
    with pytest.raises(seguridad.AtribucionInvalida):
        eventos.agregar_atribucion(f, {"texto": "campamento de una organización"}, usuario="ana")
    resultado = eventos.agregar_atribucion(
        f,
        {"texto": "el sitio a un grupo delictivo local", "atribuido_por": "La Fiscalía General del Estado",
         "url": "https://fiscalia.jalisco.gob.mx/boletin/1"},
        usuario="ana",
    )
    assert resultado["atribuciones"][0]["formato"].startswith("La Fiscalía General del Estado atribuyó públicamente")


# --- §5/§6 clasificación y cobertura ---------------------------------------
def test_las_tres_categorias_y_las_32_entidades(entorno):
    from app.colectores import google_news
    from app.core import clasificador, geo

    assert len(geo.entidades()) == 32
    assert {e["region"] for e in geo.entidades()} <= set(geo.REGIONES)
    assert set(clasificador.TERMINOS) == {"FOS", "CAM", "CSE"}
    consultas = google_news.consultas_por_entidad()
    assert len({c["entidad_iso"] for c in consultas}) == 32
    assert len(consultas) == 32 * 3


def test_clasificador_no_confunde_ruido_con_hecho(entorno):
    from app.core import clasificador

    assert clasificador.clasificar("Instalan campamento de damnificados por las lluvias").categoria is None
    assert clasificador.clasificar("Hallan fosa séptica en la colonia").confianza <= 20
