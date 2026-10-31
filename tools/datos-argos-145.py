# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 145.
Uso: python3 tools/datos-argos-145.py <plantilla ARGOS 144> <salida>
Ventana: 29-oct 11:36 → 31-oct 11:14 CDMX. Archivo: argos-2026-10-31.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "145", "2026-10-31", "11:14"
CONSULTA = "2026-10-31, última búsqueda __CONSULTA__"
DUR = "47 h 38 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 11:36 DEL 29, ES DE LA VENTANA DE ARGOS 144 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-145-001", estado="MX-TAM", region="Noreste", color="rojo", impacto="grande", fecha="2026-10-29", hora="no fijada; captura previa ~11:00 o «mediodía» (solo por resumen)", mu=1, he=2, cu=0, hk=13,
  ent="Tamaulipas", mun="Matamoros (vialidades bloqueadas; carretera Matamoros–Reynosa; acceso al puente Los Indios)", dia="29-OCT, POR RUTA; HORA NO FIJADA",
  title="TAMAULIPAS · MATAMOROS — NARCOBLOQUEOS Y BALACERAS TRAS LA CAPTURA DE «EL TITÁN»: UNA NIÑA MUERTA EN FUEGO CRUZADO; CIVILES MUERTOS AL CHOCAR CONTRA VEHÍCULOS INCENDIADOS",
  hecho="Matamoros · <code>VIALIDADES DE MATAMOROS; CARRETERA MATAMOROS–REYNOSA CERCA DE SOLISEÑO; ACCESO AL PUENTE LOS INDIOS, SOLO POR RESUMEN</code> · jueves 29-OCT, por ruta (Proceso; ABC Noticias; Latinus 2026/10/29) · " + AP + "; hora no publicada: " + RET + " · <b>bloqueos y balaceras</b> tras la captura de un objetivo prioritario, por titular (Proceso; Latinus) (🔴 narcobloqueo con víctimas civiles) · <b>1 niña muerta</b>, «en medio de fuego cruzado», por titular (ABC Noticias); <b>de 7 años y estadounidense</b>, por titular (Infobae 2026/10/30) · <b>2 heridos</b>: su madre y un rescatista, por titular (Proceso) · <b>personas ajenas muertas por los narcobloqueos</b>: «seis», por titular (Infobae 2026/10/31); «cinco», por titular, citando a la Fiscalía (Expreso 2026/10/31); «siete», por titular (Elefante Blanco 2026/10/30): <code>CIFRA CONTRADICHA — NO ARBITRADA</code> · de ellas, <b>una familia</b> al chocar con un camión incendiado, por titular (ABC Noticias 2026/10/30), y <b>un conductor</b> identificado como sexta víctima, por titular (El Mañana 2026/10/31): muertes en choque, <b>no por agresión directa</b>: no se suman a muertos por agresión · <b>52 vehículos calcinados</b>, por titular (Excélsior, sin fecha en la ruta); <b>72 vehículos retirados</b>, por titular (La Jornada 2026/10/31): miden cosas distintas · bloqueos levantados el 30, " + RES + " · <b>ningún detenido por los bloqueos ni por las muertes</b>, según la Vocería, " + RES + " · ningún abatido ni personal de seguridad muerto publicado · la captura y los bloqueos son ARG-144-015 y ARG-144-008",
  panel="<b>Niña muerta en fuego cruzado</b> y civiles muertos en choques durante los narcobloqueos: 1 muerta por disparo, 2 heridos; total de muertos contradicho (5, 6 o 7)", inst="Vocería de Seguridad de Tamaulipas" + PT + " · Fiscalía de Tamaulipas" + PR, nac="Infobae · Proceso · Latinus · El Financiero · La Jornada · Excélsior", conf="★★★☆☆",
  campo="hora no fijada; total de muertos contradicho; Vocería por titular de un medio sin fecha en la ruta", I=2, N=6, R=4, A=0,
  fechadas=["Proceso (2026/10/29)", "ABC Noticias (2026/10/29)", "Infobae (2026/10/30)", "ABC Noticias (2026/10/30)", "Infobae (2026/10/31)", "La Jornada (2026/10/31)", "El Mañana (2026/10/31)", "Expreso (2026/10/31)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — el aseguramiento de la captura es de ARG-144-015 (ventana de ARGOS 144)",
  desl="Las muertes no figuran en ARGOS 144: ARG-144-008 (bloqueos, «heridos o detenidos: ninguno publicado») y ARG-144-015 (captura) quedan como hechos distintos, en su edición. Identidad del capturado y segundo detenido: actualización de ARG-144-015, no hecho nuevo. Nombres de las víctimas: medios locales, no se reproducen. La sexta víctima pudo morir el 29 o el 30: día no fijado. Infobae republica en varias notas: una fuente por nota con fecha."),
 dict(id="ARG-145-002", estado="MX-ROO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-30", hora="~14:00 (solo por resumen)", mu=3, he=0, cu=0, hk=14,
  ent="Quintana Roo", mun="Benito Juárez, Cancún (fracc. Paseos del Mar, SM 251, calle Isla Mauricio)", dia="30-OCT, SOLO POR RESUMEN",
  fecha_txt="2026-10-30, día solo por resumen (ninguna ruta fechada)",
  title="QUINTANA ROO · CANCÚN — ATAQUE ARMADO EN PASEOS DEL MAR: TRES MUERTOS",
  hecho="Cancún · <code>FRACC. PASEOS DEL MAR, SM 251, CALLE ISLA MAURICIO, POR TITULAR (SIPSE)</code> · viernes 30-OCT, " + DSR + " · ~14:00, " + RES + " · <b>3 muertos</b>, por titular (Sipse; Sin Embargo; Quintana Roo Ahora) (🔴 homicidio múltiple) · «entre las víctimas hay una mujer», por titular (Quintana Roo Hoy) · un tercer cuerpo a ~200 m, " + RES + " · <b>ningún detenido</b>, por titular (Cambio22) · móvil: versiones de medios, no de autoridad: no se integran",
  panel="<b>Ataque armado: 3 muertos</b>", inst=SB, nac="Sin Embargo", conf="★★☆☆☆",
  campo="ninguna ruta fechada; día y hora solo por resumen; cadena regional de republicaciones; sin fuente institucional", I=0, N=1, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Paseos del Mar no figura en las cinco ediciones previas ni en el índice. Triple homicidio en Paseos del Mar de marzo de 2025 (Infobae 2025/03/19): otro hecho. Nueve portales regionales con titulares casi idénticos: una sola fuente regional. PorEsto 2026/10/30 (balance semanal): no fecha el hecho."),
 dict(id="ARG-145-003", estado="MX-MEX", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-30", hora="~22:00 (solo por resumen)", mu=2, he=1, cu=0, hk=22,
  ent="Estado de México", mun="Valle de Chalco Solidaridad (San Miguel Xico 1.ª Secc., calle Poniente 1-A entre Sur 17 y Sur 18)", dia="30-OCT, POR TITULAR («noche del viernes»), SOLO POR RESUMEN",
  fecha_txt="2026-10-30, día solo por resumen (ruta sin fecha)",
  title="ESTADO DE MÉXICO · VALLE DE CHALCO — ATAQUE ARMADO: DOS MUERTOS Y UN HERIDO",
  hecho="Valle de Chalco Solidaridad · <code>SAN MIGUEL XICO 1.ª SECC., CALLE PONIENTE 1-A ENTRE SUR 17 Y SUR 18, SOLO POR RESUMEN</code> · noche del viernes 30-OCT, " + DSR + " · ~22:00, " + RES + " · <b>2 muertos y 1 herido</b>, por titular (Quadratín Edomex) (🔴 homicidio múltiple) · víctimas no identificadas · <b>ningún detenido publicado</b> · " + FU,
  panel="<b>Ataque armado: 2 muertos y 1 herido</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única regional sin fecha en la ruta; día y hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Valle de Chalco en el índice: ARG-123-001 (carretera México-Puebla, 21-sep), ARG-123-REC-003 (tianguis Santa Cruz, 20-sep) y ARG-124-REC-002 (detención): otros hechos. «Detienen a tres por ataque… en Chalco» (Almomento, sin fecha): no se relaciona sin validar."),
 dict(id="ARG-145-004", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-30", hora="~14:15 (solo por resumen)", mu=2, he=0, cu=0, hk=14.25,
  ent="Guanajuato", mun="Pénjamo (carretera Tepuza de Ortiz – Zapote de Cestau)", dia="30-OCT, POR RUTA",
  title="GUANAJUATO · PÉNJAMO — ATAQUE ARMADO EN LA CARRETERA A ZAPOTE DE CESTAU: DOS MUERTOS (UN MUERTO Y UN HERIDO EN OTRA FUENTE)",
  hecho="Pénjamo · <code>CARRETERA TEPUZA DE ORTIZ – ZAPOTE DE CESTAU, POR TITULAR (AM)</code> · viernes 30-OCT, por ruta (AM 2026/10/30; Correo 2026/oct/30) · ~14:15, " + RES + " · <b>2 muertos</b>, por titular (AM): el segundo murió en el hospital, " + RES + " · <b>1 muerto y 1 herido</b>, por titular (Correo): <code>CIFRA CONTRADICHA — NO ARBITRADA</code>; el color sigue al saldo de AM, la versión posterior (🔴 homicidio múltiple) · víctimas de 19 y 38 años, " + RES + " · agresores huyeron, por titular (AM) · <b>ningún detenido publicado</b>",
  panel="<b>Ataque armado en carretera: 2 muertos</b> (1 muerto y 1 herido en otra fuente)", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="saldo contradicho entre las dos fuentes; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["AM (2026/10/30)", "Correo (2026/oct/30)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepuza de Ortiz y Zapote de Cestau no figuran en las cinco ediciones previas ni en el índice. Pénjamo en el índice: ARG-141-001 y otros: otros hechos. Si el segundo herido sobrevive, el hecho baja a 🟡 por fe de erratas."),
 # ======================= AMARILLOS
 dict(id="ARG-145-005", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-10-29", hora="tarde (solo por resumen)", mu=0, he=2, cu=0, hk=16,
  ent="Baja California", mun="Mexicali (col. Fundadores, calle Florencio Monreal)", dia="29-OCT, POR RUTA",
  title="BAJA CALIFORNIA · MEXICALI — HOMBRE ATRINCHERADO DISPARA CONTRA LA FESC: DOS AGENTES HERIDOS, ENTRE ELLOS EL SUBDIRECTOR OPERATIVO; EL AGRESOR, ABATIDO",
  hecho="Mexicali · <code>COL. FUNDADORES, POR TITULAR (EL IMPARCIAL)</code> · jueves 29-OCT, por ruta (Punto Norte; Periodismo Negro 2026/10/29) · " + AP + "; tarde, " + RES + " · hombre atrincherado <b>dispara contra agentes de la FESC</b>, por titular (Punto Norte; Jornada BC) · <b>2 agentes heridos</b>, uno de ellos el <b>subdirector operativo</b>, " + RES + "; «un policía herido», por titular (Poder MX) · <b>agresor abatido</b>, por titular: del lado agresor, no se suma a muertos · quién inició: patrullaje o persona atrincherada, " + RES + ": no determinado (🟡 quién inició no determinado) · la <b>FGE revisa la actuación policial</b>, por titular (El Imparcial 2026/10/30); uso de fuerza letal en investigación, por titular (Zeta) · escopeta del agresor, " + RES,
  panel="<b>Agresión a la FESC</b>: 2 agentes heridos; agresor abatido; la FGE revisa el uso de la fuerza", inst="FGE Baja California" + PT, nac="Milenio · UnoTV · N+", conf="★★★☆☆",
  campo="hora y quién inició solo por resumen; declaración de la fiscal por medios", I=1, N=3, R=5, A=0,
  fechadas=["Punto Norte (2026/10/29)", "Periodismo Negro (2026/10/29)", "En Línea BC (2026/10/30)", "El Imparcial (2026/10/30)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — escopeta del agresor solo por resumen",
  desl="Col. Fundadores y el subdirector no figuran en las cinco ediciones previas ni en el índice. Un resultado lo situó en Tijuana: error del buscador; es Mexicali. El abatido no se suma a muertos: se registra aparte."),
 dict(id="ARG-145-006", estado="MX-NLE", region="Noreste", color="amarillo", impacto="mediano", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=12.5,
  ent="Nuevo León", mun="Vallecillo (camino a La Fortuna)", dia="29-OCT, POR RUTA; HORA NO FIJADA",
  title="NUEVO LEÓN · VALLECILLO — ENFRENTAMIENTO CON FUERZA CIVIL: DOS CIVILES ARMADOS ABATIDOS",
  hecho="Vallecillo · <code>CAMINO A LA FORTUNA, SOLO POR RESUMEN</code> · jueves 29-OCT, por ruta (ABC Noticias 2026/10/29) · " + AP + ": " + RET + " · operativo de <b>Fuerza Civil</b> con <b>2 muertos</b>, por titular (ABC Noticias): <b>civiles armados abatidos</b>, por titular (El Porvenir): del lado agresor, no se suman a muertos · «repelen agresión», por titular (El Porvenir); patrullaje agredido, " + RES + ": quién inició, no acreditado por fragmento (🟡 enfrentamiento; quién inició no determinado) · <b>sin heridos de Fuerza Civil</b>, " + RES + " · 2 armas largas, vehículo y municiones, " + RES + " · <b>ningún detenido publicado</b>",
  panel="<b>Enfrentamiento con Fuerza Civil</b>: 2 civiles armados abatidos", inst="Fuerza Civil" + PR, nac="N+", conf="★★★☆☆",
  campo="hora no fijada; quién inició y armamento solo por resumen", I=1, N=1, R=3, A=0,
  fechadas=["ABC Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm="ARG-145-ARM-004",
  desl="Vallecillo no figura en las cinco ediciones previas ni en el índice. Doctor Coss (12-oct), General Treviño (septiembre), El Carrizo y autopista a Nuevo Laredo: otros hechos. «91 abatidos en 2026»: recuento de un medio, no se integra."),
 dict(id="ARG-145-007", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="tarde-noche; ingreso al hospital ~19:05 (solo por resumen)", mu=1, he=0, cu=0, hk=19,
  ent="Chihuahua", mun="Cuauhtémoc (Centro, calle Segunda entre Hidalgo y Morelos)", dia="30-OCT, POR RUTA",
  title="CHIHUAHUA · CUAUHTÉMOC — BALEAN A UN HOMBRE EN EL CENTRO; MUERE EN EL HOSPITAL",
  hecho="Cuauhtémoc · <code>CENTRO, CALLE SEGUNDA ENTRE HIDALGO Y MORELOS, SOLO POR RESUMEN</code> · viernes 30-OCT, por ruta (El Diario de Chihuahua 2026/oct/30) · tarde-noche, " + RES + " · <b>1 muerto</b>: hombre de 38 años, baleado, por titular (El Diario 2026/oct/30), identificado por un familiar, por titular (El Diario 2026/oct/31) (🟡 homicidio doloso único) · casquillos 9 mm, " + RES + " · <b>ningún detenido publicado</b>",
  panel="<b>Hombre baleado</b>: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/30)", "El Diario de Chihuahua (2026/oct/31)"], estatus="Parcialmente corroborado", arm=None,
  desl="Calle Segunda de Cuauhtémoc no figura en las cinco ediciones previas. «Dos ejecutados en La Ciudadela, Cuauhtémoc» (Tiempo): fecha no fijada, no se integra."),
 dict(id="ARG-145-008", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="~15:00 (solo por resumen)", mu=1, he=0, cu=0, hk=15,
  ent="Baja California", mun="Tijuana (av. De las Aguas, Villas del Sol / Villas del Real)", dia="30-OCT, POR RUTA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS A UNA MUJER EN LA ZONA ESTE",
  hecho="Tijuana · <code>AV. DE LAS AGUAS, FRENTE A UN SITIO DE TAXIS, POR TITULAR (ALFREDO ÁLVAREZ); VILLAS DEL SOL O VILLAS DEL REAL, POR TITULAR: CONTRADICHO</code> · viernes 30-OCT, por ruta (Punto Norte; Periodismo Negro 2026/10/30) · ~15:00, " + RES + " · <b>1 muerta</b>: mujer joven, por titular (Periodismo Negro; Punto Norte) (🟡 homicidio doloso único) · edad entre 25 y 30 años, " + RES + ": no se fija · <b>ningún detenido publicado</b>",
  panel="<b>Mujer asesinada a balazos</b>: 1 muerta", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Punto Norte (2026/10/30)", "Periodismo Negro (2026/10/30)"], estatus="Parcialmente corroborado", arm=None,
  desl="Av. De las Aguas no figura en las cinco ediciones previas ni en el índice. Villas del Real de Culiacán (ARG-144-REC-003): otro hecho, otro estado. El Congresista fecha la nota en 2023: error de la fuente, se descarta."),
 dict(id="ARG-145-009", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="no fijada", mu=1, he=0, cu=0, hk=12,
  ent="Baja California", mun="Tijuana (col. Fortín de las Flores)", dia="30-OCT, POR RUTA; HORA NO FIJADA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS AL GERENTE DE UNA EMPRESA DE TRANSPORTE EN FORTÍN DE LAS FLORES",
  hecho="Tijuana · <code>COL. FORTÍN DE LAS FLORES, POR TITULAR (TV AZTECA BC)</code> · viernes 30-OCT, por ruta (Punto Norte 2026/10/30) · hora no fijada · <b>1 muerto</b>: <b>gerente de la empresa de transporte Altisa</b>, por titular (Punto Norte; TV Azteca BC) (🟡 homicidio doloso único) · la empresa lo declara «ajeno a ella», por titular (Punto Norte) · <b>ningún detenido publicado</b>",
  panel="<b>Gerente de empresa de transporte asesinado</b>: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Punto Norte (2026/10/30)"], estatus="Parcialmente corroborado", arm=None,
  desl="Fortín de las Flores y Altisa no figuran en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-145-010", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-31", hora="mañana (solo por resumen)", mu=1, he=0, cu=0, hk=9,
  ent="Sinaloa", mun="Mazatlán (fracc. Santa Fe, cruce Pasadena–Santa Ana)", dia="31-OCT, POR RUTA; HORA NO FIJADA",
  title="SINALOA · MAZATLÁN — ASESINAN A BALAZOS A UN JOVEN EN EL FRACCIONAMIENTO SANTA FE",
  hecho="Mazatlán · <code>FRACC. SANTA FE, POR TITULAR (LUZ NOTICIAS)</code> · sábado 31-OCT, por ruta (Luz Noticias 2026-10-31) · «mañana de este sábado», " + RES + " · " + FR + " · <b>1 muerto</b>: joven, por titular (Luz Noticias; Azteca Sinaloa); 18 años, por titular (Los Noticieristas) (🟡 homicidio doloso único) · <b>ningún detenido publicado</b>",
  panel="<b>Joven asesinado a balazos</b>: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada frente al cierre; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026/10/31)"], estatus="Parcialmente corroborado", arm=None,
  desl="Fracc. Santa Fe de Mazatlán no figura en las cinco ediciones previas; Santa Fe en el índice es Tlajomulco, Jal. (ARG-137-002): otro hecho. Caso «Rodolfo», 19 años (12-sep, Sinaloahoy): otro hecho."),
 dict(id="ARG-145-011", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="no fijada", mu=0, he=0, cu=1, hk=11,
  ent="Sinaloa", mun="Mazatlán (playa Pato Blanco)", dia="30-OCT, POR <i>SLUG</i>",
  fecha_txt="2026-10-30, por <i>slug</i> (ruta sin fecha)",
  title="SINALOA · MAZATLÁN — HALLAN A UNA MUJER SIN VIDA EN LA PLAYA PATO BLANCO",
  hecho="Mazatlán · <code>PLAYA PATO BLANCO, POR <i>SLUG</i></code> · viernes 30-OCT, por <i>slug</i> («este-viernes-30-de-octubre», Sinaloahoy) · hora no fijada · <b>mujer sin vida</b>, por titular (Sinaloahoy) (🟡 cuerpo hallado) · <b>causa de muerte no informada por autoridad</b>: cuerpo hallado, aparte de los muertos por agresión · " + FU,
  panel="<b>Mujer hallada sin vida</b> en una playa: causa no informada", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; causa de muerte no informada; ruta sin fecha", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Pato Blanco no figura en las cinco ediciones previas ni en el índice."),
 # ======================= VERDES
 dict(id="ARG-145-012", estado="MX-CMX", region="Centro", color="verde", impacto="mediano", fecha="2026-10-30", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Ciudad de México", mun="Iztapalapa (col. Lomas Estrella, calle Capri)", dia="PUB. 30-OCT; DÍA DEL CATEO SOLO POR RESUMEN",
  fecha_txt="publicado el 2026-10-30 — día del cateo solo por resumen",
  title="CIUDAD DE MÉXICO · IZTAPALAPA — CATEO EN LOMAS ESTRELLA: TRES DETENIDOS; ASEGURAN ARMAS LARGAS",
  hecho="Iztapalapa · <code>COL. LOMAS ESTRELLA, CALLE CAPRI, SOLO POR RESUMEN</code> · publicado el viernes 30-OCT, por ruta (La Silla Rota 2026/10/30) · día del cateo, " + RES + ": " + RET + " · <b>cateo con 3 detenidos</b>, por titular (N+; 24 Horas) · <b>armas largas aseguradas</b>, por titular (N+), sin cifra citable (2 largas y 2 cargadores, " + RES + ") · droga: cifras contradichas entre medios, " + RES + " · informó la <b>SSC</b>, " + RES + " · identidad con el inmueble de venta de droga de La Silla Rota, " + RES,
  panel="<b>Cateo: 3 detenidos</b>; armas largas aseguradas, sin cifra citable", inst="SSC Ciudad de México" + PR, nac="Milenio · N+ · 24 Horas · La Silla Rota", conf="★★★☆☆",
  campo="día del cateo y cifras de armas solo por resumen; SSC solo por resumen", I=1, N=4, R=0, A=0,
  fechadas=["La Silla Rota (2026/10/30)"], estatus="Parcialmente corroborado", arm="ARG-145-ARM-001",
  desl="Lomas Estrella no figura en las cinco ediciones previas ni en el índice. Iztapalapa en el índice: ataques del 23-24-oct y otros: otros hechos."),
 dict(id="ARG-145-013", estado="MX-COA", region="Noreste", color="verde", impacto="mediano", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Coahuila", mun="Piedras Negras (col. Real del Norte)", dia="ACCIONES DEL 29-OCT (BOLETÍN FEDERAL); HORA NO FIJADA",
  title="COAHUILA · PIEDRAS NEGRAS — OPERATIVO FEDERAL Y ESTATAL: ASEGURAN METANFETAMINA, COCAÍNA Y UN ARMA LARGA",
  hecho="Piedras Negras · <code>COL. REAL DEL NORTE, SOLO POR RESUMEN</code> · acciones del jueves 29-OCT, por título del boletín federal (republicadores: RED113 2026/10; Tallapolítica) · " + AP + ": " + RET + " · <b>aseguramiento de metanfetamina, cocaína y armamento</b>, por titular (Potosinoticias 2026/10/30) · 38 kg de metanfetamina, 13 kg de cocaína, 1 arma larga y 94 cartuchos, " + RES + " · Ejército, GN, Marina y Fiscalía estatal, " + RES + " · detenidos: no publicados",
  panel="<b>Aseguramiento de droga y armamento</b>, sin cifra citable", inst="Gabinete de Seguridad" + PR, nac=NIN, conf="★★☆☆☆",
  campo="cifras y municipio solo por resumen; republicadores del boletín, una sola fuente", I=1, N=0, R=1, A=0,
  fechadas=["Potosinoticias (2026/10/30)"], estatus="Pendiente de corroboración", arm="ARG-145-ARM-002",
  desl="Piedras Negras en el índice: sentencias antiguas y ARG-105-REC-001; en ARGOS 142 solo como etiqueta de mapa: otros hechos. Republicadores del boletín: no suman fuente independiente."),
 dict(id="ARG-145-014", estado="MX-GRO", region="Sureste", color="verde", impacto="mediano", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Guerrero", mun="Juan R. Escudero", dia="ACCIONES DEL 29-OCT (BOLETÍN FEDERAL); HORA NO FIJADA",
  title="GUERRERO · JUAN R. ESCUDERO — ACCIÓN FEDERAL CON ASEGURAMIENTO DE ARMAS LARGAS, CARGADORES Y CARTUCHOS",
  hecho="Juan R. Escudero · <code>MUNICIPIO, SOLO POR RESUMEN</code> · acciones del jueves 29-OCT, por título del boletín federal (republicadores: RED113 2026/10; Tallapolítica) · " + AP + ": " + RET + " · <b>aseguramiento de armamento</b>: 10 armas largas, 16 cargadores y 338 cartuchos, " + RES + " · corporaciones y detenidos: no fijados · " + FU,
  panel="<b>Aseguramiento de armas largas</b>, sin cifra citable", inst="Gabinete de Seguridad" + PR, nac=NIN, conf="★★☆☆☆",
  campo="cifras, municipio y día de la acción solo por resumen; republicadores del boletín, una sola fuente", I=1, N=0, R=0, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm="ARG-145-ARM-003",
  desl="Juan R. Escudero en el índice: ARG-139-REC-002 (El Terrero, drones, 19-oct): otro hecho. Republicadores del boletín: no suman fuente independiente."),
]

# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-145-REC-001", estado="MX-SIN", region="Noroeste", fecha="2026-10-29", hora="mañana, «mientras desayunaban» (solo por resumen)", orig="ARGOS 144 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (restaurante Los Ranchos, zona Marina Mazatlán)", dia="29-OCT, POR RUTA",
  title="SINALOA · MAZATLÁN — ATAQUE ARMADO EN UN RESTAURANTE: DOS COMENSALES MUERTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 — HORA SOLO POR RESUMEN</code> · Mazatlán · <code>RESTAURANTE LOS RANCHOS, ZONA MARINA MAZATLÁN, POR TITULAR (SINALOAHOY)</code> · jueves 29-OCT, por ruta (El Diario de Chihuahua 2026/oct/29) · mañana, «mientras desayunaban», " + RES + ": anterior probable a la apertura de ARGOS 145 (11:36 del 29); si resulta posterior, es hecho propio de ARGOS 145 · <b>2 muertos</b>, por titular (El Diario de Chihuahua; El Universal: «eran comensales»; El Financiero 2026/10/30) (🔴 homicidio múltiple) · uno murió en el lugar y otro después, " + RES + " · la FGE investiga, por titular (Sinaloahoy): no es declaración · <b>ningún detenido publicado</b>",
  panel="<b>Ataque en un restaurante: 2 comensales muertos</b>", inst=SB, nac="Reforma · El Universal · El Financiero",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=3, R=2, A=0,
  fechadas=["El Diario de Chihuahua (2026/10/29)", "El Financiero (2026/10/30)"],
  desl="Los Ranchos y Marina Mazatlán no figuran en las cinco ediciones previas ni en el índice. El Diario de Chihuahua republica a Reforma: una sola fuente. Versión temprana «un muerto y un herido grave» (Extraoficial): superada por los titulares posteriores."),
 dict(id="ARG-145-REC-002", estado="MX-VER", region="Golfo", fecha="2026-10-29", hora="mañana (solo por resumen)", orig="ARGOS 144 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=1,
  ent="Veracruz", mun="Coatzacoalcos (col. Francisco Villa, calle Mixteca)", dia="29-OCT, POR RUTA",
  title="VERACRUZ · COATZACOALCOS — HALLAN EL CUERPO DECAPITADO DE UN HOMBRE CON UN MENSAJE, DENTRO DE UNA VIVIENDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 — HORA SOLO POR RESUMEN</code> · Coatzacoalcos · <code>COL. FRANCISCO VILLA, CALLE MIXTECA, POR TITULAR (GOLPE POLÍTICO)</code> · jueves 29-OCT, por ruta (La Silla Rota; Golpe Político 2026/10/29) · mañana, " + RES + ": anterior probable a la apertura de ARGOS 145; si resulta posterior, es hecho propio de ARGOS 145 · <b>cuerpo de hombre decapitado</b>, por titular (La Silla Rota; XEU; El Buen Tono), <b>con mensajes</b>, por titular (Gráfico al Día 2026/10/30) (🔴 restos humanos con mensaje) · dentro de una vivienda, por titular (Golpe Político) · «investigan posible relación» con la cabeza hallada frente al Poder Judicial (ARG-144-REC-002), por titular (XEU; La Aldea): <b>vínculo no acreditado</b> · víctima no identificada · <b>ningún detenido publicado</b>",
  panel="<b>Cuerpo decapitado con mensajes</b> dentro de una vivienda", inst=SB, nac="La Silla Rota · Milenio",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=5, A=0,
  fechadas=["La Silla Rota (2026/10/29)", "Golpe Político (2026/10/29)", "La Aldea de la Información (2026/10/30)", "Gráfico al Día (2026/10/30)"],
  desl="Calle Mixteca y col. Francisco Villa de Coatzacoalcos no figuran en las cinco ediciones previas. Cuerpo hallado sin causa de muerte informada por autoridad. Atribución del mensaje a un grupo: una fuente, no se reproduce."),
 dict(id="ARG-145-REC-003", estado="MX-TLA", region="Centro", fecha="2026-10-28", hora="aviso ~15:00, día no fijado (solo por resumen)", orig="ARGOS 144 O ANTERIOR — DÍA DEL HALLAZGO NO FIJADO", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Tlaxcala", mun="Tetlatlahuca (Santa Ana Portales, junto al río Zahuapan; límite con Nativitas)", dia="PUB. 28-OCT, POR RUTA",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL HALLAZGO NO FIJADO",
  title="TLAXCALA · TETLATLAHUCA — HALLAN RESTOS HUMANOS CALCINADOS JUNTO AL RÍO ZAHUAPAN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 O ANTERIOR — DÍA DEL HALLAZGO NO FIJADO</code> · Tetlatlahuca · <code>SANTA ANA PORTALES, CANAL A ~100 M DEL RÍO ZAHUAPAN, SOLO POR RESUMEN; «ZONA LIMÍTROFE DE NATIVITAS», POR TITULAR (LA PRENSA DE TLAXCALA)</code> · publicado el miércoles 28-OCT, por ruta (Intolerancia Diario 2026/10/28) · aviso ~15:00, sin día, " + RES + " · <b>restos humanos calcinados</b>, por titular (Quadratín Tlaxcala; La Prensa de Tlaxcala; ABC Tlax), <b>en reducción esquelética</b>, por titular (Estilo Tlax; Puebla Roja) (🔴 restos humanos) · sexo e identidad no establecidos · <b>número de víctimas: no publicado</b> — <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · la FGJ de Tlaxcala tiene el caso, " + RES,
  panel="<b>Restos humanos calcinados</b> junto al río Zahuapan; número de víctimas no publicado", inst=SB, nac=NIN,
  conf="★★★☆☆", campo="día del hallazgo no fijado; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Intolerancia Diario (2026/10/28)"],
  desl="En ARGOS 144 figuró solo en el archivo de fuentes, como visto «fecha no fijada»; el cartelón de 144 no lo publicó. La Prensa de Tlaxcala lo sitúa junto al río Atoyac: lugar contradicho."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-145-ARM-001", ficha="ARG-145-012", estado="MX-CMX", region="Centro", color="verde", ent="Ciudad de México", mun="Iztapalapa (col. Lomas Estrella)",
  fecha="2026-10-30", fecha_txt="pub. 30-oct; día del cateo solo por resumen", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 3], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="SSC Ciudad de México <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: «armas largas» por titular (N+), sin cifra citable (2 largas y 2 cargadores, solo por resumen); 3 detenidos por titular; ver ARG-145-012",
  fuentes=["La Silla Rota (2026/10/30)", "N+ (sin fecha en la ruta)", "24 Horas (sin fecha en la ruta)"]),
 dict(id="ARG-145-ARM-002", ficha="ARG-145-013", estado="MX-COA", region="Noreste", color="verde", ent="Coahuila", mun="Piedras Negras (col. Real del Norte)",
  fecha="2026-10-29", fecha_txt="acciones del 29-oct; hora no fijada", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], integra=True,
  corp="Ejército, GN, Marina y FGE Coahuila <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: «armamento» por titular, sin cifra citable (1 larga y 94 cartuchos, solo por resumen); detenidos no publicados; ver ARG-145-013",
  fuentes=["Potosinoticias (2026/10/30)", "RED113 (2026/10)", "Tallapolítica (sin fecha en la ruta)"]),
 dict(id="ARG-145-ARM-003", ficha="ARG-145-014", estado="MX-GRO", region="Sureste", color="verde", ent="Guerrero", mun="Juan R. Escudero",
  fecha="2026-10-29", fecha_txt="acciones del 29-oct; hora no fijada", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], integra=True,
  corp="Gabinete de Seguridad <span class=\"muted-note\">(republicadores, solo por resumen)</span>", conf="No confirmado",
  nota="cualitativo: 10 largas, 16 cargadores y 338 cartuchos solo por resumen; fuente única (republicadores); ver ARG-145-014",
  fuentes=["RED113 (2026/10)", "Tallapolítica (sin fecha en la ruta)"]),
 dict(id="ARG-145-ARM-004", ficha="ARG-145-006", estado="MX-NLE", region="Noreste", color="amarillo", ent="Nuevo León", mun="Vallecillo",
  fecha="2026-10-29", fecha_txt="29-oct, por ruta; hora no fijada", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], nd=[0, 1, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="Fuerza Civil <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: aseguramiento tras enfrentamiento; 2 largas solo por resumen; sin detenidos (2 abatidos); ver ARG-145-006",
  fuentes=["ABC Noticias (2026/10/29)", "N+ (sin fecha en la ruta)", "El Porvenir (sin fecha en la ruta)"]),
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
HORAS = 47 + 38 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 3] and ND == [True] * 9 + [False], (TOT, ND)
assert cnt == {"rojo": 4, "amarillo": 7, "verde": 3}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (12, 5, 1, 2, 0, 1), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,29", DENS
assert (NAP, NFR, NRET) == (5, 1, 5), (NAP, NFR, NRET)
assert sorted(e["id"] for e in E) == [f"ARG-145-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-145-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-29" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-10-29", x["id"]

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
head = head.replace("<title>ARGOS 144 — Reporte Nacional de Seguridad — 2026-10-29</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE TAMAULIPAS EL DICTAMEN SOBRE EL ORIGEN DEL DISPARO QUE MATÓ A LA NIÑA Y LA LISTA OFICIAL DE VÍCTIMAS DE LA JORNADA DE BLOQUEOS</b> (ARG-145-001).
      <br><b>2. SOLICITE A LA VOCERÍA DE SEGURIDAD DE TAMAULIPAS EL PROTOCOLO DE RETIRO DE VEHÍCULOS INCENDIADOS EN CARRETERA; VIGILE LA CARRETERA MATAMOROS–REYNOSA Y EL ACCESO AL PUENTE LOS INDIOS</b> (ARG-145-001).
      <br><b>3. SOLICITE A LAS FISCALÍAS DE QUINTANA ROO, DEL ESTADO DE MÉXICO Y DE GUANAJUATO EL SALDO OFICIAL Y LA IDENTIFICACIÓN DE LAS VÍCTIMAS</b> (ARG-145-002, -003 y -004).
      <br><b>4. SOLICITE A LA FISCALÍA DE VERACRUZ EL COTEJO GENÉTICO ENTRE LA CABEZA HALLADA FRENTE AL PODER JUDICIAL Y EL CUERPO DE LA COL. FRANCISCO VILLA</b> (ARG-144-REC-002 y ARG-145-REC-002).
      <br><b>5. SOLICITE A LAS FISCALÍAS DE BAJA CALIFORNIA Y NUEVO LEÓN LOS DICTÁMENES DE USO DE LA FUERZA Y BALÍSTICOS DE MEXICALI Y VALLECILLO</b> (ARG-145-005 y -006).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>29-oct 11:36 → 31-oct 11:14 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
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
    <b>Armamento</b>: ninguna arma integrada al total (todas las cifras, solo por resumen); <b>{DET} detenidos</b> en aseguramiento, por titular (ARG-145-012) · <b>muertos por agresión</b>: no incluyen las muertes en choque contra vehículos de los bloqueos de Matamoros (de 4 a 6, total contradicho: ARG-145-001) ni los 3 agresores abatidos (ARG-145-005 y -006) · <b>cuerpos hallados</b>: {CU} con causa no informada por autoridad · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code>, {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> y 2 rojos con <code>DÍA SOLO POR RESUMEN</code> (ARG-145-002 y -003) · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b> (hora o día no fijados frente a las 11:36 del 29): ARG-145-001, -006, -012, -013 y -014 · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos y {CU_REC} cuerpo. <b>Cálculo propio</b>.
    <br><b>Fe de erratas compacta a ARGOS 144</b>, condicionada: <b>+2 rojos</b> (Sin, Ver: ARG-145-REC-001 y -002) si su hora se fija antes de las 11:36 del 29; si se fija después, son hechos propios de esta edición · condicionada: <b>+1 rojo</b> (Tlax: ARG-145-REC-003) a la edición cuya ventana contenga el día del hallazgo (ARGOS 144 o anterior) · <b>ARG-144-014</b> (Chetumal): hecho del miércoles 28, {RES}, no del 29; sigue en 144 · <b>ARG-144-015</b> (Matamoros): detenido identificado por titular como Axel Alfredo Cárdenas Rodríguez, «El Titán»; segundo detenido y armamento (2 largas y 2 cortas), {RES} · <b>ARG-144-REC-003</b> (Culiacán): 4 localizados según la Fiscalía; «seis» privados por titular (Luz Noticias 2026-10-28; La Razón 2026/10/29): <code>CIFRA CONTRADICHA — NO ARBITRADA</code> · <b>ARG-144-005</b> (Irapuato): «noche», {RES}, frente a ~14:30: hora contradicha; sigue en 144.
    <br><b>Vistos, fuera de totales</b> — <b>de la ventana de ARGOS 144</b> (🟢 o 🟡, no se recuperan): Guadalajara, robo a un banco con bomba molotov (~10:30 del 29, {RES}) · Coahuayana, 3 detenidos con órdenes de aprehensión (boletín federal del 29; ya visto por 144 el 29) · Morelos: Xochitepec, Temixco y Cuernavaca (Acapantzingo) · Tuxtepec («El Semáforo», 28-oct) · <b>sin ruta fechada ni titular con día</b>: Zihuatanejo, chofer de transporte (jue 29, ~15:00, {RES}) · <b>Culiacán, col. Díaz Ordaz, cabeza humana frente a una vivienda</b> (jue 29, {RES}; UnoTV, sin fecha en la ruta: rojo potencial, día no fijado) · Culiacán, Los Girasoles · Ciudad Obregón, Las Haciendas · Cuautitlán, locutor muerto por bala perdida · Puebla, mujer asesinada en su vivienda · Cuernavaca (col. 1.º de Mayo) y Yautepec (noche del 29, solo por compendio).
    <br><b>Seguimiento, fuera del semáforo</b>: <b>ARG-132-002 (Orizaba)</b>: el policía ministerial herido en el cateo del 13-oct murió el viernes 30, por titular (La Silla Rota; Golpe Político; Plumas Libres 2026/10/30); esquela de la FGE, por titular (N+) — el hecho de origen fue 🟡; su reclasificación queda para decisión del destinatario · <b>ARG-144-002 (Indaparapeo)</b>: la FGE atribuye el ataque a una confusión, por titular (Meganoticias; PCM); ningún detenido · <b>ARG-144-001 (Magdalena de Kino)</b>: ningún detenido, {RES} · <b>ARG-134-REC-004 (Almoloya)</b>: FGR vincula a proceso a cuatro por la red de secuestro, {RES} (Infobae 2026/10/28; El Independiente 2026/10/29) · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[i]) for i in ("ARG-145-001", "ARG-145-002", "ARG-145-003", "ARG-145-004"))
co2 = "\n".join(ficha(byid[i]) for i in ("ARG-145-005", "ARG-145-006", "ARG-145-007", "ARG-145-008"))
co2b = "\n".join(ficha(byid[i]) for i in ("ARG-145-009", "ARG-145-010", "ARG-145-011"))
co2c = "\n".join(ficha(byid[i]) for i in ("ARG-145-012", "ARG-145-013", "ARG-145-014"))
co3 = "\n".join(ficha(rbyid[i], True) for i in ("ARG-145-REC-001", "ARG-145-REC-002", "ARG-145-REC-003"))
assert sorted(re.findall(r'id="(ARG-145-0\d\d)"', co1 + co2 + co2b + co2c)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-145-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "Iztapalapa, Piedras Negras, Juan R. Escudero y Vallecillo: cifras solo por resumen"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "Piedras Negras y Juan R. Escudero: cifras solo por resumen"),
 tile(4, "Cargadores", tv(5), "Iztapalapa y Juan R. Escudero: cifras solo por resumen"),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: 3 por titular (Iztapalapa); ninguna cifra de autoridad"),
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
    <div class="map-caption">Aseguramientos cualitativos: Ciudad de México, Coahuila, Guerrero y Nuevo León (este, tras enfrentamiento).</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> — ningún aseguramiento con cifra publicada y día fijado entre el 29-oct 11:36 y el 31-oct 11:14</td></tr>'
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
    <b>Lectura regional</b>: ninguna región con arma integrada al total; detenidos en aseguramiento: Centro 3. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: los cuatro de la tabla · Mexicali (ARG-145-005): escopeta del agresor, {RES}, sin fila.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>boletín federal de acciones del 28-oct</b> (ventana de ARGOS 144; solo por republicadores, misma fuente; Milenio, RED113, Certeza Diario): Manuel Ojinaga, Chih. (2 detenidos, 7 cartuchos), Acatic, Jal. (5 vehículos blindados), Ahome y Culiacán, Sin. (precursores y laboratorios), Tuxtepec, Oax. (2 detenidos; armas y granadas sin cifra), todo {RES} · <b>boletín del 29-oct</b>: Jalisco, cateo con un vehículo con blindaje artesanal y 10 cartuchos (municipio no fijado), {RES} · <b>Concordia, Sin., La Guásima</b>: 5 largas, 32 cargadores y 1,138 cartuchos, {RES} («cinco armas largas y más de mil cartuchos», por titular, Meganoticias); día no fijado (boletín Ahome-Concordia): <code>FECHA NO FIJADA — NO SE INTEGRA</code>; no es Zavala (ARG-141-REC-005) · <b>Acaponeta, Nay.</b> (agregado estatal; 115 cartuchos, 4 cargadores, {RES}; día no fijado) · <b>Matamoros</b> (2 largas y 2 cortas, {RES}): de ARG-144-015, ventana de ARGOS 144 · <b>Xochitlán de las Flores, Tula, Hgo.</b> (PGJEH; 1 corta y 1 larga, {RES}; La Silla Rota 2026/10/28): ventana de ARGOS 144, no de 143 — <b>sin fe de erratas a ARGOS 143</b>.
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
      <tr><td><b>Baja California</b><br>Tecate</td><td>Ataque a la Guardia Nacional (octubre de 2024); portación de armas de uso exclusivo y asociación delictuosa; procedimiento abreviado, {RES}; <b>4 sentenciados</b>, por titular · <b>nuevo en ARGOS 145</b></td><td><b>hasta 16 años</b>, por titular (El Imparcial; Diario de Tabasco; Tijuana Última Hora 2026/10/30); penas individuales, {RES}</td><td>FGR <span class="muted-note">(por titular de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · comunicado no localizado en <code>fgr.org.mx</code>; nombres discrepantes entre medios: no se reproducen; firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Baja California</b><br>Mexicali</td><td>Homicidio; <b>1 sentenciada</b>, por titular · <b>nuevo en ARGOS 145</b></td><td><b>45 años</b>, por titular (El Imparcial 2026/10/30)</td><td>FGE Baja California <span class="muted-note">(por titular)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · fuente única; día del fallo no fijado; <code>fgebc.gob.mx</code> no consultado</td><td>No confirmado</td></tr>
      <tr><td><b>Jalisco</b><br>Tlajomulco y Tlaquepaque</td><td>Feminicidio; <b>2 sentenciados</b>, por título del boletín · <b>nuevo en ARGOS 145</b></td><td>No publicada en el título</td><td>FGE Jalisco <span class="muted-note">(portada del dominio; fecha 29-oct, solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · boletín sin ruta fechada; sin pena ni campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Oaxaca</b><br>sin municipio publicado</td><td>Violencia familiar contra dos adultos mayores; <b>3 sentenciados</b>, {RES} · <b>nuevo en ARGOS 145</b></td><td>«más de 28 años» en suma, {RES}</td><td>FGE Oaxaca <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin URL ni ruta; penas individuales no publicadas</td><td>No confirmado</td></tr>
      <tr><td><b>Tabasco</b><br>Tenosique</td><td>Armas y granadas; <b>1 sentenciado</b>; procedimiento abreviado, {RES} · <b>candidato de ARGOS 144</b></td><td>7 años, 9 meses y 10 días, {RES}</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · fuente única sin fecha (Ahora Tabasco); comunicado no localizado</td><td>No confirmado</td></tr>
      <tr><td><b>Nuevo León</b><br>Doctor Arroyo · sin municipio</td><td>Homicidio simple (15 años) y revocación de absolución por abuso (40 años) · <b>candidatos de ARGOS 144, sin cambio</b></td><td><b>15</b> y <b>40 años</b>, por titular (MVS 2026/10/28)</td><td>FGJE Nuevo León · tribunal de alzada</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>fiscalianl.gob.mx</code> sin el caso</td><td>No confirmado</td></tr>
      <tr><td><b>Puebla</b><br>Huejotzingo</td><td>Feminicidio · <b>candidato de ARGOS 144, sin cambio</b></td><td><b>55 años</b>, por titular (Heraldo de Puebla; Retodiario 2026/10/29)</td><td>FGE Puebla <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · el boletín del dominio con «55 años» es de otro caso (julio de 2025): señuelo por cifra, descartado</td><td>Bajo</td></tr>
      <tr><td><b>Estado de México</b><br>Ecatepec</td><td>Homicidio y tentativa · <b>candidato de ARGOS 144, sin cambio</b></td><td><b>68 años</b>, por titular (Línea por Línea 2026/10/28)</td><td>FGJEM <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>fgjem.edomex.gob.mx</code> solo devolvió edictos</td><td>No confirmado</td></tr>
      <tr><td><b>Zacatecas</b><br>Fresnillo</td><td>Juan Manuel «N» · <b>candidato de ARGOS 143, sin cambio</b></td><td><b>68 años</b>, por titular (ECOdiario)</td><td>FGJ Zacatecas <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>fiscaliazacatecas.gob.mx</code> sin el caso</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Triple feminicidio; fallo condenatorio del 9-oct · <b>candidato de ARGOS 140 a 144</b></td><td><b>Sin pena</b>: la audiencia continúa el 5-nov, {RES}</td><td>Tribunal de Enjuiciamiento <span class="muted-note">(por medios)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · no consultado en esta edición</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Ramos Arizpe</td><td>Transporte de metanfetamina · <b>candidato de ARGOS 141 a 144</b></td><td>«más de 7 años», por titular (El Siglo de Torreón)</td><td>FGR</td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · sin resultado nuevo</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGE Oaxaca, boletín 2,930 (28-oct, {RES}; 50 años por homicidio calificado y tentativa, Sierra de Flores Magón): ventana de ARGOS 144 · FGE Colima, boletín 4950 (22-oct; «más de 46 años») · FGE Nayarit (8-oct; 40 años) · FGE Quintana Roo, comunicado 393/2026 (18-oct; 140 años) · FGE Yucatán (1-oct) · FGJ Tamaulipas FGJE-370-2026 (~6-oct) · FGE Jalisco, comunicado 1939 (19-oct). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida: <code>fgr.org.mx</code> devolvió listados históricos, sin comunicado de la ventana: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>26 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BCS, Son, Chih, Sin, Dgo · NL, Zac, Tamps · Jal, Col, Nay, Ags, Gto, Mich · CDMX, Edomex, Mor, Pue, Tlax · Ver, Tab · Chis, Oax, Gro, Yuc, QRoo · <b>de ellas, 3 solo devolvieron páginas normativas, edictos o convocatorias</b>: Sin, Edomex, Son · <b>las 14 <code>NO REVISADA</code> de ARGOS 144, revisadas</b> (prioridad sobre el ciclo)</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada (Jalisco: título del 29-oct solo por resumen)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>26</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>1</b>: Coah (<code>fge.coahuila.gob.mx</code>) · <b>dominio de la fiscalía no confirmado</b>: <b>1</b>, Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>4</b>: BC, SLP, Hgo, Qro</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 31-oct 08:30: código <code>000</code> (proxy: conexión rechazada)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en las 10 que ARGOS 144 dejó solo con consulta amplia —BCS · NL, Zac, Coah · <b>Hgo, Qro</b> (fin de dos ediciones seguidas) · Oax, Camp, Yuc— y QRoo por hechos, sin consulta de «bloqueos / instalaciones» · Tamps, Ver, Tab, Edomex, CDMX, Mor, Pue, Tlax, Gto, BC, Sin, Chih con consulta por hechos · SLP, Dgo, Jal, Col, Nay, Ags, Chis, Gro, Mich, Son: <b>solo consulta regional amplia</b> · <b>armamento: 8 de 32 por dominio oficial</b> —BCS, Dgo · Tamps, Zac · Mich · CDMX, Pue · Ver—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · dominio sin páginas: Tab, Coah · <code>NO REVISADA</code> (22): BC, Son, Chih, Sin · NL, SLP · Jal, Col, Nay, Ags, Gto · Edomex, Mor, Tlax, Hgo, Qro · Chis, Oax, Gro, Camp, Yuc, QRoo · <b>de las 13 <code>NO REVISADA</code> de ARGOS 144, revisadas 5</b> (BCS, Dgo, Zac, CDMX, Pue)</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 28-oct</b>: publicadas por republicadores (Milenio, RED113, Certeza Diario): ventana de ARGOS 144 (que lo declaró <code>SIN RESULTADO INDEXADO EN VENTANA</code> al cierre) · <b>acciones del 29-oct</b>: por republicadores (RED113, Tallapolítica): misma fuente, sin indexar en <code>gob.mx</code> · <b>acciones del 30-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Ciclo C</b> (Occidente + Sureste, judicial primero)</td><td>Aportó tres candidatos nuevos —Jalisco (dos feminicidas, título del 29-oct), Oaxaca (violencia familiar, 29-oct) y el boletín 2,930 de Oaxaca (28-oct)—; ninguno integrable</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 31-OCT 08:30: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Cuatro rojos propios en {len(ENT_ROJO)} entidades</b> (cálculo propio): un narcobloqueo con una niña muerta por disparo y civiles muertos en choques (Tamps) y tres homicidios múltiples (QRoo, Edomex, Gto), dos con día solo por resumen: <b>riesgo nacional sostenido</b>; el alza frente a ARGOS 144 no se acredita.
      <br><b>2.</b> <b>Violencia operativa</b>: siete amarillos —cuatro homicidios dolosos únicos, dos confrontaciones con corporaciones estatales con tres agresores abatidos y un cuerpo hallado— en cuatro entidades (cálculo propio).
      <br><b>3.</b> <b>Noroeste</b>: seis de los catorce hechos propios (BC 3, Sin 2, Chih 1) y una recuperación roja en Sinaloa (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: tres verdes, ninguno con cifra de armamento citable; ninguna sentencia integrable (cálculo propio; totales, en el panorama).
      <br><b>5.</b> <code>CINCO DE CATORCE HECHOS CON CLÁUSULA DE RETIRO Y TRES ROJOS RECUPERADOS DE ARGOS 144 O ANTERIORES; VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 144 SIN NORMALIZAR POR HORA. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. MATAMOROS: LA CAPTURA DE UN OBJETIVO PRIORITARIO FUE SEGUIDA EL MISMO DÍA DE BLOQUEOS CON VEHÍCULOS INCENDIADOS QUE MATARON A MÁS CIVILES POR CHOQUE QUE POR DISPARO</b> (cálculo propio: 1 por disparo; de 4 a 6 en choques, total contradicho): ARG-144-015 (captura), ARG-144-008 (bloqueos) y ARG-145-001 (víctimas); la secuencia, por titulares; la autoría de los bloqueos, no acreditada. Línea: <b>solicitar a la Vocería de Seguridad y a la Defensa el protocolo de cierre carretero y retiro de vehículos incendiados ante capturas en la frontera tamaulipeca</b>.
      <br><b>2. COATZACOALCOS: DOS HALLAZGOS DE RESTOS HUMANOS CON MENSAJE EN UNAS 30 HORAS</b> (cálculo propio, 28 y 29-oct; desarrolla la Conclusión 3 de ARGOS 144): ARG-144-REC-002 (cabeza frente al Poder Judicial de la Federación) y ARG-145-REC-002 (cuerpo decapitado en una vivienda de la col. Francisco Villa); vínculo no acreditado. Línea: <b>solicitar a la Fiscalía de Veracruz el cotejo genético y el texto íntegro de ambos mensajes</b>.
      <br><b>3. MAZATLÁN: TRES HECHOS CON VÍCTIMAS EN 48 HORAS, UNO CONTRA COMENSALES DE UN RESTAURANTE</b> (cálculo propio, 29 al 31-oct): ARG-145-REC-001 (2 muertos), ARG-145-010 (1 muerto) y ARG-145-011 (cuerpo, causa no informada); vínculo no acreditado. Línea: <b>solicitar a la Fiscalía de Sinaloa el cotejo balístico de los dos ataques y vigilar la zona Marina y el sur del puerto</b>.
      <br><b>4. TRES AGRESORES ABATIDOS EN DOS CONFRONTACIONES CON CORPORACIONES ESTATALES EL MISMO DÍA, EN DOS ESTADOS</b> (cálculo propio, 29-oct): ARG-145-005 (Mexicali, FESC; la Fiscalía revisa el uso de la fuerza letal) y ARG-145-006 (Vallecillo, Fuerza Civil); quién inició, no acreditado en ninguno; vínculo no acreditado. Línea: <b>solicitar a las fiscalías de Baja California y Nuevo León los dictámenes balísticos y de uso de la fuerza</b>.
      <br><b>5. TECATE: CONDENA, POR TITULAR, DOS AÑOS DESPUÉS DE UN ATAQUE A LA GUARDIA NACIONAL</b> (cálculo propio, octubre de 2024 a octubre de 2026): cuatro sentenciados, hasta 16 años, por titular, por portación de armas de uso exclusivo y asociación delictuosa; <code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRADO</code>. Línea: <b>solicitar a la FGR el comunicado con la causa penal, las penas individuales y la firmeza</b>.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: NARCOBLOQUEO CON VÍCTIMAS CIVILES Y HOMICIDIOS MÚLTIPLES", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA: CONFRONTACIONES CON CORPORACIONES ESTATALES Y HOMICIDIOS EN CHIHUAHUA Y BAJA CALIFORNIA", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA: TIJUANA Y MAZATLÁN", co2b)
 + page("CRIMEN ORGANIZADO (IV) — ACCIONES INSTITUCIONALES", co2c)
 + page("CRIMEN ORGANIZADO (V) — ALTO IMPACTO DE VENTANAS ANTERIORES: ARGOS 144 O ANTERIORES", co3)
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
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 144 con WINDOW_DAYS = 2"
script = script.replace("WINDOW_DAYS = 2;", "WINDOW_DAYS = 3;")
assert "WINDOW_DAYS = 3;" in script and "WINDOW_DAYS = 2;" not in script  # la ventana toca tres fechas de calendario (29, 30 y 31-oct)
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
