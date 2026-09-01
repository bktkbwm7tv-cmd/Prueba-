# ARGOS 113 — Archivo de fuentes y trazabilidad

**Corte**: 2026-09-01 · **Hora de cierre**: 13:17 CDMX (verificada con `TZ=America/Mexico_City date`, no supuesta)
**Ventana**: **2026-08-31 09:28 → 2026-09-01 13:17 CDMX** (27 h 49 min). Continuación estricta de ARGOS 112, sin hueco ni solape.

Este archivo contiene lo que **no** va al cartelón: hallazgos de método, fes de erratas, cobertura del
instrumento, rendimiento de la rotación y candidatos descartados. El cartelón es para el mando; esto
es para la auditoría.

---

## 0. Verificación de base (Bloque 0 del arranque)

| Comprobación | Esperado | Encontrado |
|---|---|---|
| Última edición en `reports/` | `argos-2026-08-31` (ARGOS 112) | ✅ `argos-2026-08-31` |
| Archivos en `reports/` | 81 | ✅ 81 |
| `main` contiene ARGOS 112 | Sí | ✅ `8415816 Generar ARGOS 112 (corte 2026-08-31)` |
| `git merge --ff-only origin/main` | Primer comando de la sesión | ✅ ejecutado antes de leer `CLAUDE.md` |

⚠️ **La rama asignada volvió a llegar desactualizada, por séptima edición consecutiva.** Al arrancar,
`claude/argos-113-daily-generation-lhkzuj` mostraba **`argos-2026-08-24` (ARGOS 106)** como última
edición —**siete ediciones por detrás**— y **no contenía su propio archivo de arranque**
`_arranque-ARGOS-113.md`. Numerar por lo que la rama tenía a la vista habría producido **un falso
«ARGOS 107» con ventana solapada de una semana**. **El `merge --ff-only` lo resolvió y la numeración
salió del archivo, no de la rama.** El modo de fallo es estable, la contramedida también, y **el
estado encontrado coincidió exactamente con el que el arranque anunciaba**: 81 archivos y
`argos-2026-08-31` como última edición.

---

## 1. Estado del egreso — vigesimoquinta edición

**Verificado en esta sesión, no heredado.**

```
curl https://gabinetedeseguridad.gob.mx/resultados/   → sin respuesta (código 000, túnel denegado)
WebFetch sobre dominios *.gob.mx y de medios          → EGRESS_BLOCKED
```

**Cero portales leídos por acceso directo.** Toda consulta institucional fue por buscador, con
**sustitución anotada** en cada ficha que la usó. **Techo de confianza del producto: ★★★★☆**;
ninguna ficha lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.

**Consecuencia sobre las casillas de cobertura**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable**
—exige lectura directa del listado de boletines— y por eso figura en **0** en todos los módulos. La
casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.

---

## 2. La obligación de calendario que vencía en esta edición

**`gabinetedeseguridad.gob.mx/resultados/` era exigible desde el 1 de septiembre de 2026, primer día
de esta ventana. Se consultó y su ausencia se declara como VACÍO DEL CORTE, no como limitación
heredada.**

Lo que sí quedó acreditado, con fuentes nacionales múltiples: **desde el 1 de septiembre los reportes
diarios preliminares de homicidio doloso y robo de vehículo dejaron de publicarse en el portal de la
SSPC y pasaron en exclusiva a ese sitio**, para las 32 entidades, conservando fuentes, metodología y
criterios de integración.

Lo que **no** se alcanzó: **ningún reporte diario del 1 de septiembre**. El dominio **sí está
parcialmente indexado** —devuelve rutas del tipo `gabinetedeseguridad.gob.mx/contenido/NNNN`—, de
modo que la vía de buscador existe pese al bloqueo, **pero ninguna de esas rutas lleva fecha y el
dominio tiene una trampa de año documentada**: en ARGOS 112 devolvió un boletín de **octubre de 2025**
a una consulta de agosto de 2026. **Ninguna cifra del dominio se usa en esta edición.**

**Estado del pendiente**: se transforma. Deja de ser «obligación de calendario pendiente» y pasa a ser
**«vacío recurrente por verificar cada corte»**: el emisor migró, el portal existe y está indexado, y
lo que falta es que sus reportes diarios sean alcanzables por buscador.

---

## 3. Rotación de cobertura — **CICLO C**, declarado y aplicado

**A ARGOS 113 le tocaba el Ciclo C: Occidente + Sureste encabezan el triaje judicial**; Noroeste,
Noreste, Centro y Golfo encabezan con armamento. **Se aplicó y se declara aquí, como exige la
metodología.** No quedaba ninguna entidad `NO REVISADA`, así que **el ciclo se aplicó limpio**, sin
prioridad de saldo.

**Qué aportó el Ciclo C que el orden anterior no habría aportado** — y esta vez el rendimiento es
**negativo en sentencias y positivo en otra cosa**:

| Región | Aporte atribuible al encabezamiento judicial |
|---|---|
| **Occidente** | **Ninguna sentencia integrable**, pero el vacío judicial quedó **acreditado en tres búsquedas**, lo que liberó presupuesto para el eje de Aguascalientes — y ahí apareció el valor real: **la identidad y la edad del detenido de Villa García**, que resuelven una contradicción abierta desde ARGOS 112, y **la recuperación del abatimiento de Los Reyes**, no fichado por ninguna edición |
| **Sureste** | **Ninguna sentencia integrable**, y el valor **no está en lo que encontró sino en lo que impidió arrastrar**: descartó con **fecha propia verificada** tres sentencias reales de Guerrero (15-may, 8-jul, 25-mar) y una de Oaxaca que, por aparecer en boletines recientes, un triaje sin chequeo de fecha podría haber presentado como del corte |

