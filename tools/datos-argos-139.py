# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 139 (rehecho el 21-oct; la versión de 43 min del 20-oct se retiró).
Uso: python3 tools/datos-argos-139.py <plantilla ARGOS 138> <salida>
Ventana: 20-oct 07:06 → 21-oct 10:23 CDMX. Archivo: argos-2026-10-21.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "139", "2026-10-21", "10:23"
CONSULTA = "2026-10-21 10:24-12:19"
DUR = "27 h 17 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 dict(id="ARG-139-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-20", hora="no fijada", mu=2, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (sindicatura de Villa Unión, col. Flor de Mayo)", dia="20-OCT, HORA NO FIJADA",
  title="SINALOA · MAZATLÁN (VILLA UNIÓN) — DOBLE HOMICIDIO DENTRO DE UNA VIVIENDA",
  hecho="Villa Unión, Mazatlán · <code>COL. FLOR DE MAYO, SOLO POR RESUMEN</code> · martes 20-OCT, por ruta (Línea Directa y Luz Noticias 2026-10-20) · " + AP + " · <b>2 muertos</b> —una mujer y un hombre— dentro de una vivienda, por titulares (🔴 homicidio múltiple) · madre e hijo, por titular de Línea Directa; «pareja», por titulares de Luz Noticias y Noroeste: <code>PARENTESCO CONTRADICHO ENTRE TITULARES</code>; edades por familiares, " + RES + ": <code>PRELIMINAR</code> · Bomberos Veteranos confirmaron los decesos, " + RES + " · <b>ningún detenido publicado</b> · sin comunicado de la Fiscalía de Sinaloa · identidades: no se reproducen",
  panel="Doble homicidio: <b>2 muertos</b> en una vivienda", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; parentesco contradicho entre titulares; ninguna fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Línea Directa (2026-10-20)", "Luz Noticias (2026-10-20)"], estatus="Parcialmente corroborado", arm=None,
  desl="Flor de Mayo no figura en las cinco ediciones previas ni en el índice. Villa Unión figura en ARG-132-REC-002 (col. Toledo Corro, 12-oct): otro hecho. Uno de los seis homicidios del 20-oct en Mazatlán según el recuento de Noroeste (cobertura en vivo, no fecha hechos); los demás, en ARG-139-004, ARG-139-010 y en el archivo de fuentes. La captura de «El Wicho» en Villa Unión (ARGOS 134, fecha no fijada): otro hecho."),
 dict(id="ARG-139-002", estado="MX-ZAC", region="Noreste", color="rojo", impacto="mediano", fecha="2026-10-20", hora="no fijada", mu=0, he=0, cu=3,
  ent="Zacatecas", mun="Jalpa (vía pública) y Moyahua (cerca de la Unidad Deportiva)", dia="20-OCT, HORA NO FIJADA",
  title="ZACATECAS · JALPA Y MOYAHUA — HALLAN TRES CUERPOS EN DOS MUNICIPIOS",
  hecho="Jalpa y Moyahua de Estrada · <code>JALPA: VÍA PÚBLICA · MOYAHUA: CERCA DE LA UNIDAD DEPORTIVA, SOLO POR RESUMEN</code> · publicado el martes 20-OCT, por ruta (Diario de Yucatán 2026/10/20) · " + AP + " · «madrugada de este martes», " + RES + " · <b>3 cuerpos</b>, por titulares —1 en Jalpa y 2 en Moyahua, " + RES + "; una primera nota daba 2 · «Fiscalía confirma localización de tres cuerpos», por titular (Meganoticias) · Policía de Investigación y Servicios Periciales, " + RES + " · <code>CAUSA DE MUERTE NO INFORMADA</code> · <code>RELACIÓN ENTRE LOS DOS HALLAZGOS NO ACREDITADA</code> · mensaje de un grupo delictivo: solo en una fuente, <code>NO CORROBORADO, NO SE INTEGRA</code> · sexo fijado solo en Jalpa (un hombre), " + RES + " · <b>ningún detenido publicado</b>",
  panel="Hallazgo de <b>3 cuerpos</b> en dos municipios", inst="Fiscalía de Zacatecas <span class=\"muted-note\">(por titular)</span>", nac="El Universal", conf="★★★☆☆",
  campo="causa de muerte no informada; confirmación institucional solo por titular; hora no fijada", I=1, N=1, R=2, A=0,
  fechadas=["Diario de Yucatán (2026/10/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="Moyahua no figura en las cinco ediciones previas ni en el índice. «Jalpa» en el índice es Jalpa de Méndez, Tabasco (ARG-133-009): otro lugar. Diario de Yucatán reproduce, según el resumen, la nota de El Universal: no se cuenta como independiente. La Fiscalía figura por el titular de Meganoticias, que no se cuenta además como regional. Cuerpos fuera del recuento de muertos por agresión: van al de cuerpos hallados."),
 dict(id="ARG-139-003", estado="MX-OAX", region="Sureste", color="rojo", impacto="mediano", fecha="2026-10-21", hora="mañana (solo por resumen)", mu=1, he=0, cu=0,
  ent="Oaxaca", mun="Juchitán de Zaragoza (crucero; ubicación solo por resumen)", dia="21-OCT, MAÑANA, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-21, mañana — DÍA SOLO POR RESUMEN",
  title="OAXACA · JUCHITÁN — ASESINAN A UN TRABAJADOR DEL AYUNTAMIENTO",
  hecho="Juchitán de Zaragoza · <code>EN UN CRUCERO, SOLO POR RESUMEN</code> · mañana del MIÉRCOLES 21-OCT, " + RES + " · " + FR + " · <b>1 muerto</b>: trabajador del Ayuntamiento, por titular (El Imparcial de Oaxaca); adscrito a limpieza, de 23 o 24 años, " + RES + ": <code>CONTRADICHO</code> (🔴 víctima servidor público) · agresores en motocicleta, " + RES + " · se dirigía a una audiencia, " + RES + " · «en 24 horas matan a cinco hombres en Juchitán», por titular (La Silla Rota 2026/10/21): <code>NO CONSTA QUE INCLUYA AL TRABAJADOR</code>; periodos de los titulares contradichos (24 h, 48 h, 2 y 3 días): <code>RECUENTO NO SE INTEGRA</code> · las autoridades no habían informado, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Trabajador municipal asesinado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día y hora solo por resumen; titular único sin fecha en la ruta; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="La víctima no figura en las ediciones previas. NO es ARG-138-001 (col. Tomás Aquino, lunes 19). Otros homicidios de Juchitán del 19 y 20-oct: ver Conclusión 2. El rojo descansa en un solo titular regional (víctima servidor público)."),
 dict(id="ARG-139-004", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="~11:00 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (Infonavit Playas, calle Lucio Blanco)", dia="20-OCT, ~11:00 POR RESUMEN",
  title="SINALOA · MAZATLÁN — ASESINAN A UN MOTOCICLISTA EN UN PUESTO DE TACOS DEL INFONAVIT PLAYAS",
  hecho="Mazatlán · <code>INFONAVIT PLAYAS, CALLE LUCIO BLANCO, JUNTO A LA CARRETERA MÉXICO 15, SOLO POR RESUMEN</code> · martes 20-OCT, por ruta (Luz Noticias 2026-10-20) · ~11:00, " + RES + " · " + AP + " · <b>1 muerto</b>: motociclista, por titulares (🟡 homicidio doloso único) · de 20 a 30 años, sin identificar, " + RES + " · ubicación «frente a Ley del Mar» en otra nota: <code>MISMO HECHO NO CONFIRMADO</code> · <b>ningún detenido publicado</b>",
  panel="Motociclista asesinado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Luz Noticias (2026-10-20)"], estatus="Parcialmente corroborado", arm=None,
  desl="Quadratín ubica el puesto en la col. Pueblo Nuevo: ubicación <code>CONTRADICHA</code>, solo por resumen. «Infonavit Playas» figura en ARGOS 129 (corte del 11-oct) como lugar de una detención sin armamento: otro hecho. No es ARG-138-005 (San Joaquín, lunes 19)."),
 dict(id="ARG-139-005", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="mañana; ~10:39 u ~11:00 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Veracruz", mun="Xalapa (col. Rubén Jaramillo, calle Ignacio Zaragoza)", dia="20-OCT, MAÑANA POR RESUMEN",
  title="VERACRUZ · XALAPA — ASESINAN A UN PRESUNTO DOCENTE DENTRO DE SU AUTOMÓVIL",
  hecho="Xalapa · <code>COL. RUBÉN JARAMILLO, CALLE IGNACIO ZARAGOZA ENTRE BENITO JUÁREZ Y YUCATÁN, SOLO POR RESUMEN</code> · martes 20-OCT, por ruta (Formato 7, Plumas Libres y Horacero 2026/10/20) · mañana, ~10:39 u ~11:00, " + RES + " · " + AP + " · <b>1 muerto</b>, hombre de ~35 años dentro de un automóvil, por titulares (🟡) · maestro o docente, por titulares; <code>«PRESUNTO» EN VARIAS NOTAS</code> · impactos: de 2 a 8 según la nota, <code>CONTRADICHO, NO SE INTEGRA</code> · Policía Ministerial y Servicios Periciales; paramédicos de la SSP confirmaron el deceso, " + RES + " · <b>ningún detenido publicado</b> · nombre: <code>CONTRADICHO</code>, no se reproduce · móvil en una sola fuente: no se integra",
  panel="Presunto docente asesinado en su vehículo: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; calidad docente «presunta»; ninguna fuente institucional", I=0, N=0, R=9, A=0,
  fechadas=["Formato 7 (2026/10/20)", "Plumas Libres (2026/10/20)", "Horacero (2026/10/20)", "La Aldea de la Información (2026/10/21)"], estatus="Parcialmente corroborado", arm=None,
  desl="Rubén Jaramillo no figura en las ediciones previas; Xalapa figura en ARG-102-001 (19-ago): otro hecho. Sube a 🔴 solo si una autoridad acredita que la víctima era servidor público (docente de escuela pública)."),
 dict(id="ARG-139-006", estado="MX-HID", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="~12:30 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Hidalgo", mun="Tezontepec de Aldama (El Chamizal)", dia="20-OCT, ~12:30 POR RESUMEN",
  title="HIDALGO · TEZONTEPEC DE ALDAMA — ATAQUE ARMADO EN EL CHAMIZAL: UN MUERTO",
  hecho="Tezontepec de Aldama · <code>COMUNIDAD EL CHAMIZAL, SOLO POR RESUMEN</code> · martes 20-OCT, por ruta (La Silla Rota 2026/10/20) · ~12:30, " + RES + "; «esta tarde», en otra nota · " + AP + " · <b>1 muerto</b>, hombre adulto sin identificar, por titulares (🟡) · «el segundo en 2 días», por titular (La Silla Rota): el primero, en Huitel el lunes 19, " + RES + " · Seguridad Pública municipal y paramédicos; la PGJEH abrió carpeta por homicidio, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Ataque armado: <b>1 muerto</b>", inst=SB, nac="La Silla Rota · El Universal", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=5, A=0,
  fechadas=["La Silla Rota (2026/10/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Chamizal no figura en las ediciones previas. Tezontepec de Aldama figura en ARG-135-REC-002 (San Gabriel, ventana de ARGOS 131): otro hecho. Huitel: ver Conclusión 3."),
 dict(id="ARG-139-007", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="no fijada", mu=1, he=1, cu=0,
  ent="Chihuahua", mun="Ciudad Juárez (Cerradas de San Pedro)", dia="20-OCT, HORA NO FIJADA",
  title="CHIHUAHUA · CIUDAD JUÁREZ — ATAQUE ARMADO EN LA ENTRADA DE UN FRACCIONAMIENTO: UN MUERTO Y UN HERIDO",
  hecho="Ciudad Juárez · <code>CERRADAS DE SAN PEDRO, CALLES BASÍLICA DE SAN PEDRO Y BASÍLICA DE TORTOSA, SOLO POR RESUMEN</code> · martes 20-OCT, por ruta (El Bordo 20261020; El Diario de Juárez y El Diario de Chihuahua 2026/oct/20) · " + AP + " · <b>1 muerto</b> y <b>1 lesionado</b>, por titulares (🟡) · víctima dentro de una camioneta, por titular (El Bordo) · <b>ningún detenido publicado</b> · dos publicaciones adicionales (Portales de San Pedro; 21-oct 07:04, N+ sin fecha, solo por resumen) con 1 muerto y 1 lesionado en camioneta: <code>POSIBLE DUPLICIDAD CON ESTA FICHA — NO SE INTEGRAN HASTA VALIDACIÓN</code> (la del 21-oct es de otro día; hora y víctima, por resumen)",
  panel="Ataque armado: <b>1 muerto</b> y 1 herido", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Bordo (20261020)", "El Diario de Juárez (2026/oct/20)", "El Diario de Chihuahua (2026/oct/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Diario de Juárez y El Diario de Chihuahua publican el mismo texto (mismo grupo): una fuente. Cerradas y Portales de San Pedro no figuran en las ediciones previas. No es ARG-138-009 (Los Alcaldes, lunes 19)."),
 dict(id="ARG-139-008", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="~06:00 u ~08:00 (solo por resumen): CONTRADICHO", mu=0, he=0, cu=0,
  ent="Michoacán", mun="Uruapan (Calzada Benito Juárez)", dia="20-OCT, HORA CONTRADICHA",
  title="MICHOACÁN · URUAPAN — ATACAN A BALAZOS UN RESTAURANTE EN LA CALZADA BENITO JUÁREZ",
  hecho="Uruapan · <code>CALZADA BENITO JUÁREZ, CERCA DEL MERCADO LA CHARANDA, SOLO POR RESUMEN</code> · martes 20-OCT, por ruta (El Financiero y cuatro regionales 2026/10/20) · madrugada; ~06:00 o reportado ~08:00, " + RES + ": <code>HORA CONTRADICHA — A LAS 06:00 SERÍA DE LA VENTANA DE ARGOS 138</code> · " + AP + " · restaurante baleado, por titulares; agresores huyeron en moto, por titular (El Financiero) (🟡 agresión sin víctimas) · al menos 6 impactos en la fachada, " + RES + " · <b>sin muertos ni heridos publicados</b> · Fiscalía Regional procesó la escena; Guardia Nacional y policías acordonaron, " + RES + " · <b>ningún detenido publicado</b> · móvil no informado",
  panel="Restaurante baleado; <b>sin víctimas</b>", inst=SB, nac="El Financiero", conf="★★★☆☆",
  campo="hora contradicha que decide la ventana; ninguna fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["El Financiero (2026/10/20)", "Grupo Marmor (2026/10/20)", "MediaNews (2026/10/20)", "Red Michoacán (2026/10/20)", "Changoonga (2026/10/20)"], estatus="Parcialmente corroborado", arm=None,
  desl="El restaurante no figura en las ediciones previas ni en el índice. Grupo Marmor, MediaNews y Red Michoacán comparten título (un texto; se cuentan como una fuente); RED113 lo replica: no se cuenta. El Financiero da «cerca de las 8», solo por resumen."),
 dict(id="ARG-139-009", estado="MX-SLP", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="~21:00 (solo por resumen)", mu=1, he=0, cu=0,
  ent="San Luis Potosí", mun="San Luis Potosí (bulevar Rocha Cordero, a la altura de Tierra Blanca)", dia="20-OCT, NOCHE, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-20, ~21:00 — DÍA SOLO POR RESUMEN",
  title="SAN LUIS POTOSÍ · CAPITAL — PERSIGUEN Y ASESINAN A UN CONDUCTOR EN EL BULEVAR ROCHA CORDERO",
  hecho="San Luis Potosí · <code>BULEVAR ROCHA CORDERO, A LA ALTURA DE TIERRA BLANCA, SOLO POR RESUMEN</code> · noche del martes 20-OCT, ~21:00, " + RES + " · publicado el 21-OCT, por ruta (Potosinoticias 2026/10/21) · " + FR + " · <b>1 muerto</b>: conductor perseguido y baleado, por titulares (🟡) · el vehículo chocó contra la contención; casquillos en el sitio, " + RES + " · la Fiscalía estatal investiga, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Conductor asesinado tras persecución: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día y hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Potosinoticias (2026/10/21)"], estatus="Parcialmente corroborado", arm=None,
  desl="Rocha Cordero no figura en las ediciones previas ni en el índice."),
 dict(id="ARG-139-010", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-20", hora="~13:00 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (fracc. La Foresta, av. Del Sol)", dia="20-OCT, ~13:00 POR RESUMEN",
  title="SINALOA · MAZATLÁN — ASESINAN A OTRO MOTOCICLISTA EN LA FORESTA",
  hecho="Mazatlán · <code>FRACC. LA FORESTA («LA FLORESTA» EN OTRAS NOTAS), AV. DEL SOL, SOLO POR RESUMEN</code> · martes 20-OCT, por titular con ruta fechada (Luz Noticias 2026-10-20: «es el tercer caso registrado este martes 20 de octubre») · ~13:00, " + RES + " · " + AP + " · <b>1 muerto</b>: motociclista, por titulares (🟡 homicidio doloso único) · repartidor; disparos desde un automóvil rojo, " + RES + " · «otro motociclista», por titular (Quadratín) · <code>RECUENTO DE CASOS DEL DÍA CONTRADICHO ENTRE MEDIOS (TRES / DOS), NO SE INTEGRA</code> · <b>ningún detenido publicado</b>",
  panel="Motociclista asesinado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Luz Noticias (2026-10-20)"], estatus="Parcialmente corroborado", arm=None,
  desl="La Foresta no figura en las ediciones previas ni en el índice. Otro hecho que ARG-139-004 (Infonavit Playas, ~11:00): colonia, hora y vehículo de los agresores distintos."),
]

# ---------------------------------------------------------------- RECUPERACIONES (ventanas anteriores; solo alto impacto)
R = [
 dict(id="ARG-139-REC-001", estado="MX-TAM", region="Noreste", fecha="2026-10-10", hora="noche (solo por resumen)", orig="ARGOS 129 — DÍA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=1, cu=0,
  ent="Tamaulipas", mun="Río Bravo (colonia irregular, solo por resumen)", dia="10-OCT, NOCHE",
  title="TAMAULIPAS · RÍO BRAVO — AGREDEN CON ARMA BLANCA A UNA DIPUTADA FEDERAL; QUEDA HERIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 129 — DÍA SOLO POR RESUMEN</code> · Río Bravo · <code>COLONIA IRREGULAR, AL SALIR DEL DOMICILIO DE UNA COLABORADORA, SOLO POR RESUMEN</code> · noche del SÁBADO 10-OCT, por tres resúmenes coincidentes (uno atribuido a Animal Político); <code>NINGÚN FRAGMENTO LITERAL CON EL DÍA</code> · primera ruta fechada: 17-OCT · <b>diputada federal del PVEM</b>, por titular; distrito 3, " + RES + " · <b>herida con arma blanca</b>, por titulares (🔴 en su ventana) · herida de <b>15 cm</b> en el costado, por titular (El Universal); en el abdomen, " + RES + "; lado derecho o izquierdo: <code>CONTRADICHO</code> · agresor encapuchado, por titular (Hoy Tamaulipas, ruta sin fecha); salido de un terreno baldío, " + RES + " · hospitalizada, " + RES + " · «FGR investiga», por titulares (Elefante Blanco 2026/10/19, La Verdad); fiscalía local, " + RES + ": <code>CONTRADICHO</code> · «Desconoce Fiscalía detalles sobre agresión a diputada federal», por titular (CN Tamaulipas 2026/10/19); fiscalía estatal, " + RES + " · pide protección federal; solicitó apoyo de la Guardia Nacional desde marzo, " + RES + " · <b>ningún detenido publicado</b> al 21-oct · <code>CIRCUNSTANCIAS SOLO POR RELATO DE LA VÍCTIMA; NINGUNA AUTORIDAD LAS CONFIRMA</code> · identidad pública por su cargo; nombre no reproducido",
  panel="<b>Diputada federal herida</b> con arma blanca", inst=SB, nac="Infobae · El Universal",
  conf="★★★☆☆", campo="día del hecho solo por resumen; circunstancias solo por relato de la víctima; sin fuente institucional", I=0, N=2, R=11, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/17)", "Infobae (2026/10/18)", "Expreso (2026/10/18)", "ABC Noticias (2026/10/19)", "En Línea Directa (2026/10/19)", "CN Tamaulipas (2026/10/19)", "Elefante Blanco (2026/10/19)"],
  desl="La diputada no figura en ningún cartelón previo ni en el índice. Día del hecho: 10-oct (el 17 es la denuncia pública), ventana de ARGOS 129 (10-oct 09:08 → 11-oct 08:58), por resumen. Río Bravo en ARG-128-REC-003 (canal Anzaldúas, aseguramiento del 8-oct): otro hecho."),
 dict(id="ARG-139-REC-002", estado="MX-GRO", region="Sureste", fecha="2026-10-19", hora="~17:00 (solo por resumen)", orig="ARGOS 138 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=0, cu=0,
  ent="Guerrero", mun="Juan R. Escudero (El Terrero)", dia="19-OCT, ~17:00",
  title="GUERRERO · EL TERRERO — ATAQUE CON DRONES EXPLOSIVOS Y DISPAROS CONTRA VIVIENDAS DE DESPLAZADOS RETORNADOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 138 — HORA SOLO POR RESUMEN</code> · El Terrero, Juan R. Escudero · lunes 19-OCT, ~17:00, " + RES + " · primera ruta fechada: 19-OCT (El Diario de Chihuahua) · «atacan con drones explosivos a desplazados», por titular (🔴 drones armados) · disparos y explosivos lanzados desde drones contra al menos 6 viviendas durante ~50 min, " + RES + " · agresores: más de 40 o ~60 hombres armados, " + RES + ": <code>CONTRADICHO</code> · el subsecretario de Asuntos Políticos y Sociales de Guerrero confirmó detonaciones y <b>ningún herido ni muerto</b>, " + RES + " · familias que habían regresado tras el desplazamiento de 2023 (50 a 61 retornados, " + RES + ") · despliegue de Ejército, Guardia Nacional y Policía Estatal tras el ataque, por titular (Diario Puntual 2026/10/21) · «reanudan ataques contra desplazados», por titular (El Diario de Chihuahua 2026/oct/20): <code>POSIBLE NUEVA AGRESIÓN O MISMO HECHO — NO SE INTEGRA HASTA VALIDACIÓN</code> · atribución a Los Ardillos: solo por habitantes, <code>NINGUNA AUTORIDAD LA ACREDITA</code> · <b>ningún detenido publicado</b>",
  panel="<b>Ataque con drones explosivos</b> a viviendas; sin heridos según el gobierno estatal", inst="Gobierno de Guerrero <span class=\"muted-note\">(solo por resumen)</span>", nac="El Financiero",
  conf="★★★☆☆", campo="hora solo por resumen; uso de drones explosivos por titular, sin parte militar", I=1, N=1, R=5, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/19)", "El Financiero (2026/10/20)", "El Diario de Chihuahua (2026/oct/20)", "Diario Puntual (2026/10/21)", "Lo de Hoy (2026/10/21)"],
  desl="El Terrero no figura en las cinco ediciones previas ni en el índice. Ataques con drones en la misma zona en enero de 2026 (Publimetro 2026/01/30): antecedente, otro hecho."),
 dict(id="ARG-139-REC-003", estado="MX-OAX", region="Sureste", fecha="2026-10-19", hora="~21:20 o ~21:30 (solo por resumen)", orig="ARGOS 138 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=0, he=1, cu=0,
  ent="Oaxaca", mun="Miahuatlán de Porfirio Díaz (col. La Merced)", dia="19-OCT, NOCHE",
  title="OAXACA · MIAHUATLÁN — ATACAN A BALAZOS AL SECRETARIO MUNICIPAL; QUEDA HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 138 — HORA SOLO POR RESUMEN</code> · Miahuatlán de Porfirio Díaz · <code>COL. LA MERCED, SOLO POR RESUMEN</code> · noche del lunes 19-OCT, ~21:20 o ~21:30, " + RES + " · primera ruta fechada: 20-OCT (Primera Línea) · <b>secretario municipal</b>, por titulares; «secretario particular del edil», por otros titulares: <code>CARGO CONTRADICHO</code>, servidor público en ambos casos (🔴 ataque contra autoridad) · <b>herido</b> en el cuello y los brazos, " + RES + "; gravedad <code>CONTRADICHA</code>: «de gravedad» o «estable», ambas " + RES + " · la FGEO abrió carpeta por tentativa de homicidio, " + RES + " · tercera agresión del año contra funcionarios o exfuncionarios del municipio, " + RES + " · <b>ningún detenido publicado</b> · identidad pública por su cargo; nombre no reproducido",
  panel="<b>Secretario municipal herido</b> a balazos", inst=SB, nac="Milenio <span class=\"muted-note\">(sin fecha en la ruta)</span>",
  conf="★★★☆☆", campo="hora solo por resumen; cargo y gravedad contradichos; ninguna fuente institucional", I=0, N=1, R=6, A=0,
  fechadas=["Primera Línea (2026/10/20)"],
  desl="Miahuatlán no figura en las cinco ediciones previas ni en el índice. Agresión al presidente municipal en junio de 2026: antecedente por resumen, otro hecho."),
]

