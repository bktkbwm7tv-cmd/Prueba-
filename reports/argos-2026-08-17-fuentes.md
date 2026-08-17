# ARGOS 100 — Registro de fuentes (auditoría)

Corte: 2026-08-17 · Ventana de hechos: **2026-08-16 07:38 CDMX → 2026-08-17 02:47 CDMX**.
Continuación de ARGOS 99 (corte 2026-08-16). Este documento respalda `argos-2026-08-17.html` y
`argos-2026-08-17-movil.html`, y existe para que todo `SIN DATO` de la edición sea demostrable.

Ventana efectiva: **~19 horas**, de la mañana del domingo a la madrugada del lunes. Es más corta que
las 24 h habituales porque el corte se toma en continuidad estricta desde el cierre de ARGOS 99.
Esa brevedad es relevante para interpretar el volumen de hechos y se hace explícita en el producto.

---

## Limitación metodológica — sexta edición consecutiva, con el bloqueo ahora medido por sonda

**Sonda de entorno ejecutada al inicio de la sesión por el coordinador**, con `curl` directo contra
cinco hosts de control:

| Host | Resultado |
|---|---|
| `www.gob.mx/guardianacional/prensa` | 403 al CONNECT |
| `www.gob.mx/sspc` | 403 al CONNECT |
| `fiscalia.chihuahua.gob.mx` | 403 al CONNECT |
| `www.eluniversal.com.mx` | 403 al CONNECT |
| `es.wikipedia.org` | 403 al CONNECT |

El registro del propio proxy lo confirma textualmente: `gateway answered 403 to CONNECT (policy
denial or upstream failure)`. **El bloqueo es total y no se limita a `*.gob.mx`**: alcanza a medios
nacionales y a dominios de control ajenos al caso. Es una política de la organización y no se
intentó rodearla.

**Consecuencia operativa aplicada en esta edición**: se prohibió `WebFetch` a los seis equipos
regionales. La definición anterior mandaba intentar la lectura directa antes de la búsqueda, lo que
desperdiciaba un turno por dominio sin ninguna posibilidad de éxito. La prohibición liberó
presupuesto real y quedó escrita en `.claude/agents/barrido-regional.md`.

**Cero portales leídos por acceso directo, de ~128 objetivo, en las seis regiones.** Ningún
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de esta edición puede presentarse como vacío
institucional verificado. **Techo de confianza efectivo: ★★★☆☆ para todos los hechos de la
ventana** — undécima edición consecutiva sin superar ★★★★☆.

### Presupuesto de búsqueda — la corrección central frente a ARGOS 99

En ARGOS 99 los seis barridos agotaron entre sí las 200 consultas de la sesión y dejaron dos hechos
rojos sin verificar. Esta edición fijó topes por adelantado:

| Equipo | Tope | Consumo | Nota |
|---|---|---|---|
| Verificación PRIORIDAD 1 | 26 | **15** | Ejecutada **primero y en solitario** para garantizar su cuota |
| Barrido Noroeste | 20 | 20 | Tope alcanzado |
| Barrido Noreste | 20 | 20 | Tope alcanzado |
| Barrido Occidente | 20 | **22** | Excedido en 2 — declarado por el propio equipo |
| Barrido Centro | 20 | **21** | Excedido en 1 — declarado por el propio equipo |
| Barrido Golfo | 20 | **24** | Excedido en 4 — declarado por el propio equipo |
| Barrido Sureste | 20 | 20 | Tope alcanzado |
| **Total** | **166** | **142 de 200** | Reserva no consumida: ~58 |

Los tres excesos se declararon sin ocultarse, que es el comportamiento que la regla busca. Ninguna
región terminó con informe vacío por inanición de presupuesto, que era el fallo silencioso de
ARGOS 99.

### La tercera casilla de cobertura cambió lo que el producto puede afirmar

Se incorporó `SIN RESULTADO INDEXADO EN VENTANA`, distinta de "sin actualización constatada" y de
"no revisada". Resultado en las seis regiones: **ninguna entidad pudo reclamar la casilla de "sin
actualización constatada"**, porque bajo bloqueo total no se puede ver el listado de boletines de
ningún portal. Sin esa casilla, un corte con cinco hechos en todo el país habría producido decenas
de `SIN DATO` falsos.

### Los doce señuelos de fecha y año neutralizados

El resumidor de `WebSearch` volvió a afirmar fechas que la fuente no sostiene, y a mayor escala que
en el corte anterior. La única técnica que funcionó fue **exigir la fecha en la URL o el titular** y
descartar cuando solo aparece en el cuerpo parafraseado.