⚠️ **Se rompe la racha de tres cortes en que la región que encabeza judicial produce la única
sentencia del corte.** La única sentencia integrable de ARGOS 113 salió de **Puebla (Centro)**, región
que encabezaba con armamento. **Pero no es un fallo de la rotación**: la causa está en la duración de
la ventana, no en el orden de búsqueda —ver §7—.

**A ARGOS 114 le toca el Ciclo A — Noroeste + Centro** encabezando el triaje judicial.

---

## 4. La deuda de cobertura más antigua, asignada por primera vez a regiones concretas

**Sexta edición consecutiva sin tocarse; en esta se asignó explícitamente en vez de dejarse al
remanente —que nunca existe—, y produjo resultado.**

| Asignación | Región | Resultado |
|---|---|---|
| **SEDENA / SEMAR / FGR / ANAM regionales** | **Noreste** (por ser la frontera y por el caso de las 210 armas) | ✅ **NO VACÍO.** Produjo el hallazgo de **Matamoros** —Ejército / IV Región Militar, 31-ago, 4 armas largas, 38 cargadores, 130 cartuchos, 1 granada, 6 placas balísticas—, que **es uno de los dos únicos aseguramientos del corte**. **ANAM / aduanas de Nuevo Laredo, Piedras Negras y Reynosa**: `SIN RESULTADO INDEXADO EN VENTANA` |
| **Mesas de Construcción de la Paz** | **Centro** | ⚠️ **Parcial.** Se identificó **una sola mesa con portal propio y desglose numérico publicable**: la de **Morelos** (`morelos.gob.mx/ultimas-noticias`), que publica detenidos, armas largas y cortas, granadas y vehículos. **Ninguno de sus boletines cae dentro de la ventana.** En Puebla, Edomex, Hidalgo, Querétaro y CDMX **no se localizó portal dedicado** |

**Conclusión de método**: **la asignación explícita funciona y debe mantenerse.** Seis ediciones
dejándola al remanente produjeron cero; una edición asignándola produjo un hallazgo integrado al
conteo y un dominio útil nuevo. **A ARGOS 114**: asignar SEDENA/SEMAR/FGR/ANAM a **Noroeste** (SEMAR
en Sinaloa y BC, zonas militares de Chihuahua) y las **Mesas** a **Occidente**.

---

## 5. Reparto de presupuesto — el objetivo de `site:` se bajó y aun así se quedó corto

**Objetivo revisado en este corte: ~60-65 % genérica · ~15 % `site:` · ~10 % judicial.**

| Región | Búsquedas | `site:` | Desviación contra el 15 % |
|---|---|---|---|
| Noroeste | 19 | 1 (5,3 %) | −9,7 pp |
| Noreste | 14 | 1 (7,1 %) | −7,9 pp |
| Occidente | 14 | 1 (7,1 %) | −7,9 pp |
| Centro | 6 | 1 (16,7 %) | +1,7 pp |
| Golfo | 7 | 0 (0 %) | −15,0 pp |
| Sureste | 15 | 2 (13,3 %) | −1,7 pp |
| **Coordinador (recall nacional)** | **8** | **0 (0 %)** | −15,0 pp |

⚠️ **Bajar el objetivo del 25 % al 15 % redujo la magnitud de la desviación pero no su dirección:
cinco de las seis regiones siguen por debajo, y dos de ellas muy por debajo.** El diagnóstico se
sostiene y se refina: **el `site:` no rinde de forma uniforme, rinde donde el dominio tiene fecha en
la ruta**. Las dos regiones que se acercaron al objetivo (Centro 16,7 %, Sureste 13,3 %) son
precisamente las que tenían dominios con fecha en la ruta que consultar —`fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`
y `boletines.guanajuato.gob.mx/AAAA/MM/DD/`—.

**Propuesta para ARGOS 114**: **dejar de fijar el objetivo como porcentaje global y fijarlo como
regla**: *`site:` solo contra dominios con fecha en la ruta; contra los demás, consulta genérica*.
Un porcentaje global obliga a gastar `site:` en dominios donde se sabe de antemano que devolverá
*home pages*. **Es la tercera edición consecutiva declarando la misma desviación en la misma
dirección: el problema es el indicador, no la ejecución.**

---

## 6. El recall nacional del coordinador — cuarta edición consecutiva como paso de mayor rendimiento

**Ejecutado antes de cerrar ningún barrido, como exige el método.**

| Origen del hecho | ARGOS 110 | ARGOS 111 | ARGOS 112 | **ARGOS 113** |
|---|---|---|---|---|
| Barridos regionales | 2 de 4 | 4 de 6 | 3 de 7 | **4 de 6** |
| **Recall nacional del coordinador** | 2 de 4 | 2 de 6 | **4 de 7** | **2 de 6, incluido el hecho principal** |

**Qué trajo el recall que ningún barrido trajo**:

1. **La detención de Piedra Gorda (`ARG-113-001`), hecho principal del corte** — y, sobre todo, **la
   identificación correcta de por qué hecho se practicó**. Ver §8.
2. **El abatimiento de Los Reyes, Michoacán** (`ARG-113-REC-001`), localizado por consulta nacional
   por tema. Occidente lo confirmó después de forma independiente.
3. **La consolidación del saldo de Ojocaliente en 11 lesionados y ~40 viviendas**, que es una
   rectificación institucional posterior al cierre de ARGOS 112.
