# ARGOS 135 — Archivo de fuentes

**Corte**: 2026-10-17 · **Ventana**: 16-oct 11:34 → 17-oct 09:28 CDMX (**21 h 54 min**; `WINDOW_DAYS = 2`) · **Densidad**: 13 hechos propios / 21,9 h = **0,59 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 09:28 CDMX). Las consultas continuaron hasta las **10:40 CDMX** (marca «Consulta» del cartelón); los hechos posteriores a las 09:28 pertenecen a ARGOS 136.

Informes íntegros de los seis equipos: extraídos al *scratchpad* de la sesión (`informe-<región>.md`) y entregados a los controles.

## 1. La base

- Clon con HEAD suelto en `60f2777`; `origin/main` en `b0558a3`. Se abrió `claude/argos-135` y se fusionó en *fast-forward* `main`, `claude/argos-129` … `-134`, en ese orden y sin conflicto. HEAD de partida: `fc05c81`.
- `reports/`: 183 archivos, última edición `argos-2026-10-16` (ARGOS 134), como estaba previsto.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`**, 09:28. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**.
- **Consulta de control** («ataque armado muertos "16 de octubre" 2026 México», en los dos modos): `standard` **ningún hecho mexicano del 16-oct**; `extended`, tampoco del 16, pero sí hechos del 15 y anteriores (Irapuato, Valle de Santiago). **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola (Noroeste 26, Noreste 24, Occidente 28, Centro 30, Golfo y federal 27, Sureste 24 = **159**) + **8 del coordinador** (6 en la ola, 2 tras la primera ronda: CDMX motociclista, La Costerita) = **169**; `procedencia-cifras` **30** → **199 de 200**. `editor-duplicidad` no busca en la web; la segunda ronda de controles se hace **sin búsquedas**.
- **Rendimiento del coordinador** (6): Culiacán, Gran Vía (**ruta fechada**: Línea Directa 2026-10-16; hora 14:40-15:00 → `ARG-135-001`) · Tijuana, Divina Providencia (titular «la tarde del 16 de octubre», ~19:00 → `ARG-135-002`) · Apatzingán, tres cuerpos (Quadratín + El Congresista + Respuesta; el resultado «heridas por explosivos» es de junio: **no se mezcla**) · «Pokémon» (confirma 4 detenidos; «ametralladora y 417 cartuchos» en el *slug* de La Nigua, `lanigua.com.mx/caen-cuatro-ligados-a-los-chapitos-les-aseguran-ametralladora-y-417-cartuchos/`, sin fecha en la ruta; fecha del operativo no publicada) · «madrugada de este sábado» (sin hecho mexicano con muertos; Apatzingán, joven atropellado tras disparar, sin muertos, visto) · boletín federal «16 de octubre de 2026» (no hallado: tercera forma de la triple consulta).

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
| **15-oct** | **EXISTE**, formato diario, publicado el **16-oct solo por resumen** (la ruta de Milenio dice «15 de octubre»; Emsavalles, titular 15 y cuerpo 16): Milenio (`acciones-relevantes-gabinete-de-seguridad-15-de-octubre-2026`), Talla Política, RED113, Emsavalles (republicadores, **no independientes**). Entidades, por resumen: BC, Col, Chih, Gro, Jal, Qro, QRoo, Sin, Son. Acciones del 15-oct: ventana de 134 → `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total. **Cifras solo por resumen: no se imprimen** (Ensenada 5 armas; Manzanillo 15 detenidos; Zapopan 1 larga; Atoyac de Álvarez, laboratorio) |
| **16-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto; agregado «16 y 17»; título entre comillas sin `site:`, por Golfo y por el coordinador). Una página regional con titular «15» y cuerpo «16» (Chiapas, 171 kg de cocaína) tiene **fecha incoherente**: no se fecha |

