# ARGOS 115 — Archivo de fuentes y trazabilidad

**Corte**: 2026-09-04 · **Ventana**: 2026-09-02 10:17 CDMX → 2026-09-04 09:09 CDMX (**46 h 52 min**)
**Hora verificada en sesión** con `TZ=America/Mexico_City date`: `2026-09-04 09:08:57 CST (viernes)`.

Este archivo conserva lo que el cartelón no publica: el barrido portal por portal, los hallazgos de
método, los descartes con su razón, las fes de erratas y la deuda que hereda la edición siguiente.

---

## 0. Verificación de base (Bloque 0 del arranque)

`git merge --ff-only origin/main` ejecutado **como primer comando de la sesión, antes de leer nada más**.

| Comprobación | Esperado | Encontrado |
|---|---|---|
| Última edición en `reports/` | `argos-2026-09-02` (ARGOS 114) | ✅ `argos-2026-09-02` |
| Archivos en `reports/` | 87 | ✅ 87 |
| `main` contiene la 114 | sí | ✅ `498d48a` |

**La rama asignada llegaba en `argos-2026-08-24` (ARGOS 106), nueve ediciones por detrás**, y sin su
propio archivo de arranque. **Noveno corte consecutivo con el mismo defecto.** El `ff-only` fue posible
(HEAD era ancestro de `origin/main`): numerar por lo que la rama tenía a la vista habría producido un
falso «ARGOS 107» con ventana solapada de más de una semana.

**Ventana**: 46 h 52 min. **Es la más larga desde ARGOS 111** y **rompe la racha de tres ventanas
decrecientes** (48 → 27 → 21 h). Declarado en portada y en la Valoración: los totales no son
comparables con los de la 114 sin normalizar por duración.

---

## 1. Egreso: vigesimoséptima edición bloqueada

Verificado **en esta sesión**, no heredado:

```
curl -sS -m 20 https://www.gob.mx/sspc
curl: (56) CONNECT tunnel failed, response 403
```

**Cero portales leídos por acceso directo.** Toda cita institucional es por título indexado o
republicador, y **cada sustitución queda anotada en la ficha que la usa**.
**Techo de confianza de todo el producto: ★★★★☆.**
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.

**Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` —que exige lectura directa—
figura en **0** en los dos cuadres. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.

---

## 2. Ciclo de rotación aplicado y declarado

**CICLO B — Noreste + Golfo encabezaron el triaje judicial**; las otras cuatro regiones encabezaron
con armamento. **No quedaba ninguna entidad `NO REVISADA` de la edición anterior**, así que el ciclo
se aplicó limpio, sin prioridad de saldo.

**Qué aportó la rotación que el orden anterior no habría aportado:**

- **Golfo** cerró el encargo de **Mesas de Construcción de la Paz** con **resultado positivo por
  primera vez**: Veracruz **sí tiene portal propio** (`veracruz.gob.mx/seguridad/mesa-de-coordinacion-para-la-construccion-de-la-paz/`
  y `cespver.gob.mx`), frente al negativo que Occidente había declarado para sus seis entidades en la
  edición anterior. **Tabasco, negativo**: solo existe el programa social «Jornadas de Paz», que **no
  se sustituye** por una mesa de coordinación.
- **Noreste**, al encabezar judicial, **detectó el patrón de fabricación de comunicados de la FGR**
  (ver §4) en San Luis Potosí, y lo detectó **por el mismo mecanismo** que Sureste en Campeche y
  Centro en Edomex y Puebla. **Tres regiones convergieron independientemente en el mismo defecto**,
  que es lo que lo acredita como patrón y no como caso aislado.

**Deuda regional asignada y su resultado:**

| Encargo | Región | Resultado |
|---|---|---|
| SEDENA / SEMAR / FGR / ANAM regionales | **CENTRO** | **Negativo declarado**: ningún comunicado propio y fechado en ventana de SEDENA, SEMAR ni ANAM. Estas corporaciones solo aparecen **integradas** en operativos conjuntos. **A diferencia de la edición anterior, esta asignación NO produjo el mayor aseguramiento del corte** |
| Mesas de Construcción de la Paz | **GOLFO** | **Positivo en Veracruz, negativo en Tabasco.** Ver arriba |
| `fiscaliaguerrero.gob.mx/index.php/AAAA/MM/DD/` | **SURESTE** | **Explotado, con negativo verificable**: `site:` con ruta `/2026/09/` no devuelve nada; el resultado más reciente indexado es `/2026/07/17/`. **Encargo cerrado: no repetir sin criterio nuevo** |

**A ARGOS 116 le toca el CICLO C — Occidente + Sureste.**

---

## 3. Barrido de las 32 entidades

Seis agentes `barrido-regional` en paralelo, lanzados en un solo mensaje antes de ningún otro encargo.

| Región | Entidades | Búsquedas | Hechos aportados |
|---|---|---|---|
| Noroeste | BC, BCS, Son, Sin, Chih, Dgo | 20 | **2** (Chihuahua ×2) |
| Noreste | Coah, NL, Tamps, SLP, Zac, Ags | 14 | **1** (Aguascalientes) |
| Occidente | Jal, Mich, Col, Nay, Gto | 19 | **2** (Guanajuato, Nayarit) |
| Centro | CDMX, Edomex, Hgo, Mor, Pue, Tlax, Qro | 18 | **2** (Puebla, Querétaro) |
| Golfo | Ver, Tab | 12 | 0 fichables |
| Sureste | Gro, Oax, Chis, Camp, Yuc, QRoo | 18 | **1** (Oaxaca) |

**Origen de los hechos publicados — el recall nacional sigue siendo obligatorio:**

| Origen | 112 | 113 | 114 | **115** |
|---|---|---|---|---|
| Barridos regionales | 3 de 7 | 4 de 6 | 3 de 8 | **6 de 7** |
| Recall y arbitraje del coordinador | 4 de 7 | 2 de 6 | 5 de 8 | **1 de 7** |

⚠️ **La proporción se invierte respecto de la edición anterior, y la causa es identificable**: el
hecho que el recall aportó —**el informe del Gabinete desde Zacatecas**— es de nuevo un **hecho
nacional de gran cobertura**, que se busca mejor por tema que por entidad. **Los barridos rindieron
más porque la ventana fue más del doble de larga**, no porque el recall haya perdido utilidad:
**siguió siendo el único que vio el hecho de apertura del cartelón**, e **interceptó tres falsos
positivos** (§5). **No retirar el recall por un resultado proporcionalmente menor.**

### Casillas de cobertura — cuadre nacional

| Casilla | Entidades |
|---|---|
| Con hallazgo **publicado en el cartelón** | **8** — Zacatecas, Puebla, Chihuahua, Guanajuato, Oaxaca, Aguascalientes, Nayarit, Querétaro |
| `SIN RESULTADO INDEXADO EN VENTANA` | **23** |
| Vacío acreditado | **1** — Tlaxcala |
| `NO REVISADA` | **0** |
| `SIN ACTUALIZACIÓN CONSTATADA` | **0** (exige lectura directa; egreso bloqueado) |
| **Cuadre** | **8 + 23 + 1 + 0 = 32** ✅ |

⚠️ **DIFERENCIA DECLARADA ENTRE EL CARTELÓN Y ESTE ARCHIVO** — regla nacida de la corrección de
ARGOS 114: **Veracruz publicó dentro de ventana** (`veracruz.gob.mx/2026/09/02/mas-de-60-vehiculos-recuperados-...`,
fecha en la ruta) **y el cartelón no lo ficha**, porque «más de 60» **no es cifra citable** y los
municipios y las cifras de armamento **solo viven en el párrafo del resumidor**. Por tanto:
**el cartelón cuenta 8 entidades con hallazgo; este archivo registra 9 con publicación en ventana.**
**Un indicador del cartelón no puede contar lo que el lector no puede verificar dentro del cartelón.**

### Casillas de cobertura — cuadre judicial

| Casilla | Entidades |
|---|---|
| Con sentencia publicada e **integrable** | **0** |
| `SIN RESULTADO INDEXADO EN VENTANA` | **30** |
| Vacío acreditado | **1** — FGE de Veracruz (sexto corte de agregados sin individualizar) |
| `NO REVISADA` | **1** — Fiscalía de Tabasco (presupuesto agotado tras priorizar la FGR; **se declara, no se disfraza**) |
| **Cuadre** | **0 + 30 + 1 + 1 = 32** ✅ |

**FGR revisada: Sí**, con sus delegaciones encabezando el triaje.

### Decisiones de portal tomadas en este corte

- ⚠️ **`fgjsonora.gob.mx` pasa a VACÍO ACREDITADO DE PORTAL.** **Sexta edición consecutiva sin
  resultado indexado.** El arranque pedía decidirlo «de una vez» y se decide: **no se le vuelve a
  asignar consulta dedicada** salvo indicio nuevo. **Sonora, como entidad, sigue revisada** por vía
  genérica: el vacío es del portal, no de la entidad.
- **`fiscalia.chihuahua.gob.mx` — trampa de *slug* sin fecha confirmada.** Sus boletines **no llevan
  fecha en la ruta** y un boletín de **junio** se presenta como actual. Ver §5.
- **`boletines.guanajuato.gob.mx`** (dominio con fecha en la ruta) **no indexó** el hecho de
  Pénjamo/Irapuato/Acámbaro/León. **Sustitución por medio regional anotada en la ficha.**
- **Dominios institucionales de Hidalgo y Puebla**: siguen **sin confirmar por `site:`**. Centro los
  consultó solo por genérica. **Deuda que pasa a ARGOS 116.**

---

## 4. HALLAZGO DE MÉTODO PRINCIPAL — el resumidor fabrica números de comunicado de la FGR

**Es el hallazgo más importante de esta edición y generaliza la lección de ARGOS 114.**

La edición anterior retractó, antes de publicar, tres sentencias de la FGR delegación Sinaloa
(`DPE/3852`, `DPE/3849`, `DPE/3850` de 2026) cuyo número de comunicado **solo vivía en el párrafo de
respuesta del buscador**. Se trató entonces como un caso aislado. **No lo era.**

**En este corte, tres regiones independientes y el coordinador localizaron el mismo defecto en cinco
entidades distintas:**

| Comunicado atribuido | Entidad | Quién lo localizó |
|---|---|---|
| `DPE/3852`, `DPE/3849`, `DPE/3850` de 2026 | Sinaloa | heredado de la edición anterior |
| `DPE/3897/2026` | Campeche | Sureste |
| `DPE/3893/2026` | San Luis Potosí | Noreste |
| `DPE/3855`, `DPE/3856`, `DPE/3857` de 2026 | Estado de México | heredado; Centro lo reencuentra |
| `DPE/3888`, `DPE/3889` de 2026 | Puebla | Centro |

**Verificación con cadena exacta entre comillas, ejecutada por el coordinador sobre dos de ellos:**

- `"DPE/3852" OR "DPE/3849" OR "DPE/3850"` → **cero titulares y cero URL con el dato**. Solo páginas
  índice de **portales espejo de la FGR sin fecha propia**: `alertaamber.fgr.org.mx`,
  `hasvistoa.fgr.org.mx`, `inacipe.fgr.org.mx`, `renadet.fgr.org.mx`, `bndf.fgr.org.mx`,
  `historicopgr.fgr.org.mx`.
- `"DPE/3897"` → **lo mismo**, y además devuelve **dos comunicados REALES de 2022**:
  `gob.mx/fgr/prensa/comunicado-fgr-dpe-3076-2022-...` y `...dpe-3016-2022-...`, **Tlaxcala**,
  **con el mismo molde de título** «FGR obtiene sentencia condenatoria contra una persona por
  portación de arma de fuego».

**Diagnóstico**: el molde de título es real y la FGR lo reutiliza desde al menos 2022 en decenas de
delegaciones. **El buscador lo completa con una delegación y un correlativo plausibles**, y lo fecha
en el día de la consulta. **La precisión del número es exactamente lo que lo hace creíble.**

**REGLA DERIVADA, para el arranque**: **un número de comunicado `DPE/…` que no aparezca literalmente
en un titular o en una URL no identifica ningún documento, por preciso que parezca.** La comprobación
correcta es **una búsqueda con la cadena exacta entre comillas**, y su resultado negativo es
**evidencia reproducible** que **vence al arbitraje del coordinador**.

**Efecto sobre el producto**: **de haberse aplicado el umbral de integración del módulo de armamento
—que admite confianza Bajo—, esta edición habría publicado cinco condenas inexistentes con delegación
y número de comunicado.** La asimetría de umbrales entre armamento y sentencias, que `CLAUDE.md`
declara deliberada, **acaba de pagarse sola por segunda edición consecutiva**.

---

## 5. Falsos positivos interceptados

**Cuatro, tres de ellos por el arbitraje del coordinador.**

| Candidato | Parecía | Es | Cómo se descartó |
|---|---|---|---|
| **Navolato, Sinaloa** — enfrentamiento, 3 muertos, 6 detenidos | del 3-sep | **30-dic-2025** | URL `infobae.com/mexico/2025/12/31/` con año en la ruta |
| **Tláhuac–Xochimilco, CDMX** — ataque armado, 3 muertos, 2 detenidos | del 3-sep | **22-may-2026** | Comunicado `ssc.cdmx.gob.mx/.../COM1477-2205-2026`, que **confirma el formato `COM<n>-DDMM-AAAA`** establecido en ARGOS 109 |
| **Chihuahua** — cateo FDZN, 6 detenidos, 2 armas, 202 cartuchos | de septiembre | **19-jun-2026** | Cuatro URL con fecha en la ruta (`laopcion` `20260619`, `zolonoticias/2026/06/19/`, `esloquehayjuarez/2026/06/19/`, `calibre800/2026/06/19/`) |
| **Emboscada al 16.º Regimiento de Caballería, Guerrero** — 3 militares muertos | del corte | **fecha inexistente** | El resumidor la fechó el **«26 de septiembre de 2026»**, **posterior al día del corte**. Patrón «el resumidor inventa futuros», ya documentado |

⚠️ **Los dos primeros los presentaba un *liveblog***: el «EN VIVO: seguridad, crimen y narcotráfico en
México hoy 3 de septiembre» de Infobae. **Confirma la regla de ARGOS 103 por enésima vez: un
*liveblog* fecha la página, no el hecho, y no basta como fuente única.**

⚠️ **El tercero enseña algo nuevo sobre `fiscalia.chihuahua.gob.mx`**: sus *slug* **no llevan fecha**,
de modo que un boletín de junio es indistinguible de uno de septiembre por la ruta. **Anotado como
trampa de dominio.**

**Descartes por ventana, sin incidencia**: Durango El Oro (28-ago, 39 armas) · Tijuana 58 armas
(1-sep) · Sabinas Hidalgo 210 armas (31-ago, ya publicado) · Veracruz 35 detenidos (1-sep, cifra
coincidente con el agregado ya contabilizado: **riesgo de doble conteo evitado**) · Campeche
Champotón (22-ago) · Quintana Roo Kantunilkín (20-ago) · Guanajuato «Sinergia» (26-ago) ·
Coahuila «Modelo de Seguridad» (corte al 30-ago) · Michoacán Tocumbo/«El Wicho» (30-ago/1-sep,
**ya publicado en la edición anterior: no vuelve como `-REC-`, que sería duplicación**).

---

## 6. Los siete ejes de seguimiento — resultado

### 6.1 ZACATECAS — tres preguntas, tres búsquedas (tope respetado)

**(c) La obligación de calendario: CUMPLIDA Y VERIFICADA.** El **Gabinete de Seguridad rindió el
informe desde Zacatecas el 4-sep**, dentro de ventana. **Línea de investigación principal: disputa
entre el CJNG y el Cártel del Pacífico** (titular con fecha en la ruta, Infobae `2026/09/04`).
Es el **hecho de apertura del cartelón** (`ARG-115-001`).

⚠️ **Las cifras del agregado NO se integran**: 3,824 detenidos, 1,200 armas, 114,000 cartuchos,
7,320 kg de droga y 6 laboratorios (1-oct-2024 a 31-ago-2026) **no aparecen en ningún titular ni URL**
—solo en el párrafo del buscador— **y además son agregado de 23 meses**, que no se reparte.
**Doble razón para no usarlas como denominador.**

**(b) Luis Moya: RESUELTO, y la contradicción se explica.** La cobertura del 1-sep
(`razon.com.mx/estados/2026/09/01/van-4-ataques-explosivos-en-el-ano-contra-cuerpos-policiacos-de-zacatecas/`,
**titular y fecha en la ruta**) enumera los cuatro como **CUATRO MUNICIPIOS**: Villa García, Tabasco,
Luis Moya y Ojocaliente. **No enumera cuatro ataques.**

> **El «cuatro del año» se cuenta por MUNICIPIO, no por evento.** Como **Luis Moya tiene dos ataques**
> —5-mar (3 uniformados heridos) y 31-jul/1-ago (**1 policía muerto**, 2 heridos, Barranquilla)—,
> **por evento son CINCO.** La autoridad no se equivoca: **usa otra unidad de medida y no la declara.**

**Esto no cierra el pendiente: lo reformula.** Sigue haciendo falta un corte de la FGJEZ con criterio
explícito. **Y aparece una quinta cifra**: «**17 ataques con explosivos en dos años**»
(Infobae `2026/09/01`, titular). **No se funden las dos listas de emisores distintos**: explosivos
(4 municipios) y agresiones a policías de la FGJEZ (7 municipios) **son universos distintos**.

**(a) El niple de Piedra Gorda: `SIN AVANCE`, tercera edición — pero con un cambio de naturaleza.**
No hay dictamen publicado del **artefacto asegurado íntegro**. **El deslinde se conserva y se
confirma**: lo peritado y publicado sigue siendo el **coche bomba EMPLEADO en Ojocaliente**, y la
búsqueda vuelve a devolver los dos objetos juntos.
⚠️ **Dato nuevo que reclasifica el pendiente**: la **propia Fiscalía estatal declara que aún no
determina qué tipo de explosivo se usó ni qué mecanismo lo detonó**. **Deja de ser un vacío de
búsqueda y pasa a ser un vacío declarado por el emisor.**

### 6.2 Los dos detenidos y el accionador de Villa García — dos búsquedas

**Vinculación a proceso: `SIN AVANCE`, cuarta edición.** Ninguno de los dos tiene causa penal
difundida. **William Ariel «N» (18)** sigue **entregado a la FGR** —cambio de fuero— sin causa
penal; **Juan Pedro «N» (29)**, sin novedad. **Son dos detenciones distintas y no se funden.**

**Dato nuevo, y es de móvil**: la autoridad vincula el **coche bomba de Ojocaliente** a una
**represalia por la detención de William Ariel «N»** en Villa García. **El intervalo entre la captura
y el atentado es de 24 a 48 horas**: es un **tiempo de respuesta medible**, y así se explota en el
cartelón. **Coexiste con la hipótesis federal de disputa CJNG–Cártel del Pacífico**: son
**complementarias, no excluyentes**, y **no se funden**.

**El accionador: vacío acreditado, no pendiente de búsqueda.** El Fiscal estatal declara que
**seguían determinando tipo de explosivo y mecanismo de detonación**. **Mecanismo confirmado**
(detonación remota por los propios sospechosos) pero **sin identificadores de fábrica, marca ni
tipo**. **No gastar más presupuesto salvo peritaje publicado.**

**Aguascalientes**: no se volvió a buscar el origen de los detenidos —ya resuelto e integrado—.
**Se buscó hacia adelante y rindió**: ver §6.7.

### 6.3 SINALOA — Rosario, Agua Verde — dos búsquedas

**`SIN AVANCE` en los tres pendientes**, y el hecho **queda fuera de esta ventana** (publicación
1-sep, anterior al arranque):

- **Situación migratoria y ruta de entrada** de los 4 colombianos y 1 cubano: `SIN RESULTADO INDEXADO EN VENTANA`.
- **Protocolo aplicado a la menor**: `SIN RESULTADO INDEXADO EN VENTANA`.
- **Vinculación a proceso**: solo consta el turno al MP de la FGR; **ningún boletín posterior**.

Localizado el **portal de la SSP de Sinaloa** con el hecho (`sspsinaloa.gob.mx/post/en-rosario-el-grupo-interinstitucional-detuvo-a-9-civiles-...`),
**que confirma el municipio de Rosario** ya cerrado en la edición anterior. **Mantiene su prioridad.**

### 6.4 MICHOACÁN — sucesión del Cártel de Los Reyes — dos búsquedas

**`SIN AVANCE`, y el negativo es el resultado.** **Ninguna violencia nueva de la disputa sucesoria
dentro de la ventana** en **Tocumbo, Los Reyes, Peribán ni colindantes**. El abatimiento de
«El Wicho»/«R5» en **Rodeo del Pinal, Tocumbo** y los bloqueos derivados (Jacona–Los Reyes,
Los Reyes–Peribán, Los Reyes–Uruapan, Uruapan–Peribán) son del **30-ago/1-sep**, **anteriores a la
ventana y ya publicados**. **No vuelven como `-REC-`: eso sería duplicación.**
**El seguimiento mantiene su prioridad**: la ventana de mayor probabilidad de repunte **no se ha cerrado**.

### 6.5 JUDICIAL — dos candidatos, dos búsquedas

**(a) Las tres sentencias de la FGR Sinaloa: RETIRADAS POR UMBRAL.** **Segunda edición consecutiva
sin fragmento citable.** Se aplica el umbral de cifras arrastradas de `CLAUDE.md`: **se retiran como
candidato y no se vuelven a listar** salvo titular o URL que contenga el número de comunicado.
Ver §4: **el defecto resultó ser sistémico, no de estas tres.**

**(b) Teotihuacán: el descarte SE SOSTIENE, tercera edición.** **Ningún comunicado de la FGR.**
Las dos URL de `gob.mx/fgr` que devuelve la consulta son **`DPE/272/19` y `DPE/392/21`** —**2019 y
2021, otros casos, el mismo molde de título**—. **Ganancia real del corte**: ahora constan los
**cuatro nombres** (Jesús Cortés Flores, Jonás Baltazar García, Jorge Javier Arenas Mendoza,
Octaviano Néstor Nochebuena), la **multa exacta de $292,160 «cada uno»**, el hecho de **diciembre de
2016** y el **CEFERESO N.º 1 «El Altiplano»**.
⚠️ **Los campos individualizadores identifican el caso; no acreditan la resolución.** Y sigue siendo
**`PENA COMPUESTA`: el «cada uno» está publicado de la MULTA, no de la prisión.** Además su
**publicación es del 1-sep**, anterior a la ventana. **Se declara la razón principal —falta de fuente
oficial— y no la accesoria**, para no dejar una regla mal aplicada en el archivo.

### 6.6 BAJA CALIFORNIA — Valdez Mainero — una búsqueda

**`SIN AVANCE`.** Confirmado el cuerpo del caso —62 años, último contacto el **viernes 28-ago**
(día verificado contra calendario), Zona Río y Estadio Caliente, denuncia impulsada por la familia—.
**Siguen sin publicarse carpeta, ficha de búsqueda e hipótesis oficial.** La cobertura del 2-sep es
`Evento anterior publicado durante el corte`: **no se ficha de nuevo.**

### 6.7 El eje que rindió sin estar en la lista — Aguascalientes hacia adelante

**Noreste aportó `ARG-115-007`**: detención en **Cosío** de **«El Niño Concepción»**, objetivo
prioritario **con carpetas en Aguascalientes Y en Zacatecas**. **Es el tercer detenido en dos semanas
que cruza ese eje** y **el primero que lo acredita documentalmente**, no por inferencia: los dos
anteriores eran *originarios* de Aguascalientes; este **tiene delitos imputados en ambas entidades**.
**El corredor Aguascalientes–Zacatecas deja de ser una lectura y pasa a ser un hecho con expediente.**

---

## 7. Fes de erratas de esta edición

**Ninguna aparece en el cartelón** —ni en la móvil—, conforme a la instrucción editorial permanente.
Se registran aquí y en `indice-arg-id.md`.

| ARG-ID | Corrección |
|---|---|
| `ARG-115-FE-001` | **Sobre el «cuatro ataques con explosivo del año» de Zacatecas** (arrastrado desde ARGOS 113). **La contradicción con el archivo NO era un error de la autoridad ni de ARGOS**: el conteo oficial enumera **cuatro MUNICIPIOS** —Villa García, Tabasco, Luis Moya, Ojocaliente—, no cuatro eventos. Como **Luis Moya tiene dos ataques documentados**, **por evento son cinco**. Se retira la marca de contradicción entre el «cuatro» y el hallazgo de Luis Moya: **son compatibles bajo unidades de medida distintas**. **Persiste la falta de un corte de la FGJEZ con criterio explícito.** NO PUBLICADA EN EL CARTELÓN |
| `ARG-115-FE-002` | **Sobre los tres candidatos judiciales de la FGR Sinaloa** (`DPE/3852`, `DPE/3849`, `DPE/3850` de 2026), retractados en ARGOS 114. **Segunda edición sin fragmento citable: se aplica el umbral y se RETIRAN definitivamente como candidatos.** La verificación con cadena exacta vuelve a devolver **cero titulares y cero URL**. **No afectan a ningún total: nunca llegaron a integrarse.** NO PUBLICADA EN EL CARTELÓN |
| `ARG-115-FE-003` | **Sobre `fgjsonora.gob.mx`.** **Sexta edición consecutiva sin resultado indexado.** Se resuelve la indecisión que el arranque arrastraba desde ARGOS 111: **se declara VACÍO ACREDITADO DE PORTAL** y no se le vuelve a asignar consulta dedicada. **Sonora, como entidad, permanece revisada por vía genérica**: el vacío es del portal, no de la entidad. NO PUBLICADA EN EL CARTELÓN |
| `ARG-115-FE-004` | **Sobre `tools/gen-movil.py`.** La derivación de la etiqueta de navegación usaba `re.fullmatch(r"\(I+\)", sufijo)`, que **solo acepta numerales romanos formados por íes**. ARGOS 115 es **la primera edición con una página «CRIMEN ORGANIZADO (IV)»** y el numeral se perdía: **dos secciones distintas aparecían como «CRIMEN ORGANIZADO» en la barra de navegación móvil**. **Se corrigió la HERRAMIENTA, no su salida** —patrón `\((?=[IVXLC])[IVXLC]+\)` y `NAV_ABREV` generado por comprensión para I–X—, y la móvil se regeneró. NO PUBLICADA EN EL CARTELÓN |
| `ARG-115-FE-005` | **HALLAZGO DE MÉTODO QUE GENERALIZA LA RETRACTACIÓN DE ARGOS 114**: el resumidor del buscador **fabrica números de comunicado de la FGR**. Localizado en **cinco entidades** por **tres regiones independientes y el coordinador** — ver §4. **Regla derivada**: un número `DPE/…` que no aparezca literalmente en un titular o una URL **no identifica ningún documento**, por preciso que parezca. **Efecto evitado**: cinco condenas inexistentes con delegación y número de comunicado. NO PUBLICADA EN EL CARTELÓN |
| `ARG-115-FE-006` | ⚠️ **DOBLE CONTEO ENTRE EDICIONES, detectado por `editor-duplicidad` y verificado por el coordinador.** El borrador integraba como hecho nuevo del 3-sep el aseguramiento de **Pénjamo, Guanajuato** —Luis Daniel «N», 27 años, 1 fusil 7.62×39, 50 cartuchos, 3 cargadores— que es **el mismo hecho del 31-ago ya publicado como `ARG-113-003` / `ARG-113-ARM-002`** y **ya integrado en el total nacional de ARGOS 113**. **Coincidencia en ocho criterios.** Ver §10. NO PUBLICADA EN EL CARTELÓN |
| `ARG-115-FE-007` | ⚠️ **CIFRA INCOMPLETA Y CIFRA EN DISPUTA, detectadas por `procedencia-cifras` y confirmadas por arbitraje del coordinador.** En Villas del Real, Chihuahua, faltaba **un revólver cal. .32** además del arma .45 —**armas cortas 1 → 2**— y los cartuchos **no eran cifra pacífica**: circulan **13, 23 y 36** entre seis regionales. Ver §10. NO PUBLICADA EN EL CARTELÓN |

---

## 8. Reservas y contradicciones vivas — declaradas, no arbitradas

| Asunto | Estado |
|---|---|
| **Cinco cifras de ataques con explosivos en Zacatecas** | 17 en dos años · 10 en 2026 · 7 contra policías · «el 4.º del año» (por municipio) · **cinco por evento**. `NO SE ARBITRAN`. **Ninguna sirve como denominador mientras no se declare la unidad de conteo** |
| **Daños en Ojocaliente** | **~40 viviendas** (autoridad estatal, 1-sep) frente a **~30** (2-sep). Vehículos: **13**. Lesionados: **11**. `NO SE ARBITRA` |
| **Dos hipótesis del móvil del coche bomba** | **Represalia por la detención de William Ariel «N»** (autoridad estatal) y **disputa CJNG–Cártel del Pacífico** (federal, 4-sep). **Complementarias, no excluyentes. No se funden** |
| **Nayarit — Acaponeta y Huajicori dentro del agregado del 2-sep** | **2 AEI, 8 cargadores, 236 cartuchos**, a **una unidad** de un hecho del **11-ago** ya descartado por ventana (8 cargadores, **235** cartuchos, 2 AEI). `POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN`. **Detectado por Occidente contrastando contra `argos-2026-08-13-fuentes.md`** |
| **Chiapas — La Trinitaria** | **2 armas largas, 920 cartuchos, 34 cargadores**, Ejército, 91.º Batallón de Infantería. **Sin fecha en URL ni en titular**; el resumidor dice «hace 3 días». `FECHA NO FIJADA — NO INTEGRAR`. **Candidato para ARGOS 116** |
| **Puebla — «operativo con dos detenidos y un agresor abatido»** | Titular suelto sin fecha fijable ni relación acreditada con «El Amarillo». **Si hubo abatido requiere ficha propia 🟡/🔴 según quién inició.** `FECHA NO FIJADA` |
| **Morelos — 31 detenidos, 1 lanzagranadas, 8 largas, 11 cortas** | `morelos.gob.mx/ultimas-noticias`, **dominio sin fecha en la ruta y con trampa de año verificada**. `FECHA NO FIJADA — NO INTEGRAR` |
| **Hidalgo — Tepeji del Río y Huichapan** | Sentencia por portación y enfrentamiento con 5 detenidos, 3 largas y 2 granadas. **Ninguna con fecha en titular ni URL.** `FECHA NO FIJADA` |
| **SSC CDMX — comunicados «1781» y «107»** | **Sin fecha en la ruta con el formato vigente `COM<n>-DDMM-AAAA`.** Se excluyen **por no poder fijarse**, no por inexistencia |

---

## 9. Controles editoriales

Los seis `barrido-regional` y los dos controles (`editor-duplicidad`, `procedencia-cifras`) se
ejecutaron **como subagentes, autorizados expresamente por el destinatario en esta sesión**.
Sus hallazgos y las correcciones aplicadas se consignan en §10. **Los dos devolvieron `CORREGIR ANTES DE PUBLICAR` y los dos tenían razón.**

**El cuarto control, que no es un subagente, es el arbitraje del coordinador**: en esta edición
**interceptó tres de los cuatro falsos positivos** (§5) y **produjo la evidencia negativa reproducible
que sostiene §4**.

⚠️ **Y en esta edición el arbitraje se sometió a su propia regla**: la evidencia negativa de la cadena
exacta **venció a la tentación de integrar** los candidatos judiciales, que es la dirección en la que
el arbitraje falló en ARGOS 114.

---

## 10. Hallazgos de los controles y correcciones aplicadas

**Décima edición consecutiva con hallazgos reales de los dos controles, y la de mayor impacto sobre
las cifras publicadas desde ARGOS 105.** Los dos devolvieron `CORREGIR ANTES DE PUBLICAR` y los dos
tenían razón. **Ambos se arbitraron con búsqueda o `grep` propios antes de obedecerlos**, y el
arbitraje **confirmó a los dos**.

### 10.1 `editor-duplicidad` — doble conteo entre ediciones (`ARG-115-FE-006`)

**El hallazgo más grave de la edición.** El borrador publicaba como hecho nuevo del **3-sep** el
aseguramiento de **Pénjamo, Guanajuato**: Luis Daniel «N», 27 años, 1 fusil cal. 7.62×39, 50 cartuchos
y 3 cargadores. **Es el mismo hecho del 31-ago** ya publicado como **`ARG-113-003` / `ARG-113-ARM-002`**
y **ya sumado al total nacional de ARGOS 113** (5 largas, 180 cartuchos, 46 cargadores).

**Verificación propia del coordinador** (`grep` sobre `indice-arg-id.md` y sobre
`reports/argos-2026-09-01.html`): **coincidencia en ocho criterios** —municipio, localidad
(Santa Elena de Aceves), nombre, edad, arma, calibre, cartuchos y cargadores—, con **boletín estatal
fechado en la ruta** (`boletines.guanajuato.gob.mx/2026/08/31/`). **El control tenía razón.**

**Cómo entró el error**: el agregado que la Secretaría de Seguridad y Paz difundió el 3-sep
**reempaqueta el aseguramiento del 31-ago dentro de una jornada de cuatro municipios y no lo fecha**.
El barrido de Occidente lo trajo de buena fe desde `am.com.mx`, con fecha en la ruta del 3-sep —**que
es la fecha de publicación, no la del hecho**—.

**Corrección aplicada en sitio** (la edición no se había distribuido):
- **`ARG-115-ARM-003` se retira**, queda sin usar y **fuera del índice**.
- **`ARG-115-005` pasa a `EVENTO CUALITATIVO — CERO CIFRAS INTEGRADAS`**, con el deslinde escrito en la
  ficha y **fila atenuada** en la tabla. **Conserva su ficha**: la difusión existió y el hecho de que un
  emisor estatal recicle cifras sin fecharlas **es dato para el mando**.
- **Los 9 detenidos tampoco se integran**: incluyen a la persona ya contada y **la fuente no los
  desglosa por municipio**, de modo que **no puede separarse lo nuevo de lo ya contado**.

⚠️ **CAUSA RAÍZ, y es de método**: el `grep` obligatorio por topónimo **sí se hizo**, pero **solo sobre
los topónimos del arranque** —Tocumbo, Los Reyes, Peribán, Rosario, Agua Verde, Luis Moya, Piedra
Gorda, Villa García, Teotihuacán, Valdez Mainero, Ojocaliente—. **Pénjamo no estaba en esa lista
porque lo aportó un barrido regional al final del proceso**, cuando el `grep` ya se había ejecutado.

> **REGLA DERIVADA PARA EL ARRANQUE**: **el `grep` por topónimo se repite sobre CADA topónimo que un
> barrido traiga, no solo sobre los que el arranque enumera.** Un hecho que el archivo ya tiene entra
> por la puerta que el `grep` no cubrió, y **los topónimos nuevos llegan siempre después del `grep`**.

### 10.2 `procedencia-cifras` — un arma omitida y una cifra en disputa (`ARG-115-FE-007`)

El borrador presentaba el aseguramiento de **Villas del Real, Chihuahua** como **1 arma corta y
13 cartuchos cal. .45**, con «cifras coincidentes entre tres regionales». **No resistió verificación
independiente**, y el control acertó **en las dos direcciones**:

- **Faltaba un arma**: además del arma cal. .45 con dos cargadores, **se aseguró un revólver cal. .32**,
  descrito por **al menos cuatro fuentes** que el borrador no había consultado.
  **El control obligó a INTEGRAR, no a retirar** — que es la dirección en la que un control rara vez
  se usa y que `CLAUDE.md` exige expresamente.
- **Los cartuchos no eran cifra pacífica**: circulan **13**, **23** y **36** entre seis regionales,
  todas con fecha en la ruta.

**Arbitraje del coordinador con búsqueda propia**: confirma literalmente **«un revólver calibre .32 y
un arma calibre .45 con dos cargadores y 13 cartuchos calibre .45»**, y **«adicionalmente, 23 cartuchos
calibre .45»** — lo que explica la variante de 36 como suma de dos lotes. **Sumarlos sería derivar de
la redacción de un resumidor**, no de una cifra publicada.

**Corrección aplicada en sitio**:
- **Armas cortas: 1 → 2** en la fila, y **2 → 3** en el total nacional.
- **Cartuchos de esa fila: `CIFRA EN DISPUTA (13/23/36) — NO SE ARBITRA`**, **retirados del total
  numérico**, que baja de 190 a **127**.
- **Confianza de la fila: Medio → Bajo**, por **corroboración asimétrica**: la fija el campo peor
  sostenido, y la marca se aplica al renglón completo.
- **Datos nuevos incorporados**: **~242 g de cristal**, **insignias además de uniformes**, y
  **Pedro D.R. (39) es originario de Ciudad de México** —los otros tres, de Chihuahua—, lo que
  **refuerza la lectura de operadores foráneos** que la serie viene registrando.

### 10.3 Otros dos hallazgos aplicados

- **Veracruz se contaba entre los «eventos cualitativos» del total de armamento sin tener ficha ni
  fila.** Es **el mismo defecto de auditabilidad que obligó a corregir ARGOS 114**, reaparecido en otro
  renglón. **Retirado**: los eventos cualitativos quedan en **2** (Puebla y Oaxaca), ambos con ficha
  verificable dentro del cartelón.
- **Oaxaca también cae en el día de apertura con hora no fijada** y no llevaba la marca.
  **Corregido**: `FRONTERA DE VENTANA — HORA NO FIJADA` en su ficha, y la portada declara **2 hechos**
  en frontera, no 1.

### 10.4 Efecto acumulado de los controles sobre las cifras publicadas

| Renglón | Borrador | Publicado | Motivo |
|---|---|---|---|
| Armas cortas | 2 | **3** | revólver .32 omitido (`FE-007`) |
| Armas largas | 2 | **1** | fusil de Pénjamo ya contado (`FE-006`) |
| Cartuchos | 190 | **127** | 13 en disputa + 50 ya contados |
| Cargadores | 7 | **4** | 3 ya contados |
| Detenidos | 15 | **6** | 9 no separables de lo ya contado |
| Entidades con aseguramiento integrado | 2 | **1** | solo Chihuahua |
| Eventos contabilizados | 3 | **2** | |

**Sin los dos controles, esta edición habría publicado un total nacional inflado en armas largas,
cartuchos, cargadores y detenidos, y corto en armas cortas.**

---

## 11. Verificaciones de construcción

| Control | Resultado |
|---|---|
| Bloque de datos hasta `const SIZE_R`, `node --check` | ✅ OK |
| Las siete constantes presentes (`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL`, `GRIS`, `MEXICO_PATHS`) | ✅ ninguna falta |
| Cada `estado:` existe en `MEXICO_PATHS` | ✅ |
| Cada `region:` coincide con `STATE_REGION` | ✅ (Aguascalientes → **Occidente**, según la tabla, no según el reparto de barridos) |
| Ninguna fecha fuera de la ventana | ✅ |
| ARG-ID duplicados | ✅ ninguno |
| Semáforo derivado de `EVENTOS` vs. contadores tecleados en portada y `radar-stats` | ✅ **0 / 0 / 7** en los tres |
| Regla de cinco líneas, contador automático | ✅ **16 bloques, 0 exceden** |
| Exactamente una etiqueta `<body>` | ✅ (**faltaba por desfase de una línea al extraer la plantilla; corregido**) |
| Secciones escritorio = secciones móvil | ✅ 8 y 8 |
| Toda tabla envuelta exactamente una vez en `table-wrap` | ✅ 2 y 2 |
| `sem-item` fuera de portada | ✅ 0 |
| `-FE-` en escritorio y en móvil | ✅ 0 y 0 |
| Pie con número, fecha y hora en todas las páginas | ✅ 8 de 8 |
| Todos los ARG-ID del escritorio presentes en la móvil | ✅ 12 de 12 |
| Restos de clases de escritorio en la móvil | ✅ 0 |
| `validación OK` del generador y contadores coincidentes | ✅ 🔴 0 🟡 0 🟢 7 |
