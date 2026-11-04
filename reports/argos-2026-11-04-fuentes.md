# ARGOS 146 — Archivo de fuentes (corte 2026-11-04)

## 1. Identidad y ventana

- **ARGOS 146**, archivo `argos-2026-11-04.html` (miércoles 4-nov-2026).
- **Ventana**: abre **sáb 31-oct 11:14 CDMX** (cierre de ARGOS 145) y cierra **mié 4-nov 06:52 CDMX** (hora real de arranque, `TZ=America/Mexico_City date`). El «Procede» llegó a las 06:53: no hubo que mover el cierre.
- **Duración: 91 h 38 min** (cálculo con `date`); densidad **24 / 91,63 h = 0,26 hechos/hora** (cálculo propio). Serie: 27 h 08 (144) · 47 h 38 (145, densidad 0,25) · **91 h 38 (146)**.
- `WINDOW_DAYS = 5` (31-oct y 1, 2, 3 y 4-nov); la plantilla de 145 traía 3; el generador lo reemplaza y lo asevera.
- **Ciclo de rotación aplicado: A (Noroeste + Centro)**, después de la prioridad sobre el ciclo (sentencias de BC, SLP, Hgo, Qro, Coah y Camp; armamento de las 8 entidades con dos ediciones `NO REVISADA`; alto impacto con consulta propia para las 10 de solo consulta amplia). **Resultado de la prioridad**: las 8 de armamento con dos ediciones (Chih, Sin, NL, Jal, Nay, Ags, Tlax, Camp) quedaron **revisadas**; de las sentencias prioritarias, BC, SLP, Hgo y Qro revisadas (SRIV); Coah y Camp siguen sin dominio confirmado (Camp: `ucs.campeche.gob.mx` republica boletines de la fiscalía; candidato). Alto impacto con consulta propia: 9 de 10 (Nay, solo amplia).
- **Red**: `curl -s -o /dev/null -m 12 -w '%{http_code}' https://www.gob.mx/fgr` → `000` (proxy: `connect_rejected`) a las 06:52. Egreso bloqueado: solo WebSearch. Techo ★★★★☆; esta edición no supera ★★★☆☆.
- **Rama**: `claude/argos-146`, encima de `claude/argos-145` (fusiones en *fast-forward*; el clon arrancó en HEAD suelto sobre `e19b060`).

## 2. Decisiones pendientes del destinatario (encargo 1)

Se plantearon en el Bloque 0. **El «Procede» no las resolvió**; se aplicó el estado vigente, reversible:

| Decisión | Estado aplicado en 146 |
|---|---|
| (a) Excepción para rojos sin ruta fechada | **No aplicada**. Cancún obtuvo ruta fechada (Noticaribe 2026/10/30) → `ARG-146-REC-001`; Valle de Chalco sigue sin ruta y resultan posiblemente **dos hechos distintos** (1.ª Secc., 2 muertos y 1 herido, noche del viernes; 2.ª Secc., 1 muerto y 1 herido) |
| (b) Celaya `ARG-143-001` | Sigue 🟡; sin fragmento nuevo |
| (c) Orizaba `ARG-132-002` | Sigue 🟡. Muerte del agente el 30-oct sostenida por tres rutas del 2026/10/30 y El Diario de Minatitlán 2026/10/31; la regla de agravantes (muerte de personal de seguridad → 🔴) haría procedente la fe de erratas de color a 132 **si el destinatario la dispone** |

## 3. Fe de erratas a ediciones anteriores (no van al cartelón)

