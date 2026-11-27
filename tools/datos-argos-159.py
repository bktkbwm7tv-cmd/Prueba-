# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 159.
Uso: python3 tools/datos-argos-159.py <plantilla ARGOS 158> <salida>
Ventana: 26-nov 13:44 → 27-nov 08:03 CDMX (18 h 19 min; jue 26 · vie 27). Archivo: argos-2026-11-27.html.
La hora de «Consulta» se fija al cierre de procedencia-cifras R2 con la variable ARGOS_CONSULTA (HH:MM)."""
import sys, re, json, os, html as H

NUM, FECHA, HORA = "159", "2026-11-27", "08:03"
CONSULTA = "2026-11-27, última búsqueda " + os.environ.get("ARGOS_CONSULTA", "__CONSULTA__")
DUR = "18 h 19 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
PR = " <span class=\"muted-note\">(solo por resumen)</span>"
PT = " <span class=\"muted-note\">(por titular)</span>"
RET = "<code>SI RESULTA ANTERIOR A LAS 13:44 DEL 26, ES DE LA VENTANA DE ARGOS 158 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
QNI = "<code>QUIÉN INICIÓ NO DETERMINADO</code>"
CND = "<code>CANTIDAD NO DETERMINADA</code>"
EAP = "<code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada por autoridad
# (cálculo propio derivado del arreglo, nunca escrito a mano). Agresores abatidos: fuera de mu.
E = [
 # ======================= ROJOS
 dict(id="ARG-159-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-26", hora="~19:15 (solo por resumen)", mu=4, he=0, cu=0, hk=19,
  ent="Sinaloa", mun="Mazatlán (col. Benito Juárez)", dia="JUE 26-NOV, POR RUTA",
  fecha_txt="jueves 26-nov, por ruta; ~19:15, solo por resumen",
  title="SINALOA · MAZATLÁN — ATAQUE ARMADO EN UNA CERRAJERÍA DE LA COLONIA BENITO JUÁREZ: CUATRO HOMBRES MUERTOS",
  hecho="Mazatlán · <code>COL. BENITO JUÁREZ</code>, negocio, por titular (López-Dóriga: «Matan a cuatro personas en un negocio de la colonia Benito Juárez, en Mazatlán»); cerrajería, por titular (Quadratín: «Atentado en cerrajería de Mazatlán deja 4 muertos»); Agustín Melgar y Revolución, " + RES + " · jueves 26-NOV, por ruta (Luz Noticias 2026-11-26); publicación del 27, por ruta (Infobae 2026/11/27: «Violencia no da tregua en Mazatlán: ejecutan a cuatro hombres en una cerrajería en medio de racha de ataques») · ~19:15, " + RES + " · " + AP + " · " + RET + " · <b>4 hombres muertos</b>, por titular (El Piñero: «Cuatro hombres mueren en ataque armado dentro de cerrajería en Mazatlán») (🔴 homicidio múltiple); primer parte de 3, por titular (Sinaloa en Línea: «Ataque armado en Mazatlán deja tres muertos en la Benito Juárez»): <code>SALDO POSTERIOR ACOGIDO</code> · dos en el lugar y dos durante el traslado, " + RES + " · dos hermanos entre las víctimas, por titular (Sinaloahoy: «Ataque a cerrajería en Mazatlán deja cuatro víctimas; identifican a dos hermanos») · FGE, Ejército, Marina y policía en el lugar, " + RES + " · " + NOD,
  panel="<b>4 hombres asesinados</b> en una cerrajería", inst=SB, nac="Infobae · López-Dóriga · Estrella Digital", conf="★★★☆☆",
  campo="hora solo por resumen en el día de apertura; ninguna fuente institucional", I=0, N=3, R=6, A=0,
  fechadas=["Luz Noticias (2026-11-26)", "Infobae (2026/11/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="La cerrajería de la col. Benito Juárez no figura en ARGOS 155 a 158. Los Acantos (ARG-158-007/-014) y los seis detenidos de Mazatlán (ARG-158-015): otros hechos; vínculo no publicado. Racha de homicidios en Mazatlán (Infobae): balance, no se integra. Sinaloahoy «Fiscalía General del Estado investiga cuatro cuerpos sin vida hallados en invasión de Mazatlán»: otro lugar, día no fijado: no se integra. Identidades: no se reproducen."),
 dict(id="ARG-159-002", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-26", hora="noche (solo por resumen)", mu=1, he=2, cu=0, hk=21,
  ent="Michoacán", mun="Zinapécuaro (Los Trigos, entronque de Ucareo)", dia="JUE 26-NOV, POR RESUMEN",
  fecha_txt="noche del jueves 26-nov, solo por resumen; publicación viernes 27-nov, por ruta",
  title="MICHOACÁN · ZINAPÉCUARO — ATACAN CUATRO VEHÍCULOS EN LA CARRETERA MORELIA–MARAVATÍO: UN NIÑO MUERTO Y DOS O TRES HERIDOS",
  hecho="Zinapécuaro · carretera Morelia–Maravatío, por titular (MiMorelia: «Atacan 4 vehículos en la carretera Morelia-Maravatío; hay un niño muerto y tres heridos»); comunidad de Los Trigos, cerca de Ucareo, " + RES + " · publicación viernes 27-NOV, por ruta (Grupo Marmor 2026/11/27: «Ataque armado contra vehículos en Zinapécuaro deja un niño muerto y tres heridos»; Changoonga 2026/11/27) · noche del jueves 26-NOV, " + DSR + " · " + FR + " · " + RET + " · <b>1 niño muerto</b>, por titular (La Voz de Michoacán: «Ataque armado en Zinapécuaro deja un niño muerto y 3 heridos») · heridos contradichos por titular: tres (Grupo Marmor; MiMorelia; La Voz de Michoacán) y dos (Meganoticias: «Un menor muerto y dos personas heridas por ataque en Zinapécuaro»): <code>HERIDOS CONTRADICHOS — SE CUENTAN 2</code> (🔴 ataque armado contra civiles en tránsito; víctimas múltiples) · primer parte de un muerto y un herido, por titular sin fecha (Quadratín: «Un muerto y un herido tras ataque armado en Zinapécuaro») · cuatro vehículos, por titular (MiMorelia) · tronco atravesado sobre la carretera para detener a los conductores, " + RES + " · caso notificado a la FGE, " + RES + " · móvil no informado · " + NOD,
  panel="<b>Ataque a 4 vehículos</b>: niño muerto, 2 o 3 heridos", inst=SB, nac="—", conf="★★★☆☆",
  campo="día y hora solo por resumen; heridos contradichos por titular; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Grupo Marmor (2026/11/27)", "Changoonga (2026/11/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="Zinapécuaro figura por ARG-157-001 (emboscada a militares del domingo 22): otro hecho, otra fecha y otras víctimas; el titular de Quadratín, sin fecha en la ruta, se cita solo como primer parte. Grupo Marmor, PCM, Respuesta y RED113: misma nota, una fuente. «Tres camionetas baleadas y un muerto en el entronque de Ucareo» (Informaoriente, sin fecha): <code>NO ACREDITADO SI ES EL MISMO HECHO</code>. Identidad del menor: no se reproduce."),
 # ======================= VERDES
 dict(id="ARG-159-003", estado="MX-DUR", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-26", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Durango", mun="Tamazula (sierra)", dia="PUBL. JUE 26-NOV, POR RUTA",
  fecha_txt="publicación jueves 26-nov, por ruta; captura del miércoles 25, solo por resumen; hora no fijada",
  title="DURANGO · TAMAZULA — MARINA Y SSPC DETIENEN A CUATRO, ENTRE ELLOS «EL CHAPO FÉLIX», SEÑALADO OPERADOR DE «LOS MAYOS»",
  hecho="Tamazula · sierra de Durango, por ruta (El Financiero 2026/11/26) · publicación jueves 26-NOV, por ruta (El Heraldo de México 2026/11/26; El Financiero 2026/11/26; El Informador 20261126; Línea Directa 2026-11-26: «Cayó el “Chapo Félix”: fuerzas federales detienen a un operador del Cártel de Sinaloa en Durango») · captura del miércoles 25, ~16:00, " + RES + ": " + EAP + " · " + AP + " · <b>4 detenidos</b>, cifra del Gabinete de Seguridad citada por medios, " + RES + " · Marina y SSPC, " + RES + " · entre ellos el señalado operador de «Los Mayos», por titular (El Siglo de Durango: «¿Quién es ‘El Chapo Félix’, presunto operador en célula de ‘Los Mayos’ que fue capturado en Durango?»; El Porvenir: «Capturan al \"Chapo Félix\", operador de Los Mayos») (🟢 detención) · 4 armas largas, 8 cargadores, 260 cartuchos y chalecos balísticos, " + RES + ": " + CND,
  panel="<b>4 detenidos</b>, entre ellos un señalado operador de «Los Mayos»", inst=SB, nac="El Heraldo de México · El Financiero · El Informador", conf="★★★☆☆",
  campo="día de la captura y cifras solo por resumen; Gabinete de Seguridad solo citado por medios", I=0, N=3, R=3, A=0,
  fechadas=["El Heraldo de México (2026/11/26)", "El Financiero (2026/11/26)", "El Informador (20261126)", "Línea Directa (2026-11-26)"], estatus="Parcialmente corroborado", arm=None, cual=True,
  desl="Tamazula figura por ARG-119-010 y ARG-123-REC-008/-009 (septiembre): otros hechos. No figura en ARGOS 158. Portada de gob.mx/sspc: aprehensión en Tamazula listada el 26, " + RES + ". Seis chalecos: un solo medio. Nombres de los detenidos: no se reproducen."),
]

# ---------------------------------------------------------------- RECUPERACIONES (fuera de todos los totales)
R = [
 dict(id="ARG-159-REC-001", estado="MX-CHH", region="Noroeste", fecha="2026-11-25", hora="tarde (solo por resumen)", orig="ARGOS 158", col_orig="rojo", mu=4, he=1, cu=0,
  ent="Chihuahua", mun="Chihuahua (col. Paseos de Camino Real)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; tarde, solo por resumen",
  title="CHIHUAHUA · CHIHUAHUA — ATAQUE ARMADO EN UN YONKE DE LA COLONIA CAMINO REAL: CUATRO MUERTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 158</code> · Chihuahua · yonke, col. Camino Real, por titular (Chihuahua Hoy: «Cuatro muertos tras ataque armado en un yonke de la colonia Camino Real en Chihuahua»); Paseos de Camino Real, " + RES + " · miércoles 25-NOV, por ruta (El Diario de Chihuahua 2026/nov/25: «Ejecutan a tres hombres en yonke; hay un herido») · tarde, " + RES + " · primer parte de <b>3 muertos y 1 herido</b>, por titular con ruta; <b>4 muertos</b>, por titular sin fecha (Chihuahua Hoy; Meridiano 107: «Suman cuatro muertos tras ataque armado en Yonke 48»): <code>SALDO POSTERIOR ACOGIDO</code> (🔴 homicidio múltiple) · un expolicía municipal entre las víctimas, por ruta semántica (El Heraldo de Chihuahua) · agresores en motocicleta, " + RES + " · " + NOD,
  panel="<b>4 muertos</b> en un yonke", inst=SB, nac="Excélsior · N+",
  conf="★★★☆☆", campo="saldo final por titular sin fecha; hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["El Diario de Chihuahua (2026/nov/25)"], estatus="Parcialmente corroborado",
  desl="Rojo sin ruta de ARGOS 158: se recupera con la ruta del 25. Comandante ministerial herido en Ciudad Aldama (Excélsior: «Ejecutan a tres y atacan a comandante en Chihuahua»): día solo por resumen, no se integra a esta ficha. Identidades: no se reproducen."),
 dict(id="ARG-159-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-11-25", hora="noche (solo por resumen)", orig="ARGOS 158", col_orig="rojo", mu=0, he=1, cu=0,
  ent="Sinaloa", mun="Navolato (Yebavito–ejido Sinaloa)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; noche, solo por resumen",
  title="SINALOA · NAVOLATO — HOMBRES ARMADOS AGREDEN A POLICÍAS ESTATALES: UN AGENTE HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 158</code> · Navolato · tramo Yebavito–ejido Sinaloa, " + RES + " · miércoles 25-NOV, por ruta (El Financiero 2026/11/25: «Hombres armados agreden a policías en tierras del “Chapo Isidro”: hay un oficial herido») · noche, " + RES + " · <b>1 policía estatal herido</b>, por titular (🔴 el grupo agrede a policías) · agresión informada por la SSP de Sinaloa, " + RES + " · " + NOD,
  panel="<b>Agresión a policías estatales</b>: 1 herido", inst=SB, nac="El Financiero",
  conf="★★★☆☆", campo="hora y circunstancia (patrullaje) solo por resumen; ninguna fuente institucional", I=0, N=1, R=1, A=0,
  fechadas=["El Financiero (2026/11/25)"], estatus="Parcialmente corroborado",
  desl="Navolato no figura en ARGOS 158; en ARG-156-002 solo como municipio con bloqueos, por resumen: otro hecho. Los Noticieristas (2026/11, sin día): misma agresión. Identidad del agente: no se reproduce."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = []

TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
ND = [True] * 10 if not any(a["integra"] for a in ARM) else [all(i in a.get("nd", []) for a in ARM if a["integra"]) for i in range(10)]
def tv(i, f=str): return "n/d" if ND[i] else f(TOT[i])
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["estado"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
NRET = sum(1 for e in E if "SE RETIRA DE ESTE TOTAL" in e["hecho"])
HORAS = 18 + 19 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
RREG = {g: sum(1 for e in E if e["color"] == "rojo" and e["region"] == g) for g in ("Noroeste", "Noreste", "Occidente", "Centro", "Golfo", "Sureste")}
assert TOT == [0] * 10 and ARMAS == 0, (TOT, ND)
assert cnt == {"rojo": 2, "amarillo": 0, "verde": 1}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU) == (5, 2, 0), (MU, HE, CU)
assert DENS == "0,16" and RPH == "0,11", (DENS, RPH)
assert (NAP, NFR, NRET) == (2, 1, 2), (NAP, NFR, NRET)
assert len(ENT) == 3 and len(ENT_ROJO) == 2, (ENT, ENT_ROJO)
assert RREG == {"Noroeste": 1, "Noreste": 0, "Occidente": 1, "Centro": 0, "Golfo": 0, "Sureste": 0}, RREG
assert sorted(e["id"] for e in E) == [f"ARG-159-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-26" <= x["fecha"] <= "2026-11-27", x["id"]
    assert x["conf"] != "★★★☆☆" or len(x["fechadas"]) + (x["N"] + x["R"]) >= 2, x["id"]
    assert x["conf"] != "★★★★☆" or x["I"] >= 1, x["id"]

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna</span>"
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
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"] + (" · día solo por resumen" if "DÍA SOLO POR RESUMEN" in e.get("fecha_txt", "") else "") + (" · fecha de publicación; día del hecho no fijado" if e.get("dia", "").startswith("PUBL") else "")}

def arm_json(a):
    c = [("n/d" if i in a.get("nd", []) else v) for i, v in enumerate(a["c"])]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if sum(a["c"]) > 30 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 158 — Reporte Nacional de Seguridad — 2026-11-26</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
    <div class="sem-item alto"><span class="dot"></span><span class="lbl">🔴 ROJO — ALTO IMPACTO</span><div class="val">{cnt["rojo"]} evento{"" if cnt["rojo"] == 1 else "s"}</div></div>
    <div class="sem-item medio"><span class="dot"></span><span class="lbl">🟡 AMARILLO — VIOLENCIA OPERATIVA</span><div class="val">{cnt["amarillo"]} evento{"" if cnt["amarillo"] == 1 else "s"}</div></div>
    <div class="sem-item bajo"><span class="dot"></span><span class="lbl">🟢 VERDE — ACCIONES INSTITUCIONALES</span><div class="val">{cnt["verde"]} evento{"" if cnt["verde"] == 1 else "s"}</div></div>
  </div>

  <div class="alerta contexto">
    <div class="flag">LO QUE DEBE HACER EL MANDO</div>
    <p>
      <b>1. SOLICITE A LA FISCALÍA DE SINALOA LA HORA, EL SALDO OFICIAL Y LA LÍNEA DE INVESTIGACIÓN DEL ATAQUE DE LA COLONIA BENITO JUÁREZ, MAZATLÁN</b> (ARG-159-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE MICHOACÁN EL PARTE DEL ATAQUE EN LA CARRETERA MORELIA–MARAVATÍO: HORA, NÚMERO DE LESIONADOS Y VEHÍCULOS AFECTADOS</b> (ARG-159-002).
      <br><b>3. SOLICITE AL GABINETE DE SEGURIDAD EL DÍA DE LA CAPTURA Y EL INVENTARIO DE TAMAZULA, Y COTÉJELOS CON EL BOLETÍN FEDERAL DEL 25</b> (ARG-159-003).
      <br><b>4. SOLICITE A LA FGR Y A LA FISCALÍA DEL ESTADO DE MÉXICO LOS COMUNICADOS ÍNTEGROS DE LAS DOS SENTENCIAS CANDIDATAS DEL 26 PARA SU INTEGRACIÓN AL CONTEO</b> (página de sentencias).
      <br><b>5. COTEJE CON LA FISCALÍA DE CHIHUAHUA Y LA SSP DE SINALOA LOS DOS ATAQUES DEL 25 RECUPERADOS DE LA VENTANA ANTERIOR</b> (ARG-159-REC-001 y -002).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
DIA = {d: sum(1 for e in E if e["fecha"] == d) for d in ("2026-11-26", "2026-11-27")}
assert DIA == {"2026-11-26": 3, "2026-11-27": 0}, DIA
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>26-nov 13:44 → 27-nov 08:03 CDMX</b> (<b>{DUR}</b>) · jue 26 (desde 13:44; 10 h 16) · vie 27 (hasta 08:03; 8 h 03) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b> · por fecha asignada: jue 26 <b>{DIA["2026-11-26"]}</b> · vie 27 <b>{DIA["2026-11-27"]}</b>; duración, densidad y reparto, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto</b> (ventana de ARGOS 158), atenuadas, <b>fuera de todos los totales</b>
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
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Muertos por agresión</th><th>Heridos</th><th>Cuerpos o restos hallados</th><th>Armas cortas</th><th>Armas largas</th><th>Armas sin categoría</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos en aseguramiento</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b></td><td><b>{tv(0)}</b></td><td><b>{tv(1)}</b></td><td><b>{tv(2)}</b></td><td><b>{tv(4, fmt)}</b></td><td><b>{tv(5)}</b></td><td><b>{tv(6)}</b></td><td><b>{tv(7)}</b></td><td><b>{tv(8)}</b></td><td><b>{tv(9)}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: ningún aseguramiento de la ventana con cantidad por titular o por autoridad: n/d · <b>muertos por agresión</b>: {MU}, cálculo propio · <b>heridos</b>: {HE}, cálculo propio (Zinapécuaro: se cuentan 2 de 2 o 3) · <b>cuerpos o restos</b>: {CU} · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>{NRET} cláusulas de retiro</b> (detalle en cada ficha).
    <br><code>BALANCES, NO SE INTEGRAN</code>: racha de homicidios en Mazatlán (Infobae 2026/11/27) · resumen semanal del Grupo Interinstitucional de Sinaloa, 16 al 22-nov (tusbuenasnoticias 2026/11/26).
    <br><b>Vistos, fuera de totales</b>: Poza Rica, Ver., taxista asesinado, «noche de este jueves 26» solo en el texto, ruta sin fecha, fuente única (XEU) · Atotonilco de Tula, Hgo., un muerto y una mujer herida en la carretera Tula–Jorobas, noche del 25 {RES}, ventana de 158 (La Silla Rota 2026/11/26) · Hermosillo, vocalista de un grupo musical herido, noche del 25 {RES}, ventana de 158 (El Imparcial 2026/11/26) · Temixco, Mor., ventana de 158 · Ciudad Aldama, Chih., comandante ministerial herido, día {RES} · Reynosa, estación Anzaldúas, restos óseos, y Viesca, Coah., dos fosas en el ejido Salitrillo: lunes 23 {RES}, ventana de 158 · Chilpancingo–Chichihualco, Gro., hombre decapitado: único titular con día en forma de cobertura «hoy lunes 23», no fija el día · Nacajuca y Macuspana, Tab., y Ulumal, Camp.: sin día por ruta o titular · Querétaro, nueve cateos y tres detenidos (Código Qro 2026/11/26): operación del 23 {RES}.
    <br><code>FE DE ERRATAS — ARGOS 158</code>: los vistos «San Fernando, Marina, un muerto y 10-11 detenidos» y «Reynosa, Valle Soleado, dos policías muertos» eran de <b>marzo de 2025</b> y del <b>5-may-2026</b>: se retiran · <b>Ahome (ARG-158-008)</b>: segunda fuente con ruta del 23 (Proyecto Puente 2026/11/23; Línea Directa 2026-11-23): deja de ser fuente única y el día queda fijado por ruta · <b>Chietla (ARG-158-REC-002)</b>: hecho distinto del de ARG-148-002 (otro lugar y otra fecha): reserva levantada · <b>dos rojos de la ventana de 158 se recuperan</b> (yonke de Chihuahua y Navolato) · <b>efecto</b> (cálculo propio): <b>ARGOS 158</b>: 21 hechos · 9 🔴 · 4 🟡 · 8 🟢 · 20 muertos por agresión · 8 heridos · 1 cuerpo · 13 entidades.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Peribán–Jilotlán (ARG-158-002/-013)</b>: 8 detenidos y 20 armas, por titular (Metapolítica y Esfera 2026/11/26: «Detienen Guardia Civil y Defensa a 8 personas y aseguran 20 armas de fuego en límites de Michoacán y Jalisco»), y 3 detenidos más con 10 armas {RES} (tusbuenasnoticias 2026/11/26): <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · <b>Cerro del Cuatro (ARG-158-004)</b>: nuevo lote óseo el jueves 26, hora no fijada {RES} (Guardia Nocturna 2026/11) · <b>Atzitzintla (ARG-158-018)</b>: detención del miércoles 25 {RES} (Milenio): día contradicho; sin vinculación publicada · <b>Ometepec (ARG-155-010)</b>: vinculado a proceso por el homicidio de un dirigente amuzgo, por titular (La Razón 2026/11/23) · <b>Cancún (ARG-155-012)</b>: 2 detenidos por el triple homicidio, por titular (Red Metropolitana 2026/11/24); los 6 son el total del operativo del 18 · <b>Juchitán (ARG-156-015/-016)</b>: nueve capturas de la célula, boletín 3004 de la FGEO {RES}; sin vinculación · <b>Tepexco (ARG-157-002)</b>: «tres muertos y dos heridos», por titular (Retodiario 2026/11/22) · <b>Texhuacán</b>: sin orden por homicidio publicada · <b>Monterrey (ARG-158-006)</b>: «solo dos heridos», FGJNL {RES}.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-159-{i:03d}"]) for i in (1, 2, 3))
co6 = "\n".join(ficha(rbyid[f"ARG-159-REC-{i:03d}"], True) for i in (1, 2))
assert sorted(re.findall(r'id="(ARG-159-0\d\d)"', co1)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-159-REC-\d\d\d)"', co6)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN RESULTADO INDEXADO EN VENTANA</code>"
NDR = "solo por resumen: <b>cantidad no determinada</b>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "ver ARG-159-003: " + NDR),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "ver ARG-159-003: " + NDR),
 tile(4, "Cargadores", tv(5), "ver ARG-159-003: " + NDR),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "sin aseguramiento integrable"),
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
    <div class="map-caption">Pase el cursor sobre un estado.</div>
  </div>
'''
def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'


armrows = "\n".join(armrow(a) for a in ARM) or '      <tr style="opacity:.72;"><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> (20 entidades por dominio; 12 <code>NO REVISADA</code>) · ningún aseguramiento de la ventana con día fijado y cantidad publicada por titular o por autoridad</td></tr>'

arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
{armrows}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: ningún arma integrada en ninguna región. <b>Cálculo propio</b>.
    <br><b>BOLETÍN FEDERAL</b>: __FED17__ · <b>corroboración débil por construcción</b>; <b>un agregado no fija el día ni la hora de cada acción</b>.
    <br><code>NO INTEGRADOS</code>: <b>ARG-159-003 Tamazula</b>: 4 armas largas, 8 cargadores y 260 cartuchos {RES}; captura del 25 {RES} · <b>Peribán–Jilotlán, 26-nov</b>: 8 detenidos y 20 armas por titular; 3 detenidos y 10 armas {RES}: posible duplicidad con ARG-158-013 · <b>Ajijic (ARG-158-016)</b>: sigue sin titular con cifras · Sinaloa, resumen semanal 16 al 22-nov: agregado, no fija hechos.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">ningún boletín de la ventana leído</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub">ver indicador de cobertura</span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Federal</b><br>cumplimiento en Puente Grande, Jal. {RES}</td><td>Delincuencia organizada y secuestro de tres personas; comunicado FGR 846/26 del 26-nov, por título republicado (Curul: «Obtiene FGR sentencia condenatoria de más de 177 años de prisión por delincuencia organizada y secuestro de tres personas»; Infobae y Argonmexico 2026/11/26)</td><td>Más de 177 años, por titular; penas por persona contradichas entre medios</td><td>FGR</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · comunicado no leído (egreso bloqueado) · penas individuales y número de sentenciados {RES} · {AP}: hora no fijada · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Estado de México</b><br>Jiquipilco (distrito de Ixtlahuaca)</td><td>Homicidio de cinco personas (hecho de 2018 {RES}); dos sentenciados (El Imparcial, El Monitor del Estado de México y Reporteros en Movimiento 2026/11/26)</td><td>181 años y 3 meses a cada uno, {RES}; «181 años», por titular</td><td>Juez del distrito de Ixtlahuaca; FGJEM {RES}</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín de la FGJEM · {AP}</td><td>Bajo</td></tr>
      <tr><td><b>Tamaulipas</b></td><td>Boletín FGJE-476-2026, listado en la portada de la fiscalía {RES}</td><td>«sentencia condenatoria de 125…», fragmento truncado</td><td>FGJE Tamaulipas</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin URL propia; delito, sentenciados y fecha {RES}</td><td>No confirmado</td></tr>
      <tr><td><b>Campeche</b></td><td>Abuso sexual de una menor (PorEsto 2026/11/26)</td><td>39 años, {RES}</td><td>FGE Campeche {RES}</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín; dominio de la fiscalía no localizado · sentencia del 25 {RES}</td><td>Bajo</td></tr>
      <tr><td><b>Chihuahua</b></td><td>Homicidio; un sentenciado (La Opción 20261125)</td><td>16 años y 8 meses, por titular</td><td>FGE {RES}</td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · página de la FGE sin fecha (Ciudad Juárez) · sin dos campos individualizadores</td><td>Bajo</td></tr>
      <tr><td colspan="6"><b>Fuera de ventana</b>: FGR Hopelchén, DPE/5332/2026 (24-nov, ventana de 158) · FGEO 3012, agregado de 14 sentencias (25-nov {RES}) · Querétaro, adolescente sentenciado por el ataque de Corregidora (Código Qro 2026/11/25). <b>Retirado de candidatos</b>: Iguala, caso Los Avispones (quinta edición sin comunicado oficial; apelado).</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida a <code>fgr.org.mx</code> (listados nacional y estatal; contenido {RES}); comunicado 846/26 del 26-nov localizado por título</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>24 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · Chih, Sin, Dgo · Coah, Tamps, SLP, Zac · Jal, Mich, Col, Nay, Ags, Gto · Edomex, Mor, Tlax, Hgo, Qro · Ver, Tab · Gro, Oax, Chis, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> por dominio estatal leído</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>23</b> fiscalías estatales · Tamaulipas: boletín FGJE-476-2026 {RES}, sin URL propia</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>8</b>: BC, BCS, Son · NL (dominio sin páginas en la consulta) · CDMX, Pue · Camp (dominio no localizado) · Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 27-nov 08:03: código <code>000</code> · sin páginas: <code>fiscalia.sonora.gob.mx</code>, dominio de la FGE de Campeche</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 16 entidades; solo consulta amplia en 16 —BC, BCS, Dgo · Coah, SLP, Zac · Gto, Nay · CDMX, Edomex, Mor, Pue, Tlax, Hgo · Chis, Yuc— · <b>armamento: 20 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (12): BC, BCS, Son, Sin, Dgo · Jal, Col, Nay, Ags, Gto · Pue · Gro</td></tr>
      <tr><td><b>Boletín federal</b></td><td>__FED17C__ · Defensa: SRIV en <code>gob.mx/defensa</code> (último indexado, 14-nov) · Guardia Nacional: último indexado, 24-nov · Semar: comunicados locales de noviembre (Recinto Portuario de Veracruz, 27-nov, {RES})</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · <code>BLOQUEO DE EGRESO REVERIFICADO EL 27-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Alto impacto</b>: {cnt["rojo"]} eventos en {len(ENT_ROJO)} entidades —un homicidio múltiple y un ataque armado contra civiles en carretera con un menor muerto—; {RPH} rojos por hora (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Noroeste {RREG["Noroeste"]} · Occidente {RREG["Occidente"]} · Noreste, Centro, Golfo y Sureste 0 (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: {cnt["amarillo"]} eventos fijados en la ventana.
      <br><b>4.</b> <b>Respuesta institucional</b>: {cnt["verde"]} acción —captura de un señalado operador regional con armamento sin cifra citable—; ninguna sentencia integrable.
      <br><b>5.</b> <code>TOTALES NO COMPARABLES SIN MÁS CON LOS DE OTRAS EDICIONES: VENTANA DE 18 H 19 MIN FRENTE A 77 H 09 MIN DE ARGOS 158; LOS TRES HECHOS CON HORA SOLO POR RESUMEN O SIN HORA. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. DOS ATAQUES CON VÍCTIMAS MÚLTIPLES EN MAZATLÁN EN DÍAS CONSECUTIVOS</b> (ARG-158-007 y ARG-159-001): Los Acantos el 25 y la colonia Benito Juárez el 26, ambos al anochecer {RES}; vínculo no acreditado. Línea: <b>solicitar el cotejo balístico de los casquillos de ambos ataques</b>.
      <br><b>2. CIERRE DE CARRETERA CON UN OBSTÁCULO PARA DETENER Y ATACAR VEHÍCULOS</b> (ARG-159-002): tronco atravesado en la Morelia–Maravatío {RES}, cinco días después de la emboscada a militares en el mismo municipio (ARG-157-001); vínculo no acreditado. Línea: <b>establecer si el tramo Ucareo–Los Trigos opera como punto de control de un grupo armado</b>.
      <br><b>3. CAPTURA DE UN SEÑALADO OPERADOR DE «LOS MAYOS» EN LA SIERRA DE DURANGO</b> (ARG-159-003): corredor serrano Tamazula–Sinaloa; vínculo con la violencia de Mazatlán no acreditado. Línea: <b>vigilar reacomodos y represalias en la sierra de Tamazula y el sur de Sinaloa</b>.
      <br><b>4. AGRESIONES A PERSONAL DE SEGURIDAD ACTIVO Y RETIRADO EN EL NORTE</b> (ARG-159-REC-001 y -002): un expolicía entre las víctimas del yonke de Chihuahua y policías estatales agredidos en Navolato, ambos el 25; vínculo no acreditado. Línea: <b>revisar amenazas previas contra policías en activo y en retiro en Chihuahua y Navolato</b>.
      <br><b>5. SENTENCIAS DE LARGA PENA SIN COMUNICADO LEÍDO</b> (página de sentencias): secuestro, en el fuero federal, y homicidio múltiple de 2018 en Jiquipilco, con unos ocho años de proceso {RES}. Línea: <b>medir el tiempo entre hecho y condena en los casos de alto impacto del Estado de México</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

FED17 = os.environ.get("ARGOS_FED17", "acciones del 23-nov: <b>indexado en <code>gob.mx/sspc</code></b> por título · acciones del 24 y del 25-nov: republicadores (Milenio; Tallapolítica; Argonmexico 2026/11/26) · acciones del 26-nov: <code>SIN RESULTADO INDEXADO EN VENTANA</code> por día, por agregado y por título; la portada de <code>gob.mx/sspc</code> lista el 26 la aprehensión en Tamazula y la del alcalde de Atzitzintla, " + RES + " · acciones del 27-nov: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · contenido <code>SOLO POR RESUMEN</code>")
arm2 = arm2.replace("__FED17__", FED17)
sent = sent.replace("__FED17C__", FED17)

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — HOMICIDIO MÚLTIPLE EN MAZATLÁN; ATAQUE CONTRA VEHÍCULOS EN ZINAPÉCUARO; CAPTURA EN TAMAZULA", co1)
 + page("CRIMEN ORGANIZADO (II) — RECUPERACIONES DE LA VENTANA DE ARGOS 158: YONKE DE CHIHUAHUA Y NAVOLATO", co6)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1 + arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if a["integra"] and any(a["c"]))
if os.environ.get("ARGOS_BORRADOR") != "1":
    assert "__" not in CONSULTA, "escribir la hora real de la última búsqueda (ARGOS_CONSULTA)"
    assert "__" not in body, "marcador sin sustituir (ARGOS_FED17)"
script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
assert f'const CONSULTA_TXT = "{CONSULTA}";' in script
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert script.count("const EVENTOS_ARM = [\n" + ea + "\n];") == 1
# la ventana de 159 toca dos fechas de calendario (26 y 27-nov); la plantilla de 158 trae 4
assert script.count("WINDOW_DAYS = 4;") == 1, "plantilla de 158 con WINDOW_DAYS = 4"
script = script.replace("WINDOW_DAYS = 4;", "WINDOW_DAYS = 2;")
assert script.count("WINDOW_DAYS = 2;") == 1 and "WINDOW_DAYS = 4;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
