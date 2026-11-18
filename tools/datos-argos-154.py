# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 154.
Uso: python3 tools/datos-argos-154.py <plantilla ARGOS 153> <salida>
Ventana: 17-nov 11:34 → 18-nov 12:32 CDMX. Archivo: argos-2026-11-18.html.
La hora de «Consulta» se fija al cierre de procedencia-cifras R2 con la variable ARGOS_CONSULTA (HH:MM)."""
import sys, re, json, os, html as H

NUM, FECHA, HORA = "154", "2026-11-18", "12:32"
CONSULTA = "2026-11-18, última búsqueda " + os.environ.get("ARGOS_CONSULTA", "__CONSULTA__")
DUR = "24 h 58 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 11:34 DEL 17, ES DE LA VENTANA DE ARGOS 153 Y SE RETIRA DE ESTE TOTAL</code>"
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
 dict(id="ARG-154-001", estado="MX-GRO", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-17", hora="tarde, ~17:00 (solo por resumen)", mu=0, he=0, cu=0, hk=17,
  ent="Guerrero", mun="Taxco de Alarcón (av. Pedro Mártir)", dia="MAR 17-NOV, POR RUTA",
  fecha_txt="martes 17-nov, por ruta; tarde, ~17:00, solo por resumen",
  title="GUERRERO · TAXCO — DISPARAN DESDE UN VEHÍCULO CONTRA AGENTES DE LA POLICÍA INVESTIGADORA MINISTERIAL EN UN FILTRO DE SEGURIDAD",
  hecho="Taxco de Alarcón · <code>AV. PEDRO MÁRTIR, FILTRO DE SEGURIDAD</code>, " + RES + " · martes 17-NOV, por ruta (La Silla Rota 2026/11/17: «Emboscada en Taxco: comando ataca a agentes de la fiscalía de Guerrero»; El Diario de Chihuahua 2026/nov/17: «Embosca grupo armado a agentes ministeriales en Taxco, Gro») · tarde, ~17:00, " + RES + " · " + AP + " · disparos desde un vehículo en movimiento contra agentes de la Policía Investigadora Ministerial en un filtro, por titular (Diario Amanecer: «Atacan a balazos a policías ministeriales durante filtro de seguridad en Taxco; aseguran 12 casquillos») (🔴 ataque contra autoridades) · <b>ningún lesionado</b>, según la FGE de Guerrero, " + RES + " · 12 casquillos asegurados, por titular · disparos contra la agencia del MP, versión de medios, " + RES + " · agresores huidos · " + NOD,
  panel="<b>Ataque a agentes ministeriales en un filtro</b>, sin lesionados", inst=SB, nac="La Silla Rota · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen; declaración de la Fiscalía solo por resumen", I=0, N=2, R=4, A=0,
  fechadas=["La Silla Rota (2026/11/17)", "El Diario de Chihuahua (2026/nov/17)", "Luces del Siglo (2026/11/18)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — casquillos: evidencia balística, no munición útil ni arma asegurada",
  desl="Taxco figura en ARG-130-003 (ranchería Taxco, Nacajuca, Tab.: homónimo) y en ARG-136-008/-009 (detenciones): otros hechos. El Diario de Chihuahua y El Diario del Noroeste reproducen la misma nota de agencia: una sola fuente. Célula criminal en Taxco, solo por medios: autoría no acreditada."),
 dict(id="ARG-154-002", estado="MX-GRO", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-17", hora="noche del 17 o primeras horas del 18, contradicho (solo por resumen)", mu=2, he=0, cu=0, hk=21,
  ent="Guerrero", mun="Xochistlahuaca (Arroyo Grande)", dia="MAR 17 O MIÉ 18-NOV, CONTRADICHO",
  fecha_txt="noche del martes 17 o primeras horas del miércoles 18, DÍA CONTRADICHO, SOLO POR RESUMEN; publicación 18-nov, por ruta",
  title="GUERRERO · XOCHISTLAHUACA — ASESINAN A UN ASPIRANTE A COORDINADOR MUNICIPAL DE MORENA Y A SU ACOMPAÑANTE TRAS UNA ASAMBLEA",
  hecho="Xochistlahuaca · <code>ARROYO GRANDE, CAMINO TRAS UNA ASAMBLEA</code>, " + RES + " · noche del martes 17-NOV o primeras horas del miércoles 18: <code>DÍA CONTRADICHO</code>, " + DSR + "; ambos dentro de la ventana · publicación 18-NOV, por ruta (El Sol de Chilpancingo 2026/11/18: «Asesinan a aspirante de Morena en Xochistlahuaca») · " + FR + " · <b>2 hombres muertos</b>: un aspirante a coordinador municipal de Morena y un acompañante, por titular (El Sur: «Matan a tiros a aspirante de Morena en Xochitlahuaca y a un acompañante») (🔴 homicidio múltiple) · interceptados en una camioneta, " + RES + " · Ejército y GN en vigilancia, " + RES + " · " + NOD,
  panel="<b>Doble homicidio</b>: aspirante partidista y acompañante", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="día y hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["El Sol de Chilpancingo (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Xochistlahuaca no figura en las ediciones previas. La víctima principal no es servidor público según las fuentes: el color lo fija el número de víctimas. Nombres: discrepantes entre medios, no se reproducen."),
 dict(id="ARG-154-003", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-17", hora="~18:00–18:15 (solo por resumen)", mu=2, he=0, cu=0, hk=18,
  ent="Sinaloa", mun="Culiacán (col. Vista Hermosa)", dia="MAR 17-NOV, POR RUTA",
  fecha_txt="martes 17-nov, por ruta; ~18:00–18:15, solo por resumen",
  title="SINALOA · CULIACÁN — ATACAN A UN CLIENTE EN UN PUESTO DE ESQUITES DE VISTA HERMOSA: MUEREN ÉL Y LA VENDEDORA",
  hecho="Culiacán · <code>COL. VISTA HERMOSA, BLVD. AGRICULTORES, PUESTO DE ESQUITES</code>, por titular (Noroeste: «Ataque armado en puesto de esquites deja un muerto y una mujer herida en el bulevar Agricultores, en Culiacán») · martes 17-NOV, por ruta (Ríodoce 2026/11/17: «Un hombre muerto y una mujer herida en puesto de esquites en Vista Hermosa, en Culiacán») · ~18:00–18:15, " + RES + " · " + AP + " · <b>2 muertos</b>: el cliente atacado y la vendedora, que muere en el hospital, por titular (Quinto Poder 2026/11/17: «Balacera en Culiacán: ataque armado en puesto de elotes deja dos muertos»; Noroeste: «Muere vendedora de esquites tras ataque a balazos en el bulevar Agricultores, en Culiacán») · <code>SALDO DE MUERTOS ACTUALIZADO: 1 EN EL PRIMER PARTE, 2 EN EL SEGUNDO, POR TITULAR — SE INTEGRAN 2</code> (🔴 homicidio múltiple) · la vendedora «habría sido víctima colateral», según la Fiscalía de Sinaloa, por titular (Noticiero Altavoz) · Ejército acordona; casquillos de grueso calibre, " + RES + " · " + NOD,
  panel="<b>Ataque en un puesto callejero: 2 muertos</b>, una colateral", inst="Fiscalía de Sinaloa" + TM, nac="N+", conf="★★★☆☆",
  campo="hora solo por resumen; declaración de la Fiscalía solo por titular de medio", I=1, N=1, R=5, A=0,
  fechadas=["Ríodoce (2026/11/17)", "Quinto Poder (2026/11/17)", "Luz Noticias (2026-11-18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Vista Hermosa no figura en las ediciones previas. «Ataques armados a negocios en Culiacán dejan tres muertos» (López Dóriga; Plaza de Armas): balance de dos hechos, no es fuente. Con 1 muerto, el hecho sería 🟡. Un medio lo sitúa el miércoles 18: contradice al resto. Identidades: discrepantes, no se reproducen."),
 dict(id="ARG-154-004", estado="MX-MEX", region="Centro", color="rojo", impacto="grande", fecha="2026-11-17", hora="tarde (solo por resumen)", mu=2, he=1, cu=0, hk=16,
  ent="Estado de México", mun="Chalco (centro, frente al Palacio Municipal)", dia="MAR 17-NOV, POR RUTA",
  fecha_txt="martes 17-nov, por ruta; tarde, solo por resumen",
  title="ESTADO DE MÉXICO · CHALCO — INTENTO DE ASALTO A UNA JOYERÍA FRENTE AL PALACIO MUNICIPAL: DOS MUERTOS",
  hecho="Chalco · <code>CENTRO, FRENTE AL PALACIO MUNICIPAL, JOYERÍA</code>, por titular (Cúspide 2026/11/17: «Balacera afuera del Palacio Municipal de Chalco deja un muerto y dos heridos.») · martes 17-NOV, por ruta (Cúspide; Reporteros en Movimiento 2026/11/17) · tarde, " + RES + " · " + AP + " · intento de asalto a una joyería, por titular (El Universal: «Intento de asalto a joyería en Chalco deja dos muertos») · <b>2 muertos</b>, saldo actualizado, por titular (El Universal; Red Metropolitana 2026/11/18: «Asalto a joyería desata balacera y deja dos muertos en Chalco»), frente a 1 en el primer parte (Cúspide): <code>SALDO DE MUERTOS ACTUALIZADO: 1 EN EL PRIMER PARTE, 2 EN EL SEGUNDO, POR TITULAR — SE INTEGRAN 2</code> (🔴 homicidio múltiple) · una víctima, trabajadora de la joyería, muere en el traslado, " + RES + " · heridos: 1, por titular (El Universal Edomex: «Intento de asalto a joyería deja dos muertos y un herido en Chalco»), 2 (Digitalmex) o 3 peatones (" + RES + "): <code>CIFRA DE HERIDOS CONTRADICHA — SE INTEGRA 1, MÍNIMO COINCIDENTE</code> · agresores huidos en motocicleta · la FGJEM investiga, " + RES + " · " + NOD,
  panel="<b>Asalto a una joyería: 2 muertos y 1 herido</b>", inst=SB, nac="El Universal · Milenio · TV Azteca", conf="★★★☆☆",
  campo="hora solo por resumen; heridos contradichos; ninguna fuente institucional", I=0, N=3, R=4, A=0,
  fechadas=["Cúspide (2026/11/17)", "Reporteros en Movimiento (2026/11/17)", "Red Metropolitana (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chalco figura por ARG-101-009 (agosto): otro hecho. N+ y Telediario («hoy 17 de noviembre»): liveblogs, no fechan ni sostienen cifras. Nombre del comercio, contradicho entre medios. Con 1 muerto, el hecho sería 🟡. Identidades: no se reproducen."),
 dict(id="ARG-154-005", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-17", hora="aviso ~11:30 (solo por resumen)", mu=2, he=0, cu=0, hk=11,
  ent="Sinaloa", mun="Mazatlán (fracc. Santa Teresa)", dia="MAR 17-NOV, POR RUTA",
  fecha_txt="martes 17-nov, por ruta; aviso ~11:30, solo por resumen, en la frontera de apertura",
  title="SINALOA · MAZATLÁN — ASESINAN A MADRE E HIJA DENTRO DE SU VIVIENDA EN SANTA TERESA, FRENTE A UNA SECUNDARIA",
  hecho="Mazatlán · <code>FRACC. SANTA TERESA, VIVIENDA FRENTE A UNA SECUNDARIA</code>, por titular (Infobae 2026/11/18: «Madre y su hija son asesinadas frente a una secundaria en Mazatlán…») · martes 17-NOV, por ruta (Línea Directa 2026-11-17) · aviso ~11:30, " + RES + " · " + AP + " · " + RET + " · <b>2 mujeres muertas, madre e hija</b>, por titular (Noroeste: «Matan a madre e hija en vivienda del fraccionamiento Santa Teresa, en Mazatlán») (🔴 homicidio múltiple) · agresión dentro del domicilio; número de agresores contradicho, " + RES + " · la alcaldesa de Mazatlán lamenta el asesinato, por titular (Línea Directa 2026-11-17) · clases suspendidas en la escuela de enfrente, " + RES + " · " + NOD,
  panel="<b>Doble homicidio en vivienda</b>: madre e hija", inst=SB, nac="Infobae", conf="★★★☆☆",
  campo="hora solo por resumen, en la frontera de apertura; ninguna fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["Línea Directa (2026-11-17)", "Infobae (2026/11/18)", "Revista Espejo (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Santa Teresa no figura en las ediciones previas; Mazatlán, por ARG-153-005 (Los Magueyes) y ARG-152-005 (col. Pueblo Nuevo): otros hechos. Edad de la madre, contradicha. Identidades: medios, no se reproducen."),
 dict(id="ARG-154-006", estado="MX-ROO", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-18", hora="no fijada", mu=3, he=0, cu=0, hk=6,
  ent="Quintana Roo", mun="Cancún, Benito Juárez (Villas Otoch, Región 247)", dia="MIÉ 18-NOV, POR RUTA",
  fecha_txt="miércoles 18-nov, por ruta; hora no fijada",
  title="QUINTANA ROO · CANCÚN — ASESINAN A TRES HOMBRES A BORDO DE UNA CAMIONETA EN VILLAS OTOCH, REGIÓN 247",
  hecho="Cancún, Benito Juárez · <code>VILLAS OTOCH, REGIÓN 247, AV. EUCALIPTO</code>, por titular (PorEsto 2026/11/18: «Ataque armado en la Región 247 de Cancún deja tres hombres sin vida»; Sol Quintana Roo: «Ataque armado deja tres muertos en Villas Otoch») · miércoles 18-NOV, por ruta (PorEsto) · hora no fijada · " + FR + " · <b>3 hombres muertos</b> a bordo de una camioneta, por titular (Turquesa News: «Ejecutan a tres hombres dentro de una camioneta en la Región 247 de Cancún») (🔴 homicidio múltiple) · la camioneta se impacta tras el ataque, " + RES + " · Policía Ministerial y peritos de la FGE; cuerpos al Semefo sin identificar, " + RES + " · " + NOD,
  panel="<b>Ataque a una camioneta: 3 muertos</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional ni nacional", I=0, N=0, R=5, A=0,
  fechadas=["PorEsto (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Villas Otoch figura solo como visto en ARGOS 152 (2 detenidos, 16-nov): otro hecho. Identidades: no establecidas."),
 dict(id="ARG-154-007", estado="MX-VER", region="Golfo", color="rojo", impacto="grande", fecha="2026-11-18", hora="primeras horas (solo por resumen)", mu=0, he=0, cu=0, hk=7,
  ent="Veracruz", mun="Poza Rica, Tihuatlán, Papantla, Cazones de Herrera y Tuxpan", dia="MIÉ 18-NOV, POR RUTA",
  fecha_txt="miércoles 18-nov, por ruta; primeras horas, solo por resumen",
  title="VERACRUZ · POZA RICA — NARCOBLOQUEOS CON QUEMA DE VEHÍCULOS Y PONCHALLANTAS EN CINCO MUNICIPIOS DEL NORTE DEL ESTADO",
  hecho="Poza Rica, Tihuatlán, Papantla, Cazones de Herrera y Tuxpan · <code>PUENTES CAZONES 1 Y 2, CARRETERA POZA RICA–PAPANTLA, AUTOPISTA TUXPAN–TOTOMOXTLE</code>, " + RES + " · miércoles 18-NOV, por ruta (PorEsto 2026/11/18: «Narcobloqueos en Veracruz: incendian vehículos y colocan ponchallantas en carreteras de cinco municipios») · primeras horas, " + RES + " · " + FR + " · <b>bloqueos con vehículos incendiados y ponchallantas en cinco municipios</b>, por titular (🔴 narcobloqueo y quema de vehículos) · vehículos incendiados: 3 según la SSP, " + RES + "; «al menos 4» en medios: <code>CANTIDAD NO DETERMINADA</code> · sin lesionados, " + RES + " · la SSP despliega operativo con fuerzas federales y municipales, por titular (El Demócrata: «Reportan quema de vehículos y bloqueos en Poza Rica, SSP implementa operativo») · reacción a una detención federal: versión extraoficial, no confirmada · " + NOD,
  panel="<b>Narcobloqueos y quema de vehículos</b> en cinco municipios", inst="SSP de Veracruz" + TM, nac="El Universal · UnoTV · Milenio · Aristegui", conf="★★★☆☆",
  campo="hora no fijada; cifra de vehículos solo por resumen", I=1, N=4, R=4, A=0,
  fechadas=["PorEsto (2026/11/18)", "Seunonoticias (2026/11/18)", "Luces del Siglo (2026/11/18)", "Aristegui (1811)"], estatus="Parcialmente corroborado", arm=None,
  desl="Poza Rica figura por hechos de agosto (ARG-102-001, ARG-103-003, ARG-107-001, ARG-108-005): otros hechos. «Al menos 6» vehículos (Todo Texcoco): no se integra."),
 dict(id="ARG-154-008", estado="MX-TAM", region="Noreste", color="rojo", impacto="grande", fecha="2026-11-17", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Tamaulipas", mun="Río Bravo (cuatro puntos de concentración)", dia="MAR 17-NOV, POR RESUMEN",
  fecha_txt="hallazgo martes 17-nov, DÍA SOLO POR RESUMEN; publicación 18-nov, por ruta; hora no fijada",
  title="TAMAULIPAS · RÍO BRAVO — COLECTIVOS HALLAN RESTOS HUMANOS CALCINADOS EN CUATRO PUNTOS DE CONCENTRACIÓN",
  hecho="Río Bravo · <code>CUATRO PUNTOS DE CONCENTRACIÓN DE RESTOS</code>, por titular (N+: «Colectivos Localizan Cuatro Concentraciones de Restos Óseos en Río Bravo, Tamaulipas») · hallazgo «este martes» 17-NOV, " + DSR + " · publicación 18-NOV, por ruta (Elefante Blanco 2026/11/18: «Río Bravo suma otro hallazgo de restos humanos quemados») · hora no fijada · " + FR + " · " + RET + " · <b>restos óseos humanos calcinados</b>, por titular (Síntesis del Golfo: «Encuentran restos humanos calcinados en una zona de exterminio en Río Bravo») (🔴 hallazgo de restos humanos) · <code>NÚMERO DE VÍCTIMAS NO DETERMINADO</code> · hallazgo de los colectivos Amor por los Desaparecidos en Tamaulipas y Amor, Paz y Esperanza; prendas para identificación; sin levantamiento total informado por la fiscalía, " + RES + " · " + NOD,
  panel="<b>Hallazgo de restos humanos calcinados</b>, número no determinado", inst=SB, nac="N+", conf="★★★☆☆",
  campo="día del hallazgo solo por resumen; número de víctimas no determinado; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["Elefante Blanco (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Río Bravo figura por los narcobloqueos de octubre (ARG-144-008): otro hecho. Reynosa, Puerta Sur (ARG-140-008, octubre): otro sitio; vínculo no acreditado. Sitios de Río Bravo de 2024 y 2025: anteriores."),
 # ======================= AMARILLOS
 dict(id="ARG-154-009", estado="MX-JAL", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-18", hora="madrugada, ~05:00 (solo por resumen)", mu=0, he=0, cu=0, hk=5,
  ent="Jalisco", mun="Zapopan (col. Ciudad del Sol)", dia="MIÉ 18-NOV, POR RUTA",
  fecha_txt="madrugada del miércoles 18-nov, por ruta; ~05:00, solo por resumen",
  title="JALISCO · ZAPOPAN — ENFRENTAMIENTO DURANTE UN OPERATIVO DE MARINA EN CIUDAD DEL SOL: TRES AGRESORES ABATIDOS",
  hecho="Zapopan · <code>COL. CIUDAD DEL SOL, LÍMITE CON JARDINES DEL SOL</code>, por titular (Informador 20261118: «Enfrentamiento en Ciudad del Sol, Zapopan: SSPC confirma tres agresores abatidos tras balacera»; Mural: «Se enfrentan Marina y civiles armados en Jardines del Sol») · madrugada del miércoles 18-NOV, por ruta (Informador 20261118; quierotv 2026/11/18) · ~05:00, " + RES + " · " + FR + " · Marina, SSPC y AIC ejecutan una orden de aprehensión y son agredidos, " + RES + " (🟡 confrontación derivada de un operativo) · <b>3 agresores abatidos</b>, por titular (Informador; Infobae 2026/11/18: «…desata enfrentamiento con la Marina en Zapopan: hay tres delincuentes muertos»); 2 en el primer parte (POSTA) · balacera de 40 minutos, por titular (Diario Puntual 2026/11/18) · ningún elemento lesionado publicado · detención: ver ARG-154-011",
  panel="Operativo federal repelido: <b>3 agresores abatidos</b>", inst="SSPC" + TM, nac="Infobae · Reforma · Excélsior · Meganoticias", conf="★★★☆☆",
  campo="hora y quién inició, solo por resumen; declaración institucional solo por titular de medio", I=1, N=4, R=3, A=0,
  fechadas=["Informador (20261118)", "Infobae (2026/11/18)", "Diario Puntual (2026/11/18)", "quierotv (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ciudad del Sol no figura en las ediciones previas; Zapopan, por ARG-149-018 (operativo contra «El R2») y ARG-149-014 (orden de la Marina en un restaurante): otros hechos. Los agresores abatidos no se suman a «muertos por agresión». Telediario («…hoy»): liveblog, no fecha."),
 dict(id="ARG-154-010", estado="MX-VER", region="Golfo", color="amarillo", impacto="mediano", fecha="2026-11-17", hora="poco antes de las 18:00 (solo por resumen)", mu=1, he=0, cu=0, hk=18,
  ent="Veracruz", mun="Coatzacoalcos (col. Independencia)", dia="MAR 17-NOV, POR RUTA",
  fecha_txt="martes 17-nov, por ruta; poco antes de las 18:00, solo por resumen",
  title="VERACRUZ · COATZACOALCOS — ASESINAN A BALAZOS A UN MECÁNICO EN LA COLONIA INDEPENDENCIA",
  hecho="Coatzacoalcos · <code>COL. INDEPENDENCIA, CALLE CRISTÓBAL COLÓN</code>, " + RES + " · martes 17-NOV, por ruta (La Silla Rota 2026/11/17: «Matan a balazos a mecánico de Coatzacoalcos; esto se sabe»; Municipiosur 2026/11/17) · poco antes de las 18:00, " + RES + " · " + AP + " · <b>1 hombre muerto</b>, mecánico, por titular (Diario de Minatitlán 2026/11/18: «Ejecutan a mecánico en Coatzacoalcos») (🟡 homicidio doloso único) · agresor único, huye, " + RES + " · " + NOD,
  panel="<b>Hombre asesinado</b> a balazos", inst=SB, nac="La Silla Rota", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["La Silla Rota (2026/11/17)", "Municipiosur (2026/11/17)", "Diario de Minatitlán (2026/11/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Independencia no figura en las ediciones previas. «Suman 51 muertes violentas en 2026» (VeracruzInforma): recuento de medios, no se integra. Identidad: no se reproduce."),
 # ======================= VERDES
 dict(id="ARG-154-011", estado="MX-JAL", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-18", hora="madrugada (solo por resumen)", mu=0, he=0, cu=0, hk=5,
  ent="Jalisco", mun="Zapopan (Ciudad del Sol y otros dos puntos)", dia="MIÉ 18-NOV, POR RUTA",
  fecha_txt="miércoles 18-nov, por ruta; madrugada, solo por resumen",
  title="JALISCO · ZAPOPAN — CAPTURAN A UN PRESUNTO LÍDER DE CÉLULA DE «LOS DELTAS» (CJNG), CON ÓRDENES POR EL SECUESTRO DE UN PERIODISTA",
  hecho="Zapopan · <code>CIUDAD DEL SOL Y OTROS DOS PUNTOS</code>, " + RES + " · miércoles 18-NOV, por ruta (El Independiente 2026/11/18: «Harfuch confirma detención de … líder de Los Deltas») · " + FR + " · <b>captura de un presunto líder de una célula de «Los Deltas» (CJNG)</b>, por titular (Parabólica: «…uno de los líderes de \"Los Deltas\", brazo armado del CJNG: Harfuch»), con órdenes de aprehensión por el secuestro de un periodista y de un empresario, " + RES + " · detenidos: 3, por titular de la declaración del secretario de Seguridad (Sinaloahoy: «Omar García Harfuch informa detención de … y dos personas tras enfrentamiento en Zapopan»), frente a 4 (SSPC), 5 (Marina, en tres intervenciones) o 6 (gobernador), " + RES + ": <code>CIFRA DE DETENIDOS CONTRADICHA</code> · Marina, SSPC y AIC · el gobernador reconoce la colaboración federal, por titular (Informador 20261118) · armamento: seis armas cortas, cargadores y cartuchos, " + RES + ": <code>CANTIDAD NO CITABLE — NO SE INTEGRA</code>",
  panel="<b>Captura de un presunto líder de célula</b>; 3 a 6 detenidos, contradicho", inst="SSPC (secretario)" + TM, nac="Excélsior · Infobae · Publimetro", conf="★★★☆☆",
  campo="cifra de detenidos contradicha; declaración institucional solo por titular de medio", I=1, N=3, R=2, A=0,
  fechadas=["El Independiente (2026/11/18)", "Heraldo de México (2026/11/18)", "Publimetro (2026/11/18)", "Informador (20261118)"], estatus="Parcialmente corroborado", arm=None,
  desl="Mismo operativo que ARG-154-009: la detención se ficha aparte. Nombre y alias: autoridad y medios; no se reproducen. El secuestro del periodista es de una ventana anterior: no se recalifica."),
 dict(id="ARG-154-012", estado="MX-GUA", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-18", hora="no fijada", mu=0, he=0, cu=0, hk=9,
  ent="Guanajuato", mun="Acámbaro (San Mateo Tócuaro)", dia="MIÉ 18-NOV, PUBLICACIÓN POR RUTA",
  fecha_txt="publicación miércoles 18-nov, por ruta del boletín estatal; día del hecho no fijado",
  title="GUANAJUATO · ACÁMBARO — DETIENEN A DOS PERSONAS CON UNA PISTOLA Y PRESUNTA DROGA EN SAN MATEO TÓCUARO",
  hecho="Acámbaro · <code>SAN MATEO TÓCUARO</code>, " + RES + " · publicación miércoles 18-NOV, por ruta del boletín estatal (boletines.guanajuato.gob.mx 2026/11/18: «Detienen autoridades estatales y federales a dos personas con arma de fuego y presunta droga en Acámbaro») · día del hecho no fijado · " + FR + " · <b>2 detenidos</b>, por titular del boletín estatal · <b>1 arma corta</b> (pistola 9 mm), por titular (Rotativo: «Detienen a dos con pistola 9 mm y presunta marihuana en Acámbaro, Guanajuato») · cargador y cartuchos, " + RES + " · FSPE y Defensa",
  panel="<b>2 detenidos con un arma corta</b> y presunta droga", inst="Gobierno de Guanajuato <span class=\"muted-note\">(boletín, por búsqueda dirigida)</span>", nac="—", conf="★★★☆☆",
  campo="día del hecho no fijado; cargador y cartuchos solo por resumen", I=1, N=0, R=2, A=0,
  fechadas=["Gobierno de Guanajuato, boletín (2026/11/18)"], estatus="Parcialmente corroborado", arm="ARG-154-ARM-001",
  desl="Tócuaro no figura en las ediciones previas; Acámbaro, por ARG-101-007, ARG-142-004 y ARG-143-REC-003: otros hechos. boletines.guanajuato.gob.mx es del gobierno estatal, no de la fiscalía."),
]
R = []
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-154-ARM-001", ficha="ARG-154-012", estado="MX-GUA", region="Occidente", color="verde", ent="Guanajuato", mun="Acámbaro (San Mateo Tócuaro)",
  fecha="2026-11-18", fecha_txt="pub. 18-nov, por ruta; día del hecho no fijado", hora="no fijada", c=[1, 0, 0, 0, 0, 0, 0, 0, 0, 2], nd=[4, 5], integra=True,
  corp="FSPE y Defensa <span class=\"muted-note\">(boletín estatal)</span>", conf="Medio",
  nota="arma corta por titular de medio; «arma de fuego» y 2 detenidos por titular del boletín estatal; cargador y cartuchos solo por resumen: n/d; FRONTERA DE VENTANA — HORA NO FIJADA",
  fuentes=["Gobierno de Guanajuato (2026/11/18)", "TV4 Noticias", "Rotativo"]),
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
HORAS = 24 + 58 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
assert TOT == [1, 0, 0, 0, 0, 0, 0, 0, 0, 2] and ND == [False] * 4 + [True, True] + [False] * 4 and ARMAS == 1, (TOT, ND)
assert cnt == {"rojo": 8, "amarillo": 2, "verde": 2}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0} and R == [], cnt_rec
assert (MU, HE, CU) == (12, 1, 0), (MU, HE, CU)
assert DENS == "0,48" and RPH == "0,32", (DENS, RPH)
assert (NAP, NFR, NRET) == (5, 7, 2), (NAP, NFR, NRET)
assert len(ENT) == 8 and len(ENT_ROJO) == 6, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-154-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-17" <= x["fecha"] <= "2026-11-18", x["id"]
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
head = head.replace("<title>ARGOS 153 — Reporte Nacional de Seguridad — 2026-11-17</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA SSP DE VERACRUZ EL SALDO OFICIAL DE VEHÍCULOS INCENDIADOS, PUNTOS BLOQUEADOS Y DETENIDOS DE LOS BLOQUEOS DEL NORTE DEL ESTADO</b> (ARG-154-007).
      <br><b>2. SOLICITE A LA FISCALÍA DE GUERRERO EL PARTE DEL ATAQUE AL FILTRO MINISTERIAL DE TAXCO Y EL COTEJO BALÍSTICO DE LOS CASQUILLOS ASEGURADOS</b> (ARG-154-001).
      <br><b>3. SOLICITE A LA FISCALÍA DE TAMAULIPAS EL LEVANTAMIENTO FORMAL DE LOS RESTOS DE RÍO BRAVO Y SU INGRESO AL REGISTRO DE IDENTIFICACIÓN GENÉTICA</b> (ARG-154-008).
      <br><b>4. SOLICITE AL GABINETE DE SEGURIDAD LA CIFRA OFICIAL DE DETENIDOS Y ASEGURAMIENTOS DEL OPERATIVO DE ZAPOPAN</b> (ARG-154-009 y -011).
      <br><b>5. SOLICITE A LA FISCALÍA DE SINALOA LA HORA OFICIAL DEL DOBLE HOMICIDIO DE SANTA TERESA, MAZATLÁN</b> (ARG-154-005).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>17-nov 11:34 → 18-nov 12:32 CDMX</b> (<b>{DUR}</b>) · mar 17 (desde 11:34) · mié 18 (hasta 12:32) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
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
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b> + restos sin número</td><td><b>{tv(0)}</b></td><td><b>{tv(1)}</b></td><td><b>{tv(2)}</b></td><td><b>{tv(4, fmt)}</b></td><td><b>{tv(5)}</b></td><td><b>{tv(6)}</b></td><td><b>{tv(7)}</b></td><td><b>{tv(8)}</b></td><td><b>{tv(9)}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: desglose en el módulo · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas; los 3 agresores abatidos en Zapopan no se suman · <b>heridos</b>: {HE}; en Chalco, el mínimo coincidente · <b>cuerpos</b>: restos calcinados en Río Bravo, <code>NÚMERO NO DETERMINADO</code>, aparte de los muertos por agresión · <b>detenidos fuera de aseguramiento</b>: Zapopan, de 3 a 6, contradicho, no se suman · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> (publicados el día de cierre) · <b>totales sujetos a {NRET} cláusulas de retiro</b> (Mazatlán: aviso ~11:30 solo por resumen; Río Bravo: día del hallazgo solo por resumen).
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: «Ataques armados a negocios en Culiacán dejan tres muertos» (López Dóriga; Plaza de Armas; miguelangelluna 2026/11/18) · «casi media docena de homicidios en menos de 24 hrs» en Ciudad Juárez (Canal 44) · «Ataques armados en bares de Cancún han dejado seis muertos…» (PorEsto 2026/11/17) · «195 detenidos y 27 armas aseguradas en primera quincena de noviembre» en Puebla (Diario Cambio) · «Reportan 35 personas detenidas en solo una semana en Guerrero» (Quadratín Guerrero) · «…mil 220 detenciones en Tabasco» (Diario de Tabasco 2026/11/17) · «Colectivos hallan restos de 9 personas en fosas clandestinas en Baja California» (Grupo Animal; brigada del 1 al 14-nov).
    <br><b>Vistos, fuera de totales</b> (sin ruta con día, fuente única o ventana anterior): Tijuana, col. Gran Tenochtitlán, hombre herido, madrugada del 18 {RES}; «Hombre resulta herido tras ataque armado en Tijuana», por titular (Periodismo Negro 2026/11/18): {FU} · Culiacán, col. Agrarista, trabajador asesinado en un negocio, tarde-noche del 17 {RES}, sin ruta propia · Tehuitzingo, Pue., hombre asesinado frente al zócalo, martes {RES}, sin ruta con día · Mexquitic de Carmona, SLP, mujer asesinada, martes 17 {RES} · Tlapehuala, Gro., cuerpo de un hombre en el río Balsas, «ayer», por El Sur, sin ruta; sin causa informada · Cajeme, joven de 18 años asesinado, noche del 17 {RES}, sin ruta · Tecate, detención de un buscado por tres homicidios, «hoy 18» {RES}, sin ruta · Nextlalpan, Edomex, 4 detenidos con armas y presunta droga, sin fecha en la ruta · Chilpancingo, armados disparan al aire e intentan incendiar un auto, sin ruta · <b>ventana de ARGOS 153</b>: Cosoleacaque, fracc. Los Prados, hombre asesinado en un auto, noche del lunes 16 {RES}: «…el homicidio ocurrió en la misma calle donde hace una semana se registró otro…», por titular (Municipiosur 2026/11/18): <b>otro hecho que ARG-149-013</b>, no duplicidad · Ciudad Juárez, Anapra, hombre quemado y asesinado el 16 («Gatilleros queman y asesinan a una tercer persona en Anapra», El Diario de Chihuahua 2026/nov/16); «Descartan vínculo entre homicidios en Anapra», por titular (El Diario de Chihuahua 2026/nov/17): 🟡, otro hecho que ARG-153-004, sin cambio a su saldo; ya en vistos de 153 · Cancún, Villas Otoch Paraíso, cuerpo embolsado y 2 detenidos, madrugada del 17 {RES} · <b>ventanas anteriores</b>: Huitzilac, Mor., búsqueda de la Triple Frontera, «38 hallazgos» de restos humanos en una semana, Comisión de Búsqueda de la CDMX por medios (Zolo Noticias 2026/11/16): 🔴, hallazgos repartidos en varios días, ventana de origen no determinable · Yautepec, Mor., 2 muertos tras una riña en una cabalgata (Informador 20261116; MVS 2026/11/17): 🔴, día y hora {RES}, sin cambio.
    <br><code>FE DE ERRATAS — ARGOS 153</code>: <b>ARG-153-001</b> Santiago Maravatío: <b>2 policías muertos y 1 herido</b>, por titular (El Heraldo de San Luis Potosí 2026/11/17: «Dos muertos tras emboscada a policías en carretera de Guanajuato»; Info7: «Ataque deja dos policías muertos y uno herido en Guanajuato»); ambos en el lugar, ~09:00 {RES} · muertos de 153: 7 → <b>8</b> (cálculo propio) · Galeana: el arsenal visto en 153 (14 armas largas, un fusil .50) tiene cifras casi idénticas a las de un operativo en Nuevo León de enero de 2025 (El Mañana, elmanana.com.mx 2025/1/15); no vinculado por fuente a ARG-152-001: se retira de vistos.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Cajeme (ataque del 10-nov, 🟡, ventana de ARGOS 150)</b>: detenciones ya publicadas el 12-nov (Heraldo de México 2026/11/12) y el 13-nov («suman 5 detenidos», visto de 153); el 17-nov, por titular, «Capturan en Cajeme a los responsables del homicidio de una niña de 6 años y al líder de su célula criminal» (El Imparcial 2026/11/17) y «…detiene a cinco hombres» (Infobae 2026/11/17): <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · <b>Acaponeta (ARG-153-002)</b>: «Fiscalía revela hipótesis sobre la muerte de los 7 hombres de Acaponeta», por titular (Heraldo de México 2026/11/17); sin identificación ni causa · <b>Cuernavaca (ARG-147-001)</b>: «Vinculan a proceso a presunto autor material del asesinato del regidor … en Cuernavaca», por titular (La Razón 2026/11/17); audiencia del martes 17 y prisión preventiva {RES} · <b>Zapopan (ARG-149-018)</b>: 20 vinculados (MVS 2026/11/16); prisión preventiva para 4, por titular (Infobae 2026/11/17), frente a 5 (MVS) {RES} · <b>Texhuacán (ARG-151-001)</b>: «Interviene FGR en investigación por asesinato de regidora de Texhuacan», por titular (Luces del Siglo 2026/11/17); ningún detenido publicado · <b>Tuxpan (ARG-150-019)</b>: 4 detenidos desde el 12-nov, por titular (MVS 2026/11/12; Proceso 2026/11/13); sin vinculación indexada · <b>Tecate (ARG-150-REC-001)</b>: detenido por un «cuádruple homicidio», por titular (En Línea BC 2026/11/16); hecho del 6-nov en Los Encinos {RES}: <code>POSIBLE MISMO CASO — EL SALDO (3 O 4 MUERTOS) NO SE CORRIGE HASTA VALIDACIÓN</code> · <code>NO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
co1 = "\n".join(ficha(byid[f"ARG-154-{i:03d}"]) for i in (1, 7, 8))
co2 = "\n".join(ficha(byid[f"ARG-154-{i:03d}"]) for i in (2, 3, 5))
co3 = "\n".join(ficha(byid[f"ARG-154-{i:03d}"]) for i in (4, 6, 10))
co4 = "\n".join(ficha(byid[f"ARG-154-{i:03d}"]) for i in (9, 11, 12))
assert sorted(re.findall(r'id="(ARG-154-0\d\d)"', co1 + co2 + co3 + co4)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
NDR = "solo por resumen: <b>cantidad no determinada</b>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), "Guanajuato (Acámbaro), por titular"),
 tile(1, "Armas largas", tv(1), NI),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), NDR),
 tile(4, "Cargadores", tv(5), NDR),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>, por titular del boletín estatal"),
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
    <b>Total nacional del corte</b>: en la página de panorama.
    <br><b>Lectura regional</b>: Occidente, 1 arma corta (Guanajuato); demás regiones, ninguna arma integrada. <b>Cálculo propio</b>.
    <br><code>BOLETÍN FEDERAL DE ACCIONES DEL 13, 14 Y 15-NOV: SIN RESULTADO INDEXADO EN VENTANA</code> (día suelto, rango y título, al inicio y al cierre) · acciones del 16: boletín diario indexado solo a través de republicadores («El Gabinete de Seguridad del Gobierno de México informa acciones relevantes del 16 de noviembre de 2026», Certeza Diario; Hoja de Ruta Digital; RED113 2026/11): ventana de ARGOS 153, <b>corroboración débil por construcción</b> · acciones del 17: __FED17__.
    <br><code>VISTOS, NO INTEGRADOS</code>: Zapopan, seis armas cortas, cargadores y cartuchos {RES} (ver ARG-154-011): cantidad no citable · Nextlalpan, Edomex, 4 detenidos con armas, sin fecha en la ruta · San Luis Potosí, col. Julián Carrillo, 6 detenidos con dos armas, 16-nov {RES} (ventana de 153) · Taxco (ARG-154-001), casquillos, y Culiacán (ARG-154-003), casquillos de grueso calibre: evidencia balística, no munición útil ni arma asegurada.
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
      <tr><td><b>Guerrero</b><br>Copanatoyac</td><td>Feminicidio; 1 sentenciado {RES} (balance semanal de Quadratín Guerrero, sin ruta)</td><td>no publicada</td><td>FGE Guerrero <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín en el dominio · semana del 9 al 15-nov, anterior a la ventana</td><td>No confirmado</td></tr>
      <tr><td><b>Sin novedad</b></td><td>Monterrey: dos casos distintos {RES} (col. Bella Vista, MVS 2026/11/13; col. Loma Bonita, MVS 2026/11/17), ya publicados · Tabasco 5119, pederastia: URL individual no identificada · Veracruz, 88 años por secuestro agravado (Hoy Xalapa 2026/11/13): sin boletín · Champotón, 66 años: reparación 7.2 o 7 mdp, contradicha {RES}</td><td>—</td><td>—</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · anteriores a la ventana</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>27 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Chih, Sin, Dgo · NL, Tamps, SLP · Jal, Mich, Gto, Col, Nay, Ags · CDMX, Edomex, Mor, Pue, Tlax, Hgo · Ver, Tab, Camp · Gro, Oax, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> por dominio</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>27</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio sin páginas indexadas</b></td><td>Son (<code>fiscalia.sonora.gob.mx</code>; incluida en las 5 <code>NO REVISADA</code>) · Camp: <code>ucs.campeche.gob.mx</code> devuelve páginas de la Fiscalía, solo de 2020-2021</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>5</b>: BCS, Son · Coah, Zac · Qro</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 18-nov 12:32: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 19 entidades; solo consulta amplia en 12 —BC, Son, Chih, Sin · Coah · Mich, Col, Ags · Tlax, Qro · Camp · Yuc—; <code>NO REVISADA</code> (1): BCS · <b>armamento: 29 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code>; Acámbaro, por boletín del gobierno estatal · <code>NO REVISADA</code> (3): NL, Gto, Col</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 13, 14 y 15-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio y al cierre · acciones del 16: boletín diario solo por republicadores · acciones del 17: __FED17C__ · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 18-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Rojos por agravante</b>: ataque contra autoridades (Guerrero), narcobloqueo con quema de vehículos (Veracruz), hallazgo de restos humanos (Tamaulipas) y homicidio múltiple (Guerrero, Sinaloa, Estado de México y Quintana Roo); {RPH} rojos por hora, frente a 0,16 en ARGOS 153 (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Sureste 3 · Noroeste 2 · Centro 1 · Golfo 1 · Noreste 1 · Occidente 0 (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: un enfrentamiento derivado de un operativo federal (Jalisco) y un homicidio doloso único (Veracruz).
      <br><b>4.</b> <b>Respuesta institucional</b>: acciones en Jalisco y Guanajuato; ninguna sentencia integrable.
      <br><b>5.</b> <code>TOTALES NO COMPARABLES SIN MÁS CON LOS DE OTRAS EDICIONES: HECHOS EN FRONTERA DE VENTANA, PUBLICADOS EL DÍA DE APERTURA SIN HORA Y CON CLÁUSULA DE RETIRO (DETALLE EN TOTALES DEL CORTE). CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. BLOQUEOS SIMULTÁNEOS EN EL NORTE DE VERACRUZ</b> (ARG-154-007): cierres coordinados en varios municipios del norte del estado con quema de vehículos y ponchallantas; reacción a una detención federal, solo versión extraoficial; vínculo no acreditado. Línea: <b>vigilar los puentes Cazones y los accesos de la autopista Tuxpan–Poza Rica ante réplicas</b>.
      <br><b>2. AGRESIÓN A UN PUNTO FIJO DE LA POLICÍA MINISTERIAL EN TAXCO</b> (ARG-154-001): disparos desde un vehículo en movimiento contra un filtro; autoría no informada; célula local, solo por medios; vínculo no acreditado. Línea: <b>vigilar filtros y puntos fijos de la Policía Investigadora Ministerial en la zona norte de Guerrero</b>.
      <br><b>3. VÍCTIMAS COLATERALES Y ATAQUES EN DOMICILIO EN SINALOA</b> (ARG-154-003 y -005): un ataque a un cliente alcanzó a la vendedora; otro, dentro de una vivienda frente a una escuela; móviles no informados; vínculo entre ambos no acreditado. Línea: <b>vigilar ataques a comercio callejero en el bulevar Agricultores de Culiacán</b>.
      <br><b>4. RESISTENCIA ARMADA A CAPTURAS EN LA ZONA METROPOLITANA DE GUADALAJARA</b> (ARG-154-009 y -011): una célula repele un operativo federal de captura; la autoridad atribuye al detenido secuestros previos; vínculo con otras células no acreditado. Línea: <b>vigilar represalias contra personal federal y periodistas en Zapopan</b>.
      <br><b>5. SITIOS DE EXTERMINIO EN LA FRONTERA TAMAULIPECA</b> (ARG-154-008): restos calcinados en varios puntos, hallados por colectivos y sin levantamiento informado por la fiscalía; vínculo con los hallazgos de Reynosa no acreditado. Línea: <b>vigilar los predios rurales de Río Bravo señalados por colectivos y su cadena de custodia</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

FED17 = "<code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título al cierre (último boletín diario: acciones del 16)"
arm2 = arm2.replace("__FED17__", FED17)
sent = sent.replace("__FED17C__", FED17)

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: ATAQUE A AGENTES MINISTERIALES, NARCOBLOQUEOS Y RESTOS HUMANOS", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: HOMICIDIOS MÚLTIPLES EN GUERRERO Y SINALOA", co2)
 + page("CRIMEN ORGANIZADO (III) — HOMICIDIOS EN ESTADO DE MÉXICO, QUINTANA ROO Y VERACRUZ", co3)
 + page("CRIMEN ORGANIZADO (IV) — VIOLENCIA OPERATIVA Y ACCIONES INSTITUCIONALES", co4)
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
# la ventana de 154 toca dos fechas de calendario (17 y 18-nov); la plantilla de 153 ya trae 2: sin reemplazo
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 153 con WINDOW_DAYS = 2"
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
