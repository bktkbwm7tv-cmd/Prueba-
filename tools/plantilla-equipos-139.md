# ARGOS 139 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **martes 20-oct-2026 07:06 CDMX** (donde cerró ARGOS 138). CIERRA: **miércoles 21-oct-2026 10:23 CDMX** (hora real de arranque de la sesión; duración 27 h 17 min). Una versión de 43 min se retiró por falta de materia: sus hallazgos están en `reports/_argos-139-retirado-*.md`.
- Calendario: domingo 18 · lunes 19 · **martes 20 · miércoles 21**. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- **ARGOS 138 (ventana 19-oct 11:05 → 20-oct 07:06) ya publicó 13 hechos**: Juchitán (-001), Cárdenas (-002), Culiacán Prados del Sol (-003) y 21 de Marzo (-004), Mazatlán San Joaquín (-005), plaza de La Marina (-006) y Lomas del Ébano (-012), Navolato La Palma (-007), Monterrey col. Hidalgo (-008), Juárez Los Alcaldes (-009/-010), Cadereyta (-011), Pénjamo (-013). Un hecho del lunes 19 tras las 11:05 o de la madrugada del martes 20 antes de las 07:06 que 138 NO publicó es de la ventana de 138: candidato `-REC-` **solo si es de alto impacto (🔴)**; si es 🟡 o 🟢, va a «VISTOS».
- **Núcleo del corte**: hechos del **martes 20-oct** (tras las 07:06) y de la **madrugada del miércoles 21** hasta el cierre, que ARGOS 138 no publicó. Publicación del 20 sin hora fijada y hecho no fechado → marca `PUBLICADO EL DÍA DE APERTURA SIN HORA`; publicación del 21 sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. Hechos posteriores al cierre son de ARGOS 140. Hechos con día del hecho (por resumen) lunes 19 publicados el 20: repórtalos con la marca, el coordinador decide (precedente de 138: Navolato).
- Nunca infieras la hora. «Madrugada de este martes» o «esta mañana» en un resumen NO fecha un hecho.
- Criterio de inclusión: entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida (excepción declarada para rojos).

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del lunes 19 tarde-noche / martes 20 madrugada.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este lunes» / «la noche del lunes» / «madrugada de este martes» + entidades.
2. Fecha en la ruta: «2026/10/20», «20 de octubre», «este martes», «la noche del martes», «2026/10/21», «madrugada de este miércoles» — HAZLA AL FINAL de tu presupuesto.
3. «funcionario / director / servidor público / policía asesinado» en tu región.
4. «fosa / colectivo / restos / cuerpos» en tu región, **UNA CONSULTA POR ENTIDAD FRONTERIZA** (BC, Son, Chih, Tamps) — en 135 la consulta regional no trajo Cachanillas ni Nogales.
5b. `site:` con UN SOLO DOMINIO por consulta: con `OR` el buscador ignora el operador.
5. Armamento: `site:` al dominio oficial de SSP/fiscalía de cada entidad que te toque por prioridad.
6. Sentencias: `site:` al dominio de la fiscalía de cada entidad que te toque por prioridad, con «sentencia condenatoria» / «condena».

## Criterio de cobertura (casillas)
- `REVISADA` (armamento o sentencias) = una búsqueda dirigida devolvió páginas del **dominio oficial de esa institución**. Un hecho hallado por medios NO cubre el dominio. `boletines.guanajuato.gob.mx` es del gobierno estatal, no de la fiscalía.
- Casillas: `SIN RESULTADO INDEXADO EN VENTANA` (SRIV, lo normal) · `SIN ACTUALIZACIÓN CONSTATADA` (no usar: no hay lectura directa) · `NO REVISADA` (no consultada). Alto impacto: declara qué entidades tuvieron consulta propia y cuáles solo consulta regional amplia.

## Procedencia (reglas duras)
- La fecha la fija la **URL o el titular**, nunca el resumen del buscador. Marca cada dato como «por fragmento/titular» o «SOLO POR RESUMEN».
- *Liveblog* (`en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`, agregados): nunca fecha un hecho ni es fuente única.
- Fecha del hecho, de publicación y de consulta: campos distintos.
- Criterio institucional: cuenta como fuente institucional solo una **declaración o comunicado citado de una autoridad nombrada** («la SSP informó», «la Fiscalía identificó»). «La Fiscalía investiga» NO cuenta.
- Sentencias: solo con término expreso de condena; sin boletín oficial = `PENDIENTE DE CONFIRMACIÓN OFICIAL`. Para identificar un caso: dos campos individualizadores coincidentes.
- Armamento: solo cantidades expresas; cortas/largas/cartuchos/cargadores por separado; «diverso armamento» = cualitativo.

## ANTES DE PROPONER UN HECHO COMO NUEVO (obligatorio, también para cada -REC-)
NO TIENES BASH. Usa la herramienta **Grep** (output_mode "files_with_matches", -i true, path /home/user/Prueba-/reports) con el topónimo como patrón y limita a estos archivos, y **PEGA LA SALIDA** en el hecho. Equivalente de referencia:
```
grep -il '<topónimo>' reports/argos-2026-10-16.html reports/argos-2026-10-17.html reports/argos-2026-10-18.html reports/argos-2026-10-19.html reports/argos-2026-10-20.html reports/indice-arg-id.md reports/argos-2026-10-20-fuentes.md reports/argos-2026-10-20-equipos.md reports/_argos-139-retirado-fuentes.md reports/_argos-139-retirado-equipos.md
```
Si sale algún archivo, abre la línea (`grep -n`) y declara si es el mismo hecho («es ARG-13X-0YY») o no. Sin la salida pegada, el hecho no se ficha.
Busca la **primera publicación** del hecho (la URL con fecha más temprana).

