# ARGOS 142 — Archivo de fuentes

**Corte**: 2026-10-27 · **Ventana**: 26-oct 08:37 → 27-oct 08:45 CDMX (**24 h 08 min**; `WINDOW_DAYS = 2`) · **Densidad**: 11 hechos propios / 24,13 h = **0,46 hechos/hora**, cálculo propio (5 🔴, 3 🟡, 3 🟢; 6 entidades). Sin recuperaciones.
**Hora de cierre**: hora real del Bloque 0 (08:45 CDMX del martes 27), declarada al destinatario. «Procede» a las 09:06 (21 min después): sin ajuste de cierre. La ola corrió de 09:10 a 09:16 aprox.; marca «Consulta 2026-10-27, última búsqueda 09:16» (se actualiza tras `procedencia-cifras`).

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-27-equipos.md`. Plantilla: `tools/plantilla-equipos-142.md`. Generador: `tools/datos-argos-142.py`.

## 1. La base

- 27-oct 08:45: clon en la rama de sesión `claude/argos-criminal-intelligence-otiawj`, en `60f2777` («Orden de ARGOS 126», por detrás); *fast-forward* a `origin/main`, `origin/claude/argos-139-qe9f01`, `origin/claude/argos-140` y `origin/claude/argos-141-nacional-kh5fj6` → `acb5426`. 233 archivos en `reports/`; última edición `argos-2026-10-26`.
- Rama de trabajo y de *push*: `claude/argos-criminal-intelligence-otiawj` (la sesión está fijada a esa rama).

## 2. Red y modo de búsqueda

- `curl https://www.gob.mx/fgr` → `000` (27-oct 08:45; `connect_rejected`). **Egreso bloqueado: solo WebSearch.** Techo ★★★★☆; esta edición no supera ★★★☆☆.
- Consulta de control en los dos modos: `extended` trae hechos de la ventana (Tehuacán con horas 9:30-9:58, Apatzingán, León, Cosoleacaque); `standard`, nada de la ventana (Tehuitzingo, Juárez NL de junio, Irapuato). **Todo `extended`.**
- Presupuesto: control 2 · coordinador 18 · ola 150 (6 × 25, agotada en los seis) · `procedencia-cifras` R1 y R2 (ver §11). Tope 200.

## 3. Rotación — prioridad sobre el ciclo y CICLO C, declarados

