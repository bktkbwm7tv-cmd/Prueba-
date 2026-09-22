# ORDEN DE ARRANQUE — ARGOS 123

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino
en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 122** (corte 2026-09-21).

⚠️ **El mensaje de arranque listo para pegar en una sesión nueva está en
`reports/_ordenes-ARGOS-123.txt`.** Este archivo es el detalle; aquél es la orden.

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

**Estado que debe encontrar ARGOS 123**: última edición `argos-2026-09-21` (ARGOS 122) y
**115 archivos** en `reports/` —contados tras el cierre de ARGOS 122, este archivo y la orden de arranque incluidos—. **Si lo que encuentra está por detrás, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️⚠️ **ESTO YA FALLÓ DIECISIETE EDICIONES SEGUIDAS Y VOLVERÁ A FALLAR.** La rama que asigna el
> entorno **llega desactualizada**. En ARGOS 122 llegó **sin la serie restituida**.
>
> **`git merge --ff-only` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
>
> ⚠️ **Y si hereda un borrador, REHAGA TODOS SUS DESLINDES después de restituir la base.**

**La rama de ARGOS 122**: `claude/argos-122-criminal-analysis-n4stuu`. **Compruebe si `main` ya la
absorbió**; si no, trabaje sobre la rama más avanzada, no sobre `main`.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 123** (se confirma con el Bloque 0) |
| **Ventana** | **abre 2026-09-21 08:57 CDMX**, cierra a la **hora real de arranque**, verificada con `TZ=America/Mexico_City date` |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `-movil.html` · `.txt` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-124.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. **Ni un minuto de hueco ni de
solape. Verifique la hora, no la suponga.**

⚠️ **SELLAR LA HORA CAMBIA LA DURACIÓN Y LA DENSIDAD.** **Los dos cocientes se recalculan AL SELLAR**,
y aparecen en portada, en la Valoración y en el bloque de armamento.

**Serie de duraciones**: 117 h 50 (119) → 75 h 06 (120) → 30 h 02 (121) → **87 h 21 (122)**.
**Densidades**: 0,19 → 0,16 → 0,25 → 0,10 → **0,19**.
**Ningún total absoluto es comparable sin normalizar por duración; la densidad sí.**

⚠️ **REGLA SIMÉTRICA, CONFIRMADA EN LAS DOS DIRECCIONES**: una ventana **corta** produce
**recuperaciones** (30 h → 3 hechos y 5 `-REC-`); una ventana **larga** produce **hechos propios**
(87 h → 17 hechos y 2 `-REC-`). **Ni la una ni la otra es indicador de cobertura.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — **íntegro**. ⚠️ **Lea con especial cuidado «Regla de las dos secciones por nota»
   —que DEROGA la de las cuatro— y «Límite de extensión — el cartelón es telegráfico», que rige por
   encima de cualquier otra consideración de redacción.**
2. `reports/_pendientes.md` — el traspaso. **Los seguimientos abiertos ya dicen qué buscar.**
3. `reports/argos-2026-09-21-fuentes.md` — la edición anterior, con sus limitaciones y su deuda.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR, Y ES DEL COORDINADOR.**

   ⚠️⚠️ **`indice-arg-id.md` EMPIEZA EN `ARG-91-001`. LAS EDICIONES 88, 89 Y 90 NO ESTÁN INDEXADAS.**
   La fórmula correcta es **«no figura en el índice, que cubre de ARGOS 91 en adelante»**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 123 HEREDA

### 3.1 Lo primero del corte

