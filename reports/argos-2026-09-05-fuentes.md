# ARGOS 116 — Archivo de fuentes y trazabilidad

**Corte**: 2026-09-05 · **Ventana**: 2026-09-04 09:09 → 2026-09-05 09:46 CDMX (**24 h 37 min**).
**Hora verificada** en la sesión con `TZ=America/Mexico_City date`, no supuesta.

Este archivo contiene lo que **no** va al cartelón: hallazgos de método, fes de erratas, cobertura,
ciclo de rotación, falsos positivos y decisiones de portal. El cartelón es para el mando; esto es
para la auditoría.

---

## 0. Verificación de base (Bloque 0 del arranque)

Ejecutada **antes de leer nada más**, como manda el arranque.

| Comprobación | Resultado |
|---|---|
| `TZ=America/Mexico_City date` | **2026-09-05 09:46 CST** — hora de arranque, sella todo el cartelón |
| `git fetch origin main` | La rama asignada estaba en **ARGOS 106** (`a1cb1d5`), **nueve ediciones por detrás**, y **no contenía su propio archivo de arranque** |
| `git merge --ff-only origin/main` | **Fast-forward limpio** a `8923835` (ARGOS 115) |
| Última edición en `reports/` | **`argos-2026-09-04`** ✅ coincide con lo que el arranque exigía |
| `ls reports/ | wc -l` | **90** ✅ coincide |

**Décima edición consecutiva en que la rama asignada llega desactualizada.** Numerar por lo que la
rama tenía a la vista habría producido un falso «ARGOS 107» con ventana solapada de once días.
**El `merge --ff-only` como primer comando de la sesión sigue siendo la defensa, y sigue siendo
necesaria.**

---

## 1. Egreso: vigesimoctava edición bloqueada

Verificado **en esta sesión**, no heredado:

```
curl https://www.gob.mx/sspc                      → curl: (56) CONNECT tunnel failed, response 403
curl https://gabinetedeseguridad.gob.mx/resultados/ → curl: (56) CONNECT tunnel failed, response 403
curl https://fiscalia.chihuahua.gob.mx            → curl: (56) CONNECT tunnel failed, response 403
```

**Cero portales leídos por acceso directo.** Techo de confianza de todo el producto: **★★★★☆**.
Toda fuente institucional del corte entra **por título indexado o por republicador**, y **cada
sustitución queda anotada en la ficha que la usa**.

**Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **exige lectura directa** y por
tanto figura en **0** en los dos cuadres. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.

