# ORDEN DE ARRANQUE — ARGOS 116

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 115** (corte 2026-09-04).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git fetch origin                                   # traer el estado real
git log --oneline -1 origin/main                   # ¿main está al día?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6             # ¿cuál es la última edición del archivo?
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 116**: última edición `argos-2026-09-04` (ARGOS 115), **90 archivos**
en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló NUEVE ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 115 mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición
> —**nueve ediciones por detrás**— y **no contenía su propio archivo de arranque**: numerar por lo que la
> rama tenía a la vista habría producido **un falso «ARGOS 107» con ventana solapada de más de una semana**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Edición** | **ARGOS 116** |
| **Ventana** | **desde 2026-09-04 09:09 CDMX** (cierre de ARGOS 115) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-117.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de solape.
**Verifique la hora, no la suponga.**

✅ **La racha de ventanas decrecientes se rompió**: 48 → 27 → 21 → **47 h**. ARGOS 115 fue la más larga
desde ARGOS 111 y **su volumen lo refleja: 7 hechos en 7 entidades, frente a 3 en 3**.
**Ninguna edición es comparable con otra sin normalizar por duración**, y así se declaró en portada y
Valoración. **Conviene sostener horas de arranque estables para que la serie recupere comparabilidad.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-04-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.

   ⚠️⚠️ **LA REGLA QUE ARGOS 115 PAGÓ CARA, Y ES LA MÁS IMPORTANTE DE ESTE ARRANQUE:
   EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO TRAIGA, INMEDIATAMENTE ANTES DE
   FICHAR — NO SOLO SOBRE LOS QUE ESTE ARCHIVO ENUMERA.**
   En ARGOS 115 el `grep` **sí se ejecutó**, sobre los once topónimos del arranque, y **funcionó**.
   Pero **Pénjamo no estaba en esa lista porque lo aportó un barrido regional al final del proceso**,
   cuando el `grep` ya se había hecho — y **Pénjamo ya estaba en el archivo**: el borrador iba a publicar
   como hecho nuevo del 3-sep un aseguramiento del **31-ago ya contabilizado en ARGOS 113**, con
   **coincidencia en ocho criterios**. **Lo detectó `editor-duplicidad` y habría sido doble conteo entre
   ediciones.** **Los topónimos nuevos llegan SIEMPRE después del `grep` inicial.**

   ⚠️ **Y el `grep` debe ser por TOPÓNIMO DE LOCALIDAD, no solo por entidad y municipio.**
   «Cuauhtémoc» es municipio de Zacatecas, de Chihuahua Y alcaldía de CDMX · «Matamoros» está en
   Tamaulipas Y Coahuila · «Los Reyes» en Michoacán Y Edomex (Los Reyes La Paz) · «Rosario»/«El Rosario»
   en Sinaloa · «Villa de La Paz» es de San Luis Potosí, **no de Guerrero**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 116 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. SEXTA EDICIÓN COMO PASO
OBLIGATORIO.**

| Origen del hecho | ARGOS 112 | ARGOS 113 | ARGOS 114 | **ARGOS 115** |
|---|---|---|---|---|
| Barridos regionales | 3 de 7 | 4 de 6 | 3 de 8 | **6 de 7** |
| Recall y arbitraje del coordinador | 4 de 7 | 2 de 6 | 5 de 8 | **1 de 7** |

⚠️ **La proporción se invirtió y NO significa que el recall haya perdido utilidad.** Con una ventana de
47 h —más del doble— los barridos rinden más. **El recall siguió siendo el único que vio el hecho de
apertura del cartelón** —el informe del Gabinete desde Zacatecas— **e interceptó TRES de los cuatro
falsos positivos**. **La razón es estructural: un hecho nacional de gran cobertura se busca mejor por
tema que por entidad, y los barridos están organizados por entidad. No lo retire.**

⚠️ **EL ARBITRAJE DEL COORDINADOR, EN SU VERSIÓN CORRECTA, FUNCIONÓ.** Ver Bloque 5. En ARGOS 115
interceptó tres falsos positivos, produjo la evidencia negativa que sostiene el hallazgo judicial, y
**cuando los dos controles editoriales lo contradijeron, arbitró con `grep` y búsqueda propios y les
dio la razón a los dos**. **Ni obedecer ni descartar por precaución: arbitrar — y aceptar el resultado.**

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene tres preguntas, el tope
es **de tres en total, no de tres por pregunta**. En ARGOS 115 se respetó en los siete ejes.
**Cerrar un seguimiento en `SIN AVANCE` es el resultado correcto cuando no hay dato.**

