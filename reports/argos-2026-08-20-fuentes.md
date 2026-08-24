# ARGOS 103 — Registro de fuentes (auditoría)

Corte: 2026-08-20 · Ventana de hechos: **2026-08-19 07:45 CDMX → 2026-08-20 08:16 CDMX**.
Continuación estricta de ARGOS 102 (corte 2026-08-19). Este documento respalda
`argos-2026-08-20.html` y `argos-2026-08-20-movil.html`, y existe para que todo `SIN DATO` de la
edición sea demostrable.

Ventana efectiva: **~24.5 horas**, de la mañana del miércoles a la mañana del jueves. Es más larga
que la de ARGOS 102 (~19 h) y más corta que la de ARGOS 101 (~35 h).

**Esta edición no se define por lo que encontró en su ventana, sino por lo que encontró en las
ventanas de las tres ediciones anteriores.**

---

## Limitación metodológica — decimocuarta edición consecutiva con el egreso bloqueado

**Sonda de entorno ejecutada al inicio de la sesión por el coordinador**, con `curl` directo:

| Host | Resultado |
|---|---|
| `www.gob.mx/sspc/prensa` | `curl: (56) CONNECT tunnel failed, response 403` |
| `www.gob.mx/guardianacional/prensa` | 403 al CONNECT |
| `comunicacion.fiscaliaveracruz.gob.mx/archivo/` | 403 al CONNECT |
| `gabinetedeseguridad.gob.mx/resultados/` | **403 al CONNECT — primera sonda de este host** |

Es una **denegación por política de la organización en el proxy de salida**, no un fallo de
herramienta ni un problema de los portales. No se intentó rodearla.

**Hallazgo nuevo de la sonda**: `gabinetedeseguridad.gob.mx/resultados/`, que pasa a ser **portal
federal de consulta obligatoria a partir del 1-sep-2026** por anuncio del propio emisor,
**también está bloqueado**. El pendiente que ARGOS 102 abrió para septiembre no se resuelve
incorporándolo al barrido: nace bloqueado igual que los demás. Queda anotado con su sonda.

**Consecuencia operativa aplicada**: se prohibió `WebFetch` a los diez equipos de esta edición.
**Los diez lo respetaron: cero usos de `WebFetch` en toda la edición.**

**Cero portales leídos por acceso directo, de ~128 objetivo.** Ningún
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de esta edición puede presentarse como vacío
institucional verificado; la casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Techo de confianza efectivo: ★★★★☆** — decimocuarta edición consecutiva sin superarlo.

---

## PRIORIDAD 1 — La auditoría de cobertura: el veredicto es SISTEMÁTICO

Se aplicó la lección 1 de ARGOS 101 y 102: la verificación prioritaria se ejecutó **antes de lanzar
los seis barridos y con la sesión para ella sola**. Consumo: **36 búsquedas de 36 asignadas** en la
primera ronda (tres equipos temáticos, los tres con el tope agotado) más **12 de 12** en la ronda de
corroboración.

### La pregunta que se auditaba

ARGOS 102 localizó **dos eventos 🔴 que ARGOS 100 y 101 no registraron** —la masacre de Tlapa de
Comonfort y el motín de Cárdenas, Tabasco—, ambos publicados **con fecha en la URL en medios
nacionales**. La pregunta era si ese fallo era **puntual o sistemático**, porque las valoraciones de
toda la serie reciente descansan sobre esa cobertura.

### El método que la respondió

**Se consultó por tipo de hecho y no por entidad.** Es la inversión exacta del método que produjo el
fallo: el barrido ordinario recorre 32 entidades y da por vacías las regiones que cierran en cero.
Tres equipos temáticos cubrieron, cada uno con 12 búsquedas y a escala nacional, las ventanas de
ARGOS 99, 100 y 101 (15-ago 07:29 → 18-ago 13:37):

| Equipo | Bloque temático | Resultado |
|---|---|---|
| **1-A** | Masacres y homicidios múltiples contra civiles | **Tres hallazgos** — dos confirmados, uno corroborado después |
| **1-B** | Ataques contra autoridades y personas protegidas | **Cero hallazgos nuevos.** Un candidato, refutado por el coordinador |
| **1-C** | Motines, fosas, narcobloqueos, AEI y drones armados | **Un hallazgo** (fosa de Celaya) más dos candidatos no integrables |

### Verificación personal del coordinador — no delegada

Se aplicó la lección 3 de ARGOS 102: **una acusación de omisión contra una edición anterior no se
publica por reporte de un agente.** Cada candidato se contrastó con `grep` sobre **todo el archivo**
antes de darlo por omitido:

| Candidato | Resultado del `grep` sobre `reports/` | Veredicto |
|---|---|---|
| Iguala, Guerrero | **Cero coincidencias en ninguna edición** | **Omisión confirmada** |
| Estudiantes UV, Veracruz (`Melanie`, `Tlaltetela`) | **Cero coincidencias en ninguna edición** | **Omisión confirmada** |
| San Rafael / El Pital, Veracruz | **Cero coincidencias en ninguna edición** | **Omisión confirmada** |
| Fosa de Celaya, Guanajuato | Sin coincidencias en las ediciones 99-102; las menciones previas de "Celaya" son `ARG-95-002` y `ARG-98-003`, **dos asaltos carreteros, otro hecho** | **Omisión confirmada** |
| La Piedad, Michoacán, 15-ago (reportado por 1-B) | `ARG-98-002` **ya lo registra**, y ARGOS 98 cita **una URL de Infobae del mismo día 15-ago** para el mismo hecho de tres abatidos | **REFUTADO — no es omisión** |
| Zanatepec, Oaxaca (reportado por 1-A como caso límite) | `ARG-98-001` **ya lo registra** | **REFUTADO — no es omisión** |

**Dos de los seis candidatos eran señuelos, y ambos se cayeron por lectura directa del archivo, no
por criterio.** El de La Piedad es el más instructivo: el equipo lo trajo desde un *liveblog* de
Infobae fechado el 15-ago, y el hecho es del 14-ago y estaba publicado desde ARGOS 98 con esa misma
fuente y esa misma fecha de publicación. **Un liveblog fecha la página, no el hecho.**

### Comprobación de coherencia interna de las fuentes

Antes de aceptar las fechas, el coordinador verificó que **el día de la semana que declaran las
fuentes corresponda al calendario real**: las notas sitúan el hallazgo de los estudiantes la mañana
del **sábado 15**, el ataque de Iguala la madrugada del **domingo 16** y el de San Rafael la noche
del **domingo 16**. El calendario de 2026 confirma que el 15 de agosto fue sábado y el 16, domingo.
**Las fuentes son internamente coherentes**, lo que descarta que las fechas procedan del resumidor.

### Los cuatro eventos 🔴 que ninguna edición registró

