# ARGOS 136 — Archivo de fuentes

**Corte**: 2026-10-18 · **Ventana**: 17-oct 09:28 → 18-oct 08:34 CDMX (**23 h 06 min**; `WINDOW_DAYS = 2`) · **Densidad**: 7 hechos propios / 23,1 h = **0,30 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 08:34 CDMX). Las consultas continuaron hasta las **09:45 CDMX** (marca «Consulta» del cartelón); los hechos posteriores a las 08:34 pertenecen a ARGOS 137.

Informes íntegros de los seis equipos: extraídos al *scratchpad* de la sesión (`informe-<región>.md`, más `notas-coordinador.md`) y entregados a los controles.

## 1. La base

- Clon con HEAD suelto en `60f2777` (cuarta edición seguida). Se abrió `claude/argos-136` y se fusionó en *fast-forward* `main` (`b0558a3`), `claude/argos-129` … `-135`, en ese orden y sin conflicto. HEAD de partida: `2338846`.
- `reports/`: 189 archivos, última edición `argos-2026-10-17` (ARGOS 135), como estaba previsto.
- **Herramientas** (commit `8a99ea8`, deuda 9 de 135): `gen-texto.py` emite en **orden de documento** (antes extraía por tipo y separaba cada subtítulo de su contenido; probado sobre 135: mismo contenido, otro orden); `gen-movil.py` retira «Toque un ARG-ID» (el índice no se publica en el teléfono), «mismo contenido verificado» y «totales en las tarjetas de arriba».

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (`CONNECT tunnel failed, response 403`), 08:34. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**. Además, 16 servidores MCP de complementos no conectaron por el mismo 403 del proxy (sin efecto en ARGOS).
- **Consulta de control** («ataque armado muertos "17 de octubre" 2026 México», en los dos modos): `standard` **ningún hecho del 17**; `extended`, Silao (Baños de Agua Caliente) y Acapulco (col. Cuauhtémoc). **Se mantuvo `extended` obligatorio.** Silao resultó de la ventana de 135 (→ `ARG-136-REC-001`); Acapulco, del corte (→ `ARG-136-002`).
- **Presupuesto**: control 2 + ola (Noroeste 26, Noreste 25, Occidente 28, Centro 28, Golfo y federal 28, Sureste 24 = **159**) + **7 del coordinador** = **168**; `procedencia-cifras` hasta **30** → hasta **198 de 200**.

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (21 `NO REVISADA` + 8 por portal en 135) | **Por dominio propio ahora (12 de las 21)**: BC (`seguridadbc.gob.mx`), BCS (`sspbcs.gob.mx`), Son (`ssp.sonora.gob.mx`, solo portada), Sin (`sspsinaloa.gob.mx`, **primer dominio devuelto en nueve ediciones**), Mich (`ssp.michoacan.gob.mx`), Gto (`seguridad.guanajuato.gob.mx`, una página), CDMX (`ssc.cdmx.gob.mx`), Edomex (`sseguridad.edomex.gob.mx`), Pue (`ssp.puebla.gob.mx`), Chis (`sspc.chiapas.gob.mx`), QRoo (`ssc.qroo.gob.mx`) y Zac (`ssp.zacatecas.gob.mx`, de las 8 por portal); Nay por `fgenay.gob.mx`. **Por portal estatal (3)**: NL (`nl.gob.mx/boletines`), Mor (`morelos.gob.mx`), Gro (`guerrero.gob.mx`). **Siguen o pasan a `NO REVISADA` (16)**: Dgo, SLP, Jal, Tlax, Hgo, Qro, Camp (dominio no devuelto) · Chih, Coah, Tamps, Col, Ags, Ver, Tab, Oax, Yuc (sin consulta de dominio propio, o dominio no devuelto) |
| Prioridad — sentencias (14 `NO REVISADA` en 135) | **Revisadas (11 de 14)**: BC (`fgebc.gob.mx`), Son (`fiscalia.sonora.gob.mx`, **primer dominio devuelto en nueve ediciones**, solo convocatorias), Chih (`fiscalia.chihuahua.gob.mx`), Coah (`sitio.fgecoahuila.gob.mx`), Mich (`comunicacion.fiscaliamichoacan.gob.mx`), Nay (`fgenay.gob.mx` — el dominio de la plantilla, `fiscalianayarit.gob.mx`, no devuelve), Ags (`fiscalia-aguascalientes.gob.mx`), CDMX (`fgjcdmx.gob.mx`), Tlax (`pgjtlaxcala.gob.mx`, solo páginas administrativas), Gro (`fiscaliaguerrero.gob.mx`), Yuc (`fge.yucatan.gob.mx`). **Siguen `NO REVISADA`**: Sin (`fiscaliasinaloa.gob.mx` no devuelto, novena edición), Hgo (`pgjhidalgo.gob.mx` no devuelto), Camp (`fgecam.gob.mx`: el buscador vuelve a ignorar el `site:`) |
| Ciclo | **B** — Noreste y Golfo encabezaron el triaje judicial tras la prioridad |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Noreste: NL, Tamps, SLP (boletines sin fecha en ruta), Zac revisadas, SRIV; Coahuila saldada. Golfo: FGE Veracruz en `comunicacion.fiscaliaveracruz.gob.mx` (no en `fiscaliaveracruz.gob.mx`) y FGE Tabasco revisadas, SRIV; nombre y causa del caso del comunicador (J-10/2026) confirmados por medios |
| Regresión por rotación | Sentencias: BCS, Dgo, Jal, Col, Gto, Edomex, Mor, Pue, Qro, Oax, Chis, QRoo pasan a `NO REVISADA`. Armamento: Chih, Coah, Tamps, Col, Ags, Ver, Tab, Oax, Yuc pasan a `NO REVISADA`. **Prioridad sobre el ciclo en 137** |

