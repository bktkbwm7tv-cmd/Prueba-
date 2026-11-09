# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 149.
Uso: python3 tools/datos-argos-149.py <plantilla ARGOS 148> <salida>
Ventana: 6-nov 07:30 → 9-nov 16:07 CDMX. Archivo: argos-2026-11-09.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "149", "2026-11-09", "16:07"
CONSULTA = "2026-11-09, última búsqueda 16:56"
DUR = "80 h 37 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 07:30 DEL 6, ES DE LA VENTANA DE ARGOS 148 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-149-001", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-07", hora="poco antes de las 20:00 (solo por resumen)", mu=1, he=2, cu=0, hk=20,
  ent="Guanajuato", mun="Salamanca (Valtierrilla)", dia="7-NOV, POR RUTA",
  title="GUANAJUATO · SALAMANCA — EMBOSCADA CONTRA MILITARES EN VALTIERRILLA: UN SOLDADO MUERTO",
  hecho="Salamanca · <code>VALTIERRILLA, POR TITULAR</code> · sábado 7-NOV, por ruta (Correo 2026/nov/07: «ataque armado contra militares en Valtierrilla deja al menos tres elementos lesionados») · noche, " + RES + " · <b>1 militar muerto</b> en hospital de Irapuato el 8-NOV, por titular (Correo 2026/nov/08; AM 2026/11/08; Meganoticias: «muere militar por ataque armado tras emboscada») · heridos: <b>2</b>, Secretaría de Gobierno del Estado, " + RES + "; <b>3</b>, Defensa citada por medios, " + RES + ": <code>CIFRA DE HERIDOS CONTRADICHA</code> (se integra la menor) · personal en recorrido, " + RES + " (🔴 ataque iniciado por el grupo contra fuerzas en recorrido y muerte de personal) · la FGE investiga, " + RES + " · " + NOD + " · armamento: no publicado",
  panel="<b>Emboscada contra militares; 1 soldado muerto</b> y 2 o 3 heridos", inst=SB, nac="Meganoticias", conf="★★★☆☆",
  campo="hora y cifra de heridos solo por resumen; ninguna fuente institucional leída", I=0, N=1, R=3, A=0,
  fechadas=["Correo (2026/nov/07)", "Correo (2026/nov/08)", "AM (2026/11/08)"], estatus="Parcialmente corroborado", arm=None,
  desl="Valtierrilla no figura en las cinco ediciones previas ni en el índice. «Jornada violenta en Guanajuato deja seis muertos, incluido un militar» (La Prensa de Coahuila 2026/11/09): recuento de medios, no se integra."),
 dict(id="ARG-149-002", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-07", hora="20:00 o 21:00 (solo por resumen, contradicha)", mu=1, he=0, cu=0, hk=21,
  ent="Guanajuato", mun="San Francisco del Rincón", dia="7-NOV, POR RUTA",
  title="GUANAJUATO · SAN FRANCISCO DEL RINCÓN — ASESINAN A BALAZOS A UN POLICÍA MUNICIPAL",
  hecho="San Francisco del Rincón · <code>LIBRAMIENTO SUR Y BLVD. EMILIANO ZAPATA</code>, " + RES + " · sábado 7-NOV, por ruta (AM 2026/11/07: «asesinan a balazos a policía de San Francisco del Rincón tras salir de su turno»; Correo 2026/nov/07: «asesinan a policía en su día de descanso») · noche, 20:00 o 21:00, " + RES + " · <b>1 muerto</b>: policía municipal, por titular · <code>CONDICIÓN DE SERVICIO CONTRADICHA</code>: «tras salir de su turno» (AM; Meganoticias; Telediario) frente a «en su día de descanso» (Correo) (🔴 víctima autoridad en cualquiera de las dos) · perseguido y atacado, " + RES + " · la SSC municipal confirmó la muerte, " + RES + ": no es declaración leída · " + NOD,
  panel="<b>Policía municipal asesinado</b> al salir de turno o en día de descanso (contradicho)", inst=SB, nac="La Silla Rota · Meganoticias", conf="★★★☆☆",
  campo="hora y condición de servicio contradichas; ninguna fuente institucional leída", I=0, N=2, R=3, A=0,
  fechadas=["AM (2026/11/07)", "Correo (2026/nov/07)", "La Silla Rota (2026/11/8)"], estatus="Parcialmente corroborado", arm=None,
  desl="«Guanajuato suma 4 policías municipales asesinados en 3 semanas, todos en sábado» (Correo 2026/nov/09): recuento de medios, no se integra. Cuerámaro (comandante muerto el 7-nov): disparo con su arma de cargo, sin autoría de terceros publicada: <b>no es hecho del corte</b>. Identidad de la víctima: medios, no se reproduce."),
 dict(id="ARG-149-003", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-07", hora="madrugada (solo por resumen)", mu=3, he=1, cu=0, hk=6,
  ent="Guanajuato", mun="Valle de Santiago (El Armadillo)", dia="7-NOV, POR RUTA",
  title="GUANAJUATO · VALLE DE SANTIAGO — GRUPO ARMADO IRRUMPE EN UNA VIVIENDA DE EL ARMADILLO: TRES MUERTOS",
  hecho="Valle de Santiago · <code>EL ARMADILLO, POR TITULAR</code> · sábado 7-NOV, por ruta (AM 2026/11/07: «grupo armado irrumpe en casa y asesina a tres hombres y deja uno herido en El Armadillo»; Correo 2026/nov/07) · madrugada, " + RES + " · <b>3 hombres muertos y 1 herido</b>, por titular (🔴 homicidio múltiple) · la FGE inicia investigación, " + RES + " · " + NOD,
  panel="<b>Grupo armado irrumpe en vivienda: 3 muertos y 1 herido</b>", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["AM (2026/11/07)", "Correo (2026/nov/07)"], estatus="Parcialmente corroborado", arm=None,
  desl="Duranes de Arriba, Valle de Santiago (21-sep, 3 muertos y 5 heridos): otro hecho, otra ventana. El Armadillo no figura en las cinco ediciones previas."),
 dict(id="ARG-149-004", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-08", hora="tarde (solo por resumen)", mu=2, he=3, cu=0, hk=15,
  ent="Guanajuato", mun="Celaya (Segunda Fracción de Crespo)", dia="8-NOV, POR RUTA",
  title="GUANAJUATO · CELAYA — ATAQUE ARMADO CONTRA UNA FAMILIA EN CRESPO: DOS MUERTOS Y TRES HERIDAS, ENTRE ELLAS UNA NIÑA",
  hecho="Celaya · <code>SEGUNDA FRACCIÓN DE CRESPO, POR TITULAR</code> · domingo 8-NOV, por ruta (El Financiero 2026/11/08: «ataque armado contra una familia en Celaya deja dos muertos y tres mujeres heridas»; AM 2026/11/08: «matan a padre e hijo, hieren a adulta mayor y niña de 2 años») · tarde, " + RES + " · <b>2 hombres muertos y 3 heridas</b>, por titular (🔴 homicidio múltiple; menor herida) · composición de las heridas distinta entre titulares, misma cifra · agresores en motocicleta, " + RES + " · " + NOD,
  panel="<b>Ataque a una familia: 2 muertos y 3 heridas</b>, una niña de 2 años", inst=SB, nac="El Financiero · La Silla Rota", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=1, A=0,
  fechadas=["El Financiero (2026/11/08)", "AM (2026/11/08)", "La Silla Rota (2026/11/9)"], estatus="Parcialmente corroborado", arm=None,
  desl="La Silla Rota 2026/11/9 («matan a padre e hijo y hieren a una menor»): mismo hecho, no se duplica. «Privan de la libertad a familia… en Celaya» (Zona Franca, sin fecha): otro hecho, no se integra."),
 dict(id="ARG-149-005", estado="MX-SLP", region="Noreste", color="rojo", impacto="grande", fecha="2026-11-07", hora="tarde del 7 (solo por resumen); localizado el 8", mu=0, he=0, cu=0, hk=18,
  ent="San Luis Potosí / Zacatecas", mun="Carretera San Tiburcio–Vanegas (lugar disputado)", dia="7-NOV, SOLO POR RESUMEN; 8-NOV, POR RUTA",
  title="SAN LUIS POTOSÍ / ZACATECAS — SECUESTRAN AL ALCALDE DE RÍO BRAVO, TAMAULIPAS; LOCALIZADO CON VIDA EN COAHUILA",
  hecho="Alcalde de Río Bravo, Tamps. · secuestrado en carretera, en ruta a Real de Catorce, " + RES + " · <code>LUGAR DISPUTADO</code>: SLP (fiscalías de Tamaulipas y Zacatecas) o Zacatecas (SSP de SLP), " + RES + " · sábado 7-NOV, tarde, " + RES + " · <b>localizado con vida el domingo 8-NOV</b>, por ruta y titular (La Jornada 2026/11/08: «localizan a alcalde de Río Bravo, Tamaulipas, tras operativo de Gabinete de Seguridad»; El Financiero 2026/11/08) · <code>VERSIÓN CONTRADICHA</code>: «rescatado» en filtro de la Policía Estatal de Coahuila, " + RES + ", frente a «escapó aprovechando un descuido», por titular (Proceso 2026/11/8) · 🔴 secuestro de servidor público · " + NOD + " · acompañantes: situación no publicada",
  panel="<b>Secuestro del alcalde de Río Bravo</b>; localizado con vida en Coahuila", inst=SB, nac="La Jornada · El Financiero · Proceso · La Silla Rota", conf="★★★☆☆",
  campo="día y hora del secuestro solo por resumen; lugar y modo de la localización contradichos; declaración del secretario solo a través del titular de un medio", I=0, N=4, R=3, A=0,
  fechadas=["La Jornada (2026/11/08)", "El Financiero (2026/11/08)", "Proceso (2026/11/8)", "La Silla Rota (2026/11/8)"], estatus="Parcialmente corroborado", arm=None,
  desl="Río Bravo en el índice: ARG-139-REC-001 (diputada herida, 10-oct) y ARG-144-008 (bloqueos, 29-oct): otros hechos. Se asigna a SLP en el mapa por la versión de dos fiscalías; reserva de lugar. Localización con vida: no se abre ficha verde por la contradicción rescate/fuga."),
 dict(id="ARG-149-006", estado="MX-SIN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-08", hora="no fijada", mu=0, he=0, cu=6, hk=12,
  ent="Sinaloa", mun="Mazatlán (Libramiento Mazatlán–Villa Unión)", dia="8-NOV, POR RUTA",
  title="SINALOA · MAZATLÁN — COLECTIVO LOCALIZA SEIS CUERPOS JUNTO AL LIBRAMIENTO MAZATLÁN–VILLA UNIÓN",
  hecho="Mazatlán · <code>PREDIO JUNTO AL LIBRAMIENTO MAZATLÁN–VILLA UNIÓN, POR TITULAR</code> · domingo 8-NOV, por ruta (Línea Directa 2026-11-08: «localizan seis cuerpos en avanzado estado de descomposición en terreno del libramiento de Mazatlán») · hora no fijada · <b>6 cuerpos</b>, por titular; hombres, " + RES + " · colectivo Por las Voces sin Justicia, tras aviso anónimo, con la Comisión Estatal de Búsqueda y policía municipal, " + RES + " · <code>«FOSA» O «EN SUPERFICIE»: CONTRADICHO</code> (La Silla Rota 2026/11/9 titula «fosa clandestina»; otros, predio) (🔴 hallazgo de restos) · causa de muerte: no informada · chaleco táctico, cartuchos y cargadores sin cifra, " + RES,
  panel="<b>6 cuerpos localizados por un colectivo</b> junto al libramiento", inst=SB, nac="La Silla Rota · López Dóriga", conf="★★★☆☆",
  campo="enterramiento y ubicación exacta contradichos; ninguna fuente institucional («la Fiscalía abre investigación» no es declaración)", I=0, N=2, R=3, A=0,
  fechadas=["Línea Directa (2026-11-08)", "Síntesis (2026/11/09)", "Proyecto Puente (2026/11/09)", "La Silla Rota (2026/11/9)"], estatus="Parcialmente corroborado", arm=None,
  desl="Libramiento de Mazatlán no figura en las cinco ediciones previas. Cuerpos sin causa de muerte informada: van a «cuerpos o restos», no a muertos por agresión."),
 dict(id="ARG-149-007", estado="MX-SIN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-07", hora="noche (solo por resumen)", mu=2, he=0, cu=0, hk=21,
  ent="Sinaloa", mun="Culiacán (Ampliación 5 de Febrero)", dia="7-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — ATAQUE ARMADO EN LA AMPLIACIÓN 5 DE FEBRERO: DOS HOMBRES MUERTOS",
  hecho="Culiacán · <code>AMPLIACIÓN 5 DE FEBRERO, CALLE PLAN DE AYALA</code> · sábado 7-NOV, por ruta (Línea Directa 2026-11-07: «dos hombres son privados de la vida a balazos en la Ampliación 5 de Febrero»; Luz Noticias 2026-11-07: «doble homicidio») · noche, " + RES + " · <b>2 hombres muertos</b>, por titular (🔴 homicidio múltiple) · edades contradichas entre notas · Ejército como primer respondiente, " + RES + " · «dos pistolas» junto a una víctima, " + RES + ": no se integra · " + NOD,
  panel="<b>Doble homicidio a balazos</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Línea Directa (2026-11-07)", "Luz Noticias (2026-11-07)"], estatus="Parcialmente corroborado", arm=None,
  desl="«Seis hombres asesinados en Culiacán durante el fin de semana» (Diario de Yucatán 2026/11/08; El Universal): recuento de medios, no se integra ni se reparte. «Ataque armado en Culiacán deja cuatro muertos» (López Dóriga): hecho del 12-oct, otra ventana."),
 # ======================= AMARILLOS
 dict(id="ARG-149-008", estado="MX-GUA", region="Occidente", color="amarillo", impacto="mediano", fecha="2026-11-08", hora="madrugada (solo por resumen)", mu=1, he=2, cu=0, hk=3,
  ent="Guanajuato", mun="Irapuato (Las Huertas 1.ª Sección)", dia="8-NOV, POR RUTA",
  title="GUANAJUATO · IRAPUATO — ATAQUE ARMADO EN LAS HUERTAS: UN MUERTO Y DOS HERIDOS",
  hecho="Irapuato · <code>LAS HUERTAS PRIMERA SECCIÓN, POR TITULAR</code> · domingo 8-NOV, por ruta (Correo 2026/nov/08: «ataque deja un muerto y 2 heridos») · madrugada, " + RES + " · <b>1 muerto y 2 heridos</b>, por titular (🟡 homicidio doloso único) · " + NOD,
  panel="Ataque armado: <b>1 muerto y 2 heridos</b>", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=1, A=0,
  fechadas=["Correo (2026/nov/08)"], estatus="Parcialmente corroborado", arm=None,
  desl="Las Huertas de Irapuato no figura en las cinco ediciones previas («Huertas de Los Fresnos», Tancítaro: otro lugar)."),
 dict(id="ARG-149-009", estado="MX-CHH", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-08", hora="tarde (solo por resumen)", mu=1, he=1, cu=0, hk=16,
  ent="Chihuahua", mun="Chihuahua (Granjas Cerro Grande)", dia="8-NOV, POR RUTA",
  title="CHIHUAHUA · CHIHUAHUA — ATAQUE ARMADO EN GRANJAS CERRO GRANDE: UN MUERTO Y UN HERIDO",
  hecho="Chihuahua · <code>GRANJAS / VISTAS CERRO GRANDE</code>, " + RES + " · domingo 8-NOV, por ruta (El Diario de Chihuahua 2026/nov/08: «ataque armado deja un muerto y un herido»; En Blanco y Negro 2026/11/08) · tarde, " + RES + " · <b>1 muerto y 1 herido</b>, por titular · «acribillan a 2 en Granjas Cerro Grande», por titular (El Pueblo 20261108): <code>SALDO CONTRADICHO</code> (🟡 homicidio doloso único; si fueran 2 muertos, 🔴) · casquillos 9 mm sin cifra fija, " + RES + " · " + NOD,
  panel="Ataque armado: <b>1 muerto y 1 herido</b> (saldo contradicho)", inst=SB, nac="—", conf="★★★☆☆",
  campo="saldo contradicho entre titulares; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["El Diario de Chihuahua (2026/nov/08)", "En Blanco y Negro (2026/11/08)"], estatus="Parcialmente corroborado", arm=None,
  desl="La pista inicial lo situaba el sábado: la ruta lo fija el domingo 8."),
 dict(id="ARG-149-010", estado="MX-SON", region="Noroeste", color="amarillo", impacto="pequeño", fecha="2026-11-07", hora="mañana (solo por resumen)", mu=1, he=0, cu=0, hk=9,
  ent="Sonora", mun="Hermosillo (col. El Mariachi)", dia="7-NOV, POR RUTA",
  title="SONORA · HERMOSILLO — HALLAN A UN HOMBRE ASESINADO A BALAZOS EN LA ENTRADA DE UN DOMICILIO",
  hecho="Hermosillo · <code>COL. EL MARIACHI</code>, " + RES + " · sábado 7-NOV, por ruta (Proyecto Puente 2026/11/07: «hallan a hombre asesinado a balazos en la entrada de un domicilio») · mañana, " + RES + " · <b>1 muerto</b> (🟡 homicidio doloso único) · " + FU + " · " + NOD,
  panel="<b>Hombre asesinado a balazos</b> en la entrada de su domicilio", inst=SB, nac="—", conf="★★☆☆☆",
  campo="fuente única; colonia y hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Proyecto Puente (2026/11/07)"], estatus="Pendiente de corroboración", arm=None,
  desl="Herido en Puerta del Rey (Hermosillo), solo por resumen y sin fuente propia: no se integra."),
 dict(id="ARG-149-011", estado="MX-BCN", region="Noroeste", color="amarillo", impacto="pequeño", fecha="2026-11-06", hora="tarde (solo por resumen)", mu=1, he=0, cu=0, hk=16,
  ent="Baja California", mun="Tijuana (Rancho Las Flores)", dia="6 O 7-NOV; PUB. 7-NOV, POR RUTA",
  fecha_txt="vie 6-nov, " + "<code>DÍA SOLO POR RESUMEN</code>" + "; publicación 7-nov, por ruta",
  title="BAJA CALIFORNIA · TIJUANA — ASESINAN A BALAZOS A UN HOMBRE EN RANCHO LAS FLORES",
  hecho="Tijuana · <code>RANCHO LAS FLORES, POR TITULAR</code> · publicación 7-NOV, por ruta (Periodismo Negro 2026/11/07) · viernes 6-NOV, tarde, " + RES + " · " + DSR + " · <b>1 muerto</b>, hombre de unos 60 años, " + RES + " (🟡 homicidio doloso único) · " + FU + " · " + NOD,
  panel="<b>Hombre asesinado a balazos</b>", inst=SB, nac="—", conf="★★☆☆☆",
  campo="fuente única; día del hecho solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Periodismo Negro (2026/11/07)"], estatus="Pendiente de corroboración", arm=None,
  desl="Barbería de la Zona Centro: 4-nov, ventana de ARGOS 147, visto. Ningún hecho de Rancho Las Flores en las cinco ediciones previas."),
 dict(id="ARG-149-012", estado="MX-OAX", region="Sureste", color="amarillo", impacto="mediano", fecha="2026-11-07", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Oaxaca", mun="Juchitán de Zaragoza", dia="7-NOV, POR RUTA",
  title="OAXACA · JUCHITÁN — ATACAN A BALAZOS EL RESTAURANTE DE UN PERIODISTA CON PROTECCIÓN FEDERAL",
  hecho="Juchitán · restaurante de un periodista incorporado al mecanismo federal de protección, por titular (José Cárdenas 2026/11: «atacan a balazos restaurante de periodista bajo protección federal en Oaxaca») · publicación 7-NOV, por ruta (Vanguardia 2026/11/07) · día del hecho: 7-NOV o noche del 6, " + RES + " · disparos contra la fachada; <b>sin heridos</b>, " + RES + " (🟡 agresión sin víctimas; blanco: periodista) · la FGEO abrió investigación, " + RES + " · el periodista anunció el cierre del negocio, por titular (El Universal Oaxaca) · " + NOD,
  panel="<b>Disparos contra el restaurante de un periodista protegido</b>; sin heridos", inst=SB, nac="El Universal · José Cárdenas", conf="★★★☆☆",
  campo="día del hecho y ausencia de heridos solo por resumen; ninguna fuente institucional", I=0, N=2, R=0, A=0,
  fechadas=["Vanguardia (2026/11/07)"], estatus="Parcialmente corroborado", arm=None,
  desl="Juchitán en el índice (ARG-125-018, ARG-138-001, ARG-139-003): otros hechos. Sin víctimas: no sube a 🔴; agresión contra periodista declarada. Identidad: medios, no se reproduce."),
 dict(id="ARG-149-013", estado="MX-VER", region="Golfo", color="amarillo", impacto="pequeño", fecha="2026-11-09", hora="no fijada", mu=1, he=0, cu=0, hk=8,
  ent="Veracruz", mun="Cosoleacaque (fracc. Los Prados)", dia="9-NOV, POR RUTA",
  title="VERACRUZ · COSOLEACAQUE — ASESINAN A BALAZOS A UN JOVEN EN EL FRACCIONAMIENTO LOS PRADOS",
  hecho="Cosoleacaque · <code>FRACC. LOS PRADOS, POR TITULAR</code> · lunes 9-NOV, por ruta (La Aldea de la Información 2026/11/09: «tenía 23 años y lo asesinaron a balazos frente a una vivienda en Cosoleacaque») · " + FR + " · <b>1 muerto</b>, por titular (🟡 homicidio doloso único) · «diez disparos», por titular (N+) · edad 23 o «unos 20», contradicha · " + NOD,
  panel="<b>Joven asesinado a balazos</b>", inst=SB, nac="N+", conf="★★★☆☆",
  campo="hora no fijada (frontera de ventana); ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["La Aldea de la Información (2026/11/09)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cosoleacaque en el índice (ARG-105-REC-004, ARG-140-018, ARG-141-003): otros hechos, otras fechas."),
 # ======================= VERDES
 dict(id="ARG-149-014", estado="MX-PUE", region="Centro", color="verde", impacto="grande", fecha="2026-11-06", hora="anuncio por la mañana (solo por resumen)", mu=0, he=0, cu=0, hk=7,
  ent="Puebla", mun="Tlachichuca (Agua Escondida El Salitrero)", dia="ANUNCIO 6-NOV, POR RUTA",
  fecha_txt="día del hecho no fijado; anuncio 6-nov, por ruta",
  title="PUEBLA · TLACHICHUCA — DESMANTELAN UN NARCOLABORATORIO DE ONCE ZONAS",
  hecho="Tlachichuca · <code>AGUA ESCONDIDA EL SALITRERO</code>, " + RES + " · anuncio del secretario de Seguridad el viernes 6-NOV por la mañana, " + RES + "; publicación 6-NOV, por ruta (Lo de Hoy 2026/11/06: «desmantelan narcolaboratorio en Puebla y en Sinaloa; estiman golpe de 4 mil…») · " + AP + " · " + RET + " · día del hecho: no fijado · laboratorio de 11 zonas, 587 costales con precursores, " + RES + " · <b>afectación estimada de 4,132 millones de pesos</b>, cifra del Gabinete por titular (Puebla Roja): estimación, no aseguramiento · corporación contradicha (Ejército o fuerzas federales y estatales), " + RES + " · «tres armas largas», una sola nota, " + RES + ": no se integra · " + NOD,
  panel="<b>Narcolaboratorio de 11 zonas desmantelado</b>; 4,132 mdp de afectación estimada", inst=SB, nac="24 Horas", conf="★★★☆☆",
  campo="día del hecho no fijado; corporación contradicha; declaración del secretario solo a través de medios", I=0, N=1, R=4, A=0,
  fechadas=["Lo de Hoy (2026/11/06)", "Síntesis (2026/11/08)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — «tres armas largas» de una sola nota, solo por resumen; laboratorio, no aseguramiento de armamento",
  desl="Boletín federal del 5-nov (Milenio: «Tlachichuca… 4,132 millones»): <b>mismo hecho</b>; si el operativo es anterior a las 07:30 del 6, es de la ventana de ARGOS 148 (cláusula). El laboratorio de Sinaloa del mismo titular: sin datos propios, no se ficha. Atempan (ARG-149-015): otro laboratorio, otro municipio."),
 dict(id="ARG-149-015", estado="MX-PUE", region="Centro", color="verde", impacto="grande", fecha="2026-11-06", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Puebla", mun="Atempan", dia="6-NOV, SOLO POR RESUMEN; PUB. 8-NOV, POR RUTA",
  fecha_txt="vie 6-nov, <code>DÍA SOLO POR RESUMEN</code>; publicación 8-nov, por ruta",
  title="PUEBLA · ATEMPAN — MARINA DESMANTELA UN LABORATORIO: 650 KILOS DE METANFETAMINA EN ELABORACIÓN Y DOS DETENIDOS",
  hecho="Atempan · Marina en operativo con FGR y fuerzas estatales y municipales, por comunicado (gob.mx/sspc, ruta sin fecha: «Marina en operativo interinstitucional detiene a dos personas y asegura 650 kilos de metanfetamina en un laboratorio clandestino en Puebla») · día del hecho: viernes 6-NOV, " + RES + " · " + DSR + " · publicación 8-NOV, por ruta (Infobae 2026/11/08; Latinus 2026/11/8; Retodiario 2026/11/08) · <b>2 detenidos</b>, por comunicado · <b>650 kg de metanfetamina en elaboración</b>, por titular · 1,200 L de ácido fenilacético, 275 kg de cloro y 425 kg de ácido tartárico, " + RES + " · armas: ninguna publicada",
  panel="<b>Laboratorio desmantelado: 650 kg de metanfetamina en elaboración; 2 detenidos</b>", inst="Marina / SSPC (comunicado; texto no leído)", nac="Infobae · Latinus · Excélsior", conf="★★★☆☆",
  campo="día del hecho solo por resumen; comunicado no leído íntegro", I=1, N=3, R=1, A=0,
  fechadas=["Infobae (2026/11/08)", "Latinus (2026/11/8)", "Retodiario (2026/11/08)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — aseguramiento de droga y precursores, no de armamento",
  desl="La Marina precisó que no es Tlachichuca, " + RES + ": dos laboratorios distintos (ARG-149-014). «Más de 4,570 mdp» por los dos (Puebla Online): suma de un medio, no se integra."),
 dict(id="ARG-149-016", estado="MX-MIC", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-08", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Michoacán", mun="Buenavista", dia="PUB. 8-NOV, POR RUTA; DÍA NO FIJADO",
  fecha_txt="publicación 8-nov, por ruta; día del cateo no fijado",
  title="MICHOACÁN · BUENAVISTA — FGE LOCALIZA SIETE EXPLOSIVOS PARA DRONES EN UN CATEO",
  hecho="Buenavista · FGE, con Guardia Civil y GN, cateo por robo de motocicletas, por titular (La Voz de Michoacán: «FGE localiza siete explosivos para drones y asegura cinco motocicletas en Buenavista») · publicación 8-NOV, por ruta (Changoonga 2026/11/08) · día del cateo: no fijado · <code>EVENTO DE FECHA NO FIJADA PUBLICADO DURANTE EL CORTE</code> · <b>7 explosivos de fabricación casera para lanzarse desde drones</b> y <b>5 motocicletas</b>, por titular · desactivados y destruidos, " + RES + " · capacidad explosiva: no dictaminada · " + NOD,
  panel="<b>7 explosivos caseros para drones</b> y 5 motocicletas asegurados en un cateo", inst=SB, nac="—", conf="★★★☆☆",
  campo="día del cateo no fijado; comunicado de la FGE solo a través de medios", I=0, N=0, R=5, A=0,
  fechadas=["Changoonga (2026/11/08)"], estatus="Parcialmente corroborado", arm="ARG-149-ARM-002",
  desl="Buenavista en el índice: otros hechos de ediciones anteriores. Si el cateo es anterior a la ventana, se retira del total por fe de erratas."),
 dict(id="ARG-149-017", estado="MX-BCN", region="Noroeste", color="verde", impacto="pequeño", fecha="2026-11-08", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Baja California", mun="Tecate (col. Emiliano Zapata)", dia="8-NOV, POR RUTA",
  title="BAJA CALIFORNIA · TECATE — FESC Y MARINA ASEGURAN DOS FUSILES ABASTECIDOS",
  hecho="Tecate · <code>COL. EMILIANO ZAPATA, POR TITULAR</code> · operativo «Unidos por Tecate», " + RES + " · publicación 8-NOV, por ruta (El Imparcial 2026/11/08: «aseguran FESC y Marina armas largas en colonia de Tecate»; En Línea BC 2026/11/08) · <b>2 armas largas</b>, por titular (Uniradio: «dos fusiles abastecidos») · cargadores y 60 cartuchos .223, " + RES + ": n/d · " + NOD,
  panel="<b>2 fusiles abastecidos asegurados</b>", inst=SB, nac="—", conf="★★★☆☆",
  campo="día del hallazgo fijado por publicación; cartuchos y cargadores solo por resumen; ninguna fuente institucional leída", I=0, N=0, R=3, A=0,
  fechadas=["El Imparcial (2026/11/08)", "En Línea BC (2026/11/08)"], estatus="Parcialmente corroborado", arm="ARG-149-ARM-001",
  desl="Cinco homicidios del 6-nov en Tecate: recuento por titular (El Congresista) de hechos separados con composición no resuelta: va a «rojos sin ruta», no a esta ficha."),
 dict(id="ARG-149-018", estado="MX-JAL", region="Occidente", color="verde", impacto="grande", fecha="2026-11-09", hora="no fijada", mu=0, he=0, cu=0, hk=10,
  ent="Jalisco", mun="Zapopan", dia="PUB. 9-NOV, POR RUTA; DÍA NO FIJADO",
  fecha_txt="publicación 9-nov, por ruta; día del operativo no fijado",
  title="JALISCO · ZAPOPAN — DETIENEN A «R2», LÍDER DE LOS RS, Y A OTRAS 19 PERSONAS TRAS UN ENFRENTAMIENTO",
  hecho="Zapopan · restaurante, " + RES + " · publicación 9-NOV, por ruta (Infobae 2026/11/09: «México detiene a un líder criminal y a otras 19 personas tras tiroteo en el oeste del país»; Quinto Poder 2026/11/09: «la caída del R2, líder de Los Rs, en Zapopan») · " + FR + " · día del operativo: no fijado · <b>1 líder y 19 personas detenidas</b>, por titular · soldado herido, " + RES + " · Gabinete de Seguridad y Semar como emisores, " + RES + " · armamento: no publicado",
  panel="<b>Detenido «R2», líder de Los Rs, y 19 personas más</b> tras enfrentamiento", inst=SB, nac="Infobae · Quinto Poder", conf="★★★☆☆",
  campo="día del operativo no fijado; quién inició el enfrentamiento no acreditado; emisor solo por resumen", I=0, N=2, R=1, A=0,
  fechadas=["Infobae (2026/11/09)", "Quinto Poder (2026/11/09)"], estatus="Parcialmente corroborado", arm=None,
  desl="<code>ENFRENTAMIENTO SIN FICHA PROPIA HASTA FIJAR SU DÍA</code>: si cae en la ventana, se abre ficha aparte (🟡 si inició la autoridad; 🔴 si el grupo atacó a personal en patrullaje). Zapopan sin coincidencia en las cinco ediciones previas."),
 dict(id="ARG-149-019", estado="MX-GRO", region="Sureste", color="verde", impacto="grande", fecha="2026-11-09", hora="no fijada", mu=0, he=0, cu=0, hk=9,
  ent="Guerrero", mun="Acapulco (aguas del Pacífico)", dia="9-NOV, POR RUTA",
  title="GUERRERO · ACAPULCO — MARINA INTERCEPTA UNA EMBARCACIÓN CON CERCA DE UNA TONELADA DE COCAÍNA: SEIS DETENIDOS",
  hecho="Pacífico frente a Acapulco · Semar, por titular (Infobae 2026/11/09: «la Marina intercepta embarcación con una tonelada de cocaína en costas de Guerrero»; Proceso 2026/11/9; La Razón 2026/11/09; MVS 2026/11/9) · " + FR + " · día de la operación: no fijado · <b>6 detenidos</b>, por titular · 24 bultos, cerca de una tonelada, peso ministerial pendiente, " + RES + " · anunciado por el secretario de Seguridad, " + RES + " · a disposición de la FGR, " + RES,
  panel="<b>Cerca de una tonelada de cocaína en una embarcación; 6 detenidos</b>", inst=SB, nac="Infobae · Proceso · La Razón · MVS", conf="★★★☆☆",
  campo="día de la operación no fijado; comunicado de la Semar solo a través de medios", I=0, N=4, R=1, A=0,
  fechadas=["Infobae (2026/11/09)", "Proceso (2026/11/9)", "La Razón (2026/11/09)", "MVS (2026/11/9)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — aseguramiento de droga, no de armamento",
  desl="No es ARG-148-009 (Chiapas y Oaxaca, 5-nov, 1 detenido): otro día, otra zona, otra cifra. Republicaciones del mismo comunicado: una fuente."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = []
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ND_ALL = list(range(10))
ARM = [
 dict(id="ARG-149-ARM-001", ficha="ARG-149-017", estado="MX-BCN", region="Noroeste", color="verde", ent="Baja California", mun="Tecate (col. Emiliano Zapata)",
  fecha="2026-11-08", fecha_txt="pub. 8-nov, por ruta", hora="no fijada", c=[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], nd=[0, 2, 3, 4, 5, 6, 7, 8, 9], integra=True,
  corp="FESC y Marina <span class=\"muted-note\">(por titular de medios)</span>", conf="Bajo",
  nota="2 largas por titular; cargadores y 60 cartuchos .223, solo por resumen: n/d; ningún detenido publicado; ver ARG-149-017",
  fuentes=["El Imparcial (2026/11/08)", "En Línea BC (2026/11/08)", "Uniradio (sin fecha en la ruta)"]),
 dict(id="ARG-149-ARM-002", ficha="ARG-149-016", estado="MX-MIC", region="Occidente", color="verde", ent="Michoacán", mun="Buenavista",
  fecha="2026-11-08", fecha_txt="pub. 8-nov; día del cateo no fijado", hora="no fijada", c=[0, 0, 0, 0, 0, 0, 0, 7, 0, 0], nd=[0, 1, 2, 3, 4, 5, 6, 8, 9], integra=True,
  corp="FGE Michoacán, Guardia Civil y GN <span class=\"muted-note\">(por titular de medios)</span>", conf="Bajo",
  nota="7 explosivos caseros para lanzarse desde drones, por titular: se clasifican como AEI (artefacto para dron), capacidad no dictaminada; 5 motocicletas; sin armas ni detenidos publicados; día no fijado: si es anterior a la ventana, se retira; ver ARG-149-016",
  fuentes=["Changoonga (2026/11/08)", "La Voz de Michoacán (sin fecha en la ruta)", "A Tiempo (sin fecha en la ruta)"]),
]

TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
# sin ningún evento con cifra integrable no hay total verificable: todas las categorías n/d
ND = [True] * 10 if not any(a["integra"] for a in ARM) else [all(i in a.get("nd", []) for a in ARM if a["integra"]) for i in range(10)]
def tv(i, f=str): return "n/d" if ND[i] else f(TOT[i])
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["estado"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R); CU_REC = sum(r["cu"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
NRET = sum(1 for e in E if "SE RETIRA DE ESTE TOTAL" in e["hecho"])
HORAS = 80 + 37 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 2, 0, 0, 0, 0, 0, 7, 0, 0], (TOT, ND)
assert ND == [True, False, True, True, True, True, True, False, True, True], ND
assert cnt == {"rojo": 7, "amarillo": 6, "verde": 6}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (14, 9, 6, 0, 0, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,24", DENS
assert (NAP, NFR, NRET) == (1, 3, 1), (NAP, NFR, NRET)
assert len(ENT) == 12 and len(ENT_ROJO) == 3, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-149-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-149-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-11-06" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-11-06", x["id"]
    assert x["conf"] != "★★★☆☆" or len(x["fechadas"]) + (x["N"] + x["R"]) >= 2, x["id"]

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
    c = [("n/d" if i in a.get("nd", []) else v) for i, v in enumerate(a["c"])]
    return {"id": a["id"], "estado": a["estado"], "region": a["region"], "color": a["color"], "impacto": "grande" if sum(a["c"]) > 30 else "mediano",
            "hecho": f'{a["mun"]}, {a["ent"]}: {c[0]} cortas, {c[1]} largas, {c[2]} sin categoría, {c[3]} especial, {c[4]} cartuchos, {c[5]} cargadores, {c[6]} granadas, {c[7]} AEI, {c[8]} explosivos, {c[9]} detenidos. {a["corp"]}. {a["nota"]}. Ficha: {a["ficha"]}. Confianza {a["conf"]}',
            "fuentes": a["fuentes"], "confianza": a["conf"], "fecha": a["fecha"], "hora": a["hora"]}

# ================================================================= PÁGINAS
tpl = open(sys.argv[1], encoding="utf-8").read()
head = tpl[:tpl.index("<body>") + len("<body>")] + "\n"
head = head.replace("<title>ARGOS 148 — Reporte Nacional de Seguridad — 2026-11-06</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA DEFENSA Y A LA FGE DE GUANAJUATO EL PARTE DE VALTIERRILLA —ARMAMENTO, CALIBRES Y CÉLULA PROBABLE— Y COTÉJELO CON EL ATAQUE AL POLICÍA DE SAN FRANCISCO DEL RINCÓN</b> (ARG-149-001 y -002).
      <br><b>2. SOLICITE A LAS FISCALÍAS DE TAMAULIPAS, SAN LUIS POTOSÍ, ZACATECAS Y COAHUILA LA CARPETA DEL ALCALDE DE RÍO BRAVO: LUGAR DEL HECHO, AUTORES Y SITUACIÓN DE LOS ACOMPAÑANTES</b> (ARG-149-005).
      <br><b>3. SOLICITE A LA FGE DE SINALOA Y A LA COMISIÓN ESTATAL DE BÚSQUEDA LA IDENTIFICACIÓN Y LA CAUSA DE MUERTE DE LOS SEIS CUERPOS DE MAZATLÁN Y SU CRUCE CON FICHAS DE DESAPARICIÓN</b> (ARG-149-006).
      <br><b>4. SOLICITE A LA FGE DE MICHOACÁN EL DICTAMEN DE LOS SIETE EXPLOSIVOS PARA DRON DE BUENAVISTA Y LA FECHA DEL CATEO</b> (ARG-149-016).
      <br><b>5. SOLICITE A LA SSPC Y A LA SEMAR EL PARTE DE ZAPOPAN: DÍA DEL ENFRENTAMIENTO, QUIÉN INICIÓ Y ARMAMENTO ASEGURADO</b> (ARG-149-018).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>6-nov 07:30 → 9-nov 16:07 CDMX</b> (<b>{DUR}</b>; vie 6 · sáb 7 · dom 8 · lun 9) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>sin recuperaciones de alto impacto de la ventana anterior</b>
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
    <b>Armamento</b>: 2 armas largas (Tecate) y 7 artefactos explosivos para dron (Buenavista, día no fijado), confianza Bajo; ningún detenido en aseguramiento con cifra de autoridad · <b>muertos por agresión</b>: {MU}, cálculo propio de las fichas; <b>heridos</b>: {HE}, con la cifra menor donde hay contradicción (Valtierrilla 2 o 3) · <b>cuerpos</b>: 6 (Mazatlán), sin causa de muerte informada · <b>detenidos fuera de aseguramiento de armas</b>: Atempan 2, Zapopan 20, Acapulco 6, por titular o comunicado: fuera del conteo de armamento.
    <br><code>BALANCES, NO SE INTEGRAN NI SE REPARTEN</code>: <b>128 homicidios dolosos del 6 al 8-nov</b> (34, 50 y 44; Sinaloa 16, Guanajuato 13), cifras preliminares del Gabinete por titular de medio (Excélsior) · <b>281 homicidios del 2 al 8-nov</b>, SSPC por titular de medio (UnoTV) · «seis hombres asesinados en Culiacán el fin de semana» (Diario de Yucatán 2026/11/08) · «4 policías municipales asesinados en 3 semanas en Guanajuato» (Correo 2026/nov/09).
    <br><code>ROJOS SIN RUTA FECHADA — NO SON HECHOS DEL CORTE</code>: <b>San Juan Cacahuatepec, Oax.</b>: 2 muertos y 1 herido, domingo 8, {RES} · <b>Tecate, BC</b>: «cinco homicidios y una persona herida… el 6 de noviembre», por titular (El Congresista), en hechos separados de composición no resuelta (Los Encinos: 2 o 3 muertos) · <b>Huaquechula, Pue.</b>: «3 muertos y un herido», sin fecha · <b>Cañada Morelos, Pue.</b>: 2 muertos, sin fecha · <b>Monterrey, NL</b>: riña en taquería, 2 muertos, sábado 7, {RES} · <b>fosas y restos sin día</b>: Reynosa (Puerta Sur / Nuevo México), Nuevo Laredo (posible ARG-146-009), Viesca, Coah., Doctor Coss, NL.
    <br><b>Vistos, fuera de totales</b>: <b>de la ventana de ARGOS 148</b> (🟡, no se recuperan): Chilpancingo, Urvan, 1 muerto (5-nov 18:30, {RES}) · <b>sin ruta fechada</b> (🟡 o 🟢): Acapulco, Adobería y av. Cuauhtémoc · Centro, Tab., ranchería González (1 muerto; mañana o tarde del 6) · Espinal, Ver. (adolescente; 7 u 8) · Coronango, Pue. (mujer de 22 años) · Atencingo, mototaxista · Culiacán, San Rafael y Díaz Ordaz · Sanalona, Culiacán: «seis armas, mil 260 cartuchos», por titular sin fecha · Concordia y Escuinapa, Sin.: cifras no sostenidas · Celaya (San Isidro de Elguera) y Cerano, Gto.: {RES} · Indaparapeo: 6 detenidos por delitos contra la salud (8-nov), día no fijado · <b>evento anterior publicado durante el corte</b>: Tabasco, 21 detenidos (3 a 5-nov) · <b>Cuerámaro</b>: comandante muerto por disparo de su arma de cargo: no es homicidio acreditado.
    <br><code>FE DE ERRATAS — ARGOS 148</code>: <b>ARG-148-003 (Navolato) pasa de 🟡 a 🔴</b>: «agresión contra militares… confirma Harfuch» y «ataque al Ejército», por titular (PorEsto 2026/11/6; Luz Noticias 2026-11-06); el grupo atacó a personal en recorrido, {RES}; comunicado de Defensa no indexado · semáforo corregido de 148: <b>3 rojos, 2 amarillos, 4 verdes</b> (cálculo propio) · <b>ARG-148-008</b>: el tramo de Tacámbaro coincide con Pedernales (3-nov; RED Michoacán 2026/11/03): <code>POSIBLE DUPLICIDAD — SE RETIRA EL TRAMO DE TACÁMBARO</code>; sin efecto numérico (renglón cualitativo) · <b>ARG-148-002</b>: saldo fijado en <b>2 muertos</b> (la segunda víctima murió en clínica del IMSS; Síntesis y Diario Puntual 2026/11/05); hora sin fijar · <b>ARG-148-001</b>: se mantiene 🔴; la SSPH lo trata como «elemento de la Policía Estatal» fuera de servicio, {RES} · <b>ARG-148-006</b>: los 4 detenidos se atribuyen a la SSPH por titular (Plaza Juárez; PulsoSur) · <b>ARG-148-004</b>: segundo abatido confirmado por el Gabinete, {RES}; identidad no confirmada.
    <br><b>Seguimiento, fuera del semáforo</b>: <b>Matamoros (ARG-144-008)</b>: «Fiscalía de Tamaulipas investiga a tres policías por muerte de una niña», por titular (Infobae 2026/11/07); tirador no identificado · <b>«El Panda», Coatzacoalcos</b>: resultado de la audiencia del 9-nov no indexado · <b>ARG-147-001 (Cuernavaca)</b>: sin detenidos; piden que la FGR atraiga el caso (La Silla Rota 2026/11/9) · <b>ARG-146-011 (Mexicali)</b>: 26 fosas y 51 hallazgos, cifra de la fiscal, {RES} (Baja Post 2026/11/07: 27 cuerpos) · <b>ARG-147-004 (Indaparapeo)</b> y <b>ARG-147-REC-001 (Champotón)</b>: sin desarrollo.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-149-{i:03d}"]) for i in (1, 2, 3, 4))
co2 = "\n".join(ficha(byid[f"ARG-149-{i:03d}"]) for i in (5, 6, 7))
co2b = "\n".join(ficha(byid[f"ARG-149-{i:03d}"]) for i in (8, 9, 10, 11, 12, 13))
co2c = "\n".join(ficha(byid[f"ARG-149-{i:03d}"]) for i in (14, 15, 16, 17, 18, 19))
assert sorted(re.findall(r'id="(ARG-149-0\d\d)"', co1 + co2 + co2b + co2c)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
DSA = "ninguno con cifra publicada en Tecate ni en Buenavista · Atempan 2, Zapopan 20 y Acapulco 6: sin aseguramiento de armas, fuera de este conteo"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI),
 tile(1, "Armas largas", tv(1), "Tecate, por titular, confianza Bajo"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "Tecate: 60, solo por resumen"),
 tile(4, "Cargadores", tv(5), "Tecate: solo por resumen"),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), "Buenavista: explosivos caseros para dron, por titular; día no fijado"),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: " + DSA),
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
    <div class="map-caption">Baja California: 2 armas largas (Tecate) · Michoacán: 7 artefactos explosivos para dron (Buenavista).</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM)
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
    <b>Lectura regional</b>: Noroeste, 2 armas largas (Baja California); Occidente, 7 artefactos explosivos para dron (Michoacán); las demás regiones, sin arma integrada. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: ninguno integrado.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>Sanalona, Culiacán</b>: «seis armas, mil 260 cartuchos y cocaína», por titular (Meganoticias), desglose 3 cortas, 3 largas y 50 cargadores {RES}; día no fijado y sin ruta fechada · <b>Concordia, Sin.</b>: 2 largas, 87 cartuchos, 1 detenido, {RES} · <b>Escuinapa, Sin.</b>: cifras no sostenidas como de Escuinapa · <b>Celaya (San Isidro de Elguera) y Cerano, Gto.</b>: armas, cartuchos y «posibles artefactos explosivos», {RES}, sin ruta · <b>Tlachichuca</b>: «tres armas largas», una sola nota, {RES} · <b>Pachuca (ARG-148-006)</b>: «dos armas de fuego», {RES}: ventana de ARGOS 148 · <b>boletín federal del 5-nov</b>: ventana de ARGOS 148.
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
      <tr><td><b>Nuevo León</b><br>Apodaca</td><td>Tráfico de personas: 83 migrantes en un camión; <b>2 sentenciados</b>, por titular (ABC Noticias 2026/11/6: «sentencian a 2 hombres…»)</td><td>16 años 10 meses y multa, {RES}</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · sin boletín; publicado el día de apertura sin hora</td><td>Bajo</td></tr>
      <tr><td><b>Guanajuato</b></td><td>Portación de armas, cargadores, cartuchos e inhibidor (aseguramiento de 2015); <b>2 personas</b>, por titular (boletines.guanajuato.gob.mx 2026/11/06: «lleva FGR a prisión a dos personas…»)</td><td>«Más de 17 años», por titular (La Prensa de Coahuila 2026/11/07)</td><td>FGR <span class="muted-note">(boletín del gobierno estatal)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · el titular dice «lleva a prisión»; término expreso de condena no leído; publicado el día de apertura sin hora</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Ramos Arizpe</td><td>Robo de hidrocarburo; 1 sentenciado; procedimiento abreviado, {RES} (La Prensa de Coahuila 2026/11/08)</td><td>13 años 4 meses, por titular</td><td>FGR <span class="muted-note">(por medios)</span></td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · «13 años por robo de hidrocarburo en Coahuila» publicado el 19-oct (Argon México 2026/10/19)</td><td>Bajo</td></tr>
      <tr><td><b>Federal</b></td><td>«El Mochaorejas»: otros 50 años, por titular (La Prensa de Coahuila 2026/11/08)</td><td>50 años, por titular</td><td>FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · comunicado no leído; fecha de la resolución no fijada</td><td>Bajo</td></tr>
      <tr><td><b>Tab · Oax · Chis · NL · Coah · Zac · Jal · Pue · Edomex · Hgo · BC</b></td><td>Paraíso (FGR, exsubdirector; pena 2 años o 2 años 8 meses) · Oaxaca 157 años (boletín 2,948 sin URL individual) · Palenque 65 años · Los Ramones y Saltillo–Monclova (4-nov) · Fresnillo (octubre) · Jalisco, dos feminicidas (29-oct) · Huejotzingo (29-oct) · Ecatepec (28-oct) · Tulantepec (sin pena publicada) · Tecate y Mexicali · <b>candidatos anteriores</b></td><td>Ver ARGOS 147 y 148 · <code>HEREDADO — NO REVERIFICADO</code> salvo lo anotado</td><td>Fiscalías estatales y FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín del dominio; publicados antes de la ventana</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio · comunicados vistos solo en resúmenes y titulares de medios</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>21 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, BCS, Son, Chih, Sin, Dgo · NL, Zac, Coah · Jal, Col · CDMX, Edomex, Pue, Mor, Tlax · Ver, Tab · Oax, Chis, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>21</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio de la fiscalía no confirmado</b></td><td><b>1</b>: Camp · Coahuila: dominio hallado, <code>sitio.fgecoahuila.gob.mx</code></td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>11</b>: Tamps, SLP · Nay, Ags, Gto, Mich · Hgo, Qro · Gro, Camp, Yuc</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 9-nov 08:14: código <code>000</code> (proxy: conexión rechazada)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 19 entidades; solo consulta amplia en 13 —Son · NL, Zac, SLP · CDMX, Tlax, Qro · Ver, Tab · Gro, Camp, Yuc, QRoo— · <b>armamento: 17 de 32 por dominio oficial</b> —Sin, Dgo · Tamps, NL, Zac, SLP, Coah · Mich, Col · CDMX · Ver, Tab · Gro, Chis, Camp, Yuc, QRoo—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · <code>NO REVISADA</code> (15): BC, BCS, Son, Chih · Jal, Nay, Ags, Gto · Edomex, Pue, Mor, Tlax, Hgo, Qro · Oax</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 5-nov</b>: existe (Milenio; RED113; Tallapolítica): ventana de ARGOS 148; incluye Tlachichuca (ver ARG-149-014) · <b>acciones del 6, 7 y 8-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, rango y título, al inicio; repetición al cierre: pendiente · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 9-NOV 08:14: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Siete rojos propios en tres entidades</b> (cálculo propio): ataque a militares, policía asesinado, secuestro de un alcalde, tres homicidios múltiples y seis cuerpos localizados. 0,09 rojos por hora (7 en {DUR}), frente a 0,14 en ARGOS 148 corregido: <b>no comparable sin más</b> (cálculo propio).
      <br><b>2.</b> <b>Guanajuato concentra cuatro de los siete rojos</b> (ARG-149-001 a -004), en el corredor Salamanca–Valle de Santiago–Celaya y en San Francisco del Rincón.
      <br><b>3.</b> <b>Sinaloa</b> suma dos rojos (ARG-149-006 y -007) y el <b>Noreste</b> uno con lugar disputado entre San Luis Potosí y Zacatecas (ARG-149-005).
      <br><b>4.</b> <b>Violencia operativa</b>: seis amarillos en seis entidades, sin enfrentamientos con la fuerza pública fichados · <b>respuesta institucional</b>: seis verdes, entre ellos dos laboratorios en Puebla y cerca de una tonelada de cocaína frente a Guerrero; ninguna sentencia integrable (totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()} CON FIN DE SEMANA COMPLETO, 3,7 VECES LA DE ARGOS 148; TRES HECHOS EN FRONTERA DE VENTANA Y UNO CON CLÁUSULA DE RETIRO. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. GUANAJUATO, CORREDOR SALAMANCA–VALLE DE SANTIAGO–CELAYA: TRES ROJOS Y UN AMARILLO EN 48 HORAS, CON UNA EMBOSCADA CONTRA MILITARES</b> (ARG-149-001, -003, -004 y -008): ataques a viviendas y a familias con agresores en motocicleta; vínculo entre hechos no acreditado. Línea: <b>solicitar a la FGE de Guanajuato la balística comparada de los cuatro hechos</b>.
      <br><b>2. POLICÍAS MUNICIPALES DE GUANAJUATO ATACADOS AL SALIR DE TURNO O EN DESCANSO, EN SÁBADO</b> (ARG-149-002; cuatro en tres semanas por recuento de medios): consistente con seguimiento previo de la víctima; requiere validación. Línea: <b>solicitar a la SSC municipal el análisis de riesgo del personal en sus traslados</b>.
      <br><b>3. ALTIPLANO POTOSINO–ZACATECANO: SECUESTRO DE UN ALCALDE EN TRÁNSITO POR CARRETERA</b> (ARG-149-005): tramo San Tiburcio–Vanegas como punto de riesgo para servidores públicos en desplazamiento; autoría no establecida. Línea: <b>solicitar una carpeta única a las cuatro fiscalías y vigilar el tramo</b>.
      <br><b>4. SUR DE SINALOA: SEIS CUERPOS LOCALIZADOS POR UN COLECTIVO, NO POR LA AUTORIDAD</b> (ARG-149-006): la búsqueda ciudadana sigue anticipando hallazgos junto a vías primarias de Mazatlán; vínculo con desapariciones no acreditado. Línea: <b>solicitar la identificación genética y el cruce con el registro estatal de personas desaparecidas</b>.
      <br><b>5. PUEBLA: DOS LABORATORIOS DE METANFETAMINA EN EL ORIENTE DEL ESTADO EN UNA SOLA VENTANA</b> (ARG-149-014 y -015): consistente con producción sintética cerca del límite con Veracruz; vínculo entre ambos no acreditado. Línea: <b>solicitar a la FGR el origen y la ruta de ingreso del ácido fenilacético asegurado</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — cifras preliminares de homicidio del fin de semana solo a través de medios (ver panorama); lectura directa no disponible · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO EN GUANAJUATO", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO EN EL NORESTE Y SINALOA", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA", co2b)
 + page("CRIMEN ORGANIZADO (IV) — ACCIONES INSTITUCIONALES", co2c)
 + page("CONTEO NACIONAL DE ARMAMENTO Y ARTEFACTOS EXPLOSIVOS ASEGURADOS", arm1)
 + page("ARMAMENTO POR EVENTO — DESGLOSE CON TRAZABILIDAD", arm2)
 + page("RASTREO NACIONAL DE SENTENCIAS Y RESULTADOS JUDICIALES", sent)
 + page("VALORACIÓN ARGOS, CONCLUSIONES E INDICADORES", cierre)
 + "\n")

ev = ",\n".join("  " + json.dumps(ev_json(e), ensure_ascii=False) for e in sorted(E, key=lambda x: {"verde":0,"amarillo":1,"rojo":2}[x["color"]]) + R)
ea = ",\n".join("  " + json.dumps(arm_json(a), ensure_ascii=False) for a in ARM if a["integra"] and any(a["c"]))
script = re.sub(r'const CONSULTA_TXT = "[^"]*";', f'const CONSULTA_TXT = "{CONSULTA}";', script)
assert f'const CONSULTA_TXT = "{CONSULTA}";' in script
script = re.sub(r'const CORTE_FECHA = "[^"]*";', f'const CORTE_FECHA = "{FECHA}";', script)
script = re.sub(r'const EVENTOS = \[\n.*?\n\];', lambda m: "const EVENTOS = [\n" + ev + "\n];", script, flags=re.S)
script = re.sub(r'const EVENTOS_ARM = \[\n.*?\n\];', lambda m: "const EVENTOS_ARM = [\n" + ea + "\n];", script, flags=re.S)
# la ventana de 149 toca cuatro fechas de calendario (6, 7, 8 y 9-nov); la plantilla de 148 trae 2
assert script.count("WINDOW_DAYS = 2;") == 1, "plantilla de 148 con WINDOW_DAYS = 2"
script = script.replace("WINDOW_DAYS = 2;", "WINDOW_DAYS = 4;")
assert script.count("WINDOW_DAYS = 4;") == 1 and "WINDOW_DAYS = 2;" not in script
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