- **Ciclo C** (Occidente + Sureste encabezan el triaje judicial), después de la prioridad sobre el ciclo.
- **Sentencias `NO REVISADA` en 141 (9)**: revisadas ahora BCS (`pgjebcs.gob.mx`), Chih, Dgo, Pue, Qro, Chis (`fge.chiapas.gob.mx`), Yuc (7); siguen `NO REVISADA` Tlax y Hgo (PGJEH sin dominio confirmado). **Dominios sin páginas en 141 (6)**: resueltos Col (`fgecolima.mx`) y Mich (`comunicacion.fiscaliamichoacan.gob.mx`); siguen Son, Coah, Camp; Nay: `fgenay.gob.mx` apareció en un resultado, sin consulta `site:` (no confirmado).
- **Armamento `NO REVISADA` en 141 (19)**: revisadas ahora NL, Col, Edomex, Ver (`veracruz.gob.mx/seguridad`), Gro, Yuc, QRoo (7) —más Mich, Tamps, SLP, Tab, ya revisadas en 141—; Oax con dominio sin páginas (`ssp.oaxaca.gob.mx`); siguen 11.
- **Alto impacto solo amplia en 141 (9)**: 8 con consulta propia (Chih, Dgo, Coah, SLP, Ags, Edomex, Hgo, Qro); Tlax sigue solo amplia.
- **Qué aportó la rotación**: Occidente y Sureste (judicial) confirmaron tres dominios de fiscalía (Colima, Michoacán, Chiapas), hallaron la única sentencia candidata del corte (FGR, Tepic) y fecharon fuera de ventana cuatro sentencias que, sin fecha, habrían pasado por candidatas (Colima 22-oct, Quintana Roo 18-oct, Jalisco 19-oct, Yucatán 1-oct). Ninguna integrable.

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **26-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en día suelto, por rango («25 y 26», «26 y 27») y por título sin `site:`, al arrancar la ola (09:10) y en la repetición final (09:16) |
| **23, 24 y 25-oct** | Agregado (ventana de 141), ahora también en Milenio https://www.milenio.com/policia/acciones-relevantes-gabinete-de-seguridad-23-24-25-de-octubre-2026: republicación, misma fuente |
| **Año trampa** | «24, 25 y 26 de octubre» devuelve el agregado de **2025** (gob.mx/sspc; El Heraldo 2025/10/27) |
| **gabinetedeseguridad.gob.mx** | Solo el agregado del 9 al 11-oct |

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Ciclo** | C, declarado (§3) |
| **1. Tehuacán** | Hecho propio: **ARG-142-003** 🔴 + **ARG-142-010** 🟢. Horas ~9:20 (diligencia), ~9:58 (Curul), «antes de las 11:00» (Ambas Manos): todas posteriores a 08:37, solo por resumen; ninguna anterior → no hay `-REC-` ni fe de erratas. Detenidos: 2 por *slug* de N+ (mujer y hombre) frente a 1 por titular de Puebla Online (versión preliminar municipal): se integra 2 con la contradicción declarada. Herido: «otro agente» (Ambas Manos, titular) / «otro hombre» (Curul, titular) / «otra persona» (resumen): calidad no fijada. Arma: 1 AR-15 por *slug* (MTP) |
| **2. FE-001 de 141** | Magdalena Contreras: hora no fijada; «El Perusi» no consta; heridos 1 / «tres» por resumen · Acultzingo: noche del 24, solo por resumen (rutas del 25) · Ostuacán: sin ancla horaria; linchamiento del 24-25 con un detenido muerto (ya en la ficha) · SLRC: 3 personas, solo por resumen · **Zavala**: Línea Directa 2026-10-23 titula «durante enfrentamiento»; la SSP, por resumen: «detectaron a hombres armados que, al ver su presencia, dispararon» → **no se acredita que la autoridad iniciara**: sigue 🔴 y en la FE. Agresión y campamento: un solo aseguramiento (5 largas, 30 cargadores, 1,150 cartuchos, 5 detenidos, por resumen). **FE-001 de 141 sigue condicionada** |
| **3. Tuxpan** | **Sábado 24 por la noche** (La Silla Rota, La Razón, Latinus 2026/10/25; «sábado» solo por resumen): **visto de 140**, no omisión de 141 |
| **4. Tulantepec** | Fallo del 9-oct; individualización iniciada el 21-oct, reprogramada al **28-oct 17:00** (por resumen, La Jornada Hidalgo); sin pena ni boletín de la PGJEH |
| **5. Boletín federal** | §4 |
| **6. No investigados en 141** | Valle de Chalco: **21-sep** (El Heraldo Edomex y El Mañana 2026/9/21): descartado · Culiacán Prepa UAS: **un solo cuerpo** = ARG-141-004 · Cancún Las Palmas: **otro hecho** (dos casas, cartulina); madrugada del 26 por resumen, sin ruta con día; 🟡 previo a la apertura: visto · Cosoleacaque checador = ARG-141-003 (Notiver: «desde una camioneta», por resumen) · Cutzato: **hallazgo nuevo**, distinto de ARG-125-036 → **ARG-142-005** |
| **7. Fichas de 141** | Pénjamo: muerte sin confirmación de autoridad; la confirmada (Ariel «N», calle Independencia, zona centro; Correo 2026/oct/26) es otro hecho, día no fijado · Zamora: no consultado · Culiacán: sin denuncia previa publicada · Erongarícuaro: 2 largas, 29 cargadores, 541 cartuchos solo por resumen (ocho republicaciones = una fuente) · Los Tlacos: detención del 23-oct por resumen; vínculo con ARG-110-REC-001 no publicado |
| **8. Seguimiento** | Exfiscal: Jáuregui, impugnación anunciada (Proceso, Infobae 2026/10/25); distinto de Zuany (amparo, caso El Pinal; Yucatán 2026/10/26) · Xalapa: imputación y prisión preventiva oficiosa del 24-oct, proceso 879/2026, por resumen; vinculación pendiente · Juchitán: vinculación no publicada · León ARG-140-005: 4 por titulares de AM (21 y 23-oct, con el fiscal), 5 solo por resumen |
| **9. Sentencias candidatas** | Ramos Arizpe (ejido Paredón): 7 a 6 m y 75 UMA, sin ruta fechada → homónimo / pendiente · Pánuco: 21-oct (listado FGR; Hora Cero 2026/10/22): fuera de ventana · Guadalajara: no localizada · Culiacán: SRIV · Caborca: 19-oct, fuera |
| **Heredados** | Ecatepec ARG-140-REC-003: «noche del martes» (= 20-oct) por resumen, sin fragmento; FE-001 de 140 sigue condicionada · Linares: edad 47 (MVS, por resumen) / 55 · Río Bravo: sin evidencia nueva · Cachanillas: 15 y 17-oct, fuera · Huimanguillo: víctimas identificadas por medios (seguimiento de ARG-140-006) · Nogales, Ajuchitlán, Taxco, Apatzingán (heredado), El Tívoli, Coquimatlán, Tepic (heredado), Patamban, Tecuala: no revisados o sin avance |

