# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 136: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-135.py <plantilla ARGOS 135> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "136", "2026-10-18", "08:34"
CONSULTA = "2026-10-18 08:34-09:45"
DUR = "23 h 06 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA: PUEDE SER ANTERIOR A LAS 09:28 DEL 17</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-136-001", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-17", hora="~17:30 (solo por resumen)",
  ent="Guanajuato", mun="Salamanca (col. Guanajuato)", dia="17-OCT, TARDE",
  title="GUANAJUATO · SALAMANCA — ASESINAN A BALAZOS A DOS HOMBRES EN LA COLONIA GUANAJUATO",
  hecho="Salamanca · <code>COL. GUANAJUATO, POR TITULAR; CALLE DOLORES HIDALGO CASI ESQUINA COMONFORT, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, por ruta de publicación · ~17:30, " + RES + " · varios hombres armados disparan y huyen, " + RES + " · <b>2 hombres muertos</b> a balazos, por titular (🔴) · uno muere en el sitio pese a la atención de paramédicos, " + RES + " · Agencia de Investigación Criminal de la FGE Guanajuato en la escena, " + RES + " · <b>ningún detenido publicado</b> · armamento no publicado · identidades: no publicadas",
  panel="Ataque armado: <b>2 hombres muertos</b>",
  inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["AM (2026/10/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="La colonia Guanajuato no figura en las cinco ediciones previas ni en el índice. NO es ARG-133-002 (bulevar Valle de Santiago, 14-oct) ni ARG-136-REC-001 (Silao)."),
 dict(id="ARG-136-002", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-17", hora="~17:30 o ~18:00 (solo por resumen; versiones distintas)",
  ent="Guerrero", mun="Acapulco (col. Cuauhtémoc, parte alta)", dia="17-OCT, TARDE, DÍA SOLO POR RESUMEN",
  title="GUERRERO · ACAPULCO — DESDE UN TAXI DISPARAN CONTRA UN NEGOCIO DE COMIDA EN LA COLONIA CUAUHTÉMOC: DOS MUERTOS Y TRES HERIDOS",
  hecho="Acapulco · <code>COL. CUAUHTÉMOC, POR TITULAR; PARTE ALTA, CALLE 10 CERCA DE VICENTE GUERRERO, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · ~17:30 o ~18:00, " + RES + ", versiones distintas · hombres a bordo de un taxi disparan al menos 20 veces contra personas en un negocio de comida, " + RES + " · <b>2 hombres muertos</b> —uno en el lugar y otro durante el traslado— y <b>3 heridos</b>, por titular (🔴) · <code>4 HERIDOS EN EL CUERPO DE UNA NOTA: CONTRADICHO</code> · FGE Guerrero, Semefo, Policía Estatal y Guardia Nacional en la escena, " + RES + " · los agresores huyen · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos y 3 heridos</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con fecha", I=0, N=0, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="La colonia Cuauhtémoc de Acapulco no figura en las cinco ediciones previas. <code>NO ES</code> el ataque homónimo en la misma colonia con 3 muertos y 2 heridos (noviembre de 2025, solo por resumen)."),
 dict(id="ARG-136-003", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-17", hora="minutos antes de la medianoche del sábado (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (col. Estela Ortiz)", dia="17-OCT, NOCHE · PUB. 18-OCT",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS A UN JOVEN DENTRO DE UNA TIENDA DE CONVENIENCIA EN LA COLONIA ESTELA ORTIZ",
  hecho="Culiacán · <code>COL. ESTELA ORTIZ (ESTHELA ORTIZ, SEGÚN OTRO MEDIO), POR TITULAR</code> · noche del SÁBADO 17-OCT, minutos antes de la medianoche, " + RES + "; «madrugada de este domingo», " + RES + "; publicado el DOMINGO 18-OCT, por ruta · <b>1 hombre muerto</b> a balazos dentro de una tienda de conveniencia, por titular (🟡) · dependiente de la tienda, por titular de Noroeste; 20 años, por titular de Café Negro · agentes ministeriales en la escena, " + RES + " · asalto o ataque directo: no determinado, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 joven asesinado</b> dentro de una tienda",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-10-18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Estela Ortiz no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-136-004", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="madrugada del domingo (solo por resumen)",
  ent="Veracruz", mun="Xalapa (col. El Moral)", dia="18-OCT, MADRUGADA, DÍA SOLO POR RESUMEN",
  title="VERACRUZ · XALAPA — ASESINAN A BALAZOS A UN HOMBRE EN LA VÍA PÚBLICA",
  hecho="Xalapa · <code>COL. EL MORAL, SOLO POR RESUMEN</code> · madrugada del DOMINGO 18-OCT, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · <b>1 hombre muerto</b> a balazos en plena vía pública, por titular (🟡) · sin signos vitales a la llegada de los paramédicos, " + RES + " · FGE Veracruz en la escena, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada · " + FR,
  panel="<b>1 hombre asesinado</b> en la vía pública",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; día, hora y colonia solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="El Moral no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-136-005", estado="MX-MOR", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-17", hora="tarde del sábado (solo por resumen)",
  ent="Morelos", mun="Temixco", dia="17-OCT, TARDE, DÍA SOLO POR RESUMEN",
  title="MORELOS · TEMIXCO — HALLAN EL CUERPO DE UN HOMBRE EN LA CAJUELA DE UN AUTO TRAS UN ATAQUE ARMADO",
  hecho="Temixco · SÁBADO 17-OCT por la tarde, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · <b>1 hombre muerto</b>, por titular (🟡) · cuerpo hallado en la cajuela de un automóvil tras un ataque, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada",
  panel="<b>1 hombre asesinado</b>; cuerpo en una cajuela",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; día y circunstancias solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Temixco no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-136-006", estado="MX-CHH", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-17", hora="«esta mañana» del sábado (solo por resumen)",
  ent="Chihuahua", mun="Chihuahua", dia="17-OCT, MAÑANA, HORA NO FIJADA",
  title="CHIHUAHUA · CHIHUAHUA — DETIENEN AL EXFISCAL GENERAL DEL ESTADO POR EL OPERATIVO DE ABRIL CON PARTICIPACIÓN DE AGENTES DE LA CIA",
  hecho="Chihuahua capital · <code>AV. CANTERA, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, por ruta · «esta mañana», " + RES + " · <b>1 detenido</b>: el <b>exfiscal general del estado</b>, por titular (🟢) · orden de aprehensión de un juez de control por <b>ejercicio ilegal del servicio público y coalición</b>, según el fiscal general del estado, por cita · causa penal 3055/2026 y orden del 16-oct, " + RES + " · ministeriales y policías estatales, " + RES + " · investigación por el operativo de abril en El Pinal con participación de agentes de la CIA, por titular · la FGR le atribuye posible <b>traición a la patria</b>, por titular de Expansión · orden también contra un exfiscal especial, " + RES + " · acusación, no condena · " + AP,
  panel="<b>Exfiscal general del estado detenido</b>",
  inst="Fiscalía de Chihuahua <span class=\"muted-note\">(por cita)</span>", nac="El Financiero · La Jornada · CNN en Español · Expansión · Reforma · Excélsior · El Universal", conf="★★★☆☆",
  campo="hora de la detención no fijada; declaración de la Fiscalía solo por cita", I=1, N=7, R=2, A=0,
  fechadas=["El Financiero (2026/10/17)", "La Jornada (2026/10/17)", "CNN en Español (2026/10/17)", "Expansión (2026/10/17)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="2026-10-17, hora no fijada",
  desl="Hecho de origen de abril de 2026, fuera de las cinco ediciones previas. Sin armamento"),
 dict(id="ARG-136-007", estado="MX-PUE", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-17", hora="detención no fechada; publicada el 2026-10-17",
  ent="Puebla", mun="Puebla (San Pedro Zacachimalpa)", dia="PUB. 17-OCT, HORA NO FIJADA",
  title="PUEBLA · PUEBLA — DETIENEN A DOS HOMBRES POR EL ATAQUE EN SAN BALTAZAR TETELA EN EL QUE MURIÓ UN NIÑO",
  hecho="Puebla capital · <code>SAN PEDRO ZACACHIMALPA, CALLE HERMANOS SERDÁN, SOLO POR RESUMEN</code> · publicado el SÁBADO 17-OCT, por ruta · <b>2 detenidos</b>, por titular (🟢) · de 18 y 22 años, " + RES + " · Policía Estatal (SSC Puebla), " + RES + "; policía municipal, según otro medio: <code>CONTRADICHO</code> · señalados por el ataque de <a href=\"#ARG-136-REC-002\"><code>ARG-136-REC-002</code></a> · en videovigilancia, uno entrega un arma a un tercero, " + RES + " · armamento asegurado: no publicado · móvil: no aclarado, " + RES + " · identidades: no se reproducen · " + AP,
  panel="<b>2 detenidos</b> por el ataque de San Baltazar Tetela",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="hora de la detención no fijada; corporación contradicha; sin fuente institucional", I=0, N=0, R=7, A=0,
  fechadas=["Paralelo19 (2026/10/17)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicada el 2026-10-17",
  desl="San Pedro Zacachimalpa no figura en las cinco ediciones previas ni en el índice. El ataque es ARG-136-REC-002: un hecho y su detención, dos fichas. Sin armamento con cifra"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-136-REC-001", estado="MX-GUA", region="Occidente", fecha="2026-10-17", hora="~06:30 (aviso al 911) o ~07:20 (solo por resumen; versiones distintas)", orig="ARGOS 135 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="Guanajuato", mun="Silao (Baños de Agua Caliente)", dia="17-OCT, MAÑANA",
  title="GUANAJUATO · SILAO — ASESINAN A UN HOMBRE Y A UNA MUJER DENTRO DE UNA VIVIENDA EN BAÑOS DE AGUA CALIENTE",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 135 — HORA SOLO POR RESUMEN</code> · <code>COMUNIDAD BAÑOS DE AGUA CALIENTE, POR TITULAR; CALLE LA LUZ, CERCA DE COMANJILLA, SOLO POR RESUMEN</code> · mañana del SÁBADO 17-OCT, " + RES + "; publicado el 17-OCT, por ruta · ~06:30 (aviso al 911) o ~07:20, " + RES + ", versiones distintas · <b>1 hombre y 1 mujer muertos</b> a balazos dentro de una vivienda, por titular (🔴 en su ventana) · el agresor huye en un vehículo, " + RES + " · Unidad de Homicidios de la FGE Guanajuato a cargo, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Hombre y mujer asesinados</b> en su vivienda", inst=SB, nac="Milenio",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["AM (2026/10/17)"],
  desl="Baños de Agua Caliente y Comanjilla no figuran en las cinco ediciones previas ni en el índice. NO es ARG-134-001 (Barrio Nuevo)."),
 dict(id="ARG-136-REC-002", estado="MX-PUE", region="Centro", fecha="2026-10-17", hora="madrugada del sábado (solo por resumen); «noche del viernes» en otra versión", orig="ARGOS 135 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="Puebla", mun="Puebla (junta auxiliar San Baltazar Tetela)", dia="17-OCT, MADRUGADA",
  title="PUEBLA · PUEBLA — ATACAN A BALAZOS A UN HOMBRE QUE LLEVABA A SU HIJO EN BRAZOS EN SAN BALTAZAR TETELA: MUERE EL NIÑO DE DOS AÑOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 135 — HORA SOLO POR RESUMEN</code> · <code>JUNTA AUXILIAR SAN BALTAZAR TETELA, POR TITULAR</code> · madrugada del SÁBADO 17-OCT, " + RES + "; «noche del viernes», según otra versión, " + RES + "; publicado el 17-OCT, por ruta · dos hombres en motocicleta disparan contra un hombre que llevaba a su hijo en brazos, " + RES + " · <b>1 niño de 2 años muerto</b> en el Hospital General del Sur, por titular · <b>1 herido</b>, el padre, por titular (🔴 en su ventana) · edad del niño: 2 años 8 meses o 2 años 10 meses, " + RES + ", <code>CONTRADICHO</code> · móvil no aclarado · detenidos: ver <a href=\"#ARG-136-007\"><code>ARG-136-007</code></a> · identidades: no se reproducen",
  panel="<b>Niño de 2 años muerto</b>; su padre, herido", inst=SB, nac=NIN,
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=7, A=0,
  fechadas=["Paralelo19 (2026/10/17)"],
  desl="San Baltazar Tetela no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-136-REC-003", estado="MX-SLP", region="Noreste", fecha="2026-10-15", hora="noche del jueves (solo por resumen)", orig="ARGOS 134 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="San Luis Potosí", mun="Tanquián de Escobedo (centro)", dia="15-OCT, NOCHE",
  title="SAN LUIS POTOSÍ · TANQUIÁN DE ESCOBEDO — ASESINAN CON ARMAS LARGAS A UN ELEMENTO DE LA GUARDIA NACIONAL EN EL CENTRO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 134 — HORA SOLO POR RESUMEN</code> · <code>CENTRO, CALLE VICENTE GUERRERO, SOLO POR RESUMEN</code> · noche del JUEVES 15-OCT, " + RES + "; publicado el 16-OCT, por ruta · <b>1 hombre muerto</b> a balazos, <b>elemento de la Guardia Nacional</b>, por titulares (🔴 en su ventana) · <code>ADSCRIPCIÓN CONTRADICHA: GUARDIA NACIONAL EN DÍAS DE DESCANSO O EXAGENTE DE LA GUARDIA CIVIL ESTATAL, SOLO POR RESUMEN; «INVESTIGAN SI PERTENECÍA», POR TITULAR DE LA OPINIÓN</code> · circulaba en motocicleta; agresores con armas largas, por titular de Pulso · originario de Tempoal, Veracruz, por titular · FGE San Luis Potosí a cargo, " + RES + " · <b>ningún detenido publicado</b>, " + RES + " · identidad: no se reproduce",
  panel="<b>Elemento de la Guardia Nacional asesinado</b>", inst=SB, nac="N+ · Milenio",
  conf="★★☆☆☆", campo="adscripción de la víctima contradicha; hora solo por resumen", I=0, N=2, R=7, A=0,
  fechadas=["Potosinoticias (2026/10/16)"],
  desl="Tanquián no figura en las cinco ediciones previas ni en el índice."),
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
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], TOT
assert cnt == {"rojo": 2, "amarillo": 3, "verde": 2}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert len(ENT) == 7, ENT
assert NFR == 2, NFR

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (e["armtxt"] if e.get("armtxt") else f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else ("sin fila — evento cualitativo, cantidad no determinada" if e.get("cual") else "sin fila — no hubo armamento asegurado"))
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
head = head.replace("<title>ARGOS 135 — Reporte Nacional de Seguridad — 2026-10-17</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE GUANAJUATO LA IDENTIFICACIÓN DE LAS VÍCTIMAS Y LA HORA DEL ATAQUE</b> (ARG-136-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE GUERRERO EL NÚMERO OFICIAL DE LESIONADOS Y EL DÍA DEL ATAQUE</b> (ARG-136-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE PUEBLA LA SITUACIÓN JURÍDICA DE LOS DETENIDOS Y LA CORPORACIÓN QUE LOS DETUVO</b> (ARG-136-007).
      <br><b>4. SOLICITE A LA FISCALÍA DE CHIHUAHUA LA HORA DE LA DETENCIÓN Y LA FECHA DE LA AUDIENCIA INICIAL</b> (ARG-136-006).
      <br><b>5. SOLICITE A LA FISCALÍA DE SAN LUIS POTOSÍ LA ADSCRIPCIÓN DE LA VÍCTIMA</b> (ARG-136-REC-003).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>17-oct 09:28 → 18-oct 08:34 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,30 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>.
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
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> · ningún aseguramiento con cantidad publicada y fecha dentro de la ventana.
    <b>Muertos en hechos propios</b>: <b>7</b> —Salamanca 2, Acapulco 2, Culiacán 1, Xalapa 1 y Temixco 1—. <b>Heridos: 3</b> en ARG-136-002, por titular (<b>4</b> en el cuerpo de una nota: contradicho). <b>Detenidos sin aseguramiento</b>: <b>3</b> (ARG-136-006 y ARG-136-007). <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-135-REC-004, <b>7 osamentas en 5 fosas</b> en dos jornadas, por titular (El Imparcial 2026/10/17) · ARG-135-REC-003, «6 cuerpos y osamentas» en un medio (Punto Norte 2026/10/17), contradicho con 4 · ARG-135-010, la séptima persona sigue sin localizarse (Infobae 2026/10/18) · ARG-135-011, el policía está imputado y la audiencia de vinculación sigue pendiente (Meridiano 2026/10/17) · ARG-134-REC-002, el ataque fue el 14-oct, por ruta (El Sol del Soconusco 2026/10/14); hora no fijada.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:2])
co2 = "\n".join(ficha(e) for e in E[2:5])
co3 = "\n".join(ficha(e) for e in E[5:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
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
{chr(10).join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> — ningún aseguramiento con cantidad publicada y fecha del hecho o de publicación dentro de la ventana</td></tr>'}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: sin lectura (ninguna fila integrada).
    <br><code>VISTOS, NO INTEGRADOS</code>: Sinaloa, SSP, col. Industrial Bravo, Culiacán: 4 detenidos y 1 ametralladora 7.62, fecha no fijada — <code>POSIBLE DUPLICIDAD CON ARG-135-ARM-001 — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · Puebla, Chignahuapan, seis cateos con Marina y Defensa, sin fecha fijada (Excélsior, ruta sin fecha) · Sinaloa, SSP, ejido Canán, 1 fusil, publicado el 16-oct, solo por resumen.
    <br><b>ARG-135-ARM-001 y ARG-135-ARM-002</b> siguen fuera del total de su edición: el primero por la posible duplicidad de arriba; el segundo, con cifra solo por resumen.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">la candidata, abajo, no se integra</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>17 estatales revisadas</b> · 15 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Tres sentenciados, nombres no reproducidos · <span class="muted-note">homicidio calificado de tres surfistas (abril de 2024), robo calificado con violencia y robo de vehículo con violencia, solo por resumen</span></td><td><b>158 años 9 meses</b> a cada uno: 135 años + 10 años 9 meses + 13 años, solo por resumen · reparación: 1,628,550 pesos y 19,542 por gastos funerarios, solo por resumen · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>FGE Baja California <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · boletín no localizado en <code>fgebc.gob.mx</code> · Infobae 2026/10/17 · miled 2026/10/17 · seguimiento de la candidata de ARGOS 135 · firmeza no informada</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Veracruz, 21 años por el homicidio de un comunicador (J-10/2026; 15-oct, sin boletín) · FGR Cosoleacaque, 4 años, y Banderilla, 2 años 6 meses (15-oct, sin boletín) · FGE Guerrero, cinco sentencias —Acapulco, Huitzuco, Iguala dos y Tlapehuala— (15-oct, solo por resumen) · Hermosillo, 25 años (16-oct) · Mesa de Coordinación de Guerrero, 11 sentencias en la semana del 5 al 11-oct (agregado, sin caso) · Hidalgo, Tulantepec: individualización de la pena el 21-oct.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>17 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · BC, Son, Chih · Coah, NL, Tamps, SLP, Zac · Mich, Nay, Ags · CDMX, Tlax · Ver, Tab · Gro, Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0 por boletín leído</b> · ninguna candidata nueva de la ventana</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>17</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>15</b>: BCS, Sin, Dgo · Jal, Col, Gto · Edomex, Mor, Pue, Hgo, Qro · Oax, Chis, Camp, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>0 errores de acceso</b> registrados (egreso bloqueado: ninguna lectura directa) · <b>3 fiscalías con dominio no devuelto</b>, dentro de las 15 <code>NO REVISADA</code>: Sin, Hgo, Camp</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 20 de 32 con consulta propia por entidad</b> · <b>11 solo por consulta regional amplia</b>: BCS, Dgo · Coah · Jal · CDMX, Edomex, Tlax, Qro · Camp, Yuc, QRoo · <code>NO REVISADA</code>: Ags · <b>armamento: 13 de 32 por dominio propio de seguridad o fiscalía</b> —BC, BCS, Son, Sin · Zac · Nay, Mich, Gto · CDMX, Edomex, Pue · Chis, QRoo—; <b>3 por portal del gobierno estatal</b> —NL, Mor, Gro—; <code>NO REVISADA</code>: Chih, Dgo · Coah, SLP, Tamps · Jal, Col, Ags · Tlax, Hgo, Qro · Ver, Tab · Oax, Camp, Yuc</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 15-oct</b>: existe (Milenio y republicadores) · <b>acciones del 16 y del 17-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta · <b>Defensa, Marina, Guardia Nacional y FGR</b>: SRIV · <b>gabinetedeseguridad.gob.mx</b>: SRIV (solo contenido de 2025)</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 18-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR DOS ROJOS</b>: ARG-136-001 y ARG-136-002 · <b>reserva</b> en ARG-136-002.
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-136-003 a ARG-136-005.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-136-006 y ARG-136-007.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-136-REC-001 a ARG-136-REC-003.
      <br><b>5.</b> <code>23 H 06 MIN; CUATRO DE SIETE CON FRONTERA O PUBLICADOS EL DÍA DE APERTURA SIN HORA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. CULIACÁN, TRES HECHOS CON MUERTOS EN DOS EDICIONES</b> (cálculo propio). ARG-136-003, ARG-135-001 y ARG-135-007. Línea: <b>solicitar a la FGE Sinaloa el cotejo balístico</b> entre los tres — hipótesis.
      <br><b>2. SILAO, ATAQUES CON MUERTOS EN VIVIENDA Y VÍA PÚBLICA EN CUATRO DÍAS.</b> ARG-136-REC-001 y ARG-134-001. Línea: <b>solicitar a la FGE Guanajuato si las carpetas comparten indicios o vehículos</b> — vínculo no acreditado.
      <br><b>3. ATAQUES DIRIGIDOS A UN ADULTO CON UN MENOR MUERTO.</b> ARG-136-REC-002 y ARG-134-REC-003. Línea: <b>solicitar a la Fiscalía de Puebla el aseguramiento y peritaje del arma vista en videovigilancia</b> — hipótesis.
      <br><b>4. TEMIXCO, CUERPO OCULTO EN UNA CAJUELA TRAS EL ATAQUE.</b> ARG-136-005. Línea: <b>solicitar a la FGE Morelos el registro del vehículo y su reporte de robo</b> — hipótesis.
      <br><b>5. CULIACÁN, AMETRALLADORAS EN DOS OPERATIVOS SIN VALIDAR ENTRE SÍ.</b> ARG-135-008 y el aseguramiento de la SSP en Industrial Bravo. Línea: <b>solicitar a la SSP Sinaloa y a la FGR si es la misma arma</b> — hipótesis.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>NO REVISADA</code>: dominio no devuelto por el buscador. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: SALAMANCA Y ACAPULCO", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA", co2)
 + page("CRIMEN ORGANIZADO (III) — ACCIONES INSTITUCIONALES", co3)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES: VENTANAS DE ARGOS 134 Y 135", rec1)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if any(a["c"]))
script = script.replace('"<br>Consulta: " + (top.fecha || "—") + " " + (top.hora || "")', '"<br>Fecha y hora (hecho o publicación): " + (top.fecha || "—") + " " + (top.hora || "") + "<br>Consulta: " + CONSULTA_TXT')
if "const CONSULTA_TXT" in script:
    script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
else:
    script = script.replace("const CORTE_FECHA", f'const CONSULTA_TXT = "{CONSULTA}";\nconst CORTE_FECHA', 1)
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert "WINDOW_DAYS = 2;" in script  # la ventana 17-oct 09:28 → 18-oct 08:34 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
