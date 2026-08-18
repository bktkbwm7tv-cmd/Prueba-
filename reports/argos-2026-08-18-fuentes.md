# ARGOS 101 — Registro de fuentes (auditoría)

Corte: 2026-08-18 · Ventana de hechos: **2026-08-17 02:47 CDMX → 2026-08-18 13:37 CDMX**.
Continuación de ARGOS 100 (corte 2026-08-17). Este documento respalda `argos-2026-08-18.html` y
`argos-2026-08-18-movil.html`, y existe para que todo `SIN DATO` de la edición sea demostrable.

Ventana efectiva: **~35 horas**, de la madrugada del lunes a la tarde del martes. Es más larga que
la de ARGOS 100 (~19 h) porque el corte se toma en continuidad estricta desde el cierre de la
edición anterior y el de hoy se levanta a media tarde. Esa diferencia de duración es relevante para
comparar volúmenes entre ediciones y se hace explícita en el producto: **un corte con más hechos que
el anterior no indica por sí mismo más violencia, sino una ventana casi el doble de larga.**

---

## Limitación metodológica — séptima edición consecutiva con el egreso bloqueado

**Sonda de entorno ejecutada al inicio de la sesión por el coordinador**, con `curl` directo contra
cuatro hosts de control:

| Host | Resultado |
|---|---|
| `www.gob.mx/guardianacional/prensa` | 403 al CONNECT |
| `fiscalia.chihuahua.gob.mx` | 403 al CONNECT |
| `www.eluniversal.com.mx` | 403 al CONNECT |
| `es.wikipedia.org` | 403 al CONNECT |

El registro del propio proxy lo confirma textualmente: `gateway answered 403 to CONNECT (policy
denial or upstream failure)`. **El bloqueo es total y no se limita a `*.gob.mx`**: alcanza a medios
nacionales y a dominios de control ajenos al caso. Es una política de la organización y no se
intentó rodearla.

**Consecuencia operativa aplicada**: se prohibió `WebFetch` a los seis equipos regionales y a los
dos de verificación prioritaria, conforme a la lección 3 de ARGOS 100.

**Cero portales leídos por acceso directo, de ~128 objetivo, en las seis regiones.** Ningún
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de esta edición puede presentarse como vacío
institucional verificado. **Techo de confianza efectivo: ★★★☆☆ para todos los hechos de la
ventana** — duodécima edición consecutiva sin superar ★★★★☆.

---

## Verificación PRIORIDAD 1 — ejecutada primero y en solitario

Se aplicó la lección 1 de ARGOS 100: la verificación prioritaria se ejecutó **antes de lanzar los
seis barridos y con la sesión para ella sola**, de modo que su cuota no dependiera de lo que
consumieran las regiones. Consumo: **26 búsquedas de 26 asignadas** (12 + 14), ambos equipos con el
tope agotado.

**Resultado de conjunto: ninguno de los dos pendientes de PRIORIDAD 1 pudo cerrarse.** A diferencia
de ARGOS 100 —donde la verificación prioritaria desmontó dos hechos falsos—, aquí el rendimiento fue
bajo en cierres y alto en **delimitación**: lo que aporta esta edición es saber con precisión qué es
lo que bloquea cada caso, y descartar tres candidatos que habrían entrado como hallazgos falsos.

### Suchiapa, Chiapas — Bulmaro "N": la contradicción de fecha NO se arbitra

- **Veredicto: fecha del hecho NO DETERMINADA CON AUTORIDAD.** Se ejecutaron búsquedas dirigidas a
  `ssp.chiapas.gob.mx` y `fge.chiapas.gob.mx` sin localizar **ningún boletín institucional sobre este
  hecho**. Sin boletín, no hay nada que arbitre entre las dos URLs.
- Lo único disponible siguen siendo **fechas de publicación**: El Heraldo de México fecha en URL
  `2026/8/15`; Infobae, `2026/08/16`. Por la regla de primera publicación, la fecha más probable del
  hecho es el **15-ago**, pero eso es una **inferencia sobre la fecha de publicación**, no una fecha
  de hecho confirmada. Grado de certeza: bajo/medio.
