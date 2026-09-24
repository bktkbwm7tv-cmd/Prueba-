# ARGOS 114 — Archivo de fuentes, cobertura y método

**Corte**: 2026-09-02 · **Ventana**: **1-sep 13:17 → 2-sep 10:17 CDMX** (**21 h 00 min**), abre exactamente
donde cerró ARGOS 113. Hora verificada con `TZ=America/Mexico_City date` al arranque de la sesión.

**Techo de confianza del producto: ★★★★☆.** Ver «Bloqueo de egreso».

---

## Bloqueo de egreso — vigesimosexta edición, verificado EN ESTA SESIÓN

No se heredó: se comprobó. `curl` contra `https://www.gob.mx/sspc` y contra
`https://gabinetedeseguridad.gob.mx/resultados/` devuelve **`curl: (56) CONNECT tunnel failed, response 403`**
—denegación por política de red en el proxy de salida, no fallo del portal—. `WebFetch` devuelve
`EGRESS_BLOCKED`.

**Consecuencias aplicadas**: cero portales leídos por acceso directo · toda cita institucional es por
**título indexado o republicador**, y **cada sustitución queda anotada en la ficha que la usa** ·
`SIN ACTUALIZACIÓN CONSTATADA` **figura en cero** en los dos indicadores de cobertura, por no ser
utilizable sin lectura directa · techo ★★★★☆ para todo el producto.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.

---

## Ciclo de rotación — **CICLO A: Noroeste + Centro** encabezando el triaje judicial

**Declarado, aplicado y con resultado.** Las otras cuatro regiones encabezaron con armamento.
Se aplicó además la instrucción de **dirigir el triaje judicial a las delegaciones de la FGR antes que a
las fiscalías estatales**.

**Qué aportó la rotación que el orden anterior no habría aportado:**

- **Noroeste**, encabezando judicial y apuntando a la FGR, localizó **tres candidatos de sentencia** —FGR
  delegación Sinaloa, comunicados atribuidos **DPE/3852, DPE/3849 y DPE/3850 de 2026**—. ⚠️ **El control
  `procedencia-cifras` los tumbó y el arbitraje del coordinador CONFIRMÓ el descarte**: no existe fragmento
  citable (ver abajo). **El corte cierra con CERO sentencias integrables**, y el ciclo cumplió su función
  real, que **no es garantizar hallazgo sino hacer demostrable el `SIN DATO`**.
- **Centro**, encabezando judicial, localizó el **candidato de Teotihuacán** (no integrado) y **descartó
  una trampa de año** en `morelos.gob.mx` (narcolaboratorio de Yautepec/Jonacatepec, que es del
  **11-oct-2025**, no del corte).
- **Cuarta edición consecutiva** en que la producción judicial integrable del país **es federal y no
  estatal**. **Las 32 fiscalías estatales dieron cero por tercer corte seguido.**

**A ARGOS 115 le toca el CICLO B — Noreste + Golfo.** No queda ninguna entidad `NO REVISADA`, así que el
ciclo se aplica limpio, sin prioridad de saldo.

**Asignación explícita de la deuda regional, en rotación** (funciona: seis ediciones al remanente dieron
cero, tres asignándola dieron resultado):

- **SEDENA / SEMAR / FGR / ANAM regionales → NOROESTE**: produjo los tres candidatos judiciales **y el
  aseguramiento de Rosario**; los candidatos no superaron el umbral de fuente.
- **Mesas de Construcción de la Paz → OCCIDENTE**: **resultado negativo declarado.** Ninguna de las seis
  entidades tiene portal de mesa con desglose numérico equivalente al de Morelos. La Mesa de Colima
  republica por `afmedios.com`, pero sus boletines localizables son de junio de 2026.
- **A ARGOS 115**: **SEDENA/SEMAR/FGR/ANAM → CENTRO** · **Mesas de Construcción de la Paz → GOLFO**.

---

## La regla nueva de `site:` — primera edición aplicándola, y funcionó

Se sustituyó el objetivo porcentual por la regla: **`site:` solo contra dominios con fecha en la ruta;
contra los demás, consulta genérica.**

| Región | Búsquedas | Con `site:` | Genéricas | % genérica |
|---|---|---|---|---|
| Noroeste | 16 | 0 | 16 | **100 %** |
| Noreste | 15 | 1 | 14 | **93 %** |
| Occidente | 12 | 1 | 11 | **92 %** |
| Centro | 17 | 2 | 15 | **88 %** |
| Golfo | 7 | 0 | 7 | **100 %** |
| Sureste | 9 | 0 | 9 | **100 %** |
| **Total regional** | **76** | **4** | **72** | **95 %** |

