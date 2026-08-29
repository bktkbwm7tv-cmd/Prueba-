# ORDEN DE ARRANQUE — ARGOS 112

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 111** (corte 2026-08-29).

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

**Estado que debe encontrar ARGOS 112**: última edición `argos-2026-08-29` (ARGOS 111), **78
archivos** en `reports/`, y `main` conteniéndola —ARGOS 111 se mergeó a `main` al cierre—.
**Si `main` está por detrás de eso, algo se rompió: pare y avísele al destinatario antes de escribir
una línea.**

> ⚠️ **Esto ya falló CINCO ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 111 mostraba `argos-2026-08-24` como última edición y **no
> contenía su propio archivo de arranque**: numerar por lo que la rama tenía a la vista habría
> producido un **falso ARGOS 107 con ventana solapada**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y
> resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 112** |
| **Ventana** | **desde 2026-08-29 09:05 CDMX** (cierre de ARGOS 111) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-113.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape. **Verifique la hora, no la suponga.**

⚠️ **Si el corte cae en septiembre**, ver el Bloque 3.5: hay una obligación de portal que vence.

⚠️ **Advertencia nueva sobre la hora de cierre.** ARGOS 111 cerró un **sábado a las 09:05** y
comprobó que **el índice del buscador iba por detrás del corte**: las consultas devolvían material
del 24 al 28 de forma consistente. **Una ventana que cierra muy temprano compra un corte que el
índice todavía no ha visto.** No es motivo para retrasar el corte, pero **sí para declararlo** y para
no confundir vacío de índice con vacío de hecho.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-29-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio por entidad y municipio antes de fichar
   cualquier hecho como nuevo**, y **leer lo que devuelva**. En ARGOS 111 ese `grep` interceptó que
   **un barrido regional traía Totolapan/Cerro de las Lumbreras como «hecho nuevo de alto impacto»
   cuando ya es `ARG-110-REC-001`**. **Cuarta edición consecutiva en que lo resuelve el archivo y no
   la web. No es formalidad.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 112 HEREDA

### 3.1 El método que funcionó y hay que conservar

**Reparto de presupuesto**: ~60-65 % consulta genérica sin `site:` · ~25 % `site:` dirigido para el
desglose numérico oficial · ~10 % judicial.

| Origen del hecho | ARGOS 109 | ARGOS 110 | ARGOS 111 |
|---|---|---|---|
| Barridos regionales | 4 de 6 | 2 de 4 | **4 de 6** |
| Recall nacional del coordinador | 2 de 6 | 2 de 4 | **2 de 6** |

**El recall nacional va ANTES de cerrar ningún barrido.** En ARGOS 111 aportó **Petatlán** —un hecho
de cuatro muertos que ninguna región supo fechar y que **ninguna edición de la serie registraba**— y
**la existencia del boletín federal del 27-ago**, que produjo una fe de erratas.

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE FUNCIONÓ Y HAY QUE MANTENERLO.** En ARGOS 110 un eje
consumió **9 de las 18 búsquedas** del Centro sin producir un dato. En ARGOS 111 **ningún eje pasó de
5**, el Centro cerró el suyo en **2** —y aun así **cerró dos contradicciones heredadas de «El Dron»**
que once búsquedas de la edición anterior no habían cerrado—. **Menos gasto, más resultado.** El
precio fue cerrar tres seguimientos en `SIN AVANCE`, que **es el resultado correcto cuando no hay
dato, no un fallo**.

### 3.2 Cobertura — qué encabeza el triaje

**La deuda de SSP está casi saldada. Quedan dos y son distintas entre sí.**

**Resueltos — no los vuelva a buscar:**

