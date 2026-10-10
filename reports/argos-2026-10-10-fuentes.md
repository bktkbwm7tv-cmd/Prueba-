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
| Densidad (hechos/h) | 0,04 | 0,30 | 0,16 | 0,40 | 0,27 | **0,27** (7 / 25,8, cálculo propio) |

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
| **Balleza / San Francisco de Borja** | **Dos hechos**: El Diario de Chihuahua 2026/oct/08, titular «Dejan dos enfrentamientos cuatro muertos»; y 2026/oct/07, titular «enfrentamiento entre soldados y sicarios deja dos muertos» (tramo Guachochi–San Francisco de Borja). Balleza ya publicado (`ARG-126-REC-004`); **Borja → `ARG-128-REC-011`** 🟡 (quién inició, no acreditado). Abatidos de Balleza: sin identificar |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| **Autolavado de Flores Magón** (`ARG-127-002`) | **3 muertos** confirmados por titulares. **Heridos**: 4 (Los Noticieristas), 5 (Luz Noticias, Sinaloahoy), 3 (Reporte18), cada uno en titular — **no se arbitra ni se suma**. Un menor de 17 años entre los muertos según Los Noticieristas: **no se reproduce el nombre**. Sin detenidos. Vínculo con el doble homicidio del 6-oct: sin información |
| **La Huerta** (`ARG-127-REC-003`) | **Duplicidad probable**: la detención de dos personas por la SSPC en Centro (Diario de Tabasco 2026/10/08; Quadratín: km 10 Carmen–Villahermosa, «a la altura del fracc. La Huerta») es el mismo evento del boletín del 7-oct. **Sigue fuera de todos los totales.** Quadratín: 317 cartuchos y granadas, solo por resumen, con desglose que no suma: no adoptado |
| **Cosalá** (`ARG-127-REC-004`) | **2,693 kg = 2.6 t truncado** (Noroeste por resumen; Sinaloahoy por titular, 2.6 t). El titular «cinco laboratorios en Jalisco, Nayarit y Sinaloa» es de **mayo de 2026** (Gabinete, Proceso 2026/5/17): **no aplica a Cosalá. Cerrado** |
| **Penjamillo** | **Fijado: tarde del miércoles 7-oct**, antes de las 20:30 de la primera publicación (MiMorelia, por resumen; Contramuro «la tarde de este miércoles»). Ventana 126 o 125 → **`ARG-128-REC-009`** 🔴 |
| **Xalisco / Ópalo** (`ARG-125-003`) | Sin cifra oficial ni identificaciones (la fiscal espera las confrontas genéticas). Ópalo: sin respaldo oficial del vínculo. «33 cráneos» (SDP): no adoptado |
| **Casas Grandes** (`ARG-126-REC-003`) | **El hecho es en la col. Infonavit Casas Grandes, Ciudad Juárez**, no en el municipio. **Móvil**: titular de Diario de Juárez y El Diario de Chihuahua 2026/oct/07, «Balacera no fue por secuestro, fue conflicto por no pagar drogas»; la Fiscalía Zona Norte descarta la mujer secuestrada (resumen). Heridos: 2 frente a 3. **Fe de erratas** `ARG-128-FE-003` |
| **Coatzacoalcos** (Pamucé) | **Vinculación a proceso de los 5** (Golpe Político 2026/10/09) → `ARG-128-007` 🟢 |
| **Huanusco** (pista NTR) | Padre de la presidenta municipal, 8-oct → `ARG-128-REC-002` 🟡 |
| **Zihuatanejo · Mixtequilla · 26 extranjeros · Comonfort · Hermosillo** | **`NO REVISADOS`**: el equipo agotó su tope. Pasan a 129 |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Pinotepa Nacional** (`ARG-128-001`) | Hallado por el coordinador. Viernes 9-oct por la tarde: dentro de ventana. **🔴 por víctima periodista** (Hamurabi Huesca Manzano, director de Pinotepa Comunica, por titular de seis medios) **y víctimas múltiples** (3, solo por resumen; otra versión: 2 muertos y una mujer lesionada). La hipótesis de la FGEO (otro blanco) **no baja el color**: la lista roja nombra al periodista como víctima, no como blanco |
| **San José del Rincón** (`ARG-128-003`) | Hallado por el coordinador. ~09:30 del viernes 9-oct, solo por resumen; **ninguna URL con fecha**. Se integra con confianza ★★☆☆☆ |
| **Segunda riña de El Castillo** (`ARG-128-004`) | «El viernes por la mañana»; la SSP lo comunica ~09:25 (resumen). Nada la sitúa antes de las 07:20 y ARGOS 127 consultó a las 07:20-07:30 sin verla: **`FRONTERA DE VENTANA`, integrada en 128** |
| **Naucalpan** (`ARG-128-005`, `-006`) | Publicado el 9-oct (Infobae, Seunonoticias), «por la noche»: la noche del jueves la infiere el resumen, no la fuente. **`FRONTERA`, integrados en 128**, dos fichas: el titular dice «dos hechos distintos» |
| **Celaya** (`ARG-128-002`) | 🟡 por **persecución** con detonaciones, que la lista amarilla nombra; quién disparó, sin precisar. 1 arma de fuego y 2 detenidos por titular → `ARG-128-ARM-001` (sin categoría) |
| **Michoacán, 12 cateos** (`ARG-128-REC-008`) | Publicado el 9 y 10-oct; los «dos agentes heridos» del titular lo atan al cateo de Sol Naciente, madrugada del 8-oct: **ventana de origen ARGOS 126**. Detención y confrontación, dos eventos |
| **Sombrerete** (`ARG-128-REC-010`) | Renglón del boletín del 7-oct (FGR) que ni 126 ni 127 fichó. **Cifras contradichas** (185 frente a 39 detonadores): no se integra al recálculo |
| **Escuinapa** (10 armas, 1,900 cartuchos, 20 AEI) | **9-sep**: descartado por fecha (verificado por el coordinador) |
| **FIRT Olmeca, 16 detenidos** (Diario de Tabasco 2026/10/09) | Agregado estatal del 5 al 8-oct; incluye la detención de La Huerta: no fichado |