**Diagnóstico: la regla resuelve el problema que el porcentaje no resolvía.** Durante tres ediciones el
objetivo de `site:` se incumplió siempre en la misma dirección, y la causa era que **obligaba a gastar
`site:` contra dominios que devuelven *home pages***. Con la regla, las cuatro consultas `site:` del corte
fueron **todas contra dominios con fecha en la ruta** —`seguridad.slp.gob.mx`,
`boletines.guanajuato.gob.mx`, `fiscaliageneralqro.gob.mx`— y **una de ellas produjo un descarte firme**:
Querétaro, cuyo boletín más reciente indexado es del 26-ago, lo que convierte su `SIN RESULTADO` en
demostrable en vez de supuesto.

**Conclusión para ARGOS 115: mantener la regla y NO reintroducir un objetivo porcentual.** El reparto
~60-65 % genérica que fijaba el arranque **queda superado por la propia regla**: con pocos dominios
fechados disponibles, la genérica sube naturalmente al 95 %, y eso es correcto, no desviación.

**Dominio fechado NUEVO, hallazgo de método de Sureste**: **`fiscaliaguerrero.gob.mx/index.php/AAAA/MM/DD/`**
lleva **fecha en la ruta**. Contradice el supuesto del encargo y **es candidato a `site:` en próximos
cortes**. No se explotó por presupuesto.

---

## El recall nacional del coordinador — quinta edición como paso de mayor rendimiento

| Origen del hecho | ARGOS 111 | ARGOS 112 | ARGOS 113 | **ARGOS 114** |
|---|---|---|---|---|
| Barridos regionales | 4 de 6 | 3 de 7 | 4 de 6 | **3 de 8** |
| **Recall y arbitraje del coordinador** | 2 de 6 | 4 de 7 | 2 de 6 | **5 de 8, incluidos el hecho principal y las tres sentencias** |

**El recall trajo el hecho de apertura del corte** —la activación del **Plan DN-III-E** por la SEDENA y el
compromiso presidencial de informe desde Zacatecas—, que **ningún barrido regional vio**, por la razón
estructural ya documentada: **un hecho nacional de gran cobertura se busca mejor por tema que por
entidad, y los barridos están organizados por entidad.**

---

## ⚠️ ARBITRAJE DEL COORDINADOR — rindió TRES veces, y en las DOS direcciones

**Es el control que no es un subagente, y por tercera edición consecutiva es el que más cambia el
producto.**

**1. Contra una exclusión que causó mi propia instrucción — cambió el conteo nacional del corte.**
El encargo al Noroeste incluía «no gastar búsqueda en Agua Verde» (era un pendiente de topónimo). El
barrido, correctamente, **excluyó por esa instrucción un evento del 1-sep** que resultó ser **el mayor
aseguramiento del corte**: **9 fusiles AK-47, 54 cargadores, 2,620 cartuchos, 10 placas balísticas y
9 detenidos** en Rosario, Sinaloa. Una búsqueda de arbitraje lo recuperó e integró.
**Lección: una instrucción de «no gastar» sobre un topónimo puede suprimir un hecho nuevo en ese mismo
topónimo. La instrucción debe acotarse al pendiente, no al lugar.**
**Y de paso cerró el pendiente**: **Agua Verde es localidad del municipio de ROSARIO**, que es
exactamente lo que `ARG-112-005` llevaba dos ediciones sin poder fijar.

**2. Contra un `PENDIENTE` que el buscador dejó a medias — y aquí el ARBITRAJE SE EQUIVOCÓ, y el control
lo corrigió.**
El Noroeste dejó los comunicados de la FGR Sinaloa en `PENDIENTE DE CONFIRMACIÓN OFICIAL`. Dos búsquedas
de arbitraje parecieron **verificar los títulos literales** de DPE/3852, DPE/3849 y DPE/3850, y el borrador
los integró como tres sentencias. ⚠️ **`procedencia-cifras` demostró que no había fragmento citable**, y
una tercera búsqueda de arbitraje **le dio la razón**. Ver «La retractación» más abajo.
**Sin el control, la edición habría publicado tres sentencias inexistentes.**

