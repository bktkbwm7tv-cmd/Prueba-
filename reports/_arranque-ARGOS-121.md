# ORDEN DE ARRANQUE — ARGOS 121

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino
en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 120** (corte 2026-09-16).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en TODO el cartelón
git fetch origin                                   # traer el estado real
git log --oneline -1 origin/main
git branch -r | sed 's#origin/##' | sort           # ¿hay ramas más avanzadas que main?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 121**: última edición `argos-2026-09-16` (ARGOS 120), **106 archivos**
en `reports/`, y la serie conteniéndola. **Si lo que encuentra está por detrás, algo se rompió: pare y
avísele al destinatario antes de escribir una línea.**

> ⚠️⚠️ **ESTO YA FALLÓ CATORCE EDICIONES SEGUIDAS Y VOLVERÁ A FALLAR.** La rama que asigna el entorno
> **llega desactualizada**. En ARGOS 120 llegó en `a1cb1d5`: **trece ediciones por detrás**, con
> **62 archivos** y `argos-2026-08-24` (ARGOS 106) como última edición.
>
> ⚠️ **Y ARGOS 120 descubrió una VARIANTE NUEVA, más cara que la de siempre: EL BORRADOR TAMBIÉN PUEDE
> VENIR DE UNA BASE EQUIVOCADA.** El borrador de ARGOS 120 se había redactado en una rama hermana que
> **nunca vio las ediciones 107 a 118**, y traía **tres afirmaciones de ausencia imposibles de
> sostener**. Al restituir la base, el `grep` por topónimo devolvió **cuatro cruces reales** —Xaltianguis,
> Huimanguillo, Maneadero y Tecámac—, uno de ellos **falso de plano**.
>
> **REGLA QUE QUEDA: un deslinde escrito sin el archivo completo a la vista NO es un deslinde
> verificado. Si hereda un borrador, REHAGA TODOS SUS DESLINDES después de restituir la base.**
>
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**

