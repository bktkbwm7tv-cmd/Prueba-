# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 128: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-128.py <plantilla ARGOS 127> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "128", "2026-10-10", "09:08"
CONSULTA = "2026-10-10 09:08-09:20"
DUR = "25 h 48 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
BOL = "<code>BOLETÍN FEDERAL DEL 8-OCT, PUBLICADO EL 9-OCT, ALCANZADO SOLO POR REPUBLICADORES: CORROBORACIÓN DÉBIL POR CONSTRUCCIÓN</code>"
RES = "<code>SOLO POR RESUMEN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-128-001", estado="MX-OAX", region="Sureste", color="rojo", impacto="grande", fecha="2026-10-09", hora="por la tarde (solo por resumen)",
  ent="Oaxaca", mun="Santiago Pinotepa Nacional (barrio La Planta)", dia="9-OCT, TARDE",
  title="OAXACA · PINOTEPA NACIONAL — ASESINADO EN UN ATAQUE ARMADO EL PERIODISTA HAMURABI HUESCA, DIRECTOR DE PINOTEPA COMUNICA",
  hecho="Santiago Pinotepa Nacional · <code>BARRIO LA PLANTA, 9a. PONIENTE Y 13a. O 15a. SUR — CRUCE CONTRADICHO</code> · VIERNES 9-OCT, por la tarde (" + RES + ") · ataque armado · <b>muere el periodista Hamurabi Huesca Manzano</b>, director del portal Pinotepa Comunica, que también trabajaba como taxista, por titular (🔴) · <b>3 muertos</b>, por titular de cuatro medios regionales; uno de ellos, señalado como el blanco, muere horas después en el hospital · <code>CIFRA CONTRADICHA: 3 MUERTOS, O 2 MUERTOS Y UNA MUJER LESIONADA</code> · <b>FGE Oaxaca</b>: el blanco era otro hombre y el móvil, una disputa entre células; no descarta el vínculo con la actividad periodística — " + RES + " · <b>cero detenidos</b> · identidades de las otras víctimas, solo por iniciales: no se reproducen",
  panel="Asesinado el <b>periodista Hamurabi Huesca</b> en un ataque armado; <b>3 muertos</b>, cifra contradicha",
  inst="FGE Oaxaca <span class=\"muted-note\">(por cita)</span>", nac="El Universal · Infobae · La Razón · Milenio", conf="★★★☆☆",
  campo="cifra de víctimas contradicha; hora, solo por resumen", I=1, N=4, R=10, A=0,
  fechadas=["La Razón (2026/10/10)", "Infobae (2026/10/10)", "El Mañana (2026/10/9)", "Primera Línea (2026/10/09)"], estatus="Parcialmente corroborado", arm=None,
  desl="Pinotepa Nacional figura en el índice (ARG-100-004, cateo de agosto): otro hecho. Barrio La Planta no figura. 🔴 por víctima periodista y víctimas múltiples"),
 dict(id="ARG-128-002", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-09", hora="~13:00 (solo por resumen)",
  ent="Guanajuato", mun="Celaya (Eje Clouthier y camino a San José de Guanajuato, col. Álamos)", dia="9-OCT ~13:00",
  title="GUANAJUATO · CELAYA — PERSECUCIÓN CON DETONACIONES DE LAS FUERZAS ESTATALES: DOS DETENIDOS Y ARMAS ASEGURADAS",
  hecho="Celaya · <code>EJE CLOUTHIER Y CAMINO A SAN JOSÉ DE GUANAJUATO, A LA ALTURA DE LA COL. ÁLAMOS</code> · VIERNES 9-OCT ~13:00 (" + RES + ") · <b>Fuerzas de Seguridad Pública del Estado</b> persiguen a hombres presuntamente armados en una camioneta · detonaciones durante el seguimiento, <code>SIN PRECISAR QUIÉN DISPARÓ</code> · <b>2 detenidos</b>, por titular · «armas aseguradas», por titular, <code>SIN CIFRA: «UN ARMA DE FUEGO» Y UN VEHÍCULO, SOLO POR RESUMEN — CANTIDAD NO DETERMINADA, NO SE INTEGRA AL TOTAL NUMÉRICO</code> (🟡) · sin lesionados publicados · <code>COLOR DE LA CAMIONETA CONTRADICHO</code> · antecedentes de los detenidos en Guanajuato y Querétaro, " + RES,
  panel="Persecución con detonaciones: <b>2 detenidos</b>; armas sin cifra",
  inst="Seguridad y Paz Gto. <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="cantidad de armas contradicha; hora y origen de los disparos, solo por resumen", I=1, N=0, R=5, A=0,
  fechadas=["AM (2026/10/09)", "Noticieros en Línea (2026/oct/09)", "Primer Plano Irapuato (2026/10/10)"], estatus="Parcialmente corroborado", arm="ARG-128-ARM-001",
  desl="Celaya figura en el índice (ARG-98-003, ARG-103-REC-006, ARG-122-002): otros hechos. NO es la detención de Celaya y Villagrán publicada el 6-oct: otra fecha. 🟡 por persecución con detonaciones"),
 dict(id="ARG-128-003", estado="MX-MEX", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-09", hora="~09:30, llamada al 911 (solo por resumen)",
  ent="Estado de México", mun="San José del Rincón (San Joaquín Lamillas)", dia="9-OCT ~09:30",
  title="ESTADO DE MÉXICO · SAN JOSÉ DEL RINCÓN — ATAQUE ARMADO CONTRA LOS OCUPANTES DE UNA CAMIONETA: DOS MUERTOS Y UN HERIDO GRAVE",
  hecho="San José del Rincón · <code>COMUNIDAD SAN JOAQUÍN LAMILLAS</code> · VIERNES 9-OCT ~09:30, llamada al 911 por detonaciones (" + RES + ") · hombres armados disparan contra los ocupantes de una camioneta Jeep Cherokee negra · <b>2 hombres muertos</b> y <b>1 herido grave</b>, por titular (🔴) · <b>FGJ del Estado de México</b> investiga · <b>cero detenidos</b> · móvil no establecido · persecución previa y cierre del paso, versión preliminar, " + RES + " · <code>NINGUNA FUENTE CON FECHA EN LA RUTA: EL DÍA, SOLO POR RESUMEN</code> · " + FR,
  panel="Ataque a una camioneta: <b>2 muertos</b> y <b>1 herido grave</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="fecha y hora solo por resumen; ninguna fuente con fecha en la ruta", I=0, N=0, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="San José del Rincón y San Joaquín Lamillas no figuran en el índice. Ninguna edición anterior lo vio: se integra en la primera que lo ve, con su reserva de fecha. 🔴 por homicidio múltiple"),
 dict(id="ARG-128-004", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-09", hora="por la mañana; la SSP informa ~09:25 (solo por resumen)",
  ent="Sinaloa", mun="Mazatlán (penal El Castillo)", dia="9-OCT, MAÑANA",
  title="SINALOA · MAZATLÁN — SEGUNDA RIÑA EN EL PENAL DE EL CASTILLO EN VEINTICUATRO HORAS: DOS INTERNOS MUERTOS",
  hecho="Centro Penitenciario <code>EL CASTILLO</code>, Mazatlán · VIERNES 9-OCT, por la mañana; la SSP lo informa ~09:25 (" + RES + ") · nueva riña en uno de los módulos · <b>2 internos muertos</b>, por titular (🔴) · <b>arma punzocortante</b>, según la FGE, por titular · sin heridos publicados · <b>Grupo Interinstitucional</b> controla · <b>FGE Sinaloa</b> investiga · <b>detenidos: no informados</b> · la SSP, por cita de medios: «una nueva riña al interior de uno de sus módulos, en la que murieron dos personas privadas de la libertad» · vínculo con la riña del 8-oct, <code>NO CONFIRMADO POR LA FGE</code> · identidades, sin verificar: no se reproducen · " + FR,
  panel="<b>Segunda riña</b> en el penal El Castillo: <b>2 internos muertos</b>",
  inst="SSP Sinaloa <span class=\"muted-note\">(por cita)</span>", nac="Proceso · El Financiero · La Silla Rota · Reforma · Excélsior", conf="★★★☆☆",
  campo="hora del hecho, solo por resumen", I=1, N=7, R=1, A=0,
  fechadas=["Proceso (2026/10/9)", "El Financiero (2026/10/09)", "La Silla Rota (2026/10/9)"], estatus="Parcialmente corroborado", arm=None,
  desl="NO es ARG-127-004 (riña del 8-oct, ventana de ARGOS 127): otro día, otro saldo; la FGE no confirma el vínculo. NO es la riña del 24-sep en el área de talleres, publicada en su día. 🔴 por motín con víctimas"),
 dict(id="ARG-128-005", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-09", hora="no fijada («por la noche»)",
  ent="Estado de México", mun="Naucalpan (col. Valle Dorado)", dia="PUB. 9-OCT, HORA NO FIJADA",
  title="ESTADO DE MÉXICO · NAUCALPAN — AGRESIÓN A BALAZOS EN VALLE DORADO: UN MUERTO Y UN LESIONADO",
  hecho="Naucalpan · <code>COL. VALLE DORADO, GUADALUPE VICTORIA Y 5 DE FEBRERO</code> · «por la noche»; publicado el VIERNES 9-OCT · agresión a balazos · <b>1 muerto</b> y <b>1 lesionado</b>, " + RES + " (🟡) · el total de los dos hechos de Naucalpan —<b>2 muertos y 1 lesionado</b>— y <b>cero detenidos</b>, por titular · <code>NOCHE DEL 8 O DEL 9-OCT: NO FIJADA</code> · " + FR,
  panel="<b>1 muerto</b> y 1 lesionado a balazos (reparto por hecho, solo por resumen)",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Infobae", conf="★★☆☆☆",
  campo="reparto de víctimas entre los dos hechos y hora, solo por resumen", I=0, N=1, R=2, A=0,
  fechadas=["Infobae (2026/10/09)", "Seunonoticias (2026/10/09)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no fijada (publicado 2026-10-09)",
  desl="Naucalpan no figura en el índice. NO es ARG-128-006 (Minas Palacio): dos hechos según el titular, vínculo no establecido. Una nota de Milenio sobre un cuerpo abandonado y 2 lesionados en Naucalpan puede ser otro hecho: no se vincula. 🟡 por homicidio doloso único"),
 dict(id="ARG-128-006", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-09", hora="no fijada («por la noche»)",
  ent="Estado de México", mun="Naucalpan (col. Minas Palacio)", dia="PUB. 9-OCT, HORA NO FIJADA",
  title="ESTADO DE MÉXICO · NAUCALPAN — ASESINADO A BALAZOS UN HOMBRE EN MINAS PALACIO",
  hecho="Naucalpan · <code>COL. MINAS PALACIO</code> · «por la noche»; publicado el VIERNES 9-OCT · agresión a balazos · <b>1 hombre muerto</b>, " + RES + " (🟡) · <b>cero detenidos</b>, por titular · alias preliminar de la víctima y venta de sustancias, versiones sin confirmar: no se reproducen · <code>NOCHE DEL 8 O DEL 9-OCT: NO FIJADA</code> · " + FR,
  panel="<b>1 hombre asesinado</b> a balazos (solo por resumen)",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Infobae", conf="★★☆☆☆",
  campo="reparto de víctimas entre los dos hechos y hora, solo por resumen", I=0, N=1, R=2, A=0,
  fechadas=["Infobae (2026/10/09)", "Seunonoticias (2026/10/09)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no fijada (publicado 2026-10-09)",
  desl="Minas Palacio no figura en el índice. NO es ARG-128-005 (Valle Dorado). 🟡 por homicidio doloso único")
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-128-REC-001", estado="MX-VER", region="Golfo", fecha="2026-10-08", hora="~21:00 (solo por resumen)", orig="ARGOS 127", col_orig="rojo",
  ent="Veracruz", mun="Papantla (tramo Miguel Hidalgo–El Porvenir)", dia="8-OCT, NOCHE",
  title="VERACRUZ · PAPANTLA — ASESINADOS EN UN ATAQUE ARMADO UNA MUJER Y SU HIJO DE CATORCE AÑOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127</code> · <code>TRAMO MIGUEL HIDALGO–EL PORVENIR</code> · noche del JUEVES 8-OCT, ~21:00 (" + RES + ") · ataque armado · <b>2 muertos</b>, por titular: <b>una mujer y su hijo de 14 años</b>; ella en un hospital de Papantla, él durante el traslado a Poza Rica (🔴 en su ventana) · <b>cero detenidos</b> · Fiscalía investiga · <code>MECÁNICA CONTRADICHA: ATAQUE A UN VEHÍCULO O IRRUPCIÓN EN UNA VIVIENDA</code> · <code>EDAD DE LA MUJER CONTRADICHA</code> · <code>NINGUNA FUENTE CON FECHA EN LA RUTA</code>",
  panel="Asesinados <b>una mujer y su hijo de 14 años</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="N+",
  conf="★★☆☆☆", campo="ninguna fuente con fecha en la ruta; mecánica contradicha", I=0, N=1, R=4, A=0,
  fechadas=[], desl="Papantla figura en el índice (ARG-112-SEN-001, ARG-119-017): otros hechos. 🔴 por víctimas múltiples, una de ellas menor de edad"),
 dict(id="ARG-128-REC-002", estado="MX-ZAC", region="Noreste", fecha="2026-10-08", hora="no fijada", orig="ARGOS 127 o 126", col_orig="amarillo",
  ent="Zacatecas", mun="Huanusco (carretera federal 54)", dia="8-OCT",
  title="ZACATECAS · HUANUSCO — MUERE TRAS UN ATAQUE ARMADO A SU VEHÍCULO EL PADRE DE LA PRESIDENTA MUNICIPAL",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127 O 126 — HORA NO FIJADA</code> · <code>CARRETERA FEDERAL 54</code> · JUEVES 8-OCT · ataque armado contra el vehículo del padre de la presidenta municipal de Huanusco · <b>1 hombre muerto</b>, por titular de dos medios nacionales (🟡 en su ventana) · dos heridas por arma de fuego según la necropsia, " + RES + " · <b>cero detenidos</b> · <code>LUGAR DEL DECESO CONTRADICHO: HOSPITAL DE JALPA O CLÍNICA DE HUANUSCO</code> · hora no fijada",
  panel="Asesinado el <b>padre de la presidenta municipal</b>", inst="FGE Zacatecas <span class=\"muted-note\">(por cita)</span>", nac="Reforma · El Universal",
  conf="★★★☆☆", campo="hora y lugar del deceso", I=1, N=2, R=3, A=0,
  fechadas=["Diario.mx (2026/oct/08)", "Quinto Poder (2026/10/08)", "El Vigía (2026/10/09)"], desl="Huanusco no figura en el índice. 🟡: homicidio doloso único; la víctima es familiar de una autoridad, no la autoridad"),
 dict(id="ARG-128-REC-003", estado="MX-TAM", region="Noreste", fecha="2026-10-08", hora="no fijada", orig="ARGOS 127 o 126", col_orig="verde",
  ent="Tamaulipas", mun="Río Bravo (canal Anzaldúas)", dia="8-OCT",
  title="TAMAULIPAS · RÍO BRAVO — ARMAS LARGAS, CARTUCHOS Y PONCHALLANTAS ASEGURADOS POR EL EJÉRCITO EN EL CANAL ANZALDÚAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127 O 126 — HORA NO FIJADA</code> · <code>CANAL ANZALDÚAS</code> · acciones del JUEVES 8-OCT · <b>Ejército</b>, en recorrido · <b>2 armas largas</b> · <b>8 cargadores</b> · <b>225 cartuchos</b> · 48 ponchallantas —todas las cifras " + RES + "; «ponchallantas», por titular—, 1 chaleco táctico, 2 placas balísticas, 1 vehículo (🟢 en su ventana) · <b>sin detenidos publicados</b> · ninguna nota reporta agresión · " + BOL,
  panel="<b>2 largas</b>, <b>225 cartuchos</b> y 8 cargadores, solo por resumen; sin detenidos", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio",
  conf="★★★☆☆", campo="desglose solo por resumen; republicadores de un mismo boletín", I=1, N=1, R=4, A=0,
  fechadas=["Línea Directa (2026-10-09)"], desl="Río Bravo no figura en el índice en octubre; el canal Anzaldúas no figura"),
 dict(id="ARG-128-REC-004", estado="MX-CHH", region="Noroeste", fecha="2026-10-08", hora="no fijada", orig="ARGOS 127 o 126", col_orig="verde",
  ent="Chihuahua", mun="Ciudad Juárez", dia="8-OCT",
  title="CHIHUAHUA · CIUDAD JUÁREZ — CATEO FEDERAL: DOS DETENIDOS, 81 CARTUCHOS Y CUATRO CARGADORES",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127 O 126 — HORA NO FIJADA</code> · acciones del JUEVES 8-OCT · <b>FGR, SSPC, Ejército y GN</b> catean un inmueble · <b>2 detenidos</b> · <b>4 cargadores</b> · <b>81 cartuchos</b> · 2 vehículos y equipo electrónico (🟢 en su ventana) · <b>sin armas publicadas</b> · cifras por cita del boletín, " + RES + " · colonia no publicada por el boletín; un medio regional sitúa un cateo con dos detenidos y cargadores en el fracc. Guanajuato, <code>SIN VERIFICAR QUE SEA EL MISMO</code> · " + BOL,
  panel="<b>2 detenidos</b>, <b>81 cartuchos</b> y 4 cargadores; sin armas", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio",
  conf="★★★☆☆", campo="cifras solo por resumen; republicadores de un mismo boletín", I=1, N=1, R=3, A=0,
  fechadas=["Línea Directa (2026-10-09)"], desl="Ciudad Juárez figura en el índice (ARG-125-030, 30-sep; ARG-126-007, 6-oct): otros hechos"),
 dict(id="ARG-128-REC-005", estado="MX-GUA", region="Occidente", fecha="2026-10-08", hora="no fijada", orig="ARGOS 127 o 126", col_orig="verde",
  ent="Guanajuato", mun="Valle de Santiago (La Isla)", dia="8-OCT",
  title="GUANAJUATO · VALLE DE SANTIAGO — DOS DETENIDOS EN LA ISLA CON 55 CARTUCHOS Y DROGA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127 O 126 — HORA NO FIJADA</code> · <code>LA ISLA</code> · acciones del JUEVES 8-OCT · <code>CORPORACIÓN NO CONFIRMADA: GN, EJÉRCITO O POLICÍA ESTATAL, SEGÚN LA FUENTE</code> · <b>2 detenidos</b> · <b>55 cartuchos</b> · dosis de metanfetamina y marihuana · 1 motocicleta (🟢 en su ventana) · <b>sin armas publicadas</b> · " + RES + " · " + BOL,
  panel="<b>2 detenidos</b> y <b>55 cartuchos</b>; sin armas", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio",
  conf="★★★☆☆", campo="cifras solo por resumen; republicadores de un mismo boletín", I=1, N=1, R=3, A=0,
  fechadas=["Línea Directa (2026-10-09)"], desl="Valle de Santiago figura en el índice (ARG-122-003, ARG-125-013, ARG-125-020): otros hechos. La Isla no figura"),
 dict(id="ARG-128-REC-006", estado="MX-PUE", region="Centro", fecha="2026-10-08", hora="no fijada", orig="ARGOS 127 o 126", col_orig="verde",
  ent="Puebla", mun="Zacatlán (Tomatlán)", dia="8-OCT",
  title="PUEBLA · ZACATLÁN — DETENIDO «EL MOCO», PRESUNTO LÍDER DE UNA CÉLULA DE ROBO DE HIDROCARBURO EN PUEBLA E HIDALGO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127 O 126 — HORA NO FIJADA</code> · <code>TOMATLÁN</code> · acciones del JUEVES 8-OCT · <b>Marina, Fiscalía y Policía Estatal de Puebla</b> detienen a Juan «N», «El Moco», objetivo prioritario, presunto líder de un grupo de robo de hidrocarburo en Puebla e Hidalgo · <b>1 detenido</b> · <b>1 arma</b> — <code>CATEGORÍA CONTRADICHA: «CORTA» O «DE FUEGO» SIN CLASIFICAR</code> · 3 millones de pesos, 3 celulares, 1 radio (🟢 en su ventana) · cifras " + RES + " · <code>UN REPUBLICADOR LO UBICA EN GUANAJUATO: ERROR DE FUENTE</code> · <code>UN MEDIO FECHA LA DETENCIÓN EL 9-OCT: NO ARBITRADO</code> · " + BOL,
  panel="Detenido <b>«El Moco»</b>, objetivo prioritario; 1 arma y 3 millones de pesos", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio · Infobae · UnoTV",
  conf="★★★☆☆", campo="categoría del arma y fecha de la detención", I=1, N=3, R=3, A=0,
  fechadas=["Infobae (2026/10/09)", "Línea Directa (2026-10-09)"], desl="Zacatlán y el Tomatlán de Puebla no figuran en el índice; el Tomatlán del índice es de Michoacán. NO es ARG-127-001 (Puebla capital)"),
 dict(id="ARG-128-REC-007", estado="MX-CHH", region="Noroeste", fecha="2026-10-08", hora="no fijada", orig="ARGOS 127 o 126", col_orig="verde",
  ent="Chihuahua", mun="Cuauhtémoc", dia="8-OCT",
  title="CHIHUAHUA · CUAUHTÉMOC — ASEGURADOS TREINTA KILOS DE COCAÍNA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 127 O 126 — HORA NO FIJADA</code> · acciones del JUEVES 8-OCT · <b>30 kg de cocaína</b> asegurados, por cita del boletín, " + RES + " (🟢 en su ventana) · corporación no publicada · <b>sin detenidos publicados</b> · <b>sin armamento</b> · " + BOL,
  panel="<b>30 kg de cocaína</b>; sin detenidos ni armas", inst="Gabinete de Seguridad <span class=\"muted-note\">(por republicador)</span>", nac="Milenio",
  conf="★★☆☆☆", campo="renglón sin corporación ni lugar; solo por resumen", I=1, N=1, R=2, A=0,
  fechadas=["Línea Directa (2026-10-09)"], desl="Cuauhtémoc de Chihuahua: NO son los 100 kg de cocaína del boletín del 6-oct, no fichados: otra cifra. NO es ARG-125-004 (exelemento de la GN, autolavado) ni los Cuauhtémoc de Colima, Zacatecas o CDMX"),
 dict(id="ARG-128-REC-008", estado="MX-MIC", region="Occidente", fecha="2026-10-08", hora="no fijada (inferencia de ARGOS: madrugada, por el cateo de Sol Naciente)", orig="ARGOS 126 o 127", col_orig="verde",
  ent="Michoacán", mun="Uruapan, Pátzcuaro y Morelia", dia="8-OCT, MADRUGADA",
  title="MICHOACÁN · URUAPAN, PÁTZCUARO Y MORELIA — DOCE CATEOS CONTRA UNA CÉLULA DE ROBO A TRANSPORTE Y SECUESTRO: DIEZ DETENIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126 O 127 — FECHA DEL HECHO, INFERENCIA DE ARGOS</code> · <code>URUAPAN, PÁTZCUARO Y MORELIA</code> · publicado el 9 y 10-oct; el primer titular de detenciones en Michoacán es del 8-oct · <b>Marina, SSPC y FGR</b> · <b>12 cateos</b> contra una célula de robo a transporte de carga y secuestro · <b>10 detenidos</b>, por titular · «dos agentes resultan heridos», por titular · <code>VÍNCULO CON EL CATEO DE SOL NACIENTE: INFERENCIA DE ARGOS</code> · <b>4 armas de fuego sin desglose</b>, cargadores, cartuchos y droga sin cifra, " + RES + " (🟢 en su ventana) · <code>UN TITULAR DEL 8-OCT DA 12 DETENIDOS: NO VERIFICADO QUE SEA LA MISMA OPERACIÓN</code> · sin comunicado oficial localizado",
  panel="<b>12 cateos</b>, <b>10 detenidos</b> y 4 armas sin desglose", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Crónica · Infobae · Milenio · MVS",
  conf="★★★☆☆", campo="armas sin desglose; detenidos, 10 frente a 12", I=0, N=4, R=5, A=0,
  fechadas=["Crónica (2026/10/09)", "Infobae (2026/10/10)", "Esfera (2026/10/09)", "MVS (2026/10/8)"], desl="Probable misma operación que ARG-127-REC-001 (cateo de Sol Naciente repelido, 🟡) —inferencia—: la confrontación y la detención son dos eventos. <code>DETENIDOS DE SOL NACIENTE: 1 (DOS TITULARES) FRENTE A 10 (TITULAR DEL CONJUNTO) — RELACIÓN NO ARBITRADA; NO SE SUMAN</code>. Pátzcuaro figura en el índice: otro hecho"),
 dict(id="ARG-128-REC-009", estado="MX-MIC", region="Occidente", fecha="2026-10-07", hora="tarde, antes de las 20:30 (solo por resumen)", orig="ARGOS 126 o 125", col_orig="rojo",
  ent="Michoacán", mun="Penjamillo", dia="7-OCT, TARDE",
  title="MICHOACÁN · PENJAMILLO — CIVILES ARMADOS DISPARAN CONTRA ELEMENTOS DE LA GUARDIA CIVIL; SIN LESIONADOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126 O 125 — HORA NO FIJADA</code> · tarde del MIÉRCOLES 7-OCT, antes de las 20:30 de la primera publicación (" + RES + ") · civiles armados disparan desde vehículos en movimiento contra la <b>Guardia Civil</b> · <b>sin elementos lesionados</b>, por titular · los agresores huyen · <b>cero detenidos</b> (🔴 en su ventana) · versiones por titular: «embosca» y «repele agresión»; <code>NINGUNA ATRIBUYE LA INICIATIVA AL ESTADO</code>",
  panel="Agresión armada a la <b>Guardia Civil</b>; sin lesionados", inst="SSP Michoacán <span class=\"muted-note\">(por cita)</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★☆☆☆", campo="hora del hecho; ninguna fuente con fecha en la ruta", I=1, N=0, R=3, A=0,
  fechadas=[], desl="Penjamillo figura en el índice solo por mención (ARG-121-REC-005): otro hecho. NO es el tiroteo del 18-sep en Penjamillo. 🔴 por ataque contra autoridades"),
 dict(id="ARG-128-REC-010", estado="MX-ZAC", region="Noreste", fecha="2026-10-07", hora="no fijada", orig="ARGOS 126 o 125", col_orig="verde",
  ent="Zacatecas", mun="Sombrerete", dia="7-OCT",
  title="ZACATECAS · SOMBRERETE — CATEO FEDERAL CON EXPLOSIVOS DE EMULSIÓN Y DETONADORES; CIFRAS CONTRADICHAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 126 O 125 — HORA NO FIJADA</code> · acciones del MIÉRCOLES 7-OCT, informadas por la FGR el 8-OCT · <b>FGR y SSPC</b>, con Defensa y GN · cateo · <b>22 explosivos</b> y <b>185 detonadores</b>, por titular de un medio regional · 16.42 m de mecha, 37 kg de fertilizante y 2 generadores, " + RES + " (🟢 en su ventana) · <code>DETENIDOS NO ATRIBUIDOS: UN TITULAR SOBRE CATEOS EN ZACATECAS Y NUEVO LEÓN DA DOS, SIN PRECISAR DÓNDE</code> · <code>CIFRAS CONTRADICHAS: OTRO MEDIO DA 22 «SALCHICHAS», 39 DETONADORES, 146 CONECTORES Y 16.72 M EN SAN JOSÉ DE LOS RANCHOS — POSIBLE DUPLICIDAD U OPERATIVO DISTINTO, NO ARBITRADO</code>",
  panel="<b>22 explosivos</b> y detonadores (185 o 39, contradichos)", inst="FGR <span class=\"muted-note\">(por cita)</span>", nac="Milenio",
  conf="★★☆☆☆", campo="cifras contradichas entre medios", I=1, N=1, R=4, A=0,
  fechadas=[], desl="Sombrerete figura en el índice (ARG-93-003, laboratorio, agosto): otro hecho. NO es ARG-127-REC-002 (Ojocaliente, mismo boletín del 7-oct): otro municipio")
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-128-ARM-001", ficha="ARG-128-002", estado="MX-GUA", region="Occidente", ent="Guanajuato", mun="Celaya (camino a San José de Guanajuato)", c=[0,0,0,0,0,0,0,0,0,2], corp="Fuerzas de Seguridad Pública del Estado", conf="Bajo", color="amarillo", fecha="2026-10-09", fecha_txt="9-oct ~13:00<br><span class=\"muted-note\">hora solo por resumen</span>", nota="EVENTO CUALITATIVO: «armas aseguradas» sin cifra (titular) frente a «un arma de fuego» (solo por resumen) — CANTIDAD NO DETERMINADA, NO SE INTEGRA AL TOTAL NUMÉRICO; 2 detenidos, por titular", fuentes=["AM (2026/10/09)", "Primer Plano Irapuato (2026/10/10)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 2], TOT
assert cnt == {"rojo": 3, "amarillo": 3, "verde": 0}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 1, "verde": 7}, cnt_rec

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
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"]}

def arm_json(a):
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": "~13:00 (solo por resumen)"}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 127 — Reporte Nacional de Seguridad — 2026-10-09</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. EXIJA A LA FISCALÍA DE OAXACA LA CARPETA DEL ATAQUE DE PINOTEPA NACIONAL</b> (ARG-128-001) y active la protección del equipo
      de Pinotepa Comunica mientras no se descarte el móvil periodístico.
      <br><b>2. AUDITE EL PENAL EL CASTILLO</b> (ARG-128-004, ARG-127-004): revisión de ingreso, custodios de los módulos de las dos riñas
      y origen de las armas de fuego y punzocortantes.
      <br><b>3. COTEJE LOS DETENIDOS DE LOS DOCE CATEOS DE MICHOACÁN</b> (ARG-128-REC-008) contra el cateo repelido de Sol Naciente y
      exija el desglose de las armas.
      <br><b>4. VIGILE EL CORREDOR DEL NORTE DE PUEBLA E HIDALGO</b> tras la captura de «El Moco» (ARG-128-REC-006): reacomodo de la
      célula de robo de hidrocarburo.
      <br><b>5. EXIJA EL INFORME DE CUMPLIMIENTO DEL AMPARO 412/2026 Y EL PERITAJE DEL VIDEO DE EL BALCÓN</b> (ARG-125-051): ninguno
      publicado; la FGE de Guerrero ofrece recompensa por los siete desaparecidos.
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>9-oct 07:20 → 10-oct 09:08 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,23 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: del más reciente al más antiguo</b>; al final, los dos de hora no fijada. <b>Cuatro de seis</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <code>NINGUNA AUTORIDAD PUBLICÓ UN AGREGADO NACIONAL DE ESTA VENTANA.</code>
  </p>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Armas cortas</th><th>Armas largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{TOT[2]}</b></td><td><b>{TOT[3]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Total de armas integradas: {ARMAS}</b> —Celaya, «armas aseguradas» sin cifra: <code>CANTIDAD NO DETERMINADA</code>—. <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento</b>. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios: 9</b> —<b>7 en los tres rojos</b> y <b>2 en los amarillos de Naucalpan</b>, reparto solo por resumen—; <b>heridos: 2</b>, San José del Rincón y Naucalpan; <b>8 muertos y 3 heridos</b> si en Pinotepa son 2 muertos y una lesionada, versión contradicha: <b>cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:4])
co2 = "\n".join(ficha(e) for e in E[4:])
rec1 = "\n".join(ficha(r, True) for r in R[:7])
rec2 = "\n".join(ficha(r, True) for r in R[7:])

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA ARMA CORTA CLASIFICADA EN HECHO PROPIO</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA EN HECHO PROPIO</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>CELAYA: «ARMAS ASEGURADAS» SIN CIFRA — NO SE INTEGRA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>NINGÚN CARTUCHO PUBLICADO EN HECHO PROPIO</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN CARGADOR PUBLICADO EN HECHO PROPIO</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>{len(ARM)} fila de armamento de {len(ARM)} hecho</b> en <b>{len(ENT_ARM)} entidad</b>: <b>cualitativa</b>, sin cifra de armas integrable; solo los 2 detenidos. <b>Totales por categoría: cálculo propio.</b>
    <code>NINGÚN HECHO PROPIO DE ALTO IMPACTO DEJÓ ARMAMENTO ASEGURADO PUBLICADO.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Verde = aseguramiento sin enfrentamiento · amarillo = derivado de enfrentamiento o persecución. La sola presencia de armas no vuelve roja a una entidad.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    cells = "".join(f"<td>{('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for v in c[:9])
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    return f'      <tr id="{a["id"]}"><td><a href="#{a["ficha"]}"><code>{a["id"]}</code></a></td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'
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
    <b>Lectura regional</b> —1 fila, <b>cálculo propio</b>—: <b>Noroeste 0</b> · <b>Noreste 0</b> · <b>Occidente 1</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    <b>1 evento cualitativo sin cantidad.</b> El armamento de las recuperaciones —Río Bravo, Ciudad Juárez, Valle de Santiago, Zacatlán, Michoacán y Sombrerete— va en su ficha y <b>no entra en esta tabla</b>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA INTEGRABLE</code> · dos titulares oficiales de la FGR del 9-oct sin caso individualizado, abajo</span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas del 9-oct quedan en <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto ordenado y publicado</b> en la ventana</span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>de 21 revisadas más la FGR</b> · 11 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Chihuahua</b><br><span class="muted-note">municipio no publicado</span></td><td>Comunicado del listado estatal de la FGR · <span class="muted-note">portación de arma de fuego y metanfetamina</span></td><td><b>7 años</b>, por titular</td><td>FGR</td><td>Titular oficial en el listado de la FGR del <b>9-oct</b>; <code>SIN SENTENCIADO, MUNICIPIO NI FIRMEZA: CASO NO INDIVIDUALIZADO</code> · <code>FRONTERA DE VENTANA</code></td><td>Medio</td></tr>
      <tr><td><b>Sinaloa</b><br><span class="muted-note">municipio no publicado</span></td><td>Comunicado del listado estatal de la FGR · <span class="muted-note">tres personas, portación de arma, cartuchos y cargadores</span></td><td><b>hasta 11 años</b>, por titular</td><td>FGR</td><td>Titular oficial del <b>9-oct</b>; <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code>; caso no individualizado · <code>FRONTERA DE VENTANA</code></td><td>Medio</td></tr>
      <tr><td><b>Guanajuato</b><br>León (San Pedro Plus)</td><td>Lázaro Alan Emmanuel «N» · <span class="muted-note">feminicidio, procedimiento abreviado; hecho del 30-oct-2025</span></td><td><b>26 años 8 meses</b></td><td>FGE Guanajuato</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el <b>9-oct</b> por dos medios con fecha en la ruta; sin boletín por <code>site:</code></td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>Monterrey (Condominios Constitución)</td><td>Dos hombres · <span class="muted-note">homicidio</span></td><td><b>28 años</b></td><td>FGE Nuevo León</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · un medio nacional, <b>9-oct</b> en la ruta; <code>FRONTERA DE VENTANA</code></td><td>Bajo</td></tr>
      <tr><td><b>Chihuahua</b><br><span class="muted-note">municipio no publicado</span></td><td>Un hombre · <span class="muted-note">abuso sexual agravado, procedimiento abreviado</span></td><td><b>8 años</b></td><td>FGE Chihuahua</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · un medio regional, <b>9-oct</b> en la ruta</td><td>Bajo</td></tr>
      <tr><td><b>Veracruz</b><br>varios distritos</td><td>Agregado de 24 h · <span class="muted-note">«20 sentencias condenatorias» con vinculaciones e imputaciones</span></td><td><span class="muted-note">no individualizada</span></td><td>FGE Veracruz</td><td>Agregado publicado el <b>9-oct</b> por republicadores; sin penas por caso · <code>NO INTEGRAR</code></td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas por primera vez, publicadas antes de la apertura</b>: Querétaro ×3 con boletín oficial (5, 6 y 8-oct) · Guerrero, Tlapehuala · Veracruz, secuestro agravado · Nuevo León, Las Sabinitas · FGR, Chihuahua y Ciudad Juárez. <code>NO SE INTEGRAN: FUERA DE VENTANA.</code>
    <br><b>Candidatos heredados, siguen sin boletín oficial</b>: Cajeme, 25 años · Campeche (Lerma), FGR · Matamoros ×6 · NL, Laurentino «N» · QRoo · Buenavista · Nayarit ×2 · Culiacán · BCS. <code>NO SE INTEGRAN.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>21 de 32</b> · <b>FGR revisada: Sí</b> · BC, BCS, Chih, Dgo · NL, Tamps · Jal, Gto, Ags, Mich · CDMX, Mor, Pue, Tlax, Hgo, Qro · Ver, Tab · Gro, Oax, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>0</b></td></tr>
      <tr><td><b>Con sentencias publicadas en ventana solo por medios o sin individualizar</b></td><td><b>4</b> fiscalías estatales: Guanajuato, Nuevo León, Chihuahua y Veracruz (agregado) · <b>y la FGR</b>, en Chihuahua y Sinaloa</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>17</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>11</b>: Son, Sin · Coah, SLP, Zac · Col, Nay · Edomex · Chis, Camp, Yuc</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 28 de 32</b> —BCS, Querétaro, Chiapas y Yucatán, <code>NO REVISADA</code>— · <b>armamento: 20 de 32</b> —BC, Sin, Coah, SLP, Col, Nay, Edomex, Tlax, Qro, Ver, Camp y Yuc, <code>NO REVISADA</code>— · <code>REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, SEDENA y SEMAR regionales: <code>NO REVISADA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 8-oct</b>: publicado el 9-oct, diario, por republicadores · <b>acciones del 9-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 10-OCT: GOB.MX Y FGR.ORG.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR TRES ROJOS</b>: ARG-128-001 (Oaxaca), ARG-128-003 (Estado de México) y ARG-128-004 (Sinaloa).
      <br><b>2.</b> <b>Contexto operativo</b>: tres amarillos (ARG-128-002, ARG-128-005, ARG-128-006); <b>ninguna acción institucional propia</b> en la ventana.
      <br><b>3.</b> <b>Ningún detenido publicado</b> por los tres rojos (ARG-128-001, ARG-128-003, ARG-128-004).
      <br><b>4.</b> La respuesta institucional del periodo aparece solo en recuperaciones (ARG-128-REC-003 a ARG-128-REC-008, ARG-128-REC-010), fuera del nivel.
      <br><b>5.</b> <code>25 H 48 MIN; CUATRO DE SEIS HECHOS CON FRONTERA DE VENTANA Y LAS HORAS DE LOS OTROS DOS SOLO POR RESUMEN; BOLETÍN FEDERAL DEL 9-OCT SIN INDEXAR: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. EN EL BAJÍO, CÉLULAS ARMADAS EN VEHÍCULOS FRENTE A LA FUERZA ESTATAL.</b> Disparos contra la Guardia Civil en Penjamillo (ARG-128-REC-009) y persecución
      con detonaciones de autor no determinado en Celaya (ARG-128-002). Línea: <b>rutas de huida y vehículos</b> — hipótesis.
      <br><b>2. ATAQUES ARMADOS CONTRA OCUPANTES DE VEHÍCULOS EN CARRETERAS Y CAMINOS RURALES.</b> San José del Rincón (ARG-128-003) y Huanusco (ARG-128-REC-002), este contra
      el familiar de una autoridad; en Papantla muere un menor (ARG-128-REC-001). Línea: <b>tramos de riesgo y perfil del blanco</b>.
      <br><b>3. LA MUNICIÓN CIRCULA SEPARADA DEL ARMA.</b> Cateos federales con cartuchos (ARG-128-REC-004, ARG-128-REC-005) y cargadores (ARG-128-REC-004) sin arma asegurada — consistente con
      acopio logístico, requiere validación. Línea: <b>rastreo de lotes</b> de munición.
      <br><b>4. EXPLOSIVO COMERCIAL EN EL NORTE DE ZACATECAS.</b> Emulsión y detonadores en Sombrerete (ARG-128-REC-010), con cifras contradichas. Línea: <b>control de
      polvorines y minas</b> como fuente de AEI — hipótesis.
      <br><b>5. LA BRECHA ENTRE DETENCIÓN Y CONDENA SIGUE ABIERTA.</b> Ninguna sentencia integrable; las de la FGR del 9-oct solo existen como titular.
      Línea: <b>exigir el comunicado completo</b> de cada sentencia anunciada.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados/</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>: ningún informe diario de octubre indexado. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — VIERNES 9-OCT: PINOTEPA NACIONAL, CELAYA, SAN JOSÉ DEL RINCÓN Y PENAL EL CASTILLO", co1)
 + page("CRIMEN ORGANIZADO (II) — HECHOS DE HORA NO FIJADA: NAUCALPAN", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES DEL 8-OCT: VENTANAS DE ARGOS 127 Y 126", rec1)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES DEL 7 Y 8-OCT: VENTANAS DE ARGOS 127, 126 Y 125", rec2)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 9-oct 07:20 → 10-oct 09:08 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R))
