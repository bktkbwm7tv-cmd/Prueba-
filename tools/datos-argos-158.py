# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 158.
Uso: python3 tools/datos-argos-158.py <plantilla ARGOS 157> <salida>
Ventana: 23-nov 08:35 → 26-nov 13:44 CDMX (77 h 09 min; lun 23 · mar 24 · mié 25 · jue 26). Archivo: argos-2026-11-26.html.
La hora de «Consulta» se fija al cierre de procedencia-cifras R2 con la variable ARGOS_CONSULTA (HH:MM)."""
import sys, re, json, os, html as H

NUM, FECHA, HORA = "158", "2026-11-26", "13:44"
CONSULTA = "2026-11-26, última búsqueda " + os.environ.get("ARGOS_CONSULTA", "__CONSULTA__")
DUR = "77 h 09 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 08:35 DEL 23, ES DE LA VENTANA DE ARGOS 157 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
PUB = "Publicado el día de apertura sin hora por fragmento: se integra en esta edición, la primera que lo ve."
TM = " <span class=\"muted-note\">(por titular de medio)</span>"
QNI = "<code>QUIÉN INICIÓ NO DETERMINADO</code>"
CND = "<code>CANTIDAD NO DETERMINADA</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada por autoridad
# (cálculo propio derivado del arreglo, nunca escrito a mano). Agresores abatidos: fuera de mu.
DPR = "<code>DÍA SOLO POR RESUMEN</code>"
INS = " <span class=\"muted-note\">(institucional, portal oficial)</span>"
E = [
 # ======================= ROJOS
 dict(id="ARG-158-001", estado="MX-SON", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-23", hora="reporte ~10:01 (solo por resumen)", mu=0, he=0, cu=5, hk=10,
  ent="Sonora", mun="Santa Ana", dia="LUN 23-NOV, POR RUTA",
  fecha_txt="lunes 23-nov, por ruta; reporte ~10:01, solo por resumen",
  title="SONORA · SANTA ANA — HALLAN CINCO HOMBRES MUERTOS DENTRO DE UNA CAMIONETA BLINDADA",
  hecho="Santa Ana · norte de Sonora, por titular · lunes 23-NOV, por ruta (La Jornada 2026/11/23: «Hallan cinco hombres muertos dentro de camioneta blindada en Santa Ana, Sonora»; El Heraldo de México 2026/11/23: «Hallan a cinco personas sin vida dentro de una camioneta blindada en Santa Ana, Sonora»; El Diario de Chihuahua 2026/nov/23: «Hallan a cinco hombres asesinados en norte de Sonora») · reporte a la FGJES ~10:01, " + RES + " · " + RET + " · <b>5 hombres muertos</b>, por titular; «ejecutados», por titular (Aristegui «2311»: «Hallan cinco hombres ejecutados en Sonora») (🔴 homicidio múltiple) · causa de muerte no informada por la autoridad: <b>se cuentan como cuerpos hallados</b> · chalecos antibalas y 4 armas largas en la escena, " + RES + ": " + CND + " · FGJES investiga, por titular (Radio Sonora: «Investiga Fiscalía de Sonora hallazgo de cinco hombres sin vida en Santa Ana») · vínculo con una estructura criminal, " + RES + ": <code>NO ACREDITADO</code> · " + NOD,
  panel="<b>5 hombres muertos</b> en camioneta blindada", inst=SB, nac="La Jornada · El Heraldo de México · Aristegui", conf="★★★☆☆",
  campo="hora solo por resumen en el día de apertura; causa de muerte no informada por autoridad", I=0, N=3, R=2, A=0,
  fechadas=["La Jornada (2026/11/23)", "El Heraldo de México (2026/11/23)", "El Diario de Chihuahua (2026/nov/23)"], estatus="Parcialmente corroborado", arm=None, cual=True,
  desl="Santa Ana, Sonora, no figura en ediciones previas (ARG-145-008 es Santa Ana de Mazatlán: otro hecho). La Opinión 2026/11/24 «Descubren 5 cuerpos sin vida dentro de una camioneta blindada en Sonora»: misma escena, publicación posterior. «Investiga Fiscalía» no es declaración nombrada: Institucional 0. Identidades: no se reproducen."),
 dict(id="ARG-158-002", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-25", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Michoacán–Jalisco", mun="Peribán – Jilotlán de los Dolores (brecha limítrofe)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; hora no fijada",
  title="MICHOACÁN–JALISCO · PERIBÁN – JILOTLÁN — AGREDEN A MILITARES EN RECONOCIMIENTO: SIETE AGRESORES ABATIDOS (OPERACIÓN «ERANDI»)",
  hecho="Brecha entre Peribán (Mich.) y Doctor Villa Gómez, Jilotlán de los Dolores (Jal.), " + RES + "; «en Michoacán», por titular (Tribuna), «en Jalisco», por titular (ABC Noticias): <code>ENTIDAD CONTRADICHA</code> · miércoles 25-NOV, por ruta (ABC Noticias 2026/11/25: «Abaten a siete y detienen a 10 tras operativo militar en Jalisco»; Tribuna 2026/11/25: «Militares se enfrentan al Cártel de los Reyes en Michoacán; hay siete abatidos y 10 detenidos») · hora no fijada · militares <b>agredidos durante reconocimientos sobre una brecha</b>, declaración de la Defensa " + RES + "; «Ejército repele agresión», por titular (Yahoo) (🔴 el grupo agrede a personal militar en patrullaje) · «operativo contra “el Maniaco”», por titular (López-Dóriga): <code>QUIÉN INICIÓ — VERSIÓN DE LA DEFENSA CITADA POR MEDIOS</code> · <b>7 agresores abatidos</b>, por titular (Infobae 2026/11/26: «Defensa confirma siete criminales abatidos y 10 detenidos tras enfrentamiento contra célula del Cártel de los Reyes»): no se suman a muertos por agresión · bajas militares: no informadas · célula del «Cártel de los Reyes», operación «Erandi» del Plan Michoacán, por titular · detención: ficha aparte",
  panel="<b>Agresión a militares</b>; 7 agresores abatidos", inst=SB, nac="Infobae · Crónica · Excélsior · El Independiente", conf="★★★☆☆",
  campo="hora no fijada; quién inició solo por versión de la Defensa citada por medios; ninguna fuente institucional leída", I=0, N=4, R=3, A=0,
  fechadas=["ABC Noticias (2026/11/25)", "Tribuna (2026/11/25)", "Infobae (2026/11/26)", "Crónica (2026/11/26)", "El Independiente (2026/11/26)"], estatus="Parcialmente corroborado", arm=None, armtxt="ver ARG-158-013",
  desl="Delito y detención en la misma ventana: dos fichas (esta y ARG-158-013). Peribán y Jilotlán figuran por ARG-91-005, ARG-97-ARM-002, ARG-98-005 y ARG-102-002 (agosto): otros hechos. Primeros partes con 4 detenidos y 6 muertos (El Heraldo de México 2026/11/25; Angulo7): saldo superado. Comunicado de la Defensa no indexado en gob.mx/defensa."),
 dict(id="ARG-158-003", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-24", hora="madrugada (solo por resumen)", mu=2, he=1, cu=0, hk=3,
  ent="Guanajuato", mun="Yuriria (San Pablo Casacuarán)", dia="MAR 24-NOV, POR RUTA",
  fecha_txt="martes 24-nov, por ruta; madrugada, solo por resumen",
  title="GUANAJUATO · YURIRIA — SICARIOS ENTRAN A UNA VIVIENDA EN CASACUARÁN: DOS MUERTOS Y UN HERIDO",
  hecho="Yuriria · <code>SAN PABLO CASACUARÁN</code>, por titular · martes 24-NOV, por ruta (La Silla Rota 2026/11/24: «Entran sicarios a hogar en Yuriria y disparan a sus moradores; dejan dos muertos y un herido»; AM 2026/11/24: «Ataque en Casacuarán deja dos muertos y un herido en Yuriria») · madrugada, " + RES + " · <b>2 muertos</b> y <b>1 herido</b>, por titular (🔴 homicidio múltiple) · ataque a una familia en su domicilio, por titular (N+: «Atacan a balazos a familia en Yuriria, Guanajuato; hay dos muertos y un herido») · Guardia Nacional acudió, " + RES + " · " + NOD,
  panel="<b>Ataque a una familia</b>: 2 muertos, 1 herido", inst=SB, nac="La Silla Rota · Milenio · N+", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=3, R=1, A=0,
  fechadas=["La Silla Rota (2026/11/24)", "AM (2026/11/24)"], estatus="Parcialmente corroborado", arm=None,
  desl="Yuriria figura por ARG-125-013 (Valle de Santiago, 3-oct) y Casacuarán por ARG-153-001 (emboscada a policías, 17-nov): otros hechos. Homónimos de AM de 2022 y 2025: otros años. Identidades: no se reproducen."),
 dict(id="ARG-158-004", estado="MX-JAL", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-24", hora="no fijada", mu=0, he=0, cu=1, hk=8,
  ent="Jalisco", mun="San Pedro Tlaquepaque (Cerro del Cuatro)", dia="MAR 24 Y MIÉ 25-NOV, POR RUTA",
  fecha_txt="publicaciones del martes 24 y del miércoles 25-nov, por ruta; hora no fijada",
  title="JALISCO · TLAQUEPAQUE — MADRES BUSCADORAS HALLAN RESTOS HUMANOS EN UNA FOSA CLANDESTINA DEL CERRO DEL CUATRO",
  hecho="San Pedro Tlaquepaque · <code>CERRO DEL CUATRO</code>, por titular · hallazgo de un cuerpo informado el martes 24-NOV, por ruta (El Informador 20261124: «Seguridad en Jalisco: Colectivo reporta hallazgo de cuerpo en el Cerro del Cuatro, Tlaquepaque»), y de <b>más restos humanos en fosa clandestina</b> el miércoles 25-NOV, por ruta (El Informador 20261125: «…Madres Buscadoras de Jalisco hallan más restos humanos en fosa clandestina del Cerro del Cuatro») (🔴 hallazgo de fosa clandestina) · «suman dos hallazgos», por titular (Milenio) · <b>al menos 1 cuerpo</b>, por titular; restos de 5 personas, " + RES + ": <code>NÚMERO DE VÍCTIMAS NO DETERMINADO — SE CUENTA 1</code> · inspecciones desde el 21-nov, " + RES + " · Madres Buscadoras de Jalisco, por titular · causa de muerte no informada por la autoridad",
  panel="<b>Fosa clandestina</b>: restos humanos", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="número de víctimas no determinado; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["El Informador (20261124)", "El Informador (20261125)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cerro del Cuatro no figura en ARGOS 155 a 157. «Hallan cuatro cuerpos en fosa clandestina de Guadalajara» (UnoTV), sin fecha: no se integra."),
 dict(id="ARG-158-005", estado="MX-MEX", region="Centro", color="rojo", impacto="grande", fecha="2026-11-25", hora="no fijada", mu=2, he=0, cu=0, hk=12,
  ent="Estado de México", mun="Ixtapaluca (Santa Cruz Tlapacoya, Cerro del Elefante)", dia="PUBL. MIÉ 25-NOV, POR RUTA",
  fecha_txt="publicación miércoles 25-nov, por ruta; día y hora del hecho no fijados",
  title="ESTADO DE MÉXICO · IXTAPALUCA — ATAQUE ARMADO EN EL CERRO DEL ELEFANTE: DOS MUERTOS",
  hecho="Ixtapaluca · <code>CERRO DEL ELEFANTE</code>, por titular (Info7: «Ataque armado deja dos muertos en el Cerro del Elefante»); col. Santa Cruz Tlapacoya, " + RES + " · publicación miércoles 25-NOV, por ruta (El Independiente 2026/11/25: «Ataque armado deja dos muertos en Ixtapaluca») · día y hora del hecho no fijados; otra nota del 23, " + RES + " · " + RET + " · <b>2 muertos</b>, por titular (N+: «Homicidio en Ixtapaluca: Dos Personas Murieron Tras Ataque Armado en el Cerro del Elefante») (🔴 homicidio múltiple) · FGJEM investiga, " + RES + " · " + NOD,
  panel="<b>2 muertos</b> en ataque armado", inst=SB, nac="N+ · Info7", conf="★★★☆☆",
  campo="día del hecho no fijado; una sola ruta fechada; ninguna fuente institucional", I=0, N=2, R=1, A=0,
  fechadas=["El Independiente (2026/11/25)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ixtapaluca figura en el índice solo en ediciones antiguas: otros hechos. Identidades: no se reproducen."),
 dict(id="ARG-158-006", estado="MX-NLE", region="Noreste", color="rojo", impacto="grande", fecha="2026-11-25", hora="noche, ~20:00 (solo por resumen)", mu=2, he=4, cu=0, hk=20,
  ent="Nuevo León", mun="Monterrey (col. San Bernabé)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; ~20:00, solo por resumen",
  title="NUEVO LEÓN · MONTERREY — ATACAN A BALAZOS A UNA FAMILIA EN SAN BERNABÉ: MUEREN UNA NIÑA Y SU PADRE",
  hecho="Monterrey · <code>COL. SAN BERNABÉ</code>, por titular · miércoles 25-NOV, por ruta (MVS 2026/11/25: «Ataque armado en San Bernabé deja sin vida a una niña y a un hombre») · ~20:00, " + RES + " · <b>2 muertos</b>, una niña y su padre, por titular (Milenio: «Niña y su padre son asesinados a balazos en su casa en Monterrey»; Excélsior: «Asesinan a balazos a niña y a un hombre en Monterrey, Nuevo León») (🔴 homicidio múltiple) · <b>al menos 4 heridos</b>, por titular (El Universal: «Ataque a balazos contra una familia en Monterrey deja dos muertos, entre ellos, una niña; hay al menos cuatro heridos»); 2, " + RES + " · ataque en el domicilio, por titular · móvil no informado · Agencia Estatal de Investigaciones, " + RES + " · " + NOD,
  panel="<b>Ataque a una familia</b>: niña y padre muertos, 4 heridos", inst=SB, nac="MVS · El Universal · Milenio · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen; heridos solo en un titular; ninguna fuente institucional", I=0, N=4, R=1, A=0,
  fechadas=["MVS (2026/11/25)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Bernabé no figura en ediciones previas. Telediario, N+, Horacero y La Tarde: republicaciones, no se cuentan aparte. «Fomerrey 113» (ENfoque): no se acoge. Identidades: no se reproducen."),
 dict(id="ARG-158-007", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-25", hora="~19:30 (solo por resumen)", mu=2, he=1, cu=0, hk=19,
  ent="Sinaloa", mun="Mazatlán (fracc. Los Acantos)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; ~19:30, solo por resumen",
  title="SINALOA · MAZATLÁN — ASESINAN A DOS MUJERES Y HIEREN A UN HOMBRE EN LOS ACANTOS",
  hecho="Mazatlán · <code>FRACC. LOS ACANTOS</code>, por titular · miércoles 25-NOV, por ruta (Ríodoce 2026/11/25: «Dos mujeres muertas y un hombre herido deja ataque armado en Los Acantos, en Mazatlán; hay 2 detenidos»; Luz Noticias 2026-11-25: «Asesinan a dos mujeres en el fraccionamiento Los Acantos en Mazatlán; hay un lesionado y dos detenidos») · ~19:30, " + RES + " · <b>2 mujeres muertas</b> y <b>1 hombre herido</b>, por titular (🔴 homicidio múltiple) · detención: ficha aparte",
  panel="<b>2 mujeres asesinadas</b>, 1 hombre herido", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Ríodoce (2026/11/25)", "Luz Noticias (2026-11-25)"], estatus="Parcialmente corroborado", arm=None,
  desl="Delito y detención en la misma ventana: dos fichas (esta y ARG-158-014). Los Acantos no figura en ediciones previas. Quadratín, Sinaloahoy, El Sol de Mazatlán y Meganoticias, sin fecha en la ruta. Identidades: no se reproducen."),
 # ======================= AMARILLOS
 dict(id="ARG-158-008", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-23", hora="noche (solo por resumen)", mu=0, he=0, cu=0, hk=21,
  ent="Sinaloa", mun="Ahome", dia="LUN 23-NOV, POR RESUMEN",
  fecha_txt="noche del lunes 23-nov, solo por resumen; publicación 24-nov, por ruta",
  title="SINALOA · AHOME — PERSECUCIÓN TERMINA EN ENFRENTAMIENTO ENTRE MARINA Y CIVILES ARMADOS",
  hecho="Ahome · publicación martes 24-NOV, por ruta (Infobae/EFE 2026/11/24: «Una persecución termina en un enfrentamiento armado en Sinaloa, México») · noche del lunes 23-NOV, " + DSR + " · " + RET + " · <b>enfrentamiento</b> entre Marina y civiles armados tras una persecución, por titular (🟡 " + QNI + ") · víctimas y detenidos: no informados · " + FU,
  panel="<b>Enfrentamiento</b> Marina–civiles armados", inst=SB, nac="Infobae (EFE)", conf="★★☆☆☆",
  campo="fuente única de agencia; día solo por resumen; quién inició no determinado", I=0, N=1, R=0, A=0,
  fechadas=["Infobae/EFE (2026/11/24)"], estatus="Pendiente de corroboración", arm=None,
  desl="La Patilla 2026/11/24 republica la nota de EFE: misma fuente. Ahome figura solo como referencia dentro de ARG-156-001/-002: otro hecho."),
 dict(id="ARG-158-009", estado="MX-VER", region="Golfo", color="amarillo", impacto="mediano", fecha="2026-11-24", hora="tarde-noche (solo por resumen)", mu=1, he=0, cu=0, hk=19,
  ent="Veracruz", mun="Hueyapan de Ocampo (Juan Díaz Covarrubias)", dia="MAR 24-NOV, POR RESUMEN",
  fecha_txt="martes 24-nov, solo por resumen; publicación 25-nov, por ruta",
  title="VERACRUZ · HUEYAPAN DE OCAMPO — ASESINAN A UN EXINTEGRANTE DE LA GUARDIA NACIONAL DENTRO DE SU AUTOMÓVIL",
  hecho="Hueyapan de Ocampo · <code>JUAN DÍAZ COVARRUBIAS</code>, " + RES + " · publicación miércoles 25-NOV, por ruta (MVS 2026/11/25: «Asesinan a exintegrante de la Guardia Nacional en Veracruz»; Infobae 2026/11/26: «Exintegrante de la Guardia Nacional muere baleado dentro de un auto deportivo en Veracruz») · martes 24-NOV, " + DSR + " · <b>1 hombre muerto</b>, exintegrante de la Guardia Nacional, por titular (🟡 homicidio doloso único; no estaba en funciones) · FGE, carpeta por homicidio, " + RES + " · " + NOD,
  panel="<b>Ex guardia nacional asesinado</b>", inst=SB, nac="MVS · Infobae", conf="★★★☆☆",
  campo="día solo por resumen; ninguna fuente institucional", I=0, N=2, R=2, A=0,
  fechadas=["MVS (2026/11/25)", "Infobae (2026/11/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Hueyapan de Ocampo no figura en ediciones previas. AVC Noticias («Asesinan a ex Guardia Nacional al sur de Veracruz») y e-veracruz («Matan a exintegrante de la Guardia Nacional en Hueyapan de Ocampo»), sin fecha en la ruta. Si una fuente acreditara servicio activo, subiría a 🔴. Identidad: no se reproduce."),
 dict(id="ARG-158-010", estado="MX-CMX", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-25", hora="mañana (solo por resumen)", mu=1, he=1, cu=0, hk=9,
  ent="Ciudad de México", mun="Cuauhtémoc (Tepito, col. Morelos)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; mañana, solo por resumen",
  title="CIUDAD DE MÉXICO · TEPITO — BALACERA DEJA UNA MUJER MUERTA Y UN ADOLESCENTE HERIDO",
  hecho="Tepito · col. Morelos, " + RES + " · miércoles 25-NOV, por ruta (La Silla Rota 2026/11/25: «Balacera en Tepito deja una mujer muerta y un menor de edad herido»; MVS 2026/11/25: «No cesa la violencia en Tepito; ahora una mujer fue asesinada»; Infobae 2026/11/25: «Ataque armado en Tepito deja una mujer sin vida y un menor de edad lesionado») · mañana, " + RES + " · <b>1 mujer muerta</b> y <b>1 menor herido</b>, por titular (🟡 homicidio doloso único); dos muertos, por titular sin fecha (Crónica Regional): <code>SALDO CONTRADICHO — SE CUENTA 1</code> · víctima alcanzada por accidente, " + RES + ": <code>NO ACREDITADO</code> · " + NOD,
  panel="<b>Mujer asesinada</b>, menor herido", inst=SB, nac="La Silla Rota · MVS · Infobae", conf="★★★☆☆",
  campo="hora solo por resumen; saldo contradicho en un titular; ninguna fuente institucional", I=0, N=3, R=0, A=0,
  fechadas=["La Silla Rota (2026/11/25)", "MVS (2026/11/25)", "Infobae (2026/11/25)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepito figura en el índice solo en ediciones antiguas: otros hechos. Edades y calle contradichas, " + RES + ". Identidades: no se reproducen."),
 dict(id="ARG-158-011", estado="MX-SON", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-25", hora="~06:30 (solo por resumen)", mu=1, he=1, cu=0, hk=6,
  ent="Sonora", mun="Hermosillo (Centro; Garmendia y Luis Encinas)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; ~06:30, solo por resumen",
  title="SONORA · HERMOSILLO — ATAQUE ARMADO EN UN DOMICILIO DEL CENTRO: UN HOMBRE MUERTO Y UNA MUJER HERIDA",
  hecho="Hermosillo · <code>CENTRO, CRUCE DE GARMENDIA Y LUIS ENCINAS</code>, por ruta · miércoles 25-NOV, por ruta (Proyecto Puente 2026/11/25: «Ataque armado deja un hombre muerto y una mujer herida en Centro de Hermosillo»; El Imparcial 2026/11/25; Infoson 2026/11/25: «Agresión armada deja un muerto y una mujer herida en el Centro de Hermosillo») · ~06:30, " + RES + " · <b>1 hombre muerto</b> y <b>1 mujer herida</b>, por titular (🟡 homicidio doloso único) · Fiscalía de Sonora investiga, " + RES + " · " + NOD,
  panel="<b>Hombre asesinado</b>, mujer herida", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Proyecto Puente (2026/11/25)", "El Imparcial (2026/11/25)", "Infoson (2026/11/25)"], estatus="Parcialmente corroborado", arm=None,
  desl="Hermosillo figura por ARG-100-003, -106-005, -125-001, -125-009, -134-012, -135-005/006 y -137-018: otros hechos. Uso del inmueble, solo por medio extraoficial: no se reproduce."),
 # ======================= VERDES
 dict(id="ARG-158-012", estado="MX-YUC", region="Sureste", color="verde", impacto="mediano", fecha="2026-11-23", hora="no fijada", mu=0, he=0, cu=0, hk=9,
  ent="Yucatán", mun="Progreso (col. Ciénega 2000)", dia="PUBL. LUN 23-NOV, POR RUTA",
  fecha_txt="publicación lunes 23-nov, por ruta; hora de la detención no fijada",
  title="YUCATÁN · PROGRESO — LA SSP DETIENE A CINCO PERSONAS POR EL ATAQUE ARMADO EN CIÉNEGA 2000",
  hecho="Progreso · <code>COL. CIÉNEGA 2000</code>, por titular · publicación lunes 23-NOV, por ruta (Diario de Yucatán 2026/11/23: «Detienen a cinco personas tras reporte de ataque armado en Ciénega 2000, Progreso») · " + AP + " · " + RET + " · comunicado de la SSP de Yucatán, por titular" + INS + " («SSP INFORMA DETENCIONES POR LOS HECHOS OCURRIDOS EN CIÉNEGA 2000, PROGRESO», ssp.yucatan.gob.mx/noticia/1031, sin fecha en la ruta) · <b>5 detenidos</b>, por titular (Quadratín Yucatán: «Detienen a 5 personas tras agresión armada en Ciénega 2000, Progreso») (🟢 detención) · 3 hombres y 2 mujeres de Ciudad del Carmen, " + RES + " · homicidio de la madrugada del 22, " + RES + ": ventana de ARGOS 156, 🟡, no se ficha · SSP, FGE y Policía Municipal, " + RES,
  panel="<b>5 detenidos</b> por un homicidio", inst="SSP Yucatán (portal, sin fecha en la ruta)", nac="—", conf="★★★☆☆",
  campo="hora de la detención no fijada en el día de apertura; comunicado sin fecha en la ruta", I=1, N=0, R=3, A=0,
  fechadas=["Diario de Yucatán (2026/11/23)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — sin aseguramiento de armamento publicado",
  desl="Ciénega 2000 no figura en ediciones previas; ARG-95-SEN-006 (Progreso, FGR, agosto): otro hecho. ProgresoHoy y The Yucatan Times (2026/11): republicaciones. Nombres: no se reproducen."),
 dict(id="ARG-158-013", estado="MX-MIC", region="Occidente", color="verde", impacto="grande", fecha="2026-11-25", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Michoacán–Jalisco", mun="Peribán – Jilotlán de los Dolores (brecha limítrofe)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; hora no fijada",
  title="MICHOACÁN–JALISCO · PERIBÁN – JILOTLÁN — LA DEFENSA DETIENE A DIEZ Y ASEGURA ARMAMENTO DE LA CÉLULA DEL «CÁRTEL DE LOS REYES»",
  hecho="Brecha Peribán–Jilotlán, " + RES + " · miércoles 25-NOV, por ruta (ABC Noticias 2026/11/25; Tribuna 2026/11/25) · <b>10 detenidos</b>, por titular (Infobae 2026/11/26: «Defensa confirma siete criminales abatidos y 10 detenidos tras enfrentamiento contra célula del Cártel de los Reyes»; EFE vía Infobae 2026/11/26: «Siete muertos y diez detenidos tras enfrentamiento armado en el oeste de México») (🟢 detención) · cifra atribuida a la Defensa por medios, sin documento · 4 detenidos en los primeros partes, por titular: saldo superado · fusil Barrett calibre .50, ametralladora Minimi, «33 armas de fuego», una granada, cargadores, cartuchos y 4 vehículos, " + RES + "; 35 armas, por titular sin fecha (La Voz de Michoacán): " + CND + " · puestos a disposición de la FGR en Zamora, " + RES,
  panel="<b>10 detenidos</b>; armamento sin cifra citable", inst=SB, nac="Infobae · Crónica · El Independiente · Excélsior", conf="★★★☆☆",
  campo="hora no fijada; cifra de la Defensa solo citada por medios; armamento solo por resumen", I=0, N=4, R=2, A=0,
  fechadas=["ABC Noticias (2026/11/25)", "Tribuna (2026/11/25)", "Infobae (2026/11/26)", "Crónica (2026/11/26)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armamento sin cantidad por titular: evento cualitativo",
  desl="Delito y detención en la misma ventana: dos fichas (ARG-158-002 y esta). Boletín federal del 25: Jilotlán, El Limoncito, 11 detenidos y 43 armas, " + RES + ", y Peribán, SSP y Defensa, 8 detenidos y 20 armas (Changoonga 2026/11/26: «SSP Y Defensa Repelen Ataque Armado En Límites De Michoacán Y Jalisco; Hay Ocho Detenidos»): <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>. Nombres: no se reproducen."),
 dict(id="ARG-158-014", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-25", hora="no fijada", mu=0, he=0, cu=0, hk=19,
  ent="Sinaloa", mun="Mazatlán (fracc. Los Acantos)", dia="MIÉ 25-NOV, POR RUTA",
  fecha_txt="miércoles 25-nov, por ruta; hora no fijada",
  title="SINALOA · MAZATLÁN — DETIENEN A DOS PRESUNTOS RESPONSABLES DEL ATAQUE EN LOS ACANTOS",
  hecho="Mazatlán · <code>FRACC. LOS ACANTOS</code>, por titular · miércoles 25-NOV, por ruta (Ríodoce 2026/11/25: «…hay 2 detenidos»; Luz Noticias 2026-11-25: «…hay un lesionado y dos detenidos») · <b>2 detenidos</b>" + TM + " (🟢 detención) · persecución de policías municipales y fuerzas federales, " + RES + " · detención extraoficial, " + RES + " · un tercer implicado buscado, " + RES + " · " + NDA,
  panel="<b>2 detenidos</b> tras el ataque", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada; detenidos sin cifra de autoridad; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Ríodoce (2026/11/25)", "Luz Noticias (2026-11-25)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — sin aseguramiento de armamento publicado",
  desl="Delito y detención en la misma ventana: dos fichas (ARG-158-007 y esta). Nombres: no se reproducen."),
 dict(id="ARG-158-015", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-25", hora="no fijada", mu=0, he=0, cu=0, hk=11,
  ent="Sinaloa", mun="Mazatlán", dia="PUBL. MIÉ 25-NOV, POR RUTA",
  fecha_txt="publicación miércoles 25-nov, por ruta; día y hora de la captura no fijados",
  title="SINALOA · MAZATLÁN — DETIENEN A SEIS PRESUNTOS INTEGRANTES DE «LOS CHAPITOS» CON ARMAS, CARGADORES Y CARTUCHOS",
  hecho="Mazatlán · publicación miércoles 25-NOV, por ruta (Infobae 2026/11/25: «Detienen con armas, cargadores y cartuchos a seis miembros de “Los Chapitos” en Mazatlán»; Ríodoce 2026/11/25: «Detienen a seis presuntos integrantes de Los Chapitos en Mazatlán») · día y hora de la captura no fijados · " + RET + " · <b>6 detenidos</b>" + TM + " (🟢 detención) · armas, cargadores y cartuchos, por titular, sin número: " + CND + " · a disposición de la FGR, " + RES + " · " + NDA,
  panel="<b>6 detenidos</b> con armas sin cifra", inst=SB, nac="Infobae", conf="★★★☆☆",
  campo="día de la captura no fijado; detenidos sin cifra de autoridad; armamento sin cantidad", I=0, N=1, R=1, A=0,
  fechadas=["Infobae (2026/11/25)", "Ríodoce (2026/11/25)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armamento sin cantidad publicada: evento cualitativo",
  desl="«Caen cuatro armados, entre ellos dos menores de edad, en Mazatlán; GOES les asegura fusiles y una granada» (Extraoficial), sin fecha: otro conteo, no se integra. Nombres: no se reproducen."),
 dict(id="ARG-158-016", estado="MX-JAL", region="Occidente", color="verde", impacto="grande", fecha="2026-11-25", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Jalisco", mun="Chapala (Ajijic)", dia="MIÉ 25-NOV, POR TITULAR DEL BOLETÍN",
  fecha_txt="acciones del miércoles 25-nov, por titular del boletín federal (republicado); hora no fijada",
  title="JALISCO · CHAPALA — FUERZAS FEDERALES ASEGURAN EN AJIJIC DOS FUSILES BARRETT, ARMAS LARGAS, GRANADAS Y CARTUCHOS",
  hecho="Chapala · <code>AJIJIC</code>, " + RES + " · acciones del miércoles 25-NOV, por titular del boletín del Gabinete de Seguridad republicado (Milenio: «Gabinete de seguridad: resultados 25 de noviembre»; Tallapolítica: «Gabinete de Seguridad del Gobierno de México informa acciones relevantes del 25 de noviembre 2026») (🟢 aseguramiento) · 2 fusiles Barrett, 4 armas largas, 73 cargadores, 1,507 cartuchos, 10 granadas, equipo táctico y 2 vehículos, uno con reporte de robo en Estados Unidos, " + RES + " · «seis armas y diez granadas» en un agregado de medio (Hoy Tamaulipas): armas largas 4 o 6 · " + CND + " · " + NOD,
  panel="<b>Aseguramiento</b>: Barrett, granadas, cartuchos", inst=SB, nac="Milenio", conf="★★☆☆☆",
  campo="cifras solo en el cuerpo del boletín republicado; republicadores = una sola fuente", I=0, N=1, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, armtxt="sin fila — cifras solo por resumen del boletín: <code>NO INTEGRAR HASTA DOCUMENTO</code>",
  desl="Boletín del 25 no indexado en gob.mx/sspc: tomado de republicadores; corroboración débil por construcción. Ajijic no figura en ARGOS 155 a 157."),
 dict(id="ARG-158-017", estado="MX-NAY", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-25", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Nayarit", mun="Ixtlán del Río (Jala)", dia="MIÉ 25-NOV, POR TITULAR DEL BOLETÍN",
  fecha_txt="acciones del miércoles 25-nov, por titular del boletín federal (republicado); publicación 26-nov, por ruta",
  title="NAYARIT · IXTLÁN DEL RÍO — FUERZAS FEDERALES INHABILITAN UN LABORATORIO DE DROGAS SINTÉTICAS",
  hecho="Ixtlán del Río · poblado Jala, " + RES + " · acciones del miércoles 25-NOV, por titular del boletín republicado (Milenio) · publicación jueves 26-NOV, por ruta (Línea Directa 2026-11-26: «Desmantelan laboratorio de drogas y decomisan arsenal en operativos federales») · <b>laboratorio inhabilitado</b>, por titular (Excélsior: «Desmantelan narcolaboratorio en Ixtlán del Río, Nayarit») (🟢 desmantelamiento) · 4,800 litros y 1,400 kilos de precursores; afectación de 4,250,400 pesos, " + RES + " · " + NOD,
  panel="<b>Narcolaboratorio</b> inhabilitado", inst=SB, nac="Excélsior · Milenio", conf="★★★☆☆",
  campo="cifras solo por resumen; boletín tomado de republicadores", I=0, N=2, R=1, A=0,
  fechadas=["Línea Directa (2026-11-26)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — laboratorio, no armamento",
  desl="Laboratorios de Nayarit de julio de 2025 y 2026: otros hechos. Ixtlán del Río no figura en ARGOS 155 a 157."),
 dict(id="ARG-158-018", estado="MX-PUE", region="Centro", color="verde", impacto="mediano", fecha="2026-11-26", hora="no fijada", mu=0, he=0, cu=0, hk=9,
  ent="Puebla", mun="Atzitzintla", dia="JUE 26-NOV, POR RUTA",
  fecha_txt="publicación jueves 26-nov, por ruta; hora no fijada",
  title="PUEBLA · ATZITZINTLA — APREHENDEN AL PRESIDENTE MUNICIPAL POR SECUESTRO EXPRÉS Y ROBO DE VEHÍCULO («OPERACIÓN ENJAMBRE»)",
  hecho="Atzitzintla · publicación jueves 26-NOV, por ruta (El Heraldo de México 2026/11/26: «Detienen en la 'Operación Enjambre' a alcalde de Atzitzintla, por secuestro exprés, robo agravado y nexos criminales»; Intolerancia 2026/11/26: «Aprehenden al edil de Atzitzintla, acusado de secuestro exprés y robo de vehículo») · " + FR + " · <b>1 servidor público aprehendido</b>, el presidente municipal, por orden de aprehensión, por titular (🟢 orden de aprehensión cumplimentada) · vínculo con «Los Zúñiga» atribuido al secretario de Seguridad, por titular de medio: <code>NO ACREDITADO POR DOCUMENTO</code> · autoridades federales y estatales, " + RES,
  panel="<b>Alcalde aprehendido</b>", inst=SB, nac="El Heraldo de México · 24 Horas · Diario de México", conf="★★★☆☆",
  campo="hora no fijada en el día de cierre; declaración del secretario solo citada por medios", I=0, N=3, R=2, A=0,
  fechadas=["El Heraldo de México (2026/11/26)", "Intolerancia (2026/11/26)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — sin aseguramiento de armamento publicado",
  desl="Atzitzintla no figura en ediciones previas. «Operación Enjambre»: seis servidores públicos detenidos, " + RES + ": agregado, no se integra. Audiencia inicial: no publicada."),
]
R = [
 dict(id="ARG-158-REC-001", estado="MX-TAB", region="Golfo", fecha="2026-11-22", hora="madrugada (solo por resumen)", orig="ARGOS 156", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Tabasco", mun="Centro (Villa Ocuiltzapotlán)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; madrugada, solo por resumen",
  title="TABASCO · CENTRO — ASESINAN A UN ADOLESCENTE DE 13 AÑOS Y A UN HOMBRE EN OCUILTZAPOTLÁN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 156</code> (madrugada del 22, " + RES + "; si resultara posterior a las 09:34 del 22, sería de ARGOS 157) · Centro · <code>VILLA OCUILTZAPOTLÁN</code>, por titular · domingo 22-NOV, por ruta (Proceso 2026/11/22: «Tabasco: asesinan a adolescente de 13 años y a un hombre en Ocuiltzapotlán») · <b>2 muertos</b>, un adolescente de 13 años y un hombre, por titular (🔴 homicidio múltiple) · " + NOD,
  panel="<b>Adolescente y hombre asesinados</b>", inst=SB, nac="Proceso",
  conf="★★☆☆☆", campo="fuente única con fecha; hora solo por resumen", I=0, N=1, R=0, A=0,
  fechadas=["Proceso (2026/11/22)"], estatus="Pendiente de corroboración",
  desl="Ocuiltzapotlán figura por ARG-143-REC-004 (tres cuerpos en el corredor Villahermosa–Frontera, octubre): otro hecho. No figura en ARGOS 156 ni 157. Identidades: no se reproducen."),
 dict(id="ARG-158-REC-002", estado="MX-PUE", region="Centro", fecha="2026-11-21", hora="noche (solo por resumen)", orig="ARGOS 156", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Puebla", mun="Chietla (Villa de Atencingo)", dia="SÁB 21-NOV, POR RESUMEN",
  fecha_txt="sábado 21-nov por la noche, solo por resumen; publicación nov-2026, por ruta",
  title="PUEBLA · CHIETLA — ASESINAN A UNA PAREJA AL LLEGAR A SU CASA EN LA VILLA DE ATENCINGO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 156</code> · Chietla · <code>VILLA DE ATENCINGO</code>, por titular (El Quinto Medio 2026/11: «Identifican a pareja asesinada en la Villa de Atencingo, Chietla») · noche del sábado 21-NOV, " + DSR + " · <b>2 muertos</b>, una pareja, por titular (Periódico Central: «Muere pareja en ataque directo afuera de su domicilio en Chietla, Puebla»; Urbano Puebla: «Identifican a pareja asesinada en ataque armado al ingresar a su casa en Chietla, Puebla»; Curul: «Los ejecutan frente a su casa en Chietla») (🔴 homicidio múltiple) · vínculo con el doble homicidio de Atencingo del 5-nov (ARG-148-002), por titular de medio: <code>NO ACREDITADO</code> · " + NOD,
  panel="<b>Pareja asesinada</b> frente a su casa", inst=SB, nac="—",
  conf="★★★☆☆", campo="día solo por resumen; ruta solo con mes; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["El Quinto Medio (2026/11)"], estatus="Parcialmente corroborado",
  desl="Visto de ARGOS 157 sin día. Chietla figura por ARG-148-002 (5-nov): otro hecho. Identidades: no se reproducen."),
 dict(id="ARG-158-REC-003", estado="MX-MIC", region="Occidente", fecha="2026-11-22", hora="tarde (solo por resumen)", orig="ARGOS 157", col_orig="rojo", mu=0, he=0, cu=2,
  ent="Michoacán", mun="Cuitzeo (San Juan Benito Juárez–Chehuayo Chico)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; tarde, solo por resumen",
  title="MICHOACÁN · CUITZEO — HALLAN DOS HOMBRES MUERTOS Y ROCIADOS CON DIÉSEL EN UNA BRECHA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 157</code> · Cuitzeo · camino San Juan Benito Juárez–Chehuayo Chico, " + RES + " · domingo 22-NOV, por ruta (RED Michoacán 2026/11/22: «Hallan a dos hombres muertos y rociados con diésel en la región de Cuitzeo»; Changoonga 2026/11/22) · tarde, " + RES + " · <b>2 cuerpos</b> con huellas de violencia, por titular (Quadratín: «Hallan 2 cuerpos con huellas de violencia en brecha de Cuitzeo») (🔴 hallazgo de restos con violencia; víctimas múltiples) · causa de muerte no informada por la autoridad · " + NOD,
  panel="<b>2 cuerpos</b> rociados con diésel", inst=SB, nac="—",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["RED Michoacán (2026/11/22)", "Changoonga (2026/11/22)"], estatus="Parcialmente corroborado",
  desl="Visto de ARGOS 157 sin ruta: se recupera con rutas del 22. «Localizan 2 cadáveres dentro de camioneta quemada en paraje de Cuitzeo» (La Voz de Michoacán): hecho de 2025, otro."),
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
HORAS = 77 + 9 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
RREG = {g: sum(1 for e in E if e["color"] == "rojo" and e["region"] == g) for g in ("Noroeste", "Noreste", "Occidente", "Centro", "Golfo", "Sureste")}
assert TOT == [0] * 10 and ARMAS == 0, (TOT, ND)
assert cnt == {"rojo": 7, "amarillo": 4, "verde": 7}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU) == (11, 8, 6), (MU, HE, CU)
assert DENS == "0,23" and RPH == "0,09", (DENS, RPH)
assert (NAP, NFR, NRET) == (1, 1, 5), (NAP, NFR, NRET)
assert len(ENT) == 12 and len(ENT_ROJO) == 7, (ENT, ENT_ROJO)
assert RREG == {"Noroeste": 2, "Noreste": 1, "Occidente": 3, "Centro": 1, "Golfo": 0, "Sureste": 0}, RREG
assert sorted(e["id"] for e in E) == [f"ARG-158-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-23" <= x["fecha"] <= "2026-11-26", x["id"]
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
head = head.replace("<title>ARGOS 157 — Reporte Nacional de Seguridad — 2026-11-23</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA DEFENSA EL PARTE DE LA BRECHA PERIBÁN–JILOTLÁN —QUIÉN INICIÓ, LUGAR E INVENTARIO— Y COTÉJELO CON LOS ASEGURAMIENTOS FEDERALES DE EL LIMONCITO Y PERIBÁN</b> (ARG-158-002 y -013).
      <br><b>2. SOLICITE A LA FISCALÍA DE SONORA LA HORA DEL HALLAZGO Y LA CAUSA DE MUERTE EN SANTA ANA</b> (ARG-158-001).
      <br><b>3. SOLICITE A LA FISCALÍA DE NUEVO LEÓN EL SALDO DE HERIDOS Y LA LÍNEA DE INVESTIGACIÓN DEL ATAQUE EN SAN BERNABÉ</b> (ARG-158-006).
      <br><b>4. SOLICITE A LA FISCALÍA DEL ESTADO DE MÉXICO EL DÍA Y LA HORA DEL ATAQUE EN EL CERRO DEL ELEFANTE</b> (ARG-158-005).
      <br><b>5. COTEJE CON LA SSP DE SINALOA Y LA FGR LA CIFRA OFICIAL DE DETENIDOS Y EL ARMAMENTO ASEGURADO EN MAZATLÁN</b> (ARG-158-014 y -015).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
DIA = {d: sum(1 for e in E if e["fecha"] == d) for d in ("2026-11-23", "2026-11-24", "2026-11-25", "2026-11-26")}
assert DIA == {"2026-11-23": 3, "2026-11-24": 3, "2026-11-25": 11, "2026-11-26": 1}, DIA
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>23-nov 08:35 → 26-nov 13:44 CDMX</b> (<b>{DUR}</b>) · lun 23 (desde 08:35; 15 h 25) · mar 24 · mié 25 · jue 26 (hasta 13:44; 13 h 44) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b> · por fecha asignada: lun 23 <b>{DIA["2026-11-23"]}</b> · mar 24 <b>{DIA["2026-11-24"]}</b> · mié 25 <b>{DIA["2026-11-25"]}</b> · jue 26 <b>{DIA["2026-11-26"]}</b>; duración, densidad y reparto, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto</b> (ventanas de ARGOS 156 y 157), atenuadas, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: ningún aseguramiento de la ventana con cantidad por titular o por autoridad: n/d · <b>muertos por agresión</b>: {MU}, cálculo propio; <b>7 agresores abatidos</b> en Peribán–Jilotlán, fuera de este total · <b>heridos</b>: {HE} (San Bernabé, 4 por titular) · <b>cuerpos o restos</b>: {CU} (Santa Ana 5; Cerro del Cuatro, al menos 1) · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>{NRET} cláusulas de retiro</b> (detalle en cada ficha).
    <br><code>BALANCES, NO SE INTEGRAN</code>: «Violencia deja siete muertos en Puebla, entre ellos el sobrino de Rafael Caro Quintero» (Proceso 2026/11/23) · «Cinco ataques armados en Puebla dejan ocho muertos y cuatro heridos en menos de 48 horas» (La Jornada de Oriente) · «Campeche suma 12 ejecuciones en noviembre» (PorEsto 2026/11/24) · «Miércoles con 47 ejecutados» (Sol Quintana Roo).
    <br><b>Vistos, fuera de totales</b> (sin día por ruta o titular): Chihuahua, yonke, tres muertos y un comandante estatal herido en Ciudad Aldama (Excélsior; El Congresista) · Reynosa, estación Anzaldúas, restos óseos hallados por un colectivo · Nacajuca, Tab., dos hombres atados y baleados (homónimos de agosto) · Temixco, El Estribo, un muerto y una mujer herida · Nezahualcóyotl, mujer asesinada (colonia y día contradichos) · Atotonilco de Tula, un muerto y una mujer herida · Hermosillo, cantante herido (solo cobertura en vivo) · Ulumal, Champotón, hombre ejecutado · Macuspana, cuerpo desmembrado · <b>ventana de 157, no rojos</b>: Chilpancingo–Chichihualco, hombre decapitado (~07:30 del 23 {RES}) · Rosarito, 4 detenidos y 6 armas por titular (El Imparcial 2026/11/23), aseguramiento de la noche del 22 {RES}.
    <br><code>FE DE ERRATAS — ARGOS 157</code>: el visto «Periférico Norte, operador de transporte» era del <b>viernes 20 en Tlalnepantla</b> (Infobae 2026/11/21): ventana de 156 · <b>tres rojos de ventanas anteriores se recuperan</b> (Ocuiltzapotlán y Chietla, de 156; Cuitzeo, de 157) · <b>efecto</b> (cálculo propio): <b>ARGOS 157</b>: 11 hechos · 4 🔴 · 5 🟡 · 2 🟢 · 9 muertos por agresión · 5 heridos · 2 cuerpos · 4 entidades · <b>ARGOS 156</b>: 20 hechos · 13 🔴 · 3 🟡 · 4 🟢 · 23 muertos por agresión (22 si en Nopaltepec murió un solo agente) · 5 heridos · 11 entidades.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Tepehuacán de Guerrero (ARG-155-011)</b>: <b>4 vinculados a proceso por homicidio calificado</b> en la audiencia del 24, por titular (La Silla Rota 2026/11/24: «Vinculan a proceso a cuatro por homicidio de policías en Tepehuacán»; Síntesis 2026/11/24) · <b>El Platanito (ARG-157-003/-009)</b>: publicación del 22 por ruta; hora sin titular; los ocho detenidos siguen sin separarse de los de Guasave (ARG-156-013) · <b>Calpulalpan (ARG-157-REC-001)</b>: 3 detenidos, por titular (abctlax: «DETIENEN A 3 HOMBRES TRAS HOMICIDIO DE MENOR EN CALPULALPAN») · <b>Tepexco (ARG-157-002)</b>: 3 o 4 muertos y 2 o 3 calcinados, contradichos por titular; hora sin titular · <b>Texhuacán (ARG-151-001)</b>: «indicios de vínculo» de los tres detenidos, según la fiscal, por titular (Plumas Libres 2026/11/25); sin imputación por homicidio · <b>Lomas de Mazatlán (ARG-157-010)</b>: 2 cargadores y calibres {RES} · <b>Guasave (ARG-156-013)</b>: vinculación de los ocho no publicada.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-158-{i:03d}"]) for i in (1, 2, 13, 3))
co2 = "\n".join(ficha(byid[f"ARG-158-{i:03d}"]) for i in (4, 5, 6))
co3 = "\n".join(ficha(byid[f"ARG-158-{i:03d}"]) for i in (7, 14, 15, 8))
co4 = "\n".join(ficha(byid[f"ARG-158-{i:03d}"]) for i in (9, 10, 11))
co5 = "\n".join(ficha(byid[f"ARG-158-{i:03d}"]) for i in (12, 16, 17, 18))
co6 = "\n".join(ficha(rbyid[f"ARG-158-REC-{i:03d}"], True) for i in (1, 2, 3))
assert sorted(re.findall(r'id="(ARG-158-0\d\d)"', co1 + co2 + co3 + co4 + co5)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-158-REC-\d\d\d)"', co6)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN RESULTADO INDEXADO EN VENTANA</code>"
NDR = "solo por resumen: <b>cantidad no determinada</b>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "Ajijic y Peribán–Jilotlán, " + NDR),
 tile(2, "Sin categoría", tv(2), "«33 armas» en Peribán–Jilotlán, " + NDR),
 tile(3, "Cartuchos", tv(4, fmt), "Ajijic, " + NDR),
 tile(4, "Cargadores", tv(5), "Ajijic, " + NDR),
 tile(5, "Granadas", tv(6), "Ajijic y Peribán–Jilotlán, " + NDR),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), "fusiles Barrett .50, " + NDR),
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

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr style="opacity:.72;"><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> (28 entidades por dominio; 4 <code>NO REVISADA</code>) · ningún aseguramiento de la ventana con día fijado y cantidad publicada por titular o por autoridad</td></tr>'

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
    <br><code>VISTOS, NO INTEGRADOS</code>: Ajijic (ARG-158-016): dos Barrett, 4 armas largas, 73 cargadores, 1,507 cartuchos y 10 granadas {RES} · Peribán–Jilotlán (ARG-158-013): Barrett, Minimi, «33 armas» y una granada {RES}; El Limoncito, 11 detenidos y 43 armas, y Peribán, 8 detenidos y 20 armas, {RES}: <code>POSIBLE DUPLICIDAD — NO INTEGRAR</code> · Mazatlán (ARG-158-015): armas sin número · Felipe Carrillo Puerto, Los Lagartos, QRoo: 7 armas largas y 24 cargadores {RES}, día no fijado (Línea Directa 2026-11-24, republicador) · Sonora: 10 armas y 245 cartuchos, boletín del 23 {RES}, sin titular · SSP de Veracruz, «En operativos del 23 al 24 de noviembre, se detuvo a 20 personas» (veracruz.gob.mx 2026/11/25): agregado, armas {RES} · Santa Ana (ARG-158-001): 4 armas largas en la escena {RES}.
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
      <tr><td><b>Campeche</b><br>Hopelchén</td><td>Cinco personas, posesión de armamento; comunicado DPE/5332/2026, {RES}</td><td>4 años, {RES}</td><td>FGR</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · listado de fgr.org.mx sin fecha en la ruta; 24-nov {RES} · boletín no leído · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Chihuahua</b></td><td>Homicidio; un sentenciado (La Opción 20261125: «Sentenciado a 16 años y 8 meses de prisión por el delito de homicidio»)</td><td>16 años y 8 meses, por titular</td><td>—</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín de la FGE · sin dos campos individualizadores</td><td>Bajo</td></tr>
      <tr><td><b>Sonora</b><br>Hermosillo</td><td>Tres personas detenidas con armamento</td><td>10 años, {RES}</td><td>FGR</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin ruta con fecha; fechas contradichas entre medios</td><td>No confirmado</td></tr>
      <tr><td><b>Guerrero</b><br>Iguala (caso Los Avispones, 2014)</td><td>Exalcalde de Iguala; homicidio en grado de tentativa {RES}</td><td>60 años, por titular (La Silla Rota 2026/11/19; PorEsto 2026/11/19: «…defensa apela fallo»)</td><td>Juzgado federal {RES}</td><td>Publicación del 19: ventana de ARGOS 155 · sin comunicado de la FGR ni del Poder Judicial · apelada: no firme</td><td>Bajo</td></tr>
      <tr><td colspan="6"><b>Fuera de ventana</b>: Chihuahua, triple homicidio en Cerro de la Cruz, 30 años (La Opción 20261120) · FGEO 2,993 (19-nov {RES}) · FGET 5126 y 5127 (18-nov, listado histórico): publicaciones anteriores a la ventana.</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida a <code>fgr.org.mx</code> (listados nacional y estatal; contenido {RES}); candidata de Jalisco del 24-nov no localizada</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>28 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, BCS, Chih, Dgo · Coah, NL, Tamps, SLP, Zac · Jal, Col, Nay, Ags, Gto · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Ver, Tab · Gro, Oax, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> por dominio estatal</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>28</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>4</b>: Son (dominio sin páginas), Sin (dominio solo con normatividad), Mich (fiscalía no consultada), Camp (dominio de la fiscalía no confirmado)</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 26-nov 06:10: código <code>000</code> · sin páginas: <code>ucs.campeche.gob.mx</code>, <code>ssp.guanajuato.gob.mx</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 21 entidades; solo consulta amplia en 11 —BC, BCS, Chih, Dgo · Coah, SLP, Zac · Col, Ags · Qro · QRoo— · <b>armamento: 28 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (4): Son, Sin, Chih · Oax</td></tr>
      <tr><td><b>Boletín federal</b></td><td>__FED17C__ · Defensa: SRIV en <code>gob.mx/defensa</code> (último indexado, 14-nov) · Guardia Nacional: sin páginas de 2026 indexadas · Semar: último indexado, 5-nov</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · <code>BLOQUEO DE EGRESO REVERIFICADO EL 26-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Alto impacto</b>: homicidios múltiples en ataques a domicilios y en la vía pública de cuatro entidades, un hallazgo de cinco cuerpos en Sonora, una fosa clandestina en la zona metropolitana de Guadalajara y una agresión a militares en la franja Michoacán–Jalisco; {RPH} rojos por hora (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Occidente {RREG["Occidente"]} · Noroeste {RREG["Noroeste"]} · Noreste {RREG["Noreste"]} · Centro {RREG["Centro"]} · Golfo y Sureste 0 (cálculo propio); menores y mujeres entre las víctimas de tres de ellos.
      <br><b>3.</b> <b>Violencia operativa</b>: homicidios dolosos únicos en Sonora, Ciudad de México y Veracruz, y un enfrentamiento de la Marina en Ahome sin iniciador determinado.
      <br><b>4.</b> <b>Respuesta institucional</b>: detenciones en cuatro entidades, un presidente municipal aprehendido y un laboratorio inhabilitado; armamento de alto poder asegurado sin cifra citable; ninguna sentencia integrable.
      <br><b>5.</b> <code>TOTALES NO COMPARABLES SIN MÁS CON LOS DE OTRAS EDICIONES: VENTANA DE 77 H 09 MIN, LA MÁS LARGA DE LA SERIE (62 H 54 MIN EN ARGOS 156; 23 H 01 MIN EN ARGOS 157), CON LA MAYORÍA DE LOS HECHOS FECHADOS EL MIÉRCOLES 25. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. ATAQUES A DOMICILIOS CON NIÑAS, ADOLESCENTES Y MUJERES ENTRE LAS VÍCTIMAS</b> (ARG-158-003, -006 y -007): Yuriria, Monterrey y Mazatlán; vínculo no acreditado. Línea: <b>revisar denuncias previas de amenazas en San Pablo Casacuarán y en la col. San Bernabé</b>.
      <br><b>2. FUSILES BARRETT EN DOS PUNTOS DE LA FRANJA JALISCO–MICHOACÁN EL MISMO DÍA</b> (ARG-158-013 y -016): Peribán–Jilotlán y Ajijic, solo por resumen; vínculo no acreditado. Línea: <b>solicitar a la FGR el rastreo de origen de los fusiles calibre .50 asegurados</b>.
      <br><b>3. CINCO HOMBRES CON CHALECO ANTIBALAS EN UNA CAMIONETA BLINDADA EN EL NORTE DE SONORA</b> (ARG-158-001): perfil de grupo armado, solo por resumen; vínculo no acreditado. Línea: <b>vigilar la carretera federal 15 en el tramo de Santa Ana</b>.
      <br><b>4. MAZATLÁN: HOMICIDIO MÚLTIPLE Y DOS DETENCIONES EL MISMO DÍA</b> (ARG-158-007, -014 y -015); vínculo no acreditado. Línea: <b>cotejar a los seis detenidos de «Los Chapitos» con los indicios del ataque en Los Acantos</b>.
      <br><b>5. FOSA CLANDESTINA EN EL CERRO DEL CUATRO, LOCALIZADA POR UN COLECTIVO</b> (ARG-158-004): hallazgos en días consecutivos. Línea: <b>dar custodia a las jornadas de búsqueda del colectivo en el Cerro del Cuatro</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

FED17 = os.environ.get("ARGOS_FED17", "acciones del 20, 21 y 22-nov (agregado): solo republicadores (RED113 2026/11; Tallapolítica; Certeza Diario) · acciones del 23-nov: <b>indexado en <code>gob.mx/sspc</code></b> por título (Milenio; Tallapolítica) · acciones del 24-nov: solo republicadores (RED113 2026/11; Tallapolítica) · acciones del 25-nov: republicadores (Milenio; Tallapolítica) · contenido <code>SOLO POR RESUMEN</code>")
arm2 = arm2.replace("__FED17__", FED17)
sent = sent.replace("__FED17C__", FED17)

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — SANTA ANA; AGRESIÓN A MILITARES Y DETENCIONES EN PERIBÁN–JILOTLÁN; YURIRIA", co1)
 + page("CRIMEN ORGANIZADO (II) — FOSA EN EL CERRO DEL CUATRO; HOMICIDIOS MÚLTIPLES EN IXTAPALUCA Y MONTERREY", co2)
 + page("CRIMEN ORGANIZADO (III) — SINALOA: LOS ACANTOS, DETENCIONES EN MAZATLÁN Y ENFRENTAMIENTO EN AHOME", co3)
 + page("CRIMEN ORGANIZADO (IV) — HOMICIDIOS EN HUEYAPAN DE OCAMPO, TEPITO Y HERMOSILLO", co4)
 + page("CRIMEN ORGANIZADO (V) — ACCIONES INSTITUCIONALES: PROGRESO, AJIJIC, IXTLÁN DEL RÍO Y ATZITZINTLA", co5)
 + page("CRIMEN ORGANIZADO (VI) — RECUPERACIONES DE LAS VENTANAS DE ARGOS 156 Y 157: OCUILTZAPOTLÁN, CHIETLA Y CUITZEO", co6)
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
# la ventana de 158 toca cuatro fechas de calendario (23, 24, 25 y 26-nov); la plantilla de 157 trae 2
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 157 con WINDOW_DAYS = 2"
script = script.replace("WINDOW_DAYS = 2;", "WINDOW_DAYS = 4;")
assert script.count("WINDOW_DAYS = 4;") == 1 and "WINDOW_DAYS = 2;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
