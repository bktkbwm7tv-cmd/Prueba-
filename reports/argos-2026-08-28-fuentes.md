# ARGOS 110 — Archivo de fuentes y registro del barrido

**Corte**: 2026-08-28 · **Ventana**: 2026-08-27 10:00 → 2026-08-28 06:25 CDMX (20 h 25 min)

Hora real de arranque verificada en la sesión con `TZ=America/Mexico_City date`:
`2026-08-28 06:25 CST`, viernes. La ventana abre exactamente donde cerró ARGOS 109 (27-ago 10:00),
sin hueco ni solape.

---

## Bloque 0 — verificación de base antes de numerar

`reports/_arranque-ARGOS-110.md` advertía que la rama asignada por el entorno llega desactualizada,
y **volvió a llegar así**: la rama mostraba `argos-2026-08-24` como última edición y **no contenía su
propio archivo de arranque**. `git merge --ff-only origin/main` se ejecutó como primer comando de la
sesión, antes de leer nada. Tras el *fast-forward*, el estado coincidió **exactamente** con el que el
arranque predecía: última edición `argos-2026-08-27` (ARGOS 109), **72 archivos** en `reports/` y
`main` conteniéndola.

**Cuarta edición consecutiva en que el patrón evita un error de numeración.** Numerar por lo que la
rama tenía a la vista habría producido un falso ARGOS 107 con ventana solapada por tercera vez.

---

## Bloque de método — reparto de presupuesto y rendimiento

Se conservó el reparto que invirtió el patrón en ARGOS 109: **~60-65 % consulta genérica sin
`site:`**, ~25 % `site:` dirigido para desglose numérico oficial, ~10 % judicial.

| Origen del hecho publicado | ARGOS 108 | ARGOS 109 | **ARGOS 110** |
|---|---|---|---|
| Barridos regionales | 3 de 8 | 4 de 6 | **2 de 4** (Zacatecas, Cintalapa) |
| Recall nacional del coordinador | 5 de 8 | 2 de 6 | **2 de 4** (Escuinapa, Pedernales) |

**El recall nacional volvió a ser decisivo, y esta vez sobre todo por lo que impidió.** Aportó dos de
los cuatro hechos —**Escuinapa no lo vio el barrido del Noroeste, que declaró su región sin hallazgos
en ventana**— y, además, **interceptó tres falsos positivos**:

1. **El comunicado conjunto SSC CDMX–SSEM** —«siete detenidos con armas, policías municipales
   muertos»— que el barrido del Centro trajo como candidato de alto impacto con `fecha no fijada`.
   Es el hecho de la **persecución de San Antonio la Isla y Tenango del Valle del 17 de marzo de
   2023**, con tres policías muertos. **El comunicado no lleva fecha en la ruta**, y es exactamente el
   supuesto de la regla nacida en ARGOS 109: *un número de comunicado sin fecha en la ruta no
   identifica un documento*. De haber entrado, ARGOS 110 habría publicado como hecho del corte un
   ataque de hace tres años y medio con dos policías muertos.
2. **Los «27 artefactos explosivos de Escuinapa»**, devueltos por el buscador junto a los resultados
   del hecho real: son **La Campana, Escuinapa**, ya publicados como `ARG-103-REC-001`.
3. **El «coche bomba de Escuinapa»** y los **ataques con dron** del mismo municipio: son de
   **junio y julio de 2026**, no de esta ventana. Se usan como contexto de escalamiento en la
   Explotación, nunca como hecho del corte.

**El `grep` obligatorio a `indice-arg-id.md` volvió a rendir, por tercera edición consecutiva.**
Interceptó que **la detención de «El Dron» en Puebla, publicada por medios nacionales el 27-ago, es
`ARG-109-004`**, ya fichada. Sin el `grep` se habría publicado como hecho nuevo del corte.

