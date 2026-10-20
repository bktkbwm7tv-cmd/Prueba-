# ARGOS 136 — Archivo de fuentes

**Corte**: 2026-10-18 · **Ventana**: 17-oct 09:28 → 18-oct 08:34 CDMX (**23 h 06 min**; `WINDOW_DAYS = 2`) · **Densidad**: 9 hechos propios / 23,1 h = **0,39 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 08:34 CDMX). Las consultas (incluidas las 30 de `procedencia-cifras`) continuaron hasta las **10:00 CDMX** (marca «Consulta» del cartelón); los hechos posteriores a las 08:34 pertenecen a ARGOS 137.

Informes íntegros de los seis equipos, notas del coordinador e informes de los cuatro controles: **copiados al repositorio** en `reports/argos-2026-10-18-equipos.md` (antes solo en el *scratchpad*). La plantilla de los equipos, en `tools/plantilla-equipos-136.md`.

## 1. La base

- Clon con HEAD suelto en `60f2777` (cuarta edición seguida). Se abrió `claude/argos-136` y se fusionó en *fast-forward* `main` (`b0558a3`), `claude/argos-129` … `-135`, en ese orden y sin conflicto. HEAD de partida: `2338846`.
- `reports/`: 189 archivos, última edición `argos-2026-10-17` (ARGOS 135), como estaba previsto.
- **Herramientas** (commit `8a99ea8`, deuda 9 de 135): `gen-texto.py` emite en **orden de documento** (antes extraía por tipo y separaba cada subtítulo de su contenido; probado sobre 135: mismo contenido, otro orden); `gen-movil.py` retira «Toque un ARG-ID» (el índice no se publica en el teléfono), «mismo contenido verificado» y «totales en las tarjetas de arriba».

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (`CONNECT tunnel failed, response 403`), 08:34. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**. Además, 16 servidores MCP de complementos no conectaron por el mismo 403 del proxy (sin efecto en ARGOS).
- **Consulta de control** («ataque armado muertos "17 de octubre" 2026 México», en los dos modos): `standard` **ningún hecho del 17**; `extended`, Silao (Baños de Agua Caliente) y Acapulco (col. Cuauhtémoc). **Se mantuvo `extended` obligatorio.** Silao resultó de la ventana de 135 (→ `ARG-136-REC-001`); Acapulco, del corte (→ `ARG-136-002`).
- **Presupuesto**: control 2 + ola (Noroeste 26, Noreste 25, Occidente 28, Centro 28, Golfo y federal 28, Sureste 24 = **159**) + **7 del coordinador** = **168**; `procedencia-cifras` **30** → **198 de 200**. `editor-duplicidad` no busca en la web; la segunda ronda de controles se hace **sin búsquedas**.

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (21 `NO REVISADA` + 8 por portal en 135) | **Por dominio propio ahora (11 de las 21, más Zac de las 8)**: BC (`seguridadbc.gob.mx`), BCS (`sspbcs.gob.mx`), Son (`ssp.sonora.gob.mx`, solo portada), Sin (`sspsinaloa.gob.mx`, **primer dominio devuelto en nueve ediciones**), Mich (`ssp.michoacan.gob.mx`), Gto (`seguridad.guanajuato.gob.mx`, una página), CDMX (`ssc.cdmx.gob.mx`), Edomex (`sseguridad.edomex.gob.mx`), Pue (`ssp.puebla.gob.mx`), Chis (`sspc.chiapas.gob.mx`), QRoo (`ssc.qroo.gob.mx`) y Zac (`ssp.zacatecas.gob.mx`, de las 8 por portal); Son y Gto, lectura parcial. **Por portal estatal (2)**: NL (`nl.gob.mx/boletines`), Gro (`guerrero.gob.mx`). **Siguen o pasan a `NO REVISADA` (18)**: Dgo, SLP, Jal, Tlax, Hgo, Qro, Camp, **Mor** (dominio no devuelto; `morelos.gob.mx` solo en una búsqueda genérica) · Chih, Coah, Tamps, Col, Ags, Ver, Tab, Oax, Yuc · **Nay** (`fgenay.gob.mx` consultado solo por la vinculación de Tepic; la SSP, `ssypc.nayarit.gob.mx`, sin consultar) |
| Prioridad — sentencias (14 `NO REVISADA` en 135) | **Revisadas (11 de 14)**: BC (`fgebc.gob.mx`), Son (`fiscalia.sonora.gob.mx`, **primer dominio devuelto en nueve ediciones**, solo convocatorias), Chih (`fiscalia.chihuahua.gob.mx`), Coah (`sitio.fgecoahuila.gob.mx`), Mich (`comunicacion.fiscaliamichoacan.gob.mx`), Nay (`fgenay.gob.mx` — el dominio de la plantilla, `fiscalianayarit.gob.mx`, no devuelve), Ags (`fiscalia-aguascalientes.gob.mx`), CDMX (`fgjcdmx.gob.mx`), Tlax (`pgjtlaxcala.gob.mx`, solo páginas administrativas), Gro (`fiscaliaguerrero.gob.mx`), Yuc (`fge.yucatan.gob.mx`). **Siguen `NO REVISADA`**: Sin (`fiscaliasinaloa.gob.mx` no devuelto, novena edición), Hgo (`pgjhidalgo.gob.mx` no devuelto), Camp (`fgecam.gob.mx`: el buscador vuelve a ignorar el `site:`) |
| Ciclo | **B** — Noreste y Golfo encabezaron el triaje judicial tras la prioridad, **por orden expresa del destinatario** (mensaje de arranque de la sesión, 18-oct 08:34: «Después, CICLO B (Noreste + Golfo)»; mismo texto en `reports/_ordenes-ARGOS-136.txt`). ⚠️ **La tabla de `CLAUDE.md` da C para 136** (A = 101, 104…, luego 134 = A, 135 = B, 136 = C): la serie declarada va desfasada desde 134 (C en 134, A en 135, B en 136). Señalado al destinatario; **137 debe decidir si retoma la tabla (A) o la serie declarada (C)** |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Noreste: NL, Tamps, SLP (boletines sin fecha en ruta), Zac revisadas, SRIV; Coahuila saldada. Golfo: FGE Veracruz en `comunicacion.fiscaliaveracruz.gob.mx` (no en `fiscaliaveracruz.gob.mx`) y FGE Tabasco revisadas, SRIV; nombre y causa del caso del comunicador (J-10/2026) confirmados por medios |
| Regresión por rotación | Sentencias: BCS, Dgo, Jal, Col, Gto, Edomex, Mor, Pue, Qro, Oax, Chis, QRoo pasan a `NO REVISADA`. Armamento: Chih, Coah, Tamps, Col, Ags, Ver, Tab, Oax, Yuc pasan a `NO REVISADA`. **Prioridad sobre el ciclo en 137** |

