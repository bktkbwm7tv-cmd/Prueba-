# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 133: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-133.py <plantilla ARGOS 132> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "133", "2026-10-15", "07:16"
CONSULTA = "2026-10-15 07:16-07:45"
DUR = "22 h 57 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-133-001", estado="MX-HID", region="Centro", color="rojo", impacto="grande", fecha="2026-10-14", hora="no fijada; boletín «la madrugada de este miércoles» (solo por resumen)",
  ent="Hidalgo", mun="Atotonilco de Tula (localidad Texas)", dia="PUB. 14-OCT, HORA NO FIJADA",
  title="HIDALGO · ATOTONILCO DE TULA — LA COMISIÓN DE BÚSQUEDA LOCALIZA UNA FOSA CLANDESTINA CON CINCO CUERPOS EN LA LOCALIDAD TEXAS",
  hecho="Atotonilco de Tula · <code>LOCALIDAD TEXAS, LÍMITE CON EL ESTADO DE MÉXICO</code> · publicado el MIÉRCOLES 14-OCT · <b>Comisión de Búsqueda de Personas de Hidalgo</b> localiza una <b>fosa clandestina</b>, por titular (🔴) · <b>5 cuerpos</b>, por titular · <b>PGJ Hidalgo</b> procesa el sitio y recupera los cuerpos, por titular de un medio · búsqueda a petición de familiares de personas desaparecidas de Atotonilco, Tula y Atitalaquia, " + RES + " · <b>ninguna identificación</b> · <code>COINCIDENCIA CON UNA MUJER DESAPARECIDA EL 5-OCT: VERSIÓN NO CONFIRMADA, NO SE INTEGRA</code> · fecha de inicio de la excavación no publicada · " + FR,
  panel="<b>Fosa clandestina</b>: <b>5 cuerpos</b>",
  inst="Comisión de Búsqueda de Hidalgo <span class=\"muted-note\">(boletín por cita)</span>", nac="El Financiero · Infobae · El Heraldo de México · La Silla Rota · Milenio · TV Azteca", conf="★★★☆☆",
  campo="boletín institucional no leído; hora del hallazgo no fijada", I=1, N=6, R=4, A=0,
  fechadas=["El Financiero (2026/10/14)", "Infobae (2026/10/14)", "El Heraldo de México (2026/10/14)", "La Silla Rota (2026/10/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="Atotonilco de Tula no figura en ninguna edición de octubre; las menciones de agosto son otros hechos. NO son las dos sepulturas de La Cañada, mismo municipio (~8-oct, solo por resumen). Cuerpos, no víctimas identificadas. 🔴 por hallazgo de fosa clandestina"),
 dict(id="ARG-133-002", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-14", hora="~12:00 (solo por resumen)",
  ent="Guanajuato", mun="Salamanca (bulevar Valle de Santiago)", dia="14-OCT, ~12:00",
  title="GUANAJUATO · SALAMANCA — ATAQUE ARMADO FRENTE A LA CENTRAL CAMIONERA: DOS MUERTOS Y UN HERIDO",
  hecho="Salamanca · <code>BULEVAR VALLE DE SANTIAGO, FRENTE A LA CENTRAL CAMIONERA — COLONIA CONTRADICHA</code> · MIÉRCOLES 14-OCT, ~12:00 (" + RES + ") · ataque armado, por titular · <b>2 muertos y 1 herido</b>, por titular (🔴) · <code>SEXO DE LAS VÍCTIMAS CONTRADICHO: HOMBRE Y MUJER O DOS HOMBRES</code> · agresores en motocicleta, " + RES + " · <code>DETENIDOS: NO CONFIRMADOS</code> · <b>FGE Guanajuato</b> investiga · identidades: no se reproducen · " + FR,
  panel="Ataque armado: <b>2 muertos</b> y <b>1 herido</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Universal", conf="★★★☆☆",
  campo="hora y detenidos solo por resumen; sin fuente institucional", I=0, N=1, R=6, A=0,
  fechadas=["Periódico AM (2026/10/14)", "Periódico Correo (2026/oct/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="Salamanca figura solo en ARG-125-044 (otro hecho). NO es el ataque de Valle de Santiago del 4-oct (Infobae 2026/10/04). Forma parte de la cuenta de «ocho muertos en tres municipios» de El Universal, que suma hechos de la ventana de ARGOS 132 (Pénjamo, Silao): esa cifra no se reproduce. 🔴 por homicidio múltiple"),
 dict(id="ARG-133-003", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-14", hora="noche: aviso al 911 «minutos antes de las 8» o ~21:00 (solo por resumen)",
  ent="Guanajuato", mun="Romita (cerca del panteón municipal)", dia="14-OCT, NOCHE",
  title="GUANAJUATO · ROMITA — ATAQUE ARMADO JUNTO AL PANTEÓN MUNICIPAL: DOS MUERTOS Y UN HERIDO GRAVE",
  hecho="Romita · <code>CRUCE DE HÉROES DE CHAPULTEPEC Y ROCHA, CERCA DEL PANTEÓN MUNICIPAL</code> · noche del MIÉRCOLES 14-OCT (" + RES + ") · ataque armado, por titular · <b>2 muertos y 1 herido grave</b>, por titular (🔴) · <code>MUERTE DEL HERIDO EN EL TRASLADO: EXTRAOFICIAL, NO SE INTEGRA</code> · Policía Municipal acordona; <b>FGE Guanajuato</b> hace peritajes, " + RES + " · <b>ningún detenido publicado</b> · identidades y móvil: no publicados",
  panel="Ataque armado: <b>2 muertos</b> y <b>1 herido grave</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="hora solo por resumen; dos medios regionales, sin fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Periódico Correo (2026/oct/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="Romita no figura en el índice ni en las tres ediciones previas. NO es ningún ataque en panteones de Culiacán, Morelia o Coyoacán devueltos por la misma búsqueda. 🔴 por homicidio múltiple"),
 dict(id="ARG-133-004", estado="MX-CMX", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-14", hora="tarde (solo por resumen)",
  ent="Ciudad de México", mun="Iztapalapa (tianguis El Salado, Santa Martha Acatitla)", dia="14-OCT, TARDE",
  title="CIUDAD DE MÉXICO · IZTAPALAPA — BALACERA EN EL TIANGUIS EL SALADO: UNA MUJER MUERTA Y COMPRADORES HERIDOS",
  hecho="Iztapalapa · <code>TIANGUIS EL SALADO, COL. SANTA MARTHA ACATITLA</code> · tarde del MIÉRCOLES 14-OCT (" + RES + ") · disparos dentro del tianguis durante una persecución contra dos hombres, " + RES + " · <b>1 mujer de ~60 años muerta</b>, por titular · <b>3 heridos</b>, por titular · <code>HERIDOS CONTRADICHOS: 3, 2 O 1 SEGÚN EL MEDIO</code> · víctimas ajenas al objetivo, " + RES + " (🔴) · <b>SSC</b> detiene a 1 hombre (ficha ARG-133-008) · identidades: no se reproducen",
  panel="Balacera en un tianguis: <b>1 mujer muerta</b> y <b>3 heridos</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Infobae · La Razón · La Jornada · Crónica · El Universal · N+", conf="★★★☆☆",
  campo="hora solo por resumen; número de heridos contradicho; sin boletín leído", I=0, N=6, R=3, A=0,
  fechadas=["Infobae (2026/10/14)", "La Razón (2026/10/14)", "La Jornada (2026/10/14)", "Crónica (2026/10/14)", "Sociedad Noticias (2026/10/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Salado no figura en el índice; las fichas previas de Iztapalapa (ARG-97-ARM-001, ARG-98-006, ARG-99-007, ARG-122-ARM-004) son otros hechos. Delito y detención en la misma ventana: dos fichas. <code>🔴 POR VÍCTIMAS MÚLTIPLES —1 MUERTA Y HERIDOS AJENOS— COMO EN ARGOS 126 (CÓCORIT); DECISIÓN REVISABLE POR EL DESTINATARIO</code>"),
 dict(id="ARG-133-005", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-10-14", hora="~11:00 (solo por resumen)",
  ent="Sinaloa", mun="Escuinapa (centro, calle Severiano Moreno)", dia="14-OCT, ~11:00",
  title="SINALOA · ESCUINAPA — ASESINAN A BALAZOS A UN EXDIRIGENTE GANADERO FRENTE A UN NEGOCIO FAMILIAR",
  hecho="Escuinapa · <code>CALLE SEVERIANO MORENO ENTRE FRANCISCO PÉREZ Y CENTENARIO, CERCA DEL DIF MUNICIPAL</code> · MIÉRCOLES 14-OCT, ~11:00 (" + RES + ") · hombres armados interceptan y disparan contra un <b>exdirigente de la Asociación Ganadera Local</b>, por titular · <b>1 muerto</b>, por titular (🟡) · una menor que lo acompañaba resulta ilesa, " + RES + " · <b>ningún detenido publicado</b> · móvil no publicado · identidad: no se reproduce · " + FR,
  panel="<b>Exdirigente ganadero asesinado</b> frente a un negocio familiar",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="MVS · Excélsior · TV Azteca", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=3, R=6, A=0,
  fechadas=["MVS Noticias (2026/10/14)", "El Diario de Juárez (2026/oct/14)", "Tribuna (2026/10/14)", "Infobae (2026/10/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="NO es el coordinador municipal de Protección Civil (ARG-130-009), ni ARG-131-004 (estética), ni ARG-129-004 (vendedora), ni ARG-130-006 (El Roblito), ni el homicidio del Malecón Siglo XXI (ARG-133-REC-004). Cargo gremial, no servidor público. 🟡 por homicidio doloso único"),
 dict(id="ARG-133-006", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-14", hora="no publicada",
  ent="Baja California", mun="Tijuana (Zona Industrial Pacífico)", dia="PUB. 14-OCT, HORA NO FIJADA",
  title="BAJA CALIFORNIA · TIJUANA — UN POLICÍA MUNICIPAL ES BALEADO AL DAR EL ALTO A UN VEHÍCULO CON REPORTE DE ROBO",
  hecho="Tijuana · <code>ZONA INDUSTRIAL PACÍFICO</code> · publicado el MIÉRCOLES 14-OCT · un agente de la <b>SSPCM</b> da el alto a un vehículo con reporte de robo; el conductor desciende y le dispara, por titular · <b>1 policía municipal herido</b>, por titular (🟡) · <code>GRAVEDAD CONTRADICHA: GRAVE O IMPACTOS EN UN BRAZO</code> · agresor en fuga · <b>ningún detenido publicado</b> · " + FR,
  panel="<b>Policía municipal herido</b> al dar el alto",
  inst="SSPC Tijuana <span class=\"muted-note\">(versión por cita)</span>", nac="N+", conf="★★★☆☆",
  campo="hora no publicada; versión de la corporación por cita", I=1, N=1, R=4, A=0,
  fechadas=["En Línea BC (2026/10/14)", "Tijuana en Línea (2026/10/14)", "Periodismo Negro (2026/10/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="Zona Industrial Pacífico no figura en el índice. 🟡: la autoridad inicia la acción (alto a un vehículo) y es agredida; sin muerte de personal"),
 dict(id="ARG-133-007", estado="MX-ROO", region="Sureste", color="amarillo", impacto="pequeno", fecha="2026-10-14", hora="mañana (solo por resumen)",
  ent="Quintana Roo", mun="Cancún (Región 201)", dia="PUB. 14-OCT, HORA NO FIJADA",
  title="QUINTANA ROO · CANCÚN — HALLAN A UN HOMBRE ASESINADO A BALAZOS EN UNA TERRACERÍA DE LA REGIÓN 201",
  hecho="Cancún · <code>REGIÓN 201, TERRACERÍA AL FINAL DE LA CALLE HACIENDA CHUNCHUCMIL</code> · publicado el MIÉRCOLES 14-OCT; hallazgo por la mañana, " + RES + " · <b>1 hombre muerto con impactos de bala</b>, por titular (🟡) · en la misma zona donde días antes se halló a una mujer asesinada, por titular · <b>ningún detenido publicado</b> · identidad: no publicada · " + FR,
  panel="Hallazgo de <b>1 hombre asesinado</b> a balazos",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="una sola fuente con fecha; hora no fijada", I=0, N=0, R=3, A=0,
  fechadas=["Por Esto (2026/10/14)"], estatus="Pendiente de corroboración", arm=None,
  desl="Región 201 no figura en el índice ni en las tres ediciones previas. NO es el homicidio del conductor de plataforma en la SM 254 (madrugada del 14-oct, sin URL con fecha: candidato). 🟡 por homicidio doloso único"),
 dict(id="ARG-133-008", estado="MX-CMX", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-14", hora="tarde (solo por resumen)",
  ent="Ciudad de México", mun="Iztapalapa (tianguis El Salado)", dia="14-OCT, TARDE",
  title="CIUDAD DE MÉXICO · IZTAPALAPA — LA SSC DETIENE A UN PRESUNTO RESPONSABLE DE LA BALACERA DEL TIANGUIS EL SALADO",
  hecho="Iztapalapa · tarde del MIÉRCOLES 14-OCT · la <b>SSC</b> detiene a un hombre de 21 años tras revisar el vehículo en que huía, por titular («capturan a un presunto responsable») · <b>1 detenido</b> (🟢) · <code>1 ARMA DE FUEGO Y EL VEHÍCULO ASEGURADOS, SOLO POR RESUMEN; TIPO DE ARMA NO PUBLICADO</code> · otros responsables: SSC analiza cámaras, " + RES + " · identidad: no se reproduce",
  panel="<b>1 detenido</b> por la balacera del tianguis",
  inst="SSC CDMX <span class=\"muted-note\">(por cita)</span>", nac="Infobae · La Razón · La Jornada", conf="★★★☆☆",
  campo="aseguramiento del arma solo por resumen; boletín SSC no leído", I=1, N=3, R=1, A=0,
  fechadas=["Infobae (2026/10/14)", "La Razón (2026/10/14)", "La Jornada (2026/10/14)"], estatus="Parcialmente corroborado", arm=None, cual=True,
  desl="Detención del mismo hecho de ARG-133-004, en la misma ventana: ficha propia en 🟢. Arma sin tipo ni cifra citable: evento cualitativo, fuera del conteo"),
 dict(id="ARG-133-009", estado="MX-CAM", region="Sureste", color="verde", impacto="mediano", fecha="2026-10-14", hora="no publicada",
  ent="Campeche", mun="Ciudad del Carmen", dia="ANUNCIO 14-OCT, HECHO NO FIJADO",
  title="CAMPECHE · CIUDAD DEL CARMEN — FUERZAS FEDERALES DETIENEN A «LA PATRONA», SEÑALADA OPERADORA DE UNA CÉLULA DE EXTORSIÓN Y SECUESTRO",
  hecho="Ciudad del Carmen · publicado el MIÉRCOLES 14-OCT · <code>FECHA DE LA DETENCIÓN NO PUBLICADA</code> · fuerzas federales cumplen una <b>orden de aprehensión por asociación delictuosa</b>, " + RES + " · detención de Noemí «N», «La Patrona», señalada operadora de una <b>célula de extorsión y secuestro</b> ligada a Jalpa de Méndez, Tabasco, por titular · <b>1 detenida</b> (🟢) · corporaciones: GN, SSPC y Defensa, " + RES + " · acusaciones, no condena · sin armamento publicado · " + FR,
  panel="Detenida la señalada operadora de una <b>célula de extorsión y secuestro</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Infobae", conf="★★★☆☆",
  campo="fecha de la detención y corporación solo por resumen", I=0, N=1, R=2, A=0,
  fechadas=["Infobae (2026/10/14)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no publicada; publicada el 2026-10-14",
  desl="NO es «La Patrona» de ARG-96-003 (operativo de narcotráfico de agosto en ocho estados). Ciudad del Carmen no figura en las tres ediciones previas. Sin armamento: fuera del conteo"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-133-REC-001", estado="MX-GUA", region="Occidente", fecha="2026-10-14", hora="~05:35 (solo por resumen)", orig="ARGOS 132", col_orig="rojo",
  ent="Guanajuato", mun="Pénjamo (col. San Miguel)", dia="14-OCT, MADRUGADA",
  title="GUANAJUATO · PÉNJAMO — COMANDO ASESINA A TRES PERSONAS, INCENDIA LA VIVIENDA E INTENTA QUEMAR UN TRÁILER EN LA CARRETERA A LA PIEDAD",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 132</code> · <code>COL. SAN MIGUEL</code> · MIÉRCOLES 14-OCT, desde ~05:35 (" + RES + ") · un grupo armado entra a una vivienda, dispara contra sus ocupantes y la incendia, por titular · <b>3 muertos</b>, por titular (🔴 en su ventana) · <code>SEXO DE LAS VÍCTIMAS CONTRADICHO</code> · disparos contra un negocio de la col. Las Américas y junto a la Dirección de Seguridad Pública, por titular · <b>intento de incendiar un tráiler</b> en la carretera federal rumbo a La Piedad, " + RES + "; «narcobloqueo», por titular de un medio · <b>ningún detenido publicado</b>",
  panel="Ataque a una vivienda: <b>3 muertos</b>; intento de bloqueo carretero", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Universal · N+",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=2, R=6, A=0,
  fechadas=["Periódico AM (2026/10/14)", "Periódico Correo (2026/oct/14)", "Proyecto Puente (2026/10/14)", "El Vigía (2026/10/14)"],
  desl="Pénjamo figura solo en ARG-94-001 y ARG-113-ARM-002 (otros hechos). Ocurrió antes de las 08:19 del 14-oct: <b>omisión de ARGOS 132</b>. 🔴 en su ventana por homicidio múltiple"),
 dict(id="ARG-133-REC-002", estado="MX-GUA", region="Occidente", fecha="2026-10-14", hora="reporte ~08:00 (solo por resumen)", orig="ARGOS 132 — 133 SI FUE DESPUÉS DE LAS 08:19", col_orig="rojo",
  ent="Guanajuato", mun="Silao (Veta de Ramales, rancho El Vergel)", dia="14-OCT, MAÑANA",
  title="GUANAJUATO · SILAO — DOS HOMBRES ASESINADOS A BALAZOS EN UN RANCHO DE VETA DE RAMALES",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 132 —133 SI FUE DESPUÉS DE LAS 08:19— HORA NO FIJADA</code> · <code>VETA DE RAMALES, RANCHO EL VERGEL</code> · mañana del MIÉRCOLES 14-OCT, reporte ~08:00 (" + RES + ") · <b>2 hombres muertos</b> a balazos, por titular (🔴 en su ventana) · aparente riña entre trabajadores del rancho, " + RES + " · <b>ningún detenido publicado</b>",
  panel="<b>2 hombres asesinados</b> en un rancho", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Universal · Milenio · N+",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=3, R=4, A=0,
  fechadas=["Periódico AM (2026/10/14)", "Periódico Correo (2026/oct/14)"],
  desl="Veta de Ramales no figura en el índice. Distinto del ataque de la col. Sopeña (ARG-133-REC-003), minutos antes: los medios los suman como «tres muertos en Silao». 🔴 en su ventana por homicidio múltiple"),
 dict(id="ARG-133-REC-003", estado="MX-GUA", region="Occidente", fecha="2026-10-14", hora="~06:00–06:40 (solo por resumen)", orig="ARGOS 132", col_orig="amarillo",
  ent="Guanajuato", mun="Silao (col. Sopeña)", dia="14-OCT, MADRUGADA",
  title="GUANAJUATO · SILAO — ASESINAN A UN HOMBRE Y SE LLEVAN A SU HERMANO EN LA COLONIA SOPEÑA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 132</code> · <code>COL. SOPEÑA</code> · MIÉRCOLES 14-OCT, ~06:00–06:40 (" + RES + ") · <b>1 hombre asesinado</b>, por titular (🟡 en su ventana) · <b>1 hombre privado de la libertad</b>, por titular · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>1 asesinado</b> y <b>1 privado de la libertad</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Universal · Milenio · N+",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=3, R=4, A=0,
  fechadas=["Periódico AM (2026/10/14)", "Periódico Correo (2026/oct/14)"],
  desl="NO es ARG-118-ARM-003 (Sopeña, 8-sep, aseguramiento). Omisión de ARGOS 132. 🟡 en su ventana por homicidio doloso único; la privación de la libertad de una persona no es desaparición múltiple"),
 dict(id="ARG-133-REC-004", estado="MX-SIN", region="Noroeste", fecha="2026-10-13", hora="~19:20 (solo por resumen)", orig="ARGOS 132", col_orig="amarillo",
  ent="Sinaloa", mun="Escuinapa (centro, Malecón Siglo XXI)", dia="13-OCT, NOCHE",
  title="SINALOA · ESCUINAPA — ASESINAN A BALAZOS AL ENCARGADO DE UN EXPENDIO EN EL MALECÓN SIGLO XXI",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 132</code> · <code>SEVERIANO MORENO Y MALECÓN SIGLO XXI, CENTRO</code> · MARTES 13-OCT, ~19:20 (" + RES + ") · <b>1 hombre asesinado</b> dentro de un depósito de cerveza, por titular (🟡 en su ventana) · <code>MÓVIL CONTRADICHO: INTENTO DE ROBO O ATAQUE DIRECTO</code> · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>1 hombre asesinado</b> en un expendio", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Luz Noticias (2026-10-13)", "Línea Directa (2026-10-13)"],
  desl="ARGOS 132 lo dejó como candidato sin URL con fecha: <b>recuperación por anclaje posterior</b>. NO es ARG-133-005, ARG-131-004 ni ARG-129-004"),
 dict(id="ARG-133-REC-005", estado="MX-SON", region="Noroeste", fecha="2026-10-13", hora="madrugada (solo por resumen)", orig="ARGOS 131", col_orig="amarillo",
  ent="Sonora", mun="Cajeme (Ciudad Obregón, col. México)", dia="13-OCT, MADRUGADA",
  title="SONORA · CAJEME — PERSECUCIÓN DE HOMBRES ARMADOS: UNO MUERTO, CUATRO DETENIDOS Y DOS PATRULLAS CON IMPACTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131</code> · <code>COL. MÉXICO HACIA EL CAMPO SAN ISIDRO</code> · madrugada del MARTES 13-OCT (" + RES + ") · aviso al C5i por personas armadas en un sedán; persecución de <b>Marina, Policía Estatal y Municipal</b> · <b>1 muerto en el vehículo</b> · <b>4 detenidos</b> · <b>2 patrullas con impactos</b> · <code>QUIÉN INICIÓ: NO DETERMINADO</code> (🟡 en su ventana) · FGJES: carpeta por tentativa de homicidio contra servidores públicos, " + RES + " · aseguradas 5 ponchallantas y 1 casquillo 9 mm, " + RES,
  panel="Persecución: <b>1 muerto</b>, <b>4 detenidos</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="Infobae",
  conf="★★★☆☆", campo="cifras y hora solo por resumen; iniciador no determinado", I=0, N=1, R=3, A=0,
  fechadas=["Infobae (2026/10/15)", "Proyecto Puente (2026/10/14)", "El Imparcial (2026/10/14)", "Infoson (2026/10/14)"],
  desl="NO es ARG-119-007 (taquería de la col. Reforma, 10-sep). Antes de las 07:23 del 13-oct: <b>omisión de ARGOS 131</b>. 🟡: iniciador no determinado; el muerto no mueve el color. Sin arma de fuego asegurada: fuera del conteo"),
 dict(id="ARG-133-REC-006", estado="MX-ZAC", region="Noreste", fecha="2026-10-11", hora="no publicada", orig="ARGOS 129 o ARGOS 130 — HORA NO FIJADA", col_orig="rojo",
  ent="Zacatecas", mun="Jerez", dia="11-OCT, HORA NO FIJADA",
  title="ZACATECAS · JEREZ — MADRES BUSCADORAS HALLAN UNA FOSA CON RESTOS HUMANOS CALCINADOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 129 O ARGOS 130 — HORA NO FIJADA</code> · DOMINGO 11-OCT, " + RES + " · el colectivo <b>Buscadoras Zacatecas</b> localiza una <b>fosa</b> con presuntos <b>restos humanos calcinados</b>, por titular («zona de exterminio») (🔴 en su ventana) · número de víctimas: no publicado · <b>FGJEZ</b> resguarda el predio; extracción en curso el 14-oct, " + RES,
  panel="<b>Fosa</b> con restos calcinados", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="ABC Noticias",
  conf="★★☆☆☆", campo="una sola fuente con fecha; día del hallazgo solo por resumen", I=0, N=1, R=0, A=0,
  fechadas=["ABC Noticias (2026/10/14)"],
  desl="Jerez no figura en las ediciones de octubre; NO son los cuatro restos de una finca de junio. Primera publicación no localizada. 🔴 en su ventana por hallazgo de fosa"),
 dict(id="ARG-133-REC-007", estado="MX-NAY", region="Occidente", fecha="2026-10-09", hora="no publicada", orig="ARGOS 128 (127 si fue antes de las 07:20) — HORA NO FIJADA", col_orig="rojo",
  ent="Nayarit", mun="Tecuala (La Presa)", dia="9-OCT, HORA NO FIJADA",
  title="NAYARIT · TECUALA — HALLAN UNA FOSA CLANDESTINA CON RESTOS HUMANOS: AL MENOS CUATRO CUERPOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 128 —127 SI FUE ANTES DE LAS 07:20— HORA NO FIJADA</code> · <code>LA PRESA</code> · VIERNES 9-OCT · <b>fosa clandestina con restos humanos</b>, por titular (🔴 en su ventana) · <b>al menos 4 cuerpos</b>, " + RES + " · <b>FGE Nayarit sin comunicado</b>, " + RES,
  panel="<b>Fosa clandestina</b>: al menos 4 cuerpos", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★☆☆☆", campo="cifra solo por resumen; sin fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["NTV (2026/10/09)"],
  desl="Tecuala no figura en el índice. Es la «fosa clandestina en zona norte» de Meganoticias 778257, que la agrupó con ARG-132-REC-004 (Acaponeta, sin fosa). NO es La Curva, Xalisco (ARG-125-003). 🔴 en su ventana por hallazgo de fosa"),
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
assert TOT == [0] * 10, TOT
assert cnt == {"rojo": 4, "amarillo": 3, "verde": 2}, cnt
assert cnt_rec == {"rojo": 4, "amarillo": 3, "verde": 0}, cnt_rec
assert len(ENT) == 7, ENT

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else ("sin fila — evento cualitativo, cantidad no determinada" if e.get("cual") else "sin fila — no hubo armamento asegurado"))
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
head = head.replace("<title>ARGOS 132 — Reporte Nacional de Seguridad — 2026-10-14</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA PROCURADURÍA DE HIDALGO LA IDENTIFICACIÓN DE LOS RESTOS DE LA FOSA DE ATOTONILCO DE TULA</b> (ARG-133-001).
      <br><b>2. SOLICITE A LA SECRETARÍA DE SEGURIDAD DE TIJUANA EL PARTE DE LA AGRESIÓN A SU AGENTE</b> (ARG-133-006).
      <br><b>3. SOLICITE A LA FISCALÍA DE LA CIUDAD DE MÉXICO EL DICTAMEN DEL ARMA ASEGURADA EN EL TIANGUIS EL SALADO</b> (ARG-133-008).
      <br><b>4. SOLICITE A LA FISCALÍA DE QUINTANA ROO EL COTEJO DE LOS DOS HALLAZGOS DE LA REGIÓN 201</b> (ARG-133-007).
      <br><b>5. SOLICITE A LA FISCALÍA DE VERACRUZ LA IDENTIDAD DEL MUERTO EN EL CATEO DE ORIZABA</b> (ARG-132-002).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>14-oct 08:19 → 15-oct 07:16 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,39 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>. <b>Seis de nueve</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <b>Ningún aseguramiento de armamento con cifra integrable en hechos propios</b>. <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento de armamento</b>; los de ARG-133-008 (arma sin cifra citable) y ARG-133-009 (sin armas) no entran. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios</b>: <b>7</b> por agresión —Salamanca 2, Romita 2, Iztapalapa 1, Escuinapa 1 y Cancún 1— y <b>5 cuerpos</b> en la fosa de Atotonilco de Tula. <b>Heridos: 6</b> —Salamanca 1, Romita 1, Iztapalapa 3 (contradicho) y 1 policía en Tijuana—. <b>Cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:4])
co2 = "\n".join(ficha(e) for e in E[4:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA ARMA CORTA CON CIFRA EN HECHO PROPIO</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA CON CIFRA EN HECHO PROPIO</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR INTEGRADA</code> · Iztapalapa, cualitativo"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>NINGÚN CARTUCHO CON CIFRA EN HECHO PROPIO</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN CARGADOR CON CIFRA EN HECHO PROPIO</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>Ninguna fila de armamento en la ventana</b>: ningún hecho propio publicó aseguramiento con cifra integrable. <code>SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Gris = sin aseguramiento de armamento con cifra integrable en la ventana. La sola presencia de armas no vuelve roja a una entidad.</div>
  </div>
'''

arm2 = f'''  <div class="table-wrap"><table class="exec wide">
    <thead><tr>
      <th>ARG-ID</th><th>Entidad</th><th>Municipio</th><th>Fecha del hecho</th>
      <th>Cortas</th><th>Largas</th><th>Sin categoría</th><th>Especial</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th>
      <th>Detenidos</th><th>Corporación</th><th>Confianza</th>
    </tr></thead>
    <tbody>
      <tr><td colspan="16"><code>SIN FILAS — NINGÚN ASEGURAMIENTO DE ARMAMENTO CON CIFRA INTEGRABLE EN LA VENTANA</code></td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: <b>0 filas</b> en las seis regiones. <b>Evento cualitativo</b>: ARG-133-008 (Iztapalapa, 1 arma de fuego sin tipo, solo por resumen).
    <br><code>VISTOS, NO INTEGRADOS</code>: San Luis Potosí, balance de 24 horas de la Guardia Civil Estatal publicado el 14-oct (agregado sin municipio; 1 arma sin tipo) · Centro, Tabasco, vinculación a proceso de 8 detenidos con 5 armas sin desglose (publicada el 15-oct; fecha del aseguramiento no fijada) · Juventino Rosas, Guanajuato, 3 armas sin desglose y 239 cartuchos (FGR; fecha del hecho no fijada).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: <b>Orizaba</b> (ARG-132-002), cateo del 13-oct: <b>3 largas, 2 cortas y 4 detenidos</b>, por cita de la FGE en medios · <b>Querétaro</b>, cateos simultáneos de madrugada del 14-oct en Colón, Amealco, Querétaro y San Juan del Río: <b>10 detenidos</b>, por titular del boletín de la Fiscalía; 1 corta y 2 artesanales, solo por resumen · <b>Villa Unión, Sinaloa</b>: captura de un operador de Los Rugrats, armas sin cifra (comunicado citado: 13-oct) · boletín del Gabinete de Seguridad de las acciones del <b>13-oct</b>, por republicadores (RED113, Talla Política, Certeza Diario): San Miguel del Brete, Gto, 1 larga, 2 cortas, 1 cargador, 73 cartuchos, 1 detenido; San Francisco Tlalcilalcalpan, Edomex, 1 larga, 2 cortas, 3 detenidos; Concordia, Sin, 1 arma, 7 cargadores, 199 cartuchos — <b>todo solo por resumen</b>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas, abajo, no se integran</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>15 estatales revisadas</b> · 17 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Chihuahua</b><br>Casas Grandes</td><td>Daniel «N» · <span class="muted-note">portación de arma de uso exclusivo; abreviado</span></td><td><b>8 años</b>, por titular</td><td>FGR <span class="muted-note">(titular de republicador)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · 860 Líder Informativo 2026/10/14 · fecha de la sentencia no publicada</td><td>Bajo</td></tr>
      <tr><td><b>Sinaloa</b></td><td>Sin nombre publicado · <span class="muted-note">portación de armas</span></td><td><b>más de 8 años</b>, por titular</td><td>FGR <span class="muted-note">(titular de medio)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Línea Directa 2026-10-14 · municipio y fecha de sentencia no publicados</td><td>Bajo</td></tr>
      <tr><td><b>Oaxaca</b><br>San Antonio de la Cal</td><td>A.J.B. · <span class="muted-note">feminicidio agravado de 2021</span></td><td><b>80 años</b>, por titular</td><td>FGEO <span class="muted-note">(boletín 2,889, título solo por resumen)</span></td><td>Boletín del 13-oct, solo por resumen; El Heraldo de México 2026/10/14 lo publica · <code>BOLETÍN SIN URL CON DÍA</code></td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Tres culpables · <span class="muted-note">feminicidio y homicidio</span></td><td><code>SIN PENA: INDIVIDUALIZACIÓN APLAZADA AL 21-OCT</code>, solo por resumen</td><td>PGJ Hidalgo <span class="muted-note">(por cita)</span></td><td>Fallo del 8-9 oct; <b>no es sentencia</b> hasta la individualización · La Silla Rota 2026/10/14</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Nuevo León, 155 años y 80 a cada uno de tres (12-13 oct) · Zacatecas, Juan «N», 10 años (13-oct) · Sonora, Nogales, 15 años (12-oct) · FGR Chihuahua, Lorenzo «N», 7 años 1 mes (12-oct) · Sinaloa, Navolato, 40 años (12-oct). <b>Sin fecha anclada</b>: Zacatecas, FGR, dos sentenciados a 4 años · Nayarit, 53 años por desaparición. <code>NO SE INTEGRAN: FUERA DE VENTANA O SIN BOLETÍN OFICIAL.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>15 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · BC, Dgo · NL, Zac · Gto · Edomex, Mor, Pue, Qro · Ver, Tab · Gro, Oax, Chis, Yuc</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada</b></td><td><b>1</b>: Oaxaca (FGEO), <b>no integrable</b> · <b>con sentencia integrable: 0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>14</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>17</b>: BCS, Son, Chih, Sin · Coah, Tamps, SLP · Jal, Col, Nay, Ags, Mich · CDMX, Tlax, Hgo · Camp, QRoo</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 32 de 32 por búsqueda dirigida en medios</b> · <b>armamento: 19 de 32</b>; <code>NO REVISADA</code>: BC, BCS, Son · SLP · Jal, Col, Nay, Mich · Pue, Tlax, Hgo · Tab · Camp · <code>ARMAMENTO Y SENTENCIAS: REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, Defensa, Marina y FGR: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 13-oct</b>: existe, <b>solo por republicadores</b>, publicado el 14-oct · <b>acciones del 14-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 15-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR CUATRO ROJOS</b>: ARG-133-001 (Hidalgo) · ARG-133-002 y ARG-133-003 (Guanajuato) · ARG-133-004 (Ciudad de México).
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-133-005 a ARG-133-007.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-133-008 y ARG-133-009.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-133-REC-001 a ARG-133-REC-007.
      <br><b>5.</b> <code>22 H 57 MIN; SEIS DE NUEVE HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. HOMICIDIOS MÚLTIPLES EN EL BAJÍO GUANAJUATENSE.</b> ARG-133-002, ARG-133-003 y ARG-133-REC-001 a -REC-003: cinco ataques en cuatro municipios el 14-oct, de madrugada a noche, <b>cálculo propio</b>; vínculo entre ellos no acreditado.
      Línea: <b>solicitar a la FGE Guanajuato el cotejo balístico</b> de los cinco — hipótesis.
      <br><b>2. FOSAS HALLADAS POR COLECTIVOS.</b> ARG-133-REC-006 (Jerez) y ARG-133-REC-007 (Tecuala), con ARG-132-001 (Navolato): tres hallazgos de buscadoras en una semana, ninguno con víctimas identificadas. Línea: <b>solicitar a las fiscalías de Zacatecas y Nayarit</b> el número de víctimas y la toma de muestras genéticas.
      <br><b>3. VIOLENCIA SOSTENIDA EN ESCUINAPA.</b> ARG-133-005 y ARG-133-REC-004, con ARG-129-004, ARG-130-006, ARG-130-009 y ARG-131-004: seis homicidios del 10 al 14-oct, <b>cálculo propio</b>. Línea: <b>solicitar a la Fiscalía de Sinaloa</b> si las seis carpetas comparten indicios — hipótesis.
      <br><b>4. CÉLULAS DE EXTORSIÓN Y SECUESTRO EN EL SURESTE.</b> ARG-133-009 (Ciudad del Carmen, célula ligada a Jalpa de Méndez). Línea: <b>solicitar a la SSPC</b> los integrantes pendientes de captura — requiere validación.
      <br><b>5. BRECHA ENTRE FALLO Y PENA.</b> Santiago Tulantepec: culpables desde el 8-9 oct, individualización aplazada al 21-oct, solo por resumen; Oaxaca: fallo del 24-sep, pena publicada en octubre. Línea: <b>solicitar a las fiscalías los tiempos procesales</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>; el balance de detenidos de la SSPC del 14-oct es un acumulado, no del corte.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: ATOTONILCO DE TULA, SALAMANCA, ROMITA E IZTAPALAPA", co1)
 + page("CRIMEN ORGANIZADO (II) — ESCUINAPA, TIJUANA, CANCÚN, IZTAPALAPA Y CIUDAD DEL CARMEN", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES: VENTANAS DE ARGOS 128 A 132", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 14-oct 08:19 → 15-oct 07:16 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R))
