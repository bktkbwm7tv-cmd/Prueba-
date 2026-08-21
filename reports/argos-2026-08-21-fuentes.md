# ARGOS 104 — Registro de fuentes

Corte: 2026-08-21 · Ventana de hechos: **2026-08-20 08:16 CDMX → 2026-08-21 07:55 CDMX**.
Continuación estricta de ARGOS 103 (corte 2026-08-20). Este documento respalda
`argos-2026-08-21.html` y `argos-2026-08-21-movil.html`, y existe para que todo `SIN DATO` de la
edición sea demostrable.

Ventana efectiva: **~23.6 horas**, de la mañana del jueves a la mañana del viernes. Comparable en
duración a la de ARGOS 103 (~24.5 h).

**Hora de arranque verificada**: `TZ=America/Mexico_City date` → **2026-08-21 07:55 CST (UTC−6)**.
Es la hora sellada en encabezado, pie y todas las marcas `Consulta:` del cartelón.

---

## Limitación metodológica — decimoquinta edición consecutiva con el egreso bloqueado

Los dominios `*.gob.mx` y los de fiscalías y secretarías estatales siguen fuera de la lista blanca
de egreso del entorno (`CONNECT tunnel failed, response 403`). Consecuencias vigentes, sin cambio
respecto de ARGOS 103:

- **Cero portales institucionales leídos por acceso directo.** Todo lo institucional de esta
  edición llega por búsqueda `site:` dirigida o por reproducción en medios.
