# ARGOS 121 — Archivo de fuentes y método

**Corte**: 2026-09-17 · **Ventana**: 2026-09-16 11:34 → 2026-09-17 17:36 CDMX (**30 h 02 min**)
**Hora sellada**: verificada con `TZ=America/Mexico_City date` como primer comando de la sesión, antes de
leer nada.

Este archivo recoge lo que **no va al cartelón**: el registro del barrido, la rotación, las fes de
erratas, las limitaciones de herramienta y la deuda de método. El cartelón es para el mando; esto es
para la auditoría.

---

## 1. La base: por decimoquinta vez, la rama llegó desactualizada

El contenedor asignó `claude/argos-121-criminal-analysis-utlcxa` **sin las ediciones 107 a 120**.
`git merge --ff-only origin/claude/argos-2026-cartel-mobile-q87ahx` restituyó el árbol a `7e8a7e4`:
**106 archivos** en `reports/` y **`argos-2026-09-16` (ARGOS 120)** como última edición, exactamente el
estado que el Bloque 0 del arranque exigía encontrar.

**Diferencia con ARGOS 120, y es la que importa**: esta edición **no heredó borrador**. Todo el
contenido se redactó **con el archivo completo ya a la vista**, de modo que **los deslindes nacieron
verificados** en vez de tener que rehacerse. La regla que ARGOS 120 dejó escrita —*un deslinde escrito
sin el archivo completo no es un deslinde verificado*— **no llegó a ponerse a prueba porque no hubo
ocasión de infringirla**.

⚠️ **La causa sigue sin resolverse.** Quince ediciones consecutivas con la misma incidencia no son un
accidente: es el comportamiento estable del entorno. El primer comando de cada sesión debe seguir siendo
la restitución de base.

---

## 2. Rotación de cobertura

**Ciclo aplicado: CICLO B** — **Noreste y Golfo** encabezaron el triaje judicial. Se declara
expresamente, como manda la regla: *una edición que no diga qué ciclo aplicó no aplicó ninguno*.

**Prioridad y ciclo coincidieron**, sin conflicto que arbitrar: las cuatro entidades que ARGOS 120 dejó
`NO REVISADA` en el módulo judicial —**Coahuila, Nuevo León, San Luis Potosí y Zacatecas**— **son todas
del Noreste**, y encabezaron.

**Qué aportó la rotación, dicho sin adornos: nada en sentencias.** El Noreste cerró sus cinco entidades
con **cero sentencias integrables** y el Golfo sus dos igual, pese a gastar en ello sus primeras
consultas. **Es el primer ciclo de los cuatro declarados que no produce una sola resolución.**

**Qué sí aportó, y no es menor**:

- El Noreste destapó que el candidato heredado de **Zacatecas** —seis personas, secuestro agravado—
  probablemente **no es de 2026 sino de 2023**: el boletín tiene *slug* sin fecha y el caso que describe
  coincide con uno que otras fuentes fechan tres años antes. **Sin encabezar judicial, ese candidato
  habría seguido vivo otra edición.**
- El Golfo acreditó que el vacío de Tabasco **no es de triaje sino de indexación**, y sumó una
  **incoherencia de correlativo** nueva del mismo emisor: el folio **37481** recibió del resumidor la
  fecha «24 de abril de 2026», **incompatible con el 37454 ya anclado en ~20-ago-2026**. Un folio
  superior no puede ser anterior. **Se descarta sin usarla.**

**Costo declarado**: **Yucatán quedó `NO REVISADA`** en los dos módulos, y **SSP y FGE de Chiapas** se
cubrieron solo por mención general, sin consulta dirigida a su dominio. **A ARGOS 122 le toca el Ciclo C
(Occidente + Sureste), y por la regla de prioridad sobre el ciclo, Yucatán debe encabezar aunque no le
toque por turno.**

**Deuda saldada**: **Colima, Nayarit, Aguascalientes, Hidalgo y Tlaxcala** —las cinco que ARGOS 120
declaró con cobertura desigual— **recibieron consulta dirigida propia en este corte**.

---

## 3. El recall nacional del coordinador, duodécima edición consecutiva

**Los dos hechos de mayor gravedad del periodo no los vio ningún barrido regional: los trajo el recall
nacional.** Coyuca de Benítez y San Andrés Chicahuaxtla aparecieron en una consulta genérica sin
restricción de dominio, después de que las seis regiones hubieran cerrado sus ejes.

**Doce ediciones seguidas con el mismo resultado dejan de ser una observación y pasan a ser una
propiedad del método**: el barrido por portales encuentra lo que las instituciones publican; el recall
nacional encuentra lo que ocurre. **No es sustituible por más equipos ni por más presupuesto por
región.**

---

## 4. El hallazgo de control del corte: una duplicación completa, evitada por el `grep`