**3. Contra un `NO INTEGRAR` que había que confirmar — y aquí el arbitraje CONFIRMÓ el no integrar.**
Centro marcó el caso de Teotihuacán como `PENDIENTE DE CONFIRMACIÓN OFICIAL`. Se arbitró con búsqueda
propia, **igual que en ARGOS 113 se hizo con la sentencia de Puebla, donde el arbitraje sí encontró el
comunicado**. Aquí **no apareció ningún comunicado de la FGR** para este caso.
**Y el arbitraje corrigió además al propio barrido**: Centro reportó «50 años **cada uno**», pero las
fuentes solo dicen «cada uno» **de la multa**; **de la prisión no**. Es el mismo supuesto de
`PENA COMPUESTA` de ARGOS 113.
**Arbitrar no siempre es integrar: aquí sostuvo el descarte y evitó publicar 200 años inexistentes.**

**4. Deslinde entre dos regiones sobre el mismo hecho** (regla nacida en ARGOS 113): **Sureste y Noreste
informaron ambos de «Villa de La Paz»**. Sureste lo identificó correctamente como **falso positivo del
resumidor en su región** (es San Luis Potosí, no Guerrero) y Noreste lo reclamó como propio.
**Las dos regiones acertaron y no hubo fusión indebida.** El control funcionó sin necesidad de arbitraje.

---

## ⚠️ LA RETRACTACIÓN — TRES SENTENCIAS RETIRADAS ANTES DE PUBLICAR

**Es el hallazgo más importante de esta edición y lo produjo un control, no el coordinador.**

El borrador integraba **tres sentencias condenatorias de la FGR delegación Sinaloa** —comunicados
atribuidos **DPE/3852/2026** («sentencia condenatoria de más de seis años… una persona detenida con arma
de fuego»), **DPE/3849/2026** («…contra dos personas detenidas con armas y narcótico en Culiacán») y
**DPE/3850/2026** («sentencia de más de cuatro años… delito contra la salud»)—, con **4 personas
sentenciadas**, y deslindaba **DPE/3851 y DPE/3853 como vinculación a proceso**.

**`procedencia-cifras` repitió la búsqueda con cadenas exactas entre comillas y encontró esto:**

- `"DPE/3852/2026"`, `"DPE/3849/2026"`, `"DPE/3850/2026"` → **cero resultados relevantes**.
- Las cadenas exactas de los tres títulos → **sin coincidencia**. Las únicas rutas devueltas son
  **páginas índice de portales espejo de la FGR** (`hasvistoa.fgr.org.mx`, `renadet.fgr.org.mx`,
  `inacipe.fgr.org.mx`) con **paginación arbitraria y sin fecha propia**, que **no contienen el texto**.
- ⚠️ **El único titular real con esa redacción es de BAJA CALIFORNIA, no de Sinaloa.** El molde de título
  es **el que la FGR reutiliza en decenas de delegaciones y fechas**.
- **El número de comunicado, la entidad y la fecha aparecen ÚNICAMENTE en el resumen generado por el
  buscador.** Es **el patrón Huajicori**, exactamente.

**El coordinador arbitró antes de obedecer, como manda la regla, y el arbitraje CONFIRMÓ el descarte**:
una tercera consulta devolvió las mismas páginas índice y la misma síntesis, sin un solo titular con el
número de comunicado.

### La lección de método, que es la que hay que conservar

⚠️ **DOS CONSULTAS AL MISMO BUSCADOR NO SON DOS FUENTES.** El borrador afirmaba en las tres fichas
«**título literal verificado en dos consultas independientes**». **No lo eran**: eran dos preguntas al
mismo resumidor sobre el mismo índice, y **repetir la pregunta confirma al resumidor, no al hecho**.
**Una verificación solo cuenta si devuelve un titular, encabezado o URL que contenga el dato** —aquí, el
número de comunicado—. **Si el dato solo vive en el párrafo de respuesta del buscador, no existe.**

### Consecuencia sobre el producto

| Campo | Borrador | Publicado |
|---|---|---|
| Sentencias condenatorias | 3 | **0** |
| Personas sentenciadas | 4 | **0** |
| Fiscalías con sentencia integrable | 1 | **0** |
| Eventos verdes en el semáforo | 5 | **2** |
| Cobertura judicial | 1 + 29 + 2 + 0 = 32 | **0 + 30 + 2 + 0 = 32** |

