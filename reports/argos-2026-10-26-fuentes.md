# ARGOS 141 — Archivo de fuentes

**Corte**: 2026-10-26 · **Ventana**: 25-oct 07:45 → 26-oct 08:37 CDMX (**24 h 52 min**; `WINDOW_DAYS = 2`) · **Densidad**: 7 hechos propios / 24,87 h = **0,28 hechos/hora**, cálculo propio (0 🔴, 5 🟡, 2 🟢; 6 entidades). Borrador previo a la ronda 1: 9 hechos (0,36).
**Hora de cierre**: hora real del Bloque 0 (08:37 CDMX del lunes 26), declarada al destinatario y aceptada con «Procede». La orden «Procede» llegó después: las búsquedas del coordinador y de la ola corrieron por la tarde, y `procedencia-cifras` R1 terminó a las **17:02 CDMX** (hora del archivo de su informe): marca «Consulta 2026-10-26, última búsqueda 17:02». Los hechos posteriores a las 08:37 pertenecen a ARGOS 142.

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-26-equipos.md`. Plantilla: `tools/plantilla-equipos-141.md`. Generador: `tools/datos-argos-141.py`.

## 1. La base

- 26-oct 08:37: clon en la rama de sesión `claude/argos-141-nacional-kh5fj6`, en `60f2777` (por detrás); *fast-forward* a `origin/main` (`d0c6ab7`), `origin/claude/argos-139-qe9f01` (`9712e79`) y `origin/claude/argos-140` (`9b4c915`). 226 archivos en `reports/`; última edición `argos-2026-10-25`.
- Rama de trabajo y de *push*: `claude/argos-141-nacional-kh5fj6` (la orden pedía `claude/argos-141`; la sesión está fijada a la rama con sufijo y así se declaró al destinatario).

## 2. Red y modo de búsqueda

- `curl https://www.gob.mx/fgr` → `000` (26-oct 08:37; `connect_rejected`). **Egreso bloqueado: solo WebSearch.** Techo ★★★★☆; esta edición no supera ★★★☆☆.
- Consulta de control en los dos modos: `extended` trae hechos de la ventana (Tuxpan, Magdalena Contreras, Pénjamo, Zamora); `standard`, nada de la ventana (Tehuitzingo: mayo de 2026). **Todo `extended`.**
- Presupuesto: control 2 · coordinador 16 · ola 150 (6 × 25, agotada en los seis) · `procedencia-cifras` R1 28 · R2 ≤ 2. Tope 200.

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