| Entidad | Hallazgo |
|---|---|
| **Baja California** | ✅ **`seguridadbc.gob.mx`** sirve boletines (`boletin_<Mes>.php`). `sspbc.gob.mx` descartado |
| **Baja California Sur** | ✅ **`sspbcs.gob.mx`** es el activo |
| **Chihuahua** | ✅ **`sspe.chihuahua.gob.mx`**, ya **interrogado al periodo**: publica sostenidamente (3, 10, 12, 24-ago). ⚠️ `ssp.chihuahua.gob.mx` es FALSO |
| **Tabasco / Tamaulipas** | ✅ **No tienen subdominio propio** (`tabasco.gob.mx/seguridad`, `tamaulipas.gob.mx/seguridadpublica/`) |
| **Coahuila** | ✅ `sspcoahuila.gob.mx` — sin punto |
| **Puebla** | ✅ `ssp.puebla.gob.mx` — **solo publica acumulados de periodo**, rara vez atribuibles a una ventana |
| **Nayarit (SSP)** | ⚠️ ver anomalía en 3.2 bis |
| **`fecc.fgjtlaxcala.gob.mx`** | ✅ **CONSULTADO**, deuda saldada |
| **Fiscalía del Estado de México** | ✅ **`fgjem.edomex.gob.mx`** — `fgjestadodemexico.gob.mx` y `fgjedomex.gob.mx` no resuelven |

**Lo que queda:**

| Entidad | Estado |
|---|---|
| **Tlaxcala** | ⚠️ **SIGUE SIN ARBITRAR.** Ni `ssc.tlaxcala.gob.mx` ni `ssctlaxcala.gob.mx` devuelven boletines fechados indexados. **Puede que la respuesta sea que ninguno publica boletín fechado**: si una edición más lo confirma, ciérrelo como vacío acreditado en vez de arrastrarlo |
| **San Luis Potosí** | ⚠️ `NO REVISADA`. `seguridad.slp.gob.mx` vs `sspslp.mx` vs `sitio.sanluis.gob.mx/SSPC/` |

### 3.2 bis ⚠️ ANOMALÍA DE PORTAL — NAYARIT

`site:ssypc.nayarit.gob.mx` devuelve **como único resultado indexado una página de apuestas** ajena a
la Secretaría. El dominio se confirmó en ARGOS 109 y **nunca se había interrogado con `site:` hasta
ARGOS 111**. Se registró como **`PORTAL NO DISPONIBLE — contenido no oficial en el índice`**, jamás
como «sin actualización». **Ninguna cifra suya se usó.** **Verifique el dominio vigente por consulta
genérica sin `site:` antes de reintentarlo.**

**Hallazgos de dominio reutilizables — no los redescubra:**

| Entidad | Dominio |
|---|---|
| **Fiscalía de Durango** | ✅ **`fiscalia.durango.gob.mx/AAAA/MM/DD/`** — **fecha en la ruta, emisor de alto volumen: ocho resoluciones solo en agosto. CONSÚLTELO DE PRIMERO junto con Querétaro** |
| **Querétaro** | ✅ `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` — fecha en la ruta |
| **Fiscalía de Michoacán** | ✅ `fiscaliamichoacan.gob.mx` — **no** `fge.michoacan.gob.mx` |
| **Fiscalía de Sinaloa** | ✅ `fiscaliasinaloa.mx` — **no** `.gob.mx` |
| **Fiscalía de Chihuahua** | ✅ `fiscalia.chihuahua.gob.mx` |
| **Fiscalía de Colima** | ✅ `fgecolima.mx` |
| **Fiscalía de Nayarit** | ✅ `fiscaliageneral.nayarit.gob.mx` |
| **Fiscalía de Tlaxcala / Puebla / Tabasco** | ✅ `fgjtlaxcala.gob.mx` · `fiscalia.puebla.gob.mx` · `fiscaliatabasco.gob.mx` (esta **`NO REVISADA`** en ARGOS 111) |
| **SSP de Aguascalientes** | ✅ `aguascalientes.gob.mx/ssp/` |
| **Guanajuato** | ⚠️ por el agregador `boletines.guanajuato.gob.mx/AAAA/MM/DD/` |
| **Sonora** | ⚠️ `fgjsonora.gob.mx` sin resultados indexados, **dos ediciones**. Ni confirmado ni descartado |
| **SSP de Zacatecas** | ⚠️ existe, pero **sus boletines NO llevan fecha en la ruta** |
| **FGJ Nuevo León** | ⚠️ **no publica boletín indexable.** No gaste `site:` |
| **FGE Veracruz** | ⚠️ ARGOS 111 **alcanzó por primera vez el dominio primario `comunicacion.fiscaliaveracruz.gob.mx`** — pero **sin fecha en la ruta y sin individualización**. Cuarto agregado consecutivo inservible |

