# ORDEN DE ARRANQUE — ARGOS 122

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino
en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 121** (corte 2026-09-17).

⚠️ **El mensaje de arranque listo para pegar en una sesión nueva está en
`reports/_ordenes-ARGOS-122.txt`.** Este archivo es el detalle; aquél es la orden.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en TODO el cartelón
git fetch origin                                   # traer el estado real
git branch -r | sed 's#origin/##' | sort           # ¿hay ramas más avanzadas que main?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 122**: última edición `argos-2026-09-17` (ARGOS 121), **110 archivos**
en `reports/`, y la serie conteniéndola. **Si lo que encuentra está por detrás, algo se rompió: pare y
avísele al destinatario antes de escribir una línea.**

> ⚠️⚠️ **ESTO YA FALLÓ QUINCE EDICIONES SEGUIDAS Y VOLVERÁ A FALLAR.** La rama que asigna el entorno
> **llega desactualizada**. En ARGOS 121 llegó **sin las ediciones 107 a 120**.
>
> **`git merge --ff-only` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
>
> ⚠️ **Y si hereda un borrador, REHAGA TODOS SUS DESLINDES después de restituir la base.** ARGOS 121 no
> heredó ninguno y por eso sus deslindes nacieron verificados; **ARGOS 120 sí, y traía tres afirmaciones
> de ausencia imposibles de sostener, una de ellas falsa de plano**.

**Rama de trabajo actual**: la que contiene ARGOS 121. **Comprobar si `main` ya la absorbió**; si no,
trabajar sobre la rama más avanzada, no sobre `main`.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 122** (se confirma con el Bloque 0) |
| **Ventana** | **abre 2026-09-17 17:36 CDMX**, cierra a la **hora real de arranque**, verificada con `TZ=America/Mexico_City date` |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `-movil.html` · `.txt` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-123.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. **Ni un minuto de hueco ni de
solape. Verifique la hora, no la suponga.**

⚠️ **SELLAR LA HORA CAMBIA LA DURACIÓN Y LA DENSIDAD.** **Los dos cocientes se recalculan AL SELLAR, no
antes**, y aparecen en portada, en la Valoración y en el bloque de armamento.

**Serie de duraciones**: 46 h 30 min → 26 h 22 min → **117 h 50 min** (119) → **75 h 06 min** (120) →
**30 h 02 min** (121). **Ningún total absoluto es comparable sin normalizar por duración; la densidad
sí.** Densidades recientes: **0,19 → 0,16 → 0,25 → 0,13**.

⚠️ **REGLA NUEVA DE ARGOS 121, SIMÉTRICA DE LA QUE DEJÓ LA 119: una ventana CORTA no produce hechos
propios, produce RECUPERACIONES.** 30 horas dieron **4 hechos y 4 `-REC-`**. **Ni la duración larga ni la
corta son indicador de cobertura.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — **íntegro** (980 líneas). ⚠️ **Incluye la sección «Límite de extensión — el cartelón es
   telegráfico», que rige por encima de cualquier otra consideración de redacción.**
2. `reports/_pendientes.md` — el traspaso. **Los seguimientos abiertos ya dicen qué buscar.**
3. `reports/argos-2026-09-17-fuentes.md` — la edición anterior, con sus limitaciones y su deuda.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR, Y ES DEL COORDINADOR.** En ARGOS 121 **detuvo una duplicación
   completa**: un barrido trajo **Nonoava, Chihuahua** —8 armas, 2,294 cartuchos, 30 cargadores y **el
   mismo detenido nominal**— como hecho nuevo del 16-sep, **siendo `ARG-120-002` del 14-sep**.
   **El barrido no puede verlo: no tiene el índice a la vista.**

   ⚠️⚠️ **`indice-arg-id.md` EMPIEZA EN `ARG-91-001`. LAS EDICIONES 88, 89 Y 90 NO ESTÁN INDEXADAS.**
   La fórmula correcta es **«no figura en el índice, que cubre de ARGOS 91 en adelante»**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 122 HEREDA

### 3.1 Lo primero del corte

