# ARGOS 105 — Registro de fuentes

Corte: 2026-08-23 · Ventana de hechos: **2026-08-21 07:55 CDMX → 2026-08-23 08:00 CDMX**.
Continuación estricta de ARGOS 104 (corte 2026-08-21). No hubo edición el 22-ago, de modo que la
ventana es de **~48.1 horas**, de la mañana del viernes a la mañana del domingo —el doble de lo
habitual—. Este documento respalda `argos-2026-08-23.html` y `argos-2026-08-23-movil.html`, y existe
para que todo `SIN DATO` de la edición sea demostrable.

**Hora de arranque verificada**: `TZ=America/Mexico_City date` → **2026-08-23 08:00 CST (UTC−6)**.
Es la hora sellada en encabezado, pie y las nueve marcas `Consulta:` del cartelón, escritorio y
móvil.

---

## Limitación que define esta edición: se agotó el presupuesto de búsqueda de la sesión

**Hallazgo de método, no del territorio.** El presupuesto de búsqueda web de la sesión
(**200 de 200 llamadas**) **se agotó antes de que cinco de las seis regiones pudieran ejecutar una
sola consulta**. El equipo del Sureste lo detectó al recibir el rechazo del sistema en sus cinco
primeros intentos y lo reportó como hallazgo crítico en vez de entregar un informe vacío; el
coordinador lo verificó con una consulta de control propia, con idéntico resultado.

Consecuencia, y es la que gobierna todo el producto de hoy:

- La **ventana propia del corte quedó barrida solo en el Noreste**, con resultado cero.
- **Noroeste, Occidente, Centro, Golfo, Sureste y el emisor federal quedan `NO REVISADA`**, en las
  32 entidades menos las cinco del Noreste: **27 de 32**.
- **Ningún módulo declara `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`**, porque la condición previa
  —el barrido— no se cumplió. La casilla aplicada es `NO REVISADA`, que es la que corresponde y no
  se disfraza.
- **El Nivel de Riesgo Nacional se declara `NO DETERMINABLE`** para la ventana. Emitir una
  valoración «baja» sobre cinco regiones no observadas convertiría un vacío de observación en un
  hallazgo.

**Decisión editorial tomada con el usuario**: publicar la edición con la cobertura realmente
verificada y **trasladar el barrido de la ventana 21-23 de agosto a ARGOS 106 como encargo
explícito**, en vez de retrasar la publicación o de rellenar el vacío. Queda escrito en
`_pendientes.md`.

## Limitación permanente — decimosexta edición consecutiva con el egreso bloqueado

Los dominios `*.gob.mx` y los de fiscalías y secretarías estatales siguen fuera de la lista blanca
de egreso (`CONNECT tunnel failed, response 403`). **Cero portales leídos por acceso directo.** El
techo de confianza del producto sigue en **★★★★☆**. `docs/solicitud-lista-blanca-egreso.md` **sigue
sin tramitar**.

---

# PRIORIDAD 1 — La deuda de registro, saldada

Era el primer encargo de `_pendientes.md` y **no costaba búsquedas**: los hechos ya estaban
encontrados, verificados y clasificados por ediciones anteriores; lo que nunca recibieron fue ficha.
Se ejecutó primero, íntegramente con `grep` sobre **todo el repositorio** —no solo sobre
`indice-arg-id.md`—, conforme a la lección de ARGOS 104.

## Resultado: seis fichas nuevas, un caso fuera de umbral y **tres falsas acusaciones de omisión**

El inventario heredado hablaba de «cuatro hechos sin ficha» más «seis vacíos incidentales que nadie
ha revisado nunca». Al contrastarlo con el archivo, la cuenta real es distinta.

### Los cuatro inventariados en ARGOS 104: los cuatro sin ficha, confirmado

