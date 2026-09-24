# ARGOS 112 — Archivo de fuentes y trazabilidad

**Corte**: 2026-08-31 · **Hora de cierre**: 09:28 CDMX (verificada con `TZ=America/Mexico_City date`, no supuesta)
**Ventana**: **2026-08-29 09:05 → 2026-08-31 09:28 CDMX** (48 h 23 min). Continuación estricta de ARGOS 111, sin hueco ni solape.

Este archivo contiene lo que **no** va al cartelón: hallazgos de método, fes de erratas, cobertura del
instrumento, rendimiento de la rotación y candidatos descartados. El cartelón es para el mando; esto
es para la auditoría.

---

## 0. Verificación de base (Bloque 0 del arranque)

| Comprobación | Esperado | Encontrado |
|---|---|---|
| Última edición en `reports/` | `argos-2026-08-29` (ARGOS 111) | ✅ `argos-2026-08-29` |
| Archivos en `reports/` | 78 | ✅ 78 |
| `main` contiene ARGOS 111 | Sí | ✅ `2e7a4c8 Generar ARGOS 111 (corte 2026-08-29)` |
| `git merge --ff-only origin/main` | Primer comando de la sesión | ✅ ejecutado antes de leer `CLAUDE.md` |

⚠️ **La rama asignada volvió a llegar desactualizada, por sexta edición consecutiva.** Al arrancar,
`claude/argos-daily-report-5qt6km` mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición y
**no contenía su propio archivo de arranque** `_arranque-ARGOS-112.md`. Numerar por lo que la rama
tenía a la vista habría producido **un falso «ARGOS 107» con ventana solapada de una semana**.
**El `merge --ff-only` lo resolvió y la numeración salió del archivo, no de la rama.** El modo de
fallo es estable y la contramedida también: **mantener el merge como primer comando.**

---

## 1. Estado del egreso — vigesimocuarta edición

**Verificado en esta sesión, no heredado.**

```
curl https://www.gob.mx/sspc                      → curl: (56) CONNECT tunnel failed, response 403
curl https://gabinetedeseguridad.gob.mx/resultados/ → curl: (56) CONNECT tunnel failed, response 403
```

**Cero portales leídos por acceso directo.** Toda consulta institucional fue por buscador, con
**sustitución anotada** en cada ficha que la usó. **Techo de confianza del producto: ★★★★☆**;
ninguna ficha lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.

**Consecuencia sobre las casillas de cobertura**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable**
en estas condiciones —exige lectura directa del listado de boletines— y por eso figura en **0** en
todos los módulos. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.

---

## 2. Rotación de cobertura — **CICLO B**, declarado y aplicado

**A ARGOS 112 le tocaba el Ciclo B: Noreste + Golfo encabezan el triaje judicial**; Noroeste,
Occidente, Centro y Sureste encabezan con armamento. **Se aplicó y se declara aquí, como exige la
metodología.**

**Qué aportó el Ciclo B que el orden anterior no habría aportado** — y esta vez el rendimiento es
alto y verificable en las dos regiones:

| Región | Aporte atribuible al encabezamiento judicial |
|---|---|
| **Golfo** | **La única sentencia integrable del corte.** Tras **cinco cortes** en que la FGE de Veracruz solo publicó agregados sin individualizar, el caso salió de la **delegación federal de la FGR** en Papantla, con nombre, delito, pena exacta, multa y **fecha en la ruta**. Un triaje que empezara por armamento, con 2-3 búsquedas restantes para lo judicial, **no habría llegado**. Además **saldó la deuda de `fiscaliatabasco.gob.mx`**, que arrastraba `NO REVISADA` |
| **Noreste** | **Cerró definitivamente el candidato de mayor volumen que la edición anterior dejó vivo** (Tabasco, Zacatecas) y **arbitró el dominio de San Luis Potosí**, que arrastraba `NO REVISADA` |

**Es la tercera vez consecutiva que la rotación produce la única sentencia del corte en la región a
la que le tocaba encabezar** (Noroeste/Durango en ARGOS 101 y 111; Golfo/Veracruz en ARGOS 112).
**El mecanismo no es cosmético: cambia lo que el producto encuentra.**

**Al siguiente le toca el Ciclo C — Occidente + Sureste.**

⚠️ **Con la prioridad por delante del turno**: la deuda de dominio (SLP, Tlaxcala, Tabasco) recaía
sobre regiones que el ciclo mandaba encabezar judicial o armamento indistintamente. **Se saldó
primero y el turno se conservó**, igual que en la edición anterior.

---

## 3. Reparto de presupuesto y origen de los hechos

**Objetivo**: ~60-65 % consulta genérica sin `site:` · ~25 % `site:` dirigido · ~10 % judicial.

| Región | Búsquedas | Genérica | `site:` | Desviación declarada |
|---|---|---|---|---|
| Noroeste | 19 | 68 % | 21 % | Leve alza en genérica, para desambiguar una conflación del resumidor |
| Noreste | 16 | 75 % | 25 % | Sin desviación relevante |
| Occidente | 19 | 89 % | 5 % | **Fuerte**: las genéricas por fecha aislaron mejor la ventana que el `site:` |
| Centro | 18 | 89 % | 11 % | **Fuerte**: el eje de armamento no dio hallazgos pese a reformular |
| Golfo | 15 | 87 % | 13 % | **Fuerte**: los dominios `.gob.mx` devolvían agregados sin fecha |
| Sureste | 20 | 55 % + seguimientos | 5 % | **Fuerte**: mismo motivo |

⚠️ **Las seis declararon desviación y cinco de las seis se desviaron en el mismo sentido: menos
`site:` del previsto.** No es indisciplina: es que **con el egreso bloqueado y el índice rezagado, el
`site:` sobre dominios oficiales devuelve *home pages*, agregados sin fecha o ruido**, mientras la
consulta genérica por fecha sí aísla la ventana. **El reparto objetivo de 25 % en `site:` fue
diseñado para un entorno con acceso directo y hoy no es alcanzable sin desperdicio.**
**Propuesta para la edición siguiente: bajar el objetivo de `site:` a ~15 % y declararlo, en vez de
seguir declarando seis desviaciones por edición contra un objetivo que el entorno no permite.**

### Origen de los hechos publicados

| Origen | Hechos |
|---|---|
| **Recall nacional del coordinador** | **4 de 7** — Ojocaliente, Villa García, la detención de Villa García y la serie de tres ataques que los encadena |
| Barridos regionales | **3 de 7** — Sabinas Hidalgo y el ancla de Zacatecas (Noreste), sur de Sinaloa y Maguarichi (Noroeste), Acapulco (Sureste), Papantla (Golfo) |

⚠️ **El recall del coordinador aportó los dos hechos rojos del corte y la serie que los explica, y lo
hizo antes de que cerrara ningún barrido.** Ninguna de las seis regiones trajo Ojocaliente ni Villa
García en su primera entrega: el Noreste sí trajo Ojocaliente, pero **después** y sin la serie.
**Es la tercera edición consecutiva en que el recall nacional aporta lo que las regiones no ven, y la
primera en que aporta el hecho principal.** **La razón es estructural**: un hecho nacional de gran
cobertura se busca mejor por tema que por entidad, y los barridos están organizados por entidad.
**Mantener el recall como paso obligatorio previo al cierre de los barridos.**