**Rama de trabajo actual**: `claude/argos-2026-cartel-mobile-q87ahx`, que contiene ARGOS 120.
**Comprobar si `main` ya la absorbió**; si no, trabajar sobre la rama más avanzada, no sobre `main`.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 121** (se confirma con el Bloque 0) |
| **Ventana** | **abre 2026-09-16 11:34 CDMX**, cierra a la **hora real de arranque**, verificada con `TZ=America/Mexico_City date` |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `reports/argos-<FECHA>-movil.html` · `reports/argos-<FECHA>.txt` · `reports/argos-<FECHA>-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-122.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. **Ni un minuto de hueco ni de
solape. Verifique la hora, no la suponga.**

⚠️ **SELLAR LA HORA CAMBIA LA DURACIÓN Y LA DENSIDAD.** En ARGOS 120 el borrador traía **73 h 36 min y
0,26 hechos/hora**; al sellar las 11:34 reales quedaron **75 h 06 min y 0,25**. **Los dos cocientes se
recalculan AL SELLAR, no antes**, y aparecen en portada, en la Valoración y en el bloque de explosivos.

**Serie de duraciones**: 47 h → 25 h → 46 h 30 min → 26 h 22 min → **117 h 50 min** (ARGOS 119) →
**75 h 06 min** (ARGOS 120). **Ningún total absoluto es comparable sin normalizar por duración; la
densidad sí.** Densidades recientes: **0,19 → 0,16 → 0,25**.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — **íntegro**. No es plantilla: son las reglas operativas. ⚠️ **Incluye la sección
   «Límite de extensión — el cartelón es telegráfico», que rige por encima de cualquier otra
   consideración de redacción.**
2. `reports/_pendientes.md` — el traspaso. **Los seguimientos abiertos ya dicen qué buscar.**
3. `reports/argos-2026-09-16-fuentes.md` — la edición anterior, **con sus limitaciones declaradas y su
   deuda de método sin atenuar**.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR.** En ARGOS 120 produjo **cuatro cruces**, y el de **Huimanguillo /
   FIRT Olmeca** era **riesgo real de recuento**: el índice ya tenía esa fuerza y ese municipio en
   `ARG-114-FE-006`, una fe de erratas que había cerrado por obsoleto un agregado de junio.

   ⚠️⚠️ **`indice-arg-id.md` EMPIEZA EN `ARG-91-001`. LAS EDICIONES 88, 89 Y 90 NO ESTÁN INDEXADAS.**
   **Ninguna ficha puede afirmar «no aparece en ningún corte anterior del archivo»**; la fórmula correcta
   es **«no aparece en el índice, que cubre de ARGOS 91 en adelante»**. **ARGOS 120 la aplicó en cinco
   fichas.** Si hay presupuesto, extienda el índice hacia atrás; si no, declare el rango en su cabecera.

---

## BLOQUE 3 — DEUDA QUE ARGOS 121 HEREDA

### 3.1 Perecedero, con fecha — lo primero del corte

⚠️ **CHIHUAHUA · Ciudad Juárez, Distrito Judicial Bravos — José Manuel E. C.**, homicidio calificado y
tentativa, hecho del 1-sep-2025, **juicio oral con «fallo condenatorio» ya dictado**. **LA
INDIVIDUALIZACIÓN DE LA PENA SE FIJÓ PARA EL JUEVES 17-SEP.** Si la audiencia se celebró, **es una
sentencia integrable de esta ventana**. Búsquelo expresamente.

### 3.2 Contradicciones vivas, sin arbitrar

- **SINALOA · El Rosario** — detenidos del arsenal de los cinco tambos: `ARG-120-010` integró **0** por
  cifra mayoritaria; **una cobertura aislada consigna 9**.
- **SINALOA · «La Noria de San Antonio»** — **84 AEI** con el **mismo desglose exacto** en dos
  publicaciones: **7-sep en San Ignacio** y **rango 11-13-sep en Mazatlán**.
  `POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN`. ⚠️ **Habría sido el mayor volumen de AEI
  del archivo.**
- **TABASCO · las seis ejecuciones del 15-sep** — municipios contradichos: Centro/Cárdenas/Macuspana/
  Nacajuca frente a Villahermosa/Comalcalco.
- **GUANAJUATO · San Francisco del Rincón** — heridos: **5, 6 o 7**. Lo cierra el parte médico.

### 3.3 Personas y casos abiertos

- **GUERRERO · Eduardo Neri — Vidal «N», 66 años**: **no localizado**; su hijo apareció asesinado
  (`ARG-120-008`). **Ninguna autoridad ha planteado la hipótesis de privación conjunta.**
- **GUERRERO · Xaltianguis — Said Sánchez Sandoval**, comisario municipal detenido: situación jurídica,
  carpeta, y **si su cargo sigue vigente**. ⚠️ **Verificar la cifra de «24 detenidos acumulados»,
  declarada y NO adoptada.**
- **ESTADO DE MÉXICO · Tecámac**: **objetivo real del ataque no resuelto** —alcaldesa o jefe de
  gabinete—, y **es el campo que decide la lectura**.

### 3.4 Candidatos judiciales vivos

**BAJA CALIFORNIA · Tijuana — Luis Martín «N»** (feminicidio, 26a 8m) · **ESTADO DE MÉXICO · Coacalco —
Israel Cruz Luna, «El Maca»** (36a 3m) · **TAMAULIPAS · Nuevo Laredo — Carlos, Adrián, Luis y José «N»**
(8a a 15a 6m, `FECHA NO FIJADA`). **Más los heredados de ediciones anteriores que `_pendientes.md`
conserva con su disposición.**

### 3.5 Renglones que NO se recuentan

⚠️ **El boletín federal del 11-13-sep dejó NUEVE bloques `FECHA NO FIJADA DENTRO DEL RANGO`**, listados
uno por uno en `_pendientes.md` con sus cifras. **Si vuelven a aparecer republicados, no son nuevos.**

---

## BLOQUE 4 — LO QUE HAY QUE VOLVER A COMPROBAR EN CADA CORTE

| Qué | Estado al cierre de ARGOS 120 |
|---|---|
| ⚠️ **El bloqueo de egreso alcanzó también a los MEDIOS, no solo a `*.gob.mx`** | **Incidencia NUEVA de ARGOS 120.** La lectura directa devolvió bloqueo **en todos los dominios probados**. **Ninguna página se leyó íntegra** y el techo bajó a **★★★☆☆**. ⚠️ **COMPRUÉBELO DE NUEVO: si la lectura de medios funciona, el techo recupera ★★★★☆ y debe hacerse constar** |
| `gabinetedeseguridad.gob.mx/resultados/` | **Décima verificación consecutiva sin cifra utilizable.** Dominio indexado, rutas sin fecha, acceso directo 403, trampa de año acreditada. **Ninguna cifra suya se usa** |
| `docs/solicitud-lista-blanca-egreso.md` | **Sigue sin tramitar** |
| **Boletín federal de acciones relevantes** | ARGOS 120 verificó **en las tres formas** que **no existe indexado** ninguno que cubra el **14, 15 o 16 de septiembre**. **El que cierre esos días debe aparecer el 17-sep o después: búsquelo, es de esta ventana** |
| `fiscaliaguerrero.gob.mx` | **Sin publicar indexable, tercera edición consecutiva** |
| **SSC y FGJ de la Ciudad de México** | **Cero boletín** sobre el doble homicidio de Tepito del 16-sep |

---

## BLOQUE 5 — BARRIDO REGIONAL Y ROTACIÓN

`CLAUDE.md` exige **seis agentes `barrido-regional` en paralelo**. **Lánzelos en un solo mensaje**, con
la deuda del Bloque 3 al frente y **tope duro de 2-3 búsquedas por eje**.

⚠️ **CICLO QUE TOCA: CICLO B — Noreste + Golfo encabezan el triaje judicial.**
**Y la prioridad de cobertura COINCIDE con el ciclo**, de modo que no hay conflicto que arbitrar: las
cuatro entidades que ARGOS 120 dejó `NO REVISADA` en el módulo judicial —**COAHUILA, NUEVO LEÓN, SAN
LUIS POTOSÍ y ZACATECAS**— **son todas del Noreste**. **Deben encabezar.**

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta **sin
  restricción de dominio** antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** **Undécima edición consecutiva**
  en que aporta los hechos de mayor gravedad que ningún barrido ve.
- ⚠️ **Arbitraje del coordinador sobre las clasificaciones que propongan, en las DOS direcciones.**
  **El criterio no es la prudencia: es el tipo de evento y quién inició.**

⚠️ **Revise toda exclusión que un barrido atribuya a una instrucción suya.** **Las prohibiciones de gasto
se redactan contra el PENDIENTE, no contra el TOPÓNIMO.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️⚠️ **UN DESLINDE ESCRITO SIN EL ARCHIVO COMPLETO NO ES UN DESLINDE — trampa NUEVA de ARGOS 120 y la más cara** | El borrador afirmaba tres veces «no aparece en ningún corte anterior» **sin poder comprobarlo**, y **una era falsa de plano** (Tecámac figura en ARGOS 93 por huachicol). **Restituya la base ANTES de escribir deslindes, o rehágalos todos después** |
| ⚠️ **LO QUE NO SE DERIVA, DIVERGE — trampa NUEVA** | El `.txt` de ARGOS 120 seguía siendo el borrador: **otra hora, otra ventana, otra densidad y sin los deslindes**. **Resuelto con `tools/gen-texto.py`.** **La móvil y el texto se GENERAN del cartelón, nunca se escriben aparte** |
| ⚠️ **UNA SUSTITUCIÓN GLOBAL SOBRE EL HTML ENSAMBLADO ALCANZA EL BLOQUE DE DATOS Y EL RENDERIZADOR** | En ARGOS 119, el `sed` del `<title>` **rompió la cadena JavaScript del radar** y `s/ARGOS 118/ARGOS 119/g` **convirtió cuatro referencias legítimas**. **Sustituya por línea, y revise después toda referencia a la edición anterior** |
| ⚠️ **CITAR UN BOLETÍN NO EQUIVALE A HABERLO EXPLOTADO** | En ARGOS 119, **dos fichas dieron por «no publicado» un desglose que su propia fuente primaria publicaba**: **+4 armas y +10 cargadores** al total nacional |
| ⚠️ **UNA PENA CONTRA VARIAS PERSONAS NO SE MULTIPLICA SI EL BOLETÍN NO DICE «A CADA UNO»** | **ARGOS 120 integró 156 años de Tamaulipas PORQUE el boletín dice «a cada una»**, frente al comunicado 612/26 de ARGOS 119, que no lo decía y quedó `PENA COMPUESTA` |
| ⚠️ **UN HECHO PUEDE REPUBLICARSE INDEFINIDAMENTE** | «El Maguey» va por **tres publicaciones, tres emisores, tres cortes**, y **las tres veces lo cerró la COLONIA**. **El `grep` por topónimo es permanente** |
| ⚠️ **UNA VENTANA LARGA NO PRODUCE RECUPERACIONES: LAS ABSORBE** | **ARGOS 119 y 120 tuvieron CERO `-REC-`.** **La cifra de recuperaciones es función de la duración y no es indicador de cobertura** |
| ⚠️ **EL AGREGADO NO SE INTEGRA: SOLO LOS SUB-EVENTOS CON ASEGURAMIENTO** | En ARGOS 120, Huimanguillo publicó **14 detenidos** y **solo se integraron los 6** de los tres sub-eventos individualizados |
| ⚠️ **UN BOLETÍN DE RANGO NO SE REPARTE POR DÍAS** | El federal del 11-13-sep **no desglosa qué renglón es de qué día**: solo se integró el que **una cobertura independiente fechó** |
| ⚠️ **EL RESUMIDOR FABRICA FECHAS Y FOLIOS `DPE/…`** | **Veintitrés en seis cortes.** **Cadena exacta entre comillas; el negativo VENCE** |
| ⚠️ **CORRELATIVO SIN FECHA** | En un portal de identificador correlativo, **un boletín ya fechado acota a todos los de numeración inferior**. Así se descartó el candidato de Tabasco en ARGOS 120 |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado trece ediciones. ⚠️ **En ARGOS 120 detectó una incoherencia que NO se pudo resolver** —«22:30 del sábado» publicado un domingo— y se declaró en vez de corregirse |
| ***Liveblog*** | **Nunca fecha un hecho ni basta como fuente única.** Se identifica por `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES` |
| **«Más de» no es cifra** | **Pero la regla es sobre la CIFRA, no sobre el titular**: si el cuerpo del boletín la fija, se integra |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| ⚠️ **Corroboración asimétrica** | **El nivel de confianza lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo |
| **Un delito y su detención son dos eventos** | **ARGOS 120 lo aplicó**: General Treviño en rojo (`ARG-120-001`) y la captura de tres implicados en verde (`ARG-120-011`), **sin sumar los 3 a los 2** |
| **Cifras derivadas** | Todo total es **cálculo propio** y se declara. ⚠️ **Compruebe la aritmética de TODO cociente y recalcule tras cada corrección** |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  Máximo cinco líneas en cada **Explotación ARGOS**, en cada recuadro `alerta contexto` y en la
  **Valoración**, numeradas `<b>N. ` **con espacio**.
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes,
  deslindes ni marcas de reserva. Se recorta la prosa, no el dato.**
- ⚠️ **TRES RECUADROS COMO MÁXIMO EN TODO EL CARTELÓN** —portada, Valoración y Conclusiones—, **y ninguno
  repite el hecho de otro**. ⚠️ **NINGÚN RECUADRO EXPLICA UN COLOR NI UN MECANISMO DEL MÉTODO.**
- **La portada lleva UN SOLO recuadro**, «LO QUE DEBE SABER EL MANDO». **Sin «Ejes del día» y sin
  resumen ejecutivo**: la instrucción del destinatario, posterior y más específica, los retiró.
- **Sin ARGOS hablando de ARGOS.** **Conclusiones de inteligencia criminal, no de método.**
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`; el ARG-ID
  `-FE-` se sigue registrando en el índice.
