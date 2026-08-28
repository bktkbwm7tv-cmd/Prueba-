# ORDEN DE ARRANQUE — ARGOS 111

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 110** (corte 2026-08-28).

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

**Estado que debe encontrar ARGOS 111**: última edición `argos-2026-08-28` (ARGOS 110), **75
archivos** en `reports/`, y `main` conteniéndola —ARGOS 110 se mergeó a `main` al cierre—.
**Si `main` está por detrás de eso, algo se rompió: pare y avísele al destinatario antes de escribir
una línea.**

> ⚠️ **Esto ya falló CUATRO ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 110 estaba **por detrás de `main`**, mostraba `argos-2026-08-24`
> como última edición y **no contenía su propio archivo de arranque**: numerar por lo que la rama
> tenía a la vista habría producido un **falso ARGOS 107 con ventana solapada**, por tercera vez.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y
> conservarlos. **Tras el merge, el estado coincidió exactamente con el que este bloque predecía.**

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 111** |
| **Ventana** | **desde 2026-08-28 06:25 CDMX** (cierre de ARGOS 110) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-112.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape. ARGOS 110 cerró **muy temprano** (06:25): si ARGOS 111 arranca por la mañana, la ventana será
corta; si arranca al día siguiente, larga. **Verifique la hora, no la suponga.**

⚠️ **Si el corte cae en septiembre**, ver el Bloque 3.5: hay una obligación de portal que vence.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-28-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio por entidad y municipio antes de fichar
   cualquier hecho como nuevo**, y **leer lo que devuelva**. En ARGOS 110 ese `grep` interceptó que
   **la detención de «El Dron» que los medios nacionales publicaron el 27-ago es `ARG-109-004`**, ya
   fichada: sin él se habría publicado como hecho nuevo del corte. **Tercera edición consecutiva en
   que lo resuelve el archivo y no la web. No es formalidad.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 111 HEREDA

### 3.1 El método que funcionó y hay que conservar

**Reparto de presupuesto**: ~60-65 % consulta genérica sin `site:` · ~25 % `site:` dirigido para el
desglose numérico oficial · ~10 % judicial. **Los cuatro hechos de ARGOS 110 llegaron por consulta
genérica**, ninguno por barrido de dominio.

| Origen del hecho | ARGOS 108 | ARGOS 109 | ARGOS 110 |
|---|---|---|---|
| Barridos regionales | 3 de 8 | 4 de 6 | **2 de 4** |
| Recall nacional del coordinador | 5 de 8 | 2 de 6 | **2 de 4** |

**El recall nacional va ANTES de cerrar ningún barrido, y su valor no está solo en lo que aporta.**
En ARGOS 110 **interceptó tres falsos positivos**, el más grave un **comunicado del 17 de marzo de
2023** —siete detenidos, dos policías municipales muertos— que el barrido del Centro traía como
candidato de alto impacto con `fecha no fijada`. **Y vio Escuinapa, el hecho de mayor volumen del
Noroeste, que el barrido de esa región no vio.**

### 3.2 Cobertura — qué encabeza el triaje

⚠️ **LOS PORTALES DE SSP ESTATAL SIGUEN ENCABEZANDO, pero la deuda ya no es la misma.** ARGOS 110 la
atacó por primera vez en cuatro ediciones y descubrió que **parte de ella no existía**.

**Resueltos — no los vuelva a buscar:**

| Entidad | Hallazgo |
|---|---|
| **Tabasco** | ✅ **No tiene subdominio propio.** Publica bajo `tabasco.gob.mx/seguridad` |
| **Tamaulipas** | ✅ **No tiene subdominio propio.** Integrada en `tamaulipas.gob.mx/seguridadpublica/` |
| **Coahuila** | ✅ `sspcoahuila.gob.mx` — **sin punto** antes de «coahuila» |
| **Durango** | ✅ `seguridad.durango.gob.mx/seccion/boletines/` — indexa, pero lo más reciente es de enero-abril 2026 |
| **Puebla** | ✅ `ssp.puebla.gob.mx` — **publica acumulados de periodo, no boletín diario**: sus cifras rara vez son atribuibles a una ventana |