| ARG-ID | Edición afectada | Corrección |
|---|---|---|
| `ARG-146-FE-001` | ARGOS 145 | **Pénjamo `ARG-145-002`**: la segunda víctima murió en el hospital (equipo Occidente, solo por resumen; titular de AM 2026/10/30 «dos hombres muertos»). **🟡 → 🔴**; ARGOS 145 pasa a 2 rojos y 6 muertos por agresión. Reserva: el fallecimiento posterior, solo por resumen |
| `ARG-146-FE-002` | ARGOS 145 | **Cancún, Paseos del Mar**: con ruta fechada (Noticaribe 2026/10/30), es 🔴 de la ventana de 145 → publicado como `ARG-146-REC-001`. Efecto sobre 145: +1 rojo, +3 muertos (con FE-001: 3 rojos, 9 muertos). Ruta de Noticaribe reencontrada en R2 de procedencia |
| — | ARGOS 145 | **Matamoros `ARG-145-REC-001`**: «seis personas ajenas» por *slug* (Infobae 2026/10/31) y «sexta víctima» (El Mañana 2026/10/31): el total de la jornada se fija en **6** (145: «5 o 6, contradicho»). Sin cambio de color ni de totales de 145 |
| — | ARGOS 144 | **Detenidos por titular de medios** (General Bravo y China 2; Lindavista 6): la cifra de Lindavista se atribuye a la SSC solo por resumen; General Bravo sin cifra de autoridad. **No se ejecuta todavía la fe de erratas 8 → n/d**: queda abierta |
| — | ARGOS 144 | **Cuautla `ARG-144-012`**: día 28-oct fijado por cinco rutas; deja de ser fuente única |

**Ario de Rosales** (militar muerto, 31-oct «mañana», solo por resumen): por la regla de frontera de ventana —ARGOS 145 cerró a las 11:14 del 31 sin verlo y la hora no está fijada— se integra a **146** como `ARG-146-024`, con `PUBLICADO EL DÍA DE APERTURA SIN HORA` y cláusula de retiro. No se recupera en 145.

## 4. Boletín federal (triple consulta)

- (a) día suelto «1 de noviembre» y «3 de noviembre»; (b) rango «30 y 31 de octubre, 1 y 2 de noviembre»; (c) título sin dominio «informa acciones relevantes del 3 de noviembre del 2026».
- **Existe un agregado de cuatro días** (acciones del 30 y 31-oct y 1 y 2-nov), publicado el 3-nov, solo por republicadores: Milenio (`…/acciones-relevantes-de-gabinete-de-seguridad-1-2-de-noviembre-2026`), RED113 (2026/11), Tallapolítica, Certeza Diario, Alcaldes de México. **Sustitución anotada; corroboración débil por construcción.** No fija día por acción y abarca la ventana de 145: nada se integra.
- **Acciones del 3-nov**: SRIV en las tres formas. Comunicado del 4-nov sobre Caminaguato–El Tepuche (Heraldo de México 2026/11/4): visto, cifras solo por resumen.
- `gabinetedeseguridad.gob.mx`: no indexa los boletines recientes.

## 5. Resolución de encargos

- **Rojos sin ruta de 145**: Cancún → REC-001; Valle de Chalco → sin ruta (ver §2).
- **Recuperaciones de 145**: REC-001 Matamoros (hora de la muerte de la niña: no publicada; proyectil 7.62 con trayectoria descendente, por titular de La Región 2026/11/03; sin comunicado; total 6) · REC-002 Mazatlán Los Ranchos («poco antes de las 11:00», solo por resumen: sigue en 144) · REC-003 Coatzacoalcos (sin hora; sin cotejo genético; N+ «la FGE confirma que son de un hombre», sin fecha) · REC-004 Tetlatlahuca (día ≤ 28-oct, no fijado).
- **Rojo potencial**: Pénjamo → FE-001 · Vallecillo `ARG-145-004` → sin fragmento; sigue 🟡.
- **Cláusulas de retiro de 145**: `-010` Iztapalapa (las cifras de Milenio, 3 detenidos y 2 largas, coinciden con el agregado federal, sin día) · `-011` Piedras Negras · `-012` Juan R. Escudero: **ninguna se ejecuta**; siguen abiertas.
- **Heredados de 144**: Ciudad del Maíz `-006` (sin día ni cifra) · Ecatepec `-007` (restos de una mujer; sin día) · Cuautla `-012` (cerrado: 28-oct) · Jaral `-020` (nota no localizada) · Concordia, La Guásima (día no fijado).
- **Sentencias candidatas**: ninguna integrable. Tecate, Mexicali, Jalisco y Huejotzingo: publicadas el 29 o 30-oct (ventana de 145). Nuevo: FGR Campeche (metilfenidato, 3-nov, solo por resumen). Oaxaca: no localizado.
- **Seguimientos**: Chenalhó → `ARG-146-020` (2 detenidos) · Orizaba (vinculación de cuatro; imputación por resumen: tentativa y delitos contra instituciones) · Indaparapeo, Magdalena de Kino, Juchitán, Xalapa: sin novedad · Mexicali `-003`: sin resultado de la revisión del uso de fuerza · Tijuana `-143-005`, Tehuacán `-142-010`, Tulantepec: no consultados · Almoloya: vinculación publicada el 27-oct.