---

## 4. La triple consulta del boletín federal — ejecutada en sus tres formas

Los días **29, 30 y 31 de agosto** se declaran `SIN RESULTADO INDEXADO EN VENTANA` **solo después de
las tres formas**, como exige la regla tras tres falsos vacíos del mismo emisor:

| Forma | Consulta | Resultado |
|---|---|---|
| **1. Día suelto** | «acciones relevantes del 30 de agosto de 2026», «...del 28 de agosto de 2026», «...del 29 de agosto de 2026» | Sin resultado del periodo |
| **2. Rango / agregado** | «"Gabinete de Seguridad" resultados "29, 30 y 31 de agosto" 2026» | Sin resultado; devuelve el agregado de **mayo** con el mismo patrón de fechas |
| **3. Título sin `site:`** | Título literal completo del boletín, sin restricción de dominio, para alcanzar republicadores | Sin resultado |

**Último boletín indexado: el del 27 de agosto**, alcanzable **solo por republicadores** (fue la
fe de erratas de la edición anterior). **Del 28 en adelante, nada.**
⚠️ **El borrador llegó a decir «26 de agosto» y lo corrigió `procedencia-cifras`.** El error era
menor en la cifra y grande en el método: **decir 26 habría borrado la corrección que la edición
anterior costó una fe de erratas**, y habría reabierto como vacío un día ya acreditado.

⚠️ **Conclusión de método, y es distinta de la de ediciones anteriores**: **no se declara que el
boletín no exista.** Se declara que **no está indexado**, y hay prueba de que el emisor **sí
comunicó** durante la ventana: los resultados de **Sabinas Hidalgo** y del **sur de Sinaloa** se
conocen por **declaración del titular de la SSPC y del Gabinete citada en medios**, no por el
boletín numerado. **El emisor comunicó por otra vía.** Esto **no es un cuarto falso vacío**: es un
vacío de índice correctamente acotado, con la vía alternativa localizada y usada.

---

## 5. Barrido de portales — cobertura y deuda de dominio

**32 de 32 entidades revisadas.** Ninguna quedó `NO REVISADA`.

### Deuda de dominio saldada en este corte

| Entidad | Resultado |
|---|---|
| **San Luis Potosí** | ✅ **`seguridad.slp.gob.mx` es el portal vivo**, sirve boletines con **fecha en la ruta** (`/noticias/AAAA/M/D/slug`). `sspslp.mx` existe como alterno sin contenido verificado; **`sitio.sanluis.gob.mx/SSPC/` no aparece en ningún resultado — no confirmado, no declarado inexistente**. La fiscalía, `fiscaliaslp.gob.mx/vi/`, está viva pero con *slugs* **sin fecha en la ruta**: respaldo más débil. **Sale de `NO REVISADA`** |
| **Tlaxcala** | ✅ **SE CIERRA COMO VACÍO ACREDITADO.** **Segunda confirmación consecutiva**: ambos dominios (`ssc.tlaxcala.gob.mx` y `ssctlaxcala.gob.mx`) **resuelven**, y ninguno publica boletines individuales fechados — **solo informes acumulados de periodo** (semestral, anual). **La respuesta a la pregunta era que ninguno publica boletín fechado.** Deja de arrastrarse |
| **Fiscalía de Tabasco** | ✅ **CONSULTADA** por genérica y dirigida, tras arrastrar `NO REVISADA`. `fiscaliatabasco.gob.mx/Boletin/Index/…` está vivo pero **sus boletines no llevan fecha en la ruta ni en el titular**; el resumidor mezcló hechos de 2017, 2024, mayo y junio de 2026 bajo el mismo dominio. `SIN RESULTADO INDEXADO EN VENTANA` |
| **FGE Veracruz** (`ARG-111-SEN-C01`) | ✅ **SE CIERRA COMO VACÍO ACREDITADO DEL EMISOR.** **Quinto corte consecutivo** de agregados —«70 resoluciones en 24 horas», «31 sentencias en una semana»— **sin individualización y sin fecha en la ruta**, mezclando sentencias con vinculaciones e imputaciones. **Deja de listarse como candidato.** La vía útil en Veracruz es la **FGR**, no la FGE |

### Anomalía de portal — Nayarit: persiste, en otra forma

La consulta **genérica sin `site:`**, como se ordenó antes de reintentar, **no reprodujo la página de
apuestas** de la edición anterior. Devolvió el directorio de `ssypc.nayarit.gob.mx` sin boletines
localizables. La consulta `site:` devolvió **seis artículos de Wikipedia sobre geografía de Nayarit**
más una página «Archivo» vacía.
**Se mantiene `PORTAL NO DISPONIBLE — índice sin boletines localizables`, nunca `SIN ACTUALIZACIÓN`.
Ninguna cifra suya se usó.** **El síntoma cambió; el diagnóstico no.**

### Cobertura declarada — las tres casillas

| Casilla | Módulo armamento | Módulo sentencias |
|---|---|---|
| `SIN ACTUALIZACIÓN CONSTATADA` | **0** | **0** — exige lectura directa, imposible con egreso bloqueado |
| Publicaron dentro de la ventana | **3** — Nuevo León, Sinaloa, Guerrero (por cita, sin boletín propio en Guerrero) | **1** — FGR, delegación de Veracruz |
| `SIN RESULTADO INDEXADO EN VENTANA` | **28 entidades** | **32 fiscalías** |
| `NO REVISADA` | **0** | **0** |
| `PORTAL NO DISPONIBLE` | **1** — `ssypc.nayarit.gob.mx` | — |

**Cuadre del módulo de armamento: 3 publicaron + 28 sin resultado indexado + 1 portal no disponible = 32.** El cuadre se hace explícito porque una versión previa de esta tabla sumaba 30 y **una casilla de cobertura que no cuadra con el universo es una cobertura no demostrable** — lo detectó `editor-duplicidad`.

### Portales que publicaron dentro de la ventana

**Uno solo, y es federal**: la **FGR** (delegación de Veracruz, caso Papantla), alcanzado por
republicador con fecha en la ruta. **Ninguna de las 32 fiscalías estatales ni ninguna SSP estatal
publicó dentro de la ventana.**

⚠️ **Y esta vez hay una causa de calendario que debe declararse**: **la ventana cubre sábado 29,
domingo 30 y la mañana del lunes 31**. Es decir, **una sola mañana hábil**. Las corporaciones y las
fiscalías publican en días hábiles. **Buena parte del vacío de esta edición es de calendario, y los
totales no son comparables sin más con los de ediciones cuya ventana cae entre semana.** Esta
advertencia está declarada también en el cartelón, en la valoración.

### Siguen sin revisar como portal propio

**SEDENA / SEMAR / FGR / ANAM regionales** y las **Mesas de Construcción de la Paz** — **sexta
edición consecutiva**. Ninguna región llegó a ellas con presupuesto disponible.

---
## 6. Seguimientos — resultado, eje por eje

### Eje 1 · **NACIONAL — la protección balística**: `SIN AVANCE`, y ahora es una omisión acreditada en seis regiones

**Era el seguimiento de mayor prioridad del corte y se probó en las seis regiones.** Resultado:
**ninguna autoridad ha publicado marca, nivel NIJ ni lote de una sola de las 25 placas balísticas**
aseguradas en las tres semanas previas (Escuinapa 7 + 10, Tepic 2, La Guásima 6).