| ARG-ID | Hecho | Fecha del hecho | Ventana | Color y razón |
|---|---|---|---|---|
| `ARG-103-REC-003` | **Iguala, Guerrero**, col. Primero de Mayo, calle Magnolias: ataque armado contra una vivienda con fusil AK-47 y arma corta. **Dos hombres muertos** (uno en el sitio, otro en hospital) y **una adolescente de 15 años herida**. Casquillos 7.62 y 9 mm | **16-ago, ~03:00 h** | **99** | 🔴 **víctimas múltiples** |
| `ARG-103-REC-004` | **Coatepec / Tlaltetela, Veracruz**: **Melanie Michelle Méndez Morales** (22) y **Luis Fernando Hernández Ibáñez**, estudiantes de Psicología de la Universidad Veracruzana, desaparecidos la noche del 14 tras salir de una cafetería en Xalapa, hallados con heridas de bala dentro de una camioneta cerca del puente Los Pescados | **15-ago** (hallazgo, mañana del sábado) | **99** | 🔴 **víctimas múltiples** |
| `ARG-103-REC-005` | **San Rafael, Veracruz**, comunidad **El Pital**: ataque armado **frente a una escuela primaria** durante una convivencia familiar. **Tres personas muertas**: Irma Lagunes y Jorge Cortés, originarios de Puebla, y Alfredo Bautista, de El Pital | **noche del 16-ago** | **100** | 🔴 **víctimas múltiples** |
| `ARG-103-REC-006` | **Celaya, Guanajuato**, entre las comunidades de **San Cayetano y La Soledad**: cuerpo semienterrado a menos de 20 cm de profundidad en terreno agrícola. **Una sola persona**, varón de ~17 años según dato pericial preliminar | **17-ago** | **101** | 🔴 **hallazgo de fosa clandestina** |

**Reserva declarada sobre `ARG-103-REC-006`**: las dos fuentes regionales que lo fechan
(`am.com.mx/celaya/2026/08/17/`, `periodicocorreo.com.mx/…/2026/aug/17/`) lo describen como
**"cuerpo semienterrado"**, mientras que las nacionales (`infobae.com/mexico/2026/08/18/`, Omnia)
lo titulan **"fosa clandestina"**. Se clasifica 🔴 por la enumeración de la metodología, que nombra
el hallazgo de fosas, **pero la discrepancia descriptiva se declara y no se resuelve**: es un solo
cuerpo, y así se reporta. **No se infiere pluralidad en ningún caso.**

**Corrección de ventana aplicada por el coordinador**: la primera ronda situó `ARG-103-REC-005` el
17-ago (ventana 101) y `ARG-103-REC-006` el 18-ago (ventana 101), en ambos casos por la **fecha de
publicación**. La ronda de corroboración localizó fuentes regionales que fechan **el hecho** un día
antes en los dos casos, lo que reasigna el primero a la **ventana 100** y confirma el segundo en la
**101**. Es la regla de `CLAUDE.md` operando: **la fecha de la URL fija la publicación, no el
hecho.**

### Candidatos que NO se integran, y por qué

| Candidato | Estado | Razón |
|---|---|---|
| **Tijuana, BC** — cuatro cuerpos en cajuelas de vehículos, zona Hipódromo, 17-ago | `NO INTEGRABLE` | Los hallazgos se produjeron en **puntos distintos a lo largo de ~8 horas**. Es compatible con una ejecución múltiple coordinada **y** con el descubrimiento en un mismo día de víctimas de hechos distintos. **Determinar cuál sería la fusión que el control existe para impedir.** Sin fuente institucional |
| **Jiutepec, Morelos** — ataque con dron contra una vivienda | `PENDIENTE DE ANCLA FECHADA` | La URL **no lleva fecha** y la hora "14:00 del 18-ago" procede **solo del resumidor**. Si fuera exacta, caería 23 minutos **después** del cierre de la ventana 101. No se integra a ningún total |
| **Cereso de Charo, Michoacán** — homicidio de "El Marino", 15-ago | `CLASIFICACIÓN EN DISPUTA` | Los medios iniciales lo llamaron **motín**; el gobernador de Michoacán lo **desmintió expresamente** el 17-ago y lo calificó de "ataque directo" de un interno con un arma calibre .25. **La autoridad niega la calificación que activaría el rojo.** Se reporta sin clasificar |

### Veredicto: el fallo es SISTEMÁTICO

**Cuatro eventos 🔴 nuevos, en tres entidades (Guerrero, Veracruz ×2, Guanajuato) y en las tres
ventanas auditadas.** Sumados a los dos que ARGOS 102 ya había localizado y a la reclasificación de
Colima, la serie 99-101 pasa de los **3 eventos rojos** que tenía registrados a **10**.

| Ventana | 🔴 registrados en su día | 🔴 localizados después | Efecto sobre su valoración |
|---|---|---|---|
| **ARGOS 99** | 3 (`ARG-99-001`, `-002`, `-003`) | **+2** (Iguala, estudiantes UV) | Su valoración **no se invierte**, pero se sostenía sobre **tres quintas partes** de sus rojos |
| **ARGOS 100** | **0** | **+2** (Cárdenas ya en 102, San Rafael hoy) | `NO DETERMINABLE` **falso**. Rectificada |
| **ARGOS 101** | **0** | **+3** (Tlapa y Colima ya en 102, Celaya hoy) | `NO DETERMINABLE` **falso**. Rectificada |

**La conclusión no admite matiz**: el fallo no fue puntual. Fue **el método**. Un barrido organizado
por entidad federativa pierde sistemáticamente los hechos de alto impacto de las entidades sin
corresponsalía sistemática en medios nacionales, y los pierde **aunque estén publicados con fecha en
la URL en medios de circulación nacional** — que es exactamente el caso de los cuatro.

**Las tres ediciones que declararon `NO DETERMINABLE` por ausencia de rojos medían su propia
cobertura, no el país.** Esa frase deja de ser una hipótesis de ARGOS 102 y pasa a ser un resultado
demostrado sobre tres ventanas consecutivas.

### Lo que el equipo 1-B aporta, precisamente por no haber encontrado nada

**Cero omisiones en el bloque de ataques contra autoridades.** No es un resultado menor ni un fracaso
del equipo: acota el fallo. Los ataques contra policías, militares y funcionarios **sí** se
publicaron y **sí** se recogieron, porque son el tipo de hecho que los medios nacionales cubren
siempre. **Lo que ARGOS pierde es la violencia contra civiles anónimos** —una familia, dos
estudiantes, tres personas en una convivencia, un cuerpo en un sembradío—, que se publica en medios
regionales y en los nacionales sin seguimiento. El sesgo de la cobertura de ARGOS **reproduce el
sesgo de la cobertura mediática**, y esa es la lección explotable de esta auditoría.

---

## Barrido regional — seis equipos, Ciclo C aplicado y declarado

### Rotación de cobertura — Ciclo C, con la excepción de Tlaxcala

`CLAUDE.md` fija un ciclo de tres ediciones: **A** (Noroeste + Centro) · **B** (Noreste + Golfo) ·
**C** (Occidente + Sureste). **A ARGOS 103 le correspondió el Ciclo C**, y así se ejecutó: Occidente
y Sureste gastaron sus primeras búsquedas en fiscalías y sentencias; Noroeste, Noreste, Golfo y
Centro encabezaron con armamento.

**Excepción aplicada, por la regla de prioridad sobre el ciclo**: **Tlaxcala** quedó `NO REVISADA` en
ARGOS 102 —única entidad del país en esa casilla— y encabezó el triaje del Centro **aunque no le
tocara por turno**. Saldar cobertura vence a mantener el turno.

**Resultado de la excepción: la deuda queda saldada.** Tlaxcala se consultó dos veces por portal
directo (`fgjtlaxcala.gob.mx`) y una vez por su señuelo documentado, y cierra en
`SIN RESULTADO INDEXADO EN VENTANA` — **una casilla escrita, no un silencio**. Es la diferencia
exacta que la metodología exige entre "no publicó" y "no se consultó".

**Rendimiento del Ciclo C, declarado sin adorno**: **ninguna de las dos regiones que encabezaron el
triaje judicial produjo una sentencia integrable**. Es la segunda edición consecutiva en que la
rotación no repite el resultado de ARGOS 101. Lo que sí produjo, otra vez, es de otra naturaleza:

