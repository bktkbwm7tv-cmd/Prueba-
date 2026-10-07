# ORDEN DE ARRANQUE — ARGOS 125

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino
en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 124** (corte 2026-09-24) y ⚠️ **REVISADO EL 2026-10-07**, al comprobarse
que la ventana de ARGOS 125 no es de dos días sino de **TRECE** —`2026-09-24 06:41 → hora real de
arranque`—. **Las premisas de la versión anterior de este archivo eran falsas y se han reescrito:
ventana, presupuesto de búsqueda, ciclo de rotación y seguimientos.** **Una orden con premisas falsas
es peor que no tenerla.**

⚠️ **El mensaje de arranque listo para pegar en una sesión nueva está en
`reports/_ordenes-ARGOS-125.txt`.** Este archivo es el detalle; aquél es la orden.

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

**Estado que debe encontrar ARGOS 125**: última edición `argos-2026-09-24` (ARGOS 124) y
**123 archivos** en `reports/`. **Si lo que encuentra está por detrás, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️⚠️ **NOVEDAD REAL, NO LA REPITA POR INERCIA: ARGOS 123 y 124 SE MERGEARON A `main`** en
> fast-forward puro. **Por primera vez en la serie, `main` está en la cabeza y el `ff-only` debe salir
> limpio.** **COMPRUÉBELO IGUAL**: si `main` viniera por detrás, busque la rama más avanzada.
>
> ⚠️ **Las ediciones 123 y 124 se construyeron en `claude/argos-123-criminal-analysis-k70hzw`, cuyo
> nombre YA NO CORRESPONDE AL CONTENIDO.** No busque una rama que se llame como su edición.
>
> ⚠️ **Y si hereda un borrador, REHAGA TODOS SUS DESLINDES después de restituir la base.**

**La rama de ARGOS 124**: `claude/argos-122-criminal-analysis-n4stuu`. **Compruebe si `main` ya la
absorbió**; si no, trabaje sobre la rama más avanzada, no sobre `main`.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 125** (se confirma con el Bloque 0) |
| **Ventana** | **abre 2026-09-24 06:41 CDMX** —donde cerró ARGOS 124—, cierra a la **hora real de arranque**, verificada con `TZ=America/Mexico_City date`. ⚠️ **Al escribirse este archivo eran 312 h 19 min: 13,0 DÍAS** |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `-movil.html` · `.txt` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, reescrito como `_arranque-ARGOS-126.md`, y su orden `_ordenes-ARGOS-126.txt` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. **Ni un minuto de hueco ni de
solape. Verifique la hora, no la suponga.**

⚠️ **SELLAR LA HORA CAMBIA LA DURACIÓN Y LA DENSIDAD.** **Los dos cocientes se recalculan AL SELLAR**,
y aparecen en portada, en la Valoración y en el bloque de armamento.

**Serie de duraciones**: 117 h 50 (119) · 75 h 06 (120) · 30 h 02 (121) · 87 h 21 (122) ·
23 h 25 (123) · **46 h 19 (124)** → **~312 h (125)**.
**Densidades**: 0,25 (121) · 0,19 (122) · 0,04 (123) · **0,30 (124)**.
**Ningún total absoluto es comparable sin normalizar por duración; la densidad sí** — ⚠️ **y en
ARGOS 125 tampoco del todo, porque el presupuesto de búsqueda no escala con la ventana.**

⚠️ **REGLA SIMÉTRICA, CONFIRMADA TRES VECES**: una ventana **corta** produce **recuperaciones**
(30 h → 3 hechos y 5 `-REC-`; **23 h → 1 hecho y 11 `-REC-`**); una ventana **larga** produce **hechos
propios** (87 h → 17 y 2). **Ni la una ni la otra es indicador de cobertura.**

⚠️⚠️ **ARGOS 123 ES EL CASO EXTREMO DE VENTANA CORTA: UN SOLO HECHO PROPIO Y ONCE RECUPERACIONES.**
Un corte con cero verdes **no describe un país en calma: describe un día sin boletín.**

---

### 1-bis — VENTANA EXTRAORDINARIA DE TRECE DÍAS · SIN PRECEDENTE EN LA SERIE

**Trece días sin publicar.** La ventana de ARGOS 125 es **2,65 veces la más larga de la serie**
(117 h 50, ARGOS 119) y **6,7 veces la de ARGOS 124**. Tres consecuencias, y las tres se olvidan si
no se fijan antes de la primera búsqueda:

