"""Corte histórico de 72 horas (§16, §17, §18).

Un corte publicado **no se modifica**: su contenido queda congelado en un
snapshot JSON sellado con SHA-256 y cualquier cambio posterior aparece en el
corte siguiente. Ese sello es lo que hace verificable la bitácora de integridad.
"""

from __future__ import annotations

import hashlib
import json
from datetime import timedelta

from .. import db
from ..config import CATEGORIAS, CONFIG, NIVELES_CORROBORACION
from . import auditoria, corroboracion, geo


class CorteInmutable(RuntimeError):
    """§16: un corte publicado no admite modificación."""


class ErrorCorte(ValueError):
    pass


def _sellar(snapshot: dict) -> str:
    canonico = json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonico.encode("utf-8")).hexdigest()


def ultimo_publicado() -> dict | None:
    return db.consultar_uno("SELECT * FROM cuts WHERE estado = 'PUBLICADO' ORDER BY numero DESC LIMIT 1")


def borrador_abierto() -> dict | None:
    return db.consultar_uno("SELECT * FROM cuts WHERE estado = 'BORRADOR' ORDER BY numero DESC LIMIT 1")


def obtener(numero: int) -> dict | None:
    fila = db.consultar_uno("SELECT * FROM cuts WHERE numero = ?", (numero,))
    if fila:
        fila["snapshot"] = db.dejs(fila["snapshot"], None)
    return fila


def listar(limite: int = 100) -> list[dict]:
    filas = db.consultar(
        "SELECT id, numero, etiqueta, ventana_inicio, ventana_fin, estado, generado_en, "
        "publicado_en, publicado_por, corte_anterior, sha256 FROM cuts ORDER BY numero DESC LIMIT ?",
        (limite,),
    )
    return filas


# ------------------------------------------------------------- generación ---
def _ventana(horas: int) -> tuple[str, str]:
    fin = db.ahora()
    anterior = ultimo_publicado()
    if anterior:
        inicio_iso = anterior["ventana_fin"]
    else:
        inicio_iso = (fin - timedelta(hours=horas)).isoformat(timespec="seconds")
    return inicio_iso, fin.isoformat(timespec="seconds")


def _eventos_de_ventana(inicio: str, fin: str) -> tuple[list[dict], list[dict]]:
    """Devuelve (nuevos, actualizados) dentro de la ventana."""
    nuevos = db.consultar(
        "SELECT * FROM events WHERE creado_en >= ? AND creado_en <= ? ORDER BY folio", (inicio, fin)
    )
    folios_nuevos = {e["folio"] for e in nuevos}
    actualizados = [
        e for e in db.consultar(
            "SELECT * FROM events WHERE ultima_actualizacion >= ? AND ultima_actualizacion <= ? ORDER BY folio",
            (inicio, fin),
        )
        if e["folio"] not in folios_nuevos
    ]
    return nuevos, actualizados


def _resumen_evento(ev: dict) -> dict:
    ent = geo.entidad(ev["entidad_iso"]) or {}
    return {
        "folio": ev["folio"],
        "categoria": ev["categoria"],
        "categoria_nombre": CATEGORIAS.get(ev["categoria"], ev["categoria"]),
        "subcategoria": ev["subcategoria"],
        "entidad_iso": ev["entidad_iso"],
        "entidad": ent.get("nombre"),
        "region": ent.get("region"),
        "municipio": ev["municipio"],
        "localidad": ev["localidad"],
        "fecha_probable_evento": ev["fecha_probable_evento"],
        "fecha_deteccion": ev["fecha_deteccion"],
        "resumen_factual": ev["resumen_factual"],
        "nivel_corroboracion": ev["nivel_corroboracion"],
        "nivel_etiqueta": corroboracion.ETIQUETAS.get(ev["nivel_corroboracion"], ""),
        "estado": ev["estado"],
        "num_fuentes": db.escalar("SELECT COUNT(*) FROM event_sources WHERE folio = ?", (ev["folio"],)),
    }


