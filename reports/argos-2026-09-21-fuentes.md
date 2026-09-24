# ARGOS 122 — Archivo de fuentes y método

**Corte**: 2026-09-21 · **Ventana**: 17-sep 17:36 → 21-sep 08:57 CDMX · **87 h 21 min**
**Hora sellada**: verificada con `TZ=America/Mexico_City date` al arranque, no supuesta.
**Densidad**: **0,19 hechos/hora** (17 ÷ 87,35 — cálculo propio, recalculada tras los controles).
**Techo de confianza**: **★★★☆☆**, por bloqueo de egreso. Tercera edición consecutiva.

Este archivo contiene lo que **no va al cartelón**: la lista íntegra de emisores, el registro del
barrido, las decisiones de arbitraje, la fe de erratas y la deuda de método. El cartelón es para el
mando; esto es para la auditoría.

---

## 1. La base: por decimoséptima vez, la rama del entorno llegó desactualizada

La rama asignada, `claude/argos-122-criminal-analysis-n4stuu`, llegó **sin la serie restituida**.
`git merge --ff-only origin/claude/argos-122-criminal-analysis-e5il36` lo resolvió en el primer
comando de la sesión, **antes de leer `CLAUDE.md`**.

Estado encontrado tras el ff: última edición `argos-2026-09-17` (ARGOS 121) y **111 archivos** en
`reports/` — la orden de arranque decía 110 porque **no se contó a sí misma**. Coincide.

⚠️ **Diecisiete ediciones seguidas no son un accidente: es el comportamiento estable del entorno.**
Esta edición **no heredó borrador**, de modo que **todos los deslindes nacieron verificados**.

---

## 2. Rotación de cobertura — CICLO C aplicado y declarado

| Regla | Aplicación en ARGOS 122 |
|---|---|
| **Ciclo que tocaba** | **CICLO C** — **Occidente y Sureste encabezan el triaje judicial** |
| **Prioridad sobre el ciclo** | **YUCATÁN primero y en los dos módulos**, por haber quedado `NO REVISADA` en ARGOS 121. Coincide con el ciclo (es del Sureste). **SSP y FGE de CHIAPAS** también encabezaron, por haberse cubierto en ARGOS 121 solo por mención general |
| **Regiones que encabezaron con armamento** | Noroeste, Noreste, Centro y Golfo |

### Qué aportó la rotación que el orden anterior no habría aportado

- **Yucatán queda saldada**: `fgeyucatan.gob.mx` y `ssp.yucatan.gob.mx` recibieron consulta dirigida
  propia. Resultado: `SIN RESULTADO INDEXADO EN VENTANA` en los dos. **Es un vacío demostrable, no un
  vacío heredado.**
- **Chiapas queda cubierta con consulta dirigida a su dominio** (`fge.chiapas.gob.mx`,
  `sspc.chiapas.gob.mx`), y **el hecho rojo de Tuxtla Gutiérrez no lo trajo el barrido: lo trajo el
  recall nacional**. El barrido sí aportó **las quince detenciones posteriores** y la **cadena de
  autoría desde el penal de Ocosingo**, que el recall no tenía.
- **El Occidente, encabezando judicial, produjo la única sentencia estatal candidata del corte**
  —Morelia, 93 años 9 meses— y **cerró por agotamiento la cifra de Mezcales**. **El Ciclo C sí produjo
  candidato judicial, a diferencia del Ciclo B de ARGOS 121, que no produjo ninguno.**
- **Corrección de dominio que la rotación hizo visible**: `fiscaliaoaxaca.gob.mx` **no existe ni
  indexa**. El dominio real es **`fge.oaxaca.gob.mx`** (espejo `portal.fgeo.gob.mx`). Se usó en
  cortes anteriores el dominio equivocado.

⚠️ **A ARGOS 123 le toca el CICLO A (Noroeste + Centro), pero la prioridad vence al ciclo**:
**Tamaulipas y Coahuila** quedaron por debajo del estándar en armamento y **Campeche** solo recibió
consulta general. **Las tres encabezan.**

---

## 3. El recall nacional del coordinador — decimotercera edición consecutiva

⚠️ **Volvió a aportar los hechos de mayor gravedad que ningún barrido regional vio.** De los **cinco
eventos rojos del corte**, **cuatro los trajo el recall**:

| Hecho | Lo trajo | Lo vio algún barrido |
|---|---|---|
| **Tuxtla Gutiérrez, Las Granjas** (3 muertos) | **Recall** | El Sureste lo confirmó y añadió las 15 detenciones |
| **Celaya** (3 muertos, 5 heridos) | **Recall** | **No** |
| **Valle de Santiago** (campo de béisbol) | **Recall** | **No** |
| **Los Aldamas, Nuevo León** | Barrido Noreste | — |
| **Sierra de Sinaloa** (agresión a SEMAR/SSPC) | **Recall** | El Noroeste lo confirmó con el desglose |
| **Mochitlán y Quechultenango** (`-REC-`) | **Recall** | **No** |

**Trece ediciones seguidas dejan de ser una observación y son una propiedad del método**: el barrido
encuentra lo que las instituciones publican; el recall, lo que ocurre. **No es sustituible por más
equipos.** Con una ventana de 87 horas la diferencia fue máxima: **los barridos regionales no
detectaron ninguno de los tres ataques con víctimas mortales civiles del corte.**

---

## 4. El boletín federal: existe uno y solo uno, y su emisor no lo indexó

**Triple consulta aplicada a los cinco tramos de la ventana** —día suelto, rango, y título sin
restricción de dominio—:

| Tramo | Resultado |
|---|---|
| **17-sep** | ✅ **EXISTE**. «El Gabinete de Seguridad del Gobierno de México informa acciones relevantes del 17 de septiembre de 2026». **De un solo día.** ⚠️ **`gob.mx/sspc` NO lo indexó**: se alcanza **solo por republicadores** —Milenio, SICOM Noticias, Eleese Noticias (fecha en la ruta), Talla Política, Certeza Diario— |
| **18-sep** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |
| **19-sep** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |
| **20-sep** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |
| **21-sep** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |

⚠️ **Cuatro de los cinco días de la ventana quedan sin agregado federal.** El formato del emisor
**volvió a cambiar**: ARGOS 121 recibió un agregado de tres días (14-16-sep); ARGOS 122 recibe un
diario. **El formato no es estable y no debe suponerse por el del corte anterior.**

**Corolario de trazabilidad aplicado**: la sustitución por republicadores **se anota en cada ficha**
y la corroboración se declara **débil por construcción** — cinco republicadores del mismo boletín
**no son cinco fuentes independientes**.

### Renglones del boletín del 17-sep integrados

Todos llevan `FRONTERA DE VENTANA — HORA NO FIJADA`, porque el boletín cubre el **17-sep** completo y
**la ventana abre ese día a las 17:36**:

