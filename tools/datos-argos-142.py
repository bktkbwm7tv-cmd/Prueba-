# -*- coding: utf-8 -*-
"""Generador de datos de ARGOS 142.
Uso: python3 tools/datos-argos-142.py <plantilla ARGOS 141> <salida>
Ventana: 26-oct 08:37 → 27-oct 08:45 CDMX. Archivo: argos-2026-10-27.html."""
import sys, re, json, html as H

NUM, FECHA, HORA = "142", "2026-10-27", "08:45"
CONSULTA = "2026-10-27, última búsqueda 09:56"
DUR = "24 h 08 min"
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
# ---------------------------------------------------------------- HECHOS PROPIOS
# mu = muertos por agresión, he = heridos, cu = cuerpos hallados sin causa de muerte informada
# (cálculo propio derivado del arreglo, nunca escrito a mano)
E = [
 # ======================= ROJOS
 dict(id="ARG-142-001", estado="MX-BCN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-26", hora="tarde, ~17:47 (solo por resumen); «noche» en otro medio", mu=1, he=1, cu=0, hk=17.8,
  ent="Baja California", mun="Tecate (col. Luis Alfonso Garzón, «Nido de las Águilas»)", dia="26-OCT, POR TITULAR; HORA SOLO POR RESUMEN",
  title="BAJA CALIFORNIA · TECATE — COMANDO ATACA A AGENTES DE LA FUERZA ESTATAL EN PATRULLAJE: UNA AGENTE MUERTA Y UN AGENTE HERIDO",
  hecho="Tecate · <code>COL. LUIS ALFONSO GARZÓN («NIDO DE LAS ÁGUILAS»), CALLE NARANJOS, SOLO POR RESUMEN</code> · lunes 26-OCT, por titular (El Congresista, «el 26 de octubre») y por ruta (El Imparcial 2026/10/26) · " + AP + " · tarde, ~17:47, " + RES + "; «noche», " + RES + " (Milenio) · agentes de la <b>Fuerza Estatal de Seguridad Ciudadana (FESC)</b> atacados durante un patrullaje, " + RES + " (🔴 ataque contra autoridades: el grupo inició) · <b>1 agente muerta</b> y <b>1 agente herido</b>, por titulares (El Imparcial; Punto Norte); «hieren a dos agentes», por titular (Milenio), y «dos personas heridas», por titular (Siempre en la Noticia): <code>NÚMERO DE HERIDOS CONTRADICHO — SE CUENTA 1</code> · disparo en la cabeza, " + RES + " · estado del herido: grave, por titulares (Zeta; NDT); fuera de peligro, " + RES + "; muerto, por titular de un medio abierto (Radar Tecate): <code>ESTADO DEL HERIDO CONTRADICHO — SE CUENTA 1 MUERTA Y 1 HERIDO</code> · la SSC de Baja California informó la muerte y la detención de tres participantes, " + RES + " · detención en ficha propia (ARG-142-009) · identidades: no se reproducen",
  panel="<b>Ataque a agentes estatales en patrullaje</b>: 1 agente muerta y 1 herido", inst="SSC Baja California" + PR, nac="Milenio",
  conf="★★★☆☆", campo="hora y comunicado de la SSC solo por resumen; número y estado de los heridos contradichos", I=0, N=1, R=10, A=3,
  fechadas=["El Imparcial (2026/10/26)", "Punto Norte (2026/10/26)", "The Baja Post (2026/10/26)", "Lindero Norte (2026/10/26)", "Periodismo Negro (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Nido de las Águilas, Luis Alfonso Garzón y el ataque no figuran en las cinco ediciones previas. Tecate en el índice: ARG-125-033 (29-sep, tres detenidos): otro hecho. «27-oct» en dos medios: la única ruta del 27 (Red Metropolitana) es posterior y agrupa este hecho con ARG-142-002; el día lo fijan las rutas del 26. Mismo municipio y día que ARG-142-002: hechos distintos, por colonia, hora y víctimas."),
 dict(id="ARG-142-002", estado="MX-BCN", region="Noroeste", color="rojo", impacto="grande", fecha="2026-10-26", hora="~13:00-13:38 (solo por resumen)", mu=4, he=0, cu=0, hk=13.5,
  ent="Baja California", mun="Tecate (col. El Escorial)", dia="26-OCT, POR RUTA",
  title="BAJA CALIFORNIA · TECATE — ATACAN A BALAZOS UNA VIVIENDA EN EL ESCORIAL: CUATRO MIEMBROS DE UNA FAMILIA MUERTOS",
  hecho="Tecate · <code>COL. EL ESCORIAL, CALLE EUCALIPTO O CEDRO, SOLO POR RESUMEN: CONTRADICHO</code> · lunes 26-OCT, publicado ese día, por ruta (En Línea BC; El Imparcial 2026/10/26) · " + AP + " · ~13:00-13:38, " + RES + " · <b>4 muertos</b>, por titulares (El Imparcial, «deja cuatro personas sin vida»; El Congresista) (🔴 homicidio múltiple) · «tres muertos y una mujer grave», por titular (NDT): la cuarta víctima murió en el hospital, " + RES + " · <b>sexo y edades contradichos</b>: tres mujeres y un hombre, por <i>slug</i> (En Línea BC); madre, hija y dos nietos, por titular (Milenio); una señora y tres hijos, por titular de una fuente abierta (Blog del Narco, <code>NO OFICIAL</code>); dos hermanos, su madre y otra mujer, " + RES + ": <code>COMPOSICIÓN NO FIJADA</code> · huida hacia la carretera Tecate–Tijuana o por terracería, " + RES + ": <code>CONTRADICHO</code> · fusiles de asalto, por titular (Quinta Fuerza): sin cifra · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Ataque a una vivienda: 4 muertos</b> de una familia", inst=SB, nac="Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; composición de las víctimas contradicha; ninguna fuente institucional", I=0, N=1, R=7, A=3,
  fechadas=["En Línea BC (2026/10/26)", "El Imparcial (2026/10/26)", "Red Metropolitana (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="El Escorial no figura en las cinco ediciones previas ni en el índice. NO es ARG-142-001 (otra colonia, otra hora; víctimas civiles). La Verdad y Red Metropolitana agrupan ambos hechos bajo un titular: una fuente por hecho."),
 dict(id="ARG-142-003", estado="MX-PUE", region="Centro", color="rojo", impacto="grande", fecha="2026-10-26", hora="mañana, ~9:58 (solo por resumen)", mu=1, he=1, cu=0, hk=9.97,
  ent="Puebla", mun="Tehuacán (col. Tepeyac; San Nicolás Tetitzintla en un medio)", dia="26-OCT, POR RUTA",
  title="PUEBLA · TEHUACÁN — ASESINAN A UN AGENTE DE LA AGENCIA ESTATAL DE INVESTIGACIÓN DURANTE UNA DILIGENCIA; OTRA PERSONA HERIDA",
  hecho="Tehuacán · <code>COL. TEPEYAC, CRUCE DE JUÁREZ NORTE Y 36 PONIENTE, SOLO POR RESUMEN; SAN NICOLÁS TETITZINTLA EN UN MEDIO: CONTRADICHO</code> · lunes 26-OCT, por ruta (Retodiario; Síntesis; Diario Puntual 2026/10/26) · " + AP + " · ~9:58, " + RES + "; diligencia iniciada ~9:20 por una denuncia de robo de vehículo, " + RES + "; ninguna fuente lo sitúa antes de las 08:37 · <b>1 agente muerto</b>: <b>agente de la Agencia Estatal de Investigación (FGE Puebla)</b>, adscrito a Robo de Vehículos, por titulares (🔴 víctima autoridad) · <b>1 herido</b>: «otro hombre herido», por titular (Curul); «hieren a otro», sin sustantivo, por titular (Ambas Manos); otro agente o «persona», " + RES + ": <code>CALIDAD DEL HERIDO NO FIJADA</code> · nombre y edad de la víctima contradichos entre medios: no se reproducen · detención en ficha propia (ARG-142-010)",
  panel="<b>Agente de la FGE asesinado</b> y 1 herido", inst="FGE Puebla" + PR, nac="N+ · Telediario",
  conf="★★★☆☆", campo="hora solo por resumen; calidad del herido no fijada; comunicado de la FGE solo por resumen", I=0, N=2, R=12, A=0,
  fechadas=["Retodiario (2026/10/26)", "Síntesis (2026/10/26)", "Diario Puntual (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Col. Tepeyac no figura en las cinco ediciones previas. Tehuacán en el índice: ARG-132-REC-001 (San Marcos Necoxtla, 12-oct): otro hecho. «Cinco agresiones contra policías en 17 días» (titular de Síntesis): recuento de un medio, no se integra."),
 dict(id="ARG-142-004", estado="MX-GUA", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-26", hora="~22:00; aviso al 911 ~22:20 (solo por resumen)", mu=2, he=1, cu=0, hk=22.0,
  ent="Guanajuato", mun="Acámbaro (col. Velasco Ibarra, faldas del Cerro del Toro)", dia="26-OCT, POR RUTA",
  title="GUANAJUATO · ACÁMBARO — ATAQUE ARMADO EN LA COL. VELASCO IBARRA: DOS MUERTOS Y UN HERIDO GRAVE",
  hecho="Acámbaro · <code>COL. VELASCO IBARRA, ESQUINA PRIMERA Y LUIS PASTEUR, SOLO POR RESUMEN</code> · noche del lunes 26-OCT, publicado ese día, por ruta (La Silla Rota 2026/10/26) · " + AP + " · ~22:00 o aviso ~22:20, " + RES + " · <b>2 jóvenes muertos</b> y <b>1 herido</b>, por titular y <i>slug</i> (La Silla Rota) (🔴 homicidio múltiple) · «queda 1 grave», por titular (AM 2026/10/27) · víctimas afuera de una vivienda o en la cochera, " + RES + ": contradicho · agresores huyeron, en motocicleta según vecinos, " + RES + " · la Fiscalía de Guanajuato recogió casquillos, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Ataque armado: 2 muertos</b> y 1 herido grave", inst=SB, nac="La Silla Rota · Milenio · Telediario", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=3, R=1, A=0,
  fechadas=["La Silla Rota (2026/10/26)", "AM (2026/10/27)"], estatus="Parcialmente corroborado", arm=None,
  desl="Velasco Ibarra y Cerro del Toro no figuran en las cinco ediciones previas. Acámbaro en el índice: ARG-101-007 (18-ago, 🟢): otro hecho. Ataque del Campamento Ferrocarriles (19-oct, Correo 2026/oct/19): otro hecho, otra ventana. «Dos muertos y tres heridos» (Milenio, Chicuacen): hecho del 5-sep."),
 dict(id="ARG-142-005", estado="MX-MIC", region="Occidente", color="rojo", impacto="mediano", fecha="2026-10-26", hora="no fijada", mu=0, he=0, cu=1, hk=1,
  ent="Michoacán", mun="Uruapan (huerta de aguacate cerca de Cutzato)", dia="PUB. 26-OCT; DÍA DEL HALLAZGO NO FIJADO",
  fecha_txt="publicado el 2026-10-26 — DÍA DEL HALLAZGO NO FIJADO",
  title="MICHOACÁN · URUAPAN — MADRES BUSCADORAS LOCALIZAN UNA FOSA CON RESTOS DE UN HOMBRE EN UNA HUERTA CERCA DE CUTZATO",
  hecho="Uruapan · <code>HUERTA DE AGUACATE CERCA DE CUTZATO, AL SUR DE LA CIUDAD, POR TITULAR (MIMORELIA)</code> · publicado el lunes 26-OCT, por ruta (Changoonga 2026/10/26) · " + AP + "; día del hallazgo no fijado · colectivo <b>Madres Buscadoras «Con una Luz en el Corazón»</b>, " + RES + " · <b>fosa clandestina con restos de un hombre</b>, por <i>slug</i> (Changoonga, «restos-de-un-hombre-en-una-fosa-clandestina») (🔴 fosa) · osamenta, por titular (MiMorelia) · esposas y pulsera con un nombre entre los indicios, " + RES + ": no identifican · Fiscalía de Michoacán, policía municipal y Comisión de Víctimas en el levantamiento; restos al Semefo, " + RES + " · número de cuerpos no determinado por la Fiscalía, " + RES + " · búsqueda de varios días, " + RES + ": el hallazgo puede ser anterior al 26; <code>SI RESULTA ANTERIOR A LAS 08:37 DEL 26, SE RETIRA DE ESTE TOTAL</code>",
  panel="<b>Fosa con restos de un hombre</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día del hallazgo no fijado; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Changoonga (2026/10/26)", "Grupo Marmor (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="ARG-125-036 (Cutzato, fosa con un cadáver, 28-sep, fuente única): coinciden localidad, colectivo, fosa y un hombre; lo separan dos rutas del 26-oct (Changoonga; Grupo Marmor) y los indicios (osamenta, esposas, pulsera): <code>DISTINTO POR FECHA DE PUBLICACIÓN — HALLAZGO ANTERIOR NO DESCARTADO</code>. Respuesta e IMN publican el mismo texto: una fuente."),
 # ======================= AMARILLOS
 dict(id="ARG-142-006", estado="MX-GUA", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-26", hora="~19:00-20:00 (solo por resumen)", mu=1, he=1, cu=0, hk=19.5,
  ent="Guanajuato", mun="León (Valle de San Bernardo, calle Valle de Piedras Negras)", dia="26-OCT, POR RUTA",
  title="GUANAJUATO · LEÓN — ASESINAN A UN HOMBRE EN VALLE DE SAN BERNARDO; SU ACOMPAÑANTE, HERIDO GRAVE",
  hecho="León · <code>VALLE DE SAN BERNARDO, CALLE VALLE DE PIEDRAS NEGRAS CASI ESQUINA VALLE DE LA MESA, SOLO POR RESUMEN</code> · lunes 26-OCT, por ruta (Correo; La Silla Rota; AM 2026/10/26) · " + AP + " · ~19:00-20:00, " + RES + " · <b>1 muerto</b> y <b>1 herido grave</b>, por <i>slug</i> (AM, «hay-un-herido-grave») (🟡 homicidio doloso único) · la víctima habría salido del Cereso semanas antes, por <i>slug</i> (Correo, «presuntamente»; La Silla Rota): <code>NO CONFIRMADO POR LA FISCALÍA</code> · agresores en motocicleta, " + RES + " · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="Ataque armado: <b>1 muerto</b> y 1 herido grave", inst=SB, nac="La Silla Rota · Milenio", conf="★★★☆☆",
  campo="hora solo por resumen; ninguna fuente institucional", I=0, N=2, R=2, A=0,
  fechadas=["Correo (2026/oct/26)", "La Silla Rota (2026/10/26)", "AM (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Valle de San Bernardo no figura en las cinco ediciones previas. León en el índice: ARG-140-005 (cuerpos, 21-oct): otro hecho. Ataque en la col. Chapalita (Correo 2026/oct/25, noche del sábado 24): otra ventana, otro hecho."),
 dict(id="ARG-142-007", estado="MX-MIC", region="Occidente", color="amarillo", impacto="pequeno", fecha="2026-10-26", hora="contradicha: tarde / ~03:30 (solo por resumen)", mu=1, he=0, cu=0, hk=15,
  ent="Michoacán", mun="Apatzingán (mercado Ignacio López Rayón, zona Centro)", dia="26-OCT, POR RUTA; HORA CONTRADICHA",
  title="MICHOACÁN · APATZINGÁN — ASESINAN A UN JOVEN DE 19 AÑOS EN UNA CARNICERÍA DEL MERCADO",
  hecho="Apatzingán · <code>CARNICERÍA DEL MERCADO IGNACIO LÓPEZ RAYÓN, ZONA CENTRO, POR TITULAR (RED MICHOACÁN)</code> · lunes 26-OCT, por ruta (Red Michoacán 2026/10/26) · " + AP + " · tarde, " + RES + " (Contramuro); ~03:30, " + RES + " (otra nota): <code>HORA CONTRADICHA — SI FUE DE MADRUGADA, ES DE LA VENTANA DE ARGOS 141 Y SE RETIRA DE ESTE TOTAL</code> · <b>1 muerto</b>: joven de 19 años, por titulares (Quadratín; Contramuro) (🟡 homicidio doloso único) · murió en el Hospital Regional, por titular (Red Michoacán) · agresores huyeron · <b>ningún detenido publicado</b> · identidad: no se reproduce",
  panel="Joven asesinado en un mercado: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora contradicha; ninguna fuente institucional", I=0, N=0, R=7, A=0,
  fechadas=["Red Michoacán (2026/10/26)", "Grupo Marmor (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Mercado Ignacio López Rayón no figura en las cinco ediciones previas. Apatzingán en el índice: ARG-134-REC-003, ARG-135-003, ARG-135-004 y ARG-137-016: otros hechos."),
 dict(id="ARG-142-008", estado="MX-SLP", region="Noreste", color="amarillo", impacto="pequeno", fecha="2026-10-26", hora="noche (solo por resumen)", mu=1, he=0, cu=0, hk=21,
  ent="San Luis Potosí", mun="San Luis Potosí (Anillo Periférico, a la altura de Tierra Blanca)", dia="26-OCT, POR RUTA",
  title="SAN LUIS POTOSÍ · CAPITAL — ASESINAN A BALAZOS A UN CONDUCTOR EN EL PERIFÉRICO, A LA ALTURA DE TIERRA BLANCA",
  hecho="San Luis Potosí · <code>ANILLO PERIFÉRICO A LA ALTURA DE TIERRA BLANCA, POR <i>SLUG</i></code> · lunes 26-OCT, por ruta (El Heraldo de San Luis Potosí 2026/10/26) · " + AP + " · «noche de este lunes», " + RES + " · <b>1 muerto</b>: <b>conductor</b>, por <i>slug</i> («asesinan-a-balazos-a-conductor») (🟡 homicidio doloso único) · perseguido varios kilómetros; perdió el control y chocó con el muro de contención, " + RES + " · <b>ningún detenido publicado</b> · identidad: no publicada",
  panel="Conductor asesinado a balazos: <b>1 muerto</b>", inst=SB, nac=NIN, conf="★★☆☆☆",
  campo="fuente única; hora solo por resumen", I=0, N=0, R=1, A=0,
  fechadas=["El Heraldo de San Luis Potosí (2026/10/26)"], estatus="Pendiente de corroboración", arm=None,
  desl="ARG-139-009 (conductor perseguido y asesinado, bulevar Rocha Cordero «a la altura de Tierra Blanca», noche del 20-oct, Potosinoticias 2026/10/21): coinciden municipio, punto de referencia, víctima y modo; los separan la fecha de la ruta (21 frente a 26) y el día del hecho («martes» frente a «este lunes», solo por resumen): <code>HECHO DISTINTO POR FECHA</code>. Periférico no figura en las cinco ediciones previas."),
 # ======================= VERDES
 dict(id="ARG-142-009", estado="MX-BCN", region="Noroeste", color="verde", impacto="mediano", fecha="2026-10-26", hora="tarde (tras el ataque de ARG-142-001)", mu=0, he=0, cu=0, hk=18,
  ent="Baja California", mun="Tecate", dia="26-OCT, POR RUTA",
  title="BAJA CALIFORNIA · TECATE — DETIENEN A TRES PRESUNTOS PARTICIPANTES EN EL ATAQUE A LA FUERZA ESTATAL",
  hecho="Tecate · lunes 26-OCT, tras el ataque de ARG-142-001, por ruta y titular (The Baja Post 2026/10/26, «hay tres detenidos») · " + AP + " · <b>3 detenidos</b>, por titulares (Zeta; El Congresista; The Baja Post) (🟢 detención) · «dos arrestados» en una versión preliminar, " + RES + " · operativo de reacción de los tres órdenes de gobierno con apoyo del Ejército, " + RES + " · nombres contradichos entre medios: no se reproducen · <b>armas aseguradas: no publicadas</b>",
  panel="Detención de <b>3 presuntos agresores</b> de agentes estatales", inst="SSC Baja California" + PR, nac="Milenio", conf="★★★☆☆",
  campo="comunicado de la SSC solo por resumen; nombres contradichos", I=0, N=1, R=4, A=2,
  fechadas=["The Baja Post (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Hecho distinto de ARG-142-001 (el ataque), en la misma ventana: dos fichas. NO es ARG-125-033 (Tecate, 29-sep). Detención sin armamento con cifra: fuera del conteo de armamento."),
 dict(id="ARG-142-010", estado="MX-PUE", region="Centro", color="verde", impacto="mediano", fecha="2026-10-26", hora="no fijada (tras el ataque de ARG-142-003)", mu=0, he=0, cu=0, hk=10.5,
  ent="Puebla", mun="Tehuacán", dia="26-OCT, POR RUTA",
  title="PUEBLA · TEHUACÁN — DETIENEN A UNA MUJER Y UN HOMBRE POR EL ASESINATO DEL AGENTE Y LES ASEGURAN UN AR-15",
  hecho="Tehuacán · detención el lunes 26-OCT tras el ataque de ARG-142-003, " + RES + " (MTP); «investigan a dos personas», por ruta (Retodiario 2026/10/26); primera ruta fechada que nombra la detención: 27-OCT (Intolerancia) · " + AP + " · <b>2 detenidos</b> —una mujer y un hombre—, por titular y <i>slug</i> (N+) (🟢 detención) · «hay un detenido», por titular (Puebla Online, versión de la policía municipal): <code>CIFRA CONTRADICHA — SE INTEGRA 2, LA DEL COMUNICADO DE LA FGE CITADO POR SIETE MEDIOS, SOLO POR RESUMEN</code> · <b>fusil AR-15</b>, por titular y <i>slug</i> (MTP, un solo medio); cantidad 1, «un arma larga», " + RES + ": <code>INTEGRADO CON RESERVA</code> · chaleco táctico e indicios balísticos, " + RES + " · puestos a disposición de la Fiscalía de Homicidios, sede Tehuacán, " + RES + " · identidades: no se reproducen",
  panel="Detención de <b>2</b> y aseguramiento de <b>un AR-15</b>", inst="FGE Puebla" + PR, nac="N+ · Telediario", conf="★★★☆☆",
  campo="comunicado de la FGE solo por resumen; número de detenidos contradicho", I=0, N=2, R=5, A=0,
  fechadas=["Retodiario (2026/10/26)", "Intolerancia (2026/10/27)"], estatus="Parcialmente corroborado", arm="ARG-142-ARM-001",
  desl="Hecho distinto de ARG-142-003 (el ataque), en la misma ventana: dos fichas."),
 dict(id="ARG-142-011", estado="MX-SON", region="Noroeste", color="verde", impacto="pequeno", fecha="2026-10-26", hora="no fijada", mu=0, he=0, cu=0, hk=2,
  ent="Sonora", mun="Cajeme (col. Xochiloa)", dia="PUB. 26-OCT; DÍA NO FIJADO",
  fecha_txt="publicado el 2026-10-26 — DÍA DEL HECHO NO FIJADO",
  title="SONORA · CAJEME — UN VEHÍCULO A EXCESO DE VELOCIDAD LLEVA A LA DETENCIÓN DE DOS HOMBRES ARMADOS Y AL ASEGURAMIENTO DE 22 CARTUCHOS",
  hecho="Cajeme · <code>COL. XOCHILOA, SOLO POR RESUMEN</code> · publicado el lunes 26-OCT, por ruta (El Imparcial 2026/10/26) · " + AP + "; día del hecho no fijado: <code>SI RESULTA ANTERIOR A LAS 08:37 DEL 26, SE RETIRA DE ESTE TOTAL</code> · <b>2 detenidos</b>, «dos hombres armados», por titular y <i>slug</i> (🟢 detención y aseguramiento) · <b>22 cartuchos</b>, por titular y <i>slug</i> · 2 armas cortas calibre 9 mm y 2 cargadores, " + RES + ": <code>NO SE INTEGRAN</code> · Policía Estatal, Marina y Policía Municipal, por titular (Telemax 2026/10/26)",
  panel="Detención de <b>2 hombres armados</b> y 22 cartuchos", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="día no fijado; armas y cargadores solo por resumen; ninguna fuente institucional", I=0, N=0, R=3, A=0,
  fechadas=["El Imparcial (2026/10/26)", "Telemax (2026/10/26)"], estatus="Parcialmente corroborado", arm="ARG-142-ARM-002",
  desl="Xochiloa no figura en las cinco ediciones previas. Cajeme en el índice: ARG-119-007 y ARG-133-REC-005: otros hechos."),
 # ======================= ROJOS añadidos tras procedencia-cifras R1
 dict(id="ARG-142-012", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-26", hora="tarde; primera nota ~20:03 (solo por resumen)", mu=2, he=1, cu=0, hk=17,
  ent="Michoacán", mun="Queréndaro (taller mecánico, av. Álvaro Obregón)", dia="26-OCT, POR RUTA",
  title="MICHOACÁN · QUERÉNDARO — ATAQUE ARMADO EN UN TALLER MECÁNICO: DOS MUERTOS Y UN HERIDO",
  hecho="Queréndaro · <code>TALLER MECÁNICO, AV. ÁLVARO OBREGÓN, SOLO POR RESUMEN; CERRADA DE EMILIANO ZAPATA EN UN MEDIO: CONTRADICHO</code> · lunes 26-OCT, publicado ese día, por ruta (Grupo Marmor 2026/10/26) · " + AP + " · «tarde de este lunes», " + RES + " · <b>2 muertos</b> y <b>1 herido</b>, por titulares (Quadratín; Grupo Marmor) (🔴 homicidio múltiple) · «refaccionaria», por <i>slug</i> (Contramuro) · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Ataque en un taller: 2 muertos</b> y 1 herido", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora solo por resumen; ubicación contradicha; ninguna fuente institucional", I=0, N=0, R=6, A=0,
  fechadas=["Grupo Marmor (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="Queréndaro no figura en las cinco ediciones previas ni en el índice."),
 dict(id="ARG-142-013", estado="MX-MIC", region="Occidente", color="rojo", impacto="grande", fecha="2026-10-26", hora="mañana (solo por resumen) — sin hora", mu=2, he=0, cu=0, hk=8,
  ent="Michoacán", mun="Morelia (carretera San Miguel del Monte–Tumbisca)", dia="26-OCT, MAÑANA SIN HORA",
  title="MICHOACÁN · MORELIA — ACRIBILLAN A DOS HOMBRES EN UNA CAMIONETA EN LA CARRETERA SAN MIGUEL DEL MONTE–TUMBISCA",
  hecho="Morelia · <code>CARRETERA SAN MIGUEL DEL MONTE–TUMBISCA, AL SUR DE LA CIUDAD, POR <i>SLUG</i></code> · lunes 26-OCT, publicado ese día, por ruta (Medianews 2026/10/26) · «la mañana de este lunes», " + RES + "; ninguna fuente da hora · " + FR + ": <code>SI UN ANCLA LO SITÚA ANTES DE LAS 08:37, ES DE LA VENTANA DE ARGOS 141 Y SE RETIRA DE ESTE TOTAL</code> · <b>2 hombres muertos</b>, por titulares (Quadratín; Medianews), presuntamente padre e hijo, por titular (Quadratín) (🔴 homicidio múltiple) · dentro de una camioneta, por titular (Medianews) · <b>ningún detenido publicado</b> · identidades: no se reproducen",
  panel="<b>Dos hombres asesinados</b> en una camioneta", inst=SB, nac=NIN, conf="★★★☆☆",
  campo="hora no fijada (frontera con la ventana de ARGOS 141); ninguna fuente institucional", I=0, N=0, R=4, A=0,
  fechadas=["Medianews (2026/10/26)"], estatus="Parcialmente corroborado", arm=None,
  desl="San Miguel del Monte y Tumbisca no figuran en las cinco ediciones previas ni en el índice."),
]

# ---------------------------------------------------------------- RECUPERACIONES (ventana de ARGOS 141; solo alto impacto)
R = []

# ---------------------------------------------------------------- ARMAMENTO (solo hechos propios)
# cortas, largas, sincat, especial, cartuchos, cargadores, granadas, aei, explosivos, detenidos
ARM = [
 dict(id="ARG-142-ARM-001", ficha="ARG-142-010", estado="MX-PUE", region="Centro", color="rojo", ent="Puebla", mun="Tehuacán",
  fecha="2026-10-26", fecha_txt="26-oct", hora="mañana", c=[0, 1, 0, 0, 0, 0, 0, 0, 0, 2], nd=[0, 2, 3, 4, 5, 6, 7, 8], integra=True,
  corp="FGE Puebla y Seguridad Pública municipal <span class=\"muted-note\">(solo por resumen)</span>", conf="Bajo",
  nota="vinculado a ARG-142-003 (🔴 en el mapa); ver ARG-142-010",
  fuentes=["Retodiario (2026/10/26)", "N+ (sin fecha en la ruta)", "MTP Noticias (sin fecha en la ruta)"]),
 dict(id="ARG-142-ARM-002", ficha="ARG-142-011", estado="MX-SON", region="Noroeste", color="verde", ent="Sonora", mun="Cajeme (col. Xochiloa)",
  fecha="2026-10-26", fecha_txt="pub. 26-oct; día no fijado", hora="no fijada", c=[0, 0, 0, 0, 22, 0, 0, 0, 0, 2], nd=[0, 1, 2, 3, 5, 6, 7, 8], integra=True,
  corp="Policía Estatal, Marina y Policía Municipal <span class=\"muted-note\">(por titular)</span>", conf="Bajo",
  nota="ver ARG-142-011",
  fuentes=["El Imparcial (2026/10/26)", "Telemax (2026/10/26)"]),
]
TOT = [sum(a["c"][i] for a in ARM if a["integra"]) for i in range(10)]
ARMAS = TOT[0] + TOT[1] + TOT[2] + TOT[3]
ND = [any(a["integra"] for a in ARM) and all(i in a.get("nd", []) for a in ARM if a["integra"]) for i in range(10)]
def tv(i, f=str): return "n/d" if ND[i] else f(TOT[i])
cnt = {k: sum(1 for e in E if e["color"] == k) for k in ("rojo", "amarillo", "verde")}
cnt_rec = {k: sum(1 for r in R if r["col_orig"] == k) for k in ("rojo", "amarillo", "verde")}
ENT = sorted(set(e["estado"] for e in E))
MU = sum(e["mu"] for e in E); HE = sum(e["he"] for e in E); CU = sum(e["cu"] for e in E)
MU_REC = sum(r["mu"] for r in R); HE_REC = sum(r["he"] for r in R)
NFR = sum(1 for e in E if "FRONTERA DE VENTANA" in e["hecho"])
NAP = sum(1 for e in E if "DÍA DE APERTURA" in e["hecho"])
HORAS = 24 + 8 / 60
DENS = f"{len(E) / HORAS:.2f}".replace(".", ",")
ENT_ROJO = sorted(set(e["estado"] for e in E if e["color"] == "rojo"))
DET = sum(a["c"][9] for a in ARM if a["integra"])
assert TOT == [0, 1, 0, 0, 22, 0, 0, 0, 0, 4], TOT
assert ND == [True, False, True, True, False, True, True, True, True, False], ND
assert cnt == {"rojo": 7, "amarillo": 3, "verde": 3}, cnt
assert cnt_rec == {"rojo": 0, "amarillo": 0, "verde": 0}, cnt_rec
assert (MU, HE, CU, MU_REC, HE_REC) == (15, 5, 1, 0, 0), (MU, HE, CU, MU_REC, HE_REC)
assert (NFR, NAP, len(ENT), len(ENT_ROJO)) == (1, 12, 6, 4), (NFR, NAP, len(ENT), len(ENT_ROJO))
assert DENS == "0,54", DENS
assert sorted(e["id"] for e in E) == [f"ARG-142-{i+1:03d}" for i in range(len(E))]
for x in E + R:
    assert x["I"] + x["N"] + x["R"] + x["A"] > 0 and (x["fechadas"] or x["conf"] == "★★☆☆☆"), x["id"]
    assert x["fecha"] >= "2026-10-26" or x in R, x["id"]

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
head = head.replace("<title>ARGOS 141 — Reporte Nacional de Seguridad — 2026-10-26</title>", f"<title>ARGOS {NUM} — Reporte Nacional de Seguridad — {FECHA}</title>")
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
      <b>1. SOLICITE A LA SSC Y A LA FISCALÍA DE BAJA CALIFORNIA EL ESTADO DEL AGENTE LESIONADO Y EL REGISTRO DE LAS ARMAS ASEGURADAS A LOS DETENIDOS, Y AUDITE EL PROTOCOLO DE PATRULLAJE EN LA COLONIA</b> (ARG-142-001).
      <br><b>2. SOLICITE A LA FISCALÍA DE BAJA CALIFORNIA EL NÚMERO, SEXO E IDENTIDAD DE LAS VÍCTIMAS, EL VEHÍCULO Y LA RUTA DE HUIDA DE LOS AGRESORES</b> (ARG-142-002).
      <br><b>3. SOLICITE A LA FGE PUEBLA LA CALIDAD DEL LESIONADO, LA SITUACIÓN JURÍDICA DE LOS DETENIDOS Y EL DICTAMEN BALÍSTICO DEL FUSIL</b> (ARG-142-003).
      <br><b>4. SOLICITE A LA FGE GUANAJUATO EL DICTAMEN DE LOS CASQUILLOS Y EL ESTADO DEL LESIONADO, Y COTEJE EL DICTAMEN CON SU REGISTRO BALÍSTICO ESTATAL</b> (ARG-142-004).
      <br><b>5. SOLICITE A LA FISCALÍA DE MICHOACÁN LA IDENTIFICACIÓN GENÉTICA DE LOS RESTOS Y SU COTEJO CON LAS FICHAS DE BÚSQUEDA DEL COLECTIVO</b> (ARG-142-005).
    </p>
  </div>

{footer()}</section>
'''

ORD = {"rojo": 0, "amarillo": 1, "verde": 2}
rows_own = "\n".join(prow(e) for e in sorted(E, key=lambda x: (ORD[x["color"]], [-ord(ch) for ch in x["fecha"]], -x["hk"])))
panorama_body = f'''  <p class="muted-note" style="margin:0 0 6px 0;">
    Ventana <b>26-oct 08:37 → 27-oct 08:45 CDMX</b> (<b>{DUR}</b>) · <b>{len(E)} hechos propios</b> en <b>{len(ENT)} entidades</b> ·
    <b>densidad {DENS} hechos/hora</b>; duración y densidad, <b>cálculo propio</b> · dentro de cada color, del más reciente al más antiguo · <b>ninguna recuperación de la ventana anterior</b>.
  </p>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Entidad · Municipio</th><th>Hecho</th><th>Nivel de riesgo</th><th>Fuente institucional</th><th>Fuente nacional</th><th>Confianza</th><th>ARG-ID</th></tr></thead>
    <tbody>
{rows_own}
    </tbody>
  </table></div>

  <div class="section-head" style="margin-top:10px;">TOTALES DEL CORTE — CÁLCULO PROPIO DE ARGOS</div>
  <p class="muted-note" style="margin:0 0 6px 0;">
    <code>NINGUNA AUTORIDAD PUBLICÓ UN AGREGADO NACIONAL DE ESTA VENTANA.</code>
  </p>
  <div class="table-wrap"><table class="exec wide">
    <thead><tr><th>Hechos propios</th><th>🔴</th><th>🟡</th><th>🟢</th><th>Recup.</th><th>Muertos por agresión</th><th>Heridos</th><th>Cuerpos hallados</th><th>Armas cortas</th><th>Armas largas</th><th>Armas sin categoría</th><th>Cartuchos</th><th>Cargadores</th><th>Granadas</th><th>AEI</th><th>Explosivos</th><th>Detenidos en aseguramiento</th><th>Entidades</th></tr></thead>
    <tbody><tr><td><b>{len(E)}</b></td><td><b>{cnt["rojo"]}</b></td><td><b>{cnt["amarillo"]}</b></td><td><b>{cnt["verde"]}</b></td><td><b>{len(R)}</b></td><td><b>{MU}</b></td><td><b>{HE}</b></td><td><b>{CU}</b></td><td><b>{tv(0)}</b></td><td><b>{tv(1)}</b></td><td><b>{tv(2)}</b></td><td><b>{tv(4, fmt)}</b></td><td><b>{tv(5)}</b></td><td><b>{tv(6)}</b></td><td><b>{tv(7)}</b></td><td><b>{tv(8)}</b></td><td><b>{TOT[9]}</b></td><td><b>{len(ENT)}</b></td></tr></tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Armamento</b>: 2 eventos contabilizados (ARG-142-ARM-001 y -002), cifras solo por <i>slug</i>; <code>n/d</code> = no publicado en fuente citable, no ausencia · detención de ARG-142-009 sin armamento con cifra: fuera de este total · <b>detenidos en aseguramiento</b>: cifras por titulares de medios; la autoridad, solo por resumen · <b>heridos</b>: 1 contado en ARG-142-001, contradicho (2 en dos medios) · <b>cuerpos hallados</b>: restos de 1 hombre en fosa (ARG-142-005) · <b>marcas</b>: {NAP} <code>PUBLICADO EL DÍA DE APERTURA SIN HORA</code> y {NFR} <code>FRONTERA DE VENTANA — HORA NO FIJADA</code> · <b>totales sujetos a las cláusulas de retiro de las fichas</b>: ARG-142-005 (−1 rojo, −1 cuerpo), -007 (−1 amarillo, −1 muerto), -011 (−1 verde, −22 cartuchos, −2 detenidos, −1 entidad), -013 (−1 rojo, −2 muertos); detenidos de ARG-142-010 contradichos (2 o 1); si un medio abierto acierta en ARG-142-001, +1 muerto y −1 herido. <b>Cálculo propio</b>.
    <br><b>Seguimientos de ediciones previas, fuera del semáforo</b>: <b>ARG-136-006 (exfiscal)</b>: impugnación de la vinculación anunciada por la defensa, por <i>slug</i> (Proceso 2026/10/25); sin resolución publicada; <code>NINGUNA ES SENTENCIA</code> · <b>ARG-140-020 (Xalapa)</b>: prisión preventiva oficiosa, por <i>slug</i> (Golpe Político 2026/10/24); vinculación no publicada · <b>ARG-140-021 (Juchitán)</b>: vinculación no publicada · <b>ARG-140-005 (León)</b>: 4 cuerpos por titulares (AM 2026/10/21 y 2026/10/23, este con declaración del fiscal); 5 por titular y <i>slug</i> (La Silla Rota 2026/10/21; también Quadratín Michoacán y Quadratín Bajío): <code>CIFRA CONTRADICHA ENTRE TITULARES — REVERIFICADA EL 27-OCT</code> · <b>ARG-140-013 (Linares)</b>: identificación publicada (MVS 2026/10/26); edad 47 {RES} (MVS), 55 heredado de ARGOS 140, también {RES}: <code>CONTRADICHA</code> · <b>ARG-141-001 (Pénjamo)</b>: muerte sin confirmación de autoridad; la confirmada por la Fiscalía, por titular (Correo 2026/oct/26), es de la calle Independencia, zona centro: otro hecho · <b>ARG-141-004 (Culiacán)</b>: un solo cuerpo, por titular (Luz Noticias 2026-10-25); denuncia previa de desaparición no publicada.
  </p>
'''

byid = {e["id"]: e for e in E}
co1 = "\n".join(ficha(byid[i]) for i in ("ARG-142-001", "ARG-142-009", "ARG-142-002", "ARG-142-003", "ARG-142-010"))
co2 = "\n".join(ficha(byid[i]) for i in ("ARG-142-004", "ARG-142-012", "ARG-142-013", "ARG-142-005"))
co3 = "\n".join(ficha(byid[i]) for i in ("ARG-142-006", "ARG-142-007", "ARG-142-008", "ARG-142-011"))
assert sorted(re.findall(r'id="(ARG-142-0\d\d)"', co1 + co2 + co3)) == sorted(byid)

ico = re.findall(r'<div class="tile[^"]*"><svg class="ico ico-lg"[^>]*>.*?</svg>', tpl)
icos = [re.search(r'<svg.*</svg>', x).group(0) for x in ico]
def tile(i, lbl, num, sub):
    cero = " cero" if num in (0, "0") else ""
    return f'    <div class="tile{cero}">{icos[i]}<span class="lbl">{lbl}</span><span class="num">{num}</span><span class="sub">{sub}</span></div>'
NI = "<code>NO PUBLICADO EN FUENTE CITABLE</code> en los dos eventos"
tiles = "\n".join([
 tile(0, "Armas cortas", tv(0), NI + " (2 cortas en Cajeme, solo por resumen)"),
 tile(1, "Armas largas", tv(1), "AR-15 por titular (Tehuacán); cantidad solo por resumen"),
 tile(2, "Sin categoría", tv(2), NI),
 tile(3, "Cartuchos", tv(4, fmt), "por titular (Cajeme)"),
 tile(4, "Cargadores", tv(5), NI),
 tile(5, "Granadas", tv(6), NI),
 tile(6, "AEI", tv(7), NI),
 tile(7, "Explosivos", tv(8), NI),
 tile(8, "Armamento especial", tv(3), NI),
 tile(9, "Detenidos", tv(9), "<b>en el mismo evento de aseguramiento</b>, por titulares de medios; autoridad solo por resumen; Tehuacán 2 o 1: contradicho"),
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
    <div class="map-caption">Dos aseguramientos contabilizados: Puebla y Sonora.</div>
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
    <b>Lectura regional</b>: Centro, 1 evento (1 arma larga, 2 detenidos) · Noroeste, 1 evento (22 cartuchos, 2 detenidos); el resto de regiones, sin evento integrable. <b>Cálculo propio</b>.
    <br><b>Eventos cualitativos sin cantidad</b>: ninguno · armas de los agresores sin aseguramiento publicado: Tecate (ARG-142-001 y -002), fuera de esta sección.
    <br><code>VISTOS, NO INTEGRADOS</code>: <b>boletín federal del 23 al 25-oct</b> (ventana de ARGOS 141, día de cada acción no fijado; también en Milenio): Mazatlán (11 granadas artesanales, 1 arma larga y 8 cargadores), Zacatecas y Tamaulipas: cifras {RES} · <b>Sonora</b>: operativo con 4 detenidos y un presunto mando abatido, sábado 24 (ventana de ARGOS 140) · <b>Veracruz</b>: 27 detenidos {RES} en operativos del 24 y 25-oct (Golpe Político 2026/10/26), agregado sin desglose · <b>Coahuila, Piedras Negras</b>: 39 cartuchos por <i>slug</i>, 1 arma y 3 cargadores {RES}, en el Puente Internacional II, día no fijado · <b>Nayarit, El Jicote</b>: <code>EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE</code>, junto con la sentencia · <b>balances semanales de Sonora, Quintana Roo y Coahuila</b>: recuentos, no se integran.
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
      <tr><td><b>Nayarit</b><br>Tepic (El Jicote)</td><td>Portación de armas de uso exclusivo del Ejército; <b>2 sentenciados</b>, por titular (Argonmexico 2026/10/26)</td><td><b>15 años</b>, por titular (Argonmexico; NX Noticias); «más de 15 años», por <i>slug</i> (Nayarit Noticias 2026/10/26); «6 meses» y multa, {RES}; sin precisar si es por persona</td><td>FGR <span class="muted-note">(por medios)</span></td><td><code>PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL</code> · boletín de la FGR no leído · fecha de la sentencia no fijada · {AP}</td><td>Bajo</td></tr>
      <tr><td><b>Hidalgo</b><br>Santiago Tulantepec</td><td>Fallo condenatorio por el triple feminicidio, publicado el 9-oct, por <i>slug</i> (La Silla Rota 2026/10/9); fecha del fallo no fijada</td><td><b>Sin pena</b>: audiencia de individualización el 28-oct a las 17:00, {RES} · <b>sin cambio desde ARGOS 141</b></td><td>Tribunal de Enjuiciamiento de Tulancingo <span class="muted-note">(por medios)</span></td><td><code>FALLO SIN PENA — PENDIENTE DE CONFIRMACIÓN OFICIAL</code> · sin boletín de la PGJEH</td><td>Bajo</td></tr>
      <tr><td><b>Coahuila</b><br>Ramos Arizpe (ejido Paredón)</td><td>Transporte de un kilo de metanfetamina, {RES}</td><td>7 años 6 meses y 75 UMA, {RES}</td><td>FGR</td><td><code>POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN</code> · ninguna ruta fechada · boletín no leído</td><td>No confirmado</td></tr>
    </tbody>
  </table></div>
  <p class="muted-note" style="margin:6px 0 0 0;">
    <b>Publicadas antes de la ventana, no integrables</b>: FGR Veracruz, Pánuco (Hora Cero 2026/10/22; número de comunicado, fecha 21-oct y pena {RES}) · FGR Caborca (Dossier Político 2026/10/19; pena {RES}) · FGE Colima, más de 46 años por <i>slug</i> (22-oct) · FGE Quintana Roo, 140 años por <i>slug</i> (fecha 18-oct {RES}) · FGE Querétaro (2026/10/22) · FGE Jalisco, El Salto (comunicado 20261019; pena {RES}) · FGE Durango (portada del dominio; fechas {RES}). <code>NO SE INTEGRAN</code>.
  </p>
  <div class="section-head" style="margin-top:10px;">INDICADOR DE COBERTURA</div>
  <div class="table-wrap"><table class="exec">
    <thead><tr><th>Renglón</th><th>Resultado</th></tr></thead>
    <tbody>
      <tr><td><b>FGR revisada</b></td><td><b>Sí</b>, por búsqueda dirigida: listados de <code>fgr.org.mx</code> y <code>gob.mx/fgr</code>: <code>SIN RESULTADO INDEXADO EN VENTANA</code>; las candidatas atribuidas a la FGR constan solo por medios</td></tr>
      <tr><td><b>Fiscalías revisadas en sentencias</b></td><td><b>19 de 32</b>, por búsqueda dirigida que devolvió páginas del dominio; acceso directo: 0 · BC, BCS, Sin, Chih, Dgo · SLP, Zac · Jal, Col, Mich · Pue, Qro · Ver, Tab · Oax, Gro, Chis, Yuc, QRoo</td></tr>
      <tr><td><b>Fiscalías con sentencia publicada en la ventana</b></td><td><b>0</b></td></tr>
      <tr><td><code>SIN RESULTADO INDEXADO EN VENTANA</code></td><td><b>19</b> fiscalías estatales revisadas</td></tr>
      <tr><td><code>SIN ACTUALIZACIÓN CONSTATADA</code></td><td><b>0</b></td></tr>
      <tr><td><b>Dominio consultado sin páginas devueltas</b></td><td><b>4</b>: Son · Coah · Nay · Camp</td></tr>
      <tr><td><code>NO REVISADA</code> — sentencias</td><td><b>9</b>: NL, Tamps · Ags, Gto · CDMX, Edomex, Mor, Tlax, Hgo</td></tr>
      <tr><td><b>Páginas no disponibles · errores de acceso</b></td><td><b>Fuentes con error de acceso</b>: bloqueo de egreso: <code>curl</code> a <code>www.gob.mx/fgr</code>, 27-oct 08:45: código <code>000</code> · <b>dominios confirmados en esta edición</b>: <code>fge.chiapas.gob.mx</code>, <code>fgecolima.mx</code>, <code>comunicacion.fiscaliamichoacan.gob.mx</code>, <code>pgjebcs.gob.mx</code>, <code>veracruz.gob.mx/seguridad</code></td></tr>
      <tr><td><b>Alto impacto y armamento</b></td><td><b>Alto impacto: 22 de 32 con consulta propia por entidad</b> · <b>10 solo por consulta regional amplia</b>: BCS, Son, Sin · Jal, Col, Nay · CDMX, Tlax · Camp, Yuc · <b>armamento: 11 de 32 por dominio oficial</b> —NL, Tamps, SLP · Col, Mich · Edomex · Ver, Tab · Gro, Yuc, QRoo—, todas <code>SIN RESULTADO INDEXADO EN VENTANA</code> · dominio sin páginas: Oax · <code>NO REVISADA</code> (20): BC, BCS, Son, Sin, Chih, Dgo · Coah, Zac · Jal, Nay, Ags, Gto · CDMX, Mor, Pue, Tlax, Hgo, Qro · Chis, Camp</td></tr>
      <tr><td><b>Boletín federal</b></td><td><b>Acciones del 26-oct</b>: <code>SIN RESULTADO INDEXADO EN VENTANA</code> en día suelto, por rango y por título (al arrancar la ola y a las 09:16) · el último indexado es el agregado del 23, 24 y 25-oct (ventana de ARGOS 141) · Guardia Nacional: una nota sin fecha · Defensa, Semar y ANAM: <code>NO REVISADAS</code></td></tr>
      <tr><td><b>Techo de confianza del producto</b></td><td><b>★★★★☆</b> (techo de política) · esta edición no supera <b>★★★☆☆</b>: sin lectura directa de documento oficial · <code>BLOQUEO DE EGRESO REVERIFICADO EL 27-OCT 08:45: GOB.MX</code></td></tr>
    </tbody>
  </table></div>
'''

cierre = f'''  <div class="alerta contexto">
    <div class="flag">VALORACIÓN ARGOS — NIVEL DE RIESGO NACIONAL</div>
    <p>
      <b>1.</b> <b>Siete rojos propios en cuatro entidades</b> (cálculo propio) —dos ataques contra personal de seguridad y procuración, cuatro homicidios múltiples y una fosa—: riesgo nacional del corte con incremento acreditado.
      <br><b>2.</b> <b>Concentración</b>: Michoacán y Baja California suman cinco de los siete rojos (cálculo propio).
      <br><b>3.</b> <b>Violencia operativa</b>: tres amarillos, todos homicidios dolosos únicos (cálculo propio); ningún enfrentamiento derivado de operativo.
      <br><b>4.</b> <b>Respuesta institucional</b>: tres verdes, todos detenciones, en tres entidades (cálculo propio).
      <br><b>5.</b> <code>{NAP + NFR} DE {len(E)} HECHOS SIN HORA FIJADA POR FRAGMENTO ({NAP} PUBLICADOS EL DÍA DE APERTURA, {NFR} EN FRONTERA) Y VENTANA DE {DUR.upper()}: TOTALES NO COMPARABLES CON ARGOS 141 SIN NORMALIZAR POR HORA. CÁLCULO PROPIO.</code>
    </p>
  </div>

  <div class="alerta contexto" style="margin-top:8px;">
    <div class="flag">CONCLUSIONES DE INTELIGENCIA CRIMINAL</div>
    <p>
      <b>1. APATZINGÁN: QUINTO HECHO CON VÍCTIMAS DEL ÍNDICE EN CATORCE DÍAS</b> (cálculo propio, 13 al 26-oct, ambos extremos; desarrolla el patrón de ARGOS 135 y 137): ARG-134-REC-003, ARG-135-003, ARG-135-004, ARG-137-016 y ARG-142-007; tres sin día fijado por fragmento; cuatro si ARG-142-007 se retira. Línea: <b>solicitar a la Fiscalía de Michoacán el cotejo balístico de los cinco y vigilar la zona Centro y el mercado</b> — hipótesis.
      <br><b>2. MICHOACÁN: DOS HOMICIDIOS DOBLES EL MISMO LUNES, UNO EN UN NEGOCIO Y OTRO EN UN VEHÍCULO EN CARRETERA</b> (cálculo propio; ARG-142-012 y ARG-142-013); el segundo, en frontera de ventana. Línea: <b>solicitar a la Fiscalía de Michoacán la identificación de las víctimas y el cotejo balístico entre ambos</b> — vínculo no acreditado.
      <br><b>3. SAN LUIS POTOSÍ: SEGUNDO CONDUCTOR ASESINADO A BALAZOS A LA ALTURA DE TIERRA BLANCA EN SIETE DÍAS</b> (cálculo propio, 20 y 26-oct): ARG-139-009 y ARG-142-008; el día de ARG-139-009, solo por resumen; ARG-142-008, de fuente única. Línea: <b>solicitar a la Fiscalía de San Luis Potosí si son dos hechos y si comparten armas</b>.
      <br><b>4. LEÓN: TRES HECHOS CON VÍCTIMAS EN SEIS DÍAS</b> (cálculo propio, 21 al 26-oct): ARG-140-005 (cuerpos), ataque de la col. Chapalita (24-oct, Correo 2026/oct/25, sin ARG-ID) y ARG-142-006; agresores en motocicleta en los dos últimos, solo por resumen. Línea: <b>solicitar a la FGE Guanajuato si comparten agresores y la situación jurídica de la víctima de ARG-142-006</b> — hipótesis.
      <br><b>5. BRECHA DETENCIÓN–CONDENA: SIETE DETENIDOS EN TRES ACCIONES DEL CORTE —CINCO TRAS LOS DOS ATAQUES A AGENTES— Y NINGUNA SENTENCIA INTEGRABLE</b> (cálculo propio: 3 en ARG-142-009, 2 en -010 y 2 en -011; de ellos, 4 en eventos de aseguramiento); la única con pena por titular, por portación de armas exclusivas en Tepic, solo por medios; detenidos contradichos en -009 y -010. Línea: <b>solicitar a las fiscalías de Baja California y Puebla la vinculación y el registro balístico de las armas, y a la FGR el boletín de Tepic</b>.
    </p>
  </div>

  <div class="section-head" style="margin-top:10px;">INDICADORES OFICIALES</div>
  <p class="muted-note" style="margin:0;">
    <b>gabinetedeseguridad.gob.mx/resultados</b> — <code>NO REVISADA</code>; lectura directa no disponible. <b>SESNSP e INEGI</b>: <code>NO REVISADOS</code> en esta edición · <b>FGR</b>: SRIV (<code>gob.mx/fgr</code>).
    <br><b>Toda cifra de este cartelón sin emisor nombrado es cálculo propio de ARGOS.</b> Los ARG-ID de ediciones previas citados en las conclusiones no se reverificaron en esta edición.
  </p>
'''

body = (port
 + page("PANORAMA DEL CORTE — ÍNDICE EJECUTIVO POR ENTIDAD", panorama_body)
 + page("CRIMEN ORGANIZADO (I) — ATAQUES A AUTORIDADES Y HOMICIDIO MÚLTIPLE: BAJA CALIFORNIA Y PUEBLA", co1)
 + page("CRIMEN ORGANIZADO (II) — HOMICIDIOS MÚLTIPLES Y FOSAS: GUANAJUATO Y MICHOACÁN", co2)
 + page("CRIMEN ORGANIZADO (III) — VIOLENCIA OPERATIVA Y ACCIONES INSTITUCIONALES: GUANAJUATO, MICHOACÁN, SAN LUIS POTOSÍ Y SONORA", co3)
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
assert "WINDOW_DAYS = 2;" in script  # la ventana toca dos fechas de calendario (26 y 27-oct); la plantilla de 141 ya trae 2
open(sys.argv[2], "w", encoding="utf-8").write(head + body + script + tail)
print("ok", cnt, cnt_rec, TOT, ARMAS, len(E), len(R), NFR, NAP, MU, HE, CU, DENS)