✅ **LA REGLA DE `site:` FUNCIONA. EL OBJETIVO PORCENTUAL SIGUE RETIRADO — NO LO REINTRODUZCA.**

> **`site:` SOLO contra dominios con fecha en la ruta; contra los demás, consulta genérica.**

**Dominios con fecha en la ruta — no los redescubra**: Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/` ·
Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` (**el único portal de las 32 que publicó con
ruta fechada en la ventana de ARGOS 115**) · Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/` ·
San Luis Potosí `seguridad.slp.gob.mx/noticias/AAAA/M/D/` · Veracruz `veracruz.gob.mx/AAAA/MM/DD/`
(**útil: es la vía de Veracruz, no la FGE**) · Guerrero `fiscaliaguerrero.gob.mx/index.php/AAAA/MM/DD/`
(**explotado en ARGOS 115 con negativo declarado: lo más reciente indexado es `/2026/07/17/`.
NO repetir sin criterio nuevo**).

**Sin fecha en la ruta (use genérica)**: Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa `fiscaliasinaloa.mx`
y `sspsinaloa.gob.mx` · Chihuahua `fiscalia.chihuahua.gob.mx` y `sspe.chihuahua.gob.mx`
(⚠️ `ssp.chihuahua.gob.mx` es FALSO) · Colima `fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` ·
Edomex `fgjem.edomex.gob.mx` · BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` ·
Coahuila `sspcoahuila.gob.mx` · Tamaulipas `tamaulipas.gob.mx/seguridadpublica/` (sin subdominio propio) ·
Tabasco `fiscaliatabasco.gob.mx` y `tabasco.gob.mx/seguridad` · Aguascalientes `aguascalientes.gob.mx/ssp/` ·
Puebla `ssp.puebla.gob.mx` · Morelos `morelos.gob.mx/ultimas-noticias`
(⚠️ **trampa de año verificada**) · Veracruz, Mesa de Paz: `cespver.gob.mx` y
`veracruz.gob.mx/seguridad/mesa-de-coordinacion-para-la-construccion-de-la-paz/` (**confirmados en ARGOS 115**).

⚠️ **TRAMPA DE DOMINIO NUEVA, VERIFICADA EN ARGOS 115**: **`fiscalia.chihuahua.gob.mx` no lleva fecha en
la ruta**, de modo que **un boletín de junio es indistinguible de uno de septiembre**. Un cateo del
**19-jun** entró como candidato y solo se descartó por **cuatro URL de republicadores con fecha**.
**Exija siempre ancla de republicador fechado para esta fiscalía.**

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** · **FGE Veracruz** (seis cortes de agregados sin
individualizar; **la vía útil en Veracruz es la FGR y el portal del gobierno estatal**) ·
**`ssypc.nayarit.gob.mx`** · ✅ **`fgjsonora.gob.mx` — DECIDIDO EN ARGOS 115 TRAS SEIS EDICIONES:
VACÍO ACREDITADO DE PORTAL. No le asigne consulta dedicada. Sonora sigue revisada como entidad por vía
genérica: el vacío es del portal, no de la entidad.**
**No publican indexable**: FGJ Nuevo León · SSP Zacatecas.

### 3.2 Cobertura — qué encabeza el triaje y a quién se le asigna la deuda

**No queda ninguna entidad `NO REVISADA` en el cuadre nacional.** ⚠️ **Sí queda UNA en el judicial:
la Fiscalía de Tabasco**, por agotamiento de presupuesto tras priorizar la FGR. **Encabeza el triaje
judicial de Golfo en ARGOS 116 por prioridad sobre el ciclo.**

**A ARGOS 116 le toca el CICLO C — Occidente + Sureste** encabezando el triaje judicial; las otras
cuatro encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

⚠️ **DIRIJA EL TRIAJE JUDICIAL A LAS DELEGACIONES DE LA FGR ANTES QUE A LAS FISCALÍAS ESTATALES.
QUINTA EDICIÓN CONSECUTIVA SIN SENTENCIA ESTATAL INTEGRABLE Y SEGUNDA SIN NINGUNA FEDERAL.**
**No retire el ciclo por un resultado negativo**: su función es hacer **demostrable** el `SIN DATO`.
Pero **lea antes el Bloque 4**: en ARGOS 115 la causa del cero **dejó de ser «no publican» y pasó a ser
demostrada**.

