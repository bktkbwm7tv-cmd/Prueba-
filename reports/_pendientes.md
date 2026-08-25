# ARGOS — Pendientes vivos

Archivo de traspaso entre ediciones. **Cada corte lo actualiza como último paso**, antes de commit.
Sirve para que una sesión nueva pueda arrancar sin que nadie tenga que recordar ni transcribir la
lista de seguimientos: basta leer este archivo y la edición anterior.

Convención: cada entrada indica desde qué edición está abierta, qué hay que buscar y qué la cierra.
Cuando algo se resuelve, se mueve a "Cerrados recientemente" con una línea, y se borra de ahí en la
segunda edición siguiente.

**Última actualización**: ARGOS 107 (corte 2026-08-25).

---

## Arranque de la edición siguiente

**`reports/_arranque-ARGOS-108.md`** contiene la orden de arranque para una sesión nueva: verificación
de base antes de numerar, ventana, deuda heredada, trampas ya verificadas y comandos de construcción.
**Escribirlo es el último paso obligatorio de cada corte**, junto con la actualización de este archivo:
sin él, la edición siguiente arranca a ciegas — que es exactamente lo que le pasó a ARGOS 106.

## Instrucción editorial permanente — la forma del cartelón

Fijada por el destinatario en ARGOS 105, tras revisar la edición en teléfono. **Rige por encima de
cualquier otra consideración de formato.**

| Regla | Detalle |
|---|---|
| **Solo el día** | El cartelón publica **únicamente hechos de su propia ventana**. Las recuperaciones de ventanas anteriores, las fes de erratas y los hallazgos de auditoría van al **archivo de fuentes y a este documento**, nunca al cartelón |
| **Sin «Ejes del día»** | La sección se retiró. Cada hecho aparece **una sola vez**, en su ficha. Las tablas de módulo (detenciones, armamento, sentencias) aportan **campos distintos** —cifras, corporación, pena—, no repiten el titular |
| **Sin exposición sobre ARGOS** | Nada de presupuesto de búsqueda, ciclos, agentes, `grep`, cobertura del instrumento ni autorreferencia. Las excepciones de trazabilidad —declaración de ventana, casillas de cobertura, contradicciones— se escriben **en una línea**, no en párrafos |
| **Iconografía de armamento** | Cada categoría de la taxonomía lleva icono propio, monocromo y de trazo, en las tarjetas de conteo y en las cabeceras de la tabla. **Siempre con etiqueta y cifra**, nunca identificando solo. Las categorías en cero se muestran atenuadas: la ausencia es dato. Fijado en `CLAUDE.md` desde ARGOS 105 |
| **Explicación al mínimo** | Es un análisis para un mando: hecho, entidad, municipio, fecha, cifras con su desglose, fuente, confianza y ARG-ID. Lo demás sobra |

---

## ARGOS 107 — lo que abre esta edición

### Seguimientos nuevos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 107 | **Poza Rica — el periodista sustraído** (`ARG-107-001`) | **Localización de Elí Martínez.** Línea perecedera y de máxima prioridad: la sustracción con vida, a diferencia de un homicidio, deja ventana de rescate. Sin boletín de la FGE de Veracruz ni de la SSP | Un boletín institucional y el cruce de las **tres carpetas de agresiones a reporteros de la fuente policiaca en Poza Rica en 2026** (enero, junio, agosto) por autoría, arma y zona |
| ARGOS 107 | **Poza Rica — el patrón de gremio** (`ARG-107-001`) | Acreditar o descartar autoría común entre las tres agresiones. Hoy solo consta la coincidencia de gremio, fuente y municipio; **no se afirma vínculo** | La balística cruzada y el tema común de las últimas publicaciones de los tres comunicadores |
| ARGOS 107 | **Mazatlán — la central de autobuses** (`ARG-107-002`) | **Video de andenes y taquilla** y **manifiestos de pasajeros** de las corridas arribadas entre 16:00 y 17:00 h del 24-ago. Sin ellos no puede probarse el señalamiento previo del arribo | El registro de la terminal. Determina si el eslabón está dentro de la central o en el origen del viaje |
| ARGOS 107 | **Candela — la fecha** (`ARG-107-003`) | ⚠️ `FECHA DEL HECHO NO ANCLADA EN RUTA`. La URL fija el año 2026, no el día; el 25-ago procede del resumidor. **Se integró a esta edición con la marca** | Una URL con día en la ruta. **Si resulta anterior al 24-ago 09:15, se retira por fe de erratas** del conteo de ARGOS 107 |
| ARGOS 107 | **Candela — identidad del abatido** (`ARG-107-003`) | Nombre y **plaza de origen** del civil abatido: es lo único que ubicaría la estructura que intentaba cruzar. Armamento asegurado no publicado | Un boletín de la SSP o de la FGE de Coahuila |
| ARGOS 107 | **El inhibidor de drones, segundo del archivo** (`ARG-107-REC-003`) | **Marca y lote** del inhibidor del megaoperativo. El de Huajicori, Nayarit (12-ago) era de origen chino, marca **Tatusky Technology**. Dos en trece días apuntan a **difusión de la contramedida**, hipótesis sin validar | El desglose técnico del aseguramiento. Si coinciden marca y lote, hay canal de abastecimiento común |
| ARGOS 107 | **Megaoperativo CJNG — desglose por entidad** (`ARG-107-REC-003`) | Las cifras —20 detenidos, 10 armas, 113 vehículos— son **agregadas para Hidalgo, Jalisco y Michoacán**. Sin desglose no puede medirse el peso de cada plaza | El boletín de la SSPC o de la FGR. También el **estatus legal de los 113 vehículos**, que es la vía patrimonial más directa |
| ARGOS 107 | **Mazatlán — fracc. Petróleos Mexicanos** | Indicio **real pero no fichado**: ataque atribuido a la noche del 24-ago, **fuente única sin fecha en ruta**, y los titulares mezclan un saldo de jornada con un hecho puntual | Una URL fechada y un saldo deslindado. `NO INTEGRADO — PENDIENTE DE ANCLA FECHADA` |
| ARGOS 107 | **Chihuahua — carretera a Ojinaga** | «Emboscada con fusiles .50 contra policías estatales»: fuente regional única, sin fecha fijable ni corroboración. **No se ficha ni se descarta** | Una segunda fuente con fecha. Sería 🔴 si se acreditara |

