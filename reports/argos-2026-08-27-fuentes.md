# ARGOS 109 — Archivo de fuentes y trazabilidad

**Corte**: 2026-08-27 · **Ventana**: 2026-08-26 14:21 → 2026-08-27 10:00 CDMX (19 h 39 min)
**Continuidad**: abre exactamente donde cerró ARGOS 108. Sin hueco ni solape.
**Hora verificada** con `TZ=America/Mexico_City date` al arranque de la sesión, no heredada:
`2026-08-27 10:00:54 CST`.

Este archivo recoge **todo lo que no debe ir al cartelón**: el registro del barrido, los descartes,
los hallazgos de método y la deuda de cobertura. El cartelón lleva hechos; esto lleva la auditoría.

---

## Bloque 0 — verificación de base

`_arranque-ARGOS-109.md` exigía comprobar el estado del archivo **antes de numerar**. Resultado:

| Comprobación | Esperado | Encontrado |
|---|---|---|
| Última edición en `reports/` | `argos-2026-08-26` (ARGOS 108) | ✔ correcto |
| Archivos en `reports/` | 69 | ✔ 69 |
| `main` contiene ARGOS 108 | sí | ✔ sí |
| Rama de trabajo respecto de `main` | — | **5 commits por detrás, 0 por delante** |

**Tercera edición consecutiva con la rama desactualizada.** La rama asignada por el entorno mostraba
`argos-2026-08-24` como última edición y **no contenía `_arranque-ARGOS-109.md`**: numerar por lo que
la rama tenía a la vista habría producido un **falso ARGOS 107 con ventana solapada**. Se resolvió
con `git merge --ff-only origin/main` **antes de leer nada más**, que es exactamente lo que el
Bloque 0 ordena. **La advertencia debe conservarse en el arranque de ARGOS 110**: el patrón lleva
tres ediciones sin fallar ni una vez en su favor.

## Bloque 5 — bloqueo de egreso, verificado en sesión

No se heredó: se comprobó con `curl` por dominio.

```
gob.mx                       curl: (56) CONNECT tunnel failed, response 403
gabinetedeseguridad.gob.mx   curl: (56) CONNECT tunnel failed, response 403
fiscaliageneralqro.gob.mx    curl: (56) CONNECT tunnel failed, response 403
fgr.org.mx                   curl: (56) CONNECT tunnel failed, response 403
www.gob.mx                   curl: (56) CONNECT tunnel failed, response 403
```

El estado del proxy lo confirma como **denegación de política en la puerta de salida**:
`connect_rejected — gateway answered 403 to CONNECT (policy denial or upstream failure)`.

**Vigesimoprimera edición consecutiva. Cero portales leídos por acceso directo. Techo de confianza
del producto: ★★★★☆; ninguna ficha lleva ★★★★★.** `docs/solicitud-lista-blanca-egreso.md` sigue sin
tramitar y sigue siendo el único cambio que elevaría ese techo.

⚠️ **`gabinetedeseguridad.gob.mx/resultados/` pasa a ser obligatorio el 1 de septiembre: quedan
cinco días.** Sigue ilegible por acceso directo. ARGOS 110 y 111 deben dejarlo declarado; a partir
del 1-sep su ausencia es un vacío exigible, no una limitación heredada.

---

## Rotación de cobertura — **CICLO B aplicado y declarado**

A ARGOS 109 le tocaba el **Ciclo B: Noreste + Golfo encabezan el triaje judicial**; Noroeste,
Occidente, Centro y Sureste encabezan con armamento. **Se aplicó y se cumplió.**

**Prioridad sobre el ciclo, también aplicada**: las tres fiscalías `NO REVISADA` heredadas de ARGOS
108 —**Jalisco, Aguascalientes y Nuevo León**— encabezaron el triaje de sus regiones **aunque no les
tocara por ciclo**. Occidente gastó sus primeras consultas en Jalisco y Aguascalientes; Noreste, en
Nuevo León. **Las tres quedan saldadas.**

### Qué aportó la rotación que el orden anterior no habría aportado