- El **Sureste** **fechó por primera vez en cuatro ediciones** el caso de Playa del Carmen abierto
  desde ARGOS 99, mediante ancla externa (`24horasqroo.mx/2026/08/12/`, fecha en la ruta), con los
  tres nombres coincidiendo. **La fecha resultante —12-ago— lo sitúa fuera de toda ventana
  cubierta**, así que no se integra; pero rompe cuatro ediciones de vacío absoluto.
- El **Occidente** **arbitró la variante de Jalisco** y **localizó los dos dominios** que llevaban
  dos ediciones como `SIN DOMINIO CANÓNICO REGISTRADO`.

### Cobertura por región

| Región | Ciclo | Búsquedas | Entidades con barrido | Resultado |
|---|---|---|---|---|
| **Occidente** | **C — judicial** | 20/20 | 3 de 6 con barrido pleno | **Los dos hechos del corte.** Arbitraje de Jalisco. **Colima `NO REVISADA`** |
| **Sureste** | **C — judicial** | 20/20 | 6 de 6 | Cero en ventana. Playa del Carmen fechado |
| **Noroeste** | Armamento | 20/20 | 6 de 6 | Cero en ventana. **Cierra los 27 AEI de Sinaloa** |
| **Noreste** | Armamento | 20/20 | 5 de 5 | Cero integrable en ventana |
| **Centro** | Armamento *(Tlaxcala primero)* | **22/20 — TOPE EXCEDIDO** | 7 de 7 | Cero en ventana. **Tlaxcala saldada** |
| **Golfo** | Armamento | 20/20 | 2 de 2 | Un evento cualitativo. Cunduacán avanza |

**Incumplimiento declarado**: el equipo del **Centro gastó 22 búsquedas de 20** y **lo reportó él
mismo**, sin que el coordinador se lo preguntara, identificando cuáles fueron las dos que
excedieron. Se registra como **desviación de método, no como hallazgo ilegítimo**: los dos hallazgos
que produjeron esas búsquedas se conservan, marcados, porque retirarlos borraría información
verdadera para cuadrar un indicador — el mismo criterio que ARGOS 102 aplicó a las cuatro fiscalías
de `procedencia-cifras`. **Un tope excedido y declarado es un dato de auditoría; uno excedido y
callado sería un fallo de control.**

### Nueva deuda de cobertura que esta edición crea

**Colima queda `NO REVISADA`**: cero búsquedas dedicadas, por agotamiento del presupuesto de
Occidente antes de llegar a ella. Sustituye a Tlaxcala como la entidad que **encabeza el triaje de
ARGOS 104 por prioridad sobre el ciclo**. **Aguascalientes y Nayarit** recibieron solo arbitraje de
dominio, sin barrido de boletines: quedan en la misma casilla, en segundo orden.

### Ganancias para el directorio de dominios

Cuatro correcciones estructurales, todas incorporadas a `docs/dominios-oficiales.md`:

1. **Jalisco — variante arbitrada, deuda de dos ediciones cerrada.** `fiscalia.jalisco.gob.mx` es el
   canónico: devuelve contenido propio indexado y sus *slugs* llevan **fecha completa como sufijo**
   (`comunicado-1055-20260605`). `fiscaliadejusticia.jalisco.gob.mx` **no devolvió un solo resultado
   propio** en dos ediciones consecutivas y se descarta. **Sube de clase B a casi-A**: un resultado
   de búsqueda ya fecha el boletín sin ancla externa.
2. **Aguascalientes** — `fiscalia-aguascalientes.gob.mx` localizado, más `@fiscaliaAGS`. **Sin
   clasificar aún**: no alcanzó el presupuesto para verificar si sus boletines llevan fecha en ruta.
3. **Nayarit** — `fiscaliageneral.nayarit.gob.mx` localizado. Igualmente **sin clasificar**.
4. **Michoacán — matiz de subdominio que cambia el objetivo del barrido.** El que realmente indexa
   es **`comunicacion.fiscaliamichoacan.gob.mx`**, no el dominio raíz, y **sus *slugs* llevan fecha
   completa** (`20250116-…`). El directorio apuntaba al sitio equivocado.

Los puntos 2 y 3 **no saldan** la deuda: localizar un dominio no es clasificarlo. Se registran como
hallazgo parcial, y así constan.

### El vacío federal se amplía a dos días

`gob.mx/sspc/prensa` tiene indexado su último boletín el **18-ago**. **Ni el 19 ni el 20 aparecen
indexados**, confirmado de forma independiente por los equipos de Golfo y Centro. Con el vacío del
18-ago que ARGOS 102 dejó abierto, **son ya tres días consecutivos sin boletín federal localizable**
(18, 19 y 20 de agosto).

⚠️ **Reserva de método que hay que declarar**: el equipo del Centro **no pudo aplicar la regla de la
doble consulta** —por día suelto y por rango— por agotamiento de presupuesto. El de Golfo sí
consultó por fecha específica en dos ocasiones. Dado que **este emisor ya ha producido dos falsos
vacíos consecutivos** por alternar formato diario y agregado sin avisar, el vacío del 19 y 20 de
agosto se declara **`SIN RESULTADO INDEXADO EN VENTANA` con reserva expresa**, y **no** como vacío
constatado. La serie ya se equivocó dos veces dando por inexistente un boletín que existía.
---

## Auditoría retroactiva — correcciones y recuperaciones de esta edición

### Fes de erratas: las valoraciones de la serie 99-101 se rectifican en bloque

| ARG-ID | Edición afectada | Corrección |
|---|---|---|
| `ARG-103-FE-001` | **ARGOS 99** | **Omitió dos eventos 🔴 de su ventana**: el ataque a una vivienda en Iguala (16-ago, dos muertos y una adolescente herida) y el doble homicidio de dos estudiantes de la Universidad Veracruzana (15-ago). Su valoración **no se invierte** —registró tres rojos y sigue siendo determinable—, pero **se sostenía sobre tres quintas partes de los rojos de su ventana** |
| `ARG-103-FE-002` | **ARGOS 100** | **Omitió un segundo evento 🔴**: el ataque armado de El Pital, San Rafael, Veracruz (noche del 16-ago, tres muertos). Sumado al motín de Cárdenas que localizó ARGOS 102, su ventana tuvo **al menos dos rojos** frente a los **cero** que declaró. `NO DETERMINABLE` **confirmado como falso** |
| `ARG-103-FE-003` | **ARGOS 101** | **Omitió un tercer evento 🔴**: el hallazgo de un cuerpo semienterrado en Celaya (17-ago). Sumado a Tlapa y a la reclasificación de Colima, su ventana tuvo **al menos tres rojos** frente a los **cero** que declaró. `NO DETERMINABLE` **confirmado como falso** |

### Recuperaciones — dos pendientes mayores que cierran

| ARG-ID | Caso | Resultado |
|---|---|---|
| `ARG-103-REC-001` | **Los 27 AEI de la segunda línea de Sinaloa** — PRIORIDAD 1 heredada de ARGOS 102 | **CONTRADICCIÓN RESUELTA.** No eran dos lecturas del mismo renglón: son **dos entradas de Sinaloa en municipios distintos**. **Ahome** (8 cortas, 9 largas, 8 cargadores, 2 detenidos, ya registrado como `ARG-102-REC-006`) y **La Campana, Escuinapa** (1 arma larga, 13 cargadores, 1,389 cartuchos, **27 AEI**, 0 detenidos publicados). Verificado por el coordinador con `grep` sobre todo el archivo: **la única mención previa de "Escuinapa" está en ARGOS 91**, y es una línea de *exclusión* —"Escuinapa y Navolato, fuera de ventana"— de otro hecho. **El renglón de los 27 AEI no está registrado en ninguna edición** |
| `ARG-103-REC-002` | **Tijuana, col. Hipódromo** — cuatro cuerpos en cajuelas (17-ago) | **Gana fuente institucional**, que `_pendientes.md` daba por inexistente: declaración en video de la **Fiscal de Baja California** ("Encontramos un patrón: venían del mismo lugar los cuatro vehículos"). **No es un boletín**, es una declaración directa: confianza **Medio**. **El hecho sigue sin integrarse** — ver reserva abajo |