Serie declarada: … · C (134) no · A (135) no · **B (136) no** (ver la advertencia del renglón «Ciclo»). **Lectura parcial en sentencias (4)**: Son (convocatorias), Tlax (sin boletines), SLP (boletines sin fecha en ruta), Nay (consulta indirecta).

**Dominios corregidos para las plantillas**: Nayarit `fgenay.gob.mx` · Michoacán `comunicacion.fiscaliamichoacan.gob.mx` · Veracruz `comunicacion.fiscaliaveracruz.gob.mx` · Zacatecas SSP `ssp.zacatecas.gob.mx` · Sonora fiscalía `fiscalia.sonora.gob.mx` · Coahuila `sitio.fgecoahuila.gob.mx`.

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **15-oct** | Existe (Milenio y republicadores, no independientes); ventana de 134. Fuera del total |
| **16-oct** | `SIN RESULTADO INDEXADO EN VENTANA` con título propio: día suelto (nada; Emsavalles encabeza con el 16 el cuerpo del 15), agregado (nada), título en Milenio (solo 14 y 15 de 2026 y el del 16-oct de **2025**, año equivocado). Candidato sin fecha: Ahora Noticias «32 detenidos en 10 estados» (`ahoranoticias.com.mx/nacional/operativos-federales-dejan-32-detenidos-y-decomisos-en-10-estados/`, sin fecha en ruta; «16 de octubre» solo por resumen; lista BC, Culiacán y Colima como el del 15: **puede ser el mismo**). **Cifras solo por resumen: no se imprimen** |
| **17-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto, agregado «16 y 17» —solo 2025—, título entre comillas sin `site:`) |