⚠️ **MANTENGA LA ASIGNACIÓN EXPLÍCITA DE LA DEUDA REGIONAL, EN ROTACIÓN.** En ARGOS 115:
**SEDENA/SEMAR/FGR/ANAM → Centro dio NEGATIVO declarado** (ningún comunicado propio y fechado en ventana;
estas corporaciones solo aparecen integradas en operativos conjuntos). **Mesas de Construcción de la Paz
→ Golfo dio el primer POSITIVO de la serie**: Veracruz **sí tiene portal propio**, Tabasco **no**.
**Un negativo declarado también es resultado: evita repetirlo.**

- **SEDENA / SEMAR / FGR / ANAM regionales → NORESTE.**
- **Mesas de Construcción de la Paz → NOROESTE** (Veracruz y Tabasco ya resueltos; **falta saber si
  Sinaloa, Chihuahua, Durango, Sonora, BC y BCS tienen portal de mesa**).
- **Dominios institucionales de Hidalgo y Puebla → CENTRO.** **Tercera edición sin confirmarse por
  `site:`**: resuélvalo o decláre­lo vacío acreditado.

### 3.3 Los seguimientos que más rinden

1. ⚠️ **CHIHUAHUA — EL AEI ASEGURADO ÍNTEGRO FUERA DE LA SERIE DE ZACATECAS.** *Seguimiento de máxima
   prioridad, y es nuevo.* **Dos búsquedas.**
   `ARG-115-003`: artefacto explosivo casero asegurado el **2-sep en la col. Villas del Real**, Chihuahua
   capital, con **4 detenidos** y **uniformes e insignias de la Dirección de Seguridad Pública Municipal**.
   **Sin tipo, carga ni sistema de iniciación publicados.**
   **Por qué importa**: hasta ARGOS 115 la única pieza íntegra del archivo era el **niple de Piedra Gorda**.
   **Ahora hay dos, en entidades sin relación, y ninguna caracterizada.**
   Qué buscar: **peritaje del artefacto** · **auditoría del inventario de prendas de la DSPM** —extravío,
   baja o sustracción— · **serie del revólver .32**, que es la pieza con mayor probabilidad de tener
   propietario registrado.
   ⚠️ **Y hay una cifra en disputa abierta**: los cartuchos cal. .45 circulan como **13, 23 y 36** entre
   seis regionales. El arbitraje halló «13» y «adicionalmente 23». `NO SE ARBITRA` hasta boletín.
2. ⚠️ **ZACATECAS — LA FENAZA, DEL 4 AL 20 DE SEPTIEMBRE.** **Dos búsquedas.**
   **787 elementos** —100 Ejército, 120 GN, 100 Policía Estatal Preventiva, 80 FRIZ— con **dispositivo
   específico de detección de explosivos**, en la entidad con **cuatro municipios atacados con explosivo
   en el año**. **La contramedida está declarada: el propio Estado reconoce el riesgo.**
   **El indicador a vigilar es si aparece artefacto en zona de concentración masiva**, que sería el salto
   de medio que la serie no ha dado. **La ventana de ARGOS 116 cae dentro de la feria.**
3. ⚠️ **ZACATECAS — LA SERIE DE EXPLOSIVOS, ahora con DOS vacíos declarados por la autoridad.**
   *Máximo DOS búsquedas en total para las dos preguntas.*
   **(a)** El **niple de Piedra Gorda** (`ARG-113-ARM-003`) **sigue sin dictamen, tercera edición** —pero
   **cambió de naturaleza**: la propia Fiscalía **declara que aún no determina tipo de explosivo ni
   mecanismo**. **Es vacío declarado por el emisor, no falta de búsqueda.** **DESLINDE QUE HAY QUE
   CONSERVAR**: lo peritado y publicado es el **coche bomba EMPLEADO en Ojocaliente**; son dos objetos
   y el resumidor los devuelve juntos.
   **(b)** **Ninguno de los dos detenidos tiene vinculación a proceso, cuarta edición.**
   William Ariel «N» (18) sigue **entregado a la FGR** sin causa penal; Juan Pedro «N» (29), sin novedad.
   ⚠️ **SON DOS DETENCIONES DISTINTAS** —30-ago en Asientos, Aguascalientes; 1-sep en Piedra Gorda,
   Cuauhtémoc, Zacatecas—. **No las funda.**
   ⚠️ **RESUELTO EN ARGOS 115, NO LO VUELVA A BUSCAR**: el «cuatro ataques del año» **cuenta MUNICIPIOS**
   —Villa García, Tabasco, Luis Moya, Ojocaliente—, **no eventos**; **por evento son CINCO**, porque
   **Luis Moya tiene dos**. **No funda la lista de explosivos (4 municipios) con la de agresiones a
   policías de la FGJEZ (7 municipios): son universos distintos.** **Y el accionador de Villa García es
   vacío acreditado: no gaste búsqueda salvo peritaje publicado.**
