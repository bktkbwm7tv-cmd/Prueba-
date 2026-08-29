# ARGOS 111 — Archivo de fuentes y trazabilidad

**Corte**: 2026-08-29 · **Ventana**: 2026-08-28 06:25 CDMX → 2026-08-29 09:05 CDMX (~26 h 40 min)
**Hora de arranque verificada**: `TZ=America/Mexico_City date` → `2026-08-29 09:05 CST`
**Continuidad**: abre exactamente donde cerró ARGOS 110 (2026-08-28 06:25 CDMX). Sin hueco ni solape.

---

## 0. Verificación de base (Bloque 0 del arranque)

| Comprobación | Resultado |
|---|---|
| `git merge --ff-only origin/main` | **Fast-forward limpio**, ejecutado como primer comando de la sesión, antes de leer `CLAUDE.md` |
| Última edición en el archivo | `argos-2026-08-28` (**ARGOS 110**) ✅ coincide con lo previsto |
| Archivos en `reports/` | **75** ✅ coincide con lo previsto |
| `main` contiene ARGOS 110 | ✅ `ffcdda1 Generar ARGOS 110 (corte 2026-08-28)` |
| Numeración | **ARGOS 111**, deducida del archivo, no de la rama |

⚠️ **La rama asignada volvió a llegar desactualizada** — quinta edición consecutiva. Mostraba `argos-2026-08-24` como última edición y **no contenía su propio archivo de arranque**. Numerar por lo que la rama tenía a la vista habría producido un falso ARGOS 107 con ventana solapada. El `ff-only` como primer comando lo evitó, exactamente como el arranque predijo.

---

## 1. Estado del egreso — vigesimotercera edición

Verificado **en esta sesión**, no heredado:

```
gob.mx                             403
www.gob.mx                         (sin respuesta)
gabinetedeseguridad.gob.mx         (sin respuesta)
fiscaliasinaloa.mx                 (sin respuesta)
seguridadbc.gob.mx                 (sin respuesta)
https://www.gob.mx/sspc            curl: (56) CONNECT tunnel failed, response 403
```

`WebFetch` contra `eleese.com.mx` devolvió `EGRESS_BLOCKED`. **Cero portales leídos por acceso directo.**
**Techo de confianza del producto: ★★★★☆.** Ninguna ficha lleva ★★★★★.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.

---

## 2. Rotación de cobertura — **CICLO A**, declarado y aplicado

**Ciclo A — Noroeste + Centro encabezan el triaje judicial.** Las otras cuatro regiones encabezaron con armamento.

⚠️ **Arbitraje de la prioridad sobre el ciclo.** La deuda de dominio de SSP —Baja California y BCS, ambas en el **Noroeste**; Tlaxcala y SLP, en el **Centro**— recaía precisamente sobre las dos regiones que este ciclo encabezan judicial. **Se resolvió sin romper el ciclo**: se ordenó a ambas gastar sus **primeras búsquedas en el arbitraje de dominio** y solo después encabezar el triaje judicial. La prioridad se saldó primero y el turno se conservó.

**Qué aportó la rotación que el orden anterior no habría aportado:**

- **El Noroeste encabezando judicial produjo la única sentencia integrable del corte** (`ARG-111-SEN-001`, FGED Durango, URL con fecha en la ruta). **Es la segunda vez que ocurre exactamente esto**: en ARGOS 101, la única sentencia integrable del corte también apareció en Durango al mandar a esa región a encabezar. No es cobertura cosmética: cambia lo que el producto encuentra.
- El **arbitraje de dominio** cerró tres ambigüedades (§4) que llevaban cuatro ediciones abiertas.

---

## 3. Reparto de presupuesto y origen de los hechos

**Seis agentes `barrido-regional` en paralelo** (autorizados por el destinatario), lanzados en un solo mensaje antes de ningún otro encargo. Presupuesto: 18 búsquedas por región, 14 en Golfo (dos entidades). **Las seis declararon su desviación.**

| Región | Búsquedas | Reparto genérico | Desviación declarada |
|---|---|---|---|
| Noroeste | 18/18 | 61 % | Ninguna. Eje Escuinapa cerrado exactamente en 3 |
| Noreste | 18/18 | 100 % genérico | **+1 en el eje de Zacatecas** (5 en vez de 4), por la contradicción institucional de lesionados. Se descontó de Coahuila y Nuevo León |
| Centro | 18/18 | ~39 % | Ninguna. **Eje «El Dron» cerrado en 2, tope respetado** |
| Occidente | 18/18 | 56 % | Ninguna. Los tres ejes gastaron 1 búsqueda cada uno, por debajo de su tope |
| Golfo | 14/14 | 57 % | **+1** en verificar dos trampas geográficas no previstas. Dejó `fiscaliatabasco.gob.mx` `NO REVISADA` |
| Sureste | 18/18 | 44 % | **−16 puntos en armamento**: los tres seguimientos agotaron sus topes duros (6 búsquedas) |

**El tope duro funcionó.** En ARGOS 110 un solo eje consumió 9 de las 18 búsquedas del Centro sin producir un dato. Esta edición **ningún eje pasó de 5**, y el Centro cerró el suyo en 2. El precio fue cerrar tres seguimientos en `SIN AVANCE` — que es el resultado correcto cuando no hay dato, no un fallo.

### Origen de los hechos publicados

| Origen | ARGOS 109 | ARGOS 110 | **ARGOS 111** |
|---|---|---|---|
| Barridos regionales | 4 de 6 | 2 de 4 | **4 de 6** |
| Recall nacional del coordinador | 2 de 6 | 2 de 4 | **2 de 6** |

**El recall nacional se ejecutó ANTES de cerrar ningún barrido**, como exige el arranque. Aportó:
1. **`ARG-111-REC-001` (Petatlán)** — hecho de 4 muertos que **ninguna región vio a tiempo de fecharlo**: el Sureste lo trajo «sin ancla de fecha localizada» y el recall ya lo tenía anclado por coherencia de día de la semana.
2. **La existencia del boletín federal del 27-ago**, que produce la fe de erratas `ARG-111-FE-001`.
3. **Interceptó un falso positivo grave**: el Sureste trajo *Cerro de las Lumbreras, San Miguel Totolapan* como «hecho nuevo de alto impacto por fechar». **Ya estaba publicado como `ARG-110-REC-001`.** Sin el `grep` del índice se habría publicado dos veces, con dos ARG-ID.