**Lo que queda, y es distinto de lo que era — son AMBIGÜEDADES, no dominios desconocidos:**

| Entidad | Ambigüedad a resolver |
|---|---|
| **Baja California** | `seguridadbc.gob.mx` (Secretaría de Seguridad Ciudadana) **vs** `sspbc.gob.mx` (transparencia). ¿Cuál sirve boletines? |
| **Baja California Sur** | `sspbcs.gob.mx` **vs** `ssbcs.gob.mx` — **ambos resuelven** |
| **Tlaxcala** | `ssc.tlaxcala.gob.mx` **vs** `ssctlaxcala.gob.mx` — **ambos devuelven resultados** |
| **San Luis Potosí** | `seguridad.slp.gob.mx` (indexa hasta el 24-ago) **vs** `sspslp.mx` **vs** `sitio.sanluis.gob.mx/SSPC/` |
| **Chihuahua** | ✅ `sspe.chihuahua.gob.mx` — ⚠️ **`ssp.chihuahua.gob.mx` es FALSO**. Localizado, **no interrogado al periodo** |
| **Nayarit** | ✅ `ssypc.nayarit.gob.mx` — dominio confirmado desde ARGOS 109, **nunca interrogado por `site:`** |

**Además**: **`fecc.fgjtlaxcala.gob.mx` sigue `NO REVISADA`**, segunda edición consecutiva. Y las
**Mesas de Construcción de la Paz** y **SEDENA / SEMAR / FGR / ANAM regionales** siguen sin revisar
como portal propio en casi ninguna región, cuatro ediciones seguidas.

**Las fiscalías están saldadas**: 32 de 32 consultadas en ARGOS 109 y 110.

**Hallazgos de dominio reutilizables — no los redescubra:**

| Entidad | Dominio |
|---|---|
| **Querétaro** | ✅ `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` — **fecha en la ruta, el mejor formato de la serie. Consúltelo de primero** |
| **Fiscalía de Michoacán** | ✅ `fiscaliamichoacan.gob.mx` (+ `comunicacion.`, `juridico.`, `directorio.`) — **no** `fge.michoacan.gob.mx` |
| **Fiscalía de Sinaloa** | ✅ `fiscaliasinaloa.mx` — **no** `.gob.mx` |
| **Fiscalía de Chihuahua** | ✅ `fiscalia.chihuahua.gob.mx` — `fgechihuahua.gob.mx` no resuelve |
| **Fiscalía de Colima** | ✅ `fgecolima.mx` — **no** `fiscalia.colima.gob.mx` |
| **Fiscalía de Nayarit** | ✅ `fiscaliageneral.nayarit.gob.mx` |
| **Fiscalía de Tlaxcala** | ✅ `fgjtlaxcala.gob.mx` |
| **Fiscalía de Puebla** | ✅ `fiscalia.puebla.gob.mx` |
| **Fiscalía de Tabasco** | ✅ `fiscaliatabasco.gob.mx` |
| **SSP de Aguascalientes** | ✅ `aguascalientes.gob.mx/ssp/` · IESPA en `/IESPA/` |
| **Guanajuato** | ⚠️ sigue por el agregador `boletines.guanajuato.gob.mx/AAAA/MM/DD/` |
| **Sonora** | ⚠️ `fgjsonora.gob.mx` probado en ARGOS 110, **sin resultados indexados**. Ni confirmado ni descartado |
| **SSP de Zacatecas** | ⚠️ existe, pero **sus boletines NO llevan fecha en la ruta**. Ninguna cifra suya entra sin ancla externa |
| **FGJ Nuevo León** | ⚠️ **no publica boletín indexable en portal**, acreditado en tres formas. **No gaste `site:` ahí** |
| **FGE Veracruz** | ⚠️ **nunca se ha alcanzado la fuente primaria**: sus agregados solo llegan por republicadores con texto idéntico |

