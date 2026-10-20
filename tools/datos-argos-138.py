# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 138: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-138.py <plantilla ARGOS 137> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "138", "2026-10-20", "07:06"
CONSULTA = "2026-10-20 07:06-09:30"
DUR = "20 h 01 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA: PUEDE SER ANTERIOR A LAS 11:05 DEL 19</code>"
FNF = "<code>FECHA DEL HECHO NO FIJADA DENTRO DEL 16 AL 18-OCT: PUBLICADO DURANTE EL CORTE</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-138-001", estado="MX-OAX", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-19", hora="~21:00 (solo por resumen)",
  ent="Oaxaca", mun="Juchitán de Zaragoza (colonia solo por resumen)", dia="19-OCT, NOCHE, DÍA SOLO POR RESUMEN",
  title="OAXACA · JUCHITÁN — ATAQUE ARMADO: DOS MUERTOS Y UN NIÑO HERIDO",
  hecho="Juchitán de Zaragoza · <code>COL. TOMÁS AQUINO, CALLE 12 DE OCTUBRE, SOLO POR RESUMEN</code> · noche del LUNES 19-OCT, ~21:00, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · <code>DÍA: UNA SOLA FUENTE (ADN SURESTE), SOLO POR RESUMEN</code>; titular de ADN Sureste con hora de actualización «23:10 h», sin día · <b>2 muertos</b>, por titulares (🔴) · heridos: <b>2 a 3</b>, por titulares (ADN Sureste 23:10 h y El Universal), <code>CONTRADICHO</code>; entre ellos <b>un niño</b> de 2 o 3 años, por titulares · un hombre que viajaba en motocicleta con su hijo, agredido, " + RES + " · trasladados al Hospital General Macedonio Benítez Fuentes, " + RES + " · <code>«MENOR DE 12 AÑOS» Y «NOCHE DEL MIÉRCOLES» EN OTRAS NOTAS DE JUCHITÁN: OTRO HECHO O DATO CONTRADICHO, NO SE INTEGRA</code> · sin comunicado de la Fiscalía de Oaxaca ni de la SSPC estatal, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos</b> y un niño herido",
  inst=SB, nac="El Universal", conf="★★☆☆☆",
  campo="día de una sola fuente y hora, solo por resumen; ninguna ruta con fecha; heridos contradichos", I=0, N=1, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Tomás Aquino no figura en las cinco ediciones previas ni en el índice. Títulos de Juchitán con «un menor gravemente herido» (Imparcial de Oaxaca, Vanguardia, ADN 23:00 h) no se cuentan: el del Imparcial de Oaxaca es del 3-jul-2026 según resumen del buscador, no leído: probable otro hecho. NO es el «panteón de Juchitán» visto en ARGOS 137 (domingo 18, Guardia Nacional herida, entidad contradicha) ni ARG-125-018 (aseguramiento del 2-oct). Comparte municipio y 2 muertos con el panteón; los separan día (domingo 18), hora (~18:30), lugar (panteón) y lesionado (Guardia Nacional)."),
 dict(id="ARG-138-002", estado="MX-TAB", region="Golfo", color="rojo", impacto="mediano", fecha="2026-10-19", hora="tarde del lunes (texto de Posta, URL sin fecha)",
  ent="Tabasco", mun="Cárdenas (predio junto a la carretera federal Huimanguillo–Cárdenas)", dia="19-OCT, HORA NO FIJADA",
  title="TABASCO · CÁRDENAS — LA FISCALÍA CONFIRMA UNA FOSA CLANDESTINA CON DOS CUERPOS",
  hecho="Cárdenas · <code>PREDIO JUNTO A LA CARRETERA FEDERAL HUIMANGUILLO–CÁRDENAS, SOLO POR RESUMEN</code> · hallazgo el LUNES 19-OCT, tarde, por texto de Posta (URL sin fecha); otra nota de Tabasco Hoy lo da el 20, " + RES + ": <code>DÍA CONTRADICHO</code> · <code>NINGUNA RUTA CON FECHA</code> · <b>fosa clandestina con 2 cuerpos</b>, por titulares (🔴) · la <b>FGE Tabasco confirma el hallazgo</b>, por titular de Tabasco Hoy · Policía de Investigación y peritos levantan indicios y muestras genéticas, " + RES + " · <b>dos jóvenes</b>, por titular de Posta; sexo y nombres solo en un medio regional no oficial: <code>NO SE REPRODUCEN</code> · <b>ningún detenido publicado</b> · <code>PUBLICACIÓN DEL 19-OCT SOLO POR RESUMEN; NINGUNA RUTA CON FECHA</code>",
  panel="Fosa clandestina: <b>2 cuerpos</b>",
  inst="FGE Tabasco <span class=\"muted-note\">(por titular)</span>", nac=NIN, conf="★★☆☆☆",
  campo="día del hallazgo por texto de una fuente sin fecha en la ruta; ninguna ruta con fecha", I=1, N=0, R=5, A=0,
  fechadas=[], estatus="Parcialmente corroborado", arm=None, fecha_txt="2026-10-19, tarde, por texto de Posta (URL sin fecha)",
  desl="La fosa de Cárdenas no figura en las cinco ediciones previas; Huimanguillo figura en ARG-120-015 (operativo de septiembre): otro hecho. NO es ARG-137-005 (restos con cartulinas en la carretera Villahermosa–Teapa)."),
 dict(id="ARG-138-003", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="~20:30 (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (fracc. Prados del Sol)", dia="19-OCT, NOCHE",
  title="SINALOA · CULIACÁN — ATAQUE ARMADO EN PRADOS DEL SOL: UN MUERTO Y UN HERIDO",
  hecho="Culiacán · <code>FRACC. PRADOS DEL SOL, POR TITULAR; CALLE MANUEL PAYNO, SOLO POR RESUMEN</code> · publicado el LUNES 19-OCT, por ruta · ~20:30, " + RES + " · atacantes en motocicleta, " + RES + " · <b>1 muerto</b> y <b>1 herido</b>, por titulares (🟡) · el muerto, de 20 años, por titular · herido hospitalizado o leve y sin traslado, " + RES + ": <code>CONTRADICHO</code> · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + AP,
  panel="Ataque armado: <b>1 muerto y 1 herido</b>",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Línea Directa (2026-10-19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Prados del Sol no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-138-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="~22:00 (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (sector 21 de Marzo)", dia="19-OCT, NOCHE",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS A UN HOMBRE AFUERA DE UN EXPENDIO EN EL SECTOR 21 DE MARZO",
  hecho="Culiacán · <code>SECTOR 21 DE MARZO, POR TITULAR</code> · publicado el LUNES 19-OCT, por ruta · noche del lunes, ~22:00, " + RES + " · <b>1 hombre muerto</b> a balazos afuera de un expendio de cerveza, por titulares (🟡) · 25 o 27 años, " + RES + ": <code>CONTRADICHO</code> · disparos desde una camioneta gris, según testigos, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + AP,
  panel="<b>1 hombre asesinado</b> afuera de un expendio",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-10-19)", "Línea Directa (2026-10-19)"], estatus="Parcialmente corroborado", arm=None,
  desl="«21 de Marzo» figura en ARG-135-013 (Colima, col. El Tívoli, calle 21 de Marzo, 16-oct): otra entidad y otro día. Sin coincidencia en el sector 21 de Marzo de Culiacán."),
 dict(id="ARG-138-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="tarde del lunes (solo por resumen)",
  ent="Sinaloa", mun="Mazatlán (fracc. San Joaquín)", dia="19-OCT, TARDE",
  title="SINALOA · MAZATLÁN — EJECUTAN A BALAZOS A UNA MUJER MOTOCICLISTA EN EL FRACCIONAMIENTO SAN JOAQUÍN",
  hecho="Mazatlán · <code>FRACC. SAN JOAQUÍN, POR TITULAR; AV. WALAMO, SOLO POR RESUMEN</code> · publicado el LUNES 19-OCT, por ruta; «este lunes», por titular de Sinaloahoy · tarde del lunes, " + RES + " · <b>1 mujer muerta</b> a balazos mientras viajaba en motocicleta, por titular (🟡) · «segundo homicidio de una mujer en Mazatlán este lunes», por titular; el primero, probablemente <a href=\"#ARG-138-012\"><code>ARG-138-012</code></a> (identificación propia, no publicada) · unos 25 años y al menos 8 impactos, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada · " + AP,
  panel="<b>Mujer motociclista asesinada</b>",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Luz Noticias (2026-10-19)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Joaquín de Mazatlán no figura en las cinco ediciones previas; San Joaquín figura en ARG-128-003 (Edomex): otro hecho. NO es ARG-137-004 (Fovissste Esperanza, 18-oct)."),
 dict(id="ARG-138-006", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="no publicada",
  ent="Sinaloa", mun="Mazatlán (plaza comercial, La Marina)", dia="PUB. 19-OCT, HORA NO FIJADA",
  title="SINALOA · MAZATLÁN — ASESINAN A BALAZOS A UN HOMBRE EN UNA PLAZA COMERCIAL DE LA MARINA",
  hecho="Mazatlán · <code>PLAZA COMERCIAL DE LA ZONA DE LA MARINA, POR TITULAR</code> · publicado el LUNES 19-OCT, por ruta · <b>1 hombre muerto</b> a balazos, por titular (🟡) · baleado en el estacionamiento; murió al llegar al hospital, " + RES + " · Marina y Ejército acordonan, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada · " + AP,
  panel="<b>1 hombre asesinado</b> en una plaza comercial",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; hora no publicada", I=0, N=0, R=1, A=0,
  fechadas=["Luz Noticias (2026-10-19)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicado el 2026-10-19",
  desl="La plaza no figura en las cinco ediciones previas. NO es ARG-138-005."),
 dict(id="ARG-138-007", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="~23:00 del lunes (solo por resumen)",
  ent="Sinaloa", mun="Navolato (La Palma)", dia="19-OCT, NOCHE, SOLO POR RESUMEN · PUB. 20-OCT",
  title="SINALOA · NAVOLATO — ENFRENTAMIENTO ENTRE CIVILES Y MILITARES EN LA PALMA: DOS ABATIDOS",
  hecho="Navolato · <code>LA PALMA, POR TITULAR</code> · publicado el MARTES 20-OCT, por ruta · noche del LUNES 19-OCT, ~23:00, " + RES + " · <b>enfrentamiento entre civiles armados y personal del Ejército</b>, por titulares (🟡) · <b>2 civiles abatidos</b>, por titulares · <code>QUIÉN INICIÓ: UN MEDIO REGIONAL DICE QUE LA PATRULLA FUE AGREDIDA, SOLO POR RESUMEN; NO ACREDITADO POR AUTORIDAD</code> · camioneta con placas de Estados Unidos; FGR en el lugar, " + RES + " · bajas militares: no publicadas · armas de fuego y equipo táctico asegurados, <b>sin cantidad</b>, " + RES + ": evento cualitativo · identidades: no publicadas · " + FR,
  panel="Enfrentamiento entre civiles y militares: <b>2 civiles abatidos</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="quién inició solo por resumen; hora no fijada", I=0, N=0, R=2, A=0,
  fechadas=["Luz Noticias (2026-10-20)"], estatus="Pendiente de corroboración", arm=None, cual=True, fecha_txt="2026-10-19, noche, solo por resumen; publicado el 2026-10-20",
  desl="La Palma no figura en las cinco ediciones previas; Navolato figura en ARG-130-005 y ARG-132-001: otros hechos."),
 dict(id="ARG-138-008", estado="MX-NLE", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="«alrededor de las 11:00» (El Porvenir) o «poco antes del mediodía» (Posta), solo por resumen",
  ent="Nuevo León", mun="Monterrey (col. Hidalgo)", dia="19-OCT, ~11:00-12:00",
  title="NUEVO LEÓN · MONTERREY — ASESINAN A UN COMERCIANTE AFUERA DE SU CASA EN LA COLONIA HIDALGO",
  hecho="Monterrey · <code>COL. HIDALGO, POR RUTA; CALLE SENDERO DE LOS LIRIOS O CRUCE CON RODRIGO ZURIAGA, SOLO POR RESUMEN: CONTRADICHO</code> · publicado el LUNES 19-OCT, por ruta · «alrededor de las 11:00» (El Porvenir), «poco antes del mediodía» (Posta) o «mañana» (Excélsior), " + RES + "; <code>LA VENTANA ABRE A LAS 11:05</code> · <b>1 hombre muerto</b>, <b>comerciante</b>, baleado afuera de su casa, por titular (🟡) · 43 años, por titular de Excélsior · llevado a la Cruz Roja, donde llegó sin vida, por su pareja o por un sobrino, " + RES + ": <code>CONTRADICHO</code> · Policía de Monterrey, ministeriales y Ejército, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + AP,
  panel="<b>Comerciante asesinado</b> afuera de su casa",
  inst=SB, nac="MVS · Milenio · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen (puede ser anterior a las 11:05); sin fuente institucional", I=0, N=3, R=8, A=0,
  fechadas=["MVS Noticias (2026/10/19)", "Enfoque Monterrey (2026/10/19)", "ABC Noticias (2026/10/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="La colonia Hidalgo de Monterrey no figura en las cinco ediciones previas ni en el índice. NO es ARG-137-008 (Nogales de la Sierra, 18-oct)."),
 dict(id="ARG-138-009", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="~21:47 (solo por resumen)",
  ent="Chihuahua", mun="Ciudad Juárez (col. Los Alcaldes)", dia="19-OCT, NOCHE",
  title="CHIHUAHUA · CIUDAD JUÁREZ — BALEAN A UNA MUJER AFUERA DE UNA VIVIENDA EN LA COLONIA LOS ALCALDES",
  hecho="Ciudad Juárez · <code>COL. LOS ALCALDES, POR TITULAR; CALLE ALBERTO ALMEIDA, SOLO POR RESUMEN; SEGUNDA CALLE CONTRADICHA ENTRE RESÚMENES</code> · publicado el LUNES 19-OCT, por ruta (El Bordo); «la noche del lunes», " + RES + " · ~21:47, " + RES + " · <b>1 mujer herida</b> a balazos afuera de una vivienda, por titular (🟡) · llevada a una clínica del IMSS; estado de salud no publicado, " + RES + " · casquillos .223 y 9 mm e impactos en un muro, " + RES + " · detenidos: ver <a href=\"#ARG-138-010\"><code>ARG-138-010</code></a> · identidad: no publicada · " + AP,
  panel="<b>Mujer herida</b> a balazos",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora y estado de salud solo por resumen; sin fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Bordo (2026-10-19)", "El Diario de Juárez (2026/oct/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="Los Alcaldes no figura en las cinco ediciones previas ni en el índice. El ataque y su detención: dos fichas."),
 dict(id="ARG-138-010", estado="MX-CHH", region="Noroeste", color="verde", impacto="pequeno", fecha="2026-10-19", hora="noche del lunes (solo por resumen)",
  ent="Chihuahua", mun="Ciudad Juárez", dia="19-OCT, NOCHE · PUB. 20-OCT",
  title="CHIHUAHUA · CIUDAD JUÁREZ — ARRESTAN A TRES POR EL ATAQUE A TIROS CONTRA UNA MUJER",
  hecho="Ciudad Juárez · publicado el MARTES 20-OCT, por ruta · <b>3 detenidos</b>, por titular (🟢) · policías municipales y estatales los persiguen y arrestan la noche del lunes, " + RES + " · huyen en un vehículo; punto de la detención contradicho entre medios, " + RES + " · por el ataque de <a href=\"#ARG-138-009\"><code>ARG-138-009</code></a> · cargos: no publicados · acusación, no condena · identidades: no publicadas · " + FR,
  panel="<b>3 detenidos</b> por el ataque a una mujer",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="corporación y hora solo por resumen; sin fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Diario de Juárez (2026/oct/20)", "El Bordo (2026-10-19)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-19, solo por resumen; publicado el 2026-10-20",
  desl="Detención ligada a ARG-138-009 por titular. Armamento asegurado: no publicado"),
 dict(id="ARG-138-011", estado="MX-NLE", region="Noreste", color="verde", impacto="mediano", fecha="2026-10-19", hora="no publicada",
  ent="Nuevo León", mun="Cadereyta Jiménez", dia="PUB. 19-OCT, HORA NO FIJADA",
  title="NUEVO LEÓN · CADEREYTA — FUERZA CIVIL CAPTURA A UN PRESUNTO LÍDER CRIMINAL Y A OCHO «GENERADORES DE VIOLENCIA»",
  hecho="Cadereyta Jiménez · publicado el LUNES 19-OCT, por ruta (ABC Noticias) y el 20-OCT (MVS) · <b>Fuerza Civil</b>, por titular · <b>9 detenidos</b>, por titulares (🟢): un presunto líder y 8 «generadores de violencia» (ABC) o 9 en cuatro operativos (MVS); el desglose de MVS incluye un adolescente de 17 años, " + RES + ": <code>COMPOSICIÓN CONTRADICHA</code> · <b>3 armas cortas</b>, vehículos, motocicletas y narcóticos sin cantidad, " + RES + " (El Porvenir, URL sin fecha); sin atribución por operativo · Allende y Montemorelos como zona de influencia, " + RES + " · acusación, no condena · identidades: no se reproducen · " + AP,
  panel="<b>9 detenidos</b> en cuatro operativos de Fuerza Civil",
  inst=SB, nac="MVS", conf="★★☆☆☆",
  campo="armamento solo por resumen; sin comunicado oficial localizado; fecha de los operativos no publicada", I=0, N=1, R=2, A=0,
  fechadas=["ABC Noticias (2026/10/19)", "MVS Noticias (2026/10/20)"], estatus="Parcialmente corroborado", arm="ARG-138-ARM-001", fecha_txt="no publicada; publicado el 2026-10-19",
  desl="Cadereyta no figura en las cinco ediciones previas ni en el índice. Posible relación con el balance semanal de la coordinación metropolitana (16-oct): no integrado"),
 dict(id="ARG-138-012", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="«mediodía» (solo por resumen)",
  ent="Sinaloa", mun="Mazatlán (col. Lomas del Ébano)", dia="19-OCT, MEDIODÍA, SOLO POR RESUMEN",
  title="SINALOA · MAZATLÁN — EJECUTAN A UNA MUJER AFUERA DE SU CASA EN LA COLONIA LOMAS DEL ÉBANO",
  hecho="Mazatlán · <code>COL. LOMAS DEL ÉBANO, POR TITULAR; CALLE AGUSTÍN ANGULO MACHADO, SOLO POR RESUMEN</code> · publicado el LUNES 19-OCT, por ruta · «al mediodía de este lunes», " + RES + "; <code>LA VENTANA ABRE A LAS 11:05</code> · <b>1 mujer muerta</b> a balazos, por titulares (🟡) · afuera de su domicilio, cerca de un jardín de niños y una primaria; Cruz Roja confirma la muerte, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada · " + AP,
  panel="<b>Mujer asesinada</b> afuera de su casa",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen (puede ser anterior a las 11:05); sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-10-19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lomas del Ébano no figura en las cinco ediciones previas. NO es ARG-137-004 (Fovissste Esperanza, 18-oct) ni ARG-138-005 (San Joaquín, tarde). Los Ébanos (ARG-104-006, agosto, aseguramiento): otro hecho."),
 dict(id="ARG-138-013", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="no publicada",
  ent="Guanajuato", mun="Pénjamo (zona centro)", dia="PUB. 19-OCT, HORA NO FIJADA",
  title="GUANAJUATO · PÉNJAMO — BALEAN A UN ABUELO Y A SU NIETO EN EL CENTRO; QUEDAN GRAVES",
  hecho="Pénjamo · <code>ZONA CENTRO, POR TITULAR; CALLE NEZAHUALCÓYOTL, SOLO POR RESUMEN</code> · publicado el LUNES 19-OCT, por ruta · <b>2 heridos graves</b>: un abuelo y su nieto, por titular (🟡) · hombre de unos 65 años y un adolescente, " + RES + " · <b>ningún detenido publicado</b> · identidades: no publicadas · " + AP,
  panel="Ataque armado: <b>2 heridos graves</b> (abuelo y nieto)",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; hora no publicada", I=0, N=0, R=1, A=0,
  fechadas=["Periódico Correo (2026/oct/19)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicado el 2026-10-19",
  desl="El centro de Pénjamo no figura en las cinco ediciones previas; Pénjamo figura en ARG-113-003 (aseguramiento) y ARG-133-REC-001 (col. San Miguel, 14-oct, 3 muertos): otro lugar y otro día. NO es ARG-137-015 (Salamanca)."),
]

# ---------------------------------------------------------------- RECUPERACIONES (ventanas anteriores, también verdes)
R = [
 dict(id="ARG-138-REC-001", estado="MX-GRO", region="Sureste", fecha="2026-10-17", hora="~18:20 o ~19:00 (solo por resumen)", orig="ARGOS 136 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="Guerrero", mun="Cuajinicuilapa (cabecera)", dia="17-OCT, TARDE",
  title="GUERRERO · CUAJINICUILAPA — ASESINAN A UN ASPIRANTE DE MORENA; SU ESPOSA, HERIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 136 — HORA SOLO POR RESUMEN</code> · <code>CABECERA MUNICIPAL, FRENTE AL TEMPLO PARROQUIAL, SOLO POR RESUMEN</code> · tarde o noche del SÁBADO 17-OCT, " + RES + "; publicado el 18-OCT, por ruta · <b>1 hombre muerto</b>: <b>aspirante de Morena</b> a la alcaldía o coordinación municipal, por titulares (🔴 en su ventana) · su <b>esposa, herida</b>, por titular · al menos tres agresores disparan contra su camioneta, " + RES + " · la <b>FGE Guerrero abre investigación</b> por su homicidio, por titular de La Razón; carpeta por homicidio calificado y lesiones calificadas, " + RES + " · <b>ningún detenido publicado</b> · segundo apellido contradicho entre medios · identidad pública por su aspiración política; nombre no reproducido",
  panel="<b>Aspirante de Morena asesinado</b>; su esposa, herida", inst="FGE Guerrero <span class=\"muted-note\">(por titular)</span>", nac="Expansión · La Razón · Infobae · MVS",
  conf="★★★☆☆", campo="hora solo por resumen", I=1, N=4, R=4, A=0,
  fechadas=["Expansión (2026/10/18)", "La Razón (2026/10/18)", "Infobae (2026/10/18)", "El Mañana (2026/10/18)", "La Razón (2026/10/19)", "MVS Noticias (2026/10/19)"],
  desl="Cuajinicuilapa no figura en las cinco ediciones previas como hecho fichado; visto sin ficha en ARGOS 137 (color pendiente)."),
]

for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
# integra=False: fila visible en la tabla, fuera del total (cifras solo por resumen; fecha del hecho no fijada)
ARM = [
 dict(id="ARG-138-ARM-001", ficha="ARG-138-011", estado="MX-NLE", region="Noreste", color="verde", ent="Nuevo León", mun="Cadereyta Jiménez", fecha="2026-10-19", hora="no publicada",
  fecha_txt="no publicada<br><span class=\"muted-note\">publicado 19-oct · día de apertura</span>", c=[3, 0, 0, 0, 0, 0, 0, 0, 0, 9], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], corp="Fuerza Civil (por titular)", conf="Bajo",
  nota="FUERA DEL TOTAL · 9 detenidos, por titular (ABC Noticias 2026/10/19); 3 armas cortas, solo por resumen; largas, cartuchos y cargadores no publicados", fuentes=["ABC Noticias (2026/10/19)", "MVS Noticias (2026/10/20)"], integra=False),
]
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM if a["integra"]))
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
NFNF = sum(1 for e in E if "FECHA DEL HECHO NO FIJADA" in e["hecho"])
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], TOT
assert cnt == {"rojo": 2, "amarillo": 9, "verde": 2}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 0, "verde": 0}, cnt_rec
assert len(ENT) == 6, ENT
assert (NFR, NAP, NFNF) == (2, 9, 0), (NFR, NAP, NFNF)
assert len(set(e["id"] for e in E)) == len(E) and all(e["id"] == f"ARG-138-{i+1:03d}" for i, e in enumerate(E))

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
head = head.replace("<title>ARGOS 137 — Reporte Nacional de Seguridad — 2026-10-19</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE OAXACA LAS CIFRAS OFICIALES DE MUERTOS Y LESIONADOS Y EL DÍA DEL ATAQUE</b> (ARG-138-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE TABASCO LA IDENTIFICACIÓN GENÉTICA DE LOS CUERPOS Y LA FECHA DEL HALLAZGO</b> (ARG-138-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE CHIHUAHUA EL ESTADO DE SALUD DE LA VÍCTIMA Y LA SITUACIÓN JURÍDICA DE LOS DETENIDOS</b> (ARG-138-009 y ARG-138-010).
      <br><b>4. SOLICITE A LA FISCALÍA DE GUERRERO EL AVANCE DE LA INVESTIGACIÓN Y SI HAY DETENIDOS</b> (ARG-138-REC-001).
      <br><b>5. SOLICITE A LA FGR EL RESULTADO DE LA AUDIENCIA FEDERAL Y SU COMUNICADO</b> (ARG-136-006).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: ORD[x["color"]]))
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>19-oct 11:05 → 20-oct 07:06 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,65 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>.
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
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> · una fila fuera del total (ARG-138-ARM-001), con 9 detenidos que no se suman a ningún total.
    <b>Muertos en hechos propios</b>: <b>8</b> por agresión —Juchitán 2, Culiacán 1 + 1, Mazatlán 1 + 1 + 1, Monterrey 1—; <b>2</b> de ellos con el día solo por resumen · <b>cuerpos en fosa</b>: <b>2</b> (ARG-138-002) · <b>abatidos</b>: <b>2</b> (ARG-138-007) · <b>Heridos</b>: <b>6 a 7</b> —Juchitán 2 a 3 (contradicho), Culiacán 1, Ciudad Juárez 1 y Pénjamo 2—. <b>Detenidos sin aseguramiento</b>: <b>3</b> (ARG-138-010). <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-136-006, audiencia inicial federal el martes 20, solo por resumen; resultado no publicado; comunicado de la FGR no localizado (traslado y vinculación estatal del jueves 22, ya en ARGOS 137) · ARG-137-REC-002, capturas del 16-oct (El Rosario) y del 17-oct (Mazatlán) según la Defensa, solo por resumen; primera publicación del 18-oct, por ruta (El Financiero, Tribuna) · ARG-137-009, publicado el 18-oct por ruta (Línea Directa 2026-10-18); día del hecho (domingo 18, ~15:00) solo por resumen · ARG-137-015, «balean a 3 personas», por titular (Periódico Correo 2026/oct/18) · ARG-137-016, publicado el 18-oct por ruta (Grupo Marmor, Red Michoacán 2026/10/18); día del hecho (domingo) solo por resumen · ARG-137-011, «hay un detenido» en cinco medios, ninguno atribuido a una autoridad nombrada: sigue contradicho · ARG-135-REC-004, Nogales: colectivos reportan <b>8 osamentas en 3 días</b>, por titular (El Imparcial 2026/10/19); cifra de colectivo, no oficial.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:2])
