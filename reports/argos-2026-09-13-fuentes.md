# ARGOS 119 — Archivo de fuentes, método y trazabilidad

**Corte**: 2026-09-13 · **Ventana**: 2026-09-08 10:38 → 2026-09-13 08:28 CDMX (**117 h 50 min**, casi
cinco días) · **Hora real verificada** con `TZ=America/Mexico_City date` al arranque de la sesión.

Este archivo recoge lo que **no** va al cartelón: método, hallazgos sobre el instrumento, fes de erratas,
disposición de candidatos y registro del barrido. El cartelón es para el mando; esto es para la auditoría.

---

## 0. Verificación de base (Bloque 0 del arranque)

| Comprobación | Resultado |
|---|---|
| `TZ=America/Mexico_City date` | **2026-09-13 08:28 CST (CDMX)** |
| `git merge --ff-only origin/main` | **Fast-forward aplicado**: la rama llegaba en `argos-2026-08-24` (ARGOS 106), **trece ediciones por detrás**. **Decimotercera vez consecutiva que falla.** |
| Última edición del archivo tras el merge | `argos-2026-09-08` (**ARGOS 118**) ✅ |
| `ls reports/ \| wc -l` | **99** ✅ |
| Numeración deducida | **ARGOS 119**, del archivo, no de la rama |

**Sin la orden del Bloque 0 esta edición se habría numerado como un falso «ARGOS 107» con ventana solapada
de veinte días.**

---

## 1. La ventana: qué cambió y qué se aplicó

**No se generó ARGOS del 9 al 12 de septiembre.** La ventana dura **117 h 50 min** frente a las
**26 h 22 min** de ARGOS 118 y las **47 h** de la más larga de la serie hasta ahora. Es **4,5 veces** la
anterior y **2,5 veces** el récord previo.

Consecuencias aplicadas, no solo declaradas:

1. **Se esperaron y se encontraron muchos más hechos**: **19 fichas de hecho** frente a 5, repartidas en
   **once páginas** en vez de ocho. **Ninguna tarjeta se comprimió**: cuando el bloque creció, se repartió
   entre más páginas.
2. **La regla «solo el día» se mantuvo intacta, pero «el día» son cinco**: un hecho del 9-sep es de esta
   ventana, **no una recuperación**. Por eso esta edición tiene **cero `-REC-`**.
3. **Los totales se declararon expresamente no comparables**, en portada y en Valoración, y **se publicó la
   densidad por hora**, que es lo único comparable: **0,16 hechos/hora** frente a **0,19** del corte
   anterior. **Más hechos en total, menos por unidad de tiempo.**
4. **Se revisó el seguimiento perecedero que vencía dentro de la ventana**: el plazo de 24 horas de
   «Los Rusos» (§4.2) y la Fenaza (§4.4).

**Ejes que quedaron sin interrogar por presupuesto**, declarados expresamente y **no disfrazados de vacío
acreditado**: el peritaje del AEI de Villas del Real (`ARG-115-003`, **cuarta vez**), el niple de Piedra
Gorda (`ARG-113-ARM-003`, **séptima**), la marca y lote del inhibidor (**sexta**), el cohecho de Tempoal,
las detenciones de Omealca, Tepuche, los cartuchos cal. .45 de Chihuahua y la contradicción de lesionados
de `ARG-110-001` (**décima**).

---

## 2. Bloqueo de egreso — verificado en esta sesión, no heredado

```
curl https://www.gob.mx/sspc                      → curl: (56) CONNECT tunnel failed, response 403
curl https://gabinetedeseguridad.gob.mx/resultados/ → curl: (56) CONNECT tunnel failed, response 403
WebFetch https://www.tallapolitica.com.mx/...      → EGRESS_BLOCKED
```

**El bloqueo no es solo de `*.gob.mx`**: alcanza también a **republicadores y medios regionales**. Se
comprobó con `WebFetch` contra `tallapolitica.com.mx`, que devolvió `EGRESS_BLOCKED`; **el boletín federal
del 9 y del 10-sep tuvo que reconstruirse por búsqueda dirigida, no por lectura**.

**Techo de confianza de todo el producto: ★★★★☆.** `docs/solicitud-lista-blanca-egreso.md` **sigue sin
tramitar** (verificado: el archivo existe, 6,410 bytes, sin cambios).

**Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` figura en **0** en los dos cuadres,
porque exige lectura directa. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.

---

## 3. Barrido regional y recall — de dónde salió cada hecho

**Seis agentes `barrido-regional` en paralelo**, lanzados en un solo mensaje antes de ningún otro encargo,
más el **recall nacional del coordinador**, ejecutado **antes de cerrar ningún barrido** (**décima edición
consecutiva como paso obligatorio**).

| Origen del hecho | ARGOS 117 | ARGOS 118 | **ARGOS 119** |
|---|---|---|---|
| Barridos regionales | 3 de 7 | 2 de 5 | **11 de 19** |
| Recall y arbitraje del coordinador | 4 de 7 | 3 de 5 | **8 de 19** |

**Las dos vías vuelven a rendir por razones opuestas y ninguna se retira:**

- **El recall aportó los cuatro hechos rojos** —Chilpancingo, Apatzingán, Mazatlán y Elota— **y las dos
  sentencias**. Ningún barrido vio Apatzingán ni Mazatlán. La causa sigue siendo estructural: **un hecho
  nacional de gran cobertura se busca mejor por tema que por entidad**.
- **Los barridos aportaron los dos hallazgos de mayor volumen explosivo** —**Escuinapa**, que trajo
  Noroeste indirectamente y cerró el coordinador, y **Ahuacatlán**, que trajo Occidente— y **las tres
  filas con boletín oficial primario**: **Guanajuato**, **Querétaro** y **Veracruz ×2**.
- **Occidente, encabezando judicial por el Ciclo C, produjo las dos únicas sentencias integrables del
  corte.**

**Tope duro de 2-3 búsquedas por eje respetado.** Presupuesto del coordinador: **20 consultas**.
**`site:` solo contra dominios con fecha en la ruta**; contra los demás, genérica. **El objetivo porcentual
sigue retirado y no se reintrodujo.**

### 3.1 Los cinco dominios con fecha en la ruta — consultados los cinco

| Dominio | Resultado en esta ventana |
|---|---|
| `boletines.guanajuato.gob.mx/AAAA/MM/DD/` | ✅ **PUBLICÓ**: cateo del **10-sep** entre León y San Felipe. **Segunda edición consecutiva en que aporta una fila con boletín oficial primario, y las dos veces sin que ningún medio la replique.** |
| `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` | ✅ **PUBLICÓ**: Operativo Sinergia del **11-sep**, 8 cateos y 9 detenidos. **Primera vez que rinde desde ARGOS 108.** |
| `veracruz.gob.mx/AAAA/MM/DD/` | ✅ **PUBLICÓ DOS VECES**: **8-sep** y **9-sep**. **Confirmado: la vía de Veracruz es el portal del Gobierno del Estado, no la FGE.** |
| `fiscalia.durango.gob.mx/AAAA/MM/DD/` | ✅ **PUBLICÓ**, pero **ambas sentencias caen FUERA de ventana** (2 y 5-sep). **El dominio con fecha en la ruta permitió descartarlas sin ambigüedad**: ése es su valor aunque no aporte fila. |
| `seguridad.slp.gob.mx/noticias/AAAA/M/D/` | `SIN RESULTADO INDEXADO EN VENTANA`. |

**El matiz de ARGOS 118 se confirma por segunda vez**: **el dominio con fecha en la ruta rinde con
independencia del eje por el que se le interrogue**. Guanajuato y Querétaro rindieron encabezando con
armamento; Veracruz también.

### 3.2 Ciclo de rotación

**CICLO C — Occidente + Sureste encabezaron el triaje judicial**, declarado y aplicado. Las otras cuatro
regiones encabezaron con armamento.

**Qué aportó la rotación que el orden anterior no habría aportado**: **las dos sentencias integradas del
corte son de Michoacán, entidad de Occidente**, y **ninguna habría aparecido si la región hubiera gastado
sus primeras consultas en armamento** — de hecho el armamento michoacano que trajo el mismo barrido
(**Los Amates**) **quedó por debajo del umbral y no se integró**. **Es el tercer ciclo consecutivo en que la
rotación cambia lo que el producto encuentra, y el segundo que lo hace ofensivamente.**

**Sureste cerró sus seis entidades sin sentencia integrable**, incluido el **encargo conservado de
`fge.yucatan.gob.mx`** —mejor taxonomía judicial de las 32, **rutas opacas sin fecha**, **tercer corte
consecutivo sin resultado**—. **El encargo se conserva.**

**A ARGOS 120 le toca el CICLO A — Noroeste + Centro.**

### 3.3 Cuadre de cobertura

- **Armamento**: 9 con aseguramiento integrado + 23 `SIN RESULTADO INDEXADO EN VENTANA` + 0 `NO REVISADA`
  + 0 `SIN ACTUALIZACIÓN CONSTATADA` = **32** ✅
- **Judicial**: 1 con sentencia integrada + 31 `SIN RESULTADO INDEXADO EN VENTANA` + 0 `NO REVISADA`
  + 0 `SIN ACTUALIZACIÓN CONSTATADA` = **32** ✅
- **Las 9 entidades del total de armamento son exactamente las 9 con fila integrada en la tabla**:
  Sinaloa, Nayarit, Hidalgo, Guerrero, Veracruz, Baja California, Durango, Guanajuato y Chiapas.
  **El indicador no cuenta nada que el cartelón no publique.**

---

## 4. Los seis ejes prioritarios: qué se buscó y qué se encontró

### 4.1 GUERRERO — los 22 AEI y los dos drones (`ARG-118-001`). Dos búsquedas.

**`SIN AVANCE` en las dos preguntas.** **(a) Ningún peritaje** de los 22 AEI: **sin tipo, carga ni sistema
de iniciación**. **(b) Ninguna fuente acredita que los dos drones estén adaptados para lanzar**: las
coberturas los describen como «hallados», sin calificarlos de armados. **Se mantienen en 0 drones armados y
no entran en armamento especial. No se cambió sin peritaje.**

**Pero el eje produjo un hecho nuevo que ningún barrido esperaba**: la **agresión armada contra militares en
patrullaje del 9-sep en Tlahuizapa y Coacoyulillo** (`ARG-119-001`), dentro de la **Operación Xaltianguis**,
y **cuatro detenciones más en El Ocotito el 11-sep** (`ARG-119-014`).

⚠️ **ARBITRAJE DE CLASIFICACIÓN DEL COORDINADOR, DECLARADO**: el barrido de Sureste propuso **🟡** para
`ARG-119-001` invocando la regla de «cuando no se puede determinar quién inició». **Se rechazó.** Tres
titulares de medios independientes fijan la secuencia —«**tras agredir a militares**», «**agreden a
oficiales**», «**tras ataque a fuerzas de seguridad**»— y las fuentes sitúan al personal en **recorridos de
patrullaje**, no ejecutando cateo, revisión ni orden. Es el supuesto expreso de la lista roja: **el grupo
criminal agrede a personal en patrullaje**. **🔴.** *Es el segundo corte consecutivo en que el coordinador
arbitra una clasificación propuesta por Sureste, y en direcciones opuestas: en ARGOS 118 rechazó un rojo
injustificado; aquí rechaza un amarillo injustificado. El criterio no es la prudencia, es el tipo de
evento.*

⚠️ **POSIBLE DUPLICIDAD DETECTADA Y NO INTEGRADA**: el barrido de Sureste trajo un aseguramiento en
**Xaltianguis** publicado el 9-sep con «**10 explosivos**» y «**más de 700 cartuchos**». **No coincide con
las cifras ya fijadas de `ARG-118-001`** (848 cartuchos, 22 AEI) **y nada permite descartar que sea el mismo
hallazgo reportado de otro modo**. `POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN`. **De
haberse integrado habría añadido falsamente 10 AEI al total nacional.**

### 4.2 GUERRERO — el plazo de 24 horas de «Los Rusos» (`ARG-118-REC-001`). Una búsqueda.

**`SIN AVANCE`, y el negativo es el resultado.** **No se localizó ningún ataque, incendio de patrullas ni
agresión atribuida al vencimiento del plazo.** Lo único verificado: **la Policía Estatal retiró las
cartulinas y las ponchallantas** en La Sabana (Acapulco) y Bajos del Ejido (Coyuca de Benítez) y **realizó
recorridos en las zonas vetadas, sin personas lesionadas**.

⚠️ **`SIN RESULTADO INDEXADO EN VENTANA` no equivale a «no pasó nada»**: acredita que **no se indexó ningún
ataque atribuido**, no que no lo hubiera. **Ninguna autoridad ha confirmado autoría ni autenticidad de las
cartulinas**, y eso no cambió.

**Lectura provisional, no acreditada**: **el plazo venció sin consecuencia pública**. Si se sostiene en el
corte siguiente, el indicador apunta a **intención sin capacidad de ejecución inmediata**.

⚠️ **HALLAZGO DE DESLINDE, APORTADO POR EL BARRIDO DE SURESTE Y CONSERVADO**: **«Los Rusos» de Guerrero y
«Los Rusos» de Mexicali son dos organizaciones distintas con el mismo apodo**. **No se fusionan.** Se anotó
expresamente en la ficha `ARG-119-015` (Tijuana), la única de Baja California del corte.

⚠️ **XALTIANGUIS: el cruce se agrava.** La localidad aparece **en el veto territorial de «Los Rusos»** y
**da nombre a la operación militar contra «Los Ardillos»** en la que se produjo `ARG-119-001`. **Dos
organizaciones distintas sobre la misma localidad, y el Estado nombra su operación con ella.**

### 4.3 PUEBLA — la patrulla clonada y los dos Barrett de Esperanza (`ARG-118-003`). Dos búsquedas.

**`SIN AVANCE` en las dos preguntas.** **(a) Ninguna fuente coteja el número económico ni las placas de la
patrulla clonada contra el parque vehicular de la DSPM de Esperanza.** **(b) Ningún número de serie de los
dos Barrett se ha publicado.** Tampoco el desglose corto/largo de las 33 armas restantes ni la marca y lote
del inhibidor (**sexta aparición del archivo sin atenderse**).

**Dato nuevo, sin coste extra**: la patrulla clonada llevaba **blindaje artesanal y torreta**, y el edil de
**Tepeyahualco** también está señalado como vinculado a «Los Zúñiga» — **con él van dos ayuntamientos
poblanos en la misma estructura**. **Contexto declarado, no integrado a totales.**

**Candidato NO integrado**: la noche del **8-sep** una **camioneta con torreta («falsa patrulla»)** intentó
interceptar un tráiler en la **carretera Puebla-Orizaba**; el conductor escapó y grabó el vehículo. **Sin
detenidos, sin armamento, sin víctimas, y fuente única regional**: **por debajo del umbral**. Se conserva
como candidato porque, de confirmarse, **acredita que la estructura siguió operando al día siguiente del
golpe**.

### 4.4 ZACATECAS — la Fenaza. Dos búsquedas.

**`SIN INCIDENTE — CUARTO RESULTADO NEGATIVO CONSECUTIVO.`** La feria corre del **4 al 20 de septiembre** y
esta ventana cubrió **seis jornadas de golpe** (8 al 13-sep). **No se localizó artefacto, amenaza, detención
ni incidente** en el recinto o su perímetro. Las dos búsquedas devolvieron **cartelera artística** y
contenido anterior al 4-sep.

**El dispositivo de 787 elementos (`ARG-115-001`) NO se recontó.** **El indicador sigue siendo si aparece
artefacto en zona de concentración masiva**, y **sigue en negativo**. **La feria cierra el 20-sep: quedan
siete días y es el seguimiento más perecedero que hereda ARGOS 120.**

### 4.5 NAYARIT — por qué Nayarit no sabía de sus seis muertos (`ARG-118-004`). Una búsqueda.

**`SIN AVANCE`.** **Ningún boletín oficial** de Zacatecas, Jalisco ni Nayarit fija armamento ni fecha. **El
armamento que circula —«31 rifles», 1 ametralladora, «cinco» granadas, lanzagranadas— sigue siendo
inconsistente entre coberturas y NO se integra.** La contradicción institucional —**Nayarit declaró no tener
conocimiento del caso**— **sigue sin arbitrar**.

⚠️ **El barrido de Occidente detectó, además, que el resumidor volvió a sintetizar una fecha del hecho
(«sábado 5 de septiembre») que ninguna fuente fija literalmente en su URL ni en su titular.** Coincide por
calendario, pero **es la misma fabricación ya acreditada en ARGOS 118**. **La reserva se conserva.**

**Pero el eje produjo el segundo hallazgo explosivo del corte**: **Ahuacatlán, loc. La Gloria**
(`ARG-119-009`), con **fusil Barrett cal. .50, lanzagranadas, 5 granadas de 40 mm y 5 AEI**. **Es la primera
vez en el archivo que un mismo aseguramiento reúne las cuatro categorías.**

### 4.6 BAJA CALIFORNIA — Mexicali, col. Bosques del Sol. Una búsqueda.

✅ **CERRADO SIN INTEGRARSE, y la disposición es expresa.** El barrido de Noroeste buscó una segunda fuente
coincidente y **solo halló notas que describen el mismo hecho con el mismo detenido y la misma colonia, sin
independencia real**. **La condición no mejoró**: sigue siendo **fuente única regional sin comunicado
oficial**, por debajo del umbral «Bajo». **Y su publicación es del ~7-sep, anterior a la apertura de esta
ventana**: de integrarse alguna vez, **correspondería a ARGOS 118, no a ARGOS 119**. **No vuelve a listarse
como candidato prioritario.**

---

## 5. Fes de erratas — no van al cartelón, sí al índice

### `ARG-119-FE-001` — El boletín federal del 10-sep republica por TERCERA vez el cateo de «El Maguey»

El **boletín del Gabinete de Seguridad del 10-sep** incluye, en Michoacán, un cateo con **2 AEI,
47 cargadores, 6 armas largas, 3 equipos, radiocomunicación y 3 vehículos con reporte de robo**. **Es el
MISMO aseguramiento que `ARG-117-004` / `ARG-118-FE-001`** —**Buenavista Tomatlán, col. El Hospital**—,
cerrado por la coincidencia exacta de **6 largas y 47 cargadores**.

**Tercera publicación del mismo hecho por tres emisores distintos en tres cortes** (SSP de Michoacán →
SEDENA/43.ª Zona Militar → Gabinete de Seguridad federal). **Detectado por el `grep` de topónimo del
coordinador sobre lo que trajo el recall, antes de fichar nada.** **De haberse integrado habría añadido
falsamente 6 armas largas, 47 cargadores y 2 AEI al total nacional de ARGOS 119.**

**No se ficha, no se integra y no vuelve como `-REC-`.** **El archivo antiguo no se reescribe.**
**Lección: un hecho puede republicarse indefinidamente, y el localizador fino —la colonia— es lo único que
lo cierra las tres veces.**

### `ARG-119-FE-002` — Aparece el desglose de armas de `ARG-118-002`, que ARGOS 118 no pudo contar

`ARG-118-002` / `ARG-118-ARM-004` (Culiacán, carretera federal 15 a la altura de **La Campana**, entronque a
Jesús María, 8-sep, 4 detenidos) se publicó con **«armas y vehículo asegurados», sin cifra ni desglose**, y
ARGOS 118 lo registró como `CANTIDAD NO DETERMINADA`.

**Las coberturas que localizó el barrido de Noroeste en este corte consignan un desglose**: **1 arma corta,
2 armas largas, 30 cargadores y «más de 500» cartuchos**.

**Disposición**: **NO se integra a ARGOS 119** —es un hecho ya publicado, no una recuperación— y **NO se
reescribe ARGOS 118**. Se registra para que **el cero contable de `ARG-118-ARM-004` se lea como «no
publicado», no como «no había»**, exactamente igual que el caso de los 2 AEI de ARGOS 117.
⚠️ **El desglose NO está fijado en titular y «más de 500» no es cifra**: **no sería integrable ni aunque
procediera.** **Segunda confirmación de la regla: un cero de una edición anterior puede ser falso.**

### `ARG-119-FE-003` — Cero recuperaciones, y es consecuencia de la ventana larga

**ARGOS 119 no publica ninguna ficha `-REC-`.** No es un vacío de búsqueda: **es efecto directo de la
ventana de cinco días**. Los hechos que en un corte de 26 horas habrían llegado como recuperación —
Ahuacatlán (hecho del 5-sep), el operativo veracruzano del 8-sep— **caen dentro de esta ventana o se
resuelven con la marca correcta**:

- **Ahuacatlán**: hecho del **5-sep**, publicación del **9-sep** → `EVENTO ANTERIOR PUBLICADO DURANTE EL
  CORTE`, **integrado al conteo con esa marca**, sin mezclarse con los hechos de las últimas 48 horas.
- **Veracruz 8-sep**: publicado **el mismo día en que cerró ARGOS 118 (10:38)** y **esa edición no lo vio**
  → `FRONTERA DE VENTANA — HORA NO FIJADA`, **integrado por ser la edición que lo ve primero**. **Si aparece
  un ancla horaria anterior a las 10:38, procede fe de erratas y retiro del total.**

**Ningún hecho inédito de ventana anterior superó el umbral para entrar como `-REC-`.**

### `ARG-119-FE-005` — Citar un boletín no equivale a haberlo explotado, y el saldo neto de los controles fue INTEGRAR

**Detectado por `procedencia-cifras`**, que devolvió `CORREGIR ANTES DE PUBLICAR` **con razón**.
**Dos fichas daban por «no publicado» un desglose que la fuente primaria que ellas mismas citaban SÍ
publicaba.**

- **ELOTA** (`ARG-119-004` / `ARG-119-ARM-008`): el **boletín propio de la SSP de Sinaloa** publica
  **1 rifle Sporter cal. 7.62×39, 1 pistola Glock cal. 9×19, 1 pistola Super cal. .38, 6 cargadores cal.
  7.62×39, 1 cal. .38, 1 cal. 9 mm y 447 + 9 + 10 = 466 cartuchos**. El borrador lo registró como
  `CANTIDAD NO DETERMINADA`. **Efecto: +2 cortas, +1 larga, +8 cargadores**, y la fila pasa a ser **la
  única del corte con calibre publicado en todas sus piezas**.
- **LEÓN-SAN FELIPE** (`ARG-119-011` / `ARG-119-ARM-009`): el **boletín de la FSPE** especifica **«un arma
  corta tipo pistola, calibre .380 ACP, dos cargadores y cinco cartuchos útiles»**. **Efecto: el arma pasa
  de sin categoría a CORTA, +1 corta, −1 sin categoría, +2 cargadores.**

⚠️ **En los dos casos la aritmética ancló la cifra**: **447 + 9 + 10 = 466** y **5 + 748 = 753**, los dos
números que el borrador sí tenía. **Es la reserva fuerte funcionando en la dirección de integrar.**

**Tercer hallazgo del mismo control, arbitrado con búsqueda propia**: el desglose de **Ahuacatlán** era
**3 largas y 1 corta**, no 2 y 1. El **comunicado de prensa n.º 59 de la 13.ª Zona Militar, V Región
Militar** dice **«además del Barrett, dos armas largas y un arma corta»**. **Efecto: +1 larga, y la fila
sube de Bajo a Medio** al aparecer el comunicado oficial que faltaba.

**Total nacional recalculado**: de **47 a 51 armas** y de **71 a 81 cargadores**; **cocientes rehechos** a
**80,4 cartuchos por arma** y **2,61 cargadores por arma larga**.

⚠️ **Segunda vez en la serie que el saldo neto de los controles es INTEGRAR más de lo que retiran**, y
**primera en que la causa es que el borrador no había leído del todo las fuentes primarias que él mismo
citaba**.

### `ARG-119-FE-004` — Un `sed` de ensamblaje corrompió el renderizador del radar

Al sustituir el `<title>` del documento, la expresión `<title>[^<]*</title>` **alcanzó también una línea del
renderizador del radar** —`'<title>' + ev.id + " — " + ev.hecho + ...`—, rompiendo la cadena JavaScript.
**`gen-movil.py` falló con `SyntaxError` y lo destapó.** Restaurado y verificado: `node --check` limpio,
mapa de aseguramientos **distinto** del mapa nacional (no vacío), y **todos los ARG-ID resuelven a un
ancla**.

⚠️ **Lección de método, y es nueva**: **una sustitución global sobre el HTML ensamblado puede alcanzar el
bloque de datos y el renderizador, no solo la prosa**. **El generador móvil es, de hecho, el control que
detecta esa corrupción**, porque es el único paso que ejecuta el JavaScript. **Nunca se publica el
escritorio sin haber generado la móvil.**

---

## 6. Trampas verificadas en este corte

| Trampa | Cómo cayó |
|---|---|
| ⚠️ **Colisión de topónimo de LOCALIDAD — la más cara del corte** | **«La Campana» es de CULIACÁN Y de ESCUINAPA.** El hallazgo de **20 AEI** del boletín federal del 9-sep está en **La Campana y Palmillas, ESCUINAPA**; `ARG-118-002` está en **La Campana, CULIACÁN**. **Sin el deslinde, el corte habría fusionado dos hechos de dos municipios a 200 km, o los habría separado mal.** Además hubo que deslindarlo de `ARG-103-REC-001` (**27 AEI en La Campana, Escuinapa**) y de `ARG-110-002` / `ARG-111-002`. **Cuatro deslindes para un solo topónimo.** |
| ⚠️ **Segunda colisión: «Tamazula»** | Es **municipio de DURANGO** y **colonia Lomas de Tamazula en CULIACÁN, SINALOA** (`ARG-107-REC-001`). **Dos entidades, dos naturalezas.** |
| ⚠️ **Tercera colisión: «Palos Prietos»** | Ya aparecía en `ARG-107-002` (Mazatlán, Central de Autobuses, 25-ago). **Misma colonia, otro inmueble, otra fecha, otras víctimas.** **La colonia sola no identifica un caso.** |
| ⚠️ **Cuarta colisión: «San Rafael»** | El operativo veracruzano del 9-sep incluye **San Rafael, MUNICIPIO DE VERACRUZ**, no la colonia homónima de la alcaldía Cuauhtémoc, CDMX. |
| ⚠️ **Republicación en cadena de un hecho ya publicado** | El cateo de «El Maguey», **tercera vez** (§5, `ARG-119-FE-001`). |
| ⚠️ **Sede de la autoridad receptora confundida con lugar del hecho** | `ARG-117-004` se puso a disposición de la **FGR con sede en Apatzingán**, y el hecho del corte es **en Apatzingán**. **Son cosas distintas** y se deslindó expresamente en `ARG-119-002`. |
| **Agregado que no se reparte** | **Cinco casos**: el balance de **Chiapas** (1,545 armas y 97,400 cartuchos en **23 meses**), el **«Modelo de Seguridad Coahuila»** (512 cateos hasta el 30-ago), el **agregado semanal de Sinaloa** (31-ago a 6-sep: 54 detenidos, 58 armas, 9,553 cartuchos, **43 AEI**), las **43 detenciones en 36 municipios** de Veracruz y las **30 detenciones** de los once cateos. **Ninguno se integró; de los dos veracruzanos solo se tomó la subnota con desglose.** |
| **Refechado** | **Operativo «Tabscoob», Villahermosa** (15-may-2026, devuelto como de septiembre) · **Tuxtla Gutiérrez** (7-sep, antes de la apertura) · **boletín 4970 FGET** (14-jun-2026) · **sentencias de Durango** (2 y 5-sep). |
| **Folios `DPE/…` fabricados** | **Cuatro nuevos en San Luis Potosí** (`DPE/4032`, `DPE/4070`, `DPE/4071`, `DPE/4089`) y **uno en Jalisco** (`DPE/4073`), todos **sin URL propia**, insertados por el resumidor sobre una página de listado genérico. **Van veintitrés en seis cortes.** **Ninguno llegó a ninguna cifra.** |
| **Cruce cruzado de entidad** | Un medio tamaulipeco replicó el boletín federal del 10-sep bajo titular local, **pero Tamaulipas no figura entre los estados con acción ese día**. Y el arsenal de **210 armas de Sabinas Hidalgo, NUEVO LEÓN** (31-ago) lo republicó un medio veracruzano. **Se comprobó la entidad, no solo el topónimo.** |
| **«Más de» no es cifra** | Dejó fuera **«más de 1,500» cartuchos** (Cosío), **«más de 5,400»** (Sonora), **«más de 500»** (el desglose de `ARG-118-002`) y **«más de 700»** (Xaltianguis). ⚠️ **Pero NO dejó fuera los 753 de Guanajuato**: el titular dice «más de 750» y **el cuerpo del boletín oficial fija 753**. **La regla es sobre la cifra, no sobre el titular.** |
| **Día de la semana contra calendario** | **8-sep martes, 9 miércoles, 10 jueves, 11 viernes, 12 sábado, 13 domingo.** Sostuvo «la noche de este miércoles» de Apatzingán, «madrugada del viernes» de Texmelucan y la atribución del 5-sep (sábado) a Ahuacatlán. |
| ***Liveblog*** | **Cuatro coberturas «EN VIVO … hoy 9 / 10 / 11 / 12 de septiembre» de Infobae** aparecieron en el recall. **Ninguna se usó para fechar un hecho ni como fuente única.** Sirvieron solo para localizar candidatos que después se anclaron en fuente propia. |
| **Corroboración asimétrica** | Bajó a **Bajo** la fila de armamento de **Ahuacatlán** (sin comunicado oficial) y a **Medio** las de **Ajacuba** (desglose 2/8 no fijado en titular) y **Tijuana** (desglose no fijado). |
| ⚠️ **Una reserva de más también es defecto** | **Se comprobó expresamente en Escuinapa**: el borrador iba a marcar reserva y **dos titulares independientes fijan las cifras** —«Ejército asegura **10 armas, mil 900 cartuchos y 20 explosivos** en Escuinapa»—. **No se aplicó reserva y la fila subió a Alto.** **Quinta vez en la serie que el criterio corrige hacia INTEGRAR o REFORZAR.** |
| **Cargadores y cartuchos** | **Nunca se sumaron entre sí.** Los **5 cartuchos útiles + 1 percutido** de Huehuetán tampoco se sumaron. |
| **Un delito y su detención** | **No se desdobló Chilpancingo ni Elota**: en los dos, la agresión y la respuesta son **una sola secuencia continua sin delito consumado aparte** —sin muertos ni heridos de la autoridad—. **El color lo fija quién inició, y por eso ambas son 🔴 en una sola ficha.** La regla de las dos fichas es para el **delito consumado con daño propio** más la detención posterior, que no es el caso. **Arbitraje del coordinador, declarado.** |

---

## 7. Umbrales aplicados, y por qué

**La asimetría entre módulos se aplicó literalmente:**

- **Armamento — confianza `Bajo` SÍ integra**: **Ahuacatlán** entró con **dos fuentes periodísticas
  coincidentes y sin comunicado oficial**, marcada con su nivel. ⚠️ **Y el arbitraje posterior la
  CORRIGIÓ AL ALZA**: apareció el **comunicado n.º 59 de la 13.ª Zona Militar** y **la fila subió a
  Medio**, además de corregir su desglose de 2 a 3 armas largas. **El umbral bajo sirvió para no perder
  la fila; el arbitraje sirvió para mejorarla.**
- **Sentencias — confianza `Bajo` NO basta**: **doce candidatos judiciales quedaron fuera**, entre ellos
  **Asientos (Aguascalientes)**, que tiene **fecha en la ruta, pena exacta al día (7a 7m 21d), multa exacta
  ($14,419) y tres nombres con alias**, y que **solo lo sostienen dos medios regionales sin comunicado de la
  FGR**. ⚠️ **Y una tercera cobertura consigna SEIS sentenciados en Asientos, no tres**:
  `POSIBLE CASO HOMÓNIMO O AGREGACIÓN DISTINTA — NO INTEGRAR HASTA VALIDACIÓN`.

⚠️ **Y el acumulado nacional de años de prisión NO se integra**, marcado
`PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`: el boletín 612/26 **no dice «a cada uno»** y **trata la
multa como cantidad única de la resolución**. **La pena publicada, 19a 6m 20d, sí se integra por fila.**

**Por debajo del umbral «Bajo» —fuente única— quedaron fuera del módulo de armamento**: **Los Amates,
Lázaro Cárdenas** (6 largas, 1,374 cartuchos, 43 cargadores, 1 rifle-granada de 40 mm), **Huehuetán,
Chiapas** (1 corta cal. .44) y **Sonora** («más de 5,400» cartuchos). **Los Amates es el mayor volumen no
integrado del corte** y su exclusión se debe a **un solo medio regional**, no a la fecha.

---

## 8. Disposición expresa de TODO candidato evaluado

| Candidato | Disposición |
|---|---|
| **BAJA CALIFORNIA · Mexicali, col. Bosques del Sol** | ✅ **CERRADO SIN INTEGRARSE.** Sigue siendo fuente única; y su publicación es anterior a esta ventana. **No vuelve a listarse.** |
| **MICHOACÁN · Buenavista Tomatlán, col. El Hospital («El Maguey»)** | ✅ **CERRADO POR TERCERA VEZ.** `ARG-119-FE-001`. |
| **MICHOACÁN · Chinicuila** | ✅ **CERRADO POR VENTANA, tercera vez.** **No vuelve a listarse.** |
| **AGUASCALIENTES · Cosío, com. El Salero** | ⚠️ **SIN AVANCE, `FECHA NO FIJADA` tercera vez.** La URL de la GN sigue sin día en la ruta. **17 largas y 1 rifle cal. .50 siguen siendo el mayor volumen pendiente del archivo.** ⚠️ **El buscador se agotó como vía**: no repetir la búsqueda salvo que se abra el acceso directo. |
| **CHIAPAS · La Trinitaria** | ⚠️ **SIN AVANCE, `FECHA NO FIJADA` QUINTA vez. No se le asignó búsqueda.** ⚠️ **Procede retirarlo por agotamiento en ARGOS 120 si no se fija.** |
| **NAYARIT · Bahía de Banderas** | **SIN CAMBIO, `FECHA NO FIJADA`. No se le asignó búsqueda.** |
| **QUINTANA ROO · Cancún** | **SIN CAMBIO, `FECHA NO FIJADA`. Sureste lo confirmó sin resultado en ventana.** |
| **ZACATECAS · seis personas por secuestro agravado (FGJ)** | ⚠️ **SIN AVANCE, `FECHA NO FIJADA` segunda vez.** El término «fallo condenatorio» está en el *slug* institucional y **basta para clasificar**, pero **el *slug* no porta fecha**. |
| **AGUASCALIENTES · Rincón de Romos** | ✅ **CERRADO, fuera de ventana.** Confirmado de nuevo: la URL fija año y mes, no el día. |
| **TABASCO · Marco «N», boletín 4894** | ✅ **CERRADO: fabricación de fecha acreditada. No vuelve a listarse.** |
| **AGUASCALIENTES · Asientos, com. Pilotos** | ⚠️ **NUEVO, NO INTEGRADO.** `PENDIENTE DE CONFIRMACIÓN OFICIAL` + `POSIBLE CASO HOMÓNIMO` (3 o 6 sentenciados). **Lo cierra el boletín de la FGR.** |
| **SINALOA · Adrián «N» (33a 4m) y Javier «N» (20a 3m 6d)** | ⚠️ **NUEVOS, NO INTEGRADOS.** El primero por republicador único; el segundo por `FECHA NO FIJADA` y ambigüedad de término. |
| **ESTADO DE MÉXICO · Hueypoxtla y Toluca** | ⚠️ **NUEVOS, NO INTEGRADOS.** `PENDIENTE DE CONFIRMACIÓN OFICIAL`: sin boletín primario de la FGJEM. |
| **TABASCO · Comalcalco (5 sentenciados, 50 años) y las tres sentencias de FGET** | ⚠️ **NUEVOS, NO INTEGRADOS.** `FECHA NO FIJADA`. |
| **COLIMA · Villa de Álvarez** · **MICHOACÁN · La Piedad** | ⚠️ **NUEVOS, NO INTEGRADOS.** `FECHA NO FIJADA`. |
| **DURANGO · feminicidio de Gómez Palacio y violación** | ✅ **DESCARTADOS POR VENTANA** (2 y 5-sep), **sin ambigüedad**, gracias al dominio con fecha en la ruta. |
| **MICHOACÁN · Los Amates, tenencia La Mira** | ⚠️ **NUEVO, NO INTEGRADO por FUENTE ÚNICA.** **Mayor volumen no integrado del corte.** **Deslindado de «Los Coyotes, Lázaro Cárdenas» de ARGOS 118.** |
| **CHIAPAS · Huehuetán** · **SONORA · 5,400 cartuchos** | ⚠️ **NUEVOS, NO INTEGRADOS por FUENTE ÚNICA** (y «más de» no es cifra). |
| **GUERRERO · Xaltianguis, «10 explosivos»** | ⚠️ **NUEVO, `POSIBLE DUPLICIDAD — NO INTEGRAR HASTA VALIDACIÓN`** frente a `ARG-118-001`. |
| **PUEBLA · falsa patrulla, carretera Puebla-Orizaba (8-sep)** | ⚠️ **NUEVO, NO INTEGRADO por fuente única.** **Se conserva: acredita continuidad operativa de «Los Zúñiga».** |
| **CHIAPAS · Tuxtla Gutiérrez (7-sep)** · **JALISCO · Lagos de Moreno** · **COLIMA · Tecomán** · **NAYARIT · Santa María del Oro** · **BCS · La Paz y Los Cabos** | ✅ **DESCARTADOS POR VENTANA.** |
| **MORELOS · 31 detenidos** · **NUEVO LEÓN · Sabinas Hidalgo** · **BC · Playas de Rosarito** · **EDOMEX · San Juan Teotihuacán** · **CHIAPAS · Tapachula y San Cristóbal** · **OAXACA · Boletín 2,317** · **TABASCO · José Alberto «N»** · **GUERRERO · Tlapa, Chilapa y Atlixtac** | **SIN CAMBIO. No se les asignó búsqueda**; conservan su disposición anterior. |

---

## 9. Controles editoriales

Ejecutados como subagentes, **autorizados expresamente por el destinatario**, y **`editor-duplicidad`
lanzado DESPUÉS de generar la móvil** para que pudiera auditar la paridad.

| Control | Resultado |
|---|---|
| `barrido-regional` ×6 | **Ejecutados en paralelo antes de ningún otro encargo.** Cobertura 32/32 en los dos cuadres. |
| `procedencia-cifras` | Ver §10. |
| `editor-duplicidad` | Ver §10. |
| **Arbitraje del coordinador** (no es subagente) | **El que más valor produjo, tercera edición consecutiva**: el `grep` de topónimo sobre lo que trajo el recall **evitó un triple conteo de 6 largas, 47 cargadores y 2 AEI**; el deslinde de «La Campana» **evitó fusionar dos municipios**; el rechazo del 🟡 propuesto por Sureste **evitó subestimar un ataque contra autoridades**; y la comprobación de titulares en Escuinapa **evitó una reserva injustificada sobre la fila mejor documentada del corte**. |

### Validación automática ejecutada antes de publicar

```
✔ exactamente un <body>          ✔ node --check del bloque de datos
✔ las doce constantes presentes  ✔ MEXICO_PATHS = 32 entidades
✔ 30 ARG-ID únicos, todos con ancla y region coherente con STATE_REGION
✔ semáforo derivado = portada = radar-stats: rojo 4 · amarillo 3 · verde 12
✔ 3 recuadros · regla de cinco líneas cumplida (contador «<b>N. » CON ESPACIO)
✔ 4 tablas, todas envueltas en table-wrap exactamente una vez
✔ cero -FE- en el cartelón       ✔ sem-item solo en portada
✔ cero medidas en «ediciones»    ✔ pie con número, fecha y hora en las 11 páginas
✔ paridad móvil: 32/32 ARG-ID · 0 map-box vacíos · 0 clases de escritorio · 1 pie
```

⚠️ **El contador de cinco líneas exige `<b>N. ` CON ESPACIO**, para que «7.62×39» no cuente como línea.
⚠️ **El `region:` sigue a `STATE_REGION`, no al reparto de barridos**: se verificó que **Nayarit y
Guanajuato son «Occidente»**, **Zacatecas es «Noreste»** y **Guerrero es «Sureste»**, aunque los barridos los
cubrieran de otro modo.

---

## 10. Qué devolvieron los controles

⚠️ **DECIMOCUARTA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES, Y LOS DOS CONTROLES DEVOLVIERON
`CORREGIR ANTES DE PUBLICAR` CON RAZÓN.** Es la primera vez en la serie que ambos lo devuelven a la vez
con hallazgos materiales.

### 10.1 `procedencia-cifras` — `CORREGIR ANTES DE PUBLICAR`

**Cuatro hallazgos, y los dos primeros son los más caros que ha atrapado el control en toda la serie**:
son **reservas indebidas sobre cifras que las propias fuentes primarias citadas por el borrador SÍ
publicaban**.

| Hallazgo | Arbitraje del coordinador | Efecto |
|---|---|---|
| ⚠️ **ELOTA: el boletín de la SSP de Sinaloa publica el desglose completo y el borrador lo dio por «cantidad no determinada»** | ✅ **ACEPTADO.** El boletín que la propia ficha citaba como fuente primaria dice **«1 rifle Sporter cal. 7.62×39, 1 pistola Glock cal. 9×19, 1 pistola Super cal. .38, 6 cargadores cal. 7.62×39, 1 cargador cal. .38, 1 cargador cal. 9 mm, 447 cartuchos cal. 7.62×39, 9 cal. .38 y 10 cal. 9 mm»**. **La aritmética lo ancla: 447 + 9 + 10 = 466**, el número que el borrador sí tenía | **+2 cortas, +1 larga, +8 cargadores.** Y **convierte a Elota en la ÚNICA FILA DEL CORTE CON CALIBRE PUBLICADO EN TODAS SUS PIEZAS** |
| ⚠️ **LEÓN-SAN FELIPE: el boletín de la FSPE especifica tipo y cargadores, y el borrador los dio por no publicados** | ✅ **ACEPTADO.** El boletín dice **«un arma corta tipo pistola, calibre .380 ACP, dos cargadores y cinco cartuchos útiles»**. **La aritmética lo ancla: 5 + 748 = 753** | **El arma pasa de «sin categoría» a CORTA; +1 corta, −1 sin categoría, +2 cargadores** |
| ⚠️ **AHUACATLÁN: el desglose 1 corta / 2 largas podía ser 1 corta / 3 largas** | ✅ **ACEPTADO tras búsqueda de arbitraje.** El control **no pudo fijarlo** y lo dejó expresamente para el coordinador. **La búsqueda localizó el COMUNICADO DE PRENSA N.º 59 DE LA 13.ª ZONA MILITAR, V REGIÓN MILITAR**, que dice **«además del Barrett, dos armas largas y un arma corta»**: **el Barrett es ADICIONAL** | **+1 larga.** Y **la fila SUBE de Bajo a Medio**: apareció el comunicado oficial que faltaba |
| ⚠️ **SEN-001: el acumulado de 81 años multiplica la pena por cuatro mientras la multa se cuenta una vez** | ✅ **ACEPTADO.** El **boletín 612/26** dice **«sentencia de 19 años, 6 meses y 20 días… en contra de 4 personas»** y **no dice «a cada uno»**; **describe la multa con la misma fórmula y como cantidad única**. **La asimetría no la sostiene el texto** | **El acumulado nacional de años de prisión NO SE INTEGRA**, marcado `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`. **La búsqueda de arbitraje aportó además los cuatro nombres —J. Carmen, Luis, Fausto y Joan «N»— y el número de comunicado**: la identificación pasa de tres campos individualizadores a cinco |
| **ESCUINAPA: «no procede reserva» estaba sobreextendida** | ✅ **ACEPTADO.** Los titulares fijan **10 armas, 1,900 cartuchos y 20 AEI**, **no** los 44 cargadores, 20 chalecos ni 13 placas | **La declaración se acota**: esas tres cifras llevan `SIN FIJAR EN TITULAR` |
| **Citas heredadas sin marcar** | ✅ **ACEPTADO.** El control **verificó en origen** que **31 ÷ 4 = 7,75** es correcto | Marcadas `HEREDADO — VERIFICADO EN ORIGEN` (el 7,75) y `HEREDADO — NO REVERIFICADO` (los 27 AEI de `ARG-103-REC-001`) |
| **EL OCOTITO: las 75 dosis son dos detenciones, no una** | ✅ **ACEPTADO.** **3 detenidos con 55 dosis** y **1 con 20**, publicadas por medios distintos | **La agregación se declara en la ficha** en vez de presentarse como un solo comunicado |

✅ **Y el control confirmó, en la dirección contraria, que NO había reserva de más en Ajacuba**: **«10
armas» sí está en titular** y **el desglose 2/8 no**, exactamente como el borrador lo había marcado.
**El control corre en las dos direcciones y esta vez validó una reserva además de retirar cuatro.**

⚠️ **VERIFICACIÓN ARITMÉTICA: el control recalculó los seis cocientes del borrador y los seis son
correctos.** **No se repitió el «83 ÷ 6 = 7,75» de ARGOS 118.** Los cocientes se recalcularon otra vez
tras las correcciones: **80,4 cartuchos por arma** (4,098 ÷ 51) y **2,61 cargadores por arma larga**
(81 ÷ 31).

### 10.2 `editor-duplicidad` — `CORREGIR ANTES DE PUBLICAR`

⚠️ **CERO DUPLICIDADES REALES**: el control verificó los ocho deslindes del corte —La Campana ×4,
Tamazula, Palos Prietos, Apatzingán, el corredor de Chilpancingo, los dos Veracruz y Xaltianguis— y
**todos son hechos genuinamente distintos**. **Toda la aritmética, la cobertura y la paridad cuadraron**.
Pero devolvió **tres afirmaciones fácticas inexactas**, y las tres son correctas:

| Hallazgo | Arbitraje | Corrección |
|---|---|---|
| ⚠️ **`ARG-119-016` decía «el mismo día en que cerró ARGOS 119 (8-sep 10:38)»** | ✅ **ACEPTADO, y destapa un defecto de método nuevo.** **8-sep 10:38 es el cierre de ARGOS 118**, no de 119. **La causa no fue un error de redacción: fue el `sed` global de ensamblaje `s/ARGOS 118/ARGOS 119/g`**, que alcanzó **cuatro referencias legítimas a la edición anterior** | **Corregidas las cuatro.** Ver `ARG-119-FE-004` |
| ⚠️ **`ARG-119-013` afirmaba que «Corregidora» no aparece en ningún corte anterior** | ✅ **ACEPTADO.** **`ARG-90-ARM-006`** (ARGOS 90, **5-ago**) ya registró un operativo de cinco municipios de Querétaro que **incluye Corregidora** —8 armas sin desglose, 7 detenidos, no integrado—. **No es el mismo hecho**, pero la afirmación era falsa | **Deslinde reescrito**: cita el antecedente y explica por qué es hecho distinto |
| ⚠️ **`ARG-119-018` afirmaba lo mismo de «Benemérito de las Américas»** | ✅ **ACEPTADO.** El topónimo figura en el **acervo de barrido de ARGOS 88-89** —1 corta, 11 largas, 340 cartuchos, y el caso «Selvin «N»»—, **cerrado entonces como `ACERVO NO FECHABLE — NO INTEGRABLE A NINGUNA VENTANA`**. **Ninguna cifra coincide** | **Deslinde reescrito** en los mismos términos |

⚠️⚠️ **Y EL HALLAZGO ESTRUCTURAL, QUE ES EL MÁS VALIOSO DE LOS DOS CONTROLES:
`reports/indice-arg-id.md` EMPIEZA EN `ARG-91-001`.** **Las ediciones 88, 89 y 90 no están indexadas.**
Por eso los dos deslindes fallaron: **no es que el coordinador no hiciera el `grep`, es que el índice no
cubre ese tramo**. **Cualquier afirmación de «no aparece en ningún corte anterior» es, hoy, no
verificable para los topónimos anteriores a ARGOS 91**, y **las dos veces que se hizo en este corte
resultó falsa**. **Se abre como deuda de método: extender el índice hacia atrás hasta la edición más
antigua conservada, o declarar en el propio índice el rango que cubre.**

### 10.3 Efecto acumulado de los dos controles sobre el producto

| Rubro | Borrador | Publicado | Causa |
|---|---|---|---|
| Armas cortas | 16 | **19** | Elota (+2), Guanajuato (+1) |
| Armas largas | 29 | **31** | Elota (+1), Ahuacatlán (+1) |
| Armas sin categoría | 2 | **1** | Guanajuato pasa a corta |
| **Total de armas** | **47** | **51** | |
| Cargadores | 71 | **81** | Elota (+8), Guanajuato (+2) |
| Armas con calibre publicado | 0 | **4** | Elota (3), Guanajuato (1) |
| Años de prisión acumulados | 81a 5m 20d | **NO SE INTEGRA** | `PENA COMPUESTA` |
| Filas con confianza Alto | 2 | **2** | Ahuacatlán sube de Bajo a Medio |

⚠️ **Los controles no retiraron ni una cifra: añadieron cuatro armas y diez cargadores, y retiraron un
acumulado judicial.** **Es la segunda vez en la serie que el saldo neto de los controles es INTEGRAR más
de lo que retiran**, y la primera en que eso ocurre **porque el borrador no había leído del todo las
fuentes primarias que él mismo citaba**. **La lección es que citar un boletín no equivale a haberlo
explotado.**

---

## 11. Nota de comparabilidad

**Serie de duraciones**: 47 h → 25 h → 46 h 30 min → 26 h 22 min → **117 h 50 min**.

**Ninguna edición es comparable con otra sin normalizar por duración.** Este corte es **4,5 veces más largo
que el anterior** y produjo **19 hechos frente a 5**, pero **menos densos**: **0,16 hechos/hora frente a
0,19**. **La serie sigue sin ventanas estables y conviene sostener horas de arranque fijas para que recupere
comparabilidad.**


---

## 12. Deuda de método que esta edición abre y no puede cerrar

⚠️ **`reports/indice-arg-id.md` NO CUBRE LAS EDICIONES 88, 89 Y 90: EMPIEZA EN `ARG-91-001`.**
Lo detectó `editor-duplicidad` al comprobar dos deslindes de este corte, y **los dos resultaron falsos por
esa causa**: «Corregidora» figura en `ARG-90-ARM-006` y «Benemérito de las Américas» en el acervo de
barrido de ARGOS 88-89.

**Consecuencia operativa, que rige desde ahora**: **ninguna ficha puede afirmar «no aparece en ningún
corte anterior del archivo» para un topónimo**, porque el `grep` no alcanza ese tramo. **La fórmula
correcta es «no aparece en el índice, que cubre de ARGOS 91 en adelante»**, o bien el deslinde expreso
contra el antecedente cuando se localice.

**Acción pendiente para ARGOS 120**: **extender el índice hacia atrás hasta la edición más antigua
conservada**, o —si no hay presupuesto— **declarar en la cabecera del propio índice el rango de ediciones
que cubre**, que cuesta una línea y evita que la próxima auditoría repita el mismo punto ciego.