⚠️⚠️ **SONORA · PUERTO PEÑASCO — LA CIFRA EXACTA DEL ARSENAL DE CERRADA DEL SOL.**
**ES EL MAYOR VOLUMEN NO INTEGRADO DEL CORTE ANTERIOR.** La autoridad publicó **«MÁS DE 40 ARMAS
LARGAS»** y **«casi cuatro mil» cartuchos**; la cifra preliminar de **33** quedó superada y
**ARGOS 122 solo integró las DOS AMETRALLADORAS MINIMI**, única cantidad expresa. **Un boletín con
el desglose exacto lo cierra y corrige el total nacional al alza.**
⚠️ **Y CON ÉL VA UN PENDIENTE DE VIDAS**: el operativo derivó del **SECUESTRO DE OCHO MINEROS
ARTESANALES DE LA REGIÓN DE SIERRA PINTA**. **Se rescataron tres. LAS OTRAS CINCO SIGUEN SIN PARADERO
PUBLICADO.**

⚠️⚠️ **CHIHUAHUA · Ciudad Juárez (Distrito Judicial Bravos) — JOSÉ MANUEL E. C.**
**SIGUE SIENDO EL CANDIDATO MÁS MADURO DEL ARCHIVO: el «fallo condenatorio» YA ESTÁ DICTADO y solo
falta la pena.** La audiencia de individualización estaba fijada para el **jueves 17-sep a las 09:00**.
**ARGOS 121 gastó tres búsquedas y ARGOS 122 cinco formulaciones distintas: `SIN RESULTADO INDEXADO EN
VENTANA` las dos veces.** ⚠️ **NO se afirma que se pospusiera: eso no está acreditado.**
**Tercera edición. Búsquelo, pero no gaste más de tres búsquedas.**

### 3.2 Candidatos judiciales vivos

- ⚠️ **MICHOACÁN · Morelia — FRANCISCO JAVIER T., 93 años 9 meses** (secuestro y homicidio agravado).
  **Cuatro republicadores con fecha en la ruta del 17-sep, ninguno del dominio de la FGE.**
  `PENDIENTE DE CONFIRMACIÓN OFICIAL`. **El boletín de `fge.michoacan.gob.mx` lo cierra.**
- ⚠️ **SAN LUIS POTOSÍ · La Pila — NORMA «N», 4 años 2 meses** y multa de **84 UMA (9,503.76 pesos)**,
  FGR. **Fuente única regional.** `PENDIENTE DE CONFIRMACIÓN OFICIAL`.
- ⚠️ **VERACRUZ · agregado de la FGE del 18-sep** — «16 sentencias condenatorias y 1 fallo». ⚠️ **El
  título del portal dice «37 resoluciones» y la cobertura «50 / 16 sentencias».** **Sin desglose
  individual no es integrable.**
- ⚠️ **TAMAULIPAS · Nuevo Laredo — «EL CHOLO», 332 años 6 meses**, `ARG-122-SEN-001`, **INTEGRADA con
  confianza Medio**. ⚠️ **Busque el comunicado primario de la FGR con su folio: subiría la confianza.
  Y si aparece evidencia de que no existe, PROCEDE FE DE ERRATAS Y RETIRO.**
- ⚠️ **BAJA CALIFORNIA · Tijuana — Luis Martín «N»**: seis medios coinciden en **26 años 8 meses,
  500 UMA y 874,680 pesos**; el boletín **fgebc.gob.mx/boletines/12722** dice **23 años sin nombre**.
  **Dos campos individualizadores nuevos** —hecho del 1-abr-2025 en avenida Revolución; captura el
  13-jul-2025 en Monterrey—. `POSIBLE CASO HOMÓNIMO`.
- ⚠️ **ESTADO DE MÉXICO · `fgjem.edomex.gob.mx`**: **QUINTA verificación sin boletín primario.**
  Temoaya (125 años), Coacalco (36a 3m), Hueypoxtla (21a 10m 15d). **Ninguna edición ha integrado una.**
- **TAMAULIPAS · Nuevo Laredo — Carlos, Adrián, Luis y José «N»**: `FECHA NO FIJADA`, **TERCER intento
  fallido**. ⚠️ **Procede declararlo `FECHA NO DETERMINABLE BAJO BLOQUEO DE EGRESO`.**