def _comparar(numero_actual: int, corte_anterior: dict | None, nuevos: list[dict], actualizados: list[dict]) -> dict:
    """§18: qué cambió respecto del corte anterior."""
    if not corte_anterior:
        return {
            "encabezado": f"CORTE {numero_actual:03d} — primer corte de la serie",
            "sin_corte_anterior": True,
            "nuevos_eventos": len(nuevos),
        }
    previo = {
        f["folio"]: f
        for f in db.consultar("SELECT * FROM cut_events WHERE cut_id = ?", (corte_anterior["id"],))
    }
    cambios_nivel = []
    for ev in actualizados + nuevos:
        antes = previo.get(ev["folio"])
        if antes and antes["nivel_corroboracion"] != ev["nivel_corroboracion"]:
            motivo = db.consultar_uno(
                "SELECT motivo FROM audit WHERE evento = ? AND campo = 'nivel_corroboracion' "
                "ORDER BY id DESC LIMIT 1", (ev["folio"],)
            )
            cambios_nivel.append({
                "folio": ev["folio"],
                "corte_anterior": antes["nivel_corroboracion"],
                "corte_actual": ev["nivel_corroboracion"],
                "motivo": (motivo or {}).get("motivo") or "Sin motivo registrado",
            })
    estados_previos = {f["entidad_iso"] for f in previo.values()}
    estados_actuales = {e["entidad_iso"] for e in nuevos + actualizados}
    descartados = db.consultar(
        "SELECT folio, fusionado_en FROM events WHERE estado IN ('DUPLICADO','FUSIONADO') "
        "AND ultima_actualizacion >= ? AND ultima_actualizacion <= ?",
        (corte_anterior["ventana_fin"], db.ahora_iso()),
    )
    return {
        "encabezado": f"CORTE {numero_actual:03d} VS CORTE {corte_anterior['numero']:03d}",
        "sin_corte_anterior": False,
        "nuevos_eventos": len(nuevos),
        "eventos_actualizados": len(actualizados),
        "cambios_de_nivel": cambios_nivel,
        "nuevos_estados_con_actividad": sorted(
            {geo.nombre(i) for i in (estados_actuales - estados_previos) if i}
        ),
        "registros_descartados_como_duplicados": descartados,
    }


