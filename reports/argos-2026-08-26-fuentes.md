# ARGOS 108 — Archivo de fuentes y trazabilidad

**Corte**: 2026-08-26 · **Ventana**: 2026-08-25 09:26 → 2026-08-26 14:21 CDMX (28 h 55 min)
**Continuidad**: abre exactamente donde cerró ARGOS 107. Sin hueco ni solape.
**Hora verificada** con `TZ=America/Mexico_City date` al arranque de la sesión, no heredada.

Este archivo recoge **todo lo que no debe ir al cartelón**: el registro del barrido, los descartes,
los hallazgos de método y la deuda de cobertura. El cartelón lleva hechos; esto lleva la auditoría.

---

## Bloque 0 — verificación de base

`_arranque-ARGOS-108.md` exigía comprobar el estado del archivo **antes de numerar**. Resultado:

| Comprobación | Esperado | Encontrado |
|---|---|---|
| Última edición en `reports/` | `argos-2026-08-25` (ARGOS 107) | ✔ correcto |
| Archivos en `reports/` | 66 | ✔ 66 |
| `main` contiene ARGOS 107 | sí | ✔ sí |
| Rama de trabajo respecto de `main` | — | **5 commits por detrás, 0 por delante** |

La rama asignada por el entorno estaba **desactualizada y sin el archivo de arranque**: `ls reports/`
sobre ella mostraba como última edición `argos-2026-08-24` y **no contenía
`_arranque-ARGOS-108.md`**. Numerar por lo que la rama tenía a la vista habría producido un
**falso ARGOS 108 con ventana solapada**. Se resolvió con `git merge --ff-only origin/main` antes de
leer nada más, que es exactamente lo que el Bloque 0 ordena. **La lección de ARGOS 107 se confirma
por segunda edición consecutiva y debe conservarse en el arranque.**

## Bloque 5 — bloqueo de egreso, verificado en sesión

No se heredó: se comprobó con `curl` por dominio.

```
gob.mx                       curl: (56) CONNECT tunnel failed, response 403
www.gob.mx                   curl: (56) CONNECT tunnel failed, response 403
gabinetedeseguridad.gob.mx   curl: (56) CONNECT tunnel failed, response 403
fgr.org.mx                   curl: (56) CONNECT tunnel failed, response 403
fiscaliaveracruz.gob.mx      curl: (56) CONNECT tunnel failed, response 403
```

El estado del proxy lo confirma como **denegación de política en la puerta de salida**
(`connect_rejected — gateway answered 403 to CONNECT (policy denial)`), no como fallo de
herramienta ni caída de portal. `WebFetch` devolvió `EGRESS_BLOCKED` explícito sobre
`heraldodemexico.com.mx`.

**Vigésima edición consecutiva. Cero portales leídos por acceso directo. Techo de confianza del
producto: ★★★★☆; ninguna ficha lleva ★★★★★.** `docs/solicitud-lista-blanca-egreso.md` sigue sin
tramitar y sigue siendo el único cambio que elevaría ese techo.

---

## Cobertura del barrido — 32 de 32 entidades

Seis agentes `barrido-regional` en paralelo, autorizados por el destinatario y lanzados **en un
solo mensaje antes de ningún otro encargo**, con la deuda de portal de ARGOS 107 al frente de cada
región.

| Región | Entidades | Presupuesto | Portales que quedaron `NO REVISADA` |
|---|---|---|---|
| Noroeste | 6 de 6 | 20/20 | SSPCE Chihuahua, SSPE BC y BCS, SSP Durango; GN prensa, SEDENA/IV RM, SEMAR Pacífico Norte, FGR, ANAM |
| Noreste | 5 de 5 | 20/20 | SSP Coahuila, FGJ Nuevo León, SSP Tamaulipas, SSPC SLP, FRIZ Zacatecas; mesas de paz de las 5; SEDENA, FGR, ANAM |
| Occidente | 6 de 6 | 20/20 | Fiscalías de Jalisco y Aguascalientes; SSP Nayarit; SEDENA, GN, FGR, ANAM; mesas de paz |
| Centro | 7 de 7 | 20/20 | SSP Puebla, SSP Tlaxcala; SEMAR y FGR regionales; ANAM |
| Golfo | 2 de 2 | **23/20** (desviación declarada) | SSPC Tabasco; policías estatales de ambas; mesas de paz de ambas; delegaciones FGR |
| Sureste | 6 de 6 | 20/20 | SEDENA VII/IX/XI RM; policías estatales diferenciadas de las 6; mesas de paz de 5; GN prensa |