### Deuda de método abierta por ARGOS 107

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 107 | **La cobertura es por entidad, no por portal** | 32 de 32 entidades **consultadas**, pero dentro de varias quedaron portales sin ver: SSP y policías estatales de Noroeste (5), Occidente (4) y Sureste (6), mesas de paz de Noreste y Sureste, y SEDENA/SEMAR/FGR regionales. **Declarados `NO REVISADA`.** Por la regla de prioridad, encabezan el triaje de ARGOS 108 |
| ARGOS 107 | **Tres dominios de fiscalía sin confirmar** | **Tlaxcala, Nayarit y Guanajuato**: no se localizó el dominio oficial. Se sustituyó Guanajuato por `boletines.guanajuato.gob.mx`, sustitución declarada. **Hallazgo reutilizable**: el dominio real de Colima es `fgecolima.mx`, no `fiscalia.colima.gob.mx` |
| ARGOS 107 | **El renglón de Los Reyes de Salgado aparece en dos boletines** | Las mismas cifras (5 largas, 5 cargadores) figuran atribuidas al boletín federal **del 19-ago** (pendiente de ARGOS 104) y al **del 21-23 ago** (barrido de esta edición). **No se cerró el pendiente**: arbitrar sin lectura directa produciría un dato peor. Lo cierra la lectura del boletín |
| ARGOS 107 | **El Ciclo C rindió defensivamente, no ofensivamente** | Occidente y Sureste encabezaron el triaje judicial y **no produjeron una sentencia integrable**, a diferencia de ARGOS 101 (Durango). Sí evitaron **dos falsos positivos** —la vinculación de Oaxaca del 24-ago, que estaba **dentro de ventana**, y el candidato de Jiquilpan— e inventariaron dominios. **Se registra sin inflarlo.** A ARGOS 108 le toca el **Ciclo A (Noroeste + Centro)** |
| ARGOS 107 | **Los dos controles editoriales siguen ejecutándose a mano** | `editor-duplicidad` y `procedencia-cifras` se ejecutaron manualmente con el mismo criterio, y **ambos produjeron hallazgos reales**. La autorización de subagentes de esta sesión cubrió los seis barridos; los controles no se invocaron como agentes y así se declara |

## ⚠ ARGOS 106 — DOS HALLAZGOS QUE CAMBIAN LA SERIE

### 1. La causa raíz de por qué cada sesión arranca desactualizada

**El HEAD por defecto del repositorio es `claude/argos-criminal-intelligence-otiawj`, que solo llega
a ARGOS 88.** La sesión de ARGOS 106 clonó eso y estuvo a punto de publicar un «ARGOS 89» —edición
que no existe ni debe existir—, con ventana solapada, sin versión móvil (`tools/gen-movil.py` no
existe en esa rama) y con el método de ARGOS 88.

| Referencia | Archivos en `reports/` | Última edición |
|---|---|---|
| `main` | 2 | anterior a ARGOS 87 |
| `claude/argos-criminal-intelligence-otiawj` (**HEAD por defecto**) | 8 | ARGOS 88 |
| rama de la edición vigente | 59+ | ARGOS 105 |

**No es una incidencia de una sesión: es la deuda «Mergear las ramas de edición a `main`», abierta
desde ARGOS 102, manifestándose.** Mientras el HEAD por defecto apunte a ARGOS 88, *toda* sesión
nueva heredará el mismo fallo.

**Acción ejecutada en ARGOS 106, autorizada por el destinatario**: mergear las ramas de edición a
`main`. **Regla nueva, de coste cero**: el primer paso de cada corte es comprobar contra qué punto de
la serie se está trabajando —`git ls-remote --heads origin` y `ls reports/`— antes de numerar la
edición. Numerar a partir de lo que la rama local tenga a la vista es lo que produjo el falso 89.

### 2. ARGOS 105 dejó cuatro hechos rojos sin publicar en su propia ventana

`grep` sobre todos los `-fuentes.md` confirma que **ninguna edición de la serie los registra**:

| ARG-ID en 106 | Hecho | Fecha |
|---|---|---|
| `ARG-106-REC-001` | **Acapulco** — comando con chalecos rotulados «Guardia Nacional» asesina a **4 integrantes de una familia** | 22-ago (o 21, contradicha) |
| `ARG-106-REC-002` | **Morelia** — balacera con elementos de la GN de civil; 2 muertos, 2 federales asegurados | 22-ago |
| `ARG-106-REC-003` | **Los Bayados, Ajuchitlán** — ataque de ~8 h contra la comunidad | 21-ago |
| `ARG-106-REC-004` | **«El Willy», Casas Grandes** — nuevos restos óseos | 20-ago |

**ARGOS 105 publicó «cero eventos rojos». Con estos cuatro, esa afirmación no se sostiene**: su
semáforo queda corregido por fe de erratas a **4 🔴 y 1 🟡**. El archivo antiguo no se reescribe.

**Es un cuarto modo de fallo**, distinto de los tres conocidos: no es de búsqueda, ni de registro, ni
de continuidad de ventana. ARGOS 105 declaró **32 de 32 entidades revisadas** y aun así no localizó
una masacre de cuatro víctimas en Acapulco ni un homicidio con participación de personal federal en
Morelia. **Es un fallo de recall dentro de una cobertura declarada completa.** Una cobertura del
100% de portales no garantiza el 100% de los hechos cuando los portales institucionales están
bloqueados y el barrido depende del buscador.

**Acción para ARGOS 107**: cuando una región se declare revisada sin hallazgos, contrastar con una
**consulta genérica por entidad sin restricción de dominio** («ataque armado \<entidad\> \<fecha\>»)
antes de cerrarla. Es lo que hizo aparecer estos cuatro hechos.