**Desviación de presupuesto declarada**: cinco de los seis barridos alcanzaron el techo superior
orientativo (Noroeste 20, Noreste 20, Occidente 19, Sureste 20, Golfo 16); Centro cerró en 18 pero
**gastó 9 de sus 18 búsquedas en el eje de «El Dron»**, más del doble de las 4 presupuestadas, por
la prioridad declarada del destinatario. **Se acepta declarado.** El coste fue real: Estado de
México, Morelos e Hidalgo recibieron una sola consulta genérica cada uno.

---

## Rotación de cobertura — Ciclo C, declarado y evaluado

**Se aplicó el Ciclo C: Occidente y Sureste encabezaron el triaje judicial**; las otras cuatro
regiones encabezaron con armamento y con la deuda de portales de SSP.

**Qué aportó el ciclo que el orden anterior no habría aportado:**

- **Ninguna sentencia integrable, y esta vez el vacío está acreditado y no supuesto.** Las doce
  fiscalías de las dos regiones fueron recorridas una por una. Sureste localizó **once resoluciones
  condenatorias reales** —Oaxaca cinco, Guerrero, Yucatán dos, Campeche, Quintana Roo dos— y
  Occidente localizó otras tantas. **Todas quedaron fuera por fecha de publicación**, entre el 3 y el
  26 de agosto. El vacío judicial de este corte es **de calendario, no de búsqueda**.
- **El hallazgo de mayor valor del ciclo no fue judicial**: al recorrer el Sureste, el barrido
  **cerró el candidato de Cintalapa** localizando una URL con día en la ruta. Ese candidato llevaba
  abierto desde ARGOS 109 como `FECHA NO FIJABLE`.
- **Constatación de fondo, para el archivo**: con ventanas de ~20 horas, **la probabilidad de que una
  fiscalía publique exactamente en esa franja es baja**. El triaje judicial encabezado sigue siendo
  necesario para que el `SIN DATO` sea demostrable, pero **su rendimiento en sentencias integrables
  está estructuralmente limitado por la duración de la ventana**, no por el orden de búsqueda.
  Es un dato que el ciclo A de ARGOS 108 enmascaró al producir una sentencia.

**Prioridad sobre el ciclo, aplicada**: las cuatro regiones restantes encabezaron con la deuda de los
once portales de SSP, por delante del armamento. Resultado en el apartado siguiente.

---

## La deuda de los once portales de SSP — estado tras esta edición

Abierta desde ARGOS 107, **sin tocarse en tres ediciones**. Esta edición la ataca por primera vez.
**No queda saldada, pero deja de ser una lista de nombres sin dominio.**

| Portal | Estado tras ARGOS 110 |
|---|---|
| **Tabasco** | ✅ **SALDADO.** **No existe subdominio propio**: la SSP publica bajo `tabasco.gob.mx/seguridad` y `tabasco.gob.mx/categoria/seguridad-publica`. La deuda era, en parte, una hipótesis de dominio inexistente |
| **Coahuila** | ✅ Dominio real **`sspcoahuila.gob.mx`** (sin punto). Existe, indexa poco. Sin boletín del periodo |
| **Tamaulipas** | ✅ **Sin subdominio propio**: integrada en `tamaulipas.gob.mx/seguridadpublica/`. Boletines indexados solo hasta el 14-ago |
| **San Luis Potosí** | ✅ **`seguridad.slp.gob.mx`**, con indexación activa hasta el 24-ago. ⚠️ Coexisten `sspslp.mx` y `sitio.sanluis.gob.mx/SSPC/` — **cuál es canónico queda sin resolver** |
| **Durango** | ✅ **`seguridad.durango.gob.mx/seccion/boletines/`**, con boletines indexados, **los más recientes de enero-abril 2026** |
| **Chihuahua** | ⚠️ **`sspe.chihuahua.gob.mx`** — hipótesis heredada `ssp.chihuahua.gob.mx` **era falsa**. Localizado, **no interrogado al periodo**: `NO REVISADA` |
| **Baja California** | ⚠️ **`seguridadbc.gob.mx`** (Secretaría de Seguridad Ciudadana), con `sspbc.gob.mx` en paralelo para transparencia. **Cuál sirve boletines, sin resolver** |
| **Baja California Sur** | ⚠️ Dos candidatos: **`sspbcs.gob.mx`** y **`ssbcs.gob.mx`**, ambos resuelven. **Sin resolver cuál es el oficial activo** |
| **Puebla** | ✅ **`ssp.puebla.gob.mx`**. Publica **acumulados de periodo**, no boletín diario: 600 acciones operativas del 1 al 15 de agosto, 175 detenciones, 178,370 L de huachicol entre el 4-jun y el 16-ago. **Ninguna cifra atribuible a esta ventana** |
| **Tlaxcala** | ⚠️ **Ambigüedad no resuelta**: `ssc.tlaxcala.gob.mx` y `ssctlaxcala.gob.mx` devuelven resultados ambos. Publicó el 26-ago un balance **de julio** (87 vehículos, 68 detenidos, 7 armas): fuera de ventana por partida doble |
| **Nayarit** | ⚠️ Dominio ya confirmado (`ssypc.nayarit.gob.mx`), **no interrogado por `site:` directo**: `NO REVISADA` |

