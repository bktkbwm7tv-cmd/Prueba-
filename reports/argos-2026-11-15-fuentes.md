# ARGOS 151 — Archivo de fuentes (corte 2026-11-15)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 151 |
| Archivo | `reports/argos-2026-11-15.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **sáb 14-nov 10:09 → dom 15-nov 10:24 CDMX** · duración **24 h 15 min** (cálculo con `date`) |
| Calendario | sáb 14 (10:09–24:00, 13 h 51) · dom 15 (00:00–10:24, 10 h 24) |
| Hora de arranque (Bloque 0) | 10:24 CDMX · «Procede» a las 10:46 (22 min): no se ajusta el cierre |
| Consulta | última búsqueda del coordinador: 10:56 CDMX (se actualiza tras `procedencia-cifras` R2) |
| `WINDOW_DAYS` | 2 (la plantilla de 150 traía 6) |
| Ciclo | **C** (Occidente + Sureste encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Red | `curl https://www.gob.mx/fgr` → `000` (15-nov 10:24): egreso bloqueado; solo WebSearch |
| Rama | `claude/argos-151-nacional-c9xttt` (fast-forward hasta `claude/argos-150-nacional-61ng7x`, 150) |

## 2. Resultado del corte

- **8 hechos propios** (🔴 3 · 🟡 3 · 🟢 2) en 5 entidades (Ver, Pue, Chis, Sin, Son); densidad 0,33 hechos/hora (cálculo propio).
- **2 recuperaciones 🔴**: `ARG-151-REC-001` Tepehuacán de Guerrero (ventana de 150) y `ARG-151-REC-002` El Arenal, Jal. (ventana de 149).
- Muertos por agresión 7 · heridos 5 · cuerpos 4 · recuperaciones 4 muertos (cálculo propio).
- Armamento integrado: 2 largas (Mazatlán) y 1,229 cartuchos (Nogales), un titular cada uno; detenidos en aseguramiento n/d (solo titular de medio, sin cifra de autoridad).
- Sentencias integrables: 0.
- Marcas: 4 `FRONTERA DE VENTANA — HORA NO FIJADA` (-001, -003, -007, -008: publicados el sábado 14, día de cierre de 150, sin hora por fragmento) · 1 cláusula de retiro (-002 Jolalpan: día solo por resumen).
- Rojo sin ruta: Chignahuapan, Cuautelolulco (5 muertos, madrugada del 15 por resumen; MTP Noticias y El Quinto Medio 2026/11, sin día en la ruta).

## 3. Fe de erratas a ediciones anteriores

| Código | Edición | Corrección |
|---|---|---|
| `ARG-151-FE-001` | 150 | Se recupera Tepehuacán de Guerrero (🔴, ~02:00 del 14): semáforo corregido de 150 = 12 🔴 · 6 🟡 · 6 🟢 |
| `ARG-151-FE-002` | 149 | Se recupera El Arenal, Jal. (🔴, 8-nov): semáforo corregido de 149 = 11 🔴 · 7 🟡 · 7 🟢 |
| `ARG-151-FE-003` | 150 | `ARG-150-004` Tuxpan: día del ataque = jueves 12-nov (MVS, Diario de Yucatán, El Mañana 2026/11/12) |
| `ARG-151-FE-004` | 150 | `ARG-150-002` Tepalcatepec: heridos = 2 (La Jornada 2026/11/11; Síntesis 2026/11/12); «tres» (Posta) preliminar |
| `ARG-151-FE-005` | 150 | `ARG-150-003` Ocotlán: Defensa por titular de medio (Infobae 2026/11/13); El Financiero 2026/11/12 |
| `ARG-151-FE-006` | 150 | `ARG-150-020` Silao: «13 armas», segundo titular fechado (Latinus 2026/11/13) |
| `ARG-151-FE-007` | 150 | `ARG-150-016` Tlalnepantla: herido con segundo titular (La Jornada Estado de México, sin fecha en ruta) |
| `ARG-151-FE-008` | 150 | `ARG-150-REC-001` Tecate: la nota de Uniradio («cuatro detenidos… taquería de Tecate») es el ataque del 4-jul-2026 (La Jornada, Punto Norte, El Financiero 2026/07/07): se retira |
| `ARG-151-FE-009` | 150 | `ARG-150-REC-002` Cacahuatepec: ningún detenido publicado; se retira «1 detenido según un solo medio» |
| `ARG-151-FE-010` | 150 | Rojos sin ruta retirados: Viesca, Reynosa Puerta Sur (tercera edición sin ruta con día); Colima (junio de 2025, Infobae 2025/06/22); Atotonilco el Alto (🟡 bloqueo aislado, Diario Puntual 2026/11/13, ventana de 150) |
| — | 149 | `ARG-149-ARM-003` Sanalona: «seis armas, mil 260 cartuchos», por titular (Meganoticias 786916); desglose 3 largas + 3 cortas y 50 cargadores solo por resumen. **No se corrige el total de 149 en el cartelón**: pendiente de validación del texto del agregado federal (ver `_pendientes.md`) |

