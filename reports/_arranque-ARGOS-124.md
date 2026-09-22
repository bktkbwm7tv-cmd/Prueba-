# ORDEN DE ARRANQUE — ARGOS 124

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino
en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 123** (corte 2026-09-22).

⚠️ **El mensaje de arranque listo para pegar en una sesión nueva está en
`reports/_ordenes-ARGOS-124.txt`.** Este archivo es el detalle; aquél es la orden.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en TODO el cartelón
git fetch origin                                   # traer el estado real
git branch -r | sed 's#origin/##' | sort           # ¿qué rama está más avanzada?
git merge --ff-only origin/<rama-más-avanzada>     # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 124**: última edición `argos-2026-09-22` (ARGOS 123) y
**119 archivos** en `reports/`. **Si lo que encuentra está por detrás, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️⚠️ **EN ARGOS 123 `main` SÍ VENÍA A LA CABEZA POR PRIMERA VEZ, PERO LA RAMA DESIGNADA LLEGÓ
> 36 COMMITS POR DETRÁS EN SU REMOTO.** El `ff-only` local lo resolvió; el `push` lo sincronizó.
>
> **`git merge --ff-only` sigue siendo el primer comando de la sesión, antes de leer `CLAUDE.md`.**
>
> ⚠️ **Y si hereda un borrador, REHAGA TODOS SUS DESLINDES después de restituir la base.**

**La rama de ARGOS 123**: `claude/argos-122-criminal-analysis-n4stuu`. **Compruebe si `main` ya la
absorbió**; si no, trabaje sobre la rama más avanzada, no sobre `main`.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 124** (se confirma con el Bloque 0) |
| **Ventana** | **abre 2026-09-22 08:57 CDMX**, cierra a la **hora real de arranque**, verificada con `TZ=America/Mexico_City date` |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `-movil.html` · `.txt` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-124.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. **Ni un minuto de hueco ni de
solape. Verifique la hora, no la suponga.**

⚠️ **SELLAR LA HORA CAMBIA LA DURACIÓN Y LA DENSIDAD.** **Los dos cocientes se recalculan AL SELLAR**,
y aparecen en portada, en la Valoración y en el bloque de armamento.

**Serie de duraciones**: 75 h 06 (120) → 30 h 02 (121) → 87 h 21 (122) → **23 h 25 (123)**.
**Densidades**: 0,16 → 0,25 → 0,19 → **0,04**.
**Ningún total absoluto es comparable sin normalizar por duración; la densidad sí.**

⚠️ **REGLA SIMÉTRICA, CONFIRMADA TRES VECES**: una ventana **corta** produce **recuperaciones**
(30 h → 3 hechos y 5 `-REC-`; **23 h → 1 hecho y 11 `-REC-`**); una ventana **larga** produce **hechos
propios** (87 h → 17 y 2). **Ni la una ni la otra es indicador de cobertura.**

⚠️⚠️ **ARGOS 123 ES EL CASO EXTREMO: UN SOLO HECHO PROPIO Y ONCE RECUPERACIONES.** Un corte con
cero verdes **no describe un país en calma: describe un día sin boletín.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — **íntegro**. ⚠️ **Lea con especial cuidado «Regla de las dos secciones por nota»
   —que DEROGA la de las cuatro— y «Límite de extensión — el cartelón es telegráfico», que rige por
   encima de cualquier otra consideración de redacción.**
2. `reports/_pendientes.md` — el traspaso. **Los seguimientos abiertos ya dicen qué buscar.**
3. `reports/argos-2026-09-22-fuentes.md` — la edición anterior, con sus limitaciones y su deuda.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR, Y ES DEL COORDINADOR.**

   ⚠️⚠️ **`indice-arg-id.md` EMPIEZA EN `ARG-91-001`. LAS EDICIONES 88, 89 Y 90 NO ESTÁN INDEXADAS.**
   La fórmula correcta es **«no figura en el índice, que cubre de ARGOS 91 en adelante»**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 124 HEREDA

### 3.1 Lo primero del corte

⚠️⚠️ **GUANAJUATO · CORREDOR LAJA-BAJÍO — EL VACÍO MÁS GRANDE QUE DEJA ARGOS 123.**
`periodicocorreo.com.mx` (21-sep) atribuye a la FGE **«23 MUERTOS Y 11 HERIDOS entre el 18 y el
20-sep»** en Valle de Santiago, Salamanca, Irapuato, Celaya, Cortazar y León, y **«14 MUERTOS EN VALLE
DE SANTIAGO EN OCHO DÍAS»**. ⚠️ **FUENTE ÚNICA REGIONAL, SIN BOLETÍN DE LA FGE: NO SE INTEGRÓ NI SE
CITÓ EN EL CARTELÓN.** **Si la cifra es cierta, un solo corredor supera todos los muertos del
documento de ARGOS 123.** **Búsquelo primero: el boletín de la FGE Guanajuato lo cierra.**

