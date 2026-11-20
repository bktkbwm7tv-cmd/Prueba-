# ARGOS 155 — Archivo de fuentes (corte 2026-11-19)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 155 |
| Archivo | `reports/argos-2026-11-19.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **mié 18-nov 12:32 → jue 19-nov 18:40 CDMX** · duración **30 h 08 min** (cálculo con `date`) |
| Calendario | mié 18 (12:32–23:59, 11 h 28) · jue 19 (00:00–18:40, 18 h 40) |
| Hora de arranque (Bloque 0) | 18:40 CDMX · «Procede» a las 18:42 (2 min): no se ajusta el cierre |
| Consulta | última búsqueda: 19:06 CDMX (cierre de `procedencia-cifras` R2) |
| `WINDOW_DAYS` | 2 (la plantilla de 154 ya traía 2: sin reemplazo; aserción `WINDOW_DAYS = 2;` única) |
| Ciclo | **A** (Noroeste + Centro encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Red | `curl https://www.gob.mx/fgr` → `000` (19-nov 18:40): egreso bloqueado; solo WebSearch |
| Rama | `claude/argos-154-security-report-etkefe` (el clon arrancó en `e19b060`, estado de 143; las dieciséis fusiones de la orden, fast-forward hasta `claude/argos-154-criminal-intelligence-g2kqhw`) |

## 2. Resultado del corte

- **13 hechos propios** (🔴 1 · 🟡 7 · 🟢 5) en 10 entidades (Mich, Sin, Gto, Tlax, Camp, Pue, Gro, Hgo, QRoo, Chih); densidad 0,43 hechos/hora; 0,03 rojos/hora (cálculo propio).
- **Ninguna recuperación** de ventanas anteriores (Mazatlán explosivos del 17, Valle de las Palmas, Silao: vistos, sin hora por titular).
- Muertos por agresión 9 · heridos 1 · cuerpos 0 · detenidos sin cifra de autoridad citable: Tepeaca 7, Chihuahua 2, Ometepec 1, Tepehuacán 4 acumulados, Cancún 6, Irapuato 1 (no se suman).
- Armamento integrado: 5 armas largas (Tepeaca, `ARG-155-ARM-001`, Bajo) · 1 arma sin categoría (Chihuahua, `ARG-155-ARM-002`, Bajo). Sentencias integrables: 0.
- Marcas: 4 `PUBLICADO EL DÍA DE APERTURA SIN HORA` (-006, -007, -009, -010) · 9 `FRONTERA DE VENTANA — HORA NO FIJADA` (-001, -002, -003, -004, -005, -008, -011, -012, -013) · 3 cláusulas de retiro (-006 León: día contradicho; -009 Tepeaca: «mañana» por resumen; -011 Tepehuacán: capturas del 17 o 18).
- Criterio aplicado a las detenciones de casos anteriores (Tepehuacán, Cancún, Ometepec): ficha 🟢 propia en la ventana de la detención, sin recalificar el delito de origen (precedente: ARG-146-017, ARG-150-021, ARG-154-011). Editor R1 señaló que, bajo una lectura estricta de «desarrollo», serían seguimientos; se mantiene el criterio del archivo.

## 3. Fe de erratas a ediciones anteriores (códigos solo aquí y en el índice)

| Código | Edición | Corrección |
|---|---|---|
| `ARG-155-FE-001` | 153 | `ARG-153-001` Santiago Maravatío: «Falleció el tercer policía de Santiago Maravatío tras la emboscada del 17 de noviembre» (La Silla Rota 2026/11/19, titular) · muertos de 153: 8 → 9; heridos de la ficha 1 → 0 (supone que el herido era el policía fallecido; cálculo propio) |
| `ARG-155-FE-002` | 154 | `ARG-154-011` Zapopan: 8 detenidos, saldo posterior por titular (Meganoticias «Suman ocho detenidos…»; NX Noticias «Sube a ocho…»; Infobae 2026/11/18), frente a 3 en el primer parte (Plaza Juárez); armas cortas 6 (154) u 8 (boletín del 18), solo por resumen, no integradas |