**El balance del Ciclo B es defensivo, y se registra sin inflarlo.** No produjo ninguna sentencia
integrable —igual que el Ciclo B de ARGOS 105 y a diferencia del Ciclo A de ARGOS 108—. Lo que sí
produjo:

1. **Golfo resolvió una reserva abierta de la edición anterior.** Encabezar con fiscalías lo llevó al
   **portal oficial del Gobierno de Veracruz**, que publicó el parte de San Andrés Tuxtla. De ahí
   salieron tres cosas que ARGOS 108 no tenía: **quién inició** (la autoridad acudió a un reporte y
   fue recibida a disparos → **sostiene el 🟡, no procede fe de erratas de color**), la **corrección
   de detenidos de 5 a 6**, y un **dato nuevo**: el rescate con vida de un empresario de 62 años.
   Es `ARG-109-FE-001`. **Entrando por armamento, ese portal no se habría tocado.**
2. **Golfo descartó dos trampas de fecha antes de gastar presupuesto en amplitud**: un boletín de
   «sentencias por pederastia agravada» que resultó ser del **24-feb-2026**, y el agregado de
   **46 sentencias condenatorias de Veracruz**, que cubre el **19-25 de agosto** y **no individualiza
   ningún caso**. Los dos habrían sido falsos positivos caros.
3. **Noreste acreditó que la fiscalía de Nuevo León no publica en portal**, consultada en tres
   formas. Es dato de método reutilizable: no volver a gastar `site:` ahí.
4. **Noreste precisó —sin resolverla— la pregunta operativa de Zacatecas** (ver abajo).

**A ARGOS 110 le toca el Ciclo C — Occidente + Sureste.**

---

## Bloque 3.1 — el cambio de método, ejecutado y medido

El hallazgo de ARGOS 108 fue que **cinco de sus ocho hechos los aportó el recall nacional, no los
seis barridos regionales**, porque con los portales bloqueados un barrido organizado por `site:` no
ve los hechos que solo publican los medios. La instrucción de esta edición fue **subir la fracción
de consulta genérica por entidad** y **ejecutar el recall nacional antes de cerrar ningún barrido**.

**Se ejecutó así**, y el resultado invierte el de ARGOS 108:

| Origen | Hechos aportados |
|---|---|
| **Barridos regionales** | **4 de 6** — Tacámbaro (Occidente), Loxicha (Sureste), Querétaro (Centro), Mexicali (Noroeste) |
| **Recall nacional del coordinador** | **2 de 6** — Tampico/Altamira y San Bernardino Tlaxcalancingo. Noreste localizó Tampico **también**, por consulta genérica |

**El cambio de reparto funcionó y hay que conservarlo.** Las seis regiones declararon haber gastado
el grueso del presupuesto en consulta genérica sin `site:`, y **las cuatro que aportaron hecho lo
hicieron por esa vía, no por `site:`**. Occidente lo dice expresamente: «el único hecho de alto
impacto confirmado dentro de la ventana se obtuvo por consulta genérica de medios regionales, no por
barrido de dominio institucional». Sureste, que en ARGOS 108 no vio los dos hechos de Guerrero,
dedicó ~14 de 22 búsquedas a consulta genérica y **aportó Loxicha**.

**Matiz que no debe perderse**: el recall nacional **sigue siendo obligatorio y sigue rindiendo**.
Aportó dos hechos que ningún barrido regional trajo primero, y —más importante— **interceptó cuatro
falsos positivos** que las regiones no vieron porque no eran suyos (ver abajo).

### Presupuesto declarado por región

| Región | Gastado / asignado | Desviación |
|---|---|---|
| Noroeste | 20 / 20 | — |
| Noreste | **25 / 20-22** | Declarada. Concentrada en el corredor de Zacatecas y en la fecha de Candela |
| Occidente | 20 / 20 | — |
| Centro | **23 / 20-22** | Declarada. Justificada por el cierre de los dos candidatos vivos |
| Golfo | **21 / 20** | Declarada |
| Sureste | 22 / 20-22 | En el techo del rango |

Tres regiones se desviaron y **las tres lo declararon**. Se acepta declarado, nunca disimulado.

---

## Trampas interceptadas en esta edición

Ocho descartes que habrían sido errores publicados. Los cuatro primeros los interceptó el **recall
nacional del coordinador**, no los barridos.

