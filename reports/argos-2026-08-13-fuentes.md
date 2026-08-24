# ARGOS 96 — Registro de fuentes (auditoría)

Corte: 2026-08-13 · Ventana de hechos: tarde del 2026-08-12 a mañana del 2026-08-13. Continuación
de ARGOS 95 (corte 2026-08-12). Este documento respalda `argos-2026-08-13.html` con los enlaces
exactos consultados para cada hecho, conforme al requisito de trazabilidad de `CLAUDE.md`. Cuatro
equipos de investigación (`osint-fuentes`) trabajaron en paralelo — ataques/desapariciones, economía
criminal, barrido de armamento, barrido de sentencias — todos contrastando sus hallazgos contra
`reports/argos-2026-08-12-fuentes.md` para evitar duplicidad con ARG-95-001 a 008, ARG-95-ARM-001 a
003 y ARG-95-SEN-001 a 007.

**Limitación metodológica confirmada de nuevo en este corte: `WebFetch` devolvió `EGRESS_BLOCKED`
para todo dominio externo probado** por los cuatro equipos (incluidos `gob.mx/sspc`, `gob.mx/fgr`,
`gob.mx/semar`, `gob.mx/sedena`, `gob.mx/guardianacional`, `fgr.org.mx`, `infobae.com`,
`jornada.com.mx`, portales estatales y numerosos medios) — mismo resultado que ARGOS 90 a 95. Ningún
documento primario se leyó por acceso directo; toda la información proviene de fragmentos de
resultados de `WebSearch`. Techo de confianza aplicado: Medio (★★★☆☆) salvo donde se indique lo
contrario. Se detectaron y descartaron al menos tres casos de conflación de fechas por el resumen
automático de `WebSearch` (Coahuila 2023, Durango junio-2026, Zitácuaro julio-2026) — documentados
abajo en la sección de pistas descartadas.

**Nota de consolidación entre equipos**: el operativo FGR/AIC en ocho estados (huachicol, tráfico de
armas y narcotráfico transnacional) fue localizado de forma independiente por el equipo de economía
criminal y por el equipo de armamento. Se consolidó bajo un único ARG-ID (`ARG-96-003`), documentado
como tarjeta de Crimen Organizado II (página 4) y referenciado en la tabla de armamento (página 5)
sin duplicar cifras — mismo criterio que ARGOS 95 aplicó a Concordia (`ARG-95-005`).

**Hallazgo relevante de este corte**: regresa un evento 🔴 ROJO tras el primer corte sin rojo de la
serie (ARGOS 95): ataque armado directo contra un campamento militar del Ejército en Tayoltita, San
Dimas, Durango (`ARG-96-001`). Un evento 🟡 AMARILLO adicional (`ARG-96-002`, Chihuahua capital).
Cuatro eventos 🟢 VERDE de economía criminal (`ARG-96-003` a `006`) y un evento 🟢 VERDE de armamento
puro (`ARG-96-ARM-001`). Ocho sentencias condenatorias nuevas (`ARG-96-SEN-001` a `008`).

**Posibles vacíos de cobertura señalados para auditoría retroactiva de ARGOS 94/95** (no se
incorporan como hechos de este corte, por caer fuera de su ventana):

- Ataque con artefacto explosivo lanzado por dron, La Estanzuela, Aquila, Michoacán (un muerto, un
  herido) — fecha en disputa entre fuentes (tarde 11-ago o mañana 12-ago 2026), en cualquier caso
  dentro de la ventana nominal de ARGOS 95, no documentado en `argos-2026-08-12-fuentes.md`.
- Quema de dos camiones de volteo, Sabanillas/Tuxpan-Tamiahua, Veracruz, y homicidio de un tráilero
  en la carretera Nuevo Teapa-Cosoleacaque, sur de Veracruz (ambos 11-ago), no documentados en
  ARGOS 95.
- Detención de Gerardo Humberto Piña, alias "El G1"/"El Gera" (célula de Maneadero, Cártel de
  Sinaloa), Ensenada, Baja California (hecho: tarde del 11-ago, publicado 12-ago), no documentada en
  ARGOS 95.
- Detención de Erick Jesús "N", alias "El Loco" (presunta Familia Michoacana), Metepec, Estado de
  México (hecho: 10-ago), no documentada en ARGOS 94 ni 95.
- Detención de dos funcionarios de la Secretaría de Medio Ambiente del Edomex por presunta red de
  extorsión a verificentros y gasolineras (hecho: 10-ago), no documentada en ARGOS 94 ni 95.
- Boletín del Gabinete de Seguridad "acciones relevantes del 11 de agosto de 2026": detención de
  Alfredo "N" en Huajicori, Nayarit, con 1 fusil Barrett, 4 armas largas, 8 cargadores, 235
  cartuchos, 2 AEI y 1 inhibidor de señal de drones — no documentado en ARGOS 95 pese a caer dentro
  de su ventana.
- Fallo condenatorio (sin pena individualizada aún) contra Gabriela "N" por secuestro agravado de 5
  personas, Villas del Pedregal, Morelia (hechos oct-2022), publicado 11-ago — fuera de la ventana
  estricta de ARGOS 96; se da seguimiento en el próximo corte cuando se espere la audiencia de
  individualización de sanción.

Se señalan aquí, con el mismo criterio que ARGOS 95 aplicó al caso de la taquería "Fermín" en
Zapopan, para revisión editorial retroactiva; no se recalifican las ediciones previas desde aquí.

---

## Crimen organizado I — ataques a autoridades y violencia operativa

### ARG-96-001 — Ataque armado contra campamento militar del Ejército, Tayoltita, San Dimas, Durango (🔴 ROJO)