El barrido del **Noroeste** trajo **Nonoava, Chihuahua** como **hecho nuevo del 16-sep**: ataque armado
contra militares en patrullaje, **8 armas de alto calibre, 2,294 cartuchos, 30 cargadores**, camioneta
con identificación clonada de SEDENA y un detenido llamado **Osiel Francisco B. C., de 22 años**.

**El `grep` por topónimo contra `indice-arg-id.md` lo detuvo.** El índice ya tenía
**`ARG-120-002`** y **`ARG-120-ARM-002`**, fechados **14-sep**, con:

| Campo | ARGOS 120 | Lo que trajo el barrido |
|---|---|---|
| Municipio | Nonoava, Chihuahua | Nonoava, Chihuahua |
| Armas | 8 de alto calibre, sin desglose | 8 de gran calibre |
| Cartuchos | 2,294 | 2,294 |
| Cargadores | 30 | 30 |
| Detenido | **Osiel Francisco B. C., 22 años** | **Osiel Francisco B. C., 22 años** |
| Vehículo | Dodge Ram con identificación clonada de SEDENA | Dodge Ram con identificación clonada de SEDENA |
| Contenedor de ametralladora | sí, no integrado | sí |

**Es el mismo hecho, republicado con dos días de diferencia en la fecha atribuida.** De haberse
integrado habría **duplicado 8 armas, 2,294 cartuchos y 30 cargadores** —el mayor volumen de munición
del periodo— en un corte cuyo total real de cartuchos es `CANTIDAD NO DETERMINADA`.

**El barrido no podía verlo: no tiene el índice a la vista. El coordinador sí. Por eso el `grep` por
topónimo es del coordinador y es permanente.**

---

## 5. El boletín federal que ARGOS 120 declaró inexistente, apareció

ARGOS 120 verificó **en las tres formas** que exige la regla de la triple consulta —día suelto, rango y
título sin restricción de dominio— que **no existía indexado** ningún boletín del Gabinete de Seguridad
que cubriera el **14, 15 o 16 de septiembre**. **Esa verificación era correcta y el vacío era real en su
momento.**

**El boletín «acciones relevantes del 14, 15 y 16 de septiembre de 2026» apareció dentro de esta
ventana**, vía republicadores —SICOM Noticias, Certeza Diario, Talla Política, Consulta Monterrey—,
**ninguno con fecha en la ruta**. `gob.mx/sspc` no lo indexa con fecha en el *slug*.
⚠️ **Varios republicadores del mismo boletín no son fuentes independientes: la corroboración de todo lo
que procede de él es débil por construcción, y así se declara ficha por ficha.**

**Consecuencia de ventana, que es la parte delicada**: el boletín **cubre tres días que pertenecen casi
enteros a la ventana de ARGOS 120** (13-sep 08:28 → 16-sep 11:34). **Solo las últimas seis horas del
16-sep caen en la ventana de ARGOS 121**, y **el emisor no desglosa qué renglón corresponde a qué día**,
menos aún a qué hora. **Un boletín de rango no se reparte por días.**

Por eso **ningún renglón del boletín se integró a los totales de ARGOS 121**. Los que tienen valor de
inteligencia se publicaron como **recuperaciones `-REC-` con ventana de origen declarada**:

| ARG-ID | Renglón | Tratamiento |
|---|---|---|
| `ARG-121-REC-003` | Mazatlán, Sinaloa: **53 AEI** en dos contenedores abandonados, SEDENA, **martes 15-sep** | **Fecha fijada por cobertura independiente** —Línea Directa, Los Noticieristas, Meganoticias, Sinaloa Hoy, Extraoficial, Quadratín—, que es lo que permite sacarlo del rango |
| `ARG-121-REC-004` | Coyame del Sotol, Chihuahua: **2 largas, 22 cargadores, 3,358 cartuchos, 1 detenido** | `FECHA NO FIJADA DENTRO DEL RANGO`. **Ninguna cobertura independiente lo fecha** |

**Renglones del boletín NO publicados**, por ser menores o sin cifra de armamento, y que **ARGOS 122 no
debe recontar**: **Comondú, BCS** (1 detenido, 145 kg de cocaína, 1 tractocamión) · **Nayarit** (7
detenidos incl. 3 menores, 10 largas, 530 cartuchos, 2 vehículos — paquete **Acaponeta**, con cifras
contradichas: otra cobertura da «6 armas y 2 mil balas») · **Del Nayar, Nayarit** (9 AEI) · **La Yesca**
(+24,000 plantas) · **Benito Juárez, QRoo** (8 kg de marihuana) · **Sayula de Alemán, Veracruz** (22 t
de maíz) · **Huimanguillo, Tabasco** (cigarros apócrifos y tractocamión — **ya cubierto por
`ARG-120-015`**) · **Mexicali, BC** (1 detenido por amenazas a autoridades).

---

## 6. Fe de erratas — el boletín federal corrige DOS filas de ARGOS 120, al alza

