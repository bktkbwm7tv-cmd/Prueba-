# ARGOS 138 — Archivo de fuentes

**Corte**: 2026-10-20 · **Ventana**: 19-oct 11:05 → 20-oct 07:06 CDMX (**20 h 01 min**; `WINDOW_DAYS = 2`) · **Densidad**: 11 hechos propios / 20,02 h = **0,55 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 07:06 CDMX). Consultas hasta las **09:30 CDMX** (marca «Consulta» del cartelón); los hechos posteriores a las 07:06 pertenecen a ARGOS 139.

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-20-equipos.md`. Plantilla de los equipos: `tools/plantilla-equipos-138.md`.

## 1. La base

- Sesión continuada (la misma que produjo ARGOS 136); clon en `claude/argos-136` (`1de5574`). ARGOS 137 se produjo en otra sesión (rama `claude/argos-137`, `292a9a9`). Se abrió `claude/argos-138` y se fusionaron en *fast-forward* `main` y `claude/argos-129` … `-137`, sin conflicto.
- `reports/`: 203 archivos, última edición `argos-2026-10-19` (ARGOS 137), como estaba previsto.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (`connect_rejected` del proxy), 07:06. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**.
- **Consulta de control** («ataque armado muertos "19 de octubre" 2026 México»): `standard`, nada del 19; `extended`, Edomex (agregado de El Independiente), Mazatlán (agregado del 18), Juchitán (→ `ARG-138-001`), Copanatoyac y Colima (ya en 137). **Se mantuvo `extended`.**
- **Presupuesto**: control 2 + ola (Noroeste 26, Noreste 27, Occidente 27, Centro 28, Golfo y federal 28, Sureste 22 = **158**) + **8 del coordinador** = **168**; `procedencia-cifras` hasta **30** → hasta **198 de 200**.
- **Grep**: los equipos no tuvieron Bash; ejecutaron el cotejo con la herramienta Grep sobre los mismos archivos. Sustitución anotada; el coordinador repitió con Bash los topónimos nuevos.

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

| Renglón | Resultado |
|---|---|
| Ciclo | **B** — Noreste y Golfo encabezaron el triaje judicial tras la prioridad (tabla de `CLAUDE.md`, retomada en 137) |
| Prioridad — sentencias (9 `NO REVISADA` en 137) | **Revisadas (7)**: Son (`fiscalia.sonora.gob.mx`, una convocatoria), Zac (`fiscaliazacatecas.gob.mx`), Gto (`portal.fgeguanajuato.gob.mx`), Mor (**`fiscaliamorelos.gob.mx`**, variante que sí devuelve), Hgo (**`procuraduria.hidalgo.gob.mx`**, solo documentos legales), Gro (`fiscaliaguerrero.gob.mx`), Yuc (`fge.yucatan.gob.mx`). **Siguen `NO REVISADA`**: **Sin** (`fiscaliasinaloa.gob.mx`, undécima edición sin devolver) y **Camp** (el buscador ignora el `site:`) |
| Prioridad — armamento (18 `NO REVISADA` en 137) | **Por dominio propio (13 de las 18)**: BC, BCS, Son (portada), Dgo (**`seguridad.durango.gob.mx`**, portada), NL (`fuerzacivil.nl.gob.mx`, una página), CDMX, Edomex, Pue, Hgo (**`s-seguridad.hidalgo.gob.mx`**), Qro (**`sscqro.gob.mx`**), Chis; **por portal estatal (5)**: Col, Ags, Mor, Tlax (`comunicacion.tlaxcala.gob.mx`), Gro. **Siguen `NO REVISADA`**: Chih (el equipo encadenó dos dominios con `OR`: operador ignorado), Jal (`seguridad.jalisco.gob.mx` y `jalisco.gob.mx` no devuelven) |
| Prioridad — alto impacto (Camp, Yuc) | **Consulta propia en las dos**; sin hechos del 19-20 |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Noreste: cinco fiscalías devolvieron dominio (Zac, NL débil, Tamps hasta el 11-oct, SLP sin fecha, Coah hasta agosto); FGJE-370-2026 fijado el 6-oct (fuera). Golfo: Veracruz, Tabasco y FGR, SRIV |
| Regresión por rotación | Sentencias: BC, BCS, Chih, Jal, Nay, Ags, Mich, CDMX, Edomex, Pue, Tlax, Qro, Oax, Chis, QRoo pasan a `NO REVISADA`. Armamento: Sin, Coah, Tamps, Mich, Gto, Ver, Tab, Oax, Camp, Yuc, QRoo pasan a `NO REVISADA`. **Prioridad sobre el ciclo en 139** |

**Dominios confirmados en 138**: `fiscaliamorelos.gob.mx` · `procuraduria.hidalgo.gob.mx` (sin boletines) · `s-seguridad.hidalgo.gob.mx` · `sscqro.gob.mx` · `fiscaliageneralqro.gob.mx` (boletín del 19-oct sobre «El Tripa») · `seguridad.durango.gob.mx` · `comunicacion.tlaxcala.gob.mx` · `portal.fgeguanajuato.gob.mx` · `ssp.zacatecas.gob.mx`. **No devuelven**: `fiscaliasinaloa.gob.mx`, `sspguerrero.gob.mx`, `ssp.nl.gob.mx`, `ssp.morelos.gob.mx`, `ces.morelos.gob.mx`, `sspc.tlaxcala.gob.mx`, `ssp.hidalgo.gob.mx`, `seguridad.hidalgo.gob.mx`, `ssc.queretaro.gob.mx`, `seguridad.jalisco.gob.mx`, `fgecam.gob.mx`, `gabinetedeseguridad.gob.mx`.

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **16, 17 y 18-oct** | Agregado publicado el **19-oct** (Milenio, Ultranoticias, RED113, Talla Política, Certeza Diario; republicadores, no independientes). Ya registrado en ARGOS 137 como evento anterior. Desglose por resumen del equipo Golfo: Tecuala, **dos acciones** (10,775 cartuchos y 586 cartuchos; el «más de 11 mil» de NTV es la suma, cálculo del medio); Lerdo de Tejada; Mahahual; Mazatlán en tres bloques. **No se imprime** |
| **19-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |
| **20-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (solo el del 20-oct-**2025**, año equivocado) |

Defensa (último 14-oct), Marina (11-oct), GN (sin 2026), FGR (2019-2022): SRIV. `gabinetedeseguridad.gob.mx`: dominio no devuelto.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Cuajinicuilapa** (color) | **🔴 por decisión del destinatario (20-oct, 07:10)** → `ARG-138-REC-001`. Precedentes: `ARG-108-REC-001`, `ARG-124-002`. 136: +1 rojo, +1 muerto (§8) |
| **Copanatoyac, coordinador del PT y cuatro familiares** | **Es de marzo de 2025** (Infobae 2025/03/30, La Jornada 2025/03/30, La Silla Rota 2025/3/29): señuelo de año. **Cerrado** |
| **Zacatecas, policías en los límites con Aguascalientes** | **Luis Moya, 1-ago-2026** (Proceso, Publimetro, El Financiero, Diario de Yucatán 2026/08/01): fuera. **Cerrado** |
| **Colima, «muerte de funcionario»** | Telediario, sin fecha; por resumen, agosto y muerte por ahogamiento de un integrante de la Universidad de Colima: no es homicidio. **Cerrado** |
| **Juchitán, panteón** (137) | Sigue sin fijar entidad ni día; **Tomás Aquino (lunes 19) es otro hecho** → `ARG-138-001` |
| **Tabasco** (`ARG-137-005`) | Municipio sigue contradicho (Teapa / Jalapa); destinatario de las cartulinas: «un alto mando de la SSPC», solo por resumen; un nombre solo en fuente abierta (no se integra) |
| **Tulancingo** (`ARG-137-006`) | ~09:20-09:30 por resumen; línea de investigación de la PGJEH no publicada |
| **Coatzacoalcos** (`ARG-137-003`) | Sin versión del agresor ni detenido; huyó en motocicleta, por resumen |
| **Colima** (`ARG-137-007`) | Día 18 por resumen; rutas del 19 (La Jornada, Infobae) fijan la publicación; armamento no publicado; «abrieron fuego primero», solo por resumen |
| **Tijuana** (`ARG-137-011`, `-017`) | «Hay un detenido» en cinco medios, ninguno atribuido a una autoridad: sigue contradicho |
| **«El Talibán»** (`ARG-137-REC-002`) | Capturas del 16-oct (El Rosario, 4) y 17-oct (Mazatlán) según la Defensa, por resumen; primera publicación 18-oct por ruta (El Financiero, Tribuna, El Diario de Chihuahua); mineros: 23-ene, por resumen |
| **Exfiscal** (`ARG-136-006`) | FGR, orden federal por traición a la patria y traslado al Altiplano (Infobae 2026/10/19, La Razón 2026/10/20, La Jornada 2026/10/19); audiencia federal el martes 20 y vinculación estatal el jueves 22, por resumen; comunicado de la FGR no localizado |
| **Fichas de 137 con día solo por resumen** | `-009`: día 18 por ruta (Línea Directa 2026-10-18) · `-015`: «balean a 3 personas», Correo 2026/oct/18 · `-016`: Grupo Marmor y Red Michoacán 2026/10/18 · `-014`: Grupo Marmor 2026/10/19 · `-002` (Tlajomulco) y `-012` (Zapopan): sin ruta con día; `-012` puede ser anterior a la apertura de 137 (minutos después de una medianoche no fijada) · `-001` y `-013`: sin cambio |
| **Linares** | Día sin fragmento literal; el herido sigue vivo (titular de Punto x Punto 2026/10/16: «dos murieron, uno está hospitalizado») |
| **FGJE-370-2026** | 6-oct, por listado del dominio: fuera de ventana; ya en vistas de 137 |
| **Patamban** | MVS 2026/10/15: «líder indígena»; defensa del bosque, «no se descarta», solo por resumen: **sigue la decisión del destinatario** |
| **Heredados sin avance** | Nogales (7 osamentas, colectivo) · Cachanillas (10, colectivo) · Ajuchitlán · Tepic · Apatzingán `ARG-135-003` · El Tívoli · Coquimatlán · Tlalnepantla · Industrial Bravo · Ensenada (boletín) |
| **«El Tripa»** | Detenido el **16-oct** (Código QRO 2026/10/16); boletín de la Fiscalía de Querétaro **2026/10/19** (`fiscaliageneralqro.gob.mx/portal/2026/10/19/…`); delito contradicho (secuestro agravado / multihomicidio). **Cerrado: 16-oct, fuera** |

## 6. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Juchitán, Tomás Aquino** (`-001`) | Sureste + coordinador: lunes 19 ~21:00, **solo por resumen**, cuatro medios regionales y uno nacional coincidentes; **ninguna ruta con fecha**. **Excepción al criterio de 137** (que dejaría el hecho como visto): se ficha por ser un rojo con cuatro o más fuentes coincidentes en el día, con ★★☆☆☆ y la marca `NINGUNA RUTA CON FECHA`. Heridos 1 a 3, contradicho |
| **Cárdenas, fosa** (`-002`) | Ajeno del Noreste (Hoy Tamaulipas); coordinador: FGE Tabasco confirma, por titular de Tabasco Hoy; 19-oct por resumen; **misma excepción**, con marca de día de apertura. 🔴 por fosa clandestina |
| **Culiacán, Prados del Sol y 21 de Marzo** (`-003`, `-004`) | Noroeste y coordinador; rutas del 19; noche del lunes por resumen. 🟡 cada uno |
| **Mazatlán, San Joaquín y La Marina** (`-005`, `-006`) | Noroeste; rutas del 19; «este lunes» por titular en `-005`. 🟡 |
| **Navolato, La Palma** (`-007`) | Coordinador; Luz Noticias 2026-10-20; quién inició no publicado → 🟡 |
| **Monterrey, col. Hidalgo** (`-008`) | Noreste; «poco antes del mediodía» por resumen: **puede ser anterior a las 11:05** → marca de apertura. 🟡 |
| **Ciudad Juárez, Los Alcaldes** (`-009`, `-010`) | Ajeno de Golfo y Noreste; coordinador: El Bordo (ruta 20261019) y El Diario de Juárez (2026/oct/20). Un hecho y su detención: dos fichas. Mujer herida (estado no publicado) → 🟡; tres detenidos → 🟢 |
| **Cadereyta** (`-011`, `ARM-001`) | Noreste; «Fuerza Civil captura a líder criminal y 8 generadores de violencia» (ABC 2026/10/19). 3 cortas solo por resumen: fila fuera del total |
| **Jiquilpan** (`-REC-002`, `ARM-002`) | Occidente; tres rutas del 18 → ventana de 137, que no lo publicó. 🟢; 31 cartuchos solo por resumen: fila fuera del total |
| **Vistos, no fichados** | **Ecatepec**, mecánico y su hijo (fuente única, agregado, día no fijado; 🔴 si se fija en la ventana) · **Mazatlán, Villa Tutuli** (1 muerto y 1 herido) y **El Conchi** (menor herido): domingo 18, 🟡 de 137, no recuperables · **Coatzacoalcos, taxista** (lunes 19 ~06:00): 🟡 de 137, no recuperable · **Culiacán, Palmanova / Los Ángeles**: día solo por resumen · **Culiacán, policía municipal «saliendo de su turno»** y **albañil del Centro**: sin fecha (🔴 el primero si se fija) · **Río Bravo, diputada federal agredida con arma punzocortante** (sábado 17, ventana de 136): agresión sin muerte a una servidora pública — **color a decisión del destinatario** · **«El Marce»**, captura anunciada el 19 por la FGE QRoo, día solo por resumen (atentado del 2-oct es `ARG-126-REC-010`) · **Chihuahua, cuatro detenidos por una narcomanta** (El Diario de Chihuahua 2026/oct/19): no examinado · **SLP, Guardia Civil Estatal, 32 detenidos** (El Heraldo de SLP 2026/10/19): agregado, sin cifras de armas · **Hermosillo, hombre de 45 años** (viernes 16, sin ruta) · **Chietla, mujer frente a una primaria** (18-oct por resumen) · **Puebla, policía estatal de Tres Cerritos**: `ARG-134-005` · **Naucalpan**: `ARG-132-004` · **210 armas de NL**: 31-ago |

## 7. Fe de erratas (no va al cartelón)

- **`ARG-138-FE-001`** — **Cuajinicuilapa** (`-REC-001`, 🔴 por decisión del destinatario): **+1 rojo y +1 muerto a ARGOS 136** (3 → 4 rojos; muertos por agresión de 136 + 1). Cálculo propio. Jiquilpan (`-REC-002`, 🟢) no altera el semáforo de 137.
- **Actualizaciones de dato de 137, no fe de erratas**: `-009`, `-014`, `-015`, `-016` con ruta fechada; `-012` posiblemente anterior a su ventana (sin fijar).

## 8. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | propia | SRIV (`seguridadbc.gob.mx`) | NO REVISADA |
| Baja California Sur | regional | SRIV (`sspbcs.gob.mx`) | NO REVISADA |
| Sonora | propia | SRIV (`ssp.sonora.gob.mx`, portada) | SRIV (`fiscalia.sonora.gob.mx`, parcial) |
| Chihuahua | propia · **hechos** (`-009`, `-010`) | NO REVISADA | NO REVISADA |
| Sinaloa | propia · **hechos** (`-003` a `-007`) | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Durango | regional | SRIV (`seguridad.durango.gob.mx`, portada) | SRIV (`fiscalia.durango.gob.mx`) |
| Coahuila | propia | NO REVISADA | SRIV (`sitio.fgecoahuila.gob.mx`) |
| Nuevo León | propia · **hechos** (`-008`, `-011`) | SRIV (`fuerzacivil.nl.gob.mx`, parcial) | SRIV (`fiscalianl.gob.mx`, parcial) |
| Tamaulipas | propia (fosas) | NO REVISADA | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | regional | SRIV (`seguridad.slp.gob.mx`) | SRIV (`fiscaliaslp.gob.mx`, sin fecha) |
| Zacatecas | propia | SRIV (`ssp.zacatecas.gob.mx`) | SRIV (`fiscaliazacatecas.gob.mx`) |
| Jalisco | propia | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Colima | propia | portal (`col.gob.mx`) | SRIV (`fgecolima.mx`) |
| Nayarit | regional | SRIV (`ssypc.nayarit.gob.mx`, organigrama) | NO REVISADA |
| Aguascalientes | NO REVISADA | portal (`aguascalientes.gob.mx`) | NO REVISADA |
| Michoacán | propia · **`-REC-002`** | NO REVISADA | NO REVISADA |
| Guanajuato | propia | NO REVISADA | SRIV (`portal.fgeguanajuato.gob.mx`) |
| Ciudad de México | regional | SRIV (`ssc.cdmx.gob.mx`) | NO REVISADA |
| Estado de México | propia | SRIV (`sseguridad.edomex.gob.mx`) | NO REVISADA |
| Morelos | regional | portal (`morelos.gob.mx`) | SRIV (`fiscaliamorelos.gob.mx`) |
| Puebla | propia | SRIV (`ssp.puebla.gob.mx`) | NO REVISADA |
| Tlaxcala | regional | portal (`comunicacion.tlaxcala.gob.mx`) | NO REVISADA |
| Hidalgo | propia | SRIV (`s-seguridad.hidalgo.gob.mx`, PDF) | SRIV (`procuraduria.hidalgo.gob.mx`, parcial) |
| Querétaro | regional | SRIV (`sscqro.gob.mx`) | NO REVISADA |
| Veracruz | regional | NO REVISADA | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | regional · **hecho** (`-002`) | NO REVISADA | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | propia · **`-REC-001`** | portal (`guerrero.gob.mx`) | SRIV (`fiscaliaguerrero.gob.mx`) |
| Chiapas | regional | SRIV (`sspc.chiapas.gob.mx`) | NO REVISADA |
| Oaxaca | propia · **hecho** (`-001`) | NO REVISADA | NO REVISADA |
| Campeche | propia | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Yucatán | propia | NO REVISADA | SRIV (`fge.yucatan.gob.mx`) |
| Quintana Roo | propia | NO REVISADA | NO REVISADA |

**Sentencias: 15 de 32** (4 parciales); **17 `NO REVISADA`**. **Armamento: 14 por dominio propio** (5 parciales), **5 por portal**, **13 `NO REVISADA`**. **Alto impacto: 20 propia, 11 regional, Ags `NO REVISADA`.**

## 9. Desglose de cálculos propios

- **Muertos por agresión en hechos propios**: Juchitán 2 + Culiacán 1 + 1 + Mazatlán 1 + 1 = **6**. Cuerpos en fosa: **2**. Abatidos: **2**. Heridos: Juchitán 1 a 3 + Culiacán 1 + Juárez 1 = **3 a 5**. Detenidos sin aseguramiento: **3** (`-010`); en filas de armamento fuera del total: 9 + 3.
- **Duración**: 19-oct 11:05 → 20-oct 07:06 = 20 h 01 min. **Densidad**: 11 / 20,02 = 0,549 → **0,55**.
- **Marcas**: FRONTERA 2 (`-007`, `-010`); día de apertura 8 (`-002`, `-003`, `-004`, `-005`, `-006`, `-008`, `-009`, `-011`); sin ruta con fecha 1 (`-001`).

## 10. Los dos controles editoriales

*(Se completa tras la primera ronda.)*

## 11. Herramientas

`tools/datos-argos-138.py` (copia de 137) → `reports/argos-2026-10-20.html`; `gen-movil.py 138 2026-10-20 137 2026-10-19 07:06`; `gen-texto.py`; `validar.js … 2026-10-19 2026-10-20` → «validación OK».

## 12. Lecciones de método (no van al cartelón)

1. **Dos de las cuatro pistas «posibles rojos» heredadas eran señuelos de fecha** (Copanatoyac 2025, Luis Moya agosto) y la tercera no era homicidio (Colima): una pista sin fecha se fecha antes de heredarla.
2. **Los dos rojos del corte llegaron sin ruta con fecha** (Juchitán, Cárdenas): el criterio de 137 los habría dejado fuera; se declaró la excepción en §6.
3. **La sección «AJENOS» volvió a aportar hechos**: Cárdenas (Noreste) y Ciudad Juárez (Golfo y Noreste).
4. **Ningún equipo tuvo Bash**: el `grep` literal de la plantilla debe reescribirse para la herramienta Grep.
