"""Bandeja de validación (§8).

Es la única puerta entre lo detectado y el registro definitivo: «Nada detectado
deberá pasar automáticamente al registro definitivo» (§4). Cada acción de este
módulo exige usuario y deja bitácora; ninguna borra filas (§14).
"""

from __future__ import annotations

from .. import db
from ..config import CATEGORIAS, CONFIG
from . import auditoria, dedupe, eventos, geo, seguridad

ESTADOS_BANDEJA = ("PENDIENTE", "VALIDADO", "DESCARTADO", "DUPLICADO", "VINCULADO")


class ErrorBandeja(ValueError):
    pass


def _decorar(item: dict) -> dict:
    ent = geo.entidad(item.get("entidad_iso")) or {}
    item["entidad"] = ent.get("nombre")
    item["region"] = ent.get("region")
    item["categoria_nombre"] = CATEGORIAS.get(item.get("categoria_detectada") or "", None)
    item["terminos"] = db.dejs(item.get("terminos"), [])
    item["riesgo_opsec"] = db.dejs(item.get("riesgo_opsec"), {})
    item["duplicados_abiertos"] = db.escalar(
        "SELECT COUNT(*) FROM duplicate_candidates WHERE raw_item_id = ? AND estado = 'ABIERTO'",
        (item["id"],),
    )
    return item


def listar(
    *,
    estado: str | None = "PENDIENTE",
    categoria: str | None = None,
    entidad_iso: str | None = None,
    confianza_min: int | None = None,
    q: str | None = None,
    limite: int = 100,
    desplazamiento: int = 0,
) -> dict:
    condiciones, params = [], []
    if estado:
        condiciones.append("estado = ?"); params.append(estado.upper())
    if categoria:
        condiciones.append("categoria_detectada = ?"); params.append(categoria.upper())
    if entidad_iso:
        condiciones.append("entidad_iso = ?"); params.append(entidad_iso)
    if confianza_min is not None:
        condiciones.append("confianza_pct >= ?"); params.append(int(confianza_min))
    if q:
        condiciones.append("(titulo LIKE ? OR resumen LIKE ? OR medio LIKE ?)")
        params += [f"%{q}%"] * 3
    donde = ("WHERE " + " AND ".join(condiciones)) if condiciones else ""
    total = db.escalar(f"SELECT COUNT(*) FROM raw_items {donde}", params)
    filas = db.consultar(
        f"SELECT * FROM raw_items {donde} ORDER BY confianza_pct DESC, fecha_deteccion DESC, id DESC "
        f"LIMIT ? OFFSET ?",
        [*params, limite, desplazamiento],
    )
    return {
        "total": total,
        "limite": limite,
        "desplazamiento": desplazamiento,
        "items": [_decorar(f) for f in filas],
    }


def obtener(raw_id: int) -> dict | None:
    fila = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (raw_id,))
    return _decorar(fila) if fila else None


# ---------------------------------------------------------- deduplicación ---
def duplicados(raw_id: int, umbral: int | None = None, recalcular: bool = True) -> dict:
    """Posibles duplicados de un registro (§12). Nunca fusiona: propone."""
    item = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (raw_id,))
    if not item:
        raise ErrorBandeja(f"Registro inexistente: {raw_id}")
    umbral = CONFIG.umbral_duplicado if umbral is None else umbral

    # Universo: eventos activos de la misma categoría o entidad, y otros
    # registros recientes de la bandeja.
    universo = db.consultar(
        """
        SELECT folio, categoria AS categoria_detectada, entidad_iso, municipio, localidad,
               resumen_factual AS titulo, fecha_probable_evento, num_cuerpos, nivel_corroboracion
        FROM events
        WHERE estado = 'ACTIVO' AND (categoria = ? OR entidad_iso = ?)
        ORDER BY fecha_deteccion DESC LIMIT 400
        """,
        (item.get("categoria_detectada") or "", item.get("entidad_iso") or ""),
    )
    universo += db.consultar(
        """
        SELECT id, titulo, resumen, entidad_iso, municipio, categoria_detectada,
               fecha_publicacion, estado
        FROM raw_items
        WHERE id <> ? AND estado IN ('PENDIENTE','VALIDADO','VINCULADO')
        ORDER BY id DESC LIMIT 400
        """,
        (raw_id,),
    )
    props = dedupe.candidatos(item, universo, umbral=umbral)

    if recalcular:
        # Sólo se dan de alta candidatos nuevos: un candidato ya resuelto por una
        # persona no se reabre porque el rastreo vuelva a puntuarlo.
        for p in props:
            es_evento = p["tipo"] == "evento"
            ya = db.consultar_uno(
                "SELECT id FROM duplicate_candidates WHERE raw_item_id = ? AND "
                + ("folio = ?" if es_evento else "otro_raw_id = ?"),
                (raw_id, p["referencia"]),
            )
            if ya:
                continue
            db.insertar("duplicate_candidates", {
                "raw_item_id": raw_id,
                "otro_raw_id": None if es_evento else int(p["referencia"]),
                "folio": p["referencia"] if es_evento else None,
                "puntaje": p["puntaje"],
                "desglose": db.js(p["desglose"]),
                "estado": "ABIERTO",
                "creado_en": db.ahora_iso(),
            })

    registrados = db.consultar(
        "SELECT * FROM duplicate_candidates WHERE raw_item_id = ? ORDER BY puntaje DESC", (raw_id,)
    )
    for r in registrados:
        r["desglose"] = db.dejs(r["desglose"], {})
        r["etiqueta"] = f"POSIBLE DUPLICIDAD: {r['puntaje']} %"
    return {
        "raw_item_id": raw_id,
        "umbral": umbral,
        "nota": "El sistema nunca fusiona por sí solo (§12). Opciones: FUSIONAR · "
                "MANTENER SEPARADOS · VINCULAR COMO FUENTE ADICIONAL.",
        "candidatos": registrados,
    }


