# ARGOS 153 — Archivo de fuentes (corte 2026-11-17)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 153 |
| Archivo | `reports/argos-2026-11-17.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **lun 16-nov 10:30 → mar 17-nov 11:34 CDMX** · duración **25 h 04 min** (cálculo con `date`) |
| Calendario | lun 16 (10:30–24:00, 13 h 30) · mar 17 (00:00–11:34, 11 h 34) |
| Hora de arranque (Bloque 0) | 11:34 CDMX · «Procede» a las 13:09 (1 h 35 min, dentro del margen de dos horas): no se ajusta el cierre |
| Consulta | última búsqueda: __CONSULTA__ CDMX (cierre de `procedencia-cifras` R2) |
| `WINDOW_DAYS` | 2 (la plantilla de 152 ya traía 2: sin reemplazo; aserción `WINDOW_DAYS = 2;` única) |
| Ciclo | **B** (Noreste + Golfo encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Red | `curl https://www.gob.mx/fgr` → `000` (17-nov 11:34): egreso bloqueado; solo WebSearch |
| Rama | `claude/argos-153-criminal-intelligence-6knrt6` (fast-forward hasta `claude/argos-152-nacional-reqwch`, 152); el clon arrancó en `e19b060` (estado de 143/144) |

## 2. Resultado del corte

- **8 hechos propios** (🔴 4 · 🟡 3 · 🟢 1) en 7 entidades (Gto, Nay, CDMX, Chih, Sin, Tamps, Mich); densidad 0,32 hechos/hora; 0,16 rojos/hora (cálculo propio).
- **Ninguna recuperación** de ventanas anteriores (Yautepec y Atotonilco el Alto, vistos: ver §7).
- Muertos por agresión 7 · heridos 7 · cuerpos sin causa informada 7 (Acaponeta) · detenidos 1 o 2, contradicho (Ciudad Victoria), sin cifra de autoridad.
- Armamento integrado: ninguno. Sentencias integrables: 0.
- Marcas: 5 `PUBLICADO EL DÍA DE APERTURA SIN HORA` (-002, -003, -004, -006, -008) · 1 `FRONTERA DE VENTANA — HORA NO FIJADA` (-001, publicado el día de cierre) · 2 cláusulas de retiro (-003 Azcapotzalco: todos los resúmenes apuntan a antes de las 10:30; -002 Acaponeta: mañana o tarde, contradicho).

## 3. Fe de erratas a ediciones anteriores (códigos solo aquí y en el índice)

| Código | Edición | Corrección |
|---|---|---|
| `ARG-153-FE-001` | 152 | `ARG-152-002` Tecate: dos víctimas halladas sin vida (Tribuna 2026/11/16, titular); tres con vida (resumen); hallazgo ~02:00 del 16 (resumen) · `ARG-152-007` Anapra: 2 muertos (El Diario de Chihuahua 2026/nov/16, titular), conserva 🟡 sin recalificación · muertos de 152: 12 → 15 |
| `ARG-153-FE-002` | 152 | Precisión a `ARG-152-FE-002` (Jolalpan, `ARG-151-002`): el «4» es por titular (Diario Cambio), ya presente en la ficha de 151; se mantienen 2. **No publicada en el cartelón** (sin efecto en cifras) |

No van al cartelón (información sin efecto en cifras): `ARG-152-009`: cateos de la madrugada del 13 (resumen): de confirmarse, evento anterior publicado durante el corte · `ARG-152-008` Calpulalpan, ~17:30 del 15 (Quadratín Tlaxcala, resumen; su titular existe, contra lo anotado en 152) · `ARG-152-004` Lachigalla: día 15 por dos rutas; ~07:00 sigue solo por resumen: cláusula viva · `ARG-152-005` Pueblo Nuevo: ~00:40 sin titular: cláusula viva · `ARG-152-003` Gaviotas Sur: hora sin titular: cláusula viva · `ARG-152-REC-002` Tijuana: sábado 14 por resumen (Periodismo Negro 2026/11/15): sin cambio · `ARG-150-005` Juchitán: jueves 12 (Latinus 2026/11/13) · `ARG-149-019` Acapulco: 9-nov por cuatro rutas · `ARG-150-012` Silao: rutas del 13; noche del 12 por resumen · `ARG-150-013` Temascatío: quién inició, sin arbitrar.

## 4. Boletín federal (triple consulta)

| Momento | Día suelto | Rango | Título sin `site:` | Resultado |
|---|---|---|---|---|
| Inicio | «"16 de noviembre" 2026 detenidos armas» | «13, 14, 15 y 16 de noviembre» (solo 2025) · «13, 14 y 15 de noviembre de 2026» | «informa acciones relevantes "15 de noviembre de 2026"» | SRIV para el 13, 14 y 15; Milenio «Gabinete de seguridad: resultados 16 de noviembre» (ruta 2026): agregado sin día por acción (Ensenada, Tlacotepec, Arteaga, Culiacán) |
| Cierre | «acciones relevantes "17 de noviembre" 2026» | «del 13 al 16 de noviembre de 2026» | «informa acciones relevantes "16 de noviembre de 2026"» | SRIV; último boletín diario indexado: acciones del 12-nov |