**Los dos casos quedan publicados como candidatos declarados y no integrados**, con **lo que le falta a
cada uno**, para que ARGOS 115 los cierre. `ARG-114-FE-008`.
**Los tres ARG-ID `ARG-114-SEN-*` quedan sin usar y retirados del índice.**

---

## Corrección del segundo control — Michoacán en el cuadre de cobertura

**`editor-duplicidad`** detectó que el cartelón declaraba **«6 con hallazgo»** incluyendo **Michoacán**,
que **no tiene ficha, fila ni entrada en `EVENTOS` en el cartelón**, porque su hallazgo se resolvió por
**fe de erratas** (`ARG-114-FE-001` y `-002`) al tratarse de un hecho **ya publicado** en `ARG-113-REC-001`.
**Contabilizar en el cartelón una entidad que el lector no puede verificar dentro del propio cartelón
viola la auditabilidad.**

**Corregido en sitio**: el cuadre público pasa de **6 + 25 + 1 + 0** a **5 + 26 + 1 + 0 = 32**.
**Este archivo conserva las 6 entidades con hallazgo**, porque aquí el trabajo sobre Michoacán **sí es
verificable**. `ARG-114-FE-009`.

**Todo lo demás que auditó `editor-duplicidad` pasó**: cero duplicidad interna, cero hechos ya publicados
presentados como nuevos, cero repetición entre secciones, cero `-FE-` en cartelón y móvil, paridad
completa escritorio/móvil, regla de las cinco líneas cumplida en los 16 bloques, y **las dos recuperaciones
fuera de `EVENTOS`, del semáforo, del radar y del mapa**, con ventana de origen declarada.

---

## Los siete ejes encomendados — resultado, con el tope duro respetado

| Eje | Tope | Gastadas | Resultado |
|---|---|---|---|
| **1. Zacatecas** (peritaje + Luis Moya + quinto ataque) | 3 en total | 3 | **(a) `SIN AVANCE`** · **(b) HALLAZGO MAYOR** · (c) **NO hubo quinto ataque** |
| **2. Los dos detenidos** | 2 | 2 | **RESERVA RESUELTA E INTEGRADA** · judicialización `SIN AVANCE` |
| **3. Baja California — Valdez Mainero** | 2 | 2 | **VERIFICADO Y PUBLICADO** como `ARG-114-REC-001` |
| **4. Michoacán — Los Reyes** | 2 | 2 | **CONFIRMADO INSTITUCIONALMENTE** — fe de erratas, no ficha |
| **5. Ciclo A + deuda regional** | — | — | **Aplicado y declarado** (arriba). **Cero sentencias integrables tras la retractación** |
| **6. Durango o Sinaloa «16 y 22»** | 1 | 1 | **RESUELTO Y CERRADO** |
| **7. Matamoros — serie y marcaje** | 1 | 1 | **`SIN AVANCE`** |

### Eje 1 — Zacatecas

**(a) El peritaje del artefacto de Piedra Gorda: `SIN AVANCE`, y con un deslinde que importa.**
Lo que sí se peritó y se publicó es el **coche bomba EMPLEADO en Ojocaliente** («los peritajes
determinaron que se trató de un coche bomba»). **El niple ASEGURADO e íntegro de Piedra Gorda
(`ARG-113-ARM-003`) NO tiene dictamen publicado.** Son dos objetos distintos y el resumidor los
devuelve juntos. **Sigue siendo la única línea de la serie que no depende de que la autoridad publique
nada, sino de que perite lo que ya tiene**, y el precedente en contra —55 artefactos destruidos *in situ*
en el sur de Sinaloa sin caracterizar— sigue vigente.

**(b) LUIS MOYA — HALLAZGO MAYOR: NO ES UN ATAQUE, SON DOS.**
El archivo de ARGOS **no tenía ninguno** (`grep` de «Luis Moya» en `indice-arg-id.md`: cero resultados).
El barrido localizó **dos ataques con explosivo contra la policía de Luis Moya en 2026**, ambos con
**fecha en la ruta** y **fuera de toda ventana abierta**:

| Fecha | Hecho | Saldo | Fuentes con fecha en la ruta |
|---|---|---|---|
| **5-mar-2026**, ~18:00 | Ataque con explosivo a la **Comandancia** | **3 uniformados heridos** | `proceso.com.mx/…/2026/3/6/…` · `infobae.com/mexico/2026/03/06/…` |
| **31-jul / 1-ago-2026**, noche | Ataque con explosivo y arma de fuego cerca de la Comandancia, **comunidad de Barranquilla** | **1 policía municipal MUERTO**, 2 heridos | `jornada.com.mx/noticia/2026/08/01/…` · `elfinanciero.com.mx/estados/2026/08/01/…` |