⚠️⚠️ **CHIHUAHUA · Cd. Juárez — JOSÉ MANUEL E. C. CUARTA EDICIÓN.**
El fallo condenatorio está dictado y **solo falta la pena**; la audiencia era el 17-sep 09:00.
**ARGOS 121, 122 y 123 gastaron tres, cinco y tres búsquedas: `SIN RESULTADO INDEXADO` las tres.**
⚠️ **NO se afirma que se pospusiera.** **Sugerencia del barrido del Noroeste, no probada aún**: buscar
**«individualización de sanciones» + «José Manuel» SIN restricción de fecha**, porque el boletín de la
pena, si existe, **usaría un slug distinto al del fallo**. **Tres búsquedas, no más.**

### 3.2 Candidatos judiciales vivos

- ⚠️ **ESTADO DE MÉXICO · `fgjem.edomex.gob.mx`** — **SEXTA verificación sin boletín primario.**
  Temoaya (125 a), Coacalco (36 a 3 m, ⚠️ **POSIBLE HOMÓNIMO** con un post de junio-2026) y Hueypoxtla
  (21 a 10 m 15 d). **Ninguna edición ha integrado una sola.** **Valore el agotamiento.**
- ⚠️ **MICHOACÁN · Morelia — FRANCISCO JAVIER T., 93 a 9 m.** ⚠️ **DOMINIO CORREGIDO:
  `comunicacion.fiscaliamichoacan.gob.mx`, NO `fge.michoacan.gob.mx`** — las ediciones anteriores
  intentaron el equivocado.
- ⚠️ **VERACRUZ · agregado del 21-sep**: «26 sentencias condenatorias y 41 vinculaciones».
  **Sin desglose individual no es integrable.** Aclarado en ARGOS 123: el «37 resoluciones» era de
  **otro boletín, del 7-sep**.
- **SAN LUIS POTOSÍ · La Pila — NORMA «N», 4 años + 84 UMA.** Dos fuentes regionales, **ninguna
  institucional**. ⚠️ **NO reproduzca la conversión a pesos de la fuente: usa la UMA de 2025.**
- **TAMAULIPAS · Nuevo Laredo — Carlos, Adrián, Luis y José «N»**: **reclasificado a sentencia**
  (15 a 6 m, 15 a 6 m, 11 a 6 m y 8 años, FGR). **Falta el boletín y el día exacto.**
- **TAMAULIPAS · «El Cholo»**, `ARG-122-SEN-001`: **se mantiene integrada con Medio**. **El folio de
  la FGR sigue sin localizarse** pese a siete medios convergentes.

### 3.3 Armamento

- **QUINTANA ROO · Cancún** — ⚠️ **precisión nueva: NO es un aseguramiento de campo, es una ENTREGA DE
  ARSENAL de 11 carpetas de la FGR a SEDENA.** Por eso ninguna fuente ancla fecha de hecho.
  **Pruebe `site:fgr.org.mx` con «entrega arsenal Sedena Cancún», no probado aún.**
- **NUEVO LEÓN · Los Aldamas** — serie y origen del **Barrett cal. .50** sin localizar; munición
  `CANTIDAD NO DETERMINADA`. ⚠️ **Y fije la fecha del hecho de «4 sujetos abatidos».**
- **SONORA · Puerto Peñasco** — «más de 40 largas» y «casi cuatro mil» cartuchos **siguen sin cifra**.
  **Sigue siendo el mayor volumen no integrado del archivo.**

### 3.4 Casos abiertos de alto impacto

- ⚠️ **GUERRERO · Mochitlán y Quechultenango** — **LA CONTRADICCIÓN EMPEORÓ: SEIS versiones.**
  10 heridos (alcalde) · 5 heridos y 0 muertos (SEDENA) · **8 heridos** (5 policías estatales + 3 GN,
  carpetas de la FGE) · **19, 22 y 29 retenidos**. ⚠️ **Explosivos SIGUEN SIN CONFIRMAR: 🟡 se
  mantiene.** **Dato nuevo: el armamento de cargo SÍ fue devuelto, sin inventario institucional.**