- **Occidente**, que tiene Tepic, buscó marca/lote/NIJ/importador y solo obtuvo el **marco
  regulatorio genérico de importación** (SAT, VUCEM) y comercio de placas civiles: **nada del caso**.
  Reconfirmó el desglose de Tepic ya publicado, sin un solo campo nuevo.
- **Noroeste** confirmó `SIN AVANCE` en Escuinapa y La Guásima.
- **Sureste** solo encontró **dotación institucional** (Chiapas entregó 500 chalecos con 1,000 placas
  a su propia SSP en abril de 2026) — **no es un aseguramiento y no se integra**; se registra para
  que no vuelva a aparecer como candidato.
- **Centro, Noreste y Golfo**: `SIN RESULTADO INDEXADO EN VENTANA`.

⚠️ **Esta ventana no aportó ninguna placa nueva**, con el mayor volumen de armas largas de la serie.
**El seguimiento cambia de naturaleza**: deja de ser «falta un dato de unos casos» y pasa a ser
**una omisión sistemática de campo** — se consigna calibre en las armas y no se consigna marca ni
nivel en el equipo de protección. **Se publicó como conclusión de inteligencia del cartelón**, porque
lo accionable no es una búsqueda más sino **un cambio en lo que la autoridad consigna**.

### Eje 2 · **SINALOA — Concordia produce, no recibe**: `SIN AVANCE` en la pregunta, **pero avance real por otra vía**

- **La pregunta directa sigue sin respuesta**: de los 49 artefactos de Concordia (28-ago) y los 172 de
  La Guásima (18-ago) **no se ha publicado tipo, iniciación, carga ni contenedor**; las fuentes solo
  reiteran que el material quedó a disposición de la FGR «para determinar el origen», y **confirman
  que los 49 fueron destruidos por detonación controlada**. **Nada sobre la cadena de precursores.**
- ⚠️ **Y el corte añadió un tercer caso: seis artefactos más en Palo Blanco el 29-ago, también
  destruidos en el lugar «por riesgo de traslado».** **227 artefactos en trece días en la misma zona,
  cero caracterizados públicamente.**
- ✅ **El avance vino de donde no se buscaba, dos veces:**
  1. **Villa García (Zacatecas) publicó el sistema de iniciación y el contenedor** —motocicleta,
     detonación remota—, que es **exactamente el campo que se pedía para Sinaloa** y que ningún
     boletín de Sinaloa ha dado. **Lo aportó la cobertura del hecho, no un peritaje.**
  2. **Maguarichi (Chihuahua) contestó la pregunta de la cadena comercial de precursores a escala
     nacional**: 5,234 detonadores eléctricos, 1.1 t de agente explosivo a granel y 6,324 piezas, en
     **camionetas con reporte de robo en Estados Unidos**. **Frente a los 5 fulminantes eléctricos del
     taller de Jiménez del Teul, es una diferencia de tres órdenes de magnitud.**

**Reformulación del seguimiento para la edición siguiente**: la pregunta ya no es «de dónde saca
Concordia los precursores», sino **«qué proporción del explosivo industrial desviado del comercio
legal alimenta la manufactura de artefactos»**. Es una pregunta de **bitácora de polvorines y robo
de material industrial**, no de buscador.

### Eje 3 · **ZACATECAS**: la pregunta del lote no se reabrió; la contradicción de lesionados sigue abierta y **el candidato del ancla queda cerrado**

- ✅ **No se reabrió la pregunta del lote ni el «antecedente del 1 de agosto»**, conforme a la
  instrucción: quedó cerrada por mal planteamiento y **no se gastó ni una búsqueda en ella**.
- ⚠️ **Contradicción de lesionados de `ARG-110-001`: SIGUE ABIERTA, y ahora con las dos partes
  nominadas.** El **fiscal Cristian Camacho Osnaya** sostiene **«cinco lesionados fuera de peligro»**
  (cuatro policías de investigación y un perito); el **Secretario de Gobierno** sostiene **«dos
  policías heridos»**. **Ninguna de las dos partes ha rectificado.** Se mantiene
  `CONTRADICHA — NO SE ARBITRA SIN FUENTE DIRECTA`. **Avance real**: la posición de la Fiscalía queda
  **atribuida a persona con nombre**, no a «la Fiscalía» genérica, lo que la hace exigible.
- ✅ **CERRADO — el candidato de mayor volumen que ARGOS 111 dejó vivo.** Los **11 detenidos y 10
  armas largas** del municipio de **Tabasco, Zacatecas**, publicados por `zacatecas.gob.mx` sin fecha
  en la ruta, **son del 15-16 de octubre de 2025**, acreditado con **dos fuentes con fecha en la
  ruta**. **No pertenecen a ninguna ventana reciente de ARGOS y no cambian ningún total.**
  **Se cierra definitivamente y no vuelve a listarse.**

⚠️ **Lección de método que hay que registrar, porque invierte una presunción**: la edición anterior
**desconfió del resumidor** cuando situó ese boletín en «octubre de 2025», y lo dejó fuera por
prudencia. **El resumidor tenía razón.** La prudencia produjo el resultado correcto —no integrar sin
ancla— **por el motivo equivocado**. **La regla se sostiene** (una fecha sin fragmento citable no
fija nada), **pero el corolario debe anotarse: que el resumidor no sea fiable no significa que se
equivoque siempre, y una fecha suya sigue mereciendo una búsqueda de arbitraje antes de descartarla
como disparate.**

### Eje 4 · **CHIHUAHUA — `ARG-111-004`, el dato que mueve el color**: `SIN AVANCE`

No se publicó confirmación ni desmentido de que el ocupante del domicilio de la calle Altos de la
Parra sea personal de seguridad. **El hecho se mantiene 🟡 en su edición de origen y no se
recalifica.** La reserva de ubicación («Cerro Coronel» / «colonia Lealtad») **sigue sin fundirse**.

### Eje 5 · **CHIAPAS — Cintalapa (`ARG-110-003`)**: ✅ **DISCREPANCIA RESUELTA**

Tres fuentes adicionales (Diario de Comitán, El Universal ×2) describen el mismo hecho y **confirman
9 cargadores, no 10**, y **aclaran que José «N», «El Feyo», es el único detenido del hecho, no una
segunda detención**. Aseguramiento: 2 fusiles AK-47 (7.62×39), 2 chalecos tácticos, 9 cargadores;
saldo de 1 muerto y 1 detenido.
**Se retira la marca `DISCREPANCIA NUMÉRICA — NO INTEGRAR HASTA VALIDACIÓN`.** Ver fe de erratas
`ARG-112-FE-001`.
⚠️ **Reserva**: las tres fuentes tienen redacción próxima entre sí — **posible corroboración débil por
construcción**. Se acepta la corrección porque **va contra la cifra que ARGOS publicó**, no a favor.

### Eje 6 · **OAXACA — Loxicha (`ARG-109-002`)**: sigue sin cerrar, con avance parcial