**Las fiscalías están saldadas**: 32 de 32 en ARGOS 109, 110 y 111.
**Siguen sin revisar como portal propio**: **SEDENA / SEMAR / FGR / ANAM regionales** y las **Mesas de
Construcción de la Paz** en casi todas las regiones — **quinta edición consecutiva**.

### 3.3 El ciclo

ARGOS 111 aplicó el **Ciclo A (Noroeste + Centro)** y **rindió**: el Noroeste encabezando judicial
produjo **la única sentencia integrable del corte, en Durango — exactamente igual que en ARGOS 101**.
Es la segunda vez que esa combinación se repite. **Durango es un emisor de alto volumen con fecha en
la ruta: consúltelo de primero.**

⚠️ **Arbitraje que ARGOS 111 tuvo que hacer y conviene recordar**: la deuda de dominio recaía sobre
las dos regiones que el ciclo mandaba encabezar judicial. **Se resolvió sin romper el ciclo**:
primeras búsquedas al arbitraje de dominio, después el triaje judicial. **La prioridad se salda
primero y el turno se conserva.**

**A ARGOS 112 le toca el Ciclo B — Noreste + Golfo** encabezando el triaje judicial; las otras cuatro
encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

### 3.4 Los seguimientos que más rinden

1. ⚠️ **NACIONAL — la protección balística.** *Seguimiento de mayor prioridad del próximo corte.*
   **Veinticinco placas balísticas en cuatro eventos y dos entidades en menos de dos semanas**:
   Escuinapa **7** (27-ago) + **10** (28-ago), Tepic **2** (27-ago), La Guásima **6** (18-ago).
   **Diecisiete en un solo municipio en dos días: eso es abastecimiento, no equipamiento
   individual.** La placa **lleva marca, nivel NIJ y lote**, se importa por fracción arancelaria
   identificable y su venta está regulada: **es la pieza más trazable de todo el material asegurado**,
   por delante del rastreo balístico de los fusiles, que exige cotejo previo.
   **Ninguna autoridad ha publicado marca ni nivel de una sola de las 25 placas.**
   **Qué pedir**: marca, nivel y lote en todo aseguramiento de equipo de protección, igual que se
   exige calibre en las armas. **La línea es el importador, no el portador.**
2. ⚠️ **SINALOA — Concordia produce, no recibe** (`ARG-111-003`). **49 artefactos el 28-ago y 172 el
   18-ago en el mismo municipio.** Ese volumen **se fabrica por lotes**. Y **no es exclusivo de
   Sinaloa**: Zacatecas acreditó manufactura local con **22 explosivos artesanales, 5 fulminantes
   eléctricos y ~30 kg de material** el 20-ago en Jiménez del Teul.
   ⚠️ **PERITAR ANTES DE DETONAR**: la destrucción *in situ* resuelve el riesgo y **cierra la línea de
   inteligencia**. Sin tipo, iniciación, carga y contenedor **no hay cotejo entre lotes**. La **cadena
   comercial de precursores** es vía documental. **Dos búsquedas máximo.**
3. **ZACATECAS — los seis AEI** (`ARG-110-001`). ⚠️ **La pregunta del lote está mal formulada y así se
   cerró**: lo del «1 de agosto» son **dos hechos** —coche bomba en **Luis Moya** y abatimiento en
   **Calera**—, y **un coche bomba no es del mismo tipo que seis artefactos sembrados**. No la
   reabra en esos términos. ⚠️ **Lo que sí sigue vivo: la contradicción de lesionados es
   INSTITUCIONAL** —Secretario de Gobierno dice **2**, Fiscalía dice **5**—. **Dos órganos del mismo
   gobierno con dos cifras.** `CONTRADICHA — NO SE ARBITRA SIN FUENTE DIRECTA`. **Una búsqueda.**