`ARG-122-013` San José Iturbide, Guanajuato · `ARG-122-015` La Piedad, Michoacán ·
`ARG-122-016` Centro (col. Pino Suárez), Tabasco · `ARG-122-017` Centro (rancho Plátano y Cacao),
Tabasco · `ARG-122-018` La Paz, Baja California Sur.

### Renglón del boletín del 17-sep DECLARADO Y NO INTEGRADO

⚠️ **MICHOACÁN, municipio consignado como «Mazatlán»** — 2 armas cortas, 2 largas, 5 cargadores,
2 detenidos, 1 vehículo blindado, SSPC y FGR.
**NO SE INTEGRA**: **no existe un municipio llamado Mazatlán en Michoacán**, el dato solo consta en
el resumen del buscador y **no pudo verificarse con fuente propia**.
`MUNICIPIO NO VERIFICADO — POSIBLE ERROR DE TRANSCRIPCIÓN DEL RESUMIDOR`.
Dado que el resumidor ha fabricado **veintitrés fechas y folios en seis cortes**, **la prudencia se
aplica al renglón completo**: se pierden 4 armas del total antes que arriesgar una entidad falsa.
**ARGOS 123 debe intentar fijarlo.**

⚠️ **JALISCO · Guadalajara** — 2 órdenes de aprehensión por extorsión agravada y asociación
delictuosa, 3 teléfonos, sin armas. **No se ficha por volumen**: es un renglón sin cifra explotable.
Se registra aquí.

---

## 5. Fe de erratas — el boletín federal del 17-sep corrige ARGOS 121 AL ALZA

### `ARG-122-FE-001` — Coyuca de Benítez, Guerrero (corrige `ARG-121-001`)

⚠️ **ES LA CORRECCIÓN MÁS IMPORTANTE DEL CORTE Y NO VA AL CARTELÓN, POR LA REGLA DE FE DE ERRATAS.**

ARGOS 121 publicó el cateo de la **Secretaría de Seguridad Pública municipal de Coyuca de Benítez**
con **siete policías detenidos, incluido su jefe**, declarando literalmente
`ARMAMENTO NO PUBLICADO: NO ALIMENTA EL CONTEO Y NO SE INFIERE`. **Hizo lo correcto: el dato no
existía publicado cuando cerró.**

El **boletín federal del 17-sep**, aparecido **después** de ese cierre, publica el desglose:

| Categoría | Cifra |
|---|---|
| **Armas largas** | **58** |
| **Armas cortas** | **32** |
| **Cargadores** | **314** |
| **Cartuchos** | **8,010** |
| **Vehículos oficiales** | **2** |
| **Detenidos** | **7 policías municipales** — ✅ **CONFIRMA la cifra que ARGOS 121 arbitró por procedencia frente a las agregaciones de 8 y 10** |

**Efecto sobre ARGOS 121**: sus totales pasarían de **2 a 34 armas cortas**, de **2 a 60 largas**, de
**0 a 314 cargadores** y de **0 a 8,010 cartuchos**. **La confianza de la fila sube de ★★★☆☆ a Medio
con desglose institucional.**

⚠️ **NO SE INTEGRA A LOS TOTALES DE ARGOS 122**: corrige la edición de origen, no la que lo encuentra.
⚠️ **NO ES FALLO DE ARGOS 121**: el boletín no existía indexado cuando cerró, y **no inferir fue la
decisión correcta**.

**Valor de inteligencia, que sí llega al cartelón por otra vía**: **noventa armas de fuego en una
corporación policial municipal** es el dato que sostiene la primera línea de «LO QUE DEBE HACER EL
MANDO» y la quinta conclusión. **Se publica como conclusión accionable, no como fe de erratas.**

### `ARG-122-FE-002` — Angamacutiro, Michoacán (adopta una cifra que ARGOS 121 declaró y no adoptó)

ARGOS 121 registró los **«18 detenidos»** de los cateos derivados de la captura de «El Señor de la T»
como **atribución de tercero NO ADOPTADA**, por no tener desglose. **Cuatro coberturas coincidentes**
—Infobae, Quadratín Michoacán, Esfera Noticias, RED Michoacán— la sostienen y **precisan el cargo de
uno de los detenidos: el director de la Policía Municipal de Angamacutiro**, más **tres agentes**.

**Queda adoptada** — pero ⚠️ **NO como hecho propio**. El control `editor-duplicidad` señaló que
`ARG-121-REC-005` **ya había citado** los 28 cateos y los 18 detenidos, y que tratarlo como hecho
nuevo era **asimétrico con el tratamiento de Coyuca**, que es la misma situación. **Se acepta el
hallazgo**: se publica como **`ARG-122-REC-002`**, **ventana de origen ARGOS 121**, **fuera del
semáforo, del mapa, del radar y de todos los totales**. **Lo que esta edición añade y no constaba es
el cargo de los cuatro policías detenidos.** **Su armamento sigue sin cantidad publicada.**

---

## 6. Pendientes cerrados y candidatos resueltos