## Seguimientos abiertos por los hechos de ARGOS 106

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 106 | **Morelia — los dos elementos de la GN asegurados** (`ARG-106-REC-002`) | ⚠️ **ARGOS 107 lo persiguió con cuatro búsquedas dirigidas: `SIN RESULTADO INDEXADO EN VENTANA`.** El estado más reciente verificable **sigue siendo el del 22-ago**: investigación en la **FGE de Michoacán, fuero común**; la **FGR podría atraerla** si la GN confirma la adscripción de los detenidos, confirmación que **no se ha producido**. **Ninguna fuente menciona fuero militar.** No hay liberación temprana ni traslado | El comunicado de adscripción de la GN, o el auto de vinculación. **El estancamiento es en sí mismo el dato**: siete días sin definición de fuero en un homicidio con presunta participación de personal federal |
| ARGOS 106 | **Acapulco — los chalecos** (`ARG-106-REC-001`) | **Sigue sin pronunciamiento de la GN** sobre el uso de sus insignias, y sin boletín de la FGE Guerrero (verificado de nuevo en ARGOS 107). Procedencia de los chalecos, sin cruzar con uniformes reportados como perdidos o robados en Guerrero | Un boletín de la FGE Guerrero y el deslinde de la GN |
| ARGOS 107 | ⚠️ **Acapulco — el «agresor herido en el tórax» PUEDE SER UNA CONFLACIÓN** (`ARG-106-REC-001`) | **Hallazgo de ARGOS 107, y reformula el pendiente anterior.** El único herido de tórax localizable es **Ernesto Manuel (41), dueño de un taller mecánico en El Quemado**, descrito por las fuentes como **víctima de un ataque distinto** —el del taller—, **no como agresor** de la masacre de La Estación. **No se localizó ninguna fuente que documente a un agresor herido en el tórax en La Estación** | **Acreditar primero el origen del dato** en el archivo de ARGOS 106 —¿de qué fuente salió?— antes de gastar una búsqueda más en el rastreo hospitalario. *Un pendiente que dirige búsquedas durante varias ediciones sobre una premisa no acreditada es más caro que un vacío declarado* |
| ARGOS 106 | **Mazatlán como concentrador** (`ARG-106-001/003/004`) | Tres de los ocho hechos de la ventana en el mismo municipio: ataque con 2 muertos, 3 AEI y un fusil de asalto. **Lectura por municipio, no por evento** | El registro completo de eventos del municipio en agosto, para confirmar o descartar disputa territorial activa en el eje rural-portuario |
| ARGOS 106 | **Sinaloa — registro consolidado de AEI de agosto** (`ARG-106-003`) | Los 3 AEI se suman a los 303 de El Rosario (18-ago) y al laboratorio con la discrepancia 72/172. **Sin desglose por municipio no se distingue expansión del fenómeno de intensificación del rastreo** | Un registro consolidado de la SEMAR |
| ARGOS 106 | **Colima — ¿carpetas acumuladas?** (`ARG-106-002`) | Dos ataques sobre el mismo núcleo familiar en 48 h y en la misma colonia. Sin móvil oficial, sin detenidos, sin medidas de protección publicadas | Si la FGE Colima los trata como hechos separados, **eso mismo es el hallazgo** sobre su capacidad de detección de series |
| ARGOS 106 | **Los Bayados — desplazamiento** (`ARG-106-REC-003`) | **Conteo de salidas de familias en los 7 días posteriores al 21-ago**: mide el éxito o fracaso del despliegue. La denuncia de **drones** sigue sin confirmación institucional y no se contabiliza | El registro estatal de desplazamiento interno |
| ARGOS 106 | **«El Willy» — corte numérico único** (`ARG-106-REC-004`) | Acumulado `EN CONFLICTO` entre **56 y ~100**. Sin denominador confiable no hay medición de avance forense | Un corte de la FGE Chihuahua: restos localizados / individualizados / identificados / entregados |
| ARGOS 106 | **Nopaltepec — el expolicía** (`ARG-106-007`) | Periodo de servicio y causa de baja de Diego Vladimir "N"; si otros elementos de la misma corporación figuran en la carpeta; destino de los vehículos. **Fuente única nacional** | Un boletín de la FGJEM y una segunda fuente |
| ARGOS 106 | **CDMX — colonias no publicadas, segunda edición consecutiva** (`ARG-106-008`) | Como `ARG-105-005`, el hecho **no puede cruzarse con el mapa de incidencia** por falta de colonia | El desglose por colonia de la FGJ CDMX para robo a casa habitación en agosto |
| ARGOS 106 | ~~**72 vs. 172 AEI — Sinaloa**~~ | **CERRADO POR RETIRADA en ARGOS 107** (`ARG-107-FE-001`). Tercera edición sin que aparezca el boletín primario: `site:gob.mx/sedena` con los términos del hecho **no lo devolvió**. Se aplica el umbral de cifras arrastradas | Ver «Cerrados recientemente». **No reabrir sin lectura directa del boletín** |
| ARGOS 106 | **Sonora — pena compuesta** (`ARG-106-SEN-REC-001`) | 28a 3d «para dos sujetos», **sin precisar si es por persona o conjunta**. No sumable | El boletín de la FGJE Sonora. Si es por persona, el acumulado sube 56 años |

## Deuda de método abierta por ARGOS 106

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 106 | ~~**Cobertura real: 5 de 32 entidades**~~ | **SALDADA en ARGOS 107**: se lanzaron los seis `barrido-regional` en paralelo y quedaron **32 de 32 entidades consultadas**. Ver la deuda nueva de ARGOS 107: la cobertura es **por entidad, no por portal** |
| ARGOS 106 | ~~**El Ciclo C no se aplicó**~~ | **APLICADO Y DECLARADO en ARGOS 107**: Occidente y Sureste encabezaron el triaje judicial; las otras cuatro regiones, armamento. Rendimiento registrado en `argos-2026-08-25-fuentes.md`. **A ARGOS 108 le toca el Ciclo A (Noroeste + Centro)** |
| ARGOS 106 | **Los tres controles no se invocaron como subagentes** | `editor-duplicidad` y `procedencia-cifras` se ejecutaron **a mano** con el mismo criterio y ambos produjeron hallazgos reales; `barrido-regional` no se ejecutó. La ausencia se declaró en el indicador de cobertura en vez de disimularse |
| ARGOS 106 | **Un *liveblog* volvió a ser fuente única** | `ARG-106-008` (Tláhuac) descansa en el minuto a minuto de Infobae. Se integró por bajo impacto y coincidencia con el día de publicación, **marcado `PENDIENTE DE CORROBORACIÓN INDEPENDIENTE`**. La regla de ARGOS 103 sigue vigente: un *liveblog* no fecha un hecho |