4. ⚠️ **ZACATECAS — el candidato de mayor volumen sin anclar.** `zacatecas.gob.mx` publicó **11
   detenidos y 10 armas largas** en el municipio de Tabasco, **sin fecha en la ruta**; el resumidor
   llegó a situarlo en «octubre de 2025». **Si ARGOS 112 lo ancla, cambia los totales de ARGOS 111 de
   forma sustancial.** **Dos búsquedas.**
5. **NACIONAL — el blanco en procuración de justicia: la hipótesis NO se confirmó.** Probada en las
   seis regiones, `SIN RESULTADO INDEXADO EN VENTANA` en todas. **No hay tercer caso; dos puntos no
   son una serie.** No se descarta, pero **no la publique como patrón**. Lo que queda **no lo contesta
   el buscador**: medir la coincidencia entre agresión y fase procesal. **Una búsqueda, o ninguna.**
6. **SINALOA — Montebello** (`ARG-111-001`): el **vehículo-ariete tiene reporte de robo** y es la única
   pieza con trazabilidad registral. Falta **calibre y número de casquillos**. **Una búsqueda.**
7. **CHIHUAHUA — un dato mueve el color** (`ARG-111-004`): confirmar o desmentir que el ocupante del
   domicilio es personal de seguridad. Si se acredita, el hecho pasa de 🟡 a 🔴. ⚠️ **Reserva de
   ubicación**: otras coberturas lo sitúan en «Cerro Coronel» y «colonia Lealtad» — **no se funden**.
   **Una búsqueda.**
8. **GUERRERO — Petatlán y Totolapan juntos** (`ARG-111-REC-001`, `ARG-110-REC-001`): **tiempo de
   respuesta desde el primer reporte** e **identidad y plaza de origen de los cuatro abatidos**. Son
   **dos regiones distintas** —Costa Grande y Tierra Caliente—: describe **expansión**.
9. **No gaste más de una búsqueda**: Escuinapa (identidad de los cinco muertos), El Arenal
   (`ARG-110-REC-002`, sin pericial), Pedernales (`ARG-110-004`, reserva abierta), Loxicha
   (`ARG-109-002`, con **candidato homónimo nuevo sin arbitrar**), Cintalapa (`ARG-110-003`,
   **discrepancia de 9 vs 10 cargadores y posible segunda detención de «El Feyo»**), Altamira
   (`ARG-109-006`), Poza Rica (`ARG-108-005`).
10. **No gaste NINGUNA**: **la disputa forestal Michoacán/Guerrero** —permisos y padrón de
    transportistas **no están indexados: es una solicitud a SEMARNAT y al RAN, no una búsqueda**—;
    **«El Dron»** (`ARG-109-004`, sus dos contradicciones ya cerradas, la pregunta principal la
    contesta un oficio); **Piedras Negras** (retirado por umbral, **no vuelve a listarse**);
    **Querétaro** (`ARG-109-005`, vacío acreditado); **Tepechitlán** (vacío acreditado).

### 3.5 ⚠️ OBLIGACIÓN DE CALENDARIO QUE VENCE

**`gabinetedeseguridad.gob.mx/resultados/` es obligatorio desde el 1 de septiembre de 2026: quedan
TRES DÍAS.** **Si el corte de ARGOS 112 cae en septiembre, ya es exigible y su ausencia debe
declararse como vacío, no como limitación heredada.** Sigue ilegible por acceso directo.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes
de ningún otro encargo**, con la deuda de portal de la 3.2 al frente de cada región, el reparto de
presupuesto de la 3.1 y **el tope duro de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  sin restricción de dominio antes de cerrarla.
- **Recall nacional del coordinador**, *además* del de cada región y **antes de cerrar los barridos**.
- **Declarar la desviación de presupuesto** si la hay. En ARGOS 111 **las seis la declararon**.

