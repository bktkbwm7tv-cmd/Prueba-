# ARGOS 135 — Archivo de fuentes

**Corte**: 2026-10-17 · **Ventana**: 16-oct 11:34 → 17-oct 09:28 CDMX (**21 h 54 min**; `WINDOW_DAYS = 2`) · **Densidad**: 10 hechos propios / 21,9 h = **0,46 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 09:28 CDMX). Las consultas continuaron hasta las **10:40 CDMX** (marca «Consulta» del cartelón); los hechos posteriores a las 09:28 pertenecen a ARGOS 136.

Informes íntegros de los seis equipos: extraídos al *scratchpad* de la sesión (`informe-<región>.md`) y entregados a los controles.

## 1. La base

- Clon con HEAD suelto en `60f2777`; `origin/main` en `b0558a3`. Se abrió `claude/argos-135` y se fusionó en *fast-forward* `main`, `claude/argos-129` … `-134`, en ese orden y sin conflicto. HEAD de partida: `fc05c81`.
- `reports/`: 183 archivos, última edición `argos-2026-10-16` (ARGOS 134), como estaba previsto.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`**, 09:28. **Ningún documento oficial leído íntegro.** Techo **★★★☆☆**.
- **Consulta de control** («ataque armado muertos "16 de octubre" 2026 México», en los dos modos): `standard` **ningún hecho mexicano del 16-oct**; `extended`, tampoco del 16, pero sí hechos del 15 y anteriores (Irapuato, Valle de Santiago). **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola (Noroeste 26, Noreste 24, Occidente 28, Centro 30, Golfo y federal 27, Sureste 24 = **159**) + **6 del coordinador** = **167**; `procedencia-cifras` hasta **30** → tope 197 de 200.
- **Rendimiento del coordinador** (6): Culiacán, Gran Vía (**ruta fechada**: Línea Directa 2026-10-16; hora 14:40-15:00 → `ARG-135-001`) · Tijuana, Divina Providencia (titular «la tarde del 16 de octubre», ~19:00 → `ARG-135-002`) · Apatzingán, tres cuerpos (Quadratín + El Congresista + Respuesta; el resultado «heridas por explosivos» es de junio: **no se mezcla**) · «Pokémon» (confirma 4 detenidos, ametralladora y 417 cartuchos en titular de La Nigua; fecha del operativo no publicada) · «madrugada de este sábado» (sin hecho mexicano con muertos; Apatzingán, joven atropellado tras disparar, sin muertos, visto) · boletín federal «16 de octubre de 2026» (no hallado: tercera forma de la triple consulta).

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (15 `NO REVISADA` en 134) | **Revisadas ahora (8)**: Chih (`fiscalia.chihuahua.gob.mx`, sin fecha en ventana), Coah (`coahuila.gob.mx`/`fgecoahuila.gob.mx`), Col (`col.gob.mx`, rutas sin fecha), Nay (`nayarit.gob.mx`, mayo-2026), Ags (`aguascalientes.gob.mx`), Ver (`veracruz.gob.mx/seguridad`, «Resultados 7 y 8 de octubre»), Tab (`tabasco.gob.mx`, junio), Yuc (`ssp.yucatan.gob.mx`). **Siguen `NO REVISADA`**: BCS, Sin (`sspsinaloa.gob.mx` no devuelto), Dgo (`ssp.durango.gob.mx` no devuelto), Edomex, Mor (`ces.morelos.gob.mx` no devuelto), Pue (`ss.puebla.gob.mx` devolvió la Secretaría de **Salud**: no cuenta), Qro (`ssc.queretaro.gob.mx` no devuelto) |
| Prioridad — sentencias (17 `NO REVISADA` en 134) | **Revisadas (12)**: BCS (`pgjebcs.gob.mx`, sin fecha), Dgo (`fiscalia.durango.gob.mx`, hasta 5-sep), NL (`fiscalianl.gob.mx`, estadísticas), SLP (`fiscaliaslp.gob.mx`, 25-ene), Zac (`fiscaliazacatecas.gob.mx`, antiguas), Jal (`fiscalia.jalisco.gob.mx`, comunicados hasta 26-ago), Col (`fgecolima.mx/boletines`, 9-oct por resumen), Gto (`portal.fgeguanajuato.gob.mx`, sin boletín), Edomex, Mor, Pue (`fiscalia.puebla.gob.mx`, feb), Qro (`fiscaliageneralqro.gob.mx`, 5, 6 y 8-oct). **Siguen `NO REVISADA`**: **Son (octava edición sin dominio de fiscalía devuelto)**, **Sin (`fiscaliasinaloa.gob.mx` no devuelto)**, Nay (`fiscalianayarit.gob.mx` sin páginas), Tlax (dominio no devuelto), Camp (el buscador ignoró el `site:` otra vez; `fgecampeche.gob.mx` sin páginas) |
| Ciclo | **A** — Noroeste y Centro encabezaron el triaje judicial tras la prioridad |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Noroeste: Ensenada, 158 años 9 meses a tres sentenciados (Infobae y crprensa 2026/10/17, sin boletín) y Hermosillo, 25 años (Tribuna 2026/10/16, fuente única). Centro: Querétaro con boletines fechados en ruta (5, 6 y 8-oct), todos anteriores |
| Regresión por rotación | Sentencias: Chih, BC, Coah, Mich, Ags, CDMX, Hgo, Gro y Yuc pasan a `NO REVISADA`. Armamento: BC, Son, NL, SLP, Jal, Mich, Gto, CDMX, Tlax, Hgo, Gro, Chis, Camp, QRoo pasan a `NO REVISADA`. **Prioridad sobre el ciclo en 136** |

Serie: … · C (134) no · **A (135) no.**

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **15-oct** | **EXISTE**, formato diario, publicado el **16-oct**: Milenio (`acciones-relevantes-gabinete-de-seguridad-15-de-octubre-2026`), Talla Política, RED113, Emsavalles (republicadores, **no independientes**). Entidades, por resumen: BC, Col, Chih, Gro, Jal, Qro, QRoo, Sin, Son. Acciones del 15-oct: ventana de 134 → `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total. **Cifras solo por resumen: no se imprimen** (Ensenada 5 armas; Manzanillo 15 detenidos; Zapopan 1 larga; Atoyac de Álvarez, laboratorio) |
| **16-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto; agregado «16 y 17»; título entre comillas sin `site:`, por Golfo y por el coordinador). Una página regional con titular «15» y cuerpo «16» (Chiapas, 171 kg de cocaína) tiene **fecha incoherente**: no se fecha |

