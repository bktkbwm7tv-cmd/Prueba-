# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 157.
Uso: python3 tools/datos-argos-157.py <plantilla ARGOS 156> <salida>
Ventana: 22-nov 09:34 → 23-nov 08:35 CDMX (23 h 01 min; dom 22 · lun 23). Archivo: argos-2026-11-23.html.
La hora de «Consulta» se fija al cierre de procedencia-cifras R2 con la variable ARGOS_CONSULTA (HH:MM)."""
import sys, re, json, os, html as H

NUM, FECHA, HORA = "157", "2026-11-23", "08:35"
CONSULTA = "2026-11-23, última búsqueda " + os.environ.get("ARGOS_CONSULTA", "__CONSULTA__")
DUR = "23 h 01 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 09:34 DEL 22, ES DE LA VENTANA DE ARGOS 156 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
NDA = "detenidos: cifra solo por titular de medio, sin cifra de autoridad: n/d"
PUB = "Publicado el día de apertura sin hora por fragmento: se integra en esta edición, la primera que lo ve."
TM = " <span class=\"muted-note\">(por titular de medio)</span>"
QNI = "<code>QUIÉN INICIÓ NO DETERMINADO</code>"
CND = "<code>CANTIDAD NO DETERMINADA</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano). Agresores abatidos: fuera de mu.
E = [
 # ======================= ROJOS
 dict(id="ARG-157-001", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-22", hora="madrugada (solo por resumen)", mu=1, he=1, cu=0, hk=3,
  ent="Michoacán", mun="Zinapécuaro (brecha, por resumen)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; madrugada, solo por resumen",
  title="MICHOACÁN · ZINAPÉCUARO — EMBOSCAN A MILITARES: UN ELEMENTO MUERTO Y OTRO HERIDO",
  hecho="Zinapécuaro · brecha de la región, " + RES + " · «presunta emboscada», por titular (Changoonga), y «tiroteo», por titular (Atiempo) · domingo 22-NOV, por ruta (Latinus 2026/11/22: «Muere militar tras emboscada de sujetos armados en Michoacán; otro elemento resulta herido»; RED Michoacán 2026/11/22: «Emboscada contra militares deja un elemento muerto en Zinapécuaro»; Changoonga 2026/11/22) · madrugada, " + RES + " · " + RET + " · <b>1 militar muerto</b> y <b>1 herido</b>, por titular (La Jornada 2026/11/23: «Un muerto y un herido, en emboscada contra militares en Zinapécuaro») (🔴 ataque a personal de las fuerzas armadas; muerte de personal) · «emboscada», por titular: el grupo inicia · cifras atribuidas a la Fiscalía de Michoacán, " + RES + " · agresores huidos, " + RES + " · " + NOD,
  panel="<b>Emboscada a militares</b>: 1 muerto, 1 herido", inst=SB, nac="Latinus · La Jornada", conf="★★★☆☆",
  campo="hora solo por resumen frente a la apertura; declaración de la Fiscalía solo por resumen", I=0, N=2, R=4, A=0,
  fechadas=["Latinus (2026/11/22)", "RED Michoacán (2026/11/22)", "Changoonga (2026/11/22)", "La Jornada (2026/11/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Zinapécuaro figura por ARG-117-REC-001 (emboscada a la BOI, 4-sep, Santa Cruz–San José Carpintero) y por ARG-101-003, ARG-102-003 y ARG-102-ARM-001 (agosto): otros hechos. «Emboscada en Zinapécuaro deja un militar muerto y tres heridos» (Meganoticias) y titulares equivalentes (Siglo Veinte; 1plana): la emboscada de septiembre, no se suma. Identidad: no se reproduce."),
 dict(id="ARG-157-002", estado="MX-PUE", region="Centro", color="rojo", impacto="grande", fecha="2026-11-22", hora="madrugada, ~03:00, o aviso a las 23:50 (solo por resumen)", mu=3, he=2, cu=0, hk=3,
  ent="Puebla", mun="Tepexco (San Juan Calmeca)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="publicación domingo 22-nov, por ruta; madrugada, ~03:00, o aviso a las 23:50, solo por resumen",
  title="PUEBLA · TEPEXCO — ATAQUE ARMADO EN SAN JUAN CALMECA: TRES HOMBRES MUERTOS, UNO MENOR DE EDAD; VEHÍCULOS INCENDIADOS",
  hecho="Tepexco · <code>SAN JUAN CALMECA</code>, por titular (UnoTV: «Violencia en la Mixteca de Puebla: queman mototaxi y asesinan a cuatro personas en San Juan Calmeca») · publicación domingo 22-NOV, por ruta (Retodiario 2026/11/22: «Riña en Tepexco deja tres muertos y dos heridos; queman mototaxi con cuerpos»; Síntesis 2026/11/22: «Tras presunta riña, abandonan tres cadáveres en Tepexco») y por slug (El Congresista «…/tres-muertos-tepexco-22-noviembre»: «Tepexco: ataque armado deja tres hombres muertos, entre ellos un menor; dos vehículos fueron incendiados») · madrugada, ~03:00, o aviso a la policía a las 23:50, " + RES + " · " + RET + " · <b>3 hombres muertos</b>, uno menor de edad, por titular, frente a 4, por titular (UnoTV; E-Consulta: «Alcalde de Tepexco pide esclarecer homicidio de cuatro personas en Calmeca»): <code>SALDO CONTRADICHO — SE CUENTAN 3</code> (🔴 homicidio múltiple y quema de vehículos) · <b>2 heridos</b>, por titular (Periódico Central: «Mueren tres personas durante ataque armado en Tepexco, Puebla; hubo dos heridos tras las agresiones»; La Jornada de Oriente: «Ataque armado en Tepexco deja tres muertos y dos heridos») · dos o tres víctimas calcinadas, contradicho por titular (Mtp Noticias: «Abandonan dos cadáveres calcinados dentro de un mototaxi»; Quadratín Puebla: «Hallan tres cuerpos calcinados y un mototaxi incendiado en Tepexco») · mototaxi incendiado, por titular · móvil contradicho por titular: riña (Mediatik; Retodiario; Síntesis) o ajuste de cuentas (Municipios Puebla) · FGE de Puebla, diligencias, " + RES + " · " + NOD,
  panel="<b>3 muertos, uno menor, y 2 heridos</b>; vehículos incendiados", inst=SB, nac="UnoTV", conf="★★★☆☆",
  campo="hora solo por resumen frente a la apertura; saldo y móvil contradichos; ninguna fuente institucional", I=0, N=1, R=9, A=0,
  fechadas=["Retodiario (2026/11/22)", "Síntesis (2026/11/22)", "El Congresista (slug «22-noviembre»)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepexco no figura en ediciones previas. «Siete ejecutados en 24 horas y cero detenidos en Puebla» (E-Consulta): balance estatal, no se integra ni sostiene la ausencia de detenidos. Identidades: no se reproducen."),
 dict(id="ARG-157-003", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-22", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Sinaloa", mun="Sinaloa de Leyva (El Platanito)", dia="PUBL. DOM 22-NOV, POR RUTA",
  fecha_txt="publicación domingo 22-nov, por ruta; día y hora del ataque no fijados",
  title="SINALOA · SINALOA DE LEYVA — ATACAN A MILITARES EN EL PLATANITO",
  hecho="Sinaloa de Leyva · <code>EL PLATANITO</code>, " + RES + " · publicación domingo 22-NOV, por ruta (La Razón 2026/11/22: «Detienen a ocho integrantes de facción del 'Chapo Isidro' tras ataque a militares en Sinaloa») · día y hora del ataque no fijados · " + AP + " · " + RET + " · <b>ataque a militares</b>, por titular (Rotativo: «Ocho detenidos tras atacar a militares en Sinaloa de Leyva»; La Jornada 2026/11/22: «Sinaloa: Cae célula del 'Chapo Isidro' tras agresión al Ejército; hay 8 detenidos»); «tiroteo», por titular (Proceso) · patrulla de reconocimiento, " + RES + " (🔴 el grupo agrede a personal militar; inicia el grupo, por titular) · bajas militares: no informadas · agresión repelida; detención: ficha aparte",
  panel="<b>Ataque a militares</b>", inst=SB, nac="La Razón · La Jornada · Proceso", conf="★★★☆☆",
  campo="día y hora del ataque no fijados; patrulla solo por resumen; ninguna fuente institucional", I=0, N=3, R=2, A=0,
  fechadas=["La Razón (2026/11/22)", "La Jornada (2026/11/22)", "Luz Noticias (2026-11-22)", "Proceso (2026/11/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Platanito y Sinaloa de Leyva no figuran en ediciones previas. Otro episodio que ARG-156-001 (Guasave): otro municipio, sin bajas militares publicadas, publicación de otro día. Ubicación en Culiacán, por titular de un medio (Yahoo), o en Guasave, " + RES + ": <code>LUGAR CONTRADICHO</code>; se acoge El Platanito (ADN40 2026-11-23)."),
 # ======================= AMARILLOS
 dict(id="ARG-157-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-22", hora="tarde, ~16:30 (solo por resumen)", mu=1, he=1, cu=0, hk=16,
  ent="Sinaloa", mun="Culiacán (bulevar Universitarios)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; tarde, ~16:30, solo por resumen",
  title="SINALOA · CULIACÁN — ASESINAN A UN HOMBRE Y HIEREN A UNA MUJER JUNTO AL CENTRO DE CIENCIAS DE SINALOA",
  hecho="Culiacán · <code>BULEVAR UNIVERSITARIOS, JUNTO AL CENTRO DE CIENCIAS DE SINALOA</code>, por titular · domingo 22-NOV, por ruta (Luz Noticias 2026-11-22: «Asesinan a balazos a un joven y hieren a una mujer junto al Centro de Ciencias de Sinaloa») · tarde, ~16:30, " + RES + " · <b>1 hombre muerto</b> y <b>1 mujer herida</b>, por titular (Noroeste: «Un muerto y una mujer herida deja ataque armado junto al Centro de Ciencias de Sinaloa, en Culiacán») (🟡 homicidio doloso único) · ataque a un automóvil, " + RES + " · " + NOD,
  panel="<b>Hombre asesinado, mujer herida</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-11-22)"], estatus="Parcialmente corroborado", arm=None,
  desl="Noroeste: «Un muerto y una mujer herida deja ataque armado junto al Centro de Ciencias de Sinaloa, en Culiacán», sin fecha en la ruta; el día lo fija Luz Noticias. Centro de Ciencias no figura en ediciones previas. «Deja jornada violenta cuatro muertos en Sinaloa» (El Diario de Chihuahua 2026/nov/22) y «Jornada violenta en Culiacán y Mazatlán deja tres muertos y cuatro heridos…» (El Informador 20261123): balances, no se integran. «Fiscalía recoge indicios…» (Sinaloahoy): no es declaración nombrada."),
 dict(id="ARG-157-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-22", hora="tarde, ~14:30 (solo por resumen)", mu=1, he=0, cu=0, hk=14,
  ent="Sinaloa", mun="Mazatlán (fracc. Prados del Sol)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; tarde, ~14:30, solo por resumen",
  title="SINALOA · MAZATLÁN — ASESINAN A UN HOMBRE EN EL FRACCIONAMIENTO PRADOS DEL SOL",
  hecho="Mazatlán · <code>FRACC. PRADOS DEL SOL</code>, por titular · domingo 22-NOV, por ruta (Línea Directa 2026-11-22: «Asesinan a […] dentro de su casa en Prados del Sol, en Mazatlán»; Luz Noticias 2026-11-22: «Asesinan a balazos a joven de 26 años en Prados del Sol, en Mazatlán») · tarde, ~14:30, " + RES + " · <b>1 hombre muerto</b>, de 26 años, por titular (Los Noticieristas: «Asesinan a balazos a joven de 26 años frente a su domicilio en Prado del Sol, Mazatlán») (🟡 homicidio doloso único) · dentro o frente al domicilio, contradicho por titular · " + NOD,
  panel="<b>Hombre asesinado</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Línea Directa (2026-11-22)", "Luz Noticias (2026-11-22)"], estatus="Parcialmente corroborado", arm=None,
  desl="Prados del Sol de Culiacán (ARG-138-003, octubre): homónimo, otro hecho. Hombre herido en la calle Desierto del mismo fraccionamiento (Los Noticieristas), sin fecha: visto, no se suma. Identidad: no se reproduce."),
 dict(id="ARG-157-006", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-22", hora="tarde (solo por resumen)", mu=1, he=0, cu=0, hk=15,
  ent="Michoacán", mun="Jacona (col. Nueva España)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; tarde, solo por resumen",
  title="MICHOACÁN · JACONA — ASESINAN A UN ADOLESCENTE EN LA COLONIA NUEVA ESPAÑA; DAÑOS EN DOS VEHÍCULOS Y UN INMUEBLE",
  hecho="Jacona · <code>COL. NUEVA ESPAÑA</code>, " + RES + " · domingo 22-NOV, por ruta (RED Michoacán 2026/11/22: «Ataque armado deja un hombre muerto y daños en 2 vehículos y un inmueble, en Jacona») · tarde, " + RES + "; «esta tarde», por titular sin fecha (Radio Zitácuaro) · <b>1 adolescente muerto</b>, por titular (Respuesta Michoacán: «Ataque armado deja un adolescente muerto y daños en dos vehículos y un inmueble, en Jacona»); la ruta fechada dice «hombre»; 16 años, por titular (La Voz de Michoacán: «Identifican a Jorge, adolescente de 16 años asesinado en Jacona») (🟡 homicidio doloso único) · daños a dos vehículos y un inmueble, por titular · más de 40 casquillos, " + RES + " · " + NOD,
  panel="<b>Adolescente asesinado</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["RED Michoacán (2026/11/22)"], estatus="Parcialmente corroborado", arm=None,
  desl="IMN México, Nanchemichoacán y La Voz de Michoacán («Ataque armado en Jacona deja un hombre muerto») reproducen la nota de RED Michoacán: una sola fuente. Jacona figura por ARG-130-001 (bomberos, octubre): otro hecho. «Asesinan a adolescente de 15 años en Jacona» (La Voz de Michoacán): fracc. Manantiales del Curutarán, 6-nov, otro hecho. «Ataque armado en la colonia Nueva España, en Jacona, deja un muerto y dos lesionados» (La Voz de Michoacán), sin fecha: <code>MISMO HECHO NO ACREDITADO — HERIDOS NO INTEGRADOS</code>. Cuerpo desmembrado en Jacona (Respuesta Michoacán), sin fecha: visto. Identidad: no se reproduce."),
 dict(id="ARG-157-007", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-22", hora="no fijada; tarde (solo por resumen)", mu=1, he=1, cu=0, hk=15,
  ent="Guanajuato", mun="Irapuato (campos Estrella, col. Las Delicias)", dia="DOM 22-NOV, POR RUTA",
  fecha_txt="domingo 22-nov, por ruta; hora no fijada; tarde, solo por resumen",
  title="GUANAJUATO · IRAPUATO — ATAQUE ARMADO EN LOS CAMPOS DE FUTBOL ESTRELLA: UN MUERTO Y UN HERIDO",
  hecho="Irapuato · <code>CAMPOS DE FUTBOL ESTRELLA, COL. LAS DELICIAS</code>, por titular (Milenio: «Irapuato: Ataque en campo de futbol La Estrella deja muerto y herido»; El Sol de Irapuato: «Asesinan a un hombre y lesionan a otro durante partido de futbol en Las Delicias, en Irapuato») · domingo 22-NOV, por ruta (Kuali 2026/11/22: «ATAQUE ARMADO EN CAMPOS ESTRELLA DEJA UN MUERTO Y UN HERIDO EN IRAPUATO»; AM 2026/11/22: «Convivían tras partido en campos de futbol de Irapuato cuando entraron y balearon a dos») · hora no fijada; tarde, " + RES + " · <b>1 hombre muerto</b> y <b>1 herido</b>, por titular (🟡 homicidio doloso único); «varios heridos», por titular sin fecha (Notus): <code>HERIDOS CONTRADICHOS — SE CUENTA 1</code> · colonia Plan de Guanajuato, por titular sin fecha (Guanajuato Informa): no se acoge · " + NOD,
  panel="<b>Ataque en campo de futbol</b>: 1 muerto, 1 herido", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="hora no fijada; heridos contradichos; ninguna fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["Kuali (2026/11/22)", "AM (2026/11/22)"], estatus="Parcialmente corroborado", arm=None,
  desl="Campos Estrella no figura en ediciones previas; Irapuato, col. Ignacio Allende (ARG-155-004, 19-nov): otro hecho. XEU lo republica bajo etiqueta de Veracruz: misma fuente, no otro hecho. Alias de la víctima por titular: no se reproduce."),
 dict(id="ARG-157-008", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-23", hora="mañana; ~06:00 o ~07:15, contradicho (solo por resumen)", mu=1, he=0, cu=0, hk=6,
  ent="Guanajuato", mun="Irapuato (av. Siglo XXI, cerca de Inforum)", dia="LUN 23-NOV, POR RUTA",
  fecha_txt="lunes 23-nov, por ruta; mañana, hora contradicha, solo por resumen",
  title="GUANAJUATO · IRAPUATO — ASESINAN A UN VENDEDOR CERCA DE INFORUM",
  hecho="Irapuato · <code>AV. SIGLO XXI, CERCA DE INFORUM</code>, por titular · lunes 23-NOV, por ruta (AM 2026/11/23: «Ataque armado deja un vendedor muerto cerca de Inforum Irapuato») · ~06:00 o ~07:15, " + RES + ": " + FR + " · <b>1 hombre muerto</b>, vendedor, por titular (Agora GTO: «Le quitan la vida a vendedor de tamales y juegos, en Irapuato») (🟡 homicidio doloso único) · móvil no informado; posible asalto, " + RES + " · " + NOD,
  panel="<b>Vendedor asesinado</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen y contradicha; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["AM (2026/11/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Inforum no figura en ediciones previas. Giro contradicho, " + RES + " (desayunos o tamales). Publicado el día de cierre sin hora por titular."),
 # ======================= VERDES
 dict(id="ARG-157-009", estado="MX-SIN", region="Noroeste", color="verde", impacto="grande", fecha="2026-11-22", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Sinaloa", mun="Sinaloa de Leyva (El Platanito)", dia="PUBL. DOM 22-NOV, POR RUTA",
  fecha_txt="publicación domingo 22-nov, por ruta; día y hora de la detención no fijados",
  title="SINALOA · SINALOA DE LEYVA — EL EJÉRCITO DETIENE A OCHO INTEGRANTES DE LA FACCIÓN DE «EL CHAPO ISIDRO» EN EL PLATANITO",
  hecho="Sinaloa de Leyva · <code>EL PLATANITO</code>, " + RES + " · publicación domingo 22-NOV, por ruta (La Razón 2026/11/22) · " + AP + " · " + RET + " · <b>8 detenidos</b>, por titular (Proceso 2026/11/23: «Caen ocho integrantes más de la facción del Chapo Isidro tras tiroteo con militares»; La Jornada 2026/11/22: «…hay 8 detenidos») (🟢 detención) · cifra atribuida a la Defensa por medios, sin documento · un menor entre los detenidos, " + RES + " · participación en bloqueos, por titular (adn40: «habrían participado en bloqueos y ataques»); los del 20-nov, " + RES + " · cuatro militares y siete agresores muertos, " + RES + " (Aristegui): saldo de ARG-156-001, no se suma · ametralladora(s) calibre .50, singular o plural contradicho, y vehículos, " + RES + ": " + CND + " · puestos a disposición de la FGR en Culiacán, " + RES,
  panel="<b>8 detenidos</b> de la facción de «El Chapo Isidro»", inst=SB, nac="Proceso · La Razón · La Jornada · Excélsior · Crónica", conf="★★★☆☆",
  campo="día y hora de la detención no fijados; cifra de la Defensa solo citada por medios", I=0, N=5, R=1, A=0,
  fechadas=["La Razón (2026/11/22)", "La Jornada (2026/11/22)", "Luz Noticias (2026-11-22)", "Proceso (2026/11/23)", "Crónica (2026/11/23)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — armamento sin cantidad publicada: evento cualitativo",
  desl="Delito y detención en la misma ventana: dos fichas (ARG-157-003 y esta). Infobae 2026/11/23: cobertura en vivo, no fecha ni sostiene. Frente a los ocho de ARG-156-013 (Guasave): presuntamente distintos, «ocho integrantes más», por titular (Proceso); total de 16, " + RES + " (La Razón); otro municipio; publicación de otro día · coinciden cifra, corporación, facción y vínculo con los bloqueos: <code>POSIBLE DUPLICIDAD CON ARG-156-013 NO DESCARTADA — DETENIDOS FUERA DE TOTALES</code>. Nombres: no se reproducen."),
 dict(id="ARG-157-010", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-22", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Sinaloa", mun="Mazatlán (Lomas de Mazatlán)", dia="PUBL. DOM 22-NOV, POR RUTA",
  fecha_txt="publicación domingo 22-nov, por ruta; hora no fijada",
  title="SINALOA · MAZATLÁN — POLICÍAS ESTATALES DETIENEN A DOS HOMBRES CON 90 CARTUCHOS Y CARGADORES EN LOMAS DE MAZATLÁN",
  hecho="Mazatlán · <code>LOMAS DE MAZATLÁN</code>, por titular · publicación domingo 22-NOV, por ruta (Línea Directa 2026-11-22: «Policías estatales detienen a dos hombres con cargadores y una moto en Mazatlán»; Luz Noticias 2026-11-22: «Detienen a dos hombres con 90 cartuchos y cargadores para armas de fuego en Lomas de Mazatlán») · hora no fijada · " + AP + " · " + RET + " · <b>2 detenidos</b>" + TM + " (🟢 detención) · <b>90 cartuchos</b>, por titular (Luz Noticias; Los Noticieristas: «Denuncia anónima al 089 termina con dos detenidos y 90 cartuchos asegurados en Mazatlán») · cargadores, por titular, sin número; 2, " + RES + ": " + CND + " · calibres, " + RES + " · Policía Estatal, por titular; Grupo Interinstitucional, " + RES + ": <code>CORPORACIÓN CONTRADICHA</code> · denuncia al 089, por titular (Sinaloahoy)",
  panel="<b>2 detenidos</b> con 90 cartuchos", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora no fijada; detenidos sin cifra de autoridad; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Línea Directa (2026-11-22)", "Luz Noticias (2026-11-22)"], estatus="Parcialmente corroborado", arm="ARG-157-ARM-001",
  desl="Lomas de Mazatlán no figura en ediciones previas."),
]
R = [
 dict(id="ARG-157-REC-001", estado="MX-TLA", region="Centro", fecha="2026-11-20", hora="noche (solo por resumen)", orig="ARGOS 156", col_orig="rojo", mu=2, he=0, cu=0,
  ent="Tlaxcala", mun="Calpulalpan (col. El Palmar)", dia="VIE 20-NOV, POR RESUMEN",
  fecha_txt="viernes 20-nov por la noche, solo por resumen; publicación 21-nov, por ruta",
  title="TLAXCALA · CALPULALPAN — ATAQUE ARMADO EN UNA VIVIENDA DE EL PALMAR: MUEREN UN JOVEN Y UNA NIÑA DE SEIS AÑOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 156</code> · Calpulalpan · <code>COL. EL PALMAR, VIVIENDA</code>, por titular · publicación sábado 21-NOV, por ruta (Gentetlx 2026/11/21: «Confirma FGJE que niña fallecida en clínica de Calpulalpan murió tras ataque armado donde ejecutaron a un hombre en vivienda de El Palmar») · noche del viernes 20-NOV, " + DSR + " · <b>2 muertos</b>, un joven y una niña de seis años, por titular (N+: «Asesinan a Balazos a una Niña de Seis Años y a un Joven en Calpulalpan, Tlaxcala»; La Prensa de Tlaxcala 2026/11: «A balazos asesinan a un hombre y a una niña de seis años en Calpulalpan»; Quadratín Tlaxcala: «Muere joven y menor de edad tras ser agredidos a balazos en Calpulalpan») (🔴 homicidio múltiple) · la niña murió en una clínica; confirmación de la FGJE, por titular de medio · 3 detenidos, " + RES + ": <code>NO SE INTEGRA</code>",
  panel="<b>Un joven y una niña asesinados</b> en una vivienda", inst=SB, nac="N+",
  conf="★★★☆☆", campo="día y hora solo por resumen; confirmación de la FGJE solo citada por medios", I=0, N=1, R=3, A=0,
  fechadas=["Gentetlx (2026/11/21)"], estatus="Parcialmente corroborado",
  desl="Calpulalpan figura por ARG-152-008 (Mazapa, robo de ganado): otro hecho. No figura en el cartelón de ARGOS 156. «Calpulalpan suma seis muertes violentas en una semana» (385grados): recuento, no se integra. Identidades: no se reproducen."),
 dict(id="ARG-157-REC-002", estado="MX-MIC", region="Occidente", fecha="2026-11-20", hora="~19:00 (solo por resumen)", orig="ARGOS 156", col_orig="rojo", mu=1, he=3, cu=0,
  ent="Michoacán", mun="Aquila (Santa María Ostula)", dia="VIE 20-NOV, POR RESUMEN",
  fecha_txt="viernes 20-nov, ~19:00, solo por resumen; publicación 21-nov, por ruta",
  title="MICHOACÁN · AQUILA — EMBOSCAN A FAMILIAS NAHUAS DE SANTA MARÍA OSTULA: UN COMUNERO MUERTO Y TRES MUJERES HERIDAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 156</code> · Aquila · <code>SANTA MARÍA OSTULA</code>, por titular · publicación sábado 21-NOV, por ruta (El Independiente 2026/11/21: «Ataque armado en Ostula deja un comunero muerto y tres mujeres heridas»; El Diario de Chihuahua 2026/nov/21: «Emboscan a familias en Michoacán; hay 1 muerto y 3 heridas») · viernes 20-NOV, ~19:00, " + DSR + " · <b>1 comunero muerto</b> y <b>3 mujeres heridas</b>, una de ellas niña de 10 años, por titular (La Jornada 2026/11/21: «Presuntos integrantes del 'CJNG' emboscan y asesinan a comunero de Santa María Ostula y hieren a una niña de 10 años») (🔴 víctimas múltiples) · «emboscada», por titular: el grupo inicia · atribución al CJNG por la comunidad, por titular (La Jornada 2026/11/22: «Embosca el CJNG a familias de Santa María Ostula, acusan»): <code>NO ACREDITADA POR AUTORIDAD</code> · " + NOD,
  panel="<b>Emboscada a familias</b>: 1 muerto, 3 heridas", inst=SB, nac="La Jornada · SinEmbargo · Milenio · Pie de Página",
  conf="★★★☆☆", campo="día y hora solo por resumen; ninguna fuente institucional", I=0, N=4, R=2, A=0,
  fechadas=["El Independiente (2026/11/21)", "La Jornada (2026/11/21)", "El Diario de Chihuahua (2026/nov/21)", "La Jornada (2026/11/22)"], estatus="Parcialmente corroborado",
  desl="Visto de ARGOS 156 sin fecha (Milenio): se recupera con rutas del 21. Ostula no figura en el índice con ARG-ID. Identidades: no se reproducen."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-157-ARM-001", ficha="ARG-157-010", estado="MX-SIN", region="Noroeste", color="verde", ent="Sinaloa", mun="Mazatlán (Lomas de Mazatlán)", fecha="2026-11-22", hora="no fijada",
  fecha_txt="publicación 22-nov, por ruta; <code>SI RESULTA ANTERIOR A LAS 09:34 DEL 22, SE RETIRA</code>", c=[0, 0, 0, 0, 90, 0, 0, 0, 0, 0], nd=[5, 9], integra=True,
  corp="Policía Estatal de Sinaloa", conf="Bajo", nota="90 cartuchos, por titular de dos medios (Luz Noticias 2026-11-22; Los Noticieristas), sin comunicado oficial leído; cargadores sin número por titular; detenidos sin cifra de autoridad",
  fuentes=["Luz Noticias (2026-11-22)", "Línea Directa (2026-11-22)", "Los Noticieristas (2026/11)"]),
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
HORAS = 23 + 1 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
RPH = f"{cnt['rojo'] / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
RREG = {g: sum(1 for e in E if e["color"] == "rojo" and e["region"] == g) for g in ("Noroeste", "Noreste", "Occidente", "Centro", "Golfo", "Sureste")}
assert TOT == [0, 0, 0, 0, 90, 0, 0, 0, 0, 0] and ARMAS == 0, (TOT, ND)
assert cnt == {"rojo": 3, "amarillo": 5, "verde": 2}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU) == (9, 5, 0), (MU, HE, CU)
assert DENS == "0,43" and RPH == "0,13", (DENS, RPH)
assert (NAP, NFR, NRET) == (3, 1, 5), (NAP, NFR, NRET)
assert len(ENT) == 4 and len(ENT_ROJO) == 3, (ENT, ENT_ROJO)
assert RREG == {"Noroeste": 1, "Noreste": 0, "Occidente": 1, "Centro": 1, "Golfo": 0, "Sureste": 0}, RREG
assert sorted(e["id"] for e in E) == [f"ARG-157-{i+1:03d}" for i in range(len(E))]
for x in E:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert "2026-11-22" <= x["fecha"] <= "2026-11-23", x["id"]
    assert x["conf"] != "★★★☆☆" or len(x["fechadas"]) + (x["N"] + x["R"]) >= 2, x["id"]
    assert x["conf"] != "★★★★☆" or x["I"] >= 1, x["id"]

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
            "confianza": e["conf"], "fecha": e["fecha"], "hora": e["hora"] + (" · día solo por resumen" if "DÍA SOLO POR RESUMEN" in e.get("fecha_txt", "") else "") + (" · fecha de publicación; día del hecho no fijado" if e.get("dia", "").startswith("PUBL") else "")}

def arm_json(a):
    c = [("n/d" if i in a.get("nd", []) else v) for i, v in enumerate(a["c"])]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if sum(a["c"]) > 30 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 156 — Reporte Nacional de Seguridad — 2026-11-22</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA DEFENSA Y A LA FISCALÍA DE MICHOACÁN LA HORA Y EL PARTE OFICIAL</b> (ARG-157-001).
      <br><b>2. COTEJE CON LA DEFENSA SI LOS OCHO DETENIDOS DE EL PLATANITO SON DISTINTOS DE LOS DE GUASAVE, Y SOLICITE EL INVENTARIO ASEGURADO</b> (ARG-157-009 y ARG-156-013).
      <br><b>3. SOLICITE A LA FISCALÍA DE PUEBLA LA HORA, EL SALDO Y EL MÓVIL</b> (ARG-157-002).
      <br><b>4. SOLICITE A LA SSP DE SINALOA EL DESGLOSE DE LO ASEGURADO EN LOMAS DE MAZATLÁN</b> (ARG-157-010).
      <br><b>5. VIGILE LA SITUACIÓN DE LAS FAMILIAS NAHUAS DE SANTA MARÍA OSTULA TRAS LA EMBOSCADA</b> (ARG-157-REC-002).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>22-nov 09:34 → 23-nov 08:35 CDMX</b> (<b>{DUR}</b>) · dom 22 (desde 09:34) · lun 23 (hasta 08:35) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperaciones de alto impacto</b> (ventana de ARGOS 156), atenuadas, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: un aseguramiento integrado, Lomas de Mazatlán, 90 cartuchos por titular de dos medios, confianza Bajo · <b>muertos por agresión</b>: {MU}, cálculo propio (Tepexco, 3 de 3 o 4, saldo contradicho) · <b>heridos</b>: {HE} · <b>detenidos</b>: El Platanito 8, sin cantidad de armamento; Lomas de Mazatlán 2, sin cifra de autoridad: n/d · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> · {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>{NRET} cláusulas de retiro</b> (detalle en cada ficha).
    <br><code>BALANCES, NO SE INTEGRAN</code>: «Deja jornada violenta cuatro muertos en Sinaloa» (El Diario de Chihuahua 2026/nov/22) · «Jornada violenta en Culiacán y Mazatlán deja tres muertos y cuatro heridos por disparos» (El Informador 20261123) · «Siete ejecutados en 24 horas y cero detenidos en Puebla» (E-Consulta).
    <br><b>Vistos, fuera de totales</b> (día solo por resumen o sin ruta): Chilpancingo, col. Del PRI, un muerto y dos heridos · Acayucan, Ver., estudiante asesinado · Hampolol, Camp., hombre ejecutado, fuente única · Cuitzeo, Mich., dos hombres muertos rociados con diésel · Cuautla, Mor., motociclista asesinado · Periférico Norte, Edomex, operador de transporte asesinado en un asalto · Chietla, Pue., pareja asesinada · Reynosa, joven muerto con arma blanca · <b>ventana de 156, no rojos</b>: Puente Nacional, Ver., feminicidio de una joven de 17 años (La Silla Rota 2026/11/21) · Libres, Pue., joven asesinado.
    <br><code>FE DE ERRATAS — ARGOS 156</code>: <b>ARG-156-003</b> (Nopaltepec): 156 contó 1 por saldo contradicho; se cuentan <b>2 agentes muertos</b> por titular (El Heraldo de San Luis Potosí 2026/11/20: «ASESINAN A DOS AGENTES DE LA FGR EN EMBOSCADA EN EL ESTADO DE MÉXICO»; Amexi; Angulo7), el segundo en un hospital {RES}; un solo fallecido, por titular (Diario Portal: «…uno muere»): saldo aún contradicho · <b>dos rojos de la ventana de 156 se recuperan</b> (Calpulalpan y Santa María Ostula) · <b>efecto sobre ARGOS 156</b> (cálculo propio): <b>18 hechos · 11 🔴 · 3 🟡 · 4 🟢 · 19 muertos por agresión (18 si en Nopaltepec murió un solo agente) · 5 heridos · 10 entidades</b>.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Guasave (ARG-156-001 y -013)</b>: ataque del grupo a militares en traslado {RES}; quién inició sigue sin titular; vinculación no publicada · <b>Pueblo Nuevo, Gto. (ARG-156-004)</b>: publicación del 19 por ruta (AM 2026/11/19); día y hora del hecho siguen {RES} · <b>Nopaltepec (ARG-156-003)</b>: «Emboscada a agentes de la FGR agudiza la violencia en Nopaltepec» (El Independiente 2026/11/23) · <b>Texhuacán (ARG-151-001)</b>: captura publicada el 20 por ruta (La Silla Rota 2026/11/20), día sin fijar · <b>Cuernavaca (ARG-147-001)</b>: llevado a juicio el señalado por el homicidio del regidor, por titular (Infobae 2026/11/17): <code>NO ES SENTENCIA</code> · <b>Juchitán (ARG-156-016)</b>: boletín 2992 publicado el 19 por ruta (Oaxaca Capital 2026/11/19); hora de la captura sin fijar.
  </p>
'''

byid = {e["id"]: e for e in E}
byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-157-{i:03d}"]) for i in (1, 2, 3, 9))
co2 = "\n".join(ficha(byid[f"ARG-157-{i:03d}"]) for i in (4, 5, 10))
co3 = "\n".join(ficha(byid[f"ARG-157-{i:03d}"]) for i in (6, 7, 8))
co4 = "\n".join(ficha(rbyid[f"ARG-157-REC-{i:03d}"], True) for i in (1, 2))
assert sorted(re.findall(r'id="(ARG-157-0\d\d)"', co1 + co2 + co3)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-157-REC-\d\d\d)"', co4)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN RESULTADO INDEXADO EN VENTANA</code>"
NDR = "solo por resumen: <b>cantidad no determinada</b>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), NI),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "Lomas de Mazatlán, por titular; confianza Bajo"),
 tile(4, "Cargadores", tv(5), "sin número por titular"),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), "calibre .50 en El Platanito, " + NDR),
 tile(9, "Detenidos", tv(9), "sin cifra de autoridad"),
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

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr style="opacity:.72;"><td colspan="16"><code>SIN RESULTADO INDEXADO EN VENTANA</code> (26 entidades por dominio; 6 <code>NO REVISADA</code>) · ningún aseguramiento de la ventana con día fijado y cantidad publicada por titular o por autoridad</td></tr>'

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
    <b>Lectura regional</b>: ningún arma integrada en ninguna región. <b>Cálculo propio</b>.
    <br><b>BOLETÍN FEDERAL</b>: acciones del 19-nov: __FED17__ · acciones del 20, 21 y 22-nov y agregado «20, 21 y 22»: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título · <b>corroboración débil por construcción</b>; <b>un agregado no fija el día ni la hora de cada acción</b>.
    <br><code>VISTOS, NO INTEGRADOS</code>: inventario de seis armas largas, cuatro cortas y una ametralladora calibre .50 {RES} (Milenio; Infobae, cobertura en vivo): <code>ATRIBUCIÓN ENTRE GUASAVE (ARG-156-013) Y EL PLATANITO (ARG-157-009) NO ARBITRADA — NO INTEGRAR</code> · Mocorito, Sin., seis detenidos: boletín de acciones del 19 {RES} · Nuevo Laredo, 16 armas: hecho del 11-nov {RES}, <code>POSIBLE DUPLICIDAD CON LOS VISTOS DE ARGOS 150 — NO INTEGRAR</code> · Reynosa, dos fusiles Barrett, sin titular ni fecha.
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
      <tr><td colspan="6"><b>Ninguna sentencia publicada en la ventana.</b> Candidatos heredados (Iguala, Oaxaca 2,993, Villahermosa 5126): si se confirman, pertenecen a la ventana de ARGOS 155.</td></tr>
      <tr><td><b>Guerrero</b><br>Iguala (caso Los Avispones, 2014)</td><td>Exalcalde de Iguala y coacusados (24 a 26, contradicho entre ediciones; <code>HEREDADO — NO REVERIFICADO</code>); homicidio en grado de tentativa y homicidio calificado {RES}; causa 4/2018 y acumuladas {RES}</td><td>60 años, por titular (Proceso 2026/11/19; La Silla Rota 2026/11/19)</td><td>Juzgado federal en Matamoros {RES}</td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin comunicado de la FGR ni del Poder Judicial · fallo del 10-nov, publicado el 19 {RES} · apelada: no firme {RES}</td><td>Bajo</td></tr>
      <tr><td><b>Oaxaca</b><br>Sierra de Flores Magón</td><td>Violación de una adulta mayor; boletín 2,993 de la FGEO</td><td>14 años, por titular del boletín («FGEO obtiene 14 años de prisión…»)</td><td>FGEO</td><td>Publicación 19-nov {RES} · fecha de la sentencia no publicada · el titular no lleva término de condena expreso · firmeza no informada</td><td>Medio</td></tr>
      <tr><td><b>Tabasco</b><br>Villahermosa</td><td>Feminicidio; boletín 5126 de la FGET, 18-nov, en el listado histórico del dominio</td><td>45 años, por titular del listado («45 años de prisión por feminicidio ocurrido en Villahermosa, obtiene la FGET»)</td><td>FGET</td><td>Ventana de ARGOS 155 · sin URL individual ni dos campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Chihuahua</b></td><td>Triple homicidio (La Opción 20261120: «Sentencian a responsable de triple homicidio»)</td><td>—</td><td>—</td><td>Condena del 13-nov {RES} · sin boletín de la FGE</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> en esta edición por dominio propio; caso Iguala por medios: sin boletín</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>29 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, BCS, Sin, Dgo · Coah, NL, Tamps, SLP, Zac · Jal, Col, Mich, Nay, Ags, Gto · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Ver, Tab · Gro, Oax, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>29</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>3</b>: Son (dominio sin páginas), Chih (dominio sin páginas), Camp (dominio de la fiscalía no confirmado)</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 23-nov 08:35: código <code>000</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 19 entidades; solo consulta amplia en 13 —BC, BCS, Son, Chih, Dgo · Coah, SLP, Zac · Nay · Qro · Oax, Chis, Yuc— · <b>armamento: 26 de 32 por dominio oficial</b>, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (6): BC, BCS, Son (dominio sin páginas), Sin, Dgo · Gto (solo boletines del gobierno estatal)</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 19-nov</b>: __FED17C__ · acciones del 20, 21 y 22 y agregado: <code>SIN RESULTADO INDEXADO EN VENTANA</code> · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · <code>BLOQUEO DE EGRESO REVERIFICADO EL 23-NOV: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Alto impacto</b>: dos agresiones armadas a personal militar (Michoacán y Sinaloa) y un homicidio múltiple en Puebla; {RPH} rojos por hora (cálculo propio).
      <br><b>2.</b> <b>Rojos por región</b>: Noroeste {RREG["Noroeste"]} · Occidente {RREG["Occidente"]} · Centro {RREG["Centro"]} · Noreste, Golfo y Sureste 0 (cálculo propio); ninguno de los tres con hora fijada por titular.
      <br><b>3.</b> <b>Violencia operativa</b>: homicidios dolosos únicos en tres entidades, sin agresiones a autoridades.
      <br><b>4.</b> <b>Respuesta institucional</b>: detenciones y un aseguramiento de munición de confianza baja; ningún arma integrada; ninguna sentencia integrable.
      <br><b>5.</b> <code>TOTALES NO COMPARABLES SIN MÁS CON LOS DE OTRAS EDICIONES: VENTANA DE 23 H 01 MIN FRENTE A 62 H 54 MIN DE ARGOS 156, CON HECHOS SUJETOS A CLÁUSULA DE RETIRO. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. AGRESIONES ARMADAS A PERSONAL MILITAR EN DOS ENTIDADES</b> (ARG-157-001 y -003): Zinapécuaro y El Platanito, Sinaloa de Leyva; lugar rural solo por resumen; vínculo no acreditado. Línea: <b>revisar los protocolos de desplazamiento de personal militar en Zinapécuaro</b>.
      <br><b>2. LA FACCIÓN DE «EL CHAPO ISIDRO» SOSTIENE AGRESIONES FUERA DE GUASAVE</b> (ARG-157-003 y -009): detenidos señalados por los bloqueos del 20-nov, por titular. Línea: <b>vigilar Sinaloa de Leyva y los municipios con bloqueos del 20-nov ante nuevas agresiones de la facción</b>.
      <br><b>3. VÍCTIMAS CALCINADAS EN LA MIXTECA POBLANA</b> (ARG-157-002): un menor entre los muertos; móvil contradicho. Línea: <b>vigilar el corredor Tepexco–Chietla (ARG-148-002, 5-nov); vínculo no acreditado</b>.
      <br><b>4. MENORES DE EDAD ENTRE LAS VÍCTIMAS</b> (ARG-157-002, -006, -REC-001 y -REC-002): Tepexco, Jacona, Calpulalpan y Ostula; vínculo no acreditado. Línea: <b>revisar reportes previos de amenazas en la col. Nueva España de Jacona y en El Palmar de Calpulalpan</b>.
      <br><b>5. DOS ATAQUES EN ESPACIOS PÚBLICOS DE IRAPUATO EN MENOS DE UN DÍA</b> (ARG-157-007 y -008): móviles no informados; vínculo no acreditado. Línea: <b>vigilar la av. Siglo XXI en horario matutino</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — sin lectura directa; cifras preliminares de homicidio de la ventana no vistas · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

FED17 = "boletín publicado, <code>SIN RESULTADO INDEXADO</code> en <code>gob.mx/sspc</code>; tomado de republicadores (RED113 2026/11; Tallapolítica; Certeza Diario); contenido <code>SOLO POR RESUMEN</code>"
arm2 = arm2.replace("__FED17__", FED17)
sent = sent.replace("__FED17C__", FED17)

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — AGRESIONES A MILITARES EN MICHOACÁN Y SINALOA; HOMICIDIO MÚLTIPLE EN TEPEXCO; DETENCIÓN EN EL PLATANITO", co1)
 + page("CRIMEN ORGANIZADO (II) — SINALOA: HOMICIDIOS EN CULIACÁN Y MAZATLÁN; DETENCIÓN EN LOMAS DE MAZATLÁN", co2)
 + page("CRIMEN ORGANIZADO (III) — HOMICIDIOS EN JACONA E IRAPUATO", co3)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES DE LA VENTANA DE ARGOS 156: CALPULALPAN Y SANTA MARÍA OSTULA", co4)
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
# la ventana de 157 toca dos fechas de calendario (22 y 23-nov); la plantilla de 156 trae 4
assert script.count("WINDOW_DAYS = 4;") == 1, "plantilla de 156 con WINDOW_DAYS = 4"
script = script.replace("WINDOW_DAYS = 4;", "WINDOW_DAYS = 2;")
assert script.count("WINDOW_DAYS = 2;") == 1 and "WINDOW_DAYS = 4;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS, RPH)