## Seguimientos abiertos por los hechos de ARGOS 105

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 105 | **Jalisco — Octavio Haro Cachúa** (`ARG-105-001`) | **Publicado.** Reporte de desaparición 11-ago, cuerpo hallado 19-ago en La Venta del Astillero, peritajes 21-ago, identificación 22-ago. La FGE declara móvil «de carácter personal» y reporta avances para órdenes de aprehensión. ⚠️ **Causa de muerte NO PUBLICADA** y **sin boletín propio** de `fiscalia.jalisco.gob.mx` | La causa de muerte, el boletín institucional y las órdenes de aprehensión cuando se cumplimenten |
| ARGOS 105 | **Jalisco — los otros dos empresarios inmobiliarios** | **Ricardo Cabezas Talavera** y **César Ríos**, reportados como no localizados en las tres semanas previas. La FGE sostiene que los tres casos son **independientes** | **Encargo para ARGOS 106**: cruzar los tres expedientes por desarrollos, socios y predios en litigio en el corredor Zapopan–carretera a Nogales. Si hay patrón, cambia la clasificación de los tres |
| ARGOS 105 | **Campeche — la avioneta de Champotón** (`ARG-105-002`) | Matrícula, bitácora y planes de vuelo **no publicados**; origen de los 3,000 L de turbosina, sin determinar; sin comunicado primario de `fgr.org.mx` | El comunicado de la FGR y el registro aeronáutico. Es la línea de mayor rendimiento del corte |
| ARGOS 105 | **Los Mezcales — dos capturas en 36 horas** | "El Pirul" en Colima (`ARG-104-005`) y **"El Abulón" en Oaxaca** (`ARG-105-003`), segundo al mando, residiendo a 1,200 km de su plaza | Estado procesal de la causa de 2023 de "El Abulón" —que explica cómo estaba en libertad— y mapeo de arrendamientos en fraccionamientos privados de Oaxaca de Juárez |
| ARGOS 105 | **Nayarit — los 6 AEI de La Yesca** (`ARG-105-007`) | `FRONTERA DE VENTANA — FECHA NO FIJADA`: podría ser del 20-ago. **Fuente única** (NTV), sin comunicado institucional; tipo de AEI y número de armas no publicados | Un ancla fechada o el comunicado. Si resulta del 20-ago, se retira del total por fe de erratas |
| ARGOS 105 | **CDMX — las alcaldías de la banda de robo a casa habitación** (`ARG-105-005`) | Sin alcaldías ni colonias publicadas, el hecho **no puede cruzarse con el mapa de incidencia**. Sin fuente institucional localizada | Un comunicado de la FGJ CDMX |
| ARGOS 105 | **Campeche — el desglose fino de Champotón** (`ARG-105-002`) | Los **3,000 L de turbosina**, el desglose 5 largas / 3 cortas, los 12 cargadores, las miras, los chalecos y los $777,750 **no se confirmaron con fragmento titulado**: solo con síntesis del buscador, reiterada en tres consultas. Con título citable están la avioneta, los 61 vehículos, los 5,912 L y los 6 detenidos | El comunicado de la FGR. ⚠️ **`WebFetch` está bloqueado también para dominios de medios**, no solo para `*.gob.mx`: eso reduce lo verificable a los títulos |
| ARGOS 105 | **Veracruz — el agregado de 36 resoluciones judiciales** | 5 condenatorias y 31 vinculaciones **sin desglose nominal**; además `CONTRADICHA`: «24 horas» frente a «este fin de semana» | El desglose caso por caso |
| ARGOS 105 | **Tabasco — «más de 200 años», resumen del 18 al 22 de agosto** | **CERRADO como fuera de ventana.** Es un **acumulado de varias personas**, no una pena única, y el **orden del correlativo lo fecha en 2025**: el boletín `37454` ya estaba localizado el 20-ago-2026, mil identificadores por encima de `36454`. **No reabrir** | — |
| ARGOS 105 | **Chiapas — posible subregistro de `ARG-104-003`** | La cobertura del 20-ago describe **8-9 detenidos en cuatro puntos** de Tapachula; la ficha registró solo Puerto Madero (4 detenidos, 3 largas). **No se tocó el archivo sin lectura directa** | Una fuente que desglose los cuatro puntos |
| ARGOS 105 | **Nuevo León — sentencia de 31 años 3 meses (Rincón de Mitras)** | Francisco "N" y Pedro "N", homicidio calificado y tentativa, hecho de sep-2023. ⚠️ **No queda fuera por la ventana** —la regla de frontera la asignaría a ARGOS 105—, sino por **fuente periodística única sin comunicado de la FGJNL** | Un post de `@FiscaliaNL`. **Es la sentencia integrable más cercana que tiene la serie**: en cuanto aparezca fuente oficial, entra con 31 años 3 meses |