### 3.3 Candidatos de armamento con umbral de agotamiento a punto de cumplirse

- ⚠️ **AGUASCALIENTES · Cosío, com. El Salero** — **17 largas, una cal. .50, «más de 1,500» cartuchos,
  3 detenidos**. `FECHA NO FIJADA`, **CUARTO intento fallido**. **Sigue siendo el mayor volumen
  pendiente del archivo.** ⚠️⚠️ **QUINTO INTENTO Y, SI FALLA, PROCEDE EL UMBRAL DE AGOTAMIENTO**, como
  en La Trinitaria y Villa González Ortega.
- ⚠️ **MICHOACÁN · municipio consignado como «MAZATLÁN»** en el boletín federal del 17-sep — 2 cortas,
  2 largas, 5 cargadores, 2 detenidos, 1 vehículo blindado. **NO EXISTE ese municipio en Michoacán.**
  `MUNICIPIO NO VERIFICADO`. **NO INTEGRADO. Fíjelo o retírelo.**
- **QUINTANA ROO · Cancún** (4 largas, 12 cortas, 20 cargadores, 226 cartuchos). `FECHA NO FIJADA`,
  **tercer intento**; **no se le asignó búsqueda en ARGOS 122**.

### 3.4 Casos abiertos de alto impacto

- ⚠️ **GUERRERO · Mochitlán y Quechultenango** (`ARG-122-REC-001`) — ⚠️⚠️ **LA CONTRADICCIÓN MÁS GRAVE
  DEL ARCHIVO ACTUAL: DOS EMISORES INSTITUCIONALES SE CONTRADICEN ENTRE SÍ.** El **alcalde** reporta
  **1 muerto y 10 heridos**; la **SEDENA** reporta **5 heridos y CERO MUERTOS**; la **FGE** dice que
  **no hay denuncias por fallecidos**. Retenidos **29 frente a 19**. ⚠️ **Y si se confirma el USO DE
  EXPLOSIVOS, alegado y no confirmado, el hecho SUBE A ROJO.** **Qué armamento de cargo fue sustraído
  a los 29 uniformados y si se recuperó.**
- ⚠️ **GUANAJUATO · Valle de Santiago** (`ARG-122-003`) — ⚠️ **LA FGE NO HA PUBLICADO CIFRA DE
  VÍCTIMAS y circulan 3 y 4 muertos.** `CIFRA CONTRADICHA — NO ARBITRADA`.
- ⚠️ **CHIAPAS · Tuxtla Gutiérrez, Las Granjas** — ⚠️ **AUDITORÍA DEL PENAL DE OCOSINGO**, desde donde
  la FGE dice que un sentenciado por homicidio calificado **ordenó el ataque**. **Situación jurídica
  de los 15 detenidos.**
- **GUANAJUATO · Celaya** — **situación del policía municipal herido**; **cero detenidos**.
- **NUEVO LEÓN · Los Aldamas** — **serie y origen del Barrett cal. .50**; **munición sin cifra**.
- **SINALOA · sierra en límites con Durango** — ⚠️⚠️ **EL MUNICIPIO, que ninguna fuente publica**;
  **iniciador y carga de los 40 AEI**; ⚠️ **COTEJO CONTRA LOS 53 DE MAZATLÁN Y LOS 84 DE LA NORIA:
  177 artefactos en trece días en el mismo corredor.**
- **GUANAJUATO · San José Iturbide** — **titularidad de la planta y permisos**, no adoptados;
  **cero detenidos en el mayor decomiso de la administración**.

---

## BLOQUE 4 — LO QUE HAY QUE VOLVER A COMPROBAR EN CADA CORTE