| Hecho | Verificación `grep` | Resolución |
|---|---|---|
| **Quema de dos camiones de volteo**, Sabanillas, Tuxpan-Tamiahua, Veracruz | Solo aparece en `argos-2026-08-13-fuentes.md`, `argos-2026-08-14-fuentes.md` y el inventario de ARGOS 104, **siempre como nota de método, nunca con ARG-ID** | **Ficha `ARG-105-REC-003`** (🟡) |
| **Homicidio de un tráilero**, carretera Nuevo Teapa–Cosoleacaque, Veracruz | Ídem. `argos-2026-08-16-fuentes.md:445` menciona Cosoleacaque, pero es **otro caso** —tres sentenciados a 45 años por homicidio doloso— y no se funde | **Ficha `ARG-105-REC-004`** (🟡) |
| Detención de **Gerardo Humberto Piña, "El G1"**, Ensenada, BC | Solo en fuentes y en menciones narrativas de ARGOS 96/97, **sin ARG-ID** | **Ficha `ARG-105-REC-005`** (🟢) |
| Detención de **Erick Jesús "N", "El Loco"**, Metepec, Edomex | Ídem | **Ficha `ARG-105-REC-006`** (🟢) |

### Los seis «vacíos incidentales» de `argos-2026-08-14-fuentes.md`, líneas 130-150

`_pendientes.md` los daba por **nunca revisados**. No es exacto: **ARGOS 98 sí los revisó** y publicó
su veredicto en `argos-2026-08-15-fuentes.md`, págs. 465-525. Lo que nadie hizo fue **registrarlos**.
Es el mismo modo de fallo que ARGOS 104 diagnosticó, un escalón más arriba: no es que el hecho no se
encontrara, ni siquiera que no se verificara — es que **se verificó dos veces y siguió sin ficha**.

| # | Hecho | Estado real | Resolución en ARGOS 105 |
|---|---|---|---|
| 1 | **Huachicol en Pesquería, NL** (62,000 L) | Confirmado por ARGOS 98, **sin ARG-ID** | **Ficha `ARG-105-REC-007`** (🟢) |
| 2 | **Rescate de secuestro en Teotihuacán, Edomex** | Confirmado por ARGOS 98, **sin ARG-ID** | **Ficha `ARG-105-REC-008`** (🟢) |
| 3 | **Aseguramiento en Apatzingán, Michoacán** | **NO ERA VACÍO** — ya anulado por ARGOS 98 | Sin acción. El registro válido es `ARG-95-ARM-001` |
| 4 | **Sentencia de Coronango, Puebla** | Ya registrada | Sin acción. El registro válido es `ARG-102-SEN-REC-001` |
| 5 | **Sentencia contra 19 integrantes del CJNG, Jalisco** | ⚠️ **NO ERA VACÍO — falsa acusación de ARGOS 98** | **Se cierra el pendiente.** Ver abajo |
| 6 | **Sentencia por abuso sexual, La Paz, BCS** | Confirmado, pero **solo dos fuentes regionales** | **Declarado fuera de umbral.** Ver abajo |

### ⚠️ Tres acusaciones de omisión que el archivo desmiente

Este es el hallazgo de método más importante de la edición, y **no entra al cartelón**.

**(1) Los funcionarios de Medio Ambiente del Edomex.** ARGOS 97 los listó como el quinto de sus
«seis vacíos», afirmando que «no fue documentado por ARGOS 94, 95 ni 96». **Es falso.** La detención
está publicada como **`ARG-94-003`** en `argos-2026-08-11.html`, con ficha completa, los dos nombres
—Raúl Piña Horta y Carlos Eduardo Solares Vega— y fecha 2026-08-10. Su desarrollo judicial es
`ARG-97-004`, publicado por el propio ARGOS 97 en el mismo corte en que lo acusaba de vacío. **No
procede ninguna ficha.**