## Deuda de método abierta por ARGOS 105

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 105 | **La serie tiene al menos un intervalo que ninguna edición cubre** | Hallazgo nuevo, y es un **tercer modo de fallo**, distinto de los dos conocidos. No es de búsqueda (el hecho no se encuentra) ni de registro (se encuentra y no se ficha): es **de continuidad de ventana**. El multihomicidio de Saltillo (`ARG-105-REC-001`) ocurre la **tarde del 4-ago**; **ARGOS 88 cerró a las 07:15 de ese día** y la ventana declarada de **ARGOS 90 abre el 5-ago**. **No existe ARGOS 89.** El hecho no fue omitido por nadie: cayó entre dos ediciones. **Acción**: recorrer las ventanas declaradas de toda la serie y **listar los intervalos sin cobertura**. Es trabajo de `grep` sobre los archivos de fuentes, **no cuesta búsquedas**, y cada hueco que aparezca es un tramo donde la serie no puede afirmar nada |
| ARGOS 105 | **Tres «vacíos» del archivo no lo eran** | El contraste con `grep` sobre todo el repositorio desmintió **tres acusaciones de omisión** heredadas: los **funcionarios de Medio Ambiente del Edomex** (acusación de ARGOS 97) estaban publicados como `ARG-94-003`; los **19 sentenciados de Tizapán el Alto** (acusación de ARGOS 98) estaban publicados como `ARG-94-SEN-002`; y **Apatzingán** ya lo había anulado ARGOS 98. **Dos pendientes vivos descansaban sobre una premisa falsa.** **Acción**: antes de heredar un pendiente, comprobar que el hecho que lo motiva no está ya en el archivo. Cuesta un `grep` |
| ARGOS 105 | **Un `grep` solo sirve si se leen sus resultados** | El control `procedencia-cifras` descubrió que `ARG-105-REC-007` iba a publicar la versión de ARGOS 98 de Pesquería **sin cotejar `ARG-102-FE-004`**, que ya la había reconciliado mejor. **El `grep` de PRIORIDAD 1 sí devolvió esa línea**, y el coordinador no la siguió. No falta un control: falta **leer lo que el control devuelve**. Cuando una consulta devuelva una fe de erratas o un `-FE-` sobre el hecho que se está fichando, **es de lectura obligatoria antes de redactar** |
| ARGOS 105 | **El orden del correlativo fecha un portal clase C** | El boletín de Tabasco `/Boletin/Index/36454` parecía de agosto de 2026 y es de **2025**: bastó compararlo con el `37454`, que el archivo ya había localizado el 20-ago-2026, **mil identificadores por encima**. En portales de ID correlativo sin fecha, **un boletín ya fechado en el archivo acota a todos los de numeración inferior**. No cuesta búsquedas y evita una trampa de aniversario |
| ARGOS 105 | **Un motivo de exclusión mal escrito es un error, aunque la exclusión sea correcta** | La sentencia de Nuevo León se excluyó «por la ventana», y ese motivo era falso: por la regla de frontera le habría correspondido a esta edición. El motivo real era la falta de fuente oficial. **Excluir bien por la razón equivocada deja el archivo con una regla mal aplicada** que la edición siguiente hereda |
| ARGOS 105 | **Un deslinde escrito en la ficha tiene que llegar también al total** | La ficha de Uruapan declaraba que sus 12 vinculados **no se contabilizan como detención nueva** —son personas ya detenidas en ARGOS 95— y el total de la página **las sumaba igual**: 42 en vez de 30. El texto y la aritmética se contradecían en la misma página. **Cuando una ficha excluye algo de un conteo, hay que comprobar que el conteo lo excluye de verdad** |
| ARGOS 105 | **El resumidor no solo confunde años: inventa futuros** | Patrón **nuevo**, distinto de la trampa de aniversario. Para el racimo de Jiutepec, Morelos, el resumen atribuyó fechas del **25, 26 y 28 de agosto de 2026**, **posteriores al día del corte**: hechos que no pueden haber ocurrido. Se descartó el racimo íntegro. **Comprobar que ninguna fecha sea posterior a la del corte** es un control de coste cero que debe hacerse siempre |
| ARGOS 105 | **La trampa de año que estuvo a punto de entrar como el hecho rojo del corte** | El resumidor presentó como del **22-ago-2026** el enfrentamiento de **Doctor Coss, Nuevo León** (12 abatidos). Las URLs primarias lo sitúan en **2025**. Sin la verificación se habría publicado el hecho más grave del corte, y sería falso. **Ninguna cifra de abatidos entra sin URL con año en la ruta** |
| ARGOS 105 | **El Ciclo B no acertó, y conviene registrarlo** | Noreste y Golfo encabezaron el triaje judicial y **ninguno halló sentencia**; la única del corte apareció en **Querétaro**, que encabezaba con armamento. **Dos éxitos consecutivos no hacen una regla.** A ARGOS 106 le toca el **Ciclo C (Occidente + Sureste)** |
| ARGOS 105 | **Tercer fallo del generador móvil, y la causa es siempre la misma** | La conversión de listas a tarjetas exigía **dos `<span>` tras la etiqueta** —texto y ARG-ID—. Una lista sin ARG-ID, como las Conclusiones, hacía que cada ítem **se comiera el siguiente**: en la móvil desaparecieron **tres de las siete conclusiones**. Corregido, con validación que falla si una tarjeta queda sin texto. **Los tres fallos del generador de esta edición comparten causa: suponer una estructura que la edición puede cambiar.** Antes de dar por buena una móvil, comparar el **número de ítems de cada lista** entre las dos versiones |
| ARGOS 105 | **El generador móvil: corregido, y la lección se repite** | El ancla de inyección de los SVG exigía el título **literal** `SEMÁFORO ARGOS`; esta edición lo matizó con un sufijo y la móvil salió **sin radar, sin mapa y con los `sem-item` en crudo**, en silencio salvo por la validación. Corregido para tolerar sufijos, y el validador ya no exige 3 SVG fijos —una edición sin aseguramientos lleva 2 legítimamente—. **Se corrigió la herramienta, no su salida**, y la corrección beneficia a todas las ediciones futuras |

## Seguimientos judiciales abiertos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 105 | **Nuevo León — Santa Catarina, 31 años 3 meses** | **Candidato de frontera, a un día de la ventana.** Francisco "N" y Pedro "N", homicidio calificado y tentativa por el ataque de **Rincón de Mitras**; publicado el **20-ago** (`mvsnoticias.com/nuevo-leon/2026/8/20/`). **Sin comunicado de la FGJNL localizado** | El boletín de la FGJNL, que **comunica por Facebook y X (`@FGJNL`), no por portal**. Mientras no exista: `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR` |
| ARGOS 101 | **Durango — Lerdo** (`ARG-101-SEN-001`) | **Pena exacta y firmeza: siguen sin obtenerse.** Continúa en «más de 26 años», **no sumable**. Duplicidad ya interceptada en ARGOS 104: un solo boletín bajo dos rutas, no dos condenas | Lectura directa o segunda fuente. ⚠️ **Va camino del mismo umbral que acaba de retirar el detalle de Durango/Gómez Palacio**: si llega a dos ediciones más sin respaldo, se retira |
| ARGOS 102 | **Coronango, Puebla** (`ARG-102-SEN-REC-001`) | ⚠️ **Contradicción abierta**: un medio publica **23 años** frente a **26 a 7 m 15 d**. `CONTRADICHA — reportar ambas`. Las **212 UMA siguen `SIN ANCLA DOCUMENTAL`** y **no se convierten a pesos** | Lectura directa del boletín de la FGE de Puebla. Ancla fechada ya obtenida: `intoleranciadiario.com/…/2026/08/11/` |
| ARGOS 99 | **SLP — Matlapa**, Elías "N" | Cuatro URL localizadas, **ninguna fechada**. Delito preciso: lesiones doblemente agravadas, hecho de ago-2024, procedimiento abreviado, 2 años 8 meses | El boletín de la FGE SLP. **El término jurídico está expreso; lo que falta es la fecha** |
| ARGOS 99 | **QRoo — Playa del Carmen**, 50 años (`ARG-103-SEG-001`) | Fechado el **12-ago**, fuera de toda ventana cubierta. Sin boletín de `fgeqroo.gob.mx` | **No integra. No reabrir salvo que aparezca fuente oficial** |
| ARGOS 99 | **Tabasco — Cunduacán**, Miguel "N" (`ARG-103-SEG-002`) | El boletín cubre Centro, Cárdenas y Cunduacán, pero **no devolvió su `id`** | ⚠️ **No gastar más búsquedas**: cuatro ediciones y once `id` demuestran que `/Boletin/Index/<id>` **no es resoluble por buscador** |
| ARGOS 102 | **Sonora — Nogales: 21 a 7 m 15 d a dos personas** | Reconfirmado con dos URLs fechadas en ruta (`eldiariodesonora.com.mx/…/2026/08/12/`, `telemax.com.mx/blog/2026/08/12/`): el hecho es del **12-ago** | **Confirmado fuera de toda ventana reciente.** Candidato de la ventana de ARGOS 96 |
| ARGOS 102 | **Sinaloa — 50 años a Wilberth "N" por secuestro agravado** | Verificado con `grep`: no figura en ninguna edición. Publicación **15-ago** con fecha en ruta | Boletín de la FGE de Sinaloa. `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR`. **Candidato a omisión de la serie 98/99** |
| ARGOS 96 | **Ruffo Appel / Ingemar**, huachicol fiscal (`ARG-98-SEG-001`) | Último movimiento: **Rigoberto Blanco Cantú se entregó en EU** (red Farías / Mefra Fletes), publicado el 20-ago con fecha en ruta | Sentencia de amparo de fondo. **No aporta línea a ningún conteo** |
| ARGOS 101 | **Guerrero — 5 sentencias** y **Guanajuato — 36 sentenciadas** | Sin avance. Agregados **sin desglose nominal**; el de Guanajuato es **anual** | El desglose caso por caso |