- **Ciclo B** (Noreste + Golfo encabezan el triaje judicial), después de la prioridad sobre el ciclo.
- **Sentencias `NO REVISADA` en 140 (16)**: revisadas ahora NL, SLP, Jal, Ags, Gto, Edomex, Mor, Tab, Oax, Gro, QRoo (11); consultadas sin páginas del dominio Son, Col, Nay, Mich (4); sigue `NO REVISADA` BCS (1). **Dominios sin páginas en 140 (5)**: resueltos Sin (`fiscaliasinaloa.mx`), Tamps (`fgjtam.gob.mx`), Zac (`fiscaliazacatecas.gob.mx`); siguen Coah y Camp.
- **Armamento `NO REVISADA` en 140 (17)**: revisadas ahora Chih, Dgo, Mor, Pue, Hgo, Qro (6); siguen 11 (BC, BCS, Son, Sin, Jal, Col, Nay, Edomex, Tlax, Camp, QRoo). **Sin páginas en 140 (3)**: Zac y Tab revisadas (`tabasco.gob.mx`); Gto sigue `NO REVISADA`.
- **Alto impacto solo amplia en 140 (16)**: 12 con consulta propia; Dgo, Tlax, Hgo, Qro siguen solo amplia.
- **Qué aportó la rotación**: Noreste y Golfo (judicial) resolvieron cuatro dominios de fiscalía (Tamaulipas, Zacatecas, Tabasco y, por Noroeste, Sinaloa) y descartaron por homonimia dos candidatas de la FGR (Saltillo/Ramos Arizpe y Veracruz/Pánuco). Ninguna sentencia integrable: el ciclo hace demostrable el `SIN DATO`.

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **23, 24 y 25-oct** | **Existe un agregado**: Ultranoticias, RED113, Talla Política, Ahora Noticias/Tabasco; Argonmexico 2026/10/26. Una fuente; corroboración débil por construcción. Día de cada acción **no fijado**: vistos, salvo Los Tlacos (ruta propia del 25: ARG-141-007) |
| **26-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en día suelto (coordinador y Golfo) y por título |
| **gabinetedeseguridad.gob.mx** | Solo el agregado del 9 al 11-oct |

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Ciclo** | B, declarado (§3) |
| **1. Ecatepec Tulpetlac (ARG-140-REC-003)** | **Sin fragmento** que fije el día: El Gráfico 2026/10/22 es la única ruta; resúmenes contradictorios («noche del martes» / «ayer por la madrugada»). Ninguna fuente sostiene la noche del miércoles 21 → **FE-001 de ARGOS 140 sigue condicionada** |
| **2. Boletín federal 23-26** | §4 |
| **3. Tulantepec** | Sin pena; audiencia el 28-oct 17:00 en el Tribunal de Enjuiciamiento de Tulancingo, solo por resumen; sin boletín de la PGJEH |
| **4. Sonora «abaten a presunto jefe»** | «El Meny», San Antonio, Arizpe, **sábado 24** (La Razón, La Jornada, El Heraldo, MVS 2026/10/24); 4 detenidos; «durante recorridos de seguridad recibieron disparos y repelieron» (resumen del comunicado) frente a operativo con apoyo aéreo (otra nota): **quién inició no determinado → 🟡**, no recuperable. Se aparta de REC-005 porque allí los titulares y *slugs* dicen «agresión», «repeler agresión» y «emboscan» |
| **4b. Coicoyán de las Flores** | **2025** (Diario de Yucatán 2025/09/01): descartado |
| **5. Fichas de 140** | Ver el bloque de seguimientos del panorama. Huimanguillo: sin identificación · León: 4 / 5 contradicho · Reynosa: sin intervención publicada · Purísima: sin detenidos · Mazatlán C4i: titular de Los Noticieristas (SSPE) · Juchitán, Iztapalapa: sin vinculación · Xalapa: prisión preventiva (Hora Cero) · Puebla/CDMX: desglose no publicado (33 armas en Puebla, solo por resumen) · Los Ranas: alias coincidente en dos medios · Chimalhuacán, Jiutepec, Ozumba: `NO REVISADOS` · Álamo/Papantla: reparto por titular de La Nigua · Cosoleacaque `-018`: el titular de Milenio «2 muertos y mujer herida» es probablemente de febrero (La Silla Rota 2026/2/24): **no se atribuye** · Cocotitlán: «emboscan» por titular |
| **6. Exfiscal** | Impugnación anunciada solo por resumen; sin amparo |
| **7. Sentencias candidatas** | Saltillo: posible homónimo (7 años 6 meses, Ramos Arizpe) · Veracruz: DPE/4787/2026, posible Pánuco, 4 años 8 meses · Guadalajara: no localizado · Ensenada: sentencia del 16-oct · General Cepeda: titular del 19-oct · Culiacán, Caborca: sin avance |
| **Heredados** | Nogales, Cachanillas, Apatzingán, El Tívoli, Coquimatlán, Linares (edad contradicha), Tepic, Patamban, Taxco (sin vinculación), Ajuchitlán (séptimo campesino sin localizar), Tecuala, Río Bravo: sin avance que cambie un color |

## 6. Arbitrajes del coordinador