| Qué | Estado al cierre de ARGOS 122 |
|---|---|
| ⚠️ **El bloqueo de egreso alcanza también a los MEDIOS** | **REVERIFICADO Y PERSISTE, TERCERA EDICIÓN.** Cuatro dominios, todos `000`. **Techo ★★★☆☆.** ⚠️ **COMPRUÉBELO DE NUEVO: si la lectura funciona, el techo recupera ★★★★☆ y debe hacerse constar** |
| `docs/solicitud-lista-blanca-egreso.md` | **Sigue sin tramitar. Es la única solución real** |
| `gabinetedeseguridad.gob.mx/resultados/` | **Duodécima verificación consecutiva sin cifra utilizable.** Ninguna cifra suya se usa |
| **Boletín federal de acciones relevantes** | ⚠️ **EL FORMATO VOLVIÓ A CAMBIAR: ARGOS 121 recibió un agregado de tres días; ARGOS 122, un diario, y solo uno.** **Cuatro de los cinco días de su ventana quedaron sin boletín**, verificados con **triple consulta en los cuatro tramos**. ⚠️ **Y `gob.mx/sspc` NO INDEXÓ EL SUYO: solo se alcanzó por republicadores.** **La tercera consulta —título sin `site:`— es la que funciona** |
| ⚠️ **Dominios oficiales mal referenciados** | **Corregido**: Oaxaca es `fge.oaxaca.gob.mx`, **no** `fiscaliaoaxaca.gob.mx`. ⚠️ **SIN VERIFICAR, compruébelos**: Querétaro (`sscqro.gob.mx`), Hidalgo (`s-seguridad.hidalgo.gob.mx`), Tlaxcala (`ssc.tlaxcala.gob.mx`) |
| `fiscaliaguerrero.gob.mx` | **Quinta edición sin publicar indexable.** **La vía que funciona es el republicador, no el dominio** |
| **SSC y FGJ de la Ciudad de México** | **Cero boletín sobre Tepito, TERCERA edición.** ⚠️ **Y ahora hay TRES versiones de edades**: 25-30, 18-19 y 15-20 |
| **FGET Tabasco** | **Sin boletín de las seis ejecuciones del 15-sep.** Nueva información parcial: **3 de las 6 ubicadas** —Centro (2) y Cárdenas (1)—; **las otras tres sin aclarar** |

---

## BLOQUE 5 — BARRIDO REGIONAL Y ROTACIÓN

`CLAUDE.md` exige **seis agentes `barrido-regional` en paralelo**. **Lánzelos en un solo mensaje**, con
la deuda del Bloque 3 al frente y **tope duro de 2-3 búsquedas por eje**.
⚠️ **Dé a cada agente la ventana COMPLETA con sus días, no «hoy».**

⚠️ **CICLO QUE TOCA: CICLO A — Noroeste + Centro encabezan el triaje judicial.**
⚠️⚠️ **PERO LA PRIORIDAD VENCE AL CICLO: TAMAULIPAS y COAHUILA quedaron por debajo del estándar en
armamento y CAMPECHE solo recibió consulta general. LAS TRES ENCABEZAN AUNQUE SEAN DEL NORESTE Y DEL
SURESTE.** **Saldar cobertura vence a mantener el turno.**

⚠️ **El Ciclo C de ARGOS 122 SÍ produjo candidato judicial** —Morelia, 93 años 9 meses— **y saldó
Yucatán en los dos módulos**, a diferencia del Ciclo B de ARGOS 121, que no produjo ninguno.
**Declare el ciclo y su rendimiento: se mide, no se supone.**

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  **sin restricción de dominio** antes de cerrarla.
- ⚠️⚠️ **RECALL NACIONAL DEL COORDINADOR, ANTES DE CERRAR LOS BARRIDOS. DECIMOTERCERA EDICIÓN
  CONSECUTIVA APORTANDO LOS HECHOS DE MAYOR GRAVEDAD.** En ARGOS 122 trajo **cuatro de los cinco
  hechos rojos**, y ⚠️ **los seis barridos regionales NO detectaron ninguno de los tres ataques con
  víctimas civiles mortales del corte**. **No es sustituible por más equipos.**