`NO SE ARBITRA CUÁL CUENTA EN EL «CUATRO» OFICIAL.` **Lo que sí queda acreditado es que el conteo
oficial de «cuatro ataques del año» no es reconciliable con lo documentado**, y que **la serie incluye
un policía muerto que no figuraba en ningún balance de ARGOS**. Lo cierra un corte de la FGJEZ con
criterio de conteo explícito.

**(c) ¿Hubo un quinto ataque en la ventana?** **No.** Ningún ataque con explosivos en las 21 h del corte.

**⚠️ Las dos listas de emisores NO se fundieron**, como exigía el encargo: la de **explosivos**
(4 municipios) y la de **agresiones a elementos policiacos** de la FGJEZ (**7 municipios**: Valparaíso,
Fresnillo, Villanueva, Jerez, Ojocaliente, Luis Moya y Villa Hidalgo) **son universos distintos**.
Unirlas sería síntesis propia de ARGOS.

**Las cuatro cifras de balance contradichas siguen sin arbitrar** —17 en dos años · 10 en 2026 · 7 contra
policías en 2026 · «el 4.º del año»—. **El hallazgo de Luis Moya las agrava**, no las resuelve.

### Eje 2 — Los dos detenidos

**RESERVA VIVA RESUELTA E INTEGRADA AL CARTELÓN.** **Ambos detenidos son originarios de Aguascalientes**:

- **Juan Pedro «N», 29 años** (Ojocaliente; capturado el **1-sep en Piedra Gorda, Cuauhtémoc, Zacatecas**):
  **fuente INSTITUCIONAL** — `zacatecas.gob.mx`, comunicado propio — más nacionales (El Imparcial,
  Aristegui, Excélsior, SDP, Milenio).
- **William Ariel «N», 18 años** (Villa García; capturado el **30-ago en Asientos, Aguascalientes**):
  **fuentes NACIONALES** — El Heraldo de México, Infobae, El Financiero — y **regional** LJA.mx
  («Aguascalentenses son señalados como presuntos generadores de violencia en Zacatecas»).

**Cumple el estándar exigido (institucional + nacional) y por eso se integra.**
**⚠️ NO SE FUNDIERON**: son **dos detenciones, dos fechas, dos entidades, dos carpetas**. El deslinde está
escrito en la ficha `ARG-114-001` y en las de la edición anterior.

**Situación jurídica: `SIN AVANCE` en ambos.** Ninguno tiene vinculación a proceso publicada.
**Dato nuevo**: **William Ariel «N» fue entregado a la FGR** — cambio de fuero, sin causa penal difundida.

**Accionador de Villa García: `SIN AVANCE` en lo técnico.** Se confirma el mecanismo —motocicleta
interceptada por civiles armados y **explosivo detonado a distancia por los propios sospechosos**—, pero
**no se publicaron identificadores de fábrica, marca ni tipo de accionador** (radiofrecuencia o
telefonía). **Tercera edición sin avance: sigue siendo la única pieza capaz de identificar al operador
sin testigo.**

### Eje 4 — Michoacán · «El Wicho»/«R5»: CONFIRMADO, y con corrección de municipio

**El pendiente se cierra, pero NO produce ficha en el cartelón**, porque el hecho es de la **madrugada
del lunes 31-ago** —fuera de la ventana— y **ya está publicado como `ARG-113-REC-001`**. Republicarlo
sería duplicación. Lo nuevo va a fe de erratas.

- **Abatimiento CONFIRMADO institucionalmente**: el titular de la SSPC lo confirmó públicamente el
  **1-sep**; existe **parte atribuido a la SEDENA**, alcanzado **por republicador**
  (`fuentesfidedignas.com.mx/index.php/2026/09/01/…`) — **corroboración débil por construcción**.
- **⚠️ CORRECCIÓN DE MUNICIPIO**: el operativo fue en el asentamiento **Rodeo del Pinal, municipio de
  TOCUMBO**, no en Los Reyes como publicó ARGOS 113. Tocumbo colinda con Los Reyes y la organización se
  denomina «Cártel de Los Reyes», lo que explica la confusión. → **`ARG-114-FE-001`**.