- ⚠️ **CDMX · Tepito** — **CUARTA edición sin boletín.** Tres versiones de edades.
- ⚠️ **CHIAPAS · penal de Ocosingo** — **dato nuevo: la FGE vinculó la MISMA ARMA a otros dos hechos**
  (16-ago en Vida Mejor, 6-sep en 27 de Febrero). **Auditoría sin resultado publicado.**
- **TABASCO · FGET** — ⚠️ **la cifra misma está en disputa: 6 según La Silla Rota, 4 según El Universal.**
- **ESTADO DE MÉXICO · Valle de Chalco** — **dos ataques en menos de 24 horas, cuatro muertos, cero
  detenidos en ambos.** **Vigile si la FGJEM publica algo.**

---

## BLOQUE 4 — LO QUE HAY QUE VOLVER A COMPROBAR EN CADA CORTE

| Qué | Estado al cierre de ARGOS 123 |
|---|---|
| ⚠️ **El bloqueo de egreso alcanza también a los MEDIOS** | **REVERIFICADO Y PERSISTE, TERCERA EDICIÓN.** Cuatro dominios, todos `000`. **Techo ★★★☆☆.** ⚠️ **COMPRUÉBELO DE NUEVO: si la lectura funciona, el techo recupera ★★★★☆ y debe hacerse constar** |
| `docs/solicitud-lista-blanca-egreso.md` | **Sigue sin tramitar. Es la única solución real** |
| `gabinetedeseguridad.gob.mx/resultados/` | **Duodécima verificación consecutiva sin cifra utilizable.** Ninguna cifra suya se usa |
| **Boletín federal de acciones relevantes** | ⚠️ **EL FORMATO VOLVIÓ A CAMBIAR: ARGOS 121 recibió un agregado de tres días; ARGOS 123, un diario, y solo uno.** **Cuatro de los cinco días de su ventana quedaron sin boletín**, verificados con **triple consulta en los cuatro tramos**. ⚠️ **Y `gob.mx/sspc` NO INDEXÓ EL SUYO: solo se alcanzó por republicadores.** **La tercera consulta —título sin `site:`— es la que funciona** |
| ⚠️ **Dominios oficiales mal referenciados** | **Corregido**: Oaxaca es `fge.oaxaca.gob.mx`, **no** `fiscaliaoaxaca.gob.mx`. ⚠️ **SIN VERIFICAR, compruébelos**: Querétaro (`sscqro.gob.mx`), Hidalgo (`s-seguridad.hidalgo.gob.mx`), Tlaxcala (`ssc.tlaxcala.gob.mx`) |
| `fiscaliaguerrero.gob.mx` | **Quinta edición sin publicar indexable.** **La vía que funciona es el republicador, no el dominio** |
| **SSC y FGJ de la Ciudad de México** | **Cero boletín sobre Tepito, TERCERA edición.** ⚠️ **Y ahora hay TRES versiones de edades**: 25-30, 18-19 y 15-20 |
| **FGET Tabasco** | **Sin boletín de las seis ejecuciones del 15-sep.** Nueva información parcial: **3 de las 6 ubicadas** —Centro (2) y Cárdenas (1)—; **las otras tres sin aclarar** |

---

## BLOQUE 5 — BARRIDO REGIONAL Y ROTACIÓN

`CLAUDE.md` exige **seis agentes `barrido-regional` en paralelo**. **Lánzelos en un solo mensaje**, con
la deuda del Bloque 3 al frente y **tope duro de 2-3 búsquedas por eje**.
⚠️ **Dé a cada agente la ventana COMPLETA con sus días, no «hoy».**

⚠️ **CICLO QUE TOCA: CICLO B — Noreste + Golfo encabezan el triaje judicial.**
⚠️⚠️ **PERO LA PRIORIDAD VENCE AL CICLO: BAJA CALIFORNIA SUR quedó `NO REVISADA` en ARGOS 123 y
ENCABEZA, aunque sea del Noroeste.** **Saldar cobertura vence a mantener el turno.**

