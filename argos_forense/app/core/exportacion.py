"""Exportaciones (§19): PDF, CSV, JSON y GeoJSON.

Ninguna exportación amplía lo que la API muestra: la generalización de §20 se
aplica antes de escribir el archivo, no después.
"""

from __future__ import annotations

import csv
import io
import json
from typing import Iterable

from .. import db
from ..config import CATEGORIAS
from . import corroboracion, cortes, eventos, geo

COLUMNAS_CSV = (
    "folio", "categoria", "categoria_nombre", "subcategoria", "entidad_iso", "entidad", "region",
    "municipio", "localidad", "fecha_probable_evento", "fecha_deteccion", "hora_deteccion",
    "nivel_corroboracion", "nivel_etiqueta", "estado", "num_cuerpos", "personas_liberadas",
    "personas_detenidas", "autoridad", "total_fuentes", "latitud", "longitud", "precision_geo",
    "ultima_actualizacion", "resumen_factual",
)


def _filas(filtros: dict) -> list[dict]:
    return eventos.listar(limite=100000, **filtros)["eventos"]


def a_json(filtros: dict) -> str:
    filas = _filas(filtros)
    return json.dumps(
        {
            "generado_en": db.ahora_iso(),
            "sistema": "ARGOS FORENSE",
            "nota_seguridad": "Ubicación generalizada conforme a §20. No contiene coordenadas operativas.",
            "total": len(filas),
            "eventos": filas,
        },
        ensure_ascii=False,
        indent=1,
    )


def a_csv(filtros: dict) -> str:
    filas = _filas(filtros)
    buffer = io.StringIO()
    escritor = csv.DictWriter(buffer, fieldnames=list(COLUMNAS_CSV), extrasaction="ignore")
    escritor.writeheader()
    for f in filas:
        f = dict(f)
        f["nivel_etiqueta"] = corroboracion.ETIQUETAS.get(f.get("nivel_corroboracion"), "")
        escritor.writerow(f)
    return buffer.getvalue()


def a_geojson(filtros: dict) -> str:
    """GeoJSON de puntos generalizados. Nunca de la ubicación fina (§20)."""
    filas = _filas(filtros)
    features = []
    for f in filas:
        if f.get("latitud") is None or f.get("longitud") is None:
            continue
        features.append({
            "type": "Feature",
            "id": f["folio"],
            "geometry": {"type": "Point", "coordinates": [f["longitud"], f["latitud"]]},
            "properties": {
                "folio": f["folio"],
                "categoria": f["categoria"],
                "categoria_nombre": f.get("categoria_nombre"),
                "subcategoria": f.get("subcategoria"),
                "entidad": f.get("entidad"),
                "municipio": f.get("municipio"),
                "nivel_corroboracion": f["nivel_corroboracion"],
                "nivel_etiqueta": f.get("nivel_etiqueta"),
                "es_hecho_confirmado": f.get("es_hecho_confirmado"),
                "fecha_probable_evento": f.get("fecha_probable_evento"),
                "precision_geo": f.get("precision_geo"),
                "total_fuentes": f.get("total_fuentes"),
            },
        })
    return json.dumps(
        {
            "type": "FeatureCollection",
            "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
            "generado_en": db.ahora_iso(),
            "nota_seguridad": (
                "Puntos generalizados (centroide de entidad o rejilla aproximada). "
                "ARGOS FORENSE no exporta ubicación táctica (§20)."
            ),
            "features": features,
        },
        ensure_ascii=False,
    )


def entidades_geojson(conteos: Iterable[dict] | None = None) -> dict:
    """Polígonos de las 32 entidades con el conteo del corte, para el mapa (§3)."""
    base = json.loads(json.dumps(geo.geojson()))  # copia
    por_iso = {c["iso"]: c for c in (conteos or [])}
    for f in base["features"]:
        iso = f["properties"]["id"]
        datos = por_iso.get(iso, {})
        ent = geo.entidad(iso) or {}
        f["properties"].update({
            "region": ent.get("region"),
            "centroide": ent.get("centroide"),
            "fosas": datos.get("fosas", 0),
            "campamentos": datos.get("campamentos", 0),
            "casas_de_seguridad": datos.get("casas_de_seguridad", 0),
            "total": datos.get("total", 0),
            "eventos_nuevos": datos.get("eventos_nuevos", 0),
            "actualizaciones": datos.get("actualizaciones", 0),
            "nivel_corroboracion_max": datos.get("nivel_corroboracion_max"),
            "por_nivel": datos.get("por_nivel", {}),
        })
    return base