4. **La obligación de calendario del Gabinete de Seguridad**, resuelta como vacío acreditado (§2).
5. **El arbitraje entre barridos** (§8) y **el arbitraje sobre el control de cifras** (§15.3), que
   **integró el primer artefacto explosivo asegurado de la serie** y cambió el conteo nacional del
   corte.

**La razón estructural sigue siendo la misma y conviene repetirla**: un hecho nacional de gran
cobertura se busca mejor **por tema** que **por entidad**, y los barridos están organizados **por
entidad**. **El recall cubre un ángulo que el barrido no puede cubrir por construcción.**

---

## 7. Hallazgo de método de esta edición: el ciclo judicial no depende del orden, depende de la ventana

**Es el hallazgo de método más útil del corte y conviene fijarlo antes de que produzca una conclusión
falsa sobre la rotación.**

- ARGOS 112 (ventana de **48 h**, dos días de fin de semana): **1 sentencia integrable**, de la región
  que encabezaba judicial.
- ARGOS 113 (ventana de **27 h**, dos días **hábiles**): **1 sentencia integrable**, de una región que
  **no** encabezaba judicial, y **cero de las 32 fiscalías estatales**.

**El corte anterior explicó su cero judicial estatal por el calendario. Este no puede**: su ventana es
la tarde de un lunes y la mañana de un martes, ambos hábiles, y el resultado estatal es igualmente
cero. **Las fiscalías estatales sí publicaron durante el barrido** —se localizaron sentencias reales
con fecha en la ruta de Guerrero (tres), Querétaro (cinco boletines de agosto), Oaxaca, Durango y
Tabasco—, **pero ninguna dentro de la ventana**.

**Conclusión**: **el ciclo de publicación de las fiscalías estatales es más lento que una ventana de
27 horas.** El triaje judicial **no sirve para garantizar hallazgo; sirve para que el `SIN DATO` sea
demostrable**, que es una función distinta y sigue siendo necesaria. **No debe interpretarse el cero
como fallo de la rotación ni retirarse el ciclo por ello.**

**Corolario para la lectura de la serie**: **los totales de esta edición no son comparables sin
normalizar por duración de ventana.** 27 h frente a 48 h explica por sí sola buena parte de la caída
de volumen (5 armas largas frente a 228). Se declaró en el cartelón como advertencia de
comparabilidad y como conclusión 10.

---

## 8. ⚠️ EL ARBITRAJE QUE SALVÓ LA EDICIÓN: dos detenciones que dos equipos fusionaron en una

**Es el fallo evitado más importante del corte, y no lo detectó ningún control: lo detectó el
coordinador al contrastar dos barridos entre sí.**

- El **barrido del Noreste** informó que la captura de **Piedra Gorda, Cuauhtémoc (Zacatecas)** era la
  de **William Ariel «N», 18 años**, por el ataque de **Villa García**, y la presentó como
  «actualización de identidad de `ARG-112-003`».
- El **barrido de Occidente** informó, de forma independiente, que **William Ariel «N» fue capturado
  el 30-ago en Asientos, Aguascalientes**.
- El **recall del coordinador** tenía fuentes explícitas de que la captura de Piedra Gorda era **por el
  ataque de la Comandancia de Ojocaliente**, el **1-sep**, y **con identidad no revelada**.

**Las tres versiones no podían ser ciertas a la vez.** Una búsqueda de arbitraje lo resolvió: **son
dos detenciones distintas**.

| | Detención A | Detención B |
|---|---|---|
| **Persona** | William Ariel «N», **18 años**, de Aguascalientes | **identidad no publicada** |
| **Fecha** | **30-ago** | **1-sep** |
| **Lugar** | **Asientos, Aguascalientes** | **Piedra Gorda, Cuauhtémoc, Zacatecas** |
| **Por qué hecho** | ataque de **Villa García** (29-ago) | ataque de la **Comandancia de Ojocaliente** (30-ago) |
| **Autoridad** | operativo conjunto Zacatecas–Aguascalientes | **SSP Zacatecas**, secretario **Arturo Medina Mayoral** |
| **ARG-ID** | `ARG-112-003`, ya publicado | **`ARG-113-001`, nuevo** |

**De haberse aceptado la versión del Noreste, ARGOS 113 no habría tenido hecho principal**: la única
detención del corte se habría publicado como actualización de un hecho ya fichado, y **la primera
detención por el ataque contra una instalación fija de mando habría desaparecido del registro**.

**Modo de fallo nuevo, y hay que anotarlo**: **dos barridos regionales pueden converger en un error
compartido cuando el hecho cruza la frontera entre sus regiones.** Villa García está en el límite
Zacatecas–Aguascalientes; el Noreste vio la detención zacatecana y le puso la identidad
aguascalentense, y Occidente vio la aguascalentense sin saber que había una segunda. **La regla que se
deriva: cuando dos regiones informen del mismo nombre propio, el coordinador arbitra con búsqueda
propia antes de integrar, aunque las dos versiones parezcan compatibles.**

---

## 9. Fes de erratas — **ninguna publicada en el cartelón**

Los `-FE-` se registran en `indice-arg-id.md` y aquí. **Cero en el cartelón, verificado por control
automático.**