⚠️⚠️ **CHIHUAHUA · Ciudad Juárez (Distrito Judicial Bravos) — JOSÉ MANUEL E. C.**
**ES EL CANDIDATO MÁS MADURO DEL ARCHIVO: el «fallo condenatorio» YA ESTÁ DICTADO y solo falta la pena.**
La audiencia de individualización estaba fijada, con cadena literal del boletín del 14-sep, para
**«el próximo jueves 17 de septiembre a las 09:00 horas»**. **ARGOS 121 gastó tres búsquedas y no
localizó su resultado indexado**, pese a **8 h 36 min** transcurridas hasta su cierre.
⚠️ **NO se afirma que se pospusiera: eso sería un hecho no acreditado.** **Búsquelo primero: si se
publicó, es sentencia integrable.**

### 3.2 Alertas de identidad y de año — dos candidatos que pueden ser falsos

- ⚠️ **ZACATECAS · Villa González Ortega** — seis personas, secuestro agravado, 100 años. El boletín
  tiene *slug* sin fecha y **el caso que describe coincide con uno que otras fuentes fechan en 2023**.
  ⚠️ **SEGUNDA EDICIÓN SIN RESPALDO CITABLE: si ARGOS 122 no lo resuelve, PROCEDE FE DE ERRATAS Y RETIRO.**
- ⚠️ **BAJA CALIFORNIA · Tijuana — Luis Martín «N»** — el **boletín oficial dice 23 años**, los medios
  **26 años 8 meses**, y el boletín **no publica nombre**. **Solo coinciden municipio y delito: dos campos
  insuficientes.** `POSIBLE CASO HOMÓNIMO`.

### 3.3 Contradicciones vivas, sin arbitrar

- **GUERRERO · Coyuca de Benítez** — detenidos: **7 (cifra de la FGE, adoptada)**, **8** o **10**.
- **GUANAJUATO · San Francisco del Rincón** — heridos: **5 o 6**, con medios de peso a ambos lados.
  **No existe parte médico indexado.**
- **TABASCO · las seis ejecuciones del 15-sep** — municipios contradichos, sin boletín de la FGET.
- **NAYARIT · Mezcales** — cartuchos: **26** frente a **~44**. **Segunda edición en conflicto.**
- **NAYARIT · Acaponeta** — **10 rifles / 24 cargadores / 530 cartuchos** frente a **«6 armas y 2 mil
  balas»**. `NO INTEGRAR HASTA VALIDACIÓN`.
- **SINALOA · «La Noria de San Antonio»** — **84 AEI**, fecha ya consolidada en **8-sep**;
  **la contradicción es de MUNICIPIO**: San Ignacio frente a Mazatlán.

### 3.4 Casos abiertos

- **GUERRERO · Coyuca** — situación jurídica y carpeta de los 7 policías; **si la corporación queda
  intervenida**; **cotejo balístico** contra su armamento de cargo.
- **OAXACA · San Andrés Chicahuaxtla** — **evolución de la menor de 3 años**, que seguía grave;
  **amenaza previa** al profesor; **cero detenidos**.
- **GUERRERO · Eduardo Neri — Vidal «N», 66 años**: **sigue no localizado**. **Ninguna autoridad ha
  planteado la privación conjunta y ARGOS tampoco la plantea.**
- **GUERRERO · Xaltianguis — Said Sánchez Sandoval**: **sin resultado de audiencia publicado**.
  ⚠️ **La cifra de «24 detenidos acumulados» sigue sin adoptarse: fuente única regional.**
- **MICHOACÁN · Angamacutiro** — **desglose por inmueble de los 28 cateos**, que probablemente contiene
  **más volumen que todo el corte 121**; **los 18 detenidos atribuidos, declarados y NO adoptados**.

### 3.5 Renglones que NO se recuentan

⚠️ **El boletín federal del 14-16-sep apareció en ARGOS 121 y sus renglones son de la ventana de ARGOS
120.** Los publicados llevan ficha `-REC-` (Mazatlán, Coyame del Sotol); **los NO publicados están
listados uno por uno en `_pendientes.md`**: Comondú · Acaponeta · Del Nayar · La Yesca · Benito Juárez ·
Sayula de Alemán · Huimanguillo · Mexicali. **Si reaparecen republicados, no son nuevos.**

---