**(2) Los 19 sentenciados de Tizapán el Alto.** ARGOS 98 lo declaró «VACÍO CONFIRMADO». **Es falso.**
Está publicado como **`ARG-94-SEN-002`** en `argos-2026-08-11-fuentes.md`, con el desglose completo
—**12 sentenciados a 18 años 1 mes 22 días y 7 a 16 años 6 meses**, acopio de armas y asociación
delictuosa, detención de noviembre de 2022 tras enfrentamiento con SEDENA— y cinco fuentes. El
pendiente vivo desde ARGOS 102 («~332 años acumulables, ventana de ARGOS 95/96, tercera edición que
se reencuentra y no se duplica») **está equivocado en el número de edición y en la premisa**: la
ventana es la de ARGOS 94 y **no falta el comunicado de la FGR para integrarlo, porque ya está
integrado**. **Pendiente cerrado.**

**(3) Apatzingán**, ya anulado por ARGOS 98 en su momento y aquí solo reconfirmado.

**Lección**: de los doce «vacíos» que el archivo arrastraba, **tres no lo eran**. Es la cuarta
edición consecutiva en que el control con `grep` impide acusar a una edición anterior de algo que sí
hizo — y la primera en que descubre que **dos pendientes vivos descansaban sobre una premisa falsa**.

### Caso declarado expresamente fuera de umbral

**La Paz, Baja California Sur** — Carlos "N", abuso sexual contra una niña (hecho del 14-abr-2025,
col. Colina de la Cruz), procedimiento abreviado, **2 años 8 meses** más multa de 134 días
($15,160.76) y terapia vía CJM. Consta el término jurídico, pero **solo con dos fuentes regionales y
sin comunicado institucional**. La regla de integración es asimétrica: en sentencias la confianza
Baja **no basta**. Se declara `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL` y
**queda resuelto como caso**, no en espera indefinida: sale de la lista de pendientes activos tras
seis ediciones sin avance, y solo volvería si apareciera fuente oficial.

---

# PRIORIDAD 2 — Auditoría de las ventanas de ARGOS 88 a 93

Único tramo que nadie había auditado, y el producido con el método menos maduro. Se ejecutó
**primero y en solitario**, antes de lanzar ninguna región, y **por tipo de hecho, no por entidad**,
que es el método que ha rendido tres veces.

**Ventanas cubiertas**: del **2 al 10 de agosto de 2026** (ARGOS 88 = corte del 4-ago;
ARGOS 90 a 93 = cortes del 7 al 10 de agosto). **La serie no tiene edición 89.**

**Equipos**: dos temáticos —(A) masacres y homicidios múltiples · (B) violencia colectiva— más una
**ronda de corroboración** sobre los candidatos. El bloque de ataques contra autoridades se omitió,
conforme al encargo: ese tipo de hecho sí se recoge.

## Lo que la auditoría integra

| ARG-ID | Hecho | Ventana de origen | Color |
|---|---|---|---|
| `ARG-105-REC-001` | **Saltillo, Coahuila** — tres personas asesinadas en un domicilio y una cuarta herida de gravedad; el agresor, expolicía de Texas, detenido esa noche en Piedras Negras | **Intervalo no cubierto (hueco 88/90)** | **🔴** |
| `ARG-105-REC-002` | **Tijuana, Baja California** — restos humanos fragmentados en la cajuela de un vehículo, en el estacionamiento de un supermercado sobre el bulevar Agua Caliente | **ARGOS 88** | **🔴** |

### El hallazgo estructural: la serie tiene un intervalo que ninguna edición cubre

El multihomicidio de Saltillo ocurre **la tarde del 4 de agosto**. **ARGOS 88 cerró a las 07:15 de
ese mismo día** y la ventana declarada de **ARGOS 90 abre el 5 de agosto**. **No existe ARGOS 89.**

El hecho, por tanto, **no fue omitido por ninguna edición**: cayó en un intervalo que ninguna
declaró suyo. Por eso `ARG-105-FE-004` no rectifica ningún conteo — es la única fe de erratas de
esta edición que **no cambia una cifra**, y existe para dejar constancia del hueco. Es un modo de
fallo distinto de los dos que la serie ya conocía: no es de búsqueda ni de registro, es **de
continuidad de ventana**.

## Ronda de corroboración — lo que cerró y lo que dejó abierto

