# ARGOS 143 — Archivo de fuentes

**Corte**: 2026-10-28 · **Ventana**: 27-oct 08:45 → 28-oct 08:28 CDMX (**23 h 43 min**; `WINDOW_DAYS = 2`) · **Densidad**: 10 hechos propios / 23,72 h = **0,42 hechos/hora**, cálculo propio (0 🔴, 9 🟡, 1 🟢; 7 entidades). **Cuatro recuperaciones de alto impacto** (tres de la ventana de 142, una de la de 138), fuera de totales. Borrador previo a la ronda 1: 11 hechos (0,46), con Tabasco como rojo propio.
**Hora de cierre**: hora real del Bloque 0 (08:28 CDMX del miércoles 28), declarada al destinatario. «Procede» a las 08:31 (3 min después): sin ajuste de cierre. La ola corrió de 08:33 a 08:40 aprox.; la ronda 1 de controles, de 08:45 a 09:00. Marca «Consulta»: ver §11.

Informes de los seis equipos (condensados por el coordinador: datos, URL y marcas íntegros), notas del coordinador y controles: `reports/argos-2026-10-28-equipos.md`. Plantilla: `tools/plantilla-equipos-143.md`. Generador: `tools/datos-argos-143.py`.

## 1. La base

- 28-oct 08:28: clon en la rama de sesión `claude/argos-criminal-intelligence-otiawj`, en `670bbe1` («Orden de ARGOS 143: fecha del miércoles 28-oct»), ya en la punta: las cinco fusiones *fast-forward* (`main`, `139-qe9f01`, `140`, `141-nacional-kh5fj6`, `criminal-intelligence-otiawj`) devolvieron «Already up to date». 240 archivos en `reports/`; última edición `argos-2026-10-27`.
- Ramas remotas nuevas, ajenas a la serie: `claude/argos-intake-app-f5wicf`, `claude/plataforma-victimologia-forense-ou0o3u` (no tocadas).
- Rama de trabajo y de *push*: `claude/argos-criminal-intelligence-otiawj`.

## 2. Red y modo de búsqueda

- `curl https://www.gob.mx/fgr` → `000` (28-oct 08:28). **Egreso bloqueado: solo WebSearch.** Techo ★★★★☆; esta edición no supera ★★★☆☆.
- Consulta de control en los dos modos: `extended` trae hechos de la ventana (Chihuahua Sol de Oriente, Celaya); `standard`, nada de la ventana (Tehuitzingo, bares sin fecha). **Todo `extended`.**
- Presupuesto: control 2 · coordinador 18 + 2 (horas de dos rojos, tomadas de la cuota de controles) · ola 150 (6 × 25, agotada en los seis) · `procedencia-cifras` R1 23 · R2: ver §11.

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