Serie: … · A (135) no · **B (136) no.**

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
| **«Pokémon» ↔ Laguna Colorada** (`ARG-135-008` ↔ `ARG-134-016`) | **Distintos, con reserva**: 4 detenidos frente a 7; célula con HSI frente a 5 cateos con Semar, SSPC, GN y FGR; publicación del 16 frente a operativo del 15 (Ríodoce 2026/10/15); familias distintas. Coincide solo «cuatro armas». Domicilios: no publicados en ninguna fuente. **Nueva posible duplicidad**: SSP Sinaloa, col. Industrial Bravo, «cuatro civiles armados», 1 ametralladora 7.62 y 385 cartuchos 7.62 (`sspsinaloa.gob.mx/post/cuatro-civiles-armados-…`, fecha no fijada; 13-16 oct por resumen): coincide en 4 detenidos y ametralladora; cartuchos y corporación distintos. **`ARG-135-ARM-001` sigue fuera del total** (ver §8) |
| **Cateos de Mazatlán y El Carrizal** (`-009`, `ARM-002`) | **No son el renglón del boletín del 15-oct**: los medios los atribuyen a un comunicado conjunto **Semar–SSPC–FEMDO del 16-oct** (MexNoticias, por resumen; Reforma al Gabinete). Rutas del 16: tusbuenasnoticias, Luz Noticias, El Diario de Chihuahua, diario.mx. Fecha de los cateos: no publicada. El Carrizal: 1 arma larga, cartuchos y dos cajas de municiones sin cifra, metanfetamina; **todo solo por resumen**. Se retira la marca «posible evento anterior»; **sigue fuera del total por cifra solo por resumen** |
| **Apatzingán** (`ARG-135-003`) | Hora **no fijada** (Quadratín, La Voz de Michoacán, El Congresista). Hallazgos «simultáneos», por resumen. Sin identificación. 134 o 135 sigue abierto |
| **Linares** (`ARG-135-REC-001`) | **Jueves 15 ~22:00** en las rutas fechadas (MVS 2026/10/16, Punto x Punto 2026/10/16 ×2, Enfoque Monterrey 2026/10/17), por resumen; «miércoles» solo en Milenio y Telediario, sin fecha en ruta. **La URL de El Mañana 2026/10/15 que 135 dio como primera publicación es el doble homicidio de Gómez Morín (Monterrey), no Linares** (equipo Noreste). Primera publicación de Linares: **16-oct**. → ventana de **134**; ver §8. Herido: sobrevivió (El Porvenir) o murió (resumen de Punto x Punto): contradicho |
| **Tijuana, Divina Providencia** (`-002`) | Sin ruta con día (Zeta y Diario Tijuana, solo `2026/10/`); identificación por «información preliminar de los cuerpos de seguridad», no de la FGE; Milenio titula «dos mujeres y bombero» (3) frente a 2 en el resto: **contradicho, sin arbitrar** |
| **Cachanillas** (`-REC-003`) | Colectivo Buscando a Tolano; hallazgo del jueves 15 (Diario Tijuana, Infobaja). **Punto Norte 2026/10/17: «6 cuerpos y osamentas apilados»** (4 cuerpos y 2 esqueletos) frente a 4: contradicho. Sin cifra oficial; la FGE llegó después y retiró al colectivo (por resumen) |
| **Nogales** (`-REC-004`) | **El Imparcial 2026/10/17: 2 osamentas más en Mariposa; «siete hallazgos en cinco fosas durante dos días»** (15 y 16-oct), Buscadoras de la Frontera. Fiscalía de Sonora resguarda. Seguimiento en el panorama |
| **Ajuchitlán** (`-010`) | Rescate del **16-oct** por ruta. **La séptima persona sigue sin localizarse** (Infobae 2026/10/18). Defensa, 9.ª Región Militar, por resumen. Amparo 412/2026 del 5-oct (ONG, por resumen). El ejido: «liberados, no rescatados» |
| **Taxco, 6 policías (2020)** | **«El Gallinero»**, 1 detenido en Maravatío (Mich.) por FGE Guerrero con FGE Michoacán, Defensa y GN; boletín de la noche del 16 (Quadratín, por resumen); La Silla Rota 2026/10/17. Fecha de la detención no publicada → **ventana de 135, acción institucional: no recuperable** |
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
| **Colores pendientes del destinatario** | Patamban, Coatzacoalcos, San Blas Atempa (Quadratín: «**ex**dirigente de la Sección 22»; otros, docente), Iztapalapa, Cajeme: sin dato nuevo. **Nuevos**: San Baltazar Tetela (`-REC-002`) y Tanquián (`-REC-003`), ver §7 |

