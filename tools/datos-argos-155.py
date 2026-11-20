# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 155.
Uso: python3 tools/datos-argos-155.py <plantilla ARGOS 154> <salida>
Ventana: 18-nov 12:32 → 19-nov 18:40 CDMX. Archivo: argos-2026-11-19.html.
La hora de «Consulta» se fija al cierre de procedencia-cifras R2 con la variable ARGOS_CONSULTA (HH:MM)."""
import sys, re, json, os, html as H

NUM, FECHA, HORA = "155", "2026-11-19", "18:40"
CONSULTA = "2026-11-19, última búsqueda " + os.environ.get("ARGOS_CONSULTA", "19:06")
DUR = "30 h 08 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 12:32 DEL 18, ES DE LA VENTANA DE ARGOS 154 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
PUB = "Publicado el día de apertura sin hora por fragmento: se integra en esta edición, la primera que lo ve."
TM = " <span class=\"muted-note\">(por titular de medio)</span>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano). Agresores abatidos: fuera de mu.
E = [
 # ======================= ROJOS
 dict(id="ARG-155-001", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-19", hora="tarde, poco antes de las 14:00 (solo por resumen)", mu=2, he=0, cu=0, hk=14,
  ent="Michoacán", mun="Uruapan (col. Rubén Jaramillo, av. Lenin)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; tarde, poco antes de las 14:00, solo por resumen",
  title="MICHOACÁN · URUAPAN — ASESINAN A DOS HOMBRES EN LA AVENIDA LENIN, COLONIA RUBÉN JARAMILLO",
  hecho="Uruapan · <code>COL. RUBÉN JARAMILLO, CRUCE DE DOS DE OCTUBRE Y AV. LENIN</code>, " + RES + " · jueves 19-NOV, por ruta (Media News 2026/11/19 y Grupo Marmor 2026/11/19: «Ejecutan a dos hombres a bordo de una camioneta, al poniente de Uruapan») · tarde, poco antes de las 14:00, " + RES + " · " + FR + " · <b>2 hombres muertos</b>, por titular (Media News; Grupo Marmor; A Tiempo: «Tiroteo en la colonia Rubén Jaramillo de Uruapan deja dos muertos») (🔴 homicidio múltiple) · en una camioneta o en la vía pública: <code>LUGAR EXACTO CONTRADICHO</code>, " + RES + " · agresores huidos en motocicleta, " + RES + " · Guardia Civil acordona; aviso a la Fiscalía, " + RES + " · víctimas sin identificar · " + NOD,
  panel="<b>Doble homicidio</b> en la vía pública", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; lugar exacto contradicho; ninguna fuente institucional ni nacional", I=0, N=0, R=4, A=0,
  fechadas=["Media News (2026/11/19)", "Grupo Marmor (2026/11/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Rubén Jaramillo: dobles homicidios de septiembre (Contramuro; Respuesta; Primera Plana; Quadratín, «Ataque armado en la Rubén Jaramillo de Uruapan deja 2 muertos», sin fecha: <code>POSIBLE CASO HOMÓNIMO — NO SE CITA</code>): otros hechos. Col. Rubén Jaramillo del índice: Xalapa (ARG-139-005), homónimo. Uruapan figura en ediciones previas por otros hechos. Identidades: no establecidas."),
 # ======================= AMARILLOS
 dict(id="ARG-155-002", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-19", hora="~08:55 (solo por resumen)", mu=1, he=0, cu=0, hk=9,
  ent="Sinaloa", mun="Culiacán (col. Miguel Hidalgo)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; ~08:55, solo por resumen",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS AL DUEÑO DE UN MINISÚPER EN LA COLONIA MIGUEL HIDALGO",
  hecho="Culiacán · <code>COL. MIGUEL HIDALGO, MINISÚPER</code>, por titular · jueves 19-NOV, por ruta (Luz Noticias 2026-11-19: «Asesinan a balazos a dueño de un minisúper en la colonia Miguel Hidalgo en Culiacán») · ~08:55, " + RES + " · " + FR + " · <b>1 hombre muerto</b>, dueño del negocio, por titular (Quadratín Sinaloa: «Asesinan a dueño de minisúper en la colonia Miguel Hidalgo de Culiacán»; Meganoticias: «Asesinan a propietario de tienda de abarrotes en colonia Miguel Hidalgo») (🟡 homicidio doloso único) · edad contradicha · la Fiscalía acude, " + RES + " · " + NOD,
  panel="<b>Comerciante asesinado</b> en su negocio", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional ni nacional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-11-19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Miguel Hidalgo figura por ARG-146-013 (taquero, 1-nov): otro hecho. Identidad: no se reproduce."),
 dict(id="ARG-155-003", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-19", hora="no publicada", mu=1, he=0, cu=0, hk=12,
  ent="Sinaloa", mun="Mazatlán (fracc. Santa Fe)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; hora no publicada",
  title="SINALOA · MAZATLÁN — MUERE UN ADOLESCENTE TRAS UN ATAQUE ARMADO EN EL FRACCIONAMIENTO SANTA FE",
  hecho="Mazatlán · <code>FRACC. SANTA FE</code>, por titular · jueves 19-NOV, por ruta (Línea Directa 2026-11-19: «Muere adolescente de 15 años tras ataque armado en Santa Fe, al sur de Mazatlán») · hora no publicada · " + FR + " · <b>1 adolescente muerto</b>, de 15 años, por titular (Noroeste: «Matan a balazos a menor de 15 años en el fraccionamiento Santa Fe, en Mazatlán»; Quadratín Sinaloa: «Muere adolescente tras ataque armado en Mazatlán») (🟡 homicidio doloso único) · " + NOD,
  panel="<b>Adolescente asesinado</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no publicada; ninguna fuente institucional ni nacional", I=0, N=0, R=5, A=0,
  fechadas=["Línea Directa (2026-11-19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Santa Fe figura por ARG-145-008 (31-oct, otra víctima): otro hecho; Mazatlán, por ARG-154-005 (Santa Teresa), ARG-153-005 y ARG-152-005: otros hechos. Identidad: no se reproduce."),
 dict(id="ARG-155-004", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-19", hora="~13:00 (solo por resumen)", mu=1, he=1, cu=0, hk=13,
  ent="Guanajuato", mun="Irapuato (col. Ignacio Allende)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; ~13:00, solo por resumen",
  title="GUANAJUATO · IRAPUATO — ATACAN A BALAZOS A DOS HOMBRES EN LA COLONIA IGNACIO ALLENDE: UN MUERTO Y UN HERIDO",
  hecho="Irapuato · <code>COL. IGNACIO ALLENDE</code>, por titular · jueves 19-NOV, por ruta (AM 2026/11/19: «Platicaban en la calle y sicarios los atacan a balazos en Irapuato; uno muere sentado en la banqueta»; Correo 2026/nov/19: «Asesinan a balazos a hombre en Ignacio Allende, Irapuato; hay un detenido bajo investigación») · ~13:00, " + RES + " · " + FR + " · <b>1 hombre muerto y 1 herido</b>, por titular (Guanajuato Informa: «Matan a un hombre, hieren a otro y detienen a un presunto implicado en la colonia Ignacio Allende, Irapuato») (🟡 homicidio doloso único) · agresores en motocicleta, " + RES + " · un detenido «bajo investigación», por titular, <code>SIN CIFRA DE AUTORIDAD — NO SE INTEGRA</code>",
  panel="<b>Ataque a balazos: 1 muerto y 1 herido</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; detenido sin confirmación de autoridad; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["AM (2026/11/19)", "Correo (2026/nov/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ignacio Allende del índice: Acapulco (ARG-136-003), homónimo; Irapuato, por ARG-146-006 (col. Primavera) y otros: otros hechos. Identidades: no se reproducen."),
 dict(id="ARG-155-005", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-19", hora="mañana, ~06:30 o ~07:00 (solo por resumen)", mu=1, he=0, cu=0, hk=7,
  ent="Michoacán", mun="Morelia (col. Adolfo López Mateos)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; mañana, ~06:30 o ~07:00, solo por resumen",
  title="MICHOACÁN · MORELIA — ASESINAN A BALAZOS AL DUEÑO DE UN MINISÚPER EN LA COLONIA ADOLFO LÓPEZ MATEOS",
  hecho="Morelia · <code>COL. ADOLFO LÓPEZ MATEOS, MINISÚPER</code>, por titular de ruta fechada (Changoonga 2026/11/19: «Asesinan a … dueño de minisúper en la Adolfo López Mateos, en Morelia») · jueves 19-NOV, por ruta · mañana, ~06:30 o ~07:00, " + RES + " · " + FR + " · <b>1 hombre muerto</b>, propietario, por titular (Quadratín: «Asesinan a balazos a un hombre dentro de minisúper en Morelia»; A Tiempo: «…asesinan a propietario del minisúper La Fuente») (🟡 homicidio doloso único) · colonia contradicha entre medios · Policía Morelia, GN y Fiscalía en el lugar, " + RES + " · " + NOD,
  panel="<b>Comerciante asesinado</b> en su negocio", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; colonia contradicha; ninguna fuente institucional ni nacional", I=0, N=0, R=6, A=0,
  fechadas=["Changoonga (2026/11/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Mismo patrón que ARG-155-002 (dueño de minisúper, Culiacán): otro hecho, otra entidad; vínculo no acreditado. Identidad: la ruta la contiene, no se reproduce."),
 dict(id="ARG-155-006", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-18", hora="tarde del 18 o noche del 17, contradicho (solo por resumen)", mu=1, he=0, cu=0, hk=17,
  ent="Guanajuato", mun="León (col. Santa María de Cementos)", dia="MAR 17 O MIÉ 18-NOV, CONTRADICHO",
  fecha_txt="publicación miércoles 18-nov, por ruta; tarde del 18 o noche del 17, DÍA SOLO POR RESUMEN",
  title="GUANAJUATO · LEÓN — ASESINAN A BALAZOS A UNA JOVEN EN LA COLONIA SANTA MARÍA DE CEMENTOS",
  hecho="León · <code>COL. SANTA MARÍA DE CEMENTOS</code>, por titular · publicación miércoles 18-NOV, por ruta (Correo 2026/nov/18: «Asesinan a balazos a una joven en la colonia Santa María de Cementos, León») · tarde del miércoles 18 o noche del martes 17: <code>DÍA CONTRADICHO</code>, " + DSR + " · " + AP + " · " + RET + " · <b>1 mujer muerta</b>, joven, por titular (Milenio: «León: asesinan a balazos a mujer en Santa María de Cementos») (🟡 homicidio doloso único) · agresores en vehículo, " + RES + " · " + NOD,
  panel="<b>Mujer asesinada</b> a balazos", inst=SB, nac="Milenio", conf="★★☆☆☆",
  campo="día contradicho, solo por resumen; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["Correo (2026/nov/18)", "Noticieros en Línea (2026/nov/19)"], estatus="Pendiente de corroboración", arm=None,
  desl="Santa María de Cementos no figura en las ediciones 146 a 154. " + PUB + " Identidad: no se reproduce."),
 dict(id="ARG-155-007", estado="MX-TLA", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-18", hora="noche (solo por resumen)", mu=1, he=0, cu=0, hk=21,
  ent="Tlaxcala", mun="Tlaxcala, Ocotlán (privada Miraflores)", dia="MIÉ 18-NOV, POR RUTA",
  fecha_txt="miércoles 18-nov, por ruta; noche, solo por resumen",
  title="TLAXCALA · OCOTLÁN — HOMBRES ARMADOS IRRUMPEN EN UNA VIVIENDA Y ASESINAN A UN HOMBRE",
  hecho="Ocotlán, Tlaxcala · <code>PRIVADA MIRAFLORES, VIVIENDA</code>, " + RES + " · miércoles 18-NOV, por ruta (Gentetlx 2026/11/18: «A balazos ejecutan a hombre en Ocotlán, Tlaxcala») · noche, ~19:30, " + RES + " · " + AP + " · <b>1 hombre muerto</b> dentro de su domicilio, por titular (Meganoticias: «Ataque armado en Ocotlán: irrumpen en casa y asesinan a un hombre»; UnoTV: «Asesinan a comerciante durante ataque armado en su domicilio, en Talxcala») (🟡 homicidio doloso único) · al menos tres agresores con armas largas; familia encañonada, " + RES + " · ocupación y edad contradichas; móvil de narcomenudeo, versión de un medio, no confirmada · la FGJ del estado realiza diligencias, " + RES + " · " + NOD,
  panel="<b>Hombre asesinado</b> en su domicilio", inst=SB, nac="UnoTV · N+", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["Gentetlx (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ocotlán, Tlax., no figura en las ediciones previas; Ocotlán, Jal. (enfrentamiento del 12-nov): homónimo. La Prensa de Tlaxcala (2026/11) y 385grados reproducen la misma nota. " + PUB + " Identidad: no se reproduce."),
 dict(id="ARG-155-008", estado="MX-CAM", region="Sureste", color="amarillo", impacto="mediano", fecha="2026-11-19", hora="no fijada", mu=1, he=0, cu=0, hk=10,
  ent="Campeche", mun="Ciudad del Carmen (Villas de Santa Ana)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; hora no fijada",
  title="CAMPECHE · CIUDAD DEL CARMEN — ASESINAN A BALAZOS A UN HOMBRE EN PLENA CALLE DE VILLAS DE SANTA ANA",
  hecho="Ciudad del Carmen · <code>VILLAS DE SANTA ANA, CALLE SANTO DOMINGO</code>, " + RES + " · jueves 19-NOV, por ruta (PorEsto 2026/11/19: «Ejecutan a hombre a balazos en plena calle de Villas de Santa Ana en Ciudad del Carmen») · hora no fijada · " + FR + " · <b>1 hombre muerto</b>, por titular (🟡 homicidio doloso único) · otras notas locales sin fecha verificada (La i Noticias; Tribuna Campeche, comunicado de la SPSC, " + RES + ") · " + NOD,
  panel="<b>Hombre asesinado</b> en la vía pública", inst=SB, nac="—", conf="★★☆☆☆",
  campo="una sola ruta con fecha; hora no fijada; comunicado de la SPSC solo por resumen", I=0, N=0, R=3, A=0,
  fechadas=["PorEsto (2026/11/19)"], estatus="Pendiente de corroboración", arm=None,
  desl="Villas de Santa Ana no figura en las ediciones 146 a 154. Identidad: no se reproduce."),
 # ======================= VERDES
 dict(id="ARG-155-009", estado="MX-PUE", region="Centro", color="verde", impacto="mediano", fecha="2026-11-18", hora="mañana (solo por resumen)", mu=0, he=0, cu=0, hk=10,
  ent="Puebla", mun="Tepeaca (barrio Santa Cruz Temilco)", dia="MIÉ 18-NOV, POR BOLETÍN",
  fecha_txt="miércoles 18-nov, por titular del boletín federal de acciones del 18; mañana, solo por resumen; publicación 19-nov, por ruta",
  title="PUEBLA · TEPEACA — SSP Y MARINA DETIENEN A SIETE PRESUNTOS INTEGRANTES DE «LOS TEPEACAS» Y ASEGURAN CINCO ARMAS LARGAS",
  hecho="Tepeaca · <code>BARRIO SANTA CRUZ TEMILCO</code>, " + RES + " · acciones del 18-NOV, por titular del boletín federal («El Gabinete de Seguridad del Gobierno de México informa acciones relevantes del 18 de noviembre de 2026», gob.mx/sspc; contenido " + RES + ") · «mañana de este miércoles», " + RES + " · publicación 19-NOV, por ruta (Infobae 2026/11/19; Intolerancia 2026/11/19) · " + AP + " · " + RET + " · <b>7 detenidos</b>, por titular (La Jornada de Oriente: «Caen siete integrantes de \"Los Tepeacas\"; decomisan cinco armas largas»; Controversia Puebla: «Intervención de SSP y Marina permite detener a siete hombres armados en Tepeaca») · <b>5 armas largas</b>, por titular (La Jornada de Oriente; La Nigua: «Caen siete en Tepeaca con cinco armas largas, 22 cargadores y equipo táctico»; Curul Puebla: «…aseguran cinco armas largas y vehículos»), rutas sin fecha · 22 cargadores, por un titular (La Nigua): <code>NO SE INTEGRA</code> (🟢 detención y aseguramiento) · más de 500 cartuchos, 5 chalecos, 2 cascos, " + RES + ": <code>CANTIDAD NO CITABLE — NO SE INTEGRA</code> · célula dedicada a vigilar ductos de hidrocarburo; cinco detenidos originarios de Veracruz y uno del Estado de México, según la SSP, " + RES + " · SSP de Puebla y Marina · " + NDA,
  panel="<b>7 detenidos y 5 armas largas</b> de una célula de huachicol", inst="Gabinete de Seguridad (boletín, por resumen)", nac="Infobae · Milenio · El Universal Puebla", conf="★★★☆☆",
  campo="hora solo por resumen, en la frontera de apertura; cifras del boletín solo por resumen", I=1, N=3, R=4, A=0,
  fechadas=["Infobae (2026/11/19)", "Intolerancia (2026/11/19)"], estatus="Parcialmente corroborado", arm="ARG-155-ARM-001",
  desl="Tepeaca figura por ARG-121-004 (pipas de gas LP, septiembre): otro hecho. " + PUB + " «Detienen al líder…» (El Universal Puebla): el cuerpo no sostiene «líder». Republicaciones del boletín (Edomex Al Día, Hoy Tamaulipas): una sola fuente. Nombres: no se reproducen."),
 dict(id="ARG-155-010", estado="MX-GRO", region="Sureste", color="verde", impacto="mediano", fecha="2026-11-18", hora="no fijada", mu=0, he=0, cu=0, hk=11,
  ent="Guerrero", mun="Ometepec (Zacualpan)", dia="MIÉ 18-NOV, POR BOLETÍN",
  fecha_txt="miércoles 18-nov, por titular del boletín federal de acciones del 18; publicación en medios 19-nov, por ruta; hora no fijada",
  title="GUERRERO · OMETEPEC — CUMPLIMENTAN ORDEN DE APREHENSIÓN CONTRA UN PRESUNTO INTEGRANTE DE «LOS RUSOS» POR EL HOMICIDIO DE UN LÍDER AMUZGO",
  hecho="Ometepec · <code>LOCALIDAD ZACUALPAN</code>, " + RES + " · acciones del 18-NOV, por titular del boletín federal (gob.mx/sspc; contenido " + RES + ") · publicación 19-NOV, por ruta (La Silla Rota 2026/11/19: «Detienen a \"Beto Zacualpan\", relacionado con asesinato de líder amuzgo»; Proceso 2026/11/19: «…integrante de Los Rusos, acusado de matar a líder amuzgo en Guerrero») · hora no fijada · " + AP + " · <b>1 detenido</b> por orden de aprehensión por homicidio calificado, por titular (🟢 orden cumplimentada) · corporación: GN, Fiscalía y Policía Estatal (boletín, " + RES + ") o Defensa, por titular (El Sur: «Detiene Defensa a un hombre por homicidio del líder amuzgo…»): <code>CORPORACIÓN CONTRADICHA</code> · homicidio de origen: enero de 2023, " + RES + "; no se recalifica · 1 arma larga, 1 cargador y 17 cartuchos, " + RES + " del boletín: <code>CANTIDAD NO CITABLE — NO SE INTEGRA</code>",
  panel="<b>Orden de aprehensión cumplimentada</b> por homicidio", inst="Gabinete de Seguridad (boletín, por resumen)", nac="Proceso · La Silla Rota", conf="★★★☆☆",
  campo="hora no fijada; contenido del boletín solo por resumen", I=1, N=2, R=2, A=0,
  fechadas=["La Silla Rota (2026/11/19)", "Proceso (2026/11/19)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — arma, cargador y cartuchos solo por resumen: cantidad no citable (ver vistos de armamento)",
  desl="Ometepec y Zacualpan no figuran en los cartelones de 151 a 154; «Los Rusos», por ARG-115-002, ARG-118-REC-001 y ARG-130-007 (Acapulco): otros hechos. Republicaciones del boletín: una sola fuente. " + PUB + " Nombre y alias: no se reproducen."),
 dict(id="ARG-155-011", estado="MX-HID", region="Centro", color="verde", impacto="mediano", fecha="2026-11-19", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Hidalgo", mun="Tepehuacán de Guerrero (caso)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="publicación jueves 19-nov, por ruta; capturas el martes 17 o el miércoles 18, SOLO POR RESUMEN; hora no fijada",
  title="HIDALGO · TEPEHUACÁN DE GUERRERO — CUATRO DETENIDOS POR EL ATAQUE A LA CASA DEL ALCALDE EN EL QUE MURIERON DOS POLICÍAS",
  hecho="Tepehuacán de Guerrero (caso) · publicación jueves 19-NOV, por ruta (Síntesis 2026/11/19: «Suman cuatro detenidos por ataque en domicilio de alcalde de Tepehuacán»; La Silla Rota 2026/11/19) · capturas: el conductor, martes 17, y otros tres por órdenes de aprehensión, martes 17 o miércoles 18, " + RES + "; <b>4 detenidos acumulados</b>; la captura del conductor es de la ventana de ARGOS 154 · " + FR + " · " + RET + " · <b>4 detenidos</b>, por titular (Milenio: «Cuatro detenidos ataque casa alcalde de Tepehuacán: móvil robo»; El Universal Hidalgo: «Robo habría motivado ataque a vivienda del alcalde de Tepehuacán; detienen a cuatro») (🟢 detención) · 1 detenido en el primer parte (Infobae 2026/11/19): secuencia, no contradicción · SSP Hidalgo, GN y PGJEH; móvil de robo, por slug de ruta fechada (La Silla Rota 2026/11/19: «confirma-gabinete-de-seguridad-que-robo-motivo-agresion-en-tepehuacan»); el secretario de Seguridad informa cuatro detenidos, " + RES + " · armas: «aseguran armas», por titular (La Jornada Hidalgo), sin cantidad: <code>CANTIDAD NO DETERMINADA</code>",
  panel="<b>4 detenidos</b> por el ataque a la casa del alcalde (seguimiento de ARG-151-009)", inst="Gabinete de Seguridad (por slug de medio)", nac="Milenio · El Universal · Infobae", conf="★★★☆☆",
  campo="día y hora de las capturas solo por resumen; declaración institucional solo por slug de medio", I=1, N=3, R=3, A=0,
  fechadas=["Síntesis (2026/11/19)", "La Silla Rota (2026/11/19)", "Zunoticia (2026/11/19)", "Infobae (2026/11/19)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armas sin cantidad publicada: evento cualitativo",
  desl="Desarrollo de ARG-151-009 (ataque del 14-nov, 2 policías muertos): la detención se ficha aparte; el homicidio no se recalifica. Dos policías sobrevivientes detenidos en Molango, versión de familiares (Milenio): fuente única, no se integra. Nombres: no se reproducen."),
 dict(id="ARG-155-012", estado="MX-ROO", region="Sureste", color="verde", impacto="mediano", fecha="2026-11-18", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Quintana Roo", mun="Cancún, Benito Juárez (caso Villas Otoch)", dia="MIÉ 18-NOV, POR RESUMEN",
  fecha_txt="publicación jueves 19-nov, por ruta; detención el miércoles 18, DÍA SOLO POR RESUMEN; hora no fijada",
  title="QUINTANA ROO · CANCÚN — DETIENEN A SEIS PERSONAS TRAS EL TRIPLE HOMICIDIO DE LA REGIÓN 247",
  hecho="Cancún · caso Villas Otoch, Región 247 · publicación jueves 19-NOV, por ruta (Noticaribe 2026/11/19: «Detienen a 6 por triple homicidio en Cancún») · detención el miércoles 18, " + DSR + "; hora no fijada · " + FR + " · <b>6 detenidos</b>, por titular (Sol Quintana Roo: «Detienen a seis por triple homicidio en Cancún»; Marcrix: «Detienen a seis personas tras triple homicidio en Cancún; dos estarían vinculadas al ataque») (🟢 detención) · vínculo con el ataque: 2 de los 6, por titular de un medio · ninguna declaración nombrada de la FGE: <code>SIN CIFRA DE AUTORIDAD</code> · una víctima identificada, " + RES,
  panel="<b>6 detenidos</b> tras un triple homicidio (seguimiento de ARG-154-006)", inst=SB, nac="—", conf="★★★☆☆",
  campo="cifra de detenidos solo por titular de medio; vínculo de 2 de 6 por un medio; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Noticaribe (2026/11/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Desarrollo de ARG-154-006 (3 muertos, Región 247, 18-nov): la detención se ficha aparte. «Capturan a seis por narcomenudeo; cuatro van por triple homicidio» (El Sureste): triple homicidio de Valle Verde, agosto: homónimo. Nombres: no se reproducen."),
 dict(id="ARG-155-013", estado="MX-CHH", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-18", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Chihuahua", mun="Chihuahua (capital)", dia="MIÉ 18-NOV, POR RESUMEN",
  fecha_txt="publicación jueves 19-nov, por ruta; operativo el miércoles 18, DÍA SOLO POR RESUMEN; hora no fijada",
  title="CHIHUAHUA · CHIHUAHUA — LA SSPE DETIENE A DOS PERSONAS CON UN ARMA, DROGA Y DINERO EN EFECTIVO",
  hecho="Chihuahua, capital · publicación jueves 19-NOV, por ruta (Al Instante Chihuahua 2026/11/19: «Detiene SSPE a dos personas en posesión de arma, droga y dinero en efectivo en Chihuahua»; El Diario de Chihuahua 2026/nov/19: «Traían un arma, droga y siete mil en efectivo, los detienen») · operativo el miércoles 18, " + DSR + "; hora no fijada · " + FR + " · <b>2 detenidos</b> por la SSPE, por titular (🟢 detención y aseguramiento) · <b>1 arma</b>, por titular de dos medios, sin categoría por titular; arma corta 9 mm, cargador y cartuchos, " + RES + " · " + NDA,
  panel="<b>2 detenidos</b> con un arma y droga", inst="SSPE (por titular de medio)", nac="—", conf="★★★☆☆",
  campo="desglose del arma solo por resumen; corporación solo por titular de medio", I=1, N=0, R=2, A=0,
  fechadas=["Al Instante Chihuahua (2026/11/19)", "El Diario de Chihuahua (2026/nov/19)"], estatus="Parcialmente corroborado", arm="ARG-155-ARM-002",
  desl="Los dos medios describen el mismo aseguramiento: un solo evento. Chihuahua capital no figura en los cartelones de 151 a 154 por un hecho de esta clase. Nombres: no se reproducen."),
]
R = []
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-155-ARM-001", ficha="ARG-155-009", estado="MX-PUE", region="Centro", color="verde", ent="Puebla", mun="Tepeaca", fecha="2026-11-18", hora="mañana (solo por resumen)",
  fecha_txt="acciones del 18-nov, por boletín; <code>SI RESULTA ANTERIOR A LAS 12:32 DEL 18, SE RETIRA</code>", c=[0, 5, 0, 0, 0, 0, 0, 0, 0, 0], nd=[4, 5, 9], integra=True,
  corp="SSP de Puebla y Marina", conf="Bajo", nota="5 armas largas, por titular de tres medios (La Jornada de Oriente, La Nigua, Curul Puebla), rutas sin fecha; 22 cargadores por un titular, no integrados; cartuchos y cargadores solo por resumen; detenidos sin cifra de autoridad citable",
  fuentes=["La Jornada de Oriente", "Controversia Puebla", "Infobae (2026/11/19)"]),
 dict(id="ARG-155-ARM-002", ficha="ARG-155-013", estado="MX-CHH", region="Noroeste", color="verde", ent="Chihuahua", mun="Chihuahua", fecha="2026-11-18", hora="no fijada",
  fecha_txt="publicación 19-nov, por ruta; operativo el 18, solo por resumen", c=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], nd=[4, 5, 9], integra=True,
  corp="SSPE de Chihuahua", conf="Bajo", nota="1 arma, por titular de dos medios, sin categoría; desglose (corta 9 mm, cargador, cartuchos) solo por resumen; detenidos sin cifra de autoridad citable",
  fuentes=["Al Instante Chihuahua (2026/11/19)", "El Diario de Chihuahua (2026/nov/19)"]),
]

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
HORAS = 30 + 8 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
assert TOT == [0, 5, 1, 0, 0, 0, 0, 0, 0, 0] and ARMAS == 6, (TOT, ND)
assert ND == [False, False, False, False, True, True, False, False, False, True], ND
assert cnt == {"rojo": 1, "amarillo": 7, "verde": 5}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0} and R == [], cnt_rec
assert (MU, HE, CU) == (9, 1, 0), (MU, HE, CU)
assert DENS == "0,43" and RPH == "0,03", (DENS, RPH)
assert (NAP, NFR, NRET) == (4, 9, 3), (NAP, NFR, NRET)
assert len(ENT) == 10 and len(ENT_ROJO) == 1, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-155-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-18" <= x["fecha"] <= "2026-11-19", x["id"]
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

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 154 — Reporte Nacional de Seguridad — 2026-11-18</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE MICHOACÁN EL PARTE DEL DOBLE HOMICIDIO DE LA AVENIDA LENIN, EN URUAPAN, Y EL COTEJO BALÍSTICO CON HECHOS PREVIOS DE LA ZONA, VÍNCULO NO ACREDITADO</b> (ARG-155-001).
      <br><b>2. SOLICITE A LA SSP DE PUEBLA EL COMUNICADO CON LA HORA, EL DESGLOSE DE MUNICIONES Y LA SITUACIÓN JURÍDICA DE LOS DETENIDOS DE TEPEACA</b> (ARG-155-009).
      <br><b>3. SOLICITE A LA FGE DE QUINTANA ROO LA CIFRA OFICIAL DE DETENIDOS Y SU VÍNCULO CON EL TRIPLE HOMICIDIO DE LA REGIÓN 247</b> (ARG-155-012).
      <br><b>4. SOLICITE A LA PGJ DE HIDALGO LA FECHA DE CADA CAPTURA Y EL INVENTARIO DE ARMAS DEL CASO TEPEHUACÁN</b> (ARG-155-011).
      <br><b>5. SOLICITE A LAS FISCALÍAS DE SINALOA Y MICHOACÁN EL MÓVIL Y EL DICTAMEN BALÍSTICO DE LOS HOMICIDIOS EN MINISÚPER DE CULIACÁN Y MORELIA</b> (ARG-155-002 y -005).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>18-nov 12:32 → 19-nov 18:40 CDMX</b> (<b>{DUR}</b>) · mié 18 (desde 12:32) · jue 19 (hasta 18:40) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
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
    <b>Armamento</b>: 2 aseguramientos integrados, confianza Bajo (Tepeaca, 5 armas largas, con cláusula de retiro; Chihuahua, 1 arma sin categoría); cartuchos, cargadores y detenidos de esos eventos, solo por resumen: n/d · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas · <b>heridos</b>: {HE} (Irapuato) · <b>cuerpos</b>: {CU} · <b>detenidos sin cifra de autoridad citable</b>: Tepeaca 7, Chihuahua 2, Ometepec 1, Tepehuacán 4 (acumulados), Cancún 6, por titular; Irapuato 1 «bajo investigación»: no se suman · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (publicados el día de cierre) · <b>totales sujetos a {NRET} cláusulas de retiro</b> (Tepeaca: «mañana de este miércoles» solo por resumen; Tepehuacán: capturas del 17 o del 18 solo por resumen; León: noche del 17 o tarde del 18 solo por resumen).
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «Miércoles con 36 ejecutados» (Sol Yucatán) · «Informe diario: aseguran drogas en Culiacán y Mazatlán; 4 homicidios, 4 heridos y 14 vehículos robados el miércoles» (Noroeste) · «Seis ataques dejan dos muertos y seis baleados ayer en Mazatlán» (Meganoticias) · «Jornada de violencia en Zona Metropolitana de Guadalajara deja 3 muertos» (López-Dóriga) · «Caen 20 personas en operativos de seguridad en ocho estados…» (Hoy Tamaulipas) y «Operativos de seguridad dejan 21 detenidos en seis estados» (Edomex Al Día): republicaciones de boletines federales.
    <br><b>Vistos, fuera de totales</b> (sin ruta con día, fuente única o ventana anterior): Coyuca de Benítez, Gro., dos cuerpos con impactos de bala en un vehículo sobre la carretera Acapulco–Zihuatanejo, ~14:00 {RES}, sin ruta con día (Azteca Guerrero): 🔴 sin día por ruta ni titular · Xochitepec, Mor., col. Nueva Morelos, joven asesinado, miércoles 18 a las 17:19 {RES}, sin ruta (Diario de Morelos; La Unión) · Santa Catarina, NL, hombre asesinado mientras reparaba su auto, 19-nov {RES}, sin ruta · Mazatlán, centro, conductor de camión urbano asesinado y una persona herida, día contradicho (17 o 18) {RES}, sin ruta · Cuitzeo, Mich., hombre asesinado en su casa, 18-nov {RES}, sin ruta · Tlaxcala, capital, expolicía federal baleado que muere en el hospital, sin fecha (Excélsior; Estilotlax): <code>POSIBLE MISMO HECHO QUE ARG-125-028 — NO INTEGRAR</code> · Pénjamo, Gto., Tierras Negras, cadáver encobijado con huellas de tortura, y San Luis de la Paz, cuerpo junto a un camino (AM 2026/11/18), hora no fijada, sin causa informada por autoridad · Monterrey, Fuerza Civil detiene a una mujer y a su hijo con tres cargadores, 19-nov {RES}, sin ruta · Veracruz, Ciudad Industrial, asalto armado a cuentahabientes de un banco (La Silla Rota 2026/11/18), «esa mañana» {RES}: patrimonial, anterior a la apertura por resumen · <b>ventana de ARGOS 154</b>: Silao, joven hallado muerto, madrugada del 18, ~04:40 {RES} (AM 2026/11/18): 🟡 · Mazatlán, ataque con explosivos a un negocio de compraventa de vehículos, martes 17 {RES}, sin ruta (El Universal): 🔴, sin hora por titular, no admite recuperación · Tecate, Valle de las Palmas, colectivos hallan restos óseos en una fosa (Punto Norte 2026/11/18; «martes 16» incoherente con el calendario): 🔴, ventana 153 o 154, sin hora por titular · <b>ventanas anteriores</b>: Huitzilac, Mor., «38 hallazgos» de restos humanos, búsqueda del 9 al 13-nov {RES}, sin desglose por día · Reynosa, nuevos puntos con restos humanos (La Verdad 2026/11), 6-nov {RES}: otro hecho que ARG-154-008 · Yautepec, Mor., cabalgata: sin cambio.
    <br><code>FE DE ERRATAS — ARGOS 153</code>: <b>ARG-153-001</b> Santiago Maravatío: «Falleció el tercer policía de Santiago Maravatío tras la emboscada del 17 de noviembre», por titular (La Silla Rota 2026/11/19) · muertos de 153: 8 → <b>9</b>; heridos de la ficha: 1 → 0, supone que el herido era el policía fallecido (cálculo propio).
    <br><code>FE DE ERRATAS — ARGOS 154</code>: <b>ARG-154-011</b> Zapopan: <b>8 detenidos</b>, saldo posterior por titular («Suman ocho detenidos tras enfrentamiento en Jardines del Sol; hay tres muertos», Meganoticias; «Sube a ocho los detenidos en operativos contra ''El Topo'' del CJNG», NX Noticias; Infobae 2026/11/18; los tres muertos del titular son agresores abatidos), frente a 3 en el primer parte (Plaza Juárez); boletín federal de acciones del 18: ocho detenidos y ocho armas cortas {RES}, frente a seis armas cortas {RES} en 154 · <code>CIFRA DE DETENIDOS ACTUALIZADA — SE SUSTITUYE «3 A 6, CONTRADICHO» POR 8</code>; armas cortas, no integradas; fuera de totales en ambas ediciones.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Mazatlán (ARG-154-005)</b>: hora ~11:30 u ~11:45 {RES}; ningún titular la fija: la cláusula de retiro sigue abierta · <b>Río Bravo (ARG-154-008)</b>: día «martes 17» {RES}; número de víctimas no informado; colectivos piden el levantamiento a la Fiscalía; sin declaración de la FGJ de Tamaulipas · <b>Xochistlahuaca (ARG-154-002)</b>: noche del martes 17 {RES}; «tercer aspirante de Morena asesinado en Guerrero», por titular (Quinto Poder 2026/11/18), frente a «segundo» {RES} · <b>Chalco (ARG-154-004)</b>: ningún titular con tercer muerto; heridos 1, 2 o 3, sin resolver · <b>Poza Rica (ARG-154-007)</b>: sin réplicas en esta ventana; vehículos 3 o 4, sin titular · <b>Taxco (ARG-154-001)</b>: ningún detenido publicado · <b>Tecate (ARG-150-REC-001)</b>: «cuádruple homicidio», por titular (En Línea BC 2026/11/16; N+), frente a 3 muertos y 2 heridos en el primer parte (Punto Norte 2026/11/07); FGE de Baja California, 4 muertos, {RES}; lugar y hora contradichos entre fuentes y sin dos campos individualizadores por titular: <code>POSIBLE MISMO CASO — EL SALDO NO SE CORRIGE HASTA VALIDACIÓN</code> · <b>Tecate (ARG-152-002)</b>: «Disputa por rancho en Tecate posible móvil del crimen de agente de la FGE y exmilitar», por titular (En Línea BC 2026/11/18); detenidos contradichos · <b>Ciudad Juárez</b>: «Vinculan a dos por ataque a federales», por titular (El Diario de Chihuahua 2026/nov/19), hecho del 11-nov, sin ficha previa localizada; <code>NO ES SENTENCIA</code> · <b>Texhuacán (ARG-151-001)</b>: ningún detenido publicado (La Silla Rota 2026/11/19) · <b>Tuxpan (ARG-150-019)</b>: sin vinculación indexada; posible segunda víctima mortal, sin fecha en la ruta (Meganoticias): no se corrige · <b>Cajeme</b>: sin vinculación publicada de los cinco detenidos.
  </p>
'''

byid = {e["id"]: e for e in E}
co1 = "\n".join(ficha(byid[f"ARG-155-{i:03d}"]) for i in (1, 2, 3))
co2 = "\n".join(ficha(byid[f"ARG-155-{i:03d}"]) for i in (4, 5, 6))
co3 = "\n".join(ficha(byid[f"ARG-155-{i:03d}"]) for i in (7, 8, 9))
co4 = "\n".join(ficha(byid[f"ARG-155-{i:03d}"]) for i in (10, 11, 12, 13))
assert sorted(re.findall(r'id="(ARG-155-0\d\d)"', co1 + co2 + co3 + co4)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
NDR = "solo por resumen: <b>cantidad no determinada</b>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "1 evento (Tepeaca), confianza <b>Bajo</b>, con cláusula de retiro"),
 tile(2, "Sin categoría", tv(2), "1 evento (Chihuahua), confianza <b>Bajo</b>"),
 tile(3, "Cartuchos", tv(4, fmt), NDR),
 tile(4, "Cargadores", tv(5), NDR),
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

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr style="opacity:.72;"><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> · ningún aseguramiento de la ventana con día fijado y cantidad publicada por titular o por autoridad</td></tr>'
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
    <b>Lectura regional</b>: Centro 5 armas largas (Tepeaca) · Noroeste 1 arma sin categoría (Chihuahua) · las demás regiones, ninguna arma integrada. <b>Cálculo propio</b>.
    <br><b>BOLETÍN FEDERAL</b>: acciones del 17 y del 18-nov: __FED17__ (republicadores: Red Metropolitana 2026/11/18; Ultranoticias; RED113 2026/11): <b>corroboración débil por construcción</b>; <b>un agregado no fija el día ni la hora de cada acción</b> · acciones del 13, 14 y 15-nov: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al cierre · acciones del 19: <code>SIN RESULTADO INDEXADO EN VENTANA</code> al cierre.
    <br><code>VISTOS, NO INTEGRADOS</code>: Yuriria, Gto., San José de Gracia, 1 detenido, 4 armas de fuego sin desglose, 7 cargadores y 166 cartuchos {RES} del boletín del 18: día y hora no fijados · Huajicori, Nay., El Huizache, 6 armas largas, 37 cargadores y 2,130 cartuchos {RES} del boletín del 18: día y hora no fijados · La Yesca, Nay., Mesa de Chapalilla, «Aseguran un lanzagranadas y mil 281 cartuchos en Nayarit», por titular (Milenio, acciones del 17): ventana de ARGOS 154 · Zapopan, ocho armas cortas {RES} del boletín del 18, frente a seis {RES} en 154: ventana de ARGOS 154 (ARG-154-011) · Monterrey, cateo de FGR y SSPC, 3 detenidos y 71 cartuchos {RES} del boletín del 18: día no fijado · Ometepec (ARG-155-010), 1 arma larga, 1 cargador y 17 cartuchos {RES} · Tepehuacán (ARG-155-011), «aseguran armas», sin cantidad · Durango, 1 arma corta, 218 cartuchos, 20 cargadores y material para explosivos, 19-nov {RES}, sin ruta (Contexto de Durango) · Culiacán, El Vino, Ejército asegura 1,000 litros y 200 kilos de químicos para metanfetamina, por titular (Noroeste), sin fecha en la ruta: precursores, fuera de la taxonomía · Acámbaro, Gto.: fecha del hecho sin fijar (17-oct o 18-nov, {RES}): <code>NO SE REINTEGRA</code>.
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
      <tr><td><b>Guerrero</b><br>Iguala (caso Los Avispones, 2014)</td><td>Exalcalde de Iguala y otras 25 personas, por titular (El Imparcial 2026/11/19); tentativa de homicidio o seis homicidios, contradicho {RES}; absuelto de delincuencia organizada {RES}</td><td>60 años, por titular (Proceso 2026/11/19; MVS 2026/11/19; La Silla Rota 2026/11/19)</td><td>Juez federal <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin comunicado de la FGR ni del Poder Judicial indexado · fecha del fallo (10 o 19-nov) {RES} · apelada: no firme {RES}</td><td>Bajo</td></tr>
      <tr><td><b>Oaxaca</b><br>Sierra de Flores Magón</td><td>Violación de una adulta mayor; boletín 2,993 de la FGEO (portal.fgeo.gob.mx)</td><td>14 años, por titular del boletín</td><td>FGEO</td><td><code>FECHA NO FIJADA</code>: ruta sin fecha; 19-nov {RES} · el titular no lleva término de condena expreso</td><td>Medio</td></tr>
      <tr><td><b>Tabasco</b><br>Villahermosa</td><td>Feminicidio; 45 años, 18-nov {RES} del índice de boletines de la FGET</td><td>no citable</td><td>FGET <span class="muted-note">(índice)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin URL individual ni dos campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Sin novedad</b></td><td>Candidatos heredados de 154 (Monterrey, Tabasco 5119, Veracruz, Champotón, Copanatoyac): sin boletín; detalle en el archivo de pendientes</td><td>—</td><td>—</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>24 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BCS, Chih, Sin, Dgo · Coah, NL, Tamps, Zac · Jal, Nay, Ags · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Ver, Tab · Gro, Oax, Chis, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> por dominio (Oaxaca: boletín sin fecha fijada)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>24</b> fiscalías estatales revisadas (Oaxaca y Tabasco, con candidato no integrable)</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio sin páginas indexadas</b></td><td>Son (<code>fiscalia.sonora.gob.mx</code>; consulta sin <code>site:</code> sin resultado en ventana; incluida en las 8 <code>NO REVISADA</code>)</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>8</b>: BC, Son · SLP · Gto, Col, Mich · Camp · Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 19-nov 18:40: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 20 entidades; solo consulta amplia en 11 —Son, Chih · NL, SLP, Zac · CDMX, Edomex, Mor, Pue, Tlax, Qro—; <code>NO REVISADA</code> (1): Dgo · <b>armamento: 21 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (11): BCS, Son, Dgo · Tamps · Edomex, Mor, Pue, Tlax, Hgo, Qro · Oax</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 17 y del 18-nov</b>: __FED17C__ · acciones del 13, 14 y 15: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al cierre · acciones del 19: <code>SIN RESULTADO INDEXADO EN VENTANA</code> al cierre · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 19-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Rojo por agravante</b>: homicidio múltiple (Michoacán); ningún ataque contra autoridades, narcobloqueo, fosa ni uso de explosivos con día fijado por ruta o titular en la ventana; {RPH} rojos por hora (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Occidente 1 · Noroeste, Noreste, Centro, Golfo y Sureste 0 (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: homicidios dolosos únicos en cinco entidades; ningún enfrentamiento derivado de un operativo.
      <br><b>4.</b> <b>Respuesta institucional</b>: dos aseguramientos integrados; tres detenciones por homicidios de ventanas anteriores, sin recalificar el delito de origen; ninguna sentencia integrable.
      <br><b>5.</b> <code>TOTALES NO COMPARABLES SIN MÁS CON LOS DE OTRAS EDICIONES: VENTANA DE 30 H, HECHOS EN FRONTERA DE VENTANA, PUBLICADOS EL DÍA DE APERTURA SIN HORA Y CON CLÁUSULA DE RETIRO (DETALLE EN TOTALES DEL CORTE). CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. DOBLE HOMICIDIO EN EL PONIENTE DE URUAPAN</b> (ARG-155-001): ataque en la vía pública o en una camioneta, lugar contradicho; huida en motocicleta, solo por resumen; móvil y autoría no informados; vínculo con hechos previos de la zona no acreditado. Línea: <b>vigilar el eje de la avenida Lenin y la colonia Rubén Jaramillo ante réplicas</b>.
      <br><b>2. ATAQUES A COMERCIANTES EN SU NEGOCIO</b> (ARG-155-002 y -005): dos dueños de minisúper asesinados el mismo día en Culiacán y Morelia; móviles no informados; vínculo entre ambos no acreditado. Línea: <b>vigilar comercios de barrio en las colonias Miguel Hidalgo (Culiacán) y Adolfo López Mateos (Morelia)</b>.
      <br><b>3. CÉLULA ARMADA DE VIGILANCIA DE DUCTOS EN TEPEACA</b> (ARG-155-009): armas largas aseguradas a un grupo dedicado al huachicol; detenidos de Veracruz y del Estado de México, solo por resumen; vínculo con otros grupos no acreditado. Línea: <b>vigilar los derechos de vía de ductos de la región de Tepeaca</b>.
      <br><b>4. DETENCIONES POR AGRESIONES A AUTORIDADES Y FIGURAS COMUNITARIAS</b> (ARG-155-010 y -011): capturas por el ataque a la casa de un alcalde en Hidalgo y por el homicidio de un líder amuzgo en Guerrero; vínculo entre los casos no acreditado. Línea: <b>dar seguimiento a la vinculación a proceso de los detenidos de ambos casos</b>.
      <br><b>5. VIOLENCIA DOMICILIARIA EN TLAXCALA</b> (ARG-155-007): irrupción armada en una vivienda de la capital, con armas largas solo por resumen; móvil de narcomenudeo, solo versión de un medio, no acreditado. Línea: <b>vigilar la zona de Ocotlán de la capital tlaxcalteca</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

FED17 = "boletín diario indexado en <code>gob.mx/sspc</code> por título; contenido <code>SOLO POR RESUMEN</code>"
arm2 = arm2.replace("__FED17__", FED17)
sent = sent.replace("__FED17C__", FED17)

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO EN URUAPAN Y HOMICIDIOS EN SINALOA", co1)
 + page("CRIMEN ORGANIZADO (II) — HOMICIDIOS EN GUANAJUATO Y MICHOACÁN", co2)
 + page("CRIMEN ORGANIZADO (III) — HOMICIDIOS EN TLAXCALA Y CAMPECHE; ACCIÓN INSTITUCIONAL EN TEPEACA", co3)
 + page("CRIMEN ORGANIZADO (IV) — ACCIONES INSTITUCIONALES: DETENCIONES EN GUERRERO, HIDALGO, QUINTANA ROO Y CHIHUAHUA", co4)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
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
# la ventana de 155 toca dos fechas de calendario (18 y 19-nov); la plantilla de 154 ya trae 2: sin reemplazo
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 154 con WINDOW_DAYS = 2"
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