**Defensa**: `gob.mx/defensa/archivo/prensa` devuelto, último ítem 14-oct → SRIV. **Marina**: `gob.mx/semar` devuelto, índice hasta septiembre → SRIV. **GN**: SRIV (lo más reciente, oct-2025). **FGR**: `gob.mx/fgr` devuelto con páginas 2018-2022 → SRIV. `gabinetedeseguridad.gob.mx/resultados`: no devuelto → `NO REVISADA`.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Silao, Barrio Nuevo** (`ARG-134-001`) | **Jueves 15 sostenido**: cuatro rutas fechadas el 15 (AM, Correo, Noticieros en Línea; N+ sin fecha). **El 14 queda descartado por exclusión**: el miércoles 14 en Silao es **otro hecho** —«doble ataque armado… deja 3 hombres muertos y uno privado de la libertad» (AM `…/2026/10/14/…-1854942.html`)—. Sin fragmento literal «este jueves». **No hay fe de erratas.** Detenidos: ninguno. FGE: sin comunicado |
| **Puebla, Tres Cerritos** (`ARG-134-005`) | Hora 08:00 / 09:27 / ~10:00: **antes de las 11:34 → ARGOS 134 confirmado**. «Día de descanso» en la mayoría (Diario Puntual 2026/10/16, El Valle 2026/10/17, Posta, Telediario); «en activo» en Retodiario y N+ (compatible: policía en activo en su día libre). SSP «informó» solo por resumen. Sin detenidos. **Dato actualizado**; 🔴 se mantiene |
| **Coquimatlán** (`ARG-134-003`) | **Sin comunicado de la FGE Colima.** 3 muertos (AFmedios, vadenuez) frente a 2 y 1 herido (Meganoticias, Colima Noticias): el hombre es muerto o herido según la fuente. Se mantiene 2 a 3 |
| **Tlalnepantla** (`ARG-134-004`) | Sin hora del hallazgo, identidad ni causa. Heraldo del Edomex «dos hombres». Sin cambio |
| **Monterrey y Santa Catarina** (`ARG-134-002`, `ARG-134-007`) | Fiscalía confirma que una víctima era expolicía (MVS 2026/10/16); ABC Noticias 2026/10/16 identifica víctimas e informa que la Fiscalía **investiga un posible vínculo**: el fiscal **no lo confirma**. Herido de Santa Catarina: sin dato. El secretario de Seguridad atribuye pertenencia a una estructura criminal, solo por resumen. **`ARG-134-007` gana declaración institucional por cita** (fiscal nombrado): no se retoca 134 |
| **Laguna Colorada** (`ARG-134-016`, `ARM-001`) | **Hora ~03:00 solo por resumen** (testimonios de pobladores): sin ancla citable → **sin fe de erratas**. Gabinete, por cita: «cuatro armas de fuego, cargadores, cartuchos…» sin desglose. **El desglose 3 largas/1 corta/8 cargadores no aparece en ninguna fuente** consultada: confirma su retirada en 134. Situación jurídica de los 7: sin dato |
| **Tezontepec y Tula** | **Son dos hechos distintos.** Tezontepec de Aldama, San Gabriel: lunes 12-oct ~19:40 (resumen), automovilista asesinado y civiles armados disparan contra policías municipales que acuden → **`ARG-135-REC-002`**, 🔴 en la ventana de 131. Tula de Allende: noche del domingo 11-oct, 1 muerto y 2 o 3 heridos (Fiscalía por titular de Vanguardia: 1 y 2); policías acudieron desarmados y su patrulla recibió un disparo, sin ataque dirigido → 🟡 de 130, **no recuperable** |
| **Patamban** (`ARG-134-006`) | Persona defensora **no acreditada** tras consulta específica (sin CEMDA, Red TDT, Comisión DH ni mecanismo). Representante de bienes comunales: autoridad agraria comunitaria, no servidor público formal. **Decisión del destinatario** |
| **Coatzacoalcos** (`ARG-134-011`) | Captura de la expareja: **no consta** (Quinto Poder 2026/10/16 «buscan a expareja»). FGE «investiga como feminicidio» (no cuenta como institucional). Médica en IMSS-Bienestar e ISSSTE, solo por resumen. **Decisión del destinatario** |
| **Barrancos** (`ARG-134-013`) | **Mismo hecho que Nakayama**: Línea Directa `…nakayama-del-sector-barrancos…-2026-10-15__1721293` (ruta fechada). Adolescente de 17 años herido leve por esquirla, por resumen → **dato actualizado**. Sinaloahoy «la noche de este martes»: contradice el calendario, descartado |
| **Irapuato, pastor** (`ARG-134-REC-001`) | «Madrugada de este 15 de octubre» (El Universal, por resumen); 01:00-02:00, por resumen → **ventana de 133**, ver §8 |
| **Chiapa de Corzo** (`ARG-134-REC-002`) | **2 muertos y 1 lesionado** por la SSP de Chiapas citada por Azteca Chiapas (por resumen); el «3» de N+ lo contradice su propio cuerpo → 🔴 en su ventana sostenido. Fecha y hora: **sin fijar** (132 o 133) |
| **El Guayabo** (`ARG-134-REC-003`) | Ataque la noche del miércoles 14 (por resumen; otro resultado dice 13); la niña murió el 15 (MVS 2026/10/15). **13 o 14 sigue abierto** |
| **Almoloya** (`ARG-134-REC-004`) | **Domingo 11-oct por la noche** en la mayoría (Por Esto 2026/10/12, Seuno 2026/10/13) → **ventana de 130**, ver §8 |
| **Cajeme** (`ARG-133-REC-005`) | FGJES, por cita: los ocupantes «presuntamente emprendieron la huida y dispararon contra los agentes»; la persecución la inició la autoridad tras un reporte al C5i. **Quién inició la agresión no consta → 🟡 con reserva, sin cambio.** 4 detenidos, un quinto ocupante muerto |
| **Ensenada (pena)** | **158 años** por titular (+9 meses solo por resumen) a cada uno de tres (Infobae, crprensa 2026/10/17); ver §11 |
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
| «El Tripa» (Querétaro) | Código QRO y Alerta Qro 2026/10/16: entregado a Hidalgo por secuestro agravado; Milenio: detenido el 9-oct. **No se ficha por la contradicción de fecha**: si fue el 9, es anterior; si fue el 16, 🟢 fichable. `SIN FECHA FIJADA` de 135 |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Culiacán, Gran Vía** (`-001`) | Noroeste lo traía sin ruta fechada; el coordinador halló Línea Directa `…a-balazos-asesinan-a-dos-primos…-2026-10-16__1721928`. Hora 14:40-15:00 solo por resumen, posterior a la apertura. 🔴 por homicidio múltiple |
| **Tijuana, Divina Providencia** (`-002`) | Noroeste sin fecha en ruta; el coordinador halló el titular de El Congresista («la tarde del 16 de octubre») y Zeta y Diario Tijuana con ruta `2026/10`. 🔴 por homicidio múltiple. **Bombero voluntario: no se trata como servidor público** |
| **Apatzingán, tres cuerpos** (`-003`) | Fecha solo por titular de El Congresista; hora no publicada. Publicado el día de apertura sin hora: como 134 no lo vio, **se integra aquí con la marca** (la edición que lo ve primero). 🔴 por homicidio múltiple con tortura |
| **Apatzingán, Generalísimo Morelos** (`-004`) | 🟡. El vendedor herido minutos antes en la misma colonia no se ficha: nexo no establecido |
| **Hermosillo** (`-005`, `-006`) | 🟡 cada uno, fuente única (Proyecto Puente). `-006` publicado el 16 sin hora: puede ser de 134 |
| **«Pokémon»** (`-008`, `ARM-001`) | 🟢. **`POSIBLE DUPLICIDAD` con `ARG-134-016` / `ARG-134-ARM-001`** (editor-duplicidad, pase 1): Culiacán, Gabinete, «cuatro armas de fuego» = 1 ametralladora + 3 cortas, droga, vehículo; Excélsior liga 4 de los 7 detenidos de 134 a una misma célula. **Fila en ceros, fuera del total hasta validación.** Ametralladora sin especificar → sin categoría. 417 cartuchos y ametralladora por *slug* de La Nigua (sin fecha en ruta); cortas y cargadores solo por resumen. Confianza **Bajo**. Cotejado con Piedras Negras (ARGOS 132: 4 armas y 16 cargadores, vinculación): otra entidad; los 16 cargadores siguen solo por resumen |
| **Cateos Mazatlán/Culiacán** (`-009`, `ARM-002`) | 🟢, confianza **Bajo**. 1 detenido y 8 vehículos en Mazatlán por titular (El Heraldo de México 2026/10/16, sin armas); 1 larga en El Carrizal, sin detenidos, solo por resumen. **`POSIBLE EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`** (boletín de las acciones del 15-oct incluye Sinaloa): **fila en ceros, fuera del total** |
| **Ajuchitlán** (`-010`) | 🟢 rescate. Seguimiento de `ARG-125-051`; el hecho del corte es la localización con vida |
| **Tepic** (`-011`) | 🟢: orden de aprehensión cumplida contra un policía estatal por el homicidio de un adolescente del 3-oct (homicidio del 3-oct no publicado en su ventana; no se recupera como `-REC-`: es anterior a las cinco ediciones previas) |
| **Linares** (`-REC-001`) | 🔴 en su ventana por homicidio múltiple. Día contradicho: Fiscalía «jueves» (por resumen), Milenio y Telediario «miércoles». Primera publicación: El Mañana 2026/10/15. **134 si fue el 15; 133 si fue el 14** |
| **Tezontepec de Aldama** (`-REC-002`) | 🔴 en su ventana por ataque contra autoridades: el grupo dispara contra policías que acuden a un reporte. Una sola fuente con ruta fechada (La Silla Rota 2026/10/13) |
| **Colima, El Tívoli** (`-013`) | Mujer asesinada el 16 ~14:20 **solo por resumen**; AFmedios (titular «Asesinan a balazos a mujer en la colonia El Tívoli, en Colima»), Meganoticias y Vadenuez, sin fecha en ruta. **Fichado en la segunda ronda** por coherencia con La Costerita (mismo defecto: día solo por resumen), 🟡 ★★☆☆☆ con `FRONTERA` |
| **Edomex, Marina y FGR** | 7 detenidos y armas; publicación del 17 solo por resumen, rutas sin fecha, desgloses contradictorios → visto, `POSIBLE DUPLICIDAD` |
| **Villahermosa, FGR procesa a 8 con arsenal** | Vinculación del 14-oct (Diario de Tabasco 2026/10/14): fuera de ventana; aseguramiento sin cifra |
| **CDMX, seis detenidos por balear a un motociclista** (`-012`) | Búsqueda del coordinador: Infobae `infobae.com/mexico/2026/10/17/detienen-a-seis-hombres-por-balear-a-un-motociclista-y-robarle-su-moto-en-cdmx/` (titular «Detienen a seis hombres por balear a un motociclista y robarle su moto en CDMX»), Milenio `milenio.com/policia/caen-seis-por-balear-a-un-joven-para-robarle-su-moto-en-cdmx`; SSC por resumen, sin comunicado; ataque del miércoles 14 → 🟢 con `FRONTERA` |
| **La Costerita** (`-007`) | Hallado por `procedencia-cifras`; búsqueda del coordinador, titulares: Noroeste «Hallan a un hombre ejecutado y maniatado a orillas de La Costerita en Culiacán» · Sinaloahoy «Fiscalía General del Estado investiga hallazgo de hombre maniatado sobre el Libramiento La Costerita» · Noticiero Altavoz «¡Atado de pies y manos! Localizan un ejecutado en La Costerita» · Los Noticieristas (ruta `2026/10`) «Ejecutado a balazos y atado de las manos y pies encuentran a un hombre en El Ranchito» · Extraoficial; sábado 17 ~07:15 solo por resumen → 🟡 con `FRONTERA` |
| **Cachanillas y Nogales** (`-REC-003`, `-REC-004`) | Hallados por `procedencia-cifras`: fosas del 15-oct publicadas el 16 → 🔴 en la ventana de 134 (133 si antes de las 07:16) |
| **Criterio de fuente institucional** | El de 134: declaración o comunicado citado de una autoridad nombrada; «la Fiscalía investiga / realiza diligencias» no cuenta. Meganoticias, Por Esto y medios estatales, regionales |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-135-FE-001`** — **Asignaciones de 134 resueltas**: Irapuato, pastor y esposa (`ARG-134-REC-001`) → **ARGOS 133** («madrugada de este 15»). Almoloya (`ARG-134-REC-004`) → **ARGOS 130** (domingo 11 por la noche): **+1 rojo, +1 muerto a 130** (verificar contra `argos-2026-10-12-fuentes.md`). Chiapa de Corzo (`-REC-002`): 2 muertos, 🔴 sostenido, ventana 132 o 133 sin fijar. El Guayabo (`-REC-003`): 13 o 14, sin fijar. **133 recalculado, cálculo propio**: rojos **6 a 8**, muertos por agresión **12 a 16** (antes 5 a 8 y 10 a 17); **6 a 11 y 12 a 18** si `ARG-135-REC-001`, `-003` y `-004` resultan de 133. `ARG-134-017` y `-REC-002`: un hecho y su detención, sin doble cómputo; arma asegurada sin cifra.
- **`ARG-135-FE-002`** — **Recuperaciones de este corte**: Linares (`ARG-135-REC-001`) añade **1 rojo y 2 muertos** a ARGOS 134 (o a 133 si fue el 14). Cachanillas (`-REC-003`) y Nogales (`-REC-004`) añaden **1 rojo cada una** a ARGOS 134 (o a 133 si antes de las 07:16 del 15). Tezontepec de Aldama (`-REC-002`) añade **1 rojo y 1 muerto** a ARGOS 131. **134: 5 rojos → hasta 8.** Cálculo propio.
- **Actualización de dato, no fe de erratas**: Tres Cerritos (día de descanso) · Barrancos (adolescente herido) · Atotonilco (2 mujeres y 3 hombres) · Laguna Colorada (desglose de 134 no localizado en ninguna fuente).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | **hecho** (`ARG-135-002`) · **`-REC-003`** · consulta del coordinador | NO REVISADA | NO REVISADA (Ensenada, por medios) |
| Baja California Sur | **NO REVISADA** | NO REVISADA | SRIV (`pgjebcs.gob.mx`) |
| Sonora | **hechos** (`-005`, `-006`) · **`-REC-004`** · seguimiento Cajeme | NO REVISADA | NO REVISADA (`fge.sonora.gob.mx` no devuelto; octava edición) |
| Chihuahua | SRIV (Juárez, Santa Teresa: sin día) | SRIV (`fiscalia.chihuahua.gob.mx`) | NO REVISADA |
| Sinaloa | **hechos** (`-001`, `-007`, `-008`, `-009`) · seguimientos | NO REVISADA (sin dominio; hechos por medios) | NO REVISADA |
| Durango | regional | NO REVISADA | SRIV (`fiscalia.durango.gob.mx`, 5-sep) |
| Coahuila | regional | SRIV (`coahuila.gob.mx`) | NO REVISADA |
| Nuevo León | SRIV · **`-REC-001`** · seguimientos | NO REVISADA | SRIV (`fiscalianl.gob.mx`) |
| Tamaulipas | SRIV | SRIV (`tamaulipas.gob.mx`) | SRIV (`fgjtam.gob.mx`, 6-11 oct) |
| San Luis Potosí | regional | NO REVISADA (dominio no devuelto) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | SRIV · seguimiento Jerez | SRIV (`zacatecas.gob.mx`) | SRIV (`fiscaliazacatecas.gob.mx`) |
| Jalisco | regional | NO REVISADA | SRIV (`fiscalia.jalisco.gob.mx`) |
| Colima | regional · **hecho** (`-013`) | SRIV (`col.gob.mx`) | SRIV (`fgecolima.mx`) |
| Nayarit | regional · **`-011`** | SRIV (`nayarit.gob.mx`) | NO REVISADA |
| Aguascalientes | SRIV (consulta propia) | SRIV (`aguascalientes.gob.mx`) | NO REVISADA |
| Michoacán | **hechos** (`-003`, `-004`) | NO REVISADA | NO REVISADA |
| Guanajuato | SRIV (consulta propia) · seguimientos | NO REVISADA | SRIV (`portal.fgeguanajuato.gob.mx`) |
| Ciudad de México | regional · **hecho** (`-012`) | NO REVISADA | NO REVISADA |
| Estado de México | SRIV · Marina/FGR (visto) | NO REVISADA | SRIV (`fiscaliaedomex.gob.mx`) |
| Morelos | regional | NO REVISADA | SRIV (`fiscaliamorelos.gob.mx`) |
| Puebla | SRIV (Tres Cerritos, 134) | NO REVISADA | SRIV (`fiscalia.puebla.gob.mx`) |
| Tlaxcala | regional | NO REVISADA | NO REVISADA |
| Hidalgo | SRIV · **`-REC-002`** | NO REVISADA | NO REVISADA |
| Querétaro | SRIV · «El Tripa» (visto) | NO REVISADA | SRIV (`fiscaliageneralqro.gob.mx`) |
| Veracruz | SRIV · seguimientos | SRIV (`veracruz.gob.mx/seguridad`) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | SRIV | SRIV (`tabasco.gob.mx`) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | **hecho** (`-010`) | NO REVISADA | NO REVISADA |
| Chiapas | SRIV · `ARG-134-REC-002` | NO REVISADA | SRIV (`fge.chiapas.gob.mx`) |
| Oaxaca | SRIV | SRIV (`portal.fgeo.gob.mx`, boletín 2,897 del 16-oct sin armas) | SRIV (`portal.fgeo.gob.mx`) |
| Campeche | regional | NO REVISADA | NO REVISADA |
| Yucatán | regional | SRIV (`ssp.yucatan.gob.mx`) | NO REVISADA |
| Quintana Roo | SRIV | NO REVISADA | SRIV (`fgeqroo.gob.mx`, 16-ago) |

**Sentencias: 18 de 32**; FGR revisada por búsqueda; **14 `NO REVISADA`**. **Armamento: 3 de 32 por dominio propio de seguridad o fiscalía** (Chih, Oax, Yuc) y **8 por portal o subsitio del gobierno estatal** (Coah, Tamps, Zac, Col, Nay, Ags, Ver, Tab); 21 `NO REVISADA`. Oaxaca: `portal.fgeo.gob.mx` **publicó en el periodo** (boletín 2,897 del 16-oct, cateo sin armas, hora no fijada). **Alto impacto: 20 de 32 con consulta propia**, 11 regional, **BCS `NO REVISADA`**.

## 10. Hechos vistos y NO fichados

Tula de Allende (🟡 de 130) · **Taxco**: detención publicada el 16-oct por el asesinato de 6 policías en 2020 — **descartada**: el equipo no registró URL ni hora, solo el titular por resumen; sin respaldo no se ficha (`SIN FECHA FIJADA` de 135) · **Manzanillo**: policía municipal asesinado, cuerpo en Tecomán (Nuevo Caxitlán) y ejecutado en Valle de las Garzas (15-oct, sin fecha verificable) · Colima: armamento de Tecomán y Coquimatlán sin fecha · TV Azteca BC «5 muertos en Tijuana y Ensenada» (agregado) · Escuinapa, exlíder ganadero asesinado (Infobae 2026/10/14, ventana de 132-133, 🟡) · Durango, FGR, rifle y 8 cargadores (6-oct) · Toluca, cuerpo junto a zona militar (15-oct, fuente única) · Tlaxcala, 20 años en Tepeyanco (14-oct, sin fecha en ruta) · Valle de Bravo, 2 largas y 5 detenidos (11-oct) · Veracruz, operativos del 14-15 oct (46 detenidos, sin armas) · Tizayuca, Los Héroes y SADASI (🟡 de 130, sin fecha en ruta) · Edomex, Marina/FGR · Apatzingán, joven atropellado tras disparar (madrugada del 17, sin muertos) · Ciudad Juárez, dos hombres en brecha de Santa Teresa (hallazgo del 11-oct, solo por resumen; fuera) · Chihuahua, ejecutado en un Fusion (sin fecha) · Mazatlán, mujer envuelta; Villa Unión, 2 muertos y 4 heridos (sin fecha) · Culiacán, Maxipista, 5 muertos: **hecho de 15-oct-2024** (año equivocado) · Quintana Roo, dos prófugos del Barrio 18 (Noticaribe 2026/10/16) — **descartada**: contenido no examinado por el equipo, sin cifra ni fecha del hecho · Cancún, 12-oct, cateos con armas (anterior) · Villahermosa, FGR procesa a 8 (vinculación del 14).

## 11. Sentencias — candidatas y vistas

| Caso | Disposición |
|---|---|
| Ensenada, tres sentenciados (nombres no reproducidos en el cartelón), **158 años** cada uno por titular (+9 meses solo por resumen; En Línea BC 2026/10/17), homicidio calificado de tres surfistas, robos | Infobae y crprensa 2026/10/17; sentencia del 16 solo por resumen; reparación ~1 millón y 549 mil pesos, por resumen; **sin boletín** → `PENDIENTE DE CONFIRMACIÓN OFICIAL`; pena compuesta; `FRONTERA` |
| Hermosillo, un sentenciado, **25 años**, «asesinato» por titular | Tribuna 2026/10/16 + Diario del Yaqui (sin fecha) → Bajo; sin boletín → pendiente; `FRONTERA`; **no es** Tribuna 2026/08/04 ni Telemax 2026/08/05 |
| Veracruz, homicidio de un periodista, 21 años (J-10/2026) | Publicada el 15: ventana de 134. Dos personas distintas en el caso (un primer implicado detenido en 2022 y el sentenciado, segundo detenido): **sin homonimia** si se mantienen separadas |
| FGR Cosoleacaque (4 años, multa 9,348 pesos) y Banderilla (2 años 6 meses, 83 UMA = 9,736 pesos, por resumen) | Primera publicación 15-oct (La Nigua, Hora Cero): ventana de 134. **Multas distintas: dos casos** |
| CDMX, Diego «N» y Abdiel «N» | Publicada 14-15 oct; sin boletín indexado |
| Nuevo León, 155 años | MVS 2026/10/13: anterior |
| Colima, 27 años por secuestro (abreviado) | Boletín del 9-oct por resumen: anterior |
| Querétaro (5, 6 y 8-oct) · Tamaulipas FGJE-370 (6-oct) · Oaxaca 2,889 (13-oct) | Anteriores |
| Sonora, Nogales, 15 años | Sin fecha en ruta; 12-oct por resumen |

## 12. Desglose de cálculos propios

- **Muertos en hechos propios**: Culiacán 2 + Culiacán 1 + Tijuana 2 + Apatzingán 3 + Apatzingán 1 + Hermosillo 1 + Hermosillo 1 + Colima 1 = **12**. Heridos integrados: **0**. Localizados con vida: **6**.
- **Armamento**: **sin total nacional verificable**. ARM-001 (publicado: 3 cortas, 1 ametralladora, 16 cargadores, 417 cartuchos, 4 detenidos) y ARM-002 (1 larga) **en ceros hasta validación**.
- **Duración**: 16-oct 11:34 → 17-oct 09:28 = 21 h 54 min. **Densidad**: 13 / 21,9 h = 0,594 → **0,59**.
- **FRONTERA**: 11 de 13 (`-003` a `-013`).

## 13. Los dos controles editoriales

**Primera ronda** (sobre `4409633`, con las notas íntegras de los seis equipos; informes en el *scratchpad*: `control-procedencia-r1.md`, `control-duplicidad-r1.md`):

- **`procedencia-cifras`**: veinte hallazgos, **diecisiete «CORREGIR»** (4, 13, 14 sin hallazgo); 30 búsquedas. **Aplicados todos** (1-3, 5-12, 15-20 y ajustes A-F): rutas solo con mes fuera de «fechadas» (Tijuana), «encobijados» solo para dos (Apatzingán), Gala Residencial y López Mateos por resumen, ametralladora sin categoría, detenido de Mazatlán fuera del conteo, recuentos de Ajuchitlán y Tepic, Ensenada 158 años (+9 meses por resumen), Hermosillo «asesinato» y homonimia, techo ★★★★☆ de política. **Hechos nuevos**: La Costerita (`-007`), Cachanillas (`-REC-003`), Nogales (`-REC-004`); el coordinador añadió CDMX (`-012`). **Renumeración**: Pokémon `-007`→`-008`, cateos `-008`→`-009`, Ajuchitlán `-009`→`-010`, Tepic `-010`→`-011`. El Tívoli: no se ficha (sin fecha en ruta), `SIN FECHA FIJADA` de 135.
- **`editor-duplicidad`**: veinte pases, **dieciséis «CORREGIR»** (3, 12, 16, 17 sin hallazgo). **Aplicados**: 1 y 2 (armamento en ceros por posible duplicidad con `ARG-134-ARM-001` y posible evento anterior del boletín del 15-oct: **sin total nacional verificable**), 4 (portada 1 sin balística; conclusiones 1, 2, 4 y 5 reescritas), 5 (mecanismo retirado del panorama, de la cobertura, del mapa y de la tarjeta de sentencias), 6 (deslindes sin color), 7 (vistos añadidos en §10), 8 (confianza Bajo en `-008` y `ARM-001`), 9a (`gen-texto.py` captura los subtítulos con `style`), 10 (`-008` impacto mediano), 11 (tooltip: «Fecha y hora (hecho o publicación)» y «Consulta» real; `-001` publicado el 16 por ruta, hecho por resumen), 13 (`FRONTERA` en Hermosillo 25 años), 14 (R de `-001` 7 y de `-003` 4), 15 (armamento 5 + 6 + 21), 18 (FE-001 recalculado, FE-002 con fosas, seguimientos de 134-002 y 134-REC-002), 19 (este archivo), 20 (índice y pendientes). **No aplicado, con motivo**: 9b (frase «Toque un ARG-ID» y nota del móvil: convención del generador desde 128); 14c (`I=1` de `-008`: la reserva «mismo comunicado» ya consta en `campo`); el color de las filas de armamento en el mapa de aseguramientos queda verde aunque estén en ceros (el generador no admite gris por fila).

## 14. Herramientas

`tools/datos-argos-135.py` (copia de la estructura de 134) → `reports/argos-2026-10-17.html`; `gen-movil.py 135 2026-10-17 134 2026-10-16 09:28`; `gen-texto.py`; `validar.js … 2026-10-16 2026-10-17` → «validación OK».

## 15. Lecciones de método (no van al cartelón)

1. **El coordinador volvió a fijar los rojos**: los dos hechos con dos muertos del 16 (Culiacán, Tijuana) llegaron de la ola sin ruta fechada; una búsqueda dirigida por topónimo los ancló.
2. **El índice del buscador no llega a la noche del viernes 16 ni al sábado 17** en Golfo, Centro y Noreste: el corte se sostiene en hechos de la tarde del 16.
3. **Los encargos de 134 se resolvieron casi todos por exclusión o por mayoría**, no por fragmento: Silao (el 14 era otro hecho), Tres Cerritos (hora antes de las 11:34), Almoloya (domingo), Irapuato (madrugada).
4. **Sonora y Sinaloa: octava edición sin dominio de fiscalía devuelto.** El `site:` encadenado con `OR` hace que el buscador ignore el operador: consultar cada dominio por separado.


**Segunda ronda** (sobre `1feb68e`, sin búsquedas; informes `control-procedencia-r2.md`, `control-duplicidad-r2.md`):

- **`procedencia-cifras`**: veinte hallazgos, diecinueve «CORREGIR» (4 sin hallazgo). **Aplicados**: 2 (paneles y tarjetas de armamento: «publicado, fuera del total»), 5, 6, 7 (`-002` a ★★☆☆☆ y R 4; TV Azteca BC, agregado), 8 (La Costerita con titulares), 9 (**El Tívoli fichado** como `-013`), 11 (recuentos de las recuperaciones), 12 (22 o 23 días, contradicho), 13 (Tepic: identidad del caso por resumen), 14 (topónimos de resumen marcados), 15 (Ensenada «asesinato» por titular), 16 (índice con sufijo «pub.»), 17, 18 (armamento 3 + 8 + 21; Oaxaca publicó), 19, 20 (rango condicionado de 133). **No aplicados, con motivo**: 1 y 10 (el control no vio las búsquedas del coordinador: el *slug* de La Nigua y el titular de Infobae de la CDMX existen; URL añadidas en §2 y §7); 3 (la fila de totales conserva los ceros: la leyenda `SIN TOTAL NACIONAL VERIFICABLE DURANTE EL CORTE` va en la nota inmediata y la regla de iconografía exige mostrar los ceros).

## 16. Emisores por ficha (lista íntegra)

- `ARG-135-001` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: Línea Directa (2026-10-16), Luz Noticias (2026-10-16) · Recuento I 0 / N 0 / R 7 / A 0
- `ARG-135-002` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: ninguna · Recuento I 0 / N 0 / R 4 / A 0
- `ARG-135-003` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: ninguna · Recuento I 0 / N 0 / R 4 / A 0
- `ARG-135-004` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: Red Michoacán (2026/10/17), Grupo Marmor (2026/10/17) · Recuento I 0 / N 0 / R 4 / A 0
- `ARG-135-005` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: Proyecto Puente (2026/10/17) · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-135-006` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: Proyecto Puente (2026/10/16) · Recuento I 0 / N 0 / R 1 / A 0
- `ARG-135-007` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: ninguna · Recuento I 0 / N 0 / R 5 / A 0
- `ARG-135-013` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: ninguna · Recuento I 0 / N 0 / R 3 / A 0
- `ARG-135-008` — Institucional: Gabinete de Seguridad (comunicado por cita) · Nacional: Infobae · El Financiero · MVS · Publimetro · Crónica · Con fecha en la ruta: Infobae (2026/10/16), El Financiero (2026/10/16), MVS Noticias (2026/10/16), Tribuna (2026/10/16), Publimetro (2026/10/16), Crónica (2026/10/16) · Recuento I 1 / N 5 / R 5 / A 0
- `ARG-135-009` — Institucional: Gabinete de Seguridad (por cita) · Nacional: El Heraldo de México · El Universal · López-Dóriga · Con fecha en la ruta: El Heraldo de México (2026/10/16), El Diario de Chihuahua / diario.mx (2026/oct/16), Línea Directa (2026-10-16) · Recuento I 0 / N 3 / R 2 / A 0
- `ARG-135-010` — Institucional: Defensa (por cita) · Nacional: El Heraldo de México · Proceso · Infobae · Con fecha en la ruta: El Heraldo de México (2026/10/16), Proceso (2026/10/16), Tribuna (2026/10/16), Quinto Poder (2026/10/16), Infobae (2026/10/17) · Recuento I 1 / N 3 / R 2 / A 0
- `ARG-135-011` — Institucional: Gobierno de Nayarit (comunicado por cita) · Nacional: Infobae · Con fecha en la ruta: Infobae (2026/10/16), Meridiano (2026/10/17), Relatos Nayarit (2026/10/17) · Recuento I 1 / N 1 / R 2 / A 0
- `ARG-135-012` — Institucional: SIN BOLETÍN · Nacional: Infobae · Milenio · Con fecha en la ruta: Infobae (2026/10/17) · Recuento I 0 / N 2 / R 0 / A 0
- `ARG-135-REC-001` — Institucional: FGJ Nuevo León (por cita) · Nacional: MVS · Milenio · Con fecha en la ruta: El Mañana (2026/10/15), MVS Noticias (2026/10/16), Punto x Punto (2026/10/16), Enfoque Monterrey (2026/10/17) · Recuento I 1 / N 2 / R 5 / A 0
- `ARG-135-REC-002` — Institucional: SIN BOLETÍN · Nacional: La Silla Rota · Con fecha en la ruta: La Silla Rota (2026/10/13) · Recuento I 0 / N 1 / R 4 / A 0
- `ARG-135-REC-003` — Institucional: SIN BOLETÍN · Nacional: N+ · Con fecha en la ruta: Tijuana en Línea (2026/10/16), El Imparcial (2026/10/16), Opinia (2026/10/16), Lindero Norte (2026/10/16) · Recuento I 0 / N 1 / R 5 / A 0
- `ARG-135-REC-004` — Institucional: SIN BOLETÍN · Nacional: ninguna · Con fecha en la ruta: El Imparcial (2026/10/16) · Recuento I 0 / N 0 / R 1 / A 0