- ⚠️ **Arbitraje del coordinador sobre las clasificaciones, EN LAS DOS DIRECCIONES.** En ARGOS 122
  se ejerció **al alza** (sierra de Sinaloa, de 🟡 a 🔴, porque quién inició **sí** estaba determinado)
  y **a la baja** (Quechultenango **se mantuvo 🟡** pese a la tentación de subirlo, porque **ninguna
  agravante tasada concurría acreditada**). **Las dos decisiones se declaran.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️⚠️ **UNA CIFRA EXACTA PUEDE SER PRELIMINAR Y QUEDAR SUPERADA POR UNA POSTERIOR SIN CIFRA — TRAMPA NUEVA DE ARGOS 122** | **Puerto Peñasco**: «33 armas largas» era del **20-sep**; el relato posterior de la autoridad da **«más de 40»**. **Tener una cifra exacta no basta: hay que comprobar que no la haya superado el emisor.** **Solo se integraron las 2 Minimi** |
| ⚠️⚠️ **UN OPERATIVO DE DOS DÍAS NO ES UN EVENTO DE ASEGURAMIENTO — TRAMPA NUEVA DE ARGOS 122** | **Puerto Peñasco**: las **7 detenciones son del 18-sep** y el **arsenal del cateo del 19**. **Los detenidos solo se cuentan en el conteo de armamento si son del MISMO evento de aseguramiento** |
| ⚠️⚠️ **UNA CIFRA QUE UNA EDICIÓN DECLARÓ Y NO ADOPTÓ NO ES UN HECHO NUEVO CUANDO SE CONFIRMA** | **Angamacutiro**: `ARG-121-REC-005` **ya citó** los 28 cateos y los 18 detenidos. Publicarlo como hecho propio **infló el corte en 1 hecho y 1 verde**. **Va como `-REC-` o como fe de erratas, según el caso, pero NO al semáforo** |
| ⚠️ **UN AGREGADO DE VÍCTIMAS NO PUEDE CERRAR UNA CIFRA QUE UNA FICHA DECLARA CONTRADICHA** | La Valoración de ARGOS 122 daba «7 muertos y 8 heridos», que **solo salía adoptando en silencio la cifra alta de Valle de Santiago**. **Se publica el RANGO** |
| ⚠️ **UN DESLINDE PUEDE AFIRMAR ALGO FALSO Y PASAR DESAPERCIBIDO** | «otros municipios» frente a `ARG-121-REC-005`, **siendo los mismos dos**. **`editor-duplicidad` existe para esto** |
| ⚠️ **UN BOLETÍN QUE LLEGA TARDE CORRIGE AL ALZA UNA EDICIÓN CERRADA, Y ESO NO ES UN FALLO DE AQUELLA** | `ARG-122-FE-001` corrige **Coyuca de Benítez** con **58 largas, 32 cortas, 314 cargadores y 8,010 cartuchos**. ⚠️ **Y LA FE DE ERRATAS NO VA AL CARTELÓN** |
| ⚠️ **UN BARRIDO PUEDE TRAER UN HECHO YA PUBLICADO COMO NUEVO** | **Nonoava, ARGOS 121.** **Solo el `grep` del coordinador lo detuvo.** **En ARGOS 122 no se repitió** |
| ⚠️ **LA HORA, CUANDO SE PUBLICA, DECIDE LA VENTANA SIN RESERVA** | **Quechultenango trae 12:00, 15:00 y 18:00** y eso permitió **asignarlo sin reserva a la ventana anterior**. **Búsquela siempre** |
| ⚠️ **UNA CIFRA CONTRADICHA SE ARBITRA POR PROCEDENCIA, NO POR MAYORÍA** | **7 detenidos** en Puerto Peñasco (titular de la SSPC federal) frente a 10; **10 años** del menor de Tuxtla (Fiscal General) frente a 12 |
| ⚠️ **SIN EMISOR INSTITUCIONAL NO SE ARBITRA EN ABSOLUTO** | **Valle de Santiago: 3 o 4 muertos, y la FGE no publicó cifra.** **Se publican las dos versiones** |
| ⚠️ **EL RESUMIDOR FABRICA FECHAS, FOLIOS Y AHORA TOPÓNIMOS** | **«Mazatlán, Michoacán» no existe.** **Veintitrés fechas y folios inventados en seis cortes, más un municipio** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado quince ediciones |
| ***Liveblog*** | **Nunca fecha un hecho ni basta como fuente única** |
| **«Más de» y «casi» no son cifra** | **Pero si el cuerpo del boletín la fija, se integra** |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| ⚠️ **Corroboración asimétrica** | **El nivel lo fija el campo PEOR sostenido** |
| **Un delito y su detención son dos eventos** | **ARGOS 122 lo aplicó dos veces**: Tuxtla (🔴 ataque / 🟢 15 detenidos) y sierra de Sinaloa (🔴 agresión / 🟢 aseguramiento) |
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
  `-FE-` se registra en el índice. ⚠️ **ARGOS 122 infringió esto con las cifras de Coyuca y
  `procedencia-cifras` lo detuvo.**