Tercer día hábil sin agregado del fin de semana del 13 al 15: pasa a 154.

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| Ciclo | B, tras la prioridad (armamento: 31 de 32 por dominio; sentencias: 17 de 32; alto impacto: consulta propia en 21, las nueve «solo amplia» de 152 incluidas) |
| Cláusulas de 152 | `-002` Tecate, `-003` Gaviotas Sur, `-004` Lachigalla, `-005` Pueblo Nuevo: ninguna hora por titular; siguen abiertas |
| Reservas de 152 | `-001` Galeana: heridos 3 → 2 → «otro menor» (Infobae 2026/11/17); sin declaración nombrada de la FGJNL; sin detenidos; arsenal (14 largas, .50, ametralladora) solo por resumen, día no fijado · `-002` Tecate: dos asesinados, tres con vida (FE-001) · `-003`: cartulina sin peritaje; Buenavista domingo 15 por ruta (Proceso) · `-006` Morelia: titulares coherentes («motociclista armado mata a un adulto mayor…», Medianews 2026/11/15; RED Michoacán y Grupo Marmor 2026/11/16): la «mecánica contradicha» de 152 no se sostiene · `-007` Anapra: 2 (FE-001) · `-009` Edomex: madrugada del 13 por resumen; inventario (15,750 l, 14 tractocamiones, 4 cortas) solo por resumen |
| REC de 152 | Chignahuapan: sin segunda hora por titular · Tijuana La Postal: sábado 14 por resumen |
| «El Mike» | Infobae 2026/11/15: «…tras agresión a elementos federales», por titular; día 14 por ruta (Tribuna, La Jornada); ~15:55 y patrullaje solo por resumen → la orden exige hora y patrullaje por titular: **visto 🟡**, tercera edición; retirar en 154 si sigue sin ancla |
| Cajeme | Día del ataque no fijado (10-nov por resumen); Heraldo, Proyecto Puente, Infoson 2026/11/13: visto; posible omisión de 150 sigue abierta |
| Boletín federal | §4 |
| Sentencias candidatas | Monterrey Bella Vista y Monterrey 25 años (MVS 2026/11/17): posible mismo caso; sin boletín · Tabasco 5119 (pederastia, 9-nov): URL individual no identificada · Veracruz 88: sin boletín · Champotón: reparación 7.2 o 7 mdp contradicha · Campeche: dominio de la fiscalía no confirmado (cuarta edición); vía posible `ucs.campeche.gob.mx/category/fge/` |
| Seguimientos | Cuernavaca: audiencia iniciada (UnoTV sin fecha) · Zapopan: 20 vinculados (Formato 7 2026/11/16) · Texhuacán: sin detenidos · Tepehuacán: tres identificados · Tuxpan: 3 → 4 detenidos · «El Panda»: vinculado 10-nov (cerrado) · Mexicali: sin novedad en ventana · Tecate Los Encinos: posible caso homónimo |

## 6. Fuentes por ficha (lista íntegra)

- **ARG-153-001 Santiago Maravatío**: Noticieros en Línea (2026/nov/17) · Telediario · Notus · ContrapuntoNews · Agoragto («fallecen dos policías…», sin fecha: no integrado).
- **ARG-153-002 Acaponeta**: MVS (2026/11/16) · NTV (2026/11/16) · Infobae (2026/11/17) · La Razón (2026/11/17) · RED Michoacán (2026/11/17) · Potosinoticias (2026/11/17) · Aristegui (1711) · Entre Líneas · La Unión · Tribuna de la Bahía · NNC · Meganoticias · Blog del Narco (NO OFICIAL). Número de comunicado «044/2026»: no localizado por R1, retirado.
- **ARG-153-003 Azcapotzalco**: El Universal · TV Azteca · N+ (titular de formato «hoy», no localizado por R1: retirado como fuente del día) · Diario Basta (2026/11/17) · Candelero · Diario de México · Consulta Monterrey · Telediario.
- **ARG-153-004 Anapra**: El Diario de Chihuahua (2026/nov/16) · El Bordo (20261116) · Puente Libre (17-nov-2026, slug) · La Parada (2026/11) · Somos Juárez (~18:00, resumen).
- **ARG-153-005 Los Magueyes**: Luz Noticias (2026-11-17) · Línea Directa (2026-11-17) · Reporte18 · Meganoticias (~23:30, resumen).
- **ARG-153-006 / -008 Ciudad Victoria**: ABC Noticias (2026/11/16) · MVS (2026/11/16) · La Región (2026/11/16) · Potosinoticias (2026/11/16) · Infobae (2026/11/17) · El Universal · Milenio · Excélsior · Notigape · El Mañana · El Mercurio de Tamaulipas · Hoy Tamaulipas · Vocería de Seguridad de Tamaulipas (mensaje republicado en locurascuerdas.mx) · Blog del Narco (NO OFICIAL).
- **ARG-153-007 Zamora**: Grupo Marmor (2026/11/16) · Videa TV · La Voz de Michoacán · RED113 · Respuesta.