- **Ciclo A** (Noroeste + Centro encabezan el triaje judicial), después de la prioridad sobre el ciclo.
- **Sentencias `NO REVISADA` en 142 (9)**: revisadas ahora NL, Tamps (nominal: solo convocatorias / informes), Ags, Gto (solo páginas institucionales), CDMX, Edomex, Mor, **Tlax y Hgo (tras dos ediciones)**. **Dominios sin páginas en 142 (4)**: resueltos Son (`fiscalia.sonora.gob.mx`) y Nay (`fgenay.gob.mx`); siguen Coah y Camp.
- **Armamento `NO REVISADA` en 142 (20)**: revisadas ahora Sin, Chih, Zac, Jal, Nay, Ags, Gto, CDMX, Pue, Tlax, Chis (11); siguen BC, BCS, Son, Dgo, Mor, Hgo, Qro, Camp (8), y Coah pasó a dominio sin páginas; Oax sigue sin páginas.
- **Alto impacto solo amplia en 142 (10)**: con consulta propia ahora BCS, Son, Sin, CDMX, Tlax (**Tlax, tras dos ediciones**), Camp, Yuc (7); **siguen solo amplia Jal, Col, Nay** (tercera edición para ninguno; segunda consecutiva): prioridad de 144.
- **Qué aportó la rotación**: el triaje judicial de Noroeste y Centro confirmó dos dominios que llevaban dos ediciones sin hallarse (Tlaxcala `fgjtlaxcala.gob.mx`, Hidalgo `procuraduria.hidalgo.gob.mx`) y la variante de Sonora (`fiscalia.sonora.gob.mx`); cerró Tulantepec como «sin cambio» antes de gastar más búsquedas y fechó en junio Cañada Morelos. Ninguna sentencia integrable.

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **26-oct** | **Existe**, sin indexar en `gob.mx`: solo por republicadores (Milenio https://www.milenio.com/policia/acciones-relevantes-gabinete-de-seguridad-26-de-octubre-2026 · RED113 2026/10 · Tallapolítica · Certeza Diario): **una fuente**, corroboración débil por construcción. Acciones del 26: ventana de 142; todas 🟢 o aseguramientos: vistos |
| **27-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en día suelto, por rango («26 y 27») y por título sin `site:`, al arrancar (08:31) y en la repetición final (08:40) |
| **Año trampa** | «26 y 27 de octubre» devuelve el 27-oct-**2025** y el agregado 24-26-oct-**2025** |
| **gabinetedeseguridad.gob.mx** | Último indexado: 16-18-oct |

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Ciclo** | A, declarado (§3) |
| **1. Tulantepec** | **Sin cambio**. Reprogramación al 28-oct 17:00, solo por resumen (La Jornada Hidalgo, sin fecha); **hora posterior al cierre**: pasa a ARGOS 144. Fallo del 8-oct (ARGOS 141), publicado el 9 |
| **2. Morelia–Tumbisca (`ARG-142-013`)** | Todos los medios dicen «en la mañana»; ninguna hora (Medianews, Quadratín, La Voz, MiMorelia, PCM, Noventa Grados, 1plana, MoreliActiva). **Sigue `FRONTERA`; sin fe de erratas** |
| **3. Cláusulas de retiro de 142** | Cutzato `-005`: día del hallazgo no fijado (sin búsqueda propia). Apatzingán `-007`: mayoría «tarde del 26», solo 1plana ~03:30; sin ancla. Cajeme `-011`: día no fijado (rutas del 26). **Ninguna se ejecuta** |
| **4. Acámbaro, Campamento Ferrocarriles** | **Recuperado: `ARG-143-REC-003`** (🔴, 2 muertos por titular; publicado el 19 por ruta; ~22:00 por resumen → ventana de ARGOS 138) |
| **5. Cañada Morelos** | **Descartado**: doble homicidio del miércoles 24-jun-2026 (e-consulta 2026-06-25); identidad con La Jornada de Oriente por contenido |
| **6. Boletín federal** | §4 |
| **7. Fichas de 142** | Tecate `-001/-009`: heridos 1 (El Imparcial; Punto Norte 2026/10/26) o 2 (Milenio): sin arbitrar; «2 mueren» solo en Radar Tecate; 3 detenidos por titular de Zeta (2026/10), dos juegos de nombres incompatibles; armas sin cifra; sin comunicado de la SSC · Tecate `-002`: «madre, hija y dos nietos», por titular (Milenio); La Verdad discrepa; sin boletín FGE BC · Tehuacán `-003/-010`: «hieren a otro» (titular), calidad no fijada; **2 detenidos y 1 AR-15 por titular** (Síntesis 2026/10/27); vinculación no hallada · SLP `-008`: N+ (sin fecha) no identifica el hecho: sigue fuente única |
| **8. Seguimiento** | Exfiscal `ARG-136-006`: impugnación anunciada en la causa federal y apelaciones en la local; sin resolución · Xalapa `ARG-140-020`: prisión preventiva (proceso 879/2026), vinculación no hallada · Juchitán `ARG-140-021`: vinculación no hallada (boletín FGEO 2,914 de la detención) · Pénjamo `ARG-141-001`: sin avance; Ariel «N» es otro hecho · Linares `ARG-140-013`: 47 (MVS) / 55 (Posta), ambos por resumen, y colonia contradicha (La Petaca / Infonavit Río Verde) |
| **9. Sentencias candidatas** | FGR Tepic: comunicado 753/26 del **26-oct** (listado FGR, por resumen): publicada antes de la ventana · Ramos Arizpe: sin ruta con día ni boletín: homónimo / pendiente · Guadalajara: no localizada · **Nueva: Fresnillo** (68 años por titular; pendiente) |
| **Heredados** | FE-001 de 141: Acultzingo 22:00-23:00 solo por resumen; sigue condicionada · FE-001 de 140 (Ecatepec): no revisada · Río Bravo: sin fecha fiable · Nogales, Ajuchitlán, Taxco, El Tívoli, Coquimatlán, Patamban, Tecuala: no revisados · Huimanguillo: identificación solo por familiares, nombres contradictorios |

## 6. Arbitrajes del coordinador

- **Hechos propios (10)**, todos 🟡 salvo uno 🟢, todos `PUBLICADO EL DÍA DE APERTURA SIN HORA`:
  - `ARG-143-001` Celaya, carretera Salvatierra–Celaya — **🟡 por arbitraje**: los titulares con ruta del 27 sostienen una **declaración nombrada del secretario de Seguridad** sobre un «ataque contra elementos de la SSPC en operativo» (Heraldo de México, Tribuna), pero también que el patrullaje **detectó un asalto en curso y lo frustró** (La Silla Rota, *slug*; La Jornada, titular). La regla de quién inicia distingue la agresión a un patrullaje (🔴) de la acción de la autoridad repelida (🟡): aquí la autoridad intervino un delito en flagrancia y fue agredida al intervenir → **confrontación derivada de una intervención, 🟡**. El abatido y el herido (asaltantes) no se cuentan como víctimas. **Decisión reversible por el destinatario**: si se juzga agresión a un patrullaje, sube a 🔴 (+1 rojo, 1 entidad con rojo).
  - `-002` Celaya, Mercado de Abastos (comerciante; tres rutas del 27) · `-003` Salamanca, San Roque (conductor; fuente única; retiro) · `-004` Chihuahua, Sol de Oriente (1 muerto; heridos 1 o 2: se cuenta 1, criterio conservador de 142) · `-005` Tijuana, Lomas de San Antonio (hora 08:30 / 08:46: retiro) · `-006` Guadalupe NL, Valle Soleado · `-007` Culiacán, Chulavista (de noche o primeras horas por resumen: retiro) · `-008` Culiacán, Aguaruto (cuerpo decapitado, 🟡 cuerpo único; precedente: tres cuerpos sin causa = 🔴, ARG-139-002) · `-009` Veracruz, col. Centro (golpes o riña: contradicho; retiro) · `-010` Rayón SLP (🟢 órdenes de aprehensión cumplimentadas por homicidio del 12-oct; posible reclusión previa por resumen; retiro).
- **Tabasco, tres cuerpos (Villahermosa–Frontera)**: **pasa de hecho propio a `ARG-143-REC-004`** tras la ronda 1 (los dos controles). Ninguna ruta lo fija en el 27; el único dato del día («el día anterior», 26) apunta a la ventana de 142, y el primer cuerpo («primeras horas») puede ser de la de 141. El borrador lo tenía como único rojo propio: la edición queda **sin rojos propios**.
- **Recuperaciones (4)**, todas 🔴, fuera de totales: `REC-001` Tecate, fosa con 3 personas (Punto Norte 2026/10/26; ubicación Cerro Azul / Nueva Hindú no fijada; posible mismo hallazgo que el de Zeta) · `REC-002` Dolores Hidalgo, florería atacada con bomba molotov y un hombre baleado que murió (ataque del 26 por ruta; 🔴 por artefacto incendiario = AEI en la taxonomía de CLAUDE.md) · `REC-003` Acámbaro, Campamento Ferrocarrilero (ventana de 138) · `REC-004` Tabasco.
- **Vistos, con motivo**: Guasave, «Chuy» González abatido por la Marina el 26 (la Marina «repelió una agresión» en trabajos de inteligencia, por resumen: 🟡, ventana de 142, no recuperable; 2 muertos, el segundo de rol desconocido) · Arizpe (🟢, 24-oct) · Tlaxcala, 8 cateos y 9 detenidos, «El Delta» (🟢, noche del 25 a mañana del 26; boletín del 26) · Zinapécuaro (boletín del 26; posible duplicidad con nota de la SSP) · Culiacán: Infonavit Barrancos frente a primaria, ciclista frente a la Feria Ganadera, cuerpo en Tierra Blanca (sin ruta con día; Tierra Blanca, hora en torno a la apertura) · Juchitán La Amistad / 10 de Mayo y Jalapa de Díaz (sin ruta con día; posible duplicidad entre los dos de Juchitán) · Texmelucan (sin ruta fechada) · Catemaco (sin ruta) · Tijuana, Brisas de Santa Fe (no confirmado) · Tecnológico de Veracruz, ácido pícrico (26-oct, accidental) · «El Moro», Acapulco (24-oct o 27, contradicho) · Topo Chico (25-oct) · Tecali de Herrera (sin fecha, no buscado) · Ensenada, mujer muerta (día no fijado) · Mazatlán, cabeza frente al Palacio Municipal (día no fijado).
- **Descartados**: San Miguel de Allende (21-ene) · Cañada Morelos (24-jun) · Policía estatal de Puebla = `ARG-134-005` (16-oct) · Agente PFM Edomex = `ARG-134-REC-004` (12-oct) · El Saucito (27-sep) · Purísima del Rincón (24-oct) · Acultzingo, Tuxpan (ventana de 140).

## 7. Fe de erratas (no va al cartelón)

- **`ARG-143-FE-001` (a ARGOS 142)**: `REC-001`, `REC-002` y `REC-004` → **rojos 7 → 10, muertos 15 → 16, cuerpos hallados 1 → 7** (cálculo propio); entidades 6 → 7 (+Tab). **Condicionada**: horas de REC-001 y REC-002 y día de REC-004, solo por resumen; si el primer cuerpo de REC-004 fue anterior a las 08:37 del 26, uno de los tres cuerpos corresponde a ARGOS 141.
- **`ARG-143-FE-002` (a ARGOS 138)**: `REC-003` → **rojos 2 → 3, muertos 8 → 10** (cálculo propio); entidades sin cambio (Gto ya contada). Condicionada: hora solo por resumen (publicado el 19 por ruta).
- `ARG-141-FE-001` y `ARG-140-FE-001` siguen condicionadas; Río Bravo (129) condicionada.

## 8. Registro del barrido — por entidad

Sentencias: **23 revisadas** (de ellas 6 sin boletines del periodo: NL, Tamps, Son, Sin, Gto, Hgo), **2 dominios sin páginas** (Coah, Camp), **7 `NO REVISADA`** (BCS, SLP, Zac, Col, Mich, Pue, Qro). Armamento: **16 por dominio**, **2 sin páginas** (Coah, Oax), **14 `NO REVISADA`** (BC, BCS, Son, Dgo, SLP, Col, Edomex, Mor, Hgo, Qro, Gro, Camp, Yuc, QRoo). Alto impacto: **22 con consulta propia**, **10 solo amplia** (Dgo, Jal, Col, Nay, Ags, Edomex, Mor, Hgo, Qro, Chis).
- **Criterio único de `REVISADA`** (arbitraje, hallazgo 14 de `editor-duplicidad` R1): una búsqueda dirigida que devolvió páginas del dominio oficial, aunque solo sean institucionales; el subconjunto sin boletines del periodo se declara aparte. Coahuila en armamento: el informe Noreste se contradice (NR / sin páginas); se registra **sin páginas** porque la consulta a `fiscalia.coahuila.gob.mx` sí se hizo. Chihuahua en armamento: `fiscalia.chihuahua.gob.mx` devolvió páginas antiguas → REVISADA, SRIV.
- **Dominios confirmados**: `fgjtlaxcala.gob.mx`, `procuraduria.hidalgo.gob.mx`, `fgenay.gob.mx`, `fiscalia.sonora.gob.mx`. **Sin páginas**: `fiscaliageneral.coahuila.gob.mx`, `fiscalia.coahuila.gob.mx`, `fgecampeche.gob.mx`, `fiscaliacampeche.gob.mx`, `ssp.oaxaca.gob.mx`, `pgjhidalgo.gob.mx`.

## 9. Emisores por ficha

El recuento I/N/R/A de cada ficha está en `tools/datos-argos-143.py`; las URL, en el archivo de equipos y en los informes de los controles (§11).

## 10. Desglose de cálculos propios

- Muertos por agresión: 7 = 1 (-002) + 1 (-003) + 1 (-004) + 1 (-005) + 1 (-006) + 1 (-007) + 1 (-009). Heridos: 1 (-004; 2 en dos medios). Cuerpos: 1 (-008). Fuera: abatido y herido de -001 (asaltantes).
- Recuperaciones: 3 muertos (REC-002 1, REC-003 2) y 6 cuerpos (REC-001 3, REC-004 3).
- Entidades: 7 (Gto, Chih, BC, NL, Sin, Ver, SLP); con rojo, 0. Densidad: 10 / 23,72 = 0,42. Marcas: 10 APERTURA, 0 FRONTERA. Cláusulas de retiro: 5 (-003, -005, -007, -009, -010); mínimo de entidades si se aplicaran todas: 4.
- Conclusiones (días con ambos extremos): Acámbaro 19 y 26-oct (8 días) · Culiacán 11 hechos del 15 al 27-oct (13 días): ARG-134-013, ARG-135-001, 135-007, 136-004, 137-009, 138-003, 138-004, 140-004, 141-004, 143-007, 143-008 · Salamanca 5 hechos del 7 al 27-oct (21 días): ARG-126-002, 133-002, 136-001, 137-015, 143-003 · motocicleta: -002 y -006 · sin detenido: 9 de 9 amarillos.

## 11. Los dos controles editoriales

**Ronda 1** (en paralelo): `editor-duplicidad` — CORREGIR (16 hallazgos; 0 duplicidades; 0 falsos vacíos; cobertura aritmética correcta) · `procedencia-cifras` — CORREGIR (22 correcciones; 23 de 24 búsquedas).
**Aplicados**: Tabasco a `REC-004` (§6) · Celaya: declaración del secretario por titular, nuevas rutas (Heraldo, Tribuna, La Jornada, ABC Noticias), herido del lado de los asaltantes registrado aparte, color arbitrado (§6) · Mercado de Abastos con AM y Noticieros en Línea (ya no fuente única) y hora contradicha · «Siguen» y «Comando» fuera de los títulos · Sol de Oriente: heridos 1 o 2, se cuenta 1 · Valle Soleado: cruce contradicho; MVS del 28 con hora no fijada · Chulavista con Luz Noticias, «dentro / frente a» contradicho, deslinde con el homónimo de Mazatlán · Aguaruto con Luz Noticias, punto contradicho, deslinde corregido · Veracruz: golpes o riña · Rayón: Fiscalía por titular, órdenes cumplimentadas, posible reclusión previa · REC-001: ubicación no fijada y «posible mismo hallazgo» · REC-002: muerte publicada el 27, N+ fuera · REC-003: sección «opinión», «lunes» por resumen · REC-004: Macultepec, arma de fuego por resumen, ARG-137-005 · cláusulas con −1 entidad · Valoración reescrita (sin rojo propio; seis entidades; sin re-titular) · Conclusión 4 del borrador (tiempos procesales, «33 meses») **retirada**; Salamanca es ahora la Conclusión 3 · la de motocicleta pasa a Conclusión 4, sin ARG-142-006, como «desarrolla la Conclusión 4 de ARGOS 142» · Conclusión 2 «desarrolla ARGOS 138 y 140» · Conclusión 5 sobre los nueve amarillos y seis entidades · seguimientos del panorama reducidos a pasos procesales (Tecate, SLP, Tumbisca y Linares, aquí, §5) · candidatos de sentencias marcados como heredados; Tulantepec 8-oct; Fresnillo con fecha 27 o 28 y nombre contradicho · vistos de armamento con marcas · `gabinetedeseguridad.gob.mx` como SRIV · subconjunto de fiscalías sin boletines.
**No aplicado, con motivo**: columna «Armamento especial» en la tabla de totales (heredado de 142; todo n/d; sin pérdida de dato) · «1 eventos» (concordancia heredada del generador del semáforo).

**Equivalencia de ARG-ID** (los informes de equipos y de la ronda 1 usan la numeración del borrador): borrador -001 (Tabasco) → `REC-004` · -002 → -001 · -003 → -002 · -004 → -003 · -005 → -004 · -006 → -005 · -007 → -006 · -008 → -007 · -009 → -008 · -010 → -009 · -011 → -010. REC-001 a -003 sin cambio.

**Ronda 2** (en serie): `editor-duplicidad` R2 — CORREGIR (13 hallazgos menores; 0 duplicidades; aritmética, fe de erratas contra 142 y 138 y cobertura limpias; validador OK). **Aplicados**: Chulavista de Mazatlán «visto en ARGOS 132» · Conclusión 3 «cinco puntos distintos» y «cuatro si se retira -003» · Rayón con Institucional 1 (Fiscalía por titular) · Veracruz con N+ como segundo nacional · frase «no se reverificaron» sustituida por «cotejados contra el índice» · REC-004 a ★★☆☆☆ (una sola ruta fechada) · Conclusión 2 con ARG-134-013 (11 hechos, 15 al 27-oct, 13 días) y Barrancos como misma colonia · Celaya: «quién abrió fuego primero: no publicado», «🟡 por reserva», y marca en la Valoración 2 · seguimiento de Tehuacán reducido a ARG-142-010 · ARG-140-006 del 21-oct · Tulantepec «candidato de ARGOS 140 a 142» · equivalencia de ARG-ID y FE-002 con totales · índice y pendientes (cierre).
`procedencia-cifras` R2: ver el archivo de equipos.

## 12. Herramientas

`python3 tools/datos-argos-143.py reports/argos-2026-10-27.html reports/argos-2026-10-28.html` · `python3 tools/gen-movil.py 143 2026-10-28 142 2026-10-27 08:28` · `python3 tools/gen-texto.py reports/argos-2026-10-28.html reports/argos-2026-10-28.txt` · `node tools/validar.js reports/argos-2026-10-28.html 2026-10-27 2026-10-28` → validación OK.

## 13. Lecciones de método (no van al cartelón)

0. **El único rojo propio del borrador era de la ventana anterior**: Tabasco llegó con ruta del 27 (publicación) y el día del hallazgo solo en el resumen («ayer»). La marca «publicado el día de apertura» no resuelve la fecha del hecho: cuando el único dato del día apunta a la ventana anterior, el hecho es `-REC-`, no propio con cláusula.
1. **La ola subestimó la fuente institucional de Celaya**: los equipos leyeron la declaración del secretario solo en resúmenes; `procedencia-cifras` halló cuatro titulares con ruta fechada. La pregunta «¿hay declaración nombrada por titular?» debe ir en los encargos de todo hecho con fuerzas federales.
2. **Tres «fuentes únicas» no lo eran** (Mercado de Abastos, Chulavista, Aguaruto): los equipos se detuvieron en el primer medio fechado. Antes de marcar fuente única, una búsqueda por el topónimo exacto.
3. **El recall trajo tres señuelos rojos de otras fechas** (policía de Puebla, 16-oct; San Miguel de Allende, enero; El Saucito, septiembre): el resumen del buscador mezcla fechas cuando la consulta lleva «este martes».
4. **«Procede» a tiempo**: 3 min. Ola y ronda 1 terminaron antes de las 09:00.