**Defensa**: `gob.mx/defensa/archivo/prensa` devuelto, último ítem 14-oct → SRIV. **Marina**: `gob.mx/semar` devuelto, índice hasta septiembre → SRIV. **GN**: SRIV (lo más reciente, oct-2025). **FGR**: `gob.mx/fgr` devuelto con páginas 2018-2022 → SRIV. `gabinetedeseguridad.gob.mx/resultados`: no devuelto → `NO REVISADA`.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Silao, Barrio Nuevo** (`ARG-134-001`) | **Jueves 15 sostenido**: cuatro rutas fechadas el 15 (AM, Correo, Noticieros en Línea; N+ sin fecha). **El 14 queda descartado por exclusión**: el miércoles 14 en Silao es **otro hecho** —«doble ataque armado… deja 3 hombres muertos y uno privado de la libertad» (AM `…/2026/10/14/…-1854942.html`)—. Sin fragmento literal «este jueves». **No hay fe de erratas.** Detenidos: ninguno. FGE: sin comunicado |
| **Puebla, Tres Cerritos** (`-005`) | Hora 08:00 / 09:27 / ~10:00: **antes de las 11:34 → ARGOS 134 confirmado**. «Día de descanso» en la mayoría (Diario Puntual 2026/10/16, El Valle 2026/10/17, Posta, Telediario); «en activo» en Retodiario y N+ (compatible: policía en activo en su día libre). SSP «informó» solo por resumen. Sin detenidos. **Dato actualizado**; 🔴 se mantiene |
| **Coquimatlán** (`-003`) | **Sin comunicado de la FGE Colima.** 3 muertos (AFmedios, vadenuez) frente a 2 y 1 herido (Meganoticias, Colima Noticias): el hombre es muerto o herido según la fuente. Se mantiene 2 a 3 |
| **Tlalnepantla** (`-004`) | Sin hora del hallazgo, identidad ni causa. Heraldo del Edomex «dos hombres». Sin cambio |
| **Monterrey y Santa Catarina** (`-002`, `-007`) | Fiscalía confirma que una víctima era expolicía (MVS 2026/10/16); ABC Noticias 2026/10/16 identifica víctimas e informa que la Fiscalía **investiga un posible vínculo**: el fiscal **no lo confirma**. Herido de Santa Catarina: sin dato. El secretario de Seguridad atribuye pertenencia a una estructura criminal, solo por resumen. **`-007` gana declaración institucional por cita** (fiscal nombrado): no se retoca 134 |
| **Laguna Colorada** (`-016`, `ARM-001`) | **Hora ~03:00 solo por resumen** (testimonios de pobladores): sin ancla citable → **sin fe de erratas**. Gabinete, por cita: «cuatro armas de fuego, cargadores, cartuchos…» sin desglose. **El desglose 3 largas/1 corta/8 cargadores no aparece en ninguna fuente** consultada: confirma su retirada en 134. Situación jurídica de los 7: sin dato |
| **Tezontepec y Tula** | **Son dos hechos distintos.** Tezontepec de Aldama, San Gabriel: lunes 12-oct ~19:40 (resumen), automovilista asesinado y civiles armados disparan contra policías municipales que acuden → **`ARG-135-REC-002`**, 🔴 en la ventana de 131. Tula de Allende: noche del domingo 11-oct, 1 muerto y 2 o 3 heridos (Fiscalía por titular de Vanguardia: 1 y 2); policías acudieron desarmados y su patrulla recibió un disparo, sin ataque dirigido → 🟡 de 130, **no recuperable** |
| **Patamban** (`-006`) | Persona defensora **no acreditada** tras consulta específica (sin CEMDA, Red TDT, Comisión DH ni mecanismo). Representante de bienes comunales: autoridad agraria comunitaria, no servidor público formal. **Decisión del destinatario** |
| **Coatzacoalcos** (`-011`) | Captura de la expareja: **no consta** (Quinto Poder 2026/10/16 «buscan a expareja»). FGE «investiga como feminicidio» (no cuenta como institucional). Médica en IMSS-Bienestar e ISSSTE, solo por resumen. **Decisión del destinatario** |
| **Barrancos** (`-013`) | **Mismo hecho que Nakayama**: Línea Directa `…nakayama-del-sector-barrancos…-2026-10-15__1721293` (ruta fechada). Adolescente de 17 años herido leve por esquirla, por resumen → **dato actualizado**. Sinaloahoy «la noche de este martes»: contradice el calendario, descartado |
| **Irapuato, pastor** (`ARG-134-REC-001`) | «Madrugada de este 15 de octubre» (El Universal, por resumen); 01:00-02:00, por resumen → **ventana de 133**, ver §8 |
| **Chiapa de Corzo** (`ARG-134-REC-002`) | **2 muertos y 1 lesionado** por la SSP de Chiapas citada por Azteca Chiapas (por resumen); el «3» de N+ lo contradice su propio cuerpo → 🔴 en su ventana sostenido. Fecha y hora: **sin fijar** (132 o 133) |
| **El Guayabo** (`ARG-134-REC-003`) | Ataque la noche del miércoles 14 (por resumen; otro resultado dice 13); la niña murió el 15 (MVS 2026/10/15). **13 o 14 sigue abierto** |
| **Almoloya** (`ARG-134-REC-004`) | **Domingo 11-oct por la noche** en la mayoría (Por Esto 2026/10/12, Seuno 2026/10/13) → **ventana de 130**, ver §8 |
| **Cajeme** (`ARG-133-REC-005`) | FGJES, por cita: los ocupantes «presuntamente emprendieron la huida y dispararon contra los agentes»; la persecución la inició la autoridad tras un reporte al C5i. **Quién inició la agresión no consta → 🟡 con reserva, sin cambio.** 4 detenidos, un quinto ocupante muerto |
| **Ensenada (pena)** | **158 años 9 meses** a cada uno de tres (Infobae, crprensa 2026/10/17); ver §11 |
| **Sentencias Veracruz, FGR Cosoleacaque y Banderilla, CDMX** | Sin boletín. Publicadas el 15 (y Cosoleacaque también el 16) → anteriores a la apertura; ver §11 |
| **Tulantepec** | No consultado (individualización el 21-oct) |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| Atotonilco (`ARG-133-001`) | PGJEH (encargado de despacho, por cita): **2 mujeres y 3 hombres**; 3 de 5 identificados, 2 entregados (Síntesis 2026/10/16, La Silla Rota 2026/10/15) |
| Jerez (`ARG-133-REC-006`) | Número de víctimas no determinado: la Fiscalía necesita perfil genético (por resumen). Los «cuatro cuerpos» de Jerez son de junio y agosto: no se suman |
| Tijuana (`ARG-133-006`) | Agresor no capturado; policía estable |
| San Blas Atempa (`ARG-132-003`) | Sin detenidos; móvil no oficial (El Mañana 2026/10/15: habría denunciado venta de drogas, por titular); dirigente de la Sección 22. Color: decisión del destinatario |
| «La Patrona» (`ARG-133-009`) | Defensa, GN, SSPC y CNI con la FGE Tabasco, por resumen |
| Puerto Aventuras (`ARG-134-015`) | Expansión 2026/10/16: sin vinculación localizada |
| Orizaba (`ARG-132-002`) | Identidad del muerto no publicada; heridos 2 o 3 |
| Navolato (`ARG-132-001`) | Sin identificaciones |
| Tecuala, Uruapan, Cotija, Salamanca, Romita, Morelia Abastos, Tonalá/Zapopan | Sin novedad fechable |
| «El Wicho» | No consultado |
| Iztapalapa, Xochimilco, Mazatepec, Toluca, Ecatepec | No consultados por presupuesto |
| «Escuinapa, un muerto y cinco heridos» | **Es de julio de 2026** (drones, 12-13 jul; Infobae 2026/07/15): se cierra |
| «El Tripa» (Querétaro) | Código QRO y Alerta Qro 2026/10/16: entregado a Hidalgo por secuestro agravado; Milenio: detenido el 9-oct. **Contradicción sin arbitrar**; publicado el 16, ya visto por 134: no se ficha |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Culiacán, Gran Vía** (`-001`) | Noroeste lo traía sin ruta fechada; el coordinador halló Línea Directa `…a-balazos-asesinan-a-dos-primos…-2026-10-16__1721928`. Hora 14:40-15:00 solo por resumen, posterior a la apertura. 🔴 por homicidio múltiple |
| **Tijuana, Divina Providencia** (`-002`) | Noroeste sin fecha en ruta; el coordinador halló el titular de El Congresista («la tarde del 16 de octubre») y Zeta y Diario Tijuana con ruta `2026/10`. 🔴 por homicidio múltiple. **Bombero voluntario: no se trata como servidor público** |
| **Apatzingán, tres cuerpos** (`-003`) | Fecha solo por titular de El Congresista; hora no publicada. Publicado el día de apertura sin hora: como 134 no lo vio, **se integra aquí con la marca** (la edición que lo ve primero). 🔴 por homicidio múltiple con tortura |
| **Apatzingán, Generalísimo Morelos** (`-004`) | 🟡. El vendedor herido minutos antes en la misma colonia no se ficha: nexo no establecido |
| **Hermosillo** (`-005`, `-006`) | 🟡 cada uno, fuente única (Proyecto Puente). `-006` publicado el 16 sin hora: puede ser de 134 |
| **«Pokémon»** (`-007`, `ARM-001`) | 🟢. Ametralladora sin especificar → **arma larga** por la taxonomía; si la autoridad la clasifica como pesada, pasa a especial. Cortas y cargadores solo por resumen; ametralladora y 417 cartuchos por titular (La Nigua). Confianza del módulo **Medio** |
| **Cateos Mazatlán/Culiacán** (`-008`, `ARM-002`) | 🟢, confianza **Bajo**: 1 larga y 1 detenido solo por resumen |
| **Ajuchitlán** (`-009`) | 🟢 rescate. Seguimiento de `ARG-125-051`; el hecho del corte es la localización con vida |
| **Tepic** (`-010`) | 🟢: orden de aprehensión cumplida contra un policía estatal por el homicidio de un adolescente del 3-oct (homicidio del 3-oct no publicado en su ventana; no se recupera como `-REC-`: es anterior a las cinco ediciones previas) |
| **Linares** (`-REC-001`) | 🔴 en su ventana por homicidio múltiple. Día contradicho: Fiscalía «jueves» (por resumen), Milenio y Telediario «miércoles». Primera publicación: El Mañana 2026/10/15. **134 si fue el 15; 133 si fue el 14** |
| **Tezontepec de Aldama** (`-REC-002`) | 🔴 en su ventana por ataque contra autoridades: el grupo dispara contra policías que acuden a un reporte. Una sola fuente con ruta fechada (La Silla Rota 2026/10/13) |
| **Colima, El Tívoli** | Mujer asesinada el 16 ~14:20 **solo por resumen**, AFmedios sin fecha en ruta: **no se ficha**, a 136 |
| **Edomex, Marina y FGR** | 7 detenidos y armas; publicación del 17 solo por resumen, rutas sin fecha, desgloses contradictorios → visto, `POSIBLE DUPLICIDAD` |
| **Villahermosa, FGR procesa a 8 con arsenal** | Vinculación del 14-oct (Diario de Tabasco 2026/10/14): fuera de ventana; aseguramiento sin cifra |
| **CDMX, seis detenidos por balear a un motociclista** | Infobae 2026/10/17, fecha del hecho no fijada: visto, a 136 |
| **Criterio de fuente institucional** | El de 134: declaración o comunicado citado de una autoridad nombrada; «la Fiscalía investiga / realiza diligencias» no cuenta. Meganoticias, Por Esto y medios estatales, regionales |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-135-FE-001`** — **Asignaciones de 134 resueltas**: Irapuato, pastor y esposa (`ARG-134-REC-001`) → **ARGOS 133** («madrugada de este 15»). Almoloya (`ARG-134-REC-004`) → **ARGOS 130** (domingo 11 por la noche). Chiapa de Corzo (`-REC-002`): 2 muertos, 🔴 sostenido, ventana 132 o 133 sin fijar. El Guayabo (`-REC-003`): 13 o 14, sin fijar.
- **`ARG-135-FE-002`** — **Recuperaciones de este corte**: Linares (`ARG-135-REC-001`) añade **1 rojo y 2 muertos** a ARGOS 134 (o a 133 si fue el 14). Tezontepec de Aldama (`ARG-135-REC-002`) añade **1 rojo y 1 muerto** a ARGOS 131. Cálculo propio.
- **Actualización de dato, no fe de erratas**: Tres Cerritos (día de descanso) · Barrancos (adolescente herido) · Atotonilco (2 mujeres y 3 hombres) · Laguna Colorada (desglose de 134 no localizado en ninguna fuente).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | **hecho** (`ARG-135-002`) · consulta del coordinador | NO REVISADA | NO REVISADA (Ensenada, por medios) |
| Baja California Sur | **NO REVISADA** | NO REVISADA | SRIV (`pgjebcs.gob.mx`) |
| Sonora | **hechos** (`-005`, `-006`) · seguimiento Cajeme | NO REVISADA | NO REVISADA (`fge.sonora.gob.mx` no devuelto; octava edición) |
| Chihuahua | SRIV (Juárez, Santa Teresa: sin día) | SRIV (`fiscalia.chihuahua.gob.mx`) | NO REVISADA |
| Sinaloa | **hechos** (`-001`, `-007`, `-008`) · seguimientos | NO REVISADA (sin dominio; hechos por medios) | NO REVISADA |
| Durango | regional | NO REVISADA | SRIV (`fiscalia.durango.gob.mx`, 5-sep) |
| Coahuila | regional | SRIV (`coahuila.gob.mx`) | NO REVISADA |
| Nuevo León | SRIV · **`-REC-001`** · seguimientos | NO REVISADA | SRIV (`fiscalianl.gob.mx`) |
| Tamaulipas | SRIV | SRIV (`tamaulipas.gob.mx`) | SRIV (`fgjtam.gob.mx`, 6-11 oct) |
| San Luis Potosí | regional | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | SRIV · seguimiento Jerez | SRIV (`zacatecas.gob.mx`) | SRIV (`fiscaliazacatecas.gob.mx`) |
| Jalisco | regional | NO REVISADA | SRIV (`fiscalia.jalisco.gob.mx`) |
| Colima | regional · El Tívoli (visto) | SRIV (`col.gob.mx`) | SRIV (`fgecolima.mx`) |
| Nayarit | regional · **`-010`** | SRIV (`nayarit.gob.mx`) | NO REVISADA |
| Aguascalientes | SRIV (consulta propia) | SRIV (`aguascalientes.gob.mx`) | NO REVISADA |
| Michoacán | **hechos** (`-003`, `-004`) | NO REVISADA | NO REVISADA |
| Guanajuato | SRIV (consulta propia) · seguimientos | NO REVISADA | SRIV (`portal.fgeguanajuato.gob.mx`) |
| Ciudad de México | regional | NO REVISADA | NO REVISADA |
| Estado de México | SRIV · Marina/FGR (visto) | NO REVISADA | SRIV (`fiscaliaedomex.gob.mx`) |
| Morelos | regional | NO REVISADA | SRIV (`fiscaliamorelos.gob.mx`) |
| Puebla | SRIV (Tres Cerritos, 134) | NO REVISADA | SRIV (`fiscalia.puebla.gob.mx`) |
| Tlaxcala | regional | NO REVISADA | NO REVISADA |
| Hidalgo | SRIV · **`-REC-002`** | NO REVISADA | NO REVISADA |
| Querétaro | SRIV · «El Tripa» (visto) | NO REVISADA | SRIV (`fiscaliageneralqro.gob.mx`) |
| Veracruz | SRIV · seguimientos | SRIV (`veracruz.gob.mx/seguridad`) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | SRIV | SRIV (`tabasco.gob.mx`) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | **hecho** (`-009`) | NO REVISADA | NO REVISADA |
| Chiapas | SRIV · `ARG-134-REC-002` | NO REVISADA | SRIV (`fge.chiapas.gob.mx`) |
| Oaxaca | SRIV | SRIV (`portal.fgeo.gob.mx`, boletín 2,897 del 16-oct sin armas) | SRIV (`portal.fgeo.gob.mx`) |
| Campeche | regional | NO REVISADA | NO REVISADA |
| Yucatán | regional | SRIV (`ssp.yucatan.gob.mx`) | NO REVISADA |
| Quintana Roo | SRIV | NO REVISADA | SRIV (`fgeqroo.gob.mx`, 16-ago) |

**Sentencias: 18 de 32**; FGR revisada por búsqueda; **14 `NO REVISADA`**. **Armamento: 11 de 32**; 21 `NO REVISADA`. **Alto impacto: 20 de 32 con consulta propia**, 11 regional, **BCS `NO REVISADA`**.

## 10. Hechos vistos y NO fichados

Tula de Allende (🟡 de 130) · Tizayuca, Los Héroes y SADASI (🟡 de 130, sin fecha en ruta) · Colima, El Tívoli · Edomex, Marina/FGR · CDMX, seis detenidos por un motociclista · Apatzingán, joven atropellado tras disparar (madrugada del 17, sin muertos) · Ciudad Juárez, dos hombres en brecha de Santa Teresa (sin día del hallazgo) · Chihuahua, ejecutado en un Fusion (sin fecha) · Mazatlán, mujer envuelta; Villa Unión, 2 muertos y 4 heridos (sin fecha) · Culiacán, Maxipista, 5 muertos («martes 15», contradice el calendario) · Quintana Roo, dos prófugos del Barrio 18 (Noticaribe 2026/10/16, sin examinar) · Cancún, 12-oct, cateos con armas (anterior) · Villahermosa, FGR procesa a 8 (vinculación del 14).

## 11. Sentencias — candidatas y vistas

| Caso | Disposición |
|---|---|
| Ensenada, tres sentenciados (nombres no reproducidos en el cartelón), **158 años 9 meses** cada uno, homicidio calificado de tres surfistas, robos | Infobae y crprensa 2026/10/17; sentencia del 16 solo por resumen; reparación ~1 millón y 549 mil pesos, por resumen; **sin boletín** → `PENDIENTE DE CONFIRMACIÓN OFICIAL`; pena compuesta; `FRONTERA` |
| Hermosillo, un sentenciado, **25 años**, homicidio calificado | Tribuna 2026/10/16, fuente única, sin boletín → pendiente |
| Veracruz, homicidio de un periodista, 21 años (J-10/2026) | Publicada el 15: ventana de 134. Dos personas distintas en el caso (un primer implicado detenido en 2022 y el sentenciado, segundo detenido): **sin homonimia** si se mantienen separadas |
| FGR Cosoleacaque (4 años, multa 9,348 pesos) y Banderilla (2 años 6 meses, 83 UMA = 9,736 pesos, por resumen) | Primera publicación 15-oct (La Nigua, Hora Cero): ventana de 134. **Multas distintas: dos casos** |
| CDMX, Diego «N» y Abdiel «N» | Publicada 14-15 oct; sin boletín indexado |
| Nuevo León, 155 años | MVS 2026/10/13: anterior |
| Colima, 27 años por secuestro (abreviado) | Boletín del 9-oct por resumen: anterior |
| Querétaro (5, 6 y 8-oct) · Tamaulipas FGJE-370 (6-oct) · Oaxaca 2,889 (13-oct) | Anteriores |
| Sonora, Nogales, 15 años | Sin fecha en ruta; 12-oct por resumen |

## 12. Desglose de cálculos propios

- **Muertos en hechos propios**: Culiacán 2 + Tijuana 2 + Apatzingán 3 + Apatzingán 1 + Hermosillo 1 + Hermosillo 1 = **10**. Heridos integrados: **0**. Localizados con vida: **6**.
- **Armamento**: ARM-001 3 cortas, 1 larga, 16 cargadores, 417 cartuchos, 4 detenidos; ARM-002 1 larga, 1 detenido → **3 cortas, 2 largas, 417 cartuchos, 16 cargadores, 5 detenidos**.
- **Duración**: 16-oct 11:34 → 17-oct 09:28 = 21 h 54 min. **Densidad**: 10 / 21,9 h = 0,457 → **0,46**.
- **FRONTERA**: 8 de 10 (`-003` a `-010`).

## 13. Los dos controles editoriales

Pendiente: primera ronda sobre la versión commiteada.

## 14. Herramientas

`tools/datos-argos-135.py` (copia de la estructura de 134) → `reports/argos-2026-10-17.html`; `gen-movil.py 135 2026-10-17 134 2026-10-16 09:28`; `gen-texto.py`; `validar.js … 2026-10-16 2026-10-17` → «validación OK».

## 15. Lecciones de método (no van al cartelón)

1. **El coordinador volvió a fijar los rojos**: los dos hechos con dos muertos del 16 (Culiacán, Tijuana) llegaron de la ola sin ruta fechada; una búsqueda dirigida por topónimo los ancló.
2. **El índice del buscador no llega a la noche del viernes 16 ni al sábado 17** en Golfo, Centro y Noreste: el corte se sostiene en hechos de la tarde del 16.
3. **Los encargos de 134 se resolvieron casi todos por exclusión o por mayoría**, no por fragmento: Silao (el 14 era otro hecho), Tres Cerritos (hora antes de las 11:34), Almoloya (domingo), Irapuato (madrugada).
4. **Sonora y Sinaloa: octava edición sin dominio de fiscalía devuelto.** El `site:` encadenado con `OR` hace que el buscador ignore el operador: consultar cada dominio por separado.
