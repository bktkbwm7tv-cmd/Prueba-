# ORDEN DE ARRANQUE — ARGOS 115

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 114** (corte 2026-09-02).

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

**Estado que debe encontrar ARGOS 115**: última edición `argos-2026-09-02` (ARGOS 114), **87 archivos**
en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló OCHO ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 114 mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición
> —**ocho ediciones por detrás**— y **no contenía su propio archivo de arranque**: numerar por lo que la
> rama tenía a la vista habría producido **un falso «ARGOS 107» con ventana solapada de más de una semana**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Edición** | **ARGOS 115** |
| **Ventana** | **desde 2026-09-02 10:17 CDMX** (cierre de ARGOS 114) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-116.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de solape.
**Verifique la hora, no la suponga.**

⚠️ **TRES VENTANAS CONSECUTIVAS DECRECIENTES: 48 h → 27 h → 21 h.** ARGOS 114 fue **el intervalo más corto
de la serie** y su volumen lo refleja: **11 armas largas y 2 eventos de aseguramiento**. **Ninguna edición
es comparable con otra sin normalizar por duración de ventana**, y ARGOS 114 lo declaró en el cartelón
como advertencia de comparabilidad y en la Valoración. **Declárelo también si su ventana es corta, y
conviene fijar horas de arranque más estables para que la serie recupere comparabilidad.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-02-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.
   ⚠️ **El `grep` debe hacerse por TOPÓNIMO DE LOCALIDAD, no solo por entidad y municipio.** En ARGOS 114
   devolvió **`ARG-112-005` y `ARG-102-REC-001` para «Agua Verde»** y obligó a un deslinde que el cartelón
   publica: **tres hechos distintos en la misma localidad en trece días**. Y confirmó que **«Luis Moya» y
   «Valdez Mainero» no tenían NINGUNA entrada**, lo que los acreditó como genuinamente nuevos.
   **Séptima edición consecutiva en que el archivo resuelve lo que la web no.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 115 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. QUINTA EDICIÓN COMO PASO DE
MAYOR RENDIMIENTO.**

| Origen del hecho | ARGOS 111 | ARGOS 112 | ARGOS 113 | **ARGOS 114** |
|---|---|---|---|---|
| Barridos regionales | 4 de 6 | 3 de 7 | 4 de 6 | **3 de 8** |
| **Recall y arbitraje del coordinador** | 2 de 6 | 4 de 7 | 2 de 6 | **5 de 8, incluidos el hecho de apertura y las tres sentencias** |

En ARGOS 114 el recall trajo **la activación del Plan DN-III-E y el compromiso presidencial de informe
desde Zacatecas**, que **ningún barrido regional vio**. **La razón es estructural: un hecho nacional de
gran cobertura se busca mejor por tema que por entidad, y los barridos están organizados por entidad.**

⚠️ **EL ARBITRAJE DEL COORDINADOR RINDIÓ TRES VECES Y EN LAS DOS DIRECCIONES.** Ver Bloque 5. **Es el
control que no es un subagente y por tercera edición seguida el que más cambia el producto.**

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene tres preguntas, el tope es
**de tres en total, no de tres por pregunta**. En ARGOS 114 se respetó en los siete ejes.
**Cerrar un seguimiento en `SIN AVANCE` es el resultado correcto cuando no hay dato.**

✅ **LA REGLA DE `site:` FUNCIONA. EL OBJETIVO PORCENTUAL QUEDA RETIRADO DEFINITIVAMENTE — NO LO
REINTRODUZCA.**

> **`site:` SOLO contra dominios con fecha en la ruta; contra los demás, consulta genérica.**

Primera edición aplicándola: **4 consultas `site:` de 76 (5 %)**, y **las cuatro contra dominios fechados**
—`seguridad.slp.gob.mx`, `boletines.guanajuato.gob.mx`, `fiscaliageneralqro.gob.mx`—. Una produjo un
**descarte firme** (Querétaro, boletín más reciente indexado del 26-ago), que convierte su `SIN RESULTADO`
en **demostrable** en vez de supuesto. **La genérica subió al 95 % y eso es el comportamiento correcto**,
no una desviación: con pocos dominios fechados disponibles, la genérica sube sola. **No mida esto con un
porcentaje objetivo.**