**Defensa** (`gob.mx/defensa/prensa`, último 14-oct), **Marina** (`gob.mx/semar`, último 12-oct), **GN** (sin octubre-2026), **FGR** (`gob.mx/fgr`, 2020): SRIV. `gabinetedeseguridad.gob.mx`: solo contenido de 2025 → SRIV.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **«Pokémon» ↔ Laguna Colorada** (`ARG-135-008` ↔ `ARG-134-016`) | **Distintos, con reserva**: 4 detenidos frente a 7; célula con HSI frente a 5 cateos con Semar, SSPC, GN y FGR; publicación del 16 frente a operativo del 15 (Ríodoce 2026/10/15); familias distintas. Coincide solo «cuatro armas». Indicio adicional: Ahora Noticias (por resumen) lista en Culiacán «dos operativos, 11 detenidos» = 7 + 4. Domicilios: no publicados en ninguna fuente. **Nueva posible duplicidad**: SSP Sinaloa, col. Industrial Bravo, «cuatro civiles armados», 1 ametralladora 7.62 y 385 cartuchos 7.62 (`sspsinaloa.gob.mx/post/cuatro-civiles-armados-…`, fecha no fijada; 13-16 oct por resumen): coincide en 4 detenidos y ametralladora; cartuchos y corporación distintos. **NO es** el aseguramiento de Industrial Bravo / La Popular del 9-10 oct (9 largas, 22 cargadores, 173 cartuchos, 7 AEI; ARGOS 131): otras cifras. Fecha y domicilio del post: pendientes. **`ARG-135-ARM-001` sigue fuera del total** (ver §8) |
| **Cateos de Mazatlán y El Carrizal** (`-009`, `ARM-002`) | **No son el renglón del boletín del 15-oct**: los medios los atribuyen a un comunicado conjunto **Semar–SSPC–FEMDO del 16-oct** (MexNoticias, por resumen; Reforma al Gabinete). Rutas del 16: tusbuenasnoticias, Luz Noticias, El Diario de Chihuahua, diario.mx. Fecha de los cateos: no publicada. El Carrizal: 1 arma larga, cartuchos y dos cajas de municiones sin cifra, metanfetamina. **Arbitraje entre Noroeste («arma larga en varias fuentes») y Golfo («todo por resumen»)**: las rutas del 16 llevan fecha, pero el «1 arma larga» no está en ningún titular ni *slug* (diario.mx: «aseguran autos, armas y droga», sin cifra): **la cantidad es solo por resumen**. Se retira la marca «posible evento anterior»; **sigue fuera del total** |
| **Apatzingán** (`ARG-135-003`) | Hora **no fijada** (Quadratín, La Voz de Michoacán, El Congresista). Hallazgos «simultáneos», por resumen. Sin identificación. 134 o 135 sigue abierto |
| **Linares** (`ARG-135-REC-001`) | **Jueves 15 ~22:00** en las rutas fechadas (MVS 2026/10/16, Punto x Punto 2026/10/16 ×2, Enfoque Monterrey 2026/10/17), por resumen; «miércoles» solo en Milenio y Telediario, sin fecha en ruta. **La URL de El Mañana 2026/10/15 que 135 dio como primera publicación es el doble homicidio de Gómez Morín (Monterrey), no Linares** (equipo Noreste). Primera publicación de Linares: **16-oct**. → ventana de **134** por la mayoría, pero **sin fragmento literal: `DÍA CONTRADICHO` persiste** (la alternativa 133 no se retira como probada); ver §8. Herido: sobrevivió (El Porvenir) o murió (resumen de Punto x Punto): contradicho |
| **Tijuana, Divina Providencia** (`-002`) | Sin ruta con día (Zeta y Diario Tijuana, solo `2026/10/`); identificación por «información preliminar de los cuerpos de seguridad», no de la FGE; Milenio titula «dos mujeres y bombero» (3) frente a 2 en el resto: **contradicho, sin arbitrar** |
| **Cachanillas** (`-REC-003`) | Colectivo Buscando a Tolano; hallazgo del jueves 15 (Diario Tijuana, Infobaja). **Punto Norte 2026/10/17: «6 cuerpos y osamentas apilados»** (4 cuerpos y 2 esqueletos, por resumen): compatible con 4 si los esqueletos son los «restos óseos» ya publicados; sin arbitrar. Sin cifra oficial; la FGE llegó después y retiró al colectivo (por resumen) |
| **Nogales** (`-REC-004`) | **El Imparcial 2026/10/17: 2 osamentas más en Mariposa; «siete hallazgos en cinco fosas durante dos días»** (15 y 16-oct), Buscadoras de la Frontera. Fiscalía de Sonora resguarda. Seguimiento en el panorama |
| **Ajuchitlán** (`-010`) | Rescate del **16-oct** por ruta. **La séptima persona sigue sin localizarse** (Infobae 2026/10/18). Defensa, 9.ª Región Militar, por resumen; la gobernadora confirmó que son del ejido **El Balcón** (por resumen): resuelve «Puerto Grande o El Balcón». Amparo 412/2026 del 5-oct (ONG, por resumen). El ejido: «liberados, no rescatados» |
| **Taxco, 6 policías (2020)** | **«El Gallinero»**, 1 detenido en Maravatío (Mich.) por FGE Guerrero con FGE Michoacán, Defensa y GN; boletín de la noche del 16 (Quadratín, por resumen); La Silla Rota 2026/10/17. Fecha de la detención no publicada → **fichado como `ARG-136-008`** con la marca de día de apertura (editor-duplicidad, pase 3; `_pendientes.md`: «si se fija en la ventana de 135, 🟢 `SIN FECHA FIJADA`») |
| **El Tívoli** (`-013`) | Sin ruta con día; vehículo o vía pública, contradicho; sin identificación |
| **CDMX** (`-012`) | **Sin comunicado de la SSC** (Milenio: «las autoridades no han emitido un comunicado oficial»); captura difundida por un periodista (Infobae). Alcaldía del ataque: no publicada |
| **La Costerita** (`-007`) | Ninguna ruta con día; «este sábado» y ~07:15 por resumen → 135 sostenido |
| **Coquimatlán** (`ARG-134-003`) | Sin comunicado FGE; 2 mujeres muertas y 1 herido (Colima Noticias) frente a 3 muertos (Vadenuez, 15-oct). Sigue 2 a 3 |
| **Tlalnepantla** (`ARG-134-004`) | La Silla Rota 2026/10/15: «se desconoce identidad y sexo» — contradice «dos hombres». Sin hora |
| **Monterrey / Santa Catarina** | ABC Noticias 2026/10/16: el fiscal «no descarta» el vínculo. Sin novedad |
| **El Guayabo** (`ARG-134-REC-003`) | **«Noche del martes»** = 13-oct (MVS 2026/10/15, por resumen) → **ventana de 132**; ver §8. FGE (Contramuro): la agresión iba dirigida contra el adulto |
| **Chiapa de Corzo** (`ARG-134-REC-002`) | **14-oct por ruta** (El Sol del Soconusco 2026/10/14; Heraldo de México 2026/10/14): no fue el 13. Hora no fijada → **132 si antes de las 08:19 del 14; 133 si después** |
| **«El Tripa»** | Código QRO y AlertaQro 2026/10/16, Noticias de Querétaro 2026/10/17; Milenio «9-oct» sin fecha en ruta. **Sigue `SIN FECHA FIJADA`** |
| **Tepic** (`-011`) | **Imputado, no vinculado**: audiencia de vinculación «la próxima semana» (Meridiano 2026/10/17); causa 2679/2026, por resumen |
| **Tezontepec** (`-REC-002`) | Sin segunda fuente con fecha en ruta; sin PGJEH |
| **Sentencias** | Ensenada: desglose y reparación (§11). Hermosillo: Tribuna 2026/10/16, sin boletín. Veracruz: comunicador, J-10/2026, sin boletín (último indexado en el dominio: 24-ago). FGR Cosoleacaque (sentencia del 8-oct) y Banderilla (9-oct; DPE/4655/2026 según La Opinión): sin boletín. CDMX Diego y Abdiel: sin boletín. Tulantepec: aplazada al 21-oct |
| **Colores pendientes del destinatario** | Patamban, Coatzacoalcos, San Blas Atempa (Quadratín: «**ex**dirigente de la Sección 22»; otros, docente), Iztapalapa, Cajeme: sin dato nuevo. **Nuevos**: San Baltazar Tetela (🟡 por lectura literal; ¿🔴 por víctima menor ajena al ataque?) y Tanquián (`-REC-002`, 🔴 si la víctima era de la GN), ver §7 |