**Sobre `ARG-103-REC-001`, lo que sostiene el cierre y lo que no**: **el boletín no se leyó íntegro**
—ninguna edición lo ha hecho—. El cierre se apoya en **triangulación por municipio distinto entre dos
medios independientes** (*El Sol de Mazatlán* y *Meganoticias*, ambos nombrando Escuinapa), y
**Escuinapa es geográficamente incompatible con Ahome**, lo que descarta que sea la misma línea leída
dos veces. **Ninguna de las dos URLs lleva fecha en la ruta**; ambas atribuyen el hecho al operativo
del 17-ago del boletín federal, cuyo título sí va fechado. **Confianza: Medio.** Los 27 AEI
corresponden a la **ventana de ARGOS 101/102** y **no se integran al total de ARGOS 103**: elevan el
acumulado del periodo, no el del corte.

**Sobre `ARG-103-REC-002`, la reserva que se mantiene**: el hecho de Tijuana **sigue sin integrarse
como ficha roja**, y no por falta de fuente sino por una razón de método que la fuente nueva no
resuelve: los cuatro cuerpos aparecieron **en puntos distintos a lo largo de unas ocho horas**.
Determinar si es **una ejecución múltiple coordinada** o **el hallazgo en un mismo día de víctimas de
hechos distintos** exige un dato que nadie ha publicado. La declaración de la Fiscal sobre una "ruta
común" **apunta** a lo primero, pero **apuntar no es acreditar**: integrarlo como un evento único
sería exactamente la fusión que el control existe para impedir. Se mantiene `NO INTEGRABLE`, ahora
con fuente institucional.

### Seguimientos judiciales que avanzan sin cerrar

| ARG-ID | Caso | Avance de esta edición |
|---|---|---|
| `ARG-103-SEG-001` | **QRoo — Playa del Carmen**, 50 años a tres personas | **Fechado por primera vez tras cuatro ediciones**: `24horasqroo.mx/2026/08/12/50-anos-prision-4/`, fecha en la ruta, con los tres nombres coincidiendo. **Consecuencia inesperada: la fecha lo saca de todas las ventanas cubiertas** (12-ago). Sigue sin boletín de `fgeqroo.gob.mx` y sin fuente oficial: `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL` |
| `ARG-103-SEG-002` | **Tabasco — Cunduacán**, Miguel "N" | **Delito confirmado por primera vez: violación** — antes constaba sin especificar. Se mantienen los 8 años, la reparación del daño y la suspensión de derechos políticos. Ancla: `novedadesdetabasco.com.mx/2026/08/15/`, **fecha en la ruta pero medio regional**. **Dos señuelos deslindados**: no es el boletín de extorsión de 10 años (`/Boletin/Index/37454`) ni el tercer caso de ~24-mar-2026. Sigue `PENDIENTE DE CONFIRMACIÓN OFICIAL` |

### Contradicción nueva que esta edición abre y no puede arbitrar

**Las 84 UMA de Tlaxcala.** ARGOS 102 atribuyó **84 UMA + 2 años 6 meses** a **Luis "N"** (Huamantla,
portación de arma). El barrido del Centro, sobre la misma serie de boletines de FGR-Tlaxcala,
encuentra el resumidor atribuyendo las **84 UMA a "Marvin 'N'"**, sin multa para Luis "N".

**No se arbitra, y la razón es la que importa**: ambas lecturas dependen del **resumidor del
buscador**, que parafrasea, y **ninguna de las URLs de esa serie lleva fecha ni permite lectura
directa**. Arbitrar entre dos paráfrasis del mismo sintetizador no produciría un dato mejor: produciría
una elección disfrazada de verificación. Queda **`CONTRADICHA — REQUIERE LECTURA DIRECTA`** hasta que
cambie la política de egreso.
---

## Módulo de sentencias — indicador de cobertura obligatorio

**Resultado del corte: cero sentencias integrables al conteo nacional.** Es la segunda edición
consecutiva sin sentencia integrable, y la segunda en que el triaje judicial rotado no produce una.

| Indicador | Valor |
|---|---|
| **Fiscalías con barrido de boletines ejecutado** | **28 de 32** |
| **FGR revisada** | **Sí** — vía FGR-Tlaxcala, FGR Cancún y FGR Nayarit; ningún resultado con ancla fechada en ventana |
| **Fiscalías con sentencia publicada dentro de la ventana** | **0** |
| **Fiscalías `SIN RESULTADO INDEXADO EN VENTANA`** | **28** |
| **Fiscalías `NO REVISADA`** | **3** — Colima (cero búsquedas), Aguascalientes y Nayarit (solo arbitraje de dominio, sin barrido de boletines) |
| **Excluida por decisión de método documentada** | **1** — Nuevo León: `fiscalianl.gob.mx` es un portal de servicios **sin sala de prensa indexable**; comunica por Facebook y X. Se cubrió por medios regionales. **No es un vacío del territorio y no se cuenta como no revisada por descuido** |
| **Páginas no disponibles** | **0** — bajo bloqueo de egreso no se intenta `WebFetch`, así que ningún portal devuelve "no disponible" en sentido estricto |
| **Portales leídos por acceso directo** | **0 de ~128** |

**La cobertura declarada no excede la verificada**: ninguna de las 28 se cierra en
`SIN ACTUALIZACIÓN CONSTATADA`, casilla que exige lectura directa del listado y que el bloqueo de
egreso hace imposible en todas.

### Candidatos judiciales examinados y por qué ninguno entra

| Caso | Entidad | Motivo de exclusión |
|---|---|---|
| Jorge Fernando "N", cohecho, 4 a 6 m, **sentencia firme** | Guanajuato | Publicación **3-4 ago** — fuera de ventana |
| "51 vinculados y 36 sentenciadas" por extorsión | Guanajuato | **Agregado sin desglose nominal** y boletín del 17-ago. No integrable ni aunque cayera en ventana |
| "34 años 9 meses" por delitos contra la libertad | Aguascalientes | **Sin URL ni fecha** — `PENDIENTE DE ANCLA FECHADA` |
| Portación de arma, "fallo condenatorio" | Nayarit | Publicación **6-ago** (`nayaritnoticias.com/2026/08/06/`) — fuera de ventana |
| Josué "N", robo de vehículo con violencia | Querétaro | Publicación **17-ago** — fuera de ventana |
| Paola Alejandra "N", homicidio culposo, 4 a 11 m | Querétaro | Publicación 4-ago y **ya integrada en ARGOS 102** — no se duplica |
| Secuestro agravado, 80 años · y 50 años | Puebla | Publicaciones 6-ago y jul-2026 — fuera de ventana; la segunda es de la **familia de firmeza** ya señalada como vivero de confusión |
| Fraude `CS2026-259` (Strategic Capital Agency) | CDMX | Publicación **7-ago** — fuera de ventana |
| Serie FGR-Tlaxcala: Elvis, Carlos, Juan, Marvin y Luis "N" | Tlaxcala | **Cinco boletines casi idénticos, ninguno con fecha en URL.** Las fechas las atribuye el resumidor (4 a 18-ago); **incluso la más tardía cae antes de la apertura de la ventana** |
| Lucila C.G., robo con violencia, 9 a 9 m | Oaxaca | Publicación **11-ago** — fuera de ventana |
| `DPE/3611/2026`, portación de arma, 6 años | QRoo (FGR) | Citado por el resumidor con fecha 19-ago, pero **`fgr.org.mx` es clase C sin fecha en ruta y no se localizó URL propia**. `PENDIENTE DE ANCLA FECHADA` |
| Fallo condenatorio, 100 años a seis personas, secuestro agravado | Zacatecas | **Segunda edición sin ancla externa.** El término va en el *slug* institucional, pero la URL no lleva fecha y `ljz.mx` no devolvió nada. Hecho de **ago-2021**: riesgo alto de trampa de aniversario. `NO ASIGNABLE A NINGUNA VENTANA` |