⚠️ **Reparta el enunciado de los ejes con cuidado.** En ARGOS 111 el Sureste gastó **6 búsquedas en
tres seguimientos** y bajó su cuota de armamento 16 puntos por debajo de lo previsto. **Si un eje
tiene tres preguntas, dele un tope de tres búsquedas en total, no de tres por pregunta.**

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| ⚠️ **SUMA INCOMPLETA — modo de fallo NUEVO de ARGOS 111** | **La más importante de esta edición, y no está catalogada en ninguna otra.** No es cifra inventada ni heredada: el borrador **sumó bien un rubro de dos intervenciones (1+4=5 armas) y usó solo la segunda intervención en otros cuatro** —cartuchos, cargadores, chalecos y placas—. Cada componente era citable; **el total no era la suma real de la fuente**. **Regla: cuando un hecho tenga dos o más intervenciones, verifique que TODOS los rubros se sumen, no solo el primero que revisó** |
| ⚠️ **Ubicación relativa sin fragmento citable** | **Regla nueva, extensión de la de distancias.** `procedencia-cifras` retiró «junto a una escuela primaria» de la ficha de Culiacán: **solo existía en el resumidor, que además escribió el nombre del plantel de dos formas distintas en dos consultas**. **Se retira en la primera pasada, como las distancias y duraciones** |
| ⚠️ **Falso vacío del boletín federal — DOS ediciones seguidas, mismo emisor** | ARGOS 110 corrigió el vacío del 26-ago **y creó el del 27**. **La tercera forma de la triple consulta hay que ejecutarla sobre CADA día declarado vacío, no solo sobre el que se investiga** |
| ⚠️ **El resumidor inventa la HORA, y también la FECHA de un boletín institucional** | En ARGOS 111 situó en **«octubre de 2025»** un boletín de `zacatecas.gob.mx` del 27-28 de agosto de 2026. **Una hora o fecha sin fragmento citable no fija nada, pero tampoco desfija la frontera**: se retira el dato y **se conserva la marca** |
| ⚠️ **Renglón de un boletín agregado con fecha mal atribuida** | **Cara en ARGOS 111**: «Tabasco · Villahermosa, 2 largas, 6 detenidos» **no era del boletín del 27-ago sino del 26**. **Verifique la fecha de cada renglón, no solo la del boletín** |
| ⚠️ **El mismo hecho llegando por segunda vía** | **Cara en ARGOS 111**: San Andrés Tuxtla apareció en el boletín federal con **los seis detenidos exactos** de `ARG-108-004`, ya publicado. **Integrarlo habría contado dos veces a las mismas personas** |
| ⚠️ **Dos aseguramientos del mismo municipio en días consecutivos: NO son necesariamente el mismo** | **Cara en los dos sentidos en ARGOS 111.** Escuinapa 27 y 28-ago tienen **5 armas largas ambos**, 26/28 cargadores, 8/7 placas — el control los marcó como posible duplicidad, **y eran dos hechos**. Lo resolvió **una fuente que los totalizaba en «10 detenidos»** para el municipio. **Ni funda por proximidad ni descarte por precaución: busque la fuente que los sume o los distinga** |
| ⚠️ **Día de la semana contra calendario** | Cuesta cero y ya ha salvado cuatro ediciones. En ARGOS 111 ancló Petatlán (miércoles 26 → jueves 27) y validó Culiacán (viernes 28) |
| ⚠️ **Hecho «parecido» en la misma colonia** | **Cara en ARGOS 111**: «dos heridos y casa quemada en Montebello» resultó ser de **diciembre de 2025**, no del 28-ago. **Compare inmueble, fecha y saldo antes de fundir** |
| ⚠️ **Topónimo repetido** | «Tabasco» es estado **y municipio de Zacatecas» —el Golfo tuvo que descartarlo expresamente—; «El Arenal», «Emiliano Zapata» y «Ciudad Madero» reaparecen bajo dominios de otra entidad |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y **no basta como fuente única** |
| **Capacidad declarada** | «42 cargadores **de 20 cartuchos cada uno**» **no** son 840 cartuchos. Nunca convertir |
| **Cifra no exacta** | «Más de 100 casquillos», «más de 2,800 cartuchos», «más de 20 cargadores» **no son cifras** y nunca se redondean. ⚠️ **Pero busque la exacta**: en Concordia, «más de 2,800» tenía un **2,825 publicado por una fuente**, que sí se integró declarando la fuente única |
| **Trampa de mes / de año / de aniversario** | Verificar `/2026/08/` frente a `/2026/04/`, `/2026/2/` y años anteriores |
| ⚠️ **El AEI empleado no es AEI asegurado** | Los seis de Zacatecas fueron **usados contra la autoridad**: van al semáforo, **no al conteo de armamento** |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. ⚠️ **Pero si la suma la publica la fuente, es de ella**: «221 AEI en diez días» lo publicaron los medios, y así se citó |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. Igual varios medios regionales con **redacción casi idéntica** — pasó con los «3 muertos» de Pedernales |
| **La pena no individualiza en delitos con abreviado** | Su reducción está tarifada |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria** |