- **Resultados del parte**: **2 fusiles automáticos**, cartuchos y cargadores «de varios calibres»
  **sin cifra exacta** (`CANTIDAD NO DETERMINADA`), **1 cuatrimoto**, **2 muertos** («R5» y un
  acompañante), **0 detenidos**. → **`ARG-114-FE-002`**. **No se integra a ningún total de ARGOS 114**:
  el hecho es de ventana anterior.
- **Sucesión**: **segunda descabezada en un mes** —«Poncho la Quiringua» detenido el 1-ago; «R5», que
  asumió tras esa detención, muerto el 31-ago—. **Sin sucesor confirmado**; la cobertura señala
  expresamente la incertidumbre. **No se localizó ningún hecho de disputa por la sucesión ya
  materializado.** **La ventana inmediata sigue siendo la de mayor probabilidad de repunte.**

### Eje 6 — «16 detenidos y 22 armas»: CERRADO, y el planteamiento heredado era erróneo

**No era una cifra atribuida a dos entidades. Son DOS EVENTOS DISTINTOS con cifras coincidentes:**

- **Durango**: SSP estatal, publicación **31-ago** (`yucatan.com.mx/mexico/2026/08/31/…`).
- **Sinaloa**: SSP estatal, **agregado de operativos en 20 municipios del 23 al 30-ago**, publicación
  **31-ago** (`infobae.com/mexico/2026/08/31/…`).

**Ambos son anteriores al inicio de la ventana (1-sep 13:17) y ninguno se integra a ARGOS 114.**
**El pendiente se cierra: la coincidencia numérica era casual, no un error de atribución.** **No reabrir.**

### Eje 7 — Matamoros: `SIN AVANCE`

Ninguna fuente publica **números de serie ni marcaje** de las 4 armas largas de `ARG-113-002`. El cotejo
con las **210 armas de Texas** interceptadas el mismo día a menos de 300 km **sigue sin poder practicarse**.
**Trampa evitada**: se identificó un **operativo distinto** en la periferia de Matamoros (4 armas largas,
19 cargadores, 306 cartuchos, 15 kg de mariguana, 3 chalecos), **sin fecha fijada**, y **no se fundió** con
el del 31-ago.

---

## Fes de erratas de esta edición — **NINGUNA figura en el cartelón**

Se registran aquí y en `_pendientes.md`; sus ARG-ID se asientan en `indice-arg-id.md`.

| ARG-ID | Sobre | Corrección |
|---|---|---|
| `ARG-114-FE-001` | `ARG-113-REC-001` (Michoacán) | **Municipio corregido**: el operativo fue en **Rodeo del Pinal, municipio de TOCUMBO**, no en Los Reyes. Tocumbo colinda con Los Reyes y la organización se llama «Cártel de Los Reyes»: de ahí la confusión. **El deslinde con `ARG-98-005` y `ARG-102-002` se mantiene** |
| `ARG-114-FE-002` | `ARG-113-REC-001` (Michoacán) | **Abatimiento CONFIRMADO institucionalmente** (SSPC, 1-sep), donde ARGOS 113 decía «no confirmado». **Parte de SEDENA por republicador**: 2 fusiles automáticos, munición sin cifra, 1 cuatrimoto, 2 muertos, 0 detenidos. **Corroboración débil por construcción.** No se integra a ningún total |
| `ARG-114-FE-003` | `ARG-112-005` (Sinaloa) | **`RESERVA DE TOPÓNIMO` CERRADA**: **Agua Verde es localidad del municipio de ROSARIO**, acreditado por las fuentes del hecho del 1-sep. Se retira la reserva abierta contra `ARG-102-REC-001` y `ARG-106-004` |
| `ARG-114-FE-004` | `ARG-113-002` (Matamoros) | **FE DE ERRATAS SOBRE EL ARCHIVO, NO SOBRE EL CARTELÓN — la premisa del encargo del coordinador era incorrecta y `procedencia-cifras` la corrigió.** **El cartelón de ARGOS 113 publicó 9,5 y es correcto**; quienes arrastraban «**8,2**» eran **este índice y `argos-2026-09-01-fuentes.md`**, con el cociente **nacional** del borrador (41 ÷ 5) aplicado por error al subconjunto de Matamoros (**38 ÷ 4 = 9,5**). **No hay contradicción entre ediciones publicadas.** Entrada del índice **corregida en sitio**. Ninguna cifra de aseguramiento se modifica |
| `ARG-114-FE-008` | Borrador de ARGOS 114 | **RETRACTACIÓN de las tres sentencias de la FGR Sinaloa antes de publicar.** Ver «La retractación» arriba |
| `ARG-114-FE-009` | Borrador de ARGOS 114 | **Michoacán retirado del cuadre de cobertura del cartelón**: 6 + 25 + 1 + 0 → **5 + 26 + 1 + 0 = 32**. Ver arriba |
| `ARG-114-FE-005` | Candidato heredado «16 y 22» | **Planteamiento heredado erróneo**: no es una cifra atribuida a dos entidades, son **dos eventos distintos** con cifras coincidentes, ambos del 31-ago. **Cerrado** |
| `ARG-114-FE-006` | Candidato heredado Tabasco «26 detenidos» | **Fechado y cerrado por obsoleto**: es el operativo **FIRT Olmeca del 22 al 25 de JUNIO de 2026**, más de dos meses antes de cualquier ventana reciente. Desglose del comunicado: 4 armas de fuego, 2 cargadores, 6 cartuchos, +400 dosis, 1 kg de mariguana, 26 detenidos (24 hombres, 2 mujeres) |
| `ARG-114-FE-007` | Candidato heredado Coatzacoalcos–Villahermosa | **Ubicado y fechado**: **Huimanguillo, Tabasco**, publicación **31-ago** en cuatro medios coincidentes. **La discrepancia de metanfetamina se resuelve**: las cuatro fuentes dan **81 kg**; **la variante de 87 kg no aparece en ninguna**. Cifra sostenida: **1,822 kg de mariguana + 81 kg de metanfetamina**. **Fuera de la ventana de ARGOS 114** |

