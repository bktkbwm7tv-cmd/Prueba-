# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 129: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-129.py <plantilla ARGOS 128> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "129", "2026-10-11", "08:58"
CONSULTA = "2026-10-11 08:58-09:40"
DUR = "23 h 50 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SEMAR = "<code>COMUNICADO DE LA SEMAR DEL 10-OCT CON CINCO EVENTOS DE FECHA NO PUBLICADA, ALCANZADO SOLO POR MEDIOS</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-129-001", estado="MX-VER", region="Golfo", color="rojo", impacto="grande", fecha="2026-10-10", hora="~22:00 (solo por resumen)",
  ent="Veracruz", mun="Minatitlán (refinería Lázaro Cárdenas, portada norte)", dia="10-OCT ~22:00",
  title="VERACRUZ · MINATITLÁN — ATAQUE ARMADO EN EL ACCESO NORTE DE LA REFINERÍA DE PEMEX: UN VIGILANTE MUERTO Y UN HERIDO",
  hecho="Minatitlán · <code>REFINERÍA LÁZARO CÁRDENAS, PORTADA NORTE</code> · SÁBADO 10-OCT, noche, ~22:00 (" + RES + ") · agresores, en motocicleta según una versión (" + RES + "), disparan contra personal de vigilancia en el acceso y huyen · <b>1 vigilante muerto</b> y <b>1 herido</b>, por titular de seis medios (🔴) · <code>SALDO CONTRADICHO: PEMEX, POR TITULAR DE DOS MEDIOS, INFORMA «DOS LESIONADOS» Y NINGÚN FALLECIDO</code> · <b>FGE Veracruz</b> investiga · despliegue de Policía Estatal, Marina, Defensa y GN, " + RES + " · <b>cero detenidos</b> · móvil no establecido · identidades no publicadas",
  panel="Ataque armado en el acceso de la <b>refinería de Pemex</b>: <b>1 vigilante muerto</b> y 1 herido, saldo contradicho",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span> · Pemex <span class=\"muted-note\">(por cita)</span>", nac="Infobae · La Silla Rota · Milenio · El Universal · López-Dóriga", conf="★★★☆☆",
  campo="saldo contradicho (un muerto o dos lesionados); hora, solo por resumen", I=0, N=6, R=2, A=0,
  fechadas=["La Silla Rota (2026/10/10)", "Infobae (2026/10/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Minatitlán y la refinería Lázaro Cárdenas no figuran en el índice. Infobae «EN VIVO» del 11-oct: <i>liveblog</i>, no fecha el hecho. 🔴 por ataque a infraestructura crítica"),
 dict(id="ARG-129-002", estado="MX-PUE", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-10", hora="~14:00 (solo por resumen)",
  ent="Puebla", mun="San Gregorio Atzompa (junta auxiliar de Chipilo)", dia="10-OCT ~14:00",
  title="PUEBLA · CHIPILO — DISPARAN CONTRA POLICÍAS QUE INTENTABAN REVISAR UNA CAMIONETA: UN POLICÍA ESTATAL HERIDO",
  hecho="Chipilo de Francisco Javier Mina, San Gregorio Atzompa · SÁBADO 10-OCT, tarde, ~14:00 (" + RES + ") · los ocupantes de una camioneta disparan contra <b>policías estatales y municipales</b> que intentan detenerla para revisión, y huyen a pie · <b>1 policía estatal herido</b> por arma de fuego, por titular; estable, " + RES + " (🟡) · <b>camioneta Volkswagen Tiguan gris sin placas asegurada</b>, por titular · <b>cero detenidos</b> · <b>sin armas aseguradas publicadas</b> · operativo con Marina, GN, Defensa, FGE y FGR, " + RES + " · <code>ORIGEN DE LA PERSECUCIÓN CONTRADICHO: ROBO DE VEHÍCULO O VIGILANCIA</code> · <code>UN MEDIO LO FECHA EL «11 DE OCTUBRE»: EL RESTO, SÁBADO 10</code>",
  panel="Disparan contra policías en una revisión: <b>1 policía estatal herido</b>; camioneta asegurada, sin detenidos",
  inst="SSP Puebla <span class=\"muted-note\">(por cita)</span>", nac="Infobae · El Universal Puebla · N+", conf="★★★☆☆",
  campo="hora y origen de la persecución, solo por resumen", I=1, N=3, R=6, A=0,
  fechadas=["Síntesis (2026/10/10)", "Infobae (2026/10/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chipilo y San Gregorio Atzompa no figuran en el índice. 🟡: la autoridad intenta la revisión y es repelida; sin muertos del personal. Si se acredita emboscada, sube a rojo"),
 dict(id="ARG-129-003", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-10", hora="tarde (solo por resumen)",
  ent="Sinaloa", mun="Escuinapa (col. Insurgentes)", dia="10-OCT, TARDE",
  title="SINALOA · ESCUINAPA — ASESINADO A BALAZOS UN JOVEN EN UN TALLER MECÁNICO DE LA COLONIA INSURGENTES",
  hecho="Escuinapa · <code>COL. INSURGENTES, TALLER MECÁNICO</code> · SÁBADO 10-OCT, por la tarde (" + RES + ") · hombres armados disparan contra un joven que reparaba una camioneta · <b>1 hombre de 25 años muerto</b>, por titular (🟡) · <b>FGE Sinaloa</b> procesa el lugar, " + RES + " · <b>cero detenidos</b> · móvil no establecido · identidad: no se reproduce · " + FR,
  panel="<b>1 joven asesinado</b> a balazos en un taller mecánico",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="hora, solo por resumen; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Línea Directa (2026-10-10)"], estatus="Parcialmente corroborado", arm=None,
  desl="Escuinapa figura en el índice: otros hechos. NO es el homicidio en un taller de motocicletas de la col. Pueblo Nuevo del 18-sep. NO es ARG-129-004 (zona centro). 🟡 por homicidio doloso único"),
 dict(id="ARG-129-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-10", hora="no fijada",
  ent="Sinaloa", mun="Escuinapa (zona centro)", dia="PUB. 10-OCT, HORA NO FIJADA",
  title="SINALOA · ESCUINAPA — ASESINADA EN UN ATAQUE ARMADO UNA VENDEDORA DE BIRRIA EN LA ZONA CENTRO",
  hecho="Escuinapa · <code>ZONA CENTRO</code> · SÁBADO 10-OCT, publicado ese día · ataque armado · <b>1 mujer muerta</b>, vendedora de birria, por titular (🟡) · <b>cero detenidos</b> · móvil no establecido · identidad: no se reproduce · " + FR,
  panel="<b>1 mujer asesinada</b>, vendedora de birria",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="hora y lugar exacto no publicados; fuente única con fecha", I=0, N=0, R=1, A=0,
  fechadas=["Línea Directa (2026-10-10)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-10, hora no fijada",
  desl="NO es ARG-129-003 (taller de la col. Insurgentes): dos ataques según el titular. 🟡 por homicidio doloso único"),
 dict(id="ARG-129-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-10-10", hora="no fijada",
  ent="Sinaloa", mun="Mazatlán (inmediaciones de Las Porras)", dia="PUB. 10-OCT, HORA NO FIJADA",
  title="SINALOA · MAZATLÁN — AGREDEN A ELEMENTOS DE LA MARINA CERCA DE LAS PORRAS: UN DETENIDO CON UN ARMA LARGA",
  hecho="Mazatlán · <code>INMEDIACIONES DEL POBLADO LAS PORRAS</code> · fecha del hecho no publicada; comunicado del SÁBADO 10-OCT · <b>elementos navales agredidos</b> por presuntos integrantes de la delincuencia organizada; la Marina repele · <code>CONTEXTO DEL DESPLIEGUE NO PUBLICADO: QUIÉN INICIÓ, NO DETERMINADO</code> (🟡) · <b>1 detenido</b> · <b>1 arma larga</b> · <b>29 cartuchos</b> — cifras " + RES + " · sin bajas publicadas · " + SEMAR + " · " + FR,
  panel="Agresión a <b>marinos</b>: <b>1 detenido</b>, 1 arma larga y 29 cartuchos, solo por resumen",
  inst="SEMAR <span class=\"muted-note\">(por cita)</span>", nac="La Razón · N+", conf="★★☆☆☆",
  campo="fecha del hecho no publicada; cifras solo por resumen", I=1, N=2, R=3, A=0,
  fechadas=["La Razón (2026/10/10)", "Línea Directa (2026-10-10)"], estatus="Parcialmente corroborado", arm="ARG-129-ARM-001", fecha_txt="no publicada (comunicado del 2026-10-10)",
  desl="Las Porras no figura en el índice. NO es el ataque a marinos de julio cerca de la presa Picachos ni el enfrentamiento de agosto en Camacho. 🟡: sin bajas del personal y sin contexto que acredite emboscada; si se acredita, sube a rojo"),
 dict(id="ARG-129-006", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-10", hora="no fijada",
  ent="Sinaloa", mun="sur del estado (Varados y Siqueros)", dia="PUB. 10-OCT, HORA NO FIJADA",
  title="SINALOA · SUR DEL ESTADO — LA MARINA INHABILITA SIETE ARTEFACTOS EXPLOSIVOS IMPROVISADOS EN VARADOS Y SIQUEROS",
  hecho="Sur de Sinaloa · <code>POBLADOS VARADOS Y SIQUEROS</code> · fecha del hecho no publicada; comunicado del SÁBADO 10-OCT · <b>Marina</b> · <b>7 artefactos explosivos improvisados</b> localizados e inhabilitados por personal especializado, " + RES + "; «explosivos», por titular (🟢) · <b>sin detenidos en este evento</b> · <code>EL COMUNICADO SUMA 8 ARMAS LARGAS, 67 CARGADORES Y 215 CARTUCHOS EN CINCO EVENTOS, SIN ATRIBUCIÓN POR EVENTO — SOLO POR RESUMEN: NO SE INTEGRAN SALVO LAS PORRAS</code> · otro evento del mismo comunicado: 1 detenido con dosis de droga en la col. Infonavit Playas, Mazatlán, sin armamento · " + SEMAR + " · " + FR,
  panel="<b>7 AEI inhabilitados</b>, solo por resumen; sin detenidos",
  inst="SEMAR <span class=\"muted-note\">(por cita)</span>", nac="La Razón · N+", conf="★★☆☆☆",
  campo="fecha del hecho no publicada; cifra de AEI solo por resumen", I=1, N=2, R=4, A=0,
  fechadas=["La Razón (2026/10/10)", "Línea Directa (2026-10-10)"], estatus="Parcialmente corroborado", arm="ARG-129-ARM-002", fecha_txt="no publicada (comunicado del 2026-10-10)",
  desl="Varados y Siqueros no figuran en el índice. Las «103 mil dosis» del mismo comunicado son de Rincón de Higueras, El Rosario, 4-oct, publicadas el 5-oct: <code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code>, no se ficha. NO es ARG-125-ARM-007 ni ARG-126-004 (Pánuco, 82 AEI): otros lugares"),
 dict(id="ARG-129-007", estado="MX-HID", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-10", hora="no fijada",
  ent="Hidalgo", mun="Pachuca (Las Lajas)", dia="PUB. 10-OCT, HORA NO FIJADA",
  title="HIDALGO · PACHUCA — CATEO EN LAS LAJAS: DOS DETENIDOS Y 630 DOSIS DE DROGA",
  hecho="Pachuca · <code>LAS LAJAS</code> · publicado el SÁBADO 10-OCT · <b>Defensa y GN</b> con corporaciones estatales · cateo · <b>2 detenidos</b> y <b>630 dosis</b> aseguradas, por titular (🟢) · <b>sin armamento publicado</b> · " + FR,
  panel="Cateo: <b>2 detenidos</b> y 630 dosis; sin armamento",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="La Silla Rota", conf="★★☆☆☆",
  campo="fuente única; hora no fijada", I=0, N=1, R=0, A=0,
  fechadas=["La Silla Rota (2026/10/10)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-10, hora no fijada",
  desl="Las Lajas no figura en el índice; Pachuca figura (ARG-95-001, ARG-108-007): otros hechos"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-129-REC-001", estado="MX-MIC", region="Occidente", fecha="2026-10-02", hora="~23:00 (solo por resumen)", orig="ARGOS 125", col_orig="rojo",
  ent="Michoacán", mun="Zamora (bar El Nuevo Quijote, col. Las Fuentes)", dia="2-OCT, NOCHE",
  title="MICHOACÁN · ZAMORA — ATAQUE ARMADO EN UN BAR: CUATRO MUERTOS Y TRES HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>BAR EL NUEVO QUIJOTE, COL. LAS FUENTES</code> · noche del VIERNES 2-OCT, ~23:00 (" + RES + ") · hombres armados irrumpen y disparan contra los clientes · <b>4 muertos</b> —tres hombres y una mujer, " + RES + "— y <b>3 heridos</b>, por titular de seis medios (🔴 en su ventana) · más de 30 casquillos de varios calibres, " + RES + " · <b>cero detenidos</b> · <b>FGE Michoacán</b> investiga una disputa entre células, " + RES,
  panel="Ataque a un bar: <b>4 muertos</b> y <b>3 heridos</b>", inst="SSP Michoacán <span class=\"muted-note\">(por cita)</span>", nac="El Financiero · Latinus · EFE",
  conf="★★★☆☆", campo="hora y composición de las víctimas, solo por resumen", I=1, N=3, R=5, A=0,
  fechadas=["Latinus (2026/10/3)", "El Financiero (2026/10/04)", "PorEsto (2026/10/3)", "Diario de Yucatán (2026/10/03)", "Correo (2026/oct/04)"], desl="Zamora no figura en el índice: ARGOS 125, cuya ventana contenía el 2-oct, no lo publicó. 🔴 por homicidio múltiple"),
 dict(id="ARG-129-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-10-09", hora="noche del 9-oct a la mañana del 10 (solo por resumen)", orig="ARGOS 128", col_orig="verde",
  ent="Sinaloa", mun="Culiacán (col. Los Pinos)", dia="9-OCT, NOCHE",
  title="SINALOA · CULIACÁN — CATEO FEDERAL EN LOS PINOS: ARMAS Y ARTEFACTOS EXPLOSIVOS RETIRADOS POR EL GRUPO ANTIBOMBAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 128</code> · <code>COL. LOS PINOS, CALLE RÍO PAPALOAPAN</code> · el operativo inicia la noche del VIERNES 9-OCT y se prolonga hasta la mañana del sábado 10 (" + RES + ") · <b>Ejército, FGR y GN</b> aseguran una vivienda · armas y artefactos explosivos, retirados por el grupo antibombas de la GN, por titular · <code>SIN CIFRA PUBLICADA — CANTIDAD NO DETERMINADA</code> (🟢 en su ventana) · <b>sin detenidos publicados</b> · un ataque previo a la vivienda, " + RES + ", <code>NO ACREDITADO</code>",
  panel="Cateo con <b>armas y explosivos</b>, sin cifra; sin detenidos", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Universal · N+",
  conf="★★★☆☆", campo="armamento sin cifra; hora solo por resumen", I=0, N=2, R=3, A=1,
  fechadas=["Línea Directa (2026-10-10)"], desl="Los Pinos no figura en el índice. Inicio dentro de la ventana de ARGOS 128, que no lo publicó. Blog del Narco: <code>NO OFICIAL</code>"),
 dict(id="ARG-129-REC-003", estado="MX-NLE", region="Noreste", fecha="2026-10-10", hora="madrugada (solo por resumen)", orig="ARGOS 128", col_orig="verde",
  ent="Nuevo León", mun="General Escobedo (col. Unión Agropecuarios Lázaro Cárdenas del Norte)", dia="10-OCT, MADRUGADA",
  title="NUEVO LEÓN · ESCOBEDO — DOS DETENIDOS TRAS UNA RIÑA CON UN ARMA CORTA Y DROGA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 128</code> · <code>COL. UNIÓN AGROPECUARIOS LÁZARO CÁRDENAS DEL NORTE</code> · madrugada del SÁBADO 10-OCT (" + RES + ") · policía de Escobedo interviene en una riña en vía pública · <b>2 detenidos</b>, por titular · <b>1 arma corta</b>, <b>1 cargador</b> y <b>15 cartuchos</b>, marihuana y cocaína — cifras " + RES + " (🟢 en su ventana) · sin lesionados publicados · <code>NINGUNA FUENTE CON FECHA EN LA RUTA</code>",
  panel="<b>2 detenidos</b> con 1 arma corta, solo por resumen", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Milenio <span class=\"muted-note\">(Telediario)</span>",
  conf="★★☆☆☆", campo="ninguna fuente con fecha en la ruta; cifras solo por resumen", I=0, N=1, R=2, A=0,
  fechadas=[], desl="Escobedo figura en el índice (ARG-96-004, ARG-105-REC-001): otros hechos. Madrugada del 10-oct: anterior a la apertura de ARGOS 129"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-129-ARM-001", ficha="ARG-129-005", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Mazatlán (Las Porras)", c=[0,1,0,0,29,0,0,0,0,1], corp="Marina", conf="Bajo", color="amarillo", fecha="2026-10-10", hora="no fijada", fecha_txt="no publicada<br><span class=\"muted-note\">comunicado del 10-oct</span>", nota="Aseguramiento derivado de una agresión a personal naval; cifras SOLO POR RESUMEN de dos medios", fuentes=["La Razón (2026/10/10)", "Línea Directa (2026-10-10)"]),
 dict(id="ARG-129-ARM-002", ficha="ARG-129-006", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="sur del estado (Varados y Siqueros)", c=[0,0,0,0,0,0,0,7,0,0], corp="Marina", conf="Bajo", color="verde", fecha="2026-10-10", hora="no fijada", fecha_txt="no publicada<br><span class=\"muted-note\">comunicado del 10-oct</span>", nota="7 AEI inhabilitados, SOLO POR RESUMEN; capacidad explosiva no descrita; el armamento restante del comunicado no se atribuye por evento y no se integra", fuentes=["La Razón (2026/10/10)", "Línea Directa (2026-10-10)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [0, 1, 0, 0, 29, 0, 0, 7, 0, 1], TOT
assert cnt == {"rojo": 1, "amarillo": 4, "verde": 2}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 0, "verde": 2}, cnt_rec

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
head = head.replace("<title>ARGOS 128 — Reporte Nacional de Seguridad — 2026-10-10</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
    <div class="sem-item alto"><span class="dot"></span><span class="lbl">🔴 ROJO — ALTO IMPACTO</span><div class="val">{cnt["rojo"]} evento</div></div>
    <div class="sem-item medio"><span class="dot"></span><span class="lbl">🟡 AMARILLO — VIOLENCIA OPERATIVA</span><div class="val">{cnt["amarillo"]} eventos</div></div>
    <div class="sem-item bajo"><span class="dot"></span><span class="lbl">🟢 VERDE — ACCIONES INSTITUCIONALES</span><div class="val">{cnt["verde"]} eventos</div></div>
  </div>

  <div class="alerta contexto">
    <div class="flag">LO QUE DEBE HACER EL MANDO</div>
    <p>
      <b>1. EXIJA A PEMEX Y A LA FISCALÍA DE VERACRUZ EL SALDO OFICIAL DEL ATAQUE A LA REFINERÍA DE MINATITLÁN</b> (ARG-129-001) y revise la
      seguridad física de los accesos de las instalaciones del sur de Veracruz.
      <br><b>2. COTEJE CON EL COMUNICADO ÍNTEGRO DE LA SEMAR LA FECHA Y EL LUGAR DE CADA EVENTO DEL SUR DE SINALOA</b> (ARG-129-005, ARG-129-006):
      la agresión a marinos y los artefactos explosivos no tienen día publicado.
      <br><b>3. EXIJA A LA FISCALÍA DE MICHOACÁN LA CARPETA DEL ATAQUE AL BAR DE ZAMORA</b> (ARG-129-REC-001): ningún detenido publicado en las fuentes localizadas.
      <br><b>4. EXIJA A LA FISCALÍA DE OAXACA LA CIFRA OFICIAL DE VÍCTIMAS DEL ATAQUE DE PINOTEPA NACIONAL</b> (ARG-128-001) y la constancia de
      intervención del Mecanismo de Protección.
      <br><b>5. AUDITE EL INGRESO DE ARMAS AL PENAL EL CASTILLO</b> (ARG-127-004, ARG-128-004): la Fiscalía de Sinaloa investiga el ingreso; ningún
      responsable publicado.
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>10-oct 09:08 → 11-oct 08:58 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,29 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: los dos de hora publicada primero; después, los de hora no fijada</b>. <b>Cinco de siete</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <b>Total de armas integradas: {ARMAS}</b>, solo por resumen. <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento</b>; los 2 de Pachuca, sin armamento, no entran. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios: 3</b> —1 en el rojo, saldo contradicho, y 2 en los amarillos de Escuinapa—; <b>heridos: 2</b>, Minatitlán y Chipilo; <b>2 muertos y 3 heridos</b> si en Minatitlán son dos lesionados, versión de Pemex: <b>cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:4])
co2 = "\n".join(ficha(e) for e in E[4:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA ARMA CORTA EN HECHO PROPIO</code>"),
 tile(1, "Armas largas", TOT[1], "Las Porras, Mazatlán · <code>SOLO POR RESUMEN</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR INTEGRADA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "Las Porras, Mazatlán · <code>SOLO POR RESUMEN</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN CARGADOR ATRIBUIBLE POR EVENTO</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "Varados y Siqueros, sur de Sinaloa · <code>SOLO POR RESUMEN</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>{len(ARM)} filas de armamento de {len(ARM)} hechos</b> en <b>{len(ENT_ARM)} entidad</b>, las dos del comunicado de la SEMAR del 10-oct, <b>cifras solo por resumen</b>. <b>Totales por categoría: cálculo propio.</b>
    <code>EL ÚNICO HECHO ROJO DEL CORTE NO DEJÓ ARMAMENTO ASEGURADO PUBLICADO.</code>
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
    <b>Lectura regional</b> —2 filas, <b>cálculo propio</b>—: <b>Noroeste 2</b> · <b>Noreste 0</b> · <b>Occidente 0</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    <b>Sin evento cualitativo propio.</b> El armamento de las recuperaciones —Culiacán, sin cifra, y Escobedo— va en su ficha y <b>no entra en esta tabla</b>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA INTEGRABLE</code> · las candidatas del 10-oct, solo por medios, abajo</span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas quedan en <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto ordenado y publicado por fuente oficial</b> en la ventana</span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>de 21 revisadas más la FGR</b> · 11 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Sinaloa</b><br>Navolato (Villa Juárez)</td><td>Manuel Antonio «N» · <span class="muted-note">feminicidio agravado de una menor; hecho de octubre de 2023</span></td><td><b>80 años</b>, por titular de varios medios · tope de cumplimiento de 70, <code>SOLO POR RESUMEN</code></td><td>FGE Sinaloa</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>10-oct</b>; el título de la Fiscalía solo reproducido por un medio, sin boletín en el dominio oficial · <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br><span class="muted-note">municipio no verificado</span></td><td>Tres personas · <span class="muted-note">secuestro y homicidios</span></td><td><span class="muted-note">no verificada</span></td><td>FGE Nuevo León <span class="muted-note">(por cita)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · un medio nacional, <b>10-oct</b> en la ruta; contenido no verificado · <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
      <tr><td><b>Estado de México</b><br><span class="muted-note">varios municipios</span></td><td>Operación Enjambre · <span class="muted-note">27 personas en 16 sentencias, mayoría exservidores públicos</span></td><td><code>AÑOS CONTRADICHOS ENTRE MEDIOS, SOLO POR RESUMEN</code></td><td>FGJ Estado de México <span class="muted-note">(por cita)</span></td><td>Agregado publicado el <b>10-oct</b>; fecha de cada resolución no fijada; sin boletín · <code>NO INTEGRAR</code></td><td>Bajo</td></tr>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Tres hombres · <span class="muted-note">homicidio de tres turistas extranjeros, mayo de 2024</span></td><td><code>SIN PENA: VEREDICTO DE CULPABILIDAD DEL 9-OCT; INDIVIDUALIZACIÓN DE SANCIONES, 16-OCT</code></td><td>FGE Baja California</td><td><b>No es sentencia</b> hasta la audiencia de individualización · fuera de ventana</td><td>Medio</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas por primera vez, publicadas antes de la apertura</b>: FGR, nueve personas por secuestro en CDMX y Edomex · Tamaulipas, El Mante · Zacatecas, violencia familiar · Baja California, robo con violencia. <code>NO SE INTEGRAN: FUERA DE VENTANA.</code>
    <br><b>Candidatos heredados, siguen sin boletín oficial</b>: FGR Chihuahua y Sinaloa (9-oct) · León, 26 años 8 meses · NL, Condominios Constitución · Chihuahua, 8 años · Querétaro, Corregidora (boletín del 8-oct, hora no fijada). <code>NO SE INTEGRAN.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>21 de 32</b> · <b>FGR revisada: Sí</b> · BC, Dgo · Coah, Tamps, SLP, Zac · Jal, Col, Nay, Ags, Mich · Pue, Qro, Edomex, Mor, Tlax · Ver, Tab · Gro, Chis, Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>0</b></td></tr>
      <tr><td><b>Con sentencias publicadas en ventana solo por medios</b></td><td><b>3</b> fiscalías estatales: Sinaloa, Nuevo León y Estado de México (agregado)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>21</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>11</b>: BCS, Son, Chih, Sin · NL · Gto · CDMX, Hgo · Camp, Oax, QRoo</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 23 de 32</b> —BC, BCS, Son, Chih, Dgo, Coah, CDMX, Tlax y Camp, <code>NO REVISADA</code>— · <b>armamento: 9 de 32</b> —Sin, Zac, Col, Gto, Ags, Ver, Tab, Yuc y Camp; las otras 23, <code>NO REVISADA</code>— · <code>REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, SEDENA y SEMAR: <code>NO REVISADA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 9 y del 10-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 11-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR UN ROJO</b>: ARG-129-001 (Veracruz).
      <br><b>2.</b> <b>Contexto operativo</b>: cuatro amarillos (ARG-129-002 a ARG-129-005), tres de ellos en Sinaloa.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-129-006 y ARG-129-007; <b>ningún detenido publicado</b> por ARG-129-001, ARG-129-003 y ARG-129-004.
      <br><b>4.</b> <b>Sin acto nuevo en los seguimientos abiertos</b>: ARG-128-001, ARG-128-003, ARG-128-004 y ARG-125-051.
      <br><b>5.</b> <code>23 H 50 MIN; CINCO DE SIETE HECHOS CON FRONTERA DE VENTANA; BOLETÍN FEDERAL DEL 9 Y 10-OCT SIN INDEXAR; ARMAMENTO REVISADO EN 9 DE 32: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. ESCUINAPA CONCENTRA LA VIOLENCIA HOMICIDA DEL SUR DE SINALOA.</b> Dos homicidios en un mismo día, en un taller y en la zona centro (ARG-129-003,
      ARG-129-004), sin detenidos. Línea: <b>cotejo balístico</b> entre los dos hechos — hipótesis.
      <br><b>2. DISPAROS CONTRA LA POLICÍA PARA EVITAR UNA REVISIÓN VEHICULAR.</b> En Chipilo (ARG-129-002) los ocupantes de un vehículo sin placas disparan y lo
      abandonan. Línea: <b>origen del vehículo</b> y vínculo con robo de unidades.
      <br><b>3. ARSENALES CON EXPLOSIVOS EN VIVIENDA URBANA DE CULIACÁN.</b> Cateo con intervención del grupo antibombas (ARG-129-REC-002), sin cifra ni detenidos.
      Línea: <b>exigir el inventario</b> del aseguramiento — consistente con almacenamiento logístico, requiere validación.
      <br><b>4. NARCOMENUDEO CON ARMA EN ZONAS METROPOLITANAS.</b> Cateo en Pachuca (ARG-129-007) y riña con arma corta en Escobedo (ARG-129-REC-003).
      Línea: <b>puntos de venta</b> y su protección armada.
      <br><b>5. LA BRECHA ENTRE DETENCIÓN Y CONDENA SIGUE ABIERTA.</b> Ninguna sentencia integrable; las del 10-oct solo existen en medios, y el caso de Ensenada
      aún no tiene pena. Línea: <b>exigir el boletín oficial</b> de cada sentencia anunciada.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados/</b> — <code>NO REVISADA</code>: el buscador no devolvió páginas del dominio. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — SÁBADO 10-OCT: MINATITLÁN, CHIPILO Y ESCUINAPA", co1)
 + page("CRIMEN ORGANIZADO (II) — HECHOS DE HORA NO FIJADA: SUR DE SINALOA Y PACHUCA", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES: VENTANAS DE ARGOS 125 Y 128", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 10-oct 09:08 → 11-oct 08:58 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R))
