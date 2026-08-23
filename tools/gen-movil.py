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
  /* Tablas anchas reflujadas a tarjetas (ARGOS 102): una tarjeta por fila, con el
     nombre de la columna delante del valor. Sustituye a la regla que las retiraba. */
  .tabla-tarjetas{margin:8px 0;}
  .fila-tarjeta{border:1px solid var(--border);border-radius:6px;background:var(--panel);
    padding:8px 10px;margin:6px 0;}
  .fila-tarjeta .campo{font-size:11.5px;line-height:1.5;padding:2px 0;
    border-bottom:1px dotted rgba(76,230,255,0.14);}
  .fila-tarjeta .campo:last-child{border-bottom:none;}
  .fila-tarjeta .campo .k{display:block;font-family:var(--mono);font-size:9px;
    letter-spacing:1px;color:var(--cyan);text-transform:uppercase;}
  .fila-total{border:1px solid var(--border);border-radius:6px;background:var(--panel-2);
    padding:8px 10px;margin:6px 0;font-size:11.5px;line-height:1.5;}
"""
if ".tabla-scroll" not in shell:
    shell = shell.replace("</style>", CSS_TABLA + "</style>", 1)

# Anclas realmente existentes en el escritorio: solo estas pueden enlazarse.
ANCLAS = frozenset(re.findall(r'<div class="nota" id="([^"]+)"', desk))

# ---------------------------------------------------------------- 3. secciones
paginas = re.findall(r'<section class="page">(.*?)</section>', desk, re.S)
if not paginas:
    sys.exit("El escritorio no tiene ninguna <section class=\"page\">.")


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


def _celdas_a_tarjeta(fila_html, cabeceras):
    """Convierte un <tr> del escritorio en una tarjeta apilada de la móvil."""
    celdas = re.findall(r"(<t[dh][^>]*>)(.*?)</t[dh]>", fila_html, re.S)
    if not celdas:
        return ""
    # Fila de totales o de nota: una sola celda con colspan. Se emite entera.
    if len(celdas) == 1:
        return f'<div class="fila-total">{celdas[0][1].strip()}</div>'
    # BUG DE ARGOS 104: esta función emparejaba celda i con cabecera i, ignorando
    # colspan. En la fila TOTAL de la pág. 5 —que abre con un td colspan=4 y cierra
    # con otro colspan=2— eso desplazaba TODAS las etiquetas y la móvil publicaba
    # "Cortas 172" y "Granadas 16" donde el escritorio decía 2 armas cortas y
    # 2 granadas. Cifras falsas, no un defecto de maquetación. Ahora se lleva la
    # cuenta real de columnas y las celdas que abarcan varias se emiten a lo ancho,
    # sin etiqueta, porque ninguna cabecera concreta las describe.
    partes = []
    col = 0
    for apertura, celda in celdas:
        m = re.search(r'colspan\s*=\s*["\']?(\d+)', apertura, re.I)
        span = int(m.group(1)) if m else 1
        valor = celda.strip()
        if not valor or valor in ("—", "&mdash;"):
            col += span
            continue          # columna vacía: no se inventa contenido ni se ocupa espacio
        if span > 1:
            partes.append(f'<div class="campo campo-ancho">{valor}</div>')
        else:
            etiqueta = cabeceras[col] if col < len(cabeceras) else f"col. {col + 1}"
            partes.append(f'<div class="campo"><span class="k">{etiqueta}</span>{valor}</div>')
        col += span
    return '<div class="fila-tarjeta">' + "".join(partes) + "</div>"


def tabla_a_ficha(p, con_tarjetas):
    """Reflúa las tablas del escritorio a la anchura de un teléfono, SIN perder contenido.

    Historia de esta función, porque explica su forma actual:

    - La primera versión retiraba TODAS las tablas de la sección. Con ellas se
      perdían los indicadores de cobertura que `CLAUDE.md` declara obligatorios.
    - ARGOS 101 la afinó para retirar solo las de más de cuatro columnas, y
      conservar las estrechas dentro de un contenedor desplazable.
    - El control `editor-duplicidad` de ARGOS 102 midió lo que esa regla costaba:
      la móvil reproducía **13 de los 27 ARG-ID** de la edición. Cinco tablas
      anchas se sustituían por una nota, y con ellas desaparecían del móvil ocho
      de las nueve recuperaciones, cinco de las once fes de erratas y las tres
      líneas del módulo de armamento. Un lector que solo tuviera la móvil no
      podía verificar la mitad de la edición.

    La regla actual no retira ninguna tabla. Las de hasta cuatro columnas se
    conservan íntegras en un contenedor desplazable; **las anchas se reflúan a
    tarjetas apiladas**, una por fila, con el nombre de cada columna delante de su
    valor. Se pierde la lectura comparativa entre filas —que en un teléfono no
    existía de todos modos— y no se pierde ni un dato.
    """
    def sustituir(m):
        bloque = m.group(0)
        cabeza = bloque.split("</thead>")[0] if "</thead>" in bloque else ""
        cabeceras = [re.sub(r"<[^>]+>", "", c).strip()
                     for c in re.findall(r"<th\b[^>]*>(.*?)</th>", cabeza, re.S)]
        ncols = len(cabeceras) if cabeceras else 99
        interior = bloque.split('<div class="table-wrap">')[-1].rsplit("</div>", 1)[0]
        if ncols <= 4:
            # Cabe en pantalla estrecha: se conserva, desplazable en su contenedor.
            return '<div class="tabla-scroll">' + interior + "</div>"
        cuerpo = bloque.split("</thead>")[-1] if "</thead>" in bloque else bloque
        filas = re.findall(r"<tr\b[^>]*>(.*?)</tr>", cuerpo, re.S)
        tarjetas = "".join(_celdas_a_tarjeta(f, cabeceras) for f in filas)
        if not tarjetas:
            return '<div class="tabla-scroll">' + interior + "</div>"
        return ('<div class="tabla-tarjetas"><p class="muted-note">'
                f"<b>Tabla ejecutiva de {ncols} columnas</b>, reflujada a tarjetas para esta "
                "versión. <b>No se omitió ningún dato</b>; la tabla en su forma original está en "
                f"<code>reports/argos-{FECHA}.html</code>.</p>" + tarjetas + "</div>")

    p = re.sub(r'<div class="table-wrap">.*?</table>\s*</div>', sustituir, p, flags=re.S)

    # Red de seguridad: una tabla escrita sin el envoltorio `table-wrap` no la
    # detectaba la regla de arriba y llegaba entera a la móvil, desbordando el
    # ancho de la página entera (fallo real de ARGOS 100, pág. 2). El envoltorio
    # es una convención del escritorio y es fácil olvidarlo al redactar, así que
    # aquí se atrapa: lo que sobreviva se hace desplazable dentro de su propio
    # contenedor, nunca a costa del cuerpo del documento.
    p = re.sub(r"<table\b.*?</table>",
               lambda m: '<div class="tabla-scroll">' + m.group(0) + "</div>",
               p, flags=re.S)
    return p


SEM = f'''<div class="semaforo">
    <div class="sem alto"><span class="dot"></span><span class="lbl">🔴 ROJO<br>ALTO IMPACTO</span><span class="val">{n_rojo}</span></div>
    <div class="sem medio"><span class="dot"></span><span class="lbl">🟡 AMARILLO<br>VIOL. OPERATIVA</span><span class="val">{n_ama}</span></div>
    <div class="sem bajo"><span class="dot"></span><span class="lbl">🟢 VERDE<br>ACC. INSTITUC.</span><span class="val">{n_verde}</span></div>
  </div>'''

# Los títulos y el número de páginas se DERIVAN del escritorio, no se fijan aquí.
# Fijarlos rompía el generador cada vez que una edición cambiaba de estructura: pasó de
# 7 a 6 páginas en ARGOS 98 y de 6 a 8 en ARGOS 102, y en ambos casos hubo que tocar el
# script. Lo estable no es el número de páginas, es que cada una lleva su título en el
# masthead y que la portada es la primera.
TITULOS_CORTOS = {
    "CRIMEN ORGANIZADO": "CRIMEN ORGANIZADO",
    "CONTEO NACIONAL DE ARMAMENTO": "ARMAMENTO Y EXPLOSIVOS",
    "RASTREO NACIONAL DE SENTENCIAS": "RASTREO DE SENTENCIAS",
    "AUDITORÍA RETROACTIVA": "AUDITORÍA RETROACTIVA",
    "VALORACIÓN": "VALORACIÓN",
    "TABLERO EJECUTIVO": "TABLERO EJECUTIVO",
}


def titulo_de(pagina, indice):
    """Extrae el título de una página del masthead del escritorio y lo abrevia."""
    if indice == 0:
        return "PORTADA"
    m = re.search(r'<h2 style="font-size:14px;">(.*?)</h2>', pagina, re.S)
    if not m:
        return f"SECCIÓN {indice + 1}"
    crudo = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    # El masthead usa "TÍTULO — subtítulo descriptivo"; para la navegación móvil
    # basta la parte anterior al guion largo.
    corto = crudo.split("—")[0].strip()
    for clave, abrev in TITULOS_CORTOS.items():
        if corto.startswith(clave):
            # Del resto del título solo se conserva el numeral romano de
            # "CRIMEN ORGANIZADO (I)" / "(II)". Cualquier otra cola es la
            # enumeración descriptiva del masthead, que no cabe en la barra
            # de navegación de un teléfono y se descarta.
            sufijo = corto[len(clave):].strip()
            if re.fullmatch(r"\(I+\)", sufijo):
                return f"{abrev} {sufijo}"
            return abrev
    return corto


TITULOS = [(titulo_de(pg, i), i + 1) for i, pg in enumerate(paginas)]
TOTAL = len(TITULOS)

# La barra de navegación se hereda del shell de la edición anterior y llevaba tantos
# enlaces como secciones tuviera aquella. Se reconstruye a partir de TITULOS para que
# no queden anclas muertas ni falten secciones cuando la estructura cambie.
NAV_ABREV = {
    "CRIMEN ORGANIZADO (I)": "C. ORGANIZADO I",
    "CRIMEN ORGANIZADO (II)": "C. ORGANIZADO II",
    "ARMAMENTO Y EXPLOSIVOS": "ARMAMENTO",
    "RASTREO DE SENTENCIAS": "SENTENCIAS",
    "AUDITORÍA RETROACTIVA": "AUDITORÍA",
    "TABLERO EJECUTIVO": "TABLERO",
}
nav_links = "\n".join(
    f'    <a href="#s{n}">{NAV_ABREV.get(t, t)}</a>' for t, n in TITULOS)
m_nav = re.search(r'( *<a href="#s\d+">.*?</a>\n?)+', shell, re.S)
if not m_nav:
    sys.exit("No se localizó la barra de navegación en el shell de la móvil anterior.")
shell = shell[: m_nav.start()] + nav_links + "\n" + shell[m_nav.end():]

partes = []
for i, (titulo, n) in enumerate(TITULOS):
    es_sentencias = "RASTREO NACIONAL DE SENTENCIAS" in paginas[i]
    tiene_mapa_arm = 'id="argos-map-arm"' in paginas[i]
    cuerpo = tabla_a_ficha(lista_a_reg(limpia(paginas[i]), ANCLAS), con_tarjetas=es_sentencias)

    if n == 1:
        # Consumir TODO el bloque de visuales hasta el semáforo: un .*? no
        # codicioso deja huérfano el panel del mapa.
        cuerpo = re.sub(
            r'<div class="cover-visuals">.*?(?=<div class="block-head">SEMÁFORO ARGOS[^<]*</div>)',
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
        cuerpo = re.sub(r'<div class="semaforo">.*?(?=<div class="block-head">EJES DEL DÍA[^<]*</div>)',
                        SEM + "\n\n  ", cuerpo, flags=re.S)
    if tiene_mapa_arm:
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
    <span class="pg">PÁG. {n} / {TOTAL}</span>
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
if salida.count('<section class="seccion"') != TOTAL:
    errores.append(f"no hay {TOTAL} secciones")
if "sem-item" in salida or "stat-tile" in salida or "cover-visuals" in salida:
    errores.append("quedaron restos de clases de escritorio")
svg_esperados = 3 if 'id="argos-map-arm"' in desk else 2
if salida.count("<svg") != svg_esperados:
    errores.append(f"se esperaban {svg_esperados} SVG, hay {salida.count('<svg')}")

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