| # | Señuelo | Fecha real | Fecha sugerida |
|---|---|---|---|
| 1 | Azcapotzalco, CDMX — 4 ejecutados, menor de 13 años | **14-jun-2026** | 16-ago-2026 |
| 2 | Veracruz — "108 armas de fuego" (Tierra Blanca) | **15-jun-2026** | ventana 15-17 ago |
| 3 | "Tormenta Junior", Matamoros | **17-ago-2025** | 17-ago (sin año) |
| 4 | Acapulco, Las Playas — armas y 52 dosis | **15-dic-2025** | entre resultados recientes |
| 5 | Veracruz — COESCONPAZ "33 años / 8 años" | **30-ene-2023** | agosto 2026 |
| 6 | Veracruz — "51 resoluciones / 12 condenatorias" | **13-mar-2026** | agosto 2026 |
| 7 | Cuautla — bar "La Azotea", 1 muerto 2 heridos | **14-mar-2026** | ventana |
| 8 | Morelia — Jorge "N", 82 años | 12-ago, **caso distinto** | Gabriela "N" |
| 9 | Morelia — Brenda Marisol G., 110 años | **29-abr-2025**, caso distinto | Gabriela "N" |
| 10 | La Piedad — 3 sicarios muertos, 4 policías heridos | **22-feb-2026**, hecho distinto | `ARG-98-002` |
| 11 | FGJ-CDMX — fraude bancario, 5 vinculados | hecho procesal **10-ago** | URL lleva 17-ago |
| 12 | Zamora — El Universal, 3 abatidos, misma colonia | **2-oct-2025** | 15-ago-2026 |

El caso 11 es el más instructivo: la URL de Infobae lleva fecha 17-ago y sería válida bajo la regla
de "fecha en la URL", pero esa es la **fecha de publicación** y el hecho procesal es del 10-ago. La
regla de la URL fija la publicación, no el hecho; ambos deben distinguirse siempre.

---

## Verificación PRIORIDAD 1 — los tres pendientes heredados de ARGOS 99

**Dos de los tres eran falsos.** Es el resultado más importante de esta edición.

### ARG-100-FE-001 — Azcapotzalco, CDMX: error de fecha heredado

- **Veredicto**: el hecho es real, pero del **14 de junio de 2026**, no del 16 de agosto.
- Cuatro personas muertas por arma de fuego en calle Doctor Licéaga, col. Pueblo de Santa María
  Malinalco: hombres de **39 y 13 años** y mujeres de **35 y 26**. Dos adolescentes heridas
  sobrevivieron. Agresores en tres motocicletas. Dosis de droga en el inmueble.
- Fechas fijadas **en la URL**: `lasillarota.com/metropoli/2026/6/14/…`, `latinus.us/mexico/2026/6/14/…`,
  `infobae.com/mexico/2026/06/14/…`, `jornada.com.mx/noticia/2026/06/14/capital/…`,
  `record.com.mx/…/2026061518230590601`. También El Universal, Excélsior, MVS Noticias y Heraldo.
- Barrido específico de FGJ-CDMX y SSC-CDMX para el **15-17 de agosto de 2026**: **ningún
  multihomicidio en Azcapotzalco**. Dato coherente: La Jornada del 15-ago-2026 reporta la cifra más
  baja de homicidios dolosos en quince años para el jueves previo.
- **RESERVA EXPRESA, publicada en el producto**: no localizar la nota **no prueba** que no ocurriera
  nada esa madrugada. Lo demostrado es que el hecho descrito con ese detalle es de junio.
- **Contradicción que persiste dentro del evento de junio**: la edad de las dos menores heridas se
  reporta como 10 y 12 años en unas fuentes y 15 y 17 en otras. No se resolvió.
- Ninguna fuente institucional primaria localizada; toda la corroboración es de medios que citan a
  la autoridad de forma indirecta.

### ARG-100-FE-002 — Zamora, Michoacán: omisión real de ARGOS 99, recuperada

- **Veredicto**: confirmado, hecho del **15-ago-2026 ~05:00 h**. Fecha fijada en URL:
  `redmichoacan.com/2026/08/15/caen-cuatro-armados-tras-operativo-y-balacera-en-zamora-…`
- Reporte al C5i/911 por personas armadas en col. Primero de Mayo; detonaciones también en col.
  Monte Olivo; despliegue de Ejército y Guardia Nacional.
- **4 detenidos**: Salvador A. D., José Ángel C. Z., José R. O., Miguel Ángel A. G.
- Asegurado: **3 fusiles AR-15**, **1 pistola**, camioneta con reporte de robo, ponchallantas.
  Sin lesionados (preliminar). A disposición del MP Federal.
- **Ninguna fuente publica cartuchos ni cargadores.** No se infiere.
- Fuentes regionales: RED Michoacán, La Voz de Michoacán, Mi Morelia, Respuesta, Contramuro,
  Atiempo, RED113. **Sin comunicado institucional localizado.** Confianza ★★★☆☆.
