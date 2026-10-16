# ARGOS 134 — Archivo de fuentes

**Corte**: 2026-10-16 · **Ventana**: 15-oct 07:16 → 16-oct 11:34 CDMX (**28 h 18 min**; `WINDOW_DAYS = 2`) · **Densidad**: 18 hechos propios / 28,3 h = **0,64 hechos/hora**, cálculo propio.
**Hora de cierre**: la hora real de arranque de la producción tras la orden del destinatario (11:34 CDMX). El Bloque 0 se ejecutó a las 05:56; el cierre se fijó en el arranque de la producción y se declara aquí.

Informes íntegros de los seis equipos: extraídos al *scratchpad* de la sesión (`informe-<región>.md`) y entregados a los controles.

## 1. La base

- Clon con HEAD suelto en `60f2777`; `origin/main` en `b0558a3`. Se abrió `claude/argos-134` y se fusionó en *fast-forward* `main`, `claude/argos-129` … `-133`, en ese orden y sin conflicto. HEAD de partida: `c5aec70`.
- `reports/`: 177 archivos, última edición `argos-2026-10-15` (ARGOS 133), como estaba previsto.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (`connect_rejected` del proxy), 05:56. **Ningún documento oficial leído íntegro.** Techo **★★★☆☆**.
- **Consulta de control** («ataque armado muertos "15 de octubre" 2026 México», en los dos modos): `standard` **no devolvió ningún hecho del 15-oct**; `extended` trajo Monterrey (Gómez Morín), Hermosillo, Coquimatlán (que el resumidor situó en Jalisco: **error del resumidor**, es Colima) e Irapuato. **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola (Noroeste 26, Noreste 24, Occidente 31, Centro 26, Golfo y federal 26, Sureste 24 = **157**) + **7 del coordinador** = **166**; `procedencia-cifras` hasta **30** → tope de 200.
- Occidente excedió su cuota en **una** búsqueda (31 de 30), declarado por el propio equipo.
- **Rendimiento del coordinador** (7): policías emboscados (sin hecho en México; Monterrey «ex policías»), madrugada del viernes (**Puebla, Tres Cerritos** y Atoyac), fosas del 15 (solo Atotonilco y Navolato, ya publicados), abatidos del 15 (sin resultado en ventana), Puebla FGE (**ARG-134-REC-005**), Silao Barrio Nuevo ×2 (**ARG-134-001**: día jueves 15, solo por resumen).

## 3. Rotación — prioridad sobre el ciclo y CICLO C, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (12 `NO REVISADA` en 133) | **Revisadas ahora (7)**: BC (`seguridadbc.gob.mx`, último sep-2026), Son (`sonora.gob.mx`, último may-2026), SLP (`seguridad.slp.gob.mx`, `slp.gob.mx/ssp`, `fiscaliaslp.gob.mx`; último mar-2026), Jal (`secretariadeseguridad.jalisco.gob.mx`, nota antigua), Mich (`ssp.michoacan.gob.mx`, último 26-ago), Tlax (`comunicacion.tlaxcala.gob.mx`), Hgo (`hidalgo.gob.mx/periodico`). **Siguen `NO REVISADA`**: BCS, Col, Nay (dominio no devuelto), Pue (ningún dominio devuelto), Tab (no devuelto) |
| Prioridad — sentencias (17 `NO REVISADA` en 133) | **Revisadas (8)**: Chih (`fiscalia.chihuahua.gob.mx`, último jun-2026), Coah (`fgecoahuila.gob.mx`, índice hasta 31-ago), Tamps (`fgjtam.gob.mx`, FGJE-370-2026 del 6-oct), Ags (`fiscalia-aguascalientes.gob.mx`, 2-oct), Mich (`comunicacion.fiscaliamichoacan.gob.mx`, índice rezagado), CDMX (`fgjcdmx.gob.mx`, 7-9 oct), Hgo (`procuraduria.hidalgo.gob.mx`), QRoo (`fgeqroo.gob.mx`, 16-ago). **Siguen `NO REVISADA`**: BCS (`procuraduriabcs.gob.mx` no devuelto), **Son (séptima edición sin dominio de fiscalía devuelto)**, **Sin (`fiscaliasinaloa.gob.mx` no devuelto)**, SLP, Jal, Col, Nay (0 resultados del dominio), Tlax, Camp (el buscador ignoró el `site:`) |
| Ciclo | **C** — Occidente y Sureste encabezaron el triaje judicial tras la prioridad |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Occidente: Nayarit 53 años (publicada el 14), Colima asistencia familiar (sin fecha en ruta), FGR Vallarta (posible homónimo). Sureste: Oaxaca 80 años anclada al boletín 2,889 del 13-oct (fuera); FGEO publicó en ventana los boletines 2,895 y 2,897, sin sentencia |
| Regresión por rotación | Sentencias: NL, Zac, Edomex, Mor, Pue, Qro, Dgo pasan a `NO REVISADA` (sin dominio devuelto). Armamento: Chih, Dgo, Coah, Ags, Edomex, Mor, Qro, Ver, Yuc. **Prioridad sobre el ciclo en 135** |

