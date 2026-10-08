# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 126: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-126.py <plantilla ARGOS 125> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "126", "2026-10-08", "08:56"
CONSULTA = "2026-10-08 09:05"
DUR = "17 h 41 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
BOL = "<code>BOLETÍN FEDERAL DEL 7-OCT, ALCANZADO SOLO POR REPUBLICADORES —LA FECHA DEL BOLETÍN, SOLO POR RESUMEN—: CORROBORACIÓN DÉBIL POR CONSTRUCCIÓN</code>"

# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-126-001", estado="MX-SON", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-07", hora="17:40 (una fuente; otra, 18:00)",
  ent="Sonora", mun="Cajeme (Cócorit)", dia="7-OCT",
  title="SONORA · CAJEME — ATAQUE ARMADO CONTRA JÓVENES EN EL BARRIO EL CONTI DE CÓCORIT: MUERE UN ADOLESCENTE DE QUINCE AÑOS Y TRES QUEDAN HERIDOS",
  hecho="Cócorit · <code>BARRIO EL CONTI, CAMINO CARRETERO Y CUAUHTÉMOC</code> · MIÉRCOLES 7-OCT ~17:40 · dos sujetos en un automóvil disparan contra jóvenes frente a una tienda, junto a un punto señalado por vecinos como de venta de droga · <b>1 muerto, de 15 años</b> · <b>3 heridos</b>, de 21, 18 y 17 años, uno grave (🔴) · casquillos 9 mm · FGJES procesa la escena · <b>cero detenidos</b> · <code>HORA CONTRADICHA: 17:40 FRENTE A 18:00</code> · <code>UNA NOTA SIN FECHA REPORTA CUATRO HERIDOS Y NINGÚN MUERTO: NO FIJADA AL MISMO HECHO</code> · casquillos, edades y hora <code>SOLO POR RESUMEN</code> · <code>UN TITULAR NACIONAL HABLA DE «TRES MENORES HERIDOS»: EDADES CONTRADICHAS</code>",
  panel="Ataque a un grupo de jóvenes: <b>1 muerto de 15 años</b> y <b>3 heridos</b>",
  inst="FGJES <span class=\"muted-note\">(por cita)</span>", nac="Eje Central", conf="★★★☆☆",
  campo="hora, edades y saldo contradichos", I=1, N=1, R=4, A=0,
  fechadas=["Proyecto Puente (2026/10/07)", "Medios Obson (2026/10/07)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cócorit no figura en el índice. Antecedente en el mismo barrio El Conti: ataque del 9-sep ligado por arma a ARG-119-007 (Ciudad Obregón, 10-sep) — otro hecho. NO es ARG-125-009 (Hermosillo, 5-oct). 🔴 por víctimas múltiples: cuatro alcanzados. Precedente contrario: ARG-120-009 (1 muerto y 2 heridos, 🟡). Si se desmiente el muerto, pasa a 🟡"),
 dict(id="ARG-126-002", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-07", hora="no fijada",
  ent="Guanajuato", mun="Salamanca (col. San Isidro)", dia="7-OCT",
  title="GUANAJUATO · SALAMANCA — ASESINADO A BALAZOS UN HOMBRE DENTRO DE UN DOMICILIO DE LA COLONIA SAN ISIDRO",
  hecho="Salamanca · <code>COLONIA SAN ISIDRO</code> · publicado MIÉRCOLES 7-OCT · <b>1 hombre muerto</b> a balazos dentro de un domicilio; sin signos vitales a la llegada de paramédicos (🟡) · <b>cero detenidos</b> · identidad no publicada · " + FR + " · <code>FUENTE ÚNICA</code>",
  panel="<b>1 hombre asesinado</b> a balazos en un domicilio",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="fuente única; día y hora del hecho", I=0, N=0, R=1, A=0,
  fechadas=["Periódico Correo (2026/oct/07)"], estatus="Pendiente de corroboración", arm=None,
  desl="Salamanca figura en el índice como ARG-125-044 (policía municipal, 25-sep): otro hecho. 🟡 por homicidio doloso único sin agravantes de la lista roja"),
 dict(id="ARG-126-003", estado="MX-HID", region="Centro", color="verde", impacto="mediano", fecha="2026-10-07", hora="no fijada",
  ent="Hidalgo", mun="Tlaxcoapan", dia="7-OCT",
  title="HIDALGO · TLAXCOAPAN — CATEO EN LA COLONIA CENTRO: CUATRO FUSILES DE ASALTO, TRES ARMAS CORTAS Y 279 DOSIS",
  hecho="Tlaxcoapan · <code>COLONIA CENTRO</code> · cateo publicado MIÉRCOLES 7-OCT · <b>SSPH con Defensa y PGJEH</b> · <b>4 fusiles de asalto</b> y <b>3 armas cortas</b> —descritos por la SSPH como de uso exclusivo de las Fuerzas Armadas— · <b>11 cargadores</b> · <b>47 cartuchos</b> · 133 dosis de hierba y 146 de granulado tipo cristal · 4 chalecos balísticos, 2 cascos, 1 báscula (🟢) · <b>cero detenidos</b> publicados: lo asegurado, a disposición del MP · " + FR + " · desglose <code>SOLO POR RESUMEN</code>",
  panel="Cateo: <b>4 fusiles</b>, <b>3 cortas</b>, 11 cargadores, 47 cartuchos y <b>279 dosis</b>; sin detenidos",
  inst="SSPH <span class=\"muted-note\">(por cita)</span>", nac="Milenio · La Silla Rota", conf="★★★☆☆",
  campo="desglose de armas por resumen; sin detenidos publicados", I=1, N=2, R=5, A=0,
  fechadas=["Zunoticia (2026/10/07)", "La Silla Rota (2026/10/8)"], estatus="Parcialmente corroborado", arm="ARG-126-ARM-001",
  desl="Tlaxcoapan no figura en el índice. Primer hecho propio de Hidalgo tras su NO REVISADA de ARGOS 125"),
 dict(id="ARG-126-004", estado="MX-SIN", region="Noroeste", color="verde", impacto="grande", fecha="2026-10-07", hora="no fijada",
  ent="Sinaloa", mun="Concordia (Pánuco)", dia="7-OCT",
  title="SINALOA · CONCORDIA — OCHENTA Y DOS ARTEFACTOS EXPLOSIVOS IMPROVISADOS, UN ARMA LARGA Y 670 CARTUCHOS EN PÁNUCO",
  hecho="Pánuco, Concordia · acciones del MIÉRCOLES 7-OCT · <b>Ejército y Policía Estatal</b> · <b>82 AEI</b> · <b>1 arma larga</b> · <b>5 cargadores</b> · <b>670 cartuchos</b> · 1 chaleco, 2 placas balísticas, 1 vehículo (🟢) · <b>cero detenidos</b> · <code>LUGAR DEL HALLAZGO NO PUBLICADO</code> · <code>TIPO DE ARTEFACTO NO PUBLICADO</code> · los <b>82 AEI</b>, por titular; arma, cargadores y cartuchos <code>SOLO POR RESUMEN</code> · " + FR + " · " + BOL,
  panel="<b>82 AEI</b>, 1 arma larga, 5 cargadores y <b>670 cartuchos</b>",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="arma, cargadores y cartuchos solo por resumen; lugar no publicado", I=1, N=0, R=2, A=0,
  fechadas=["Los Noticieristas (2026/10, solo mes)"], estatus="Parcialmente corroborado", arm="ARG-126-ARM-002",
  desl="Concordia figura en el índice (ARG-95-005, ARG-106-003 y otros): otros hechos. Pánuco no figura. NO es ARG-111-003 (49 AEI destruidos por SEMAR, 28-ago) ni ARG-124-003 (75 AEI tipo mina, 2 AK-47, 600 cartuchos, 2 detenidos, 22-sep, Ejército y Policía Estatal): mismo municipio, otras fechas y cifras"),
 dict(id="ARG-126-005", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-07", hora="no fijada",
  ent="Sinaloa", mun="El Rosario", dia="7-OCT",
  title="SINALOA · EL ROSARIO — 1,198 CARTUCHOS, TRES CARGADORES Y DOCE KILOS DE METANFETAMINA",
  hecho="El Rosario · <code>COLONIA LUIS DONALDO COLOSIO Y ANONAL</code> · acciones del MIÉRCOLES 7-OCT · <b>Ejército</b> · <b>1,198 cartuchos</b> · <b>3 cargadores</b> · 12 kg de metanfetamina, 2,867 dosis de cocaína y 1 kg de marihuana (🟢) · <b>sin armas ni detenidos publicados</b> · los 12 kg, por titular; cartuchos y cargadores <code>SOLO POR RESUMEN</code> · " + FR + " · " + BOL + "",
  panel="<b>1,198 cartuchos</b>, 3 cargadores y <b>12 kg de metanfetamina</b>",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="cartuchos y cargadores solo por resumen; dos republicadores del mismo boletín", I=1, N=0, R=2, A=0,
  fechadas=["Los Noticieristas (2026/10, solo mes)"], estatus="Pendiente de corroboración", arm="ARG-126-ARM-003",
  desl="NO es ARG-125-010 (campamento con 42 AEI y 15 drones, 5-oct): otra fecha, otra colonia, otro desglose. El Rosario figura en el índice en otros cortes"),
 dict(id="ARG-126-006", estado="MX-NLE", region="Noreste", color="verde", impacto="pequeno", fecha="2026-10-07", hora="no fijada",
  ent="Nuevo León", mun="Apodaca", dia="7-OCT",
  title="NUEVO LEÓN · APODACA — CATEO DE LA FGR Y LA SSPC: DOS DETENIDOS, UN ARMA CORTA Y DOS KILOS DE METANFETAMINA",
  hecho="Apodaca · cateo en un inmueble, acciones del MIÉRCOLES 7-OCT · <b>FGR y SSPC</b> · <b>2 detenidos</b> · <b>1 arma corta</b> y 1 réplica (no se cuenta) · <b>2 cargadores</b> · <b>13 cartuchos</b> · 2 kg de metanfetamina, medicamento controlado, efectivo sin cifra, 1 vehículo, 4 celulares (🟢) · cifras <code>SOLO POR RESUMEN</code> · " + FR + " · " + BOL,
  panel="<b>2 detenidos</b>, 1 arma corta, 13 cartuchos y <b>2 kg de metanfetamina</b>",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="un solo republicador, sin fecha en la ruta", I=1, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm="ARG-126-ARM-004",
  desl="Apodaca no figura en el índice"),
 dict(id="ARG-126-007", estado="MX-CHH", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-07", hora="no fijada",
  ent="Chihuahua", mun="Ciudad Juárez", dia="7-OCT",
  title="CHIHUAHUA · CIUDAD JUÁREZ — VEINTISÉIS PERSONAS EXTRANJERAS RESCATADAS, DOS DE ELLAS MENORES; UN DETENIDO",
  hecho="Ciudad Juárez · acciones del MIÉRCOLES 7-OCT · <b>SSPC y Guardia Nacional</b> · <b>1 hombre detenido</b> · <b>26 personas de nacionalidad extranjera rescatadas</b>, 2 menores (🟢) · sin armamento publicado · nacionalidades no publicadas · cifras <code>SOLO POR RESUMEN</code> · " + FR + " · " + BOL,
  panel="<b>26 extranjeros rescatados</b>, 2 menores; <b>1 detenido</b>",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="un solo republicador, sin fecha en la ruta", I=1, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Ciudad Juárez figura en el índice en otros cortes: otros hechos. NO es la balacera de Infonavit Casas Grandes (ARG-126-REC-003). NO es Balleza (ARG-126-REC-004)"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-126-REC-001", estado="MX-PUE", region="Centro", fecha="2026-10-07", hora="~06:00", orig="ARGOS 125", col_orig="amarillo",
  ent="Puebla", mun="Eloxochitlán (Ojo de Agua)", dia="7-OCT 06:00",
  title="PUEBLA · ELOXOCHITLÁN — UN COMANDO DE UNOS VEINTE HOMBRES EN OCHO CAMIONETAS IRRUMPE EN UNA CASA DE OJO DE AGUA Y MATA A UN HOMBRE",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · Ojo de Agua · MIÉRCOLES 7-OCT ~06:00 · <b>~20 hombres armados en 8 camionetas</b> irrumpen en un domicilio · <b>1 hombre de 45 años muerto</b> (🟡 en su ventana) · casquillos de arma larga sin cifra · FGE Puebla investiga · <b>cero detenidos</b> · <code>NÚMERO DE ATACANTES Y VEHÍCULOS, PRELIMINAR</code> · <code>COORDINACIÓN CRIMINAL NO ACREDITADA: NO SUBE A ROJO</code>",
  panel="Comando de ~20 en 8 camionetas: <b>1 muerto</b>", inst="FGE Puebla <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★☆☆☆", campo="sin fuente nacional; cifras de atacantes preliminares", I=1, N=0, R=5, A=0,
  fechadas=["Síntesis (2026/10/07)", "Reto Diario (2026/10/07)"], desl="Eloxochitlán no figura en el índice. NO es la colonia Ojo de Agua de San Martín Texmelucan (ARG-119-006)"),
 dict(id="ARG-126-REC-002", estado="MX-MIC", region="Occidente", fecha="2026-10-07", hora="madrugada", orig="ARGOS 125", col_orig="amarillo",
  ent="Michoacán", mun="Tarímbaro", dia="7-OCT MADRUGADA",
  title="MICHOACÁN · TARÍMBARO — DISPARAN CONTRA UNA PATRULLA MUNICIPAL EN LA CARRETERA MORELIA-SALAMANCA; SIN HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · inmediaciones de San Agustín del Maíz, carretera Morelia–Salamanca · madrugada del MIÉRCOLES 7-OCT · disparos contra una unidad de la <b>Policía Municipal</b> desde una Toyota Tacoma · <b>sin policías heridos</b> · Guardia Civil en apoyo · <b>cero detenidos</b> (🟡 en su ventana) · <code>QUIÉN INICIÓ, CONTRADICHO</code>: una versión, ataque a la unidad; otra, persecución iniciada por los agentes · color de la camioneta contradicho",
  panel="Disparos contra una <b>patrulla municipal</b>; sin heridos", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="quién inició la agresión", I=0, N=0, R=8, A=0,
  fechadas=["Red Michoacán (2026/10/07)", "Changoonga (2026/10/07)", "Media News (2026/10/07)"], desl="Tarímbaro no figura en el índice. 🟡 y no 🔴 porque quién inició no es determinable"),
 dict(id="ARG-126-REC-003", estado="MX-CHH", region="Noroeste", fecha="2026-10-07", hora="madrugada", orig="ARGOS 125", col_orig="amarillo",
  ent="Chihuahua", mun="Ciudad Juárez (Infonavit Casas Grandes)", dia="7-OCT MADRUGADA",
  title="CHIHUAHUA · CIUDAD JUÁREZ — BALACERA ENTRE PRESUNTOS SECUESTRADORES EN CASAS GRANDES: UN MUERTO, DOS HERIDOS DETENIDOS Y UNA MUJER LIBERADA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>INFONAVIT CASAS GRANDES, F. J. ALEGRE Y PEDRO MEOQUI</code> · madrugada del MIÉRCOLES 7-OCT · <b>1 muerto</b> · <b>2 heridos</b> —3 según otro medio— · <code>DETENIDOS CONTRADICHO: UNA VERSIÓN TRASLADA A LOS HERIDOS COMO DETENIDOS; OTRA NO REPORTA CAPTORES DETENIDOS</code> · <b>mujer liberada</b>, atada, que declaró llevar meses retenida —34 años y casi seis meses, <code>SOLO POR RESUMEN</code>— (🟡 en su ventana) · SSPM y Fiscalía de Distrito Zona Norte, que aseguró la vivienda · <code>MÓVIL CONTRADICHO: REPARTO DE UN RESCATE FRENTE A DEUDA DE DROGAS</code>",
  panel="Balacera entre presuntos secuestradores: <b>1 muerto</b>, 2 heridos, <b>1 mujer liberada</b>", inst="SSPM · FGE <span class=\"muted-note\">(por cita)</span>", nac="Infobae",
  conf="★★★☆☆", campo="móvil, heridos y detenidos contradichos", I=1, N=1, R=5, A=0,
  fechadas=["Infobae (2026/10/07)", "El Diario de Juárez (2026/oct/07, dos notas)", "El Diario de Chihuahua (2026/oct/07)"], desl="NO es ARG-126-007 (26 extranjeros rescatados, SSPC y GN) ni ARG-125-030 (colonia Casas Grandes, 30-sep, 3 detenidos y cocaína). 🟡: confrontación focalizada entre particulares; la liberación es parte del mismo hecho"),
 dict(id="ARG-126-REC-004", estado="MX-CHH", region="Noroeste", fecha="2026-10-07", hora="madrugada o mañana (otra versión: noche del 6-oct)", orig="ARGOS 125", col_orig="rojo",
  ent="Chihuahua", mun="Balleza (Pinalejo)", dia="7-OCT MAÑANA",
  title="CHIHUAHUA · BALLEZA — CIVILES ARMADOS ATACAN A MILITARES EN RECORRIDO EN PINALEJO: DOS AGRESORES ABATIDOS; TRES ARMAS LARGAS Y 87 KILOS DE MARIHUANA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>PINALEJO, JUNTO A UNA ESCUELA</code> · madrugada o mañana del MIÉRCOLES 7-OCT —otra versión: noche del martes 6— · militares en recorrido de vigilancia localizan una Tahoe abandonada; llegan varios vehículos cuyos ocupantes <b>disparan contra el Ejército</b> · <b>2 civiles armados abatidos</b> · <b>sin militares heridos</b> publicados · <b>3 armas largas</b> · <b>11 cargadores</b> · <b>231 cartuchos</b> —230 útiles según otros tres medios— · 87 kg de marihuana · <b>5 vehículos</b> —2 según otra versión— (🔴 en su ventana) · FGE Chihuahua · el aseguramiento figura en el boletín federal del 7-oct · quién inició: titular de Vanguardia, «Ataque contra militares termina en balacera» · desglose <code>SOLO POR RESUMEN</code>",
  panel="Civiles armados atacan a <b>militares en recorrido</b>: <b>2 agresores abatidos</b>, 3 armas largas", inst="FGE Chihuahua <span class=\"muted-note\">(por cita)</span> · Gabinete <span class=\"muted-note\">(republicador)</span>", nac="El Universal · Vanguardia",
  conf="★★★☆☆", campo="hora del hecho y desglose contradichos", I=2, N=2, R=4, A=0,
  fechadas=["El Diario (2026/oct/07)"], desl="Balleza y Pinalejo no figuran en el índice. 🔴 por quién inicia: agresión a personal en patrullaje; el número de abatidos no mueve el color."),
 dict(id="ARG-126-REC-005", estado="MX-MIC", region="Occidente", fecha="2026-10-06", hora="tarde", orig="ARGOS 125", col_orig="rojo",
  ent="Michoacán", mun="Salvador Escalante (El Querendal)", dia="6-OCT",
  title="MICHOACÁN · SALVADOR ESCALANTE — ATAQUE ARMADO EN UN ACOPIO DE AGUACATE DE EL QUERENDAL: TRES MUERTOS, UNO DE QUINCE AÑOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>EL QUERENDAL</code> · tarde del MARTES 6-OCT · hombres armados bajan de una camioneta, entran a un acopio de aguacate y disparan contra los trabajadores · <b>3 muertos</b>: 2 en el lugar y <b>1 adolescente de 15 años</b> en el hospital de Pátzcuaro (🔴 en su ventana) · FGE Michoacán abre carpeta · Guardia Civil despliega operativo · <b>cero detenidos</b> · <code>NOMBRES Y EDADES DE LOS ADULTOS, CONTRADICHOS</code> · vehículo con placas de Jalisco <code>SOLO POR RESUMEN</code>",
  panel="Ataque en un <b>acopio de aguacate</b>: <b>3 muertos</b>, uno de 15 años", inst="FGE Michoacán <span class=\"muted-note\">(por cita)</span>", nac="Excélsior · Meganoticias",
  conf="★★★☆☆", campo="identidad de las víctimas", I=1, N=2, R=6, A=0,
  fechadas=["Red Michoacán (2026/10/06)", "Grupo Marmor (2026/10/06)"], desl="Salvador Escalante figura en el índice como ARG-109-001 (agosto): otro hecho"),
 dict(id="ARG-126-REC-006", estado="MX-SIN", region="Noroeste", fecha="2026-10-06", hora="no fijada", orig="ARGOS 125", col_orig="verde",
  ent="Sinaloa", mun="Culiacán (Parque Alamedas)", dia="6-OCT",
  title="SINALOA · CULIACÁN — TRES ARMAS LARGAS Y MÁS DE QUINIENTOS CARTUCHOS EN UN VEHÍCULO DE PARQUE ALAMEDAS, TRAS UNA LLAMADA AL 089",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>PARQUE ALAMEDAS</code> · MARTES 6-OCT · GOES / SSP Sinaloa, material a disposición de la FGR · llamada al 089 por una privación de la libertad: <b>nadie en el inmueble</b> · en un vehículo, <b>3 armas largas</b>, <b>más de 500 cartuchos</b>, cargadores y un cubo de ponchallantas (🟢 en su ventana) · <code>CARGADORES Y CARTUCHOS: CANTIDAD NO DETERMINADA</code> —el desglose 1 AK-47, 2 AR-15, 16 cargadores y 555 cartuchos solo existe en el resumen del buscador, segunda edición sin respaldo citable— · <b>cero detenidos</b> · <code>UN TITULAR SIN FECHA HABLA DE TRES CIVILES DETENIDOS EN CULIACÁN: NO ATADO A ESTE HECHO</code>",
  panel="<b>3 armas largas</b> y <b>más de 500 cartuchos</b> en un vehículo", inst="SSP Sinaloa <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="cargadores y cartuchos sin cifra citable", I=1, N=0, R=4, A=0,
  fechadas=["Línea Directa (2026-10-06)"], desl="Parque Alamedas no figura en el índice. NO es ARG-126-REC-011 (Corolla del Centro, 2-oct) ni ARG-125-006 (Carboneras, 6-oct, 819 cartuchos). Fecha del hecho fijada por la de publicación: no posterior al 6-oct"),
 dict(id="ARG-126-REC-007", estado="MX-OAX", region="Sureste", fecha="2026-10-05", hora="~20:00", orig="ARGOS 125", col_orig="rojo",
  ent="Oaxaca", mun="Santa María Mixtequilla", dia="5-OCT 20:00",
  title="OAXACA · SANTA MARÍA MIXTEQUILLA — HOMBRES ARMADOS BALEAN EL PALACIO MUNICIPAL Y UNA PATRULLA E INCENDIAN UNA MOTOCICLETA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · cabecera municipal, Istmo de Tehuantepec · LUNES 5-OCT ~20:00 · hombres encapuchados, algunos con armas largas, disparan contra la <b>fachada del palacio municipal</b> y contra una <b>patrulla de la Policía Municipal</b>; incendian una motocicleta (🔴 en su ventana) · <b>sin heridos</b> · <b>cero detenidos</b> · la SSPC de Oaxaca envía la Fuerza Especial <b>Binnizá</b> · <code>UNA FUENTE FECHA EL 4-OCT; EL 5-OCT FUE LUNES</code>",
  panel="Ataque a balazos contra el <b>palacio municipal</b> y una <b>patrulla</b>; sin heridos", inst="SSPC Oaxaca <span class=\"muted-note\">(por cita)</span>", nac="Infobae · El Universal",
  conf="★★★☆☆", campo="número de atacantes y fecha (4 o 5-oct)", I=1, N=2, R=5, A=0,
  fechadas=["Infobae (2026/10/06)"], desl="Mixtequilla no figura en el índice. 🔴: el grupo criminal inicia la agresión contra autoridades"),
 dict(id="ARG-126-REC-008", estado="MX-GRO", region="Sureste", fecha="2026-10-05", hora="mañana", orig="ARGOS 125", col_orig="rojo",
  ent="Guerrero", mun="Zihuatanejo (sierra, San Ignacio)", dia="5-OCT EN ADELANTE",
  title="GUERRERO · ZIHUATANEJO — ATAQUES A BALAZOS Y CON DRONES EXPLOSIVOS EN LA SIERRA: UN MUERTO, UN HERIDO Y CINCO COMUNIDADES ABANDONADAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>SAN IGNACIO, SIERRA PONIENTE</code> · desde la mañana del LUNES 5-OCT · civiles armados atacan a pobladores a balazos y con <b>drones explosivos</b> · <b>1 muerto</b> · <b>1 herido</b> · casquillos <b>cal. .50</b> y una camioneta blindada asegurada (🔴 en su ventana) · <b>desplazamiento</b>: ~150 personas de 5 comunidades según dos titulares; ≥30 familias según Meganoticias, que lo atribuye a la alcaldesa · Fuerzas Armadas y policía municipal en la zona · un desplazado sitúa el cobro de cuota por kilo de res desde 2021 (<code>SOLO POR RESUMEN</code>) · <code>CIFRA DE DESPLAZADOS CONTRADICHA</code> · <code>DRONES ARMADOS, POR TESTIMONIOS Y MEDIOS; LA AUTORIDAD REPORTA SU PRESENCIA</code>",
  panel="Ataques con <b>drones explosivos</b>: <b>1 muerto</b>, 1 herido y <b>~150 desplazados</b>", inst="Ayuntamiento <span class=\"muted-note\">(por cita)</span>", nac="Infobae · Meganoticias",
  conf="★★★☆☆", campo="cifra de desplazados y uso de drones armados", I=1, N=2, R=3, A=0,
  fechadas=["Infobae (2026/10/07)"], desl="Zihuatanejo figura en el índice (ARG-99-005, cocaína en el mar): otro hecho. NO es San Ignacio, Sinaloa (explosivos para dron, 28-sep)"),
 dict(id="ARG-126-REC-009", estado="MX-YUC", region="Sureste", fecha="2026-10-03", hora="no fijada", orig="ARGOS 125", col_orig="verde",
  ent="Yucatán", mun="Mérida", dia="3-OCT",
  title="YUCATÁN · MÉRIDA — CUATRO DETENIDOS POR EL ATENTADO DE MONTES DE AMÉ",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · SÁBADO 3-OCT · <b>SSP Yucatán</b> · <b>4 detenidos</b> —2 hombres y 2 mujeres— por el ataque del 2-oct (🟢 en su ventana) · participación no acreditada judicialmente · cifra <code>SOLO POR TITULAR</code>",
  panel="<b>4 detenidos</b>; vínculo con el atentado del 2-oct por titular único", inst="SSP Yucatán <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★☆☆☆", campo="cifra de detenidos solo por titular", I=1, N=0, R=1, A=0,
  fechadas=["Noticaribe (2026/10/03)"], desl="Un delito y su detención son dos eventos: el ataque es ARG-126-REC-010"),
 dict(id="ARG-126-REC-010", estado="MX-YUC", region="Sureste", fecha="2026-10-02", hora="~11:00", orig="ARGOS 125", col_orig="amarillo",
  ent="Yucatán", mun="Mérida (Montes de Amé)", dia="2-OCT",
  title="YUCATÁN · MÉRIDA — ATENTADO A BALAZOS EN MONTES DE AMÉ CONTRA «EL MARCE», SEÑALADO COMO OBJETIVO PRIORITARIO DE QUINTANA ROO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>MONTES DE AMÉ, NORTE DE MÉRIDA</code> · VIERNES 2-OCT ~11:00 · sicarios en motocicleta disparan contra <b>José Marcelino Chan Tun, «El Marce»</b>, a quien los medios ligan a Los Chapitos · <b>1 herido</b>, estable (🟡 en su ventana) · <code>VÍNCULO CRIMINAL, SOLO PERIODÍSTICO</code> · hora <code>SOLO POR RESUMEN</code>",
  panel="Atentado contra <b>«El Marce»</b>: <b>1 herido</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Proceso · La Silla Rota",
  conf="★★★☆☆", campo="sin fuente institucional; vínculo criminal periodístico", I=0, N=2, R=1, A=0,
  fechadas=["Diario de Yucatán (2026/10/02)", "Proceso (2026/10/2)", "La Silla Rota (2026/10/2)"], desl="Mérida y Montes de Amé no figuran en el índice. 🟡: homicidio en grado de tentativa, víctima única"),
 dict(id="ARG-126-REC-011", estado="MX-SIN", region="Noroeste", fecha="2026-10-02", hora="15:30-16:00", orig="ARGOS 125", col_orig="verde",
  ent="Sinaloa", mun="Culiacán (Centro)", dia="2-OCT",
  title="SINALOA · CULIACÁN — UN COROLLA ROBADO, ABANDONADO EN EL CENTRO CON DOS FUSILES, UNO CON LANZAGRANADAS, Y UNA GRANADA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 125</code> · <code>ÁLVARO OBREGÓN Y RAFAEL BUELNA</code> · VIERNES 2-OCT, tarde · vehículo con reporte de robo desde mayo · <b>2 fusiles</b>, uno con <b>lanzagranadas</b> acoplado · <b>1 granada</b>, entregada a la 9.ª Zona Militar · ponchallantas (🟢 en su ventana) · desglose anunciado por la SSPyTM el MARTES 6-OCT · <b>cero detenidos</b> · <code>AUTORIDAD A CARGO CONTRADICHA: MP FEDERAL FRENTE A FGE</code>",
  panel="Vehículo robado con <b>2 fusiles</b> —uno con lanzagranadas— y <b>1 granada</b>", inst="SSPyTM <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="autoridad a cargo", I=1, N=0, R=2, A=0,
  fechadas=["Línea Directa (2026-10-02 y 2026-10-06)"], desl="NO es ARG-126-REC-006 (Parque Alamedas, 6-oct): otra fecha, otras armas, otra corporación"),
 dict(id="ARG-126-REC-012", estado="MX-GUA", region="Occidente", fecha="2026-09-21", hora="no fijada", orig="ARGOS 123 (frontera 122)", col_orig="rojo",
  ent="Guanajuato", mun="León (Arroyo Hondo)", dia="21-SEP",
  title="GUANAJUATO · LEÓN — RESTOS DE CINCO PERSONAS EN UN POZO DE ARROYO HONDO, TRAS EL HALLAZGO DE UNA MUJER DECAPITADA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 123</code> · <code>ARROYO HONDO, TIMOTEO LOZANO Y MONTE CARMELO</code> · LUNES 21-SEP · peritos de la FGE Guanajuato, con Policía Municipal, GN y Ejército, recuperan de un pozo <b>restos de 5 personas</b>, desmembrados y en bolsas (🔴 en su ventana) · la búsqueda partió de una <b>mujer decapitada</b> hallada el domingo 20-sep · <code>CIFRA CONTRADICHA: 5 FRENTE A 6 —CON O SIN LA MUJER—; UNA VERSIÓN DA 4 EN EL POZO</code> · identidades no publicadas · " + FR.replace("HORA NO FIJADA", "ENTRE ARGOS 122 Y 123"),
  panel="<b>Pozo con restos de 5 personas</b>", inst="FGE Guanajuato <span class=\"muted-note\">(por cita)</span>", nac="El Universal · Uno TV",
  conf="★★★☆☆", campo="número de cuerpos y hora del hallazgo", I=1, N=2, R=5, A=0,
  fechadas=["Noticieros en Línea (2026/sep/21)", "Diario de Yucatán (2026/09/22)"], desl="León figura en el índice (ARG-100-002 y otros): otros hechos."),
 dict(id="ARG-126-REC-013", estado="MX-GRO", region="Sureste", fecha="2026-08-21", hora="noche", orig="ARGOS 105", col_orig="rojo",
  ent="Guerrero", mun="Tlapehuala", dia="21-AGO",
  title="GUERRERO · TLAPEHUALA — ASESINADA A TIROS LA DIRIGENTE MUNICIPAL DE MOVIMIENTO CIUDADANO, NADIA VEHURINI MATADAMA DÍAZ",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 105</code> · noche del VIERNES 21-AGO · <b>Nadia Vehurini Matadama Díaz</b>, dirigente municipal de MC, <b>asesinada a tiros</b> (🔴 en su ventana) · al menos 6 casquillos · FGE Guerrero abre carpeta · <b>cero detenidos</b> · <code>FECHA CONTRADICHA: 21 O 22-AGO, AMBAS EN LA MISMA VENTANA</code> · <code>LUGAR CONTRADICHO: TLAPEHUALA FRENTE A CHILPANCINGO</code>",
  panel="Asesinada la <b>dirigente municipal de MC</b>", inst="FGE Guerrero <span class=\"muted-note\">(por cita)</span>", nac="ADN40 · Infobae",
  conf="★★★☆☆", campo="lugar del hecho", I=1, N=3, R=0, A=0,
  fechadas=["ADN40 (2026-08-23)", "ABC Noticias (2026/8/23)", "Infobae (2026/08/24)"], desl="Tlapehuala no figura en el índice. Patrón de dirigentes políticos: con ARG-124-002 (Coatzacoalcos), ARG-123-REC-001 (Tetecala, dirigente municipal del PRI) y ARG-108-REC-001 (Mazatepec); 🔴 por precedente de la serie — coincidencia registrada, vinculación no afirmada"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-126-ARM-001", ficha="ARG-126-003", estado="MX-HID", region="Centro", ent="Hidalgo", mun="Tlaxcoapan", c=[3,4,0,0,47,11,0,0,0,0], corp="SSPH + Defensa + PGJEH", conf="Medio", nota="«uso exclusivo», según la SSPH", fuentes=["Zunoticia (2026/10/07)", "La Silla Rota (2026/10/8)"]),
 dict(id="ARG-126-ARM-002", ficha="ARG-126-004", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Concordia (Pánuco)", c=[0,1,0,0,670,5,0,82,0,0], corp="Ejército + Policía Estatal", conf="Bajo", nota="tipo de AEI no publicado", fuentes=["Los Noticieristas (2026/10)"]),
 dict(id="ARG-126-ARM-003", ficha="ARG-126-005", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="El Rosario", c=[0,0,0,0,1198,3,0,0,0,0], corp="Ejército", conf="Bajo", nota="un solo republicador", fuentes=[]),
 dict(id="ARG-126-ARM-004", ficha="ARG-126-006", estado="MX-NLE", region="Noreste", ent="Nuevo León", mun="Apodaca", c=[1,0,0,0,13,2,0,0,0,2], corp="FGR + SSPC", conf="Bajo", nota="1 réplica, no se cuenta", fuentes=[]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [4, 5, 0, 0, 1928, 21, 0, 82, 0, 2], TOT
assert cnt == {"rojo": 1, "amarillo": 1, "verde": 5}, cnt

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else "sin fila — no hubo armamento asegurado")
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
        · <b>Hecho</b>: {e["fecha"]} · <b>Hora</b>: {e["hora"]} · <b>Consulta</b>: {CONSULTA} ·
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
            "hecho": strip(e["hecho"]), "fuentes": e["fechadas"] or ["Gabinete de Seguridad, boletín del 7-oct (republicador)"],
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"]}

def arm_json(a):
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": "verde", "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"] or ["Gabinete de Seguridad, boletín del 7-oct (republicador)"], "confianza": a["conf"], "fecha": "2026-10-07", "hora": "no fijada"}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 125 — Reporte Nacional de Seguridad — 2026-10-07</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <div class="map-caption">Color = evento de mayor impacto por entidad. Pase el cursor sobre un estado.</div>
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
      <b>1. IDENTIFIQUE A LOS DOS ABATIDOS DE BALLEZA</b> (ARG-126-REC-004). Coteje por serie las tres armas largas y los cinco vehículos
      contra carpetas abiertas en la sierra Tarahumara.
      <br><b>2. REFUERCE LAS SEDES MUNICIPALES DEL ISTMO</b> (ARG-126-REC-007). Vigilancia de palacios y patrullas de Mixtequilla y
      municipios vecinos mientras no haya detenidos.
      <br><b>3. EXPLOTE EL TESTIMONIO DE CASAS GRANDES</b> (ARG-126-REC-003). Entrevista a la mujer liberada, cateos anunciados y cruce
      con denuncias de secuestro de larga duración en Ciudad Juárez.
      <br><b>4. IDENTIFIQUE LA RED DE LOS 26 EXTRANJEROS</b> (ARG-126-007). Nacionalidades, punto de ingreso y destino previsto, con el
      Instituto Nacional de Migración.
      <br><b>5. EXIJA EL CUMPLIMIENTO DEL AMPARO 412/2026</b> para los siete desaparecidos de El Balcón (ARG-125-051): plan de búsqueda,
      registros de Semefo e informes de seguridad.
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>7-oct 15:15 → 8-oct 08:56 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,40 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: del más reciente al más antiguo.</b>
    <br><code>SEIS DE LOS SIETE HECHOS PROPIOS LLEVAN FRONTERA DE VENTANA — HORA NO FIJADA: LOS TOTALES NO SON COMPARABLES CON LOS DE NINGUNA EDICIÓN ANTERIOR.</code>
    <br><code>LAS {len(R)} RECUPERACIONES DEL FINAL PERTENECEN A VENTANAS ANTERIORES Y QUEDAN FUERA DEL SEMÁFORO, DEL MAPA, DEL RADAR Y DE TODOS LOS TOTALES.</code>
    <br><b>Toque un ARG-ID para ir a su ficha</b>, donde están las fuentes, el nivel de confianza y los deslindes.
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
    <code>NINGUNA AUTORIDAD PUBLICÓ UN AGREGADO NACIONAL DE ESTA VENTANA.</code> <b>Tres de las cuatro filas de armamento proceden del boletín federal del 7-oct</b>, alcanzado solo por republicadores.
  </p>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Armas cortas</th><th>Armas largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{TOT[2]}</b></td><td><b>{TOT[3]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Total de armas integradas: {ARMAS}</b> —{TOT[0]} cortas y {TOT[1]} largas, <b>cálculo propio</b>—. <b>Cartuchos y cargadores nunca se suman entre sí.</b>
    <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento</b>; fuera de ese conteo, <b>1 detenido</b> en Ciudad Juárez (ARG-126-007). <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios: 2</b> —1 en el rojo de Cócorit y 1 en el amarillo de Salamanca—, más <b>3 heridos</b> en Cócorit —<b>cálculo propio</b>—.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:])
rec1 = "\n".join(ficha(r, True) for r in R[:7])
rec2 = "\n".join(ficha(r, True) for r in R[7:])

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA CON CALIBRE NI SERIE PUBLICADO</code>"),
 tile(1, "Armas largas", TOT[1], "<code>CUATRO DESCRITOS COMO DE USO EXCLUSIVO</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>1,868 DE ELLOS, SOLO POR RESUMEN</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NUNCA SE SUMAN CON LOS CARTUCHOS</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<b>un solo evento</b> · <code>TIPO DE ARTEFACTO NO PUBLICADO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR PUBLICADO POR SEPARADO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGUNA PIEZA CAL. .50 NI DRON ARMADO ASEGURADO EN HECHO PROPIO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>{len(ARM)} filas de armamento de {len(ARM)} hechos</b> en <b>{len(ENT_ARM)} entidades</b>: <b>todos con cifra</b>, ninguno cualitativo. <b>Totales por categoría: cálculo propio.</b>
    <code>TRES FILAS PROCEDEN DEL BOLETÍN FEDERAL DEL 7-OCT, CON FRONTERA DE VENTANA.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Verde = aseguramiento sin enfrentamiento · amarillo = derivado de enfrentamiento. La sola presencia de armas no vuelve roja a una entidad.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    cells = "".join(f"<td>{('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for v in c[:9])
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    return f'      <tr id="{a["id"]}"><td><a href="#{a["ficha"]}"><code>{a["id"]}</code></a></td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>2026-10-07</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'
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
    <b>Lectura regional</b> —4 filas, <b>cálculo propio</b>—: <b>Noroeste 2</b> · <b>Noreste 1</b> · <b>Occidente 0</b> · <b>Centro 1</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    <code>SINALOA APORTA LOS 82 AEI Y 1,868 DE LOS 1,928 CARTUCHOS, CÁLCULO PROPIO.</code> El armamento de las recuperaciones —Balleza y Culiacán, Parque Alamedas y Centro— va en su ficha y <b>no entra en esta tabla</b>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA CON BOLETÍN DEL DOMINIO OFICIAL EN LA VENTANA</code> · dos publicadas por medios el 7-oct, abajo</span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub"><b>5 personas</b> en dos candidatas con pena publicada quedan en <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto ordenado y publicado</b> en la ventana</span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>de 16 revisadas más la FGR</b> · 16 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Chihuahua</b><br>Ciudad Juárez (col. Acequias)</td><td>Cristian «N», Jesús «N», Isaac «N» y Gerson «N» · <span class="muted-note">portación de arma de uso exclusivo, abreviado</span></td><td><b>6 a 11 m 9 d</b> (dos) · <b>6 a 5 m 20 d</b> (dos)</td><td>FGR · FECOR</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>7-oct</b> por tres medios, uno con fecha en la ruta; <code>FRONTERA DE VENTANA</code>; la segunda pena, solo por resumen</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br><span class="muted-note">municipio no publicado</span></td><td>Laurentino «N» · <span class="muted-note">delitos sexuales contra una adolescente de 13 años</span></td><td><b>44 años</b></td><td>FGJ Nuevo León</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>7-oct</b> por un medio nacional con fecha en la ruta; <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas por primera vez, publicadas antes de la apertura y sin boletín oficial</b>: Santa Catarina, NL, 25 años a dos (6-oct) · Edomex: Cuautitlán Izcalli 58 a 9 m (3-oct), Ecatepec 30 a 7 m (5-oct), Ocoyoacac 48 a 9 m (1-oct), Soyaniquilpan 50 años (29-sep) · Cárdenas, Tab., FGR, 4 a 8 m (sin fecha fijada). <code>NO SE INTEGRAN.</code>
    <br><b>Candidatos heredados, siguen sin boletín oficial</b>: San Andrés Tuxtla 58 a 4 m · Nogales 50 años · Tijuana FGR 29 años ×2 · Puebla 36 a 6 m y 32 a 3 m · Puebla 13 años (lectura del 8-oct: sin resultado) · Hidalgo 50 años ×2 · Nuevo León, cuatro casos · Juárez 58 a 4 m · Lagos de Moreno 11 años 40 días. <code>NO SE INTEGRAN.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>16 de 32</b> · <b>FGR revisada: Sí</b> · BC, Son, Chih, Dgo · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · NL · Ver, Tab · Jal, Gto</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>0</b></td></tr>
      <tr><td><b>Con sentencias publicadas en ventana solo por medios</b></td><td><b>1</b> fiscalía estatal: Nuevo León · <b>y la FGR</b>, en Chihuahua</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>16</b>: BCS, Sin · Coah, Tamps, SLP, Zac · Col, Nay, Ags, Mich · Chis, Oax, Gro, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 32 de 32</b> por búsqueda genérica · <b>armamento: 30 de 32</b> —Morelos y Tlaxcala, <code>NO REVISADA</code>— · <b>ningún portal por <code>site:</code></b> · GN, SEDENA y SEMAR regionales: <code>NO REVISADA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>7-oct</b>: localizado, diario, por republicadores · <b>8-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 8-OCT: GOB.MX Y MEDIOS</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>UN SOLO EVENTO ROJO FIJA EL NIVEL</b>: el ataque contra jóvenes en Cócorit, Cajeme, con <b>un adolescente de 15 años muerto y tres heridos</b>.
      <br><b>2.</b> <b>Un amarillo</b> —homicidio en un domicilio de Salamanca— y <b>cinco verdes</b>, cuatro de ellos del boletín federal del 7-oct.
      <br><b>3.</b> <b>La respuesta asegura sin detener</b>: <b>2 detenidos</b> en cuatro eventos de armamento; Tlaxcoapan y Pánuco, sin detenidos —<b>cálculo propio</b>—.
      <br><b>4.</b> Las recuperaciones de la ventana de ARGOS 125 suman <b>cuatro rojos</b> —agresión al Ejército en Balleza, Salvador Escalante, Mixtequilla y la sierra de Zihuatanejo— que el mando debe leer junto al corte.
      <br><b>5.</b> <code>17 H 41 MIN Y SEIS DE SIETE HECHOS CON FRONTERA DE VENTANA: LOS TOTALES NO SON COMPARABLES CON LOS DE NINGUNA EDICIÓN ANTERIOR.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. CONCORDIA ES DEPÓSITO RECURRENTE DE AEI.</b> 82 en Pánuco, tras <b>49 el 28-ago</b> (ARG-111-003) y <b>75 el 22-sep</b> (ARG-124-003) en el mismo municipio, y los de El Rosario y Escuinapa (ARG-125-010, ARG-125-005): el corredor Concordia–El Rosario–Escuinapa
      sostiene producción, no acopio aislado. Línea: <b>cotejo de componentes y búsqueda del taller</b> — hipótesis, requiere validación.
      <br><b>2. EL DRON EXPLOSIVO YA DESPLAZA POBLACIÓN EN GUERRERO.</b> San Ignacio, sierra de Zihuatanejo: drones, casquillos .50 y blindado, sobre una
      extorsión ganadera que un desplazado sitúa desde 2021 (ARG-126-REC-008). Línea: <b>cuotas por kilo de res</b> en la sierra poniente.
      <br><b>3. LA CADENA DEL AGUACATE ES BLANCO ARMADO.</b> Tres muertos en un acopio de Salvador Escalante, uno de 15 años. Línea: <b>padrón de acopios
      y cuotas por caja</b> en la meseta purépecha.
      <br><b>4. FUSILES DE USO EXCLUSIVO EN EL NARCOMENUDEO DE HIDALGO.</b> Cuatro en un punto de venta de Tlaxcoapan, con chalecos y cascos, sin detenidos:
      capacidad de fuego de célula, no de vendedor. Línea: <b>serie e importación</b> de los cuatro fusiles.
      <br><b>5. EN SONORA EL MENOR MUERE JUNTO AL PUNTO DE VENTA.</b> 13 años en Hermosillo (ARG-125-009) y 15 en Cócorit (ARG-126-001), ambos junto a lo que vecinos y fiscal describen como puntos de droga — hipótesis.
      Línea: <b>mapa de puntos de venta con presencia de menores</b> en Hermosillo y Cajeme.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados/</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación nueva localizada dentro de la ventana</b>.
    <br><b>El agregado federal del periodo</b> es el <b>boletín de acciones relevantes del Gabinete de Seguridad del 7-oct</b>, diario, alcanzado por dos republicadores.
    <code>NO INDEXADO POR SU EMISOR: SUS REPUBLICADORES NO SON FUENTES INDEPENDIENTES ENTRE SÍ.</code>
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — MIÉRCOLES 7-OCT", co1)
 + page("CRIMEN ORGANIZADO (II) — MIÉRCOLES 7-OCT, BOLETÍN FEDERAL", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES DE LA VENTANA DE ARGOS 125: 7 A 5-OCT", rec1)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES: 3 Y 2-OCT, Y VENTANAS DE ARGOS 123 Y 105", rec2)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM)
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert "WINDOW_DAYS = 14" in script
script = script.replace("WINDOW_DAYS = 14", "WINDOW_DAYS = 2")
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, TOT, ARMAS, len(E), len(R))