- **El techo de confianza de todo el producto sigue siendo ★★★★☆.**
- `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**. Es el único cambio que elevaría
  el techo del producto.

Conforme a la instrucción de arranque, **esta edición no gastó ninguna búsqueda en el pendiente de
Veracruz** (`BLOQUEADO POR EGRESO`, seis ediciones intentándolo).

---

## PRIORIDAD 2 — Rectificación en bloque de las valoraciones de ARGOS 99, 100 y 101

**Ejecutada.** Era el segundo encargo de PRIORIDAD 1 de `_pendientes.md` y llevaba una edición
abierta: ARGOS 103 estableció los conteos rectificados y los publicó en su propia fe de erratas,
pero **los tres cartelones afectados seguían publicando su valoración original**, dos de ellas
`NO DETERMINABLE`, sin que quien los abriera tuviera forma de saber que estaban rectificadas.

### Formato elegido y por qué

Se decidió entre las dos opciones que `_pendientes.md` planteaba:

| Opción | Decisión |
|---|---|
| Nota de fe de erratas **insertada en cada cartelón afectado** | **ELEGIDA** |
| **Cartelón de rectificación propio** | Descartada |

**Razón**: un cartelón de rectificación separado deja intacta la valoración falsa **en el punto de
consulta**. Un mando que abre `argos-2026-08-17.html` lee `NIVEL NO DETERMINABLE` y no tiene por qué
saber que existe un documento posterior que lo desmiente. La rectificación tiene que estar donde
está el error. El cartelón de rectificación propio, además, habría sido ARGOS hablando de ARGOS
durante siete páginas, que es justo lo que la regla del mando prohíbe.

### Lo que se insertó

Un bloque compacto, inmediatamente **encima** del texto de la valoración original, en **las seis
piezas** (escritorio y móvil de las tres ediciones). El texto original **no se altera ni se borra**:
el archivo conserva lo que se publicó y añade lo que hoy consta.

| Edición | Archivo | 🔴 publicado | 🔴 rectificado | Hechos rectificadores |
|---|---|---|---|---|
| **ARGOS 99** | `argos-2026-08-16.html` + `-movil` | 3 | **5** | `ARG-103-REC-003` Iguala · `ARG-103-REC-004` estudiantes UV |
| **ARGOS 100** | `argos-2026-08-17.html` + `-movil` | 0 — `NO DETERMINABLE` | **2** | `ARG-103-REC-005` El Pital · motín de Cárdenas (ARGOS 102) |
| **ARGOS 101** | `argos-2026-08-18.html` + `-movil` | 0 — `NO DETERMINABLE` | **3** | `ARG-103-REC-006` Celaya · Tlapa de Comonfort y Colima (ARGOS 102) |

**Alcance declarado en cada bloque**: afecta al **conteo de eventos 🔴 y a la valoración**; **no** a
las fichas publicadas ni a los totales de armamento, detenidos o sentencias, que quedan como se
publicaron.

### Dos precisiones que la rectificación incorpora y que no estaban dichas

1. **ARGOS 99 no se invierte, y decirlo importa.** Es la única de las tres cuya valoración sigue en
   pie: registró tres rojos, el nivel era determinable y el alza que declaró era correcta. Lo que
   cambia es que se apoyaba en **tres quintas partes** de los rojos de su ventana — y los dos
   omitidos son **homicidios múltiples contra civiles**, exactamente el rasgo en que ese corte fundó
   su alza. La conclusión era buena; la base era más estrecha de lo que el propio corte creía.
2. **ARGOS 101 había planteado bien su reserva.** Su texto declaraba que si los restos humanos de
   Colima se confirmaban, el evento reclasificaba a rojo «y con él la valoración del corte». **Se
   confirmaron.** La reserva estaba correctamente planteada; lo que faltó fue **volver sobre ella**.
   Es un fallo de seguimiento, no de criterio, y se distingue del de ARGOS 100, que es de cobertura.

### Residuo conocido que esta edición no cierra

Las **portadas** de ARGOS 100 y 101 (semáforo y contadores del radar) siguen mostrando el conteo
original, porque están generadas desde el arreglo `EVENTOS` de cada edición y regenerarlas obligaría
a reescribir fichas que la rectificación deja expresamente intactas. `NO DETERMINABLE` **solo
aparece en la valoración** de ambas ediciones —verificado con `grep`—, que es donde está el bloque
rectificador. Queda anotado en `_pendientes.md`.

---
## PRIORIDAD 1 — La auditoría hacia atrás sobre las ventanas de ARGOS 95 a 98

Ejecutada **primero y en solitario**, cuarta edición consecutiva que confirma el valor de esa
secuencia. Método heredado de ARGOS 103 y ordenado por `_pendientes.md`: **consultar por tipo de
hecho y no por entidad**, en equipos temáticos, más una ronda de corroboración.

| Equipo | Perímetro | Presupuesto | Consumo |
|---|---|---|---|
| **1-A** | Masacres y homicidios múltiples | 20 | **20 de 20** |
| **1-B** | Violencia colectiva: motines, fosas, narcobloqueos, AEI, drones armados, desaparición y secuestro múltiples, infraestructura crítica | 20 | **20 de 20** |
| **1-C** | Ronda de corroboración | 18 | *(ver abajo)* |

El bloque de **ataques contra autoridades se omitió**, conforme a la instrucción: ARGOS 103 demostró
que ese tipo de hecho **sí se recoge**, y el presupuesto rendía más en el segmento que sí se pierde.

### Verificación personal del coordinador — no delegada

Tercera edición que aplica la regla, y tercera en que **salva al producto de una acusación falsa**.
Cada candidato a omisión se contrastó con `grep` sobre todo el repositorio **antes** de aceptarlo.

**Candidato rechazado: San Pedro Amuzgos, Oaxaca** (14-ago, tres personas ejecutadas dentro de un
domicilio). El equipo 1-A lo trajo como omisión de ARGOS 98. **Es falso**: está publicado como
`ARG-99-003`, con la Fiscalía General de Oaxaca confirmando, e integrado por ARGOS 99 como *evento
anterior publicado durante el corte*. El archivo, además, **lo sostiene mejor que el hallazgo**: el
equipo no localizó fuente institucional y el archivo sí la tiene. Sin `grep`, ARGOS 104 habría
acusado a ARGOS 98 de una omisión inexistente.

**Deslinde de duplicidad: los 303 AEI de El Rosario, Sinaloa.** El equipo 1-B lo trajo como reserva
fuera de ventana. Está registrado desde ARGOS 102 como `ARG-102-REC-001`. **No se reintegra.**

---

### El hallazgo que reorienta la pregunta: el fallo no es solo de cobertura, es de registro

La auditoría se encargó para averiguar **dónde empieza el fallo**. La respuesta no está donde se
esperaba, y es más incómoda: **en la ventana de ARGOS 95 hay un evento 🔴 que el propio ARGOS
localizó, verificó y clasificó como rojo hace seis ediciones — y que nunca llegó al producto.**

La secuencia consta documentada en el repositorio:

| Edición | Qué hizo con el ataque con dron de Aquila, Michoacán |
|---|---|
| **ARGOS 95** (12-ago) | No lo cubrió. Publica **«Corte sin eventos rojos»** |
| **ARGOS 96** (13-ago) | Lo detecta y lo señala como *posible vacío de cobertura* de ARGOS 95 |
| **ARGOS 97** (14-ago) | Lo **confirma** con ocho fuentes coincidentes, lo clasifica **🔴 ROJO** por uso de artefacto explosivo por dron con resultado de muerte, y lo archiva como *«constancia editorial para el archivo histórico»* |
| **ARGOS 98 a 103** | Nada. **Nunca recibió ARG-ID ni ficha** — verificado con `grep` sobre `indice-arg-id.md` |

Es un modo de fallo **distinto** del que ARGOS 103 diagnosticó. Aquel era de **búsqueda**: el hecho
no se encontraba. Este es de **registro**: el hecho se encontró, se verificó, se clasificó — y se
guardó en una nota metodológica en vez de en una ficha. El principio de no recalificación
retroactiva, que existe para impedir que un corte cambie el color de un hecho pasado, se aplicó de
más: se leyó como si prohibiera **publicar** el hecho, cuando solo prohíbe **recolorearlo**.

**No fue un caso aislado.** La misma auditoría de ARGOS 97 confirmó **seis vacíos** y detectó
**seis más** de forma incidental. De los confirmados, solo el de Huajicori llegó a producir un
ARG-ID (`ARG-98-FE-001`). Siguen sin registro, verificado con `grep`:

| Hecho confirmado por ARGOS 97 y nunca registrado | Ventana | Color |
|---|---|---|
| **Ataque con dron, La Estanzuela, Aquila, Michoacán** — 1 muerto, 1 herido | ARGOS 95 | **🔴** |
| **Quema de dos camiones de volteo**, Sabanillas, Tuxpan-Tamiahua, Veracruz | ARGOS 95 | 🟡 |
| **Homicidio de un tráilero**, carretera Nuevo Teapa–Cosoleacaque, Veracruz | ARGOS 95 | 🟡 |
| Detención de Gerardo Humberto Piña, **"El G1"**, Ensenada, Baja California | ARGOS 95/96 | 🟢 |
| Detención de Erick Jesús "N", **"El Loco"**, Metepec, Estado de México | ARGOS 94/95/96 | 🟢 |

Esta edición **publica como ficha el 🔴 de Aquila** (`ARG-104-REC-001`), que es lo que corresponde
hacer con un hecho de alto impacto, y **rectifica el conteo de ARGOS 95**. Los tres 🟡/🟢 no reciben
ficha en este cartelón —no son de alto impacto y su espacio le pertenece a los hechos del corte—
pero quedan inventariados aquí y en `_pendientes.md` para que dejen de ser invisibles.

### Ronda de corroboración (equipo 1-C) — 17 de 18 búsquedas

Tercera edición consecutiva que confirma su valor: **cerró una reserva abierta, fijó una ventana y
deslindó un falso positivo**, y en ningún caso se limitó a repetir lo que la primera ronda ya decía.

**Aquila — la fecha sigue sin arbitrarse, y esta vez se sabe por qué.** No es que falten fuentes:
es que **las fuentes se contradicen entre sí**. Un mismo resultado combina «tarde del martes 11» con
«miércoles por la mañana» en el mismo texto. Las dos únicas URLs con fecha en la ruta
(`medianews.mx/2026/08/12/`, `elmanana.com.mx/2026/8/12/`) llevan **fecha de publicación**, no del
hecho. Se declara `FECHA EN DISPUTA ENTRE FUENTES (11 o 12-ago) — NO ARBITRADA`. **La ventana de
origen no cambia por ello**: bajo cualquiera de las dos lecturas el hecho es anterior al cierre de
ARGOS 96, y las ediciones 96 y 97 ya lo habían situado en la ventana nominal de **ARGOS 95**.
Comunicado institucional: `SIN RESULTADO INDEXADO EN VENTANA`. **El peritaje está pendiente**: solo
consta que se aseguraron fragmentos metálicos «considerados posible metralla» para análisis, así que
el término se conserva literal —**artefacto explosivo presuntamente lanzado por dron**— y no se
escala a mina ni a granada.

**Buenavista — la hora sí queda fijada, y decide la ventana.** Fuentes independientes coinciden en
**~06:30 h del jueves 13-ago**, coherente con el calendario. La ventana de ARGOS 96 cierra ~07:00
CDMX de ese día: el hecho cae **dentro**, por media hora. **No es frontera de ventana**: la hora
está fijada por coincidencia entre fuentes, no inferida.

**Reserva cerrada: Ciudad Juárez, 14 rescatados y ocho detenidos.** El equipo 1-B lo dejó abierto
por falta de fecha. **El hecho es del 21 de julio de 2026**, con **boletín institucional propio** de
la SSPE de Chihuahua (`sspe.chihuahua.gob.mx`). **Fuera de ventana por tres semanas. Cerrado**, sin
reserva pendiente.

**Falso positivo deslindado: el boletín de la FGE de Baja California.** Al buscar la detención de
"El G1" en Ensenada apareció `fgebc.gob.mx/boletines/12637-…`, de título casi idéntico. **Es otro
caso**: enero de 2025, otro detenido, sin relación con el Cártel de Sinaloa. Es exactamente el fallo
de Coronango —un *slug* que se lee bien y describe otro caso— y confirma por qué se exigen **dos
campos individualizadores** para identificar un caso. La verificación de "El G1" queda **incompleta**,
no negativa: se descartó un homónimo, no se demostró que no exista boletín.

### Lo que la auditoría integra

| ARG-ID | Hecho | Ventana de origen | Color |
|---|---|---|---|
| `ARG-104-REC-001` | **Aquila, Michoacán** — artefacto explosivo presuntamente lanzado por dron sobre una vivienda en La Estanzuela; un adulto mayor muerto y un herido | **ARGOS 95** | **🔴** |
| `ARG-104-REC-002` | **Buenavista, Michoacán** — ataque armado contra una camioneta en la colonia Del Parque; muertas una mujer de 18 años y su bebé, una mujer mayor herida de gravedad | **ARGOS 96** | **🔴** |

Ninguno de los dos entra en los totales del corte de ARGOS 104, conforme a la regla del mando.

### Fe de erratas que producen

| ARG-ID | Edición | 🔴 publicado | 🔴 rectificado | Hecho que lo rectifica |
|---|---|---|---|---|
| `ARG-104-FE-001` | **ARGOS 95** | 0 — «Corte sin eventos rojos» | **1** | `ARG-104-REC-001` Aquila |
| `ARG-104-FE-002` | **ARGOS 96** | 1 | **2** | `ARG-104-REC-002` Buenavista |

### Categorías con resultado cero, declaradas y no supuestas

El equipo 1-B recorrió con vocabulario institucional y periodístico y **no localizó ningún hecho con
fecha verificable dentro del 11-15 de agosto** en: **motines carcelarios**, **hallazgo de fosas
clandestinas**, **ataques a infraestructura crítica**, **desapariciones múltiples como evento único**
y **secuestro masivo**. No es un `SIN DATO` por falta de barrido: es un cero con el barrido hecho.

### Señuelos y trampas de aniversario descartados en esta auditoría

| Candidato | Por qué no entra |
|---|---|
| **Salamanca, Guanajuato** — cinco muertos, dos adolescentes | Hecho del **21-jun-2026**. Reindexado por búsquedas de agosto |
| **Tzintzimeo, Álvaro Obregón, Michoacán** — ataque en velorio | Hecho del **11-jul-2026** |
| **Cereso de Ciudad Juárez** — «riña para implantar terror» | El hecho de fondo es de **11-ago-2022**; lo del 11-ago-2026 es una **audiencia** del juicio oral. Actividad judicial, no violencia colectiva |
| **Nuevo León** — «secuestro masivo de 17 personas» | Reindexado de **marzo-abril de 2024**. Lo único fechado en el corte es una **detención** |
| **Tazumbos, Jilotlán de los Dolores, Jalisco** — 11 AEI | Ya publicado como `ARG-97-ARM-002`. Coincide fecha, municipio, cantidad y tipo |
| **El Rosario, Sinaloa** — 303 AEI | Ya publicado como `ARG-102-REC-001` |
| **Pueblo Nuevo, Guanajuato** — depósito de cerveza, tres muertos | **15-ago, ~22:00 h**: posterior al cierre de ARGOS 98 (07:29). Fuera de las cuatro ventanas |
| **Irapuato, Guanajuato** — futbolistas, cuatro muertos | **19-ago**, fuera de ventana |
| **Tlapa de Comonfort, Guerrero** — cuatro muertos | **18-ago**, fuera de ventana |
| **Narcobloqueos de Michoacán** | **19-ago**: es `ARG-103-001`, ya publicado |

---

## Barrido regional — seis equipos, Ciclo A aplicado y declarado

### Rotación de cobertura — Ciclo A, con Colima por prioridad sobre el ciclo

Le tocaba el **Ciclo A**: **Noroeste y Centro encabezan el triaje judicial**; Noreste, Occidente,
Golfo y Sureste encabezan con armamento. Se aplicó, y **Colima encabezó el triaje de Occidente por
la regla de prioridad sobre el ciclo**, pese a que a Occidente le tocaba armamento.

**Qué aportó la rotación que el orden anterior no habría aportado.** La respuesta es literal y
comprobable: **la única sentencia integrable de las 32 entidades apareció en Durango**, la primera
entidad del triaje del Noroeste. Es la **segunda vez en la serie** —tras ARGOS 101, también en
Durango— que el resultado judicial del corte aparece exactamente donde la rotación mandó buscar
primero. El Centro, la otra región que encabezó el triaje judicial, cerró en cero integrable, de
modo que la rotación acertó en una de sus dos apuestas y **el rendimiento neto es positivo por
tercera edición**.

**Colima sale de `NO REVISADA` con hecho propio en ventana** —la detención de "El Pirul"— y con una
corrección de directorio que explica por qué llevaba tres ediciones sin aparecer.

### Cobertura por región

| Región | Entidades | Búsquedas | `NO REVISADA` | Aportación |
|---|---|---|---|---|
| **Noroeste** | 6 de 6 | 20/20 | 0 | **La única sentencia integrable** (Durango) · 3 aseguramientos nuevos (Sinaloa ×2, BC) · duplicidad interceptada |
| **Noreste** | 5 de 5 | 20/20 | 0 | **El único hecho 🟡** (Juchipila) · Ciudad Victoria · cierre propuesto del pendiente de Zacatecas |
| **Occidente** | 6 de 6 | 20/20 | 0 | **Colima saldada** · Aguascalientes y Nayarit **clasificados** · portal de Colima localizado |
| **Centro** | 7 de 7 | 20/20 | 0 | CDMX ("El Mayus") · avance de Coronango · **contaminación de Jiutepec detectada** |
| **Golfo** | 2 de 2 | 20/20 | 0 | **Doble consulta federal** · **Veracruz arbitrado** · cierre del pendiente del operativo de Michoacán |
| **Sureste** | 6 de 6 | 20/20 | 0 | Quintana Roo y Chiapas · **todo el armamento especial del corte** |

**32 de 32 entidades con barrido, ninguna `NO REVISADA`, y los seis topes respetados.** El Centro,
que en ARGOS 103 gastó 22 de 20, cerró esta vez en 20 exactas.

### El vacío federal era falso — tercera vez del mismo emisor

`_pendientes.md` traía **18, 19 y 20 de agosto sin boletín indexado**, declarado *con reserva
expresa* porque ARGOS 103 no pudo aplicar la doble consulta. **Se aplicó, y el vacío se cae.**

| Día | Resultado | Cómo se localizó |
|---|---|---|
| **18-ago** | **EXISTE** | URL canónica `gob.mx/sspc/prensa/…-18-de-agosto-de-2026`, más réplica en `laprensa.mx` |
| **19-ago** | **EXISTE** | **La URL canónica de `gob.mx` no se indexó**; se localizó en tres republicadores, uno con fecha en ruta (`eleese.com.mx/2026/08/20/`) |
| **20-ago** | `SIN RESULTADO INDEXADO EN VENTANA` | **Doble consulta aplicada** —día suelto y rango—. Se publicaría el 21-ago por la mañana. **Ya no se declara con reserva** |

**Es el tercer falso vacío consecutivo de este emisor, y la causa cambió.** Los dos primeros fueron
de **formato** —el emisor alternaba diario y agregado—. Este es de **indexación**: el boletín del
19-ago **existe y su portal no lo indexa**, de modo que solo aparece por sus republicadores. La
consecuencia práctica es que **consultar `site:gob.mx/sspc` no basta**, y hay que consultar también
por el título del boletín sin restricción de dominio. Tres equipos independientes —Golfo, Noroeste y
Sureste— llegaron a la misma conclusión por caminos distintos.

⚠️ **Un cuarto equipo, Occidente, no lo encontró** y, al no hallar la cadena literal, marcó como
`PENDIENTE DE ANCLA FECHADA` los renglones de Romita, Tlajomulco y Los Reyes de Salgado. **Su
cautela fue correcta y su conclusión, incompleta.** Se resolvió **no integrando** esos tres
renglones: apoyarlos en la lectura que otro equipo hizo del mismo boletín para otras entidades sería
la fusión que estos controles existen para impedir. Queda como pendiente.

### Ganancias para el directorio de dominios — `docs/dominios-oficiales.md` v1.2

1. **Colima sí tiene portal canónico, y no está en `.gob.mx`.** Es **`fgecolima.mx/boletines/<n>`**,
   más `col.gob.mx/Portal/detalle_noticia/<base64>`. El directorio lo daba por inexistente durante
   tres ediciones **porque se buscaba bajo el patrón `.gob.mx`**. Clase **C** (ID correlativo, sin
   fecha), con indexación pobre — que no es lo mismo que ausencia de portal.
2. **Aguascalientes y Nayarit dejan de estar `SIN CLASIFICAR`.** Ambos **clase C**. Nayarit es
   **la peor estructura del directorio**: querystring paginado, **sin URL propia por boletín**, de
   modo que no solo no se puede fechar, tampoco se puede citar un boletín concreto.
3. **Veracruz arbitrado — deuda de dos ediciones cerrada.** El mismo comunicado se publica en dos
   rutas y **la canónica es la fechada**: `veracruz.gob.mx/AAAA/MM/DD/<slug>/`. Probado con un par
   idéntico. Además, **`ssp.veracruz.gob.mx` no es un dominio**: la SSP cuelga de
   `veracruz.gob.mx/seguridad/`.
4. **`gabinetedeseguridad.gob.mx/contenido/<id>/` sí devuelve resultados indexados** y publica
   sentencias de la FGR. Sigue bloqueado al acceso directo: **no es un dominio muerto, es un dominio
   ilegible por acceso directo**.
5. **Tabasco cierra como clase C definitiva.** Once `id` distintos recuperados, **ninguno
   correlaciona con fecha**. Tercera edición que lo comprueba: dejar de sondear el patrón.
6. **Nuevas para el directorio**: `spsc.campeche.gob.mx` y `sspo.gob.mx` publican boletines propios
   indexados y no figuraban. Ambos clase C.
7. **Estado de México — precisión que cierra el intento de arbitraje.** No es un problema de
   variante: `fgjem.edomex.gob.mx` solo devuelve **PDF de 2019-2025** y `/prensa` **no está
   indexado**. **Arbitrar entre las dos direcciones no produciría un dato mejor.**

---

## Los hechos de la ventana

| ARG-ID | Hecho | Fecha | Color | Confianza |
|---|---|---|---|---|
| `ARG-104-001` | **Juchipila, Zacatecas** — agresión armada repelida durante cateos. 10 detenidos, **2 personas liberadas**, 1 arma larga, 60 cartuchos, 8 cargadores, **152 ponchallantas** | 20-ago | **🟡** | ★★★☆☆ |
| `ARG-104-002` | **Lázaro Cárdenas, Quintana Roo** — 4 cateos. 4 largas, 354 cartuchos, 15 cargadores, **2 granadas de fragmentación**, **1 aditamento lanzagranadas**, 2 narcoinvernaderos, 1 detenido | 19 o 20-ago | 🟢 | ★★★☆☆ |
| `ARG-104-003` | **Puerto Madero, Tapachula, Chiapas** — 4 detenidos de "Los Mayitos", **dos con órdenes judiciales en Guatemala**. 3 largas | 20-ago | 🟢 | ★★★☆☆ |
| `ARG-104-004` | **Álvaro Obregón, CDMX** — "El Mayus", presunto sicario **buscado por feminicidio**, detectado tras una riña de tránsito. 1 corta | 20-ago | 🟢 | ★★☆☆☆ |
| `ARG-104-005` | **Colima** — "El Pirul", Cártel de Los Mezcales, orden por homicidio calificado. **Sin armamento publicado** | 21-ago | 🟢 | ★★★☆☆ |
| `ARG-104-006` | **Mazatlán, Sinaloa** — La Angostura (6 largas, 5,675 cartuchos, 85 cargadores, **1 Barrett**) y Los Ébanos (3,290 cartuchos, 45 cargadores, **sin armas**) | 19-ago ⟶ | 🟢 | ★★★☆☆ |
| `ARG-104-007` | **Mexicali, Baja California** — 1 corta, 1 cargador, **120 kg de fentanilo** | 19-ago ⟶ | 🟢 | ★★★☆☆ |
| `ARG-104-008` | **Ciudad Victoria, Tamaulipas** — 7 largas, 340 cartuchos, 18 cargadores | 19-ago ⟶ | 🟢 | ★★★☆☆ |
| `ARG-104-SEN-001` | **Gómez Palacio, Durango** — 7 a 10 m por robo agravado, procedimiento abreviado. Multa $64,150.38, reparación $397,554.90 | pub. 20-ago | 🟢 | Medio |

`⟶` = `Evento anterior publicado durante el corte`.

### Reservas declaradas sobre los hechos de la ventana

- **`ARG-104-001` — la hora no está publicada.** Si el hecho fue anterior a las 08:16 quedaría fuera
  de ventana. **ARGOS 103 cerró a esa hora sin recogerlo**, lo que respalda su ubicación aquí, pero
  no es concluyente. Además, el **número de liberados está contradicho dentro de la misma fuente**:
  el boletín estatal y el *slug* dicen **2**, el titular dice **1**. Se publica **2** con la salvedad.
- **`ARG-104-002` — `FRONTERA DE VENTANA`.** El hecho es del 19 o del 20; la publicación es del 20.
  Se integra en la edición que lo ve primero, con la marca, que es permanente.
- **`ARG-104-003` — desglose contradicho.** Dos lecturas incompatibles de la misma fuente
  institucional: **0 cortas y 172 cartuchos** frente a **4 cortas y 322 cartuchos**. Solo se integran
  las **3 largas y los 4 detenidos**, coincidentes en las tres fuentes. No se promedia ni se elige la
  más repetida.
- **`ARG-104-006` — el Barrett no se suma.** `NO DETERMINABLE SI ESTÁ COMPRENDIDO EN LAS SEIS
  LARGAS`. Mismo criterio que `ARG-103-ARM-001`.
- **Corroboración débil por construcción en los cuatro hechos del 19-ago**: los tres republicadores
  reproducen **el mismo boletín**, no son fuentes independientes. Se declara.

### Hechos examinados que NO reciben ficha

| Hecho | Por qué |
|---|---|
| **Veracruz — bloque de hechos graves** (cuerpo desmembrado en Coatzintla, cabeza humana en Poza Rica, normalista asesinada en Tuxpan) | ⚠️ **El descarte mejor razonado del corte.** La fuente es un **agregador sin fecha en ruta** (`vernota.php?id=`), el "20 de agosto" procede **solo del resumidor**, y el **mismo bloque de hechos aparece casi idéntico en resultados del 25 y 26 de junio de 2026**. Riesgo alto de recirculación. **Si otro equipo lo fecha en ventana con URL fechada, sería 🔴.** `PENDIENTE DE ANCLA FECHADA` |
| **Coahuila — enfrentamiento en la brecha Rancherías, Hidalgo** | Ninguna de las tres URLs lleva día; cantidades no publicadas. Sería 🟡 si se fechara. **No integra** |
| **Chiapas — Mapastepec**, dos detenidos tras disparar contra policía estatal | Ruta *hash* sin fecha (`ssp.chiapas.gob.mx/noticias/J5Iqvh…`). Candidato 🟡 **sin ancla fechada** |
| **Guanajuato, Jalisco y Michoacán** en el boletín del 19-ago (Romita · Tlajomulco · Los Reyes de Salgado, 5 largas y 5 cargadores) | `PENDIENTE DE ANCLA FECHADA`. Ver la reserva del barrido federal |
| **La Paz, BCS** — 4 detenidos, 2 personas rescatadas | El resumidor **mezcló dos boletines distintos**: las listas de estados de sus dos respuestas no coinciden. **No asignable** |
| **Huachicol — Rigoberto Blanco Cantú se entrega en EU** (`jornada.com.mx/2026/08/20/`) | Publicación en ventana, pero **hecho en el extranjero y no es aseguramiento ni sentencia**. Se cita en el Análisis ARGOS como movimiento del seguimiento abierto desde ARGOS 96; **no aporta línea a ningún conteo** |

---

## Presupuesto de búsqueda

| Equipo | Tope | Consumo |
|---|---|---|
| 1-A Masacres y homicidios múltiples | 20 | 20 |
| 1-B Violencia colectiva | 20 | 20 |
| 1-C Ronda de corroboración | 18 | 17 |
| Barrido Noroeste | 20 | 20 |
| Barrido Noreste | 20 | 20 |
| Barrido Occidente | 20 | 20 |
| Barrido Centro | 20 | 20 |
| Barrido Golfo + doble consulta federal | 20 | 20 |
| Barrido Sureste | 20 | 20 |
| **TOTAL** | **198** | **177** |

**Nueve de nueve topes respetados** — se restaura la racha que ARGOS 103 rompió, y el equipo que la
rompió (Centro) cerró esta vez en 20 exactas.

**Reparto**: **57 búsquedas (32%) a la auditoría** y **120 (68%) a cubrir el país**. En ARGOS 103 la
proporción fue del 38% a auditar, y costó Colima y el módulo de sentencias. **Este corte no pagó ese
precio**: 32 de 32 entidades revisadas, Colima saldada y una sentencia integrable.

---

## Valoración del corte

### Nivel de Riesgo Nacional ARGOS: sin eventos rojos localizados, nivel bajo con reserva expresa

El barrido cubrió **32 de 32 entidades** sin ninguna en casilla `NO REVISADA` y **no localizó un
solo hecho de alto impacto** con fecha fijada dentro de la ventana. El único hecho con confrontación
armada —Juchipila— es **🟡** porque **la autoridad inició la acción**, conforme al criterio de quién
inicia; las siete acciones institucionales **no reducen el nivel de riesgo**.

**Por qué no se declara `NO DETERMINABLE`, y por qué tampoco se declara un cero limpio.** Las dos
opciones que la serie ha usado son insatisfactorias por razones opuestas. `NO DETERMINABLE` fue la
fórmula de ARGOS 100 y 101, y **esta misma edición acaba de rectificar las dos**: era una abstención
que ocultaba una cobertura fallida. Pero un cero limpio afirmaría más de lo que se puede sostener,
porque el segmento que este producto pierde de forma sistemática —**violencia contra civiles sin
comunicado institucional**— es exactamente el que no puede darse por vacío.

La formulación elegida separa lo que consta de lo que no: **cero rojos localizados con el barrido
completo hecho y declarado**, más la reserva de que **«no se localizó» nunca significa «no
ocurrió»**. La diferencia entre ambas cosas ya no es una hipótesis del producto: **está acreditada
siete veces** —tres en ARGOS 103, dos en ARGOS 104, más los dos de Veracruz inventariados sin ficha—.

### Advertencia obligatoria de comparabilidad

Los totales de este corte **no son comparables sin más** con los de ediciones anteriores:
**cuatro de los siete eventos verdes son hechos del 19-ago** publicados dentro de la ventana, y
`ARG-104-ARM-002` está marcado `FRONTERA DE VENTANA`. Además, **cinco ediciones tienen ya su conteo
de 🔴 rectificado** —95, 96, 99, 100 y 101—: cualquier serie temporal construida sobre sus
valoraciones originales está viciada, y debe reconstruirse con las rectificadas.

---

## Lecciones de método de esta edición

1. **El índice responde "¿tiene ARG-ID?", no "¿ARGOS ya sabía esto?".** El hallazgo mayor del corte
   —el 🔴 de Aquila— **no estaba en `indice-arg-id.md`**: estaba en el cuerpo de dos archivos de
   fuentes, como nota de método. Un `grep` sobre el índice lo habría declarado inédito; un `grep`
   sobre todo el repositorio reveló que **el producto lo sabía desde hacía seis ediciones**. La
   comprobación de duplicidad debe hacerse **sobre el repositorio entero**, no sobre el índice.
2. **El principio de no recalificación retroactiva se estaba aplicando de más.** Prohíbe **cambiar el
   color** de un hecho pasado; no prohíbe **publicarlo**. ARGOS 97 leyó la regla como si le impidiera
   abrir ficha, y archivó un 🔴 confirmado como "constancia editorial para el archivo histórico".
   **Una regla que existe para proteger la integridad del archivo terminó impidiendo que el archivo
   se completara.**
3. **La contradicción no siempre está entre fuentes.** En Juchipila, el **titular y el *slug* del
   mismo medio** dan cifras distintas de personas liberadas, y el *slug* coincide con el boletín
   oficial. Comprobar la coherencia interna de una fuente **incluye comparar sus propios campos**.
4. **Que un portal no indexe su propio boletín no significa que el boletín no exista.** El del
   19-ago solo aparece por republicadores. La regla de la doble consulta era insuficiente y **queda
   ampliada a tres formas en `CLAUDE.md`**.
5. **Un equipo que no encuentra lo que otros sí puede estar señalando la causa.** Occidente no
   localizó el boletín del 19-ago y marcó sus renglones como no anclados. Su conclusión era
   incompleta y **su cautela, correcta**: se resolvió **no integrando** esos renglones, porque
   apoyarlos en la lectura que otro equipo hizo del mismo boletín para otras entidades habría sido
   la fusión que estos controles existen para impedir.
6. **Rendimiento de la rotación, tercera medición consecutiva.** Ciclo A: la única sentencia
   integrable apareció en **Durango**, primera entidad del triaje del Noroeste — igual que en
   ARGOS 101. El Centro, la otra región que encabezó el triaje judicial, cerró en cero. **Una de dos
   apuestas acertadas, con saldo neto positivo.**
7. **El reparto del presupuesto se corrigió solo.** ARGOS 103 gastó el **38%** en auditarse y le
   costó Colima y el módulo de sentencias. ARGOS 104 gastó el **32%** y cerró con **32 de 32
   entidades, Colima saldada y una sentencia integrable**. La auditoría no tiene por qué pagarse con
   cobertura.

