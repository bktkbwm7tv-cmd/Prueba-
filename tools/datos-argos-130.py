# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 130: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-130.py <plantilla ARGOS 129> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "130", "2026-10-12", "08:19"
CONSULTA = "2026-10-12 08:19-08:50"
DUR = "23 h 21 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
A129 = "<code>SI FUE ANTES DE LAS 08:58 DEL 11-OCT, PERTENECE A LA VENTANA DE ARGOS 129</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-130-001", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-11", hora="~12:30 (solo por resumen, atribuida a la SSP)",
  ent="Michoacán", mun="Jacona (base de Bomberos y Protección Civil)", dia="11-OCT ~12:30",
  title="MICHOACÁN · JACONA — COMANDO ATACA LA BASE DE BOMBEROS Y A POLICÍAS MUNICIPALES: DOS POLICÍAS MUERTOS; TRES AGRESORES ABATIDOS EN LA HUIDA",
  hecho="Jacona · <code>BASE DE BOMBEROS Y PROTECCIÓN CIVIL; LIBRAMIENTO Y CARRETERA JACONA–JIQUILPAN — VIALIDAD CONTRADICHA</code> · DOMINGO 11-OCT, ~12:30 (" + RES + ", atribuida a la SSP) · comando armado en camionetas dispara contra la base y contra policías municipales · <b>2 policías municipales muertos</b>, por titular (🔴) · en la huida, GN y Guardia Civil enfrentan a los agresores cuando colocaban ponchallantas: <b>3 agresores abatidos</b>, por titular · <code>SALDO CONTRADICHO: «6 MUERTOS Y 3 HERIDOS», TITULAR ATRIBUIDO A LA FGE, FRENTE A «8 MUERTOS Y 6 HERIDOS», TITULAR DE QUADRATÍN Y OTROS MEDIOS</code> · al menos 1 civil muerto y una paramédica herida, " + RES + " · <b>cero detenidos</b> · armas largas y una camioneta aseguradas, <code>SIN CIFRA PUBLICADA — CANTIDAD NO DETERMINADA</code> · despliegue de GN, Guardia Civil, Defensa y FGE en Jacona y Zamora · identidades: no se reproducen · " + FR,
  panel="Ataque a la <b>base de Bomberos</b> y a policías: <b>2 policías muertos</b>, 3 agresores abatidos; saldo total 6 u 8, contradicho",
  inst="SSP Michoacán · FGE Michoacán <span class=\"muted-note\">(por cita)</span>", nac="El Heraldo de México · Excélsior · 24 Horas · Telediario · En Blanco y Negro", conf="★★★☆☆",
  campo="saldo total contradicho (6 u 8 muertos); hora solo por resumen", I=1, N=5, R=9, A=1,
  fechadas=["El Heraldo de México (2026/10/11)", "En Blanco y Negro (2026/10/11)", "La Prensa de Coahuila (2026/10/11)", "Quinto Poder (2026/10/12)"], estatus="Parcialmente corroborado", arm=None,
  desl="Jacona no figura en el índice ni en las tres ediciones previas. NO es Zamora, bar El Nuevo Quijote (ARG-129-REC-001). «3 policías y 4 agresores»: un solo medio. Aseguramiento del mismo día en Atecucario, Zamora: sin cifras ni vínculo acreditado, no se ficha. Blog del Narco: <code>NO OFICIAL</code>. 🔴 por ataque contra autoridades con muerte de personal"),
 dict(id="ARG-130-002", estado="MX-ROO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-11", hora="~20:30 (solo por resumen)",
  ent="Quintana Roo", mun="Cancún (fracc. Los Corales, SM 77)", dia="11-OCT ~20:30",
  title="QUINTANA ROO · CANCÚN — DOS MOTOCICLISTAS ASESINAN A UNA MUJER Y A UN INSTRUCTOR DE BAILE EN LOS CORALES",
  hecho="Cancún · <code>FRACC. LOS CORALES, SM 77, ESTACIONAMIENTO DE UN EDIFICIO</code> · DOMINGO 11-OCT, noche, ~20:30 (" + RES + ") · dos hombres en motocicleta disparan contra una mujer y un instructor de baile · <b>2 muertos</b> —una mujer de ~50 años y un hombre de ~35—, por titular (🔴) · <code>MÓVIL: CONFUSIÓN DE OBJETIVO, HIPÓTESIS NO CONFIRMADA</code> · <b>cero detenidos</b> · Servicios Periciales del estado procesa el lugar, " + RES + " · identidades: no se reproducen · " + FR,
  panel="<b>2 muertos</b> por disparos de dos motociclistas",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Noticaribe (2026/10/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Los Corales y la SM 77 no figuran en el índice. NO son los ataques a mototaxistas del 7-oct ni la doble ejecución del Polígono Sur del 25-sep (fuentes en el archivo). 🔴 por homicidio múltiple"),
 dict(id="ARG-130-003", estado="MX-TAB", region="Golfo", color="rojo", impacto="mediano", fecha="2026-10-11", hora="madrugada, ~03:00 (solo por resumen)",
  ent="Tabasco", mun="Nacajuca (ranchería Taxco)", dia="11-OCT, MADRUGADA",
  title="TABASCO · NACAJUCA — ASESINAN EN SU VIVIENDA A UN MATRIMONIO Y A SU HIJA DE 13 AÑOS",
  hecho="Nacajuca · <code>RANCHERÍA TAXCO, VIVIENDA</code> · madrugada del DOMINGO 11-OCT, ~03:00 (" + RES + ") · dos hombres armados irrumpen en la vivienda · <b>3 muertos</b> —un hombre de 46 años, una mujer de 42 y su hija de 13—, por titular (🔴) · <b>FGE Tabasco</b> confirma el ataque y abre carpeta, por titular · <b>cero detenidos</b> · operativo estatal y federal, " + RES + " · identidades: no se reproducen · " + A129 + " · " + FR,
  panel="<b>3 muertos</b> en una vivienda: un matrimonio y su hija de 13 años",
  inst="FGE Tabasco <span class=\"muted-note\">(por titular de medios)</span>", nac="El Universal · Excélsior · N+", conf="★★★☆☆",
  campo="hora solo por resumen", I=1, N=3, R=9, A=0,
  fechadas=["Diario de Tabasco (2026/10/11)", "El Heraldo de San Luis Potosí (2026/10/11)", "La Prensa de Coahuila (2026/10/11)", "El Mañana (2026/10/12)"], estatus="Parcialmente corroborado", arm=None,
  desl="Taxco (Nacajuca) no figura en el índice; Nacajuca figura (ARG-108-007): otro hecho. Azteca Chiapas «hoy-11-de-octubre»: forma de <i>liveblog</i>, no fecha el hecho. 🔴 por homicidio múltiple con una menor"),
 dict(id="ARG-130-004", estado="MX-MIC", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-11", hora="madrugada, ~05:00 (solo por resumen)",
  ent="Michoacán", mun="Morelia (col. Solidaridad)", dia="11-OCT, MADRUGADA",
  title="MICHOACÁN · MORELIA — ATAQUE ARMADO EN UN NEGOCIO DE MICHELADAS DE LA COLONIA SOLIDARIDAD: DOS MUERTOS Y UN HERIDO",
  hecho="Morelia · <code>COL. SOLIDARIDAD, NEGOCIO DE MICHELADAS</code> · madrugada del DOMINGO 11-OCT, ~05:00 (" + RES + ") · hombres armados disparan contra el negocio · <b>2 muertos</b> y <b>1 herido</b>, por titular (🔴) · 17 casquillos, " + RES + " · <b>cero detenidos</b> · identidades: no se reproducen · " + A129 + " · " + FR,
  panel="<b>2 muertos</b> y 1 herido en un negocio de micheladas",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Changoonga (2026/10/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Solidaridad (Morelia) no figura en el índice; Morelia figura: otros hechos. Un segundo ataque en Ilustres Novohispanos, citado solo por un resumen, sin nota localizada: no se ficha. 🔴 por homicidio múltiple"),
 dict(id="ARG-130-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-11", hora="aviso ~11:00 (solo por resumen)",
  ent="Sinaloa", mun="Navolato (San Pedro)", dia="11-OCT ~11:00",
  title="SINALOA · NAVOLATO — HALLAN A UN HOMBRE ASESINADO Y ENVUELTO EN PLÁSTICO JUNTO A LA AUTOPISTA, EN SAN PEDRO",
  hecho="Navolato · <code>SAN PEDRO, JUNTO A LA AUTOPISTA BENITO JUÁREZ</code> · DOMINGO 11-OCT, aviso ~11:00 (" + RES + ") · hallazgo · <b>1 hombre asesinado</b>, envuelto en plástico, por titular (🟡) · <code>DOS TITULARES DEL MISMO DÍA; QUE SEAN UN SOLO HALLAZGO NO ESTÁ ACREDITADO: SE CUENTA UNO</code> · <b>cero detenidos</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 hombre asesinado</b>, hallado envuelto en plástico",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="hora solo por resumen; un solo hallazgo no acreditado; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-10-11)", "Línea Directa (2026-10-11)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Pedro (Navolato) no figura en el índice. 🟡 por homicidio doloso único; si son dos cuerpos, sube a rojo"),
 dict(id="ARG-130-006", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-11", hora="no publicada",
  ent="Sinaloa", mun="Escuinapa (col. El Roblito)", dia="PUB. 11-OCT, HORA NO FIJADA",
  title="SINALOA · ESCUINAPA — ASESINAN A BALAZOS A UN HOMBRE DENTRO DE SU DOMICILIO EN LA COLONIA EL ROBLITO",
  hecho="Escuinapa · <code>COL. EL ROBLITO, DOMICILIO</code> · publicado el DOMINGO 11-OCT; hora no publicada · <b>1 hombre asesinado</b> a balazos dentro de su domicilio, por titular (🟡) · <b>cero detenidos</b> publicados · identidad: no se reproduce · " + FR,
  panel="<b>1 hombre asesinado</b> en su domicilio",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="una sola fuente; hora no publicada", I=0, N=0, R=1, A=0,
  fechadas=["Línea Directa (2026-10-11)"], estatus="Pendiente de corroboración", arm=None,
  desl="El Roblito no figura en el índice. NO es ARG-129-003 (col. Insurgentes) ni ARG-129-004 (zona centro). 🟡 por homicidio doloso único"),
 dict(id="ARG-130-007", estado="MX-GRO", region="Sureste", color="verde", impacto="mediano", fecha="2026-10-11", hora="no publicada",
  ent="Guerrero", mun="Acapulco", dia="PUB. 11-OCT, HORA NO FIJADA",
  title="GUERRERO · ACAPULCO — DETIENEN A «EL JUNIOR», SEÑALADO LÍDER DE UNA CÉLULA VINCULADA A «LOS RUSOS»",
  hecho="Acapulco · <code>LUGAR DE LA CAPTURA CONTRADICHO</code> · anunciada el DOMINGO 11-OCT por el titular de la SSPC; hora no publicada · <b>SSPC y Semar</b>, con Policía Estatal y FGE Guerrero (" + RES + ") · detención de Eliceo «N», «El Junior» · <b>1 detenido</b> (🟢) · señalado por el ataque a agentes federales de octubre de 2025, por titular · <code>ASEGURAMIENTO CONTRADICHO: «DOS ARMAS DE FUEGO, CARTUCHOS, 300 DOSIS Y UNA CAMIONETA» FRENTE A «1 LARGA, 1 CORTA Y 2 CARGADORES», SOLO POR RESUMEN — CANTIDAD NO DETERMINADA</code> · " + FR,
  panel="Detenido <b>«El Junior»</b>, célula vinculada a «Los Rusos»; armamento sin cifra fijada",
  inst="SSPC <span class=\"muted-note\">(anuncio en redes, por cita)</span>", nac="El Financiero · Proceso · Infobae · La Razón · El Universal · Aristegui", conf="★★★☆☆",
  campo="hora no publicada; aseguramiento contradicho, solo por resumen", I=1, N=8, R=6, A=0,
  fechadas=["El Financiero (2026/10/11)", "Proceso (2026/10/11)", "Infobae (2026/10/11)", "La Razón (2026/10/12)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="2026-10-11 (anuncio), hora no publicada",
  desl="«El Junior» no figura en el índice; «Los Rusos» figura (ARG-115-002, ARG-118-REC-001): otros hechos. El ataque de octubre de 2025 no se recalifica. Agresión al personal en la captura: una nota, no acreditada. Armamento: evento cualitativo, fuera del conteo"),
 dict(id="ARG-130-008", estado="MX-CHH", region="Noroeste", color="verde", impacto="pequeno", fecha="2026-10-11", hora="no publicada",
  ent="Chihuahua", mun="Ciudad Juárez (col. Francisco I. Madero)", dia="PUB. 11-OCT, HORA NO FIJADA",
  title="CHIHUAHUA · CIUDAD JUÁREZ — DETIENEN A TRES HOMBRES CON UN REVÓLVER Y 34 CARTUCHOS",
  hecho="Ciudad Juárez · <code>COL. FRANCISCO I. MADERO</code> · publicado el DOMINGO 11-OCT; hora no publicada · <b>SSP Municipal de Juárez</b> · <b>3 detenidos</b>, por titular (🟢) · <b>1 revólver calibre .38</b>, por titular · <b>34 cartuchos</b>, por titular · sin enfrentamiento publicado · " + FR,
  panel="<b>3 detenidos</b> con 1 revólver y 34 cartuchos",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span> · SSPM Juárez <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="hora no publicada; sin boletín institucional", I=0, N=0, R=3, A=0,
  fechadas=["Diario de Juárez (2026/oct/11)", "El Diario de Chihuahua (2026/oct/11)", "La Opción (20261011)"], estatus="Parcialmente corroborado", arm="ARG-130-ARM-001", fecha_txt="2026-10-11, hora no publicada",
  desl="Col. Francisco I. Madero (Ciudad Juárez) no figura en el índice; la homónima de Colima (ARG-106-002) es otro hecho"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = []

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-130-ARM-001", ficha="ARG-130-008", estado="MX-CHH", region="Noroeste", ent="Chihuahua", mun="Ciudad Juárez (col. Francisco I. Madero)", c=[1,0,0,0,34,0,0,0,0,3], corp="SSP Municipal de Juárez", conf="Bajo", color="verde", fecha="2026-10-11", hora="no publicada", fecha_txt="2026-10-11<br><span class=\"muted-note\">hora no publicada</span>", nota="Aseguramiento sin enfrentamiento; cifras por titular de tres medios regionales; sin comunicado oficial", fuentes=["Diario de Juárez (2026/oct/11)", "El Diario de Chihuahua (2026/oct/11)", "La Opción (20261011)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [1, 0, 0, 0, 34, 0, 0, 0, 0, 3], TOT
assert cnt == {"rojo": 4, "amarillo": 2, "verde": 2}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0}, cnt_rec
assert len(ENT) == 6, ENT

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else "sin fila — no hubo armamento asegurado")
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
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"]}

def arm_json(a):
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 129 — Reporte Nacional de Seguridad — 2026-10-11</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <div class="map-caption">Color = evento de mayor impacto por entidad. Pase el cursor sobre un estado.</div>
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
      <b>1. EXIJA A LA FISCALÍA DE MICHOACÁN EL SALDO OFICIAL DE JACONA</b> (ARG-130-001) —6 u 8 muertos— y el inventario de las armas
      aseguradas a los agresores; refuerce la custodia de las bases de Bomberos y Protección Civil del corredor Zamora–Jacona.
      <br><b>2. EXIJA A PEMEX Y A LA FISCALÍA DE VERACRUZ EL SALDO OFICIAL DE MINATITLÁN</b> (ARG-129-001) y audite la seguridad física de los
      accesos de la refinería.
      <br><b>3. PIDA A LA SEMAR EL COMUNICADO ÍNTEGRO DEL 10-OCT</b> (ARG-129-005): fecha y lugar de cada evento, y cotejo de sus siete artefactos
      explosivos con ARG-125-005.
      <br><b>4. EXIJA A LA SSPC EL INVENTARIO DE LO ASEGURADO A «EL JUNIOR»</b> (ARG-130-007): número y tipo de armas, cartuchos y lugar de la
      captura.
      <br><b>5. EXIJA A LA FISCALÍA DE OAXACA EL COMUNICADO DE PINOTEPA</b> (ARG-128-001): cifra oficial de víctimas, detenidos y constancia del
      Mecanismo de Protección.
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>11-oct 08:58 → 12-oct 08:19 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,34 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>. <b>Los ocho</b> llevan <code>FRONTERA DE VENTANA</code>; dos, con indicio de madrugada.
    <br><code>SIN RECUPERACIONES DE VENTANAS ANTERIORES EN ESTA EDICIÓN.</code>
    <br><b>Toque un ARG-ID para ir a su ficha</b>, donde están las fuentes, el nivel de confianza y los deslindes.
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
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Armas cortas</th><th>Armas largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{TOT[2]}</b></td><td><b>{TOT[3]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Total de armas integradas: {ARMAS}</b>, por titular. <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento</b>; el de Acapulco, con armamento sin cifra fijada, no entra. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios: 15</b> —6 en Jacona, cifra atribuida a la FGE, 3 en Nacajuca, 2 en Cancún, 2 en Morelia y 2 en Sinaloa—; <b>17</b> con la cifra de 8 en Jacona. <b>Heridos: 4 o 7</b>. Incluye 3 agresores abatidos: <b>cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:4])
co2 = "\n".join(ficha(e) for e in E[4:])

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "Ciudad Juárez · revólver .38 · por titular"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA CON CIFRA</code> · Jacona, sin cifra"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR INTEGRADA</code> · Acapulco, contradicho"),
 tile(3, "Cartuchos", fmt(TOT[4]), "Ciudad Juárez · por titular"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN CARGADOR CON CIFRA FIJADA</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>{len(ARM)} fila de armamento de {len(ARM)} hecho</b> en <b>{len(ENT_ARM)} entidad</b>, <b>cifras por titular</b>. <b>Totales por categoría: cálculo propio.</b>
    <code>NINGUNO DE LOS CUATRO ROJOS DEJÓ ARMAMENTO CON CIFRA PUBLICADA: JACONA, «ARMAS LARGAS» SIN NÚMERO.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Verde = aseguramiento sin enfrentamiento · amarillo = derivado de enfrentamiento o agresión. La sola presencia de armas no vuelve roja a una entidad.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    cells = "".join(f"<td>{('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for v in c[:9])
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    return f'      <tr id="{a["id"]}"><td><a href="#{a["ficha"]}"><code>{a["id"]}</code></a></td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'
arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
{chr(10).join(armrow(a) for a in ARM)}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b> —1 fila, <b>cálculo propio</b>—: <b>Noroeste 1</b> · <b>Noreste 0</b> · <b>Occidente 0</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    <b>Eventos cualitativos sin cantidad</b>: Jacona (ARG-130-001) y Acapulco (ARG-130-007), en su ficha, <b>fuera de esta tabla</b>.
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: Guanajuato, boletín estatal del 11-oct (boletines.guanajuato.gob.mx, 2026/10/11) sobre aseguramientos del 25 y 26-sep en Santiago Maravatío y Valle de Santiago: 1 arma corta, 1 cargador, 2 cartuchos y 3 detenidos, solo por resumen.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA INTEGRABLE</code> · candidatas solo por medios, abajo</span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas quedan en <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto ordenado y publicado por fuente oficial</b> en la ventana</span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>de 15 revisadas</b> · FGR no revisada · 17 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Zacatecas</b></td><td>José «N» · <span class="muted-note">violencia familiar agravada y lesiones; procedimiento abreviado</span></td><td><b>3 años, 2 meses y 28 días</b>, solo por resumen</td><td>FGJ Zacatecas <span class="muted-note">(por cita)</span></td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code>: misma pena exacta que Juan «N», publicado el 8-oct · publicado el <b>11-oct</b> · <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>García y Santa Catarina</td><td>Tres personas · <span class="muted-note">secuestro agravado y homicidio calificado, enero de 2022</span></td><td><b>105 años 10 meses; 80 años; 25 años 10 meses</b>, solo por resumen</td><td>FGE Nuevo León <span class="muted-note">(por cita)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>10-oct</b> (MVS, Enfoque) · ventana de ARGOS 129</td><td>Bajo</td></tr>
      <tr><td><b>Sinaloa</b><br>Navolato (Villa Juárez)</td><td>Manuel Antonio «N» · <span class="muted-note">feminicidio agravado de una menor</span></td><td><b>80 años</b>, por titular · <code>TOPE DE 70 O 60 AÑOS, CONTRADICHO</code></td><td>FGE Sinaloa <span class="muted-note">(slug de un republicador)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · el término «sentencia condenatoria» solo en el slug de un republicador, no en el dominio oficial · ventana de ARGOS 129</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Tres personas · <span class="muted-note">feminicidio y homicidio</span></td><td><code>SIN PENA: VEREDICTO; INDIVIDUALIZACIÓN DE SANCIONES, 14-OCT</code></td><td>PGJ Hidalgo <span class="muted-note">(por cita)</span></td><td><b>No es sentencia</b> hasta la audiencia de individualización · fecha del veredicto no fijada</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Baja California, Ensenada</b>: veredicto del 9-oct; individualización de sanciones el <b>16-oct</b>, sin pena. <b>Vistas, publicadas antes de la apertura</b>: Tamaulipas FGJE-370 (6-oct), Querétaro, Corregidora (8-oct), FGR Campeche y Quintana Roo (7 y 9-oct), Oaxaca, Magdalena Teitipac (9-oct), Guanajuato, León (9-oct). <code>NO SE INTEGRAN: FUERA DE VENTANA O SIN BOLETÍN OFICIAL.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>15 de 32</b> · <b>FGR revisada: No</b> · BCS, Chih, Dgo · Coah, NL, Tamps, SLP · Jal, Nay · CDMX, Qro · Ver, Tab · Oax, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>0</b></td></tr>
      <tr><td><b>Con sentencia publicada en ventana solo por medios</b></td><td><b>1</b>: Zacatecas, posible caso homónimo</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>17</b>: BC, Son, Sin · Zac · Col, Ags, Mich, Gto · Edomex, Mor, Pue, Tlax, Hgo · Gro, Chis, Camp, Yuc</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 31 de 32</b> —Ags, <code>NO REVISADA</code>— · <b>armamento: 18 de 32</b> —BC, Son, Chih, Sin · NL, SLP, Zac · Mich, Gto · CDMX, Edomex, Mor, Pue, Tlax · Ver, Tab · Gro, Oax; las otras 14, <code>NO REVISADA</code>— · <code>REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, SEDENA y SEMAR: <code>NO REVISADA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 9, 10 y 11-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta; último indexado, acciones del 8-oct</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 12-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR CUATRO ROJOS</b>: ARG-130-001 a ARG-130-004 (Michoacán, Quintana Roo y Tabasco).
      <br><b>2.</b> <b>Contexto operativo</b>: dos amarillos en Sinaloa (ARG-130-005, ARG-130-006).
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-130-007 y ARG-130-008; <b>ningún detenido publicado</b> por los cuatro rojos.
      <br><b>4.</b> <b>Seguimiento</b>: en ARG-129-001 muere el segundo trabajador, por titular de cuatro medios; sin saldo oficial. Sin acto nuevo en ARG-128-001, ARG-128-003 y ARG-125-051.
      <br><b>5.</b> <code>23 H 21 MIN; LOS OCHO HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. HOMICIDIO MÚLTIPLE NOCTURNO EN VIVIENDAS Y NEGOCIOS.</b> ARG-130-003, ARG-130-004. Línea: <b>hora exacta y peritaje balístico</b>
      de cada ataque — patrón por validar.
      <br><b>2. SICARIATO EN MOTOCICLETA CON POSIBLE ERROR DE OBJETIVO EN CANCÚN.</b> ARG-130-002. Línea: <b>videovigilancia de la ruta de huida</b>
      y cotejo con ataques recientes en la ciudad — hipótesis.
      <br><b>3. HOMICIDIO SELECTIVO SOSTENIDO EN SINALOA.</b> ARG-130-005, ARG-130-006, tras ARG-129-003 y ARG-129-004. Línea: <b>cotejo balístico</b>
      entre los cuatro hechos — hipótesis.
      <br><b>4. ARMA CORTA DE CALIBRE .38 EN DETENCIÓN MUNICIPAL DE CIUDAD JUÁREZ.</b> ARG-130-008. Línea: <b>rastreo de origen del revólver</b>
      — no confirmado.
      <br><b>5. LA BRECHA ENTRE DETENCIÓN Y CONDENA SIGUE ABIERTA.</b> Ninguna sentencia integrable; las de Nuevo León y Sinaloa solo existen en
      medios. Línea: <b>exigir el boletín oficial</b> de cada sentencia anunciada.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — el buscador devolvió la portada, con el informe del 5-oct; <code>SIN RESULTADO INDEXADO EN VENTANA</code>. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: JACONA, CANCÚN, NACAJUCA Y MORELIA", co1)
 + page("CRIMEN ORGANIZADO (II) — SINALOA, ACAPULCO Y CIUDAD JUÁREZ", co2)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM)
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert "WINDOW_DAYS = 2;" in script  # la ventana 11-oct 08:58 → 12-oct 08:19 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R))