| ARG-ID | Contenido |
|---|---|
| `ARG-113-FE-001` | **Sobre `ARG-112-001` (Ojocaliente): el saldo se consolidó al alza por tercera vez.** ARGOS 112 publicó **7 lesionados** (Secretaría General de Gobierno, 30-ago) y **10** (fiscal general Cristian Paul Camacho, 31-ago), sin arbitrar. El **1-sep** la autoridad estatal consolidó **11 lesionados, tres aún hospitalizados y estables**, y añadió un campo que ARGOS 112 no tenía: **alrededor de 40 viviendas afectadas** —frente a los 11 vehículos y 2 patrullas ya publicados—. **Aplicación de la regla de rectificación en cadena**: aceptada la rectificación del mecanismo y del saldo, se revisaron los demás campos del hecho y apareció el de daños a vivienda. **La cifra de 11 no se integra a ningún total de ARGOS 113** —el hecho es de la ventana anterior— y solo figura como referencia de contexto en la ficha de la detención. NO PUBLICADA EN EL CARTELÓN |
| `ARG-113-FE-002` | **Sobre `ARG-112-003` (detenido de Villa García): la contradicción de edad queda resuelta a favor de 18 años.** ARGOS 112 registró la edad **contradicha (22-23 frente a 18)** y sin identidad publicada. Se acreditan: **nombre** (William Ariel «N»), **edad 18**, **lugar y fecha de captura** (Asientos, Aguascalientes, **30-ago**, no el 29 del ataque) y **un dato nuevo de peso**: contaba con **boletín de búsqueda de la Fiscalía de Aguascalientes desde el 10 de junio**, es decir **estaba reportado como no localizado antes del ataque**. Se reconoció como sicario del CJNG en su identificación ministerial: **dicho del detenido, no acreditación institucional**. **Situación jurídica: sigue sin publicarse vinculación a proceso.** NO PUBLICADA EN EL CARTELÓN |
| `ARG-113-FE-003` | **Sobre el candidato de Bocoyna, Chihuahua, que ARGOS 112 dejó como `NO REVISADO A FONDO` y señaló como candidato prioritario: NO ES UN HECHO NUEVO.** Es la **continuación informativa del mismo hallazgo de Maguarichi** ya contabilizado en ARGOS 112. Bocoyna y Maguarichi son **colindantes en la misma sierra**, y el despliegue del **26-30 de agosto** incluye **expresamente a Maguarichi** entre sus puntos (San Juanito, El Puerto de los Núñez, **Maguarichi**, Las Agujas, Ataros). Las cifras coinciden: **6,322 frente a 6,324 piezas de alto explosivo** —diferencia de dos unidades entre redacciones— y **1.1 toneladas de agente a granel en ambos**. **Ninguna cifra se retira y ninguna se añade**: el candidato se cierra sin efecto sobre ningún total. NO PUBLICADA EN EL CARTELÓN |
| `ARG-113-FE-004` | **Sobre la deuda de las placas balísticas: cambia de naturaleza y se retira de la lista de búsqueda.** Con las **6 de Matamoros** son **31 placas en tres semanas** (cálculo propio) y **de ninguna se ha publicado marca, nivel NIJ ni lote**. Se preguntó en **las seis regiones en tres cortes consecutivos** con resultado idéntico. **Deja de ser línea de búsqueda —no se le asignan más consultas— y pasa a conclusión permanente del producto**, publicada como tal en el cartelón. NO PUBLICADA EN EL CARTELÓN |
| `ARG-113-FE-005` | **Sobre `ARG-110-001` (Tabasco, Zacatecas, 27-ago): la contradicción de lesionados sigue sin arbitrarse, y con un desplazamiento nuevo.** El barrido del Noreste encontró que **la mayoría de la cobertura de esta ronda sostiene «dos policías de la FRIZ heridos, leves»** y que **la cifra de 5 atribuida al fiscal Camacho no reapareció**. **No se arbitra**: la no reaparición de una cifra no la desmiente. `CONTRADICHA — NO SE ARBITRA SIN FUENTE DIRECTA`, cuarta edición. NO PUBLICADA EN EL CARTELÓN |
| `ARG-113-FE-006` | **Sobre `ARG-112-005` (sur de Sinaloa): la `RESERVA DE TOPÓNIMO` no se cierra.** Se confirma la **localidad** «Agua Verde» para la primera de las cuatro intervenciones, pero **ninguna fuente indexada publica el municipio administrativo**. El cotejo contra `ARG-102-REC-001` (Agua Verde, El Rosario) y `ARG-106-004` (Palo Blanco, Mazatlán/La Noria) **queda abierto**. Gasto: **una búsqueda**, conforme al tope. NO PUBLICADA EN EL CARTELÓN |

---

## 10. Los siete ejes del arranque — qué devolvió cada uno

| # | Eje | Tope | Gastado | Resultado |
|---|---|---|---|---|
| **1** | **ZACATECAS — la serie** | 3 | 3 | ⚠️ **Las tres preguntas contestadas.** **Peritaje comparado**: `SIN RESULTADO INDEXADO EN VENTANA`. **Carpeta única**: `SIN RESULTADO`, **y con indicio en contra** — la FGJEZ mantiene **carpetas abiertas en siete municipios** por agresiones a policías. **¿Cuarto ataque EN LA VENTANA?** **NO**: dos búsquedas dedicadas devuelven solo los tres hechos conocidos y sus derivaciones. ⚠️ **Pero sí un cuarto ataque DEL AÑO que no estaba en el registro**: la autoridad documenta **cuatro ataques con explosivos contra policías en 2026** —Villa García, Tabasco, **Luis Moya** y Ojocaliente—, y **Luis Moya no figuraba en el archivo de ARGOS**. Lo detectó `procedencia-cifras` al auditar la lista de municipios |
| **2** | **Villa García — iniciación remota** | 2 | 2 | **Explotación técnica del accionador**: `SIN AVANCE`, ninguna fuente indexada la publica. **Situación jurídica del detenido**: **sin vinculación a proceso publicada**. **Pero la edad contradicha queda resuelta (18) y aparece un dato nuevo de peso**: boletín de búsqueda desde el 10-jun. Ver `ARG-113-FE-002` |
| **3** | **CHIHUAHUA — Bocoyna** | 2 | 2 | ✅ **CERRADO.** Es el mismo hallazgo de Maguarichi, no un evento nuevo. Ver `ARG-113-FE-003`. **El candidato prioritario heredado queda resuelto y no se reabre** |
| **4** | **`gabinetedeseguridad.gob.mx/resultados/`** | — | 2 | ✅ **Migración acreditada, reporte diario no alcanzable. Se declara vacío del corte.** Ver §2. **Trampa de año evitada**: ninguna cifra del dominio se usa |
| **5** | **Ciclo C + deuda regional** | — | — | ✅ **Aplicado limpio y declarado** (§3). **La deuda SEDENA/SEMAR/FGR/ANAM y Mesas se asignó a regiones concretas por primera vez y produjo resultado** (§4) |
| **6** | **Placas balísticas** | 1 | 1 | ⚠️ **Vacío confirmado por tercera vez, y el corte aportó 6 placas más.** **Se retira de la lista de búsqueda y queda como conclusión permanente.** Ver `ARG-113-FE-004` |
| **7** | **Sinaloa — municipio de Agua Verde** | 1 | 1 | `SIN AVANCE`. **La reserva de topónimo no se cierra.** Ver `ARG-113-FE-006` |

