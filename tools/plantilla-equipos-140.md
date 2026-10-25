# ARGOS 140 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **miércoles 21-oct-2026 10:23 CDMX** (donde cerró ARGOS 139). CIERRA: **domingo 25-oct-2026 07:45 CDMX** (hora real de arranque; ventana de 93 h 22 min). **VENTANA LARGA (~90-95 h)**: la orden del 22-oct no se ejecutó.
- Calendario: lunes 19 · martes 20 · **miércoles 21 · jueves 22 · viernes 23 · sábado 24 · domingo 25**. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- **ARGOS 139 (ventana 20-oct 07:06 → 21-oct 10:23) ya publicó 10 hechos**: Mazatlán Villa Unión (-001), Jalpa y Moyahua (-002), Juchitán trabajador municipal (-003), Mazatlán Infonavit Playas (-004) y La Foresta (-010), Xalapa (-005), Tezontepec El Chamizal (-006), Ciudad Juárez Cerradas de San Pedro (-007), Uruapan Los Cipreses (-008), San Luis Potosí Rocha Cordero (-009); y recuperó Río Bravo, El Terrero y Miahuatlán (-REC-001 a -003). Un hecho del martes 20 o de la mañana del miércoles 21 antes de las 10:23 que 139 NO publicó es de la ventana de 139: candidato `-REC-` **solo si es de alto impacto (🔴)**; si es 🟡 o 🟢, va a «VISTOS».
- **Núcleo del corte**: hechos del **miércoles 21 (tras las 10:23) al domingo 25** hasta el cierre. **Una ventana larga absorbe recuperaciones**: todo lo de esos cinco días es hecho propio, no `-REC-`. Publicación del 21 sin hora fijada → `PUBLICADO EL DÍA DE APERTURA SIN HORA`; publicación del 25 sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. Hechos posteriores al cierre son de ARGOS 141.
- **Fin de semana**: «fin de semana violento», «N muertos de viernes a domingo» son **balances**: nunca se reparten ni se integran; sirven para buscar cada hecho con su propia nota.
- Nunca infieras la hora. «Esta mañana» o «madrugada de este sábado» en un resumen NO fecha un hecho.
- Criterio de inclusión: entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida (excepción declarada para rojos).

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del viernes 23 al domingo 25.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este jueves» / «este viernes» / «este sábado» / «este domingo» / «fin de semana» + entidades.
2. Fecha en la ruta, UNA POR DÍA: «2026/10/21», «2026/10/22», «2026/10/23», «2026/10/24», «2026/10/25» (o «21 de octubre» … «25 de octubre») — HAZLA AL FINAL de tu presupuesto.
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
grep -il '<topónimo>' reports/argos-2026-10-16.html reports/argos-2026-10-17.html reports/argos-2026-10-18.html reports/argos-2026-10-19.html reports/argos-2026-10-20.html reports/argos-2026-10-21.html reports/indice-arg-id.md reports/argos-2026-10-21-fuentes.md reports/argos-2026-10-21-equipos.md
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

## Novedades de 140 (lecciones de 139 y de las ventanas largas 119 y 122)
- **Tope por equipo: 25 búsquedas** (ventana larga; el coordinador hace el recall nacional por día y la triple consulta federal de cinco días).
- **Lección de 122**: los barridos no detectaron ninguno de los ataques con víctimas civiles; los trajo el recall. **Dedica al menos 4 búsquedas a violencia de alto impacto** (ataque armado, masacre, emboscada, funcionario asesinado, fosa) en tus entidades, repartidas entre jueves-viernes y sábado-domingo.
- Sección **«AJENOS»** obligatoria; **URL completa de TODO resultado** que respalde un dato; **ordinales en titulares**: busca el primero.
- ⚠️ **REPUBLICACIONES = UNA FUENTE**: varias notas con el mismo título o *slug* (mismo grupo o réplica) se cuentan **una vez**. En 139: Diario de Juárez = Diario de Chihuahua; Grupo Marmor = MediaNews = Red Michoacán; Diario de Yucatán reproduce a El Universal.
- ⚠️ **ECO DE CONSULTA**: si pones una cifra entre comillas, el resumen puede devolvértela sin respaldo («17 cargadores» de 139). **La cifra solo vale si aparece en un titular o *slug***; si no, `SOLO POR RESUMEN`.
- ⚠️ **RECUENTOS DE MEDIOS** («seis asesinados este martes», «cinco en 24 horas»): sirven para buscar cada hecho; **nunca se integran** ni fechan nada. Identifica cada víctima con su propia nota.
- **Cuerpos sin causa de muerte informada** se reportan aparte («cuerpos hallados»), no como muertos por agresión.
- **Criterio de lectura parcial**: parcial si el último ítem indexado del dominio es anterior al 1-sep-2026 o la ruta es opaca sin fecha.
- **Dominios confirmados en 139**: `fge.chiapas.gob.mx`, `fge.yucatan.gob.mx`, `ssp.chiapas.gob.mx`, `fiscalia.durango.gob.mx` (portada con boletines de octubre), `fiscaliaguerrero.gob.mx`. **Sin páginas** (prueba una variante): `fge.sinaloa.gob.mx`, `pgjhidalgo.gob.mx`, `fiscalia.tlaxcala.gob.mx` (prueba `pgjtlaxcala.gob.mx`), `fiscalia.campeche.gob.mx`, `ssp.guerrero.gob.mx`, `seguridad.nl.gob.mx`, `ssp.durango.gob.mx`, `ssp.bajacalifornia.gob.mx`, `sspes.sonora.gob.mx`, `ssp.hidalgo.gob.mx`, `ssp.morelos.gob.mx`, `ssc.queretaro.gob.mx`, `seguridadypaz.guanajuato.gob.mx`.
- Ciclo de 140: **A** (Noroeste + Centro encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
- **Prioridad sobre el ciclo** (cobertura de 139): **sentencias `NO REVISADA` (11)**: BC, BCS, Chih, Sin · Tamps · CDMX, Pue, Tlax, Hgo, Qro · Camp. **Armamento `NO REVISADA` (19)**: BC, Son, Dgo, Chih, Sin · Coah, NL, Tamps, SLP · Mich, Gto · Mor, Tlax, Hgo · Gro, Oax, Camp, Yuc, QRoo. **Alto impacto con CONSULTA PROPIA obligatoria (7, solo amplia en 139)**: BC, Chih, Coah, NL, Ags, Gto, Edomex.
- **Boletín federal**: triple consulta para el 21, 22, 23, 24 y 25-oct, con rango «del 23 al 25» (la hace el coordinador, y la repite al final de la ola: el del 19-oct se indexó con un día de retraso).