Localizado el artículo exacto: tres víctimas —Donaldo M. R. (49, mototaxista), su esposa Zaragoza
H. M. (46) y Martín S. R. (28)— en Santa Catarina Loxicha. **El perfil de víctimas no incluye a la
niña de 4 años** de `ARG-109-002`, lo que **apunta a caso distinto, no a doble encabezado del mismo
hecho**. **Pero el *slug* no lleva fecha y el resumidor la sitúa en «15 de junio» sin respaldo en la
ruta ni en el titular**: la fecha **se descarta como no fijada**.
Se mantiene `POSIBLE CASO HOMÓNIMO — NO INTEGRAR HASTA VALIDACIÓN`, **con la precisión ganada**.

### Eje 7 · **GUERRERO — Petatlán y Totolapan (`ARG-111-REC-001`, `ARG-110-REC-001`)**: `SIN DATO` en las tres preguntas, con un hallazgo cualitativo

- **(a) Tiempo de respuesta**: **ninguna fuente publica una cifra**. Lo que sí consta es la
  **declaración de los propios pobladores de que la fuerza pública no llegó en ningún momento** del
  enfrentamiento —de la tarde del miércoles 26 a la madrugada del jueves 27— y su **acusación
  expresa de omisión** a autoridades de los tres niveles. **Es dato cualitativo, no cifra**, y así se
  registra: **no se convierte en un tiempo de respuesta inferido.**
- **(b) Identidad y plaza de origen de los cuatro abatidos**: `SIN DATO`. Las fuentes se refieren
  genéricamente a «sicarios de La Familia Michoacana». **No permite determinar desplazamiento desde
  Tierra Caliente frente a reclutamiento local**, que era la pregunta.
- **(c) Situación jurídica de las armas empleadas por los pobladores**: `SIN DATO`. Ninguna fuente
  reporta investigación ni proceso contra ellos.

**Se cierran los tres en `SIN AVANCE`, que es el resultado correcto cuando no hay dato.**

### Eje 8 · **MICHOACÁN — Pedernales (`ARG-110-004`)**: `SIN AVANCE`, reserva sostenida

**El boletín de la FGE de Michoacán sigue sin aparecer.** Los siete portales regionales que sostienen
«3 muertos» **comparten redacción casi idéntica**: son republicadores de una nota base,
**corroboración débil por construcción, no siete fuentes**. **No se recalifica el semáforo de la
edición de origen.**

### Eje 9 · **VERACRUZ — Poza Rica (`ARG-108-005`)**: `SIN AVANCE`

El cotejo balístico cruzado de las tres carpetas **sigue sin constar realizado**.

### Ejes cerrados sin gasto, conforme a la instrucción

**Ninguna búsqueda** en: la disputa forestal Michoacán/Guerrero (**es una solicitud a SEMARNAT y al
RAN, no una búsqueda**), «El Dron» (`ARG-109-004`, la pregunta principal la contesta un oficio),
Piedras Negras (retirado por umbral), Querétaro `ARG-109-005` y Tepechitlán (vacíos acreditados).

---

## 7. Fes de erratas — **NO PUBLICADAS EN EL CARTELÓN**

Conforme a la instrucción editorial vigente: se asignan y se registran en `indice-arg-id.md`, y
**no abren página, sección ni ficha en el producto**.

### `ARG-112-FE-001` — `ARG-110-003` (Cintalapa, Chiapas): **9 cargadores, no 10**, y una sola detención
Tres fuentes adicionales confirman **9 cargadores útiles** donde ARGOS 110 fichó **10**, y aclaran que
**José «N», «El Feyo», es el único detenido del hecho**, no una segunda detención independiente.
**Se corrige el renglón y se retira la marca de discrepancia.** Efecto sobre el total de ARGOS 110:
**−1 cargador**. Sin efecto sobre detenidos, que no se habían duplicado en el conteo.

### `ARG-112-FE-002` — Zacatecas, municipio de Tabasco: el candidato **no era de ninguna ventana de ARGOS**
Los **11 detenidos y 10 armas largas** publicados por `zacatecas.gob.mx` sin fecha en la ruta, que
ARGOS 111 dejó como `SIN ANCLA FECHADA — NO INTEGRAR AL TOTAL` y señaló como «el candidato de mayor
volumen del corte», **son del 15-16 de octubre de 2025**, acreditado con dos URLs con fecha en la
ruta. **No modifican ningún total de ARGOS 111** —nunca se integraron— **y el candidato se cierra
definitivamente.** **La decisión de no integrarlo fue correcta; la hipótesis de que pertenecía al
corte era falsa.**

### `ARG-112-FE-003` — `ARG-111-SEN-C01` (FGE Veracruz): se **cierra como vacío acreditado del emisor**
Tras **cinco cortes consecutivos** de agregados sin individualización ni fecha en la ruta, el
candidato **deja de arrastrarse**. No se retira ninguna cifra —nunca se integró ninguna— y **se
registra la vía sustituta: la delegación de la FGR en Veracruz sí individualiza**, y de ahí salió
`ARG-112-SEN-001`.

### `ARG-112-FE-004` — Deuda de dominio de **Tlaxcala**: se cierra como **vacío acreditado**
Tras arrastrarse varias ediciones sin arbitrar, **queda establecido que ninguno de los dos dominios
publica boletines individuales fechados** —solo acumulados de periodo—. **La pregunta tenía respuesta
negativa y se declara como tal**, en vez de seguir figurando como ambigüedad pendiente.

---
## 8. Fichas del corte

Siete eventos en cinco entidades. **Semáforo: 🔴 2 · 🟡 0 · 🟢 5.**

### `ARG-112-001` — Ojocaliente, Zacatecas · Comandancia de la Policía Municipal · 🔴
**30-ago, ~20:00.** AEI colocado en un vehículo particular y detonado frente a la comandancia,
durante la Feria Regional 2026. **7 lesionados (6 civiles + 1 policía municipal)**; 11 vehículos
particulares y 2 patrullas dañados, más instalaciones, viviendas y comercios. Suspensión de clases en
todos los niveles de la cabecera, cancelación de la coronación de la Reina de la Feria y cierre al
público de la Presidencia Municipal. **Sin detenidos.**
**Rojo por**: ataque contra autoridades (lo inicia el grupo criminal) + empleo de explosivos +
víctimas civiles + terror contra población en espacio público. **Cuatro criterios concurrentes.**
✅ **Línea de autoría publicada, y es el hallazgo más accionable del hecho**: la Fiscalía informó el
31-ago que **rastreó por número de serie el vehículo portador**, que tenía **reporte de robo con
violencia en Jalisco desde abril de 2026**, y **atribuyó el ataque de forma hipotética al CJNG**,
apoyándose además en la declaración del detenido de Villa García. **La atribución es hipótesis de la
autoridad y así se consigna.** **La trazabilidad registral del vehículo funcionó — que es justo lo
que no se está haciendo con los artefactos.**
**Rectificación oficial registrada**: el secretario general de Gobierno, Rodrigo Reyes Mugüerza,
informó primero que el artefacto habría sido **arrojado desde un vehículo en movimiento** y después
precisó que, según el reporte de la SSP, **fue colocado en un automóvil particular y detonado**.
**Se publica la versión rectificada y se deja constancia de la primera.**
⚠️ `CIFRA DE LESIONADOS ACTUALIZADA POR LA AUTORIDAD — NO SE ARBITRA`: **el borrador llegó a
tratar el «10» como cifra aislada y lo descartaba. Era incorrecto y lo detectó `procedencia-cifras`.**
La cifra de **7 (6 civiles + 1 policía)** es del **parte de la noche del hecho**, de la Secretaría
General de Gobierno; la de **10 (8 civiles + 2 policías municipales, 2 de gravedad, sin fallecidos)**
es una **actualización del 31-ago del fiscal general Cristian Paul Camacho**. **Las dos son
institucionales y la diferencia es de momento, no de fuente.** **Se publican ambas con emisor y
fecha, y no se arbitra** sin lectura directa del boletín, imposible con el egreso bloqueado.
⚠️ **Es el mismo criterio que el borrador ya aplicaba bien al mecanismo del artefacto y que no había
aplicado al saldo**: una inconsistencia interna de trato entre dos rectificaciones del mismo hecho.
Fuentes: Secretaría General de Gobierno de Zacatecas · SSP Zacatecas · Gabinete de Seguridad (las
tres **por cita**) · El Financiero · Excélsior · Aristegui Noticias · Infobae · El Imparcial · El
Siglo de Torreón · Potosinoticias · Periódico Mirador · Proyecto Puente. **★★★★☆**