⚠️ **El Ciclo C de ARGOS 123 SÍ produjo candidato judicial** —Morelia, 93 años 9 meses— **y saldó
Yucatán en los dos módulos**, a diferencia del Ciclo B de ARGOS 121, que no produjo ninguno.
**Declare el ciclo y su rendimiento: se mide, no se supone.**

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  **sin restricción de dominio** antes de cerrarla.
- ⚠️⚠️ **RECALL NACIONAL DEL COORDINADOR, ANTES DE CERRAR LOS BARRIDOS. DECIMOCUARTA EDICIÓN
CONSECUTIVA APORTANDO LOS HECHOS DE MAYOR GRAVEDAD.** En ARGOS 123 trajo **los tres homicidios
múltiples del documento** —Valle de Chalco, Tetecala y Tehuantepec— y ⚠️ **los seis barridos
regionales no detectaron ni uno solo**. **No es sustituible por más equipos.**
- ⚠️ **Arbitraje del coordinador sobre las clasificaciones, EN LAS DOS DIRECCIONES.** En ARGOS 123
  se ejerció **al alza** (sierra de Sinaloa, de 🟡 a 🔴, porque quién inició **sí** estaba determinado)
  y **a la baja** (Quechultenango **se mantuvo 🟡** pese a la tentación de subirlo, porque **ninguna
  agravante tasada concurría acreditada**). **Las dos decisiones se declaran.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️⚠️ **UNA CIFRA EXACTA PUEDE SER PRELIMINAR Y QUEDAR SUPERADA POR UNA POSTERIOR SIN CIFRA — TRAMPA NUEVA DE ARGOS 123** | **Puerto Peñasco**: «33 armas largas» era del **20-sep**; el relato posterior de la autoridad da **«más de 40»**. **Tener una cifra exacta no basta: hay que comprobar que no la haya superado el emisor.** **Solo se integraron las 2 Minimi** |
| ⚠️⚠️ **UN OPERATIVO DE DOS DÍAS NO ES UN EVENTO DE ASEGURAMIENTO — TRAMPA NUEVA DE ARGOS 123** | **Puerto Peñasco**: las **7 detenciones son del 18-sep** y el **arsenal del cateo del 19**. **Los detenidos solo se cuentan en el conteo de armamento si son del MISMO evento de aseguramiento** |
| ⚠️⚠️ **UNA CIFRA QUE UNA EDICIÓN DECLARÓ Y NO ADOPTÓ NO ES UN HECHO NUEVO CUANDO SE CONFIRMA** | **Angamacutiro**: `ARG-121-REC-005` **ya citó** los 28 cateos y los 18 detenidos. Publicarlo como hecho propio **infló el corte en 1 hecho y 1 verde**. **Va como `-REC-` o como fe de erratas, según el caso, pero NO al semáforo** |
| ⚠️ **UN AGREGADO DE VÍCTIMAS NO PUEDE CERRAR UNA CIFRA QUE UNA FICHA DECLARA CONTRADICHA** | La Valoración de ARGOS 123 daba «7 muertos y 8 heridos», que **solo salía adoptando en silencio la cifra alta de Valle de Santiago**. **Se publica el RANGO** |
| ⚠️ **UN DESLINDE PUEDE AFIRMAR ALGO FALSO Y PASAR DESAPERCIBIDO** | «otros municipios» frente a `ARG-121-REC-005`, **siendo los mismos dos**. **`editor-duplicidad` existe para esto** |
| ⚠️ **UN BOLETÍN QUE LLEGA TARDE CORRIGE AL ALZA UNA EDICIÓN CERRADA, Y ESO NO ES UN FALLO DE AQUELLA** | `ARG-122-FE-001` corrige **Coyuca de Benítez** con **58 largas, 32 cortas, 314 cargadores y 8,010 cartuchos**. ⚠️ **Y LA FE DE ERRATAS NO VA AL CARTELÓN** |
| ⚠️ **UN BARRIDO PUEDE TRAER UN HECHO YA PUBLICADO COMO NUEVO** | **Nonoava, ARGOS 121.** **Solo el `grep` del coordinador lo detuvo.** **En ARGOS 123 no se repitió** |
| ⚠️ **LA HORA, CUANDO SE PUBLICA, DECIDE LA VENTANA SIN RESERVA** | **Quechultenango trae 12:00, 15:00 y 18:00** y eso permitió **asignarlo sin reserva a la ventana anterior**. **Búsquela siempre** |
| ⚠️ **UNA CIFRA CONTRADICHA SE ARBITRA POR PROCEDENCIA, NO POR MAYORÍA** | **7 detenidos** en Puerto Peñasco (titular de la SSPC federal) frente a 10; **10 años** del menor de Tuxtla (Fiscal General) frente a 12 |
| ⚠️ **SIN EMISOR INSTITUCIONAL NO SE ARBITRA EN ABSOLUTO** | **Valle de Santiago: 3 o 4 muertos, y la FGE no publicó cifra.** **Se publican las dos versiones** |
| ⚠️ **EL RESUMIDOR FABRICA FECHAS, FOLIOS Y AHORA TOPÓNIMOS** | **«Mazatlán, Michoacán» no existe.** **Veintitrés fechas y folios inventados en seis cortes, más un municipio** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado quince ediciones |
| ***Liveblog*** | **Nunca fecha un hecho ni basta como fuente única** |
| **«Más de» y «casi» no son cifra** | **Pero si el cuerpo del boletín la fija, se integra** |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| ⚠️ **Corroboración asimétrica** | **El nivel lo fija el campo PEOR sostenido** |
| **Un delito y su detención son dos eventos** | **ARGOS 123 lo aplicó dos veces**: Tuxtla (🔴 ataque / 🟢 15 detenidos) y sierra de Sinaloa (🔴 agresión / 🟢 aseguramiento) |
| **Cifras derivadas** | Todo total es **cálculo propio** y se declara. ⚠️ **Recalcule TODO cociente DESPUÉS de las correcciones de los controles** |
| ⚠️ **LO QUE NO SE DERIVA, DIVERGE** | **La móvil y el texto se GENERAN del cartelón, nunca se escriben aparte.** **Los dos generadores derivan ya el turno del pie del cartelón** |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