**Balance honesto: 5 de 11 resueltos** —Tabasco, Coahuila, Tamaulipas, SLP, Durango, más Puebla con
matiz—; **4 con dominio precisado pero no interrogado**; **2 con ambigüedad de dominio abierta**.
**Lo que se aprendió es que la deuda era en parte inexistente**: al menos dos de los once portales
—Tabasco y Tamaulipas— **no tienen subdominio propio**, de modo que tres ediciones han cargado con
una deuda que en su caso no podía saldarse buscando un dominio que no existe.

**Tlaxcala** sigue con cobertura débil: `fgjtlaxcala.gob.mx` fue consultada con `site:` dirigido y no
devolvió sentencia indexada; **`fecc.fgjtlaxcala.gob.mx` quedó `NO REVISADA`** por agotamiento del
presupuesto tras el eje de «El Dron».

---

## Triple consulta del boletín federal — resultado y corrección a ARGOS 109

Ejecutada **en las tres formas** por el coordinador:

1. **Día suelto** («acciones relevantes del 27 de agosto de 2026») → no devuelve.
2. **Rango o agregado** → no devuelve agregado del 26-27.
3. **Título sin `site:`** → devuelve **el boletín del 26 de agosto**, a través de dos republicadores:
   `red113mx.com/2026/08/…` (con año y mes en la ruta) y `tallapolitica.com.mx`.

**Corrección a ARGOS 109, que se registra aquí y no en el cartelón.** Aquella edición declaró que
«no existe boletín del 26 ni del 27 con URL verificable» y contabilizó el caso como el **cuarto falso
positivo del resumidor**. **El boletín del 26 de agosto sí existe**: lo que fallaba era la indexación
de `gob.mx`, no el documento. Se alcanza únicamente **por republicadores**, que es exactamente el
supuesto que la **tercera forma de la triple consulta** —añadida en ARGOS 104— fue escrita para
cubrir. La conclusión de ARGOS 109 sobre el 26-ago **se corrige**; la del 27-ago **se confirma**: no
existe boletín de ese día con URL verificable.

**ARG-ID de la corrección: `ARG-110-FE-001`.** Registrado en `indice-arg-id.md`, **sin presencia en el
cartelón**, conforme a la instrucción del destinatario.

**Corroboración débil por construcción**: los dos republicadores del boletín del 26-ago **no son
fuentes independientes entre sí**. Por eso su desglose (Durango: 3 cortas, 6 largas, 600 cartuchos,
22 cargadores, 12 granadas, 4 detenidos) va en la **línea inferior** de las tarjetas de armamento y
**no se suma a ningún total**.

---

## Registro del barrido — región por región

### Noroeste (BC, BCS, Sonora, Chihuahua, Sinaloa, Durango) — 6 de 6 · 20 búsquedas

