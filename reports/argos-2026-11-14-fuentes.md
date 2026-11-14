# ARGOS 150 — Archivo de fuentes (corte 2026-11-14)

## 1. Identidad y ventana

| Campo | Valor |
|---|---|
| Número | ARGOS 150 |
| Archivo | `reports/argos-2026-11-14.html` · móvil `-movil.html` · texto `.txt` |
| Ventana | **lun 9-nov 16:07 → sáb 14-nov 10:09 CDMX** · duración **114 h 02 min** (cálculo con `date`) |
| Calendario | lun 9 (16:07–24:00, 7 h 53) · mar 10 (24 h) · mié 11 (24 h) · jue 12 (24 h) · vie 13 (24 h) · sáb 14 (00:00–10:09, 10 h 09) |
| Contexto | Cinco días sin edición (pausa del destinatario). La orden de 150 fechada el 10-nov no se ejecutó; la ventana abre donde cerró 149, sin hueco |
| Hora de arranque (Bloque 0) | 10:09 CDMX · «Continúa» a las 10:13 (4 min): no se ajusta el cierre |
| Consulta | última búsqueda de la ola y del coordinador: 10:23 CDMX (se actualiza tras `procedencia-cifras` R2) |
| `WINDOW_DAYS` | 6 (la plantilla de 149 traía 4) |
| Ciclo | **B** (Noreste + Golfo encabezan el triaje judicial), tras la prioridad sobre el ciclo |
| Red | `curl https://www.gob.mx/fgr` → `000` (14-nov 10:09): egreso bloqueado; solo WebSearch |
| Rama | `claude/argos-150-nacional-61ng7x` (fast-forward hasta `claude/zealous-mendel-baacj5`, 149) |

### Presupuesto por día (declarado en el Bloque 0)

Coordinador: 12 de recall repartidas 2 por fecha (9 a 14) más «fosas», «bloqueos», «drones / instalaciones»; 6 de triple consulta federal. Ola: 25 por equipo con prioridad 🔴 y boletines federales; 4 por equipo reservadas a la fecha en la ruta (10 a 14-nov).

## 2. Resultado del corte

- **23 hechos propios** en 12 entidades: **11 🔴 · 6 🟡 · 6 🟢**; densidad 0,20 hechos/hora (cálculo propio).
- **3 recuperaciones** de la ventana de ARGOS 149 (🔴): Tecate, San Juan Cacahuatepec, Monterrey. Fuera de todos los totales.
- Armamento integrado: 16 largas, 1 especial (lanzagranadas), 39 cargadores, 2 granadas, 21 detenidos en aseguramiento; sin categoría n/d (Silao 13, solo por resumen, no integradas) (cálculo propio).
- Muertos por agresión 15 · heridos 6 · cuerpos o restos 5 · abatidos por la fuerza pública 9 (cálculo propio).
- Sentencias integrables: 0.

## 3. Fe de erratas a ediciones anteriores

| Código | Edición | Corrección |
|---|---|---|
| `ARG-150-FE-001` | 149 | Tres rojos de su ventana recuperados (`ARG-150-REC-001` a `-003`): semáforo corregido de 149, **10 🔴, 7 🟡, 7 🟢** |
| `ARG-150-FE-002` | 149 | `ARG-149-009`: saldo 1 muerto y 1 herido fijado (Tiempo 2026-11-08; La Paradoja 2026/11); se retira «saldo contradicho». Sin efecto numérico |
| `ARG-150-FE-003` | 149 | `ARG-149-010` y `-011`: ya no son fuente única; confianza ★★☆☆☆ → ★★★☆☆ |
| `ARG-150-FE-004` | 149 | Rojos sin ruta retirados: Huaquechula (julio; Ángulo 7, Diario Cambio), Cañada Morelos (e-consulta 2026-06-25), Doctor Coss (MVS 2026/6/29) |
| `ARG-150-FE-005` | 149 | Candidato de sentencia «Ramos Arizpe 13 años 4 meses» = General Cepeda, 19-oct (Red Metropolitana 2026/10/19; Miled 2026/10/19), republicado el 8-nov: se retira |

