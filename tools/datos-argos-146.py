# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 146.
Uso: python3 tools/datos-argos-146.py <plantilla ARGOS 145> <salida>
Ventana: 31-oct 11:14 → 4-nov 06:52 CDMX. Archivo: argos-2026-11-04.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "146", "2026-11-04", "06:52"
CONSULTA = "__CONSULTA__"
DUR = "91 h 38 min"
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
RET = "<code>SI RESULTA ANTERIOR A LAS 11:14 DEL 31, ES DE LA VENTANA DE ARGOS 145 Y SE RETIRA DE ESTE TOTAL</code>"
FU = "<code>FUENTE ÚNICA</code>"
DSR = "<code>DÍA SOLO POR RESUMEN</code>"
NOD = "<b>ningún detenido publicado</b>"
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos o restos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-146-001", estado="MX-CMX", region="Centro", color="rojo", impacto="grande", fecha="2026-11-01", hora="noche (solo por resumen)", mu=2, he=0, cu=0, hk=21,
  ent="Ciudad de México", mun="Cuauhtémoc (col. Morelos, Tepito)", dia="1-NOV, POR RUTA",
  title="CIUDAD DE MÉXICO · TEPITO — ASESINAN A UNA MUJER Y A SU HIJO MENOR MIENTRAS PEDÍAN CALAVERITA",
  hecho="Col. Morelos (Tepito) · <code>CRUCE DE PEÑÓN Y TENOCHTITLÁN, SOLO POR RESUMEN</code> · domingo 1-NOV, noche, por titular («Día de Muertos»: Tribuna 2026/11/02) · <b>2 muertos</b>: una mujer y <b>su hijo de 3 años</b>, por titular (El Gráfico 2026/11/02; Tribuna); «4 años», por titular (Publimetro 2026/11/03; Diario de Yucatán 2026/11/03): <code>EDAD CONTRADICHA</code> (🔴 homicidio múltiple; víctima menor) · «mientras pedían calaverita», por titular (Publimetro) · dos agresores en bicicleta eléctrica, " + RES + " · vínculo de la víctima con La Unión Tepito: por titular de medios (Infobae 2026/11/03; Publimetro), <b>no acreditado por autoridad</b> · SSC y FGJCDMX en el lugar, " + RES + ": no es declaración · " + NOD,
  panel="<b>Mujer y su hijo menor (3 o 4 años, contradicho) asesinados</b> en Día de Muertos", inst=SB, nac="El Financiero · Infobae · Publimetro · El Gráfico", conf="★★★☆☆",
  campo="hora solo por resumen; edad del niño contradicha; ninguna fuente institucional", I=0, N=4, R=3, A=0,
  fechadas=["Tribuna (2026/11/02)", "El Gráfico (2026/11/02)", "El Financiero (2026/11/02)", "Infobae (2026/11/02)", "Publimetro (2026/11/03)", "Diario de Yucatán (2026/11/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tepito en el índice: ARG-120-006 (16-sep, Rinconada y Toltecas, 2 mujeres muertas) y ARG-122-010 / ARG-122-ARM-004 (Iztapalapa, cateo vinculado a La Unión Tepito, 18-sep): otros hechos. Identidad y alias de la víctima: medios, no se reproducen."),
 dict(id="ARG-146-002", estado="MX-VER", region="Golfo", color="rojo", impacto="grande", fecha="2026-11-02", hora="noche, después de las 22:00 (solo por resumen)", mu=2, he=0, cu=0, hk=22,
  ent="Veracruz", mun="Chinameca (panteón municipal)", dia="2-NOV, POR TITULAR",
  title="VERACRUZ · CHINAMECA — ATAQUE ARMADO EN EL PANTEÓN MUNICIPAL DURANTE DÍA DE MUERTOS: DOS HOMBRES MUERTOS",
  hecho="Chinameca · <code>PANTEÓN MUNICIPAL, POR TITULAR</code> · lunes 2-NOV, noche, «durante las celebraciones de Día de Muertos», por titular (Diario de Yucatán 2026/11/03); después de las 22:00, " + RES + " · <b>2 hombres muertos</b>, por titular (Diario de Yucatán; Golpe Político 2026/11/03; Proyecto Puente 2026/11/03; La Silla Rota 2026/11/3: «asesinados»); primera versión «un muerto y un lesionado» (misma nota de La Silla Rota, actualizada): superada (🔴 homicidio múltiple en acto público) · ambos murieron en hospitales, " + RES + " · dos agresores en motocicleta, " + RES + " · festejos suspendidos, " + RES + " · la FGE abre carpeta, por titular (La Prensa de Coahuila 2026/11/03): no es declaración · " + NOD,
  panel="<b>Ataque en el panteón en Día de Muertos: 2 muertos</b>", inst=SB, nac="El Universal · N+ · La Silla Rota", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=3, R=5, A=0,
  fechadas=["La Silla Rota (2026/11/3)", "Diario de Yucatán (2026/11/03)", "Golpe Político (2026/11/03)", "Proyecto Puente (2026/11/03)", "La Prensa de Coahuila (2026/11/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Chinameca no figura en las cinco ediciones previas ni en el índice. Nombres y alias de las víctimas: medios, no se reproducen."),
 dict(id="ARG-146-003", estado="MX-GRO", region="Sureste", color="rojo", impacto="grande", fecha="2026-11-03", hora="madrugada, ~05:30 (solo por resumen)", mu=2, he=1, cu=0, hk=5.5,
  ent="Guerrero", mun="Acapulco (El Veintiuno, km 21)", dia="3-NOV, POR RUTA",
  title="GUERRERO · ACAPULCO — COMANDO IRRUMPE EN UNA FIESTA EN EL KILÓMETRO 21: DOS MUERTOS Y UN HERIDO",
  hecho="Acapulco · <code>EL VEINTIUNO (KM 21), CALLE LIBÉLULA, SOLO POR RESUMEN</code> · martes 3-NOV, por ruta (diario.mx 2026/nov/03) · madrugada, ~05:30, " + RES + " · <b>2 muertos</b> y <b>1 herido</b>, por titular (Quadratín Guerrero: «2 muertos y un herido»; diario.mx: «mata a dos») (🔴 homicidio múltiple) · «irrumpen hombres armados en una fiesta», por titular (Bajo Palabra) · víctimas, tío y sobrino, " + RES + " · " + NOD,
  panel="<b>Ataque a una fiesta: 2 muertos y 1 herido</b>", inst=SB, nac="La Silla Rota", conf="★★★☆☆",
  campo="hora y día (lunes o martes) solo por resumen; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["diario.mx (2026/nov/03)", "La Silla Rota (2026/11/3)"], estatus="Parcialmente corroborado", arm=None,
  desl="«El Veintiuno» (Quadratín) y «km 21» (Bajo Palabra): mismo hecho (calle, hora y saldo coinciden). La Silla Rota (2026/11/3) lo sitúa el lunes 2 por la noche: día contradicho, ambos dentro de la ventana. El herido, solo por el titular de Quadratín. No figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-146-004", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-02", hora="~01:00 (solo por resumen)", mu=3, he=0, cu=0, hk=1,
  ent="Guanajuato", mun="Celaya (col. Ejidal)", dia="2-NOV, POR RUTA",
  title="GUANAJUATO · CELAYA — ASESINAN A TRES HOMBRES EN UN ATAQUE ARMADO EN LA COLONIA EJIDAL",
  hecho="Celaya · <code>COL. EJIDAL, POR TITULAR (AM); CALLE EJIDO DEL BOSQUE, SOLO POR RESUMEN</code> · lunes 2-NOV, por ruta (AM 2026/11/02) · ~01:00, " + RES + " · <b>3 hombres muertos</b>, por titular (AM: «matan a 3 hombres») (🔴 homicidio múltiple); un balance de Correo da 1 muerto y 1 sobreviviente, " + RES + ": no se arbitra por resumen · " + NOD,
  panel="<b>Ataque armado: 3 hombres muertos</b> (saldo contradicho)", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única por titular; saldo contradicho por resumen", I=0, N=0, R=1, A=0,
  fechadas=["AM (2026/11/02)"], estatus="Pendiente de corroboración", arm=None,
  desl="Col. Ejidal no figura en las cinco ediciones previas ni en el índice. ARG-143-001 (Celaya, asalto intervenido por la SSPC): otro hecho. Los balances de Día de Muertos de Guanajuato (Correo 2026/nov/02: nueve; Latinus 2026/11/3: ocho) no se reparten ni se integran."),
 dict(id="ARG-146-005", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-02", hora="~21:10 (solo por resumen)", mu=3, he=0, cu=0, hk=21.2,
  ent="Guanajuato", mun="Silao (Monte del Coecillo)", dia="2-NOV, POR RUTA",
  title="GUANAJUATO · SILAO — ATAQUE ARMADO EN MONTE DEL COECILLO: TRES MUERTOS",
  hecho="Silao · <code>COMUNIDAD MONTE DEL COECILLO, POR TITULAR</code> · lunes 2-NOV, por ruta (Correo 2026/nov/02) · ~21:10, " + RES + " · «dos muertos y un lesionado», por titular (Correo); «muere tercera víctima», por titular (Noticieros en Línea 2026/nov/03): <b>3 muertos</b>, el tercero en hospital (🔴 homicidio múltiple) · «matan a tres personas», por titular (N+) · motociclistas armados huyeron, " + RES + " · " + NOD,
  panel="<b>Ataque armado en una comunidad: 3 muertos</b>", inst=SB, nac="N+", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["Correo (2026/nov/02)", "AM (2026/11/03)", "Noticieros en Línea (2026/nov/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Monte del Coecillo no figura en las cinco ediciones previas ni en el índice. El Escoplo, Silao («dos presuntos muertos», Correo 2026/nov/02) y «ataques simultáneos en Silao y Romita» (Milenio, sin fecha): posible relación no establecida; vistos, fuera de totales."),
 dict(id="ARG-146-006", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-11-04", fecha_txt="publicado el 2026-11-04 — DÍA Y HORA NO FIJADOS", hora="no fijada", mu=2, he=2, cu=0, hk=3,
  ent="Guanajuato", mun="Irapuato (col. Primavera)", dia="PUB. 4-NOV, POR RUTA",
  title="GUANAJUATO · IRAPUATO — ATAQUE ARMADO EN LA COLONIA PRIMAVERA: DOS MUERTOS Y DOS HERIDOS",
  hecho="Irapuato · <code>COL. PRIMAVERA, POR TITULAR</code> · publicado el miércoles 4-NOV, por ruta (Correo 2026/nov/04) · " + FR + " · <b>2 hombres muertos y 2 heridos</b>, por titular (Correo; Primer Plano Irapuato) (🔴 homicidio múltiple) · día y hora del ataque no publicados · " + NOD,
  panel="<b>Ataque armado: 2 muertos y 2 heridos</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día y hora no fijados; ninguna fuente institucional", I=0, N=0, R=2, A=0,
  fechadas=["Correo (2026/nov/04)", "Primer Plano Irapuato (2026/11/04)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Primavera de Irapuato no figura en las cinco ediciones previas ni en el índice (Primavera en el índice: Amecameca, ARG-119-005, otro hecho). Si la publicación del 4 corresponde a un hecho del 3, sigue siendo de esta ventana."),
 dict(id="ARG-146-007", estado="MX-MIC", region="Occidente", color="rojo", impacto="mediano", fecha="2026-11-02", hora="madrugada (solo por resumen)", mu=0, he=0, cu=0, hk=4,
  ent="Michoacán", mun="Uruapan (calz. Benito Juárez, col. Mártires)", dia="2-NOV, POR RUTA",
  title="MICHOACÁN · URUAPAN — DISPARAN DESDE UNA VIVIENDA CONTRA MILITARES",
  hecho="Uruapan · <code>CALZ. BENITO JUÁREZ, COL. MÁRTIRES, SOLO POR RESUMEN</code> · lunes 2-NOV, por ruta (Changoonga 2026/11/02) · madrugada, " + RES + " · «ataque armado contra elementos del Ejército», por <i>slug</i> (Changoonga) (🔴 el grupo agrede a personal militar) · disparos desde una vivienda contra militares en recorrido de vigilancia, " + RES + ": <code>PATRULLAJE SOLO POR RESUMEN</code> · <b>sin muertos ni heridos publicados</b> · detención de dos hombres: ficha propia, ARG-146-017",
  panel="<b>Agresión armada contra militares</b> desde una vivienda; sin víctimas publicadas", inst="Guardia Civil y Defensa" + PR, nac="El Universal", conf="★★★☆☆",
  campo="patrullaje y hora solo por resumen", I=0, N=1, R=4, A=0,
  fechadas=["Changoonga (2026/11/02)"], estatus="Parcialmente corroborado", arm=None, armtxt="armamento en ARG-146-017",
  desl="Calz. Benito Juárez de Uruapan: ARG-139-008 (restaurante baleado, 20-oct, sin víctimas): otro hecho. Delito y detención en la misma ventana: dos fichas."),
 dict(id="ARG-146-008", estado="MX-TAM", region="Noreste", color="rojo", impacto="mediano", fecha="2026-11-02", hora="~01:00 (solo por resumen)", mu=1, he=0, cu=0, hk=1,
  ent="Tamaulipas", mun="Reynosa (col. Los Muros)", dia="2-NOV, POR RUTA",
  title="TAMAULIPAS · REYNOSA — ASESINAN A UN ELEMENTO DE LA GUARDIA ESTATAL",
  hecho="Reynosa · <code>COL. LOS MUROS, POR <i>SLUG</i> (LA REGIÓN)</code> · lunes 2-NOV, por ruta (La Región 2026/11/02; CN Tamaulipas 2026/11/02) · ~01:00, " + RES + " · <b>1 muerto</b>: <b>elemento de la Guardia Estatal</b>, por titular (Elefante Blanco; Hoy Tamaulipas) (🔴 víctima autoridad) · en su día de descanso, " + RES + " · la FGJ investiga, " + RES + ": no es declaración · " + NOD,
  panel="<b>Elemento de la Guardia Estatal asesinado</b>", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=4, A=0,
  fechadas=["La Región (2026/11/02)", "CN Tamaulipas (2026/11/02)", "Elefante Blanco (2026/11/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Los Muros no figura en las cinco ediciones previas ni en el índice. Nombre de la víctima: una nota, no se reproduce."),
 dict(id="ARG-146-009", estado="MX-TAM", region="Noreste", color="rojo", impacto="mediano", fecha="2026-11-02", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Tamaulipas", mun="Nuevo Laredo", dia="2-NOV, POR TITULAR",
  title="TAMAULIPAS · NUEVO LAREDO — UN COLECTIVO LOCALIZA RESTOS ÓSEOS",
  hecho="Nuevo Laredo · lunes 2-NOV, por titular (N+, forma «hoy 2 de noviembre» de un solo hecho); publicado el 3-NOV, por ruta (Diario Puntual; Lo de Hoy 2026/11/03) · un colectivo de búsqueda <b>localiza restos óseos</b>, por titular (N+); ropa y llaveros para identificar los restos, por titular (Diario Puntual 2026/11/03) (🔴 restos humanos) · fosa clandestina no confirmada por autoridad, " + RES + " · <b>número de víctimas: no publicado</b> — <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · ninguna autoridad nombrada",
  panel="<b>Restos óseos</b> localizados por un colectivo; número no publicado", inst=SB, nac="N+", conf="★★★☆☆",
  campo="número de víctimas no publicado; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Diario Puntual (2026/11/03)", "Lo de Hoy (2026/11/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Nuevo Laredo en el índice: ARG-122-SEN-001 (sentencia, col. Sector Centro): otro hecho. Restos hallados sin causa de muerte informada por autoridad."),
 dict(id="ARG-146-010", estado="MX-SON", region="Noroeste", color="rojo", impacto="grande", fecha="2026-11-03", hora="jornada de búsqueda (solo por resumen)", mu=0, he=0, cu=4, hk=12,
  ent="Sonora", mun="Suaqui Grande", dia="3-NOV, POR RUTA",
  title="SONORA · SUAQUI GRANDE — BUSCADORAS LOCALIZAN UNA FOSA CLANDESTINA CON RESTOS DE CUATRO PERSONAS",
  hecho="Suaqui Grande · publicado el martes 3-NOV, por ruta (El Imparcial 2026/11/03; Proyecto Puente 2026/11/03) · colectivo Buscadoras por la Paz Sonora <b>localiza una fosa clandestina</b>, por titular (El Imparcial) · <b>restos de al menos 4 personas</b>, por titular (El Imparcial: «cuatro personas»; Proyecto Puente y Medios OBSON: «al menos cuatro»): cifra mínima (🔴 fosa) · cuatro o tres cráneos extraídos, " + RES + ": <code>CIFRA CONTRADICHA</code>; prevalece el mínimo del titular · día de la jornada, " + RES + " · peritos de la FGJE trasladaron los restos, " + RES + ": no es declaración · primera fosa hallada por un colectivo en la Sierra Baja, por titular de un medio regional",
  panel="<b>Fosa clandestina con restos de al menos 4 personas</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="cifra del colectivo, sin cifra oficial; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["El Imparcial (2026/11/03)", "Proyecto Puente (2026/11/03)", "Medios OBSON (2026/11/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Suaqui Grande no figura en las cinco ediciones previas ni en el índice. Restos hallados sin causa de muerte informada por autoridad."),
 dict(id="ARG-146-011", estado="MX-BCN", region="Noroeste", color="rojo", impacto="mediano", fecha="2026-11-02", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Baja California", mun="Mexicali (poblado Miguel Alemán)", dia="2-NOV, POR RUTA",
  title="BAJA CALIFORNIA · MEXICALI — NUEVA FOSA CLANDESTINA EN EL POBLADO MIGUEL ALEMÁN",
  hecho="Mexicali · <code>POBLADO MIGUEL ALEMÁN, POR TITULAR</code> · lunes 2-NOV, por ruta (El Imparcial 2026/11/02: «localizan una fosa más con restos humanos»; Periodismo Negro 2026/11/02) · <b>fosa clandestina con restos humanos</b>, por titular (Zeta; N+) (🔴 fosa) · segundo hallazgo de restos óseos el 3-NOV en jornada estatal, por titular (Zeta 2026/11; El Imparcial 2026/11/03) · «dos fosas clandestinas en el Valle de Mexicali», por titular (La Jornada 2026/11/04) · <b>número de víctimas: no publicado</b> — <code>CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO</code> · «49 cuerpos en 2026» (N+; Periodismo Negro) frente a «50 restos» (La Jornada, " + RES + "): recuento de medios, no se integra · la FGE no actualizó cifras, " + RES,
  panel="<b>Fosa con restos humanos</b> en el poblado Miguel Alemán y segundo hallazgo de restos óseos (3-nov); número no publicado", inst=SB, nac="La Jornada · N+", conf="★★★☆☆",
  campo="número de víctimas no publicado; ninguna fuente institucional", I=0, N=2, R=3, A=0,
  fechadas=["El Imparcial (2026/11/02)", "Periodismo Negro (2026/11/02)", "El Imparcial (2026/11/03)", "La Jornada (2026/11/04)"], estatus="Parcialmente corroborado", arm=None,
  desl="Miguel Alemán, Sin., en ARGOS 143 (aseguramiento en vistos): homónimo de otra entidad; sin ARG-ID previo de fosas en Mexicali. Segundo hallazgo del 3-nov y Cerro Centinela (posibles restos óseos, 3-nov, mismas fuentes): <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code>."),
 dict(id="ARG-146-012", estado="MX-MEX", region="Centro", color="rojo", impacto="grande", fecha="2026-10-31", fecha_txt="2026-10-31 — " + "DÍA SOLO POR RESUMEN", hora="tarde o noche (solo por resumen)", mu=2, he=1, cu=0, hk=16,
  ent="Estado de México", mun="Cuautitlán Izcalli (U.H. Infonavit Norte)", dia="PUB. 1-NOV, POR RUTA",
  title="ESTADO DE MÉXICO · CUAUTITLÁN IZCALLI — ATAQUE ARMADO EN UNA CHELERÍA: DOS MUERTOS Y UNA MUJER HERIDA",
  hecho="Cuautitlán Izcalli · <code>U.H. INFONAVIT NORTE, POR TITULAR (MILENIO)</code> · publicado el domingo 1-NOV, por ruta (El Monitor del Edomex 2026/11/01) · sábado 31-OCT, tarde o noche («noche», Milenio), " + DSR + " · " + RET + " · <b>2 muertos y 1 mujer herida</b>, por titular (El Monitor del Edomex; Digitalmex) (🔴 homicidio múltiple) · ataque directo, según el presidente municipal, " + RES + " · " + NOD,
  panel="<b>Ataque en una chelería: 2 muertos y 1 herida</b>", inst="Presidente municipal" + PR, nac="Milenio", conf="★★★☆☆",
  campo="día y hora solo por resumen", I=0, N=1, R=2, A=0,
  fechadas=["El Monitor del Edomex (2026/11/01)"], estatus="Parcialmente corroborado", arm=None,
  desl="Cuautitlán Izcalli no figura en las cinco ediciones previas ni en el índice. Col. La Quebrada (1 muerto y 3 heridos, sin ruta): visto."),
 # ======================= AMARILLOS
 dict(id="ARG-146-013", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="pequeno", fecha="2026-11-01", hora="~10:50-11:00 (solo por resumen)", mu=1, he=1, cu=0, hk=10.9,
  ent="Sinaloa", mun="Culiacán (col. Miguel Hidalgo)", dia="1-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — ASESINAN AL DUEÑO DE UNA TAQUERÍA EN LA COLONIA MIGUEL HIDALGO; UN HERIDO",
  hecho="Culiacán · <code>COL. MIGUEL HIDALGO, POR TITULAR</code> · domingo 1-NOV, por ruta (Luz Noticias 2026-11-01; Línea Directa 2026-11-01) · ~10:50-11:00, " + RES + " · <b>1 muerto</b>: el dueño de la taquería, por titular · <b>1 herido</b>, por titular (Luz Noticias) (🟡 homicidio doloso único) · " + NOD,
  panel="<b>Dueño de una taquería asesinado</b>; 1 herido", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["Luz Noticias (2026-11-01)", "Línea Directa (2026-11-01)"], estatus="Parcialmente corroborado", arm=None,
  desl="Taquería El Compaye y col. Miguel Hidalgo no figuran en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-146-014", estado="MX-PUE", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-11-01", hora="~22:40 (solo por resumen)", mu=1, he=1, cu=0, hk=22.7,
  ent="Puebla", mun="San Martín Texmelucan (col. La Purísima)", dia="1-NOV, POR TITULAR",
  title="PUEBLA · SAN MARTÍN TEXMELUCAN — ATAQUE ARMADO TRAS EL DESFILE DE DÍA DE MUERTOS: UN MUERTO Y UN HERIDO",
  hecho="San Martín Texmelucan · <code>AV. INDEPENDENCIA, COL. LA PURÍSIMA, SOLO POR RESUMEN</code> · domingo 1-NOV, noche, por titular («desfile de Día de Muertos»: UnoTV; Intolerancia Diario 2026/11/02) · ~22:40, " + RES + " · <b>1 muerto y 1 herido</b>, por titular (UnoTV) (🟡 homicidio doloso único) · ocupantes de un vehículo del desfile, " + RES + " · " + NOD,
  panel="<b>Ataque tras el desfile: 1 muerto y 1 herido</b>", inst=SB, nac="UnoTV", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=2, A=0,
  fechadas=["Intolerancia Diario (2026/11/02)"], estatus="Parcialmente corroborado", arm=None,
  desl="Texmelucan: visto en los archivos de equipos de ARGOS 143 y 144 (col. Morelos, 27-28-oct, 1 muerto y 1 herido; Retodiario 2026/10/28; sin ARG-ID): otro hecho. ARG-119-006 (col. Ojo de Agua, septiembre): otro hecho."),
 dict(id="ARG-146-015", estado="MX-MEX", region="Centro", color="amarillo", impacto="pequeno", fecha="2026-11-02", hora="no fijada", mu=1, he=1, cu=0, hk=12,
  ent="Estado de México", mun="Tultitlán (Prados Sur)", dia="2-NOV, POR TITULAR",
  title="ESTADO DE MÉXICO · TULTITLÁN — ASESINAN A UN CHECADOR DE TRANSPORTE Y HIEREN A OTRO",
  hecho="Tultitlán · <code>PRADOS SUR, POR TITULAR (TELEDIARIO)</code> · lunes 2-NOV, por titular (Telediario: «hoy 2 noviembre 2026») · <b>1 muerto</b> (checador de combis) <b>y 1 herido</b>, por titular (Sociedad Noticias 2026/11/03; Digitalmex) (🟡 homicidio doloso único) · agresores en motocicleta, " + RES + " · " + NOD,
  panel="<b>Checador de transporte asesinado</b>; 1 herido", inst=SB, nac="N+", conf="★★★☆☆",
  campo="hora no fijada; ninguna fuente institucional", I=0, N=1, R=3, A=0,
  fechadas=["Sociedad Noticias (2026/11/03)"], estatus="Parcialmente corroborado", arm=None,
  desl="Tultitlán no figura en las cinco ediciones previas ni en el índice. Lugar descrito de tres formas (Av. Prados Norte, col. Prados Sur, Unidad Morelos 3.ª Secc.)."),
 dict(id="ARG-146-016", estado="MX-JAL", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-11-02", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Jalisco", mun="San Pedro Tlaquepaque (San Martín de las Flores)", dia="2-NOV, POR RUTA",
  title="JALISCO · TLAQUEPAQUE — AGREDEN A POLICÍAS MUNICIPALES DURANTE UNA BÚSQUEDA TRAS UNA BALACERA",
  hecho="Tlaquepaque · <code>SAN MARTÍN DE LAS FLORES, SOLO POR RESUMEN</code> · lunes 2-NOV, por ruta (Informador 20261102; Crónica 2026/11/02) · policías municipales <b>agredidos a disparos</b> durante la búsqueda de los autores de una balacera previa, " + RES + " (🟡 agresión derivada de una acción policial) · <b>policías ilesos</b>, " + RES + " · uno de los agresores, herido, " + RES + " · detención: ficha propia, ARG-146-018",
  panel="<b>Agresión a policías municipales</b> durante una búsqueda; policías ilesos", inst=SB, nac="Crónica", conf="★★★☆☆",
  campo="circunstancia y saldo solo por resumen", I=0, N=1, R=1, A=0,
  fechadas=["Informador (2026/11/02)", "Crónica (2026/11/02)"], estatus="Parcialmente corroborado", arm=None, armtxt="armamento en ARG-146-018",
  desl="San Martín de las Flores no figura en las cinco ediciones previas ni en el índice. Balacera previa con cuatro jóvenes heridos: sin ruta ni día propio, visto."),
 # ======================= VERDES
 dict(id="ARG-146-017", estado="MX-MIC", region="Occidente", color="verde", impacto="mediano", fecha="2026-11-02", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Michoacán", mun="Uruapan (col. Mártires)", dia="2-NOV, POR RUTA",
  title="MICHOACÁN · URUAPAN — GUARDIA CIVIL Y DEFENSA DETIENEN A DOS HOMBRES TRAS LA AGRESIÓN A MILITARES",
  hecho="Uruapan · lunes 2-NOV, por ruta (Changoonga 2026/11/02) · <b>2 hombres detenidos</b>, por titular (Quadratín; El Universal; Changoonga: «apañan a 2»): cifra de medios, sin comunicado citado · arma corta 9 mm, 22 cartuchos, marihuana y dos teléfonos, " + RES + " · Guardia Civil y Defensa, " + RES,
  panel="<b>2 detenidos</b> tras la agresión a militares; arma corta y cartuchos (solo por resumen)", inst="Guardia Civil y Defensa" + PR, nac="El Universal", conf="★★★☆☆",
  campo="armamento solo por resumen; detenidos por titular de medios", I=0, N=1, R=4, A=0,
  fechadas=["Changoonga (2026/11/02)"], estatus="Parcialmente corroborado", arm="ARG-146-ARM-001",
  desl="Hecho delictivo: ARG-146-007. Detenidos fuera del conteo de armamento hasta cifra de autoridad."),
 dict(id="ARG-146-018", estado="MX-JAL", region="Occidente", color="verde", impacto="pequeno", fecha="2026-11-02", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Jalisco", mun="San Pedro Tlaquepaque (San Martín de las Flores)", dia="2-NOV, POR RUTA",
  title="JALISCO · TLAQUEPAQUE — DETIENEN A DOS HOMBRES TRAS LA AGRESIÓN A POLICÍAS",
  hecho="Tlaquepaque · lunes 2-NOV, por ruta (Informador 20261102: «detienen a dos hombres tras agresión a policías»; Crónica 2026/11/02: «detiene a 2 sujetos») · <b>2 detenidos</b>, por titular: cifra de medios, sin comunicado citado · un arma de fuego y un mototaxi, " + RES,
  panel="<b>2 detenidos</b> tras la agresión a policías", inst=SB, nac="Crónica", conf="★★★☆☆",
  campo="armamento solo por resumen; detenidos por titular de medios", I=0, N=1, R=1, A=0,
  fechadas=["Informador (2026/11/02)", "Crónica (2026/11/02)"], estatus="Parcialmente corroborado", arm="ARG-146-ARM-002",
  desl="Hecho delictivo: ARG-146-016."),
 dict(id="ARG-146-019", estado="MX-GRO", region="Sureste", color="verde", impacto="mediano", fecha="2026-11-03", fecha_txt="publicado el 2026-11-03 — DÍA DE LA DETENCIÓN NO FIJADO", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Guerrero", mun="Cocula (detención) · Iguala (delito)", dia="PUB. 3-NOV, POR RUTA",
  title="GUERRERO · COCULA — DETIENEN A «EL PIKACHU», SEÑALADO COMO INTEGRANTE DE LOS TLACOS, POR UN HOMICIDIO EN IGUALA",
  hecho="Cocula · publicado el martes 3-NOV, por ruta (Proyecto Puente 2026/11/03; Cúspide 2026/11/03) · día de la detención no fijado · " + RET + " · <b>1 detenido</b>, por titular (Quadratín: «cae por homicidio El Pikachu, presunto integrante de Los Tlacos»); el homicidio de un abogado en Iguala, por titular (Infobae 2026/11/04) · delito original, octubre de 2025, " + RES + ": evento anterior, no se recalifica · pistola, cargador y cartuchos sin cifra, " + RES + " · FGE Guerrero, " + RES,
  panel="<b>Detenido «El Pikachu»</b> (Los Tlacos) por un homicidio de 2025", inst="FGE Guerrero" + PR, nac="Infobae · Milenio", conf="★★★☆☆",
  campo="día de la detención no fijado; corporación solo por resumen", I=0, N=2, R=3, A=0,
  fechadas=["Proyecto Puente (2026/11/03)", "Cúspide (2026/11/03)", "Infobae (2026/11/04)"], estatus="Parcialmente corroborado", arm="ARG-146-ARM-003",
  desl="«El Pikachu» de Pánuco, Veracruz (Notiver): otro detenido, otro caso. «Los Tlacos» e Iguala en el índice: ARG-141-007 (3 detenidos por extorsión, 25-oct; Iguala y Copalillo) y ARG-110-REC-001 (San Miguel Totolapan): otros hechos, otros detenidos; vínculo no acreditado."),
 dict(id="ARG-146-020", estado="MX-CHP", region="Sureste", color="verde", impacto="mediano", fecha="2026-11-03", fecha_txt="publicado el 2026-11-03 — DÍA DE LAS DETENCIONES NO FIJADO", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Chiapas", mun="Chenalhó", dia="PUB. 3-NOV, POR RUTA",
  title="CHIAPAS · CHENALHÓ — DETIENEN A DOS HOMBRES POR EL HOMICIDIO DEL DEFENSOR DE FAMILIAS DESPLAZADAS",
  hecho="Chenalhó · publicado el martes 3-NOV, por ruta (Diario de Yucatán 2026/11/03; MVS 2026/11/3; Herqles 2026/11/03; La Razón 2026/11/04) · día de las detenciones no fijado · " + RET + " · <b>2 detenidos</b>, por titular (Diario de Yucatán: «detienen a dos hombres por el homicidio de defensor de familias desplazadas»; La Razón: «caen 2») · el fiscal general informó las detenciones y la premeditación, " + RES + " · se busca a otros implicados, " + RES,
  panel="<b>2 detenidos</b> por el homicidio del defensor (ARG-144-004)", inst="FGE Chiapas" + PR, nac="MVS · La Razón", conf="★★★☆☆",
  campo="día de las detenciones no fijado; declaración del fiscal solo por resumen", I=0, N=2, R=2, A=0,
  fechadas=["Diario de Yucatán (2026/11/03)", "MVS (2026/11/3)", "Herqles (2026/11/03)", "La Razón (2026/11/04)"], estatus="Parcialmente corroborado", arm=None, armtxt="sin fila — sin aseguramiento publicado",
  desl="Hecho delictivo: ARG-144-004 (28-oct, ventana de ARGOS 144), no se recalifica. ARGOS 145 (archivo de fuentes): detenidos solo extraoficiales. Las cuatro rutas son coberturas de la misma información."),
 dict(id="ARG-146-021", estado="MX-ROO", region="Sureste", color="verde", impacto="pequeno", fecha="2026-11-03", fecha_txt="publicado el 2026-11-03 — DÍA DE LAS DETENCIONES NO FIJADO", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Quintana Roo", mun="Benito Juárez (Cancún)", dia="PUB. 3-NOV, POR RUTA",
  title="QUINTANA ROO · CANCÚN — DETIENEN A «GARABATO» Y A DOS PRESUNTOS INTEGRANTES DE UN GRUPO CRIMINAL",
  hecho="Cancún · publicado el martes 3-NOV, por ruta (Por Esto 2026/11/3) · día de las detenciones no fijado · " + RET + " · detención de «Garabato» y de presuntos integrantes de un grupo criminal ligado a ataques armados, por <i>slug</i> (Por Esto) · <b>3 detenidos</b>, " + RES + " · señalado por al menos tres ataques en las regiones 249 y 251, " + RES + " · " + FU,
  panel="<b>Detenido «Garabato»</b> con otros dos, ligados a ataques armados", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; cifra de detenidos solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["Por Esto (2026/11/3)"], estatus="Pendiente de corroboración", arm=None, armtxt="sin fila — aseguramiento no publicado",
  desl="La nota no vincula a los detenidos con Paseos del Mar (ARG-146-REC-001): <code>VÍNCULO NO ACREDITADO</code>."),
 dict(id="ARG-146-022", estado="MX-SIN", region="Noroeste", color="amarillo", impacto="mediano", fecha="2026-11-02", hora="~09:40 (solo por resumen)", mu=0, he=0, cu=0, hk=9.7,
  ent="Sinaloa", mun="Culiacán (Feria Ganadera)", dia="2-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — ATACAN CON ARMAS DE FUEGO LAS INSTALACIONES DE LA FERIA GANADERA",
  hecho="Culiacán · <code>INSTALACIONES DE LA FERIA GANADERA, POR TITULAR</code> · lunes 2-NOV, por ruta (Infobae 2026/11/02; Latinus 2026/11/2) · ~09:40, " + RES + " · <b>agresión armada contra las instalaciones</b>, por titular (Infobae: «atacan con armas de fuego instalaciones de la Feria Ganadera»; Latinus: «registran agresión armada») · disparos también contra los militares que las resguardan, " + RES + ": no acreditado (🟡 agresión sin víctimas publicadas; quién era el blanco, no determinado) · <b>sin muertos ni heridos publicados</b> · detención de tres: ficha propia, ARG-146-023",
  panel="<b>Agresión armada contra las instalaciones de la Feria Ganadera</b>; sin víctimas publicadas", inst=SB, nac="Infobae · Latinus", conf="★★★☆☆",
  campo="blanco de la agresión y hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=0, A=0,
  fechadas=["Infobae (2026/11/02)", "Latinus (2026/11/2)"], estatus="Parcialmente corroborado", arm=None, armtxt="armamento en ARG-146-023",
  desl="Feria Ganadera no figura en las cinco ediciones previas ni en el índice. Delito y detención en la misma ventana: dos fichas. Si se acredita el ataque a los militares, sube a 🔴."),
 dict(id="ARG-146-023", estado="MX-SIN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-11-03", fecha_txt="publicado el 2026-11-03 — DÍA DE LAS DETENCIONES NO FIJADO", hora="no fijada", mu=0, he=0, cu=0, hk=12,
  ent="Sinaloa", mun="Culiacán", dia="PUB. 3-NOV, POR RUTA",
  title="SINALOA · CULIACÁN — DETIENEN A TRES PERSONAS, UNA MENOR DE EDAD, POR LA AGRESIÓN A LA FERIA GANADERA",
  hecho="Culiacán · publicado el martes 3-NOV, por ruta (Proyecto Puente 2026/11/03; QuieroTV 2026/11/03) · <b>3 detenidos, uno menor de edad</b>, por titular (Proyecto Puente: «detienen a tres personas… uno es menor de edad»): cifra de medios, sin comunicado citado · armas aseguradas: 3, 4 o 5 según la fuente, " + RES + ": <code>CIFRAS CONTRADICHAS — NO SE INTEGRAN</code> · 641 cartuchos y 24 cargadores, " + RES,
  panel="<b>3 detenidos</b>, uno menor de edad, por la agresión a la Feria Ganadera", inst=SB, nac="UnoTV", conf="★★★☆☆",
  campo="armamento contradicho; detenidos por titular de medios", I=0, N=1, R=2, A=0,
  fechadas=["Proyecto Puente (2026/11/03)", "QuieroTV (2026/11/03)"], estatus="Parcialmente corroborado", arm="ARG-146-ARM-004",
  desl="Hecho delictivo: ARG-146-022. Puede estar contenido en el renglón de Culiacán del agregado federal (22 armas, 76 cargadores, 1,054 cartuchos): nada se integra."),
 dict(id="ARG-146-024", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-31", fecha_txt="publicado el 2026-10-31 — HORA NO FIJADA", hora="«mañana» (solo por resumen)", mu=1, he=2, cu=0, hk=9,
  ent="Michoacán", mun="Ario de Rosales (El Ortigal)", dia="PUB. 31-OCT, POR RUTA",
  title="MICHOACÁN · ARIO DE ROSALES — ATAQUE ARMADO CONTRA MILITARES EN EL ORTIGAL: UN SOLDADO MUERTO Y DOS HERIDOS",
  hecho="Ario de Rosales · <code>EL ORTIGAL, POR TITULAR</code> · publicado el sábado 31-OCT, por ruta (Latinus 2026/10/31; Grupo Marmor 2026/10/31; Changoonga 2026/10/31; La Prensa de Coahuila 2026/10/31) · " + AP + " · «mañana», " + RES + " · " + RET + " · <b>1 militar muerto y 2 heridos</b>, por titular (Grupo Marmor; Latinus: «ataque armado en contra de militares») (🔴 muerte de personal de las fuerzas armadas) · emboscada, según autoridades estatales, " + RES + " · " + NOD,
  panel="<b>Ataque contra militares: 1 soldado muerto y 2 heridos</b>", inst=SB, nac="Latinus · Excélsior", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=4, A=0,
  fechadas=["Latinus (2026/10/31)", "Grupo Marmor (2026/10/31)", "Changoonga (2026/10/31)", "La Prensa de Coahuila (2026/10/31)"], estatus="Parcialmente corroborado", arm=None,
  desl="Ario de Rosales en el índice: ARG-140-REC-001 (La Palma, 20-oct): otro hecho. ARGOS 145 cerró a las 11:14 del 31 sin este hecho: se integra a la edición que lo ve primero, con la marca."),
]
# ---------------------------------------------------------------- RECUPERACIONES (solo alto impacto de ventanas anteriores)
R = [
 dict(id="ARG-146-REC-001", estado="MX-ROO", region="Sureste", fecha="2026-10-30", hora="~14:00 (solo por resumen)", orig="ARGOS 145", col_orig="rojo", mu=3, he=0, cu=0,
  ent="Quintana Roo", mun="Benito Juárez (Cancún, Paseos del Mar, región 251)", dia="30-OCT, POR RUTA",
  title="QUINTANA ROO · CANCÚN — EJECUTAN A TRES PERSONAS EN PASEOS DEL MAR",
  hecho="<code>VENTANA DE ORIGEN: ARGOS 145</code> · Cancún · <code>PASEOS DEL MAR, REGIÓN 251, POR RUTA Y TITULAR; CALLE ISLA MAURICIO, SOLO POR RESUMEN</code> · viernes 30-OCT, por ruta (Noticaribe 2026/10/30) · ~14:00, " + RES + " · <b>3 muertos</b>, por <i>slug</i> (Noticaribe: «ejecutan a tres personas en la región 251»); una mujer entre las víctimas, por titular (Quintana Roo Hoy) (🔴 homicidio múltiple) · atacantes en motocicleta, " + RES + " · " + NOD + ", por titular (Cambio22)",
  panel="<b>Tres personas ejecutadas</b> en un fraccionamiento", inst=SB, nac="Sipse (sin fecha en la ruta)",
  conf="★★★☆☆", campo="hora solo por resumen; ninguna fuente institucional", I=0, N=1, R=5, A=0,
  fechadas=["Noticaribe (2026/10/30)"],
  desl="ARGOS 145 lo registró como visto sin ruta fechada. Detención de «Garabato» (ARG-146-021): vínculo no acreditado."),
]
for r in R:
    r["color"] = "rec"; r["impacto"] = "grande" if r["col_orig"] == "rojo" else "mediano"

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ND_ALL = list(range(10))
ARM = [
 dict(id="ARG-146-ARM-001", ficha="ARG-146-017", estado="MX-MIC", region="Occidente", color="verde", ent="Michoacán", mun="Uruapan (col. Mártires)",
  fecha="2026-11-02", fecha_txt="2-nov, por ruta", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="Guardia Civil y Defensa <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: 1 corta 9 mm y 22 cartuchos, solo por resumen; 2 detenidos por titular de medios, sin cifra de autoridad: n/d; ver ARG-146-017",
  fuentes=["Changoonga (2026/11/02)", "Quadratín (sin fecha en la ruta)", "El Universal (sin fecha en la ruta)"]),
 dict(id="ARG-146-ARM-002", ficha="ARG-146-018", estado="MX-JAL", region="Occidente", color="verde", ent="Jalisco", mun="San Pedro Tlaquepaque",
  fecha="2026-11-02", fecha_txt="2-nov, por ruta", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="Policía de Tlaquepaque <span class=\"muted-note\">(por titular)</span>", conf="Bajo",
  nota="cualitativo: un arma de fuego sin categoría, solo por resumen; 2 detenidos por titular de medios: n/d; ver ARG-146-018",
  fuentes=["Informador (2026/11/02)", "Crónica (2026/11/02)"]),
 dict(id="ARG-146-ARM-003", ficha="ARG-146-019", estado="MX-GRO", region="Sureste", color="verde", ent="Guerrero", mun="Cocula",
  fecha="2026-11-03", fecha_txt="pub. 3-nov; día de la detención no fijado", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="FGE Guerrero <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="cualitativo: pistola, cargador y cartuchos sin cifra, solo por resumen; 1 detenido por titular: n/d; ver ARG-146-019",
  fuentes=["Proyecto Puente (2026/11/03)", "Cúspide (2026/11/03)"]),
 dict(id="ARG-146-ARM-004", ficha="ARG-146-023", estado="MX-SIN", region="Noroeste", color="verde", ent="Sinaloa", mun="Culiacán",
  fecha="2026-11-03", fecha_txt="pub. 3-nov; día de la detención no fijado", hora="no fijada", c=[0] * 10, nd=ND_ALL, integra=True,
  corp="<span class=\"muted-note\">no publicada por titular</span>", conf="Bajo",
  nota="cualitativo: 3, 4 o 5 armas según la fuente, 641 cartuchos y 24 cargadores, solo por resumen: cifras contradichas; 3 detenidos por titular de medios: n/d; ver ARG-146-023",
  fuentes=["Proyecto Puente (2026/11/03)", "QuieroTV (2026/11/03)"]),
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
HORAS = 91 + 38 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0] * 10 and ND == [True] * 10, (TOT, ND)
assert cnt == {"rojo": 13, "amarillo": 5, "verde": 6}, cnt
assert cnt_rec == {"rojo": 1, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC, CU_REC) == (21, 9, 4, 3, 0, 0), (MU, HE, CU, MU_REC, HE_REC, CU_REC)
assert DENS == "0,26", DENS
assert (NAP, NFR, NRET) == (1, 1, 5), (NAP, NFR, NRET)
assert len(ENT) == 14 and len(ENT_ROJO) == 9, (ENT, ENT_ROJO)
assert sorted(e["id"] for e in E) == [f"ARG-146-{i+1:03d}" for i in range(len(E))]
assert [r["id"] for r in R] == [f"ARG-146-REC-{i+1:03d}" for i in range(len(R))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-31" or x in R, x["id"]
    assert x in E or x["fecha"] <= "2026-10-31", x["id"]

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
head = head.replace("<title>ARGOS 145 — Reporte Nacional de Seguridad — 2026-10-31</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA FISCALÍA DE GUANAJUATO EL COTEJO BALÍSTICO ENTRE LOS ATAQUES DE CELAYA, SILAO E IRAPUATO</b> (ARG-146-004, -005 y -006).
      <br><b>2. SOLICITE A LA DEFENSA Y A LA FISCALÍA DE MICHOACÁN LOS PARTES DE LAS AGRESIONES A MILITARES Y LA SITUACIÓN JURÍDICA DE LOS DOS DETENIDOS DE URUAPAN</b> (ARG-146-007, -017 y -024).
      <br><b>3. SOLICITE A LAS FISCALÍAS DE SONORA, BAJA CALIFORNIA Y TAMAULIPAS EL NÚMERO OFICIAL DE VÍCTIMAS Y LA IDENTIFICACIÓN DE LOS RESTOS LOCALIZADOS POR COLECTIVOS</b> (ARG-146-009, -010 y -011).
      <br><b>4. SOLICITE A LAS FISCALÍAS DE LA CIUDAD DE MÉXICO, VERACRUZ, GUERRERO Y DEL ESTADO DE MÉXICO LAS LÍNEAS DE INVESTIGACIÓN Y LOS DETENIDOS DE LOS ATAQUES MÚLTIPLES</b> (ARG-146-001, -002, -003 y -012).
      <br><b>5. SOLICITE A LA FISCALÍA DE TAMAULIPAS EL MÓVIL DEL ARG-146-008 Y A LAS DE CHIAPAS, GUERRERO Y SINALOA LA SITUACIÓN JURÍDICA DE LOS DETENIDOS</b> (ARG-146-019, -020 y -023).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
rows_rec = "\n".join(prow(r, True) for r in sorted(R, key=lambda x: x["fecha"], reverse=True))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>31-oct 11:14 → 4-nov 06:52 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · <b>{len(R)} recuperación de alto impacto de la ventana anterior</b>, atenuada, <b>fuera de todos los totales</b>
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
    <b>Armamento</b>: ninguna arma ni detenido integrado al total: cifras solo por resumen o sin cifra de autoridad · <b>muertos por agresión</b>: {MU}, con los 3 de Celaya (ARG-146-004: saldo contradicho por resumen; con la versión de Correo, {MU-2}) · <b>cuerpos o restos hallados</b>: al menos {CU} (Suaqui Grande, cifra mínima por titular); Nuevo Laredo y Miguel Alemán, número no publicado · <b>marcas</b>: {NAP} de {len(E)} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>totales sujetos a las cláusulas de retiro de {NRET} fichas</b> (día no fijado frente a las 11:14 del 31): ARG-146-012, -019, -020, -021 y -024 · <b>recuperación, fuera de totales</b>: {MU_REC} muertos; efecto sobre ARGOS 145, en el archivo de fuentes. <b>Cálculo propio</b>.
    <br><b>Vistos, fuera de totales</b> — <b>de la ventana de ARGOS 145</b> (🟢 o 🟡, no se recuperan): Concordia, Sin. (militares agredidos tras localizar un campamento; 3 abatidos; 29-oct, ventana anterior; aseguramiento de La Guásima, posible mismo operativo) · aseguramientos de Huajicori y Huitzuco: en la página de armamento · <b>sin ruta fechada ni titular con día</b> — <code>SIN RUTA FECHADA — NO SE FICHA</code>: Valle de Chalco: San Miguel Xico 1.ª Secc., 2 muertos y 1 herido, noche del viernes (Quadratín, sin fecha en la ruta: probable ventana de ARGOS 145); 2.ª Secc., 1 muerto y 1 herido (Milenio; Telediario, sin fecha): posibles hechos distintos · Mazatlán, policía municipal herido (ruta sin día) · Acolman, 2 muertos en una tienda · Jiutepec, ataque a agentes · Culiacán, Alturas del Sur, mujer asesinada (pertenencia a la GN no confirmada) · Papantla · Acapulco, La Laja · Silao, El Escoplo y «Silao y Romita» · Tehuacán · Cuautitlán Izcalli, La Quebrada · Mexicali, Cerro Centinela (restos óseos en peritaje) · <b>balances, no se reparten ni se integran</b>: fin de semana (116 homicidios del 30-oct al 1-nov, {RES}) · Guanajuato (8 y 9 en Día de Muertos) · Morelos (8) · puente de Día de Muertos (42 detenidos y 149 armas) · Tabasco (12 detenidos) · Veracruz, SSP (34 detenidos).
    <br><b>Seguimiento, fuera del semáforo</b>: <b>ARG-132-002 (Orizaba)</b>: el policía ministerial murió el 30-oct, por titular (La Silla Rota; Golpe Político; Plumas Libres 2026/10/30); vinculan a cuatro «por ataque a policías durante cateo», por titular (La Jornada Veracruz; N+, sin fecha); «por crimen de policía ministerial», por titular (La Silla Rota 2026/11/3); fecha de la vinculación no fijada · <b>ARG-144-008 / ARG-145-REC-001 (Matamoros)</b>: «seis personas ajenas» muertas en la jornada de bloqueos, por titular (Infobae 2026/10/31; El Mañana 2026/10/31); proyectil 7.62 con trayectoria descendente en la muerte de la niña, por titular (La Región 2026/11/03); sin comunicado oficial · <b>ARG-145-001 (Culiacán)</b>: víctima identificada por un medio, no por autoridad · <code>NINGUNO ES SENTENCIA</code>.
  </p>
'''

byid = {e["id"]: e for e in E}
rbyid = {r["id"]: r for r in R}
co1 = "\n".join(ficha(byid[f"ARG-146-{i:03d}"]) for i in (1, 2, 3, 4))
co2 = "\n".join(ficha(byid[f"ARG-146-{i:03d}"]) for i in (5, 6, 7, 24, 8))
co2b = "\n".join(ficha(byid[f"ARG-146-{i:03d}"]) for i in (9, 10, 11, 12))
co2c = "\n".join(ficha(byid[f"ARG-146-{i:03d}"]) for i in (13, 22, 14, 15, 16))
co2d = "\n".join(ficha(byid[f"ARG-146-{i:03d}"]) for i in (17, 18, 23, 19, 20, 21))
co3 = "\n".join(ficha(rbyid[i], True) for i in ("ARG-146-REC-001",))
assert sorted(re.findall(r'id="(ARG-146-0\d\d)"', co1 + co2 + co2b + co2c + co2d)) == sorted(byid)
assert sorted(re.findall(r'id="(ARG-146-REC-\d\d\d)"', co3)) == sorted(rbyid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0", "n/d") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code>"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), "Uruapan y Cocula: cifras solo por resumen"),
 tile(1, "Armas largas", tv(1), NI),
 tile(2, "Sin categoría", tv(2), "Tlaquepaque: solo por resumen; Culiacán: 3, 4 o 5, contradicho"),
 tile(3, "Cartuchos", tv(4, fmt), "Uruapan y Culiacán: cifras solo por resumen"),
 tile(4, "Cargadores", tv(5), "Cocula: sin cifra"),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>: ninguna cifra de autoridad; Uruapan 2, Tlaquepaque 2, Culiacán 3 y Cocula 1, por titulares de medios"),
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
    <div class="map-caption">Sin aseguramiento con cifra integrable; cuatro eventos cualitativos en la tabla (Michoacán, Jalisco, Sinaloa y Guerrero).</div>
  </div>
'''

def armrow(a):
    c = a["c"]
    nd = a.get("nd", [])
    cells = "".join(f"<td>{'n/d' if i in nd else ('<b>'+fmt(v)+'</b>') if v else '0'}</td>" for i, v in enumerate(c[:9]))
    det = "n/d" if 9 in nd else (f"<b>{c[9]}</b>" if c[9] else "0")
    st = '' if a["integra"] else ' style="opacity:.72;"'
    return f'      <tr id="{a["id"]}"{st}><td>{('<a href="#'+a["ficha"]+'">') if a["ficha"] != a["id"] else ''}<code>{a["id"]}</code>{'</a>' if a["ficha"] != a["id"] else ''}</td><td>{a["ent"]}</td><td>{a["mun"]}</td><td>{a["fecha_txt"]}</td>{cells}<td>{det}</td><td>{a["corp"]}</td><td><b>{a["conf"]}</b><br><span class="muted-note">{a["nota"]}</span></td></tr>'

armrows = "\n".join(armrow(a) for a in ARM) or '      <tr><td colspan="16"><code>SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE</code> — ningún aseguramiento con cifra publicada y día fijado entre el 31-oct 11:14 y el 4-nov 06:52</td></tr>'
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
    <b>Lectura regional</b>: ninguna región con arma ni detenido integrado al total. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: los cuatro de la tabla.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>boletín federal de acciones del 30 y 31-oct y 1 y 2-nov</b> (agregado sin día por acción, que abarca la ventana de ARGOS 145; solo por republicadores, misma fuente: Milenio, RED113, Tallapolítica, Certeza Diario): Culiacán (22 armas, 76 cargadores, 1,054 cartuchos), Huitzuco (66 armas), Ahumada, Chih. (7 detenidos, 5 armas), Texcoco–Chimalhuacán–Ecatepec (12 detenidos, 178,780 litros), Puebla, Unidad Antorchista (3 detenidos, 1 corta, 4 cargadores, 51 cartuchos), Nayarit (2 detenidos, 3 largas, 9 cargadores, 374 cartuchos), Iztapalapa (3 detenidos, 2 largas) y Matamoros (1 detenido, 1 larga, 71 cartuchos), todo {RES}: <code>FECHA NO FIJADA — NO SE INTEGRA</code> · <b>Culiacán, El Tepuche</b> (37 armas, 2,735 cartuchos; Luz Noticias 2026-11-03) y <b>Caminaguato–El Tepuche</b> (15 largas, 30 cargadores; Heraldo de México 2026/11/4), {RES}: <code>POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN</code> · <b>Huajicori, Nay.</b> (ntv 2026/11/03; hecho del 30-oct, ventana de ARGOS 145; 6 o 4 detenidos, cifras contradichas) · <b>Concordia, La Guásima</b>: ver panorama; <code>POSIBLE DUPLICIDAD</code> con la agresión del 29-oct hasta validación.
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
      <tr><td><b>Campeche</b><br>San Francisco de Campeche</td><td>Posesión de metilfenidato; <b>1 sentenciado</b>, {RES} · <b>nuevo en ARGOS 146</b></td><td>No publicada</td><td>FGR <span class="muted-note">(solo por resumen)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · comunicado del 3-nov solo en el resumen del buscador; sin URL, pena ni campos individualizadores</td><td>No confirmado</td></tr>
      <tr><td><b>Baja California</b><br>Tecate</td><td>Ataque a la Guardia Nacional (2024); procedimiento abreviado; <b>4 sentenciados</b>, por titular · <b>candidato de ARGOS 145</b></td><td><b>hasta 16 años</b>, por titular (El Imparcial; Tijuana Última Hora 2026/10/30); penas individuales, {RES}</td><td>FGR <span class="muted-note">(por titular de medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · publicado el 30-oct (ventana de ARGOS 145); comunicado no localizado</td><td>Bajo</td></tr>
      <tr><td><b>Baja California</b><br>Mexicali</td><td>Homicidio calificado y desaparición; <b>1 sentenciada</b>, por titular · <b>candidato de ARGOS 145</b></td><td><b>45 años</b>, por titular (El Imparcial 2026/10/29; Periodismo Negro 2026/10/30)</td><td>FGE Baja California <span class="muted-note">(por titular)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · <code>fgebc.gob.mx</code> consultado: caso no indexado; ventana de ARGOS 145</td><td>Bajo</td></tr>
      <tr><td><b>Puebla</b><br>Huejotzingo</td><td>Feminicidio y aborto · <b>candidato de ARGOS 144</b></td><td><b>55 años</b>, por titular (Retodiario; Heraldo de Puebla; Intolerancia Diario 2026/10/29)</td><td>FGE Puebla <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · ventana de ARGOS 145; boletín del dominio no localizado</td><td>Bajo</td></tr>
      <tr><td><b>Jalisco · Oaxaca · Tabasco · NL · Edomex · Zac · Coah · Hgo</b></td><td>Dos feminicidas (29-oct) · Oaxaca, violencia familiar (29-oct) · Tenosique · Doctor Arroyo y 40 años · Ecatepec · Fresnillo · Ramos Arizpe · Tulantepec · <b>candidatos anteriores, sin cambio</b></td><td>Ver ARGOS 145</td><td>Fiscalías estatales y FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín del dominio en la ventana; Tulantepec: audiencia de pena el 5-nov, <code>HEREDADO — NO REVERIFICADO</code></td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGE Querétaro (boletines de enero a septiembre de 2026) · FGE Durango (24-ago y 28-jul) · FGE Tabasco (boletín 5012, 7-ago) · FGE Veracruz (enero y febrero) · FGE Oaxaca (boletín 2603, 7-jul) · FGE Nayarit (8-oct) · FGE Jalisco (16-oct). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>No</b> por dominio: <code>fgr.org.mx</code> solo devolvió la portada · comunicados de la ventana vistos solo en resúmenes del buscador</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>15 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, Sin, Dgo · NL, SLP, Zac · Jal, Nay · Edomex, Hgo, Qro · Ver, Tab · Oax, Gro</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b> en dominio oficial con fecha acreditada</td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>15</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>1</b>: Son (<code>fiscalia.sonora.gob.mx</code>) · <b>dominio de la fiscalía no confirmado</b>: <b>2</b>, Coah y Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>14</b>: BCS, Chih · Tamps · Col, Ags, Mich, Gto · CDMX, Mor, Pue, Tlax · Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 4-nov 06:52: código <code>000</code> (proxy: conexión rechazada)</td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto</b>: <b>consulta propia</b> en 9 de las 10 que ARGOS 145 dejó solo con consulta amplia —Dgo · SLP · Jal, Col, Ags, Mich · Chis, Gro; Son—; Nay, solo amplia · <b>armamento: 20 de 32 por dominio oficial</b> —Chih, Sin · NL, SLP · Jal, Nay, Ags, Mich, Gto · Mor, Tlax, Hgo, Qro · Ver · Camp, Chis, Oax, Gro, Yuc, QRoo—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> (Gto: solo normateca) · dominio sin páginas: Tab · <code>NO REVISADA</code> (11): BC, BCS, Son, Dgo · Coah, Tamps, Zac · Col · CDMX, Edomex, Pue</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 30 y 31-oct y 1 y 2-nov</b>: un agregado, publicado por republicadores (Milenio, RED113, Tallapolítica, Certeza Diario); sin indexar en <code>gob.mx</code> · <b>acciones del 3-nov</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título · Guardia Nacional, Defensa y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 4-NOV 06:52: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Trece rojos propios en nueve entidades</b> (cálculo propio): siete homicidios múltiples, un servidor público asesinado, dos agresiones a militares y tres hallazgos de restos humanos. <b>Alza del riesgo nacional frente a ARGOS 145</b>: 0,14 rojos por hora, frente a 0,06 como máximo en ARGOS 145 (cálculo propio).
      <br><b>2.</b> <b>Guanajuato</b> concentra tres de los trece rojos (ARG-146-004, -005 y -006); saldo, en la Conclusión 1 (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: cinco amarillos —tres homicidios dolosos con un herido cada uno, una agresión a policías municipales y una agresión armada contra las instalaciones de la Feria Ganadera de Culiacán— en cuatro entidades (cálculo propio).
      <br><b>4.</b> <b>Respuesta institucional</b>: seis verdes, ninguno con cifra de armamento o de detenidos citable; ninguna sentencia integrable (cálculo propio; totales, en el panorama).
      <br><b>5.</b> <code>VENTANA DE {DUR.upper()} CON FIN DE SEMANA Y DÍA DE MUERTOS: TOTALES NO COMPARABLES CON ARGOS 145 SIN NORMALIZAR POR HORA; CINCO DE VEINTICUATRO HECHOS CON CLÁUSULA DE RETIRO; UN ROJO RECUPERADO DE ARGOS 145. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. GUANAJUATO: TRES ATAQUES CON VÍCTIMAS MÚLTIPLES EN TRES MUNICIPIOS DEL CORREDOR CELAYA–SILAO–IRAPUATO DEL 2 AL 4-NOV</b> (cálculo propio: Irapuato, día no fijado; 8 muertos —Celaya, saldo contradicho— y 2 heridos): ARG-146-004, -005 y -006; vínculo no acreditado. Línea: <b>vigilar las colonias Ejidal (Celaya) y Primavera (Irapuato) y la comunidad Monte del Coecillo (Silao)</b>.
      <br><b>2. MICHOACÁN: DOS AGRESIONES A MILITARES EN TRES DÍAS, UNA CON UN SOLDADO MUERTO</b> (cálculo propio): ARG-146-024 (Ario de Rosales, 31-oct) y ARG-146-007 (Uruapan, 2-nov; dos detenidos, ARG-146-017); vínculo no acreditado. Línea: <b>vigilar los recorridos militares en las regiones de Ario de Rosales y Uruapan y solicitar a la fiscalía el cotejo balístico entre ambos hechos</b>.
      <br><b>3. RESTOS HUMANOS LOCALIZADOS POR COLECTIVOS EN TRES ESTADOS FRONTERIZOS DEL NORTE EN DOS DÍAS, NINGUNO CON CIFRA OFICIAL DE VÍCTIMAS</b> (cálculo propio, 2 y 3-nov): ARG-146-009 (Nuevo Laredo), -010 (Suaqui Grande) y -011 (Mexicali). Línea: <b>vigilar las jornadas de búsqueda de colectivos en curso en Sonora, Baja California y Tamaulipas</b>.
      <br><b>4. ATAQUES EN ACTOS PÚBLICOS DE DÍA DE MUERTOS, CON UN MENOR (3 O 4 AÑOS, EDAD CONTRADICHA) ENTRE LAS VÍCTIMAS</b> (cálculo propio: 5 muertos y 1 herido): ARG-146-001 (Tepito), -002 (panteón de Chinameca) y -014 (desfile de Texmelucan); vínculo no acreditado. Línea: <b>vigilar panteones, desfiles y reuniones públicas en las próximas celebraciones</b>.
      <br><b>5. DETENCIONES POR HOMICIDIOS DE UN DEFENSOR Y DE UN ABOGADO: A UNA SEMANA EN CHENALHÓ Y A UN AÑO EN IGUALA</b> (cálculo propio: 28-oct a 3-nov; octubre de 2025 a 3-nov): ARG-146-020 y -019; ninguna sentencia. Línea: <b>vigilar la vinculación a proceso y medir la brecha hasta sentencia en ambos casos</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx</b> — <code>SIN RESULTADO INDEXADO EN VENTANA</code>; lectura directa no disponible · <b>SSPC</b>: 116 homicidios del 30-oct al 1-nov, {RES} (Eje Central): balance, no se integra · <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición.
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b>
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ALTO IMPACTO: TEPITO, CHINAMECA, ACAPULCO Y CELAYA", co1)
 + page("CRIMEN ORGANIZADO (II) — ALTO IMPACTO: SILAO, IRAPUATO, URUAPAN, ARIO DE ROSALES Y REYNOSA", co2)
 + page("CRIMEN ORGANIZADO (III) — ALTO IMPACTO: RESTOS HUMANOS Y CUAUTITLÁN IZCALLI", co2b)
 + page("CRIMEN ORGANIZADO (IV) — VIOLENCIA OPERATIVA", co2c)
 + page("CRIMEN ORGANIZADO (V) — ACCIONES INSTITUCIONALES", co2d)
 + page("CRIMEN ORGANIZADO (VI) — ALTO IMPACTO DE LA VENTANA DE ARGOS 145: CANCÚN", co3)
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
assert script.count("WINDOW_DAYS = 3;") == 1, "plantilla de 145 con WINDOW_DAYS = 3"
script = script.replace("WINDOW_DAYS = 3;", "WINDOW_DAYS = 5;")
assert "WINDOW_DAYS = 5;" in script and "WINDOW_DAYS = 3;" not in script  # la ventana toca cinco fechas de calendario (31-oct y 1, 2, 3 y 4-nov)
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, NRET, MU, HE, CU, DENS)