4. ⚠️ **NACIONAL — EL CORREDOR AGUASCALIENTES–ZACATECAS YA ESTÁ ACREDITADO.** **Una búsqueda.**
   `ARG-115-007`: **«El Niño Concepción»**, detenido en **Cosío**, es el **tercer detenido en dos semanas
   que cruza el eje y el primero con carpetas en LAS DOS entidades** —doble homicidio en San Francisco de
   los Romo y otro en Zacatecas—. Los dos anteriores solo eran *originarios* de Aguascalientes.
   Qué buscar: **si aparece en la estructura que la FGJEZ atribuye a la serie de explosivos**. Lo demás
   —expediente único, cruce de telefonía— **es consulta documental, no búsqueda web**.
5. **CHIAPAS — LA TRINITARIA, el candidato de mayor volumen pendiente.** **Una búsqueda.**
   **2 armas largas, 920 cartuchos, 34 cargadores**, Ejército, 91.º Batallón de Infantería.
   **Sin fecha en URL ni en titular**; el resumidor dice «hace 3 días». `FECHA NO FIJADA — NO INTEGRAR`.
   **Lo cierra una URL fechada.**
6. **JUDICIAL — dos candidatos, una búsqueda cada uno como máximo.**
   **(a) Teotihuacán, Edomex**: `PENDIENTE DE CONFIRMACIÓN OFICIAL`, **tercera edición**. Constan
   **cuatro nombres** (Jesús Cortés Flores, Jonás Baltazar García, Jorge Javier Arenas Mendoza,
   Octaviano Néstor Nochebuena), **multa de $292,160 «cada uno»**, hecho de **dic-2016**, CEFERESO N.º 1.
   ⚠️ **Los campos individualizadores identifican el caso; NO acreditan la resolución.**
   ⚠️ **`PENA COMPUESTA`: el «cada uno» es de la MULTA, no de la PRISIÓN.** Si es por persona el
   acumulado sube 200 años; si conjunta, 50. **Lo cierra el comunicado de la FGR, y solo eso.**
   **(b) Puebla · «operativo con dos detenidos y un agresor abatido»**: titular suelto sin fecha.
   ⚠️ **Si hubo abatido requiere ficha propia 🟡 o 🔴 según quién inició.**
   ⚠️ **NO gaste búsqueda en las tres sentencias de la FGR Sinaloa: RETIRADAS DEFINITIVAMENTE en
   ARGOS 115 por umbral, segunda edición sin fragmento citable.** Ver Bloque 4.
7. ⚠️ **NO gaste NINGUNA búsqueda en**: **protección balística** (conclusión permanente: **41 placas
   acumuladas**, ninguna con marca, nivel NIJ ni lote) · **el municipio administrativo de Agua Verde**
   (cerrado: es **Rosario**) · **«16 detenidos y 22 armas»** (cerrado: dos eventos distintos) ·
   **Tabasco «26 detenidos»** (cerrado: junio) · **Coatzacoalcos–Villahermosa** (cerrado: **Huimanguillo**,
   81 kg) · **Bocoyna/Maguarichi** · **San Miguel de Allende** · **Poza Rica** · **Pedernales** ·
   **Tlaxcala** y **FGE Veracruz** · disputa forestal Michoacán/Guerrero · **«El Dron»** ·
   Querétaro `ARG-109-005` · **Petatlán y Totolapan** · **Loxicha** (homónimo de 2023 ya descartado) ·
   **Matamoros serie y marcaje** (tres ediciones en `SIN AVANCE`) · **el accionador de Villa García**
   (vacío acreditado) · **el origen aguascalentense de los dos detenidos** (resuelto e integrado).
   ⚠️ **PERO RECUERDE LA REGLA: estas prohibiciones van contra el PENDIENTE, no contra el TOPÓNIMO.
   Si aparece un hecho NUEVO, en ventana, en cualquiera de esos lugares, SE INFORMA Y SE FICHA.**
8. **Una sola búsqueda, y solo si sobra**: Valdez Mainero (`ARG-114-REC-001`) · el componente extranjero
   de Rosario (`ARG-114-002`) · la sucesión del Cártel de Los Reyes (Tocumbo, Los Reyes, Peribán) ·
   la contradicción de lesionados de `ARG-110-001` (**sexta edición sin arbitrar**) ·
   los 39 vehículos de «El Amarillo» (`ARG-115-002`).

### 3.4 `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verifíquelo cada corte