1. **EL NÚMERO ES 125, NO 137.** La numeración cuenta **ediciones, no días**. Trece días sin publicar
   son un hueco de **ventana**, no de numeración. **No existen las ediciones 125 a 136**: no hay que
   recuperarlas, ni renumerar, ni fingir que existieron. El archivo de fuentes lo dice **en una
   línea** y nada más: **es trazabilidad, no narrativa.**
2. ⚠️⚠️ **CASI NADA ES RECUPERACIÓN.** El `-REC-` es para hechos de la ventana de una **edición
   anterior**. Todo lo ocurrido **entre el 24-sep 06:41 y la hora de cierre es de ESTA ventana**: es
   **hecho propio con su fecha**, por antiguo que parezca. **Un hecho del 25 de septiembre no es una
   recuperación: entra en los totales del corte.** Solo es `-REC-` lo fechado **antes** del
   24-sep 06:41. Por la regla simétrica, **espere el mayor volumen de hechos propios del archivo.**
3. **ADVERTENCIA DE COMPARABILIDAD, OBLIGATORIA Y EN UNA LÍNEA**, en la Valoración y en el panorama:
   los totales absolutos de este corte **no son comparables** con los de ninguna edición anterior.
   **Una línea, no un recuadro**: el límite de tres recuadros no se toca.

**El presupuesto de búsqueda no escala a trece días.** Trece días × 32 entidades × dos módulos **no
es ejecutable**, y trece días de boletín federal **no se consultan día por día**. Orden de gasto:
(1) los tres encargos del Bloque 3.1; (2) **recall nacional en dos tramos** —24-30 sep y 1-7 oct—,
**por gravedad, no por cronología**; (3) los seis barridos, con la ventana completa y sus días;
(4) boletín federal **por rango y por título sin `site:`**, reservando el día suelto para los días
que el recall señale.

⚠️⚠️ **PRECIO DE ADMISIÓN PARA PUBLICAR UN CORTE DE TRECE DÍAS: EL `NO REVISADA` SE DECLARA POR DÍA
Y POR ENTIDAD** en el archivo de fuentes. **Un barrido de trece días declarado como completo sería la
afirmación más falsa de la serie.** Declarar el hueco es dato, y es lo que hace auditable el corte.

⚠️ **Ninguna ficha se comprime para caber.** Si el volumen crece, **crecen las páginas** —`CLAUDE.md`
es explícito—. ARGOS 124 cerró en 13 páginas; esta edición puede necesitar más y **eso no es un
defecto.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — **íntegro**. ⚠️ **Lea con especial cuidado «Regla de las dos secciones por nota»
   —que DEROGA la de las cuatro— y «Límite de extensión — el cartelón es telegráfico», que rige por
   encima de cualquier otra consideración de redacción.**
2. `reports/_pendientes.md` — el traspaso. **Los seguimientos abiertos ya dicen qué buscar.**
3. `reports/argos-2026-09-24-fuentes.md` — la edición anterior, con sus limitaciones y su deuda.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR, Y ES DEL COORDINADOR.**

   ⚠️⚠️ **`indice-arg-id.md` EMPIEZA EN `ARG-91-001`. LAS EDICIONES 88, 89 Y 90 NO ESTÁN INDEXADAS.**
   La fórmula correcta es **«no figura en el índice, que cubre de ARGOS 91 en adelante»**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 125 HEREDA

### 3.1 Lo primero del corte — TRES ENCARGOS. TRECE DÍAS LES HAN DADO TIEMPO DE MOVERSE.

⚠️⚠️ **1. GUANAJUATO · COMONFORT — SEGUIMIENTO NUEVO Y PRIORITARIO.**
El **23-sep** un grupo armado **emboscó con ponchallantas** a una patrulla de las **FSPE** en
**Delgado de Arriba** y **mató a TRES POLICÍAS ESTATALES** (dos hombres y una mujer). `ARG-124-001`.
**CERO DETENIDOS** entonces. ⚠️ Un titular nacional publicó **cuatro** policías muertos y **dos civiles
abatidos**; ARGOS adoptó **tres**, la cifra de la **Secretaría de Seguridad y Paz de Guanajuato**, y
**no integró a los civiles**. **Busque: ¿detenidos en trece días? ¿confirmó la autoridad a los dos
civiles? ¿inventario del armamento empleado?** ⚠️ **Si hay detención, es un HECHO NUEVO EN VERDE con su
propio ARG-ID**, no una corrección del rojo: **un delito y su detención son dos eventos.**

