# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 131: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-131.py <plantilla ARGOS 130> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "131", "2026-10-13", "07:23"
CONSULTA = "2026-10-13 07:23-08:30"
DUR = "23 h 04 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-131-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-12", hora="noche, ~20:15–20:40 (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (col. Vallado Viejo)", dia="12-OCT, NOCHE",
  title="SINALOA · CULIACÁN — COMANDO ATACA UNA VIVIENDA EN VALLADO VIEJO: CUATRO MUERTOS",
  hecho="Culiacán · <code>COL. VALLADO VIEJO, CALLE SEGUNDA, VIVIENDA</code> · noche del LUNES 12-OCT, ~20:15–20:40 (" + RES + ") · hombres armados disparan contra las personas reunidas en la vivienda · <b>3 muertos y 1 herido</b>, por titular; <b>el herido muere en el hospital: 4 muertos</b>, por titular (🔴) · <b>dos mujeres y dos hombres</b>, entre ellos una madre y su hijo, por titular · <b>ningún detenido publicado</b> · identidades: no se reproducen · " + FR,
  panel="Ataque a una vivienda: <b>4 muertos</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="López-Dóriga · El Universal", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=2, R=9, A=0,
  fechadas=["Línea Directa (2026-10-12, dos notas)"], estatus="Parcialmente corroborado", arm=None,
  desl="Vallado Viejo no figura en el índice ni en las tres ediciones previas. NO es el cateo de la col. Industrial Bravo / La Popular (9 y 10-oct) ni ARG-129-REC-002 (Los Pinos). Los Noticieristas 2026/10 (sin día) «asciende a cuatro muertos». 🔴 por homicidio múltiple"),
 dict(id="ARG-131-002", estado="MX-MOR", region="Centro", color="rojo", impacto="grande", fecha="2026-10-12", hora="tarde (solo por resumen)",
  ent="Morelos", mun="Totolapan, Tlayacapan, Atlatlahucan y Oaxtepec", dia="12-OCT, TARDE",
  title="MORELOS · TOTOLAPAN — TRAS LA CAPTURA DE «EL GÜERO GYM», BLOQUEOS, QUEMA DE VEHÍCULOS Y RETENCIÓN DE PERSONAL DE LA FISCALÍA: EL DETENIDO ES LIBERADO A CAMBIO",
  hecho="Totolapan, Oaxtepec, Tlayacapan y Atlatlahucan · LUNES 12-OCT, por la tarde (" + RES + ") · <b>FIDAI de la Fiscalía de Morelos</b> y fuerzas federales detienen a José David «N», «El Güero Gym» · enfrentamiento, <b>quema de vehículos y bloqueos carreteros</b>, por titular (🔴) · <b>3 colaboradores de la Fiscalía Regional Oriente retenidos</b> y liberados <b>a cambio del detenido</b>, por titular («lo canjeó») · 3 policías heridos y liberación ~19:35, " + RES + " · <b>2 policías de la SSPC Morelos muertos en un accidente de patrulla</b> en la autopista La Pera–Cuautla cuando acudían al apoyo, por titular · <code>POLICÍAS MUERTOS CONTRADICHO: 2 O 4, POR TITULAR; VÍNCULO CON EL OPERATIVO NO ACLARADO POR LA AUTORIDAD — ACCIDENTE, NO AGRESIÓN</code> · <code>LIBERADOS: 3 O 4, CONTRADICHO</code> · <b>la detención quedó revertida</b>: no se abre ficha verde · <b>ningún detenido publicado</b> por los bloqueos · " + FR,
  panel="<b>Narcobloqueos y quema de vehículos</b>; 3 colaboradores de la Fiscalía retenidos y canjeados por el detenido",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span> · Fiscalía de Morelos <span class=\"muted-note\">(por cita)</span>", nac="El Financiero · ADN40 · Infobae · Publimetro", conf="★★★☆☆",
  campo="hora y heridos solo por resumen; policías muertos contradichos (2 o 4); sin boletín institucional", I=0, N=6, R=11, A=0,
  fechadas=["El Financiero (2026/10/12)", "ADN40 (2026-10-12)", "El Informador (20261012)", "El Diario de Chihuahua (2026/oct/12)", "Infobae (2026/10/13)", "Publimetro (2026/10/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="«El Güero Gym» no figura en el índice. Totolapan figura (ARG-110-REC-001): es San Miguel Totolapan, Guerrero, otro hecho. Liveblog de Infobae del 13-oct: no fecha el hecho. Vinculación con el Cártel del Pacífico: solo por resumen. Los policías muertos en el accidente vial no se suman a los muertos por agresión. 🔴 por narcobloqueos y quema de vehículos con retención de servidores públicos"),
 dict(id="ARG-131-003", estado="MX-PUE", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-12", hora="~22:30 o antes de medianoche (solo por resumen)",
  ent="Puebla", mun="Puebla (11 Sur y Cuauhtémoc)", dia="12-OCT, NOCHE",
  title="PUEBLA · PUEBLA — RAFAGUEAN CON ARMAS LARGAS LA CAMIONETA DE LA COORDINACIÓN DE HOMICIDIOS DE LA FISCALÍA: UN AGENTE HERIDO",
  hecho="Puebla · <code>AV. 11 SUR Y CUAUHTÉMOC, SOLO POR RESUMEN — COLONIA CONTRADICHA: LOMAS DE CASTILLOTLA O GUADALUPE HIDALGO</code> · noche del LUNES 12-OCT, ~22:30 —día y hora " + RES + "— · agresores disparan con <b>armas largas</b>, por titular, contra una camioneta de la <b>Coordinación de Homicidios de la FGE Puebla</b> (🔴) · <b>1 agente ministerial o auxiliar del MP herido</b>, por titular · ataque desde motocicleta, " + RES + ", contradicho · <code>OBJETIVO CONTRADICHO: EL COORDINADOR GENERAL DE HOMICIDIOS O UN AGENTE DEL MINISTERIO PÚBLICO</code>, que no viajaba en la unidad · <b>ningún detenido publicado</b> · la FGE no emitió información · identidades: no se reproducen · " + FR,
  panel="Ataque con armas largas a la <b>Coordinación de Homicidios de la FGE</b>: <b>1 agente herido</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="hora y colonia solo por resumen; sin fuente institucional ni nacional", I=0, N=0, R=6, A=0,
  fechadas=["Capital Puebla (2026/10/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="La Coordinación de Homicidios de la FGE Puebla no figura en el índice. NO es el doble homicidio de Popular Castillotla (julio). Publicado el 13-oct: <code>SI OCURRIÓ DESPUÉS DE LAS 07:23 DEL 13-OCT, PERTENECE A ARGOS 132</code>; el texto lo sitúa el lunes por la noche. 🔴 por ataque del grupo criminal contra servidores públicos"),
 dict(id="ARG-131-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-12", hora="~10:00 (solo por resumen)",
  ent="Sinaloa", mun="Escuinapa (zona centro, estética)", dia="12-OCT ~10:00",
  title="SINALOA · ESCUINAPA — ASESINAN A BALAZOS A UNA MUJER DENTRO DE UNA ESTÉTICA DEL CENTRO",
  hecho="Escuinapa · <code>ZONA CENTRO, ESTÉTICA — CRUCE SOLO POR RESUMEN</code> · LUNES 12-OCT, ~10:00 (" + RES + ") · dos hombres armados entran y disparan · <b>1 mujer asesinada</b>, por titular (🟡) · huyen en motocicleta, " + RES + " · <b>FGE Sinaloa investiga</b>, por titular · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 mujer asesinada</b> dentro de una estética",
  inst="FGE Sinaloa <span class=\"muted-note\">(por titular de medios)</span>", nac="El Universal · Posta", conf="★★★☆☆",
  campo="hora solo por resumen; sin boletín institucional", I=1, N=2, R=5, A=0,
  fechadas=["Línea Directa (2026-10-12)", "La Prensa de Coahuila (2026/10/12)"], estatus="Parcialmente corroborado", arm=None,
  desl="NO es la mujer asesinada en una taquería el sábado 10-oct (otro hecho, anterior) ni ARG-130-006 / -009. «19 en el año» y «ocho mujeres en Sinaloa en doce días»: recuentos de medios, no oficiales. 🟡 por homicidio doloso único"),
 dict(id="ARG-131-005", estado="MX-OAX", region="Sureste", color="verde", impacto="grande", fecha="2026-10-12", hora="no publicada",
  ent="Oaxaca", mun="Océano Pacífico, frente a Huatulco", dia="PUB. 12-OCT, HORA NO FIJADA",
  title="OAXACA · PACÍFICO — LA MARINA ASEGURA 1.2 TONELADAS DE COCAÍNA FRENTE A HUATULCO Y DETIENE A SEIS PERSONAS",
  hecho="Océano Pacífico · <code>366 MILLAS NÁUTICAS AL SUR DE HUATULCO — DISTANCIA CONTRADICHA, SOLO POR RESUMEN</code> · publicado el LUNES 12-OCT; fecha del aseguramiento no publicada · <b>Semar</b>, con la Guardia Costera de EE. UU. · <b>1.2 toneladas</b> de presunta cocaína, por titular (🟢) · <b>6 detenidos</b>, por titular · cinco extranjeros, 1,268 kg en 46 bultos y afectación de 289 mdp, " + RES + " · entrega en la 22 Zona Naval y a la FGR, " + RES + " · sin armamento publicado · " + FR,
  panel="<b>1.2 t de cocaína</b> y <b>6 detenidos</b> en altamar",
  inst="Semar · SSPC <span class=\"muted-note\">(por cita)</span>", nac="La Razón · El Imparcial · Infobae", conf="★★★☆☆",
  campo="fecha del aseguramiento no publicada; comunicado solo por cita", I=1, N=3, R=5, A=0,
  fechadas=["La Razón (2026/10/12)", "El Imparcial (2026/10/12)", "Diario Puntual (2026/10/12)", "Sociedad Noticias (2026/10/12)", "Infobae (2026/10/13)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no publicada; publicado el 2026-10-12",
  desl="Huatulco y la cifra no figuran en las tres ediciones previas. Republicadores del mismo comunicado: no independientes. Un medio da 190 mn: contradicción declarada. Sin armamento: fuera del conteo"),
 dict(id="ARG-131-006", estado="MX-TAB", region="Golfo", color="verde", impacto="mediano", fecha="2026-10-12", hora="no publicada",
  ent="Tabasco", mun="Villahermosa", dia="PUB. 12-OCT, HORA NO FIJADA",
  title="TABASCO · VILLAHERMOSA — DETIENEN A «EL CABRA», SEÑALADO LÍDER DE LA MARA 18 BUSCADO POR EL SALVADOR",
  hecho="Villahermosa · publicado el LUNES 12-OCT · <code>FECHA DEL HECHO NO FIJADA: 9, 11 O 12-OCT, SOLO POR RESUMEN</code> · <b>anunciada por el titular de la SSPC</b>, por titular · Semar, Defensa, GN y corporaciones estatales, " + RES + " · detención de Óscar Ariel «N», «El Cabra», señalado líder de la <b>Mara 18</b> · <b>1 detenido</b>, por titular (🟢) · orden internacional; <b>buscado por El Salvador por 15 homicidios</b>, por titular · acusaciones, no condena · dosis de marihuana sin cifra · sin armamento publicado · " + FR,
  panel="Detenido <b>«El Cabra»</b>, señalado líder de la Mara 18",
  inst="SSPC <span class=\"muted-note\">(anuncio, por titular de medios)</span>", nac="Proceso · El Informador · El Financiero · La Jornada", conf="★★★☆☆",
  campo="fecha del hecho no fijada (9, 11 o 12-oct)", I=1, N=4, R=4, A=0,
  fechadas=["Proceso (2026/10/12)", "El Informador (20261012)", "El Financiero (2026/10/12)", "La Jornada (2026/10/13)", "Central Municipal (2026/10/12)", "Lo de Hoy (2026/10/13)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no fijada (11 o 12-oct); publicado el 2026-10-12",
  desl="«El Cabra» y Mara 18 no figuran en el índice. Liveblog de Infobae del 12-oct: no fecha el hecho. Si la captura fue el 11-oct antes de las 08:19 del 12, pertenecía a la ventana de ARGOS 130; si fue el 9-oct (un medio, solo por resumen), es evento anterior publicado durante el corte y sale de los totales. Sin armamento: fuera del conteo"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-131-REC-001", estado="MX-VER", region="Golfo", fecha="2026-10-11", hora="~18:30–19:00 (solo por resumen)", orig="ARGOS 130", col_orig="amarillo",
  ent="Veracruz", mun="Otatitlán (restaurante El Cedral)", dia="11-OCT, NOCHE",
  title="VERACRUZ · OTATITLÁN — ASESINAN EN SU RESTAURANTE AL EXALCALDE JORGE GUERRERO GARCÍA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 130</code> · <code>RESTAURANTE EL CEDRAL, JUNTO AL PASO DE LA PANGA DEL PAPALOAPAN — SOLO POR RESUMEN</code> · noche del DOMINGO 11-OCT, ~18:30–19:00 (" + RES + ") · hombres armados disparan contra el exalcalde de Otatitlán (2014-2017) y excandidato en 2025 · <b>1 muerto</b>, por titular (🟡 en su ventana) · <b>FGE Veracruz</b> sigue varias líneas de investigación, por titular · <b>ningún detenido publicado</b>",
  panel="Asesinado el <b>exalcalde de Otatitlán</b> en su restaurante", inst="FGE Veracruz <span class=\"muted-note\">(por titular de medios)</span>", nac="Proceso · Infobae · El Heraldo de México · MVS · Latinus",
  conf="★★★☆☆", campo="hora solo por resumen; sin boletín institucional", I=1, N=7, R=6, A=0,
  fechadas=["Proceso (2026/10/12)", "Infobae (2026/10/12)", "El Heraldo de México (2026/10/12)", "MVS (2026/10/12)", "Latinus (2026/10/12)", "Intolerancia (2026/10/12)"],
  desl="Otatitlán no figura en el índice. 🟡 por homicidio doloso único: un exalcalde no es servidor público en funciones; Latinus lo titula «violencia política». Dentro de la ventana de ARGOS 130, que no lo publicó"),
 dict(id="ARG-131-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-10-11", hora="tarde (solo por resumen)", orig="ARGOS 130", col_orig="rojo",
  ent="Sinaloa", mun="Mazatlán (col. Klein, cancha de futbol)", dia="11-OCT, TARDE",
  title="SINALOA · MAZATLÁN — ASESINAN A DOS JUGADORES DE FUTBOL EN UNA CANCHA DE LA COLONIA KLEIN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 130</code> · <code>COL. KLEIN, CANCHA DE FUTBOL — SOLO POR RESUMEN</code> · tarde del DOMINGO 11-OCT (" + RES + ") · ataque armado contra los jugadores · <b>2 muertos</b>, por titular (🔴 en su ventana) · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>2 muertos</b> en una cancha de futbol", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Informador · El Universal · Posta",
  conf="★★★☆☆", campo="hora y colonia solo por resumen; sin fuente institucional", I=0, N=3, R=3, A=0,
  fechadas=["El Informador (20261011)", "Luz Noticias (2026-10-11)", "El Heraldo de San Luis Potosí (2026/10/11)"],
  desl="ARGOS 130 lo dejó como candidato sin URL con fecha («Mazatlán ×2»); la nota de El Informador lo ancla al 11-oct. La mujer asesinada en Villa Unión el mismo día sigue sin URL con fecha: no se ficha"),
 dict(id="ARG-131-REC-003", estado="MX-MIC", region="Occidente", fecha="2026-10-11", hora="mañana (por titular)", orig="ARGOS 129 o ARGOS 130 — HORA NO FIJADA", col_orig="rojo",
  ent="Michoacán", mun="Morelia (col. Ilustres Novohispanos)", dia="11-OCT, MAÑANA",
  title="MICHOACÁN · MORELIA — ASESINAN A DOS HOMBRES DENTRO DE UNA VIVIENDA EN ILUSTRES NOVOHISPANOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 129 O ARGOS 130 — HORA NO FIJADA</code> · <code>COL. ILUSTRES NOVOHISPANOS, VIVIENDA</code> · mañana del DOMINGO 11-OCT, por titular · hombres armados disparan dentro de la casa · <b>2 muertos</b>, por titular (🔴 en su ventana) · <code>HERIDO CONTRADICHO: «UN HERIDO» (SOLO POR RESUMEN) FRENTE A «NO HUBO TERCER LESIONADO» (POR TITULAR)</code> · FGE Michoacán procesa la escena, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>2 muertos</b> dentro de una vivienda", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora no fijada; sin fuente institucional", I=0, N=0, R=7, A=0,
  fechadas=["Changoonga (2026/10/11)", "Grupo Marmor (2026/10/11)"],
  desl="NO es ARG-130-004 (col. Solidaridad, negocio de micheladas). ARGOS 130 lo descartó por no tener nota localizada; Changoonga y Grupo Marmor lo anclan al 11-oct. Si fue antes de las 08:58, su ventana es la de ARGOS 129"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = []
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [0] * 10, TOT
assert cnt == {"rojo": 3, "amarillo": 1, "verde": 2}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 1, "verde": 0}, cnt_rec
assert len(ENT) == 5, ENT

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else ("sin fila — evento cualitativo, cantidad no determinada" if e.get("cual") else "sin fila — no hubo armamento asegurado"))
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
head = head.replace("<title>ARGOS 130 — Reporte Nacional de Seguridad — 2026-10-12</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. EXIJA A LA FISCALÍA DE MORELOS EL PARTE DEL OPERATIVO DE TOTOLAPAN</b> (ARG-131-002): situación jurídica del detenido liberado,
      identificación de quienes retuvieron a su personal y protocolo de traslado de detenidos de alto valor.
      <br><b>2. REFUERCE LA PROTECCIÓN DE LA COORDINACIÓN DE HOMICIDIOS DE LA FGE PUEBLA</b> (ARG-131-003) y exija el peritaje balístico
      de la camioneta atacada.
      <br><b>3. EXIJA A LA FISCALÍA DE SINALOA LAS CARPETAS DE VALLADO VIEJO Y ESCUINAPA</b> (ARG-131-001, ARG-131-004) y el cotejo de
      casquillos con los homicidios previos de Escuinapa.
      <br><b>4. EXIJA A LA FISCALÍA DE MICHOACÁN EL SALDO OFICIAL Y EL INVENTARIO DE JACONA</b> (ARG-130-001).
      <br><b>5. PIDA A LA SSPC EL BOLETÍN DE ACCIONES DEL 12-OCT</b> y la fecha y lugar de la captura de «El Cabra» (ARG-131-006).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>12-oct 08:19 → 13-oct 07:23 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,26 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>. <b>Los seis</b> llevan <code>FRONTERA DE VENTANA</code>.
    <br><code>LAS {len(R)} RECUPERACIONES DEL FINAL PERTENECEN A VENTANAS ANTERIORES Y QUEDAN FUERA DEL SEMÁFORO, DEL MAPA, DEL RADAR Y DE TODOS LOS TOTALES.</code>
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
    <b>Ningún aseguramiento de armamento con cifra en hechos propios</b>. <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento de armamento</b>; los 6 de ARG-131-005 y el de ARG-131-006, sin armas, no entran. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos por agresión en hechos propios: 5</b> —4 en Culiacán y 1 en Escuinapa—; no incluye los 2 o 4 policías muertos en el accidente vial de ARG-131-002. <b>Heridos: 1</b> por titular (Puebla); 3 en Totolapan, solo por resumen. <b>Cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA ARMA CORTA CON CIFRA EN HECHO PROPIO</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA CON CIFRA EN HECHO PROPIO</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR INTEGRADA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>NINGÚN CARTUCHO CON CIFRA EN HECHO PROPIO</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN CARGADOR CON CIFRA EN HECHO PROPIO</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>Ninguna fila de armamento en la ventana</b>: ningún hecho propio publicó aseguramiento de armas, cartuchos ni explosivos con cifra. <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Gris = sin aseguramiento de armamento con cifra en la ventana. La sola presencia de armas no vuelve roja a una entidad.</div>
  </div>
'''

arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
      <tr><td colspan="16"><code>SIN FILAS — NINGÚN ASEGURAMIENTO DE ARMAMENTO CON CIFRA EN LA VENTANA</code></td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: <b>0 filas</b> en las seis regiones. <b>Eventos cualitativos</b>: ARG-131-003 (armas largas usadas en el ataque, no aseguradas).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: boletín del Gabinete de Seguridad de las acciones del <b>9, 10 y 11-oct</b>, publicado el 12-oct y localizado solo por republicadores (Línea Directa 2026-10-12, Argon México 2026/10/12) —«22 sospechosos y 35 armas en 12 estados», por titular de Excélsior; desglose solo por resumen, no cuadra—, con el cateo de Ciudad Isla, Veracruz (10-oct: 8 armas sin desglose, 41 cargadores, 34 cartuchos, solo por resumen).
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile"><span class="lbl">Sentencias condenatorias</span><span class="num">1</span><span class="sub">FGR · Baja California Sur · <a href="#ARG-131-SEN-001-F">ARG-131-SEN-001</a></span></div>
    <div class="tile"><span class="lbl">Personas sentenciadas</span><span class="num">1</span><span class="sub">procedimiento abreviado</span></div>
    <div class="tile"><span class="lbl">Pena acumulada</span><span class="num">8 años</span><span class="sub">un solo caso; <b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto publicado</b> · decomiso del narcótico, solo por resumen</span></div>
    <div class="tile"><span class="lbl">Fiscalías con resultado</span><span class="num">1</span><span class="sub">FGR · <b>18 estatales revisadas</b>, ninguna integrable · 14 <code>NO REVISADA</code></span></div>
  </div>

  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>ARG-ID</th><th>Fiscalía</th><th>Entidad</th><th>Delito</th><th>Sentenciados</th><th>Pena</th><th>Multa</th><th>Reparación del daño</th><th>Tipo de sentencia</th><th>Firmeza</th><th>Fuente oficial</th><th>Corroboración</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr id="ARG-131-SEN-001"><td><a href="#ARG-131-SEN-001-F"><code>ARG-131-SEN-001</code></a></td><td>FGR · Fiscalía Federal en BCS</td><td>Baja California Sur · La Paz (Pichilingue)</td><td>Contra la salud, transporte de metanfetamina</td><td><b>1</b> · Óscar «N»</td><td><b>8 años</b>, por titular sin fecha</td><td><span class="muted-note">no publicada</span></td><td><span class="muted-note">no publicada</span></td><td>Condenatoria · procedimiento abreviado <span class="muted-note">(solo por resumen)</span></td><td><span class="muted-note">no informada</span></td><td>gabinetedeseguridad.gob.mx <span class="muted-note">(slug indexado, sin fecha)</span></td><td>Tijuana Última Hora (12/10/2026) · Zócalo · Uniradio</td><td><b>Medio</b></td></tr>
    </tbody>
  </table></div>

  <div class="nota" id="ARG-131-SEN-001-F">
    <div class="nota-header"><h3>BAJA CALIFORNIA SUR · LA PAZ — OCHO AÑOS DE PRISIÓN POR TRANSPORTAR MÁS DE UNA TONELADA DE METANFETAMINA</h3><span class="risk-flag bajo">SENTENCIA</span></div>
    <div class="nota-body">
      <div class="apartado"><span class="k">HECHO</span>
        La Paz · <code>RECINTO PORTUARIO DE PICHILINGUE, PUESTO MILITAR DE SEGURIDAD</code> · detención en <b>julio de 2025</b> por Defensa y GN en un tractocamión, {RES} · <b>FGR</b> · <b>sentencia condenatoria</b>, por titular del boletín · contra <b>ÓSCAR «N»</b> · <b>8 años de prisión</b>, por titular sin fecha en la ruta · <b>1,020.80 kg</b> de clorhidrato de metanfetamina y procedimiento abreviado, {RES} · decomiso del narcótico, {RES} · <code>FECHA DE LA SENTENCIA NO PUBLICADA</code>: se integra por su publicación del 12-oct · firmeza no informada · {FR}
      </div>
      <div class="apartado"><span class="k">TRAZABILIDAD</span>
        <code>ARG-131-SEN-001</code> · <b>Confianza</b>: 🟡 Medio, <b>la fija el campo peor sostenido</b>: boletín oficial indexado por su <i>slug</i>, no leído íntegro por el bloqueo de egreso ·
        <b>Fuentes</b>: <b>Institucional 1</b> · <b>Nacional 1</b> · <b>Regional 4</b> · <b>Abierta 0</b> ·
        con fecha en la ruta: <b>Tijuana Última Hora (12/10/2026)</b>
        · <b>Sentencia</b>: no publicada · <b>Publicación</b>: 2026-10-12 · <b>Consulta</b>: {CONSULTA} ·
        <b>Estatus</b>: Confirmado por fuente oficial indexada
        <br><b>Deslindes y reservas</b>: Pichilingue no figura en el índice. Campos individualizadores coincidentes —nombre, peso, lugar y procedimiento—, <b>solo por resumen</b>; la pena, por titular sin fecha (Zócalo); la publicación, por la fecha en la ruta de otro medio. NO es Rafael «N», 7 años 6 meses, 337 litros (Noticias La Paz 2026/10/10, fuera de ventana), ni Amílcar «C», Sonora, 831.51 kg. Excélsior titula «9 años» sobre una transportista: <code>POSIBLE CASO HOMÓNIMO</code>, no se integra. Republicadores del mismo boletín: no independientes
      </div>
    </div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Sonora</b><br>Nogales</td><td>Mateo «N» · <span class="muted-note">tentativa de feminicidio; procedimiento abreviado</span></td><td><b>15 años</b>, por titular</td><td>FGJE Sonora <span class="muted-note">(titular de republicadores)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · publicado el 12-oct (El Diario de Sonora) · dominio de la fiscalía no devuelto</td><td>Bajo</td></tr>
      <tr><td><b>Chihuahua</b></td><td>Lorenzo «N» · <span class="muted-note">posesión de armas y droga</span></td><td><b>7 años</b>, por titular · 1 mes adicional, solo por resumen</td><td><span class="muted-note">no fijada</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el 12-oct (El Diario de Chihuahua)</td><td>Bajo</td></tr>
      <tr><td><b>Zacatecas</b><br>Chalchihuites</td><td>Nayeli «N» y Elizandro «N» · <span class="muted-note">cargadores y cartuchos de uso exclusivo</span></td><td><b>4 años</b>, por titular</td><td>FGR <span class="muted-note">(por medios)</span></td><td><code>FECHA DE PUBLICACIÓN NO ANCLADA: URL 2026/10 SIN DÍA</code> · <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo · Baja California</b><br>Santiago Tulantepec · Ensenada</td><td>Veredictos de culpabilidad · <span class="muted-note">feminicidio y homicidio; homicidio de tres surfistas</span></td><td><code>SIN PENA: INDIVIDUALIZACIÓN EL 14 Y EL 16-OCT</code></td><td>PGJ Hidalgo · FGE BC <span class="muted-note">(por cita)</span></td><td><b>No son sentencia</b> hasta la audiencia de individualización</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Chihuahua, 166 años 8 meses por el ataque a ministeriales de 2023 (10-oct) · Nuevo León, tres personas (10-oct) · Sinaloa, Navolato, 80 años (10-oct) · Colima, 27 años por secuestro (9-oct) · Michoacán, Numarán (11-oct). <code>NO SE INTEGRAN: FUERA DE VENTANA O SIN BOLETÍN OFICIAL.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>18 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · BC, Chih, Dgo · NL, Tamps, SLP · Jal, Ags, Mich · Edomex, Pue · Ver, Tab · Chis, Oax, Gro, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>1</b>: FGR</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>18</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>14</b>: BCS, Son, Sin · Coah, Zac · Col, Nay, Gto · CDMX, Mor, Tlax, Hgo, Qro · Camp</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 30 de 32 por búsqueda dirigida en medios</b> —BCS y Dgo, <code>NO REVISADA</code>— · <b>armamento: 23 de 32</b>; <code>NO REVISADA</code>: BCS, Son, Chih, Sin, Edomex, Tlax, Hgo, Oax, Gro · <code>ARMAMENTO Y SENTENCIAS: REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, Defensa y Marina: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 9, 10 y 11-oct</b>: agregado publicado el 12-oct, <b>solo por republicadores</b> · <b>acciones del 12-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 13-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR TRES ROJOS</b>: ARG-131-001 a ARG-131-003 (Sinaloa, Morelos y Puebla); dos de ellos, contra personal de fiscalías.
      <br><b>2.</b> <b>Contexto operativo</b>: un amarillo en Escuinapa (ARG-131-004).
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-131-005 y ARG-131-006; <b>ningún detenido publicado</b> por los tres rojos; en Totolapan, la detención quedó revertida.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-131-REC-001 a ARG-131-REC-003, de las ventanas de ARGOS 129 y 130, fuera de los totales.
      <br><b>5.</b> <code>23 H 04 MIN; LOS SEIS HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. CAPACIDAD DE COACCIÓN SOBRE LA PROCURACIÓN DE JUSTICIA EN EL CENTRO.</b> ARG-131-002, ARG-131-003: un grupo impuso la liberación de un detenido y otro
      atacó con armas largas a la Coordinación de Homicidios. Línea: <b>trazabilidad de las amenazas previas</b> al personal — hipótesis.
      <br><b>2. ATAQUE A VIVIENDA CON VÍCTIMAS FAMILIARES Y HOMICIDIO DE MUJERES EN EL SUR DE SINALOA.</b> ARG-131-001, ARG-131-004. Línea: <b>cotejo balístico</b>
      y perfil de víctima — patrón por validar.
      <br><b>3. RUTA MARÍTIMA DE COCAÍNA EN EL PACÍFICO SUR, LEJOS DE COSTA.</b> ARG-131-005. Línea: <b>origen y destino de la embarcación</b> y nacionalidad de la
      tripulación — consistente con tránsito sur–norte, no confirmado.
      <br><b>4. LIDERAZGO DE PANDILLA CENTROAMERICANA ASENTADO EN VILLAHERMOSA.</b> ARG-131-006. Línea: <b>red de apoyo local</b> y corredor de ingreso — requiere validación.
      <br><b>5. BRECHA ENTRE DETENCIÓN Y CONDENA.</b> ARG-131-SEN-001: unos quince meses entre la detención y la publicación de la pena, <b>cálculo propio</b>; las sentencias estatales de Sonora y Chihuahua solo
      existen en medios. Línea: <b>exigir el boletín oficial</b> de cada sentencia anunciada.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: CULIACÁN, TOTOLAPAN Y PUEBLA", co1)
 + page("CRIMEN ORGANIZADO (II) — ESCUINAPA, PACÍFICO SUR Y VILLAHERMOSA", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES: VENTANAS DE ARGOS 129 Y 130", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 12-oct 08:19 → 13-oct 07:23 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R))
