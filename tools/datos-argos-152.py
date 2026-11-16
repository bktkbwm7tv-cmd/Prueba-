# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 152.
Uso: python3 tools/datos-argos-152.py <plantilla ARGOS 151> <salida>
Ventana: 15-nov 10:24 → 16-nov 10:30 CDMX. Archivo: argos-2026-11-16.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "152", "2026-11-16", "10:30"
CONSULTA = "2026-11-16, última búsqueda 11:30"
DUR = "24 h 06 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 10:24 DEL 15, ES DE LA VENTANA DE ARGOS 151 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
PUB = "Publicado el día de cierre de ARGOS 151 sin hora por fragmento: se integra en esta edición, la primera que lo ve."
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-152-001", estado="MX-NLE", region="Noreste", color="rojo", impacto="grande", fecha="2026-11-16", hora="~01:00 (solo por resumen)", mu=3, he=2, cu=0, hk=1,
  ent="Nuevo León", mun="Galeana (ejido Boca del Refugio)", dia="LUN 16-NOV, POR RUTA",
  fecha_txt="lunes 16-nov, por ruta; ~01:00, solo por resumen",
  title="NUEVO LEÓN · GALEANA — ATACAN A UNA FAMILIA EN SU VIVIENDA EN EL EJIDO BOCA DEL REFUGIO: TRES MUERTOS, DOS DE ELLOS MENORES",
  hecho="Galeana · <code>EJIDO BOCA DEL REFUGIO, VIVIENDA</code>, " + RES + " · lunes 16-NOV, por ruta (Enfoque Monterrey 2026/11/16: «deja ataque armado tres muertos, entre ellos una menor, en Galeana»; ABC Noticias 2026/11/16: «tragedia en Galeana: matan a papá y a sus dos hijos»; El Heraldo de México 2026/11/16: «atacan a familia en Galeana: mueren tres personas, dos de ellos menores de edad») · madrugada, ~01:00, " + RES + " · <b>3 muertos</b>, por titular: un hombre y sus dos hijos, una niña y un adolescente (🔴 homicidio múltiple) · heridos: «sube a dos heridos y tres muertos», por titular (MVS 2026/11/16); primer parte, «un muerto y tres menores heridos», por titular (MVS 2026/11/16); un menor herido grave o cuatro heridos, " + RES + ": <code>CIFRA DE HERIDOS CONTRADICHA — SE INTEGRAN 2, ÚLTIMA CIFRA CON TITULAR</code> · FGJNL abrió carpeta; Fuerza Civil acudió, " + RES + " · regreso de los agresores y segundo enfrentamiento, " + RES + ": no se integra · " + NOD,
  panel="<b>Ataque a una familia: 3 muertos</b>, dos de ellos menores", inst=SB, nac="El Heraldo de México · Milenio · N+", conf="★★★☆☆",
  campo="hora solo por resumen; cifra de heridos contradicha; ninguna fuente institucional", I=0, N=3, R=7, A=0,
  fechadas=["Enfoque Monterrey (2026/11/16)", "MVS Noticias (2026/11/16)", "ABC Noticias (2026/11/16)", "Punto x Punto (2026/11/16)", "El Heraldo de México (2026/11/16)"], estatus="Parcialmente corroborado", arm=None,
  desl="Boca del Refugio no figura en las ediciones previas; Galeana, solo como localidad de Acapulco (ARG-117 y -118): otro lugar. «Ejecutan a dos hombres dentro de una vivienda en Galeana» (MVS 2026/9/30): otro hecho. Cateo y armas aseguradas en Galeana (ABC), sin vínculo publicado: no se integra. Identidades: medios, no se reproducen."),
 dict(id="ARG-152-002", estado="MX-BCN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-15", hora="~01:00–01:30 (solo por resumen)", mu=0, he=0, cu=0, hk=1,
  ent="Baja California", mun="Tecate (Las Juntas)", dia="DOM 15-NOV, POR RUTA",
  fecha_txt="domingo 15-nov, por ruta; ~01:00–01:30, solo por resumen",
  title="BAJA CALIFORNIA · TECATE — COMANDO PRIVA DE LA LIBERTAD EN UN RANCHO DE LAS JUNTAS A CINCO HOMBRES, ENTRE ELLOS UN AGENTE DE LA FISCALÍA ESTATAL",
  hecho="Tecate · <code>RANCHO EN LAS JUNTAS</code>, " + RES + " · domingo 15-NOV, por ruta (Diario de Yucatán 2026/11/15: «comando armado secuestra a cinco hombres en Tecate; dos fueron asesinados»; Radar Tecate News 2026/11/15: «reportan dos muertos en Paraíso Jurásico») · ~01:00–01:30, " + RES + " · " + FR + " · " + RET + " · <b>5 hombres privados de la libertad</b>, por titular, por un comando de unos 14 hombres armados, " + RES + " (🔴 secuestro múltiple; víctima autoridad) · entre ellos <b>un agente de la FGE</b> y militares retirados, por titular (El Universal: «comando secuestra a militares retirados, agente ministerial y excapitán aéreo en Tecate, BC; 2 fueron asesinados y 3 abandonados sobrevivientes») · tres liberados, esposados, en la carretera Tecate–Ensenada, " + RES + " · <code>SUERTE DE DOS VÍCTIMAS CONTRADICHA: «DOS FUERON ASESINADOS», POR TITULAR, FRENTE A «REPORTAN DOS DESAPARECIDOS», POR TITULAR (PODER MX); LA FGE NO CONFIRMA MUERTES NI HA LOCALIZADO CUERPOS, SOLO POR RESUMEN; SIN COMUNICADO NI DECLARACIÓN NOMBRADA DE LA FGE — NO SE INTEGRAN AL TOTAL DE MUERTOS</code> · " + NOD,
  panel="<b>Comando priva de la libertad a 5 hombres</b>, entre ellos un agente de la FGE", inst=SB, nac="El Universal", conf="★★★☆☆",
  campo="suerte de dos víctimas contradicha; hora solo por resumen; sin comunicado de la FGE", I=0, N=1, R=5, A=0,
  fechadas=["Diario de Yucatán (2026/11/15)", "Radar Tecate News (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Las Juntas no figura en las ediciones previas; Tecate, por otros hechos (ARG-150-REC-001, Los Encinos, 6-nov): otro hecho. " + PUB + " Predio llamado «Rancho de los Dinosaurios» o «Paraíso Jurásico», según el medio. Identidades: medios, no se reproducen."),
 dict(id="ARG-152-003", estado="MX-TAB", region="Golfo", color="rojo", impacto="grande", fecha="2026-11-15", hora="noche del 14 o madrugada del 15 (solo por resumen)", mu=3, he=1, cu=0, hk=0,
  ent="Tabasco", mun="Centro (Villahermosa, col. Gaviotas Sur)", dia="14 O 15-NOV; PUB. 15-NOV, POR RUTA",
  fecha_txt="noche del 14 o madrugada del 15-nov, contradicho, solo por resumen; publicación 15-nov, por ruta",
  title="TABASCO · CENTRO — ATAQUE EN UNA VIVIENDA DE GAVIOTAS SUR: TRES HOMBRES MUERTOS, UNA MUJER HERIDA Y CARTULINA CON PLAZO DE 24 HORAS",
  hecho="Villahermosa, Centro · <code>COL. GAVIOTAS SUR, VIVIENDA</code>, por titular (UnoTV: «ataque armado deja tres hombres muertos y una mujer herida en la colonia Gaviotas Sur, en Villahermosa, Tabasco»; Quadratín Tabasco: «ataque en Gaviotas Sur deja 3 muertos y mujer herida; FGET investiga hechos»; El Universal: «investiga FGE multihomicidio en Villahermosa») · publicación 15-NOV, por ruta (Proceso 2026/11/15: «asesinan a cuatro hombres en Centro, Tabasco; dejan amenaza para abandonar la plaza en 24 horas»; El Heraldo de México 2026/11/15: «ataque a balazos deja 3 personas fallecidas y una mujer lesionada»; Diario de Yucatán 2026/11/15: «investigan multihomicidio tras ataque armado en una vivienda de Tabasco») · <code>DÍA CONTRADICHO</code>: noche del sábado 14 o madrugada del domingo 15, " + RES + "; ambas versiones anteriores a las 10:24 del 15 · " + FR + " · " + RET + " · <b>3 hombres muertos y 1 mujer herida</b>, por titular (🔴 homicidio múltiple) · cartulina con plazo de 24 horas a un grupo rival para abandonar la plaza, por titular (Proceso) · el cuarto muerto del titular de Proceso es otro ataque (ranchería Buenavista 1a. sección, «horas después», " + RES + "): no se suma · la FGE inició carpeta por multihomicidio, " + RES + " · " + NOD,
  panel="<b>Ataque en una vivienda: 3 muertos y 1 herida</b>; cartulina con plazo de 24 horas", inst=SB, nac="Proceso · El Universal · El Heraldo de México · UnoTV · Posta", conf="★★★☆☆",
  campo="día y hora contradichos, solo por resumen; ninguna fuente institucional", I=0, N=5, R=3, A=0,
  fechadas=["Proceso (2026/11/15)", "El Heraldo de México (2026/11/15)", "Diario de Yucatán (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Gaviotas Sur no figura en las ediciones previas; las «Gaviotas» y «Buenavista» del índice son de Sinaloa y Michoacán: otros hechos. " + PUB + " Identidades: medios, no se reproducen."),
 dict(id="ARG-152-004", estado="MX-OAX", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-15", hora="~07:00 (solo por resumen)", mu=1, he=0, cu=0, hk=7,
  ent="Oaxaca", mun="San Juan Lachigalla (San Andrés Niño, distrito de Ejutla)", dia="DOM 15-NOV, POR RUTA",
  fecha_txt="domingo 15-nov, por ruta; ~07:00, solo por resumen",
  title="OAXACA · SAN JUAN LACHIGALLA — ASESINAN A BALAZOS AL AGENTE MUNICIPAL DE SAN ANDRÉS NIÑO ANTES DE UN TEQUIO",
  hecho="San Juan Lachigalla · <code>AGENCIA DE SAN ANDRÉS NIÑO, CANCHA, DISTRITO DE EJUTLA</code>, " + RES + " · domingo 15-NOV, por ruta (La Jornada 2026/11/15: «asesinan a agente municipal de San Juan Lachigalla, Oaxaca»; Proyecto Puente 2026/11/15: «asesinan a agente municipal de San Andrés Niño, Oaxaca; fue atacado a balazos») · ~07:00, " + RES + "; «(14:30 h)» en el titular de ADN Sureste es hora de la nota · " + FR + " · " + RET + " · <b>1 agente municipal muerto</b>, por titular (🔴 víctima autoridad) · atacado antes de un tequio, por titular (ADN Sureste: «ejecutan a agente municipal de San Andrés Niño previo a un tequio») · los agresores lo esperaban, línea de la FGEO, " + RES + " · " + NOD,
  panel="<b>Agente municipal asesinado</b> a balazos", inst=SB, nac="La Jornada", conf="★★★☆☆",
  campo="hora solo por resumen frente a la apertura de las 10:24; ninguna fuente institucional", I=0, N=1, R=8, A=0,
  fechadas=["La Jornada (2026/11/15)", "Proyecto Puente (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lachigalla y San Andrés Niño no figuran en las ediciones previas. " + PUB + " Autoridad comunitaria electa por sistema normativo indígena, " + RES + ". Identidades: medios, no se reproducen."),
 dict(id="ARG-152-005", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-15", hora="~00:40 (solo por resumen)", mu=2, he=3, cu=0, hk=0,
  ent="Sinaloa", mun="Mazatlán (col. Pueblo Nuevo)", dia="DOM 15-NOV, POR RUTA",
  fecha_txt="domingo 15-nov, por ruta; ~00:40, solo por resumen",
  title="SINALOA · MAZATLÁN — ATAQUE ARMADO EN UNA FIESTA EN LA COLONIA PUEBLO NUEVO: DOS MUERTOS Y TRES MÚSICOS HERIDOS",
  hecho="Mazatlán · <code>COL. PUEBLO NUEVO, CALLE ESTADO DE OCCIDENTE, FIESTA EN UNA VIVIENDA</code>, " + RES + " · domingo 15-NOV, por ruta (Informador 20261115: «Sinaloa: ataque armado en Mazatlán deja tres músicos heridos durante una fiesta»; Luz Noticias 2026-11-15: «aumenta a dos el saldo mortal de balacera durante fiesta en la colonia Pueblo Nuevo de Mazatlán»; Línea Directa 2026-11-15: «sube a dos la cifra de asesinados en ataque durante fiesta en Mazatlán; hay tres músicos heridos») · ~00:40, " + RES + " · " + FR + " · " + RET + " · <b>2 muertos y 3 heridos</b>, por titular; el segundo muerto, en el hospital (🔴 homicidio múltiple) · <code>SALDO ACTUALIZADO: 1 MUERTO EN EL PRIMER PARTE, POR TITULAR (LUZ NOTICIAS; NOROESTE; LOS NOTICIERISTAS), 2 EN LA ACTUALIZACIÓN (LUZ NOTICIAS; LÍNEA DIRECTA); EL TITULAR DE INFORMADOR SOLO TRAE LOS HERIDOS</code> · heridos, integrantes de la banda que amenizaba, por titular · peritos de la Fiscalía en el lugar, " + RES + " · " + NOD,
  panel="Ataque en una fiesta: <b>2 muertos y 3 músicos heridos</b>", inst=SB, nac="El Universal", conf="★★★☆☆",
  campo="hora solo por resumen frente a la apertura; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["Informador (20261115)", "Luz Noticias (2026-11-15)", "Línea Directa (2026-11-15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Visto en ARGOS 151 sin ruta con día («fiesta en la col. Pueblo Nuevo, 1 muerto»): se ficha ahora, con el segundo fallecimiento. No es ARG-151-004 (bar, Zona Dorada, 1 muerto y 1 herido) ni ARG-151-005 (col. 12 de Mayo, 1 muerto y 4 heridos): otra colonia, otra calle, otras cifras. Pueblo Nuevo de Escuinapa (ARG-132 y -133): otro municipio. " + PUB + " Identidades: medios, no se reproducen."),
 # ======================= AMARILLOS
 dict(id="ARG-152-006", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-15", hora="noche (solo por resumen)", mu=1, he=2, cu=0, hk=21,
  ent="Michoacán", mun="Morelia (col. Colinas del Sur)", dia="DOM 15-NOV, POR RUTA",
  fecha_txt="domingo 15-nov, por ruta; noche, solo por resumen",
  title="MICHOACÁN · MORELIA — ATAQUE ARMADO EN UNA VIVIENDA DE COLINAS DEL SUR: UN HOMBRE MUERTO Y DOS MUJERES HERIDAS",
  hecho="Morelia · <code>COL. COLINAS DEL SUR, CALLE NANCHE, VIVIENDA</code>, " + RES + " · domingo 15-NOV, por ruta (Grupo Marmor 2026/11/15: «agresión a balazos al sur de Morelia deja saldo de un fallecido y dos mujeres lesionadas») · noche, " + RES + " · " + FR + " · <b>1 hombre muerto y 2 mujeres heridas</b>, por titular (Quadratín: «ataque armado deja un hombre muerto y 2 mujeres heridas en Morelia») (🟡 homicidio doloso único) · una de las heridas estaría embarazada, por titular (MiMorelia), preliminar · Policía de Morelia y FGE, diligencias, " + RES + " · «motociclista mata a adulto mayor y hiere a dos mujeres en Morelia», por titular (La Voz de Michoacán): <code>MECÁNICA CONTRADICHA</code> · " + NOD,
  panel="Ataque en una vivienda: <b>1 muerto y 2 mujeres heridas</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; mecánica contradicha; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Grupo Marmor (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Colinas del Sur no figura en las ediciones previas."),
 dict(id="ARG-152-007", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-15", hora="noche (solo por resumen)", mu=1, he=0, cu=0, hk=20,
  ent="Chihuahua", mun="Ciudad Juárez (Puerto de Anapra)", dia="DOM 15-NOV, POR RUTA",
  fecha_txt="domingo 15-nov, por ruta; noche, solo por resumen",
  title="CHIHUAHUA · CIUDAD JUÁREZ — ATACAN A BALAZOS A UNA PAREJA EN PUERTO DE ANAPRA",
  hecho="Ciudad Juárez · <code>PUERTO DE ANAPRA, CRUCE DE QUIMERA Y GUACHINANGO</code>, " + RES + " · domingo 15-NOV, por ruta (El Diario de Juárez 2026/nov/15: «asesinan a mujer y hombre a balazos en Puerto de Anapra») · noche, " + RES + " · " + FR + " · <code>SALDO CONTRADICHO</code>: 2 muertos, una mujer y un hombre, por titular (El Diario de Juárez), frente a «muere hombre», por titular (NetNoticias: «acribillan a pareja en Anapra, Juárez: muere hombre»); mujer herida, " + RES + ", no se integra: <b>se integra 1 muerto, mínimo coincidente</b> (🟡 homicidio doloso, cifra mínima) · FGE Chihuahua a cargo, " + RES + " · " + NOD,
  panel="Ataque a una pareja: <b>1 o 2 muertos</b>, contradicho", inst=SB, nac="—", conf="★★★☆☆",
  campo="saldo contradicho entre dos fuentes; hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Diario de Juárez (2026/nov/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Anapra no figura en las ediciones previas; ataque de agosto de 2025 en Rancho Anapra (cuatro muertos): otro hecho, fuera de serie. Identidades: no publicadas."),
 dict(id="ARG-152-008", estado="MX-TLA", region="Centro", color="amarillo", impacto="mediano", fecha="2026-11-15", hora="no fijada", mu=1, he=0, cu=0, hk=12,
  ent="Tlaxcala", mun="Calpulalpan (Mazapa)", dia="PUB. 15-NOV, POR RUTA",
  fecha_txt="publicación domingo 15-nov, por ruta; hora no fijada",
  title="TLAXCALA · CALPULALPAN — MATAN A UN CAMPESINO ADULTO MAYOR PARA ROBARLE SU GANADO",
  hecho="Calpulalpan · <code>MAZAPA</code>, " + RES + " · publicación domingo 15-NOV, por ruta (Gente Tlx 2026/11/15: «asesinan a adulto mayor en Calpulalpan; presuntamente le robaron su ganado») · hora no fijada · " + FR + " · <b>1 hombre muerto</b>, adulto mayor, por titular (🟡 homicidio doloso único) · «matan a golpes a campesino de 75 años en Calpulalpan, Tlaxcala», por titular (Cinco Radio); «asesinan a campesino de 75 años durante robo de borregos en Tlaxcala», por titular (Meganoticias) · " + NOD,
  panel="<b>Campesino asesinado</b> en un robo de ganado", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada; mecánica solo por medios regionales; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Gente Tlx (2026/11/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Calpulalpan y Mazapa no figuran en las ediciones previas. Móvil de robo de ganado: medios."),
 # ======================= VERDES
 dict(id="ARG-152-009", estado="MX-MEX", region="Centro", color="verde", impacto="grande", fecha="2026-11-15", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Estado de México", mun="Atlacomulco, Jiquipilco, Jocotitlán, Calimaya y Naucalpan (solo por resumen)", dia="PUB. 15-NOV, POR RUTA",
  fecha_txt="publicación domingo 15-nov, por ruta; día de los cateos no fijado",
  title="ESTADO DE MÉXICO — DIEZ CATEOS CONTRA UNA RED DE HUACHICOL DE GAS LP: CUATRO DETENIDOS, ENTRE ELLOS UN EXCANDIDATO A ALCALDE",
  hecho="Estado de México · 10 cateos en cinco municipios —Atlacomulco, Jiquipilco, Jocotitlán, Calimaya y Naucalpan—, " + RES + " · publicación domingo 15-NOV, por ruta (La Silla Rota 2026/11/15: «excandidato de MC cae por presunta red de huachicol en Edomex»; El Heraldo de México 2026/11/15: «cateos en Edomex dejan cuatro detenidos y más de 15 mil litros de gas»; Proyecto Puente 2026/11/15: «…realizan 10 cateos y detienen a cuatro personas») · <code>DÍA DE LOS CATEOS NO FIJADO</code> · " + FR + " · <b>10 cateos</b>, por titular · <b>~15 mil litros de gas LP</b>: «15 mil», por titular (SinEmbargo); «casi 16 mil», por titular (López-Dóriga): <code>CIFRA DE LITROS CONTRADICHA — SE CONSIGNA «~15 MIL»</code> · tractocamiones, pipas y semirremolques, " + RES + " · armas cortas, cargadores y cartuchos, " + RES + ": <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · Gabinete de Seguridad, con Marina, FGR, SSPC, GN y CNI, " + RES + " · " + NDA + " (4, por titular) · detención en la madrugada del viernes 13, " + RES + ": si los cateos son del 13, no son de esta ventana: <code>POSIBLE DUPLICIDAD — NO CONFIRMADA</code>",
  panel="<b>Red de huachicol: 10 cateos y 4 detenidos</b>; ~15 mil litros de gas LP", inst=SB, nac="La Silla Rota · El Heraldo de México · SinEmbargo · López-Dóriga", conf="★★★☆☆",
  campo="día de los cateos no fijado; ninguna fuente institucional leída", I=0, N=4, R=2, A=0,
  fechadas=["La Silla Rota (2026/11/15)", "El Heraldo de México (2026/11/15)", "Proyecto Puente (2026/11/15)", "El Diario de Chihuahua (2026/nov/15)"], estatus="Parcialmente corroborado", arm="ARG-152-ARM-001",
  desl="Huachicol en el Estado de México en el índice: hechos de agosto (ARG-91 a -98), otros. Operativo Otomí (acumulado de 50 días, visto en ARGOS 151): sin coincidencia publicada de fecha, cifras ni detenidos; vínculo no acreditado. Identidades: medios, no se reproducen."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-152-REC-001", estado="MX-PUE", region="Centro", fecha="2026-11-15", hora="madrugada, por titular; ~04:00, solo por resumen", orig="ARGOS 151", col_orig="rojo", mu=5, he=0, cu=0,
  ent="Puebla", mun="Chignahuapan (Cuautelolulco)", dia="DOM 15-NOV, MADRUGADA",
  fecha_txt="domingo 15-nov, por ruta; madrugada, por titular",
  title="PUEBLA · CHIGNAHUAPAN — CINCO HOMBRES MUERTOS A BALAZOS TRAS UN BAILE EN CUAUTELOLULCO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 151</code> · Chignahuapan · <code>CUAUTELOLULCO, CARRETERA CHIGNAHUAPAN–COCULCO (PUE-112), KM 23</code>, " + RES + " · domingo 15-NOV, por ruta (Infobae 2026/11/15: «cinco hombres mueren en enfrentamiento armado tras baile en Chignahuapan, Puebla»; La Silla Rota 2026/11/15: «localizan cinco hombres muertos en carretera de Chignahuapan, Puebla»; El Heraldo de México 2026/11/15: «hallan cinco hombres ejecutados tras balacera en carretera de Chignahuapan, Puebla») · madrugada, por titular (TV Azteca: «¡Madrugada de terror en Puebla! Ataque armado deja cinco hombres muertos en Chignahuapan»); ~04:00, " + RES + " · <b>5 hombres muertos</b>, por titular (🔴 homicidio múltiple) · tras un baile de fiesta patronal, por titular · «enfrentamiento» o «riña» entre dos grupos, según el medio · dos vehículos baleados y armas, por titular (Diario Puntual 2026/11/16: «ejecutan a cinco hombres en Chignahuapan; hallan dos vehículos baleados y armas») · ~01:50 o ~04:00, " + RES + " · la FGE abrió carpeta, " + RES + " · " + NOD,
  panel="<b>5 hombres muertos</b> tras un baile", inst=SB, nac="Infobae · La Silla Rota · El Heraldo de México · Latinus · TV Azteca",
  conf="★★★☆☆", campo="hora solo por resumen (madrugada, por titular); ninguna fuente institucional", I=0, N=5, R=4, A=0,
  fechadas=["Infobae (2026/11/15)", "Síntesis (2026/11/15)", "La Silla Rota (2026/11/15)", "El Heraldo de México (2026/11/15)", "El Heraldo de Puebla (2026/11/15)", "Latinus (2026/11/15)", "Diario Puntual (2026/11/16)"],
  desl="Rojo sin ruta fechada en ARGOS 151 (MTP Noticias; El Quinto Medio): se recupera con seis rutas del 15. La madrugada descansa en un titular sin ruta fechada (TV Azteca): ancla de hora débil. Atribución a un grupo criminal: solo por resumen, no se reproduce. Identidades: no publicadas."),
 dict(id="ARG-152-REC-002", estado="MX-BCN", region="Noroeste", fecha="2026-11-14", hora="tarde-noche (solo por resumen)", orig="ARGOS 151", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Baja California", mun="Tijuana (col. La Postal)", dia="SÁB 14-NOV, POR RESUMEN",
  fecha_txt="sábado 14-nov, tarde-noche, solo por resumen; publicación 15-nov, por ruta",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A DOS HOMBRES A BALAZOS JUNTO A LAS VÍAS DEL TREN EN LA COLONIA LA POSTAL",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 151</code> · Tijuana · <code>COL. LA POSTAL, JUNTO A LAS VÍAS DEL TREN</code>, por titular (Diario Tijuana 2026/11: «asesinan a dos hombres a balazos junto a las vías del tren en la colonia La Postal») · tarde-noche del sábado 14-NOV, " + DSR + " · publicación 15-NOV, por ruta (Periodismo Negro 2026/11/15: «asesinan a dos hombres a balazos junto a las vías del tren en Tijuana») · <b>2 hombres muertos</b>, por titular (🔴 homicidio múltiple) · heridas en la cabeza; el agresor huyó a pie por las vías, " + RES + " · FGE de Baja California, diligencias, " + RES + " · " + NOD,
  panel="<b>2 hombres muertos</b> junto a las vías del tren", inst=SB, nac="—",
  conf="★★★☆☆", campo="día solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Periodismo Negro (2026/11/15)"],
  desl="La Postal no figura en las ediciones previas; doble homicidio en la col. Postal de septiembre de 2024 (Zeta): otro hecho. Doble homicidio junto a las vías en Otay (Zeta), " + RES + ": posible confusión de ubicación, no se suma. Si resultara del domingo 15 después de las 10:24, es hecho de esta ventana. Alias de las víctimas: medios, no se reproducen."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-152-ARM-001", ficha="ARG-152-009", estado="MX-MEX", region="Centro", color="verde", ent="Estado de México", mun="cinco municipios <span class=\"muted-note\">(solo por resumen)</span>",
  fecha="2026-11-15", fecha_txt="pub. 15-nov, por ruta; día de los cateos no fijado", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], nd=list(range(10)), integra=False,
  corp="Gabinete de Seguridad <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="armas cortas, cargadores y cartuchos solo por resumen: CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO; 4 detenidos por titular de medio, sin cifra de autoridad: n/d; FRONTERA DE VENTANA — HORA NO FIJADA; ver ARG-152-009",
  fuentes=["La Silla Rota (2026/11/15)"]),
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
HORAS = 24 + 6 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0] * 10, (TOT, ND)
assert ND == [True] * 10, ND
assert cnt == {"rojo": 5, "amarillo": 3, "verde": 1}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (12, 8, 0, 7, 0, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,37", DENS
assert (NAP, NFR, NRET) == (0, 8, 4), (NAP, NFR, NRET)
assert len(ENT) == 9 and len(ENT_ROJO) == 5, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-152-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-152-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-11-15" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-11-15", x["id"]
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
head = head.replace("<title>ARGOS 151 — Reporte Nacional de Seguridad — 2026-11-15</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE NUEVO LEÓN EL PARTE DEL ATAQUE DE GALEANA, LA CIFRA OFICIAL DE VÍCTIMAS Y EL REGISTRO DEL SEGUNDO ENFRENTAMIENTO REPORTADO POR TESTIGOS</b> (ARG-152-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE BAJA CALIFORNIA LA SITUACIÓN OFICIAL DE LAS PERSONAS NO LOCALIZADAS EN TECATE Y LA IDENTIFICACIÓN OFICIAL DE LAS CINCO VÍCTIMAS</b> (ARG-152-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE TABASCO EL PERITAJE DE LA CARTULINA DE GAVIOTAS SUR Y SU COTEJO CON MENSAJES PREVIOS EN CENTRO</b> (ARG-152-003).
      <br><b>4. SOLICITE A LA FISCALÍA DE OAXACA LAS LÍNEAS DE INVESTIGACIÓN DEL ATAQUE AL AGENTE MUNICIPAL DE SAN ANDRÉS NIÑO, Y A LA DE SINALOA EL PARTE DEL SEGUNDO FALLECIMIENTO Y LAS MEDIDAS DE PROTECCIÓN PARA LOS MÚSICOS HERIDOS DE PUEBLO NUEVO</b> (ARG-152-004 y -005).
      <br><b>5. SOLICITE AL GABINETE DE SEGURIDAD EL INVENTARIO OFICIAL —ARMAS, COMBUSTIBLE Y VEHÍCULOS— Y LA FECHA DE LOS CATEOS CONTRA LA RED DE HUACHICOL DEL ESTADO DE MÉXICO</b> (ARG-152-009).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>15-nov 10:24 → 16-nov 10:30 CDMX</b> (<b>{DUR}</b>) · dom 15 (desde 10:24) · lun 16 (hasta 10:30) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto</b> (ventana de ARGOS 151), atenuadas, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: ningún evento con cantidad integrable; el de huachicol, cualitativo · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas; fuera, las dos víctimas de Tecate de suerte contradicha y la segunda víctima de Anapra · <b>heridos</b>: {HE}; en Galeana, la última cifra con titular · <b>privados de la libertad</b>: 5 (Tecate), por titular · <b>detenidos</b>: 4 (huachicol), solo por titular de medio, sin cifra de autoridad: n/d · <b>marcas</b>: {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (todos los publicados el domingo 15, día de apertura) · <b>totales sujetos a {NRET} cláusulas de retiro</b> (Tecate, Gaviotas Sur, Lachigalla y Pueblo Nuevo: hora solo por resumen anterior a las 10:24) · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos, por titular.
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «Mazatlán suma siete asesinatos y nueve heridos tras 11 ataques armados… durante el fin de semana» (Infobae 2026/11/16) · «7 homicidios este fin de semana en Michoacán» (Meganoticias) · balance mensual de armas de la SSP de Veracruz (Formato 7 2026/11/15) · «15 miembros de cabildo asesinados» (La Razón 2026/11/16).
    <br><b>Vistos, fuera de totales</b> (ventana anterior por resumen, sin ruta con día o fuente única): Atotonilco el Alto, Jal., <b>detención de un presunto operador de Los R's ligado al caso del alcalde de Uruapan</b>, tras un enfrentamiento con un agresor muerto el sábado 14 (Expansión 2026/11/14), hora no fijada —ventana de 150 o 151— y quién inició, solo por resumen · Irapuato, col. Esfuerzo Obrero, hombre muerto en el hospital (AM 2026/11/15; ~06:00 {RES}) y Venado de Yóstiro, joven asesinado en su casa (~03:30 {RES}): ventana de 151 · Morelia, Villas del Pedregal (sábado 14, ~22:00 {RES}), otro hecho que ARG-152-006 · Apatzingán, motociclista (sábado 14 por la noche) · Poza Rica, local de telefonía, 1 muerto y 1 herida (sábado 14, ~21:00 {RES}) · Torreón, vecino herido (~02:00 del 15 {RES}) · Chiautempan, Xaxala, hombre asesinado (Gente Tlx 2026/11/15, «esta noche»; sábado {RES}) · Villahermosa, ranchería Buenavista 1a. sección, hombre asesinado (Proceso 2026/11/15), sin día ni hora propios · Culiacán, Ampliación El Mirador, hombre herido, sin día en la ruta · Navolato, Villa Juárez, cuerpo con golpes, sin causa informada por autoridad · Zacatelco, hombre herido por un conocido (Gente Tlx 2026/11/16) · Celaya, hombre asesinado en una gasolinera, y Uruapan, La Cedrera, sin día en la ruta · Cancún, Villas Otoch, dos detenidos por tentativa de homicidio (PorEsto 2026/11/16), hecho sin fecha.
    <br><code>FE DE ERRATAS — ARGOS 151</code>: <b>dos rojos de la ventana de 151 se recuperan</b> (Chignahuapan y Tijuana): <b>6 rojos, 3 amarillos, 2 verdes</b> (cálculo propio; Tijuana, día solo por resumen) · <b>ARG-151-002</b>: 3 muertos, por titular (Cinco Radio: «… tres muertos, entre ellos dos policías de Morelos»; E-consulta); 2, por titular (Periódico Central); 4, solo por resumen: cifra contradicha, se mantienen 2 · <b>ARG-151-003</b>: «localizan calcinados a empresario, empleada y escoltas desaparecidos en Chahuites, Oaxaca», por titular (Proceso 2026/11/15); identificación pericial pendiente.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Zapopan (ARG-149-014 / -018)</b>: audiencia de vinculación de cinco presuntos escoltas el 15-nov (Infobae 2026/11/15), resultado no publicado · <b>Guadalajara</b>: muere bajo custodia, en un hospital privado, un interno de alto perfil del penal de Puente Grande (domingo 15; falla orgánica, comunicado de la SSP de Jalisco {RES}; ABC Noticias 2026/11/15) · <code>NO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-152-{i:03d}"]) for i in (1, 3, 5))
co2 = "\n".join(ficha(byid[f"ARG-152-{i:03d}"]) for i in (2, 4))
co3 = "\n".join(ficha(byid[f"ARG-152-{i:03d}"]) for i in (6, 7, 8, 9))
co4 = "\n".join(ficha(rbyid[f"ARG-152-REC-{i:03d}"], True) for i in (1, 2))
assert sorted(re.findall(r'id="(ARG-152-0\d\d)"', co1 + co2 + co3)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-152-REC-\d\d\d)"', co4)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), "n/d — ver ARG-152-ARM-001"),
 tile(1, "Armas largas", tv(1), NI),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "n/d — ver ARG-152-ARM-001"),
 tile(4, "Cargadores", tv(5), "n/d — ver ARG-152-ARM-001"),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: n/d — ver ARG-152-ARM-001"),
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
    <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code>: ningún aseguramiento de la ventana con cantidad publicada por titular o por autoridad.
    <br><b>Lectura regional</b>: ninguna región con arma integrada; Centro, un evento cualitativo (Estado de México) sin cantidad determinada. <b>Cálculo propio</b>.
    <br><code>BOLETÍN FEDERAL DE ACCIONES DEL 13, 14 Y 15-NOV: SIN RESULTADO INDEXADO EN VENTANA</code> (día suelto, rango y título, al inicio y al cierre); último indexado: acciones del 12-nov.
    <br><code>VISTOS, NO INTEGRADOS</code>: Cocula, Gro., 2 armas largas, 11 cargadores y 263 cartuchos {RES}, detención sin día; operativo previo del 3-nov en Tlanipatlán con cifras parecidas (ARG-146-ARM-003): <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · Querétaro, una pistola, dos cargadores y 34 cartuchos tras un concierto {RES}, sin día · Tabasco, FIRT Olmeca, 22 detenidos del 9 al 12-nov (Diario de Tabasco 2026/11/13): ventana de 150 · Matamoros, «Los Ciclones», Barrett .50 y granada (13-nov por ruta): ventana de 150, ya visto.
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
      <tr><td><b>Nuevo León</b><br>Monterrey (col. Bella Vista)</td><td>Homicidio calificado y delitos contra la salud {RES}; 1 sentenciado (MVS 2026/11/13)</td><td>«Casi 26 años», por titular; 25 años 10 meses {RES}; <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>Fiscalía de NL <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín en el dominio · ventana de ARGOS 150</td><td>Bajo</td></tr>
      <tr><td><b>Tabasco</b><br>Jalpa de Méndez</td><td>Pederastia; boletín FGET 5119, fechado el 9-nov por el listado del dominio; nota de un medio con otro sentenciado posible: <code>POSIBLE CASO HOMÓNIMO</code></td><td>30 años, por titular del listado</td><td>FGE Tabasco <span class="muted-note">(listado del dominio)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · URL individual no identificada · ventana de ARGOS 150</td><td>Bajo</td></tr>
      <tr><td><b>Sin novedad</b></td><td>Veracruz, 88 años por secuestro agravado (Hoy Xalapa 2026/11/13) · Champotón, 66 años 8 meses, procedimiento abreviado (PorEsto 2026/11/6): dominio de la fiscalía de Campeche no confirmado</td><td>—</td><td>—</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>22 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Son, Chih, Sin, Dgo · NL, Tamps, Coah, Zac, SLP · Mich, Ags · CDMX, Edomex, Pue, Tlax, Mor, Hgo, Qro · Ver, Tab · Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> · candidatos de la tabla: publicados antes de la ventana</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>22</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio de la fiscalía no confirmado</b></td><td>Camp, tercera edición (incluida en las 10 <code>NO REVISADA</code>)</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>10</b>: BCS · Jal, Gto, Col, Nay · Oax, Chis, Gro, QRoo, Camp</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 16-nov 10:30: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 23 entidades, Durango incluida; solo consulta amplia en 9 —Chih, BCS · Coah · Col, Nay, Ags · CDMX · Camp, Yuc— · <b>armamento: 11 de 32 por dominio oficial</b> —SLP · Col, Jal, Gto, Nay · Mor · Gro, Oax, Camp, Chis, QRoo—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (21): BC, BCS, Son, Chih, Sin, Dgo · NL, Tamps, Coah, Zac · Mich, Ags · CDMX, Edomex, Pue, Tlax, Hgo, Qro · Ver, Tab · Yuc</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 13, 14 y 15-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio y al cierre · último indexado: acciones del 12-nov (Milenio, Ultranoticias, SICOM, RED113, Tallapolítica, Certeza Diario) · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 16-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Cinco rojos propios en cinco entidades</b>: 0,21 rojos por hora (5 en {DUR}), frente a 0,16 en ARGOS 151 (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Noroeste 2 · Noreste 1 · Golfo 1 · Sureste 1 · Occidente y Centro 0; dos recuperaciones de la ventana de 151, fuera de totales (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: tres amarillos (Michoacán, Chihuahua y Tlaxcala).
      <br><b>4.</b> <b>Respuesta institucional</b>: un verde (huachicol, Estado de México) sin armamento integrable; ninguna sentencia integrable (totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()} SIN BOLETÍN FEDERAL INDEXADO; OCHO DE NUEVE HECHOS EN FRONTERA DE VENTANA Y CUATRO ROJOS —6 DE LOS 12 MUERTOS— CON CLÁUSULA DE RETIRO: TOTALES NO COMPARABLES SIN MÁS. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. VIVIENDAS Y FIESTAS FAMILIARES COMO BLANCO NOCTURNO EN CUATRO ENTIDADES: 9 MUERTOS Y 8 HERIDOS —CÁLCULO PROPIO—, CON MENORES Y MÚSICOS ENTRE LAS VÍCTIMAS</b> (ARG-152-001, -003, -005 y -006): ataques contra ocupantes de viviendas y reuniones; forma de acceso no informada; -003 y -005 con cláusula de retiro; vínculo entre hechos no acreditado. Línea: <b>vigilar la reincidencia de ataques a domicilios en el sur de Nuevo León (Galeana)</b>.
      <br><b>2. CARTULINA CON PLAZO DE 24 HORAS EN VILLAHERMOSA</b> (ARG-152-003): es consistente con una disputa territorial abierta en Centro; los grupos no han sido identificados por autoridad. Línea: <b>vigilar en las 48 horas siguientes hechos armados en Centro, Tabasco, al vencer el plazo</b>.
      <br><b>3. COMANDO NUMEROSO CONTRA CINCO VÍCTIMAS, ENTRE ELLAS MILITARES RETIRADOS Y UN AGENTE EN ACTIVO, EN UN RANCHO DE TECATE</b> (ARG-152-002): tres víctimas abandonadas esposadas en la carretera Tecate–Ensenada, solo por resumen; móvil, oficio de las víctimas y vínculo no acreditados. Línea: <b>vigilar hechos armados en el corredor Tecate–Ensenada</b>.
      <br><b>4. AGENTE MUNICIPAL DE UNA COMUNIDAD INDÍGENA ATACADO EN UN ESPACIO COMUNITARIO</b> (ARG-152-004): la espera de los agresores, solo por resumen, sugiere un ataque dirigido; móvil no informado y vínculo con otros hechos no acreditado. Línea: <b>vigilar amenazas contra agentes municipales del distrito de Ejutla</b>.
      <br><b>5. HUACHICOL DE GAS LP CON TRACTOCAMIONES Y PIPAS EN CINCO MUNICIPIOS DEL ESTADO DE MÉXICO</b> (ARG-152-009): el equipo, solo por resumen, es consistente con distribución a escala; vínculo del excandidato con la red no acreditado. Línea: <b>vigilar tomas y centros de carga de gas LP en el corredor Atlacomulco–Jocotitlán</b>.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: ATAQUES EN VIVIENDAS Y FIESTAS", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: PRIVACIÓN DE LA LIBERTAD Y AUTORIDAD COMUNITARIA", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA Y ACCIONES INSTITUCIONALES", co3)
 + page("CRIMEN ORGANIZADO (IV) — ALTO IMPACTO DE LA VENTANA DE ARGOS 151: CHIGNAHUAPAN Y TIJUANA", co4)
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
assert script.count("const EVENTOS_ARM = [\n" + ea + "\n];") == 1
# la ventana de 152 toca dos fechas de calendario (15 y 16-nov); la plantilla de 151 ya trae 2: sin reemplazo
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 151 con WINDOW_DAYS = 2"
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
