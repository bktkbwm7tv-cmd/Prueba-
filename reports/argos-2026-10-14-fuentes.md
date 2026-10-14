# ARGOS 132 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-14 · **Ventana**: 2026-10-13 07:23 → 2026-10-14 08:19 CDMX · **24 h 56 min**
**Rama**: `claude/argos-132` (partió de `origin/claude/argos-131` = `db02540`).

---

## 1. La base

Bloque 0 a las **08:19 CST** del 14-oct. El clon arrancó en `60f2777` (13 commits por detrás de `origin/main`, como en 128-131), HEAD suelto: se abrió
`claude/argos-132` antes de fusionar. `--ff-only origin/main` → `b0558a3`; `origin/claude/argos-129` → `9eaba81`; `origin/claude/argos-130` → `63c1325`;
`origin/claude/argos-131` → `db02540`. **Los cuatro merges, fast-forward.** Estado: `argos-2026-10-13` (ARGOS 131) y **165 archivos** en `reports/`, lo previsto.

| Serie | 127 | 128 | 129 | 130 | 131 | **132** |
|---|---|---|---|---|---|---|
| Duración | 22 h 24 | 25 h 48 | 23 h 50 | 23 h 21 | 23 h 04 | **24 h 56** |
| Densidad (hechos/h) | 0,27 | 0,23 | 0,25 | 0,39 | 0,26 | **0,24** (6 / 24,93, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (13 y 14-oct). El generador lo comprueba con `assert`.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (08:19). **Ningún documento oficial leído íntegro.** Techo **★★★☆☆**, decimocuarta edición.
- **Consulta de control** («ataque armado muertos 13 de octubre 2026», en los dos modos): `standard` **no encontró ningún hecho del 13-oct** —devolvió Juárez,
  Puebla, Salvatierra (febrero), Reynosa, Ecuador—; `extended` trajo **San Blas Atempa** (13-oct) y Culiacán (12-oct). **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola de seis equipos (Noroeste 30, Noreste 22, Occidente 26, Centro 30, Golfo y federal 28, Sureste 22 = **158**) + **10 del
  coordinador** (una, la fosa de Navolato, tras `procedencia-cifras`) = **170**; `procedencia-cifras` **25** → **195 de 200**. `editor-duplicidad` no busca en la web.
- **Rendimiento del coordinador**: la búsqueda nacional del **martes 13** halló **San Blas Atempa** y **Cotija**; la del **miércoles 14**, **«El Cromo»** y el
  **boletín federal del 12-oct**. Las otras: noche del martes (sin resultado), boletín del 13-oct (dos, sin resultado), FGEO 80 años, Orizaba (hora y «un civil»),
  Acaponeta (fecha y kilómetro) y, tras el control, Navolato (fosa). **La ola y el coordinador omitieron la fosa de Navolato**: la halló `procedencia-cifras`.

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (9 `NO REVISADA` en 131) | **Revisadas ahora (6)**: BCS (`bcs.gob.mx`), Son (`sonora.gob.mx`, `seguridad.sonora.gob.mx`), Chih (`sspe.chihuahua.gob.mx`), **Sin (`sspsinaloa.gob.mx`, dominio confirmado)**, Tlax (`comunicacion.tlaxcala.gob.mx`), Hgo (`hidalgo.gob.mx`, solo Periódico Oficial). **Siguen `NO REVISADA`**: Edomex (`edomex.gob.mx` no devuelto), Oax y Gro (el equipo no documentó dominio devuelto; corregido tras `editor-duplicidad`) |
| Prioridad — sentencias (14 `NO REVISADA` en 131) | **Revisadas**: **Coah (`sitio.fgecoahuila.gob.mx`, dominio confirmado; último indexado 31-ago)**, **Zac (`fiscaliazacatecas.gob.mx`, confirmado)**, Col (`fgecolima.mx`), CDMX (`fgjcdmx.gob.mx`), Mor (`fiscaliamorelos.gob.mx`), Qro (`fiscaliageneralqro.gob.mx`). **Siguen `NO REVISADA`**: BCS, **Son y Sin (quinta edición)**, Nay (`fiscalianayarit.gob.mx`: 0), Gto (`portal.fgeguanajuato.gob.mx` sin boletín), Tlax (sin dominio oficial), Hgo, Camp (`fiscalia.campeche.gob.mx` no devuelto) |
| Prioridad — alto impacto | **BCS y Dgo revisadas por búsqueda propia** (SRIV): alto impacto 32 de 32 |
| Ciclo | **A** — Noroeste + Centro encabezaron el triaje judicial tras la prioridad |
| Rendimiento | **Ninguna sentencia integrable.** El ciclo A halló Sonora (Nogales, republicadores), FGR Chihuahua (dos, republicador) y Querétaro (tres, `fiscaliageneralqro.gob.mx` con fecha en la ruta, 5 a 8-oct: **fuera de ventana**). Fuera del ciclo: Oaxaca (FGEO, 80 años), Nuevo León (155 años) y Zacatecas (10 años) |
| Regresión por rotación | Armamento: BC, Coah, NL, Tamps, SLP, Ags, CDMX, Mor, Qro, Chis, Camp, Yuc, QRoo vuelven a `NO REVISADA` (sin `site:` devuelto). Sentencias: BC, NL, SLP, Edomex, Pue, Gro, Chis, Yuc. **Prioridad sobre el ciclo en 133** |

Serie: C (125) sí · A (126) no · B (127) no · C (128) no · A (129) no · B (130) no · C (131) no · **A (132) no.**

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **12-oct** | **EXISTE**, solo por republicadores: Milenio («acciones-relevantes-de-gabinete-de-seguridad-12-de-octubre-2026», sin fecha en la ruta), RED113 2026/10, SICOM, Hoja de Ruta, Talla Política, Certeza Diario, La Prensa; **Argon México 2026/10/13** («Golpea Gabinete de Seguridad al crimen… en nueve estados»). Publicación del 13-oct, hora no fijada. Las acciones son del **12-oct**: ventana de 131 → `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total. Estados: Edomex, Mich, Nay, NL, Oax, Qro, Sin, Tamps, Ver. Desglose, **solo por resumen**: Cotija, Plan del Cerro, 122 AEI, 4 largas, 4 cargadores, 45 cartuchos (Ejército) · Zinacantepec, 3 detenidos, 2 largas, 1 corta · Matamoros, 4 largas · Concordia, 1 larga, 1 cargador, 23 cartuchos · Santa Catarina, 3 detenidos, 137 kg de metanfetamina · Sayula de Alemán, hidrocarburo · Huimilpan, 72,000 L · La Yesca, 41,200 plantas |
| **13-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto, «12 y 13» y título sin `site:`), dos veces (ola y coordinador). La consulta se hizo el 14 por la mañana: puede ser retraso del índice. **No se declara inexistente.** |

**Trampa de año**: no apareció 2025 esta vez; sí devolvió «12, 13 y 14 de junio de 2026» y el agregado del 2 al 4-oct. `gabinetedeseguridad.gob.mx/resultados/`:
SRIV (solo robo de vehículo del 1 al 10-oct). **GN** (último indexado 20-may), **Defensa** (26-jun), **Marina** (agosto para armamento) y **FGR** (`gob.mx/fgr`,
solo 2020-2022): `SIN RESULTADO INDEXADO EN VENTANA`, una búsqueda dirigida cada una.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Totolapan** (`ARG-131-002`) | **Comunicado de la Fiscalía de Morelos**, por cita de medios: liberación por «protocolo de emergencia»; agentes con golpes y heridas de bala (Delitos de Alto Impacto); ≥10 investigados; un estudiante de servicio social retenido con ellos, **una sola fuente** (3 o 4 liberados sigue contradicho). **«El Güero Gym» no recapturado**; el titular de la SSPC «adelanta su arresto» (Infobae 2026/10/13). Responsables de la retención: no identificados; ningún detenido. Proceso 2026/10/13 (381774, 381826). **Policías muertos en el accidente: 4 por titular** (El Heraldo de México 2026/10/12, «Mueren 4 policías al caer de un puente…») frente a 2 (La Jornada 2026/10/12, cifra inicial): **4 es la cifra actualizada**, por titular; SSPC Morelos, por resumen. Sigue siendo **accidente, no agresión**. Seguimiento: acción 3 de la portada |
| **Puebla, FGE** (`ARG-131-003`) | Colonia: **Guadalupe Hidalgo** (av. 11 Sur), Síntesis 2026/10/13 («Ataque armado contra agentes ministeriales deja un herido en Puebla; no hay detenidos») y Diario Puntual 2026/10/13; Lomas de Castillotla, descartada. Comando en motocicletas con armas largas, por resumen. Herido: auxiliar ministerial, estable (FGE, por resumen). **Objetivo NO DETERMINADO** (dos nombres distintos en medios; no se reproducen). Hora: noche del lunes 12, sin hora citable. Cero detenidos. **Sigue en 131.** Tribuna «Guadalupe Hidalgo» ≠ Pachuca: misatribución del resumidor |
| **«El Cabra»** (`ARG-131-006`) | **Fecha de la captura NO fijada**: todas las fuentes datan el **anuncio** (12-oct). Infobae 2026/10/12, Síntesis 2026/10/12, El Diario de Chihuahua 2026/oct/12, La Jornada 2026/10/13. **Sin fe de erratas.** Trampa: un resumen le atribuyó «7 detenidos, 3 víctimas liberadas y más de 40 armas largas» — son de una operación de Sonora citada el 14-oct |
| **Horas del 11-oct** | **Ninguna citable.** Nacajuca: madrugada (La Prensa de Coahuila 2026/10/11; La Silla Rota 2026/10/12). Morelia micheladas: ~02:15 (Blog del Narco, NO OFICIAL) o ~05:00 (Quadratín, resumen). Ilustres Novohispanos: «mañana» por titular. Parral: ~03:00 por resumen. Las cuatro siguen con su marca |
| **Parral** (`-REC-004`) | Contradicción sin arbitrar: El Diario de Chihuahua 2026/oct/12 «asciende a dos»; Fiscalía Zona Sur, 0 muertos y 3 lesionados, solo por resumen, sin comunicado posterior. Armamento: 1 AR-15 y 2 cargadores, solo por resumen |
| **Jacona** (`ARG-130-001`) | **El 6 es de la FGE** (atiempo.mx «Eleva FGE a 6 muertos y 3 heridos», por resumen; desglose: 2 policías municipales, 1 civil, 3 agresores abatidos); **no se halló que la SSP diera el 6**. El 8 sigue solo en medios. Quién abatió: Guardia Civil (FGE) o GN (otras notas). Inventario cualitativo; cero detenidos. Grupo Marmor 2026/10/11 |
| **Vallado Viejo** (`ARG-131-001`) | **Es el mismo hecho que «Recursos Hidráulicos»** (calle Segunda, cerca de Federalismo; El Sol de Sinaloa, Extraoficial): madre e hijo, 4 muertos. N+ con «12-octubre-2026» en la ruta ancla el **día**; hora sin fijar. Sin FGE; cero detenidos. **No es omisión ni hecho de 132.** Acción 4 de la portada |
| **Minatitlán** (`ARG-129-001`) | **FGE Veracruz: 1 muerto y 1 lesionado** (Mexican Times, sin fecha, por resumen) frente a **2 muertos** por titular (Milenio «…dejó dos muertos»; N+ «Muere segundo vigilante…»). Ataque la noche del sábado 10-oct; segunda muerte el domingo 11 antes de las 20:00, solo por resumen. Cero detenidos; móvil no oficial |
| **Otatitlán** (`-REC-001`) | Sin detenidos; «diversas líneas de investigación» (gobernadora). MVS 2026/10/12. Color 🟡 sin cambio, revisable por el destinatario |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| SEMAR 10-oct (Sinaloa) | Comunicado RN-4 107/2026 (por resumen). **12 largas** = Las Cañas (4) + Rincón de Higueras (8); **13 si se suma Las Porras (1)**, que **ya es `ARG-129-ARM-001`**: se resuelve la discrepancia 12/13. 88 cargadores y 2,849 cartuchos, **cálculo propio** sobre cifras por resumen. **7 AEI de Varados y Siqueros: `POSIBLE DUPLICIDAD` con los 7 destruidos en Mazatlán de `ARG-125-005`** — no se resuelve |
| Zamora (`ARG-129-REC-001`) | Sin arbitrar: 4 (Milenio y otros) frente a 5 (IMN, sin día) |
| Industrial Bravo / La Popular | Probablemente **un solo operativo** con dos topónimos (9 largas, 22 cargadores, 173 cartuchos, 7 AEI, sin fecha en la ruta). Relación con `ARG-129-REC-002` (Los Pinos): **NO DETERMINADA** |
| Juchitán, La Ventosa | Hombre de 56 años ejecutado frente a la casa del agente municipal, 39 casquillos, cartulina (Meganoticias, El Imparcial de Oaxaca, sin fecha; La Onda 2026/10). Secretaría de Gobierno: «orden criminal», posible extorsión. **No se acredita ataque contra el agente**: sigue sin ficha |
| La Curva, Nayarit (`ARG-125-003`) | FGE sin cifra oficial de víctimas tras nueve días (nnc.mx) |
| Acapulco «El Junior» | Inventario: 2 armas sin desglose (titular de la SSPC). Sigue cualitativo |
| Pinotepa, Cancún Los Corales, Chipilo, Pachuca, El Balcón | Sin acto nuevo. Chipilo: policía fuera de peligro |
| Ciudad Juárez (`ARG-130-008`) | Publicación del 11-oct confirmada; fecha del hecho sin fijar |
| Ciudad Hidalgo, decapitado | Es **Ciudad Hidalgo, Michoacán** (11-oct, carretera a Los Azufres, Quadratín sin fecha): sigue sin URL con fecha |
| Ciudad Isla | Gráfico al Día 2026/10/13: 8 armas sin desglose, 41 cargadores, 34 cartuchos, localidad Mazoco; hecho del 10-oct. Sigue evento anterior |
| Sombrerete | 185 frente a 39 detonadores: sin resolver |

## 7. Arbitrajes del coordinador (versión final, tras los controles)

| Caso | Arbitraje |
|---|---|
| **Navolato, fosa de Campo Romero** (`ARG-132-001`) | **🔴 por hallazgo de fosa clandestina. Hallado por `procedencia-cifras`; la ola lo omitió.** Diario de Yucatán 2026/10/13 (réplica de El Universal, «Colectivo de búsqueda halla tres cuerpos en fosas clandestinas en Navolato») y Revista Espejo 2026/10/13; Sinaloahoy titula «Fiscalía General del Estado localiza restos de tres personas…» (sin fecha). Colectivos: «alrededor de cinco», solo por resumen; primer reporte, 1 (Meganoticias 778717). Hallazgo progresivo («Van dos», Noticiero Altavoz): **fecha de inicio no fijada → `FRONTERA`** |
| **Orizaba** (`-002`) | 🟡: la autoridad inicia (cateo) y es repelida. Muerto no identificado (El Sol de Veracruz titula «un civil»); si fuera personal o víctima ajena, sube a 🔴. Rescate absorbido en el mismo evento: **decisión revisable**. Día y hora solo por resumen: `FRONTERA` (corrección de `procedencia-cifras`) |
| **San Blas Atempa** (`-003`) | 🟡 por homicidio doloso único. **Decisión revisable por el destinatario**: docente de escuela pública, coordinador académico y exrepresentante seccional de la Sección 22 (solo por resumen); la escala no lo trata como «servidor público» y el ingreso armado al plantel no acredita por sí la «ejecución pública dirigida a aterrorizar». ADN Sureste fecha su nota a las 10:45 del 13: frontera del lado de la apertura. Hospital contradicho (Tehuantepec o Salina Cruz) |
| **Naucalpan** (`-004`) | 🟡. «Mañana del martes», solo por resumen: frontera del lado de la apertura |
| **Cotija** (`-005`) | **Pasa de recuperación a hecho propio** (`procedencia-cifras` 27): los resúmenes se contradicen —12-oct al mediodía o 13-oct—; publicado el 13-oct, día de cierre de 131, sin hora: **regla de frontera, se integra en la edición que lo ve primero**. 🟡: el iniciador solo está en la versión militar, y solo por resumen; si se acredita la agresión al reconocimiento, sube a 🔴. 3 AK-47 solo por resumen: `POSIBLE DUPLICIDAD` con las 4 largas de Plan del Cerro (boletín del 12-oct) |
| **«El Cromo»** (`-006`) | 🟢. Anuncio del 14-oct; fecha de captura no publicada: `FRONTERA`. Semar por titular (Infobae «Marina captura a "El Cromo", líder de una célula del CJNG en Oaxaca»). Órdenes 2 (El Universal, *slug*) o 3 (El Imparcial): contradicho |
| **Escuinapa, Pueblo Nuevo** | **Sale de la ventana** (`procedencia-cifras` 1): Línea Directa 2026-10-12__1719331 («Detienen a tres hombres armados y con motos robadas en persecución en Escuinapa») fija la publicación el 12-oct → **`ARG-132-REC-005`, 🟢, ventana de 130 o 131**. La fila `ARM-001` se retira de todos los totales |
| **León** | **Sale de la ventana** (`procedencia-cifras` 6): el resumen fecha el hecho el 27-sep (dos búsquedas). **Evento anterior publicado durante el corte**, línea en el módulo de armamento, fuera del total. Ficha y fila `ARM-002` retiradas |
| **Monterrey, Nueva Topo Chico** | **No se integra**: una sola fuente (MVS 2026/10/13), cifras solo por resumen |
| **Tehuacán** (`-REC-001`) | Ventana de 131. **Recuperación por anclaje posterior, no omisión**: 131 lo vio y lo descartó por falta de URL con fecha |
| **Villa Unión** (`-REC-002`) | Lunes 12 por la tarde; Luz Noticias y Línea Directa 2026-10-12. Omisión de 131 |
| **Doctor Coss** (`-REC-003`) | **🔴 en su ventana** (`procedencia-cifras` 33): El Porvenir titula «Repelen ataque y abaten a dos sujetos en Dr. Coss»; Fuerza Civil afirma que los civiles dispararon primero contra el patrullaje. Versión única de la autoridad. ~16:00 solo por resumen → 131 (130 si fue antes de las 08:19). 2 largas por *slug* de El Universal |
| **Acaponeta** (`-REC-004`) | Hallazgo del domingo 11-oct sin hora: ventana de 129 o 130. 🔴 por homicidio múltiple. Meganoticias Tepic 778257 («Localizan cuerpos y fosa clandestina en zona norte de Nayarit») **no verificada: retirada de las fuentes**; si es este hecho, añade fosa |
| **Sentencias** | **Ninguna integrable.** FGEO 80 años: título institucional y campos individualizadores (iniciales, pena, año y lugar del hecho), pero **publicación sin URL con día** (La Onda 2026/10; el 13-oct y el «8-ene-2021», solo por resumen de la búsqueda del coordinador). NL, Zac, Son, FGR Chihuahua: medios o republicadores |
| **Boletín federal del 12-oct** | **No se ficha como recuperación** (a diferencia de `ARG-128-REC-003` a `-007`): acciones verdes con cifras **solo por resumen** y sin URL fechada de cada acción. Línea de evento anterior en el módulo de armamento. **Su armamento no entró en los totales de 131** |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-132-FE-001`** — **Omisiones de ARGOS 131**: Villa Unión (`-REC-002`, 🟡) y Doctor Coss (`-REC-003`, 🔴, si fue después de las 08:19 del 12). Tehuacán
  (`-REC-001`, 🟡) es **recuperación por anclaje posterior**, no omisión. **Conteo de 131 recalculado, cálculo propio**, con los tres: rojos 3 → **4**, amarillos
  1 → **3**, verdes sin cambio; muertos por agresión 5 → **7**, más **2 agresores abatidos** en Doctor Coss. Escuinapa (`-REC-005`, 🟢, 130 o 131) se asigna
  cuando se fije la hora. **El armamento del boletín federal del 12-oct no entró en los totales de 131.**
- **`ARG-132-FE-002`** — **Omisión de ARGOS 129 o 130**: Acaponeta (`-REC-004`), un rojo y tres muertos; se asigna cuando se fije la hora.
- **Sin fe de erratas** por «El Cabra» (fecha de captura no fijada) ni por las horas del 11-oct (ninguna citable). Cotija no es fe de erratas: se integra en 132
  por la regla de frontera.
- **Actualización de dato de 131, no fe de erratas**: Totolapan, policías muertos en el accidente, 4 por titular (cifra actualizada); Puebla, colonia Guadalupe
  Hidalgo; Vallado Viejo = Recursos Hidráulicos.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV | NO REVISADA | NO REVISADA (`fgebc.gob.mx` no devuelto) · Tijuana 9 a 4 m, 6-oct, fuera |
| Baja California Sur | SRIV (búsqueda propia) | SRIV (`bcs.gob.mx`) | NO REVISADA (solo FGR: Pichilingue, ya `ARG-131-SEN-001`) |
| Sonora | SRIV | SRIV (`sonora.gob.mx`, `seguridad.sonora.gob.mx`) | NO REVISADA (`fge.sonora.gob.mx` no devuelto; quinta edición) · Nogales, candidato |
| Chihuahua | SRIV · seguimiento Parral | SRIV (`sspe.chihuahua.gob.mx`, agregado 4-11 oct) | SRIV (`fiscalia.chihuahua.gob.mx`) · FGR, dos candidatas |
| Sinaloa | **hecho** (`-001`) · `-REC-002`, `-REC-005` · seguimiento Vallado Viejo | SRIV (`sspsinaloa.gob.mx`; Pueblo Nuevo, ventana anterior) | NO REVISADA (quinta edición; solo republicadores: Navolato 40 años, 12-oct, fuera) |
| Durango | SRIV (búsqueda propia) | SRIV (`fiscalia.durango.gob.mx`) | SRIV (`fiscalia.durango.gob.mx`, último agosto) |
| Coahuila | SRIV | NO REVISADA (solo medios) | SRIV (**`sitio.fgecoahuila.gob.mx`**, último 31-ago) |
| Nuevo León | SRIV · `-REC-003` | NO REVISADA (`nl.gob.mx` no devuelto) · Monterrey, visto | NO REVISADA · 155 años, candidato |
| Tamaulipas | SRIV | NO REVISADA | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | SRIV | NO REVISADA · Zona Industrial, visto | NO REVISADA |
| Zacatecas | SRIV | SRIV (`ssp.zacatecas.gob.mx`, último 15-ago) | SRIV (**`fiscaliazacatecas.gob.mx`**) · Juan «N», candidato |
| Jalisco | **hecho** (`-006`) | SRIV (`secretariadeseguridad.jalisco.gob.mx`) | SRIV (`fge.jalisco.gob.mx`) |
| Colima | SRIV | SRIV (`col.gob.mx`) | SRIV (`fgecolima.mx`, 9-oct, fuera) |
| Nayarit | SRIV · `-REC-004` · seguimiento La Curva | SRIV (`nayarit.gob.mx`) | NO REVISADA (`fiscalianayarit.gob.mx`: 0) |
| Aguascalientes | SRIV | NO REVISADA | SRIV (`fiscalia-aguascalientes.gob.mx`, 2-oct) |
| Michoacán | **hecho** (`-005`) · seguimiento Jacona | SRIV (`ssp.michoacan.gob.mx`, último 10-sep) | SRIV (`fiscaliamichoacan.gob.mx`) |
| Guanajuato | SRIV | SRIV en ventana (`boletines.guanajuato.gob.mx`, 13-oct: León, hecho del 27-sep, evento anterior) | NO REVISADA (`portal.fgeguanajuato.gob.mx` sin boletín) |
| Ciudad de México | SRIV (Azcapotzalco e Iztacalco, sin URL con fecha) | NO REVISADA | SRIV (`fgjcdmx.gob.mx`) |
| Estado de México | **hecho** (`-004`) | NO REVISADA (`edomex.gob.mx` no devuelto) | NO REVISADA |
| Morelos | SRIV · seguimiento Totolapan | NO REVISADA | SRIV (`fiscaliamorelos.gob.mx`, listado del 12-oct sin sentencias) |
| Puebla | SRIV · `-REC-001` · seguimiento FGE | SRIV (`puebla.gob.mx`, agregado 1-10 oct) | NO REVISADA |
| Tlaxcala | SRIV | SRIV (`comunicacion.tlaxcala.gob.mx`) | NO REVISADA (sin dominio oficial devuelto) |
| Hidalgo | SRIV · Tulantepec sin pena | SRIV (`hidalgo.gob.mx`, solo Periódico Oficial) | NO REVISADA (`procuraduriahidalgo.gob.mx` no devuelto) |
| Querétaro | SRIV | NO REVISADA | SRIV (`fiscaliageneralqro.gob.mx`, 5 a 8-oct, fuera) |
| Veracruz | **hecho** (`-002`) · seguimiento Minatitlán y Otatitlán | SRIV (`veracruz.gob.mx`, 7-8 oct) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | SRIV · seguimiento «El Cabra» | SRIV (`tabasco.gob.mx`, junio) | SRIV (`fiscaliatabasco.gob.mx`, abril) |
| Guerrero | SRIV (Zihuatanejo, sin URL verificada) | NO REVISADA (dominio devuelto no documentado) | NO REVISADA (dominio devuelto no documentado) |
| Chiapas | SRIV | NO REVISADA (dominio devuelto no documentado) | NO REVISADA (sin portal estatal devuelto) |
| Oaxaca | **hecho** (`-003`) | NO REVISADA (dominio devuelto no documentado) | **Publicó, no integrable** (`portal.fgeo.gob.mx`, boletín 2,889: 80 años, publicación sin día anclado) |
| Campeche | SRIV | NO REVISADA | NO REVISADA (`fiscalia.campeche.gob.mx` no devuelto) |
| Yucatán | SRIV · Oxkutzcab visto | NO REVISADA (`ssp.yucatan.gob.mx` no devuelto) | NO REVISADA |
| Quintana Roo | SRIV · Cancún cateos (12-oct), visto | NO REVISADA (`qroo.gob.mx` no devuelto) | SRIV (`fgeqroo.gob.mx`) |

**Sentencias: 16 de 32** (15 SRIV + Oaxaca, publicó sin integrar); FGR revisada por búsqueda; **16 `NO REVISADA`**. **Armamento: 16 de 32** (23 en 131: regresión por rotación y
rebaja de Gro, Oax y Chis tras `editor-duplicidad`, por no constar el dominio devuelto). **Alto impacto: 32 de 32
por búsqueda dirigida en medios.**

## 10. Hechos vistos y NO fichados, con motivo

- **Escuinapa, Malecón Siglo XXI** (encargado de expendio, noche del martes 13 por resumen): Los Noticieristas 2026/10 sin día → candidato de 133.
- **Culiacán, col. Miguel Hidalgo** (disparos contra vivienda, sin lesionados): sin URL con fecha.
- **Zihuatanejo, col. Vicente Guerrero** (1 muerto, 13-oct por resumen): URL no verificada.
- **Xalapa, El Castillo** (hombre sin vida en carnicería) y **Villahermosa, Linda Vista** (gas LP, 2 detenidos): solo por resumen.
- **Veracruz, Abdón «N»**: anuncio del 13-oct (Hora Cero 2026/10/13) sin municipio ni fecha de captura → candidato de 133.
- **Sonora, operación citada en la conferencia del 14-oct** (7 detenidos, 3 víctimas liberadas, «más de 40 armas largas», solo por resumen del equipo Golfo):
  sin URL ni municipio → candidato de 133; **el SRIV de Sonora en alto impacto y armamento queda matizado por este candidato**.
- **Tonalá, Jalisco** (col. Jalisco): Guardia Nocturna 2026/10, sin día. **CDMX, Azcapotzalco e Iztacalco**: sin URL con fecha.
- **Mazatlán, llanteras** (Chulavista; Valles del Ejido): sin día en la ruta.
- **Valle de Bravo, «Cara de Cochi»** (10-oct; Infobae 2026/10/12): evento anterior; armamento `POSIBLE DUPLICIDAD` con el agregado del 9 al 11-oct.
- **Monterrey, Nueva Topo Chico**: una sola fuente. **SLP, Zona Industrial** (El Heraldo de SLP 2026/10/13): arma sin tipo. **SLP, Tamasopo** (5 detenidos, droga):
  sin armas, sin fecha. **SLP, GCE 24 h** (38 detenidos): agregado. **Oxkutzcab** (PorEsto 2026/10/13): sin cifra de armas. **Cancún, dos cateos** (12-oct):
  cifras contradichas; La Selva SM 225 `POSIBLE DUPLICIDAD` con el cateo del 8-oct.
- **Istmo de Oaxaca, agresiones del 5 al 12-oct** (Palacio de Santa María Mixtequilla, comandancia de Santo Domingo Petapa; Oaxaca Capital 2026/10/12): sin
  fechas individuales → candidatos de 133 (posible ataque a autoridad).
- **Sentencias no integradas**: FGR Sonora 706/26 (hasta 12 años, cuatro hombres; NX Noticias, sin fecha) · Culiacán, Pedro «N» (4 años 10 meses; Los
  Noticieristas 2026/10 sin día) · Navolato, José Abel «N» (40 años; Línea Directa 2026-10-12, ventana de 131) · Zacatecas, FGR, Nayeli y Elizandro «N» (4 años;
  NTR 2026/10 sin día: sigue sin fecha anclada) · Querétaro, tres sentencias (5 a 8-oct, fuera) · Colima, 27 años (boletín del 9-oct, por resumen del equipo
  Occidente, fuera).
- **Sonora, «6 millones de dosis»** (Diario de Yucatán 2026/10/13) y **Chihuahua, informe semanal SSPE**: agregados, no eventos.
- **Piedras Negras** (4 armas, 16 cargadores): vinculación a proceso, no sentencia; fecha del hecho no fijada.
- **«El Tripa»** (detenido en Querétaro el 9-oct): fuera de ventana.

## 11. Desglose de cálculos propios

- Duración: 13-oct 07:23 → 14-oct 08:19 = **24 h 56 min** = 24,93 h. Densidad: 6 / 24,93 = **0,24**.
- Muertos en hechos propios: por agresión, Orizaba 1 + San Blas Atempa 1 + Naucalpan 1 = **3**; agresores abatidos, Cotija **3**; cuerpos en fosa, Navolato **3**.
  Heridos: **3** ministeriales (Orizaba). Rescatados: **2**.
- Armamento propio integrable: **0** en todas las categorías.
- Frontera: **6 de 6**.
- Conclusión 1, «tercero en el municipio desde el 8-9 oct»: `ARG-128-005` y `-006` (noche del 8 o 9-oct) + `ARG-132-004` (13-oct).
- Conclusión 3, «cinco abatidos»: Cotija 3 + Doctor Coss 2.
- Conclusión 5: Oaxaca (2021), Zacatecas (2018), Sonora (2025), años por resumen.
- SEMAR 10-oct: 4 + 8 = 12 largas; 21 + 67 = 88 cargadores; 2,634 + 215 = 2,849 cartuchos (sobre cifras por resumen).
- Fe de erratas de 131: rojos 3 + 1 (Doctor Coss) = 4; amarillos 1 + 2 (Tehuacán, Villa Unión) = 3; muertos 5 + 2 = 7.

## 12. Fuentes por ficha

- **`ARG-132-001`** — Institucional 1 (FGE Sinaloa, por titular de Sinaloahoy). Nacional 2: El Universal (réplica en Diario de Yucatán 2026/10/13); N+. Regional 8:
  Revista Espejo 2026/10/13; Noroeste (KI26480596); Los Noticieristas 2026/10 (1147742); Sinaloahoy; Meganoticias (778717); Puntualizando; Noticiero Altavoz; Diario de Yucatán.
- **`ARG-132-002`** — Nacional 1: La Silla Rota 2026/10/13 (532902). Regional 7: Golpe Político 2026/10/13 (dos notas); Meganoticias (778941, 778935); TV Azteca
  Veracruz; XEU (1436624); La Nigua; El Buen Tono; El Sol de Veracruz («…y un civil sin vida»). «Uno grave», calle y hora: resumen de la búsqueda del coordinador.
- **`ARG-132-003`** — Institucional 1 (FGEO, por cita). Nacional 5: El Financiero 2026/10/13; Infobae 2026/10/13; La Jornada 2026/10/13; La Silla Rota 2026/10/13
  (532825); Aristegui (1310). Regional 6: El Informador 20261013-0100; Proyecto Puente 2026/10/13; Tribuna 2026/10/13; Sociedad Noticias 2026/10/13; Medios
  Obson 2026/10/13; ADN Sureste (10:45 h). Internacionales: La Opinión, Noticias SIN, La Prensa (Nicaragua). Hospital de Salina Cruz: La Razón 2026/10/14, resumen.
- **`ARG-132-004`** — Nacional 2: El Heraldo de México 2026/10/13 (907562); El Universal. Regional 3: Cúspide México 2026/10/14; Telediario; Quadratín Edomex.
- **`ARG-132-005`** — Regional 8: Grupo Marmor 2026/10/13; Red Michoacán 2026/10/13; La Voz de Michoacán; Respuesta; Contramuro; 1plana; IMN; Info7. Abierta 1:
  Blog del Narco (NO OFICIAL).
- **`ARG-132-006`** — Institucional 1 (anuncio de la SSPC, por titular). Nacional 5: Infobae 2026/10/14; La Razón 2026/10/14; La Silla Rota 2026/10/14 (532942);
  El Heraldo de México 2026/10/14 (908087); El Universal («…cuenta con dos órdenes de aprehensión por homicidio»). Regional 1: El Imparcial 2026/10/14 («…tres órdenes…»).
- **`ARG-132-REC-001`** — Nacional 1: N+. Regional 8: Síntesis 2026/10/13; Reto Diario 2026/10/13; Intolerancia 2026/10/13 (1059025); Cinco Radio; Urbano;
  La Jornada de Oriente; ATN; Ambas Manos.
- **`ARG-132-REC-002`** — Regional 3: Luz Noticias 2026-10-12 (309430); Línea Directa 2026-10-12__1718876; Noroeste (AE26444343). Llantera del 1-oct: Línea
  Directa 2026-10-01 (equipo Noroeste).
- **`ARG-132-REC-003`** — Nacional 2: MVS Noticias 2026/10/12 (749525); El Universal («…aseguran dos armas largas»). Regional 2: El Porvenir (1034193, «Repelen
  ataque…»); Meganoticias (778464).
- **`ARG-132-REC-004`** — Regional 3: NTV 2026/10/11; Nayarit Noticias 2026/10/11; NNC. Meganoticias Tepic 778257: no verificada, retirada.
- **`ARG-132-REC-005`** — Institucional 1: `sspsinaloa.gob.mx/post/tres-civiles-armados-fueron-detenidos-por-el-grupo-interinstitucional-en-escuinapa…` (sin
  fecha). Regional 3: Línea Directa 2026-10-12__1719331; Tus Buenas Noticias 2026/10/13 (65628); Los Noticieristas 2026/10 («armas calibre 9 mm y dos motocicletas»).
- **León (evento anterior)** — `boletines.guanajuato.gob.mx/2026/10/13/detienen-fspe-a-un-hombre-con-un-revolver-y-49-cartuchos-utiles-en-leon/`; Guanajuato Informa.
- **Sentencia candidata de Oaxaca** — La Onda Oaxaca 2026/10; revista-mujeres; «A.J.B.», San Antonio de la Cal y el año: resumen de la búsqueda del coordinador.

## 13. Los dos controles editoriales

Racha: **dieciocho pases consecutivos, dieciocho «CORREGIR»**. Lanzados en paralelo sobre la versión estable `5536566`, con las notas de **los seis equipos**
(resúmenes en el *scratchpad*; los informes íntegros de los equipos documentan los dominios de §9).

**`procedencia-cifras`** (25 búsquedas, 0 `WebFetch` útiles) — **CORREGIR**. **Un rojo omitido** (fosa de Navolato).

| # | Hallazgo | Disposición |
|---|---|---|
| 1-5 | Escuinapa, Pueblo Nuevo, publicado el 12-oct (Línea Directa): fuera de ventana; título «dos pistolas» sin titular; confianza incoherente | **Corregido**: `ARG-132-REC-005` 🟢 ★★☆☆☆; título «armas 9 mm»; fila de armamento retirada |
| 6-8 | León: hecho del 27-sep por resumen | **Corregido**: evento anterior, ficha y fila retiradas |
| 9 | Totales de armamento | **Corregido**: 0 en todas las categorías; `SIN TOTAL NACIONAL VERIFICABLE` |
| 10 | Rojo omitido: fosa de Navolato | **Corregido**: `ARG-132-001` 🔴 |
| 14 | Día de Orizaba solo por resumen | **Corregido**: día marcado; `FRONTERA` |
| 17-18 | San Blas: hospital contradicho; perfil de la víctima | **Corregido** |
| 20-21 | Conclusión 1: «cinco días» y patrón de motocicleta no sostenidos | **Corregido** |
| 23, 25 | «El Cromo»: órdenes 2 o 3 con fuentes; Semar por titular | **Corregido** |
| 27-29 | Cotija: fecha 12 o 13 contradicha; iniciador solo por la versión militar | **Corregido**: pasa a hecho propio 🟡 con `FRONTERA` y reserva de 🔴 |
| 31-33 | Doctor Coss: ~16:00; 2 largas por *slug*; «Repelen ataque» | **Corregido**: 🔴 en su ventana |
| 34, 36, 42 | Conclusiones 3, 4 y 5 | **Corregido**: reescritas |
| 40 | Meganoticias Tepic no verificada | **Corregido**: retirada |
| 41 | «8-ene-2021» no verificado | **Corregido**: «2021» |
| 43 | Colima 27 años | **Sostenido** por el informe del equipo Occidente (boletín del 9-oct, resumen) |
| 44 | Tipos de fuente | **Corregido** |
| 45 | Cancún «24 armas» = 17 + 7 | **Corregido**: «16 o 25» |
| 46 | Oaxaca dentro del SRIV | **Corregido**: «publicó, no integrable» |

**`editor-duplicidad`** (sin búsquedas) — **CORREGIR**. **Ningún duplicado real** con 128-131.

| # | Hallazgo | Disposición |
|---|---|---|
| 1-2 | Conclusiones 1 y 3 sin sustento | **Corregido** |
| 3 | Armamento de fichas (Cotija, Doctor Coss) ausente del módulo | **Corregido**: Cotija, cualitativo con `POSIBLE DUPLICIDAD`; Doctor Coss y Escuinapa en «recuperaciones, fuera del total» |
| 4 | Boletín del 12-oct sin ARG-ID | **No se ficha**: motivo en §7; constancia en `FE-001` |
| 5 | Oaxaca en SRIV; operación de Sonora del 14-oct sin registro | **Corregido** (§9, §10) |
| 6 | Cobertura no sostenida por las notas resumidas | **Corregido en parte**: Gro, Oax y Chis bajan a `NO REVISADA` en armamento y Gro en sentencias (dominio no documentado en el informe). **Armamento 19 → 16; sentencias 17 → 16** |
| 7 | Confianzas opuestas | **Resuelto** al retirar `-005` y `-006` |
| 8 | Panorama de Doctor Coss: «Fuerza Civil (por cita)» | **Corregido**: SIN BOLETÍN |
| 9 | Recuento por tipo de fuente | **Corregido** |
| 10 | Deslindes sin referente | **Corregido**: fuentes de la llantera y de La Higuerita; `ARG-115-ARM-004`; Pueblo Nuevo 18-sep; criterio de Villa Unión |
| 11 | Conclusión 5 de método | **Corregido**: brecha hecho–condena |
| 12 | Repetición panorama / Valoración | **Corregido**: Valoración solo con ARG-ID |
| 13 | Portada: cláusula del Istmo; dos solicitudes por línea | **Corregido** |
| 14 | Tehuacán no es omisión | **Corregido** |
| 15-17 | Hechos y datos sin rastro en §10 y §12 | **Corregido** |
| 18 | Índice y pendientes | **Corregido** al cierre |
| 19 | BC en la regresión; persecución de Escuinapa | **Corregido** |
| 20 | Móvil: IDs de armamento inexistentes | **Resuelto**: ya no hay filas |

**Segundo pase** — `validar.js` → **validación OK** (escritorio); `gen-movil.py` → **validación OK** (móvil); `.txt` regenerado. Segundo `editor-duplicidad` sin web
sobre la versión corregida: ver al pie.

## 14. Herramientas

`tools/datos-argos-132.py` (desde 131; `ARM = []` con tabla «SIN FILAS», como en 131; sentencias sin ficha integrada; portada con una solicitud por línea).
`gen-movil.py` y `gen-texto.py` sin cambios. `validar.js`: OK.

## 15. Lecciones de método (no van al cartelón)

1. **La ola de seis equipos omitió el único rojo propio del corte** (fosa de Navolato) y lo halló `procedencia-cifras`, como Escuinapa en 130. Propuesta para
   133: una búsqueda por equipo de «fosa / colectivo de búsqueda / restos» por sus entidades, además de la de «funcionario asesinado».
2. **Dos de seis fichas propias eran de otra ventana** (Escuinapa publicada el 12; León, hecho del 27-sep). La fecha de publicación de un republicador del 13 no
   basta: hay que buscar la primera publicación del mismo hecho antes de fichar.
3. **La búsqueda nacional del coordinador volvió a traer hechos que la ola no traía** (San Blas Atempa, «El Cromo», el boletín del 12-oct), quinta edición seguida.
4. **Sonora y Sinaloa, quinta edición sin dominio de fiscalía devuelto.** Propuesta para 133: aceptar como `REVISADA` la búsqueda que devuelve el título del
   boletín en republicadores, o retirarlas de la deuda de rotación.
5. **Los equipos deben dejar escrito el dominio devuelto por entidad**: tres entidades de armamento bajaron a `NO REVISADA` por no constar.
6. **El docente como víctima** y **el exalcalde como víctima** (131) no están en la escala de agravantes: pendiente de fijar en `CLAUDE.md` por el destinatario.