- **Conclusión operativa: se mantiene exactamente el tratamiento de ARGOS 100.** Sigue siendo
  **candidato a omisión de ARGOS 99**, no corrección confirmada. **Bajo ninguno de los dos
  escenarios de fecha (15 o 16-ago) el hecho cae en la ventana de ARGOS 101**, de modo que no suma a
  ningún total de este corte. Se publica como ficha de recuperación, sin integrarse.
- **Desglose de armamento, confirmado y consistente entre seis fuentes**: 1 arma corta calibre 9 mm,
  **2 cargadores**, **32 cartuchos útiles** —contabilizados por separado, nunca sumados—, 15
  envoltorios de presunta cocaína tipo crack, chaleco balístico, funda y un vehículo. Un solo
  detenido. **No determinado**: el monto del efectivo asegurado y la hora del hecho.
- **Elemento de mayor valor de inteligencia, confirmado por todas las fuentes**: el uniforme
  **clonado** de la Fuerza de Reacción Inmediata Pakal (FRIP) con **insignias apócrifas**.
- Confianza: **★★★☆☆ / Bajo**. Sin fuente institucional, la escala no permite subir.
- **Deslinde obligatorio anotado para ediciones futuras**: el barrido tropezó con un resultado de
  `ssp.chiapas.gob.mx` sobre una orden de aprehensión contra un servidor público por abuso de
  autoridad en **Cintalapa de Figueroa**, que es un **caso distinto**, y con un tercer caso —también
  distinto y mucho mayor— de cateos en Suchiapa con 26 detenidos (ver la ficha del barrido Sureste).
  Tres hechos separados, dos de ellos en el mismo municipio y ambos con el tema de uniformes y
  usurpación de funciones de por medio: **no fusionarlos por topónimo.**

### Veracruz — las nueve condenatorias del agregado del 13-ago: cero desglosadas

- **Resultado: 0 de las 9 condenatorias pendientes pudieron desglosarse** con datos mínimos
  suficientes. **No se localizó el listado nominal íntegro de las 53 resoluciones.** Cuarta edición
  consecutiva con el pendiente abierto.
- **Lo que sí se corroboró**: el agregado del **13-ago-2026** existe y está fijado por **dos fuentes
  con fecha en URL** —`lapoliticaenrosa.com/2026/08/13/…` y `golpepolitico.com/2026/08/13/…`—.
  Desglose citado: **11 sentencias condenatorias, 42 vinculaciones a proceso, 18 imputaciones, 13
  órdenes judiciales cumplimentadas, 10 detenciones en flagrancia, 1 persona localizada**, presentado
  por la Fiscal General Lisbeth Aurelia Jiménez Aguirre en la COESCONPAZ. Distribución regional
  citada, sin desglose caso por caso: Tantoyuca, Córdoba, Cosamaloapan, Veracruz, Xalapa,
  Coatzacoalcos y Tuxpan.
- **Cosamaloapan sigue siendo la única documentada** (`ARG-100-SEN-SEG-001`, ARGOS 100). Se
  reencontró y **no se republica como hallazgo nuevo**, conforme a la regla de deduplicación.

**Dos candidatos descartados — habrían entrado como hallazgos falsos:**

| Candidato | Por qué se descarta |
|---|---|
| **"Condenas de hasta 350 años"** — Miguel "N" y Andrés Emiliano "N", Fiscalía Regional de Tuxpan, secuestro agravado de 7 personas migrantes (3 menores), hechos del 17-jun-2023, juicio oral J-04/2024 | El título institucional indexado en `comunicacion.fiscaliaveracruz.gob.mx` **no lleva fecha en el slug** (caracteres unicode decorativos, sin `/2026/08/`), así que no puede fecharse con el método exigido. La única fuente con indicio de fecha (`laopinion.net`) lo sitúa en **junio de 2026**, dos meses fuera de ventana |
| **Córdoba / Poza Rica** — Pedro "N" (110 años); Jorge Alberto "N" y Roberto "N" (50 años), secuestro agravado | Coincide en **cifras exactas** con `lapoliticaenrosa.com/2026/08/05/…`, fechado en URL el **5-ago-2026**, que corresponde a un **agregado distinto: 32 resoluciones, no 53**. Pertenece al lote del 5-ago |