---

## 4. Barrido de portales — resultado del arbitraje de dominio

**La deuda ya no era de descubrimiento sino de arbitraje, y así se atacó.**

### Resueltos en esta edición

| Entidad | Arbitraje | Resultado |
|---|---|---|
| **Baja California** | `seguridadbc.gob.mx` vs `sspbc.gob.mx` | ✅ **`seguridadbc.gob.mx` es el que sirve boletines**, con estructura `boletin_<Mes>.php` y meses ENERO–JULIO 2026 indexados. **Agosto no está indexado** → `SIN RESULTADO INDEXADO EN VENTANA` |
| **Baja California Sur** | `sspbcs.gob.mx` vs `ssbcs.gob.mx` | ✅ **`sspbcs.gob.mx` es el dominio activo** (Policía Estatal Preventiva, C4 La Paz, manuales 2026). Sin boletín de agosto indexado |
| **Chihuahua** | `sspe.chihuahua.gob.mx` | ✅ **Confirmado y por primera vez INTERROGADO AL PERIODO**: publica (3, 10, 12 y 24-ago indexados), pero **nada del 28-29** |
| **Estado de México** | dominio de la fiscalía | ✅ **`fgjem.edomex.gob.mx`** — `fgjestadodemexico.gob.mx` y `fgjedomex.gob.mx` no resuelven contenido. Hallazgo nuevo |

### No resueltos — se declaran, no se disimulan

| Entidad | Estado |
|---|---|
| **Tlaxcala** | ⚠️ **SIGUE SIN ARBITRAR.** Ni `ssc.tlaxcala.gob.mx` ni `ssctlaxcala.gob.mx` devolvieron boletines fechados indexados: **no pudo determinarse cuál sirve boletines**. Queda tan abierto como antes |
| **San Luis Potosí** | ⚠️ `NO REVISADA`. El Noreste gastó su margen en el eje de Zacatecas. Tres candidatos siguen sin arbitrar |
| **`fecc.fgjtlaxcala.gob.mx`** | ✅ **CONSULTADO** — `SIN RESULTADO INDEXADO EN VENTANA`. Se salda tras **dos ediciones** en `NO REVISADA` |

### ⚠️ Anomalía de portal — Nayarit

`site:ssypc.nayarit.gob.mx` devolvió **como único resultado indexado** una página titulada **«HOKIJP168: SiTus ToTo Link Togel Online»** — contenido de apuestas, ajeno por completo a la Secretaría de Seguridad. El dominio fue confirmado en ARGOS 109 y **nunca se había interrogado por `site:`**; al hacerlo por primera vez aparece esto.

Se registra como **`PORTAL NO DISPONIBLE — contenido no oficial en el índice`**, nunca como «sin actualización». Hipótesis abiertas: dominio expirado, secuestro de dominio o error de indexación. **No se usó ninguna cifra procedente de ese dominio.** Verificar por consulta genérica antes de reintentarlo.

### Cobertura declarada — las tres casillas

- **`SIN ACTUALIZACIÓN CONSTATADA`: 0 portales.** Requiere lectura directa del listado, imposible con el egreso bloqueado. **Ninguna región usó esta casilla**, correctamente.
- **`SIN RESULTADO INDEXADO EN VENTANA`**: la casilla correcta en casi todos los casos.
- **`NO REVISADA`**: SLP (arbitraje), `fiscaliatabasco.gob.mx`, SSP de Querétaro, portales propios de SSP/Fiscalía de Campeche, Yucatán y Quintana Roo, `fiscaliamichoacan.gob.mx`, `fgecolima.mx`, `fiscaliageneral.nayarit.gob.mx`, fiscalías de Jalisco y Guanajuato, IESPA Aguascalientes, y **SEDENA / SEMAR / FGR / ANAM regionales y Mesas de Construcción de la Paz en casi todas las regiones** — quinta edición consecutiva.
- **`HEREDADO — NO REVERIFICADO`**: `seguridad.durango.gob.mx/seccion/boletines/`.

**Entidades con al menos una consulta: 32 de 32.** **Entidades con cobertura de portal completa (SSP + Fiscalía + Policía Estatal + Mesa de Paz): 0.** Se declara así y no como cobertura total.

### Portales que publicaron en ventana

**Uno solo: `fiscalia.durango.gob.mx`** (`/2026/08/28/`). Corrige el dato que ARGOS 110 dejó a vigilar: aquella edición fue la primera reciente **sin un solo portal institucional publicando en ventana**; esta recupera uno. **El problema es la ventana corta, no solo el bloqueo** — con ~26 h, un único portal de 32 entidades es el orden de magnitud esperable.

---

## 5. La triple consulta del boletín federal

Ejecutada **en las tres formas**, como exige la regla:

1. **Día suelto** — «acciones relevantes del 28 de agosto de 2026»: sin resultado.
2. **Rango o agregado** — «del 28, 29…»: sin resultado.
3. **Título sin restricción de dominio**: sin resultado para el 28.

→ **El boletín del 28-ago no está indexado en ninguna de las tres formas.** `SIN RESULTADO INDEXADO EN VENTANA`. Es coherente con el horario habitual de publicación del emisor, posterior al cierre de esta ventana.

**Pero la tercera forma sí localizó el boletín del 27-ago** (publicado el 28, dentro del corte), invisible por `site:gob.mx/sspc`, alcanzable solo por republicadores: `eleese.com.mx/2026/08/28/…` y `tallapolitica.com.mx`. **Ver `ARG-111-FE-001`.**

⚠️ **Sustitución anotada y corroboración débil por construcción**: dos republicadores del mismo boletín **no son fuentes independientes**. Todo el bloque «publicado durante el corte» descansa en esa base y así se declara.

---

## 6. Fichas del corte