**Dominios con fecha en la ruta — no los redescubra**: Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/` ·
Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` · Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/` ·
San Luis Potosí `seguridad.slp.gob.mx/noticias/AAAA/M/D/` · Veracruz `veracruz.gob.mx/AAAA/MM/DD/`
(**útil: es la vía de Veracruz, no la FGE**) · ⚠️ **`fiscaliaguerrero.gob.mx/index.php/AAAA/MM/DD/` —
NUEVO de ARGOS 114, hallazgo de método de Sureste, SIN EXPLOTAR. Asígnelo a Sureste.**
**Sin fecha en la ruta (use genérica)**: Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa `fiscaliasinaloa.mx` ·
Chihuahua `fiscalia.chihuahua.gob.mx` y `sspe.chihuahua.gob.mx` (⚠️ `ssp.chihuahua.gob.mx` es FALSO) ·
Colima `fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` · Edomex `fgjem.edomex.gob.mx` ·
BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` · Coahuila `sspcoahuila.gob.mx` ·
Aguascalientes `aguascalientes.gob.mx/ssp/` · Puebla `ssp.puebla.gob.mx` · Tabasco `fiscaliatabasco.gob.mx` ·
Morelos `morelos.gob.mx/ultimas-noticias` (⚠️ **trampa de año verificada: devolvió un narcolaboratorio de
octubre de 2025 a una consulta de septiembre de 2026**).

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** · **FGE Veracruz** (cinco cortes de agregados sin
individualizar; **la vía útil en Veracruz es la FGR y el portal del gobierno estatal**) ·
**`ssypc.nayarit.gob.mx`**. **No publican indexable**: FGJ Nuevo León · SSP Zacatecas ·
**`fgjsonora.gob.mx` (QUINTA edición sin resultado: decida de una vez si se declara vacío acreditado o se
le asigna una consulta dedicada)**.

### 3.2 Cobertura — qué encabeza el triaje y a quién se le asigna la deuda

**No queda ninguna entidad `NO REVISADA`: el ciclo se aplica limpio, sin prioridad de saldo.**

**A ARGOS 115 le toca el CICLO B — Noreste + Golfo** encabezando el triaje judicial; las otras cuatro
encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

⚠️ **DIRIJA EL TRIAJE JUDICIAL A LAS DELEGACIONES DE LA FGR ANTES QUE A LAS FISCALÍAS ESTATALES. CUARTA
EDICIÓN CONSECUTIVA EN QUE LA PRODUCCIÓN JUDICIAL INTEGRABLE DEL PAÍS ES FEDERAL**: FGR Papantla (112),
FECOR Puebla (113) y **ARGOS 114: cero integrables, tras retractar tres candidatos sin fragmento citable**. **Las 32 fiscalías estatales
dieron cero por tercer corte seguido**, y la causa está acreditada: **su ciclo de publicación es más lento
que una ventana corta**. **No retire el ciclo por un resultado negativo**: su función es hacer
**demostrable** el `SIN DATO`, no garantizar hallazgo.

⚠️ **MANTENGA LA ASIGNACIÓN EXPLÍCITA DE LA DEUDA REGIONAL, EN ROTACIÓN.** En ARGOS 114,
**SEDENA/SEMAR/FGR/ANAM → Noroeste produjo el mayor aseguramiento del corte**; **Mesas de Construcción de la Paz →
Occidente dio resultado NEGATIVO declarado** (ninguna de las seis entidades tiene portal de mesa con
desglose equivalente al de Morelos). **Un negativo declarado también es resultado: evita repetirlo.**

- **SEDENA / SEMAR / FGR / ANAM regionales → CENTRO.**
- **Mesas de Construcción de la Paz → GOLFO.**

### 3.3 Los seguimientos que más rinden

