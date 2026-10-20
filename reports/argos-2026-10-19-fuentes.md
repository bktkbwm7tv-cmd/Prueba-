# ARGOS 137 — Archivo de fuentes

**Corte**: 2026-10-19 · **Ventana**: 18-oct 08:34 → 19-oct 11:05 CDMX (**26 h 31 min**; `WINDOW_DAYS = 2`) · **Densidad**: 18 hechos propios / 26,52 h = **0,68 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 11:05 CDMX). La orden de proceder llegó después; las consultas continuaron hasta la marca «Consulta» del cartelón. Los hechos posteriores a las 11:05 del 19 pertenecen a ARGOS 138.

Informes íntegros de los seis equipos, notas del coordinador e informes de los controles: `reports/argos-2026-10-19-equipos.md`. Plantilla de los equipos: `tools/plantilla-equipos-137.md`.

## 1. La base

- Clon con HEAD suelto en `60f2777` (quinta edición seguida). Se abrió `claude/argos-137` y se fusionó en *fast-forward* `main` (`b0558a3`), `claude/argos-129` … `-136`, en ese orden y sin conflicto. HEAD de partida: `1de5574`.
- `reports/`: 196 archivos, última edición `argos-2026-10-18` (ARGOS 136), como estaba previsto.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`**, 11:05. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**. Además, 16 servidores MCP de complementos no conectaron por el 403 del proxy (sin efecto en ARGOS).
- **Consulta de control** («ataque armado muertos "18 de octubre" 2026 México», en los dos modos): `standard` **ningún hecho del 18** (un bar de Morelos sin fecha: resultó de agosto); `extended`, Copanatoyac, Acapulco («jornada violenta»), Colima («El Español» y «Santos»), Monterrey y el *liveblog* del exfiscal. **Se mantuvo `extended` obligatorio.** Copanatoyac → `ARG-137-001`; Colima → `-007`; Monterrey → `-008`; Acapulco → `-013` (el resto de la «jornada» es de 136).
- **Presupuesto**: control 2 + ola (Noroeste 27, Noreste 25, Occidente 27, Centro 27, Golfo y federal 27, Sureste 26 = **159**) + **10 del coordinador** = **171**; `procedencia-cifras` **29** → **200 de 200**. `editor-duplicidad` no busca en la web.

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

| Renglón | Resultado |
|---|---|
| Decisión | **Ciclo A** (Noroeste + Centro), **por decisión del destinatario** («Proceda con las recomendaciones», 19-oct): **retoma la tabla de `CLAUDE.md`** (137 = A). Fin del desfase iniciado en 134. **138 = B, 139 = C** |
| Prioridad — armamento (18 `NO REVISADA` en 136) | **Saldadas por dominio propio (4)**: SLP (`seguridad.slp.gob.mx`; `sspc.slp.gob.mx` no existe), Nay (`ssypc.nayarit.gob.mx`, solo organigrama), Camp (`spsc.campeche.gob.mx`), Yuc (`ssp.yucatan.gob.mx`). **Por portal estatal (5)**: Coah (`coahuila.gob.mx`), Tamps (`tamaulipas.gob.mx`), Ver (`veracruz.gob.mx/seguridad`), Tab (`tabasco.gob.mx`), Oax (`oaxaca.gob.mx/comunicacion`). **Siguen `NO REVISADA` (9)**: Chih y Dgo (`ssp.chihuahua.gob.mx`, `ssp.durango.gob.mx`: el buscador devolvió *Diario de Cuyo*), Jal (`ssp.jalisco.gob.mx`), Col (`ssp.col.gob.mx`), Ags (`ssp.aguascalientes.gob.mx`), Mor (`ssp.morelos.gob.mx`), Tlax (`ssc.tlaxcala.gob.mx`), Hgo (`seguridad.hidalgo.gob.mx`), Qro (`ssc.queretaro.gob.mx`): **dominio no devuelto** |
| Prioridad — sentencias (15 `NO REVISADA` en 136) | **Saldadas (10)**: BCS (`pgjebcs.gob.mx`), Dgo (`fiscalia.durango.gob.mx`), Jal (`fiscalia.jalisco.gob.mx`), Col (`fgecolima.mx`), Edomex (`fgjem.edomex.gob.mx`, solo PDF antiguos; `fiscalia.edomex.gob.mx` no devuelve), Pue (`fiscalia.puebla.gob.mx`), Qro (`fiscaliageneralqro.gob.mx`), Oax (**`portal.fgeo.gob.mx`**; `fiscaliaoaxaca.gob.mx` no devuelve), Chis (`fge.chiapas.gob.mx`), QRoo (`fgeqroo.gob.mx`). **Siguen (5)**: Sin (`fiscaliasinaloa.gob.mx` y `.mx`: **décima edición sin devolver**), Gto (`fiscalia.guanajuato.gob.mx` no devuelve), Mor (`fiscalia.morelos.gob.mx` no devuelve), Hgo (`pgjhidalgo.gob.mx` no devuelve), Camp (`fgecam.gob.mx`: el buscador ignora el `site:`) |
| Prioridad — alto impacto de Aguascalientes | **Saldada**: dos consultas propias (Occidente), SRIV |
| Ciclo A — rendimiento | **Ninguna sentencia integrable.** Noroeste: BC, BCS, Chih, Dgo revisadas (SRIV); Son y Sin, dominio no devuelto. Centro: CDMX, Edomex, Pue, Tlax, Qro revisadas (SRIV; Querétaro con tres sentencias del 5, 6 y 8-oct, fuera de ventana); Mor y Hgo, dominio no devuelto. **Lo que aportó**: Durango y Querétaro con ruta fechada del dominio (la portada de `fiscalia.durango.gob.mx` lista sentencias del 5 y 7-oct); BCS por primera vez por dominio propio |
| Regresión por rotación | Sentencias: Son, Zac, Gto (además de Sin, Mor, Hgo, Camp) y Gro, Yuc pasan a `NO REVISADA`. Armamento: BC, BCS, Son, NL, CDMX, Edomex, Pue, Gro, Chis pasan a `NO REVISADA`. **Prioridad sobre el ciclo en 138** |

**Dominios corregidos para las plantillas**: Oaxaca fiscalía **`portal.fgeo.gob.mx`** · SLP seguridad **`seguridad.slp.gob.mx`** · BCS procuraduría **`pgjebcs.gob.mx`** · Colima fiscalía **`fgecolima.mx`** · Edomex fiscalía **`fgjem.edomex.gob.mx`** · Campeche seguridad **`spsc.campeche.gob.mx`** · Yucatán seguridad **`ssp.yucatan.gob.mx`**.

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **16, 17 y 18-oct** | **Agregado de tres días**, hallado **solo por la tercera forma** (título, sin `site:`): Milenio (`milenio.com/policia/acciones-relevantes-gabinete-de-seguridad-16-17-18-de-octubre-2026`), Ultranoticias, RED113, Tallapolítica, Certeza Diario, NX Noticias — **republicadores, no independientes**. Día suelto y rango en el dominio: SRIV. Ocho entidades; renglones de Nayarit (Tecuala) y Veracruz (Lerdo de Tejada) como filas atenuadas **`ARG-137-ARM-001` y `-002`**, sin ficha, `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total (Tecuala: ametralladora, granada y 1 detenido por titular de NTV; el resto por resumen); Quintana Roo (Mahahual), Sinaloa (Mazatlán, 1.5 t de marihuana), Michoacán (Cotija), Edomex (Jilotepec), CDMX (Tlalpan): vistos. **Criterio**: fila ARM atenuada solo si un titular fechado sostiene el dato; el resto, visto. Agregado de medios: 20,082 cartuchos, 227 cargadores, ≥22 armas (solo por resumen, no se imprime como dato) |
| **19-oct** | `SIN RESULTADO INDEXADO EN VENTANA` |
| `gabinetedeseguridad.gob.mx` | Indexado hasta marzo de 2026 (y el agregado del 17-19 oct de **2025**): SRIV |