# ------------------------------------------------------------------- PDF ----
def _pdf_disponible() -> bool:
    try:
        import reportlab  # noqa: F401
    except ImportError:
        return False
    return True


def corte_a_pdf(numero: int) -> bytes:
    """PDF del corte con sus dieciséis apartados (§17).

    Si reportlab no está instalado se levanta un error explícito: no se
    devuelve un PDF vacío ni un sucedáneo.
    """
    if not _pdf_disponible():
        raise RuntimeError(
            "Exportación PDF no disponible: falta reportlab. Instálelo con "
            "`pip install reportlab` o exporte en JSON/CSV."
        )
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    corte = cortes.obtener(numero)
    if not corte:
        raise ValueError(f"No existe el corte {numero}.")
    snap = corte["snapshot"] or {}

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=letter,
        leftMargin=16 * mm, rightMargin=16 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
        title=corte["etiqueta"], author="ARGOS FORENSE",
    )
    base = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=base["Heading1"], fontSize=16, textColor=colors.HexColor("#0b2b3c"))
    h2 = ParagraphStyle("h2", parent=base["Heading2"], fontSize=11.5, textColor=colors.HexColor("#12556f"),
                        spaceBefore=10, spaceAfter=4)
    normal = ParagraphStyle("n", parent=base["BodyText"], fontSize=8.5, leading=11.5, alignment=TA_LEFT)
    pequeno = ParagraphStyle("s", parent=normal, fontSize=7.5, textColor=colors.HexColor("#4a5b66"))

    def tabla(cabeceras, filas, anchos=None):
        datos = [[Paragraph(f"<b>{c}</b>", pequeno) for c in cabeceras]]
        for fila in filas:
            datos.append([Paragraph(str(c if c is not None else "—"), pequeno) for c in fila])
        t = Table(datos, colWidths=anchos, repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbe7ec")),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#9fb4bf")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f6f8")]),
            ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ]))
        return t

    hist = []
    hist.append(Paragraph(corte["etiqueta"], h1))
    hist.append(Paragraph(
        f"Ventana {snap.get('ventana', {}).get('inicio', '—')} → {snap.get('ventana', {}).get('fin', '—')} · "
        f"Estado: {corte['estado']} · Sello SHA-256: {corte['sha256'] or 'sin sellar (borrador)'}", pequeno))
    hist.append(Spacer(1, 6))

    # 1 y 2
    re_ = snap.get("resumen_ejecutivo", {})
    hist.append(Paragraph("1. Resumen ejecutivo", h2))
    hist.append(tabla(
        ["Indicador", "Valor"],
        [[k.replace("_", " ").capitalize(), v] for k, v in re_.items()],
        [110 * mm, 60 * mm],
    ))
    tn = snap.get("total_nacional", {})
    hist.append(Paragraph("2. Total nacional", h2))
    hist.append(tabla(
        ["Categoría", "Eventos"],
        [[CATEGORIAS.get(k, k), v] for k, v in tn.get("por_categoria", {}).items()] +
        [["TOTAL", tn.get("total", 0)]],
        [120 * mm, 50 * mm],
    ))

    # 3-5
    for i, (clave, titulo) in enumerate(
        [("FOS", "3. Fosas clandestinas"), ("CAM", "4. Campamentos"), ("CSE", "5. Casas de seguridad")]
    ):
        bloque = snap.get("categorias", {}).get(clave, {})
        hist.append(Paragraph(titulo, h2))
        hist.append(Paragraph(
            f"Total activos: {bloque.get('total', 0)} · Nuevos en el corte: {len(bloque.get('nuevos', []))} · "
            f"Por nivel: {bloque.get('por_nivel', {})}", normal))
        if bloque.get("nuevos"):
            hist.append(tabla(
                ["Folio", "Entidad", "Municipio", "Nivel", "Resumen"],
                [[e["folio"], e["entidad"], e["municipio"], e["nivel_corroboracion"], e["resumen_factual"]]
                 for e in bloque["nuevos"]],
                [30 * mm, 25 * mm, 25 * mm, 12 * mm, 78 * mm],
            ))

    hist.append(PageBreak())

    # 6-9
    for titulo, clave, cols in (
        ("6. Nuevos eventos", "nuevos_eventos", None),
        ("7. Actualizaciones", "actualizaciones", None),
        ("8. Eventos confirmados", "eventos_confirmados", None),
        ("9. Eventos por verificar", "eventos_por_verificar", None),
    ):
        filas = snap.get(clave, [])
        hist.append(Paragraph(f"{titulo} ({len(filas)})", h2))
        if filas:
            hist.append(tabla(
                ["Folio", "Cat.", "Entidad", "Municipio", "Nivel", "Fuentes", "Resumen"],
                [[e["folio"], e["categoria"], e["entidad"], e["municipio"], e["nivel_corroboracion"],
                  e["num_fuentes"], e["resumen_factual"]] for e in filas],
                [28 * mm, 10 * mm, 22 * mm, 22 * mm, 11 * mm, 13 * mm, 64 * mm],
            ))
        else:
            hist.append(Paragraph("Sin registros en el corte.", pequeno))

    # 10
    hist.append(PageBreak())
    hist.append(Paragraph("10. Desglose por entidad", h2))
    hist.append(tabla(
        ["Entidad", "Región", "Fosas", "Camp.", "Casas", "Nuevos", "Total"],
        [[v["entidad"], v["region"], v["por_categoria"].get("FOS", 0), v["por_categoria"].get("CAM", 0),
          v["por_categoria"].get("CSE", 0), v["nuevos"], v["total"]]
         for v in snap.get("desglose_por_entidad", {}).values()],
        [42 * mm, 26 * mm, 18 * mm, 18 * mm, 18 * mm, 20 * mm, 18 * mm],
    ))

    # 11
    hist.append(Paragraph("11. Mapa nacional", h2))
    hist.append(Paragraph(
        snap.get("mapa_nacional", {}).get("nota", "")
        + " El mapa interactivo vive en la aplicación; aquí se reproduce su conteo por entidad.", normal))

    # 12
    comp = snap.get("comparacion", {})
    hist.append(Paragraph("12. Comparación con el corte anterior", h2))
    hist.append(Paragraph(comp.get("encabezado", "—"), normal))
    if comp.get("cambios_de_nivel"):
        hist.append(tabla(
            ["Folio", "Corte anterior", "Corte actual", "Motivo"],
            [[c["folio"], c["corte_anterior"], c["corte_actual"], c["motivo"]] for c in comp["cambios_de_nivel"]],
            [30 * mm, 22 * mm, 22 * mm, 96 * mm],
        ))
    else:
        hist.append(Paragraph("Sin cambios de nivel respecto del corte anterior.", pequeno))

    # 13
    hist.append(Paragraph("13. Fuentes utilizadas", h2))
    fuentes = snap.get("fuentes_utilizadas", [])
    hist.append(
        tabla(["Nivel", "Medio o institución", "Notas"], [[f["nivel"], f["medio"], f["notas"]] for f in fuentes],
             [18 * mm, 110 * mm, 20 * mm])
        if fuentes else Paragraph("Sin fuentes nuevas ligadas durante la ventana.", pequeno)
    )

    # 14
    hist.append(Paragraph("14. Pendientes de corroboración", h2))
    pend = snap.get("pendientes_de_corroboracion", [])
    hist.append(
        tabla(["Folio", "Nivel", "Entidad", "Resumen"],
              [[p["folio"], p["nivel_corroboracion"], geo.nombre(p["entidad_iso"]), p["resumen_factual"]] for p in pend],
              [30 * mm, 12 * mm, 28 * mm, 100 * mm])
        if pend else Paragraph("Sin eventos pendientes de corroboración.", pequeno)
    )

    # 15
    hist.append(PageBreak())
    hist.append(Paragraph("15. Metodología", h2))
    met = snap.get("metodologia", {})
    hist.append(tabla(
        ["Nivel", "Definición"],
        [[k, v] for k, v in met.get("niveles_corroboracion", {}).items()], [16 * mm, 154 * mm]))
    hist.append(Spacer(1, 4))
    for clave in ("regla_de_validacion", "regla_de_duplicidad", "regla_de_atribucion", "regla_de_seguridad"):
        if met.get(clave):
            hist.append(Paragraph(f"• {met[clave]}", normal))

    # 16
    hist.append(Paragraph("16. Bitácora de integridad", h2))
    hist.append(tabla(
        ["Concepto", "Valor"],
        [[k.replace("_", " ").capitalize(), v] for k, v in snap.get("bitacora_integridad", {}).items()],
        [110 * mm, 60 * mm]))
    hist.append(Spacer(1, 6))
    hist.append(Paragraph(
        "ARGOS FORENSE · Uso institucional · Producto OSINT: no contiene información operativa "
        "ni ubicación táctica (§20).", pequeno))

    doc.build(hist)
    return buffer.getvalue()