## 6. Fuentes por ficha (lista íntegra)

- **001 Tepito**: Tribuna, El Gráfico, Quinto Poder, El Financiero (2026/11/02); Infobae (2026/11/02 y 2026/11/03); Publimetro, Diario de Yucatán (2026/11/03); Ejecentral, Telediario, La Opinión (sin fecha).
- **002 Chinameca**: La Silla Rota (2026/11/3, nota 535731), Diario de Yucatán, Golpe Político, Proyecto Puente, La Prensa de Coahuila (2026/11/03), La Verdad (2026/11); El Universal, N+, Meganoticias, Julio Astillero, XEU, La Nigua (sin fecha).
- **003 Acapulco**: diario.mx (2026/nov/03); Quadratín Guerrero, Bajo Palabra (sin fecha); La Silla Rota (2026/11/3, día lunes).
- **004 Celaya**: AM (2026/11/02). Correo, balance (solo por resumen).
- **005 Silao**: Correo (2026/nov/02), AM (2026/11/03), Noticieros en Línea (2026/nov/03), N+ (sin fecha).
- **006 Irapuato**: Correo (2026/nov/04), Primer Plano Irapuato (2026/11/04).
- **007 / 017 Uruapan**: Changoonga (2026/11/02); Quadratín, El Universal, MiMorelia, Contramuro (sin fecha). Meganoticias 784945 («detienen a dos hombres tras ataque armado contra militares», catalogada como CDMX por un equipo): **posible misma nota de Uruapan**, por cotejar.
- **008 Reynosa**: La Región, CN Tamaulipas (2026/11/02), Elefante Blanco (2026/11/03); Milenio, Hoy Tamaulipas (sin fecha).
- **009 Nuevo Laredo**: N+ (slug «hoy-2-de-noviembre»), Diario Puntual, Lo de Hoy (2026/11/03).
- **010 Suaqui Grande**: El Imparcial, Proyecto Puente, Medios OBSON (2026/11/03); Nuestras Noticias Sonora (sin fecha).
- **011 Mexicali**: El Imparcial (2026/11/02 y 2026/11/03), Periodismo Negro (2026/11/02), La Jornada (2026/11/04); Zeta (2026/11), N+, El Congresista (sin fecha).
- **012 Cuautitlán Izcalli**: El Monitor del Edomex, Cúspide (2026/11/01); Digitalmex, Milenio (dos notas), Unomásuno (sin fecha).
- **013 Culiacán El Compaye**: Luz Noticias, Línea Directa (2026-11-01); Sinaloahoy, Los Noticieristas (2026/11).
- **014 Texmelucan**: Intolerancia Diario (2026/11/02); UnoTV, La Jornada de Oriente, Telediario y otros (sin fecha).
- **015 Tultitlán**: Telediario (titular «hoy 2 noviembre 2026»), Sociedad Noticias (2026/11/03), N+, Digitalmex.
- **016 / 018 Tlaquepaque**: Informador (20261102), Crónica (2026/11/02).
- **019 Cocula**: Proyecto Puente, Cúspide (2026/11/03), Infobae (2026/11/04); Quadratín, Bajo Palabra, Milenio (sin fecha).
- **020 Chenalhó**: Diario de Yucatán, MVS, Herqles (2026/11/03), La Razón (2026/11/04); Diario de Chiapas, SDP (sin fecha).
- **021 Cancún «Garabato»**: Por Esto (2026/11/3).
- **022 / 023 Feria Ganadera**: Infobae (2026/11/02), Latinus (2026/11/2), Proyecto Puente, QuieroTV (2026/11/03); UnoTV, Diario de México, NX Noticias, Meganoticias (sin fecha).
- **024 Ario de Rosales**: Latinus, Grupo Marmor, Changoonga, La Prensa de Coahuila (2026/10/31); La Voz de Michoacán, A Tiempo, El Horizonte, Excélsior, MiMorelia (sin fecha).
- **REC-001 Cancún**: Noticaribe (2026/10/30); Sipse, Quintana Roo Ahora, Turquesa News, Cambio22, Periodistas Quintana Roo, Quintana Roo Hoy (sin fecha).