- **Sin hecho propio con cifra anclada en ventana.** Todos los aseguramientos con desglose que el
  buscador devuelve para la región son del 14 al 26 de agosto.
- **No vio Escuinapa**, que es el hecho de mayor volumen de su región en la ventana. Lo aportó el
  recall nacional. Es el argumento empírico más fuerte de esta edición a favor de mantener el recall.
- Casillas: `SIN RESULTADO INDEXADO EN VENTANA` para SSP de Chihuahua, BC, BCS y Durango, FGJ Sonora,
  Fiscalía de Sinaloa y Fiscalía de Chihuahua. **Cero** `SIN ACTUALIZACIÓN CONSTATADA`.
- Cobertura desigual declarada: **Baja California Sur y Sonora** recibieron solo búsqueda genérica.

### Noreste (Coahuila, NL, Tamaulipas, SLP, Zacatecas) — 5 de 5 · 20 búsquedas

- **Aporta `ARG-110-001`** (Tabasco, Zacatecas), por **consulta genérica**, no por `site:`.
- **FGJ Nuevo León**: no se reintentó, por instrucción. La acreditación de ARGOS 109 —no publica
  boletín indexable en portal— se mantiene.
- Reparto real declarado: ~70 % genérico / 20 % `site:` / 10 % judicial, con sobreconsumo en genérico
  por tres trampas de fecha (Coahuila abril y junio, Nuevo León 21-26 ago, SLP 26 ago).

### Occidente (Jalisco, Colima, Nayarit, Aguascalientes, Michoacán, Guanajuato) — 6 de 6 · 19 búsquedas

- **Encabezó el triaje judicial (Ciclo C).** Seis fiscalías recorridas, **sin sentencia integrable**.
- Localizó el hecho de **Pedernales** como subproducto del recorrido judicial.
- **Cierra la contradicción de Guanajuato** heredada de ARGOS 109: los homicidios son del
  **martes 25 de agosto** —día de semana verificado—, con cifra de 7 hombres y 2 mujeres anclada en
  `redmetropolitana.com.mx/2026/08/26/`. **Fuera de ventana**; no requiere arbitraje para este corte.
- **Descartó los narcobloqueos «tras la muerte de El Mencho»**: son del **22 de febrero de 2026**.
  Trampa de mes evitada.
- **Morelia (`ARG-106-REC-002`)**: gastada la única búsqueda autorizada, sin novedad. **Se cierra.**

### Centro (CDMX, Edomex, Morelos, Puebla, Tlaxcala, Hidalgo, Querétaro) — 7 de 7 · 18 búsquedas

- **Sin hecho propio en ventana.**
- **Eje prioritario de «El Dron» (`ARG-109-004`): sin avance, y el resultado negativo es informativo.**
  Ver apartado propio abajo.
- **Querétaro (`ARG-109-005`)**: el boletín de la FGE `fiscaliageneralqro.gob.mx/portal/2026/08/26/`
  es el mismo hecho ya fichado. **Los dos vacíos siguen abiertos**: las tres armas siguen **sin
  clasificación publicada** y el efectivo sigue como «importante cantidad» **sin cifra**. Es un vacío
  de publicación acreditado, no de búsqueda.
- **Descartó la operación CJNG Hidalgo-Jalisco-Michoacán** (20 detenidos, 10 armas): es del 24-ago.
- **`fecc.fgjtlaxcala.gob.mx`: `NO REVISADA`**, declarado.

### Golfo (Veracruz, Tabasco) — 2 de 2 · 16 búsquedas

- **Sin hecho ni aseguramiento en ventana.**
- **Deuda de portal saldada**: SSP de Tabasco sin subdominio propio.
- **Cierra el candidato de Jalapilla, Rafael Delgado**, abierto desde ARGOS 109:
  `golpepolitico.com/2026/08/25/…` lo fija en el **martes 25 de agosto**, día de semana verificado.
  **Fuera de toda ventana cubierta.** Se cierra sin integrar.
