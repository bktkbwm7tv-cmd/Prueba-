# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 144.
Uso: python3 tools/datos-argos-144.py <plantilla ARGOS 143> <salida>
Ventana: 28-oct 08:28 → 29-oct 11:36 CDMX. Archivo: argos-2026-10-29.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "144", "2026-10-29", "11:36"
CONSULTA = "2026-10-29, última búsqueda 13:39"
DUR = "27 h 08 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 08:28 DEL 28, ES DE LA VENTANA DE ARGOS 143 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-144-001", estado="MX-SON", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-28", hora="~19:44, atribuida a la Fiscalía de Sonora (solo por resumen)", mu=1, he=0, cu=0, hk=19.7,
  ent="Sonora", mun="Magdalena de Kino (col. Centro, instalaciones de la AMIC)", dia="28-OCT, POR RUTA",
  title="SONORA · MAGDALENA DE KINO — ATACAN A BALAZOS LAS INSTALACIONES DE LA AGENCIA MINISTERIAL DE INVESTIGACIÓN CRIMINAL: MUERE UN AGENTE",
  hecho="Magdalena de Kino · <code>COL. CENTRO, INSTALACIONES DE LA AMIC, SOLO POR RESUMEN</code> · miércoles 28-OCT, por ruta (Proyecto Puente 2026/10/28) · ~19:44, hora atribuida a la <b>Fiscalía de Sonora</b>, " + RES + " · <b>ataque armado contra las instalaciones de la AMIC</b>, por titular (El Universal; UnoTV; Expreso) (🔴 ataque contra autoridades: el grupo agrede una sede de la corporación) · <b>1 agente ministerial muerto</b>, por titular; nombre por titular de un medio abierto (El Congresista): no se reproduce · AMIC, 45/a. Zona Militar, Policía Estatal y municipal acudieron, " + RES + " · <b>ningún detenido publicado</b> · vínculo de la víctima con narcomenudeo: hipótesis de un medio, " + RES + ", no se integra",
  panel="<b>Ataque armado contra instalaciones de la AMIC</b>: 1 agente muerto", inst="Fiscalía de Sonora" + PR, nac="Infobae · UnoTV · El Universal", conf="★★★☆☆",
  campo="hora y comunicado de la Fiscalía solo por resumen; sin boletín indexado", I=1, N=3, R=3, A=1,
  fechadas=["Proyecto Puente (2026/10/28)", "Infobae (2026/10/29)", "Diario de Tabasco (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Magdalena de Kino no figura en las cinco ediciones previas ni en el índice (el patrón «AMIC» devuelve otros hechos). Sáric (incendio en Seguridad Pública, madrugada del 27): otro hecho, ventana de ARGOS 142, no se integra. Diario de Tabasco republica: no suma fuente independiente."),
 dict(id="ARG-144-002", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-28", hora="noche, ~21:45, atribuida a la Fiscalía (solo por resumen)", mu=2, he=1, cu=0, hk=21.75,
  ent="Michoacán", mun="Indaparapeo (comunidad El Triunfo, calle Prolongación de Bravo)", dia="28-OCT, POR RUTA DEL 29",
  title="MICHOACÁN · INDAPARAPEO — ASESINAN A UN REGIDOR DEL AYUNTAMIENTO Y A SU ESPOSA; SU HIJO, HERIDO",
  hecho="Indaparapeo · <code>COMUNIDAD EL TRIUNFO, CALLE PROLONGACIÓN DE BRAVO, SOLO POR RESUMEN</code> · noche del miércoles 28-OCT, por resumen; publicación del 29, por ruta (Grupo Marmor; La Silla Rota; Esfera Noticias 2026/10/29) · ~21:45, " + RES + " · <b>2 muertos</b>: <b>regidor del Ayuntamiento</b> y <b>su esposa</b>, por titular (La Silla Rota; Grupo Marmor; La Voz de Michoacán) · <b>1 herido</b>: su hijo, por titular (🔴 víctima servidor público; víctimas múltiples) · la esposa murió en el lugar y el regidor en el hospital, " + RES + " · agresores en al menos tres vehículos, " + RES + " · <b>ningún detenido publicado</b> · amenazas previas a pobladores: versión de un partido político, no de autoridad: no se integra",
  panel="<b>Regidor y su esposa asesinados</b>: 2 muertos y 1 herido", inst="FGE Michoacán" + PR, nac="La Silla Rota · TV Azteca · Noroeste · Diario de México", conf="★★★☆☆",
  campo="hora y declaración de la Fiscalía solo por resumen; día del hecho por resumen (rutas del 29)", I=1, N=4, R=4, A=1,
  fechadas=["Grupo Marmor (2026/10/29)", "La Silla Rota (2026/10/29)", "Esfera Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Indaparapeo en el índice: ARG-140-016 (disparos contra una base de policías, 23-oct): otro hecho. RED113 republica: no suma fuente independiente."),
 dict(id="ARG-144-003", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-28", hora="~19:30 (solo por resumen)", mu=3, he=0, cu=0, hk=19.5,
  ent="Guanajuato", mun="Acámbaro (comunidad Santiaguillo)", dia="28-OCT, POR RUTA",
  title="GUANAJUATO · ACÁMBARO — ATAQUE CON ESCOPETA EN LA COMUNIDAD DE SANTIAGUILLO: TRES MUERTOS, UNO DE ELLOS DE 16 AÑOS",
  hecho="Acámbaro · <code>COMUNIDAD SANTIAGUILLO, DOMICILIO, SOLO POR RESUMEN</code> · miércoles 28-OCT, por ruta (Correo 2026/oct/28, primera publicación) · ~19:30, " + RES + " · <b>3 muertos</b>, por titular (Correo; La Silla Rota; AM; Noticieros en Línea), <b>uno de 16 años</b>, por titular (AM; NPI); «un adolescente», por titular (Noticieros en Línea) (🔴 homicidio múltiple) · <b>escopeta</b>, por titular; casquillos calibre 12, " + RES + " · <b>riña</b>, por titular (AM); «discusión entre vecinos», por titular (Observatorio Informativo, que sitúa el hecho el «martes», " + RES + ": <code>CONTRADICHO</code>) · agresor prófugo · <b>ningún detenido publicado</b>",
  panel="<b>Ataque con escopeta: 3 muertos</b>, uno de 16 años", inst=SB, nac="La Silla Rota · Meganoticias", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=7, A=0,
  fechadas=["Correo (2026/oct/28)", "La Silla Rota (2026/10/29)", "AM (2026/10/29)", "Noticieros en Línea (2026/oct/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Santiaguillo no figura en las cinco ediciones previas ni en el índice. Acámbaro: ARG-142-004 (col. Velasco Ibarra, 26-oct) y ARG-143-REC-003 (Campamento Ferrocarrilero, 19-oct): otros hechos. «Guardia Nocturna» (junio): otro hecho."),
 dict(id="ARG-144-004", estado="MX-CHP", region="Sureste", color="rojo", impacto="grande", fecha="2026-10-28", hora="tarde (solo por resumen; un medio local: mañana)", mu=1, he=0, cu=0, hk=16,
  ent="Chiapas", mun="Chenalhó (comunidad Yabteclum)", dia="28-OCT, POR RUTA",
  title="CHIAPAS · CHENALHÓ — ASESINAN A BALAZOS A UN DEFENSOR DE DERECHOS HUMANOS DE FAMILIAS DESPLAZADAS, BENEFICIARIO DEL MECANISMO FEDERAL DE PROTECCIÓN",
  hecho="Chenalhó · <code>COMUNIDAD YABTECLUM, SOLO POR RESUMEN</code> · miércoles 28-OCT, por ruta (La Jornada; La Silla Rota; Proceso; Heraldo de México 2026/10/28) · tarde, " + RES + "; «mañana», un medio local: <code>CONTRADICHO</code> · <b>1 muerto</b>: <b>defensor de derechos humanos</b> y representante de familias desplazadas, por titular (La Jornada; Proceso; La Silla Rota) (🔴 víctima persona defensora) · <b>con protección federal desde 2023</b>, por titular (Diario Puntual) · dos agresores en motocicleta, " + RES + " · el <b>fiscal de Chiapas</b> ordenó un grupo especial, " + RES + " · <b>ningún detenido publicado</b>",
  panel="<b>Defensor de derechos humanos asesinado</b>: 1 muerto", inst="Fiscal General de Chiapas" + PR, nac="La Jornada · La Silla Rota · Proceso · Heraldo de México · Infobae", conf="★★★☆☆",
  campo="hora contradicha y solo por resumen; declaración del fiscal solo por resumen", I=1, N=5, R=0, A=0,
  fechadas=["La Jornada (2026/10/28)", "La Silla Rota (2026/10/28)", "Proceso (2026/10/28)", "Heraldo de México (2026/10/28)", "Infobae (2026/10/29)", "Diario Puntual (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chenalhó y Yabteclum no figuran en las cinco ediciones previas ni en el índice. Ninguna fuente regional de Chiapas localizada. La Silla Rota contabiliza nueve activistas asesinados desde 2019 en Chiapas: recuento de un medio, no se integra."),
 dict(id="ARG-144-005", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-28", hora="~14:30 (solo por resumen)", mu=2, he=0, cu=0, hk=14.5,
  ent="Guanajuato", mun="Irapuato (col. Azteca y col. Nuevo Amanecer)", dia="28-OCT, POR RUTA; HORA NO FIJADA",
  title="GUANAJUATO · IRAPUATO — ATAQUE ARMADO EN LA COLONIA AZTECA: DOS MUERTOS",
  hecho="Irapuato · <code>COL. AZTECA, POR <i>SLUG</i> (CORREO); COL. NUEVO AMANECER, POR <i>SLUG</i> (AM): CONTRADICHO</code> · miércoles 28-OCT, por ruta (Correo 2026/oct/28; AM 2026/10/28; Primer Plano 2026/10/28) · " + AP + "; ~14:30, " + RES + ": " + RET + " · <b>2 muertos</b>, por titular (Correo; AM; Primer Plano) (🔴 homicidio múltiple) · uno murió al derrapar en motocicleta mientras era trasladado, " + RES + " · alias de una víctima: medio local, no se reproduce · <b>ningún detenido publicado</b>",
  panel="<b>Ataque armado: 2 muertos</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; colonia contradicha; ninguna fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Correo (2026/oct/28)", "AM (2026/10/28)", "Primer Plano (2026/10/28)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Azteca y Nuevo Amanecer no figuran en las cinco ediciones previas ni en el índice. Irapuato en el índice: ARG-133-010, ARG-134-REC-001, ARG-134-018 y ARG-140-014: otros hechos. Col. Benito Juárez de Irapuato (1 muerto, ~07:15 del 28 solo por resumen; Correo y AM 2026/10/28): otro hecho, ventana de ARGOS 143, 🟡: visto."),
 dict(id="ARG-144-006", estado="MX-SLP", region="Noreste", color="rojo", impacto="mediano", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=0, hk=0.9,
  ent="San Luis Potosí", mun="Ciudad del Maíz (cerca del ejido Palomas)", dia="PUB. 28-OCT; DÍA DEL HALLAZGO NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL HALLAZGO NO FIJADO",
  title="SAN LUIS POTOSÍ · CIUDAD DEL MAÍZ — LOCALIZAN RESTOS ÓSEOS EN UN POSIBLE SITIO DE INHUMACIÓN CLANDESTINA",
  hecho="Ciudad del Maíz · <code>PREDIOS CERCA DEL EJIDO PALOMAS Y DE LA COLONIA AGRÍCOLA LA LIBERTAD, SOLO POR RESUMEN</code> · publicado el miércoles 28-OCT, por ruta (Potosinoticias 2026/10/28) · " + AP + "; día del hallazgo no fijado: " + RET + " · <b>presunta fosa clandestina con restos óseos</b>, por titular y <i>slug</i> (Potosinoticias; Plano Informativo) (🔴 hallazgo de fosa) · búsqueda de la Comisión Estatal de Búsqueda con colectivos, Guardia Civil Estatal y Guardia Nacional, " + RES + " · restos trasladados al Servicio Médico Legal de Rioverde, " + RES + " · <b>número de personas: no publicado</b> — <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · hallazgos similares en la zona en años previos, " + RES + " (Plano Informativo)",
  panel="<b>Posible fosa clandestina con restos óseos</b>: número de víctimas no publicado", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola ruta fechada; día del hallazgo y número de víctimas no publicados; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Potosinoticias (2026/10/28)"], estatus="Pendiente de corroboración", arm=None,
  desl="Ciudad del Maíz y Palomas no figuran en las cinco ediciones previas ni en el índice. Cuerpos hallados: sin cifra, fuera del total numérico."),
 dict(id="ARG-144-007", estado="MX-MEX", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=0, hk=0.8,
  ent="Estado de México", mun="Ecatepec (col. Rústica Xalostoc, inmueble)", dia="PUB. 28-OCT; DÍA DEL HALLAZGO NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL HALLAZGO NO FIJADO",
  title="ESTADO DE MÉXICO · ECATEPEC — HALLAN RESTOS HUMANOS ENTERRADOS Y CUBIERTOS CON CEMENTO EN UN INMUEBLE, EN LA BÚSQUEDA DE UNA MUJER DESAPARECIDA",
  hecho="Ecatepec · <code>COL. RÚSTICA XALOSTOC, INMUEBLE, POR TITULAR (EL MONITOR DEL EDOMEX)</code> · publicado el miércoles 28-OCT, por ruta (El Monitor del Estado de México 2026/10/28, primera publicación; Reporteros en Movimiento 2026/10/28) · " + AP + "; día del hallazgo no fijado: " + RET + " · <b>restos humanos enterrados y cubiertos con cemento</b>, por titular (El Monitor; Excélsior; La Prensa de Coahuila) (🔴 restos humanos en inhumación clandestina) · identidad no confirmada: <b>posibles restos</b>, por titular (Tribuna), de una <b>mujer de 52 años</b> desaparecida, por titular (Quadratín Edomex); vista por última vez el 15-oct, " + RES + "; «cuerpo enterrado con cemento», por titular (TV Azteca) · <b>número de víctimas: no publicado</b> — <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · la detención por este caso es hecho aparte: ARG-144-019",
  panel="<b>Restos humanos bajo cemento</b> en un inmueble: número de víctimas no publicado", inst="FGJEM" + PR, nac="Excélsior · TV Azteca", conf="★★★☆☆",
  campo="día del hallazgo no fijado; identidad no confirmada; FGJEM solo por resumen", I=1, N=2, R=5, A=0,
  fechadas=["El Monitor del Edomex (2026/10/28)", "Reporteros en Movimiento (2026/10/28)", "Tribuna (2026/10/29)", "La Prensa de Coahuila (2026/10/29)", "Sociedad Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Rústica Xalostoc no figura en las cinco ediciones previas ni en el índice. Ecatepec en el índice: ARG-140-REC-003 (Santa María Tulpetlac, 20-oct): otro hecho. Las Vegas Xalostoc (hombre muerto y pareja baleada, noche del 27, solo por resumen): otro hecho, ventana de ARGOS 143, 🟡: visto. Restos sin cifra: fuera del total numérico de cuerpos."),
 dict(id="ARG-144-008", estado="MX-TAM", region="Noreste", color="rojo", impacto="grande", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=0.7,
  ent="Tamaulipas", mun="Matamoros y Río Bravo (varios puntos)", dia="29-OCT, POR RUTA; HORA NO FIJADA",
  title="TAMAULIPAS · MATAMOROS — BLOQUEOS CON VEHÍCULOS DE CARGA EN OCHO PUNTOS TRAS LA DETENCIÓN DE UN OBJETIVO PRIORITARIO; EL ALCALDE PIDE RESGUARDARSE",
  hecho="Matamoros y Río Bravo · <code>OCHO PUNTOS DE MATAMOROS, POR TITULAR; «DIVERSOS PUNTOS» DE RÍO BRAVO, SOLO POR RESUMEN</code> · jueves 29-OCT, por ruta (Heraldo de México 2026/10/29) · " + FR + " · <b>bloqueos en ocho puntos de Matamoros</b>, por titular (ABC Noticias 2026/10/29); «8 bloqueos con tráileres», por titular (Capital México) (🔴 narcobloqueo) · atribuidos a la <b>Vocería de Seguridad de Tamaulipas</b>, " + RES + " · ponchallantas y choferes obligados a bajar, " + RES + " · el <b>alcalde de Matamoros</b> pide a la población resguardarse, por titular (Heraldo de México) · una secundaria retuvo a sus alumnos y se suspendieron clases vespertinas, " + RES + " · vehículos incendiados, heridos o detenidos por los bloqueos: ninguno publicado · la detención que los precede es hecho aparte: ARG-144-015",
  panel="<b>Bloqueos con vehículos de carga</b> en ocho puntos tras una detención", inst="Vocería de Seguridad de Tamaulipas" + PR + " · alcalde de Matamoros" + PT, nac="Heraldo de México · Capital México", conf="★★★☆☆",
  campo="emisor oficial solo por resumen; hora no fijada", I=1, N=2, R=2, A=0,
  fechadas=["Heraldo de México (2026/10/29)", "ABC Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Matamoros en el índice: hechos de otras fechas. Bloqueo de productores en la carretera Victoria–Matamoros (más de 30 horas) e Izúcar de Matamoros (Puebla, transportistas): otros hechos, no se integran. Rescate de 12 secuestrados en Matamoros y Nuevo Laredo (27-oct, La Región): ventana de ARGOS 143, 🟢: visto."),
 dict(id="ARG-144-009", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-29", hora="poco después de las 07:00 (solo por resumen)", mu=0, he=0, cu=1, hk=7,
  ent="Guerrero", mun="Acapulco (col. Emiliano Zapata, calle 15, frente a la parroquia)", dia="29-OCT, POR RUTA; HORA SOLO POR RESUMEN",
  fecha_txt="2026-10-29, por ruta de publicación; hora solo por resumen",
  title="GUERRERO · ACAPULCO — ARROJAN DESDE UN AUTO DOS BOLSAS CON LOS RESTOS DE UNA PERSONA DESMEMBRADA EN LA COLONIA EMILIANO ZAPATA",
  hecho="Acapulco · <code>COL. EMILIANO ZAPATA, CALLE 15, FRENTE A LA PARROQUIA DEL PERPETUO SOCORRO, SOLO POR RESUMEN</code> · publicado el jueves 29-OCT, por ruta (Sociedad Noticias 2026/10/29) · " + FR + " · poco después de las 07:00, " + RES + " · <b>restos de una persona desmembrada en dos bolsas</b>, por titular (Quadratín Guerrero; Meganoticias) (🔴 restos humanos exhibidos en vía pública) · arrojados desde un auto por hombres armados, " + RES + " · víctima no identificada · <b>ningún detenido publicado</b>",
  panel="<b>Restos de una persona desmembrada</b> arrojados en bolsas", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Sociedad Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Calle 15 y la parroquia del Perpetuo Socorro no figuran en las cinco ediciones previas ni en el índice. «Emiliano Zapata» devuelve hallazgos de 2024 y 2025 en Acapulco y uno de Morelos: otros hechos. Cuerpo hallado sin causa de muerte informada por autoridad: en la columna de cuerpos."),
 # ======================= AMARILLOS
 dict(id="ARG-144-010", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-28", hora="contradicha: mañana / ~16:00 (solo por resumen)", mu=1, he=0, cu=0, hk=12,
  ent="Veracruz", mun="Tecolutla (Cañada Rica, límite con Papantla)", dia="28-OCT, POR RUTA; HORA CONTRADICHA",
  title="VERACRUZ · TECOLUTLA — ASESINAN A UN COMERCIANTE DE CÍTRICOS EN UN ASALTO A UNA BÁSCULA EN CAÑADA RICA",
  hecho="Tecolutla · <code>CAÑADA RICA, BÁSCULA DE CÍTRICOS, POR <i>SLUG</i> (INFOVERACRUZ)</code> · miércoles 28-OCT, por ruta (Infoveracruz; Golpe Político 2026/10/28) · " + AP + "; «mañana» o ~16:00, " + RES + ": " + RET + " · <b>1 muerto</b>: comerciante de cítricos, por <i>slug</i> (Infoveracruz) (🟡 homicidio doloso único) · intentó resguardarse en su automóvil, por titular (Gráfico al Día) · asalto, por titular · edad y origen contradichos entre medios; una acompañante herida solo en dos medios, " + RES + ": no se suma · 4 casquillos .38, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Comerciante asesinado en un asalto: <b>1 muerto</b>", inst=SB, nac="N+", conf="★★★☆☆",
  campo="hora contradicha y solo por resumen; ninguna fuente institucional", I=0, N=1, R=9, A=0,
  fechadas=["Infoveracruz (2026/10/28)", "Golpe Político (2026/10/28)", "Gráfico al Día (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tecolutla y Cañada Rica no figuran en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-144-011", estado="MX-ROO", region="Sureste", color="amarillo", impacto="pequeno", fecha="2026-10-28", hora="tarde (solo por resumen)", mu=1, he=1, cu=0, hk=15,
  ent="Quintana Roo", mun="Benito Juárez (Cancún, fracc. Cielo Nuevo)", dia="28-OCT, POR RUTA",
  title="QUINTANA ROO · CANCÚN — ATAQUE ARMADO EN EL FRACCIONAMIENTO CIELO NUEVO: UN MUERTO Y UNA MUJER HERIDA",
  hecho="Cancún · <code>FRACC. CIELO NUEVO; ATAQUE EN LA SM 249 Y CAPTURA EN LA REGIÓN 251, SOLO POR RESUMEN</code> · miércoles 28-OCT, por ruta (Por Esto; Noticaribe 2026/10/28) · tarde, " + RES + " · <b>1 muerto</b>: hombre, por titular (Por Esto; Noticaribe) (🟡 homicidio doloso único) · <b>1 mujer herida</b>, por titular (DRV Noticias; Clic Noticias) · nacionalidad y actividad de la víctima: versión de un medio, no de autoridad: no se reproduce · la detención de tres personas es hecho aparte: ARG-144-016",
  panel="Ataque armado: <b>1 muerto y 1 herida</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=8, A=0,
  fechadas=["Por Esto (2026/10/28)", "Noticaribe (2026/10/28)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cielo Nuevo no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-144-012", estado="MX-MOR", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-28", hora="no fijada", mu=0, he=2, cu=0, hk=0.6,
  ent="Morelos", mun="Cuautla (frente al Tecnológico de Cuautla, límite con Yecapixtla)", dia="PUB. 28-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL HECHO NO FIJADO",
  title="MORELOS · CUAUTLA — BALEAN UNA COMBI DE PASAJEROS FRENTE AL TECNOLÓGICO DE CUAUTLA: EL CHOFER Y UN ESTUDIANTE, HERIDOS",
  hecho="Cuautla · <code>FRENTE AL TECNOLÓGICO DE CUAUTLA, LÍMITE CON YECAPIXTLA; RUTA 9, SOLO POR RESUMEN</code> · publicado el miércoles 28-OCT, por ruta (La Razón 2026/10/28) · " + AP + "; día del hecho no fijado: " + RET + " · <b>ataque a balazos contra una combi</b>, por titular (La Razón; El Universal; Diario de Morelos) · <b>2 heridos</b>: chofer y estudiante, por titular (El Universal; Diario de Morelos); 3, un medio, " + RES + ": <code>CONTRADICHO</code> (🟡 agresión sin muertos) · agresores en motocicleta, " + RES + " · el <b>fiscal de Morelos</b> confirmó los heridos, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Ataque a una combi: <b>2 heridos</b>", inst="Fiscal de Morelos" + PR, nac="La Razón · El Universal", conf="★★★☆☆",
  campo="día del hecho no fijado; declaración del fiscal solo por resumen", I=1, N=2, R=4, A=0,
  fechadas=["La Razón (2026/10/28)", "La Razón (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Tecnológico de Cuautla y la Ruta 9 no figuran en las cinco ediciones previas ni en el índice. Cuautla y Yecapixtla: un solo hecho (misma unidad, mismos heridos). Cuautla, col. Gabriel Tepepa (hombre asesinado ~23:30 del 27, solo por resumen): otro hecho, ventana de ARGOS 143, 🟡: visto."),
 dict(id="ARG-144-013", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=1, hk=0.4,
  ent="Guanajuato", mun="Valle de Santiago (col. Ranchos Unidos)", dia="28-OCT, POR RUTA; HORA NO FIJADA",
  title="GUANAJUATO · VALLE DE SANTIAGO — DESCUBREN EL CUERPO DE UN HOMBRE CON UN DISPARO EN LA CABEZA EN LA COLONIA RANCHOS UNIDOS",
  hecho="Valle de Santiago · <code>COL. RANCHOS UNIDOS, POR <i>SLUG</i> (CORREO)</code> · miércoles 28-OCT, por ruta (Correo 2026/oct/28) · " + AP + "; hora no informada: " + RET + " · <b>1 cuerpo con un disparo en la cabeza</b>, por <i>slug</i> (Correo) (🟡 hallazgo de un cuerpo) · fecha de la muerte no publicada: <code>CAUSA NO INFORMADA POR AUTORIDAD</code> · " + FU + " · <b>ningún detenido publicado</b>",
  panel="Cuerpo hallado con un disparo: <b>1 cuerpo</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; hora no informada; causa no informada por autoridad", I=0, N=0, R=1, A=0,
  fechadas=["Correo (2026/oct/28)"], estatus="Pendiente de corroboración", arm=None,
  desl="Ranchos Unidos no figura en las cinco ediciones previas ni en el índice. Valle de Santiago en el índice: ARG-125-013, ARG-125-020 y ARG-128-REC-005: otros hechos. Col. Morelos de Valle de Santiago (hombre muerto, «tarde del miércoles» solo por resumen, sin ruta fechada): visto."),
 dict(id="ARG-144-014", estado="MX-ROO", region="Sureste", color="amarillo", impacto="pequeno", fecha="2026-10-29", hora="no fijada", mu=1, he=0, cu=0, hk=0.3,
  ent="Quintana Roo", mun="Othón P. Blanco (Chetumal, Nachicocom)", dia="29-OCT, POR RUTA; HORA NO FIJADA",
  title="QUINTANA ROO · CHETUMAL — UN COMANDO ARMADO IRRUMPE EN UNA VIVIENDA DE NACHICOCOM Y ASESINA A UN EXPOLICÍA",
  hecho="Chetumal · <code>NACHICOCOM, VIVIENDA, POR <i>SLUG</i> (POR ESTO)</code> · publicado el jueves 29-OCT, por ruta (Por Esto 2026/10/29) · " + FR + "; «noche del jueves», " + RES + " (Zócalo; Sol Quintana Roo), incoherente con una publicación del 29; «miércoles», " + RES + ": <code>DÍA CONTRADICHO</code> · <b>1 muerto</b>: <b>expolicía</b> estatal, por titular (Por Esto; Zócalo; Sol Quintana Roo) (🟡 homicidio doloso único: la víctima no era servidor público en activo) · comando armado, por titular · <b>ningún detenido publicado</b>",
  panel="Expolicía asesinado en su vivienda: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día contradicho; hora no fijada; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Por Esto (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Nachicocom no figura en las cinco ediciones previas ni en el índice. Si la autoridad acredita que la víctima era servidor público en activo, el hecho sube a 🔴."),
 # ======================= VERDES
 dict(id="ARG-144-015", estado="MX-TAM", region="Noreste", color="verde", impacto="mediano", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=0.7,
  ent="Tamaulipas", mun="Matamoros", dia="29-OCT, POR RUTA; HORA NO FIJADA",
  title="TAMAULIPAS · MATAMOROS — FUERZAS FEDERALES DETIENEN A UN OBJETIVO PRIORITARIO DE LA DELINCUENCIA ORGANIZADA",
  hecho="Matamoros · jueves 29-OCT, por ruta (Heraldo de México 2026/10/29) · " + FR + " · <b>detención de un «objetivo prioritario»</b>, por titular (Heraldo de México: única fuente con esa expresión); «presunto líder criminal», atribuido a la <b>Vocería de Seguridad de Tamaulipas</b>, " + RES + " (Diario del Yaqui) (🟢 detención) · por <b>fuerzas federales</b>, " + RES + " · identidad y delitos: no publicados · <b>1 detenido</b>, deducido del singular del titular; «no se confirmaban personas detenidas», " + RES + " (El Mañana): <code>CONTRADICHO</code> · armamento asegurado: no publicado · los bloqueos posteriores son hecho aparte: ARG-144-008",
  panel="<b>Detención de un objetivo prioritario</b>: 1 detenido, con reserva", inst="Vocería de Seguridad de Tamaulipas" + PR, nac="Heraldo de México", conf="★★☆☆☆",
  campo="detención por titular de una sola fuente; número de detenidos deducido y contradicho", I=1, N=1, R=1, A=0,
  fechadas=["Heraldo de México (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Detención en Reynosa de un «objetivo prioritario» (Yahoo, abril): otro hecho. Detención sin armamento con cifra: fuera del conteo de armamento."),
 dict(id="ARG-144-016", estado="MX-ROO", region="Sureste", color="verde", impacto="pequeno", fecha="2026-10-28", hora="tarde (solo por resumen)", mu=0, he=0, cu=0, hk=15,
  ent="Quintana Roo", mun="Benito Juárez (Cancún, fracc. Cielo Nuevo)", dia="28-OCT, POR RUTA",
  title="QUINTANA ROO · CANCÚN — DETIENEN A TRES PERSONAS TRAS UNA PERSECUCIÓN Y ASEGURAN UN ARMA DE FUEGO, POR EL ATAQUE DE CIELO NUEVO",
  hecho="Cancún · miércoles 28-OCT, por ruta (Noticaribe 2026/10/28, «hay tres detenidos») · tarde, " + RES + " · <b>3 detenidos</b>, por <i>slug</i> (Noticaribe) y titular (Sol Quintana Roo) (🟢 detención) · tras una persecución, " + RES + " · <b>1 arma de fuego</b>, tipo no publicado, " + RES + ": sin fila de armamento · policía de Cancún; puestos a disposición de la FGE, " + RES + " · el ataque es hecho aparte: ARG-144-011",
  panel="<b>3 detenidos</b> tras una persecución", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="arma y corporación solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Noticaribe (2026/10/28)", "Por Esto (2026/10/28)"], estatus="Parcialmente corroborado", arm=None,
  desl="Delito y detención en la misma ventana: dos fichas (ARG-144-011 y esta). El arma existe solo en el resumen del buscador: sin aseguramiento citable, fuera del conteo de armamento."),
 dict(id="ARG-144-017", estado="MX-NLE", region="Noreste", color="verde", impacto="pequeno", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=0, hk=0.6,
  ent="Nuevo León", mun="General Bravo y China", dia="PUB. 28-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DE LOS CATEOS NO FIJADO",
  title="NUEVO LEÓN · GENERAL BRAVO Y CHINA — SIETE CATEOS DEJAN DOS DETENIDOS Y ASEGURAN ARMAS, CARTUCHOS Y DROGA",
  hecho="General Bravo y China · publicado el miércoles 28-OCT, por ruta (MVS; Punto x Punto 2026/10/28) · " + AP + "; «la semana pasada», un medio, " + RES + ": " + RET + " · <b>7 cateos</b>, por titular (El Porvenir; Hora Cero) · <b>2 detenidos</b>, por titular (MVS; Punto x Punto) (🟢 cateos y aseguramiento) · <b>armas</b> y droga, por titular (MVS); 2 armas sin clasificar y cartuchos, " + RES + ": <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · droga, básculas y teléfonos, " + RES + " · FGJE de Nuevo León, por titular de un medio (El Porvenir), sin declaración citada",
  panel="<b>7 cateos</b>: 2 detenidos; armas sin cifra y droga", inst=SB, nac="MVS", conf="★★★☆☆",
  campo="día de los cateos no fijado; ninguna declaración institucional", I=0, N=1, R=5, A=0,
  fechadas=["MVS (2026/10/28)", "Punto x Punto (2026/10/28)"], estatus="Parcialmente corroborado", arm="ARG-144-ARM-001",
  desl="General Bravo y China no figuran en las cinco ediciones previas; ARG-135-ARM-001 («Industrial Bravo»): otro hecho."),
 dict(id="ARG-144-018", estado="MX-CMX", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=0, hk=0.5,
  ent="Ciudad de México", mun="Gustavo A. Madero (col. Lindavista)", dia="PUB. 28-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL CATEO NO FIJADO",
  title="CIUDAD DE MÉXICO · GUSTAVO A. MADERO — CATEO EN LINDAVISTA CONTRA LA FALSIFICACIÓN DE PLACAS: SEIS DETENIDOS, DOS ARMAS Y DROGA",
  hecho="Gustavo A. Madero · <code>COL. LINDAVISTA, POR TITULAR</code> · publicado el miércoles 28-OCT, por ruta (La Silla Rota; Publimetro 2026/10/28) · " + AP + "; día del cateo no fijado: " + RET + " · <b>6 detenidos</b>, por titular (La Silla Rota; Publimetro) (🟢 cateo y detención) · placas falsas y con reporte de robo, por titular; cifras contradichas, " + RES + " · <b>armas</b>, por titular (NX Noticias); 1 corta, 1 larga y cartuchos, " + RES + ": <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · ocho edades listadas en un medio (Crónica), " + RES + ", frente a 6 detenidos · droga, " + RES + " · SSC con la Fiscalía capitalina, SEMAR y GN; «la SSC informó», " + RES + " · altar con presuntos restos óseos: video de un periodista, no confirmado por la autoridad: <code>NO SE INTEGRA</code>",
  panel="<b>Cateo</b>: 6 detenidos; armas sin cifra y placas apócrifas", inst="SSC" + PR, nac="La Silla Rota · Publimetro · TV Azteca", conf="★★★☆☆",
  campo="comunicado de la SSC solo por resumen; día no fijado; número de detenidos con reserva", I=1, N=3, R=4, A=0,
  fechadas=["La Silla Rota (2026/10/28)", "Publimetro (2026/10/28)"], estatus="Parcialmente corroborado", arm="ARG-144-ARM-002",
  desl="Lindavista no figura en las cinco ediciones previas; Gustavo A. Madero en ARGOS 141: otro hecho. Si la autoridad confirma restos humanos en el inmueble, el hecho abre ficha 🔴 aparte."),
 dict(id="ARG-144-019", estado="MX-MEX", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=0, hk=0.8,
  ent="Estado de México", mun="Ecatepec (col. Rústica Xalostoc)", dia="PUB. 28-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DE LA DETENCIÓN NO FIJADO",
  title="ESTADO DE MÉXICO · ECATEPEC — DETIENEN A LA SOBRINA Y A UN HOMBRE POR LA DESAPARICIÓN DE UNA MUJER DE 52 AÑOS",
  hecho="Ecatepec · publicado el miércoles 28-OCT, por ruta (El Monitor del Edomex 2026/10/28) · " + AP + "; día de la detención no fijado: " + RET + " · <b>2 detenidos</b>: sobrina de la víctima y un hombre, por titular (Tribuna; Sociedad Noticias; El Monitor) (🟢 detención) · por <b>desaparición cometida por particulares</b>, con agravantes, " + RES + " · FGJEM; órdenes de aprehensión giradas por un juez, " + RES + " · el hallazgo de los restos es hecho aparte: ARG-144-007",
  panel="<b>2 detenidos</b> por la desaparición de una mujer", inst="FGJEM" + PR, nac="Excélsior · TV Azteca", conf="★★★☆☆",
  campo="día de la detención no fijado; FGJEM solo por resumen", I=1, N=2, R=4, A=0,
  fechadas=["El Monitor del Edomex (2026/10/28)", "Tribuna (2026/10/29)", "Sociedad Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Delito y detención publicados en la misma ventana: dos fichas (ARG-144-007 y esta). Detención sin armamento: fuera del conteo de armamento."),
 dict(id="ARG-144-020", estado="MX-GUA", region="Occidente", color="verde", impacto="pequeno", fecha="2026-10-28", hora="no fijada", mu=0, he=0, cu=0, hk=0.4,
  ent="Guanajuato", mun="Jaral del Progreso (col. Las Flores)", dia="PUB. 28-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL OPERATIVO NO FIJADO",
  title="GUANAJUATO · JARAL DEL PROGRESO — DETIENEN A DOS HOMBRES CON TRES ARMAS LARGAS, EQUIPO TÁCTICO Y UNA CAMIONETA ROBADA",
  hecho="Jaral del Progreso · <code>COL. LAS FLORES, SOLO POR RESUMEN</code> · publicado el miércoles 28-OCT, por ruta (boletín del Gobierno de Guanajuato 2026/10/28) · " + AP + "; día del operativo no fijado: " + RET + " · <b>2 detenidos</b> y <b>3 armas largas</b>, por titular del boletín y de Quadratín Bajío (🟢 detención y aseguramiento) · cartuchos y cargadores sin cifra, " + RES + " · 6 chalecos y 6 cascos, " + RES + " · camioneta con reporte de robo, por titular · Seguridad y Paz de Guanajuato con la Defensa, " + RES + " · <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>: La Silla Rota (2026/10/26) publicó un arsenal asegurado a dos hombres en la misma colonia, ya vinculados a proceso",
  panel="<b>2 detenidos</b> con 3 armas largas <span class=\"muted-note\">(posible duplicidad)</span>", inst="Gobierno de Guanajuato (boletín)" + PT, nac="N+", conf="★★★☆☆",
  campo="posible duplicidad con un aseguramiento del 26-oct; día del operativo no fijado", I=1, N=1, R=1, A=0,
  fechadas=["Gobierno de Guanajuato (2026/10/28)"], estatus="Parcialmente corroborado", arm="ARG-144-ARM-003",
  desl="Jaral del Progreso no figura en las cinco ediciones previas ni en el índice. La Silla Rota 2026/10/26 (misma colonia, dos presuntos integrantes del CSRL, 24 ponchallantas): posible mismo aseguramiento con otra cifra; no arbitrado."),
]

# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-144-REC-001", estado="MX-CMX", region="Centro", fecha="2026-10-28", hora="mañana, «primeras horas» (solo por resumen); una nota publicada a las 08:33 (solo por resumen)", orig="ARGOS 143 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Ciudad de México", mun="Cuauhtémoc (col. Centro, República de Perú y República de Argentina)", dia="28-OCT, POR RUTA",
  title="CIUDAD DE MÉXICO · CENTRO HISTÓRICO — ASESINAN A BALAZOS A DOS HERMANOS EN REPÚBLICA DE PERÚ Y ARGENTINA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 143 — HORA SOLO POR RESUMEN</code> · Cuauhtémoc · <code>CRUCE DE REPÚBLICA DE PERÚ Y REPÚBLICA DE ARGENTINA, COL. CENTRO</code> · miércoles 28-OCT, por ruta (Proceso; Infobae; El Gráfico 2026/10/28) · mañana, «primeras horas», " + RES + "; una nota publicada a las 08:33 —cinco minutos después del cierre de ARGOS 143—, " + RES + ": hecho sin hora fijada, previsiblemente anterior a las 08:28 · <b>2 muertos</b>: dos hermanos, por titular (Proceso) (🔴 homicidio múltiple) · 13 disparos, " + RES + " · agresores en bicicleta eléctrica, por titular (El Universal) · <b>ningún detenido publicado</b> · <code>SI RESULTA POSTERIOR A LAS 08:28 DEL 28, ES HECHO PROPIO DE ARGOS 144</code>",
  panel="<b>Dos hermanos asesinados a balazos</b>: 2 muertos", inst=SB, nac="Proceso · Infobae · El Universal · El Gráfico",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=4, R=1, A=0,
  fechadas=["Proceso (2026/10/28)", "Infobae (2026/10/28)", "El Gráfico (2026/10/28)"],
  desl="República de Perú y Argentina no figuran en las cinco ediciones previas ni en el índice. NO es el doble homicidio de dos hermanos en República de Chile (13-sep): otro hecho. Tlalpan, cuerpo calcinado (27-oct, Infobae, fuente única, sin causa informada): visto."),
 dict(id="ARG-144-REC-002", estado="MX-VER", region="Golfo", fecha="2026-10-28", hora="madrugada, «primeros minutos» del miércoles (solo por resumen)", orig="ARGOS 143 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=1,
  ent="Veracruz", mun="Coatzacoalcos (av. Universidad Veracruzana, frente al Poder Judicial de la Federación)", dia="28-OCT, POR RUTA",
  title="VERACRUZ · COATZACOALCOS — ABANDONAN UNA CABEZA HUMANA CON UN MENSAJE DE AMENAZA FRENTE AL PODER JUDICIAL DE LA FEDERACIÓN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 143 — HORA SOLO POR RESUMEN</code> · Coatzacoalcos · <code>AV. UNIVERSIDAD VERACRUZANA, FRENTE AL PODER JUDICIAL DE LA FEDERACIÓN, POR TITULAR</code> · miércoles 28-OCT, por ruta (La Silla Rota 2026/10/28; Diario del Istmo 20261028; Sociedad Noticias 2026/10/28) · madrugada, " + RES + " (dos resúmenes independientes) · <b>cabeza humana en una mochila</b>, por titular (La Silla Rota; Quinta Fuerza; El Buen Tono); «hielera», por titular (TV Azteca; Avi Veracruz): <code>CONTRADICHO</code> · <b>con mensaje de amenaza</b>, por titular (N+; Telediario) (🔴 restos humanos exhibidos frente a una sede judicial) · contenido del mensaje: no publicado íntegro · víctima no identificada; resto del cuerpo no localizado · <b>ningún detenido publicado</b> · <code>SI RESULTA POSTERIOR A LAS 08:28 DEL 28, ES HECHO PROPIO DE ARGOS 144</code>",
  panel="<b>Cabeza humana con mensaje de amenaza</b> frente al Poder Judicial", inst=SB, nac="N+ · Milenio · TV Azteca · La Silla Rota",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=4, R=7, A=0,
  fechadas=["La Silla Rota (2026/10/28)", "Diario del Istmo (2026/10/28)", "Sociedad Noticias (2026/10/28)"],
  desl="Av. Universidad Veracruzana y el Poder Judicial no figuran en las cinco ediciones previas. Coatzacoalcos en el índice: ARG-134-011, ARG-137-003 y otros: otros hechos. Trabajador de la CMAS (28-oct): muerte no violenta según la Fiscalía, no se integra. Cuerpo hallado sin causa de muerte informada por autoridad."),
 dict(id="ARG-144-REC-003", estado="MX-SIN", region="Noroeste", fecha="2026-10-27", hora="noche, ~22:00-23:00 (solo por resumen)", orig="ARGOS 143 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Sinaloa", mun="Culiacán (fracc. Villas del Real)", dia="27-OCT, SOLO POR RESUMEN",
  fecha_txt="2026-10-27, solo por resumen (publicado el 28)",
  title="SINALOA · CULIACÁN — UN CONVOY ARMADO PRIVA DE LA LIBERTAD A CUATRO JÓVENES EN VILLAS DEL REAL; LA FISCALÍA LOS LOCALIZA CON VIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 143 — HORA SOLO POR RESUMEN</code> · Culiacán · <code>FRACC. VILLAS DEL REAL, POR <i>SLUG</i> (LUZ NOTICIAS)</code> · noche del martes 27-OCT, " + RES + "; publicación del 28, por ruta (Luz Noticias 2026-10-28; El Diario de Chihuahua 2026/oct/28; El Diario del Noroeste 2026/oct/28) · <b>4 jóvenes privados de la libertad</b>, por titular (El Diario de Chihuahua; El Diario del Noroeste); <b>6</b> en la versión inicial, por titular (Extraoficial; Julio Astillero; Azteca Sinaloa): <code>CONTRADICHO</code>; 4, precisión atribuida a la <b>Fiscalía de Sinaloa</b>, " + RES + " (🔴 privación de la libertad múltiple por un convoy armado) · dos menores de edad, por titular (Café Negro Portal) · <b>localizados con vida</b>, por <i>slug</i> (Luz Noticias; Revista Espejo) · circunstancias de la localización: no publicadas · <b>ningún detenido publicado</b>",
  panel="<b>4 jóvenes privados de la libertad</b> por un convoy armado; localizados con vida", inst="Fiscalía de Sinaloa" + PR, nac="El Diario de Chihuahua (Reforma) · Meganoticias",
  conf="★★★☆☆", campo="día y hora solo por resumen; cifra contradicha; Fiscalía solo por resumen", I=1, N=2, R=5, A=0,
  fechadas=["Luz Noticias (2026/10/28)", "El Diario de Chihuahua (2026/10/28)", "El Diario del Noroeste (2026/10/28)", "Revista Espejo (2026/10/29)"],
  desl="Villas del Real de Chihuahua capital (ARG-115-003): otro hecho, otro estado. Culiacán, Villas del Real, ~12-oct (archivo de fuentes de ARGOS 129): sin ficha, otra fecha. La pareja de Colinas del Rey (sin ruta propia ni día): no se integra. «8 secuestrados» (UnoTV) y «12, 14 o 15 asesinados» del 27: balances, no se integran."),
 dict(id="ARG-144-REC-004", estado="MX-SIN", region="Noroeste", fecha="2026-10-27", hora="~06:00-06:30 (solo por resumen)", orig="ARGOS 142 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=1,
  ent="Sinaloa", mun="Mazatlán (Palacio Municipal)", dia="27-OCT, POR RUTA",
  title="SINALOA · MAZATLÁN — ABANDONAN UNA HIELERA CON UNA CABEZA HUMANA FRENTE AL PALACIO MUNICIPAL",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 142 — HORA SOLO POR RESUMEN</code> · Mazatlán · <code>EXTERIOR DEL PALACIO MUNICIPAL, POR TITULAR</code> · martes 27-OCT, por ruta (Central Municipal; Revista Espejo 2026/10/27) · ~06:00-06:30, " + RES + ": anterior a la apertura de ARGOS 143 (08:45 del 27) · <b>hielera con restos humanos</b>, por titular (Revista Espejo); <b>cabeza humana</b>, por titular (Central Municipal; La Razón) (🔴 restos humanos exhibidos frente a una sede de gobierno) · el Ayuntamiento <b>condena</b> el hallazgo, por titular (Revista Espejo) · dos sujetos en una camioneta, según el <b>secretario de Seguridad municipal</b>, " + RES + " · mensaje: contradicho entre medios y el secretario · <b>ningún detenido publicado</b>",
  panel="<b>Cabeza humana en una hielera</b> frente al Palacio Municipal", inst="Ayuntamiento de Mazatlán" + PT + " · secretario de Seguridad municipal" + PR, nac="La Razón · Infobae",
  conf="★★★☆☆", campo="hora solo por resumen; declaración del secretario solo por resumen", I=1, N=2, R=4, A=0,
  fechadas=["Central Municipal (2026/10/27)", "Revista Espejo (2026/10/27)", "La Razón (2026/10/28)", "Infobae (2026/10/28)", "El Diario del Noroeste (2026/10/28)"],
  desl="En ARGOS 143 figuró solo como visto, «día no fijado»: no tuvo ficha. Palacio Municipal en el índice: ARG-126-REC-007 (Santa María Mixtequilla, Oax.) y ARG-99-001 (Palacio de Gobierno de Culiacán): otros hechos. Supervisión de tropas por el secretario de la Defensa en Mazatlán (Infobae 2026/10/28): contexto, no hecho."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-144-ARM-001", ficha="ARG-144-017", estado="MX-NLE", region="Noreste", color="verde", ent="Nuevo León", mun="General Bravo y China",
  fecha="2026-10-28", fecha_txt="pub. 28-oct; día no fijado", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 2], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="FGJE Nuevo León <span class=\"muted-note\">(por titular de un medio)</span>", conf="Bajo",
  nota="cualitativo: «armas» por titular, sin cifra citable (2, solo por resumen); 2 detenidos por titular; ver ARG-144-017",
  fuentes=["MVS (2026/10/28)", "Punto x Punto (2026/10/28)", "El Porvenir (sin fecha en la ruta)"]),
 dict(id="ARG-144-ARM-002", ficha="ARG-144-018", estado="MX-CMX", region="Centro", color="verde", ent="Ciudad de México", mun="Gustavo A. Madero (col. Lindavista)",
  fecha="2026-10-28", fecha_txt="pub. 28-oct; día no fijado", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 6], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="SSC, Fiscalía capitalina, SEMAR y GN <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: «armas» por titular (NX), sin cifra citable (1 corta y 1 larga, solo por resumen); 6 detenidos por titular, con reserva; ver ARG-144-018",
  fuentes=["La Silla Rota (2026/10/28)", "Publimetro (2026/10/28)", "NX Noticias (sin fecha en la ruta)"]),
 dict(id="ARG-144-ARM-003", ficha="ARG-144-020", estado="MX-GUA", region="Occidente", color="verde", ent="Guanajuato", mun="Jaral del Progreso (col. Las Flores)",
  fecha="2026-10-28", fecha_txt="pub. 28-oct; día no fijado", hora="no fijada", c=[0, 3, 0, 0, 0, 0, 0, 0, 0, 2], nd=[0, 2, 3, 4, 5, 6, 7, 8], integra=False,
  corp="Seguridad y Paz de Guanajuato y Defensa <span class=\"muted-note\">(boletín estatal, por titular)</span>", conf="Medio",
  nota="<code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> (La Silla Rota 2026/10/26, misma colonia); ver ARG-144-020",
  fuentes=["Gobierno de Guanajuato (2026/10/28)", "Quadratín Bajío (sin fecha en la ruta)", "N+ (sin fecha en la ruta)"]),
]
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
# sin ningún evento integrable no hay total verificable: todas las categorías n/d
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
HORAS = 27 + 8 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 8] and ND == [True] * 9 + [False], (TOT, ND)
assert cnt == {"rojo": 9, "amarillo": 5, "verde": 6}, cnt
assert cnt_rec == {"rojo": 4, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (12, 4, 2, 2, 0, 2), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,74", DENS
assert sorted(e["id"] for e in E) == [f"ARG-144-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-144-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-28" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-10-28", x["id"]

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
head = head.replace("<title>ARGOS 143 — Reporte Nacional de Seguridad — 2026-10-28</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE CHIAPAS Y AL MECANISMO FEDERAL DE PROTECCIÓN EL ESTADO DE LAS MEDIDAS DE PROTECCIÓN VIGENTES Y LA LÍNEA DE INVESTIGACIÓN</b> (ARG-144-004).
      <br><b>2. SOLICITE A LA VOCERÍA DE SEGURIDAD DE TAMAULIPAS EL REPORTE DE DAÑOS Y LA SITUACIÓN JURÍDICA; VIGILE MATAMOROS Y RÍO BRAVO</b> (ARG-144-008 y -015).
      <br><b>3. SOLICITE A LA COMISIÓN ESTATAL DE BÚSQUEDA DE SAN LUIS POTOSÍ EL NÚMERO DE VÍCTIMAS, LA EXTENSIÓN DEL SITIO Y EL COTEJO GENÉTICO CON LAS FICHAS DE BÚSQUEDA DE LA ZONA</b> (ARG-144-006).
      <br><b>4. SOLICITE A LA FISCALÍA DEL ESTADO DE MÉXICO LA IDENTIFICACIÓN GENÉTICA DE LOS RESTOS Y AUDITE SI LA DESAPARICIÓN DEL 15-OCT ACTIVÓ LA BÚSQUEDA INMEDIATA</b> (ARG-144-007 y -019).
      <br><b>5. SOLICITE A LA FISCALÍA DE SINALOA LAS CIRCUNSTANCIAS DE LA LOCALIZACIÓN Y EL REGISTRO DE LOS VEHÍCULOS PARTICIPANTES</b> (ARG-144-REC-003).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>28-oct 08:28 → 29-oct 11:36 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · dentro de cada color, por fecha y después por hora estimada solo por resumen; hora no fijada, al final de cada fecha · <b>{len(R)} recuperaciones de alto impacto de ventanas anteriores</b>, atenuadas, <b>fuera de todos los totales</b>
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
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b></td><td><b>{tv(0)}</b></td><td><b>{tv(1)}</b></td><td><b>{tv(2)}</b></td><td><b>{tv(4, fmt)}</b></td><td><b>{tv(5)}</b></td><td><b>{tv(6)}</b></td><td><b>{tv(7)}</b></td><td><b>{tv(8)}</b></td><td><b>{tv(9)}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: ninguna arma con cifra citable — dos aseguramientos cualitativos (General Bravo y China; Lindavista) con <b>{DET} detenidos</b> por titular; Jaral del Progreso (3 largas, 2 detenidos), <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>; <code>n/d</code> = no publicado en fuente citable, no ausencia · <b>cuerpos hallados</b>: {CU} con causa no informada por autoridad; Ciudad del Maíz (ARG-144-006) y Ecatepec (ARG-144-007), <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b> (hora o día no fijados frente a las 08:28 del 28): ARG-144-005, -006, -007, -010, -012, -013, -017, -018, -019 y -020 · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos y {CU_REC} cuerpos. <b>Cálculo propio</b>.
    <br><b>Vistos de la ventana de ARGOS 143, fuera de totales</b> (🟢 o 🟡, no se recuperan): Irapuato, col. Benito Juárez (~07:15 del 28, solo por resumen) · rescate de 12 secuestrados en Matamoros y Nuevo Laredo (27-oct) · Culiacán: Díaz Ordaz, Infonavit Barrancos · Mazatlán, Ramón F. Iturbe · Cuautla, Gabriel Tepepa · Ecatepec, Las Vegas Xalostoc · Texmelucan · Puebla, Los Encinos (madrugada del 28, solo por resumen); los aseguramientos vistos, en la página de armamento.
    <br><b>Seguimientos procesales, fuera del semáforo</b>: <b>ARG-143-010 (Rayón)</b>: órdenes notificadas en reclusión, por titular («Ya en prisión, aprehenden a hermanos», Pulso; San Luis Hoy) · <b>ARG-140-020 (Xalapa)</b>: prisión preventiva oficiosa · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[i]) for i in ("ARG-144-001", "ARG-144-002", "ARG-144-004", "ARG-144-008", "ARG-144-003"))
co2 = "\n".join(ficha(byid[i]) for i in ("ARG-144-005", "ARG-144-006", "ARG-144-007", "ARG-144-009"))
co2b = "\n".join(ficha(byid[i]) for i in ("ARG-144-010", "ARG-144-011", "ARG-144-012", "ARG-144-013", "ARG-144-014"))
co2c = "\n".join(ficha(byid[i]) for i in ("ARG-144-015", "ARG-144-016", "ARG-144-017", "ARG-144-018", "ARG-144-019", "ARG-144-020"))
co3 = "\n".join(ficha(rbyid[i], True) for i in ("ARG-144-REC-001", "ARG-144-REC-002", "ARG-144-REC-003", "ARG-144-REC-004"))
assert sorted(re.findall(r'id="(ARG-144-0\d\d)"', co1 + co2 + co2b + co2c)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-144-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), "Lindavista: cifra solo por resumen"),
 tile(1, "Armas largas", tv(1), "Lindavista, solo por resumen; Jaral del Progreso (3), en reserva por posible duplicidad"),
 tile(2, "Sin categoría", tv(2), "General Bravo y China: cifra solo por resumen"),
 tile(3, "Cartuchos", tv(4, fmt), "publicados sin cifra en dos eventos"),
 tile(4, "Cargadores", tv(5), NI),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: dos eventos cualitativos"),
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
    <div class="map-caption">Aseguramientos cualitativos: Nuevo León y Ciudad de México; Jaral del Progreso, en reserva.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> — ningún aseguramiento con cifra publicada y día fijado entre el 27-oct 08:45 y el 28-oct 08:28</td></tr>'
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
    <b>Lectura regional</b>: ninguna región con arma de cifra citable; detenidos en aseguramiento: Noreste 2 · Centro 6. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: General Bravo y China (ARG-144-ARM-001) y Lindavista (ARG-144-ARM-002): «armas» por titular, cifras solo por resumen · Cancún (ARG-144-016): un arma solo por resumen, sin fila · Matamoros (ARG-144-015): armamento no publicado.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>Tuxtepec, Oax.</b> («El Semáforo»; Semar, SSPC y FGR, publicado el 28): armas y granadas sin cifra, {RES}; el boletín federal de acciones del 27 registra un cateo en Tuxtepec con 2 detenidos: <code>POSIBLE MISMO OPERATIVO — DÍA NO FIJADO</code>, ventana de ARGOS 143 · <b>boletín federal del 27-oct</b> (ventana de ARGOS 143; solo por republicadores, misma fuente): Cocula, Gro. (4 cargadores, 115 cartuchos), Sinaloa (1 ametralladora, 530 cartuchos), Huajicori, Nay. (1 larga, cargadores y cartuchos), todo {RES} · <b>Alfredo V. Bonfil, Culiacán</b> (Marina; 3 largas, 3 cargadores, 46 cartuchos, {RES}): <code>POSIBLE MISMO HECHO</code> que Guasave, «Chuy» González (26-oct), visto en ARGOS 143; ventana de ARGOS 142 · <b>Xochitlán de las Flores, Hgo.</b> (operativo del 27, Síntesis 2026/10/27; 1 corta, 1 larga, 1 cargador, {RES}; 3 detenidos) · <b>agregado de la SSP de Veracruz</b> (operativos del 26 y 27, publicado el 28: 3 largas, 1 corta, 38 detenidos, {RES}) · <b>Hermosillo, 5 de Mayo</b> (27-oct ~23:20, {RES}; «aseguran un arma de fuego», por titular de Proyecto Puente 2026/10/28; 1 detenido).
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
      <tr><td><b>Nuevo León</b><br>Doctor Arroyo</td><td>Homicidio simple (San Ignacio de Torres, marzo de 2025, {RES}); <b>1 sentenciado</b>, Edgar «N», {RES} · <b>nuevo en ARGOS 144</b></td><td><b>15 años</b>, por titular (MVS 2026/10/28); reparación sin monto: <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code></td><td>FGJE Nuevo León <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · boletín no localizado en el dominio; firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>sin municipio publicado</td><td>Abuso contra una menor; segunda instancia <b>revoca una absolución</b>, por titular · <b>nuevo en ARGOS 144</b></td><td><b>40 años</b>, por titular (MVS 2026/10/28)</td><td>Tribunal de alzada <span class="muted-note">(por titular)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · solo titular; sin campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Puebla</b><br>Huejotzingo</td><td>Feminicidio de su pareja embarazada («esposa» en otros titulares: <code>CONTRADICHO</code>); <b>1 sentenciado</b>, expolicía, por titular · <b>nuevo en ARGOS 144</b></td><td><b>55 años</b>, por titular (Heraldo de Puebla; Retodiario 2026/10/29)</td><td>FGE Puebla <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín en <code>fiscalia.puebla.gob.mx</code>; día del fallo no fijado</td><td>Bajo</td></tr>
      <tr><td><b>Estado de México</b><br>Ecatepec</td><td>Homicidio y homicidio en grado de tentativa; <b>1 sentenciada</b>, por titular · <b>nuevo en ARGOS 144</b></td><td><b>68 años</b>, por titular (Línea por Línea 2026/10/28)</td><td>FGJEM <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · fuente única; no es el caso de Fresnillo</td><td>No confirmado</td></tr>
      <tr><td><b>Tabasco</b><br>Tenosique</td><td>Armas y granadas; <b>1 sentenciado</b>, por titular · <b>nuevo en ARGOS 144</b></td><td>No publicada en titular</td><td>FGR <span class="muted-note">(informado el 28, solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · comunicado no localizado; sin fecha en la ruta</td><td>No confirmado</td></tr>
      <tr><td><b>Baja California</b><br>Tijuana</td><td>Robo con violencia; procedimiento abreviado, por titular · <b>nuevo en ARGOS 144</b></td><td><b>más de 3 años</b>, por titular (Uniradio); 3 años 6 meses, {RES}</td><td>FGE Baja California <span class="muted-note">(por titular)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin fecha en la ruta; sin campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Zacatecas</b><br>Fresnillo</td><td>Homicidio calificado, tentativa y daño doloso; Juan Manuel «N» · <b>candidato de ARGOS 143, sin cambio</b></td><td><b>68 años</b>, por titular (ECOdiario); 68 años 8 meses, {RES}</td><td>FGJ Zacatecas <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · boletín no localizado; publicación anterior a esta ventana (ya listada por ARGOS 143)</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Triple feminicidio; fallo condenatorio publicado el 9-oct · <b>candidato de ARGOS 140 a 143</b></td><td><b>Sin pena</b>: la audiencia de individualización del 28-oct entró en receso por un corte de energía y continúa el 5-nov, {RES}; penas de 40 a 90 años: proyección de los abogados de las víctimas, no resolución</td><td>Tribunal de Enjuiciamiento <span class="muted-note">(por medios)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>procuraduria.hidalgo.gob.mx</code> sin boletín indexado</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Ramos Arizpe</td><td>Transporte de metanfetamina · <b>candidato de ARGOS 141 a 143, sin cambio</b></td><td>«más de 7 años», por titular (El Siglo de Torreón)</td><td>FGR</td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · dominio estatal sin páginas</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGR Nayarit, Tepic (El Jicote), 15 años, por titular (Argonmexico 2026/10/26); meses adicionales: <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · FGE Querétaro (5, 6, 8 y 22-oct, por ruta) · FGE Jalisco, comunicado 1939 (19-oct) · FGE Colima, boletín 4978 (15-oct) · Tamaulipas FGJE-412 (26-oct) · Ensenada, 158 años 9 meses (individualización del 16-oct) · Nuevo León, 155 años (13-oct). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida: listado de <code>fgr.org.mx</code> sin comunicado de la ventana: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>15 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, BCS, Dgo · SLP, Zac, NL, Tamps · Jal, Col, Mich · Pue, Qro, Hgo · Ver, Tab · <b>de ellas, 2 solo devolvieron páginas estadísticas o normativas</b>: NL, Hgo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>2</b>: Son · Coah · <b>dominio de la fiscalía no confirmado</b>: <b>1</b>, Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>14</b>: Chih, Sin · Nay, Ags, Gto · CDMX, Edomex, Mor, Tlax · Chis, Oax, Gro, Yuc, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 29-oct 11:36: código <code>000</code> · <b>dominio hallado en esta edición</b>: <code>spsc.campeche.gob.mx</code> (SSP de Campeche)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 22 de 32 con consulta propia por entidad</b> (de ellas, <b>5 solo por topónimo de hechos hallados</b>: CDMX, Mor, Pue, Tlax, Gro) · <b>10 solo por consulta regional amplia</b>: BCS · NL, Zac, Coah · Hgo, Qro · Oax, Camp, Yuc, QRoo · <b>Jal, Col, Nay, Ags y Dgo, con consulta propia</b> · <b>armamento: 16 de 32 por dominio oficial</b> —BC · SLP, Tamps · Col, Mich, Gto (boletín del gobierno estatal) · Edomex, Mor, Hgo, Qro · Ver, Tab · Gro, Yuc, QRoo, Chis—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> salvo Gto (Jaral del Progreso) · dominio sin páginas: Son, Coah, Oax · <code>NO REVISADA</code> (13): BCS, Chih, Sin, Dgo · NL, Zac · Jal, Nay, Ags · CDMX, Pue, Tlax · Camp</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 27-oct</b>: publicadas solo por republicadores (Milenio, RED113): misma fuente, sin indexar en <code>gob.mx</code>; ventana de ARGOS 143 · <b>acciones del 28-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título (al arrancar la ola y a las 13:39) · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code> · Semar: por medios</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 29-OCT 11:36: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Nueve rojos propios en {len(ENT_ROJO)} entidades</b> (cálculo propio): tres contra una autoridad, un servidor público o una persona defensora (Son, Mich, Chis), un narcobloqueo (Tamps), dos homicidios múltiples (Gto) y tres hallazgos de fosa o restos (SLP, Edomex, Gro): <b>incremento del riesgo nacional acreditado</b> frente a ARGOS 143.
      <br><b>2.</b> <b>Violencia operativa</b>: cinco amarillos —tres homicidios dolosos únicos, una agresión con dos heridos y un cuerpo hallado— en cuatro entidades (cálculo propio).
      <br><b>3.</b> <b>Guanajuato</b>: cuatro de los veinte hechos propios, dos de ellos rojos (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: seis verdes, uno con posible duplicidad (Jaral del Progreso); ninguna sentencia integrable (cálculo propio; totales, en el panorama).
      <br><b>5.</b> <code>DIEZ DE VEINTE HECHOS CON CLÁUSULA DE RETIRO Y CUATRO ROJOS RECUPERADOS DE ARGOS 142 Y 143; VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 143 SIN NORMALIZAR POR HORA. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. TRES AGENTES DE CORPORACIONES ESTATALES MUERTOS EN TRES ATAQUES ENTRE EL 26 Y EL 28-OCT (DOS EL 26), EN TRES ESTADOS</b> (cálculo propio; desarrolla el dato de los dos ataques a agentes de la Conclusión 5 de ARGOS 142): ARG-142-001 (Tecate, agente estatal en patrullaje), ARG-142-003 (Tehuacán, agente de la FGE) y ARG-144-001 (Magdalena de Kino, agente de la AMIC dentro de su sede); vínculo entre ellos no acreditado. Línea: <b>solicitar a las fiscalías de Baja California, Puebla y Sonora el cotejo balístico entre los tres hechos y auditar la protección de las sedes ministeriales</b>.
      <br><b>2. INDAPARAPEO: SEGUNDO ATAQUE EN CINCO DÍAS</b> (cálculo propio, 23 y 28-oct): ARG-140-016 (disparos contra una base de seguridad, sin lesionados) y ARG-144-002 (regidor y su esposa asesinados); vínculo no acreditado. Línea: <b>solicitar a la Fiscalía de Michoacán el cotejo de los casquillos de ambos hechos y vigilar la comunidad El Triunfo</b>.
      <br><b>3. RESTOS HUMANOS EXHIBIDOS ANTE SEDES DE AUTORIDAD: DOS EN VEINTICUATRO HORAS, EN DOS ESTADOS</b> (cálculo propio, 27 y 28-oct): ARG-144-REC-004 (Mazatlán, Palacio Municipal; mensaje contradicho) y ARG-144-REC-002 (Coatzacoalcos, Poder Judicial de la Federación; mensaje de amenaza por titular); ARG-144-009 (Acapulco, restos arrojados en la vía pública el 29). Línea: <b>solicitar a las fiscalías de Sinaloa y Veracruz el texto íntegro de los mensajes y la identificación genética; vigilar sedes municipales y judiciales</b>.
      <br><b>4. ACÁMBARO: TERCER HOMICIDIO MÚLTIPLE EN DIEZ DÍAS, SIETE MUERTOS</b> (cálculo propio, 19 al 28-oct; desarrolla la Conclusión 1 de ARGOS 143): ARG-143-REC-003 (2), ARG-142-004 (2) y ARG-144-003 (3, con escopeta; riña por titular); vínculo no acreditado. Línea: <b>solicitar a la Fiscalía de Guanajuato el cotejo balístico de los tres hechos</b>.
      <br><b>5. IRAPUATO: CUATRO HECHOS CON VÍCTIMAS EN EL ÍNDICE EN QUINCE DÍAS, SIETE MUERTOS</b> (cálculo propio, 14 al 28-oct): ARG-133-010, ARG-134-REC-001, ARG-140-014 y ARG-144-005 (este, con cláusula de retiro); más un homicidio en la col. Benito Juárez el 28, visto de la ventana de ARGOS 143; vínculo no acreditado. Línea: <b>solicitar a la Fiscalía de Guanajuato el cotejo balístico del ataque de la col. Azteca con ARG-140-014 y con el de la col. Benito Juárez</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>fgr.org.mx</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b> Los ARG-ID de ediciones previas citados en las conclusiones, cotejados contra el índice de ARG-ID.
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: ATAQUES A AUTORIDADES, SERVIDORES PÚBLICOS Y DEFENSORES; NARCOBLOQUEO; HOMICIDIO MÚLTIPLE", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: HOMICIDIO MÚLTIPLE, FOSA Y RESTOS HUMANOS", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA: VERACRUZ, QUINTANA ROO, MORELOS Y GUANAJUATO", co2b)
 + page("CRIMEN ORGANIZADO (IV) — ACCIONES INSTITUCIONALES", co2c)
 + page("CRIMEN ORGANIZADO (V) — ALTO IMPACTO DE VENTANAS ANTERIORES: ARGOS 143 Y ARGOS 142", co3)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana toca dos fechas de calendario (28 y 29-oct); la plantilla de 143 ya trae 2
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
