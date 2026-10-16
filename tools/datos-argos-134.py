# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 134: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-134.py <plantilla ARGOS 133> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "134", "2026-10-16", "11:34"
CONSULTA = "2026-10-16 11:34-12:05"
DUR = "28 h 18 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-134-001", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-15", hora="~15:30 (solo por resumen; otra versión, ~14:00)",
  ent="Guanajuato", mun="Silao (Barrio Nuevo)", dia="PUB. 15-OCT, DÍA SOLO POR RESUMEN",
  title="GUANAJUATO · SILAO — ATAQUE ARMADO EN BARRIO NUEVO: TRES HOMBRES ASESINADOS AFUERA DE UNA TIENDA",
  hecho="Silao · <code>BARRIO NUEVO, CRUCE DE 16 DE SEPTIEMBRE Y SAN AGUSTÍN, AFUERA DE UNA TIENDA</code> · JUEVES 15-OCT, ~15:30 (" + RES + ") · <code>DÍA DEL HECHO SOLO POR RESUMEN; PUBLICACIÓN DEL 15-OCT POR RUTA; UN EQUIPO LO FECHÓ EL MIÉRCOLES 14: SI SE CONFIRMA, ES DE ARGOS 133</code> · ataque armado, por titular · <b>3 hombres muertos</b>, por titular (🔴) · agresores en motocicleta, " + RES + " · <b>FGE Guanajuato</b> investiga, " + RES + " · <b>ningún detenido publicado</b> · identidades y móvil: no publicados · " + FR,
  panel="Ataque armado: <b>3 hombres muertos</b>",
  inst=SB, nac="N+", conf="★★★☆☆",
  campo="día y hora solo por resumen; sin fuente institucional", I=0, N=1, R=6, A=0,
  fechadas=["Periódico AM (2026/10/15)", "Periódico Correo (2026/oct/15)", "Noticieros en Línea (2026/oct/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Barrio Nuevo no figura en las tres ediciones previas. NO es el ataque del 2-oct en la misma colonia (Correo 2026/oct/02), ni ARG-133-REC-002 (Veta de Ramales) ni ARG-133-REC-003 (Sopeña). 🔴 por homicidio múltiple"),
 dict(id="ARG-134-002", estado="MX-NLE", region="Noreste", color="rojo", impacto="mediano", fecha="2026-10-15", hora="~12:00–12:10 (solo por resumen)",
  ent="Nuevo León", mun="Monterrey / San Pedro Garza García (Gómez Morín)", dia="15-OCT, ~12:10",
  title="NUEVO LEÓN · MONTERREY — EJECUTAN A DOS HOMBRES DENTRO DE UN AUTOMÓVIL EN LA RAMPA DE GÓMEZ MORÍN",
  hecho="Límite Monterrey–San Pedro Garza García · <code>RAMPA DE AV. GÓMEZ MORÍN HACIA MORONES PRIETO</code> · JUEVES 15-OCT, ~12:10 (" + RES + ") · disparos contra un automóvil, por titular · <b>2 hombres muertos</b>, por titular (🔴) · <b>ningún detenido</b>, por <i>slug</i> · <b>FGJ Nuevo León</b> procesa el sitio, " + RES + " · <code>AMBAS VÍCTIMAS EXPOLICÍAS, SEÑALADAS POR LA SSP NUEVO LEÓN COMO EXINTEGRANTES DE UNA ESTRUCTURA CRIMINAL: POR TITULAR, CITA DE SEGUNDA MANO</code> · identidades: no se reproducen",
  panel="Ataque a un automóvil: <b>2 hombres muertos</b>",
  inst="SSP Nuevo León <span class=\"muted-note\">(declaración por cita)</span>", nac="El Universal · Milenio · Reforma · MVS · diario.mx", conf="★★★☆☆",
  campo="hora solo por resumen; versión oficial solo por cita en medios", I=1, N=5, R=4, A=0,
  fechadas=["Publimetro (2026/10/15)", "Grupo Marmor (2026/10/15)", "MVS Noticias (2026/10/15)", "ABC Noticias (2026/10/15)", "Diario de Yucatán (2026/10/15)", "ABC Noticias (2026/10/16)"], estatus="Parcialmente corroborado", arm=None,
  desl="Gómez Morín no figura en las tres ediciones previas ni en el índice. Mismo hecho que «Matan a 2 ex policías ligados a narcogrupo» (Reforma, El Norte, diario.mx 2026/oct/16): no se cuenta dos veces. Reserva: exautoridades. 🔴 por homicidio múltiple"),
 dict(id="ARG-134-003", estado="MX-COL", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-15", hora="~17:40 (solo por resumen)",
  ent="Colima", mun="Coquimatlán (centro, calle Hidalgo)", dia="15-OCT, TARDE",
  title="COLIMA · COQUIMATLÁN — ATAQUE ARMADO EN EL CENTRO: DOS O TRES MUERTOS, UNA MENOR ENTRE ELLOS (CONTRADICHO)",
  hecho="Coquimatlán · <code>CENTRO, CALLE HIDALGO</code> · JUEVES 15-OCT, ~17:40 (" + RES + ") · ataque armado, por titular · <code>MUERTOS CONTRADICHOS: 3 —DOS MUJERES, UNA MENOR, Y UN HOMBRE— (AFMEDIOS, VADENUEZ) O 2 MUERTOS Y 1 LESIONADA (MEGANOTICIAS) O DOS MUJERES MUERTAS Y UN HOMBRE HERIDO (COLIMANOTICIAS), POR TITULAR</code> (🔴) · el hombre murió a una cuadra y media al huir, " + RES + "; hora y día solo por resumen · <b>ningún detenido publicado</b> · FGE Colima: sin comunicado localizado",
  panel="Ataque armado: <b>2 a 3 muertos</b>, una de ellas menor (contradicho)",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="número de muertos contradicho; fecha solo por la página de archivo de un medio", I=0, N=0, R=4, A=0,
  fechadas=["vadenuez.info (archivo 2026/10/15)"], estatus="Pendiente de corroboración", arm=None,
  desl="Coquimatlán no figura en las tres ediciones previas ni en el índice. La nota de AFmedios «un muerto y 3 personas lesionadas» (sin fecha) puede ser otro hecho: no se integra. 🔴 por homicidio múltiple"),
 dict(id="ARG-134-004", estado="MX-MEX", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-15", hora="contradicha: «minutos después de las 7» o ~08:00 (solo por resumen)",
  ent="Estado de México", mun="Tlalnepantla de Baz (San Lucas Patoni)", dia="15-OCT, HORA NO FIJADA",
  title="ESTADO DE MÉXICO · TLALNEPANTLA — ABANDONAN DOS CUERPOS EMPLAYADOS EN SAN LUCAS PATONI, EN EL LÍMITE CON GUSTAVO A. MADERO",
  hecho="Tlalnepantla de Baz · <code>COL. SAN LUCAS PATONI, VENUSTIANO CARRANZA Y JOSÉ MARÍA MORELOS, LÍMITE CON GAM</code> · JUEVES 15-OCT · <code>HORA CONTRADICHA, SOLO POR RESUMEN: «MINUTOS DESPUÉS DE LAS 7» O ~08:00; COLINDA CON LA APERTURA</code> · hallazgo de <b>2 cuerpos emplayados</b>, por titular (🔴) · con huellas de violencia, " + RES + " · <code>SEXO CONTRADICHO: DOS HOMBRES (MILENIO) O NO DETERMINADO (LA SILLA ROTA)</code> · causa de muerte no publicada · cámaras captan a dos hombres que dejan los bultos, " + RES + " · <b>FGJEM</b> investiga, por titular · <b>ningún detenido publicado</b> · <code>REPRESALIA ORDENADA DESDE UN PENAL: VERSIÓN NO CONFIRMADA, NO SE INTEGRA</code> · " + FR,
  panel="Hallazgo de <b>2 cuerpos emplayados</b>",
  inst=SB, nac="La Silla Rota · Milenio · N+ · Infobae", conf="★★★☆☆",
  campo="hora del hallazgo contradicha y colindante con la apertura; sin fuente institucional", I=0, N=4, R=2, A=0,
  fechadas=["La Silla Rota (2026/10/15)", "Infobae (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Lucas Patoni no figura en las tres ediciones previas; ARG-125-022 es Tlalnepantla, Morelos (otro hecho). El muerto de Toluca y el de Ecatepec del mismo titular de Infobae no se fichan: sin segunda fuente. 🔴 por hallazgo de 2 cuerpos con huellas de violencia"),
 dict(id="ARG-134-005", estado="MX-PUE", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-16", hora="contradicha: 08:00, alerta 09:27 o «minutos antes de las 10:00» (solo por resumen)",
  ent="Puebla", mun="Puebla (col. Tres Cerritos, bulevar Carmelitas)", dia="16-OCT, MAÑANA, HORA NO FIJADA",
  title="PUEBLA · PUEBLA — ASESINAN A BALAZOS EN LA COLONIA TRES CERRITOS A UN HOMBRE SEÑALADO COMO POLICÍA ESTATAL",
  hecho="Puebla capital · <code>COL. TRES CERRITOS, BULEVAR CARMELITAS</code> · VIERNES 16-OCT, por la mañana · <code>HORA CONTRADICHA: 08:00, ALERTA 09:27 O MINUTOS ANTES DE LAS 10:00, SOLO POR RESUMEN</code> · agresores en motocicleta, por titular · <b>1 hombre muerto</b>, «policía estatal» en titulares de varios medios (🔴) · <code>CONDICIÓN DE POLICÍA SIN COMUNICADO DE SSP NI FGE; «PRESUNTO» EN UN TITULAR; «EN ACTIVO» O «EN SU DÍA DE DESCANSO»: CONTRADICHO</code> · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>Hombre señalado como policía estatal</b>, asesinado",
  inst=SB, nac="El Universal", conf="★★★☆☆",
  campo="condición de policía sin confirmación oficial; hora solo por resumen", I=0, N=1, R=5, A=0,
  fechadas=["Retodiario (2026/10/16)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tres Cerritos no figura en las tres ediciones previas. NO es ARG-131-003 (camioneta de la FGE, 12-oct). 🔴 por víctima policía · reserva: condición no confirmada oficialmente"),
 dict(id="ARG-134-006", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-10-15", hora="mañana; ~08:00 según la Fiscalía (solo por resumen)",
  ent="Michoacán", mun="Tangancícuaro (Patamban)", dia="15-OCT, MAÑANA, HORA NO FIJADA",
  title="MICHOACÁN · TANGANCÍCUARO — ASESINAN AL REPRESENTANTE DE BIENES COMUNALES DE PATAMBAN AFUERA DE SU DOMICILIO",
  hecho="Patamban, Tangancícuaro · afuera de su domicilio · JUEVES 15-OCT, por la mañana; ~08:00, " + RES + " · un hombre en motocicleta le dispara, " + RES + " · <b>1 muerto</b>: el <b>representante de bienes comunales</b> de Patamban, por titular; «líder indígena purépecha», por titular de MVS; murió en el traslado (🟡) · <code>DEFENSA DEL TERRITORIO COMO MÓVIL: NO DESCARTADA POR LA FISCALÍA, SOLO POR RESUMEN</code> · aviso a la <b>Fiscalía Regional de Zamora</b>, " + RES + " · <b>ningún detenido publicado</b> · móvil no determinado · identidad: no se reproduce · " + FR,
  panel="<b>Representante comunal asesinado</b>",
  inst=SB, nac="MVS", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["Grupo Marmor (2026/10/15)", "MVS Noticias (2026/10/15)", "Medianews (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Patamban no figura en las tres ediciones previas ni en el índice. 🟡 por homicidio doloso único · reserva: posible persona defensora, no acreditada"),
 dict(id="ARG-134-007", estado="MX-NLE", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="aviso ~18:45 (solo por resumen)",
  ent="Nuevo León", mun="Santa Catarina (Rincón de las Mitras)", dia="15-OCT, ~18:45",
  title="NUEVO LEÓN · SANTA CATARINA — ATAQUE A BALAZOS EN RINCÓN DE LAS MITRAS: UN HOMBRE MUERTO Y OTRO HERIDO GRAVE",
  hecho="Santa Catarina · <code>COL. RINCÓN DE LAS MITRAS</code> · JUEVES 15-OCT, aviso ~18:45 (" + RES + ") · ataque armado, por titular · <b>1 hombre muerto y 1 herido grave</b>, por titular (🟡) · agresores en motocicleta, " + RES + " · <b>ningún detenido publicado</b> · <code>RELACIÓN CON ARG-134-002 INVESTIGADA, NO CONFIRMADA</code>, por titular de un medio · identidades: no se reproducen",
  panel="Ataque armado: <b>1 muerto</b> y <b>1 herido</b>",
  inst=SB, nac="MVS · Milenio · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=3, R=2, A=0,
  fechadas=["MVS Noticias (2026/10/15)", "ABC Noticias (2026/10/15)", "Enfoque Monterrey (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Rincón de las Mitras no figura en las tres ediciones previas; «Santa Catarina» del índice es Loxicha, Oaxaca. 🟡 por homicidio doloso único"),
 dict(id="ARG-134-008", estado="MX-MOR", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="hacia el mediodía (solo por resumen)",
  ent="Morelos", mun="Yautepec (Oaxtepec, av. La Nacional)", dia="15-OCT, MEDIODÍA",
  title="MORELOS · YAUTEPEC — ASESINAN A BALAZOS A UNA COMERCIANTE DE DULCES EN OAXTEPEC",
  hecho="Oaxtepec, Yautepec · <code>SANTA ROSA, AV. LA NACIONAL</code> · JUEVES 15-OCT, hacia el mediodía (" + RES + ") · agresores en motocicleta disparan contra la propietaria de una dulcería, por titular · <b>1 mujer muerta</b>, por titular (🟡) · <b>FGE Morelos</b> investiga como feminicidio, por titular · <code>COBRO DE PISO: LÍNEA DE INVESTIGACIÓN NO CONFIRMADA</code>, por titular de un medio · <b>ningún detenido publicado</b>",
  panel="<b>Comerciante asesinada</b> a balazos",
  inst=SB, nac="MVS · Infobae · La Jornada · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=4, R=1, A=0,
  fechadas=["MVS Noticias (2026/10/15)", "Infobae (2026/10/16)", "La Jornada (2026/10/16)"], estatus="Parcialmente corroborado", arm=None,
  desl="Oaxtepec no figura en las tres ediciones previas. 🟡 por homicidio doloso único"),
 dict(id="ARG-134-009", estado="MX-CMX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="tarde (solo por resumen)",
  ent="Ciudad de México", mun="Azcapotzalco (col. Pasteros)", dia="15-OCT, TARDE",
  title="CIUDAD DE MÉXICO · AZCAPOTZALCO — ATACAN A BALAZOS UN AUTOMÓVIL TRAS UNA PERSECUCIÓN: DOS HOMBRES HERIDOS, UNO EXTRANJERO",
  hecho="Azcapotzalco · <code>COL. PASTEROS, AHUEHUETE Y AQUILES SERDÁN</code> · tarde del JUEVES 15-OCT (" + RES + ") · sujetos en motocicleta persiguen y disparan contra un automóvil, " + RES + " · <b>2 hombres heridos</b>, uno extranjero, por titular (🟡) · <code>UN MUERTO SEGÚN TV AZTECA: SOLO POR RESUMEN; SU <i>SLUG</i> DICE «HAY HERIDOS»: NO SE INTEGRA</code> · detención en ficha ARG-134-014",
  panel="Ataque a un automóvil: <b>2 heridos</b>",
  inst=SB, nac="El Heraldo de México · Infobae · N+ · TV Azteca", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=4, R=1, A=0,
  fechadas=["El Heraldo de México (2026/10/15)", "Infobae (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="El ataque no figura en las tres ediciones previas; la mención de Azcapotzalco en el archivo de fuentes de 133 es un hecho de junio. Delito y detención: dos fichas (ARG-134-014). 🟡 por ataque armado sin muertos"),
 dict(id="ARG-134-010", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="mañana, camino a la escuela (solo por resumen)",
  ent="Estado de México", mun="Coacalco (col. Zacuauhtitla)", dia="15-OCT, MAÑANA, HORA NO FIJADA",
  title="ESTADO DE MÉXICO · COACALCO — ATACAN A BALAZOS A UN EJIDATARIO Y A SU HIJA DE 13 AÑOS CAMINO A LA ESCUELA",
  hecho="Coacalco · <code>COL. ZACUAUHTITLA</code> · JUEVES 15-OCT, por la mañana (" + RES + ") · sujetos en motocicleta disparan contra un ejidatario y su hija, por titular · <b>2 heridos graves</b>: un hombre de 42 años, " + RES + ", y su hija de 13, por titular (🟡) · al menos 18 disparos, " + RES + " · <b>ningún detenido publicado</b> · " + FR,
  panel="Ataque armado: <b>2 heridos</b>, una de ellas menor",
  inst=SB, nac="La Silla Rota", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Seuno Noticias (2026/10/15)", "La Silla Rota (2026/10/15)", "Grupo Marmor (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Zacuauhtitla no figura en las tres ediciones previas. 🟡 por ataque armado sin muertos · reserva: víctima menor herida"),
 dict(id="ARG-134-011", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="hallazgo por la tarde (solo por resumen); hora de la muerte no publicada",
  ent="Veracruz", mun="Coatzacoalcos (fracc. Santa Cecilia)", dia="15-OCT, TARDE",
  title="VERACRUZ · COATZACOALCOS — HALLAN ASESINADA EN SU DEPARTAMENTO A UNA MÉDICA DEL IMSS-BIENESTAR; LA FISCALÍA INVESTIGA FEMINICIDIO",
  hecho="Coatzacoalcos · <code>FRACC. SANTA CECILIA</code> · JUEVES 15-OCT, hallazgo por la tarde (" + RES + ") · <b>1 mujer muerta</b> con heridas de arma blanca, médica del IMSS-Bienestar, por titular (🟡) · <b>FGE Veracruz</b> investiga como feminicidio, por titular · <code>EXPAREJA BUSCADA COMO PROBABLE RESPONSABLE: POR TITULAR DE UN MEDIO; SIN ORDEN PUBLICADA</code> · <b>ningún detenido</b> · <code>HORA DE LA MUERTE NO PUBLICADA</code>",
  panel="<b>Médica asesinada</b>: feminicidio en investigación",
  inst=SB, nac="MVS · Infobae", conf="★★★☆☆",
  campo="hora de la muerte no publicada; sin comunicado de la FGE", I=0, N=2, R=4, A=0,
  fechadas=["MVS Noticias (2026/10/15)", "Infobae (2026/10/16)", "Formato Siete (2026/10/16)", "El Independiente (2026/10/16)", "Quinto Poder (2026/10/16)"], estatus="Parcialmente corroborado", arm=None,
  desl="Santa Cecilia no figura en las tres ediciones previas. 🟡 por homicidio doloso único · reserva: servidora pública"),
 dict(id="ARG-134-012", estado="MX-SON", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="no fijada; «noche del jueves», ~20:30, solo por resumen",
  ent="Sonora", mun="Hermosillo (col. Villas del Seris)", dia="PUB. 15-OCT, HORA NO FIJADA",
  title="SONORA · HERMOSILLO — ASESINAN A BALAZOS A UN JOVEN EN LA COLONIA VILLAS DEL SERIS",
  hecho="Hermosillo · <code>COL. VILLAS DEL SERIS (VILLA DE SERIS, SEGÚN OTROS MEDIOS), AL SUR DE LA CIUDAD</code> · publicado el JUEVES 15-OCT · <code>HORA NO FIJADA: «NOCHE DEL JUEVES», ~20:30, SOLO POR RESUMEN</code> · ataque armado, por titular · <b>1 joven muerto</b>, por titular (🟡) · <b>ningún detenido publicado</b> · móvil no publicado · identidad: no se reproduce · " + FR,
  panel="<b>1 joven asesinado</b> a balazos",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["El Imparcial (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Villas del Seris no figura en las tres ediciones previas. 🟡 por homicidio doloso único"),
 dict(id="ARG-134-013", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="no publicada; «este jueves», por titular",
  ent="Sinaloa", mun="Culiacán (Infonavit Barrancos)", dia="15-OCT, HORA NO FIJADA",
  title="SINALOA · CULIACÁN — ASESINAN A BALAZOS A UN HOMBRE FRENTE A UN JARDÍN DE NIÑOS EN INFONAVIT BARRANCOS",
  hecho="Culiacán · <code>INFONAVIT BARRANCOS, FRENTE A UN JARDÍN DE NIÑOS</code> · «este jueves» 15-OCT, por titular · <b>1 hombre muerto</b> a balazos, por titular (🟡) · la <b>Fiscalía de Sinaloa</b> lo identifica, por titular de un medio · <code>UN HERIDO, POR TITULARES SIN FECHA EN LA RUTA (NOROESTE, EXTRAOFICIAL): NO SE INTEGRA AL TOTAL</code> · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 hombre asesinado</b> a balazos",
  inst="Fiscalía de Sinaloa <span class=\"muted-note\">(identificación por cita)</span>", nac=NIN, conf="★★☆☆☆",
  campo="ninguna fuente con fecha en la ruta; día solo por el titular", I=1, N=0, R=3, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Infonavit Barrancos no figura en las tres ediciones previas. <code>POSIBLE DUPLICIDAD CON EL ATAQUE A UN CICLISTA EN LA COL. ANTONIO NAKAYAMA (EL SOL DE SINALOA): NO SE FICHA APARTE HASTA VALIDAR</code>. 🟡 por homicidio doloso único"),
 dict(id="ARG-134-019", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-15", hora="~19:45–20:00 (solo por resumen)",
  ent="Guanajuato", mun="San Francisco del Rincón (col. Cuauhtémoc)", dia="15-OCT, NOCHE",
  title="GUANAJUATO · SAN FRANCISCO DEL RINCÓN — ASESINAN A BALAZOS A UN MOTOCICLISTA EN LA COLONIA CUAUHTÉMOC",
  hecho="San Francisco del Rincón · <code>COL. CUAUHTÉMOC («LAS COLONIAS»)</code> · JUEVES 15-OCT, ~19:45–20:00 (" + RES + ") · ataque a balazos contra un motociclista, por titular · <b>1 hombre muerto</b>, por titular (🟡) · <b>ningún detenido publicado</b> · identidad y móvil: no publicados",
  panel="<b>Motociclista asesinado</b> a balazos",
  inst=SB, nac="La Silla Rota · Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=2, R=2, A=0,
  fechadas=["Periódico AM (2026/10/15)", "Periódico Correo (2026/oct/16)", "La Silla Rota (2026/10/16)"], estatus="Parcialmente corroborado", arm=None,
  desl="La col. Cuauhtémoc de San Francisco del Rincón no figura en las ediciones 130 a 133 ni en el índice. 🟡 por homicidio doloso único"),
 dict(id="ARG-134-014", estado="MX-CMX", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-16", hora="no publicada",
  ent="Ciudad de México", mun="Azcapotzalco", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="CIUDAD DE MÉXICO · AZCAPOTZALCO — LA SSC DETIENE A UN IMPLICADO EN EL ATAQUE CONTRA EL AUTOMÓVIL DE LA COLONIA PASTEROS",
  hecho="Azcapotzalco · publicado el VIERNES 16-OCT · la <b>SSC</b> detiene a un hombre señalado como implicado, por titular; puesto a disposición de la FGJCDMX, " + RES + " · <b>1 detenido</b> (🟢) · <code>2 ARMAS DE FUEGO SIN TIPO, 1 SILENCIADOR Y 2 MOTOCICLETAS ASEGURADOS: SOLO POR RESUMEN DE UNA FUENTE</code> · " + FR,
  panel="<b>1 detenido</b> por el ataque de la col. Pasteros",
  inst="SSC CDMX <span class=\"muted-note\">(por cita)</span>", nac="Infobae", conf="★★☆☆☆",
  campo="una sola fuente; aseguramiento solo por resumen", I=1, N=1, R=0, A=0,
  fechadas=["Infobae (2026/10/16)"], estatus="Pendiente de corroboración", arm=None, cual=True, fecha_txt="no publicada; publicada el 2026-10-16",
  desl="Mismo hecho que ARG-134-009: delito y detención, dos fichas. Armas de fuente única: sin fila, No confirmado"),
 dict(id="ARG-134-015", estado="MX-ROO", region="Sureste", color="verde", impacto="mediano", fecha="2026-10-15", hora="no publicada",
  ent="Quintana Roo", mun="Puerto Aventuras", dia="15-OCT, HORA NO FIJADA",
  title="QUINTANA ROO · PUERTO AVENTURAS — LA FISCALÍA DETIENE AL PRESIDENTE MUNICIPAL POR EXTORSIÓN AGRAVADA",
  hecho="Puerto Aventuras · JUEVES 15-OCT · la <b>FGE Quintana Roo</b> detiene al <b>presidente municipal</b> por <b>extorsión agravada</b>, por titular · <b>3 detenidos</b> —el alcalde, una funcionaria del ayuntamiento y un familiar—, " + RES + " (🟢) · puestos a disposición de un juez de control, " + RES + " · acusación, no condena · sin armamento publicado · identidades: no se reproducen · " + FR,
  panel="Detenido el <b>presidente municipal</b> por extorsión agravada; <b>3 detenidos</b>, solo por resumen",
  inst="FGE Quintana Roo <span class=\"muted-note\">(por cita)</span>", nac="El Financiero · N+ · Milenio", conf="★★★☆☆",
  campo="número de detenidos solo por resumen; boletín no leído", I=1, N=3, R=1, A=0,
  fechadas=["El Financiero (2026/10/15)"], estatus="Parcialmente corroborado", arm=None,
  desl="Puerto Aventuras no figura en las tres ediciones previas ni en el índice. Servidor público como imputado, no como víctima. Sin armamento: fuera del conteo"),
 dict(id="ARG-134-016", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-15", hora="desde ~03:00 (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (Laguna Colorada, Los Becos y Costa Rica)", dia="15-OCT, HORA NO FIJADA",
  title="SINALOA · CULIACÁN — CINCO CATEOS FEDERALES EN LAGUNA COLORADA: SIETE DETENIDOS Y ARMAS ASEGURADAS",
  hecho="Culiacán · <code>LAGUNA COLORADA, LOS BECOS Y COSTA RICA</code> · JUEVES 15-OCT · <code>INICIO ~03:00, SOLO POR RESUMEN: ANTERIOR A LA APERTURA SI SE CONFIRMA</code> · <b>cinco cateos</b> de Marina, SSPC, GN y FGR contra una célula, " + RES + " · <b>7 detenidos</b> tras cinco cateos, por titular (🟢) · <b>4 armas de fuego</b>, por resumen de dos medios · <code>DESGLOSE 3 LARGAS, 1 CORTA Y 8 CARGADORES DE UNA SOLA FUENTE SIN FECHA: NO SE INTEGRA</code> · droga y efectivo sin cifra citable · habitantes intentan impedir detenciones, por titular · " + FR,
  panel="Cinco cateos: <b>7 detenidos</b> y <b>4 armas</b> sin desglose integrable",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(comunicado por cita)</span>", nac="La Jornada · El Heraldo de México · Milenio · Infobae · SDP", conf="★★☆☆☆",
  campo="número de armas solo por resumen; hora de inicio solo por resumen", I=1, N=5, R=3, A=0,
  fechadas=["Por Esto (2026/10/15)", "La Jornada (2026/10/15)", "El Heraldo de México (2026/10/15)", "Infobae (2026/10/15)"], estatus="Parcialmente corroborado", arm="ARG-134-ARM-001",
  desl="Laguna Colorada no figura en las tres ediciones previas. NO es la captura de «El Wicho» en Villa Unión (fecha no fijada, sin integrar). Los «siete detenidos» de Línea Directa son este mismo hecho: no se suman dos veces"),
 dict(id="ARG-134-017", estado="MX-CHP", region="Sureste", color="verde", impacto="pequeno", fecha="2026-10-15", hora="no publicada",
  ent="Chiapas", mun="Chiapa de Corzo", dia="PUB. 15-OCT, HORA NO FIJADA",
  title="CHIAPAS · CHIAPA DE CORZO — DETIENEN A UN PRESUNTO RESPONSABLE DE LA BALACERA EN UN BAR CLANDESTINO DE RIBERA LAS FLECHAS",
  hecho="Chiapa de Corzo · publicado el JUEVES 15-OCT · detención de un hombre señalado por el ataque en un bar clandestino de la col. Ribera Las Flechas (ARG-134-REC-002), por titular · <b>1 detenido</b> (🟢) · corporación no publicada · camioneta asegurada, " + RES + " · sin armamento con cifra · identidad: no se reproduce · " + FR,
  panel="<b>1 detenido</b> por la balacera de un bar clandestino",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente con fecha; fecha de la detención no publicada", I=0, N=0, R=2, A=0,
  fechadas=["El Sol del Soconusco (2026/10/15)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicada el 2026-10-15",
  desl="Mismo hecho que ARG-134-REC-002: delito y detención, dos fichas. Sin armamento con cifra"),
 dict(id="ARG-134-018", estado="MX-GUA", region="Occidente", color="verde", impacto="pequeno", fecha="2026-10-16", hora="no publicada",
  ent="Guanajuato", mun="Irapuato (col. Las Rosas)", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="GUANAJUATO · IRAPUATO — DETIENEN A UN HOMBRE LIGADO POR UN MEDIO AL ASESINATO DE UN PASTOR Y SU ESPOSA",
  hecho="Irapuato · detención en la col. Las Rosas, " + RES + " · <b>1 detenido</b>: «hay un detenido», por titular (🟢) · <code>CONDICIÓN DE PROBABLE RESPONSABLE DEL DOBLE HOMICIDIO DE ARG-134-REC-001: SOLO POR RESUMEN</code> · fecha de la detención no publicada; publicada el VIERNES 16-OCT · corporación no publicada · identidad: no se reproduce · " + FR,
  panel="<b>1 detenido</b> por el doble homicidio de Villas de El Dorado",
  inst=SB, nac="La Silla Rota", conf="★★☆☆☆",
  campo="una sola fuente con la detención; fecha no publicada", I=0, N=1, R=0, A=0,
  fechadas=["La Silla Rota (2026/10/16)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicada el 2026-10-16",
  desl="Mismo hecho que ARG-134-REC-001: delito y detención, dos fichas. NO son los detenidos del bar Continental (ARG-133-010)"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-134-REC-001", estado="MX-GUA", region="Occidente", fecha="2026-10-15", hora="~01:00 o ~02:00 (solo por resumen; otra nota, «mañana»)", orig="ARGOS 133 (134 SI FUE DESPUÉS DE LAS 07:16) — HORA NO FIJADA", col_orig="rojo",
  ent="Guanajuato", mun="Irapuato (Villas de El Dorado)", dia="15-OCT, MADRUGADA",
  title="GUANAJUATO · IRAPUATO — ASESINAN A UN PASTOR CRISTIANO Y A SU ESPOSA EN LA ENTRADA DE SU CASA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 133 —134 SI FUE DESPUÉS DE LAS 07:16— HORA NO FIJADA</code> · <code>FRACC. VILLAS DE EL DORADO</code> · JUEVES 15-OCT · <code>HORA CONTRADICHA: ~01:00, ~02:00 O «MAÑANA», SOLO POR RESUMEN</code> · un hombre en motocicleta dispara contra un pastor y su esposa afuera de su casa, por titular · <b>2 muertos</b>: él en el lugar y ella en el hospital, " + RES + " (🔴 en su ventana) · <b>1 detenido</b> (ficha ARG-134-018) · móvil no confirmado · identidades: no se reproducen",
  panel="<b>Pastor y su esposa asesinados</b>", inst=SB, nac="El Universal · Informador · La Silla Rota",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=3, R=1, A=0,
  fechadas=["Informador (20261015)", "Kuali (2026/10/15)", "La Silla Rota (2026/10/16)"],
  desl="Villas de El Dorado no figura en las tres ediciones previas. NO es ARG-133-010 (bar Continental). 🔴 en su ventana por homicidio múltiple"),
 dict(id="ARG-134-REC-002", estado="MX-CHP", region="Sureste", fecha="2026-10-14", hora="no publicada", orig="ARGOS 133 (132 SI FUE EL 13 O ANTES DE LAS 08:19 DEL 14) — FECHA NO FIJADA", col_orig="rojo", fecha_txt="no fijado; publicado el 2026-10-14",
  ent="Chiapas", mun="Chiapa de Corzo (col. Ribera Las Flechas)", dia="PUB. 14-OCT, HORA NO FIJADA",
  title="CHIAPAS · CHIAPA DE CORZO — BALACERA EN UN BAR CLANDESTINO DE RIBERA LAS FLECHAS: DOS O TRES MUERTOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 133 —132 SI FUE EL 13 O ANTES DE LAS 08:19 DEL 14— FECHA NO FIJADA</code> · <code>COL. RIBERA LAS FLECHAS, KM 6 DE LA CARRETERA TUXTLA–LA ANGOSTURA</code> · publicado el MIÉRCOLES 14-OCT · balacera en un bar clandestino tras una riña, " + RES + " · <code>MUERTOS CONTRADICHOS: 1 Y 2 HERIDOS (EL SOL DEL SOCONUSCO 14-OCT, QUADRATÍN, DIARIO DE CHIAPAS), 2 Y 1 HERIDO (EL SOL DEL SOCONUSCO 15-OCT) O 3 (N+, MEGANOTICIAS), POR TITULAR</code> (🔴 en su ventana con dos o más; 🟡 con uno) · detención en ficha ARG-134-017",
  panel="Balacera en un bar: <b>1 a 3 muertos</b> (contradicho)", inst=SB, nac="El Heraldo de México · N+",
  conf="★★☆☆☆", campo="número de muertos contradicho; fecha no fijada", I=0, N=2, R=4, A=0,
  fechadas=["El Heraldo de México (2026/10/14)", "El Sol del Soconusco (2026/10/14)", "El Sol del Soconusco (2026/10/15)"],
  desl="Chiapa de Corzo no figura en las tres ediciones previas. 🔴 en su ventana por homicidio múltiple, si se sostienen dos o más muertos"),
 dict(id="ARG-134-REC-003", estado="MX-MIC", region="Occidente", fecha="2026-10-14", hora="no publicada", orig="ARGOS 132 O ARGOS 133 — FECHA NO FIJADA", col_orig="rojo", fecha_txt="13 o 14-oct, no fijado; muerte de la menor ~06:00 del 15-oct, solo por resumen",
  ent="Michoacán", mun="Apatzingán (El Guayabo)", dia="13 O 14-OCT, NO FIJADO",
  title="MICHOACÁN · APATZINGÁN — ATAQUE ARMADO EN EL GUAYABO: MUEREN UN HOMBRE Y SU HIJA DE OCHO AÑOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 132 O ARGOS 133 — FECHA DEL ATAQUE NO FIJADA (13 O 14-OCT)</code> · <code>EL GUAYABO, APATZINGÁN</code> · ataque armado contra una vivienda, " + RES + " · <b>1 hombre muerto</b> en el lugar y <b>su hija de 8 años</b> herida; trasladada en helicóptero militar, murió en un hospital de Morelia hacia las 06:00 del 15-oct, " + RES + " · <b>2 muertos</b>, por titular (🔴 en su ventana) · <code>DENUNCIA DE LA FAMILIA SOBRE EL AUXILIO MILITAR: CONTRADICHA, NO SE INTEGRA</code> · <b>ningún detenido publicado</b>",
  panel="Ataque a una vivienda: <b>un hombre y su hija</b> muertos", inst=SB, nac="MVS",
  conf="★★★☆☆", campo="fecha del ataque solo por resumen; sin fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["MVS Noticias (2026/10/15)"],
  desl="El Guayabo no figura en las fichas de las tres ediciones previas. 🔴 en su ventana por homicidio múltiple"),
 dict(id="ARG-134-REC-004", estado="MX-MEX", region="Centro", fecha="2026-10-11", hora="noche (solo por resumen)", orig="ARGOS 130 (131 SI FUE DESPUÉS DE LAS 08:19 DEL 12)", col_orig="rojo",
  ent="Estado de México", mun="Almoloya de Juárez (San Agustín Altamirano)", dia="11-OCT, NOCHE",
  title="ESTADO DE MÉXICO · ALMOLOYA DE JUÁREZ — MATAN A UN AGENTE DE LA FGR Y HIEREN A OTRO EN UN ATAQUE ARMADO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 130 —131 SI FUE DESPUÉS DE LAS 08:19 DEL 12-OCT—</code> · <code>SAN AGUSTÍN ALTAMIRANO</code> · noche del DOMINGO 11-OCT (" + RES + "; una nota dice martes) · ataque armado contra agentes de la FGR durante un operativo, por titular · <b>1 agente de la FGR muerto y 1 herido</b>, por titular (🔴 en su ventana) · <b>3 detenidos</b>, por titular · identidades: no se reproducen",
  panel="<b>Agente de la FGR muerto</b> y otro herido", inst=SB, nac="Milenio",
  conf="★★★☆☆", campo="iniciador no determinado; fecha y hora solo por resumen", I=0, N=1, R=5, A=0,
  fechadas=["Por Esto (2026/10/12)", "Seuno Noticias (2026/10/13)"],
  desl="Almoloya de Juárez no figura en las fichas de ARGOS 129 a 133. 🔴 en su ventana por muerte de personal de seguridad"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-134-ARM-001", ficha="ARG-134-016", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Culiacán (Laguna Colorada)", c=[0,0,4,0,0,0,0,0,0,7],
  corp="Marina · SSPC · GN · FGR", conf="Bajo", color="verde", fecha="2026-10-15", hora="no fijada",
  fecha_txt="15-oct<br><span class=\"muted-note\">FRONTERA DE VENTANA</span>",
  nota="«4 armas de fuego» por resumen de dos medios: sin categoría · 7 detenidos por titular (Por Esto 2026/10/15) · desglose 3 largas, 1 corta y 8 cargadores de una sola fuente sin fecha: NO SE INTEGRA · inicio ~03:00 solo por resumen: si se confirma, sale del total por fe de erratas",
  fuentes=["Por Esto (2026/10/15)", "Infobae (2026/10/15)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
assert TOT == [0, 0, 4, 0, 0, 0, 0, 0, 0, 7], TOT
assert cnt == {"rojo": 5, "amarillo": 9, "verde": 5}, cnt
assert cnt_rec == {"rojo": 4, "amarillo": 0, "verde": 0}, cnt_rec
assert len(ENT) == 13, ENT
assert NFR == 12, NFR

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
head = head.replace("<title>ARGOS 133 — Reporte Nacional de Seguridad — 2026-10-15</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE COLIMA EL NÚMERO OFICIAL DE VÍCTIMAS</b> (ARG-134-003).
      <br><b>2. SOLICITE A LA FISCALÍA DEL ESTADO DE MÉXICO LA IDENTIFICACIÓN Y LA CAUSA DE MUERTE</b> (ARG-134-004).
      <br><b>3. SOLICITE A LA FISCALÍA DEL ESTADO DE MÉXICO EL PARTE MÉDICO DE LA VÍCTIMA MENOR</b> (ARG-134-010).
      <br><b>4. SOLICITE A LA FISCALÍA DE QUINTANA ROO LA SITUACIÓN JURÍDICA DE LOS DETENIDOS</b> (ARG-134-015).
      <br><b>5. SOLICITE A LA FISCALÍA DE MICHOACÁN LA FECHA DEL ATAQUE</b> (ARG-134-REC-003).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>15-oct 07:16 → 16-oct 11:34 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,67 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>. <b>Doce de diecinueve</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <b>Armamento</b>: <b>1 evento integrado</b> (ARG-134-ARM-001, confianza Bajo: 4 armas sin categoría). <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento de armamento</b>; los de ARG-134-014, -015, -017 y -018 no entran. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios</b>: <b>15 a 16</b> por agresión —Silao 3, Monterrey 2, Coquimatlán 2 a 3 (contradicho), Puebla 1, Patamban 1, Santa Catarina 1, Oaxtepec 1, Coatzacoalcos 1, Hermosillo 1, Culiacán 1 y San Francisco del Rincón 1— y <b>2 cuerpos</b> en Tlalnepantla. <b>Heridos: 5 a 6</b> —Santa Catarina 1, Azcapotzalco 2, Coacalco 2 y Coquimatlán 0 a 1 (contradicho)—; el herido de Culiacán, sin fecha en la ruta, no se integra. <b>Cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:5])
co2 = "\n".join(ficha(e) for e in E[5:14])
co3 = "\n".join(ficha(e) for e in E[14:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA ARMA CORTA CON DESGLOSE INTEGRABLE</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA CON DESGLOSE INTEGRABLE</code>"),
 tile(2, "Sin categoría", TOT[2], "Culiacán, Laguna Colorada · <b>confianza Bajo</b>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "<code>NINGÚN CARTUCHO CON CIFRA EN HECHO PROPIO</code>"),
 tile(4, "Cargadores", TOT[5], "<code>NINGÚN CARGADOR CON CIFRA INTEGRABLE</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA EN HECHO PROPIO</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>Una fila de armamento en la ventana</b>, Sinaloa, con <b>confianza Bajo</b>: 4 armas sin categoría. <b>Total nacional del corte</b>: en la página de panorama.
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Verde = aseguramiento sin enfrentamiento. Gris = sin aseguramiento con cifra integrable. La sola presencia de armas no vuelve roja a una entidad.</div>
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
    <b>Lectura regional</b> —1 fila, <b>cálculo propio</b>—: <b>Noroeste 1</b> · <b>Noreste 0</b> · <b>Occidente 0</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>. <b>Sin fila, No confirmado</b>: ARG-134-014 (Azcapotzalco, armas de fuente única).
    <br><code>VISTOS, NO INTEGRADOS</code>: Tijuana, plaza El Lago (una sola fuente sin fecha) · Comalcalco, Tabasco (no ligado a URL con fecha) · Villahermosa y Pozos, Guanajuato (vinculaciones a proceso de aseguramientos anteriores) · Panixtlahuaca, Oaxaca (cateos del 14-oct, sin cifra completa).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: boletín federal de las <b>acciones del 14-oct</b>, publicado el 15-oct: Gustavo Díaz Ordaz (Tamaulipas), Poza Rica (Veracruz), Concordia y Escuinapa (Sinaloa), Orizaba (ARG-132-002). <code>CANTIDADES SOLO POR RESUMEN, SIN FRAGMENTO: NO SE PUBLICAN</code>.
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
      <tr><td><b>Veracruz</b><br>Veracruz</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">homicidio calificado de un periodista (enero de 2022); juicio oral</span></td><td><b>21 años</b>, por titular</td><td>FGE Veracruz <span class="muted-note">(por titulares de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · La Silla Rota 2026/10/15 · boletín no localizado · <code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code></td><td>Bajo</td></tr>
      <tr><td><b>Veracruz</b><br>Cosoleacaque</td><td>Dos sentenciados, nombres no reproducidos · <span class="muted-note">portación de arma de uso exclusivo; abreviado, audiencia del 8-oct</span></td><td><b>4 años</b> y multa, por titular</td><td>FGR <span class="muted-note">(por <i>slug</i> de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · La Nigua 2026/10/15 · Hora Cero 2026/10/16 · sentencia del 8-oct</td><td>Bajo</td></tr>
      <tr><td><b>Veracruz</b><br>Banderilla</td><td>Un sentenciado · <span class="muted-note">portación de pistola sin licencia; sentencia del 9-oct</span></td><td><b>2 años 6 meses</b>, por <i>slug</i></td><td>FGR <span class="muted-note">(por <i>slug</i> de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Hora Cero 2026/10/15 · la fecha 14-oct de otro medio, solo por resumen</td><td>Bajo</td></tr>
      <tr><td><b>Ciudad de México</b><br>Cuauhtémoc</td><td>Dos sentenciados, nombres no reproducidos · <span class="muted-note">homicidios en la col. Morelos (marzo de 2025)</span></td><td>Penas solo por resumen</td><td>FGJCDMX <span class="muted-note">(cuenta oficial en X, título por resumen)</span></td><td>Primera publicación el <b>14-oct</b> (crprensa 2026/10/14): anterior a la apertura · boletín no leído</td><td>Bajo</td></tr>
      <tr><td><b>Colima</b></td><td>Sin nombre publicado · <span class="muted-note">incumplimiento de obligaciones de asistencia familiar</span></td><td><b>3 años</b>, por titular</td><td>FGE Colima <span class="muted-note">(por titular de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin URL con fecha · delito no prioritario</td><td>Bajo</td></tr>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Culpables, número sin fragmento · <span class="muted-note">homicidio de tres surfistas</span></td><td><code>SIN PENA LOCALIZADA</code></td><td>FGE BC</td><td>Veredicto del 10-oct; individualización programada el 16-oct, solo por resumen; <b>no es sentencia</b></td><td>—</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Culpables, número sin fragmento · <span class="muted-note">triple feminicidio</span></td><td><code>SIN PENA: INDIVIDUALIZACIÓN APLAZADA AL 21-OCT</code></td><td>PGJ Hidalgo <span class="muted-note">(por cita)</span></td><td>Fallo del 8-9 oct; <b>no es sentencia</b> hasta la individualización</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Nayarit, 53 años por desaparición (14-oct) · FGR Chihuahua, 8 años (14-oct) · FGR Sinaloa, «más de 8 años» (14-oct) · Oaxaca FGEO, 80 años (El Heraldo de México 2026/10/14) · Zacatecas, 10 años (13-oct) · Nuevo León, 155 años (13-oct). <b>Sin fecha anclada</b>: Jalisco, FGR Puerto Vallarta, 4 años (<code>POSIBLE CASO HOMÓNIMO</code>) · Sonora, Nogales, 15 años.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>15 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · BC, Chih · Coah, Tamps · Ags, Mich · CDMX, Hgo · Ver, Tab · Gro, Oax, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0 por boletín leído</b> · candidatas solo por medios: Veracruz (FGE y FGR), Colima, Ciudad de México</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales · <b>sin boletín indexado, no «sin sentencias»</b></td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>17</b>: BCS, Son, Sin, Dgo · NL, SLP, Zac · Jal, Col, Nay, Gto · Edomex, Mor, Pue, Tlax, Qro · Camp</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 31 de 32</b> por búsqueda en medios, en parte por consulta regional amplia y no por entidad; <code>NO REVISADA</code>: Ags · <b>armamento: 17 de 32</b>; <code>NO REVISADA</code>: BCS, Chih, Sin, Dgo · Coah · Col, Nay, Ags · Edomex, Mor, Pue, Qro · Ver, Tab · Yuc (Sinaloa: hecho por medios, sin dominio oficial) · <code>REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 14-oct</b>: existe, publicado el 15-oct (Milenio y republicadores) · <b>acciones del 15-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta · <b>Guardia Nacional y FGR</b>: SRIV · <b>Defensa y Marina</b>: <code>NO REVISADA</code>, dominio no devuelto</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 16-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR CINCO ROJOS</b>: ARG-134-001 a ARG-134-005.
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-134-006 a ARG-134-013 y ARG-134-019.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-134-014 a ARG-134-018.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-134-REC-001 a ARG-134-REC-004.
      <br><b>5.</b> <code>28 H 18 MIN; DOCE DE DIECINUEVE HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. SILAO, FOCO DEL BAJÍO.</b> ARG-134-001 se suma a ARG-133-REC-002 y ARG-133-REC-003 en dos días. Línea: <b>solicitar a la FGE Guanajuato el cotejo de casquillos</b> de los tres — hipótesis.
      <br><b>2. PERSONAL DE SEGURIDAD Y PROCURACIÓN COMO BLANCO.</b> ARG-134-005 y ARG-131-003 en Puebla en cuatro días; ARG-134-REC-004 contra agentes de la FGR. Línea: <b>solicitar a la FGE Puebla si las dos carpetas comparten indicios</b> — vínculo no acreditado.
      <br><b>3. DOBLE ATAQUE EN EL ÁREA METROPOLITANA DE MONTERREY.</b> ARG-134-002 y ARG-134-007, el mismo día. Línea: <b>solicitar a la FGJ Nuevo León el cotejo balístico</b> — hipótesis.
      <br><b>4. CATEOS FEDERALES CONTRA UNA CÉLULA EN CULIACÁN.</b> ARG-134-016. Línea: <b>solicitar a la SSPC la situación jurídica de los detenidos</b> — requiere validación.
      <br><b>5. VÍCTIMAS CON CARGO COMUNITARIO O PÚBLICO.</b> ARG-134-006 y ARG-134-011, con ARG-132-003. Línea: <b>solicitar a las fiscalías de Michoacán y Veracruz si el cargo es línea de investigación</b> — hipótesis.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>NO REVISADA</code>: dominio no devuelto por el buscador. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: SILAO, MONTERREY, COQUIMATLÁN, TLALNEPANTLA Y PUEBLA", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA", co2)
 + page("CRIMEN ORGANIZADO (III) — ACCIONES INSTITUCIONALES", co3)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES: VENTANAS DE ARGOS 130 A 133", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 15-oct 07:16 → 16-oct 11:34 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