- **Localiza el agregado de la FGE Veracruz** del 27-ago: 55 resoluciones judiciales «en 24 horas»,
  de ellas **16 sentencias condenatorias** y un caso destacado de **50 años por secuestro agravado en
  Coatzacoalcos**. **No integrable**: sin fuente primaria —solo republicadores con texto idéntico, que
  no son independientes—, sin individualización de caso alguno, mezclando sentencias con 36
  vinculaciones a proceso y 19 imputaciones, y con periodo de «24 horas» sin hora de inicio.
  `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL` + `FRONTERA DE VENTANA`.
  **Tercera edición consecutiva con el mismo defecto de formato del mismo emisor** (36, 46 y ahora 55).
- No completó la triple consulta federal por presupuesto; **la ejecutó el coordinador**.

### Sureste (Chiapas, Oaxaca, Guerrero, Campeche, Yucatán, Quintana Roo) — 6 de 6 · 20 búsquedas

- **Encabezó el triaje judicial (Ciclo C).** Seis fiscalías recorridas, once resoluciones localizadas,
  **ninguna en ventana**.
- **Aporta `ARG-110-003` y resuelve la fecha de Cintalapa**, abierta desde ARGOS 109. Ver abajo.
- **Aporta el hallazgo de Totolapan** (`ARG-110-REC-001`), fuera de ventana por hora.
- **Loxicha (`ARG-109-002`): sin avance.** La búsqueda dirigida devolvió mayoritariamente la
  emboscada de **Santiago Mitlatongo / Magdalena Jaltepec de noviembre de 2023** —otra región, otro
  año, otras cifras—, **caso homónimo por tema** que se descarta expresamente. **El deslinde
  criminal-agrario sigue abierto.**
- **Campeche, Yucatán y Quintana Roo: consulta combinada, no individual.** Declarado, no disfrazado.

---

## Cintalapa — cómo se cerró un candidato que llevaba una edición abierto

ARGOS 109 lo dejó como `FECHA NO FIJABLE — NO INTEGRAR`: la nota decía «a media tarde del jueves», el
jueves de esa semana era el 27-ago, y su tarde era **posterior al cierre de aquella ventana**. La URL
solo anclaba `/2026/08/`.

**Lo cerró exactamente lo que el arranque predijo que lo cerraría: una URL con día en la ruta.**
`miguelangelluna.mx/2026/08/27/enfrentamiento-armado-deja-un-muerto-y-un-detenido-en-chiapas` fija el
hecho en el **jueves 27 de agosto**, coherente con el calendario y con «media tarde», que es
posterior a las 10:00 de apertura de esta ventana. **El hecho es de ARGOS 110.**

**Nota sobre el resumidor**: insistió en «26 de agosto» en **tres consultas distintas**, sin ancla de
URL que lo sostuviera. Se descartó esa fecha. Es la misma lección de ARGOS 103 y 109: **el día de la
semana contra el calendario, y la fecha en la ruta, vencen al resumen**.

**Deslinde declarado**: el «operativo Cuauhtémoc» de Cintalapa —3 detenidos, 2 rifles 7.62×39,
1 pistola 9 mm, 27 cargadores, 752 cartuchos— **no se funde** con este hecho: no tiene fecha en la
ruta y podría ser de otro día. Mismo municipio y mismo calibre hacen el riesgo de doble conteo alto,
y la fecha no lo descarta. **Sus cifras no se integran.**

---

## «El Dron» — el seguimiento prioritario, y por qué su resultado negativo es un dato

La pregunta que el destinatario declaró prioritaria: **¿las tres armas viajaron con él desde Sinaloa
o se las dieron en destino?** —lo que distingue **red de traslado** de **red de acogida**, y cambia
dónde se busca al segundo tirador.

**Respuesta: `SIN RESULTADO INDEXADO EN VENTANA`, por los dos lados.**

- **Lado Puebla** (barrido Centro, 9 búsquedas): ninguna fuente publica **cotejo balístico, número de
  serie ni procedencia** de las tres armas. Tampoco **contrato de arrendamiento, titular del servicio
  eléctrico ni padrón vehicular** del inmueble. `fiscalia.puebla.gob.mx` consultada por `site:`, sin
  boletín del caso.
