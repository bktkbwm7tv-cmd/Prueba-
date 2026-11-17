# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 153.
Uso: python3 tools/datos-argos-153.py <plantilla ARGOS 152> <salida>
Ventana: 16-nov 10:30 → 17-nov 11:34 CDMX. Archivo: argos-2026-11-17.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "153", "2026-11-17", "11:34"
CONSULTA = "2026-11-17, última búsqueda __CONSULTA__"
DUR = "25 h 04 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 10:30 DEL 16, ES DE LA VENTANA DE ARGOS 152 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
PUB = "Publicado el día de apertura sin hora por fragmento: se integra en esta edición, la primera que lo ve."
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-153-001", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-17", hora="~09:00 (solo por resumen)", mu=1, he=1, cu=0, hk=9,
  ent="Guanajuato", mun="Santiago Maravatío (carretera Salvatierra–Yuriria, tramo de Casacuarán)", dia="MAR 17-NOV, POR RUTA",
  fecha_txt="martes 17-nov, por ruta; ~09:00, solo por resumen",
  title="GUANAJUATO · SANTIAGO MARAVATÍO — EMBOSCAN A DOS POLICÍAS MUNICIPALES AL SALIR DE TURNO EN LA CARRETERA SALVATIERRA–YURIRIA: UNO MUERTO Y OTRO GRAVE",
  hecho="Carretera Salvatierra–Yuriria · <code>TRAMO CERCANO A CASACUARÁN, YURIRIA</code>, " + RES + " · martes 17-NOV, por ruta (Noticieros en Línea 2026/nov/17: «emboscan a policías de Santiago Maravatío tras salir de turno; uno muere y otro queda grave») · ~09:00, " + RES + " · " + FR + " · <b>1 policía municipal muerto y 1 herido grave</b>, por titular (🔴 víctima autoridad) · fuera de servicio, «tras salir de turno», por titular; se dirigían a Yuriria, " + RES + " · «Santiago Maravatío: asesinan a policía tras ataque Salvatierra-Yuriria», por titular (Telediario); «emboscan a policías y uno fallece en Yuriria», por titular (Notus) · agresores huidos; operativo de búsqueda; la FGE de Guanajuato inició la investigación, " + RES + " · " + NOD,
  panel="<b>Emboscada a policías municipales: 1 muerto y 1 herido grave</b>", inst=SB, nac="Telediario", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["Noticieros en Línea (2026/nov/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Santiago Maravatío no figura en las ediciones previas; Maravatío, Mich. (ARG-136-008): otro hecho. Emboscada de septiembre de 2024 en el mismo corredor: otro hecho; «fallecen dos policías de Santiago Maravatío…» (Agoragto, sin fecha en la ruta), posiblemente de 2024: no se integra. Identidades: no publicadas."),
 dict(id="ARG-153-002", estado="MX-NAY", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-16", hora="tarde (solo por resumen)", mu=0, he=0, cu=7, hk=16,
  ent="Nayarit", mun="Acaponeta (brecha a La Guásima, autopista Tepic–Mazatlán)", dia="LUN 16-NOV, POR RUTA",
  fecha_txt="hallazgo lunes 16-nov, por ruta; tarde, solo por resumen",
  title="NAYARIT · ACAPONETA — HALLAN SIETE CUERPOS DE HOMBRES ENVUELTOS EN PLÁSTICO EN UNA BRECHA JUNTO A LA AUTOPISTA TEPIC–MAZATLÁN",
  hecho="Acaponeta · <code>BRECHA HACIA LA GUÁSIMA, AUTOPISTA TEPIC–MAZATLÁN, KM 111</code>, " + RES + " · hallazgo lunes 16-NOV, por ruta (MVS 2026/11/16: «hallan 7 cuerpos en Nayarit cerca de la autopista Tepic-Mazatlán»; NTV 2026/11/16: «confirma Fiscalía de Nayarit que los siete cuerpos hallados en Acaponeta son hombres») · tarde, " + RES + " · " + AP + " · <b>7 cuerpos de hombres</b>, por titular (🔴 hallazgo de restos humanos) · envueltos en bolsas de plástico, por titular (RED Michoacán 2026/11/17: «¡Hallan siete cuerpos envueltos en bolsas de plástico en Acaponeta, Nayarit!») · al menos tres semanas de fallecidos, por titular (Infobae 2026/11/17); entre una y tres, " + RES + " · causa de muerte no determinada; identidades no establecidas; posible traslado desde otro sitio, " + RES + " · Fiscalía de Nayarit, comunicado 044/2026, " + RES + " · " + NOD,
  panel="<b>Hallazgo de 7 cuerpos</b> de hombres, embolsados", inst="Fiscalía de Nayarit <span class=\"muted-note\">(por titular de medio)</span>", nac="MVS · Infobae · La Razón · Aristegui", conf="★★★☆☆",
  campo="hora del hallazgo solo por resumen; comunicado institucional no leído", I=1, N=4, R=4, A=1,
  fechadas=["MVS Noticias (2026/11/16)", "NTV (2026/11/16)", "Infobae (2026/11/17)", "La Razón (2026/11/17)", "RED Michoacán (2026/11/17)", "Potosinoticias (2026/11/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Acaponeta figura por ARG-132-REC-004 (km 112+600, tres cuerpos, octubre): otro hecho, mismo corredor. La nota de Infobae mezcla datos de otro caso: no se usan. Origen de las víctimas en Sinaloa, solo por medios: no confirmado. Cuerpos sin causa de muerte informada: se cuentan aparte de los muertos por agresión. Blog del Narco, NO OFICIAL."),
 dict(id="ARG-153-003", estado="MX-CMX", region="Centro", color="rojo", impacto="grande", fecha="2026-11-16", hora="primeras horas del 16 o noche del 15 (solo por resumen)", mu=2, he=1, cu=0, hk=2,
  ent="Ciudad de México", mun="Azcapotzalco (col. San Pedro Xalpa)", dia="LUN 16-NOV, POR TITULAR",
  fecha_txt="lunes 16-nov, por titular; primeras horas del 16 o noche del 15, solo por resumen",
  title="CIUDAD DE MÉXICO · AZCAPOTZALCO — ATACAN A BALAZOS UN AUTOMÓVIL EN SAN PEDRO XALPA: DOS MUERTOS Y UN HERIDO",
  hecho="Azcapotzalco · <code>COL. SAN PEDRO XALPA, CATARINO BENAVIDES Y 23 DE ABRIL</code>, " + RES + " · lunes 16-NOV, por titular (N+: «Balacera Hoy 16 de Noviembre 2026: en Azcapotzalco Deja Dos Muertos y un Herido») · primeras horas del lunes 16 o noche del 15, " + RES + " · " + AP + " · " + RET + " · <b>2 muertos</b>, por titular (🔴 homicidio múltiple) · heridos: 1, por titular (El Universal: «balacera en Azcapotzalco deja dos personas muertas y una herida»; N+), frente a 2, por titular (TV Azteca: «Mientras dormía: Balacera en Azcapotzalco deja dos muertos y dos heridos…»): <code>CIFRA DE HERIDOS CONTRADICHA — SE INTEGRA 1, MÍNIMO COINCIDENTE</code> · «acribillan a 3 hombres dentro de automóvil», por titular (Diario Basta 2026/11/17): los tres ocupantes, mismo hecho · agresores en otro vehículo, más de 20 disparos; huida, " + RES + " · SSC y FGJCDMX, diligencias e indicios balísticos, " + RES + " · «un detenido» en el encabezado de un medio, no sostenido en el texto: no se integra · " + NOD,
  panel="<b>Ataque a un automóvil: 2 muertos y 1 herido</b>", inst=SB, nac="El Universal · N+ · TV Azteca", conf="★★★☆☆",
  campo="hora solo por resumen, apunta a antes de la apertura; ninguna fuente institucional", I=0, N=3, R=4, A=0,
  fechadas=["Diario Basta (2026/11/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Pedro Xalpa no figura en las ediciones previas; Azcapotzalco, por ARG-134-009 y -014 (col. Pasteros, octubre): otro hecho. El titular de N+ fecha la página, no fija la hora. Identidades: no publicadas."),
 dict(id="ARG-153-004", estado="MX-CHH", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-16", hora="no fijada", mu=2, he=1, cu=0, hk=20,
  ent="Chihuahua", mun="Ciudad Juárez (Puerto de Anapra)", dia="LUN 16-NOV, POR RUTA",
  fecha_txt="lunes 16-nov, por ruta; hora no fijada",
  title="CHIHUAHUA · CIUDAD JUÁREZ — SEGUNDO DOBLE HOMICIDIO EN PUERTO DE ANAPRA EN MENOS DE 24 HORAS: DOS HOMBRES MUERTOS Y UNO HERIDO",
  hecho="Ciudad Juárez · <code>PUERTO DE ANAPRA</code>, por titular · lunes 16-NOV, por ruta (El Diario de Chihuahua 2026/nov/16: «asesinan a dos en Juárez; segundo doble homicidio en menos de 24 horas»; El Bordo 20261116: «asesinan a dos hombres y lesionan a otro en Anapra») · hora no fijada · " + AP + " · <b>2 hombres muertos y 1 herido</b>, por titular (🔴 homicidio múltiple) · «matan a dos y hieren a uno a balazos en Puerto de Anapra», por titular (Puente Libre, ruta del 17-nov) · SSPM de Juárez, " + RES + " · tercer homicidio en la colonia —hombre baleado y vivienda incendiada—, día no fijado: no se suma · mismos agresores, según un solo medio y fuente extraoficial: <code>VÍNCULO NO ACREDITADO</code> · " + NOD,
  panel="<b>Doble homicidio: 2 muertos y 1 herido</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada frente a la apertura; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["El Diario de Chihuahua (2026/nov/16)", "El Bordo (20261116)", "Puente Libre (17-nov-2026)"], estatus="Parcialmente corroborado", arm=None,
  desl="Anapra figura por ARG-152-007 (pareja atacada el domingo 15): otro hecho, del día anterior; el titular de El Diario lo distingue como segundo. Identidades: no publicadas."),
 # ======================= AMARILLOS
 dict(id="ARG-153-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-16", hora="~23:30 (solo por resumen)", mu=1, he=2, cu=0, hk=23,
  ent="Sinaloa", mun="Mazatlán (fracc. Los Magueyes)", dia="LUN 16-NOV, POR TITULAR",
  fecha_txt="noche del lunes 16-nov, por titular; ~23:30, solo por resumen",
  title="SINALOA · MAZATLÁN — HOMBRE ARMADO DISPARA CONTRA UN CONVIVIO EN LOS MAGUEYES: UN MUERTO Y DOS HERIDOS",
  hecho="Mazatlán · <code>FRACC. LOS MAGUEYES, VIVIENDA</code>, " + RES + " · noche del lunes 16-NOV, por titular (Reporte18: «deja noche del lunes dos asesinatos en Mazatlán») · ~23:30, " + RES + " · publicación 17-NOV, por ruta (Luz Noticias 2026-11-17: «ataque armado deja un muerto y dos heridos en Los Magueyes, Mazatlán»; Línea Directa 2026-11-17: «hombre armado irrumpe y dispara durante convivio en Mazatlán; hay un muerto y dos heridos») · <b>1 hombre muerto y 2 heridos</b>, por titular (🟡 homicidio doloso único) · una herida es mujer, " + RES + " · Ejército y Policía Municipal; la FGE integra carpeta, " + RES + " · otro homicidio de la misma noche (Infonavit Playas), sin ruta propia: no se suma · " + NOD,
  panel="Ataque a un convivio: <b>1 muerto y 2 heridos</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-11-17)", "Línea Directa (2026-11-17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Los Magueyes no figura en las ediciones previas. «Mazatlán suma siete asesinatos…» (Infobae 2026/11/16): balance, no fuente del hecho. Identidades: no publicadas."),
 dict(id="ARG-153-006", estado="MX-TAM", region="Noreste", color="amarillo", impacto="mediano", fecha="2026-11-16", hora="~11:40 (solo por resumen)", mu=0, he=2, cu=0, hk=11,
  ent="Tamaulipas", mun="Ciudad Victoria (exterior del Hospital La Salle)", dia="LUN 16-NOV, POR RUTA",
  fecha_txt="lunes 16-nov, por ruta; ~11:40, solo por resumen",
  title="TAMAULIPAS · CIUDAD VICTORIA — PERSECUCIÓN Y BALACERA FRENTE AL HOSPITAL LA SALLE: DOS HERIDOS",
  hecho="Ciudad Victoria · <code>EXTERIOR DEL HOSPITAL LA SALLE</code>, por titular · lunes 16-NOV, por ruta (ABC Noticias 2026/11/16: «ataque armado frente al Hospital La Salle provoca fuerte operativo en Ciudad Victoria»; MVS 2026/11/16: «reportan operativo tras persecución cerca de hospital en Tamaulipas») · ~11:40, " + RES + " · " + AP + " · persecución y disparos; una camioneta impacta en el área de urgencias, " + RES + " · <b>2 heridos</b>, por titular (N+: «…Provoca Pánico; Hay Dos Heridos») (🟡 confrontación derivada de un operativo; quién inició, no determinado) · Vocería de Seguridad de Tamaulipas: «Autoridades mantiene presencia policial en las inmediaciones del Hospital La Salle de Victoria», por titular de su mensaje, republicado; persecución de personas sospechosas, situación controlada, " + RES + " · el hospital: hechos fuera de sus instalaciones, " + RES + " · corporación: Defensa, GN, Guardia Estatal o Policía Investigadora, según el medio · detenciones: ver ARG-153-008",
  panel="<b>Persecución y balacera: 2 heridos</b>", inst="Vocería de Seguridad de Tamaulipas <span class=\"muted-note\">(mensaje republicado)</span>", nac="MVS · El Universal · Milenio · Infobae", conf="★★★☆☆",
  campo="hora solo por resumen; quién inició no determinado; mensaje institucional solo republicado", I=1, N=4, R=5, A=0,
  fechadas=["ABC Noticias (2026/11/16)", "MVS Noticias (2026/11/16)", "La Región (2026/11/16)", "Infobae (2026/11/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Hospital La Salle no figura en las ediciones previas; Ciudad Victoria, por aseguramientos de agosto (ARG-91-010, ARG-104-008): otros hechos. Bloqueos y vehículos incendiados en Matamoros y Río Bravo atribuidos a la detención, solo por resumen: no se fichan. Identidades: no publicadas."),
 dict(id="ARG-153-007", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-16", hora="tarde (solo por resumen)", mu=1, he=0, cu=0, hk=17,
  ent="Michoacán", mun="Zamora (col. Ferrocarril)", dia="LUNES, POR TITULAR; 16-NOV, POR RESUMEN",
  fecha_txt="lunes, por titular; 16-nov, DÍA SOLO POR RESUMEN; tarde, solo por resumen",
  title="MICHOACÁN · ZAMORA — ASESINAN A BALAZOS A UN HOMBRE EN LA COLONIA FERROCARRIL",
  hecho="Zamora · <code>COL. FERROCARRIL</code>, por titular (La Voz de Michoacán: «asesinan a balazos a un joven en la colonia Ferrocarril de Zamora»; PCM: «joven muere tras agresión armada en la Ferrocarril de Zamora») · lunes, por titular (Videa TV: «¡DOBLE ATAQUE EN ZAMORA! Un muerto y un herido en dos agresiones armadas el mismo lunes»); 16-NOV, " + DSR + " · tarde, " + RES + " · <b>1 hombre muerto</b>, por titular (🟡 homicidio doloso único) · la FGE investiga, " + RES + " · otra agresión el mismo día, col. Valencia 2a. sección, un joven herido (~13:25, " + RES + "): no se suma; vínculo no informado · " + NOD,
  panel="<b>Hombre asesinado</b> a balazos", inst=SB, nac="—", conf="★★☆☆☆",
  campo="día solo por resumen; ninguna ruta con fecha; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Colonia Ferrocarril no figura en las ediciones previas; Zamora, por hechos de agosto a octubre (ARG-98-002, ARG-129-REC-001, ARG-141-002): otros hechos. Identidades: medios, no se reproducen."),
 # ======================= VERDES
 dict(id="ARG-153-008", estado="MX-TAM", region="Noreste", color="verde", impacto="mediano", fecha="2026-11-16", hora="~11:40 (solo por resumen)", mu=0, he=0, cu=0, hk=11,
  ent="Tamaulipas", mun="Ciudad Victoria (Hospital La Salle)", dia="LUN 16-NOV, POR RUTA",
  fecha_txt="lunes 16-nov, por ruta; ~11:40, solo por resumen",
  title="TAMAULIPAS · CIUDAD VICTORIA — DOS DETENIDOS TRAS LA PERSECUCIÓN FRENTE AL HOSPITAL LA SALLE; CAPTURA DE UN PRESUNTO JEFE REGIONAL, NO CONFIRMADA",
  hecho="Ciudad Victoria · <code>HOSPITAL LA SALLE</code>, por titular · lunes 16-NOV, por ruta (Potosinoticias 2026/11/16; Infobae 2026/11/17: persecución y balacera que terminan con una detención, por titular) · " + AP + " · <b>2 detenidos</b>: «hay dos presuntos detenidos», por titular (El Universal) · identidades y circunstancias no informadas por autoridad, " + RES + " · captura de un presunto jefe regional del Cártel del Golfo, por titular de medios (Potosinoticias; Excélsior: «Presumen detención…»): <code>IDENTIDAD NO CONFIRMADA POR AUTORIDAD</code> · " + NDA + " · armamento asegurado: no publicado",
  panel="<b>2 detenidos</b> tras la persecución; identidad no confirmada", inst=SB, nac="El Universal · Infobae · Excélsior", conf="★★★☆☆",
  campo="cifra de detenidos solo por titular de medio; identidad no confirmada; ninguna fuente institucional", I=0, N=3, R=2, A=1,
  fechadas=["Potosinoticias (2026/11/16)", "Infobae (2026/11/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Mismo operativo que ARG-153-006: la detención se ficha aparte. Alias: medios, no se reproduce. Blog del Narco, NO OFICIAL."),
]
R = []
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
HORAS = 25 + 4 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
assert TOT == [0] * 10 and ND == [True] * 10, (TOT, ND)
assert cnt == {"rojo": 4, "amarillo": 3, "verde": 1}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0} and R == [], cnt_rec
assert (MU, HE, CU) == (7, 7, 7), (MU, HE, CU)
assert DENS == "0,32" and RPH == "0,16", (DENS, RPH)
assert (NAP, NFR, NRET) == (5, 1, 1), (NAP, NFR, NRET)
assert len(ENT) == 7 and len(ENT_ROJO) == 4, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-153-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-16" <= x["fecha"] <= "2026-11-17", x["id"]
    assert x["conf"] != "★★★☆☆" or len(x["fechadas"]) + (x["N"] + x["R"]) >= 2, x["id"]

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
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"] + (" · día solo por resumen" if "DÍA SOLO POR RESUMEN" in e.get("fecha_txt", "") else "")}

def arm_json(a):
    c = [("n/d" if i in a.get("nd", []) else v) for i, v in enumerate(a["c"])]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if sum(a["c"]) > 30 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 152 — Reporte Nacional de Seguridad — 2026-11-16</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE GUANAJUATO EL PARTE DE LA AGRESIÓN A LOS POLICÍAS MUNICIPALES DE SANTIAGO MARAVATÍO Y LAS MEDIDAS DE PROTECCIÓN PARA EL AGENTE HERIDO</b> (ARG-153-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE NAYARIT EL DICTAMEN DE CAUSA DE MUERTE Y EL AVANCE EN LA IDENTIFICACIÓN DE LAS VÍCTIMAS HALLADAS EN ACAPONETA</b> (ARG-153-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE LA CIUDAD DE MÉXICO LA HORA OFICIAL DEL ATAQUE DE SAN PEDRO XALPA Y EL REGISTRO DE SUS INDICIOS BALÍSTICOS</b> (ARG-153-003).
      <br><b>4. SOLICITE A LA FISCALÍA DE CHIHUAHUA, ZONA NORTE, EL ANÁLISIS CONJUNTO DE LOS HOMICIDIOS DE PUERTO DE ANAPRA</b> (ARG-153-004 y ARG-152-007).
      <br><b>5. SOLICITE A LA VOCERÍA DE SEGURIDAD DE TAMAULIPAS LA CONFIRMACIÓN OFICIAL DE LAS DETENCIONES DE CIUDAD VICTORIA Y SU PUESTA A DISPOSICIÓN</b> (ARG-153-008).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>16-nov 10:30 → 17-nov 11:34 CDMX</b> (<b>{DUR}</b>) · lun 16 (desde 10:30) · mar 17 (hasta 11:34) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>ninguna recuperación de ventanas anteriores</b>
  </p>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Entidad · Municipio</th><th>Hecho</th><th>Nivel de riesgo</th><th>Fuente institucional</th><th>Fuente nacional</th><th>Confianza</th><th>ARG-ID</th></tr></thead>
    <tbody>
{rows_own}
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
    <b>Armamento</b>: ningún aseguramiento de la ventana con cantidad publicada por titular o por autoridad · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas · <b>heridos</b>: {HE}; en Azcapotzalco, el mínimo coincidente · <b>cuerpos</b>: {CU} (Acaponeta), sin causa de muerte informada, aparte de los muertos por agresión · <b>detenidos</b>: 2 (Ciudad Victoria), solo por titular de medio, sin cifra de autoridad: n/d · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (Santiago Maravatío, publicado el día de cierre) · <b>totales sujetos a {NRET} cláusula de retiro</b> (Azcapotzalco: hora solo por resumen anterior a las 10:30).
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «Mazatlán suma siete asesinatos y nueve heridos tras 11 ataques armados… durante el fin de semana» (Infobae 2026/11/16) · «Lunes con 36 ejecutados» (Sol Yucatán) · «Suman ya 15 miembros de cabildo asesinados en un año» (La Razón 2026/11/16) · «Con más de 60 resoluciones judiciales y 45 imputaciones durante el fin de semana…» (Hoy Xalapa 2026/11/16) · «Quintana Roo registró un total de 299 personas detenidas en una semana» (PorEsto 2026/11/17) · «Detienen fuerzas del orden a 22 personas en pro de la seguridad» (Luces del Siglo 2026/11/17; operativos al 12-nov).
    <br><b>Vistos, fuera de totales</b> (sin ruta con día, fuente única o ventana anterior): Chilapa, Gro., col. Valle Dorado, comerciante asesinado, noche del lunes {RES}, fuente única sin fecha en la ruta · Cosoleacaque, Ver., fracc. Los Prados, hombre asesinado en un auto, lunes 16 {RES} · Zamora, col. Valencia 2a. sección, joven herido (~13:25 {RES}) · Emiliano Zapata, Mor., Tetecalita, hombre asesinado, martes {RES} · Apatzingán, comerciante asesinado, sin día en la ruta · Ciudad Juárez, Anapra, hombre baleado y vivienda incendiada, sin día · Mazatlán, Infonavit Playas, hombre muerto en el hospital, sin ruta propia · Matamoros y Río Bravo, bloqueos y vehículos incendiados, {RES} · <b>ventana de ARGOS 152</b>: Ensenada, ~75 kg de metanfetamina y 1 detenido (~01:00 del 16 {RES}; Periodismo Negro 2026/11/16) · San Juan Mixtepec, Oax., 1 muerto y varios heridos por un grupo armado (domingo 15 {RES}) · Champotón, persona sin vida en un domicilio (PorEsto 2026/11/15) · Morelia, dos detenidos armados en motocicleta (RED Michoacán 2026/11/15) · <b>ventana de ARGOS 151</b>, rojos sin hora por titular: Yautepec, Mor., 2 muertos tras una riña en una cabalgata (sábado 14 {RES}; Informador 20261116; La Silla Rota 2026/11/16) · Atotonilco el Alto, Jal., captura de un operador «tras agresión a elementos federales», por titular (Infobae 2026/11/15); ~15:55 del sábado 14 y patrullaje, {RES}.
    <br><code>FE DE ERRATAS — ARGOS 152</code>: <b>ARG-152-002</b> Tecate: dos víctimas halladas sin vida el lunes 16, por titular (Tribuna 2026/11/16: «hallan sin vida a agente de la FGE y a capitán retirado en Baja California; habían sido secuestrados»; Linderonorte 2026/11/16; Radar Tecate 2026/11/16); tres con vida; hallazgo ~02:00 del 16 {RES} · <b>ARG-152-007</b> Anapra: 2 muertos, por titular (El Diario de Chihuahua 2026/nov/17: «identifican a pareja asesinada en Anapra») · muertos de 152: 12 → <b>15</b>, sin cambio de color (cálculo propio) · <b>ARG-152-008</b> Calpulalpan: ~17:30 del 15 {RES}; «matan a golpes a campesino para robarle sus borregos, en Calpulalpan», por titular (Quadratín Tlaxcala) · <b>ARG-152-009</b>: cateos en la madrugada del 13 {RES} · <code>FE DE ERRATAS — ARGOS 151</code>: <b>ARG-151-002</b> Jolalpan: <b>3 muertos</b>, por dos titulares (Cinco Radio; e-consulta: «ataque armado en Jolalpan deja tres muertos; anuncian base de Guardia Nacional»).
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Cuernavaca (ARG-147-001)</b>: inicia el 17-nov la audiencia de vinculación del presunto autor material (UnoTV), resultado no publicado · <b>Zapopan (ARG-149-014 / -018)</b>: vinculación a proceso de 20 detenidos del operativo (Meganoticias, sin fecha en la ruta); los cinco escoltas, sin resolución individual atable · <b>Texhuacán (ARG-151-001)</b>: «…aún no hay detenidos» (Formato 7 2026/11/16) · <b>Tepehuacán (ARG-151-009)</b>: tres identificados, ningún detenido · <b>Tecate, Los Encinos (ARG-150-REC-001)</b>: un detenido en Tijuana por orden de aprehensión (En Línea BC 2026/11/16; captura del 10-nov {RES}); «cuádruple homicidio», por titular, frente a 3 muertos de la ficha: cifra por revisar · <b>Cajeme</b>: niña de seis años muerta y sus padres heridos; «suman 5 detenidos», por titular (El Heraldo de México 2026/11/13); día del ataque no fijado · <code>NO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
co1 = "\n".join(ficha(byid[f"ARG-153-{i:03d}"]) for i in (1, 2))
co2 = "\n".join(ficha(byid[f"ARG-153-{i:03d}"]) for i in (3, 4))
co3 = "\n".join(ficha(byid[f"ARG-153-{i:03d}"]) for i in (5, 6, 7, 8))
assert sorted(re.findall(r'id="(ARG-153-0\d\d)"', co1 + co2 + co3)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), NI),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), NI),
 tile(4, "Cargadores", tv(5), NI),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: ninguno con cifra de autoridad"),
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

assert ARM == []
arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
      <tr style="opacity:.72;"><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> · ningún aseguramiento de la ventana con día fijado y cantidad publicada por titular o por autoridad</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code>.
    <br><b>Lectura regional</b>: ninguna región con arma integrada. <b>Cálculo propio</b>.
    <br><code>BOLETÍN FEDERAL DE ACCIONES DEL 13, 14 Y 15-NOV: SIN RESULTADO INDEXADO EN VENTANA</code> (día suelto, rango y título, al inicio y al cierre) · «Gabinete de seguridad: resultados 16 de noviembre» (Milenio, ruta 16-nov-2026): agregado, no fija el día de cada acción.
    <br><code>VISTOS, NO INTEGRADOS — DÍA NO FIJADO</code>: Tlacotepec de Benito Juárez, Pue., localidad Tepetatera, Marina y Policía Municipal, 4 detenidos, 3 armas largas, 1 corta artesanal, 3 cargadores y 15 cartuchos {RES} (agregado federal) · Arteaga, 1 detenido con un arma larga, cartuchos y placas balísticas {RES} (agregado federal) · Galeana, N.L., 14 armas largas, un fusil calibre .50, una ametralladora, ~50 cargadores y más de 800 cartuchos {RES} · Sinaloa (Elota) y Michoacán, tres laboratorios de metanfetamina desmantelados por Marina, con armas y explosivos {RES} (Tus Buenas Noticias 2026/11/17) · Chihuahua, Aldama, 7 armas, 900 cartuchos, 32 cargadores y 12 artefactos explosivos {RES}, comunicados de la SSPE del 4 al 13-nov: anteriores a la ventana.
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
      <tr><td><b>Nuevo León</b><br>Monterrey</td><td>Homicidio; 1 sentenciado, por titular (MVS 2026/11/17: «sentencian a 25 años a homicida en Monterrey»)</td><td>25 años, por titular</td><td>Fiscalía de NL <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín en el dominio · publicado en la ventana</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>Monterrey (col. Bella Vista)</td><td>Homicidio calificado y delitos contra la salud {RES}; 1 sentenciado (MVS 2026/11/13); otro caso que el anterior {RES}</td><td>«Casi 26 años», por titular; <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>Fiscalía de NL <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín en el dominio · ventana de ARGOS 150</td><td>Bajo</td></tr>
      <tr><td><b>Sin novedad</b></td><td>Tabasco, boletín FGET 5119, 30 años por pederastia, Jalpa de Méndez (9-nov, listado del dominio; URL individual no identificada) · Veracruz, 88 años por secuestro agravado de nueve víctimas, juicio oral (Hoy Xalapa 2026/11/13; Formato 7 2026/11/13) · Champotón, 66 años 8 meses, procedimiento abreviado (PorEsto 2026/11/6); reparación del daño 7.2 o 7 millones, contradicha</td><td>—</td><td>—</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · ventanas anteriores</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>17 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BCS · NL, Tamps, Coah, Zac, SLP · Jal, Gto, Col, Nay · CDMX · Ver, Tab · Oax, Chis, Gro, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> por dominio · Monterrey, solo por medios</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>17</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio de la fiscalía no confirmado</b></td><td>Camp, cuarta edición (incluida en las 15 <code>NO REVISADA</code>)</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>15</b>: BC, Son, Chih, Sin, Dgo · Mich, Ags · Edomex, Mor, Pue, Tlax, Hgo, Qro · Camp, Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 17-nov 11:34: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 21 entidades, las nueve que solo tuvieron consulta amplia en 152 incluidas; solo consulta amplia en 11 —Dgo · NL, Zac, SLP · Jal · Edomex, Mor, Pue, Tlax, Hgo, Qro— · <b>armamento: 31 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (1): Mor</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 13, 14 y 15-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio y al cierre · acciones del 16: agregado de Milenio sin día por acción · último boletín diario indexado: acciones del 12-nov · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 17-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Cuatro rojos propios en cuatro entidades</b>: {RPH} rojos por hora (4 en {DUR}), frente a 0,21 en ARGOS 152 (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Occidente 2 · Centro 1 · Noroeste 1 · Noreste, Golfo y Sureste 0; ninguna recuperación de ventanas anteriores (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: tres amarillos (Sinaloa, Tamaulipas y Michoacán).
      <br><b>4.</b> <b>Respuesta institucional</b>: un verde (Tamaulipas) sin armamento integrable; ninguna sentencia integrable (totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()} SIN BOLETÍN FEDERAL DIARIO INDEXADO; CINCO DE OCHO HECHOS PUBLICADOS EL DÍA DE APERTURA SIN HORA FIJADA Y UN ROJO —2 DE LOS 7 MUERTOS— CON CLÁUSULA DE RETIRO: TOTALES NO COMPARABLES SIN MÁS. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. POLICÍAS MUNICIPALES ATACADOS FUERA DE SERVICIO EN EL SUR DE GUANAJUATO</b> (ARG-153-001): emboscada en el trayecto de regreso tras el turno; móvil y autores no informados; vínculo con otros ataques a policías del estado no acreditado. Línea: <b>vigilar los trayectos de policías municipales de Santiago Maravatío y Yuriria al cambio de turno</b>.
      <br><b>2. DEPÓSITO DE SIETE CUERPOS EN EL CORREDOR TEPIC–MAZATLÁN</b> (ARG-153-002): cuerpos embolsados con semanas de fallecidos, solo por resumen, son consistentes con traslado y abandono, no con ejecución en el sitio; origen de las víctimas no confirmado. Línea: <b>cruzar las identificaciones con los registros de personas desaparecidas de Sinaloa y Nayarit</b>.
      <br><b>3. REINCIDENCIA HOMICIDA EN PUERTO DE ANAPRA</b> (ARG-153-004, con ARG-152-007): dos ataques con dos muertos cada uno en menos de 24 horas en la misma colonia; vínculo entre hechos no acreditado. Línea: <b>vigilar Puerto de Anapra como foco de reincidencia en Ciudad Juárez</b>.
      <br><b>4. ATAQUE DESDE OTRO VEHÍCULO CONTRA OCUPANTES DE UN AUTOMÓVIL EN AZCAPOTZALCO</b> (ARG-153-003): más de 20 disparos, solo por resumen, son consistentes con un ataque dirigido; móvil no informado; vínculo no acreditado. Línea: <b>vigilar ataques contra vehículos en movimiento en Azcapotzalco y su límite con Naucalpan</b>.
      <br><b>5. OPERATIVO CON PERSECUCIÓN FRENTE A UN HOSPITAL EN CIUDAD VICTORIA</b> (ARG-153-006 y -008): presunta captura de un jefe regional, no confirmada por autoridad; bloqueos en Matamoros y Río Bravo, solo por resumen, vínculo no acreditado. Línea: <b>vigilar bloqueos y reacciones armadas en la frontera tamaulipeca en las 72 horas siguientes</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: EMBOSCADA A POLICÍAS Y HALLAZGO DE CUERPOS", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: HOMICIDIOS MÚLTIPLES EN CIUDAD DE MÉXICO Y CIUDAD JUÁREZ", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA Y ACCIONES INSTITUCIONALES", co3)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if a["integra"] and any(a["c"]))
assert "__" not in CONSULTA, "escribir la hora real de la última búsqueda"
script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
assert f'const CONSULTA_TXT = "{CONSULTA}";' in script
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert script.count("const EVENTOS_ARM = [\n" + ea + "\n];") == 1
# la ventana de 153 toca dos fechas de calendario (16 y 17-nov); la plantilla de 152 ya trae 2: sin reemplazo
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 152 con WINDOW_DAYS = 2"
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