No va al cartelón como fe de erratas: **Tecate `ARG-150-REC-001`**. El equipo Noroeste propuso 3 → 4 muertos («cuádruple homicidio», En Línea BC 2026/11/16; N+); `editor-duplicidad` R1 lo detuvo: los titulares no traen dos campos individualizadores (Los Encinos no está en el titular del 16) y R1 de procedencia halló lugar y hora contradichos (Punto Norte ~22:30, Dr. Arturo Guerra y Av. Nuevo León; FGE BC ~20:20, Andador del Río). Queda en seguimiento como `POSIBLE MISMO CASO`.

## 4. Boletín federal (triple consulta)

| Momento | Día suelto | Rango | Título sin `site:` | Resultado |
|---|---|---|---|---|
| Inicio | «Gabinete de Seguridad informa acciones relevantes "18 de noviembre de 2026"» | «acciones relevantes "17 y 18 de noviembre" 2026» | «"informa acciones relevantes" "17 de noviembre de 2026"» | **Acciones del 17 y del 18: boletines diarios indexados en `gob.mx/sspc`** por título (contenido solo por resumen) y republicadores (Red Metropolitana 2026/11/18; Ultranoticias; RED113; Tallapolítica). Del 18: Yuriria, Zapopan (8 detenidos, 8 cortas), Culiacán El Vino, Huajicori, Monterrey, Ometepec, Tepeaca, por resumen. Del 17: Hidalgo (Tamps), Mexicali, Acaponeta, La Yesca (lanzagranadas), Culiacán, Acapulco |
| Cierre | «"informa acciones relevantes del 19 de noviembre de 2026"» | «acciones relevantes "13, 14 y 15 de noviembre" 2026» | «"informa acciones relevantes del 15 de noviembre de 2026"» | 19: SRIV · 13, 14 y 15: SRIV (gabinetedeseguridad.gob.mx lista comunicados conjuntos sueltos del 13, 14 y 15 por resumen); último diario en ese tramo: 12-nov |

Un agregado no fija el día ni la hora de cada acción: Tepeaca y Ometepec entran con marca de apertura; Yuriria, Huajicori y Monterrey, a vistos (sin nota con día y hora).

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| Ciclo | A, tras la prioridad (armamento: 21 de 32 por dominio, Gto, Col y NL saldadas; sentencias: 24 de 32, BCS, Coah, Zac, Qro saldadas; Son sin dominio; alto impacto: consulta propia en 20, BCS saldada) |
| Cláusulas de 154 | -005 Mazatlán: ~11:30/~11:45 solo por resumen; abierta · -008 Río Bravo: «martes 17» por resumen; abierta |
| Reservas de 154 | -002: noche del 17 por resumen (~21:30/~23:00); «tercer» aspirante por titular (Quinto Poder) · -004 Chalco: sin tercer muerto por titular; heridos sin resolver · -007: sin réplicas; vehículos 3 o 4 · -008: víctimas no informadas; colectivos piden levantamiento · -011: 8 detenidos (FE-002) |
| Acámbaro | Fecha del hecho sin fijar (17-oct por resumen de Milenio, 18-nov por resumen de Rotativo): no se reintegra |
| Cláusulas de 153 y 152 | Ninguna hora por titular (Azcapotzalco, Acaponeta, Tecate, Gaviotas Sur, Lachigalla, Pueblo Nuevo) |
| Huitzilac / Yautepec | 38 hallazgos del 9 al 13-nov, sin desglose por día: visto · Yautepec sin cambio |
| Tecate «cuádruple» | Posible mismo caso; saldo no corregido (§3) |
| Sentencias candidatas | Sin boletín: Monterrey, Tabasco 5119, Veracruz 88, Champotón, Copanatoyac · nuevas: Iguala (Avispones, 60 años al exalcalde), Oaxaca (boletín 2,993, fecha), Villahermosa (feminicidio, 45 años, índice FGET) |
| Seguimientos | Zapopan -154-011 (FE-002); vinculación sin novedad · Cajeme: sin vinculación · Cuernavaca: sin novedad · Texhuacán: sin detenidos · Tepehuacán: 4 detenidos (ficha -011) · Mexicali: sin consulta (tercera edición) |