Fuentes sin fecha en la ruta, por ficha (regionales salvo que se indique): `-001` Azteca Sinaloa, Meganoticias, Sinaloahoy, Noroeste, Los Noticieristas (2026/10) · `-002` Zeta (2026/10), Diario Tijuana (2026/10), Alfredo Álvarez, El Congresista (TV Azteca BC: agregado, solo corrobora) · `-003` Quadratín, El Congresista, Respuesta Michoacán, La Primera de AM · `-004` La Voz de Michoacán, Meganoticias · `-007` Noroeste, Sinaloahoy, Noticiero Altavoz, Los Noticieristas (2026/10), Extraoficial · `-013` AFmedios, Meganoticias, Vadenuez · `-008` La Nigua (*slug* con «ametralladora y 417 cartuchos»), Maya Comunicación, Quadratín México, Posta, Tribuna (2026/10/16) · `-009` El Diario de Chihuahua/diario.mx, Línea Directa · `-010` Tribuna, Quinto Poder, Récord · `-012` Milenio (nacional) · `-REC-001` El Porvenir, Telediario · `-REC-002` News Hidalgo, Énfasis, Criterio Hidalgo, Quadratín Hidalgo · `-REC-003` Infobaja.

### Segunda ronda — `editor-duplicidad`

Veinte pases sobre `1feb68e`, dieciocho «CORREGIR» (10 y 11 sin hallazgo). Varios ya estaban resueltos en `f0a4f51` (2 parcial, 5, 6 de `-002`, 7a, 9, 16b). **Aplicados**: 1 (Valoración 5: `-008` y `-009` verdes con reserva), 2 (tarjetas sin cifras no integradas; lectura regional «sin lectura»), 3 (`EVENTOS_ARM` vacío: Sinaloa gris en el mapa de aseguramientos; pie sin explicación de color), 4 (`ARM-002`: Marina solo por resumen), 5 (`-010` R 3 con Récord), 6 (`-010` a ★★☆☆☆; campo de `-001`), 7b (Piedras Negras cotejado, §7) y 7c (Tezontepec: encargo de 134), 8 (Ensenada: desarrollo de 131 y 134), 9 (verificar Almoloya contra las fuentes de 130), 12 (definiciones fuera del panorama; tarjeta de detenidos), 13 (deslindes sin justificación de agravante; «Agencia Estatal de Investigación» en lugar de «AEI»), 14 (introducción de armamento y «once de trece» del panorama retiradas; conclusión 2 reescrita), 15 (conclusiones 4 y 5), 16a (renglón de páginas no disponibles), 17 (§5 con ARG-ID completos; índice con marcas de duda), 19 (Taxco y Barrio 18 descartados con motivo; El Tripa `SIN FECHA FIJADA`; pendientes completados), 20 (`CONSULTA_TXT` se reemplaza si la plantilla ya lo trae: probado con la plantilla de 135 → «validación OK»; extractor y plantilla de equipos copiados a `tools/`). **No aplicados, con motivo**: 18 (orden de encabezados en `gen-texto.py` y frases del móvil en `gen-movil.py`: cambio de herramienta que afecta a todas las ediciones; pasa a deuda de método de 136).
