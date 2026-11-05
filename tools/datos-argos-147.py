# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 147.
Uso: python3 tools/datos-argos-147.py <plantilla ARGOS 146> <salida>
Ventana: 4-nov 06:52 → 5-nov 09:42 CDMX. Archivo: argos-2026-11-05.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "147", "2026-11-05", "09:42"
CONSULTA = "2026-11-05, última búsqueda 10:45"
DUR = "26 h 50 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 06:52 DEL 4, ES DE LA VENTANA DE ARGOS 146 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-147-001", estado="MX-MOR", region="Centro", color="rojo", impacto="grande", fecha="2026-11-04", hora="tarde, ~16:00 (solo por resumen)", mu=1, he=0, cu=0, hk=16,
  ent="Morelos", mun="Cuernavaca (Ejidos de Acapantzingo)", dia="4-NOV, POR RUTA",
  title="MORELOS · CUERNAVACA — ASESINAN A BALAZOS AL REGIDOR GABRIEL RIVAS RÍOS",
  hecho="Cuernavaca · <code>EJIDOS DE ACAPANTZINGO, SOLO POR RESUMEN</code> · miércoles 4-NOV, por ruta (La Razón; La Jornada; Infobae 2026/11/04; Proceso 2026/11/4; Informador 20261104) · " + AP + " · tarde, ~16:00, " + RES + " · " + RET + " · <b>1 muerto</b>: <b>Gabriel Rivas Ríos, regidor de Cuernavaca</b>, por titular (La Razón; La Jornada; Infobae) (🔴 víctima servidor público) · atacado a balazos dentro de su vehículo, por titular (TV Azteca) · «había denunciado amenazas», por titular (Proceso) · agresores en motocicleta, " + RES + " · la Fiscalía de Morelos «agotará todas las líneas de investigación», por titular (La Razón): declaración nombrada · móvil no establecido · " + NOD,
  panel="<b>Regidor de Cuernavaca asesinado a balazos</b>; había denunciado amenazas", inst="Fiscalía de Morelos" + PT, nac="La Razón · La Jornada · Infobae · Proceso", conf="★★★☆☆",
  campo="hora solo por resumen; declaración de la Fiscalía solo a través del titular de un medio", I=1, N=8, R=4, A=0,
  fechadas=["La Razón (2026/11/04)", "La Jornada (2026/11/04)", "Infobae (2026/11/04)", "Proceso (2026/11/4)", "Informador (20261104)", "Central Municipal (2026/11/04)", "Código Qro (2026/11/04)", "Quinto Poder (2026/11/04)"], estatus="Parcialmente corroborado", arm=None,
  desl="Acapantzingo en ARGOS 145 (vistos de la ventana de 144): otro hecho. La víctima no figura en las cinco ediciones previas ni en el índice. ARG-144-002 (regidor de Indaparapeo, 28-oct): otro hecho, otra entidad. Acompañante del regidor en el vehículo, solo por resumen: lesiones no publicadas."),
 dict(id="ARG-147-002", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-04", hora="~mediodía (solo por resumen)", mu=2, he=0, cu=0, hk=12,
  ent="Michoacán", mun="Tancítaro (Los Fresnos)", dia="PUB. 4-NOV, POR RUTA",
  title="MICHOACÁN · TANCÍTARO — ASESINAN A BALAZOS A DOS HERMANOS EN UNA HUERTA DE AGUACATE",
  hecho="Tancítaro · <code>LOS FRESNOS, HUERTA DE AGUACATE, SOLO POR RESUMEN</code> · publicado el miércoles 4-NOV, por ruta (Grupo Marmor 2026/11/04; Media News 2026/11/05) · " + AP + " · ~mediodía, " + RES + " · " + RET + " · <b>2 hombres muertos, hermanos</b>, por titular (Grupo Marmor; Respuesta; La Voz de Michoacán: «asesinan a balazos a dos hermanos en huerta de aguacate») (🔴 homicidio múltiple) · productores de aguacate, " + RES + " · la FGE realizó diligencias, " + RES + ": no es declaración · " + NOD,
  panel="<b>Dos hermanos asesinados a balazos</b> en una huerta de aguacate", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora y lugar solo por resumen; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Grupo Marmor (2026/11/04)", "Media News (2026/11/05)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tancítaro no figura en las cinco ediciones previas ni en el índice. El Congresista atribuye un doble homicidio en Tancítaro a una disputa por herencia, con otros nombres y fecha «4 de octubre», solo por resumen: <code>POSIBLE HECHO DISTINTO — NO SE INTEGRA</code>. Identidad de las víctimas: medios, no se reproduce."),
 dict(id="ARG-147-003", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-11-04", hora="hallazgo ~07:30-07:54 (solo por resumen)", mu=2, he=0, cu=0, hk=8,
  ent="Guerrero", mun="Chilpancingo (col. Tierra y Libertad)", dia="4-NOV, POR RUTA Y TITULAR",
  title="GUERRERO · CHILPANCINGO — HALLAN A DOS HOMBRES ASESINADOS Y TORTURADOS EN UN TERRENO BALDÍO",
  hecho="Chilpancingo · <code>COL. TIERRA Y LIBERTAD, SOLO POR RESUMEN</code> · miércoles 4-NOV, por ruta y titular (Informador 20261104: «jornada violenta en Guerrero deja siete muertos»; El Congresista: «en distintas localidades este miércoles») · " + AP + " · hallazgo ~07:30-07:54, " + RES + " · " + RET + " · <b>2 hombres hallados asesinados y torturados</b> en un terreno baldío, por titular (Bajo Palabra; Milenio: «hallan dos cuerpos en lote baldío de Chilpancingo»; Meganoticias: «presuntamente torturados»; rutas sin fecha) (🔴 homicidio múltiple) · parte de «siete hombres asesinados en varios municipios de Guerrero en menos de ocho horas», por titular (Infobae 2026/11/05): <b>cinco municipios y reparto, solo por resumen</b> · causa de muerte no informada por autoridad · " + NOD,
  panel="<b>Dos hombres hallados asesinados y torturados</b>", inst=SB, nac="Infobae · El Universal", conf="★★☆☆☆",
  campo="día y colonia solo por resumen; titulares del hallazgo sin fecha en la ruta; ninguna fuente institucional", I=0, N=3, R=3, A=0,
  fechadas=["Informador (20261104)", "Infobae (2026/11/05)"], estatus="Pendiente de corroboración", arm=None,
  desl="Tierra y Libertad de Chilpancingo no figura en las cinco ediciones previas ni en el índice; «Tierra y Libertad», El Diario de Chihuahua 2025/dec/30: otro hecho (2025). Resto de la jornada: Olinalá, ficha propia (ARG-147-007); Tixtla (1), Zihuatanejo (1) y Acapulco, Nuevo Puerto Marqués (1): homicidios únicos o cuerpos sin causa, solo por resumen, vistos fuera de totales. La jornada no se integra como balance."),
 dict(id="ARG-147-004", estado="MX-MIC", region="Occidente", color="rojo", impacto="mediano", fecha="2026-11-04", hora="noche (solo por resumen)", mu=0, he=0, cu=0, hk=21,
  ent="Michoacán", mun="Indaparapeo (Colonia de Guadalupe y San Lucas Pío)", dia="PUB. 5-NOV, POR RUTA",
  title="MICHOACÁN · INDAPARAPEO — ENFRENTAMIENTO ENTRE GRUPOS CRIMINALES CON USO DE DRONES",
  hecho="Indaparapeo · <code>COLONIA DE GUADALUPE Y SAN LUCAS PÍO, SOLO POR RESUMEN</code> · publicado el jueves 5-NOV, por ruta (Grupo Marmor 2026/11/05) · " + FR + " · noche del miércoles 4, " + RES + " · <b>enfrentamiento entre grupos criminales con uso de drones</b>, por titular (Grupo Marmor; Respuesta; La Voz de Michoacán: «utilizan drones»); «drones explosivos», por titular (La Redacción) (🔴 uso de drones armados) · capacidad explosiva no confirmada por autoridad · grupos señalados, " + RES + ": no se reproducen · se pidió apoyo al Ejército, la GN y la Guardia Civil, " + RES + " · saldo no informado · " + NOD,
  panel="<b>Enfrentamiento entre grupos con drones</b>; saldo no informado", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día solo por resumen; capacidad de los drones no confirmada; republicaciones de una misma nota", I=0, N=0, R=2, A=0,
  fechadas=["Grupo Marmor (2026/11/05)", "RED113 (2026/11)"], estatus="Parcialmente corroborado", arm=None,
  desl="Indaparapeo en el índice: ARG-140-016 (base de operaciones, 23-oct) y ARG-144-002 (El Triunfo, regidor, 28-oct): otros hechos, otro lugar. Grupo Marmor, Respuesta, La Voz de Michoacán, Indicio e IMN publican la misma nota: una fuente."),
 # ======================= AMARILLOS
 dict(id="ARG-147-005", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-04", hora="~19:00 (solo por resumen)", mu=1, he=2, cu=0, hk=19,
  ent="Guanajuato", mun="Pénjamo (zona centro)", dia="4-NOV, POR RUTA",
  title="GUANAJUATO · PÉNJAMO — ATAQUE ARMADO EN UN PUESTO DE LA ZONA CENTRO: UN MUERTO Y DOS HERIDOS",
  hecho="Pénjamo · <code>ZONA CENTRO, POR TITULAR (CORREO); PUESTO DE GELATINAS, POR TITULAR (N+); CALLE DEGOLLADO, SOLO POR RESUMEN</code> · miércoles 4-NOV, por ruta (Correo 2026/nov/04) · " + AP + " · ~19:00, " + RES + " · " + RET + " · <b>1 muerto</b> y <b>2 heridos</b>, por titular (Correo; AM 2026/11/05; Milenio; N+) (🟡 homicidio doloso único) · heridos, familiares de la víctima, " + RES + " · la Fiscalía investiga, " + RES + ": no es declaración · " + NOD,
  panel="<b>Ataque armado: 1 muerto y 2 heridos</b>", inst=SB, nac="Milenio · N+", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["Correo (2026/nov/04)", "AM (2026/11/05)"], estatus="Parcialmente corroborado", arm=None,
  desl="Pénjamo en el índice: ARG-141-001 (col. Lázaro Cárdenas, 25-oct, 1 muerto y 2 heridos, tres jóvenes; mismo saldo y medio): otro hecho por fecha, colonia y víctimas. ARG-138-013 (zona centro, 19-oct, abuelo y nieto), ARG-145-002 (carretera Tepuza de Ortiz–Zapote de Cestau, 30-oct), ARG-113-ARM-002 y ARG-94-001: otros hechos. Puesto de gelatinas y calle Degollado: sin coincidencias. Identidad de las víctimas: medios, no se reproduce."),
 dict(id="ARG-147-006", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-04", hora="tarde-noche (solo por resumen)", mu=1, he=0, cu=0, hk=20,
  ent="Sinaloa", mun="Culiacán (col. Alturas del Sur)", dia="4-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS A UN JOVEN EN ALTURAS DEL SUR",
  hecho="Culiacán · <code>COL. ALTURAS DEL SUR, POR TITULAR</code> · miércoles 4-NOV, por ruta (Línea Directa 2026-11-04: «asesinan a balazos a un joven en Alturas del Sur») · " + AP + " · tarde-noche, " + RES + " · " + RET + " · <b>1 muerto</b>: hombre de unos 25 años, afuera de un domicilio, " + RES + " (🟡 homicidio doloso único) · militares cercanos acudieron, " + RES + " · " + FU + " · " + NOD,
  panel="<b>Joven asesinado a balazos</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Línea Directa (2026-11-04)"], estatus="Pendiente de corroboración", arm=None,
  desl="Alturas del Sur: mujer hallada muerta, presunta integrante de la GN (2-nov o antes; vista en ARGOS 146; pertenencia no acreditada): otro hecho. Col. Guadalupe Victoria: ARG-147-008. Fracc. Los Ángeles e Infonavit Solidaridad: sin ruta fechada propia, vistos."),
 dict(id="ARG-147-007", estado="MX-GRO", region="Sureste", color="amarillo", impacto="mediano", fecha="2026-11-04", hora="~11:00 (solo por resumen)", mu=2, he=0, cu=0, hk=11,
  ent="Guerrero", mun="Olinalá (San Antonio Coyoacán)", dia="4-NOV, POR RUTA Y TITULAR",
  title="GUERRERO · OLINALÁ — ENFRENTAMIENTO ENTRE GRUPOS ARMADOS: DOS MUERTOS",
  hecho="Olinalá · <code>SAN ANTONIO COYOACÁN, SOLO POR RESUMEN</code> · miércoles 4-NOV, por ruta y titular (Informador 20261104; El Congresista) · " + AP + " · ~11:00, " + RES + " · " + RET + " · <b>2 hombres muertos</b> en un enfrentamiento entre grupos armados, " + RES + "; ambos con chalecos tácticos y armas largas, " + RES + " (🟡 enfrentamiento; quién inició, no determinado) · parte de los siete asesinados del 4-nov en Guerrero, por titular (Infobae 2026/11/05) · ningún detenido ni aseguramiento publicado",
  panel="<b>Enfrentamiento entre grupos armados: 2 muertos</b>", inst=SB, nac="Infobae · El Universal", conf="★★☆☆☆",
  campo="lugar, hora y circunstancia solo por resumen; ninguna fuente institucional", I=0, N=2, R=2, A=0,
  fechadas=["Informador (20261104)", "Infobae (2026/11/05)"], estatus="Pendiente de corroboración", arm=None,
  armtxt="sin fila — armas largas de los fallecidos, solo por resumen: no consta aseguramiento",
  desl="Olinalá y San Antonio Coyoacán no figuran en las cinco ediciones previas ni en el índice. Chilpancingo: ARG-147-003."),
 # ======================= VERDES
 dict(id="ARG-147-008", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-04", hora="~16:30 (solo por resumen)", mu=1, he=0, cu=0, hk=16.5,
  ent="Sinaloa", mun="Culiacán (col. Guadalupe Victoria)", dia="4-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — ASESINAN A UN HOMBRE EN UNA VIVIENDA DE LA COLONIA GUADALUPE VICTORIA",
  hecho="Culiacán · <code>COL. GUADALUPE VICTORIA, POR TITULAR</code> · miércoles 4-NOV, por ruta (Línea Directa 2026-11-04: «asesinan a un hombre en una vivienda de la colonia Guadalupe Victoria») · " + AP + " · ~16:30, " + RES + " · " + RET + " · <b>1 muerto</b> dentro de una vivienda, por titular (🟡 homicidio doloso único) · hombre de unos 50 años, " + RES + " · " + FU + " · " + NOD,
  panel="<b>Hombre asesinado</b> dentro de una vivienda", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Línea Directa (2026-11-04)"], estatus="Pendiente de corroboración", arm=None,
  desl="Col. Guadalupe Victoria (Las Tres Cruces) no figura en las cinco ediciones previas ni en el índice. Alturas del Sur: ARG-147-006, otro hecho."),
 dict(id="ARG-147-009", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-04", hora="~11:20 (solo por resumen)", mu=1, he=0, cu=0, hk=11.3,
  ent="Sinaloa", mun="Mazatlán (Mercado Hidalgo)", dia="PUB. 4-NOV, POR RUTA",
  title="SINALOA · MAZATLÁN — EJECUTAN AL PROPIETARIO DE UNA FRUTERÍA EN EL MERCADO HIDALGO",
  hecho="Mazatlán · <code>MERCADO HIDALGO, POR TITULAR</code> · publicado el miércoles 4-NOV, por ruta (Luz Noticias 2026-11-04: «sicarios llegan al mercado Hidalgo y ejecutan a propietario de una frutería») · " + AP + " · ~11:20 del miércoles, " + RES + " · agrupado con la explosión del 4-nov por <i>slug</i> (El Universal) y por ruta (Diario de Yucatán 2026/11/04); una fecha del 3, solo por resumen, no reencontrada · «mercado Juárez», por titular (Meganoticias 785603): <code>NOMBRE DEL MERCADO CONTRADICHO</code> · <code>SI EL HECHO RESULTA ANTERIOR A LAS 06:52 DEL 4 (O DEL 3-NOV), ES DE LA VENTANA DE ARGOS 146 Y SE RETIRA DE ESTE TOTAL</code> · <b>1 muerto</b>: propietario de una frutería, por titular (🟡 homicidio doloso único) · dos agresores en motocicleta, " + RES + " · «asesinan a dos personas en distintos hechos», por titular (El Universal, sin fecha en la ruta) · " + NOD,
  panel="<b>Propietario de una frutería ejecutado</b>", inst=SB, nac="El Universal", conf="★★★☆☆",
  campo="día por agrupación de medios; hora solo por resumen; nombre del mercado contradicho; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Luz Noticias (2026-11-04)"], estatus="Parcialmente corroborado", arm=None,
  desl="Mercado Hidalgo de Mazatlán no figura en las cinco ediciones previas ni en el índice. Abogada de la av. Carlos Canseco: ARG-147-010, otro hecho."),
 dict(id="ARG-147-010", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-04", hora="no fijada", mu=1, he=0, cu=0, hk=13,
  ent="Sinaloa", mun="Mazatlán (av. Carlos Canseco)", dia="PUB. 4-NOV, POR RUTA",
  title="SINALOA · MAZATLÁN — EJECUTAN A UNA ABOGADA EN LA AVENIDA CARLOS CANSECO",
  hecho="Mazatlán · <code>AV. CARLOS CANSECO, POR TITULAR</code> · publicado el miércoles 4-NOV, por ruta (Luz Noticias 2026-11-04: «ejecutan a abogada por la avenida Carlos Canseco al norte de Mazatlán») · " + AP + " · hora no publicada; <code>DÍA DEL HECHO NO FIJADO (3 O 4-NOV)</code>: agrupado con la explosión del 4-nov por <i>slug</i> (El Universal); «en 48 horas, atacan a balazos a cuatro mujeres», por titular (El Universal) · <code>SI EL HECHO RESULTA ANTERIOR A LAS 06:52 DEL 4 (O DEL 3-NOV), ES DE LA VENTANA DE ARGOS 146 Y SE RETIRA DE ESTE TOTAL</code> · <b>1 muerta</b>: abogada, por titular (🟡 homicidio doloso único; la profesión no es agravante de la lista roja) · baleada mientras conducía, " + RES + " · «Fiscalía General del Estado investiga asesinato», por titular (Sinaloahoy, sin fecha en la ruta): no es declaración · " + NOD,
  panel="<b>Abogada ejecutada</b> mientras conducía", inst=SB, nac="El Universal", conf="★★★☆☆",
  campo="día del hecho no fijado; hora no publicada; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Luz Noticias (2026-11-04)"], estatus="Parcialmente corroborado", arm=None,
  desl="Av. Carlos Canseco no figura en las cinco ediciones previas ni en el índice. La ruta de Luz Noticias fija la publicación, no el hecho. Identidad de la víctima: medios, no se reproduce."),
 dict(id="ARG-147-011", estado="MX-YUC", region="Sureste", color="verde", impacto="pequeno", fecha="2026-11-04", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Yucatán", mun="municipio no publicado", dia="PUB. 4-NOV, POR RUTA",
  title="YUCATÁN — DETIENEN AL PRESUNTO AUTOR INTELECTUAL DE UN HOMICIDIO EN LA AVENIDA HUAYACÁN DE CANCÚN",
  hecho="Yucatán, municipio no publicado · publicado el miércoles 4-NOV, por ruta (Noticaribe 2026/11/04) · " + AP + " · día de la detención no fijado · " + RET + " · detención del presunto autor intelectual de un homicidio en la avenida Huayacán (Cancún), por <i>slug</i> (Noticaribe) · operativo conjunto de las fiscalías de Quintana Roo y Yucatán, " + RES + " · señalado también por un ataque contra dos agentes de investigación, " + RES + " · 1 detenido, " + RES + " · " + FU,
  panel="<b>Detenido el presunto autor intelectual</b> de un homicidio en Cancún", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; día de la detención no fijado; detenido solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Noticaribe (2026/11/04)"], estatus="Pendiente de corroboración", arm=None,
  armtxt="sin fila — aseguramiento no publicado",
  desl="Avenida Huayacán no figura en las cinco ediciones previas ni en el índice. Homicidio original: 22-jul-2026, solo por resumen: evento anterior, no se recalifica. «Garabato» (ARG-146-021, Cancún, 3 detenidos): otro detenido; vínculo no acreditado."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-147-REC-001", estado="MX-CAM", region="Sureste", fecha="2026-11-01", hora="no fijada", orig="ARGOS 146", col_orig="rojo", mu=4, he=2, cu=0,
  ent="Campeche", mun="Champotón (Mayatecún II)", dia="2-NOV, POR RUTA",
  title="CAMPECHE · CHAMPOTÓN — ATAQUE ARMADO EN UN EXPENDIO DE BEBIDAS EN MAYATECÚN II: CUATRO MUERTOS Y DOS HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 146</code> · Champotón · <code>MAYATECÚN II, POR TITULAR (TV AZTECA); ESTABLECIMIENTO DE BEBIDAS, SOLO POR RESUMEN</code> · publicado el lunes 2-NOV, por ruta (La Prensa de Coahuila 2026/11/02) · domingo 1-NOV, " + DSR + " · <b>4 muertos</b> y <b>2 heridos</b>, por titular (La Prensa de Coahuila; TV Azteca; Omnia; Tribuna Campeche) (🔴 homicidio múltiple) · «tras altercado», por titular · cinco muertos según un medio, " + RES + ": superado por los titulares · «presunta detención de dos responsables», por titular (PorEsto 2026/11/5): sin cifra de autoridad",
  panel="<b>Ataque en un expendio de bebidas: 4 muertos y 2 heridos</b>", inst=SB, nac="TV Azteca",
  conf="★★★☆☆", campo="día solo por resumen; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["La Prensa de Coahuila (2026/11/02)", "PorEsto (2026/11/5)"],
  desl="Champotón en el índice: ARG-105-002 (rancho El Cerrito, 23-ago): otro hecho. Detención de dos presuntos responsables: seguimiento; ficha verde propia solo con cifra de autoridad y día fijado."),
 dict(id="ARG-147-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-11-01", hora="no fijada", orig="ARGOS 146", col_orig="rojo", mu=3, he=1, cu=0,
  ent="Sinaloa", mun="Mazatlán (dos centros de rehabilitación)", dia="2-NOV, POR RUTA",
  title="SINALOA · MAZATLÁN — ATACAN DOS CENTROS DE REHABILITACIÓN: TRES INTERNOS MUERTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 146</code> · Mazatlán · <code>COLS. FELIPE ÁNGELES Y FLORES MAGÓN, SOLO POR RESUMEN</code> · publicado el lunes 2-NOV, por ruta (Herqles 2026/11/02: «ataques a centros de rehabilitación en Mazatlán: tres muertos») · domingo 1-NOV, " + DSR + "; hora no fijada · <b>3 muertos</b> en dos centros, por titular (Herqles; Guardia Nocturna 2026/11: «atacan dos centros contra adicciones… tres internos muertos») (🔴 homicidio múltiple) · primer centro: «dos internos muertos y un herido», por titular (Noroeste) · segundo centro: 1 muerto y 4 heridos, " + RES + " · " + NOD,
  panel="<b>Ataque a dos centros de rehabilitación: 3 muertos</b>", inst=SB, nac="El Universal",
  conf="★★★☆☆", campo="día solo por resumen; hora no fijada; heridos del segundo centro solo por resumen; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["Herqles (2026/11/02)", "Guardia Nocturna (2026/11)"],
  desl="Visto en el archivo de equipos de ARGOS 146 («centro de rehabilitación, 1 muerto, 4 heridos», sin fecha), no publicado en su cartelón: era el segundo centro. Heridos del segundo centro, solo por resumen: fuera del total. Otro ataque del mismo día (calle Cima de las Rocas, 2 muertos en un automóvil), solo por resumen: visto. ARG-147-REC-003 (Coto Premier) y ARG-145-REC-002 (Los Ranchos): otros hechos."),
 dict(id="ARG-147-REC-003", estado="MX-SIN", region="Noroeste", fecha="2026-11-04", hora="~06:34 (solo por resumen)", orig="ARGOS 146", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (fracc. Coto Premier)", dia="4-NOV, POR RUTA",
  title="SINALOA · MAZATLÁN — ARROJAN EXPLOSIVOS ARTESANALES CONTRA UNA VIVIENDA EN COTO PREMIER",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 146</code> · Mazatlán · <code>FRACC. COTO PREMIER, POR TITULAR (NOROESTE)</code> · miércoles 4-NOV, por ruta (Luz Noticias 2026-11-04; Diario de Yucatán 2026/11/04) · <b>~06:34 del miércoles 4, " + RES + "</b> (Noroeste): anterior a la apertura de esta ventana · <b>artefactos explosivos arrojados contra una vivienda</b>, por titular (Noroeste: «arrojan dos explosivos artesanales»; N+, por <i>slug</i>: «lanzan-dos-explosivos-artesanales»; Luz Noticias: «arrojan artefacto explosivo») (🔴 uso de explosivos) · «detonan artefacto en cochera y localizan otro junto a la vivienda», por titular (Los Noticieristas): <code>NÚMERO DE ARTEFACTOS CONTRADICHO</code> (uno, por titular de Luz Noticias; dos, por titular de Noroeste) · sin heridos, " + RES + " · Ejército en el lugar y vecinos evacuados, " + RES + " · composición y capacidad de los artefactos: no informadas por autoridad · " + NOD,
  panel="<b>Explosivos artesanales contra una vivienda</b>; sin heridos publicados", inst=SB, nac="N+ · El Universal", conf="★★★☆☆",
  campo="hora solo por resumen; número de artefactos contradicho; ninguna fuente institucional", I=0, N=2, R=6, A=0,
  fechadas=["Luz Noticias (2026-11-04)", "Diario de Yucatán (2026/11/04)", "Los Noticieristas (2026/11)"],
  desl="Coto Premier no figura en las cinco ediciones previas ni en el índice. Abogada (av. Carlos Canseco) y frutería del Mercado Hidalgo, reunidos con este hecho por Diario de Yucatán: ARG-147-010 y -009. Centros de rehabilitación del 1-nov: ARG-147-REC-002, otro hecho. Artefacto localizado junto a la vivienda: <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code>."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ND_ALL = list(range(10))
ARM = []
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
HORAS = 26 + 50 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0] * 10 and ND == [True] * 10, (TOT, ND)
assert cnt == {"rojo": 4, "amarillo": 6, "verde": 1}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (12, 2, 0, 7, 3, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,41", DENS
assert (NAP, NFR, NRET) == (10, 1, 10), (NAP, NFR, NRET)
assert len(ENT) == 6 and len(ENT_ROJO) == 3, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-147-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-147-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-11-04" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-11-04", x["id"]

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
head = head.replace("<title>ARGOS 146 — Reporte Nacional de Seguridad — 2026-11-04</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE MORELOS LAS LÍNEAS DE INVESTIGACIÓN Y EL ESTADO DE LAS DENUNCIAS PREVIAS DE AMENAZAS DEL REGIDOR ASESINADO</b> (ARG-147-001).
      <br><b>2. SOLICITE A LA DEFENSA Y A LA GUARDIA CIVIL DE MICHOACÁN EL PARTE SOBRE EL USO DE DRONES EN INDAPARAPEO Y VIGILE LAS HUERTAS DE LOS FRESNOS, TANCÍTARO</b> (ARG-147-004 y -002).
      <br><b>3. SOLICITE A LA FISCALÍA DE SINALOA EL DICTAMEN DE LOS ARTEFACTOS DE COTO PREMIER, INCLUIDO EL LOCALIZADO JUNTO A LA VIVIENDA, Y LAS LÍNEAS DE INVESTIGACIÓN DE LOS CUATRO HOMICIDIOS DE CULIACÁN Y MAZATLÁN</b> (ARG-147-REC-003, -006, -008, -009 y -010).
      <br><b>4. SOLICITE A LA FISCALÍA DE GUERRERO EL DESGLOSE OFICIAL POR MUNICIPIO DE LOS SIETE HOMICIDIOS DEL 4-NOV</b> (ARG-147-003 y -007).
      <br><b>5. SOLICITE A LA FISCALÍA DE CAMPECHE LA SITUACIÓN JURÍDICA DE LOS PRESUNTOS DETENIDOS POR EL ATAQUE DE CHAMPOTÓN Y A LA DE SINALOA LA DE LOS ATAQUES A CENTROS DE REHABILITACIÓN</b> (ARG-147-REC-001 y -002).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>4-nov 06:52 → 5-nov 09:42 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto de la ventana anterior</b>, atenuada, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: ninguna arma ni detenido integrado al total: ningún aseguramiento con cifra de autoridad en la ventana · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas, incluidos 2 integrantes de grupos armados (Olinalá) · <b>cuerpos o restos hallados</b>: {CU} · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b> (hora no fijada frente a las 06:52 del 4): todas salvo ARG-147-004 · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos y {HE_REC} heridos, por titular (4 heridos más del segundo centro de Mazatlán, solo por resumen, fuera del cálculo); efecto sobre ARGOS 146, en el archivo de fuentes. <b>Cálculo propio</b>.
    <br><b>Vistos, fuera de totales</b> — <b>de la ventana de ARGOS 146</b> (🟢 o 🟡, no se recuperan): Tuxtla Gutiérrez, Chis. (6 detenidos; ver armamento) · Coatzacoalcos, «El Panda» (detenido el 3-nov; prisión preventiva, por titular, Hora Cero 2026/11/04) · Ixtapaluca, «El Patrón», líder de Los Linos (3-nov) · Tijuana, coordinador del Movimiento del Sombrero asesinado (noche del domingo 1-nov, {RES}; publicado el 4) · Mazatlán, policía municipal herido: día fijado, 2-nov (El Diario de Chihuahua 2026/nov/02) · Irapuato, Las Heras (3-nov) · Tulum, Francisco Uh May (persecución y balacera, 1 muerto, por <i>slug</i>; 1 detenido, {RES}; PorEsto 2026/11/3) · <b>sin ruta fechada propia o día no fijado</b> — <code>SIN RUTA FECHADA — NO SE FICHA</code>: Guerrero, Culiacán: en los deslindes de ARG-147-003 y -006 · Querétaro, col. Morelos (1 muerto, por titular; día, {RES}) · San Luis Potosí, bulevar Río Santiago (persecución) · Reynosa, col. Puerta Sur, restos calcinados y fosa hallados por un colectivo (sin fecha; ARG-140-008 en el mismo predio, 22-oct) · Valle de Chalco · Jiutepec · <b>cuerpos sin causa informada por autoridad</b>: Cortazar, col. Chapingo (1, en bolsas, por titular; Noticieros en Línea 2026/nov/04) · Nogales, Ver. (1, por titular; Golpe Político 2026/11/04) · Tepic (2 adultos mayores, por titular; causa por determinar; NTV 2026/11/04) · <b>balances, no se reparten ni se integran</b>: Guerrero, ver ARG-147-003 · Guanajuato y Sinaloa, «13 asesinatos en un día», por titular (diario.mx 2026/nov/05); 42 en el país, {RES} · Guanajuato, «al menos ocho», por titular (Turquesa, sin fecha).
    <br><b>Seguimiento, fuera del semáforo</b>: <b>ARG-146-006 (Irapuato)</b>: «cuatro lesionados», por titular (Latinus 2026/11/4), frente a «dos heridos» (Correo; La Silla Rota 2026/11/4): <code>CIFRA DE HERIDOS CONTRADICHA</code> · <b>ARG-146-019, -020 y -021</b>: detenciones del 3-nov, por ruta y por el boletín federal de acciones del 3-nov: cláusulas de retiro cerradas, se quedan en ARGOS 146 · <b>ARG-144-008 / ARG-145-REC-001 (Matamoros)</b>: el fiscal de Tamaulipas atribuye el disparo que mató a la niña a un helicóptero de la Guardia Estatal, por titular (Nación321 y Expreso 2026/11/02; Síntesis 2026/11/03) · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-147-{i:03d}"]) for i in (1, 2, 3, 4))
co2 = "\n".join(ficha(byid[f"ARG-147-{i:03d}"]) for i in (5, 7, 6, 8))
co2b = "\n".join(ficha(byid[f"ARG-147-{i:03d}"]) for i in (9, 10, 11))
co3 = "\n".join(ficha(rbyid[i], True) for i in ("ARG-147-REC-001", "ARG-147-REC-002", "ARG-147-REC-003"))
assert sorted(re.findall(r'id="(ARG-147-0\d\d)"', co1 + co2 + co2b)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-147-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
DSA = "ningún aseguramiento con cifra de autoridad en la ventana"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), NI),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), NI),
 tile(4, "Cargadores", tv(5), NI),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), "Indaparapeo: drones, por titular; no asegurados (ARG-147-004)"),
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
    <div class="map-caption">Sin aseguramiento con cifra integrable en la ventana.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> — ningún aseguramiento con cifra publicada y día fijado entre el 4-nov 06:52 y el 5-nov 09:42</td></tr>'
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
    <b>Lectura regional</b>: ninguna región con arma ni detenido integrado al total. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: ninguno con fila; drones de Indaparapeo, en su ficha; artefacto localizado en Coto Premier, ventana de ARGOS 146 (ARG-147-REC-003).
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>boletín federal de acciones del 3-nov</b> (ventana de ARGOS 146; <code>gob.mx/sspc</code>, por índice, y republicadores): Cocula, Gro. (2 largas, 1 corta, 12 cargadores, 335 cartuchos y 3 detenidos, {RES}; es ARG-146-019 / ARG-146-ARM-003) · <b>Tuxtla Gutiérrez, Chis.</b>: 6 detenidos, «diez armas y 895 cartuchos», por titular (La Nigua, sin fecha); 5 cortas, 5 largas y 36 cargadores, {RES}; primera publicación 3-nov (crprensa; Diario de Yucatán 2026/11/03): ventana de ARGOS 146 · <b>Villahermosa, Gaviotas Norte</b>: 3 detenidos, 1 corta, 1 cargador, {RES}: <code>FECHA NO FIJADA — NO SE INTEGRA</code> · <b>Sinaloa, Semar</b>: 15 largas, 30 cargadores, <code>HEREDADO — NO REVERIFICADO</code> (= Caminaguato–El Tepuche, visto en ARGOS 146) · <b>Edomex, operativo contra «Los Gigan»</b>: 32 detenidos, 20 armas, 178,780 litros, {RES}: <code>FECHA NO FIJADA — NO SE INTEGRA</code>; posible relación con Texcoco–Chimalhuacán–Ecatepec (12 detenidos, 178,780 litros, ARGOS 146, <code>HEREDADO — NO REVERIFICADO</code>): <code>POSIBLE DUPLICIDAD</code> · <b>boletín federal de acciones del 4-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code>.
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
      <tr><td><b>Oaxaca</b><br>San Antonio de la Cal</td><td>Secuestro agravado (2011); <b>2 sentenciados</b>, por titular · <b>nuevo en ARGOS 147</b></td><td><b>157 años</b>, por titular (Primera Línea 2026/11/04); 87 años 6 meses y 70 años, {RES}: su suma da 157 años 6 meses, <code>CIFRA CONTRADICHA</code></td><td>FGE Oaxaca <span class="muted-note">(boletín 2,948, solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · boletín no leído; solo republicadores del mismo comunicado; firmeza no informada; fecha de la sentencia no fijada</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>Los Ramones</td><td>Portación de arma de uso exclusivo y posesión de drogas, {RES}; procedimiento abreviado; <b>1 sentenciado</b>, por titular · <b>nuevo en ARGOS 147</b></td><td>«más de cinco años», por titular (MVS 2026/11/4); 5 años 5 meses 19 días, {RES}</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · fuente única; sin boletín del dominio</td><td>No confirmado</td></tr>
      <tr><td><b>Tabasco</b></td><td>Portación de arma de fuego sin licencia; 1 sentenciado, {RES} · <b>nuevo en ARGOS 147</b></td><td>No publicada</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin URL, pena ni campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Jalisco</b><br>Tlajomulco · Tlaquepaque</td><td>Dos feminicidios; <b>2 sentenciados</b> · candidato anterior</td><td><b>55 y 40 años</b>, por titular de medios (Informador 20261029)</td><td>Fiscalía de Jalisco <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el 29-oct, fuera de esta ventana; boletín del dominio no localizado</td><td>Bajo</td></tr>
      <tr><td><b>Puebla</b><br>Huejotzingo</td><td>Feminicidio y aborto · candidato de ARGOS 144</td><td>55 años, por titular de medios</td><td>FGE Puebla <span class="muted-note">(por medios)</span></td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · el boletín de 55 años del dominio es de otro caso (secuestro, 2025)</td><td>No confirmado</td></tr>
      <tr><td><b>BC · NL · Edomex · Zac · Coah · Hgo · Camp</b></td><td>Tecate (FGR, 4 sentenciados) · Mexicali (45 años) · NL 40 años y Doctor Arroyo, NL (15 años), ambos 28-oct · Ecatepec · Fresnillo · Ramos Arizpe · Tulantepec (audiencia de pena del 5-nov) · FGR Campeche (metilfenidato: no localizado) · <b>candidatos anteriores</b></td><td>Ver ARGOS 146 · <code>HEREDADO — NO REVERIFICADO</code></td><td>Fiscalías estatales y FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín del dominio en la ventana</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGJ Tamaulipas (FGJE-424-2026, 29-oct, {RES}) · FGE Tabasco (24-oct) · FGE Colima (15-oct) · FGE Quintana Roo (18-oct) · FGE Guerrero (15-oct) · FGE Oaxaca (boletín 2,933, octubre). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio: <code>fgr.org.mx</code> solo devolvió listados sin fecha · comunicados vistos solo en resúmenes del buscador</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>25 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, BCS, Chih · Tamps, NL, Zac, SLP · Jal, Col, Ags, Mich, Gto · CDMX, Edomex, Mor, Pue, Tlax, Hgo · Ver, Tab · Oax, Gro, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada · Oaxaca: boletín 2,948 del 4-nov visto solo por resumen y por republicadores</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>24</b> fiscalías estatales revisadas (todas salvo Oaxaca)</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>1</b>: Son (<code>fiscalia.sonora.gob.mx</code>) · <b>dominio de la fiscalía no confirmado</b>: <b>2</b>, Coah y Camp (<code>ucs.campeche.gob.mx</code> devuelve páginas: es comunicación social, no la fiscalía)</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>4</b>: Sin, Dgo · Nay · Qro</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 5-nov 09:42: código <code>000</code> (proxy: conexión rechazada)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en las 8 que ARGOS 146 dejó solo con consulta amplia —Nay, Coah, Zac, Hgo, Qro, Oax, Camp, Yuc— · <b>armamento: 13 de 32 por dominio oficial</b> —BC, BCS, Dgo, Sin · Tamps, Zac · Col · CDMX, Edomex · Ver, Tab · Oax, Chis—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> (Tab: <code>tabasco.gob.mx</code> ya devuelve páginas) · dominio sin páginas: Son · dominio no confirmado: Coah · <code>NO REVISADA</code> (17): Chih · NL, SLP · Jal, Nay, Ags, Mich, Gto · Mor, Pue, Tlax, Hgo, Qro · Camp, Gro, Yuc, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 3-nov</b>: existe (<code>gob.mx/sspc</code>, por índice; Milenio, Tallapolítica, Certeza Diario): ventana de ARGOS 146 · <b>acciones del 4-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título, al inicio y al cierre · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 5-NOV 09:42: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Cuatro rojos propios en tres entidades</b> (cálculo propio), por víctima autoridad, drones y homicidio múltiple. <b>Riesgo nacional sostenido frente a ARGOS 146</b>: 0,15 rojos por hora (4 en {DUR}), frente a 0,14 publicado en ARGOS 146 (cálculo propio).
      <br><b>2.</b> <b>Michoacán</b> concentra dos de los cuatro rojos (ARG-147-002 y -004); <b>Guerrero</b>, un rojo y un amarillo en la misma jornada (ARG-147-003 y -007).
      <br><b>3.</b> <b>Violencia operativa</b>: seis amarillos en tres entidades; cuatro en Sinaloa, en Culiacán y Mazatlán (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: un verde, de fuente única, sin cifra de armamento ni de detenidos citable; ninguna sentencia integrable; ningún boletín federal de acciones del 4-nov indexado (cálculo propio).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()}: DIEZ DE ONCE HECHOS PUBLICADOS EL DÍA DE APERTURA SIN HORA, CON CLÁUSULA DE RETIRO, Y UNO EN FRONTERA DE VENTANA; TRES ROJOS RECUPERADOS DE ARGOS 146, CON 7 MUERTOS, FUERA DE TOTALES. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. MICHOACÁN: EMPLEO DE DRONES ENTRE GRUPOS CRIMINALES EN EL ORIENTE DEL ESTADO Y VIOLENCIA LETAL EN LA FRANJA AGUACATERA, EN LA MISMA JORNADA</b> (ARG-147-004 y -002); vínculo no acreditado. Línea: <b>solicitar a la Defensa y a la Guardia Civil el registro de drones del 4-nov en Indaparapeo y cruzarlo con ARG-140-016 y ARG-144-002, en el mismo municipio</b>.
      <br><b>2. VÍCTIMA SERVIDOR PÚBLICO CON DENUNCIA PREVIA DE AMENAZAS, POR TITULAR</b> (ARG-147-001): perfil de víctima de riesgo. Línea: <b>solicitar a la Fiscalía de Morelos el estado de esas denuncias y verificar medidas de protección de los demás integrantes del cabildo</b>.
      <br><b>3. SINALOA: EXPLOSIVOS ARTESANALES CONTRA UNA VIVIENDA, CON UN ARTEFACTO LOCALIZADO JUNTO A ELLA, POR TITULAR, Y CUATRO HOMICIDIOS DOLOSOS ÚNICOS EN CULIACÁN Y MAZATLÁN PUBLICADOS EL 4-NOV</b> (ARG-147-REC-003, -006 y -008 a -010); vínculo no acreditado. Línea: <b>solicitar a la FGE de Sinaloa el dictamen del artefacto (carga, iniciador, fabricación local) y vigilar el Mercado Hidalgo y Coto Premier</b>.
      <br><b>4. GUERRERO: EJE CENTRO–MONTAÑA CON HALLAZGO DE VÍCTIMAS TORTURADAS Y GRUPOS ARMADOS CON CHALECO Y ARMA LARGA</b> (ARG-147-003 y -007; «varios municipios», por titular; cinco, solo por resumen). Línea: <b>vigilar el corredor Chilpancingo–Tixtla–Olinalá</b>.
      <br><b>5. BLANCOS CON CONCURRENCIA DE PERSONAS: UN EXPENDIO DE BEBIDAS Y DOS CENTROS DE REHABILITACIÓN EL 1-NOV, DÍA SOLO POR RESUMEN, 7 MUERTOS</b> (cálculo propio; ARG-147-REC-001 y -002); vínculo no acreditado. Línea: <b>vigilar centros de rehabilitación de Mazatlán y solicitar la situación jurídica de los presuntos detenidos de Champotón</b>.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: CUERNAVACA, TANCÍTARO, CHILPANCINGO E INDAPARAPEO", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA: PÉNJAMO, OLINALÁ Y CULIACÁN", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA EN MAZATLÁN Y ACCIONES INSTITUCIONALES", co2b)
 + page("CRIMEN ORGANIZADO (IV) — ALTO IMPACTO DE LA VENTANA DE ARGOS 146: CHAMPOTÓN Y MAZATLÁN", co3)
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
assert script.count("WINDOW_DAYS = 5;") == 1, "plantilla de 146 con WINDOW_DAYS = 5"
script = script.replace("WINDOW_DAYS = 5;", "WINDOW_DAYS = 2;")
assert "WINDOW_DAYS = 2;" in script and "WINDOW_DAYS = 5;" not in script  # la ventana toca dos fechas de calendario (4 y 5-nov)
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