- **Tras la ronda 1** (`procedencia-cifras`): **Tehuacán** (agente ministerial asesinado y detención) sale de ARGOS 141: cinco resúmenes convergen en el lunes 26 entre las 9:00 y las 10:00, posterior al cierre de las 08:37 (rutas Retodiario, Síntesis, Diario Puntual 2026/10/26). Mismo criterio que `ARG-140-REC-003` (convergencia de resúmenes para asignar ventana). **Pasa a ARGOS 142** como hecho propio 🔴. **Tuxpan** (dirigente sindical del transporte) sale: la mayoría de los resúmenes lo sitúa la noche del **sábado 24** → ventana de 140, 🟡, no recuperable: visto.
- **Los Tlacos** entra como `ARG-141-007` (🟢, ruta propia del 25, marca de apertura), por simetría con Erongarícuaro (`editor-duplicidad` R1).
- **Renumeración del borrador a la edición**: -003→-001 (Pénjamo), -004→-002 (Zamora), -006→-003 (Cosoleacaque), -007→-004 (Culiacán), -008→-005 (Cancún), -009→-006 (Erongarícuaro), nuevo -007 (Los Tlacos); retirados -001, -002 (Tehuacán) y -005 (Tuxpan). `ARM-001` remite a -006.
- **Recuperaciones (ventana de 140; solo 🔴)**: Magdalena Contreras (madrugada del 25 en todos los resúmenes; tres rutas del 25), Acultzingo (noche del 24 o madrugada del 25), Ostuacán (doble feminicidio, 21-23-oct), San Luis Río Colorado (tres fosas, 24-oct), Zavala/Concordia (noche del 23 según la SSP, por resumen; «agresión», «repeler agresión», «emboscan» por titular y *slug*; probable mismo operativo que el campamento del boletín federal: si se acredita que la autoridad inició, baja a 🟡).
- **Por qué Zavala es 🔴 y Arizpe 🟡** (`editor-duplicidad` R2, H5): en Zavala **tres medios distintos** titulan o *sluguean* la iniciativa del grupo («tras agresión», Los Noticieristas; «tras repeler agresión», Sinaloahoy; «emboscan a militares», TV Azteca) y la SSP de Sinaloa, por resumen, dice que los civiles dispararon al ver a los uniformados; quién inició **queda determinado por titular**. En Arizpe los titulares hablan de «abatir» y «neutralizar a un objetivo prioritario», con apoyo aéreo: operativo dirigido; el «recibieron disparos» solo consta por resumen: **no determinado → 🟡**. Si se acredita que el campamento y la agresión son el mismo operativo y que la autoridad llegó a ejecutar una acción (cateo, inhabilitación), Zavala baja a 🟡 y FE-001 queda en 12 rojos.
- **Vistos, con motivo**: Colima col. Fátima, Tecomán Cerro de Ortega, Tlaquepaque Las Huertas, Yecapixtla (sin ruta con día; 🟡) · Álvaro Obregón Corpus Christi, Yautepec, Tehuitzingo, Tijuana (madrugada del 25 o antes: ventana de 140, 🟡/🟢) · Abraham Núñez (Culiacán, sábado 24) · Culiacán col. Jesús Valdez (cuerpo sin causa publicada) · Cutzato (posible duplicidad con `ARG-125-036`) · Cancún, tres detenidos relacionados con cinco hechos (sin fecha) · Campeche, Ciudad Concordia (resumen) · Acapulco «El Moro» (24-oct, 🟡) · Matamoros 23-oct · «Mando 20» (23-oct, 🟢) · Hopelchén (23-oct) · Valle de Chalco (N+, fecha no fijada; **no investigado**: pendiente).

## 7. Fe de erratas (no va al cartelón)

- **`ARG-141-FE-001` — ARGOS 140**: las recuperaciones `ARG-141-REC-001` a `-005` son rojos de su ventana que 140 no publicó. Efecto sobre ARGOS 140 (cálculo propio): **rojos de 8 a 13; muertos por agresión de 15 a 21** (+2 Magdalena Contreras, +2 Acultzingo, +2 Ostuacán); **heridos de 8 a 9** (+1 Magdalena Contreras, mínimo); los 2 muertos de Ostuacán se cuentan como **muertos por agresión** (feminicidio con presuntos responsables detenidos), no como cuerpos hallados; San Luis Río Colorado (restos sin número) y Zavala (agresores heridos, solo por resumen) no mueven cifras. **Condicionada**: el día o la hora de todas las recuperaciones son solo por resumen; Zavala, además, por el posible inicio estatal.
- **`ARG-140-FE-001` (a ARGOS 139)**: sigue condicionada (Ecatepec sin fragmento).
- **Cosoleacaque (`ARG-140-018`)**: «2 muertos y mujer herida» (Milenio, sin fecha) no se atribuye: probable caso de febrero de 2026 (La Silla Rota 2026/2/24; Golpe Político 2026/02/25).
- Condicionada, sin cambio: Río Bravo (129).