### `ARG-111-001` — Culiacán, Sinaloa · fraccionamiento Montebello · 🔴
**Hecho**: viernes 28-ago por la mañana. Sujetos a bordo de dos vehículos dispararon con armas largas contra la fachada de un edificio de departamentos de cuatro niveles y embistieron el portón principal con un vehículo con reporte de robo, que quedó encajado en el acceso. Incendiaron el inmueble con residentes dentro. Bomberos de Culiacán rescataron con escala telescópica a **cinco personas: tres menores y dos mujeres**, todas ilesas. Peritos de la FGE Sinaloa acordonaron y recolectaron casquillos.
**Corroboración**: institucional por cita (FGE Sinaloa, Bomberos de Culiacán) + `redmetropolitana.com.mx/2026/08/28/` + `capitalmexico.com.mx` + `nmas.com.mx` + `quadratin.com.mx` + `acontecersanluis.wordpress.com/2026/08/28/`.
**Color**: 🔴 por **terror contra población civil** — ataque armado e incendio deliberado contra inmueble habitado, con menores atrapados. El color lo fija el **tipo de evento**, no el saldo: que no haya muertos no lo baja de categoría.
**Reservas**: «más de 100 casquillos» **no es cifra** y no se cuenta. **La hora no se publica con fragmento citable**: `FRONTERA DE VENTANA — HORA NO FIJADA`. Se integra a la edición que lo ve primero.
⚠️ **Deslinde**: `cafenegroportal.com` publica además «Ataque a balazos deja **dos heridos** y **casa** quemada en Montebello» — **casa**, no edificio, y **2 heridos** frente a residentes ilesos. **Son dos hechos, no uno.** No se funden.
**Trazabilidad**: `ARG-111-001` · Confianza 🟡 Medio · ★★★★☆ · Consulta 2026-08-29 09:05 CDMX

### `ARG-111-002` — Escuinapa, Sinaloa · zona rural (Huerta Quevedo) · 🟢
**Hecho**: 28-ago. El Grupo Interinstitucional (Policía Municipal de Escuinapa, Policía Estatal y Fuerzas Armadas) detuvo a **3 personas** —una de nacionalidad estadounidense— en dos intervenciones en zona rural, tras reportes de detonaciones. Aseguró **5 armas largas cal. 7.62×39, 700 cartuchos, 26 cargadores, 4 chalecos tácticos y 8 placas balísticas**. Puestos a disposición de la FGR, delegación Mazatlán.
**Corroboración**: `vivalanoticia.mx/2026/08/28`, `fuentesfidedignas.com.mx/2026/08/28/`, `puntualizando.com`. Sin comunicado oficial leído — **Pendiente de corroboración institucional directa.**
⚠️ **Deslinde obligatorio**: **no es `ARG-110-002`.** Aquél es el 27-ago (5 muertos, 7 detenidos por el Ejército, 7 placas balísticas); éste es el 28-ago, otra corporación, 3 detenidos, 8 placas. Día distinto, saldo distinto, corporación distinta.
**Trazabilidad**: `ARG-111-002` · Confianza 🟡 Medio · ★★★☆☆ · Consulta 2026-08-29 09:05 CDMX

### `ARG-111-003` — Concordia, Sinaloa · «Operación Sable» · 🟢
**Hecho**: viernes 28-ago. La SEMAR, en coordinación con FGR y SSPC, localizó y **destruyó por detonación controlada 49 artefactos explosivos improvisados**, mediante trabajo de inteligencia, patrullaje terrestre y reconocimiento aéreo. Aseguró además **5 armas de fuego sin clasificación publicada, 55 cargadores y 3 vehículos**, droga y equipo táctico sin cifra. **Sin detenidos publicados.**
**Corroboración**: `razon.com.mx/2026/08/28/`, `publimetro.com.mx/2026/08/28/`, `eldiariodechihuahua.mx/2026/aug/28/`, `cronica.com.mx/2026/08/28/`, `miguelangelluna.mx/2026/08/28/`, `lopezdoriga.com`.
**Reservas**: «más de 2,800 cartuchos» **no es cifra** y no se integra. Las 5 armas **no se reparten** entre cortas y largas: la autoridad no las clasificó.
**Trazabilidad**: `ARG-111-003` · Confianza 🟡 Medio · ★★★★☆ · Consulta 2026-08-29 09:05 CDMX

### `ARG-111-004` — Chihuahua, Chihuahua · calle Altos de la Parra · 🟡
**Hecho**: noche del 28-ago. Sujetos a bordo de una motocicleta dispararon varias veces contra un domicilio. **Sin lesionados**; solo daños materiales.
**Reserva decisiva**: la fuente describe el domicilio como **«presuntamente habitado por un agente estatal»**. **«Presuntamente» no acredita adscripción**, y de ese dato depende el color: si se confirmara que el ocupante es personal de seguridad, el hecho sería un **ataque contra autoridad → 🔴**. **Mientras no se acredite, se clasifica 🟡 y se declara la reserva**, conforme a la regla de no inflar el nivel de riesgo con hechos no acreditados.
**Corroboración**: `eldiariochihuahua.mx/2026/aug/28/`. **Fuente única — Pendiente de corroboración independiente.**
**Trazabilidad**: `ARG-111-004` · Confianza 🟠 Bajo · ★★☆☆☆ · Consulta 2026-08-29 09:05 CDMX

### `ARG-111-SEN-001` — FGED Durango · Región Laguna · 🟢
**Resolución**: **sentencia condenatoria** contra **Víctor Hugo Camacho Vázquez** por **robo agravado y daños**: **más de 10 años 8 meses** de prisión.
**Fuente oficial**: `fiscalia.durango.gob.mx/2026/08/28/fged-obtiene-sentencia-condenatoria-por-mas-de-10-anos-para-responsable-de-robo-agravado-y-danos-en-la-region-laguna/` — ***slug* institucional con el término jurídico literal y fecha en la ruta**, el respaldo más fuerte de la escala.
**Firmeza**: no informada. No se asume.
**Base de la decisión de integrarla**: la regla del *slug* institucional de `CLAUDE.md` —«para clasificar un caso como sentencia, el término en el *slug* institucional basta»— la sostiene. El barrido la propuso como `PENDIENTE DE CONFIRMACIÓN OFICIAL` por no haber podido leer el cuerpo; **se arbitró en contra de esa propuesta**: con el egreso bloqueado, exigir lectura del cuerpo haría inalcanzable *toda* sentencia de forma permanente, y la regla existe precisamente para ese supuesto. La pena se publica **como la publica el emisor** («más de 10 años 8 meses»), sin redondear ni precisar lo que la fuente no precisa.
**Trazabilidad**: `ARG-111-SEN-001` · Confianza 🟡 Medio · ★★★★☆ · Consulta 2026-08-29 09:05 CDMX