## 6. Seguimientos sin cambio de ficha

Coatzacoalcos (expareja prófuga, Golpe Político 2026/10/17) · Orizaba · Villahermosa · San Blas Atempa (sin detenidos) · Jerez (número no determinado) · Atotonilco · Hermosillo `-005`/`-006` (sin segunda fuente; «hombre de 51 años», Medios Obson 2026/10/17, no atribuible) · Iztapalapa, Xochimilco, Mazatepec, Toluca, Ecatepec: no consultados por presupuesto · Patamban: no consultado · Barrio 18 (QRoo): no consultado.

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Salamanca, col. Guanajuato** (`-001`) | Occidente; AM `…/salamanca/2026/10/17/…-1856213.html` fija el sábado; ~17:30 por resumen (AM y Milenio), posterior a la apertura. Esquina contradicha (Dolores Hidalgo–Comonfort / Celaya–Comonfort). El Salmantino, cuarta regional. 🔴 por homicidio múltiple. **NO es** `ARG-133-002` |
| **Acapulco, col. Cuauhtémoc** (`-002`) | Pista de control; sábado 17 ~17:30/18:00 solo por resumen, **ninguna ruta con fecha** → ★★☆☆☆. 🔴. Título reducido a la fórmula del titular de Quadratín. Homónimo de noviembre de 2025 descartado |
| **Acapulco, col. Vicente Guerrero** (`-003`) | **Hallado por `procedencia-cifras`**: Quadratín «Hallan a 2 asesinados con huellas de tortura en Acapulco», sábado ~19:00 por resumen, fuente única sin fecha en ruta → 🔴 ★★☆☆☆. Distinto del cuerpo del 15-oct en la misma calle |
| **Culiacán** (`-004`) | Coordinador; colonia **contradicha** (Estela Ortiz / Ruiz Cortines), Línea Directa 2026-10-18 añadida por `procedencia-cifras`. 🟡 con `FRONTERA` |
| **Ensenada, Maneadero** (`-005`) | **Hallado por `procedencia-cifras`**: aviso ~09:30 del sábado por resumen (dos minutos después de la apertura) → **marca de día de apertura**; Zeta solo con mes; causa de muerte no determinada → 🟡 ★★☆☆☆ |
| **Exfiscal de Chihuahua** (`-006`) | ~10:20 según el Registro Nacional de Detenciones (titular de Radionet; hora por resumen) → **posterior a la apertura: se retira la marca de día de apertura**. Delitos por titular de UnoTV; muerte de agentes de la CIA por titulares (Informador, Forbes); abril y El Pinal solo por resumen; FGR, traición a la patria, por titulares de Expansión y La Silla Rota, sin comunicado de la FGR. 🟢 |
| **Puebla, detenidos** (`-007`) | 2 detenidos por titulares (Paralelo19, Ambas Manos, Curul) frente a 1 («detiene a sicario», Urbano): **contradicho**. Hora no fijada → marca de día de apertura. 🟢 |
| **Taxco** (`-008`, `-009`) | **Fichados tras editor-duplicidad (pase 3)**: mismo criterio que `-006` y `-007` en 135 y 136 (publicados el día de apertura sin hora fijada). `-008`: «El Gallinero» (alias no reproducido), boletín de la noche del 16 solo por resumen. `-009`: detención del 16 o del 17, contradicha; el policía detenido con él, solo en Quadratín, no se integra. 🟢 cada uno |
| **Silao, Baños de Agua Caliente** (`-REC-001`) | ~06:30, ~07:20 o ~07:30 por resumen, todas antes de las 09:28 → **ventana de 135**. 🔴 por homicidio múltiple. Deslindado de `ARG-133-REC-002` y `-REC-003` |
| **Tanquián de Escobedo** (`-REC-002`) | Golfo lo pasó a Noreste; jueves 15 ~21:00 (Potosinoticias 2026/10/16) → **ventana de 134**. 🔴 provisional por víctima de una fuerza de seguridad; **adscripción contradicha** (Milenio: «aún se desconoce»; La Opinión: «investigan si pertenecía») → título «reportado como elemento»; **si no era de la GN, 🟡: decisión del destinatario** |
| **Cuauhtémoc, Chihuahua, campo menonita** (`-REC-003`) | **Hallado por `procedencia-cifras`**: ~09:00 del sábado por resumen, antes de la apertura → **ventana de 135**; «viernes» en un medio (día contradicho); tres rutas del 17 de un mismo grupo editorial. 🔴 por homicidio múltiple |
| **San Baltazar Tetela, el ataque** | Centro: «madrugada» del 17 por resumen → ventana de 135. **Lectura literal de la metodología: homicidio doloso único → 🟡** (editor-duplicidad, pase 12: «víctima civil ajena» es agravante de la tabla «quién inicia», que rige operativos). **No recuperable como 🟡**; el hecho consta en el Hecho de `-007`. **Si el destinatario lo fija en 🔴, se recupera en 137** |
| **Xalapa, El Moral** (retirado) | `procedencia-cifras`: el homicidio de El Moral con esa descripción es del **sábado 3-oct ~22:15** (Golpe Político 2026/10/03, Diario Gráfico 2026/10/05); ninguna nota del 18 → **retirado del borrador**: `POSIBLE HECHO ANTERIOR — NO INTEGRAR HASTA FIJAR DÍA` |
| **Temixco, Lomas del Carril** (retirado) | `procedencia-cifras`: la fuente dice «el sábado» y «ayer» (incoherencia interna), la cajuela estaba abierta durante el ataque (no hubo ocultamiento) y la colonia acumula varios homicidios sin fecha en ruta → **retirado**: `POSIBLE CASO HOMÓNIMO — DÍA NO FIJADO` |
| **Juchitán, ataque a un diseñador muxe** | Dos detenidos; Proceso 2026/10/16 (publicado antes de la apertura) → visto |
| **León, Valle Hermoso** | 1 muerto y 1 herido, noche del viernes 16 → 🟡 de 135, no recuperable |
| **Chignahuapan** | Seis cateos con apoyo de Marina (titular de Excélsior, sin fecha en ruta); 9 detenidos y 1 arma por resumen; fecha no fijada → visto |
| **Radio Hoy, Caribe Verde** | Ruta 2026/10/17, entidad no determinada → visto, no atribuible |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-136-FE-001`** — **Linares** (`ARG-135-REC-001`): primera publicación **16-oct**, no 15 (la URL de El Mañana era de otro hecho); jueves 15 por la noche en las rutas fechadas, por resumen → **ventana de 134 por la mayoría, `DÍA CONTRADICHO` persiste**. **El Guayabo** (`ARG-134-REC-003`): martes 13 → **ventana de 132** (por resumen). **Chiapa de Corzo** (`ARG-134-REC-002`): 14-oct por ruta → **132 o 133 según la hora**. Cálculo propio: **132: +1 rojo y 2 muertos** (El Guayabo), **más 1 rojo si Chiapa de Corzo fue antes de las 08:19** (muertos 1 a 3, SSP: 2; 🟡 si 1); **133 pierde El Guayabo** y conserva Linares y Chiapa de Corzo como alternativas. El rango de 133 se recalcula en `_pendientes.md` contra `argos-2026-10-15-fuentes.md`, no aquí.
- **`ARG-136-FE-002`** — **Recuperaciones de este corte**: Silao (`-REC-001`) y Cuauhtémoc, Chih. (`-REC-003`) añaden **2 rojos y 4 muertos a ARGOS 135** (3 → 5 rojos; 12 → 16 muertos con las recuperaciones rojas; el total no incluye los amarillos no recuperados de la ventana: León, Valle Hermoso, 1 muerto, y San Baltazar Tetela, 1 niño). Tanquián (`-REC-002`) añade **1 rojo y 1 muerto a ARGOS 134** (hasta 9 rojos; **8 si la víctima no era de la GN** y el hecho es 🟡). San Baltazar Tetela: 🟡 de 135, **no se recuenta** salvo decisión del destinatario (entonces, 135: 6 rojos, 17 muertos). Cálculo propio.
- **`ARG-136-FE-003`** — **Armamento de 135**: `ARM-001` deja de estar en duplicidad con `ARG-134-ARM-001` y pasa a **posible duplicidad con el aseguramiento de la SSP Sinaloa en Industrial Bravo**: sigue fuera del total. `ARM-002`: retirada la marca de evento anterior (comunicado del 16, no boletín del 15); sigue fuera porque la cantidad solo consta por resumen. **Sin cambio en los totales de 135.**
- **Actualización de dato, no fe de erratas**: Nogales («siete hallazgos en cinco fosas») · Cachanillas (4 cuerpos y 2 esqueletos según un medio: compatible con 4, no contradictorio) · Ajuchitlán (séptima persona; ejido El Balcón) · Tepic (imputado, sin vinculación) · Divina Providencia (2 o 3, contradicho) · Tlalnepantla (sexo no confirmado).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | propia · **hecho** (`-005`) · seguimientos | SRIV (`seguridadbc.gob.mx`) | SRIV (`fgebc.gob.mx`) |
| Baja California Sur | regional | SRIV (`sspbcs.gob.mx`) | NO REVISADA |
| Sonora | propia · seguimientos | SRIV (`ssp.sonora.gob.mx`, portada) | SRIV (`fiscalia.sonora.gob.mx`) |
| Chihuahua | propia · **hecho** (`-006`) · **`-REC-003`** | NO REVISADA | SRIV (`fiscalia.chihuahua.gob.mx`) |
| Sinaloa | propia · **hecho** (`-004`) | SRIV (`sspsinaloa.gob.mx`; Industrial Bravo sin fecha) | NO REVISADA |
| Durango | regional | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Coahuila | regional | NO REVISADA | SRIV (`sitio.fgecoahuila.gob.mx`) |
| Nuevo León | propia · seguimientos | por portal (`nl.gob.mx`) | SRIV (`fiscalianl.gob.mx`) |
| Tamaulipas | propia (fosas) | NO REVISADA (dominio no devuelto) | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | propia · **`-REC-002`** | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | propia · seguimiento | SRIV (`ssp.zacatecas.gob.mx`) | SRIV (`fiscaliazacatecas.gob.mx`) |
| Jalisco | regional | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Colima | propia · seguimientos | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Nayarit | propia · seguimiento | NO REVISADA (`fgenay.gob.mx` solo por la vinculación de Tepic) | SRIV (`fgenay.gob.mx`, consulta indirecta) |
| Aguascalientes | NO REVISADA | NO REVISADA (dominio no devuelto) | SRIV (`fiscalia-aguascalientes.gob.mx`) |
| Michoacán | propia · seguimientos | SRIV (`ssp.michoacan.gob.mx`) | SRIV (`comunicacion.fiscaliamichoacan.gob.mx`) |
| Guanajuato | propia · **hecho** (`-001`) · **`-REC-001`** | SRIV (`seguridad.guanajuato.gob.mx`) | NO REVISADA |
| Ciudad de México | regional · seguimiento | SRIV (`ssc.cdmx.gob.mx`) | SRIV (`fgjcdmx.gob.mx`) |
| Estado de México | regional · seguimiento | SRIV (`sseguridad.edomex.gob.mx`) | NO REVISADA |
| Morelos | propia (Temixco, retirado) | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Puebla | propia · **hecho** (`-007`) | SRIV (`ssp.puebla.gob.mx`) | NO REVISADA |
| Tlaxcala | regional | NO REVISADA (dominio no devuelto) | SRIV (`pgjtlaxcala.gob.mx`, administrativas) |
| Hidalgo | propia · seguimientos | NO REVISADA (dominio no devuelto) | NO REVISADA (dominio no devuelto) |
| Querétaro | regional · «El Tripa» | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Veracruz | propia (Xalapa, retirado) | NO REVISADA (dominio no devuelto) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | propia | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | propia · **hechos** (`-002`, `-003`, `-008`, `-009`) · seguimientos | por portal (`guerrero.gob.mx`, semanal del 5-11 oct) | SRIV (`fiscaliaguerrero.gob.mx`, listados del 15-oct) |
| Chiapas | propia · seguimiento | SRIV (`sspc.chiapas.gob.mx`) | NO REVISADA |
| Oaxaca | propia · seguimiento | NO REVISADA | NO REVISADA |
| Campeche | regional | NO REVISADA (`site:` ignorado) | NO REVISADA (`site:` ignorado) |
| Yucatán | regional | NO REVISADA | SRIV (`fge.yucatan.gob.mx`) |
| Quintana Roo | regional | SRIV (`ssc.qroo.gob.mx`) | NO REVISADA |

**Sentencias: 17 de 32**; FGR revisada por búsqueda; **15 `NO REVISADA`**. **Armamento: 12 de 32 por dominio propio** (2 de lectura parcial), **2 por portal estatal**, **18 `NO REVISADA`**. Sentencias: 4 de las 17 de lectura parcial. **Alto impacto: 20 de 32 con consulta propia**, 11 regional, **Aguascalientes `NO REVISADA`**.

## 10. Hechos vistos y NO fichados

Ver §7 (Xalapa y Temixco retirados, San Baltazar Tetela, Juchitán, León, Chignahuapan, Radio Hoy) · Sinaloa, SSP: ejido Canán (16-oct, por resumen), Escuinapa (12-oct), Mazatlán (14-oct), 1 y 4-oct: anteriores · Guerrero, Mesa de Coordinación, semanas del 28-sep y del 5-oct: anteriores · Hidalgo, Tlaxcoapan, 4 largas, 3 cortas (fecha no fijada) · Edomex, GN 9-11 oct (agregado) · Nuevo Laredo, 15 detenidos (9-oct) · Reynosa (13 y 16-oct) · Zacatecas, dos «generadores de violencia» (sin fecha) · Pinotepa Nacional, periodista asesinado el 9-oct (ya publicado: `ARG-128-001`) · Quintana Roo, Santa Cecilia (16-oct) y SM 69 (14-oct) · Almoloya de Juárez (ya en 135, ventana de 130) · Morelos, «El Güero Gym» (12-oct, *liveblog*) · Torreón (1-oct).

## 11. Sentencias — candidatas y vistas

| Caso | Disposición |
|---|---|
| **Ensenada**, tres sentenciados (alias de uno no reproducido) | **158 años 9 meses a cada uno** = 135 (homicidio calificado) + 10 años 9 meses (robo calificado con violencia) + 13 (robo de vehículo con violencia), **solo por resumen**; reparación **1,628,550 pesos + 19,542** por gastos funerarios, solo por resumen; hechos del 27-28 abr 2024 en Punta San José; fallo del 9-oct e individualización del 16. Infobae 2026/10/17, miled 2026/10/17. **Boletín no localizado** (`fgebc.gob.mx` devolvió el 15368, caso conexo de 20 años). `PENDIENTE DE CONFIRMACIÓN OFICIAL`; seguimiento de la candidata de 135 |
| Hermosillo, 25 años | Tribuna 2026/10/16; sin boletín; ventana de 135 |
| Veracruz, comunicador, 21 años (J-10/2026) | 15-oct; el término de la FGE sería «comunicador» (por resumen): el cartelón dice «comunicador» |
| FGR Cosoleacaque y Banderilla | 15-oct; sin boletín |
| FGE Guerrero, cinco sentencias del listado del 15-oct | Solo por resumen, sin URL individual |

## 12. Desglose de cálculos propios

- **Entidades**: 6, por la entidad de la autoridad que actúa (Taxco: FGE Guerrero); Maravatío (Mich.), lugar de la detención de `-008`, no suma entidad.
- **Muertos en hechos propios**: Salamanca 2 + Acapulco 2 + Acapulco 2 + Culiacán 1 + Ensenada 1 = **8** (7 sin Ensenada: causa no determinada). Heridos: 3 por titular en `-002` (4 contradicho). Detenidos sin aseguramiento: 1 (`-006`) + 2 (`-007`, 1 en otro medio) + 1 (`-008`) + 1 (`-009`) = **5** (4 si en Puebla fue 1).
- **Armamento**: **sin total nacional verificable**; ninguna fila.
- **Duración**: 17-oct 09:28 → 18-oct 08:34 = 23 h 06 min. **Densidad**: 9 / 23,1 h = 0,390 → **0,39**.
- **FRONTERA**: 1 de 9 (`-004`); **publicados el día de apertura sin hora**: 4 (`-005`, `-007`, `-008`, `-009`).

## 13. Los dos controles editoriales

**Primera ronda** (sobre `003942a`, con las notas íntegras de los seis equipos y del coordinador; informes en el *scratchpad*: `control-procedencia-r1.md`, `control-duplicidad-r1.md`):

- **`procedencia-cifras`**: veinte hallazgos, **diecinueve «CORREGIR»** (sin hallazgo: el n.º 12, los 3 heridos de Acapulco, sostenido por titular); 30 búsquedas. **Aplicados todos**: 1 (Xalapa retirado), 2-4 (Temixco retirado: día no fijado, homonimia, sin ocultamiento), 5 (exfiscal ~10:20 por RND; sin marca de apertura; portada 4), 6 (fuentes con fecha del exfiscal; abril y El Pinal por resumen), 7 (detenidos de Puebla contradichos; recuento 5), 8-9 (Tanquián «reportado como elemento»; marcas), 10 (Culiacán, colonia contradicha; Línea Directa), 11 (Salamanca, esquina contradicha; El Salmantino), 13 (**Acapulco, Vicente Guerrero → `-003`**), 14 (**Cuauhtémoc, Chih. → `-REC-003`**), 15 (**Maneadero → `-005`**), 16 (conclusión 2 reescrita), 17 (Nogales: «hallazgos»), 18-19 (cobertura con lecturas parciales), 20 (Chignahuapan).
- **`editor-duplicidad`**: veinte pases, **quince «CORREGIR»** (2, 3, 5 a 8, 10, 12, 13, 15 a 20) y cinco «SIN HALLAZGO» (1, 4, 9, 11, 14); el informe se tituló «14 / 6» por error de recuento, corregido por el propio control en la segunda ronda. **Aplicados**: 2 (deslinde de Silao con 133-REC-002/-003), 3 (**Taxco fichado: `-008`, `-009`**), 5 (Temixco y Tetela retirados: conclusión 3 → Apatzingán, conclusión 4 → Taxco), 6 (portada 3 → Tepic, `ARG-135-011`), 7 (conclusiones 2 y 5 reescritas; Industrial Bravo solo en «vistos»), 8 (deslinde de dos fichas, oración de ARM y «Toque un ARG-ID» retirados), 10 (títulos de Acapulco y Tanquián; AIC «alertada»; exfiscal con fragmentos), 12 (**San Baltazar Tetela a 🟡, no recuperable**), 13 (Tanquián, título y FE condicional), 15 (Morelos y Nayarit a `NO REVISADA` en armamento; indicadores oficiales SRIV), 16 (seguimientos: Cachanillas compatible, Nogales «hallazgos», Chiapa de Corzo fuera del cartelón), 17 (**ciclo: advertencia escrita en §3**; Pinotepa = `ARG-128-001`; El Balcón; Linares `DÍA CONTRADICHO`), 18 (indicio 7 + 4; arbitraje de ARM-002; cotejo con La Popular), 19 (FE), 20 (índice y pendientes: escritos al cierre, tras la segunda ronda). **No aplicado, con motivo**: 17.1, cambiar a ciclo C — **el destinatario ordenó B**; se deja la advertencia y la decisión a 137.

**Segunda ronda** (sobre `900a00a`, sin búsquedas; informes en `reports/argos-2026-10-18-equipos.md`):

- **`procedencia-cifras`**: veinte hallazgos, **quince «CORREGIR»** (16 a 20 sin hallazgo: aritmética, cobertura y `-REC-003` verificados). **Aplicados todos**: 1 (`-003` «dos personas»; hombres por resumen; deslindes con Zihuatanejo y entre `-002` y `-003`), 2 (títulos de `-004` y `-007`), 3 (exfiscal: «dos» agentes, juez de control y corporaciones **por resumen**; «exfiscal de Chihuahua»), 4 (recuentos: `-006` N 13 / R 4 con Politico.mx, UnoTV y Radionet; `-REC-001` R 5; `-REC-003` sin «mismo grupo»; `-009` **conserva N 5 / R 3: los cinco medios salieron en la búsqueda 3 del coordinador, cuyas URL se añadieron a las notas**), 5 (`-008`: «homicidio de seis policías»; 2020 y «estatales» por resumen), 6 (deslinde de Maneadero con `ARG-120-019`), 7 (Tanquián: columna nacional y reserva de adscripción), 8 (totales con reserva de Ensenada y Puebla; columna «Detenidos en aseguramiento»; «Orden: …» retirado), 9 (seguimientos con la cifra citable de Punto Norte), 10 (conclusiones con marcas), 11 (vistos de armamento), 12 (sentencias vistas con marcas), 13 (errores de acceso), 14 (este archivo, índice y pendientes), 15 (Salamanca: día del hecho por la hora).
- **`editor-duplicidad`**: veinte pases, **once «CORREGIR»** (1, 4, 6, 8, 12, 13, 14, 15, 17, 18, 20). **Aplicados**: 1 (este §13, §3 con la cita de la orden de ciclo, §5 Cachanillas, §15 renumerado), 4, 6 (**`-009`: los datos tienen respaldo en la búsqueda 3 del coordinador, todos marcados por resumen; URL añadidas a las notas**; «secuestro agravado» y La Familia Michoacana se conservan con la marca), 8 (FE-002 con los amarillos no recuperados), 12 (conclusiones 1 a 4 declaran a qué patrón previo se suman), 13 (tarjeta de sentenciados; leyenda del mapa sin explicación de color), 14 («armamento asegurado: no publicado»), 15, 17 (huérfano retirado; `validar.js` y el móvil, a deuda), 18 (errores de acceso), 20 (índice y pendientes escritos).

## 14. Herramientas

`tools/datos-argos-136.py` (copia de la estructura de 135) → `reports/argos-2026-10-18.html`; `gen-movil.py 136 2026-10-18 135 2026-10-17 08:34`; `gen-texto.py`; `validar.js … 2026-10-17 2026-10-18` → «validación OK».

## 15. Lecciones de método (no van al cartelón)

1. **La pista de control trajo los dos rojos-candidatos del sábado** (Silao, Acapulco): Silao resultó anterior a la apertura. La consulta de control en `extended` es también la primera búsqueda útil del corte.
2. **El índice no llega al sábado por la noche en Noreste, Golfo ni Centro**; la búsqueda final «madrugada de este domingo» del coordinador trajo tres candidatos que la ola no vio, de los que **solo Culiacán (`-004`) sobrevivió**: Xalapa era del 3-oct y Temixco no tenía día fijado. **`procedencia-cifras` volvió a encontrar tres hechos** (`-003`, `-005`, `-REC-003`), como en 135.
3. **Un hallazgo del buscador con «madrugada de este domingo» no fecha el hecho**: el resumen atribuyó a Xalapa una frase de otra nota. Antes de fichar, una ruta fechada o un titular con día.
4. **Por primera vez en nueve ediciones**, el buscador devolvió el dominio de la SSP de Sinaloa y el de la fiscalía de Sonora (`fiscalia.sonora.gob.mx`, no `fge.sonora`).
5. **El equipo Golfo encontró un hecho de otra región** (Tanquián, SLP): conviene que cada equipo pase lo ajeno al coordinador, como hizo.

## 16. Emisores por ficha (lista íntegra)

- `ARG-136-001` — Institucional: SIN BOLETÍN · Nacional: Milenio · Con fecha en la ruta: AM (2026/10/17) · Regionales: AM, Meganoticias, Guanajuato Informa, El Salmantino · Recuento I 0 / N 1 / R 4 / A 0
- `ARG-136-002` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: ninguna · Regionales: Quadratín Guerrero, Bajo Palabra · Recuento I 0 / N 0 / R 2 / A 0
- `ARG-136-003` — Institucional: SIN BOLETÍN · Con fecha en la ruta: ninguna · Regional: Quadratín Guerrero · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-136-004` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Luz Noticias (2026-10-18), Línea Directa (2026-10-18) · Regionales: Luz Noticias, Línea Directa, Noroeste, Café Negro, El Sol de Sinaloa, Los Noticieristas (2026/10) · Recuento I 0 / N 0 / R 6 / A 0
- `ARG-136-005` — Institucional: SIN BOLETÍN · Con fecha en la ruta: ninguna (Zeta 2026/10) · Regionales: Zeta, El Congresista · Recuento I 0 / N 0 / R 2 / A 0
- `ARG-136-006` — Institucional: Fiscalía de Chihuahua (por cita) · Nacional: Proceso, El Financiero, La Jornada, CNN en Español, Expansión, Infobae, La Razón, Publimetro, La Silla Rota, Politico.mx, Reforma, Excélsior, UnoTV (El Universal, Forbes e Informador citados, no contados) · Con fecha en la ruta: Proceso, El Financiero, La Jornada, CNN en Español, Expansión, Infobae, La Razón, Publimetro, La Silla Rota, Politico.mx (2026/10/17), Luz Noticias (2026-10-17) · Regionales: Luz Noticias, Crónica Regional, El Congresista, Radionet · Recuento I 1 / N 13 / R 4 / A 0
- `ARG-136-007` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Paralelo19 (2026/10/17) · Regionales que sostienen la detención: Paralelo19, Ambas Manos, Estrella Digital, Curul Puebla, Urbano Tlaxcala (singular) · Recuento I 0 / N 0 / R 5 / A 0
- `ARG-136-008` — Institucional: SIN BOLETÍN (boletín de la FGE Guerrero solo por resumen) · Nacional: Milenio, N+, La Silla Rota · Con fecha en la ruta: La Silla Rota (2026/10/17) · Regionales: Quadratín Guerrero, Sur Acapulco, Telediario · Recuento I 0 / N 3 / R 3 / A 0
- `ARG-136-009` — Institucional: SIN BOLETÍN (URL en las notas del coordinador, búsqueda 3) · Nacional: Proceso, El Universal, Milenio, UnoTV, La Jornada · Con fecha en la ruta: Proceso (2026/10/17), La Jornada (2026/10/18) · Regionales: Quadratín Guerrero, Bajo Palabra, Tribuna de México · Recuento I 0 / N 5 / R 3 / A 0
- `ARG-136-REC-001` — Institucional: SIN BOLETÍN · Nacional: Milenio · Con fecha en la ruta: AM (2026/10/17) · Regionales: AM, Quinta Fuerza, Guanajuato Informa, Telediario, Observatorio Informativo · Recuento I 0 / N 1 / R 5 / A 0
- `ARG-136-REC-002` — Institucional: SIN BOLETÍN · Nacional: N+, Milenio · Con fecha en la ruta: Potosinoticias (2026/10/16) · Regionales: Potosinoticias, Pulso, Código San Luis, San Luis Hoy, Global Media, La Opinión, Consulta Monterrey · Recuento I 0 / N 2 / R 7 / A 0
- `ARG-136-REC-003` — Institucional: SIN BOLETÍN · Con fecha en la ruta: El Diario de Chihuahua, diario.mx, El Diario del Noroeste (2026/oct/17; independencia no verificada) · Recuento I 0 / N 0 / R 3 / A 0
