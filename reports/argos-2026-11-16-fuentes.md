# ARGOS 152 — Archivo de fuentes (corte 2026-11-16)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 152 |
| Archivo | `reports/argos-2026-11-16.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **dom 15-nov 10:24 → lun 16-nov 10:30 CDMX** · duración **24 h 06 min** (cálculo con `date`) |
| Calendario | dom 15 (10:24–24:00, 13 h 36) · lun 16 (00:00–10:30, 10 h 30) |
| Hora de arranque (Bloque 0) | 10:30 CDMX · «Procede» a las 10:32 (2 min): no se ajusta el cierre |
| Consulta | última búsqueda: 10:58 CDMX (cierre de `procedencia-cifras` R2) |
| `WINDOW_DAYS` | 2 (la plantilla de 151 ya traía 2: sin reemplazo; aserción `WINDOW_DAYS = 2;` única) |
| Ciclo | **A** (Noroeste + Centro encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Red | `curl https://www.gob.mx/fgr` → `000` (16-nov 10:30): egreso bloqueado (`connect_rejected`); solo WebSearch |
| Rama | `claude/argos-152-nacional-reqwch` (fast-forward hasta `claude/argos-151-nacional-c9xttt`, 151) |

## 2. Resultado del corte

- **9 hechos propios** (🔴 5 · 🟡 3 · 🟢 1) en 9 entidades (NL, BC, Tab, Oax, Sin, Mich, Chih, Tlax, Edomex); densidad 0,37 hechos/hora (cálculo propio).
- **2 recuperaciones 🔴** de la ventana de 151: `ARG-152-REC-001` Chignahuapan (madrugada del 15 por titular) y `ARG-152-REC-002` Tijuana, La Postal (sábado 14 por resumen).
- Muertos por agresión 12 · heridos 7 · cuerpos 0 · privados de la libertad 5 (Tecate) · recuperaciones 7 muertos (cálculo propio).
- Armamento integrado: ninguno; Edomex (huachicol) cualitativo: armas solo por resumen.
- Sentencias integrables: 0.
- Marcas: 8 `FRONTERA DE VENTANA — HORA NO FIJADA` (todos los hechos publicados el domingo 15, día de cierre de 151) · 4 cláusulas de retiro (-002 Tecate ~01:00; -003 Gaviotas Sur, noche del 14 o madrugada del 15; -004 Lachigalla ~07:00; -005 Pueblo Nuevo ~00:40: horas solo por resumen).

## 3. Fe de erratas a ediciones anteriores

| Código | Edición | Corrección |
|---|---|---|
| `ARG-152-FE-001` | 151 | Se recuperan Chignahuapan y Tijuana, La Postal (🔴): semáforo corregido de 151 = 6 🔴 · 3 🟡 · 2 🟢 (cálculo propio). Si las cláusulas de retiro de -002 a -005 se activan, esos cuatro rojos pasan también a 151 |
| `ARG-152-FE-002` | 151 | `ARG-151-002` Jolalpan: «tres muertos, entre ellos dos policías de Morelos», por titular (Cinco Radio; E-consulta); cifra 2, 3 o 4, contradicha; se mantienen 2 |
| `ARG-152-FE-003` | 151 | `ARG-151-003` carretera 190: «empresario, empleada y escoltas», por titular (Proceso 2026/11/15); identificación pericial pendiente |

## 4. Boletín federal (triple consulta)

| Momento | Día suelto | Rango | Título sin `site:` | Resultado |
|---|---|---|---|---|
| Inicio | «"15 de noviembre" 2026 detenidos armas» | «13, 14 y 15 de noviembre» | «informa acciones relevantes "13 de noviembre de 2026"» | SRIV; último indexado: acciones del 12-nov (Milenio, Ultranoticias, SICOM, RED113, Tallapolítica, Certeza, Consulta Monterrey) |
| Cierre | «"15 de noviembre" … Milenio 2026» | «del 13 al 15 de noviembre 2026» | «informa acciones relevantes "14 de noviembre de 2026"» | SRIV |