⚠️⚠️ **2. VERACRUZ · COATZACOALCOS — SEGUIMIENTO NUEVO Y PRIORITARIO, CON LÍNEA DE ARCHIVO.**
El **23-sep** ejecutaron con **diez impactos** a **GUILLERMO PAMUCE YEP**, «El Chino Yep», exregidor de
Jáltipan y **coordinador regional del partido PAZ**. `ARG-124-002`. **Cero detenidos, móvil no
establecido.**
⚠️⚠️ **ES EL SEGUNDO CUADRO DEL MISMO PARTIDO ASESINADO EN EL ARCHIVO.** El primero fue
`ARG-108-REC-001`, **Mazatepec, Morelos**, coordinador municipal del partido PAZ. Y **ARGOS 123
publicó Tetecala (PRI)**. **Tres dirigentes políticos municipales en el archivo reciente**, con el
proceso electoral federal 2026-2027 abriéndose. **SI APARECE UN CUARTO, ES PATRÓN Y HAY QUE DECIRLO.**
**El patrón se registra; la vinculación NO se afirma sin acreditación.** ⚠️ **Una ventana de trece días
es la primera que puede ver el patrón de verdad: búsquelo expresamente, no espere a que caiga.**

⚠️⚠️ **3. GUANAJUATO · CORREDOR LAJA-BAJÍO — TERCERA EDICIÓN COMO MAYOR VACÍO DEL ARCHIVO.**
`periodicocorreo.com.mx` (21-sep) atribuye a la FGE **«23 MUERTOS Y 11 HERIDOS entre el 18 y el
20-sep»** en Valle de Santiago, Salamanca, Irapuato, Celaya, Cortazar y León, y **«14 MUERTOS EN VALLE
DE SANTIAGO EN OCHO DÍAS»**. **ARGOS 124 gastó tres búsquedas: NO EXISTE BOLETÍN DE LA FGE.** Ocho
medios lo republicaron **atribuyéndolo a «registros de la Fiscalía», ninguno enlazando documento**.
`NO INTEGRADO NI CITADO`. **Si el boletín aparece, ciérrelo; si no aparece en esta tercera, DECIDA**:
o se cierra por **agotamiento declarado**, o se dice **por qué sigue abierto**. **No lo herede una
cuarta vez sin disposición.**

### 3.2 Candidatos judiciales vivos — trece días dan tiempo a que aparezca el boletín

- ⚠️⚠️ **CHIHUAHUA · Cd. Juárez — JOSÉ MANUEL E. C.: LA PENA YA APARECIÓ.** **37 AÑOS Y 6 MESES**,
  **Fiscalía de Distrito Zona Norte**, **tres campos individualizadores coincidentes: SIN HOMÓNIMO
  POSIBLE.** ⚠️ **NO INTEGRADA**: ninguna URL lleva **fecha en la ruta** y no hay boletín oficial.
  **Si fija la fecha o halla el boletín, SE INTEGRA.** **La pista que funcionó**: buscar
  **«individualización de sanciones» sin restricción de fecha** — el boletín de la pena usa **otro
  *slug*** que el del fallo.
- **QUINTANA ROO · Cancún** — **sentencia nueva no integrada: 80 AÑOS** a tres personas por
  **secuestro agravado**, publicada el **22-sep dentro de la ventana de ARGOS 124**, **sin boletín de
  la fiscalía**.
- ⚠️ **VERACRUZ · los agregados de la FGE** — **PATRÓN ESTRUCTURAL DEL EMISOR, no vacío de búsqueda:
  quinta edición.** Tres boletines solo en la ventana de ARGOS 124 —11 sentencias (22-sep), 21 y un
  fallo (23-sep), **75 en una semana** (23-sep, desglosado solo por región)—. **Ninguno identifica un
  caso.** ⚠️ **Existen boletines individuales con nombre y pena en el dominio de la FGE, pero sus rutas
  NO llevan fecha**: no pueden atarse a ninguna ventana. **Si logra fechar uno, es la primera sentencia
  integrable de Veracruz en cinco ediciones.**