## BLOQUE 4 — LO QUE HAY QUE VOLVER A COMPROBAR EN CADA CORTE

| Qué | Estado al cierre de ARGOS 121 |
|---|---|
| ⚠️ **El bloqueo de egreso alcanza también a los MEDIOS** | **REVERIFICADO Y PERSISTE, segunda edición.** Seis dominios probados, **todos bloqueados**: `gob.mx/sspc`, `fiscaliachihuahua.gob.mx`, Infobae, El Financiero, Milenio y un republicador. **Techo ★★★☆☆.** ⚠️ **COMPRUÉBELO DE NUEVO: si la lectura funciona, el techo recupera ★★★★☆ y debe hacerse constar** |
| `docs/solicitud-lista-blanca-egreso.md` | **Sigue sin tramitar. Es la única solución real** |
| `gabinetedeseguridad.gob.mx/resultados/` | **Undécima verificación consecutiva sin cifra utilizable.** Ninguna cifra suya se usa |
| **Boletín federal de acciones relevantes** | ⚠️ **El formato NO es estable: la triple consulta es obligatoria.** El del **14-16-sep apareció el 17**, después de que ARGOS 120 lo verificara inexistente en las tres formas. **El siguiente debe cubrir el 17 en adelante** |
| `fiscaliaguerrero.gob.mx` | **Cuarta edición sin publicar indexable.** ⚠️ **Diagnóstico precisado: el portal SÍ está indexado; lo que no lo están son sus boletines recientes.** **La vía que funciona es el republicador, no el dominio** |
| ⚠️ `fgjem.edomex.gob.mx` | **EL VACÍO JUDICIAL MÁS COSTOSO DEL ARCHIVO: tres resoluciones sin boletín** —Temoaya 125 años, Coacalco 36a 3m, Hueypoxtla 21a 10m 15d—. **Ninguna edición ha integrado una sola** |
| **SSC y FGJ de la Ciudad de México** | **Cero boletín sobre Tepito, segunda edición.** ⚠️ **Edades contradichas (25-30 vs 18-19)** y **una cifra de «4 detenidos» con nombres DESCARTADA por no corroborarse** |
| `fgeqroo.gob.mx` | **Sin comunicado del 16 ni del 17-sep**, tras haber sido la mejor fuente del corte anterior |

---

## BLOQUE 5 — BARRIDO REGIONAL Y ROTACIÓN

`CLAUDE.md` exige **seis agentes `barrido-regional` en paralelo**. **Lánzelos en un solo mensaje**, con
la deuda del Bloque 3 al frente y **tope duro de 2-3 búsquedas por eje**.

⚠️ **CICLO QUE TOCA: CICLO C — Occidente + Sureste encabezan el triaje judicial.**
⚠️ **PERO LA PRIORIDAD VENCE AL CICLO: YUCATÁN quedó `NO REVISADA` en los dos módulos y debe encabezar
aunque le toque por ciclo (es del Sureste, de modo que coinciden).** **SSP y FGE de CHIAPAS** se
cubrieron solo por mención general, **sin consulta dirigida a su dominio**: también encabezan.

⚠️ **El Ciclo B de ARGOS 121 fue el primero que NO produjo una sola sentencia.** Lo que sí produjo:
la **alerta de año** del candidato de Zacatecas y la **incoherencia de correlativo** del folio 37481 de
la FGET. **Declárelo igual: el rendimiento del ciclo se mide, no se supone.**

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta **sin
  restricción de dominio** antes de cerrarla.
- ⚠️⚠️ **RECALL NACIONAL DEL COORDINADOR, ANTES DE CERRAR LOS BARRIDOS. DUODÉCIMA EDICIÓN CONSECUTIVA
  EN QUE APORTA LOS HECHOS DE MAYOR GRAVEDAD QUE NINGÚN BARRIDO VE.** En ARGOS 121 trajo **los dos
  hechos rojos del periodo**. **Ya no es una observación: es una propiedad del método, y no es
  sustituible por más equipos.**