- **Tratamiento**: cae en la ventana de ARGOS 99 (15-ago 07:29 → 16-ago 07:38). Se publica como
  ficha de recuperación y **no se suma a ningún total de ARGOS 100**.

### ARG-100-FE-003 — Veracruz "108 armas": descartado por ventana

- **Veredicto**: hecho del **15-jun-2026**, dos meses fuera de ventana. Fecha fijada por el propio
  boletín institucional: `veracruz.gob.mx/2026/06/15/ssp-y-fuerzas-federales-aseguran-armamento-granadas-y-droga-en-tierra-blanca/`
- Cateos en tres inmuebles de **Tierra Blanca** por SSP Veracruz, SEMAR, SEDENA, GN y FGR:
  **108 armas largas**, 50 granadas, 2,700 cargadores, 51,400 cartuchos, 3 lanzagranadas, material
  pirotécnico, 2 vehículos "Razer", 1 camioneta, 2 motocicletas y 440 kg de marihuana.
  **Sin detenidos reportados.**
- Contradicción menor no resuelta: impacto económico de 110 mdp (Gabinete) frente a 11.5 mdp
  atribuidos solo a la droga. No afecta la fecha.
- Corroboración: El Universal, La Jornada (`/2026/06/15/estados/`), veracruzenred.mx, Panorama
  Edomex, La Red Informativa. Confianza ★★★★★ **para el hecho**, irrelevante para este corte.
- **Descartado expresamente** para que no vuelva a resurgir en cortes futuros.

---

## Página 2 — Crimen organizado (I)

### ARG-100-001 — Altamira, Tamaulipas: 297,000 L de diésel (🟢 VERDE)

- **Hecho**: 16-ago-2026. Diligencia ministerial de la FGR con apoyo de la SEMAR en una
  distribuidora de combustible. Asegurados **297,000 litros de diésel**, el inmueble,
  **23 tractocamiones**, **70 remolques tipo plataforma**, **23 dollys** y equipo de trasiego.
- **Contradicción publicada sin arbitrar**: El Universal reporta **3 detenidos**
  (`eluniversal.com.mx/nacion/aseguran-297-mil-litros-de-diesel-en-altamira-tamaulipas-reportan-tres-detenidos/`);
  La Razón reporta **2** (`razon.com.mx/estados/2026/08/16/aseguran-297-mil-litros-de-diesel-en-altamira-tamaulipas-hay-dos-detenidos/`,
  fecha en URL). No se localizó comunicado de FGR ni SEMAR que fije el número.
- **Corroboración**: nacional (El Universal, La Razón) + regional (Plano Informativo, Hoy Tamaulipas,
  Uniradio). Las cinco coinciden en los 297,000 L y en el inventario de unidades.
  `Pendiente de corroboración institucional.` Confianza ★★★☆☆ / Medio.
- **Contexto NO verificado institucionalmente**, registrado como tal y no como dato: los medios
  citan un acumulado de ~4.52 millones de litros y 16 detenidos desde el 21-jul, y describen este
  como el cuarto golpe al huachicol en Tamaulipas en tres semanas.
- **No entra al módulo de armamento**: sin armas aseguradas. Sus detenidos corresponden a
  "Detenciones relevantes" del tablero ejecutivo.
- **Reactiva la categoría de huachicol**, declarada sin actualización en los dos cortes anteriores.

### ARG-100-002 — León, Guanajuato: 506 kg de marihuana en paquetería (🟢 VERDE)

- **Hecho**: 16-ago-2026. Un oficial canino de las FSPE ("Orkan") detecta **506 kg de presunta
  marihuana** en **39 cajas** dentro de una empresa de paquetería de la col. Las Rosas. A
  disposición de la FGR-León. **Sin detenidos.**
- **Fuente institucional — la única del corte fechada dentro de la ventana**:
  `boletines.guanajuato.gob.mx/2026/08/16/detecta-oficial-canino-de-las-fspe-mas-de-media-tonelada-de-presunta-marihuana-en-paqueteria-de-leon/`
  con fecha en la propia URL. **No pudo leerse por acceso directo**: se localizó por índice de
  buscador, por lo que la cita descansa en el resumen indexado y no en el documento.
- **Corroboración**: Infobae, La Jornada San Luis, AM León, Periódico Correo, todas del 16-ago.
  Confianza ★★★☆☆ / Medio.
- **Fuera de la taxonomía del módulo de armamento** (es droga). Sin detenidos, no aporta a ningún
  renglón.

### ARG-100-003 — Hermosillo, Sonora: 3 armas cortas, 5 detenidos (🟢 VERDE)