- ⚠️ **ESTADO DE MÉXICO · `fgjem.edomex.gob.mx`** — **SÉPTIMA verificación sin boletín primario.**
  Temoaya (125 a), **Coacalco ya individualizado** —**Israel Cruz Luna «El Maca», líder de «Los
  Macas»**, 36 a 3 m— y Hueypoxtla (21 a 10 m 15 d). ⚠️ **Sigue `POSIBLE CASO HOMÓNIMO`: NADIE HA
  COTEJADO el post de junio-2026 casi idéntico. Hágalo: es una búsqueda, no un proyecto.**
- **MICHOACÁN · Morelia — FRANCISCO JAVIER T., 93 a 9 m.** **Homónimo DESCARTADO**: ocho
  republicadores coinciden en tres campos individualizadores. Sigue `PENDIENTE DE CONFIRMACIÓN
  OFICIAL`. ⚠️ **DOMINIO CORREGIDO: `comunicacion.fiscaliamichoacan.gob.mx`, NO
  `fge.michoacan.gob.mx`.**
- **SAN LUIS POTOSÍ · La Pila — NORMA «N»**: **la pena es 4 AÑOS 2 MESES, no 4 años** (corregida en
  ARGOS 124), + 84 UMA. Dos fuentes regionales, **ninguna institucional**. ⚠️ **NO reproduzca la
  conversión a pesos de la fuente: usa la UMA de 2025, no la vigente.**
- **TAMAULIPAS · Nuevo Laredo — Carlos, Adrián, Luis y José «N»**: sentencias dictadas
  (15 a 6 m ×2, 11 a 6 m y 8 años, FGR). **Falta el boletín y el día exacto.**
- **TAMAULIPAS · «El Cholo»**, `ARG-122-SEN-001`: **se mantiene integrada con Medio**. **El folio de
  la FGR sigue sin localizarse** pese a siete medios convergentes.

⚠️ **UMBRAL ASIMÉTRICO**: armamento integra con confianza **Bajo**; **sentencias NO**. Una sentencia
sin fuente oficial queda `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL`. **Una
sentencia inexistente atribuida a una persona con nombre no se corrige con una fe de erratas.**

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
- ⚠️ **CDMX · Tepito** — **SEXTA edición sin boletín** de SSC ni FGJ. **Las edades ya convergen**:
  **Abigail Herrera, 19, y Odette Rosas, 18**, por cuatro fuentes independientes; las versiones
  «25-30» y «15-20» **no tienen respaldo**.
- ⚠️ **CHIAPAS · penal de Ocosingo** — la FGE vinculó la **misma arma a otros dos hechos** (16-ago y
  6-sep). ⚠️ **DISCREPANCIA SIN ARBITRAR**: la deuda citaba «16-ago en **Vida Mejor**»; una fuente del
  21-sep cita «**Patria Nueva**». **¿Mismo barrio con otro nombre o dos hechos?** **Auditoría del penal
  sin resultado publicado.**
- **TABASCO · FGET** — ⚠️ **corrección de calendario de ARGOS 124: el «lunes violento» es el 14-sep,
  no el 15.** **La cifra sigue en disputa: 4 frente a 6.**
- ⚠️ **NUEVO LEÓN · Los Aldamas — RIESGO DE CONFLACIÓN DECLARADO**: **cuatro incidentes distintos en el
  mismo municipio en años diferentes.** **Ninguna cifra de los anteriores debe atribuirse al de
  septiembre.**
- ⚠️ **SONORA · Puerto Peñasco** — la cifra exacta sigue abierta: **«más de 40» y «casi cuatro mil» NO
  SON CIFRAS.** ⚠️⚠️ **NO REABRA las «cinco personas sin paradero»: `ARG-123-FE-001` las cerró. Son dos
  grupos distintos.**
- **ESTADO DE MÉXICO · Valle de Chalco** — **dos ataques en menos de 24 horas, cuatro muertos, cero
  detenidos en ambos.** **Vigile si la FGJEM publica algo.**

---

## BLOQUE 4 — LO QUE HAY QUE VOLVER A COMPROBAR EN CADA CORTE