- ⚠️ **Arbitraje del coordinador sobre las clasificaciones, en las DOS direcciones.** **El criterio es el
  tipo de evento y quién inició, nunca la prudencia ni el número de muertos.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️⚠️ **UN BARRIDO PUEDE TRAER UN HECHO YA PUBLICADO COMO NUEVO — trampa confirmada en ARGOS 121** | **Nonoava**: mismo municipio, mismas 8 armas, mismos 2,294 cartuchos, mismos 30 cargadores y **el mismo detenido nominal**, con la fecha corrida dos días. **Solo el `grep` del coordinador lo detuvo.** **El barrido no tiene el índice a la vista** |
| ⚠️ **UN OPERATIVO CON NOMBRE PROPIO QUE SE REPITE ES EL SUPUESTO EXACTO DE RECUENTO** | **«Sinergia por Querétaro»** aparece en `ARG-109-005` (27-ago) y en `ARG-121-003` (17-sep), **con los mismos municipios**. **Son eventos distintos, pero el deslinde es obligatorio y permanente** |
| ⚠️ **LA HORA, CUANDO SE PUBLICA, DECIDE LA VENTANA SIN RESERVA** | **Chicahuaxtla trae «01:30»** y eso permitió **asignarlo sin reserva a la ventana anterior** en vez de marcarlo `FRONTERA DE VENTANA`. **Búsquela siempre: casi nunca está, y cuando está lo resuelve todo** |
| ⚠️ **UN BOLETÍN DE RANGO NO SE REPARTE POR DÍAS NI POR HORAS** | El federal del 14-16-sep **solo permitió fechar el renglón que una cobertura independiente fechó** (Mazatlán, martes 15). **El resto quedó `FECHA NO FIJADA DENTRO DEL RANGO`** |
| ⚠️ **UN BOLETÍN QUE LLEGA TARDE CORRIGE AL ALZA UNA EDICIÓN CERRADA, Y ESO NO ES UN FALLO DE AQUELLA** | `ARG-121-FE-001` y `-FE-002` **corrigen Tapachula y Ensenada al alza** con datos que **no existían publicados cuando ARGOS 120 cerró**. **ARGOS 120 hizo lo correcto al no inferir** |
| ⚠️ **UNA CIFRA CONTRADICHA SE ARBITRA POR PROCEDENCIA, NO POR MAYORÍA** | En Coyuca se adoptó **7** por ser **la atribuida expresamente a la FGE**, no por ser la más repetida. **Mismo criterio que las 66 armas de El Rosario** |
| ⚠️ **DOS EVENTOS EN EL MISMO MUNICIPIO NO SON EL MISMO EVENTO** | Los **«9 detenidos»** de El Rosario eran de **Agua Verde, ~3-sep**, no del arsenal de los cinco tambos. **El municipio compartido no identifica un caso** |
| ⚠️ **EL RESUMIDOR FABRICA FECHAS Y FOLIOS** | **Veintitrés en seis cortes**, más el folio **37481** de la FGET fechado por el resumidor en «abril de 2026» siendo **superior al 37454 ya anclado en agosto**. **Cadena exacta entre comillas; el negativo VENCE** |
| **Correlativo sin fecha** | En un portal de identificador correlativo, **un boletín ya fechado acota a todos los de numeración inferior** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado catorce ediciones |
| ***Liveblog*** | **Nunca fecha un hecho ni basta como fuente única.** ⚠️ **En ARGOS 121 estuvo a punto de introducir «4 detenidos» con nombres en el caso de Tepito: descartado en segunda consulta** |
| **«Más de» no es cifra** | **Pero si el cuerpo del boletín la fija, se integra** |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| ⚠️ **Corroboración asimétrica** | **El nivel lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo |
| **Un delito y su detención son dos eventos** | **ARGOS 121 lo aplicó**: Coyuca en verde (`ARG-121-001`) y el homicidio en rojo (`ARG-121-REC-001`), **sin sumarse** |
| **Cifras derivadas** | Todo total es **cálculo propio** y se declara. ⚠️ **Compruebe la aritmética de TODO cociente y recalcule tras cada corrección** |
| ⚠️ **LO QUE NO SE DERIVA, DIVERGE** | **La móvil y el texto se GENERAN del cartelón, nunca se escriben aparte.** ⚠️ **Y si el generador miente, se corrige EL GENERADOR**: en ARGOS 121 fijaba «Corte matutino» sobre un corte vespertino |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️⚠️ **DOS APARTADOS POR FICHA: «HECHO» Y «TRAZABILIDAD». NADA MÁS.** Instrucción editorial directa
  del destinatario, dada tras revisar ARGOS 121: *«quita la corroboración y explotación ARGOS; es un
  reporte para mandos; hay que reducir los textos y no repetir las noticias en los diferentes
  secciones»*. **`CLAUDE.md` la recoge en «Regla de las dos secciones por nota», que DEROGA la de las
  cuatro.** ⚠️ **Las fuentes, los deslindes y las marcas de reserva NO se suprimen: son dato, no prosa,
  y van comprimidos en Trazabilidad** —recuento por tipo, nombrados solo los que llevan fecha en la
  ruta, lista íntegra al archivo de fuentes—.