## 7. Procedencia: decisiones de clasificación

1. **Uruapan `-007` 🔴**: el *slug* («ataque armado contra elementos del Ejército») sostiene que el grupo agredió al personal; el patrullaje y la vivienda, solo por resumen (`PATRULLAJE SOLO POR RESUMEN`). Se mantiene 🔴 por el criterio de quién inicia; si se acreditara un cateo previo, bajaría a 🟡.
2. **Feria Ganadera `-022` 🟡**: los disparos contra los militares que resguardan las instalaciones constan solo por resumen; no se acredita ataque contra autoridades → 🟡 con reserva.
3. **Celaya `-004`**: 3 muertos por titular de fuente única; el balance de Correo (1 muerto y 1 sobreviviente) solo por resumen y no reencontrado en R1: contradicción declarada en ficha, totales, valoración y conclusiones.
4. **Suaqui Grande**: «al menos 4» como cifra mínima; tres o cuatro cráneos, por resumen.
5. **Mexicali**: el segundo hallazgo del 3-nov y Cerro Centinela pueden ser el mismo; cuerpos sin cifra: no afecta totales.
6. **Fichas 019, 020, 021 y 023**: en `EVENTOS` llevan la fecha de publicación (3-nov), porque el día de la detención no está fijado; radar y mapa las sitúan ahí. No cambia totales.
7. **Detenidos en aseguramiento**: ninguno con cifra de autoridad → `n/d` (Uruapan 2, Tlaquepaque 2, Culiacán 3, Cocula 1, por titulares de medios).

## 8. Controles editoriales

**Ronda 1** (en paralelo):
- `editor-duplicidad` R1 — CORREGIR (21 hallazgos; 0 duplicidades reales). Aplicados: deslindes de Miguel Alemán (homónimo de Sinaloa en 143), Texmelucan (visto de equipos, sin ARG-ID), Cocula (ARG-141-007 y ARG-110-REC-001), Tepito (ARG-120-006), Nuevo Laredo (ARG-122-SEN-001), Chenalhó (archivo de fuentes de 145) · posible duplicidad Mexicali/Cerro Centinela · Celaya contradicho en totales, valoración y conclusiones · «menos de 54 horas» · edad contradicha en la Conclusión 4 · cuerpos «al menos» · conclusiones con líneas de vigilancia, distintas de las solicitudes de portada · portada línea 5 por ARG-ID · Huajicori y Huitzuco solo en armamento · retirados Indaparapeo y Cuautla del seguimiento · Oaxaca en candidatos · `</p>` huérfano · pie del mapa de armamento. Pendientes de cierre: `__CONSULTA__`, índice, archivo de fuentes (este).
- `procedencia-cifras` R1 — CORREGIR (16 hallazgos; 22 de 24 búsquedas). Aplicados: Feria Ganadera con ruta → `-022` y `-023` · Irapuato con segunda ruta (deja de ser fuente única) · Reynosa con día por ruta (La Región y CN Tamaulipas 2026/11/02) · Valle de Chalco como posibles dos hechos · Izcalli «tarde o noche» · Uruapan, patrullaje solo por resumen · Mexicali 49 frente a 50 · Suaqui, cifra mínima y cráneos · Acapulco, día contradicho (lunes/martes) · Cancún REC, «una mujer entre las víctimas» · **Ario de Rosales a la edición que lo ve primero** (`-024`) · Orizaba, imputación por titular · Nuevo Laredo, forma «hoy-DD». Mazatlán (policía herido), Acolman y Jiutepec: sin ruta con día; no se fichan.

**Ronda 2** (en serie): ver §9.

## 9. Ronda 2 (en serie)