| Candidato | Qué parecía | Qué era | Control que lo atrapó |
|---|---|---|---|
| **Luis Moya, Zacatecas** — «5 abatidos y 2 detenidos» | Enfrentamiento en la región prioritaria del corte | **Doble trampa.** La nota con esas cifras es de **2024** (`informador.mx/…20240630`). Y el hecho de agosto de 2026 en Luis Moya es del **31-jul** (policía muerto por explosivo); los **5 abatidos** son de **Calera**, el **1-ago** | Verificación de fecha en la ruta |
| **Tula de Allende, Hidalgo** — «3 abatidos, 1 oficial herido, 2 detenidos» | Enfrentamiento del corte | Hecho del **21-feb-2026** (`latinus.us/mexico/2026/2/21/`) | Trampa de mes: `/2026/2/` frente a `/2026/8/` |
| **Santo Domingo Zanatepec, Oaxaca** — 3 muertos en salón de fiestas | Hecho de alto impacto | Hecho del **14-ago-2026**, publicado el 15 | Fecha en la ruta |
| **El Roble, Mazatlán** — «26 vinculados, 15 fusiles, 2,744 cartuchos, 118 cargadores» | Aseguramiento nuevo del 26-ago | **Es la vinculación a proceso** de un aseguramiento **ya contabilizado en ARGOS 92** (`ARG-92-002`, 8-ago: 15 largas, 94 cargadores, 2,964 cartuchos). Vinculación a proceso **no es sentencia** y el armamento **no se recuenta** | **`grep` al índice** — igual que en ARGOS 108, lo resolvió el archivo, no la web |
| **Cintalapa, Chiapas** | Agresión armada dentro de ventana | La nota dice **«a media tarde del jueves»**; el jueves de esa semana es el **27-ago**, y su tarde es **posterior al cierre de la ventana**. La URL solo ancla `/2026/08/` | **Coherencia interna: día de la semana contra calendario** — el mismo control que salvó a ARGOS 103 |
| **Armería, Colima** — 2 muertos, 26-ago | Hecho del corte | Ocurrió a las **12:52 h**, **antes de la apertura de la ventana (14:21)** | Hora publicada |
| **Durango capital** — «8 largas, 4 cortas, 65 cargadores» | Aseguramiento del 26-ago | El artículo **se contradice a sí mismo**, y el par **8 largas / 4 cortas es idéntico** al de **Mapimí, 15-ago**, ya publicado. El resumidor reutilizó cifras de otro evento | Contradicción interna + memoria de la serie |
| **Acapulco, Cumbres de Llano Largo** — taxi atacado, 1 muerto y 1 herida | Hecho nuevo, «distinto al de Costa Azul» | **Es el mismo saldo y el mismo patrón que `ARG-108-003`**, y «Cumbres de Llano Largo» es precisamente **la ubicación alternativa que ARGOS 108 ya declaró como contradicción** del agregado de jornada. Sin URL primaria fechada | **`editor-duplicidad`** — habría entrado como hecho nuevo del corte |

### Boletín federal — regla de la triple consulta, ejecutada

Consultado **en las tres formas**: por **día suelto** («acciones relevantes del 26 de agosto»), por
**rango o agregado**, y por **título sin restricción de dominio** para alcanzar republicadores.

**Resultado**: el más reciente con URL propia verificable es el del **25 de agosto** (localizado vía
republicador `red113mx.com/2026/08/`). **No existe boletín del 26 ni del 27 con URL propia.** El
resumidor sí afirma contenido del 26-ago —«en Sonora, dos detenidos y ~20 kg de fentanilo y
heroína»—, **sin devolver enlace citable**. `SIN URL PROPIA — NO EXISTE PARA ARGOS`.

**Cuarta edición consecutiva** en que el resumidor afirma un boletín federal que no devuelve URL.
La regla de la triple consulta sigue siendo el control correcto y sigue costando tres búsquedas.

---

## El seguimiento de máxima prioridad — corredor Juchipila–Tlaltenango–Tepechitlán

**La pregunta operativa no se cierra, pero se reformula, que es un avance real.**

