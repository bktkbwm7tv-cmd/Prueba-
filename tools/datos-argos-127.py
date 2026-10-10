# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 127: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-127.py <plantilla ARGOS 126> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "127", "2026-10-09", "07:20"
CONSULTA = "2026-10-09 07:20-07:30"
DUR = "22 h 24 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
BOL = "<code>BOLETÍN FEDERAL DEL 7-OCT, PUBLICADO EL 8-OCT, ALCANZADO SOLO POR REPUBLICADORES: CORROBORACIÓN DÉBIL POR CONSTRUCCIÓN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-127-001", estado="MX-PUE", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-08", hora="~19:00 (solo por resumen)",
  ent="Puebla", mun="Puebla (Fuentes de San Bartolo)", dia="8-OCT ~19:00",
  title="PUEBLA · PUEBLA — ASESINADO A BALAZOS UN HOMBRE DENTRO DE UN AUTOMÓVIL EN FUENTES DE SAN BARTOLO",
  hecho="Puebla capital · <code>FUENTES DE SAN BARTOLO, 123 PONIENTE</code> · JUEVES 8-OCT, ~19:00 (<code>SOLO POR RESUMEN</code>) · <b>1 hombre muerto</b> a balazos dentro de un Mercedes-Benz (🟡) · <b>cero detenidos</b> · identidad publicada por un solo medio, no oficial: no se reproduce · <code>UN AGRESOR LESIONADO, SOLO POR RESUMEN: NO SE INTEGRA</code>",
  panel="<b>1 hombre asesinado</b> a balazos dentro de un automóvil",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="sin fuente institucional ni nacional; hora por resumen", I=0, N=0, R=5, A=0,
  fechadas=["Diario Puntual (2026/10/08)", "Síntesis (2026/10/08)", "Reto Diario (2026/10/08)"], estatus="Pendiente de corroboración", arm=None,
  desl="Fuentes de San Bartolo no figura en el índice; Puebla capital figura en otros cortes: otros hechos. 🟡 por homicidio doloso único sin agravantes de la lista roja"),
 dict(id="ARG-127-002", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-08", hora="~14:20 (solo por resumen)",
  ent="Sinaloa", mun="Mazatlán (col. Ricardo Flores Magón)", dia="8-OCT ~14:20",
  title="SINALOA · MAZATLÁN — ATAQUE ARMADO EN UN AUTOLAVADO DE LA COLONIA FLORES MAGÓN: TRES MUERTOS; HERIDOS, DE 2 A 4 SEGÚN LA FUENTE",
  hecho="Mazatlán · <code>COL. RICARDO FLORES MAGÓN</code> · JUEVES 8-OCT ~14:20 · sujetos armados en un Nissan March rojo disparan contra quienes estaban dentro de un autolavado · <b>3 muertos</b>: 2 en el lugar y <b>1 joven de 24 años</b> en el hospital · <b>heridos</b>: <code>CONTRADICHOS: 2 / 3 / 4 SEGÚN LA FUENTE — NO SE SUMAN</code> (🔴) · FGE Sinaloa a cargo · <b>cero detenidos</b> · los 3 muertos, por titular; hora, calles, vehículo y edad <code>SOLO POR RESUMEN</code>",
  panel="Ataque en un autolavado: <b>3 muertos</b>; heridos contradichos (2 a 4)",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="La Jornada", conf="★★★☆☆",
  campo="número de heridos y hora", I=0, N=1, R=6, A=0,
  fechadas=["Luz Noticias (2026-10-08)", "Línea Directa (2026-10-08)", "La Jornada (2026/10/09)"], estatus="Parcialmente corroborado", arm=None,
  desl="Flores Magón y el autolavado no figuran en el índice. NO es ARG-127-004 (penal El Castillo, mismo municipio y día): otro lugar, otra hora, otras víctimas. 🔴 por homicidio múltiple"),
 dict(id="ARG-127-003", estado="MX-COL", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-08", hora="~12:43, aviso a emergencias (solo por resumen)",
  ent="Colima", mun="Colima (col. Moctezuma)", dia="8-OCT ~12:43",
  title="COLIMA · COLIMA — ASESINADO A BALAZOS UN HOMBRE DENTRO DE UN NEGOCIO DE LA COLONIA MOCTEZUMA",
  hecho="Colima capital · <code>COL. MOCTEZUMA, CALLE MEXICALI</code> · JUEVES 8-OCT, aviso a emergencias ~12:43 (<code>SOLO POR RESUMEN</code>) · sujetos armados entran a un negocio y disparan contra un hombre; huyen en un vehículo · <b>1 hombre muerto</b> (🟡) · <b>cero detenidos</b> · identidad no publicada · <code>LUGAR CONTRADICHO: BARBERÍA O ESTÉTICA; MEXICALI Y TAMAULIPAS O MEXICALI Y SONORA</code> · <code>NINGUNA FUENTE CON FECHA EN LA RUTA: EL DÍA, POR TITULAR («ESTE JUEVES»)</code>",
  panel="<b>1 hombre asesinado</b> a balazos dentro de un negocio",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="ninguna fuente con fecha en la ruta; lugar contradicho", I=0, N=0, R=6, A=0,
  fechadas=[], estatus="Parcialmente corroborado", arm=None,
  desl="Colima figura en el índice (ARG-101-002, ARG-104-005, ARG-105-006, ARG-106-002, de agosto; ARG-117-003, de septiembre): otros hechos. Homicidios en la misma colonia de 2022, 2023 y 2024: otros hechos. 🟡 por homicidio doloso único sin agravantes de la lista roja"),
 dict(id="ARG-127-004", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-08", hora="~10:00, petición de apoyo de custodios (solo por resumen)",
  ent="Sinaloa", mun="Mazatlán (penal El Castillo)", dia="8-OCT ~10:00",
  title="SINALOA · MAZATLÁN — RIÑA CON DISPAROS EN EL PENAL DE EL CASTILLO: DIEZ MUERTOS, UNO DE ELLOS UN MENOR DE VISITA, Y DIECISÉIS INTERNOS HERIDOS",
  hecho="Centro Penitenciario <code>EL CASTILLO</code>, Mazatlán · JUEVES 8-OCT, día de visita familiar · riña con disparos entre internos; los custodios piden apoyo ~10:00 · <b>10 muertos</b>: <b>9 internos</b> y <b>1 menor de edad que estaba de visita</b> · <b>16 internos heridos</b>, trasladados a hospitales (🔴) · <b>SSP Sinaloa</b> confirma la cifra, por titular · <b>detenidos: no informados</b> · visitas suspendidas · FGE Sinaloa investiga · que el titular de la SSP descarte el ingreso de un grupo armado, <code>SOLO POR RESUMEN</code> · <code>CIFRA INICIAL: 6 MUERTOS Y 15 HERIDOS</code> · <code>EDAD DEL MENOR CONTRADICHA: NO SE PUBLICA</code> · <code>INGRESO DE LAS ARMAS AL PENAL: SIN EXPLICACIÓN OFICIAL</code> · hora <code>SOLO POR RESUMEN</code>",
  panel="Riña con disparos en el <b>penal El Castillo</b>: <b>10 muertos</b> —un menor de visita— y <b>16 heridos</b>",
  inst="SSP Sinaloa <span class=\"muted-note\">(por cita)</span>", nac="Proceso · La Jornada · Infobae · El Financiero · Reforma", conf="★★★☆☆",
  campo="hora del inicio y edad del menor", I=1, N=9, R=5, A=0,
  fechadas=["Proceso (2026/10/8)", "Expansión (2026/10/08)", "La Silla Rota (2026/10/8)", "El Financiero (2026/10/08)", "El Heraldo de México (2026/10/8)", "El Mañana (2026/10/8)", "Informador (20261008)", "Infobae (2026/10/09)", "La Jornada (2026/10/09)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Castillo no figura en el índice; Mazatlán figura en 33 ARG-ID, el más reciente ARG-125-ARM-013 (2-oct): otros hechos. NO es ARG-127-002 (autolavado de Flores Magón). 🔴 por motín con víctimas, que la lista roja nombra"),
 dict(id="ARG-127-005", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-08", hora="no fijada",
  ent="Sinaloa", mun="Culiacán (privada Montecarlo)", dia="PUB. 8-OCT, HORA NO FIJADA",
  title="SINALOA · CULIACÁN — CAMIONETA CON BLINDAJE ARTESANAL, TREINTA CARTUCHOS CALIBRE .50 Y DOS CARGADORES PARA FUSIL BARRETT",
  hecho="Culiacán · <code>PRIVADA MONTECARLO</code> · publicado JUEVES 8-OCT · <b>GOES de la Policía Estatal</b> con el Grupo Interinstitucional, en patrullaje · Chevrolet Cheyenne con <b>blindaje artesanal</b> y sistema ponchallantas · <b>30 cartuchos cal. .50</b> · <b>2 cargadores para fusil tipo Barrett</b> (🟢) · <b>sin arma</b> asegurada · <b>cero detenidos</b> · <code>30 Y 2: SOLO POR RESUMEN</code>; por titular solo «cargadores» en plural, «municiones calibre 50» y la camioneta · " + FR,
  panel="Camioneta blindada: <b>30 cartuchos .50</b> y <b>2 cargadores Barrett</b> (solo por resumen); sin arma ni detenidos",
  inst="SSP Sinaloa <span class=\"muted-note\">(post indexado, no leído)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="30 y 2, solo por resumen", I=1, N=0, R=5, A=0,
  fechadas=["Línea Directa (2026-10-08)", "Luz Noticias (2026-10-08)", "Tus Buenas Noticias (2026/10/08)"], estatus="Parcialmente corroborado", arm="ARG-127-ARM-001", fecha_txt="no fijada (publicado 2026-10-08)",
  desl="Montecarlo no figura en el índice. NO es ARG-126-REC-011 (Corolla con lanzagranadas, Centro, 2-oct) ni ARG-126-REC-006 (Parque Alamedas, 6-oct)"),
 dict(id="ARG-127-006", estado="MX-SLP", region="Noreste", color="verde", impacto="pequeno", fecha="2026-10-08", hora="no fijada",
  ent="San Luis Potosí", mun="San Luis Potosí (Real de Peñasco, Rural Atlas, Papagayos)", dia="PUB. 8-OCT, HORA NO FIJADA",
  title="SAN LUIS POTOSÍ · SAN LUIS POTOSÍ — LA GUARDIA CIVIL ESTATAL DETIENE A TRES PERSONAS: DOS REVÓLVERES Y CARTUCHOS",
  hecho="San Luis Potosí capital · tres intervenciones publicadas el JUEVES 8-OCT · <b>Guardia Civil Estatal</b> · <code>REAL DE PEÑASCO</code>: José «N», 29 años, <b>1 revólver</b> y <b>29 cartuchos</b> · <code>RURAL ATLAS</code>: Francisco «N», 47 años, <b>1 revólver</b>, <b>6 cartuchos</b> y 1 vehículo · <code>PAPAGAYOS</code>: Eder «N», 43 años, solo presunta droga (🟢) · <b>3 detenidos</b>, por titular; 2 de ellos con arma · revólveres, cartuchos, nombres y edades <code>SOLO POR RESUMEN</code> · <b>35 cartuchos</b> = 29 + 6 de dos intervenciones distintas, <b>cálculo propio</b> · " + FR,
  panel="<b>3 detenidos</b>; 2 revólveres y 35 cartuchos (suma propia, por resumen)",
  inst="SSPC SLP <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="desglose por persona, solo por resumen", I=1, N=0, R=5, A=0,
  fechadas=["El Heraldo de SLP (2026/10/08)", "Potosí Noticias (2026/10/08)"], estatus="Parcialmente corroborado", arm="ARG-127-ARM-002", fecha_txt="no fijada (publicado 2026-10-08)",
  desl="Real de Peñasco, Rural Atlas y Papagayos no figuran en el índice. El detenido de Papagayos no entra en el conteo de armamento")
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-127-REC-001", estado="MX-MIC", region="Occidente", fecha="2026-10-08", hora="~03:30-05:00 (solo por resumen)", orig="ARGOS 126", col_orig="amarillo",
  ent="Michoacán", mun="Uruapan (col. Sol Naciente)", dia="8-OCT MADRUGADA",
  title="MICHOACÁN · URUAPAN — CATEO FEDERAL REPELIDO A BALAZOS EN LA COLONIA SOL NACIENTE: DOS AGENTES HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126</code> · <code>COL. SOL NACIENTE, ORIENTE DE URUAPAN</code> · madrugada del JUEVES 8-OCT, ~03:30-05:00 · agentes federales ejecutan un cateo y son recibidos a balazos · <b>2 agentes heridos</b> (🟡 en su ventana) · <code>DETENIDOS CONTRADICHOS: 1 FRENTE A 10, «SALDO PRELIMINAR»</code> · <code>CORPORACIÓN FEDERAL NO PRECISADA</code> · sin comunicado oficial localizado",
  panel="Cateo federal repelido: <b>2 agentes heridos</b>; detenidos, 1 o 10", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Meganoticias",
  conf="★★★☆☆", campo="número de detenidos y hora", I=0, N=1, R=2, A=0,
  fechadas=[], desl="Uruapan figura en el índice (ARG-95-004, ARG-105-004, ARG-125-035, ARG-125-036): otros hechos, otras colonias. 🟡: el Estado inicia y es repelido; los heridos no mueven el color"),
 dict(id="ARG-127-REC-002", estado="MX-ZAC", region="Noreste", fecha="2026-10-07", hora="no fijada", orig="ARGOS 126", col_orig="verde",
  ent="Zacatecas", mun="Ojocaliente (Las Coloradas)", dia="7-OCT",
  title="ZACATECAS · OJOCALIENTE — CINCO ARMAS LARGAS, 1,093 CARTUCHOS Y 47 CARGADORES EN LAS COLORADAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126</code> · <code>LAS COLORADAS</code> · acciones del MIÉRCOLES 7-OCT · <b>Ejército</b> · <b>5 armas largas</b> · <b>1,093 cartuchos</b> · <b>47 cargadores</b> · 7 chalecos tácticos, 12 placas balísticas, 2 vehículos (🟢 en su ventana) · <b>sin detenidos publicados</b> · desglose <code>SOLO POR RESUMEN</code> · ninguna nota reporta agresión ni enfrentamiento · " + BOL,
  panel="<b>5 armas largas</b>, <b>1,093 cartuchos</b> y 47 cargadores; sin detenidos", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio",
  conf="★★★☆☆", campo="republicadores de un mismo boletín", I=1, N=1, R=3, A=0,
  fechadas=["Milenio (acciones del 7-oct en la ruta)"], desl="Ojocaliente figura en el índice (ARG-112-001, coche bomba del 30-ago; ARG-114-001): otros hechos. Las Coloradas no figura"),
 dict(id="ARG-127-REC-003", estado="MX-TAB", region="Golfo", fecha="2026-10-07", hora="no fijada", orig="ARGOS 126", col_orig="verde",
  ent="Tabasco", mun="Centro (fracc. La Huerta)", dia="7-OCT",
  title="TABASCO · CENTRO — DOS DETENIDOS EN LA HUERTA: CUATRO ARMAS LARGAS, TRES CORTAS Y 540 CARTUCHOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126</code> · <code>FRACCIONAMIENTO LA HUERTA</code> · acciones del MIÉRCOLES 7-OCT · <b>Guardia Nacional, Defensa, SSPC, FGR y Policía Estatal</b> · <b>2 detenidos</b> · <b>4 armas largas</b> · <b>3 armas cortas</b> · <b>7 cargadores</b> · <b>540 cartuchos</b> · 4 kg de marihuana, 80 dosis de metanfetamina, 100 de cocaína, chalecos y placas (🟢 en su ventana) · desglose <code>SOLO POR RESUMEN</code>; «siete armas», por otra fuente · " + BOL + " · <code>POSIBLE DUPLICIDAD CON UNA DETENCIÓN DE DOS PERSONAS DE LA SSPC EN CENTRO PUBLICADA EL 8-OCT</code>",
  panel="<b>2 detenidos</b>, <b>4 largas</b>, <b>3 cortas</b> y 540 cartuchos", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio · El Independiente",
  conf="★★☆☆☆", campo="desglose solo por resumen; posible duplicidad", I=1, N=2, R=2, A=0,
  fechadas=["Milenio (acciones del 7-oct en la ruta)", "El Independiente (2026/10/08)"], desl="La Huerta no figura en el índice. NO es ARG-124-ARM-008 (Centro, 23-sep)"),
 dict(id="ARG-127-REC-004", estado="MX-SIN", region="Noroeste", fecha="2026-10-07", hora="no fijada", orig="ARGOS 126", col_orig="verde",
  ent="Sinaloa", mun="Cosalá", dia="7-OCT",
  title="SINALOA · COSALÁ — CINCO LABORATORIOS CLANDESTINOS INHABILITADOS Y 2.6 TONELADAS DE METANFETAMINA DESTRUIDAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126</code> · acciones del MIÉRCOLES 7-OCT · <b>SSPC y FGR</b> · <b>5 laboratorios</b> inhabilitados, por titular de dos medios regionales · <b>2.6 toneladas de metanfetamina</b> destruidas, por titular; <code>2,693 KG, 450 KG DE SÓLIDO BLANCO Y 450 KG DE SOSA: SOLO POR RESUMEN</code> (🟢 en su ventana) · <b>sin armamento</b> · detenidos no informados · <code>UN TITULAR NACIONAL SITÚA CINCO LABORATORIOS EN JALISCO, NAYARIT Y SINALOA: NO ARBITRADO</code> · " + BOL,
  panel="<b>5 laboratorios</b> inhabilitados y <b>2.6 t de metanfetamina</b> destruidas", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio",
  conf="★★★☆☆", campo="cifras de sustancias solo por resumen", I=1, N=1, R=2, A=0,
  fechadas=["Línea Directa (2026-10-08)"], desl="Cosalá no figura en el índice en octubre. ARGOS 126 lo retiró por falta de fragmento; la cifra de laboratorios ya se sostiene en el slug de Noroeste"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-127-ARM-001", ficha="ARG-127-005", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Culiacán (privada Montecarlo)", c=[0,0,0,0,30,2,0,0,0,0], corp="GOES + Grupo Interinstitucional", conf="Bajo", nota="cartuchos cal. .50 y cargadores para Barrett, sin arma; 30 y 2 solo por resumen", fuentes=["Línea Directa (2026-10-08)", "Luz Noticias (2026-10-08)"]),
 dict(id="ARG-127-ARM-002", ficha="ARG-127-006", estado="MX-SLP", region="Noreste", ent="San Luis Potosí", mun="San Luis Potosí", c=[2,0,0,0,35,0,0,0,0,2], corp="Guardia Civil Estatal", conf="Bajo", nota="dos intervenciones (29 + 6 cartuchos, suma propia); cifras solo por resumen; 1 detenido más, sin arma, fuera del conteo", fuentes=["El Heraldo de SLP (2026/10/08)", "Potosí Noticias (2026/10/08)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [2, 0, 0, 0, 65, 2, 0, 0, 0, 2], TOT
assert cnt == {"rojo": 2, "amarillo": 2, "verde": 2}, cnt

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
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": "verde", "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": "2026-10-08", "hora": "no fijada"}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 126 — Reporte Nacional de Seguridad — 2026-10-08</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. EXIJA EL DICTAMEN BALÍSTICO Y EL ORIGEN DE LAS ARMAS DEL PENAL EL CASTILLO</b> (ARG-127-004): cómo entraron, quién custodiaba
      y cómo se controló la visita familiar del 8-oct.
      <br><b>2. LOCALICE EL VEHÍCULO DE LOS ATACANTES DEL AUTOLAVADO DE FLORES MAGÓN</b> (ARG-127-002) con cámaras y lectores de
      placas de Mazatlán.
      <br><b>3. EXIJA EL PARTE DEL CATEO DE SOL NACIENTE, URUAPAN</b> (ARG-127-REC-001): corporación, número real de detenidos —1 o 10—
      y estado de los dos agentes heridos.
      <br><b>4. VIGILE EL CUMPLIMIENTO DEL AMPARO 412/2026</b> para los siete desaparecidos de El Balcón (ARG-125-051) y exija el peritaje
      oficial del video del 8-oct antes de usarlo como dato.
      <br><b>5. EXIJA A LA FISCALÍA DE NAYARIT LA CIFRA E IDENTIFICACIONES DE LA CURVA</b>, Xalisco (ARG-125-003): la Presidencia y la
      CNB remiten a ella y no hay comunicado indexado.
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>8-oct 08:56 → 9-oct 07:20 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,27 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: del más reciente al más antiguo</b>; al final, los dos de hora no fijada.
    <br><code>LAS {len(R)} RECUPERACIONES DEL FINAL PERTENECEN A LA VENTANA DE ARGOS 126 Y QUEDAN FUERA DEL SEMÁFORO, DEL MAPA, DEL RADAR Y DE TODOS LOS TOTALES.</code>
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
    <b>Total de armas integradas: {ARMAS}</b> —{TOT[0]} cortas, <b>cálculo propio</b>—. <b>Cartuchos y cargadores nunca se suman entre sí.</b>
    <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento</b>; fuera de ese conteo, <b>1 detenido</b> sin arma en San Luis Potosí (ARG-127-006). Cifras de armamento <b>solo por resumen</b> en las dos filas. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios: 15</b> —<b>13 en los dos rojos de Mazatlán</b> y 2 en los amarillos de Colima y Puebla—, más <b>16 heridos en el penal</b> y, en el autolavado, <b>de 2 a 4 según la fuente, sin sumar</b>: <b>cálculo propio</b>.
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
 tile(0, "Armas cortas", TOT[0], "<code>DOS REVÓLVERES, SIN CALIBRE PUBLICADO</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA EN HECHO PROPIO</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>30 DE ELLOS, CAL. .50 · TODOS SOLO POR RESUMEN</code>"),
 tile(4, "Cargadores", TOT[5], "<code>LOS DOS, PARA FUSIL TIPO BARRETT · SOLO POR RESUMEN</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR PUBLICADO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>MUNICIÓN .50 SIN FUSIL: NO SE CUENTA COMO ARMA</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>{len(ARM)} filas de armamento de {len(ARM)} hechos</b> en <b>{len(ENT_ARM)} entidades</b>: <b>todas con cifra</b>, ninguna cualitativa. <b>Totales por categoría: cálculo propio.</b>
    <code>LAS DOS FILAS LLEVAN FRONTERA DE VENTANA Y DESGLOSE SOLO POR RESUMEN.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Verde = aseguramiento sin enfrentamiento · amarillo = derivado de enfrentamiento. La sola presencia de armas no vuelve roja a una entidad.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    cells = "".join(f"<td>{('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for v in c[:9])
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    return f'      <tr id="{a["id"]}"><td><a href="#{a["ficha"]}"><code>{a["id"]}</code></a></td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>no fijada<br><span class="muted-note">pub. 2026-10-08</span></td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'
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
    <b>Lectura regional</b> —2 filas, <b>cálculo propio</b>—: <b>Noroeste 1</b> · <b>Noreste 1</b> · <b>Occidente 0</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    El armamento de las recuperaciones —Ojocaliente y Centro, Tabasco— va en su ficha y <b>no entra en esta tabla</b>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA CON BOLETÍN DEL DOMINIO OFICIAL EN LA VENTANA</code> · dos publicadas por medios el 8-oct, abajo</span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub"><b>6 personas</b> —1 + 5, <b>suma propia</b>— en dos candidatas con pena publicada quedan en <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto ordenado y publicado</b> en la ventana</span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>de 24 revisadas más la FGR</b> · 8 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Sonora</b><br>Cajeme (Ampliación Alameda)</td><td>Luis Carlos «N» · <span class="muted-note">homicidio calificado, juicio oral; hecho del 14-mar-2024</span></td><td><b>25 años</b></td><td>FGJES</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>8-oct</b> por un medio con fecha en la ruta y tres sin ella; <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
      <tr><td><b>Campeche</b><br>Campeche (Lerma)</td><td>Juan «N», Elizabet «N», Francisco «N», Carlos «N» y Vilma «N» · <span class="muted-note">posesión de cartuchos y de arma de uso exclusivo, abreviado; cateo del 15-jul-2024</span></td><td><b>2 a 5 m</b> y multa, solo por resumen</td><td>FGR · juez de Control Federal</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>8-oct</b> por un medio regional con fecha en la ruta; <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
      <tr><td><b>Veracruz</b><br>Veracruz</td><td>Sebastián Alejandro «N» · <span class="muted-note">homicidio doloso calificado, juicio oral J-10/2026</span></td><td><span class="muted-note">no publicada</span></td><td>FGE Veracruz</td><td>Fallo condenatorio sin pena, dentro de un <b>agregado de 24 h</b> publicado el 8-oct por un medio; <code>NO INTEGRAR</code></td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas por primera vez, publicadas antes de la apertura y sin boletín oficial</b>: Matamoros, Tamps., 6 sentenciados a 25 años 3 días por la desaparición de cuatro estadounidenses (6-oct) · Quintana Roo, FGE, hasta 50 años (7-oct) · Buenavista, Mich., 28 años a dos (~7-oct) · Nayarit, 240 años por secuestro (3-oct) y 40 años (6-oct) · FGR: Juárez, Senderos de San Isidro, 6 a 8 m a tres (6-oct); Hermosillo–Sahuaripa, 15 años a tres (6-oct); Colima, 4 años a tres · BCS, La Paz, 21 años (1-oct). <b>Sin fecha fijada</b>: Culiacán, 22 años (ruta solo con mes). <code>NO SE INTEGRAN.</code>
    <br><b>Candidatos heredados, siguen sin boletín oficial</b>: Juárez FGR (Acequias) · NL, Laurentino «N», 44 años · Edomex ×4 · Santa Catarina · Cárdenas FGR · San Andrés Tuxtla · Nogales · Tijuana FGR · Puebla · Hidalgo · Lagos de Moreno. <code>NO SE INTEGRAN.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>24 de 32</b> · <b>FGR revisada: Sí</b> · BCS, Sin, Son, Chih, Dgo · Coah, NL, Tamps, SLP, Zac · Col, Nay, Ags, Mich · CDMX, Edomex · Ver, Tab · Gro, Chis, Oax, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>0</b></td></tr>
      <tr><td><b>Con sentencias publicadas en ventana solo por medios</b></td><td><b>2</b> fiscalías estatales: Sonora y Veracruz (agregado) · <b>y la FGR</b>, en Campeche</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>22</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>8</b>: BC · Jal, Gto · Mor, Pue, Hgo, Qro, Tlax</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 31 de 32</b> —Aguascalientes, <code>NO REVISADA</code>— · <b>armamento: 26 de 32</b> —BCS, Son, Dgo, CDMX, Ags y Tlaxcala, <code>NO REVISADA</code>— · Morelos, <code>SIN RESULTADO INDEXADO EN VENTANA</code> por <code>site:</code> · GN, SEDENA y SEMAR regionales: <code>NO REVISADA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 7-oct</b>: publicado el 8-oct, diario, por republicadores · <b>acciones del 8-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 9-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR DOS ROJOS EN EL MISMO MUNICIPIO Y EL MISMO DÍA</b>: motín con víctimas (ARG-127-004) y homicidio múltiple (ARG-127-002), Mazatlán.
      <br><b>2.</b> <b>Amarillos</b> por homicidio doloso único (ARG-127-001, ARG-127-003); <b>verdes</b> de aseguramiento sin enfrentamiento (ARG-127-005, ARG-127-006).
      <br><b>3.</b> <b>Ningún detenido publicado</b> por los cuatro hechos violentos —en el penal, no informados—: la respuesta institucional del corte no alcanza a los hechos que fijan el nivel.
      <br><b>4.</b> Las cuatro recuperaciones de la ventana de ARGOS 126 —un amarillo y tres verdes— quedan fuera del nivel y de los totales.
      <br><b>5.</b> <code>22 H 24 MIN; DOS DE SEIS HECHOS CON FRONTERA DE VENTANA Y LAS HORAS DE LOS OTROS CUATRO SOLO POR RESUMEN; BOLETÍN FEDERAL DEL 8-OCT SIN INDEXAR: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. EN CONCORDIA EL AEI SE CARGA EN DRON.</b> Los titulares describen «explosivos para dron» en Pánuco (ARG-126-004) —el listado de la SSPE, solo por resumen—, 15 días
      después de los «tipo mina» del mismo municipio (ARG-124-003, cifra heredada): dos tipologías, <b>cálculo propio de fechas</b>. Línea: <b>taller y operadores de dron</b> — hipótesis.
      <br><b>2. EL CALIBRE .50 CIRCULA EN CULIACÁN SIN SU FUSIL.</b> Segundo hallazgo de armamento de alto poder en un vehículo en ocho días (ARG-127-005,
      ARG-126-REC-011). Línea: <b>rastreo del fusil .50</b> y de los talleres de blindaje artesanal.
      <br><b>3. DOS RENGLONES MAYORES DEL BOLETÍN DEL 7-OCT, SIN DETENIDOS.</b> Ojocaliente (ARG-127-REC-002) y Cosalá (ARG-127-REC-004): el boletín federal no publica detenidos en sus mayores aseguramientos.
      Línea: <b>exigir detenidos y carpeta</b> por cada aseguramiento mayor.
      <br><b>4. EJECUCIÓN URBANA DENTRO DE NEGOCIOS Y VEHÍCULOS.</b> Colima (ARG-127-003) y Puebla (ARG-127-001): ataque dirigido, a corta distancia, con vehículo de huida.
      Línea: <b>videovigilancia y placas</b> de los vehículos de huida.
      <br><b>5. LA BRECHA ENTRE DETENCIÓN Y CONDENA SIGUE ABIERTA.</b> Ninguna sentencia con boletín oficial en la ventana; las dos candidatas —Cajeme y Campeche, FGR— solo
      existen en medios. Línea: <b>exigir el boletín</b> de cada sentencia anunciada.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados/</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>: lo indexado llega al 6-oct. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación nueva localizada dentro de la ventana</b>.
    <br><b>El agregado federal del periodo</b> es el <b>boletín de las acciones del 7-oct, publicado el 8-oct</b>, diario, alcanzado por republicadores.
    <code>NO INDEXADO POR SU EMISOR: SUS REPUBLICADORES NO SON FUENTES INDEPENDIENTES ENTRE SÍ.</code>
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — JUEVES 8-OCT: PUEBLA, MAZATLÁN Y COLIMA", co1)
 + page("CRIMEN ORGANIZADO (II) — JUEVES 8-OCT: PENAL EL CASTILLO Y HECHOS DE HORA NO FIJADA", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES DE LA VENTANA DE ARGOS 126: 8 Y 7-OCT", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 8-oct 08:56 → 9-oct 07:20 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, TOT, ARMAS, len(E), len(R))