- `editor-duplicidad` R2 — CORREGIR (1 bloqueante, 10 editoriales; 0 duplicidades). **Aplicados**: Conclusión 2 sin «casquillos» ni «Tacámbaro» (no sostenidos) · Tepito, titular y panorama sin la edad como dato · Celaya en el panorama · Valoración 1 y 2 sin repetir las Conclusiones · Conclusión 1 «del 2 al 4-nov» · Concordia y La Guásima, posible duplicidad declarada · deslinde de Texmelucan con Retodiario 2026/10/28 · recuento «Institucional» con criterio único (0 cuando la declaración consta solo por resumen: -007, -012, -017, -019, -020) · diario.mx y Quadratín como regionales · Feria Ganadera: 24 cargadores y posible inclusión en el agregado federal · orden de ARM · «células armadas» retirado. **Aceptado sin cambio**: -019 y -020 como 🟢 de hoy (detención de delito pasado: regla de CLAUDE.md). Recuentos por tipo de las fichas = fuentes citadas en la ficha; la lista íntegra, en §6.
- `procedencia-cifras` R2 — CORREGIR (10 hallazgos; 6 de 6 búsquedas; ninguna cifra de peso cae). **Aplicados**: Celaya con segundo titular fechado (Noticieros en Línea 2026/nov/03, «sube a tres»): **la atribución a Correo de «1 muerto y 1 sobreviviente» no tiene respaldo** y se retira; deja de ser fuente única (★★★☆☆) · Tepito: «3 años» por titulares del 2026/11/02 (Diario de Yucatán, El Heraldo de SLP), «4 años» por Vanguardia y Ejecentral sin fecha; día del hecho solo por resumen · Chinameca: día solo por resumen; N+ no sostiene la cifra; La Verdad añadida; lugar «en o cerca del panteón» · Acapulco: día solo por resumen · Silao: AM 2026/11/03 («dos muertos»), versión superada; Primer Plano Irapuato añadido · Tultitlán: día solo por *slug* «hoy-DD» · Conclusión 5: «seis días» y «unos 13 meses», con la fecha de 2025 solo por resumen · Conclusión 1: suma de fichas, no el balance de Latinus · Valoración 1: «0,02 a 0,06 en ARGOS 145» (publicado / con las correcciones de §3) · 116 homicidios retirado de indicadores (sigue en balances).
- **Convención señalada y no corregida en bloque**: en las fichas con «lunes 2-NOV, por ruta» (Celaya, Silao, Uruapan, Tlaquepaque, Reynosa, Mexicali) la ruta fija la publicación del mismo día; el día del hecho coincide con la publicación y no cambia la ventana. Se mantiene la forma de 145.
- **Construcción**: `python3 tools/datos-argos-146.py reports/argos-2026-10-31.html reports/argos-2026-11-04.html` · `python3 tools/gen-movil.py 146 2026-11-04 145 2026-10-31 06:52` (25/25 tarjetas; contadores 13/5/6; validación OK) · `python3 tools/gen-texto.py` · `node tools/validar.js reports/argos-2026-11-04.html 2026-10-31 2026-11-04` → **validación OK**. `validar.js` no aplica al móvil (falla igual sobre el móvil de 145); el móvil lo valida `gen-movil.py`.
- **Marca «Consulta»**: 07:26 CDMX (cierre de la última búsqueda de R2).

## 10. Presupuesto de búsqueda

Control 2 · coordinador 17 + 2 de repetición federal = 19 de 20 · ola 150 (6 × 25) · procedencia R1 22 de 24 · R2 6 de 6 · **total 199 de 200**.

## 11. Hallazgos de método (no van al cartelón)

1. **El agregado federal de cuatro días** (30-oct a 2-nov) cruza dos ventanas: no puede integrarse por día; con él, el boletín federal no aporta ninguna cifra integrable en una ventana larga.
2. **Rojo sin ruta que sí la tenía** (Feria Ganadera): el equipo Noroeste no la halló y R1 la encontró en dos búsquedas. La búsqueda por topónimo exacto con día debe hacerse en la ola para todo rojo «sin ruta».
3. **Frontera de apertura**: un hecho publicado el día de apertura con hora solo por resumen («mañana») no debe recuperarse a la edición anterior por inferencia; se integra a la que lo ve primero con la marca (Ario de Rosales).
4. **Deslindes escritos de memoria**: cinco deslindes del primer borrador citaban mal el archivo. El grep debe abrir la línea, no solo listar el archivo.
5. **Duración real frente a la anunciada**: la orden anunció «más de 90 h»; la medida fue 91 h 38 min. Correcto esta vez.