---

## Contradicciones que ARGOS 114 NO arbitra

| Caso | Estado |
|---|---|
| **Viviendas afectadas en Ojocaliente** | **~40** (autoridad estatal, 1-sep) frente a **~30** (cobertura del 2-sep). **Vehículos coincidentes: 13** (11 particulares + 2 patrullas); **lesionados: 11**, sin variación. `CIFRAS CONTRADICHAS — NO SE ARBITRAN`. **Cuarta rectificación potencial del mismo hecho**: el saldo ya fue 7 → 10 → 11 |
| **Cuántos ataques con explosivos lleva Zacatecas** | Las cuatro cifras siguen en pie **y ahora hay una quinta pieza**: **Luis Moya tiene DOS ataques documentados en 2026**. `NO SE ARBITRA` |
| **La pena de Teotihuacán** | **La multa se publica «cada uno» ($292,160); la prisión, no.** `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`. Si fuera por persona el acumulado nacional subiría 200 años; si conjunta, 50. **No se integra por otro motivo además: no hay comunicado oficial** |
| **Indicadores nacionales del Segundo Informe** | **32,824 armas y 519 t de droga** (Presidencia, administración completa) frente a **24,000 armas y +346 t** (balance de periodo distinto). **Alcances distintos, no necesariamente incompatibles.** `NO SE ARBITRAN` · **ninguna se usa como denominador** |

---

## Indicador de cobertura nacional — **cuadra con 32**

| Casilla | N.º | Entidades |
|---|---|---|
| **Con hallazgo** | **6** | Sinaloa · San Luis Potosí · Zacatecas · Veracruz · Baja California · Michoacán |
| `SIN RESULTADO INDEXADO EN VENTANA` | **25** | Las demás |
| **Vacío acreditado** | **1** | **Tlaxcala** (ambos dominios resuelven; ninguno publica boletines individuales fechados) |
| `NO REVISADA` | **0** | — |
| `SIN ACTUALIZACIÓN CONSTATADA` | **0** | **No utilizable**: exige lectura directa y el egreso está bloqueado |
| **TOTAL** | **32** | **6 + 25 + 1 + 0 = 32** ✔ |

**Indicador de cobertura judicial**: Fiscalías revisadas **32 de 32** · FGR revisada **Sí** · con sentencia
**integrable** en ventana **0** —**tras la retractación**— · `SIN RESULTADO INDEXADO EN VENTANA` **30** ·
**vacío acreditado 2** (Tlaxcala; **FGE Veracruz**, cinco cortes de agregados sin individualizar) ·
`NO REVISADA` **0** · **0 + 30 + 2 + 0 = 32** ✔
**Nota**: el cuadre NACIONAL del cartelón es **5 + 26 + 1 + 0 = 32** (sin Michoacán, ver arriba); el de este
archivo es **6 + 25 + 1 + 0 = 32** (con Michoacán, cuyo trabajo aquí sí es verificable). **La diferencia es
deliberada y está declarada.**