**Tope duro de 2-3 búsquedas por eje: respetado en los siete.** Ningún eje excedió su asignación.

---

## 11. Candidatos no integrados — y por qué

Los siete que llegaron al cartelón (página 4) más los cerrados en el barrido:

| Candidato | Motivo |
|---|---|
| **Chihuahua · Bocoyna** | `POSIBLE DUPLICIDAD — RESUELTA: ES EL MISMO HALLAZGO`. Ver `ARG-113-FE-003` |
| **Tamaulipas · Matamoros, arsenal con Barrett .50** | `FUERA DE VENTANA`. Hecho del **24-25 de junio de 2026**. Mismo municipio y misma región militar que el hallazgo del 31-ago: el buscador los devuelve juntos. **Deslindado expresamente** |
| **Durango o Sinaloa · «16 detenidos y 22 armas»** | `ENTIDAD NO DETERMINADA`. La misma cifra aparece atribuida a **operativos en Durango** y a **operativos en 20 municipios de Sinaloa**, ambas fechadas el 31-ago. **Una cifra sin entidad no es integrable** |
| **Coahuila · «Modelo de Seguridad Coahuila»** | `AGREGADO SIN FECHA DE HECHO`. 215 armas, 788 kg de droga, 512 cateos, 289 detenidos «a través del 30 de agosto», sin desglose por evento ni periodo definido |
| **Tabasco · «operativos coordinados, 26 detenidos»** | `FECHA NO FIJADA`. Comunicado del portal estatal **sin fecha en la ruta ni en el titular**, armamento sin desglose |
| **Puebla · San Martín Texmelucan, detención con arma** | `FECHA NO FIJADA`. Boletín de la SSP estatal con *slug* sin fecha en la ruta |
| **Nacional · reporte diario del Gabinete de Seguridad** | `SIN RESULTADO INDEXADO EN VENTANA — VACÍO DEL CORTE` (§2) |
| **Baja California · desaparición de Emilio Valdez Mainero, Tijuana** | `NO REVISADO A FONDO`. Publicación con fecha en la ruta del **1-sep**, dentro de ventana, pero **solo se localizó el titular**. **Candidato prioritario de ARGOS 114** |
| **Guanajuato · San Miguel de Allende, Victoria y Dolores Hidalgo** | `FUERA DE VENTANA`. **Nueva fuente reconfirma el 25-ago** como fecha del hecho. **El candidato se cierra**: la disputa de fecha queda resuelta a favor de la republicación tardía |
| **Nayarit · Acaponeta y Huajicori** | `FECHA NO FIJADA`, sin cambios. **Se acredita además que no se funde** con el agregado federal 17-29 ago (27 detenidos, 17 largas, 31 AEI): **las cifras no coinciden** |
| **Chiapas · ataque armado en Pueblo Nuevo Solistahuacán, 2 muertos** | `FUERA DE VENTANA`. Publicación del **30-ago**; hecho del 29 o 30, ambos anteriores a la apertura |
| **Colima · «Los Mezcales», 3 detenidos** | Sin cifra de armamento. **Deslindado** de `ARG-104-005` («El Pirul», Colima) y `ARG-105-003` («El Abulón», Oaxaca) |
| **Veracruz/Tabasco · 1,822 kg de mariguana y 81-87 kg de metanfetamina, carretera Coatzacoalcos–Villahermosa** | `FECHA DEL HECHO NO FIJADA` y **discrepancia de cifra** entre versiones (81 vs 87 kg de metanfetamina). Aparece en un **balance de fin de semana** que agrega hechos del 29 al 31 de agosto. **No se reparte un agregado en una ventana de 27 horas** |
| **San Luis Potosí · narcolaboratorio en Santa María del Río** | Localizado en un **liveblog** del 31-ago. `LIVEBLOG — NO FECHA EL HECHO Y NO BASTA COMO FUENTE ÚNICA` |
| **Querétaro · caso atribuido por el resumidor al boletín 08/04** | **Falso positivo del resumidor documentado**: el titular real de esa URL es «concluye proceso penal por hecho de tránsito en Los Arcos», con **acuerdos reparatorios**, no condena. El resumidor **inventó nombre, alias y terminología**. **No se integra** |

---

## 12. Cobertura verificada — 32 de 32 entidades

**Seis agentes `barrido-regional` en paralelo, lanzados en un solo mensaje antes de ningún otro
encargo, como exige `CLAUDE.md`.**