**Defensa**, **Marina**, **GN**, **FGR** (`gob.mx/fgr`, 2017-2022): SRIV. Primera Región Naval (5-15 oct): anterior.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Acapulco** (`ARG-136-002`, `-003`) | Ninguna ruta con día; sábado 17 por resumen (17:41-18:00 y ~19:00-20:00). **Lesionados de `-002`: 3 en todas las notas** (Quadratín, Bajo Palabra, En Primer Plano, El Sur): el «4» de 136 no reaparece. `-003`: segunda fuente (En Primer Plano, El Sur); sin identificación. «Cinco muertos y tres heridos» (El Sur) = `-002` + `-003` + Héroes de Guerrero (`ARG-137-013`) |
| **Taxco** (`-008`, `-009`) | `-008`: fecha de la detención **no publicada**; el 16 es el día del anuncio (boletín nocturno, por resumen). `-009`: cumplimentada «el 16-oct en Taxco», por resumen; **vinculado a proceso** por un juez de control de Iguala (El Diario de Chihuahua 2026/oct/18, titular «procesan»; Reforma por resumen). Atribución a La Familia Michoacana: sigue solo por resumen. **El policía detenido no fue detenido «con él»**: es otro caso (Paintla, julio; La Plaza Diario) |
| **Exfiscal** (`-006`) | Hora del 17: **no fijada** (RND ~10:20 no corroborado). Audiencia inicial estatal el **domingo 18**: proceso en libertad; vinculación el **jueves 22-oct 10:00** (La Razón 2026/10/18 y 2026/10/19). **FGR lo detuvo a la salida** por traición a la patria → **seguimiento de `ARG-136-006`, fuera del semáforo** (la persona ya se contó en 136; `editor-duplicidad`, ronda 1, pase 5). Hora contradicha: sábado 17 en un receso (Pie de Página) o cerca de la medianoche del domingo (Excélsior), ambas por resumen. La Jornada 2026/10/18 (*slug* «vinculan a proceso») contradicha |
| **Cuauhtémoc** (`-REC-003`) | ~09:00 es del **hallazgo**, no del ataque; víctimas identificadas por resumen (21 y 23 años, desaparecidos desde el 15-oct) → **ventana de 135 o anterior**; `-REC-` sostenida |
| **SSP Sinaloa, «Cuatro civiles armados»** ↔ `ARG-135-ARM-001` | Línea Directa y Tus Buenas Noticias, **ruta 2026/10/16**: col. Industrial Bravo; 1 ametralladora 7.62, 2 pistolas .45, 1 de 9 mm; **420 cartuchos = 385 (7.62) + 25 (9 mm) + 10 (.45)**, por resumen. **El «417» no aparece en ninguna fuente.** Mismo aseguramiento que «Pokémon»: **probable, no probado** → `POSIBLE DUPLICIDAD` se mantiene; ver §8 |
| **Culiacán** (`-004`) | Colonia **sin arbitrar** (Estela Ortiz: Luz Noticias, Noroeste, Café Negro, Azteca; Ruiz Cortines: Línea Directa, Los Noticieristas, Extraoficial, Sinaloahoy). Esquina Fernando Cuén y Pablo Macías, junto al CECATI 32 (resumen) |
| **San Baltazar Tetela** (`-007`) | **2 detenidos** (18 y 22 años; La Jornada de Oriente, Curul, Ambas Manos, Paralelo19; Urbano en singular); a disposición de la Fiscalía por homicidio; **sin vinculación publicada**; corporación no fijada; hora del ataque no fijada («noche del viernes 16» en varias notas). **🟡 por decisión del destinatario** |
| **Maneadero** (`-005`) | Causa de muerte e identidad: no publicadas; el ~09:30 no se confirmó |
| **Linares** (`ARG-135-REC-001`) | Milenio (ruta sin fecha): «**la noche de este miércoles**» en el cuerpo de la nota, por resumen → el peso del fragmento va al **miércoles 14 (ventana de 133)**; rutas fechadas del 16-17 sin día. `DÍA CONTRADICHO` persiste. Herido: sin fuente que diga que murió |
| **Chiapa de Corzo** (`ARG-134-REC-002`) | «**Tarde noche de este miércoles**» 14-oct (Heraldo de México 2026/10/14, por resumen) → **ventana de 133**. Saldo: FGE preliminar 1 muerto y 2 lesionados; SSP 2 muertos y 1 grave; un medio 3: **contradicho**. Un detenido («Wilmar», por resumen) |
| **Tanquián** (`ARG-136-REC-002`) | **Ninguna autoridad nombrada confirma la adscripción a la GN** (N+, Potosinoticias, Emsavalles, La Nigua, Pulso: medios; En Serio Noticias: «un veracruzano»; `fiscaliaslp.gob.mx` sin boletín). **Regla del destinatario → 🟡** (ver §8). Además: enfrentamientos de la Guardia Civil Estatal la noche del sábado 17 (1 abatido, 1 herido, 2 detenidos, 4-5 vehículos; secretario general de Gobierno: disputa entre grupos) → **ventana de 136, 🟡/🟢: no recuperable** |
| **Recalcular 133** | Ver §8, `ARG-137-FE-003` |
| **Heredados** | Apatzingán (`-003` de 135): hora no fijada; titular de El Congresista con «16 de octubre» · Divina Providencia: **2** en cuatro de cuatro medios; el 3 de Milenio no se corrobora · Cachanillas: 4 cuerpos y restos (tres medios); Punto Norte 2026/10/18: «**van 10 cuerpos en tres días de búsqueda**» (titular, colectivo); sin cifra oficial · Nogales: sin cifra oficial · Ajuchitlán: séptima persona sin localizar (Infobae 2026/10/18) · Tepic: sin vinculación publicada · Hermosillo `-005`/`-006` de 135: no revisado · CDMX (SSC): sin comunicado · El Tívoli: no localizado · Tezontepec: segunda fuente con ruta (La Silla Rota 2026/10/13), lunes 12 ~19:40 · «El Tripa»: detención del 16-oct (Código QRO, AlertaQro, rutas del 16); Milenio dice 9-oct: contradicción abierta · Coquimatlán: 2 o 3, sin FGE · Tlalnepantla: no resuelto (hallado solo un hecho de Tlalnepantla, **Morelos**, 2-oct: no cotejado con la ficha) · Monterrey/Santa Catarina: sin novedad |
| **Sentencias** | Ensenada: publicada el 17-oct (Periódico Correo, CR Prensa), boletín no localizado: **ventana de 136**, sigue `PENDIENTE` · Hermosillo: 16-oct · Veracruz, comunicador: 15-oct (La Silla Rota, La Política en Rosa, Hora Cero) · FGR Cosoleacaque (Abigail y Armando «N», 4 años; **no confundir** con Cristopher «N», 2 años 6 meses) y Banderilla (resolución del **9-oct**): 14-16 oct · Tulantepec: individualización el **miércoles 21-oct**, sigue programada |
| **Colores pendientes** | San Baltazar Tetela: **🟡, decidido**. Tanquián: **🟡 por la regla** (no acreditada la GN); registrado en el cartelón como seguimiento. Patamban (`ARG-134-006`): representante de bienes comunales; rutas del 15-oct; la Fiscalía «no descarta» defensa del bosque, por resumen — **¿persona defensora?: decisión del destinatario**. Coatzacoalcos, San Blas Atempa, Iztapalapa, Cajeme: sin dato nuevo. **Nuevo**: Cuajinicuilapa (ver §7) |