- **Ningún hecho con ficha propia entra además en una tabla resumen.**
- **Toda cifra en cero lleva al lado el dato que la explica.** **Las categorías en cero se muestran
  atenuadas: la ausencia es dato.**
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>` —`exec wide`
  si tiene muchas columnas—. **Nada de `sem-item` fuera de la portada.**
- ⚠️ **Cada sentencia integrada lleva ficha propia.**

### Estructura de páginas que hereda ARGOS 121

**Trece páginas**, como salió ARGOS 120: portada · crimen organizado **(I) a (VIII)** · armamento ·
sentencias · tabla judicial y cobertura · valoración y conclusiones.
**Si el volumen lo pide, se reparte entre más páginas: nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de argos-2026-09-16.html, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️⚠️ NO los sustituya con un sed GLOBAL sobre el HTML ensamblado.
#    Tramos de la plantilla de ARGOS 120 (reports/argos-2026-09-16.html):
#      (a) cabecera: líneas 1-429
#      (b) <script> + MEXICO_VIEWBOX + MEXICO_PATHS: hasta antes de const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 121 <FECHA> 120 2026-09-16 <HORA>

# 3. Texto: NO se escribe, se genera.
python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt

# 4. La validación debe decir "validación OK" y los contadores deben coincidir con
#    el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
#    ⚠️ REGENERE MÓVIL Y TEXTO DESPUÉS DE CADA CORRECCIÓN DEL ESCRITORIO.
```

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes, Nayarit y
Guanajuato son «Occidente»**; **Zacatecas es «Noreste»**; **Guerrero es «Sureste»**; **Durango es
«Noroeste»**. Un `region:` mal puesto **coloca el eco del radar en el sector equivocado y nadie lo nota**.