- **Lado Sinaloa** (barrido Noroeste): ni la Fiscalía de Sinaloa ni la SSP publicaron **carpeta,
  cotejo ni novedad sobre el segundo tirador**.

**Dos hallazgos que sí produjo el eje, y que van aquí y no al cartelón:**

1. **Contradicción de fuentes sobre la identidad del segundo tirador, sin arbitrar.** Un resumen
   afirma que «otro sospechoso referido como El Dron también escapó de Culiacán a Puebla pero sigue
   prófugo», lo que **choca con la identificación mayoritaria de que El Dron es el detenido**
   (Jesús Alberto Hidalgo Iribe). **No se arbitra sin lectura directa del boletín.** Se registra.
2. **Posible confusión de dos operativos distintos en Cholula.** `diariocambio.com.mx` atribuye un
   operativo en Cholula a la detención de **«la Tripa», líder del «comando Tlahuica»**, objetivo
   distinto. **No puede resolverse bajo el bloqueo de egreso.** Se declara como contradicción sin
   arbitrar, no se integra.

**El dato de gestión**: el hecho se publicó el 26-ago, la cobertura nacional lo replicó el 27, y
**treinta horas después ninguna autoridad ha publicado nada sobre la estructura que lo alojaba**. La
pregunta del cotejo balístico **no la contesta el buscador: la contesta un oficio**. Se traslada a
`_pendientes.md` sin degradar su prioridad.

---

## Correcciones a ediciones anteriores — todas aquí, ninguna en el cartelón

Conforme a la instrucción del destinatario, reiterada al cierre de ARGOS 109 e incumplida por aquella
edición. **El cartelón de ARGOS 110 no abre página, sección ni ficha de fe de erratas.** Los ARG-ID
`-FE-` se asignan y se registran en `indice-arg-id.md`.

| ARG-ID | Corrección |
|---|---|
| `ARG-110-FE-001` | **El boletín federal del 26-ago sí existe.** ARGOS 109 lo declaró inexistente por falta de URL y lo contabilizó como cuarto falso positivo del resumidor. Se alcanza por republicadores; el fallo era de indexación de `gob.mx`, no del documento. **Se corrige la conclusión sobre el 26-ago; se confirma la del 27-ago** |
| `ARG-110-FE-002` | **Tijuana, Zona Centro** (candidato de ARGOS 109, `FRONTERA DE VENTANA — FECHA NO FIJADA`): **anclado al miércoles 26-ago** por `elimparcial.com/tij/policiaca/2026/08/26/`, día de semana verificado. **Fuera de la ventana de ARGOS 110.** Reserva resuelta, candidato cerrado |
| `ARG-110-FE-003` | **Bar de Concordia, Sinaloa** (candidato de ARGOS 109, sin URL propia): **anclado al domingo 23-ago** por `luznoticias.mx/2026-08-23/`, con **6 heridos**. Queda **fuera de las ventanas de ARGOS 109 y 110**; debió cerrarse en una edición anterior. Candidato cerrado, no integrado |
| `ARG-110-FE-004` | **Jalapilla, Rafael Delgado, Veracruz** (candidato de ARGOS 109, sin fecha): **anclado al martes 25-ago** por `golpepolitico.com/2026/08/25/`. **Fuera de toda ventana cubierta.** Candidato cerrado |
| `ARG-110-FE-005` | **Guanajuato, «ocho homicidios en cinco horas»** (`CONTRADICHA` desde ARGOS 109): el hecho es del **martes 25-ago**, con 7 hombres y 2 mujeres, anclado en `redmetropolitana.com.mx/2026/08/26/`. **Fuera de ventana**; la contradicción de cifra con `paginanueve.com` **no se arbitra porque ya no afecta a ningún corte abierto** |