## 8. Registro del barrido — por entidad

Ver el «Indicador de cobertura» del cartelón y los informes íntegros. Sentencias: 17 revisadas, 6 dominios sin páginas, 9 `NO REVISADA`. Armamento: 13 por dominio, 19 `NO REVISADA`. Alto impacto: 23 con consulta propia, 9 solo amplia. Dominios nuevos confirmados: `fgjtam.gob.mx`, `fiscaliazacatecas.gob.mx`, `fiscaliasinaloa.mx`, `fiscaliatabasco.gob.mx`, `portal.fgeguanajuato.gob.mx`, `fiscalia-aguascalientes.gob.mx`, `fgeqroo.gob.mx`, `fiscalianl.gob.mx`, `fiscaliaslp.gob.mx`, `fiscaliamorelos.gob.mx`, `fgjem.edomex.gob.mx`. **Sin páginas**: `fgjes.sonora.gob.mx`, `fiscalia.coahuila.gob.mx`, `fiscalia.col.gob.mx`, `fiscaliageneralnayarit.gob.mx`, `fiscalia.michoacan.gob.mx`, `fgecampeche.gob.mx`, `ssp.tabasco.gob.mx`.

## 9. Emisores por ficha

El recuento I/N/R/A de cada ficha está en `tools/datos-argos-141.py`; las URL, en el archivo de equipos y en el informe de `procedencia-cifras` R1.

## 10. Desglose de cálculos propios

- Muertos por agresión en hechos propios: 4 = 1 (-001, no confirmado por autoridad) + 1 (-002) + 1 (-003) + 1 (-004). Heridos: 3 = 2 (-001) + 1 (-002). Cuerpos hallados: 0.
- Recuperaciones: 6 muertos (2 + 2 + 2) y 1 herido (REC-001), fuera de todo total.
- Armamento: 1 evento contabilizado (ARM-001: 3 detenidos; demás categorías `n/d`) y 1 cualitativo (-007).
- Entidades: 6 (Gto, Mich, Ver, Sin, QRoo, Gro). Densidad: 7 / 24,87 = 0,28. Marcas: 4 FRONTERA, 3 APERTURA.
- Conclusiones: Pénjamo, cuatro hechos del 14 al 25-oct (12 días contando ambos extremos) · transporte, tres del 19 al 25-oct (7 días: ARG-137-014, ARG-140-012, ARG-141-003) · instituciones, cuatro del 24 al 26-oct (3 días) · Zamora–Jacona, tres en octubre (2, 11 y 25-oct, fechas del índice).

## 11. Los dos controles editoriales

**Ronda 1** (en paralelo): `editor-duplicidad` — CORREGIR (20 hallazgos; sin duplicidades reales; aritmética OK) · `procedencia-cifras` — CORREGIR (20 pases; 28 de 30 búsquedas). Aplicados: Tehuacán a ARGOS 142; Tuxpan a vistos; Los Tlacos como ficha; Milenio fuera de Pénjamo; La Opinión en lugar de N+ en Cosoleacaque, con posible segundo lesionado; unicidad inferida del cuerpo de la Prepa UAS; Cancún con calidad contradicha y posible duplicado de Las Palmas; REC-001 «al menos 1 herido»; REC-003 con la ruta del 26; REC-004 personas no determinadas; REC-005 con titulares y *slugs* de agresión, probable mismo operativo y heridos fuera; Concordia en ARGOS 137, no 139; seguimientos rehechos (exfiscal, Xalapa por Hora Cero, C4i por titular de la SSPE; Milenio de Cosoleacaque retirado); vistos de armamento con las 11 entidades del agregado, Arizpe y Tehuacán; eventos cualitativos declarados; portada y Valoración sin rojo propio; Conclusiones rehechas con patrones del índice (Pénjamo con el cuarto hecho, transporte con ARG-137-014 y ARG-139-009, instituciones, Zamora–Jacona, Los Tlacos) y sin ARG-ID de la portada.
**No aplicado, con motivo**: «Jalisco, consulta propia parcial» se mantiene como propia (Tlaquepaque); recuento de N+ en Tuxpan: la ficha salió.