La pregunta era: **¿la orden de aprehensión contra el director de Seguridad Pública de Juchipila
deriva de los cateos del 21-ago (`ARG-104-001`), que dejaron 10 detenidos y 2 personas liberadas?**

**Lo que se acreditó en este corte:**

- **Ninguna fuente publica el número de causa penal ni de carpeta.** Sin él, la pregunta no se cierra.
- **Sí consta, por declaración del Fiscal General de Zacatecas**, que **ambas detenciones de mando
  municipal** —Tlaltenango, 4-feb-2026, y Juchipila, 25-ago-2026— **se originaron «en el marco» del
  Plan de Seguridad Aguascalientes-Zacatecas (SAGAZ)**, activo **desde finales de junio de 2026**.
- **La detención de Juchipila se ejecutó «tras la ejecución de dos órdenes de cateo»**, del propio
  25-ago, **distintas de las del 21-ago**.
- Los detenidos fueron trasladados a la **Fiscalía Especializada contra Secuestro, Extorsión y
  Delitos de Alto Impacto** y quedaron en el **CERERESO Varonil de Cieneguillas**.

**Por qué esto importa y no es un no-resultado.** La lectura simplista —«misma carpeta que el
21-ago»— **queda descartada como afirmación sostenible**, y se sustituye por una más precisa y más
útil: **el vínculo acreditado entre los dos mandos municipales caídos no es una carpeta, sino un
plan de investigación interestatal de seis meses**. Eso cambia a quién hay que preguntar: no a la
carpeta del cateo, sino a **la coordinación SAGAZ**, que es donde está el mapa de qué corporaciones
municipales del corredor están bajo escrutinio. **La recomendación de revisión preventiva de control
de confianza en todo el corredor Juchipila–Tlaltenango–Tepechitlán se mantiene y se refuerza.**

**Sigue sin publicarse**: identidad y plaza de origen de los **cuatro abatidos de Tepechitlán**
(25-ago) y **qué armamento se les recogió**. Rastreado en cinco coberturas distintas; **ninguna lo
reporta**. Se confirma que **la autoridad no lo publicó**, que es distinto de que ARGOS no lo
encontrara.

**Confirmado además**: los boletines de `ssp.zacatecas.gob.mx` y `zacatecas.gob.mx` **no llevan fecha
en la ruta**. Es la razón estructural por la que la trampa de aniversario de Tepechitlán fue posible
en ARGOS 108, y seguirá siéndolo.

---

## Cobertura del barrido — 32 de 32 entidades

Seis agentes `barrido-regional` en paralelo, autorizados por el destinatario y lanzados **en un solo
mensaje antes de ningún otro encargo**, con la deuda de portal de ARGOS 108 al frente de cada región
y con la instrucción del Bloque 3.1 sobre el reparto de presupuesto.

| Región | Entidades | Triaje | Portales que quedaron `NO REVISADA` |
|---|---|---|---|
| Noroeste | 6 de 6 | Armamento | SSPE de BC y BCS, SSPCE Chihuahua, SSP Durango; fiscalías de Sonora y BCS; GN prensa, SEDENA/IV RM, SEMAR Pacífico Norte, FGR, ANAM; mesas de paz |
| Noreste | 5 de 5 | **Judicial (Ciclo B)** | SSP de Coahuila, Tamaulipas y SLP; SSP/Fuerza Civil de Nuevo León; mesas de paz de las 5; SEDENA, SEMAR, FGR y ANAM regionales |
| Occidente | 6 de 6 | Armamento | SSP de las 6 entidades; mesas de paz de las 6; SEDENA, GN, FGR, ANAM; contenido de prensa de la SSyPC de Nayarit |
| Centro | 7 de 7 | Armamento | SSP de Puebla y Tlaxcala; **Tlaxcala con cobertura débil, equivalente a `NO REVISADA`**; SEMAR y FGR regionales; ANAM |
| Golfo | 2 de 2 | **Judicial (Ciclo B)** | SSPC Tabasco; policías estatales de ambas; mesas de paz de ambas; delegaciones FGR |
| Sureste | 6 de 6 | Armamento | SEDENA VII/IX/XI RM; policías estatales diferenciadas de las 6; mesas de paz; GN prensa; delegaciones FGR |