## 8. Fe de erratas (no va al cartelón)

*Se completa con el dictamen de `procedencia-cifras` (§13).*

- **`ARG-128-FE-001`** — sobre **ARGOS 127**: siete hechos de su ventana no publicados (`ARG-128-REC-001` a `-007`). Efecto sobre su
  semáforo: rojos 2 → **3** (Papantla), amarillos 2 → **3** (Huanusco), verdes 2 → **7** (Río Bravo, Juárez, Valle de Santiago, Zacatlán,
  Cuauhtémoc).
- **`ARG-128-FE-002`** — sobre **ARGOS 126**: cuatro hechos de su ventana —o de la de 125, hora no fijada— no publicados (`ARG-128-REC-008`
  a `-011`). Efecto sobre el semáforo de 126 tras `ARG-127-FE-001`: rojos 1 → **2** (Penjamillo), amarillos 2 → **3** (Borja), verdes 7 → **9**
  (Michoacán, Sombrerete). Si Penjamillo o Borja resultan de la ventana de 125, se trasladan allí.
- **`ARG-128-FE-003`** — sobre **`ARG-126-REC-003`** (Casas Grandes): el titular «presuntos secuestradores» queda **contradicho**; el
  móvil publicado es una deuda de drogas (dos titulares regionales del 7-oct) y la Fiscalía Zona Norte descarta la mujer secuestrada.
  **Lugar**: col. Infonavit Casas Grandes, Ciudad Juárez. El color 🟡 no cambia.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV | NO REVISADA | SRIV (`site:fgebc.gob.mx`; último 4-oct) |