### `ARG-111-REC-001` — Petatlán, Guerrero · Las Mesas del Parotal · 🔴 · **RECUPERACIÓN**
**Hecho**: presuntos integrantes de **La Familia Michoacana** irrumpieron en la localidad; **los pobladores los enfrentaron y mataron a cuatro**. El enfrentamiento comenzó la **tarde del miércoles 26-ago** y se prolongó hasta la **madrugada del jueves 27**.
**Ventana de origen declarada**: **ARGOS 109** (26-ago 14:21 → 27-ago 10:00 CDMX). **Fuera de todos los totales de ARGOS 111** — no entra en el semáforo, ni en el radar, ni en el mapa.
**Por qué se publica aquí**: **ninguna edición de la serie lo registra**. `grep` de «Petatlán» y «Parotal» sobre todo `reports/` devuelve cero.
**Anclaje**: coherencia de día de la semana verificada contra calendario — 26-ago-2026 **es** miércoles y 27-ago **es** jueves. La atribución de la fuente es interna y externamente coherente.
**Corroboración**: `guerrero.quadratin.com.mx`, `quadratin.com.mx`. **Sin fuente institucional** — Pendiente de corroboración oficial.
⚠️ **Deslinde**: **no es `ARG-110-REC-001`** (Cerro de las Lumbreras, San Miguel Totolapan, 6 muertos, «Los Tlacos»). Otro municipio, otra organización, otro saldo.
**Trazabilidad**: `ARG-111-REC-001` · Confianza 🟠 Bajo · ★★★☆☆ · Consulta 2026-08-29 09:05 CDMX

---

## 7. Candidatos que NO se integran

| Candidato | Motivo |
|---|---|
| **Zacatecas · municipio de Tabasco — 11 detenidos, 10 armas largas, «más de 20 cargadores», chalecos y placas, uniformes falsos, 1 vehículo robado** | Publicado por `zacatecas.gob.mx` —**fuente institucional**— pero **SIN FECHA EN LA RUTA**. El resumidor llegó a fecharlo en «octubre de 2025», lo que confirma que no se puede fiar de él. `SIN ANCLA FECHADA — NO INTEGRAR AL TOTAL`. «Más de 20 cargadores» tampoco es cifra. **Es el candidato de mayor valor del corte y se queda fuera por un campo que la autoridad no publica** |
| **Veracruz · agregado de la FGE** (`lapoliticaenrosa.com/2026/08/28/`) | **Cuarto agregado consecutivo sin desglose.** URL fechada dentro de ventana, pero sin individualización. `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL`. Se alcanzó por primera vez el dominio primario `comunicacion.fiscaliaveracruz.gob.mx`, pero **sin fecha en la ruta y sin individualización** |
| **Oaxaca · «14 cateos ASAEO, 9 detenidos»** frente a «21 cateos, 10 detenidos» del boletín federal, mismo 27-ago | `POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN` |
| **Veracruz · San Andrés Tuxtla** (3 cortas, 1 larga, 43 cartuchos, 7 cargadores, 6 detenidos, 2 liberados), del boletín federal del 27-ago | **EXCLUIDO POR DUPLICIDAD**: coincide con **`ARG-108-004`** —San Andrés Tuxtla, 6 detenidos tras la corrección de ARGOS 109, rescate de persona privada de la libertad—. **No se recuenta.** Es el mismo hecho llegando por segunda vía |
| **Oaxaca · Istmo de Tehuantepec** — hombre con orden de aprehensión dispara contra agentes de la FGE | Sin fecha fijada y sin saldo. No integrado |
| **Sinaloa · 7 homicidios del jueves 27-ago** (Culiacán, Mazatlán, Escuinapa) | Fuera de ventana |
| **Guerrero · Cerro de las Lumbreras / San Miguel Totolapan** | **YA PUBLICADO** como `ARG-110-REC-001`. Un barrido lo trajo como hecho nuevo; el `grep` del índice lo interceptó |

---

## 8. Fes de erratas — **NO PUBLICADAS EN EL CARTELÓN**

Conforme a la instrucción editorial permanente: van a este archivo y a `_pendientes.md`; el ARG-ID se registra en `indice-arg-id.md`; **ninguna abre página, sección ni ficha en el cartelón**.

### `ARG-111-FE-001` — El boletín federal del 27-ago **SÍ existe**
ARGOS 110 escribió: «**Se confirma que no existe boletín del 27-ago con URL verificable**» (`ARG-110-FE-001`). **Es falso.** El boletín existe y es alcanzable por republicadores con fecha en la ruta: `eleese.com.mx/2026/08/28/el-gabinete-de-seguridad-…-del-27-de-agosto-de-2026/` y `tallapolitica.com.mx`.

⚠️ **Es el mismo modo de fallo, por segunda edición consecutiva, y sobre el emisor que ya lo había producido.** ARGOS 110 corrigió el falso vacío del 26-ago **y en el mismo movimiento creó el del 27**. La causa es idéntica: `gob.mx` no indexa el documento, y una búsqueda con `site:` no lo alcanza en ninguna de sus dos primeras formas.

**Lección que sí es nueva**: la tercera forma de la triple consulta **no basta con estar escrita, hay que ejecutarla sobre cada día declarado vacío, no solo sobre el día que se está investigando**. ARGOS 110 la aplicó al 26 y no al 27.

### `ARG-111-FE-002` — `ARG-110-SEN-C02` (Piedras Negras) se **retira** por umbral
Raúl «N», tráfico de 26 personas extranjeras, 9 años 7 meses 6 días y multa de 6,000 UMA. **Tercera edición consecutiva sin una sola URL con fecha en la ruta**, pese a cuatro fuentes nacionales y a una consulta más en esta edición que aportó detalle (colonia Las Cumbres, vehículo tipo Urban, procedimiento abreviado) pero **ningún ancla temporal**.

