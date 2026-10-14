# -*- coding: utf-8 -*-
"""Generador de datos único de ARGOS 132: fichas, panorama, EVENTOS, EVENTOS_ARM y totales derivados.
Uso: python3 tools/datos-argos-131.py <plantilla ARGOS 131> <salida>"""
import sys, re, json, html as H

NUM, FECHA, HORA = "132", "2026-10-14", "08:19"
CONSULTA = "2026-10-14 08:19-10:30"
DUR = "24 h 56 min"
ESTR = {"★★★☆☆": "🟡 Medio", "★★☆☆☆": "🟠 Bajo", "★★★★☆": "🟢 Alto"}
FLAG = {"rojo": ("alto", "ROJO"), "amarillo": ("medio", "AMARILLO"), "verde": ("bajo", "VERDE"), "rec": ("sindato", "RECUPERACIÓN")}
SEM = {"rojo": "🔴 Rojo", "amarillo": "🟡 Amarillo", "verde": "🟢 Verde"}
FR = "<code>FRONTERA DE VENTANA — HORA NO FIJADA</code>"
RES = "<code>SOLO POR RESUMEN</code>"
# ---------------------------------------------------------------- HECHOS PROPIOS
E = [
 dict(id="ARG-132-001", estado="MX-VER", region="Golfo", color="amarillo", impacto="mediano", fecha="2026-10-13", hora="noche, ~19:30–20:00 (solo por resumen)",
  ent="Veracruz", mun="Orizaba (col. El Espinal Bajo)", dia="13-OCT, NOCHE",
  title="VERACRUZ · ORIZABA — RECIBEN A TIROS UN CATEO DE LA POLICÍA MINISTERIAL: TRES AGENTES HERIDOS, UN MUERTO Y DOS PERSONAS RESCATADAS",
  hecho="Orizaba · <code>COL. EL ESPINAL BAJO, AV. DE LA FUENTE ENTRE GÓMEZ FARÍAS Y 5 DE MAYO — SOLO POR RESUMEN</code> · noche del MARTES 13-OCT, ~19:30–20:00 (" + RES + ") · la <b>Policía Ministerial</b>, con apoyo estatal y federal, ejecuta un <b>cateo</b> y es <b>repelida a tiros</b>, por titular (🟡) · <b>3 policías ministeriales heridos</b>, por titular; uno grave, " + RES + " · <b>1 persona muerta</b>, por titular · <code>IDENTIDAD DEL MUERTO NO DETERMINADA: «UN CIVIL» POR TITULAR DE UN SOLO MEDIO; SI FUERA PERSONAL O VÍCTIMA AJENA, SUBE A 🔴</code> · <b>2 personas presuntamente privadas de la libertad, rescatadas</b>, por titular · <b>ningún detenido publicado</b> · armamento asegurado: no publicado",
  panel="Cateo repelido: <b>3 ministeriales heridos</b>, <b>1 muerto</b> y <b>2 personas rescatadas</b>",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="La Silla Rota · Meganoticias · TV Azteca", conf="★★★☆☆",
  campo="hora e identidad del muerto no fijadas; sin boletín institucional", I=0, N=3, R=5, A=0,
  fechadas=["La Silla Rota (2026/10/13)", "Golpe Político (2026/10/13, dos notas)"], estatus="Parcialmente corroborado", arm=None, cual=True,
  desl="Orizaba no figura en el índice ni en las tres ediciones previas; «cinco presuntos secuestradores muertos en Orizaba» (El Universal) es de 2025. 🟡 por confrontación derivada de un operativo. El rescate es resultado del mismo cateo: no se abre ficha verde aparte"),
 dict(id="ARG-132-002", estado="MX-OAX", region="Sureste", color="amarillo", impacto="mediano", fecha="2026-10-13", hora="mañana, antes de las 10:45 (solo por resumen)",
  ent="Oaxaca", mun="San Blas Atempa (Secundaria Técnica 69)", dia="13-OCT, MAÑANA",
  title="OAXACA · SAN BLAS ATEMPA — HOMBRES ARMADOS ENTRAN A UNA SECUNDARIA Y ASESINAN A UN PROFESOR FRENTE A LOS ALUMNOS",
  hecho="San Blas Atempa · <code>ESCUELA SECUNDARIA TÉCNICA N.° 69</code> · mañana del MARTES 13-OCT, al inicio de clases (" + RES + ") · hombres armados entran al plantel y disparan contra un <b>profesor</b> frente a alumnos, por titular · <b>1 muerto</b>, por titular (🟡): fallece en el ISSSTE de Tehuantepec, " + RES + " · <b>FGEO</b>: carpeta por homicidio calificado y despliegue de la Agencia Estatal de Investigaciones, " + RES + " · <b>ningún detenido publicado</b> · móvil no publicado · identidad: no se reproduce · " + FR,
  panel="<b>Profesor asesinado</b> dentro de una secundaria",
  inst="FGEO <span class=\"muted-note\">(por cita)</span>", nac="El Financiero · Infobae · La Jornada · El Informador", conf="★★★☆☆",
  campo="hora solo por resumen; sin boletín institucional", I=1, N=4, R=6, A=0,
  fechadas=["El Financiero (2026/10/13)", "Infobae (2026/10/13)", "La Jornada (2026/10/13)", "El Informador (20261013)", "Proyecto Puente (2026/10/13)", "Sociedad Noticias (2026/10/13)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Blas Atempa no figura en el índice ni en las tres ediciones previas; el boletín FGEO 2,685 (5-ago) es otro caso. <code>SI OCURRIÓ ANTES DE LAS 07:23 DEL 13-OCT, SU VENTANA ES LA DE ARGOS 131</code>. Uniformes que simulaban ser de la Fiscalía: un solo medio, no se integra. Vínculo con las agresiones del Istmo: no acreditado. 🟡 por homicidio doloso único"),
 dict(id="ARG-132-003", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-10-13", hora="mañana (solo por resumen)",
  ent="Estado de México", mun="Naucalpan (col. La Mancha 1)", dia="13-OCT, MAÑANA",
  title="ESTADO DE MÉXICO · NAUCALPAN — DESDE UNA MOTOCICLETA ASESINAN A BALAZOS A UNA MUJER QUE CONDUCÍA SU VEHÍCULO",
  hecho="Naucalpan · <code>COL. LA MANCHA 1, AV. MOLINOS DE VIENTO — SOLO POR RESUMEN</code> · mañana del MARTES 13-OCT (" + RES + ") · agresores en motocicleta disparan contra una mujer que conducía, por titular · <b>1 mujer asesinada</b>, por titular (🟡) · al menos 2 impactos, " + RES + " · <code>VEHÍCULO CONTRADICHO: CAMIONETA O AUTOMÓVIL</code> · <b>FGJEM</b> investiga, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce · " + FR,
  panel="<b>1 mujer asesinada</b> dentro de su vehículo",
  inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="El Heraldo de México · El Universal", conf="★★★☆☆",
  campo="hora solo por resumen; sin fuente institucional", I=0, N=2, R=3, A=0,
  fechadas=["El Heraldo de México (2026/10/13)", "Cúspide México (2026/10/14)"], estatus="Parcialmente corroborado", arm=None,
  desl="La Mancha no figura en el índice; NO es ARG-128-005 (Valle Dorado) ni ARG-128-006 (Minas Palacio). <code>SI OCURRIÓ ANTES DE LAS 07:23 DEL 13-OCT, SU VENTANA ES LA DE ARGOS 131</code>. 🟡 por homicidio doloso único"),
 dict(id="ARG-132-004", estado="MX-JAL", region="Occidente", color="verde", impacto="grande", fecha="2026-10-14", hora="no publicada",
  ent="Jalisco", mun="Guadalajara", dia="ANUNCIO 14-OCT, HECHO NO FIJADO",
  title="JALISCO · GUADALAJARA — DETIENEN AL SEÑALADO LÍDER DE «LOS CROMOS», CÉLULA VINCULADA AL CJNG CON RECOMPENSA DE DOS MILLONES",
  hecho="Guadalajara · <b>anunciada el MIÉRCOLES 14-OCT por el titular de la SSPC</b>, por titular · <code>FECHA DE LA CAPTURA NO PUBLICADA</code> · Semar y CNI, " + RES + " · detención de Iván «N», «El Cromo», señalado líder de <b>Los Cromos</b>, vinculados al CJNG, por titular · <b>1 detenido</b> (🟢) · <b>recompensa de 2 millones de pesos</b>, por titular · <code>ÓRDENES DE APREHENSIÓN POR HOMICIDIO: 2 O 3, CONTRADICHO</code> · acusaciones, no condena · sin armamento publicado · " + FR,
  panel="Detenido el señalado líder de <b>Los Cromos</b>",
  inst="SSPC <span class=\"muted-note\">(anuncio, por titular de medios)</span>", nac="La Razón · La Silla Rota · El Heraldo de México", conf="★★★☆☆",
  campo="fecha de la captura no publicada; anuncio sin boletín leído", I=1, N=3, R=1, A=0,
  fechadas=["La Razón (2026/10/14)", "La Silla Rota (2026/10/14)", "El Heraldo de México (2026/10/14)", "El Imparcial (2026/10/14)"], estatus="Parcialmente corroborado", arm=None, fecha_txt="no publicada; anunciada el 2026-10-14",
  desl="«El Cromo» y Los Cromos no figuran en el índice ni en las tres ediciones previas. Operación en el Istmo de Oaxaca: solo por resumen; vínculo con ARG-132-002 no acreditado. Si la captura fue anterior a las 07:23 del 13-oct, es evento anterior publicado durante el corte y sale de los totales. Sin armamento: fuera del conteo"),
 dict(id="ARG-132-005", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-13", hora="no publicada",
  ent="Sinaloa", mun="Escuinapa (col. Pueblo Nuevo)", dia="PUB. 13-OCT, HORA NO FIJADA",
  title="SINALOA · ESCUINAPA — UNA PERSECUCIÓN EN PUEBLO NUEVO TERMINA CON TRES DETENIDOS Y DOS PISTOLAS ASEGURADAS",
  hecho="Escuinapa · <code>COL. PUEBLO NUEVO</code> · publicado el MARTES 13-OCT · <code>FECHA DEL HECHO NO FIJADA: 12 O 13-OCT, SOLO POR RESUMEN</code> · <b>Grupo Interinstitucional</b> —policía municipal y Ejército—, por la SSP Sinaloa · persecución, por titular · <b>3 detenidos</b>, por titular (🟢) · <b>2 armas cortas 9 mm, 2 cargadores y 18 cartuchos</b>, " + RES + " · 2 motocicletas, una con reporte de robo, " + RES + " · sin disparos publicados · " + FR,
  panel="Persecución: <b>3 detenidos</b> y <b>2 pistolas</b>",
  inst="SSP Sinaloa <span class=\"muted-note\">(<i>slug</i> indexado, sin fecha)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★★☆☆",
  campo="fecha del hecho y desglose solo por resumen", I=1, N=0, R=1, A=0,
  fechadas=["Tus Buenas Noticias (2026/10/13)"], estatus="Parcialmente corroborado", arm="ARG-132-ARM-001", fecha_txt="no fijada (12 o 13-oct); publicado el 2026-10-13",
  desl="Pueblo Nuevo no figura en el índice; NO es ARG-124-006 (22-sep) ni ARG-131-004 (estética del centro). Si ocurrió antes de las 07:23 del 13-oct, su ventana es la de ARGOS 131"),
 dict(id="ARG-132-006", estado="MX-GUA", region="Occidente", color="verde", impacto="pequeno", fecha="2026-10-13", hora="no publicada",
  ent="Guanajuato", mun="León (Rancho Nuevo de la Venta)", dia="BOLETÍN 13-OCT, HORA NO FIJADA",
  title="GUANAJUATO · LEÓN — LAS FUERZAS DE SEGURIDAD DEL ESTADO DETIENEN A UN HOMBRE CON UN REVÓLVER Y 49 CARTUCHOS",
  hecho="León · <code>RANCHO NUEVO DE LA VENTA — SOLO POR RESUMEN</code> · boletín del MARTES 13-OCT; fecha y hora del hecho no publicadas · <b>FSPE</b> · <b>1 detenido</b>, <b>1 revólver</b> y <b>49 cartuchos útiles</b>, por el <i>slug</i> del boletín oficial (🟢) · puesto a disposición de la autoridad federal, " + RES + " · " + FR,
  panel="<b>1 detenido</b> con <b>1 revólver</b> y <b>49 cartuchos</b>",
  inst="Gobierno de Guanajuato <span class=\"muted-note\">(boletín, <i>slug</i> con fecha)</span>", nac="<span class=\"muted-note\">ninguna</span>", conf="★★☆☆☆",
  campo="una sola fuente; boletín no leído íntegro por el bloqueo de egreso", I=1, N=0, R=0, A=0,
  fechadas=["boletines.guanajuato.gob.mx (2026/10/13)"], estatus="Confirmado por fuente oficial indexada", arm="ARG-132-ARM-002", fecha_txt="no publicada; boletín del 2026-10-13",
  desl="Rancho Nuevo de la Venta no figura en el índice. El acumulado del mismo boletín (desde 2024) no es de la ventana y no se integra"),
]

# ---------------------------------------------------------------- RECUPERACIONES
R = [
 dict(id="ARG-132-REC-001", estado="MX-PUE", region="Centro", fecha="2026-10-12", hora="noche (solo por resumen)", orig="ARGOS 131", col_orig="amarillo",
  ent="Puebla", mun="Tehuacán (San Marcos Necoxtla)", dia="12-OCT, NOCHE",
  title="PUEBLA · TEHUACÁN — ASESINAN A BALAZOS A UN HOMBRE DENTRO DE UNA TIENDA EN SAN MARCOS NECOXTLA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131</code> · <code>SAN MARCOS NECOXTLA, TIENDA</code> · noche del LUNES 12-OCT (" + RES + ") · agresores huyen en un sedán y una motocicleta, " + RES + " · <b>1 hombre asesinado</b>, por titular (🟡 en su ventana) · <b>FGE Puebla</b>: carpeta por homicidio calificado, " + RES + " · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="<b>1 hombre asesinado</b> dentro de una tienda", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional ni nacional", I=0, N=0, R=9, A=0,
  fechadas=["Síntesis (2026/10/13)", "Reto Diario (2026/10/13)", "Intolerancia (2026/10/13)"],
  desl="Necoxtla no figura en el índice. ARGOS 131 lo vio y no lo fichó por falta de URL con fecha; Síntesis, Reto Diario e Intolerancia lo anclan. Nombre y edad discrepan entre medios"),
 dict(id="ARG-132-REC-002", estado="MX-MIC", region="Occidente", fecha="2026-10-12", hora="~12:00 (solo por resumen)", orig="ARGOS 131", col_orig="amarillo",
  ent="Michoacán", mun="Cotija (El Metidero)", dia="12-OCT, MEDIODÍA",
  title="MICHOACÁN · COTIJA — EL EJÉRCITO ABATE A TRES HOMBRES ARMADOS EN UN ENFRENTAMIENTO EN EL METIDERO",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131</code> · <code>EL METIDERO, HUERTA LA HACIENDA — SOLO POR RESUMEN</code> · LUNES 12-OCT, ~12:00 (" + RES + ") · enfrentamiento entre el <b>Ejército</b> y hombres armados, por titular · <b>3 agresores abatidos</b>, por titular (🟡 en su ventana) · <code>QUIÉN INICIÓ: NO DETERMINADO — VERSIONES CONTRADICHAS</code> · 3 fusiles AK-47 asegurados, " + RES + " · <b>ningún detenido publicado</b> · sin comunicado de la Defensa",
  panel="Enfrentamiento: <b>3 agresores abatidos</b> por el Ejército", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★☆☆☆", campo="fecha, hora e iniciador solo por resumen; dos medios con el mismo titular", I=0, N=0, R=7, A=1,
  fechadas=["Grupo Marmor (2026/10/13)", "Red Michoacán (2026/10/13)"],
  desl="Cotija figura solo en el agregado federal del 9 al 11-oct (otra acción). El boletín federal del 12-oct da 122 AEI, 4 largas, 4 cargadores y 45 cartuchos en Plan del Cerro, Cotija, solo por resumen: relación con este enfrentamiento NO DETERMINADA. Blog del Narco: NO OFICIAL. Publicado el 13-oct: si ocurrió después de las 07:23 del 13, pertenece a ARGOS 132"),
 dict(id="ARG-132-REC-003", estado="MX-SIN", region="Noroeste", fecha="2026-10-12", hora="~12:15 (solo por resumen)", orig="ARGOS 131", col_orig="amarillo",
  ent="Sinaloa", mun="Mazatlán (Villa Unión, col. Toledo Corro)", dia="12-OCT, MEDIODÍA",
  title="SINALOA · MAZATLÁN — ATACAN A BALAZOS UNA ESTÉTICA EN VILLA UNIÓN: UN HOMBRE MUERTO Y UNA MUJER HERIDA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 131</code> · <code>VILLA UNIÓN, COL. TOLEDO CORRO, ESTÉTICA</code> · LUNES 12-OCT, aviso ~12:15 (" + RES + ") · ataque armado · <b>1 hombre muerto y 1 mujer herida</b>, por titular (🟡 en su ventana) · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque a una estética: <b>1 muerto</b> y <b>1 herida</b>", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora solo por resumen; sin fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-10-12)", "Línea Directa (2026-10-12)"],
  desl="Toledo Corro no figura en el índice. NO es la llantera de Villa Unión (1-oct), ni la mujer asesinada en Villa Unión el 11-oct que ARGOS 131 dejó sin URL con fecha, ni ARG-131-004 (estética de Escuinapa)"),
 dict(id="ARG-132-REC-004", estado="MX-NLE", region="Noreste", fecha="2026-10-12", hora="no publicada", orig="ARGOS 130 o ARGOS 131 — HORA NO FIJADA", col_orig="amarillo",
  ent="Nuevo León", mun="Doctor Coss", dia="PUB. 12-OCT, HORA NO FIJADA",
  title="NUEVO LEÓN · DOCTOR COSS — FUERZA CIVIL ABATE A DOS HOMBRES ARMADOS AL ACTIVAR EL OPERATIVO MURALLA",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 130 O ARGOS 131 — HORA NO FIJADA</code> · publicado el LUNES 12-OCT · <b>Fuerza Civil</b>, Operativo Muralla, por titular · enfrentamiento con civiles armados · <b>2 abatidos</b>, por titular (🟡 en su ventana) · <code>QUIÉN INICIÓ: NO DETERMINADO</code> · 2 armas largas aseguradas, ningún agente herido y otros agresores en fuga, " + RES + " · <b>ningún detenido publicado</b>",
  panel="Enfrentamiento: <b>2 abatidos</b> por Fuerza Civil", inst="Fuerza Civil <span class=\"muted-note\">(por cita)</span>", nac="MVS",
  conf="★★★☆☆", campo="hora y quién inició no fijados; desglose solo por resumen", I=0, N=1, R=1, A=0,
  fechadas=["MVS Noticias (2026/10/12)"],
  desl="<code>NO ES EL HECHO DEL 22-AGO-2025</code> (12 abatidos, mismo municipio): trampa de año. Doctor Coss no figura en el índice de 2026"),
 dict(id="ARG-132-REC-005", estado="MX-NAY", region="Occidente", fecha="2026-10-11", hora="no publicada", orig="ARGOS 129 o ARGOS 130 — HORA NO FIJADA", col_orig="rojo",
  ent="Nayarit", mun="Acaponeta (carretera Tepic–Mazatlán)", dia="11-OCT, HORA NO FIJADA",
  title="NAYARIT · ACAPONETA — HALLAN TRES CUERPOS ENVUELTOS EN COBIJAS JUNTO A LA CARRETERA TEPIC–MAZATLÁN",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 129 O ARGOS 130 — HORA NO FIJADA</code> · <code>KM 112+600, ACCESO A LAS GUÁSIMAS — KILÓMETRO CONTRADICHO (111), SOLO POR RESUMEN</code> · DOMINGO 11-OCT · hallazgo de <b>3 cuerpos envueltos en cobijas</b>, por titular (🔴 en su ventana) · cartulinas con mensajes, contenido no publicado, " + RES + " · causa de muerte e identidades: no publicadas · <b>FGE Nayarit sin comunicado</b>, " + RES,
  panel="Hallazgo de <b>3 cuerpos</b> junto a la carretera", inst="<span class=\"muted-note\">SIN BOLETÍN</span>", nac="<span class=\"muted-note\">ninguna</span>",
  conf="★★★☆☆", campo="hora no fijada; sin fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["NTV (2026/10/11)", "Nayarit Noticias (2026/10/11)"],
  desl="NO es el hallazgo de La Higuerita, km 126 (9-sep). ARGOS 131 lo dejó como candidato sin URL con fecha; NTV y Nayarit Noticias lo anclan al 11-oct. Si fue antes de las 08:58 del 11-oct, su ventana es la de ARGOS 129. 🔴 por homicidio múltiple"),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-132-ARM-001", ficha="ARG-132-005", estado="MX-SIN", region="Noroeste", ent="Sinaloa", mun="Escuinapa (Pueblo Nuevo)", c=[2,0,0,0,18,2,0,0,0,3], corp="Grupo Interinstitucional (municipal y Ejército)", conf="Bajo", color="verde", fecha="2026-10-13", hora="no fijada", fecha_txt="12 o 13-oct, no fijada<br><span class=\"muted-note\">publicado el 13-oct</span>", nota="Desglose SOLO POR RESUMEN del boletín de la SSP Sinaloa; FRONTERA DE VENTANA", fuentes=["SSP Sinaloa (slug sin fecha)", "Tus Buenas Noticias (2026/10/13)"]),
 dict(id="ARG-132-ARM-002", ficha="ARG-132-006", estado="MX-GUA", region="Occidente", ent="Guanajuato", mun="León (Rancho Nuevo de la Venta)", c=[1,0,0,0,49,0,0,0,0,1], corp="FSPE", conf="Medio", color="verde", fecha="2026-10-13", hora="no fijada", fecha_txt="no publicada<br><span class=\"muted-note\">boletín del 13-oct</span>", nota="Cifras por el slug del boletín oficial; FRONTERA DE VENTANA", fuentes=["boletines.guanajuato.gob.mx (2026/10/13)"]),
]
TOT = [sum(a["c"][i] for a in ARM) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["ent"] for e in E))
ENT_ARM = sorted(set(a["ent"] for a in ARM))
assert TOT == [3, 0, 0, 0, 67, 2, 0, 0, 0, 4], TOT
assert cnt == {"rojo": 0, "amarillo": 3, "verde": 3}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 4, "verde": 0}, cnt_rec
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
      <b>1. SOLICITE A LA FISCALÍA DE VERACRUZ LA IDENTIDAD DEL FALLECIDO Y EL PARTE DEL CATEO DE ORIZABA</b> (ARG-132-001).
      <br><b>2. SOLICITE A LA FGEO EL MÓVIL DEL ATAQUE EN LA SECUNDARIA DE SAN BLAS ATEMPA</b> (ARG-132-002) y evalúe el resguardo de planteles del Istmo.
      <br><b>3. SOLICITE A LA FISCALÍA DE MORELOS EL PARTE DE LA RETENCIÓN DE TOTOLAPAN Y LA SITUACIÓN DEL LIBERADO</b> (ARG-131-002), y a la SSPC Morelos
      el informe del accidente de la autopista La Pera–Cuautla.
      <br><b>4. SOLICITE A LA FISCALÍA DE SINALOA EL PARTE DEL ATAQUE DE VALLADO VIEJO</b> (ARG-131-001), que los medios también sitúan en Recursos Hidráulicos.
      <br><b>5. SOLICITE A LA SSPC EL BOLETÍN DE ACCIONES DEL 13-OCT Y A LA FISCALÍA DE NAYARIT EL COMUNICADO DEL HALLAZGO DE ACAPONETA</b> (ARG-132-REC-005).
    </p>
  </div>