Quinta edición consecutiva en que rinde, y esta vez su aportación decisiva fue **un deslinde**.

**Saltillo — resuelto en cuatro de cinco puntos.** Fijó **3 muertas y 1 herida** sin discrepancia
entre siete fuentes; localizó un **segundo boletín institucional** que no se conocía
(`sitio.fgecoahuila.gob.mx/2026/08/05/`, previo al del 06-ago, ambos con **fecha en la ruta**);
confirmó que las tres víctimas eran **civiles**, sin carácter de autoridad. **No resolvió la hora**:
las fuentes dicen «por la tarde» y un rango de 14:30-15:30 h procede de un resumen de buscador que
**no pudo cotejarse**, así que **no se consigna como hora del hecho**. Detectó además una
**variación terminológica real** —«homicidio calificado» frente a «homicidio agravado», ambos
atribuidos a la Fiscalía—: `CONTRADICHA`, se publican los dos, no se funden. Y descartó un resultado
agregado que situaba el hecho en «colonia Antonio Cárdenas» y «un lunes»: **incompatible con el
calendario** —el 4-ago-2026 fue martes— y con siete fuentes identificables.

**Tijuana — el deslinde que evitó una duplicidad.** El archivo ya registra `ARG-103-REC-002`:
**cuatro cuerpos en cajuelas, zona Hipódromo, Tijuana, 17 de agosto**. Los dos hechos comparten
municipio, zona y *modus*, y **ambos cayeron en lunes** —coincidencia real del calendario que es
precisamente lo que induce a fundirlos—. El deslinde quedó acreditado en **cinco campos**: fecha (3
frente a 17), número de vehículos (uno frente a cuatro), vehículo (**Honda Civic verde, placas de
California 4UDV950**; ninguno de los cuatro del 17 lo es), punto exacto (Calimax de Agua Caliente
frente a cuatro puntos distintos) y forma de presentación (**restos fragmentados en contenedores**
frente a cuerpos completos encajuelados). **Son eventos autónomos.**

Lo que **no** cerró: el **número de víctimas de Tijuana** sigue `CANTIDAD NO PUBLICADA` —la FGE de BC
no descartó más de una y no se localizó identificación forense posterior—; **no existe boletín
institucional** localizable del hecho; y persiste una **contradicción de colonia** (Hipódromo, en los
titulares de dos regionales, frente a «20 de Noviembre» en un resumen de buscador):
`CONTRADICHA — no se funden`.

## Categorías con resultado cero, declaradas y no supuestas

El equipo B recorrió con vocabulario institucional y periodístico y **no localizó ningún hecho con
fecha verificable dentro del 2-10 de agosto** en: **narcobloqueos y quema masiva de vehículos**;
**ataques con explosivos, AEI o drones armados contra población civil**; **fosas clandestinas**
propiamente dichas; **desapariciones múltiples** (3+ personas en un mismo hecho); **secuestros
masivos**; **motines carcelarios con víctimas**; **ataques a infraestructura crítica**; y
**desplazamiento forzado** como hecho nuevo fechado.

El equipo A no localizó ningún homicidio múltiple adicional de 3+ víctimas más allá de Saltillo, y
documentó **cinco hechos de 2 víctimas** que quedan expresamente fuera del umbral: Bacalar–Felipe
Carrillo Puerto (QRoo, 3-ago), Santiago Undameo (Michoacán, 8-ago), Nacajuca (Tabasco, 7-ago),
Cuernavaca (Morelos, 2-ago) y La Cima, Zapopan (Jalisco, 10-ago).

## Trampas de aniversario detectadas y descartadas

Nueve, todas verificadas por año antes de descartarse. Las tres que más se parecían a un hallazgo:

- **Motín del penal de Apodaca, NL** — los resultados solo acreditan **enero y julio de 2022**.
- **Secuestro de 12 trabajadores en Anáhuac, NL** — hecho de **abril de 2024**, con una cita
  contaminada que atribuía declaraciones a un presidente que no lo era en 2026.