`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.

---

## 2. Ciclo de rotación aplicado y declarado

**A ARGOS 116 le tocaba el CICLO C — Occidente + Sureste encabezando el triaje judicial.**
**Aplicado.** Las otras cuatro regiones encabezaron con armamento.

**Prioridad sobre el ciclo, también aplicada**: la **Fiscalía de Tabasco**, única entidad
`NO REVISADA` del cuadre judicial de ARGOS 115, **encabezó el triaje de Golfo** aunque no le tocaba
por ciclo. **Saldar cobertura vence a mantener el turno.**

### Qué aportó el Ciclo C que el orden anterior no habría aportado

**Rompió parcialmente la racha.** Dirigir las primeras consultas a las **delegaciones de la FGR**
—no a las fiscalías estatales, no al armamento— produjo **cinco candidatos con el término literal de
condena**, cuando las cinco ediciones anteriores no habían producido ninguno localizable:

- **Occidente**: cuatro casos federales (Aguascalientes, Michoacán, Colima, Nayarit).
- **Sureste**: ninguno integrable, pero **confirmó `fge.yucatan.gob.mx` como portal con taxonomía de
  sentencias explícita** —primer hallazgo positivo de dominio judicial en la región en varias
  ediciones— e **interceptó dos números `DPE/…` fabricados** antes de que llegaran a ninguna cifra.

**Ninguno se integró**, y las causas son de fecha y de umbral, no de búsqueda (ver §6). **El
rendimiento del ciclo está limitado por la duración de la ventana**: con 24,6 h la probabilidad de
que una fiscalía publique sentencia en esa franja es estructuralmente baja. **No retire el ciclo por
un resultado negativo: su función es hacer demostrable el `SIN DATO`, y esta vez lo hizo.**

**A ARGOS 117 le toca el CICLO A — Noroeste + Centro.**

---

## 3. Barrido de las 32 entidades

Seis agentes `barrido-regional` en paralelo, lanzados en un solo mensaje antes de ningún otro
encargo, con la deuda regional al frente y el tope duro de 2-3 búsquedas por eje.

| Región | Entidades | Encabezó | Hechos aportados |
|---|---|---|---|
| Noroeste | BC, BCS, Sonora, Chihuahua, Sinaloa, Durango | Armamento | **1** (Ciudad Juárez) |
| Noreste | Coahuila, NL, Tamaulipas, SLP, Zacatecas | Armamento | 0 |
| Occidente | Jalisco, Colima, Nayarit, Aguascalientes, Michoacán, Guanajuato | **Judicial (Ciclo C)** | 0 |
| Centro | CDMX, Edomex, Morelos, Puebla, Tlaxcala, Hidalgo, Querétaro | Armamento | **1** (Puebla) |
| Golfo | Veracruz, Tabasco | **Judicial (Tabasco, por prioridad)** | **2** (Coatzacoalcos, Tempoal) |
| Sureste | Chiapas, Oaxaca, Guerrero, Campeche, Yucatán, QRoo | **Judicial (Ciclo C)** | 0 |

### El recall nacional del coordinador — séptima edición como paso obligatorio

**Ejecutado antes de cerrar ningún barrido**, como manda el arranque.

| Origen del hecho | ARGOS 113 | ARGOS 114 | ARGOS 115 | **ARGOS 116** |
|---|---|---|---|---|
| Barridos regionales | 4 de 6 | 3 de 8 | 6 de 7 | **4 de 6** |
| Recall y arbitraje del coordinador | 2 de 6 | 5 de 8 | 1 de 7 | **2 de 6** |

⚠️ **El recall aportó los DOS hechos de mayor gravedad del corte, y ningún barrido vio ninguno de
los dos**: **Omealca** (el único rojo, hecho de apertura del cartelón) y **Tepuche** (la
recuperación). Golfo confirmó Omealca después, de forma independiente y con dos URL fechadas más,
pero **el hecho entró por el recall**. **Ningún barrido vio Tepuche en ningún momento**, ni siquiera
Noroeste, que cubre Sinaloa.

**La razón vuelve a ser estructural y confirma lo que ARGOS 115 anotó**: un hecho nacional de gran
cobertura —un ataque a personal federal, el asesinato de un funcionario municipal— **se busca mejor
por tema que por entidad**, y los barridos están organizados por entidad. **No lo retire.**

### Casillas de cobertura — cuadre nacional

| Casilla | N.º | Detalle |
|---|---|---|
| **Con hecho publicado e integrado** | **3** | Veracruz, Chihuahua, Puebla |
| `SIN RESULTADO INDEXADO EN VENTANA` | **29** | Las 29 restantes |
| `SIN ACTUALIZACIÓN CONSTATADA` | **0** | Exige lectura directa; imposible bajo bloqueo |
| `NO REVISADA` | **0** | — |
| **Total** | **32** | ✅ **3 + 29 + 0 + 0 = 32** |

### Casillas de cobertura — cuadre judicial

| Casilla | N.º |
|---|---|
| **Fiscalías con sentencia publicada e integrable** | **0** |
| `SIN RESULTADO INDEXADO EN VENTANA` | **32** |
| `SIN ACTUALIZACIÓN CONSTATADA` | **0** |
| `NO REVISADA` | **0** |
| **Total** | **32** ✅ **0 + 32 + 0 + 0 = 32** |

**FGR revisada: Sí**, con sus delegaciones estatales, y **encabezando el triaje** por instrucción.
✅ **La Fiscalía de Tabasco queda SALDADA**: Golfo la consultó en **cinco formas distintas**
(`site:`, fecha del 4-sep, fecha del 5-sep, boletín histórico y genérica por término jurídico) y el
resultado es `SIN RESULTADO INDEXADO EN VENTANA`, **no `NO REVISADA`**. **No queda ninguna entidad
sin revisar en ninguno de los dos cuadres.**

### Deuda regional asignada — resultado

- **SEDENA / SEMAR / FGR / ANAM → NORESTE**: **NEGATIVO declarado**, igual que el de Centro en
  ARGOS 115. Ningún comunicado propio y fechado en ventana; estas corporaciones **solo aparecen
  integradas en operativos conjuntos**. **ANAM/Aduanas**: `NO REVISADA` por presupuesto, declarado
  como tal y no disfrazado. **Dos regiones con el mismo negativo: el patrón puede darse por
  establecido y el encargo puede cerrarse.**
- **Mesas de Construcción de la Paz → NOROESTE**: **cerrado con negativo constatado en 5 de 6**.
  **Chihuahua, Sinaloa, Durango, Baja California y BCS tienen mesa, y ninguna tiene portal propio**:
  publican dentro del portal estatal. **Sonora**: sin indicio localizable, negativo no concluyente.
  **Con Veracruz (sí tiene) y Tabasco (no tiene) ya resueltos en ARGOS 115, el encargo queda cerrado
  salvo Sonora.**
- ✅ **Dominios institucionales de Hidalgo y Puebla → CENTRO: RESUELTOS tras tres ediciones**,
  y con una corrección de fondo (ver §5).

---

## 4. Lo que el `grep` de archivo impidió publicar

⚠️ **La regla que ARGOS 115 pagó cara funcionó, y esta edición la validó DOS veces.**
El `grep` se ejecutó **sobre cada topónimo que los barridos y el recall trajeron, inmediatamente
antes de fichar** —no solo sobre los que enumeraba el arranque—. **Los dos hallazgos siguientes
llegaron de barridos, después del `grep` inicial**, que es exactamente el supuesto del fallo de
Pénjamo.

| Candidato propuesto | Lo que devolvió el `grep` | Decisión |
|---|---|---|
| ⚠️ **Tihuatlán, Veracruz** — Golfo lo propuso como **«candidato vivo para ARGOS 117»**: FGR, huachicol, **51,910 L**, **95 cartuchos**, 2 armas, atribuido por el resumidor al **4-sep-2026** | **`ARG-102-REC-004`** — *«Tihuatlán, Veracruz: 2 largas, 1 corta, **95 cartuchos**, **51,910 L** de hidrocarburo»*. **Dos campos individualizadores idénticos.** | **YA PUBLICADO EN ARGOS 102.** No es candidato: el resumidor **refechó al 4-sep un hecho de agosto**. **No se integra ni se arrastra a ARGOS 117** |
| ⚠️ **Puebla — «operativo con dos detenidos y un agresor abatido»**, heredado de ARGOS 115 como candidato vivo que exigía **ficha propia 🟡 o 🔴 según quién inició** | **`ARG-109-004`** — *«San Bernardino Tlaxcalancingo, Puebla: operativo de la SSPC federal para detener a «El Dron»…; repelido a tiros: **1 agresor abatido, 2 detenidos**, 3 armas (**🟡 por iniciador**)»* | **YA PUBLICADO EN ARGOS 109, Y CON EL COLOR YA RESUELTO.** **Nunca fue un candidato abierto**: se arrastró dos ediciones porque la descripción heredada no llevaba el nombre del caso |

**Lección, distinta de la de Pénjamo**: allí el defecto fue **no repetir el `grep`**; aquí el `grep`
sí se repitió, y lo que falló antes fue **cómo se redactó el candidato en el traspaso**. Un candidato
descrito por su titular genérico —«operativo con dos detenidos y un agresor abatido»— **es
irreconocible contra el archivo**. **REGLA NUEVA: todo candidato que pase a `_pendientes.md` debe
llevar municipio y, si se conoce, nombre o alias — nunca solo el titular.**

Otros tres cotejados y descartados por el mismo procedimiento, sin llegar al borrador:

- **Oaxaca, Valles Centrales / ASAEO** (Sureste, `cronica.com.mx` del 4-sep): **es `ARG-115-006`**
  —mismos **6 cateos**, mismos **3 detenidos**—, republicado un día después sin fecharlo como nuevo.
- **Guanajuato, jornada de cuatro municipios** (4 largas, 10 cortas, 58 cargadores, 1,702 cartuchos):
  es del **boletín federal del 3-sep**, **fuera de ventana**. Cotejado además **por municipio y por
  nombre** contra el archivo, por la trampa de reempaquetado de ARGOS 115.
- **Fenaza, 787 elementos**: **ya publicado en `ARG-115-001`**. Lo del corte es **el resultado del
  dispositivo**, no el dispositivo.

---

## 5. Hallazgos de método

### 5.1 El resumidor sigue fabricando números de comunicado de la FGR — cuatro más, en tres entidades

Confirmación del patrón de `ARG-115-FE-005`, ahora con **cuatro casos nuevos verificados por cadena
exacta entre comillas, todos con resultado CERO**:

| Comunicado atribuido | Entidad | Quién lo interceptó |
|---|---|---|
| `DPE/3931/2026` | Colima | Occidente |
| `DPE/3927/2026` | Zacatecas | Noreste |
| `DPE/3921/2026` | Chiapas | Sureste |
| `DPE/3924/2026` | Chiapas | Sureste |

Con los cinco de ARGOS 115 y el de ARGOS 114, van **diez números fabricados en tres ediciones, en
nueve entidades**. **El molde de título es real y la FGR lo reutiliza desde 2022; el buscador lo
completa con delegación y correlativo plausibles y lo fecha en el día de la consulta.**
**Ninguno llegó a ninguna cifra publicada.** La regla se confirma: **un `DPE/…` que no aparezca
literalmente en un titular o una URL no identifica ningún documento**, y **el negativo de la cadena
exacta vence al arbitraje**.

Un quinto caso, distinto y también interceptado: **Baja California, `DPE/3930/2026`**, atribuido a
una vinculación a proceso por hidrocarburos del 4-sep. **Ni es sentencia ni es armamento**, y el
número tampoco aparece en titular ni URL.

### 5.2 Dominios: Hidalgo no tiene «Fiscalía General», y el error costó tres ediciones

⚠️ **La deuda llevaba tres ediciones abierta porque se buscaba una institución que no existe.**

- **Puebla — RESUELTO**: **`fiscalia.puebla.gob.mx`**, con boletines en
  `/index.php/informacion-socialmente-util/boletines`. **`fiscaliapuebla.gob.mx` y
  `fgepuebla.gob.mx` NO existen**: el dominio correcto **no fusiona las palabras**.
- **Hidalgo — RESUELTO CON CORRECCIÓN DE FONDO**: **no existe una «Fiscalía General del Estado de
  Hidalgo»**. La institución es la **Procuraduría General de Justicia del Estado de Hidalgo
  (PGJEH)**, dominio **`procuraduria.hidalgo.gob.mx`**. ⚠️ **Y la cuenta `@FGR_Hgo` es la delegación
  estatal de la FGR federal, no la fiscalía estatal**: no confundirlas.

**Use `procuraduria.hidalgo.gob.mx` para Hidalgo desde ARGOS 117.** Ninguno de los dos lleva fecha en
la ruta: **consulta genérica**.

### 5.3 Dominio nuevo confirmado con taxonomía judicial explícita

**`fge.yucatan.gob.mx`** publica con *slugs* del tipo «sentenciados a prisión en juicio abreviado» y
«fallo condenatorio en procedimiento abreviado». **Es formato utilizable**, aunque su boletín más
reciente (Kanasín, 8 años) cae el **1-sep**, fuera de ventana. **Asignarle consulta dedicada en el
próximo Ciclo C.**

### 5.4 Defecto de construcción detectado por la validación, no por revisión visual

Al ensamblar el escritorio a partir de la edición anterior, **el bloque `MEXICO_VIEWBOX` +
`MEXICO_PATHS` —la geometría completa de las 32 entidades— quedó fuera**, porque vive entre el
cierre de la última `<section>` y `const CORTE_FECHA`, en un rango que el corte de plantilla no cubre.
**El cartelón habría cargado con el radar poblado y los dos mapas vacíos.**
**Lo detectó el script de coherencia obligatorio** —que valida que cada `estado:` exista en
`MEXICO_PATHS`—, **no la inspección a ojo**, que no habría visto nada raro en el HTML.

⚠️ **AVISO PARA ARGOS 117**: el arranque advierte que `<body>` está en la línea 429 y que el corte de
datos va en `REGION_ORDER`. **Faltaba advertir un tercer rango.** En el escritorio de ARGOS 116 el
bloque de mapa vive **entre `<script>` y `const CORTE_FECHA`**. **Extraiga la plantilla en tres
tramos, no en dos, y compruebe siempre `MEXICO_PATHS` con el validador.**

---

## 6. Los ejes de seguimiento — resultado

### 6.1 CHIHUAHUA — el AEI de Villas del Real (2 búsquedas, tope respetado)

- **(a) Peritaje del artefacto**: `SIN RESULTADO INDEXADO EN VENTANA`. Se revisaron las siete
  coberturas del hecho; **ninguna publica tipo de carga, contenedor ni sistema de iniciación**.
  Consta que **SEDENA se hizo cargo del aseguramiento del explosivo**, sin más detalle público.
- **(b) Auditoría del inventario de uniformes e insignias de la DSPM**:
  `SIN RESULTADO INDEXADO EN VENTANA`. Ningún comunicado municipal sobre extravío, baja o sustracción.
- **Cifra en disputa (13 / 23 / 36 cartuchos cal. .45)**: `NO SE ARBITRA`. Sin boletín de la Fiscalía
  Zona Centro con desglose.
- ✅ **Deslinde conservado y verificado**: **Villas del Real** (urbano, AEI + uniformes + 4 detenidos)
  y **el km 91 de la federal 45** (intercepción de la FGR con metanfetamina) **siguen siendo dos
  aseguramientos distintos**; ninguna fuente los fundió en esta edición.

**Siguen habiendo DOS piezas explosivas íntegras en el archivo y NINGUNA caracterizada.**

### 6.2 ZACATECAS — la Fenaza (2 búsquedas)

**El dispositivo estaba ya publicado en `ARG-115-001` y NO se recuenta.** Lo que esta edición aporta
es **el resultado del indicador que se vigilaba**:

> **La feria cumplió su primera jornada dentro de esta ventana SIN incidente, amenaza, detención ni
> artefacto localizado en el recinto o su perímetro.** `SIN RESULTADO INDEXADO EN VENTANA` para
> incidente en Fenaza.

**El salto de medio —artefacto en zona de concentración masiva— sigue sin darse.** La feria corre
**hasta el 20-sep**: **la ventana de vigilancia sigue abierta y es la más perecedera del archivo.**

### 6.3 ZACATECAS — la serie de explosivos (2 búsquedas en total para las dos preguntas)

- **(a) Niple de Piedra Gorda** (`ARG-113-ARM-003`): `SIN AVANCE`, **cuarta edición**. Sigue siendo
  **vacío declarado por la autoridad**, no falta de búsqueda. ✅ **Deslinde conservado**: lo peritado y
  publicado es **el coche bomba EMPLEADO en Ojocaliente**, no el **niple ASEGURADO**.
- **(b) Vinculación a proceso de los dos detenidos**: `SIN AVANCE`, **quinta edición**.
  **William Ariel «N» (18)** sigue **entregado a la FGR sin causa penal difundida**;
  **Juan Pedro «N» (29)**, sin novedad.

⚠️ **ARBITRAJE DEL COORDINADOR — la confusión de las dos detenciones reapareció y se rechazó otra vez.**
Noreste trajo dos fuentes que describen a **ambos** detenidos como capturados en Piedra Gorda y
vinculan a William Ariel con el ataque de **Villa García**, y lo marcó `POSIBLE CONFUSIÓN DE FUENTE`.
**El arbitraje con `grep` sobre el archivo le dio la razón al deslinde, no a las fuentes**:

- `ARG-113-FE-002`: **William Ariel «N», 18 años, capturado el 30-ago en ASIENTOS, AGUASCALIENTES**,
  por el ataque de **Villa García**; con boletín de búsqueda de la Fiscalía de Aguascalientes desde
  el 10-jun.
- `ARG-113-001`: **Juan Pedro «N», 29 años, detenido el 1-sep en PIEDRA GORDA, Cuauhtémoc,
  ZACATECAS**, por el ataque de **Ojocaliente**, **con boletín propio de la SSP estatal**.

**El propio índice registra que dos barridos ya las habían fusionado en ARGOS 113 y que el
coordinador las separó entonces.** **Es la segunda vez que la misma confusión llega desde las
fuentes: el deslinde se mantiene y conviene blindarlo en el traspaso.**

**No se volvió a buscar** —por instrucción y porque está resuelto— el «cuatro ataques del año»
(cuenta **municipios**; por evento son **cinco**, porque Luis Moya tiene dos), el accionador de
Villa García (vacío acreditado) ni el origen aguascalentense de los detenidos (integrado).

### 6.4 AGUASCALIENTES–ZACATECAS — «El Niño Concepción» (1 búsqueda, la única autorizada)

**Pregunta única**: ¿aparece en la estructura que la FGJEZ atribuye a la serie de explosivos?

> **NEGATIVO / NO CONFIRMADO.** Las fuentes atribuyen la línea del ataque de Ojocaliente **al CJNG
> como organización** y reportan un primer detenido **distinto** de «El Niño Concepción».
> **Ninguna fuente lo vincula con la célula de los artefactos.**

**Consecuencia analítica, y es un deslinde que hay que conservar**: el corredor
Aguascalientes–Zacatecas queda acreditado **por carpetas de homicidio en las dos entidades**,
**no por la estructura de los explosivos**. **Son dos cosas y no se funden.**
Lo demás —expediente único, cruce de telefonía— **es consulta documental, no búsqueda web**, y no se
gastó presupuesto en ello.

### 6.5 CHIAPAS — La Trinitaria (1 búsqueda)

`FECHA NO FIJADA — NO INTEGRAR`, **segunda edición**. El fragmento existe y es citable
—*«personal del 91.º Batallón de Infantería… aseguró **dos armas largas, 34 cargadores y 920
cartuchos útiles**»*, Diario de Chiapas— **pero la URL no lleva ruta fechada y el titular tampoco**.
La fecha «1 de septiembre» **vive solo en el párrafo del motor**. **Lo cierra una URL fechada, y solo
eso.** **Es el segundo mayor volumen pendiente del archivo.**

### 6.6 JUDICIAL — los dos candidatos (1 búsqueda cada uno)

- **(a) San Juan Teotihuacán, Edomex**: **tercera edición sin acreditar, y ahora con causa
  demostrada.** Centro consultó `gabinetedeseguridad.gob.mx` **en tres formas** —por municipio, por
  los cuatro nombres y por la cifra exacta de multa `"292,160"` entre comillas— y **ninguna devolvió
  titular ni URL institucional del caso**. Los diez resultados más cercanos del dominio son
  **sentencias de otros casos** con penas y delitos distintos.
  **Lo único que lo sostiene son tres notas de medios**, y **las dos con fecha en la ruta lo fijan en
  el 1-sep**: **fuera de esta ventana**.
  ⚠️ **La pena compuesta sigue SIN RESOLVER, y una fuente la enturbió más**: el resumidor parafrasea
  que se impuso «a cada uno» 50 años de prisión **además** de la multa, lo que **contradice o amplía**
  el dato establecido de que el «cada uno» es de la **multa**. **Como procede del párrafo del motor y
  no de un fragmento citable, no se acepta como resolución.** **50 años conjuntos o 200 acumulados:
  sigue sin poder determinarse.**
  **Vía recomendada para ARGOS 117**: `fgr.org.mx/es/FGR/Nacional` **con paginación**
  (`_rid/61?p=NN`), **no** `gabinetedeseguridad.gob.mx`, que no lo indexó en ninguna variante.
- **(b) Puebla, «operativo con dos detenidos y un agresor abatido»**: **CERRADO — YA PUBLICADO**
  como `ARG-109-004` (ver §4). **No requiere ficha nueva y su color ya estaba resuelto en 🟡.**

**No se gastó ninguna búsqueda en las tres sentencias de la FGR Sinaloa**, retiradas definitivamente
por umbral en ARGOS 115.

### 6.7 El eje que rindió sin estar en la lista — Veracruz

**Ninguno de los siete ejes prioritarios apuntaba a Veracruz**, y la entidad aportó **tres de los
cinco hechos del corte**, entre ellos **el único rojo**. Dos vías distintas y ambas necesarias:
**el recall nacional** vio Omealca; **el barrido de Golfo** —la región más pequeña, con presupuesto
para profundizar— vio Coatzacoalcos y Tempoal, **y confirmó Omealca de forma independiente**.

---

## 7. Falsos positivos interceptados

| Candidato | Por qué no entró |
|---|---|
| **Tihuatlán, Veracruz** (51,910 L, 95 cartuchos) | **Ya publicado, `ARG-102-REC-004`.** El resumidor lo refechó al 4-sep |
| **Puebla, «dos detenidos y un abatido»** | **Ya publicado, `ARG-109-004`**, con color 🟡 ya resuelto |
| **Oaxaca, ASAEO Valles Centrales** | **Ya publicado, `ARG-115-006`**: mismos 6 cateos, mismos 3 detenidos |
| **Guanajuato, jornada de 4 municipios** | Boletín federal del **3-sep**, fuera de ventana. Cotejado por municipio y por nombre |
| **Zacatecas, «cinco personas armadas en el Centro»** | Hecho del **14-jun-2026**. El título sin fecha en ruta de `ssp.zacatecas.gob.mx` sugería actualidad |
| **Nuevo León, «6 del Cártel del Noreste»** | La propia nota dice «hace apenas 2 días»: hecho hacia el **2-sep**, `FECHA NO FIJADA` |
| **Durango, Las Calzadas** (2 armas, 108 cartuchos) | Publicado el **3-sep**, antes de la apertura |
| **Sinaloa, El Rosario** (9 fusiles, 2,620 cartuchos) | Hecho del **31-ago**; es `ARG-114-002`, ya conocido |
| **Nuevo León, Sabinas Hidalgo** (210 armas) | Hecho del **30-ago**; es `ARG-112-004` |
| **Coahuila, «215 armas / 788 kg / 512 cateos»** | **Estadística acumulada** del modelo estatal hasta el 30-ago. Agregado que no se reparte |
| **«Operación Frontera Norte»** (5,542 armas, 1,050,731 cartuchos) | **Acumulado sep-2025 a jun-2026.** No es dato de ventana |
| **Cuatro comunicados `DPE/…`** | Números **fabricados**, cero resultados con cadena exacta (§5.1) |
| **Michoacán, Chinicuila** (sentencia, 4 personas) | **Publicado el 3-sep**, fuera de ventana. **Está bien fechado: la causa es la ventana, no la fuente** |
| **Aguascalientes, Rincón de Romos** (sentencia, 4 personas) | Sus dos URL **fijan mes, no día**. En 25 h eso no asigna nada |

---

## 8. Reservas y contradicciones vivas — declaradas, no arbitradas

1. **Cartuchos cal. .45 de Villas del Real**: **13 / 23 / 36**. `NO SE ARBITRA HASTA BOLETÍN.`
2. **Detenidos de Guerrero (Tlapa, Chilapa, Atlixtac)**: **71 iniciales frente a 66 finales**, tras
   liberar a 63 policías acreditados. `NO SE ARBITRA.` **Y las 284 armas serían dotación
   institucional de policías municipales desarmados, no incautación a estructura criminal**: aunque
   se fechara, **no es comparable con el resto del conteo**.
3. **Pena compuesta de Teotihuacán**: el «cada uno» es **de la multa**.
   `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA.`
4. **Nayarit, Acaponeta**: la sentencia de Manuel «N» **tiene URL fechada el 4-sep, dentro de
   ventana**, pero **la sostiene un solo medio regional**. `PENDIENTE DE CONFIRMACIÓN OFICIAL.`
   ⚠️ **Deslinde**: **no es** el agregado de Acaponeta y Huajicori de `ARG-115-ARM-004`
   (2 AEI, 8 cargadores, 236 cartuchos): **otra localidad, otras cifras, y es hecho procesal, no
   aseguramiento del corte**.
5. **Ciudad Victoria** (`ARG-104-ARM-008`): **340 frente a 103 cartuchos**.
   `CONTRADICHA — NO SE ARBITRA SIN LECTURA DIRECTA`, sin novedad.
6. **Hora de localización del cuerpo del síndico de Tepuche**: no consta en ninguna fuente.
   **NO SE INFIERE** — es lo que decide en qué edición se cuenta.

---

## 9. Controles editoriales

**Autorizados por el destinatario y ejecutados como subagentes**: seis `barrido-regional`,
`editor-duplicidad` y `procedencia-cifras`.

⚠️ **UNDÉCIMA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES DE LOS DOS CONTROLES.
LOS DOS DEVOLVIERON `CORREGIR ANTES DE PUBLICAR` Y LOS DOS TENÍAN RAZÓN.**

---

## 10. Hallazgos de los controles y correcciones aplicadas

### 10.1 `procedencia-cifras` — dos integraciones que tumban la tesis central del borrador

⚠️ **Es el hallazgo de mayor impacto sobre las cifras desde ARGOS 115, y va en la dirección de
INTEGRAR, no de retirar.** El borrador había construido su tesis de portada, de la página de
armamento y de sus conclusiones sobre una premisa falsa: **«ninguna de las 10 armas tiene categoría
publicada»**.

| Hallazgo | Evidencia | Efecto |
|---|---|---|
| **Ciudad Juárez: las 7 armas SÍ tienen desglose — 3 largas y 4 cortas** | Reproducible en consultas independientes; **suma exactamente las 7 que el titular fija**. Detalle adicional: **2 fusiles Palmetto (cal. .223 y cal. 5.56) y una tercera larga cal. .223**; cortas Kimber, Taurus, Stoeger y Smith & Wesson | **Armas cortas 0 → 4; armas largas 0 → 3** |
| **Coatzacoalcos: NO era «solo armas blancas»** | En el inmueble de **Lomas de Barrillas** se aseguró **1 arma de fuego tipo revólver**, además de armas blancas, marihuana y 3 motocicletas. **Un revólver es arma corta con categoría publicada** | **El evento entra al módulo**: +1 corta y **+8 detenidos**; el hecho pasa a tener fila y a cartografiarse |

**ARBITRAJE DEL COORDINADOR — no se obedeció, se verificó, y el control ganó.** El control **declaró
expresamente que no había podido fijar ninguno de los dos datos a un titular o URL** por bloqueo de
egreso. El coordinador ejecutó **dos búsquedas propias** con consultas distintas y **las dos
confirmaron el hallazgo**, además de aportar los nombres de los seis detenidos de Ciudad Juárez y el
reparto nominal de los 15 de Coatzacoalcos. **Se intentó además acceso directo a dos URL fechadas de
medios regionales**: `CONNECT tunnel failed, response 403` en las dos —**el bloqueo ya no es solo de
`*.gob.mx`**—.

**Decisión de integración, calibrada por lo que cada dato sostiene**:

- **El desglose 3 largas + 4 cortas SE INTEGRA**, aunque no esté en titular, porque **suma exactamente
  las 7 armas que el titular sí fija** y **dos verificaciones independientes lo devuelven igual**.
  La fila permanece en **confianza Bajo** y la marca se aplica al renglón completo.
- **Marcas y calibres NO se integran como cifra**: se publican **con reserva expresa
  `SIN FIJAR EN TITULAR`**, porque orientan la investigación pero ningún titular los sostiene.
- **El revólver de Lomas de Barrillas SE INTEGRA** como 1 arma corta, y **solo los 8 detenidos de ese
  cateo** entran al módulo: **los 7 de la col. 24 de Octubre no**, porque en ese inmueble **no hubo
  arma de fuego** y el módulo solo cuenta detenidos de eventos con aseguramiento de armamento.

**Efecto acumulado sobre el total nacional publicado**:

| Rubro | Borrador | Publicado | Causa |
|---|---|---|---|
| Armas cortas | 0 | **5** | +4 Juárez, +1 Coatzacoalcos |
| Armas largas | 0 | **3** | +3 Juárez |
| Armas sin clasificar | 10 | **3** | 7 de Juárez pasan a tener categoría |
| **Armas en total** | 10 | **11** | +1 revólver de Coatzacoalcos |
| Detenidos | 15 | **23** | +8 de Lomas de Barrillas |
| Eventos contabilizados | 3 | **4** | Coatzacoalcos entra al módulo |

**Sin este control, la edición habría publicado un total corto en armas y detenidos, y —peor— tres
tesis falsas**: que ninguna arma tenía categoría, que no había pieza cotejable y que Coatzacoalcos no
tenía armas de fuego. **Es la segunda vez en la serie que un control AUMENTA un total, y la primera
que obliga a reescribir una conclusión de portada.**

### 10.2 `editor-duplicidad` — tres incoherencias internas, todas corregidas

**Cero duplicidades reales**: cruzó los diez topónimos contra los 216 ARG-ID del índice y contra todos
los `.html` y `-fuentes.md` del repositorio, **sin una sola coincidencia**, y **confirmó que los cinco
descartes por «ya publicado» no se colaron** al cartelón ni como ficha, ni como fila, ni como cifra.

| Hallazgo | Corrección aplicada |
|---|---|
| **El recuadro decía «CINCO CANDIDATOS» y la tabla tenía SEIS** —faltaba Tabasco en la narrativa—, con un tercer número («8 candidatos» en portada) sin puente explícito | Recuadro reescrito a **«SEIS CANDIDATOS»**, con **Tabasco incorporado** a la enumeración de motivos, y portada explicitada: **«8 candidatos declarados —6 judiciales y 2 de armamento—»** |
| **«Van a detenciones relevantes»**, en la ficha de Coatzacoalcos, **remitía a una tabla que esta edición no tiene** | Frase eliminada. Ahora dice que los 7 detenidos de la col. 24 de Octubre **constan en esa misma ficha, su único registro del corte** |
| **Fuga de hallazgo de método al cartelón**: se nombraban **Zacatecas y dos de Chiapas** por sus números `DPE/…` **sin ficha ni caso asociado** | Generalizado a **«el mismo defecto se confirmó en tres números más de otras entidades, documentados en el archivo de fuentes»**. **Solo Colima, que sí tiene fila propia, se nombra** |

**Observación del control que NO se corrige, y por qué**: señaló que la portada usa
**«LO QUE DEBE SABER EL MANDO»** en lugar de **«Ejes del día»**, que es la etiqueta de `CLAUDE.md`.
**La instrucción editorial permanente del destinatario, fijada en ARGOS 105 y reiterada, retiró «Ejes
del día» y fijó un solo recuadro con ese nombre.** El control lo señaló expresamente «por
transparencia, no como hallazgo». **Se mantiene la instrucción del destinatario**, que es posterior y
más específica.

### 10.3 Lo que el arbitraje del coordinador aportó por su cuenta

Además de confirmar los dos hallazgos de `procedencia-cifras`, el arbitraje:

- **Rechazó por segunda vez la fusión de las dos detenciones de Zacatecas** (§6.3), con `grep` propio
  sobre el archivo, **contra dos fuentes que la traían fundida**.
- **Detectó los dos «candidatos» que eran hechos ya publicados** (§4), uno de ellos arrastrado dos
  ediciones.
- **Descubrió el antecedente que hacía legible el cateo de Coatzacoalcos**: el ataque a balazos contra
  el bar **«La Ventanita»** del **31-ago**, que ningún barrido reportó y que **la FGE sí vincula a los
  15 detenidos**. **Es de una ventana anterior, no está en el archivo y NO se recuenta aquí**: se
  declara como antecedente dentro de la ficha.
- **Encontró la contradicción de los rescatados de Ciudad Juárez** (2 o 4) y **la de los detenidos de
  Coatzacoalcos** (15 o 14), ninguna de las cuales venía marcada. **Las dos se declaran, no se arbitran.**

---

## 11. Verificaciones de construcción

Script de coherencia obligatorio, ejecutado sobre el escritorio ya ensamblado:

```
node --check del bloque de datos ................ OK
MEXICO_PATHS ................................... 32 entidades
EVENTOS 5 · EVENTOS_ARM 4 · ARG-ID duplicados ... 0
cada estado: existe en MEXICO_PATHS ............. OK
cada region: coincide con STATE_REGION .......... OK
ninguna fecha fuera de la ventana ............... OK
semáforo derivado = radar-stats = portada ....... 1 🔴 / 0 🟡 / 4 🟢
exactamente una etiqueta <body> ................. OK
secciones ....................................... 8
toda tabla envuelta exactamente una vez ......... 2 de 2
-FE- en el cartelón y en la móvil ............... 0 y 0
sem-item fuera de portada ....................... 0
pie con número, fecha y hora en las 8 páginas ... OK
regla de cinco líneas en los 17 bloques ......... OK
medidas en «ediciones» dentro del cartelón ...... 0
paridad de ARG-ID escritorio/móvil .............. 10 de 10
restos de clases de escritorio en la móvil ...... 0
```

**Total nacional recalculado desde las filas integradas**, no desde el borrador:
`4+0+0+1 = 5 cortas` · `3+0+0+0 = 3 largas` · `0+2+1+0 = 3 sin clasificar` · **11 armas** ·
`0+50+0+0 = 50 cartuchos` · `6+6+3+8 = 23 detenidos`. **Cuadra con lo publicado.**

⚠️ **Defecto de construcción detectado por el validador y no por revisión visual**: el bloque
`MEXICO_VIEWBOX` + `MEXICO_PATHS` había quedado fuera al extraer la plantilla (§5.4).
**El cartelón habría cargado con el radar poblado y los dos mapas vacíos.**

**Móvil generada con `tools/gen-movil.py 116 2026-09-05 115 2026-09-04 09:46`**, nunca a mano.
Salida del generador: `contadores 🔴 1 🟡 0 🟢 4` · `tarjetas: móvil 6 / escritorio 6` ·
`validación OK`. **Los contadores coinciden con el semáforo del escritorio.**

---

## 12. Nota sobre la comparabilidad de esta edición

**Ventana de 24 h 37 min frente a 46 h 52 min de la anterior: la mitad.**
**5 hechos frente a 7**, es decir **más densidad por hora, no menos**.
**Ninguna edición es comparable con otra sin normalizar por duración**, y así se declara en portada y
en la Valoración. **Conviene sostener horas de arranque estables** para que la serie recupere
comparabilidad: llevamos 47 h → 25 h.