### Señuelo estructural nuevo, tipificado en esta edición

El título institucional **"Condenas de hasta 350 años y 53 resoluciones judiciales"** combina la
cifra de un lote (53, del 13-ago) con una **pena que pertenece a un caso de dos meses antes**. No es
un error del buscador: es la forma en que la propia Fiscalía redacta sus agregados.

> **Regla de método que deja ARGOS 101**: nunca aceptar una **pena destacada en el titular de un
> agregado** sin una URL fechada que ate esa pena específicamente a ese corte. Un agregado puede
> reutilizar cifras históricas en su encabezado sin dejar de ser veraz.

Se confirma además el **patrón de boletín acumulativo rotativo** de la FGE Veracruz: los medios
regionales publican agregados solapados —22, 24, 32, 36, 37, 40, 44, 48, 51, 69 y 78 resoluciones en
fechas distintas de 2026—, lo que vuelve **estructuralmente difícil** aislar los 11 casos de un solo
corte de 24 h sin acceso directo al boletín fuente.

---

## El hallazgo central de método: se desmiente el vacío federal de cuatro ediciones

**ARGOS 98, 99 y 100 publicaron que el boletín del Gabinete de Seguridad llevaba cuatro cortes sin
indexarse y que el más reciente localizable era el del 13-ago. Es falso.** Está indexado:

> **"El Gabinete de Seguridad del Gobierno de México informa acciones relevantes del 14, 15 y 16 de
> agosto de 2026"** —
> `https://www.gob.mx/sspc/prensa/el-gabinete-de-seguridad-del-gobierno-de-mexico-informa-acciones-relevantes-del-14-15-y-16-de-agosto-de-2026`

**Localizado de forma independiente por cuatro de los seis equipos regionales** (Noroeste, Noreste,
Centro y Golfo), por rutas de búsqueda distintas, con dos reproducciones íntegras que lo corroboran
(`tallapolitica.com.mx`, `red113mx.com`).

**La causa del falso vacío está identificada**: el Gabinete **cambió de boletín diario a agregado de
varios días**. Las búsquedas por día suelto —"boletín del 14", "del 15", "del 16"— no alcanzan un
documento cuyo título enumera los tres. Los boletines no faltaban: **estaban fusionados**. El vacío
declarado era, en su mayor parte, **un artefacto de la consulta, no una interrupción de la
publicación**.

**Lo que sí subsiste**: no existe boletín indexado del **17-ago**. El vacío real es de **un día**, no
de cuatro cortes. La consulta `site:gob.mx/sspc/prensa` devuelve la serie del 3 al 16 de agosto sin
el 17.

Se localizó además un **portal federal que ninguna edición había registrado**:
`gabinetedeseguridad.gob.mx`, con sección `/resultados/` y contenidos con identificador propio.

> **Lección de método, la más importante de esta edición**: cuatro ediciones consecutivas publicaron
> como vacío institucional lo que era un cambio de formato del emisor. Un `SIN DATO` confirmado por
> repetición **no queda confirmado: queda repetido**. La coincidencia de varios equipos independientes
> no valida un vacío si todos ejecutan la misma consulta equivocada. **Cuando un vacío se prolonga,
> la hipótesis que debe probarse primero no es que el emisor dejó de publicar, sino que el barrido
> dejó de encontrarlo.**

**Consecuencia pendiente, declarada y no ejecutada**: el boletín trae desglose por entidad —incluido
**Michoacán con 4 fusiles, 1 lanzagranadas acoplado, 12 cargadores, 123 cartuchos y 9 AEI**, y
**Veracruz con 6 armas largas, 4 cortas, 10 cargadores y 13,300 cartuchos**—. Son **hechos del 14 al
16 de agosto**, es decir de las ventanas de ARGOS 99 y 100, y **no se integran a ARGOS 101**. Además,
esas cifras proceden del **resumidor del buscador, no de la lectura del boletín**, por lo que se
registran como `NO CONFIRMADO`. Su recuperación como omisión de ediciones anteriores queda abierta
en `_pendientes.md`.

