# ARGOS 141 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **domingo 25-oct-2026 07:45 CDMX** (donde cerró ARGOS 140). CIERRA: **hora real de arranque de la sesión de ARGOS 141** = **lunes 26-oct-2026 08:37 CDMX** (24 h 52 min).
- Calendario: miércoles 21 · jueves 22 · viernes 23 · sábado 24 · **domingo 25 · lunes 26 · martes 27**. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- **ARGOS 140 (ventana 21-oct 10:23 → 25-oct 07:45) ya publicó 23 hechos** —Iztapalapa (-001, -019), Purísima del Rincón (-002), Mazatlán San Fernando (-003), Culiacán Villa Bonita (-004), León cinco cuerpos (-005), Huimanguillo fosa y cabeza (-006, -007), Reynosa Puerta Sur (-008), Escuinapa camión (-009), Jiutepec (-010), Chimalhuacán (-011), Ozumba (-012), Linares La Petaca (-013), Irapuato La Lupita (-014), Valle de Santiago (-015), Indaparapeo (-016), Álamo/Papantla (-017), Cosoleacaque (-018), Xalapa detención (-020), Juchitán 7 detenidos (-021), Puebla/CDMX 36 armas (-022), Culiacán Los Ranas (-023)— y recuperó Ario de Rosales, Cocotitlán y Ecatepec Tulpetlac (-REC-001 a -003). Un hecho del 21 al 25 (antes de las 07:45) que 140 NO publicó es de la ventana de 140: candidato `-REC-` **solo si es de alto impacto (🔴)**; si es 🟡 o 🟢, va a «VISTOS».
- **Núcleo del corte**: hechos del **domingo 25 (tras las 07:45)** en adelante. Publicación del 25 sin hora fijada → `PUBLICADO EL DÍA DE APERTURA SIN HORA`; publicación del día de cierre sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`.
- **Fin de semana**: «fin de semana violento», «N muertos de viernes a domingo» son **balances**: nunca se reparten ni se integran.
- Nunca infieras la hora. «Esta mañana» o «madrugada de este lunes» en un resumen NO fecha un hecho.
- Criterio de inclusión: entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida (excepción declarada para rojos).

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del domingo 25 y del día de cierre.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este domingo» / «la noche del domingo» / «este lunes» / «madrugada de este lunes» + entidades.
2. Fecha en la ruta, UNA POR DÍA de la ventana («2026/10/25», «2026/10/26»…): **4 BÚSQUEDAS RESERVADAS** para esto, que no se gastan en otra cosa; hazlas AL FINAL.
3. «funcionario / director / servidor público / policía asesinado» en tu región.
4. «fosa / colectivo / restos / cuerpos» en tu región, **UNA CONSULTA POR ENTIDAD FRONTERIZA** (BC, Son, Chih, Tamps) — en 135 la consulta regional no trajo Cachanillas ni Nogales.
5b. ⚠️ **`site:` CON UN SOLO DOMINIO POR CONSULTA. NUNCA `OR` ENTRE DOMINIOS**: el buscador ignora el operador y la consulta se pierde (pasó en dos equipos de 140).
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
grep -il '<topónimo>' reports/argos-2026-10-18.html reports/argos-2026-10-19.html reports/argos-2026-10-20.html reports/argos-2026-10-21.html reports/argos-2026-10-25.html reports/indice-arg-id.md reports/argos-2026-10-25-fuentes.md reports/argos-2026-10-25-equipos.md
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

## Novedades de 141 (lecciones de 140)
- **Tope por equipo: 25 búsquedas, de ellas 4 reservadas a la fecha en la ruta por día.**
- **Las pistas del recall nacional del coordinador vienen en tu encargo**: el coordinador hace el recall ANTES de lanzarte. Verifícalas primero.
- **Seguimientos procesales de casos ya publicados** (vinculaciones, audiencias, impugnaciones) NO se proponen como fichas: van a «SEGUIMIENTOS» con su ARG-ID de origen.
- **Republicaciones del boletín federal** (SICOM, RED113, Talla Política, Ultranoticias, Certeza Diario y medios que reproducen el comunicado) = **una** fuente.
- ⚠️ **REPUBLICACIONES = UNA FUENTE** · ⚠️ **ECO DE CONSULTA**: la cifra solo vale en titular o *slug* · ⚠️ **RECUENTOS DE MEDIOS** nunca se integran · **cuerpos sin causa de muerte informada por autoridad**, aparte.
- Secciones obligatorias: **ENCARGOS, HECHOS DEL CORTE, CANDIDATOS -REC-, SEGUIMIENTOS, ARMAMENTO, SENTENCIAS, AJENOS, DESCARTADOS POR VENTANA, CORRECCIONES, INDICADOR DE COBERTURA**; URL completa de TODO resultado que respalde un dato; ordinales en titulares: busca el primero.
- **Dominios confirmados en 140**: `comunicacion.fiscaliaveracruz.gob.mx`, `portal.fgeo.gob.mx` (Oaxaca; no `fiscaliaoaxaca.gob.mx`), `fiscaliageneralqro.gob.mx`, `seguridad.slp.gob.mx`, `fgebc.gob.mx`, `fiscalia.chihuahua.gob.mx`, `fiscalia.durango.gob.mx`, `fgjcdmx.gob.mx`, `fiscalia.puebla.gob.mx`, `ssp.michoacan.gob.mx`, `fiscaliaguerrero.gob.mx`, `fge.chiapas.gob.mx`, `ssp.chiapas.gob.mx`, `fge.yucatan.gob.mx`; FGR en `fgr.org.mx` (listados). **Sin páginas en 140** (prueba una variante): `fge.sinaloa.gob.mx`, `fiscalia.tamaulipas.gob.mx`, `fiscalia.coahuila.gob.mx`, `fiscalia.zacatecas.gob.mx`, `fiscalia.campeche.gob.mx`, `fiscalia.tabasco.gob.mx`, `fiscalia.guanajuato.gob.mx`.
- Ciclo de 141: **B** (Noreste + Golfo encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
- **Prioridad sobre el ciclo** (cobertura de 140): **sentencias `NO REVISADA` (16)**: BCS, Son · NL, SLP · Jal, Col, Nay, Ags, Mich, Gto · Edomex, Mor · Tab · Oax, Gro, QRoo; **dominio sin páginas (5)**: Sin, Tamps, Coah, Zac, Camp. **Armamento `NO REVISADA` (17)**: BC, BCS, Son, Chih, Sin, Dgo · Jal, Col, Nay · Edomex, Mor, Pue, Tlax, Hgo, Qro · Camp, QRoo; **sin páginas (3)**: Zac, Gto, Tab. **Alto impacto con CONSULTA PROPIA obligatoria (16, solo amplia en 140)**: BCS, Son, Sin, Dgo · Jal, Col, Nay · CDMX, Mor, Pue, Tlax, Hgo, Qro · Chis, Camp, Yuc.
- **Boletín federal**: triple consulta para el 23, 24 y 25-oct y para cada día de la ventana (la hace el coordinador, y la repite al final de la ola).