1. ⚠️ **ZACATECAS — EL ARTEFACTO SIGUE SIN PERITAR Y LUIS MOYA SON DOS ATAQUES, NO UNO.**
   *Seguimiento de máxima prioridad. Máximo TRES búsquedas en total.*
   **(a) El artefacto.** El **niple asegurado e íntegro** de Piedra Gorda (`ARG-113-ARM-003`) **sigue sin
   dictamen publicado, segunda edición**. ⚠️ **DESLINDE QUE HAY QUE CONSERVAR**: lo que sí se peritó y se
   publicó es **el coche bomba EMPLEADO en Ojocaliente** —«los peritajes determinaron que se trató de un
   coche bomba»—. **Son dos objetos distintos y el resumidor los devuelve juntos.** Precedente en contra
   vigente: **55 artefactos destruidos *in situ* en el sur de Sinaloa sin caracterizar ninguno**.
   **(b) Luis Moya.** **HALLAZGO DE ARGOS 114: no es un ataque, son DOS**, y el archivo no tenía ninguno.
   **5-mar-2026** (~18:00, Comandancia, **3 uniformados heridos**; Proceso e Infobae, fecha en la ruta) y
   **31-jul/1-ago-2026** (noche, comunidad de **Barranquilla**, **1 policía municipal MUERTO** y 2 heridos;
   La Jornada y El Financiero, fecha en la ruta). **No consta cuál cuenta en el «cuatro del año» oficial.**
   ⚠️ **NO vuelva a fundir dos listas de emisores distintos**: la de **explosivos** (4 municipios) y la de
   **agresiones a elementos policiacos** de la FGJEZ (**7 municipios**: Valparaíso, Fresnillo, Villanueva,
   Jerez, Ojocaliente, Luis Moya y Villa Hidalgo) **son universos distintos**.
   **Las cuatro cifras de balance siguen contradichas y el hallazgo de Luis Moya las AGRAVA, no las
   resuelve.** Lo cierra un corte de la FGJEZ **con criterio de conteo explícito**.
   **(c) La obligación de calendario, ya vencida**: la Presidencia comprometió **informe de Gobernación el
   jueves 3-sep** y **del Gabinete de Seguridad desde Zacatecas el viernes 4-sep**. **ARGOS 115 debe
   verificar si se rindieron y qué desglose traen.** Es la vía más probable de resolver (a) y (b) de un golpe.
2. ⚠️ **LOS DOS DETENIDOS, Y AGUASCALIENTES COMO ORIGEN.** **Dos búsquedas.**
   **RESUELTO E INTEGRADO en ARGOS 114**: **ambos son originarios de Aguascalientes** —Juan Pedro «N» (29)
   con **fuente institucional** `zacatecas.gob.mx`; William Ariel «N» (18) con **tres nacionales y una
   regional**—. **No lo vuelva a buscar: búsquelo hacia adelante.**
   **Sigue abierto**: **ninguno tiene vinculación a proceso publicada, tercera edición**. **Dato nuevo:
   William Ariel «N» fue ENTREGADO A LA FGR** —cambio de fuero—, sin causa penal difundida.
   **Y el accionador de Villa García sigue sin explotación técnica publicada, tercera edición**: mecanismo
   confirmado (detonación remota por los propios sospechosos) pero **sin identificadores de fábrica, marca
   ni tipo**. **Una búsqueda por edición como máximo.**
   ⚠️ **SON DOS DETENCIONES DISTINTAS** —30-ago en Asientos, Aguascalientes; 1-sep en Piedra Gorda,
   Cuauhtémoc, Zacatecas—. **Dos barridos las fusionaron en ARGOS 113. No repita el error.**
3. **SINALOA — EL COMPONENTE EXTRANJERO DE ROSARIO** (`ARG-114-002`). **Dos búsquedas.**
   **4 colombianos y 1 cubano** de 9 detenidos, más **2 mujeres, una MENOR DE EDAD**. **Es dotación
   importada de personal, no de armamento.** Qué buscar: **situación migratoria y ruta de entrada** de los
   cinco extranjeros · **protocolo aplicado a la menor** · si hay vinculación a proceso.
4. **MICHOACÁN — LA SUCESIÓN DEL CÁRTEL DE LOS REYES.** **Dos búsquedas.**
   **Segunda descabezada en un mes y sin sucesor confirmado**; la cobertura señala expresamente la
   incertidumbre. **La ventana inmediata sigue siendo la de mayor probabilidad de repunte.**
   ⚠️ **El municipio del operativo es TOCUMBO (Rodeo del Pinal), no Los Reyes** —corregido en
   `ARG-114-FE-001`—. Vigilar **Tocumbo, Los Reyes, Peribán** y colindantes.