| Qué | Estado al cierre de ARGOS 124, revisado para ARGOS 125 |
|---|---|
| ⚠️ **El bloqueo de egreso alcanza también a los MEDIOS** | **REVERIFICADO Y PERSISTE, QUINTA EDICIÓN.** Cuatro dominios, todos `000`. **Techo ★★★☆☆, sexta edición.** ⚠️ **COMPRUÉBELO DE NUEVO: si la lectura funciona, el techo recupera ★★★★☆ y debe hacerse constar** |
| `docs/solicitud-lista-blanca-egreso.md` | **Sigue sin tramitar. Es la única solución real** |
| `gabinetedeseguridad.gob.mx/resultados/` | **Duodécima verificación consecutiva sin cifra utilizable.** Ninguna cifra suya se usa |
| **Boletín federal de acciones relevantes** | ⚠️⚠️ **EL FORMATO CAMBIÓ TRES EDICIONES SEGUIDAS: diario (122), agregado de tres días (123), diario otra vez (124). NO SE PUEDE ANTICIPAR: la triple consulta es obligatoria cada vez.** ⚠️ **Y `gob.mx/sspc` NO INDEXA LOS SUYOS: la tercera consulta —título SIN `site:`— es la única que ha funcionado cinco ediciones seguidas.** ⚠️⚠️ **CON TRECE DÍAS DE VENTANA, NO SE CONSULTA DÍA POR DÍA: rango y título primero, día suelto solo donde el recall señale, y los días no consultados se declaran `NO REVISADA` uno a uno** |
| ⚠️ **El resumidor del buscador sobre el boletín federal** | **En ARGOS 124 dos consultas sobre el MISMO boletín del 22-sep devolvieron LISTAS DE ESTADOS CONTRADICTORIAS. No se integró nada de lo contradicho. Haga lo mismo** |
| ⚠️ **Dominios oficiales mal referenciados** | **Corregidos y confirmados**: Michoacán `comunicacion.fiscaliamichoacan.gob.mx` (**no** `fge.michoacan.gob.mx`) · Campeche `ucs.campeche.gob.mx` (**no** `ssp.campeche.gob.mx`) · Oaxaca `fge.oaxaca.gob.mx` (**no** `fiscaliaoaxaca.gob.mx`). **Confirmados**: `sscqro.gob.mx` (tiene `/boletin/`), `s-seguridad.hidalgo.gob.mx`, `ssc.tlaxcala.gob.mx`, `ssp.zacatecas.gob.mx`, `seguridad.slp.gob.mx` |
| `fiscaliaguerrero.gob.mx` | **Quinta edición sin publicar indexable.** **La vía que funciona es el republicador, no el dominio** |
| **SSC y FGJ de la Ciudad de México** | **Cero boletín sobre Tepito, QUINTA edición.** **Las edades ya convergen por cuatro fuentes: Abigail Herrera, 19, y Odette Rosas, 18** |
| **FGET Tabasco** | **Sin boletín.** ⚠️ **Corrección de calendario de ARGOS 124: el «lunes violento» es el 14-sep, no el 15.** **La cifra sigue en disputa: 4 frente a 6** |
| ⚠️⚠️ **COAHUILA y ZACATECAS** | **Cobertura débil DOS ediciones seguidas: ninguna alcanzó `site:` dedicado a su SSP estatal. ENCABEZAN el triaje de ARGOS 125 por prioridad sobre el ciclo** |

---

## BLOQUE 5 — BARRIDO REGIONAL Y ROTACIÓN

`CLAUDE.md` exige **seis agentes `barrido-regional` en paralelo**. **Lánzelos en un solo mensaje**, con
la deuda del Bloque 3 al frente y **tope duro de búsquedas por eje**.
⚠️⚠️ **Dé a cada agente la ventana COMPLETA CON SUS TRECE DÍAS, no «hoy» ni «esta semana».** Una
ventana mal transmitida al agente produce cobertura de dos días declarada como de trece.

⚠️ **CICLO QUE TOCA: CICLO C — Occidente + Sureste encabezan el triaje judicial.**
⚠️⚠️ **PERO LA PRIORIDAD VENCE AL CICLO: COAHUILA y ZACATECAS arrastran cobertura débil DOS ediciones
seguidas y ninguna alcanzó `site:` dedicado a su SSP estatal. ENCABEZAN.** **Saldar cobertura vence a
mantener el turno.**

**Rendimiento histórico de la rotación**: Ciclo B (121) **no** produjo candidato · Ciclo C (122)
**sí** —Morelia, 93 a 9 m— · Ciclo A (123) **no**, dos correcciones de archivo · Ciclo B (124)
**no**, dos correcciones. **Dos de cuatro ciclos producen candidato; los cuatro producen corrección.**
**Declare el ciclo y su rendimiento: se mide, no se supone.**