**Verificado de nuevo en ARGOS 115**: la migración **está acreditada** —desde el 1-sep los reportes
diarios de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí para las 32 entidades—
pero **ningún reporte resultó alcanzable**: **el dominio está indexado y sus rutas no llevan fecha**, y
**la trampa de año persiste**. **Tercera edición sin usar ninguna cifra suya.**
**Verifíquelo cada corte, declare el resultado y no use ninguna cifra suya** mientras persista.

---

## BLOQUE 4 — EL HALLAZGO JUDICIAL QUE CAMBIA CÓMO SE BUSCA UNA SENTENCIA

⚠️ **EL RESUMIDOR DEL BUSCADOR FABRICA NÚMEROS DE COMUNICADO DE LA FGR.** Es el hallazgo de método más
importante que hereda ARGOS 116, y **generaliza la retractación de ARGOS 114**, que se había tratado
como un caso aislado. **No lo era.**

En ARGOS 115, **tres regiones independientes y el coordinador** localizaron el mismo defecto en
**cinco entidades**:

| Comunicado atribuido | Entidad |
|---|---|
| `DPE/3852`, `DPE/3849`, `DPE/3850` de 2026 | Sinaloa |
| `DPE/3897/2026` | Campeche |
| `DPE/3893/2026` | San Luis Potosí |
| `DPE/3855` a `DPE/3857` de 2026 | Estado de México |
| `DPE/3888`, `DPE/3889` de 2026 | Puebla |

**La verificación con cadena exacta entre comillas devuelve siempre lo mismo**: páginas índice de
**portales espejo de la FGR sin fecha propia** —`alertaamber`, `hasvistoa`, `inacipe`, `renadet`, `bndf`,
`historicopgr`— y **comunicados REALES de otros años** con el mismo molde de título: `DPE/3076/2022` y
`DPE/3016/2022`, **ambos de Tlaxcala**, «FGR obtiene sentencia condenatoria contra una persona por
portación de arma de fuego».

**Diagnóstico**: el molde de título **es real** y la FGR lo reutiliza desde al menos 2022 en decenas de
delegaciones. **El buscador lo completa con una delegación y un correlativo plausibles, y lo fecha en el
día de la consulta.** **La precisión del número es exactamente lo que lo hace creíble.**

> ⚠️ **REGLA OPERATIVA**: **un número de comunicado `DPE/…` que no aparezca literalmente en un TITULAR o
> en una URL no identifica ningún documento, por preciso que parezca.** La comprobación correcta es
> **una búsqueda con la cadena exacta entre comillas**, y **su resultado negativo es evidencia
> reproducible que vence al arbitraje del coordinador**.

**Efecto evitado**: de haberse aplicado el umbral del módulo de armamento —que admite confianza Bajo—,
**ARGOS 115 habría publicado cinco condenas inexistentes con delegación y número de comunicado**.
**La asimetría de umbrales entre armamento y sentencias que `CLAUDE.md` declara deliberada se ha pagado
sola dos ediciones seguidas.**

---

## BLOQUE 5 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes de
ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla de `site:`** de la 3.1 y **el tope
duro de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta sin
  restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Sexta edición consecutiva.
  **No es opcional**, aunque los barridos rindan más en ventanas largas.
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS Y SOBRE SUS EXCLUSIONES.** Ver Bloque 6.

⚠️ **Y REVISE TODA EXCLUSIÓN QUE UN BARRIDO ATRIBUYA A UNA INSTRUCCIÓN SUYA.** Es el modo de fallo de
ARGOS 114 y sigue vigente: **las prohibiciones de gasto se redactan contra el PENDIENTE, no contra el
TOPÓNIMO.**

