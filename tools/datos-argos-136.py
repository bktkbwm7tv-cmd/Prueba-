# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 136: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-136.py <plantilla ARGOS 135> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "136", "2026-10-18", "08:34"
CONSULTA = "2026-10-18 08:34-10:00"
DUR = "23 h 06 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA: PUEDE SER ANTERIOR A LAS 09:28 DEL 17</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-136-001", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-17", hora="~17:30 (solo por resumen)",
  ent="Guanajuato", mun="Salamanca (col. Guanajuato)", dia="17-OCT, TARDE",
  title="GUANAJUATO · SALAMANCA — ASESINAN A BALAZOS A DOS HOMBRES EN LA COLONIA GUANAJUATO",
  hecho="Salamanca · <code>COL. GUANAJUATO, POR TITULAR; CALLE DOLORES HIDALGO CASI ESQUINA COMONFORT (AM) O CRUCE CELAYA–COMONFORT (MILENIO, EL SALMANTINO): CONTRADICHO, SOLO POR RESUMEN</code> · publicado el SÁBADO 17-OCT, por ruta (AM); hecho el mismo día por la hora ~17:30, dos medios coinciden, " + RES + " · varios hombres armados disparan y huyen, " + RES + " · <b>2 hombres muertos</b> a balazos, por titular (🔴) · uno muere en el sitio pese a la atención de paramédicos, " + RES + " · Agencia de Investigación Criminal de la FGE Guanajuato alertada para el peritaje, " + RES + " · <b>ningún detenido publicado</b> · armamento no publicado · identidades: no publicadas",
  panel="Ataque armado: <b>2 hombres muertos</b>",
  inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="día del hecho y hora solo por resumen; esquina contradicha; sin fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["AM (2026/10/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="La colonia Guanajuato no figura en las cinco ediciones previas ni en el índice. NO es ARG-133-002 (bulevar Valle de Santiago, 14-oct) ni ARG-136-REC-001 (Silao)."),
 dict(id="ARG-136-002", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-17", hora="~17:30 o ~18:00 (solo por resumen; versiones distintas)",
  ent="Guerrero", mun="Acapulco (col. Cuauhtémoc, parte alta)", dia="17-OCT, TARDE, DÍA SOLO POR RESUMEN",
  title="GUERRERO · ACAPULCO — ATAQUE ARMADO EN LA COLONIA CUAUHTÉMOC: DOS MUERTOS Y TRES HERIDOS",
  hecho="Acapulco · <code>COL. CUAUHTÉMOC, POR TITULAR; PARTE ALTA, CALLE 10 CERCA DE VICENTE GUERRERO, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · ~17:30 o ~18:00, " + RES + ", versiones distintas · hombres a bordo de un taxi disparan al menos 20 veces contra personas en un negocio de comida, " + RES + " · <b>2 hombres muertos</b> —uno en el lugar y otro durante el traslado— y <b>3 heridos</b>, por titular (🔴) · <code>4 HERIDOS EN EL CUERPO DE UNA NOTA: CONTRADICHO</code> · FGE Guerrero, Semefo, Policía Estatal y Guardia Nacional en la escena, " + RES + " · los agresores huyen · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos y 3 heridos</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con fecha", I=0, N=0, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="La colonia Cuauhtémoc de Acapulco no figura en las cinco ediciones previas. <code>NO ES</code> el ataque homónimo en la misma colonia con 3 muertos y 2 heridos (noviembre de 2025, solo por resumen). NO es ARG-136-003 (col. Vicente Guerrero, ~19:00)."),
 dict(id="ARG-136-003", estado="MX-GRO", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-17", hora="~19:00 (solo por resumen)",
  ent="Guerrero", mun="Acapulco (col. Vicente Guerrero)", dia="17-OCT, NOCHE, DÍA SOLO POR RESUMEN",
  title="GUERRERO · ACAPULCO — HALLAN A DOS PERSONAS ASESINADAS CON HUELLAS DE TORTURA",
  hecho="Acapulco · <code>COL. VICENTE GUERRERO; CALLES RAYMUNDO OLIVAR E IGNACIO ALLENDE, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, ~19:00, " + RES + " · <code>NINGUNA RUTA CON FECHA</code> · <b>2 personas asesinadas</b> con <b>huellas de tortura</b>, por titular (🔴); hombres, " + RES + " · uno atado y con torniquete; otro envuelto en una sábana, " + RES + " · policías ministeriales, Guardia Nacional y Marina; peritos de la FGE Guerrero y Semefo, " + RES + " · <b>ningún detenido publicado</b> · identidades: no publicadas",
  panel="Hallazgo de <b>2 personas asesinadas con huellas de tortura</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; día, hora y colonia solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="La colonia Vicente Guerrero de Acapulco no figura en las cinco ediciones previas ni en el índice. NO es ARG-136-002 (col. Cuauhtémoc) ni el hallazgo de un cuerpo en la misma calle del 15-oct (solo por resumen) ni Zihuatanejo, col. Vicente Guerrero (13-oct, no publicado)."),
 dict(id="ARG-136-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-17", hora="minutos antes de la medianoche del sábado (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (col. Estela Ortiz o Ruiz Cortines)", dia="17-OCT, NOCHE · PUB. 18-OCT",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS A UN JOVEN DENTRO DE UNA TIENDA DE CONVENIENCIA; COLONIA CONTRADICHA",
  hecho="Culiacán · <code>COL. ESTELA/ESTHELA ORTIZ, POR TITULAR (LUZ NOTICIAS, NOROESTE, CAFÉ NEGRO, EL SOL DE SINALOA); COL. RUIZ CORTINES, POR TITULAR (LÍNEA DIRECTA, LOS NOTICIERISTAS): CONTRADICHO; CRUCE FERNANDO CUÉN Y PABLO MACÍAS VALENZUELA, SOLO POR RESUMEN</code> · noche del SÁBADO 17-OCT, minutos antes de la medianoche, " + RES + "; «madrugada de este domingo», " + RES + "; publicado el DOMINGO 18-OCT, por ruta · <b>1 hombre muerto</b> a balazos dentro de una tienda de conveniencia, por titular (🟡) · empleado de la tienda, por titulares; 20 años, por titular · agentes ministeriales en la escena, " + RES + " · asalto o ataque directo: no determinado, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 joven asesinado</b> dentro de una tienda",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="colonia contradicha; hora solo por resumen; sin fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Luz Noticias (2026-10-18)", "Línea Directa (2026-10-18)"], estatus="Parcialmente corroborado", arm=None,
  desl="Estela Ortiz y Ruiz Cortines no figuran en las cinco ediciones previas ni en el índice. NO es el homicidio de abril de 2026 en una de las dos colonias (colonia a precisar, solo por resumen)."),
 dict(id="ARG-136-005", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-17", hora="aviso al 911 ~09:30 (solo por resumen)",
  ent="Baja California", mun="Ensenada (Maneadero)", dia="17-OCT, MAÑANA, HORA SOLO POR RESUMEN",
  title="BAJA CALIFORNIA · ENSENADA — LOCALIZAN UN CUERPO CON SIGNOS DE VIOLENCIA CERCA DE UN ARROYO DE MANEADERO",
  hecho="Ensenada · <code>MANEADERO, CERCA DE UN ARROYO, POR TITULAR</code> · SÁBADO 17-OCT, aviso al 911 ~09:30, " + RES + " · <code>ZETA: RUTA SOLO CON AÑO Y MES</code> · <b>1 cuerpo con signos de violencia</b>, por titular (🟡) · envuelto en una cobija, con golpes en el cráneo, " + RES + " · <code>CAUSA DE MUERTE NO DETERMINADA</code> · FGE Baja California a cargo, " + RES + " · <b>ningún detenido publicado</b> · sin identificar · " + AP,
  panel="Hallazgo de <b>1 cuerpo con signos de violencia</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día y hora solo por resumen; ninguna ruta con día", I=0, N=0, R=2, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Maneadero figura en el índice por ARG-105-REC-005 (detención, ventana de ARGOS 95) y por ARG-120-019 (seis detenidos, 14-sep): otros hechos."),
 dict(id="ARG-136-006", estado="MX-CHH", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-17", hora="~10:20 según el Registro Nacional de Detenciones; ~10:00 en otra versión (solo por resumen)",
  ent="Chihuahua", mun="Chihuahua", dia="17-OCT, MAÑANA",
  title="CHIHUAHUA · CHIHUAHUA — DETIENEN AL EXFISCAL DE CHIHUAHUA POR EL OPERATIVO CON AGENTES DE LA CIA",
  hecho="Chihuahua capital · <code>AV. CANTERA, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, por ruta · ~10:20, según el Registro Nacional de Detenciones, por titular de Radionet; hora " + RES + "; ~10:00 en otra versión · <b>1 detenido</b>: el <b>exfiscal de Chihuahua</b>, por titular; titular de la Fiscalía General del Estado hasta abril, " + RES + " (🟢) · orden de aprehensión por <b>ejercicio ilegal del servicio público y coalición</b>, por titular de UnoTV; el fiscal general del estado informó la orden, por cita; librada por un juez de control, " + RES + " · causa penal 3055/2026 y orden del 16-oct, " + RES + " · ministeriales y policías estatales, " + RES + " · investigación por el operativo con agentes de la CIA y la muerte de agentes de la CIA, por titulares (Informador, Forbes); dos agentes, " + RES + "; abril de 2026 y El Pinal (Morelos, Chih.), " + RES + " · la FGR le atribuye posible <b>traición a la patria</b>, por titulares de Expansión y La Silla Rota; sin comunicado de la FGR localizado · orden también contra un exfiscal especial, " + RES + " · acusación, no condena",
  panel="<b>Exfiscal de Chihuahua detenido</b>",
  inst="Fiscalía de Chihuahua <span class=\"muted-note\">(por cita)</span>", nac="Proceso · El Financiero · La Jornada · CNN en Español · Expansión · Infobae · La Razón · Publimetro · La Silla Rota · Politico.mx · Reforma · Excélsior · UnoTV", conf="★★★☆☆",
  campo="hora solo por resumen; declaración de la Fiscalía solo por cita", I=1, N=13, R=4, A=0,
  fechadas=["Proceso (2026/10/17)", "El Financiero (2026/10/17)", "La Jornada (2026/10/17)", "CNN en Español (2026/10/17)", "Expansión (2026/10/17)", "Infobae (2026/10/17)", "La Razón (2026/10/17)", "Publimetro (2026/10/17)", "La Silla Rota (2026/10/17)", "Politico.mx (2026/10/17)", "Luz Noticias (2026-10-17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Hecho de origen de abril de 2026, solo por resumen, fuera de las cinco ediciones previas. Armamento asegurado: no publicado"),
 dict(id="ARG-136-007", estado="MX-PUE", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-17", hora="detención no fechada; publicada el 2026-10-17",
  ent="Puebla", mun="Puebla (San Pedro Zacachimalpa)", dia="PUB. 17-OCT, HORA NO FIJADA",
  title="PUEBLA · PUEBLA — DETIENEN A PRESUNTOS RESPONSABLES DEL ATAQUE EN SAN BALTAZAR TETELA EN EL QUE MURIÓ UN NIÑO",
  hecho="Puebla capital · <code>SAN PEDRO ZACACHIMALPA, CALLE HERMANOS SERDÁN, SOLO POR RESUMEN</code> · publicado el SÁBADO 17-OCT, por ruta · <b>2 detenidos</b>, por titulares (🟢); «detiene a sicario», en singular, por titular de otro medio: <code>CONTRADICHO</code> · de 18 y 22 años, " + RES + " · Policía Estatal (SSC Puebla), " + RES + "; policía municipal, según otro medio: <code>CONTRADICHO</code> · señalados por el ataque de la madrugada del 17 en la junta auxiliar San Baltazar Tetela, " + RES + ", en el que murió un niño de 2 años y su padre resultó herido, por titulares · en videovigilancia, uno entrega un arma a un tercero, " + RES + " · armamento asegurado: no publicado · móvil: no aclarado, " + RES + " · identidades: no se reproducen · " + AP,
  panel="<b>2 detenidos</b> por titulares (1 en otro medio) por el ataque de San Baltazar Tetela",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="hora de la detención no fijada; número y corporación contradichos; sin fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Paralelo19 (2026/10/17)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicada el 2026-10-17",
  desl="San Pedro Zacachimalpa y San Baltazar Tetela no figuran en las cinco ediciones previas ni en el índice. Ataque: ventana de ARGOS 135. Armamento asegurado: no publicado"), dict(id="ARG-136-008", estado="MX-GRO", region="Sureste", color="verde", impacto="pequeno", fecha="2026-10-17", hora="detención no fechada; publicada el 2026-10-17",
  ent="Guerrero", mun="Taxco de Alarcón (detención en Maravatío, Michoacán)", dia="PUB. 17-OCT, HORA NO FIJADA",
  title="GUERRERO · TAXCO — DETIENEN A UN PRESUNTO INTEGRANTE DE LA FAMILIA MICHOACANA POR EL HOMICIDIO DE SEIS POLICÍAS",
  hecho="Detención en Maravatío de Ocampo, Michoacán, " + RES + " · publicado el SÁBADO 17-OCT, por ruta · boletín de la FGE Guerrero la noche del 16, " + RES + " · <b>1 detenido</b>, presunto integrante de La Familia Michoacana, por titular (🟢) · orden de aprehensión por el <b>homicidio de 6 policías</b> en Taxco, por titular; estatales, " + RES + " · emboscada del 21-jun-2020 en la carretera Taxco–Tetipac, " + RES + "; 22-jun en otra fuente · FGE Guerrero con la Fiscalía de Michoacán, Defensa y Guardia Nacional, " + RES + " · fecha de la detención: no publicada · acusación, no condena · alias e identidad: no se reproducen · " + AP,
  panel="<b>1 detenido</b> por el homicidio de 6 policías",
  inst=SB, nac="Milenio · N+ · La Silla Rota", conf="★★☆☆☆",
  campo="fecha de la detención no publicada; boletín solo por resumen", I=0, N=3, R=3, A=0,
  fechadas=["La Silla Rota (2026/10/17)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no publicada; publicada el 2026-10-17",
  desl="El detenido no figura en las cinco ediciones previas ni en el índice; Taxco figura solo como ranchería de Nacajuca (ARG-130-003). Hecho de origen de 2020, solo por resumen. Armamento asegurado: no publicado"),
 dict(id="ARG-136-009", estado="MX-GRO", region="Sureste", color="verde", impacto="pequeno", fecha="2026-10-17", hora="16 o 17-oct (solo por resumen; contradicho)",
  ent="Guerrero", mun="Taxco de Alarcón (centro)", dia="PUB. 17-OCT, HORA NO FIJADA",
  title="GUERRERO · TAXCO — DETIENEN AL DIRECTOR DE REGLAMENTOS DEL AYUNTAMIENTO POR EL SECUESTRO DEL PADRE DEL ALCALDE",
  hecho="Taxco de Alarcón · detención el VIERNES 16-OCT en el centro, según un medio, " + RES + "; 17-OCT, según otra versión, " + RES + ": <code>CONTRADICHO</code> · publicado el SÁBADO 17-OCT, por ruta · <b>1 detenido</b>: el <b>director de Reglamentos</b> del ayuntamiento, por titular (🟢) · orden de aprehensión por <b>secuestro agravado</b> del padre del alcalde (11-abr-2026), " + RES + " · la FGE Guerrero lo señala como integrante de La Familia Michoacana, " + RES + " · <code>UN POLICÍA DETENIDO EN EL MISMO DISPOSITIVO, SOLO EN UN MEDIO: NO SE INTEGRA</code> · fuerzas federales y estatales, " + RES + " · acusación, no condena · identidad: no se reproduce · " + AP,
  panel="<b>Director de Reglamentos detenido</b> por secuestro",
  inst=SB, nac="Proceso · El Universal · Milenio · UnoTV · La Jornada", conf="★★☆☆☆",
  campo="fecha de la detención contradicha; declaración de la Fiscalía solo por resumen", I=0, N=5, R=3, A=0,
  fechadas=["Proceso (2026/10/17)", "La Jornada (2026/10/18)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="16 o 17-oct, contradicho; publicada el 2026-10-17",
  desl="Reglamentos de Taxco no figura en las cinco ediciones previas ni en el índice. NO es ARG-136-008. Armamento asegurado: no publicado")
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-136-REC-001", estado="MX-GUA", region="Occidente", fecha="2026-10-17", hora="~06:30 (aviso al 911) o ~07:20 (solo por resumen; versiones distintas)", orig="ARGOS 135 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="Guanajuato", mun="Silao (Baños de Agua Caliente)", dia="17-OCT, MAÑANA",
  title="GUANAJUATO · SILAO — ASESINAN A UN HOMBRE Y A UNA MUJER DENTRO DE UNA VIVIENDA EN BAÑOS DE AGUA CALIENTE",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 135 — HORA SOLO POR RESUMEN</code> · <code>COMUNIDAD BAÑOS DE AGUA CALIENTE, POR TITULAR; CALLE LA LUZ, CERCA DE COMANJILLA, SOLO POR RESUMEN</code> · mañana del SÁBADO 17-OCT, " + RES + "; publicado el 17-OCT, por ruta · ~06:30 (aviso al 911) o ~07:20, " + RES + ", versiones distintas · <b>1 hombre y 1 mujer muertos</b> a balazos dentro de una vivienda, por titular (🔴 en su ventana) · el agresor huye en un vehículo, " + RES + " · Unidad de Homicidios de la FGE Guanajuato a cargo, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Hombre y mujer asesinados</b> en su vivienda", inst=SB, nac="Milenio",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["AM (2026/10/17)"],
  desl="Baños de Agua Caliente y Comanjilla no figuran en las cinco ediciones previas ni en el índice. NO es ARG-134-001 (Barrio Nuevo) ni ARG-133-REC-002 (Veta de Ramales) ni ARG-133-REC-003 (col. Sopeña): otra localidad, otras víctimas y otra fecha."),
 dict(id="ARG-136-REC-002", estado="MX-SLP", region="Noreste", fecha="2026-10-15", hora="noche del jueves, ~21:00 (solo por resumen)", orig="ARGOS 134 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="San Luis Potosí", mun="Tanquián de Escobedo (centro)", dia="15-OCT, NOCHE",
  title="SAN LUIS POTOSÍ · TANQUIÁN DE ESCOBEDO — ASESINAN A BALAZOS A UN HOMBRE REPORTADO COMO ELEMENTO DE LA GUARDIA NACIONAL",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 134 — HORA SOLO POR RESUMEN</code> · <code>CENTRO, CALLE VICENTE GUERRERO, SOLO POR RESUMEN</code> · noche del JUEVES 15-OCT, ~21:00, " + RES + "; publicado el 16-OCT, por ruta · <b>1 hombre muerto</b> a balazos, <b>elemento de la Guardia Nacional</b> según dos titulares (🔴 en su ventana) · <code>ADSCRIPCIÓN CONTRADICHA: GUARDIA NACIONAL EN DÍAS DE DESCANSO O EXAGENTE DE LA GUARDIA CIVIL ESTATAL, SOLO POR RESUMEN; «INVESTIGAN SI PERTENECÍA», POR TITULAR DE LA OPINIÓN</code> · circulaba en motocicleta, " + RES + " · agresores con armas largas, por titular de Pulso · veracruzano, por titular de La Opinión; originario de Tempoal, " + RES + " · FGE San Luis Potosí a cargo, " + RES + " · <b>ningún detenido publicado</b>, " + RES + " · identidad: no se reproduce",
  panel="<b>Hombre asesinado</b>, reportado como elemento de la Guardia Nacional", inst=SB, nac="N+ (titular: Guardia Nacional) · Milenio (adscripción no confirmada)",
  conf="★★☆☆☆", campo="adscripción de la víctima contradicha; hora solo por resumen", I=0, N=2, R=7, A=0,
  fechadas=["Potosinoticias (2026/10/16)"],
  desl="Tanquián no figura en las cinco ediciones previas ni en el índice; Tempoal (ARG-116-005, ARG-122-011) es otro hecho. <code>ADSCRIPCIÓN NO CONFIRMADA: COLOR PENDIENTE</code>"), dict(id="ARG-136-REC-003", estado="MX-CHH", region="Noroeste", fecha="2026-10-17", hora="~09:00 (solo por resumen)", orig="ARGOS 135 — HORA SOLO POR RESUMEN", col_orig="rojo",
  ent="Chihuahua", mun="Cuauhtémoc (campo menonita)", dia="17-OCT, MAÑANA",
  title="CHIHUAHUA · CUAUHTÉMOC — ENCUENTRAN DOS CUERPOS EN UNA CAMIONETA EN UN CAMPO MENONITA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 135 — HORA SOLO POR RESUMEN</code> · <code>CAMPO MENONITA, POR TITULAR; CAMPO 34, CALLE MANITOBA, SOLO POR RESUMEN</code> · SÁBADO 17-OCT, ~09:00, " + RES + "; publicado el 17-OCT, por ruta · «viernes» en un medio: <code>DÍA CONTRADICHO</code> · <b>2 cuerpos</b> en una camioneta, por titular; «dos ejecutados», por titular de otro medio (🔴 en su ventana) · heridas de bala en la cabeza, según la Fiscalía, " + RES + " · camioneta sin placas, " + RES + " · <b>ningún detenido publicado</b> · identidades: no publicadas",
  panel="Hallazgo de <b>2 cuerpos</b> en una camioneta", inst=SB, nac=NIN,
  conf="★★☆☆☆", campo="hora solo por resumen; día contradicho en un medio; independencia entre las tres rutas no verificada", I=0, N=0, R=3, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/17)", "diario.mx (2026/oct/17)", "El Diario del Noroeste (2026/oct/17)"],
  desl="Campo menonita 34 y calle Manitoba no figuran en las cinco ediciones previas ni en el índice. NO es ARG-125-004 ni ARG-128-REC-007 (Cuauhtémoc, Chih.). Reserva: si la hora fuera posterior a las 09:28, es hecho del corte.")
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = []
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
assert TOT == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], TOT
assert cnt == {"rojo": 3, "amarillo": 2, "verde": 4}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert len(ENT) == 6, ENT
assert NFR == 1, NFR

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
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"]}

def arm_json(a):
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 135 — Reporte Nacional de Seguridad — 2026-10-17</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE GUANAJUATO LA IDENTIFICACIÓN DE LAS VÍCTIMAS Y LA HORA DEL ATAQUE</b> (ARG-136-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE GUERRERO EL NÚMERO OFICIAL DE LESIONADOS Y EL DÍA DEL ATAQUE</b> (ARG-136-002).
      <br><b>3. SOLICITE A LA FISCALÍA DE NAYARIT LA FECHA DE LA AUDIENCIA DE VINCULACIÓN DEL POLICÍA IMPUTADO</b> (ARG-135-011).
      <br><b>4. SOLICITE A LA FISCALÍA DE CHIHUAHUA LA FECHA DE LA AUDIENCIA INICIAL Y EL COTEJO DE LA HORA REGISTRADA DE LA DETENCIÓN</b> (ARG-136-006).
      <br><b>5. SOLICITE A LA FISCALÍA DE SAN LUIS POTOSÍ LA ADSCRIPCIÓN DE LA VÍCTIMA</b> (ARG-136-REC-002).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>17-oct 09:28 → 18-oct 08:34 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,39 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>.
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
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> · ningún aseguramiento con cantidad publicada y fecha dentro de la ventana.
    <b>Muertos en hechos propios</b>: <b>8</b> —Salamanca 2, Acapulco 2 + 2, Culiacán 1 y Ensenada 1— (<b>7</b> sin Ensenada: causa de muerte no determinada). <b>Heridos: 3</b> en ARG-136-002, por titular (<b>4</b> en el cuerpo de una nota: contradicho). <b>Detenidos sin aseguramiento</b>: <b>5</b> —ARG-136-006, 1; ARG-136-007, 2 (1 en otro medio: contradicho); ARG-136-008, 1; ARG-136-009, 1— (<b>4</b> si en Puebla fue 1; ARG-136-007 a -009 publicados el día de apertura sin hora). <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-135-REC-004, «siete hallazgos en cinco fosas durante dos días», por titular (El Imparcial 2026/10/17) · ARG-135-REC-003, «6 cuerpos y osamentas apilados», por titular (Punto Norte 2026/10/17); 4 cuerpos y 2 esqueletos, solo por resumen; sin cifra oficial · ARG-135-010, la séptima persona sigue sin localizarse, por titular (Infobae 2026/10/18) · ARG-135-011, imputado, por titular (Meridiano 2026/10/17); audiencia de vinculación «la próxima semana», solo por resumen.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:5])