**La cobertura es por entidad, no por portal.** Los portales sin ver se declaran `NO REVISADA`, nunca
`SIN ACTUALIZACIÓN`.

**Deuda de ARGOS 108 saldada**: las tres fiscalías `NO REVISADA` —**Jalisco, Aguascalientes y Nuevo
León**— fueron consultadas. **Deuda de SSP no saldada**: de los once portales de SSP pendientes
(Chihuahua, BC, BCS, Durango, Coahuila, Tamaulipas, SLP, Puebla, Tlaxcala, Nayarit, Tabasco),
**ninguno se consultó como portal propio**. Es la deuda más antigua del producto y **encabeza el
triaje de ARGOS 110 por prioridad sobre el ciclo**.

### Dominios oficiales — inventario actualizado

| Entidad | Estado | Dominio |
|---|---|---|
| **SSP de Nayarit** | ✅ **CERRADO en este corte** | **`ssypc.nayarit.gob.mx`** — **ni `ssp.nayarit.gob.mx` ni `sspc.nayarit.gob.mx`**, que eran las dos hipótesis heredadas. **Las dos eran falsas** |
| **Fiscalía de Michoacán** | ✅ **CONFIRMADO en este corte** | `fiscaliamichoacan.gob.mx`, con subdominios activos `comunicacion.`, `juridico.` y `directorio.` — **no** `fge.michoacan.gob.mx` |
| **Fiscalía de Sinaloa** | ✅ **CONFIRMADO en este corte** | **`fiscaliasinaloa.mx`** (sección «Boletines Informativos» localizada) — **no** `fiscaliasinaloa.gob.mx` |
| Querétaro | Confirmado, **el mejor formato de la serie** | `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` |
| Chihuahua | Confirmado y funcional vía `site:` | `fiscalia.chihuahua.gob.mx` |
| Tlaxcala | Confirmado en ARGOS 108 | `fgjtlaxcala.gob.mx` · anticorrupción `fecc.fgjtlaxcala.gob.mx` |
| Nayarit (fiscalía) | Confirmado en ARGOS 108 | `fiscaliageneral.nayarit.gob.mx` |
| Aguascalientes (SSP) | Confirmado en ARGOS 108 | `aguascalientes.gob.mx/ssp/` · IESPA en `/IESPA/` |
| Colima | Confirmado en ARGOS 107 | `fgecolima.mx` |
| **Guanajuato** | ⚠️ sigue sin confirmar | Se mantiene el agregador `boletines.guanajuato.gob.mx`, **sustitución declarada** |
| **Sonora** | ⚠️ sigue sin confirmar | `fgjsonora.gob.mx` no probado en este corte |
| **SSP de Zacatecas** | ⚠️ **advertencia estructural** | `ssp.zacatecas.gob.mx` existe pero **sus boletines no llevan fecha en la ruta**. Ninguna cifra suya entra sin ancla externa |

**Tres dominios cerrados en un solo corte**, dos de ellos —Nayarit y Sinaloa— **desmintiendo la
hipótesis heredada**. Es dato que ARGOS 110 no tiene que volver a pagar.

---

## Candidatos vivos heredados — los dos cerrados

**1. Morelos · Cuautla — Luis Ángel «N», extorsión agravada, 16 años 8 meses (FIDAI).**
**RETIRADO DE CANDIDATOS.** Segunda edición consecutiva sin lograr **una sola URL con fecha en la
ruta**; el «25-ago» procede del resumidor. Cuatro búsquedas adicionales sobre
`fiscaliamorelos.gob.mx` y medios locales no devolvieron nada que lo fije.

**Agravante decisivo hallado en este corte, y es un hallazgo de método reutilizable**: existen
**al menos otros dos casos de extorsión agravada en Cuautla y Jiutepec con la pena exacta de
16 años 8 meses**, obtenidos por la misma fiscalía mediante procedimiento abreviado. **Es la firma
del abreviado**: la reducción está tarifada y casos distintos convergen en el mismo número.
Consecuencia general: **en delitos con alto uso de procedimiento abreviado, la pena deja de ser
campo individualizador** y no puede contarse entre los ≥2 campos que la regla del *slug* exige.
Es exactamente el error que hizo caer a ARGOS 98 en Coronango. **Se aplica el umbral de fe de
erratas por acumulación: se retira del acumulado y no vuelve a listarse como candidato.**