- **Hecho**: 16-ago-2026. La AMIC detiene a **cinco hombres** en col. Casa Bonita Residencial, blvd.
  Agustín G. del Campo. Asegurados **3 armas cortas (pistolas)** y droga. Uno de los detenidos
  acumula **8 órdenes de aprehensión por desaparición y secuestro**.
- **Cartuchos y cargadores: no especificados por ninguna fuente.** No se infieren ni se sustituyen
  por cero en el total; se marcan `n/p` en la tabla.
- **Fuentes**: Tribuna (regional, fecha en URL `tribuna.com.mx/seguridad/2026/08/16/…`), Infobae
  (nacional, URL `infobae.com/mexico/2026/08/17/…`), Crítica (regional). Las tres coinciden en
  detenidos, armas y órdenes de aprehensión.
- **Sin fuente institucional**: no se localizó comunicado de FGJES ni de `sonora.gob.mx`.
  `Pendiente de corroboración independiente.` Confianza ★★★☆☆ / **Bajo** en la escala del módulo.
- **Único evento del corte que alimenta el conteo nacional de armamento.**

---

## Página 3 — Crimen organizado (II)

### ARG-100-004 — Pinotepa Nacional, Oaxaca: cateo con 3 detenidos (🟢 VERDE)

- **Hecho**: 16-ago-2026. Cateo de la FGEO con **3 detenidos** (1 mujer, 2 hombres),
  metanfetamina y cannabis. **Sin armamento asegurado.**
- **Cantidad de narcótico no publicada** → evento cualitativo, no aporta cifras a ningún total.
- Localizado por búsqueda dirigida a la FGEO en el barrido Sureste. `portal.fgeo.gob.mx` no pudo
  leerse por acceso directo. `Pendiente de corroboración independiente.` Confianza ★★★☆☆.
- **Valor de contraste de cobertura**: es la única acción institucional localizada en las seis
  entidades del Sureste, y confirma que la FGEO sí produjo actividad publicable en el periodo — lo
  que refuerza que el silencio de los demás portales es `SIN RESULTADO INDEXADO`, no inactividad.
- Sus 3 detenidos **no entran** al módulo de armamento (detención sin aseguramiento de armas).

### ARG-100-005 — Tijuana, Baja California: 1 arma sin clasificar (🟢 VERDE)

- **Hecho**: 16-ago-2026. La Policía Municipal detiene a Hugo "N", 37 años, tras denuncia por asalto
  a un peatón en el Cañón del Padre. Asegurada **1 arma de fuego cargada**, **tipo no especificado**.
  Remitido a la FGE. **No vinculado por la autoridad a la delincuencia organizada.**
- **Fuente única regional**: `tijuanaenlinea.com/policiaca/2026/08/16/capturan-a-asaltante-armado-tras-atender-denuncia-en-canon-del-padre/`
  (fecha en URL). Sin segunda fuente ni comunicado.
  `Pendiente de corroboración independiente.` Confianza ★★☆☆☆ / Bajo.
- **Fuera del total nacional por dos razones independientes**, cualquiera suficiente: (a) arma **sin
  clasificar** como corta o larga, lo que impide asignarla a una categoría de la taxonomía
  obligatoria; (b) **fuente única**, por debajo del umbral de integración. Su detenido tampoco suma.
- Se registra por completitud del barrido; valor de inteligencia bajo.

### ARG-100-SEG-001 — Seguimientos que no cierran

| Caso | Estado tras este corte |
|---|---|
| **Edomex, verificentros (`ARG-97-004`)** | Audiencia del 15-ago 10:30 h en el Juzgado de Control de Chalco **sin resolución publicada**. Seis búsquedas dirigidas adicionales, **diez acumuladas entre dos ediciones**; todas las fuentes siguen describiendo la audiencia como futura o en curso. `SIN RESULTADO INDEXADO EN VENTANA` |
| **Morelos, Cuautla (`ARG-99-004`)** | Contradicción **reconfirmada en ambos extremos**: 2 lesionados (Fiscalía de Morelos) frente a 5 (La Unión, Azteca Morelos). Sin boletín de cierre de la FGE Morelos |
| **Oaxaca, Zanatepec (`ARG-98-001`)** | **Tercer corte consecutivo sin detenidos.** Búsqueda dirigida a la FGEO sin actualización posterior al 15-ago |
| **Michoacán, Gabriela "N" (ARGOS 92)** | Audiencia de individualización de sanción **sigue sin celebrarse**. Sin pena impuesta, no hay sentencia que contar |

---

## Página 4 — Conteo Nacional de Armamento

### Total nacional del corte

