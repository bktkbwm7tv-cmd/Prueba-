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
 # ======================= ROJO
 dict(id="ARG-145-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-29", hora="~18:00-18:20 (solo por resumen)", mu=0, he=0, cu=1, hk=18,
  ent="Sinaloa", mun="Culiacán (col. Díaz Ordaz)", dia="29-OCT, POR RUTA",
  title="SINALOA · CULIACÁN — ABANDONAN UNA HIELERA CON UNA CABEZA HUMANA EN UNA VIVIENDA DE LA COLONIA DÍAZ ORDAZ",
  hecho="Culiacán · <code>COL. DÍAZ ORDAZ, POR TITULAR (RÍODOCE); CALLE CONSTITUYENTE ENRIQUE COLUNGA, SOLO POR RESUMEN</code> · jueves 29-OCT, por ruta (Ríodoce 2026/10/29) · " + AP + "; ~18:00 o 18:20, " + RES + " · <b>hielera con una cabeza humana</b> en una vivienda, por titular (Ríodoce); «frente a una vivienda», por titular (UnoTV) (🔴 restos humanos) · <b>con mensaje</b>, por titular (Sinaloahoy) · «segundo caso en 48 horas», por titular (UnoTV) · la FGE investiga, " + RES + ": no es declaración · víctima no identificada · <b>ningún detenido publicado</b>",
  panel="<b>Cabeza humana en una hielera, con mensaje</b>, en una vivienda", inst=SB, nac="UnoTV", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=6, A=0,
  fechadas=["Ríodoce (2026/10/29)"], estatus="Parcialmente corroborado", arm=None,
  desl="Díaz Ordaz en ARGOS 144: ataque a una vivienda (27-oct, tarde), visto de la ventana de ARGOS 143: otro hecho. El «primer caso» de UnoTV es ARG-144-REC-004 (Mazatlán, 27-oct): otro hecho, otra ciudad. Cuerpo hallado sin causa de muerte informada por autoridad."),
 # ======================= AMARILLOS
 dict(id="ARG-145-002", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-10-30", hora="~14:15 (solo por resumen)", mu=1, he=0, cu=0, hk=14.25,
  ent="Guanajuato", mun="Pénjamo (carretera Tepuza de Ortiz – Zapote de Cestau)", dia="30-OCT, POR RUTA",
  title="GUANAJUATO · PÉNJAMO — ATAQUE ARMADO EN LA CARRETERA A ZAPOTE DE CESTAU: UN MUERTO; LA SEGUNDA VÍCTIMA, MUERTA O HERIDA SEGÚN LA FUENTE",
  hecho="Pénjamo · <code>CARRETERA TEPUZA DE ORTIZ – ZAPOTE DE CESTAU, POR TITULAR (AM)</code> · viernes 30-OCT, por ruta (AM 2026/10/30; Correo 2026/oct/30) · ~14:15, " + RES + " · <b>1 muerto</b>, por titular de ambas fuentes · la <b>segunda víctima</b>: muerta, por titular (AM: «dos hombres muertos»), o herida, por titular (Correo: «un muerto y un herido»): <code>CIFRA CONTRADICHA — NO SE INTEGRA AL TOTAL HASTA VALIDACIÓN</code> (🟡) · víctimas de 19 y 38 años, " + RES + " · agresores huyeron, por titular (AM) · <b>ningún detenido publicado</b>",
  panel="<b>Ataque armado en carretera: 1 muerto</b>; segunda víctima muerta o herida (contradicho)", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="saldo contradicho entre las dos fuentes; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["AM (2026/10/30)", "Correo (2026/oct/30)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepuza de Ortiz y Zapote de Cestau no figuran en las cinco ediciones previas ni en el índice. Pénjamo en el índice: ARG-141-001 (col. Lázaro Cárdenas) y otros: otros hechos."),
 dict(id="ARG-145-003", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-10-29", hora="tarde (solo por resumen)", mu=0, he=1, cu=0, hk=16,
  ent="Baja California", mun="Mexicali (col. Fundadores)", dia="29-OCT, POR RUTA",
  title="BAJA CALIFORNIA · MEXICALI — HOMBRE ATRINCHERADO DISPARA CONTRA LA FESC: HIEREN AL SUBDIRECTOR OPERATIVO; EL AGRESOR, ABATIDO",
  hecho="Mexicali · <code>COL. FUNDADORES, POR TITULAR (EL IMPARCIAL)</code> · jueves 29-OCT, por ruta (Punto Norte; Periodismo Negro 2026/10/29) · " + AP + "; tarde, " + RES + " · hombre atrincherado <b>dispara contra agentes de la FESC</b>, por titular (Jornada BC) · <b>1 herido</b>: el <b>subdirector operativo de la FESC</b>, por titular (Alfredo Álvarez); un segundo agente herido, " + RES + ": no se suma · <b>agresor abatido</b>, por titular (Jornada BC): del lado agresor, no se suma a muertos · quién inició: patrullaje o persona atrincherada, " + RES + ": no determinado (🟡) · la <b>FGE revisa la actuación policial</b>, por titular (El Imparcial 2026/10/30); el uso de fuerza letal, en investigación, por titular (Zeta) · escopeta del agresor, " + RES,
  panel="<b>Agresión a la FESC</b>: 1 agente herido (el subdirector); agresor abatido; la FGE revisa el uso de la fuerza", inst="FGE Baja California" + PT, nac="Milenio · UnoTV · N+", conf="★★★☆☆",
  campo="hora y quién inició solo por resumen; segundo herido solo por resumen", I=1, N=3, R=5, A=0,
  fechadas=["Punto Norte (2026/10/29)", "Periodismo Negro (2026/10/29)", "En Línea BC (2026/10/30)", "El Imparcial (2026/10/30)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — escopeta del agresor solo por resumen",
  desl="Col. Fundadores no figura en las cinco ediciones previas ni en el índice. El abatido no se suma a muertos: se registra aparte."),
 dict(id="ARG-145-004", estado="MX-NLE", region="Noreste", color="amarillo", impacto="mediano", fecha="2026-10-29", hora="noche (solo por resumen)", mu=0, he=0, cu=0, hk=21,
  ent="Nuevo León", mun="Vallecillo (camino a La Fortuna)", dia="29-OCT, POR RUTA",
  title="NUEVO LEÓN · VALLECILLO — FUERZA CIVIL ABATE A DOS EN UN OPERATIVO",
  hecho="Vallecillo · <code>CAMINO A LA FORTUNA, SOLO POR RESUMEN</code> · jueves 29-OCT, por ruta (ABC Noticias 2026/10/29) · " + AP + "; noche, " + RES + " · <b>Fuerza Civil abate a dos</b>, por titular (La Verdad 2026/10; N+: «Confirma Fuerza Civil… Operativo Muralla»); «operativo… deja 2 muertos», por titular (ABC Noticias): del lado agresor, no se suman a muertos · agresión a balazos durante un recorrido de vigilancia, " + RES + " (La Verdad): quién inició, no acreditado por fragmento (🟡) · <b>sin heridos de Fuerza Civil</b>, " + RES + " · 2 armas largas, vehículo y municiones, " + RES + " · <b>ningún detenido publicado</b> · vínculo del operativo con la violencia de Tamaulipas: un medio, no acreditado",
  panel="<b>Operativo de Fuerza Civil</b>: 2 abatidos", inst="Fuerza Civil" + PT, nac="N+", conf="★★★☆☆",
  campo="hora, quién inició y armamento solo por resumen", I=1, N=1, R=3, A=0,
  fechadas=["ABC Noticias (2026/10/29)"], estatus="Parcialmente corroborado", arm="ARG-145-ARM-003",
  desl="Vallecillo no figura en las cinco ediciones previas ni en el índice. Doctor Coss (12-oct), General Treviño (septiembre), El Carrizo y autopista a Nuevo Laredo: otros hechos. «91 abatidos en 2026»: recuento de un medio, no se integra."),
 dict(id="ARG-145-005", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="tarde-noche; ingreso al hospital ~19:05 (solo por resumen)", mu=1, he=0, cu=0, hk=19,
  ent="Chihuahua", mun="Cuauhtémoc (Centro, calle Segunda entre Hidalgo y Morelos)", dia="30-OCT, POR RUTA",
  title="CHIHUAHUA · CUAUHTÉMOC — BALEAN A UN HOMBRE EN EL CENTRO; MUERE EN EL HOSPITAL",
  hecho="Cuauhtémoc · <code>CENTRO, CALLE SEGUNDA ENTRE HIDALGO Y MORELOS, SOLO POR RESUMEN</code> · viernes 30-OCT, por ruta (El Diario de Chihuahua 2026/oct/30) · tarde-noche, " + RES + " · <b>1 muerto</b>: hombre de 38 años, baleado, por titular (El Diario 2026/oct/30), identificado por un familiar, por titular (El Diario 2026/oct/31) (🟡 homicidio doloso único) · casquillos 9 mm, " + RES + " · <b>ningún detenido publicado</b>",
  panel="<b>Hombre baleado</b>: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/30)", "El Diario de Chihuahua (2026/oct/31)"], estatus="Parcialmente corroborado", arm=None,
  desl="Calle Segunda de Cuauhtémoc no figura en las cinco ediciones previas. «Dos ejecutados en La Ciudadela, Cuauhtémoc» (Tiempo): fecha no fijada, no se integra."),
 dict(id="ARG-145-006", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="~15:00 (solo por resumen)", mu=1, he=0, cu=0, hk=15,
  ent="Baja California", mun="Tijuana (av. De las Aguas, Villas del Sol / Villas del Real)", dia="30-OCT, POR RUTA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS A UNA MUJER EN LA ZONA ESTE",
  hecho="Tijuana · <code>AV. DE LAS AGUAS, FRENTE A UN SITIO DE TAXIS, POR TITULAR (ALFREDO ÁLVAREZ); VILLAS DEL SOL O VILLAS DEL REAL, POR TITULAR: CONTRADICHO</code> · viernes 30-OCT, por ruta (Punto Norte; Periodismo Negro 2026/10/30) · ~15:00, " + RES + " · <b>1 muerta</b>: mujer joven, por titular (Periodismo Negro; Punto Norte) (🟡 homicidio doloso único) · edad entre 25 y 30 años, " + RES + ": no se fija · <b>ningún detenido publicado</b>",
  panel="<b>Mujer asesinada a balazos</b>: 1 muerta", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Punto Norte (2026/10/30)", "Periodismo Negro (2026/10/30)"], estatus="Parcialmente corroborado", arm=None,
  desl="Av. De las Aguas no figura en las cinco ediciones previas ni en el índice. Villas del Real de Culiacán (ARG-144-REC-003): otro hecho, otro estado."),
 dict(id="ARG-145-007", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="no fijada", mu=1, he=0, cu=0, hk=12,
  ent="Baja California", mun="Tijuana (col. Fortín de las Flores)", dia="30-OCT, POR RUTA; HORA NO FIJADA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS AL GERENTE DE UNA EMPRESA DE TRANSPORTE EN FORTÍN DE LAS FLORES",
  hecho="Tijuana · <code>COL. FORTÍN DE LAS FLORES, POR TITULAR (TV AZTECA BC)</code> · viernes 30-OCT, por ruta (Punto Norte 2026/10/30) · hora no fijada · <b>1 muerto</b>: <b>gerente de la empresa de transporte Altisa</b>, por titular (Punto Norte; TV Azteca BC) (🟡 homicidio doloso único) · la empresa lo declara «ajeno a ella», por titular (Punto Norte) · <b>ningún detenido publicado</b>",
  panel="<b>Gerente de empresa de transporte asesinado</b>: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Punto Norte (2026/10/30)"], estatus="Parcialmente corroborado", arm=None,
  desl="Fortín de las Flores y Altisa no figuran en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-145-008", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-31", hora="mañana (solo por resumen)", mu=1, he=0, cu=0, hk=9,
  ent="Sinaloa", mun="Mazatlán (fracc. Santa Fe, cruce Pasadena–Santa Ana)", dia="31-OCT, POR RUTA; HORA NO FIJADA",
  title="SINALOA · MAZATLÁN — ASESINAN A BALAZOS A UN JOVEN EN EL FRACCIONAMIENTO SANTA FE",
  hecho="Mazatlán · <code>FRACC. SANTA FE, POR TITULAR (LUZ NOTICIAS)</code> · sábado 31-OCT, por ruta (Luz Noticias 2026-10-31) · «mañana de este sábado», " + RES + " · " + FR + " · <b>1 muerto</b>: joven, por titular (Luz Noticias; Azteca Sinaloa); 18 años, por titular (Los Noticieristas) (🟡 homicidio doloso único) · <b>ningún detenido publicado</b>",
  panel="<b>Joven asesinado a balazos</b>: 1 muerto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada frente al cierre; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026/10/31)"], estatus="Parcialmente corroborado", arm=None,
  desl="Fracc. Santa Fe de Mazatlán no figura en las cinco ediciones previas; Santa Fe en el índice es Tlajomulco, Jal. (ARG-137-002): otro hecho. Caso «Rodolfo», 19 años (12-sep, Sinaloahoy): otro hecho."),
 dict(id="ARG-145-009", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-30", hora="no fijada", mu=0, he=0, cu=1, hk=11,
  ent="Sinaloa", mun="Mazatlán (playa Pato Blanco)", dia="30-OCT, POR <i>SLUG</i>",
  fecha_txt="2026-10-30, por <i>slug</i> (ruta sin fecha)",
  title="SINALOA · MAZATLÁN — HALLAN A UNA MUJER SIN VIDA EN LA PLAYA PATO BLANCO",
  hecho="Mazatlán · <code>PLAYA PATO BLANCO, POR <i>SLUG</i></code> · viernes 30-OCT, por <i>slug</i> («este-viernes-30-de-octubre», Sinaloahoy) · hora no fijada · <b>mujer sin vida</b>, por titular (Sinaloahoy) (🟡 cuerpo hallado) · <b>causa de muerte no informada por autoridad</b>: cuerpo hallado, aparte de los muertos por agresión · " + FU,
  panel="<b>Mujer hallada sin vida</b> en una playa: causa no informada", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; causa de muerte no informada; ruta sin fecha", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Pato Blanco no figura en las cinco ediciones previas ni en el índice."),
 # ======================= VERDES,
 dict(id="ARG-145-010", estado="MX-CMX", region="Centro", color="verde", impacto="mediano", fecha="2026-10-30", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Ciudad de México", mun="Iztapalapa (col. Lomas Estrella, calle Capri)", dia="PUB. 30-OCT; DÍA DEL CATEO SOLO POR RESUMEN",
  fecha_txt="publicado el 2026-10-30 — día del cateo solo por resumen",
  title="CIUDAD DE MÉXICO · IZTAPALAPA — CATEO EN LOMAS ESTRELLA: ASEGURAN DROGA Y ARMAS; DETENIDOS",
  hecho="Iztapalapa · <code>COL. LOMAS ESTRELLA, CALLE CAPRI, SOLO POR RESUMEN</code> · publicado el viernes 30-OCT, por ruta (La Silla Rota 2026/10/30) · día del cateo, " + RES + ": " + RET + " · <b>cateo con 3 detenidos</b>, por titular sin fecha en la ruta (Milenio; NX Noticias): <code>POSIBLE CASO HOMÓNIMO</code> de otros cateos en Iztapalapa con tres detenidos; ninguna cifra de autoridad · <b>armas aseguradas</b>, por titular (Milenio), sin cifra citable (2 largas y 2 cargadores, " + RES + ") · droga: cifras contradichas entre medios, " + RES + " · informó la <b>SSC</b>, " + RES + " · identidad con el inmueble de venta de droga de La Silla Rota, " + RES,
  panel="<b>Cateo</b>: droga y armas aseguradas; 3 detenidos por titulares sin fecha", inst="SSC Ciudad de México" + PR, nac="Milenio · N+ · 24 Horas · La Silla Rota", conf="★★★☆☆",
  campo="día del cateo y cifras de armas solo por resumen; detenidos por titulares sin fecha; SSC solo por resumen", I=1, N=4, R=0, A=0,
  fechadas=["La Silla Rota (2026/10/30)"], estatus="Parcialmente corroborado", arm="ARG-145-ARM-001",
  desl="Lomas Estrella no figura en las cinco ediciones previas ni en el índice. Iztapalapa en el índice: ataques del 23-24-oct y otros: otros hechos."),
 dict(id="ARG-145-011", estado="MX-COA", region="Noreste", color="verde", impacto="mediano", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Coahuila", mun="Piedras Negras (col. Real del Norte)", dia="ACCIONES DEL 29-OCT (BOLETÍN FEDERAL); HORA NO FIJADA",
  title="COAHUILA · PIEDRAS NEGRAS — ASEGURAN METANFETAMINA, COCAÍNA Y ARMAMENTO EN UN OPERATIVO",
  hecho="Piedras Negras · <code>COL. REAL DEL NORTE, SOLO POR RESUMEN</code> · acciones del jueves 29-OCT, por título del boletín federal (republicadores: RED113 2026/10; Tallapolítica) · " + AP + ": " + RET + " · <b>aseguramiento de metanfetamina, cocaína y armamento</b>, por titular (Potosinoticias 2026/10/30) · 38 kg de metanfetamina, 13 kg de cocaína, 1 arma larga y 94 cartuchos, " + RES + " · Ejército, GN, Marina y Fiscalía estatal, " + RES + " · detenidos: no publicados",
  panel="<b>Aseguramiento de droga y armamento</b>, sin cifra citable", inst="Gabinete de Seguridad <span class=\"muted-note\">(boletín por republicadores, solo por resumen)</span>", nac=NIN, conf="★★☆☆☆",
  campo="cifras y municipio solo por resumen; republicadores del boletín, una sola fuente", I=0, N=0, R=2, A=0,
  fechadas=["Potosinoticias (2026/10/30)"], estatus="Pendiente de corroboración", arm="ARG-145-ARM-002",
  desl="Piedras Negras en el índice: sentencias antiguas y ARG-105-REC-001: otros hechos. Visto de ARGOS 142 (Puente Internacional II: 1 arma, 3 cargadores, 39 cartuchos, 1 detenida): otro lugar, otra corporación, otras cifras. Republicadores del boletín: no suman fuente independiente."),
 dict(id="ARG-145-012", estado="MX-GRO", region="Sureste", color="verde", impacto="mediano", fecha="2026-10-29", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Guerrero", mun="Juan R. Escudero", dia="ACCIONES DEL 29-OCT (BOLETÍN FEDERAL); HORA NO FIJADA",
  title="GUERRERO · JUAN R. ESCUDERO — ACCIÓN FEDERAL REGISTRADA EN EL BOLETÍN DEL GABINETE DE SEGURIDAD DEL 29-OCT",
  hecho="Juan R. Escudero · <code>MUNICIPIO, SOLO POR RESUMEN</code> · acciones del jueves 29-OCT, por título del boletín federal (republicadores: RED113 2026/10; Tallapolítica) · " + AP + ": " + RET + " · <b>aseguramiento de armamento</b>: 10 armas largas, 16 cargadores y 338 cartuchos, " + RES + " · corporaciones y detenidos: no fijados · " + FU,
  panel="<b>Aseguramiento de armamento</b>, cifras solo por resumen", inst="Gabinete de Seguridad <span class=\"muted-note\">(boletín por republicadores, solo por resumen)</span>", nac=NIN, conf="★★☆☆☆",
  campo="cifras, municipio y día de la acción solo por resumen; republicadores del boletín, una sola fuente", I=0, N=0, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm="ARG-145-ARM-004",
  desl="Juan R. Escudero en el índice: ARG-139-REC-002 (El Terrero, drones, 19-oct): otro hecho. Republicadores del boletín: no suman fuente independiente."),
]

# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-145-REC-001", estado="MX-TAM", region="Noreste", fecha="2026-10-29", hora="no fijada; la captura que la precede, ~11:00 (solo por resumen)", orig="ARGOS 144 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=1, he=2, cu=0,
  ent="Tamaulipas", mun="Matamoros", dia="29-OCT, POR RUTA",
  title="TAMAULIPAS · MATAMOROS — BLOQUEOS Y BALACERAS: MUERE UNA NIÑA DE SIETE AÑOS; SU MADRE Y UN RESCATISTA, HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 — HORA SOLO POR RESUMEN</code> · Matamoros · jueves 29-OCT, por ruta (Proceso 2026/10/29) · hora de la muerte no publicada; la captura que precede a los bloqueos, ~11:00, " + RES + ": anterior probable a la apertura de ARGOS 145; si la muerte resulta posterior a las 11:36, es hecho propio de ARGOS 145 · <b>1 niña muerta</b>, por <i>slug</i> (Proceso: «bloqueos y balaceras… dejan una niña sin vida»); <b>de 7 años y estadounidense</b>, «murió en operativo», por titular (Infobae 2026/10/30); «en medio de fuego cruzado», por titular (ABC Noticias): circunstancia contradicha (🔴 víctima civil ajena) · <b>2 heridos</b>: su madre y un rescatista, por <i>slug</i> (Proceso) · origen del disparo, en investigación, " + RES + "; un familiar lo atribuye a un helicóptero, " + RES + ": no se integra · <b>muertos de la jornada</b>: «seis», por titular (Proceso 2026/10/30; La Jornada 2026/10/30; Infobae 2026/10/31); «cinco», por titular (Expreso 2026/10/31): <code>CIFRA CONTRADICHA — NO ARBITRADA</code> · los demás, al chocar contra vehículos incendiados de los bloqueos, por titular (ABC Noticias 2026/10/30; El Mañana 2026/10/31): no por agresión directa; desarrollo de ARG-144-008, fuera de totales · <b>52 vehículos calcinados</b>, por titular (Excélsior, sin fecha en la ruta); <b>72 retirados</b>, por titular (La Jornada 2026/10/31) · ningún detenido por las muertes, " + RES,
  panel="<b>Niña de 7 años muerta</b> en la jornada de bloqueos; 2 heridos; muertos de la jornada: 5 o 6, contradicho", inst="Vocería de Seguridad de Tamaulipas <span class=\"muted-note\">(por titular de un medio sin fecha)</span>", nac="Infobae · Proceso · La Jornada · Latinus · Excélsior",
  conf="★★★☆☆", campo="hora no fijada; total de muertos contradicho; circunstancia de la muerte contradicha", I=1, N=5, R=3, A=0,
  fechadas=["Proceso (2026/10/29)", "Infobae (2026/10/30)", "Proceso (2026/10/30)", "La Jornada (2026/10/30)", "ABC Noticias (2026/10/30)", "Infobae (2026/10/31)", "El Mañana (2026/10/31)", "Expreso (2026/10/31)"],
  desl="Los bloqueos son ARG-144-008 y la captura, ARG-144-015 (ventana de ARGOS 144): esta ficha registra a la víctima, no repite el bloqueo. Capturado identificado como Axel Alfredo Cárdenas Rodríguez, «El Titán», por titular (Infobae 2026/10/29). Nombres de las víctimas: medios locales, no se reproducen. «Siete muertos» (Elefante Blanco 2026/10/30): no reverificado."),
 dict(id="ARG-145-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-10-29", hora="poco antes de las 11:00, «mientras desayunaban» (solo por resumen)", orig="ARGOS 144 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (restaurante Los Ranchos, zona Marina Mazatlán)", dia="29-OCT, POR RUTA",
  title="SINALOA · MAZATLÁN — ATAQUE ARMADO EN UN RESTAURANTE: DOS COMENSALES MUERTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 — HORA SOLO POR RESUMEN</code> · Mazatlán · <code>RESTAURANTE LOS RANCHOS, ZONA MARINA MAZATLÁN, POR TITULAR (SINALOAHOY)</code> · jueves 29-OCT, por ruta (El Diario de Chihuahua 2026/oct/29) · poco antes de las 11:00, «mientras desayunaban», " + RES + ": anterior probable a la apertura de ARGOS 145 (11:36 del 29); si resulta posterior, es hecho propio de ARGOS 145 · <b>2 muertos</b>, por titular (El Diario de Chihuahua; El Universal: «eran comensales»; El Financiero 2026/10/30); «cobra su segunda víctima mortal», por titular (Luz Noticias 2026-10-29) (🔴 homicidio múltiple) · uno murió en el lugar y otro después, " + RES + " · la FGE investiga, por titular (Sinaloahoy): no es declaración · <b>ningún detenido publicado</b>",
  panel="<b>Ataque en un restaurante: 2 comensales muertos</b>", inst=SB, nac="Reforma · El Universal · El Financiero",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=3, R=2, A=0,
  fechadas=["El Diario de Chihuahua (2026/10/29)", "El Diario del Noroeste (2026/10/29)", "Luz Noticias (2026/10/29)", "El Financiero (2026/10/30)"],
  desl="Los Ranchos y Marina Mazatlán no figuran en las cinco ediciones previas ni en el índice. El Diario de Chihuahua republica a Reforma: una sola fuente. Versión temprana «un muerto y un herido grave» (Extraoficial): superada por los titulares posteriores."),
 dict(id="ARG-145-REC-003", estado="MX-VER", region="Golfo", fecha="2026-10-29", hora="mañana (solo por resumen)", orig="ARGOS 144 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=1,
  ent="Veracruz", mun="Coatzacoalcos (col. Francisco Villa, calle Mixteca)", dia="29-OCT, POR RUTA",
  title="VERACRUZ · COATZACOALCOS — HALLAN EL CUERPO DECAPITADO DE UN HOMBRE CON MENSAJE DENTRO DE UNA VIVIENDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 — HORA SOLO POR RESUMEN</code> · Coatzacoalcos · <code>COL. FRANCISCO VILLA, CALLE MIXTECA, POR TITULAR (GOLPE POLÍTICO)</code> · jueves 29-OCT, por ruta (La Silla Rota; Golpe Político 2026/10/29) · mañana, " + RES + ": anterior probable a la apertura de ARGOS 145; si resulta posterior, es hecho propio de ARGOS 145 · <b>cuerpo de hombre decapitado</b>, por titular (La Silla Rota; XEU; El Buen Tono), <b>con mensaje</b>, por titular (La Nigua); «mensajes», por titular (Gráfico al Día 2026/10/30): número contradicho · una nota describe tronco y extremidades, " + RES + ": descripción contradicha (🔴 restos humanos con mensaje) · dentro de una vivienda, por titular (Golpe Político) · «tras hallazgo de cabeza, localizan cuerpo de hombre decapitado», por <i>slug</i> (La Silla Rota); «investigan posible relación» con la cabeza hallada frente al Poder Judicial (ARG-144-REC-002), por titular (XEU; La Aldea): <code>POSIBLE MISMA VÍCTIMA QUE ARG-144-REC-002 — CUERPOS NO SUMABLES ENTRE EDICIONES HASTA COTEJO GENÉTICO</code> · víctima no identificada · <b>ningún detenido publicado</b>",
  panel="<b>Cuerpo decapitado con mensaje</b> dentro de una vivienda", inst=SB, nac="La Silla Rota · Milenio",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=5, A=0,
  fechadas=["La Silla Rota (2026/10/29)", "Golpe Político (2026/10/29)", "La Aldea de la Información (2026/10/30)", "Gráfico al Día (2026/10/30)"],
  desl="Calle Mixteca no figura en las cinco ediciones previas; col. Francisco Villa de Coatzacoalcos, solo en un visto de ARGOS 142 (checador de autobuses, sin fecha): otro hecho. Cuerpo hallado sin causa de muerte informada por autoridad. Atribución del mensaje a un grupo: una fuente, no se reproduce."),
 dict(id="ARG-145-REC-004", estado="MX-TLA", region="Centro", fecha="2026-10-28", hora="aviso ~15:00, día no fijado (solo por resumen)", orig="ARGOS 144 O ANTERIOR — DÍA DEL HALLAZGO NO FIJADO", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Tlaxcala", mun="Tetlatlahuca (Santa Ana Portales, junto al río Zahuapan; límite con Nativitas)", dia="PUB. 28-OCT, POR RUTA",
  fecha_txt="publicado el 2026-10-28 — DÍA DEL HALLAZGO NO FIJADO",
  title="TLAXCALA · TETLATLAHUCA — HALLAN RESTOS HUMANOS CALCINADOS JUNTO AL RÍO ZAHUAPAN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 144 O ANTERIOR — DÍA DEL HALLAZGO NO FIJADO</code> · Tetlatlahuca · <code>SANTA ANA PORTALES, CANAL A ~100 M DEL RÍO ZAHUAPAN, SOLO POR RESUMEN; «ZONA LIMÍTROFE DE NATIVITAS», POR TITULAR (LA PRENSA DE TLAXCALA)</code> · publicado el miércoles 28-OCT, por ruta (Intolerancia Diario 2026/10/28) · aviso ~15:00, sin día, " + RES + " · <b>restos humanos calcinados</b>, por titular (Quadratín Tlaxcala; La Prensa de Tlaxcala; ABC Tlax), <b>en reducción esquelética</b>, por titular (Estilo Tlax; Puebla Roja) (🔴 restos humanos) · sexo e identidad no establecidos · <b>número de víctimas: no publicado</b> — <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · la FGJ de Tlaxcala tiene el caso, " + RES,
  panel="<b>Restos humanos calcinados</b> junto al río Zahuapan; número de víctimas no publicado", inst=SB, nac=NIN,
  conf="★★★☆☆", campo="día del hallazgo no fijado; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Intolerancia Diario (2026/10/28)"],
  desl="Publicado el 28 (ventana de ARGOS 144); día del hallazgo no fijado. La Prensa de Tlaxcala lo sitúa junto al río Atoyac: lugar contradicho."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ND_ALL = list(range(10))