def resolver_duplicado(candidato_id: int, decision: str, *, usuario: str, motivo: str) -> dict:
    """FUSIONAR / MANTENER_SEPARADOS / VINCULAR — siempre decisión humana (§12)."""
    decision = decision.upper().replace(" ", "_")
    validas = {"FUSIONAR", "MANTENER_SEPARADOS", "VINCULAR"}
    if decision not in validas:
        raise ErrorBandeja(f"Decisión inválida: {decision!r}. Válidas: {', '.join(sorted(validas))}")
    cand = db.consultar_uno("SELECT * FROM duplicate_candidates WHERE id = ?", (candidato_id,))
    if not cand:
        raise ErrorBandeja(f"Candidato inexistente: {candidato_id}")
    if not motivo or not motivo.strip():
        raise ErrorBandeja("Toda resolución de duplicidad exige motivo (§14).")

    estado = {"FUSIONAR": "FUSIONADO", "MANTENER_SEPARADOS": "SEPARADOS", "VINCULAR": "VINCULADO"}[decision]
    db.actualizar(
        "duplicate_candidates",
        {"estado": estado, "resuelto_por": usuario, "resuelto_en": db.ahora_iso()},
        "id = ?", (candidato_id,),
    )
    auditoria.registrar(
        usuario=usuario, proceso="dedupe", entidad_tipo="duplicate_candidate", entidad_id=candidato_id,
        evento=cand["folio"], campo="estado", valor_anterior=cand["estado"], valor_nuevo=estado,
        motivo=f"{motivo} · puntaje {cand['puntaje']} %",
    )

    resultado = {"candidato": candidato_id, "decision": decision, "estado": estado}
    if decision in ("FUSIONAR", "VINCULAR") and cand["folio"]:
        item = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (cand["raw_item_id"],))
        if item:
            eventos.ligar_fuente(
                cand["folio"], item, usuario=usuario,
                tipo_aporte="CORROBORACION",
                motivo=f"{decision} desde bandeja · {motivo}",
            )
            _marcar(item["id"], "DUPLICADO" if decision == "FUSIONAR" else "VINCULADO",
                    folio=cand["folio"], usuario=usuario, motivo=motivo)
            resultado["folio"] = cand["folio"]
    return resultado


# ------------------------------------------------------------- decisiones ---
def _marcar(raw_id: int, estado: str, *, folio: str | None, usuario: str, motivo: str) -> None:
    anterior = db.consultar_uno("SELECT estado FROM raw_items WHERE id = ?", (raw_id,))
    db.actualizar(
        "raw_items",
        {"estado": estado, "folio": folio, "motivo": motivo,
         "revisado_por": usuario, "revisado_en": db.ahora_iso()},
        "id = ?", (raw_id,),
    )
    auditoria.registrar(
        usuario=usuario, proceso="bandeja", entidad_tipo="raw_item", entidad_id=raw_id, evento=folio,
        campo="estado", valor_anterior=(anterior or {}).get("estado"), valor_nuevo=estado, motivo=motivo,
    )


def validar(raw_id: int, *, usuario: str, motivo: str = "", **datos) -> dict:
    """VALIDAR: emite folio y crea la ficha del evento (§9, §10)."""
    item = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (raw_id,))
    if not item:
        raise ErrorBandeja(f"Registro inexistente: {raw_id}")
    if item["estado"] != "PENDIENTE":
        raise ErrorBandeja(f"El registro {raw_id} ya fue resuelto como {item['estado']}.")
    folio = eventos.crear_desde_raw(
        item, usuario=usuario, motivo=motivo or "Validado en bandeja", **datos
    )
    _marcar(raw_id, "VALIDADO", folio=folio, usuario=usuario, motivo=motivo or "Validado en bandeja")
    return {"raw_item_id": raw_id, "folio": folio, "ficha": eventos.ficha(folio)}