⚠️ **No van al cartelón**, conforme a la regla. Van aquí y a `_pendientes.md`, y sus ARG-ID quedan
registrados en el índice.

### `ARG-121-FE-001` — Tapachula, Chiapas (corrige `ARG-120-016` y `ARG-120-ARM-004`)

ARGOS 120 integró, con **fuente única regional y sin desglose institucional**: *5 armas largas —3
escopetas y 2 fusiles—, 201 cartuchos, 1 detenido (Julio «N»), cargadores no publicados*.

El boletín federal del 14-16-sep publica **el mismo hecho con el desglose completo**: en **Tapachula**,
GN, Ejército, SEMAR, Fiscal y Policía Estatal catearon un inmueble donde detuvieron a **una persona** y
aseguraron **cinco armas largas, dos cargadores, 248 cartuchos, DOS GRANADAS, cuatro silenciadores,
cuatro miras telescópicas**, dosis de droga, 10 cámaras de vigilancia, 250 piezas de diábolo y un GPS.

**Corrección**: **+47 cartuchos** (248 frente a 201) · **+2 cargadores** (de «no publicados» a 2) ·
**+2 granadas** (de 0 a 2) · silenciadores y miras en rubro aparte.
**Efecto sobre ARGOS 120**: sus totales pasarían de **9,194 a 9,241 cartuchos**, de **178 a 180
cargadores** y de **1 a 3 granadas**. **La confianza de la fila sube de Bajo a Medio**: ahora tiene
fuente institucional.
⚠️ **Es un caso de la trampa «citar un boletín no equivale a haberlo explotado», en su variante
temporal: el boletín no existía cuando ARGOS 120 cerró. No es un fallo de aquella edición.**

### `ARG-121-FE-002` — Ensenada, Baja California (corrige `ARG-120-019`)

ARGOS 120 integró: *FESC detiene a seis personas, incluido un menor de 17 años, tras persecución apoyada
con dron*, con **`ARMAMENTO NO ESPECIFICADO: no alimenta el conteo y NO SE INFIERE`**.

El boletín federal publica el desglose: en **Ensenada**, Ejército y Policía Estatal detuvieron a **seis
personas, incluido un menor**, y aseguraron **dos armas largas, un arma corta, tres cargadores, 91
cartuchos, dos chalecos tácticos y dos vehículos**.

**Corrección**: **+2 armas largas** · **+1 arma corta** · **+3 cargadores** · **+91 cartuchos**.
**ARGOS 120 hizo lo correcto al no inferir**; el dato simplemente no estaba publicado todavía.

### `ARG-121-FE-003` — El Rosario, Sinaloa: la cifra de CERO detenidos queda CONFIRMADA

El pendiente heredado decía que `ARG-120-010` integró **0 detenidos** por cifra mayoritaria y que **una
cobertura aislada consignaba 9**. **Queda resuelto, y la resolución es que ARGOS 120 acertó.**

Los **«9 detenidos» pertenecen a OTRO evento**: un aseguramiento distinto y anterior en **Agua Verde,
El Rosario**, publicado el **~3-sep**, con **nueve fusiles automáticos, 54 cargadores, 2,620 cartuchos y
cinco kilos de marihuana**, y **nueve detenidos —cuatro colombianos, una cubana, dos mujeres—**. Todas
las coberturas del hallazgo de los cinco tambos lo describen como **arsenal enterrado, sin persona
presente ni detención asociada**.

⚠️ **Si una edición futura integrara «9 detenidos» a `ARG-120-010`, estaría fusionando dos eventos por
coincidencia de municipio: exactamente lo que la regla de deslinde prohíbe.** **Pendiente CERRADO.**

---

## 7. Pendientes cerrados y marcos corregidos