- ⚠️ **EL ANÁLISIS VIVE UNA SOLA VEZ, AL CIERRE**: Valoración (5 líneas) y Conclusiones de inteligencia
  criminal (5 líneas). **No ficha por ficha.**
- ⚠️ **CADA HECHO EN DOS LUGARES COMO MÁXIMO**: un renglón en la tabla **«PANORAMA DEL CORTE»**
  (página 2, **único listado resumido**) y su **ficha**. **Prohibida una tercera aparición.**
  ⚠️ **El recuadro de portada NO repite titulares**: se titula **«LO QUE DEBE HACER EL MANDO»** y lleva
  **cinco líneas de ACCIÓN** —qué auditar, cotejar, vigilar o exigir—. **Los totales tampoco se
  repiten**: van en la página de panorama y los módulos remiten a ella.
- ⚠️ **CINCO LÍNEAS.** Máximo cinco en cada recuadro `alerta contexto` y en la **Valoración**,
  numeradas `<b>N. ` **con espacio**.
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes,
  deslindes ni marcas de reserva. Se recorta la prosa, no el dato.**
- ⚠️ **TRES RECUADROS COMO MÁXIMO EN TODO EL CARTELÓN** —portada, Valoración y Conclusiones—, **y ninguno
  repite el hecho de otro**. ⚠️ **NINGÚN RECUADRO EXPLICA UN COLOR NI UN MECANISMO DEL MÉTODO.**
- **La portada lleva UN SOLO recuadro**, «LO QUE DEBE SABER EL MANDO». **Sin «Ejes del día» y sin
  resumen ejecutivo.**
- **Sin ARGOS hablando de ARGOS.** **Conclusiones de inteligencia criminal, no de método.**
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`; el ARG-ID
  `-FE-` se sigue registrando en el índice.
- **Ningún hecho con ficha propia entra además en una tabla resumen.**
- **Toda cifra en cero lleva al lado el dato que la explica.** **Las categorías en cero se muestran
  atenuadas: la ausencia es dato.**
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>` —`exec wide`
  si tiene muchas columnas—. **Nada de `sem-item` fuera de la portada.**
- ⚠️ **Cada sentencia integrada lleva ficha propia** —y también la declarada y no integrada.
- ⚠️ **Toda ficha `-REC-` lleva su ventana de origen declarada y queda FUERA del semáforo, del mapa, del
  radar y de todos los totales.** **En el cartelón se muestran atenuadas.**

### Estructura de páginas que hereda ARGOS 122

**ARGOS 121 salió en NUEVE páginas** con 3 hechos, 5 recuperaciones y 1 sentencia: portada ·
**panorama del corte** · crimen organizado (I) a (III) · armamento · sentencias · candidatos y
cobertura · valoración y conclusiones. **ARGOS 120 salió en trece con 19 hechos.**
⚠️ **La reestructuración a dos apartados recortó un 33 % del texto del cuerpo** sin perder una sola
cifra, fecha, fuente ni deslinde. **El número de páginas lo fija el volumen, no la costumbre:
si un bloque crece se reparte entre más páginas, nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de argos-2026-09-17.html, sustituir el <title>, CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️⚠️ NO los sustituya con un sed GLOBAL sobre el HTML ensamblado: alcanza el bloque de datos
#    y el renderizador. Sustituya POR LÍNEA.
#    Tramos de la plantilla de ARGOS 121 (reports/argos-2026-09-17.html):
#      (a) cabecera: líneas 1-431   (el <title> está en la línea 5)
#      (b) <script> + MEXICO_VIEWBOX + MEXICO_PATHS: hasta antes de const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 122 <FECHA> 121 2026-09-17 <HORA>