⚠️ **CADA ARG-ID DE `EVENTOS` Y DE `EVENTOS_ARM` DEBE TENER UN ANCLA `id=` EN EL DOCUMENTO.**

**Comprobación de coherencia obligatoria**, ejecutable con `node:vm` sobre el `<script>` del cartelón:
que **`MEXICO_PATHS` tiene 32 entidades**, que **cada `estado:` existe**, que **cada `region:` coincide
con `STATE_REGION`**, que **ninguna fecha cae fuera de la ventana**, que **no hay ARG-ID duplicados**,
que **cada ARG-ID resuelve a un ancla**, que **el semáforo derivado coincide con la portada y con
`radar-stats`**, que **hay exactamente un `<body>`**, que **toda tabla está envuelta exactamente una
vez**, que **hay cero `-FE-`**, que **`sem-item` solo aparece en portada**, que **ningún bloque supera
las cinco líneas**, que **hay como máximo 3 recuadros** y que **el pie aparece en todas las páginas**.

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

⚠️⚠️ **ARGOS 120 NO EJECUTÓ `editor-duplicidad` NI `procedencia-cifras` COMO SUBAGENTES.** Hizo en su
lugar el `grep` contra el índice y el cuadre aritmético, **y lo declaró sin atenuar en su archivo de
fuentes**. **Consecuencia para ARGOS 121: si cita una cifra de ARGOS 120, márquela
`HEREDADO — NO REVERIFICADO`.** ⚠️ **Y no repita la omisión: los dos controles llevaban catorce
ediciones consecutivas con hallazgos reales.**

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos y
sobre sus propias instrucciones.

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS**, y **toda disposición es
   expresa** —cerrado, sin avance o fuera de ventana—.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**—.
3. Escribir `reports/argos-<FECHA>-fuentes.md` con el registro del barrido, el ciclo aplicado, el costo
   de cobertura y las limitaciones de herramienta.
4. **Escribir `reports/_arranque-ARGOS-122.md`** y borrar este archivo.
5. **Mergear a `main`** y verificar que quedó.