## Vacíos de publicación que siguen sin resolverse

| Desde | Caso | Estado |
|---|---|---|
| ARGOS 105 | **Tijuana — el número de víctimas de `ARG-105-REC-002`** | `CANTIDAD NO PUBLICADA`. La FGE de BC **no descartó más de una víctima** y no se localizó identificación forense posterior. **Contradicción de colonia abierta**: Hipódromo (titulares de dos regionales) frente a «20 de Noviembre» (resumen de buscador), `CONTRADICHA — no fundir`. Lo cierra un boletín de `fgebc.gob.mx` con **dos campos individualizadores** |
| ARGOS 105 | **Saltillo — la hora de `ARG-105-REC-001` y el término jurídico exacto** | La hora sigue en «por la tarde»; el rango 14:30-15:30 h **procede de un resumen y no se consigna**. El término oscila entre **«homicidio calificado»** y **«homicidio agravado»**, ambos atribuidos a la Fiscalía: `CONTRADICHA`. Lo cierra la lectura directa de `sitio.fgecoahuila.gob.mx/2026/08/05/` o `/2026/08/06/`, **ambos con fecha en la ruta** |
| ARGOS 105 | **Cuatro de los ocho hechos recuperados no tienen boletín institucional localizable** | Tijuana, Pesquería, Teotihuacán y el conjunto veracruzano descansan en fuentes periodísticas coincidentes, con la institucional acreditada **solo de forma indirecta**. Lo cierra la petición formal a **FGE Baja California, FGR Nuevo León, FGJEM y FGE Veracruz** |
| ARGOS 105 | **Tamaulipas — choque Ejército/civiles armados atribuido al 21-ago** | Único indicio con fecha potencialmente **dentro** de la ventana del corte. **Fuente abierta única** (Blog del Narco), sin municipio, sin cifras y sin corroboración. `NO OFICIAL — PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL`. No se integra ni se descarta |
| ARGOS 105 | **Pesquería, NL — el oleoducto retirado** | `ARG-105-REC-007` publicó el hecho **sin «1 oleoducto»**, porque la reconciliación `ARG-102-FE-004` —cuatro URLs con fecha en ruta— **no lo recoge**, mientras que la lectura heredada de ARGOS 98 sí. `CONTRADICHA — no se funden`. Lo cierra el comunicado de la **FGR** sobre el cateo del predio **Dulces Nombres** del 12-ago |
| ARGOS 105 | **Veracruz — el conteo de fuentes de `ARG-105-REC-003` y `-004`** | «Más de nueve» y «siete» fuentes regionales nacen en ARGOS 97 **sin nombrar una sola cabecera** y no han podido recontarse. Publicado como `CONTEO DE FUENTES NO VERIFICABLE`. **El hecho subyacente no depende de ello.** Lo cierra enumerar las cabeceras, si alguna edición vuelve sobre el caso |
| ARGOS 104 | **Occidente en el boletín federal del 19-ago** | Los renglones de **Romita (Gto.), Tlajomulco (Jal.) y Los Reyes de Salgado (Mich., 5 largas y 5 cargadores)** siguen sin integrarse: sin URL fechada que los ancle. `PENDIENTE DE ANCLA FECHADA` — lo cierra una consulta al boletín **por título sin restricción de dominio** |
| ARGOS 104 | **Veracruz — el bloque de hechos graves del agregador** | Cuerpo desmembrado en Coatzintla, cabeza humana en Poza Rica, normalista asesinada en Tuxpan. ⚠️ Fuente **sin fecha en ruta**, y el mismo bloque aparece casi idéntico en resultados de **junio de 2026**: riesgo alto de recirculación. **Si se fechara en ventana sería 🔴**. Séptima edición: `BLOQUEADO POR EGRESO` |
| ARGOS 102 | **Jiutepec, Morelos — ataque con dron y explosivos** | ⚠️ **Contaminado con un hecho de 2025**: el racimo es mayoritariamente de **agosto de 2025**. Las dos URLs de `diariodemorelos.com` **siguen sin fecha en ruta**. `PENDIENTE DE ANCLA FECHADA` **con advertencia de trampa de aniversario**. **No se declara 🔴** |
| ARGOS 102 | **`gabinetedeseguridad.gob.mx/resultados/` — obligatorio desde el 1-sep** | **Faltan nueve días.** Sigue **BLOQUEADO** al acceso directo, aunque la ruta `/contenido/<id>/` **sí devuelve resultados indexados** y publica sentencias de la FGR. **No es un dominio muerto, es un dominio ilegible por acceso directo** |
| ARGOS 102 | **Tijuana, col. Hipódromo** — cuatro cuerpos en cajuelas (`ARG-103-REC-002`) | Sigue `NO INTEGRABLE`: los cuerpos aparecieron en **puntos distintos a lo largo de ~8 horas**. ⚠️ **Dato nuevo de ARGOS 105**: la **misma firma reaparece en la misma zona el 3-ago** (`ARG-105-REC-002`), catorce días antes. **Deslindados en cinco campos, son hechos distintos** — pero el patrón de zona sí es común y es línea de explotación |
| ARGOS 101 | **Zinapécuaro** (`ARG-101-003`) | Sin avance. **Tres hechos con la misma firma** en el mismo municipio. Se mantiene 🟡 |
| ARGOS 102 | **Los Reyes, Michoacán** (`ARG-102-002`) | Sin avance. El aseguramiento de Los Reyes del boletín federal es **sin detenidos y sin abatidos**: **no es el hecho de los cinco abatidos** y no debe fusionarse |
| ARGOS 102 | **Alfajayucan, Hidalgo** (`ARG-102-005`) | Sin avance. Solo páginas-etiqueta sin fecha. `PENDIENTE DE ANCLA FECHADA` |
| ARGOS 104 | **Coahuila — brecha Rancherías, Hidalgo** · **Chiapas — Mapastepec** | Sin avance; ARGOS 105 no les gastó búsqueda. Ninguna de sus URLs lleva día. Ambos serían 🟡 si se fecharan |