### 3.3 El ciclo

ARGOS 110 aplicó el **Ciclo C** (Occidente + Sureste) y **rindió negativamente en sentencias, con un
hallazgo estructural**: doce fiscalías recorridas, más de veinte resoluciones condenatorias
localizadas, **ninguna dentro de la ventana**. **Con ventanas de ~20 horas, la probabilidad de que
una fiscalía publique en esa franja es baja.** El triaje judicial encabezado **sigue siendo necesario
para que el `SIN DATO` sea demostrable**, pero su rendimiento en sentencias integrables **está
limitado por la duración de la ventana, no por el orden de búsqueda**. El Ciclo A de ARGOS 108
enmascaró esto al producir una sentencia.

Su rendimiento real fue otro: **el Sureste cerró el candidato de Cintalapa** —abierto desde ARGOS
109— al localizar una URL con día en la ruta, y **Occidente descartó por calendario dos señuelos**.

**A ARGOS 111 le toca el Ciclo A — Noroeste + Centro** encabezando el triaje judicial; las otras
cuatro encabezan con armamento. **Salvo que la deuda de SSP mande otra cosa**: la prioridad sobre el
ciclo vence al turno, y **Baja California y BCS —las dos ambigüedades de dominio más cerradas— están
las dos en el Noroeste**, que este ciclo encabeza judicial. Resuélvalo declarándolo.

*Se declara expresamente en el archivo de fuentes, junto con qué aportó la rotación.* Una edición que
no diga qué ciclo aplicó, no aplicó ninguno.

### 3.4 Los seguimientos que más rinden

1. **Zacatecas — los seis artefactos de la carretera federal 54** (`ARG-110-001`). *Es el seguimiento
   de mayor prioridad del próximo corte.* **Dos AEI detonados contra personal de la FGJEZ y la FRIZ, y
   cuatro más sembrados y destruidos por detonación controlada**, en la comunidad de San Luis,
   municipio de Tabasco, cerca de la presa El Chique. **Seis artefactos en un punto no son una
   emboscada: son una posición preparada, y eso implica un taller.** Pregunta que decide:
   **¿son los seis del mismo lote que los empleados el 1 de agosto en la misma entidad?** El peritaje
   comparado de **iniciadores, contenedores y carga** establece si hay **un único taller abasteciendo
   el corredor** —objetivo físico localizable— o varios armadores. Falta **tipo de artefacto, sistema
   de iniciación, carga y si hubo detenidos**. ⚠️ **Cifra de heridos contradicha (2 vs 5), sin
   arbitrar.** ⚠️ **Ocurre en el corredor Juchipila–Tlaltenango–Tepechitlán**: refuerza ese
   seguimiento, no lo sustituye.
2. **Nacional — el blanco se desplaza a procuración de justicia.** **Dos agresiones con explosivos
   contra fiscalías el 26 y el 27 de agosto**, en entidades sin relación: amenaza contra sedes de la
   **FGR en Mexicali** y ataque efectivo contra la **FGJEZ en Zacatecas**. En ninguna el blanco fue
   Ejército, Marina ni GN: **fueron las corporaciones que integran carpetas**. **Medir la coincidencia
   entre agresión y fase procesal.** Si el patrón se confirma, es un cambio de doctrina de protección.
3. **Sinaloa — el equipo balístico de Escuinapa** (`ARG-110-002`). **Cuatro cuerpos con chalecos
   tácticos**, más **5 chalecos y 7 placas balísticas** asegurados. **Las placas son mercancía
   trazable** —marca, nivel NIJ, lote— y **llegan antes al abastecedor que el rastreo de los fusiles**.
   Falta **identidad y adscripción de los cinco muertos** y **si los 7 detenidos del Ejército y los 5
   de la fiscalía son las mismas personas**: de ello depende cerrar el conteo. ⚠️ **Escuinapa acumula
   en 2026 fusil, AEI, coche bomba y drones armados**: vigile el escalamiento de medio en zona
   habitada.