| Región | Entidades | Con hallazgo en ventana | `SIN RESULTADO INDEXADO` | Vacío acreditado | `NO REVISADA` |
|---|---|---|---|---|---|
| Noroeste | 6 | 2 (Chihuahua, Baja California) | 4 | 0 | 0 |
| Noreste | 5 | 3 (Zacatecas, Nuevo León, Tamaulipas) | 2 | 0 | 0 |
| Occidente | 6 | 1 (Guanajuato) | 5 | 0 | 0 |
| Centro | 7 | 1 (Puebla) | 5 | 1 (Tlaxcala) | 0 |
| Golfo | 2 | 0 | 2 | 0 | 0 |
| Sureste | 6 | 1 (Chiapas) | 5 | 0 | 0 |
| **TOTAL** | **32** | **8** | **23** | **1** | **0** |

**8 + 23 + 1 + 0 = 32.** `SIN ACTUALIZACIÓN CONSTATADA` en **0**, por no ser utilizable bajo bloqueo
de egreso.

**Notas de portal**:
- `ssypc.nayarit.gob.mx` — `PORTAL NO DISPONIBLE — índice sin boletines localizables`. **Ninguna cifra
  suya se usa.** Gasto: cero búsquedas, por instrucción.
- **Tlaxcala** — vacío acreditado del emisor, confirmado en dos cortes. **No se gastó búsqueda.**
- **FGE Veracruz** — vacío acreditado del emisor. **No se gastó búsqueda.** La vía útil sigue siendo
  la FGR.
- **`seguridad.slp.gob.mx`** — vive y tiene fecha en la ruta; el boletín más reciente indexado es del
  **18-ago**, fuera de ventana.

---

## 13. Trampas verificadas en este corte

| Trampa | Dónde apareció | Cómo se resolvió |
|---|---|---|
| ⚠️ **Fusión de dos hechos por dos regiones distintas** | Las dos detenciones de la serie de Zacatecas | **Arbitraje del coordinador con búsqueda propia.** Ver §8. **Modo de fallo nuevo** |
| ⚠️ **Rectificación en cadena de la autoridad** | Saldo de Ojocaliente: 7 → 10 → **11**, más un campo nuevo (**~40 viviendas**) | Se revisaron los demás campos del hecho tras aceptar la rectificación. Ver `ARG-113-FE-001` |
| **Trampa de fecha por municipio repetido** | Matamoros: arsenal de **junio de 2026** frente al hallazgo del **31-ago**, mismo municipio y misma región militar | Deslinde expreso en ficha y en tabla de candidatos. **Es la razón de que armamento especial esté en 0** |
| **Topónimo repetido** | «Cuauhtémoc» (municipio de Zacatecas **y** alcaldía de CDMX), «Los Reyes» (Michoacán **y** Los Reyes La Paz, Edomex), «Matamoros» (Tamaulipas **y** Coahuila) | `grep` de topónimo **de localidad** sobre `indice-arg-id.md` antes de fichar. Devolvió `ARG-102-002` y `ARG-98-005` para Los Reyes: **deslinde publicado** |
| **Día de la semana contra calendario** | «el sábado» para Villa García, «la noche del domingo» para Ojocaliente, «madrugada del lunes» para Los Reyes | **Verificado**: 29-ago = sábado, 30-ago = domingo, 31-ago = lunes, 1-sep = martes. **Las tres atribuciones son coherentes**, y la de Los Reyes es la que sitúa el hecho fuera de ventana |
| **Trampa de año en dominio oficial** | `gabinetedeseguridad.gob.mx` | **Ninguna cifra del dominio se usa** (§2) |
| ***Liveblog*** | Coberturas «EN VIVO … hoy 31 de agosto» y «hoy 1 de septiembre» de Infobae | **Ningún hecho se fecha con ellas.** El narcolaboratorio de Santa María del Río se descartó por descansar solo en una |
| **Falso positivo del resumidor** | Querétaro, boletín 08/04 | Contrastado contra el titular real: el resumidor **inventó** nombre, alias y terminología jurídica |
| **Cifra no exacta** | «alrededor de 40 viviendas», «más de un millón de pesos en embutidos» | **No se redondean ni se integran como cifra** |
| **Pena compuesta** | Sentencia de Puebla: «50 años … para ambos» | `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`. **Años acumulados: no determinado** |
| **Corroboración débil por construcción** | Matamoros (medios sobre la misma base del Gabinete), Pénjamo (republicador único), Arriaga (republicador único), Bocoyna (redacción casi idéntica) | **Declarada en las cuatro fichas** |
| **AEI empleado ≠ AEI asegurado** | Los tres artefactos de la serie de Zacatecas | **Fuera del conteo de armamento.** La tarjeta de AEI está en 0 y lo explica |

---

## 14. Deuda de método que ARGOS 113 deja abierta

1. ⚠️ **El objetivo porcentual de `site:` no funciona como indicador** — tercera edición consecutiva
   con desviación en la misma dirección, ya bajado de 25 % a 15 %. **Propuesta concreta: sustituirlo
   por una regla de aplicación** (`site:` solo contra dominios con fecha en la ruta). Ver §5.
2. ⚠️ **Modo de fallo nuevo: dos barridos regionales pueden converger en un error compartido cuando el
   hecho cruza la frontera entre sus regiones.** **Regla derivada: cuando dos regiones informen del
   mismo nombre propio, el coordinador arbitra con búsqueda propia antes de integrar.** Ver §8.
3. **El ciclo judicial no depende del orden sino de la duración de la ventana** (§7). **No retirar el
   ciclo por un resultado negativo**: su función es hacer demostrable el `SIN DATO`.