## 6. Arbitrajes del coordinador

- **Hechos propios (11)**: Tecate FESC (`-001`, 🔴, el grupo inició contra un patrullaje, por resumen; «tarde» por titulares) y su detención (`-009`, 🟢, 3 por titulares, sin armas con cifra) · Tecate El Escorial (`-002`, 🔴, 4 muertos por titular; composición contradicha) · Tehuacán (`-003` 🔴 / `-010` 🟢) · Acámbaro (`-004`, 🔴, 2 muertos y 1 herido por *slug*) · Cutzato (`-005`, 🔴 fosa, día del hallazgo no fijado, publicado el 26) · León Valle de San Bernardo (`-006`, 🟡) · Apatzingán mercado (`-007`, 🟡, hora contradicha: si fue ~03:30 es de la ventana de 141 y 🟡 no recuperable) · SLP Periférico (`-008`, 🟡, fuente única) · Cajeme (`-011`, 🟢, publicado el 26, día no fijado).
- **Marca de apertura**: 8 de 11 (todas las de hora solo por resumen publicadas el 26). `-001` y `-009` quedan sin marca: «tarde del lunes» por titulares. `-010` sigue al ataque de `-003`.
- **Recuperaciones**: ninguna. El único 🔴 candidato de la ventana de 141 (Chihuahua, «levantón» de una empleada de Oxxo a medianoche del 25 al 26, El Diario de Chihuahua 2026/oct/26) es una desaparición única tras disparos sin muertos: **🟡**, no recuperable; visto.
- **Omisión de 141, solo registro (🟡, no recuperable)**: Alpatláhuac (Ver), adolescente de 16 años asesinado el domingo 25 ~15:30, por resumen (La Silla Rota 2026/10/26). Efecto sobre 141 (cálculo propio): amarillos 5 → 6, muertos 4 → 5. No se emite fe de erratas: no es alto impacto y el día es solo por resumen.
- **Vistos, con motivo**: Yautepec, dirigente de taxis herido (día y hora 08:15/10:45 solo por resumen, rutas sin fecha; 🟡) · Tepetzingo, dos hermanas heridas (~02:00, día no fijado; 🟡) · Yecapixtla (00:50 del 26: ventana de 141; 🟡; ya visto en 141) · San Quintín, hombre herido (titular con día en un medio abierto: fuente única no oficial; 🟡) · Mexicali, detención de «Isra» (día solo por resumen; 🟢) · Queréndaro, 2 muertos y 1 herido en un taller, y Morelia–Tumbisca, 2 muertos (Quadratín, rutas sin fecha; día solo por resumen: **rojos sin ancla; se encargan a `procedencia-cifras` R1**) · Morelia, motociclista muerto con escopeta (día no fijado) · Tlaquepaque, hombre muerto y mujer herida (Milenio, sin fecha) · Escobedo NL, Portal del Fraile (sin fecha) · SLP, detención de «la Wiwa» (sin fecha) · Piedras Negras, vinculación de Paula «N» (sin fecha; anterior) · Uruapan taquería (sábado 24: ventana de 140) · León col. Chapalita (sábado 24) · Zapopan (domingo 25; 🟡) · Miahuatlán y Ocotlán (Oax; día solo por resumen) · Chilpancingo, hombre «embolsado» (sin fragmento) · Cañada Morelos, 2 muertos (sin fecha) · Pénjamo, Ariel «N» (zona centro; día del ataque no fijado) · Mazatlán, granadas (agregado 23-25) · Sonora «objetivo neutralizado» = Arizpe/Cucurpe, sábado 24 (visto de 140).
- **Descartados**: CDMX col. Guerrero (8-jun) · Valle de Chalco (21-sep) · Cuichapa (22-oct) · Juchitán estudiante, San Blas Atempa, Pinotepa (fuera) · General Treviño (septiembre) · Tlaquiltenango (sin fecha).

## 7. Fe de erratas (no va al cartelón)