### ⚠️⚠️ DECISIÓN DE MÉTODO QUE LLEVA DOS EDICIONES HEREDÁNDOSE — ARGOS 125 LA RESUELVE

**Quince ediciones consecutivas: los seis barridos regionales no han producido un solo hecho rojo.**
Los dos de ARGOS 124 los trajo **el recall del coordinador**, y los seis barridos **no detectaron
ninguno**. Es un patrón, no una casualidad, y **con trece días de ventana el recall de una sola
persona no puede cubrir el país**.

**ORDEN**: cada agente `barrido-regional` incorpora, **además** de la cobertura institucional,
**recall de sucesos de alto impacto de su región** en la ventana. Se declara en el archivo de fuentes
como **cambio de método**, con su rendimiento **región por región**: qué trajo el recall regional que
la cobertura institucional no habría traído. **Si no aporta nada, eso también se escribe y la pregunta
queda cerrada por fin, en un sentido o en otro.**

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  **sin restricción de dominio** antes de cerrarla.
- ⚠️⚠️ **RECALL NACIONAL DEL COORDINADOR, ANTES DE CERRAR LOS BARRIDOS. DECIMOQUINTA EDICIÓN
CONSECUTIVA APORTANDO LOS HECHOS DE MAYOR GRAVEDAD.** En ARGOS 124 trajo **LOS DOS HECHOS ROJOS del
documento** —Comonfort y Coatzacoalcos— y ⚠️ **los seis barridos regionales no detectaron ninguno**.
**No es sustituible por más equipos.** ⚠️⚠️ **Pero con trece días de ventana tampoco basta por sí
solo: de ahí la orden de recall regional del apartado siguiente.**
- ⚠️ **Arbitraje del coordinador sobre las clasificaciones, EN LAS DOS DIRECCIONES.** En ARGOS 124
  se ejerció **al alza** (sierra de Sinaloa, de 🟡 a 🔴, porque quién inició **sí** estaba determinado)
  y **a la baja** (Quechultenango **se mantuvo 🟡** pese a la tentación de subirlo, porque **ninguna
  agravante tasada concurría acreditada**). **Las dos decisiones se declaran.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️⚠️ **UNA CIFRA EXACTA PUEDE SER PRELIMINAR Y QUEDAR SUPERADA POR UNA POSTERIOR SIN CIFRA — TRAMPA NUEVA DE ARGOS 124** | **Puerto Peñasco**: «33 armas largas» era del **20-sep**; el relato posterior de la autoridad da **«más de 40»**. **Tener una cifra exacta no basta: hay que comprobar que no la haya superado el emisor.** **Solo se integraron las 2 Minimi** |