4. **La asignación explícita de la deuda regional funciona** (§4) y debe continuarse en rotación.
5. **Ninguna sentencia estatal en dos cortes consecutivos; las dos integrables las produjo la FGR.**
   Conviene **dirigir el triaje judicial a las delegaciones de la FGR antes que a las fiscalías
   estatales**, que es lo que ya rompió cinco cortes de agregados en Veracruz.

---

## 15. Los dos controles editoriales — octava edición consecutiva con hallazgos reales

**Ambos devolvieron `CORREGIR ANTES DE PUBLICAR`. Los dos tenían razón, y uno de ellos cambió el
conteo del corte.**

### 15.1 `editor-duplicidad`

| Hallazgo | Corrección aplicada |
|---|---|
| ⚠️ **La tabla de cobertura declaraba 8 entidades «con hallazgo» y tres no se sostenían.** **Chihuahua** contaba como hallazgo lo que el propio cartelón declaraba duplicidad en otra página; **Nuevo León** no tenía ficha ni ARG-ID —su único respaldo era una mención a un hecho de la ventana anterior—; **Baja California** no aparecía en ninguna parte del cartelón, solo como candidato `NO REVISADO A FONDO` en este archivo | **Reclasificada la tabla entera.** Ahora: **5 con hecho integrado** (las cinco con ficha y ARG-ID) · **4 con publicación no integrable** (Chihuahua, Nuevo León, Michoacán y Baja California, cada una con su motivo) · **22 sin resultado indexado** · **1 vacío acreditado**. **Suma 32 y la composición es verificable renglón por renglón.** Es el mismo modo de fallo que el «falso vacío», en sentido inverso: **falso hallazgo** |
| ⚠️ **El contenido de `ARG-113-FE-002` —marcada `NO PUBLICADA EN EL CARTELÓN`— se había filtrado a la Conclusión 4**, con datos individualizadores de una persona (edad, fecha de su boletín de búsqueda) **sin ficha, sin fuente y sin aparato de corroboración**, sobre un hecho de la ventana anterior | **Reescrita la Conclusión 4.** Conserva el **patrón de captación juvenil**, que es inteligencia criminal legítima, y **retira los datos individualizadores**, declarando que proceden de fichas de otra ventana y quedan en el registro de trazabilidad. **Publicar una fe de erratas por la puerta de las conclusiones es publicarla igual** |
| **Repetición de párrafo entre la portada y las Conclusiones 1 y 2**, y entre el recuadro de «cero rojos» y la Valoración | **Recortadas.** Las Conclusiones 1 y 2 **remiten** a la portada y conservan solo su línea accionable; la Valoración **remite** y se limita a lo suyo: por qué la ausencia de evento rojo **no equivale a reducción de amenaza**. **La regla de no duplicación alcanza a los párrafos** |
| **Reserva sobre «8,2 cargadores por arma larga»**: mezcla un depósito fronterizo con una portación individual rural | **Retirada la razón agregada.** Se publican **las dos razones por evento** —9,5 en Matamoros, 3 en Pénjamo— con la advertencia de que promediarlas no describe ninguno de los dos casos |
| Verificados **sin hallazgo**: los cuatro deslindes del borrador (Piedra Gorda/Asientos, Los Reyes, Matamoros/junio, Bocoyna/Maguarichi), los totales de armamento, las 31 placas, la coherencia entre el indicador judicial y la tabla de 32 entidades, y que **la recuperación no figura en `EVENTOS`** | — |

### 15.2 `procedencia-cifras` — y el arbitraje que cambió el conteo