{footer()}</section>
'''

rows_own = "\n".join(prow(e) for e in E)
rows_rec = "\n".join(prow(r, True) for r in R)
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>13-oct 07:23 → 14-oct 08:19 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad 0,24 hechos/hora</b>, <b>cálculo propio</b>. <b>Orden: amarillos, verdes</b>; <b>ningún rojo propio</b>. <b>Cinco de seis</b> llevan <code>FRONTERA DE VENTANA</code>.
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
    <b>Detenidos</b> = solo los del <b>mismo evento de aseguramiento de armamento</b>; el de ARG-132-004, sin armas, no entra. <b>Entidades</b> = con al menos un hecho propio.
    <b>Muertos en hechos propios: 3</b> —Orizaba, San Blas Atempa y Naucalpan—. <b>Heridos: 3</b> policías ministeriales (Orizaba). <b>Rescatados: 2</b>. <b>Cálculo propio</b>.
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
 tile(0, "Armas cortas", TOT[0], "Escuinapa 2 · León 1 · <code>ESCUINAPA, SOLO POR RESUMEN</code>"),
 tile(1, "Armas largas", TOT[1], "<code>NINGUNA ARMA LARGA CON CIFRA EN HECHO PROPIO</code>"),
 tile(2, "Sin categoría", TOT[2], "<code>NINGUNA ARMA SIN CLASIFICAR INTEGRADA</code>"),
 tile(3, "Cartuchos", fmt(TOT[4]), "León 49 · Escuinapa 18"),
 tile(4, "Cargadores", TOT[5], "Escuinapa · <code>SOLO POR RESUMEN</code>"),
 tile(5, "Granadas", TOT[6], "<code>NINGUNA GRANADA PUBLICADA</code>"),
 tile(6, "AEI", TOT[7], "<code>NINGÚN AEI EN HECHO PROPIO</code> · los 122 de Cotija son de una acción anterior"),
 tile(7, "Explosivos", TOT[8], "<code>NINGÚN EXPLOSIVO, DETONADOR NI INICIADOR EN HECHO PROPIO</code>"),
 tile(8, "Armamento especial", TOT[3], "<code>NINGÚN ARMAMENTO ESPECIAL PUBLICADO</code>"),
 tile(9, "Detenidos", TOT[9], "<code>SOLO EN EVENTOS CON ASEGURAMIENTO DE ARMAMENTO</code>"),
])
assert len(icos) == 10, len(icos)

arm1 = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    <b>{len(ARM)} filas de armamento</b> de {len(ARM)} hechos verdes en <b>{len(ENT_ARM)} entidades</b>; <b>ambas con FRONTERA DE VENTANA</b>. <b>Totales por categoría: cálculo propio.</b>
    <code>NINGÚN HECHO AMARILLO PUBLICÓ ARMAMENTO ASEGURADO CON CIFRA.</code>
  </p>
  <div class="conteo">
{tiles}
  </div>

  <div class="panel" style="margin-top:8px;">
    <div class="panel-title"><span>MAPA DE ASEGURAMIENTOS — SEMÁFORO ARGOS</span><span>GIS POR ENTIDAD</span></div>
    <div class="map-box" id="argos-map-arm"></div>
    <div class="map-caption">Verde = aseguramiento sin enfrentamiento. La sola presencia de armas no vuelve roja a una entidad.</div>
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
    <b>Lectura regional</b> —2 filas, <b>cálculo propio</b>—: <b>Noroeste 1</b> · <b>Noreste 0</b> · <b>Occidente 1</b> · <b>Centro 0</b> · <b>Golfo 0</b> · <b>Sureste 0</b>.
    <b>Evento cualitativo</b>: ARG-132-001 (cateo de Orizaba, armamento no publicado).
    <br><code>VISTOS, NO INTEGRADOS</code>: Monterrey, col. Nueva Topo Chico (1 larga, 1 corta, 1 cargador, 1 detenido: <b>una sola fuente</b>, MVS 2026/10/13) · San Luis Potosí, Zona Industrial (1 arma sin tipo, 3 detenidos) · Oxkutzcab, Yucatán (armas sin cifra, 2 detenidos) · Cancún, dos cateos publicados el 12-oct (<code>CIFRAS CONTRADICHAS ENTRE MEDIOS: 16, 24 O 25 ARMAS</code>).
    <br><code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE — FUERA DEL TOTAL</code>: boletín del Gabinete de Seguridad de las acciones del <b>12-oct</b>, localizado por republicadores (Milenio, RED113, Argon México 2026/10/13): Cotija, Plan del Cerro, <b>122 AEI</b>, 4 largas, 4 cargadores y 45 cartuchos; Zinacantepec, 2 largas, 1 corta y 3 detenidos; Matamoros, 4 largas; Concordia, 1 larga, 1 cargador y 23 cartuchos — <b>todo solo por resumen</b>.
  </p>
'''