### `ARG-112-002` — Villa García, Zacatecas · límite con Aguascalientes · 🔴 · **FRONTERA DE VENTANA**
**29-ago, hora no fijada.** Motocicleta colocada al costado del camino con explosivos y **detonada de
forma remota**; la onda alcanzó **una patrulla** y **el vehículo particular de una civil**.
**Lesionados de gravedad: un policía estatal preventivo y una maestra**, identificada como Alma
Patricia, originaria de Villa García, que conducía un Mazda rojo y fue trasladada a un hospital de la
capital. **La FGJEZ coordina con la Fiscalía de Aguascalientes** para fijar el punto exacto de origen.
**Rojo por**: ataque contra autoridades + explosivos + víctima civil.
⚠️ **Es el único de los tres ataques de la serie con sistema de iniciación y contenedor publicados**,
y por eso es el de mayor valor de explotación técnica del corte.
`FRONTERA DE VENTANA — HORA NO FIJADA`: publicación el **29-ago**, día en que ARGOS 111 cerró a las
09:05, sin hora citable. **Se integra a la edición que lo ve primero.** Marca permanente.
`RESERVA DE NATURALEZA`: parte de las coberturas titula «ataque armado» y parte «ataque con
explosivos»; el cuerpo describe consistentemente un artefacto detonado a distancia. **No se funden ni
se infiere uso de arma de fuego no publicado.**
Fuentes: FGJ Zacatecas (por cita) · Infobae · El Imparcial · La Prensa · SDP Noticias · El Diario del
Noroeste (**fecha en la ruta**) · Turquesa News. **★★★★☆**

### `ARG-112-003` — Detención del probable responsable de Villa García · 🟢
**29-ago**, horas después del ataque. **Un hombre de entre 22 y 23 años, originario de
Aguascalientes**, detenido como probable responsable. **Sin identidad, corporación aprehensora,
lugar de captura ni situación jurídica publicados.**
⚠️ **Ficha separada por regla expresa de `CLAUDE.md`**: el delito (`ARG-112-002`) y su respuesta
institucional caen **ambos dentro de la ventana**, así que **se abren dos fichas con dos ARG-ID**.
**Las lesiones graves de dos personas no se contabilizan en verde** por haberse capturado a un
probable responsable. Es la regla nacida del fallo de `ARG-101-008` y **esta es la primera edición
desde entonces en que vuelve a aplicarse en su supuesto exacto.**
`Pendiente de corroboración institucional.` Fuentes: El Imparcial · Infobae · El Diario de Chihuahua
(**fecha en la ruta**). **★★★☆☆**

### `ARG-112-004` — Sabinas Hidalgo, Nuevo León · 🟢 · **FRONTERA DE VENTANA**
**31-ago, hora no fijada.** Sobre la carretera Nuevo Laredo–Monterrey, la **Agencia de Investigación
Criminal de la FGR** con SEDENA, SEMAR, SSPC y Guardia Nacional ubicó **dos vehículos acoplados a
semirremolques procedentes de Texas**, con armamento en **compartimentos ocultos**.
**210 armas: 195 largas y 15 cortas**, más cargadores. **3 detenidos.** Informado por el titular de
la SSPC.
**Cartuchos no integrados**: la única mención es «más de 200 armas y cartuchos», **sin desglose**;
«más de» no es cifra.
`FRONTERA DE VENTANA — HORA NO FIJADA`: publicación el **31-ago**, día de cierre, sin hora citable.
Fuentes: Gabinete de Seguridad / SSPC (por cita) · Excélsior · El Financiero (**fecha en la ruta**) ·
Infobae (**fecha en la ruta**) · Aristegui Noticias · 24 Horas · SDP Noticias. **★★★★☆**

### `ARG-112-005` — Sur de Sinaloa · Agua Verde y Palo Blanco · 🟢
**29-ago.** Cuatro intervenciones de SEMAR, Ejército, Guardia Nacional, FGR y SSPC.
**Agregado oficial de las cuatro**: 8 detenidos, 33 armas largas, 6 explosivos, 11 vehículos.
**Agua Verde**: 29 armas largas, 68 cargadores, 50 cartuchos, 1 granada, 2 vehículos, chalecos y
cascos **sin cifra**, 2 contadoras de dinero, 19 bolsas de polvo similar a cocaína y 4 de mariguana
**sin peso**.
**Palo Blanco**: campamento; 2 armas largas, 9 cargadores, 1,000 cartuchos, 5 vehículos y **6 AEI
destruidos en el lugar por riesgo de traslado**.
⚠️ `CIFRA PARCIAL POR RUBRO — DECLARADA`: **largas y detenidos se toman del agregado oficial**
(33 y 8); **cargadores, cartuchos y granada solo de las dos intervenciones desglosadas** (77 · 1,050 ·
1), porque **las otras dos no se publicaron con detalle**. **Son suelos, no totales, y así se declara
en el cartelón.** Esta es la contramedida directa contra el modo de fallo de **suma incompleta** que
la edición anterior estrenó.
**Deslinde expreso**: **no es** `ARG-111-002` (Escuinapa, 28-ago) **ni** `ARG-111-003` (Concordia,
28-ago) — localidades, fechas, cifras y perfil de armamento distintos.
Fuentes: Gabinete de Seguridad (por cita) · Infobae (**fecha en la ruta**) · El Financiero (**fecha en
la ruta**) · López-Dóriga Digital. **★★★★☆**

### `ARG-112-006` — Acapulco de Juárez, Guerrero · 🟢
**30-ago.** La FGE de Guerrero con fuerzas federales detuvo **en flagrancia**, en patrullajes
preventivos, a **Zeus «N» y Aldo «N»**, presuntos integrantes del grupo «GNG». **1 arma corta cal.
.380**, **2 cargadores metálicos** y munición **de cuatro calibres**: 10 de .380, **37 de 7.62×39**,
7 de 9 mm y 2 de .223. Además 46 dosis de hierba verde (no es armamento).
⚠️ **Tres de los cuatro calibres no tienen arma correspondiente en el aseguramiento**, incluido el
**7.62×39, calibre de fusil**: es el dato de explotación del hecho.
**Los calibres se conservan separados**; el total de **56 cartuchos** de la tabla es **cálculo propio
de ARGOS**.
**Fuente nacional única, sin boletín institucional indexado** —la consulta dirigida a
`fiscaliaguerrero.gob.mx` no devuelve nada posterior a mediados de agosto—. Se integra al conteo de
armamento con nivel **Bajo**, conforme al **umbral asimétrico** que lo admite en armamento y no en
sentencias. Fuente: Infobae (**fecha en la ruta**). **★★☆☆☆**