5. **ESTADO DE MÉXICO — TEOTIHUACÁN, el candidato judicial prioritario.** **Una búsqueda.**
   **4 sentenciados, 50 años, secuestro agravado, multa $292,160 cada uno**, hecho de **diciembre de 2016**,
   CEFERESO N.º 1 «El Altiplano». `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR`.
   **Ya se arbitró en ARGOS 114 y el descarte SE SOSTUVO**: no apareció comunicado de la FGR.
   ⚠️ **Y añada el otro candidato judicial vivo**: las **tres sentencias de la FGR delegación Sinaloa**
   (DPE/3852, DPE/3849, DPE/3850 de 2026, 4 personas), **retractadas por falta de fragmento citable**.
   **Las cierra un titular, encabezado o URL que contenga el número de comunicado**, y solo eso.
   ⚠️ **Y es `PENA COMPUESTA`: la multa se publica «cada uno», la prisión NO.** **Si es por persona el
   acumulado nacional sube 200 años; si conjunta, 50.** **Lo cierra el comunicado de la FGR, y solo eso.**
6. **BAJA CALIFORNIA — VALDEZ MAINERO.** **Una búsqueda.** Publicado en ARGOS 114 como
   `ARG-114-REC-001`. Falta: **carpeta, ficha de búsqueda, hipótesis oficial**. **Cuatro días entre el
   último contacto y la difusión, y la denuncia la impulsó la familia, no la autoridad.**
7. ⚠️ **NO gaste NINGUNA búsqueda en**: **protección balística** (conclusión permanente: **41 placas
   acumuladas**, ninguna con marca, nivel NIJ ni lote) · **«16 detenidos y 22 armas»** (cerrado: son dos
   eventos distintos) · **el municipio de Agua Verde** (cerrado: es **Rosario**) · **Tabasco «26 detenidos»**
   (cerrado: es de junio) · **Coatzacoalcos–Villahermosa** (cerrado: **Huimanguillo**, 31-ago, **81 kg**) ·
   **Bocoyna/Maguarichi** · **San Miguel de Allende** · **Poza Rica** · **Pedernales** · **Tlaxcala** y
   **FGE Veracruz** · disputa forestal Michoacán/Guerrero · **«El Dron»** · Querétaro `ARG-109-005` ·
   Petatlán y Totolapan · **Matamoros serie y marcaje** (dos ediciones en `SIN AVANCE`).
8. **Una sola búsqueda, y solo si sobra**: Loxicha (`ARG-109-002`) · Chihuahua `ARG-111-004` ·
   la contradicción de lesionados de `ARG-110-001` (**quinta edición sin arbitrar**) · la munición sin su
   arma de Acapulco (`ARG-112-006`) · el inhibidor de Puebla (`ARG-113-SEN-001`).

### 3.4 `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verifíquelo cada corte

**Verificado de nuevo en ARGOS 114**: la migración **está acreditada** —desde el 1-sep los reportes diarios
de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí para las 32 entidades— pero
**ningún reporte del 1 ni del 2 de septiembre resultó alcanzable**, ni por búsqueda dirigida ni genérica:
**el dominio está indexado y sus rutas no llevan fecha**. **La trampa de año persiste.**
**Verifíquelo cada corte, declare el resultado y no use ninguna cifra suya** mientras persista.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes de
ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla de `site:`** de la 3.1 y **el tope duro
de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta sin
  restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Quinta edición consecutiva como
  paso de mayor rendimiento. **No es opcional.**
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS Y SOBRE SUS EXCLUSIONES.** Ver Bloque 5.