| Pendiente heredado | Resolución |
|---|---|
| **Boletín federal del 14, 15 y 16-sep** | **APARECIÓ.** Ver sección 5 |
| **El Rosario — detenidos de `ARG-120-010`** | **CERRADO: 0 es correcto.** Ver `ARG-121-FE-003` |
| **Tecámac — objetivo real del ataque** | **CERRADO.** La **FGJEM descarta expresamente el ataque contra la alcaldesa Rosi Wong**; el objetivo era **Carlos Galindo**, con **19 impactos** en el vehículo. ⚠️ **Precisión de cargo**: ARGOS 120 lo consignó como «jefe de gabinete»; las coberturas del 16 y 17-sep lo describen como **regidor y coordinador de asesores**. **Se anota, no se corrige el hecho** |
| **«La Noria de San Antonio» — 84 AEI** | **MARCO CORREGIDO, no cerrado.** La contradicción **NO es de fecha**: el hecho es **único y del 8-sep-2026** (Operación Sable, SEMAR, 1 detenido, 2 largas, 334 cartuchos, 18 cargadores). **La contradicción es de MUNICIPIO**: San Ignacio frente a Mazatlán. **Corresponde a la ventana de ARGOS 118-119, no a la 120.** Sigue `POSIBLE DUPLICIDAD` en su campo de municipio |
| **Chiapas · La Trinitaria** (2 largas, 920 cartuchos, 34 cargadores) | **RETIRADO POR AGOTAMIENTO. Quinto intento sin fijar fecha.** Ni URL ni titular la portan en ninguna vía. `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO` |
| **Guerrero · Vidal «N», Eduardo Neri** | **SIN AVANCE.** Sigue no localizado. **Ninguna autoridad ha planteado la hipótesis de privación conjunta y este corte tampoco la plantea** |
| **Guerrero · Xaltianguis — Said Sánchez Sandoval** | **SIN AVANCE en situación jurídica ni carpeta.** Puesto a disposición de un juez de control; **el resultado de la audiencia no está publicado**. **La cifra de «24 detenidos acumulados» sigue sostenida por una sola fuente regional y NO SE ADOPTA**, igual que en ARGOS 120 |
| **Guanajuato · San Francisco del Rincón — heridos** | **SIN ARBITRAR. 5 frente a 6**, con medios de peso a ambos lados. **No existe parte médico indexado.** ⚠️ **Hallazgo nuevo: la «serie de ataques a canchas» SÍ está documentada** con hechos distintos y fechados —Salamanca 25-ene-2026 (10 muertos), Irapuato-ejido Malvas 19-ago-2026 (4 muertos)—, **pero ninguna autoridad la declara serie**. La cifra de prensa «16 asesinados viendo futbol este año» **no tiene respaldo oficial y no se adopta** |
| **Tabasco · las seis ejecuciones del 15-sep** | **SIN ARBITRAR.** La FGET no publicó desglose por municipio y hora |
| **Nayarit · Bahía de Banderas** | **Localidad precisada: Mezcales.** ⚠️ **Cifra de cartuchos en conflicto**: el archivo registra **26**; esta edición encuentra **~44** (11 + 14 en cargadores + 19 sueltos). **Ninguna es cita literal.** `SEGUNDA EDICIÓN EN CONFLICTO` |
| **Aguascalientes · Cosío, El Salero** (17 largas, una cal. .50) | **TERCER INTENTO SIN FIJAR FECHA.** El boletín de GN existe con *slug* sin fecha. **Sigue siendo el mayor volumen pendiente del archivo** |

---

## 8. El encargo perecedero: Ciudad Juárez

**La audiencia de individualización de la pena de José Manuel E. C. estaba fijada, con cadena literal
del boletín del 14-sep, para «el próximo jueves 17 de septiembre a las 09:00 horas»** ante el Tribunal de
Juicio Oral del Distrito Judicial Bravos, tras el **«fallo condenatorio»** ya dictado por homicidio
calificado y tentativa (hecho del 1-sep-2025).

**Tres búsquedas dedicadas no localizaron publicación indexada de su resultado**, pese a haber
transcurrido **8 h 36 min** entre la hora fijada y el cierre de la ventana.

⚠️ **No se afirma que la audiencia se pospusiera: eso sería un hecho no acreditado.** Lo que se declara
es que **su resultado no está publicado indexado al cierre**. **Sigue como candidato vivo para ARGOS
122, y es el más maduro del archivo**: el término jurídico ya es expreso y solo falta la pena.

---

## 9. Limitación de herramienta — reverificada, y el techo no sube

ARGOS 120 declaró como incidencia nueva que **el bloqueo de egreso alcanzaba también a los medios**, no
solo a `*.gob.mx`, y ordenó comprobarlo de nuevo. **Comprobado, y persiste**:

| Dominio | Vía | Resultado |
|---|---|---|
| `www.gob.mx/sspc` | `curl` | `000` |
| `fiscaliachihuahua.gob.mx` | `curl` | `000` |
| `www.infobae.com` | `curl` y `WebFetch` | `000` · `EGRESS_BLOCKED` |
| `www.elfinanciero.com.mx` | `curl` y `WebFetch` | `000` · `EGRESS_BLOCKED` |
| `www.milenio.com` | `curl` | `000` |
| `sicomnoticias.mx` | `WebFetch` | `EGRESS_BLOCKED` |

**Ninguna página de este corte se leyó íntegra.** Todo lo publicado se sostiene en los extractos del
buscador más la fecha en la ruta de las URL.