| Pendiente heredado | Disposición en ARGOS 122 |
|---|---|
| ⚠️ **CHIHUAHUA · Ciudad Juárez — JOSÉ MANUEL E. C.** | **`SIN RESULTADO INDEXADO EN VENTANA`, SEGUNDA EDICIÓN.** **Cinco formulaciones distintas** —`site:` al dominio, sin restricción, con nombre completo, con «individualización de la pena», con «Cordillera de los Andes»—. **El fallo condenatorio está confirmado y fechado; la pena no aparece.** ⚠️ **NO se afirma que la audiencia se pospusiera: eso no está acreditado.** **Sigue siendo el candidato más maduro del archivo** |
| ⚠️ **ZACATECAS · Villa González Ortega** | **CIERRE REFORZADO.** El Noreste localizó **URL con fecha en la ruta de 2023** (`elmanana.com.mx/nacional/2023/4/29/…`) y una nota que fija el arresto en **agosto de 2021**. **Confirma el retiro por agotamiento de ARGOS 121. NO REABRIR** |
| ⚠️ **BAJA CALIFORNIA · Tijuana — Luis Martín «N»** | **SE REFUERZA, NO SE CIERRA.** Seis medios regionales independientes coinciden **sin variación** en **26 años 8 meses, 500 UMA (56,570 pesos) y 874,680 pesos**. **Dos campos individualizadores NUEVOS**: hecho del **1-abr-2025 entre 00:22 y 07:12 en avenida Revolución, Zona Centro**, y **captura el 13-jul-2025 en Monterrey, Nuevo León** (vinculación 18-jul-2025). ⚠️ **El boletín `fgebc.gob.mx/boletines/12722` sigue sin poder leerse y sigue diciendo 23 años sin nombre.** `POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN` |
| **NAYARIT · Mezcales — cartuchos** | ⚠️ **PROCEDE RETIRO POR AGOTAMIENTO.** **Tercera versión localizada**: 14 + 12 = **26** (Tribuna de la Bahía, Crítica DN), frente a 11 + 14 + 19 = **44** de otras. **El umbral de la regla de cifras arrastradas se cumple.** `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`. **Además el hecho es anterior al 14-sep**: fuera de esta ventana en cualquier caso |
| ⚠️ **AGUASCALIENTES · Cosío, El Salero** | **CUARTO INTENTO FALLIDO.** Mismo *slug* de `gob.mx/guardianacional/prensa` **sin fecha en la ruta**, reconfirmado; **ningún republicador con fecha propia**. **Sigue siendo el mayor volumen pendiente del archivo** —17 largas, una cal. .50, «más de 1,500» cartuchos, 3 detenidos—. ⚠️ **Si ARGOS 123 tampoco lo fija, PROCEDE EL UMBRAL DE AGOTAMIENTO como en La Trinitaria** |
| **TAMAULIPAS · Nuevo Laredo — Carlos, Adrián, Luis y José «N»** | **TERCER INTENTO FALLIDO.** Ni FGR ni Poder Judicial Federal de Tamaulipas publican el día; los republicadores confirman **mes y año, no día**. ⚠️ **Procede declararlo `FECHA NO DETERMINABLE BAJO BLOQUEO DE EGRESO`** |
| **GUANAJUATO · San Francisco del Rincón — heridos 5 o 6** | ⚠️ **HALLAZGO ORIENTADOR, NO CIERRE**: existen **DOS incidentes armados distintos y consecutivos** en el mismo municipio —**12-sep** (centro, 1-2 muertos, 1 herido grave) y **13/14-sep** (cancha del Barrio de Guadalupe, 1 muerto, 6 heridos)—. **La contradicción del archivo puede ser una CONFLACIÓN DE DOS HECHOS, no una cifra en disputa.** Sin parte médico en ninguno. **ARGOS 123 debe revisarlo como dos fichas posibles** |
| **ESTADO DE MÉXICO · fgjem.edomex.gob.mx** | **QUINTA VERIFICACIÓN SIN BOLETÍN PRIMARIO.** Temoaya (125 años), Coacalco (36a 3m) y Hueypoxtla (21a 10m 15d) siguen **sin boletín de la fiscalía emisora**. **Sigue siendo el vacío judicial más costoso del archivo** |
| **CIUDAD DE MÉXICO · Tepito** | **CERO BOLETÍN, TERCERA EDICIÓN.** Y aparece una **TERCERA versión de edades** —«15 y 20 años»— junto a las dos ya registradas (25-30 y 18-19). **No se arbitra.** La cifra de «4 detenidos» **sigue descartada** por proceder de un *liveblog* |
| **fiscaliaguerrero.gob.mx** | **QUINTA EDICIÓN.** Por instrucción expresa se limitó a una búsqueda: **el patrón de no indexación de sus boletines recientes está documentado y la vía que funciona es el republicador** |
| **SINALOA · Mazatlán — los 53 AEI** | `SIN RESULTADO INDEXADO EN VENTANA` para zona exacta, iniciador y carga. **El hecho es del 15-sep: fuera de esta ventana.** No se republica |
| **CHIHUAHUA · Coyame del Sotol — calibre** | ⚠️ **ALERTA NUEVA**: el Noroeste encontró **al menos TRES sucesos distintos en el mismo municipio con cifras distintas** —«22 armas y 10 mil cartuchos» (2025), «rifle y más de mil 800 cartuchos» (17-sep-2026) y el de 3,358 cartuchos—. **ARGOS 123 debe tratar «Coyame del Sotol» como varios eventos candidatos, no como uno** |

---

## 7. Arbitrajes del coordinador — en las dos direcciones

El arbitraje sobre las clasificaciones es del coordinador y **se ejerce también a la baja**.

| Caso | Propuesta del barrido | Decisión y motivo |
|---|---|---|
| **Sierra de Sinaloa** (`ARG-122-005`) | 🟡 **con reserva** — «la fuente no precisa quién disparó primero» | ⚠️ **SE SUBE A 🔴.** Proceso, Excélsior y El Heraldo dicen expresamente **«tras agresión a marinos y policías»** y **«personal fue agredido con armas de fuego por sujetos a bordo de seis vehículos»**. **Quién inició SÍ está determinado**: el grupo criminal, contra personal en patrullaje. Es la fila roja de la tabla |
| **Los Aldamas** (`ARG-122-004`) | **caso límite, 🔴 o 🟡** | ⚠️ **🔴.** Los sujetos **dispararon al ser detectados durante un patrullaje activo**, no al ser objeto de un cateo o una detención. **Los cuatro abatidos no mueven el color** |
| **Mochitlán y Quechultenango** (`ARG-122-REC-001`) | 🟡 | ⚠️ **SE CONFIRMA 🟡, Y ESTE ARBITRAJE ES A LA BAJA.** El coordinador valoró subirlo a 🔴 por el bloqueo coordinado en dos municipios, la quema de patrullas y la carpeta por tentativa de homicidio. **No procede**: `CLAUDE.md` es explícito en que **cuando la fuerza pública ejecuta una acción y es repelida, el color es amarillo**, y **ninguna de las agravantes tasadas concurre acreditada** —los explosivos están **alegados sin confirmación oficial**, los dos civiles heridos **participaban en el hecho** y **no hay muerte de personal acreditada**. **Subirlo habría inflado el nivel de riesgo nacional con un hecho no acreditado, que es justo lo que la metodología prohíbe** |
| **Puerto Peñasco** (`ARG-122-007`) | 🟡 | **🟡 confirmado.** Operativo iniciado por la autoridad, con topón. **Los 7 detenidos y las 3 víctimas rescatadas no mueven el color** |
| **Juchitán** (`ARG-122-006`) | 🟡 | **🟡 confirmado.** **Sin víctimas**; ninguna agravante de la lista roja concurre. **La condición de la víctima no basta sin daño consumado** |
| **Tuxtla Gutiérrez** (`ARG-122-001`) | 🔴 | **🔴 confirmado**: víctimas múltiples + menor entre las víctimas + ejecución pública |
| **General Treviño, Nuevo León** | traído como aseguramiento nuevo del 15-sep | ⚠️ **NO SE INTEGRA.** Son **tres vinculaciones a proceso** por el enfrentamiento del **14-sep** ya publicado (`ARG-120-ARM-003`). **Una vinculación a proceso no es un aseguramiento nuevo ni una sentencia.** **El propio barrido lo advirtió y acertó** |

### Cifras contradichas y cómo se resolvieron

