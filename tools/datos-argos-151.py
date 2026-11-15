# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 151.
Uso: python3 tools/datos-argos-151.py <plantilla ARGOS 150> <salida>
Ventana: 14-nov 10:09 → 15-nov 10:24 CDMX. Archivo: argos-2026-11-15.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "151", "2026-11-15", "10:24"
CONSULTA = "2026-11-15, última búsqueda 10:56"
DUR = "24 h 15 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 10:09 DEL 14, ES DE LA VENTANA DE ARGOS 150 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-151-001", estado="MX-VER", region="Golfo", color="rojo", impacto="grande", fecha="2026-11-14", hora="~14:20 (solo por resumen)", mu=2, he=0, cu=0, hk=14,
  ent="Veracruz", mun="Texhuacán (carretera Apoxteca–Aticpac)", dia="SÁB 14-NOV, POR RUTA",
  title="VERACRUZ · TEXHUACÁN — ASESINAN EN LA CARRETERA APOXTECA–ATICPAC A LA REGIDORA DEL AYUNTAMIENTO Y AL DIRIGENTE MUNICIPAL DEL PRI",
  hecho="Texhuacán · <code>CARRETERA ESTATAL APOXTECA–ATICPAC, SIERRA DE ZONGOLICA</code>, " + RES + " · sábado 14-NOV, por ruta (Informador 20261114: «Veracruz: asesinan a balazos a líder priísta y a regidora de Texhuacan»; Golpe Político 2026/11/14; El Independiente 2026/11/14: «ataque armado deja muertos a dirigente del PRI y a regidora en Veracruz») · ~14:20, " + RES + "; «(19:19 h)» en el titular de ADN Sureste es hora de la nota · " + FR + " · <b>2 muertos</b>, por titular: la <b>regidora del Ayuntamiento</b> y el <b>presidente del comité municipal del PRI</b> (🔴 víctima servidora pública; homicidio múltiple) · él, en el sitio; ella, horas después en hospital, " + RES + " · tercera ocupante herida, " + RES + ": no se integra · al menos 16 casquillos, " + RES + " (Plaza de Armas) · la FGE realizó diligencias, " + RES + ": no es declaración · " + NOD,
  panel="<b>Regidora y dirigente municipal del PRI asesinados</b> en carretera", inst=SB, nac="El Universal · Excélsior · Infobae", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=3, R=6, A=0,
  fechadas=["Informador (20261114)", "El Independiente (2026/11/14)", "Plumas Libres (2026/11/14)", "Golpe Político (2026/11/14)", "Infobae (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Texhuacán no figura en ninguna edición previa. Condena del PRI estatal y de MC: partidos, no autoridad. Versión distinta del dirigente nacional del PRI sobre la salud de la regidora, " + RES + ": superada por los titulares. Identidades: medios, no se reproducen."),
 dict(id="ARG-151-002", estado="MX-PUE", region="Centro", color="rojo", impacto="grande", fecha="2026-11-14", hora="tarde (solo por resumen)", mu=2, he=0, cu=0, hk=16,
  ent="Puebla", mun="Jolalpan (Huachinantla)", dia="SÁB 14-NOV, POR RESUMEN; PUB. 15-NOV, POR RUTA",
  fecha_txt="sábado 14-nov, tarde, solo por resumen; publicación 15-nov, por ruta",
  title="PUEBLA · JOLALPAN — EMBOSCAN EN HUACHINANTLA A UN MANDO POLICIAL DE AXOCHIAPAN, MOR., Y A SU ESCOLTA: DOS POLICÍAS MUERTOS",
  hecho="Jolalpan · <code>HUACHINANTLA, CARRETERA AXOCHIAPAN–HUACHINANTLA</code>, " + RES + " · tarde del sábado 14-NOV, " + DSR + " · publicación 15-NOV, por ruta (Intolerancia Diario 2026/11/15: «matan a policías de Axochiapan, Morelos, durante emboscada en Jolalpan») · " + RET + " · <b>2 policías de Morelos muertos</b> —el responsable operativo de seguridad de Axochiapan y su escolta—, por titular (Diario de Morelos: «mando policiaco de Axochiapan y su escolta mueren en enfrentamiento armado en los límites de Morelos y Puebla»; El Universal Puebla: «matan a dos policías de Morelos tras emboscada en Jolalpan») (🔴 muerte de personal de seguridad) · perseguían una camioneta con reporte de robo, por titular (Crónica Regional: «dos policías de Morelos mueren al perseguir un vehículo robado hasta Puebla») · patrullas incendiadas, " + RES + " · «cuatro muertos», por titular (Municipios Puebla; Diario Cambio: «enfrentamiento armado entre policías y civiles deja cuatro muertos en Jolalpan»), frente a dos: <code>CIFRA CONTRADICHA — SE INTEGRAN 2, MÍNIMO COINCIDENTE; NO SE ARBITRA</code> · SSPC Morelos confirmó las muertes y SSP Puebla reforzó el operativo por aire y tierra, " + RES + " · " + NOD,
  panel="<b>Emboscada a policías de Morelos: 2 muertos</b>, un mando y su escolta", inst=SB, nac="Milenio · Crónica Regional", conf="★★★☆☆",
  campo="día y hora solo por resumen; cifra de muertos contradicha (2 o 4); declaraciones de SSPC Morelos y SSP Puebla solo por resumen", I=0, N=2, R=6, A=0,
  fechadas=["Intolerancia Diario (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Jolalpan, Huachinantla y Axochiapan no figuran en las ediciones previas. Atribución a «Los Michoacanos»: un solo medio (Periódico Central), <code>NO OFICIAL</code>. «Emboscada» o «enfrentamiento» según el medio: con muerte de personal, 🔴 con independencia de quién inició. Identidades: medios, no se reproducen."),
 dict(id="ARG-151-003", estado="MX-CHP", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-14", hora="mañana (solo por resumen)", mu=0, he=0, cu=4, hk=9,
  ent="Chiapas", mun="Carretera federal 190, rumbo a Tonalá (límites con Oaxaca)", dia="SÁB 14-NOV, POR RUTA",
  title="CHIAPAS · CARRETERA 190, LÍMITES CON OAXACA — HALLAN CUATRO CUERPOS JUNTO A UNA CAMIONETA QUEMADA; SERÍAN LOS DESAPARECIDOS DE CHAHUITES",
  hecho="Carretera federal 190, rumbo a Tonalá, en los límites con San Pedro Tapanatepec, Oax., por titular (Infobae 2026/11/15: «autoridades localizan cuatro cuerpos calcinados en la carretera 190, rumbo a Tonalá, Chiapas: serían los desaparecidos de Chahuites») · sábado 14-NOV, por ruta (La Jornada 2026/11/14: «hallan cuatro cuerpos calcinados en límites de Chiapas y Oaxaca») · mañana, " + RES + "; «10:35 h» en el titular de ADN Sureste es hora del comunicado de la FGEO, no del hallazgo · " + FR + " · <b>4 cuerpos</b>, por titular (🔴 cuerpos hallados; víctimas privadas de la libertad) · <code>CALCINADOS: 4, POR TITULAR (LA JORNADA; INFOBAE), FRENTE A 2, POR TITULAR (QUADRATÍN: «HALLAN 4 CUERPOS EN LÍMITES DE OAXACA Y CHIAPAS; 2 CALCINADOS»)</code> · junto a la camioneta en que viajaban, quemada, " + RES + " · «serían empresario y escoltas desaparecidos», por titular (El Diario de Chihuahua 2026/nov/14); desaparición en Chahuites, Oax., el 11-NOV, " + RES + " · «policías auxiliares» en una versión, " + RES + ": <code>CONDICIÓN DE LAS VÍCTIMAS CONTRADICHA</code> · Fiscalía de Oaxaca confirma el hallazgo en Chiapas, por titular de medio (Quadratín Oaxaca: «confirma Fiscalía de Oaxaca hallazgo de 4 cuerpos en Chiapas»; Primera Línea 2026/11/14: «en colaboración interestatal, fiscalías de Oaxaca y Chiapas localizan cuatro cuerpos sin vida») · identificación no definitiva · " + NOD,
  panel="<b>4 cuerpos</b> junto a una camioneta quemada; serían los desaparecidos de Chahuites", inst="Fiscalía de Oaxaca <span class=\"muted-note\">(por titular de medio; comunicado no leído)</span>", nac="La Jornada · Infobae · Milenio", conf="★★★☆☆",
  campo="hora del hallazgo solo por resumen; número de calcinados contradicho; identificación no definitiva", I=1, N=3, R=4, A=0,
  fechadas=["La Jornada (2026/11/14)", "Primera Línea (2026/11/14)", "El Diario de Chihuahua (2026/nov/14)", "Infobae (2026/11/15)", "Zolo (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chahuites no figura en las ediciones previas; Tapanatepec, solo en una ficha de septiembre: otro hecho. La desaparición del 11-NOV no se publicó en ARGOS 150: antecedente, sin ficha propia. Cuerpos sin causa de muerte informada por autoridad: van a «cuerpos o restos». Identidades: medios, no se reproducen."),
 dict(id="ARG-151-009", estado="MX-HID", region="Centro", color="rojo", impacto="grande", fecha="2026-11-14", hora="~02:00 (solo por resumen)", mu=2, he=0, cu=0, hk=2,
  ent="Hidalgo", mun="Tepehuacán de Guerrero (Acoxcatlán)", dia="SÁB 14-NOV, POR RUTA; MADRUGADA, POR RESUMEN",
  fecha_txt="sábado 14-nov, por ruta; ~02:00, solo por resumen",
  title="HIDALGO · TEPEHUACÁN DE GUERRERO — COMANDO IRRUMPE EN LA VIVIENDA DEL ALCALDE EN ACOXCATLÁN: DOS POLICÍAS MUNICIPALES MUERTOS",
  hecho="Tepehuacán de Guerrero · <code>COMUNIDAD DE ACOXCATLÁN, VIVIENDA DEL PRESIDENTE MUNICIPAL</code> · sábado 14-NOV, por ruta (Proceso 2026/11/14: «balean inmueble del alcalde de Tepehuacán de Guerrero; hay un policía muerto y otro herido»; Tribuna 2026/11/14: «comando armado irrumpe en domicilio del alcalde de Tepehuacán, Hidalgo, y deja dos policías muertos») · ~02:00, " + RES + " · " + FR + " · " + RET + " · <b>2 policías municipales muertos</b>, por titular (Milenio: «dos policías murieron en ataque armado domicilio alcalde Tepehuacán»; La Jornada 2026/11/15: «fallecen dos policías municipales tras ataque a edil de Tepehuacán») (🔴 víctimas autoridad); el segundo, en el hospital, a hora no informada, " + RES + " · alcalde ausente; otros dos custodios sometidos, " + RES + " · la PGJEH identificó a tres presuntos responsables; búsqueda de una caja fuerte, " + RES + " (subprocurador, a través de medios) · " + NOD,
  panel="<b>Ataque a la vivienda del alcalde: 2 policías municipales muertos</b>", inst=SB, nac="Proceso · El Universal · Milenio · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen frente a la apertura de las 10:09; declaración de la PGJEH solo por resumen", I=0, N=4, R=3, A=0,
  fechadas=["Proceso (2026/11/14)", "Heraldo de México (2026/11/14)", "Tribuna (2026/11/14)", "La Jornada (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepehuacán y Acoxcatlán no figuran en las ediciones previas. Publicado el día de cierre de ARGOS 150 sin hora por fragmento: se integra en esta edición, la primera que lo ve. Móvil de robo: extraoficial; vínculo con delincuencia organizada descartado por autoridades estatales, " + RES + ". Identidades: medios, no se reproducen."),
 # ======================= AMARILLOS
 dict(id="ARG-151-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-14", hora="noche (solo por resumen)", mu=1, he=1, cu=0, hk=23,
  ent="Sinaloa", mun="Mazatlán (Zona Dorada, av. Camarón Sábalo)", dia="SÁB 14-NOV, POR RESUMEN; PUB. 15-NOV, POR RUTA",
  fecha_txt="noche del sábado 14-nov, solo por resumen; publicación 15-nov, por ruta",
  title="SINALOA · MAZATLÁN — ATAQUE ARMADO EN UN BAR DE LA ZONA DORADA: UN MUERTO Y UN HERIDO",
  hecho="Mazatlán · <code>BAR DE LA AV. CAMARÓN SÁBALO, ZONA DORADA, POR TITULAR</code> · «últimos minutos de este sábado», " + RES + " · publicación 15-NOV, por ruta (Luz Noticias 2026-11-15: «ataque armado en antro bar de la Zona Dorada deja un muerto y un herido en Mazatlán»; Línea Directa 2026-11-15: «agresión armada deja a un hombre sin vida y un herido en bar de la Camarón Sábalo») · <b>1 muerto y 1 herido</b>, por titular (🟡 homicidio doloso único) · víctima, personal de seguridad del lugar, " + RES + " · la Fiscalía realiza diligencias, " + RES + " · " + NOD,
  panel="Ataque en un bar: <b>1 muerto y 1 herido</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="día y hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-11-15)", "Línea Directa (2026-11-15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Zona Dorada y Camarón Sábalo no figuran en las ediciones previas. «Vigilante del bar … fallece y cliente resulta lesionado» (Sinaloahoy, madrugada del domingo): probable mismo hecho, no se suma."),
 dict(id="ARG-151-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-15", hora="noche del 14 o madrugada del 15 (solo por resumen)", mu=1, he=4, cu=0, hk=2,
  ent="Sinaloa", mun="Mazatlán (col. 12 de Mayo)", dia="14 O 15-NOV; PUB. 15-NOV, POR RUTA",
  fecha_txt="noche del 14 o madrugada del 15-nov, contradicho; publicación 15-nov, por ruta",
  title="SINALOA · MAZATLÁN — BALACERA EN UNA REUNIÓN EN LA COLONIA 12 DE MAYO: UN MUERTO Y CUATRO HERIDOS",
  hecho="Mazatlán · <code>COL. 12 DE MAYO, POR TITULAR</code> · publicación 15-NOV, por ruta (Luz Noticias 2026-11-15: «balacera deja un muerto y cuatro heridos en la colonia 12 de Mayo de Mazatlán») · <code>MOMENTO CONTRADICHO</code>: noche del sábado 14 o madrugada del domingo 15, " + RES + "; dentro de la ventana en ambas versiones · <b>1 muerto y 4 heridos</b>, por titular (Los Noticieristas 2026/11; Noroeste: «ataque en vivienda de la 12 de Mayo deja un hombre sin vida y 4 heridos») (🟡 homicidio doloso único) · reunión en una vivienda, " + RES + " · " + NOD,
  panel="Balacera en una reunión: <b>1 muerto y 4 heridos</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="momento del ataque contradicho; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-11-15)"], estatus="Parcialmente corroborado", arm=None,
  desl="12 de Mayo no figura en las ediciones previas. Mismo criterio de color que ARG-140-011 (1 muerto y 3 heridos: 🟡)."),
 dict(id="ARG-151-006", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-15", hora="madrugada; reporte ~03:30 (solo por resumen)", mu=1, he=0, cu=0, hk=4,
  ent="Sinaloa", mun="Culiacán (col. Esthela Ortiz de Domínguez)", dia="DOM 15-NOV, POR RESUMEN; PUB. 15-NOV, POR RUTA",
  fecha_txt="madrugada del domingo 15-nov, solo por resumen; publicación 15-nov, por ruta",
  title="SINALOA · CULIACÁN — MUERE EN EL HOSPITAL UN HOMBRE ATACADO A BALAZOS EN LA COLONIA ESTHELA ORTIZ",
  hecho="Culiacán · <code>COL. ESTHELA ORTIZ DE DOMÍNGUEZ, POR TITULAR</code> · madrugada del domingo 15-NOV, " + RES + "; reporte ~03:30 y traslado al hospital ~05:30, " + RES + " · publicación 15-NOV, por ruta (Luz Noticias 2026-11-15: «muere hombre tras ser atacado a balazos en la colonia Esthela Ortiz de Culiacán») · <b>1 hombre muerto</b> en el hospital, por titular (Noroeste: «muere hombre tras ataque a tiros en la colonia Esthela Ortiz») (🟡 homicidio doloso único) · Policía Estatal Preventiva y Cruz Roja; la Fiscalía, a cargo, " + RES + " · " + NOD,
  panel="<b>Hombre muerto</b> tras ataque a balazos", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen y discrepante; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-11-15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Estela/Esthela Ortiz en el índice: ARG-136-004 (17-oct, joven asesinado en una tienda de conveniencia, 🟡): otro hecho, cuatro semanas antes. Única ruta fechada de este hecho: Luz Noticias 2026-11-15."),
 # ======================= VERDES
 dict(id="ARG-151-007", estado="MX-SON", region="Noroeste", color="verde", impacto="grande", fecha="2026-11-14", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Sonora", mun="Nogales", dia="PUB. 14-NOV, POR RUTA",
  fecha_txt="publicación sábado 14-nov, por ruta; hora no fijada",
  title="SONORA · NOGALES — MILITARES DETIENEN A TRES PERSONAS CON 1,229 CARTUCHOS ÚTILES",
  hecho="Nogales · publicación sábado 14-NOV, por ruta (El Imparcial 2026/11/14: «militares detienen a tres con mil 229 cartuchos útiles en Nogales») · " + FR + " · <b>1,229 cartuchos útiles</b>, por titular · Ejército, por titular; GN y Policía Estatal, col. Del Rosario, " + RES + " · " + NDA + " (3, por titular) · " + FU,
  panel="<b>1,229 cartuchos</b> asegurados por el Ejército", inst=SB, nac="—", conf="★★☆☆☆",
  campo="una sola fuente; hora no fijada frente a la apertura; ninguna fuente institucional", I=0, N=0, R=1, A=0,
  fechadas=["El Imparcial (2026/11/14)"], estatus="Pendiente de corroboración", arm="ARG-151-ARM-001",
  desl="Nogales en el índice: ARG-96-SEN-005 (sentencia) y ARG-135-REC-004 (fosas): otros hechos; sin aseguramiento previo con esta cifra. Si resulta anterior a las 10:09 del 14, es de la ventana de ARGOS 150."),
 dict(id="ARG-151-008", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-14", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Sinaloa", mun="Mazatlán", dia="PUB. 14-NOV, POR RUTA",
  fecha_txt="publicación sábado 14-nov, por ruta; hora no fijada",
  title="SINALOA · MAZATLÁN — PERSECUCIÓN DEL EJÉRCITO TERMINA CON UN DETENIDO Y DOS FUSILES ASEGURADOS",
  hecho="Mazatlán · publicación sábado 14-NOV, por ruta (Luz Noticias 2026-11-14: «persecución del Ejército termina con un detenido, dos fusiles y un auto asegurados en Mazatlán») · " + FR + " · <b>2 fusiles</b> y 1 automóvil, por titular · Ejército, por titular · " + NDA + " (1, por titular) · una sola fuente con día en la ruta; la corroboran, por titular y sin día en la ruta, Noroeste («detiene Ejército a un hombre tras disparar contra vivienda en la Flores Magón»), Sinaloahoy y Los Noticieristas · la persecución empezó tras disparos contra una vivienda de la col. Flores Magón, por titular: sin víctimas publicadas ni ruta con día, <b>no se ficha como hecho propio</b> (🟡, visto)",
  panel="<b>2 fusiles</b> asegurados tras una persecución del Ejército", inst=SB, nac="—", conf="★★☆☆☆",
  campo="una sola fuente con día en la ruta; hora no fijada frente a la apertura; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-11-14)"], estatus="Pendiente de corroboración", arm="ARG-151-ARM-002",
  desl="Sin enfrentamiento con la autoridad publicado: 🟢. Los disparos contra la vivienda: visto, sin ficha (sin víctimas publicadas). Mazatlán, El Roble (12-nov, 2 largas, 8 cargadores, 210 cartuchos, 2 detenidos; visto en ARGOS 150): otro hecho. Si resulta anterior a las 10:09 del 14, es de la ventana de ARGOS 150."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-151-REC-001", estado="MX-JAL", region="Occidente", fecha="2026-11-08", hora="no fijada", orig="ARGOS 149", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Jalisco", mun="El Arenal (ejido Huaxla)", dia="SÁB 7 O DOM 8-NOV, CONTRADICHO",
  title="JALISCO · EL ARENAL — LOCALIZAN SIN VIDA, CON IMPACTOS DE BALA, A UNA PAREJA DESAPARECIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 149</code> · El Arenal · brecha del ejido Huaxla, " + RES + " · <code>DÍA DEL HALLAZGO CONTRADICHO</code>: sábado 7 o domingo 8-NOV, " + RES + "; ambos dentro de la ventana de ARGOS 149 · publicación 9-NOV, por ruta (Crónica Jalisco 2026/11/09: «investigan asesinato de pareja en El Arenal; estaban desaparecidos») · <b>2 muertos</b>, por titular (Milenio: «localizan sin vida a pareja desaparecida en El Arenal, Jalisco») (🔴 homicidio múltiple) · <code>CAUSA CONTRADICHA</code>: impactos de arma de fuego o lesiones en el cráneo, " + RES + " · desaparecidos días antes, " + RES,
  panel="<b>Pareja desaparecida localizada sin vida: 2 muertos</b>", inst=SB, nac="Milenio",
  conf="★★★☆☆", campo="día del hallazgo y causa contradichos, solo por resumen; ninguna fuente institucional", I=0, N=1, R=1, A=0,
  fechadas=["Crónica Jalisco (2026/11/09)"],
  desl="Visto sin ruta en ARGOS 150 (rojos sin ruta: «El Arenal, Jal.»). Si el hallazgo resultara posterior a las 16:07 del 9-nov, es de la ventana de ARGOS 150. No es ARG-150-016 (col. El Arenal, Tlalnepantla): otra entidad. Identidades: medios, no se reproducen."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-151-ARM-001", ficha="ARG-151-007", estado="MX-SON", region="Noroeste", color="verde", ent="Sonora", mun="Nogales",
  fecha="2026-11-14", fecha_txt="pub. 14-nov, por ruta; hora no fijada", hora="no fijada", c=[0, 0, 0, 0, 1229, 0, 0, 0, 0, 0], nd=[0, 1, 2, 3, 5, 6, 7, 8, 9], integra=True,
  corp="Ejército <span class=\"muted-note\">(por titular de medio)</span>", conf="Bajo",
  nota="1,229 cartuchos por un solo titular fechado (El Imparcial 2026/11/14); 3 detenidos por titular de medio, sin cifra de autoridad: n/d; resto de categorías no publicado: n/d; FRONTERA DE VENTANA — HORA NO FIJADA; ver ARG-151-007",
  fuentes=["El Imparcial (2026/11/14)"]),
 dict(id="ARG-151-ARM-002", ficha="ARG-151-008", estado="MX-SIN", region="Noroeste", color="verde", ent="Sinaloa", mun="Mazatlán",
  fecha="2026-11-14", fecha_txt="pub. 14-nov, por ruta; hora no fijada", hora="no fijada", c=[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], nd=[0, 2, 3, 4, 5, 6, 7, 8, 9], integra=True,
  corp="Ejército <span class=\"muted-note\">(por titular de medio)</span>", conf="Bajo",
  nota="2 fusiles (armas largas) por un solo titular fechado (Luz Noticias 2026-11-14); 1 detenido por titular de medio, sin cifra de autoridad: n/d; FRONTERA DE VENTANA — HORA NO FIJADA; ver ARG-151-008",
  fuentes=["Luz Noticias (2026-11-14)"]),
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
HORAS = 24 + 15 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 2, 0, 0, 1229, 0, 0, 0, 0, 0], (TOT, ND)
assert ND == [True, False, True, True, False, True, True, True, True, True], ND
assert cnt == {"rojo": 4, "amarillo": 3, "verde": 2}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (9, 5, 4, 2, 0, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,37", DENS
assert (NAP, NFR, NRET) == (0, 5, 2), (NAP, NFR, NRET)
assert len(ENT) == 6 and len(ENT_ROJO) == 4, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-151-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-151-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-11-14" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-11-14", x["id"]
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
head = head.replace("<title>ARGOS 150 — Reporte Nacional de Seguridad — 2026-11-14</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LAS FISCALÍAS DE VERACRUZ E HIDALGO LOS PARTES DE TEXHUACÁN Y TEPEHUACÁN —CASQUILLOS Y CALIBRES— Y LAS MEDIDAS DE PROTECCIÓN VIGENTES PARA AMBOS CABILDOS</b> (ARG-151-001 y -009).
      <br><b>2. SOLICITE A LA SSP DE PUEBLA Y A LA SSPC DE MORELOS EL PARTE CONJUNTO DE JOLALPAN Y EL PROTOCOLO DE PERSECUCIÓN ENTRE ENTIDADES; VIGILE LA CARRETERA AXOCHIAPAN–HUACHINANTLA</b> (ARG-151-002).
      <br><b>3. SOLICITE A LAS FISCALÍAS DE OAXACA Y CHIAPAS LA IDENTIFICACIÓN DE LOS CUERPOS DE LA CARRETERA 190 Y SU CRUCE CON LA DENUNCIA DE DESAPARICIÓN DE CHAHUITES</b> (ARG-151-003).
      <br><b>4. SOLICITE A LA FISCALÍA DE SINALOA EL COTEJO BALÍSTICO DE LOS TRES ATAQUES DEL FIN DE SEMANA EN MAZATLÁN Y CULIACÁN</b> (ARG-151-004 a -006).
      <br><b>5. SOLICITE A LA DEFENSA EL INVENTARIO OFICIAL Y EL RASTREO DE LOTE DE LOS CARTUCHOS DE NOGALES Y DE LOS FUSILES DE MAZATLÁN</b> (ARG-151-007 y -008).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>14-nov 10:09 → 15-nov 10:24 CDMX</b> (<b>{DUR}</b>) · sáb 14 (desde 10:09) · dom 15 (hasta 10:24) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperación de alto impacto</b> (ventana de ARGOS 149), atenuada, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: desglose en su página; cifras de un solo titular cada una (mínimos) · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas · <b>heridos</b>: {HE}; la tercera ocupante de Texhuacán, solo por resumen, fuera · <b>cuerpos o restos</b>: {CU} (carretera 190), sin causa de muerte informada por autoridad · <b>detenidos</b>: Nogales 3 y Mazatlán 1, solo por titular de medio, sin cifra de autoridad: n/d · <b>marcas</b>: {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (Texhuacán, carretera 190, Tepehuacán, Nogales y Mazatlán: publicados el día de apertura) · <b>totales sujetos a {NRET} cláusulas de retiro</b> (Jolalpan, día solo por resumen; Tepehuacán, ~02:00 por resumen) · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos, por titular.
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «jornada violenta en Mazatlán deja cuatro muertos y cinco heridos» (El Universal) · «Michoacán llega a 36 policías asesinados» (La Silla Rota 2026/11/13).
    <br><code>ROJO SIN RUTA FECHADA — CANDIDATO NO FICHADO</code>: <b>Chignahuapan, Pue., Cuautelolulco</b>: ataque armado con 5 muertos, madrugada del domingo 15 {RES}; dos titulares (MTP Noticias; El Quinto Medio 2026/11: «saldo preliminar de 5 personas muertas»), ninguno con día en la ruta; sin confirmación oficial.
    <br><b>Vistos, fuera de totales</b> (sin ruta con día, hora frente a la apertura no fijada, fuente única o de la ventana anterior): Mazatlán, col. Azteca (hombre asesinado «la mañana del sábado 14», {RES}; si fue antes de las 10:09, de la ventana de 150) · Mazatlán, fiesta en la col. Pueblo Nuevo (1 muerto) y av. Emilio Barragán (2 heridos), sin día en la ruta · San José del Cabo, Villas de Cortés, joven herido (Península Digital 2026/11/14), fuente única · Apatzingán, motociclista asesinado (RED Michoacán 2026/11/14), hora no fijada · El Salto, Jal., riña en un puesto de comida · Saltillo, cuerpo en una caseta policial abandonada, sin día · Ciudad Valles, dos camionetas incendiadas antes de las 05:00 del 14 {RES} · Zitácuaro, bloqueo de pobladores el 14 (Seuno 2026/11/14), desarrollo de ARG-150-001, protesta civil · Matías Romero, Oax., bloqueo por la detención de un periodista: protesta · Cajeme, Son., la FGJES detiene a un hombre y realiza cateos (El Imparcial 2026/11/14): sin hecho previo publicado · Colima, la Marina captura a un presunto jefe de sicarios ligado a una masacre en una panadería (Infobae 2026/11/14; detención del 13 {RES}) · Matamoros, «Los Ciclones»: agresión a fuerzas federales y 4 detenidos (ABC 2026/11/13), ventana de 150; no es ARG-144-008.
    <br><code>FE DE ERRATAS — ARGOS 150 Y 149</code>: <b>un rojo de la ventana de 149 se recupera</b> (El Arenal): <b>11 rojos, 7 amarillos, 7 verdes</b> (cálculo propio) · <b>ARG-150-002</b>: heridos: 2 por titular (Zócalo), 3 por titular (Posta): <code>HERIDOS CONTRADICHOS</code>, sin cambio · <b>ARG-150-003</b>: Defensa, por titular de medio (Infobae 2026/11/13: «Defensa reporta como saldo dos criminales abatidos y un hondureño detenido») · <b>ARG-150-020</b>: «13 armas», segundo titular (Latinus 2026/11/13), no reverificado en control; desglose solo por resumen · <b>ARG-150-016</b>: el herido, con segunda nota (La Jornada Estado de México, {RES}); sigue ★★☆☆☆ · <b>ARG-150-REC-001</b>: «cuatro detenidos por asesinato múltiple en una taquería de Tecate» (Uniradio) es el ataque del 4-jul-2026 (La Jornada 2026/07/07): se retira de la ficha · <b>ARG-150-REC-002</b>: ningún detenido publicado: se retira «1 detenido según un solo medio» · <b>rojos sin ruta de 150 retirados</b>: Viesca y Reynosa, Puerta Sur (tercera edición sin ruta con día) · Colima, «3 muertos y 15 detenidos» (es de junio de 2025: El Financiero 2025/06/23) · Atotonilco el Alto (quema de dos camiones el 12-nov, Diario Puntual 2026/11/13): 🟡, bloqueo aislado, ventana de 150, visto sin ficha, no se integra al semáforo de 150; García Harfuch «descarta narcobloqueos», por titular.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Zapopan (ARG-149-014 / -018)</b>: 15 de los 20 detenidos liberados y 5 imputados, por titular (N+) · <code>NO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-151-{i:03d}"]) for i in (1, 2, 9, 3))
co2 = "\n".join(ficha(byid[f"ARG-151-{i:03d}"]) for i in (4, 5, 6, 7, 8))
co3 = "\n".join(ficha(rbyid[f"ARG-151-REC-{i:03d}"], True) for i in (1,))
assert sorted(re.findall(r'id="(ARG-151-0\d\d)"', co1 + co2)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-151-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "Mazatlán: 2 fusiles, por titular"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "Nogales: 1,229, por titular"),
 tile(4, "Cargadores", tv(5), NI),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: Nogales 3 y Mazatlán 1, solo por titular de medio, sin cifra de autoridad"),
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

armrows = "\n".join(armrow(a) for a in ARM)
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
    <b>Lectura regional</b>: Noroeste, 2 largas y 1,229 cartuchos (Sinaloa y Sonora, Ejército en ambos); Noreste, Occidente, Centro, Golfo y Sureste, sin arma integrada. <b>Cálculo propio</b>.
    <br><code>BOLETÍN FEDERAL DE ACCIONES DEL 13, 14 Y 15-NOV: SIN RESULTADO INDEXADO EN VENTANA</code> (día suelto, rango y título, al inicio y al cierre); el fin de semana puede publicarse agregado.
    <br><code>VISTOS, NO INTEGRADOS</code>: Ciudad Victoria, 3 detenidos, 2 armas, 58 cargadores y unos 2,000 cartuchos {RES} (El Independiente 2026/11/14): <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> con Nuevo Laredo, Villas de San Miguel, boletín del 12 · Matamoros, Barrett .50, 3 largas, 14 cargadores y 1,200 cartuchos {RES} (ABC 2026/11/13): ventana de 150 · Cajeme, arma 9 mm sin cifra de autoridad: seguimiento · Edomex, Operativo Otomí, 65 cortas y 17 largas en 50 días {RES}: acumulado.
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
      <tr><td><b>Nuevo León</b><br>Monterrey</td><td>Homicidio («asesinato», por titular; MVS 2026/11/13); 1 sentenciado</td><td>25 años por homicidio y 10 meses por delitos contra la salud, {RES}: <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>Fiscalía de NL <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín · ventana de ARGOS 150</td><td>Bajo</td></tr>
      <tr><td><b>Tabasco</b><br>Jalpa de Méndez</td><td>Pederastia; boletín FGET 5119, fechado el 9-nov por el listado del dominio; <code>POSIBLE CASO HOMÓNIMO</code></td><td>30 años, por titular del listado</td><td>FGE Tabasco <span class="muted-note">(listado del dominio)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · texto no leído · ventana de ARGOS 150</td><td>Bajo</td></tr>
      <tr><td><b>Sin novedad</b></td><td>Veracruz, 88 años (Hoy Xalapa 2026/11/13) · Champotón, 66 años, por titular (PorEsto 2026/11/6): ya vistos en ARGOS 150</td><td>—</td><td>—</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>18 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BCS, Dgo · NL · Jal, Col, Nay, Gto · CDMX, Edomex, Pue, Tlax · Ver, Tab · Oax, Chis, Gro, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> · candidatos de la tabla: publicados antes de la ventana</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>18</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio de la fiscalía no confirmado</b></td><td>Camp (incluida en las 14 <code>NO REVISADA</code>)</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>14</b>: BC, Son, Sin, Chih · Tamps, Coah, Zac, SLP · Mich, Ags · Mor, Hgo, Qro · Camp</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 15-nov 10:24: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 18 entidades; solo consulta amplia en 14 —BC, Son, Chih, Dgo · NL, Zac, SLP · CDMX, Edomex, Tlax, Qro · Chis, Gro, QRoo— · <b>armamento: 15 de 32 por dominio oficial</b> —Sin, Dgo · NL, Tamps, Coah, Zac · Mich · CDMX, Pue · Ver, Tab · Chis, Camp, Yuc, QRoo—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (17): BC, BCS, Son, Chih · SLP · Jal, Gto, Col, Nay, Ags · Edomex, Hgo, Mor, Tlax, Qro · Oax, Gro</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 13, 14 y 15-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio y al cierre · último indexado: acciones del 12-nov (Milenio, Ultranoticias, SICOM, RED113, Tallapolítica, Certeza Diario) · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 15-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Cuatro rojos propios en cuatro entidades</b>: 0,16 rojos por hora (4 en {DUR}), frente a 0,10 en ARGOS 150 (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Centro 2 · Golfo 1 · Sureste 1 · Noroeste, Noreste y Occidente 0 (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: tres amarillos, los tres en Sinaloa (Mazatlán 2, Culiacán 1).
      <br><b>4.</b> <b>Respuesta institucional</b>: dos verdes del Ejército en el Noroeste; ninguna sentencia integrable (totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE FIN DE SEMANA DE {DUR.upper()}, SIN BOLETÍN FEDERAL INDEXADO; CINCO HECHOS EN FRONTERA DE VENTANA Y DOS CON CLÁUSULAS DE RETIRO: TOTALES NO COMPARABLES SIN MÁS. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. AUTORIDADES MUNICIPALES ATACADAS FUERA DE UN DISPOSITIVO DE SEGURIDAD: REGIDORA EN CARRETERA SERRANA Y VIVIENDA DE UN ALCALDE CUSTODIADA POR POLICÍAS</b> (ARG-151-001 y -009): en ambos, el blanco se desplazaba o residía en zona rural; móviles no informados por autoridad y vínculo entre hechos no acreditado. Línea: <b>solicitar a las fiscalías de Veracruz e Hidalgo el análisis de riesgo de los cabildos de la sierra</b>.
      <br><b>2. LÍMITE MORELOS–PUEBLA: UNA PERSECUCIÓN POR ROBO DE VEHÍCULO TERMINA EN EMBOSCADA AL CRUZAR DE ENTIDAD</b> (ARG-151-002): es consistente con el uso del límite estatal como zona de repliegue preparada; atribución a un grupo solo en un medio no oficial. Línea: <b>vigilar la carretera Axochiapan–Huachinantla y revisar el protocolo de persecución entre entidades</b>.
      <br><b>3. COSTA DE CHIAPAS: VÍCTIMAS PRIVADAS DE LA LIBERTAD EN OAXACA APARECEN MUERTAS Y QUEMADAS EN OTRA ENTIDAD, SOBRE LA CARRETERA 190</b> (ARG-151-003): el traslado entre entidades es consistente con un cruce de jurisdicción que dificulta la investigación; identidad no confirmada. Línea: <b>solicitar una carpeta coordinada FGEO–FGE Chiapas</b>.
      <br><b>4. MAZATLÁN: DOS ATAQUES CON SIETE VÍCTIMAS —2 MUERTOS Y 5 HERIDOS, CÁLCULO PROPIO— EN UNA NOCHE, EN LA ZONA TURÍSTICA Y EN UNA COLONIA HABITACIONAL</b> (ARG-151-004 y -005): blancos en reuniones y establecimientos nocturnos; vínculo con disputa criminal no acreditado. Línea: <b>vigilar la Zona Dorada en horario nocturno de fin de semana</b>.
      <br><b>5. MUNICIÓN EN VOLUMEN EN LA FRANJA FRONTERIZA DE SONORA</b> (ARG-151-007): 1,229 cartuchos en un solo aseguramiento, por titular, es consistente con abastecimiento de células más que con dotación individual; origen y calibre no publicados. Línea: <b>solicitar a la Defensa el calibre y el rastreo de lote</b>.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: AUTORIDADES Y CUERPOS HALLADOS", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA Y ACCIONES INSTITUCIONALES", co2)
 + page("CRIMEN ORGANIZADO (III) — ALTO IMPACTO DE LA VENTANA DE ARGOS 149: EL ARENAL", co3)
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
# la ventana de 151 toca dos fechas de calendario (14 y 15-nov); la plantilla de 150 trae 6
assert script.count("WINDOW_DAYS = 6;") == 1, "plantilla de 150 con WINDOW_DAYS = 6"
script = script.replace("WINDOW_DAYS = 6;", "WINDOW_DAYS = 2;")
assert script.count("WINDOW_DAYS = 2;") == 1 and "WINDOW_DAYS = 6;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