def generar(*, usuario: str = "sistema", horas: int | None = None) -> dict:
    """Genera el corte como BORRADOR. Publicarlo es un acto aparte (§16)."""
    abierto = borrador_abierto()
    if abierto:
        raise ErrorCorte(
            f"Ya existe un corte en borrador: {abierto['etiqueta']}. Publíquelo o descártelo antes de generar otro."
        )
    horas = horas or int(db.config_get("corte_horas", CONFIG.corte_horas))
    inicio, fin = _ventana(horas)
    anterior = ultimo_publicado()
    numero = (db.escalar("SELECT MAX(numero) FROM cuts", (), 0) or 0) + 1
    etiqueta = f"ARGOS FORENSE — CORTE {numero:03d}"

    nuevos, actualizados = _eventos_de_ventana(inicio, fin)
    activos = db.consultar("SELECT * FROM events WHERE estado = 'ACTIVO'")

    por_categoria = {c: [] for c in CATEGORIAS}
    for ev in activos:
        por_categoria.setdefault(ev["categoria"], []).append(ev)

    por_entidad: dict[str, dict] = {}
    for ent in geo.entidades():
        iso = ent["iso"]
        de_entidad = [e for e in activos if e["entidad_iso"] == iso]
        nuevos_ent = [e for e in nuevos if e["entidad_iso"] == iso]
        por_entidad[iso] = {
            "entidad": ent["nombre"],
            "region": ent["region"],
            "total": len(de_entidad),
            "por_categoria": {c: sum(1 for e in de_entidad if e["categoria"] == c) for c in CATEGORIAS},
            "nuevos": len(nuevos_ent),
            "por_nivel": {n: sum(1 for e in de_entidad if e["nivel_corroboracion"] == n) for n in NIVELES_CORROBORACION},
            "con_actividad": bool(nuevos_ent),
        }

    fuentes_usadas = db.consultar(
        """
        SELECT es.nivel, COALESCE(es.medio, s.nombre) AS medio, COUNT(*) AS notas
        FROM event_sources es LEFT JOIN sources s ON s.id = es.source_id
        WHERE es.creado_en >= ? AND es.creado_en <= ?
        GROUP BY es.nivel, medio ORDER BY es.nivel, notas DESC
        """,
        (inicio, fin),
    )
    pendientes = db.consultar(
        "SELECT folio, entidad_iso, categoria, nivel_corroboracion, resumen_factual FROM events "
        "WHERE estado = 'ACTIVO' AND nivel_corroboracion IN ('C','D') ORDER BY nivel_corroboracion DESC, folio"
    )
    bandeja_pendiente = db.escalar("SELECT COUNT(*) FROM raw_items WHERE estado = 'PENDIENTE'")

    snapshot = {
        "etiqueta": etiqueta,
        "numero": numero,
        "ventana": {"inicio": inicio, "fin": fin, "horas": horas},
        "generado_en": db.ahora_iso(),
        # 1. Resumen ejecutivo
        "resumen_ejecutivo": {
            "eventos_activos": len(activos),
            "nuevos_en_el_corte": len(nuevos),
            "actualizados_en_el_corte": len(actualizados),
            "entidades_con_actividad": sum(1 for v in por_entidad.values() if v["con_actividad"]),
            "confirmados": sum(1 for e in activos if e["nivel_corroboracion"] == "A"),
            "por_verificar": sum(1 for e in activos if e["nivel_corroboracion"] == "D"),
            "pendientes_en_bandeja": bandeja_pendiente,
        },
        # 2. Total nacional
        "total_nacional": {
            "por_categoria": {c: len(v) for c, v in por_categoria.items()},
            "por_nivel": {n: sum(1 for e in activos if e["nivel_corroboracion"] == n) for n in NIVELES_CORROBORACION},
            "total": len(activos),
        },
        # 3-5. Cada categoría
        "categorias": {
            c: {
                "nombre": CATEGORIAS[c],
                "total": len(por_categoria.get(c, [])),
                "nuevos": [_resumen_evento(e) for e in nuevos if e["categoria"] == c],
                "por_nivel": {
                    n: sum(1 for e in por_categoria.get(c, []) if e["nivel_corroboracion"] == n)
                    for n in NIVELES_CORROBORACION
                },
            }
            for c in CATEGORIAS
        },
        # 6-9
        "nuevos_eventos": [_resumen_evento(e) for e in nuevos],
        "actualizaciones": [_resumen_evento(e) for e in actualizados],
        "eventos_confirmados": [_resumen_evento(e) for e in activos if e["nivel_corroboracion"] == "A"],
        "eventos_por_verificar": [_resumen_evento(e) for e in activos if e["nivel_corroboracion"] == "D"],
        # 10
        "desglose_por_entidad": por_entidad,
        # 11
        "mapa_nacional": {
            "tipo": "conteo_por_entidad",
            "nota": "Coloreado por entidad. No incluye ubicación fina de ningún evento (§20).",
            "datos": {iso: v["total"] for iso, v in por_entidad.items()},
        },
        # 12
        "comparacion": _comparar(numero, anterior, nuevos, actualizados),
        # 13
        "fuentes_utilizadas": fuentes_usadas,
        # 14
        "pendientes_de_corroboracion": pendientes,
        # 15
        "metodologia": {
            "categorias": CATEGORIAS,
            "niveles_corroboracion": NIVELES_CORROBORACION,
            "regla_de_validacion": "Ningún hallazgo del rastreo llega al registro definitivo sin validación humana (§4, §8).",
            "regla_de_duplicidad": "El sistema puntúa la posible duplicidad y nunca fusiona por sí solo (§12).",
            "regla_de_atribucion": "No se atribuye un sitio a ninguna organización salvo que una fuente identificable lo haya hecho, y la atribución va ligada a esa fuente (§21).",
            "regla_de_seguridad": "No se publican coordenadas precisas, domicilios ni datos personales; la ubicación se expone generalizada (§20).",
            "ventana": f"{horas} horas",
        },
    }
    # 16. Bitácora de integridad
    snapshot["bitacora_integridad"] = {
        "eventos_en_snapshot": len(activos),
        "movimientos_registrados_en_ventana": db.escalar(
            "SELECT COUNT(*) FROM audit WHERE ts >= ? AND ts <= ?", (inicio, fin)
        ),
        "altas_en_bandeja_en_ventana": db.escalar(
            "SELECT COUNT(*) FROM raw_items WHERE fecha_deteccion >= ? AND fecha_deteccion <= ?", (inicio, fin)
        ),
        "descartes_en_ventana": db.escalar(
            "SELECT COUNT(*) FROM raw_items WHERE estado = 'DESCARTADO' AND revisado_en >= ? AND revisado_en <= ?",
            (inicio, fin),
        ),
        "corte_anterior": anterior["numero"] if anterior else None,
        "sello_corte_anterior": anterior["sha256"] if anterior else None,
    }

    cut_id = db.insertar("cuts", {
        "numero": numero,
        "etiqueta": etiqueta,
        "ventana_inicio": inicio,
        "ventana_fin": fin,
        "estado": "BORRADOR",
        "generado_en": db.ahora_iso(),
        "corte_anterior": anterior["id"] if anterior else None,
        "snapshot": db.js(snapshot),
        "sha256": None,
        "creado_en": db.ahora_iso(),
    })
    folios_nuevos = {e["folio"] for e in nuevos}
    folios_act = {e["folio"] for e in actualizados}
    for ev in activos:
        db.insertar("cut_events", {
            "cut_id": cut_id,
            "folio": ev["folio"],
            "categoria": ev["categoria"],
            "entidad_iso": ev["entidad_iso"],
            "nivel_corroboracion": ev["nivel_corroboracion"],
            "estado": ev["estado"],
            "es_nuevo": 1 if ev["folio"] in folios_nuevos else 0,
            "es_actualizado": 1 if ev["folio"] in folios_act else 0,
            "num_fuentes": db.escalar("SELECT COUNT(*) FROM event_sources WHERE folio = ?", (ev["folio"],)),
        })
    auditoria.registrar(
        usuario=usuario, proceso="corte", entidad_tipo="cut", entidad_id=cut_id,
        campo="estado", valor_anterior=None, valor_nuevo="BORRADOR",
        motivo=f"Generación de {etiqueta} · ventana {inicio} → {fin}",
    )
    return {"id": cut_id, "numero": numero, "etiqueta": etiqueta, "estado": "BORRADOR", "snapshot": snapshot}