---

## Presupuesto de búsqueda

| Equipo | Tope | Consumo | Nota |
|---|---|---|---|
| Verificación PRIORIDAD 1 — Suchiapa | 12 | **12** | Ejecutada **primero y en solitario** |
| Verificación PRIORIDAD 1 — Veracruz | 14 | **14** | Ídem |
| Barrido Noroeste | 20 | 20 | Tope alcanzado |
| Barrido Noreste | 20 | 20 | Tope alcanzado |
| Barrido Occidente | 20 | 20 | Tope alcanzado |
| Barrido Centro | 20 | 20 | Tope alcanzado |
| Barrido Golfo | 20 | 20 | Tope alcanzado |
| Barrido Sureste | 20 | 20 | Tope alcanzado |
| Coordinación (verificación directa) | — | 2 | Cocaína del Pacífico y Colima |
| **Total** | **146** | **148 de 200** | **Ningún equipo excedió su tope** |

Frente a ARGOS 100 (142 consumidas, tres equipos excedidos), esta edición **cierra con los ocho
topes respetados**. El mandato de `CLAUDE.md` (4 portales × 32 entidades + federales) sigue siendo
aritméticamente imposible: exige entre 200 y 500 consultas.

### Rotación de cobertura — aplicada y declarada

ARGOS 100 dejó **trece fiscalías sin revisar** (las seis del Noroeste y las siete del Centro) porque
el presupuesto se agotó en armamento. **ARGOS 101 invirtió el orden de triaje en esas dos regiones**:
gastaron sus primeras búsquedas en el módulo judicial. Resultado: **las 32 fiscalías quedan revisadas
en esta edición**, ninguna región cierra con entidades `NO REVISADA`, y la deuda de cobertura
rotatoria queda saldada por primera vez desde que se detectó.

---

## Hechos de la ventana — respaldo por evento

### ARG-101-001 — Pacífico frente a Lázaro Cárdenas, Michoacán (🟢 VERDE)

- **Hecho**: 17-ago-2026. La Octava Región Naval y la Décimo Sexta Zona Naval de la SEMAR localizan
  **54 bultos** con **más de 1,600 kg de presunta cocaína** a la deriva, ~**329 km al suroeste** de
  Lázaro Cárdenas, en patrullaje aéreo de rutina. **Sin detenidos ni embarcación asociada.**
- **Fuentes con fecha en URL**: `razon.com.mx/mexico/2026/08/17/`, `tribuna.com.mx/seguridad/2026/08/17/`,
  `cronica.com.mx/nacional/2026/08/17/`, `diario.mx/nacional/2026/aug/17/`,
  `periodicocorreo.com.mx/nacional/2026/aug/17/`. Además CódigoQro, Atiempo, Meganoticias,
  Periódico Palacio. **Nueve fuentes coinciden** en las 1.6 t, los 54 bultos y la distancia.
- **Discrepancia declarada y resuelta**: el *slug* de La Crónica dice "más de 16 toneladas"; su propio
  titular y las otras ocho fuentes dicen 1.6 t. Se publica **1,600 kg** y el "16" se descarta como
  error de slug, dejándolo anotado para que no reaparezca.
- **Cifras citadas NO integradas**: el valor de 340.2 mdp y los 3.2 millones de dosis son
  estimaciones de la autoridad reproducidas por los medios; las ~90 toneladas del sexenio son un
  **agregado de administración**, fuera de todo conteo del corte.
- **SEMAR citada por todas las fuentes; su comunicado no se localizó indexado.** Confianza ★★★☆☆.
- **Fuera de la taxonomía del módulo de armamento** (es droga).

### ARG-101-002 — Colima, Colima (🟡 AMARILLO)

- **Hecho**: 18-ago-2026. SSPC de Colima + SEMAR + FGE intervienen una presunta casa de seguridad;
  **son agredidos y repelen la agresión**. **Dos presuntos integrantes del CJNG abatidos**,
  identidades no publicadas. Asegurados **granadas, armas de fuego, cargadores, chalecos, carrilleras,
  "más de 2,500 cartuchos"** y equipo táctico.