for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = []
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
HORAS = 27 + 17 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
assert TOT == [0] * 10, TOT
assert cnt == {"rojo": 3, "amarillo": 7, "verde": 0}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC) == (9, 1, 3, 0, 2), (MU, HE, CU, MU_REC, HE_REC)
assert (NFR, NAP, len(ENT)) == (2, 8, 8), (NFR, NAP, len(ENT))
assert DENS == "0,37", DENS
assert all(e["id"] == f"ARG-139-{i+1:03d}" for i, e in enumerate(E))
assert len(set(r["id"] for r in R)) == len(R) and all(r["id"] == f"ARG-139-REC-{i+1:03d}" for i, r in enumerate(R))
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]

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
    c = a["c"]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if c[7] or c[4] > 1000 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 138 — Reporte Nacional de Seguridad — 2026-10-20</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE ZACATECAS LA CAUSA DE MUERTE, LA IDENTIFICACIÓN Y SI HAY RELACIÓN ENTRE LOS HALLAZGOS</b> (ARG-139-002).
      <br><b>2. SOLICITE A LA FISCALÍA DE SINALOA LA HORA, LA IDENTIFICACIÓN Y LA LÍNEA DE INVESTIGACIÓN</b> (ARG-139-001).
      <br><b>3. SOLICITE AL GOBIERNO DE GUERRERO Y A LA DEFENSA EL PARTE, SI HUBO UNA NUEVA AGRESIÓN Y SU FECHA, Y LA PERMANENCIA DEL DESPLIEGUE</b> (ARG-139-REC-002).
      <br><b>4. SOLICITE A LA FISCALÍA DE OAXACA LA CARPETA Y LAS MEDIDAS DE PROTECCIÓN</b> (ARG-139-REC-003).
      <br><b>5. SOLICITE A LA PGJ DE HIDALGO LA PENA Y LA REPARACIÓN DEL DAÑO DEL FALLO DEL 8-OCT</b> (Santiago Tulantepec; ver Rastreo de Sentencias).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: ORD[x["color"]]))
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>20-oct 07:06 → 21-oct 10:23 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b>.
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
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Muertos por agresión</th><th>Heridos</th><th>Cuerpos hallados</th><th>Armas cortas</th><th>Armas largas</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos en aseguramiento</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE</code> · <b>cuerpos hallados</b>: causa de muerte no informada, fuera del recuento de muertos por agresión · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · en las recuperaciones, <b>{HE_REC} heridos</b> y {MU_REC} muertos, fuera de todo total. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-136-006, <b>prisión preventiva</b> por traición a la patria dictada por un juez federal, por titulares (La Verdad Juárez y Raíchali 2026/10/21); «oficiosa» y «madrugada del 21-oct», {RES}; vinculación federal el sábado 24-oct, por titular (El Imparcial 2026/10/21); 15:00, {RES}; audiencia estatal el jueves 22-oct, por titular (La Razón 2026/10/19) · ARG-138-002, hallazgo informado el lunes 19, {RES}; identificación y detenidos: <code>NO OFICIAL, NO SE INTEGRA</code> · ARG-138-009/-010, detenidos tres o dos (uno de 16 años): <code>CONTRADICHO</code> · ARG-125-003 (Xalisco), 85 indicios, tres fosas más en Tecuala y diez detenidos, {RES} (Infobae 2026/10/20): <code>POSIBLE DUPLICIDAD CON ARG-133-REC-007 (TECUALA, LA PRESA) — NO SE INTEGRA HASTA VALIDACIÓN</code> · ARG-135-REC-003 (Tijuana), nuevos restos óseos en el cerro de Infonavit Cachanillas el martes 20, {RES}; cifra oficial no publicada.
  </p>
