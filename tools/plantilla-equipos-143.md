# ARGOS 143 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **martes 27-oct-2026 08:45 CDMX** (donde cerró ARGOS 142). CIERRA: **hora real de arranque de la sesión de ARGOS 143** (**miércoles 28-oct-2026 08:28 CDMX**).
- Calendario: sábado 24 · domingo 25 · lunes 26 · **martes 27 · miércoles 28 · jueves 29** · viernes 30. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- **ARGOS 142 (ventana 26-oct 08:37 → 27-oct 08:45) ya publicó 13 hechos** —Tecate FESC (-001) y su detención (-009), Tecate El Escorial (-002), Tehuacán agente de la AEI (-003) y su detención (-010), Acámbaro Velasco Ibarra (-004), Cutzato fosa (-005), León Valle de San Bernardo (-006), Apatzingán mercado (-007), SLP Periférico/Tierra Blanca (-008), Cajeme Xochiloa (-011), Queréndaro taller (-012), Morelia–Tumbisca (-013, FRONTERA)— y ninguna recuperación. Un hecho del 26 (tras las 08:37) o del 27 antes de las 08:45 que 142 NO publicó es de la ventana de 142: candidato `-REC-` **solo si es de alto impacto (🔴)**; si es 🟡 o 🟢, va a «VISTOS».
- **Núcleo del corte**: hechos del **martes 27 (tras las 08:45)** en adelante. Publicación del 27 sin hora fijada → `PUBLICADO EL DÍA DE APERTURA SIN HORA`; publicación del día de cierre sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`.
- **Fin de semana**: «fin de semana violento», «N muertos de viernes a domingo» son **balances**: nunca se reparten ni se integran.
- Nunca infieras la hora. «Esta mañana» o «madrugada de este lunes» en un resumen NO fecha un hecho.
- Criterio de inclusión: entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida (excepción declarada para rojos).

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del martes 27 antes de las 08:45 (solo 🔴, candidatos `-REC-`) y del día de cierre.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este martes» / «la noche del martes» / «este miércoles» / «madrugada de este miércoles» + entidades.
2. Fecha en la ruta, UNA POR DÍA de la ventana («2026/10/27», «2026/10/28»…): **4 BÚSQUEDAS RESERVADAS** para esto, que no se gastan en otra cosa; hazlas AL FINAL.
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
grep -il '<topónimo>' reports/argos-2026-10-20.html reports/argos-2026-10-21.html reports/argos-2026-10-25.html reports/argos-2026-10-26.html reports/argos-2026-10-27.html reports/indice-arg-id.md reports/argos-2026-10-27-fuentes.md reports/argos-2026-10-27-equipos.md
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

## Novedades de 143 (lecciones de 142)
- **Tope por equipo: 25 búsquedas, de ellas 4 reservadas a la fecha en la ruta por día.**
- **Las pistas del recall nacional del coordinador vienen en tu encargo**: el coordinador hace el recall ANTES de lanzarte. Verifícalas primero.
- **Seguimientos procesales de casos ya publicados** (vinculaciones, audiencias, impugnaciones) NO se proponen como fichas: van a «SEGUIMIENTOS» con su ARG-ID de origen.
- ⚠️ **REPUBLICACIONES = UNA FUENTE** · ⚠️ **ECO DE CONSULTA**: la cifra solo vale en titular o *slug* · ⚠️ **RECUENTOS DE MEDIOS** nunca se integran · **cuerpos sin causa de muerte informada por autoridad**, aparte.
- ⚠️ **NUEVO (142): UN ROJO SIN RUTA FECHADA NO SE DEJA EN VISTOS SIN BUSCARLO.** Queréndaro y Tumbisca llegaron de la ola con ruta sin fecha (Quadratín) y procedencia-cifras halló sus rutas del 26 (Grupo Marmor, Medianews): si ves un 🔴 sin fecha, **gasta una búsqueda en hallar una ruta fechada** antes de entregarlo.
- ⚠️ **NUEVO (142): HORA POR TITULAR ≠ HORA POR RESUMEN.** «Tarde del lunes» solo vale si está en el titular o el *slug*; en Tecate estaba solo en el cuerpo (resumen).
- ⚠️ **NUEVO (141): HORA DEL HECHO FRENTE AL CIERRE.** Si varios resúmenes coinciden en una hora posterior al cierre, el hecho es de la edición siguiente (Tehuacán salió así de 141). Reporta todas las horas que veas, con su medio.
- ⚠️ **NUEVO (141): AGREGADO FEDERAL DE FIN DE SEMANA.** Una acción del agregado sin nota propia fechada NO fija día: va a vistos. Si encuentras la nota propia con fecha, tráela.
- ⚠️ **NUEVO (141): SINÓNIMOS DE MUNICIPIO Y COLONIA.** Dos notas del mismo municipio con distinta colonia son, salvo prueba, hechos distintos (Pénjamo «zona centro» ≠ col. Lázaro Cárdenas).
- Secciones obligatorias: **ENCARGOS, HECHOS DEL CORTE, CANDIDATOS -REC-, SEGUIMIENTOS, ARMAMENTO, SENTENCIAS, AJENOS, DESCARTADOS POR VENTANA, CORRECCIONES, INDICADOR DE COBERTURA**; URL completa de TODO resultado que respalde un dato; ordinales en titulares: busca el primero.
- **Dominios confirmados (140-142)**: `comunicacion.fiscaliaveracruz.gob.mx`, `portal.fgeo.gob.mx`, `fiscaliageneralqro.gob.mx`, `seguridad.slp.gob.mx`, `fgebc.gob.mx`, `fiscalia.chihuahua.gob.mx`, `fiscalia.durango.gob.mx`, `fgjcdmx.gob.mx`, `fiscalia.puebla.gob.mx`, `ssp.michoacan.gob.mx`, `fiscaliaguerrero.gob.mx`, `ssp.chiapas.gob.mx`, `fge.yucatan.gob.mx`, **`fgjtam.gob.mx`, `fiscaliazacatecas.gob.mx`, `fiscaliasinaloa.mx`, `fiscaliatabasco.gob.mx`, `tabasco.gob.mx` (SSP), `portal.fgeguanajuato.gob.mx`, `fiscalia-aguascalientes.gob.mx`, `fgeqroo.gob.mx`, `fiscalianl.gob.mx`, `fiscaliaslp.gob.mx`, `fiscaliamorelos.gob.mx`, `fgjem.edomex.gob.mx`, `fiscalia.jalisco.gob.mx`**; **nuevos en 142**: `fge.chiapas.gob.mx`, `fgecolima.mx` (Col), `comunicacion.fiscaliamichoacan.gob.mx` (Mich), `pgjebcs.gob.mx` (BCS), `www.veracruz.gob.mx/seguridad/` (SSP Ver), `ssp.yucatan.gob.mx`, `ssc.qroo.gob.mx`; FGR en `fgr.org.mx` (listados). **Sin páginas en 142** (prueba una variante): `fgjes.sonora.gob.mx` (prueba `fiscalia.sonora.gob.mx`), `fiscalia.coahuila.gob.mx` y `fge.coahuila.gob.mx` (prueba `fiscaliageneral.coahuila.gob.mx`), `fiscaliageneralnayarit.gob.mx` (prueba `fgenay.gob.mx`), `fgecampeche.gob.mx` y `fiscalia.campeche.gob.mx`, `ssp.oaxaca.gob.mx`, `ssp.veracruz.gob.mx` (no existe), PGJEH de Hidalgo (sin dominio).
- Ciclo de 143: **A** (Noroeste + Centro encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
- **Prioridad sobre el ciclo** (cobertura de 142): **sentencias `NO REVISADA` (9)**: NL, Tamps · Ags, Gto · CDMX, Edomex, Mor, Tlax, Hgo (**Tlax y Hgo, dos ediciones seguidas**); **dominio sin páginas (4)**: Son, Coah, Nay, Camp. **Armamento `NO REVISADA` (20)**: BC, BCS, Son, Sin, Chih, Dgo · Coah, Zac · Jal, Nay, Ags, Gto · CDMX, Mor, Pue, Tlax, Hgo, Qro · Chis, Camp; sin páginas: Oax. **Alto impacto con CONSULTA PROPIA obligatoria (10, solo amplia en 142)**: BCS, Son, Sin · Jal, Col, Nay · CDMX, Tlax (**Tlax, dos ediciones**) · Camp, Yuc.
- **Boletín federal**: triple consulta para el 26-oct (seguía sin indexar al cierre de 142), el 27-oct y cada día de la ventana (la hace el coordinador, y la repite al final de la ola).
