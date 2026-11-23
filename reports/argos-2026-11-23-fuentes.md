# ARGOS 157 — Archivo de fuentes (corte 2026-11-23)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 157 |
| Archivo | `reports/argos-2026-11-23.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **dom 22-nov 09:34 → lun 23-nov 08:35 CDMX** · duración **23 h 01 min** (cálculo con `date`) |
| Calendario | dom 22 (09:34–23:59, 14 h 26) · lun 23 (00:00–08:35, 8 h 35) |
| Hora de arranque (Bloque 0) | 08:35 CDMX · «Procede» a las 09:39 (1 h 04): dentro de las dos horas, no se ajusta el cierre |
| Consulta | 10:04 CDMX (hora real tomada con `date` al regenerar tras el cierre de `procedencia-cifras` R2; el agente no informó su reloj) |
| Red | `curl https://www.gob.mx/fgr` → `000` (23-nov 08:35): egreso bloqueado; solo WebSearch; techo ★★★★☆ |
| Ciclo | **C** (Occidente + Sureste encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Rama | `claude/argos-157-criminal-intelligence-qpwf2b` (encima de `claude/argos-156-criminal-intelligence-kx9pts`) |
| Radar | `WINDOW_DAYS = 2` (la plantilla de 156 traía 4; reemplazado y asertado) |

## 2. Resultado del corte

- **10 hechos propios** (🔴 3 · 🟡 5 · 🟢 2) en 4 entidades (Mich, Pue, Sin, Gto); densidad 0,43 hechos/hora; 0,13 rojos/hora (cálculo propio).
- **2 recuperaciones** de la ventana de ARGOS 156, rojas, fuera de totales: `ARG-157-REC-001` Calpulalpan (vie 20, solo por resumen; publicación 21 por ruta) y `ARG-157-REC-002` Santa María Ostula (vie 20 ~19:00, solo por resumen; publicación 21 por ruta; rojo por víctimas múltiples, arbitrado en R1).
- Muertos por agresión 9 (Tepexco cuenta 3 de 3 o 4) · heridos 5 · cuerpos 0.
- Armamento integrado: `ARG-157-ARM-001` Lomas de Mazatlán, 90 cartuchos por titular de dos medios (confianza Bajo; cargadores y detenidos n/d). Sentencias integrables: 0.
- Marcas: 3 `PUBLICADO EL DÍA DE APERTURA SIN HORA` (-003, -009, -010) · 1 frontera (-008) · 5 cláusulas de retiro (-001, -002, -003, -009, -010). **Los tres rojos dependen de cláusula**: ninguno tiene hora fijada por titular, y en Zinapécuaro y Tepexco el resumen apunta a antes de las 09:34.
- Delito y detención en la misma ventana: El Platanito (-003 ataque, -009 detención).

## 3. Fe de erratas a ediciones anteriores

- `ARG-157-FE-001` → **ARG-156-003** (Nopaltepec): 156 contó 1 por saldo contradicho; se cuentan 2 (El Heraldo de San Luis Potosí 2026/11/20; Amexi; Angulo7; Netnoticias; Quinta Fuerza), segundo fallecimiento en hospital solo por resumen; Diario Portal y López-Dóriga, un fallecido: saldo aún contradicho. Quadratín Edomex no reproducido en R1.
- `ARG-157-FE-002` → **conteo de ARGOS 156**: + Calpulalpan y + Ostula (rojos). Efecto (cálculo propio): 18 hechos · 11 🔴 · 3 🟡 · 4 🟢 · 19 muertos por agresión (18 si Nopaltepec = 1) · 5 heridos · 10 entidades.
- No es fe de erratas: Pueblo Nuevo (`ARG-156-004`), publicación del 19 por ruta (AM 2026/11/19); día y hora del hecho siguen solo por resumen: dato adicional en seguimiento.

## 4. Boletín federal (triple consulta)

| Momento | Día suelto | Rango | Título / dominio | Resultado |
|---|---|---|---|---|
| Control | — | — | «Gabinete de Seguridad acciones relevantes 22 de noviembre 2026» (standard y extended) | standard: 2024 y 2025 · extended: último, acciones del 19 por republicadores |
| Inicio | «"acciones relevantes del 20 de noviembre"» | «"20, 21 y 22 de noviembre"» | (por título) | 19: publicado, por republicadores (RED113 2026/11; Tallapolítica; Certeza Diario) · 20, 21, 22 y agregado: SRIV |
| Cierre | «"…del 21 de noviembre"» · «"…del 22 de noviembre"» | «"21 y 22"» / «"20 y 21"» | `site:gob.mx/sspc` «de noviembre de 2026» | Sin cambio · `gob.mx/sspc` indexa 3, 5, 6-8, 9, 17 y 18; el 19 solo figura en el índice de prensa sin contenido · liveblog «hoy 22 de noviembre» no fecha · Radiorama «del 22 al 24 de noviembre» sin año: no se cita |

Contenido del 19 por resumen (no fija día ni hora): Mocorito 6 detenidos con un líder; Guerrero 5 detenidos; Churumuco laboratorio; AICM pasajero con dos armas (20-nov): vistos.

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| Ciclo | C tras la prioridad. Sentencias: 29 de 32 revisadas por dominio (saldadas BCS, Sin, Dgo, Jal, Ags, Nay, CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro, Gro, Chis, QRoo; siguen Chih y Son sin páginas, Camp sin dominio) · armamento: 26 de 32 (saldadas Chih, Tamps, CDMX, Pue; siguen BC, Son, Sin; nuevas NO REVISADA: BCS, Dgo, Gto) · alto impacto: 19 con consulta propia (saldadas NL, Mich, Jal, Col, Tlax, Tab, Camp, Ags), 13 solo amplia. **Aporte de la rotación**: ninguna sentencia integrable; Occidente halló Zinapécuaro y Jacona; el Sureste confirmó que el índice de `fiscaliaguerrero.gob.mx` está atrasado (último 2-oct) |
| Cláusulas de retiro de 156 | -003 Nopaltepec: hora sin titular · -004 Pueblo Nuevo: publicación del 19 por ruta (AM), hora solo resumen · -012 Mexicali: El Imparcial 2026/11/20, 19:55 solo resumen · -016 Juchitán: Oaxaca Capital 2026/11/19, hora sin titular. Abiertas |
| Reservas de 156 | -001: quién inició, Harfuch y Defensa por resumen (ataque del grupo a militares en traslado), sin titular · inventario en dos versiones por resumen, atribución no arbitrada · -002: sin cifra de vehículos · -003: 2 muertos (FE) · -005: sin cambio · -006: municipio sigue no fijado (Ocoyucan, La Jornada; San Andrés Cholula, Infobae) · -009: sin localización · -010/-014: comunicado SSP (veracruz.gob.mx 2026/11/20) sin cifra de armas; detenidos atendidos en el IMSS por resumen · -011: heridos 1 o 2 (Digitalmex, dos slugs) · -015/-016: armamento solo por resumen |
| Posible duplicidad Mojolo | Ninguna fuente separa los 3 cuerpos de los 7 abatidos; «Identifican a cuatro abatidos…; ya son nueve» (Línea Directa 2026-11-22): recuento, no se integra |
| Cláusulas heredadas | 155-006 León (Correo 2026/nov/18 vs Noticieros en Línea 2026/nov/19) · 155-009 Tepeaca · 155-011 Tepehuacán (prisión preventiva; audiencia 24-nov y causa 1634/2026 por resumen) · 154-005, 154-008 (Elefante Blanco 2026/11/18) · 153-002 Acaponeta (lun 16 por ruta; cuerpos de 1-3 semanas) · 153-003 · 152-002 a -005: sin hora por titular |
| Vistos con posible ascenso | Chilapa–Atlixtac: hallazgo del 18 por resumen · Mazatlán explosivos y Culiacán Libertad/Felipe Ángeles: NO REVISADOS · Ostula: **ascendido a `-REC-002`** · Puente Nacional: feminicidio del 20 (ventana 156), no rojo |
| Sentencias candidatas | Iguala (sin boletín FGR/PJ; apelada) · FGEO 2,993 (19-nov por resumen) · FGET 5126 (listado histórico; 18-nov; sin URL individual) · Copanatoyac: no hallada (Quadratín, feminicidio, posible homónimo) · Chihuahua triple homicidio (La Opción 20261120; condena 13-nov por resumen) |
| Seguimientos | Guasave: sin vinculación; 5 a FGR Culiacán y 3 a CDMX por resumen · Carrillo: sin vinculación · Juchitán: sin vinculación · Texhuacán: captura publicada el 20 (La Silla Rota) · Tepehuacán: audiencia 24 · Cajeme y Tecate: NO REVISADOS · Ometepec: sin novedad · Cancún: 3 vs 6 · Zapopan: sin novedad · Cuernavaca: vinculado; llevado a juicio (Infobae 2026/11/17) |

## 6. Fuentes por ficha (lista íntegra)

- **ARG-157-001 Zinapécuaro**: Latinus (2026/11/22) · RED Michoacán (2026/11/22) · Changoonga (2026/11/22) · La Jornada (2026/11/23) · La Voz de Michoacán («muere-militar-emboscada-zinapecuaro») · Contramuro · CB Televisión · Atiempo · Meganoticias Morelia · El Clarín. Otro hecho (sept.): Meganoticias, La Voz, Siglo Veinte, 1plana («…tres heridos»).
- **ARG-157-002 Tepexco**: Retodiario (2026/11/22) · Síntesis (2026/11/22) · El Congresista (slug 22-noviembre) · Periódico Central · La Jornada de Oriente · Carlos Martín Huerta · ENfoque · Urbano · Quadratín Puebla · Telediario · Mtpnoticias · Pueblaroja · Mediatik · Municipios Puebla · El Quinto Medio · UnoTV · E-Consulta (dos notas).
- **ARG-157-003 / -009 El Platanito**: La Razón (2026/11/22) · La Jornada (2026/11/22 y 2026/11/23) · Luz Noticias (2026-11-22) · Proceso (2026/11/23) · Crónica (2026/11/23) · El Mañana · adn40 · Grupo Marmor · Excélsior · Rotativo · Netnoticias · SDP Noticias · Sinaloa en Línea · La Plaza Diario · Yahoo Noticias · Infobae 2026/11/23 (cobertura en vivo: no fecha ni sostiene).
- **ARG-157-004 Culiacán**: Luz Noticias (2026-11-22) · Noroeste · Sinaloahoy · Quadratín Sinaloa · Café Negro.
- **ARG-157-005 Mazatlán, Prados del Sol**: Línea Directa (2026-11-22) · Luz Noticias (2026-11-22) · Meganoticias · Los Noticieristas (2026/11) · Noroeste.
- **ARG-157-006 Jacona**: RED Michoacán (2026/11/22; no reproducida en R1) · Respuesta Michoacán · IMN México · Quadratín · La Voz de Michoacán · Radio Zitácuaro · RED113 (2026/11) · Atiempo.
- **ARG-157-007 Irapuato, campos Estrella**: Kuali (2026/11/22, dos notas) · AM (2026/11/22) · Milenio · El Sol de Irapuato · Notus («varios heridos») · Guanajuato Informa · Telediario · XEU (republica).
- **ARG-157-008 Irapuato, Inforum**: AM (2026/11/23) · Agora GTO.
- **ARG-157-010 Lomas de Mazatlán**: Línea Directa (2026-11-22) · Luz Noticias (2026-11-22) · Los Noticieristas (2026/11) · Sinaloahoy · Info7 · Meganoticias.
- **ARG-157-REC-001 Calpulalpan**: Gentetlx (2026/11/21) · N+ · La Prensa de Tlaxcala (2026/11) · Quadratín Tlaxcala · Excélsior («Matan a 3 jóvenes en dos entidades»: no nombra Calpulalpan, no se cuenta) · El Sol de Tlaxcala en X (NO OFICIAL; dice colonia Centro).
- **ARG-157-REC-002 Ostula**: El Independiente (2026/11/21) · La Jornada (2026/11/21 y 2026/11/22) · El Diario de Chihuahua (2026/nov/21) · SinEmbargo · Pie de Página · Milenio.

## 7. Procedencia: decisiones de clasificación

- **Zinapécuaro y Tepexco**: día 22 por ruta, hora solo por resumen anterior a las 09:34 → ficha propia con cláusula de retiro (no `-REC-`: ningún titular fija la hora). Tepexco: dos resúmenes distintos (~03:00; aviso 23:50).
- **El Platanito**: «ataque a militares» por titular (el grupo inicia) → 🔴; patrulla de reconocimiento solo por resumen. Detención: ficha aparte. Frente a ARG-156-013: «ocho más» (Proceso), total 16 por resumen (La Razón), otro municipio → presuntamente distintos; posible duplicidad no descartada, detenidos fuera de totales.
- **Ostula**: 1 muerto y 3 heridas → víctimas múltiples (agravante de la escala para homicidio único) → 🔴 `-REC-` de 156. Atribución al CJNG solo por la comunidad.
- **Lomas de Mazatlán**: 90 cartuchos por titular de dos medios con ruta del 22 → se integra con confianza Bajo (umbral asimétrico de armamento), con marca de apertura y cláusula.
- **Hampolol**: ruta «/22/» sin mes; madrugada por resumen (anterior a la apertura) y amarillo → visto.
- **Chilpancingo**: ninguna ruta con fecha; señuelos con mismo saldo (mayo 2025; Coppel 11-nov) → visto.
- **Institucional**: autoridad citada por medios sin documento (Defensa en -003/-009; FGJE en -REC-001; FGE Mich en -001) → I=0 en todos (criterio uniforme, R1).

## 8. Controles editoriales

| Control | Ronda | Veredicto | Correcciones aplicadas |
|---|---|---|---|
| `editor-duplicidad` | R1 (paralelo) | CORREGIR | FE de 156 con efecto completo · Nopaltepec como arbitraje de saldo · Pueblo Nuevo a seguimiento · deslinde Platanito/156-013 con discriminadores y reserva · inventario reasignado a «atribución no arbitrada» · Zinapécuaro con ARG-117-REC-001 · Irapuato -007 con ARG-155-004 · sentencias: reserva de 2,993, 5126 «No confirmado», Iguala HEREDADO · tarjetas SRIV · Ostula a `-REC-002` · valoración sin ciudades ni recuento de marcas · conclusión 2 con otro encabezado · vistos y seguimientos recortados · E-Consulta retirado de -002 · fecha de publicación en el mapa · títulos de -005 y -007 · portada con cotejo |
| `procedencia-cifras` | R1 (paralelo, 24) | CORREGIR | Infobae liveblog retirado de -003/-009 · Lomas de Mazatlán 90 cartuchos por titular, ARM-001, sin «fuente única» ni GN · Tepexco: rutas 22, calcinados y móvil contradichos, 4 por UnoTV y E-Consulta · -003 retitulado · -007 con campo de futbol y Las Delicias por titular, «varios heridos» contradicho · I=0 uniforme · Nopaltepec sobre El Heraldo SLP, contradicción registrada · Jacona 16 años por titular, 15 años = 6-nov, «un muerto y dos lesionados» como reserva · citas literales (Línea Directa, Kuali) · -008 sin «ambulante» · .50 singular/plural |
| `editor-duplicidad` | R2 (serie) | CORREGIR (menor) | Valoración 3: tres entidades, no dos · Valoración 1 sin justificar el color · conclusión 2 con línea distinta de la portada (vigilar Sinaloa de Leyva y municipios con bloqueos) · emisor personal sustituido por el medio · panel de Tepexco «3 muertos, uno menor» · tarjetas y lectura regional sin repetir Lomas de Mazatlán. Alias «El Chapo Isidro»: se mantiene (precedente de 156) |
| `procedencia-cifras` | R2 (serie, 6 de 6) | CORREGIR (menor) | RED Michoacán 2026/11/22 (Jacona) reproducido: día por ruta · 16 años por titular de La Voz de Michoacán (Quadratín no reproducido) · IMN, Nanchemichoacán y La Voz = una fuente · Tepexco: Mtp Noticias «dos cadáveres calcinados» frente a Quadratín «tres» · El Sol de Irapuato citado completo · Lomas de Mazatlán: corporación contradicha · El Platanito: lugar contradicho; saldo de Aristegui = ARG-156-001, no se suma · Noroeste sin fecha en la ruta (día por Luz Noticias) · marcador de consulta sustituido (10:04) |

No corregido, con razón: los vistos y balances se mantienen en una línea cada uno (son trazabilidad de descarte, recortados a lo indispensable); el resto pasa a este archivo.

## 9. Presupuesto de búsqueda

Control 2 + coordinador 18 + ola 150 (6 × 25) + `procedencia-cifras` R1 24 + R2 6 = **200** (de 200).

## 10. Hallazgos de método (no van al cartelón)

1. **Boletín del 19** sigue solo por republicadores; 20, 21 y 22 sin indexar a las 09:52 del 23.
2. **Liveblog con fecha de otro día en la ruta**: Infobae «en-vivo-…-hoy-22-de-noviembre» publicado con ruta 2026/11/23; el equipo Noroeste lo trajo como fuente fechada.
3. **Recall del coordinador**: Tepexco y Zinapécuaro, los dos rojos del domingo, tienen hora por resumen anterior a la apertura: el riesgo de que el corte quede sin rojos propios tras la cláusula es real.
4. **Señuelos de saldo idéntico en la misma colonia** (Chilpancingo, col. Del PRI: 1 muerto y 2 heridos en mayo de 2025 y el 11-nov en Coppel): sin ruta con fecha, no se fichó.
5. **Encargos no cubiertos por presupuesto**: Noroeste no revisó Mazatlán explosivos, Culiacán Libertad, Cajeme, Tecate, ni las cláusulas 152-154 del Noroeste.
6. **Federales** (GN, Defensa, Semar, FGR) sin consulta por dominio en ningún equipo.

No corregido, con razón (R2): la marca `FRONTERA DE VENTANA` que propuso `procedencia-cifras` para Zinapécuaro y Tepexco no aplica (la frontera es para hechos publicados el día de **cierre**); ambos llevan la cláusula de retiro de apertura. Latinus, RED Michoacán y La Jornada 2026/11/23 (Zinapécuaro) y el «menor» de Tepexco (El Congresista) fueron reproducidos literalmente en R1; R2 no los volvió a ver por presupuesto: se mantienen.