| Renglón | Cifra | Nota |
|---|---|---|
| Armas cortas | **3** | Hermosillo, Sonora |
| Armas largas | 0 | Ninguna dentro de la ventana |
| Cartuchos | **SIN CIFRA** | Ninguna fuente publicó cifra — no es cero, es ausencia de publicación |
| Cargadores | **SIN CIFRA** | Ídem. Nunca se suman con los cartuchos |
| Granadas · AEI · Explosivos | 0 | Sin registro |
| Armamento especial · drones armados | 0 | Sin registro |
| **Personas detenidas** | **5** | En el mismo evento del aseguramiento |
| Entidades con aseguramiento | **1** | Sonora |
| Eventos contabilizados | **1** | `ARG-100-ARM-001` |
| Eventos cualitativos sin cantidad | **4** | Detallados abajo |

**La distinción entre `0` y `SIN CIFRA` es material**: cero significa que la autoridad publicó una
cifra y era cero; `SIN CIFRA` significa que nadie publicó nada. Sustituir lo segundo por lo primero
sería inventar un dato.

### Tabla obligatoria

| ARG-ID | Entidad | Municipio | Fecha hecho | Cortas | Largas | Cartuchos | Cargadores | Granadas | AEI | Expl. | Detenidos | Corporación | Fuente primaria | Corroboración | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ARG-100-ARM-001 | Sonora | Hermosillo | 2026-08-16 | 3 | 0 | n/p | n/p | 0 | 0 | 0 | 5 | AMIC / FGJES | Tribuna | Infobae, Crítica | Bajo |

### Eventos cualitativos y no integrados

- **Tijuana, BC** (`ARG-100-005`): 1 arma **sin clasificar**, fuente única. Fuera por taxonomía y por
  umbral de corroboración. Detenido no integrado.
- **Altamira, Tamaulipas** (`ARG-100-001`): hidrocarburo y 116 unidades vehiculares, fuera de
  taxonomía. Detenidos (2 o 3, sin conciliar) van a "Detenciones relevantes".
- **León, Guanajuato** (`ARG-100-002`): 506 kg de marihuana, fuera de taxonomía. Sin detenidos.
- **Pinotepa Nacional, Oaxaca** (`ARG-100-004`): narcótico en cantidad no publicada, sin armamento.
  3 detenidos no integrados.
- **Zamora, Michoacán** (`ARG-100-FE-002`): 3 fusiles AR-15, 1 pistola, 4 detenidos —
  **hecho del 15-ago, ventana de ARGOS 99**. Recuperado como omisión, **no sumado** a este corte.

### Corrección al total de ARGOS 99 — Sain Alto, Zacatecas (`ARG-99-ARM-002`)

**Reserva (b) de corroboración asimétrica: RESUELTA.** El barrido Noreste localizó el boletín
**institucional primario** de la SSP de Zacatecas:
`ssp.zacatecas.gob.mx/detienen-fuerzas-de-seguridad-a-cinco-probables-generadores-de-violencia-aseguran-arma-de-fuego-y-droga/`

Confirma textualmente **1 arma corta, 1 cargador y 16 cartuchos útiles**, además de 30 envoltorios
de metanfetamina, 2 equipos de comunicación y los **5 detenidos con nombre y edad**. ARGOS 99 había
dejado el desglose fuera de su total porque solo una de tres fuentes lo publicaba. Al tratarse de
una **fuente institucional primaria** y no de una segunda réplica mediática, el criterio de "versión
aislada" deja de aplicar: **procede reintegrar 1 arma corta, 1 cargador y 16 cartuchos al total de
ARGOS 99**, con confianza **Medio** (fuente oficial única).

El hecho es del 15-ago: **la corrección se aplica al total de ARGOS 99, no al de esta edición.**

**Reserva (a): SIGUE ABIERTA.** El boletín **no consigna hora**, de modo que la pertenencia del
hecho a la ventana estricta de ARGOS 99 continúa sin poder demostrarse. Se mantiene
`HORA NO DETERMINADA`.

### Contradicción abierta que NO se cierra — "Operación Sable", Mazatlán (`ARG-97-ARM-003`)

Sigue sin arbitrar (1 cargador / 15 cartuchos frente a 9 cargadores / 55 cartuchos). **Dato nuevo
aportado por el barrido Noroeste**, que no constaba en `_pendientes.md`: la intervención se sitúa en
el **fraccionamiento Real del Valle** con **3 detenidos**, además de droga, radios, vehículos y
efectivo. **No se integra**: la fecha de esa nota no está fijada en URL ni titular. Solo un boletín
de la SSP o de la FGE de Sinaloa puede cerrarla.

### Indicador de cobertura — armamento