**Ninguna de estas cinco correcciones apareció en el cartelón.** Ninguna cambia una cifra publicada:
las cinco cierran candidatos o corrigen una conclusión de método.

---

## Candidatos no integrados — el registro completo

| Candidato | Motivo |
|---|---|
| **CDMX / Edomex — comunicado conjunto SSC-SSEM**, 7 detenidos, policías muertos | `DESCARTADO — HECHO DEL 17 DE MARZO DE 2023`. Comunicado sin fecha en la ruta. Interceptado por el recall nacional |
| **Sinaloa · Escuinapa** — segundo desglose (6 rifles, 40 cargadores, 5 AEI, 6 personas) | `POSIBLE DUPLICIDAD — NO INTEGRAR HASTA VALIDACIÓN`. Difiere del parte de SEDENA en detenidos (7/6) y armas (5/6); la vocería estatal habla de 5 detenidos |
| **Chiapas · Cintalapa**, «operativo Cuauhtémoc» | `FECHA NO FIJABLE`. Mismo municipio y calibre que `ARG-110-003`: riesgo alto de doble conteo |
| **San Luis Potosí · Santa María del Río**, narcolaboratorio, 11 detenidos | `FUERA DE VENTANA`. Original ancla `/2026/08/26/`; la republicación del 27 no aporta hora |
| **Nuevo León** — 8 armas, 19 cargadores, 2,690 cartuchos | `FUERA DE VENTANA`. Boletín federal del 26-ago |
| **Coahuila · Castaños y Progreso** — 116 armas y otro de 10 armas | `TRAMPA DE MES`. Fechas reales: **14-abr** y **29-jun de 2026** |
| **Guanajuato · San Diego de la Unión** — secuestro agravado, 70 años, 4 sentenciados | `FUERA DE VENTANA`. Publicado 26-ago |
| **Michoacán · Jiquilpan** — violación equiparada agravada, 11a1m10d | `FUERA DE VENTANA`. Publicado 24-ago |
| **Once resoluciones del Sureste** (Oaxaca ×5, Guerrero, Yucatán ×2, Campeche, QRoo ×2) | `FUERA DE VENTANA`. Publicadas entre el 4 y el 26 de agosto |
| **Sentencias FGR Noroeste** (Chihuahua, Cd. Juárez, Nogales, Etchojoa) | `FUERA DE VENTANA`. Todas fechadas 14-ago (DPE/3539, 3541, 3542, 3548, 3549) |
| **Coahuila · Piedras Negras** — tráfico de personas, 9a7m6d | `PENDIENTE DE ANCLA FECHADA`. Segunda edición sin URL con fecha en la ruta. **Advertencia de homónimo**: otro caso del mismo delito en Coahuila con pena de **12 años** |
| **Veracruz** — agregado de 55 resoluciones, 16 condenatorias | `PENDIENTE DE CONFIRMACIÓN OFICIAL` + `FRONTERA DE VENTANA`. Solo republicadores, sin individualización |
| **Nayarit** — dos sentencias en Facebook oficial | `SIN ANCLA DE FECHA`. Los posts no llevan fecha en la ruta |
| **Guerrero · Cerro de las Lumbreras** | **Integrado como `-REC-`**, no como hecho del corte: 04:00 h del 27-ago, **anterior a la apertura** |
| **Guerrero · El Arenal, Acapulco** | **Integrado como `-REC-`**: hallazgo del miércoles 26-ago |

---

## Nota sobre la frontera de ventana

**Tres de los cuatro hechos llevan `FRONTERA DE VENTANA — HORA NO FIJADA`.** La causa es la misma que
ARGOS 102 documentó y que ARGOS 109 sufrió en cinco de seis: **las ventanas de ARGOS se declaran con
precisión de minutos y las fuentes publican con precisión de día.**

Esta edición añade un matiz que conviene registrar: **la frontera cortó en los dos sentidos y con
consecuencias opuestas**, lo que valida la regla.