ARM = [
 dict(id="ARG-145-ARM-001", ficha="ARG-145-010", estado="MX-CMX", region="Centro", color="verde", ent="Ciudad de México", mun="Iztapalapa (col. Lomas Estrella)",
  fecha="2026-10-30", fecha_txt="pub. 30-oct; día del cateo solo por resumen", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="SSC Ciudad de México <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: «armas» por titular (Milenio), sin cifra citable (2 largas y 2 cargadores, solo por resumen); 3 detenidos por titulares sin fecha, sin cifra de autoridad: n/d; ver ARG-145-010",
  fuentes=["La Silla Rota (2026/10/30)", "Milenio (sin fecha en la ruta)", "NX Noticias (sin fecha en la ruta)"]),
 dict(id="ARG-145-ARM-002", ficha="ARG-145-011", estado="MX-COA", region="Noreste", color="verde", ent="Coahuila", mun="Piedras Negras (col. Real del Norte)",
  fecha="2026-10-29", fecha_txt="acciones del 29-oct; hora no fijada", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="Ejército, GN, Marina y FGE Coahuila <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: «armamento» por titular (Potosinoticias), sin cifra citable (1 larga y 94 cartuchos, solo por resumen); detenidos no publicados; ver ARG-145-011",
  fuentes=["Potosinoticias (2026/10/30)", "RED113 (2026/10)", "Tallapolítica (sin fecha en la ruta)"]),
 dict(id="ARG-145-ARM-003", ficha="ARG-145-004", estado="MX-NLE", region="Noreste", color="amarillo", ent="Nuevo León", mun="Vallecillo",
  fecha="2026-10-29", fecha_txt="29-oct, por ruta; noche, solo por resumen", hora="noche (solo por resumen)", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="Fuerza Civil <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: aseguramiento tras enfrentamiento; 2 largas solo por resumen; ningún detenido publicado (2 abatidos); ver ARG-145-004",
  fuentes=["ABC Noticias (2026/10/29)", "La Verdad (2026/10)", "N+ (sin fecha en la ruta)"]),
 dict(id="ARG-145-ARM-004", ficha="ARG-145-012", estado="MX-GRO", region="Sureste", color="verde", ent="Guerrero", mun="Juan R. Escudero",
  fecha="2026-10-29", fecha_txt="acciones del 29-oct; hora no fijada", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=False,
  corp="Gabinete de Seguridad <span class=\"muted-note\">(republicadores, solo por resumen)</span>", conf="No confirmado",
  nota="<code>NO CONFIRMADO — NO SE INTEGRA</code>: 10 largas, 16 cargadores y 338 cartuchos solo por resumen; fuente única (republicadores); ver ARG-145-012",
  fuentes=["RED113 (2026/10)", "Tallapolítica (sin fecha en la ruta)"]),
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
assert TOT == [0] * 10 and ND == [True] * 10, (TOT, ND)
assert cnt == {"rojo": 1, "amarillo": 8, "verde": 3}, cnt
assert cnt_rec == {"rojo": 4, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (5, 1, 2, 3, 2, 1), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,25", DENS
assert (NAP, NFR, NRET) == (5, 1, 3), (NAP, NFR, NRET)
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
      <b>1. SOLICITE A LA FISCALÍA Y A LA VOCERÍA DE SEGURIDAD DE TAMAULIPAS EL DICTAMEN BALÍSTICO, LA LISTA OFICIAL DE VÍCTIMAS Y EL PROTOCOLO DE RETIRO DE VEHÍCULOS INCENDIADOS EN CARRETERA</b> (ARG-145-REC-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE SINALOA LA IDENTIFICACIÓN GENÉTICA Y EL TEXTO DEL MENSAJE DE CULIACÁN, Y EL COTEJO BALÍSTICO DE LOS ATAQUES DE MAZATLÁN</b> (ARG-145-001, -008 y ARG-145-REC-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE VERACRUZ EL COTEJO GENÉTICO ENTRE LOS DOS HALLAZGOS DE COATZACOALCOS</b> (ARG-144-REC-002 y ARG-145-REC-003).
      <br><b>4. SOLICITE A LAS FISCALÍAS DE BAJA CALIFORNIA Y NUEVO LEÓN LOS DICTÁMENES BALÍSTICOS Y DE USO DE LA FUERZA</b> (ARG-145-003 y -004).
      <br><b>5. AUDITE CON LAS FISCALÍAS DE QUINTANA ROO, DEL ESTADO DE MÉXICO Y DE GUANAJUATO EL SALDO OFICIAL DE CANCÚN, VALLE DE CHALCO Y PÉNJAMO</b> (ARG-145-002 y vistos del panorama).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>29-oct 11:36 → 31-oct 11:14 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto de ventanas anteriores</b>, atenuadas, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: ninguna arma ni detenido integrado al total: cifras solo por resumen o sin cifra de autoridad · <b>muertos por agresión</b>: no incluyen los 3 abatidos (ARG-145-003 y -004) ni la segunda víctima de Pénjamo (ARG-145-002, contradicha) · <b>cuerpos hallados</b>: {CU} con causa no informada por autoridad · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b> (día no fijado frente a las 11:36 del 29): ARG-145-010, -011 y -012 · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos, {HE_REC} heridos y {CU_REC} cuerpo; efecto sobre ARGOS 144, en el archivo de fuentes. <b>Cálculo propio</b>.
    <br><b>Vistos, fuera de totales</b> — <b>de la ventana de ARGOS 144</b> (🟢 o 🟡, no se recuperan): Guadalajara, robo a un banco con bomba molotov (~10:30 del 29, {RES}) · Morelos: Xochitepec, Temixco y Cuernavaca (Acapantzingo) · Coahuayana, 3 detenidos con órdenes de aprehensión (boletín federal del 29, {RES}): posible mismo operativo que una nota del 29-oct (AFmedios) no fichada en ARGOS 144; no se ficha · <b>sin ruta fechada ni titular con día</b> — <code>SIN RUTA FECHADA — NO SE FICHA</code>: <b>Cancún, Paseos del Mar, ataque armado: 3 muertos</b>, por titular (Sipse; Cambio22); viernes 30, ~14:00, {RES} · <b>Valle de Chalco, San Miguel Xico: 2 muertos y 1 herido</b>, por titular (Quadratín Edomex, fuente única); noche del viernes 30, {RES}; otra fuente, 1 muerto y 1 herido en la 2.ª Secc., madrugada del sábado, {RES}: <code>CIFRA CONTRADICHA</code> · Zihuatanejo, chofer de transporte (jue 29, ~15:00, {RES}) · Culiacán, Los Girasoles · Ciudad Obregón, Las Haciendas · Cuautitlán, locutor muerto por bala perdida · Puebla, mujer asesinada en su vivienda · Cuernavaca (col. 1.º de Mayo) y Yautepec (noche del 29, solo por compendio).
    <br><b>Seguimiento, fuera del semáforo</b>: <b>ARG-132-002 (Orizaba)</b>: el policía ministerial herido en el cateo del 13-oct murió el viernes 30, por titular (La Silla Rota; Golpe Político; Plumas Libres 2026/10/30); esquela de la FGE, por titular (N+) · <b>ARG-144-002 (Indaparapeo)</b>: la FGE atribuye el ataque a una confusión, por titular (Meganoticias; PCM); ningún detenido · <b>ARG-144-001 (Magdalena de Kino)</b>: ningún detenido, {RES} · <b>ARG-134-REC-004 (Almoloya)</b>: FGR vincula a proceso a cuatro por la red de secuestro, {RES} (Infobae 2026/10/28; El Independiente 2026/10/29) · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[i]) for i in ("ARG-145-001", "ARG-145-002", "ARG-145-003", "ARG-145-004"))
co2 = "\n".join(ficha(byid[i]) for i in ("ARG-145-005", "ARG-145-006", "ARG-145-007"))
co2b = "\n".join(ficha(byid[i]) for i in ("ARG-145-008", "ARG-145-009"))
co2c = "\n".join(ficha(byid[i]) for i in ("ARG-145-010", "ARG-145-011", "ARG-145-012"))
co3 = "\n".join(ficha(rbyid[i], True) for i in ("ARG-145-REC-001", "ARG-145-REC-002", "ARG-145-REC-003", "ARG-145-REC-004"))
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
 tile(1, "Armas largas", tv(1), "Iztapalapa, Piedras Negras y Vallecillo: cifras solo por resumen; Juan R. Escudero, no confirmado"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "Piedras Negras y Juan R. Escudero: cifras solo por resumen"),
 tile(4, "Cargadores", tv(5), "Iztapalapa y Juan R. Escudero: cifras solo por resumen"),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: ninguna cifra de autoridad; Iztapalapa, 3 por titulares sin fecha"),
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
    <div class="map-caption">Aseguramientos cualitativos: Ciudad de México, Coahuila y Nuevo León (este, tras enfrentamiento); Guerrero, no confirmado.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
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
    <b>Lectura regional</b>: ninguna región con arma ni detenido integrado al total. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: los tres integrados de la tabla; Juan R. Escudero, no confirmado · Mexicali (ARG-145-003): escopeta del agresor, {RES}, sin fila.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>boletín federal de acciones del 28-oct</b> (ventana de ARGOS 144; solo por republicadores, misma fuente; Milenio, RED113, Certeza Diario): Manuel Ojinaga, Chih. (2 detenidos, 7 cartuchos), Acatic, Jal. (5 vehículos blindados), Ahome y Culiacán, Sin. (precursores y laboratorios), Tuxtepec, Oax. (2 detenidos; armas y granadas sin cifra), todo {RES} · <b>boletín del 29-oct</b>: Jalisco, cateo con un vehículo con blindaje artesanal y 10 cartuchos (municipio no fijado), {RES} · <b>Concordia, Sin., La Guásima</b>: 5 largas, 32 cargadores y 1,138 cartuchos, {RES} («cinco armas largas y más de mil cartuchos», por titular, Meganoticias); día no fijado (boletín Ahome-Concordia): <code>FECHA NO FIJADA — NO SE INTEGRA</code>; no es Zavala (ARG-141-REC-005) · <b>Acaponeta, Nay.</b> (agregado estatal; 115 cartuchos, 4 cargadores, {RES}; día no fijado) · <b>Matamoros</b>: armamento de la captura, ARG-144-015, ventana de ARGOS 144 · <b>Xochitlán de las Flores, Tula, Hgo.</b> (PGJEH; 1 corta y 1 larga, {RES}; La Silla Rota 2026/10/28): ventana de ARGOS 144.
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
      <tr><td><b>Puebla</b><br>Huejotzingo</td><td>Feminicidio · <b>candidato de ARGOS 144, sin cambio</b></td><td><b>55 años</b>, por titular (Heraldo de Puebla; Retodiario 2026/10/29)</td><td>FGE Puebla <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · el boletín del dominio con «55 años» es de otro caso (julio de 2025): otro caso</td><td>Bajo</td></tr>
      <tr><td><b>Estado de México</b><br>Ecatepec</td><td>Homicidio y tentativa · <b>candidato de ARGOS 144, sin cambio</b></td><td><b>68 años</b>, por titular (Línea por Línea 2026/10/28)</td><td>FGJEM <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>fgjem.edomex.gob.mx</code> solo devolvió edictos</td><td>No confirmado</td></tr>
      <tr><td><b>Zacatecas</b><br>Fresnillo</td><td>Juan Manuel «N» · <b>candidato de ARGOS 143, sin cambio</b></td><td><b>68 años</b>, por titular (ECOdiario)</td><td>FGJ Zacatecas <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>fiscaliazacatecas.gob.mx</code> sin el caso</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Triple feminicidio; fallo condenatorio del 9-oct · <b>candidato de ARGOS 140 a 144</b></td><td><b>Sin pena</b>: la audiencia continúa el 5-nov, {RES}</td><td>Tribunal de Enjuiciamiento <span class="muted-note">(por medios)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>HEREDADO — NO REVERIFICADO</code></td><td>Bajo</td></tr>
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
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>26 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BCS, Son, Chih, Sin, Dgo · NL, Zac, Tamps · Jal, Col, Nay, Ags, Gto, Mich · CDMX, Edomex, Mor, Pue, Tlax · Ver, Tab · Chis, Oax, Gro, Yuc, QRoo · <b>23 con páginas de boletines y 3 solo con páginas normativas, edictos o convocatorias</b> (Sin, Edomex, Son)</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada (Jalisco: título del 29-oct solo por resumen)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>24</b> fiscalías estatales revisadas · <b>2 con título de condena sin ruta fechada</b>: Jal (29-oct, {RES}), Oax (28 y 29-oct, {RES})</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>1</b>: Coah (<code>fge.coahuila.gob.mx</code>) · <b>dominio de la fiscalía no confirmado</b>: <b>1</b>, Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>4</b>: BC, SLP, Hgo, Qro</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 31-oct 08:30: código <code>000</code> (proxy: conexión rechazada)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en las 10 que ARGOS 144 dejó solo con consulta amplia —BCS · NL, Zac, Coah · Hgo, Qro · Oax, Camp, Yuc— y QRoo por hechos, sin consulta de «bloqueos / instalaciones» · Tamps, Ver, Tab, Edomex, CDMX, Mor, Pue, Tlax, Gto, BC, Sin, Chih con consulta por hechos · SLP, Dgo, Jal, Col, Nay, Ags, Chis, Gro, Mich, Son: <b>solo consulta regional amplia</b> · <b>armamento: 8 de 32 por dominio oficial</b> —BCS, Dgo · Tamps, Zac · Mich · CDMX, Pue · Ver—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · dominio sin páginas: Tab, Coah · <code>NO REVISADA</code> (22): BC, Son, Chih, Sin · NL, SLP · Jal, Col, Nay, Ags, Gto · Edomex, Mor, Tlax, Hgo, Qro · Chis, Oax, Gro, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 28-oct</b>: publicadas por republicadores (Milenio, RED113, Certeza Diario): ventana de ARGOS 144 · <b>acciones del 29-oct</b>: por republicadores (RED113, Tallapolítica): misma fuente, sin indexar en <code>gob.mx</code> · <b>acciones del 30-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 31-OCT 08:30: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Un rojo propio</b> (cálculo propio): restos humanos con mensaje en Culiacán (Sin). <b>Alza del riesgo nacional frente a ARGOS 144 no acreditada</b>.
      <br><b>2.</b> <b>Violencia operativa</b>: ocho amarillos —cinco homicidios dolosos, uno con saldo contradicho; dos confrontaciones con corporaciones estatales con tres abatidos; un cuerpo hallado— en cinco entidades (cálculo propio).
      <br><b>3.</b> <b>Noroeste</b>: siete de los doce hechos propios (Sin 3, BC 3, Chih 1) y una recuperación roja en Sinaloa (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: tres verdes, ninguno con cifra de armamento o de detenidos citable; ninguna sentencia integrable (cálculo propio; totales, en el panorama).
      <br><b>5.</b> <code>TRES DE DOCE HECHOS CON CLÁUSULA DE RETIRO Y CUATRO ROJOS RECUPERADOS DE ARGOS 144 O ANTERIORES; VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 144 SIN NORMALIZAR POR HORA. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. MATAMOROS: LA CAPTURA DE UN OBJETIVO PRIORITARIO FUE SEGUIDA EL MISMO DÍA DE BLOQUEOS CON VEHÍCULOS INCENDIADOS QUE MATARON A MÁS CIVILES POR CHOQUE QUE POR DISPARO</b> (cálculo propio: con el total de seis, por titular, 6 − 1 = 5 en choques; con el de cinco, 4): ARG-144-015 (captura), ARG-144-008 (bloqueos) y ARG-145-REC-001 (víctimas); vínculo no acreditado entre los autores de los bloqueos y el grupo del capturado. Línea: <b>solicitar a la Vocería de Seguridad y a la Defensa el protocolo de cierre carretero y retiro de vehículos incendiados ante capturas en la frontera tamaulipeca</b>.
      <br><b>2. RESTOS HUMANOS EXHIBIDOS O CON MENSAJE: CUATRO HALLAZGOS EN DOS ESTADOS DEL 27 AL 29-OCT, DOS CABEZAS EN HIELERA EN SINALOA</b> (cálculo propio; desarrolla la Conclusión 3 de ARGOS 144): ARG-144-REC-004 (Mazatlán, hielera ante el Palacio Municipal) y ARG-145-001 (Culiacán, hielera con mensaje); ARG-144-REC-002 y ARG-145-REC-003 (Coatzacoalcos: cabeza frente al Poder Judicial de la Federación; cuerpo decapitado con mensaje, posible misma víctima); vínculo no acreditado. Línea: <b>solicitar a las fiscalías de Veracruz y Sinaloa el cotejo genético y el texto íntegro de los mensajes</b>.
      <br><b>3. MAZATLÁN: TRES HECHOS CON VÍCTIMAS DEL 29 AL 31-OCT, UNO CONTRA COMENSALES DE UN RESTAURANTE</b> (cálculo propio): ARG-145-REC-002 (2 muertos), ARG-145-008 (1 muerto) y ARG-145-009 (cuerpo, causa no informada); vínculo no acreditado. Línea: <b>solicitar a la Fiscalía de Sinaloa el cotejo balístico de los dos ataques y vigilar la zona Marina, el fracc. Santa Fe y la playa Pato Blanco</b>.
      <br><b>4. TRES ABATIDOS EN DOS CONFRONTACIONES CON CORPORACIONES ESTATALES EL MISMO DÍA, EN DOS ESTADOS</b> (cálculo propio, 29-oct): ARG-145-003 (Mexicali, FESC; la Fiscalía revisa el uso de la fuerza letal) y ARG-145-004 (Vallecillo, Fuerza Civil); quién inició, no acreditado en ninguno; vínculo no acreditado. Línea: <b>solicitar a las fiscalías de Baja California y Nuevo León los dictámenes balísticos y de uso de la fuerza</b>.
      <br><b>5. TECATE (PENDIENTE DE CONFIRMACIÓN OFICIAL, NO INTEGRADO): CONDENA, POR TITULAR, UNOS DOS AÑOS DESPUÉS DE UN ATAQUE A LA GUARDIA NACIONAL</b> (cálculo propio: 2024, por titular, a octubre de 2026): cuatro sentenciados, hasta 16 años, por titular, por portación de armas de uso exclusivo y asociación delictuosa. Línea: <b>solicitar a la FGR el comunicado con la causa penal, las penas individuales y la firmeza</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>fgr.org.mx</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO Y VIOLENCIA OPERATIVA: CULIACÁN, PÉNJAMO, MEXICALI Y VALLECILLO", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA: CUAUHTÉMOC Y TIJUANA", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA: MAZATLÁN", co2b)
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