**Egreso bloqueado, vigesimotercera edición.** `*.gob.mx`, `gabinetedeseguridad.gob.mx`,
`fiscaliasinaloa.mx`, `seguridadbc.gob.mx` y los dominios de medios están bloqueados; `curl` devuelve
`CONNECT tunnel failed, response 403` y `WebFetch` devuelve `EGRESS_BLOCKED`. **Cero portales por
acceso directo.** Techo de confianza: **★★★★☆**; ninguna ficha lleva ★★★★★.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar. **Verifíquelo en la sesión, no lo herede.**

✅ **ARGOS 111 recuperó un portal institucional publicando en ventana** (FGE Durango), tras la
edición 110 que no tuvo ninguno. **Con ~26 h, un único portal de 32 entidades es el orden de magnitud
esperable**: el problema es la ventana corta, no solo el bloqueo.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales** —también fuera del
  radar, del mapa y del semáforo—.
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** No se abre página, sección ni ficha. **Van al archivo de
  fuentes y a `reports/_pendientes.md`.** Si una corrección es imprescindible para leer una cifra del
  corte, se resuelve **en una línea dentro de la ficha que la use**. El ARG-ID `-FE-` **se sigue
  asignando y registrando en `indice-arg-id.md`**. **ARGOS 111 cumplió**: cinco `-FE-` registrados,
  ninguno en el cartelón.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha**
  con enlace `#ARG-ID` y aporta **campos distintos**.
- **Toda cifra en cero lleva al lado el dato que la explica.** Las tarjetas de armamento van con
  **doble cifra rotulada** —arriba, lo asegurado en hechos de la ventana; abajo, lo publicado durante
  el corte procedente de hechos anteriores— y **leyenda encima del bloque**. La línea inferior es
  **cálculo propio de ARGOS** y se declara. Regla general: *cuando una cifra correcta pueda leerse
  como un error, el defecto es del producto*. **ARGOS 111 usó tres recuadros**: por qué hay un solo
  rojo y cuatro de cinco eventos en Sinaloa; por qué hay **cero explosivos con 49 AEI** y cero
  detenidos en el hallazgo mayor; y por qué **32 fiscalías producen una sentencia** y el acumulado de
  años está en cero. **Ese es el modelo.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura del instrumento van al
  archivo de fuentes y a `_pendientes.md`. **No mida en «ediciones» dentro del cartelón**: mida en
  fechas. Las excepciones de trazabilidad, **en una línea**.
