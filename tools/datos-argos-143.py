# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 143.
Uso: python3 tools/datos-argos-143.py <plantilla ARGOS 142> <salida>
Ventana: 27-oct 08:45 → 28-oct 08:28 CDMX. Archivo: argos-2026-10-28.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "143", "2026-10-28", "08:28"
CONSULTA = "2026-10-28, última búsqueda 08:40"
DUR = "23 h 43 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 08:45 DEL 27, ES DE LA VENTANA DE ARGOS 142 Y SE RETIRA DE ESTE TOTAL</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJO
 dict(id="ARG-143-001", estado="MX-TAB", region="Golfo", color="rojo", impacto="grande", fecha="2026-10-27", hora="no fijada; «el día anterior», primeras horas y horas después (solo por resumen)", mu=0, he=0, cu=3, hk=1,
  ent="Tabasco", mun="Centro (carretera Villahermosa–Frontera: km 22.5, entrada al pozo Racemosa, y cerca de Villa Ocuiltzapotlán)", dia="PUB. 27-OCT; DÍA DEL HALLAZGO NO FIJADO",
  fecha_txt="publicado el 2026-10-27 — DÍA DEL HALLAZGO NO FIJADO",
  title="TABASCO · CENTRO — HALLAN LOS CUERPOS DE TRES HOMBRES ENVUELTOS EN SÁBANAS EN EL CORREDOR VILLAHERMOSA–FRONTERA",
  hecho="Centro · <code>CARRETERA VILLAHERMOSA–FRONTERA: KM 22.5, ENTRADA AL POZO RACEMOSA, Y CERCA DE VILLA OCUILTZAPOTLÁN, SOLO POR RESUMEN</code> · publicado el martes 27-OCT, por ruta (La Razón 2026/10/27) · " + AP + " · «el día anterior», un cuerpo en las primeras horas y dos horas después, " + RES + ": " + RET + " · <b>3 personas sin vida</b>, por titular (La Razón, «hallan sin vida a tres personas en Tabasco») (🔴 hallazgo múltiple) · <b>3 hombres</b>, envueltos en sábanas, " + RES + " · huellas de tortura y lesiones por arma de fuego, por titular de un medio regional (El Sol del Sureste / Diario Presente, «tres cuerpos con huellas de tortura»): <code>FUENTE ÚNICA — CAUSA DE MUERTE NO INFORMADA POR AUTORIDAD</code> · Ejército, Guardia Nacional y SSPC en el lugar; carpeta por homicidio de la Fiscalía de Tabasco, " + RES + " · víctimas sin identificar · <b>ningún detenido publicado</b>",
  panel="<b>Tres cuerpos hallados</b> en el corredor Villahermosa–Frontera", inst=SB, nac="La Razón", conf="★★★☆☆",
  campo="día y hora del hallazgo solo por resumen; tortura por una sola fuente; ninguna fuente institucional", I=0, N=1, R=1, A=0,
  fechadas=["La Razón (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="Racemosa, Ocuiltzapotlán y Macultepec no figuran en las cinco ediciones previas ni en el índice. ARG-140-006 (Huimanguillo, fosa, 22-oct) y ARG-138-002 (Cárdenas, fosa, 19-oct): otros municipios, otros hechos. El Novillo y El Espino (dos cuerpos, 24-oct, sin ruta fechada): otro punto, otro día. «Asesinan a tres personas en el centro de Tabasco» (El Universal, sin fecha): no se atribuye."),
 # ======================= AMARILLOS
 dict(id="ARG-143-002", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-10-27", hora="antes del mediodía, ~11:00 (solo por resumen)", mu=0, he=0, cu=0, hk=11,
  ent="Guanajuato", mun="Celaya (carretera Salvatierra–Celaya)", dia="27-OCT, POR RUTA",
  title="GUANAJUATO · CELAYA — AGENTES FEDERALES FRUSTRAN EL ASALTO A UN CAMIÓN DE CARGA EN LA CARRETERA SALVATIERRA–CELAYA: UN PRESUNTO ASALTANTE ABATIDO",
  hecho="Celaya · <code>CARRETERA SALVATIERRA–CELAYA; CERCA DE MABE, OJO SECO O CERRO PRIETO, SOLO POR RESUMEN: CONTRADICHO</code> · martes 27-OCT, por ruta (AM; MVS; Correo; La Silla Rota; Potosinoticias; Síntesis 2026/10/27) · " + AP + " · ~11:00, " + RES + " · <b>agentes federales en patrullaje detectan el trasvase de la carga de un camión</b>, por <i>slug</i> (La Silla Rota, «patrullaje-detecto-asalto-que-derivo-en-balacera») · los asaltantes disparan primero, " + RES + ": <code>QUIÉN INICIÓ NO ACREDITADO POR AUTORIDAD</code> (🟡 confrontación derivada de una intervención de la autoridad) · <b>1 presunto asaltante abatido</b> y <b>1 herido que huye</b>, por titulares (AM; MVS) · ningún agente lesionado publicado · Guardia Nacional, AIC y Fuerzas de Seguridad Pública del Estado en apoyo; el secretario de Seguridad lo informó en redes, " + RES + " · camión, 3 teléfonos y 1 inhibidor de señal asegurados, " + RES + " · <b>armas aseguradas: no publicadas</b> · <b>ningún detenido publicado</b>",
  panel="<b>Asalto a camión frustrado por agentes federales</b>: 1 presunto asaltante abatido", inst="SSPC" + PR, nac="MVS · La Silla Rota · Infobae (EFE)", conf="★★★☆☆",
  campo="hora y quién inició solo por resumen; punto exacto contradicho", I=0, N=3, R=4, A=0,
  fechadas=["AM (2026/10/27)", "MVS (2026/10/27)", "Correo (2026/oct/27)", "La Silla Rota (2026/10/27)", "Potosinoticias (2026/10/27)", "Síntesis (2026/10/27)", "Infobae/EFE (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="La carretera Salvatierra–Celaya no figura en las cinco ediciones previas. Celaya en el índice: ARG-122-002, ARG-128-002 y ARG-137-REC-001: otros hechos. El abatido no se suma a «muertos por agresión»: se registra aparte."),
 dict(id="ARG-143-003", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="tarde, ~15:00 (solo por resumen)", mu=1, he=0, cu=0, hk=15,
  ent="Guanajuato", mun="Celaya (inmediaciones del Mercado de Abastos)", dia="27-OCT, POR RUTA",
  title="GUANAJUATO · CELAYA — ASESINAN A BALAZOS AL DUEÑO DE UN NEGOCIO DE COMIDA RÁPIDA CERCA DEL MERCADO DE ABASTOS",
  hecho="Celaya · <code>INMEDIACIONES DEL MERCADO DE ABASTOS, SOLO POR RESUMEN</code> · martes 27-OCT, por ruta (Correo 2026/oct/27) · " + AP + " · ~15:00, " + RES + " · <b>1 muerto</b>: <b>dueño de un negocio de comida rápida</b>, por <i>slug</i> (Correo) (🟡 homicidio doloso único) · agresores en motocicleta, " + RES + " · Policía Municipal y Guardia Nacional acudieron, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Dueño de un negocio asesinado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Correo (2026/oct/27)"], estatus="Pendiente de corroboración", arm=None,
  desl="Mercado de Abastos de Celaya no figura en las cinco ediciones previas. Mismo municipio y día que ARG-143-002: hechos distintos por punto, hora y víctima."),
 dict(id="ARG-143-004", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="no fijada", mu=1, he=0, cu=0, hk=2,
  ent="Guanajuato", mun="Salamanca (col. San Roque, av. del Trabajo)", dia="27-OCT, POR RUTA; HORA NO FIJADA",
  title="GUANAJUATO · SALAMANCA — SIGUEN Y ASESINAN A BALAZOS A UN CONDUCTOR EN LA COLONIA SAN ROQUE",
  hecho="Salamanca · <code>COL. SAN ROQUE, AV. DEL TRABAJO, SOLO POR RESUMEN</code> · martes 27-OCT, por ruta (Correo 2026/oct/27) · " + AP + "; hora no informada: " + RET + " · <b>1 muerto</b>: <b>conductor</b>, por <i>slug</i> (Correo, «asesinan-a-balazos-a-un-conductor-en-la-colonia-san-roque») (🟡 homicidio doloso único) · seguido por sus agresores antes del ataque, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Conductor asesinado a balazos: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; hora no informada", I=0, N=0, R=1, A=0,
  fechadas=["Correo (2026/oct/27)"], estatus="Pendiente de corroboración", arm=None,
  desl="Col. San Roque de Salamanca no figura en las cinco ediciones previas ni en el índice. Salamanca en el índice: ARG-125-044 (25-sep): otro hecho."),
 dict(id="ARG-143-005", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="tarde; primeras notas ~17:50-18:05 (solo por resumen)", mu=1, he=2, cu=0, hk=17.5,
  ent="Chihuahua", mun="Chihuahua (col. Sol de Oriente)", dia="27-OCT, POR RUTA",
  title="CHIHUAHUA · CAPITAL — COMANDO ATACA A TRES HOMBRES EN SOL DE ORIENTE: UN MUERTO Y DOS HERIDOS",
  hecho="Chihuahua · <code>COL. SOL DE ORIENTE, PRADERAS DE MACOUPIN Y SOL DE ALTAIR O CENTAURI, SOLO POR RESUMEN: CONTRADICHO</code> · martes 27-OCT, por ruta (El Diario de Chihuahua 2026/oct/27; En Blanco y Negro; La Gaceta 2026/10/27) · " + AP + " · tarde, " + RES + " · <b>1 muerto</b> y <b>2 heridos</b>, hombres, por titulares (El Diario; En Blanco y Negro) (🟡 homicidio doloso único) · «un muerto y un herido», por titular (El Pueblo, 20261027): <code>NÚMERO DE HERIDOS CONTRADICHO — SE CUENTAN 2</code> · agresores en una Ram y una Cherokee negras; casquillos 9 mm, " + RES + " · Policía Municipal y Fiscalía del Estado en el lugar, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>1 muerto</b> y 2 heridos", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; heridos contradichos; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/27)", "En Blanco y Negro (2026/10/27)", "La Gaceta (2026/10/27)", "El Pueblo (20261027)"], estatus="Parcialmente corroborado", arm=None,
  desl="Sol de Oriente no figura en las cinco ediciones previas ni en el índice. El Saucito (dos muertos y un herido) es del 27-sep: otro hecho, otra ventana."),
 dict(id="ARG-143-006", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="contradicha: ~08:30 / ~08:46 / «poco antes de las 9:00» (solo por resumen)", mu=1, he=0, cu=0, hk=8.8,
  ent="Baja California", mun="Tijuana (Lomas de San Antonio, circuito Mercedes)", dia="27-OCT, POR RUTA; HORA CONTRADICHA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A UN MOTOCICLISTA EN UN CAMINO DE TERRACERÍA DE LOMAS DE SAN ANTONIO",
  hecho="Tijuana · <code>LOMAS DE SAN ANTONIO, CIRCUITO 2 O 3 MERCEDES, SOLO POR RESUMEN: CONTRADICHO</code> · martes 27-OCT, por ruta (Periodismo Negro; PSN 2026/10/27) · " + AP + " · ~08:30, " + RES + " (Zeta); ~08:46 y «poco antes de las 9:00», " + RES + " (otros medios): <code>HORA CONTRADICHA EN TORNO A LA APERTURA</code> — " + RET + " · <b>1 muerto</b>: <b>motociclista</b>, por titulares (Zeta; Periodismo Negro) (🟡 homicidio doloso único) · la Cruz Roja certificó la muerte; indicios de arma corta; Fiscalía del Estado a cargo, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada",
  panel="Motociclista asesinado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora contradicha en torno a la apertura; ninguna fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Periodismo Negro (2026/10/27)", "PSN (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lomas de San Antonio no figura en las cinco ediciones previas ni en el índice. «739 homicidios en 2026» (Zeta): acumulado de un medio, no se integra."),
 dict(id="ARG-143-007", estado="MX-NLE", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="noche, ~19:00 (solo por resumen)", mu=1, he=0, cu=0, hk=19,
  ent="Nuevo León", mun="Guadalupe (col. Valle Soleado)", dia="27-OCT, POR RUTA",
  title="NUEVO LEÓN · GUADALUPE — ASESINAN A BALAZOS A UN HOMBRE EN VALLE SOLEADO",
  hecho="Guadalupe · <code>COL. VALLE SOLEADO, CRUCE DE VALLE SONORA Y VALLE ALTO, SOLO POR RESUMEN</code> · martes 27-OCT, por ruta (MVS; Enfoque Monterrey 2026/10/27) · " + AP + " · ~19:00, «martes por la noche», " + RES + " · <b>1 muerto</b>: hombre de 53 años, en bicicleta, " + RES + "; «asesinan a balazos a hombre», por <i>slug</i> (MVS) (🟡 homicidio doloso único) · dos agresores en motocicleta; 8 casquillos 9 mm, " + RES + " · línea de investigación ligada a venta de droga, atribuida a fuente policial no nombrada, por ruta (MVS 2026/10/28), " + RES + ": <code>NO CONFIRMADA</code> · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Hombre asesinado a balazos: <b>1 muerto</b>", inst=SB, nac="MVS", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=1, A=0,
  fechadas=["MVS (2026/10/27)", "Enfoque Monterrey (2026/10/27)", "MVS (2026/10/28)"], estatus="Parcialmente corroborado", arm=None,
  desl="Valle Soleado no figura en las cinco ediciones previas ni en el índice. La nota de Apodaca de Telediario es otro hecho."),
 dict(id="ARG-143-008", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="no fijada", mu=1, he=0, cu=0, hk=3,
  ent="Sinaloa", mun="Culiacán (fracc. Chulavista, calle Juan Ledezma)", dia="27-OCT, POR RUTA; HORA NO FIJADA",
  title="SINALOA · CULIACÁN — ASESINAN A UN HOMBRE EN SU CASA DEL FRACCIONAMIENTO CHULAVISTA",
  hecho="Culiacán · <code>FRACC. CHULAVISTA, CALLE JUAN LEDEZMA, SOLO POR RESUMEN</code> · martes 27-OCT, por ruta (Línea Directa 2026-10-27) · " + AP + "; hora no fijada: " + RET + " · <b>1 muerto</b>, «asesinan a un hombre en su casa», por <i>slug</i> (Línea Directa) (🟡 homicidio doloso único) · edad 38 o 43 años, " + RES + ": <code>CONTRADICHA</code> · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Hombre asesinado en su casa: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única con ruta fechada; hora no fijada", I=0, N=0, R=1, A=0,
  fechadas=["Línea Directa (2026-10-27)"], estatus="Pendiente de corroboración", arm=None,
  desl="Chulavista no figura en las cinco ediciones previas ni en el índice. «Al menos seis asesinados el martes en Culiacán» (Meganoticias): recuento de un medio, no se integra; los demás hechos del día, sin ruta fechada, quedan vistos."),
 dict(id="ARG-143-009", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="aviso ~09:00-10:00 (solo por resumen)", mu=0, he=0, cu=1, hk=9.5,
  ent="Sinaloa", mun="Culiacán (Aguaruto, zona de cribas junto al río Culiacán)", dia="27-OCT, POR RUTA",
  title="SINALOA · CULIACÁN — LOCALIZAN UN CUERPO DECAPITADO JUNTO AL RÍO EN LA ZONA DE CRIBAS DE AGUARUTO",
  hecho="Culiacán · <code>ZONA DE CRIBAS DE AGUARUTO, A UN COSTADO DEL RÍO CULIACÁN, POR <i>SLUG</i></code> · martes 27-OCT, por ruta (Línea Directa 2026-10-27) · " + AP + " · aviso ~09:00-10:00, " + RES + " · <b>1 cuerpo</b>, «persona asesinada», por <i>slug</i> (Línea Directa); decapitado, por <i>slug</i> (Noroeste) (🟡 hallazgo de un cuerpo) · descomposición avanzada, «varios días» sin vida, " + RES + ": <code>FECHA DE LA MUERTE NO FIJADA — CAUSA NO INFORMADA POR AUTORIDAD</code> · sin identificar · <b>ningún detenido publicado</b>",
  panel="<b>Cuerpo decapitado</b> hallado junto al río", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; fecha de la muerte y causa no informadas por autoridad", I=0, N=0, R=4, A=0,
  fechadas=["Línea Directa (2026-10-27)"], estatus="Parcialmente corroborado", arm=None,
  desl="Aguaruto en el índice: penal y hechos de otras ediciones, no este hallazgo. Cuerpo envuelto en Tierra Blanca (mañana del 27, sin ruta fechada; hora en torno a la apertura): otro hecho, visto."),
 dict(id="ARG-143-010", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-27", hora="no fijada", mu=1, he=0, cu=0, hk=4,
  ent="Veracruz", mun="Veracruz (col. Centro)", dia="PUB. 27-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-27 — DÍA DEL HECHO NO FIJADO",
  title="VERACRUZ · PUERTO — MATAN A GOLPES A UN ADULTO MAYOR FRENTE A SU VIVIENDA EN LA COLONIA CENTRO",
  hecho="Veracruz · <code>COL. CENTRO, FRENTE A SU VIVIENDA, POR <i>SLUG</i></code> · publicado el martes 27-OCT, por ruta (Golpe Político; La Silla Rota 2026/10/27) · " + AP + "; día y hora no fijados: " + RET + " · <b>1 muerto</b>: <b>adulto mayor</b>, «asesinan a golpes», por <i>slug</i> (Golpe Político) (🟡 homicidio doloso único) · edad 70-80 años: <code>CONTRADICHA</code> · vecinos señalan a un presunto responsable, por <i>slug</i> (La Silla Rota); persona en situación de calle, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Adulto mayor asesinado a golpes: <b>1 muerto</b>", inst=SB, nac="La Silla Rota", conf="★★★☆☆",
  campo="día y hora no fijados; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Golpe Político (2026/10/27)", "La Silla Rota (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="La col. Centro del puerto de Veracruz no figura en las cinco ediciones previas con este hecho."),
 # ======================= VERDE
 dict(id="ARG-143-011", estado="MX-SLP", region="Noreste", color="verde", impacto="pequeno", fecha="2026-10-27", hora="no fijada", mu=0, he=0, cu=0, hk=5,
  ent="San Luis Potosí", mun="Rayón", dia="PUB. 27-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-27 — DÍA DE LA DETENCIÓN NO FIJADO",
  title="SAN LUIS POTOSÍ · RAYÓN — DETIENEN A DOS HERMANOS POR UN PROBABLE HOMICIDIO CALIFICADO",
  hecho="Rayón · publicado el martes 27-OCT, por ruta (Potosinoticias; MC Noticias 2026/10/27) · " + AP + "; día de la detención no fijado: " + RET + " · <b>2 detenidos</b>, «dos hermanos», por titular y <i>slug</i> (Potosinoticias) (🟢 detención) · por <b>probable homicidio calificado</b>, por <i>slug</i>; hecho del 12-OCT, " + RES + ": <code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code> · corporación: no fijada · sin armamento asegurado publicado · identidades: no se reproducen",
  panel="Detención de <b>2 hermanos</b> por un homicidio previo", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día de la detención y del homicidio no fijados; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Potosinoticias (2026/10/27)", "MC Noticias (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="Rayón (SLP) no figura en las cinco ediciones previas ni en el índice (la única coincidencia es el mercado López Rayón de Apatzingán, ARG-142-007). El homicidio del 12-oct no tiene ficha propia. Detención sin armamento con cifra: fuera del conteo de armamento."),
]

# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-143-REC-001", estado="MX-BCN", region="Noroeste", fecha="2026-10-26", hora="~11:30 (solo por resumen)", orig="ARGOS 142 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=3,
  ent="Baja California", mun="Tecate (fosa cerca de Cerro Azul)", dia="26-OCT, POR RUTA",
  title="BAJA CALIFORNIA · TECATE — COLECTIVO LOCALIZA UNA FOSA CLANDESTINA CON LOS RESTOS DE TRES PERSONAS CERCA DE CERRO AZUL",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 142 — HORA SOLO POR RESUMEN</code> · Tecate · <code>CERCA DEL POBLADO DE CERRO AZUL; COL. NUEVA HINDÚ, CERCA DEL RANCHO LAS CREATURAS, EN OTRO MEDIO: CONTRADICHO</code> · lunes 26-OCT, por ruta (Punto Norte 2026/10/26, primera publicación) · ~11:30, " + RES + "; «tarde de este lunes», " + RES + " (Zeta): posterior a las 08:37 · colectivo <b>Unión y Fuerza por Nuestros Desaparecidos Tecate</b>, por titular y cuerpo (Punto Norte) · <b>fosa clandestina con 3 personas enterradas</b>, por titular (Punto Norte) (🔴 fosa) · <b>una mujer y dos hombres</b>, por titular (En Línea BC 2026/10/27); dos masculinos, " + RES + " (Zeta) · un cuerpo con tatuajes, por titular (El Imparcial 2026/10/27) · enterrados al menos 7 meses, estimación del colectivo, " + RES + " · Comisión Estatal de Búsqueda, Guardia Nacional y Fiscalía en el levantamiento, " + RES,
  panel="<b>Fosa con 3 personas</b> (1 mujer y 2 hombres)", inst=SB, nac=NIN,
  conf="★★★☆☆", campo="hora solo por resumen; ubicación contradicha entre medios; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Punto Norte (2026/10/26)", "El Imparcial (2026/10/27)", "En Línea BC (2026/10/27)"],
  desl="Cerro Azul, Nueva Hindú y el colectivo no figuran en las cinco ediciones previas ni en el índice. Tecate en ARGOS 142: ARG-142-001, -002 y -009, otros hechos. Zeta (Nueva Hindú) y Punto Norte (Cerro Azul): mismo día, misma cifra y colectivo: <code>UN SOLO HALLAZGO, UBICACIÓN NO FIJADA</code>."),
 dict(id="ARG-143-REC-002", estado="MX-GUA", region="Occidente", fecha="2026-10-26", hora="tarde (solo por resumen)", orig="ARGOS 142 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=1, he=0, cu=0,
  ent="Guanajuato", mun="Dolores Hidalgo (avenida Sur, florería)", dia="26-OCT, POR RUTA",
  title="GUANAJUATO · DOLORES HIDALGO — ATACAN UNA FLORERÍA CON UNA BOMBA MOLOTOV Y BALEAN A UN HOMBRE, QUE MUERE EN EL HOSPITAL",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 142 — HORA SOLO POR RESUMEN</code> · Dolores Hidalgo · <code>FLORERÍA DE LA AVENIDA SUR, A UNAS CUADRAS DEL CENTRO, SOLO POR RESUMEN</code> · lunes 26-OCT, por ruta (Correo 2026/oct/26, «atacan florería… con una bomba molotov; hay un herido») · tarde, " + RES + "; «lunes 25» en un párrafo de Correo: error de calendario (el 25 fue domingo) · <b>ataque con bomba molotov</b> contra el comercio, por titulares (Correo; La Silla Rota) (🔴 artefacto incendiario: AEI por la taxonomía ARGOS) · <b>1 hombre baleado afuera</b>, por titular (AM, «balean a Jacinto afuera de una florería»), <b>muere en el hospital el 27-OCT</b>, por titulares (Correo 2026/oct/27; AM 2026/10/27) · la Fiscalía de Guanajuato confirmó la muerte, " + RES + " · el comercio ya había sido atacado en septiembre, " + RES + " · <b>ningún detenido publicado</b>",
  panel="<b>Ataque con bomba molotov</b> a una florería: 1 muerto", inst="FGE Guanajuato" + PR, nac="La Silla Rota · N+",
  conf="★★★☆☆", campo="hora solo por resumen; confirmación de la Fiscalía solo por resumen", I=0, N=2, R=3, A=0,
  fechadas=["Correo (2026/oct/26)", "Correo (2026/oct/27)", "AM (2026/10/27)", "La Silla Rota (2026/10/27)"],
  desl="Dolores Hidalgo, la florería y la bomba molotov no figuran en las cinco ediciones previas ni en el índice. El ataque es del 26 (ventana de 142); la muerte del 27 no abre un hecho nuevo."),
 dict(id="ARG-143-REC-003", estado="MX-GUA", region="Occidente", fecha="2026-10-19", hora="noche, ~22:00 (solo por resumen)", orig="ARGOS 138 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Guanajuato", mun="Acámbaro (Campamento Ferrocarrilero, «La Cochinilla»)", dia="19-OCT, POR RUTA",
  title="GUANAJUATO · ACÁMBARO — ATAQUE ARMADO DENTRO DE UNA VIVIENDA DEL CAMPAMENTO FERROCARRILERO: DOS MUERTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 138 — HORA SOLO POR RESUMEN</code> · Acámbaro · <code>CAMPAMENTO FERROCARRILERO («LA COCHINILLA»), DENTRO DE UNA VIVIENDA, POR TITULAR (LA SILLA ROTA; LA NIGUA)</code> · lunes 19-OCT, por ruta (Correo 2026/oct/19); ~22:00, «minutos después de las 10 de la noche», " + RES + ": dentro de la ventana de ARGOS 138 (19-oct 11:05 → 20-oct 07:06) · <b>2 muertos</b>, por titulares (AM 2026/10/20, «2 muertos en Acámbaro»; Correo) (🔴 homicidio múltiple) · hombres armados entraron a la vivienda, " + RES + " · Fiscalía de Guanajuato en el lugar, " + RES + " · ataque previo en la misma colonia el lunes 12-OCT (1 muerto), " + RES + " (AM) · <b>ningún detenido publicado</b> · identidades: no publicadas",
  panel="<b>Ataque armado en una vivienda: 2 muertos</b>", inst=SB, nac="La Silla Rota · Milenio",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=3, A=0,
  fechadas=["Correo (2026/oct/19)", "AM (2026/10/20)", "La Silla Rota (2026/10/20)"],
  desl="Campamento Ferrocarrilero no tiene ficha en ninguna edición (cotejo del índice y de ARGOS 138 a 142). NO es ARG-142-004 (col. Velasco Ibarra, 26-oct). «Dos muertos y tres heridos» (Milenio, Cancha Política) es Chicuacen, 4-sep: otro hecho."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = []
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
HORAS = 23 + 43 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0] * 10 and ND == [True] * 10, (TOT, ND)
assert cnt == {"rojo": 1, "amarillo": 9, "verde": 1}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (7, 2, 4, 3, 0, 3), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert (NFR, NAP, NRET, len(ENT), len(ENT_ROJO)) == (0, 11, 6, 8, 1), (NFR, NAP, NRET, len(ENT), len(ENT_ROJO))
assert DENS == "0,46", DENS
assert sorted(e["id"] for e in E) == [f"ARG-143-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-143-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-27" or x in R, x["id"]
    assert x in E or x["fecha"] < "2026-10-27", x["id"]

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
head = head.replace("<title>ARGOS 142 — Reporte Nacional de Seguridad — 2026-10-27</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE TABASCO LA IDENTIFICACIÓN, LA CAUSA DE MUERTE Y LA FECHA Y HORA DEL HALLAZGO DE LAS TRES VÍCTIMAS</b> (ARG-143-001).
      <br><b>2. SOLICITE A LA SSPC Y A LA FISCALÍA DE GUANAJUATO EL PARTE DE LA INTERVENCIÓN —QUIÉN ABRIÓ FUEGO, ARMAS ASEGURADAS, IDENTIDAD DEL ABATIDO— Y COTÉJELO CON LOS ROBOS A TRANSPORTE DE CARGA DEL TRAMO</b> (ARG-143-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE BAJA CALIFORNIA Y A LA COMISIÓN ESTATAL DE BÚSQUEDA LA UBICACIÓN EXACTA DE LA FOSA Y EL COTEJO GENÉTICO DE LOS RESTOS CON LAS FICHAS DEL COLECTIVO</b> (ARG-143-REC-001).
      <br><b>4. SOLICITE A LA FISCALÍA DE GUANAJUATO EL DICTAMEN DEL ARTEFACTO INCENDIARIO Y EL BALÍSTICO, Y COTEJE EL ATAQUE CON EL DE SEPTIEMBRE CONTRA EL MISMO COMERCIO</b> (ARG-143-REC-002).
      <br><b>5. SOLICITE A LA FISCALÍA DE CHIHUAHUA EL DICTAMEN DE LOS CASQUILLOS 9 MM Y EL REGISTRO DE LAS DOS CAMIONETAS DE LOS AGRESORES</b> (ARG-143-005).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>27-oct 08:45 → 28-oct 08:28 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · dentro de cada color, del más reciente al más antiguo · <b>{len(R)} recuperaciones de alto impacto de ventanas anteriores</b>, atenuadas, <b>fuera de todos los totales</b>.
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
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> — ningún aseguramiento con cifra publicada y día fijado en la ventana; <code>n/d</code> = no publicado en fuente citable, no ausencia · <b>muertos por agresión</b>: no incluyen al presunto asaltante abatido por agentes federales (ARG-143-002) · <b>heridos</b>: 2 en ARG-143-005, contradicho (1 en un medio) · <b>cuerpos hallados</b>: 3 en ARG-143-001 y 1 en ARG-143-009, causa no informada por autoridad · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b>: ARG-143-001 (−1 rojo, −3 cuerpos, −1 entidad), -004, -006, -008 y -010 (−1 amarillo y −1 muerto cada una) y -011 (−1 verde) · <b>recuperaciones, fuera de totales</b>: {MU_REC} muertos y {CU_REC} cuerpos. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: <b>ARG-142-001 y -009 (Tecate)</b>: 1 agente herido por titular (El Imparcial) y 2 por titular (Milenio): <code>SIN ARBITRAR</code>; «2 mueren», por titular de un medio abierto (Radar Tecate), contradicho por todos los demás; detenidos 3, {RES}, con dos juegos de nombres incompatibles; armas de los detenidos: sin cifra · <b>ARG-142-002 (Tecate)</b>: «madre, hija y dos nietos», por titular (Milenio) · <b>ARG-142-003 y -010 (Tehuacán)</b>: «detienen a dos personas con un AR-15», por titular (Síntesis 2026/10/27): 2 detenidos y 1 arma larga, ahora por titular; vinculación no publicada · <b>ARG-142-008 (SLP)</b>: sin segunda fuente con ruta fechada · <b>ARG-136-006 (exfiscal)</b>: impugnación anunciada en las dos causas; sin resolución publicada · <b>ARG-140-020 (Xalapa)</b> y <b>ARG-140-021 (Juchitán)</b>: vinculación no publicada · <b>ARG-134-REC-004 (Almoloya)</b>: cuatro vinculados a proceso y un quinto detenido el 22-oct, {RES} · <b>ARG-140-013 (Linares)</b>: edad 47 o 55, ambas {RES}, y colonia contradicha · <b>ARG-142-013 (Tumbisca)</b>: «en la mañana» en todos los medios, sin hora: sigue en frontera · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[i]) for i in ("ARG-143-001", "ARG-143-002", "ARG-143-003", "ARG-143-004"))
co2 = "\n".join(ficha(byid[i]) for i in ("ARG-143-005", "ARG-143-006", "ARG-143-007", "ARG-143-008", "ARG-143-009", "ARG-143-010", "ARG-143-011"))
co3 = "\n".join(ficha(rbyid[i], True) for i in ("ARG-143-REC-001", "ARG-143-REC-002", "ARG-143-REC-003"))
assert sorted(re.findall(r'id="(ARG-143-0\d\d)"', co1 + co2)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-143-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), NI + "; cifras de Tlaxcala, Zinapécuaro y Guasave, solo por resumen y de días anteriores"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), NI),
 tile(4, "Cargadores", tv(5), NI),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI + "; la bomba molotov de ARG-143-REC-002 es de la ventana de ARGOS 142"),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI + "; ametralladora de Zinapécuaro, solo por resumen y día no fijado"),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: ninguno con cifra en la ventana"),
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
    <div class="map-caption">Ningún aseguramiento contabilizado en la ventana: todas las entidades en gris.</div>
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
    <b>Lectura regional</b>: ninguna región con evento integrable. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: ninguno en la ventana · armas de los agresores sin aseguramiento publicado: Celaya (ARG-143-002), fuera de esta sección.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>boletín federal del 26-oct</b> (acciones del 26, ventana de ARGOS 142; publicado el 27 solo por republicadores, misma fuente): Zinapécuaro, Mich. (3 largas, 1 ametralladora, 8 cargadores, 190 cartuchos, {RES}; otra nota de la SSP con 191 cartuchos y dos vehículos: <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>), Puebla (3 detenidos, 2 largas, 11 cargadores, {RES}), Tlaxcala (8 cateos, 9 detenidos por titulares; 3 largas, {RES}; noche del 25 a la mañana del 26), Benito Juárez, Q. Roo (2 detenidos, 175 kg de mariguana) y Sinaloa (4 camionetas) · <b>Guasave, Sin.</b>: 3 largas, cargadores y cartuchos sin cifra, {RES}, tras el enfrentamiento del 26 con la Marina (ventana de ARGOS 142) · <b>Tlaltenango, Zac.</b>: 2,116 o 2,117 cartuchos y 8 cargadores, por titular «más de 2 mil cartuchos» (Reporteros en Movimiento 2026/10/27); hecho del 23-oct, {RES} · <b>Nuevo Laredo, Tamps.</b> (1 corta, 15 cargadores, 387 cartuchos) y <b>Miguel Alemán, Sin.</b> (4 largas, 20 cargadores, 275 cartuchos): sin fecha en la ruta · <b>Arizpe, Son.</b> (4 detenidos, 5 largas, 2 cortas): agregado del 23-25-oct · <b>Concordia, Sin.</b>: = ARG-141-REC-005.
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
      <tr><td><b>Zacatecas</b><br>Fresnillo</td><td>Homicidio calificado, tentativa de homicidio calificado y daño doloso; hechos del 13-ene y 16-feb-2023 (cols. Plan de Ayala y Arboledas), {RES}; <b>1 sentenciado</b>, Juan Manuel «N», por titular (ECOdiario)</td><td><b>68 años</b>, por titular (ECOdiario, «obtiene FGJEZ sentencia de 68 años»); 68 años 8 meses, juicio oral y límite de cumplimiento de 50 años, {RES}</td><td>FGJ Zacatecas <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · boletín no localizado en el dominio · ruta con año y mes, sin día (NTR 2026/10); «27 de octubre», {RES}: fecha no fijada</td><td>Bajo</td></tr>
      <tr><td><b>Nayarit</b><br>Tepic (El Jicote)</td><td>Portación de armas de uso exclusivo; <b>2 sentenciados</b>, por titular</td><td><b>15 años</b>, por titular (Argonmexico 2026/10/26); «15 años y seis meses», {RES}</td><td>FGR <span class="muted-note">(comunicado 753/26, por medios)</span></td><td><code>PUBLICADA ANTES DE LA VENTANA</code> (26-oct, {RES} del listado de la FGR) · boletín no leído</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Fallo condenatorio por el triple feminicidio, publicado el 9-oct, por <i>slug</i> (La Silla Rota 2026/10/9)</td><td><b>Sin pena</b>: audiencia de individualización el 28-oct a las 17:00, {RES}, <b>posterior al cierre</b></td><td>Tribunal de Enjuiciamiento de Tulancingo <span class="muted-note">(por medios)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín de la PGJEH</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Ramos Arizpe (ejido Paredón)</td><td>Transporte de un kilo de metanfetamina; José «N», {RES}</td><td>«más de 7 años», por titular (El Siglo de Torreón, ruta con año); 7 años 6 meses y 75 UMA, {RES}</td><td>FGR</td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · ninguna ruta con día · boletín no localizado</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGR, comunicados 735/26, 738/26 y 740/26 (21 y 22-oct, {RES}) · FGJ Edomex, 33 años por asalto a transporte (26-oct, por medios) · PGJEH, nueve sentencias por feminicidio (informe, Síntesis 2026/10/23) · FGE Quintana Roo, 140 años (18-oct, {RES}) · FGE Guerrero (15-oct) · FGE Baja California (4 y 11-oct) · FGE Nayarit, 40 años (8-oct) · FGE Durango (última, 2026/09/05). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida: listado de <code>fgr.org.mx</code>, último comunicado indexado 753/26 (26-oct): <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>23 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Son, Sin, Chih, Dgo · NL, Tamps · Jal, Nay, Ags, Gto · CDMX, Edomex, Mor, Tlax, Hgo · Ver, Tab · Oax, Gro, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>23</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>2</b>: Coah · Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>7</b>: BCS · SLP, Zac · Col, Mich · Pue, Qro</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 28-oct 08:28: código <code>000</code> · <b>dominios confirmados en esta edición</b>: <code>fgjtlaxcala.gob.mx</code>, <code>procuraduria.hidalgo.gob.mx</code>, <code>fgenay.gob.mx</code>, <code>fiscalia.sonora.gob.mx</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 22 de 32 con consulta propia por entidad</b> · <b>10 solo por consulta regional amplia</b>: Dgo · Jal, Col, Nay, Ags · Edomex, Mor, Hgo, Qro · Chis · <b>armamento: 16 de 32 por dominio oficial</b> —Sin, Chih · NL, Tamps, Zac · Jal, Nay, Ags, Gto, Mich · CDMX, Pue, Tlax · Ver, Tab · Chis—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · dominio sin páginas: Coah, Oax · <code>NO REVISADA</code> (14): BC, BCS, Son, Dgo · SLP · Col · Edomex, Mor, Hgo, Qro · Gro, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 26-oct</b>: publicadas el 27 solo por republicadores (Milenio, RED113, Tallapolítica, Certeza Diario): misma fuente, sin indexar en <code>gob.mx</code> · <b>acciones del 27-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título (al arrancar la ola y a las 08:40) · Guardia Nacional: SRIV · Semar: por medios · Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 28-OCT 08:28: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Un solo rojo propio</b> —tres cuerpos hallados en Tabasco, con día del hallazgo no fijado— (cálculo propio): riesgo nacional del corte <b>sin incremento acreditado por ataque a autoridades ni homicidio múltiple fijado en la ventana</b>.
      <br><b>2.</b> <b>Violencia operativa</b>: nueve amarillos en siete entidades —siete homicidios dolosos únicos, un cuerpo hallado y una confrontación derivada de una intervención federal— (cálculo propio).
      <br><b>3.</b> <b>Guanajuato</b>: tres de los nueve amarillos y dos de las tres recuperaciones de alto impacto (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: un verde, una detención por un homicidio del 12-oct; ningún aseguramiento de armamento con cifra en la ventana (cálculo propio).
      <br><b>5.</b> <code>{NAP} DE {len(E)} HECHOS SIN HORA FIJADA POR FRAGMENTO Y {NRET} CON CLÁUSULA DE RETIRO; VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 142 SIN NORMALIZAR POR HORA. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. ACÁMBARO: DOS HOMICIDIOS DOBLES EN OCHO DÍAS</b> (cálculo propio, 19 y 26-oct, ambos extremos): ARG-143-REC-003 (Campamento Ferrocarrilero, dentro de una vivienda) y ARG-142-004 (col. Velasco Ibarra); un ataque previo en el Campamento el 12-oct, solo por resumen. Línea: <b>solicitar a la Fiscalía de Guanajuato el cotejo balístico entre ambos y vigilar el Campamento Ferrocarrilero</b> — vínculo no acreditado.
      <br><b>2. CULIACÁN: DIEZ HECHOS CON VÍCTIMAS EN EL ÍNDICE EN DOCE DÍAS</b> (cálculo propio, 16 al 27-oct): ARG-135-001, 135-007, 136-004, 137-009, 138-003, 138-004, 140-004, 141-004, 143-008 y 143-009; dos rojos (dobles) y ocho amarillos; otros tres del 27-oct sin ruta fechada. Línea: <b>solicitar a la Fiscalía de Sinaloa el parte diario de homicidios con hora y colonia</b>.
      <br><b>3. AGRESORES EN MOTOCICLETA CONTRA VÍCTIMAS ÚNICAS EN TRES HECHOS DE DOS CORTES</b> (cálculo propio): ARG-143-003 (Celaya) y ARG-143-007 (Guadalupe), y ARG-142-006 (León); el medio de huida, en los tres, solo por resumen. Línea: <b>solicitar a las fiscalías de Guanajuato y Nuevo León el registro de motocicletas y el cotejo de casquillos</b> — patrón no acreditado.
      <br><b>4. TIEMPOS PROCESALES: CONDENA POR HOMICIDIO 33 MESES DESPUÉS DEL PRIMER HECHO</b> (cálculo propio, 13-ene-2023 a oct-2026, Fresnillo, pendiente de confirmación oficial) y <b>fallo sin pena a los 19 días</b> (cálculo propio, 9 al 28-oct, Tulantepec). Línea: <b>solicitar a la Fiscalía de Zacatecas el boletín de la sentencia y a la PGJEH la pena impuesta</b>.
      <br><b>5. HOMICIDIO SIN DETENIDO: LOS DIEZ HECHOS VIOLENTOS DEL CORTE, SIN DETENIDO PUBLICADO</b> (cálculo propio; entre ellos ARG-143-003, -004, -006, -007, -008, -009 y -010); la única detención de la ventana (ARG-143-011) es por un homicidio del 12-oct. Línea: <b>solicitar a las fiscalías de seis entidades el estado de las carpetas</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>NO REVISADA</code>; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>fgr.org.mx</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b> Los ARG-ID de ediciones previas citados en las conclusiones no se reverificaron en esta edición.
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — HALLAZGO DE CUERPOS Y CONFRONTACIÓN: TABASCO Y GUANAJUATO", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA Y ACCIÓN INSTITUCIONAL: CHIHUAHUA, BAJA CALIFORNIA, NUEVO LEÓN, SINALOA, VERACRUZ Y SAN LUIS POTOSÍ", co2)
 + page("CRIMEN ORGANIZADO (III) — VENTANAS ANTERIORES: ARGOS 142 Y ARGOS 138", co3)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana toca dos fechas de calendario (27 y 28-oct); la plantilla de 142 ya trae 2
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
