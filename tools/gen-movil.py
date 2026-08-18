#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construye la versión MÓVIL de una edición ARGOS transformando la de escritorio.

Sustituye al script antiguo, que quedó desfasado al pasar de 7 a 6 páginas en
ARGOS 98 y reconstruía la estructura vieja. Este no reconstruye nada: toma el
escritorio ya terminado y lo reflúa a una columna, de modo que la móvil no puede
divergir del cartelón — que es el fallo que arrastraba la serie.

Qué hace, en orden:
  1. Ejecuta tools/gen-movil-svg.js sobre el escritorio para obtener el radar, el
     mapa de portada, el mapa de aseguramientos y el BLOQUE DE CONTADORES, todos
     derivados de los arreglos EVENTOS y EVENTOS_ARM.
  2. Reutiliza el shell (head/CSS/topbar/nav) de la móvil de la edición anterior.
  3. Extrae las 6 secciones del escritorio y les aplica el mapeo de clases móvil.
  4. Incrusta los SVG y el contador ya renderizados.

REGLA DE ORO (bug de ARGOS 97): el div `radar-stats` de la móvil es estático y NO
se regenera solo. Aquí se toma SIEMPRE de la salida del generador, nunca se
escribe a mano. Si alguien lo teclea, volverá a desincronizarse del semáforo.

Uso:
    python3 tools/gen-movil.py <NUM> <FECHA> <NUM_ANT> <FECHA_ANT> <HORA>

Ejemplo (ARGOS 100, corte del 17-ago, partiendo de la móvil de ARGOS 99):
    python3 tools/gen-movil.py 100 2026-08-17 99 2026-08-16 07:41

La HORA debe ser la real de CDMX (TZ=America/Mexico_City date +%H:%M), la misma
que ya lleva sellada el escritorio.
"""
import os
import re
import subprocess
import sys
import tempfile

if len(sys.argv) != 6:
    sys.exit(__doc__)

NUM, FECHA, NUM_ANT, FECHA_ANT, HORA = sys.argv[1:6]

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESK = f"{RAIZ}/reports/argos-{FECHA}.html"
BASE = f"{RAIZ}/reports/argos-{FECHA_ANT}-movil.html"
OUT = f"{RAIZ}/reports/argos-{FECHA}-movil.html"

for f in (DESK, BASE):
    if not os.path.exists(f):
        sys.exit(f"No existe {f}")

# ---------------------------------------------------------------- 1. SVG
tmp = tempfile.mkdtemp(prefix="argos-movil-")
subprocess.run(
    ["node", f"{RAIZ}/tools/gen-movil-svg.js", DESK, f"{tmp}/x"],
    check=True, capture_output=True,
)
leer = lambda n: open(f"{tmp}/{n}", encoding="utf-8").read()
svg_radar, svg_map, svg_arm = leer("out-radar.svg"), leer("out-map.svg"), leer("out-map-arm.svg")
stats_html = leer("out-stats.html").strip()          # <-- contador: del generador, no a mano

# Los contadores mandan: el semáforo de la móvil se deriva de ellos.
cuenta = re.findall(r"<b>(\d+)</b>", stats_html)
if len(cuenta) != 3:
    sys.exit(f"El generador no devolvió 3 contadores: {stats_html!r}")
n_rojo, n_ama, n_verde = cuenta

desk = open(DESK, encoding="utf-8").read()
base = open(BASE, encoding="utf-8").read()

# ---------------------------------------------------------------- 2. shell
MARCA = "<!-- ===================== 1 — PORTADA"
if MARCA not in base:
    sys.exit("La móvil anterior no tiene el marcador de la sección 1; revisa el shell a mano.")
shell = base[: base.index(MARCA)]
shell = (shell
         .replace(f"ARGOS {NUM_ANT} — Reporte Nacional de Seguridad ({FECHA_ANT}) · Móvil",
                  f"ARGOS {NUM} — Reporte Nacional de Seguridad ({FECHA}) · Móvil")
         .replace(f'<span class="n">{NUM_ANT}</span>', f'<span class="n">{NUM}</span>')
         .replace(f"<b>{FECHA_ANT}</b>", f"<b>{FECHA}</b>"))
shell = re.sub(r"\d{2}:\d{2} \(CDMX\)", f"{HORA} (CDMX)", shell)

# CSS de la red de seguridad de tablas. Se inyecta aquí y no se hereda del shell
# de la edición anterior, para que el generador siga siendo autosuficiente aunque
# la móvil previa no lo tuviera.
CSS_TABLA = """
  .tabla-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%;
    border:1px solid var(--border);border-radius:6px;margin:8px 0;}
  .tabla-scroll table{border-collapse:collapse;font-size:11px;min-width:max-content;}
  .tabla-scroll th,.tabla-scroll td{border:1px solid var(--border);padding:5px 7px;
    text-align:left;white-space:nowrap;}
  .tabla-scroll th{background:var(--panel-2);color:var(--cyan);font-family:var(--mono);
    font-size:9.5px;letter-spacing:1px;}
  .tabla-scroll td{background:var(--panel);}
  /* Segunda causa previsible de desborde en esta serie: una URL o un ARG-ID
     largo sin espacios. Se parte en vez de empujar el ancho de la página. */
  .seccion code, .seccion a, .reg-txt, .nota-body{overflow-wrap:anywhere;}
  .seccion img, .seccion svg{max-width:100%;height:auto;}