## 6. Seguimientos sin cambio de ficha

Nogales (sin cifra oficial) · Orizaba (cateo del 13-oct; imputación posterior) · Otatitlán (exalcalde, 12-oct; no cotejado) · Coatzacoalcos (`ARG-134-011`) · Hermosillo · Iztapalapa (tianguis El Salado, 14-oct; col. Rodeo, 7-oct: anteriores) · Puebla, policía estatal en Tres Cerritos (16-oct; `ARG-134-005`).

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Copanatoyac** (`-001`) | Pista de control; «tarde del domingo» por resumen en dos fuentes; **ninguna ruta con fecha** → ★★☆☆☆. 🔴 por homicidio múltiple. Deslindado del homicidio de un coordinador del PT del mismo municipio |
| **Tlajomulco** (`-002`) | Ajeno del equipo Centro; búsqueda propia: madrugada del lunes 19 por resumen; sin ruta con fecha → ★★☆☆☆, `FRONTERA`. 🔴 |
| **Coatzacoalcos** (`-003`) | La Silla Rota **2026/10/18** fija el domingo; ~14:00 por resumen; la segunda muerte por titulares regionales (Vanguardia Veracruz, Diario Acayucan). 🔴 por homicidio múltiple; riña de pareja solo por resumen. Deslindado del pendiente de Coatzacoalcos |
| **Mazatlán, Fovissste Esperanza** (`-004`) | Búsqueda propia; Luz Noticias **2026-10-18**; hora no fijada → marca de día de apertura. 🔴 |
| **Tabasco, torso** (`-005`) | Golfo; El Universal (titulares) y Diario de Yucatán 2026/10/18; municipio contradicho (Teapa / Jalapa); cartulinas por titular, destinatario por resumen. 🔴 por restos humanos con mensaje (precedente `ARG-125-013`) |
| **Tulancingo** (`-006`) | Búsqueda de cierre; La Silla Rota **2026/10/19**; ~09:20-09:30 por resumen (antes de las 11:05); SEPH confirma que era su trabajador (titular de Criterio). **🔴 por víctima servidor público** |
| **Colima** (`-007`) | Occidente; **🟡 por el criterio de quién inicia**: operativo repelido según la «Mesa de Seguridad» (titulares de Portal Colima, AFmedios y Vadenuez; quién inició, por resumen); muertos del lado criminal no mueven el color. Marca de día de apertura |
| **Mazatlán, tarde violenta** (retirada) | Agregado de medios (Viva la Noticia; Luz Noticias 2026-10-18, «dos heridos tras ataques casi simultáneos»); **posible solapamiento con `-004`** → retirada del semáforo y de los totales (`editor-duplicidad`, ronda 1, pase 1); queda en el deslinde de `-004` |
| **Tijuana** (`-011`, `-017`) | Delito y detención en la misma ventana: **dos fichas**; la detención, por titular de un medio y contradicha por Opinia |
| **Juchitán, panteón** (visto) | **Entidad contradicha**: Azteca Guerrero y El Sur lo sitúan en **Juchitán, Guerrero** (Costa Chica); el equipo Sureste lo leyó como Oaxaca. Día solo por resumen; GN herido (Interacción). **No fichado**: `ENTIDAD Y DÍA NO FIJADOS`. Si una autoridad nombrada confirma que el agresor atacó a la GN → 🔴 |
| **Cuajinicuilapa, aspirante de Morena** (visto) | **Sábado 17, tarde** (~18:20-19:00, por resumen; FGE Guerrero abrió carpeta, titular de La Razón 2026/10/18) → **ventana de 136**. Aspirante a la coordinación municipal: **no es autoridad, servidor público, periodista ni persona defensora** → **lectura literal 🟡: no recuperable**. Esposa lesionada. **COLOR PREGUNTADO AL DESTINATARIO EN ESTA EDICIÓN, SIN RESPUESTA AL CIERRE**: queda 🟡. Precedentes: `ARG-108-REC-001` y `ARG-124-002` (🔴, excandidato y exregidor con cargo partidista), `ARG-131-REC-001` (🟡, exalcalde). Si el destinatario lo fija en 🔴, se recupera en 138 como `-REC-` (136: +1 rojo, +1 muerto) |
| **Celaya, agente de Tránsito** (`-REC-001`) | Occidente; ~05:00-05:30 del sábado 17 por resumen → **ventana de 135**. 🔴 por víctima autoridad |
| **Tecuala y Lerdo de Tejada** (`ARM-001`, `-002`) | Renglones del agregado federal 16-18 oct: **`EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`** → filas atenuadas, sin ficha, fuera del semáforo y del total (`editor-duplicidad`, ronda 1, pase 6). Celdas sin cifra citable: «n/d» |
| **«El Talibán» y cuatro** (`-REC-002`) | Hallado por `procedencia-cifras` (ronda 1); Proceso 2026/10/18; capturas del 16 al 18 solo por resumen → **evento anterior publicado durante el corte**, ficha `-REC-002` fuera de los totales (`editor-duplicidad`, ronda 2, pase 2, opción A) |
| **Hermosillo, Villa de Seris** (`-018`, `ARM-003`) | Ruta 2026/10/18 (El Imparcial); ~01:30 solo por resumen → misma marca de día de apertura que `-004`, `-005`, `-007`, `-008`, `-010`; una sola fuente: `ARM-003` fuera del total. **Criterio**: entra el hecho con ruta fechada del día de apertura; queda visto el que no la tiene (Irapuato) |
| **Vistos de la ventana de 136, no recuperables** | Irapuato, col. Miguel Hidalgo (~02:30 del domingo por resumen, sin ruta con fecha, 🟡) · Tanquián, enfrentamientos (noche del sábado, 🟡/🟢) · Cd. Juárez, col. Libertad (sábado noche, arma blanca, 🟡) · Agua Prieta, Son.: abatido el presunto homicida de un dentista de Nogales (El Imparcial 2026/10/17; dos agentes lesionados por resumen; 🟡) |
| **Vistos, no fijados o fuera de ventana** (`FECHA NO FIJADA — SIN VERIFICAR`) | **Copanatoyac, coordinador del PT y cuatro familiares** (Quadratín, sin fecha; 🔴 si cae en la ventana) · **Zacatecas, ataque a policías municipales en los límites con Aguascalientes** (El Universal, sin fecha; 1 muerto, 2 heridos; 🔴 si cae en la ventana) · Colima, «muerte de funcionario» (Telediario, sin fecha) · Zapopan, cancha de Arcos de Guadalupe (~17-oct) · San Felipe, BC, pareja herida (El Congresista) · Culiacán, Laureles Pinos (lunes tarde: ARGOS 138) · «Asesinan a cuatro el lunes» en Chihuahua (lunes no fijado) · Hermosillo, choque en el bulevar Kino (no delictivo) · Zapopan, restaurante de mariscos (sin fecha) · Escuinapa, Macoyahui (sin fecha) · Tlapa, taxista (sin fecha) · Reynosa, fosa y tres hombres (~12-oct) · Cuauhtémoc, «suman 10 homicidios en una semana» (sin fecha) |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-137-FE-001`** — **Tanquián** (`ARG-136-REC-002`): ninguna autoridad nombrada acredita la adscripción a la Guardia Nacional → **🟡 en su ventana**, por la regla del destinatario. **ARGOS 134: 8 rojos** (no 9); el muerto no se recuenta entre las recuperaciones rojas. Cálculo propio.
- **`ARG-137-FE-002`** — **Celaya** (`ARG-137-REC-001`) añade **1 rojo y 1 muerto a ARGOS 135**: tras `ARG-136-FE-002` (5 rojos, 16 muertos), **135: 6 rojos, 17 muertos**. Cálculo propio.
- **`ARG-137-FE-003`** — **133 recalculado** contra `argos-2026-10-15-fuentes.md`, `ARG-134-FE-001`, `ARG-135-FE-001` y `ARG-136-FE-001`: base firme **6 rojos y 12 muertos por agresión** (5 y 10 propios + Irapuato, pastor y esposa). **Chiapa de Corzo** pasa a **133** por la hora («tarde noche» del 14, por resumen): +1 rojo y +2 muertos con la cifra de la SSP (🟡 y sin rojo si fue 1 muerto; 3 en un medio). **Linares**: alternativa de 133 reforzada por fragmento (Milenio, «miércoles»), `DÍA CONTRADICHO`: +1 rojo y +2 muertos si fue el 14. **Cachanillas** y **Nogales**: 133 solo si antes de las 07:16 del 15 (+1 rojo cada una, sin muertos por agresión). **133: 6 a 10 rojos; 12 a 17 muertos por agresión.** **132** pierde la alternativa de Chiapa de Corzo y conserva El Guayabo (+1 rojo, +2 muertos). Cálculo propio.
- **`ARG-137-FE-004`** — **`ARG-135-ARM-001`**: la cifra **«417 cartuchos» no aparece en ninguna fuente**; el aseguramiento de Industrial Bravo publicado el 16-oct suma 420 (385 + 25 + 10), solo por resumen. La fila **sigue fuera del total**; si se acredita que es el mismo aseguramiento, la cifra correcta es 420 y no 417. **Sin cambio en los totales de 135.**
- **Actualización de dato, no fe de erratas**: `ARG-136-002`, 3 heridos (sin versión de 4) · `ARG-136-009`, el policía no fue detenido con él; vinculado a proceso · `ARG-136-007`, 2 detenidos · Divina Providencia, 2 · Cachanillas, «10 cuerpos en tres días» (colectivo).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | propia · **hechos** (`-011`, `-017`) · seguimientos | NO REVISADA | SRIV (`fgebc.gob.mx`) |
| Baja California Sur | regional | NO REVISADA | SRIV (`pgjebcs.gob.mx`) |
| Sonora | propia · **hecho** (`-018`, `ARM-003`) · seguimientos | NO REVISADA | NO REVISADA |
| Chihuahua | propia · seguimiento de `ARG-136-006` | NO REVISADA (dominio no devuelto) | SRIV (`fiscalia.chihuahua.gob.mx`) |
| Sinaloa | propia · **hechos** (`-004`, `-009`, `-010`) · **`-REC-002`** | SRIV (`sspsinaloa.gob.mx`) | NO REVISADA (dominio no devuelto) |
| Durango | regional | NO REVISADA (dominio no devuelto) | SRIV (`fiscalia.durango.gob.mx`) |
| Coahuila | regional | por portal (`coahuila.gob.mx`) | SRIV (`sitio.fgecoahuila.gob.mx`, lectura parcial) |
| Nuevo León | propia · **hecho** (`-008`) | NO REVISADA | SRIV (`fiscalianl.gob.mx`) |
| Tamaulipas | propia (fosas) | por portal (`tamaulipas.gob.mx`) | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | propia · Tanquián | SRIV (`seguridad.slp.gob.mx`) | SRIV (`fiscaliaslp.gob.mx`, lectura parcial) |
| Zacatecas | propia | SRIV (`ssp.zacatecas.gob.mx`) | NO REVISADA |
| Jalisco | propia · **hechos** (`-002`, `-012`) | NO REVISADA (dominio no devuelto) | SRIV (`fiscalia.jalisco.gob.mx`) |
| Colima | propia · **hecho** (`-007`) | NO REVISADA (dominio no devuelto) | SRIV (`fgecolima.mx`) |
| Nayarit | propia · `ARM-001` (fuera del total) | SRIV (`ssypc.nayarit.gob.mx`) | SRIV (`fgenay.gob.mx`) |
| Aguascalientes | propia | NO REVISADA (dominio no devuelto) | SRIV (`fiscalia-aguascalientes.gob.mx`) |
| Michoacán | propia · **hechos** (`-014`, `-016`) | SRIV (`ssp.michoacan.gob.mx`) | SRIV (`comunicacion.fiscaliamichoacan.gob.mx`) |
| Guanajuato | propia · **hecho** (`-015`) · **`-REC-001`** | SRIV (`seguridad.guanajuato.gob.mx`) | NO REVISADA (dominio no devuelto) |
| Ciudad de México | propia (Iztapalapa) | NO REVISADA | SRIV (`fgjcdmx.gob.mx`) |
| Estado de México | regional | NO REVISADA | SRIV (`fgjem.edomex.gob.mx`, lectura parcial) |
| Morelos | propia | NO REVISADA (dominio no devuelto) | NO REVISADA (dominio no devuelto) |
| Puebla | propia · seguimiento | NO REVISADA | SRIV (`fiscalia.puebla.gob.mx`) |
| Tlaxcala | regional | NO REVISADA (dominio no devuelto) | SRIV (`pgjtlaxcala.gob.mx`, lectura parcial) |
| Hidalgo | propia · **hecho** (`-006`) | NO REVISADA (dominio no devuelto) | NO REVISADA (dominio no devuelto) |
| Querétaro | regional · «El Tripa» | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliageneralqro.gob.mx`) |
| Veracruz | propia · **hecho** (`-003`) · `ARM-002` (fuera del total) | por portal (`veracruz.gob.mx`) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | propia · **hecho** (`-005`) | por portal (`tabasco.gob.mx`) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | propia · **hechos** (`-001`, `-013`) · seguimientos | NO REVISADA | NO REVISADA |
| Chiapas | regional · Chiapa de Corzo | NO REVISADA | SRIV (`fge.chiapas.gob.mx`) |
| Oaxaca | regional · Juchitán (visto) | por portal (`oaxaca.gob.mx/comunicacion`) | SRIV (`portal.fgeo.gob.mx`) |
| Campeche | NO REVISADA | SRIV (`spsc.campeche.gob.mx`) | NO REVISADA (`site:` ignorado) |
| Yucatán | NO REVISADA | SRIV (`ssp.yucatan.gob.mx`) | NO REVISADA |
| Quintana Roo | propia | SRIV (`ssc.qroo.gob.mx`) | SRIV (`fgeqroo.gob.mx`) |