⚠️ **Por eso el techo de confianza de esta edición es ★★★☆☆ y no el ★★★★☆ habitual — segunda edición
consecutiva.** **No es una degradación del criterio: es una degradación de la herramienta.**
`docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**, y es la única solución real.

**Excepción declarada**: `ARG-121-003` (Querétaro) lleva **★★★★☆** porque **tiene boletín oficial con
fecha en la ruta**, aunque tampoco se pudiera leer íntegro. **Es la única fila del corte con fuente
primaria institucional.**

---

## 10. Cifras del corte y su procedencia

**Todos los totales son cálculo propio de ARGOS**: ninguna autoridad publicó un agregado nacional del
corte. Comprobaciones aritméticas sobre las filas integradas:

⚠️ **ESTAS CIFRAS SON LAS RECALCULADAS DESPUÉS DE LOS CONTROLES**, no las del borrador: la corrección
de Morelia (sección 11) retiró un evento entero de los totales.

| Total | Desglose | Cuadre |
|---|---|---|
| **2 armas cortas** | 2 (Querétaro) | ✔ |
| **2 armas largas** | 2 (Querétaro) | ✔ |
| **0 sin categoría** | las cuatro armas están clasificadas | ✔ |
| **Cartuchos** | `CANTIDAD NO DETERMINADA`: «diversos» (Querétaro), sin cifra | ✔ |
| **0 cargadores** | la FGE de Querétaro no los publicó, pese a desglosar las armas | ✔ |
| **6 detenidos** | 6 (Querétaro) | ✔ |
| **1 entidad, 1 evento** | **un solo emisor sostiene el conteo nacional del corte** | ✔ |
| **Densidad 0,10 h/hora** | 3 ÷ 30,033 = 0,0999, frente a 19 ÷ 75,10 = 0,25 | ✔ |
| **Duración 30 h 02 min** | 16-sep 11:34 → 17-sep 17:36 | ✔ |
| **1,679 cartuchos/arma** | 3,358 ÷ 2 (Coyame, **no integra**) | ✔ |
| **1,238,880 pesos** | 247,776 × 5 (Temoaya, **no integra**) | ✔ |

⚠️ **La duración y la densidad se recalcularon al sellar la hora real**, no se heredaron de ningún
borrador — no hubo borrador del que heredarlas.

⚠️ **Cifras que NO se integraron y por qué**: los **7 policías de Coyuca** y los **6 de Tepeaca**, por no
haber aseguramiento de armamento en sus eventos —van a detenciones relevantes, no al módulo—; los **18
detenidos** de los cateos derivados de Michoacán, **sin desglose por inmueble**; los **cartuchos de
ambos eventos integrados**, por aproximados; los **2 rifles de municiones** de Querétaro, por **no ser
arma de fuego**.

⚠️ **Campo que sigue en retroceso**: **una de cinco armas con calibre publicado** —el fusil .223 de
Angamacutiro— y **cero con número de serie**. ARGOS 120 midió **19 de 92 sin categoría y cero series**.
**Seguir midiéndolo corte a corte.**

---

## 11. Controles ejecutados

| Control | Estado |
|---|---|
| `barrido-regional` ×6 | **Ejecutado en paralelo, en un solo mensaje**, con la deuda al frente y tope de 2-3 búsquedas por eje. **113 búsquedas en total** |
| Recall nacional del coordinador | **Ejecutado antes de cerrar los barridos.** Aportó los dos hechos de mayor gravedad |
| `grep` por topónimo contra el índice | **Ejecutado sobre cada topónimo antes de fichar.** Detuvo la duplicación de Nonoava |
| Comprobación de coherencia con `node:vm` | **`validación OK`**: 32 entidades en `MEXICO_PATHS`, cada `region:` coincide con `STATE_REGION`, ninguna fecha fuera de ventana, cero ARG-ID duplicados, cada ARG-ID con ancla, semáforo derivado = portada = `radar-stats`, un solo `<body>`, 5 tablas y 5 envoltorios `table-wrap`, cero `-FE-`, `sem-item` solo en portada, ningún bloque de más de cinco líneas, **3 recuadros** y pie en las **9 páginas** |
| `gen-movil.py` | **`validación OK`** · contadores 🔴 0 🟡 0 🟢 4 · **9 tarjetas móvil / 9 escritorio** |
| `gen-texto.py` | Ejecutado. ⚠️ **Se corrigió la HERRAMIENTA, no su salida**: el generador fijaba «Corte matutino» y este corte es **vespertino**. Ahora **deriva el turno del pie del cartelón** |
| `editor-duplicidad` | **Ejecutado como subagente**, después de generar la móvil. **Devolvió `CORREGIR ANTES DE PUBLICAR`** |
| `procedencia-cifras` | **Ejecutado como subagente**. **Devolvió `CORREGIR ANTES DE PUBLICAR`, con un error de hecho** |

⚠️ **ARGOS 120 declaró sin atenuar que no había pasado los dos últimos controles. ARGOS 121 los pasó
ambos, y los dos devolvieron hallazgos reales.** **Esta sección existe para que se vea qué habría llegado
al mando si no se hubieran ejecutado.**

### 11.1 El hallazgo más grave: un error de hecho, no de procedencia

⚠️⚠️ **`procedencia-cifras` detectó que la captura de «El Señor de la T» NO ocurrió donde ni cuando el
borrador decía.** El borrador la situaba **en Angamacutiro el jueves 17-sep**, siguiendo al barrido de
Occidente. **La detención fue en MORELIA, Boulevard Juan Pablo II, el MARTES 15-SEP.**

**Cómo se produjo el error, que es lo que importa**: las **once coberturas llevan `2026/09/17` en la
ruta**, y el barrido tomó esa fecha como la del hecho. **El cuerpo de las notas dice que la detención fue
el 15 y que el 17 es el día en que se anunció.** Angamacutiro y Puruándiro **no son el lugar de la
captura: son la zona de operación del detenido y el sitio de los 28 cateos posteriores**.

**Es exactamente la regla que `CLAUDE.md` enuncia —*la fecha de la URL fija la publicación, no el
hecho*— y el barrido cayó en ella pese a tenerla escrita en su encargo.** El coordinador **verificó el
hallazgo con fuente propia antes de aceptarlo**, y se confirmó.

**Consecuencias, todas aplicadas**:

- El hecho pasa a **`ARG-121-REC-005`**, **recuperación de la ventana de ARGOS 120**, **fuera de todos
  los totales**.
- **Los totales nacionales se recalcularon**: de **3 a 2 armas largas**, de **4 a 0 cargadores**, de
  **7 a 6 detenidos**, de **2 a 1 entidad**.
- **La densidad cae de 0,13 a 0,10 hechos por hora** (3 ÷ 30,033).
- **La única arma del periodo con calibre publicado —el fusil .223— deja de ser del corte**: las cuatro
  armas integradas quedan **sin calibre y sin serie**.
- **Se ganó dato de inteligencia que el borrador no tenía**: el detenido es **Manuel Alejandro Rendón
  Aguilar, 51 años**, la corporación **sí está identificada** —SSPC, SEDENA, SEMAR, FGR y FGE
  Michoacán—, circulaba en **camioneta con reporte de robo**, y **las investigaciones lo vinculan con el
  homicidio del síndico de Penjamillo, Roberto Ramírez Zárate (2025), y con la desaparición de la
  expresidenta municipal de Angamacutiro, Maribel Juárez Blanquet**.
- **Deslindes nuevos y obligatorios**: **Morelia figura tres veces en el índice** —`ARG-106-REC-002`,
  `ARG-120-018` y `ARG-120-ARM-008`—, y **el síndico de Penjamillo no es el síndico de
  `ARG-116-REC-001`** (David Guadalupe Ramírez González, Tepuche, Culiacán), **pese al apellido
  coincidente**.

### 11.2 Los demás hallazgos, uno por uno

| Control | Hallazgo | Corrección |
|---|---|---|
| `procedencia-cifras` | **«Seis días» entre el 13 y el 17-sep** | **Son cuatro.** Corregido |
| `procedencia-cifras` | ⚠️ **La cifra «14,787 armas» no pudo localizarse en ninguna búsqueda**, ni siquiera como publicación real | **Se declara así en el cartelón.** No es una cifra «contradicha»: es **una cifra cuya existencia no se pudo verificar**, y esa brecha es más grave |
| `procedencia-cifras` | **Chicahuaxtla**: unas coberturas dicen **«ambos graves»**, otras que **el profesor está estable** | **Contradicción declarada y no arbitrada**; se publican **las dos versiones** |
| `procedencia-cifras` | **Los indicadores del Gabinete** podrían ser del informe de gobierno de principios de septiembre | **Reserva de fecha declarada**; se citan **como contexto, no como indicador del corte** |
| `procedencia-cifras` | **Coyame del Sotol acumula varios operativos con cifras parecidas** | Anotado para blindar deslindes futuros |
| `procedencia-cifras` | **Tepeaca**: existe una cifra agregada de **58,600 litros** (3 pipas + 2 camiones de San Salvador El Verde) | **48,600 es la correcta para el hecho publicado.** La agregada se declara **para que no se lea después como contradicción** |
| `procedencia-cifras` | **«Los Jockes» tiene una tercera sentencia**: 70 años, 6-ago-2026, secuestro de una madre y su hija en Toluca | Registrado para futuros deslindes sobre Altamirano Moreno |
| `procedencia-cifras` | **«Mario Arturo Castillo Ramos»**: el segundo apellido no aparece en los fragmentos recuperables | **Confirmación parcial declarada.** No es motivo de retiro |
| `editor-duplicidad` | ⚠️ **El generador MÓVIL fijaba «Corte: Matutino», igual que el de texto** | **Se corrigió LA HERRAMIENTA, no su salida.** ⚠️ **El mismo defecto estaba en los dos generadores y solo se vio al compararlos entre sí** |
| `editor-duplicidad` | **El cuadre judicial decía «4 candidatos» y la tabla tenía 5 filas** | **Recalculado a `0 + 5 + 26 + 1 = 32`**, y **se declara el criterio en el cartelón**: el cuadre es **por entidad, no por caso** |
| `editor-duplicidad` | **Zacatecas lleva TRES apariciones, no dos**: desapareció **sin cierre documentado** en ARGOS 120 | **Retirado por agotamiento en este corte, no aplazado.** El umbral se había cumplido en ARGOS 119 |
| `editor-duplicidad` | **Existe `ARG-119-013`** (Querétaro/Corregidora, 8 cateos, 9 detenidos, 11-sep), tercer episodio de «Sinergia» | **No requería cita**, pero queda anotado: **el operativo acumula tres episodios y el deslinde es permanente** |
| `editor-duplicidad` | **Confirmó que Nonoava no entró** en ninguna de las tres versiones, que **las 16 apariciones de «DESLINDE» usan la fórmula correcta** del rango del índice, y que **no hay duplicidad interna ni ARGOS hablando de ARGOS** | Sin cambios |

**Qué se lleva de aquí ARGOS 122**: **los dos controles se ganaron su coste en una sola edición.** Uno
detectó **un error de hecho que habría inflado los totales nacionales con un evento de la ventana
anterior**; el otro, **un defecto de herramienta que afectaba a los dos generadores a la vez**. **Ninguno
de los dos era visible desde el cartelón.**

En consecuencia, **toda cifra de ARGOS 120 citada en esta edición va marcada
`HEREDADO — NO REVERIFICADO`**, salvo las tres corregidas por fe de erratas en la sección 6, que sí se
reverificaron.

---

## 12. Fuentes

**Institucionales**: **FGE de Querétaro** —comunicado propio con fecha en la ruta, **única fuente
primaria institucional del corte**— · Gabinete de Seguridad federal —boletín del 14, 15 y 16-sep, **vía
republicadores**— · FGE Guerrero (por cita) · FGE Oaxaca (por cita) · FGJEM (por cita) · SSP Puebla y
SEMAR (por cita) · SEDENA, GN y Policía Estatal de Chihuahua (por cita, vía boletín federal) · FGE de
Baja California (`fgebc.gob.mx/boletines/12722`) · FGJ Zacatecas (*slug* sin fecha).

**Nacionales**: Infobae · La Razón · El Heraldo de México · N+ · Aristegui Noticias · SDP Noticias ·
La Silla Rota · El Imparcial · El Sol de México (OEM-Informex) · Récord · El Informador · Quadratín
México · El Universal · Milenio · Latinus · La Prensa de Coahuila · Noroeste.

**Regionales**: Meganoticias · Azteca Guerrero · La Plaza Diario de Acapulco · Tribuna de México ·
Diario de Confianza · Análisis.mx · El Imparcial de Oaxaca · Grupo Animal · Viva la Noticia · Guardia
Nocturna · La Región Tula · DigitalMex · NX Noticias · Comunicación XXI · Argón México · Reporteros en
Movimiento · Código QRO · Críptica · Tepeaca Noticias · Diario Cambio · La Jornada de Oriente · La
Opción · Quadratín Michoacán · Línea Directa · Los Noticieristas · Sinaloa Hoy · Extraoficial · Café
Negro Portal · La Gaceta Chihuahua · Al Instante Chihuahua · Juárez Noticias · Zeta Tijuana · Diario
Tijuana · En Línea BC · Nayarit Noticias · NTV · Crítica DN · AM Periódico · Cadena Láser · La Nigua.

⚠️ **Republicadores usados como vía y NO como fuente independiente**: SICOM Noticias · Certeza Diario ·
Talla Política · Consulta Monterrey. **Varios republicadores del mismo boletín no son fuentes
independientes**: la corroboración de `ARG-121-REC-003` y `ARG-121-REC-004` es **débil por
construcción**, y así se declara en sus fichas.

---

## 13. Vacíos de publicación que el mando debe conocer

- **`fiscaliaguerrero.gob.mx`**: **cuarta edición consecutiva sin publicar indexable**. El barrido
  precisó el diagnóstico: **el portal existe y está indexado**, pero **sus boletines recientes no lo
  están** —los resultados más nuevos son de marzo a julio de 2026—. **No es que no publique: es que el
  buscador no lo alcanza**, el mismo patrón que ARGOS 104 documentó para el boletín federal. Guerrero
  aporta **los dos hechos rojos del periodo sin una sola fuente institucional propia**.
- **`fgjem.edomex.gob.mx`**: **sin boletín indexado** para la sentencia de 125 años de Temoaya, ni para
  Coacalco, ni para Hueypoxtla. **Tres resoluciones de la misma fiscalía que ninguna edición ha podido
  integrar por falta de su propio boletín.** Es **el vacío judicial más costoso del archivo reciente**.
- **SSC y FGJ de la Ciudad de México**: **cero boletín** sobre el doble homicidio de Tepito del 16-sep,
  **segunda edición consecutiva**. ⚠️ **Y una contradicción de edades sin arbitrar**: «25 y 30 años»
  frente a «18 y 19». ⚠️ **Se descartó expresamente una cifra de «4 detenidos» con nombres**, atribuida
  al caso por un *liveblog* y **no corroborada en segunda consulta**: **no se integra**.
- **`gabinetedeseguridad.gob.mx/resultados/`**: **undécima verificación consecutiva sin cifra
  utilizable**. Dominio indexado, rutas sin fecha, acceso directo bloqueado.
- **`fgeqroo.gob.mx`**, que fue la mejor fuente del corte anterior: **sin comunicado del 16 ni del
  17-sep**. **Sin actualización sobre la situación jurídica de los 5 detenidos de `ARG-120-013`.**

---

## 14. Lo que esta edición deja dicho sobre sí misma

**Una ventana de 30 horas no mide violencia: mide publicación.** El corte cierra con **cero eventos
rojos dentro de ventana** y **cuatro recuperaciones**, dos de ellas rojas. **Los hechos graves del
periodo ocurrieron; lo que no había ocurrido todavía, cuando ARGOS 120 cerró, era su publicación.**

Es exactamente el fenómeno inverso al que documentó el arranque —*una ventana larga no produce
recuperaciones: las absorbe*—. **Queda la regla simétrica: una ventana corta no produce hechos propios,
produce recuperaciones. Ni la una ni la otra es indicador de cobertura.**


---

## 15. Reestructuración editorial de esta edición

**Instrucción directa del destinatario, recibida tras la primera entrega del corte**: *«Quita la
corroboración y explotación ARGOS. Recuerda, es un reporte para mandos. Hay que reducir los textos y no
repetir las noticias en los diferentes secciones.»*

**Aplicada, y consagrada en `CLAUDE.md`** como **«Regla de las dos secciones por nota»**, que **deroga
la de las cuatro**. Las ediciones siguientes la heredan del repositorio, no de esta conversación.

### Qué se retiró

- **El apartado «Corroboración»** como bloque narrativo, en las **9 fichas**.
- **El apartado «Explotación ARGOS»** ficha por ficha, también en las 9 — **45 líneas de análisis
  repartidas** que ahora se concentran en **10**: cinco en la Valoración y cinco en las Conclusiones.
- **La tabla «Distribución del corte»** de la última página y **la tabla jurídica de una sola fila**,
  que **repetían** lo que ya estaba en la ficha.
- **El total nacional de armamento** dejó de imprimirse dos veces: vive en la página de panorama y el
  módulo **remite** a ella.
- **Los titulares del recuadro de portada**: era la **tercera** aparición de cada hecho.

### Qué NO se retiró, y por qué

⚠️ **Las fuentes, los deslindes y las marcas de reserva se conservaron íntegras en cuanto a contenido**,
trasladadas al bloque de **Trazabilidad**. **Son dato, no prosa**, y `CLAUDE.md` prohíbe recortarlos:
sin ellos el producto deja de ser auditable, que es la razón de ser de ARGOS.

**Lo que sí se comprimió es su forma**: las listas de emisores pasaron de enumerar los catorce nombres a
dar el **recuento por tipo** con los **fechados en la ruta nombrados**. **La lista íntegra sigue
publicada en la sección 12 de este archivo**, que es donde se audita.

### Qué cambió la portada

El recuadro dejó de ser **«LO QUE DEBE SABER EL MANDO»** —un resumen de titulares— y pasó a ser
**«LO QUE DEBE HACER EL MANDO»**: cinco líneas de **acción accionable** —auditar los retenes municipales
de la costa de Guerrero, cotejo balístico contra el armamento de cargo, vigilar el nivel municipal como
unidad de riesgo, exigir calibre y serie en los boletines, cotejar los dos depósitos de AEI de
Mazatlán—. **Un mando que ya vio el panorama y la ficha no necesita el titular una tercera vez.**

### Resultado medido

| Medida | Antes | Después | Reducción |
|---|---|---|---|
| **Palabras del cuerpo del cartelón** | 9,708 | **6,435** | **33 %** |
| **Palabras de la versión en texto** | 9,565 | **6,482** | **32 %** |
| **Líneas de la versión en texto** | 812 | **543** | **33 %** |
| **Apartados por ficha** | 4 | **2** | — |
| **Apariciones máximas de un hecho** | 3 | **2** | — |
| **Páginas** | 9 | **9** | sin cambio |
| **Cifras, fechas, fuentes o deslindes perdidos** | — | **0** | — |

**Las nueve páginas se mantienen porque ninguna tarjeta se comprimió**: lo que se recortó fue prosa, y
el espacio liberado se repartió en vez de apretar el contenido. **La validación con `node:vm` incorpora
dos comprobaciones nuevas**: que **no exista ningún apartado «Corroboración» ni «Explotación ARGOS»**, y
que **cada ficha tenga exactamente dos apartados, uno de ellos «Trazabilidad»**.