**La cobertura es por entidad, no por portal.** Los portales sin ver se declaran `NO REVISADA`,
nunca `SIN ACTUALIZACIÓN`. El agente de Golfo gastó **23 de 20** búsquedas y lo declaró en vez de
disimularlo, para no cortar a la mitad el cruce de las tres carpetas de periodistas de Poza Rica;
la desviación se acepta y se registra.

**Deuda de ARGOS 107 saldada**: los seis portales nominalmente pendientes de Centro (FGJ CDMX,
Fiscalía Morelos, FGE Tlaxcala, SSP Hidalgo, SSPMQ Querétaro, SEDENA/SEMAR/FGR) fueron consultados;
las fiscalías del Noroeste y del Sureste también. Lo que queda abierto es **otra capa de portal**,
más fina, listada arriba.

### Dominios oficiales — inventario actualizado

| Entidad | Estado | Dominio |
|---|---|---|
| **Tlaxcala** | ✅ **CONFIRMADO en este corte** | `fgjtlaxcala.gob.mx` (unidad anticorrupción en `fecc.fgjtlaxcala.gob.mx`) |
| **Nayarit** (fiscalía) | ✅ **CONFIRMADO en este corte** | `fiscaliageneral.nayarit.gob.mx` |
| **Aguascalientes** (SSP) | ✅ **CONFIRMADO en este corte** | `aguascalientes.gob.mx/ssp/` · IESPA en `/IESPA/` |
| Colima | Confirmado en ARGOS 107 | `fgecolima.mx` (**no** `fiscalia.colima.gob.mx`) |
| Chihuahua | Precisado | `fiscalia.chihuahua.gob.mx` (**`fgechihuahua.gob.mx` no resuelve**) |
| **Michoacán** (fiscalía) | ⚠️ indicio, sin confirmar | posiblemente `fiscaliamichoacan.gob.mx`, **no** `fge.michoacan.gob.mx` — validar en ARGOS 109 |
| **Nayarit** (SSP) | ⚠️ sin confirmar | probar `ssp.nayarit.gob.mx` y `sspc.nayarit.gob.mx` antes de declarar inexistencia |
| **Guanajuato** | ⚠️ sin confirmar | se sigue usando el agregador `boletines.guanajuato.gob.mx`, **sustitución declarada** |
| **Sonora / Sinaloa** (fiscalías) | ⚠️ sin confirmar | `fgjsonora.gob.mx` y `fiscaliasinaloa.gob.mx` no devuelven contenido propio vía `site:`; existe `fiscaliasinaloa.mx` |

**Tres dominios confirmados y dos precisados en un solo corte**: el rendimiento de dedicar el triaje
judicial a dos regiones. Es dato que hereda ARGOS 109 y que no hay que volver a pagar.

---

## Rotación de cobertura — **CICLO A aplicado y declarado**

A ARGOS 108 le tocaba el **Ciclo A: Noroeste + Centro encabezan el triaje judicial**; Noreste,
Occidente, Golfo y Sureste encabezan con armamento. **Se aplicó y se cumplió**: los dos agentes del
ciclo gastaron sus primeras consultas en fiscalías y poderes judiciales antes de tocar armamento.

**Qué aportó la rotación que el orden anterior no habría aportado:**

1. **Centro localizó las dos únicas sentencias estatales del corte.** La FGE de Querétaro
   (`fiscaliageneralqro.gob.mx`) fue **el único portal institucional de las 32 entidades que publicó
   dentro de la ventana**, con dos boletines fechados `2026/08/25/` en la ruta. Entrando por
   armamento, Querétaro —entidad de bajo volumen de aseguramiento— habría quedado al final de la
   cola y esas dos sentencias se habrían perdido. **Es rendimiento ofensivo, no defensivo**, a
   diferencia del Ciclo C de ARGOS 107.
2. **Centro cerró el dominio de Tlaxcala**, pendiente heredado desde ARGOS 107, y **Occidente cerró
   el de Nayarit** — el triaje judicial es lo que obliga a resolver qué dominio de fiscalía responde.