Segundo lunes sin agregado indexado del fin de semana: las acciones del 13 al 15 pasan a 153.

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| Cláusula `-151-002` Jolalpan | Día 14 ~14:30 solo por resumen (Urbano); rutas sin día: cláusula sigue abierta; «tres muertos» por titular (FE-002) |
| Cláusula `-151-009` Tepehuacán | ~02:00 del 14 solo por resumen; día 14 por tres rutas (La Silla Rota, Infobae, Tribuna): cláusula sigue abierta |
| Frontera de 151 (-001, -003, -007, -008, -009) | Ninguna hora fijada por fragmento: marcas permanentes |
| Reservas -001 Texhuacán | Secretario de Gobierno de Veracruz: la FGE intervino, sin detenidos (La Silla Rota 2026/11/15, resumen); gobernadora: FGE y FGR coordinadas (Meganoticias, titular); tercera ocupante «gravemente herida» (Diario Puntual 2026/11/16), estado no informado por autoridad |
| Reservas -002 Jolalpan | 2/3/4 muertos (FE-002); atribución solo Periódico Central (NO OFICIAL); sin detenidos |
| Reservas -003 carretera 190 | Proceso: «empresario, empleada y escoltas» (FE-003); PABIC por resumen; calcinados 4 o 2 sin arbitrar; identificación pendiente |
| Reservas -005 | Momento sin fijar (madrugada del 15 por resumen; Luz Noticias 315036) |
| Reservas -007/-008 | Sin segunda fuente para Nogales; sin cifra de autoridad para detenidos; -008: Sinaloahoy «al menos dos armas largas, cartuchos, placas balísticas» (posible mismo operativo) |
| Reservas -009 | Tres identificados por la PGJEH, ningún detenido (Periódico Central, titular) |
| Duplicidad -004 | Nota de Noroeste «zona turística… un muerto y una mujer herida» (CM592554) es antigua: descartada. Día de La Malinche (14 o 15) sin ruta |
| Rojo sin ruta Chignahuapan | Seis rutas del 15 + «madrugada» por titular (TV Azteca): `ARG-152-REC-001` |
| REC-001 El Arenal | Domingo 8 ~11:22 por resumen; causa no confirmada por autoridad; sin cambio |
| Cláusulas de 150 | `-011` SJR: rutas del 10 (Expreso Querétaro; Noticias de Querétaro 11): sigue · `-004` Tuxpan: rutas del 12 (Miled; Golpe Político); segunda víctima muere el 13 (Yucatán 2026/11/13); detenidos sin vinculación hallada · `-005` Juchitán: jueves 12 por convergencia; sin cambio · `-006` San José del Rincón: 10 u 11 · `-012` Silao: 12 o 13 · `-013` Temascatío: Defensa «recorridos» vs SSP «cumplimentar detenciones»: 🟡 con reserva · `-010` Las Víboras: cantidad no publicada |
| Cláusulas de 149 y 148 | `-149-020/-021`: sin día dentro del agregado · `-149-006`: superficie (resumen) vs «fosa clandestina» (La Opinión 2026/11/10, titular) · `-149-013` Cosoleacaque: día 9 por ruta, ~08:00 resumen · `-149-019` Acapulco: no consultado · `-149-005` Río Bravo: lugar Zacatecas (Expreso 2026/11/09) o SLP; rescate o fuga contradicho · `-148-007`: día sin fijar |
| Boletín federal | SRIV (sección 4) |
| Sentencias candidatas | Monterrey (col. Bella Vista, 25 a 10 m, pena compuesta; `fiscalianl.gob.mx` sin boletines indexados) · Tabasco 5119 (URL individual no identificada; Tabasco HOY: posible homónimo) · Veracruz 88 (sin boletín) · Champotón (solo PorEsto; dominio de la fiscalía de Campeche no confirmado, tercera edición) |
| Seguimientos | Zapopan: audiencia de 5 escoltas el 15-nov, resultado no hallado · Cuernavaca `-147-001`: detenido 11/12-nov (Infobae; Harfuch por titular), audiencia el 17-nov (resumen) · «El Panda»: sin audiencia nueva · Matamoros `-144-008`: sin detenidos · Mexicali `-146-011`: no consultado · Tuxpan `-150-019`: no consta · Cajeme: ataque contra una familia con una niña muerta (fecha no fijada); «suman 5 detenidos» (Heraldo 2026/11/13); detenciones en ventana de 150: **posible omisión de 150**, pendiente de fijar el día del ataque |

## 6. Fuentes por ficha (lista íntegra)