## 4. Boletín federal (triple consulta)

| Momento | Día suelto | Rango | Título sin `site:` | Resultado |
|---|---|---|---|---|
| Inicio | «13 de noviembre» | «13, 14 y 15 de noviembre» | «informa acciones relevantes del 13 de noviembre de 2026» · «del 14 de noviembre» | SRIV; último indexado: acciones del 12-nov (Milenio, SICOM, RED113, Tallapolítica, Ultranoticias, Certeza, Consulta Monterrey) |
| Cierre | «"13 de noviembre de 2026"» | «13 y 14 de noviembre» | «14 de noviembre … Milenio» | SRIV |

Fin de semana: el boletín del 13 al 15 puede salir agregado el lunes 16. Las acciones del 13 son de la ventana de 150.

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| Cláusula `-150-011` San Juan del Río | Sin novedad: rutas del 10 (Expreso; Al Minuto); ninguna evidencia del 9: cláusula sigue abierta |
| Frontera `-150-017` Tijuana | Hora no fijada (El Imparcial, Periodismo Negro 2026/11/14): se mantiene en 150 con su marca |
| `-150-004` Tuxpan | Día = 12 (FE-003); segunda víctima: publicación 13, fecha de la muerte no fijada; situación jurídica de detenidos y marino: no publicada |
| `-150-005` Juchitán | Jueves 12 por convergencia de resúmenes; sin ruta con día del hecho: sigue `DÍA CONTRADICHO` |
| `-150-006` San José del Rincón | Día 10 (resumen) u 11; lugar cabecera o Sabaneta: sin cambio |
| `-150-003/-018` Ocotlán | FE-005; heridos 2 por titular (Extraoficial); armamento sin cifra por titular |
| `-150-012/-020` Silao | FE-006; día 13 por rutas (resumen «madrugada de este viernes»): sigue contradicho; GN muerto «días antes»: sin nota propia |
| `-150-013` Temascatío | Sin declaración nombrada; 🟡 con reserva |
| `-150-010` Las Víboras | Cantidad no publicada; sin segunda ruta |
| `-150-016` Tlalnepantla | FE-007; duplicidad con -015: no descartada (otras víctimas por titular) |
| REC de 150 | FE-008 (Tecate), FE-009 (Cacahuatepec); Monterrey: 2 detenidos solo por medios (ABC 2026/11/8; Milenio) |
| Rojos sin ruta de 150 | FE-010; El Arenal → `ARG-151-REC-002` |
| Cláusulas 149 | `-015` Atempan: 6-nov por resumen, publicación 8-nov (Infobae) · `-016` Buenavista: no consultado · `-020/-021`: sin día · `-013` Cosoleacaque: «~08:00» por resumen · `-019` Acapulco: hora no fijada |
| Reservas 149 | `-005` Río Bravo: sin novedad · `-006` Mazatlán: superficie (Línea Directa) vs fosa (La Silla Rota) · `-014` Zapopan: sin declaración |
| Cláusulas 148 | `-007` Morelia: día sin fijar |
| Sentencias candidatas | Veracruz 88 (pub. 13), Monterrey 25 a 10 m (pub. 13), Tabasco 5119 (9-nov por listado): ventana de 150, sin boletín leído |
| Seguimientos | «El Panda»: sin audiencia nueva · Zapopan R2: 15 liberados y 5 imputados (N+) · Cuernavaca: detenido relacionado, boletín del 11-nov (resumen) · Matamoros: sin detenidos · Mexicali: sin cifra nueva · Tuxpan -019: no consta |

## 6. Fuentes por ficha (lista íntegra)