## 7. Procedencia: decisiones de clasificación

- **Rojos**: Santiago Maravatío (víctima autoridad; fuera de servicio no mueve el color) · Acaponeta (hallazgo de restos humanos; 7 cuerpos aparte de los muertos por agresión) · Azcapotzalco y Anapra (homicidio múltiple).
- **Azcapotzalco**: día y hora solo por resumen, todos antes de las 10:30 → ficha propia con cláusula de retiro (regla de la orden: con hora solo por resumen, no -REC-).
- **Acaponeta**: hora contradicha (mañana o tarde) → cláusula de retiro.
- **Ciudad Victoria**: operativo (🟡) y detención (🟢) en dos fichas; detenidos 1 o 2 contradicho; identidad no confirmada; alias fuera.
- **Tecate**: el hallazgo de los cuerpos es desarrollo de `ARG-152-002`, no hecho nuevo (FE-001).
- **Yautepec** (2 muertos, riña en cabalgata, sábado 14): 🔴, pero día y hora solo por resumen y el 14 se reparte entre 150 y 151 a las 10:09: ventana de origen no determinable → visto, no -REC- (decisión del coordinador frente a la recomendación de duplicidad R1, que proponía -REC- por el precedente de Tijuana).
- **Cosoleacaque**: posible duplicidad con `ARG-149-013`.
- **Chilapa**: fuente única, día solo por resumen → visto.
- **Ninguna fiscalía** publicó comunicado leído; la Fiscalía de Nayarit y la Vocería de Tamaulipas cuentan como institucionales solo por titular de medio o republicación.

## 8. Controles editoriales

| Control | Ronda | Veredicto | Correcciones aplicadas |
|---|---|---|---|
| `procedencia-cifras` | R1 (paralelo, 24 búsquedas) | CORREGIR | El Diario de Chihuahua: titular corregido y ruta nov/16 (no 17) · Anapra tercer homicidio: «queman vivo…» (Puente Libre), no «baleado y vivienda incendiada» · Acaponeta: hora contradicha, cláusula de retiro, semanas contradichas (Infobae, Entre Líneas, resumen), comunicado 044/2026 retirado · Azcapotzalco: N+ retirado, día solo por resumen, «más de 20 disparos» por slug · Ciudad Victoria: N+ sustituido por Notigape y El Mañana · Zamora: PCM → Grupo Marmor 2026/11/16; día por ruta; ★★★☆☆ · Los Magueyes: discrepancia de Reporte18 · Jolalpan: «cuatro» de Diario Cambio · Agoragto: fecha no determinada · Tecate: solo Tribuna |
| `editor-duplicidad` | R1 (paralelo) | CORREGIR | Terceras apariciones retiradas de las fichas (Rancho Anapra, Infonavit Playas, col. Valencia, bloqueos) · detenidos 1 o 2 contradicho · Cajeme a vistos · Cosoleacaque: posible duplicidad con -149-013 · seguimientos con dos campos (Cuernavaca con regidor y día solo por resumen; Zapopan solo -149-018; Texhuacán y Tepehuacán con titular) · Tecate Los Encinos: posible caso homónimo · FE reescrita (Jolalpan, se mantienen 2; Tecate condicional; -152-008 fuera) · Monterrey: posible duplicidad entre candidatos · «El Mike» 🟡 · Valoración sin reimprimir conteos · conclusiones sin cifras de ficha, líneas distintas de la portada · método fuera del indicador · fila «sin novedad» de sentencias fuera. **No aplicada, con razón**: Yautepec como -REC- (§7). Galeana arsenal: posible duplicidad con el cateo de ARG-152-001, marcado |
| `editor-duplicidad` | R2 (serie) | CORREGIR | N+ retirado del panorama de Azcapotzalco (nacional: El Universal · TV Azteca · Telediario) · «emboscada de septiembre de 2024» retirada del deslinde de -001 (sin fuente) · fe de erratas de Jolalpan fuera del cartelón (`ARG-153-FE-002` reasignada a precisión de `ARG-152-FE-002`) · cláusula de `ARG-152-009` fuera de la FE · balances ya publicados en 152 retirados (Infobae Mazatlán; La Razón cabildos) · Valoración 2 y 5 sin reimprimir totales · Monterrey Bella Vista y «El Mike» marcados como ya publicados en 152. **No aplicada, con razón**: Yautepec como -REC- (§7; la ventana de origen 150 o 151 no es determinable, a diferencia de Tijuana, cuyo sábado tarde-noche caía entero en 151) |