⚠️ **Y REVISE TODA EXCLUSIÓN QUE UN BARRIDO ATRIBUYA A UNA INSTRUCCIÓN SUYA.** Es el modo de fallo nuevo
de ARGOS 114 y está en el Bloque 5.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| ⚠️ **«VERIFICADO EN DOS CONSULTAS INDEPENDIENTES» NO SIGNIFICA NADA SI LAS DOS SON AL MISMO BUSCADOR — trampa NUEVA de ARGOS 114, y la que más costó** | **ARGOS 114 estuvo a punto de publicar TRES SENTENCIAS INEXISTENTES.** El borrador integró tres condenas de la FGR delegación Sinaloa (comunicados atribuidos **DPE/3852, DPE/3849, DPE/3850 de 2026**, 4 personas sentenciadas) afirmando «título literal verificado en dos consultas independientes». **No lo eran**: eran dos preguntas al mismo resumidor sobre el mismo índice. `procedencia-cifras` repitió la búsqueda **con cadena exacta entre comillas** y obtuvo **cero resultados**: el número de comunicado, la entidad y la fecha **solo existían en el párrafo de respuesta del buscador**; las únicas rutas eran **páginas índice de portales espejo de la FGR sin fecha propia**, y **el único titular real con esa redacción es de BAJA CALIFORNIA** —el molde de título lo reutiliza la FGR en decenas de delegaciones—. **Es el patrón Huajicori.** **REGLA: una verificación cuenta SOLO si devuelve un TITULAR, ENCABEZADO o URL que contenga el dato. Si el dato vive únicamente en el párrafo de respuesta del motor, NO EXISTE.** Y **repetir la pregunta confirma al resumidor, no al hecho** |
| ⚠️ **El arbitraje del coordinador también se equivoca** | **En ARGOS 114 el arbitraje integró los tres candidatos judiciales y un control los tumbó con razón.** La regla «arbitrar antes de obedecer» **se mantiene** —en esa misma edición salvó el mayor aseguramiento del corte—, **pero el arbitraje no es la última palabra: es una búsqueda más y puede fallar como cualquier otra.** **Cuando un control aporta evidencia NEGATIVA reproducible —una cadena exacta que no devuelve nada—, esa evidencia vence al arbitraje** |
| ⚠️ **Un indicador de cobertura del CARTELÓN no puede contar lo que el cartelón no publica** | `editor-duplicidad` detectó que ARGOS 114 declaraba «6 con hallazgo» incluyendo **Michoacán**, cuyo trabajo se resolvió por **fe de erratas** y no por ficha. **Contabilizar una entidad que el lector no puede verificar dentro del propio cartelón viola la auditabilidad.** Corregido a **5 + 26 + 1 + 0 = 32**. **El archivo de fuentes SÍ conserva las 6, y la diferencia entre ambos cuadres se declara** |
| ⚠️ **UNA INSTRUCCIÓN DE «NO GASTAR BÚSQUEDA EN X» PUEDE SUPRIMIR UN HECHO NUEVO EN X — modo de fallo NUEVO de ARGOS 114, y el más importante de este arranque** | La instrucción sobre «Agua Verde» —dirigida a un **pendiente de topónimo**— hizo que el Noroeste excluyera, **correctamente según su encargo**, **el mayor aseguramiento del corte**: 9 fusiles AK-47, 54 cargadores, 2,620 cartuchos, 10 placas y 9 detenidos, ocurrido **en ese mismo lugar**. **Lo recuperó el arbitraje del coordinador y cambió el conteo nacional.** **REGLA: las prohibiciones de gasto se redactan contra el PENDIENTE, no contra el TOPÓNIMO** —«no reinsistir en el municipio administrativo de Agua Verde», nunca «no gastar en Agua Verde»—. **Y el coordinador revisa toda exclusión que un barrido atribuya a una instrucción suya** |
| ⚠️ **ARBITRAR NO SIEMPRE ES INTEGRAR** | **En ARGOS 114 el arbitraje rindió TRES veces y en las dos direcciones.** (a) **Recuperó** el aseguramiento de Rosario que una instrucción había suprimido. (b) **Convirtió en integrables** las tres sentencias de la FGR Sinaloa, que un barrido dejó en `PENDIENTE` por no tener fecha en la ruta: dos búsquedas verificaron los **títulos literales** y **separaron DPE/3851 y DPE/3853, que son vinculación a proceso**. (c) **SOSTUVO un descarte**: en Teotihuacán no apareció comunicado de la FGR, y **de paso corrigió al barrido**, que había leído «50 años cada uno» cuando el «cada uno» **es solo de la multa**. **Ni obedecer ni descartar por precaución: arbitrar** |
| ⚠️ **Dos barridos convergen en el mismo error cuando el hecho cruza la frontera entre sus regiones** | Regla de ARGOS 113, y en ARGOS 114 **funcionó sin necesidad de arbitraje**: Sureste y Noreste vieron ambos «Villa de La Paz» y **Sureste lo identificó correctamente como falso positivo del resumidor en su región** (es San Luis Potosí, no Guerrero). **Cuando dos regiones informen del mismo nombre propio, el coordinador arbitra con búsqueda propia antes de integrar** |
| ⚠️ **RECTIFICACIÓN EN CADENA DE LA AUTORIDAD** | El saldo de Ojocaliente se rectificó **tres veces** (7 → 10 → 11) y en ARGOS 114 apareció **una posible cuarta**: **~40 viviendas** (autoridad estatal, 1-sep) frente a **~30** (cobertura del 2-sep), con **vehículos coincidentes en 13** y **lesionados en 11**. `NO SE ARBITRA`. **Cuando acepte una rectificación en un campo, revise si hay rectificaciones posteriores en los demás campos del mismo hecho** |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | **`grep` del topónimo de localidad, no solo de municipio.** En ARGOS 114 devolvió `ARG-112-005` y `ARG-102-REC-001` para **«Agua Verde»** y obligó a un deslinde publicado. **«Cuauhtémoc» es municipio de Zacatecas, de Chihuahua Y alcaldía de CDMX; «Matamoros» está en Tamaulipas Y Coahuila; «Los Reyes» en Michoacán Y Edomex (Los Reyes La Paz); «Rosario»/«El Rosario» en Sinaloa** |
| ⚠️ **Misma localidad, fechas distintas, hechos distintos** | Agua Verde aparece **tres veces en trece días** con **tres cifras y tres corporaciones**: `ARG-102-REC-001` (19-ago, 303 AEI), `ARG-112-005` (29-ago, 29 largas, 68 cargadores) y `ARG-114-002` (1-sep, 9 AK-47, 2,620 cartuchos). **El buscador los devuelve juntos. Deslinde obligatorio** |
| ⚠️ **Dos objetos del mismo caso que el resumidor funde** | **El artefacto EMPLEADO y el artefacto ASEGURADO de la serie de Zacatecas.** Buscar «peritaje» devuelve el dictamen del **coche bomba empleado**, no del **niple asegurado**. **Lea qué objeto peritó el dictamen antes de dar por cerrado el pendiente** |
| ⚠️ **El AEI empleado no es AEI asegurado** | Los tres primeros de la serie **fueron usados contra la autoridad**: van al semáforo, **no al conteo de armamento**. El de Piedra Gorda **sí fue asegurado y sí cuenta** |
| ⚠️ **Pena compuesta** | «50 años … **para ambos**» o «para cuatro» **no es sumable**. ⚠️ **Y en Teotihuacán la trampa es más fina: el «cada uno» está publicado de la MULTA y no de la PRISIÓN.** `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`, años acumulados: no determinado |
| ⚠️ **«Más de» no es cifra** | **«Más de seis años» y «más de cuatro años» no son cifras y no se redondean.** Aunque los tres candidatos de ARGOS 114 acabaron retractados por otra razón, la regla se mantiene: **sumar «más de» daría un piso, no un acumulado, y ARGOS no publica pisos como totales** |
| ⚠️ **Sentencia frente a vinculación a proceso** | La FGR publica ambas el mismo día, con números correlativos y títulos parecidos. **Lea el verbo del título** —pero antes compruebe que el título EXISTE: en ARGOS 114 ni las sentencias ni las vinculaciones tenían fragmento citable |
| ⚠️ **Dos casos de la misma fiscalía, el mismo día** | **Municipio, delito y pena coincidentes NO identifican un caso**: hacen falta **dos campos individualizadores**. Es la lección de Coronango — **y «El Comandante RH, Coronango» está en la lista de candidatos vivos** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado siete ediciones. En ARGOS 114 confirmó que **el 28-ago-2026 fue viernes**, que es lo que sostiene la cronología de Valdez Mainero, y que **el 30-ago fue domingo** |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y **no basta como fuente única**. En ARGOS 114 Sureste descartó con esta regla una detención por extorsión en Oaxaca |
| **Trampa de año en el propio dominio oficial** | `morelos.gob.mx` devolvió un **narcolaboratorio de octubre de 2025** a una consulta de septiembre de 2026. `gabinetedeseguridad.gob.mx` ya lo había hecho antes |
| **Agregado que no se reparte** | Un balance de varios días **no se distribuye** en una ventana corta. En ARGOS 114 se aplicó a Veracruz (29-31 ago, 35 detenidos) y a Sinaloa (23-30 ago, 20 municipios) |
| **Cifra no exacta** | «más de», «alrededor de» **no es cifra** y no se redondea. **Pero busque la exacta** |
| **Capacidad declarada** | «cargadores de 20 cartuchos cada uno» **no** se convierte en cartuchos |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. ⚠️ **Y compruebe la aritmética: ARGOS 113 publicó «8,2 cargadores por arma» donde 38 ÷ 4 = 9,5** (`ARG-114-FE-004`) |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. En ARGOS 114 se declaró en el parte de SEDENA sobre Michoacán y en la respuesta federal de Zacatecas |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria** |