- **Masacre de Buenavista de los Hurtado, Guerrero** — **enero de 2024**, no 2026.

Se descartaron además, por caer fuera de la ventana auditada: los narcobloqueos de Los Reyes y
Peribán (Michoacán) y la quema de vehículos en Colima, ambos del **1-ago**; el tiroteo de Salamanca
(**25-ene-2026**); el ataque de Tlaltizapán, Morelos (**23-may-2026**); y los hallazgos de fosas de
Celaya, Apaseo el Alto, Miguel Alemán y Bahía de Lobos, todos del **17-19 de agosto**.

## Reserva de método que la auditoría deja anotada

El equipo B observó que el buscador devolvió **una concentración desproporcionada de resultados en
la tercera semana de agosto** para casi todas las categorías, y muy poca cobertura específica del
2-10 de agosto. Puede deberse a menor actividad, o a que el índice prioriza contenido reciente:
**no se puede descartar un falso vacío**. Los ceros declarados arriba son ceros **de lo indexado**,
no del territorio.

---

# Barrido del corte — Ciclo B

**Rotación declarada: CICLO B.** Encabezaban el triaje judicial **Noreste y Golfo**; las otras cuatro
regiones encabezaban con armamento. **Ninguna entidad venía en `NO REVISADA` de ARGOS 104**, así que
el turno se aplicó limpio, sin prioridad sobre el ciclo.

De las seis regiones, **solo el Noreste alcanzó a ejecutarse** antes del agotamiento del
presupuesto. El Golfo, la otra región del ciclo, **no llegó a lanzar consulta**: la mitad del
experimento de rotación de esta edición **no se pudo realizar**.

## Noreste — barrido completo, resultado cero

| Portal | Qué devolvió | Casilla |
|---|---|---|
| `sitio.fgecoahuila.gob.mx` | Boletines hasta el 06-ago; el archivo `/2026/` no devolvió nada de la ventana | `SIN RESULTADO INDEXADO EN VENTANA` |
| `fiscalianl.gob.mx` | Cero, como advierte el directorio: portal de servicios **sin sala de prensa indexable**. **No es un vacío del territorio** | `SIN RESULTADO INDEXADO EN VENTANA` |
| `fgjtam.gob.mx` | Solo PDF y diagnósticos institucionales | `SIN RESULTADO INDEXADO EN VENTANA` |
| `fiscaliaslp.gob.mx` | Publica boletines de condena, **ninguno fechable**; los fechados por medios caen el 12 y el 15-ago | `SIN RESULTADO INDEXADO EN VENTANA` |
| `fiscaliazacatecas.gob.mx` · `ssp.zacatecas.gob.mx` | Sentencias sin fecha en URL; el ancla `ljz.mx` solo devolvió casos de julio | `SIN RESULTADO INDEXADO EN VENTANA` |
| `zacatecas.gob.mx` | Operación Rastrillo (12-ago) y explosivos de Jiménez del Teúl (20-ago) | Ambos **fuera de ventana** |
| `gob.mx/sspc` | Boletín del **20-ago** con URL canónica | **Fuera de ventana** |

**Entidades revisadas: 5. Portales leídos por acceso directo: 0.** Las SSP estatales, policías
estatales y mesas de paz de las cinco entidades quedaron `NO REVISADA` por presupuesto, y así se
declaran.

**Qué aportó encabezar el triaje judicial**, y el resultado es **negativo e informativo**: el patrón
de ARGOS 101 y 104 —«la sentencia integrable aparece en la primera entidad del triaje de la región
que encabeza»— **no se repitió**. Dos éxitos no garantizan un tercero. Lo que sí permitió el orden
fue **descartar tres candidatos judiciales con evidencia** —Santa Catarina (NL), Ponciano "N" y
Raúl "N" (Coahuila)— antes de gastar presupuesto en armamento, y comprobar temprano que el mismo
patrón de portales sin fecha se repetiría en el otro módulo, como en efecto ocurrió.