**2. SSC CDMX — comunicado 946 (cargadores y 400 cartuchos, Gustavo A. Madero).**
**DESCARTADO — FUERA DE VENTANA.** Hallazgo de método: **SSC CDMX reutiliza el número de comunicado
entre años bajo esquemas de URL distintos**. El formato vigente en 2026 es `COM<n>-DD-MM-AAAA`
—verificado con un `COM946-02-04-2026` que es **otro comunicado, sobre extorsión tipo
«montachoques» en Venustiano Carranza, del 2-abr-2026**—, mientras la URL candidata no lleva fecha
alguna. La evidencia apunta a un hecho **anterior a 2026**. No es ambiguo: está fuera.

**Regla nueva que de aquí se deriva**: *verificar siempre el esquema de URL vigente del emisor en el
año del corte antes de aceptar un número de comunicado sin fecha como candidato.*

---

## Controles editoriales antes de publicar

**Ejecutados a mano, con el mismo criterio, y se declara.** La autorización de subagentes de esta
sesión cubrió **los seis barridos**; `editor-duplicidad` y `procedencia-cifras` **no se invocaron
como agentes**. Es la **cuarta edición consecutiva** en esa situación, y la cuarta en que **ambos
producen hallazgos reales**.

### `editor-duplicidad` — hallazgos

1. **Interceptó un hecho que iba camino de publicarse como nuevo**: el ataque a un taxi colectivo en
   **Cumbres de Llano Largo, Acapulco**, que el barrido de Sureste trajo como «hecho distinto» del de
   Costa Azul. **Mismo saldo (1 muerto, 1 herida), mismo patrón y sin URL primaria fechada**, y
   «Cumbres de Llano Largo» es **precisamente la ubicación alternativa que ARGOS 108 ya declaró como
   contradicción** del agregado de jornada de `ARG-108-003`. Publicarlo habría duplicado un hecho ya
   fichado y, peor, habría convertido una contradicción declarada en dos hechos.
2. **Verificó el trasvase ficha → tabla de módulo**: los aseguramientos y detenidos de las cuatro
   fichas con armamento llegan íntegros a la tabla de la pág. 5. **Detenidos: 3+2+2+1 = 8**, que es
   la cifra de la tarjeta.
3. **Verificó que ningún hecho con ficha propia se repite en tabla resumen**: no hay «Ejes del día»
   ni resumen ejecutivo; la tabla de armamento **remite a la ficha por enlace** y aporta campos
   distintos (corporación, confianza, desglose por taxonomía).
4. **Deslinde de duplicidad publicado en el cartelón**: Tampico/Altamira **no es** `ARG-100-001`
   (Altamira, 297,000 L, 17-ago). Distinta fecha, distinto volumen, distinto conjunto de inmuebles.

### `procedencia-cifras` — hallazgos, tres de ellos contra el propio borrador

1. **Retiró dos distancias geográficas estimadas por el redactor** —«a más de mil kilómetros»,
   repetida en la ficha de Puebla y en la conclusión 6—. **Son cifras inferidas y están prohibidas.**
   Se sustituyeron por la afirmación cualitativa «en el extremo opuesto del país», que sostiene igual
   el análisis. **Es el mismo defecto que el control retiró en ARGOS 108**: el redactor reincide y el
   control vuelve a atraparlo.
2. **Obligó a declarar dos sumas propias**: el **total de 9 armas** de la ventana y los **8 detenidos**
   son **cálculo propio de ARGOS** sobre cifras publicadas evento por evento; ninguna autoridad
   publicó agregado nacional de este corte. Ahora van marcados como tales en el cartelón.
3. **Exigió respaldo a una cifra heredada**: los «297,000 litros» usados en la conclusión 7 para
   comparar volumen proceden de una edición anterior. Se les añadió su ARG-ID (`ARG-100-001`), y
   la cifra tiene además corroboración externa. **ARGOS no es fuente de sí mismo**, pero sí puede
   citarse a sí mismo si señala el renglón.