Serie: … · B (133) no · **C (134) no.**

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **14-oct** | **EXISTE**, formato diario, publicado el **15-oct**: Milenio (`acciones-relevantes-de-gabinete-de-seguridad-14-de-octubre-2026`), RED113, Talla Política, Certeza Diario (republicadores, **no independientes**); Línea Directa y Heraldo de Puebla 2026/10/15 resumen. Acciones del 14-oct: ventana de 133 → `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total. Desglose **solo por resumen**: Orizaba (ARG-132-002) 4 detenidos, 3 largas, 2 cortas, 12 cargadores, 248 cartuchos · Poza Rica 3 detenidos, 2 largas, 4 cargadores, 103 cartuchos, 4 liberados · Gustavo Díaz Ordaz (Valadeces) 2 largas, 22 cargadores, 665 cartuchos · Concordia 3 largas, 6 cargadores, 45 cartuchos, 3 granadas · Escuinapa 18 cargadores, 971 cartuchos · Altotonga, Coatzacoalcos y Cuernavaca: 3 cateos, órdenes contra 4 personas |
| **15-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto, «14 y 15», título sin `site:`). Probablemente se publique después del cierre: **no se declara inexistente** |

**GN**: `gob.mx/guardianacional/prensa` devuelto con notas de 2024-2025 y una de Chiapas sin fecha → SRIV. **Defensa** y **Marina**: dominio no devuelto → `NO REVISADA`. **FGR**: `fgr.org.mx` devuelto (listado hasta 9-oct) → SRIV. `gabinetedeseguridad.gob.mx/resultados`: no devuelto → `NO REVISADA`.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Atotonilco de Tula** (`ARG-133-001`) | **3 de 5 cuerpos identificados**, 2 entregados a sus familias; los 5 adultos con ficha de búsqueda, según el encargado de despacho de la PGJEH (La Silla Rota 2026/10/15, Síntesis 2026/10/16, El Universal Hidalgo, Criterio Hidalgo). **Sexo contradicho**: PGJEH «2 mujeres y 3 hombres» frente a «4 hombres y 1 mujer» de las notas del 14. Fecha de inicio de la excavación, boletín de la Comisión y coincidencia con la mujer desaparecida el 5-oct: no localizados. **Dato actualizado, no hecho nuevo** |
| **Irapuato, bar Continental** (`ARG-133-010`) | **Segunda fuente con fecha**: Primer Plano Irapuato 2026/10/15. Hora: «minutos después de las 23:00» del 14 o «cerca de la medianoche», por resumen: **confirma 133**. Detenidos: 2 por Grupo Lobo, vinculación no confirmada; no se atribuyen |
| **Salamanca** (`-002`) | Detenidos **siguen contradichos** (Grupo Lobo: dos jóvenes «presuntamente»; SSP Irapuato: 7 detenidos por hechos recientes, sin URL). No se integran |
| **Romita** (`-003`) | **Segunda fuente con fecha**: AM 2026/10/15 («Acribillan a tres hombres en Romita…»). Hora: ~20:00-21:00. Muerte del herido: **contradicha**, se mantiene 2 muertos y 1 herido grave |
| **Iztapalapa** (`-004`, `-008`) | **Heridos: 3** en Proceso 2026/10/15, La Jornada, UnoTV, Infobae y La Razón; 1 en La Prensa → la mayoría sostiene 3, **dato actualizado**. Arma: «arma de fuego», sin tipo. Vinculación del detenido: no localizada. Color: sin cambio; decisión del destinatario pendiente |
| **Pénjamo, Silao ×2** (`ARG-133-REC-001` a `-003`) | Pénjamo ~05:00-05:30 y Veta de Ramales 07:20 (AM, por resumen): **ventana de 132 confirmada**. Sopeña: sin hora nueva |
| **Cajeme** (`-REC-005`) | Sin hora citable. Primera publicación: El Imparcial, Proyecto Puente e Infoson 2026/10/14. **Dato nuevo, solo por resumen**: los ocupantes habrían disparado contra los agentes; la Fiscalía abrió carpeta por tentativa de homicidio contra servidores públicos → **revisión de color pendiente** (🟡 → 🔴 si se acredita que el grupo inició) |
| **«El Wicho»** | Captura del 13-oct solo por resumen; primera publicación 2026/10/14 (Tribuna, La Jornada, Quinto Poder). **Sin fecha citable: sigue sin integrarse** |
| **Cotija** (`ARG-132-005`) | Sin fragmento citable del 12-oct; la datación «13 de octubre de 2026» de Red Michoacán es de publicación. **Sin fe de erratas** |
| **Escuinapa** (`-005`, `-011`) | `-011`: fragmento citable «la noche de este miércoles» (Luz Noticias 2026-10-15) → hecho del 14, **la marca `FRONTERA` de 133 era prescindible**. `-005`: ~11:00 solo por resumen; segundas fuentes con fecha: Tribuna, El Diario de Chihuahua, Diario de Yucatán 2026/10/14. Detenidos: ninguno. **ARG-130-009: domingo 11-oct** (Revista Espejo 2026/10/11, La Razón 2026/10/12) |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| Navolato (`ARG-132-001`) | Sin identificaciones; FGE: 3 personas preliminar (Sinaloahoy, sin fecha); Luz Noticias 2026-10-13 «Localizan otro cuerpo» |
| Orizaba (`ARG-132-002`) | Sin comunicado FGE posterior ni identidad del muerto. Heridos 2 (La Jornada 2026/10/14) o 3 (La Silla Rota). Titular de Milenio «Tres policías muertos»: ninguna otra fuente lo sostiene, descartado |
| San Blas Atempa (`ARG-132-003`) | Sin detenidos ni móvil; La Jornada 2026/10/14, El Mañana 2026/10/14. Color: decisión del destinatario pendiente |
| Tijuana (`ARG-133-006`) | **Detenida la acompañante** (Tijuana en Línea 2026/10/15); agresor no capturado; policía estable |
| Cancún (`ARG-133-007`) | Sin cotejo. **SM 254**: madrugada del 14-oct ~02:00, Por Esto y Noticaribe 2026/10/14 → ventana de 132; 🟡, no recuperable como `-REC-` |
| «La Patrona» (`ARG-133-009`) | Detención del 14-oct (Infobae, Crónica 2026/10/14); «fuerzas federales y estatales»; vínculo con Jalpa de Méndez por prensa |
| Jerez (`ARG-133-REC-006`) | Hallazgo del 11-oct; número de víctimas no determinado (restos calcinados) |
| Tecuala (`ARG-133-REC-007`) | «Al parecer 4, fuentes no oficiales» (Nayarit Noticias 2026/10/10, por resumen); NTV: cantidad desconocida |
| Reynosa, Actrices Mexicanas | 1 mujer en fosa (aviso anónimo) y 3 hombres asesinados en otros puntos, 12-oct, sin URL con fecha: **se cierra como anterior** |
| Zihuatanejo (13-oct) | Sin URL de 2026: sigue sin respaldo |
| Minatitlán, «El Cabra», Nacajuca, Otatitlán | Sin novedad |
| Naucalpan (`ARG-132-004`) | Sin detenidos (Telediario, por resumen) |
| Tulantepec | Aplazada al 21-oct; cambio de defensa, por resumen |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Silao, Barrio Nuevo** (`ARG-134-001`) | Hallado por el coordinador; el equipo de Occidente lo traía como hecho del 14-oct. Dos consultas: el resumen lo fija el **jueves 15** ~15:30; tres URL del 15-oct (AM 1855473, Correo 169211, Noticieros en Línea). **Día solo por resumen**. 🔴 por homicidio múltiple |
| **Monterrey, Gómez Morín** (`-002`) | 🔴 por homicidio múltiple. **Exautoridad: reserva, no mueve el color** (la escala no fija exautoridades). Identidades no reproducidas |
| **Coquimatlán** (`-003`) | 🔴 con 2 o 3 muertos. Fecha solo por la página de archivo de vadenuez (2026/10/15): ★★☆☆☆ |
| **Tlalnepantla** (`-004`) | 🔴 por hallazgo de dos cuerpos con huellas de violencia (homicidio múltiple). Toluca y Ecatepec del mismo titular de Infobae: no fichados |
| **Puebla, Tres Cerritos** (`-005`) | 🔴 por víctima policía. **Condición solo por titulares** («presunto», «en activo»). Viernes 16 por la mañana, antes del cierre por cualquiera de las dos horas; `FRONTERA` por la regla (día de cierre, hora no fijada) |
| **Patamban** (`-006`) | **🟡**, no 🔴 como proponía el equipo: representante de bienes comunales = autoridad agraria del núcleo, no servidor público; mismo criterio que el exdirigente ganadero de `ARG-133-005`. Revisable por el destinatario |
| **Coatzacoalcos** (`-011`) | 🟡 con reserva: médica del IMSS-Bienestar (servidora pública por empleo); feminicidio con móvil de pareja; agravante sin fijar, como el docente de `ARG-132-003` |
| **Coacalco** (`-010`) | 🟡: sin muertos; menor herida, reserva. «Rumbo a la escuela» puede ser antes de las 07:16 → `FRONTERA` |
| **Hermosillo** (`-012`) | 🟡. Hora «noche del jueves» solo por resumen; publicación 15-oct → `FRONTERA` |
| **Culiacán, Barrancos** (`-013`) | 🟡, ★★☆☆☆: «este jueves» por titular, sin URL con fecha |
| **Culiacán, Laguna Colorada** (`-016`) | 🟢. Inicio ~03:00 solo por resumen: si se fija, es de 133. Armamento integrado con confianza **Bajo**: «4 armas» por resumen de dos medios, desglose 3 largas/1 corta/8 cargadores solo por resumen (`ARG-134-ARM-001`) |
| **Detenciones** (`-014`, `-017`, `-018`) | 🟢 cada una, ficha propia, separadas del delito (regla de los dos eventos). `-014`: 2 armas sin tipo de fuente única → cualitativo |
| **Puerto Aventuras** (`-015`) | 🟢. Servidor público imputado, no víctima |
| **Recuperaciones** | `-REC-001` Irapuato, pastor y esposa (~01:00 del 15 → **133**); `-REC-002` Chiapa de Corzo (14-oct → **133**, 132 si antes de 08:19); `-REC-003` El Guayabo (13 o 14 → **132 o 133**); `-REC-004` Almoloya de Juárez, agente de la FGR (noche del 11 → **130**, ventana 11-oct 08:58 → 12-oct 08:19); `-REC-005` Puebla, personal de Homicidios de la FGE (noche del 12 → **131**, 132 si después de las 07:23 del 13). Las cinco 🔴 en su ventana |
| **Vistos, no fichados** | Uruapan, base de taxis (madrugada del 15, sin víctimas, 🟡 de ventana probable 133: no recuperable) · Atoyac, Veracruz (ataque del 14, muerte madrugada del 15: 🟡 de 133) · Panixtlahuaca, Oaxaca (14-oct, 🟡 de 133) · Xochimilco, Tierra Nueva (fecha sin fijar) · Mazatepec (sin fecha) · Culiacán, Nakayama (día solo por resumen) · Tijuana, El Lago (una sola fuente) · Querétaro, «El Tripa» (una sola fuente, fecha de la detención no publicada) · Toluca y Ecatepec (una sola fuente) · Escuinapa, «un muerto y cinco heridos» (El Tiempo MX, sin fecha: posible agregado) · Morelia, Mercado de Abastos (sin URL) · Tonalá y Zapopan, dos jóvenes llevados por la fuerza (sin fecha) |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-134-FE-001`** — **Omisiones de ARGOS 133**: Irapuato, pastor y esposa (🔴, 2 muertos) y Chiapa de Corzo (🔴, 2 a 3 muertos; 132 si fue antes de las 08:19). El Guayabo (🔴, 2 muertos) se asigna a 132 o 133 cuando se fije la fecha. **Conteo de 133 recalculado, cálculo propio**: rojos 5 → **7**; muertos por agresión 10 → **14 a 15**.
- **`ARG-134-FE-002`** — **Omisión de ARGOS 130**: Almoloya de Juárez (🔴, 1 agente de la FGR muerto). **Omisión de ARGOS 131** (132 si fue después de las 07:23): Puebla, personal de Homicidios (🔴, 1 herido).
- **Actualización de dato, no fe de erratas**: Atotonilco (3 de 5 identificados; sexo contradicho) · Iztapalapa (3 heridos por mayoría de fuentes) · `ARG-133-011` (noche del 14 por fragmento: la marca `FRONTERA` sobraba) · Tijuana (detenida la acompañante) · Cajeme (posible agresión iniciada por los ocupantes, color en revisión).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV · Tijuana El Lago (fuente única) · seguimiento `ARG-133-006` | SRIV (`seguridadbc.gob.mx`, sep-2026) | SRIV (`fgebc.gob.mx`) · Ensenada sin pena |
| Baja California Sur | SRIV | NO REVISADA (ningún dominio devuelto) | NO REVISADA |
| Sonora | **hecho** (`ARG-134-012`) | SRIV (`sonora.gob.mx`, may-2026) | NO REVISADA (`fge.sonora.gob.mx` no devuelto; séptima edición) |
| Chihuahua | SRIV | NO REVISADA | SRIV (`fiscalia.chihuahua.gob.mx`, jun-2026) |
| Sinaloa | **hechos** (`ARG-134-013`, `-016`) · seguimientos Escuinapa, Navolato | **hecho** por medios (`ARG-134-ARM-001`) | NO REVISADA (`fiscaliasinaloa.gob.mx` no devuelto) |
| Durango | SRIV (medios) | NO REVISADA | NO REVISADA |
| Coahuila | SRIV | NO REVISADA (ningún dominio de armamento) | SRIV (`fgecoahuila.gob.mx`, ago) |
| Nuevo León | **hechos** (`ARG-134-002`, `-007`) | SRIV (`nl.gob.mx/es/boletines`) | NO REVISADA (`fiscalianl.gob.mx` no devuelto) |
| Tamaulipas | SRIV · Reynosa (anterior) | SRIV (`tamaulipas.gob.mx`) · Valadeces, evento anterior | SRIV (`fgjtam.gob.mx`, 6-oct) |
| San Luis Potosí | SRIV | SRIV (`seguridad.slp.gob.mx`, mar-2026) | NO REVISADA |
| Zacatecas | SRIV · seguimiento Jerez | SRIV (`ssp.zacatecas.gob.mx`, sep) | NO REVISADA (dominio no devuelto) |
| Jalisco | SRIV · Tonalá/Zapopan (sin fecha) | SRIV (`secretariadeseguridad.jalisco.gob.mx`, antigua) | NO REVISADA (0 resultados del dominio) |
| Colima | **hecho** (`ARG-134-003`) | NO REVISADA (0 resultados del dominio) | NO REVISADA (0 resultados del dominio) |
| Nayarit | SRIV · seguimiento Tecuala | NO REVISADA | NO REVISADA |
| Aguascalientes | **NO REVISADA** | NO REVISADA | SRIV (`fiscalia-aguascalientes.gob.mx`, 2-oct) |
| Michoacán | **hecho** (`ARG-134-006`) · `-REC-003` · Uruapan (visto) | SRIV (`ssp.michoacan.gob.mx`, 26-ago) | SRIV (`comunicacion.fiscaliamichoacan.gob.mx`) |
| Guanajuato | **hechos** (`ARG-134-001`, `-018`) · `-REC-001` · seguimientos | SRIV (`boletines.guanajuato.gob.mx`, 15-oct: vinculación FGR, aseguramiento del 6-oct) | SRIV (`boletines.guanajuato.gob.mx`; `portal.fgeguanajuato.gob.mx` 0 resultados) |
| Ciudad de México | **hechos** (`ARG-134-009`, `-014`) · seguimiento Iztapalapa | SRIV (`ssc.cdmx.gob.mx`) | SRIV (`fgjcdmx.gob.mx`, 7-9 oct) · Diego y Abdiel, publicada el 14 |
| Estado de México | **hechos** (`ARG-134-004`, `-010`) · `-REC-004` | NO REVISADA | NO REVISADA |
| Morelos | **hecho** (`ARG-134-008`) | NO REVISADA | NO REVISADA |
| Puebla | **hecho** (`ARG-134-005`) · `-REC-005` | NO REVISADA (ningún dominio devuelto) | NO REVISADA |
| Tlaxcala | SRIV | SRIV (`comunicacion.tlaxcala.gob.mx`) | NO REVISADA |
| Hidalgo | SRIV · seguimiento Atotonilco | SRIV (`hidalgo.gob.mx/periodico`) | SRIV (`procuraduria.hidalgo.gob.mx`) |
| Querétaro | SRIV · «El Tripa» (visto) | NO REVISADA | NO REVISADA |
| Veracruz | **hecho** (`ARG-134-011`) · Atoyac (visto) | NO REVISADA (solo boletín federal) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) · Gamboa y Cosoleacaque, candidatas |
| Tabasco | SRIV | NO REVISADA (no devuelto) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | SRIV | SRIV (`guerrero.gob.mx`, may) | SRIV (`fiscaliaguerrero.gob.mx`, jun) |
| Chiapas | **hecho** (`ARG-134-017`) · `-REC-002` | SRIV (`ssp.chiapas.gob.mx`) | SRIV (`fge.chiapas.gob.mx`, jul-2025) |
| Oaxaca | SRIV · Panixtlahuaca (visto) · San Blas Atempa | SRIV (`sspo.gob.mx`) | SRIV (`portal.fgeo.gob.mx`: boletines 2,895 y 2,897 en ventana, sin sentencia) |
| Campeche | SRIV · seguimiento «La Patrona» | SRIV (`spsc.campeche.gob.mx`, 24-ago) | NO REVISADA (`site:` ignorado) |
| Yucatán | SRIV | NO REVISADA (nada devuelto) | SRIV (`fge.yucatan.gob.mx`, 1-oct) |
| Quintana Roo | **hecho** (`ARG-134-015`) | SRIV (`cgc.qroo.gob.mx`) | SRIV (`fgeqroo.gob.mx`, 16-ago) |