| ⚠️⚠️ **UN OPERATIVO DE DOS DÍAS NO ES UN EVENTO DE ASEGURAMIENTO — TRAMPA NUEVA DE ARGOS 124** | **Puerto Peñasco**: las **7 detenciones son del 18-sep** y el **arsenal del cateo del 19**. **Los detenidos solo se cuentan en el conteo de armamento si son del MISMO evento de aseguramiento** |
| ⚠️⚠️ **UNA CIFRA QUE UNA EDICIÓN DECLARÓ Y NO ADOPTÓ NO ES UN HECHO NUEVO CUANDO SE CONFIRMA** | **Angamacutiro**: `ARG-121-REC-005` **ya citó** los 28 cateos y los 18 detenidos. Publicarlo como hecho propio **infló el corte en 1 hecho y 1 verde**. **Va como `-REC-` o como fe de erratas, según el caso, pero NO al semáforo** |
| ⚠️ **UN AGREGADO DE VÍCTIMAS NO PUEDE CERRAR UNA CIFRA QUE UNA FICHA DECLARA CONTRADICHA** | La Valoración de ARGOS 124 daba «7 muertos y 8 heridos», que **solo salía adoptando en silencio la cifra alta de Valle de Santiago**. **Se publica el RANGO** |
| ⚠️ **UN DESLINDE PUEDE AFIRMAR ALGO FALSO Y PASAR DESAPERCIBIDO** | «otros municipios» frente a `ARG-121-REC-005`, **siendo los mismos dos**. **`editor-duplicidad` existe para esto** |
| ⚠️ **UN BOLETÍN QUE LLEGA TARDE CORRIGE AL ALZA UNA EDICIÓN CERRADA, Y ESO NO ES UN FALLO DE AQUELLA** | `ARG-122-FE-001` corrige **Coyuca de Benítez** con **58 largas, 32 cortas, 314 cargadores y 8,010 cartuchos**. ⚠️ **Y LA FE DE ERRATAS NO VA AL CARTELÓN** |
| ⚠️ **UN BARRIDO PUEDE TRAER UN HECHO YA PUBLICADO COMO NUEVO** | **Nonoava, ARGOS 121.** **Solo el `grep` del coordinador lo detuvo.** **En ARGOS 124 no se repitió** |
| ⚠️ **LA HORA, CUANDO SE PUBLICA, DECIDE LA VENTANA SIN RESERVA** | **Quechultenango trae 12:00, 15:00 y 18:00** y eso permitió **asignarlo sin reserva a la ventana anterior**. **Búsquela siempre** |
| ⚠️ **UNA CIFRA CONTRADICHA SE ARBITRA POR PROCEDENCIA, NO POR MAYORÍA** | **7 detenidos** en Puerto Peñasco (titular de la SSPC federal) frente a 10; **10 años** del menor de Tuxtla (Fiscal General) frente a 12 |
| ⚠️ **SIN EMISOR INSTITUCIONAL NO SE ARBITRA EN ABSOLUTO** | **Valle de Santiago: 3 o 4 muertos, y la FGE no publicó cifra.** **Se publican las dos versiones** |
| ⚠️ **EL RESUMIDOR FABRICA FECHAS, FOLIOS Y AHORA TOPÓNIMOS** | **«Mazatlán, Michoacán» no existe.** **Veintitrés fechas y folios inventados en seis cortes, más un municipio** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado quince ediciones |
| ***Liveblog*** | **Nunca fecha un hecho ni basta como fuente única** |
| **«Más de» y «casi» no son cifra** | **Pero si el cuerpo del boletín la fija, se integra** |
| **Cargadores y cartuchos** | **Nunca se suman entre sí** |
| ⚠️ **Corroboración asimétrica** | **El nivel lo fija el campo PEOR sostenido** |
| **Un delito y su detención son dos eventos** | **ARGOS 124 lo aplicó dos veces**: Tuxtla (🔴 ataque / 🟢 15 detenidos) y sierra de Sinaloa (🔴 agresión / 🟢 aseguramiento) |
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
  `-FE-` se registra en el índice. ⚠️ **ARGOS 124 infringió esto con las cifras de Coyuca y
  `procedencia-cifras` lo detuvo.**
- ⚠️ **Toda ficha `-REC-` lleva su ventana de origen declarada, se muestra atenuada y queda FUERA del
  semáforo, del mapa, del radar y de todos los totales.**