4. **Puebla/Sinaloa — la red que alojaba a «El Dron»** (`ARG-109-004`). **Sin avance pese a 11
   búsquedas.** La pregunta sigue siendo **si las tres armas viajaron con él o se las dieron en
   destino** —red de traslado frente a red de acogida—, y **el segundo tirador sigue prófugo**.
   ⚠️ **Dos contradicciones nuevas sin arbitrar**: un resumen afirma que «otro sospechoso referido
   como El Dron sigue prófugo», lo que choca con la identificación del detenido; y `diariocambio.com.mx`
   atribuye un operativo en Cholula a **«la Tripa», del «comando Tlahuica»** — posible confusión de dos
   operativos. **La pregunta no la contesta el buscador: la contesta un oficio.** Gaste **dos búsquedas
   como máximo** salvo que aparezca boletín: la edición anterior gastó nueve sin resultado.
5. **Michoacán y Guerrero — la disputa forestal es una sola línea.** Tractocamión maderero incendiado
   en el eje de salida forestal de Opopeo (`ARG-109-001`) y familia aniquilada por negarse a ceder
   tierras para explotación forestal en Totolapan (`ARG-110-REC-001`). **Se ataca el transporte en una
   entidad y la tenencia de la tierra en la contigua.** Pida **permisos de aprovechamiento forestal**
   sobre ambos polígonos y **situación registral y comunal del Cerro de las Lumbreras**.
6. **Tamaulipas — el rancho de Altamira** (`ARG-109-006`). **Sin avance**: no se localizó titularidad
   registral, cruce con ANAM, permisos SEMARNAT/UMA ni destino del diésel. Dato nuevo menor: los
   ejemplares quedaron bajo resguardo de **PROFEPA**. **Mantiene prioridad**, con **dos búsquedas**.
7. **Michoacán — reserva de saldo en Pedernales** (`ARG-110-004`). La SSP confirmó **un muerto**; dos
   medios regionales elevaron después a **tres**, sin confirmación. **Si la FGE confirma tres, el
   hecho pasa de 🟡 a 🔴 y el semáforo de ARGOS 110 cambia.** Una búsqueda.
8. **Guerrero — El Arenal** (`ARG-110-REC-002`). Falta **confirmación pericial de que los restos son
   humanos**, número mínimo de individuos y **si el predio ya estaba señalado por denuncia previa**.
9. **No gaste más de una búsqueda**: Loxicha (`ARG-109-002`, sin avance y con un homónimo de 2023 ya
   descartado), Piedras Negras (`ARG-110-SEN-C02`, dos ediciones sin ancla).
10. **No gaste ninguna**: Querétaro (`ARG-109-005`) —**vacío de publicación acreditado**, las armas
    siguen sin clasificar y el efectivo sin cifra—; Morelia (`ARG-106-REC-002`) —**cerrado**—;
    Tepechitlán —armamento **no publicado**, vacío acreditado—.

### 3.5 ⚠️ OBLIGACIÓN DE CALENDARIO QUE VENCE

**`gabinetedeseguridad.gob.mx/resultados/` es obligatorio desde el 1 de septiembre de 2026: quedan
CUATRO DÍAS.** El emisor anunció ahí la migración de los reportes diarios preliminares de homicidio y
robo de vehículo. **Si el corte de ARGOS 111 cae en septiembre, ya es exigible y su ausencia debe
declararse como vacío, no como limitación heredada.** Sigue ilegible por acceso directo.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes
de ningún otro encargo**, con la deuda de portal de la sección 3.2 al frente de cada región y con la
instrucción de la 3.1 sobre el reparto de presupuesto.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  sin restricción de dominio antes de cerrarla. **En ARGOS 110 el Noroeste cerró su región sin ver
  Escuinapa**, que el recall nacional sí vio.
- **Recall nacional del coordinador**, *además* del de cada región y **antes de cerrar los barridos**.
- **Declarar la desviación de presupuesto** si la hay. En ARGOS 110 cinco regiones alcanzaron el techo
  y una gastó el doble de lo previsto en el eje prioritario; **las seis lo declararon**.