**Todos los candidatos con término jurídico expreso quedaron fuera por fecha, no por calificación
jurídica.** No es una edición en la que las fiscalías no publicaran sentencias: es una en la que
ninguna de las que publicaron cae dentro de una ventana de 24.5 horas, y en la que **la mayoría de
los portales no permite fechar lo que publica**. La escasez es del método de fechado disponible bajo
bloqueo, y así debe leerse.
---

## Los hechos de la ventana

Tres fichas. **Dos de ellas son las dos caras del mismo suceso** —una acción del Estado y la
respuesta armada que provocó— y por eso van separadas, conforme a la regla de que un delito y la
respuesta institucional son dos eventos con dos ARG-ID.

### ARG-103-001 — Narcobloqueos, quema de vehículos y agresión armada contra la Guardia Nacional, Michoacán (🔴 ROJO)

**Hecho confirmado.** Tras el operativo federal contra Heraclio "N", alias **"El Tío Lako"**,
señalado como jefe regional del CJNG, grupos criminales responden con **bloqueos carreteros y quema
de vehículos en múltiples municipios de Michoacán**. La Presidenta confirmó el operativo en la
conferencia matutina; el gobernador Alfredo Ramírez Bedolla informó del despliegue de SEDENA y
Guardia Nacional.

**Cifra de bloqueos: CONTRADICHA — se reportan todas las lecturas, no se funden ni se promedian.**

| Cifra | Fuente |
|---|---|
| **24 puntos**, reporte del **C5 estatal a las 08:30 h** | `nmas.com.mx`, `tribunadelabahia.com.mx` |
| **"más de 20 puntos"** | Quadratín (C5), Infobae |
| **11 bloqueos** | LatinUS, `tribunadelabahia.com.mx` (segundo artículo, cifra distinta del mismo portal) |
| **"al menos ocho carreteras"** | Diario de Morelos |

**Ninguna fuente institucional escrita fija una cifra única.** El listado de municipios también varía
entre fuentes —Zamora, Tangancícuaro, Tzintzuntzan, Coeneo, Zacapu, La Piedad, Numarán, Chilchota,
Ecuandureo, Churintzio, Purépero, Pátzcuaro, Tanhuato, Yurécuaro— y **no existe un listado
institucional único**: se reportan las variantes sin fusionarlas.

**Corroboración.** Siete fuentes **fechadas por la propia URL** —seis con la fecha en la ruta y una (`informador.mx`) en el *slug*—: `infobae.com/mexico/2026/08/19/` ·
`elfinanciero.com.mx/estados/2026/08/19/` · `jornada.com.mx/noticia/2026/08/19/estados/` ·
`informador.mx/…20260819-0070.html` · `changoonga.com/2026/08/19/` · `adn40.mx/mexico/2026-08-19/` ·
`redmichoacan.com/2026/08/19/`. Institucional **verbal, no escrita**: Presidencia y gobierno de
Michoacán. **No se localizó comunicado escrito** de SSPC, Gabinete de Seguridad o Guardia Nacional
con el número de bloqueos: `SIN RESULTADO INDEXADO EN VENTANA`.

**⚠️ CIFRA DE VÍCTIMAS RETIRADA POR CONTAMINACIÓN CRUZADA — y es el hallazgo de método del corte.**
Una cadena de portales (Meganoticias, Enlace Noticias24, Contramuro) atribuye a este hecho **"cinco
civiles muertos"** en conteo preliminar. **Esa cifra no es de este hecho**: pertenece a
`ARG-102-002` —Los Reyes, Los Palillos, **18-ago**, cinco presuntos agresores abatidos—, ya publicado
por ARGOS 102. El equipo de verificación lo detectó y **el coordinador lo comprobó personalmente**
contra el archivo: la nota de Quadratín sitúa su operativo "a las 12 horas del **martes** anterior",
y **el 18 de agosto de 2026 fue martes**. **La cifra queda excluida.** Este corte **no publica
víctimas mortales** para `ARG-103-001`.

**Frontera de ventana.** Un indicio sitúa las primeras quemas en Zamora **hacia las 06:00 h**, antes
de que abra la ventana (07:45); pero ese dato procede **del resumidor, sin fragmento literal**, y la
regla prohíbe inferir la hora. En cambio, **el reporte del C5 de 24 puntos a las 08:30 h cae
demostrablemente dentro de la ventana**. Se marca
`FRONTERA DE VENTANA — HORA DE ORIGEN NO FIJADA CON CERTEZA`, y se integra a esta edición: **es la
primera que lo ve**, y ARGOS 102 cerró a las 07:45 sin él.

**Explotación ARGOS.** El patrón es el de **represalia territorial contra la captura de un mando
regional**: no busca recuperar al detenido, sino imponer un coste visible y simultáneo en la red
carretera de varios municipios. Su valor de inteligencia no está en los bloqueos sino en **el mapa
que dibujan**: los municipios afectados —el corredor Zamora–La Piedad–Ecuandureo–Tanhuato más el
eje Zacapu–Pátzcuaro— acotan el **área de control efectivo de la célula**, y esa lectura sí es
explotable aunque la cifra exacta esté contradicha. **Líneas a explotar**: si la capacidad de
bloqueo simultáneo se corresponde con el corredor donde se ejecutó el aseguramiento; si el
armamento especial incautado —calibre .50, Minimi, lanzagranadas— indica una célula de contención
territorial y no de trasiego; y **por qué el emisor federal no ha publicado nada por escrito sobre
un evento de esta magnitud** tres días después. **Vacío principal**: ninguna autoridad ha publicado
un saldo, ni de víctimas ni de detenidos por los bloqueos.

**Trazabilidad**: `ARG-103-001` · 🔴 ROJO · Confianza **★★★★☆** · Institucional (verbal) / Nacional /
Regional · Consulta: 2026-08-20, 08:16 CDMX.

### ARG-103-002 — Operativo federal contra célula del CJNG, Tanhuato y Ecuandureo, Michoacán (🟢 VERDE)

**Hecho confirmado.** Operativo **único y coordinado** —no dos hechos— en las localidades de
**Tinaja de Vargas (Tanhuato)** y **El Colesio (Ecuandureo)**, por Ejército, Guardia Nacional, SSPC,
FGR y Marina, derivado de trabajos de inteligencia militar. **12 personas detenidas** (9 en el
despliegue inicial y 3 posteriores del mismo operativo), entre ellas **la hija y la pareja** del
objetivo. **64 vehículos**, 2 inmuebles, equipo táctico y un dron asegurados.

**Deduplicación resuelta expresamente**: los 12 detenidos son **9 + 3 del mismo despliegue**, no dos
eventos independientes; se cuenta **un solo evento de aseguramiento**, y los detenidos **no se suman
entre fichas**.