**Sentencias: 16 de 32**; FGR revisada por búsqueda; **16 `NO REVISADA`**. **Armamento: 18 de 32**; 14 `NO REVISADA`. **Alto impacto: 31 de 32** (Aguascalientes `NO REVISADA`). Federales: Gabinete (boletín del 14 existe), GN y FGR SRIV; **Defensa y Marina `NO REVISADA`**.

## 10. Hechos vistos y NO fichados

Ver §7, último renglón. Además: Escuinapa, `ARG-133-005` y `-011` (seguimientos) · Xalapa, col. La Salud (sin fecha en ruta; «mañana» del 15 puede ser anterior) · sentencias de §11.

## 11. Sentencias — candidatas y vistas

| Caso | Disposición |
|---|---|
| Veracruz, Sebastián Alejandro «N», 21 años, homicidio del periodista José Luis Gamboa (juicio oral J-10/2026) | Publicada en ventana (La Silla Rota, La Política en Rosa 2026/10/15); **sin boletín** → `PENDIENTE DE CONFIRMACIÓN OFICIAL`. Segundo detenido del caso: cotejar homonimia con un sentenciado previo |
| FGR, Cosoleacaque, Abigail «N» y Armando «N», 4 años y multa de 9,348 pesos | Sentencia del 8-oct; publicación en ventana (La Nigua 2026/10/15, Hora Cero 2026/10/16) → pendiente |
| FGJCDMX, Diego «N» (47 a 6 m) y Abdiel «N» (71 a 3 m, tope de 70), homicidios en la col. Morelos | Título de la cuenta oficial en X: «Obtuvimos sentencias condenatorias…» (por resumen); sentencia del 6-oct; **primera publicación 14-oct** (crprensa) → anterior a la apertura; **omisión de 133 en el módulo de sentencias**, no integrable aquí |
| Colima FGE, asistencia familiar, 3 años | Solo medios, sin fecha en ruta; delito no prioritario |
| Nayarit, Sergio Candelario «N», 53 años 3 meses, desaparición por particulares | NTV 2026/10/14 → fuera |
| FGR Banderilla 2 a 6 m; FGR Antonio «N» 3 a 2 m 12 d | Publicadas el 14-oct → fuera |
| FGR Jalisco (Vallarta), Moisés «N», 4 años | Multa idéntica a otros casos: `POSIBLE CASO HOMÓNIMO`; sin fecha |
| Ensenada | Veredicto del 10-oct; pena no localizada |

