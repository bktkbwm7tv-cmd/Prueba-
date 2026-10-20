# ARGOS 138 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **lunes 19-oct-2026 11:05 CDMX** (donde cerró ARGOS 137). CIERRA: **martes 20-oct-2026 07:06 CDMX**. Duración 20 h 01 min.
- Calendario: domingo 18 · lunes 19 · martes 20. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- Un hecho del lunes 19 ANTES de las 11:05 pertenece a ARGOS 137 (ventana 18-oct 08:34 → 19-oct 11:05). Si 137 no lo publicó, es candidato `-REC-` (recuperación), no hecho del corte. Hechos del domingo 18 (y antes) que ninguna edición publicó: también `-REC-`.
- Hechos del lunes 19 (mediodía, tarde y noche) y de la madrugada del martes 20 (hasta 07:06) son el núcleo del corte. Hechos del martes 20 después de las 07:06 son de ARGOS 139: descártalos por ventana.
- Publicación el día 19 sin hora fijada → un hecho del lunes puede ser anterior a las 11:05: marca `PUBLICADO EL DÍA DE APERTURA SIN HORA`. Publicación el día 20 sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. Nunca infieras la hora. «Madrugada de este martes» en un resumen NO fecha un hecho.
- Criterio de inclusión (escrito en 137): entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida.
- Pistas de la consulta de control (sin verificar; todo por resumen): **Edomex** — Ecatepec, mecánico de 46 años y su hijo de 17 asesinados en su taller; Naucalpan, mujer muerta al manejar (El Independiente, ruta 2026/10/19, agregado: fija día y hora de cada uno) · **Mazatlán** — «ataques armados dejan tres fallecidos y un menor herido» (Diario de Yucatán 2026/10/19; agregado: ¿hechos del 18, ya en 137, o del 19 tras las 11:05?) · **Juchitán, Oaxaca** — col. Tomás Aquino, 2 muertos y 3 heridos, uno de 3 años (El Universal, sin fecha en ruta; ¿es el «panteón» heredado de 137?).

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del lunes 19 tarde-noche / martes 20 madrugada.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este lunes» / «la noche del lunes» / «madrugada de este martes» + entidades.
2. Fecha de cierre en la ruta: «2026/10/20», «20 de octubre» y «2026/10/19» — HAZLA AL FINAL de tu presupuesto, no al principio (el índice tarda en llegar a la noche).
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
Ejecuta LITERALMENTE, para cada topónimo (municipio y colonia), y **PEGA LA SALIDA** en el hecho:
```
cd /home/user/Prueba- && grep -il '<topónimo>' reports/argos-2026-10-15.html reports/argos-2026-10-16.html reports/argos-2026-10-17.html reports/argos-2026-10-18.html reports/argos-2026-10-19.html reports/indice-arg-id.md reports/argos-2026-10-19-fuentes.md reports/argos-2026-10-19-equipos.md
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

## Novedades de 138
- Sección **«AJENOS»** obligatoria: hechos de otra región que veas, con URL, sin gastar búsquedas en ellos.
- **Registra la URL completa de TODO resultado que respalde un dato.**
- Dominios corregidos en 137: `portal.fgeo.gob.mx`, `seguridad.slp.gob.mx`, `pgjebcs.gob.mx`, `fgecolima.mx`, `fgjem.edomex.gob.mx`, `spsc.campeche.gob.mx`, `ssp.yucatan.gob.mx`; y de 136: `fgenay.gob.mx`, `ssypc.nayarit.gob.mx`, `comunicacion.fiscaliamichoacan.gob.mx`, `comunicacion.fiscaliaveracruz.gob.mx`, `ssp.zacatecas.gob.mx`, `fiscalia.sonora.gob.mx`, `sitio.fgecoahuila.gob.mx`, `fiscalia-aguascalientes.gob.mx`.
- Dominios que NO devolvieron en 137 (prueba una variante): `fiscaliasinaloa.gob.mx`, `fiscalia.guanajuato.gob.mx`, `fiscalia.morelos.gob.mx`, `pgjhidalgo.gob.mx`, `ssp.chihuahua.gob.mx`, `ssp.durango.gob.mx`, `ssp.jalisco.gob.mx`, `ssp.col.gob.mx`, `ssp.aguascalientes.gob.mx`, `ssp.morelos.gob.mx`, `ssc.tlaxcala.gob.mx`, `seguridad.hidalgo.gob.mx`, `ssc.queretaro.gob.mx`.
- Color decidido por el destinatario para 138: **Cuajinicuilapa (aspirante de Morena, sábado 17) = 🔴**, se recupera (lo ficha el coordinador; no gastes búsquedas salvo dato nuevo).
- Ciclo de 138: **B** (Noreste + Golfo encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