## 6. Fuentes por ficha (lista íntegra)

- **ARG-155-001 Uruapan**: Media News (2026/11/19) · Grupo Marmor (2026/11/19) · A Tiempo · Respuesta Michoacán · IMN · RED113 (2026/11). Quadratín («Ataque armado en la Rubén Jaramillo…»): posible homónimo de septiembre, no se cita.
- **ARG-155-002 Culiacán**: Luz Noticias (2026-11-19) · Quadratín Sinaloa · Meganoticias · Sinaloahoy · Café Negro.
- **ARG-155-003 Mazatlán**: Línea Directa (2026-11-19) · Noroeste · Quadratín Sinaloa · Meganoticias · Reporte18. Luz Noticias (2026-11-19): no reproducida en R2, retirada de las fechadas.
- **ARG-155-004 Irapuato**: AM (2026/11/19) · Correo (2026/nov/19) · Guanajuato Informa.
- **ARG-155-005 Morelia**: Changoonga (2026/11/19; ruta con nombre propio) · Quadratín · El Congresista · A Tiempo · Contramuro · MoreliActiva · RED113 · La Voz de Michoacán.
- **ARG-155-006 León**: Correo (2026/nov/18) · Noticieros en Línea (2026/nov/19; «noche del martes» por resumen) · Milenio · Noticias Vespertinas.
- **ARG-155-007 Ocotlán, Tlax.**: Gentetlx (2026/11/18) · La Prensa de Tlaxcala (2026/11, dos notas) · 385grados · Meganoticias · UnoTV · N+ · Periódico Enfoque · Cinco Radio.
- **ARG-155-008 Ciudad del Carmen**: PorEsto (2026/11/19) · La i Noticias · Tribuna Campeche (comunicado de la SPSC, por resumen) · La Revista Peninsular.
- **ARG-155-009 Tepeaca**: boletín federal del 18 (gob.mx/sspc; contenido por resumen) · Infobae (2026/11/19) · Intolerancia (2026/11/19) · La Jornada de Oriente · La Nigua · Curul Puebla · Controversia Puebla · SICOM · Milenio · El Universal Puebla · Urbano · Telediario · Hipócrita Lector.
- **ARG-155-010 Ometepec**: boletín federal del 18 · La Silla Rota (2026/11/19) · Proceso (2026/11/19) · La Jornada (2026/11/19) · Infobae (2026/11/19) · Cinco Radio · La Nigua · Ámbito · El Sur (Defensa).
- **ARG-155-011 Tepehuacán**: Síntesis (2026/11/19) · La Silla Rota (2026/11/19, dos notas; slug «confirma-gabinete-de-seguridad-que-robo-motivo…») · Zunoticia (2026/11/19) · Infobae (2026/11/19) · Milenio · La Jornada Hidalgo · El Universal Hidalgo.
- **ARG-155-012 Cancún**: Noticaribe (2026/11/19) · Sol Quintana Roo · Marcrix.
- **ARG-155-013 Chihuahua**: Al Instante Chihuahua (2026/11/19) · El Diario de Chihuahua (2026/nov/19) · Entre Líneas · N+ · Tiempo · NetNoticias · Tierra Fuerte.

## 7. Procedencia: decisiones de clasificación