## 12. Desglose de cálculos propios

- **Muertos en hechos propios**: Silao 3 + Monterrey 2 + Coquimatlán 2-3 + Puebla 1 + Patamban 1 + Santa Catarina 1 + Oaxtepec 1 + Coatzacoalcos 1 + Hermosillo 1 + Culiacán 1 = **14 a 15**; más **2 cuerpos** en Tlalnepantla.
- **Heridos**: Santa Catarina 1 + Azcapotzalco 2 + Coacalco 2 + Coquimatlán 0-1 = **5 a 6**.
- **Armamento**: una fila (Laguna Colorada): 1 corta, 3 largas, 8 cargadores, 7 detenidos.
- **Densidad**: 18 / 28,3 h = 0,636 → **0,64**.
- **FRONTERA**: 11 de 18 (`-004`, `-005`, `-006`, `-010`, `-012` a `-018`).

## 13. Los dos controles editoriales

*(Se completa tras los pases.)*

## 14. Herramientas

`tools/datos-argos-134.py` (copia de la estructura de 133 con `armrow` de 129) → `reports/argos-2026-10-16.html`; `gen-movil.py 134 2026-10-16 133 2026-10-15 11:34`; `gen-texto.py`; `validar.js … 2026-10-15 2026-10-16` → «validación OK».

## 15. Lecciones de método (no van al cartelón)

1. **El coordinador volvió a hallar el rojo con más muertos** (Silao, Barrio Nuevo): el equipo lo traía con fecha equivocada (14-oct). Una segunda consulta por «este jueves / miércoles» lo fijó.
2. **Las búsquedas de la madrugada del día de apertura sí rindieron**: Irapuato (pastor) y Chiapa de Corzo, ambos de la ventana de 133.
3. **Los pendientes «sin URL con fecha» rinden recuperaciones cuando se buscan expresamente**: Almoloya y El Guayabo.
4. **Sinaloa y Sonora: séptima edición sin dominio de fiscalía devuelto.**
