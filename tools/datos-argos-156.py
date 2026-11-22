# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 156.
Uso: python3 tools/datos-argos-156.py <plantilla ARGOS 155> <salida>
Ventana larga: 19-nov 18:40 → 22-nov 09:34 CDMX (62 h 54 min; jue 19 · vie 20 · sáb 21 · dom 22). Archivo: argos-2026-11-22.html.
La hora de «Consulta» se fija al cierre de procedencia-cifras R2 con la variable ARGOS_CONSULTA (HH:MM)."""
import sys, re, json, os, html as H

NUM, FECHA, HORA = "156", "2026-11-22", "09:34"
CONSULTA = "2026-11-22, última búsqueda " + os.environ.get("ARGOS_CONSULTA", "__CONSULTA__")
DUR = "62 h 54 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 18:40 DEL 19, ES DE LA VENTANA DE ARGOS 155 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
PUB = "Publicado el día de apertura sin hora por fragmento: se integra en esta edición, la primera que lo ve."
TM = " <span class=\"muted-note\">(por titular de medio)</span>"
QNI = "<code>QUIÉN INICIÓ NO DETERMINADO</code>"
CND = "<code>CANTIDAD NO DETERMINADA</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano). Agresores abatidos: fuera de mu.
E = [
 # ======================= ROJOS
 dict(id="ARG-156-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-20", hora="noche (solo por resumen)", mu=4, he=0, cu=0, hk=21,
  ent="Sinaloa", mun="Guasave", dia="VIE 20-NOV, POR RUTA",
  fecha_txt="viernes 20-nov, por ruta; noche, solo por resumen",
  title="SINALOA · GUASAVE — ATACAN A FUERZAS FEDERALES DURANTE LA CAPTURA DE «EL CHAPO ISIDRO»: CUATRO MILITARES MUERTOS",
  hecho="Guasave · viernes 20-NOV, por ruta (La Jornada 2026/11/20: «Sinaloa: reportan enfrentamientos y quema de vehículos en Guasave tras ataque a fuerzas federales»; Proceso 2026/11/20: «Ataque armado contra fuerzas federales desata operativo en Guasave…») · noche, " + RES + " · <b>4 militares muertos</b>, por titular (Proceso 2026/11/21: «Cuatro soldados murieron en operativo contra \"El Chapo Isidro\"»; Yahoo Noticias: «…deja cuatro militares muertos, siete agresores abatidos y ocho detenidos») (🔴 muerte de personal de las fuerzas de seguridad) · <b>7 agresores abatidos</b>, por titular: fuera del recuento de muertos por agresión · Defensa, Fuerzas Especiales y GN; saldo de la Defensa del sábado 21, por titular de medio (UnoTV: «Chapo Isidro: Defensa confirma 11 muertos y 8 detenidos tras operativo en Guasave») · «emboscada», por titular (Excélsior: «Emboscada en Guasave destaca en reporte del Gabinete de Seguridad»), frente a «resistencia armada» a la captura, " + RES + ": " + QNI + "; el color lo fija la muerte de personal · militares en traslado de refuerzo, " + RES + " · armamento asegurado (fusil Barrett, lanzagranadas, explosivos), " + RES + ": " + CND,
  panel="<b>Ataque a fuerzas federales: 4 militares muertos</b>", inst="Defensa (por titular de medio)", nac="Proceso · La Jornada · UnoTV · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen; quién inició no determinado; saldo de la Defensa solo por titular de medio", I=1, N=5, R=2, A=0,
  fechadas=["La Jornada (2026/11/20)", "Proceso (2026/11/20)", "ADN40 (2026-11-20)", "Proceso (2026/11/21)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armamento sin cantidad publicada: evento cualitativo",
  desl="Guasave figura por ARG-91-001 (El Burrión, agosto): otro hecho. Captura: ficha aparte (ARG-156-015); bloqueos: ficha aparte (ARG-156-002); cuerpos de Mojolo: ficha aparte (ARG-156-009), vínculo no acreditado. «Suman 11 muertos» (Noroeste; Luz Noticias 2026-11-21): recuento de medios, no se integra; las 11 muertes de la Defensa son 4 militares y 7 agresores."),
 dict(id="ARG-156-002", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-20", hora="noche (solo por resumen)", mu=0, he=0, cu=0, hk=22,
  ent="Sinaloa", mun="Guasave (Ahome, Salvador Alvarado, Mocorito y Navolato, solo por resumen)", dia="VIE 20-NOV, POR RUTA",
  fecha_txt="viernes 20-nov por la noche, por ruta; publicación también el sábado 21, por ruta",
  title="SINALOA · GUASAVE — BLOQUEOS Y QUEMA DE VEHÍCULOS TRAS LA CAPTURA DE «EL CHAPO ISIDRO»",
  hecho="Guasave · viernes 20-NOV por la noche, por ruta (ADN40 2026-11-20: «Enfrentamiento en Guasave, Sinaloa: reportan disparos, vehículos incendiados y helicópteros»; La Jornada 2026/11/20) · publicación sábado 21-NOV, por ruta (ABC Noticias 2026/11/21: «Captura de \"El Chapo Isidro\" desata balacera y quema de vehículos en Guasave») · <b>bloqueos y quema de vehículos</b>, por titular (Excélsior: «Enfrentamiento, bloqueos y quema de vehículos desatan alerta en Guasave, Sinaloa») (🔴 narcobloqueo y quema de vehículos) · número de vehículos: no publicado · Ahome (tráileres incendiados en Los Mochis), Salvador Alvarado, Mocorito y Navolato, " + RES + ": <code>MUNICIPIOS NO FIJADOS POR TITULAR</code> · Gobierno de Sinaloa: Guasave «bajo control», por titular (La Razón 2026/11/21: «Guasave está 'bajo control' tras bloqueos por captura de 'El Chapo Isidro', asegura Gobierno de Sinaloa») · víctimas: no informadas · " + NOD,
  panel="<b>Bloqueos y quema de vehículos</b>", inst="Gobierno de Sinaloa (por titular de medio)", nac="Excélsior · La Jornada · ABC Noticias · La Razón", conf="★★★☆☆",
  campo="número de vehículos no publicado; municipios distintos de Guasave solo por resumen; declaración estatal solo por titular de medio", I=1, N=4, R=0, A=0,
  fechadas=["ADN40 (2026-11-20)", "La Jornada (2026/11/20)", "ABC Noticias (2026/11/21)", "La Razón (2026/11/21)"], estatus="Parcialmente corroborado", arm=None,
  desl="Mismo episodio que ARG-156-001; ficha aparte por tipo de hecho. UnoTV («Confirman ataque contra fuerzas federales en Guasave; balaceras se extienden a otros municipios»): el titular no nombra municipios. Poza Rica (ARG-154-007): otro hecho, otra entidad."),
 dict(id="ARG-156-003", estado="MX-MEX", region="Centro", color="rojo", impacto="grande", fecha="2026-11-19", hora="no fijada; tarde o noche (solo por resumen)", mu=1, he=0, cu=0, hk=19,
  ent="Estado de México", mun="Nopaltepec (San Felipe Teotitlán)", dia="JUE 19-NOV, POR RUTA",
  fecha_txt="jueves 19-nov, por ruta; hora no fijada; tarde o noche, solo por resumen",
  title="ESTADO DE MÉXICO · NOPALTEPEC — ATACAN A AGENTES DE LA FGR EN SAN FELIPE TEOTITLÁN",
  hecho="Nopaltepec · <code>SAN FELIPE TEOTITLÁN</code>, por titular · jueves 19-NOV, por ruta (Heraldo de México Edomex 2026/11/19: «Ataque armado contra dos agentes de la FGR deja ambos sin vida en Nopaltepec») · hora no fijada; tarde o noche, " + RES + " · " + AP + " · " + RET + " · agentes de la FGR, Subsede Texcoco, " + RES + " · <b>2 agentes muertos</b>, por titular (Heraldo; La Prensa: «Ataque armado contra agentes de la FGR deja dos muertos en Nopaltepec»; Quadratín Edomex: «Asesinan a dos agentes de la FGR tras emboscada en Nopaltepec»), frente a <b>1 muerto y 1 herido</b>, por titular (La Jornada Estado de México: «Ataque armado contra agentes de la FGR en Nopaltepec deja una persona sin vida y un herido»; Digitalmex): <code>SALDO CONTRADICHO — SE CUENTA 1</code> (🔴 víctima autoridad) · «emboscada», por titular (Quadratín), frente a persecución de presuntos huachicoleros, por titular (Digitalmex): " + QNI + " · línea de huachicol, por titular (Milenio: «Huachicol, línea por asesinato de agentes de FGR en Nopaltepec») · ninguna declaración nombrada de la FGR ni de la FGJEM · " + NOD,
  panel="<b>Ataque a agentes federales</b>: 1 o 2 muertos", inst=SB, nac="Milenio · La Jornada", conf="★★★☆☆",
  campo="hora no fijada frente a la apertura; saldo contradicho; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["Heraldo de México Edomex (2026/11/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Nopaltepec figura por ARG-106-007 (detenidos de «Los Cerdos», agosto): otro hecho. " + PUB + " Identidades: no se reproducen."),
 dict(id="ARG-156-004", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-19", hora="noche, ~21:20 (solo por resumen)", mu=2, he=0, cu=0, hk=21,
  ent="Guanajuato", mun="Pueblo Nuevo (carretera a Huanímaro)", dia="JUE 19-NOV, POR RESUMEN",
  fecha_txt="publicación viernes 20-nov, por ruta; noche del jueves 19, ~21:20, DÍA SOLO POR RESUMEN",
  title="GUANAJUATO · PUEBLO NUEVO — EMBOSCAN Y ASESINAN AL DIRECTOR DE LA POLICÍA MUNICIPAL Y A SU ESCOLTA",
  hecho="Pueblo Nuevo, Gto. · carretera Pueblo Nuevo–Huanímaro, " + RES + " · noche del jueves 19-NOV, ~21:20, " + DSR + " · publicación viernes 20-NOV, por ruta (La Silla Rota 2026/11/20: «Emboscan y asesinan al director de Policía de Pueblo Nuevo»; La Jornada 2026/11/20: «Matan a balazos al director de la policía de Pueblo Nuevo, Guanajuato»; Proceso 2026/11/20) · " + RET + " · <b>2 policías muertos</b>, el director de la Policía Municipal y su escolta, por titular (El Universal: «Tras ataque, muere escolta del director de policía de Pueblo Nuevo; Fiscalía de Guanajuato investiga el hecho»); primer parte: escolta herido, por titular (El Universal) (🔴 víctimas autoridad) · «emboscada», por titular (La Silla Rota) · momento del deceso del escolta contradicho, " + RES + " · ninguna declaración nombrada de la FGE · " + NOD,
  panel="<b>Mando policial municipal y escolta asesinados</b>", inst=SB, nac="Infobae · Proceso · La Jornada · El Universal", conf="★★★☆☆",
  campo="día y hora solo por resumen; ninguna fuente institucional", I=0, N=4, R=4, A=0,
  fechadas=["Infobae (2026/11/20)", "Proceso (2026/11/20)", "La Jornada (2026/11/20)", "La Silla Rota (2026/11/20)", "Correo (2026/nov/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="No figura en el cartelón de ARGOS 155 (cierre a las 18:40 del 19). Pueblo Nuevo de Mazatlán (ARG-152-005): homónimo. «Guanajuato suma 24 policías asesinados» (La Nigua) y «cuatro policías en una semana» (Proceso): recuentos de medios, no se integran. Identidades: no se reproducen."),
 dict(id="ARG-156-005", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-20", hora="madrugada (solo por resumen)", mu=2, he=1, cu=0, hk=3,
  ent="Sinaloa", mun="Escuinapa (carretera federal 15, Palmillas–La Concha)", dia="VIE 20-NOV, POR RUTA",
  fecha_txt="viernes 20-nov, por ruta; madrugada, solo por resumen",
  title="SINALOA · ESCUINAPA — ATACAN A UNA FAMILIA EN LA CARRETERA FEDERAL 15: MUEREN UN NIÑO DE SEIS AÑOS Y UNA MUJER EMBARAZADA",
  hecho="Escuinapa · <code>CARRETERA FEDERAL 15, TRAMO PALMILLAS–LA CONCHA</code>, por titular (Sinaloahoy: «Ataque en Palmillas deja tres víctimas de una familia y un lesionado trasladado a Tepic») · viernes 20-NOV, por ruta (La Silla Rota 2026/11/20: «Nayarit pide blindar frontera con Sinaloa; matan a niño y a embarazada»; La Jornada 2026/11/20: «Asesinan a menor y mujer embarazada en límites de Nayarit y Sinaloa») · madrugada, " + RES + " · <b>2 muertos</b>, un niño de 6 años y una mujer embarazada, por titular (Noroeste: «Una mujer embarazada y un niño de 6 años mueren tras ataque a balazos al sur de Escuinapa»); «3 muertos» contando el producto de la gestación, por titular (Los Noticieristas) · <b>1 herido</b>, por titular (Sinaloahoy); un segundo herido, " + RES + " (🔴 homicidio múltiple) · familia de Nayarit en tránsito de Mazatlán a Tepic; cierre del paso por hombres armados, " + RES + " · la víctima sería militar, por titular de un medio (La Nigua): no confirmado · Nayarit pide reforzar la vigilancia del límite, por titular (La Silla Rota) · " + NOD,
  panel="<b>Familia atacada en carretera</b>: un niño y una mujer embarazada muertos", inst=SB, nac="La Jornada · La Silla Rota", conf="★★★☆☆",
  campo="hora solo por resumen; heridos contradichos; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["La Silla Rota (2026/11/20)", "La Jornada (2026/11/20)", "El Diario de Chihuahua (2026/nov/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="Escuinapa figura por ARG-132-REC-005 y ARG-133-011 (col. Pueblo Nuevo, octubre): otros hechos. Acaponeta, Nay. (ARG-153-002): otro hecho. Identidades: no se reproducen."),
 dict(id="ARG-156-006", estado="MX-PUE", region="Centro", color="rojo", impacto="grande", fecha="2026-11-21", hora="tarde, ~16:30 a ~17:00 (solo por resumen)", mu=2, he=0, cu=0, hk=17,
  ent="Puebla", mun="Lomas de Angelópolis III (San Andrés Cholula u Ocoyucan)", dia="SÁB 21-NOV, POR RUTA",
  fecha_txt="sábado 21-nov, por ruta; tarde, ~16:30 a ~17:00, solo por resumen",
  title="PUEBLA · LOMAS DE ANGELÓPOLIS — ASESINAN A DOS HOMBRES EN UN ATAQUE ARMADO",
  hecho="Lomas de Angelópolis III · municipio: San Andrés Cholula, por titular (Heraldo de México 2026/11/21: «Ataque armado deja dos muertos en Cholula»), u Ocoyucan, " + RES + ": <code>MUNICIPIO NO FIJADO</code> · sábado 21-NOV, por ruta (Heraldo de México; El Financiero 2026/11/21; Lo de Hoy 2026/11/21) · tarde, ~16:30 a ~17:00, " + RES + " · <b>2 hombres muertos</b>, por titular (Puebla Ahora: «Asesinan a dos hombres en Lomas de Angelópolis III; FGE investiga ataque armado») (🔴 homicidio múltiple) · una víctima sería familiar de un capo y la otra su escolta, por titular (El Financiero: «Matan a presunto sobrino de Caro Quintero en Lomas de Angelópolis, Puebla; asesinan también a su escolta»; Infobae 2026/11/22): <code>IDENTIDAD NO CONFIRMADA POR AUTORIDAD</code> · arma calibre .556 en el lugar, " + RES + " · " + NOD,
  panel="<b>Doble homicidio</b> en fraccionamiento residencial", inst=SB, nac="El Financiero · Infobae · Heraldo de México · La Jornada", conf="★★★☆☆",
  campo="hora y municipio no fijados; identidad no confirmada; ninguna fuente institucional", I=0, N=5, R=2, A=0,
  fechadas=["Heraldo de México (2026/11/21)", "El Financiero (2026/11/21)", "Lo de Hoy (2026/11/21)", "Infobae (2026/11/22)", "La Jornada (2026/11/22)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lomas de Angelópolis figura por ARG-115-002 (detenciones, septiembre): otro hecho. Nombres: no se reproducen."),
 dict(id="ARG-156-007", estado="MX-CHH", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-21", hora="no fijada; «anoche», por titular del 22", mu=2, he=0, cu=0, hk=20,
  ent="Chihuahua", mun="Ciudad Juárez (col. Altavista)", dia="SÁB 21-NOV, POR RUTA",
  fecha_txt="sábado 21-nov, por ruta y por titular del 22 («anoche»); hora no fijada",
  title="CHIHUAHUA · CIUDAD JUÁREZ — ASESINAN A DOS MUJERES DENTRO DE UNA CAMIONETA EN EL ESTACIONAMIENTO DE UN SUPERMERCADO DE LA ALTAVISTA",
  hecho="Ciudad Juárez · <code>COL. ALTAVISTA, ESTACIONAMIENTO DE SUPERMERCADO</code>, por titular · sábado 21-NOV, por ruta (El Diario de Juárez 2026/nov/21: «Abaten a dos mujeres en estacionamiento del S-Mart Altavista»; Somos Juárez 2026/11/21) y por titular del 22 (El Diario de Juárez 2026/nov/22: «Dispararon al menos 17 veces contra las dos mujeres asesinadas anoche en Jeep») · hora no fijada · <b>2 mujeres muertas</b>, por titular (N+: «Asesinan a Balazos a 2 Mujeres en Estacionamiento de Supermercado en Ciudad Juárez») (🔴 homicidio múltiple) · 17 casquillos percutidos, por titular (El Diario de Juárez 2026/nov/22: «Recabaron 17 casquillos percutidos tras ejecución de mujeres») · modelo de la camioneta contradicho · aseguramiento de un vehículo de los agresores, " + RES + " · " + NOD,
  panel="<b>Doble homicidio de mujeres</b>", inst=SB, nac="N+", conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["El Diario de Juárez (2026/nov/21)", "El Diario de Juárez (2026/nov/22)", "Somos Juárez (2026/11/21)"], estatus="Parcialmente corroborado", arm=None,
  desl="Altavista no figura en los cartelones de 152 a 155. Ciudad Juárez, ataque a federales del 11-nov: otro hecho (seguimiento). Identidades: no se reproducen."),
 dict(id="ARG-156-008", estado="MX-CHH", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-21", hora="no fijada", mu=0, he=0, cu=2, hk=12,
  ent="Chihuahua", mun="Ciudad Juárez (col. Manuel Valdez)", dia="SÁB 21-NOV, POR RUTA",
  fecha_txt="sábado 21-nov, por ruta; hora no fijada",
  title="CHIHUAHUA · CIUDAD JUÁREZ — HALLAN DOS CUERPOS ENTERRADOS EN UNA VIVIENDA DE LA COLONIA MANUEL VALDEZ",
  hecho="Ciudad Juárez · <code>COL. MANUEL VALDEZ, VIVIENDA</code>, por titular · sábado 21-NOV, por ruta (Circuito Frontera 2026/11/21: «Hallan dos cuerpos enterrados en una vivienda de la colonia Manuel Valdez») · hora no fijada · <b>2 cuerpos inhumados clandestinamente</b>, por titular (El Diario de Chihuahua 2026/nov/22: «Hallan dos cuerpos inhumados en casa»; Entre Líneas: «Localiza FGE cuerpos inhumados clandestinamente durante cateo en la colonia Manuel Valdez») (🔴 inhumación clandestina) · hallazgo durante un cateo de la FGE, por titular de medio · causa de muerte e identidad: no informadas · " + NOD,
  panel="<b>2 cuerpos inhumados</b> en una vivienda", inst="FGE de Chihuahua (por titular de medio)", nac="—", conf="★★★☆☆",
  campo="hora no fijada; actuación de la FGE solo por titular de medio; causa de muerte no informada", I=1, N=0, R=3, A=0,
  fechadas=["Circuito Frontera (2026/11/21)", "El Diario de Chihuahua (2026/nov/22)"], estatus="Parcialmente corroborado", arm=None,
  desl="Manuel Valdez no figura en los cartelones de 152 a 155. Inhumación en vivienda intervenida, no fosa de colectivo."),
 dict(id="ARG-156-009", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-21", hora="mañana; aviso ~07:40 o ~09:00 (solo por resumen)", mu=0, he=0, cu=3, hk=8,
  ent="Sinaloa", mun="Guasave (El Burrión, junto al estadio de Mojolo)", dia="SÁB 21-NOV, POR RUTA",
  fecha_txt="sábado 21-nov, por ruta; mañana, solo por resumen",
  title="SINALOA · GUASAVE — LOCALIZAN A TRES HOMBRES SIN VIDA CON EQUIPO TÁCTICO JUNTO AL ESTADIO DE BÉISBOL DE MOJOLO",
  hecho="Guasave · <code>SINDICATURA EL BURRIÓN, JUNTO AL ESTADIO DE MOJOLO</code>, por titular · sábado 21-NOV, por ruta (Línea Directa 2026-11-21: «Localizan a tres hombres sin vida junto a estadio de beisbol en Guasave; portaban equipo táctico») · mañana, aviso ~07:40 o ~09:00, " + RES + " · <b>3 hombres sin vida</b> con equipo táctico, por titular; junto a una camioneta blindada, por titular (Meganoticias: «Hallan a tres hombres sin vida junto a camioneta blindada en Guasave») (🔴 hallazgo múltiple) · causa de muerte: no informada por autoridad · vínculo con ARG-156-001: <code>NO ACREDITADO</code> · " + NOD,
  panel="<b>3 hombres sin vida</b> con equipo táctico", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; causa de muerte no informada; ninguna fuente institucional ni nacional", I=0, N=0, R=2, A=0,
  fechadas=["Línea Directa (2026-11-21)"], estatus="Parcialmente corroborado", arm=None,
  desl="«Hallan a otros 4 hombres asesinados en comunidades de Guasave; suman 11 muertos» (Noroeste; Luz Noticias 2026-11-21): recuento de medios, no se integra. Identidades: no se reproducen."),
 dict(id="ARG-156-010", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-22", hora="no informada", mu=0, he=0, cu=0, hk=2,
  ent="Sinaloa", mun="Culiacán (fracc. Stanza Torralba)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="publicación domingo 22-nov, por ruta; día y hora del hecho no fijados",
  title="SINALOA · CULIACÁN — HOMBRES ARMADOS SACAN DE UNA CASA A TRES JÓVENES, UNO DE ELLOS MENOR DE EDAD",
  hecho="Culiacán · <code>FRACC. STANZA TORRALBA, VIVIENDA</code>, " + RES + " · publicación domingo 22-NOV, por ruta (Infobae 2026/11/22: «Tres jóvenes fueron sacados de una casa por hombres armados en Culiacán, entre ellos un menor de edad; se desconoce su paradero») · día y hora del hecho no fijados · " + FR + " · <b>3 jóvenes privados de la libertad</b>, uno menor de edad, por titular; paradero desconocido (🔴 desaparición múltiple) · " + FU + " · " + NOD,
  panel="<b>3 jóvenes privados de la libertad</b>", inst=SB, nac="Infobae", conf="★★☆☆☆",
  campo="fuente única; día y hora del hecho no fijados; ninguna fuente institucional", I=0, N=1, R=0, A=0,
  fechadas=["Infobae (2026/11/22)"], estatus="Pendiente de corroboración", arm=None,
  desl="Stanza Torralba no figura en los cartelones de 152 a 155. Identidades: no se reproducen."),
 dict(id="ARG-156-011", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-11-21", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Guerrero", mun="Chilapa de Álvarez y Atlixtac (paraje Las Antenas)", dia="SÁB 21-NOV, POR RUTA",
  fecha_txt="publicación sábado 21-nov, por ruta; día del hallazgo, solo por resumen; hora no fijada",
  title="GUERRERO · CHILAPA — UN COLECTIVO HALLA RESTOS HUMANOS DURANTE LA BÚSQUEDA DE UN JOVEN DESAPARECIDO",
  hecho="Chilapa de Álvarez–Atlixtac · <code>PARAJE LAS ANTENAS</code>, " + RES + " · publicación sábado 21-NOV, por ruta (El Independiente 2026/11/21: «Hallan restos humanos durante búsqueda de joven desaparecido en Chilapa») · día del hallazgo, " + DSR + "; hora no fijada · <b>restos óseos</b>, por titular (El Sur: «Halla colectivo restos óseos en zona entre Chilapa y Atlixtac») (🔴 hallazgo de restos) · número de personas: no informado · «posiblemente humanos», " + RES + " · ninguna autoridad nombrada · " + NOD,
  panel="<b>Restos óseos</b> hallados por un colectivo", inst=SB, nac="—", conf="★★☆☆☆",
  campo="día del hallazgo solo por resumen; número de personas no informado; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Independiente (2026/11/21)"], estatus="Pendiente de corroboración", arm=None,
  desl="Chilapa figura en ARGOS 153 por otro hecho (comerciante, col. Valle Dorado, visto): no es este. Restos sin cifra de personas: no se suman al total de cuerpos."),
 # ======================= AMARILLOS
 dict(id="ARG-156-012", estado="MX-VER", region="Golfo", color="amarillo", impacto="mediano", fecha="2026-11-20", hora="tarde (solo por resumen)", mu=0, he=0, cu=0, hk=14,
  ent="Veracruz", mun="Carlos A. Carrillo", dia="VIE 20-NOV, POR RUTA",
  fecha_txt="viernes 20-nov, por ruta; tarde, solo por resumen",
  title="VERACRUZ · CARLOS A. CARRILLO — AGREDEN A POLICÍAS ESTATALES DURANTE EL DESFILE DEL 20 DE NOVIEMBRE: UN AGRESOR MUERTO",
  hecho="Carlos A. Carrillo · inmediaciones de un campo deportivo, " + RES + " · viernes 20-NOV, por ruta (ABC Noticias 2026/11/20: «Interrumpen desfile del 20 de noviembre por balacera en Veracruz»; MVS 2026/11/20: «Deja un muerto y dos detenidos enfrentamiento armado en Veracruz»; La Silla Rota 2026/11/20) · tarde, " + RES + " · <b>1 hombre muerto</b>, presunto agresor, por titular (El Informador 2026/11/20: «Veracruz: Enfrentamiento entre presuntos delincuentes y policías deja un muerto y dos detenidos»): fuera del recuento de muertos por agresión · ningún policía lesionado, " + RES + " · agresión a policías estatales, por titular del comunicado de la SSP («Detiene SSP a dos hombres y asegura armas de fuego tras agresión en Carlos A. Carrillo»); los agentes recababan información sobre un inmueble, " + RES + ": " + QNI + " (🟡 confrontación sin agravantes) · desfile escolar suspendido, por titular · detención: ficha aparte",
  panel="<b>Agresión a policías estatales</b>: 1 agresor muerto", inst="SSP de Veracruz (comunicado)", nac="MVS · El Informador · EFE", conf="★★★★☆",
  campo="hora y contenido del comunicado solo por resumen", I=1, N=3, R=4, A=0,
  fechadas=["ABC Noticias (2026/11/20)", "MVS (2026/11/20)", "La Silla Rota (2026/11/20)", "Hora Cero (2026/11/20)"], estatus="Confirmado", arm=None,
  desl="Carrillo del índice: col. Julián Carrillo, SLP (ARGOS 154): homónimo. «Ataque en Veracruz deja dos agentes federales muertos y una herida: Harfuch» (ABC Noticias 2026/9/5): Omealca, septiembre, otro hecho. EFE (Infobae, ABC Color, SWI): una sola fuente."),
 dict(id="ARG-156-013", estado="MX-MEX", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-20", hora="~09:10 (solo por resumen)", mu=1, he=1, cu=0, hk=9,
  ent="Estado de México", mun="Ecatepec (Plaza Aragón)", dia="VIE 20-NOV, POR RUTA",
  fecha_txt="viernes 20-nov, por ruta; ~09:10, solo por resumen",
  title="ESTADO DE MÉXICO · ECATEPEC — INTENTO DE ASALTO A UNA CAMIONETA DE VALORES EN PLAZA ARAGÓN: UN CUSTODIO MUERTO",
  hecho="Ecatepec · <code>PLAZA ARAGÓN</code>, por titular · viernes 20-NOV, por ruta (La Jornada 2026/11/20: «Asalto a camioneta de valores en Plaza Aragón deja un custodio muerto»; La Silla Rota 2026/11/20: «Intento de asalto en Plaza Aragón deja un muerto en Ecatepec») · ~09:10, " + RES + " · <b>1 custodio muerto</b>, por titular · <b>1 herido</b>, por titular (Heraldo de México Edomex 2026/11/20: «…reportan un muerto y un lesionado»); dos o más, " + RES + " (🟡 homicidio doloso único) · agresores huidos en motocicleta, " + RES + " · " + NOD,
  panel="<b>Custodio de valores asesinado</b>", inst=SB, nac="La Jornada · Heraldo de México · ADN40", conf="★★★☆☆",
  campo="hora solo por resumen; heridos contradichos; ninguna fuente institucional", I=0, N=3, R=2, A=0,
  fechadas=["La Jornada (2026/11/20)", "La Silla Rota (2026/11/20)", "Heraldo de México Edomex (2026/11/20)", "ABC Noticias (2026/11/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="Plaza Aragón no figura en el índice. ADN40 («…hoy 20 de noviembre») y N+: coberturas tipo liveblog, no fechan. Identidad: no se reproduce."),
 dict(id="ARG-156-014", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-19", hora="noche (solo por resumen)", mu=1, he=0, cu=0, hk=21,
  ent="Baja California", mun="Mexicali (col. Hacienda de las Torres)", dia="JUE 19-NOV, POR RESUMEN",
  fecha_txt="publicación viernes 20-nov, por ruta; noche del jueves 19, DÍA SOLO POR RESUMEN",
  title="BAJA CALIFORNIA · MEXICALI — ASESINAN A UN HOMBRE QUE CAYÓ EN SU CAMIONETA A UN CANAL",
  hecho="Mexicali · <code>COL. HACIENDA DE LAS TORRES</code>, " + RES + " · publicación viernes 20-NOV, por ruta (Punto Norte 2026/11/20, palabras del slug: «muere hombre en ataque armado cayo en su camioneta a un canal en mexicali») · noche del jueves 19, " + DSR + " · " + RET + " · <b>1 hombre muerto</b>, por slug de ruta fechada (🟡 homicidio doloso único) · " + FU + " · " + NOD,
  panel="<b>Hombre asesinado</b> en su camioneta", inst=SB, nac="—", conf="★★☆☆☆",
  campo="fuente única; día solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Punto Norte (2026/11/20)"], estatus="Pendiente de corroboración", arm=None,
  desl="Hacienda de las Torres no figura en los cartelones de 152 a 155; Mexicali, por ARG-146-011 (fosas): otro hecho. Identidad: no se reproduce."),
 # ======================= VERDES
 dict(id="ARG-156-015", estado="MX-SIN", region="Noroeste", color="verde", impacto="grande", fecha="2026-11-20", hora="noche (solo por resumen)", mu=0, he=0, cu=0, hk=21,
  ent="Sinaloa", mun="Guasave", dia="VIE 20-NOV, POR RESUMEN",
  fecha_txt="publicación sábado 21-nov, por ruta; captura la noche del viernes 20, DÍA SOLO POR RESUMEN",
  title="SINALOA · GUASAVE — FUERZAS FEDERALES CAPTURAN A «EL CHAPO ISIDRO» Y DETIENEN A OCHO PERSONAS",
  hecho="Guasave · captura la noche del viernes 20-NOV, " + DSR + " · publicación sábado 21-NOV, por ruta (El Informador 2026/11/21: «Tras balacera en Guasave que dejó cuatro militares muertos, trasladan al \"Chapo Isidro\" a la FEMDO»; Proceso 2026/11/21) · <b>captura de «El Chapo Isidro»</b>, señalado jefe de la organización Beltrán Leyva, por titular (🟢 detención) · <b>8 detenidos</b>, cifra de la Defensa por titular de medio (UnoTV: «Chapo Isidro: Defensa confirma 11 muertos y 8 detenidos tras operativo en Guasave»; Yahoo Noticias) · traslado a la FEMDO, por titular · Defensa, Fuerzas Especiales y GN · armamento, equipo táctico, droga y dinero, " + RES + ": " + CND,
  panel="<b>Captura de un jefe criminal y 8 detenidos</b>", inst="Defensa (por titular de medio)", nac="UnoTV · Proceso · El Informador · Yahoo Noticias", conf="★★★☆☆",
  campo="día y hora de la captura solo por resumen; cifra de la Defensa solo por titular de medio", I=1, N=4, R=0, A=0,
  fechadas=["El Informador (2026/11/21)", "Proceso (2026/11/21)", "Record (2026/11/21)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armamento sin cantidad publicada: evento cualitativo",
  desl="Delito y captura en la misma ventana: dos fichas (ARG-156-001 y esta). Nombre: no se reproduce."),
 dict(id="ARG-156-016", estado="MX-VER", region="Golfo", color="verde", impacto="mediano", fecha="2026-11-20", hora="tarde (solo por resumen)", mu=0, he=0, cu=0, hk=15,
  ent="Veracruz", mun="Carlos A. Carrillo", dia="VIE 20-NOV, POR RUTA",
  fecha_txt="viernes 20-nov, por ruta; tarde, solo por resumen",
  title="VERACRUZ · CARLOS A. CARRILLO — LA SSP DETIENE A DOS HOMBRES Y ASEGURA ARMAS DE FUEGO TRAS LA AGRESIÓN",
  hecho="Carlos A. Carrillo · viernes 20-NOV, por ruta (Hora Cero 2026/11/20: «Detiene SSP a dos hombres y asegura armas de fuego tras agresión en Carlos A. Carrillo», republicación del comunicado; Golpe Político 2026/11/20: «Detienen a dos hombres tras enfrentamiento con policías estatales en Carlos A. Carrillo») · <b>2 detenidos</b>, cifra de autoridad por titular del comunicado de la SSP (🟢 detención) · armas de fuego y equipo táctico, por titular, sin cantidad: " + CND + " · vehículos, chalecos y presunta droga, " + RES,
  panel="<b>2 detenidos</b> y armas sin cantidad publicada", inst="SSP de Veracruz (comunicado)", nac="MVS · El Informador", conf="★★★★☆",
  campo="cantidad de armas no publicada; hora solo por resumen", I=1, N=2, R=2, A=0,
  fechadas=["Hora Cero (2026/11/20)", "Golpe Político (2026/11/20)"], estatus="Confirmado", arm=None, armtxt="sin fila — armas sin cantidad publicada: evento cualitativo",
  desl="Delito y detención en la misma ventana: dos fichas (ARG-156-012 y esta). Nombres: no se reproducen."),
 dict(id="ARG-156-017", estado="MX-OAX", region="Sureste", color="verde", impacto="mediano", fecha="2026-11-21", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Oaxaca", mun="Juchitán de Zaragoza", dia="SÁB 21-NOV, POR RUTA",
  fecha_txt="publicación sábado 21-nov, por ruta; día de la captura no publicado",
  title="OAXACA · JUCHITÁN — FISCALÍA, DEFENSA, SEMAR, GN Y POLICÍA ESTATAL DETIENEN A TRES INTEGRANTES DE «LOS CROMOS»",
  hecho="Juchitán de Zaragoza · publicación sábado 21-NOV, por ruta (La Razón 2026/11/21: «Detienen a tres presuntos integrantes de 'Los Cromos' en Oaxaca»; El Imparcial 2026/11/21) · día de la captura no publicado · <b>3 detenidos</b>, por titular del boletín 2998 de la FGEO («En operativo conjunto, Fiscalía de Oaxaca, DEFENSA, SEMAR, Guardia Nacional y Policía Estatal detienen a tres integrantes de \"Los Cromos\" en Juchitán; suman siete capturas de esta célula») (🟢 detención) · siete capturas acumuladas de la célula, por titular; cuatro previas, el 19-nov, boletín 2992, " + RES + " · 2 armas largas, 3 cargadores y cartuchos, " + RES + ": <code>CANTIDAD NO CITABLE — NO SE INTEGRA</code> · vínculo con extorsión, secuestro y homicidio en el Istmo, por titular (El Imparcial)",
  panel="<b>3 detenidos</b> de una célula del Istmo", inst="FGEO (boletín 2998)", nac="La Razón · Sinembargo · UnoTV", conf="★★★☆☆",
  campo="día de la captura no publicado; armamento solo por resumen", I=1, N=3, R=1, A=0,
  fechadas=["La Razón (2026/11/21)", "El Imparcial (2026/11/21)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armas y cartuchos solo por resumen: cantidad no citable",
  desl="«Los Cromos» figura por ARG-132-006 (captura de su líder, octubre): otro hecho; Juchitán, por ARG-150-005 y ARG-149-012: otros hechos. Boletín 2992 (4 detenidos, 19-nov por resumen): sin ruta ni hora, no se ficha. Nombres: no se reproducen."),
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
HORAS = 62 + 54 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
RREG = {g: sum(1 for e in E if e["color"] == "rojo" and e["region"] == g) for g in ("Noroeste", "Noreste", "Occidente", "Centro", "Golfo", "Sureste")}
assert TOT == [0] * 10 and ARMAS == 0 and ND == [True] * 10, (TOT, ND)
assert cnt == {"rojo": 11, "amarillo": 3, "verde": 3}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0} and R == [], cnt_rec
assert (MU, HE, CU) == (15, 2, 5), (MU, HE, CU)
assert DENS == "0,27" and RPH == "0,17", (DENS, RPH)
assert (NAP, NFR, NRET) == (1, 1, 3), (NAP, NFR, NRET)
assert len(ENT) == 9 and len(ENT_ROJO) == 6, (ENT, ENT_ROJO)
assert RREG == {"Noroeste": 7, "Noreste": 0, "Occidente": 1, "Centro": 2, "Golfo": 0, "Sureste": 1}, RREG
assert sorted(e["id"] for e in E) == [f"ARG-156-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-19" <= x["fecha"] <= "2026-11-22", x["id"]
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
head = head.replace("<title>ARGOS 155 — Reporte Nacional de Seguridad — 2026-11-19</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA DEFENSA EL PARTE DE QUIÉN INICIÓ LA AGRESIÓN EN GUASAVE Y EL INVENTARIO DEL ARMAMENTO ASEGURADO EN EL OPERATIVO</b> (ARG-156-001 y -015).
      <br><b>2. SOLICITE A LA FGR Y A LA FISCALÍA DEL ESTADO DE MÉXICO EL SALDO OFICIAL Y LA HORA DEL ATAQUE A AGENTES FEDERALES EN NOPALTEPEC</b> (ARG-156-003).
      <br><b>3. SOLICITE A LA FISCALÍA DE GUANAJUATO LA HORA Y LA LÍNEA DE INVESTIGACIÓN DE LA EMBOSCADA AL MANDO POLICIAL DE PUEBLO NUEVO</b> (ARG-156-004).
      <br><b>4. SOLICITE A LA FISCALÍA DE SINALOA LA HORA, EL NÚMERO DE HERIDOS Y EL MÓVIL DEL ATAQUE A LA FAMILIA EN ESCUINAPA</b> (ARG-156-005).
      <br><b>5. SOLICITE A LA FISCALÍA DE SINALOA LA ACTIVACIÓN DE BÚSQUEDA DE LOS TRES JÓVENES PRIVADOS DE LA LIBERTAD EN CULIACÁN</b> (ARG-156-010).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>19-nov 18:40 → 22-nov 09:34 CDMX</b> (<b>{DUR}</b>) · ventana larga: jue 19 (desde 18:40) · vie 20 · sáb 21 · dom 22 (hasta 09:34) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
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
    <b>Armamento</b>: ningún aseguramiento de la ventana con cantidad publicada por titular o por autoridad: n/d · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas (Nopaltepec, 1 de 1 o 2, saldo contradicho); <b>agresores abatidos, fuera</b>: 7 (Guasave) y 1 (Carlos A. Carrillo) · <b>heridos</b>: {HE} (Escuinapa, Ecatepec) · <b>cuerpos</b>: {CU} (Ciudad Juárez 2, Guasave 3); restos de Chilapa sin cifra de personas, no se suman · <b>detenidos</b>: Guasave 8 (cifra de la Defensa por titular de medio), Carlos A. Carrillo 2 (SSP), Juchitán 3 (FGEO): sin cantidad de armamento, fuera del conteo de detenidos en aseguramiento; no se suman · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (publicado el día de cierre) · <b>totales sujetos a {NRET} cláusulas de retiro</b> (Nopaltepec: hora no fijada; Pueblo Nuevo y Mexicali: noche del 19 solo por resumen).
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «Tres muertos y un herido dejan ataques en Culiacán» (López-Dóriga; Síntesis 2026/11/20) · «Hallan a otros 4 hombres asesinados en comunidades de Guasave; suman 11 muertos» (Noroeste) · «Reporta Fuerza Civil 62 detenidos durante operativo metropolitano en Nuevo León» (MVS 2026/11/20) · «Más de 60 detenidos tras operativos en Veracruz» (Meganoticias) · «Guanajuato suma 24 policías asesinados» (La Nigua) · «México suma 221 policías asesinados en 2026» (UnoTV).
    <br><b>Vistos, fuera de totales</b> (sin ruta con día, fuente única o ventana anterior): Puente Nacional, Ver., cuerpo de una adolescente reportada desaparecida, viernes {RES}, sin ruta, causa no informada por autoridad · Tamuín, SLP, hombre asesinado en su domicilio, sábado 21 {RES}, sin ruta (Telediario) · Cuautla, Mor., conductor asesinado en su auto, viernes {RES}, sin ruta · Cañada Morelos, policías heridos, entidad no fijada, sin ruta · Santa María Ostula, Mich., comunero muerto y tres mujeres heridas en una emboscada (Milenio), sin fecha · Culiacán, La Costerita, dos cuerpos, sin fecha en la ruta · Mocorito, Sin., seis detenidos, día {RES} · Zihuatanejo, Gro., cinco detenidos con armas y droga, 20-nov {RES}, sin ruta · Tehuitzingo y Cuautlancingo, Pue., detenidos con armas, sin ruta · Tulum, QRoo, turista herido, sin fecha · Pachuca, Hgo., exdirector policial de Huehuetla asesinado, sin fecha · General Bravo, NL, tres capturados tras persecución, sin fecha · Piedras Negras, Coah., restos de un cuerpo (FGE), sin fecha · <b>ventanas anteriores</b>: Acapulco, km 21, dos muertos en una vivienda: 3-nov por ruta (El Diario 2026/nov/03) · Mazatlán, ataque con explosivos a un lote de autos, 17-nov por ruta (Luz Noticias 2026-11-17), hora {RES}; autoridades lo consideran hecho aislado (Línea Directa 2026-11-18): no admite recuperación · Cosoleacaque, Los Prados, hombre asesinado el lunes 16 {RES}: otro hecho que ARG-149-013 · Nuevo Laredo, 16 armas y más de 4 mil cartuchos (La Región 2026/11/22), hecho del 11-nov {RES}: <code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — POSIBLE DUPLICIDAD CON EL BOLETÍN DEL 11</code> · Parras, Coah., osamenta, 17-nov · Valle de las Palmas: sin cambio.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Uruapan (ARG-155-001)</b>: lugar, camioneta, por titular («¡Ultiman a dos hombres a bordo de una camioneta en Uruapan!…», RED Michoacán 2026/11/19); la vía pública, versión de otros medios {RES} · <b>Tepehuacán (ARG-155-011)</b>: «Cuatro imputados por caso de Tepehuacán ya están en prisión preventiva», por titular (La Silla Rota 2026/11/20); duplicidad del plazo constitucional; sin vinculación; día de las capturas sin fijar · <b>Texhuacán (ARG-151-001)</b>: «Fiscalía de Veracruz captura a 3 presuntos asesinos de Regidora y líder local del PRI», por titular (Sinembargo), día de la captura sin fijar: no se ficha · <b>Cajeme</b>: «FGJES imputa a dos hombres por el homicidio de una niña de 6 años…», por titular (El Imparcial 2026/11/20); sin vinculación · <b>Ciudad Juárez</b>: dos vinculados a proceso por el ataque a federales del 11-nov (El Diario 2026/nov/19); <code>NO ES SENTENCIA</code> · <b>Ometepec (ARG-155-010)</b>: Defensa y GN {RES}; sin vinculación publicada · <b>Cancún (ARG-155-012)</b>: 6 detenidos por titular frente a 3 («Triple homicidio en Villas Otoch: trasciende detención», Quintana Roo Hoy); sin cifra de la FGE · <b>Río Bravo (ARG-154-008)</b>: «Río Bravo suma otro hallazgo de restos humanos quemados» (Elefante Blanco 2026/11/18); víctimas y levantamiento no informados · <b>Culiacán (ARG-155-002)</b>: un encargado de minisúper muerto en la col. Miguel Hidalgo figura en el balance del 20-nov {RES}: <code>POSIBLE DESFASE DE FECHA — EN REVISIÓN</code> · <b>Tecate (ARG-150-REC-001)</b>: sin dos campos individualizadores por titular: el saldo no se corrige · <b>Mexicali (ARG-146-011)</b>: consultado; sin novedad en la ventana · <b>cláusulas de 152 a 155</b> (Santa Teresa, Pueblo Nuevo de Mazatlán, Tecate, Gaviotas Sur, Lachigalla, Acaponeta, Azcapotzalco, León, Tepeaca): ningún titular fija la hora; siguen abiertas.
  </p>
'''

byid = {e["id"]: e for e in E}
co1 = "\n".join(ficha(byid[f"ARG-156-{i:03d}"]) for i in (1, 2, 15))
co2 = "\n".join(ficha(byid[f"ARG-156-{i:03d}"]) for i in (3, 4, 5))
co3 = "\n".join(ficha(byid[f"ARG-156-{i:03d}"]) for i in (6, 7, 8))
co4 = "\n".join(ficha(byid[f"ARG-156-{i:03d}"]) for i in (9, 10, 11))
co5 = "\n".join(ficha(byid[f"ARG-156-{i:03d}"]) for i in (12, 16, 13))
co6 = "\n".join(ficha(byid[f"ARG-156-{i:03d}"]) for i in (14, 17))
assert sorted(re.findall(r'id="(ARG-156-0\d\d)"', co1 + co2 + co3 + co4 + co5 + co6)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
NDR = "solo por resumen: <b>cantidad no determinada</b>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "Guasave y Carlos A. Carrillo: sin cantidad publicada; Juchitán, " + NDR),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), NDR),
 tile(4, "Cargadores", tv(5), NDR),
 tile(5, "Granadas", tv(6), "lanzagranadas en Guasave, " + NDR),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), "Guasave, " + NDR),
 tile(8, "Armamento especial", tv(3), "fusil Barrett en Guasave, " + NDR),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento con cantidad</b>: ninguno"),
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
    <b>Lectura regional</b>: ninguna región con arma integrada · aseguramientos sin cantidad publicada en Noroeste (Guasave), Golfo (Carlos A. Carrillo) y Sureste (Juchitán). <b>Cálculo propio</b>.
    <br><b>BOLETÍN FEDERAL</b>: acciones del 19-nov: __FED17__ · acciones del 20 y del 21-nov: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título · agregado de fin de semana: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · acciones del 13, 14 y 15-nov: <code>SIN RESULTADO INDEXADO EN VENTANA</code>; comunicados conjuntos sueltos del 13, 14 y 15 en gabinetedeseguridad.gob.mx, {RES} · <b>corroboración débil por construcción</b>; <b>un agregado no fija el día ni la hora de cada acción</b>.
    <br><code>VISTOS, NO INTEGRADOS</code>: Guerrero, 5 detenidos, 3 armas largas, 20 cargadores y 650 cartuchos; Tlaxcala, 1 detenido, 5 armas largas y 4 cortas (FGR y SSPC); Sayula de Alemán, Ver., 4 detenidos en cateos; Camargo, Tamps., armas, granadas y fentanilo: todo {RES} del boletín de acciones del 19, día y hora no fijados · Guasave (ARG-156-015): fusil Barrett, lanzagranadas y explosivos {RES}, sin cantidad · Carlos A. Carrillo (ARG-156-016): «asegura armas de fuego», por titular, sin cantidad · Juchitán (ARG-156-017): 2 armas largas, 3 cargadores y cartuchos {RES} del boletín 2998 · Juchitán, boletín 2992: 4 detenidos y 2 armas cortas {RES}, 19-nov sin hora · Nuevo Laredo, 16 armas, dos de ellas calibre .50, y más de 4 mil cartuchos, por titular (La Región 2026/11/22): hecho del 11-nov {RES}, <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · Tehuitzingo, Pue., escopeta y 6 cartuchos; Cuautlancingo, Pue., arma larga y pistola: {RES}, sin ruta.
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
      <tr><td><b>Guerrero</b><br>Iguala (caso Los Avispones, 2014)</td><td>Exalcalde de Iguala y otros coacusados (24 o 25, contradicho); tentativa de homicidio y homicidio calificado {RES}; absuelto de delincuencia organizada {RES}</td><td>60 años, por titular (Proceso 2026/11/19; La Silla Rota 2026/11/19; Heraldo de México 2026/11/20)</td><td>Juzgado federal en Matamoros {RES}</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin comunicado de la FGR (fgr.org.mx consultado) ni del Poder Judicial · fallo del 10-nov, dado a conocer el 19 {RES}: ventana de ARGOS 155 o frontera · apelada: no firme {RES}</td><td>Bajo</td></tr>
      <tr><td><b>Oaxaca</b><br>Sierra de Flores Magón</td><td>Violación de una adulta mayor; boletín 2,993 de la FGEO</td><td>14 años, por titular del boletín («FGEO obtiene 14 años de prisión…»)</td><td>FGEO</td><td>Publicación 19-nov {RES}: ventana de ARGOS 155 o frontera · fecha de la sentencia no publicada · el titular no lleva término de condena expreso · firmeza no informada</td><td>Medio</td></tr>
      <tr><td><b>Tabasco</b><br>Villahermosa</td><td>Feminicidio; boletín 5126 de la FGET, 18-nov {RES}</td><td>45 años {RES}</td><td>FGET <span class="muted-note">(índice)</span></td><td>Ventana de ARGOS 155 · sin URL individual ni dos campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Fuera de ventana</b></td><td>Monterrey: dos casos distintos (MVS 2026/11/13 y 2026/11/17) · Veracruz, 88 años por secuestro (Formato Siete 2026/11/13) · Champotón, 66 años (PorEsto 2026/11/6) · Tabasco 5119 y 5120 (9 y 10-nov)</td><td>—</td><td>—</td><td>Publicación anterior a la apertura; sin boletín leído</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida a <code>fgr.org.mx</code> (caso Iguala): <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>14 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Son · Coah, NL, Tamps, SLP, Zac · Gto, Col, Mich · Ver, Tab · Oax, Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> por dominio (Oaxaca: boletín 2,993 publicado el 19 {RES}, frontera)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>14</b> fiscalías estatales revisadas (Sonora: el dominio solo devuelve convocatorias; SLP: primera revisión del dominio)</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>18</b>: BCS, Chih, Sin, Dgo · Jal, Ags, Nay · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Camp · Gro, Chis, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 22-nov 09:34: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 20 entidades; solo consulta amplia en 11 —BCS · NL · Mich, Jal, Col · Tlax, Qro · Tab, Camp · Chis, Yuc—; <code>NO REVISADA</code> (1): Ags · <b>armamento: 25 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> salvo Oaxaca y Veracruz (boletines sin cantidad citable) · <code>NO REVISADA</code> (7): BC, Son, Chih, Sin · Tamps · CDMX, Pue</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 19-nov</b>: __FED17C__ · acciones del 20 y 21 y agregado de fin de semana: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · acciones del 13, 14 y 15: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · <code>BLOQUEO DE EGRESO REVERIFICADO EL 22-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Rojo por agravante</b>: muerte de personal militar, agresión letal a agentes federales y a un mando policial municipal, bloqueos con quema de vehículos, homicidios múltiples, privación múltiple de la libertad y hallazgos de cuerpos y restos; {RPH} rojos por hora (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Noroeste {RREG["Noroeste"]} · Centro {RREG["Centro"]} · Occidente {RREG["Occidente"]} · Sureste {RREG["Sureste"]} · Noreste y Golfo 0 (cálculo propio); cuatro de los rojos del Noroeste se concentran en Guasave y su entorno.
      <br><b>3.</b> <b>Violencia operativa</b>: una confrontación con policías estatales sin bajas policiales; homicidios dolosos únicos en el Estado de México y Baja California.
      <br><b>4.</b> <b>Respuesta institucional</b>: captura de un jefe de organización criminal en Sinaloa y detenciones en Veracruz y Oaxaca; ningún aseguramiento con cantidad integrable; ninguna sentencia integrable.
      <br><b>5.</b> <code>TOTALES NO COMPARABLES SIN MÁS CON LOS DE OTRAS EDICIONES: VENTANA LARGA DE 62 H 54 MIN (CUATRO DÍAS DE CALENDARIO), HECHOS CON CLÁUSULA DE RETIRO Y EN FRONTERA DE VENTANA (DETALLE EN TOTALES DEL CORTE). CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. REACCIÓN ARMADA A LA CAPTURA DE UN JEFE REGIONAL EN EL NORTE DE SINALOA</b> (ARG-156-001, -002, -009 y -015): ataque a fuerzas federales, bloqueos y quema de vehículos la misma noche; cuerpos con equipo táctico a la mañana siguiente, vínculo no acreditado. Línea: <b>vigilar los ejes Guasave–Los Mochis y Guasave–Guamúchil ante réplicas y reacomodo de mando</b>.
      <br><b>2. AGRESIONES LETALES A PERSONAL DE SEGURIDAD EN EL CENTRO Y EL BAJÍO</b> (ARG-156-003 y -004): agentes federales en el oriente del Estado de México y un mando municipal en el sur de Guanajuato; vínculo entre los casos no acreditado. Línea: <b>revisar las medidas de protección de mandos municipales en traslados carreteros del sur de Guanajuato</b>.
      <br><b>3. CIVILES EN TRÁNSITO ATACADOS EN EL LÍMITE SINALOA–NAYARIT</b> (ARG-156-005): cierre de paso a un vehículo familiar en carretera federal; versión de despojo solo por resumen; autoría no informada. Línea: <b>vigilar el tramo Palmillas–La Concha de la carretera federal 15 en coordinación con Nayarit</b>.
      <br><b>4. INHUMACIÓN CLANDESTINA Y RESTOS HALLADOS POR COLECTIVOS</b> (ARG-156-008 y -011): cuerpos enterrados en una vivienda de Ciudad Juárez y restos en la Montaña baja de Guerrero; identidades no informadas. Línea: <b>cotejar los hallazgos con los registros de personas desaparecidas de Ciudad Juárez y Chilapa</b>.
      <br><b>5. HOMICIDIOS MÚLTIPLES EN ESPACIOS RESIDENCIALES Y COMERCIALES</b> (ARG-156-006 y -007): fraccionamiento residencial en la zona metropolitana de Puebla y estacionamiento comercial en Ciudad Juárez; identidad de las víctimas de Puebla no confirmada; vínculo no acreditado. Línea: <b>vigilar los accesos de Lomas de Angelópolis ante posibles réplicas</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

FED17 = "boletín publicado, <code>SIN RESULTADO INDEXADO</code> en <code>gob.mx/sspc</code>; tomado de republicadores (RED113 2026/11; Tallapolítica; Certeza Diario; Ultranoticias; Ahora Tabasco); contenido <code>SOLO POR RESUMEN</code>"
arm2 = arm2.replace("__FED17__", FED17)
sent = sent.replace("__FED17C__", FED17)

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — GUASAVE: ATAQUE A FUERZAS FEDERALES, BLOQUEOS Y CAPTURA", co1)
 + page("CRIMEN ORGANIZADO (II) — AGRESIONES A AUTORIDADES EN EL ESTADO DE MÉXICO Y GUANAJUATO; FAMILIA ATACADA EN ESCUINAPA", co2)
 + page("CRIMEN ORGANIZADO (III) — HOMICIDIOS MÚLTIPLES EN PUEBLA Y CIUDAD JUÁREZ; INHUMACIÓN CLANDESTINA", co3)
 + page("CRIMEN ORGANIZADO (IV) — CUERPOS EN GUASAVE, PRIVACIÓN MÚLTIPLE EN CULIACÁN Y RESTOS EN CHILAPA", co4)
 + page("CRIMEN ORGANIZADO (V) — VERACRUZ Y ESTADO DE MÉXICO: AGRESIÓN A POLICÍAS, DETENCIÓN Y ASALTO", co5)
 + page("CRIMEN ORGANIZADO (VI) — HOMICIDIO EN MEXICALI; DETENCIONES EN JUCHITÁN", co6)
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
# ventana larga: cuatro fechas de calendario (19, 20, 21 y 22-nov); la plantilla de 155 trae 2
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 155 con WINDOW_DAYS = 2"
script = script.replace("WINDOW_DAYS = 2;", "WINDOW_DAYS = 4;")
assert script.count("WINDOW_DAYS = 4;") == 1 and "WINDOW_DAYS = 2;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