## Contradicciones abiertas

| Desde | Caso | Detalle |
|---|---|---|
| ARGOS 105 | **Juchipila — cartuchos** | Una consulta devolvió **118 cartuchos** frente a los **60** publicados en `ARG-104-ARM-001`. Probablemente el mismo resumidor parafraseando con imprecisión. **No se tocó el archivo sin lectura directa que lo sostenga** |
| ARGOS 104 | **Chiapas: Sureste o Pacífico** | Se regionaliza como **Sureste** desde ARGOS 88; en `argos-2026-08-03/04.html` figuró como **Pacífico**. **Sureste es la lectura correcta.** *No se toca el archivo antiguo* |
| ARGOS 104 | **Puerto Madero, Chiapas** (`ARG-104-ARM-003`) | **Dos lecturas incompatibles de la misma fuente institucional**. Solo se integraron las **3 largas y los 4 detenidos**. `CONTRADICHA — NO INTEGRAR HASTA VALIDACIÓN` |
| ARGOS 104 | **Juchipila — personas liberadas** · **El fusil Barrett de La Angostura** | La primera, contradicción **dentro de la misma fuente** (titular dice una, boletín y *slug* dicen dos): se publicó **2** con la salvedad. El segundo, `NO DETERMINABLE` si está comprendido en las seis largas: se publica por separado, no se suma |
| ARGOS 103 | **Armamento especial vs. armas largas** (`ARG-103-ARM-001`) | La balanza se inclina a que **el armamento especial NO está comprendido** en las largas, pero es paráfrasis del resumidor. Confianza **Media**. El boletín federal da **dos armas cortas** frente a **una** de la ficha |
| ARGOS 99 | **Culiacán** (`ARG-99-001`) | Ubicación conciliada. **Hora: tres versiones —12:30, 13:00 y ~14:00—.** `CONTRADICHA — reportar las tres, no promediar`. **Sin detenidos: confirmado** |
| ARGOS 101 | **Mapimí, Durango** | Desglose **8 largas + 4 cortas = 12 armas**, con **87 cargadores y 4,715 cartuchos**, frente a los **65 cargadores** del boletín federal. **Contradicción de cargadores abierta** |
| ARGOS 100 | **Altamira, Tamaulipas** (`ARG-100-001`) | **Se propone cerrar como `2 o 3 — DISCREPANCIA NO RESUELTA`.** El "comunicado de la Primera Zona Naval del 15-ago" **sigue sin existir localizable** |
| ARGOS 103 | **Las 84 UMA de Tlaxcala** · **La cifra de bloqueos de Michoacán** (`ARG-103-001`) | Sin cambio en ninguna. La primera, `CONTRADICHA — REQUIERE LECTURA DIRECTA`; **no gastar búsquedas**: arbitrar entre dos paráfrasis del mismo resumidor no produce un dato mejor. La segunda, cuatro lecturas publicadas sin fundir |
| ARGOS 103 | **La reserva de color de `ARG-103-002`** | Sin cambio. Una fuente que sitúe la agresión a la GN en el punto de la captura obliga a fe de erratas |
| ARGOS 102 | **Chiapas — Cintalapa y Benemérito de las Américas** | Son casos **distintos** de los del archivo. La ficha de Cintalapa **sigue debiendo reescribirse o retirarse**. Los "37 cargadores de 30 cartuchos cada uno" son **capacidad declarada**: nunca convertir a 1,110 |
| ARGOS 101 | **Colima** (`ARG-101-002`) | Sin arbitrar: Infobae y Puente Libre no reportan detenidos, El Occidental reporta 1 mujer detenida |
| ARGOS 99 | **Indicador SESNSP: −48% frente a −60%** | Sin cambio. `HEREDADO — NO REVERIFICADO`. **Origen verificado**: entró en ARGOS 86 con respaldo citable real, así que **se conserva y no procede fe de erratas** |
| ARGOS 98 | **"Operación Sable", Mazatlán** (`ARG-97-ARM-003`) · **Privada Amberes, Ciudad Juárez** · **Azcapotzalco** · **Campeche — Hopelchén** | Sin avance en ninguno |