**Sentencias: 23 de 32** (6 de lectura parcial: Coah, SLP, Edomex, Tlax, Mich, Chis); FGR revisada por búsqueda; **9 `NO REVISADA`**. **Armamento: 9 de 32 por dominio propio** (4 de lectura parcial: Nay, Gto, QRoo, Yuc), **5 por portal estatal**, **18 `NO REVISADA`**. **Alto impacto: 22 de 32 con consulta propia**, 8 regional, **Campeche y Yucatán `NO REVISADA`**.

## 10. Hechos vistos y NO fichados

Ver §7.

## 11. Sentencias — candidatas y vistas

Ver §5 y el cartelón. Ninguna integrable en la ventana; Ensenada sigue `PENDIENTE DE CONFIRMACIÓN OFICIAL` (sin fila propia: sin novedad respecto de 136). Vistas nuevas, todas anteriores a la apertura: Tamaulipas FGJE-370-2026 (seis sentenciados por desaparición; ~6-oct por resumen) · Querétaro (5, 6 y 8-oct; **ya en ARGOS 132**, retirada del cartelón) · Nayarit (8-oct) · FGR Campeche DPE/4524/2026 (7-oct) · BCS (1-13 oct) · Sinaloa, por medios (Navolato, Ahome; 12-16 oct) · Durango (5 y 7-oct, titulares de portada) · Jalisco (mayo y agosto) · Colima (21-sep) · Aguascalientes (2-oct) · Oaxaca, 80 años (13-14 oct).