- **Portales leídos por acceso directo: 0** de ~128 objetivo, en las seis regiones, sin excepción.
- **Portales consultados por búsqueda dirigida: 38.**
- **Portales que publicaron dentro de la ventana: 1** — `boletines.guanajuato.gob.mx`.
- **Sin resultado indexado en ventana: 37.**
- **Sin actualización constatada: 0.** Ninguna entidad puede reclamar esta casilla.
- **Entidades con cobertura mínima** (una sola búsqueda agregada, sin barrido de los cuatro
  portales): Puebla, Hidalgo, Querétaro, Tlaxcala, Campeche, Yucatán, Quintana Roo.
- **No consultados**: Policía Estatal o equivalente en la mayoría de entidades; SEDENA, SEMAR y ANAM
  sin consulta dirigida propia.
- **Mesa de Construcción de la Paz**: **0 de 32**, y **deja de contarse en el denominador** — casi
  nunca tiene sitio propio; solo se busca ante un hecho de alto impacto, condición no cumplida en
  ninguna región.

### Vacío federal — cuarto corte consecutivo

`gob.mx/sspc` / Gabinete de Seguridad: **el boletín diario más reciente indexado sigue siendo el del
13-ago**. Búsquedas dirigidas específicas para el 14, 15, 16 y 17 de agosto no devolvieron nada.
Confirmado de forma **independiente por cuatro de los seis equipos regionales** (Noroeste,
Occidente, Golfo, Sureste). Es la fuente que publica el desglose numérico por entidad: sin ella este
módulo no puede medir volumen nacional, solo registrar lo que la prensa recogió.

Guardia Nacional (`gob.mx/guardianacional/prensa`): boletines indexados datan de 2024-2025, sin
fecha 2026-08 verificable en URL o titular.

---

## Página 5 — Rastreo Nacional de Sentencias

### Conteo nacional del corte

**Cero en todos los renglones**: 0 condenatorias, 0 absolutorias, 0 procedimientos abreviados,
0 sentencias en juicio oral, 0 firmes, 0 personas sentenciadas, 0 años de prisión acumulados,
0 multas, 0 reparación del daño ordenada.

**Este cero no es un vacío institucional demostrado**: trece fiscalías no llegaron a revisarse y
ningún boletín pudo leerse por acceso directo. La casilla correcta para las diecinueve revisadas es
`SIN RESULTADO INDEXADO EN VENTANA`.

### ARG-100-SEN-SEG-001 — Cosamaloapan, Veracruz: se rompe el vacío de tres ediciones

**Primera de las "10 condenatorias sin desglose" del agregado del 13-ago que se logra identificar.**

- **Autoridad**: FGE Veracruz, por conducto de la Unidad Especializada en Combate al Secuestro.
- **Delito**: secuestro agravado. **Distrito judicial**: Cosamaloapan.
- **Sentenciados (5)**: Ángel Manuel "N", Pablo "N", Yael Alberto "N", Francisco Antonio "N",
  Fernando "N".
- **Pena**: **180 años de prisión a cada uno** (900 años en conjunto).
- **Firmeza: NO INFORMADA.** Ninguna fuente indica si causó estado. No se asume.
- **Hecho de origen**: secuestro del **22-ago-2024** en la localidad de Pachuca, mun. Ixmatlahuacan;
  liberación de **3 víctimas** y detención en flagrancia el **2-sep-2024**.
- **Publicación**: **13-ago-2026**, dentro del agregado "53 resoluciones judiciales / 11 sentencias
  condenatorias" presentado en la COESCONPAZ.
- **Fuentes**: `golpepolitico.com/2026/08/13/…` (reproduce el boletín con detalle fáctico completo,
  fecha en URL); corroboración independiente de `xeu.mx` y `elsoldeveracruz.com` (cifra conjunta de
  900 años) y `notiver.com` (cifra individual de 180 años). URL institucional en
  `comunicacion.fiscaliaveracruz.gob.mx` **no localizada indexada**.
- **Estatus**: `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL`.
  Confianza **Medio**.
- **Fuera de la ventana** (13-ago) → no se integra al conteo de ARGOS 100.
- **Sobre la pena**: 180 años por secuestro agravado es coherente con acumulación por número de
  víctimas, pero sin constancia de firmeza ni de si las penas son concurrentes procede la marca
  `Pena compuesta — requiere revisión jurídica`.
- **Lección operativa confirmada**: la vía útil **no** es la sala de prensa de la Fiscalía —que
  publica agregados— sino la **reproducción íntegra del boletín en medios regionales**.
- **Quedan 9 de las 10 condenatorias sin desglose.**

### Seguimientos judiciales que no cierran