### `ARG-112-SEN-001` — FGR / FECOR · Papantla, Veracruz · 🟢 · **FRONTERA DE VENTANA**
**Publicada el 29-ago.** **Sentencia condenatoria** contra **Pedro «N»** por **portación de arma de
fuego de uso exclusivo de las Fuerzas Armadas**. **Cuatro años de prisión** y **multa de 80 UMAS
($9,384)**. **Firmeza no informada** — ARGOS no la presume. **Sin causa penal ni tribunal
identificados**, que son los campos que harían seguible la condena en apelación.
**Término condenatorio expreso en la fuente**, requisito de integración.
**Los 20 cartuchos del hecho juzgado NO se integran al conteo de armamento**: son de una detención
anterior, no un aseguramiento de la ventana.
Fuente oficial: **FGR / FECOR**, por republicador **con fecha en la ruta**. Corroboración: **un
segundo republicador del mismo boletín — débil por construcción, no fuente independiente**.
Nivel **Medio**, que **sí alcanza el umbral** del módulo. `FRONTERA DE VENTANA — HORA NO FIJADA`.

### Línea inferior — **Maguarichi, Chihuahua**, 28-ago (fuera de ventana, publicado durante el corte)
Ejército y Guardia Nacional en patrullaje por las barrancas de Maguarichi localizaron **tres
camionetas abandonadas con reporte de robo —dos en Estados Unidos (Arizona y Texas) y una en
Chihuahua, México—**, cargadas con explosivos:
**6,324 piezas de explosivo de alto poder**, **1.1 toneladas de agente explosivo a granel**,
**1,710 metros de material de iniciación y detonación** y **5,234 detonadores eléctricos**.
**Sin personas en el sitio.** Puestas a disposición del MP en San Juanito; material destruido por
personal especializado de la **42/a Zona Militar**.
**Es el mayor volumen de material explosivo de toda la serie** y **no se suma a ningún total del
corte**: el hecho es del 28-ago, anterior a la apertura de la ventana.
⚠️ **Corrección de resumidor registrada por el barrido**: una primera consulta devolvió un resumen
que **fusionaba este hallazgo con las cifras de armas de Sinaloa** bajo un encabezado falso. **Se
descartó esa versión conflada y se usó la fuente específica de Maguarichi.**
Fuentes: La Jornada (**fecha en la ruta**) · El Diario de Chihuahua (**fecha en la ruta**) ·
Excélsior · Notisistema.

---
## 9. Candidatos que NO se integran

| Candidato | Cifras que aportaba | Motivo |
|---|---|---|
| **Guanajuato** · San Miguel de Allende, Victoria y Dolores Hidalgo | 7 detenidos · 13 armas (4 largas, 9 cortas) · 529 cartuchos · 37 cargadores | `FECHA DEL HECHO EN DISPUTA`. Única URL con fecha en la ruta: **29-ago**; otra fuente lo sitúa el **25-ago** con **cifras idénticas** — más consistente con **republicación tardía** que con evento nuevo. **Las cifras no están en duda; la fecha sí** |
| **Veracruz** · Martínez de la Torre, Coatzacoalcos y San Andrés Tuxtla — «14 detenidos» | 14 detenidos agrupados; armamento **sin cifra** | `POSIBLE DUPLICIDAD`. **Los 6 de San Andrés Tuxtla son `ARG-108-004`, reapareciendo por TERCERA vez**; Coatzacoalcos ya figuró en el boletín federal del 27-ago. La nota **agrupa** los 8 restantes y **ARGOS no infiere el reparto** |
| **Nayarit** · Acaponeta y Huajicori | 7 detenidos · 6 largas · 62 cargadores · 600 cartuchos · 3 chalecos · **15 AEI** | `FECHA NO FIJADA`. Ningún resultado con fecha en la ruta. **No se afirma ni se descarta** su pertenencia a la ventana |
| **Chihuahua** · Bocoyna | sin desglose obtenido | `NO REVISADO A FONDO`. Publicación del **31-ago**, municipio colindante con Maguarichi. **No se descarta por fecha sino por falta de verificación.** **Candidato prioritario de la edición siguiente** |
| **Oaxaca** · ASAEO, «14 cateos / 9 detenidos» vs «21 cateos / 10 detenidos» | — | `POSIBLE DUPLICIDAD` **y además fuera de ventana** (27-28 ago). No es integrable en ningún caso |
| **Coahuila** · sentencia de Allende | 2 sentenciados · 4a2m y 4a | `FUERA DE VENTANA`. Término expreso, pero **sin URL fechada**; la evidencia apunta al 28-ago |
| **Tamaulipas** · sentencia de Reynosa | 2 sentenciados · 50 años c/u · multa $337,960 | `FUERA DE VENTANA` (~24-ago) |
| **Baja California Sur** · Los Cabos | armas, vehículos, detenidos | `TRAMPA DE FECHA DETECTADA`. Los titulares parecían recientes; **el hecho es de mayo-junio de 2026**. Descartado por el propio control de fecha del barrido |
| **Estado de México** · «aseguran armas, 10 detenidos» en `gabinetedeseguridad.gob.mx/contenido/6985` | 10 detenidos | ⚠️ `TRAMPA DE AÑO`. El boletín es del **21-oct-2025**. **Lo devolvió una consulta de agosto de 2026 sin marcar el año**: es exactamente el modo de fallo contra el que existe el control de mes/año |
| **Michoacán** · Ecuandureo, adolescente con 2 ametralladoras | — | `NO ES SENTENCIA`. **Vinculación a proceso** dictada el 30-ago, **dentro de la ventana**, pero una vinculación **nunca** se cuenta como condena. El aseguramiento subyacente es del 19-ago |
| **Nacional** · boletín diario del Gabinete, 29-31 ago | — | `SIN RESULTADO INDEXADO EN VENTANA`, **tras las tres formas de consulta**. Ver §4 |

---

## 10. Módulo de armamento — totales

**Todos los totales son cálculo propio de ARGOS**, derivados de cifras expresamente publicadas.

### Línea A — asegurado en hechos DE LA VENTANA (3 eventos, 3 entidades)

