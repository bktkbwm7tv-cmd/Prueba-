# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 150.
Uso: python3 tools/datos-argos-150.py <plantilla ARGOS 149> <salida>
Ventana: 9-nov 16:07 → 14-nov 10:09 CDMX. Archivo: argos-2026-11-14.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "150", "2026-11-14", "10:09"
CONSULTA = "2026-11-14, última búsqueda 10:23"
DUR = "114 h 02 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 16:07 DEL 9, ES DE LA VENTANA DE ARGOS 149 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS — AUTORIDADES
 dict(id="ARG-150-001", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-13", hora="tarde (solo por resumen)", mu=2, he=0, cu=0, hk=14,
  ent="Michoacán", mun="Zitácuaro (Curungueo)", dia="13-NOV, POR RUTA",
  title="MICHOACÁN · ZITÁCUARO — EMBOSCADA CONTRA LA GUARDIA CIVIL EN CURUNGUEO: DOS AGENTES MUERTOS",
  hecho="Zitácuaro · <code>CARRETERA ZITÁCUARO–MORELIA, CURUNGUEO, POR TITULAR</code> (Grupo Marmor 2026/11/13: «ataque armado en Curungueo cobra la vida de dos policías») · viernes 13-NOV, por ruta · tarde, " + RES + " · <b>2 agentes de la Guardia Civil muertos</b>, por titular (La Silla Rota 2026/11/13: «con emboscada a 2 estatales…»; MVS 2026/11/13: «confirma SSP muerte de dos elementos tras ataque en Zitácuaro») · 1 agente herido, " + RES + ", y «hay una mujer herida», por <i>slug</i> (Contramuro 13112026): <code>HERIDOS CONTRADICHOS — NO SE INTEGRAN</code> · atacados por la retaguardia desde dos camionetas, " + RES + " (🔴 ataque iniciado por el grupo contra fuerzas en patrullaje; muerte de personal) · «emboscada» frente a «presunto enfrentamiento» (1Plana) · " + NOD + " · armamento: no publicado",
  panel="<b>Emboscada contra la Guardia Civil: 2 agentes muertos</b>", inst="SSP Michoacán <span class=\"muted-note\">(por titular de medio; comunicado no leído)</span>", nac="La Silla Rota · MVS", conf="★★★☆☆",
  campo="hora y modo del ataque solo por resumen; heridos contradichos; declaración de la SSP solo a través del titular de un medio", I=1, N=2, R=4, A=0,
  fechadas=["La Silla Rota (2026/11/13)", "MVS (2026/11/13)", "Grupo Marmor (2026/11/13)", "Contramuro (13112026)"], estatus="Parcialmente corroborado", arm=None,
  desl="Zitácuaro en ARGOS 149: solo el laboratorio del agregado federal del 6 al 8-nov, sin ficha: otro hecho. Bloqueo y quema de llantas de pobladores de Curungueo tras el ataque: protesta civil, no narcobloqueo. «Michoacán llega a 36 policías asesinados» (La Silla Rota): recuento de medio, no se integra. Identidades: SSP a través de medios, no se reproducen."),
 dict(id="ARG-150-002", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-11", hora="noche (solo por resumen)", mu=1, he=2, cu=0, hk=21,
  ent="Michoacán", mun="Tepalcatepec (El Toril)", dia="11-NOV, POR RUTA",
  title="MICHOACÁN · TEPALCATEPEC — ATAQUE ARMADO CONTRA LA BASE DE LA POLICÍA MUNICIPAL EN EL TORIL: UN POLICÍA MUERTO",
  hecho="Tepalcatepec · <code>BASE DE LA POLICÍA MUNICIPAL, EL TORIL, POR TITULAR</code> (La Jornada 2026/11/11: «ataque a la base de la Policía Municipal de El Toril deja un muerto y dos heridos») · miércoles 11-NOV, por ruta (Grupo Marmor 2026/11/11) · noche, " + RES + " · <b>1 policía municipal muerto</b>, por titular · <code>HERIDOS CONTRADICHOS</code>: 2, por titular (La Jornada), frente a «tres policías heridos», por titular (Posta) · atribución al CJNG, por titular de medio (Infobae 2026/11/12), no oficial (🔴 ataque contra instalación de autoridad) · suspensión de clases y labores del Ayuntamiento el 12-NOV, por titular (Infobae; UnoTV) · " + NOD + " · armamento: no publicado",
  panel="<b>Ataque a la base de la Policía Municipal: 1 policía muerto</b>, 2 o 3 heridos", inst=SB, nac="La Jornada · Infobae · UnoTV", conf="★★★☆☆",
  campo="hora solo por resumen; heridos contradichos; ninguna fuente institucional", I=0, N=3, R=3, A=0,
  fechadas=["La Jornada (2026/11/11)", "Grupo Marmor (2026/11/11)", "Infobae (2026/11/12)", "Diario Puntual (2026/11/12)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepalcatepec no figura en las cinco ediciones previas. «Madrugada del jueves» (XEVT), " + RES + ": superado por las rutas del 11. Un ataque a una base de Tepalcatepec de septiembre, mezclado en un resumen: otro hecho."),
 dict(id="ARG-150-003", estado="MX-JAL", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-12", hora="no fijada", mu=0, he=2, cu=0, hk=13,
  ent="Jalisco", mun="Ocotlán", dia="12-NOV, POR RUTA",
  title="JALISCO · OCOTLÁN — CIVILES ARMADOS AGREDEN AL EJÉRCITO: DOS AGRESORES ABATIDOS, UN MILITAR Y UNA MUJER HERIDOS",
  hecho="Ocotlán · jueves 12-NOV, por ruta (La Jornada 2026/11/12: «enfrentamiento entre el Ejército y un grupo armado en Ocotlán deja dos muertos») · hora no fijada · personal militar <b>agredido por civiles armados al atender un reporte de vehículo robado</b>, Defensa (cuenta oficial en X), " + RES + " · <b>2 agresores abatidos</b>, por titular (El Universal: «abaten a dos criminales en Ocotlán… una mujer fue herida en el fuego cruzado») · <b>1 militar herido</b>, por titular (Sinaloahoy) · <b>1 mujer herida</b>, ajena al hecho, por titular (El Universal; Aristegui) · <code>HERIDOS CONTRADICHOS</code>: 2, frente a «dos muertos y tres heridos», por titular (Capital México) (🔴 agresión iniciada por el grupo contra personal en servicio; víctima civil ajena) · 1 detenido: ver <a href=\"#ARG-150-018\"><code>ARG-150-018</code></a>",
  panel="<b>Agresión al Ejército: 2 agresores abatidos</b>, 1 militar y 1 mujer heridos", inst="Defensa <span class=\"muted-note\">(cuenta oficial en X; solo por resumen)</span>", nac="La Jornada · El Universal · Milenio", conf="★★★☆☆",
  campo="quién inició, según la versión de Defensa, solo por resumen; hora no fijada", I=1, N=3, R=3, A=0,
  fechadas=["La Jornada (2026/11/12)", "Grupo Marmor (2026/11/12)", "Lo de Hoy (2026/11/13)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — armamento en <a href=\"#ARG-150-018\"><code>ARG-150-018</code></a>",
  desl="Los agresores abatidos no mueven el color ni se suman a «muertos por agresión». Quema de vehículos y bloqueos en Atotonilco el Alto el mismo día: sin ruta con día; García Harfuch «descarta narcobloqueos», por titular (El Universal): <code>ROJO SIN RUTA FECHADA</code>, en el panorama. Ocotlán no figura en las cinco ediciones previas."),
 dict(id="ARG-150-005", estado="MX-OAX", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-12", hora="noche (solo por resumen)", mu=1, he=0, cu=0, hk=21,
  ent="Oaxaca", mun="Juchitán de Zaragoza", dia="12-NOV, SOLO POR RESUMEN; PUB. 13-NOV, POR RUTA",
  title="OAXACA · JUCHITÁN — ASESINAN EN SU DOMICILIO A UN POLICÍA MUNICIPAL",
  hecho="Juchitán · <code>COL. TIERRA Y LIBERTAD O LIBERTAD, CONTRADICHA</code>, " + RES + " · <code>DÍA CONTRADICHO</code>: jueves 12-NOV por la noche o martes 10, " + RES + " · publicación 13-NOV, por ruta (Latinus 2026/11/13; Diario de Yucatán 2026/11/13: «ataques armados dejan dos hombres muertos en Juchitán y Santo Domingo Tehuantepec») · «asesinan en su domicilio a policía municipal de Juchitán», por titular (Omnia) · <b>1 policía municipal en activo muerto</b>, en su día de descanso, por titular (Imparcial Oaxaca) (🔴 víctima autoridad) · dos agresores, " + RES + " · la Comisaría municipal confirmó la muerte, " + RES + ": no es declaración leída · " + NOD,
  panel="<b>Policía municipal asesinado en su domicilio</b>", inst=SB, nac="Latinus · La Silla Rota", conf="★★★☆☆",
  campo="día contradicho, solo por resumen; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["Latinus (2026/11/13)", "La Silla Rota (2026/11/13)", "Diario de Yucatán (2026/11/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="No es ARG-149-012 (restaurante de un periodista, 7-nov): otro hecho, otra víctima. Conductor asesinado en Santo Domingo Tehuantepec, en la misma nota de Diario de Yucatán: 🟡, visto. Identidad: medios, no se reproduce."),
 dict(id="ARG-150-006", estado="MX-MEX", region="Centro", color="rojo", impacto="mediano", fecha="2026-11-10", hora="tarde (solo por resumen)", mu=1, he=0, cu=0, hk=16,
  ent="Estado de México", mun="San José del Rincón", dia="10 U 11-NOV; PUB. 11-NOV, POR RUTA",
  fecha_txt="10 u 11-nov, contradicho; publicación 11-nov, por ruta",
  title="ESTADO DE MÉXICO · SAN JOSÉ DEL RINCÓN — MATAN A BALAZOS A UN POLICÍA MUNICIPAL QUE INTENTÓ FRUSTRAR UN ROBO DE VEHÍCULO",
  hecho="San José del Rincón · <code>LUGAR CONTRADICHO</code>: inmediaciones del mercado municipal o de una universidad, " + RES + " · publicación 11-NOV, por ruta (Seuno 2026/11/11: «asesinan a policía en Edomex durante persecución de auto robado»; Reporteros en Movimiento 2026/11/11: «asesinan a policía municipal al intentar frustrar robo de vehículo») · <code>DÍA CONTRADICHO</code>: martes 10 por la tarde o miércoles 11, " + RES + " · <b>1 policía municipal muerto</b> a balazos, por titular (🔴 víctima autoridad) · agresión de terceros, no arma de cargo · la FGJEM investiga, " + RES + " · " + NOD,
  panel="<b>Policía municipal asesinado al intentar frustrar un robo de vehículo</b>", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="día y lugar contradichos; ninguna fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["Seuno (2026/11/11)", "Reporteros en Movimiento (2026/11/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="San José del Rincón en el índice: ARG-128-003 (San Joaquín Lamillas, octubre): otro hecho. Identidad: medios, no se reproduce."),
 # ======================= ROJOS — HOMICIDIOS MÚLTIPLES Y HALLAZGOS
 dict(id="ARG-150-004", estado="MX-VER", region="Golfo", color="rojo", impacto="grande", fecha="2026-11-12", hora="no fijada", mu=2, he=0, cu=0, hk=3,
  ent="Veracruz", mun="Tuxpan (Centro Médico de Tuxpan)", dia="11 O 12-NOV; PUB. 12-NOV, POR RUTA",
  fecha_txt="11 o 12-nov, contradicho; publicación 12-nov, por ruta",
  title="VERACRUZ · TUXPAN — ATAQUE ARMADO DENTRO DE UN HOSPITAL PRIVADO: DOS MUERTOS",
  hecho="Tuxpan · <code>CENTRO MÉDICO DE TUXPAN, POR TITULAR</code> · publicación 12-NOV, por ruta (La Silla Rota 2026/11/12: «asesinan a balazos a Jorge Cantú dentro del Centro Médico Tuxpan; detienen a 4»; MVS 2026/11/12) · <code>DÍA DEL ATAQUE CONTRADICHO</code>: miércoles 11 o madrugada del jueves 12, " + RES + " · víctima hospitalizada tras sobrevivir a un ataque tres días antes, por titular (Proceso 2026/11/13: «sobrevive a atentado y lo rematan dentro de clínica»; La Aldea 2026/11/13) · <b>1 hombre muerto en el sitio</b>; su acompañante, herida, murió después, por titular (Noticias Veracruz y Diario de Yucatán 2026/11/13: «muere segunda víctima…»; fecha de la muerte no fijada, publicación del 13 por ruta): <b>2 muertos</b> (🔴 homicidio múltiple dentro de una instalación de salud) · 4 detenidos: ver <a href=\"#ARG-150-019\"><code>ARG-150-019</code></a>",
  panel="<b>Ataque dentro de un hospital privado: 2 muertos</b>", inst=SB, nac="La Silla Rota · MVS · Proceso · El Universal", conf="★★★☆☆",
  campo="día del ataque contradicho; ninguna fuente institucional leída", I=0, N=4, R=4, A=0,
  fechadas=["La Silla Rota (2026/11/12)", "MVS (2026/11/12)", "Diario de Yucatán (2026/11/12)", "Proceso (2026/11/13)", "Noticias Veracruz (2026/11/13)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — armamento no publicado",
  desl="Tuxpan en el índice: ARG-102-REC-005 y ARG-105-REC-003: otros hechos. Primer ataque contra la misma víctima (martes 10, calle Colombia): " + RES + ", antecedente, sin ficha propia. Identidades: medios, no se reproducen."),
 dict(id="ARG-150-007", estado="MX-CHH", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-12", hora="no fijada", mu=2, he=0, cu=0, hk=12,
  ent="Chihuahua", mun="Chihuahua (Las Malvinas)", dia="12-NOV, POR RUTA",
  title="CHIHUAHUA · CHIHUAHUA — ATAQUE ARMADO EN LAS MALVINAS: DOS HOMBRES MUERTOS, UNO DE ELLOS EXPOLICÍA",
  hecho="Chihuahua · <code>COL. LAS MALVINAS, POR TITULAR</code> · jueves 12-NOV, por ruta (El Diario de Chihuahua 2026/nov/12: «ataque armado deja dos hombres muertos en Las Malvinas») · <b>2 hombres muertos</b>, por titular (🔴 homicidio múltiple) · uno, expolicía municipal, por titular (Tiempo; Es Noticia 2026/11) · versión inicial «un muerto y un herido», por titular (La Opción y El Bordo 20261112): superada; el segundo murió a dos cuadras, " + RES + " · domicilio señalado como punto de venta, " + RES + " · " + NOD,
  panel="<b>Doble homicidio</b>; una víctima, expolicía municipal", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional («la FGE realizó diligencias» no es declaración)", I=0, N=0, R=5, A=0,
  fechadas=["El Diario de Chihuahua (2026/nov/12)", "La Opción (20261112)", "El Bordo (20261112)", "Es Noticia (2026/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Las Malvinas no figura en las cinco ediciones previas. ARG-149-009 (Granjas Cerro Grande, 8-nov): otro hecho."),
 dict(id="ARG-150-008", estado="MX-HID", region="Centro", color="rojo", impacto="grande", fecha="2026-11-12", hora="noche (solo por resumen)", mu=0, he=0, cu=3, hk=21,
  ent="Hidalgo", mun="Ajacuba (Tecomatlán)", dia="12-NOV, SOLO POR RESUMEN; PUB. 13-NOV, POR RUTA",
  title="HIDALGO · AJACUBA — CATEO POR UN REPORTE DE DESAPARICIÓN: FOSA CON TRES CUERPOS EN EL PATIO DE UNA VIVIENDA",
  hecho="Ajacuba · <code>TECOMATLÁN («EL RINCONCITO», SEGÚN EL UNIVERSAL; «SAN NICOLÁS TECOMATLÁN», SEGÚN OTROS)</code> · cateo de la noche del jueves 12-NOV, " + RES + " · publicación 13-NOV, por ruta (Diario de Yucatán 2026/11/13: «reporte por desaparición lleva al hallazgo de tres cuerpos en una casa de Ajacuba») · <b>3 cuerpos</b> enterrados en el patio, por titular (La Jornada Hidalgo: «PGJEH localiza tres cuerpos en una fosa clandestina durante cateo») (🔴 fosa) · PGJEH, fiscalía especializada en desaparición y Comisión de Búsqueda, " + RES + " · identidad y causa de muerte: no informadas · " + NOD,
  panel="<b>Fosa con 3 cuerpos</b> en una vivienda, hallada en un cateo", inst="PGJEH <span class=\"muted-note\">(por titular de medio; comunicado no leído)</span>", nac="El Universal · Milenio", conf="★★★☆☆",
  campo="día del cateo solo por resumen; declaración de la PGJEH solo a través del titular de un medio", I=1, N=2, R=5, A=0,
  fechadas=["Diario de Yucatán (2026/11/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ajacuba en el índice: ARG-119-ARM-003 (septiembre, aseguramiento): otro hecho. Vínculo con robo de hidrocarburo: medio no oficial, no se reproduce. Cuerpos sin causa de muerte informada: van a «cuerpos o restos»."),
 dict(id="ARG-150-009", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-11-12", hora="no fijada", mu=0, he=0, cu=2, hk=12,
  ent="Guanajuato", mun="Irapuato (Cuchicuato–Tamahula)", dia="12-NOV, POR RUTA",
  title="GUANAJUATO · IRAPUATO — COLECTIVO LOCALIZA DOS FOSAS CON DOS CRÁNEOS Y RESTOS ÓSEOS ENTRE CUCHICUATO Y TAMAHULA",
  hecho="Irapuato · <code>ENTRE CUCHICUATO Y TAMAHULA, POR TITULAR</code> · jueves 12-NOV, por ruta (AM 2026/11/12: «localiza colectivo dos cráneos y restos óseos en fosas clandestinas en Irapuato»; Correo 2026/nov/12: «Hasta Encontrarte halla nuevas fosas con restos humanos») · colectivo Hasta Encontrarte, tras un reporte anónimo, " + RES + " · <b>2 fosas, 2 cráneos y restos óseos</b>, por titular (🔴 fosa) · número de personas: no determinado · prendas y calzado, " + RES + " · indicios trasladados al Semefo, " + RES,
  panel="<b>Colectivo localiza 2 fosas</b> con 2 cráneos y restos óseos", inst=SB, nac="N+", conf="★★★☆☆",
  campo="número de personas no determinado; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["AM (2026/11/12)", "Correo (2026/nov/12)", "Noticieros en Línea (2026/nov/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cuchicuato y Tamahula no figuran en las cinco ediciones previas. En «cuerpos o restos» se cuentan los 2 cráneos, por titular; el número real de personas puede ser mayor."),
 dict(id="ARG-150-010", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-13", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Sinaloa", mun="Culiacán (Las Víboras, sindicatura de Costa Rica)", dia="13-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — MADRES BUSCADORAS LOCALIZAN RESTOS HUMANOS EN LAS VÍBORAS",
  hecho="Culiacán · <code>POBLADO LAS VÍBORAS, SINDICATURA DE COSTA RICA, POR TITULAR</code> · viernes 13-NOV, por ruta (Luz Noticias 2026-11-13: «madres buscadoras localizan restos humanos en el poblado de Las Víboras») · colectivo Madres en Lucha por tu Regreso a Casa, con GN y fiscalía especializada, " + RES + " · <b>restos humanos</b>, por titular; <code>CANTIDAD NO DETERMINADA</code> (🔴 restos) · identidad: por determinar",
  panel="<b>Colectivo localiza restos humanos</b>; cantidad no publicada", inst=SB, nac="—", conf="★★★☆☆",
  campo="día sostenido por una sola ruta; cantidad no publicada; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-11-13)"], estatus="Parcialmente corroborado", arm=None,
  desl="Las Víboras no figura en las cinco ediciones previas. Sin cifra: no entra en «cuerpos o restos»."),
 dict(id="ARG-150-011", estado="MX-QUE", region="Centro", color="rojo", impacto="mediano", fecha="2026-11-10", hora="no fijada", mu=0, he=0, cu=2, hk=10,
  ent="Querétaro", mun="San Juan del Río (San Pablo Potrerillos)", dia="PUB. 10-NOV, POR RUTA",
  fecha_txt="publicación 10-nov, por ruta; día del hallazgo no fijado",
  title="QUERÉTARO · SAN JUAN DEL RÍO — DOS HOMBRES MUERTOS EN SAN PABLO POTRERILLOS; CAUSA CONTRADICHA",
  hecho="San Juan del Río · <code>SAN PABLO POTRERILLOS, POR TITULAR</code> · publicación 10-NOV, por ruta (Al Minuto 2026/11/10: «localizan a dos hombres sin vida en San Pablo Potrerillos»; Expreso Querétaro 2026/11/10) · día del hallazgo no fijado · " + RET + " · <b>2 hombres muertos</b>, por titular · <code>CAUSA CONTRADICHA</code>: «riña deja 2 muertos», por titular (Quadratín Querétaro; Pensador Queretano), frente a señales de tortura y heridas de bala, " + RES + " (🔴 homicidio múltiple) · la FGE asumió las diligencias, " + RES + " · " + NOD,
  panel="<b>2 hombres muertos</b>; causa contradicha (riña o ataque)", inst=SB, nac="N+", conf="★★★☆☆",
  campo="causa contradicha; día del hallazgo no fijado; ninguna fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["Al Minuto (2026/11/10)", "Expreso Querétaro (2026/11/10)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Pablo Potrerillos no figura en las cinco ediciones previas. Causa no informada por autoridad: va a «cuerpos o restos». «Macabro hallazgo» (Noticias de Querétaro), citado por el equipo, no se localizó en procedencia: retirado."),
 # ======================= AMARILLOS
 dict(id="ARG-150-012", estado="MX-GUA", region="Occidente", color="amarillo", impacto="grande", fecha="2026-11-12", hora="noche del 12 o madrugada del 13 (solo por resumen)", mu=0, he=0, cu=0, hk=23,
  ent="Guanajuato", mun="Silao (La Aldea)", dia="12 O 13-NOV; PUB. 13-NOV, POR RUTA",
  fecha_txt="noche del 12 o madrugada del 13-nov, contradicho; publicación 13-nov, por ruta",
  title="GUANAJUATO · SILAO — FUERZAS ESTATALES Y FEDERALES ACUDEN A UNA DENUNCIA EN LA ALDEA Y SON ATACADAS: SEIS AGRESORES ABATIDOS",
  hecho="Silao · <code>LA ALDEA, CALLE SOLIDARIDAD, POR TITULAR</code> (AM 2026/11/13) · <code>DÍA CONTRADICHO</code>: noche del jueves 12 o madrugada del viernes 13, " + RES + " · publicación 13-NOV, por ruta · Secretaría de Seguridad y Paz: denuncia anónima al 089; fuerzas estatales, Ejército y GN acuden y son atacadas desde un inmueble, " + RES + " (🟡 confrontación derivada de una acción de la autoridad) · <b>6 presuntos integrantes del CJNG abatidos</b>, por titular (Latinus 2026/11/13; La Silla Rota 2026/11/13) · ningún elemento lesionado, " + RES + " · aseguramiento: <a href=\"#ARG-150-020\"><code>ARG-150-020</code></a>",
  panel="Operativo repelido: <b>6 agresores abatidos</b>", inst=SB, nac="Latinus · La Silla Rota · La Jornada", conf="★★★☆☆",
  campo="quién inició, según la versión oficial, solo por resumen; día contradicho", I=0, N=3, R=2, A=0,
  fechadas=["Latinus (2026/11/13)", "La Silla Rota (2026/11/13)", "AM (2026/11/13)", "La Jornada (2026/11/14)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — aseguramiento en <a href=\"#ARG-150-020\"><code>ARG-150-020</code></a>",
  desl="Los abatidos no mueven el color ni se suman a «muertos por agresión». Silao en el índice: ARG-146-005 y anteriores: otros hechos. Un elemento de la GN muerto «hace dos días en el mismo lugar»: un solo resumen, no verificado, no se ficha."),
 dict(id="ARG-150-013", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-11", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Guanajuato", mun="Irapuato (La Trinidad de Temascatío)", dia="11-NOV, BOLETÍN FEDERAL",
  fecha_txt="11-nov, por ruta (AM 2026/11/11) y boletín federal",
  title="GUANAJUATO · IRAPUATO — GUARDIA NACIONAL Y EJÉRCITO REPELEN UN ATAQUE ARMADO EN LA TRINIDAD DE TEMASCATÍO",
  hecho="Irapuato · <code>LA TRINIDAD DE TEMASCATÍO</code>, boletín federal de acciones del 11-NOV republicado (Milenio, ruta con el día; Certeza Diario) · «Guardia Nacional y Ejército repelen ataque armado y detienen a seis personas», por titular (Diario de Yucatán 2026/11/12) · atacados en un recorrido de reconocimiento, según Defensa, " + RES + " · <code>QUIÉN INICIÓ NO DETERMINADO POR TITULAR</code> (🟡 con reserva: sube a 🔴 si se acredita la agresión a personal en patrullaje) · <b>1 agresor abatido</b>, por titular (AM 2026/11/11: «enfrentamiento en límites de Irapuato y Salamanca deja un presunto agresor muerto y detenidos»; Correo 2026/nov/12: «… y abaten a uno») · detención: <a href=\"#ARG-150-021\"><code>ARG-150-021</code></a>",
  panel="Agresión a la GN y al Ejército, repelida: <b>1 agresor abatido</b>", inst="Gabinete de Seguridad <span class=\"muted-note\">(boletín republicado; texto no leído)</span>", nac="Milenio · Infobae", conf="★★★☆☆",
  campo="quién inició solo por resumen; boletín leído solo a través de republicadores", I=1, N=2, R=3, A=0,
  fechadas=["AM (2026/11/11)", "Milenio (boletín de acciones del 11-nov, por ruta)", "Diario de Yucatán (2026/11/12)", "Correo (2026/nov/12)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — aseguramiento en <a href=\"#ARG-150-021\"><code>ARG-150-021</code></a>",
  desl="Temascatío no figura en las cinco ediciones previas. «9 largas y 4 cortas en un inmueble» (Infobae): cifras de Silao, mezcla de hechos, no se usan."),
 dict(id="ARG-150-014", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-10", hora="mañana (solo por resumen)", mu=1, he=0, cu=0, hk=9,
  ent="Michoacán", mun="Morelia (Primo Tapia Poniente)", dia="10-NOV, POR RUTA",
  title="MICHOACÁN · MORELIA — ASESINAN A BALAZOS A UN EXCOMISARIO REGIONAL DE SEGURIDAD DE URUAPAN",
  hecho="Morelia · <code>COL. PRIMO TAPIA PONIENTE</code>, " + RES + " · martes 10-NOV, por ruta (Grupo Marmor 2026/11/10: «asesinan en Morelia a excomisario de Seguridad Pública de la región Uruapan»; Publimetro 2026/11/10) · mañana, " + RES + " · <b>1 muerto</b>, frente a su negocio, " + RES + " · exservidor público sin cargo vigente (🟡 homicidio doloso único) · la FGE ofrecía, desde 2024, recompensa por su captura por secuestro agravado, por titular (Quinto Poder 2026/11/10) · " + NOD,
  panel="<b>Excomisario regional de Uruapan asesinado</b>", inst=SB, nac="Publimetro · La Razón · Excélsior", conf="★★★☆☆",
  campo="hora y lugar exacto solo por resumen; ninguna fuente institucional", I=0, N=3, R=2, A=0,
  fechadas=["Quinto Poder (2026/11/10)", "Publimetro (2026/11/10)", "Grupo Marmor (2026/11/10)", "La Razón (2026/11/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Agravante de servidor público: no aplica, cargo no vigente. Primo Tapia no figura en las cinco ediciones previas. Identidad: medios, no se reproduce."),
 dict(id="ARG-150-015", estado="MX-MEX", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-13", hora="~04:30 (solo por resumen)", mu=1, he=1, cu=0, hk=4,
  ent="Estado de México", mun="Naucalpan (San Bartolo, base de la Ruta 05)", dia="13-NOV, POR RUTA",
  title="ESTADO DE MÉXICO · NAUCALPAN — ATAQUE A CHOFERES DE LA RUTA 05 EN GUSTAVO BAZ: UN MUERTO Y UN HERIDO",
  hecho="Naucalpan · <code>SAN BARTOLO, CALZ. GUSTAVO BAZ, BASE DE LA RUTA 05, POR TITULAR</code> · viernes 13-NOV, por ruta (El Monitor 2026/11/13: «ataque armado contra transportistas en Naucalpan deja un muerto y un lesionado»; Heraldo de México 2026/11/13) · ~04:30, " + RES + " · <b>1 chofer muerto y 1 herido</b>, por titular (🟡 homicidio doloso único) · casquillos: entre 11 y 13, cifra variable · " + NOD,
  panel="Ataque a choferes de transporte público: <b>1 muerto y 1 herido</b>", inst=SB, nac="Heraldo de México · López Dóriga", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=3, A=0,
  fechadas=["El Monitor (2026/11/13)", "Heraldo de México (2026/11/13)", "Cúspide (2026/11/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="Extorsión al transporte: no acreditada por autoridad; sube a 🔴 solo si se acredita un ataque coordinado. ARG-148-004 (Naucalpan, «El General»): otro hecho."),
 dict(id="ARG-150-016", estado="MX-MEX", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-13", hora="no fijada", mu=1, he=1, cu=0, hk=12,
  ent="Estado de México", mun="Tlalnepantla (El Arenal)", dia="13-NOV, POR RUTA",
  title="ESTADO DE MÉXICO · TLALNEPANTLA — ATAQUE ARMADO EN EL ARENAL: UN MUERTO Y UN HERIDO",
  hecho="Tlalnepantla · <code>COL. EL ARENAL, POR TITULAR</code> · viernes 13-NOV, por ruta (Heraldo de México, edición Edomex, 2026/11/13: «ataque armado en Tlalnepantla: matan a un hombre y dejan a otro herido») · <b>1 muerto y 1 herido</b>, por titular (🟡 homicidio doloso único) · " + FU + " · " + NOD,
  panel="Ataque armado: <b>1 muerto y 1 herido</b>", inst=SB, nac="—", conf="★★☆☆☆",
  campo="fuente única; hora no fijada", I=0, N=0, R=1, A=0,
  fechadas=["Heraldo de México Edomex (2026/11/13)"], estatus="Pendiente de corroboración", arm=None,
  desl="«Arenal» en el índice: Acapulco (ARG-110-REC-002) y El Arenal, Jal. (visto en este corte): otros lugares."),
 dict(id="ARG-150-017", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-14", hora="no fijada", mu=1, he=0, cu=0, hk=6,
  ent="Baja California", mun="Tijuana (Nuevo Milenio)", dia="PUB. 14-NOV, POR RUTA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS A UN HOMBRE DENTRO DE UNA VIVIENDA EN NUEVO MILENIO",
  hecho="Tijuana · <code>COL. NUEVO MILENIO, POR TITULAR</code> · publicación sábado 14-NOV, por ruta (El Imparcial 2026/11/14: «asesinan a balazos a hombre dentro de una vivienda en Nuevo Milenio») · " + FR + " · <b>1 muerto</b>, hombre de unos 45 años, " + RES + " (🟡 homicidio doloso único) · «asesinan a balazos a hombre al interior de un domicilio en Nuevo Milenio», por titular (Periodismo Negro 2026/11/14) · " + NOD,
  panel="<b>Hombre asesinado a balazos</b> dentro de una vivienda", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada frente al cierre de las 10:09; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["El Imparcial (2026/11/14)", "Periodismo Negro (2026/11/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="Si resulta posterior a las 10:09 del 14, se retira de este total y pasa a ARGOS 151. Nuevo Milenio no figura en las cinco ediciones previas."),
 # ======================= VERDES
 dict(id="ARG-150-018", estado="MX-JAL", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-12", hora="no fijada", mu=0, he=0, cu=0, hk=13,
  ent="Jalisco", mun="Ocotlán", dia="12-NOV, POR RUTA",
  title="JALISCO · OCOTLÁN — DETENIDO UN HOMBRE TRAS LA AGRESIÓN AL EJÉRCITO; ARMAMENTO DE ALTO PODER SIN CIFRA FIJADA",
  hecho="Ocotlán · jueves 12-NOV, por ruta (Grupo Marmor 2026/11/12) · <b>1 detenido</b>, de nacionalidad hondureña, por titular (Tribuna de la Bahía: «enfrentamiento en Ocotlán: dos muertos, un detenido»; Milenio: «deja muertos y detenidos») y Defensa, " + RES + " · armamento: 2 armas largas, 1 ametralladora 5.56 mm, 1 fusil Barrett calibre .50, 2 granadas de 40 mm y 1 vehículo con blindaje artesanal, " + RES + ": <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · delito: <a href=\"#ARG-150-003\"><code>ARG-150-003</code></a>",
  panel="<b>1 detenido</b>; armamento de alto poder sin cifra por titular", inst="Defensa <span class=\"muted-note\">(solo por resumen)</span>", nac="Milenio · El Universal", conf="★★★☆☆",
  campo="armamento solo por resumen; cifra de detenido por titular de medio y Defensa por resumen", I=1, N=2, R=1, A=0,
  fechadas=["Grupo Marmor (2026/11/12)", "Lo de Hoy (2026/11/13)"], estatus="Parcialmente corroborado", arm="ARG-150-ARM-005",
  desl="Delito y detención en la misma ventana: dos fichas. Identidad del detenido: no se reproduce."),
 dict(id="ARG-150-019", estado="MX-VER", region="Golfo", color="verde", impacto="mediano", fecha="2026-11-12", hora="no fijada", mu=0, he=0, cu=0, hk=6,
  ent="Veracruz", mun="Tuxpan", dia="12-NOV, POR RUTA",
  title="VERACRUZ · TUXPAN — CUATRO DETENIDOS POR EL ATAQUE AL HOSPITAL, UNO DE ELLOS ELEMENTO DE LA MARINA EN ACTIVO",
  hecho="Tuxpan · publicación 12-NOV, por ruta · <b>4 detenidos</b>, por titular (Golpe Político 2026/11/12: «detienen a cuatro personas por ataque armado en centro médico de Tuxpan»; La Silla Rota 2026/11/12; MVS 2026/11/12) · «la Fiscalía informó cuatro detenidos», " + RES + " · <b>un elemento de la Marina en activo</b>, por titular (El Buen Tono: «detienen a marino en activo por presunta participación en homicidio dentro de una clínica de Tuxpan»); la Semar lo confirmó, " + RES + " · primeras versiones, «tres detenidos, dos marinos» (Proyecto Puente 2026/11/12): superadas · detenidos tras una persecución, " + RES + " · Fiscalía Regional de Tuxpan, " + RES + " · armamento: no publicado · delito: <a href=\"#ARG-150-004\"><code>ARG-150-004</code></a>",
  panel="<b>4 detenidos</b> por el ataque al hospital; uno, marino en activo", inst=SB, nac="La Silla Rota · MVS · El Universal", conf="★★★☆☆",
  campo="cifra de detenidos de la Fiscalía y confirmación de la Semar solo por resumen", I=0, N=3, R=3, A=0,
  fechadas=["Golpe Político (2026/11/12)", "La Silla Rota (2026/11/12)", "MVS (2026/11/12)", "Hoy Xalapa (2026/11/13)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — detención sin aseguramiento de armamento publicado; fuera del conteo de detenidos en aseguramiento",
  desl="Delito y detención en la misma ventana: dos fichas. Identidades: medios, no se reproducen."),
 dict(id="ARG-150-020", estado="MX-GUA", region="Occidente", color="verde", impacto="grande", fecha="2026-11-12", hora="noche del 12 o madrugada del 13 (solo por resumen)", mu=0, he=0, cu=0, hk=23,
  ent="Guanajuato", mun="Silao (La Aldea)", dia="12 O 13-NOV; PUB. 13-NOV, POR RUTA",
  fecha_txt="noche del 12 o madrugada del 13-nov, contradicho; publicación 13-nov, por ruta",
  title="GUANAJUATO · SILAO — ASEGURAN ARMAS Y VEHÍCULOS TRAS EL ENFRENTAMIENTO DE LA ALDEA",
  hecho="Silao · <code>LA ALDEA</code> · publicación 13-NOV, por ruta · «aseguran armas», por titular (Vanguardia; La Silla Rota) · <b>13 armas</b> (9 largas y 4 cortas), 3 vehículos, chalecos, cascos, cargadores y cartuchos, " + RES + ": <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> (titular con la cifra no localizado en procedencia) · prendas con insignias de grupos criminales, " + RES + " · Secretaría de Seguridad y Paz, Ejército y GN · <b>ningún detenido publicado</b> · enfrentamiento: <a href=\"#ARG-150-012\"><code>ARG-150-012</code></a>",
  panel="<b>Armas aseguradas</b>; cifra solo por resumen", inst=SB, nac="Latinus · La Silla Rota · Vanguardia", conf="★★★☆☆",
  campo="cifra de armas solo por resumen; ninguna fuente institucional leída", I=0, N=3, R=1, A=0,
  fechadas=["Latinus (2026/11/13)", "La Silla Rota (2026/11/13)", "Proyecto Puente (2026/11/13)"], estatus="Parcialmente corroborado", arm="ARG-150-ARM-001",
  desl="Operativo con enfrentamiento: dos fichas. «Silao, autopista León–Salamanca, 8 largas y 3 cortas» del boletín federal del 9-nov: otro hecho, visto en armamento."),
 dict(id="ARG-150-021", estado="MX-GUA", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-11", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Guanajuato", mun="Irapuato (La Trinidad de Temascatío)", dia="11-NOV, BOLETÍN FEDERAL",
  fecha_txt="acciones del 11-nov, boletín federal; publicación 12-nov, por ruta",
  title="GUANAJUATO · IRAPUATO — SEIS DETENIDOS Y ARMAS ASEGURADAS EN LA TRINIDAD DE TEMASCATÍO",
  hecho="Irapuato · <code>LA TRINIDAD DE TEMASCATÍO</code> · boletín federal de acciones del 11-NOV republicado (Milenio; Certeza Diario) · <b>6 detenidos</b>, por titular (Diario de Yucatán 2026/11/12: «… repelen ataque armado y detienen a seis personas») y boletín · 5 largas, 1 corta, 6 cargadores, 155 cartuchos, 4 chalecos, 2 motocicletas y 2 vehículos, " + RES + ": n/d · GN y Ejército · agresión: <a href=\"#ARG-150-013\"><code>ARG-150-013</code></a>",
  panel="<b>6 detenidos</b>; armas sin desglose por titular", inst="Gabinete de Seguridad <span class=\"muted-note\">(boletín republicado; texto no leído)</span>", nac="Milenio", conf="★★★☆☆",
  campo="desglose de armamento solo por resumen; boletín leído solo a través de republicadores", I=1, N=1, R=1, A=0,
  fechadas=["Milenio (boletín de acciones del 11-nov, por ruta)", "Diario de Yucatán (2026/11/12)"], estatus="Parcialmente corroborado", arm="ARG-150-ARM-004",
  desl="Republicadores del mismo boletín: una fuente. Operativo con enfrentamiento: dos fichas."),
 dict(id="ARG-150-022", estado="MX-CHP", region="Sureste", color="verde", impacto="grande", fecha="2026-11-10", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Chiapas", mun="Benemérito de las Américas (col. Bellavista)", dia="10-NOV, BOLETÍN FEDERAL",
  fecha_txt="acciones del 10-nov, boletín federal; publicación 11-nov, por ruta",
  title="CHIAPAS · BENEMÉRITO DE LAS AMÉRICAS — CATORCE DETENIDOS Y DOCE ARMAS LARGAS ASEGURADAS",
  hecho="Benemérito de las Américas · camino de terracería de la col. Bellavista, " + RES + " · boletín federal de acciones del 10-NOV republicado (Milenio, ruta con el día; RED113; Tallapolítica) · <b>14 detenidos y 12 armas largas</b>, por titular (La Nigua: «operativo en Chiapas detiene a 14 y asegura 12 armas largas»; Rotativo: «… 12 armas»); 14 detenidos, por ruta (Alerta Chiapas 2026/11/11; Diario Puntual 2026/11/11) · 97 cargadores, 882 cartuchos y 17 chalecos tácticos, boletín, " + RES + ": n/d · Defensa, Marina, SSPC, FGR, GN, Policía Estatal y Fuerza de Reacción Inmediata Pakal, " + RES + " · vínculo con el Cártel de Sinaloa atribuido por el Gabinete, " + RES,
  panel="<b>14 detenidos y 12 armas largas</b>", inst="Gabinete de Seguridad <span class=\"muted-note\">(boletín republicado; texto no leído)</span>", nac="Milenio · Heraldo de México", conf="★★★☆☆",
  campo="cargadores y cartuchos solo por resumen; boletín leído solo a través de republicadores", I=1, N=2, R=3, A=0,
  fechadas=["Milenio (boletín de acciones del 10-nov, por ruta)", "Red Metropolitana (2026/11/11)", "Heraldo de México (2026/11/11)", "Alerta Chiapas (2026/11/11)"], estatus="Parcialmente corroborado", arm="ARG-150-ARM-002",
  desl="Benemérito en el índice: ARG-119-ARM-011 (10-sep, 2 cortas, 1 detenido): otro hecho. Republicadores del boletín: una fuente."),
 dict(id="ARG-150-023", estado="MX-VER", region="Golfo", color="verde", impacto="mediano", fecha="2026-11-10", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Veracruz", mun="Chacaltianguis", dia="10-NOV, BOLETÍN FEDERAL",
  fecha_txt="acciones del 10-nov, boletín federal",
  title="VERACRUZ · CHACALTIANGUIS — MARINA Y POLICÍA ESTATAL ASEGURAN CUATRO ARMAS LARGAS, DOS GRANADAS Y UN LANZAGRANADAS",
  hecho="Chacaltianguis · Marina y Policía Estatal · boletín federal de acciones del 10-NOV republicado (Milenio, ruta con el día; RED113); inclusión del caso en ese boletín, " + DSR + " · <b>4 armas largas, 39 cargadores, 2 granadas y 1 lanzagranadas</b>, por titular (Poder y Crítica: «cuatro armas largas, 39 cargadores, dos granadas y un lanzagranadas integran el arsenal asegurado en Chacaltianguis») · 3 vehículos y 8 chalecos tácticos, " + RES + " · " + NOD,
  panel="<b>4 armas largas, 2 granadas y 1 lanzagranadas</b>", inst="Gabinete de Seguridad <span class=\"muted-note\">(boletín republicado; texto no leído)</span>", nac="Milenio", conf="★★★☆☆",
  campo="día del aseguramiento fijado solo por el boletín; titular del medio sin fecha en la ruta", I=1, N=1, R=3, A=0,
  fechadas=["Milenio (boletín de acciones del 10-nov, por ruta)", "Potosí Noticias (2026/11/12)"], estatus="Parcialmente corroborado", arm="ARG-150-ARM-003",
  desl="Chacaltianguis no figura en las cinco ediciones previas. Posible reiteración en el boletín del 11-nov, " + RES + ": se cuenta una sola vez."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-150-REC-001", estado="MX-BCN", region="Noroeste", fecha="2026-11-06", hora="16:00 a 22:00 (solo por resumen)", orig="ARGOS 149", col_orig="rojo", mu=3, he=2, cu=0,
  ent="Baja California", mun="Tecate (Los Encinos)", dia="6-NOV, SOLO POR RESUMEN",
  title="BAJA CALIFORNIA · TECATE — ATAQUE ARMADO EN LOS ENCINOS: TRES MUERTOS Y DOS HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 149</code> · Tecate · <code>LOS ENCINOS</code>, " + RES + " · viernes 6-NOV, noche, " + DSR + "; publicación 7-NOV, por ruta · entre las 16:00 y las 22:00, " + RES + ": posterior a las 07:30 del 6 · <b>3 muertos y 2 heridos</b>, por titular (Punto Norte 2026/11/07: «acribillan a 5 personas en Tecate: 3 muertos y 2 heridos»); heridos «graves»: el saldo puede subir (🔴 homicidio múltiple) · jornada de «cinco homicidios y una persona lesionada» en dos ataques, por titular (Zeta): <code>COMPOSICIÓN NO RESUELTA</code> · «cuatro detenidos por asesinato múltiple en una taquería de Tecate» (Uniradio, sin fecha): <code>POSIBLE DUPLICIDAD — NO SE INTEGRA</code>",
  panel="<b>Ataque armado: 3 muertos y 2 heridos</b>", inst=SB, nac="—",
  conf="★★★☆☆", campo="día y hora solo por resumen; composición de la jornada no resuelta; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Punto Norte (2026/11/07)", "Zeta (2026/11)"],
  desl="Visto sin ruta en ARGOS 149 (rojos sin ruta: «Tecate, cinco homicidios»). Masacre de octubre (ARG-142 y ARG-143-REC-001) y ARG-149-017 (fusiles, 8-nov): otros hechos."),
 dict(id="ARG-150-REC-002", estado="MX-OAX", region="Sureste", fecha="2026-11-08", hora="noche (solo por resumen)", orig="ARGOS 149", col_orig="rojo", mu=2, he=1, cu=0,
  ent="Oaxaca", mun="San Juan Cacahuatepec", dia="8-NOV, SOLO POR RESUMEN",
  title="OAXACA · SAN JUAN CACAHUATEPEC — ATAQUE ARMADO: DOS MUERTOS Y UN HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 149</code> · San Juan Cacahuatepec · domingo 8-NOV, noche, " + DSR + " · publicación 9-NOV, por ruta (Diario Puntual 2026/11/09: «Ayuntamiento confirma asesinato de hijo de titular del DIF en Oaxaca») · <b>2 muertos y 1 herido</b>, por titular (El Imparcial 2026/11/10: «… ataque deja dos muertos y un herido») · una víctima, hijo de la presidenta del DIF municipal, por titular (🔴 homicidio múltiple) · la FGEO investiga, " + RES + " · 1 detenido según un solo medio, " + RES + ": no se integra",
  panel="<b>Ataque armado: 2 muertos y 1 herido</b>", inst=SB, nac="El Imparcial · Infobae · El Universal",
  conf="★★★☆☆", campo="día solo por resumen; ninguna fuente institucional", I=0, N=3, R=3, A=0,
  fechadas=["Diario Puntual (2026/11/09)", "El Imparcial (2026/11/10)"],
  desl="Visto sin ruta en ARGOS 149. Identidades: medios, no se reproducen."),
 dict(id="ARG-150-REC-003", estado="MX-NLE", region="Noreste", fecha="2026-11-07", hora="~10:30 (solo por resumen)", orig="ARGOS 149", col_orig="rojo", mu=2, he=1, cu=0,
  ent="Nuevo León", mun="Monterrey (taquería)", dia="7-NOV, POR RUTA",
  title="NUEVO LEÓN · MONTERREY — RIÑA CON ARMA BLANCA EN UNA TAQUERÍA: DOS MUERTOS Y UN HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 149</code> · Monterrey · taquería de la col. Valle Verde, " + RES + " · sábado 7-NOV, por ruta (ABC Noticias 2026/11/7; Primera Línea 2026/11/07: «ataque con arma blanca deja dos muertos y un herido en taquería de Monterrey») · ~10:30, " + RES + " · <b>2 muertos y 1 herido</b>, por titular (🔴 homicidio múltiple) · riña entre trabajadores, por titular (Quinta Fuerza): <b>sin vínculo con grupo criminal publicado</b> · audiencia de control de detención el 11-NOV; la Fiscalía de NL buscará homicidio agravado, " + RES + " (MVS 2026/11/11) · detenidos: 2, " + RES,
  panel="<b>Riña con arma blanca: 2 muertos y 1 herido</b>", inst=SB, nac="MVS",
  conf="★★★☆☆", campo="detenidos y hora solo por resumen; ninguna fuente institucional leída", I=0, N=1, R=2, A=0,
  fechadas=["ABC Noticias (2026/11/7)", "Primera Línea (2026/11/07)", "MVS (2026/11/11)"],
  desl="Visto sin ruta en ARGOS 149. ARG-146-013 (Culiacán, otra taquería): otro hecho."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ND_ALL = list(range(10))
ARM = [
 dict(id="ARG-150-ARM-001", ficha="ARG-150-020", estado="MX-GUA", region="Occidente", color="amarillo", ent="Guanajuato", mun="Silao (La Aldea)",
  fecha="2026-11-12", fecha_txt="12 o 13-nov; pub. 13-nov, por ruta", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], integra=False,
  corp="Secretaría de Seguridad y Paz, Ejército y GN <span class=\"muted-note\">(por medios)</span>", conf="Bajo",
  nota="13 armas (9 largas y 4 cortas), cargadores y cartuchos, solo por resumen: CANTIDAD NO DETERMINADA, no se integra; ningún detenido publicado; aseguramiento derivado de enfrentamiento (🟡); ver ARG-150-020",
  fuentes=["Latinus (2026/11/13)", "La Silla Rota (2026/11/13)", "Proyecto Puente (2026/11/13)"]),
 dict(id="ARG-150-ARM-002", ficha="ARG-150-022", estado="MX-CHP", region="Sureste", color="verde", ent="Chiapas", mun="Benemérito de las Américas",
  fecha="2026-11-10", fecha_txt="acciones del 10-nov, boletín federal", hora="no fijada", c=[0, 12, 0, 0, 0, 0, 0, 0, 0, 14], nd=[0, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="Defensa, Marina, SSPC, FGR, GN y Policía Estatal <span class=\"muted-note\">(boletín federal republicado)</span>", conf="Bajo",
  nota="12 largas y 14 detenidos por titular y boletín federal republicado; 97 cargadores y 882 cartuchos, solo por resumen: n/d; ver ARG-150-022",
  fuentes=["Milenio (acciones del 10-nov)", "Red Metropolitana (2026/11/11)", "Heraldo de México (2026/11/11)"]),
 dict(id="ARG-150-ARM-003", ficha="ARG-150-023", estado="MX-VER", region="Golfo", color="verde", ent="Veracruz", mun="Chacaltianguis",
  fecha="2026-11-10", fecha_txt="acciones del 10-nov, boletín federal", hora="no fijada", c=[0, 4, 0, 1, 0, 39, 2, 0, 0, 0], nd=[0, 2, 4, 7, 8, 9], integra=True,
  corp="Marina y Policía Estatal <span class=\"muted-note\">(boletín federal republicado)</span>", conf="Bajo",
  nota="4 largas, 39 cargadores, 2 granadas y 1 lanzagranadas (armamento especial) por titular y boletín; cartuchos no publicados; ningún detenido publicado; ver ARG-150-023",
  fuentes=["Milenio (acciones del 10-nov)", "Poder y Crítica (sin fecha en la ruta)", "Potosí Noticias (2026/11/12)"]),
 dict(id="ARG-150-ARM-004", ficha="ARG-150-021", estado="MX-GUA", region="Occidente", color="amarillo", ent="Guanajuato", mun="Irapuato (La Trinidad de Temascatío)",
  fecha="2026-11-11", fecha_txt="acciones del 11-nov, boletín federal", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 6], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="GN y Ejército <span class=\"muted-note\">(boletín federal republicado)</span>", conf="Bajo",
  nota="6 detenidos por titular y boletín; 5 largas, 1 corta, 6 cargadores y 155 cartuchos, solo por resumen: n/d; aseguramiento derivado de agresión (🟡); ver ARG-150-021",
  fuentes=["Milenio (acciones del 11-nov)", "Diario de Yucatán (2026/11/12)"]),
 dict(id="ARG-150-ARM-005", ficha="ARG-150-018", estado="MX-JAL", region="Occidente", color="rojo", ent="Jalisco", mun="Ocotlán",
  fecha="2026-11-12", fecha_txt="12-nov, por ruta", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="Defensa <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="1 detenido por titular; 2 largas, 1 ametralladora, 1 Barrett .50, 2 granadas de 40 mm y 1 vehículo blindado artesanal, solo por resumen: CANTIDAD NO DETERMINADA; armamento vinculado a un evento de alto impacto (🔴); ver ARG-150-018",
  fuentes=["Grupo Marmor (2026/11/12)", "Tribuna de la Bahía (sin fecha en la ruta)"]),
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
HORAS = 114 + 2 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 16, 0, 1, 0, 39, 2, 0, 0, 21], (TOT, ND)
assert ND == [True, False, True, False, True, False, False, True, True, False], ND
assert cnt == {"rojo": 11, "amarillo": 6, "verde": 6}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (13, 6, 7, 7, 4, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,20", DENS
assert (NAP, NFR, NRET) == (0, 1, 1), (NAP, NFR, NRET)
assert len(ENT) == 12 and len(ENT_ROJO) == 10, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-150-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-150-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-11-09" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-11-09", x["id"]
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
head = head.replace("<title>ARGOS 149 — Reporte Nacional de Seguridad — 2026-11-09</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA SSP Y A LA FGE DE MICHOACÁN EL PARTE DE ZITÁCUARO Y DE TEPALCATEPEC —ARMAMENTO, CALIBRES Y VEHÍCULOS— Y COTEJE LOS CASQUILLOS DE AMBOS ATAQUES</b> (ARG-150-001 y -002).
      <br><b>2. SOLICITE A LA DEFENSA EL PARTE DE OCOTLÁN —QUIÉN INICIÓ, ARMAMENTO ASEGURADO Y SITUACIÓN JURÍDICA DEL DETENIDO— Y VIGILE EL CORREDOR OCOTLÁN–ATOTONILCO EL ALTO</b> (ARG-150-003 y -018).
      <br><b>3. SOLICITE A LA FISCALÍA DE VERACRUZ Y A LA SEMAR LA SITUACIÓN JURÍDICA DE LOS CUATRO DETENIDOS DE TUXPAN, INCLUIDO EL MARINO EN ACTIVO, Y AUDITE LA CUSTODIA DE LESIONADOS POR ARMA DE FUEGO EN HOSPITALES PRIVADOS</b> (ARG-150-004 y -019).
      <br><b>4. SOLICITE A LAS FISCALÍAS DE HIDALGO, GUANAJUATO Y SINALOA LA IDENTIFICACIÓN DE LOS RESTOS DE AJACUBA, IRAPUATO Y LAS VÍBORAS Y SU CRUCE CON FICHAS DE DESAPARICIÓN</b> (ARG-150-008, -009 y -010).
      <br><b>5. SOLICITE A LA SSP DE GUANAJUATO EL INVENTARIO OFICIAL DE LAS ARMAS DE SILAO Y DE TEMASCATÍO Y SU INGRESO AL REGISTRO BALÍSTICO</b> (ARG-150-020 y -021).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>9-nov 16:07 → 14-nov 10:09 CDMX</b> (<b>{DUR}</b>) · lun 9 (desde 16:07) · mar 10 · mié 11 · jue 12 · vie 13 · sáb 14 (hasta 10:09) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto de la ventana de ARGOS 149</b>, atenuadas, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: desglose en su página; armamento especial: {tv(3)} (lanzagranadas) · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas, incluida la acompañante de Tuxpan, muerta el 13-nov; <b>heridos</b>: {HE} · <b>cuerpos o restos</b>: {CU} (Ajacuba 3, Irapuato 2 cráneos, San Juan del Río 2), sin causa de muerte informada por autoridad; Las Víboras, sin cifra · <b>abatidos por la fuerza pública</b>: 9, por titular (Silao 6, Ocotlán 2, Temascatío 1), fuera de «muertos por agresión» · <b>heridos contradichos fuera del cálculo</b>: Zitácuaro y el tercer herido de Tepalcatepec y de Ocotlán · <b>marcas</b>: {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (Tijuana, día de cierre) · <b>totales sujetos a {NRET} cláusula de retiro</b> (San Juan del Río: día del hallazgo no fijado frente a las 16:07 del 9) · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos y {HE_REC} heridos, por titular.
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «Michoacán llega a 36 policías asesinados» (La Silla Rota 2026/11/13) · «suman 21 agentes asesinados en el año» en Guanajuato (Proyecto Puente 2026/11/09) · Tabasco, «22 detenidos» del 9 al 12-nov (Diario de Tabasco 2026/11/13) · Quintana Roo, «mil personas heridas por arma de fuego» en 2026 (PorEsto 2026/11/13) · 2,395 detenidos por extorsión de julio de 2025 a octubre de 2026, mañanera del 10-nov, por titular de medio (Tiempo).
    <br><code>ROJOS SIN RUTA FECHADA — CANDIDATOS NO FICHADOS</code>: <b>Atotonilco el Alto, Jal.</b>: quema de un tractocamión y un camión y bloqueos tras Ocotlán, 12-nov {RES}; García Harfuch «descarta narcobloqueos», por titular (El Universal) · <b>El Arenal, Jal.</b>: dos jóvenes desaparecidos en Zapopan, hallados sin vida, domingo 8 {RES}: de la ventana de ARGOS 149 · <b>Silao, La Aldea</b>: elemento de la GN muerto días antes, un solo resumen · <b>Viesca, Coah.</b>: fosas, sin fecha · <b>Reynosa, Puerta Sur / Nuevo México ITAVU</b>: hallazgos del 4 al 6-nov, {RES}, sin ruta con día · <b>Colima</b>: enfrentamiento con 3 muertos y 15 detenidos, sin fecha.
    <br><b>Vistos, fuera de totales</b> (🟡 sin ruta propia o con fuente agregada): Mazatlán, Arboledas Infonavit (adulto mayor muerto y nieto herido) y Culiacán (adolescente; hombre en Infonavit Humaya), martes 10, nota agregada · Culiacán, joven privado de la libertad en Villa Bonita y hallado sin vida en la col. Universitaria (Luz Noticias 2026-11-13) · Hermosillo, Álvaro Obregón (miércoles 11, {RES}) · Santo Domingo Tehuantepec, conductor (Diario de Yucatán 2026/11/13) · Iztapalapa, El Mirador (13-nov, no verificado) · Puebla, Guadalupe Hidalgo (1 muerto el 9 y el 10, sin hora) · Mamantel, Camp. (sin ruta) · <b>ajeno</b>: Puebla, ocho bloqueos de familiares de internos del penal de San Miguel (10-nov): protesta, sin quema de vehículos, por titular (Reto Diario 2026/11/10): no es narcobloqueo.
    <br><code>FE DE ERRATAS — ARGOS 149</code>: <b>tres rojos de su ventana se recuperan</b> (Tecate, San Juan Cacahuatepec y Monterrey): semáforo corregido de 149, <b>10 rojos, 7 amarillos, 7 verdes</b> (cálculo propio) · <b>ARG-149-009</b>: saldo fijado en <b>1 muerto y 1 herido</b> (Tiempo 2026-11-08; La Paradoja 2026/11): se retira «saldo contradicho» · <b>ARG-149-010 y -011</b>: dejan de ser fuente única (Medios Obson y Dossier Político 2026/11/07; PSN 2026/11/07 y Diario Tijuana 2026/11): confianza ★★★☆☆ · <b>ARG-149-005</b>: «del supuesto rescate al escape», por titular (Infobae 2026/11/10): contradicción vigente · <b>rojos sin ruta de 149 retirados</b>: Huaquechula (julio), Cañada Morelos (25-jun; e-consulta 2026-06-25) y Doctor Coss (junio–julio) · <b>candidato de sentencia «Ramos Arizpe»</b>: es General Cepeda, publicada el 19-oct (Red Metropolitana 2026/10/19) y republicada el 8-nov: se retira.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>«El Panda», Coatzacoalcos</b>: vinculado a proceso por desaparición cometida por particulares y homicidio calificado, por titular (La Silla Rota 2026/11/10; Infobae 2026/11/11) · <b>ARG-149-014 / -018 (Zapopan, «R2»)</b>: 15 de los 20 detenidos liberados con medidas cautelares, {RES} · <b>ARG-147-001 (Cuernavaca)</b>: detenido el presunto autor material en Xochitepec, 11 o 12-nov, {RES} · <b>Matamoros (ARG-144-008)</b>: tres policías declaran por los disparos desde el helicóptero, por titular (Elefante Blanco 2026/11/09); sin detenidos · <b>ARG-146-011 (Mexicali)</b>: nuevos restos en la jornada de búsqueda del Miguel Alemán, por titular (El Imparcial 2026/11/12), sin cifra · Rioverde, SLP: vinculación a proceso (12-nov) · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-150-{i:03d}"]) for i in (1, 2, 3, 5, 6))
co2 = "\n".join(ficha(byid[f"ARG-150-{i:03d}"]) for i in (4, 7, 8, 9, 10, 11))
co2b = "\n".join(ficha(byid[f"ARG-150-{i:03d}"]) for i in (12, 13, 14, 15, 16, 17))
co2c = "\n".join(ficha(byid[f"ARG-150-{i:03d}"]) for i in (18, 19, 20, 21, 22, 23))
co3 = "\n".join(ficha(rbyid[f"ARG-150-REC-{i:03d}"], True) for i in (1, 2, 3))
assert sorted(re.findall(r'id="(ARG-150-0\d\d)"', co1 + co2 + co2b + co2c)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-150-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
DSA = "Benemérito 14 y Temascatío 6 (boletín federal y titular) · Ocotlán 1 (titular) · Tuxpan 4: sin aseguramiento de armas, fuera de este conteo"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), "Silao 4 y Temascatío 1, solo por resumen: n/d"),
 tile(1, "Armas largas", tv(1), "Benemérito 12 y Chacaltianguis 4, por titular"),
 tile(2, "Sin categoría", tv(2), "Silao: 13, solo por resumen: no se integra"),
 tile(3, "Cartuchos", tv(4, fmt), "Benemérito 882 y Temascatío 155, solo por resumen: n/d"),
 tile(4, "Cargadores", tv(5), "Chacaltianguis, por titular; Benemérito 97, solo por resumen"),
 tile(5, "Granadas", tv(6), "Chacaltianguis, por titular; Ocotlán 2 de 40 mm, solo por resumen"),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), "Chacaltianguis: 1 lanzagranadas, por titular; Ocotlán, Barrett .50, solo por resumen"),
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
    <b>Lectura regional</b>: Occidente, 7 detenidos (Guanajuato 6, Jalisco 1), sin arma integrada; Sureste, 12 largas y 14 detenidos (Chiapas); Golfo, 4 largas, 1 lanzagranadas, 2 granadas y 39 cargadores (Veracruz); Noroeste, Noreste y Centro, sin arma integrada. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: Ocotlán (ARG-150-018): 2 largas, 1 ametralladora 5.56 mm, 1 Barrett .50, 2 granadas de 40 mm y vehículo con blindaje artesanal, {RES} · Silao (ARG-150-020 / ARM-001): 13 armas, 9 largas y 4 cortas, {RES}: fila atenuada, no integrada.
    <br><code>VISTOS, NO INTEGRADOS — BOLETÍN FEDERAL REPUBLICADO, CIFRAS SOLO POR RESUMEN</code>: <b>acciones del 9-nov</b> (<code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code>; si son anteriores a las 16:07, de la ventana de ARGOS 149): Silao, autopista León–Salamanca, 5 detenidos, 8 largas y 3 cortas · Concordia, Sin., 3 detenidos, 6 largas y 650 cartuchos · Santa Isabel, Chih., 4 detenidos, 19 cargadores y 280 cartuchos · Mazatlán, 3 armas y un aditamento lanzagranadas · Jonuta, Tab., 5 detenidos (= Potosí Noticias 2026/11/13: <code>POSIBLE DUPLICIDAD</code>) · <b>acciones del 11-nov</b>: Nuevo Laredo, 2 detenidos, 12 armas con 2 Barrett, 92 cargadores y 2,256 cartuchos · Culiacán, 3 detenidos (un menor), 3 armas, 7 cargadores y 209 cartuchos · <b>acciones del 12-nov</b>: Nuevo Laredo, Villas de San Miguel, 2 largas y 58 cargadores (<code>POSIBLE DUPLICIDAD</code> con el del 11) · General Escobedo, NL, 4,220 cartuchos en una transmisión · Guadalupe y Calvo, Chih., 2 detenidos, 2 largas, 14 cargadores y 420 cartuchos · Mazatlán, El Roble, 2 detenidos, 2 largas, 8 cargadores y 210 cartuchos · Aquila y Carácuaro, Mich., laboratorio y precursores (afectación <code>CIFRA CONTRADICHA</code>: 2,540 o 2,638 mdp) · <b>medios</b>: Tenosique, Tab., 5 detenidos y 3 armas, un solo titular (Potosí Noticias 2026/11/10) · Morelia, cateos, 2 detenidos, armas contradichas · Chihuahua, SSPE, 2 cortas, 4 cargadores y 36 cartuchos, día no fijado.
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
      <tr><td><b>Veracruz</b><br>carretera Isla–Santiago</td><td>Secuestro agravado de nueve víctimas (hechos de enero de 2022); 1 sentenciado, por titular (Hoy Xalapa 2026/11/13; Horacero 2026/11/13: «88 años de prisión para responsable de secuestro agravado…»)</td><td>88 años, por titular</td><td>FGE Veracruz <span class="muted-note">(texto republicado por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · el dominio de la fiscalía no devolvió el boletín; fecha de la sentencia no fijada; término «sentencia condenatoria» {RES}</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>Monterrey</td><td>Homicidio (hecho del 25-jun-2025); 1 sentenciado, por titular (MVS 2026/11/13: «sentencian a casi 26 años de prisión a hombre por asesinato en Monterrey»)</td><td>«Casi 26 años», por titular</td><td>Fiscalía de NL <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín del dominio; pena exacta y tribunal no leídos</td><td>Bajo</td></tr>
      <tr><td><b>Tabasco</b><br>Jalpa de Méndez</td><td>Pederastia agravada; boletín FGET 5119, {RES}</td><td>30 años, {RES}</td><td>FGE Tabasco <span class="muted-note">(listado del dominio; URL individual no indexada)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code>; texto no leído</td><td>Bajo</td></tr>
      <tr><td><b>Fuera de ventana</b></td><td>Apodaca, FGR, 83 migrantes (6-nov) · FGR Guanajuato, «más de 17 años» (6-nov) · «El Mochaorejas», 50 años (Crónica e Infobae 2026/11/08) · Champotón, 66 años 8 meses (PorEsto 2026/11/6) · Oaxaca, 157 años (Primera Línea 2026/11/04) · Palenque, 65 años (4-nov) · Paraíso, FGR, 2 años o 2 años 8 meses (5-nov, {RES}) · balances de la FGE Veracruz (24 y 172 sentencias, agregados)</td><td>—</td><td>FGR y fiscalías estatales <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicados antes de la ventana o agregados sin caso identificable</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio · comunicados vistos solo en resúmenes y titulares de medios</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>22 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Son, Chih · Tamps, NL, Coah, SLP, Zac · Nay, Ags, Gto, Mich · Hgo, Qro, Mor · Ver, Tab · Oax, Chis, Gro, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada · Tabasco: boletín 5119, {RES}</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>22</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio de la fiscalía no confirmado</b></td><td>Camp (incluida en las 10 <code>NO REVISADA</code>)</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>10</b>: BCS, Sin, Dgo · Jal, Col · CDMX, Edomex, Pue, Tlax · Camp</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 14-nov 10:09: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 18 entidades; solo consulta amplia en 14 —BCS, Dgo · Tamps, Coah · Col, Nay, Ags · Edomex, Pue, Mor, Hgo · Tab · Camp, Yuc— · <b>armamento: 19 de 32 por dominio oficial</b> —BC, BCS, Son, Chih · SLP · Jal, Nay, Ags, Gto · CDMX, Edomex, Pue, Mor, Tlax, Hgo, Qro · Ver · Oax, QRoo—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (13): Sin, Dgo · NL, Tamps, Coah, Zac · Mich, Col · Tab · Chis, Gro, Camp, Yuc</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 6, 7 y 8-nov</b>: <code>gob.mx/sspc</code> indexado y segundo republicador (RED113), además de Milenio · <b>acciones del 9-nov</b>: <code>gob.mx/sspc</code> indexado; RED113; Certeza Diario; contenido {RES}; día de apertura sin hora (vistos en armamento) · <b>del 10, 11 y 12-nov</b>: por republicadores (Milenio, RED113, Tallapolítica, Hoja de Ruta, Ultranoticias, SICOM, Certeza Diario); alimentan ARG-150-013, -021, -022 y -023 · <b>acciones del 13-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio y al cierre · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 14-NOV 10:09: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Once rojos propios en diez entidades</b> (cálculo propio). 0,10 rojos por hora (11 en {DUR}), frente a 0,12 en ARGOS 149 corregido (cálculo propio).
      <br><b>2.</b> <b>Cinco de los once rojos tienen por blanco o víctima a fuerzas de seguridad</b>: tres agresiones (Michoacán dos, Jalisco una) y dos policías municipales asesinados (Oaxaca, Estado de México).
      <br><b>3.</b> <b>Tres hallazgos de fosas o restos</b> (Hidalgo, Guanajuato, Sinaloa) y dos homicidios múltiples (Veracruz, Chihuahua); Noreste, sin rojos propios.
      <br><b>4.</b> <b>Violencia operativa</b>: seis amarillos, dos de ellos operativos repelidos en Guanajuato · <b>respuesta institucional</b>: seis verdes; ninguna sentencia integrable (totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()}, 1,4 VECES LA DE ARGOS 149, TRAS CINCO DÍAS SIN EDICIÓN; UN HECHO EN FRONTERA DE VENTANA; BOLETÍN FEDERAL DEL 13-NOV SIN INDEXAR. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. MICHOACÁN: DOS ATAQUES CONTRA POLICÍAS EN TRES DÍAS EN LOS EXTREMOS DEL ESTADO —BASE FIJA EN TIERRA CALIENTE Y PATRULLA EN CARRETERA AL ORIENTE—</b> (ARG-150-001 y -002): modos distintos, fuego contra instalación y ataque por la retaguardia; vínculo entre hechos no acreditado. Línea: <b>vigilar el tramo Zitácuaro–Morelia y los accesos de El Toril</b>.
      <br><b>2. CIÉNEGA DE JALISCO: CÉLULA CON FUSIL CALIBRE .50, GRANADAS DE 40 MM Y BLINDAJE ARTESANAL ENFRENTA AL EJÉRCITO EN ZONA URBANA</b> (ARG-150-003 y -018): armamento solo por resumen; es consistente con capacidad antimaterial; vínculo con la quema de vehículos en Atotonilco el Alto no acreditado. Línea: <b>solicitar el rastreo de origen del Barrett</b>.
      <br><b>3. VERACRUZ NORTE: VÍCTIMA REMATADA EN UN HOSPITAL TRES DÍAS DESPUÉS DE SOBREVIVIR A UN PRIMER ATAQUE, CON UN MARINO EN ACTIVO ENTRE LOS DETENIDOS</b> (ARG-150-004 y -019): participación de un servidor público en activo: hipótesis de investigación, no acreditada judicialmente. Línea: <b>cruzar el registro de servicio del marino detenido con la fecha del primer ataque</b>.
      <br><b>4. ISTMO DE TEHUANTEPEC: POLICÍA MUNICIPAL ASESINADO EN JUCHITÁN UNA SEMANA DESPUÉS DEL ATAQUE AL RESTAURANTE DE UN PERIODISTA</b> (ARG-150-005; antes ARG-149-012): dos blancos ligados a funciones públicas en la misma ciudad; vínculo no acreditado. Línea: <b>solicitar a la FGEO el cotejo balístico de ambos hechos</b>.
      <br><b>5. CUERPOS EN PATIOS Y PREDIOS RURALES: TRES HALLAZGOS EN DOS DÍAS, UNO POR CATEO DERIVADO DE UN REPORTE DE DESAPARICIÓN</b> (ARG-150-008, -009 y -010): Ajacuba muestra el enterramiento dentro de una vivienda habitada; vínculo con redes de desaparición no acreditado. Línea: <b>vigilar inmuebles ligados a denuncias de desaparición en el Valle del Mezquital</b>.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: ATAQUES CONTRA AUTORIDADES", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: HOMICIDIOS MÚLTIPLES, FOSAS Y RESTOS", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA", co2b)
 + page("CRIMEN ORGANIZADO (IV) — ACCIONES INSTITUCIONALES", co2c)
 + page("CRIMEN ORGANIZADO (V) — ALTO IMPACTO DE LA VENTANA DE ARGOS 149: TECATE, SAN JUAN CACAHUATEPEC Y MONTERREY", co3)
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
# la ventana de 150 toca seis fechas de calendario (9, 10, 11, 12, 13 y 14-nov); la plantilla de 149 trae 4
assert script.count("WINDOW_DAYS = 4;") == 1, "plantilla de 149 con WINDOW_DAYS = 4"
script = script.replace("WINDOW_DAYS = 4;", "WINDOW_DAYS = 6;")
assert script.count("WINDOW_DAYS = 6;") == 1 and "WINDOW_DAYS = 4;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