- **ARG-152-001 Galeana**: Enfoque Monterrey (2026/11/16) · MVS Noticias (2026/11/16, dos notas: 753601 y 753613) · ABC Noticias (2026/11/16) · Punto x Punto (2026/11/16) · El Heraldo de México (2026/11/16) · Milenio · El Norte · Posta · Telediario · N+ · Meganoticias · ENfoque.
- **ARG-152-002 Tecate**: Diario de Yucatán (2026/11/15) · Radar Tecate News (2026/11/15) · El Universal · El Tiempo MX · Videa TV · Poder MX («reportan dos desaparecidos»). Alfredo Álvarez y El Congresista: consultados por la ola, no localizados en R1; no contados.
- **ARG-152-003 Gaviotas Sur**: Proceso (2026/11/15) · El Heraldo de México (2026/11/15) · Diario de Yucatán (2026/11/15) · El Universal · UnoTV · Posta · Quadratín Tabasco · XEVT.
- **ARG-152-004 Lachigalla**: La Jornada (2026/11/15) · Proyecto Puente (2026/11/15) · El Universal Oaxaca · El Imparcial de Oaxaca · ADN Sureste («14:30 h») · Meganoticias · El Sol del Sureste · NVI Noticias · Zócalo.
- **ARG-152-005 Pueblo Nuevo**: Informador (20261115) · Luz Noticias (2026-11-15, 315113) · Línea Directa (2026-11-15) · Noroeste · Infobae/EFE (2026/11/16, agregado).
- **ARG-152-006 Colinas del Sur**: Grupo Marmor (2026/11/15) · Quadratín · MiMorelia · Contramuro · La Voz de Michoacán · A Tiempo.
- **ARG-152-007 Anapra**: El Diario de Juárez (2026/nov/15) · NetNoticias.
- **ARG-152-008 Calpulalpan**: Gente Tlx (2026/11/15) · Cinco Radio · Meganoticias · La Prensa de Tlaxcala (2026/11). Quadratín Tlaxcala: cita no localizada en R1, retirada.
- **ARG-152-009 Edomex**: La Silla Rota (2026/11/15) · El Heraldo de México (2026/11/15) · Proyecto Puente (2026/11/15) · El Diario de Chihuahua (2026/nov/15) · El Diario del Noroeste (2026/nov/15) · SinEmbargo · López-Dóriga · Quadratín Edomex · Digitalmex · Mexiquense Digital (20261116).
- **ARG-152-REC-001 Chignahuapan**: Infobae (2026/11/15) · Síntesis (2026/11/15) · La Silla Rota (2026/11/15) · El Heraldo de México (2026/11/15) · El Heraldo de Puebla (2026/11/15) · Latinus (2026/11/15) · Diario Puntual (2026/11/16) · TV Azteca · El Universal · MTP Noticias · El Congresista · Sucesos Puebla · Quadratín Puebla.
- **ARG-152-REC-002 Tijuana**: Periodismo Negro (2026/11/15) · Diario Tijuana (2026/11) · Síntesis TV.

## 7. Procedencia: decisiones de clasificación

- **Criterio de frontera uniforme (deuda de 151)**: los hechos publicados el domingo 15 con hora solo por resumen se fichan en 152 con FRONTERA; si la hora del resumen es anterior a las 10:24, además cláusula de retiro. La hora del resumen nunca decide sola la ventana.
- **Chignahuapan como -REC-**: la madrugada la fija un titular (TV Azteca), no solo el resumen.
- **Tijuana como -REC-**: día sábado 14 por resumen en nota publicada el 15 (regla de 143: «ayer» en nota del día de apertura).
- **Rojos**: Galeana (homicidio múltiple; menores) · Tecate (privación de la libertad de cinco; agente de la FGE) · Gaviotas Sur (homicidio múltiple) · Lachigalla (víctima autoridad comunitaria) · Pueblo Nuevo (homicidio múltiple tras el segundo fallecimiento).
- **Tecate**: muertos fuera del total por contradicción «asesinados» / «no localizados».
- **Anapra**: 1 o 2 muertos por titular; se integra 1 (mínimo coincidente) y se clasifica por la cifra mínima.
- **«El Mike» (Atotonilco el Alto, 14-nov)**: hora no fijada (ventana de 150 o 151) y quién inició solo por resumen (versión de García Harfuch: recorrido de prevención, ocupantes abren fuego) → no se sube a rojo; visto. Si una fuente fija por titular el inicio por el grupo y la hora, es -REC- 🔴 de 151.
- **Edomex huachicol**: 🟢 con FRONTERA; día de los cateos no fijado; armas solo por resumen → cualitativo; detenidos por titular de medio → n/d.
- **Félix Gallardo**: muerte bajo custodia por causas médicas (comunicado de la SSP de Jalisco, por resumen): seguimiento, fuera del semáforo.
- **Día contradicho entre dos versiones anteriores a las 10:24 (Gaviotas Sur)**: ficha propia con cláusula de retiro; -REC- solo cuando la versión anterior es única (Tijuana).
- **Ninguna fiscalía** (FGE BC, FGJNL, FGE Tabasco, FGEO, FGE Puebla) publicó comunicado o declaración nombrada indexada sobre los hechos del corte: todas las fichas «SIN BOLETÍN».
- **Nombres y alias**: ningún nombre o alias de víctima o detenido en el cartelón.

## 8. Controles editoriales