- **Toda cifra en cero lleva al lado el dato que la explica.** **Las categorías en cero se muestran
  atenuadas: la ausencia es dato.**
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`
  —`exec wide` si tiene muchas columnas—. **Nada de `sem-item` fuera de la portada.**

### Estructura de páginas que hereda ARGOS 125

**ARGOS 124 salió en DOCE páginas** con 17 hechos, 2 recuperaciones y 1 sentencia: portada ·
panorama del corte · crimen organizado (I) a (VI) · armamento · sentencias · candidatos y cobertura ·
valoración y conclusiones. **ARGOS 121 salió en nueve con 3 hechos; ARGOS 120, en trece con 19.**
**El número de páginas lo fija el volumen, no la costumbre: si un bloque crece se reparte entre más
páginas, nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de reports/argos-2026-09-24.html, sustituir el <title>, CORTE_FECHA,
#    EVENTOS y EVENTOS_ARM. ⚠️ CORTE_FECHA y el <title> SE HEREDAN y es fácil olvidarlos.
#    ⚠️⚠️ NO los sustituya con un sed GLOBAL: alcanza el bloque de datos y el renderizador.
#    Tramos de la plantilla de ARGOS 124 (reports/argos-2026-09-24.html):
#      (a) cabecera: líneas 1-431   (el <title> está en la línea 5)
#      (b) <script> + MEXICO_VIEWBOX + MEXICO_PATHS: hasta antes de const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>
#    ⚠️ CONSTRUIR POR PARTES EN UN DIRECTORIO DE TRABAJO Y ENSAMBLAR FUNCIONA BIEN Y ES REPETIBLE.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 125 <FECHA> 124 2026-09-24 <HORA>
#    (argumentos: NUM · FECHA · NUM_ANT · FECHA_ANT · HORA real CDMX)

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

⚠️⚠️ **NOVEDAD: EL VALIDADOR YA ESTÁ EN EL REPOSITORIO, en `tools/validar.js`. NO LO REESCRIBA.**
Hasta ARGOS 124 vivía en el directorio de trabajo de la sesión y **cada edición nueva lo rehacía desde
cero**, perdiendo comprobaciones ganadas una por una. **Recibe la ventana por argumento**:

```bash
node tools/validar.js reports/argos-2026-10-07.html 2026-09-24 2026-10-07
```

Comprueba con `node:vm` sobre el `<script>`:
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
⚠️ **Y desde ARGOS 124 comprueba dos cosas más**: que **todo `color` tenga entrada en `SEVERITY_COLOR`
y `SEVERITY_LABEL`** —`rec` no la tenía y los estados se pintaban `fill="undefined"` en silencio— y que
**mapa y radar del corte usen `EVENTOS_CORTE`**, no `EVENTOS`.

⚠️ **RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS**, y **vuelva a recalcularlo DESPUÉS de las
correcciones de los controles**. **En ARGOS 124 los controles cambiaron seis totales de golpe.**

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

⚠️⚠️ **ARGOS 121, 122, 123 y 124 los ejecutaron y LOS OCHO PASES DEVOLVIERON `CORREGIR ANTES DE
PUBLICAR`, con hallazgos reales las ocho veces. NO ROMPA LA RACHA.**
⚠️ **En ARGOS 123 revirtieron el arbitraje central del coordinador; en ARGOS 124 cambiaron SEIS totales
nacionales, reclasificaron un hecho y encontraron un defecto de herramienta que contradecía al propio
cartelón.**
⚠️⚠️ **Y con trece días de ventana, el riesgo de duplicación contra el archivo es el más alto de la
serie: `editor-duplicidad` es más necesario aquí que en ninguna edición anterior.**

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos,
sobre los controles y sobre sus propias instrucciones. ⚠️ **En ARGOS 124 el coordinador verificó por su
cuenta el hallazgo de Puerto Peñasco y lo encontró MAYOR de lo que el control apuntaba.**
**Un control acierta en la dirección; el coordinador fija la magnitud.**

⚠️⚠️ **PERO EN ARGOS 123 EL COORDINADOR PERDIÓ EL ARBITRAJE CENTRAL, Y ESO TAMBIÉN ES EJERCERLO**:
defendió integrar siete renglones de un boletín **citando el precedente que le favorecía y sin buscar
el que le contradecía** —ARGOS 121 frente al boletín del 14-16-sep, y `ARG-122-REC-002`—.
**`editor-duplicidad` los encontró, eran ciertos y el arbitraje se revirtió entero.**
**BUSQUE EL PRECEDENTE QUE LE CONTRADICE, NO SOLO EL QUE LE RESPALDA. Cuando varios barridos coinciden
contra el criterio del coordinador, eso es dato. Un arbitraje que no puede perderse no es arbitraje.**

⚠️ **Y EL `grep` POR TOPÓNIMO SOBRE `reports/indice-arg-id.md` ES DEL COORDINADOR Y SE HACE
INMEDIATAMENTE ANTES DE FICHAR**: en ARGOS 123 y 124 detuvo sendas duplicaciones —Iztapalapa y
Tempoal— que los barridos traían como hechos nuevos.

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS**, y **toda disposición es
   expresa** —cerrado, sin avance o fuera de ventana—.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-` y los `-REC-`**—.
3. Escribir `reports/argos-<FECHA>-fuentes.md` con el registro del barrido, el ciclo aplicado, los
   arbitrajes en las dos direcciones, los hallazgos de los controles y las limitaciones de herramienta.
4. **Escribir `reports/_arranque-ARGOS-126.md` y `reports/_ordenes-ARGOS-126.txt`** y borrar este
   archivo y su orden. ⚠️ **No los herede por inercia: ARGOS 125 reescribió los de la 125 porque
   declaraban una ventana corta que no existió.** **Una orden con premisas falsas es peor que no
   tenerla.**
5. **Empujar a la rama designada** y **mergear a `main`**, verificando que quedó.