| Hallazgo | Corrección aplicada |
|---|---|
| ⚠️ **PÉNJAMO: el calibre y la identidad SÍ estaban publicados, y el borrador decía que no.** El **boletín oficial de la Secretaría de Seguridad de Guanajuato**, con **fecha en la ruta** (`boletines.guanajuato.gob.mx/2026/08/31/`), y el medio regional ya citado en la propia ficha publican **arma larga cal. 7.62×39 mm**, **50 cartuchos del mismo calibre** y **Luis Daniel «N», de 27 años** | **Integrados los tres datos** en la ficha, la tabla y el conteo. **No es un detalle**: el 7.62×39 es **el calibre que concentra los aseguramientos recientes del Pacífico y del corredor**, y el mismo del que en el corte anterior aparecieron **37 cartuchos en Acapulco sin arma correspondiente**. **El vacío «sin calibre» era del borrador, no de la fuente** |
| ⚠️ **«Nueve municipios con carpeta abierta» era una SÍNTESIS PROPIA sin declarar** — y sostenía tres conclusiones. Lo citable son **dos listas distintas de dos emisores distintos**: **siete municipios** con carpetas por **agresiones a elementos policiacos en carreteras y caminos de terracería** (Valparaíso, Fresnillo, Villanueva, Jerez, Ojocaliente, Luis Moya, Villa Hidalgo), y por separado **cuatro ataques con explosivos contra policías en 2026** (Villa García, Tabasco, Luis Moya y Ojocaliente). **Ninguna fuente dice «nueve» ni junta ambas listas** | **Reescrito el recuadro y las Conclusiones 1 y 2.** Se publican **las dos listas por separado, con su emisor y su categoría**, y la unión se marca `SÍNTESIS PROPIA DE ARGOS`. ⚠️ **Y la corrección mejoró el hallazgo**: la segunda lista acredita que **los ataques con explosivos contra policías en 2026 son CUATRO, no tres** — el cuarto, **Luis Moya**, **no estaba en el registro de ARGOS y no tiene fecha publicada**. **Luis Moya y Ojocaliente aparecen en las dos listas** |
| ⚠️ **Las cifras de contexto de Zacatecas no eran dos sino cuatro, y dos de ellas sí se contradicen.** El borrador publicó **17 en dos años** y **10 en 2026** afirmando que «no se contradicen» —cierto entre ellas—, pero la ventana también indexa **7 ataques contra policías en 2026** y **«el 4.º ataque del año contra cuerpos policiacos»**, que describen nominalmente el mismo universo con cifras distintas | **Publicadas las cuatro** con su emisor, marcadas `CIFRAS CONTRADICHAS — NO SE ARBITRAN`, y **retirada la afirmación de que no se contradicen**. **Ninguna se usa como denominador** |
| **Error aritmético en la Conclusión 5**: aplicaba el cociente nacional (41/5 = 8,2) al subconjunto de Matamoros (38/4 = 9,5) | **Corregido**, y coincide con la corrección paralela de `editor-duplicidad` |
| **Segunda trampa de fecha en Matamoros**: existe un operativo del **4-5 de agosto de 2026** con **4 detenidos**, 1 arma larga, 2 cargadores y 133 cartuchos, que el buscador tiende a mezclar con el del 31-ago | **Añadido el deslinde expreso** a la tabla de candidatos. **Es la razón de que la casilla de detenidos de Matamoros quede vacía en vez de tomar prestada esa cifra** |
| **Precisión sobre Los Reyes**: la **sanción** es del Departamento del Tesoro (OFAC) y la **recompensa de 3 mdd** del **Departamento de Estado**; el borrador las presentaba en una sola frase | **Corregido**: dos agencias, dos instrumentos |
| **Confirmaciones que no exigieron cambio**: el saldo de **11 lesionados y ~40 viviendas** de Ojocaliente es la cifra vigente y **el descarte de la de 15/30 viviendas fue correcto** —es la versión **más antigua** de la serie, del parte de la noche del 30-ago, no una rectificación posterior—; la **`PENA COMPUESTA`** de Puebla se sostiene (ninguna fuente precisa «cada uno» ni «conjunta»); el **deslinde del caso del licor** es correcto y el *slug* institucional lo confirma como caso de **una sola persona**; las **31 placas** y los **27 meses** están bien calculados | — |

### 15.3 ⚠️ El arbitraje que cambió el conteo del corte

**`procedencia-cifras` marcó `NO INTEGRAR` la identidad del detenido de Piedra Gorda** —circulaba en
fuentes regionales y contradecía a las nacionales que el propio borrador citaba— **y pidió registrar
la contradicción**. Señaló además que esas fuentes regionales mencionaban **armamento asegurado en el
domicilio** que el borrador no recogía.

**El arranque obliga a arbitrar antes de obedecer, y aquí el arbitraje era obligado**: si ese
armamento era institucional, **cambiaba el conteo nacional del corte**. Una búsqueda lo resolvió:

- **El boletín es institucional**: `ssp.zacatecas.gob.mx`, «Detienen a presunto integrante de grupo
  delictivo relacionado con explosivo colocado en Dirección de Seguridad de Ojocaliente».
- **La identificación la publica una fuente nacional** que el borrador ya citaba: **Aristegui
  Noticias**, «Identifican a detenido por explosión en comandancia de Ojocaliente». **Juan Pedro «N»,
  29 años.**
- **Lo asegurado en el domicilio**: **un explosivo artesanal tipo niple**, **una granada de
  fragmentación**, **22 artefactos ponchallantas**, **cinco cargadores abastecidos**, dosis de
  mariguana, metanfetamina y cocaína, y **el vehículo en que viajaba**.

**Qué cambió en el producto**: se abrió `ARG-113-ARM-003`, y el conteo nacional pasó de **41 a 46
cargadores**, de **1 a 2 granadas**, de **0 a 1 AEI**, de **1 a 2 detenidos** y de **2 a 3 eventos en
3 entidades**.

⚠️ **Y lo que importa no es la aritmética**: **es el primer artefacto explosivo ASEGURADO de toda la
serie de Zacatecas.** Los tres anteriores fueron **empleados** y no dejaron material íntegro que
peritar. **La línea técnica que la serie llevaba seis días sin tener ya no depende de que la autoridad
publique nada: depende de que perite lo que ya tiene en su poder.** Es ahora la primera línea
accionable del corte.

**Lección de método, y es la tercera edición seguida que apunta a lo mismo**: `procedencia-cifras`
acertó al no integrar el nombre **con la evidencia que tenía**, y acertó al **señalar el material
asegurado como pista viva**. **Lo que ningún control puede hacer es la búsqueda que resuelve: eso es
del coordinador.** **Ni obedecer ni descartar por precaución: arbitrar.**

### 15.4 Registrado para trazabilidad, sin integrar

- **Un tercer caso de la FECOR Puebla**, publicado el **25-ago**: «hasta 62 años de prisión a tres
  personas por robo y secuestro exprés», hecho de diciembre de 2023 en la México-Amozoc-Perote.
  **Fuera de ventana y distinto de los otros dos.** Se anota para que **ninguna edición futura lo
  confunda** con `ARG-113-SEN-001` ni con el caso del licor.
- **La cifra «1,800 huevos de tortuga» de Arriaga** solo aparece **dentro del resumen del buscador**:
  el título del boletín contenedor sí es citable, la cifra en sí no. **La ficha ya lleva la confianza
  más baja del corte (★★☆☆☆) y la marca `PENDIENTE DE CORROBORACIÓN INDEPENDIENTE`**; se deja
  constancia expresa de que **el número no tiene fragmento propio**.