⚠️ **Y HAGA EL `grep` DE ARCHIVO SOBRE LO QUE LOS BARRIDOS TRAIGAN, no solo sobre lo que este archivo
enumera.** Es la lección de ARGOS 115 y está en el Bloque 2.

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte. **En ARGOS 115 el resumidor fechó una emboscada a militares el «26 de septiembre de 2026», tres semanas en el futuro** |
| ⚠️ **UN AGREGADO ESTATAL PUEDE REEMPAQUETAR UN HECHO YA PUBLICADO SIN FECHARLO — trampa NUEVA de ARGOS 115, y la que más costó** | La Secretaría de Seguridad y Paz de Guanajuato difundió el **3-sep** una jornada de **cuatro municipios** que **incluía, sin fecharlo, un aseguramiento del 31-ago ya publicado y ya contabilizado** (`ARG-113-003`). **La fecha en la ruta era correcta: era la de publicación.** Coincidencia en **ocho criterios** —municipio, localidad, nombre, edad, arma, calibre, cartuchos, cargadores—. **Habría sido doble conteo ENTRE ediciones**, no republicación de titular. **REGLA: todo agregado por jornada de difusión se coteja contra el archivo por MUNICIPIO Y POR NOMBRE, no por titular** |
| ⚠️ **UN CONTROL PUEDE OBLIGAR A INTEGRAR, NO SOLO A RETIRAR** | **Primera vez en la serie que un control AUMENTA un total.** `procedencia-cifras` acreditó que en Villas del Real faltaba **un revólver cal. .32** además del arma .45: **armas cortas 1 → 2**. **Encargue los controles en las dos direcciones**: es lo que `CLAUDE.md` pide y rara vez se ejercita |
| ⚠️ **«VERIFICADO EN DOS CONSULTAS INDEPENDIENTES» NO SIGNIFICA NADA SI LAS DOS SON AL MISMO BUSCADOR** | **Una verificación cuenta SOLO si devuelve un TITULAR, ENCABEZADO o URL que CONTENGA el dato.** Si vive únicamente en el párrafo de respuesta del motor, **NO EXISTE**. **Repetir la pregunta confirma al resumidor, no al hecho.** Ver Bloque 4: en ARGOS 115 esto se generalizó a **cinco entidades** |
| ⚠️ **El arbitraje del coordinador también se equivoca — pero en ARGOS 115 no lo hizo** | En ARGOS 114 integró tres sentencias que un control tumbó con razón. **En ARGOS 115, cuando los DOS controles lo contradijeron, arbitró con `grep` y búsqueda propios y les dio la razón a los dos.** **La regla se mantiene: arbitrar antes de obedecer, y cuando un control aporte evidencia reproducible —una cadena exacta que no devuelve nada, o un `grep` que devuelve el hecho— esa evidencia VENCE al arbitraje** |
| ⚠️ **Un indicador de cobertura del CARTELÓN no puede contar lo que el cartelón no publica** | Corregido en ARGOS 114 en el indicador de entidades y **reaparecido en ARGOS 115 en el total de armamento**: Veracruz se contaba entre los «eventos cualitativos» **sin tener ficha ni fila**. **Compruebe los DOS renglones, no solo el indicador** |
| ⚠️ **Trampa de *slug* sin fecha en `fiscalia.chihuahua.gob.mx`** | Sus boletines **no llevan fecha en la ruta**: un cateo del **19-jun** entró como candidato de septiembre y solo se descartó por **cuatro URL de republicadores con fecha**. **Exija ancla de republicador fechado** |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | `grep` del topónimo de localidad, no solo de municipio. «Cuauhtémoc» es Zacatecas, Chihuahua Y CDMX · «Matamoros» Tamaulipas Y Coahuila · «Los Reyes» Michoacán Y Edomex · «Rosario» Sinaloa · «Villa de La Paz» es **San Luis Potosí, no Guerrero** |
| ⚠️ **Dos objetos del mismo caso que el resumidor funde** | **El artefacto EMPLEADO y el ASEGURADO de la serie de Zacatecas.** Buscar «peritaje» devuelve el dictamen del **coche bomba empleado**, no del **niple asegurado**. **Lea qué objeto peritó el dictamen** |
| ⚠️ **El AEI empleado no es AEI asegurado** | Los tres primeros de la serie de Zacatecas **fueron usados contra la autoridad**: van al semáforo, **no al conteo**. El de Piedra Gorda y **el de Villas del Real, Chihuahua** **sí fueron asegurados y sí cuentan** |
| ⚠️ **Pena compuesta** | «50 años para los cuatro» **no es sumable**. ⚠️ **En Teotihuacán el «cada uno» está publicado de la MULTA, no de la PRISIÓN** |
| ⚠️ **«Más de» no es cifra** | **«Más de seis años», «más de 60 vehículos» no son cifras y no se redondean.** En ARGOS 115 dejó a Veracruz fuera del cartelón pese a haber publicado en ventana |
| ⚠️ **Sentencia frente a vinculación a proceso** | La FGR publica ambas el mismo día con títulos parecidos. **Lea el verbo del título** — y compruebe que el título EXISTE. **«Mandar a la cárcel» no es término de condena** (Tamaulipas, ARGOS 115) |
| ⚠️ **Dos casos de la misma fiscalía, el mismo día** | **Municipio, delito y pena coincidentes NO identifican un caso**: hacen falta **dos campos individualizadores**. **Y la PENA no individualiza en delitos con alto uso de abreviado** |
| ⚠️ **Corroboración asimétrica** | **El nivel de confianza de una fila lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo. En ARGOS 115 bajó de Medio a Bajo la fila de Villas del Real por los cartuchos en disputa, pese a tener seis fuentes coincidentes en todo lo demás |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado ocho ediciones. En ARGOS 115: **2-sep miércoles, 3-sep jueves, 4-sep viernes**; el **28-ago fue viernes** (Valdez Mainero) |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y **no basta como fuente única**. **En ARGOS 115 un solo *liveblog* del 3-sep presentó como del día un hecho de DICIEMBRE DE 2025 (Navolato) y otro de MAYO DE 2026 (Tláhuac)** |
| **Trampa de año en el propio dominio oficial** | `morelos.gob.mx` devolvió un narcolaboratorio de **octubre de 2025**. `gabinetedeseguridad.gob.mx` ya lo había hecho |
| **Agregado que no se reparte** | Un balance de varios días **no se distribuye** en una ventana. En ARGOS 115 se aplicó a **Nayarit** (9,688 cartuchos, **la mayor cifra del corte, no sumada**) y a Coahuila |
| **Cifra no exacta** | «más de», «alrededor de» **no es cifra**. **Pero busque la exacta** |
| **Capacidad declarada** | «cargadores de 20 cartuchos cada uno» **no** se convierte en cartuchos |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. **Y compruebe la aritmética**: en ARGOS 115, 127 ÷ 2 = **63,5**, no 63 |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. En ARGOS 115 se declaró en el boletín federal del 2-sep, en el informe del Gabinete y en el agregado de Nayarit |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria** |

