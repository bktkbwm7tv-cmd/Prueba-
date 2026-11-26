# ARGOS 158 — Archivo de fuentes (corte 2026-11-26)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 158 |
| Archivo | `reports/argos-2026-11-26.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **lun 23-nov 08:35 → jue 26-nov 13:44 CDMX** · duración **77 h 09 min** (cálculo con `date`): la más larga de la serie (156: 62 h 54; 157: 23 h 01) |
| Calendario | lun 23 (08:35–23:59, 15 h 25) · mar 24 (24 h) · mié 25 (24 h) · jue 26 (00:00–13:44, 13 h 44) |
| Hora de arranque (Bloque 0) | 06:10 CDMX · «Procede» a las 13:44 (7 h 34 después): el Comisario aprobó cerrar la ventana a la hora del «Procede» |
| Consulta | __CONSULTA__ CDMX (hora real tomada con `date` al cierre de `procedencia-cifras` R2) |
| Red | `curl https://www.gob.mx/fgr` → `000` (26-nov 06:10): egreso bloqueado; solo WebSearch; techo ★★★★☆ |
| Ciclo | **A** (Noroeste + Centro encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Rama | `claude/argos-158-criminal-intelligence-0wpevh` (encima de `claude/argos-158-criminal-intelligence-2goit7`, que trae la orden; esta encima de `claude/argos-157-criminal-intelligence-qpwf2b`) |
| Radar | `WINDOW_DAYS = 4` (la plantilla de 157 traía 2; reemplazado y asertado) |

## 2. Resultado del corte

- **18 hechos propios** (🔴 7 · 🟡 4 · 🟢 7) en 12 entidades (Son, Sin, NL, Mich, Gto, Jal, Nay, Edomex, CDMX, Pue, Ver, Yuc); densidad 0,23 hechos/hora; 0,09 rojos/hora (cálculo propio). Por fecha asignada: lun 23 3 · mar 24 3 · mié 25 11 · jue 26 1.
- **3 recuperaciones** rojas, fuera de totales: `ARG-158-REC-001` Ocuiltzapotlán (ventana 156; madrugada del 22 solo por resumen; Proceso 2026/11/22) · `-REC-002` Chietla (ventana 156; sábado 21 solo por resumen; ruta solo con mes) · `-REC-003` Cuitzeo (ventana 157; tarde del 22 solo por resumen; rutas del 22).
- Muertos por agresión 11 · heridos 8 · cuerpos o restos 6 (Santa Ana 5, causa no informada por autoridad; Cerro del Cuatro, al menos 1). 7 agresores abatidos fuera del total.
- Armamento integrado: **ninguno** (ninguna cifra por titular ni por autoridad de un aseguramiento de la ventana). Sentencias integrables: 0.
- Marcas: 1 `PUBLICADO EL DÍA DE APERTURA SIN HORA` (-012) · 1 frontera (-018) · 5 cláusulas de retiro (-001, -005, -008, -012, -015).
- Delito y detención en la misma ventana: Peribán–Jilotlán (-002 / -013) y Los Acantos (-007 / -014).

## 3. Fe de erratas a ediciones anteriores

- `ARG-158-FE-001` → **ARGOS 157, vistos**: «Periférico Norte, Edomex, operador de transporte asesinado en un asalto» era del viernes 20, ~03:00, en Tlalnepantla (Infobae 2026/11/21; Seuno Noticias y Lo de Hoy 2026/11/23): ventana de 156, 🟡, no se recupera.
- `ARG-158-FE-002` → **conteo de ARGOS 156**: + Ocuiltzapotlán y + Chietla (rojos). Efecto (cálculo propio, sobre `ARG-157-FE-002`): 20 hechos · 13 🔴 · 3 🟡 · 4 🟢 · 23 muertos por agresión (22 si Nopaltepec = 1) · 5 heridos · 11 entidades (+ Tabasco).
- `ARG-158-FE-003` → **conteo de ARGOS 157**: + Cuitzeo (rojo; 2 cuerpos). Efecto (cálculo propio): 11 hechos · 4 🔴 · 5 🟡 · 2 🟢 · 9 muertos por agresión · 5 heridos · 2 cuerpos · 4 entidades.

## 4. Boletín federal (triple consulta)

| Momento | Día suelto | Rango | Título / dominio | Resultado |
|---|---|---|---|---|
| Inicio | «acciones relevantes "23 de noviembre"» · «"24 de noviembre"» · «"25 de noviembre"» | «"20, 21 y 22 de noviembre"» | «"Acciones relevantes del Gabinete de Seguridad"» sin dominio · `site:gob.mx/sspc` | 20-22 (agregado): solo republicadores (RED113 2026/11; Tallapolítica; Certeza Diario) · **23: indexado en `gob.mx/sspc`** y en Milenio y Tallapolítica · 24: solo republicadores (RED113 2026/11; Tallapolítica) · 25: Milenio y Tallapolítica · `gob.mx/sspc` indexa 3, 5, 6-8, 9, 17, 18 y 23 |
| Cierre | __FEDCIERRE__ | | | |

Contenido por resumen (no fija hora; el del 23 puede incluir acciones anteriores a las 08:35): 23 — Rosarito 4 detenidos, 2 largas y 4 cortas; Sonora 1 detenido, 10 armas, 245 cartuchos; Felipe Carrillo Puerto (Los Lagartos) 7 largas y 24 cargadores; Nayarit 9 detenidos y 4 largas; Matamoros (Los Tres Ríos) 15 vehículos · 25 — Ajijic (ficha -016, sin fila); Ixtlán del Río/Jala laboratorio (ficha -017); Jilotlán, El Limoncito, 11 detenidos y 43 armas (posible duplicidad con -013). SSPC 26-nov: orden de aprehensión contra el presidente municipal de Atzitzintla (ficha -018).

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| Ciclo | A tras la prioridad. Sentencias: 28 de 32 por dominio (saldada Chih; siguen Son —sin páginas— y Camp —sin dominio—; nuevas NO REVISADA: Sin —solo normatividad— y Mich —no consultada—) · armamento: 28 de 32 (saldadas BC, BCS, Dgo, Gto; siguen Son, Sin; nuevas Chih, Oax) · alto impacto: consulta propia en 21 (saldadas Son, Oax, Chis, Yuc, Nay); solo amplia 11 (BC, BCS, Chih, Dgo · Coah, SLP, Zac · Col, Ags · Qro · QRoo) |
| Cláusulas de retiro de 157 | -001 Zinapécuaro: sin hora por titular · -002 Tepexco: sin hora por titular («madrugada del domingo» solo resumen) · -003/-009 El Platanito: publicación 22 por ruta (La Razón); hora sin titular · -010 Lomas de Mazatlán: sin hora · -008 Inforum: ~06:00 del 23 solo resumen (dentro de 157). Todas siguen abiertas |
| Reservas de 157 | -009: los ocho de El Platanito siguen sin separarse de los de ARG-156-013 (misma cifra, misma facción; ninguna fuente con nombres o comunicado) · -002: 3 o 4 muertos y 2 o 3 calcinados por titular; móvil sin autoridad · -003: sin bajas militares documentadas (los 4 militares muertos son de Guasave) · -006 y -007: sin resolver · -010: 2 cargadores, 70 cartuchos .223 y 20 7.62×39 solo resumen; Policía Estatal por titular · -REC-001: 3 detenidos por titular (abctlax; La Prensa de Tlaxcala 2026/11); SSC por resumen |
| Cláusulas heredadas | 156-003 Nopaltepec: hora sin titular; saldo 2 (La Prensa; Angulo7) frente a 1 y 1 herido (La Jornada Estado de México; Reporteros en Movimiento 2026/11/20, «martes» incoherente) · 156-004, 156-012, 156-016: sin novedad · 155-006, 155-009: sin hora · **155-011 Tepehuacán: vinculados los 4 el 24-nov** (seguimiento) · 154-008 Río Bravo: rutas del 18 (Elefante Blanco; CN Tamaulipas); hallazgo del 17 solo resumen · 153-003: heridos 1 o 2 (TV Azteca «dos muertos y dos heridos») · 152-003 Gaviotas Sur: sin hora · 152-002, -004, -005, 153-002, 154-005: no revisadas |
| Vistos con posible ascenso | Cuitzeo: **ascendido a `-REC-003`** · Chietla: **ascendido a `-REC-002`** · Chilpancingo col. Del PRI: sin ruta · Hampolol y Acayucan: madrugada del 22, ventana 156, amarillos · Cuautla: dom 22 noche, ventana 157, amarillo · Periférico Norte: vie 20 (FE-001) · Mazatlán explosivos y Culiacán Libertad: no revisados |
| Boletín federal | §4 |
| Sentencias candidatas | Iguala (sin boletín FGR/PJ; apelada) · FGEO 2,993 (19-nov) · FGET 5126 (sin URL individual; 5127, 18-nov, desaparición, fallo condenatorio) · Chihuahua triple homicidio (La Opción 20261120: 30 años y 2 meses; publicada antes de la ventana) · Copanatoyac: no hallada · nuevas: FGR Hopelchén DPE/5332/2026 · Chihuahua 16 años y 8 meses (La Opción 20261125) · FGR Hermosillo 10 años (resumen) · FGR Jalisco 24-nov: no localizada |
| Seguimientos | Tepehuacán: vinculación de 4 (24-nov) · Guasave: sin vinculación (prisión preventiva a «El Chapo Isidro» y dos más, resumen) · Texhuacán: «indicios de vínculo», orden en trámite (Plumas Libres 2026/11/25) · Carrillo, Juchitán: sin vinculación · Lomas de Angelópolis: Ocoyucan solo por resumen; Infobae 2026/11/22 (sobrino de Caro Quintero) · Atzitzintla: audiencia no publicada · Cajeme, Tecate, Ometepec, Cancún, Zapopan, Stanza Torralba: no revisados |

## 6. Fuentes por ficha (lista íntegra)

- **ARG-158-001 Santa Ana**: La Jornada (2026/11/23) · El Heraldo de México (2026/11/23) · El Diario de Chihuahua (2026/nov/23) · Aristegui (/2311/) · Radio Sonora · La Opinión (2026/11/24) · El Universal.
- **ARG-158-002 / -013 Peribán–Jilotlán**: ABC Noticias (2026/11/25) · Tribuna (2026/11/25) · Infobae (2026/11/26) · EFE vía Infobae (2026/11/26) · El Independiente (2026/11/26) · Crónica (2026/11/26) · Excélsior · El Informador (20261126) · La Voz de Michoacán · Yahoo · López-Dóriga · El Heraldo de México (2026/11/25, primer parte) · LJA · Angulo7 · Changoonga (2026/11/26, Peribán) · Quadratín (Peribán).
- **ARG-158-003 Yuriria**: La Silla Rota (2026/11/24) · AM (2026/11/24) · N+ · Milenio · La Prensa de Coahuila (2026/11/24, agregado).
- **ARG-158-004 Cerro del Cuatro**: El Informador (20261124 y 20261125) · Milenio · UnoTV (no se usa).
- **ARG-158-005 Ixtapaluca**: El Independiente (2026/11/25) · Info7 · N+.
- **ARG-158-006 Monterrey**: MVS (2026/11/25) · El Universal · Milenio · Meganoticias · Excélsior · Telediario · N+ · Horacero · Quinta Fuerza · La Tarde · ENfoque.
- **ARG-158-007 / -014 Los Acantos**: Ríodoce (2026/11/25) · Luz Noticias (2026-11-25) · Quadratín · Sinaloahoy · El Sol de Mazatlán · Meganoticias.
- **ARG-158-008 Ahome**: Infobae/EFE (2026/11/24) · La Patilla (2026/11/24, republica).
- **ARG-158-009 Hueyapan de Ocampo**: MVS (2026/11/25) · Infobae (2026/11/26) · AVC Noticias · e-veracruz.
- **ARG-158-010 Tepito**: La Silla Rota (2026/11/25) · MVS (2026/11/25) · Infobae (2026/11/25) · Maya Comunicación · Meganoticias · XEVT · Crónica Regional («Mueren una mujer y un menor»).
- **ARG-158-011 Hermosillo**: Proyecto Puente (2026/11/25) · El Imparcial (2026/11/25) · Infoson (2026/11/25).
- **ARG-158-012 Progreso**: SSP Yucatán (ssp.yucatan.gob.mx/noticia/1031, sin fecha en la ruta) · Diario de Yucatán (2026/11/23) · Quadratín Yucatán · ProgresoHoy · The Yucatan Times (2026/11).
- **ARG-158-015 Mazatlán, «Los Chapitos»**: Infobae (2026/11/25) · Ríodoce (2026/11/25).
- **ARG-158-016 Ajijic**: Milenio («resultados 25 de noviembre») · Tallapolítica · Hoy Tamaulipas (agregado) · Línea Directa (2026-11-26, agregado).
- **ARG-158-017 Ixtlán del Río**: Milenio · Excélsior · Línea Directa (2026-11-26).
- **ARG-158-018 Atzitzintla**: El Heraldo de México (2026/11/26) · Intolerancia (2026/11/26) · 24 Horas · Carlos Martín Huerta · Vadenuez · Diario de México · SSPC (portada, 26-nov, por resumen).
- **ARG-158-REC-001 Ocuiltzapotlán**: Proceso (2026/11/22).
- **ARG-158-REC-002 Chietla**: El Quinto Medio (2026/11) · Periódico Central (id 532620) · Urbano Puebla · Curul · Diario Cambio (vínculo con ARG-148-002).
- **ARG-158-REC-003 Cuitzeo**: RED Michoacán (2026/11/22) · Changoonga (2026/11/22) · RED113 (2026/11) · Mi Morelia · La Voz de Michoacán · Quadratín.

## 7. Procedencia: decisiones de clasificación

- **Peribán–Jilotlán (-002)**: la Defensa, citada por medios, dice que el personal fue agredido «durante reconocimientos sobre una brecha»; «Ejército repele agresión» por titular → el grupo inicia contra personal en patrullaje → 🔴 (mismo criterio que El Platanito en 157). «Operativo contra “el Maniaco”» por titular deja la reserva escrita. Los 7 abatidos no se suman.
- **Santa Ana (-001)**: «cinco hombres muertos», «asesinados» y «ejecutados» por titular, sin causa informada por autoridad → 🔴 y se cuentan como cuerpos hallados. Hora ~10:01 del 23 solo por resumen → cláusula de retiro.
- **Tepito (-010), Hermosillo (-011)**: un muerto y un herido → 🟡 (criterio de 157 en Culiacán, -004). «Por accidente» en Tepito solo por resumen.
- **Hueyapan (-009)**: exintegrante de la Guardia Nacional, no en funciones → 🟡.
- **Ixtapaluca (-005)**: publicación 25 por ruta; otra nota del 23 solo por resumen → cláusula de retiro.
- **Mazatlán, seis detenidos (-015)**: día de la captura no fijado → cláusula de retiro.
- **Ajijic (-016)**: cifras solo en el cuerpo del boletín republicado (Milenio; Tallapolítica = una fuente) → ficha 🟢 sin fila de armamento.
- **Rosarito**: 4 detenidos y 6 armas por titular (El Imparcial 2026/11/23), aseguramiento de la noche del 22 solo por resumen → visto de la ventana de 157, no se integra.
- **Recuperaciones**: Ocuiltzapotlán y Chietla, dos muertos cada uno (víctimas múltiples) → 🔴 en su ventana; Cuitzeo, dos cuerpos con huellas de violencia → 🔴. Ninguna tiene hora por titular; las tres quedan fuera de todos los totales de 158.
- **Institucional**: autoridad citada por medios sin documento (Defensa, FGJES, FGJEM, Harfuch) → I=0. Solo Progreso tiene portal oficial (SSP Yucatán) → I=1.

## 8. Controles editoriales

__CONTROLES__

## 9. Presupuesto de búsqueda

Control 2 + coordinador 16 (14 antes de la ola + 2 de repetición federal) + ola 151 (6 × 25; el Noroeste usó 26) + `procedencia-cifras` R1 24 + R2 6 = **199** (de 200).

## 10. Hallazgos de método (no van al cartelón)

1. **Ventana larga sin control del «Procede»**: el «Procede» llegó 7 h 34 después del Bloque 0; la ventana se cerró a esa hora con aprobación del Comisario (77 h 09 min).
2. **Concentración en el miércoles 25** (11 de 18 hechos): el lunes 23 y el jueves 26 quedaron con muy pocos hechos fijados por ruta; las búsquedas reservadas por fecha en la ruta no devolvieron hechos nuevos en ninguna región.
3. **El Noroeste volvió a exceder el tope** (26 de 25) y dejó Chihuahua sin armamento por dominio; Occidente dejó la fiscalía de Michoacán sin sentencias; el Sureste, Oaxaca sin armamento.
4. **Pista falsa del recall**: Cuarto Poder «Tres muertos y heridos tras un ataque armado» era del 18-sep (Tuxtla Gutiérrez).
5. **Vistos de 157 mal fechados**: Periférico Norte (FE-001) y Cuitzeo (tenía rutas del 22 que 157 no vio).
6. **Boletín del 23 indexado en `gob.mx/sspc`**: primer boletín diario indexado desde el 18; el 24 y el 25 siguen solo en republicadores.
7. **Duplicidad federal–Defensa**: el mismo despliegue en Peribán–Jilotlán aparece con tres cifras (Defensa 10 detenidos y 33 armas; boletín 11 y 43; Peribán 26-nov 8 y 20): ninguna se integra.