**Egreso bloqueado, vigesimosexta edición.** `curl` contra `*.gob.mx` devuelve
**`curl: (56) CONNECT tunnel failed, response 403`**; `WebFetch` devuelve `EGRESS_BLOCKED`.
**Cero portales por acceso directo.** Techo de confianza: **★★★★☆**.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar. **Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige lectura
directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las casillas deben CUADRAR con las 32 entidades.** ARGOS 114 cuadró **dos veces**: nacional
**6 + 25 + 1 + 0 = 32** y judicial **1 + 29 + 2 + 0 = 32**.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  **Máximo cinco líneas** en cada **Explotación ARGOS** (numeradas 1. a 5.), en cada **recuadro
  `alerta contexto`** y en la **Valoración**. La portada lleva **UN SOLO recuadro**, «LO QUE DEBE SABER EL
  MANDO». **«Hecho confirmado» va en registro telegráfico** —fecha · lugar · corporación · cifras ·
  reservas, separado por `·`—, no en prosa. **«Corroboración» es una lista de emisores por tipo.**
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes, deslindes
  ni marcas de reserva. Se recorta la prosa, no el dato.**
  **ARGOS 114 lo cumplió en los 16 bloques**, verificado con un contador automático.
- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con ARG-ID
  `-REC-`, **ventana de origen declarada** y **fuera de todos los totales** —incluido el semáforo, el radar
  y el mapa—. **ARGOS 114 publicó dos** (`ARG-114-REC-001` Tijuana, `ARG-114-REC-002` Veracruz), **ninguna
  en el arreglo `EVENTOS`**, en **página propia** con nota de encabezado.
  ⚠️ **Y un hecho YA PUBLICADO en una edición anterior no vuelve como `-REC-`: eso es duplicación.**
  Lo nuevo sobre él va a **fe de erratas** —así se trató el abatimiento de Michoacán en ARGOS 114—.
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID `-FE-`
  **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 114 cumplió**: **siete `-FE-`
  registrados, cero en el cartelón y cero en la móvil**, verificado por control automático.
  ⚠️ **Cuidado al citar un deslinde: escribir `ARG-113-FE-006` dentro de una ficha mete un `-FE-` en el
  cartelón.** Ocurrió en ARGOS 114 y se corrigió antes de publicar. **Cite «el corte anterior», no el ARG-ID.**
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha** con
  enlace `#ARG-ID` y aporta **campos distintos**.