**Egreso bloqueado, vigesimoséptima edición.** `curl` contra `*.gob.mx` devuelve
**`curl: (56) CONNECT tunnel failed, response 403`**; `WebFetch` devuelve `EGRESS_BLOCKED`
—**y en ARGOS 115 también contra dominios de medios regionales**—.
**Cero portales por acceso directo.** Techo de confianza: **★★★★☆**.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar. **Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige lectura
directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las casillas deben CUADRAR con las 32 entidades.** ARGOS 115 cuadró **dos veces**: nacional
**8 + 23 + 1 + 0 = 32** y judicial **0 + 30 + 1 + 1 = 32**.

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  **Máximo cinco líneas** en cada **Explotación ARGOS** (numeradas 1. a 5.), en cada **recuadro
  `alerta contexto`** y en la **Valoración**. La portada lleva **UN SOLO recuadro**, «LO QUE DEBE SABER EL
  MANDO». **«Hecho confirmado» va en registro telegráfico** —fecha · lugar · corporación · cifras ·
  reservas, separado por `·`—, no en prosa. **«Corroboración» es una lista de emisores por tipo.**
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes, deslindes
  ni marcas de reserva. Se recorta la prosa, no el dato.**
  **ARGOS 115 lo cumplió en los 16 bloques**, verificado con un contador automático.
- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con ARG-ID
  `-REC-`, **ventana de origen declarada** y **fuera de todos los totales**.
  **ARGOS 115 no publicó ninguna** y no la necesitaba.
  ⚠️ **Y un hecho YA PUBLICADO en una edición anterior no vuelve como `-REC-`: eso es duplicación.**
  Lo nuevo sobre él va a **fe de erratas**.
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID `-FE-`
  **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 115 cumplió**: **siete `-FE-`
  registrados, cero en el cartelón y cero en la móvil**, verificado por control automático.
  ⚠️ **Cuidado al citar un deslinde: escribir un `-FE-` dentro de una ficha mete un `-FE-` en el cartelón.**
  **Cite «el corte anterior», no el ARG-ID** —salvo que sea un ARG-ID de hecho, como `ARG-113-003`, que sí
  puede citarse.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha** con
  enlace `#ARG-ID` y aporta **campos distintos**.
- **Toda cifra en cero lleva al lado el dato que la explica.** Tarjetas de armamento con **doble cifra
  rotulada** y **leyenda encima del bloque**; la línea inferior es **cálculo propio** y se declara.
  **ARGOS 115 usó seis recuadros explicativos**, entre ellos **por qué la mayor cifra de munición del
  corte no está en el total** y **por qué el umbral de sentencias es más alto que el de armamento**.
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura van al archivo de fuentes.
  **No mida en «ediciones» dentro del cartelón**: mida en fechas.
- **Conclusiones de inteligencia criminal**, no de método.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.** Use `<div class="alerta contexto">…`.
- ⚠️ **Cada sentencia integrada lleva ficha propia con sus apartados.** ARGOS 115 no integró ninguna.