## 12. Desglose de cálculos propios

- **Entidades**: 12 — Gro, Jal, Ver, Sin, Tab, Hgo, Col, NL, BC, Mich, Gto, Son. Chihuahua (seguimiento de `ARG-136-006`) y Nayarit (`ARM-001`, fuera del total) no aportan hecho propio.
- **Muertos en hechos propios**: 2 (`-001`) + 2 (`-002`) + 2 (`-003`) + 2 (`-004`) + 1 (`-006`) + 1 (`-008`) + 1 (`-009`) + 1 (`-010`) + 1 (`-011`) + 1 (`-012`) + 1 (`-013`) + 1 (`-014`) = **16**; 7 con el día solo por resumen (`-001` ×2, `-002` ×2, `-009`, `-012`, `-013`). Abatidos: 2 (`-007`). Restos: torso y restos en tres municipios (`-005`). **Heridos**: 2 (`-001`) + 1 (`-002`) + 3 (`-015`, solo por resumen) + 2 (`-016`, solo por resumen) = **8**. **Detenidos sin aseguramiento**: **1** (`-017`, contradicho); los 5 de `-REC-002` no se recuentan. Detenidos en filas ARM fuera del total: 1 + 2 + 2 = 5, no sumados.
- **Armamento**: **sin total nacional verificable**; tres filas fuera del total.
- **Duración**: 18-oct 08:34 → 19-oct 11:05 = 26 h 31 min = 26,52 h. **Densidad**: 18 / 26,52 = 0,679 → **0,68**.
- **Marcas**: FRONTERA 5 (`-002`, `-006`, `-011`, `-014`, `-017`) + día de apertura 6 (`-004`, `-005`, `-007`, `-008`, `-010`, `-018`) = **11 de 18**. Sin ruta con fecha: 8 (`-001`, `-002`, `-009`, `-012`, `-013`, `-015`, `-016`, `-017`), de ellos **6 sin otra marca**. Solo `-003` queda sin marca.