co3 = "\n".join(ficha(e) for e in E[5:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"),
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
    <div class="map-caption">Sin aseguramiento integrable en el corte.</div>
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
{chr(10).join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> — ningún aseguramiento con cantidad publicada y fecha del hecho o de publicación dentro de la ventana</td></tr>'}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: sin lectura (ninguna fila integrada).
    <br><code>VISTOS, NO INTEGRADOS</code>: Sinaloa, SSP, Culiacán: 4 detenidos, por título del boletín; col. Industrial Bravo y 1 ametralladora 7.62, solo por resumen; fecha no fijada — <code>POSIBLE DUPLICIDAD CON ARG-135-ARM-001 — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · Puebla, Chignahuapan, cateos con apoyo de Marina, por titular (Excélsior, ruta sin fecha); seis cateos, 9 detenidos y 1 arma, solo por resumen; sin fecha fijada · Sinaloa, SSP, ejido Canán, 1 fusil, publicado el 16-oct, solo por resumen.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">1 candidata sin confirmar (Ensenada)</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>17 estatales revisadas</b>, 4 de lectura parcial · 15 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Tres sentenciados, nombres no reproducidos · <span class="muted-note">homicidio calificado de tres surfistas (abril de 2024), robo calificado con violencia y robo de vehículo con violencia, solo por resumen</span></td><td><b>158 años 9 meses</b> a cada uno: 135 años + 10 años 9 meses + 13 años, solo por resumen · reparación: 1,628,550 pesos y 19,542 por gastos funerarios, solo por resumen · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>FGE Baja California <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · boletín no localizado en <code>fgebc.gob.mx</code> · Infobae 2026/10/17 · miled 2026/10/17 · seguimiento de la candidata de ARGOS 135 · firmeza no informada</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Veracruz, 21 años por el homicidio de un comunicador, por titular de La Política en Rosa (15-oct, sin boletín; causa J-10/2026, solo por resumen) · FGR Cosoleacaque, 4 años, por titular de Hora Cero, y Banderilla, 2 años 6 meses, solo por resumen (15-oct, sin boletín) · FGE Guerrero, cinco sentencias —Acapulco, Huitzuco, Iguala dos y Tlapehuala— (15-oct, solo por resumen) · Hermosillo, 25 años, solo por resumen (16-oct) · Mesa de Coordinación de Guerrero, 11 sentencias en la semana del 5 al 11-oct, solo por resumen (agregado, sin caso) · Hidalgo, Tulantepec: individualización de la pena el 21-oct, solo por resumen.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>17 de 32</b>, de ellas <b>4 de lectura parcial</b> (Son, solo convocatorias; Tlax, sin boletines; SLP, boletines sin fecha; Nay, consulta indirecta) · <b>FGR revisada: Sí</b>, por búsqueda · BC, Son, Chih · Coah, NL, Tamps, SLP, Zac · Mich, Nay, Ags · CDMX, Tlax · Ver, Tab · Gro, Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0 por boletín leído</b> · ninguna candidata nueva de la ventana</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>17</b> fiscalías estatales, 4 de lectura parcial</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>15</b>: BCS, Sin, Dgo · Jal, Col, Gto · Edomex, Mor, Pue, Hgo, Qro · Oax, Chis, Camp, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: dominios <code>*.gob.mx</code> (403 del proxy, reverificado el 18-oct a las 08:34); 0 errores en los demás dominios consultados · <b>3 fiscalías con dominio no devuelto</b>, dentro de las 15 <code>NO REVISADA</code>: Sin, Hgo, Camp</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 20 de 32 con consulta propia por entidad</b> · <b>11 solo por consulta regional amplia</b>: BCS, Dgo · Coah · Jal · CDMX, Edomex, Tlax, Qro · Camp, Yuc, QRoo · <code>NO REVISADA</code>: Ags · <b>armamento: 12 de 32 por dominio propio de seguridad o fiscalía</b> —BC, BCS, Son, Sin · Zac · Mich, Gto · CDMX, Edomex, Pue · Chis, QRoo—, 2 de lectura parcial (Son, solo portada; Gto, una página); <b>2 por portal del gobierno estatal</b> —NL, Gro—; <code>NO REVISADA</code> (18): Chih, Dgo · Coah, SLP, Tamps · Jal, Col, Nay, Ags · Mor, Tlax, Hgo, Qro · Ver, Tab · Oax, Camp, Yuc</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 15-oct</b>: existe (Milenio y republicadores) · <b>acciones del 16 y del 17-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta · <b>Defensa, Marina, Guardia Nacional y FGR</b>: SRIV · <b>gabinetedeseguridad.gob.mx</b>: SRIV (solo contenido de 2025)</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 18-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR TRES ROJOS</b>: ARG-136-001 a ARG-136-003 · <b>reserva</b> en ARG-136-002 y ARG-136-003.
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-136-004 y ARG-136-005.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-136-006 a ARG-136-009.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-136-REC-001 a ARG-136-REC-003.
      <br><b>5.</b> <code>23 H 06 MIN; CINCO DE NUEVE CON FRONTERA O PUBLICADOS EL DÍA DE APERTURA SIN HORA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. CULIACÁN, TERCER HECHO CON MUERTO EN DOS EDICIONES</b> (cálculo propio; día de ARG-135-007 solo por resumen; colonia de ARG-136-004 contradicha). ARG-136-004 se suma a ARG-135-001 y ARG-135-007. Línea: <b>solicitar a la FGE Sinaloa el cotejo de casquillos de los tres</b> — hipótesis; vínculo no acreditado.
      <br><b>2. SILAO, CUARTO ATAQUE CON MUERTOS ENTRE EL 14 Y EL 17-OCT</b> (cálculo propio). ARG-136-REC-001 se suma a ARG-133-REC-002, ARG-133-REC-003 y ARG-134-001. Línea: <b>solicitar a la FGE Guanajuato si las carpetas comparten indicios o vehículos</b> — vínculo no acreditado.
      <br><b>3. APATZINGÁN, TERCER HECHO CON MUERTOS ENTRE EL 13 Y EL 16-OCT</b> (cálculo propio; el 13, solo por resumen; el 16, sin hora). ARG-135-003 se suma a ARG-135-004 y ARG-134-REC-003. Línea: <b>solicitar a la Fiscalía Regional de Apatzingán el cotejo de indicios entre las tres carpetas</b> — hipótesis.
      <br><b>4. GUERRERO, DOS DETENCIONES EN TAXCO EN EL MISMO CORTE.</b> ARG-136-008 (La Familia Michoacana, por titular; hecho de 2020) y ARG-136-009 (secuestro de 2026; adscripción solo por resumen). Línea: <b>solicitar a la FGE Guerrero si las órdenes provienen de la misma carpeta o estructura</b> — hipótesis; vínculo no acreditado.
      <br><b>5. BAJA CALIFORNIA Y SONORA, FOSAS CON CIFRA DE COLECTIVO Y SIN CIFRA OFICIAL.</b> ARG-135-REC-003 y ARG-135-REC-004. Línea: <b>solicitar a las Comisiones Estatales de Búsqueda la cifra oficial y el calendario de identificación genética</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code> (solo contenido de 2025); lectura directa no disponible. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: SALAMANCA Y ACAPULCO", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA", co2)
 + page("CRIMEN ORGANIZADO (III) — ACCIONES INSTITUCIONALES", co3)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES: VENTANAS DE ARGOS 134 Y 135", rec1)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if any(a["c"]))
script = script.replace('"<br>Consulta: " + (top.fecha || "—") + " " + (top.hora || "")', '"<br>Fecha y hora (hecho o publicación): " + (top.fecha || "—") + " " + (top.hora || "") + "<br>Consulta: " + CONSULTA_TXT')
if "const CONSULTA_TXT" in script:
    script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
else:
    script = script.replace("const CORTE_FECHA", f'const CONSULTA_TXT = "{CONSULTA}";\nconst CORTE_FECHA', 1)
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
assert "WINDOW_DAYS = 2;" in script  # la ventana 17-oct 09:28 → 18-oct 08:34 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