**Ronda 2** (en serie): `editor-duplicidad` R2 — CORREGIR (9 hallazgos; 0 duplicidades; aritmética, ARG-ID y renumeración limpios). Aplicados: Conclusión 2 a **tres** trabajadores (ARG-139-009 es «conductor» sin ocupación publicada: fuera); Valoración 4 sin el hecho de 142 (ahora: recuperaciones); Valoración 1 sin remisión; Valoración 2 y Conclusión 3 con la calidad contradicha y la fiscalía de Guanajuato; deslinde de Concordia con los ARG-ID del índice; razón de Zavala 🔴 frente a Arizpe 🟡 (§6); nota de eventos cualitativos armonizada; «1 herido»; antecedentes de Los Tlacos (ARGOS 96 y 117); recuperaciones del panorama ordenadas por fecha; índice y pendientes al cierre. **Decisiones escritas**: (a) las tarjetas de armamento y sentencias en `n/d` y cero se mantienen por la regla de iconografía («la ausencia es dato»); (b) la marca «Consulta» es la hora real de la última búsqueda (17:02) y el pie lleva la hora del corte (08:37): son campos distintos, como manda CLAUDE.md.
`procedencia-cifras` R2 (0 de 2 búsquedas) — CORREGIR (9 hallazgos; aritmética y totales sin descuadre; ninguna cifra de Tehuacán ni de Tuxpan en totales). Aplicados todos: §10 a tres trabajadores; recuentos de emisores sin réplicas (Zamora R 2; Los Tlacos R 1); marca de heredado en la Conclusión 5 y nota de ARG-ID no reverificados; Conclusión 1 con el día de Marfil por resumen y dos reservas; hora de Tehuacán «solo por resumen» en los vistos; Ostuacán con el periodo 19-23-oct y criterio de conteo en FE-001; «sin lesionados» de Cancún por resumen y «coyote de tránsito» por *slug*; municipios de Los Tlacos por resumen; REC-001 «al menos 1 herido»; institucional 0 en REC-001 y REC-005 (autoridad solo por resumen). **Presupuesto final**: 2 + 16 + 150 + 28 + 0 = **196 de 200**. **Edición sellada.**

## 12. Herramientas

`python3 tools/datos-argos-141.py reports/argos-2026-10-25.html reports/argos-2026-10-26.html` · `python3 tools/gen-movil.py 141 2026-10-26 140 2026-10-25 08:37` · `python3 tools/gen-texto.py reports/argos-2026-10-26.html reports/argos-2026-10-26.txt` · `node tools/validar.js reports/argos-2026-10-26.html 2026-10-25 2026-10-26` → validación OK.

## 13. Lecciones de método (no van al cartelón)

1. **Ocho horas entre el cierre declarado y la ola**: el «Procede» llegó ~8 h después del Bloque 0. La ventana se cerró a la hora del Bloque 0, como se declaró; el coste fue que la prensa del lunes por la mañana (Tehuacán) ya estaba indexada y hubo que retirarla por hora. Conviene que la ventana cierre a la hora del «Procede» cuando la diferencia supere unas horas, o declararlo así en la orden.
2. **El recall antes de la ola funcionó**: las cinco recuperaciones y los dos amarillos con más fuentes (Tuxpan, Magdalena Contreras) salieron del recall y los equipos los verificaron con presupuesto.
3. **El agregado federal de fin de semana no fija días**: solo las acciones con nota propia fechada pueden entrar; el resto queda visto.
4. **Las conclusiones deben contar contra el índice y contra los deslindes de la propia edición** (Pénjamo, cuarto hecho).
