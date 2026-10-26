# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 141.
Uso: python3 tools/datos-argos-141.py <plantilla ARGOS 140> <salida>
Ventana: 25-oct 07:45 → 26-oct 08:37 CDMX. Archivo: argos-2026-10-26.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "141", "2026-10-26", "08:37"
CONSULTA = "2026-10-26, última búsqueda 17:02"
DUR = "24 h 52 min"
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
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= AMARILLOS
 dict(id="ARG-141-001", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-25", hora="~22:30 (solo por resumen)", mu=1, he=2, cu=0, hk=22.5,
  ent="Guanajuato", mun="Pénjamo (col. Lázaro Cárdenas, calle Joaquín Pardavé)", dia="25-OCT, ~22:30 POR RESUMEN",
  title="GUANAJUATO · PÉNJAMO — ATACAN A TRES JÓVENES AFUERA DE UN DOMICILIO: UN MUERTO Y DOS HERIDOS",
  hecho="Pénjamo · <code>COL. LÁZARO CÁRDENAS, CALLE JOAQUÍN PARDAVÉ, SOLO POR RESUMEN</code> · noche del domingo 25-OCT (~22:30), " + RES + "; publicado el lunes 26, por ruta (AM 2026/10/26) · " + FR + " · <b>1 muerto</b> y <b>2 heridos graves</b>, por <i>slug</i> (AM, «un-muerto-y-dos-graves») (🟡 homicidio doloso único) · el muerto falleció en el hospital; heridos de 18 y 19 años, " + RES + " · tres lesionados y muerte extraoficial, por titular de Telediario: <code>MUERTE NO CONFIRMADA POR AUTORIDAD</code> · agresores en motocicleta, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Ataque a tres jóvenes: <b>1 muerto</b> y 2 heridos", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; muerte sin confirmación oficial; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["AM (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lázaro Cárdenas (Pénjamo) no figura en las cinco ediciones previas. Pénjamo en el índice: ARG-133-REC-001 (col. San Miguel, 14-oct) y ARG-138-013 (zona centro, 19-oct): otros hechos. Homicidio en la calle Marfil de la misma colonia (AM 2026/10/22): ventana anterior, otro hecho, 🟡 no recuperable. Ataque a jóvenes en la «zona centro» (Milenio, sin fecha en la ruta): colonia distinta, <code>POSIBLE HECHO DISTINTO</code>, no se cuenta como fuente."),
 dict(id="ARG-141-002", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-25", hora="poco antes de las 20:00 (solo por resumen)", mu=1, he=1, cu=0, hk=19.9,
  ent="Michoacán", mun="Zamora (col. La Medallita, calle Purépero)", dia="25-OCT, ~20:00 POR RESUMEN",
  title="MICHOACÁN · ZAMORA — AGRESIÓN ARMADA EN LA MEDALLITA: UN MUERTO Y UNA MUJER HERIDA",
  hecho="Zamora · <code>COL. LA MEDALLITA, CALLE PURÉPERO, SOLO POR RESUMEN</code> · domingo 25-OCT, publicado ese día, por ruta (Medianews 2026/10/25) · " + AP + " · poco antes de las 20:00, " + RES + " · <b>1 hombre muerto</b> y <b>1 mujer herida</b>, por <i>slug</i> (Medianews; Grupo Marmor) (🟡 homicidio doloso único) · edades contradichas entre medios · la Fiscalía de Michoacán procesó la escena, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Agresión armada: <b>1 muerto</b> y 1 herida", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Medianews (2026/10/25)", "Grupo Marmor (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="La Medallita y Zamora no figuran en las cinco ediciones previas. Zamora en el índice: ARG-129-REC-001 (bar El Nuevo Quijote): otro hecho. Contramuro, IMN México y Respuesta publican el mismo texto: una fuente con Medianews."),
 dict(id="ARG-141-003", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-25", hora="noche, ~23:15 (solo por resumen)", mu=1, he=0, cu=0, hk=23.2,
  ent="Veracruz", mun="Cosoleacaque (barrio Primero, calle Miguel Hidalgo, junto a la Transístmica)", dia="25-OCT, NOCHE POR RESUMEN",
  title="VERACRUZ · COSOLEACAQUE — ASESINAN A BALAZOS A UN CHECADOR DE AUTOBUSES",
  hecho="Cosoleacaque · <code>BARRIO PRIMERO, CALLE MIGUEL HIDALGO, JUNTO A LA CARRETERA TRANSÍSTMICA, SOLO POR RESUMEN</code> · noche del domingo 25-OCT, reporte poco antes de las 23:15, " + RES + "; publicado el lunes 26, por ruta (El Diario de Minatitlán y Municipio Sur 2026/10/26) · " + FR + " · <b>1 muerto</b>: <b>checador de autobuses</b>, por <i>slug</i> (El Diario de Minatitlán) (🟡 homicidio doloso único) · hombre de 33 años con tres heridas de bala, " + RES + " · hombre sin vida con presuntas heridas de bala, por titular (La Opinión) · un segundo lesionado no localizado, " + RES + ": <code>NO SE INTEGRA</code> · <b>ningún detenido publicado</b> · identidad: una sola fuente, no se reproduce",
  panel="<b>Checador de autobuses</b> asesinado: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["El Diario de Minatitlán (2026/10/26)", "Municipio Sur (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="«¡Asesinan al checador!» (Notiver, sin fecha): posible el mismo, no cotejado. NO es ARG-140-018 (camino a Temex, 23-oct, dos muertos): otro lugar y otro día. Barrio Primero no figura en las cinco ediciones previas. ARG-105-REC-004 (Nuevo Teapa–Cosoleacaque): otro hecho."),
 dict(id="ARG-141-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-10-25", hora="~18:45 el hallazgo (solo por resumen)", mu=1, he=0, cu=0, hk=18.75,
  ent="Sinaloa", mun="Culiacán (col. Morelos; hallado junto a Ciudad Universitaria, Malecón Nuevo)", dia="25-OCT, POR TITULAR",
  title="SINALOA · CULIACÁN — PRIVAN DE LA LIBERTAD A UN EXEMPLEADO DEL SUPREMO TRIBUNAL Y LO HALLAN EJECUTADO JUNTO A CIUDAD UNIVERSITARIA",
  hecho="Culiacán · <code>PRIVADO DE LA LIBERTAD EN LA COL. MORELOS; HALLADO A ESPALDAS DE CIUDAD UNIVERSITARIA, BULEVAR FRANCISCO LABASTIDA, SOLO POR RESUMEN</code> · domingo 25-OCT, por titular (Extraoficial, «levantado este domingo») y por ruta (Luz Noticias 2026-10-25) · " + AP + " · hallazgo ~18:45, " + RES + " · <b>1 muerto</b>: <b>exempleado del Supremo Tribunal de Justicia del Estado</b>, por titulares (Luz Noticias; Los Noticieristas) (🟡 homicidio doloso único: exempleado, no servidor público en funciones) · privado de la libertad horas antes, por titular (Diario de Yucatán 2026/10/26) · maniatado y ejecutado a balazos, por titular (Extraoficial) · 38 años, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>Exempleado del Poder Judicial</b> privado de la libertad y ejecutado: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Luz Noticias (2026-10-25, dos notas)", "Revista Espejo (2026/10/26)", "Diario de Yucatán (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="«Maniatado en el Malecón Nuevo» es este cuerpo, por titular de Extraoficial; «encintado cerca de la Prepa UAS» (Luz Noticias 2026-10-25): <code>UNICIDAD INFERIDA POR LUGAR Y RASGOS — POSIBLE SEGUNDO CUERPO, NO SE INTEGRA HASTA VALIDACIÓN</code>. Ciudad Universitaria y Malecón Nuevo no figuran en las cinco ediciones previas. Cuerpo en una vivienda de la col. Jesús Valdez (Luz Noticias 2026-10-25): visto, sin causa de muerte publicada."),
 dict(id="ARG-141-005", estado="MX-ROO", region="Sureste", color="amarillo", impacto="pequeno", fecha="2026-10-26", hora="madrugada (solo por resumen)", mu=0, he=0, cu=0, hk=3,
  ent="Quintana Roo", mun="Cancún (SM 243, calle Los Zapotes)", dia="PUB. 26-OCT; MADRUGADA POR RESUMEN",
  title="QUINTANA ROO · CANCÚN — DISPARAN CONTRA LA CASA DE UNA PRESUNTA EXAGENTE DE TRÁNSITO Y DEJAN UNA AMENAZA",
  hecho="Cancún · <code>SM 243, CALLE LOS ZAPOTES, POR TITULAR (CLIC NOTICIAS; TURQUESA NEWS); «234» EN EL CUERPO DE PORESTO, SOLO POR RESUMEN</code> · madrugada, " + RES + "; publicado el lunes 26, por ruta (PorEsto y Noticaribe 2026/10/26) · " + FR + " · disparos contra la vivienda de una <b>presunta exagente de tránsito municipal</b>, por <i>slug</i> (PorEsto); «agente» en otro resumen: <code>CALIDAD CONTRADICHA</code> (🟡 agresión sin lesionados) · «dejan amenaza», por titular (Sol Quintana Roo); contenido no informado · tres disparos y agresores en motocicleta, " + RES + " · <b>sin lesionados</b> · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Disparos y amenaza contra una vivienda: <b>sin lesionados</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["PorEsto (2026/10/26)", "Noticaribe (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="«Las Palmas: disparan contra dos casas y dejan advertencia» (Quintana Roo Hoy, sin fecha): posible el mismo hecho, no cotejado. SM 243 y Los Zapotes no figuran en las cinco ediciones previas. Cancún en el índice: ARG-130-002 (Los Corales) y ARG-133-007 (Región 201): otros hechos."),
 # ======================= VERDES
 dict(id="ARG-141-006", estado="MX-MIC", region="Occidente", color="verde", impacto="pequeno", fecha="2026-10-26", hora="no fijada", mu=0, he=0, cu=0, hk=2,
  ent="Michoacán", mun="Erongarícuaro", dia="PUB. 26-OCT; HORA NO FIJADA",
  fecha_txt="publicado el 2026-10-26 — DÍA DEL HECHO NO FIJADO",
  title="MICHOACÁN · ERONGARÍCUARO — EJÉRCITO, GUARDIA NACIONAL Y GUARDIA CIVIL DETIENEN A TRES Y ASEGURAN ARMAS Y DROGA",
  hecho="Erongarícuaro · publicado el lunes 26-OCT, por ruta (Medianews 2026/10/26) · " + FR + "; día del aseguramiento no fijado · Ejército, Guardia Nacional y Guardia Civil, por <i>slug</i> (Medianews, «militares-gn-y-gc») · <b>3 detenidos</b>, por <i>slug</i> (🟢 detención y aseguramiento) · armas y droga, por <i>slug</i>; 2 fusiles, 29 cargadores y 541 cartuchos, " + RES + ": <code>DESGLOSE NO INTEGRADO</code> · dosis de droga, 4 teléfonos, equipo táctico y un vehículo, " + RES,
  panel="Aseguramiento: <b>3 detenidos</b>, armas y droga", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="desglose de armamento solo por resumen; día no fijado", I=0, N=0, R=2, A=0,
  fechadas=["Medianews (2026/10/26)"], estatus="Parcialmente corroborado", arm="ARG-141-ARM-001",
  desl="Erongarícuaro no figura en las cinco ediciones previas ni en el índice. A Tiempo publica el mismo hecho: corroboración regional."),
 dict(id="ARG-141-007", estado="MX-GRO", region="Sureste", color="verde", impacto="pequeno", fecha="2026-10-25", hora="no fijada", mu=0, he=0, cu=0, hk=1,
  ent="Guerrero", mun="Iguala y Copalillo", dia="PUB. 25-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-25 — DÍA DEL HECHO NO FIJADO (BOLETÍN AGREGADO DEL 23 AL 25-OCT)",
  title="GUERRERO · IGUALA Y COPALILLO — DETIENEN A TRES INTEGRANTES DE «LOS TLACOS» POR EXTORSIÓN",
  hecho="Iguala y Copalillo · publicado el domingo 25-OCT, por ruta (Código QRO 2026/10/25) · " + AP + "; día de la detención no fijado: el boletín federal agrega del 23 al 25-OCT; si fue el 23 o el 24, es de la ventana de ARGOS 140 · <b>3 detenidos</b>, integrantes de «Los Tlacos», por extorsión, por <i>slug</i> (Código QRO) (🟢 detención) · órdenes de aprehensión por extorsión agravada; uno señalado como operador regional y financiero, " + RES + " · 4 armas, 1 cargador y 3 cartuchos en Copalillo, " + RES + ": <code>NO SE INTEGRA</code> · boletín del Gabinete de Seguridad, por republicadores: una fuente",
  panel="Detención de <b>3 integrantes de «Los Tlacos»</b> por extorsión", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicadores)</span>", nac=NIN, conf="★★★☆☆",
  campo="día no fijado; cifras de armamento solo por resumen", I=1, N=0, R=2, A=0,
  fechadas=["Código QRO (2026/10/25)", "Argonmexico (2026/10/26)"], estatus="Parcialmente corroborado", arm=None, cual=True,
  desl="«Los Tlacos» en el índice: ARG-110-REC-001 (San Miguel Totolapan, agosto): otro hecho. Grupo Animal reproduce el boletín: una fuente."),
]

# ---------------------------------------------------------------- RECUPERACIONES (ventana de ARGOS 140; solo alto impacto)
R = [
 dict(id="ARG-141-REC-001", estado="MX-CMX", region="Centro", fecha="2026-10-25", hora="madrugada (solo por resumen)", orig="ARGOS 140 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=2, he=1, cu=0,
  ent="Ciudad de México", mun="La Magdalena Contreras (col. Cuauhtémoc, Cruz Blanca y Cruz Verde)", dia="25-OCT, MADRUGADA",
  title="CIUDAD DE MÉXICO · MAGDALENA CONTRERAS — DISPARAN EN UNA FIESTA PATRONAL DE SAN JUDAS TADEO: DOS MUERTOS Y UN HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 140 — HORA SOLO POR RESUMEN</code> · La Magdalena Contreras · <code>COL. CUAUHTÉMOC, CRUZ BLANCA Y CRUZ VERDE, SOLO POR RESUMEN</code> · madrugada del domingo 25-OCT, en todos los resúmenes, antes de las 07:45; primera ruta fechada: 25-OCT (La Jornada; El Independiente) · fiesta o baile patronal de San Judas Tadeo, por titulares · <b>2 hombres muertos</b> y <b>al menos 1 herido</b>, por titular (La Jornada); un lesionado «baleado cinco veces», por titular (El Gráfico 2026/10/26): <code>POSIBLE SEGUNDO HERIDO</code> (🔴 homicidio múltiple) · «riña» que escaló a disparos, por titular (La Jornada) · herido: hombre de 41 años según la SSC, " + RES + "; una mujer en otros medios: <code>SEXO DEL HERIDO CONTRADICHO</code> · edades de las víctimas contradichas · el agresor huyó; alias en un solo medio · la alcaldía suspendió los festejos, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Disparos en fiesta patronal: <b>2 muertos</b> y 1 herido", inst="SSC CDMX" + PR, nac="La Jornada · El Universal · Milenio · El Gráfico",
  conf="★★★☆☆", campo="hora solo por resumen; sexo del herido contradicho", I=1, N=4, R=4, A=0,
  fechadas=["La Jornada (2026/10/25)", "El Independiente (2026/10/25)", "Cúspide (2026/10/26)", "El Gráfico (2026/10/26)"],
  desl="La Magdalena Contreras no figura en las cinco ediciones previas. Cúspide y Quinta Fuerza dicen «domingo 26»: error de calendario (el 26 es lunes)."),
 dict(id="ARG-141-REC-002", estado="MX-VER", region="Golfo", fecha="2026-10-24", hora="noche del 24 o madrugada del 25 (solo por resumen)", orig="ARGOS 140 — DÍA Y HORA SOLO POR RESUMEN", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Veracruz", mun="Acultzingo (vía férrea, km 288+450, Cumbres de Acultzingo–Nogales)", dia="24-25-OCT, NOCHE",
  title="VERACRUZ · ACULTZINGO — ASESINAN A DOS CUSTODIOS FERROVIARIOS AL FRUSTRAR EL ASALTO A UN TREN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 140 — DÍA Y HORA SOLO POR RESUMEN</code> · Acultzingo · <code>VÍA FÉRREA, KM 288+450, CUMBRES DE ACULTZINGO–NOGALES; ATITLA DE ABAJO O COXOLITLA DE ARRIBA, SOLO POR RESUMEN: CONTRADICHO</code> · noche del sábado 24 (22:00-23:00) o madrugada del domingo 25, " + RES + "; antes de las 07:45 en todas las versiones · primera ruta fechada: 25-OCT (La Silla Rota; Golpe Político) · <b>2 custodios ferroviarios muertos</b>, por titulares (🔴 homicidio múltiple) · al intentar frustrar el asalto a un tren de carga, por titulares · golpes y pedradas, por titulares (La Nigua; El Buen Tono); sin arma de fuego, " + RES + " · la Fiscalía de Veracruz investiga · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Dos custodios ferroviarios</b> asesinados en un asalto a tren", inst=SB, nac="La Silla Rota", conf="★★★☆☆",
  campo="día y hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=10, A=0,
  fechadas=["La Silla Rota (2026/10/25)", "Golpe Político (2026/10/25)", "Plumas Libres (2026/10/26)"],
  desl="Acultzingo no figura en las cinco ediciones previas ni en el índice. Descarrilamiento del 11-oct en el mismo municipio, por resumen: sin víctimas, no se integra."),
 dict(id="ARG-141-REC-003", estado="MX-CHP", region="Sureste", fecha="2026-10-21", hora="no fijada", orig="ARGOS 140 — FECHAS DE HALLAZGO SOLO POR RESUMEN", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Chiapas", mun="Ostuacán", dia="21-23-OCT",
  title="CHIAPAS · OSTUACÁN — DOBLE FEMINICIDIO DE UNA MUJER Y SU NIETA DE 12 AÑOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 140 — FECHAS DE HALLAZGO SOLO POR RESUMEN</code> · Ostuacán · desaparecidas el lunes 19-OCT; la mujer, hallada el miércoles 21, y la niña, el 23, " + RES + " · primera ruta fechada: 24-OCT (La Jornada) · <b>doble feminicidio</b>: <b>una mujer y su nieta de 12 años</b>, por titulares (Latinus; Quinto Poder) (🔴 homicidio múltiple) · «venganza personal», según el fiscal, por titular (La Jornada 2026/10/26) · dos detenidos informados la tarde del sábado 24, " + RES + " · pobladores <b>lincharon a los dos detenidos: uno murió</b>, por <i>slug</i> (La Jornada 2026/10/24; La Razón 2026/10/26) · incendio de la presidencia municipal: una fuente, <code>NO CONFIRMADO</code> · identidades: no se reproducen",
  panel="<b>Doble feminicidio</b>: una mujer y su nieta de 12 años", inst="Fiscalía de Chiapas" + PT, nac="La Jornada · Latinus · La Razón · Reforma · Milenio · N+",
  conf="★★★☆☆", campo="fechas de hallazgo solo por resumen", I=1, N=6, R=1, A=0,
  fechadas=["La Jornada (2026/10/24 y 2026/10/26)", "Latinus (2026/10/25)", "Quinto Poder (2026/10/25)", "La Razón (2026/10/26)"],
  desl="Ostuacán no figura en las cinco ediciones previas ni en el índice. El linchamiento del 24 (un detenido muerto) y las dos detenciones son hechos distintos de la misma ventana, 🟡 y 🟢: no se recuperan; el incendio de la presidencia, sin confirmar, no cambia el color. El liveblog de Infobae del 25 no fecha nada."),
 dict(id="ARG-141-REC-004", estado="MX-SON", region="Noroeste", fecha="2026-10-24", hora="no fijada", orig="ARGOS 140 — DÍA DEL HALLAZGO SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Sonora", mun="San Luis Río Colorado (zona desértica al sur de la ciudad)", dia="24-OCT",
  title="SONORA · SAN LUIS RÍO COLORADO — UN COLECTIVO HALLA TRES FOSAS CON RESTOS HUMANOS EN ZONA DESÉRTICA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 140 — DÍA DEL HALLAZGO SOLO POR RESUMEN</code> · San Luis Río Colorado · <code>ZONA DESÉRTICA AL SUR DE LA CIUDAD, POR TITULAR</code> · sábado 24-OCT, jornada de búsqueda de un colectivo, " + RES + " · primera ruta fechada: 25-OCT (El Imparcial) · <b>tres fosas con restos humanos</b>, por titular (El Imparcial) (🔴 fosas) · número de personas contradicho entre resúmenes y titulares: <code>NO DETERMINADO — CIFRA NO CONFIRMADA POR AUTORIDAD</code> · identificación genética pendiente, " + RES + " · sin comunicado de la Fiscalía de Sonora",
  panel="<b>Tres fosas</b> con restos humanos", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="día del hallazgo solo por resumen; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["El Imparcial (2026/10/25)"],
  desl="San Luis Río Colorado no figura en las cinco ediciones previas ni en el índice. Restos sin número de víctimas confirmado por autoridad: fuera de todo recuento."),
 dict(id="ARG-141-REC-005", estado="MX-SIN", region="Noroeste", fecha="2026-10-23", hora="noche (solo por resumen)", orig="ARGOS 140 — DÍA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Sinaloa", mun="Concordia (inmediaciones del poblado Zavala)", dia="23-OCT, NOCHE",
  title="SINALOA · CONCORDIA — CIVILES ARMADOS AGREDEN A PERSONAL DE SEGURIDAD CERCA DE ZAVALA: CINCO DETENIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 140 — DÍA SOLO POR RESUMEN</code> · Concordia · <code>INMEDIACIONES DEL POBLADO ZAVALA, POR TITULAR</code> · noche del viernes 23-OCT, según la SSP de Sinaloa, " + RES + " · <b>agresión armada contra personal de seguridad</b>, por titulares (Los Noticieristas; Sinaloahoy, «tras agresión armada») y <i>slug</i> («tras repeler agresión», Sinaloahoy; «emboscan a militares», TV Azteca) (🔴 ataque contra autoridades: el grupo inició); recorrido o patrullaje, " + RES + " · Policía Estatal, Grupo de Operaciones Especiales y Ejército, " + RES + " · <b>5 detenidos</b>, por titulares · 3 de ellos heridos, " + RES + ": <code>NO SE INTEGRA</code> · fusiles AK-47 y equipo táctico, por titular (Sinaloahoy); cifras, " + RES + " · campamento clandestino inhabilitado en Zavala con cinco detenidos, por titular (Noroeste) y en el boletín federal del 23 al 25-oct: <code>PROBABLE MISMO OPERATIVO (MUNICIPIO, LOCALIDAD, CINCO DETENIDOS, CORPORACIONES Y ARMAS LARGAS COINCIDEN) — UNA SOLA FICHA; SI LA AUTORIDAD INICIÓ, BAJA A 🟡</code> · armamento fuera de todo total",
  panel="<b>Agresión a personal de seguridad</b>: 5 detenidos", inst="SSP Sinaloa" + PR, nac="Milenio",
  conf="★★★☆☆", campo="día solo por resumen; probable mismo operativo que el campamento", I=1, N=1, R=5, A=0,
  fechadas=["Medios OBSON (2026/10/26)"],
  desl="Zavala no figura en las cinco ediciones previas ni en el índice; Concordia en ARGOS 137 (ARG-126-004 y otros) es otro hecho. Los heridos son agresores, solo por resumen: fuera de todo recuento."),
]

for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-141-ARM-001", ficha="ARG-141-006", estado="MX-MIC", region="Occidente", color="verde", ent="Michoacán", mun="Erongarícuaro",
  fecha="2026-10-26", fecha_txt="pub. 26-oct; día no fijado", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 3], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="Ejército, Guardia Nacional y Guardia Civil <span class=\"muted-note\">(por <i>slug</i>)</span>", conf="Bajo",
  nota="3 detenidos por slug (Medianews 2026/10/26); 2 fusiles, 29 cargadores y 541 cartuchos solo por resumen: no integrados",
  fuentes=["Medianews (2026/10/26)", "A Tiempo (sin fecha en la ruta)"]),
]
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
ND = [any(a["integra"] for a in ARM) and all(i in a.get("nd", []) for a in ARM if a["integra"]) for i in range(10)]
def tv(i, f=str): return "n/d" if ND[i] else f(TOT[i])
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["estado"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
HORAS = 24 + 52 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 3], TOT
assert cnt == {"rojo": 0, "amarillo": 5, "verde": 2}, cnt
assert cnt_rec == {"rojo": 5, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC) == (4, 3, 0, 6, 1), (MU, HE, CU, MU_REC, HE_REC)
assert (NFR, NAP, len(ENT), len(ENT_ROJO)) == (4, 3, 6, 0), (NFR, NAP, len(ENT), len(ENT_ROJO))
assert DENS == "0,28", DENS
assert sorted(e["id"] for e in E) == [f"ARG-141-{i+1:03d}" for i in range(len(E))]
assert len(set(r["id"] for r in R)) == len(R) and all(r["id"] == f"ARG-141-REC-{i+1:03d}" for i, r in enumerate(R))
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-25" or x in R, x["id"]

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
head = head.replace("<title>ARGOS 140 — Reporte Nacional de Seguridad — 2026-10-25</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA SSC Y A LA FISCALÍA DE LA CIUDAD DE MÉXICO LA HORA DEL ATAQUE, EL NÚMERO DE LESIONADOS Y SU IDENTIDAD</b> (ARG-141-REC-001).
      <br><b>2. COTEJE CON LA SSP DE SINALOA Y EL GABINETE DE SEGURIDAD SI LA AGRESIÓN Y EL CAMPAMENTO INHABILITADO SON EL MISMO OPERATIVO Y QUIÉN INICIÓ EL FUEGO, Y AUDITE EL DESGLOSE DEL ARMAMENTO</b> (ARG-141-REC-005).
      <br><b>3. SOLICITE A LA FISCALÍA DE VERACRUZ LA HORA DEL ATAQUE Y VIGILE CON LA CONCESIONARIA Y LA GUARDIA NACIONAL EL TRAMO FERROVIARIO AFECTADO</b> (ARG-141-REC-002).
      <br><b>4. SOLICITE A LA FISCALÍA DE SONORA EL NÚMERO DE PERSONAS Y LA IDENTIFICACIÓN GENÉTICA DE LOS RESTOS, Y COTÉJELOS CON LAS FICHAS DE BÚSQUEDA DEL COLECTIVO</b> (ARG-141-REC-004).
      <br><b>5. SOLICITE A LA FISCALÍA DE CHIAPAS LA SITUACIÓN JURÍDICA DEL DETENIDO SOBREVIVIENTE Y VIGILE SU CUSTODIA</b> (ARG-141-REC-003).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>25-oct 07:45 → 26-oct 08:37 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · dentro de cada color, del más reciente al más antiguo · <b>ningún rojo propio fijado en la ventana</b>.
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
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Muertos por agresión</th><th>Heridos</th><th>Cuerpos hallados</th><th>Armas cortas</th><th>Armas largas</th><th>Armas sin categoría</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos en aseguramiento</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b></td><td><b>{tv(0)}</b></td><td><b>{tv(1)}</b></td><td><b>{tv(2)}</b></td><td><b>{tv(4, fmt)}</b></td><td><b>{tv(5)}</b></td><td><b>{tv(6)}</b></td><td><b>{tv(7)}</b></td><td><b>{tv(8)}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: 1 evento contabilizado (ARG-141-ARM-001: detenidos por <i>slug</i>, <b>desglose solo por resumen</b>; <code>n/d</code> = no publicado en fuente citable, no ausencia) y 1 evento cualitativo sin cantidad (ARG-141-007) · <b>los totales incluyen 1 muerto no confirmado por autoridad</b> (ARG-141-001) · <b>marcas</b>: {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> y {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · en las recuperaciones, <b>{MU_REC} muertos</b> y <b>{HE_REC} heridos</b>, fuera de todo total. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: <b>ARG-136-006 (exfiscal)</b>: vinculación federal por traición a la patria, por titular (Tribuna 2026/10/25), ya reportada en ARGOS 140; impugnación anunciada por la defensa, {RES}; «Pelea… para salir de El Altiplano» (El Diario de Chihuahua 2026/oct/26) se refiere al penal; <code>NINGUNA ES SENTENCIA</code> · <b>ARG-140-020 (Xalapa)</b>: prisión preventiva por homicidio doloso calificado, por <i>slug</i> (Hora Cero 2026/10/24); «oficiosa», {RES}; vinculación no publicada · <b>ARG-140-005 (León)</b>: 4 cuerpos por titular (AM 2026/10/23) y 5 por <i>slug</i> (La Silla Rota y otros, 2026/10/21): <code>CIFRA CONTRADICHA</code> · <b>ARG-140-013 (Linares)</b>: la víctima era el encargado del depósito, por <i>slug</i> (MVS 2026/10/25); edad 47 o 55: <code>CONTRADICHA</code> · <b>ARG-140-017</b>: reparto por titular (La Nigua): 1 muerto en Álamo y 2 heridos en Papantla · <b>ARG-140-003</b>: «supervisor del Subcentro de Comando; SSPE confirma muerte de elemento activo del C4i», por titular (Los Noticieristas); ningún detenido · <b>ARG-140-023</b>: nombre y alias del detenido coinciden en El Financiero (2026/10/22) y Expreso (2026/10/23); boletín no leído · <b>ARG-140-REC-002 (Cocotitlán)</b>: «emboscan a policías», por titular (El Universal) · <b>ARG-140-REC-003 (Ecatepec)</b>: sin fragmento que fije el día · <b>ARG-140-021 (Juchitán)</b>: vinculación no publicada.
  </p>
'''

rec1 = "\n".join(ficha(r, True) for r in R[0:3])
rec2 = "\n".join(ficha(r, True) for r in R[3:])
byid = {e["id"]: e for e in E}
co1 = "\n".join(ficha(byid[i]) for i in ("ARG-141-001", "ARG-141-002", "ARG-141-003", "ARG-141-004"))
co2 = "\n".join(ficha(byid[i]) for i in ("ARG-141-005", "ARG-141-006", "ARG-141-007"))

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>NO PUBLICADO EN FUENTE CITABLE</code> en el único evento"
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
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>, por <i>slug</i>"),
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
    <div class="map-caption">Un aseguramiento contabilizado: Michoacán.</div>
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
{chr(10).join(armrow(a) for a in ARM)}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: Occidente, 1 evento (3 detenidos; armamento sin desglose citable); el resto de regiones, sin evento integrable. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: Guerrero, Copalillo (ARG-141-007), armas sin cifra citable · Sinaloa, Concordia (ARG-141-REC-005), fusiles AK-47 sin cifra citable, fuera de todo total.
    <br><code>VISTOS, NO INTEGRADOS — BOLETÍN FEDERAL AGREGADO DEL 23, 24 Y 25-OCT, DÍA DE CADA ACCIÓN NO FIJADO, CIFRAS SOLO POR RESUMEN, NO HEREDABLES</code>: Zacatecas (Tlaltenango y Villanueva), Veracruz (Tlalixcoyan), Sinaloa (Guardia Nacional), Sonora, Colima, Tabasco, Baja California (Mexicali), Ciudad de México (Gustavo A. Madero), Jalisco y Tamaulipas: sin desglose citable; cifras en el archivo de equipos · <b>Sonora, Arizpe</b>: presunto mando abatido, 4 detenidos y armas largas y cortas, sábado 24 (ventana de ARGOS 140); quién inició no determinado (🟡): no recuperable · <b>Puebla, Tehuacán</b>: detención y arma larga del lunes 26 por la mañana, posterior al cierre: ARGOS 142.
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
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Fallo condenatorio del 8-oct por el triple feminicidio, por <i>slug</i> (La Silla Rota 2026/10/9)</td><td><b>Sin pena</b>: audiencia de individualización el 28-oct a las 17:00, {RES}</td><td>Tribunal de Enjuiciamiento de Tulancingo <span class="muted-note">(solo por resumen)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín de la PGJEH</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Saltillo o Ramos Arizpe</td><td>Transporte de más de un kilo de metanfetamina, {RES}</td><td>7 años (listado FGR, 22-oct) o 7 años 6 meses (El Siglo de Torreón), {RES}</td><td>FGR</td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · pena y municipio no coinciden · boletín no leído</td><td>No confirmado</td></tr>
      <tr><td><b>Veracruz</b><br>Pánuco, {RES}</td><td>Portación de arma de uso reservado, por fragmento del listado (DPE/4787/2026, 21-oct)</td><td>4 años 8 meses, {RES}</td><td>FGR</td><td><code>POSIBLE CASO HOMÓNIMO</code> · publicado antes de la ventana · boletín no leído</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Candidatas heredadas, publicadas antes de la ventana y sin boletín leído</b>: Ensenada, tres sentenciados, 158 años 9 meses cada uno por titular, sentencia del 16-oct (Infobae 2026/10/17) · General Cepeda, más de 13 años por huachicol, por titular (Red Metropolitana 2026/10/19), procedimiento abreviado {RES} · Culiacán, 18 años (19-oct) · Caborca, 8 años, caso no identificado · FGR Guadalajara, 3 años, no localizado. <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida: listados de <code>fgr.org.mx</code> sin texto de comunicado; <code>gob.mx/fgr</code> sin resultado de la ventana</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>17 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Sin · NL, Tamps, SLP, Zac · Jal, Ags, Gto · CDMX, Edomex, Mor · Ver, Tab · Oax, Gro, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>17</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>6</b>: Son, Coah · Col, Nay, Mich · Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>9</b>: BCS, Chih, Dgo · Pue, Qro, Tlax, Hgo · Chis, Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 26-oct 08:37: código <code>000</code> · <b>dominios confirmados</b>: <code>fgjtam.gob.mx</code>, <code>fiscaliazacatecas.gob.mx</code>, <code>fiscaliasinaloa.mx</code>, <code>fiscaliatabasco.gob.mx</code>, <code>portal.fgeguanajuato.gob.mx</code>, <code>fiscalia-aguascalientes.gob.mx</code>, <code>fgeqroo.gob.mx</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 23 de 32 con consulta propia por entidad</b> · <b>9 solo por consulta regional amplia</b>: Chih, Dgo · Coah, SLP · Ags · Edomex, Tlax, Hgo, Qro · <b>armamento: 13 de 32 por dominio oficial</b> —Chih, Dgo · Tamps, SLP, Zac · Mich · CDMX, Mor, Pue, Hgo, Qro · Tab · Chis—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (19): BC, BCS, Son, Sin · NL, Coah · Jal, Col, Nay, Ags, Gto · Edomex, Tlax · Ver · Oax, Gro, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 23, 24 y 25-oct</b>: existe un agregado; consultado por sus republicadores (Ultranoticias, RED113, Talla Política; Argonmexico 2026/10/26): día de cada acción no fijado · <b>acciones del 26-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · Guardia Nacional, Defensa, Semar y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 26-OCT 08:37: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Sin rojo propio fijado en la ventana</b>: el nivel lo fijan cinco rojos de la ventana de ARGOS 140 recuperados en esta edición (ver panorama), fuera de los totales.
      <br><b>2.</b> <b>Violencia operativa</b>: homicidios únicos y una agresión con amenaza; dos víctimas vinculadas a instituciones de justicia o seguridad.
      <br><b>3.</b> <b>Respuesta institucional</b>: dos detenciones con armamento sin desglose citable; ninguna sentencia integrable.
      <br><b>4.</b> <b>Riesgo de arrastre</b>: un ataque mortal a un agente ministerial del lunes por la mañana, posterior al cierre, pasa a ARGOS 142.
      <br><b>5.</b> <code>{NFR + NAP} DE {len(E)} HECHOS SIN HORA FIJADA Y VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 140 SIN NORMALIZAR POR HORA.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. PÉNJAMO: CUARTO ATAQUE ARMADO CON VÍCTIMAS EN DOCE DÍAS</b> (cálculo propio): ARG-133-REC-001, ARG-138-013, homicidio de la calle Marfil del 21-oct (AM 2026/10/22; ventana de ARGOS 140, sin ficha) y ARG-141-001; dos en la col. Lázaro Cárdenas. Línea: <b>solicitar a la FGE Guanajuato el cotejo balístico de los cuatro</b> — hipótesis.
      <br><b>2. TRANSPORTE: CUATRO TRABAJADORES DEL SECTOR ASESINADOS EN SIETE DÍAS, SEGÚN EL ÍNDICE</b> (cálculo propio): ARG-137-014 (camionero), ARG-139-009 (conductor), ARG-140-012 (operador) y ARG-141-003 (checador). Línea: <b>solicitar a las fiscalías si las víctimas denunciaron extorsión o cobro de piso</b> — vínculo no acreditado.
      <br><b>3. PERSONAL O EXPERSONAL DE INSTITUCIONES DE SEGURIDAD Y JUSTICIA COMO BLANCO: CUATRO HECHOS EN TRES DÍAS</b> (cálculo propio): ARG-140-002, ARG-140-003, ARG-141-004 y ARG-141-005. Línea: <b>solicitar a las fiscalías de Sinaloa y Quintana Roo si las víctimas tenían amenazas previas, y vigilar al personal en activo de las mismas áreas</b>.
      <br><b>4. ZAMORA–JACONA: TERCER ATAQUE ARMADO DEL ÍNDICE EN OCTUBRE</b> (cálculo propio): ARG-129-REC-001 (bar), ARG-130-001 (base de Bomberos y policías) y ARG-141-002. Línea: <b>solicitar a la FGE Michoacán si los tres comparten armas o agresores</b> — hipótesis.
      <br><b>5. «LOS TLACOS»: DETENCIÓN POR EXTORSIÓN DE UN GRUPO YA ASOCIADO A UNA INCURSIÓN CON SEIS MUERTOS</b> (ARG-110-REC-001 y ARG-141-007). Línea: <b>solicitar a la FGR y a la FGE Guerrero si los detenidos se vinculan con esa incursión y con la red de cobro</b> — vínculo no acreditado.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>NO REVISADA</code>; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>gob.mx/fgr</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — VIOLENCIA OPERATIVA: GUANAJUATO, MICHOACÁN, VERACRUZ Y SINALOA", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA Y ACCIONES INSTITUCIONALES: QUINTANA ROO, MICHOACÁN Y GUERRERO", co2)
 + page("CRIMEN ORGANIZADO (III) — VENTANA ANTERIOR: ARGOS 140 (I)", rec1)
 + page("CRIMEN ORGANIZADO (IV) — VENTANA ANTERIOR: ARGOS 140 (II)", rec2)
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
assert "WINDOW_DAYS = 5;" in script
script = script.replace("WINDOW_DAYS = 5;", "WINDOW_DAYS = 2;")  # la ventana toca dos fechas de calendario (25 y 26-oct)
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, MU, HE, CU, DENS)