- **Ninguna nueva.** `ARG-141-FE-001` (a ARGOS 140) sigue condicionada; `ARG-140-FE-001` (a ARGOS 139) sigue condicionada (Ecatepec: «noche del martes», por resumen: el 20-oct que ya figura en el índice; ningún fragmento); Río Bravo (129) condicionada.
- Registro (sin FE): omisión 🟡 de 141 en Alpatláhuac (§6).

## 8. Registro del barrido — por entidad

Ver el «Indicador de cobertura» del cartelón y los informes íntegros. Sentencias: 19 revisadas, 4 dominios sin páginas, 9 `NO REVISADA`. Armamento: 11 por dominio, 1 sin páginas, 20 `NO REVISADA`. Alto impacto: 22 con consulta propia, 10 solo amplia. **Dominios nuevos confirmados**: `fge.chiapas.gob.mx`, `fgecolima.mx`, `comunicacion.fiscaliamichoacan.gob.mx`, `pgjebcs.gob.mx`, `www.veracruz.gob.mx/seguridad/` (SSP Veracruz; `ssp.veracruz.gob.mx` no existe como host indexado), `ssp.yucatan.gob.mx`, `ssc.qroo.gob.mx`. **Sin páginas**: `fgjes.sonora.gob.mx`, `fiscalia.coahuila.gob.mx`, `fge.coahuila.gob.mx`, `fiscalia.col.gob.mx`, `fiscaliageneralnayarit.gob.mx`, `fiscalia.michoacan.gob.mx`, `fgecampeche.gob.mx`, `fiscalia.campeche.gob.mx`, `ssp.oaxaca.gob.mx`. **Por probar**: `fgenay.gob.mx` (Nay), `fiscalia.sonora.gob.mx`, `fiscaliageneral.coahuila.gob.mx`.

## 9. Emisores por ficha

El recuento I/N/R/A de cada ficha está en `tools/datos-argos-142.py`; las URL, en el archivo de equipos.

## 10. Desglose de cálculos propios

- Muertos por agresión: 11 = 1 (-001) + 4 (-002) + 1 (-003) + 2 (-004) + 1 (-006) + 1 (-007) + 1 (-008). Heridos: 4 = 1 (-001) + 1 (-003) + 1 (-004) + 1 (-006). Cuerpos hallados: 1 (-005, restos de un hombre).
- Armamento: 2 eventos contabilizados — ARM-001 (1 larga, 2 detenidos) y ARM-002 (22 cartuchos, 2 detenidos); total 1 larga, 22 cartuchos, 4 detenidos; demás categorías `n/d`. Cualitativos: -009 (Tecate, armas no publicadas) y -002 (fusiles de asalto por titular).
- Entidades: 6 (BC, Pue, Gto, Mich, SLP, Son); con rojo, 4 (BC, Pue, Gto, Mich). Densidad: 11 / 24,13 = 0,46. Marcas: 8 APERTURA, 0 FRONTERA.
- Valoración 2: Tecate, 1 + 4 = 5 muertos.
- Conclusiones: Apatzingán, cinco hechos del 13 al 26-oct (14 días contando ambos extremos; fechas del índice) · flagrancia, 3 + 2 = 5 detenidos · SLP, 20 y 26-oct (7 días) · León, 21 y 26-oct (seis días después) · brecha, 3 + 2 + 2 = 7 detenidos.

## 11. Los dos controles editoriales

(Se completa al cierre.)

## 12. Herramientas

`python3 tools/datos-argos-142.py reports/argos-2026-10-26.html reports/argos-2026-10-27.html` · `python3 tools/gen-movil.py 142 2026-10-27 141 2026-10-26 08:45` · `python3 tools/gen-texto.py reports/argos-2026-10-27.html reports/argos-2026-10-27.txt` · `node tools/validar.js reports/argos-2026-10-27.html 2026-10-26 2026-10-27` → validación OK.

## 13. Lecciones de método (no van al cartelón)

1. **«Procede» a tiempo**: 21 min entre el Bloque 0 y el «Procede»; la ola terminó ~30 min después del cierre. Ningún hecho se perdió por hora.
2. **El recall del coordinador trajo los cuatro rojos de la región Noroeste y Occidente** (Tecate ×2, Acámbaro) antes de la ola; los equipos los fijaron por ruta.
3. **Dominios de fiscalía que no son los supuestos**: Michoacán (`comunicacion.fiscaliamichoacan.gob.mx`), Colima (`fgecolima.mx`), Veracruz SSP (`veracruz.gob.mx/seguridad`). Actualizar la plantilla de 143.
4. **Republicaciones de un comunicado** (Tehuacán: catorce portales) no son fuentes independientes: recuento R alto, corroboración real baja.