El umbral de fe de erratas es de **dos** ediciones. Se rebasó. **Se retira del acumulado y se marca `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`.** No vuelve a listarse como candidato. *Señalar un problema sin resolverlo, edición tras edición, no es trazabilidad.*
(Se conserva el deslinde: no se funde con el caso homónimo de 12 años del mismo delito en Coahuila.)

### `ARG-111-FE-003` — `ARG-109-004`: la contradicción de «la Tripa» **queda deslindada**
`diariocambio.com.mx` atribuía un operativo en Cholula a «la Tripa», del «comando Tlahuica», y se sospechaba confusión de dos operativos. **No hay confusión: son dos hechos distintos.** La detención de «la Tripa» (Homero «N», Comando Tlahuica) es de **junio de 2026 en San Pedro Cholula**; la de «El Dron» es del **26-ago-2026 en San Bernardino Tlaxcalancingo, San Andrés Cholula**. Municipios contiguos de la misma zona conurbada, separados por más de dos meses. **Contradicción cerrada.**

### `ARG-111-FE-004` — `ARG-109-004`: se retira la contradicción (a)
No existe fuente indexada que sostenga «otro sospechoso referido como El Dron sigue prófugo». Las fuentes identifican consistentemente a **Jesús Alberto Hidalgo Iribe** como «El Dron», detenido y herido el 26-ago, y al **segundo tirador como prófugo sin ese alias**. **La formulación se retira** de la tabla de contradicciones; queda solo «segundo tirador prófugo, identidad no publicada».

### `ARG-111-FE-005` — atribución de fecha corregida antes de publicar
El renglón **«Tabasco · Villahermosa, 2 armas largas, 6 detenidos»** **no pertenece al boletín
federal del 27-ago** sino al del **26 de agosto**. Detectado por `procedencia-cifras` en dos consultas
independientes y **retirado de la línea inferior antes de publicar**. Es la «trampa de mes/día» del
`CLAUDE.md` operando dentro de un mismo boletín agregado por republicadores.

---

## 9. Seguimientos — resultado, eje por eje

### Eje 1 · Zacatecas, los seis AEI de la carretera federal 54 (`ARG-110-001`) — **SIN AVANCE en la pregunta que decide**

⚠️ **Primero, una precisión de ventana que cambia el encuadre**: el ataque es del **jueves 27-ago**, anterior a la apertura de esta ventana. **En ARGOS 111 es seguimiento, no ficha nueva**, y así se trata.

**La pregunta era: ¿los seis son del mismo lote que los del 1 de agosto?** **No se puede responder, y ahora se sabe por qué.**

1. **El antecedente estaba mal identificado en el propio arranque.** Lo del «1 de agosto» son en realidad **dos hechos de la noche del 31-jul al 1-ago**: un **coche bomba en Luis Moya** (1 policía municipal muerto, 2 heridos, Operativo SAGAS) y, horas después, **Calera** (Río Frío), donde la FRIZ abatió a 5 civiles armados. **Un coche bomba y seis artefactos sembrados no son el mismo tipo de dispositivo**, y comparar «lote» entre ellos es comparar cosas distintas.
2. **No existe peritaje comparado publicado** de iniciadores, contenedores ni carga. Tampoco se publicó, para el hecho del 27-ago, **tipo de artefacto, sistema de iniciación ni carga**. Sin eso **no se distingue fabricación de adquisición**, que era el objeto de la pregunta.

**Pero el corte sí aporta la pieza que faltaba, y viene de otro sitio:** el hallazgo del **20-ago en Jiménez del Teul, Zacatecas** —**22 explosivos artesanales, 5 fulminantes eléctricos, ~30 kg de material explosivo y mecha lenta**, asegurados por Ejército, GN, FRIZ y FGJEZ— acredita **capacidad de manufactura local en la entidad**. Es un hecho fuera de ventana y no se integra a ningún total, pero **desplaza la hipótesis**: no hace falta un abastecedor externo para explicar seis artefactos. **La pregunta correcta para la edición siguiente ya no es «¿de dónde vinieron?» sino «¿cuántos talleres hay y dónde están?»**

⚠️ **La contradicción de lesionados sigue sin arbitrar, y ahora se sabe que es institucional, no periodística**: el **Secretario de Gobierno** dice **2 policías con heridas leves**; la **Fiscalía** dice **5 lesionados fuera de peligro**. **Dos órganos del mismo gobierno estatal con dos cifras.** No se promedia ni se elige. `CONTRADICHA — NO SE ARBITRA SIN FUENTE DIRECTA`.

### Eje 2 · El blanco se desplaza a procuración de justicia — **la hipótesis NO se confirma en esta ventana**

Se probó en **las seis regiones**. Resultado: **`SIN RESULTADO INDEXADO EN VENTANA` en las seis.** Ninguna agresión, amenaza ni AEI contra fiscalía, ministerio público o personal ministerial entre el 28 y el 29 de agosto.

**Lectura honesta**: los dos casos que originaron la hipótesis —Mexicali (26-ago) y Zacatecas (27-ago)— **siguen siendo dos**, y dos casos en dos días no son una serie. **No hay tercer caso.** La hipótesis **no se descarta** —el intervalo es demasiado corto para descartarla— pero **tampoco se refuerza**, y publicarla como patrón confirmado sería inventar una tendencia con dos puntos.

Lo que **sí** queda pendiente y no depende del buscador: **medir la coincidencia entre agresión y fase procesal** —qué carpetas sobre cada plaza llegaron a etapa crítica en los quince días previos—. Eso lo contesta un oficio, no una consulta.

### Eje 3 · Escuinapa, el equipo balístico (`ARG-110-002`) — **avance real, por una vía que no era la prevista**

Las tres preguntas del arranque siguen **SIN AVANCE**: no se publicó marca, nivel NIJ ni lote de las placas; no se publicó identidad ni adscripción de los cinco muertos; y no se pudo determinar si los 7 detenidos del Ejército y los 5 de la fiscalía son las mismas personas.