⚠️ **Advertencia de reparto**: en ARGOS 110 el eje prioritario consumió **9 de las 18 búsquedas** del
Centro y dejó Estado de México, Morelos e Hidalgo con **una consulta genérica cada uno**, sin
producir un solo dato nuevo. **Ponga tope duro a los ejes de seguimiento** —dos o tres búsquedas— y
gaste el resto en la ventana.

Si el destinatario **no** autoriza subagentes, haga barrido dirigido a mano y **declare la cobertura
real**: `NO REVISADA` para lo no consultado, jamás `SIN ACTUALIZACIÓN`.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| ⚠️ **Comunicado sin fecha en la ruta** | **La más cara de ARGOS 110.** El comunicado conjunto SSC CDMX–SSEM «siete detenidos, policías municipales muertos» es del **17 de marzo de 2023**. Un barrido lo traía como candidato de alto impacto. **Verifique el formato de URL vigente del emisor en el año del corte antes de aceptar el candidato** |
| ⚠️ **La hora, no solo la fecha** | **Cara en ARGOS 110 en los dos sentidos**: Cintalapa **entró** porque «media tarde» es posterior a las 10:00; **Totolapan quedó fuera por seis horas** —04:00 h— pese a sus **seis muertos**. Cuando la fuente publica hora, **compárela con la apertura de la ventana** |
| ⚠️ **Día de la semana contra calendario** | **Cerró Cintalapa en ARGOS 110**: el resumidor insistió en «26 de agosto» **en tres consultas**, sin ancla; la URL con día en la ruta lo fijó en el **jueves 27**. Cuesta cero y ya ha salvado tres ediciones |
| ⚠️ **Hecho «parecido pero en otra localidad» del mismo municipio** | **Cara en ARGOS 110**: **El Pedregoso** (26-ago, 3 detenidos, 0 muertos) y **Pedernales** (27-ago, 1 muerto, 0 detenidos) son **dos hechos**, no uno. **Compare localidad, fecha y saldo antes de fundir o de fichar como nuevo** |
| ⚠️ **Dos desgloses del mismo hecho que no cuadran** | **Cara en ARGOS 110**: Escuinapa devolvió «7 detenidos, 5 largas, 28 cargadores» y «6 personas, 6 rifles, 40 cargadores, 5 AEI». **No promedie ni elija el mayor**: integre el que tenga corporación y autoridad receptora nombradas, y marque el otro `POSIBLE DUPLICIDAD` |
| **Trampa de mes** | **Cara en ARGOS 110**: Coahuila «116 armas» es del **14-abr**; los narcobloqueos «tras la muerte de El Mencho» son del **22-feb**. Verificar `/2026/08/` frente a `/2026/2/` y `/2026/04/` |
| **Trampa de aniversario** | Ninguna cifra entra sin año verificable en la ruta |
| ⚠️ **Topónimo repetido en el país** | **Cara en ARGOS 110 al auditar**: **«El Arenal» es municipio de Hidalgo y comunidad de Acapulco**; **«Tabasco» es estado y municipio de Zacatecas**; **«Emiliano Zapata» es ejido en decenas de entidades**. El `grep` del índice devuelve falsos positivos: **léalos, no los cuente** |
| ⚠️ **Caso homónimo por tema, no por lugar** | **Cara en ARGOS 110**: buscar «conflicto agrario Oaxaca» devuelve la emboscada de **Santiago Mitlatongo de noviembre de 2023** —otra región, otro año, otras cifras— como si fuera Loxicha 2026 |
| ⚠️ **El resumidor inventa la HORA, no solo la fecha** | **Regla nueva de ARGOS 110.** `procedencia-cifras` retiró la hora «10:00 h» y la ubicación «camino a Los Sábalos» de Escuinapa: **solo existían en el resumen del buscador**. **Una hora sin fragmento citable no fija nada, pero tampoco desfija la frontera**: se retira la hora y **se conserva la marca** |
| ⚠️ **Distancias y duraciones estimadas por el redactor** | **TERCERA REINCIDENCIA** (ARGOS 108, 109 y 110: «a unos quince minutos del poblado»). **Deja de ser descuido.** **Regla operativa: toda expresión de distancia o duración que no proceda de una medición publicada se retira en la primera pasada, no en el control** |
| ⚠️ **Cifras derivadas sin declarar** | **Cara en ARGOS 110**: «veintiséis días de diferencia» entre dos hechos y «veintiuna resoluciones descartadas» eran **cálculos propios no declarados y no verificables**. Publique las dos fechas, o declare el cálculo |
| **Vinculación a proceso presentada como aseguramiento nuevo** | Vinculación **no es sentencia** y el armamento **no se recuenta** |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y **no basta como fuente única** |
| **Capacidad declarada** | «42 cargadores **de 20 cartuchos cada uno**» **no** son 840 cartuchos. Nunca convertir |
| **Cifra no exacta** | «Más de veinte cartuchos» y «más de cien fragmentos óseos» **no son cifras** y nunca se redondean |
| **Evolución de saldo ≠ contradicción** | **Se ficha la versión institucional y se declara la posterior.** En Pedernales, la SSP confirmó 1 muerto y dos medios elevaron después a 3: **se fichó 1, con la reserva declarada**. No se promedian |
| ⚠️ **El AEI empleado no es AEI asegurado** | **Regla nueva de ARGOS 110.** Los seis artefactos de Zacatecas fueron **usados contra la autoridad**: entran en el semáforo como evento rojo, **no en el conteo de armamento**. Un AEI detonado no es un aseguramiento |
| **La pena no individualiza en delitos con abreviado** | Su reducción está tarifada: la pena exacta **deja de contar** entre los ≥2 campos individualizadores |
| **Sumas propias sin declarar** | Todo total nacional que ARGOS calcule es **cálculo propio** y **se declara en el cartelón** |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria antes de redactar** |