| Categoría | Total | Nota |
|---|---|---|
| Armas cortas | **16** | 15 Sabinas Hidalgo + 1 Acapulco |
| **Armas largas** | **228** | **195 Sabinas Hidalgo** + 33 sur de Sinaloa. **El 86 % en un solo evento** |
| Cartuchos | **1,106** | 1,050 sur de Sinaloa (**suelo: 2 de 4 intervenciones**) + 56 Acapulco (**suma propia de 4 calibres**). **Sabinas Hidalgo no aporta**: «más de 200 armas y cartuchos» no es cifra |
| Cargadores | **172** | 93 Sabinas Hidalgo (**fuente única**) + 77 sur de Sinaloa (**suelo**) + 2 Acapulco |
| Granadas | **1** | Agua Verde. La única del corte |
| **AEI** | **6** | Palo Blanco, **destruidos in situ por riesgo de traslado**, ninguno peritado públicamente |
| Explosivos y componentes | **0** | Los 6 AEI se destruyeron sin publicar componentes recuperados |
| Armamento especial | **0** | Ningún .50, lanzagranadas, dron armado ni blindado artesanal — **pese a 228 armas largas** |
| **Placas balísticas** | **0** | ⚠️ **Cero, tras 25 en tres semanas.** Ver eje 1 |
| Chalecos tácticos | **0 con cifra** | Agua Verde reporta «chalecos y cascos» **sin cantidad**: evento cualitativo |
| **Personas detenidas** | **13** | 3 Sabinas Hidalgo + 8 sur de Sinaloa + 2 Acapulco |
| Entidades con aseguramiento | **3** | Nuevo León · Sinaloa · Guerrero |
| Eventos contabilizados | **3** | Eventos cualitativos sin cantidad: **1** (chalecos y cascos de Agua Verde) |

### Línea B — publicado durante el corte, hecho ANTERIOR a la ventana

**Un solo hecho: Maguarichi, Chihuahua (28-ago).** **Fuera del total de la ventana.**

| Categoría | Cifra |
|---|---|
| Explosivo de alto poder | **6,324 piezas** |
| Agente explosivo a granel | **1.1 toneladas** |
| Material de iniciación y detonación | **1,710 metros** |
| Detonadores eléctricos | **5,234** |
| Vehículos | 3 camionetas con reporte de robo: **2 en EE. UU. (Arizona y Texas) y 1 en Chihuahua, México** |
| Detenidos | **0** — sin personas en el sitio |

⚠️ **Los AEI empleados en Ojocaliente y Villa García NO figuran en ningún conteo**: fueron **usados
contra la autoridad, no asegurados**. Un artefacto detonado no es un aseguramiento; entra en el
semáforo, no en el módulo. **Misma regla aplicada a los seis de Zacatecas en la edición anterior.**

### Lectura regional

| Región | Eventos | Largas | Cargadores | AEI | Detenidos |
|---|---|---|---|---|---|
| Noreste | 1 (Nuevo León) | **195** | 93 | 0 | 3 |
| Noroeste | 1 (Sinaloa) | 33 | 77 | **6** | 8 |
| Sureste | 1 (Guerrero) | 0 | 2 | 0 | 2 |
| Occidente · Centro · Golfo · Pacífico Sur | **0** | 0 | 0 | 0 | 0 |

⚠️ **Advertencia de lectura, publicada también en el cartelón**: el 86 % de las armas largas está en
Nuevo León **porque allí se interceptó un envío en tránsito**, no porque la entidad concentre
armamento. **El armamento no era de Nuevo León, iba por Nuevo León.**

---

## 11. Módulo de sentencias — indicador de cobertura

| Indicador | Resultado |
|---|---|
| Fiscalías estatales revisadas | **32 de 32** — cuarta edición consecutiva |
| FGR revisada | **Sí**, incluidas delegaciones estatales |
| Fiscalías con sentencia publicada **en ventana** | **0** de 32 |
| Sentencias integradas al conteo nacional | **1**, y es **federal** |
| Personas sentenciadas · años acumulados · multas | **1** · **4 años** · **$9,384** |
| Reparación del daño ordenada | **0** — congruente con el tipo penal (portación, sin víctima individualizada) |
| Sentencias firmes | **0** — firmeza **no informada**, nunca presumida |
| `SIN RESULTADO INDEXADO EN VENTANA` | **32** |
| `SIN ACTUALIZACIÓN CONSTATADA` | **0** — casilla no utilizable con egreso bloqueado |
| `NO REVISADA` | **0** |
| Páginas con error de acceso | **32 + federales** — `CONNECT tunnel failed, 403` |

⚠️ **Causa de calendario, declarada**: la ventana cubre **sábado, domingo y la mañana del lunes** —
**una sola mañana hábil**. Las fiscalías publican en días hábiles. **Buena parte del cero de las 32
es de calendario, no de capacidad institucional**, y así se dice en el cartelón. Se localizaron
muchas sentencias, **todas anteriores al 29-ago**: Querétaro publicó siete en agosto y Durango ocho,
ninguna dentro del corte.

---
## 12. Controles editoriales

**Los tres se ejecutaron. Los dos primeros con subagente, autorizado por el destinatario.**

| Control | Veredicto | Rendimiento |
|---|---|---|
| `barrido-regional` ×6 | — | **32 de 32 entidades.** Ciclo B aplicado y declarado |
| `editor-duplicidad` | **`CORREGIR ANTES DE PUBLICAR`** | **Ninguna duplicidad real**: los cinco riesgos señalados estaban bien resueltos. **Pero encontró un riesgo que nadie había visto** y dos fisuras de trazabilidad |
| `procedencia-cifras` | **`CORREGIR ANTES DE PUBLICAR`** | **Cuatro correcciones**, una de ellas **grave y de criterio**, más dos reservas que **refuerzan** una ficha |

**Séptima edición consecutiva con hallazgos reales de los dos controles.**

### Hallazgos de `editor-duplicidad` — y qué se hizo

1. ⚠️ **Colisión de topónimo que ni el barrido ni el coordinador habían visto.** «Agua Verde» y
   «Palo Blanco» **ya figuran en el archivo** como localidades del mismo corredor del sur de
   Sinaloa: **Agua Verde en El Rosario** (`ARG-102-REC-001`, 14-16 ago, 303 artefactos) y **Palo
   Blanco en Mazatlán**, como La Noria-Palo Blanco (`ARG-106-004`, 23-ago). **No son este hecho** —
   composición y fechas distintas—, **pero la autoridad no publicó el municipio de las localidades
   del 29-ago**, así que el cotejo no puede cerrarse.
   **Aplicado**: se añadió a la ficha una `RESERVA DE TOPÓNIMO` explícita, con los dos precedentes
   nombrados y la condición que la cerraría (que se publique el municipio). **Es el tipo de hallazgo
   que solo produce el cruce contra el archivo**, no la búsqueda.
2. ⚠️ **Repetición casi literal entre la nota del semáforo (portada) y la Valoración (p. 6)** sobre
   la progresión del blanco en Zacatecas — la regla de no duplicación alcanza también a dos bloques
   narrativos de la misma edición.
   **Aplicado**: la Valoración se recortó y ahora **remite** a la portada para la descripción, y se
   limita a lo que le toca — **por qué esa progresión, en la metodología, es un incremento del riesgo
   estratégico y no un simple aumento de intensidad**.
3. **Casillas de cobertura del módulo de armamento que sumaban 30 de 32.**
   **Aplicado**: cuadradas a 32 (3 publicaron + 28 sin resultado indexado + 1 portal no disponible),
   con el cuadre hecho explícito. **Una casilla que no cuadra con el universo es una cobertura no
   demostrable.**
4. Verificó además, sin que estuviera en el encargo, que `ARG-112-SEN-001` no colisiona con
   `ARG-90-SEN-005` (Papantla, feminicidio): **mismo municipio, distinto emisor, delito y pena**.

### Hallazgos de `procedencia-cifras` — y qué se hizo