Los códigos FE van solo aquí y al índice: `gen-movil.py` los rechaza en el cartelón. **FE-002, -003 y -004 se apoyan en los informes de los equipos y no se reverificaron en `procedencia-cifras` R1: `HEREDADO — NO REVERIFICADO`.**

## 4. Boletín federal (triple consulta)

| Acciones del | Resultado |
|---|---|
| 6, 7 y 8-nov (agregado) | `gob.mx/sspc/prensa/el-gabinete-de-seguridad-del-gobierno-de-mexico-informa-acciones-relevantes-del-6-7-y-8-de-noviembre-de-2026` indexado; **segundo republicador**: RED113 (`red113mx.com/2026/11/…_01237552677.html`); Milenio. Ventana de 149: encargo 5 cerrado (sin ficha nueva) |
| 9-nov | `gob.mx/sspc/…del-9-de-noviembre-de-2026` indexado; RED113; Certeza Diario; Milenio. Publicado el 10. Contenido por resumen: Santa Isabel, Silao autopista, Romita, Concordia, Culiacán, Mazatlán, Pinotepa, Jonuta. **Día de apertura sin hora**: vistos en armamento, no integrados (cifras solo por resumen) |
| 10-nov | Milenio, RED113, Tallapolítica. Alimenta `ARG-150-022` (Benemérito) y `-023` (Chacaltianguis) |
| 11-nov | Milenio, RED113, Hoja de Ruta, Tallapolítica, Certeza Diario, Argon México 2026/11/12. Alimenta `ARG-150-013` / `-021` (Temascatío); Nuevo Laredo y Culiacán, vistos |
| 12-nov | Milenio, RED113, Ultranoticias, SICOM, Tallapolítica, Certeza Diario, Consulta Monterrey. Escobedo, Nuevo Laredo, Guadalupe y Calvo, Mazatlán, Aquila, Carácuaro, El Tule, Chietla: vistos. Afectación contradicha 98 / 2,540 / 2,638 mdp |
| 13-nov | `SIN RESULTADO INDEXADO EN VENTANA` por día, por rango (12-13, 13-14) y por título, al inicio y al cierre |

Republicadores del mismo boletín: una fuente, corroboración débil por construcción.

## 5. Resolución de encargos

| Encargo | Resultado |
|---|---|
| 0. Ciclo | B aplicado tras la prioridad sobre el ciclo; Noreste y Golfo encabezaron sentencias. Aporte: candidatos de Veracruz (88 años) y Monterrey (casi 26 años), ambos sin boletín |
| 1. Cláusulas de 149 | `-015` Atempan: día 6 solo por resumen (Infobae 2026/11/08; Quiero TV 2026/11/09; Intolerancia 2026/11/10; gob.mx/sspc sin fecha en la ruta): **sigue** · `-016` Buenavista: primera ruta 8-nov (Esfera Noticias): **sigue** · `-020` Sanalona, `-021` Escuinapa: día no fijado dentro del agregado: **siguen** |
| 1. Frontera de 149 | `-013` Cosoleacaque: «mañana del lunes 9», solo por resumen: **sigue la marca** (si se fija, se queda en 149) · `-019` Acapulco: rutas del 9 sin hora (El Financiero, Crónica, PorEsto, Publimetro): **sigue** |
| 2. Reservas de 149 | `-005` Río Bravo: Infobae 2026/11/10 «del supuesto rescate al escape»; FGJ Tamps: no ha declarado; lugar, autores y acompañantes, abiertos · `-006` Mazatlán: mismo hecho que La Opinión 2026/11/10; La Silla Rota 2026/11/9 «fosa clandestina»; fosa o superficie, contradicho; identificación y causa sin novedad · `-014` Zapopan: sin testimonio independiente; 15 de 20 liberados (RES) · `-009`: fijado 1 y 1 · `-002` SFR: sigue contradicho |
| 3. Rojos sin ruta de 149 | Cacahuatepec → `REC-002` · Tecate → `REC-001` · Monterrey taquería → `REC-003` · Huaquechula, Cañada Morelos → otras fechas · Viesca, Nuevo Laredo, Reynosa → siguen sin ruta |
| 4. Cláusulas de 148 | `-002` hora: sin novedad · `-007` Morelia: día 5-nov solo por resumen · `-009`: sin novedad |
| 5. Boletín federal | Ver §4 |
| 6. Sentencias candidatas | Ninguna integrable; ver §7 |
| 7. Seguimiento | «El Panda» vinculado a proceso (La Silla Rota 2026/11/10; Infobae 2026/11/11) · Matamoros: tres policías declaran (Elefante Blanco 2026/11/09) · Cuernavaca `-147-001`: detenido el presunto autor material (RES) · Mexicali `-146-011`: nuevos restos (El Imparcial 2026/11/12) |