3. **Noroeste inventarió el estado real de las seis fiscalías del noroeste** y precisó el dominio de
   Chihuahua. No produjo sentencia integrable: sus boletines más recientes son del 24-ago, un día
   antes de la apertura. **Se registra sin inflarlo.**

**Balance**: el Ciclo A rindió **una sentencia estatal doble y dos dominios**. Frente al rendimiento
defensivo del Ciclo C en ARGOS 107, esta vez la rotación cambió lo que el producto encontró.
**A ARGOS 109 le toca el Ciclo B — Noreste + Golfo.**

---

## Control de recall — el hallazgo de método del corte

El arranque exigía dos controles: recall por región y **recall nacional del coordinador**, *además*
del de cada región. Ambos se ejecutaron. El resultado es contundente y debe registrarse sin adornos:

> **Cinco de los ocho hechos del corte los aportó el recall nacional del coordinador, no los
> barridos regionales.** Chilpancingo y Acapulco (Guerrero) no los detectó Sureste; Tepechitlán y
> Juchipila (Zacatecas) no los detectó Noreste; el «Koki» apareció en las dos vías.

Las regiones declararon correctamente `SIN RESULTADO INDEXADO EN VENTANA` para sus portales —y era
cierto: **ninguna autoridad publicó boletín sobre esos cuatro hechos**—. El fallo no es de los
agentes ni de su cobertura: es que **con los portales bloqueados, un barrido organizado por dominio
institucional no ve los hechos que solo publican los medios**. La consulta genérica nacional
(`ataque armado / violencia México 25 y 26 de agosto de 2026`) sí los ve.

**Es el mismo cuarto modo de fallo que ARGOS 106 documentó** —recall insuficiente dentro de una
cobertura declarada completa— y por segunda edición consecutiva el recall nacional del coordinador
es lo que lo compensa. **No es un control opcional: es el que produce la mayoría de los hechos.**
Debe seguir siendo obligatorio y debe ejecutarse **antes** de dar por cerrado ningún barrido.

Golfo y Occidente sí ejecutaron su control de recall genérico y de ahí salieron San Andrés Tuxtla y
el estado del pendiente de Morelia. Noreste también, y de ahí salieron su hallazgo de Ciudad
Victoria y su alerta de duplicidad de Coahuila.

---

## Los ocho hechos de la ventana

| ARG-ID | Entidad · municipio | Fecha · hora | Color | Origen del hallazgo | Confianza |
|---|---|---|---|---|---|
| `ARG-108-001` | Guerrero · Chilpancingo | 25-ago, 15:00 | 🔴 | Recall nacional | ★★★☆☆ |
| `ARG-108-002` | Zacatecas · Tepechitlán | 25-ago, 13:00 | 🔴 | Recall nacional | ★★★☆☆ |
| `ARG-108-003` | Guerrero · Acapulco | 26-ago, 14:00 | 🔴 | Recall nacional | ★★★☆☆ |
| `ARG-108-004` | Veracruz · San Andrés Tuxtla y Catemaco | 26-ago, madrugada | 🟡 | Barrido Golfo | ★★☆☆☆ |
| `ARG-108-005` | Veracruz · Poza Rica | 25-ago, mañana | 🟢 | Barrido Golfo + recall | ★★★★☆ |
| `ARG-108-006` | Zacatecas · Juchipila | 25-ago, 11:16 | 🟢 | Recall nacional | ★★★☆☆ |
| `ARG-108-007` | Hidalgo (carretera México–Pachuca) / Tabasco | 26-ago | 🟢 | Recall nacional + Golfo | ★★★★☆ |
| `ARG-108-008` | Tamaulipas · Reynosa | 25-ago | 🟢 | Barrido Noreste | ★★★★☆ |

Más `ARG-108-FE-001` (fe de erratas sobre Candela) y `ARG-108-REC-001` (recuperación de Mazatepec),
ambos **fuera de todos los totales del corte**.

### Clasificaciones que exigieron aplicar una regla, no un juicio