## Deuda editorial y de método heredada

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 98 | **Lista blanca de egreso** | `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**. **Cero portales leídos por acceso directo, decimosexta edición.** Sigue siendo **el único cambio que elevaría el techo del producto** por encima de ★★★★☆ |
| ARGOS 102 | **Mergear las ramas de edición a `main`** | ⚠️ **Avance en ARGOS 105**: la rama de ARGOS 104 se integró con `git merge --ff-only`, así que la 105 arranca sobre ella. **Siguen sin mergearse a `main` las ramas de ARGOS 88 a 105.** Nota operativa: **`barrido-regional`, `procedencia-cifras` y `editor-duplicidad` ya resuelven por nombre** — el rodeo por `general-purpose` que hicieron falta en ARGOS 104 ya no es necesario para los tres controles, aunque en ARGOS 105 los seis barridos regionales sí se lanzaron con el rodeo |
| ARGOS 100 | **Correcciones de ARGOS 99 a ARGOS 98 que siguen sin aplicarse** | **Octava edición sin ejecutarse.** Reintegrar Lázaro Cárdenas (`ARG-98-ARM-003`) al total de ARGOS 98; sustituir dos URL mal citadas en `argos-2026-08-15-fuentes.md`; incorporar tres hechos omitidos por ARGOS 98 (Chilpancingo/Los Ardillos 14-ago, Nopala Hidalgo 13-ago, excomandante por tortura en Cuautla); reintegrar el desglose de Sain Alto al total de ARGOS 99. Se suman las nueve recuperaciones `ARG-102-REC-*` y los 27 AEI de Escuinapa |
| ARGOS 104 | **Las portadas rectificadas no reflejan su conteo** | A las de ARGOS 95, 96, 99, 100 y 101 se suman ahora **ARGOS 88, 94 y 95** por las fes de erratas de ARGOS 105. Todas llevan su bloque de fe de erratas encima de la valoración, pero sus **portadas** siguen mostrando el conteo original, porque se generan desde el arreglo `EVENTOS` de cada edición. **Residuo conocido y acotado** |

## Cerrados recientemente

- **72 vs. 172 AEI, Sinaloa — CERRADO POR RETIRADA** (`ARG-107-FE-001`). Tercera edición sin que
  aparezca el boletín primario que arbitre: el barrido de Noroeste intentó `site:gob.mx/sedena` con
  los términos del hecho y **no lo devolvió**. Se aplica el umbral de cifras arrastradas de
  `CLAUDE.md`: **se retira del acumulado** y el renglón queda como `CANTIDAD NO DETERMINADA — NO SE
  INTEGRA AL TOTAL NUMÉRICO`. El resto del desglose del evento —2,450 L de sustancias, 98
  cargadores, 8,095 cartuchos, 1 Barrett .50, 6 armas largas— **no se altera**. Se confirmó de paso
  que la disputa **no afecta al evento de El Rosario** (>300 AEI, 18-ago, SEMAR), que está bien
  anclado. *Señalar un problema sin resolverlo, edición tras edición, no es trazabilidad.*

- **La deuda de cobertura de ARGOS 106 — SALDADA.** Las 27 entidades `NO REVISADA` se consultaron
  en ARGOS 107, con las seis regiones lanzadas en paralelo antes que ningún otro encargo: **32 de
  32**. En su lugar queda abierta una deuda más fina y honesta: la cobertura es **por entidad, no
  por portal**.

- **El Ciclo C — APLICADO Y DECLARADO** en ARGOS 107, tras saltarse en ARGOS 106. Rendimiento
  **defensivo**, no ofensivo: no produjo sentencia integrable, pero evitó dos falsos positivos —uno
  de ellos **dentro de ventana**— e inventarió qué dominios de fiscalía responden. *Dos éxitos y un
  empate no hacen una regla; se registra tal cual.*

- **La deuda de registro — SALDADA.** Los cuatro hechos inventariados por ARGOS 104 y los dos
  incidentales que seguían sin ficha recibieron ARG-ID (`ARG-105-REC-003` a `-008`), y el séptimo
  —La Paz, BCS— **se declaró expresamente fuera de umbral** en vez de quedar en espera indefinida.
  *Cerrada la deuda que ARGOS 104 abrió como PRIORIDAD 1.*

- **La auditoría de las ventanas 88-93 — CERRADA**, y con un hallazgo estructural: además de dos
  hechos 🔴 nuevos (`ARG-105-REC-001` Saltillo y `ARG-105-REC-002` Tijuana), destapó que **la serie
  tiene un intervalo que ninguna edición cubre**. *Cerrada la auditoría; se abre en su lugar la deuda
  de método sobre los huecos de ventana.*

- **Jalisco — Tizapán el Alto, 19 sentenciados — CERRADO, y no como se esperaba.** No faltaba el
  comunicado de la FGR para integrarlo: **ya estaba publicado como `ARG-94-SEN-002`** desde
  ARGOS 94, con el desglose completo (12 a 18a 1m 22d y 7 a 16a 6m). El pendiente llevaba **tres
  ediciones vivo sobre una premisa falsa**. *Cerrado.*

- **La Paz, BCS — CERRADO como fuera de umbral.** Séptima edición sin fuente oficial; la regla
  asimétrica de sentencias no admite confianza Baja. `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR
  AL CONTEO NACIONAL`, y sale de la lista de pendientes activos.

- **Durango, Gómez Palacio (`ARG-104-SEN-001`) — RESUELTO por retirada.** Segunda edición con la pena
  exacta y los importes sin respaldo citable: la regla de las cifras arrastradas obliga a retirarlos.
  **La sentencia se conserva**, la pena queda en «más de 7 años» **no sumable**, y multa y reparación
  pasan a `CANTIDAD NO DETERMINADA` (`ARG-105-FE-005`). *Cerrado.*

- **El directorio de dominios — depurado.** Llevaba la fila corregida de Aguascalientes **prepuesta
  al título del archivo**, y filas obsoletas duplicadas de **Colima** y **Nayarit** conviviendo con
  las corregidas. Colima queda donde le corresponde, en Occidente. *Cerrado.*

- **El bug de anclaje del generador móvil — CERRADO, corregido en la herramienta.** Y con él la
  exigencia de 3 SVG fijos, que penalizaba a las ediciones sin aseguramientos.

- **Los pendientes cerrados en ARGOS 104** —la auditoría 95-98, la rectificación en bloque de 99-101,
  la deuda de cobertura de Colima, Aguascalientes y Nayarit, la variante de Veracruz, el falso vacío
  del boletín federal y el bug de `colspan`— *se retiran conforme a la convención de dos ediciones.*

---

## Cómo arrancar la edición siguiente

**No se transcribe aquí.** La orden de arranque vive en **`reports/_arranque-ARGOS-108.md`**, que se
escribe al cierre de cada edición y la consume la siguiente. Ese archivo lleva la verificación de
base previa a numerar, la ventana, la deuda heredada, las trampas ya verificadas y los comandos de
construcción.

Una sesión nueva arranca leyendo, en este orden: **`_arranque-ARGOS-108.md`** → **`CLAUDE.md`** →
**este archivo** → **`reports/argos-2026-08-25-fuentes.md`** → **`reports/indice-arg-id.md`**.

### Lo que funcionó en ARGOS 107 y conviene repetir

1. **Lanzar los seis `barrido-regional` en paralelo antes que nada.** 32 de 32 entidades frente a
   las 5 de 32 de ARGOS 106. Es la diferencia entre un producto con cobertura y uno sin ella.
2. **Un recall nacional del coordinador, además del de cada región.** Las regiones agotan
   presupuesto; el coordinador no. De ahí salieron **dos de los tres hechos recuperados**
   —Tecamachalco y el megaoperativo del CJNG—.
3. **Leer lo que el `grep` devuelve.** Las dos coincidencias de `editor-duplicidad` parecían ruido y
   una —el inhibidor de drones de Huajicori, 12-ago— **mejoró una conclusión del cartelón**: el
   hallazgo dejó de presentarse como inédito y pasó a ser el segundo en trece días.
4. **Verificar el TÍTULO de la URL institucional, no solo su existencia.** El candidato a sentencia
   de Jiquilpan tenía respaldo institucional aparente hasta que se leyó el título de la nota:
   hablaba de **Morelia y Uruapan**. Es el fallo de Coronango repitiéndose, y el control lo atrapó.
5. **Perseguir la fecha en la ruta hasta el final.** Tres candidatos cayeron o quedaron marcados por
   esa sola comprobación. Uno —«Operativo Muralla, 9 detenidos y 9 armas largas»— resultó ser del
   **27 de enero** y habría metido nueve armas largas falsas en el conteo nacional.
6. **No convertir capacidad declarada en munición.** Los «42 cargadores de 20 cartuchos cada uno» de
   ese mismo operativo no son 840 cartuchos. La regla del caso de Chiapas sigue rindiendo.
7. **Declarar `NO REVISADA` con granularidad de portal, no de entidad.** Decir «32 de 32» sin más
   habría sido cierto y engañoso a la vez.