## 13. Los dos controles editoriales

**Primera ronda** (sobre `eed76fa`, con las notas íntegras de los seis equipos y del coordinador; informes en `argos-2026-10-19-equipos.md`):

- **`procedencia-cifras`**: 29 búsquedas; veinte pases, **diecisiete «CORREGIR»** (sin hallazgo: 4, Tulancingo; 8, Lerdo; 14, Monterrey, Culiacán, Escuinapa). **Aplicados**: 1 y 15 (día solo por resumen en la trazabilidad), 2 (Tlajomulco: 2020 y herida contradicha), 3 (torso: lugar y «mismo día» por resumen), 5 (Coatzacoalcos: versiones del agresor), 6 (Mazatlán: fragmentos fechados), 7 (Tecuala: ametralladora en largas, granada por titular; **integración parcial no aplicada**: el control de duplicidad la llevó a evento anterior), 9 (Colima: «Mesa de Seguridad», título, día contradicho), 10 (exfiscal: a seguimiento), 11 (Celaya: título, ventana condicional, calle), 12 (Valoración 5), 13 (Tijuana: título y contradicción), 16 (vistos de armamento; Hermosillo; FE de 417), 17 (Ensenada sin fila; Tulantepec por resumen), 18 (Conclusiones 1 y 3), 19 (**«El Talibán» → ficha**; Mazatlán, marihuana → visto; Cuajinicuilapa, Tanquián, Agua Prieta a vistos), 20 (Juchitán: en este archivo, §7; **no en el cartelón**: entidad y día no fijados, sin dato accionable).
- **`editor-duplicidad`**: veinte pases, **catorce «CORREGIR»**. **Aplicados**: 1 (**Mazatlán «tarde violenta» retirada**), 4 (deslindes de Tecuala, Coatzacoalcos, Tabasco, Copanatoyac, Lerdo), 5 (**exfiscal a seguimiento**), 6 (**Tecuala y Lerdo: evento anterior**), 7 (ametralladora en largas), 9 (Tanquián en seguimientos; Cuajinicuilapa: color preguntado), 10 (**Hermosillo → ficha**), 11 (pistas sin destino → §7), 13 (títulos de Salamanca, Tijuana, Colima), 14 (texto de método), 16 (Ensenada y vistas repetidas), 17 (cobertura: lecturas parciales, federales, 000, SESNSP/INEGI), 19 (Conclusiones 1 y 3), 20 (este archivo, índice y pendientes, al cierre).