- **Fecha fijada** en el slug de `puentelibre.mx/...-18-agosto-2026/` y en la URL de
  `infobae.com/mexico/2026/08/18/`. Corroboración: Milenio, El Occidental, Chihuahua en Red.
- **Dos extremos NO arbitrados, publicados sin conciliar**: (a) **detenidos** — Infobae y Puente
  Libre no reportan ninguno, El Occidental reporta **1 mujer detenida** y describe a un abatido como
  **jefe de sicarios**; (b) **restos humanos** en el inmueble, **solo en el titular de Infobae**, sin
  reproducirse en el cuerpo de ninguna otra fuente. **Ninguno se integra.**
- **Señuelos deslindados**: "El Huesos", objetivo prioritario del CJNG abatido en Colima, es del
  **14-may-2026**; "El Topo", presunto jefe de sicarios del CJNG en Colima, del **21-jul-2026**.
  La atribución de "jefe de sicarios" es exactamente el punto por el que este hecho podría
  fusionarse con aquellos. **Son tres hechos distintos.**
- **Evento cualitativo en el módulo de armamento**: ninguna cantidad exacta. **La presencia de
  granadas está confirmada y su cantidad no**; "más de 2,500 cartuchos" es **cifra imprecisa** y por
  regla no se integra. Confianza ★★★☆☆ / Medio.
- **Reserva de reclasificación**: si se confirma el hallazgo de restos humanos, **el evento pasa a
  🔴 ROJO** y con él la valoración del corte.

### ARG-101-003 — Zinapécuaro, Michoacán (🟡 AMARILLO)

- **Hecho**: noche del 17-ago, pasadas las 21:00 h. Detonaciones de alto calibre entre San José del
  Rincón y Taimeo, ~**una hora** de intercambio. Movilización de SEDENA, GN y Guardia Civil.
  **Sin información oficial**: se desconoce si hubo fallecidos o lesionados.
- **Fuentes**: Quadratín, Respuesta, MiMorelia, La Voz de Michoacán, Red 113. **Cinco medios
  regionales coinciden; sin fuente institucional ni nacional.**
