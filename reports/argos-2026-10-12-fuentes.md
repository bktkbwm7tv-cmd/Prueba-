# ARGOS 130 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-12 · **Ventana**: 2026-10-11 08:58 → 2026-10-12 08:19 CDMX · **23 h 21 min**
**Rama**: `claude/argos-130` (partió de `origin/claude/argos-129` = `9eaba81`).

---

## 1. La base

Bloque 0 a las **08:19 CST** del 12-oct. El clon arrancó en `60f2777` (por detrás de `origin/main`, como en 128 y 129);
`git merge --ff-only origin/main` avanzó `60f2777 → b0558a3`; `git merge --ff-only origin/claude/argos-129` avanzó `b0558a3 → 9eaba81`.
**Los dos merges, fast-forward.** Estado: `argos-2026-10-11` (ARGOS 129) y **153 archivos** en `reports/`, lo previsto. HEAD suelto: se abrió
`claude/argos-130`.

| Serie | 125 | 126 | 127 | 128 | 129 | **130** |
|---|---|---|---|---|---|---|
| Duración | 320 h 34 | 17 h 41 | 22 h 24 | 25 h 48 | 23 h 50 | **23 h 21** |
| Densidad (hechos/h) | 0,16 | 0,40 | 0,27 | 0,23 | 0,25 | **0,39** (9 / 23,35, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (11 y 12-oct). El generador lo comprueba con `assert`.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** a las 08:19; el proxy registra `www.gob.mx:443 — connect_rejected` (política de la
  organización). **Ningún documento leído íntegro.** Techo **★★★☆☆**, duodécima edición.
- **Consulta de control** (Minatitlán, ataque a la refinería, en los dos modos): `standard` **no encontró el caso** —devolvió incendios de
  2021 y 2023—; `extended` trajo la cobertura del 11-oct con el saldo contradicho. **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola de **seis equipos** (Noroeste 30, Noreste 24, Occidente 28, Centro 30, Golfo y federal 26, Sureste 22 = **160**)
  + **7 del coordinador** = **169**; `procedencia-cifras` **25** (0 `WebFetch`) → **194 de 200**. `editor-duplicidad` no busca en la web.
- **Rendimiento del coordinador**: la búsqueda nacional del **domingo 11** halló **Jacona** —el rojo principal— y la cobertura de Morelia; la del
  **lunes 12** no aportó hechos nuevos. Las otras cinco: Jacona (dos), Nacajuca (madrugada), Cancún (segunda fuente y hora) y Acapulco (cobertura).

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (23 `NO REVISADA` en 129) | **Revisadas ahora**: Son (`seguridad.sonora.gob.mx`), Chih (`fiscalia.chihuahua.gob.mx`), NL (`nl.gob.mx`, sin octubre), SLP (**`seguridad.slp.gob.mx`, dominio confirmado por primera vez**), Mich (`ssp.michoacan.gob.mx`), CDMX (`ssc.cdmx.gob.mx`), Edomex (`sseguridad.edomex.gob.mx`), Mor (`morelos.gob.mx`), Pue (`ssp.puebla.gob.mx`), **Tlax (`ssc.tlaxcala.gob.mx` y `ssctlaxcala.gob.mx`, devueltos SIN `site:`: primera vez en cinco ediciones)**, Gro (`guerrero.gob.mx`), Oax (`oaxaca.gob.mx/comunicacion`). **Siguen `NO REVISADA`**: BC (`seguridadbc.gob.mx` devuelto en una búsqueda de alto impacto, no de armamento), BCS, Dgo, Coah, Tamps, Jal, Nay, Hgo, Qro, Chis, QRoo |
| Prioridad — sentencias | **Revisadas**: BCS (`pgjebcs.gob.mx`), Chih, NL (`fiscalianl.gob.mx`, solo páginas estáticas), CDMX (`fgjcdmx.gob.mx`), Oax (**`portal.fgeo.gob.mx`, dominio real confirmado**), QRoo (**`fgeqroo.gob.mx`, dominio real confirmado**). **NO REVISADA**: Son (tercera edición), Sin (tercera edición), Gto, Hgo, Camp |
| Prioridad — alto impacto | BC, BCS, Son, Chih, Dgo, Coah, CDMX, Tlax, Camp: **revisadas por medios**, sin hecho propio salvo Chih (`ARG-130-008`) |
| Ciclo | **B** — Noreste + Golfo encabezaron el triaje judicial |
| Rendimiento | **Ninguna sentencia integrable.** El ciclo B halló Tamaulipas FGJE-370 (6-oct, seis sentenciados por desaparición, fuera de ventana), el índice FGJE-381 a 384 (ilegible) y un candidato de Zacatecas con `POSIBLE CASO HOMÓNIMO` |

Serie: C (125) sí · A (126) no · B (127) no · C (128) no · A (129) no · **B (130) no — candidatos, sin integrable.**

**No confirmados**: `fiscaliasinaloa.gob.mx`, `fiscalia.sonora.gob.mx`, dominio de la Fiscalía de Campeche (solo `x.com/fgecam`), `pgjhidalgo.gob.mx`,
fiscalía de Guanajuato (`fiscaliageneral.guanajuato.gob.mx` no devuelto), fiscalía de Baja California.

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **9-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |
| **10-oct** | `SIN RESULTADO INDEXADO EN VENTANA`: día suelto, rangos «9, 10 y 11» y «10 y 11», título sin `site:` |
| **11-oct** | `SIN RESULTADO INDEXADO EN VENTANA` |

Último indexado: acciones del **8-oct** (SICOM, Ahora Noticias, Certeza Diario, ABC Tlaxcala; Milenio «resultados 8 de octubre»). **Trampa de año**:
el rango devolvió `gob.mx/sspc/prensa/…-10-11-y-12-de-octubre-de-2025` (2025). `gabinetedeseguridad.gob.mx` devolvió la portada con el informe del
5-oct (publicado el 6-oct) → dominio revisado, SRIV. GN, Defensa y Marina: `NO REVISADA`.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Minatitlán** (`ARG-129-001`) | **Muere el segundo trabajador** la noche del 11-oct (hora solo por resumen): titulares de La Silla Rota **2026/10/12** (532586, «Muere segundo trabajador de Pemex tras ataque en refinería de Minatitlán»), López-Dóriga, N+ Veracruz y La Nigua (sin fecha); Milenio titula «dejó dos muertos». **Saldo de medios al 12-oct: 2 muertos.** Pemex: **primer comunicado, «dos lesionados»** (por cita); **segundo comunicado no localizado**. nvnoticias 2026/10/11 titula «Confirma Pemex muerte de trabajador»: única, contradicha. Mexican Times: «Fiscalía confirma un muerto» (titular). Hora del ataque: ~22:00, Latinus, solo por resumen; se descarta «cerca de medianoche». **Cero detenidos.** Un resumen con «7 detenidos» y «sicario fallecido» mezcla otro hecho: **rechazado**. **Seguimiento, no hecho nuevo**: una línea en la Valoración. La ficha de 129 no se corrige por fe de erratas: el saldo cambió después de su corte |
| **SEMAR 10-oct** (`ARG-129-005`) | Comunicado de la Cuarta Región Naval, cinco eventos **sin fecha por evento** («en días recientes», por resumen). **Las Porras: «1 larga, 29 cartuchos, 1 detenido» no aparece en ningún titular ni *slug*** (tres búsquedas con la cifra entre comillas). **VENCE → `ARG-130-FE-001`** (§8). Totales del comunicado, solo por resumen: 13 largas, 88 cargadores, 2,878 cartuchos, 2 detenidos, 7 AEI; titulares: Meganoticias «Marina asegura 13 armas y neutraliza siete explosivos en Sinaloa», Los Noticieristas 2026/10 «… 12 armas largas …» (contradicción 12/13). **7 AEI de Varados y Siqueros frente a `ARG-125-005`** («poblado Veranos», Gabinete 6-oct, por resumen): coinciden corporación, municipio, cifra y verbo; difiere la localidad (posible error de transcripción). **No resuelto: sigue `POSIBLE DUPLICIDAD — NO INTEGRAR`** |
| **Escuinapa** (`ARG-129-003`, `-004`) | **Hora no publicada en ningún resultado.** Vendedora: «mañana del sábado», solo por resumen; Madero entre Libertad y Belisario Domínguez. Sigue en 129 con `FRONTERA`; sin detenidos |
| **Zamora** (`ARG-129-REC-001`) | **Ningún detenido por el ataque**; carpeta no publicada. **Saldo contradicho**: 4 muertos por titular (Changoonga 2026/10/03, PorEsto 2026/10/3, Correo 2026/oct/04, IMN; Infobae 2026/10/06 titula «cuatro víctimas») frente a 5 solo por resumen (Infobae 2026/10/06). **Sin fe de erratas**: ver §8. Los 4 policías: robo calificado y ejercicio ilícito del servicio público (MVS 2026/10/5, Changoonga 2026/10/06); sin vinculación localizada |
| **Pinotepa** (`ARG-128-001`) | **Sin acto nuevo.** **3 muertos por titular** (Quadratín Oaxaca, sin fecha; Diario Marca 2026/10). SinEmbargo, «cuatro», solo por resumen. Viernes 9-oct por la tarde; 13a. Sur y 9a. Poniente. FGEO, disputa entre células, por cita. Sin detenidos. Mecanismo: solo «se solicitó», un medio |
| **San José del Rincón** (`ARG-128-003`) | **Tercera edición sin fuente con fecha del hecho.** Única URL con fecha: El Independiente **2026/10/12** (publicación, no hecho). Viernes 9-oct ~09:30, solo por resumen. **Decisión: se marca `FECHA NO ANCLADA` y se mantiene en la ventana de 128** con ★★☆☆☆; sale de los encargos y pasa a seguimiento de baja prioridad |
| **El Balcón** (`ARG-125-051`) | Sin acto nuevo. Amparo 412/2026 vigente (Réplica 2026/10/06; Crónica 2026/10/08). Sin peritaje oficial publicado. Marcha a Palacio Nacional: sin fecha. **No se describe el video** |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| Chipilo (`ARG-129-002`) | Sin acto nuevo; cero detenidos. Origen, por resumen: camioneta con reporte de robo. Vehículo: Tiguan (SSP) o Teramont (Infobae). Sigue 🟡 |
| Pachuca (`ARG-129-007`) | **630** por titular (La Silla Rota y Síntesis 2026/10/10) frente a **640** por titular de Zunoticia 2026/10/10. 540 + 90 = 630 solo por resumen. **Sigue contradicho por titular** |
| Los Pinos (`ARG-129-REC-002`) | Sin inventario oficial; sigue cualitativo |
| Penal El Castillo | Sin acto nuevo. Infobae 2026/10/11: «22 muertos en cinco episodios» (contexto). Ingreso de armas: armas de fuego frente a punzocortante, contradicho |
| Ensenada | **Sin pena**; individualización el **16-oct**; la FGE pide 210 años por persona (resumen) |
| Navolato, 80 años | Sin boletín en el dominio oficial (`fiscaliasinaloa.gob.mx` no devuelto, tercera edición) |
| Naucalpan (`-005`, `-006`) | **Noche del 8 al 9-oct** (Infobae 2026/10/09, Seuno 2026/10/09). Cierra |
| Celaya (`ARG-128-002`) | Crónica 2026/10/06: «3 armas de fuego» (titular), 2 detenidos; Celaya y Villagrán. Fuera de ventana |
| Michoacán, 12 cateos (`-REC-008`) | 10 detenidos, «4 armas» (Crónica 2026/10/09, Infobae 2026/10/10, solo por resumen), sin desglose; 2 agentes de la SSPC heridos |
| Sombrerete (`-REC-010`) | **185 frente a 39 detonadores: sin resolver.** NTR Zacatecas (2026/10): 39 detonadores y 146 conectores; mayoría: 185, solo por resumen |
| Borja | Sigue `POSIBLE DUPLICIDAD` con `ARG-126-REC-004` |
| Corregidora | Boletín oficial `fiscaliageneralqro.gob.mx/portal/2026/10/08/manuel-n-sentenciado…` (jueves 8-oct): ventana de 127; hora no fijada. **Cierra como seguimiento** |
| Zihuatanejo | ~150 desplazados (Infobae 2026/10/07); sin actualización |
| Mixtequilla | **Santa María Mixtequilla, Oaxaca** (Infobae 2026/10/06), no Veracruz: error de entidad en el pendiente |
| Comonfort, Hermosillo, Xalisco/La Curva | Sin resultado |
| Los Reyes | Changoonga 2026/10/09: 5 detenidos, 2 largas (resumen); 9-oct. Fuera de ventana |
| Huanímaro | AM 2026/10/07: 2 detenidos, 3 largas (slug de NPI), 3 cargadores, 68 cartuchos (resumen); fecha del hecho no fijada |
| Santa María Magdalena | Código Qro 2026/10/08: vinculación de tres (no sentencia); 3 cortas, 5 cargadores, >200 cartuchos, solo por resumen |
| Tetlatlahuca, Chiautempan | Sin resultado de octubre |
| Úrsula Camila Osorio | Localizada (Azteca Morelos, sin fecha); fuera de ventana |
| La Huerta (`ARG-127-REC-003`) | **Mismo hecho que «La Flaca» y «El Titi»** (Quadratín Tabasco). Cartuchos 540 (Gabinete) frente a 317 (desglose de Quadratín, cálculo propio): no conciliado; fecha 7 u 8-oct |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Jacona** (`ARG-130-001`) | 🔴 por **ataque del grupo criminal contra autoridades con muerte de personal** (2 policías municipales, por titular de Quadratín). Los 3 agresores abatidos por GN y Guardia Civil no mueven el color. **Saldo contradicho**: «6 muertos y 3 heridos» (titular de atiempo.mx atribuido a la FGE; La Voz, Telediario, Heraldo, Meganoticias) frente a «8 muertos y 6 heridos» (Quadratín, Excélsior, 24 Horas, En Blanco y Negro, Quinto Poder). Se integra **6** como cifra atribuida a la FGE; el total alternativo se declara. Hora ~12:30, solo por resumen (atribuida a la SSP): **`FRONTERA`** por caer el 11-oct, día de cierre de 129, sin hora citable; ningún indicio de hora anterior a las 08:58. Atecucario (Zamora): aseguramiento sin cifras, sin vínculo: no se ficha |
| **Cancún** (`-002`) | 🔴 por homicidio múltiple. ~20:30, solo por resumen; Noticaribe 2026/10/11 y cuatro regionales sin fecha |
| **Nacajuca** (`-003`) y **Morelia** (`-004`) | 🔴 por homicidio múltiple. **Madrugada del 11-oct (~03:00 y ~05:00), solo por resumen**: si se confirman, pertenecen a la ventana de 129. Por la regla de frontera, **se integran en la edición que los ve primero** con la marca, y la ficha lo declara. Si un ancla horaria citable los sitúa antes de las 08:58, se retiran por fe de erratas y pasan a 129 |
| **Navolato** (`-005`) | Luz Noticias y Línea Directa titulan el hallazgo con detalles distintos (envuelto en plástico / junto a la autopista); **se cuenta uno**; si son dos cuerpos, sube a rojo |
| **Acapulco** (`-007`) | 🟢 por detención. El ataque de octubre de 2025 no se recalifica. Armamento contradicho («dos armas de fuego» frente a «1 larga, 1 corta, 2 cargadores»), solo por resumen: cualitativo. «Siete detenidos» = acumulado del caso, no de este evento |
| **Ciudad Juárez** (`-008`) | 🟢. **1 revólver .38 y 34 cartuchos y 3 detenidos, por titular** (Diario de Juárez y El Diario de Chihuahua 2026/oct/11; La Opción 20261011). **Fecha del hecho no fijada: 10 u 11-oct, solo por resumen** (corrección de `procedencia-cifras`); si fue el 10-oct, sale de la ventana. Policía municipal. Integra al conteo con confianza Bajo (escala del módulo) y ★★★☆☆ en la ficha (escala general): dos escalas por diseño de `CLAUDE.md` |
| **Escuinapa, coordinador de Protección Civil** (`-009`) | **Omisión de la ola detectada por `procedencia-cifras`**. 🔴 por **víctima servidor público**. Titulares con fecha: Línea Directa 2026-10-11__1718412 («Confirman asesinato del director de Protección Civil de Escuinapa…»), ADN40 2026-10-11 («Reportan asesinato del titular de Protección Civil de Escuinapa, Sinaloa»), Infobae 2026/10/12 («… durante acciones por el huracán Simón»), Diario de Juárez y El Diario de Chihuahua 2026/oct/12; Reforma y TV Azteca sin fecha. Tarde del domingo, zona centro o calle Aldama, solo por resumen. **El nombre de la víctima no se reproduce en el cartelón.** `FRONTERA`. El resumen de `-006` (El Roblito) trae «~11:30, Aldama y Usumacinta»: posible mezcla; se declara en las dos fichas |
| **Guanajuato, boletín del 11-oct** | Hechos del 25 y 26-sep: `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`; fuera del total, una línea en el módulo de armamento |
| **Tijuana, llantera** (col. Los Altos) | 2 muertos y 1 herido, madrugada del 11-oct, solo por resumen; **ninguna URL con fecha** (Jornada BC, Síntesis TV, Blanco y Negro) → **no se ficha**; candidato para 131 |
| **Mazatlán ×2, Culiacán (Villas del Real), Ciudad Hidalgo (decapitado), Morelos (Pueblo Viejo), Apatzingán (herido)** | Sin URL con fecha o sin nota localizada → **no se fichan** |
| **Juchitán, La Ventosa** | El texto dice «este sábado» (10-oct) aunque el resumidor lo fecha el 11: **incoherencia interna**; ventana de 129, sin URL individual. Candidato: posible agresión a una autoridad auxiliar (agente municipal) |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-130-FE-001`** — **umbral de cifras arrastradas** sobre `ARG-129-005` / `ARG-129-ARM-001` (Las Porras): segunda edición solo por resumen.
  Se retiran **1 arma larga, 29 cartuchos y 1 detenido** → `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`. Se conserva la ficha
  🟡 (agresión a personal naval, titular de La Razón «… hay 2 detenidos» para el comunicado completo). **Armamento de 129 recalculado, cálculo
  propio**: largas **0**, cartuchos **0**, detenidos en evento de aseguramiento **0**.
- **`ARG-130-FE-002`** — **RETIRADA ANTES DE PUBLICAR** por `procedencia-cifras` (hallazgo 6): la subida de Zamora a 5 muertos descansaba solo en
  un resumen, y el titular del mismo Infobae dice «cuatro víctimas». **No se corrige 129**: el saldo de `ARG-129-REC-001` queda **4 por titular frente
  a 5 solo por resumen, sin arbitrar**. El ARG-ID `-FE-002` queda registrado como retirado y no se reutiliza.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV · Tijuana, sin URL con fecha | NO REVISADA (`seguridadbc.gob.mx` solo en la búsqueda de alto impacto) | NO REVISADA (fiscalía no devuelta) · Ensenada, veredicto |
| Baja California Sur | SRIV (medios) | NO REVISADA | SRIV (`pgjebcs.gob.mx`) |
| Sonora | SRIV | SRIV (`seguridad.sonora.gob.mx`) | NO REVISADA (tercera edición) |
| Chihuahua | **hecho** (Ciudad Juárez) | SRIV (`fiscalia.chihuahua.gob.mx`) · **hecho por medios** | SRIV (`fiscalia.chihuahua.gob.mx`) |
| Sinaloa | **hechos** (Navolato, Escuinapa ×2) | SRIV (`sspsinaloa.gob.mx`) | NO REVISADA (tercera edición) |
| Durango | SRIV | NO REVISADA | SRIV (`fiscalia.durango.gob.mx`) |
| Coahuila | SRIV (medios) | NO REVISADA | SRIV (`sitio.fgecoahuila.gob.mx`, indexa hasta agosto) |
| Nuevo León | SRIV | SRIV (`nl.gob.mx`, sin octubre) | SRIV (`fiscalianl.gob.mx`) · candidato del 10-oct |
| Tamaulipas | SRIV | NO REVISADA | SRIV (`fgjtam.gob.mx`; FGJE-381 a 384 ilegibles) |
| San Luis Potosí | SRIV | SRIV (**`seguridad.slp.gob.mx`**) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | SRIV | SRIV (`ssp.zacatecas.gob.mx`) | NO REVISADA (dominio no devuelto) · candidato del 11-oct, medios |
| Jalisco | SRIV | NO REVISADA | SRIV (`fiscalia.jalisco.gob.mx`) |
| Colima | SRIV | NO REVISADA | NO REVISADA |
| Nayarit | SRIV | NO REVISADA | SRIV (`fiscaliageneral.nayarit.gob.mx`) |
| Aguascalientes | NO REVISADA | NO REVISADA | NO REVISADA |
| Michoacán | **hechos** (Jacona, Morelia) | SRIV (`ssp.michoacan.gob.mx`) | NO REVISADA |
| Guanajuato | SRIV (medios) | SRIV (`boletines.guanajuato.gob.mx`; evento anterior) | NO REVISADA (dominio no devuelto) |
| Ciudad de México | SRIV | SRIV (`ssc.cdmx.gob.mx`) | SRIV (`fgjcdmx.gob.mx`) |
| Estado de México | SRIV | SRIV (`sseguridad.edomex.gob.mx`) | NO REVISADA |
| Morelos | SRIV | SRIV (`morelos.gob.mx`) | NO REVISADA |
| Puebla | SRIV | SRIV (`ssp.puebla.gob.mx`; resumen semanal sin año verificable, no usado) | NO REVISADA |
| Tlaxcala | SRIV (medios) | SRIV (**`ssc.tlaxcala.gob.mx`**, **`ssctlaxcala.gob.mx`**) | NO REVISADA |
| Hidalgo | SRIV | NO REVISADA | NO REVISADA · veredicto de Santiago Tulantepec |
| Querétaro | SRIV | NO REVISADA | SRIV (`fiscaliageneralqro.gob.mx`) |
| Veracruz | SRIV · seguimiento Minatitlán | SRIV (`veracruz.gob.mx`) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | **hecho** (Nacajuca) | SRIV (`tabasco.gob.mx`) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | **hecho** (Acapulco) | SRIV (`guerrero.gob.mx`; informe semanal del 5-oct) | NO REVISADA |
| Chiapas | SRIV | NO REVISADA | NO REVISADA |
| Oaxaca | SRIV · seguimiento Pinotepa | SRIV (`oaxaca.gob.mx/comunicacion`) | SRIV (**`portal.fgeo.gob.mx`**) |
| Campeche | SRIV (medios) | NO REVISADA | NO REVISADA (dominio no hallado) |
| Yucatán | SRIV | NO REVISADA | NO REVISADA |
| Quintana Roo | **hecho** (Cancún) | NO REVISADA | SRIV (**`fgeqroo.gob.mx`**) |

**Sentencias: 15 de 32; FGR no revisada; 17 `NO REVISADA`.** **Armamento: 17 de 32** (desde 9 en 129). **Alto impacto: 31 de 32, por búsqueda dirigida en medios** (criterio de 129 para este módulo; el del dominio oficial rige armamento y sentencias).

## 10. Hechos vistos y NO fichados, con motivo

- **Tijuana, llantera** (2 muertos, 1 herido): sin URL con fecha. **Mazatlán** (centro comercial; Puesta del Sol), **Culiacán, Villas del Real**
  (sin heridos), **Ciudad Hidalgo** (decapitado), **Morelos, Pueblo Viejo**, **Apatzingán** (herido): sin URL con fecha o sin nota.
- **Huejotzingo, Puebla** (3 cateos, 3 detenidos, 1 pistola, 1 cargador, 13 cartuchos): hecho del 10-oct, URLs sin fecha → candidato de 129.
- **Cancún SM 225** (8-oct, 5 largas, 1 corta, >1,000 cartuchos; Clic Noticias sin fecha) y **Puerto Cancún** (7-oct): no publicados; ventanas
  de 127 o 128; sin URL con fecha → pendientes.
- **Playa del Carmen** (mujer asesinada, noche del sábado 10-oct) y **Juchitán, La Ventosa** (sábado 10-oct): ventana de 129, sin URL individual.
- **CDMX, 4 detenidos por robo a tiendas** (Infobae 2026/10/12): sin armamento, sin alto impacto.
- **Jalisco, marcha por el agua** (39 detenidos, 59 heridos, El Universal sin fecha): orden público; no investigado.
- **Torreón, secundaria** (1-oct), **Reynosa, El Guerreño** (~2-oct), **Coahuila, San Vicente** (1-oct), **Durango, Nuevo Garabitos** (6-oct),
  **Mexicali** (5-oct), **Los Cabos** (23-sep): fuera de ventana.
- **Casino Royale**: juez ordena liberar a dos sentenciados (Infobae 2026/10/09): hecho judicial del 9-oct, fuera de ventana.

## 11. Desglose de cálculos propios

- Duración: 11-oct 08:58 → 12-oct 08:19 = **23 h 21 min** = 23,35 h. Densidad: 9 / 23,35 = **0,39**.
- Muertos en hechos propios: 6 (Jacona, cifra atribuida a la FGE: 2 policías, 3 agresores, 1 civil) + 2 (Cancún) + 3 (Nacajuca) + 2 (Morelia)
  + 1 (Navolato) + 1 + 1 (Escuinapa) = **16**; con 8 en Jacona, **18**. Heridos: 3 o 6 (Jacona) + 1 (Morelia) = **4 o 7**.
- Armamento propio: cortas 1, cartuchos 34, detenidos 3 — por titular.
- Frontera: **9 de 9**; con indicio de madrugada (posible ventana de 129): 2 (`-003`, `-004`).

## 12. Fuentes por ficha

- **`ARG-130-001`** — Institucional 1 (SSP y FGE Michoacán, por cita). Nacional 4: El Heraldo de México 2026/10/11 (906095); Excélsior; 24 Horas;
  Telediario. Regional 10: En Blanco y Negro 2026/10/11; La Voz de Michoacán; Quadratín («Suman 8 muertos y 6 heridos…»; «… 4 heridos y 2 policías
  muertos»); atiempo.mx («Eleva FGE a 6 muertos y 3 heridos…»); MiMorelia (n5594412, n5594398); Meganoticias 778095 y 778104; 1plana; Quinto Poder
  2026/10/12; La Prensa de Coahuila 2026/10/11; Contramuro. Abierta 1: Blog del Narco 2026/10 (`NO OFICIAL`).
- **`ARG-130-002`** — Regional 5: Noticaribe 2026/10/11; Depeso; SIPSE Novedades 516196; Periodistas Quintana Roo; El Congresista.
- **`ARG-130-003`** — Institucional 1 (FGE Tabasco, por titular de Quadratín Tabasco). Nacional 3: El Universal; Excélsior; N+. Regional 9: Quadratín
  Tabasco; Diario de Tabasco 2026/10/11; El Heraldo de San Luis Potosí 2026/10/11; El Mañana 2026/10/12 (182362); Azteca Chiapas («hoy-11-de-octubre»,
  *liveblog*); Dominio Público; Veracruz en Red; Posta vl2265341; La Prensa de Coahuila 2026/10/11.
- **`ARG-130-004`** — Regional 9: Contramuro («… deja 2 muertos y un herido»); MiMorelia; Respuesta Michoacán; IMN; Meganoticias; RED113; Quadratín («Ataque armado en negocio de micheladas deja 2 muertos en Morelia»); La Voz de Michoacán; Changoonga
  2026/10/11 («… hay dos muertos y un herido»).
- **`ARG-130-009`** — Nacional 4: ADN40 2026-10-11; Infobae 2026/10/12; Reforma; TV Azteca. Regional 3: Línea Directa 2026-10-11__1718412; Diario de
  Juárez 2026/oct/12; El Diario de Chihuahua 2026/oct/12.
- **`ARG-130-005`** — Regional 3: Luz Noticias 2026-10-11 (309266); Línea Directa 2026-10-11__1718258; Noroeste OB26413836.
- **`ARG-130-006`** — Regional 5: Línea Directa 2026-10-11__1718388; Noroeste IB26414682; Los Noticieristas 2026/10; Viva la Noticia; Canal 66.
- **`ARG-130-007`** — Institucional 1 (SSPC, anuncio del titular, por cita; Contramuro «Confirma SSPC…»). Nacional 7: El Financiero 2026/10/11;
  Proceso 2026/10/11 (381657); Infobae 2026/10/11; La Razón 2026/10/12; TV Azteca («… y 6 más»: acumulado del caso); Aristegui (1110); Quadratín México.
  Regional 7: El Universal San Luis (edición regional); Sur Acapulco (dos notas); Contramuro; Enfoque Noticias; Eje Central; Maya Comunicación; Trasfondo Informativo 2026/10.
- **`ARG-130-008`** — Regional 5: Diario de Juárez 2026/oct/11 (1142807); El Diario de Chihuahua 2026/oct/11 (846643); La Opción 20261011 (529693); El Bordo
  20261011 (mismo grupo que La Opción); Calibre 800 2026/10/11.
- **Sentencias** — Zacatecas: NTR Zacatecas 2026/10 («sentencian-a-jose…»), Imagenzac («fgjez-obtiene-condena…»); homónimo: NTR 2026/10 («sentencian-a-juan-n…»).
  NL: MVS 2026/10/10 (749349), Enfoque Monterrey 2026/10/10, El Mañana 2026/10/11 (182312), Milenio, Posta. Navolato: Noticiero Altavoz, Línea Directa
  2026-10-10__1717897, El Universal, Los Noticieristas 1146008. Hidalgo: Periódico Central 73605. Ensenada: Infobae 2026/10/10, Diario Tijuana 2026/10.

## 13. Los dos controles editoriales — ejecutados sobre la versión estable, los dos con «CORREGIR»

Racha: **dieciséis pases consecutivos, dieciséis «CORREGIR»** (quince hasta 129 + este). Lanzados en paralelo sobre el borrador validado y
commiteado (`92bca81`), con las notas de la ola (las de Occidente se añadieron tras el hallazgo 15 de `editor-duplicidad`).

**`editor-duplicidad`** (sin búsquedas) — **CORREGIR**. Ningún hecho duplicado ni ya publicado.

| # | Hallazgo | Disposición |
|---|---|---|
| 1 | «Sin fila — no hubo armamento asegurado» en `-001` y `-007` | **Corregido**: «evento cualitativo, cantidad no determinada» |
| 2 | Alto impacto 31/32 con la definición del dominio oficial; BC armamento por una búsqueda de alto impacto | **Corregido**: alto impacto «por búsqueda dirigida en medios»; BC armamento → `NO REVISADA`; **armamento 17 de 32** |
| 3 | «MADRUGADA» como dato en el panorama de `-003`, `-004` | **Corregido**: «HORA NO FIJADA»; Valoración 5 declara la retirada si se ancla antes de las 08:58 |
| 4 | Dos escalas de confianza en `-008` | **No se corrige**: escalas distintas por diseño de `CLAUDE.md` (★ general; Alto/Medio/Bajo en armamento y sentencias) |
| 5 | Fe de erratas fuera del cartelón | **No se corrige**: instrucción permanente del destinatario (ARGOS 109) |
| 6 | Jacona y Acapulco repetidos en el módulo de armamento; frase de método | **Corregido**: una sola mención por ARG-ID |
| 7 | Cifras en la portada («6 u 8», «siete») | **Corregido**: retiradas. Las acciones 2, 3 y 5 se mantienen: son seguimientos sin acto oficial nuevo |
| 8 | Valoración 4 sin fuente fechada; frase sin dato | **Corregido**: La Silla Rota 2026/10/12; «saldo oficial no localizado» |
| 9 | NL y Navolato sin marca de heredado | **Corregido**: «CANDIDATO HEREDADO DE ARGOS 129» |
| 10 | Clasificación de En Blanco y Negro; La Prensa de Coahuila | **Corregido**: En Blanco y Negro → regional. La Prensa de Coahuila: dos notas con *slug* propio, no *liveblog* |
| 11 | Regresión de cobertura por rotación | **Corregido** en `_pendientes.md` (prioridad en 131) |
| 12 | «los 1 ARG-ID» en el móvil | **Corregido** en `gen-movil.py` |
| 13-15 | §13, índice, notas de Occidente | **Corregido** |

**`procedencia-cifras`** (25 búsquedas, 0 `WebFetch`) — **CORREGIR**.

| # | Hallazgo | Disposición |
|---|---|---|
| 1 | **Omisión**: asesinato del coordinador de Protección Civil de Escuinapa (11-oct) | **Corregido**: `ARG-130-009` 🔴; propios 8 → **9**, rojos 4 → **5**, muertos 15/17 → **16/18**, densidad 0,34 → **0,39** |
| 2 | Fecha del hecho de Juárez = fecha de publicación | **Corregido**: «10 u 11-oct, solo por resumen» en ficha y tabla |
| 3 | Edades y «dos agresores» por resumen marcados como titular (Nacajuca, Cancún); hora 20:00–20:30 | **Corregido** |
| 4 | Acapulco: «1 detenido» inferido; «y 6 más» | **Corregido**: «1 en este evento, por titulares en singular»; acumulado declarado. «Un presunto sicario murió»: del ataque de 2025 según el resumen; no se integra |
| 5 | Zacatecas: fecha no anclada | **Corregido**: `FECHA NO ANCLADA`; posible republicación; indicador 1 → 0 |
| 6 | `ARG-130-FE-002` (Zamora, 5 muertos) solo por resumen y contradicha por titular | **Corregido**: **fe de erratas retirada**; contradicción registrada |
| 7 | `ARG-130-FE-001` (Las Porras) | **Confirmada** |
| R1-R8 | Composición de los saldos de Jacona y «4 heridos»; recuentos; lugar de Navolato; primera versión de Cancún; El Universal San Luis; Hidalgo y Ensenada; Navolato «70 años»; NL 105 por titular y deslinde; «ningún detenido publicado» | **Corregidos** |

**Segundo pase** — `validar.js` → **validación OK** (escritorio); `gen-movil.py` → **validación OK** (móvil); `.txt` regenerado. Sin presupuesto
para un segundo pase con búsqueda (194 de 200).

## 14. Herramientas

`tools/datos-argos-130.py` (desde 129; sin página de recuperaciones: ninguna en la edición; campo `cual=True` para fichas con aseguramiento
sin cifra). `gen-movil.py`: concordancia de «el ARG-ID / los N ARG-ID». `gen-texto.py` sin cambios. `validar.js`: OK.

## 15. Lecciones de método (no van al cartelón)

1. **La búsqueda nacional del coordinador por día volvió a dar el rojo principal** (Jacona), tercera edición seguida. Se mantiene.
2. **La cuota `site:` de armamento por entidad funcionó**: armamento sube de 9 a 17 entidades revisadas; Tlaxcala, por fin, devolvió su dominio
   buscado sin `site:`.
3. **Nueve de nueve hechos con `FRONTERA`**: el cierre de 129 a las 08:58 de un domingo deja todo el día 11 en frontera, y los hechos de madrugada
   (Nacajuca, Morelia) caen del lado de 129 si se confirma la hora. Un corte a medianoche o con hora de cierre fija reduciría la frontera.
4. **Sonora y Sinaloa, sentencias, tercera edición `NO REVISADA`**: el dominio de la fiscalía no aparece en el índice. Probar `fge.sonora.gob.mx`,
   `fiscalia.sinaloa.gob.mx` y la búsqueda por título del boletín sin `site:`.
5. **La ola omitió un rojo** (Escuinapa, coordinador de Protección Civil) que halló `procedencia-cifras`: el equipo Noroeste lo vio mezclado con El Roblito. Encargar a cada equipo una búsqueda por «servidor público / funcionario / director» asesinado en sus entidades.