**Pero el corte produjo el dato que hace explotable la línea**, y no es de Escuinapa: **el equipo de protección balística aparece en cuatro eventos distintos**, tres de ellos en 48 horas, repartidos entre **Sinaloa y Nayarit**.

| Evento | Fecha | Chalecos | Placas balísticas |
|---|---|---|---|
| Escuinapa, Sinaloa (`ARG-110-002`) | 27-ago | 5 | **7** |
| **Escuinapa, Sinaloa (`ARG-111-002`)** | **28-ago** | **5** | **10** |
| Tepic, Nayarit (boletín federal) | 27-ago | 4 | **2** |
| La Guásima, Concordia, Sinaloa (antecedente) | 18-ago | 4 | **6** |
| Zacatecas, mun. de Tabasco (candidato sin ancla) | 27-28-ago | sí | **sí, sin cifra** |

**Diecisiete placas balísticas contabilizadas en un solo municipio en dos días, y veinticinco en cuatro eventos y dos entidades en menos de dos semanas.** Eso ya no es equipamiento individual: es **abastecimiento**. Y las placas siguen siendo **la pieza más trazable del conjunto** —marca, nivel NIJ, lote, importador—, muy por delante del rastreo de los fusiles. **La línea a explotar es el importador, no el portador.**

### Eje 4 · Ambigüedades de dominio de SSP — **tres de cuatro resueltas**. Ver §4.

### Otros seguimientos

| Caso | Resultado |
|---|---|
| **Puebla — la red de «El Dron»** (`ARG-109-004`) | **SIN AVANCE** en la pregunta principal, con **2 búsquedas** frente a las 11 de la edición anterior. **Pero cerró las dos contradicciones** (`-FE-003` y `-FE-004`). El tope duro funcionó: menos gasto, más resultado |
| **Michoacán — Pedernales** (`ARG-110-004`) | **La reserva sigue abierta y ahora se entiende mejor.** El respaldo periodístico de «3 muertos» pasó de 2 a **6 medios regionales**, pero **varios comparten redacción casi idéntica**: son republicadores de una sola nota base, **corroboración débil por construcción**, no seis fuentes. **No se recalifica el semáforo de ARGOS 110.** Falta el boletín de la FGE |
| **Michoacán — revólver .32 de Tacámbaro** (`ARG-109-001`) | **SIN AVANCE.** Sin número de serie, identidad de detenidos ni carpeta. Deslinde El Pedregoso/Pedernales reverificado y sostenido |
| **Michoacán/Guerrero — disputa forestal** | **SIN AVANCE.** Ni permisos de aprovechamiento forestal ni padrón de transportistas madereros están indexados. **No es una vía de buscador: es una solicitud a SEMARNAT y al RAN** |
| **Guerrero — El Arenal** (`ARG-110-REC-002`) | **SIN AVANCE.** **Sigue sin confirmación pericial de que los restos sean humanos**; la fuente más reciente sigue citando a un familiar diciendo que se requieren estudios forenses y genéticos. Sin número mínimo de individuos, sin cotejo, sin denuncia previa, sin titularidad |
| **Oaxaca — Loxicha** (`ARG-109-002`) | **SIN AVANCE**, y con **un candidato nuevo sin arbitrar**: «Acribillan a matrimonio y a un joven en Loxicha» (`imparcialoaxaca.mx`), **perfil de víctimas distinto** (matrimonio + joven, no una niña de 4 años). `POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN` |
| **Chiapas — Cintalapa** (`ARG-110-003`) | **Identidad del detenido obtenida**: José «N», «El Feyo», manifestó pertenecer al CCyG; 1 fusil 7.62×39 y 5 dosis de cristal. ⚠️ **Dos discrepancias nuevas**: una fuente da **9 cargadores** donde ARGOS 110 fichó **10**; y no está claro si «El Feyo» es una **segunda detención** o el detenido ya contabilizado. `DISCREPANCIA NUMÉRICA — NO INTEGRAR HASTA VALIDACIÓN`. Sin trazabilidad de la llamada al C5 |
| **Tamaulipas — rancho de Altamira** (`ARG-109-006`) | **SIN AVANCE** con 2 búsquedas. Dato nuevo menor: bienes asegurados por **33.9 mdp** atribuidos a la célula «Los Rojos» del Cártel del Golfo. Sin titularidad registral, ANAM, SEMARNAT/UMA ni destino del diésel |
| **Veracruz — Poza Rica** (`ARG-108-005`) | **SIN AVANCE.** El cotejo balístico cruzado de las tres carpetas **sigue sin constar realizado** |

---

## 10. Módulo de armamento — totales

**Todos los totales son cálculo propio de ARGOS**, derivados de cifras expresamente publicadas. Se declaran como tales.

### Línea A — asegurado en hechos DE LA VENTANA (2 eventos, 1 entidad)

*Cifras finales, tras las correcciones de `procedencia-cifras`.*

| Categoría | Total | Nota |
|---|---|---|
| Armas cortas | **1** | Concordia. Escuinapa no aportó ninguna: sus dos intervenciones describen solo armas largas |
| Armas largas | **9** | 5 Escuinapa (todas cal. 7.62×39) + 4 Concordia. **Corregido**: el borrador daba las 5 de Concordia como «sin clasificar»; la fuente sí las clasifica en 4 largas y 1 corta |
| Cartuchos | **3,528** | 703 Escuinapa (3+700, dos intervenciones) + 2,825 Concordia. **La cifra de Concordia procede de fuente única**; las demás publican «más de 2,800», que no es cifra |
| Cargadores | **82** | 27 Escuinapa (1+26) + 55 Concordia |
| Granadas | **0** | Ninguna publicada en la ventana |
| **AEI** | **49** | Concordia, **todos destruidos por detonación controlada**, ninguno trasladado ni peritado públicamente |
| Explosivos y componentes | **0** | La autoridad no publicó qué componentes se recuperaron de los 49 artefactos |
| Armamento especial | **0** | — |
| Chalecos tácticos | **5** | Escuinapa (1+4) |
| **Placas balísticas** | **10** | Escuinapa (2+8) |
| **Personas detenidas** | **3** | Escuinapa, una de nacionalidad estadounidense. **Concordia no produjo detenidos**: ausencia confirmada, no omisión |
| Entidades con aseguramiento | **1** | Sinaloa |
| Eventos contabilizados | **2** | Eventos cualitativos sin cantidad: 0 |