- **`ARG-108-002` Tepechitlán → 🔴**: el grupo criminal **inició** la agresión contra personal
  federal en tránsito. Es *ataque contra autoridades*, no *confrontación derivada de operativo*.
  **Los cuatro abatidos no mueven el color**: contar bajas del lado criminal como medida de gravedad
  convertiría la eficacia de la respuesta estatal en aumento del riesgo nacional.
- **`ARG-108-004` San Andrés Tuxtla → 🟡 por reserva**: ninguna fuente establece quién inició.
  La metodología obliga a 🟡 y a declarar la reserva; subir a rojo por defecto inflaría el nivel con
  un hecho no acreditado.
- **`ARG-108-001` y `ARG-108-003` → 🔴 por víctimas múltiples**, agravante expreso de la escala para
  el homicidio doloso que sin él sería 🟡.
- **`ARG-108-005` Poza Rica → 🟢, y el delito del 24-ago conserva su 🔴** (`ARG-107-001`): son **dos
  eventos, no uno**. Reserva declarada en la ficha: **la autoridad no publicó cómo fue localizado**,
  así que no se afirma rescate operativo.
- **`ARG-108-FE-001` Candela → 🔴** por el agravante *muerte de personal de las fuerzas de
  seguridad*, que opera **con independencia de quién inició**.

---

## Fe de erratas — `ARG-108-FE-001` corrige `ARG-107-003`

ARGOS 107 publicó Candela como **🟡, con 1 civil abatido y 1 policía herido**, y con la marca
`FECHA DEL HECHO NO ANCLADA EN RUTA`. Las tres cosas se corrigen:

| Campo | ARGOS 107 | ARGOS 108 |
|---|---|---|
| Fecha del hecho | 25-ago, **no anclada** | **25-ago 04:30**, anclada por declaración del fiscal general |
| Saldo | 1 civil abatido · 1 policía **herido** | **2 civiles abatidos · 1 policía muerto** (Mauro Flores) |
| Color | 🟡 AMARILLO | **🔴 ROJO** |
| Armamento | «sin armamento publicado» | **2 armas largas**, ponchallantas, 1 vehículo |
| Identidad de abatidos | pendiente | preliminar: uno del **Estado de México**, otro de **Nuevo León** |

**El semáforo de ARGOS 107 queda corregido a 3 🔴 y 0 🟡.** El archivo antiguo no se reescribe.
El hecho **pertenece a la ventana de ARGOS 107** y por tanto **no se recuenta** en ARGOS 108: solo
sus dos armas largas entran en la línea inferior de las tarjetas de armamento, marcadas como
procedentes de otra ventana.

