# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 140 (orden rehecha el 25-oct; la del 22-oct no se ejecutó).
Uso: python3 tools/datos-argos-140.py <plantilla ARGOS 139> <salida>
Ventana: 21-oct 10:23 → 25-oct 07:45 CDMX (ventana larga). Archivo: argos-2026-10-25.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "140", "2026-10-25", "07:45"
CONSULTA = "2026-10-25 07:46-07:57"
DUR = "93 h 22 min"
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
BF = "Boletín federal del 22-oct <span class=\"muted-note\">(por republicadores)</span>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-140-001", estado="MX-CMX", region="Centro", color="rojo", impacto="mediano", fecha="2026-10-23", hora="tarde (solo por resumen)", mu=2, he=1, cu=0,
  ent="Ciudad de México", mun="Iztapalapa (Calzada Ermita Iztapalapa, col. Ampliación Ricardo Flores Magón)", dia="23-OCT, TARDE",
  title="CIUDAD DE MÉXICO · IZTAPALAPA — ATAQUE ARMADO EN CALZADA ERMITA: DOS MUERTOS Y UN HERIDO",
  hecho="Iztapalapa · <code>CALZADA ERMITA IZTAPALAPA, COL. AMPLIACIÓN RICARDO FLORES MAGÓN, SOLO POR RESUMEN</code> · viernes 23-OCT, por ruta (Latinus, La Razón, Proceso, Tribuna, Quinto Poder y Cúspide 2026/10/23) · tarde, " + RES + " · <b>2 muertos</b> y <b>1 herido</b>, por titulares (🔴 homicidio múltiple) · ~15 detonaciones, " + RES + " · agresores huyeron en motocicleta, por titular de Infobae 2026/10/24 · la SSC informó, " + RES + " · detención de dos presuntos responsables: ficha propia, ARG-140-017 · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos</b> y 1 herido", inst="SSC CDMX" + PR, nac="Latinus · La Razón · Proceso · Infobae", conf="★★★☆☆",
  campo="hora y detonaciones solo por resumen; fuente institucional solo por resumen", I=1, N=6, R=3, A=0,
  fechadas=["Latinus (2026/10/23)", "La Razón (2026/10/23)", "Proceso (2026/10/23)", "Tribuna (2026/10/23)", "Quinto Poder (2026/10/23)", "Cúspide (2026/10/23)", "Infobae (2026/10/24)"], estatus="Parcialmente corroborado", arm=None,
  desl="Calzada Ermita y Ricardo Flores Magón (Iztapalapa) no figuran en las cinco ediciones previas. Iztapalapa en el índice: ARG-133-004 y -008 (tianguis El Salado, 14-oct): otro hecho. Un doble homicidio «cuatro días» antes en la misma calzada, por resumen de Infobae: no fijado, no se integra."),
 dict(id="ARG-140-002", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-24", hora="~09:45-10:00 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Guanajuato", mun="Purísima del Rincón (Libramiento Sur / bulevar Las Torres)", dia="24-OCT, MAÑANA POR RESUMEN",
  title="GUANAJUATO · PURÍSIMA DEL RINCÓN — ASESINAN A UNA POLICÍA MUNICIPAL AL SALIR DE SU TURNO",
  hecho="Purísima del Rincón · <code>LIBRAMIENTO SUR Y BULEVAR LAS TORRES, SOLO POR RESUMEN</code> · sábado 24-OCT, por ruta (Latinus, AM, Tribuna y Miguel Ángel Luna 2026/10/24) · ~09:45-10:00, " + RES + " · <b>1 muerta</b>: <b>policía municipal</b>, por titulares (🔴 víctima autoridad) · al salir de su turno, a bordo de su motocicleta, por titulares · 31 años; dos agresores en motocicleta, " + RES + " · la FGE abrió carpeta, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>Policía municipal asesinada</b>: 1 muerta", inst=SB, nac="Latinus · Milenio · El Universal", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=4, R=3, A=0,
  fechadas=["Latinus (2026/10/24)", "AM (2026/10/24)", "Tribuna (2026/10/24)", "Miguel Ángel Luna (2026/10/24)"], estatus="Parcialmente corroborado", arm=None,
  desl="Purísima del Rincón no figura en las cinco ediciones previas ni en el índice. Policía vial asesinada en Celaya el 17-oct, por resumen: ventana anterior, otro hecho."),
 dict(id="ARG-140-003", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-24", hora="~07:30 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Sinaloa", mun="Mazatlán (fracc. San Fernando, calle San Marcos)", dia="24-OCT, ~07:30 POR RESUMEN",
  title="SINALOA · MAZATLÁN — ASESINAN A UN TRABAJADOR DEL C4i A BORDO DE SU CAMIONETA",
  hecho="Mazatlán · <code>FRACC. SAN FERNANDO, CALLE SAN MARCOS, SOLO POR RESUMEN</code> · sábado 24-OCT, por ruta (Luz Noticias 2026-10-24) · ~07:30, " + RES + " · <b>1 muerto</b>: conductor de una camioneta Ram blanca, por titular · <b>trabajador del C4i</b>, por titulares (Meganoticias, Expreso, Los Noticieristas); área administrativa de la SSP estatal, " + RES + ": <code>ADSCRIPCIÓN CONTRADICHA</code>, servidor público en ambas (🔴 víctima servidor público) · ~20 casquillos, por titular (Reporte 18) · la Fiscalía confirmó el homicidio, por titular (Sinaloahoy) · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>Trabajador del C4i asesinado</b>: 1 muerto", inst="FGE Sinaloa" + PT, nac=NIN, conf="★★★☆☆",
  campo="adscripción contradicha; hora solo por resumen; confirmación institucional solo por titular regional", I=1, N=0, R=7, A=0,
  fechadas=["Luz Noticias (2026-10-24)", "Los Noticieristas (2026/10)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Fernando (Mazatlán) no figura en las cinco ediciones previas ni en el índice. Quadratín Sinaloa y Quadratín México publican el mismo texto: una fuente. La Fiscalía figura por el titular de Sinaloahoy, que no se cuenta además como regional."),
 dict(id="ARG-140-004", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-23", hora="noche (solo por resumen)", mu=2, he=0, cu=0,
  ent="Sinaloa", mun="Culiacán (fracc. Villa Bonita, negocio de sushi)", dia="23-OCT, NOCHE, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-23, noche — DÍA SOLO POR RESUMEN",
  title="SINALOA · CULIACÁN — ATAQUE ARMADO EN UN NEGOCIO DE SUSHI DE VILLA BONITA: DOS MUERTOS",
  hecho="Culiacán · <code>FRACC. VILLA BONITA, ESTACIONAMIENTO DE UN NEGOCIO DE SUSHI, SOLO POR RESUMEN</code> · noche del viernes 23-OCT, " + RES + "; <code>NINGUNA RUTA CON FECHA</code> (excepción declarada para rojos) · <b>2 muertos</b>, hombres, por titulares (🔴 homicidio múltiple) · «Fiscalía investiga», por titular (Sinaloahoy) · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="día solo por resumen; ninguna ruta con fecha; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Villa Bonita figura en ARG-97-001 (14-ago): otro hecho. «Fiscalía investiga» no cuenta como fuente institucional."),
 dict(id="ARG-140-005", estado="MX-GUA", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-21", hora="uno ~11:00; los demás no fijada (solo por resumen)", mu=0, he=0, cu=5,
  ent="Guanajuato", mun="León (Cañada del Real, col. Brisas del Sol, La Providencia y un cuarto punto)", dia="21-OCT, HORA NO FIJADA",
  title="GUANAJUATO · LEÓN — HALLAN CINCO CUERPOS EN CUATRO PUNTOS DE LA CIUDAD",
  hecho="León · <code>CAÑADA DEL REAL, COL. BRISAS DEL SOL, LA PROVIDENCIA Y UN CUARTO PUNTO, SOLO POR RESUMEN</code> · miércoles 21-OCT, por titulares con ruta fechada (La Silla Rota, Intolerancia y La Prensa de Coahuila 2026/10/21, «este miércoles») · " + AP + " · <b>5 cuerpos</b>, por titulares (🔴 hallazgo de cuerpos) · una mujer, por titulares; cuerpo de mujer calcinado, cuerpo desmembrado en bolsas y hombre de ~30 años (~11:00), " + RES + " · <code>CIFRA NO CONFIRMADA POR AUTORIDAD</code> · <code>CAUSA DE MUERTE NO INFORMADA</code> · <code>RELACIÓN ENTRE LOS HALLAZGOS NO ACREDITADA</code> · <b>ningún detenido publicado</b>",
  panel="Hallazgo de <b>5 cuerpos</b> en cuatro puntos", inst=SB, nac="La Silla Rota", conf="★★★☆☆",
  campo="cifra sin confirmación oficial; hora no fijada; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["La Silla Rota (2026/10/21)", "Intolerancia (2026/10/21)", "La Prensa de Coahuila (2026/10/21)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cañada del Real y Brisas del Sol no figuran en las cinco ediciones previas ni en el índice. No es la fosa del pozo de Arroyo Hondo (21-sep): otro hecho. Cuerpos fuera del recuento de muertos por agresión: van al de cuerpos hallados."),
 dict(id="ARG-140-006", estado="MX-TAB", region="Golfo", color="rojo", impacto="mediano", fecha="2026-10-21", hora="no fijada", mu=0, he=0, cu=2,
  ent="Tabasco", mun="Huimanguillo (Chicoacán, junto a la carretera Huimanguillo–Villa Estación Chontalpa)", dia="21-OCT, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-21 — DÍA SOLO POR RESUMEN",
  title="TABASCO · HUIMANGUILLO — FOSA CLANDESTINA CON DOS CUERPOS EN CHICOACÁN",
  hecho="Huimanguillo · <code>CHICOACÁN, PREDIO JUNTO A LA CARRETERA A VILLA ESTACIÓN CHONTALPA, SOLO POR RESUMEN</code> · hallazgo el miércoles 21-OCT, " + RES + " · publicado el 22-OCT, por ruta (Diario de Yucatán 2026/10/22) · " + AP + " · <b>fosa clandestina con 2 cuerpos</b>, por titulares (🔴 fosa) · dos jóvenes de 18 y 19 años desaparecidos desde el 13-oct, identificados por familiares, " + RES + "; pruebas genéticas pendientes · la FGE Tabasco abrió carpeta y el fiscal apunta a un móvil pasional, " + RES + " · «investiga FGR», por titular (Cuarto Poder) · cabeza humana abandonada frente a una escuela de Huimanguillo, por titular (La Silla Rota 2026/10/22): <code>RELACIÓN NO ACREDITADA, DÍA NO FIJADO</code> · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Fosa clandestina</b>: 2 cuerpos", inst=SB, nac="El Universal · TV Azteca", conf="★★★☆☆",
  campo="día del hallazgo solo por resumen; identificación no oficial; ninguna fuente institucional citada", I=0, N=2, R=6, A=0,
  fechadas=["Diario de Yucatán (2026/10/22)", "Entérate México (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chicoacán no figura en las cinco ediciones previas ni en el índice. NO es ARG-138-002 (Cárdenas, Sección 10 Azucarero, 19-oct). Huimanguillo figura en ARG-120-015 (septiembre): otro hecho. Entérate México agrega las dos fosas (cuatro jóvenes): el recuento no se integra. Cuerpos fuera del recuento de muertos por agresión."),
 dict(id="ARG-140-007", estado="MX-TAM", region="Noreste", color="rojo", impacto="pequeno", fecha="2026-10-23", hora="no fijada", mu=0, he=0, cu=0,
  ent="Tamaulipas", mun="Reynosa (predio tras Puerta Sur)", dia="22-23-OCT, HORA NO FIJADA",
  title="TAMAULIPAS · REYNOSA — UN COLECTIVO HALLA RESTOS ÓSEOS EN UN NUEVO PUNTO DE PUERTA SUR",
  hecho="Reynosa · <code>PREDIO TRAS PUERTA SUR, SOLO POR RESUMEN</code> · publicado el viernes 23-OCT, por ruta (El Mañana 2026/10/23); hallazgo el 22 o el 23, " + RES + " · <b>restos óseos humanos</b> y una credencial, por titular (🔴 restos) · cráneo, mandíbula y fémur, " + RES + " · hallazgo del colectivo Amor por los Desaparecidos, " + RES + " · «nuevo punto», por titular (Hoy Tamaulipas) · <code>NÚMERO DE VÍCTIMAS NO DETERMINADO</code> · <code>CREDENCIAL NO VINCULADA A LOS RESTOS</code> · sin intervención institucional publicada · «once hallazgos en 2026», " + RES + ": <code>RECUENTO NO SE INTEGRA</code>",
  panel="<b>Restos óseos</b> en un nuevo punto", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="número de víctimas no determinado; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["El Mañana (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Puerta Sur no figura en las cinco ediciones previas ni en el índice. Fosa de Reynosa del 12-oct, descartada en ARGOS 139: otro hecho. Restos sin número de víctimas: fuera de todo recuento."),
 # ======================= AMARILLOS
 dict(id="ARG-140-008", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-10-22", hora="no fijada", mu=0, he=1, cu=0,
  ent="Sinaloa", mun="Escuinapa (col. Francisco I. Madero)", dia="22-OCT, HORA NO FIJADA",
  title="SINALOA · ESCUINAPA — ATACAN A BALAZOS UN CAMIÓN CON ESTUDIANTES; HIEREN AL CHOFER",
  hecho="Escuinapa · <code>COL. FRANCISCO I. MADERO, SOLO POR RESUMEN</code> · jueves 22-OCT, por ruta (El Diario 2026/oct/22, ABC Noticias y Revista Espejo 2026/10/22) · camión con estudiantes atacado a balazos, por titulares · <b>chofer herido</b>, por titulares; lesión leve según la SSP de Sinaloa, " + RES + " · <b>ningún estudiante herido</b>, " + RES + " · estudiantes a bordo: 12 o ~30, por titulares: <code>CONTRADICHO</code> · agresión dirigida al conductor, según la SSP, " + RES + " · el chofer condujo hasta un retén militar, " + RES + " · <b>ningún detenido publicado</b> · (🟡 agresión sin muertos; sube a 🔴 si se acredita ataque contra la población civil a bordo)",
  panel="Camión con estudiantes baleado: <b>1 herido</b>", inst="SSP Sinaloa" + PR, nac="Reforma · La Razón", conf="★★★☆☆",
  campo="número de estudiantes contradicho; fuente institucional solo por resumen", I=1, N=2, R=4, A=0,
  fechadas=["El Diario (2026/oct/22)", "ABC Noticias (2026/10/22)", "Revista Espejo (2026/10/22)", "La Razón (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ninguno de los hechos de Escuinapa del índice (ARG-131-004, ARG-133-005, ARG-133-011, ARG-137-010 y otros) es este. Reforma, El Diario y La Prensa de Coahuila publican el mismo título: una fuente."),
 dict(id="ARG-140-009", estado="MX-MOR", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-22", hora="tarde (solo por resumen)", mu=1, he=1, cu=0,
  ent="Morelos", mun="Jiutepec (col. Lomas del Texcal)", dia="22-OCT, TARDE",
  title="MORELOS · JIUTEPEC — ASESINAN A UNA MUJER; SU HIJA QUEDA HERIDA",
  hecho="Jiutepec · <code>COL. LOMAS DEL TEXCAL, SOLO POR RESUMEN</code> · jueves 22-OCT, por titular («HOY jueves 22 de octubre de 2026», Azteca Morelos) · tarde, " + RES + " · <b>1 muerta</b> y <b>1 herida</b> —su hija—, por titulares (🟡 homicidio doloso único) · «dos mujeres asesinadas y una menor herida en Morelos», por titular (La Silla Rota 2026/10/23): agrega tres ataques, <code>RECUENTO NO SE INTEGRA</code> · <b>ningún detenido publicado</b>",
  panel="Mujer asesinada e hija herida: <b>1 muerta</b>", inst=SB, nac="TV Azteca · La Silla Rota", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=1, A=0,
  fechadas=["Azteca Morelos (titular, 22-oct)", "La Silla Rota (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Lomas del Texcal y Jiutepec no figuran en las cinco ediciones previas."),
 dict(id="ARG-140-010", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-24", hora="mañana (por titular)", mu=1, he=0, cu=0,
  ent="Estado de México", mun="Ozumba (carretera México–Cuautla, frente a una gasolinera)", dia="24-OCT, MAÑANA",
  title="ESTADO DE MÉXICO · OZUMBA — ASESINAN A UN OPERADOR DE TRANSPORTE PÚBLICO EN LA MÉXICO–CUAUTLA",
  hecho="Ozumba · <code>CARRETERA MÉXICO–CUAUTLA, FRENTE A UNA GASOLINERA, SOLO POR RESUMEN</code> · mañana del sábado 24-OCT, por titular con ruta fechada (Seuno Noticias 2026/10/24, «este sábado 24») · <b>1 muerto</b>: operador de combi de la Ruta 85, por titulares (🟡 homicidio doloso único) · agresor en motocicleta, " + RES + " · la FGJEM, a cargo, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Operador de transporte asesinado: <b>1 muerto</b>", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Seuno Noticias (2026/10/24)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ozumba no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-140-011", estado="MX-NLE", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-24", hora="no fijada", mu=1, he=0, cu=0,
  ent="Nuevo León", mun="Linares (col. La Petaca, depósito de cerveza)", dia="24-OCT, HORA NO FIJADA",
  title="NUEVO LEÓN · LINARES — ASESINAN A UN HOMBRE DENTRO DE UN DEPÓSITO",
  hecho="Linares · <code>COL. LA PETACA, DEPÓSITO DE CERVEZA, SOLO POR RESUMEN</code> · sábado 24-OCT, por ruta (Punto x Punto 2026/10/24) · <b>1 muerto</b>, hombre, por titular (🟡 homicidio doloso único) · 55 años, " + RES + " · Seguridad Pública y Fuerza Civil acudieron, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Hombre asesinado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente regional; hora no fijada", I=0, N=0, R=1, A=0,
  fechadas=["Punto x Punto (2026/10/24)"], estatus="Pendiente de corroboración", arm=None,
  desl="La Petaca no figura en las cinco ediciones previas. Linares figura en ARG-135-REC-001 (Provileón): otro hecho."),
 dict(id="ARG-140-012", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-24", hora="no fijada", mu=1, he=0, cu=0,
  ent="Guanajuato", mun="Irapuato (col. La Lupita)", dia="24-OCT, HORA NO FIJADA",
  title="GUANAJUATO · IRAPUATO — UN MOTOCICLISTA ARMADO MATA A UNA MUJER EN LA LUPITA",
  hecho="Irapuato · <code>COL. LA LUPITA, POR TITULAR</code> · sábado 24-OCT, por ruta (Periódico Correo 2026/oct/24) · <b>1 muerta</b>, mujer, por titular (🟡 homicidio doloso único) · agresor en motocicleta, por titular · <b>ningún detenido publicado</b>",
  panel="Mujer asesinada: <b>1 muerta</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente regional; hora no fijada", I=0, N=0, R=1, A=0,
  fechadas=["Periódico Correo (2026/oct/24)"], estatus="Pendiente de corroboración", arm=None,
  desl="La Lupita no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-140-013", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-24", hora="~13:35 (solo por resumen)", mu=1, he=0, cu=0,
  ent="Guanajuato", mun="Valle de Santiago (col. Los Antorchistas)", dia="24-OCT, ~13:35 POR RESUMEN",
  title="GUANAJUATO · VALLE DE SANTIAGO — ASESINAN A UN HOMBRE DENTRO DE SU CASA",
  hecho="Valle de Santiago · <code>COL. LOS ANTORCHISTAS, SOLO POR RESUMEN</code> · sábado 24-OCT, por ruta (AM 2026/10/24) · ~13:35, " + RES + " · <b>1 muerto</b>, hombre, dentro de su casa, por titular (🟡 homicidio doloso único) · ~50 años, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Hombre asesinado en su casa: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente regional; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["AM (2026/10/24)"], estatus="Pendiente de corroboración", arm=None,
  desl="Los Antorchistas no figura en las cinco ediciones previas ni en el índice. Valle de Santiago, 2 a 4-oct: ventanas anteriores, otros hechos."),
 dict(id="ARG-140-014", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-23", hora="noche (solo por resumen)", mu=0, he=0, cu=0,
  ent="Michoacán", mun="Indaparapeo (base de operaciones de seguridad)", dia="23-OCT, NOCHE POR RESUMEN",
  title="MICHOACÁN · INDAPARAPEO — DISPARAN CONTRA POLICÍAS EN UNA BASE DE OPERACIONES; SIN LESIONADOS",
  hecho="Indaparapeo · <code>BASE DE OPERACIONES INTERINSTITUCIONAL, SOLO POR RESUMEN</code> · publicado el viernes 23-OCT, por ruta (Grupo Marmor 2026/10/23); noche del 23 o 24-OCT, " + RES + ": <code>DÍA CONTRADICHO</code> · disparos contra policías, por titulares; «durante operativo», por titular (Changoonga 2026/10/24) · militares y policías estatales repelieron; agresores huyeron al cerro, " + RES + " · <b>sin lesionados</b>, por titular · <b>ningún detenido</b> ni arma asegurada, " + RES + " · (🟡: <code>QUIÉN INICIÓ, NO DETERMINADO</code>)",
  panel="Disparos contra policías; <b>sin lesionados</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día contradicho; quién inició no determinado; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Grupo Marmor (2026/10/23)", "Changoonga (2026/10/24)"], estatus="Parcialmente corroborado", arm=None,
  desl="Indaparapeo no figura en las cinco ediciones previas ni en el índice. Grupo Marmor y Red Michoacán publican el mismo título: una fuente."),
 dict(id="ARG-140-015", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-21", hora="noche (solo por resumen)", mu=1, he=2, cu=0,
  ent="Veracruz", mun="Álamo Temapache (domicilio) y Papantla (taquería)", dia="21-OCT, NOCHE POR RESUMEN",
  title="VERACRUZ · ÁLAMO Y PAPANTLA — DOS ATAQUES ARMADOS: UN MUERTO Y DOS HERIDOS",
  hecho="Álamo Temapache y Papantla · <code>ÁLAMO: UN DOMICILIO · PAPANTLA: UNA TAQUERÍA, SOLO POR RESUMEN</code> · noche del miércoles 21-OCT, " + RES + " · publicado el 22-OCT, por ruta (Formato 7 2026/10/22) · <b>dos ataques</b> con <b>1 muerto</b> y <b>2 heridos</b> en total, por titular (🟡) · reparto de víctimas entre los dos municipios, " + RES + " · <code>RELACIÓN ENTRE LOS DOS ATAQUES NO ACREDITADA</code> · <b>ningún detenido publicado</b>",
  panel="Dos ataques: <b>1 muerto</b> y 2 heridos", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente efectiva; día solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Formato 7 (2026/10/22)"], estatus="Pendiente de corroboración", arm=None,
  desl="XEU replica el título de Formato 7: una fuente. Álamo figura en ARGOS 139 (Estero del Ídolo, martes 20, menor asesinado, visto): otro hecho. Papantla en el índice: otro hecho."),
 dict(id="ARG-140-016", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeno", fecha="2026-10-23", hora="madrugada (solo por resumen)", mu=2, he=0, cu=0,
  ent="Veracruz", mun="Cosoleacaque (camino a Temex, dos puntos)", dia="23-OCT, MADRUGADA POR RESUMEN",
  title="VERACRUZ · COSOLEACAQUE — ASESINAN A UN ADOLESCENTE Y A UN JOVEN EN DOS PUNTOS DEL CAMINO A TEMEX",
  hecho="Cosoleacaque · <code>CAMINO A TEMEX, DOS PUNTOS DISTINTOS, SOLO POR RESUMEN</code> · madrugada del viernes 23-OCT, " + RES + " · publicado el 23-OCT, por ruta (Golpe Político 2026/10/23) · <b>2 muertos</b>, uno de 17 años, por titulares · <code>RELACIÓN ENTRE LOS DOS HOMICIDIOS NO ACREDITADA</code> (🟡; sube a 🔴 si se acredita un solo ataque) · <b>ningún detenido publicado</b>",
  panel="Dos homicidios en dos puntos: <b>2 muertos</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="relación entre los hechos no acreditada; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Golpe Político (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cosoleacaque figura en ARG-105-REC-004 (agosto) y en una sentencia federal vista en ARGOS 135-136: otros hechos."),
 # ======================= VERDES
 dict(id="ARG-140-017", estado="MX-CMX", region="Centro", color="verde", impacto="pequeno", fecha="2026-10-23", hora="tarde (solo por resumen)", mu=0, he=0, cu=0,
  ent="Ciudad de México", mun="Iztacalco (calle Coruña, col. Santa Anita)", dia="23-OCT",
  title="CIUDAD DE MÉXICO · IZTACALCO — DETIENEN A DOS JÓVENES POR EL ATAQUE DE CALZADA ERMITA",
  hecho="Iztacalco · <code>CALLE CORUÑA, COL. SANTA ANITA, SOLO POR RESUMEN</code> · viernes 23-OCT, por ruta (La Razón, Tribuna y Quinto Poder 2026/10/23; Infobae 2026/10/24) · <b>2 detenidos</b>, de 22 años, por titulares · localizados por las cámaras del C2 Oriente, " + RES + " · una arma corta y la motocicleta aseguradas, " + RES + " · a disposición del MP por homicidio, " + RES + " · hecho delictivo: ARG-140-001",
  panel="Detención: <b>2 detenidos</b> por el ataque de Calzada Ermita", inst="SSC CDMX" + PR, nac="La Razón · Infobae", conf="★★★☆☆",
  campo="aseguramiento y fuente institucional solo por resumen", I=1, N=2, R=2, A=0,
  fechadas=["La Razón (2026/10/23)", "Tribuna (2026/10/23)", "Quinto Poder (2026/10/23)", "Infobae (2026/10/24)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — una arma corta, solo por resumen: no se integra",
  desl="Delito y detención en la misma ventana: dos fichas. Comunicado de la SSC no indexado."),
 dict(id="ARG-140-018", estado="MX-VER", region="Golfo", color="verde", impacto="pequeno", fecha="2026-10-22", hora="no fijada", mu=0, he=0, cu=0,
  ent="Veracruz", mun="Xalapa", dia="22-OCT, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-22 — DÍA SOLO POR RESUMEN",
  title="VERACRUZ · XALAPA — DETIENEN AL PRESUNTO HOMICIDA DEL PROFESOR ASESINADO EN SU AUTOMÓVIL",
  hecho="Xalapa · detención el jueves 22-OCT, " + RES + " · publicada el 23 y el 24-OCT, por ruta (Golpe Político 2026/10/23; La Silla Rota 2026/10/24) · <b>1 detenido</b>, por titulares · imputado por homicidio doloso calificado, según la FGE, " + RES + " · operativo con el Ejército, " + RES + " · hecho delictivo: ARG-139-005, ventana de ARGOS 139 · la víctima, profesor de una secundaria pública, por titulares (Gráfico al Día 2026/10/21; La Silla Rota): <code>SIN ACREDITACIÓN INSTITUCIONAL DE SU CALIDAD DE SERVIDOR PÚBLICO</code>",
  panel="Detención: <b>1 detenido</b> por el homicidio de un profesor", inst="FGE Veracruz" + PR, nac="La Silla Rota", conf="★★★☆☆",
  campo="día de la detención solo por resumen; fuente institucional solo por resumen", I=1, N=1, R=1, A=0,
  fechadas=["Golpe Político (2026/10/23)", "La Silla Rota (2026/10/24)"], estatus="Parcialmente corroborado", arm=None,
  desl="ARG-139-005 conserva su color (🟡) mientras ninguna autoridad acredite la calidad de servidor público de la víctima."),
 dict(id="ARG-140-019", estado="MX-OAX", region="Sureste", color="verde", impacto="mediano", fecha="2026-10-22", hora="no fijada", mu=0, he=0, cu=0,
  ent="Oaxaca", mun="Juchitán de Zaragoza", dia="PUB. 22-OCT; HECHO NO FIJADO",
  fecha_txt="publicado el 2026-10-22 — FECHA DEL HECHO NO FIJADA (21 o 22-oct)",
  title="OAXACA · JUCHITÁN — DETIENEN A SIETE PERSONAS POR SEIS HOMICIDIOS RECIENTES",
  hecho="Juchitán de Zaragoza · publicado el jueves 22-OCT (boletín de la FGEO, por título; Latinus 2026/10/22) · <code>FECHA DE LA DETENCIÓN NO FIJADA</code> · <b>7 detenidos</b>, por titulares —dos mujeres, cuatro hombres y un adolescente, " + RES + "— · relacionados con «seis homicidios recientes», por título del boletín · FGEO, Policía Estatal, Defensa y Guardia Nacional, " + RES + " · <b>1 arma larga</b>, cargadores y cartuchos sin cantidad, mariguana y cristal, " + RES + " · <code>VINCULACIÓN DE CADA DETENIDO CON CADA HOMICIDIO, PRESUNTA</code> · iniciales publicadas: no se reproducen",
  panel="<b>7 detenidos</b> por seis homicidios", inst="FGEO" + PT, nac="El Universal · Latinus · Imagen Radio", conf="★★★☆☆",
  campo="fecha del hecho no fijada; aseguramiento solo por resumen", I=1, N=3, R=2, A=0,
  fechadas=["Latinus (2026/10/22)", "Diario de Yucatán (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  armtxt="sin fila — cantidades solo por resumen: evento cualitativo",
  desl="Ninguna ficha previa de estos detenidos. Diario de Yucatán reproduce la nota nacional: no se cuenta como independiente. Homicidios de Juchitán del 19 al 21-oct: ARG-138-001 y ARG-139-003, ventanas anteriores."),
 dict(id="ARG-140-020", estado="MX-PUE", region="Centro", color="verde", impacto="grande", fecha="2026-10-22", hora="no fijada", mu=0, he=0, cu=0,
  ent="Puebla", mun="Puebla de Zaragoza y Amozoc; y Iztapalapa, Ciudad de México", dia="22-OCT, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-22 — DÍA SOLO POR RESUMEN (boletín federal del 22-oct)",
  title="PUEBLA Y CIUDAD DE MÉXICO — CINCO CATEOS: CUATRO DETENIDOS Y 36 ARMAS DE UNA RED DE FABRICACIÓN",
  hecho="Puebla de Zaragoza, Amozoc e Iztapalapa · acciones del 22-OCT, por título del boletín federal, " + RES + " · publicado el 23 y el 24-OCT, por ruta (El Diario de Chihuahua 2026/oct/23, ABC Noticias e Intolerancia 2026/10/23, Diario Puntual 2026/10/24) · <b>5 cateos</b>, <b>4 detenidos</b> y <b>36 armas</b>, por titular (Diario Puntual); 37, " + RES + ": <code>CONTRADICHO, SE INTEGRA LA CIFRA DEL TITULAR</code> · red de fabricación de armas, por titulares; armas artesanales y un torno, " + RES + " · SSPC, FGR y Marina, " + RES + " · <code>DESGLOSE CORTAS/LARGAS NO PUBLICADO</code>",
  panel="Cinco cateos: <b>4 detenidos</b> y <b>36 armas</b>", inst=BF, nac="N+", conf="★★★☆☆",
  campo="desglose no publicado; cifra contradicha (36/37); boletín leído por republicadores", I=1, N=1, R=4, A=0,
  fechadas=["El Diario de Chihuahua (2026/oct/23)", "ABC Noticias (2026/10/23)", "Intolerancia (2026/10/23)", "Diario Puntual (2026/10/24)"], estatus="Parcialmente corroborado", arm="ARG-140-ARM-001",
  desl="Boletín federal del 22-oct y medios: un solo aseguramiento, contado una vez. Iztapalapa: otro hecho que ARG-140-001 y -017."),
 dict(id="ARG-140-021", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-22", hora="no fijada", mu=0, he=0, cu=0,
  ent="Sinaloa", mun="Culiacán", dia="22-OCT, DÍA SOLO POR RESUMEN",
  fecha_txt="2026-10-22 — DÍA SOLO POR RESUMEN (boletín federal del 22-oct)",
  title="SINALOA · CULIACÁN — DETIENEN A CUATRO PERSONAS, ENTRE ELLAS UN LÍDER DE CÉLULA",
  hecho="Culiacán · acciones del 22-OCT, por título del boletín federal (Milenio, <i>slug</i> «22-de-octubre-2026»), " + RES + " · <b>4 detenidos</b>, uno señalado como líder de una célula, " + RES + " · 4 armas largas, 25 cargadores, 1,338 cartuchos, granadas (2, en un resumen), 50 pastillas de fentanilo y 200 dosis de cocaína, " + RES + ": <code>CIFRAS NO SE INTEGRAN</code>",
  panel="<b>4 detenidos</b>, uno líder de célula", inst=BF, nac="Milenio", conf="★★☆☆☆",
  campo="todas las cifras solo por resumen de un boletín leído por republicadores", I=1, N=1, R=0, A=0,
  fechadas=["Milenio (slug, 22-oct-2026)"], estatus="Pendiente de corroboración", arm=None,
  armtxt="sin fila — cifras solo por resumen: evento cualitativo",
  desl="Republicadores del boletín (SICOM, RED113, Talla Política): una fuente. Liveblog de Infobae del 23-oct sobre la captura del líder de «Los Ranas»: no fecha ni sostiene nada."),
 dict(id="ARG-140-022", estado="MX-CHH", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-22", hora="no fijada", mu=0, he=0, cu=0,
  ent="Chihuahua", mun="Chihuahua (Distrito Judicial Morelos; audiencia por videoconferencia desde el Altiplano)", dia="22-OCT",
  title="CHIHUAHUA — VINCULAN A PROCESO AL EXFISCAL POR EJERCICIO ILEGAL DEL SERVICIO PÚBLICO; DESCARTAN COALICIÓN",
  hecho="Chihuahua · jueves 22-OCT, por ruta (La Jornada, La Razón y MVS 2026/10/22) · <b>vinculación a proceso estatal</b> del exfiscal por <b>ejercicio ilegal del servicio público</b>, por titulares · el juez <b>descartó el delito de coalición</b>, por titular (Infobae 2026/10/23) · causa 3055/2026 y plazo de dos meses de investigación complementaria, " + RES + " · un medio atribuye la resolución a un juez federal: <code>CONTRADICHO</code> · la defensa impugnará, por titular (Aristegui) · <code>NO ES SENTENCIA</code> · identidad pública por su cargo; nombre no reproducido",
  panel="Exfiscal <b>vinculado a proceso</b> (fuero común)", inst=SB, nac="La Jornada · La Razón · MVS · Infobae · Proceso", conf="★★★☆☆",
  campo="causa y plazo solo por resumen; comunicado de la FGE Chihuahua no localizado", I=0, N=7, R=1, A=0,
  fechadas=["La Jornada (2026/10/22)", "La Razón (2026/10/22)", "MVS (2026/10/22)", "Informador (20261022)", "Infobae (2026/10/23)", "Proceso (2026/10/23)", "860 Líder Informativo (2026/10/23)"], estatus="Parcialmente corroborado", arm=None,
  desl="Seguimiento de ARG-136-006; la prisión preventiva federal del 21-oct ya figura en ARGOS 139: no se repite. Causa distinta de la federal (ARG-140-023)."),
 dict(id="ARG-140-023", estado="MX-CHH", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-24", hora="no fijada (audiencia del sábado 24; publicación del 25)", mu=0, he=0, cu=0,
  ent="Chihuahua", mun="Caso Chihuahua (audiencia en el Centro de Justicia Penal Federal del Altiplano)", dia="24-OCT, HORA NO FIJADA",
  title="FEDERAL — VINCULAN A PROCESO AL EXFISCAL DE CHIHUAHUA POR TRAICIÓN A LA PATRIA",
  hecho="Altiplano · audiencia del sábado 24-OCT, por titular de Infobae 2026/10/23 (continuaría el sábado) · resolución publicada el domingo 25-OCT, por ruta (La Razón, Infobae, Zolo Noticias 2026/10/25; El Diario 2026/oct/25; El Pueblo 20261025) · " + FR + " · <b>vinculación a proceso federal</b> por <b>traición a la patria</b>, por titulares · sigue en el Altiplano, por titular (Infobae) · causa 408/2026, prisión preventiva y dos meses de investigación complementaria, " + RES + " · audiencia extendida a la madrugada del 25, " + RES + " · comunicado de la FGR no localizado · <code>NO ES SENTENCIA</code>",
  panel="Exfiscal <b>vinculado a proceso</b> (federal)", inst=SB, nac="La Razón · Infobae · Excélsior · Milenio", conf="★★★☆☆",
  campo="hora de la resolución no fijada; causa y plazo solo por resumen; sin comunicado de la FGR", I=0, N=5, R=3, A=0,
  fechadas=["La Razón (2026/10/25)", "Infobae (2026/10/25)", "El Diario (2026/oct/25)", "Zolo Noticias (2026/10/25)", "El Pueblo (20261025)"], estatus="Parcialmente corroborado", arm=None,
  desl="Seguimiento de ARG-136-006 y de ARG-140-022 (causa estatal, otra). Si la resolución se dictó después de las 07:45 del 25, pertenece a ARGOS 141 (fe de erratas)."),
]

# ---------------------------------------------------------------- RECUPERACIONES (ventana de ARGOS 139; solo alto impacto)
R = [
 dict(id="ARG-140-REC-001", estado="MX-MIC", region="Occidente", fecha="2026-10-20", hora="~23:30 o madrugada del 21 (solo por resumen)", orig="ARGOS 139 — DÍA Y HORA SOLO POR RESUMEN", col_orig="rojo", mu=3, he=2, cu=0,
  ent="Michoacán", mun="Ario de Rosales (La Palma); Salvador Escalante en otra nota", dia="20-OCT, NOCHE",
  title="MICHOACÁN · ARIO DE ROSALES — ATAQUE ARMADO EN LA PALMA: TRES MUERTOS Y DOS HERIDOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 139 — DÍA Y HORA SOLO POR RESUMEN</code> · Ario de Rosales, por titulares · <code>LOCALIDAD LA PALMA, SOLO POR RESUMEN; SALVADOR ESCALANTE, POR TITULAR DE QUADRATÍN: MUNICIPIO CONTRADICHO</code> · noche del martes 20-OCT (~23:30) o madrugada del 21, " + RES + "; antes de las 10:23 en ambos casos · primera ruta fechada: 21-OCT (MVS; Grupo Marmor) · <b>3 muertos</b> y <b>2 heridos</b>, por titulares (🔴 homicidio múltiple) · víctimas de 18, 19 y 24 años; heridos de 57 y de 14 o 15 años, " + RES + " · ataque a una vivienda o paraje serrano, " + RES + " · vehículo con blindaje artesanal y móvil atribuido a la Fiscalía, " + RES + ": <code>NO SE INTEGRA</code> · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>3 muertos</b> y 2 heridos", inst=SB, nac="MVS",
  conf="★★★☆☆", campo="día, hora y municipio contradichos; ninguna fuente institucional", I=0, N=1, R=7, A=0,
  fechadas=["MVS (2026/10/21)", "Grupo Marmor (2026/10/21)"],
  desl="Ario de Rosales, La Palma (Michoacán) y Salvador Escalante no figuran en las cinco ediciones previas; «La Palma» del índice es Navolato (ARG-138-007) y «Ario» en ARGOS 135 es una calle de Apatzingán: otros. Grupo Marmor y Red Michoacán publican el mismo título: una fuente."),
 dict(id="ARG-140-REC-002", estado="MX-MEX", region="Centro", fecha="2026-10-21", hora="~06:10 (solo por resumen)", orig="ARGOS 139 — HORA SOLO POR RESUMEN", col_orig="rojo", mu=1, he=1, cu=0,
  ent="Estado de México", mun="Cocotitlán (carretera México–Cuautla, cerca del acceso a San Andrés Metla)", dia="21-OCT, ~06:10",
  title="ESTADO DE MÉXICO · COCOTITLÁN — ATACAN UNA PATRULLA EN LA MÉXICO–CUAUTLA: UN POLICÍA MUERTO Y OTRO HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 139 — HORA SOLO POR RESUMEN</code> · Cocotitlán · <code>CARRETERA MÉXICO–CUAUTLA, CERCA DEL ACCESO A SAN ANDRÉS METLA, SOLO POR RESUMEN</code> · madrugada del miércoles 21-OCT, ~06:10, " + RES + " · primera ruta fechada: 22-OCT (El Gráfico; Diario de Yucatán; Síntesis; Reporteros en Movimiento) · patrulla municipal atacada a balazos, por titulares · <b>1 policía municipal muerto</b> y <b>1 herido</b>, por titulares (🔴 muerte de personal de seguridad) · «estaba en servicio», confirmó el municipio, por titular (Plana Mayor) · el herido, en la cabeza y grave, " + RES + "; «dos policías» atacados, por titular de El Gráfico: <code>NÚMERO DE HERIDOS CONTRADICHO</code> · «emboscada», por titulares (Posta, Cuestión de Polémica); el municipio descarta un ataque directo, " + RES + ": <code>MODALIDAD CONTRADICHA</code> · la FGJEM investiga · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Policía municipal asesinado</b> y otro herido", inst="Ayuntamiento de Cocotitlán" + PT, nac="Excélsior · Milenio · Posta · Telediario · El Gráfico",
  conf="★★★☆☆", campo="hora solo por resumen; modalidad y número de heridos contradichos", I=1, N=5, R=6, A=0,
  fechadas=["El Gráfico (2026/10/22)", "Diario de Yucatán (2026/10/22)", "Síntesis (2026/10/22)", "Reporteros en Movimiento (2026/10/22)"],
  desl="Cocotitlán y San Andrés Metla no figuran en las cinco ediciones previas ni en el índice. El ataque a «dos policías en la México–Cuautla» (El Gráfico 2026/10/22) es este hecho. Choque de la La Pera–Cuautla (12-oct): otro hecho."),
 dict(id="ARG-140-REC-003", estado="MX-MEX", region="Centro", fecha="2026-10-20", hora="noche (solo por resumen)", orig="ARGOS 139 — DÍA SOLO POR RESUMEN, CONTRADICHO", col_orig="rojo", mu=4, he=1, cu=0,
  ent="Estado de México", mun="Ecatepec (Santa María Tulpetlac, calle Oaxaca)", dia="20-OCT, NOCHE",
  title="ESTADO DE MÉXICO · ECATEPEC — ATAQUE ARMADO EN UN INMUEBLE DE TULPETLAC: CUATRO MUERTOS Y UNA HERIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 139 — DÍA SOLO POR RESUMEN, CONTRADICHO</code> · Ecatepec · <code>SANTA MARÍA TULPETLAC, CALLE OAXACA, SOLO POR RESUMEN</code> · «la noche del martes» 20-OCT, " + RES + " · primera ruta fechada: 22-OCT (El Gráfico); hora de publicación de El Universal, 22-oct 03:10, " + RES + ": <code>LA PUBLICACIÓN ES COMPATIBLE CON LA NOCHE DEL MIÉRCOLES 21 — DÍA NO FIJADO</code> · <b>4 muertos</b> dentro del inmueble —tres hombres y una mujer— y <b>1 mujer herida</b> fuera, por titulares y resumen (🔴 homicidio múltiple) · inmueble señalado como punto de venta de droga, por titular (El Gráfico) · agresores en un sedán blanco, " + RES + " · la Fiscalía mexiquense investiga · <b>ningún detenido publicado</b>",
  panel="Ataque armado: <b>4 muertos</b> y 1 herida", inst=SB, nac="El Universal · El Gráfico",
  conf="★★★☆☆", campo="día contradicho entre el resumen y la publicación; ninguna fuente institucional", I=0, N=2, R=2, A=0,
  fechadas=["El Gráfico (2026/10/22)"],
  desl="Tulpetlac no figura en las cinco ediciones previas ni en el índice. NO es «Ecatepec Colosio» (19-oct, visto en ARGOS 139) ni la balacera de El Obraje Diamante (septiembre). Si el ataque fue la noche del miércoles 21, es hecho propio de ARGOS 140 y entra en sus totales por fe de erratas."),
]

for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-140-ARM-001", ficha="ARG-140-020", estado="MX-PUE", region="Centro", color="verde", ent="Puebla y Ciudad de México", mun="Puebla de Zaragoza, Amozoc e Iztapalapa",
  fecha="2026-10-22", fecha_txt="22-oct (solo por resumen)", hora="no fijada", c=[0, 0, 36, 0, 0, 0, 0, 0, 0, 4], nd=[0, 1, 3, 4, 5, 6, 7, 8], integra=True,
  corp="SSPC, FGR y Marina <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="36 armas y 4 detenidos por titular (Diario Puntual 2026/10/24); 37, solo por resumen; desglose no publicado",
  fuentes=["Diario Puntual (2026/10/24)", "El Diario de Chihuahua (2026/oct/23)", "ABC Noticias (2026/10/23)", "Boletín federal del 22-oct (republicadores)"]),
]
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["estado"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
HORAS = 93 + 22 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
assert TOT == [0, 0, 36, 0, 0, 0, 0, 0, 0, 4], TOT
assert cnt == {"rojo": 7, "amarillo": 9, "verde": 7}, cnt
assert cnt_rec == {"rojo": 3, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC) == (14, 5, 7, 8, 4), (MU, HE, CU, MU_REC, HE_REC)
assert (NFR, NAP, len(ENT), len(ENT_ROJO)) == (1, 2, 13, 5), (NFR, NAP, len(ENT), len(ENT_ROJO))
assert DENS == "0,25", DENS
assert all(e["id"] == f"ARG-140-{i+1:03d}" for i, e in enumerate(E))
assert len(set(r["id"] for r in R)) == len(R) and all(r["id"] == f"ARG-140-REC-{i+1:03d}" for i, r in enumerate(R))
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-21" or x in R, x["id"]

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
head = head.replace("<title>ARGOS 139 — Reporte Nacional de Seguridad — 2026-10-21</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DEL ESTADO DE MÉXICO LA FECHA Y LA HORA OFICIALES, LA IDENTIFICACIÓN DE LAS VÍCTIMAS Y LA LÍNEA DE INVESTIGACIÓN</b> (ARG-140-REC-003).
      <br><b>2. SOLICITE A LA FISCALÍA DE TABASCO LA IDENTIFICACIÓN GENÉTICA, LA CAUSA DE MUERTE Y SI EL CASO GUARDA RELACIÓN CON OTROS HALLAZGOS DEL MUNICIPIO</b> (ARG-140-006).
      <br><b>3. SOLICITE A LA FISCALÍA DE OAXACA EL DESGLOSE QUE VINCULE A CADA DETENIDO CON CADA HOMICIDIO Y LA FECHA DE LA AUDIENCIA DE IMPUTACIÓN</b> (ARG-140-019).
      <br><b>4. SOLICITE A LA FISCALÍA DE MICHOACÁN EL MUNICIPIO, LA HORA Y LA CARPETA DE INVESTIGACIÓN</b> (ARG-140-REC-001).
      <br><b>5. SOLICITE A LA PGJ DE HIDALGO LA NUEVA FECHA DE LA AUDIENCIA DE INDIVIDUALIZACIÓN Y LA PENA DEL FALLO CONDENATORIO</b> (Santiago Tulantepec; ver Rastreo de Sentencias).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]])))
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>21-oct 10:23 → 25-oct 07:45 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · dentro de cada color, del más reciente al más antiguo.
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
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b></td><td><b>{TOT[0]}</b></td><td><b>{TOT[1]}</b></td><td><b>{TOT[2]}</b></td><td><b>{fmt(TOT[4])}</b></td><td><b>{TOT[5]}</b></td><td><b>{TOT[6]}</b></td><td><b>{TOT[7]}</b></td><td><b>{TOT[8]}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: un solo aseguramiento con cantidad por titular (ARG-140-ARM-001), <b>sin desglose</b>: las categorías en cero de esa fila son <code>NO PUBLICADO</code>, no ausencia · <b>cuerpos hallados</b>: causa de muerte no informada, fuera del recuento de muertos por agresión; los restos de Reynosa (ARG-140-007), sin número de víctimas, fuera de todo recuento · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · en las recuperaciones, <b>{MU_REC} muertos</b> y <b>{HE_REC} heridos</b>, fuera de todo total. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-139-001, parentesco «madre e hijo» / «pareja»: <code>CONTRADICHO</code> · ARG-139-002, sin causa de muerte ni identificación oficial · ARG-139-003, adscripción municipal por reconocimiento de compañeros, {RES}; la FGEO vincula a siete detenidos con seis homicidios recientes (ARG-140-019) · ARG-139-005, detenido el presunto homicida (ARG-140-018) · ARG-139-007, la hora «21-oct 07:04» es la de publicación de N+, no la del ataque · ARG-139-008, hora ~06:00 {RES}: sin fijar · ARG-139-REC-002, «reanudan ataques» (El Diario de Chihuahua 2026/oct/20) se refiere al ataque del 19: sin nueva agresión publicada · ARG-139-REC-003, herido, fuera de peligro, {RES} · ARG-125-003 (Xalisco), tres fosas con cinco cuerpos en Tecuala y diez detenidos, {RES}: <code>POSIBLE DUPLICIDAD CON ARG-133-REC-007 — NO SE INTEGRA HASTA VALIDACIÓN</code> · ARG-135-REC-003 (Tijuana), cifra oficial no publicada.
  </p>
'''

rec1 = "\n".join(ficha(r, True) for r in R)
co1 = "\n".join(ficha(e) for e in E[0:4])
co2 = "\n".join(ficha(e) for e in E[4:7])
co3 = "\n".join(ficha(e) for e in E[7:12])
co4 = "\n".join(ficha(e) for e in E[12:16])
co5 = "\n".join(ficha(e) for e in E[16:20])
co6 = "\n".join(ficha(e) for e in E[20:])

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>NO PUBLICADO EN EL ÚNICO EVENTO CON CANTIDAD</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], NI),
 tile(1, "Armas largas", TOT[1], NI),
 tile(2, "Sin categoría", TOT[2], "<b>1 evento</b> (ARG-140-ARM-001), por titular; desglose no publicado"),
 tile(3, "Cartuchos", fmt(TOT[4]), NI),
 tile(4, "Cargadores", TOT[5], NI),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA INTEGRABLE</code>; boletín del 22-oct, solo por resumen"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI INTEGRABLE</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR INTEGRABLE</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<b>en el mismo evento de aseguramiento</b>, por titular"),
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
    <div class="map-caption">Un aseguramiento integrable: Puebla (con cateo en Iztapalapa).</div>
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
{chr(10).join(armrow(a) for a in ARM)}
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Lectura regional</b>: Centro, 1 evento (36 armas sin categoría, 4 detenidos); el resto de regiones, sin evento integrable. <b>Cálculo propio</b>.
    <br><code>VISTOS, NO INTEGRADOS — CIFRAS SOLO POR RESUMEN</code>: boletín federal del 22-oct — <b>Sinaloa, Culiacán</b> (ARG-140-021): 4 largas, 25 cargadores, 1,338 cartuchos y granadas · <b>Chihuahua, Ojinaga</b>: 1 larga y 1 granada o aditamento lanzagranadas (<code>CONTRADICHO</code>), 1 detenido · <b>Hidalgo, Juárez</b>: 2 armas, 1 cargador, 24 cartuchos, 250 L de hidrocarburo, 2 detenidos · boletín federal del 21-oct — <b>Quintana Roo</b>: 2 largas, 2 cortas, 4 cargadores · <b>Veracruz</b>: 2 largas, 1 corta, 4 detenidos · <b>Oaxaca, Juchitán</b> (ARG-140-019): 1 larga · <b>Ciudad de México, Iztacalco</b> (ARG-140-017): 1 corta · <b>Colima</b>: armas y un AEI de una célula, sin cifra ni fecha fijada: cualitativo.
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code>: <b>Chiapas, Huixtla</b>, aduana, martes 20-oct (El Sol del Soconusco 2026/10/20): 4 detenidos, 1 carabina y 3 pistolas en una sola fuente; ventana de ARGOS 139, <code>FUERA DEL TOTAL</code>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">3 candidatas en ventana, sin boletín leído</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>ningún caso integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub">ver indicador de cobertura</span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS EN VENTANA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Tres sentenciados, nombres no reproducidos · <span class="muted-note">fallo condenatorio del 8-oct por la muerte de tres mujeres (La Silla Rota 2026/10/9)</span></td><td><b>Sin pena</b>: audiencia de individualización del 21-oct pospuesta «por falla de energía», por titular (La Jornada Hidalgo, sin fecha en la ruta); nueva fecha 28-oct, {RES}</td><td>Tribunal de Enjuiciamiento de Tulancingo <span class="muted-note">(solo por resumen)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín de la PGJEH · «40 a 90 años» es estimación de la asesoría de las víctimas, no pena</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Saltillo</td><td>Un sentenciado · <span class="muted-note">transporte de más de un kilo de metanfetamina, {RES}</span></td><td><b>7 años</b>, {RES}</td><td>FGR <span class="muted-note">(listado de fgr.org.mx, 22-oct, por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · boletín no leído; número de comunicado ambiguo · firmeza no informada</td><td>No confirmado</td></tr>
      <tr><td><b>Jalisco</b><br>Tlajomulco, Zapotlanejo y El Salto</td><td>Tres comunicados de sentencia condenatoria · <span class="muted-note">portación de arma y cartuchos, {RES}</span></td><td><b>No obtenida</b></td><td>FGR <span class="muted-note">(listado de fgr.org.mx, 21-oct, por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · {AP} · penas y número de personas no obtenidos</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Candidatas heredadas, publicadas antes de la ventana y sin boletín leído</b>: Culiacán, 18 años (19-oct) · Ensenada, tres sentenciados, 158 años 9 meses por titular (Sin Embargo), «158 años» en otro titular: redondeo, <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code> (17-oct) · General Cepeda, 13 años 4 meses (FGR, 19-oct) · Caborca, 8 años (FGR, 19-oct). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>11 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Chih, Dgo · CDMX, Pue, Qro, Hgo, Tlax · Ver · Chis, Yuc — todas de lectura parcial (último ítem indexado anterior a la ventana) · <b>FGR</b>: <code>gob.mx/fgr</code> solo devolvió 2019-2022; listados de <code>fgr.org.mx</code> del 21 y 22-oct</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> estatales · FGR: 4 comunicados de sentencia en listados (Jalisco 3, Coahuila 1), sin texto leído</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>11</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>9</b>: Sin, Tamps, Coah, Zac, Camp, Tab, Gto, Jal, Col</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>12</b>: BCS, Son · NL, SLP · Nay, Ags, Mich · Edomex, Mor · Oax, Gro, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 25-oct 06:52: código <code>000</code> · <b>dominio nuevo confirmado</b>: <code>comunicacion.fiscaliaveracruz.gob.mx</code>, <code>portal.fgeo.gob.mx</code>, <code>fiscaliageneralqro.gob.mx</code>, <code>seguridad.slp.gob.mx</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 17 de 32 con consulta propia por entidad</b> (entre ellas las 7 pendientes de ARGOS 139: BC, Chih, Coah, NL, Ags, Gto, Edomex) · <b>15 solo por consulta regional amplia</b>: BCS, Son, Dgo · Jal, Col, Nay · CDMX, Mor, Pue, Tlax, Hgo, Qro · Chis, Camp, Yuc · <b>armamento: 11 de 32 por dominio oficial</b> —NL, Tamps, SLP · Mich, Ags · CDMX · Ver · Chis, Gro, Yuc, Oax—, todas de lectura parcial salvo Oax; <code>NO REVISADA</code> o dominio sin páginas (21): BC, BCS, Son, Chih, Sin, Dgo · Coah, Zac · Jal, Col, Nay, Gto · Edomex, Mor, Pue, Tlax, Hgo, Qro · Tab · Camp, QRoo</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 21 y del 22-oct</b>: existen; consultadas por sus republicadores (Ultranoticias, RED113, Talla Política, Certeza Diario; Milenio, SICOM) · <b>acciones del 23 y del 24-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas, repetidas al final de la consulta · <b>gabinetedeseguridad.gob.mx</b>: el buscador solo devuelve el agregado del 9 al 11-oct · Guardia Nacional, Defensa y Semar: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 25-OCT 06:52: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>{cnt["rojo"]} ROJOS PROPIOS EN {len(ENT_ROJO)} ENTIDADES</b>: dos contra personal de seguridad o de monitoreo (ARG-140-002 y -003), dos homicidios múltiples (-001 y -004) y tres hallazgos de cuerpos, fosa o restos (-005 a -007).
      <br><b>2.</b> <b>{cnt["amarillo"]} amarillos</b>: siete con muertos o heridos por ataque armado y dos agresiones sin muertos (-008 y -014).
      <br><b>3.</b> <b>{cnt["verde"]} acciones institucionales</b>: tres detenciones ligadas a homicidios (-017 a -019), dos cateos y aseguramientos (-020 y -021) y dos vinculaciones a proceso (-022 y -023).
      <br><b>4.</b> <b>Ventana de ARGOS 139</b>: tres rojos recuperados (ARG-140-REC-001 a -003), fuera de los totales.
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 139 SIN NORMALIZAR POR HORA; LOS DÍAS 23 A 25 TIENEN INDEXACIÓN INCOMPLETA.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. PERSONAL DE SEGURIDAD Y DE MONITOREO ATACADO FUERA DE UNA ACCIÓN OPERATIVA: TRES HECHOS, TRES MUERTOS</b> (cálculo propio): ARG-140-002 (policía al salir de su turno, en su motocicleta), ARG-140-003 (trabajador del C4i en su camioneta) y ARG-140-REC-002 (patrulla en carretera). Línea: <b>solicitar a las fiscalías de Guanajuato, Sinaloa y Estado de México si las víctimas tenían amenazas previas y si el ataque fue dirigido</b> — hipótesis, sin vínculo entre entidades.
      <br><b>2. CORREDOR MÉXICO–CUAUTLA, ORIENTE DEL ESTADO DE MÉXICO: DOS ATAQUES MORTALES EN CUATRO DÍAS</b> (cálculo propio): ARG-140-REC-002 (Cocotitlán, 21-oct) y ARG-140-010 (Ozumba, 24-oct), sobre la misma carretera. Línea: <b>solicitar a la FGJEM y a la Guardia Nacional el registro de agresiones en el tramo Cocotitlán–Ozumba y si comparten agresores</b> — hipótesis.
      <br><b>3. DOS HALLAZGOS SIN IDENTIFICACIÓN NI CAUSA DE MUERTE OFICIAL</b> (cálculo propio): ARG-140-005 (León: cinco cuerpos en cuatro puntos el mismo día, uno calcinado y uno desmembrado, por resumen) y ARG-140-007 (Reynosa: restos óseos hallados por un colectivo, sin número de víctimas). Línea: <b>solicitar a las fiscalías de Guanajuato y Tamaulipas la identificación, la causa de muerte y si los hallazgos se cruzan con fichas de búsqueda</b>.
      <br><b>4. SINALOA: VIOLENCIA EN TRES MUNICIPIOS Y RESPUESTA EN UNO</b> (cálculo propio): ARG-140-003 (Mazatlán), ARG-140-004 (Culiacán, dos muertos), ARG-140-008 (Escuinapa, transporte con estudiantes) y ARG-140-021 (Culiacán, cuatro detenidos, uno señalado como líder de célula). Línea: <b>solicitar a la FGE Sinaloa si los detenidos de Culiacán se vinculan con alguno de los ataques de la ventana</b> — vínculo no acreditado.
      <br><b>5. DETENCIONES SIN CIERRE JUDICIAL: DOS DETENCIONES LIGADAS A HOMICIDIOS, NINGUNA SENTENCIA INTEGRABLE</b> (cálculo propio): ARG-140-017 (dos detenidos por el ataque de Calzada Ermita, el mismo día), ARG-140-018 (Xalapa, dos días después del homicidio). Línea: <b>solicitar a la FGJCDMX y a la FGE Veracruz la audiencia de imputación y la vinculación de los detenidos</b>.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: CIUDAD DE MÉXICO, GUANAJUATO Y SINALOA", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: CUERPOS, FOSA Y RESTOS EN GUANAJUATO, TABASCO Y TAMAULIPAS", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA: SINALOA, MORELOS, ESTADO DE MÉXICO, NUEVO LEÓN Y GUANAJUATO", co3)
 + page("CRIMEN ORGANIZADO (IV) — VIOLENCIA OPERATIVA: GUANAJUATO, MICHOACÁN Y VERACRUZ", co4)
 + page("CRIMEN ORGANIZADO (V) — ACCIONES INSTITUCIONALES: DETENCIONES Y CATEOS", co5)
 + page("CRIMEN ORGANIZADO (VI) — ACCIONES INSTITUCIONALES: SINALOA Y PROCESOS DEL EXFISCAL", co6)
 + page("CRIMEN ORGANIZADO (VII) — VENTANA ANTERIOR: ARGOS 139", rec1)
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
assert "WINDOW_DAYS = 2;" in script
script = script.replace("WINDOW_DAYS = 2;", "WINDOW_DAYS = 5;")  # la ventana toca cinco fechas de calendario (21 a 25-oct)
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, MU, HE, CU, DENS)
