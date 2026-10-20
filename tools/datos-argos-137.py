# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 137: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-137.py <plantilla ARGOS 136> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "137", "2026-10-19", "11:05"
CONSULTA = "2026-10-19 11:05-16:55"
DUR = "26 h 31 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA: PUEDE SER ANTERIOR A LAS 08:34 DEL 18</code>"
FNF = "<code>FECHA DEL HECHO NO FIJADA DENTRO DEL 16 AL 18-OCT: PUBLICADO DURANTE EL CORTE</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-137-001", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-18", hora="tarde (solo por resumen)",
  ent="Guerrero", mun="Copanatoyac (Crucero de Oztocingo)", dia="18-OCT, TARDE, DÍA SOLO POR RESUMEN",
  title="GUERRERO · COPANATOYAC — ATACAN A BALAZOS A UNA FAMILIA DE COMERCIANTES: DOS MUERTOS Y DOS HERIDOS",
  hecho="Copanatoyac · <code>CRUCERO DE OZTOCINGO, PUESTO DE COCOS Y AGUAS FRESCAS DURANTE LA FIESTA DE SAN LUCAS, SOLO POR RESUMEN</code> · tarde del DOMINGO 18-OCT, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · hombres armados a bordo de una camioneta disparan y huyen, " + RES + " · <b>2 muertos</b> —un matrimonio— y <b>2 heridos</b>, por titulares (🔴) · heridos: un niño de 8 años y una joven de 18, graves, trasladados al hospital IMSS-Bienestar de Tlapa, " + RES + " · FGE Guerrero acudió, " + RES + " · <b>ningún detenido publicado</b> · móvil: no publicado · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos y 2 heridos</b>",
  inst=SB, nac="Unomásuno", conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con fecha; sin fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-18, DÍA SOLO POR RESUMEN",
  desl="Copanatoyac y Oztocingo no figuran en las cinco ediciones previas ni en el índice. Distinto por cifras y perfil del homicidio de un coordinador del PT del mismo municipio y cuatro familiares (fecha no fijada, solo por resumen): no se integra y no se descarta relación."),
 dict(id="ARG-137-002", estado="MX-JAL", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-19", hora="madrugada (solo por resumen)",
  ent="Jalisco", mun="Tlajomulco de Zúñiga (fracc. Hacienda Santa Fe)", dia="19-OCT, MADRUGADA, DÍA SOLO POR RESUMEN",
  title="JALISCO · TLAJOMULCO — IRRUMPEN EN UNA VIVIENDA DE HACIENDA SANTA FE: DOS MUERTOS Y UNA MUJER HERIDA",
  hecho="Tlajomulco de Zúñiga · <code>FRACC. HACIENDA SANTA FE, POR TITULAR; CALLES PADUA Y ROMA, SOLO POR RESUMEN</code> · madrugada del LUNES 19-OCT, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · varios hombres irrumpen en un domicilio, " + RES + " · <b>2 muertos</b> —un hombre y una mujer— y <b>1 mujer herida</b>, por titulares (🔴) · ~25 años, según la Cruz Verde, " + RES + " · la herida, con un impacto en el tórax, llevada por un vehículo de plataforma, " + RES + "; una tercera persona escapó, según un medio, " + RES + " · <b>ningún detenido publicado</b> · identidades: no publicadas · " + FR,
  panel="Ataque a una vivienda: <b>2 muertos y 1 herida</b>",
  inst=SB, nac="N+ · Milenio", conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con fecha; sin fuente institucional", I=0, N=2, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-19, DÍA SOLO POR RESUMEN",
  desl="Hacienda Santa Fe no figura en las cinco ediciones previas ni en el índice. Un titular de Milenio «Matan a una mujer en Hacienda Santa Fe» no se integra: identidad con este hecho no verificada; «Asesinan a tres personas en Hacienda Santa Fe» (Milenio) es de 2020. Llegada de la herida contradicha (vehículo de plataforma o por sus medios), solo por resumen."),
 dict(id="ARG-137-003", estado="MX-VER", region="Golfo", color="rojo", impacto="mediano", fecha="2026-10-18", hora="~14:00 (solo por resumen)",
  ent="Veracruz", mun="Coatzacoalcos (col. Santa Isabel)", dia="18-OCT, TARDE",
  title="VERACRUZ · COATZACOALCOS — DOS MUERTOS, UN HOMBRE Y UNA MUJER, EN UNA CUARTERÍA DE SANTA ISABEL: MÓVIL NO CONFIRMADO",
  hecho="Coatzacoalcos · <code>COL. SANTA ISABEL, POR TITULAR; CALLE PELÍCANOS ESQUINA ANDADOR GORRIONES, SOLO POR RESUMEN</code> · DOMINGO 18-OCT, por ruta (La Silla Rota) · ~14:00, " + RES + " · <b>1 hombre muerto</b> en una cuartería y <b>1 mujer herida</b>, por titular del 18; <b>la mujer murió</b>, por titulares regionales («suman dos fallecidos»); «en el traslado», " + RES + ": <b>2 muertos</b> (🔴) · el agresor huye en motocicleta, según un medio, " + RES + "; agresión mutua de la pareja o tercera persona que huyó, según otros, " + RES + ": <code>CONTRADICHO</code> · riña o discusión de pareja, " + RES + "; <code>MÓVIL NO CONFIRMADO POR AUTORIDAD</code> · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado en una cuartería: <b>2 muertos</b>",
  inst=SB, nac="La Silla Rota · N+", conf="★★★☆☆",
  campo="segunda muerte por titulares (N+ y dos regionales); móvil solo por resumen; sin fuente institucional", I=0, N=2, R=8, A=0,
  fechadas=["La Silla Rota (2026/10/18)", "Gráfico al Día (2026/10/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Santa Isabel no figura en las cinco ediciones previas ni en el índice. NO es ARG-134-011 (Coatzacoalcos, fracc. Santa Cecilia, 15-oct)."),
 dict(id="ARG-137-004", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-18", hora="no fijada",
  ent="Sinaloa", mun="Mazatlán (Fovissste Esperanza)", dia="PUB. 18-OCT, HORA NO FIJADA",
  title="SINALOA · MAZATLÁN — ASESINAN A BALAZOS A DOS HOMBRES EN EL FOVISSSTE ESPERANZA",
  hecho="Mazatlán · <code>FRACC. FOVISSSTE ESPERANZA, POR TITULAR</code> · publicado el DOMINGO 18-OCT, por ruta (Luz Noticias) · <b>2 hombres asesinados</b> a balazos, por titulares (🔴) · uno debajo de una camioneta y otro dentro de la cabina, por titular de Los Noticieristas · <b>ningún detenido publicado</b> · identidades: no publicadas · " + AP,
  panel="<b>2 hombres asesinados</b> en una camioneta",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-10-18)", "Línea Directa (2026-10-18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Fovissste Esperanza no figura en las cinco ediciones previas ni en el índice. Un funcionario municipal no registró homicidios dolosos en Mazatlán del 15 al 17-oct, solo por resumen. Agregados de medios de la tarde en Mazatlán (2 o 3 muertos, 3 o 4 heridos): posible solapamiento, no integrados."),
 dict(id="ARG-137-005", estado="MX-TAB", region="Golfo", color="rojo", impacto="mediano", fecha="2026-10-18", hora="no fijada",
  ent="Tabasco", mun="Jalapa o Teapa (carretera Villahermosa–Teapa, km 27)", dia="18-OCT, HORA NO FIJADA",
  title="TABASCO · CARRETERA VILLAHERMOSA–TEAPA — HALLAN UN TORSO HUMANO EN UNA BOLSA CON CARTULINAS DE AMENAZA",
  hecho="<code>KM 27 DE LA CARRETERA VILLAHERMOSA–TEAPA, CERCA DE LA COMUNIDAD SAN ANTONIO, TEAPA (EL UNIVERSAL), O RANCHERÍA LA UNIÓN, JALAPA (DIARIO DE YUCATÁN): MUNICIPIO CONTRADICHO; KM 27, SAN ANTONIO, LA UNIÓN Y ASTAPA, SOLO POR RESUMEN</code> · publicado el DOMINGO 18-OCT, por ruta · <b>torso humano</b> en una bolsa negra, por titulares (🔴); manchas de sangre, " + RES + " · <b>cartulinas con mensajes de amenaza</b>, por titular de El Universal; dirigidas a un alto mando de la SSPC, " + RES + "; contenido no revelado · <b>restos humanos con amenazas en tres municipios</b>, por titular de El Universal; «el mismo día», " + RES + ": extremidades cerca de Astapa (Jalapa) y restos en Nacajuca, " + RES + " · Fiscalía de Tabasco: carpeta de investigación, Semefo, " + RES + " · <b>ningún detenido publicado</b> · víctima sin identificar · " + AP,
  panel="<b>Torso humano con cartulinas de amenaza</b>; restos en otros dos puntos",
  inst=SB, nac="El Universal", conf="★★★☆☆",
  campo="municipio contradicho; destinatario de los mensajes solo por resumen; hora no fijada; sin fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["Diario de Yucatán (2026/10/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Teapa y Jalapa (Tab.) no figuran en las cinco ediciones previas; «Nuevo Teapa» (Ver.) figura en ARG-105-REC-004 y «Jalapa» (Gro.) en ARG-120-008; Nacajuca figura en ARG-130-003 (ranchería Taxco): otros hechos. NO es ARG-120-005 (seis ejecutados con mensajes, 15-sep)."),
 dict(id="ARG-137-006", estado="MX-HID", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-19", hora="~09:20 o ~09:30 (solo por resumen)",
  ent="Hidalgo", mun="Tulancingo de Bravo (col. Plan de Ayala)", dia="19-OCT, MAÑANA",
  title="HIDALGO · TULANCINGO — MATAN A UN TRABAJADOR DE SERVICIOS REGIONALES DE LA SECRETARÍA DE EDUCACIÓN",
  hecho="Tulancingo · <code>COL. PLAN DE AYALA, CALLE ADOLFO RUIZ CORTINES, CERCA DE LAS OFICINAS DE SERVICIOS REGIONALES DE LA SEPH, SOLO POR RESUMEN</code> · LUNES 19-OCT, por ruta (La Silla Rota) · ~09:20 o ~09:30, " + RES + " · <b>1 hombre muerto</b>: <b>trabajador de Servicios Regionales de Educación</b>, por titulares (🔴) · la SEPH lamenta el fallecimiento de su trabajador, por titular de Criterio · un disparo en el pecho; el agresor huye en bicicleta, " + RES + " · Procuraduría de Hidalgo a cargo, " + RES + " · móvil: no publicado · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>Trabajador de la Secretaría de Educación de Hidalgo asesinado</b>",
  inst="SEPH <span class=\"muted-note\">(por titular: confirma que era su trabajador)</span>", nac="La Silla Rota · Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; la SEPH confirma la adscripción, no las circunstancias", I=1, N=2, R=5, A=0,
  fechadas=["La Silla Rota (2026/10/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tulancingo y Plan de Ayala no figuran en las cinco ediciones previas ni en el índice. Parentesco de la víctima con el titular regional: extraoficial, no se reproduce."),
 dict(id="ARG-137-007", estado="MX-COL", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-10-18", hora="no fijada",
  ent="Colima", mun="Coquimatlán (tramo a Villa de Álvarez)", dia="PUB. 18-OCT, HORA NO FIJADA",
  title="COLIMA · COQUIMATLÁN — ENFRENTAMIENTO CON LA MARINA: DOS PRESUNTOS INTEGRANTES DE LOS MEZCALES ABATIDOS",
  hecho="<code>TRAMO CARRETERO COQUIMATLÁN–VILLA DE ÁLVAREZ, POR TITULARES</code> · publicado el DOMINGO 18-OCT, por ruta (Proyecto Puente) · la «Mesa de Seguridad» informa que, tras un enfrentamiento, <b>2 presuntos generadores de violencia resultaron abatidos</b>, por titulares de Portal Colima, AFmedios y Vadenuez (🟡) · día 18 por ruta de un medio; 19 en el resumen del buscador: <code>CONTRADICHO</code> · durante un operativo, ambos dispararon contra Marina y policía estatal, que repelieron, " + RES + " · señalados como operadores de <b>Los Mezcales</b>, por titulares · alias publicados: «El Español» y «Santos», por titulares · <b>ningún detenido publicado</b> · <b>armamento asegurado: no publicado</b> · personal de seguridad: sin bajas publicadas · " + AP,
  panel="Enfrentamiento: <b>2 presuntos integrantes de Los Mezcales abatidos</b>",
  inst="Mesa de Seguridad de Colima <span class=\"muted-note\">(por titular)</span>", nac="Infobae · La Jornada · Publimetro · UnoTV · TV Azteca", conf="★★★☆☆",
  campo="hora no fijada; versión oficial solo por cita, sin contraste", I=1, N=5, R=6, A=0,
  fechadas=["Proyecto Puente (2026/10/18)", "Infobae (2026/10/19)", "La Jornada (2026/10/19)", "Publimetro (2026/10/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Los Mezcales figuran en el índice por ARG-104-005 y ARG-105-003 (detenciones de agosto): otros hechos. Vínculos con homicidios atribuidos por medios, no por autoridad. NO es ARG-134-003 (Coquimatlán, 15-oct)."),
 dict(id="ARG-137-008", estado="MX-NLE", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="no fijada",
  ent="Nuevo León", mun="Monterrey (col. Nogales de la Sierra)", dia="PUB. 18-OCT, HORA NO FIJADA",
  title="NUEVO LEÓN · MONTERREY — ASESINAN A BALAZOS A UN HOMBRE EN NOGALES DE LA SIERRA",
  hecho="Monterrey · <code>COL. NOGALES DE LA SIERRA, POR TITULARES; CALLE LIMONES, SOLO POR RESUMEN</code> · publicado el DOMINGO 18-OCT, por ruta (MVS) · <b>1 hombre muerto</b> a balazos, por titulares (🟡) · ~25 años, una herida de bala; Fuerza Civil lo localizó tras un aviso, " + RES + " · si fue baleado en el sitio o llegó herido: no determinado, " + RES + " · <b>ningún detenido publicado</b> · sin identificar · " + AP,
  panel="<b>1 hombre asesinado</b> a balazos",
  inst=SB, nac="MVS · Milenio · N+", conf="★★★☆☆",
  campo="hora no fijada; sin fuente institucional", I=0, N=3, R=1, A=0,
  fechadas=["MVS (2026/10/18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Nogales de la Sierra no figura en las cinco ediciones previas ni en el índice. NO es ARG-135-REC-004 (Nogales, Sonora)."),
 dict(id="ARG-137-009", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="~15:00 (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (bulevar Emiliano Zapata)", dia="18-OCT, TARDE, DÍA SOLO POR RESUMEN",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS A UNA MUJER DENTRO DE UNA HELADERÍA",
  hecho="Culiacán · <code>BULEVAR EMILIANO ZAPATA, SOLO POR RESUMEN</code> · DOMINGO 18-OCT, ~15:00, " + RES + " · <b>1 mujer muerta</b> a balazos dentro de una heladería, por titulares (🟡) · perseguida por un hombre armado que bajó de un automóvil; el agresor huye, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>1 mujer asesinada</b> dentro de una heladería",
  inst=SB, nac="Milenio", conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con fecha", I=0, N=1, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-18, DÍA SOLO POR RESUMEN",
  desl="El bulevar Emiliano Zapata de Culiacán y la heladería no figuran en las cinco ediciones previas ni en el índice. NO es ARG-136-004 (tienda de conveniencia, noche del 17)."),
 dict(id="ARG-137-010", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="no fijada",
  ent="Sinaloa", mun="Escuinapa", dia="PUB. 18-OCT, HORA NO FIJADA",
  title="SINALOA · ESCUINAPA — MATAN A BALAZOS A UNA MUJER",
  hecho="Escuinapa · publicado el DOMINGO 18-OCT, por ruta · <b>1 mujer muerta</b> a balazos, por titular (🟡) · «suman 12 feminicidios en Sinaloa este mes», por titular; clasificación jurídica del hecho no informada por autoridad · <b>ningún detenido publicado</b> · identidad: no publicada · " + AP,
  panel="<b>1 mujer asesinada</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; hora no fijada", I=0, N=0, R=1, A=0,
  fechadas=["Diario de Yucatán (2026/10/18)"], estatus="Pendiente de corroboración", arm=None,
  desl="Escuinapa figura en ARGOS 132 a 134 por otros hechos (12-oct y anteriores) y en el índice por ARG-110-002, ARG-111-002 y ARG-119-008."),
 dict(id="ARG-137-011", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="~02:38 (solo por resumen)",
  ent="Baja California", mun="Tijuana (col. Genaro Vázquez)", dia="19-OCT, MADRUGADA",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS A UN ADOLESCENTE DE 17 AÑOS EN SU VIVIENDA",
  hecho="Tijuana · <code>COL. GENARO VÁZQUEZ, POR TITULAR; CALLE JAZMÍN ESQUINA GERANIO, SOLO POR RESUMEN</code> · LUNES 19-OCT, por ruta (Opinia) · ~02:38, " + RES + " · <b>1 adolescente de 17 años muerto</b> a balazos, por titulares (🟡) · tres hombres tocan a la puerta y uno dispara, por titular de Blanco y Negro y " + RES + " · detención: ARG-137-017 · identidad: no se reproduce · " + FR,
  panel="<b>Adolescente de 17 años asesinado</b> en su vivienda",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Opinia (2026/10/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="Genaro Vázquez no figura en las cinco ediciones previas ni en el índice. Detención: ARG-137-017."),
 dict(id="ARG-137-012", estado="MX-JAL", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="no fijada",
  ent="Jalisco", mun="Zapopan (col. El Zapote)", dia="18-OCT, DÍA SOLO POR RESUMEN",
  title="JALISCO · ZAPOPAN — ASESINAN A BALAZOS A UN HOMBRE EN EL ZAPOTE",
  hecho="Zapopan · <code>COL. EL ZAPOTE, POR TITULAR</code> · «este domingo 18 de octubre», " + RES + " · <code>RUTA SIN FECHA</code> · <b>1 hombre muerto</b> a balazos, por titular (🟡) · 32 años, al menos 5 impactos, afuera de una tienda; Cruz Verde confirmó el deceso, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada",
  panel="<b>1 hombre asesinado</b> a balazos",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; día solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-18, DÍA SOLO POR RESUMEN",
  desl="El Zapote no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-137-013", estado="MX-GRO", region="Sureste", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="~11:45, «después de las 12» o «la tarde» (solo por resumen; contradicho)",
  ent="Guerrero", mun="Acapulco (col. Héroes de Guerrero)", dia="18-OCT, DÍA SOLO POR RESUMEN",
  title="GUERRERO · ACAPULCO — MATAN A BALAZOS A UN HOMBRE EN LA COLONIA HÉROES DE GUERRERO",
  hecho="Acapulco · <code>COL. HÉROES DE GUERRERO, POR TITULAR DE AGENCIA IRZA; CALLE LÁZARO CÁRDENAS, SOLO POR RESUMEN</code> · «este domingo», " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · ~11:45, «después de las 12» o «la tarde», " + RES + ": <code>CONTRADICHO</code> · <b>1 hombre muerto</b> a balazos, por titulares (🟡) · perseguido y baleado, versiones extraoficiales, " + RES + " · <b>ningún detenido publicado</b> · sin identificar",
  panel="<b>1 hombre asesinado</b> a balazos",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día solo por resumen; hora contradicha; ninguna ruta con fecha", I=0, N=0, R=3, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-18, DÍA SOLO POR RESUMEN",
  desl="Héroes de Guerrero no figura en las cinco ediciones previas ni en el índice. NO es ARG-136-002 ni ARG-136-003 (sábado 17); las notas de «cinco muertos y tres heridos» suman estos tres hechos."),
 dict(id="ARG-137-014", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-19", hora="madrugada (solo por resumen)",
  ent="Michoacán", mun="Nuevo Parangaricutiro (San Juan Nuevo)", dia="19-OCT, MADRUGADA",
  title="MICHOACÁN · SAN JUAN NUEVO — ASESINAN A BALAZOS A UN CAMIONERO EN SAN JUAN NUEVO",
  hecho="San Juan Nuevo · LUNES 19-OCT, por ruta (tres medios) · madrugada, " + RES + " · <b>1 hombre muerto</b> a balazos: <b>camionero</b>, por titulares (🟡) · 25 años, en la cochera de su casa, " + RES + " · <b>ningún detenido publicado</b> · corporación: no publicada · identidad: no se reproduce · " + FR,
  panel="<b>1 camionero asesinado</b> a balazos",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; sin fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Grupo Marmor (2026/10/19)", "Red Michoacán (2026/10/19)", "MediaNews (2026/10/19)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Juan Nuevo no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-137-015", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="~21:00 (solo por resumen)",
  ent="Guanajuato", mun="Salamanca (Los Hernández)", dia="18-OCT, NOCHE, DÍA SOLO POR RESUMEN",
  title="GUANAJUATO · SALAMANCA — ATAQUE ARMADO A UNA CAMIONETA EN LOS HERNÁNDEZ: HERIDOS",
  hecho="Salamanca · <code>LOS HERNÁNDEZ, POR TITULAR</code> · DOMINGO 18-OCT, ~21:00, " + RES + " · <code>RUTA SIN FECHA</code> · ataque armado a una camioneta, por titular · <b>3 heridos</b>, " + RES + "; «deja heridos», por titular (🟡) · <b>ningún detenido publicado</b> · identidades: no publicadas",
  panel="Ataque a una camioneta: <b>heridos</b> (3, solo por resumen)",
  inst=SB, nac="Milenio", conf="★★☆☆☆",
  campo="una sola fuente; día, hora y número de heridos solo por resumen", I=0, N=1, R=0, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-18, DÍA SOLO POR RESUMEN",
  desl="Los Hernández no figura en las cinco ediciones previas ni en el índice. NO es ARG-136-001 (col. Guanajuato, 17-oct) ni ARG-133-002 (bulevar Valle de Santiago, 14-oct)."),
 dict(id="ARG-137-016", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-18", hora="tarde (solo por resumen)",
  ent="Michoacán", mun="Apatzingán (col. Buenos Aires)", dia="18-OCT, TARDE, DÍA SOLO POR RESUMEN",
  title="MICHOACÁN · APATZINGÁN — BALEAN A UNA PAREJA DENTRO DE UNA VIVIENDA DE LA COLONIA BUENOS AIRES",
  hecho="Apatzingán · <code>COL. BUENOS AIRES, POR TITULAR; CALLE JOSÉ MARÍA LAFRAGUA, SOLO POR RESUMEN</code> · tarde del DOMINGO 18-OCT, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · <b>una pareja baleada</b> dentro de un domicilio, por titulares (🟡) · <b>2 heridos</b> —un hombre y una mujer, 25 años—, hospitalizados, " + RES + "; «queda herida», en singular, por titular de Quadratín · Fiscalía Regional de Apatzingán recaba indicios, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque a una vivienda: <b>pareja baleada</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con fecha", I=0, N=0, R=3, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="2026-10-18, DÍA SOLO POR RESUMEN",
  desl="La colonia Buenos Aires de Apatzingán no figura en las cinco ediciones previas ni en el índice. NO es ARG-135-003 (El Varillero y Las Cahuingas)."),
 dict(id="ARG-137-017", estado="MX-BCN", region="Noroeste", color="verde", impacto="pequeno", fecha="2026-10-19", hora="no fijada",
  ent="Baja California", mun="Tijuana (col. Genaro Vázquez)", dia="19-OCT, HORA NO FIJADA",
  title="BAJA CALIFORNIA · TIJUANA — SEGÚN UN MEDIO, HAY UN DETENIDO TRAS EL HOMICIDIO DEL ADOLESCENTE DE GENARO VÁZQUEZ",
  hecho="Tijuana · <code>FECHA DE LA DETENCIÓN NO FIJADA; RUTA SIN FECHA</code> · <b>1 detenido</b>, por titular («hay un detenido») (🟢); Opinia (2026/10/19) no informa detenidos: <code>CONTRADICHO</code> · corporación y circunstancias de la detención: no publicadas · identidad y móvil: no publicados, " + RES + " · acusación, no condena · " + FR,
  panel="<b>1 detenido</b> por el homicidio del adolescente",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="detención sostenida por un titular; corporación no publicada", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None, fecha_txt="19-oct, posterior al homicidio de ~02:38 (ARG-137-011, hora solo por resumen); hora no fijada",
  desl="Delito: ARG-137-011."),
 dict(id="ARG-137-018", estado="MX-SON", region="Noroeste", color="verde", impacto="pequeno", fecha="2026-10-18", hora="~01:30 (solo por resumen)",
  ent="Sonora", mun="Hermosillo (col. Villa de Seris)", dia="PUB. 18-OCT, HORA NO FIJADA",
  title="SONORA · HERMOSILLO — DETIENEN A DOS «OBJETIVOS PRIORITARIOS» CON UNA PISTOLA 9 MM",
  hecho="Hermosillo · <code>COL. VILLA DE SERIS, SOLO POR RESUMEN</code> · publicado el DOMINGO 18-OCT, por ruta (El Imparcial) · ~01:30, " + RES + " · <b>2 detenidos</b>, «objetivos prioritarios», con <b>1 pistola 9 mm</b> y 40 envoltorios de presunto cristal, por titular (🟢) · un hombre de 32 años y una mujer de 23; Policía Preventiva, " + RES + " · acusación, no condena · " + AP,
  panel="<b>2 detenidos</b> con 1 pistola",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["El Imparcial (2026/10/18)"], estatus="Pendiente de corroboración", arm="ARG-137-ARM-003", fecha_txt="2026-10-18, hora no fijada",
  desl="Villas del Seris figura en ARG-134-012 (joven muerto, 15-oct): otro hecho.")
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-137-REC-001", estado="MX-GUA", region="Occidente", fecha="2026-10-17", hora="~05:00 o ~05:30 (solo por resumen)", orig="ARGOS 135 SI FUE ANTES DE LAS 09:28 DEL 17 (HORA SOLO POR RESUMEN); SI NO, ARGOS 136", col_orig="rojo",
  ent="Guanajuato", mun="Celaya (col. Gobernadores)", dia="17-OCT, MADRUGADA",
  title="GUANAJUATO · CELAYA — ASESINAN A BALAZOS A UNA AGENTE DE TRÁNSITO; UN CONDUCTOR HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 135 SI FUE ANTES DE LAS 09:28 DEL 17 (HORA SOLO POR RESUMEN); SI NO, ARGOS 136</code> · <code>COL. GOBERNADORES, POR TITULAR; CALLE BOCANEGRA (FRANCISCO O MANUEL) O ANASTASIO BUSTAMANTE, SOLO POR RESUMEN: CONTRADICHO</code> · madrugada del SÁBADO 17-OCT, " + RES + "; publicado el 17-OCT, por ruta · ~05:00 o ~05:30, " + RES + " · <b>1 mujer muerta</b>: <b>agente de Tránsito de Celaya</b> (Policía Vial, " + RES + "), por titulares; en su día de descanso, por titular de un medio; «iba a su trabajo», según otro, solo por resumen: <code>CONTRADICHO</code> (🔴 en su ventana) · <b>1 conductor herido</b>, por titulares · «motosicarios», por titular de La Silla Rota · el alcalde de Celaya pide no especular, por titular; la agente no había recibido amenazas, según el director de la corporación, por titular de Correo (2026/oct/19) · <b>ningún detenido publicado</b> · 26 o 27 años, " + RES + ": contradicho · identidad: no se reproduce",
  panel="<b>Agente de Tránsito asesinada</b>; 1 conductor herido", inst="Gobierno municipal de Celaya <span class=\"muted-note\">(por titular)</span>", nac="La Silla Rota · Milenio",
  conf="★★★☆☆", campo="hora solo por resumen; calle contradicha", I=1, N=2, R=6, A=0,
  fechadas=["La Silla Rota (2026/10/17)", "Periódico Correo (2026/oct/17)", "AM (2026/10/17)", "Noticieros en Línea (2026/oct/17)"],
  desl="La colonia Gobernadores y la víctima no figuran en las cinco ediciones previas ni en el índice; Celaya figura en ARG-136-001 solo como nombre de una calle de Salamanca."),
 dict(id="ARG-137-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-10-17", hora="no fijada (16 a 18-oct, solo por resumen)", orig="ARGOS 135 (16-OCT) Y 136 (17-OCT) — FECHAS SOLO POR RESUMEN; 18-OCT EN OTRO RESUMEN", col_orig="verde",
  ent="Sinaloa", mun="Mazatlán y El Rosario", dia="16-18 OCT · PUB. 18-OCT",
  title="SINALOA · MAZATLÁN Y EL ROSARIO — DETIENEN A «EL TALIBÁN» Y A CUATRO PRESUNTOS INTEGRANTES DE LOS CHAPITOS POR EL CASO DE LOS 10 MINEROS",
  hecho="<code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — VENTANAS DE ORIGEN: ARGOS 135 Y 136, FECHAS SOLO POR RESUMEN</code> · publicado el DOMINGO 18-OCT, por ruta (Proceso) · <b>5 detenidos</b> —«El Talibán» y cuatro presuntos integrantes de Los Chapitos—, por titular (🟢) · por <b>secuestro y homicidio de 10 mineros</b>, por titular · cuatro detenidos en El Rosario el 16-oct y «El Talibán» en Mazatlán el 17-oct, " + RES + "; el 18-oct en otro resumen: <code>CONTRADICHO</code> · Gabinete de Seguridad y Defensa informan; a disposición de la FGR, " + RES + " · armamento asegurado: no publicado · acusación, no condena · identidades: no se reproducen",
  panel="<b>5 detenidos</b> por el secuestro y homicidio de 10 mineros",
  inst=SB, nac="Proceso · Infobae · Político.mx", conf="★★★☆☆",
  campo="fecha de cada detención solo por resumen; sin comunicado oficial localizado", I=0, N=3, R=0, A=0,
  fechadas=["Proceso (2026/10/18)", "Infobae (2026/10/19)", "Político.mx (2026/10/19)"],
  desl="«El Talibán» y los 10 mineros no figuran en el índice. El Rosario figura en ARG-120-010, ARG-125-010 y ARG-126-005, y Concordia en ARG-126-004: otros hechos. NO es ARG-122-007 (ocho mineros, Sierra Pinta, Sonora). Fecha del secuestro y de los homicidios: no publicada.")
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
# integra=False: fila visible en la tabla, fuera del total (cifras solo por resumen; fecha del hecho no fijada)
ARM = [
 dict(id="ARG-137-ARM-001", ficha="ARG-137-ARM-001", estado="MX-NAY", region="Occidente", color="verde", ent="Nayarit", mun="Tecuala (San Felipe Aztatán y El Arrayán)", fecha="2026-10-18", hora="no fijada",
  fecha_txt="16 a 18-oct, no fijada", c=[0, 1, 0, 0, 0, 0, 1, 0, 0, 1], nd=[4, 5], corp="no publicada en el titular; Gabinete de Seguridad, solo por resumen del agregado", conf="Bajo",
  nota="EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL · por titular (NTV 2026/10/19): ametralladora, granada, «más de 11 mil cartuchos»: <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> y 1 detenido · 2 armas largas, 54 cargadores y 10,775 cartuchos en el boletín, solo por resumen · San Felipe Aztatán y El Arrayán no figuran; Tecuala figura en ARG-133-REC-007 (fosa de La Presa): otro hecho · republicadores no independientes", fuentes=["NTV (2026/10/19)", "Milenio (agregado 16-18 oct)"], integra=False),
 dict(id="ARG-137-ARM-002", ficha="ARG-137-ARM-002", estado="MX-VER", region="Golfo", color="verde", ent="Veracruz", mun="Lerdo de Tejada (col. José María Martínez Ruiz)", fecha="2026-10-18", hora="no fijada",
  fecha_txt="16 a 18-oct, no fijada", c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 2], nd=[0, 1, 4, 5], corp="Marina, Fiscalía y Policía Estatal (solo por resumen)", conf="Bajo",
  nota="EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL · 2 detenidos y «armas aseguradas», por titular (La Nigua) · 2 largas, 1 corta, 3 cargadores y 21 cartuchos, solo por resumen · POSIBLE DUPLICIDAD con el agregado semanal de cateos de Veracruz · «Sebastián Lerdo de Tejada» es una calle de Cd. Obregón (ARG-119-007): otro hecho", fuentes=["La Nigua", "Milenio (agregado 16-18 oct)"], integra=False),
 dict(id="ARG-137-ARM-003", ficha="ARG-137-018", estado="MX-SON", region="Noroeste", color="verde", ent="Sonora", mun="Hermosillo (col. Villa de Seris)", fecha="2026-10-18", hora="~01:30 (solo por resumen)",
  fecha_txt="publicado el 18-oct, hora no fijada", c=[1, 0, 0, 0, 0, 0, 0, 0, 0, 2], corp="Policía Preventiva (solo por resumen)", conf="No confirmado",
  nota="FUERA DEL TOTAL: una sola fuente (El Imparcial 2026/10/18, por titular)", fuentes=["El Imparcial (2026/10/18)"], integra=False),
]
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM if a["integra"]))
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
NFNF = sum(1 for e in E if "FECHA DEL HECHO NO FIJADA" in e["hecho"])
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], TOT
assert cnt == {"rojo": 6, "amarillo": 10, "verde": 2}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 0, "verde": 1}, cnt_rec
assert len(ENT) == 12, ENT
assert (NFR, NAP, NFNF) == (5, 6, 0), (NFR, NAP, NFNF)
assert len(set(e["id"] for e in E)) == len(E) and all(e["id"] == f"ARG-137-{i+1:03d}" for i, e in enumerate(E))

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
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
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 136 — Reporte Nacional de Seguridad — 2026-10-18</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE GUERRERO EL COMUNICADO OFICIAL Y LA HORA DEL ATAQUE</b> (ARG-137-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE TABASCO EL MUNICIPIO DEL HALLAZGO Y EL DESTINATARIO DE LOS MENSAJES</b> (ARG-137-005).
      <br><b>3. SOLICITE A LA PROCURADURÍA DE HIDALGO LA HORA DEL ATAQUE Y LA LÍNEA DE INVESTIGACIÓN</b> (ARG-137-006).
      <br><b>4. SOLICITE A LA FGR EL COMUNICADO DE LA ORDEN Y LA FECHA DE LA AUDIENCIA FEDERAL</b> (ARG-136-006).
      <br><b>5. SOLICITE AL GABINETE DE SEGURIDAD EL DESGLOSE Y LA FECHA DE CADA ASEGURAMIENTO</b> (ARG-137-ARM-001 y ARG-137-ARM-002).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>18-oct 08:34 → 19-oct 11:05 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,68 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>.
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
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Armas cortas</th><th>Armas largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos en aseguramiento</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{TOT[2]}</b></td><td><b>{TOT[3]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> · tres filas fuera del total (ARG-137-ARM-001 a -003), con 5 detenidos que no se suman a ningún total (1, 2 y 2).
    <b>Muertos en hechos propios</b>: <b>16</b> —Copanatoyac 2, Tlajomulco 2, Coatzacoalcos 2, Mazatlán 2, Tulancingo 1, Monterrey 1, Culiacán 1, Escuinapa 1, Tijuana 1, Zapopan 1, Acapulco 1 y San Juan Nuevo 1—; <b>7</b> de ellos con el día solo por resumen · <b>abatidos</b>: <b>2</b> (ARG-137-007) · <b>restos humanos</b>: 1 torso y restos en tres municipios, por titular de El Universal (ARG-137-005). <b>Heridos</b>: <b>8</b>, todos con el día solo por resumen —por titular: Copanatoyac 2 y Tlajomulco 1; solo por resumen: Salamanca 3 y Apatzingán 2—. <b>Detenidos sin aseguramiento</b>: <b>1</b> —ARG-137-017, contradicho—; los 5 de ARG-137-REC-002 no se recuentan. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-136-006, audiencia estatal el domingo 18: proceso en libertad y vinculación el jueves 22, por titular (La Razón 2026/10/18); la FGR lo detuvo con una orden federal por traición a la patria y lo trasladó al Altiplano, por titulares (La Jornada 2026/10/18, Infobae 2026/10/19); «vinculan a proceso» en el slug de La Jornada 2026/10/18: <code>CONTRADICHO</code> por la resolución aplazada al 22; la orden se anunció el 17-oct, por ruta (La Jornada, Proceso, Diario.mx); hora de la detención federal no fijada (sábado 17 en un receso o cerca de la medianoche del domingo), solo por resumen; no se recuenta · ARG-136-REC-002, ninguna autoridad nombrada confirma la adscripción de la víctima a la Guardia Nacional: amarillo en su ventana · ARG-136-009, «procesan a funcionario de Taxco», por titular (El Diario de Chihuahua 2026/oct/18); vinculación por un juez de control de Iguala, solo por resumen · ARG-136-007, a disposición de la Fiscalía de Puebla por homicidio, sin vinculación publicada, solo por resumen · ARG-135-REC-003, «van 10 cuerpos en tres días de búsqueda», por titular (Punto Norte 2026/10/18): <code>MISMO PREDIO NO VERIFICADO</code>; sin cifra oficial · ARG-135-010, la séptima persona sigue sin localizarse, por titular (Infobae 2026/10/18) · ARG-135-011, sin audiencia de vinculación publicada.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:6])
co3 = "\n".join(ficha(e) for e in E[6:11])
co4 = "\n".join(ficha(e) for e in E[11:16])
co5 = "\n".join(ficha(e) for e in E[16:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code> · 3 filas fuera del total"),
 tile(1, "Armas largas", TOT[1], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA EN HECHO PROPIO</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>NINGÚN DETENIDO EN EVENTO DE ASEGURAMIENTO</code>"),
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
    <div class="map-caption">Sin aseguramiento integrable en el corte; tres filas fuera del total.</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = f"<b>{c[9]}</b>" if c[9] else "0"
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
{chr(10).join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> — ningún aseguramiento con cantidad publicada y fecha del hecho o de publicación dentro de la ventana</td></tr>'}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: sin lectura (ninguna fila integrada). Filas atenuadas: <code>FUERA DEL TOTAL</code>.
    <br><code>VISTOS, NO INTEGRADOS</code>: Sinaloa, SSP, Culiacán, col. Industrial Bravo: 4 detenidos, por título del boletín; 1 ametralladora 7.62, 3 armas cortas y 420 cartuchos (385 de 7.62), solo por resumen; publicado el 16-oct, por ruta (Línea Directa, Tus Buenas Noticias) — <code>POSIBLE DUPLICIDAD CON ARG-135-ARM-001 — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · agregado del Gabinete de Seguridad del 16 al 18-oct, otros renglones, <code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code>: Sinaloa, Mazatlán, 3 detenidos con más de 1.5 toneladas de marihuana, por titular (Línea Directa 2026-10-19), armas y cartuchos contradichos entre resúmenes; Quintana Roo, Mahahual, 2 detenidos y 324 cartuchos, solo por resumen; Michoacán, Cotija, campamentos inhabilitados, solo por resumen · Veracruz, 33 cateos y 29 detenidos, por titular (Hora Cero 2026/10/19); «del 12 al 18-oct» y la atribución a la FGE, solo por resumen; armas sin cifra (agregado semanal, cualitativo).
    <br><b>Fe de erratas</b>: ARG-135-ARM-001, «417 cartuchos» retirada — sin fragmento citable en ARGOS 135 ni 136: <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">ninguna candidata nueva de la ventana</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>23 estatales revisadas</b>, 6 de lectura parcial · 9 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td colspan="6"><code>SIN CANDIDATA NUEVA EN LA VENTANA</code> — Ensenada (ARGOS 136): sin novedad; boletín no localizado en <code>fgebc.gob.mx</code>; sigue <code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code></td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Tamaulipas, Tribunal de Enjuiciamiento, sentencia por desaparición cometida por particulares, comunicado FGJE-370-2026 (ruta sin fecha; seis sentenciados y ~6-oct, solo por resumen) · Nayarit, 40 años por violación equiparada (8-oct, solo por resumen) · FGR Campeche, dos sentenciados por portación de arma (7-oct, solo por resumen) · Hidalgo, Tulantepec (tres culpables, fallo del 8-9 oct): individualización de la pena el miércoles 21-oct, solo por resumen.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>23 de 32</b>, de ellas <b>6 de lectura parcial</b> (Coah, indexado hasta agosto; SLP, sin consulta dedicada; Edomex, solo PDF antiguos; Tlax, un PDF de 2023; Mich, solo hasta enero de 2025; Chis, solo 2024-2025) · <b>FGR revisada: Sí</b>, por búsqueda · BC, BCS, Chih, Dgo · Coah, NL, Tamps, SLP · Jal, Col, Nay, Mich, Ags · CDMX, Edomex, Pue, Tlax, Qro · Ver, Tab · Chis, Oax, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0 por boletín leído</b> · ninguna candidata nueva de la ventana</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>23</b> fiscalías estatales, 6 de lectura parcial</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>9</b>: Son, Sin · Zac · Gto · Mor, Hgo · Gro, Camp, Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>gob.mx/fgr</code> devolvió <code>000</code> a las 11:05 del 19-oct; 0 errores en los demás dominios consultados · <b>dominios no devueltos por el buscador</b>, dentro de las 9 <code>NO REVISADA</code>: Sin, Mor, Hgo, Gto, Camp</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 22 de 32 con consulta propia por entidad</b> · <b>8 solo por consulta regional amplia</b>: BCS, Dgo · Coah · Edomex, Tlax, Qro · Chis, Oax · <code>NO REVISADA</code>: Camp, Yuc · <b>armamento: 9 de 32 por dominio propio de seguridad</b> —Sin · SLP, Zac · Nay, Mich, Gto · Camp, Yuc, QRoo—, de ellas <b>4 de lectura parcial</b> (Nay, solo organigrama; Gto, una página; QRoo, solo informes; Yuc, sin fecha clara); <b>5 por portal del gobierno estatal</b> —Coah, Tamps, Ver, Tab, Oax—; <code>NO REVISADA</code> (18): BC, BCS, Son, Chih, Dgo · NL · Jal, Col, Ags · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Gro, Chis</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 16, 17 y 18-oct</b>: agregado de tres días, solo por republicadores (consulta por título, sin <code>site:</code>); por día suelto y por rango en el dominio: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <b>acciones del 19-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <b>Guardia Nacional y FGR</b>: SRIV (con <code>site:</code>) · <b>Defensa y Marina</b>: SRIV (consulta sin <code>site:</code>); búsqueda federal del equipo Golfo; Noroeste y Occidente: <code>NO REALIZADA</code> · <b>gabinetedeseguridad.gob.mx</b>: SRIV (indexado hasta marzo de 2026)</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 19-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR SEIS ROJOS</b>: ARG-137-001 a ARG-137-006 · <b>reserva</b> en ARG-137-001, ARG-137-002 y ARG-137-005.
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-137-007 a ARG-137-016.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-137-017 y ARG-137-018.
      <br><b>4.</b> <b>Ventanas anteriores</b>: ARG-137-REC-001 y ARG-137-REC-002.
      <br><b>5.</b> <code>26 H 31 MIN; ONCE DE DIECIOCHO CON MARCA DE FRONTERA (5 DE CIERRE, 6 DE APERTURA) Y OTROS SEIS SIN RUTA CON FECHA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. SINALOA, TRES HECHOS CON MUERTOS EL 18-OCT</b> (cálculo propio; hora de ARG-137-004 y ARG-137-010 no fijada; día de ARG-137-009 solo por resumen). ARG-137-004, -009 y -010 se suman a ARG-136-004 y a ARG-135-001 y ARG-135-007. Línea: <b>solicitar a la FGE Sinaloa el cotejo balístico entre Culiacán, Mazatlán y Escuinapa</b> — hipótesis; vínculo no acreditado.
      <br><b>2. ACAPULCO, TERCER HECHO CON MUERTOS EN DOS DÍAS</b> (cálculo propio; días solo por resumen). ARG-137-013 se suma a ARG-136-002 y ARG-136-003. Línea: <b>solicitar a la FGE Guerrero si las tres carpetas comparten indicios</b> — vínculo no acreditado.
      <br><b>3. COLIMA, LOS MEZCALES: DOS PRESUNTOS OPERADORES (ATRIBUCIÓN DE MEDIOS) ABATIDOS TRAS DOS DETENCIONES DE AGOSTO (UN PRESUNTO SICARIO Y UN SEGUNDO AL MANDO)</b> (cálculo propio). ARG-137-007 se suma a ARG-104-005 y ARG-105-003; atribución de operadores por medios. Línea: <b>solicitar a la Mesa de Seguridad de Colima el armamento asegurado y los peritajes</b>.
      <br><b>4. SALAMANCA, TERCER ATAQUE ARMADO EN CINCO DÍAS (14, 17 Y 18-OCT)</b> (cálculo propio; día de ARG-137-015 solo por resumen). ARG-137-015 se suma a ARG-133-002 y ARG-136-001. Línea: <b>solicitar a la FGE Guanajuato el cotejo de casquillos entre los tres ataques</b> — hipótesis.
      <br><b>5. APATZINGÁN, CUARTO HECHO VIOLENTO ENTRE EL 13 Y EL 18-OCT</b> (cálculo propio; día de ARG-137-016 solo por resumen). ARG-137-016 se suma a ARG-135-003, ARG-135-004 y ARG-134-REC-003. Línea: <b>solicitar a la Fiscalía Regional de Apatzingán el cotejo de indicios</b> — hipótesis.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code> (indexado hasta marzo de 2026); lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>gob.mx/fgr</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: GUERRERO, JALISCO Y VERACRUZ", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: SINALOA, TABASCO E HIDALGO", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA", co3)
 + page("CRIMEN ORGANIZADO (IV) — VIOLENCIA OPERATIVA", co4)
 + page("CRIMEN ORGANIZADO (V) — ACCIONES INSTITUCIONALES", co5)
 + page("CRIMEN ORGANIZADO (VI) — VENTANAS ANTERIORES: ARGOS 135 Y 136", rec1)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if a["integra"] and any(a["c"]))
script = script.replace('"<br>Consulta: " + (top.fecha || "—") + " " + (top.hora || "")', '"<br>Fecha y hora (hecho o publicación): " + (top.fecha || "—") + " " + (top.hora || "") + "<br>Consulta: " + CONSULTA_TXT')
if "const CONSULTA_TXT" in script:
    script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
else:
    script = script.replace("const CORTE_FECHA", f'const CONSULTA_TXT = "{CONSULTA}";\nconst CORTE_FECHA', 1)
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert "WINDOW_DAYS = 2;" in script  # la ventana 18-oct 08:34 → 19-oct 11:05 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