| Baja California Sur | NO REVISADA | SRIV (`site:`) | SRIV (`site:`) |
| Sonora | SRIV | SRIV (`site:`) | NO REVISADA (Cajeme, ya publicado) |
| Chihuahua | REC Borja · REC Juárez · REC Cuauhtémoc | SRIV (`site:`) | SRIV estatal · **FGR, titular** (`DPE/4566`) · 8 años, solo medios |
| Sinaloa | **hecho** (penal, 2.ª riña) | SRIV (`site:sspsinaloa.gob.mx`) | NO REVISADA estatal · **FGR, titular** (`DPE/4574`) |
| Durango | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Coahuila | SRIV | NO REVISADA | NO REVISADA |
| Nuevo León | SRIV | SRIV (`site:`) | SRIV · **solo medios** (28 años, 9-oct) |
| Tamaulipas | SRIV · REC Río Bravo | SRIV (`site:fgjtam.gob.mx`, hasta FGJE-376) | SRIV |
| San Luis Potosí | SRIV | SRIV (`site:`, débil) | NO REVISADA |
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
| Veracruz | **hecho** (Coatzacoalcos) · REC Papantla | SRIV | SRIV · agregado FGE solo por republicadores |
| Tabasco | SRIV | SRIV (`site:`) | SRIV (`site:`) |
| Guerrero | encargo (El Balcón) | SRIV | SRIV (`site:`; titular del 8-oct) |
| Chiapas | SRIV | SRIV (`site:`) | NO REVISADA (dominio no confirmado) |
| Oaxaca | **hecho** (Pinotepa, por el coordinador) | SRIV (`site:`) | SRIV (`site:`) |
| Campeche | SRIV | NO REVISADA (sin `site:`) | NO REVISADA (dominio no confirmado; Lerma solo medios) |
| Yucatán | NO REVISADA | NO REVISADA | NO REVISADA |
| Quintana Roo | SRIV | SRIV (`site:`) | SRIV (`site:`; último 29-jun) |

**Sentencias: 21 de 32 + FGR; 11 `NO REVISADA`** (Son, Sin · Coah, SLP, Zac · Col, Nay · Edomex · Chis, Camp, Yuc). **Armamento: 23 de 32**
(NO REVISADA: BC, Coah, Col, Nay, Edomex, Tlax, Qro, Camp, Yuc). **Alto impacto: 29 de 32** (NO REVISADA: BCS, Qro, Yuc).

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

- Duración: 9-oct 07:20 → 10-oct 09:08 = **25 h 48 min** = 25,8 h. Densidad: 7 / 25,8 = **0,27**.
- Muertos en hechos propios: 3 (Pinotepa, por resumen) + 2 + 2 + 1 + 1 = **9**; en rojos 3 + 2 + 2 = **7**. Heridos: 1 (San José del
  Rincón) + 1 (Valle Dorado) = **2**.
- Recuperaciones por color de origen: 🔴 2 (Papantla, Penjamillo) · 🟡 2 (Huanusco, Borja) · 🟢 7.
- Armamento de la ventana de 127 tras `ARG-128-FE-001` (solo hechos con cifra, cálculo propio; pendiente del dictamen sobre Montecarlo y
  SLP): cortas 2 (SLP) · largas 2 (Río Bravo) · sin categoría 1 (Zacatlán) · cartuchos 65 + 225 + 81 + 55 = **426** · cargadores 2 + 8 + 4 =
  **14** · detenidos 2 + 2 + 2 + 1 = **7**. Las pistolas 9 mm del penal (`ARG-127-004`) no tienen cifra citable: no se integran.
- Armamento de la ventana de 126 tras `ARG-128-FE-002`: las 4 armas de Michoacán (`-REC-008`) son **solo por resumen y sin desglose**; los
  10 detenidos, por titular. Sombrerete, contradicho: no se integra.
- Recompensa de El Balcón: 1.5 mdp, por titular.

## 12. Fuentes por ficha