- **Rojo**: Uruapan (homicidio múltiple). Ninguna otra pista roja con día por ruta o titular: Coyuca de Benítez (sin ruta), Mazatlán explosivos (17 por resumen, sin ruta), Valle de las Palmas («martes 16» incoherente).
- **Uruapan**: rutas del 19 (Media News, Grupo Marmor); hora poco antes de las 14:00 por resumen, dentro de la ventana en cualquier caso; marca de frontera por publicarse el día de cierre.
- **Tepeaca**: día por el título del boletín federal (acciones del 18); «mañana de este miércoles» por resumen → cláusula de retiro (si es anterior a las 12:32 del 18, es de 154, verde: no admite `-REC-`).
- **León**: Correo (ruta del 18) sitúa el hecho el miércoles por resumen; Noticieros en Línea, la noche del martes por resumen → día contradicho y cláusula de retiro.
- **Cancún y Chihuahua**: la ruta del 19 fecha la publicación; la detención es del 18 por resumen (R1 de procedencia).
- **Ciudad del Carmen y León**: dejaron de ser «fuente única» tras R1 (otras notas sin fecha verificada); se quedan en ★★☆☆☆.
- **Armamento**: Tepeaca 5 largas por tres titulares sin fecha en la ruta (R2); Chihuahua 1 arma sin categoría por dos titulares (Al Instante 2026/11/19; El Diario de Chihuahua 2026/nov/19). Ometepec, Yuriria, Huajicori, Monterrey: cifras solo por resumen del boletín → vistos.
- **Iguala (Avispones)**: sentencia de juez federal publicada en la ventana por medios nacionales con ruta del 19; sin comunicado oficial → `PENDIENTE DE CONFIRMACIÓN OFICIAL` (umbral asimétrico de sentencias).

## 8. Controles editoriales

| Control | Ronda | Veredicto | Correcciones aplicadas |
|---|---|---|---|
| `procedencia-cifras` | R1 (paralelo, 24 búsquedas) | CORREGIR | Uruapan sin Quadratín (homónimo), con Grupo Marmor · Tepeaca: «cinco» por un titular · Cancún y Chihuahua: detención del 18 por resumen · León: día contradicho; Milenio · Carmen: sin «fuente única» · Morelia ~06:30 o ~07:00 · Ocotlán ~19:30; N+ · Ometepec: corporación contradicha (Defensa) · Tepehuacán: Gabinete por slug · Zapopan: Infobae 2026/11/18 · Iguala: 60 años al exalcalde |
| `editor-duplicidad` | R1 (paralelo) | CORREGIR | Deslindes de -003 (ARG-145-008), -004 (ARG-136-003, ARG-146-006), -009 (ARG-121-004) · FE de Tecate retirada · Zapopan armas 6/8 · Chihuahua a armamento (ARM-002) · Irapuato en detenidos no sumados · Tepehuacán condicional · marca de apertura en Tepeaca · portada 5 y conclusión 2 distintas · Valoración 3 y 4 reescritas · heridos de 153 · expolicía de Tlaxcala (ARG-125-028) · seguimiento en el panel de -011 y -012 · fila «sin novedad» compactada |
| `editor-duplicidad` | R2 (serie) | PUBLICAR | Menores aplicados: portada 1 y conclusión 1 sin vínculo presupuesto; conclusión 5 con reserva de armas largas; frase de apertura en -009; «Los Rusos» en el deslinde de -010 |
| `procedencia-cifras` | R2 (serie, 4 de 6 búsquedas) | PUBLICAR | Mazatlán: Línea Directa y Noroeste en lugar de Luz Noticias · Tepeaca: tres titulares con «cinco armas largas» (La Nigua, Curul Puebla); 22 cargadores por un titular, no integrados · supuesto del 1 → 0 de heridos declarado |

## 9. Presupuesto de búsqueda

Control 2 + coordinador 18 + ola 150 (6 × 25) + `procedencia-cifras` R1 24 + R2 4 = **198** (de 200).

## 10. Hallazgos de método (no van al cartelón)

1. **Boletín federal reindexado**: el diario del 17 y el del 18 aparecieron en `gob.mx/sspc` por título; la triple consulta los alcanzó al primer intento. El tramo 13-15 sigue sin diario.
2. **Fecha de publicación frente a fecha de la detención**: tres verdes llegaron fechados por la ruta del 19 cuando la detención era del 18 (por resumen).
3. **Deslindes «no figura»**: dos falsos en R1; acotar el rango o citar el ARG-ID.
4. **Rotación, ciclo A**: Noroeste y Centro revisaron 11 fiscalías (SRIV); la rotación no aportó sentencia integrable; la candidata más relevante (Iguala) es federal y llegó por medios.
5. **Centro sin armamento por dominio en seis entidades**: el triaje judicial consumió el tope del equipo.