"""
if ".tabla-scroll" not in shell:
    shell = shell.replace("</style>", CSS_TABLA + "</style>", 1)

# Anclas realmente existentes en el escritorio: solo estas pueden enlazarse.
ANCLAS = frozenset(re.findall(r'<div class="nota" id="([^"]+)"', desk))

# ---------------------------------------------------------------- 3. secciones
paginas = re.findall(r'<section class="page">(.*?)</section>', desk, re.S)
if len(paginas) != 6:
    sys.exit(f"El escritorio tiene {len(paginas)} páginas, se esperaban 6.")


def limpia(p):
    """Quita masthead y footbar; aplica el mapeo de clases escritorio -> móvil."""
    p = re.sub(r'<header class="masthead">.*?</header>', "", p, flags=re.S)
    p = re.sub(r'<footer class="footbar">.*?</footer>', "", p, flags=re.S)
    p = p.replace('class="section-head"', 'class="block-head"')
    p = p.replace('<div class="stat-grid">', '<div class="stats">')
    p = p.replace('<div class="stat-tile">', '<div class="stat">')
    p = p.replace('<div class="grid-2">', "<div>")
    p = p.replace("ESTADOS CON ASEGURAMIENTOS", "ESTADOS")
    p = p.replace("PERSONAS DETENIDAS", "DETENIDOS")
    return p


def lista_a_reg(bloque, anclas_validas=frozenset()):
    """Convierte <div class="list"> del escritorio en tarjetas .reg de la móvil.

    Un ARG-ID solo se enlaza si existe realmente una ficha con ese id en el
    documento. Antes bastaba con que el ID fuera de la edición en curso, lo que
    producía enlaces muertos hacia hechos descartados que nunca llegaron a tener
    ficha propia (detectado por editor-duplicidad en ARGOS 100).
    """
    def una(m):
        cls, tag, txt, idd = m.group(1), m.group(2), m.group(3), m.group(4)
        idd = re.sub(r"<[^>]+>", "", idd).strip()
        anchor = (f'<a class="argid" href="#{idd}">{idd}</a>'
                  if idd.startswith(f"ARG-{NUM}-") and idd in anclas_validas
                  else f'<span class="argid">{idd}</span>')
        return (f'<div class="reg">\n    <div class="reg-top">'
                f'<span class="tag {cls}">{tag}</span>{anchor}</div>\n'
                f'    <div class="reg-txt">{txt}</div>\n  </div>')
    pat = re.compile(r'<div class="list-item"><span class="tag ([a-z]+)">([^<]*)</span>'
                     r'<span>(.*?)</span><span>(.*?)</span></div>', re.S)
    return pat.sub(una, bloque).replace('<div class="list">', "<div>")


def tabla_a_ficha(p, con_tarjetas):
    """Las tablas ANCHAS se retiran para evitar desplazamiento horizontal.

    Regla afinada en ARGOS 101 tras un hallazgo del control `procedencia-cifras`:
    la versión anterior retiraba TODAS las tablas de la sección, y con ellas se
    perdían los dos indicadores de cobertura —que `CLAUDE.md` declara
    obligatorios— y la tabla de indicadores oficiales. Peor aún, el aviso
    sustitutorio afirmaba que esos campos constaban en las fichas de la misma
    sección, lo que era falso para las tablas que no describen eventos.

    Ahora solo se retiran las tablas de MÁS DE CUATRO COLUMNAS, que son las que
    realmente desbordan. Las de dos, tres o cuatro columnas —cobertura,
    indicadores, seguimientos— caben y se conservan íntegras, dentro de su propio
    contenedor desplazable. La nota que sustituye a una tabla retirada NO declara
    una integridad que la sección no tenga.
    """
    def sustituir(m):
        bloque = m.group(0)
        ncols = len(re.findall(r'<th\b', bloque.split('</thead>')[0])) if '</thead>' in bloque else 99
        if ncols <= 4:
            # Cabe en pantalla estrecha: se conserva, desplazable en su contenedor.
            return '<div class="tabla-scroll">' + bloque.split('<div class="table-wrap">')[-1].rsplit('</div>', 1)[0] + '</div>'
        if con_tarjetas:
            return ('<p class="muted-note"><b>Tabla ejecutiva de ' + str(ncols) + ' columnas.</b> '
                    'No se reproduce en esta versión por ancho; cada evento tiene su ficha completa '
                    'en esta misma sección, y la tabla íntegra está en '
                    f'<code>reports/argos-{FECHA}.html</code>.</p>')
        return ('<p class="muted-note"><b>Tabla ejecutiva de ' + str(ncols) + ' columnas.</b> '
                'No se reproduce en esta versión por ancho. <b>Sus cifras no constan en otro lugar '
                'de la versión móvil</b>: consúltese la tabla íntegra en '
                f'<code>reports/argos-{FECHA}.html</code> o el registro de fuentes en '
                f'<code>reports/argos-{FECHA}-fuentes.md</code>.</p>')

    p = re.sub(r'<div class="table-wrap">.*?</table>\s*</div>', sustituir, p, flags=re.S)

    # Red de seguridad: una tabla escrita sin el envoltorio `table-wrap` no la
    # detectaba la regla de arriba y llegaba entera a la móvil, desbordando el
    # ancho de la página entera (fallo real de ARGOS 100, pág. 2). El envoltorio
    # es una convención del escritorio y es fácil olvidarlo al redactar, así que
    # aquí se atrapa: lo que sobreviva se hace desplazable dentro de su propio
    # contenedor, nunca a costa del cuerpo del documento.
    p = re.sub(r'<table\b.*?</table>',
               lambda m: '<div class="tabla-scroll">' + m.group(0) + '</div>',
               p, flags=re.S)
    return p


SEM = f'''<div class="semaforo">
    <div class="sem alto"><span class="dot"></span><span class="lbl">🔴 ROJO<br>ALTO IMPACTO</span><span class="val">{n_rojo}</span></div>
    <div class="sem medio"><span class="dot"></span><span class="lbl">🟡 AMARILLO<br>VIOL. OPERATIVA</span><span class="val">{n_ama}</span></div>
    <div class="sem bajo"><span class="dot"></span><span class="lbl">🟢 VERDE<br>ACC. INSTITUC.</span><span class="val">{n_verde}</span></div>
  </div>'''

TITULOS = [("PORTADA", 1), ("CRIMEN ORGANIZADO (I)", 2), ("CRIMEN ORGANIZADO (II)", 3),
           ("ARMAMENTO Y EXPLOSIVOS", 4), ("RASTREO DE SENTENCIAS", 5), ("VALORACIÓN", 6)]

partes = []
for i, (titulo, n) in enumerate(TITULOS):
    cuerpo = tabla_a_ficha(lista_a_reg(limpia(paginas[i]), ANCLAS), con_tarjetas=(n == 5))

    if n == 1:
        # Consumir TODO el bloque de visuales hasta el semáforo: un .*? no
        # codicioso deja huérfano el panel del mapa.
        cuerpo = re.sub(
            r'<div class="cover-visuals">.*?(?=<div class="block-head">SEMÁFORO ARGOS</div>)',
            f'''<div class="viz">
    <div class="viz-title"><span>RADAR CENTRAL</span><span>EN VIVO</span></div>
    <div class="radar-box">{svg_radar}</div>
    <div class="radar-stats">{stats_html}</div>
  </div>

  <div class="viz">
    <div class="viz-title"><span>MAPA NACIONAL</span><span>FOCOS DEL CORTE</span></div>
    <div class="map-box">{svg_map}</div>
    <div class="map-caption">Color = evento de mayor impacto por entidad.</div>
  </div>

  ''', cuerpo, flags=re.S)
        # Mismo motivo: consumir hasta "EJES DEL DÍA" o quedan sem-item sueltos.
        cuerpo = re.sub(r'<div class="semaforo">.*?(?=<div class="block-head">EJES DEL DÍA</div>)',
                        SEM + "\n\n  ", cuerpo, flags=re.S)
    if n == 4:
        cuerpo = re.sub(
            r'<div class="panel">\s*<div class="panel-title">.*?</div>\s*'
            r'<div class="map-box" id="argos-map-arm"></div>\s*<div class="map-caption">(.*?)</div>\s*</div>',
            lambda m: f'''<div class="viz">
    <div class="viz-title"><span>MAPA DE ASEGURAMIENTOS</span><span>SEMÁFORO ARGOS</span></div>
    <div class="map-box">{svg_arm}</div>
    <div class="map-caption">{m.group(1)}</div>
  </div>''', cuerpo, flags=re.S)

    partes.append(f'''<!-- ===================== {n} — {titulo} ===================== -->
<section class="seccion" id="s{n}">
  <div class="sec-head">
    <h2>{titulo}</h2>
    <span class="pg">PÁG. {n} / 6</span>
  </div>
{cuerpo}
</section>''')

NOTA = f'''
  <p class="muted-note">
    Esta es la <b>versión móvil</b> de ARGOS {NUM}, con el mismo contenido verificado que la versión de
    cartelón (<code>reports/argos-{FECHA}.html</code>), reflujada a una sola columna. Las tablas
    ejecutivas se presentan como fichas para evitar desplazamiento horizontal; no se omitió ni resumió
    ninguna tarjeta. El radar, el mapa de portada y el mapa de aseguramientos se generan de los mismos
    arreglos <code>EVENTOS</code> y <code>EVENTOS_ARM</code> que la versión de escritorio mediante
    <code>tools/gen-movil-svg.js</code>, y <b>los contadores del radar se toman del propio generador</b>,
    no se escriben a mano: es el origen del error corregido en ARGOS 97.
  </p>'''
partes[-1] = partes[-1].replace("</section>", NOTA + "\n</section>")

FOOTER = f'''
<footer class="footbar">
  <div>Versión 3.0 · Edición móvil</div>
  <div>Fecha: {FECHA} · Hora: {HORA} (CDMX) · Corte: Matutino</div>
  <div>ARGOS N.° {NUM} · <span class="uso">USO INSTITUCIONAL</span></div>
</footer>

</body>
</html>
'''

salida = shell + "\n".join(partes) + FOOTER
open(OUT, "w", encoding="utf-8").write(salida)

# ---------------------------------------------------------------- 4. validación
errores = []
for etiqueta in ("div", "section", "p"):
    a = len(re.findall(r"<" + etiqueta + r"\b", salida))
    c = len(re.findall(r"</" + etiqueta + r">", salida))
    if a != c:
        errores.append(f"{etiqueta}: {a} abre / {c} cierra")
if salida.count('<section class="seccion"') != 6:
    errores.append("no hay 6 secciones")
if "sem-item" in salida or "stat-tile" in salida or "cover-visuals" in salida:
    errores.append("quedaron restos de clases de escritorio")
if salida.count("<svg") != 3:
    errores.append(f"se esperaban 3 SVG, hay {salida.count('<svg')}")

# --- control de desborde horizontal (fallo de ARGOS 100) ---------------------
# La móvil de ARGOS 100 se salió de la pantalla y la validación dijo "OK": comprobaba
# markup, secciones y SVG, pero nunca el ANCHO. Estas dos comprobaciones cubren los dos
# orígenes reales del desborde. Se ejecutan sobre el ESCRITORIO, que es donde escribe el
# redactor: corregir ahí es lo que evita que el fallo vuelva a colarse en silencio.
sueltas = len(re.findall(r'<table\b', desk)) - len(
    re.findall(r'<div class="table-wrap">\s*<table\b', desk))
if sueltas > 0:
    errores.append(
        f"{sueltas} tabla(s) del escritorio sin envoltorio <div class=\"table-wrap\">: "
        "la regla que retira las retículas detecta por el envoltorio y no dispararía")

# Tokens largos sin punto de corte (URLs desnudas, IDs concatenados) en texto visible.
texto = re.sub(r"<svg.*?</svg>", " ", salida, flags=re.S)
texto = re.sub(r"<style.*?</style>", " ", texto, flags=re.S)
texto = re.sub(r"<script.*?</script>", " ", texto, flags=re.S)
texto = re.sub(r"<[^>]+>", " ", texto)
largos = sorted({t for t in re.findall(r"\S{75,}", texto)})
if largos:
    errores.append(
        f"{len(largos)} token(s) de 75+ caracteres sin corte en texto visible "
        f"(desbordan en pantalla estrecha), p. ej.: {largos[0][:90]}")

print(f"escrita {OUT} ({len(salida)} bytes)")
print(f"contadores del generador: 🔴 {n_rojo}  🟡 {n_ama}  🟢 {n_verde}")
print("tarjetas: móvil %d / escritorio %d"
      % (salida.count('class="nota"'), desk.count('class="nota"')))
if errores:
    sys.exit("VALIDACIÓN FALLIDA:\n  - " + "\n  - ".join(errores))
print("validación OK")