### Línea B — publicado durante el corte, hechos ANTERIORES a la ventana

Del boletín federal del 27-ago. **Fuera del total de la ventana.** Corroboración débil por
construcción (republicadores). *Cifras finales, tras las correcciones de `procedencia-cifras`.*

| Categoría | Total |
|---|---|
| Armas cortas | **11** (Mapastepec 3 · Tepic 2 · Oaxaca 2 · Cd. Madero 3 · Coatzacoalcos 1) |
| Armas largas | **12** (Mapastepec 1 · Tepic 4 · Oaxaca 4 · Cd. Madero 3) |
| Cartuchos | **1,072** (70 · 825 · 171 · 6) |
| Cargadores | **54** (3 · 28 · 23) |
| Granadas | **7** (Tepic 5 · Cd. Madero 2) |
| AEI | **4** (Aldama) |
| Armamento especial | **1** (lanzagranadas acoplado, Tepic) — **el único de todo el corte** |
| Chalecos | **8** (Tepic 4 · Cd. Madero 4) · Placas balísticas **2** (Tepic) |
| Personas detenidas | **28** (Mapastepec 9 · Oaxaca 10 · Cd. Madero 3 · Coatzacoalcos 6) |

**Dos renglones retirados antes de publicar**, ambos por hallazgo de control:
- **Tabasco · Villahermosa** (2 largas, 6 detenidos): **fecha mal atribuida**. Pertenece al boletín
  del **26 de agosto**, no al del 27. Retirarlo bajó largas de 10 a 8 antes de sumar Oaxaca, y
  detenidos de 34 a 28.
- **Veracruz · San Andrés Tuxtla** (3 cortas, 1 larga, 43 cartuchos, 7 cargadores, 6 detenidos):
  **duplicidad con `ARG-108-004`**, confirmada por `editor-duplicidad`.

⚠️ **Oaxaca se integra con contradicción declarada**: tres fuentes dan 4 largas y 2 cortas; una
nacional titula «4 armas de fuego» en total. **No se arbitra.**

⚠️ **Los 6 AEI de Zacatecas (`ARG-110-001`) NO figuran en ningún conteo**: fueron **empleados contra la autoridad**, no asegurados. Un AEI detonado no es un aseguramiento.

---

## 11. Módulo de sentencias — indicador de cobertura

| Indicador | Valor |
|---|---|
| Fiscalías revisadas | **32 de 32** (al menos una consulta) |
| FGR revisada | **Sí** |
| Fiscalías con sentencia publicada **en ventana** | **1** (FGED Durango) |
| Sentencias condenatorias integradas | **1** |
| Personas sentenciadas | **1** |
| Años de prisión acumulados | **No sumables**: la única pena se publica como «más de 10 años 8 meses», **cifra abierta**. `PENA NO EXACTA — NO SE INTEGRA AL TOTAL NUMÉRICO` |
| Sentencias firmes | **0** — la firmeza no se informa y **no se asume** |
| Fiscalías sin resultado indexado en ventana | **31** |
| Páginas no disponibles | **1** (`ssypc.nayarit.gob.mx`, anomalía de contenido) |
| No integradas | 1 agregado (Veracruz) · 1 retirada por umbral (`ARG-111-FE-002`) |

**Sentencias localizadas y descartadas por ventana**: 7 en Querétaro (4–25 ago), 4 en el Sureste (14 y 19 ago), 8 en Durango anteriores al 28-ago, varias en Michoacán y Jalisco. **La regla se cumple: se descartan por fecha, no por calidad.**

⚠️ **Confirmación del hallazgo estructural de ARGOS 110**: con ventanas de ~26 horas, **la probabilidad de que una fiscalía publique en esa franja es baja**. Se recorrieron 32 fiscalías para obtener **una** sentencia integrable. El triaje judicial encabezado **sigue siendo necesario para que el `SIN DATO` sea demostrable** —y esta vez produjo la sentencia—, pero su rendimiento está limitado por **la duración de la ventana**, no por el orden de búsqueda.

---

## 12. Controles editoriales

| Control | Ejecución |
|---|---|
| `barrido-regional` ×6 | ✅ Seis agentes en paralelo, autorizados por el destinatario |
| `editor-duplicidad` | ✅ Ejecutado como subagente |
| `procedencia-cifras` | ✅ Ejecutado como subagente |

Resultados en §13.

---

## 13. Hallazgos de los controles

**Sexta edición consecutiva en que los dos controles editoriales producen hallazgos reales.** Esta
vez ambos devolvieron `CORREGIR ANTES DE PUBLICAR` y **las nueve correcciones se aplicaron antes de
publicar**.

### `editor-duplicidad` — tres hallazgos, dos arbitrados con búsqueda adicional

| Hallazgo | Resolución |
|---|---|
| ✅ **San Andrés Tuxtla es `ARG-108-004`** | **CONFIRMADO Y EXCLUIDO.** El control verificó la coincidencia de municipio, corporación y **los seis detenidos exactos** —cifra ya corregida por `ARG-109-FE-001`—. Integrarlo habría contado dos veces a las mismas seis personas. El desglose de armas y la colonia son dato nuevo: se registran aquí, **no en el conteo** |
| ⚠️ **`ARG-111-002` Escuinapa: ¿duplicado de `ARG-110-002`?** | **ARBITRADO A FAVOR DE INTEGRAR, con fuente que el control no tenía.** Su duda era legítima —5 armas largas en ambos, 26/28 cargadores, 8/7 placas, 4/5 chalecos— y es exactamente la trampa de «dos desgloses del mismo hecho» de ARGOS 110. Se gastó **una búsqueda de coordinador** y apareció el deslinde: una fuente nacional **totaliza expresamente «diez detenidos» para el municipio** —siete el 27 y tres el 28—, lo que acredita que **se suman y no se sustituyen**. Además fijó el desglose por intervención. **Sin esa búsqueda, el hecho de mayor valor del corte se habría quedado fuera por precaución** |
| ⚠️ **Culiacán: «2 heridos / casa quemada» sin arbitrar** | **RESUELTO CON UNA BÚSQUEDA.** El control no podía arbitrarlo desde el archivo y advirtió, correctamente, que publicar «todos ilesos» con una fuente hablando de dos heridos sería falso. La verificación estableció que **esa nota corresponde a un hecho de diciembre de 2025**: no es el mismo evento ni cae en ninguna ventana abierta. **«Todos ilesos» se sostiene** |