**Candidato de frontera para ARGOS 106**: la sentencia de **31 años 3 meses** contra Francisco "N" y
Pedro "N" por el ataque de Rincón de Mitras, Santa Catarina, NL, publicada el **20-ago**
(`mvsnoticias.com/nuevo-leon/2026/8/20/`) — **un día antes de abrir la ventana**, y sin comunicado de
la FGJNL localizado.

**Indicio no integrable**: Blog del Narco menciona un choque entre Ejército y civiles armados en
Tamaulipas el «viernes 21 de agosto», **sin municipio, sin cifras y sin corroboración**. Fuente
abierta única: `NO OFICIAL — PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL`. No se integra ni se descarta.

**Contradicción menor anotada y no aplicada**: una consulta devolvió para Juchipila **118 cartuchos**
frente a los **60** ya publicados en `ARG-104-ARM-001`. Es probablemente el mismo resumidor
parafraseando con imprecisión. **No se toca el archivo sin lectura directa que lo sostenga.**

## Las cinco regiones restantes

| Región | Entidades | Estado |
|---|---|---|
| Noroeste | 6 | `NO REVISADA` — presupuesto agotado |
| Occidente | 6 | `NO REVISADA` — presupuesto agotado |
| Centro | 7 | `NO REVISADA` — presupuesto agotado |
| Golfo | 2 | `NO REVISADA` — presupuesto agotado. **Encabezaba el triaje judicial por ciclo** |
| Sureste | 6 | `NO REVISADA` — presupuesto agotado; el equipo lo detectó y reportó en vez de entregar un informe vacío |
| Federal | — | `NO REVISADA` para la ventana 21-23. **La regla de la triple consulta no llegó a ejecutarse** |

---

# Fe de erratas de esta edición

| ARG-ID | Edición | Publicado | Rectificado | Hecho que lo rectifica |
|---|---|---|---|---|
| `ARG-105-FE-001` | **ARGOS 88** | 🔴 **0** · 🟡 1 · 🟢 4 | 🔴 **1** · 🟡 1 · 🟢 4 | `ARG-105-REC-002` Tijuana |
| `ARG-105-FE-002` | **ARGOS 94** | 🔴 1 · 🟡 1 · 🟢 **3** | 🔴 1 · 🟡 1 · 🟢 **5** | `ARG-105-REC-006` Metepec · `ARG-105-REC-008` Teotihuacán |
| `ARG-105-FE-003` | **ARGOS 95** | 🟡 **3** · 🟢 **8** | 🟡 **5** · 🟢 **10** | `ARG-105-REC-003` · `-004` · `-005` · `-007` |
| `ARG-105-FE-004` | **Ninguna** | — | — | `ARG-105-REC-001` Saltillo cae en el **hueco 88/90**; ningún conteo se rectifica |
| `ARG-105-FE-005` | **ARGOS 104** | 7 a 10 m · multa $64,150.38 · reparación $397,554.90 | **«Más de 7 años», no sumable**; multa y reparación `CANTIDAD NO DETERMINADA` | Cifras arrastradas **dos ediciones** sin respaldo citable |

**ARGOS 95 se rectifica por segunda edición consecutiva**: con `ARG-104-FE-001` (Aquila) y las
cuatro fichas de hoy, su corte pasa de **0 🔴 · 3 🟡 · 8 🟢** a **1 🔴 · 5 🟡 · 10 🟢**.

**Residuo conocido y acotado**: las portadas de ARGOS 88, 94 y 95 siguen mostrando su semáforo
original, porque se generan desde el arreglo `EVENTOS` de cada edición y regenerarlas obligaría a
reescribir fichas que la rectificación deja intactas. La rectificación consta en el bloque de fe de
erratas de cada cartelón afectado.

---

# Nota de método sobre el generador móvil

Se corrigió **la herramienta, no su salida**, conforme a la práctica establecida en ARGOS 104.