| Caso | Estado |
|---|---|
| **FGE Tabasco, Cunduacán** (`ARG-99-SEN-002`) | 8 años por violación, Miguel "N". Dos búsquedas dirigidas adicionales a `fiscaliatabasco.gob.mx` **no localizaron el boletín**. Sigue `PENDIENTE DE CONFIRMACIÓN OFICIAL`. Dato útil: los boletines se numeran en `/Boletin/Index/<id>` |
| **FGJEM Ecatepec (40 años)** (`ARG-99-SEN-001`) | Sin comunicado institucional localizado. Sin integrar |
| **FGESLP Matlapa (2a8m)** (`ARG-99-SEN-003`) | Sin comunicado institucional localizado. Sin integrar |
| **Michoacán, Gabriela "N"** (ARGOS 92) | Sin pena impuesta. No hay sentencia que contar |
| **Edomex, verificentros** (`ARG-97-004`) | **Una vinculación a proceso no es sentencia** y no entrará a este módulo aunque se publique |
| **Playa del Carmen, QRoo** | 50 años a tres personas por homicidio calificado doble, publicada 12-ago-2026, **sigue ausente de todos los `-fuentes.md`**. Ver abajo |

### Vacío de edición anterior — Playa del Carmen, Quintana Roo

Confirmado y **enriquecido** por el barrido Sureste. Sigue ausente del repositorio.

- **Sentenciados**: Rodman de Jesús Calderón Pineda "Zombi", Juan José Velázquez Ramírez "Pollo",
  Óscar Zacarías Chablé "Botitas"/"Sicario". **50 años** cada uno por homicidio calificado doble.
- **Hecho**: 12-oct-2020, Quinta Avenida, col. Centro.
- **Multa citada**: 260,640 pesos por sentenciado — **no reverificada institucionalmente**.
- **Fuentes**: `24horasqroo.mx/2026/08/12/50-anos-prision-4/`, `quintanaroohoy.com`,
  `grupointeractivotv.com`, `periodicoquequi.com`.
- **No es hallazgo de ARGOS 100**: es un vacío de edición anterior, pendiente de integración formal.

### Sentencias localizadas y descartadas por ventana

Documentadas para que la edición siguiente no las recoja como nuevas:

| Entidad | Sentencia | Fecha |
|---|---|---|
| Oaxaca | 140 años, secuestro agravado ("El Pumba") | 3-ago |
| Oaxaca | 9 años, robo con violencia, San Pedro Pochutla | 11-ago |
| Guerrero | 80 años, secuestro agravado | 6-ago |
| Yucatán (FGR) | 8 años y 7a2m a cinco personas, narcomenudeo y cartuchos de uso exclusivo | 6-ago |
| Guanajuato (FGR) | 13a4m y 6a8m, delincuencia organizada | principios de agosto |
| Guanajuato | Ratificación de 4.5 años por cohecho, exfuncionario | 3-ago |
| Tamaulipas | 50 años a doce secuestradores | mayo-2026 |
| Zacatecas | 4 años por extorsión | julio-2026 |
| Jalisco | 19 sentenciados del CJNG, hasta 18 años | 10-ago (ya cerrado en ARGOS 99) |

### Indicador de cobertura — sentencias

- **Fiscalías revisadas: 19 de 32.**
- **Fiscalías NO revisadas: 13** — las seis del **Noroeste** (Baja California, Baja California Sur,
  Sonora, Chihuahua, Sinaloa, Durango) y las siete del **Centro** (CDMX, Estado de México, Morelos,
  Puebla, Tlaxcala, Hidalgo, Querétaro). En ambas regiones el presupuesto se agotó en el módulo de
  armamento antes de llegar a la búsqueda judicial. **Se reportan como no revisadas, jamás como
  "sin actualización".**
- **FGR revisada: parcialmente** — solo por incidencia regional en Golfo y Sureste, sin consulta
  dirigida a sus fiscalías especializadas ni a sus delegaciones estatales.
- **Fiscalías con sentencia publicada dentro de la ventana: 0.**
- **Fiscalías con resultado indexado fuera de la ventana: 8.**
- **Páginas no disponibles: 0 registradas como tales**, porque no se intentó el acceso directo: la
  sonda inicial demostró que habría fallado en todos los dominios.
- **Portales tratados por búsqueda dirigida**: `pjeveracruz.gob.mx`,
  `comunicacion.fiscaliaveracruz.gob.mx`, `fiscaliaveracruz.gob.mx`, `veracruz.gob.mx/seguridad`,
  `fiscaliatabasco.gob.mx`, `portal.fgeo.gob.mx`, `fiscaliaguerrero.gob.mx`, `ssp.chiapas.gob.mx`,
  `fgecam.campeche.gob.mx`, `ucs.campeche.gob.mx`, `fge.yucatan.gob.mx`, `fgeqroo.gob.mx`,
  `fiscalia.jalisco.gob.mx`, `fiscaliazacatecas.gob.mx`, `ssp.zacatecas.gob.mx`,
  `tamaulipas.gob.mx/seguridadpublica`, `fiscalia.chihuahua.gob.mx`, `fiscalia.durango.gob.mx`,
  `boletines.guanajuato.gob.mx`, `ssp.michoacan.gob.mx`, `fgjcdmx.gob.mx`, `ssc.cdmx.gob.mx`,
  `fiscaliaedomex.gob.mx`, `fiscalia.puebla.gob.mx`, `fiscaliageneralqro.gob.mx`,
  `fgjtlaxcala.gob.mx`, `gob.mx/sspc`, `gob.mx/guardianacional/prensa`.

