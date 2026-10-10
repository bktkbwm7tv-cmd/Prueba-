# ARGOS 128 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-10 · **Ventana**: 2026-10-09 07:20 → 2026-10-10 09:08 CDMX · **25 h 48 min**
**Rama**: `claude/argos-128` (partió de `origin/claude/argos-127` = `96b7a8f`).

---

## 1. La base

Bloque 0 ejecutado como primer comando: hora real **2026-10-10 09:08 CST** (UTC−6). El clon arrancó en `60f2777`, dos commits por detrás
de `origin/main`: `git merge --ff-only origin/main` avanzó en fast-forward `60f2777 → 7e55aad` (no «Already up to date», porque el clon
local, no `origin/main`, estaba atrasado; `origin/main` = `7e55aad`, como se esperaba). `git merge --ff-only origin/claude/argos-127`
avanzó en fast-forward `7e55aad → 96b7a8f`. Estado encontrado: `argos-2026-10-09` (ARGOS 127) y **141 archivos** en `reports/`, lo
previsto. HEAD suelto: se abrió `claude/argos-128` antes de escribir.

| Serie | 123 | 124 | 125 | 126 | 127 | **128** |
|---|---|---|---|---|---|---|
| Duración | 23 h 25 | 46 h 19 | 320 h 34 | 17 h 41 | 22 h 24 | **25 h 48** |
| Densidad (hechos/h) | 0,04 | 0,30 | 0,16 | 0,40 | 0,27 | **0,23** (6 / 25,8, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (9 y 10-oct). El generador lo comprueba con `assert`.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`**; el proxy registra `www.gob.mx:443 — connect_rejected` (política de la
  organización). Reverificado al cierre del barrido: `fgr.org.mx`, `sspsinaloa.gob.mx`, `fiscaliaguerrero.gob.mx` y `milenio.com` → `000`.
  `WebFetch` de los agentes a medios (nmas, milenio, lineadirectaportal, tallapolitica, red113, diariodetabasco, noroeste) → `ENOTFOUND`.
  **Ningún documento leído íntegro.** Techo **★★★☆☆**, décima edición.
- **Consulta de control** (penal El Castillo, «riña 9 de octubre», en los dos modos): `standard` devolvió solo la riña del 8-oct con la
  cifra preliminar (6 muertos, 15 heridos); `extended` halló la **segunda riña del 9-oct** (Proceso 2026/10/9, Expansión 2026/10/09,
  Quinto Poder 2026/10/09). **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + una sola ola de **nueve equipos** (encargos 22, seguimientos 14, boletín federal 15, Noroeste 20, Noreste 18,
  Occidente 22, Centro 22, Golfo 12, Sureste 20 = **165**) + **8 del coordinador** = **175**; `procedencia-cifras` con tope de **25** →
  techo **200**. `editor-duplicidad` no busca en la web.
- **Rendimiento del coordinador**: una búsqueda nacional por día de la semana («viernes 9 de octubre», ataque armado) halló **dos rojos
  que ningún equipo regional trajo**: Pinotepa Nacional (Sureste) y San José del Rincón (Centro). Los equipos regionales del Sureste y del
  Centro declararon sin hecho en ventana las dos entidades. Lección en §15.

## 3. Rotación — prioridad sobre el ciclo y CICLO C, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — sentencias | **BC · Jal, Gto · Mor, Pue, Hgo, Qro, Tlax**: las ocho revisadas por `site:`. Querétaro devolvió **tres boletines oficiales con fecha en la ruta** (5, 6 y 8-oct), todos previos a la apertura. Guanajuato: León, 26 años 8 meses, solo medios (9-oct) |
| Prioridad — armamento | **BCS, Son, Dgo, CDMX, Ags**: revisadas por `site:` (SRIV). **Tlaxcala: `NO REVISADA` por segunda edición** — `site:ssc.tlaxcala.gob.mx` devolvió páginas ajenas (dominio no confirmado) y no se consultó `pgjtlaxcala` por armamento |
| Prioridad — alto impacto | **Aguascalientes**: revisada en medios (SRIV) |
| Ciclo | **C** — Occidente + Sureste encabezaron el triaje judicial |
| Rendimiento | **Ninguna sentencia integrable.** El ciclo C halló Guanajuato (León, solo medios, en ventana) y Guerrero (Tlapehuala, 60 años, titular del portal de la FGE, 8-oct, previo). La prioridad halló Querétaro ×3 con boletín oficial, previos |

Serie: C (125) sí · A (126) no · B (127) no · **C (128) no — candidatos, sin integrable.**

## 4. Boletín federal — triple consulta

| Acciones de | Publicado | Estado | Formato |
|---|---|---|---|
| 8-oct | **9-oct** (Línea Directa 2026-10-09__1717173) | **LOCALIZADO** por republicadores: Milenio (acciones del 8-oct en la ruta), SICOM, Candelero, RED113, Tallapolítica, Ahora Noticias, Ahora Tabasco | **diario**, 6 entidades: Chih, Gto, Pue, Tamps, Sin, Tab |
| 9-oct | — | `SIN RESULTADO INDEXADO EN VENTANA`: día suelto (con y sin `site:`), rango «8 y 9», título sin `site:`. **Rangos «7, 8 y 9» y «9 y 10» no probados como cadena** | — |

`gabinetedeseguridad.gob.mx` por `site:`: nada de octubre. `gob.mx/sspc` por `site:`: el archivo de prensa llega al 7-oct. GN, Defensa y
Marina con fecha 9-oct: sin resultado (una sola consulta agrupada: cobertura débil).

**Arbitraje del boletín del 8-oct**: hechos del 8-oct, **anteriores a la apertura de 128** y dentro de la ventana de ARGOS 127, que no lo
tuvo indexado. Se publican como **`-REC-` con ventana de origen ARGOS 127** (precedente de 127 con el boletín del 7-oct):
`ARG-128-REC-003` Río Bravo · `-004` Ciudad Juárez · `-005` Valle de Santiago · `-006` Zacatlán · `-007` Cuauhtémoc. **Renglón de
Tabasco** (Centro, 4 cateos, ~120 cámaras, sin cifras): **no fichado** — cualitativo y `POSIBLE DUPLICIDAD` con `ARG-127-REC-003` (La
Huerta: la detención de «La Flaca» y «El Titi», con equipo de videovigilancia, por Quadratín). **Renglón de Sinaloa**: sin detalle en
ninguna fuente; su correspondencia con Montecarlo (`ARG-127-005`) es hipótesis no confirmada. **Control de topónimo**: Río Bravo buscado
por topónimo (sin agresión); Juárez, Valle de Santiago y Zacatlán por grep del índice.

## 5. Los cuatro encargos

| Encargo | Resultado |
|---|---|
| **Penal El Castillo, 8-oct** (`ARG-127-004`) | **Edad del menor: 2 años** — Línea Directa 2026-10-08 (*slug* «tenia-dos-anos…confirma-sspe») y titular de Excélsior; El Financiero 2026/10/08 dio 11 en titular; CEDH «1 año» solo por resumen. **Armas**: «pistolas calibre 9 mm» (titular de Excélsior), módulos 4 y 5 por resumen; la FGE, por titular de Luz Noticias 2026-10-09, «disparos con arma corta y larga»: contradicción. **Hora**: ~10:00 (El Financiero) / ~11:00 (Milenio) por resumen; 17:35 hora del informe de la SSP. **Ingreso de armas**: sin explicación oficial (el titular de la SSP investiga a trabajadores, por resumen). **Detenidos**: ninguno. **Heridos**: 16 (SSP) frente a 17 (FGE, por resumen; puede sumar la riña del 9). Comunicado de la SSP: `site:sspsinaloa.gob.mx` sin resultado |
| **Penal El Castillo, 9-oct** | **Hecho nuevo** → `ARG-128-004` |
| **Montecarlo · SLP · Ojocaliente** | Ver §8 (dictamen de `procedencia-cifras`) |
| **Uruapan, Sol Naciente** (`ARG-127-REC-001`) | **Corporación**: FGR con Marina, GN y SSPC (resumen) / «agentes de la SSPC» (titulares de fuente abierta). **Detenidos**: **1 en el cateo de Sol Naciente** (titulares de Quadratín y Meganoticias) y **10 en el conjunto de 12 cateos** en Uruapan, Pátzcuaro y Morelia (titular de Crónica 2026/10/09 «Detienen a 10 personas tras 12 cateos en Michoacán; dos agentes resultan heridos»; Infobae 2026/10/10). MVS 2026/10/8: 12 detenidos. **Se abre `ARG-128-REC-008`** (detención, 🟢) separada de la confrontación (`ARG-127-REC-001`, 🟡). Estado de los agentes: no publicado |
| **El Balcón** (`ARG-125-051`) | **Peritaje oficial del video: no existe ninguno publicado.** No se describe su contenido. Amparo 412/2026: concedido el 5-oct por el Juzgado Noveno de Distrito (Iguala), **federal** —La Jornada lo llama «estatal»—; plazo de 3 días para informes; **cumplimiento: sin informe público**. FGE Guerrero ofrece **1.5 mdp** de recompensa (titulares de Proceso, La Silla Rota y El Independiente, 2026/10/9). Marcha en Tecpan (~2 mil, por resumen) y anuncio de marcha a Palacio Nacional. Carpeta: no publicada |
| **Balleza / San Francisco de Borja** | **Indicio de dos hechos, no acreditado**: El Diario de Chihuahua 2026/oct/08, titular «Dejan dos enfrentamientos cuatro muertos»; y 2026/oct/07, titular «enfrentamiento entre soldados y sicarios deja dos muertos» (tramo Guachochi–San Francisco de Borja). **Un solo medio**, y Pinalejo está cerca de Guachochi: `POSIBLE DUPLICIDAD CON ARG-126-REC-004 — NO INTEGRAR HASTA VALIDACIÓN`. El borrador lo fichó como `ARG-128-REC-011`; retirado por `editor-duplicidad` (el ARG-ID no se reutiliza). Abatidos de Balleza: sin identificar |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| **Autolavado de Flores Magón** (`ARG-127-002`) | **3 muertos** confirmados por titulares. **Heridos**: 4 (Los Noticieristas), 5 (Luz Noticias, Sinaloahoy), 3 (Reporte18), cada uno en titular — **no se arbitra ni se suma**. Un menor de 17 años entre los muertos según Los Noticieristas: **no se reproduce el nombre**. Sin detenidos. Vínculo con el doble homicidio del 6-oct: sin información |
| **La Huerta** (`ARG-127-REC-003`) | **Duplicidad probable**: la detención de dos personas por la SSPC en Centro (Diario de Tabasco 2026/10/08; Quadratín: km 10 Carmen–Villahermosa, «a la altura del fracc. La Huerta») es el mismo evento del boletín del 7-oct. **Sigue fuera de todos los totales.** Quadratín: 317 cartuchos y granadas, solo por resumen, con desglose que no suma: no adoptado |
| **Cosalá** (`ARG-127-REC-004`) | **2,693 kg = 2.6 t truncado** (Noroeste por resumen; Sinaloahoy por titular, 2.6 t). El titular «cinco laboratorios en Jalisco, Nayarit y Sinaloa» es de **mayo de 2026** (Gabinete, Proceso 2026/5/17): **no aplica a Cosalá. Cerrado** |
| **Penjamillo** | **Fijado: tarde del miércoles 7-oct**, antes de las 20:30 de la primera publicación (MiMorelia, por resumen; Contramuro «la tarde de este miércoles»). Ventana 126 o 125 → **`ARG-128-REC-009`** 🔴 |
| **Xalisco / Ópalo** (`ARG-125-003`) | Sin cifra oficial ni identificaciones (la fiscal espera las confrontas genéticas). Ópalo: sin respaldo oficial del vínculo. «33 cráneos» (SDP): no adoptado |
| **Casas Grandes** (`ARG-126-REC-003`) | **El hecho es en la col. Infonavit Casas Grandes, Ciudad Juárez**, no en el municipio. **Móvil**: titular de Diario de Juárez y El Diario de Chihuahua 2026/oct/07, «Balacera no fue por secuestro, fue conflicto por no pagar drogas»; la Fiscalía Zona Norte descarta la mujer secuestrada (resumen). Heridos: 2 frente a 3. **Fe de erratas** `ARG-128-FE-003` |
| **Coatzacoalcos** (Pamucé) | **Vinculación a proceso de los 5**, por cuatro titulares (Golpe Político 2026/10/09, Diario de Xalapa, N+, Liberal). **Fecha del acto contradicha**: Municipio Sur 2026/10/06 ya titulaba «detenidas y vinculadas a proceso»; La Silla Rota 2026/10/9, «se quedan en prisión». **No se ficha**: seguimiento de `ARG-124-002` / `ARG-125-021` sin acto nuevo acreditado en la ventana (el borrador lo fichó como `ARG-128-007` 🟢; retirado por los dos controles; el ARG-ID no se reutiliza) |
| **Huanusco** (pista NTR) | Padre de la presidenta municipal, 8-oct → `ARG-128-REC-002` 🟡 |
| **Zihuatanejo · Mixtequilla · 26 extranjeros · Comonfort · Hermosillo** | **`NO REVISADOS`**: el equipo agotó su tope. Pasan a 129 |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Pinotepa Nacional** (`ARG-128-001`) | Hallado por el coordinador. Viernes 9-oct por la tarde: dentro de ventana. **🔴 por víctima periodista** (Hamurabi Huesca Manzano, director de Pinotepa Comunica, por titular de seis medios) **y víctimas múltiples** (3, solo por resumen; otra versión: 2 muertos y una mujer lesionada). La hipótesis de la FGEO (otro blanco) **no baja el color**: la lista roja nombra al periodista como víctima, no como blanco |
| **San José del Rincón** (`ARG-128-003`) | Hallado por el coordinador. ~09:30 del viernes 9-oct, solo por resumen; **ninguna URL con fecha**. Se integra con confianza ★★☆☆☆ |
| **Segunda riña de El Castillo** (`ARG-128-004`) | «El viernes por la mañana»; la SSP lo comunica ~09:25 (resumen). Nada la sitúa antes de las 07:20 y ARGOS 127 consultó a las 07:20-07:30 sin verla: **`FRONTERA DE VENTANA`, integrada en 128** |
| **Naucalpan** (`ARG-128-005`, `-006`) | Publicado el 9-oct (Infobae, Seunonoticias), «por la noche»: la noche del jueves la infiere el resumen, no la fuente. **`FRONTERA`, integrados en 128**, dos fichas: el titular dice «dos hechos distintos» |
| **Celaya** (`ARG-128-002`) | 🟡 por **persecución** con detonaciones, que la lista amarilla nombra; quién disparó, sin precisar. 2 detenidos por titular; «armas aseguradas» por titular frente a «un arma de fuego» por resumen → `ARG-128-ARM-001` **cualitativa**, sin cifra integrada |
| **Michoacán, 12 cateos** (`ARG-128-REC-008`) | Publicado el 9 y 10-oct; MVS 2026/10/8 ya titula 12 detenidos en Michoacán, de modo que el hecho es ≤ 8-oct y **no es de la ventana de 128**. El vínculo con Sol Naciente («dos agentes heridos») y la madrugada del 8-oct son **inferencia de ARGOS**, declarada en la ficha: ventana de origen **126 o 127**. Detención y confrontación, dos eventos; los detenidos de Sol Naciente (1) y del conjunto (10) **no se suman** |
| **Sombrerete** (`ARG-128-REC-010`) | Renglón del boletín del 7-oct (FGR) que ni 126 ni 127 fichó. **Cifras contradichas** (185 frente a 39 detonadores): no se integra al recálculo |
| **Boletín del 8-oct como `-REC-`, no como `FRONTERA` propia** | Los hechos son del 8-oct, enteramente anteriores a la apertura de 128 (9-oct 07:20): la regla de frontera opera cuando la fecha del hecho puede caer en la ventana, y aquí no puede. Sin hora, la ventana de origen es **127 o 126** (126 cerró el 8-oct 08:56). El precedente de 126 (boletín del 7-oct como propio) se dio porque esa ventana sí contenía el 7-oct |
| **Escuinapa** (10 armas, 1,900 cartuchos, 20 AEI) | **9-sep**: descartado por fecha (verificado por el coordinador) |
| **FIRT Olmeca, 16 detenidos** (Diario de Tabasco 2026/10/09) | Agregado estatal del 5 al 8-oct; incluye la detención de La Huerta: no fichado |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-128-FE-001`** — sobre **ARGOS 127**: siete hechos del 8-oct no publicados (`ARG-128-REC-001` a `-007`). Ventana de origen: **127**
  para Papantla (~21:00); **127 o 126, hora no fijada**, para Huanusco y los cinco renglones del boletín del 8-oct. Efecto sobre el semáforo
  de 127, si todos son suyos: rojos 2 → **3** (Papantla), amarillos 2 → **3** (Huanusco), verdes 2 → **7** (Río Bravo, Juárez, Valle de
  Santiago, Zacatlán, Cuauhtémoc).
- **`ARG-128-FE-002`** — sobre **ARGOS 126** (o 125/127, hora no fijada): tres hechos no publicados (`ARG-128-REC-008` a `-010`; Penjamillo y Sombrerete, 126 o 125). Efecto
  sobre el semáforo de 126 tras `ARG-127-FE-001`: rojos 1 → **2** (Penjamillo), amarillos **2**, verdes 7 → **9** (Michoacán, Sombrerete).
  Si Penjamillo resulta de la ventana de 125, o Michoacán de la de 127, se trasladan allí.
- **`ARG-128-FE-003`** — sobre **`ARG-126-REC-003`** (Casas Grandes): el titular «presuntos secuestradores» queda **contradicho**; el
  móvil publicado es una deuda de drogas (dos titulares regionales del 7-oct) y la Fiscalía Zona Norte descarta la mujer secuestrada.
  **Lugar**: col. Infonavit Casas Grandes, Ciudad Juárez. El color 🟡 no cambia.
- **`ARG-128-FE-004`** — **umbral de cifras arrastradas** (dictamen de `procedencia-cifras`): llegan a **dos ediciones consecutivas solo
  por resumen** y se retiran: **Montecarlo** (`ARG-127-005` / `ARG-127-ARM-001`) 30 cartuchos .50 y 2 cargadores —se conserva, por *slug*
  institucional y titulares, «cargadores para Barrett .50», sin cantidad—; **San Luis Potosí** (`ARG-127-006` / `ARG-127-ARM-002`) 2
  revólveres, 29 + 6 = 35 cartuchos —se conserva «3 detenidos con armas y presunta droga», por titular; «arma» frente a «armas» en los
  titulares—; **Ojocaliente** (`ARG-127-REC-002`) 5 largas, 1,093 cartuchos, 47 cargadores. Todos: `CANTIDAD NO DETERMINADA — NO SE
  INTEGRA AL TOTAL NUMÉRICO`.
- **Armamento recalculado, cálculo propio** —
  **ventana de 127** tras FE-004 y FE-001: hechos propios de 127 → **0** en todas las categorías de armamento; **detenidos en evento de aseguramiento: 3** (SLP, por titular:
  «detiene a tres personas con armas y presunta droga»; arma sin cantidad); con las recuperaciones del boletín del 8-oct, todas **solo por resumen** (primera edición): largas **2** · sin categoría
  **1** (Zacatlán) · cartuchos 225 + 81 + 55 = **361** · cargadores 8 + 4 = **12** · detenidos 2 + 2 + 1 = **5**; con SLP, **8**.
  **Ventana de 126** tras `ARG-127-FE-001`, `-FE-003` y FE-004: cortas **4** · largas 10 − 5 = **5** · cartuchos 1,153 − 1,093 = **60** ·
  cargadores 60 − 47 = **13** · AEI **82** · detenidos **2**; Michoacán (`-REC-008`) añade **10 detenidos** por titular y **4 armas sin
  desglose solo por resumen** si se confirma su ventana; Sombrerete, contradicho, no se integra.
- **Sentencia posible de la ventana de 127**: Querétaro, Manuel «N», amenazas y daños dolosos, Corregidora, 3 años —boletín oficial con
  fecha 2026/10/08 en la ruta, hora no fijada (127 abrió el 8-oct 08:56)—. **No se integra a 128**; si se fija dentro de 127, su conteo
  judicial pasa de 0 a 1. Óscar Eduardo «N» (6-oct) y Juan Diego «N» (5-oct) son de ventanas anteriores.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV | NO REVISADA | SRIV (`site:fgebc.gob.mx`; último 4-oct) |
| Baja California Sur | NO REVISADA | SRIV (`site:`) | SRIV (`site:`) |
| Sonora | SRIV | SRIV (`site:`) | NO REVISADA (Cajeme, ya publicado) |
| Chihuahua | SRIV · REC Juárez · REC Cuauhtémoc · Borja, posible duplicidad | SRIV (`site:`) | SRIV estatal · **FGR, titular** (`DPE/4566`) · 8 años, solo medios |
| Sinaloa | **hecho** (penal, 2.ª riña) | NO REVISADA (el `site:` solo buscó el penal y Montecarlo) | NO REVISADA estatal · **FGR, titular** (`DPE/4574`) |
| Durango | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Coahuila | SRIV | NO REVISADA | NO REVISADA |
| Nuevo León | SRIV | SRIV (`site:`) | SRIV · **solo medios** (28 años, 9-oct) |
| Tamaulipas | SRIV · REC Río Bravo | SRIV (`site:fgjtam.gob.mx`, hasta FGJE-376) | SRIV |
| San Luis Potosí | SRIV | NO REVISADA (`site:` sin páginas del dominio) | NO REVISADA |
| Zacatecas | REC Huanusco · REC Sombrerete | SRIV (`site:`) | NO REVISADA |
| Jalisco | SRIV | SRIV | SRIV (`site:`) |
| Colima | SRIV (con reserva) | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Nayarit | SRIV | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Aguascalientes | SRIV | SRIV (`site:`) | SRIV (`site:`; titulares del 2-oct) |
| Michoacán | REC 12 cateos · REC Penjamillo | SRIV (`site:`) | SRIV (`site:`) |
| Guanajuato | **hecho** (Celaya) · REC Valle de Santiago | **hecho** (Celaya) | SRIV (`site:`) · **solo medios** (León) |
| Ciudad de México | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Estado de México | **hechos** (San José del Rincón, Naucalpan ×2) | NO REVISADA (dominio no confirmado) | NO REVISADA (`site:` sin boletines) |
| Morelos | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Puebla | SRIV · REC Zacatlán | SRIV | SRIV (`site:`) |
| Tlaxcala | SRIV | **NO REVISADA** (segunda edición) | SRIV (`site:pgjtlaxcala.gob.mx`) |
| Hidalgo | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Querétaro | NO REVISADA (genérica) | NO REVISADA | SRIV en ventana · **3 boletines oficiales previos** |
| Veracruz | SRIV · REC Papantla · seguimiento Coatzacoalcos | NO REVISADA (`site:` sin páginas del dominio) | SRIV · agregado FGE solo por republicadores |
| Tabasco | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Guerrero | encargo (El Balcón) | SRIV | SRIV (`site:`; titular del 8-oct) |
| Chiapas | NO REVISADA (búsqueda genérica) | SRIV (`site:`) | NO REVISADA (dominio no confirmado) |
| Oaxaca | **hecho** (Pinotepa, por el coordinador) | SRIV (`site:`) | SRIV (`site:`) |
| Campeche | SRIV | NO REVISADA (sin `site:`) | NO REVISADA (dominio no confirmado; Lerma solo medios) |
| Yucatán | NO REVISADA | NO REVISADA | NO REVISADA |
| Quintana Roo | SRIV | SRIV (`site:`) | SRIV (`site:`; último 29-jun) |

**Sentencias: 21 de 32 + FGR; 11 `NO REVISADA`** (Son, Sin · Coah, SLP, Zac · Col, Nay · Edomex · Chis, Camp, Yuc). **Armamento: 20 de 32**
(NO REVISADA: BC, Sin, Coah, SLP, Col, Nay, Edomex, Tlax, Qro, Ver, Camp, Yuc). **Alto impacto: 28 de 32** (NO REVISADA: BCS, Qro, Chis, Yuc).
**Criterio único** (fijado tras `editor-duplicidad`): `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial (o, en alto
impacto, búsqueda dirigida en medios de la entidad); dominio no devuelto o búsqueda genérica = `NO REVISADA`.

## 10. Hechos vistos y NO fichados, con motivo

| Hecho | Motivo |
|---|---|
| Oaxaca, Ocotlán de Morelos, «disparos» (Heraldo de México 2026/10/9) | Nota de jornada, forma de *liveblog*; sin cifras ni hora |
| Tlaxcala, Amozoc–Perote, falsos policías contra una familia | Fecha no fijada, sin URL fechada, sin muertos |
| Puebla, Tehuitzingo, «10 muertos» (Telemundo) | Sin fecha en la ruta; no verificado |
| Edomex, Ecatepec, 2 cuerpos en cajuela | «8-oct» por resumen, sin fecha ni fuente nominal |
| SLP, 9 detenidos por robo al autotransporte (`ARG-125-015`) | Cifras de armas discrepantes entre medios, solo por resumen; candidato a revisión en 129 |
| Nayarit, Santa María del Oro, 11 granadas (Infobae 2026/10/03) | Anterior; posible ya publicado |
| Tabasco, boletín del 8-oct, Centro, 4 cateos | Cualitativo; posible duplicidad con La Huerta |
| FIRT Olmeca, 16 detenidos | Agregado del 5 al 8-oct |
| Escuinapa, 10 armas y 20 AEI | 9-sep |
| Nonoava, hechos de septiembre | Otros hechos |
| CDMX, Álvaro Obregón, 4-oct; Morelos, 8 asesinados, 1-oct | Anteriores; no verificados contra el índice |

## 11. Desglose de cálculos propios

- Duración: 9-oct 07:20 → 10-oct 09:08 = **25 h 48 min** = 25,8 h. Densidad: 6 / 25,8 = **0,23**.
- Muertos en hechos propios: 3 (Pinotepa, por titular, contradicho: 8 si son 2) + 2 + 2 + 1 + 1 = **9**; en rojos 3 + 2 + 2 = **7**. Heridos: 1 (San José del
  Rincón) + 1 (Valle Dorado) = **2**.
- Recuperaciones por color de origen: 🔴 2 (Papantla, Penjamillo) · 🟡 1 (Huanusco) · 🟢 7 = **10**.
- Armamento recalculado de las ventanas de 127 y 126: ver §8.
- Recompensa de El Balcón: 1.5 mdp, por titular.

## 12. Fuentes por ficha

- **`ARG-128-001`** — La Razón 2026/10/10; Infobae 2026/10/10; El Mañana 2026/10/9; Primera Línea 2026/10/09; Noticierog y La Onda Oaxaca 2026/10 (titulares con «tres muertos»); El Universal y El Universal Oaxaca, El Siglo de Torreón, El Sol de Chiapas, Billie Parker, MexNoticias, Noventagrados, Milenio (video) (s/f).
- **`ARG-128-002`** — AM 2026/10/09; Noticieros en Línea 2026/oct/09; Primer Plano Irapuato 2026/10/10; NPI, Ágora (s/f). Deslinde: Crónica 2026/10/06, «Detienen a 2 personas y aseguran 3 armas de fuego en Celaya y Villagrán» (otro hecho).
- **`ARG-128-003`** — Quadratín Edomex; Cuestión de Polémica (s/f).
- **`ARG-128-004`** — deslinde: La Silla Rota 2026/9/24, «Riña en penal El Castillo de Mazatlán deja dos muertos» (otro hecho). Fuentes: Proceso 2026/10/9; El Financiero 2026/10/09; La Silla Rota 2026/10/9; Reforma, Excélsior, N+ (s/f); Los Noticieristas 2026/10; Infobae 2026/10/09 (crisis penitenciaria).
- **`ARG-128-005` / `-006`** — Infobae 2026/10/09; Seunonoticias 2026/10/09; La Nigua (s/f). Infobae «EN VIVO» 9-oct: *liveblog*, no fecha el hecho.
- **`ARG-128-REC-001`** — N+; XEU 1436162; La Nigua; Veracruz Informa; Veracruz en Red (s/f).
- **`ARG-128-REC-002`** — Reforma ar3291046; El Universal; Diario.mx 2026/oct/08; Quinto Poder 2026/10/08; El Vigía 2026/10/09.
- **`ARG-128-REC-003` a `-007`** — Milenio (acciones del 8-oct en la ruta); Línea Directa 2026-10-09; SICOM, Candelero, RED113, Tallapolítica, Ahora Noticias (republicadores). Río Bravo: Hoy Tamaulipas 629359, El Mañana 6195024. Zacatlán: Infobae 2026/10/09, UnoTV, Capital México.
- **`ARG-128-REC-008`** — Crónica 2026/10/09; Infobae 2026/10/10; Esfera 2026/10/09; Sociedad Noticias 2026/10/09; MVS 2026/10/8; Milenio; Quadratín; Meganoticias 777096; La Voz de Michoacán.
- **`ARG-128-REC-009`** — MiMorelia n5594093; Contramuro; Quadratín (s/f).
- **`ARG-128-REC-010`** — La Nigua; Express Zacatecas; NTR Zacatecas 2026/10; Corresponsales; Milenio (acciones del 7-oct).
- **Borja (no fichado)** — El Diario de Chihuahua 2026/oct/07 (845151) y 2026/oct/08 (845773).
- **Coatzacoalcos (no fichado)** — Golpe Político 2026/10/09; Liberal; Diario de Xalapa; N+; Municipio Sur 2026/10/06; La Silla Rota 2026/10/9.
- **Sentencias** — FGR, listado estatal (`fgr.org.mx`; los folios DPE aparecen **solo en el resumen del buscador** y no se publican, regla de `ARG-115-FE-005`); La Silla Rota 2026/10/9 y Correo 2026/oct/09 (León); MVS 2026/10/9 (NL, 28 años); El Diario de Chihuahua 2026/oct/09 (8 años); La Política en Rosa y Hora Cero 2026/10/09 (agregado FGE Veracruz); fiscaliageneralqro.gob.mx 2026/10/08, /10/06, /10/05 (Querétaro); fiscaliaguerrero.gob.mx, portada (Tlapehuala); Golpe Político 2026/10/08 (Veracruz, 150 años).

## 13. Los dos controles editoriales — ejecutados sobre la versión estable, los dos con «CORREGIR»

Racha: **catorce pases consecutivos, catorce «CORREGIR»** (trece hasta 127 + este). Lanzados en paralelo sobre el borrador validado y
commiteado (`7810da0`); **el borrador no se tocó mientras corrían**. Los informes citan la numeración del borrador; tras ellos se retiraron
`ARG-128-007` y `ARG-128-REC-011` **sin renumerar** (los ARG-ID retirados no se reutilizan).

**`procedencia-cifras`** (25 búsquedas) — **CORREGIR**. Hallazgos y disposición:

| # | Hallazgo | Disposición |
|---|---|---|
| A1-A3 | Montecarlo, SLP y Ojocaliente: segunda edición solo por resumen | **Corregido**: `ARG-128-FE-004`; recálculo en §8 |
| 1 | Pinotepa, «3 muertos» citable por cuatro titulares | **Corregido**: marca de resumen retirada de la cifra; contradicción mantenida |
| 3 | Cruce 13a. o 15a. Sur | **Corregido**: declarado contradicho |
| 4 | Punzocortante, citable por titular | **Corregido** |
| 9 | San José del Rincón: fecha solo por resumen | **Corregido en parte**: marca `FRONTERA` y reserva; **se mantiene como hecho propio** (ver abajo) |
| 11-12 | Celaya: «armas» en titular frente a «un arma» por resumen | **Corregido**: fila `ARG-128-ARM-001` cualitativa; total de armas 1 → **0** |
| 16 | Coatzacoalcos: vinculación ya titulada el 6-oct | **Corregido**: retirado como hecho; seguimiento en §6 |
| 19 | «Hospital Civil» no respaldado | **Corregido** |
| 20-21 | Río Bravo: cifras en título y panel sin marca | **Corregido** |
| 24 | Juárez: colonia | **Corregido**: fracc. Guanajuato, sin verificar que sea el mismo cateo |
| 26 | Valle de Santiago: corporación | **Corregido**: no confirmada |
| 29 | Michoacán: fecha y vínculo inferidos | **Corregido**: declarados `INFERENCIA DE ARGOS`; origen 126 o 127 |
| 32-33 | Sombrerete: detenidos no atribuidos; publicación del 8-oct | **Corregido** |
| 34 | Portada 5: «vencido el plazo de tres días» | **Corregido**: retirado; la recompensa se sostiene en tres titulares del 9-oct (equipo de encargos) |
| 38 | Heridos: 3 si Pinotepa son 2 muertos y 1 lesionada | **Corregido**: «8 si son 2» declarado |
| 45 | Cobertura con criterio desigual | **Corregido** (con `editor-duplicidad` #10) |

**`editor-duplicidad`** (sin búsquedas) — **CORREGIR**. Hallazgos y disposición:

| # | Hallazgo | Disposición |
|---|---|---|
| 1 | `ARG-128-007` es seguimiento, no hecho | **Corregido**: retirado; propios 7 → **6**, 🟢 1 → **0**, entidades 5 → **4** |
| 2 | `REC-008` repite datos de `ARG-127-REC-001` y afirma 1 vs 10 sin respaldo | **Corregido en parte**: se mantiene como ficha de la **detención** (evento distinto de la confrontación, regla «un delito y su detención son dos eventos»); vínculo marcado inferencia; 1 frente a 10 `NO ARBITRADO`, sin sumar |
| 3 | Deslinde de `-004` publicaba datos de `ARG-127-004` (edad, pistolas) | **Corregido**: retirados del cartelón; quedan en §5 |
| 4 | Folios DPE solo por resumen | **Corregido**: retirados del cartelón |
| 5 | «Módulos 4 y 5», «tres días», recompensa | **Corregido**: los dos primeros retirados; la recompensa, con tres titulares |
| 6 | San José del Rincón sin ancla de fecha | **No se retira** (ver abajo); marca `FRONTERA` y ★★☆☆☆ |
| 7 | Boletín del 8-oct como `-REC-` frente a `FRONTERA` | **Corregido en parte**: origen «127 o 126, hora no fijada»; se mantiene `-REC-` (§7) |
| 8 | Borja con fuente única | **Corregido**: retirado; `POSIBLE DUPLICIDAD` |
| 9 | Penjamillo 🟡 | **No se corrige** (ver abajo); título sin «en operativo» |
| 10 | Cobertura | **Corregido**: alto impacto 28, armamento 20, criterio único |
| 11 | 3 frente a 4 hechos de hora no fijada | **Corregido**: cuatro de seis con `FRONTERA` |
| 12 | Archivo de fuentes, índice y pendientes | **Corregido** (el archivo existía tras el borrador; índice y pendientes, al cierre) |
| 13 | Portada y Conclusiones sobre los mismos hechos | **Corregido**: Conclusiones rehechas sobre Celaya, Penjamillo, San José del Rincón, Huanusco, Papantla, Juárez, Valle de Santiago, Sombrerete y sentencias |
| 14 | Valoración explicaba colores y el mecanismo `-REC-` | **Corregido**: remite por ARG-ID y dice qué vigilar |
| 15 | Conclusión 3 citaba mal | **Corregido** |
| 17 | Bloque «vistas por primera vez» | **Corregido**: una línea; arbitraje de Querétaro en §8 |
| 18-20 | Muertos, recuentos de fuentes, Cuauhtémoc 100 kg | **Corregido** |
| 21-22 | Móvil divergente; `.txt` sin recuadros ni `-REC-` | **Corregido**: regenerados; **`gen-texto.py` reparado** (dos expresiones regulares) |
| 16 | Totales en tres sitios | **No se corrige**: precedente de 126 y 127 |

**Hallazgos que se deciden no corregir, con motivo** (regla del control editorial):

- **San José del Rincón (`ARG-128-003`) se mantiene como hecho propio.** Ninguna edición anterior lo vio; dos titulares sostienen el saldo; el
  día «viernes 9» solo por resumen. Retirarlo dejaría un homicidio múltiple sin edición: la regla de frontera manda integrarlo en la primera
  que lo ve, con marca. **Si aparece una fuente que lo fije el 8-oct, se traslada a 127 por fe de erratas.**
- **Penjamillo (`ARG-128-REC-009`) se mantiene 🔴.** Los tres titulares describen a civiles armados que disparan contra la Guardia Civil
  («embosca», «repele agresión», «ataque a policías»); ninguno describe una acción del Estado repelida. «En operativo» venía solo del resumen.
  La regla de quién inicia da rojo.

**Segundo pase** — `validar.js` → **validación OK** (escritorio); `gen-movil.py` → **validación OK** (móvil); `.txt` con las 16 fichas y los
tres recuadros. Sin presupuesto de búsqueda para un segundo pase de `procedencia-cifras` (200 de 200).

**Segundo pase de `editor-duplicidad`** (sin búsquedas, sobre `8f99170`) — **CORREGIR**, hallazgos menores; ninguna duplicidad ni rastro de
lo retirado; aritmética de §8 y del cartelón verificada.

| # | Hallazgo | Disposición |
|---|---|---|
| H1 | Heridos si Pinotepa son 2 muertos | **Corregido**: «8 muertos y 3 heridos» |
| H2 | Conclusión 1 atribuía a Celaya disparos de autor no determinado | **Corregido** |
| H3 | Deslindes de la riña del 24-sep y de Celaya–Villagrán sin fuente en el archivo | **Corregido**: fuentes fechadas en §12; «(3 armas)» retirado del cartelón |
| H4 | Pinotepa: cuatro titulares y recuento de fuentes | **Corregido**: Regional 10 (Noticierog, La Onda Oaxaca, MexNoticias y Noventagrados con «tres» en titular, según `procedencia-cifras`); «disputa entre células» ya marcada por resumen |
| H5, H12 | Indicadores contradecían el panorama y repetían el renglón de cobertura | **Corregido**: el boletín queda solo en el indicador de cobertura |
| H6 | Fe de erratas en el cartelón | **No se corrige**: instrucción permanente del destinatario (ARGOS 109), «sin fe de erratas en el cartelón»; quedan en §8 y en el índice |
| H7 | Detenidos de SLP en el recálculo | **Corregido**: 3 por titular |
| H8 | Conclusiones 2 y 3 | **Corregido** |
| H9 | Ventana de Sombrerete | **Corregido**: 126 o 125 |
| H10, H11 | Pendientes sin disposición; Coatzacoalcos cerrado con fecha sin arbitrar | **Corregido** en `_pendientes.md` |
| H13 | Valoración 3 repetía la función de la portada; totales en tres sitios | **Corregido** lo primero; lo segundo, **no**: precedente de 126 y 127 y bloque obligatorio de iconografía |
| H14 | Texto fijo del generador móvil («ARGOS 97», «los 1 ARG-ID») | **No se corrige en esta edición**: pasa a deuda de método |

Tras este pase: `validar.js` y `gen-movil.py` → **validación OK**. No se lanzó un tercer pase: los hallazgos eran de redacción y referencia.

## 14. Herramientas

`tools/datos-argos-128.py` (generador único) → `reports/argos-2026-10-10.html`; `tools/gen-movil.py 128 2026-10-10 127 2026-10-09 09:08`;
`tools/gen-texto.py`; `node tools/validar.js reports/argos-2026-10-10.html 2026-10-09 2026-10-10` → **validación OK**.
El generador acepta ahora `color` y `fecha` por fila de armamento (127 los tenía fijos en verde y 8-oct). `gen-texto.py` reparado: incluye los
recuadros y las fichas `-REC-` (deuda de método 5 de 127).

## 15. Lecciones de método (no van al cartelón)

1. **El barrido regional no trajo los dos rojos más graves del Sureste y del Centro**; una búsqueda nacional del coordinador por día de la
   semana los halló. Para 129: **cada equipo regional debe abrir con una búsqueda por día de la semana y entidad** antes del triaje de
   portales, y el coordinador debe reservar **una búsqueda nacional por día de la ventana**.
2. **Tlaxcala armamento, `NO REVISADA` por segunda edición**: dominio de la SSC no confirmado. En 129 se busca primero el dominio real.
3. **Yucatán, `NO REVISADA` en los tres módulos**: encabeza el triaje de 129.