def publicar(numero: int, *, usuario: str) -> dict:
    """Sella el corte. A partir de aquí no se modifica (§16)."""
    fila = db.consultar_uno("SELECT * FROM cuts WHERE numero = ?", (numero,))
    if not fila:
        raise ErrorCorte(f"No existe el corte {numero}.")
    if fila["estado"] == "PUBLICADO":
        raise CorteInmutable(
            f"El corte {numero:03d} ya está publicado y no puede modificarse (§16). "
            "Cualquier cambio aparece en el corte siguiente."
        )
    snapshot = db.dejs(fila["snapshot"], {}) or {}
    snapshot["publicado_en"] = db.ahora_iso()
    snapshot["publicado_por"] = usuario
    sello = _sellar(snapshot)
    db.actualizar(
        "cuts",
        {"estado": "PUBLICADO", "publicado_en": snapshot["publicado_en"], "publicado_por": usuario,
         "snapshot": db.js(snapshot), "sha256": sello},
        "numero = ?", (numero,),
    )
    auditoria.registrar(
        usuario=usuario, proceso="corte", entidad_tipo="cut", entidad_id=fila["id"],
        campo="estado", valor_anterior="BORRADOR", valor_nuevo="PUBLICADO",
        motivo=f"Publicación de {fila['etiqueta']} · sello SHA-256 {sello}",
    )
    return {"numero": numero, "etiqueta": fila["etiqueta"], "estado": "PUBLICADO", "sha256": sello}


def verificar_sello(numero: int) -> dict:
    """Recalcula el sello del corte publicado y lo compara con el registrado."""
    fila = db.consultar_uno("SELECT * FROM cuts WHERE numero = ?", (numero,))
    if not fila:
        raise ErrorCorte(f"No existe el corte {numero}.")
    if fila["estado"] != "PUBLICADO":
        return {"numero": numero, "estado": fila["estado"], "sellado": False}
    snapshot = db.dejs(fila["snapshot"], {}) or {}
    actual = _sellar(snapshot)
    return {
        "numero": numero,
        "estado": "PUBLICADO",
        "sellado": True,
        "sha256_registrado": fila["sha256"],
        "sha256_actual": actual,
        "integro": actual == fila["sha256"],
    }


def comparar_cortes(numero_a: int, numero_b: int) -> dict:
    """§18: comparación explícita entre dos cortes ya generados."""
    a = db.consultar_uno("SELECT * FROM cuts WHERE numero = ?", (numero_a,))
    b = db.consultar_uno("SELECT * FROM cuts WHERE numero = ?", (numero_b,))
    if not a or not b:
        raise ErrorCorte("Alguno de los dos cortes no existe.")
    ev_a = {f["folio"]: f for f in db.consultar("SELECT * FROM cut_events WHERE cut_id = ?", (a["id"],))}
    ev_b = {f["folio"]: f for f in db.consultar("SELECT * FROM cut_events WHERE cut_id = ?", (b["id"],))}
    cambios = []
    for folio, fila_a in ev_a.items():
        fila_b = ev_b.get(folio)
        if fila_b and fila_a["nivel_corroboracion"] != fila_b["nivel_corroboracion"]:
            motivo = db.consultar_uno(
                "SELECT motivo FROM audit WHERE evento = ? AND campo = 'nivel_corroboracion' ORDER BY id DESC LIMIT 1",
                (folio,),
            )
            cambios.append({
                "folio": folio,
                f"corte_{numero_b:03d}": fila_b["nivel_corroboracion"],
                f"corte_{numero_a:03d}": fila_a["nivel_corroboracion"],
                "motivo": (motivo or {}).get("motivo") or "Sin motivo registrado",
            })
    return {
        "encabezado": f"CORTE {numero_a:03d} VS CORTE {numero_b:03d}",
        "nuevos_eventos": sorted(set(ev_a) - set(ev_b)),
        "eventos_actualizados": sorted(f for f, v in ev_a.items() if v["es_actualizado"]),
        "cambios_de_nivel": cambios,
        "nuevos_estados_con_actividad": sorted(
            {geo.nombre(v["entidad_iso"]) for f, v in ev_a.items() if f not in ev_b}
        ),
        "eventos_ausentes_en_el_actual": sorted(set(ev_b) - set(ev_a)),
    }