def descartar(raw_id: int, *, usuario: str, motivo: str) -> dict:
    """DESCARTAR: el registro se conserva con estado DESCARTADO (§14), nunca se borra."""
    if not motivo or not motivo.strip():
        raise ErrorBandeja("Descartar exige motivo (§14).")
    item = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (raw_id,))
    if not item:
        raise ErrorBandeja(f"Registro inexistente: {raw_id}")
    _marcar(raw_id, "DESCARTADO", folio=None, usuario=usuario, motivo=motivo)
    return {"raw_item_id": raw_id, "estado": "DESCARTADO", "motivo": motivo}


def vincular(raw_id: int, folio: str, *, usuario: str, motivo: str = "", tipo_aporte: str = "CORROBORACION") -> dict:
    """VINCULAR A EVENTO EXISTENTE: una fuente más para un evento ya abierto (§13)."""
    item = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (raw_id,))
    if not item:
        raise ErrorBandeja(f"Registro inexistente: {raw_id}")
    if not eventos.obtener(folio):
        raise ErrorBandeja(f"Evento inexistente: {folio}")
    resultado = eventos.ligar_fuente(
        folio, item, usuario=usuario, tipo_aporte=tipo_aporte,
        motivo=motivo or "Vinculado desde bandeja",
    )
    _marcar(raw_id, "VINCULADO", folio=folio, usuario=usuario, motivo=motivo or "Vinculado desde bandeja")
    return {"raw_item_id": raw_id, "folio": folio, **resultado}


def marcar_posible_duplicado(raw_id: int, *, usuario: str, motivo: str = "") -> dict:
    """POSIBLE DUPLICADO: aparta el registro sin decidir todavía."""
    item = db.consultar_uno("SELECT * FROM raw_items WHERE id = ?", (raw_id,))
    if not item:
        raise ErrorBandeja(f"Registro inexistente: {raw_id}")
    _marcar(raw_id, "DUPLICADO", folio=item["folio"], usuario=usuario,
            motivo=motivo or "Marcado como posible duplicado; pendiente de arbitraje")
    return {"raw_item_id": raw_id, "estado": "DUPLICADO"}


# ------------------------------------------------------------------- alta ---
def registrar_hallazgo(datos: dict) -> int | None:
    """Alta de un registro detectado por el rastreo. Devuelve el id, o None si ya existía.

    El registro nace PENDIENTE. No hay ninguna vía por la que un hallazgo se
    convierta en evento sin pasar por `validar()`.
    """
    url = (datos.get("url") or "").strip()
    if not url:
        return None
    from .evidencia import hash_url

    huella = hash_url(url)
    if db.consultar_uno("SELECT id FROM raw_items WHERE url_hash = ?", (huella,)):
        return None

    revision = seguridad.revisar(datos.get("titulo") or "", datos.get("resumen") or "", datos.get("texto") or "")
    ahora = db.ahora_iso()
    raw_id = db.insertar("raw_items", {
        "source_id": datos.get("source_id"),
        "collective_id": datos.get("collective_id"),
        "url": url,
        "url_hash": huella,
        "titulo": (datos.get("titulo") or "").strip()[:500] or "(sin título)",
        "medio": datos.get("medio"),
        "nivel_fuente": datos.get("nivel_fuente"),
        "fecha_publicacion": datos.get("fecha_publicacion"),
        "fecha_deteccion": ahora,
        "categoria_detectada": datos.get("categoria_detectada"),
        "subcategoria": datos.get("subcategoria"),
        "entidad_iso": datos.get("entidad_iso"),
        "entidad_confianza": datos.get("entidad_confianza"),
        "municipio": datos.get("municipio"),
        "resumen": datos.get("resumen"),
        "terminos": db.js(datos.get("terminos") or []),
        "confianza_pct": int(datos.get("confianza_pct") or 0),
        "riesgo_opsec": db.js(revision.como_dict()),
        "estado": "PENDIENTE",
        "corte_deteccion": datos.get("corte_deteccion"),
        "creado_en": ahora,
    })
    auditoria.registrar(
        usuario="sistema", proceso="rastreo", entidad_tipo="raw_item", entidad_id=raw_id,
        campo="estado", valor_anterior=None, valor_nuevo="PENDIENTE",
        motivo="Alta por rastreo automático", fuente_origen=url,
    )
    return raw_id