Fuente que lo ancla: declaración del fiscal **Federico Fernández Montañez**, citada por
[El Siglo de Torreón](https://www.elsiglodetorreon.com.mx/noticia/2026/enfrentamiento-en-candela-coahuila-deja-3-personas-muertas-2-civiles-armados-y-un-policia.html)
y [El Tiempo Monclova](https://eltiempomx.com/noticia/2026/fiscal-confirma-muerte-de-policia-estatal-tras-enfrentamiento-en-candela.html);
[El Heraldo de Saltillo `/2026/08/25/`](https://elheraldodesaltillo.mx/2026/08/25/muere-elemento-de-la-policia-estatal-en-enfrentamiento-en-candela-abaten-a-un-delincuente/),
[MVS `/2026/8/25/`](https://mvsnoticias.com/nacional/estados/2026/8/25/enfrentamiento-en-coahuila-deja-un-policia-estatal-muerto-743355.html).

**Resuelve además la alerta del barrido de Noreste**, que planteó tres hipótesis sin poder arbitrar:
(a) evolución de `ARG-107-003`, (b) resurfación del enfrentamiento de Hidalgo, Coahuila de
octubre-2025, (c) tercer hecho distinto. **Es la (a)**: municipio, hora, corporación y fiscal
coinciden; el de octubre-2025 es otro municipio y otro año.

---

## Controles editoriales — ejecutados a mano, y ambos produjeron hallazgos

La autorización de subagentes del destinatario cubrió **los seis barridos regionales**.
`editor-duplicidad` y `procedencia-cifras` **no se invocaron como agentes**; se ejecutaron a mano con
el mismo criterio, como en ARGOS 106 y 107. **Se declara la ausencia, no se disimula.**

### `editor-duplicidad` — un doble conteo real interceptado

Contraste de los ocho hechos y de los dos candidatos de armamento contra `indice-arg-id.md` y los
`-fuentes.md` de toda la serie.

> ⚠️ **HALLAZGO PRINCIPAL — `ARG-104-ARM-008`.** El aseguramiento de **Ciudad Victoria, Tamaulipas**
> —**7 armas largas, 18 cargadores**—, republicado el 25-ago por
> [La Razón `/2026/08/25/`](https://www.razon.com.mx/estados/2026/08/25/aseguran-siete-armas-largas-y-640-dosis-de-droga-en-operativo-en-ciudad-victoria/),
> **es el mismo hecho que ARGOS 104 ya publicó como `ARG-104-ARM-008`**, con fecha del hecho
> **19 de agosto**. Coinciden **armas largas y cargadores en cifra exacta**, entidad, municipio y
> corporación. El barrido de Noreste lo trajo con la marca `CONTRADICHA — 19 o 25-ago` precisamente
> porque el resumidor de Capital México lo fechaba el 19: **el archivo resuelve la contradicción a
> favor del 19**. De haberse integrado habría añadido **7 armas largas y 18 cargadores fantasma** al
> conteo nacional.
>
> **Discrepancia de munición que queda abierta**: ARGOS 104 publicó **340 cartuchos**; la
> republicación de este corte, **103**. `CONTRADICHA — NO SE ARBITRA SIN LECTURA DIRECTA`.

Otras coincidencias revisadas y **leídas**, conforme a la regla de que un `grep` sin leer no cuenta:

| Coincidencia | Veredicto |
|---|---|
| **Juchipila** en `argos-2026-08-21-fuentes.md` | ✔ No es duplicado: es `ARG-104-001`, y se cita **deliberadamente** como cruce de archivo en la ficha `ARG-108-006` |
| **«Amado»** en `argos-2026-08-11` y `-19` | ✔ Falso positivo: son «medicamento» y **Teófilo Amado de Jesús**, víctima de otro caso. Nada que ver con Víctor Manuel Amado de León |
| **«blindaje artesanal»** en `argos-2026-08-24` | ✔ No es duplicado: `ARG-106-003` es **1 vehículo asegurado por SEMAR en Sinaloa**; éste es la **destrucción de 25 en Tamaulipas por la FGR**. Distinto estado, distinta naturaleza |
| **Mazatepec / Víctor Manuel Amado de León** | ✔ **Sin precedente en toda la serie** → procede como `-REC-` |
| Tepechitlán · Koki · limpiaparabrisas · María de la O · San Andrés Tuxtla · Bryan Isaac · Irineo · Amozoc · Pinal de Amoles | ✔ Sin precedente |

**Regla de no duplicación verificada en el cartelón**: ningún hecho con ficha propia aparece además
en una tabla resumen. La tabla de la pág. 5 contiene **solo** el evento de Candela, que no tiene
ficha de hecho sino fe de erratas; los 25 blindados de `ARG-108-008` **no** figuran en la tabla, solo
en la línea inferior de su tarjeta y con remisión a la ficha.

### `procedencia-cifras` — dos cifras propias sin fuente, retiradas

Auditoría de cada número del borrador contra su fragmento citable.

> ⚠️ **HALLAZGO — cifras inferidas por el redactor.** El borrador afirmaba que Tepechitlán y
> Juchipila **«distan unos 60 km»**, que San Andrés Tuxtla está **«a más de 60 km de la costa»** y
> que el «Koki» fue capturado **«a más de 700 km»** de su plaza. **Ninguna de las tres procede de
> fuente alguna**: son estimaciones geográficas del redactor. Violan la regla de *cero cifras
> inferidas* y **se retiraron las tres**, conservando la afirmación cualitativa —«sobre el mismo eje
> sur», «en la sierra y no en el litoral», «fuera de su plaza»—, que es lo que sostiene el análisis
> y no necesita número.

Cálculos propios **declarados como tales en el cartelón**, no presentados como dato de fuente:

| Cifra | Origen | Estado |
|---|---|---|
| **188 años 4 meses** de prisión acumulados | 62 + 54 + 54 + 5 + (13a 4m) | ✔ declarado *cálculo propio* |
| **1,265,628 pesos** de multas | 414,960 + 425,334 + 425,334 | ✔ declarado *cálculo propio*; los **400 días multa** de Querétaro **no se convierten** por falta del valor diario |
| **2 armas largas** en la línea inferior de las tarjetas | único evento tras el deslinde de duplicidad | ✔ declarado *cálculo propio* |
| Brecha detención–condena (2a 5m / 2a 8m / 4a 6m) | fechas de hecho y de resolución publicadas | ✔ declarado *cálculo propio*: ninguna autoridad publica el intervalo |
| **28 h 55 min** de ventana | horas de apertura y cierre | ✔ declarado |
| «menos de dos horas» entre Tepechitlán y Juchipila | 13:00 − 11:16, ambas publicadas | ✔ declarado |
| **5 personas detenidas** en el corte | 2 (Juchipila) + 3 (Koki) | ✔ los 5 de San Andrés Tuxtla **quedan fuera** por ser fuente única sin confirmación |
| «más de 15 casquillos» de 9 mm | cifra consolidada | ✔ se anota que el reporte preliminar decía «más de 10» |

Cifras de **sentencia de Puebla** (62/54/54 años y las tres multas): proceden del resumen del
boletín de la FGR difundido por La Jornada, **no de lectura del documento primario** —imposible bajo
el bloqueo—. Son internamente consistentes (las dos penas idénticas llevan multa idéntica) y la
fuente es oficial de origen. Se integran con esa reserva, que el cartelón declara de forma general.

---

## Trampas interceptadas en este corte

| Trampa | Qué habría entrado | Cómo se atrapó |
|---|---|---|
| ⚠️ **Aniversario — Tepechitlán** | **3 armas largas, 7 cargadores, 90 cartuchos y 7 explosivos** falsos en el conteo nacional | Las cifras circulan asociadas al municipio pero corresponden al **17-feb-2026**, comunidad de San Pedro Ocotlán, agresión contra las **FRIZ** (no la GN) con **4 detenidos** (no 4 abatidos). Fechado en `ljz.mx/18/02/2026/` y `canalnuevezacatecas.com.mx/noticias/2026-02-18/`. **El boletín de la SSP de Zacatecas que las contiene no lleva fecha en su ruta**, que es lo que hace confundible el par |
| ⚠️ **Resumidor sin URL propia — boletín federal del «24 de agosto»** | Un desglose completo de Campeche, Sinaloa, Edomex, Guanajuato y Michoacán: **~19 largas, 15 cortas, 1,854 cartuchos, 112 cargadores, 1 granada y 49 AEI** | El resumidor afirma el boletín «acciones relevantes del 24 de agosto de 2026 (25/08/2026)» con desglose, pero **`site:gob.mx/sspc/prensa` lista boletines hasta el 21-23 de agosto y salta al siguiente**: ninguna consulta devolvió su URL propia. **Los cuatro barridos que lo buscaron llegaron a lo mismo.** El arranque ya documentaba que este emisor produjo dos veces el mismo falso positivo. **No entra en ninguna de las dos líneas** |
| ⚠️ **Duplicidad — Ciudad Victoria** | 7 largas y 18 cargadores contados dos veces | `editor-duplicidad` contra `ARG-104-ARM-008` (ver arriba) |
| ⚠️ **Homonimia de organización** | Atribuir a «Pueblo Unido» (Tabasco) los antecedentes de «Pueblos Unidos» (Hidalgo/Michoacán) | Nombres casi idénticos, organizaciones distintas. El propio resumidor mezcló las dos al describir la captura del «Koki». **Advertido en la ficha, para el mando** |
| ⚠️ **Agregado de jornada — Acapulco** | Un saldo de **2 muertos y 3 heridos** atribuido a un hecho puntual de 1 muerto y 1 herida | Los titulares nacionales pluralizan («ataques al transporte público») y agregan más de un hecho. Se ficha lo que la fuente puntual sostiene y **se declaran ambas versiones**. Es la lección de ARGOS 103 |
| **Mes / año en la ruta** | «Operativo Muralla» (NL, 27-ene) y otros | Ninguna cifra entró sin año y mes correctos en la ruta. Noroeste descartó además un caso de BCS que era de **diciembre de 2025** |
| **Contradicción de saldo — Chilpancingo** | Publicar 1 muerto cuando eran 3 | No es discrepancia entre fuentes sino **evolución por defunciones hospitalarias**: se declara así |

---

## Pendientes trabajados en este corte

| Pendiente | Estado tras ARGOS 108 |
|---|---|
| **`ARG-107-001` Poza Rica — localización de Elí Martínez** | ✅ **CERRADO.** Localizado con vida el 25-ago tras ~12 h; FGE Veracruz lo localizó, CEAPP activó medidas de protección. Era *la línea más perecedera del archivo* |
| **`ARG-107-001` — cruce de las tres carpetas de Poza Rica** | ✅ **RESUELTO Y PUBLICADO.** Carlos Castro (8-ene, homicidio, av. 20 de Noviembre, col. Cazones) · Luis Ángel López Valdez (11-jun, homicidio, 18 heridas, col. Cazones) · Elí Martínez (24-ago, av. 20 de Noviembre). **Dos de tres en la misma avenida, las tres con medidas de la CEAPP, cero detenidos en las tres.** Vínculo de autoría **no acreditado** |
| **`ARG-107-003` Candela — la fecha** | ✅ **CERRADO.** Anclada en 25-ago 04:30, dentro de la ventana de ARGOS 107. **No procede retiro** |
| **`ARG-107-003` Candela — identidad del abatido** | 🟡 **PARCIAL.** Son **dos** abatidos, identificados preliminarmente como originarios del Estado de México y de Nuevo León. Faltan nombres |
| **`ARG-106-REC-001` Acapulco — «el agresor herido en el tórax»** | ✅ **CERRADO POR MAL PLANTEAMIENTO.** El barrido de Sureste acreditó que el único herido de tórax localizable es **Ernesto Manuel (41), dueño del taller de El Quemado**, descrito por las fuentes como **víctima** de otro ataque, no agresor. **No existe fuente que documente a un agresor herido en el tórax en La Estación.** Se cierra sin gastar más presupuesto en rastreo hospitalario |
| **`ARG-106-REC-002` Morelia — definición de fuero** | ⛔ **SIN MOVIMIENTO, novena edición.** Sigue en fuero común (FGE Michoacán); la FGR podría atraerlo si la GN confirma la adscripción, y **la GN no se ha pronunciado**. `SIN RESULTADO INDEXADO EN VENTANA` |
| **Los Reyes de Salgado, Michoacán** — ancla fechada | ✅ **ANCLA ENCONTRADA.** El hecho (5 abatidos, 5 largas, 5 cargadores) es del **18-ago-2026** (`atiempo.mx`) — **fuera de la ventana de ARGOS 107 y de ésta**. Se marca `ANCLA ENCONTRADA — FUERA DE VENTANA, NO INTEGRABLE`; corresponde a la edición del 18-ago |
| **`ARG-107-002` Mazatlán — central de autobuses** | ⛔ Sin actualización en ventana. Noroeste confirmó el hecho base (1 muerto, 1 herido grave, 1 detenido; víctima identificada informalmente como Simplicio «N», 32 años, de Nayarit) pero **sin identificación oficial, vinculación ni línea publicadas** |
| **SLP — Matlapa, Elías «N»** (desde ARGOS 99) | 🟡 **AVANCE PARCIAL.** Noreste fijó la **fecha de publicación en 15-ago-2026**, fuera de esta ventana. No cierra, pero deja de ser un caso sin fecha |
| **Dominios de Tlaxcala, Nayarit y Guanajuato** | 🟢 **DOS DE TRES CERRADOS** (Tlaxcala, Nayarit). Guanajuato sigue por agregador |
| **Boletín del Gabinete del 19-ago / Los Reyes de Salgado en dos boletines** | ⛔ Sin resolver. Requiere lectura directa, imposible bajo bloqueo |

---

## Descartes de mayor coste — para que ARGOS 109 no los reintroduzca

| Hecho | Por qué NO entró |
|---|---|
| **Boletín del Gabinete de Seguridad «24 de agosto»** con desglose por entidad | `RESUMIDOR SIN URL PROPIA` — ver trampas |
| **Ciudad Victoria, Tamaulipas** (7 largas, 18 cargadores) | Duplicado de `ARG-104-ARM-008`, hecho del 19-ago |
| **Cifras de armamento de Tepechitlán** (3 largas, 7 explosivos) | Hecho del **17-feb-2026**, otro municipio-comunidad y otra corporación agredida |
| **Michoacán · Jiquilpan**, «sentencia por violación equiparada agravada, +11 años» | `POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN`. Es el fallo de ARGOS 107 repitiéndose: mismo tipo de *slug*, sin campos individualizadores |
| **Morelos · Cuautla**, extorsión agravada, 16a 8m (Luis Ángel «N») | URL de `24morelos.com` **sin fecha en la ruta**; el «25 de agosto» es afirmación del resumidor. **Candidato vivo para ARGOS 109** |
| **Puebla**, 254 acciones operativas / 106 detenidos / 10 armas / 62 cartuchos | **Agregado semanal del 17 al 23 de agosto**, fuera de ventana y multidelito |
| **Michoacán**, 9 detenidos tras 24 bloqueos viales | Hecho del **19-ago** |
| **Baja California Sur**, 3 sujetos con armas y uniformes tácticos | Hecho de **diciembre de 2025** |
| **Sinaloa**, sentencia de 118 años por secuestro y violación | Sin fecha de publicación fijable en ventana |
| **Oaxaca**, boletín FGEO 2,743 | **Vinculación a proceso, no sentencia** (descartado ya en ARGOS 107, reconfirmado) |
| **FGR Cancún y Chilpancingo**, sentencias de 4-7 años | 19-ago, y sin URL fechada propia |
| **Campaña SEDENA «Sí al Desarme, Sí a la Paz»** (Edomex y otros) | **Entrega voluntaria, no aseguramiento por autoridad**: fuera de la taxonomía |
| **SSC CDMX**, comunicado 946 (cargadores y 400 cartuchos, GAM) | URL sin fecha en la ruta; no se puede fijar dentro o fuera de ventana. **Candidato vivo para ARGOS 109** |
| **Chiapas · Jiquipilas**, enfrentamiento con el Ejército | Sin fecha fijable; no se afirma ni se niega |

---

## Deuda de método que ARGOS 108 deja abierta

1. **El barrido por dominio institucional no ve la mayoría de los hechos.** Cinco de ocho los aportó
   el recall nacional. Mientras dure el bloqueo, el recall genérico **no es complemento, es la vía
   principal**, y así debe presupuestarse: los agentes deberían gastar una fracción mayor de su
   presupuesto en consulta genérica por entidad y menos en `site:` que devuelve boletines viejos.
2. **`gabinetedeseguridad.gob.mx/resultados/` es obligatorio desde el 1-sep**: quedan **seis días**.
   Sigue ilegible por acceso directo.
3. **Los dos controles editoriales siguen ejecutándose a mano** y **los dos volvieron a producir
   hallazgos reales** —un doble conteo y tres cifras inferidas—. Es la tercera edición consecutiva.
4. **El generador móvil tenía un defecto de envoltorio duplicado** (`<div class="tabla-scroll">`
   anidado), presente en cuatro tablas de la móvil de ARGOS 107 y en tres de ésta: dos contenedores
   desplazables anidados atrapan el gesto de arrastre táctil. **Se corrigió la herramienta**
   (`tools/gen-movil.py`, red de seguridad con *lookbehind*), no su salida, conforme al Bloque 7.
   Verificado: 0 envoltorios duplicados, 3 de 3 tablas envueltas exactamente una vez.
5. **Correcciones de ARGOS 99 a ARGOS 98**: novena edición sin ejecutarse.

---

## Validación de la edición

```
python3 tools/gen-movil.py 108 2026-08-26 107 2026-08-25 14:21
  contadores del generador: 🔴 3  🟡 1  🟢 4
  tarjetas: móvil 11 / escritorio 11
  validación OK
```

Comprobado además: 7 secciones en ambas versiones · 9 iconos en ambas · 0 tarjetas `.reg` vacías ·
0 restos de clases de escritorio (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) ·
6 de 6 tablas del escritorio envueltas en `table-wrap` · 3 de 3 tablas de la móvil envueltas en
`tabla-scroll` sin anidamiento · contadores del radar idénticos al semáforo de la portada ·
`EVENTOS_ARM = []` y `div#argos-map-arm` omitido, porque un mapa enteramente gris no aporta
inteligencia.