- ⚠️⚠️ **DOS APARTADOS POR FICHA: «HECHO» Y «TRAZABILIDAD». NADA MÁS.** **Las fuentes, los deslindes y
  las marcas de reserva NO se suprimen: son dato, no prosa, y van comprimidos en Trazabilidad**
  —recuento por tipo, nombrados solo los que llevan fecha en la ruta, lista íntegra al archivo de
  fuentes—.
- ⚠️ **EL ANÁLISIS VIVE UNA SOLA VEZ, AL CIERRE**: Valoración (5 líneas) y Conclusiones de inteligencia
  criminal (5 líneas). **No ficha por ficha.**
- ⚠️ **CADA HECHO EN DOS LUGARES COMO MÁXIMO**: un renglón en **«PANORAMA DEL CORTE»** (página 2,
  **único listado resumido**, con el **total nacional que no se reimprime en ningún otro sitio**) y su
  **ficha**. **Prohibida una tercera aparición.**
- ⚠️ **La portada lleva UN SOLO recuadro**, **«LO QUE DEBE HACER EL MANDO»**, con **cinco líneas de
  ACCIÓN**. **No repite titulares.**
- ⚠️ **TRES RECUADROS COMO MÁXIMO EN TODO EL CARTELÓN.** **NINGUNO EXPLICA UN COLOR NI UN MECANISMO
  DEL MÉTODO.**
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`; el ARG-ID
  `-FE-` se registra en el índice. ⚠️ **ARGOS 123 infringió esto con las cifras de Coyuca y
  `procedencia-cifras` lo detuvo.**
- ⚠️ **Toda ficha `-REC-` lleva su ventana de origen declarada, se muestra atenuada y queda FUERA del
  semáforo, del mapa, del radar y de todos los totales.**
- **Toda cifra en cero lleva al lado el dato que la explica.** **Las categorías en cero se muestran
  atenuadas: la ausencia es dato.**
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`
  —`exec wide` si tiene muchas columnas—. **Nada de `sem-item` fuera de la portada.**

### Estructura de páginas que hereda ARGOS 124

**ARGOS 123 salió en DOCE páginas** con 17 hechos, 2 recuperaciones y 1 sentencia: portada ·
panorama del corte · crimen organizado (I) a (VI) · armamento · sentencias · candidatos y cobertura ·
valoración y conclusiones. **ARGOS 121 salió en nueve con 3 hechos; ARGOS 120, en trece con 19.**
**El número de páginas lo fija el volumen, no la costumbre: si un bloque crece se reparte entre más
páginas, nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de reports/argos-2026-09-22.html, sustituir el <title>, CORTE_FECHA,
#    EVENTOS y EVENTOS_ARM. ⚠️ CORTE_FECHA y el <title> SE HEREDAN y es fácil olvidarlos.
#    ⚠️⚠️ NO los sustituya con un sed GLOBAL: alcanza el bloque de datos y el renderizador.
#    Tramos de la plantilla de ARGOS 123 (reports/argos-2026-09-22.html):
#      (a) cabecera: líneas 1-431   (el <title> está en la línea 5)
#      (b) <script> + MEXICO_VIEWBOX + MEXICO_PATHS: hasta antes de const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>
#    ⚠️ CONSTRUIR POR PARTES EN UN DIRECTORIO DE TRABAJO Y ENSAMBLAR FUNCIONA BIEN Y ES REPETIBLE.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 123 <FECHA> 122 2026-09-22 <HORA>