## 6. Fuentes por ficha (lista íntegra)

| ARG-ID | Fuentes |
|---|---|
| 001 Zitácuaro | La Silla Rota 2026/11/13 · MVS 2026/11/13 (SSP, por titular) · Grupo Marmor 2026/11/13 · Contramuro 13112026 · La Voz de Michoacán · AF Medios · RED113 · NX Noticias |
| 002 Tepalcatepec | La Jornada 2026/11/11 · Grupo Marmor 2026/11/11 · Infobae 2026/11/12 · Diario Puntual 2026/11/12 · Posta · La Voz · UnoTV · Heraldo de México 2026/11/11 · Excélsior |
| 003 Ocotlán | La Jornada 2026/11/12 · Grupo Marmor 2026/11/12 · Lo de Hoy 2026/11/13 · El Universal · Milenio · Tribuna de la Bahía · Defensa (X, RES) · ABC Color 2026/11/12 (agencia) |
| 004 Tuxpan | La Silla Rota 2026/11/12 · MVS 2026/11/12 · Diario de Yucatán 2026/11/12 y 2026/11/13 · Proyecto Puente 2026/11/12 · Proceso 2026/11/13 · La Aldea 2026/11/13 · Hoy Xalapa 2026/11/13 · Noticias Veracruz 2026/11/13 · El Universal · XEU · N+ · Meganoticias · TV Azteca |
| 005 Juchitán | Latinus 2026/11/13 · La Silla Rota 2026/11/13 · Diario de Yucatán 2026/11/13 · Quadratín Oaxaca · Imparcial Oaxaca · Diario Marca 2026/11 · Entidad Oaxaca 2026/11 · Omnia |
| 006 San José del Rincón | Seuno 2026/11/11 · Reporteros en Movimiento 2026/11/11 · Telediario · Digitalmex · Diario Evolución · Directiva · Ultranoticias · Poder Edomex |
| 007 Chihuahua | El Diario de Chihuahua 2026/nov/12 · La Opción 20261112 · El Bordo 20261112 · Es Noticia 2026/11 · Tiempo · Impacto Noticias · Omnia · Noticias Delicias · Ocho Columnas 2026/11 |
| 008 Ajacuba | Diario de Yucatán 2026/11/13 · Milenio · Zócalo · La Jornada Hidalgo (PGJEH, por titular) · La Verdad Hidalgo · News Hidalgo · Sin Filtro · Es Periodismo |
| 009 Irapuato | AM 2026/11/12 · Correo 2026/nov/12 · Noticieros en Línea 2026/nov/13 · Quadratín Bajío · N+ · NPI |
| 010 Las Víboras | Luz Noticias 2026-11-13 · Café Negro · Impacto Noticias · Quadratín Sinaloa |
| 011 San Juan del Río | Al Minuto 2026/11/10 · Expreso Querétaro 2026/11/10 · Quadratín Querétaro («riña deja 2 muertos») · Pensador Queretano · N+ · Crónica Regional · Libertad de Palabra · Amanecer Qro. «Macabro hallazgo» (Noticias de Querétaro 2026/11/11), citado por el equipo Centro, no se localizó en procedencia: retirado |
| 012 / 020 Silao | Latinus 2026/11/13 · La Silla Rota 2026/11/13 · AM 2026/11/13 · La Jornada 2026/11/14 · Proyecto Puente 2026/11/13 · UnoTV · El Universal · Vanguardia · Meganoticias · El Otro Enfoque 2026/11/13 · Info7 · El Diario de Chihuahua 2026/nov/13 |
| 013 / 021 Temascatío | Milenio (boletín del 11) · Certeza Diario · Diario de Yucatán 2026/11/12 · Infobae 2026/11/13 |
| 014 Morelia | Quinto Poder 2026/11/10 · Publimetro 2026/11/10 · Grupo Marmor 2026/11/10 · La Razón 2026/11/11 · Excélsior |
| 015 Naucalpan | El Monitor 2026/11/13 · Heraldo de México 2026/11/13 · Cúspide 2026/11/13 · Heraldo SLP 2026/11/13 · Telediario · López Dóriga · Ejecentral · Quadratín Edomex · N+ · Infobae 2026/11/13 |
| 016 Tlalnepantla | Heraldo de México Edomex 2026/11/13 |
| 017 Tijuana | El Imparcial 2026/11/14 · Periodismo Negro 2026/11/14 · Uniradio · Blanco y Negro |
| 018 Ocotlán | Ver 003 |
| 019 Tuxpan | Ver 004 |
| 022 Benemérito | Milenio (boletín del 10) · RED113 · Tallapolítica · Red Metropolitana 2026/11/11 · Heraldo de México 2026/11/11 · El Diario de Chihuahua 2026/nov/11 · Alerta Chiapas 2026/11/11 · Diario Puntual 2026/11/11 · Quadratín Chiapas · Meganoticias |
| 023 Chacaltianguis | Milenio (boletín del 10) · RED113 · Poder y Crítica · El Buen Tono · La Nigua · Potosí Noticias 2026/11/12 |
| REC-001 Tecate | Punto Norte 2026/11/07 · Zeta 2026/11 · El Congresista · Consulta Monterrey · Uniradio (taquería, sin fecha) |
| REC-002 Cacahuatepec | Diario Puntual 2026/11/09 · El Imparcial 2026/11/10 · Quadratín Oaxaca · Diario Marca 2026/11 · Imparcial Oaxaca |
| REC-003 Monterrey | ABC Noticias 2026/11/7 · Primera Línea 2026/11/07 · MVS 2026/11/11 · Vanguardia · Quinta Fuerza |

