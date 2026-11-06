# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 148.
Uso: python3 tools/datos-argos-147.py <plantilla ARGOS 147> <salida>
Ventana: 5-nov 09:42 → 6-nov 07:30 CDMX. Archivo: argos-2026-11-06.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "148", "2026-11-06", "07:30"
CONSULTA = "2026-11-06, última búsqueda 07:41"
DUR = "21 h 48 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 09:42 DEL 5, ES DE LA VENTANA DE ARGOS 147 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-148-001", estado="MX-HID", region="Centro", color="rojo", impacto="grande", fecha="2026-11-05", hora="tarde (solo por resumen)", mu=1, he=0, cu=0, hk=16,
  ent="Hidalgo", mun="Pachuca (col. Real de Minas)", dia="5-NOV, POR RUTA",
  title="HIDALGO · PACHUCA — ASESINAN A UN POLICÍA ESTATAL, EXDIRECTOR DE LA POLICÍA DE HUEHUETLA, EN UN INTENTO DE ASALTO",
  hecho="Pachuca · <code>COL. REAL DE MINAS, POR TITULAR</code> · jueves 5-NOV, por ruta (La Silla Rota 2026/11/5: «muere policía estatal tras asalto en la colonia Real de Minas de Pachuca; 4 detenidos»; Síntesis 2026/11/05; Sociedad Noticias 2026/11/05) · " + AP + " · tarde, " + RES + " · " + RET + " · <b>1 muerto</b>: «policía estatal», por titular (La Silla Rota; Quadratín); «exdirector de la policía de Huehuetla», por titular (Sociedad Noticias; Milenio; El Universal) (🔴 víctima autoridad) · <code>CONDICIÓN DE AGENTE EN ACTIVO NO CONFIRMADA</code> · fuera de servicio; intento de asalto, " + RES + " · familiar acompañante privado de la libertad, " + RES + ": <code>CONTRADICHO</code> · detención de cuatro: ficha propia, ARG-148-007",
  panel="<b>Policía estatal, exdirector de la policía de Huehuetla, asesinado</b> en un intento de asalto", inst=SB, nac="La Silla Rota · Milenio · El Universal · N+", conf="★★★☆☆",
  campo="hora y circunstancia solo por resumen; condición de agente en activo no confirmada; ninguna fuente institucional", I=0, N=4, R=4, A=0,
  fechadas=["La Silla Rota (2026/11/5)", "Síntesis (2026/11/05)", "Sociedad Noticias (2026/11/05)"], estatus="Parcialmente corroborado", arm=None,
  desl="Real de Minas y Huehuetla no figuran en las cinco ediciones previas ni en el índice. Delito y detención en la misma ventana: dos fichas. Identidad de la víctima: medios, no se reproduce."),
 dict(id="ARG-148-002", estado="MX-PUE", region="Centro", color="rojo", impacto="grande", fecha="2026-11-05", hora="mañana o tarde (solo por resumen, contradicho)", mu=2, he=0, cu=0, hk=12,
  ent="Puebla", mun="Chietla (Villa de Atencingo)", dia="5-NOV, POR RUTA",
  title="PUEBLA · CHIETLA — ATAQUE ARMADO FRENTE AL BANCO DEL BIENESTAR DE ATENCINGO: DOS MUERTOS",
  hecho="Chietla · <code>VILLA DE ATENCINGO, FRENTE AL BANCO DEL BIENESTAR, POR TITULAR</code> · jueves 5-NOV, por ruta (Síntesis 2026/11/05; Retodiario 2026/11/05) · " + AP + " · <code>HORA CONTRADICHA</code>: mañana o tarde, " + RES + " · " + RET + " · <b>2 muertos</b>, por titular (Síntesis; N+; e-consulta; El Universal Puebla; Meganoticias: «cobra dos vidas»); «un hombre muerto y una mujer herida», por titular (Retodiario; Quadratín): la mujer murió después, " + RES + ": <code>SALDO CONTRADICHO</code> (🔴 homicidio múltiple) · un hombre adulto mayor y una mujer que vendía comida, " + RES + " · dos agresores en motocicleta, " + RES + " · la FGE investiga, " + RES + ": no es declaración · " + NOD,
  panel="<b>Ataque frente al Banco del Bienestar: 2 muertos</b> (saldo contradicho)", inst=SB, nac="N+ · El Universal · Meganoticias", conf="★★★☆☆",
  campo="hora contradicha; saldo contradicho entre titulares; ninguna fuente institucional", I=0, N=3, R=6, A=0,
  fechadas=["Síntesis (2026/11/05)", "Retodiario (2026/11/05)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chietla en el archivo de pendientes: ataque del domingo 18-oct (visto de ARGOS 137): otro hecho. Si el ataque fue por la mañana y antes de las 09:42 del 5, es de la ventana de ARGOS 147. Identidad de las víctimas: medios, no se reproduce."),
 # ======================= AMARILLOS
 dict(id="ARG-148-003", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-05", hora="tarde, ~15:00 o ~18:00 (solo por resumen)", mu=0, he=0, cu=0, hk=15,
  ent="Sinaloa", mun="Navolato (Las Trancas)", dia="5-NOV, POR RUTA",
  title="SINALOA · NAVOLATO — ENFRENTAMIENTO ENTRE MILITARES Y CIVILES ARMADOS EN LAS TRANCAS: TRES ABATIDOS",
  hecho="Navolato · <code>LAS TRANCAS, POR TITULAR</code> · jueves 5-NOV, por ruta (Línea Directa 2026-11-05: «se enfrentan elementos del Ejército Mexicano y civiles armados en Las Trancas»; Luz Noticias 2026-11-05) · " + AP + " · ~15:00 o ~18:00, " + RES + " · " + RET + " · <b>3 abatidos</b>, «presuntos gatilleros», por titular (Luz Noticias; Línea Directa: «confirman tres abatidos») · «agresión a militares», por titular (Meganoticias: «habría dejado»); patrullaje, " + RES + " (🟡 quién inició no acreditado por autoridad) · jeep, armamento y equipo táctico asegurados, sin cifra, " + RES + " · militares heridos: no informado · " + NOD,
  panel="<b>Enfrentamiento entre militares y civiles armados: 3 abatidos</b>", inst=SB, nac="Meganoticias · N+", conf="★★★☆☆",
  campo="quién inició, solo por medios; hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=5, A=0,
  fechadas=["Línea Directa (2026-11-05)", "Luz Noticias (2026-11-05)"], estatus="Parcialmente corroborado", arm="ARG-148-ARM-003",
  desl="Las Trancas no figura en las cinco ediciones previas ni en el índice. Navolato en el índice: ARG-130-005, ARG-132-001 y ARG-138-007 (La Palma, 🟡): otros hechos. Si Defensa acredita que el grupo agredió a militares en patrullaje, sube a 🔴."),
 dict(id="ARG-148-004", estado="MX-MEX", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-05", hora="tarde (solo por resumen)", mu=0, he=0, cu=0, hk=16.5,
  ent="Estado de México", mun="Naucalpan (Lomas Verdes)", dia="5-NOV, POR RUTA",
  title="ESTADO DE MÉXICO · NAUCALPAN — ABATEN A «EL GENERAL», SEÑALADO POR EL HOMICIDIO DEL COMISARIO MILTON MORALES",
  hecho="Naucalpan · <code>LOMAS VERDES, SOLO POR RESUMEN</code> · jueves 5-NOV, por ruta (La Jornada 2026/11/05: «abaten a El General, señalado por homicidio de Milton Morales»; Quinto Poder 2026/11/05; Noticias Veracruz 2026/11/05) · " + AP + " · tarde, " + RES + " · " + RET + " · <b>2 abatidos</b>, entre ellos el señalado como líder del Cártel Nuevo Imperio, por titular (Quinto Poder; Noticias Veracruz) · SSPC, AIC-FGR y CNI cumplían una orden de aprehensión y fueron recibidos a balazos, según el secretario de Seguridad, " + RES + " (🟡 la autoridad ejecuta una acción y es repelida) · un agente y un familiar heridos, " + RES + " · identidad del segundo abatido: no oficial",
  panel="<b>Abatido el señalado por el homicidio del comisario Milton Morales</b> y un acompañante", inst=SB, nac="La Jornada · El Universal · Infobae", conf="★★★☆☆",
  campo="secuencia del enfrentamiento y heridos solo por resumen; declaración del secretario solo por resumen", I=0, N=3, R=2, A=0,
  fechadas=["La Jornada (2026/11/05)", "Quinto Poder (2026/11/05)", "Noticias Veracruz (2026/11/05)", "Infobae (2026/11/06)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lomas Verdes y el Cártel Nuevo Imperio no figuran en las cinco ediciones previas ni en el índice. Homicidio de Milton Morales: 21-jul-2024, hecho anterior, no se recalifica. Abatidos: no entran en «muertos por agresión»."),
 dict(id="ARG-148-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-05", hora="noche (solo por resumen)", mu=1, he=0, cu=0, hk=21,
  ent="Sinaloa", mun="Culiacán (col. CNOP)", dia="5-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — PERSIGUEN Y ASESINAN A BALAZOS A UN HOMBRE EN LA COLONIA CNOP",
  hecho="Culiacán · <code>COL. CNOP, POR TITULAR</code> · jueves 5-NOV, por ruta (Línea Directa 2026-11-05: «a balazos privan de la vida a un hombre frente a un domicilio en la colonia CNOP») · " + AP + " · noche, " + RES + " · " + RET + " · <b>1 muerto</b>, por titular (Línea Directa; Los Noticieristas 2026/11: «corretean y asesinan a balazos a un hombre») (🟡 homicidio doloso único) · " + NOD,
  panel="<b>Hombre perseguido y asesinado a balazos</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Línea Directa (2026-11-05)", "Los Noticieristas (2026/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. CNOP no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-148-006", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-05", hora="mañana (solo por resumen)", mu=1, he=0, cu=0, hk=9,
  ent="Sinaloa", mun="Culiacán (col. Los Huizaches)", dia="5-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — HALLAN A UN HOMBRE ATADO DE MANOS Y ASESINADO A BALAZOS CERCA DE UNA CASETA MILITAR",
  hecho="Culiacán · <code>COL. LOS HUIZACHES, SOLO POR RESUMEN; CERCA DE UNA CASETA MILITAR, POR TITULAR</code> · jueves 5-NOV, por ruta (Línea Directa 2026-11-05: «atado de manos y asesinado a balazos hallan a un hombre cerca de una caseta militar») · " + AP + " · mañana, " + RES + " · " + RET + " · <b>1 muerto</b>, por titular; «con huellas de tortura», por titular (Quadratín Sinaloa, sin fecha en la ruta) (🟡 homicidio doloso único) · " + NOD,
  panel="<b>Hombre hallado atado y asesinado</b>, con huellas de tortura", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora del hallazgo solo por resumen (puede ser anterior a las 09:42); ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Línea Directa (2026-11-05)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Los Huizaches no figura en las cinco ediciones previas ni en el índice."),
 # ======================= VERDES
 dict(id="ARG-148-007", estado="MX-HID", region="Centro", color="verde", impacto="mediano", fecha="2026-11-05", hora="tarde (solo por resumen)", mu=0, he=0, cu=0, hk=17,
  ent="Hidalgo", mun="Pachuca (autopista México–Pachuca)", dia="5-NOV, POR RUTA",
  title="HIDALGO · PACHUCA — DETIENEN A CUATRO PERSONAS TRAS EL ASESINATO DEL POLICÍA EN REAL DE MINAS",
  hecho="Pachuca · jueves 5-NOV, por ruta (La Silla Rota 2026/11/5: «… 4 detenidos»; Sociedad Noticias 2026/11/05: «detienen a cuatro») · " + AP + " · " + RET + " · <b>4 detenidos</b>, por titular: cifra de medios · tres hombres y una mujer, uno herido de bala; localizados por el C5i en la autopista México–Pachuca, según la SSPH, " + RES + " · «dos detenidos», por titular (Criterio Hidalgo): versión previa · puestos a disposición del MP por homicidio y asalto, " + RES,
  panel="<b>4 detenidos tras el asesinato del policía</b> (ARG-148-001)", inst=SB, nac="La Silla Rota · Milenio", conf="★★★☆☆",
  campo="cifra de detenidos por titular de medios; declaración de la SSPH solo por resumen", I=0, N=2, R=3, A=0,
  fechadas=["La Silla Rota (2026/11/5)", "Sociedad Noticias (2026/11/05)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — aseguramiento no publicado",
  desl="Hecho delictivo: ARG-148-001."),
 dict(id="ARG-148-008", estado="MX-MIC", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-05", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Michoacán", mun="Morelia", dia="PUB. 5-NOV, POR RUTA",
  title="MICHOACÁN · MORELIA — FGE DETIENE A TRES PERSONAS E INCAUTA UN ARMA LARGA Y 119 CARTUCHOS EN CUATRO CATEOS",
  hecho="Morelia · publicado el jueves 5-NOV, por ruta (Esfera Noticias 2026/11/05: «detienen a tres personas e incauta arma de fuego, 119 cartuchos y narcóticos durante cuatro cateos») · " + AP + " · día de los cateos no fijado · " + RET + " · <b>3 detenidos</b>, por titular: cifra de medios («FGE detiene a tres personas», La Primera de AM) · <b>1 arma larga</b>, por titular (La Primera de AM); «arma de fuego», por titular (Esfera) · <b>119 cartuchos</b>, por titular (Esfera; Quadratín) · 2 cargadores, rifle Remington en Tiníjaro, " + RES + " · FGE de Michoacán con apoyo de Defensa, GN y Policía Morelia, " + RES + " · «tres cateos… mil 400 dosis», por titular (Contramuro): <code>POSIBLE DUPLICIDAD</code> con otra versión",
  panel="<b>4 cateos: 3 detenidos, 1 arma larga y 119 cartuchos</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día de los cateos no fijado; categoría del arma por titular de un medio; detenidos sin cifra de autoridad citada", I=0, N=0, R=6, A=0,
  fechadas=["Esfera Noticias (2026/11/05)", "RED113 (2026/11)"], estatus="Parcialmente corroborado", arm="ARG-148-ARM-001",
  desl="Morelia, cateos de la FGE: sin coincidencia de colonia ni cifras en las cinco ediciones previas. Detenidos fuera del conteo de armamento hasta cifra de autoridad."),
 dict(id="ARG-148-009", estado="MX-MIC", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-05", hora="no fijada", mu=0, he=0, cu=0, hk=11,
  ent="Michoacán", mun="Queréndaro, Cotija y Tacámbaro", dia="PUB. 5-NOV, POR RUTA",
  title="MICHOACÁN · QUERÉNDARO, COTIJA Y TACÁMBARO — EJÉRCITO Y GN ASEGURAN ARMAS, GRANADAS Y EXPLOSIVOS",
  hecho="Queréndaro, Cotija y Tacámbaro · publicado el jueves 5-NOV, por ruta (RED Michoacán 2026/11/05: «Ejército y GN decomisan armas, granadas, drogas y explosivos en tres municipios de Michoacán») · " + AP + " · día del aseguramiento no fijado · " + RET + " · «710 cartuchos», por titular de un solo medio (A Tiempo, sin fecha en la ruta) · desglose por municipio, " + RES + ": Queréndaro, 2 largas, 320 cartuchos, 12 cargadores; Cotija, 10 artefactos explosivos improvisados; Tacámbaro, 2 largas, 390 cartuchos, 11 cargadores y 3 granadas · Ejército y GN; entrega a la FGR, " + RES + " · sin detenidos publicados · <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code>",
  panel="<b>Armas, granadas y explosivos asegurados</b> en tres municipios; cifras solo por resumen", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="cifras solo por resumen o por un solo titular; día no fijado; republicaciones de una misma nota", I=0, N=0, R=1, A=0,
  fechadas=["RED Michoacán (2026/11/05)"], estatus="Pendiente de corroboración", arm="ARG-148-ARM-002",
  desl="Tacámbaro en el índice: ARG-109-001, ARG-109-ARM-001 y ARG-110-004 (agosto): otros hechos. Cotija y Tacámbaro, febrero de 2026 (Infobae 2026/02/03): otro hecho."),
 dict(id="ARG-148-010", estado="MX-CHP", region="Sureste", color="verde", impacto="grande", fecha="2026-11-05", hora="no fijada", mu=0, he=0, cu=0, hk=12.5,
  ent="Chiapas y Oaxaca", mun="aguas del Pacífico frente a Chiapas y Oaxaca", dia="PUB. 5-NOV, POR RUTA",
  title="PACÍFICO · CHIAPAS Y OAXACA — LA MARINA ASEGURA MÁS DE UNA TONELADA DE COCAÍNA: UN DETENIDO",
  hecho="Costas de Chiapas y Oaxaca · publicado el jueves 5-NOV, por ruta (El Financiero 2026/11/05; Proceso 2026/11/5; La Silla Rota 2026/11/5) · " + AP + " · día de las operaciones no fijado · " + RET + " · <b>más de una tonelada de cocaína</b> y <b>1 detenido</b>, por titular (El Financiero: «aseguran más de una tonelada… hay un detenido») · anuncio del secretario de Seguridad, por titular (La Silla Rota: «…: Harfuch»): declaración nombrada · «golpe de 273 millones de pesos», por titular (Proceso) · 1,149 kg en 32 bultos, dos operaciones, " + RES + " · Semar",
  panel="<b>Más de una tonelada de cocaína asegurada en el Pacífico; 1 detenido</b>", inst="Secretario de Seguridad" + PT, nac="El Financiero · Proceso · La Silla Rota", conf="★★★☆☆",
  campo="día de las operaciones no fijado; desglose solo por resumen; declaración del secretario por titular de un medio", I=1, N=3, R=0, A=0,
  fechadas=["El Financiero (2026/11/05)", "Proceso (2026/11/5)", "La Silla Rota (2026/11/5)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — aseguramiento de droga, no de armamento",
  desl="N+ «más de 4 toneladas de cocaína en embarcaciones en Chiapas y Oaxaca» (sin fecha; 13 o 16 detenidos): otro hecho, no se integra."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = []
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ND_ALL = list(range(10))
ARM = [
 dict(id="ARG-148-ARM-001", ficha="ARG-148-008", estado="MX-MIC", region="Occidente", color="verde", ent="Michoacán", mun="Morelia",
  fecha="2026-11-05", fecha_txt="pub. 5-nov; día de los cateos no fijado", hora="no fijada", c=[0, 1, 0, 0, 119, 0, 0, 0, 0, 0], nd=[0, 2, 3, 5, 6, 7, 8, 9], integra=True,
  corp="FGE Michoacán <span class=\"muted-note\">(por titular de medios)</span>", conf="Bajo",
  nota="1 larga (titular de La Primera de AM) y 119 cartuchos (titulares de Esfera y Quadratín); 2 cargadores, solo por resumen; 3 detenidos por titular de medios, sin cifra de autoridad: n/d; día no fijado: cláusula de retiro; ver ARG-148-008",
  fuentes=["Esfera Noticias (2026/11/05)", "Quadratín (sin fecha en la ruta)", "La Primera de AM (sin fecha en la ruta)"]),
 dict(id="ARG-148-ARM-002", ficha="ARG-148-009", estado="MX-MIC", region="Occidente", color="verde", ent="Michoacán", mun="Queréndaro, Cotija y Tacámbaro",
  fecha="2026-11-05", fecha_txt="pub. 5-nov; día no fijado", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="Ejército y GN <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: 4 largas, 710 cartuchos, 23 cargadores, 3 granadas y 10 AEI, solo por resumen o por un solo titular; ver ARG-148-009",
  fuentes=["RED Michoacán (2026/11/05)", "A Tiempo (sin fecha en la ruta)"]),
 dict(id="ARG-148-ARM-003", ficha="ARG-148-003", estado="MX-SIN", region="Noroeste", color="amarillo", ent="Sinaloa", mun="Navolato (Las Trancas)",
  fecha="2026-11-05", fecha_txt="5-nov, por ruta", hora="tarde (solo por resumen)", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="Defensa <span class=\"muted-note\">(por medios)</span>", conf="Bajo",
  nota="cualitativo: jeep, armamento y equipo táctico sin cifra, solo por resumen; sin detenidos; ver ARG-148-003",
  fuentes=["Línea Directa (2026-11-05)", "Luz Noticias (2026-11-05)"]),
]

TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
# sin ningún evento con cifra integrable no hay total verificable: todas las categorías n/d
ND = [True] * 10 if not any(a["integra"] for a in ARM) else [all(i in a.get("nd", []) for a in ARM if a["integra"]) for i in range(10)]
def tv(i, f=str): return "n/d" if ND[i] else f(TOT[i])
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["estado"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R); CU_REC = sum(r["cu"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
NRET = sum(1 for e in E if "SE RETIRA DE ESTE TOTAL" in e["hecho"])
HORAS = 21 + 48 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 1, 0, 0, 119, 0, 0, 0, 0, 0], (TOT, ND)
assert cnt == {"rojo": 2, "amarillo": 4, "verde": 4}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (5, 0, 0, 0, 0, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,46", DENS
assert (NAP, NFR, NRET) == (10, 0, 10), (NAP, NFR, NRET)
assert len(ENT) == 6 and len(ENT_ROJO) == 2, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-148-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-148-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-11-05" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-11-05", x["id"]

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
head = head.replace("<title>ARGOS 147 — Reporte Nacional de Seguridad — 2026-11-05</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA SSPH Y A LA PROCURADURÍA DE HIDALGO LA SITUACIÓN JURÍDICA DE LOS CUATRO DETENIDOS Y LA CONDICIÓN DE SERVICIO DE LA VÍCTIMA</b> (ARG-148-001 y -007).
      <br><b>2. SOLICITE A LA FISCALÍA DE PUEBLA EL SALDO OFICIAL, LA HORA Y LAS LÍNEAS DE INVESTIGACIÓN DEL ATAQUE DE ATENCINGO</b> (ARG-148-002).
      <br><b>3. SOLICITE A LA DEFENSA EL PARTE DE LAS TRANCAS: QUIÉN INICIÓ, ARMAMENTO ASEGURADO Y SITUACIÓN DEL PERSONAL</b> (ARG-148-003).
      <br><b>4. SOLICITE A LA FGE DE MICHOACÁN Y A LA FGR EL DESGLOSE OFICIAL DE LO ASEGURADO EN MORELIA, QUERÉNDARO, COTIJA Y TACÁMBARO, INCLUIDOS LOS 10 ARTEFACTOS EXPLOSIVOS</b> (ARG-148-008 y -009).
      <br><b>5. COTEJE LAS ARMAS ASEGURADAS EN NAUCALPAN CON LAS INVESTIGACIONES ABIERTAS DEL CÁRTEL NUEVO IMPERIO Y VIGILE LAS COLONIAS CNOP Y LOS HUIZACHES DE CULIACÁN</b> (ARG-148-004, -005 y -006).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>5-nov 09:42 → 6-nov 07:30 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>sin recuperaciones de alto impacto de la ventana anterior</b>
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
    <b>Armamento</b>: 1 arma larga y 119 cartuchos (Morelia, confianza Bajo, día no fijado); el resto, cualitativo; ningún detenido con cifra de autoridad · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas · <b>abatidos por la fuerza pública</b>: 5 (Navolato 3, Naucalpan 2), fuera de «muertos por agresión» · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b> (hora no fijada frente a las 09:42 del 5): todas. <b>Cálculo propio</b>.
    <br><b>Vistos, fuera de totales</b> — <b>de la ventana de ARGOS 147</b> (🟢 o 🟡, no se recuperan): Coscomatepec, Tetelcingo (12 cateos, 7 detenidos; inicio ~04:00 del 5, {RES}) · Edomex y CDMX, 38 cateos y 32 detenidos (anuncio «en plena madrugada» del 5, {RES}; = «Los Gigan», visto en ARGOS 147) · Mazatlán, Coto Residencial Atlántico (vivienda baleada antes de las 06:30 del 5, sin heridos) · Ensenada, «El Pariente» abatido y dos agentes estatales heridos (primeras horas del 4, {RES}; El Vigía 2026/11/5) · Tijuana, barbería de la Zona Centro, y Ciudad Juárez, col. Aldama (4-nov, 1 muerto cada uno) · Iztacalco, dos detenidos de la célula «Bebé Casasola» (4-nov; Infobae 2026/11/06) · <b>sin ruta fechada</b> — <code>SIN RUTA FECHADA — NO SE FICHA</code>: Chilpancingo, Urvan de la ruta Tribuna Nacional–Tomatal: «un muerto y 4 heridos», por titular (Quadratín Guerrero), o «un muerto y dos heridos», por titular (El Sur); 18:30 del jueves, {RES} · Reynosa, entre Puerta Sur y Nuevo México ITAVU: fosa, restos óseos y material calcinado (La Verdad 2026/11, sin día; ARG-140-008 en la misma zona) · <b>balances, no se integran</b>: Guanajuato y Sinaloa, «13 asesinatos en un día» (4-nov; diario.mx 2026/nov/05).
    <br><b>Seguimiento, fuera del semáforo</b>: <b>ARG-144-008 / ARG-145-REC-001 (Matamoros)</b>: «bala que mató a la niña Aranza salió de helicóptero de Guardia Estatal: Fiscalía», por titular (Proceso 2026/11/5); tirador no identificado · <b>ARG-147-001 (Cuernavaca)</b>: sin detenidos; la Fiscalía de Morelos podría citar a regidores y magistrados, {RES} · <b>ARG-147-010 (Mazatlán)</b>: día 4-nov fijado (Luz Noticias 2026-11-04; Noroeste, «el miércoles») · <b>ARG-147-REC-001 (Champotón)</b>: «detienen a 2 presuntos implicados», por titular (Tribuna Campeche); sin cifra de autoridad · <b>Cihuatlán, Jal.</b>: dos vinculados a proceso por portación de armas (Red Metropolitana 2026/11/05); aseguramiento de fecha no fijada · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-148-{i:03d}"]) for i in (1, 2, 3, 4))
co2 = "\n".join(ficha(byid[f"ARG-148-{i:03d}"]) for i in (5, 6, 7))
co2b = "\n".join(ficha(byid[f"ARG-148-{i:03d}"]) for i in (8, 9, 10))
assert sorted(re.findall(r'id="(ARG-148-0\d\d)"', co1 + co2 + co2b)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
DSA = "Morelia 3 y Pachuca 4, por titulares de medios: sin cifra de autoridad"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "Morelia, confianza Bajo; Queréndaro y Tacámbaro: 4, solo por resumen"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "Morelia; Queréndaro y Tacámbaro: 710, un solo titular"),
 tile(4, "Cargadores", tv(5), "Morelia 2 y Michoacán 23, solo por resumen"),
 tile(5, "Granadas", tv(6), "Tacámbaro: 3, solo por resumen"),
 tile(6, "AEI", tv(7), "Cotija: 10, solo por resumen"),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: " + DSA),
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
    <div class="map-caption">Michoacán: 1 arma larga y 119 cartuchos integrados (Morelia); dos eventos cualitativos en la tabla.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> — ningún aseguramiento con cifra publicada entre el 5-nov 09:42 y el 6-nov 07:30</td></tr>'
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
    <b>Lectura regional</b>: Occidente, 1 arma larga y 119 cartuchos (Michoacán); las demás regiones, sin arma integrada. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: Queréndaro, Cotija y Tacámbaro (ARG-148-ARM-002) y Navolato (ARG-148-ARM-003).
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>Cihuatlán, Jal.</b>: 1 corta, 4 largas, 28 cargadores, 778 cartuchos y 2 detenidos, {RES}; aseguramiento de fecha no fijada, publicado con la vinculación a proceso del 5-nov: <code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — NO SE INTEGRA</code> · <b>Tequila, Jal.</b>: vehículo con blindaje artesanal y 10 cartuchos (Potosinoticias 2026/10/30): anterior a la ventana · <b>Edomex y CDMX, 38 cateos</b>: armas contradictorias (20, 10 o 5), ventana de ARGOS 147 · <b>Coscomatepec</b>: armas sin cifra, ventana de ARGOS 147 · <b>boletín federal de acciones del 4-nov</b> (Milenio; RED113; Tallapolítica): ventana de ARGOS 147 · <b>acciones del 5-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code>.
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
      <tr><td><b>Tabasco</b><br>Paraíso</td><td>Portación de arma de uso exclusivo; exsubdirector de Seguridad Pública municipal; procedimiento abreviado; <b>1 sentenciado</b>, por titular · <b>nuevo en ARGOS 148</b></td><td>«2 años», por titular (Quadratín); 2 años 8 meses, {RES}: <code>CIFRA CONTRADICHA</code></td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · comunicado no leído; notas sin fecha en la ruta; fecha de la sentencia no fijada</td><td>Bajo</td></tr>
      <tr><td><b>Oaxaca</b><br>San Antonio de la Cal</td><td>Secuestro agravado (2011); 2 sentenciados · candidato de ARGOS 147</td><td>157 años, por titular del boletín 2,948 en el listado de <code>portal.fgeo.gob.mx</code> {RES}; 157 años 6 meses por suma, {RES}: <code>CIFRA CONTRADICHA</code></td><td>FGE Oaxaca</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · URL individual del boletín no obtenida; publicado el 4-nov (ventana de ARGOS 147)</td><td>Bajo</td></tr>
      <tr><td><b>Chiapas · NL · Coah</b></td><td>Palenque, feminicidio, 65 años (El Sol del Soconusco 2026/11/04) · Los Ramones, FGR, más de cinco años (MVS 2026/11/4) · Saltillo–Monclova, FGR, 7 años (La Prensa de Coahuila 2026/11/04) · <b>publicados el 4-nov</b></td><td>Por titular de medios</td><td>FGE Chiapas y FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · ventana de ARGOS 147; sin boletín del dominio</td><td>Bajo</td></tr>
      <tr><td><b>BC · Jal · Pue · Edomex · Zac · Coah · Hgo</b></td><td>Tecate · Mexicali · Jalisco (dos feminicidas) · Huejotzingo (posible homónimo) · Ecatepec · Fresnillo · Ramos Arizpe · Tulantepec (audiencia del 5-nov: sin resultado indexado) · <b>candidatos anteriores</b></td><td>Ver ARGOS 147 · <code>HEREDADO — NO REVERIFICADO</code></td><td>Fiscalías estatales y FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín del dominio en la ventana</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGE Colima (3-nov) · FGE Durango (5-sep) · FGE Querétaro (22-sep) · FGE Guerrero (12-ago) · FGE Quintana Roo (18-oct) · FGE Jalisco (19-oct). <code>NO SE INTEGRAN</code>. <b>Cihuatlán, Jal.</b>: vinculación a proceso, no sentencia.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio: <code>fgr.org.mx</code> solo devolvió listados sin fecha · comunicados vistos solo en resúmenes del buscador</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>19 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · Sin, Dgo · Tamps, SLP · Jal, Col, Nay, Ags, Mich, Gto · Hgo, Qro · Ver, Tab · Gro, Oax, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>19</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio de la fiscalía no confirmado</b></td><td><b>2</b>: Coah y Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>11</b>: BC, BCS, Son, Chih · NL, Zac · CDMX, Edomex, Pue, Mor, Tlax</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 6-nov 07:30: código <code>000</code> (proxy: conexión rechazada)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 20 entidades; solo consulta amplia en 12 —BCS, Dgo · Coah · Jal, Col, Nay, Ags · CDMX, Mor, Qro · Oax, Chis— · <b>armamento: 22 de 32 por dominio oficial</b> —Chih · NL, SLP, Zac, Tamps · Jal, Ags, Mich, Gto · Pue, Mor, Tlax, Hgo, Qro · Ver, Tab · Gro, Oax, Chis, Yuc, QRoo, Camp—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · dominio sin páginas: Nay · <code>NO REVISADA</code> (9): BC, BCS, Son, Sin, Dgo · Coah · Col · CDMX, Edomex</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 4-nov</b>: existe (Milenio; RED113; Tallapolítica): ventana de ARGOS 147 · <b>acciones del 5-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio y al cierre · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 6-NOV 07:30: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Dos rojos propios en dos entidades</b> (cálculo propio), por víctima autoridad y homicidio múltiple. <b>Descenso del riesgo nacional frente a ARGOS 147</b>: 0,09 rojos por hora (2 en {DUR}), frente a 0,15 en ARGOS 147 (cálculo propio).
      <br><b>2.</b> <b>Centro</b> concentra los dos rojos (Hidalgo y Puebla: ARG-148-001 y -002), ambos con condición de la víctima o saldo por confirmar.
      <br><b>3.</b> <b>Violencia operativa</b>: cuatro amarillos en dos entidades, con 5 abatidos por la fuerza pública en dos enfrentamientos (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: cuatro verdes; 1 arma larga y 119 cartuchos integrados; ninguna sentencia integrable (cálculo propio; totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()}: LOS DIEZ HECHOS PUBLICADOS EL DÍA DE APERTURA SIN HORA, CON CLÁUSULA DE RETIRO; SIN BOLETÍN FEDERAL DEL 5-NOV INDEXADO. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. ENFRENTAMIENTOS CON LA FUERZA PÚBLICA EN SINALOA Y EL ESTADO DE MÉXICO EL MISMO DÍA: 5 ABATIDOS</b> (cálculo propio; ARG-148-003 y -004); en Naucalpan, el objetivo era el señalado por el homicidio de un mando policial; vínculo no acreditado. Línea: <b>solicitar la balística de las armas aseguradas y cruzarla con las investigaciones del Cártel Nuevo Imperio</b>.
      <br><b>2. EXMANDO POLICIAL MUNICIPAL ASESINADO EN UN INTENTO DE ASALTO, CON ANTECEDENTE DE SECUESTRO EN 2022, POR <i>SLUG</i> (EFFETÁ)</b> (ARG-148-001 y -007). Línea: <b>verificar si el móvil fue robo o ataque dirigido y solicitar la situación de su protección previa</b>.
      <br><b>3. MICHOACÁN: GRANADAS, ARTEFACTOS EXPLOSIVOS IMPROVISADOS Y ARMAS LARGAS EN TRES MUNICIPIOS, SOLO POR RESUMEN</b> (ARG-148-009): consistente con capacidad explosiva distribuida en el centro y occidente del estado; requiere validación. Línea: <b>solicitar el dictamen de los 10 AEI de Cotija</b>.
      <br><b>4. CULIACÁN: VÍCTIMA ATADA Y CON HUELLAS DE TORTURA CERCA DE UNA CASETA MILITAR, POR TITULAR</b> (ARG-148-006). Línea: <b>vigilar las colonias Los Huizaches y CNOP y solicitar a la FGE de Sinaloa causa y antecedentes</b>.
      <br><b>5. RUTA MARÍTIMA DEL PACÍFICO SUR: MÁS DE UNA TONELADA DE COCAÍNA FRENTE A CHIAPAS Y OAXACA, POR TITULAR</b> (ARG-148-010). Línea: <b>solicitar a la Semar el punto de aseguramiento, el tipo de embarcación y la nacionalidad del detenido</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>; lectura directa no disponible · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO Y ENFRENTAMIENTOS: PACHUCA, ATENCINGO, NAVOLATO Y NAUCALPAN", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA EN CULIACÁN Y DETENCIONES EN PACHUCA", co2)
 + page("CRIMEN ORGANIZADO (III) — ACCIONES INSTITUCIONALES: MICHOACÁN Y PACÍFICO SUR", co2b)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if a["integra"] and any(a["c"]))
script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
assert f'const CONSULTA_TXT = "{CONSULTA}";' in script
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 147 con WINDOW_DAYS = 2"
# la ventana de 148 también toca dos fechas (5 y 6-nov): sin reemplazo
assert "WINDOW_DAYS = 2;" in script  # la ventana toca dos fechas de calendario (5 y 6-nov)
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