| Cifra | Versiones | Resolución |
|---|---|---|
| **Puerto Peñasco — detenidos** | **7** (titular de la SSPC federal) · **10** (cobertura regional) | **ARBITRADA POR PROCEDENCIA: se adopta 7**, la atribuida expresamente a la autoridad. Mismo criterio que Coyuca y El Rosario |
| **Puerto Peñasco — armas largas** | **33** · **«más de 40»** | **Se conserva 33**, única cifra expresa. `«MÁS DE» NO ES CIFRA` |
| **Tuxtla Gutiérrez — edad del menor herido** | **10** (Fiscal General) · **12** (otra cobertura) | **ARBITRADA POR PROCEDENCIA: se adopta 10** |
| **Valle de Santiago — muertos** | **4 y 5 heridos** · **3 y 5 heridos** | ⚠️ **NO SE ARBITRA.** **La FGE de Guanajuato no publicó cifra**, y **sin emisor institucional no se arbitra por mayoría**. **Se publican las dos versiones** |
| **Quechultenango — muertos y retenidos** | **1 muerto / 10 heridos** (alcalde) · **5 heridos, cero muertos** (SEDENA) · **sin denuncias por fallecidos** (FGE) · **2 fallecidos** · **4 muertos y 8 heridos** · retenidos **29** frente a **19** | ⚠️ **NO SE ARBITRA.** **Cuatro versiones institucionales y periodísticas en conflicto abierto, sin conciliación pública.** Se publican todas |
| **«El Cholo» — pena** | **332 años 6 meses** · **«300 años»** · **«más de 300»** | **Se adopta 332 años 6 meses**: **cifra precisa, en el cuerpo de ocho coberturas y atribuida expresamente a la FGR**. Los titulares redondean |

---

## 8. La decisión de integrar la sentencia de «El Cholo»

`CLAUDE.md` es asimétrico a propósito: **una sentencia con confianza «Bajo» no basta**, y
`Bajo` se define como **«dos fuentes periodísticas coincidentes sin comunicado oficial»**.

**Aquí SÍ hay comunicado oficial**: ocho coberturas nacionales y regionales **citan expresamente a la
FGR como emisora** y **nombran la unidad —FEMDO en coordinación con FECOR—**, con **pena exacta, multa
exacta al peso y cinco campos individualizadores**. Lo que falta **no es el comunicado, sino la
lectura directa de `fgr.org.mx`**, imposible **para toda fuente de esta edición** por el bloqueo de
egreso.

Eso es **«fuente oficial única con datos suficientes» = Medio**, y **Medio sí integra**.
**Precedente del archivo**: `ARG-120-SEN-001` y `ARG-120-SEN-002`, ambas de la FGR, **se integraron con
confianza Medio bajo el mismo bloqueo**. Aplicar aquí un criterio más estricto sería **cambiar la
regla entre ediciones**.

⚠️ **Si ARGOS 123 localiza el comunicado con su número de folio, la confianza sube y se anota.
Si aparece evidencia de que el comunicado no existe, procede fe de erratas y retiro.**

---

## 9. Limitación de herramienta — reverificada, y el techo sigue sin subir

| Dominio | Vía | Resultado |
|---|---|---|
| `www.gob.mx/sspc` | `curl` | `000` |
| `fiscaliachihuahua.gob.mx` | `curl` | `000` |
| `www.infobae.com` | `curl` | `000` |
| `www.milenio.com` | `curl` | `000` |

**Ninguna página de este corte se leyó íntegra.** Todo lo publicado se sostiene en **extractos del
buscador más la fecha en la ruta de las URL**.