**Egreso bloqueado, vigesimosegunda edición.** `*.gob.mx`, `gabinetedeseguridad.gob.mx`,
`fiscaliasinaloa.mx` y los dominios de medios —`infobae.com` incluido— están bloqueados; `curl`
devuelve `CONNECT tunnel failed, response 403` y `WebFetch` devuelve `EGRESS_BLOCKED`. **Cero portales
por acceso directo.** Techo de confianza: **★★★★☆**; ninguna ficha lleva ★★★★★.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar. **Verifíquelo en la sesión, no lo herede**:
basta un `curl` por dominio.

⚠️ **Dato nuevo, a vigilar**: ARGOS 110 es **la primera edición reciente sin un solo portal
institucional publicando en ventana** —ARGOS 109 tuvo al menos la FGE de Querétaro—. Sus cuatro
fichas se sostienen en **fuente institucional por cita** más corroboración de medios. **Si se repite,
el problema es la ventana corta, no el bloqueo**, y conviene decirlo.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales** —también fuera del
  radar, del mapa y del semáforo—.
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** No se abre página, sección ni ficha de fe de erratas.
  **Las correcciones van al archivo de fuentes y a `reports/_pendientes.md`.** Si una corrección es
  imprescindible para leer una cifra del corte en curso, se resuelve **en una línea dentro de la
  ficha que la use**. El ARG-ID `-FE-` **se sigue asignando y registrando en `indice-arg-id.md`**.
  **ARGOS 110 cumplió**: cinco `-FE-` registrados, **ninguno en el cartelón**.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha**
  con enlace `#ARG-ID` y aporta **campos distintos** —cifras, corporación, confianza—, no repite el
  titular.
