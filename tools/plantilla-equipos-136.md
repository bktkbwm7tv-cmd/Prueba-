# ARGOS 136 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **sábado 17-oct-2026 09:28 CDMX** (donde cerró ARGOS 135). CIERRA: **domingo 18-oct-2026 08:34 CDMX**. Duración 23 h 06 min.
- Calendario: viernes 16 · sábado 17 · domingo 18. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- Un hecho del sábado 17 ANTES de las 09:28 pertenece a ARGOS 135 (ventana 16-oct 11:34 → 17-oct 09:28). Si 135 no lo publicó, es candidato `-REC-` (recuperación), no hecho del corte. Hechos del viernes 16 (y antes) que ninguna edición publicó: también `-REC-`.
- Hechos del sábado 17 (mañana tras 09:28, tarde y noche) y madrugada del domingo 18 son el núcleo del corte.
- Publicación el día 17 sin hora fijada → hecho del sábado puede ser anterior a las 09:28: marca `PUBLICADO EL DÍA DE APERTURA SIN HORA`. Publicación el día 18 sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. Nunca infieras la hora.
- Pista de la consulta de control (sin verificar): Silao, Baños de Agua Caliente, pareja asesinada «mañana del sábado 17» (Milenio); Acapulco, col. Cuauhtémoc, 2 muertos y 3-4 heridos en local de comida (Quadratín Guerrero, sin fecha). Fija hora y día.

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del sábado 17 tarde-noche / domingo 18 madrugada.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este sábado» / «la noche del sábado» / «madrugada de este domingo» + entidades.
2. Fecha de cierre en la ruta: «2026/10/18», «18 de octubre» y «2026/10/17» — HAZLA AL FINAL de tu presupuesto, no al principio (el índice tarda en llegar a la noche).
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
Haz `grep -il <topónimo>` (municipio y colonia) en:
`reports/argos-2026-10-13.html reports/argos-2026-10-14.html reports/argos-2026-10-15.html reports/argos-2026-10-16.html reports/argos-2026-10-17.html reports/indice-arg-id.md reports/argos-2026-10-17-fuentes.md`
y declara el resultado de ese cotejo en cada hecho («no figura» / «es ARG-13X-0YY»). En 134 una recuperación propuesta era ARG-131-003, ya publicada. Lo mismo para cada `-REC-`.
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