'''

rec1 = "\n".join(ficha(r, True) for r in R)
co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:6])
co3 = "\n".join(ficha(e) for e in E[6:])

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>NINGÚN ASEGURAMIENTO INTEGRABLE EN LA VENTANA</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], NI),
 tile(1, "Armas largas", TOT[1], NI),
 tile(2, "Sin categoría", TOT[2], NI),
 tile(3, "Cartuchos", fmt(TOT[4]), NI),
 tile(4, "Cargadores", TOT[5], NI),
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
{chr(10).join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ARMAMENTO INTEGRABLE EN LA VENTANA</code> — ningún aseguramiento con cantidad por titular fechado y fecha del hecho dentro de la ventana</td></tr>'}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: sin lectura (ninguna fila integrada).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code>: <b>Baja California, Tecate (La Rumorosa)</b>, hecho del 19-oct (En Línea BC 2026/10/19: «caen dos presuntos integrantes…», por titular): el boletín federal de acciones del 19-oct, publicado el 20-oct (Argonmexico 2026/10/20; Milenio), da 4 armas largas, 1 corta, 13 cargadores, 99 cartuchos y 2 detenidos, {RES}; <code>FUERA DEL TOTAL</code>.<br><code>VISTOS, NO INTEGRADOS</code>: <b>Veracruz</b>: agregado semanal de la Fiscalía (12-18 oct, publicado el 20-oct, {RES}): armas sin cifra, cualitativo · <b>San Luis Potosí</b>: balance de 24 h de la Guardia Civil Estatal, agregado sin evento individual · <b>Ciudad de México</b>: nota de la SSC con 1 pistola y 3 cartuchos, fecha solo por resumen: <code>FECHA NO FIJADA, NO SE INTEGRA</code>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">4 casos candidatos sin boletín</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>21 estatales revisadas</b>, 16 de lectura parcial · 11 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Sinaloa</b><br>Culiacán</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">feminicidio en grado de tentativa, por titular</span></td><td><b>18 años</b>, por titular</td><td>FGE Sinaloa <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · candidata desde ARGOS 138 · Luz Noticias 2026-10-19, por titular; Línea Directa 2026-10-19, <code>HEREDADO — NO REVERIFICADO</code> · boletín no localizado · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>General Cepeda</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">huachicol, por titular; sustracción ilícita de hidrocarburo en procedimiento abreviado, ~48 mil litros de diésel, {RES}</span></td><td><b>13 años</b>, por titular (Argonmexico 2026/10/19); 13 años 4 meses, {RES}; multa sin monto</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Argonmexico 2026/10/19; Diario de Tabasco, Red Metropolitana y Miled, no reverificados · boletín no localizado · publicada el 19-oct, ventana de ARGOS 138 · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Sonora</b><br>Caborca</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">transporte de casi 100 kg de metanfetamina, {RES}</span></td><td><b>8 años</b>, {RES}</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Telemax e Infobae 2026/10/19, no reverificados · boletín no leído · publicada el 19-oct, ventana de ARGOS 138 · firmeza no informada</td><td>Bajo</td></tr>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Tres sentenciados, nombres no reproducidos · <span class="muted-note">multihomicidio de tres surfistas extranjeros, por titulares</span></td><td><b>158 años</b>, por titular (El Financiero 2026/10/17); 9 meses adicionales, por titular de Sin Embargo; a cada uno, {RES} · no se suma · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>FGE Baja California <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · candidata desde ARGOS 135 · boletín no localizado · firmeza no informada</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Fuera de ventana, sin integrar</b>: Durango, sentencia de más de 14 años por violación (portada indexada de la Fiscalía, boletín del 19-oct, por titular) · Jalisco, El Salto, 15 años, y Guadalajara, más de 7 años (listado de la Fiscalía, 18 y 19-oct, {RES}) · Colima, 27 años por secuestro agravado (9-oct, {RES}) · <b>Santiago Tulantepec, Hidalgo</b>: fallo condenatorio del 8-oct ({RES}; La Silla Rota lo publica el 9-oct) por la muerte de tres mujeres, sin pena; la audiencia de individualización continúa el 21-oct a las 17:45, después del cierre, {RES}.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>21 de 32</b>, por búsqueda dirigida; acceso directo: 0; de ellas <b>16 de lectura parcial</b> · lectura no parcial (último ítem indexado de octubre): Jal, Nay, Ags, Col, Dgo · parcial: Son · Coah, NL, SLP, Zac · Mich, Gto · Edomex, Mor · Ver, Tab · Oax, Gro, Chis, Yuc, QRoo · <b>FGR</b>: <code>gob.mx/fgr</code> consultado, solo devolvió 2020-2022</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> · candidatas solo por medios, publicadas antes de la ventana: Sinaloa, Baja California, FGR (Coahuila y Sonora)</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>21</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>11</b>: BC, BCS, Chih, Sin · Tamps · CDMX, Pue, Tlax, Hgo, Qro · Camp</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 10:23 del 21-oct: código <code>000</code> · <b>dominios no devueltos por el buscador</b>: <code>fge.sinaloa.gob.mx</code>, <code>pgjhidalgo.gob.mx</code>, <code>fiscalia.tlaxcala.gob.mx</code>, <code>fiscalia.campeche.gob.mx</code>, <code>ssp.guerrero.gob.mx</code>, <code>seguridad.nl.gob.mx</code>, <code>ssp.durango.gob.mx</code>, <code>ssp.bajacalifornia.gob.mx</code>, <code>sspes.sonora.gob.mx</code>, <code>ssp.hidalgo.gob.mx</code>, <code>ssp.morelos.gob.mx</code>, <code>ssc.queretaro.gob.mx</code>, <code>seguridadypaz.guanajuato.gob.mx</code> · <b>dominios confirmados</b>: <code>fge.chiapas.gob.mx</code>, <code>fge.yucatan.gob.mx</code>, <code>ssp.chiapas.gob.mx</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 25 de 32 con consulta propia por entidad</b> · <b>7 solo por consulta regional amplia</b>: BC, Chih · Coah, NL · Ags, Gto · Edomex · <b>armamento: 13 de 32 por dominio oficial</b> —BCS · Zac · Jal, Nay, Ags, Col · CDMX, Edomex, Pue, Qro · Ver, Tab · Chis—, de lectura parcial salvo Jal y Col; <code>NO REVISADA</code> (19): BC, Son, Dgo, Chih, Sin · Coah, NL, Tamps, SLP · Mich, Gto · Mor, Tlax, Hgo · Gro, Oax, Camp, Yuc, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 19-oct</b>: publicado el 20-oct (Milenio; Argonmexico 2026/10/20), consultado por sus republicadores; hechos del 19-oct, ventanas anteriores · <b>acciones del 20-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas · <b>acciones del 21-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code>, solo por rango · <b>gabinetedeseguridad.gob.mx</b>: <code>NO REVISADA</code> · Guardia Nacional, Defensa y Semar: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 21-OCT 10:23: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>{cnt["rojo"]} ROJOS PROPIOS EN TRES ENTIDADES</b>: ARG-139-001, -002 y -003; el color de -002 y de -003 descansa en reserva (ver trazabilidad).
      <br><b>2.</b> <b>{cnt["amarillo"]} amarillos</b>: seis homicidios únicos y un ataque a un establecimiento sin víctimas.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ninguna acción con hecho dentro de la ventana; el boletín federal de acciones del 19-oct, publicado el 20-oct, es evento anterior, fuera del semáforo.
      <br><b>4.</b> <b>Ventanas anteriores</b>: tres rojos recuperados (ARG-139-REC-001 a -003), fuera de los totales.
      <br><b>5.</b> <code>NINGÚN HECHO PROPIO CON HORA FIJADA POR FUENTE: TOTALES NO COMPARABLES SIN MÁS CON LA SERIE.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. MAZATLÁN, TRES MOTOCICLISTAS ASESINADOS EL 20-OCT (DOS EN ESTA VENTANA)</b> (cálculo propio): Flores Magón («la madrugada de este martes», por titular de Luz Noticias 2026-10-20; ventana de ARGOS 138), ARG-139-004 y ARG-139-010; se suman a ARG-138-005 (mujer motociclista, 19-oct). <code>RECUENTO DE MEDIOS CONTRADICHO (TRES / DOS), NO SE INTEGRA</code>. Línea: <b>solicitar a la FGE Sinaloa si las víctimas eran repartidores</b> — hipótesis.
      <br><b>2. JUCHITÁN, DOS FICHAS CON MUERTOS EN TRES DÍAS Y OTROS TRES HOMICIDIOS SIN DÍA FIJADO.</b> ARG-138-001 (19-oct) y ARG-139-003 (21-oct); dos mototaxistas y un estudiante, días solo por resumen; La Silla Rota 2026/10/21 titula «cinco hombres en 24 horas»: composición contradicha, no se integra. Línea: <b>solicitar a la FGEO el desglose oficial y si los hechos se vinculan entre sí</b> — vínculo no acreditado.
      <br><b>3. TEZONTEPEC DE ALDAMA, TRES HECHOS ARMADOS DESDE LA VENTANA DE ARGOS 131.</b> ARG-135-REC-002 (San Gabriel, disparos contra policías municipales), Huitel (19-oct, solo por resumen; visto) y ARG-139-006. Línea: <b>solicitar a la PGJEH si los tres hechos comparten agresores o vehículos</b> — hipótesis.
      <br><b>4. VÍCTIMAS A BORDO DE AUTOMÓVIL O CAMIONETA EN TRES DE LOS SEIS HOMICIDIOS ÚNICOS</b> (cálculo propio; los dos motociclistas, en la 1): ARG-139-005 (Xalapa, dentro de su automóvil), ARG-139-007 (Ciudad Juárez, en una camioneta) y ARG-139-009 (San Luis Potosí, conductor perseguido). Línea: <b>vigilar el ataque a ocupantes de vehículos en vía pública y solicitar a las tres fiscalías el calibre de los casquillos</b> — sin vínculo entre entidades.
      <br><b>5. AGRESORES EN MOTOCICLETA EN DOS HECHOS PROPIOS Y DOS DEL ÍNDICE.</b> ARG-139-008 (Uruapan, «sujetos huyeron en moto», por titular de El Financiero), ARG-139-003 (Juchitán, solo por resumen), ARG-132-004 (Naucalpan) y ARG-130-002 (Cancún). Línea: <b>solicitar a las fiscalías de Michoacán y Oaxaca la descripción de las motocicletas y si existen videos de vigilancia</b> — hipótesis; modus operandi común, sin vínculo acreditado.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>NO REVISADA</code>; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>gob.mx/fgr</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: SINALOA, ZACATECAS Y OAXACA", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA: SINALOA, VERACRUZ E HIDALGO", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA: CHIHUAHUA, MICHOACÁN, SAN LUIS POTOSÍ Y SINALOA", co3)
 + page("CRIMEN ORGANIZADO (IV) — VENTANAS ANTERIORES: ARGOS 129 Y 138", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # el radar conserva la escala de dos días
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