sent = f'''  <div class="conteo">
    <div class="tile cero"><span class="lbl">Sentencias condenatorias</span><span class="num">0</span><span class="sub"><code>NINGUNA SENTENCIA INTEGRABLE EN LA VENTANA</code></span></div>
    <div class="tile cero"><span class="lbl">Personas sentenciadas</span><span class="num">0</span><span class="sub">las candidatas, abajo, no se integran</span></div>
    <div class="tile cero"><span class="lbl">Pena acumulada</span><span class="num">0</span><span class="sub"><b>los años nunca se suman entre casos</b></span></div>
    <div class="tile cero"><span class="lbl">Reparación del daño</span><span class="num">0</span><span class="sub"><b>ningún monto integrable</b></span></div>
    <div class="tile cero"><span class="lbl">Fiscalías con resultado</span><span class="num">0</span><span class="sub"><b>17 estatales revisadas</b> · 15 <code>NO REVISADA</code></span></div>
  </div>

  <div class="section-head" style="margin-top:10px;">CANDIDATOS Y COBERTURA</div>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Entidad · Municipio</th><th>Caso</th><th>Pena publicada</th><th>Autoridad</th><th>Por qué NO se integra</th><th>Confianza</th></tr></thead>
    <tbody>
      <tr><td><b>Oaxaca</b><br>San Antonio de la Cal</td><td>A.J.B. · <span class="muted-note">feminicidio agravado (8-ene-2021)</span></td><td><b>80 años</b>, por titular</td><td>FGEO <span class="muted-note">(boletín 2,889, título solo por resumen)</span></td><td><code>FECHA DE PUBLICACIÓN NO ANCLADA: URL 2026/10 SIN DÍA</code> · el 13-oct, solo por resumen</td><td>Bajo</td></tr>
      <tr><td><b>Nuevo León</b><br>Monterrey</td><td>Cuatro sentenciados · <span class="muted-note">secuestro agravado y homicidio calificado (2019-2023)</span></td><td><b>155 años</b> a uno y <b>80</b> a cada uno de tres, por titular y resumen</td><td>FGJ Nuevo León <span class="muted-note">(por cita)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · MVS 2026/10/13 · <code>PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA</code></td><td>Bajo</td></tr>
      <tr><td><b>Zacatecas</b><br>Guadalupe</td><td>Juan «N» · <span class="muted-note">violación equiparada agravada; abreviado</span></td><td><b>10 años</b>, por titular</td><td>FGJEZ <span class="muted-note">(titular de republicador)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · LJZ 13/10/2026 · boletín no indexado en el dominio</td><td>Bajo</td></tr>
      <tr><td><b>Sonora</b><br>Nogales</td><td>Mateo «N» · <span class="muted-note">tentativa de feminicidio; abreviado</span></td><td><b>15 años</b>, por titular</td><td>FGJE Sonora <span class="muted-note">(titular de republicadores)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · El Vigía 2026/10/13 · dominio de la fiscalía no devuelto</td><td>Bajo</td></tr>
      <tr><td><b>Chihuahua</b><br>Ciudad Juárez</td><td>Lorenzo «N» · Jaqueline y Francisco «N» · <span class="muted-note">armas y droga</span></td><td><b>7 años 1 mes</b> · <b>7 años 6 meses</b>, por titular y resumen</td><td>FGR <span class="muted-note">(titular de republicador)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · 860 Líder Informativo 2026/10/13 · Lorenzo «N», publicado ya el 12-oct</td><td>Bajo</td></tr>
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
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>17 de 32</b> · <b>FGR revisada: Sí</b>, por búsqueda · Chih, Dgo · Coah, Tamps, Zac · Jal, Col, Ags, Mich · CDMX, Mor, Qro · Ver, Tab · Gro, Oax, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia integrable</b></td><td><b>0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>17</b> fiscalías estatales</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b> · exige lectura directa del portal</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>15</b>: BC, BCS, Son, Sin · NL, SLP · Nay, Gto · Edomex, Pue, Tlax, Hgo · Chis, Camp, Yuc</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 32 de 32 por búsqueda dirigida en medios</b> · <b>armamento: 19 de 32</b>; <code>NO REVISADA</code>: BC, Coah, NL, Tamps, SLP, Ags, CDMX, Edomex, Mor, Qro, Camp, Yuc, QRoo · <code>ARMAMENTO Y SENTENCIAS: REVISADA = BÚSQUEDA DIRIGIDA QUE DEVOLVIÓ EL DOMINIO OFICIAL</code> · GN, Defensa, Marina y FGR: <code>SIN RESULTADO INDEXADO EN VENTANA</code></td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 12-oct</b>: existe, <b>solo por republicadores</b> · <b>acciones del 13-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en las tres formas de consulta</td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★☆☆</b> · <code>BLOQUEO DE EGRESO REVERIFICADO EL 14-OCT: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>NINGÚN EVENTO ROJO PROPIO EN LA VENTANA.</b>
      <br><b>2.</b> <b>Contexto operativo</b>: tres amarillos, ARG-132-001 a ARG-132-003 (Veracruz, Oaxaca y Estado de México).
      <br><b>3.</b> <b>Respuesta institucional propia</b>: ARG-132-004 a ARG-132-006.
      <br><b>4.</b> <b>Recuperaciones</b>: ARG-132-REC-001 a ARG-132-REC-005, de las ventanas de ARGOS 129 a 131, fuera de los totales; ARG-132-REC-005, rojo en su ventana.
      <br><b>5.</b> <code>24 H 56 MIN; CINCO DE SEIS HECHOS CON FRONTERA DE VENTANA: TOTALES NO COMPARABLES SIN MÁS.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. ATAQUE DESDE MOTOCICLETA CONTRA CONDUCTORES EN NAUCALPAN.</b> ARG-132-003, tercer homicidio en el municipio en cinco días con ARG-128-005 y ARG-128-006, <b>cálculo propio</b>.
      Línea: <b>solicitar a la FGJEM el cotejo balístico</b> de los tres casos — patrón por validar.
      <br><b>2. MANDO DE CÉLULAS AFINES AL CJNG FUERA DE SU ZONA DE OPERACIÓN.</b> ARG-132-004: captura en Guadalajara de una célula que operaría en el Istmo, solo por resumen.
      Línea: <b>solicitar a la SSPC la red de apoyo</b> de la célula — requiere validación.
      <br><b>3. ARMA CORTA Y MOTOCICLETA EN EL SUR DE SINALOA.</b> ARG-132-005 y ARG-132-REC-003 (Escuinapa y Villa Unión). Línea: <b>solicitar el cruce</b> de motocicletas con reporte de robo y casquillos 9 mm — hipótesis.
      <br><b>4. ENFRENTAMIENTOS CON ABATIDOS SIN PARTE OFICIAL.</b> ARG-132-REC-002 y ARG-132-REC-004: cinco abatidos y armas largas sin comunicado. Línea: <b>solicitar a la Defensa y a Fuerza Civil</b> el parte de cada hecho.
      <br><b>5. BRECHA ENTRE CONDENA ANUNCIADA Y BOLETÍN OFICIAL.</b> Seis sentencias de Oaxaca, Nuevo León, Zacatecas, Sonora y la FGR solo existen en medios en esta ventana.
      Línea: <b>solicitar el boletín oficial</b> de cada una.
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
 + page("CRIMEN ORGANIZADO (I) — VIOLENCIA OPERATIVA: ORIZABA, SAN BLAS ATEMPA Y NAUCALPAN", co1)
 + page("CRIMEN ORGANIZADO (II) — ACCIONES INSTITUCIONALES: GUADALAJARA, ESCUINAPA Y LEÓN", co2)
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