También confirmó: `ARG-111-003`, `ARG-111-004`, `ARG-111-SEN-001` y `ARG-111-REC-001` **limpios de duplicidad**; que **«Petatlán» y «Parotal» no existen en el archivo**; que el retiro de `ARG-110-SEN-C02` por umbral es correcto; y **que un barrido regional trajo Totolapan como hecho nuevo cuando ya es `ARG-110-REC-001`**.

⚠️ **Hallazgo colateral valioso**: el control localizó que existe **otro «49 AEI»** en `argos-2026-08-26-fuentes.md`, procedente de un agregado del resumidor sobre acciones del 24-ago, **nunca integrado por falta de URL propia**. Es **coincidencia numérica sin relación** con Concordia —otras entidades, otro armamento—. Queda anotado para que ninguna edición futura los funda.

### `procedencia-cifras` — seis correcciones aplicadas

| Corrección | Detalle |
|---|---|
| ⚠️ **Error de agregación propio en Escuinapa** | El borrador sumó bien las armas largas (1+4=5) pero **usó solo la segunda intervención** en cuatro rubros. Corregido a **703 cartuchos** (3+700), **27 cargadores** (1+26), **5 chalecos** (1+4) y **10 placas balísticas** (2+8). **No era una cifra inventada: era una suma incompleta**, que es un modo de fallo nuevo en la serie y merece quedar registrado |
| ⚠️ **Concordia: las armas SÍ estaban clasificadas** | El borrador las daba como «5 sin clasificar». Una fuente publica el desglose: **4 largas y 1 corta**. Cambia el total nacional: cortas de 0 a **1**, largas de 5 a **9** |
| ⚠️ **Concordia: cartuchos** | «Más de 2,800» no es cifra, pero **una fuente publica 2,825 exactos**. Se integra la exacta **declarando que descansa en fuente única** |
| ⚠️ **Tabasco · Villahermosa: fecha mal atribuida** | Verificado en dos consultas: pertenece al boletín del **26 de agosto**, no al del 27. **Retirado de la línea inferior antes de publicar.** Corrige largas de 10 a 8 y detenidos de 34 a 28 en esa línea |
| ⚠️ **Oaxaca: SÍ tenía cifra de armamento** | Mi lectura del boletín no la vio; tres fuentes dan **4 largas y 2 cortas**, y una nacional titula «4 armas de fuego» en total. **Se integra con la contradicción declarada, sin arbitrar.** Sube la línea inferior a **11 cortas y 12 largas** |
| ⚠️ **Culiacán: hora y ubicación retiradas** | La hora «06:30» aparecía de forma consistente en dos consultas, con cruce de calles — hay indicio de que procede de una nota real—, pero **sin fragmento citable**. Se retira y **se conserva la marca de frontera**. También se retiró la ubicación «junto a una escuela primaria»: solo constaba en el resumidor, **que escribió el nombre del plantel de dos formas distintas**. Y se retiró el desglose «2 mujeres», que tampoco tenía fragmento propio |

**Aportaciones que enriquecieron el producto**, además de las correcciones: la **individualización completa de la sentencia de Durango** —fecha del hecho (7-mar-2024), localidad, objetos sustraídos, multa y reparación—, que eleva el caso de dos a **cinco campos individualizadores**; el hallazgo de que la **pena exacta consta en el cuerpo y el titular la redondea**; los **casquillos 9 mm** de Chihuahua; los **4 chalecos** de Ciudad Madero; y las **6 placas balísticas** del hallazgo del 18-ago en La Guásima, que completan la serie del eje balístico.

**Confirmó además**: que los **6 AEI de Zacatecas no se colaron** en ningún conteo; que **cartuchos y cargadores no se sumaron entre sí** en ningún renglón; que no hubo **ninguna conversión de cargadores a cartuchos**; y que «más de 100 casquillos» y «más de 2,800 cartuchos» estaban **correctamente tratadas como no-cifra**.

⚠️ **Reserva abierta que el control dejó anotada**: otras coberturas del ataque de Chihuahua lo sitúan en **«Cerro Coronel»** y en la **«colonia Lealtad»**. **No se funden ni se arbitran** sin verificar que se trata del mismo domicilio. Declarado en la ficha.

### Cuarta reincidencia evitada, y por primera vez en la primera pasada

La regla operativa que ARGOS 110 escribió —«**toda expresión de distancia o duración que no proceda
de una medición publicada se retira en la primera pasada, no en el control**»— **funcionó**: el
redactor no introdujo ninguna. Lo que el control sí retiró fue una **ubicación relativa** («junto a
una escuela primaria»), que es la misma familia de defecto. **Se propone extender la regla del
arranque de distancias y duraciones a las ubicaciones relativas.**

---

## 14. Advertencia de comparabilidad

**Los totales de ARGOS 111 no son comparables sin más con los de otras ediciones.** Razones, todas declaradas:

1. **Dos de los cuatro hechos y el hecho de recuperación llevan reserva de frontera o de fuente.** `ARG-111-001` es `FRONTERA DE VENTANA — HORA NO FIJADA`.
2. **El módulo de armamento del corte descansa en una sola entidad** (Sinaloa) y **dos eventos**. Un total nacional construido sobre dos eventos no mide el país: mide lo que se publicó.
3. **El candidato de mayor volumen del corte —Zacatecas, 11 detenidos y 10 armas largas— quedó fuera** por falta de fecha en la ruta, pese a ser fuente institucional. Si se anclara, cambiaría los totales de forma sustancial.
4. **El índice del buscador va por detrás del corte.** La ventana cierra a las 09:05 del sábado 29 y las consultas devolvían consistentemente material del 24 al 28. **Parte del vacío de esta edición es de reloj, no de método** — lo declararon Occidente y Centro de forma independiente.