- **`ARG-128-001`** — La Razón 2026/10/10; Infobae 2026/10/10; El Mañana 2026/10/9; Primera Línea 2026/10/09; El Universal y El Universal Oaxaca, El Siglo de Torreón, El Sol de Chiapas, Billie Parker, Milenio (video) (s/f).
- **`ARG-128-002`** — AM 2026/10/09; Noticieros en Línea 2026/oct/09; Primer Plano Irapuato 2026/10/10; NPI, Ágora (s/f).
- **`ARG-128-003`** — Quadratín Edomex; Cuestión de Polémica (s/f).
- **`ARG-128-004`** — Proceso 2026/10/9; El Financiero 2026/10/09; La Silla Rota 2026/10/9; Reforma, Excélsior, N+ (s/f); Los Noticieristas 2026/10; Infobae 2026/10/09 (crisis penitenciaria).
- **`ARG-128-005` / `-006`** — Infobae 2026/10/09; Seunonoticias 2026/10/09; La Nigua (s/f). Infobae «EN VIVO» 9-oct: *liveblog*, no fecha el hecho.
- **`ARG-128-007`** — Golpe Político 2026/10/09; Liberal (s/f). Antecedentes: Municipio Sur 2026/10/06, Noticias Veracruz 2026/10/05.
- **`ARG-128-REC-001`** — N+; XEU 1436162; La Nigua; Veracruz Informa; Veracruz en Red (s/f).
- **`ARG-128-REC-002`** — Reforma ar3291046; El Universal; Diario.mx 2026/oct/08; Quinto Poder 2026/10/08; El Vigía 2026/10/09.
- **`ARG-128-REC-003` a `-007`** — Milenio (acciones del 8-oct en la ruta); Línea Directa 2026-10-09; SICOM, Candelero, RED113, Tallapolítica, Ahora Noticias (republicadores). Río Bravo: Hoy Tamaulipas 629359, El Mañana 6195024. Zacatlán: Infobae 2026/10/09, UnoTV, Capital México.
- **`ARG-128-REC-008`** — Crónica 2026/10/09; Infobae 2026/10/10; Esfera 2026/10/09; Sociedad Noticias 2026/10/09; MVS 2026/10/8; Milenio; Quadratín; Meganoticias 777096; La Voz de Michoacán.
- **`ARG-128-REC-009`** — MiMorelia n5594093; Contramuro; Quadratín (s/f).
- **`ARG-128-REC-010`** — La Nigua; Express Zacatecas; NTR Zacatecas 2026/10; Corresponsales; Milenio (acciones del 7-oct).
- **`ARG-128-REC-011`** — El Diario de Chihuahua 2026/oct/07 (845151) y 2026/oct/08 (845773).
- **Sentencias** — FGR, listado estatal (`fgr.org.mx`, `DPE/4566/2026`, `DPE/4574/2026`, `DPE/4537/2026`); La Silla Rota 2026/10/9 y Correo 2026/oct/09 (León); MVS 2026/10/9 (NL, 28 años); El Diario de Chihuahua 2026/oct/09 (8 años); La Política en Rosa y Hora Cero 2026/10/09 (agregado FGE Veracruz); fiscaliageneralqro.gob.mx 2026/10/08, /10/06, /10/05 (Querétaro); fiscaliaguerrero.gob.mx, portada (Tlapehuala); Golpe Político 2026/10/08 (Veracruz, 150 años).

## 13. Los dos controles editoriales

*Pendiente: se registran aquí al recibir los informes.*

## 14. Herramientas

`tools/datos-argos-128.py` (generador único) → `reports/argos-2026-10-10.html`; `tools/gen-movil.py 128 2026-10-10 127 2026-10-09 09:08`;
`tools/gen-texto.py`; `node tools/validar.js reports/argos-2026-10-10.html 2026-10-09 2026-10-10` → **validación OK**.
El generador acepta ahora `color` y `fecha` por fila de armamento (127 los tenía fijos en verde y 8-oct).

## 15. Lecciones de método (no van al cartelón)

1. **El barrido regional no trajo los dos rojos más graves del Sureste y del Centro**; una búsqueda nacional del coordinador por día de la
   semana los halló. Para 129: **cada equipo regional debe abrir con una búsqueda por día de la semana y entidad** antes del triaje de
   portales, y el coordinador debe reservar **una búsqueda nacional por día de la ventana**.
2. **Tlaxcala armamento, `NO REVISADA` por segunda edición**: dominio de la SSC no confirmado. En 129 se busca primero el dominio real.
3. **Yucatán, `NO REVISADA` en los tres módulos**: encabeza el triaje de 129.