# 3. Texto: NO se escribe, se genera. Deriva el turno del corte del pie del cartelón.
python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt

# 4. La validación debe decir "validación OK" y los contadores deben coincidir con el semáforo.
#    Si no, se corrige la HERRAMIENTA, no su salida.
#    ⚠️ REGENERE MÓVIL Y TEXTO DESPUÉS DE CADA CORRECCIÓN DEL ESCRITORIO.
```

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes, Nayarit
y Guanajuato son «Occidente»**; **Zacatecas y San Luis Potosí son «Noreste»**; **Guerrero es
«Sureste»**; **Durango es «Noroeste»**; **Querétaro e Hidalgo son «Centro»**; **Veracruz y Tabasco son
«Golfo»**. Un `region:` mal puesto **coloca el eco del radar en el sector equivocado y nadie lo nota**.

⚠️ **CADA ARG-ID DE `EVENTOS` Y DE `EVENTOS_ARM` DEBE TENER UN ANCLA `id=` EN EL DOCUMENTO**, y también
los `-REC-` y `-SEN-` citados.

**ARGOS 123 dejó el validador escrito y funcionando.** Comprueba con `node:vm` sobre el `<script>`:
**32 entidades en `MEXICO_PATHS`**, **cada `estado:` existe**, **cada `region:` coincide con
`STATE_REGION`**, **ninguna fecha cae fuera de la ventana**, **ningún ARG-ID duplicado**, **cada ARG-ID
resuelve a un ancla**, **cada enlace `href="#ARG-…"` resuelve**, **el semáforo derivado coincide con la
portada y con `radar-stats`**, **hay exactamente un `<body>`**, **toda tabla está envuelta exactamente
una vez**, **cero `-FE-`**, **`sem-item` solo en portada**, **cada ficha tiene EXACTAMENTE dos
apartados, «HECHO» y «TRAZABILIDAD»**, **no existe «Corroboración» ni «Explotación ARGOS»**,
**ningún recuadro supera las cinco líneas**, **máximo 3 recuadros**, y **el pie aparece en todas las
páginas**.
⚠️ **Las `const` NO se exponen como propiedades del contexto**: hay que devolverlas con una expresión
final, `vm.runInContext(code + '\n;({EVENTOS,EVENTOS_ARM,MEXICO_PATHS,STATE_REGION,CORTE_FECHA})', ctx)`.

⚠️ **RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS**, y **vuelva a recalcularlo DESPUÉS de las
correcciones de los controles**. **En ARGOS 123 los controles cambiaron seis totales de golpe.**

*Notas del generador móvil, que NO son defectos*: **no lleva `<script>`** · **`table-wrap` aparece en
cero** —se renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**. **Verifíquelo contando ARG-ID, no etiquetas `<table>`.**

---

## BLOQUE 9 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que una cifra ya declarada por una edición anterior se cuente como hecho propio, **y que un deslinde afirme algo que el índice no puede sostener** |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **que una cifra preliminar superada se publique como definitiva**, y **que un agregado cierre en silencio una contradicción declarada** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **ARGOS 121 y ARGOS 123 los ejecutaron y los dos devolvieron `CORREGIR ANTES DE PUBLICAR` con
hallazgos reales las dos veces. NO ROMPA LA RACHA.**
⚠️ **En ARGOS 123 cambiaron SEIS totales nacionales y reclasificaron un hecho.**

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos,
sobre los controles y sobre sus propias instrucciones. ⚠️ **En ARGOS 123 el coordinador verificó por su
cuenta el hallazgo de Puerto Peñasco y lo encontró MAYOR de lo que el control apuntaba.**
**Un control acierta en la dirección; el coordinador fija la magnitud.**

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS**, y **toda disposición es
   expresa** —cerrado, sin avance o fuera de ventana—.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-` y los `-REC-`**—.
3. Escribir `reports/argos-<FECHA>-fuentes.md` con el registro del barrido, el ciclo aplicado, los
   arbitrajes en las dos direcciones, los hallazgos de los controles y las limitaciones de herramienta.
4. **Escribir `reports/_arranque-ARGOS-124.md`** y borrar este archivo.
5. **Empujar a la rama designada** y **mergear a `main`**, verificando que quedó.