**Segunda ronda** (sobre `58a5834`, sin búsquedas):

- **`procedencia-cifras`**: veinte pases, **catorce «CORREGIR»**. **Aplicados**: 1 (tooltip: «día solo por resumen»), 2 (torso: manchas de sangre; restos en tres municipios), 3 (Coatzacoalcos: «en el traslado» por resumen), 4 (fecha de la detención de Tijuana), 5 (seguimiento del exfiscal con la contradicción de La Jornada), 6 (Celaya: edad y Policía Vial por resumen), 7 (Talibán: fecha contradicha; resuelto por la opción A de duplicidad), 9 (**celdas «n/d»**; corporación de Tecuala), 10 (vistos: Veracruz y Industrial Bravo; **FE de 417 publicada en el cartelón**), 12-13 (heridos y detenidos con procedencia), 15 («otros seis»), 16 (Conclusiones 1 y 3), 17 (**el móvil muestra las filas ARM sin ficha**: `gen-movil.py`), 18-20 (este archivo renumerado, índice, pendientes).
- **`editor-duplicidad`**: veinte pases, **doce «CORREGIR»**. **Aplicados**: 1 (deslinde del Talibán), 2 (**opción A: `-REC-002`**, fuera de totales), 3 (deslinde de Hermosillo, sin acusación de omisión), 4 (5 detenidos de filas ARM declarados), 5 («n/d» y deslindes de ARM), 6 (**Conclusión 4 con `ARG-133-002`**), 7 (Conclusión 3, «presuntos operadores»), 8 (Querétaro retirada; Tulantepec con vínculo), 9 (títulos de `-003`, `-014`, `-017`), 10 (colas de armamento duplicadas), 11 (detenido solo en `-017`), 15 (federales: solo el equipo Golfo), 19-20 (pistas, índice, pendientes). **Sin aplicar, con motivo**: Juchitán no entra al cartelón (entidad y día no fijados; registrado aquí).

## 14. Herramientas

`tools/datos-argos-137.py` (copia de la estructura de 136; `ARM` con campos `integra` y `nd`: las filas fuera del total se muestran atenuadas, con «n/d» donde no hay cifra citable, y no alimentan `EVENTOS_ARM`; `R` admite ventanas anteriores en verde) → `reports/argos-2026-10-19.html`; `gen-movil.py` emite como tarjetas las filas de armamento sin ficha propia; `gen-movil.py 137 2026-10-19 136 2026-10-18 11:05`; `gen-texto.py`; `validar.js … 2026-10-18 2026-10-19`.

## 15. Lecciones de método (no van al cartelón)

1. **La ola no trajo los dos rojos del lunes por la mañana** (Tulancingo, Tlajomulco): el primero salió de la búsqueda de cierre del coordinador, el segundo de la sección «AJENOS» del equipo Centro. **La sección «AJENOS» funcionó**: tres pistas de otras regiones (Tlajomulco, Copanatoyac, Cuajinicuilapa) llegaron por ahí.
2. **Los equipos no hicieron `grep` en los HTML** (Noroeste y Sureste lo declararon): el cotejo lo hizo el coordinador. La plantilla debe exigir el comando literal.
3. **Una entidad homónima** (Juchitán de Zaragoza, Oax. / Juchitán, Gro.) llevó a un equipo a corregir como «error geográfico» lo que probablemente era correcto. Ante topónimos repetidos entre estados, fijar la entidad por el medio regional antes de asignar región.
4. **El agregado federal volvió a ser de tres días** (16-18) y solo apareció por republicadores: la tercera forma de la triple consulta sigue siendo la que encuentra.
5. **`procedencia-cifras` volvió a hallar hechos** que la ola no traía («El Talibán» y cuatro; Mazatlán, 1.5 t; Agua Prieta): cuarta edición seguida.
6. **Las conclusiones deben cotejarse contra todo el archivo, no solo contra la edición anterior**: la de Salamanca omitió `ARG-133-002`.
7. **Las «vistas» de sentencias se repiten entre ediciones** (Querétaro, ya en 132): cotejar antes de imprimirlas.
8. **Criterio de inclusión por ruta fechada**, escrito por primera vez: entra con marca de día de apertura el hecho con ruta fechada del 18; queda visto el que solo tiene hora por resumen y ninguna ruta (Irapuato). Para filas de armamento: atenuada solo si un titular fechado sostiene el dato.