- **ARG-151-001 Texhuacán**: Informador (20261114) · Golpe Político (2026/11/14) · El Independiente (2026/11/14) · Infobae (2026/11/15) · El Universal · Excélsior · Reforma · Aristegui · Quadratín · Meganoticias 788813 · Plaza de Armas · ADN Sureste («19:19 h») · El Siglo de Torreón · El Coahuilense.
- **ARG-151-002 Jolalpan**: Intolerancia Diario (2026/11/15) · El Quinto Medio (2026/11) · Diario de Morelos · El Universal Puebla (dos notas) · López Dóriga · Milenio · La Jornada de Oriente · La Unión Morelos · MTP Noticias · Curul · Diario sin Secretos · Crónica Regional · Mediatik · Municipios Puebla («4 muertos», no se integra) · Periódico Central («Los Michoacanos», NO OFICIAL).
- **ARG-151-003 Carretera 190**: La Jornada (2026/11/14) · Infobae (2026/11/15) · Diario.mx (2026/nov/15) · El Imparcial (2026/11/15) · Zolo (2026/11/15) · Quadratín Oaxaca (dos notas, sin fecha) · Milenio · ADN Sureste («10:35 h»).
- **ARG-151-004 Mazatlán bar**: Luz Noticias (2026-11-15) · Línea Directa (2026-11-15) · Noroeste · El Universal (jornada, recuento) · La Prensa de Coahuila (2026/11/15, republicación).
- **ARG-151-005 Mazatlán 12 de Mayo**: Luz Noticias (2026-11-15) · Los Noticieristas (2026/11) · Noroeste · Sinaloahoy.
- **ARG-151-006 Culiacán**: Luz Noticias (2026-11-15) · Noroeste · Viva la Noticia · Café Negro.
- **ARG-151-007 Nogales**: El Imparcial (2026/11/14).
- **ARG-151-008 Mazatlán Ejército**: Luz Noticias (2026-11-14).
- **ARG-151-REC-001 Tepehuacán**: Proceso (2026/11/14, dos notas) · Heraldo de México (2026/11/14) · Tribuna (2026/11/14) · La Silla Rota (2026/11/14) · Infobae (2026/11/14) · La Jornada (2026/11/15) · Politico.mx (2026/11/15) · Central Municipal (2026/11/15) · El Universal (dos notas) · Milenio · Excélsior · Quadratín Hidalgo · La Jornada Hidalgo · El Porvenir · Julio Astillero.
- **ARG-151-REC-002 El Arenal**: Crónica Jalisco (2026/11/09) · Milenio.

## 7. Procedencia: decisiones de clasificación

- **Texhuacán como hecho del corte** (y no «rojo sin ruta», como propuso Golfo): el día tiene tres rutas del 14; la hora (~14:20) es solo por resumen, por lo que lleva `FRONTERA DE VENTANA`.
- **Jolalpan**: ruta solo del 15; día 14 por resumen → cláusula de retiro si resulta anterior a las 10:09 del 14. 🔴 por muerte de personal, con independencia de quién inició.
- **Carretera 190**: entidad Chiapas por titular (Quadratín: «…hallazgo de 4 cuerpos en Chiapas»; Infobae); 🔴 por cuerpos hallados de víctimas privadas de la libertad.
- **Mazatlán 12 de Mayo**: 🟡, mismo criterio que ARG-140-011 (1 muerto y 3 heridos).
- **Nogales y Mazatlán Ejército**: 🟢; detenidos solo por titular de medio → n/d en el conteo (regla de 146: cifra de autoridad).
- **Tepehuacán como -REC-** y no hecho del corte: la hora ~02:00 es convergente en los resúmenes y el primer titular («un policía muerto y otro herido», Proceso 2026/11/14) describe el primer parte de la madrugada; si apareciera hora posterior a las 10:09, pasa a 151.
- **Atotonilco el Alto**: dos camiones incendiados tras el enfrentamiento de Ocotlán = bloqueo aislado 🟡, no quema masiva; Harfuch descarta narcobloqueos por titular. No se recupera.
- **Chignahuapan**: dos titulares con 5 muertos, ninguno con día en la ruta y sin autoridad: rojo sin ruta.
- **Nombres**: ningún nombre de víctima o detenido; el alias de un detenido de Colima se omitió.

## 8. Controles editoriales

_Se completa tras las rondas R1 (paralelo) y R2 (serie)._

## 9. Presupuesto de búsqueda

Control 2 + coordinador 18 + ola 150 (6 × 25) + `procedencia-cifras` R1 _n_ + R2 _n_ = _total_ (se completa al cierre).

## 10. Hallazgos de método (no van al cartelón)

1. **Equipos que entregan como «rojo sin ruta» un hecho con día por ruta y sin hora** (Golfo: Texhuacán): la plantilla debe distinguir «sin ruta con día» de «sin hora».
2. **Señuelo de homónimo de topónimo**: «Tepehuacán de Guerrero» (Hgo.) apareció en búsquedas del Sureste por «Guerrero»; tres equipos lo pasaron como ajeno.
3. **Fuente de una REC contaminada por un hecho de otro mes** (Tecate, Uniradio, julio): antes de citar una nota sin fecha en una -REC-, fijar su mes.
4. **Ciclo C**: la rotación saldó 8 de las 10 fiscalías `NO REVISADA` y 11 de las 13 entidades de armamento `NO REVISADA`; quedan Sin y Camp (sentencias), Col y Gro (armamento).
5. **Durango**: cuarta edición sin consulta propia de ataques (solo amplia): encabezar el alto impacto de 152.
