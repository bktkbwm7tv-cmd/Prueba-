#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva la versión en TEXTO de una edición ARGOS a partir de su cartelón.

No reescribe contenido: extrae el del escritorio ya publicado, de modo que el
texto no pueda divergir del cartelón — que es justo el fallo que se produce
cuando el .txt se conserva del borrador y el cartelón se corrige después.
"""
import html as H
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()


SENT = "\x00"


def limpia(x, saltos=True):
    """HTML → texto.

    Los saltos del FUENTE no son saltos del documento: el cartelón parte sus
    párrafos a ~100 columnas para poder leerse, y tomarlos por separadores
    producía una línea en blanco cada dos renglones. Solo `<br>` separa.
    """
    x = re.sub(r"<br\s*/?>", SENT if saltos else " · ", x, flags=re.I)
    x = re.sub(r"<[^>]+>", "", x)
    x = H.unescape(x)
    x = re.sub(r"\s+", " ", x)
    partes = [re.sub(r" +", " ", t).strip() for t in x.split(SENT)]
    return "\n".join(t for t in partes if t).strip()


def plegar(t, ancho=96):
    """Repliega a ancho fijo, respetando los saltos ya decididos."""
    import textwrap
    fuera = []
    for ln in t.split("\n"):
        fuera += textwrap.wrap(ln, ancho) or [""]
    return fuera


SEP = "=" * 76
RAYA = "-" * 76
out = []

# Cabecera, tomada del propio cartelón.
num = re.search(r'<span class="n">(\d+)</span>', s).group(1)
fecha = re.search(r"<b>Fecha:</b>\s*([\d-]+)", s).group(1)
hora = re.search(r"<b>Hora:</b>\s*([\d:]+)", s).group(1)
# El turno del corte se DERIVA del pie del cartelón, nunca se fija:
# ARGOS 120 publicó un .txt que decía "matutino" sobre un corte vespertino.
_m = re.search(r"<span>Corte:\s*([^<]+?)\s*</span>", s)
corte_turno = _m.group(1) if _m else "No declarado"
_v = re.search(r"Ventana <b>(.*?)</b> \(<b>(.*?)</b>\)", s)
if _v is None:
    raise SystemExit(
        "gen-texto: el cartelón no declara la ventana en el formato canónico.\n"
        "  Esperado, literal:  Ventana <b>DD-mes HH:MM \u2192 DD-mes HH:MM CDMX</b> (<b>N h N min</b>)\n"
        "  Corrija el CARTELÓN, no esta herramienta: la ventana es dato obligatorio del producto."
    )
vent = limpia(_v.group(0), False)
out += [
    f"ARGOS {num} — REPORTE NACIONAL DE SEGURIDAD",
    "REPORTE DIARIO DE INTELIGENCIA CRIMINAL",
    "«INVESTIGACIONES, BÚSQUEDA Y VERDAD»",
    "",
    f"Corte informativo: {fecha} · {hora} (CDMX)",
    vent.replace("Ventana ", "Ventana: "),
    f"Versión 3.0 · Corte {corte_turno.lower()} · USO INSTITUCIONAL",
    "",
]

for pag in re.findall(r'<section class="page">(.*?)</section>', s, re.S):
    out += [SEP, ""]
    # Cada bloque se guarda con su posición en la página y se emite en ORDEN DE
    # DOCUMENTO: extraer por tipo (todos los títulos, luego los recuadros, luego
    # las fichas…) dejaba cada subtítulo lejos de su contenido (deuda de 135).
    bloques = []

    def pon(pos, lineas):
        bloques.append((pos, len(bloques), lineas))

    # Portada: radar, mapa y semáforo.
    if 'id="argos-radar"' in pag:
        m = re.search(r'id="argos-radar-stats">((?:<div>.*?</div>)+)</div>', pag, re.S)
        ls = ["[ RADAR CENTRAL — EN VIVO ]", ""]
        for d in re.findall(r"<div>(.*?)</div>", m.group(1), re.S):
            ls.append("  · " + limpia(d, False))
        mc = re.search(r'<div class="map-caption">(.*?)</div>', pag, re.S)
        ls += ["", "[ MAPA NACIONAL — FOCOS DEL CORTE — GIS POR ENTIDAD ]", "", limpia(mc.group(1)), ""]
        pon(m.start(), ls)
        sem = list(re.finditer(r'<div class="sem-item .*?</div>\s*</div>', pag, re.S))
        if sem:
            ls = ["## SEMÁFORO ARGOS", ""]
            for it in sem:
                it = it.group(0)
                lbl = limpia(re.search(r'class="lbl">(.*?)</span>', it, re.S).group(1))
                val = limpia(re.search(r'class="val">(.*?)</div>', it, re.S).group(1))
                ls += [f"  · {lbl} — {val}", ""]
            pon(max(sem[0].start(), m.start() + 1), ls)

    # Títulos de sección.
    for m in re.finditer(r'<div class="section-head"[^>]*>(?:<h2[^>]*>)?(.*?)(?:</h2>)?</div>', pag, re.S):
        t = limpia(m.group(1))
        if t and "SEMÁFORO ARGOS" not in t:
            pon(m.start(), [f"## {t}", ""])

    # Recuadros (portada, valoración, conclusiones).
    # La bandera es un <div>, no un <span>: el patrón anterior cortaba en su
    # cierre y el recuadro salía vacío (fallo de 126 y 127).
    for m in re.finditer(r'<div class="alerta contexto"[^>]*>\s*<div class="flag">(.*?)</div>\s*<p>(.*?)</p>', pag, re.S):
        pon(m.start(), ["── " + limpia(m.group(1)), ""] + plegar(limpia(m.group(2))) + [""])

    # Tarjetas de conteo.
    for m in re.finditer(r'<div class="tile[^"]*">(.*?)</div>\s*(?=<div class="tile|</div>)', pag, re.S):
        tile = m.group(1)
        lbl = re.search(r'class="lbl">(.*?)</span>', tile, re.S)
        num_ = re.search(r'class="num">(.*?)</span>', tile, re.S)
        sub = re.search(r'class="sub">(.*?)</span>', tile, re.S)
        if lbl and num_:
            linea = f"  · {limpia(lbl.group(1))}: {limpia(num_.group(1))}"
            if sub:
                linea += " — " + limpia(sub.group(1), False)
            pon(m.start(), [linea, ""])

    # Fichas (las -REC- llevan atributo style: el patrón lo admite).
    for m in re.finditer(r'<div class="nota" id="([^"]+)"[^>]*>(.*?)(?=<div class="nota" id=|<div class="section-head"|<div class="alerta contexto"|<div class="table-wrap"|<footer|$)', pag, re.S):
        cuerpo = m.group(2)
        h3m = re.search(r"<h3>(.*?)</h3>", cuerpo, re.S)
        if not h3m:
            continue
        h3 = limpia(h3m.group(1), False)
        flag = re.search(r'class="risk-flag [^"]*">(.*?)</span>', cuerpo, re.S)
        ls = [f"### {h3}" + (f" [{limpia(flag.group(1))}]" if flag else ""), ""]
        for ap in re.findall(r'<div class="apartado"><span class="k">(.*?)</span>(.*?)</div>', cuerpo, re.S):
            ls += [f"── {limpia(ap[0])}", ""] + plegar(limpia(ap[1])) + [""]
        pon(m.start(), ls)

    # Tablas.
    for m in re.finditer(r'<div class="table-wrap"><table[^>]*>(.*?)</table></div>', pag, re.S):
        tab = m.group(1)
        ls = []
        ths = [limpia(c, False) for c in re.findall(r"<th\b[^>]*>(.*?)</th>", tab, re.S)]
        if ths:
            ls += ["  " + " | ".join(ths)]
        for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", tab.split("</thead>")[-1], re.S):
            tds = [limpia(c, False) for c in re.findall(r"<td\b[^>]*>(.*?)</td>", tr, re.S)]
            if tds:
                ls += ["  " + " | ".join(tds)]
        pon(m.start(), ls + [""])

    # Notas al pie de la página (muted-note fuera de tablas).
    for m in re.finditer(r'<p class="muted-note"[^>]*>(.*?)</p>', pag, re.S):
        txt = limpia(m.group(1))
        if txt:
            pon(m.start(), plegar(txt) + [""])

    for _, _, ls in sorted(bloques):
        out += ls

    out += [RAYA,
            f"  · Versión 3.0 · Fecha: {fecha} · Hora: {hora} (CDMX) · Corte: {corte_turno} · "
            f"ARGOS N.° {num} · USO INSTITUCIONAL",
            ""]

txt = "\n".join(out)
txt = re.sub(r"\n{3,}", "\n\n", txt)
open(dst, "w", encoding="utf-8").write(txt.rstrip() + "\n")
print(f"escrito {dst}: {len(txt)} bytes, {txt.count(chr(10))} líneas")