## 6. Seguimientos sin cambio de ficha

Coatzacoalcos (expareja prófuga, Golpe Político 2026/10/17) · Orizaba · Villahermosa · San Blas Atempa (sin detenidos) · Jerez (número no determinado) · Atotonilco · Hermosillo `-005`/`-006` (sin segunda fuente; «hombre de 51 años», Medios Obson 2026/10/17, no atribuible) · Iztapalapa, Xochimilco, Mazatepec, Toluca, Ecatepec: no consultados por presupuesto · Patamban: no consultado · Barrio 18 (QRoo): no consultado.

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Salamanca, col. Guanajuato** (`-001`) | Occidente; AM `…/salamanca/2026/10/17/…-1856213.html` fija el sábado; ~17:30 por resumen, posterior a la apertura. 🔴 por homicidio múltiple. **NO es** `ARG-133-002` (bulevar Valle de Santiago, 14-oct) |
| **Acapulco, col. Cuauhtémoc** (`-002`) | Pista de control; Sureste y coordinador: sábado 17 ~17:30/18:00 solo por resumen, **ninguna ruta con fecha** → ★★☆☆☆. 🔴 por homicidio múltiple. Homónimo de noviembre de 2025 (3 muertos, 2 heridos) descartado |
| **Culiacán, Estela Ortiz** (`-003`), **Xalapa** (`-004`), **Temixco** (`-005`) | Hallados por el coordinador («madrugada de este domingo»). `-003` con ruta del 18 (Luz Noticias); `-004` y `-005`, fuente única sin fecha en ruta. 🟡 cada uno |
| **Exfiscal de Chihuahua** (`-006`) | Noroeste lo trajo como titular de Informador (ruta `20261017`); coordinador: sábado 17 «esta mañana», por resumen → **`PUBLICADO EL DÍA DE APERTURA SIN HORA`**; puede ser de 135. 🟢. **Nombre no reproducido** en el cartelón |
| **San Baltazar Tetela** (`-REC-002`, `-007`) | Centro: ataque de la «madrugada» del 17, por resumen → **ventana de 135**, no publicado. **Color 🔴 propuesto por víctima civil ajena al ataque dirigido (menor de edad), agravante de la lista; un solo muerto: decisión del destinatario.** Detención de dos (San Pedro Zacachimalpa), hora no fijada → 🟢 del corte con marca. **Un hecho y su detención: dos fichas** |
| **Silao, Baños de Agua Caliente** (`-REC-001`) | ~06:30 o ~07:20 por resumen, antes de las 09:28 → **ventana de 135**. 🔴 por homicidio múltiple |
| **Tanquián de Escobedo** (`-REC-003`) | Golfo lo pasó a Noreste; coordinador: jueves 15 por la noche (Potosinoticias 2026/10/16) → **ventana de 134**. 🔴 por víctima elemento de una fuerza de seguridad; **adscripción contradicha** (GN en descanso o exagente de la Guardia Civil Estatal): **decisión del destinatario** |
| **Taxco, director de Reglamentos** | Detenido el **viernes 16** (Quadratín, por resumen) con un policía; Proceso 2026/10/17; secuestro del padre del alcalde del 11-abr. Ventana de 135; acción institucional: **visto, no recuperable** |
| **Juchitán, ataque a un diseñador muxe** | Dos detenidos; Proceso 2026/10/16, El Imparcial 2026/10/17; ataque de septiembre. Ventana de 135: **visto, no recuperable** |
| **León, Valle Hermoso** | 1 muerto y 1 herido, noche del viernes 16 → 🟡 de 135, no recuperable |
| **Chignahuapan** | Seis cateos, 9 detenidos, 1 arma, 1 cargador, «18 elementos balísticos»; Excélsior sin fecha en ruta; fecha no fijada → visto |
| **Radio Hoy, Caribe Verde** | Ruta 2026/10/17, entidad no determinada → visto, no atribuible |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-136-FE-001`** — **Linares** (`ARG-135-REC-001`): primera publicación **16-oct**, no 15 (la URL de El Mañana era de otro hecho); jueves 15 por la noche en las rutas fechadas → **ventana de 134**; se retira la alternativa «133 si fue el 14». **El Guayabo** (`ARG-134-REC-003`): martes 13 → **ventana de 132** (por resumen). **Chiapa de Corzo** (`ARG-134-REC-002`): 14-oct por ruta → **132 o 133 según la hora**. Cálculo propio: **132: +1 rojo y 2 muertos** (El Guayabo), **más 1 rojo y 2 muertos si Chiapa de Corzo fue antes de las 08:19**; **133 pierde las dos alternativas** (El Guayabo y Linares) y conserva Chiapa de Corzo como alternativa; **134: Linares fijado** en su ventana. El rango de 133 se recalcula en `_pendientes.md` contra `argos-2026-10-15-fuentes.md`, no aquí.
- **`ARG-136-FE-002`** — **Recuperaciones de este corte**: Silao (`-REC-001`) y San Baltazar Tetela (`-REC-002`) añaden **2 rojos y 3 muertos a ARGOS 135** (3 → 5 rojos; 12 → 15 muertos). Tanquián (`-REC-003`) añade **1 rojo y 1 muerto a ARGOS 134** (hasta 9 rojos). Cálculo propio.
- **`ARG-136-FE-003`** — **Armamento de 135**: `ARM-001` deja de estar en duplicidad con `ARG-134-ARM-001` y pasa a **posible duplicidad con el aseguramiento de la SSP Sinaloa en Industrial Bravo**: sigue fuera del total. `ARM-002`: retirada la marca de evento anterior (comunicado del 16, no boletín del 15); sigue fuera por cifra solo por resumen. **Sin cambio en los totales de 135.**
- **Actualización de dato, no fe de erratas**: Nogales (7 osamentas en 5 fosas) · Cachanillas (6, contradicho) · Ajuchitlán (séptima persona) · Tepic (imputado, sin vinculación) · Divina Providencia (2 o 3, contradicho) · Tlalnepantla (sexo no confirmado).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | propia · seguimientos | SRIV (`seguridadbc.gob.mx`) | SRIV (`fgebc.gob.mx`) |
| Baja California Sur | regional | SRIV (`sspbcs.gob.mx`) | NO REVISADA |
| Sonora | propia · seguimientos | SRIV (`ssp.sonora.gob.mx`, portada) | SRIV (`fiscalia.sonora.gob.mx`) |
| Chihuahua | propia · **hecho** (`-006`) | NO REVISADA | SRIV (`fiscalia.chihuahua.gob.mx`) |
| Sinaloa | propia · **hecho** (`-003`) | SRIV (`sspsinaloa.gob.mx`; Industrial Bravo sin fecha) | NO REVISADA |
| Durango | regional | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Coahuila | regional | NO REVISADA | SRIV (`sitio.fgecoahuila.gob.mx`) |
| Nuevo León | propia · seguimientos | por portal (`nl.gob.mx`) | SRIV (`fiscalianl.gob.mx`) |
| Tamaulipas | propia (fosas) | NO REVISADA (dominio no devuelto) | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | propia · **`-REC-003`** | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | propia · seguimiento | SRIV (`ssp.zacatecas.gob.mx`) | SRIV (`fiscaliazacatecas.gob.mx`) |
| Jalisco | regional | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Colima | propia · seguimientos | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Nayarit | propia · seguimiento | SRIV (`fgenay.gob.mx`) | SRIV (`fgenay.gob.mx`) |
| Aguascalientes | NO REVISADA | NO REVISADA (dominio no devuelto) | SRIV (`fiscalia-aguascalientes.gob.mx`) |
| Michoacán | propia · seguimientos | SRIV (`ssp.michoacan.gob.mx`) | SRIV (`comunicacion.fiscaliamichoacan.gob.mx`) |
| Guanajuato | propia · **hecho** (`-001`) · **`-REC-001`** | SRIV (`seguridad.guanajuato.gob.mx`) | NO REVISADA |
| Ciudad de México | regional · seguimiento | SRIV (`ssc.cdmx.gob.mx`) | SRIV (`fgjcdmx.gob.mx`) |
| Estado de México | regional · seguimiento | SRIV (`sseguridad.edomex.gob.mx`) | NO REVISADA |
| Morelos | propia · **hecho** (`-005`) | por portal (`morelos.gob.mx`) | NO REVISADA |
| Puebla | propia · **hecho** (`-007`) · **`-REC-002`** | SRIV (`ssp.puebla.gob.mx`) | NO REVISADA |
| Tlaxcala | regional | NO REVISADA (dominio no devuelto) | SRIV (`pgjtlaxcala.gob.mx`, administrativas) |
| Hidalgo | propia · seguimientos | NO REVISADA (dominio no devuelto) | NO REVISADA (dominio no devuelto) |
| Querétaro | regional · «El Tripa» | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Veracruz | propia · **hecho** (`-004`) | NO REVISADA (dominio no devuelto) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | propia | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | propia · **hecho** (`-002`) · seguimientos | por portal (`guerrero.gob.mx`, semanal del 5-11 oct) | SRIV (`fiscaliaguerrero.gob.mx`, listados del 15-oct) |
| Chiapas | propia · seguimiento | SRIV (`sspc.chiapas.gob.mx`) | NO REVISADA |
| Oaxaca | propia · seguimiento | NO REVISADA | NO REVISADA |
| Campeche | regional | NO REVISADA (`site:` ignorado) | NO REVISADA (`site:` ignorado) |
| Yucatán | regional | NO REVISADA | SRIV (`fge.yucatan.gob.mx`) |
| Quintana Roo | regional | SRIV (`ssc.qroo.gob.mx`) | NO REVISADA |

**Sentencias: 17 de 32**; FGR revisada por búsqueda; **15 `NO REVISADA`**. **Armamento: 13 de 32 por dominio propio**, **3 por portal estatal**, **16 `NO REVISADA`**. **Alto impacto: 20 de 32 con consulta propia**, 11 regional, **Aguascalientes `NO REVISADA`**.

## 10. Hechos vistos y NO fichados

Ver §7 (Taxco, Juchitán, León, Chignahuapan, Radio Hoy) · Sinaloa, SSP: ejido Canán (16-oct, por resumen), Escuinapa (12-oct), Mazatlán (14-oct), 1 y 4-oct: anteriores · Guerrero, Mesa de Coordinación, semanas del 28-sep y del 5-oct: anteriores · Hidalgo, Tlaxcoapan, 4 largas, 3 cortas (fecha no fijada) · Edomex, GN 9-11 oct (agregado) · Nuevo Laredo, 15 detenidos (9-oct) · Reynosa (13 y 16-oct) · Zacatecas, dos «generadores de violencia» (sin fecha) · Pinotepa Nacional, periodista asesinado el 9-oct (no cotejado con 131: pendiente) · Quintana Roo, Santa Cecilia (16-oct) y SM 69 (14-oct) · Almoloya de Juárez (ya en 135, ventana de 130) · Morelos, «El Güero Gym» (12-oct, *liveblog*) · Torreón (1-oct).

## 11. Sentencias — candidatas y vistas

| Caso | Disposición |
|---|---|
| **Ensenada**, tres sentenciados (alias de uno no reproducido) | **158 años 9 meses a cada uno** = 135 (homicidio calificado) + 10 años 9 meses (robo calificado con violencia) + 13 (robo de vehículo con violencia), **solo por resumen**; reparación **1,628,550 pesos + 19,542** por gastos funerarios, solo por resumen; hechos del 27-28 abr 2024 en Punta San José; fallo del 9-oct e individualización del 16. Infobae 2026/10/17, miled 2026/10/17. **Boletín no localizado** (`fgebc.gob.mx` devolvió el 15368, caso conexo de 20 años). `PENDIENTE DE CONFIRMACIÓN OFICIAL`; seguimiento de la candidata de 135 |
| Hermosillo, 25 años | Tribuna 2026/10/16; sin boletín; ventana de 135 |
| Veracruz, comunicador, 21 años (J-10/2026) | 15-oct; el término de la FGE sería «comunicador» (por resumen): el cartelón dice «comunicador» |
| FGR Cosoleacaque y Banderilla | 15-oct; sin boletín |
| FGE Guerrero, cinco sentencias del listado del 15-oct | Solo por resumen, sin URL individual |

## 12. Desglose de cálculos propios

- **Muertos en hechos propios**: Salamanca 2 + Acapulco 2 + Culiacán 1 + Xalapa 1 + Temixco 1 = **7**. Heridos: 3 por titular en `-002` (4 contradicho). Detenidos sin aseguramiento: 1 (`-006`) + 2 (`-007`) = **3**.
- **Armamento**: **sin total nacional verificable**; ninguna fila.
- **Duración**: 17-oct 09:28 → 18-oct 08:34 = 23 h 06 min. **Densidad**: 7 / 23,1 h = 0,303 → **0,30**.
- **FRONTERA**: 2 de 7 (`-003`, `-004`); **publicados el día de apertura sin hora**: 2 (`-006`, `-007`).

## 13. Los dos controles editoriales

*(Se completa tras la primera ronda.)*

## 14. Herramientas

`tools/datos-argos-136.py` (copia de la estructura de 135) → `reports/argos-2026-10-18.html`; `gen-movil.py 136 2026-10-18 135 2026-10-17 08:34`; `gen-texto.py`; `validar.js … 2026-10-17 2026-10-18` → «validación OK».

## 15. Lecciones de método (no van al cartelón)

1. **La pista de control trajo los dos rojos-candidatos del sábado** (Silao, Acapulco): Silao resultó anterior a la apertura. La consulta de control en `extended` es también la primera búsqueda útil del corte.
2. **El índice no llega al sábado por la noche en Noreste, Golfo ni Centro**; la búsqueda final «madrugada de este domingo» del coordinador trajo tres hechos (`-003`, `-004`, `-005`) que la ola no vio.
3. **Por primera vez en nueve ediciones**, el buscador devolvió el dominio de la SSP de Sinaloa y el de la fiscalía de Sonora (`fiscalia.sonora.gob.mx`, no `fge.sonora`).
4. **El equipo Golfo encontró un hecho de otra región** (Tanquián, SLP): conviene que cada equipo pase lo ajeno al coordinador, como hizo.

## 16. Emisores por ficha (lista íntegra)

- `ARG-136-001` — Institucional: SIN BOLETÍN · Nacional: Milenio · Con fecha en la ruta: AM (2026/10/17) · Regionales: AM, Meganoticias, Guanajuato Informa · Recuento I 0 / N 1 / R 3 / A 0
- `ARG-136-002` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: ninguna · Regionales: Quadratín Guerrero, Bajo Palabra · Recuento I 0 / N 0 / R 2 / A 0
- `ARG-136-003` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Luz Noticias (2026-10-18) · Regionales: Luz Noticias, Noroeste, Café Negro · Recuento I 0 / N 0 / R 3 / A 0
- `ARG-136-004` — Institucional: SIN BOLETÍN · Con fecha en la ruta: ninguna · Regional: XEU · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-136-005` — Institucional: SIN BOLETÍN · Con fecha en la ruta: ninguna · Regional: La Unión de Morelos · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-136-006` — Institucional: Fiscalía de Chihuahua (por cita) · Nacional: El Financiero, La Jornada, CNN en Español, Expansión, Reforma, Excélsior, El Universal · Con fecha en la ruta: El Financiero (2026/10/17), La Jornada (2026/10/17), CNN en Español (2026/10/17), Expansión (2026/10/17) · Regionales: Crónica Regional, El Congresista · Recuento I 1 / N 7 / R 2 / A 0
- `ARG-136-007` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Paralelo19 (2026/10/17) · Regionales: Paralelo19, La Jornada de Oriente, Estrella Digital, Urbano Tlaxcala, Ambas Manos, Municipios Puebla, Tribuna Noticias · Recuento I 0 / N 0 / R 7 / A 0
- `ARG-136-REC-001` — Institucional: SIN BOLETÍN · Nacional: Milenio · Con fecha en la ruta: AM (2026/10/17) · Regionales: AM, Quinta Fuerza, Guanajuato Informa, Telediario · Recuento I 0 / N 1 / R 4 / A 0
- `ARG-136-REC-002` — Institucional: SIN BOLETÍN · Con fecha en la ruta: Paralelo19 (2026/10/17) · Regionales: Paralelo19, La Jornada de Oriente, Estrella Digital, Vanguardia, Urbano Tlaxcala, Meganoticias, El Congresista · Recuento I 0 / N 0 / R 7 / A 0
- `ARG-136-REC-003` — Institucional: SIN BOLETÍN · Nacional: N+, Milenio · Con fecha en la ruta: Potosinoticias (2026/10/16) · Regionales: Potosinoticias, Pulso, Código San Luis, San Luis Hoy, Global Media, La Opinión, Consulta Monterrey · Recuento I 0 / N 2 / R 7 / A 0