# 3. Texto: NO se escribe, se genera. Ya deriva el turno del corte del pie del cartelón.
python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt

# 4. La validación debe decir "validación OK" y los contadores deben coincidir con
#    el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
#    ⚠️ REGENERE MÓVIL Y TEXTO DESPUÉS DE CADA CORRECCIÓN DEL ESCRITORIO.
```

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes, Nayarit y
Guanajuato son «Occidente»**; **Zacatecas es «Noreste»**; **Guerrero es «Sureste»**; **Durango es
«Noroeste»**; **Querétaro e Hidalgo son «Centro»**. Un `region:` mal puesto **coloca el eco del radar en
el sector equivocado y nadie lo nota**.

⚠️ **CADA ARG-ID DE `EVENTOS` Y DE `EVENTOS_ARM` DEBE TENER UN ANCLA `id=` EN EL DOCUMENTO**, y también
los `-REC-` y `-SEN-` citados.

**Comprobación de coherencia obligatoria**, ejecutable con `node:vm` sobre el `<script>` del cartelón.
⚠️ **Las `const` NO se exponen como propiedades del contexto**: hay que devolverlas con una expresión
final, `vm.runInContext(code + '\n;({EVENTOS,EVENTOS_ARM,MEXICO_PATHS,STATE_REGION,CORTE_FECHA})', ctx)`.
**ARGOS 121 dejó el validador escrito y funcionando**; comprueba que **`MEXICO_PATHS` tiene 32
entidades**, que **cada `estado:` existe**, que **cada `region:` coincide con `STATE_REGION`**, que
**ninguna fecha cae fuera de la ventana**, que **no hay ARG-ID duplicados**, que **cada ARG-ID resuelve a
un ancla**, que **el semáforo derivado coincide con la portada y con `radar-stats`**, que **hay
exactamente un `<body>`**, que **toda tabla está envuelta exactamente una vez**, que **hay cero `-FE-`**,
que **`sem-item` solo aparece en portada**, que **ningún bloque supera las cinco líneas**, que **hay como
máximo 3 recuadros**, que **el pie aparece en todas las páginas** y —⚠️ **comprobación nueva de
ARGOS 121**— que **NO existe ningún apartado «Corroboración» ni «Explotación ARGOS»** y que **cada ficha
tiene exactamente dos apartados, uno de ellos «TRAZABILIDAD»**.

⚠️ **RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS**, y **vuelva a recalcularlo DESPUÉS de las
correcciones de los controles**.

*Notas del generador móvil, que NO son defectos*: **no lleva `<script>`** · **`table-wrap` aparece en
cero** —se renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**. **Verifíquelo contando ARG-ID, no etiquetas `<table>`.**

---

## BLOQUE 9 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo, que las casillas no cuadren con las 32 y **que un deslinde afirme algo que el índice no puede sostener** |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **que se descarte por precaución una que sí debía integrarse** y **que se dé por «no publicado» un dato que la fuente primaria citada SÍ publica** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **ARGOS 120 no ejecutó los dos primeros y lo declaró como deuda. ARGOS 121 SÍ los ejecutó, como
subagentes.** **No rompa la racha.**

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos y
sobre sus propias instrucciones. ⚠️ **Revise toda exclusión que un barrido atribuya a una instrucción
suya: las prohibiciones de gasto se redactan contra el PENDIENTE, no contra el TOPÓNIMO.**

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS**, y **toda disposición es
   expresa** —cerrado, sin avance o fuera de ventana—.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-` y los `-REC-`**—.
3. Escribir `reports/argos-<FECHA>-fuentes.md` con el registro del barrido, el ciclo aplicado, el costo
   de cobertura y las limitaciones de herramienta.
4. **Escribir `reports/_arranque-ARGOS-123.md`** y borrar este archivo.
5. **Mergear a `main`** y verificar que quedó.