- ⚠️ **Toda ficha `-REC-` lleva su ventana de origen declarada, se muestra atenuada y queda FUERA del
  semáforo, del mapa, del radar y de todos los totales.**
- **Toda cifra en cero lleva al lado el dato que la explica.** **Las categorías en cero se muestran
  atenuadas: la ausencia es dato.**
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`
  —`exec wide` si tiene muchas columnas—. **Nada de `sem-item` fuera de la portada.**

### Estructura de páginas que hereda ARGOS 123

**ARGOS 122 salió en DOCE páginas** con 17 hechos, 2 recuperaciones y 1 sentencia: portada ·
panorama del corte · crimen organizado (I) a (VI) · armamento · sentencias · candidatos y cobertura ·
valoración y conclusiones. **ARGOS 121 salió en nueve con 3 hechos; ARGOS 120, en trece con 19.**
**El número de páginas lo fija el volumen, no la costumbre: si un bloque crece se reparte entre más
páginas, nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de reports/argos-2026-09-21.html, sustituir el <title>, CORTE_FECHA,
#    EVENTOS y EVENTOS_ARM. ⚠️ CORTE_FECHA y el <title> SE HEREDAN y es fácil olvidarlos.
#    ⚠️⚠️ NO los sustituya con un sed GLOBAL: alcanza el bloque de datos y el renderizador.
#    Tramos de la plantilla de ARGOS 122 (reports/argos-2026-09-21.html):
#      (a) cabecera: líneas 1-431   (el <title> está en la línea 5)
#      (b) <script> + MEXICO_VIEWBOX + MEXICO_PATHS: hasta antes de const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>
#    ⚠️ CONSTRUIR POR PARTES EN UN DIRECTORIO DE TRABAJO Y ENSAMBLAR FUNCIONA BIEN Y ES REPETIBLE.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 123 <FECHA> 122 2026-09-21 <HORA>

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

**ARGOS 122 dejó el validador escrito y funcionando.** Comprueba con `node:vm` sobre el `<script>`:
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
correcciones de los controles**. **En ARGOS 122 los controles cambiaron seis totales de golpe.**

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

⚠️ **ARGOS 121 y ARGOS 122 los ejecutaron y los dos devolvieron `CORREGIR ANTES DE PUBLICAR` con
hallazgos reales las dos veces. NO ROMPA LA RACHA.**
⚠️ **En ARGOS 122 cambiaron SEIS totales nacionales y reclasificaron un hecho.**

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos,
sobre los controles y sobre sus propias instrucciones. ⚠️ **En ARGOS 122 el coordinador verificó por su
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
