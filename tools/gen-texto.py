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
vent = limpia(re.search(r"Ventana <b>(.*?)</b> \(<b>(.*?)</b>\)", s).group(0), False)
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

    # Portada: radar, mapa y semáforo.
    if 'id="argos-radar"' in pag:
        st = re.search(r'id="argos-radar-stats">((?:<div>.*?</div>)+)</div>', pag, re.S).group(1)
        out += ["[ RADAR CENTRAL — EN VIVO ]", ""]
        for d in re.findall(r"<div>(.*?)</div>", st, re.S):
            out.append("  · " + limpia(d, False))
        out += ["", "[ MAPA NACIONAL — FOCOS DEL CORTE — GIS POR ENTIDAD ]", ""]
        out += [limpia(re.search(r'<div class="map-caption">(.*?)</div>', pag, re.S).group(1)), ""]
        out += ["## SEMÁFORO ARGOS", ""]
        for it in re.findall(r'<div class="sem-item .*?</div>\s*</div>', pag, re.S):
            lbl = limpia(re.search(r'class="lbl">(.*?)</span>', it, re.S).group(1))
            val = limpia(re.search(r'class="val">(.*?)</div>', it, re.S).group(1))
            out += [f"  · {lbl} — {val}", ""]

    # Títulos de sección.
    for t in re.findall(r'<div class="section-head">(?:<h2[^>]*>)?(.*?)(?:</h2>)?</div>', pag, re.S):
        t = limpia(t)
        if t and "SEMÁFORO ARGOS" not in t:
            out += [f"## {t}", ""]

    # Recuadros (portada, valoración, conclusiones).
    for al in re.findall(r'<div class="alerta contexto"[^>]*>(.*?)</div>', pag, re.S):
        flag = re.search(r'class="flag">(.*?)</span>', al, re.S)
        if flag:
            out += ["── " + limpia(flag.group(1)), ""]
        cuerpo = re.search(r"<p>(.*?)</p>", al, re.S)
        if cuerpo:
            for ln in plegar(limpia(cuerpo.group(1))):
                out.append(ln)
            out.append("")

    # Tarjetas de conteo.
    for tile in re.findall(r'<div class="tile[^"]*">(.*?)</div>\s*(?=<div class="tile|</div>)', pag, re.S):
        lbl = re.search(r'class="lbl">(.*?)</span>', tile, re.S)
        num_ = re.search(r'class="num">(.*?)</span>', tile, re.S)
        sub = re.search(r'class="sub">(.*?)</span>', tile, re.S)
        if lbl and num_:
            linea = f"  · {limpia(lbl.group(1))}: {limpia(num_.group(1))}"
            if sub:
                linea += " — " + limpia(sub.group(1), False)
            out += [linea, ""]

    # Fichas.
    for nota in re.findall(r'<div class="nota" id="([^"]+)">(.*?)(?=<div class="nota" id=|<footer)', pag, re.S):
        _, cuerpo = nota
        h3 = limpia(re.search(r"<h3>(.*?)</h3>", cuerpo, re.S).group(1), False)
        flag = re.search(r'class="risk-flag [^"]*">(.*?)</span>', cuerpo, re.S)
        out += [f"### {h3}" + (f" [{limpia(flag.group(1))}]" if flag else ""), ""]
        for ap in re.findall(r'<div class="apartado"><span class="k">(.*?)</span>(.*?)</div>', cuerpo, re.S):
            out += [f"── {limpia(ap[0])}", ""]
            for ln in plegar(limpia(ap[1])):
                out.append(ln)
            out.append("")

    # Tablas.
    for tab in re.findall(r'<div class="table-wrap"><table[^>]*>(.*?)</table></div>', pag, re.S):
        ths = [limpia(c, False) for c in re.findall(r"<th\b[^>]*>(.*?)</th>", tab, re.S)]
        if ths:
            out += ["  " + " | ".join(ths)]
        cuerpo = tab.split("</thead>")[-1]
        for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>", cuerpo, re.S):
            tds = [limpia(c, False) for c in re.findall(r"<td\b[^>]*>(.*?)</td>", tr, re.S)]
            if tds:
                out += ["  " + " | ".join(tds)]
        out += [""]

    # Notas al pie de la página (muted-note fuera de tablas).
    for nt in re.findall(r'<p class="muted-note"[^>]*>(.*?)</p>', pag, re.S):
        txt = limpia(nt)
        if txt:
            out += plegar(txt) + [""]

    out += [RAYA,
            f"  · Versión 3.0 · Fecha: {fecha} · Hora: {hora} (CDMX) · Corte: {corte_turno} · "
            f"ARGOS N.° {num} · USO INSTITUCIONAL",
            ""]

txt = "\n".join(out)
txt = re.sub(r"\n{3,}", "\n\n", txt)
open(dst, "w", encoding="utf-8").write(txt.rstrip() + "\n")
print(f"escrito {dst}: {len(txt)} bytes, {txt.count(chr(10))} líneas")