1. ⚠️ **LA CORRECCIÓN MÁS IMPORTANTE DEL CORTE, y es de criterio, no de dato.** El borrador
   descartaba la cifra de **10 heridos** de Ojocaliente **por «aislada»**. **No lo era**: es la
   **actualización institucional del 31-ago del fiscal general Cristian Paul Camacho** —10 heridos,
   8 civiles y 2 policías, 2 de gravedad, sin fallecidos— frente al parte de la noche del hecho de
   la Secretaría General de Gobierno (7).
   ⚠️ **El fallo es de coherencia interna**: la misma ficha **ya aplicaba correctamente el criterio
   de «se conserva la versión rectificada»** al mecanismo del artefacto, y **no lo aplicó al saldo**.
   **Aplicado**: se publican **ambas cifras con emisor y fecha**, marcadas como
   `CIFRA ACTUALIZADA POR LA AUTORIDAD — NO SE ARBITRA`, y el hecho se lee como **«entre 7 y 10, con
   10 como cifra vigente de la Fiscalía»**. Corregido también en portada, valoración y arreglo de
   datos.
   **Regla que conviene fijar**: *cuando una edición acepte una rectificación de la autoridad en un
   campo de un hecho, debe revisar si hay rectificaciones posteriores en los demás campos del mismo
   hecho.* Una autoridad que corrige el mecanismo suele corregir también el saldo.
2. ⚠️ **Omisión asociada**: el mismo boletín del fiscal publica **línea de autoría** —vehículo
   portador rastreado por número de serie, con **reporte de robo con violencia en Jalisco desde
   abril de 2026**, y **atribución hipotética al CJNG**—, mientras el apartado «qué vacíos existen»
   afirmaba que **no había** línea de autoría. **Aplicado**: se incorporó como hallazgo, marcando la
   atribución como **hipótesis de la autoridad, no acreditada**, y se usó en la conclusión 4 como
   prueba de que **la vía registral sí funciona cuando se emplea**.
3. ⚠️ **Error de hecho en tres lugares del cartelón, uno de ellos una conclusión de inteligencia**:
   las tres camionetas de Maguarichi **no** tienen todas reporte de robo en Estados Unidos. Son
   **dos en EE. UU. (Arizona y Texas) y una en Chihuahua, México**. **Aplicado** en la tabla de línea
   inferior, en la conclusión 4 y en este archivo. **La conclusión se sostiene y gana precisión**:
   el origen del material **cruza dos jurisdicciones, no una**.
4. ⚠️ **«El último boletín federal indexado es el del 26 de agosto» era inexacto**: es el del **27**,
   alcanzable por republicadores. **Aplicado.** El error era menor en la cifra y grande en el método:
   **decir 26 habría borrado la corrección que la edición anterior costó una fe de erratas.**
5. ⚠️ **Edad del detenido de Villa García contradicha**: la mayoría de coberturas dice **22-23 años**;
   otra, referida al mismo hecho, dice **18**. **Aplicado**: se retiró la edad como cifra cerrada y
   se declaró la reserva.
6. ✅ **Dos reservas que REFUERZAN la ficha de Villa García**, no la debilitan:
   - **El dato de mayor valor del corte —motocicleta portadora y detonación remota— procede de una
     declaración institucional nominada**: el **secretario de Seguridad Pública de Aguascalientes,
     Antonio Martínez Romo**, que el borrador no acreditaba. **Aplicado**: añadido como fuente
     institucional. **Son dos instituciones de dos entidades distintas**, lo que mejora la
     corroboración.
   - `RESERVA DE SECUENCIA`: una síntesis regional describe al detenido como «el hombre que manejaba
     la moto», secuencia distinta de la dominante. **El peso de la evidencia favorece la versión
     publicada**, pero **la reserva se declara y no se resuelve**.
7. ✅ **Verificación aritmética completa sin descuadres**, y **confirmó que la hora de Ojocaliente
   (~20:00) sí tiene fragmento citable** — no procedía retirarla, pese a la advertencia preventiva
   del encargo. **También confirmó el uso correcto de las cifras heredadas** (25 placas, 49 y 172
   artefactos, 5 fulminantes de Jiménez del Teul): usadas como contexto declarado, **nunca sumadas a
   los totales del corte**.

⚠️ **Lección de la edición sobre cómo usar los controles**: la instrucción de arranque advertía que
**un control que dice «no integrar» merece una búsqueda de arbitraje antes de obedecerlo**. Esta
edición encontró **el caso simétrico**: **un control puede obligar a integrar lo que el borrador
había descartado.** Las dos advertencias son la misma regla — **ni obedecer ni descartar por
precaución: arbitrar**.

---

## 13. Construcción y validación

```
node --check sobre el bloque de datos extraído  → OK
validación de coherencia                        → validación OK
  · cada estado: existe en MEXICO_PATHS         → 10/10
  · cada region: coincide con STATE_REGION      → 10/10
  · ninguna fecha fuera de la ventana           → 10/10
  · ARG-ID duplicados                           → ninguno
  · semáforo derivado de EVENTOS                → 🔴 2 · 🟡 0 · 🟢 5, idéntico a los contadores de portada
python3 tools/gen-movil.py 112 2026-08-31 111 2026-08-29 09:28
  → contadores del generador: 🔴 2 🟡 0 🟢 5 · tarjetas móvil 7 / escritorio 7 · validación OK
```

⚠️ **Defecto propio detectado por la validación y corregido antes de publicar**: al sustituir el
bloque de datos, el ensamblado **dejó fuera `REGION_ORDER`, `STATE_REGION`, `SEVERITY_*` y `GRIS`**,
que viven entre `EVENTOS_ARM` y `SIZE_R`. **El cartelón habría cargado con el radar y el mapa rotos.**
Lo detectó el `node --check` con el recuento de coherencia, **no la vista**. **Es la razón por la que
esa comprobación existe y hay que seguir ejecutándola.**

**Comprobaciones estructurales**: una sola etiqueta `<body>` · 6 secciones · 7 tablas, **todas
envueltas exactamente una vez** en `table-wrap`, ninguna suelta · 7 fichas con `id` de ARG-ID real ·
`cero -FE-` en escritorio y móvil · ningún `sem-item` fuera de la portada · pie con número, fecha y
hora en las seis páginas · `argos-map-arm` restituido (hay aseguramientos).
**Móvil**: 6 secciones · 13 `tabla-scroll` · 3 `<table>` · **cero restos de clases de escritorio** ·
**cero `table-wrap`** (el generador los renombra: no es un defecto) · sin `<script>`.

---

## 14. Qué queda abierto

Ver `reports/_pendientes.md`, actualizado como último paso. Los tres seguimientos de mayor prioridad
para la edición siguiente:

1. ⚠️ **La serie de artefactos explosivos de Zacatecas** — tres ataques en seis días con progresión de
   blanco acreditada. **Peritaje comparado de los tres artefactos** y **carpeta única**.
2. ⚠️ **Chihuahua · Bocoyna**, publicado el 31-ago, `NO REVISADO A FONDO`, colindante con Maguarichi.
   **Puede ser continuación del mismo hallazgo.**
3. ⚠️ **`gabinetedeseguridad.gob.mx/resultados/` ya es exigible** desde el 1 de septiembre: **su
   ausencia se declara como vacío, no como limitación heredada.**
