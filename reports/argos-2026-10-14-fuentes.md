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
- **Presupuesto**: control 2 + ola de seis equipos (Noroeste 30, Noreste 22, Occidente 26, Centro 30, Golfo y federal 28, Sureste 22 = **158**) + **9 del
  coordinador** = **169**; `procedencia-cifras` hasta **25**. `editor-duplicidad` no busca en la web.
- **Rendimiento del coordinador**: la búsqueda nacional del **martes 13** halló **San Blas Atempa** y **Cotija**; la del **miércoles 14**, **«El Cromo»** y el
  **boletín federal del 12-oct**. Las otras: noche del martes (sin resultado), boletín del 13-oct (dos, sin resultado), FGEO 80 años, Orizaba (hora y «un civil»),
  Acaponeta (fecha y kilómetro).

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (9 `NO REVISADA` en 131) | **Revisadas ahora**: BCS (`bcs.gob.mx`), Son (`sonora.gob.mx`, `seguridad.sonora.gob.mx`), Chih (`sspe.chihuahua.gob.mx`), **Sin (`sspsinaloa.gob.mx`, dominio confirmado, con hecho)**, Tlax (`comunicacion.tlaxcala.gob.mx`), Hgo (`hidalgo.gob.mx`, solo Periódico Oficial), Oax, Gro (`sspgro.gob.mx`). **Sigue `NO REVISADA`**: Edomex (`edomex.gob.mx` no devuelto) |
| Prioridad — sentencias (14 `NO REVISADA` en 131) | **Revisadas**: **Coah (`sitio.fgecoahuila.gob.mx`, dominio confirmado; último indexado 31-ago)**, **Zac (`fiscaliazacatecas.gob.mx`, confirmado)**, Col (`fgecolima.mx`), CDMX (`fgjcdmx.gob.mx`), Mor (`fiscaliamorelos.gob.mx`), Qro (`fiscaliageneralqro.gob.mx`). **Siguen `NO REVISADA`**: BCS, **Son y Sin (quinta edición)**, Nay (`fiscalianayarit.gob.mx`: 0), Gto (`portal.fgeguanajuato.gob.mx` sin boletín), Tlax (sin dominio oficial), Hgo, Camp (`fiscalia.campeche.gob.mx` no devuelto) |
| Prioridad — alto impacto | **BCS y Dgo revisadas por búsqueda propia** (SRIV): alto impacto 32 de 32 |
| Ciclo | **A** — Noroeste + Centro encabezaron el triaje judicial tras la prioridad |
| Rendimiento | **Ninguna sentencia integrable.** El ciclo A halló Sonora (Nogales, republicadores), FGR Chihuahua (dos, republicador) y Querétaro (tres, `fiscaliageneralqro.gob.mx` con fecha en la ruta, 5 a 8-oct: **fuera de ventana**). Fuera del ciclo: Oaxaca (FGEO, 80 años), Nuevo León (155 años) y Zacatecas (10 años) |
| Regresión por rotación | Armamento: Coah, NL, Tamps, SLP, Ags, CDMX, Mor, Qro, Camp, Yuc, QRoo vuelven a `NO REVISADA` (sin `site:` devuelto). Sentencias: BC, NL, SLP, Edomex, Pue, Chis, Yuc. **Prioridad sobre el ciclo en 133** |

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

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Orizaba** (`ARG-132-001`) | 🟡: la autoridad inicia (cateo) y es repelida. **El muerto no está identificado** (El Sol de Veracruz titula «un civil»; La Silla Rota no lo sabe): si fuera personal o víctima ajena, sube a 🔴. El rescate de dos personas es resultado del mismo cateo: **no se abre ficha verde aparte**. Hora 19:30–20:00, solo por resumen; dentro de la ventana sin frontera |
| **San Blas Atempa** (`-002`) | 🟡 por homicidio doloso único. **Decisión revisable por el destinatario**: el docente de escuela pública no está tratado en la escala como «servidor público», y el ingreso armado al plantel con alumnos no acredita por sí la «ejecución pública dirigida a aterrorizar». ADN Sureste fecha su nota a las 10:45 del 13: el hecho es anterior; **frontera del lado de la apertura** |
| **Naucalpan** (`-003`) | 🟡. «Mañana del martes», solo por resumen: frontera del lado de la apertura |
| **«El Cromo»** (`-004`) | 🟢. Anuncio del 14-oct; fecha de la captura no publicada: integrado con `FRONTERA` (criterio de `ARG-131-006`). Nombre del alias **fuera del titular** |
| **Escuinapa, Pueblo Nuevo** (`-005`) | 🟢 con fila de armamento. Boletín de la SSP Sinaloa por *slug* sin fecha; publicación anclada por Tus Buenas Noticias 2026/10/13; fecha del hecho 12 o 13, por resumen. Confianza de la fila: **Bajo** (desglose por resumen) |
| **León** (`-006`) | 🟢 con fila de armamento. Cifras en el *slug* del boletín oficial con fecha en la ruta: **Medio** |
| **Monterrey, Nueva Topo Chico** | **No se integra**: una sola fuente (MVS 2026/10/13), cifras solo por resumen. Ni Bajo (exige dos fuentes) |
| **Tehuacán** (`-REC-001`) | Noche del lunes 12: ventana de 131. ARGOS 131 lo había descartado por falta de URL con fecha; tres regionales del 13-oct lo anclan |
| **Cotija** (`-REC-002`) | ~12:00 del lunes 12, solo por resumen: ventana de 131. 🟡: no se pudo determinar quién inició. ★★☆☆☆: los dos medios con fecha llevan el mismo titular (posible réplica). Relación con los 122 AEI de Plan del Cerro (boletín del 12-oct): no determinada |
| **Villa Unión** (`-REC-003`) | Lunes 12, aviso ~12:15 por Noroeste (sin fecha en la ruta); Luz Noticias 2026-10-12 y Línea Directa 2026-10-12 anclan el día. Ventana de 131 |
| **Doctor Coss** (`-REC-004`) | Publicado el 12-oct sin hora: ventana de 130 o 131. Trampa de año con el hecho de agosto de 2025 |
| **Acaponeta** (`-REC-005`) | Hallazgo del domingo 11-oct sin hora: ventana de 129 o 130. 🔴 por homicidio múltiple. ARGOS 131 lo dejó como candidato «Meganoticias sin fecha»; NTV y Nayarit Noticias 2026/10/11 |
| **Sentencias** | **Ninguna integrable.** FGEO 80 años: título institucional, campos individualizadores (iniciales, pena, fecha y lugar del hecho), pero **publicación sin URL con día** (La Onda 2026/10; el 13-oct solo por resumen): por el corolario de agregados, no se integra. NL, Zac, Son, FGR Chihuahua: solo republicadores o medios |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-132-FE-001`** — **Omisiones de ARGOS 131**: Tehuacán (`-REC-001`), Cotija (`-REC-002`) y Villa Unión (`-REC-003`), los tres amarillos en su ventana.
  **Conteo de 131 recalculado, cálculo propio**: amarillos 1 → **4**; rojos y verdes sin cambio; muertos por agresión 5 → **7** (Tehuacán y Villa Unión), más
  **3 agresores abatidos** en Cotija. Doctor Coss (`-REC-004`) se asigna a 130 o 131 cuando se fije la hora.
- **`ARG-132-FE-002`** — **Omisión de ARGOS 129 o 130**: Acaponeta (`-REC-005`), un rojo y tres muertos; se asigna cuando se fije la hora.
- **Sin fe de erratas** por «El Cabra» (fecha de captura no fijada) ni por las horas del 11-oct (ninguna citable).
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
| Sinaloa | **hecho** (`-005`) · `-REC-003` · seguimiento Vallado Viejo | **hecho** (`sspsinaloa.gob.mx`) | NO REVISADA (quinta edición; solo republicadores: Navolato 40 años, 12-oct, fuera) |
| Durango | SRIV (búsqueda propia) | SRIV (`fiscalia.durango.gob.mx`) | SRIV (`fiscalia.durango.gob.mx`, último agosto) |
| Coahuila | SRIV | NO REVISADA (solo medios) | SRIV (**`sitio.fgecoahuila.gob.mx`**, último 31-ago) |
| Nuevo León | SRIV · `-REC-004` | NO REVISADA (`nl.gob.mx` no devuelto) · Monterrey, visto | NO REVISADA · 155 años, candidato |
| Tamaulipas | SRIV | NO REVISADA | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | SRIV | NO REVISADA · Zona Industrial, visto | NO REVISADA |
| Zacatecas | SRIV | SRIV (`ssp.zacatecas.gob.mx`, último 15-ago) | SRIV (**`fiscaliazacatecas.gob.mx`**) · Juan «N», candidato |
| Jalisco | **hecho** (`-004`) | SRIV (`secretariadeseguridad.jalisco.gob.mx`) | SRIV (`fge.jalisco.gob.mx`) |
| Colima | SRIV | SRIV (`col.gob.mx`) | SRIV (`fgecolima.mx`, 9-oct, fuera) |
| Nayarit | SRIV · `-REC-005` · seguimiento La Curva | SRIV (`nayarit.gob.mx`) | NO REVISADA (`fiscalianayarit.gob.mx`: 0) |
| Aguascalientes | SRIV | NO REVISADA | SRIV (`fiscalia-aguascalientes.gob.mx`, 2-oct) |
| Michoacán | SRIV · `-REC-002` · seguimiento Jacona | SRIV (`ssp.michoacan.gob.mx`, último 10-sep) | SRIV (`fiscaliamichoacan.gob.mx`) |
| Guanajuato | **hecho** (`-006`) | **hecho** (`boletines.guanajuato.gob.mx`, 13-oct) | NO REVISADA (`portal.fgeguanajuato.gob.mx` sin boletín) |
| Ciudad de México | SRIV (Azcapotzalco e Iztacalco, sin URL con fecha) | NO REVISADA | SRIV (`fgjcdmx.gob.mx`) |
| Estado de México | **hecho** (`-003`) | NO REVISADA (`edomex.gob.mx` no devuelto) | NO REVISADA |
| Morelos | SRIV · seguimiento Totolapan | NO REVISADA | SRIV (`fiscaliamorelos.gob.mx`, listado del 12-oct sin sentencias) |
| Puebla | SRIV · `-REC-001` · seguimiento FGE | SRIV (`puebla.gob.mx`, agregado 1-10 oct) | NO REVISADA |
| Tlaxcala | SRIV | SRIV (`comunicacion.tlaxcala.gob.mx`) | NO REVISADA (sin dominio oficial devuelto) |
| Hidalgo | SRIV · Tulantepec sin pena | SRIV (`hidalgo.gob.mx`, solo Periódico Oficial) | NO REVISADA (`procuraduriahidalgo.gob.mx` no devuelto) |
| Querétaro | SRIV | NO REVISADA | SRIV (`fiscaliageneralqro.gob.mx`, 5 a 8-oct, fuera) |
| Veracruz | **hecho** (`-001`) · seguimiento Minatitlán y Otatitlán | SRIV (`veracruz.gob.mx`, 7-8 oct) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | SRIV · seguimiento «El Cabra» | SRIV (`tabasco.gob.mx`, junio) | SRIV (`fiscaliatabasco.gob.mx`, abril) |
| Guerrero | SRIV (Zihuatanejo, sin URL verificada) | SRIV (`sspgro.gob.mx`) | SRIV |
| Chiapas | SRIV | SRIV (`sspc.chiapas.gob.mx`) | NO REVISADA (sin portal estatal devuelto) |
| Oaxaca | **hecho** (`-002`) | SRIV | SRIV (`portal.fgeo.gob.mx`) · 80 años, candidato |
| Campeche | SRIV | NO REVISADA | NO REVISADA (`fiscalia.campeche.gob.mx` no devuelto) |
| Yucatán | SRIV · Oxkutzcab visto | NO REVISADA (`ssp.yucatan.gob.mx` no devuelto) | NO REVISADA |
| Quintana Roo | SRIV · Cancún cateos (12-oct), visto | NO REVISADA (`qroo.gob.mx` no devuelto) | SRIV (`fgeqroo.gob.mx`) |

**Sentencias: 17 de 32; FGR revisada por búsqueda; 15 `NO REVISADA`.** **Armamento: 19 de 32** (23 en 131: regresión por rotación). **Alto impacto: 32 de 32
por búsqueda dirigida en medios.**

## 10. Hechos vistos y NO fichados, con motivo

- **Escuinapa, Malecón Siglo XXI** (encargado de expendio, noche del martes 13 por resumen): Los Noticieristas 2026/10 sin día → candidato de 133.
- **Culiacán, col. Miguel Hidalgo** (disparos contra vivienda, sin lesionados): sin URL con fecha.
- **Zihuatanejo, col. Vicente Guerrero** (1 muerto, 13-oct por resumen): URL no verificada.
- **Xalapa, El Castillo** (hombre sin vida en carnicería) y **Villahermosa, Linda Vista** (gas LP, 2 detenidos): solo por resumen.
- **Veracruz, Abdón «N»**: anuncio del 13-oct (Hora Cero 2026/10/13) sin municipio ni fecha de captura → candidato de 133.
- **Tonalá, Jalisco** (col. Jalisco): Guardia Nocturna 2026/10, sin día. **CDMX, Azcapotzalco e Iztacalco**: sin URL con fecha.
- **Mazatlán, llanteras** (Chulavista; Valles del Ejido): sin día en la ruta.
- **Valle de Bravo, «Cara de Cochi»** (10-oct; Infobae 2026/10/12): evento anterior; armamento `POSIBLE DUPLICIDAD` con el agregado del 9 al 11-oct.
- **Monterrey, Nueva Topo Chico**; **SLP, Zona Industrial**; **Oxkutzcab**; **Cancún, dos cateos**: en la nota del módulo de armamento.
- **Sonora, «6 millones de dosis»** (Diario de Yucatán 2026/10/13) y **Chihuahua, informe semanal SSPE**: agregados, no eventos.
- **Piedras Negras** (4 armas, 16 cargadores): vinculación a proceso, no sentencia; fecha del hecho no fijada.
- **«El Tripa»** (detenido en Querétaro el 9-oct): fuera de ventana.

## 11. Desglose de cálculos propios

- Duración: 13-oct 07:23 → 14-oct 08:19 = **24 h 56 min** = 24,93 h. Densidad: 6 / 24,93 = **0,24**.
- Muertos en hechos propios: Orizaba 1 + San Blas Atempa 1 + Naucalpan 1 = **3**. Heridos: **3** ministeriales (Orizaba). Rescatados: **2**.
- Armamento: cortas 2 + 1 = **3**; cartuchos 18 + 49 = **67**; cargadores **2**; detenidos en evento de aseguramiento 3 + 1 = **4**. Entidades con armamento: 2.
- Frontera: **5 de 6** (todos salvo Orizaba).
- Naucalpan, «tercer homicidio en cinco días» (Conclusión 1): `ARG-128-005` y `-006` (9-oct) + `ARG-132-003` (13-oct).
- Conclusión 4, «cinco abatidos»: Cotija 3 + Doctor Coss 2.
- SEMAR 10-oct: 4 + 8 = 12 largas; 21 + 67 = 88 cargadores; 2,634 + 215 = 2,849 cartuchos (sobre cifras por resumen).

## 12. Fuentes por ficha

- **`ARG-132-001`** — Nacional 3: La Silla Rota 2026/10/13 (532902); Meganoticias (778941); TV Azteca Veracruz. Regional 5: Golpe Político 2026/10/13 (dos notas);
  XEU (1436624); La Nigua; El Buen Tono; El Sol de Veracruz («…y un civil sin vida»).
- **`ARG-132-002`** — Institucional 1 (FGEO, por cita). Nacional 4: El Financiero 2026/10/13; Infobae 2026/10/13; La Jornada 2026/10/13; El Informador
  20261013-0100. Regional 6: Proyecto Puente 2026/10/13; Sociedad Noticias 2026/10/13; Tribuna 2026/10/13; Medios Obson 2026/10/13; ADN Sureste (10:45 h);
  Aristegui (1310). Además: La Opinión, Noticias SIN y La Prensa (Nicaragua) 2026/10/13, internacionales. Telediario (uniformes): dato aislado.
- **`ARG-132-003`** — Nacional 2: El Heraldo de México 2026/10/13 (907562); El Universal. Regional 3: Cúspide México 2026/10/14; Telediario; Quadratín Edomex.
- **`ARG-132-004`** — Institucional 1 (anuncio de la SSPC, por titular). Nacional 3: La Razón 2026/10/14; La Silla Rota 2026/10/14 (532942); El Heraldo de
  México 2026/10/14 (908087). Regional 1: El Imparcial 2026/10/14.
- **`ARG-132-005`** — Institucional 1: `sspsinaloa.gob.mx/post/tres-civiles-armados-fueron-detenidos-por-el-grupo-interinstitucional-en-escuinapa…` (sin fecha).
  Regional 1: Tus Buenas Noticias 2026/10/13 (65628).
- **`ARG-132-006`** — Institucional 1: `boletines.guanajuato.gob.mx/2026/10/13/detienen-fspe-a-un-hombre-con-un-revolver-y-49-cartuchos-utiles-en-leon/`.
- **`ARG-132-REC-001`** — Regional 9: Síntesis 2026/10/13; Reto Diario 2026/10/13; Intolerancia 2026/10/13 (1059025); N+; Cinco Radio; Urbano; La Jornada de
  Oriente; ATN; Ambas Manos.
- **`ARG-132-REC-002`** — Regional 7: Grupo Marmor 2026/10/13; Red Michoacán 2026/10/13; Respuesta; La Voz de Michoacán; Contramuro; 1plana; IMN. Abierta 1:
  Blog del Narco (NO OFICIAL).
- **`ARG-132-REC-003`** — Regional 3: Luz Noticias 2026-10-12 (309430); Línea Directa 2026-10-12__1718876; Noroeste (AE26444343).
- **`ARG-132-REC-004`** — Nacional 1: MVS Noticias 2026/10/12 (749525). Regional 1: Meganoticias (778464).
- **`ARG-132-REC-005`** — Regional 4: NTV 2026/10/11; Nayarit Noticias 2026/10/11; NNC; Meganoticias Tepic (778257).

## 13. Los dos controles editoriales

*(Se completa tras los controles.)*

## 14. Herramientas

`tools/datos-argos-132.py` (desde 131; filas de armamento restituidas con `armrow` de 129; sentencias sin ficha integrada; portada con acciones como solicitud).
`gen-movil.py` y `gen-texto.py` sin cambios. `validar.js`: OK.

## 15. Lecciones de método (no van al cartelón)

1. **La búsqueda nacional del coordinador volvió a traer hechos que la ola no traía** (San Blas Atempa, «El Cromo», el boletín del 12-oct), quinta edición seguida.
2. **Cuatro omisiones de 131 y una de 129-130 recuperadas**, todas por publicación posterior al cierre o por anclaje tardío de la URL: la franja del lunes 12
   por la tarde y la noche se indexó el 13.
3. **Sonora y Sinaloa, quinta edición sin dominio de fiscalía devuelto.** Sinaloa sí devolvió `sspsinaloa.gob.mx` para armamento. Propuesta para 133: aceptar como
   `REVISADA` la búsqueda que devuelve el título del boletín en republicadores, o retirarlas de la deuda de rotación.
4. **El docente como víctima** y **el exalcalde como víctima** (131) no están en la escala de agravantes: pendiente de fijar en `CLAUDE.md` por el destinatario.