- **Toda cifra en cero lleva al lado el dato que la explica.** Las tarjetas de armamento van con
  **doble cifra rotulada** —arriba, lo asegurado en hechos de la ventana; abajo, lo publicado durante
  el corte procedente de hechos anteriores— y **leyenda encima del bloque**. La línea inferior es
  **cálculo propio de ARGOS** y se declara. Regla general: *cuando una cifra correcta pueda leerse
  como un error, el defecto es del producto*. **ARGOS 110 necesitó tres recuadros**: por qué el verde
  del semáforo estaba en cero habiendo ocho detenidos, por qué había ocho armas largas y ninguna
  corta, y por qué un agregado de 16 condenas no produce una sola sentencia citable. **Ese es el
  modelo.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura del instrumento van al
  archivo de fuentes y a `_pendientes.md`. **No mida en «ediciones» dentro del cartelón**: mida en
  fechas. Las excepciones de trazabilidad —declaración de ventana, casillas de cobertura,
  comparabilidad, bloqueo de egreso, deslindes—, **en una línea**.
- **Conclusiones de inteligencia criminal**, no de método: patrones territoriales, perfil de víctima,
  modus operandi, capacidad de fuego, brecha detención-condena, líneas a explotar.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`. Una
  `<table>` suelta desborda la móvil **en silencio**.
- **Nada de `sem-item` fuera de la portada.** Para el «Nivel de Riesgo Nacional» de la última página
  use `<div class="alerta contexto"><span class="flag">NIVEL: …</span><p>…</p></div>`.
- **Los `id` de las fichas** solo deben tener forma de ARG-ID si son un ARG-ID real: el generador
  móvil recoge `<div class="nota" id="…">` como anclas enlazables.

### Estructura de páginas que hereda ARGOS 111

**Seis páginas**, como salió ARGOS 110: portada · crimen organizado (I), alto impacto · crimen
organizado (II) y recuperaciones · armamento · sentencias · valoración y conclusiones. Si el volumen
de fichas lo pide, **se reparte entre más páginas: nunca se comprime una tarjeta para que quepa**.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    Radar, mapa y semáforo se derivan de esos arreglos: nunca teclear los contadores a mano.
#    El campo `region:` de cada evento debe coincidir con STATE_REGION (Zacatecas es NORESTE).
#    ⚠️ CORTE_FECHA se hereda y es fácil olvidarlo: ARGOS 110 lo detectó en la revisión final.
#    ⚠️ Actualizar el <title> del <head>: también se hereda.
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO. Compruébelo contra el contenido real del corte.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 111 <FECHA> 110 2026-08-28 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

**Comprobación de coherencia que ARGOS 110 añadió y conviene repetir** —cuesta un comando y verifica
lo que el ojo no ve—: extraer el `<script>` a un archivo, hacer `node --check`, y ejecutar un
recuento que valide que **cada `estado:` existe en `MEXICO_PATHS`** y que **cada `region:` coincide
con `STATE_REGION`**. Un `region:` mal puesto no rompe nada: **coloca el eco del radar en el sector
equivocado y nadie lo nota**.

**Defecto de plantilla vigente — no lo reintroduzca**: la edición 108 traía **dos etiquetas `<body>`
consecutivas**. Si copia una edición como base, **compruebe que hay exactamente una**.

**Corregido en ARGOS 108 y vigente**: `gen-movil.py` envolvía dos veces las tablas que ya traían
`table-wrap`. Se arregló con un *lookbehind*. **No lo reintroduzca.**

**Comprobar antes de publicar**: mismo número de páginas e iconos en ambas versiones · cero tarjetas
`.reg` sin texto · cero restos de clases de escritorio (`sem-item`, `stat-tile`, `cover-visuals`,
`masthead`) · toda tabla envuelta exactamente una vez en el escritorio · sin desbordamiento
horizontal a 390 px · **sintaxis del script validada con `node --check`**.

*Nota*: la móvil **no lleva `<script>`** —el generador hornea los contadores—, así que `node --check`
solo aplica al escritorio. Y una tabla de **más de cuatro columnas se reflúa a tarjetas** en la
móvil: es diseño del generador, no pérdida de datos. Por eso **`table-wrap` y `list-item` aparecen
en cero al contarlos en la móvil**: el generador los renombra. **No es un defecto**; compruébelo
contra la móvil de la edición anterior antes de «arreglarlo».

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide | Rendimiento en ARGOS 110 |
|---|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo | **Tres hallazgos**: el `grep` interceptó que la detención de «El Dron» es `ARG-109-004`; **deslindó El Pedregoso de Pedernales**, que iban camino de publicarse como un solo hecho; y verificó trece localidades nuevas contra todo el archivo, descartando dos falsos positivos de topónimo |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón | **Cuatro retiradas**: una cifra derivada no declarada, **una hora y una ubicación que solo existían en el resumidor**, una distancia estimada por el redactor —**tercera reincidencia**— y un conteo propio no verificable |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido | 32 de 32 entidades |

Si el destinatario no autoriza subagentes para los dos primeros, **ejecútelos a mano con el mismo
criterio** —así se hizo en ARGOS 106, 107, 108, 109 y 110, y **los cinco produjeron hallazgos
reales**— y **declare** la ausencia en el indicador de cobertura, no la disimule.

Cuando un control devuelva `CORREGIR ANTES DE PUBLICAR`, se corrige y se vuelve a pasar. Si se decide
no corregir, la razón se deja escrita en el archivo de fuentes.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al
   cartelón pero sí al índice.
3. **Escribir `reports/_arranque-ARGOS-112.md`** y borrar este archivo.
4. Commit descriptivo, push a la rama de la edición, y **merge a `main`** para que la rama por
   defecto no vuelva a quedarse atrás.

---

## TEXTO PARA PEGAR EN EL CHAT NUEVO

> Genera el ARGOS de hoy. Antes de numerar la edición, lee `reports/_arranque-ARGOS-111.md` y
> ejecuta su Bloque 0: la numeración sale del archivo, no de lo que veas en la rama local, y el
> `git merge --ff-only origin/main` va antes de leer nada más. Después lee `CLAUDE.md`,
> `reports/_pendientes.md` y `reports/argos-2026-08-28-fuentes.md`.
>
> La ventana abre donde cerró ARGOS 110 (2026-08-28 06:25 CDMX) y cierra a la hora real de arranque,
> verificada con `TZ=America/Mexico_City date`.
>
> Prioridades: **los seis artefactos de la carretera federal 54 en Zacatecas** —si son del mismo lote
> que los del 1 de agosto, que es lo que distingue un taller único de varios armadores—; **el
> desplazamiento del blanco hacia procuración de justicia**, con dos agresiones con explosivos contra
> fiscalías el 26 y el 27 de agosto; **el equipo balístico de Escuinapa**, que es mercancía trazable y
> llega antes al abastecedor que los fusiles; **resolver las ambigüedades de dominio de SSP** —Baja
> California, BCS, Tlaxcala y San Luis Potosí tienen dos o tres dominios vivos cada una, y ya no es
> una deuda de descubrimiento sino de arbitraje—; y aplicar y declarar el **Ciclo A (Noroeste +
> Centro)**, salvo que la deuda de SSP mande otra cosa.
>
> Conserva el reparto de presupuesto: ~60-65 % consulta genérica sin `site:`, y el recall nacional del
> coordinador **antes** de cerrar ningún barrido. **Pon tope duro de dos o tres búsquedas a cada eje
> de seguimiento**: en ARGOS 110 uno consumió la mitad del presupuesto de su región sin producir dato.
>
> Respeta el Bloque 6: **sin fe de erratas en el cartelón** —van al archivo de fuentes y a
> `_pendientes.md`, y el ARG-ID `-FE-` se sigue registrando en el índice—; sin resumen ejecutivo;
> ningún hecho con ficha propia se repite en una tabla resumen; y toda cifra en cero lleva al lado el
> dato que la explica —las tarjetas de armamento van con doble cifra rotulada—.
>
> Genera cartelón **y** versión móvil —esta última con `tools/gen-movil.py`, nunca a mano—,
> actualiza `_pendientes.md` e `indice-arg-id.md`, escribe el arranque de ARGOS 112, y al cerrar
> mergea a `main`.
>
> Autorizo subagentes para los seis barridos regionales.