| Control | Ronda | Veredicto | Correcciones aplicadas |
|---|---|---|---|
| `procedencia-cifras` | R1 (paralelo, 24 búsquedas) | CORREGIR | Galeana: heridos 1 → 2 (última cifra con titular, MVS 753613) · Tecate: titular contrario «reportan dos desaparecidos» (Poder MX) en lugar de un titular no localizado; El Congresista retirado · Gaviotas Sur: cita de El Universal mal atribuida → UnoTV, Quadratín Tabasco y El Universal («investiga FGE multihomicidio en Villahermosa») · Pueblo Nuevo: Infobae/EFE no es del hecho → El Universal; saldo de 1 muerto en el primer parte declarado · Morelia: motociclista por titular (La Voz) · Anapra: mujer herida solo por resumen; noche por resumen · Calpulalpan: cita de Quadratín Tlaxcala inexistente → Cinco Radio y Meganoticias · Edomex: «más de 15 mil» → «~15 mil» (SinEmbargo; López-Dóriga «casi 16 mil»); armas solo por resumen fuera de tarjetas; detención del 13 por resumen · Chignahuapan: «dos vehículos baleados y armas» por titular (Diario Puntual 2026/11/16) · fe de erratas de 151-002 y -003 con titulares literales |
| `editor-duplicidad` | R1 (paralelo) | CORREGIR | Seguimiento de Monterrey atado a ARG-150-REC-003 retirado (caso homónimo: secuestro frente a riña) · nombre de un medio-persona retirado de -002 · interno de alto perfil sin nombre ni cargo criminal · conclusiones 1, 3 y 5 ajustadas a lo que dicen las fichas · portada 2 y 4 (la 4 repetía la de 151) · deslindes de -005 (nombra -151-004 y -005), -009 (Otomí) · repeticiones retiradas (Buenavista, Villas del Pedregal, Cocula, Querétaro, Mazatlán) · tarjetas n/d · fe de erratas con reserva de Tijuana · archivo de equipos: «El Mike» visto, no REC. **No aplicada, con razón**: Anapra «doble homicidio» en diario.mx es la misma URL de El Diario de Juárez, no segunda fuente |

| `editor-duplicidad` | R2 (serie) | CORREGIR | Calpulalpan R 2 → 3 · conclusión 3: «agente de la FGE», no «en activo» · conclusión 4: San Andrés Niño y tequio (lo indígena, solo por resumen) · deslinde de -009 con los ARG-ID reales de huachicol · REC-001 sin hora duplicada ni deslinde de método · listas de fuentes de -002 y -008 reconciliadas con R1 |
| `procedencia-cifras` | R2 (serie, 6 búsquedas) | CORREGIR | Chignahuapan: La Silla Rota y El Heraldo de México (aportados por Centro) no reproducidos en R1 ni R2 → sustituidos por Síntesis y El Universal Puebla, verificados; N 5 → 3 · Pueblo Nuevo: El Universal, solo heridos, nombrado en el hecho. **No aplicadas, con razón**: Quadratín Tabasco (Gaviotas Sur) lo reprodujo R1 por titular; la discrepancia de Galeana es entre dos medios distintos (Enfoque Monterrey, reproducido en R1, y ENfoque Noticias); Milenio y N+ los aportó Noreste con URL y R1 reprodujo N+. Criterio: Meganoticias, regional. Sin comunicado de la FGJNL ni confirmación de muertes de la FGE BC al cierre |

Regla de criterio añadida a §7 (petición de R1): día contradicho entre dos versiones, ambas anteriores a las 10:24 del 15 (Gaviotas Sur) → ficha propia con cláusula de retiro; -REC- solo cuando la versión anterior es única (Tijuana).

## 9. Presupuesto de búsqueda

Control 2 + coordinador 18 + ola 148 (Noroeste 25, Noreste 25, Occidente 25, Centro 25, Golfo 23, Sureste 25) + `procedencia-cifras` R1 24 + R2 6 = **198** (2 sobrantes de Golfo).

## 10. Hallazgos de método (no van al cartelón)

1. **Ciclo A con prioridad**: la prioridad saldó Sinaloa (sentencias), Colima y Guerrero (armamento) y Durango (alto impacto, consulta propia tras cuatro ediciones); Campeche sigue sin dominio de fiscalía confirmado (**tercera edición**).
2. **Armamento por dominio en retroceso**: 11 de 32 (151: 15). Noroeste no hizo ninguna consulta `site:` de armamento; Golfo tampoco. Exigir en la plantilla una consulta de armamento por entidad aunque la región encabece sentencias.
3. **Día de cierre en domingo**: ocho de nueve hechos llevan FRONTERA; la serie depende del resumen del buscador para la hora de casi todo el corte.
4. **Hechos ajenos útiles**: Occidente trajo Cd. Juárez (Anapra), que Noroeste no vio. Mantener la sección de ajenos.
5. **Rotación**: Ciclo A aportó Sinaloa en sentencias (dominio con boletines de 2025-26, SRIV) y la consulta propia de Durango, sin hechos.