Recuento por tipo: un emisor por nota propia; ediciones estatales de medios nacionales, regionales (criterio de §6 de 148).

## 7. Procedencia: decisiones de clasificación

1. **Ocotlán 🔴**: Defensa sitúa a su personal «atendiendo un reporte de vehículo robado» (acción de la autoridad) y agredido (RES); el rojo lo fija **solo la agravante** de la civil herida ajena al hecho, con independencia de quién inició. Dos fichas (agresión y detención).
2. **Silao 🟡**: la autoridad acude a una denuncia al 089 y es repelida (RES): confrontación derivada de una acción de la autoridad. Los 6 abatidos no mueven el color. Dos fichas.
3. **Temascatío 🟡 con reserva**: «repelen ataque armado» por titular, «en recorrido de reconocimiento» solo por resumen: quién inició no determinado por titular → 🟡.
4. **Morelia 🟡**: excomisario sin cargo vigente; la agravante de servidor público exige función actual.
5. **Tuxpan 🔴 + 🟢**: dos muertos (la segunda víctima murió después; fecha no fijada, publicación del 13 por ruta) y cuatro detenidos: dos fichas. Día del ataque contradicho (11 o 12); primer ataque contra la misma víctima, martes 10, solo por resumen.
6. **Monterrey (REC-003) 🔴**: homicidio múltiple por tipo de evento, aunque sea riña con arma blanca sin vínculo criminal publicado; reserva escrita en la ficha.
7. **San Juan del Río 🔴**: tras procedencia R1, 2 muertos por titular (Al Minuto y Expreso Querétaro 2026/11/10) y causa contradicha (riña o ataque): muerte violenta en ambas versiones → «muertos por agresión», 🔴 por víctimas múltiples; cláusula de retiro (día del hallazgo frente a las 16:07 del 9).
8. **Armamento por resumen**: las cifras de boletín leídas solo en el resumen del buscador no se integran (n/d); se integran solo las que trae un titular: Benemérito 12 largas y 14 detenidos; Chacaltianguis 4 largas, 39 cargadores, 2 granadas, 1 lanzagranadas; Temascatío 6 detenidos; Ocotlán 1 detenido. **Silao, 13 armas: no se integra** — el titular de Latinus con la cifra no se localizó en `procedencia-cifras` R1; los titulares hallados dicen «aseguran armas».
9. **Atotonilco el Alto**: quema de vehículos sin ruta con día y desmentido de narcobloqueo por titular: rojo sin ruta, no se ficha.
10. **Puebla, bloqueos del 10-nov**: protesta de familiares de internos, sin quema de vehículos (Reto Diario 2026/11/10): ajeno.
11. **Tijuana, 14-nov**: publicada el día de cierre sin hora: `FRONTERA DE VENTANA — HORA NO FIJADA`; si resulta posterior a las 10:09, pasa a 151.
12. **Mazatlán, «6 cuerpos en fosa» (La Opinión 2026/11/10)**: es `ARG-149-006`, no hecho nuevo.
13. **Escalas de confianza**: las fichas usan ★ y el módulo de armamento Alto/Medio/Bajo (CLAUDE.md). Que ARM-002 a -005 lleven «Bajo» y sus fichas ★★★☆☆ no es contradicción: el módulo baja porque el boletín no se leyó.
14. **Institucional**: solo cuenta declaración o comunicado de autoridad nombrada **por titular** (SSP Michoacán, PGJEH) o boletín federal republicado; versiones de Defensa, Fiscalía o SSP leídas solo en el resumen cuentan 0 (Ocotlán, Silao, Tuxpan).
15. **Sentencias sin fecha, no integrables** (vistas por los equipos): fgebc 16282 (robo de vehículo, 6 años 8 meses), Chihuahua «20 años, Juárez», Nayarit «40 años por violación equiparada» (portada de fgenay). Riesgo de homónimo: Monterrey «casi 26 años» frente a «25 años, col. Alhambra»; Tabasco 5119 frente a Bersain «N» (13 años 4 meses, 6-nov) y Cristóbal «N» (30 años, 30-oct).

## 8. Controles editoriales

Pendiente de completar tras R1 y R2.

## 9. Presupuesto de búsqueda

Control 2 · coordinador 18 · ola 151 (Centro 26: excedió el tope en 1) · `procedencia-cifras` R1 24 · R2 5 (reducida en 1 para compensar el exceso de Centro) = **200**.

## 10. Hallazgos de método (no van al cartelón)

1. **Ventana de seis fechas**: los equipos gastaron las búsquedas de ruta en días con pocos resultados; Noroeste solo hizo 3 de 4. Las rutas con comillas devuelven coberturas, no rutas.
2. **Centro excedió el tope en 1** y entregó el cotejo grep solo en modo conteo (sin abrir línea a línea Naucalpan y Tlalnepantla): el control de duplicidad lo cubre.
3. **El boletín del 9 se publicó el 10** y no alcanzó a 149: con cierre a media tarde, el boletín del día de cierre siempre llega a la edición siguiente; sus acciones quedan como día de apertura sin hora.
4. **Republicadores del boletín**: ninguno trae cifras en el titular; los aseguramientos federales solo se integran cuando un medio regional titula la cifra.
5. Dominio nuevo: `sspe.chihuahua.gob.mx` (SSPE de Chihuahua).
