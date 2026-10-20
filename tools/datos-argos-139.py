# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 139: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-139.py <plantilla ARGOS 138> <salida>
ARGOS 139 comparte fecha de corte con ARGOS 138 (2026-10-20): sus archivos llevan el sufijo «b» (argos-2026-10-20b.*)."""
import sys, re, json, html as H

NUM, FECHA, HORA = "139", "2026-10-20", "07:49"
CONSULTA = "2026-10-20 07:58-08:40"
DUR = "43 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos (cálculo propio derivado del arreglo, nunca escrito a mano)
E = []

# ---------------------------------------------------------------- RECUPERACIONES (ventanas anteriores)
R = [
 dict(id="ARG-139-REC-001", estado="MX-TAM", region="Noreste", fecha="2026-10-10", hora="noche (solo por resumen)", orig="ARGOS 129 — DÍA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=1,
  ent="Tamaulipas", mun="Río Bravo (colonia irregular, solo por resumen)", dia="10-OCT, NOCHE",
  title="TAMAULIPAS · RÍO BRAVO — AGREDEN CON ARMA BLANCA A UNA DIPUTADA FEDERAL; QUEDA HERIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 129 — DÍA SOLO POR RESUMEN</code> · Río Bravo · <code>COLONIA IRREGULAR, AL SALIR DEL DOMICILIO DE UNA COLABORADORA, SOLO POR RESUMEN</code> · noche del SÁBADO 10-OCT, por dos resúmenes coincidentes; <code>NINGÚN FRAGMENTO LITERAL CON EL DÍA</code> · denuncia pública desde el 17-OCT, por ruta · <b>diputada federal del PVEM</b>, por titular; distrito 3, " + RES + " · <b>herida con arma blanca</b>, por titulares (🔴 en su ventana) · herida de <b>15 cm</b> en el costado, por titular (El Universal); en el abdomen, " + RES + "; lado derecho o izquierdo: <code>CONTRADICHO</code> · agresor encapuchado salido de un terreno baldío, " + RES + " · hospitalizada, " + RES + " · «FGR investiga», por titulares (Elefante Blanco 2026/10/19, La Verdad); fiscalía local, " + RES + ": <code>CONTRADICHO</code> · la Fiscalía de Tamaulipas «desconoce detalles» de la agresión, por titular (CN Tamaulipas 2026/10/19) · pide protección federal; solicitó apoyo de la Guardia Nacional desde marzo, " + RES + " · <b>ningún detenido publicado</b> · <code>CIRCUNSTANCIAS SOLO POR RELATO DE LA VÍCTIMA; NINGUNA AUTORIDAD LAS CONFIRMA</code> · identidad pública por su cargo; nombre no reproducido",
  panel="<b>Diputada federal herida</b> con arma blanca", inst=SB, nac="Infobae · El Universal",
  conf="★★★☆☆", campo="día del hecho solo por resumen; circunstancias solo por relato de la víctima; sin fuente institucional", I=0, N=2, R=11, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/17)", "Infobae (2026/10/18)", "Expreso (2026/10/18)", "ABC Noticias (2026/10/19)", "En Línea Directa (2026/10/19)", "CN Tamaulipas (2026/10/19)", "Elefante Blanco (2026/10/19)"],
  desl="La diputada no figura en ninguna edición previa ni en el índice. Visto sin ficha en ARGOS 138 con el sábado 17 —día de la denuncia pública— como día del hecho: corregido al 10-oct, ventana de ARGOS 129 (10-oct 09:08 → 11-oct 08:58). Río Bravo en el boletín federal del 8-oct (ARGOS 128-129, ponchallantas): otro hecho."),
]

for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = []
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
assert TOT == [0] * 10, TOT
assert cnt == {"rojo": 0, "amarillo": 0, "verde": 0}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, MU_REC, HE_REC) == (0, 0, 0, 1)
assert len(set(r["id"] for r in R)) == len(R) and all(r["id"] == f"ARG-139-REC-{i+1:03d}" for i, r in enumerate(R))

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (e["armtxt"] if e.get("armtxt") else f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else ("sin fila — evento cualitativo, cantidad no determinada" if e.get("cual") else "sin fila — armamento asegurado: no publicado"))
    return f'''  <div class="nota" id="{e["id"]}"{op}>
    <div class="nota-header"><h3>{e["title"]}</h3><span class="risk-flag {cls}">{lab}</span></div>
    <div class="nota-body">
      <div class="apartado"><span class="k">HECHO</span>
        {e["hecho"]}
      </div>
      <div class="apartado"><span class="k">TRAZABILIDAD</span>
        <code>{e["id"]}</code> · <b>Confianza</b>: {nivel} ({e["conf"]}), <b>la fija el campo peor sostenido</b>: {e["campo"]} ·
        <b>Fuentes</b>: <b>Institucional {e["I"]}</b> · <b>Nacional {e["N"]}</b> · <b>Regional {e["R"]}</b> · <b>Abierta {e["A"]}</b> ·
        con fecha en la ruta: {fech}
        · <b>Hecho</b>: {e.get("fecha_txt", e["fecha"])} · <b>Hora</b>: {e["hora"]} · <b>Consulta</b>: {CONSULTA} ·
        <b>Estatus</b>: {e.get("estatus", "Parcialmente corroborado")} · {armtxt}<br><b>Deslindes y reservas</b>: {e["desl"]}
      </div>
    </div>
  </div>
'''

def footer():
    return f'''  <footer class="footbar">
    <span>Versión 3.0</span>
    <span>Fecha: {FECHA} · Hora: {HORA} (CDMX)</span>
    <span>Corte: Matutino</span>
    <span>ARGOS N.° {NUM}</span>
    <span class="uso">USO INSTITUCIONAL</span>
  </footer>
'''

def page(title, body):
    return f'<section class="page">\n  <div class="section-head"><h2 style="font-size:14px;">{title}</h2></div>\n\n{body}\n{footer()}</section>\n'

def prow(e, rec=False):
    mun = e["mun"]
    dia = e["dia"] if not rec else "VENTANA " + e["orig"]
    sem = SEM[e["color"]] if not rec else SEM[e["col_orig"]] + ' <span class="muted-note">(en su ventana)</span>'
    st = ' style="opacity:.72;"' if rec else ""
    return f'      <tr{st}><td><b>{e["ent"]}</b><br>{mun}<br><span class="muted-note">{dia}</span></td><td>{e["panel"]}</td><td>{sem}</td><td>{e["inst"]}</td><td>{e["nac"]}</td><td>{e["conf"]}</td><td><a href="#{e["id"]}"><code>{e["id"]}</code></a></td></tr>'

def strip(s): return H.unescape(re.sub(r"<[^>]+>", "", s))

def ev_json(e):
    return {"id": e["id"], "estado": e["estado"], "region": e["region"], "color": e["color"], "impacto": e["impacto"],
            "hecho": strip(e["hecho"]), "fuentes": e["fechadas"] or ["Fuentes regionales sin fecha en la ruta"],
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"] + (" · día solo por resumen" if "DÍA SOLO POR RESUMEN" in e.get("fecha_txt", "") else "")}

def arm_json(a):
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 138 — Reporte Nacional de Seguridad — 2026-10-20</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
assert f"<title>ARGOS {NUM}" in head
script = tpl[tpl.index("<script>"):tpl.index("</script>") + len("</script>")]
tail = tpl[tpl.index("</script>") + len("</script>"):]

port = f'''<section class="page">
  <header class="masthead">
    <div class="brand">
      <div class="argos-num"><span class="w">ARGOS</span><span class="n">{NUM}</span></div>
      <div class="sub">SISTEMA DE INTELIGENCIA CRIMINAL TRAZABLE</div>
    </div>
    <div class="titles">
      <h1>REPORTE NACIONAL DE SEGURIDAD</h1>
      <h2>REPORTE DIARIO DE INTELIGENCIA CRIMINAL</h2>
      <div class="motto">INVESTIGACIONES, BÚSQUEDA Y VERDAD</div>
    </div>
    <div class="corte">
      CORTE INFORMATIVO<br>
      <b>Fecha:</b> {FECHA}<br>
      <b>Hora:</b> {HORA} (CDMX)
    </div>
  </header>

  <div class="cover-visuals">
    <div class="panel">
      <div class="panel-title"><span>RADAR CENTRAL</span><span>EN VIVO</span></div>
      <div class="radar-box" id="argos-radar"></div>
      <div class="radar-stats" id="argos-radar-stats"><div>🔴 Alto impacto<br><b>{cnt["rojo"]}</b></div><div>🟡 Violencia operativa<br><b>{cnt["amarillo"]}</b></div><div>🟢 Acciones institucionales<br><b>{cnt["verde"]}</b></div></div>
    </div>
    <div class="panel">
      <div class="panel-title"><span>MAPA NACIONAL — FOCOS DEL CORTE</span><span>GIS POR ENTIDAD</span></div>
      <div class="map-box" id="argos-map"></div>
      <div class="map-caption">Pase el cursor sobre un estado.</div>
    </div>
  </div>

  <div class="section-head">SEMÁFORO ARGOS</div>
  <div class="semaforo">
    <div class="sem-item alto"><span class="dot"></span><span class="lbl">🔴 ROJO — ALTO IMPACTO</span><div class="val">{cnt["rojo"]} eventos</div></div>
    <div class="sem-item medio"><span class="dot"></span><span class="lbl">🟡 AMARILLO — VIOLENCIA OPERATIVA</span><div class="val">{cnt["amarillo"]} eventos</div></div>
    <div class="sem-item bajo"><span class="dot"></span><span class="lbl">🟢 VERDE — ACCIONES INSTITUCIONALES</span><div class="val">{cnt["verde"]} eventos</div></div>
  </div>

  <div class="alerta contexto">
    <div class="flag">LO QUE DEBE HACER EL MANDO</div>
    <p>
      <b>1. SOLICITE A LA FGR Y A LA FISCALÍA DE TAMAULIPAS LA CARPETA, EL DÍA DEL ATAQUE Y LAS MEDIDAS DE PROTECCIÓN</b> (ARG-139-REC-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE OAXACA EL DÍA DEL ATAQUE, LAS CIFRAS DE LESIONADOS Y LA EDAD DEL MENOR</b> (ARG-138-001).
      <br><b>3. SOLICITE A LA FISCALÍA DE TABASCO LA FECHA DEL HALLAZGO Y LA IDENTIFICACIÓN GENÉTICA DE LOS CUERPOS</b> (ARG-138-002).
      <br><b>4. SOLICITE A LA FISCALÍA DE CHIHUAHUA EL ESTADO DE SALUD DE LA VÍCTIMA Y LA SITUACIÓN JURÍDICA DE LOS TRES DETENIDOS</b> (ARG-138-009 y ARG-138-010).
      <br><b>5. SOLICITE A FUERZA CIVIL EL DESGLOSE DEL ARMAMENTO Y LA FECHA DE LOS OPERATIVOS DE CADEREYTA</b> (ARG-138-011).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: ORD[x["color"]])) or '      <tr><td colspan="7"><code>NINGÚN HECHO PROPIO CON RUTA FECHADA DENTRO DE LA VENTANA</code> — sin publicación indexada del 20-oct que ARGOS 138 no hubiera publicado</td></tr>'
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>20-oct 07:06 → 20-oct 07:49 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,00 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>.
  </p>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Entidad · Municipio</th><th>Hecho</th><th>Nivel de riesgo</th><th>Fuente institucional</th><th>Fuente nacional</th><th>Confianza</th><th>ARG-ID</th></tr></thead>
    <tbody>
{rows_own}
{rows_rec}
    </tbody>
  </table></div>

  <div class="section-head" style="margin-top:10px;">TOTALES DEL CORTE — CÁLCULO PROPIO DE ARGOS</div>
  <p class="muted-note" style="margin:0 0 6px 0;">
    <code>NINGUNA AUTORIDAD PUBLICÓ UN AGREGADO NACIONAL DE ESTA VENTANA.</code>
  </p>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Armas cortas</th><th>Armas largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos en aseguramiento</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{TOT[2]}</b></td><td><b>{TOT[3]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> · <b>Muertos en hechos propios</b>: <b>{MU}</b> · <b>Heridos</b>: <b>{HE}</b> · en la recuperación, <b>{HE_REC} herida</b>, fuera de todo total. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-136-006, ingreso al penal del Altiplano por traición a la patria, por titular (El Financiero 2026/10/20); resultado de la audiencia inicial federal no publicado; vinculación estatal el jueves, por titular de Excélsior (22-oct por calendario); 10:00, solo por resumen · ARG-138-007, segunda ruta (Luz Noticias 2026-10-20); «militares agredidos», solo por resumen, sin parte de la Defensa · ARG-138-010, publicado el 20-oct por ruta (El Diario de Chihuahua 2026/oct/20); SSPE como emisora, solo por resumen; situación jurídica no publicada · ARG-138-006, víctima de nombre Daniel, solo por resumen; un medio lo sitúa «este martes»: <code>DÍA CONTRADICHO</code> · ARG-138-011, primera publicación el 19-oct por ruta (ABC Noticias 2026/10/19); 2 operativos (Posta) o 4 (MVS, ABC), solo por resumen: <code>CONTRADICHO</code> · ARG-138-001, «noche del miércoles» incompatible con el calendario; heridos 2 a 3 y menor de 2 o 3 años: sin resolver · ARG-138-REC-001, ningún detenido publicado al 20-oct · ARG-137-007, la Mesa de Coordinación de Colima atribuye la agresión a los abatidos («dispararon contra los elementos, quienes respondieron»), solo por resumen (Infobae, La Jornada 2026/10/19); sin parte de la Marina · Santiago Tulantepec, Hidalgo: fallo condenatorio del 9-oct por la muerte de tres mujeres, «triple feminicidio» por titular (La Silla Rota 2026/10/9); calificación por víctima solo por resumen: <code>CONTRADICHA</code>; individualización de la pena el miércoles 21-oct.
  </p>
'''

byid = {r["id"]: r for r in R}
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], NI),
 tile(1, "Armas largas", TOT[1], NI),
 tile(2, "Sin categoría", TOT[2], NI),
 tile(3, "Cartuchos", fmt(TOT[4]), NI),
 tile(4, "Cargadores", TOT[5], NI),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA EN HECHO PROPIO</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>NINGÚN DETENIDO EN EVENTO DE ASEGURAMIENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>Total nacional del corte</b>: en la página de panorama.
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Sin aseguramiento integrable en el corte.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'


arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
{chr(10).join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> — ningún aseguramiento con cantidad publicada y fecha del hecho o de publicación dentro de la ventana</td></tr>'}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: sin lectura (ninguna fila integrada).
    <br><code>VISTOS, NO INTEGRADOS — VENTANAS ANTERIORES</code>: <b>Michoacán, Cotija (Lourdes)</b>, Ejército, 1 arma larga, 1 cargador y 25 cartuchos, por resumen del agregado federal del 16, 17 y 18-oct (Milenio, publicado el 19) · <b>Baja California, La Rumorosa</b>, 2 detenidos, 5 armas y 17 cargadores, solo por resumen (En Línea BC 2026/10/19) · <b>Puebla, Chietla y Tehuacán</b>, Marina, 4 detenidos y un arma de fuego, cartuchos sin cifra (Tus Buenas Noticias 2026/10/19) · <b>Sonora, Hermosillo (Villa de Seris)</b>, 2 detenidos y 1 arma corta 9 mm, por titular (El Imparcial 2026/10/18) · <b>Sinaloa, Culiacán (Industrial Bravo)</b>, 16-oct, 4 detenidos, una ametralladora 7.62 y 3 pistolas; 420 cartuchos —385 de 7.62 mm, 25 de 9 mm y 10 de .45—, solo por resumen.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">4 casos candidatos sin boletín</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>18 estatales revisadas</b>, 15 de lectura parcial · 14 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Sinaloa</b><br>Culiacán</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">feminicidio en grado de tentativa, por titular; hechos de abril de 2025, col. Libertad, solo por resumen</span></td><td><b>18 años</b>, por titular</td><td>FGE Sinaloa <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Luz Noticias y Línea Directa 2026-10-19 · boletín no localizado · publicado el 19-oct · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>General Cepeda</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">sustracción ilícita de hidrocarburo, por titular; procedimiento abreviado, solo por resumen</span></td><td><b>más de 13 años</b>, por titular; 13 años 4 meses, solo por resumen; multa sin monto</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Miled 2026/10/19 · boletín no localizado · publicado el 19-oct · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Sonora</b><br>Caborca</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">transporte de casi 100 kg de metanfetamina, por titular</span></td><td><b>8 años</b>, solo por resumen</td><td>FGR <span class="muted-note">(por titular de Telemax)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Telemax, Infobae y El Heraldo de México 2026/10/19 · boletín no leído · publicado el 19-oct · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Tres sentenciados, nombres no reproducidos · <span class="muted-note">homicidio calificado de tres surfistas extranjeros (2024), robo con violencia y robo de vehículo, por titulares</span></td><td><b>158 años 9 meses</b>, por titular; por cada sentenciado (135 años + 10 años 9 meses + 13 años), solo por resumen de dos medios · no se suma entre sentenciados · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>FGE Baja California <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · El Financiero y CR Prensa 2026/10/17 · boletín no localizado en <code>fgebc.gob.mx</code> · individualización del 16-oct, solo por resumen</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Fuera de ventana, sin integrar</b>: Oaxaca, 80 años por feminicidio agravado (FGEO, boletín 2889, 13-oct, fecha por listado) · Tamaulipas, FGJE-370-2026 (6-oct) · Santiago Tulantepec, fallo del 9-oct sin pena.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>18 de 32</b>, de ellas <b>15 de lectura parcial</b> · lectura no parcial: Tamps, Oax, Gro · parcial: BC, BCS, Chih · Jal, Nay, Ags, Mich, Col · CDMX, Edomex, Pue, Qro · Ver, Tab · QRoo · <b>FGR revisada: no</b> (solo por medios)</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> · candidatas solo por medios, publicadas antes de la ventana: Sinaloa, Baja California, FGR (Coahuila y Sonora)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>18</b> fiscalías estatales, 15 de lectura parcial</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>14</b>: Sin, Son, Dgo · Coah, NL, SLP, Zac · Gto · Mor, Tlax, Hgo · Chis, Camp, Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 07:49 del 20-oct: código <code>000</code> · <b>dominios no devueltos por el buscador</b>: <code>fiscalia.guanajuato.gob.mx</code>, <code>fiscaliachiapas.gob.mx</code>, <code>fiscalia.chiapas.gob.mx</code>, <code>fgecam.gob.mx</code>, <code>fgecampeche.gob.mx</code>, <code>fiscalia.yucatan.gob.mx</code>, <code>ssp.nl.gob.mx</code>, <code>seguridad.jalisco.gob.mx</code>, <code>ssp.tabasco.gob.mx</code>, <code>ssp.chihuahua.gob.mx</code> · <code>fiscaliasinaloa.mx</code> devuelve solo documentos normativos</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 21 de 32 con consulta propia por entidad</b> · <b>11 solo por consulta regional amplia</b>: BCS, Dgo · Coah, SLP, Zac · CDMX, Pue, Tlax, Qro · Camp, Yuc · <b>armamento: 13 de 32 por dominio oficial</b> —Chih, Sin · Coah, Tamps, SLP, Zac · Mich · Ver, Tab · Oax, Camp, Yuc, QRoo—, de ellas <b>9 de lectura parcial</b> (Chih, Mich, Ver, Tab, Camp, Yuc, QRoo, Zac, Tamps); <code>NO REVISADA</code> (19): BC, BCS, Son, Dgo · NL · Jal, Nay, Ags, Col, Gto · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Gro, Chis</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 16, 17 y 18-oct</b>: agregado publicado el 19-oct, ya registrado en ARGOS 137 · <b>acciones del 19 y del 20-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta · <b>gabinetedeseguridad.gob.mx</b>: dominio no devuelto</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 20-OCT 07:49: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>SIN EVENTO ROJO PROPIO EN LA VENTANA</b>: 0 rojos, 0 amarillos, 0 verdes.
      <br><b>2.</b> <b>Última lectura del nivel</b>: los dos rojos de ARGOS 138, ARG-138-001 y ARG-138-002, ambos con reserva.
      <br><b>3.</b> <b>Ventana anterior</b>: ARG-139-REC-001.
      <br><b>4.</b> <b>Respuesta institucional propia</b>: ninguna acción publicada en la ventana.
      <br><b>5.</b> <code>43 MIN; NINGUNA PUBLICACIÓN DEL 20-OCT INDEXADA AL CORTE: TOTALES NO COMPARABLES CON LA SERIE.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. FOSAS DE LA FRONTERA NORTE LOCALIZADAS POR COLECTIVOS, SIN CIFRA OFICIAL.</b> ARG-135-REC-003 (Tijuana, Cachanillas): «van 10 cuerpos en tres días de búsqueda», cuerpos, osamentas y restos, por titular (Punto Norte 2026/10/18) · ARG-135-REC-004 (Nogales, Mariposa) y Sonoyta: «8 osamentas en 3 días», por titular (El Imparcial 2026/10/19); 7 en Nogales y 1 en Sonoyta, solo por resumen. Cifras de colectivos, no oficiales. Línea: <b>solicitar a las fiscalías de Baja California y Sonora la cifra oficial y el avance de identificación</b>.
      <br><b>2. ENFRENTAMIENTOS CON FUERZAS FEDERALES SIN PARTE PUBLICADO.</b> ARG-138-007 (Navolato, Ejército) y ARG-137-007 (Colima, Marina): en los dos, la agresión atribuida a los civiles procede de medios o de una mesa estatal, solo por resumen. Línea: <b>solicitar a la Defensa y a la Marina el parte, quién inició y el armamento asegurado</b>.
      <br><b>3. EXFISCAL DE CHIHUAHUA: DOS PROCESOS EN CURSO.</b> ARG-136-006: federal por traición a la patria, con ingreso al Altiplano; estatal por ejercicio ilegal del servicio público y coalición, solo por resumen. Línea: <b>vigilar la audiencia de vinculación estatal del jueves 22-oct 10:00 y la medida cautelar federal</b>.
      <br><b>4. CONDENAS PUBLICADAS SOLO POR MEDIOS.</b> Feminicidio en tentativa (Culiacán), huachicol (General Cepeda), metanfetamina (Caborca) y homicidio múltiple (Ensenada): cuatro condenas del 17 y 19-oct sin boletín leído. Línea: <b>solicitar a la FGR y a las fiscalías de Sinaloa y Baja California los boletines, la firmeza y la reparación del daño</b>.
      <br><b>5. SINALOA, MAZATLÁN: HOMICIDIO EN PLAZA COMERCIAL CON POSIBLE ANTECEDENTE.</b> ARG-138-006 y un homicidio en el estacionamiento de una plaza de La Marina publicado por Noroeste sin día en la ruta, posiblemente el 11-oct. Línea: <b>solicitar a la FGE Sinaloa si son el mismo lugar y si los casquillos coinciden</b> — hipótesis.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — dominio no devuelto por el buscador; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>gob.mx/fgr</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — VENTANA ANTERIOR: ARGOS 129", rec1)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if a["integra"] and any(a["c"]))
script = script.replace('"<br>Consulta: " + (top.fecha || "—") + " " + (top.hora || "")', '"<br>Fecha y hora (hecho o publicación): " + (top.fecha || "—") + " " + (top.hora || "") + "<br>Consulta: " + CONSULTA_TXT')
if "const CONSULTA_TXT" in script:
    script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
else:
    script = script.replace("const CORTE_FECHA", f'const CONSULTA_TXT = "{CONSULTA}";\nconst CORTE_FECHA', 1)
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert "WINDOW_DAYS = 2;" in script  # el radar conserva la escala de dos días; la ventana de 43 min no tiene ecos propios
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