### Advertencia estructural sobre la regla de validación jurídica

Mientras el egreso siga bloqueado, la regla de CLAUDE.md que exige el **término literal** de condena
es **inaplicable**: los resúmenes del buscador llegan parafraseados y a veces traducidos. **Toda
sentencia localizada en estas condiciones queda, como máximo, en `PENDIENTE DE CONFIRMACIÓN
OFICIAL`**, y el conteo nacional judicial permanecerá estructuralmente en cero. No es un resultado
del sistema de justicia: es un resultado del canal de acceso. Esta advertencia quedó escrita por
adelantado en la definición de `barrido-regional` para no redescubrirse cada corte.

---

## Caso sin arbitrar por contradicción entre URLs — Suchiapa, Chiapas

Bulmaro "N", detenido con **1 arma corta 9 mm, 2 cargadores, 32 cartuchos**, 15 envoltorios de
presunta cocaína tipo crack, uniforme clonado de la Fuerza Pakal, chaleco, funda y vehículo.

**Contradicción de fecha entre URLs**: El Heraldo de México fecha la nota en su URL el
**2026/8/15**; Infobae la fecha en su URL el **2026/08/16**. Aplicando la regla de primera
publicación, el hecho es del 15-ago, anterior al inicio de la ventana de ARGOS 100.

**Se descarta de esta edición.** Es **candidato a omisión de ARGOS 99** —no figura en
`argos-2026-08-16-fuentes.md`, verificado por lectura íntegra— y se entrega como **pista para
arbitraje editorial**, no como corrección confirmada, porque la contradicción no pudo resolverse sin
acceso directo a las fuentes.

---

## Categorías buscadas sin resultado verificable en la ventana

Ninguna de estas puede presentarse como vacío institucional, por las razones del apartado de
cobertura: **fosas clandestinas, narcobloqueos, ataques a infraestructura crítica, drones armados,
uso de AEI, ataques a autoridades, desapariciones múltiples, narcotráfico marítimo, redes
financieras y congelamiento de cuentas UIF, extorsión, trata, aduanas.**

**Huachicol** deja de estar en esta lista: se reactiva con `ARG-100-001`.

---

## Contexto institucional del corte

- **Boletines del Gabinete de Seguridad**: sin indexar desde el 13-ago. **Cuarto corte consecutivo.**
- **Guardia Nacional**: sin boletín con fecha 2026-08 verificable.
- **Único boletín institucional del corte fechado en ventana**: FSPE Guanajuato, 16-ago.
- **Registro de agentes**: los tres controles de CLAUDE.md (`barrido-regional`, `procedencia-cifras`,
  `editor-duplicidad`) **no estaban disponibles por nombre al inicio de la sesión**, igual que en
  ARGOS 99. Los seis barridos se ejecutaron cargándoles su archivo de definición como primer paso,
  con el mismo método y las mismas herramientas. El registro se recargó a mitad de sesión. **Es un
  fallo reincidente**, no resuelto.

---

## Indicadores oficiales — respaldo

**SESNSP**, homicidio doloso: **86.9 → 45.4 víctimas/día (−48%)**, sep. 2024 – jun. 2026.

- **Entrada al repositorio**: ARGOS 86 (`reports/argos-2026-08-02.html`), conforme a la fe de erratas
  de procedencia `ARG-99-FE-003`.
- **Estatus**: `HEREDADO — NO REVERIFICADO`. Con el egreso bloqueado, `gob.mx/sesnsp` no es
  consultable y la reverificación es **materialmente imposible**. Se aplica la distinción entre *sin
  respaldo jamás* (que obligaría a fe de erratas) y *con respaldo de origen, sin reverificación*
  (que es este caso).
- **Contradicción abierta**: ARGOS 90 registró una cifra alterna de **−60%** para el mismo periodo,
  marcada entonces como *no verificada en portal primario*. Sigue sin resolverse.
- **Sin actualización oficial adicional dentro de la ventana de este corte.**
- No se publican indicadores derivados, proyecciones ni tasas calculadas por ARGOS. Cualquier lectura
  de tendencia a partir de los cinco eventos de este corte sería estadísticamente inválida.