### Estructura de páginas que hereda ARGOS 116

**Ocho páginas**, como salió ARGOS 115: portada · crimen organizado (I) a (IV) · armamento · sentencias ·
valoración y conclusiones. ARGOS 114 usó siete con página de recuperaciones.
**Si el volumen lo pide, se reparte entre más páginas: nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en TODAS las páginas (8 en ARGOS 115).
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.
#    ⚠️ AL EXTRAER LA PLANTILLA: la etiqueta <body> está en la línea 429 del escritorio anterior,
#    NO en la 428. En ARGOS 115 un desfase de una línea la dejó fuera y hubo que reinsertarla.
#    Compruebe SIEMPRE que haya exactamente una.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 116 <FECHA> 115 2026-09-04 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
#    En ARGOS 115 se corrigió el generador: perdía el numeral de la página (IV).
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.** Entre `EVENTOS_ARM` y
`SIZE_R` viven **`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL` y
`GRIS`**. ARGOS 112 los dejó fuera y **el cartelón habría cargado con el radar y el mapa rotos**.

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes es
«Occidente» en la tabla** aunque el barrido lo cubra Noreste. Un `region:` mal puesto **coloca el eco del
radar en el sector equivocado y nadie lo nota**.

**Comprobación de coherencia obligatoria** —ARGOS 115 la ejecutó como un solo script de Python y conviene
reutilizarla—: extraer el bloque de datos del `<script>` **hasta `const SIZE_R`**, hacer `node --check`, y
validar que **las siete constantes están presentes**, que **cada `estado:` existe en `MEXICO_PATHS`**, que
**cada `region:` coincide con `STATE_REGION`**, que **ninguna fecha cae fuera de la ventana**, que **no hay
ARG-ID duplicados** y que **el semáforo derivado de `EVENTOS` coincide con los contadores tecleados en la
portada y en `radar-stats`**.

⚠️ **Y añada el contador automático de la regla de cinco líneas**, que ARGOS 115 usó sobre los 16 bloques:
cuenta `<b>N.` dentro de cada `EXPLOTACIÓN ARGOS` y de cada `alerta contexto`.

⚠️ **Y RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS, no desde el borrador.** En ARGOS 115 los
dos controles cambiaron **seis renglones del total** y el recálculo independiente fue lo que confirmó el
cuadre final.

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en ambas
versiones · toda tabla envuelta **exactamente una vez** en el escritorio · **cero `-FE-` en ambas** · cero
`sem-item` fuera de portada · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio en la
móvil (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) · **pie con número, fecha y hora en todas las
páginas del escritorio** · **todos los ARG-ID del escritorio presentes en la móvil** · sin desbordamiento
horizontal a 390 px.

*Notas del generador, que NO son defectos*: la móvil **no lleva `<script>`** · **`table-wrap` aparece en
cero** —el generador lo renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**, de modo que **`<table>` puede aparecer en CERO en la móvil sin que se pierda un solo
dato**. **Verifíquelo contando ARG-ID, no etiquetas `<table>`.** · La móvil lleva **un solo pie**.

---

## BLOQUE 9 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo y que las casillas de cobertura no cuadren con las 32 entidades |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **y que se descarte por precaución una que sí debía integrarse** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **DÉCIMA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES DE LOS DOS CONTROLES, Y LA DE MAYOR IMPACTO SOBRE
LAS CIFRAS DESDE ARGOS 105.** En ARGOS 115 **los dos devolvieron `CORREGIR ANTES DE PUBLICAR` y los dos
tenían razón**: entre ambos cambiaron **seis renglones del total nacional**.
**Sin ellos, la edición habría publicado un total inflado en armas largas, cartuchos, cargadores y
detenidos, y corto en armas cortas.**
Si el destinatario no autoriza subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la
ausencia en el indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una búsqueda o
un `grep` de arbitraje antes de obedecerlo**, y **un control puede obligar a INTEGRAR lo que el borrador
descartó por precaución** —en ARGOS 115 añadió un arma que faltaba—. **Ni obedecer ni descartar por
precaución: arbitrar.** **Y cuando el arbitraje confirme al control, dígalo.**

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos
**y sobre sus propias instrucciones**. En ARGOS 115 **interceptó tres de los cuatro falsos positivos** y
**produjo la evidencia negativa reproducible del Bloque 4**.

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al cartelón
   pero sí al índice. **Y retirar del índice los ARG-ID que se hayan quedado sin usar por una corrección**,
   como `ARG-115-ARM-003`.
3. **Escribir `reports/_arranque-ARGOS-117.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
