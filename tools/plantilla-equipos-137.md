# ARGOS 137 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **domingo 18-oct-2026 08:34 CDMX** (donde cerró ARGOS 136). CIERRA: **lunes 19-oct-2026 11:05 CDMX**. Duración 26 h 31 min.
- Calendario: sábado 17 · domingo 18 · lunes 19. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- Un hecho del domingo 18 ANTES de las 08:34 (madrugada del domingo) pertenece a ARGOS 136 (ventana 17-oct 09:28 → 18-oct 08:34). Si 136 no lo publicó, es candidato `-REC-` (recuperación), no hecho del corte. Hechos del sábado 17 (y antes) que ninguna edición publicó: también `-REC-`.
- Hechos del domingo 18 (mañana tras 08:34, tarde y noche) y de la madrugada y mañana del lunes 19 (hasta 11:05) son el núcleo del corte. Hechos del lunes 19 después de las 11:05 son de ARGOS 138: descártalos por ventana.
- Publicación el día 18 sin hora fijada → un hecho del domingo puede ser anterior a las 08:34: marca `PUBLICADO EL DÍA DE APERTURA SIN HORA`. Publicación el día 19 sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. Nunca infieras la hora. «Madrugada de este domingo» en un resumen NO fecha un hecho, y si fuera del domingo antes de las 08:34 sería de 136.
- Pistas de la consulta de control (sin verificar, todo por resumen): Copanatoyac (Gro.), ataque a familia que vendía cocos, 2 muertos y 2 heridos, «18 de octubre» (Quadratín Guerrero, sin fecha en ruta) · Acapulco, «cinco muertos y tres heridos en jornada violenta» entre la noche del sábado y el domingo (El Sur Acapulco, sin fecha en ruta) · Colima, «El Español» y «Santos» muertos en enfrentamiento con Marina y policía estatal (Infobae, sin fecha) · Monterrey, joven de 25 años muerto por arma de fuego (Telediario, sin fecha) · *liveblog* Infobae 2026/10/18: exfiscal de Chihuahua, primera audiencia «este domingo». Fija día y hora de cada uno.

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del domingo 18 tarde-noche / lunes 19 madrugada.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este domingo» / «la noche del domingo» / «madrugada de este lunes» + entidades.
2. Fecha de cierre en la ruta: «2026/10/19», «19 de octubre» y «2026/10/18» — HAZLA AL FINAL de tu presupuesto, no al principio (el índice tarda en llegar a la noche).
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
`reports/argos-2026-10-14.html reports/argos-2026-10-15.html reports/argos-2026-10-16.html reports/argos-2026-10-17.html reports/argos-2026-10-18.html reports/indice-arg-id.md reports/argos-2026-10-18-fuentes.md reports/argos-2026-10-18-equipos.md`
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

## Novedades de 137
- Dominios corregidos: Nayarit fiscalía `fgenay.gob.mx`, SSP `ssypc.nayarit.gob.mx` · Michoacán `comunicacion.fiscaliamichoacan.gob.mx` · Veracruz `comunicacion.fiscaliaveracruz.gob.mx` · Zacatecas SSP `ssp.zacatecas.gob.mx` · Sonora fiscalía `fiscalia.sonora.gob.mx` · Coahuila `sitio.fgecoahuila.gob.mx` · Aguascalientes `fiscalia-aguascalientes.gob.mx`.
- **Registra la URL completa de TODO resultado que respalde un hecho** (también los que solo confirmen un dato): en 136 faltaron URL que luego hubo que recuperar.
- Si encuentras un hecho de OTRA región, pásalo al coordinador en una sección «AJENOS» sin gastar búsquedas en él.
- Colores decididos por el destinatario para 137: San Baltazar Tetela queda 🟡 (no se recupera). Tanquián (`ARG-136-REC-002`): 🔴 solo si una autoridad nombrada confirma que la víctima era de la GN; si no se acredita, 🟡.
- Ciclo de rotación de 137: **A** (Noroeste + Centro encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