- **Toda cifra en cero lleva al lado el dato que la explica.** Tarjetas de armamento con **doble cifra
  rotulada** y **leyenda encima del bloque**; la línea inferior es **cálculo propio** y se declara.
  **ARGOS 114 usó cinco recuadros explicativos**: por qué el rojo está en cero con un coche bomba reciente ·
  las 41 placas sin marca · la lectura regional · **por qué hay tres condenas y cero años acumulables** ·
  las cuatro cifras en disputa. **Ese es el modelo.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.** En ARGOS 114 **cinco de las nueve
  tarjetas** están en cero y **las cinco llevan su explicación**.
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura van al archivo de fuentes.
  **No mida en «ediciones» dentro del cartelón**: mida en fechas.
- **Conclusiones de inteligencia criminal**, no de método.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.** Use `<div class="alerta contexto">…`.
- **Los `id` de las fichas** solo deben tener forma de ARG-ID si son un ARG-ID real.
- ⚠️ **Cada sentencia integrada lleva ficha propia con sus apartados** —hecho procesal, pena y estatus,
  corroboración, explotación—, no solo un renglón de tabla. **ARGOS 114 publicó tres fichas de sentencia.**

### Estructura de páginas que hereda ARGOS 115

**Siete páginas**, como salió ARGOS 114: portada · crimen organizado (I) · crimen organizado (II) ·
**recuperaciones** · armamento · sentencias · valoración y conclusiones.
ARGOS 113 usó seis; **ARGOS 114 abrió una página propia para las recuperaciones en lugar de comprimirlas**.
Si el volumen lo pide, **se reparte entre más páginas: nunca se comprime una tarjeta**.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en TODAS las páginas (7 en ARGOS 114).
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 115 <FECHA> 114 2026-09-02 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.** Entre `EVENTOS_ARM` y
`SIZE_R` viven **`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL` y
`GRIS`**. ARGOS 112 los dejó fuera y **el cartelón habría cargado con el radar y el mapa rotos, sin que la
vista lo detectara**. **ARGOS 113 y 114 cortaron bien y lo verificaron con un control automático.** Repítalo.