byid = {e["id"]: e for e in E}
pg = lambda *ids: "\n".join(ficha(byid["ARG-138-" + i]) for i in ids)
co2 = pg("003", "004", "005", "012", "006")
co3 = pg("007", "008", "009", "013")
co4 = pg("010", "011")
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code> · 1 fila fuera del total"),
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
    <div class="map-caption">Sin aseguramiento integrable en el corte; una fila fuera del total.</div>
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
    <b>Lectura regional</b>: sin lectura (ninguna fila integrada). Filas atenuadas: <code>FUERA DEL TOTAL</code>.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>San Luis Potosí</b>, Guardia Civil Estatal, <b>32 detenidos</b>, por titular (El Heraldo de SLP 2026/10/19): agregado de 24 h sin municipio ni hora; 4 armas de fuego, 252 cartuchos y 16 cargadores, solo por resumen · <b>Michoacán, Jiquilpan</b>, SSP y Defensa, <b>3 detenidos</b>, por titulares (Esfera Noticias, Red Michoacán, Changoonga 2026/10/18); 31 cartuchos (23 de 7.62×39 mm y 8 de .223), solo por resumen; publicado el 18-oct, ventana de ARGOS 136 o 137 · <b>Tamaulipas, Reynosa</b>, Guardia Estatal, vehículo, municiones y artefactos metálicos tras repeler una agresión, por titular (La Región 2026/10/18); ponchallantas y cifras solo por resumen; quién inició, sin examinar; ventana de ARGOS 136 o 137, hora no fijada · <b>Michoacán, Cotija</b>, Ejército, un arma larga, un cargador y 25 cartuchos, solo por resumen; URL sin fecha.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">1 candidata sin confirmar (Culiacán)</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>15 estatales revisadas</b>, 5 de lectura parcial · 17 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Sinaloa</b><br>Culiacán</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">feminicidio en grado de tentativa, por titular; hechos de abril de 2025 en la col. Libertad, solo por resumen</span></td><td><b>18 años</b>, por titular</td><td>FGE Sinaloa, Agencia del MP especializada en homicidio doloso <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Luz Noticias 2026-10-19 · boletín no localizado; <code>fiscaliasinaloa.gob.mx</code> no devuelto · firmeza no informada · publicado el día de apertura sin hora</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Sin vistas nuevas</b>: los boletines de sentencia devueltos por los dominios (Durango, Colima, San Luis Potosí, Morelos, Tabasco, Yucatán) son anteriores a octubre o no tienen fecha en la ruta.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>15 de 32</b>, de ellas <b>5 de lectura parcial</b> (Son, solo una convocatoria; NL, una página ajena a prensa; SLP, boletines sin fecha; Hgo, solo documentos legales; Yuc, nada posterior a 2025) · <b>FGR revisada: lectura parcial</b>, solo comunicados de 2019-2022 · Son, Dgo · Coah, NL, Tamps, SLP, Zac · Col, Gto · Mor, Hgo · Ver, Tab · Gro, Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0 por boletín leído</b> · candidata solo por medios: Sinaloa</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales, 5 de lectura parcial</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>17</b>: BC, BCS, Chih, Sin · Jal, Nay, Ags, Mich · CDMX, Edomex, Pue, Tlax, Qro · Oax, Chis, Camp, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code> y <code>fiscaliasinaloa.gob.mx</code>, 07:39 del 20-oct: <code>CONNECT tunnel failed, response 403</code>; 0 errores medidos en los demás dominios: no se probaron por <code>curl</code> · <b>dominios no devueltos por el buscador</b>, dentro de las 17 <code>NO REVISADA</code>: Sin, Camp</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 20 de 32 con consulta propia por entidad</b> · <b>11 solo por consulta regional amplia</b>: BCS, Dgo · SLP · Nay · CDMX, Mor, Tlax, Qro · Ver, Tab · Chis · <code>NO REVISADA</code>: Ags · <b>armamento: 14 de 32 por dominio propio de seguridad</b> —BC, BCS, Son, Dgo · NL, SLP, Zac · Nay · CDMX, Edomex, Pue, Hgo, Qro · Chis—, de ellas <b>7 de lectura parcial</b> (Son y Dgo, solo portada; NL, una página; Nay, organigrama; Hgo, solo PDF institucionales; Qro, notas de 2019-2022; Chis, rutas opacas sin fecha); <b>5 por portal del gobierno estatal</b> —Col, Ags, Mor, Tlax, Gro—; <code>NO REVISADA</code> (13): Chih, Sin · Coah, Tamps · Jal, Mich, Gto · Ver, Tab · Oax, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 16, 17 y 18-oct</b>: agregado publicado el 19-oct, ya registrado en ARGOS 137 · <b>acciones del 19 y del 20-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta · <b>Defensa, Marina, Guardia Nacional y FGR</b>: SRIV · <b>gabinetedeseguridad.gob.mx</b>: dominio no devuelto</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 20-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR DOS ROJOS</b>: ARG-138-001 y ARG-138-002 · <b>reserva</b> en los dos.
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-138-003 a ARG-138-009, ARG-138-012 y ARG-138-013.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-138-010 y ARG-138-011.
      <br><b>4.</b> <b>Ventana anterior</b>: ARG-138-REC-001.
      <br><b>5.</b> <code>20 H 01 MIN; ONCE DE TRECE CON RUTA FECHADA Y MARCA DE FRONTERA (2 DE CIERRE, 9 DE APERTURA); ARG-138-001 Y ARG-138-002 SIN RUTA CON FECHA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. CULIACÁN, SIETE HECHOS CON MUERTOS (OCHO VÍCTIMAS) DEL 15 AL 19-OCT</b> (cálculo propio; horas solo por resumen). ARG-138-003 y ARG-138-004 se suman a ARG-137-009, ARG-136-004, ARG-135-001, ARG-135-007 y ARG-134-013. Línea: <b>solicitar a la FGE Sinaloa el cotejo balístico entre los siete hechos</b> — hipótesis; vínculo no acreditado.
      <br><b>2. MAZATLÁN, TRES HOMICIDIOS PUBLICADOS EL LUNES TRAS ARG-137-004 (DOMINGO)</b> (cálculo propio; horas solo por resumen). ARG-138-012, ARG-138-005 y ARG-138-006; dos víctimas mujeres. Línea: <b>solicitar a la FGE Sinaloa si las carpetas comparten casquillos o vehículos</b> — hipótesis.
      <br><b>3. DOS ENFRENTAMIENTOS CON PERSONAL MILITAR EN DOS DÍAS (18/19 Y 19-OCT, DÍAS SOLO POR RESUMEN), SIN PARTE PUBLICADO.</b> ARG-138-007 se suma a ARG-137-007 (Colima, mismo tipo de hecho). Línea: <b>solicitar a la Defensa y a la Marina el parte, quién inició y el armamento asegurado</b>.
      <br><b>4. MONTERREY, CUARTO HECHO CON MUERTOS EN EL ÁREA METROPOLITANA EN CINCO DÍAS</b> (cálculo propio). ARG-138-008 se suma a ARG-137-008, ARG-134-002 y ARG-134-007; ARG-138-011: Cadereyta sin antecedente en el índice. Línea: <b>solicitar a Fuerza Civil el desglose del armamento y si los detenidos se vinculan con los homicidios</b> — hipótesis; vínculo no acreditado.
      <br><b>5. GUANAJUATO, DOS ATAQUES CON HERIDOS EN DOS DÍAS.</b> ARG-138-013 se suma a ARG-137-015 (Salamanca, tres baleados). Línea: <b>solicitar a la FGE Guanajuato el estado de los lesionados y si los casquillos coinciden</b> — hipótesis.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: OAXACA Y TABASCO", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA: SINALOA", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA: SINALOA, NUEVO LEÓN, CHIHUAHUA Y GUANAJUATO", co3)
 + page("CRIMEN ORGANIZADO (IV) — ACCIONES INSTITUCIONALES", co4)
 + page("CRIMEN ORGANIZADO (V) — VENTANA ANTERIOR: ARGOS 136", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 19-oct 11:05 → 20-oct 07:06 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
