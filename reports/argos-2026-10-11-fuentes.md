# ARGOS 129 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-11 · **Ventana**: 2026-10-10 09:08 → 2026-10-11 08:58 CDMX · **23 h 50 min**
**Rama**: `claude/argos-129` (partió de `origin/main` = `b0558a3`).

---

## 1. La base

Bloque 0 ejecutado dos veces. A las **01:01 CST** del 11-oct: el clon arrancó en `60f2777` (por detrás de `origin/main`, como en 128);
`git merge --ff-only origin/main` avanzó en fast-forward `60f2777 → b0558a3` («ARGOS 127 y 128 mergeadas a main (#14)»); `argos-127` y
`argos-128` respondieron «Already up to date». Estado: `argos-2026-10-10` (ARGOS 128) y **147 archivos** en `reports/`, lo previsto. El
destinatario aplazó el arranque a las 05:00 para tener más información; el arranque real fue a las **08:58 CST**, con el Bloque 0
repetido (sin cambios). HEAD suelto: se abrió `claude/argos-129`.

| Serie | 124 | 125 | 126 | 127 | 128 | **129** |
|---|---|---|---|---|---|---|
| Duración | 46 h 19 | 320 h 34 | 17 h 41 | 22 h 24 | 25 h 48 | **23 h 50** |
| Densidad (hechos/h) | 0,30 | 0,16 | 0,40 | 0,27 | 0,23 | **0,29** (7 / 23,83, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (10 y 11-oct). El generador lo comprueba con `assert`.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** a las 01:01 y a las 08:58; el proxy registra `www.gob.mx:443 — connect_rejected`
  (política de la organización). Un `WebFetch` de un agente a `seunonoticias.mx` → `ENOTFOUND`. **Ningún documento leído íntegro.**
  Techo **★★★☆☆**, undécima edición.
- **Consulta de control** (Pinotepa Nacional, Hamurabi Huesca, en los dos modos): `standard` **no encontró el caso** —devolvió el ataque
  a otro periodista de Pinotepa en marzo—; `extended` trajo la cobertura del 9-10 oct con la línea de la FGEO. **Se mantuvo `extended`
  obligatorio.**
- **Presupuesto**: control 2 + una ola de **nueve equipos** (encargos 18, boletín federal 18, seguimientos 18, Noroeste 20, Noreste 18,
  Occidente 18, Centro 20, Golfo 14, Sureste 20 = **164**) + **8 del coordinador** = **174**; `procedencia-cifras` con tope de **25** → techo **199**.
- **Rendimiento del coordinador**: las dos búsquedas nacionales por día («sábado 10 de octubre», «domingo 11 de octubre») hallaron
  **Minatitlán** y **Chipilo**, que después confirmaron los equipos del Golfo y del Centro. Las otras seis: afinado de Minatitlán, Chipilo,
  comunicado de la SEMAR, Escuinapa, Zamora y Las Porras.

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — Yucatán (tres módulos) | **Revisada en los tres**: alto impacto en medios (SRIV); armamento `site:yucatan.gob.mx` y `ssp.yucatan.gob.mx` (SRIV); sentencias `fge.yucatan.gob.mx` (SRIV). **Se salda la deuda de 128** |
| Prioridad — armamento | **Revisadas (SRIV)**: Sin (`sspsinaloa.gob.mx`), Col (`fgecolima.mx`), Ver (`veracruz.gob.mx/seguridad`, dominio real; `ssp.veracruz.gob.mx` no existe en el índice), Camp (`spsc.campeche.gob.mx`). **NO REVISADA**: **Tlax (cuarta edición: `ssc.tlaxcala.gob.mx` no devolvió páginas)**, BC, Coah, SLP (dominio SSP no confirmado), Nay, Edomex, Qro |
| Prioridad — sentencias | **Revisadas (SRIV)**: Coah (débil, solo PDF), SLP (`fiscaliaslp.gob.mx`), Zac (`fiscaliazacatecas.gob.mx`), Col (`fgecolima.mx`), Nay (`fiscaliageneral.nayarit.gob.mx`), Edomex (`fgjem.edomex.gob.mx`), Chis (`fge.chiapas.gob.mx`). **NO REVISADA**: Son (`fiscalia.sonora.gob.mx` no devuelto), Sin (`fiscaliasinaloa.gob.mx` no devuelto), Camp (`fiscalia.campeche.gob.mx` y `fgecampeche.gob.mx` no devueltos) |
| Prioridad — alto impacto | Qro y Chis revisadas (medios); **BCS NO REVISADA por segunda edición** |
| Ciclo | **A** — Noroeste + Centro encabezaron el triaje judicial |
| Rendimiento | **Ninguna sentencia integrable.** El ciclo A halló **Navolato, 80 años** (Noroeste, publicado el 10-oct, solo medios) y **Operación Enjambre** (Centro, agregado del 10-oct, solo medios), además del veredicto de Ensenada (no sentencia) |

Serie: C (125) sí · A (126) no · B (127) no · C (128) no · **A (129) no — candidatos, sin integrable.**

Dominios confirmados en 129 (devolvieron páginas): `fge.yucatan.gob.mx`, `yucatan.gob.mx`, `spsc.campeche.gob.mx`, `fge.chiapas.gob.mx`,
`fiscaliaguerrero.gob.mx`, `fgecolima.mx`, `fiscaliageneral.nayarit.gob.mx`, `comunicacion.fiscaliamichoacan.gob.mx`,
`fiscalia-aguascalientes.gob.mx`, `boletines.guanajuato.gob.mx`, `fiscalia.jalisco.gob.mx`, `fgjem.edomex.gob.mx`,
`fiscaliageneralqro.gob.mx`, `fiscalia.puebla.gob.mx`, `fiscaliamorelos.gob.mx`, `pgjtlaxcala.gob.mx` (un PDF de 2023),
`veracruz.gob.mx/seguridad`, `comunicacion.fiscaliaveracruz.gob.mx`, `tabasco.gob.mx`, `fiscaliatabasco.gob.mx`, `fiscaliaslp.gob.mx`,
`fiscaliazacatecas.gob.mx`, `ssp.zacatecas.gob.mx`, `fgjtam.gob.mx`, `fiscaliageneralcoahuila.gob.mx` (PDF), `fgebc.gob.mx`,
`sspsinaloa.gob.mx`, `fiscalia.durango.gob.mx`. **No confirmados**: `ssc.tlaxcala.gob.mx`, `pgjhidalgo.gob.mx`, `fiscaliaoaxaca.gob.mx`,
`fiscaliaquintanaroo.gob.mx`, `fiscalia.campeche.gob.mx`, `fgecampeche.gob.mx`, `fiscalia.sonora.gob.mx`, `fiscaliasinaloa.gob.mx`,
`fiscaliagto.gob.mx`, `ssp.veracruz.gob.mx`, dominio de la SSP SLP, `gabinetedeseguridad.gob.mx`.

## 4. Boletín federal — triple consulta

| Acciones de | Publicado | Estado | Formato |
|---|---|---|---|
| 8-oct (cotejo) | 9-oct | Localizado (ARGOS 128) | diario, 6 entidades |
| **9-oct** | — | `SIN RESULTADO INDEXADO EN VENTANA`: día suelto («acciones relevantes» y «acciones destacadas»), rangos «7, 8 y 9», «9 y 10», «9, 10 y 11», título sin `site:` (Milenio, Ahora Noticias) | — |
| **10-oct** | — | `SIN RESULTADO INDEXADO EN VENTANA`: día suelto, rangos, título. Consulta del 11-oct por la mañana: el boletín suele salir por la tarde | — |

`gob.mx/sspc` por `site:`: devuelve el dominio, nada de octubre. `gabinetedeseguridad.gob.mx`: el buscador no devolvió el dominio → `NO REVISADA`.
GN, Defensa y Marina: consulta agrupada → `NO REVISADA`. **El comunicado de la SEMAR del 10-oct** (sur de Sinaloa) se alcanzó por medios
(La Razón, Línea Directa, Noroeste, Extraoficial, Los Noticieristas, N+).

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Pinotepa Nacional** (`ARG-128-001`) | **Sin acto nuevo.** Cifra **sigue contradicha**: «tres muertos» por titular (Diario Puntual 2026/10/10, Noticierog, Noventagrados); «dos muertos y un lesionado —hombre—» solo por resumen (Reto Diario 2026/10/09). Un resumen sin medio nombrado dice que el presunto blanco murió ~18:20 en el hospital (reconciliación posible, **no verificada**). **Hora**: no fijada («hacia las 16:00» desmentida). **FGEO**: disputa entre células; blanco, alias «El Darío» (iniciales D.A.S.A.); cruce 13a. Sur y 9a. Poniente — todo por resumen; comunicado primario no localizado. **Detenidos**: ninguno. **Mecanismo**: solo «se ha solicitado la intervención» (un medio, resumen). Artículo 19 pide la línea periodística (Noticias SIN 2026/10/10) |
| **Penal El Castillo** (`ARG-127-004`, `ARG-128-004`) | **Sin acto nuevo en ventana**; sin tercera riña indexada. Segunda riña: **hora no fijada** (la SSP «no precisa la hora», por resumen; Reforma publica a las 10:05). Fuentes fechadas: La Jornada, El Financiero, El Diario, AM 2026/10/09. **Ingreso de armas**: la FGE lo investiga (titular de Los Noticieristas); Luz Noticias 2026-10-09, titular, «disparos con arma corta y larga»; 9 mm y posible trabajador, por resumen. **Detenidos y traslados**: ninguno publicado. Visitas reanudadas; titular de Infobae 2026/10/10, «muerte de 12 presos» (10 + 2: coincide con lo publicado; **sin fe de erratas**) |
| **San José del Rincón** (`ARG-128-003`) | **Ninguna fuente con fecha en la ruta, por segunda edición** (Quadratín Edomex, TresPM, Digital Mex 71518, Cuestión de Polémica, Directiva). Tampoco se acredita el 8-oct. **Se mantiene en 128 con su marca `FRONTERA` y ★★☆☆☆**. «Cuatro armas cortas» aseguradas por la FGJEM: un medio, solo por resumen → no se integra |
| **Literales del boletín del 8-oct** | **No aparecen**: ver §8, `ARG-129-FE-001` |
| **El Balcón** (`ARG-125-051`) | **Sin peritaje oficial publicado** del video (no se describe su contenido). Amparo 412/2026: sin informe de cumplimiento público. Recompensa de 1.5 mdp, tres titulares del 9-oct. Marcha a Palacio Nacional anunciada (titular de El Universal), **realización no confirmada**. Sin localizaciones ni detenidos nuevos |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| **Naucalpan** (`-005`, `-006`) | Noche del 8 o del 9: **sin información verificable**; la publicación del 9-oct es lo único fechado. Se mantiene `FRONTERA` |
| **Celaya** (`-002`) | Cifra de la Secretaría de Seguridad y Paz: **no localizada**; «un arma» (resumen) frente a «armas» (titular) sigue sin arbitrar; quién disparó: sin información |
| **Michoacán, 12 cateos** (`-REC-008`) | Crónica y Sociedad Noticias 2026/10/09 en la ruta; Infobae 2026/10/10. **4 armas sin tipo**, solo por resumen. Comunicado SSPC replicado por un republicador sin fecha (Edomex al Día). El gobernador: «más de 10 detenidos» (resumen). Relación con Sol Naciente: **sin información** |
| **Sombrerete** (`-REC-010`) | 185 (La Nigua, titular) frente a 39 detonadores (Imagenzac/NTR, resumen): **no arbitrado**; todas las fuentes hablan de **un solo cateo**; **ningún detenido en Sombrerete** (los dos del titular conjunto son de Apodaca) |
| **Borja–Nonoava** | **Sin segunda fuente**: sigue `POSIBLE DUPLICIDAD CON ARG-126-REC-004` |
| **«El Moco»** (`-REC-006`) | **Fijado: 8-oct** (Medios OBSON 2026/10/08 en la ruta; Canal 44, «jueves 8», por resumen). **Cerrado** |
| **Querétaro, Corregidora** | Boletín oficial 2026/10/08; hora de publicación no fijada; algunos medios lo fechan el 7-oct. **Sigue sin asignarse a 127**; no entra en 129 |
| **Coatzacoalcos** | Vinculación del **9-oct** por dos fuentes con fecha (Golpe Político, La Silla Rota); el 5-oct fue la imputación (Noticias Veracruz 2026/10/05). Ventana 128; seguimiento, no se ficha |
| **Zihuatanejo · Mixtequilla · Comonfort · Hermosillo** | **NO REVISADOS** (tope). Pasan a 130 |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Minatitlán** (`ARG-129-001`) | 🔴 por **ataque a infraestructura crítica**: agresión armada contra el personal de vigilancia en el acceso de una refinería. El saldo (1 muerto y 1 herido, seis titulares, frente a «dos lesionados» de Pemex, dos titulares) **no mueve el color**; sí fija la confianza |
| **Chipilo** (`ARG-129-002`) | 🟡 por **quién inicia**: la policía intenta una revisión y es repelida. Sin muertos del personal. Si se acredita emboscada, sube |
| **Escuinapa** (`-003`, `-004`) | Dos fichas: el titular de Línea Directa 2026-10-10 los da como **«dos ataques»**. 🟡 cada uno por homicidio doloso único. `FRONTERA`: publicados el 10-oct sin hora del hecho —el «tarde» del primero es solo por resumen— |
| **Comunicado de la SEMAR del 10-oct** (`-005`, `-006`) | Cinco eventos sin fecha publicada. **Las Porras** (agresión a marinos, 1 detenido, 1 larga, 29 cartuchos, por resumen): 🟡, porque «fueron agredidos» no acredita emboscada ni patrullaje; la regla manda amarillo cuando no se determina quién inició. **Varados y Siqueros** (7 AEI inhabilitados): 🟢. **Rincón de Higueras, El Rosario** (103 mil dosis): 4-oct, ya publicado el 5-oct → `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, no fichado. **Infonavit Playas** (1 detenido, dosis): sin armamento, mencionado en `-006`. El agregado de 8 largas, 67 cargadores y 215 cartuchos **no se atribuye por evento** y no se integra salvo Las Porras. Todo `FRONTERA` |
| **Pachuca, Las Lajas** (`-007`) | 🟢; fuente única con fecha; sin armamento: no entra en la tabla de armamento |
| **Zamora** (`ARG-129-REC-001`) | Bar El Nuevo Quijote, **viernes 2-oct ~23:00**: dentro de la ventana de **ARGOS 125** (24-sep → 7-oct), que no lo publicó; no figura en el índice. `-REC-` 🔴. Fe de erratas en §8 |
| **Culiacán, Los Pinos** (`-REC-002`) | El operativo **inicia la noche del 9-oct** (ventana de 128) y sigue la mañana del 10; no se acredita que el aseguramiento terminara después de las 09:08. `-REC-` con origen 128, cualitativo |
| **Escobedo** (`-REC-003`) | «Madrugada de este sábado» 10-oct: anterior a la apertura. `-REC-` con origen 128; fuentes sin fecha en la ruta |
| **Navolato, 80 años** | Sentencia publicada el 10-oct; el *slug* «obtiene-fiscalia-de-sinaloa-sentencia-condenatoria…» está en un **medio** (Noticiero Altavoz), no en el dominio oficial → `PENDIENTE DE CONFIRMACIÓN OFICIAL` (umbral asimétrico) |
| **Ensenada** | **Veredicto de culpabilidad** del 9-oct; individualización de sanciones el 16-oct: **no es sentencia** |
| **Papantla** (equipo del Golfo) | Ya publicado como `ARG-128-REC-001`: el equipo no lo cotejó. Infobae y Plumas Libres 2026/10/10 añaden «posible cobro de piso» (resumen): sin cambio |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-129-FE-001`** — **umbral de cifras arrastradas** sobre el boletín del 8-oct (`ARG-128-REC-003`, `-004`, `-005`): segunda edición
  solo por resumen. Se retiran: **Río Bravo** 2 armas largas, 225 cartuchos, 8 cargadores —se conserva «48 ponchallantas», titular de Hoy
  Tamaulipas 629359, y «armas» sin cantidad—; **Ciudad Juárez** 81 cartuchos y 4 cargadores —se conserva, por *slug* de Puente Libre,
  «arrestaron a pareja… les aseguraron cargadores»: **2 detenidos** y cargadores sin cantidad—; **Valle de Santiago** 55 cartuchos y 2 detenidos.
  Todos: `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`.
- **Armamento recalculado de la ventana de 127**, cálculo propio, tras FE-004 (128) y FE-001 (129): largas **0** · sin categoría **1** (Zacatlán)
  · cartuchos **0** · cargadores **0** · detenidos en evento de aseguramiento **6** (SLP 3, por titular; Juárez 2, por *slug*; Zacatlán 1).
- **`ARG-129-FE-002`** — sobre **ARGOS 125**: un hecho no publicado, `ARG-129-REC-001` (Zamora, 2-oct). Efecto sobre el semáforo de 125: rojos
  **+1**; muertos **+4**, heridos **+3**.
- **`ARG-129-FE-003`** — sobre **ARGOS 128**: dos hechos no publicados, `ARG-129-REC-002` (Culiacán, Los Pinos) y `-REC-003` (Escobedo). Efecto
  sobre el semáforo de 128: verdes 0 → **2**. Armamento de 128: Escobedo añadiría 1 corta, 1 cargador, 15 cartuchos y 2 detenidos, **solo por
  resumen**; Los Pinos, cualitativo.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | NO REVISADA | NO REVISADA | SRIV (`fgebc.gob.mx`) · veredicto de Ensenada |
| Baja California Sur | NO REVISADA (segunda edición) | NO REVISADA | NO REVISADA |
| Sonora | NO REVISADA (Palo Fierro sin URL) | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Chihuahua | NO REVISADA | NO REVISADA | NO REVISADA (sin `site:`) |
| Sinaloa | **hechos** (Escuinapa ×2, Las Porras, Varados) · REC Los Pinos | SRIV (`sspsinaloa.gob.mx`) · **hechos SEMAR** | NO REVISADA (dominio no devuelto) · Navolato, solo medios |
| Durango | NO REVISADA | NO REVISADA | SRIV (`fiscalia.durango.gob.mx`; 5 y 7-oct) |
| Coahuila | NO REVISADA | NO REVISADA | SRIV débil (PDF) |
| Nuevo León | SRIV · REC Escobedo | NO REVISADA | NO REVISADA · candidato del 10-oct, solo medios |
| Tamaulipas | SRIV | NO REVISADA | SRIV (`fgjtam.gob.mx`; FGJE-381 del 10-oct, Matamoros, **sin leer**) |
| San Luis Potosí | SRIV | NO REVISADA (dominio SSP no confirmado) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | SRIV | SRIV (`ssp.zacatecas.gob.mx`) | SRIV (`fiscaliazacatecas.gob.mx`) |
| Jalisco | SRIV | NO REVISADA | SRIV (`fiscalia.jalisco.gob.mx`) |
| Colima | SRIV | SRIV (`fgecolima.mx`) | SRIV (`fgecolima.mx`) |
| Nayarit | SRIV | NO REVISADA | SRIV (`fiscaliageneral.nayarit.gob.mx`) |
| Aguascalientes | SRIV | SRIV | SRIV (`fiscalia-aguascalientes.gob.mx`) |
| Michoacán | SRIV · REC Zamora | NO REVISADA | SRIV (`comunicacion.fiscaliamichoacan.gob.mx`) |
| Guanajuato | SRIV | SRIV (`boletines.guanajuato.gob.mx`) | NO REVISADA (dominio no devuelto) |
| Ciudad de México | NO REVISADA | NO REVISADA | NO REVISADA |
| Estado de México | SRIV (medios) | NO REVISADA | SRIV (`fgjem.edomex.gob.mx`) · Enjambre, solo medios |
| Morelos | SRIV | NO REVISADA | SRIV (`fiscaliamorelos.gob.mx`) |
| Puebla | **hecho** (Chipilo) | NO REVISADA | SRIV (`fiscalia.puebla.gob.mx`) |
| Tlaxcala | NO REVISADA | **NO REVISADA (cuarta edición)** | SRIV débil (`pgjtlaxcala.gob.mx`) |
| Hidalgo | SRIV · **hecho** (Pachuca) | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Querétaro | SRIV | NO REVISADA | SRIV (`fiscaliageneralqro.gob.mx`) |
| Veracruz | **hecho** (Minatitlán) | SRIV (`veracruz.gob.mx/seguridad`) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | SRIV | SRIV (`tabasco.gob.mx`) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | SRIV | NO REVISADA | SRIV (`fiscaliaguerrero.gob.mx`) |
| Chiapas | SRIV | NO REVISADA | SRIV (`fge.chiapas.gob.mx`) |
| Oaxaca | SRIV (seguimiento Pinotepa) | NO REVISADA | NO REVISADA (dominio no devuelto) |
| Campeche | NO REVISADA | SRIV (`spsc.campeche.gob.mx`) | NO REVISADA (dominio no devuelto) |
| Yucatán | SRIV | SRIV | SRIV (`fge.yucatan.gob.mx`) |
| Quintana Roo | SRIV | NO REVISADA | NO REVISADA (dominio no devuelto) |

**Sentencias: 21 de 32 + FGR; 11 `NO REVISADA`.** **Armamento: 9 de 32** (Sin, Zac, Col, Gto, Ags, Ver, Tab, Yuc, Camp) — **caída desde 20**:
los equipos del Centro, Noroeste y Noreste no hicieron `site:` de armamento en la mayoría de sus entidades. **Alto impacto: 23 de 32.**

## 10. Hechos vistos y NO fichados, con motivo

| Hecho | Motivo |
|---|---|
| Sinaloa, El Rosario, 103 mil dosis | 4-oct, publicado el 5-oct (Línea Directa 2026-10-05) |
| Sinaloa, Culiacán col. Independencia, mujer baleada; Sonora, Hermosillo, Palo Fierro | Sin URL de nota; solo por resumen |
| Sinaloa, Concordia, más de 80 AEI (8-oct) | `POSIBLE DUPLICIDAD` con `ARG-126-004` (Pánuco) |
| Sinaloa, La Costerita, vinculación de 4 | Seguimiento procesal |
| Tlaxcala, Tetlatlahuca, 1 arma y 7 cartuchos; Chiautempan, FGR | Sin fecha en la ruta; vinculación no es sentencia |
| Querétaro, Santa María Magdalena, 3 cortas | Vinculación del 8-oct; fecha del cateo no fijada |
| Edomex, Operativo Otomí | Acumulado sin periodo ni municipios; 1,311 frente a 1,360 detenidos |
| SLP, parte de 24 h del 9-oct | Agregado estatal sin desglose por evento |
| Michoacán, Los Reyes, 5 cateos; Guanajuato, Huanímaro (1-oct) | Fecha no fijada / ventana 125; candidatos para cotejo en 130 |
| Sonora, FGR Nogales, 3 años 2 meses | «11 de octubre» solo por resumen, sin URL |
| Yucatán, Montes de Amé, prisión preventiva | Medida cautelar, no sentencia; ventana anterior |
| Tamaulipas, Frontera Chica, despliegue | Informativo; ventana anterior |

## 11. Desglose de cálculos propios

- Duración: 10-oct 09:08 → 11-oct 08:58 = **23 h 50 min** = 23,83 h. Densidad: 7 / 23,83 = **0,29**.
- Muertos en hechos propios: 1 (Minatitlán, contradicho) + 1 + 1 (Escuinapa) = **3**. Heridos: 1 (Minatitlán) + 1 (Chipilo) = **2**; con la versión de
  Pemex, **2 muertos y 3 heridos**.
- Armamento propio: largas 1, cartuchos 29, AEI 7, detenidos 1 — todas solo por resumen.
- Recuperaciones por color de origen: 🔴 1 (Zamora) · 🟢 2 = **3**.
- Frontera: 5 de 7 (`-003` a `-007`).

## 12. Fuentes por ficha

- **`ARG-129-001`** — La Silla Rota 2026/10/10 (532488); Infobae 2026/10/11; Milenio (dos notas); López-Dóriga; Expreso 266224; Azteca Veracruz; Tiempo; El Universal («dos lesionados»); SDP («Pemex confirma dos trabajadores lesionados»). Infobae «EN VIVO» 11-oct: *liveblog*.
- **`ARG-129-002`** — Síntesis 2026/10/10; Infobae 2026/10/11; Puebla Online 166599; Quadratín Puebla; El Universal Puebla; Meganoticias 778011; N+ (Foro TV); Ambas Manos 354674; Curul; Quince Minutos; Oronoticias; El Congresista («11 de octubre»).
- **`ARG-129-003`** — Línea Directa 2026-10-10__1718001; Los Noticieristas 2026/10 (1146166); Azteca Sinaloa.
- **`ARG-129-004`** — Línea Directa 2026-10-10__1718001 (titular «En dos ataques privan de la vida a vendedora de birria y a joven en un taller en Escuinapa»).
- **`ARG-129-005` / `-006`** — La Razón 2026/10/10; Línea Directa 2026-10-10__1717862; Noroeste JC26245851 y BP26384621; N+; Extraoficial; Los Noticieristas 1142362; Sinaloahoy; Noticiero Altavoz.
- **`ARG-129-007`** — La Silla Rota 2026/10/10 (532437).
- **`ARG-129-REC-001`** — Latinus 2026/10/3 (185995); El Financiero 2026/10/04; PorEsto 2026/10/3; Diario de Yucatán 2026/10/03; ABC Noticias 2026/10/3; Correo 2026/oct/04; Grupo Marmor 2026/10/03; Síntesis 2026/10/03; Tiempo.
- **`ARG-129-REC-002`** — Línea Directa 2026-10-10__1717866; Los Noticieristas 1146043; N+; El Universal; Sinaloahoy; Blog del Narco (`NO OFICIAL`).
- **`ARG-129-REC-003`** — Consulta Monterrey; Hora Cero; Telediario.
- **Sentencias** — Navolato: Noticiero Altavoz (*slug* institucional reproducido), Línea Directa 2026-10-10__1717897, Los Noticieristas 1146008, Azteca Sinaloa, Extraoficial; NL: MVS 2026/10/10 (749349); Enjambre: El Vigía 2026/10/10 (514524), AD Noticias; Ensenada: El Imparcial 2026/10/09, Infobae 2026/10/10, El Financiero 2026/10/10, En Línea BC 2026/10/09, La Silla Rota 2026/10/10.

## 13. Los dos controles editoriales

*(Se completa tras su ejecución sobre la versión estable.)*

## 14. Herramientas

`tools/datos-argos-129.py` (generador único) → `reports/argos-2026-10-11.html`; `tools/gen-movil.py 129 2026-10-11 128 2026-10-10 08:58`;
`tools/gen-texto.py`; `node tools/validar.js reports/argos-2026-10-11.html 2026-10-10 2026-10-11` → **validación OK**. Las filas `ARM` llevan
ahora `hora` propia (128 la tenía fija en el JSON del mapa).

## 15. Lecciones de método (no van al cartelón)

1. **Las búsquedas nacionales por día volvieron a rendir**: trajeron el único rojo (Minatitlán) antes que el equipo regional.
2. **El armamento cayó de 20 a 9 entidades revisadas**: tres equipos gastaron su tope en alto impacto y sentencias sin `site:` de armamento.
   Para 130, **cada equipo debe dedicar al menos una búsqueda `site:` de armamento por entidad** antes de cerrar.
3. **Tlaxcala armamento, cuarta edición `NO REVISADA`**: el dominio `ssc.tlaxcala.gob.mx` no aparece en el índice del buscador. Hay que buscar
   el dominio real por otra vía (p. ej., «Secretaría de Seguridad Ciudadana Tlaxcala boletín» sin `site:`).
4. **Los equipos regionales no cotejaron con el HTML de la edición anterior** (Papantla traído como nuevo). Debe exigirse en el encargo.
5. **El comunicado de la SEMAR sin fecha por evento** obliga a declarar `FRONTERA` en cadena: pedir el comunicado íntegro en 130.