- Nacional: [Reforma](https://www.reforma.com/chocan-militares-y-civiles-armados-en-durango-abaten-a-uno/ar3256907) ·
  [La Jornada](https://www.jornada.com.mx/noticia/2026/08/12/estados/un-muerto-y-dos-militares-lesionados-deja-enfrentamiento-armado-en-tayoltita-durango)
- Regional: [POSTA México](https://www.posta.com.mx/durango/reportan-ataque-a-militares-en-tayoltita-durango-este-12-de-agosto-esto-se-sabe/vl2242480) ·
  [El Siglo de Durango](https://www.elsiglodedurango.com.mx/noticia/2026/militares-repelen-agresion-armada-en-tayoltita-4-personas-habrian-muerto-cifra-extraoficial.html) ·
  [Red Metropolitana](https://www.redmetropolitana.com.mx/2026/08/12/un-muerto-y-dos-militares-lesionados-deja-enfrentamiento-armado-en-tayoltita-durango/) ·
  [El Diario de Chihuahua](https://www.eldiariodechihuahua.mx/nacional/2026/aug/12/chocan-militares-y-civiles-armados-en-durango-abaten-a-uno-827061.html) ·
  [Plano Informativo](https://planoinformativo.com/1163154/chocan-militares-y-civiles-armados-en-durango-abaten-a-uno-) ·
  [Viva la Noticia Durango](https://vivalanoticiadgo.mx/2026/08/12/ataque-armado-tayoltita-durango/)

Sin fuente institucional directa: SEDENA y el Gabinete de Seguridad no habían emitido comunicado
propio al momento de la consulta (2026-08-13), más de 24 horas después del hecho — vacío operativo
señalado para el corte siguiente.

12-ago-2026, ~06:00 h, inmediaciones de la pista aérea de Tayoltita, cabecera de San Dimas, Durango
(Sierra Madre Occidental, franja de conexión con Sinaloa). Un grupo de civiles armados llegó al
campamento donde el Ejército mantiene presencia y abrió fuego contra el personal militar, que
repelió la agresión; se solicitó refuerzo terrestre y apoyo aéreo. Saldo de la versión mayoritaria
(Reforma, La Jornada, POSTA, Red Metropolitana, Diario de Chihuahua): un presunto agresor abatido y
dos elementos del Ejército heridos, atendidos médicamente. Sin identidad de los agresores, sin
atribución confirmada a organización criminal, sin detenidos reportados al momento de la consulta.
**Contradicción sin resolver**: El Sol de Durango reporta "dos presuntos agresores sin vida" y El
Siglo de Durango cita por separado una cifra extraoficial de "4 personas habrían muerto" — no se
puede establecer cuál versión es correcta con las herramientas disponibles.

**Explotación ARGOS**: un ataque directo contra una posición militar (no una persecución derivada de
otro delito) es consistente con la hipótesis de disputa territorial activa entre facciones del
Cártel de Sinaloa en la franja serrana Durango-Sinaloa — hipótesis que requiere validación
institucional. Líneas a explotar: balance oficial de bajas/heridos por SEDENA, identidad de los
agresores, detenidos en el despliegue posterior. La ausencia de comunicado institucional más de 24 h
después del hecho es en sí un vacío relevante para el seguimiento de ARGOS 97.

**Trazabilidad**: `ARG-96-001` · Nivel de confianza: 🟡 Medio (★★★☆☆ — corroboración nacional y
regional múltiple, sin fuente institucional directa) · Fuentes: Nacional / Regional · Consulta:
2026-08-13.

### ARG-96-002 — Ataque armado contra unidad de Inteligencia de la Policía Municipal y persecución, Chihuahua capital / Aquiles Serdán, Chihuahua (🟡 AMARILLO)

- Institucional (indirecta): Fiscalía General del Estado de Chihuahua, movilizada al lugar, referida
  por medios sin comunicado propio con folio localizado.
- Regional: [El Diario de Chihuahua](https://www.eldiariodechihuahua.mx/local/2026/aug/12/atacan-a-balazos-a-policias-de-inteligencia-y-desatan-operativo-827004.html) ·
  [Tiempo.com.mx](https://www.tiempo.com.mx/local/ataque-policias-chihuahua-aquiles-serdan-persecucion-sujetos-armados-balazos-operativo-halcon-ejercito/) ·
  [Omnia](https://www.omnia.com.mx/noticia/438102/despliegan-operativo-tras-ataque-a-balazos-contra-unidad-de-la-dspm) ·
  [El Heraldo de Chihuahua](https://oem.com.mx/elheraldodechihuahua/policiaca/atacan-a-balazos-a-unidad-de-inteligencia-de-la-policia-municipal-en-chihuahua-31541790) ·
  [La Opción de Chihuahua](https://laopcion.com.mx/local/atacan-a-policias-municipales-y-sujetos-armados-escapan-20260812-524923.html) ·
  [Quadratín Chihuahua](https://chihuahua.quadratin.com.mx/principal/operativo-por-disparos-a-patrulla-deriva-en-rina-entre-policias/) ·
  [InfoChihuahua](https://infochihuahua.com/ciudad/se-enfrentan-policias-de-chihuahua-y-aquiles-serdan-durante-persecucion-de-sujetos-armados/)

12-ago-2026, por la tarde, periférico Vicente Lombardo Toledano, ciudad de Chihuahua. Sujetos
armados dispararon contra una unidad del Grupo de Inteligencia de la Dirección de Seguridad Pública
Municipal (DSPM). Los agentes iniciaron persecución hacia Aquiles Serdán; una patrulla de la Policía
Municipal de ese municipio se interpuso en la ruta, lo que —según cobertura regional— permitió la
fuga de los agresores, y derivó en un altercado entre ambas corporaciones municipales. Se desplegó
operativo aéreo y terrestre (helicóptero Halcón 1, drones) sin ubicar a los responsables. Sin heridos
ni detenidos reportados. `Pendiente de corroboración independiente` sobre el móvil del ataque inicial
y su posible vínculo con estructura de crimen organizado.

**Explotación ARGOS**: la interposición entre corporaciones municipales durante la persecución es un
dato operativo que sugiere, sin poder afirmarse, una falla de coordinación interinstitucional en zona
conurbada; explotar si se repite un patrón similar en próximos cortes. Se clasifica amarillo por
tratarse de agresión directa contra fuerza de seguridad con persecución, sin acreditarse el origen
del hecho detonante ni vínculo confirmado con crimen organizado.

**Trazabilidad**: `ARG-96-002` · Nivel de confianza: 🟡 Medio (★★★☆☆) · Fuentes: Institucional
(indirecta) / Regional · Consulta: 2026-08-13.

### Seguimiento sin novedad sustantiva dentro de la ventana

- **ARG-94-001 (Pénjamo-Manuel Doblado, Guanajuato)**: sin detenidos reportados dentro de la ventana.
- **ARG-94-002 (Chilpancingo, Guerrero)**: sin novedad sobre ese caso específico. Nota de contexto no
  confundible: el 12-ago se reportó la detención de seis presuntos integrantes de "Los Tlacos" por
  extorsión en Chilpancingo ([N+](https://www.nmas.com.mx/guerrero/seguridad/foro-tv-video-detienen-seis-integrantes-los-tlacos-extorsion-chilpancingo-guerrero-hoy-12-agosto-2026/)) —
  hecho distinto (verde, extorsión), sin vínculo con la persecución del 10-ago; fuera del alcance de
  Crimen I, no se integra como tarjeta propia por no alcanzar el umbral de relevancia frente al resto
  del corte.
- **ARG-93-001 (Los Reyes La Paz, Estado de México)**: sin detenidos. Único desarrollo del corte:
  nota de contexto periodístico ([Infobae, 12-ago](https://www.infobae.com/mexico/2026/08/12/ataque-a-nina-de-10-anos-destapa-una-decada-de-extorsiones-a-transportistas-en-el-edomex/))
  que documenta extorsión histórica a transportistas de Ruta 69 y reitera la identificación no
  oficial de "Los Vallarta" por parte de las víctimas/gremio — sigue siendo versión de terceros, no
  atribución de la FGJEM; no constituye avance operativo.
- **ARG-93-002 (Los Mochis, Sinaloa)**: sin novedad adicional a la ya documentada en ARGOS 95.
- **ARG-92-001 (Morelia, Michoacán — asesinato de Arturo Herrera Guzmán)**: agresores prófugos, sin
  detenidos dentro de la ventana. Sin novedad posterior al 11-ago ya documentado en ARGOS 95.
- **Taquería "Fermín", Zapopan, Jalisco**: sin detenidos ni identificación de responsables. Único
  desarrollo: difusión pública el 13-ago de video de cámaras de seguridad con la secuencia del
  ataque ([Publimetro](https://www.publimetro.com.mx/entretenimiento/2026/08/13/alfredo-olivas-video-muestra-ataque-contra-su-primo-en-zapopan/),
  [TV Azteca Jalisco](https://www.aztecajalisco.com/noticias-jalisco/ataque-en-taqueria-zapopan-revisan-camaras-para-identificar-a-agresores));
  la Fiscalía de Jalisco continúa análisis de cámaras, sin detenidos ni líneas reveladas.

### Hechos revisados y descartados (fuera de ventana o sub-umbral)

- Ataque con dron explosivo, La Estanzuela, Aquila, Michoacán: fecha en disputa (11 o 12-ago), en
  ambos casos fuera de la ventana de ARGOS 96 — ver nota de posible vacío de cobertura al inicio.
- Quema de camiones y homicidio de tráilero, carreteras de Veracruz (11-ago): fuera de ventana — ver
  nota de posible vacío de cobertura al inicio.
- Ataque armado en "callejón de los Yonkes", colonia Sánchez Taboada, Tijuana, Baja California
  (12-ago, mediodía): dos heridos, un detenido; sin elemento que acredite vínculo con estructura de
  delincuencia organizada — sub-umbral, no se integra.
- Intento de asalto/robo contra el vehículo del coordinador general del C5 de la Ciudad de México,
  Salvador Guerrero Chiprés (11-ago tarde): fuera de ventana y, según la cobertura disponible, sin
  elementos que acrediten un ataque dirigido contra su función — no se integra.
- Narcobloqueos, secuestros masivos, masacres, hallazgos de fosas, desapariciones múltiples: sin
  hallazgo verificable dentro de la ventana tras barrido dirigido.

---

## Crimen organizado II — economía criminal y extorsión

### ARG-96-003 — Operativo FGR/AIC en ocho estados: narcotráfico transnacional ("La Patrona"), huachicol y cateos conexos (🟢 VERDE)

- Institucional (indirecta): Fiscalía General de la República / Agencia de Investigación Criminal
  (AIC), comunicado difundido la tarde del 12-ago-2026 (`fgr.org.mx` no accedido directamente,
  `EGRESS_BLOCKED`)
- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/12/cateos-detenciones-y-aseguramientos-en-ocho-estados-fgr-golpea-redes-de-huachicol-trafico-de-armas-y-narcotrafico-transnacional/) ·
  [El Sol de México/OEM](https://oem.com.mx/elsoldemexico/mexico/explosivos-arsenal-y-farmacos-falsos-ocho-operativos-federales-exhiben-escalada-de-violencia-en-ocho-estados-29174614) ·
  [La Silla Rota](https://lasillarota.com/estados/2026/8/13/fgr-da-golpe-al-huachicol-trafico-de-armas-y-narco-en-8-estados-524312.html) ·
  [Aristegui Noticias](https://aristeguinoticias.com/1208/mexico/cae-la-patrona-extranjera-ligada-a-red-internacional-de-cocaina/) ·
  [UDGTV](https://udgtv.com/noticias/detienen-en-mexico-a-la-patrona/328131)
- Regional: [Hoy Tamaulipas](https://hoytamaulipas.net/notas/624386/Operativos-sacuden-ocho-estados-decomisan-arsenal-y-356-mil-litros-de-diesel-de-huachicol.html) ·
  [Omnia — Estado de México](https://www.omnia.com.mx/noticia/438143/cae-la-patrona-en-edomex-la-ligan-a-red-internacional-de-trafico-de-cocaina-haci)

Operativos ejecutados el 9 y 10 de agosto de 2026 por la AIC-FGR, con Ejército, Guardia Nacional,
Marina y SSPC, en Sinaloa, Michoacán, Tamaulipas, Puebla, Estado de México, Baja California, Morelos
y Colima, derivados de trabajos de inteligencia procesal; comunicado difundido el 12-ago
(`Evento anterior publicado durante el corte`). Componentes verificados:

- **Narcotráfico transnacional**: detención en Atizapán de Zaragoza, Estado de México, de Gladys
  "N", alias "La Patrona", presunta operadora logística de una red de tráfico internacional de
  cocaína que impregnaba químicamente la droga en prendas de vestir para envío por paquetería aérea
  a Estados Unidos, Europa y Australia. Puesta a disposición judicial en Colima.
- **Huachicol**: cateo en Mazatlán, Sinaloa — 14,010 L de combustible, cuatro vehículos, 15
  contenedores (más armamento, ver tabla de la Sección 1); aseguramiento de un tractocamión en
  Nahuatzen, Michoacán, por el mismo delito.
- **Cateos conexos**: tres inmuebles en Jiutepec (Morelos), Colima capital y Villa de Álvarez
  (Colima).
- **Detención adicional**: Apolonio "N", por probable uso indebido de credenciales de servidor
  público, Jiutepec, Morelos.
- Mención sin desglose por estado del cumplimiento de órdenes de aprehensión/reaprehensión contra
  cuatro personas por delitos relacionados con armas de fuego.

**Contradicción/vacío sin resolver**: la cobertura agregada cita "al menos 16 personas detenidas"
para el conjunto del operativo, cifra que no concilia con los detenidos atribuibles nominal o
geográficamente en las notas consultadas (ocho, ver tabla de armamento). No se integra la cifra de
16 al conteo nacional por falta de desglose oficial verificable.

**Armamento asegurado** (ver también página 5 / Sección 1): 2 armas cortas (Manzanillo, Colima), 1
arma larga (Jiutepec/Colima/Villa de Álvarez), 1 cargador y 13 cartuchos de uso exclusivo de las
FFAA (Mazatlán, Sinaloa); mención cualitativa de explosivos sin cifra en Nuevo Progreso, Tamaulipas.

**Explotación ARGOS**: el método de impregnación química de ropa para envío por paquetería aérea es
consistente con reportes previos de logística de exportación de cocaína hacia mercados fuera del
corredor tradicional México-Estados Unidos (Europa, Australia) — hipótesis que requiere validación
con más casos, no debe generalizarse. La simultaneidad geográfica (8 estados) sugiere una operación
de inteligencia procesal centralizada, no reactiva. Vacío: sin nacionalidad de la detenida, sin
identificación de la organización matriz, sin cifra de droga asegurada en el operativo mismo, sin
desglose numérico de armamento para 5 de 8 entidades.

**Trazabilidad**: `ARG-96-003` · Confianza: 🟡 Medio · Fuentes: Institucional (indirecta) / Nacional
/ Regional · Consulta: 2026-08-13 07:00 CDMX.

### ARG-96-004 — Huachicol: aseguramiento de 356,500 litros de diésel, General Escobedo, Nuevo León (🟢 VERDE)

- Institucional (indirecta): Gabinete de Seguridad, reporte de "acciones relevantes del 11 de agosto
  de 2026" (`gob.mx/sspc` no accedido directamente, `EGRESS_BLOCKED`)
- Nacional: [LatinUS](https://latinus.us/mexico/2026/8/12/huachicol-en-nuevo-leon-decomisan-mas-de-350-mil-litros-de-combustible-en-general-escobedo-181406.html)
- Regional: [Hoy Tamaulipas](https://hoytamaulipas.net/notas/624386/Operativos-sacuden-ocho-estados-decomisan-arsenal-y-356-mil-litros-de-diesel-de-huachicol.html)
  (cobertura de estado vecino, no medio nativo de Nuevo León) · agregadores que replican el
  comunicado íntegro: [Talla Política](https://www.tallapolitica.com.mx/gabinete-de-seguridad-del-gobierno-de-mexico-informa-acciones-relevantes-del-11-de-agosto-de-2026/),
  [RED113](http://www.red113mx.com/2026/08/el-gabinete-de-seguridad-del-gobierno_0682133840.html)

Cateo del 11-ago-2026 a un inmueble en General Escobedo, Nuevo León, por Guardia Nacional, Ejército,
FGR, Policía Estatal y Seguridad Física de Pemex: 356,500 litros de diésel, siete tractocamiones, un
vehículo, 12 toneles, dos cajas secas y cinco bombas de trasvase. Sin detenidos ligados a este hecho.
El mismo comunicado reporta acciones coordinadas adicionales en BC, Guerrero, Michoacán, Nayarit,
Sinaloa, Sonora y Veracruz, sin desglose suficiente por estado en las fuentes consultadas.

**Deduplicación verificada**: distinto de `ARG-95-006` (Güémez/Matamoros, Tamaulipas, 348,700 L,
operativo del 7-ago difundido el 10-ago) y de un aseguramiento de 111,000 L en el mismo municipio de
julio de 2026 (evento de fecha distinta, no del corte). **Posible vacío de cobertura de ARGOS 95**:
el boletín "acciones relevantes del 11 de agosto" pudo publicarse después del cierre de consulta de
esa edición (2026-08-12, 07:00 CDMX); se integra aquí como `Evento anterior publicado durante el
corte`.

**Explotación ARGOS**: confirma a Nuevo León como punto reiterado de almacenamiento de huachicol en
el corredor industrial de Monterrey (General Escobedo ya registró aseguramientos similares en julio
2026) — consistente con la hipótesis, señalada en ediciones previas, de concentración logística de
huachicol en el área metropolitana de Monterrey; requiere validación con más cortes. Vacío: sin
detenidos, sin identificación de la razón social del inmueble, sin desglose de los otros siete
estados mencionados en el mismo comunicado.

**Trazabilidad**: `ARG-96-004` · Confianza: 🟡 Medio · Fuentes: Institucional (indirecta) / Nacional
/ Regional (adyacente) · Consulta: 2026-08-13 07:00 CDMX.

### ARG-96-005 — Huachicol fiscal / red financiera: vinculación a proceso de la apoderada legal de Ingemar, caso Ruffo Appel, Nezahualcóyotl, Estado de México (🟢 VERDE — avance judicial)

- Institucional: audiencia de juez de control federal, citada directamente por medios
- Nacional: [El Universal](https://www.eluniversal.com.mx/nacion/vinculan-a-proceso-a-apoderada-legal-de-ingemar-por-huachicol-ferroviario-juez-ratifica-prision-preventiva/) ·
  [La Razón](https://www.razon.com.mx/mexico/2026/08/09/dictan-prision-preventiva-contra-guadalupe-n-apoderada-legal-de-ingemar/) ·
  [Proceso](https://www.proceso.com.mx/nacional/2026/8/13/vinculan-a-proceso-a-la-representante-legal-de-ingemar-empresa-ligada-a-ruffo-377939.html) ·
  [Infobae](https://www.infobae.com/mexico/2026/08/13/cae-otra-pieza-del-caso-ruffo-vinculan-a-proceso-a-apoderada-legal-de-ingemar-por-delincuencia-organizada-y-contrabando/) ·
  [SDP Noticias](https://www.sdpnoticias.com/mexico/vinculan-a-proceso-a-guadalupe-hernandez-ligada-a-caso-de-huachicol-fiscal-de-ernesto-ruffo/) ·
  [La Jornada](https://www.jornada.com.mx/2026/08/10/politica/011n1pol)
- Regional: [Zócalo](https://www.zocalo.com.mx/procesan-a-guadalupe-n-apoderada-legal-de-la-empresa-ingemar-de-ruffo-appel/) ·
  [Quadratín México](https://mexico.quadratin.com.mx/vinculan-a-proceso-a-apoderada-de-ingemar-ligada-con-red-de-huachicol/) ·
  [El Siglo de Torreón](https://www.elsiglodetorreon.com.mx/noticia/2026/dan-prision-preventiva-a-la-apoderada-legal-de-ingemar-vinculada-a-ernesto-ruffo.html)

12-ago-2026: un juez de control federal vinculó a proceso a Guadalupe Hernández Hinojosa, apoderada
legal de Ingemar S.A. de C.V. — empresa señalada por la FGR como parte de la red de contrabando de
hidrocarburos ("huachicol ferroviario") vinculada al exgobernador de Baja California Ernesto Ruffo
Appel — por probable participación en contrabando y delincuencia organizada. El juez ratificó la
prisión preventiva justificada, a cumplirse en el Centro Penitenciario y de Reinserción Social
Nezahualcóyotl Sur, Estado de México, y fijó tres meses para el cierre de la investigación
complementaria. La FGR la identificó como firmante autorizada de cuentas bancarias de Ingemar y
señaló que gestionó ante aduanas mercancía con documentación inconsistente. Con esta vinculación, la
red suma nueve personas detenidas, ocho ya vinculadas a proceso, incluido Ruffo Appel. **Desarrollo
nuevo** respecto del estatus "sin desarrollo" registrado en ARGOS 95 para este seguimiento.

**Nota conexa (no integrada como hecho separado, trámite en curso)**: el 12-ago el abogado de Ruffo
Appel promovió un amparo adicional contra su vinculación a proceso del 19-jul y contra la prisión
preventiva oficiosa que cumple en el Reclusorio Preventivo Federal (Altiplano); cobertura en vivo de
Infobae del 12-ago menciona además amparos concedidos a Ruffo y a Gilda Lozoya cuyo alcance exacto no
quedó claro en las fuentes consultadas. `Pendiente de corroboración independiente`.

**Explotación ARGOS**: primera vinculación a proceso adicional documentada desde ARGOS 94 sobre esta
red; línea a explotar: patrón de imputación a firmantes autorizados/apoderados legales de empresas
huachicoleras (posible replicabilidad en otras empresas de la red, no confirmado). Riesgo: litigio
de amparo activo en paralelo puede alterar el estatus de prisión preventiva de los ya vinculados —
dar seguimiento a resoluciones en próximos cortes. Vacío: sin número de carpeta de investigación.

**Trazabilidad**: `ARG-96-005` · Confianza: 🟢 Alto · Fuentes: Institucional / Nacional / Regional ·
Consulta: 2026-08-13 07:00 CDMX.

### ARG-96-006 — Rescate de víctima de secuestro virtual, Morelia, Michoacán (🟢 VERDE)

- Institucional (directa): Policía Morelia, [nota 1](https://www.policiamorelia.gob.mx/policia-morelia-rescata-a-joven-victima-de-secuestro-virtual/) ·
  [nota 2](https://www.policiamorelia.gob.mx/policia-morelia-localiza-a-joven-victima-de-secuestro-virtual-y-lo-entrega-sano-y-salvo-a-sus-familiares/)
- Regional: [Atiempo.mx](https://atiempo.mx/morelia/policia-morelia-rescata-a-joven-victima-de-secuestro-virtual/) ·
  [Quadratín Michoacán](https://www.quadratin.com.mx/justicia/localiza-policia-morelia-a-joven-victima-de-secuestro-virtual/)

12-ago-2026, Morelia, Michoacán. Elementos de la Policía Morelia (municipal) localizaron sano y
salvo a un joven víctima de extorsión en modalidad de secuestro virtual, tras reporte de sus padres
en la zona de Ciudad Universitaria. Se evitó el pago exigido; la familia fue canalizada a la
Fiscalía Especializada en Combate al Secuestro y Extorsión de la FGE Michoacán. Sin detenidos. **No
duplica `ARG-95-008`** (tres víctimas, Guardia Civil estatal, 11-ago, ~450,000 pesos evitados):
corporación distinta (municipal vs. estatal), fecha y número de víctimas distintos. Sin cobertura de
medio nacional.

**Explotación ARGOS**: segundo hallazgo consecutivo de secuestro virtual frustrado en Morelia en dos
cortes distintos (11 y 12 de agosto) — sugiere actividad sostenida de esta modalidad en la capital
michoacana y protocolo institucional activo (Unidad Antiextorsión/Fiscalía Especializada); sin
vínculo confirmado con estructura de crimen organizado específica. Línea a explotar: acumulado
mensual de secuestros virtuales frustrados en Michoacán. Vacío: sin identidad de los extorsionadores.

**Trazabilidad**: `ARG-96-006` · Confianza: 🟡 Medio (institucional directa + regional, sin nacional)
· Fuentes: Institucional (directa) / Regional · Consulta: 2026-08-13 07:00 CDMX.

### Hallazgo de confianza insuficiente — no integrado

**Detención de Dylan "N", alias "El Becerro" (presunto CIDA), Acapulco, Guerrero** (12-ago): 55
bolsas con sustancia similar a cristal, 29 bolsas de hierba verde similar a marihuana, una
motocicleta. Atribuido a la FGE Guerrero, pero solo una fuente distinguible ([Infobae, cobertura en
vivo del 12-ago](https://www.infobae.com/mexico/2026/08/12/en-vivo-seguridad-narcotrafico-y-crimen-en-mexico-hoy-12-de-agosto-procesan-a-angel-aguirre-por-caso-ayotzinapa/)),
replicada sin aportar información independiente. Confianza: No confirmado. `Pendiente de
corroboración independiente`.

### Categorías sin hallazgo verificable en la ventana estricta

- **Narcolaboratorios**: sin desmantelamiento nuevo con fecha de hecho o publicación en la ventana.
- **Narcotráfico marítimo**: sin decomiso de SEMAR con fecha de hecho en la ventana.
- **Redes financieras / UIF (evento discreto)**: sin acción de congelamiento nueva. Nota de contexto
  regulatorio, no evento: la SCJN resolvió el 12-ago que los jueces no pueden suspender
  cautelarmente los bloqueos de cuentas de la UIF ([La Silla Rota](https://lasillarota.com/dinero/2026/8/13/corte-blinda-bloqueos-de-la-uif-que-pasa-con-tu-dinero-si-hacienda-congela-tu-cuenta-524355.html)).
- **Extradiciones**: sin hecho verificable en la ventana.

---

## Sección 1 — Armamento (ver tabla completa en el cartelón, página 5)

### ARG-96-ARM-001 — Cateos "Sinergia por Querétaro": 10 detenidos, armas de fabricación artesanal (🟢 VERDE)

- Institucional (indirecta): Fiscalía General del Estado de Querétaro, citada por [Quadratín
  Querétaro](https://queretaro.quadratin.com.mx/diez-detenidos-en-10-cateos-en-varios-municipios-de-queretaro/) ·
  [Al Minuto Noticias Querétaro](https://www.alminutonoticias.com.mx/queretaro/deja-operativo-interinstitucional-10-detenidos-tras-cateos-en-queretaro-amealco-y-pedro-escobedo/2026/08/12/)
  (`fiscaliageneralqro.gob.mx` no accedido directamente, `EGRESS_BLOCKED`)
- Regional: [Crónica Regional](https://www.cronicaregional.com.mx/policiaca/detienen-a-10-personas-tras-ejecutar-operativo-simultaneo-en-tres-municipios-de-queretaro/) ·
  [Críptica Querétaro](https://criptica.com.mx/diez-cateos-en-queretaro-dejan-10-detenidos-aseguran-droga-armas-y-equipo-de-vigilancia/) ·
  [AlertaQro](https://www.alertaqronoticias.com/2026/08/12/cateos-en-tres-municipios-de-queretaro-dejan-diez-personas-detenidas-entre-ellas-hay-adolescentes/) ·
  [Reqronexion](https://www.reqronexion.com/realiza-fiscalia-10-cateos-y-detiene-a-10-personas-en-queretaro-amealco-y-pedro-escobedo/)

12-ago-2026, Fiscalía General del Estado de Querétaro, con Policía de Investigación del Delito,
Servicios Periciales, Policía Estatal, Guardia Nacional, Ejército y policías municipales de Pedro
Escobedo y Querétaro, ejecutó 10 órdenes de cateo simultáneas en Querétaro, Amealco de Bonfil y Pedro
Escobedo, derivadas de investigaciones por lesiones dolosas, daños, delitos contra la salud y
portación de armas prohibidas. 10 detenidos (7 adultos, 3 adolescentes — identidad omitida por
tratarse de menores). Aseguramiento: armas de fabricación artesanal (cantidad no especificada,
evento cualitativo), cartuchos útiles (cantidad no especificada), metanfetamina; en otros puntos de
intervención, 1 arma de fuego (tipo no especificado), dosis de narcótico, cámaras de videovigilancia,
teléfonos y documentación. Sin granadas, AEI ni explosivos reportados. Sin cobertura de medio
nacional.

**Explotación ARGOS**: participación de tres adolescentes entre los detenidos en un operativo
vinculado a delitos contra la salud y portación de armas — línea a explotar sobre reclutamiento o
uso de menores en la zona metropolitana de Querétaro; requiere validación adicional. Vacío: sin
desglose numérico del armamento, sin estatus legal de los detenidos.

**Trazabilidad**: `ARG-96-ARM-001` · Confianza: Medio (fuente institucional estatal citada + cuatro
regionales, sin medio nacional) · Fuentes: Institucional (indirecta) / Regional (4) · Consulta:
2026-08-13.

### Pistas descartadas por caer fuera de la ventana o resultar falsas (documentadas para auditoría)

- **Huajicori, Nayarit** (Barrett + 2 AEI, hecho 11-ago, boletín Gabinete de Seguridad "11 de
  agosto"): hecho y publicación anteceden la ventana de ARGOS 96 — ver nota de posible vacío de
  ARGOS 95 al inicio de este documento.
- **Mazatlán, Sinaloa, 28 detenidos** (15 armas largas, 94 cargadores, 2,964 cartuchos): hecho
  7-ago, publicación 9-10-ago — fuera de ventana, no capturado por ARGOS 93/94/95; vacío acumulado
  señalado, no integrado a este corte.
- **Sinaloa, 52 detenidos agregados** (Concordia, Mazatlán, San Ignacio, Navolato, Culiacán, Ahome,
  7-9 ago): cifra de contexto agregada anterior a la ventana; el sub-evento de Concordia ya está
  cubierto en `ARG-95-005`, no se duplica.
- **"Armas envueltas para regalo", Coahuila**: resultado indexado de **2023** (Puente Internacional
  Acuña) — descartado, pista falsa del resumen automático de `WebSearch`.
- **"Vehículos blindados y arsenal táctico", sierra de Durango**: hecho del **26-jun-2026** —
  descartado, fuera de ventana.
- **Movilización de fuerzas armadas, Las Palmas, Puerto Vallarta**: nota fechada ~3 semanas antes de
  su publicación — fuera de ventana, descartada.
- **Coahuila — "15 armas cortas, 24 cargadores, tres personas y cuatro servidores públicos
  detenidos"**: cifra obtenida únicamente del resumen automático de `WebSearch` sobre el operativo
  de ocho estados; no se pudo verificar contra ningún resultado independiente ni contra el propio
  desglose por entidad de ese operativo (que no incluye a Coahuila). Descartada por riesgo de
  conflación/alucinación del resumen automático — no se integra ni se suma al total nacional.
- **Zitácuaro, Michoacán** (armas, droga, un detenido): hecho del **19-jul-2026** — descartado, fuera
  de ventana (verificación cruzada corrigió una sugerencia inicial de fecha de agosto).
- **Monclova, Coahuila, 47,319 L de combustible**: huachicol sin armamento asociado — no corresponde
  a la taxonomía de esta sección.

### Total nacional del corte (solo eventos con confianza Medio o superior)

| Categoría | Cantidad | Eventos que aportan |
|---|---|---|
| Armas cortas | 2 | Manzanillo, Colima (`ARG-96-003`) |
| Armas largas | 1 | Jiutepec/Colima/Villa de Álvarez (`ARG-96-003`) |
| Cartuchos | 13 (uso exclusivo FFAA, Mazatlán/Sinaloa) | `ARG-96-003` |
| Cargadores | 1 (Mazatlán/Sinaloa) | `ARG-96-003` |
| Granadas | 0 confirmadas en ventana | — |
| AEI | 0 confirmados en ventana | — |
| Explosivos/componentes | 0 con cantidad determinada (mención cualitativa sin cifra, Nuevo Progreso, Tamaulipas) | — |
| Armamento especial | 0 confirmados en ventana | — |
| Personas detenidas (mismo evento de aseguramiento, con arma cuantificada) | 2 (Manzanillo, Colima) | — |
| Personas detenidas adicionales por posesión/portación sin cifra de armamento (no integradas al total numérico) | 3 (Tijuana BC, Nuevo Progreso Tamaulipas, Tepeaca Puebla) | `ARG-96-003` |
| Estados con aseguramiento verificado (Medio o superior) | 3 (Colima, Sinaloa, Querétaro) | — |
| Eventos contabilizados | 2 (`ARG-96-003` cross-ref, `ARG-96-ARM-001`) | — |
| Eventos cualitativos sin cantidad agregada | 2 (armas artesanales y 1 arma sin tipo, Querétaro; explosivos sin cifra, Tamaulipas) | — |
| Eventos de confianza insuficiente / descartados (no integrados) | 8 (ver pistas descartadas) | — |

**Advertencia de auditoría**: el total nacional de este corte es notablemente más bajo que en
ARGOS 95, no por menor actividad operativa real, sino porque (1) el boletín "acciones relevantes"
del Gabinete de Seguridad correspondiente a la ventana estricta (12-13 ago) no fue localizado al
momento de la consulta, y (2) el operativo FGR de ocho estados publicó la mayoría de sus cifras de
armamento sin desglose por tipo o cantidad en cinco de ocho entidades. Esto **no equivale** a
ausencia real de aseguramientos en esas entidades durante la ventana — se registra como vacío de
información, no como vacío de actividad.

### Indicador de cobertura

Portales federales de consulta obligatoria: 1 de 6 con contenido localizado (FGR, vía agregadores).
Guardia Nacional, SEDENA, SEMAR, Aduanas/ANAM: sin boletín propio localizado para 12-13-ago. Gabinete
de Seguridad/SSPC: el boletín más reciente indexado corresponde al 11-ago (fuera de ventana,
corresponde a ARGOS 95); sin boletín del 12 o 13-ago localizado al momento del corte. Portales
estatales: 25 de 32 entidades con búsqueda dirigida ejecutada — 1 con evento verificado de fuente
institucional directa citada (Querétaro). Sin búsqueda dirigida en este corte: Aguascalientes, CDMX,
Hidalgo, Nayarit, San Luis Potosí, Tlaxcala (6 entidades) — se reportan como no revisadas, no como
`SIN DATO`.

---

## Sección 2 — Sentencias (ver tabla completa en el cartelón, página 6)

### ARG-96-SEN-001 — FGR/FECOR Querétaro — Posesión simple de metanfetamina

- Regional: [CódigoQro](https://codigoqro.mx/nota/local/2026/08/12/condenan-ngel-n-posesion-metanfetamina-queretaro)
- Institucional: FGR (FECOR), citada por el medio, sin acceso directo.

Revisión vehicular en Amazcala, El Marqués, Querétaro; hallazgo de dosis y contenedores con
sustancias con características de cocaína y metanfetamina, y báscula. Sentenciado: Ángel "N".
Delito: posesión simple de metanfetamina. Juicio oral. Pena: 4 años 10 meses 15 días + multa de 75
UMA. Reparación del daño no especificada. Firmeza no informada.

### ARG-96-SEN-002 — FGR/FECOR Coahuila — Delitos contra la salud y portación de arma, Piedras Negras

- Regional: [El Siglo de Torreón](https://www.elsiglodetorreon.com.mx/noticia/2026/pareja-detenida-con-droga-y-arma-en-piedras-negras-recibe-6-anos-de-prision.html)
- Institucional: comunicado FGR DPE/3493/2026 (atribuido, sede Monclova, `EGRESS_BLOCKED`)

Cateo en colonia SUTERM, Piedras Negras, Coahuila: 457 g de metanfetamina, 64 g de cocaína, 415 g de
marihuana y un arma de fuego. Sentenciados: Carlos "N" y Génesis "N" (pareja). Pena: 6 años de
prisión (no se aclara si es individual idéntica o conjunta — `Pena compuesta — requiere revisión
jurídica` aplicada a la multa) + multa de 134 UMA. Se contabilizan 2 personas sentenciadas con 6 años
cada una; la multa no se suma al acumulado por la ambigüedad señalada.

### ARG-96-SEN-003 — FGR/FECOR Coahuila — Posesión de cocaína, tramo Allende-Piedras Negras

- Regional: [Periódico Zócalo](https://www.zocalo.com.mx/sentencian-a-sujeto-que-traia-mas-de-dos-kilos-de-droga-en-piedras-negras/)
  (fecha de publicación exacta no confirmada con certeza)
- Institucional: FGR (FECOR), procedimiento abreviado, atribuido, sin acceso directo.

Detención de Jobb "N" en el tramo Allende-Piedras Negras, Coahuila; 2.219 kg de cocaína.
Procedimiento abreviado. Pena: 6 años 8 meses + multa de 8 UMA. Confianza: 🟠 Bajo — fuente única y
fecha de publicación sin confirmación certera dentro de la ventana estricta; se incorpora con esta
reserva, pendiente de validación en el próximo corte.

### ARG-96-SEN-004 — FGR — Tráfico de personas agravado (migrantes), Monclova, Coahuila

- Regional: [El Siglo de Torreón](https://www.elsiglodetorreon.com.mx/noticia/2026/sentencian-a-12-anos-a-operador-por-trafico-de-160-migrantes-en-monclova.html) ·
  [Vanguardia](https://vanguardia.com.mx/coahuila/dan-12-anos-de-prision-a-traficante-de-migrantes-en-coahuila-AO22797403)
- Nacional: [Excélsior](https://www.excelsior.com.mx/nacional/traficante-personas-condenado-12-anos-prision-coahuila) ·
  [Uniradio Informa Baja California](https://www.uniradiobaja.com/policiaca/fgr-obtiene-sentencia-12-anos-prision-una-persona-delito-trafico-migrantes-n898705) ·
  [Omnia](https://www.omnia.com.mx/noticia/438126/condenan-a-12-anos-de-prision-a-sujeto-por-traficar-a-mas-de-160-migrantes-a-eu-)

Hecho base: marzo de 2022, tráiler abandonado en colonia Petrolera, Monclova, Coahuila, con decenas
de migrantes de Nicaragua, Cuba, Honduras y Guatemala. Sentenciado: Ponciano Páez Nájera. Delito:
tráfico de personas agravado. Pena: 12 años + multa de $721,650. Reparación del daño no especificada.
**Contradicción menor sin resolver**: una nota cita "22 migrantes"; se conserva la cifra mayoritaria
("más de 160") reportada en 6 de 7 fuentes localizadas, con la salvedad expresa.

### ARG-96-SEN-005 — FGJES Sonora — Trata de personas y corrupción de menores, Nogales

- Regional: [Telemax](https://telemax.com.mx/blog/2026/08/12/sentencian-a-mas-de-21-anos-a-dos-personas-por-trata-y-corrupcion-de-menores-en-nogales/) ·
  [Crítica](https://www.critica.com.mx/vernoticias.php?artid=118302&mas=1) ·
  [Expreso Sonora](https://www.expreso.com.mx/noticias/sonora/nogales-pareja-sentenciada-por-trata-y-corrupcion-de-menores/262306) ·
  [Tribuna](https://tribuna.com.mx/seguridad/2026/08/12/recibe-pareja-mas-de-21-anos-de-carcel-en-nogales-obligaban-a-menor-a-intimar-con-hombres-por-dinero_653320/) ·
  [El Diario de Sonora](https://eldiariodesonora.com.mx/nogales/2026/08/12/sentencian-mas-21-anos-prision-pareja-trata-corrupcion-menor.html)
- Institucional: FGJES, citada por los cinco medios.

Explotación sexual de una adolescente de 16 años en Nogales, Sonora (dic-2024/ene-2025). Sentenciados:
Gloria Guadalupe "N" y César Telésforo "N". Pena: 21 años 7 meses 15 días — reportada como conjunta,
sin certeza si es individual o repartida (`Pena compuesta — requiere revisión jurídica`, no sumada al
total de años). Multa: $506,696.19. Reparación del daño material: $20,100. Reparación del daño moral:
$18,239.76.

### ARG-96-SEN-006 — FGE Michoacán (Fiscalía Especializada de Homicidio Doloso) — Secuestro agravado, Morelia

- Regional: [Quadratín Michoacán](https://www.quadratin.com.mx/justicia/dictan-82-anos-de-prision-a-responsable-de-secuestro-en-morelia/) ·
  [Agencia Infomania](https://agenciainfomania.com/fge-obtiene-sentencia-de-82-anos-de-prision-contra-responsable-de-secuestro-agravado-en-morelia/)
- Institucional: FGE Michoacán, citada directamente por ambos medios.

Hecho: 24-may-2023, colonia Adolfo López Mateos, Morelia — víctima Alexis Bernardo "N" privado de la
libertad, agredido y localizado sin vida al día siguiente. Sentenciado: Jorge "N". Pena: 82 años +
$1,049,646.40 por reparación integral del daño a víctimas indirectas. Suspensión de derechos
políticos.

### ARG-96-SEN-007 — FGESLP San Luis Potosí — Homicidio, ejido Ojo de Agua, Ciudad Valles

- Regional: [Quadratín San Luis Potosí](https://sanluispotosi.quadratin.com.mx/regiones/dan-30-anos-de-prision-a-homicida-en-ciudad-valles/)
- Institucional: FGESLP, citada por el medio.

Hecho: mayo de 2023, campo de fútbol del ejido Ojo de Agua, Ciudad Valles — agresión con arma blanca.
Sentenciado: José "N". Pena: 30 años + sanción pecuniaria y reparación del daño (montos no
especificados en la fuente).

### ARG-96-SEN-008 — FGE Guanajuato — Violación y violencia familiar, Huanímaro

- Regional: [NoticiasNPI](https://noticiasnpi.com/sentencian-por-abuso-sexual-y-violencia-familiar-a-hombre-en-huanimaro/)
  (fuente única, fecha de publicación estimada, no confirmada con certeza)
- Institucional: FGE Guanajuato, citada por el medio.

Violencia física y psicológica desde fines de 2024; agresión sexual en jun-2025, Huanímaro,
Guanajuato. Sentenciado: Carlos Enrique (apellido no publicado). Procedimiento abreviado. Pena: 6
años 4 meses + reparación del daño (monto no especificado). Confianza: 🔴 No corroborado / 🟠 Bajo.
`Pendiente de corroboración independiente.`

### Nota de contexto — no incorporado como caso numerado (fuera de ventana / pena pendiente)

FGE Michoacán (Fiscalía Especializada de Feminicidios) obtuvo **fallo condenatorio** (sin pena aún
individualizada) contra Gabriela "N" por secuestro agravado de 5 personas en Villas del Pedregal,
Morelia (hechos oct-2022, tres víctimas posteriormente asesinadas). Publicado 11-ago-2026 — fuera de
la ventana estricta de ARGOS 96; seguimiento en el próximo corte cuando se espere la audiencia de
individualización de sanción.

### Duplicidad detectada (no incorporada)

El caso "FGR, procedimiento abreviado, Flamboyanes Campestre, Progreso, Yucatán" (Magdiel "N"/Walter
"N") reapareció en la búsqueda de este corte vía una nota fechada 11-ago; es el mismo hecho ya
documentado como `ARG-95-SEN-006`. No se duplica.

### Vacío señalado para seguimiento

Veracruz publicó un agregado de "13 sentencias condenatorias" (de 48 resoluciones judiciales, con 35
vinculaciones a proceso) sin desglose individual (delito, sentenciado, pena por caso) verificable —
no integrable a la tabla nominal por falta de datos mínimos por sentencia; fecha del reporte
ambigua. Se recomienda seguimiento directo al portal de la fiscalía veracruzana en el próximo corte.

### Conteo acumulado de este corte

Sentencias condenatorias: **8** (`ARG-96-SEN-001` a `008`). Personas sentenciadas: **10**. Años de
prisión acumulados (cifras exactas, personas distintas, excluida la pena conjunta ambigua de Sonora):
4a10m15d + 6a + 6a + 6a8m + 12a + 82a + 30a + 6a4m ≈ **153 años, 10 meses, 15 días**. Multas
acumuladas (solo montos en pesos publicados; UMA no convertidas): $721,650 + $506,696.19 =
**$1,228,346.19**. Reparación del daño acumulada: $1,049,646.40 + $20,100 + $18,239.76 =
**$1,087,986.16**. Ninguna sentencia declarada firme.

### Indicador de cobertura

Fiscalías/entidades con búsqueda dirigida ejecutada: **25 de 32** (Querétaro, Coahuila, Sonora,
Michoacán, Veracruz, Jalisco, Nuevo León, Chihuahua, Tamaulipas, Puebla, Estado de México, Chiapas,
Tabasco, Yucatán, Sinaloa, Guanajuato, Hidalgo, Morelos, Zacatecas, San Luis Potosí, Durango, Oaxaca,
Guerrero, CDMX, Baja California). No revisadas: **7** (Baja California Sur, Colima, Nayarit,
Aguascalientes, Tlaxcala, Campeche, Quintana Roo) — reportadas como no revisadas, no como "sin
actualización". FGR revisada: **Parcialmente** (sin acceso directo a `fgr.org.mx`). Fiscalías con
sentencia publicada: **6** (FGR/Querétaro, FGR/Coahuila ×3, FGJES Sonora, FGE Michoacán, FGESLP, FGE
Guanajuato). Fiscalías con búsqueda dirigida sin sentencia nueva verificable: **19**. Páginas no
disponibles: `fgr.org.mx` (`EGRESS_BLOCKED`, probado directamente).

---

## Categorías sin dato verificado en este corte

- **Narcolaboratorios**: sin desmantelamiento nuevo dentro de la ventana.
- **Narcotráfico marítimo**: sin decomiso nuevo dentro de la ventana.
- **Redes financieras / UIF**: sin acción discreta nueva de congelamiento de cuentas.
- **Desapariciones múltiples / fosas clandestinas**: sin hallazgo verificable.
- **Narcobloqueos criminales / secuestros masivos / infraestructura crítica**: sin hallazgo
  verificable.
- **Indicadores oficiales nuevos**: sin informe SESNSP/INEGI/Gabinete de Seguridad publicado
  específicamente para el 12-13 de agosto al momento del corte.

## Limitaciones de la búsqueda

- **`WebFetch` devolvió `EGRESS_BLOCKED` para todo dominio externo probado** en los cuatro barridos
  de este corte, replicando el resultado de ARGOS 90 a 95.
- Crimen I: búsqueda dirigida ejecutada para Durango, Chihuahua, Michoacán, Veracruz, Guerrero,
  Estado de México, Jalisco, Baja California; resto de entidades vía cobertura nacional genérica.
- Crimen II: búsqueda dirigida para Sinaloa, Michoacán, Tamaulipas, Puebla, Estado de México, Baja
  California, Morelos, Colima, Nuevo León, Guerrero.
- Armamento: 25 de 32 entidades con búsqueda dirigida; sin revisar Aguascalientes, CDMX, Hidalgo,
  Nayarit, San Luis Potosí, Tlaxcala.
- Sentencias: 25 de 32 entidades con búsqueda dirigida; sin revisar Baja California Sur, Colima,
  Nayarit, Aguascalientes, Tlaxcala, Campeche, Quintana Roo.
- Portales federales de consulta obligatoria: 1 de 6 con contenido localizado (FGR vía agregadores);
  Guardia Nacional, SEDENA, SEMAR, SSPC/Gabinete de Seguridad y Aduanas/ANAM sin boletín propio del
  12-13 de agosto localizado.
- Al menos tres casos confirmados de conflación de fechas por el resumen automático de `WebSearch`
  (Coahuila 2023, Durango junio-2026, Zitácuaro julio-2026), descartados tras verificación cruzada —
  se recomienda a los equipos de próximos cortes verificar doblemente cualquier cifra antes de
  integrarla.
- Seis posibles vacíos de cobertura retroactivos identificados en ediciones anteriores (Aquila
  Michoacán, Veracruz camiones/tráilero, El G1 Ensenada, El Loco Metepec, funcionarios Edomex
  verificentros, Huajicori Nayarit) — documentados al inicio de este documento para auditoría
  editorial, no incorporados como hechos de esta edición.