- **Hacia dentro**: Cintalapa entró porque «media tarde» es inequívocamente posterior a las 10:00.
- **Hacia fuera**: **Totolapan quedó fuera por seis horas** —04:00 h contra apertura a las 10:00—
  pese a ser, con seis muertos, el hecho de mayor saldo humano de las dos ventanas. Se publica como
  recuperación, fuera de todos los totales. **Si se hubiera integrado, el semáforo de este corte
  mostraría cuatro rojos y el nivel de riesgo sería otro.**

**Los totales de esta edición no son comparables sin más** con los de ediciones cuyos hechos quedaron
fijados por hora dentro de ventana. **Declarado en el cartelón, en una línea.**

---

## Controles editoriales

| Control | Ejecución | Resultado |
|---|---|---|
| `barrido-regional` ×6 | **Subagentes, autorizados** | 32 de 32 entidades. Cobertura declarada por entidad, no por portal |
| `editor-duplicidad` | **A mano** — la autorización cubrió solo los barridos | **Tres hallazgos.** (1) `grep` del índice interceptó que la detención de «El Dron» es `ARG-109-004`; (2) deslindó **El Pedregoso (26-ago, `ARG-109-001`) de Pedernales (27-ago, `ARG-110-004`)**: localidad, fecha y saldo distintos, no es el mismo hecho; (3) verificó las trece localidades nuevas contra todo el archivo — **«El Arenal» previo es el municipio de Hidalgo, no la comunidad de Acapulco**, y **«Cintalapa» previo son casos judiciales de otro expediente** |
| `procedencia-cifras` | **A mano** | **Cuatro retiradas.** (1) «veintiséis días de diferencia» — **cifra derivada no declarada**, sustituida por las dos fechas; (2) **la hora «10:00 h» y la ubicación «camino a Los Sábalos» de Escuinapa solo existían en el resumen del buscador** — retiradas, la marca de frontera se conserva; (3) «a unos quince minutos del poblado» en El Arenal — **distancia estimada por el redactor**, prohibida: **tercera edición consecutiva con el mismo defecto**; (4) «veintiuna resoluciones descartadas» — **conteo propio no verificable**, sustituido por la única cifra que un barrido declaró (once, Sureste). Además obligó a **declarar como cálculo propio** los dos totales de armamento y la línea inferior |

**Cuarta edición consecutiva en que los dos controles ejecutados a mano producen hallazgos reales.**
El defecto de las distancias estimadas por el redactor **reincide por tercera vez** (ARGOS 108, 109 y
110): deja de ser un descuido y pasa a `_pendientes.md` como deuda de método con causa identificada.

---

## Limitaciones declaradas

- **Egreso bloqueado, vigesimosegunda edición.** Verificado en esta sesión, no heredado: `gob.mx`,
  `gabinetedeseguridad.gob.mx` y `fiscaliasinaloa.mx` devuelven
  `curl: (56) CONNECT tunnel failed, response 403`; `www.infobae.com` devuelve `EGRESS_BLOCKED` en
  `WebFetch`. **Cero portales leídos por acceso directo.** Techo de confianza: **★★★★☆**; ninguna
  ficha lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
- **`gabinetedeseguridad.gob.mx/resultados/`: quedan cuatro días.** Obligatorio desde el 1 de
  septiembre. **Si el corte de ARGOS 111 cae en septiembre, su ausencia es un vacío exigible, no una
  limitación heredada**, y debe declararse como tal.
- **Ninguna fiscalía ni portal se declara `SIN ACTUALIZACIÓN CONSTATADA`**: esa casilla exige lectura
  directa del listado de boletines, imposible bajo el bloqueo. Todas quedan en
  `SIN RESULTADO INDEXADO EN VENTANA` o en `NO REVISADA`.
- **Ninguna ficha de esta edición tiene boletín institucional propio con URL localizada.** Es la
  primera edición reciente sin un solo portal oficial que publique en ventana: ARGOS 109 tuvo al
  menos la FGE de Querétaro. Las cuatro fichas se sostienen en **fuente institucional por cita** más
  corroboración de medios.