- **Conclusiones de inteligencia criminal**, no de método. **ARGOS 111 publicó seis**, todas
  accionables: la trazabilidad de las placas, la producción de AEI en Concordia, el desplazamiento del
  blanco civil al domicilio colectivo, las dos incursiones de Guerrero, la brecha detención-condena
  medida en el caso más simple, y el coste operativo de un dato no publicado.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`. Una
  `<table>` suelta desborda la móvil **en silencio**.
- **Nada de `sem-item` fuera de la portada.** Para el «Nivel de Riesgo Nacional» use
  `<div class="alerta contexto"><span class="flag">NIVEL: …</span><p>…</p></div>`.
- **Los `id` de las fichas** solo deben tener forma de ARG-ID si son un ARG-ID real.

### Estructura de páginas que hereda ARGOS 112

**Seis páginas**, como salió ARGOS 111: portada · crimen organizado (I), alto impacto · crimen
organizado (II), acciones institucionales y recuperaciones · armamento · sentencias · valoración y
conclusiones. Si el volumen lo pide, **se reparte entre más páginas: nunca se comprime una tarjeta**.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    Radar, mapa y semáforo se derivan de esos arreglos: nunca teclear los contadores a mano.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en las SEIS páginas.
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 112 <FECHA> 111 2026-08-29 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

**Comprobación de coherencia que conviene repetir** —cuesta un comando y verifica lo que el ojo no
ve—: extraer el bloque de datos del `<script>` a un archivo, hacer `node --check`, y ejecutar un
recuento que valide que **cada `estado:` existe en `MEXICO_PATHS`**, que **cada `region:` coincide con
`STATE_REGION`** y que **el semáforo derivado de `EVENTOS` coincide con los contadores tecleados en la
portada**. Un `region:` mal puesto **coloca el eco del radar en el sector equivocado y nadie lo nota**.

*Truco*: el `<script>` completo no corre en `node` porque usa `document`. **Extraiga solo hasta
`const SIZE_R`** —que es donde terminan los datos— y valide sobre eso.

**Defecto de plantilla vigente — no lo reintroduzca**: la edición 108 traía **dos etiquetas `<body>`
consecutivas**. **Compruebe que hay exactamente una.**
**Corregido en ARGOS 108 y vigente**: `gen-movil.py` envolvía dos veces las tablas con `table-wrap`.
**No lo reintroduzca.**

**Comprobar antes de publicar**: mismo número de secciones e iconos en ambas versiones · cero
tarjetas `.reg` sin texto · cero restos de clases de escritorio (`sem-item`, `stat-tile`,
`cover-visuals`, `masthead`) · toda tabla envuelta exactamente una vez en el escritorio · **cero
`-FE-` en ambas versiones** · sin desbordamiento horizontal a 390 px.

*Nota*: la móvil **no lleva `<script>`** —el generador hornea los contadores—. Una tabla de **más de
cuatro columnas se reflúa a tarjetas**: es diseño, no pérdida de datos. Por eso **`table-wrap` y
`page` aparecen en cero al contarlos en la móvil**: el generador los renombra. **No es un defecto**;
compruébelo contra la móvil de la edición anterior antes de «arreglarlo». En ARGOS 111 ambas móviles
dieron **6 secciones, 14 `tabla-scroll` y 2 `<table>`**, idénticas.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide | Rendimiento en ARGOS 111 |
|---|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo | **`CORREGIR ANTES DE PUBLICAR` con tres hallazgos**: confirmó que San Andrés Tuxtla es `ARG-108-004` y lo excluyó; **advirtió que un barrido traía Totolapan como hecho nuevo siendo `ARG-110-REC-001`**; y marcó dos dudas que exigieron arbitraje |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón | **`CORREGIR ANTES DE PUBLICAR` con seis correcciones**, dos de ellas cambiando totales nacionales: **suma incompleta en Escuinapa**, **armas de Concordia sí clasificadas**, **cartuchos exactos que existían**, **fecha mal atribuida en Tabasco**, **armamento de Oaxaca que sí tenía respaldo**, y **hora y ubicación retiradas** en Culiacán |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido | 32 de 32 entidades |

⚠️ **Lección de ARGOS 111 sobre cómo usar los controles**: **dos de sus advertencias se resolvieron
con una búsqueda cada una, y en sentidos opuestos.** La de Montebello **confirmó** el problema (la
nota de «dos heridos» era de otro año, y de no haberlo verificado se habría publicado un deslinde
falso o un saldo falso). La de Escuinapa **se levantó**: el control pedía no integrar el hecho, y una
sola búsqueda encontró la fuente que lo acreditaba como evento distinto. **Un control que dice
«no integrar» merece una búsqueda de arbitraje antes de obedecerlo a ciegas: aceptar por precaución
habría dejado fuera el hecho de mayor valor del corte.**

Si el destinatario no autoriza subagentes para los dos primeros, **ejecútelos a mano con el mismo
criterio** —así se hizo en ARGOS 106-110, y **los seis produjeron hallazgos reales**— y **declare** la
ausencia en el indicador de cobertura.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al
   cartelón pero sí al índice.
3. **Escribir `reports/_arranque-ARGOS-113.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