## Semáforo (propón color con rótulo breve)
- 🔴 homicidio múltiple, víctima autoridad/servidor público/periodista/persona defensora, ataque iniciado por el grupo contra fuerzas en patrullaje, fosa/restos, explosivos/drones, narcobloqueo, quema de vehículos.
- 🟡 homicidio doloso único sin agravantes, enfrentamiento derivado de operativo, agresión sin muertos, quién inició no determinado.
- 🟢 detenciones, aseguramientos, cateos, rescates. Delito y detención en la misma ventana = DOS hechos.
- Muertos del lado criminal no mueven el color.

## Formato del informe (además del formato de tu definición de agente)
Para cada HECHO DEL CORTE: entidad · municipio/colonia · día y hora (fuente de cada uno) · víctimas (muertos/heridos, sexo) · corporación · detenidos · armamento · color propuesto con rótulo · fuentes con URL completa, separando institucional / nacional / regional / abierta, y marcando cuáles llevan fecha en la ruta · primera publicación · cotejo grep · reservas.
Secciones obligatorias: ENCARGOS (respuesta a cada uno, aunque sea «sin novedad»), HECHOS DEL CORTE, CANDIDATOS -REC-, ARMAMENTO, SENTENCIAS, DESCARTADOS POR VENTANA, CORRECCIONES A EDICIONES ANTERIORES, INDICADOR DE COBERTURA por entidad (alto impacto / armamento / sentencias).
Entrega el informe ÍNTEGRO en tu mensaje final: el coordinador lo pasará tal cual a los controles editoriales.

## Novedades de 139
- Sección **«AJENOS»** obligatoria: hechos de otra región que veas, con URL, sin gastar búsquedas en ellos.
- **Registra la URL completa de TODO resultado que respalde un dato.**
- **ORDINALES EN TITULARES** («segundo homicidio…», «tercer ataque…»): busca siempre el primero.
- Dominios que NO devolvieron en 138 (prueba una variante): `fiscaliasinaloa.gob.mx` (undécima edición; prueba `fge.sinaloa.gob.mx`, `fiscaliasinaloa.mx`), `sspguerrero.gob.mx`, `ssp.nl.gob.mx`, `ssp.morelos.gob.mx`, `ces.morelos.gob.mx`, `sspc.tlaxcala.gob.mx`, `ssp.hidalgo.gob.mx`, `ssc.queretaro.gob.mx`, `seguridad.jalisco.gob.mx`, `fgecam.gob.mx`, `gabinetedeseguridad.gob.mx`.
- Dominios que sí devolvieron antes: `portal.fgeo.gob.mx`, `seguridad.slp.gob.mx`, `pgjebcs.gob.mx`, `fgecolima.mx`, `fgjem.edomex.gob.mx`, `spsc.campeche.gob.mx`, `ssp.yucatan.gob.mx`, `fgenay.gob.mx`, `ssypc.nayarit.gob.mx`, `comunicacion.fiscaliamichoacan.gob.mx`, `comunicacion.fiscaliaveracruz.gob.mx`, `ssp.zacatecas.gob.mx`, `fiscalia.sonora.gob.mx`, `sitio.fgecoahuila.gob.mx`, `fiscalia-aguascalientes.gob.mx`.
- **Criterio de lectura parcial**: parcial si el último ítem indexado del dominio es anterior al 1-sep-2026 o la ruta es opaca sin fecha.
- Color decidido por el destinatario para 139: **Río Bravo (diputada federal herida con arma blanca; noche del sábado 10-oct por resumen, ventana de ARGOS 129) = 🔴 `-REC-`**: lo ficha el coordinador; no gastes búsquedas salvo dato nuevo.
- Ciclo de 139: **C** (Occidente + Sureste encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
- **Prioridad sobre el ciclo** (cobertura de la versión retirada, que rige sobre la de 138): **sentencias `NO REVISADA` (14)**: Sin, Son, Dgo · Coah, NL, SLP, Zac · Gto · Mor, Tlax, Hgo · Chis, Camp, Yuc. **Armamento `NO REVISADA` (19)**: BC, BCS, Son, Dgo · NL · Jal, Nay, Ags, Col, Gto · CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro · Gro, Chis. **Alto impacto con CONSULTA PROPIA obligatoria (11, solo regional amplia en la retirada)**: BCS, Dgo, Coah, SLP, Zac, CDMX, Pue, Tlax, Qro, Camp, Yuc.
- **Encargos ya resueltos en la versión retirada (no repetir búsqueda salvo dato nuevo)**: Ecatepec Colosio (no fichar sin nota propia fechada) · «El Charro» (Guerrero, no es ARG-136-008) · narcomanta (Ciudad Juárez) · Puerto Morelos · Laureles Pinos · Palmanova · Cotija · Tlalnepantla (dos homónimos) · Ensenada («a cada uno»).
- **Boletín federal**: triple consulta para el 19, 20 y 21-oct (la hace el coordinador).