**Vacíos acreditados respetados, sin gasto de búsqueda**: Tlaxcala · FGE Veracruz ·
`ssypc.nayarit.gob.mx`. **No publican indexable**: FGJ Nuevo León · SSP Zacatecas ·
`fgjsonora.gob.mx` (**quinta edición sin resultado, ni confirmado ni descartado**).

---

## `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verificado y declarado

**Verificado en esta edición, no heredado.** La migración **está acreditada**: desde el 1-sep los reportes
diarios de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí para las 32 entidades.
**Ningún reporte del 1 ni del 2 de septiembre resultó alcanzable**, ni por búsqueda dirigida ni genérica:
el dominio está indexado pero **sus rutas no llevan fecha**. **La trampa de año persiste** y **ninguna
cifra del dominio se usa**. **Verifíquelo cada corte y declare el resultado.**

---

## Deuda de método que ARGOS 114 deja abierta

1. ⚠️ **Una instrucción de «no gastar búsqueda en X» puede suprimir un hecho nuevo en X.** Es el fallo
   evitado más importante de esta edición: la instrucción sobre «Agua Verde» —dirigida a un pendiente de
   topónimo— hizo que el barrido excluyera **el mayor aseguramiento del corte**, ocurrido en ese mismo
   lugar. **Regla derivada: las prohibiciones de gasto deben redactarse contra el PENDIENTE, no contra el
   TOPÓNIMO** —«no reinsistir en el municipio administrativo de Agua Verde», no «no gastar en Agua Verde»—.
   **Y el coordinador debe revisar toda exclusión que un barrido atribuya a una instrucción suya.**
2. **El reparto porcentual de búsquedas deja de ser indicador, definitivamente.** Con la regla nueva la
   genérica subió al **95 %** y **eso es el comportamiento correcto**, no una desviación. **No
   reintroducir objetivos porcentuales en ARGOS 115.**
3. **Cuarta edición seguida en que la producción judicial integrable es federal.** **Mantener el triaje
   dirigido a las delegaciones de la FGR** antes que a las fiscalías estatales: es lo que produjo las tres
   sentencias de esta edición.
4. **El ciclo de publicación de las fiscalías estatales es más lento que las ventanas cortas.** Tercer
   corte con cero de las 32. **No retirar el ciclo**: su función es hacer **demostrable** el `SIN DATO`.
5. **Tres ventanas consecutivas decrecientes** —48 h, 27 h, **21 h**—. **Los totales no son comparables
   sin normalizar por duración**, y así se declara en el cartelón. **Conviene fijar horas de arranque más
   estables.**
6. **`fiscaliaguerrero.gob.mx` lleva fecha en la ruta** y no se explotó. **Asignar a Sureste en ARGOS 115.**
7. **Dominios institucionales de Hidalgo y Puebla sin confirmar** por `site:`. Verificar en la próxima
   edición que Centro encabece.
8. ⚠️ **«VERIFICADO EN DOS CONSULTAS INDEPENDIENTES» NO SIGNIFICA NADA SI LAS DOS SON AL MISMO BUSCADOR.**
   Es la lección de la retractación y **debe entrar en las trampas verificadas**. Una verificación cuenta
   **solo si devuelve un titular, encabezado o URL que contenga el dato**. Si el dato vive únicamente en el
   párrafo de respuesta del motor, **no existe**.
9. ⚠️ **UN INDICADOR DE COBERTURA DEL CARTELÓN NO PUEDE CONTAR LO QUE EL CARTELÓN NO PUBLICA.** El archivo
   de fuentes sí. **Los dos cuadres pueden diferir, pero la diferencia se declara.**
10. **La protección balística sigue siendo conclusión permanente, no línea de búsqueda**: **41 placas
   acumuladas** (cálculo propio) y **ninguna con marca, nivel NIJ ni lote**. **No se le asigna búsqueda.**

---

## Autorización de subagentes

El destinatario autorizó **los seis barridos regionales y los dos controles editoriales**. Los ocho se
ejecutaron. El **arbitraje del coordinador** —que no es un subagente— se ejecutó además, y es el que
produjo cinco de los ocho hechos de la edición.