**Comprobación de coherencia obligatoria** —ARGOS 114 la ejecutó como un solo script de Python y conviene
reutilizarla—: extraer el bloque de datos del `<script>` **hasta `const SIZE_R`**, hacer `node --check`, y
validar que **las siete constantes están presentes**, que **cada `estado:` existe en `MEXICO_PATHS`**, que
**cada `region:` coincide con `STATE_REGION`**, que **ninguna fecha cae fuera de la ventana**, que **no hay
ARG-ID duplicados** y que **el semáforo derivado de `EVENTOS` coincide con los contadores tecleados en la
portada y en `radar-stats`**. Un `region:` mal puesto **coloca el eco del radar en el sector equivocado y
nadie lo nota**.

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en ambas
versiones · toda tabla envuelta **exactamente una vez** en el escritorio · **cero `-FE-` en ambas** · cero
`sem-item` fuera de portada · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio en la
móvil (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) · **pie con número, fecha y hora en todas las
páginas del escritorio** · **todos los ARG-ID del escritorio presentes en la móvil** · sin desbordamiento
horizontal a 390 px.

*Notas del generador, que NO son defectos*: la móvil **no lleva `<script>`** · **`table-wrap` aparece en
cero** —el generador lo renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**, de modo que **`<table>` puede aparecer en CERO en la móvil sin que se pierda un solo
dato**. **En ARGOS 114 las dos tablas (16 y 13 columnas) se reflujaron y los 10 ARG-ID siguen en ambas
versiones.** **Verifíquelo contando ARG-ID, no etiquetas `<table>`.** · La móvil lleva **un solo pie**.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo y que las casillas de cobertura no cuadren con las 32 entidades |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, y que se descarte por precaución una que sí debía integrarse |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

**Novena edición consecutiva con hallazgos reales de los dos controles.** Si el destinatario no autoriza
subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la ausencia en el indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una búsqueda de
arbitraje antes de obedecerlo**, y **un control puede obligar a INTEGRAR lo que el borrador descartó por
precaución**. **Ni obedecer ni descartar por precaución: arbitrar.**

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos
**y sobre sus propias instrucciones**. Ver Bloque 5. **En ARGOS 114 produjo cinco de los ocho hechos de la
edición, y ningún subagente lo habría hecho.**

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al cartelón
   pero sí al índice.
3. **Escribir `reports/_arranque-ARGOS-116.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
