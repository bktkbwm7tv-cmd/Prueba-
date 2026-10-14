# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 132: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-131.py <plantilla ARGOS 131> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "132", "2026-10-14", "08:19"
CONSULTA = "2026-10-14 08:19-11:30"
DUR = "24 h 56 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-132-001", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-13", hora="mañana (solo por resumen)",
  ent="Sinaloa", mun="Navolato (Campo Romero, Villa Juárez)", dia="PUB. 13-OCT, HORA NO FIJADA",
  title="SINALOA · NAVOLATO — COLECTIVOS DE BÚSQUEDA HALLAN UNA FOSA CLANDESTINA EN CAMPO ROMERO: TRES CUERPOS",
  hecho="Navolato · <code>PREDIO AGRÍCOLA CERCA DE CAMPO ROMERO, SINDICATURA DE VILLA JUÁREZ</code> · publicado el MARTES 13-OCT; hallazgo por la mañana, " + RES + " · <b>colectivos de búsqueda</b> localizan una <b>fosa clandestina</b>, por titular (🔴) · <b>3 cuerpos</b>, por titular · <b>FGE Sinaloa: restos de 3 personas</b>, por titular de un medio · <code>COLECTIVOS ESTIMAN «ALREDEDOR DE CINCO», SOLO POR RESUMEN; EL PRIMER REPORTE DIO 1</code> · aviso por llamada anónima y maquinaria de la Comisión Estatal de Búsqueda, " + RES + " · restos sin identificar; temporalidad no publicada · " + FR,
  panel="<b>Fosa clandestina</b>: <b>3 cuerpos</b>",
  inst="FGE Sinaloa <span class=\"muted-note\">(por titular de medios)</span>", nac="El Universal · N+", conf="★★★☆☆",
  campo="hora solo por resumen; cifra de la FGE por titular de un medio, sin boletín", I=1, N=2, R=8, A=0,
  fechadas=["Diario de Yucatán (2026/10/13, réplica de El Universal)", "Revista Espejo (2026/10/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="Campo Romero no figura en el índice ni en las tres ediciones previas; Villa Juárez aparece solo por una sentencia (Manuel Antonio «N»), otro caso. NO son los hallazgos de Villa Juárez de julio (Proceso 2026/7/23). Cuerpos, no víctimas identificadas. 🔴 por hallazgo de fosa clandestina"),
 dict(id="ARG-132-002", estado="MX-VER", region="Golfo", color="amarillo", impacto="mediano", fecha="2026-10-13", hora="noche, ~19:30–20:00 (solo por resumen)",
  ent="Veracruz", mun="Orizaba (col. El Espinal Bajo)", dia="13-OCT, NOCHE",
  title="VERACRUZ · ORIZABA — RECIBEN A TIROS UN CATEO DE LA POLICÍA MINISTERIAL: TRES AGENTES HERIDOS, UN MUERTO Y DOS PERSONAS RESCATADAS",
  hecho="Orizaba · <code>COL. EL ESPINAL BAJO, AV. DE LA FUENTE ENTRE GÓMEZ FARÍAS Y 5 DE MAYO — SOLO POR RESUMEN</code> · noche del MARTES 13-OCT, ~19:30–20:00 —día y hora " + RES + "— · la <b>Policía Ministerial</b>, con apoyo estatal y federal, ejecuta un <b>cateo</b> y es <b>repelida a tiros</b>, por titular (🟡) · <b>3 policías ministeriales heridos</b>, por titular; uno grave, " + RES + " · <b>1 persona muerta</b>, por titular · <code>IDENTIDAD DEL MUERTO NO DETERMINADA: «UN CIVIL» POR TITULAR DE UN SOLO MEDIO; SI FUERA PERSONAL O VÍCTIMA AJENA, SUBE A 🔴</code> · <b>2 personas presuntamente privadas de la libertad, rescatadas</b>, por titular · <b>ningún detenido publicado</b> · armamento asegurado: no publicado · " + FR,
  panel="Cateo repelido: <b>3 ministeriales heridos</b>, <b>1 muerto</b> y <b>2 personas rescatadas</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="La Silla Rota", conf="★★★☆☆",
  campo="día, hora e identidad del muerto no fijados; sin boletín institucional", I=0, N=1, R=7, A=0,
  fechadas=["La Silla Rota (2026/10/13)", "Golpe Político (2026/10/13, dos notas)"], estatus="Parcialmente corroborado", arm=None, cual=True,
  desl="Orizaba no figura en el índice ni en las tres ediciones previas (solo la carretera Puebla–Orizaba); «cinco presuntos secuestradores muertos en Orizaba» (El Universal) es de 2025. 🟡 por confrontación derivada de un operativo. El rescate es resultado del mismo cateo: no se abre ficha verde aparte"),
 dict(id="ARG-132-003", estado="MX-OAX", region="Sureste", color="amarillo", impacto="mediano", fecha="2026-10-13", hora="mañana, antes de las 10:45 (solo por resumen)",
  ent="Oaxaca", mun="San Blas Atempa (Secundaria Técnica 69)", dia="13-OCT, MAÑANA",
  title="OAXACA · SAN BLAS ATEMPA — HOMBRES ARMADOS ENTRAN A UNA SECUNDARIA Y ASESINAN A UN PROFESOR FRENTE A LOS ALUMNOS",
  hecho="San Blas Atempa · <code>ESCUELA SECUNDARIA TÉCNICA N.° 69</code> · mañana del MARTES 13-OCT, al inicio de clases (" + RES + ") · hombres armados entran al plantel y disparan contra un <b>profesor</b> frente a alumnos, por titular · <b>1 muerto</b>, por titular (🟡) · <code>HOSPITAL CONTRADICHO: ISSSTE DE TEHUANTEPEC O SALINA CRUZ</code> · coordinador académico y exrepresentante seccional de la Sección 22, " + RES + " · <b>FGEO</b>: carpeta por homicidio calificado y despliegue de la Agencia Estatal de Investigaciones, " + RES + " · <b>ningún detenido publicado</b> · móvil no publicado · identidad: no se reproduce · " + FR,
  panel="<b>Profesor asesinado</b> dentro de una secundaria",
  inst="FGEO <span class=\"muted-note\">(por cita)</span>", nac="El Financiero · Infobae · La Jornada · La Silla Rota · Aristegui", conf="★★★☆☆",
  campo="hora solo por resumen; sin boletín institucional", I=1, N=5, R=6, A=0,
  fechadas=["El Financiero (2026/10/13)", "Infobae (2026/10/13)", "La Jornada (2026/10/13)", "La Silla Rota (2026/10/13)", "El Informador (20261013)", "Proyecto Puente (2026/10/13)", "Tribuna (2026/10/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Blas Atempa no figura en el índice ni en las tres ediciones previas; el boletín FGEO 2,685 (5-ago) es otro caso. <code>SI OCURRIÓ ANTES DE LAS 07:23 DEL 13-OCT, SU VENTANA ES LA DE ARGOS 131</code>. Uniformes que simulaban ser de la Fiscalía: un solo medio, no se integra. Vínculo con las agresiones del Istmo: no acreditado. 🟡 por homicidio doloso único"),
 dict(id="ARG-132-004", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-13", hora="mañana (solo por resumen)",
  ent="Estado de México", mun="Naucalpan (col. La Mancha 1)", dia="13-OCT, MAÑANA",
  title="ESTADO DE MÉXICO · NAUCALPAN — DESDE UNA MOTOCICLETA ASESINAN A BALAZOS A UNA MUJER QUE CONDUCÍA SU VEHÍCULO",
  hecho="Naucalpan · <code>COL. LA MANCHA 1, AV. MOLINOS DE VIENTO — SOLO POR RESUMEN</code> · mañana del MARTES 13-OCT (" + RES + ") · agresores en motocicleta disparan contra una mujer que conducía, por titular · <b>1 mujer asesinada</b>, por titular (🟡) · al menos 2 impactos, " + RES + " · <code>VEHÍCULO CONTRADICHO: CAMIONETA O AUTOMÓVIL</code> · <b>FGJEM</b> investiga, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 mujer asesinada</b> dentro de su vehículo",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Heraldo de México · El Universal", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=2, R=3, A=0,
  fechadas=["El Heraldo de México (2026/10/13)", "Cúspide México (2026/10/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="La Mancha no figura en el índice; NO es ARG-128-005 (Valle Dorado) ni ARG-128-006 (Minas Palacio). <code>SI OCURRIÓ ANTES DE LAS 07:23 DEL 13-OCT, SU VENTANA ES LA DE ARGOS 131</code>. 🟡 por homicidio doloso único"),
 dict(id="ARG-132-005", estado="MX-MIC", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-10-13", hora="no fijada: 12-oct ~12:00 o 13-oct (solo por resumen, contradicho)",
  ent="Michoacán", mun="Cotija (El Metidero)", dia="PUB. 13-OCT, HECHO 12 O 13-OCT",
  title="MICHOACÁN · COTIJA — EL EJÉRCITO ABATE A TRES HOMBRES ARMADOS EN UN ENFRENTAMIENTO EN EL METIDERO",
  hecho="Cotija · <code>EL METIDERO, HUERTA LA HACIENDA — SOLO POR RESUMEN</code> · publicado el MARTES 13-OCT · <code>FECHA DEL HECHO CONTRADICHA: LUNES 12 AL MEDIODÍA O MARTES 13, SOLO POR RESUMEN</code> · enfrentamiento entre el <b>Ejército</b> y hombres armados, por titular · <b>3 agresores abatidos</b>, por titular (🟡) · <code>QUIÉN INICIÓ: SOLO LA VERSIÓN MILITAR, SOLO POR RESUMEN — PERSONAL EN RECONOCIMIENTO RECIBE DISPAROS; SI SE ACREDITA, SUBE A 🔴</code> · 3 fusiles AK-47 asegurados, " + RES + " · <b>ningún detenido publicado</b> · sin comunicado de la Defensa · " + FR,
  panel="Enfrentamiento: <b>3 agresores abatidos</b> por el Ejército",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="fecha, hora e iniciador solo por resumen; los medios con fecha replican el mismo titular", I=0, N=0, R=8, A=1,
  fechadas=["Grupo Marmor (2026/10/13)", "Red Michoacán (2026/10/13)"], estatus="Parcialmente corroborado", arm=None, cual=True, fecha_txt="no fijada (12 o 13-oct); publicado el 2026-10-13",
  desl="Cotija figura solo en el agregado federal del 9 al 11-oct (otra acción). <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>: el boletín federal del 12-oct da 4 largas, 4 cargadores, 45 cartuchos y 122 AEI en Plan del Cerro, Cotija, solo por resumen. Blog del Narco: NO OFICIAL. Si ocurrió el 12-oct, su ventana es la de ARGOS 131. 🟡: el iniciador no está acreditado"),
 dict(id="ARG-132-006", estado="MX-JAL", region="Occidente", color="verde", impacto="grande", fecha="2026-10-14", hora="no publicada",
  ent="Jalisco", mun="Guadalajara", dia="ANUNCIO 14-OCT, HECHO NO FIJADO",
  title="JALISCO · GUADALAJARA — LA MARINA DETIENE AL SEÑALADO LÍDER DE «LOS CROMOS», CÉLULA DEL CJNG QUE OPERA EN OAXACA",
  hecho="Guadalajara · <b>anunciada el MIÉRCOLES 14-OCT por el titular de la SSPC</b>, por titular · <code>FECHA DE LA CAPTURA NO PUBLICADA</code> · <b>Semar</b>, por titular; CNI, " + RES + " · detención de Iván «N», «El Cromo», señalado líder de <b>Los Cromos</b>, <b>célula del CJNG en Oaxaca</b>, por titular · <b>1 detenido</b> (🟢) · <b>recompensa de 2 millones de pesos</b>, por titular · <code>ÓRDENES DE APREHENSIÓN POR HOMICIDIO: 2 (EL UNIVERSAL) O 3 (EL IMPARCIAL), POR TITULAR, CONTRADICHO</code> · acusaciones, no condena · sin armamento publicado · " + FR,
  panel="Detenido el señalado líder de <b>Los Cromos</b>",
  inst="SSPC <span class=\"muted-note\">(anuncio, por titular de medios)</span>", nac="Infobae · La Razón · La Silla Rota · El Heraldo de México · El Universal", conf="★★★☆☆",
  campo="fecha de la captura no publicada; anuncio sin boletín leído", I=1, N=5, R=1, A=0,
  fechadas=["Infobae (2026/10/14)", "La Razón (2026/10/14)", "La Silla Rota (2026/10/14)", "El Heraldo de México (2026/10/14)", "El Imparcial (2026/10/14)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no publicada; anunciada el 2026-10-14",
  desl="«El Cromo» y Los Cromos no figuran en el índice ni en las ediciones previas. Vínculo con ARG-132-003: no acreditado. Si la captura fue anterior a las 07:23 del 13-oct, es evento anterior publicado durante el corte y sale de los totales. Sin armamento: fuera del conteo"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-132-REC-001", estado="MX-PUE", region="Centro", fecha="2026-10-12", hora="noche (solo por resumen)", orig="ARGOS 131", col_orig="amarillo",
  ent="Puebla", mun="Tehuacán (San Marcos Necoxtla)", dia="12-OCT, NOCHE",
  title="PUEBLA · TEHUACÁN — ASESINAN A BALAZOS A UN HOMBRE EN UNA TIENDA DE SAN MARCOS NECOXTLA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131</code> · <code>SAN MARCOS NECOXTLA, TIENDA — «DENTRO» O «FRENTE A», CONTRADICHO</code> · noche del LUNES 12-OCT (" + RES + ") · agresores huyen en un automóvil y una motocicleta, " + RES + " · <b>1 hombre asesinado</b>, por titular (🟡 en su ventana) · <b>FGE Puebla</b>: carpeta por homicidio calificado, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>1 hombre asesinado</b> en una tienda", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="N+",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=1, R=8, A=0,
  fechadas=["Síntesis (2026/10/13)", "Reto Diario (2026/10/13)", "Intolerancia (2026/10/13)"],
  desl="Necoxtla no figura en el índice. ARGOS 131 lo vio y no lo fichó por falta de URL con fecha: <b>recuperación por anclaje posterior</b>, no omisión. Nombre y edad discrepan entre medios"),
 dict(id="ARG-132-REC-002", estado="MX-SIN", region="Noroeste", fecha="2026-10-12", hora="tarde, aviso ~12:15 (solo por resumen)", orig="ARGOS 131", col_orig="amarillo",
  ent="Sinaloa", mun="Mazatlán (Villa Unión, col. Toledo Corro)", dia="12-OCT, TARDE",
  title="SINALOA · MAZATLÁN — ATACAN A BALAZOS UNA ESTÉTICA EN VILLA UNIÓN: UN HOMBRE MUERTO Y UNA MUJER HERIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131</code> · <code>VILLA UNIÓN, COL. TOLEDO CORRO, ESTÉTICA</code> · LUNES 12-OCT, por la tarde (" + RES + ") · ataque armado · <b>1 hombre muerto y 1 mujer herida</b>, por titular (🟡 en su ventana) · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque a una estética: <b>1 muerto</b> y <b>1 herida</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-10-12)", "Línea Directa (2026-10-12)"],
  desl="Toledo Corro no figura en el índice. NO es la llantera de Villa Unión (1-oct, Línea Directa 2026-10-01) ni la mujer asesinada en Villa Unión que ARGOS 131 dejó sin URL con fecha (11-oct, una mujer muerta; aquí 12-oct, hombre muerto y mujer herida), ni ARG-131-004 (estética de Escuinapa)"),
 dict(id="ARG-132-REC-003", estado="MX-NLE", region="Noreste", fecha="2026-10-12", hora="~16:00 (solo por resumen)", orig="ARGOS 131 (130 si fue antes de las 08:19) — HORA NO FIJADA", col_orig="rojo",
  ent="Nuevo León", mun="Doctor Coss", dia="12-OCT, TARDE",
  title="NUEVO LEÓN · DOCTOR COSS — FUERZA CIVIL REPELE UN ATAQUE AL ACTIVAR EL OPERATIVO MURALLA Y ABATE A DOS HOMBRES ARMADOS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131 —130 SI FUE ANTES DE LAS 08:19— HORA NO FIJADA</code> · LUNES 12-OCT, ~16:00 (" + RES + ") · civiles armados disparan contra el patrullaje de <b>Fuerza Civil</b> (Operativo Muralla), por titular («Repelen ataque…», versión de la autoridad) (🔴 en su ventana) · <b>2 agresores abatidos</b>, por titular · <b>2 armas largas aseguradas</b>, por <i>slug</i> · ningún agente herido y otros agresores en fuga, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Ataque a patrullaje: <b>2 agresores abatidos</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="MVS · El Universal",
  conf="★★★☆☆", campo="hora solo por resumen; iniciador según la sola versión de la autoridad", I=0, N=2, R=2, A=0,
  fechadas=["MVS Noticias (2026/10/12)"],
  desl="<code>NO ES EL HECHO DEL 22-AGO-2025</code> (12 abatidos, mismo municipio): trampa de año. Doctor Coss no figura en el índice de 2026. 🔴 en su ventana por ataque a personal en patrullaje"),
 dict(id="ARG-132-REC-004", estado="MX-NAY", region="Occidente", fecha="2026-10-11", hora="no publicada", orig="ARGOS 129 o ARGOS 130 — HORA NO FIJADA", col_orig="rojo",
  ent="Nayarit", mun="Acaponeta (carretera Tepic–Mazatlán)", dia="11-OCT, HORA NO FIJADA",
  title="NAYARIT · ACAPONETA — HALLAN TRES CUERPOS ENVUELTOS EN COBIJAS JUNTO A LA CARRETERA TEPIC–MAZATLÁN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 129 O ARGOS 130 — HORA NO FIJADA</code> · <code>KM 112+600, ACCESO A LAS GUÁSIMAS — KILÓMETRO CONTRADICHO (111), SOLO POR RESUMEN</code> · DOMINGO 11-OCT · hallazgo de <b>3 cuerpos envueltos en cobijas</b>, por titular (🔴 en su ventana) · cartulinas con mensajes, contenido no publicado, " + RES + " · causa de muerte e identidades: no publicadas · <b>FGE Nayarit sin comunicado</b>, " + RES,
  panel="Hallazgo de <b>3 cuerpos</b> junto a la carretera", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora no fijada; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["NTV (2026/10/11)", "Nayarit Noticias (2026/10/11)"],
  desl="NO es el hallazgo de La Higuerita, km 126 (9-sep, La Prensa de Coahuila 2026/09/10) ni ARG-115-ARM-004 (agregado de aseguramientos, sin víctimas). ARGOS 131 lo dejó como candidato sin URL con fecha; NTV y Nayarit Noticias lo anclan al 11-oct. Si fue antes de las 08:58 del 11-oct, su ventana es la de ARGOS 129. 🔴 por homicidio múltiple"),
 dict(id="ARG-132-REC-005", estado="MX-SIN", region="Noroeste", fecha="2026-10-12", hora="no publicada", orig="ARGOS 130 o ARGOS 131 — HORA NO FIJADA", col_orig="verde",
  ent="Sinaloa", mun="Escuinapa (col. Pueblo Nuevo)", dia="PUB. 12-OCT, HORA NO FIJADA",
  title="SINALOA · ESCUINAPA — UNA PERSECUCIÓN EN PUEBLO NUEVO TERMINA CON TRES DETENIDOS Y ARMAS 9 MM ASEGURADAS",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 130 O ARGOS 131 — HORA NO FIJADA</code> · <code>COL. PUEBLO NUEVO</code> · publicado el LUNES 12-OCT · <b>Grupo Interinstitucional</b> —policía municipal y Ejército—, por la SSP Sinaloa · persecución, por titular · <b>3 detenidos</b>, por titular (🟢 en su ventana) · armas calibre 9 mm y motocicletas robadas, por titular; <b>2 armas cortas, 2 cargadores y 18 cartuchos</b>, " + RES + " · sin disparos publicados",
  panel="Persecución: <b>3 detenidos</b> y armas 9 mm", inst="SSP Sinaloa <span class=\"muted-note\">(<i>slug</i> indexado, sin fecha)</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★☆☆☆", campo="desglose solo por resumen", I=1, N=0, R=3, A=0,
  fechadas=["Línea Directa (2026-10-12)", "Tus Buenas Noticias (2026/10/13)"],
  desl="Pueblo Nuevo no figura en el índice; NO es ARG-124-006 (22-sep, GN, 9 largas), ni ARG-131-004 (estética del centro), ni el homicidio del taller de motocicletas de Pueblo Nuevo (18-sep). Armamento de ventana anterior: fuera del conteo"),
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
assert cnt == {"rojo": 1, "amarillo": 4, "verde": 1}, cnt
assert cnt_rec == {"rojo": 2, "amarillo": 2, "verde": 1}, cnt_rec
assert len(ENT) == 6, ENT

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
head = head.replace("<title>ARGOS 131 — Reporte Nacional de Seguridad — 2026-10-13</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE SINALOA LA CIFRA OFICIAL Y LA IDENTIFICACIÓN DE LOS RESTOS DE LA FOSA DE CAMPO ROMERO</b> (ARG-132-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE VERACRUZ LA IDENTIDAD DEL FALLECIDO Y EL PARTE DEL CATEO DE ORIZABA</b> (ARG-132-002).
      <br><b>3. SOLICITE A LA FGEO EL MÓVIL DEL ATAQUE EN LA SECUNDARIA DE SAN BLAS ATEMPA</b> (ARG-132-003).
      <br><b>4. SOLICITE A LA FISCALÍA DE MORELOS EL PARTE DE LA RETENCIÓN DE TOTOLAPAN Y LA SITUACIÓN DEL LIBERADO</b> (ARG-131-002).
      <br><b>5. SOLICITE A LA FISCALÍA DE NAYARIT EL COMUNICADO DEL HALLAZGO DE ACAPONETA</b> (ARG-132-REC-004).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>13-oct 07:23 → 14-oct 08:19 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,24 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: rojos, amarillos, verdes</b>. <b>Los seis</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <b>Ningún aseguramiento de armamento con cifra integrable en hechos propios</b>. <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento de armamento</b>; el de ARG-132-006, sin armas, no entra. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios</b>: <b>3</b> por agresión —Orizaba, San Blas Atempa y Naucalpan—, <b>3 agresores abatidos</b> en Cotija y <b>3 cuerpos</b> en la fosa de Navolato. <b>Heridos: 3</b> policías ministeriales. <b>Rescatados: 2</b>. <b>Cálculo propio</b>.
  </p>
'''

co1 = "\n".join(ficha(e) for e in E[:3])
co2 = "\n".join(ficha(e) for e in E[3:])
rec1 = "\n".join(ficha(r, True) for r in R)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
tiles = "\n".join([
 tile(0, "Armas cortas", TOT[0], "<code>NINGUNA ARMA CORTA CON CIFRA EN HECHO PROPIO</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA INTEGRABLE</code> · Cotija, posible duplicidad"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR INTEGRADA</code>"),
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
    <b>Lectura regional</b>: <b>0 filas</b> en las seis regiones. <b>Eventos cualitativos</b>: ARG-132-002 (cateo de Orizaba, armamento no publicado) · ARG-132-005 (Cotija, 3 AK-47 solo por resumen: <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> con las 4 largas de Plan del Cerro).
    <br><code>VISTOS, NO INTEGRADOS</code>: Monterrey, col. Nueva Topo Chico (1 larga, 1 corta, 1 cargador, 1 detenido: <b>una sola fuente</b>, MVS 2026/10/13) · San Luis Potosí, Zona Industrial (1 arma sin tipo, 3 detenidos: sin cifra por categoría) · Oxkutzcab, Yucatán (armas sin cifra, 2 detenidos) · Cancún, dos cateos publicados el 12-oct (<code>CIFRAS CONTRADICHAS ENTRE MEDIOS: 16 O 25 ARMAS</code>; La Selva, SM 225: <code>POSIBLE DUPLICIDAD</code> con el cateo del 8-oct).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: León, FSPE, 1 revólver, 49 cartuchos y 1 detenido (boletín oficial del 13-oct; hecho del 27-sep, solo por resumen) · boletín del Gabinete de Seguridad de las acciones del <b>12-oct</b>, por republicadores (Milenio, RED113, Argon México 2026/10/13): Cotija, Plan del Cerro, <b>122 AEI</b>, 4 largas, 4 cargadores y 45 cartuchos; Zinacantepec, 2 largas, 1 corta y 3 detenidos; Matamoros, 4 largas; Concordia, 1 larga, 1 cargador y 23 cartuchos — <b>todo solo por resumen</b>.
    <br><b>Recuperaciones, fuera del total</b>: ARG-132-REC-003 (Doctor Coss, 2 largas) · ARG-132-REC-005 (Escuinapa, 2 cortas, 2 cargadores y 18 cartuchos, solo por resumen).
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas, abajo, no se integran</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>16 estatales revisadas</b> · 16 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Oaxaca</b><br>San Antonio de la Cal</td><td>A.J.B. · <span class="muted-note">feminicidio agravado de 2021</span></td><td><b>80 años</b>, por titular</td><td>FGEO <span class="muted-note">(boletín 2,889, título solo por resumen)</span></td><td><code>FECHA DE PUBLICACIÓN NO ANCLADA: URL 2026/10 SIN DÍA</code> · el 13-oct, solo por resumen</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>Monterrey</td><td>Cuatro sentenciados · <span class="muted-note">secuestro agravado y homicidio calificado (2019-2023)</span></td><td><b>155 años</b> a uno y <b>80</b> a cada uno de tres, por titular y resumen</td><td>FGJ Nuevo León <span class="muted-note">(por cita)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · MVS 2026/10/13 · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>Bajo</td></tr>
      <tr><td><b>Zacatecas</b><br>Guadalupe</td><td>Juan «N» · <span class="muted-note">violación equiparada agravada; abreviado</span></td><td><b>10 años</b>, por titular</td><td>FGJEZ <span class="muted-note">(titular de republicador)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · LJZ 13/10/2026 · boletín no indexado en el dominio</td><td>Bajo</td></tr>
      <tr><td><b>Sonora</b><br>Nogales</td><td>Mateo «N» · <span class="muted-note">tentativa de feminicidio; abreviado</span></td><td><b>15 años</b>, por titular</td><td>FGJE Sonora <span class="muted-note">(titular de republicadores)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · El Vigía 2026/10/13 · dominio de la fiscalía no devuelto</td><td>Bajo</td></tr>
      <tr><td><b>Chihuahua</b></td><td>Lorenzo «N» · Jaqueline y Francisco «N» · <span class="muted-note">armas y droga</span></td><td><b>7 años 1 mes</b> · <b>7 años 6 meses</b>, por titular y resumen</td><td>FGR <span class="muted-note">(titular de republicador)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · 860 Líder Informativo 2026/10/13 · Lorenzo «N», publicado ya el 12-oct</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Tres culpables · <span class="muted-note">feminicidio y homicidio</span></td><td><code>SIN PENA INDEXADA: INDIVIDUALIZACIÓN EL 14-OCT</code></td><td>PGJ Hidalgo <span class="muted-note">(por cita)</span></td><td>Fallo del 8-9 oct; <b>no es sentencia</b> hasta la individualización</td><td>Bajo</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Vistas, publicadas antes de la apertura</b>: Sinaloa, Navolato, 40 años (12-oct) · Sinaloa, Navolato, 80 años (10-oct) · Colima, 27 años (9-oct) · Guanajuato, León, 26 años 8 meses (9-oct) · Querétaro, tres sentencias (5 a 8-oct). <code>NO SE INTEGRAN: FUERA DE VENTANA O SIN BOLETÍN OFICIAL.</code>
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>16 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · Chih, Dgo · Coah, Tamps, Zac · Jal, Col, Ags, Mich · CDMX, Mor, Qro · Ver, Tab · Oax, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada</b></td><td><b>1</b>: Oaxaca (FGEO), <b>no integrable</b> · <b>con sentencia integrable: 0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>16</b>: BC, BCS, Son, Sin · NL, SLP · Nay, Gto · Edomex, Pue, Tlax, Hgo · Gro, Chis, Camp, Yuc</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 32 de 32 por búsqueda dirigida en medios</b> · <b>armamento: 16 de 32</b>; <code>NO REVISADA</code>: BC, Coah, NL, Tamps, SLP, Ags, CDMX, Edomex, Mor, Qro, Gro, Oax, Chis, Camp, Yuc, QRoo · <code>ARMAMENTO Y SENTENCIAS: REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, Defensa, Marina y FGR: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 12-oct</b>: existe, <b>solo por republicadores</b> · <b>acciones del 13-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 14-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NIVEL FIJADO POR UN ROJO</b>: ARG-132-001 (Sinaloa).
      <br><b>2.</b> <b>Contexto operativo</b>: ARG-132-002 a ARG-132-005.
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-132-006.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-132-REC-001 a ARG-132-REC-005.
      <br><b>5.</b> <code>24 H 56 MIN; LOS SEIS HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. HOMICIDIOS POR ARMA DE FUEGO EN NAUCALPAN.</b> ARG-132-004: tercero en el municipio desde el 8-9 oct, con ARG-128-005 y ARG-128-006, <b>cálculo propio</b>;
      el modus operandi de los dos anteriores no se publicó. Línea: <b>solicitar a la FGJEM el cotejo balístico</b> de los tres casos — hipótesis.
      <br><b>2. MANDO DE UNA CÉLULA DEL CJNG EN OAXACA, CAPTURADO EN GUADALAJARA.</b> ARG-132-006. Línea: <b>solicitar a la SSPC la red de apoyo</b> de la célula en el Istmo — requiere validación.
      <br><b>3. ENFRENTAMIENTOS CON ABATIDOS Y ARMAS LARGAS.</b> ARG-132-005 y ARG-132-REC-003: cinco abatidos, <b>cálculo propio</b>. Línea: <b>solicitar a la Defensa el parte de Cotija</b> con iniciador y armamento.
      <br><b>4. ATAQUES ARMADOS DENTRO DE COMERCIOS.</b> ARG-132-REC-001 y ARG-132-REC-002 (una tienda y una estética). Línea: <b>solicitar a las fiscalías de Puebla y Sinaloa</b> las denuncias previas de extorsión — hipótesis.
      <br><b>5. BRECHA ENTRE HECHO Y CONDENA EN VIOLENCIA CONTRA MUJERES.</b> Tres de las seis condenas candidatas —Oaxaca, Zacatecas, Sonora— son por hechos de 2018 a 2025.
      Línea: <b>solicitar a las fiscalías los tiempos procesales</b> de cada caso.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>. <b>SESNSP, INEGI y FGR</b>: <b>sin publicación estadística nueva localizada dentro de la ventana</b>; el balance de detenciones del 14-oct es un acumulado de dos años, no del corte.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO Y VIOLENCIA OPERATIVA: NAVOLATO, ORIZABA Y SAN BLAS ATEMPA", co1)
 + page("CRIMEN ORGANIZADO (II) — NAUCALPAN, COTIJA Y GUADALAJARA", co2)
 + page("CRIMEN ORGANIZADO (III) — RECUPERACIONES: VENTANAS DE ARGOS 129 A 131", rec1)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana 13-oct 07:23 → 14-oct 08:19 toca dos fechas de calendario
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R))