**Fallo detectado**: el ancla de inyección de los SVG de portada exigía el título **literal**
`SEMÁFORO ARGOS`. Esta edición matizó ese encabezado —`SEMÁFORO ARGOS — HECHOS DE VENTANAS
ANTERIORES`—, la expresión regular dejó de casar y la móvil salió **sin radar, sin mapa y con los
`sem-item` del escritorio en crudo**. El fallo era **silencioso salvo por la validación**, que lo
atrapó. Corregido para tolerar cualquier sufijo, en ese ancla y en el de `EJES DEL DÍA`.

**Segundo fallo**: el validador exigía **exactamente 3 SVG**. Una edición sin aseguramientos no tiene
mapa de armamento y legítimamente lleva **2**. Ahora cuenta los que el escritorio realmente pide.

**Control de desborde**: atrapó **tres URLs de 75+ caracteres** —los dos boletines de la FGE de
Coahuila y el *slug* de Infobae— que habrían desbordado la pantalla en móvil. Se corrigieron **en el
escritorio**, con puntos de corte, y se regeneró. **Paridad final: 9 de 9 fichas**, contadores
coincidentes (🔴 2 · 🟡 2 · 🟢 4).

---

# Control editorial antes de publicar

Los tres controles obligatorios, con su resultado. **`barrido-regional` ×6 no pudo completarse** —el
presupuesto de búsqueda se agotó tras el Noreste—, y esa es la razón por la que ningún módulo declara
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`: la condición previa no se cumplió.

## `editor-duplicidad` → **PUBLICABLE**

Contrastó los ocho `-REC-` y las cinco fes de erratas contra **todo el repositorio**, no solo contra
el índice, y verificó los tres cruces de mayor riesgo:

- **Tijuana 3-ago frente a `ARG-103-REC-002` (17-ago)**: el deslinde de cinco campos **se sostiene**.
  Confirmó además con `date -d` que **ambas fechas caen en lunes** — coincidencia real del
  calendario, no error, y precisamente lo que induciría a fundirlos.
- **Pesquería frente a `ARG-96-004`** (General Escobedo): distintos por municipio, volumen y fecha.
- **Cosoleacaque frente a `argos-2026-08-16-fuentes.md:445`**: es **otro caso** —sentencia de 45 años
  contra tres personas por homicidio doloso agravado—, sin relación con el homicidio sin detenidos de
  la carretera.

**Control de autorreferencia: limpio.** Es la **primera edición en tres** en que no hubo que retirar
un solo pasaje del cartelón: ARGOS 103 y 104 necesitaron esa poda, la segunda vez en doce pasajes.
Escribir el borrador **sin** esos bloques desde el principio, en vez de escribirlos y retirarlos,
funcionó.

**Señalamiento no bloqueante, aplicado igualmente**: el resumen ejecutivo y las conclusiones 1 y 3
enunciaban el mismo juicio dos veces. Se aligeró el resumen ejecutivo, que ahora se queda con el
hecho y deja el juicio interpretativo a las conclusiones.

## `procedencia-cifras` → **CORREGIR ANTES DE PUBLICAR**, tres hallazgos, los tres aplicados

**(1) Pesquería: el archivo ya tenía una reconciliación mejor que la que iba a publicarse.** La ficha
reproducía la versión de ARGOS 98, sin cotejar **`ARG-102-FE-004`**, que volvió sobre el mismo hecho
—mismo municipio, misma fecha, mismos 62,000 L— con **cuatro URLs con fecha en la ruta** y estableció
un listado distinto: **sin oleoducto**, con **9 cajas secas vacías**, con el predio nombrado
(**Dulces Nombres**) y con el incendio previo precisado (**1 muerto, 3 lesionados y 1 intoxicado**).

Es el hallazgo más incómodo de la edición porque **el `grep` de PRIORIDAD 1 sí devolvió esa línea** y
el coordinador no la siguió. La lección no es que falte un control, es que **un `grep` solo sirve si
se leen sus resultados**.

Corrección aplicada: se retira **«1 oleoducto»** de las cinco apariciones que tenía en el cartelón
—portada, ficha, explotación, pág. 5 y conclusión 5— y del arreglo `EVENTOS`; se añaden las **9 cajas
secas vacías**, el **predio Dulces Nombres** y el **intoxicado**; la corroboración pasa a declarar las
**cuatro URLs fechadas**; el antecedente declara ahora las **cuatro apariciones previas sin ARG-ID**
(ARGOS 97, 98, 101 y `ARG-102-FE-004`); y la confianza sube de 🟠 **Bajo** a 🟡 **Medio**, porque
cuatro URLs fechadas sostienen más que cinco medios sin fecha. La divergencia queda declarada como
`CONTRADICHA — no se funden las dos versiones`.

**(2) El conteo de fuentes regionales de los dos hechos de Veracruz no es verificable.** «Más de
nueve» y «siete» nacen en `argos-2026-08-14-fuentes.md:66` **sin nombrar una sola cabecera regional**
—solo se nombran los dos nacionales, Infobae y Excélsior— y se arrastraban sin recontarse desde
ARGOS 97. Es exactamente el patrón que el hallazgo `H-06` de ARGOS 104 documentó («ocho fuentes
regionales — se nombran siete»).

Corrección aplicada: **se deja de dar el número como preciso**. Las dos fichas declaran ahora
`CONTEO DE FUENTES NO VERIFICABLE`, y su nivel de confianza se apoya en lo que sí está nombrado —dos
nacionales, una con fecha en ruta, más institucional indirecta—. **El hecho subyacente no se toca**:
está sostenido con independencia del recuento.

**(3) Saltillo: una cifra derivada sin declarar, y además underivable.** La explotación afirmaba que
entre el hecho y el intento de cruce hubo «**menos de nueve horas** y unos 400 km». La propia ficha
declara que **la hora del hecho no está fijada**, así que el intervalo **no puede derivarse en
absoluto**, y la distancia tampoco tenía fuente citada.

Corrección aplicada: **se retiran las dos cifras**. El párrafo dice ahora lo que las fuentes sí
sostienen —el hecho es de la tarde, la detención de esa noche— y declara expresamente que **el
intervalo exacto no se calcula**.

## Lo que los dos controles confirmaron sin cambios

- **Aritmética de las tres fes de erratas**: recalculada de forma independiente por los dos controles
  contra los arreglos `EVENTOS` reales de ARGOS 88, 94 y 95. **Las tres cuadran exactamente.**
- **Trazado ficha → tabla**: ninguna de las ocho fichas declara aseguramiento de armamento, la pág. 5
  lo declara igual, y las cuatro fichas con detenido figuran en la tabla de la pág. 2 con sus seis
  personas. Sin omisiones silenciosas.
- **Paridad escritorio/móvil**: idéntica en fichas, ejes, tablas, contadores e indicadores de
  cobertura. **No se repitió el fallo de etiquetas desplazadas** de ediciones previas.
- **`ARG-105-FE-005` (Durango)**: premisa comprobada contra `argos-2026-08-21-fuentes.md:476` — el
  *slug* institucional es `fged-obtiene-sentencia-de-mas-de-7-anos-…`, que sostiene «más de 7 años» y
  **no** la pena exacta ni los importes. Segunda edición sin respaldo citable: el umbral se aplica
  correctamente.

---

# Cobertura declarada de esta edición

| Concepto | Valor |
|---|---|
| Entidades revisadas en la ventana del corte | **5 de 32** (Noreste) |
| Entidades `NO REVISADA` | **27 de 32** |
| FGR revisada | **No** |
| Emisor federal — regla de la triple consulta | **No ejecutada** |
| Portales leídos por acceso directo | **0** — decimosexta edición |
| Hechos fijados dentro de la ventana del corte | **0** |
| Hechos de ventanas anteriores documentados por primera vez | **8** |
| Sentencias integradas al conteo nacional | **0** |
| Total nacional de armamento | `SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE` |
| Nivel de Riesgo Nacional | `NO DETERMINABLE` para la ventana |
