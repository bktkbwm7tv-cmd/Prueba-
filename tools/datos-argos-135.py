# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 135: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-135.py <plantilla ARGOS 134> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "135", "2026-10-17", "09:28"
CONSULTA = "2026-10-17 09:28-10:40"
DUR = "21 h 54 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
SB = "<span class=\"muted-note\">SIN BOLETÍN</span>"
NIN = "<span class=\"muted-note\">ninguna</span>"
AP = "<code>PUBLICADO EL DÍA DE APERTURA SIN HORA: PUEDE SER ANTERIOR A LAS 11:34 DEL 16</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-135-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-16", hora="~14:40–15:00 (solo por resumen)",
  ent="Sinaloa", mun="Culiacán (bulevar Gran Vía, Valle del Agua)", dia="16-OCT, TARDE",
  title="SINALOA · CULIACÁN — ASESINAN A DOS PRIMOS FRENTE A UN RESIDENCIAL DEL BULEVAR GRAN VÍA, RUMBO A IMALA",
  hecho="Culiacán · <code>BULEVAR GRAN VÍA, FRENTE AL RESIDENCIAL VILLA SAN JOSÉ, SECTOR VALLE DEL AGUA (LOS ÁNGELES, SEGÚN OTROS MEDIOS), JUNTO A LA CARRETERA A IMALA</code> · VIERNES 16-OCT, por ruta · ~14:40–15:00, " + RES + " · disparos contra dos hombres que conversaban junto a dos vehículos, por titular · <b>2 hombres muertos</b>, primos, por titular (🔴) · <code>ARMA LARGA O DE ALTO CALIBRE, SOLO POR RESUMEN</code> · <b>ningún detenido publicado</b> · FGE Sinaloa a cargo, " + RES + " · identidades: no se reproducen",
  panel="Ataque armado: <b>2 hombres muertos</b>",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora y tipo de arma solo por resumen; sin fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Línea Directa (2026-10-16)"], estatus="Parcialmente corroborado", arm=None,
  desl="Gran Vía, Valle del Agua e Imala no figuran en las cinco ediciones previas ni en el índice. El liveblog de Noroeste («este viernes») no fecha el hecho. 🔴 por homicidio múltiple"),
 dict(id="ARG-135-002", estado="MX-BCN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-10-16", hora="~19:00 (solo por resumen)",
  ent="Baja California", mun="Tijuana (col. Divina Providencia, delegación Playas)", dia="16-OCT, TARDE-NOCHE",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A UN BOMBERO VOLUNTARIO Y A UNA MUJER EN LA COLONIA DIVINA PROVIDENCIA",
  hecho="Tijuana · <code>CALLE CARRILLO PUERTO, COL. DIVINA PROVIDENCIA, DELEGACIÓN PLAYAS DE TIJUANA</code> · VIERNES 16-OCT, «la tarde del 16 de octubre», por titular · ~19:00, " + RES + " · disparos contra un hombre dentro de un vehículo; la mujer huye y es alcanzada, " + RES + " · <b>2 muertos</b> —un hombre, <b>bombero voluntario</b>, y una mujer—, por titular (🔴) · <code>4 CASQUILLOS 9 MM, SOLO POR RESUMEN</code> · peritos y AEI de la FGE Baja California en la escena, " + RES + " · <b>ningún detenido publicado</b> · móvil no publicado · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos</b>, uno de ellos bombero voluntario",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora y casquillos solo por resumen; sin fuente institucional", I=0, N=0, R=5, A=0,
  fechadas=["Zeta Tijuana (2026/10)", "Diario Tijuana (2026/10)"], estatus="Parcialmente corroborado", arm=None,
  desl="Divina Providencia no figura en las cinco ediciones previas ni en el índice. NO es ARG-133-006 (policía herido, Zona Industrial Pacífico). Bombero voluntario: no es servidor público acreditado. 🔴 por homicidio múltiple"),
 dict(id="ARG-135-003", estado="MX-MIC", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-16", hora="no publicada",
  ent="Michoacán", mun="Apatzingán (Las Cahuingas y col. El Varillero)", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="MICHOACÁN · APATZINGÁN — HALLAN A TRES HOMBRES TORTURADOS Y ASESINADOS, ENCOBIJADOS, EN DOS PUNTOS",
  hecho="Apatzingán · <code>LAS CAHUINGAS (1 CUERPO) Y COL. EL VARILLERO, CALLE MARIANO JIMÉNEZ (2 CUERPOS)</code> · VIERNES 16-OCT, por titular · hallazgo de <b>3 hombres muertos</b>, envueltos en cobijas, con impactos de bala y <b>huellas de tortura</b>, por titular (🔴) · el primero, de unos 35 años, hallado por campesinos; los otros dos, minutos después, por vecinos, " + RES + " · Fiscalía Regional de Apatzingán en diligencias, " + RES + " · <b>ningún detenido publicado</b> · identidades: no publicadas · " + AP + " · " + FR,
  panel="Hallazgo de <b>3 hombres torturados y asesinados</b>",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fecha solo por titular de un medio sin fecha en la ruta; hora no publicada", I=0, N=0, R=3, A=0,
  fechadas=[], estatus="Pendiente de corroboración", arm=None,
  desl="Las Cahuingas y El Varillero no figuran en las cinco ediciones previas. NO es ARG-134-REC-003 (El Guayabo) ni el hallazgo de junio con lesiones por explosivos (RED113 2026/06). 🔴 por homicidio múltiple con tortura"),
 dict(id="ARG-135-004", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-16", hora="«esta noche» del viernes (solo por resumen)",
  ent="Michoacán", mun="Apatzingán (col. Generalísimo Morelos)", dia="16-OCT, NOCHE · PUB. 17-OCT",
  title="MICHOACÁN · APATZINGÁN — HOMBRES ARMADOS IRRUMPEN EN UNA VIVIENDA Y ASESINAN A UNA MUJER FRENTE A SUS HIJOS",
  hecho="Apatzingán · <code>COL. GENERALÍSIMO MORELOS, CALLE PRIMER TRIBUNAL DE ARIO</code> · noche del VIERNES 16-OCT, " + RES + "; publicado el SÁBADO 17-OCT, por ruta · sujetos armados irrumpen en la vivienda, " + RES + " · <b>1 mujer muerta</b> a balazos frente a sus hijos menores, por titular (🟡) · <b>ningún detenido publicado</b> · móvil no publicado · identidad: no se reproduce · <code>VENDEDOR HERIDO EN UN PUESTO DE LA MISMA COLONIA MINUTOS ANTES: NEXO NO ESTABLECIDO, NO SE INTEGRA</code> · " + FR,
  panel="<b>Mujer asesinada</b> en su vivienda",
  inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Red Michoacán (2026/10/17)", "Grupo Marmor (2026/10/17)"], estatus="Parcialmente corroborado", arm=None,
  desl="Generalísimo Morelos no figura en las cinco ediciones previas. NO es ARG-135-003. 🟡 por homicidio doloso único"),
 dict(id="ARG-135-005", estado="MX-SON", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-16", hora="noche del viernes (solo por resumen)",
  ent="Sonora", mun="Hermosillo (Gala Residencial, zona sur)", dia="16-OCT, NOCHE · PUB. 17-OCT",
  title="SONORA · HERMOSILLO — HALLAN A UN HOMBRE ASESINADO A BALAZOS DENTRO DE UNA VIVIENDA DE GALA RESIDENCIAL",
  hecho="Hermosillo · <code>GALA RESIDENCIAL, ZONA SUR</code> · noche del VIERNES 16-OCT, " + RES + "; publicado el SÁBADO 17-OCT, por ruta · <b>1 hombre muerto</b> con impactos de bala dentro de una vivienda, por titular (🟡) · <b>ningún detenido publicado</b> · identidad: no publicada · " + FR,
  panel="<b>1 hombre asesinado</b> en una vivienda",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Proyecto Puente (2026/10/17)"], estatus="Pendiente de corroboración", arm=None,
  desl="Gala Residencial no figura en las cinco ediciones previas. NO es ARG-134-012 (Villas del Seris). 🟡 por homicidio doloso único"),
 dict(id="ARG-135-006", estado="MX-SON", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-10-16", hora="no publicada",
  ent="Sonora", mun="Hermosillo (zona sur, bulevar López Mateos)", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="SONORA · HERMOSILLO — AGRESIÓN ARMADA DEJA SIN VIDA A UN HOMBRE AL SUR DE LA CIUDAD",
  hecho="Hermosillo · <code>ZONA SUR, BULEVAR LÓPEZ MATEOS, SEGÚN EL RESUMEN</code> · publicado el VIERNES 16-OCT, por ruta · agresión armada, por titular · <b>1 hombre muerto</b>, de unos 50 años, " + RES + " (🟡) · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + AP + " · " + FR,
  panel="<b>1 hombre asesinado</b> al sur de la ciudad",
  inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="una sola fuente; hora no publicada", I=0, N=0, R=1, A=0,
  fechadas=["Proyecto Puente (2026/10/16)"], estatus="Pendiente de corroboración", arm=None,
  desl="NO es ARG-134-012 (Villas del Seris, noche del 15) ni ARG-135-005. 🟡 por homicidio doloso único"),
 dict(id="ARG-135-007", estado="MX-SIN", region="Noroeste", color="verde", impacto="grande", fecha="2026-10-16", hora="operativo no fechado; publicado el 2026-10-16",
  ent="Sinaloa", mun="Culiacán", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="SINALOA · CULIACÁN — CAEN CUATRO INTEGRANTES DE UNA CÉLULA DEDICADA A TRAFICAR Y REPARAR ARMAMENTO; ASEGURAN UNA AMETRALLADORA Y 417 CARTUCHOS",
  hecho="Culiacán · domicilios ubicados por trabajo de inteligencia e intercambio de información con HSI (EE. UU.), según el <b>Gabinete de Seguridad</b>, por cita · publicado el VIERNES 16-OCT · fecha del operativo: no publicada · <b>4 detenidos</b>, por titular; <b>dos con orden de aprehensión por delincuencia organizada y tráfico de armas</b>, " + RES + " (🟢) · <b>1 ametralladora</b> y <b>417 cartuchos</b>, por titular · <code>3 ARMAS CORTAS Y 16 CARGADORES, SOLO POR RESUMEN</code> · 200 dosis de droga y 1 vehículo, " + RES + " · situación jurídica: a determinar por el MP · identidades: no se reproducen · " + AP + " · " + FR,
  panel="<b>4 detenidos</b>; <b>1 ametralladora</b>, <b>3 cortas</b> y <b>417 cartuchos</b>",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(comunicado por cita)</span>", nac="Infobae · El Financiero · MVS · Publimetro · Crónica", conf="★★★☆☆",
  campo="armas cortas y cargadores solo por resumen; fecha del operativo no publicada", I=1, N=5, R=4, A=0,
  fechadas=["Infobae (2026/10/16)", "El Financiero (2026/10/16)", "MVS Noticias (2026/10/16)", "Tribuna (2026/10/16)", "Publimetro (2026/10/16)", "Crónica (2026/10/16)"], estatus="Parcialmente corroborado", arm="ARG-135-ARM-001", fecha_txt="no publicada; publicado el 2026-10-16",
  desl="No figura en las cinco ediciones previas ni en el índice. NO es ARG-134-016 (Laguna Colorada). Las notas republican un mismo comunicado: no son fuentes independientes"),
 dict(id="ARG-135-008", estado="MX-SIN", region="Noroeste", color="verde", impacto="pequeno", fecha="2026-10-16", hora="cateos no fechados; publicados el 2026-10-16",
  ent="Sinaloa", mun="Mazatlán (Mangle Marina y Golf) y Culiacán (El Carrizal)", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="SINALOA · MAZATLÁN Y CULIACÁN — CATEOS FEDERALES: UN DETENIDO, UN ARMA LARGA, OCHO VEHÍCULOS Y DROGA",
  hecho="Mazatlán · <code>RESIDENCIAL MANGLE MARINA Y GOLF</code> y Culiacán · <code>EL CARRIZAL</code> · cateos de Marina, SSPC y FGR, por cita en medios · publicado el VIERNES 16-OCT, por ruta · fecha de los cateos: no publicada · <b>1 detenido</b>, " + RES + " (🟢) · <b>1 arma larga</b>, " + RES + " · <code>CARTUCHOS SIN CIFRA: CUALITATIVO</code> · 8 vehículos y droga, " + RES + " · " + AP + " · " + FR,
  panel="Cateos: <b>1 detenido</b> y <b>1 arma larga</b>",
  inst="Gabinete de Seguridad <span class=\"muted-note\">(por cita)</span>", nac="El Diario de Chihuahua · diario.mx", conf="★★☆☆☆",
  campo="detenido y arma solo por resumen; fecha de los cateos no publicada", I=1, N=2, R=1, A=0,
  fechadas=["diario.mx (2026/oct/16)", "El Diario de Chihuahua (2026/oct/16)", "Línea Directa (2026-10-16)"], estatus="Pendiente de corroboración", arm="ARG-135-ARM-002", fecha_txt="no publicada; publicado el 2026-10-16",
  desl="Mangle Marina y El Carrizal no figuran en las cinco ediciones previas. NO es ARG-135-007 ni ARG-134-016"),
 dict(id="ARG-135-009", estado="MX-GRO", region="Sureste", color="verde", impacto="grande", fecha="2026-10-16", hora="no publicada",
  ent="Guerrero", mun="Ajuchitlán del Progreso (sierra; Puerto Grande o El Balcón)", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="GUERRERO · AJUCHITLÁN DEL PROGRESO — EJÉRCITO Y GUARDIA NACIONAL LOCALIZAN CON VIDA A SEIS CAMPESINOS PRIVADOS DE LA LIBERTAD; UNO SIGUE DESAPARECIDO",
  hecho="Ajuchitlán del Progreso · <code>SIERRA; PUERTO GRANDE O EL BALCÓN, VERSIONES DISTINTAS</code> · publicado el VIERNES 16-OCT, por ruta · <b>Defensa</b> y <b>Guardia Nacional</b> localizan con vida a <b>6 de 7 campesinos</b> desaparecidos desde el 24-sep, por titular (🟢) · buen estado de salud y traslado a la Fiscalía estatal, según Defensa, " + RES + " · <b>1 persona sigue sin localizar</b>, por titular · <code>ATRIBUCIÓN A UN GRUPO CRIMINAL: SOLO HABITANTES Y MEDIOS, NO SE INTEGRA</code> · ningún detenido publicado · identidades: no se reproducen · " + AP + " · " + FR,
  panel="<b>6 campesinos localizados con vida</b>; 1 sigue desaparecido",
  inst="Defensa <span class=\"muted-note\">(por cita)</span>", nac="El Heraldo de México · Proceso · Infobae · Tribuna · Quinto Poder", conf="★★★☆☆",
  campo="declaración de Defensa solo por resumen; hora no publicada", I=1, N=5, R=0, A=0,
  fechadas=["El Heraldo de México (2026/10/16)", "Proceso (2026/10/16)", "Tribuna (2026/10/16)", "Quinto Poder (2026/10/16)", "Infobae (2026/10/17)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no publicada; publicado el 2026-10-16",
  desl="Seguimiento de ARG-125-051 (privación de la libertad del 24-sep, 🔴 en su ventana): el rescate es un hecho distinto. Sin armamento"),
 dict(id="ARG-135-010", estado="MX-NAY", region="Occidente", color="verde", impacto="pequeno", fecha="2026-10-16", hora="detención no fechada; publicada el 2026-10-16",
  ent="Nayarit", mun="Tepic", dia="PUB. 16-OCT, HORA NO FIJADA",
  title="NAYARIT · TEPIC — CUMPLEN ORDEN DE APREHENSIÓN CONTRA UN POLICÍA ESTATAL POR LOS DISPAROS QUE MATARON A UN ADOLESCENTE",
  hecho="Tepic · publicado el VIERNES 16-OCT, por ruta · se cumple <b>orden de aprehensión</b> contra <b>1 policía estatal</b> por los disparos que mataron a un adolescente de 16 años durante una persecución del 3-oct, por titular (🟢) · comunicado del gobierno de Nayarit, " + RES + " · acusación, no condena · identidad: no se reproduce · " + AP + " · " + FR,
  panel="<b>1 policía estatal detenido</b> por la muerte de un adolescente",
  inst="Gobierno de Nayarit <span class=\"muted-note\">(comunicado por cita)</span>", nac="Infobae", conf="★★☆☆☆",
  campo="una sola fuente; fecha de la detención no publicada", I=1, N=1, R=0, A=0,
  fechadas=["Infobae (2026/10/16)"], estatus="Pendiente de corroboración", arm=None, fecha_txt="no publicada; publicada el 2026-10-16",
  desl="El homicidio del 3-oct no figura en las ediciones de su ventana ni en el índice. Servidor público como imputado, no como víctima. Sin armamento"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-135-REC-001", estado="MX-NLE", region="Noreste", fecha="2026-10-15", hora="noche (solo por resumen)", orig="ARGOS 134 (133 SI FUE LA NOCHE DEL MIÉRCOLES 14) — DÍA CONTRADICHO", col_orig="rojo",
  ent="Nuevo León", mun="Linares (col. Provileón)", dia="15-OCT, NOCHE",
  title="NUEVO LEÓN · LINARES — ATAQUE ARMADO FRENTE A UN DEPÓSITO DE LA COLONIA PROVILEÓN: DOS HOMBRES MUERTOS Y UNO HERIDO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 134 —133 SI FUE LA NOCHE DEL MIÉRCOLES 14— DÍA CONTRADICHO</code> · <code>COL. PROVILEÓN, DEPÓSITO EN EL CRUCE DE AV. NOGAL Y OCOTE</code> · noche del JUEVES 15-OCT según la Fiscalía, " + RES + "; «miércoles» en otros medios · disparos desde un vehículo, " + RES + " · <b>2 hombres muertos</b> —uno en el lugar y otro en el hospital— y <b>1 herido</b>, por titular (🔴 en su ventana) · la <b>Fiscalía de Nuevo León</b> identificó a las víctimas, por cita · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>2 muertos y 1 herido</b>", inst="FGJ Nuevo León <span class=\"muted-note\">(por cita)</span>", nac="MVS · Milenio",
  conf="★★★☆☆", campo="día contradicho (14 o 15); hora solo por resumen", I=1, N=2, R=4, A=0,
  fechadas=["El Mañana (2026/10/15)", "MVS Noticias (2026/10/16)", "Punto x Punto (2026/10/16)", "Enfoque Monterrey (2026/10/17)"],
  desl="Linares y Provileón no figuran en las cinco ediciones previas ni en el índice. 🔴 en su ventana por homicidio múltiple"),
 dict(id="ARG-135-REC-002", estado="MX-HID", region="Centro", fecha="2026-10-12", hora="~19:40 (solo por resumen)", orig="ARGOS 131 — HORA NO FIJADA", col_orig="rojo",
  ent="Hidalgo", mun="Tezontepec de Aldama (San Gabriel)", dia="12-OCT, NOCHE",
  title="HIDALGO · TEZONTEPEC DE ALDAMA — EJECUTAN A UN AUTOMOVILISTA EN SAN GABRIEL Y DISPARAN CONTRA LOS POLICÍAS MUNICIPALES QUE ACUDEN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131 — HORA NO FIJADA</code> · <code>SAN GABRIEL</code> · LUNES 12-OCT, ~19:40, " + RES + " · <b>1 automovilista muerto</b> a tiros dentro de su auto, por titular · civiles armados <b>disparan contra los policías municipales</b> que llegan al reporte, por titular; intercambio de disparos y persecución; los agresores huyen a pie, " + RES + " (🔴 en su ventana) · patrulla dañada; <b>ningún policía herido</b> y <b>ningún detenido</b>, " + RES + " · peritos de la PGJEH en la escena, " + RES,
  panel="<b>1 automovilista asesinado</b>; disparos contra policías municipales", inst=SB, nac=NIN,
  conf="★★☆☆☆", campo="hora solo por resumen; una sola fuente con fecha en la ruta", I=0, N=0, R=4, A=0,
  fechadas=["La Silla Rota (2026/10/13)"],
  desl="Tezontepec no figura en las cinco ediciones previas ni en el índice. NO es la balacera de Tula del 11-oct (🟡, ventana de 130, no recuperable). 🔴 en su ventana por ataque contra autoridades"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-135-ARM-001", ficha="ARG-135-007", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Culiacán", c=[3,1,0,0,417,16,0,0,0,4],
  corp="Gabinete de Seguridad (por cita)", conf="Medio", color="verde", fecha="2026-10-16", hora="operativo no fechado",
  fecha_txt="no publicada<br><span class=\"muted-note\">publicado 16-oct · FRONTERA DE VENTANA</span>",
  nota="ametralladora y 417 cartuchos por titular; 3 cortas y 16 cargadores solo por resumen · ametralladora sin especificar: se integra como arma larga por la taxonomía; si la autoridad la clasifica como pesada, pasa a especial · 4 detenidos por titular",
  fuentes=["Infobae (2026/10/16)", "MVS Noticias (2026/10/16)", "Tribuna (2026/10/16)"]),
 dict(id="ARG-135-ARM-002", ficha="ARG-135-008", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Mazatlán y Culiacán", c=[0,1,0,0,0,0,0,0,0,1],
  corp="Marina · SSPC · FGR (por cita)", conf="Bajo", color="verde", fecha="2026-10-16", hora="cateos no fechados",
  fecha_txt="no publicada<br><span class=\"muted-note\">publicado 16-oct · FRONTERA DE VENTANA</span>",
  nota="1 arma larga y 1 detenido solo por resumen · cartuchos sin cifra: cualitativo",
  fuentes=["diario.mx (2026/oct/16)", "El Diario de Chihuahua (2026/oct/16)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
assert TOT == [3, 2, 0, 0, 417, 16, 0, 0, 0, 5], TOT
assert cnt == {"rojo": 3, "amarillo": 3, "verde": 4}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 0, "verde": 0}, cnt_rec
assert len(ENT) == 6, ENT
assert NFR == 8, NFR

def fmt(n): return f"{n:,}"

def ficha(e, rec=False):
    cls, lab = FLAG[e["color"]]
    op = ' style="opacity:.72;"' if rec else ""
    nivel = ESTR[e["conf"]]
    fech = " · ".join(f"<b>{x}</b>" for x in e["fechadas"]) if e["fechadas"] else "<span class=\"muted-note\">ninguna con fecha en la ruta</span>"
    if rec:
        armtxt = "<b>Ventana de origen</b>: " + e["orig"] + " — <b>fuera de todos los totales</b>"
    else:
        armtxt = "<b>Conteo de armamento</b>: " + (e["armtxt"] if e.get("armtxt") else f'<a href="#{e["arm"]}"><code>{e["arm"]}</code></a>' if e["arm"] else ("sin fila — evento cualitativo, cantidad no determinada" if e.get("cual") else "sin fila — no hubo armamento asegurado"))
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
head = head.replace("<title>ARGOS 134 — Reporte Nacional de Seguridad — 2026-10-16</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE BAJA CALIFORNIA EL DICTAMEN BALÍSTICO DE LOS CASQUILLOS</b> (ARG-135-002).
      <br><b>2. SOLICITE A LA FISCALÍA DE MICHOACÁN LA IDENTIFICACIÓN DE LAS VÍCTIMAS Y LA HORA DEL HALLAZGO</b> (ARG-135-003).
      <br><b>3. SOLICITE A LA FISCALÍA DE GUERRERO LA SITUACIÓN DE LA PERSONA AÚN NO LOCALIZADA</b> (ARG-135-009).
      <br><b>4. SOLICITE A LA FISCALÍA DE NAYARIT LA SITUACIÓN JURÍDICA DEL AGENTE DETENIDO</b> (ARG-135-010).
      <br><b>5. SOLICITE A LA FISCALÍA DE NUEVO LEÓN EL DÍA DEL ATAQUE</b> (ARG-135-REC-001).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>16-oct 11:34 → 17-oct 09:28 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,46 hechos/hora</b>; duración y densidad, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>. <b>Ocho de diez</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <b>Armamento</b>: <b>2 eventos integrados</b>, los dos en Sinaloa (ARG-135-ARM-001, confianza Medio; ARG-135-ARM-002, confianza Bajo). <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento de armamento</b>; el de ARG-135-010 no entra. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios</b>: <b>10</b> —Culiacán 2, Tijuana 2, Apatzingán 3 + 1 y Hermosillo 1 + 1—. <b>Heridos: 0</b> integrados. <b>Personas localizadas con vida: 6</b> (ARG-135-009). <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: ARG-134-013, un adolescente herido leve por esquirla, solo por resumen (Línea Directa 2026-10-15) · ARG-134-005, «en su día de descanso» en la mayoría de los medios · ARG-133-001, sexo de los cinco cuerpos según la PGJEH: 2 mujeres y 3 hombres, por cita.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:6])
co3 = "\n".join(ficha(e) for e in E[6:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "Culiacán · <b>solo por resumen</b>"),
 tile(1, "Armas largas", TOT[1], "Culiacán (ametralladora) y Mazatlán/Culiacán"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CATEGORÍA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "Culiacán · <b>por titular</b>"),
 tile(4, "Cargadores", TOT[5], "Culiacán · <b>solo por resumen</b>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA EN HECHO PROPIO</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code>"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>Dos filas de armamento en la ventana</b>, las dos en Sinaloa. <b>Total nacional del corte</b>: en la página de panorama.
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
    <b>Lectura regional</b> —2 filas, <b>cálculo propio</b>—: <b>Noroeste 2</b> · <b>Noreste 0</b> · <b>Occidente 0</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    <br><code>VISTOS, NO INTEGRADOS</code>: Estado de México, Marina y FGR, 7 detenidos y armas en dos puntos (publicación del 17 solo por resumen; desgloses contradictorios: <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: boletín federal de las <b>acciones del 15-oct</b>, publicado el 16-oct: Baja California, Colima, Chihuahua, Guerrero, Jalisco, Querétaro, Quintana Roo, Sinaloa y Sonora. <code>CANTIDADES SOLO POR RESUMEN, SIN FRAGMENTO: NO SE PUBLICAN</code>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas, abajo, no se integran</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>18 estatales revisadas</b> · 14 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Baja California</b><br>Ensenada</td><td>Tres sentenciados, nombres no reproducidos · <span class="muted-note">homicidio calificado de tres surfistas, robo calificado y robo de vehículo con violencia; fecha de la sentencia (16-oct) solo por resumen</span></td><td><b>158 años 9 meses</b> a cada uno, por titular · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>FGE Baja California <span class="muted-note">(por titulares de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Infobae 2026/10/17 · crprensa 2026/10/17 · boletín no localizado · <code>FRONTERA DE VENTANA — HORA NO FIJADA</code></td><td>Bajo</td></tr>
      <tr><td><b>Sonora</b><br>Hermosillo</td><td>Un sentenciado, nombre no reproducido · <span class="muted-note">homicidio calificado; fecha de la sentencia no publicada</span></td><td><b>25 años</b>, por titular</td><td>Fiscalía de Sonora <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · Tribuna 2026/10/16 (hora no fijada) · fuente única · boletín no localizado</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Veracruz, 21 años por el homicidio de un periodista (15-oct, sin boletín) · FGR Cosoleacaque, 4 años (15-oct) · FGR Banderilla, 2 años 6 meses (15-oct) · Ciudad de México, dos sentenciados por homicidios en la col. Morelos (14-oct) · Nuevo León, 155 años (13-oct) · Oaxaca FGEO, 80 años (13-oct) · Colima FGE, 27 años por secuestro (9-oct, solo por resumen) · Querétaro, tres boletines del 5, 6 y 8-oct · Tamaulipas FGJE-370-2026 (6-oct).
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>18 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · BCS, Dgo · NL, Tamps, SLP, Zac · Jal, Col, Gto · Edomex, Mor, Pue, Qro · Ver, Tab · Oax, Chis, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0 por boletín leído</b> · candidatas solo por medios: Baja California, Sonora</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>18</b> fiscalías estatales · <b>sin boletín indexado, no «sin sentencias»</b></td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>14</b>: BC, Son, Chih, Sin · Coah · Mich, Nay, Ags · CDMX, Tlax, Hgo · Gro, Camp, Yuc</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 20 de 32 con consulta propia por entidad</b> · <b>11 solo por consulta regional amplia</b>: Dgo · Coah, SLP · Jal, Col, Nay · CDMX, Mor, Tlax · Camp, Yuc · <code>NO REVISADA</code>: BCS · <b>armamento: 11 de 32</b> —Chih · Coah, Tamps, Zac · Col, Nay, Ags · Ver, Tab · Oax, Yuc—; <code>NO REVISADA</code>: BC, BCS, Son, Sin, Dgo · NL, SLP · Jal, Mich, Gto · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Gro, Chis, Camp, QRoo (Sinaloa: hechos por medios, sin dominio oficial) · <code>REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 15-oct</b>: existe, publicado el 16-oct (Milenio y republicadores) · <b>acciones del 16-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta · <b>Defensa, Marina, Guardia Nacional y FGR</b>: SRIV · <b>gabinetedeseguridad.gob.mx</b>: <code>NO REVISADA</code>, dominio no devuelto</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 17-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR TRES ROJOS</b>: ARG-135-001 a ARG-135-003 · <b>reserva</b> en ARG-135-003.
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-135-004 a ARG-135-006.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-135-007 a ARG-135-010.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-135-REC-001 y ARG-135-REC-002.
      <br><b>5.</b> <code>21 H 54 MIN; OCHO DE DIEZ HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. CULIACÁN, ATAQUE CON ARMA LARGA EN ZONA RESIDENCIAL.</b> ARG-135-001, a plena tarde; tipo de arma solo por resumen. Línea: <b>solicitar a la FGE Sinaloa el cotejo de los casquillos</b> con hechos previos del sector — hipótesis.
      <br><b>2. SINALOA, ABASTECIMIENTO Y MANTENIMIENTO DE ARMAMENTO.</b> ARG-135-007 y ARG-135-008, tras ARG-134-016: tres operativos federales en dos días. Línea: <b>solicitar a la FGR el rastreo de origen de la ametralladora</b> — requiere validación.
      <br><b>3. APATZINGÁN, AGRESIÓN DENTRO DE VIVIENDAS.</b> ARG-135-004 y ARG-134-REC-003, con víctimas menores o frente a menores. Línea: <b>solicitar a la FGE Michoacán si las carpetas comparten indicios</b> — vínculo no acreditado.
      <br><b>4. HERMOSILLO, ZONA SUR.</b> ARG-135-005, ARG-135-006 y ARG-134-012 en dos días. Línea: <b>solicitar a la Fiscalía de Sonora el cotejo balístico</b> — hipótesis.
      <br><b>5. POLICÍAS MUNICIPALES AGREDIDOS AL ACUDIR A UN REPORTE.</b> ARG-135-REC-002. Línea: <b>solicitar a la PGJ Hidalgo el peritaje de la patrulla</b> — sin heridos ni detenidos publicados.
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
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: CULIACÁN, TIJUANA Y APATZINGÁN", co1)
 + page("CRIMEN ORGANIZADO (II) — VIOLENCIA OPERATIVA", co2)
 + page("CRIMEN ORGANIZADO (III) — ACCIONES INSTITUCIONALES", co3)
 + page("CRIMEN ORGANIZADO (IV) — RECUPERACIONES: VENTANAS DE ARGOS 131 Y 134", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 16-oct 11:34 → 17-oct 09:28 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR)