4. **Retiró el desglose de Durango** («8 largas, 4 cortas, 65 cargadores»): el artículo se contradice
   y las cifras coinciden exactamente con las de Mapimí del 15-ago.
5. **Rechazó «más de veinte cartuchos»** (Tijuana): no es cifra exacta y **nunca se redondea**.
6. **Rechazó las cifras de El Roble/Mazatlán** por doble conteo (ver arriba).

### `barrido-regional` ×6 — condición previa cumplida

32 de 32 entidades. Ninguna casilla `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de esta edición se
declaró sin barrido previo.

---

## Nota sobre la frontera de ventana

**Cinco de los seis hechos llevan la marca `FRONTERA DE VENTANA — HORA NO FIJADA`.** Es la
proporción más alta de la serie desde ARGOS 102. La causa es estructural y ya está descrita en
`CLAUDE.md`: **las ventanas de ARGOS se declaran con precisión de minutos y las fuentes publican con
precisión de día**. Con una ventana corta (19 h 39 min) que abre a media tarde, casi todo lo
publicado el día de apertura cae en la franja indecidible.

**Consecuencia declarada en el cartelón, como exige la regla**: los totales de ARGOS 109 **no son
comparables sin más** con los de ediciones cuyos hechos quedaron fijados por hora dentro de ventana.
Las cinco marcas son permanentes; si aparece un ancla horaria que sitúe alguno antes de las 14:21 del
26-ago, se corregirá por fe de erratas y se retirará del total.

---

## Hechos de la edición — índice rápido

| ARG-ID | Entidad · Municipio | Color | Confianza |
|---|---|---|---|
| `ARG-109-001` | Michoacán · Tacámbaro / Salvador Escalante | 🔴 | ★★★★☆ |
| `ARG-109-002` | Oaxaca · San Agustín Loxicha | 🔴 | ★★★☆☆ |
| `ARG-109-003` | Baja California · Mexicali | 🔴 | ★★★★☆ |
| `ARG-109-004` | Puebla · San Bernardino Tlaxcalancingo | 🟡 | ★★★★☆ |
| `ARG-109-005` | Querétaro · Querétaro y San Juan del Río | 🟢 | ★★★★☆ |
| `ARG-109-006` | Tamaulipas · Tampico y Altamira | 🟢 | ★★★☆☆ |
| `ARG-109-ARM-001` a `-004` | Michoacán, Puebla, Querétaro, Tamaulipas | — | Medio / Medio / **Alto** / Medio |
| `ARG-109-FE-001` | Fe de erratas sobre `ARG-108-004` (Veracruz) | — | ★★★★☆ |

**Sentencias integradas: 0.** **Recuperaciones `-REC-`: 0** — el barrido y el recall no localizaron
ningún hecho de alto impacto de ventanas anteriores sin publicar.

---

## Construcción y validación

```
python3 tools/gen-movil.py 109 2026-08-27 108 2026-08-26 10:00
→ escrita reports/argos-2026-08-27-movil.html (168,102 bytes)
→ contadores del generador: 🔴 3  🟡 1  🟢 2
→ tarjetas: móvil 8 / escritorio 8
→ validación OK
```

Comprobado además: `<title>` actualizado · **`<body>` duplicado de ARGOS 108 corregido** (la edición
anterior traía dos etiquetas `<body>` consecutivas; se dejó una) · sintaxis del script del escritorio
validada con `node --check` · 6 tablas, **todas envueltas exactamente una vez** en `table-wrap` ·
**0 anidamientos `tabla-scroll`** · 0 clases de escritorio en la móvil (`sem-item`, `stat-tile`,
`cover-visuals`, `masthead`) · 15 iconos en ambas versiones · 11 ARG-ID en ambas versiones ·
0 tarjetas `.reg` sin texto · `EVENTOS_ARM` poblado y `div#argos-map-arm` **restituido** (ARGOS 108
lo había omitido por no tener aseguramientos).

La tabla de desglose por evento, de **13 columnas**, se reflúa a tarjetas en la móvil por diseño del
generador: **no se pierde ningún dato**, y así lo declara la propia versión de teléfono.