- **ADVERTENCIA DE MÉTODO**: la fecha aparece **solo en el cuerpo** ("la noche del lunes 17 de
  agosto"), no en URL ni titular. El único refuerzo objetivo es que el 17-ago-2026 fue lunes.
  **La fecha no queda fijada** y la ficha se publica con esa reserva. Confianza ★★☆☆☆.
- **No se fusionan** dos notas que podrían describir otro hecho: Contramuro (1 muerto, 1 herido,
  bloqueos) y Excélsior (quema de vehículos), ambas sin fecha fijable. Existe un enfrentamiento
  previo documentado en Zinapécuaro en **abril de 2026**.
- **Cero aporte al conteo de armamento.**

### ARG-101-004 — Texcoco y Ecatepec, Estado de México (🟢 VERDE)

- **Hecho publicado el 18-ago**: detención de **cuatro presuntos agentes investigadores de la
  FGJEM** —Benito "N" (57), María Fernanda "N" (38), Efraín "N" (65), Mario "N" (43)— por
  **extorsión y secuestro exprés**, por la **FEMDO** y la **AIC** de la FGR con la SSPC y la Fuerza
  de Tarea Marina Ecatepec. Asegurados armas de uso exclusivo, cartuchos útiles y drogas sintéticas,
  **ninguno con cantidad**.
- **Fuentes**: `infobae.com/mexico/2026/08/18/` (fecha en URL), Quadratín Edomex, Red Acciones.
  **Sin boletín de FGR ni FGJEM localizado.** Confianza ★★★☆☆ / Medio.
- **Fecha del hecho no fijada**: lo fijado es la publicación.
- **Evento cualitativo**; sus **4 detenidos sí se contabilizan** (`ARG-101-ARM-003`).

### ARG-101-005 — Cuauhtémoc, Ciudad de México (🟢 VERDE)

- Cateo de SSC-CDMX y FGJ-CDMX con apoyo de GN y SEMAR, col. Guerrero. **1 arma corta**, cartuchos
  **sin cantidad**, **2 detenidos** (mujer de 27, hombre de 36). Publicación fijada:
  `heraldodemexico.com.mx/nacional/2026/8/17/`; corroboración NotiMX.
- **Único evento del corte con cifra exacta de armamento.** Confianza ★★★☆☆ / Medio.

### ARG-101-006 — Seis municipios, Querétaro (🟢 VERDE)

- Cateos simultáneos informados por la FGE de Querétaro: **7 detenidos**, drogas y armas
  **sin cantidad**. Publicación fijada: `infobae.com/mexico/2026/08/18/`. **Fuente única.**
- **Señuelo descartado**: la nota de "5 cateos, 5 detenidos y 110 dosis" de la estrategia *Sinergia
  por Querétaro* **no pudo fecharse** y es hecho distinto.
- **Hallazgo de método**: `fiscaliageneralqro.gob.mx` es el portal mejor indexado de la región
  Centro, con **fecha en la ruta** (`/portal/AAAA/MM/DD/`) y categoría propia `/sentencias/`.

### ARG-101-007 — Acámbaro, Guanajuato (🟢 VERDE)

- FSPE detiene a **4 personas** en col. San Isidro; **5 armas de fuego**, **137 dosis**, 3
  motocicletas con alteraciones documentales. Publicación fijada en La Crónica y AM (17-ago);
  corroboración Guanajuato Desconocido.
- **La fuente no desglosa cortas y largas.** Se abre el renglón **armas sin clasificar**: repartir
  la cifra sería inventar el reparto. **No suma ni a cortas ni a largas.**
- La búsqueda dirigida a `boletines.guanajuato.gob.mx` **no localizó el boletín** pese a que el texto
  de los medios es reproducción de un comunicado: **la sustitución queda escrita, no se hace en
  silencio.** Confianza ★★★☆☆ / Medio.

### ARG-101-008 — Tijuana, Baja California (🟢 VERDE)

- 3 detenidos (Fausto "N", Ramón "N", Kevin "N") por ataque armado con un fallecido, Zona Centro.
  Publicación fijada: `elimparcial.com/tij/policiaca/2026/08/17/`. **Fuente única.**
- **Sin aseguramiento de armamento publicado** → fuera del conteo. El cuerpo dice "el lunes" y la
  publicación es del mismo lunes 17: **fecha del hecho ambigua**. Confianza ★★☆☆☆.

### ARG-101-009 — Chalco, Estado de México (🟢 VERDE) — cierra `ARG-97-004`

- **Vinculación a proceso** de Raúl "N" (extorsión agravada) y Carlos Eduardo "N" (abuso de
  autoridad), exfuncionarios de la Secretaría del Medio Ambiente; prisión preventiva en Chalco.
- Publicación fijada: `lasillarota.com/metropoli/2026/8/17/`, `cronica.com.mx/.../2026/08/17/`,
  La Jornada 18-ago. **Sin boletín de la FGJEM.**
- **Cierra un seguimiento abierto desde ARGOS 97 y buscado diez veces** entre ARGOS 99 y 100.
  **NO es sentencia**: no entra al módulo judicial. La cifra de **430 mdp** y la cuota de 200 mil
  pesos mensuales por verificentro son **dato periodístico sin respaldo institucional**.
- **Valida la casilla** `SIN RESULTADO INDEXADO EN VENTANA`: el caso nunca estuvo inactivo, estaba
  sin indexar.

### ARG-101-010 — Zapopan, Jalisco (🟢 VERDE)

- La FGR vincula a proceso a **5 presuntos integrantes de "Los Deltas"** por **acopio de armas** y
  posesión de cartuchos de uso exclusivo, tras dos cateos. **Ninguna cifra publicada.**
  Publicación 17-ago, fuente única de tipo agregador. **NO es sentencia.** Confianza ★★☆☆☆ / Bajo.

### ARG-101-SEN-001 — Región Laguna, Durango (🟢 VERDE) — única condenatoria integrada

Ver el desarrollo completo y la justificación de método en la pág. 5 del cartelón.

- **Fuente oficial**: `fiscalia.durango.gob.mx/2026/08/17/fged-obtiene-sentencia-condenatoria-por-mas-de-26-anos-para-responsable-de-homicidio-calificado-y-agravado-por-parentesco-en-la-region-laguna/`
- **El término "sentencia condenatoria" y la pena "más de 26 años" están en el slug del dominio
  institucional**, que es texto primario de la autoridad y no paráfrasis del resumidor, y la fecha
  está en la propia ruta. Esa es la razón por la que se integra pese al bloqueo.
- **Pena no sumable al acumulado** ("más de 26 años" no es cantidad exacta). **Firmeza no
  informada.** **Nombre del sentenciado no publicado**: el que circula procede del cuerpo
  parafraseado, no del texto institucional. **Sin corroboración independiente localizada.**
  Confianza **Medio**.

---

## Cobertura por región — resultado del barrido

| Región | Entidades | Casillas | Hechos en ventana | Consumo |
|---|---|---|---|---|
| **Noroeste** | 6 de 6 revisadas | 1 portal publicó en ventana (`fiscalia.durango.gob.mx`); 7 `SIN RESULTADO INDEXADO` | 2 (`ARG-101-008`, `ARG-101-SEN-001`) | 20/20 |
| **Noreste** | 5 de 5 revisadas | 10 portales dirigidos, 0 con material en ventana | **0** | 20/20 |
| **Occidente** | 6 de 6 revisadas | 1 portal publicó (`boletines.guanajuato.gob.mx`); 4 `SIN RESULTADO INDEXADO` | 3 (`ARG-101-002`, `-003`, `-007`) + `-010` | 20/20 |
| **Centro** | 7 de 7 revisadas | 10 portales dirigidos; Querétaro publicó fuera de ventana | 4 (`ARG-101-004`, `-005`, `-006`, `-009`) | 20/20 |
| **Golfo** | 2 de 2 revisadas | 10 portales dirigidos, 0 con hecho en ventana | **0** | 20/20 |
| **Sureste** | 6 de 6 revisadas | 6 portales dirigidos, 0 con hecho en ventana | **0** | 20/20 |

**Ninguna entidad quedó `NO REVISADA`.** **Ninguna entidad pudo reclamar `SIN ACTUALIZACIÓN
CONSTATADA`**: bajo bloqueo total no puede verse el listado de boletines de ningún portal.

**Tres regiones aportaron cero hechos a la ventana** (Noreste, Golfo, Sureste) con todas sus
entidades consultadas. Ese cero es de **indexación, no de actividad**: las tres localizaron hechos
fuera de ventana en esos mismos portales, lo que demuestra que los emisores sí publican.

### Portales con fecha en la ruta — directorio útil confirmado en este corte

Fechables sin leerlos, y por tanto prioritarios en el triaje de próximas ediciones:
`fiscalia.durango.gob.mx/AAAA/MM/DD/` · `boletines.guanajuato.gob.mx/AAAA/MM/DD/` ·
`fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`.

**Portales con identificador opaco — estructuralmente inservibles bajo bloqueo**:
`fge.chiapas.gob.mx/Prensa/Articulo/<GUID>` (sin fecha alguna) y
`fiscaliatabasco.gob.mx/Boletin/Index/<id>` (numeración sin correspondencia pública con fecha).
Ambos exigen **ancla externa fechada** antes de asignar cualquier boletín a una ventana.

---

## Categorías sin resultado verificable en la ventana

`SIN RESULTADO INDEXADO EN VENTANA` para: **huachicol** (el hecho de Pesquería, NL, es del 14-16 ago
y del boletín federal), **fosas clandestinas**, **desapariciones**, **laboratorios clandestinos**,
**redes financieras y operaciones con recursos de procedencia ilícita**, **extorsión** como hecho
nuevo (los dos casos del corte son resoluciones judiciales, no hechos), **ataques a autoridades**,
**narcobloqueos**, **uso de drones armados** y **artefactos explosivos improvisados**.

Ninguna de estas categorías puede declararse `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`: no se
leyó ningún portal por acceso directo, de modo que la casilla correcta es la de resultado no
indexado.