⚠️ **Techo de confianza ★★★☆☆ — tercera edición consecutiva.** **No es una degradación del criterio:
es una degradación de la herramienta.** `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar y
es la única solución real.** **Los seis barridos, ejecutados en paralelo, no levantan este techo:
multiplican las peticiones contra la misma puerta cerrada.**

---

## 10. Registro del barrido — cobertura entidad por entidad

**Seis agentes `barrido-regional` en paralelo, en un solo mensaje.** Búsquedas declaradas: **Sureste
22 · Occidente 20 · Noroeste 20 · Noreste 22 · Centro 23 · Golfo 26**. El Centro **declaró exceso de
presupuesto (+3) sin atenuarlo**; se registra.

### Portales que publicaron dentro de la ventana

Gabinete de Seguridad (boletín 17-sep, vía republicadores) · FGE Chiapas (por cita del Fiscal General)
· FGE Guanajuato (por cita, sin cifra en Valle de Santiago) · Fuerza Civil Nuevo León (por cita) ·
SSPC federal y SEMAR (por cita) · FGE Oaxaca (por cita) · SSC y FGJ CDMX (por cita) · FGE Veracruz
(boletín de sentencias del 18-sep y cateo de Tempoal) · Guardia Civil Estatal de San Luis Potosí ·
FGE Michoacán (por cita) · FGR (sentencia de Nuevo Laredo y delegación de San Luis Potosí).

### `SIN RESULTADO INDEXADO EN VENTANA`

fgeyucatan.gob.mx · ssp.yucatan.gob.mx · fge.chiapas.gob.mx · sspc.chiapas.gob.mx · fgeqroo.gob.mx ·
fiscaliatabasco.gob.mx · fiscaliaestatal.jalisco.gob.mx · fiscalianayarit.gob.mx ·
fiscalia.aguascalientes.gob.mx · fiscaliaguanajuato.gob.mx · fgecolima.gob.mx · sspjalisco.gob.mx ·
ssp.michoacan.gob.mx · fge.michoacan.gob.mx · fiscalia.durango.gob.mx · fgebc.gob.mx ·
sspe.chihuahua.gob.mx · fiscaliachihuahua.gob.mx (para la pena de Juárez) · SSP Tamaulipas ·
FGE/SSP Coahuila · FGJ Nuevo León · FGJ Zacatecas · FGE San Luis Potosí (boletín propio) ·
sseguridad.edomex.gob.mx · ssp.morelos.gob.mx · ssp.puebla.gob.mx · sscqro.gob.mx ·
s-seguridad.hidalgo.gob.mx · ssc.tlaxcala.gob.mx · fgjem.edomex.gob.mx · fiscaliageneralqro.gob.mx ·
fiscalia.puebla.gob.mx · PGJ Hidalgo · FGE Morelos · PGJ Tlaxcala · ssc.cdmx.gob.mx ·
gob.mx/guardianacional/prensa · gob.mx/sspc (tramos 18-21 sep) · gabinetedeseguridad.gob.mx/resultados/
· SEMAR Cuarta Región Naval · FGET Tabasco (boletín de las seis ejecuciones del 15-sep).

### `SIN ACTUALIZACIÓN CONSTATADA` — se vio el listado

`ssp.zacatecas.gob.mx`: publicaciones del 17 y 20-sep sobre **seguridad en desfiles patrios y pláticas
de prevención de extorsión**, **sin aseguramiento de armamento en la ventana**. **Única casilla de este
tipo del corte**, porque **bajo bloqueo de egreso casi nunca puede afirmarse**.

### `NO REVISADA`

**Cero entidades.** La **profundidad fue desigual y se declara**: **Tamaulipas y Coahuila** quedaron
por debajo del estándar en armamento **por falta de indexación, no por omisión de búsqueda**;
**Campeche** solo recibió consulta general; **Aduanas/ANAM del puerto de Veracruz** no se llegó a
consultar; las **SSP de Colima, Nayarit, Aguascalientes y Guanajuato** no recibieron consulta
dirigida propia.

### Correcciones de dominio detectadas — para la instrucción de ARGOS 123

| Dominio usado | Dominio real |
|---|---|
| `fiscaliaoaxaca.gob.mx` | **`fge.oaxaca.gob.mx`** (espejo `portal.fgeo.gob.mx`) |
| `ssc.queretaro.gob.mx` | probablemente **`sscqro.gob.mx`** — sin verificar |
| `ssph.hidalgo.gob.mx` | probablemente **`s-seguridad.hidalgo.gob.mx`** — sin verificar |
| Tlaxcala (prensa general) | **`ssc.tlaxcala.gob.mx`** — sin verificar |

---

## 11. Señuelos descartados — no redescubrirlos

| Señuelo | Por qué se descartó |
|---|---|
| **Tierra Blanca, Veracruz** — «108 armas largas, 50-57 granadas, ~51,400 cartuchos, ~2,700 cargadores, 3 lanzagranadas» | **Es de JUNIO de 2026.** Reaparece indexado sin fecha visible en varios portales, pero **La Jornada y La Red Informativa lo anclan con fecha en la ruta en junio**. **Cifras idénticas a las que se buscaban: trampa de señuelo documental** |
| **Coahuila** — «116 armas» / «cientos de armas en cateo en Piedras Negras» | **Es del 14-abril-2026** |
| **Nuevo León** — «arsenal de 210 armas de fuego» | Publicado **1-sep-2026**, fuera de ventana |
| **Sonora** — «Juan N», Hermosillo, FGR, 7 años 7 meses 19 días, multa 177 UMA | ⚠️ **SIN URL VERIFICABLE. Posible fabricación del resumidor**, mismo patrón que los folios inventados. **No se integra ni se presenta como hallazgo** |
| **Chihuahua** — 4 largas, 590+ cartuchos, 16 cargadores, 18-sep | **Sin URL propia**: solo en el resumen del buscador. `NO CONFIRMADO — NO SE INTEGRA` |
| **Durango · Tamazula** — 1 ametralladora, 1 larga, 2 cargadores, 145 cartuchos, artefacto explosivo | **Fecha no fijada** ni en ruta ni en cuerpo. **No se integra** |
| **Jalisco · Ojuelos** — «21 detenidos, armas, 9 mil cartuchos y 53 explosivos en 2 estados» | ⚠️ **Los «53 explosivos» son los 53 AEI de Mazatlán ya publicados (`ARG-121-REC-003`)**, dentro de un agregado. `FECHA NO FIJADA` y **riesgo de duplicidad**: **no se integra** |
| **El Rosario y Escuinapa, Sinaloa; Ensenada, BC** | Del agregado federal **14-16-sep**: **ventana de ARGOS 120**. **No se recuentan** |

---

## 12. Lista íntegra de fuentes por ficha

**Institucionales citadas** (ninguna leída íntegra): Gabinete de Seguridad · SSPC federal · SEMAR ·
SEDENA · FGR (FEMDO, FECOR, delegaciones de Tamaulipas y San Luis Potosí) · Guardia Nacional ·
FGE Chiapas · FGE Guanajuato · FGE Oaxaca · FGE Veracruz · FGE Michoacán · FGE Guerrero ·
FGJ Ciudad de México · SSC Ciudad de México · Fuerza Civil Nuevo León · Guardia Civil Estatal de
San Luis Potosí · SSP Veracruz.

**Nacionales**: La Jornada · Infobae · Milenio · El Universal · Excélsior · Proceso · El Financiero ·
El Heraldo de México · La Razón · La Silla Rota · N+ · SDP Noticias · MVS Noticias · SinEmbargo ·
Vanguardia · Aristegui Noticias · La Crónica de Hoy · El Informador · Diario de Yucatán.

**Regionales**: Alerta Chiapas · ZOLO Noticias · El Sol del Soconusco · KCH Comunicación ·
El Congresista · Periódico AM · Periódico Correo · Guanajuato Informa · Notus · Azteca Bajío ·
UnoTV · El Imparcial (Sonora) · Proyecto Puente · RED Michoacán · Tribuna · En Blanco y Negro ·
Los Noticieristas · Azteca Sinaloa · Diario de Juárez · Central Municipal · La Opinión ·
La Clave Online · XEU Noticias · Zócalo · Veracruz en Red · La Nigua · Potosí Noticias ·
El Heraldo de San Luis Potosí · Esfera Noticias · Quadratín Michoacán · El Sol del Bajío · Rotativo ·
El Tiempo Monclova · NX Noticias · Diario de México · TV Azteca · Posta · ABC Noticias ·
La Plaza Diario de Acapulco · Quadratín Guerrero · El Sur Acapulco · Serpientes y Escaleras.

**Republicadores del boletín federal del 17-sep** (⚠️ **no son fuentes independientes entre sí**):
SICOM Noticias · Eleese Noticias · Certeza Diario · Talla Política · Milenio.

**Fuentes abiertas consultadas y NO usadas como confirmación**: ninguna se integró. Las coberturas
de blogs de nota roja aparecieron en resultados y **se descartaron expresamente** —el saldo de
Quechultenango que publicaban no coincide con ninguna fuente institucional—.

---

## 13. Vacíos de publicación que el mando debe conocer

1. **La munición desaparece de los boletines cuando el arsenal es grande.** **59 armas largas y solo
   124 cartuchos**: los cuatro mayores aseguramientos —sierra de Sinaloa, Puerto Peñasco, Los Aldamas
   e Iztapalapa— **publicaron las armas y no la munición**. Sin esa razón **no se estima capacidad de
   fuego ni autonomía de combate**.
2. **Cero números de serie en 65 armas**, y **solo dos calibres publicados**, las dos piezas cal. .50.
   **El retroceso continúa**: ARGOS 121 midió 1 calibre de 5 armas y 0 series; ARGOS 120, 0 series.
3. **La FGE de Guanajuato no publicó cifra de víctimas de Valle de Santiago** pese a ser el hecho de
   mayor gravedad de la entidad en el corte.
4. **Cuatro de los cinco días de la ventana sin agregado federal**, y el único existente **no indexado
   por su propio emisor**.
5. **`fgjem.edomex.gob.mx`**: tres resoluciones sin boletín, quinta verificación.
6. **SSC y FGJ de la Ciudad de México**: cero boletín sobre Tepito, tercera edición.
7. **FGET Tabasco**: sin boletín de las seis ejecuciones del 15-sep, con municipios contradichos.

---

## 14. Deuda de método que ARGOS 122 deja abierta

| Asunto | Estado |
|---|---|
| **La rama del entorno llega desactualizada** | **Decimoséptima vez.** `git merge --ff-only` lo resuelve. **Comportamiento estable, no accidente** |
| **El bloqueo de egreso** | **Tercera edición consecutiva.** Techo ★★★☆☆. `docs/solicitud-lista-blanca-egreso.md` **sin tramitar** |
| **El recall nacional del coordinador** | **Decimotercera edición aportando los hechos de mayor gravedad.** **Cuatro de los cinco rojos del corte.** Los barridos **no vieron ninguno de los tres ataques con víctimas civiles mortales** |
| **El renglón de Michoacán con municipio inexistente** | **Declarado y no integrado.** ARGOS 123 debe fijarlo o retirarlo |
| **Cuatro dominios oficiales mal referenciados** | Oaxaca corregido; Querétaro, Hidalgo y Tlaxcala **sin verificar** |
| **El presupuesto del Centro se excedió en 3 búsquedas** | **Declarado sin atenuar por el propio barrido.** Se registra |
| **Coyame del Sotol puede ser tres eventos, no uno** | **Alerta nueva.** ARGOS 123 debe tratarlo como varios candidatos |
| **San Francisco del Rincón puede ser dos hechos, no una cifra en disputa** | **Alerta nueva.** Cambia la naturaleza del pendiente |


---

## 15. Los dos controles editoriales — ejecutados, y los dos devolvieron hallazgos reales

⚠️ **ARGOS 120 no los ejecutó. ARGOS 121 sí, y los dos devolvieron `CORREGIR ANTES DE PUBLICAR`.
ARGOS 122 los ejecutó como subagentes y los dos volvieron a devolver `CORREGIR ANTES DE PUBLICAR`
con hallazgos reales. La racha se mantiene.**

### 15.1 El hallazgo más grave: Puerto Peñasco no era un evento, eran dos, y su arsenal no se podía contar

`procedencia-cifras` detectó que el descriptor **«rifle cal. .50»** no lo usa ninguna fuente, y que
el borrador **omitía dos ametralladoras**. La verificación propia del coordinador lo confirmó y lo
amplió:

| Lo que decía el borrador | Lo verificado |
|---|---|
| **33 armas largas** | **«MÁS DE 40 armas largas»**, incluidas **2 AMETRALLADORAS MINIMI**. **33 era la cifra preliminar del 20-sep y quedó superada por el relato posterior de la autoridad** |
| **1 «rifle» cal. .50** | **1 AMETRALLADORA BROWNING M-2 CAL. .50** |
| **armas cortas sin numerar** | **CINCO ARMAS CORTAS**, cifra expresa |
| **cartuchos «miles»** | **«casi cuatro mil»** — sigue sin ser cifra |
| **fecha del aseguramiento: 18-sep** | **19-SEP**, en una **SEGUNDA INTERVENCIÓN CON ORDEN DE CATEO** de un **Juez de Control Penal Oral del Primer Distrito Judicial**. El **18** fue el operativo, el tiroteo, la persecución, las **7 detenciones** y el **rescate de 3 víctimas** |
| **sin calibres** | **5.56, .223 y 7.62×39**, publicados **para el conjunto, no por arma** |
| **explosivos sin cifra** | **ARTEFACTOS EXPLOSIVOS IMPROVISADOS** sin cifra: son **AEI**, no explosivos, y van en esa categoría |
| **contexto no registrado** | ⚠️ **El operativo derivó de la investigación del SECUESTRO DE OCHO PERSONAS dedicadas a la MINERÍA ARTESANAL en la región de SIERRA PINTA.** Se rescataron **tres**. **Las otras cinco siguen sin paradero publicado** |

**Correcciones aplicadas, y su efecto en el total nacional**:

- **Armas largas de Sonora**: se integran **solo las 2 Minimi**, única cantidad expresa.
  `«MÁS DE 40» NO ES CIFRA`. **El total nacional de largas baja de 59 a 28.**
  ⚠️ **Es el mayor volumen NO INTEGRADO del corte, y la regla lo exige: preferimos perder 38 armas
  del total antes que sumar una cifra que la propia autoridad superó.**
- **Armas cortas**: **+5**. **El total nacional sube de 5 a 10.**
- **Detenidos**: los **7 son del 18-sep** y el arsenal del **cateo del 19**. La regla cuenta solo a
  los detenidos **en el mismo evento de aseguramiento**: **no se integran**.
  **El total nacional baja de 27 a 20.**
- **Fecha de `ARG-122-ARM-002`**: **19-sep**, no 18.

### 15.2 El descuadre aritmético de la Valoración

`procedencia-cifras` detectó que **«7 muertos y 8 heridos»** no salía de ninguna suma declarada:
la única forma de obtenerlo era **excluir Celaya en silencio y adoptar la cifra alta y no arbitrada
de Valle de Santiago**. ⚠️ **Es decir: la Valoración resolvía por su cuenta una contradicción que la
ficha declara expresamente `NO ARBITRADA`.**

**Corregido**: la Valoración publica ahora **«NUEVE O DIEZ MUERTOS Y TRECE HERIDOS»**, con el rango
declarado, y el recuadro de portada publica **«SEIS O SIETE MUERTOS Y OCHO HERIDOS»** para los dos
ataques a espacios deportivos, también con el rango. **Una cifra contradicha no se cierra en un
agregado.**

### 15.3 La fe de erratas de Coyuca estaba en el cartelón

`procedencia-cifras` señaló que las cifras de Coyuca —**58 largas y 32 cortas**— aparecían en
**«Conclusiones de inteligencia criminal»** y en el recuadro de portada **sin ARG-ID y sin
trazabilidad**, siendo una **corrección a ARGOS 121**.

**Se acepta**: `CLAUDE.md` es explícito en que **no va fe de erratas al cartelón**. **Las cifras se
retiran del cartelón** y viven aquí, en `ARG-122-FE-001`. **La conclusión se conserva sin ellas**,
porque el patrón —**el nivel municipal como unidad capturada**— sí es inteligencia criminal
accionable y no depende de la cifra corregida.

### 15.4 Lo que `editor-duplicidad` corrigió

| Hallazgo | Corrección aplicada |
|---|---|
| ⚠️ **`ARG-122-014` (Angamacutiro) se publicaba como hecho propio**, siendo una cifra que **`ARG-121-REC-005` ya había citado** | **RECLASIFICADO a `ARG-122-REC-002`**, fuera del semáforo y de todos los totales. **El corte pasa de 18 a 17 hechos propios, de 11 a 10 verdes y de densidad 0,21 a 0,19.** ⚠️ **El control señaló además la asimetría con Coyuca**, que se resolvió como fe de erratas siendo la misma situación. **Tenía razón: el tratamiento es ahora simétrico** |
| **El deslinde de Angamacutiro afirmaba «otros municipios»** frente a `ARG-121-REC-005` | ⚠️ **ERA FALSO: los municipios son los mismos.** **Corregido**: «otra fecha y otros detenidos —los municipios SÍ son los mismos, y por eso el deslinde es obligatorio—» |
| **El recuadro de portada decía «TRES PIEZAS CAL. .50»** | **Son DOS** —el Barrett de Los Aldamas y la Browning M-2 de Puerto Peñasco—, más **tres ametralladoras**. **Corregido** |
| **El cuadre de cobertura 4 + 28 + 1 = 33 no se explicaba junto a su tabla** | **Añadida una fila «Universo de revisión: 33 = 32 fiscalías estatales + FGR»** en la propia tabla |
| **Verificó que no se repitiera el fallo de Nonoava** | ✅ **Ningún hecho ya publicado llegó como nuevo.** **El riesgo mayor —los 40 AEI de la sierra frente a los 53 de Mazatlán y los 84 de La Noria— quedó descartado** por fecha, cifra, corporación y modalidad |
| **Verificó la aritmética de armamento fila por fila** | ✅ **Cuadraba entonces y vuelve a cuadrar tras las correcciones**, recalculada de forma independiente por el coordinador |
| **Paridad móvil/escritorio** | ✅ **29 ARG-ID en las tres versiones, conjuntos idénticos** |
| **Forma del cartelón** | ✅ **20 apartados «HECHO» y 20 «TRAZABILIDAD», cero «Corroboración», cero «Explotación ARGOS», tres recuadros, cero `-FE-` en el cuerpo** |

### 15.5 Totales antes y después de los controles

| Renglón | Borrador | Publicado | Motivo |
|---|---|---|---|
| **Hechos propios** | 18 | **17** | Angamacutiro → `-REC-` |
| **Semáforo verde** | 11 | **10** | ídem |
| **Recuperaciones `-REC-`** | 1 | **2** | ídem |
| **Densidad** | 0,21 | **0,19** | 17 ÷ 87,35 |
| **Armas cortas** | 5 | **10** | +5 de Puerto Peñasco |
| **Armas largas** | 59 | **28** | −33 de Puerto Peñasco, +2 Minimi |
| **Detenidos** | 27 | **20** | −7 de Puerto Peñasco, de otro evento |
| **Total de armas integradas** | 65 | **39** | ídem |
| **Muertos de los ataques civiles** | «7 y 8 heridos» | **9 o 10 y 13 heridos** | suma completa, con el rango declarado |

⚠️ **Sin los dos controles, este corte habría publicado 33 armas largas que la propia autoridad
superó, 7 detenidos atribuidos al evento equivocado, un hecho ya citado por ARGOS 121 como hecho
nuevo, un deslinde con una afirmación falsa y un agregado de víctimas que arbitraba en silencio una
contradicción declarada. Los dos controles son obligatorios y esta edición lo confirma.**

---

## 16. Reordenación cronológica — instrucción editorial del destinatario, posterior a la publicación

**Instrucción recibida tras revisar la versión móvil**: *«Solo pon del día de hoy información.»*

**Comprobación previa a ejecutarla, que cambió la decisión**: el corte **no tiene un solo hecho
fechado el 21-sep**. El desglose es **5 hechos del 17 · 6 del 18 · 3 del 19 · 3 del 20 · 0 del 21**,
y la ventana del día de hoy solo abarca de **00:00 a 08:57**. Aplicada al pie de la letra, la
instrucción habría dejado el cartelón **con cero hechos propios**, y los **17 hechos del 17 al 20
—los cinco rojos incluidos— se habrían perdido del archivo**, porque ARGOS 123 abre donde éste cierra
y nadie habría vuelto a mirar ese tramo.

**Decisión del destinatario, consultado con el dato delante**: **conservar la ventana íntegra y
reordenar el cartelón de lo más reciente a lo más antiguo.**

**Lo aplicado**, sin tocar un solo dato, cifra, fuente, deslinde ni clasificación:

| Antes | Ahora |
|---|---|
| Fichas agrupadas **por entidad y región** | Fichas ordenadas **por fecha, de la más reciente a la más antigua** |
| Página 3 abría con **Celaya (18-sep)** | Página 3 abre con **Valle de Santiago (20-sep)** |
| Los renglones del boletín federal del **17-sep** quedaban intercalados | Quedan **agrupados al final**, en las páginas V y VI, con su marca `FRONTERA DE VENTANA` |
| Tabla «Panorama del corte» en orden temático | **Ordenada 20 → 17-sep**, con el orden declarado en su encabezado |
| Las dos recuperaciones, dispersas | **Juntas al cierre del bloque de crimen organizado**, atenuadas |

**Añadido al encabezado del panorama**, porque es dato de trazabilidad y no opinión:
`NINGÚN HECHO DEL CORTE ESTÁ FECHADO EL 21-SEP: LA VENTANA SOLO ALCANZA HASTA LAS 08:57 DE HOY.`

⚠️ **Los totales, el semáforo, la densidad y los ARG-ID no cambian**: 17 hechos, 5/2/10, 0,19
hechos/hora, 29 ARG-ID en las tres versiones. **Es una reordenación de presentación, no una
reedición.** La validación y los dos generadores se volvieron a pasar después.

**Lección para ARGOS 123**: cuando una instrucción editorial, leída al pie de la letra, **vaciaría el
producto**, lo correcto no es obedecerla ni descartarla, sino **poner el dato delante del
destinatario y dejar que decida**. Aquí el dato era que **hoy no había hechos**, y bastó decirlo.

---

## 17. Defecto del generador móvil corregido — encabezados duplicados

**Instrucción recibida**: *«Es muchísima información y se repite dos veces en los reportes de
criminalistas 1 y 2; hay que dejar solo uno y la fecha de la nota.»*

**Diagnóstico**: no era duplicación de contenido, era **un defecto de `tools/gen-movil.py`**.
La herramienta escribía **su propia cabecera corta** (`CRIMEN ORGANIZADO (I)`) y, pegada, **dejaba
intacta la cabecera larga del escritorio** (`CRIMEN ORGANIZADO (I) — LO MÁS RECIENTE DEL CORTE:
DOMINGO 20 Y LUNES 21 DE SEPTIEMBRE`). **Veinte títulos para diez secciones**, dos seguidos en cada
una.

⚠️ **Se corrigió LA HERRAMIENTA, no su salida**, conforme a la regla del archivo. Cuatro cambios:

1. **`limpia()` retira el encabezado de página que duplica el título.** Solo el que usa
   `<h2 style="font-size:14px;">`, que es **exactamente el que `titulo_de()` lee**. Los
   `section-head` internos —«TOTALES DEL CORTE», «INDICADORES OFICIALES», «SEMÁFORO ARGOS»— **no
   llevan ese `h2` y se conservan**: son subtítulos legítimos, no duplicados.
2. **Cada ficha muestra su fecha** en la cabecera, junto a la etiqueta de color: `20-SEP`, `19-SEP`…
   **Se deriva del propio apartado TRAZABILIDAD de la ficha** (`<b>Hecho</b>: 2026-MM-DD`); si una
   ficha no publica fecha, **no se inventa ninguna**.
3. **Cada sección muestra el rango de fechas de sus fichas** junto al número de página.
4. **Dos títulos que desbordaban** la cabecera y la barra de navegación del teléfono se abrevian:
   «CANDIDATOS JUDICIALES NO INTEGRADOS E INDICADOR DE COBERTURA» → **«CANDIDATOS Y COBERTURA»**, y
   «PANORAMA DEL CORTE» → **«PANORAMA»** en la barra.

**Resultado medido**: **de 20 encabezados a 12, uno por sección**, y **19 fichas con su fecha
visible**. **El cartelón de escritorio y el `.txt` no se tocaron**; la validación, la paridad de
29 ARG-ID y los contadores del generador se repasaron después.

**Lección de método**: el destinatario reportó «se repite dos veces» y la lectura literal apuntaba
al contenido. **No era el contenido: era el generador.** Antes de recortar un producto por
duplicación, **comprobar si la duplicación la introduce la herramienta**.

---

## 18. El panorama dejaba de ser un índice en el teléfono

**Instrucción recibida**, con captura de la versión móvil: *«Estos saturan más de información.»*

**Diagnóstico**: la tabla **«Panorama del corte»** tiene **siete columnas**. El generador reflúa toda
tabla de más de cuatro a **tarjetas apiladas con el nombre de cada columna delante de su valor** —regla
correcta, nacida en ARGOS 102 para no perder datos—. Aplicada al panorama producía **veinte tarjetas de
siete campos cada una**: `ENTIDAD · MUNICIPIO`, `HECHO`, `NIVEL DE RIESGO`, `FUENTE INSTITUCIONAL`,
`FUENTE NACIONAL`, `CONFIANZA`, `ARG-ID`.

⚠️ **El panorama dejaba de ser un índice y se convertía en un segundo reporte completo, colocado
delante del reporte de verdad.** En el escritorio no se nota —cada hecho ocupa **una línea**—; en un
teléfono, **ciento cuarenta bloques etiquetados antes de la primera ficha**.

**Corregido en la herramienta**: `tools/gen-movil.py` reconoce el panorama por su firma —**es la única
tabla del cartelón que lleva a la vez «Nivel de riesgo» y «ARG-ID»**; la de armamento tiene ARG-ID pero
no nivel— y lo reflúa a **modo índice**: un renglón compacto por hecho con **entidad y municipio, qué
pasó, su color y su ARG-ID**.

**Los tres campos de procedencia salen del índice móvil, y no se pierde nada**: fuente institucional,
fuente nacional y nivel de confianza viven **íntegros, con su recuento por tipo y sus emisores
nombrados, en el apartado TRAZABILIDAD de la ficha a la que el propio ARG-ID enlaza**, y la tabla de
siete columnas **sigue completa en el cartelón de escritorio**. La nota del bloque lo dice al lector:
*«Toque un ARG-ID para ir a su ficha, donde están las fuentes, el nivel de confianza y los deslindes.»*

**Resultado medido**: **20 renglones de índice**, **cero campos de fuente o confianza** en la sección de
panorama de la móvil, y el archivo baja de **221,022 a 212,625 bytes**. **Escritorio y `.txt`
intactos**; paridad de **29 ARG-ID** y validación repasadas.

**Lección de método, que vale para todo generador**: una regla puede ser correcta en general y **errónea
para un caso concreto**. «Ninguna tabla se pierde, las anchas se reflúan a tarjetas» salvó el módulo de
armamento en ARGOS 102 y **arruinó el índice en ARGOS 122**. La tabla que es un **índice** no se trata
como la tabla que es un **registro**.

---

## 19. Dos tablas salen de la versión móvil, y la paridad se conserva

**Instrucción editorial del destinatario**, con dos capturas: *«Estas quítalas, es demasiada
información.»* Señaló el **índice de panorama** y la **tabla de armamento por evento**.

**Retiradas de la móvil**, en el generador:

| Tabla | Por qué sale | Dónde sigue estando |
|---|---|---|
| **Panorama del corte** — 7 columnas, 20 filas | Cada fila **repite el titular de una ficha** que está unos centímetros más abajo | Íntegra en el **cartelón de escritorio**; cada hecho, en su ficha |
| **Armamento por evento** — 17 columnas, 9 filas | Cada fila **repite el apartado HECHO de su propia ficha** y gasta **siete líneas en categorías con valor cero** | Íntegra en el **cartelón**; los **totales nacionales**, en las tarjetas de conteo de la propia móvil; el desglose de cada hecho, en su ficha |

**NO se retiraron**: la tabla de **totales nacionales del corte** —12 columnas pero **una sola fila**,
y es el agregado que `CLAUDE.md` exige publicar—, ni las de **candidatos** y **cobertura**, que caben
a lo ancho de un teléfono.

### El coste se midió y se eliminó, no se aceptó

Retirar el módulo de armamento del teléfono **costaba cuatro ARG-ID** —`ARG-122-ARM-003`, `-004`,
`-008` y `-009`—, los únicos que **ninguna ficha citaba**. Los otros cinco sobrevivían porque sus
fichas los referencian en TRAZABILIDAD.

⚠️ **Es el fallo que `editor-duplicidad` midió en ARGOS 102**, cuando la móvil reproducía 13 de 27
ARG-ID por retirar tablas anchas. **No se repite aquí**: en vez de aceptar la pérdida, **se añadió la
referencia cruzada que faltaba** a las cuatro fichas —`ARG-122-004` (Los Aldamas), `ARG-122-010`
(Iztapalapa), `ARG-122-011` (Tempoal) y `ARG-122-018` (La Paz)—, en el apartado TRAZABILIDAD, que es
donde viven los enlaces entre fichas.

**Resultado**: **29 ARG-ID en las dos versiones, conjuntos idénticos**, con las tablas fuera del
teléfono. **La trazabilidad no dependía de la tabla: dependía de que cada ficha citara su fila.**
Ahora todas lo hacen, y eso **mejora también el cartelón de escritorio**.

**Peso de la móvil a lo largo de las tres correcciones**: **223,909 → 221,022 → 212,625 → 193,603
bytes**, un **13 % menos** que al publicarse, **sin perder una sola ficha ni un solo ARG-ID**.

⚠️ **La nota de cierre de la móvil se corrigió**: afirmaba *«no se omitió ni resumió ninguna
tarjeta»*, que tras esta retirada **habría sido falso sobre las tablas**. Ahora declara qué dos no se
publican, por qué no se pierde nada y que **ninguna ficha se omitió**. **Un producto que se describe
mal a sí mismo no es auditable.**