## 16. Emisores por ficha (lista íntegra)

- `ARG-137-001` — Institucional: SIN BOLETÍN · Nacional: Unomásuno · Con fecha en la ruta: ninguna · Regionales: Quadratín Guerrero, El Sur, Agencia IRZA, Telediario · Recuento I 0 / N 1 / R 4 / A 0
- `ARG-137-002` — Institucional: SIN BOLETÍN · Nacional: N+, Milenio · Con fecha en la ruta: ninguna · Regionales: Telediario, Zócalo · Recuento I 0 / N 2 / R 2 / A 0
- `ARG-137-003` — Institucional: SIN BOLETÍN · Nacional: La Silla Rota, N+ · Con fecha en la ruta: La Silla Rota (2026/10/18), Gráfico al Día (2026/10/19) · Regionales: Gráfico al Día, El Sol de Veracruz, XEU, AVI Veracruz, La Nigua, La Opinión, Vanguardia Veracruz, Diario Acayucan · Recuento I 0 / N 2 / R 8 / A 0
- `ARG-137-004` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Luz Noticias (2026-10-18), Línea Directa (2026-10-18) · Regionales: Luz Noticias, Línea Directa, Los Noticieristas · Recuento I 0 / N 0 / R 3 / A 0
- `ARG-137-005` — Institucional: SIN BOLETÍN · Nacional: El Universal · Con fecha en la ruta: Diario de Yucatán (2026/10/18) · Regionales: Diario de Yucatán, Cuarto Poder, El Mañana, MexNoticias, El Congresista · Recuento I 0 / N 1 / R 5 / A 0
- `ARG-137-006` — Institucional: SEPH (por titular de Criterio) · Nacional: La Silla Rota, Milenio · Con fecha en la ruta: La Silla Rota (2026/10/19) · Regionales: El Universal Hidalgo, Criterio Hidalgo, Énfasis, La Jornada Hidalgo, Effeta · Recuento I 1 / N 2 / R 5 / A 0
- `ARG-137-007` — Institucional: Mesa de Seguridad de Colima (por titular de Portal Colima, AFmedios y Vadenuez) · Nacional: Infobae, La Jornada, Publimetro, UnoTV, TV Azteca · Con fecha en la ruta: Proyecto Puente (2026/10/18), Infobae, La Jornada, Publimetro (2026/10/19) · Regionales: Proyecto Puente, Portal Colima, AFmedios, Vadenuez, Meganoticias, Telediario · Recuento I 1 / N 5 / R 6 / A 0
- `ARG-137-008` — Institucional: SIN BOLETÍN · Nacional: MVS, Milenio, N+ · Con fecha en la ruta: MVS (2026/10/18) · Regional: Telediario · Recuento I 0 / N 3 / R 1 / A 0
- `ARG-137-009` — Institucional: SIN BOLETÍN · Nacional: Milenio · Regionales: Meganoticias, El Congresista · Recuento I 0 / N 1 / R 2 / A 0
- `ARG-137-010` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Diario de Yucatán (2026/10/18) · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-137-011` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Opinia (2026/10/19) · Regionales: Opinia, Diario Tijuana (2026/10), Blanco y Negro, alfredoalvarez.mx · Recuento I 0 / N 0 / R 4 / A 0
- `ARG-137-012` — Institucional: SIN BOLETÍN · Regional: Telediario · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-137-013` — Institucional: SIN BOLETÍN · Regionales: Quadratín Guerrero, Agencia IRZA, El Sur · Recuento I 0 / N 0 / R 3 / A 0
- `ARG-137-014` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Grupo Marmor, Red Michoacán, MediaNews (2026/10/19) · Regionales: los tres y Respuesta · Recuento I 0 / N 0 / R 4 / A 0
- `ARG-137-015` — Institucional: SIN BOLETÍN · Nacional: Milenio · Recuento I 0 / N 1 / R 0 / A 0
- `ARG-137-016` — Institucional: SIN BOLETÍN · Regionales: Contramuro, Quadratín Michoacán, IMN · Recuento I 0 / N 0 / R 3 / A 0
- `ARG-137-017` — Institucional: SIN BOLETÍN · Regional: alfredoalvarez.mx (titular) · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-137-018` — Institucional: SIN BOLETÍN · Con fecha en la ruta: El Imparcial (2026/10/18) · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-137-REC-001` — Institucional: gobierno municipal de Celaya (alcalde, por titular de Correo) · Nacional: La Silla Rota, Milenio · Con fecha en la ruta: La Silla Rota (2026/10/17), Periódico Correo (2026/oct/17, 2026/oct/19), AM (2026/10/17), Noticieros en Línea (2026/oct/17) · Regionales: Correo, AM, Noticieros en Línea, Ágora, Telediario, Sinaloahoy · Recuento I 1 / N 2 / R 6 / A 0
- `ARG-137-REC-002` — Institucional: SIN BOLETÍN (Gabinete y Defensa, por resumen) · Nacional: Proceso, Infobae, Político.mx · Con fecha en la ruta: Proceso (2026/10/18), Infobae, Político.mx (2026/10/19) · Recuento I 0 / N 3 / R 0 / A 0
- `ARG-137-ARM-001` — Gabinete de Seguridad (por republicadores: Milenio, Ultranoticias, RED113, Tallapolítica, Certeza Diario; no independientes) · Con fecha en la ruta: NTV (2026/10/19) · NX Noticias
- `ARG-137-ARM-002` — Gabinete de Seguridad (por republicadores) · Regional: La Nigua
- `ARG-137-ARM-003` — El Imparcial (2026/10/18), ficha `ARG-137-018`