**Corroboración.** `infobae.com/mexico/2026/08/20/` (12 detenidos) ·
`infobae.com/mexico/2026/08/19/` (declaración del gobernador, 9 detenidos) ·
`proyectopuente.com.mx/2026/08/19/` (64 vehículos en el titular) · `redmichoacan.com/2026/08/19/` ·
MiMorelia · La Voz de Michoacán · El Heraldo de México. **Sin comunicado institucional indexado**:
`site:gob.mx/sedena`, `site:gob.mx/guardianacional` y `site:gob.mx/sspc` no devolvieron nada sobre
Tanhuato, Ecuandureo ni el objetivo. Casilla: `SIN RESULTADO INDEXADO EN VENTANA`.

**⚠️ RESERVA DE COLOR, DECLARADA Y NO RESUELTA.** Tres portales regionales (Meganoticias, Enlace
Noticias24, Contramuro) reportan **agresión armada de civiles contra la Guardia Nacional en Tanhuato
y Yurécuaro**. **No se pudo determinar si esa agresión ocurrió durante la ejecución del cateo o si
forma parte de la reacción de bloqueos** ya recogida en `ARG-103-001`. Las notas centradas en el
operativo describen aseguramiento **sin relatar intercambio de disparos en el punto de la captura**.

Se resuelve así, y se explica por qué: la ficha del operativo se clasifica **🟢 VERDE** —captura y
aseguramiento, sin confrontación acreditada en el sitio—, y **la agresión queda recogida dentro de
`ARG-103-001`, que es 🔴**. Con eso, **la agresión no desaparece del semáforo**, que es exactamente
lo que la regla de "un delito y su detención son dos eventos" existe para impedir. **Si aparece una
fuente que sitúe la agresión en el punto de la captura, esta ficha pasa a 🟡 por fe de erratas.**

**Explotación ARGOS.** Lo relevante no es el número de detenidos sino **la composición del
armamento**: una ametralladora **calibre .50**, cuatro **Minimi 5.56 mm** y dos **lanzagranadas
acoplados** no son armamento de escolta ni de trasiego, sino **de contención territorial** —diseñado
para negar el acceso a una zona—. Sumado a los **64 vehículos** y a los **8 AEI**, el conjunto
sugiere una célula con función de **control de corredor**, no de distribución. **Requiere
validación**: ninguna autoridad ha publicado la adscripción de la célula ni el destino del
armamento.

**Trazabilidad**: `ARG-103-002` · 🟢 VERDE *(con reserva de color declarada)* · Confianza
**★★★★☆** para detenidos y vehículos, **★★★☆☆** para el desglose de armamento · Institucional
(verbal, vía gobernador) / Nacional / Regional · Consulta: 2026-08-20, 08:16 CDMX.

### ARG-103-003 — Operativo de seguridad en varios municipios, Veracruz (🟢 VERDE)

**Hecho confirmado.** La SSP de Veracruz, en coordinación con Guardia Nacional, Ejército y Marina,
informa **21 personas detenidas** y 174 dosis de sustancias ilícitas aseguradas en operativos en
Poza Rica, Álamo, Misantla y otros municipios. **Dos de las 21 detenciones fueron por posesión ilegal
de arma de fuego**; el resto, por narcomenudeo y robo. Armamento publicado: **2 armas cortas y 1
réplica**.

**Marca de periodo**: `Evento anterior publicado durante el corte` — el hecho es del **17-18 de
agosto** y la publicación del **19**. No se mezcla con los hechos de la ventana.

**Corroboración.** Institucional con **fecha en la ruta**:
`veracruz.gob.mx/2026/08/19/fuerzas-de-seguridad-detienen-a-21-personas-y-aseguran-174-dosis-de-presuntas-sustancias-ilicitas/`.
**Fuente institucional única**: `Pendiente de corroboración independiente.`

**La réplica no se cuenta como arma.** Se reporta porque la autoridad la publicó, pero **no integra
el total de armas cortas**: una réplica no es un arma de fuego y sumarla inflaría el conteo nacional.

**Trazabilidad**: `ARG-103-003` · 🟢 VERDE · Confianza **★★★☆☆** · Institucional · Consulta:
2026-08-20, 08:16 CDMX.

### Hechos examinados que NO reciben ficha

| Hecho | Entidad | Razón |
|---|---|---|
| **Coatzacoalcos** — disparan diez veces contra un guardia, que resulta ileso (19-ago, fecha en ruta) | Veracruz | **Fuente única y ambigüedad de sujeto**: la nota no precisa si el blanco es autoridad o seguridad privada. Sin eso, el color no es asignable. `Pendiente de corroboración independiente.` |
| **Jardines de Escobedo** — ataque armado en un partido de futbol (19-ago) | Nuevo León | Ataque dirigido a un civil, **sin confrontación con autoridad y sin vínculo acreditado con crimen organizado**; la fuente no reporta fallecidos. No clasificable sin ese dato |
| **Jiutepec** — ataque con dron y explosivos contra una vivienda | Morelos | `PENDIENTE DE ANCLA FECHADA`, **segunda edición**. La URL no lleva fecha y la hora procede del resumidor. Si se fechara dentro de ventana sería 🔴 por uso de drones armados |
| **Detención de Fausto Ernesto Corrales Rodríguez** | CDMX | **Sin URL verificable**: solo lo afirma el resumidor. No se integra ni como candidato |
---

## Módulo de armamento — conteo nacional del corte

**Dos eventos contabilizados, en dos entidades.**

| ARG-ID | Entidad · Municipio | Fecha del hecho | Cortas | Largas | Cartuchos | Cargadores | Granadas | AEI | Explosivos | Detenidos | Corporación | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ARG-103-ARM-001` | Michoacán · Tanhuato y Ecuandureo | 19-ago | **1** | **9** | s/c | s/c | 0 | **8** | 0 | **12** | Ejército, GN, SSPC, FGR, Marina | **Medio** |
| `ARG-103-ARM-002` | Veracruz · Poza Rica, Álamo, Misantla y otros | 17-18 ago | **2** | 0 | s/c | s/c | 0 | 0 | 0 | **2** | SSP Veracruz + GN, Ejército, Marina | **Medio** |

`s/c` = mencionados por la fuente **sin cifra**. **No se integran a ningún total y no se infieren.**

### Total nacional del corte

| Categoría | Total | Nota |
|---|---|---|
| **Armas cortas** | **3** | 1 Michoacán + 2 Veracruz. **La réplica de Veracruz no se cuenta** |
| **Armas largas** | **9** | Todas en Michoacán |
| **Armamento especial** | **7 piezas** | 1 ametralladora **calibre .50**, 4 **Minimi 5.56 mm**, 2 **lanzagranadas acoplados** |
| **AEI** | **8** | Todos en Michoacán |
| **Cartuchos** | `CANTIDAD NO DETERMINADA` | Mencionados en ambos eventos sin cifra |
| **Cargadores** | `CANTIDAD NO DETERMINADA` | Ídem. **Nunca se suman con los cartuchos** |
| **Granadas** | **0** | |
| **Explosivos y componentes** | **0** | |
| **Drones armados** | **0** | Se aseguró **un dron** en Michoacán, **sin que ninguna fuente lo describa como armado**. No se cuenta como dron armado |
| **Personas detenidas en eventos con aseguramiento** | **14** | 12 + 2. No se suman entre fichas |
| **Estados con aseguramientos** | **2** | Michoacán, Veracruz |
| **Eventos contabilizados** | **2** | |
| **Eventos cualitativos sin cantidad** | **2** | Cartuchos y cargadores, en los dos eventos |

**⚠️ Reserva de conteo sobre el armamento especial — no se suma a las armas largas.** La taxonomía de
`CLAUDE.md` sitúa las ametralladoras entre las **armas largas** y las **ametralladoras pesadas y de
calibre .50** entre el **armamento especial**. Las fuentes publican "9 armas largas" **y**, por
separado, el calibre .50, las Minimi y los lanzagranadas, **sin precisar si estas piezas están
incluidas dentro de las nueve**. Sumarlas daría 16 y **podría estar contando dos veces las mismas
armas**. Se publican **las dos cifras por separado, tal como las publica la fuente**, y el total
nacional de armas largas se mantiene en **9**. `NO DETERMINABLE SI EL ARMAMENTO ESPECIAL ESTÁ
COMPRENDIDO EN LAS NUEVE LARGAS`.

**Cálculo propio declarado**: los totales de esta tabla son **suma de ARGOS** sobre cifras publicadas
por las fuentes. **Ninguna autoridad publicó un agregado nacional** para este periodo, así que el
agregado es de ARGOS y se dice.

### Lectura regional

| Región | Eventos | Lectura |
|---|---|---|
| **Occidente** | 1 | **Concentra la totalidad del armamento del corte**, incluido todo el armamento especial y los 8 AEI |
| **Golfo** | 1 | Dos armas cortas en un operativo de 21 detenciones mayoritariamente por narcomenudeo |
| Noroeste · Noreste · Centro · Sureste | **0** | `SIN RESULTADO INDEXADO EN VENTANA` en las cuatro. **No es ausencia constatada de hechos** |

**Advertencia obligatoria sobre los cuatro ceros regionales.** La auditoría de PRIORIDAD 1 de esta
misma edición demostró que **un cero regional es una hipótesis, no un dato**, y que tres ediciones
consecutivas convirtieron ceros de este tipo en valoraciones nacionales falsas. Los cuatro ceros de
hoy se publican **con esa advertencia expresa** y no sostienen ninguna afirmación sobre el
territorio.

**Explotación ARGOS del módulo.** El corte no permite lecturas de tendencia —dos eventos son
demasiado pocos—, pero sí una observación cualitativa: **todo el armamento de alto poder del periodo
está en un solo corredor de un solo estado**, y corresponde a una sola célula. El calibre .50, las
Minimi y los lanzagranadas acoplados son consistentes con **capacidad de negación de área**, no con
protección de cargamento; los 8 AEI, con **manufactura local**. Es consistente con lo observado en
El Rosario y La Piedad en el periodo anterior, y **refuerza la hipótesis —no confirmada— de un
patrón de fortificación territorial en el occidente de Michoacán**. Requiere validación con
comunicados institucionales que hoy no existen.
---

## Presupuesto de búsqueda

| Equipo | Tope | Consumo | Nota |
|---|---|---|---|
| PRIORIDAD 1 — 1-A · masacres y homicidios múltiples | 12 | **12** | Ejecutado **primero y en solitario**. Tres hallazgos |
| PRIORIDAD 1 — 1-B · ataques contra autoridades | 12 | **12** | Ídem. **Cero hallazgos** — y el cero acota el fallo |
| PRIORIDAD 1 — 1-C · motines, fosas, AEI | 12 | **12** | Ídem. Un hallazgo |
| PRIORIDAD 1 — corroboración de los cuatro hallazgos | 12 | **12** | Segunda ronda. Corrigió **dos ventanas** |
| Verificación del único rojo de la ventana | 14 | **14** | **Detectó la contaminación cruzada de la cifra de víctimas** |
| Barrido Noroeste | 20 | 20 | Tope alcanzado. **Cierra los 27 AEI** |
| Barrido Noreste | 20 | 20 | Tope alcanzado |
| Barrido Occidente *(Ciclo C — triaje judicial)* | 20 | 20 | Tope alcanzado |
| Barrido Centro *(Tlaxcala primero)* | 20 | **22** | ⚠️ **TOPE EXCEDIDO EN 2 — declarado por el propio equipo** |
| Barrido Golfo | 20 | 20 | Tope alcanzado |
| Barrido Sureste *(Ciclo C — triaje judicial)* | 20 | 20 | Tope alcanzado |
| Coordinación | — | **0** | Sonda de egreso por `curl` y **seis verificaciones directas del archivo con `grep`**: sin consumo de búsqueda |
| **Total** | **182 asignadas** | **184 de un techo de 200** | **10 de 11 topes respetados** |

**Se rompe la racha de dos ediciones con los topes íntegros**, y se dice. El exceso es de dos
búsquedas sobre 182, lo detectó y lo declaró el propio equipo sin que se le preguntara, y sus dos
hallazgos se conservan marcados. **Un tope excedido y declarado es un dato de auditoría; uno
excedido y callado sería un fallo de control.**

**Cuatro de los once equipos —48 de las 184 búsquedas, el 26 % del presupuesto— se dedicaron a
auditar a ARGOS, no a cubrir el país.** Fue la decisión correcta y el resultado la justifica, pero tiene un coste que hay que
declarar: **Colima quedó sin revisar** y el módulo de sentencias cerró en cero.

---

## Valoración del corte

### Nivel de Riesgo Nacional ARGOS: DETERMINABLE, por primera vez en cuatro ediciones

**Y no porque el país haya cambiado, sino porque el instrumento por fin ve.**

La ventana registra **un evento 🔴** —los narcobloqueos de Michoacán— y es, además, **el mejor
documentado de la serie reciente**: siete fuentes con fecha en la ruta, dos autoridades confirmándolo
verbalmente y ★★★★☆. Frente a `ARG-102-002`, que se sostenía en dos medios regionales, la diferencia
de calidad probatoria es de otra escala.

**Valoración: riesgo ALTO y TERRITORIALMENTE CONCENTRADO.** El hecho rojo del corte es una
**represalia coordinada contra una acción del Estado**, ejecutada de forma simultánea en más de una
decena de municipios de **un solo estado**. Es un indicador de **capacidad de respuesta armada
organizada** —no de deterioro nacional generalizado—, y así debe leerse: el resto del país no
registra eventos rojos en esta ventana, **con la advertencia de que esa ausencia es exactamente el
tipo de dato que esta misma edición acaba de demostrar que ARGOS mide mal**.

**Las dos acciones verdes no reducen el nivel**: se reportan como capacidad institucional. El
operativo que detonó los bloqueos es, de hecho, la acción institucional de mayor calibre del periodo
—12 detenidos y armamento de contención territorial—, y **el bloqueo es la medida del coste que el
Estado impuso**, no un fracaso suyo.

### Advertencia obligatoria de comparabilidad

Los totales de este corte **no son comparables sin más** con los de ediciones anteriores, por dos
razones que se declaran juntas:

1. **La ventana dura 24.5 h** frente a las ~19 h de ARGOS 102 y las ~35 h de ARGOS 101.
2. **La auditoría de esta edición demuestra que los totales de rojos de ARGOS 99, 100 y 101 estaban
   incompletos**, y en dos casos eran falsos. **Cualquier serie temporal construida sobre las
   valoraciones de esa ventana está viciada** mientras no se reconstruya con las diez rojas
   conocidas hoy.

---

## Lecciones de método de esta edición

1. **Invertir el eje del barrido encuentra lo que el barrido pierde.** Consultar **por tipo de hecho
   y no por entidad** produjo cuatro eventos rojos que tres ediciones no vieron, con 36 búsquedas.
   No fue una mejora incremental de cobertura: **fue el hallazgo que redefine la serie**. Debe
   incorporarse como fase permanente, no como auditoría extraordinaria.
2. **El cero de un equipo puede valer tanto como el hallazgo de otro.** El equipo 1-B no encontró
   nada, y ese cero **acotó el diagnóstico**: los ataques contra autoridades sí se recogen; lo que
   ARGOS pierde es la violencia contra civiles anónimos. **Un cero bien documentado es un resultado,
   no un fracaso.**
3. **Verificar personalmente contra el archivo sigue siendo indispensable, y hoy tumbó dos
   acusaciones de seis.** La Piedad y Zanatepec llegaron como omisiones y **ya estaban publicadas**.
   Ninguna edición debe publicar una acusación contra otra por reporte de un agente.
4. **Un *liveblog* fecha la página, no el hecho.** Produjo un falso hallazgo en la auditoría y estuvo
   a punto de producir una cifra de cinco muertos falsa en el hecho principal del corte. **Ambas
   veces la fuente era el mismo tipo de página.** Debe tratarse como fuente de clase propia.
5. **La contaminación cruzada entre hechos vecinos es un riesgo real y detectable.** Cinco muertos de
   un hecho del 18-ago estuvieron a punto de atribuirse a otro del 19-ago, en el mismo estado y con
   el mismo actor. Lo que lo impidió fue **comprobar el día de la semana**: la fuente decía "martes",
   y el 18 fue martes. **Verificar la coherencia interna de una fuente cuesta cero búsquedas.**
6. **Declarar el propio incumplimiento vale más que un indicador limpio.** El equipo del Centro
   reportó su exceso sin que se le preguntara. Esa conducta es la que hace auditable al producto, y
   se registra como tal, no como falta.
7. **Publicar dos cifras contradictorias es más honesto que elegir una.** Los bloqueos van con cuatro
   cifras distintas y el armamento especial sin sumarse a las armas largas. **Un total limpio que
   oculta una duda es peor producto que un total con reserva.**
---

## Control editorial antes de publicar — los tres controles obligatorios

Los tres se ejecutaron. **Los agentes de control no resuelven por nombre** —su definición llega con
el `git merge --ff-only` de arranque, después de que la sesión tome su registro—, así que se lanzaron
como `general-purpose` **indicándoles que leyeran primero su archivo en `.claude/agents/`**. Funciona
y no degrada el resultado: ambos controles devolvieron hallazgos reales, y uno de ellos detectó una
regresión que el redactor no vio.

### 1 · `barrido-regional` ×6 — ejecutado

Seis equipos regionales en paralelo, condición previa para que cualquier módulo pueda declarar un
vacío. Resultados y cobertura, arriba.

### 2 · `editor-duplicidad` — `CORREGIR ANTES DE PUBLICAR` · **corregido**

**Hallazgo aceptado, y era una regresión del redactor.** El borrador incluía en la página 2 un bloque
**"ARGOS ALERTA"** y una tabla de **"EVENTOS PRIORITARIOS DEL CORTE"**. `CLAUDE.md` los **retiró
expresamente** de la estructura del reporte —"No incluye un bloque 'ARGOS ALERTA' ni una tabla
adicional de 'eventos prioritarios': ambos repetían el mismo hecho de mayor gravedad ya resumido en
'Ejes del día' y desarrollado en su ficha completa"—, y el control verificó que **ninguna de las tres
ediciones anteriores los trae**. Con ellos, `ARG-103-001/002/003` aparecían en **cuatro lugares** en
vez de los dos que fija la regla de no duplicación.

**Corrección aplicada**: ambos bloques **eliminados** del cartelón y de la móvil, que se regeneró.
La página 2 queda con lo que la estructura prescribe: **resumen ejecutivo y detenciones relevantes**.

**Por qué se acepta esta vez sin discutir el remedio**: a diferencia del caso de ARGOS 102 —donde el
control propuso recortar una cifra verdadera para cuadrar un indicador y el redactor tuvo razón al no
aceptarlo—, aquí **eliminar no borra ninguna información**: todo el contenido de los dos bloques
subsiste en las fichas y en las páginas 7 y 8. Se elimina redundancia, no dato.

**Lección para el redactor, y es incómoda**: la regresión se produjo porque el coordinador siguió una
descripción **desactualizada** de la estructura del reporte en vez de la del repositorio. **El archivo
del repositorio es el que manda**, y ese principio es justo el que ARGOS predica para las fuentes.

**Lo que el control declaró limpio**: la separación deliberada de `ARG-103-001` y `ARG-103-002` en dos
fichas —verificó que detenidos y armamento constan **solo** en la segunda y que la agresión a la GN no
se contabiliza dos veces—; el deslinde de `ARG-103-REC-001` (Escuinapa) frente a `ARG-102-REC-006`
(Ahome); las cuatro acusaciones de omisión, que **reverificó con `grep` por su cuenta** con el mismo
resultado que el coordinador; y la **paridad escritorio/móvil**.

### 3 · `procedencia-cifras` — un `CORREGIR ANTES DE PUBLICAR` · **corregido**

**Hallazgo aceptado**: el borrador afirmaba que *"cuatro equipos —el 38 % del presupuesto— se
dedicaron a auditar a ARGOS"*. **Ninguna operación reproduce ese 38 %**: los cuatro equipos de
auditoría consumieron **48 búsquedas**, que son el **26 %** de las 184 del corte; la fracción de
*equipos* sería 4 de 11, un 36 %. **Era una cifra derivada mal calculada y presentada sin declarar la
operación** — exactamente el fallo que este control existe para atrapar.

**Corrección aplicada**: se sustituye por **"48 de las 184 búsquedas, el 26 %"**, con la operación a
la vista.

**Dos observaciones también aceptadas**:

1. Al reutilizar los **303 AEI de El Rosario** y los **9 de La Piedad** como comparación cualitativa,
   el borrador no repetía la **reserva de origen** de la segunda cifra. Se añaden **los ARG-ID de
   procedencia** y la reserva literal `confirmados por concordancia de frase, documento no leído
   íntegro`. Ninguna de las dos cifras entra en ningún total de este corte.
2. La cifra contaminada no solo cambió de hecho: **cambió de sujeto**. Lo que en el archivo son
   *cinco presuntos agresores abatidos* reaparece en los portales como *cinco civiles muertos*. Se
   añade esa precisión a la ficha, porque **la mutación del sujeto es más grave que la del número**.

**Lo que el control recalculó y declaró limpio**: el total nacional de armamento (3 cortas · 9 largas ·
7 piezas especiales · 8 AEI · 14 detenidos), con la réplica **no sumada** y el armamento especial
**no sumado** a las largas; la deduplicación de detenidos (12 + 2 = 14, con las 19 restantes ni
duplicadas ni desaparecidas); las cuatro cifras de bloqueos, ninguna presentada como oficial; el
presupuesto (182 asignadas, 184 consumidas de 200); el indicador de cobertura (28 + 3 + 1 = 32); la
reconstrucción **de 3 rojos a 10**, verificada evento por evento contra ARGOS 101 y 102; y el
tratamiento del indicador SESNSP heredado.

Verificó además que **ninguna cifra del cartelón procede solo del resumidor del buscador**: los tres
casos que dependían de él —la hora de las 06:00 de Zamora, el "14:00" de Jiutepec y la fecha del
`DPE/3611/2026` de QRoo— están marcados y **excluidos de todos los totales**.

### Balance de los controles

**Dos hallazgos `CORREGIR ANTES DE PUBLICAR`, los dos aceptados y corregidos antes del commit.** Uno
era una regresión estructural que el redactor introdujo por seguir una versión desactualizada de la
norma; el otro, una cifra derivada mal calculada. **Ninguno de los dos lo habría detectado una
revisión general**, que es exactamente el argumento por el que estos controles no son sustituibles.
