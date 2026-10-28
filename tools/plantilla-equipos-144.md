# ARGOS 144 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **miércoles 28-oct-2026 08:28 CDMX** (donde cerró ARGOS 143). CIERRA: **hora real de arranque de la sesión de ARGOS 144** (el coordinador la escribe aquí al copiar la plantilla: ____).
- Calendario: lunes 26 · martes 27 · **miércoles 28 · jueves 29 · viernes 30** · sábado 31. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- **ARGOS 143 (ventana 27-oct 08:45 → 28-oct 08:28) ya publicó 10 hechos propios** —Celaya carretera Salvatierra–Celaya (-001), Celaya Mercado de Abastos (-002), Salamanca San Roque (-003), Chihuahua Sol de Oriente (-004), Tijuana Lomas de San Antonio (-005), Guadalupe Valle Soleado (-006), Culiacán Chulavista (-007), Culiacán Aguaruto (-008), Veracruz col. Centro (-009), Rayón (-010)— y **cuatro recuperaciones**: Tecate fosa (REC-001), Dolores Hidalgo florería (REC-002), Acámbaro Campamento Ferrocarrilero (REC-003), Tabasco Villahermosa–Frontera (REC-004). Un hecho del 27 (tras las 08:45) o del 28 antes de las 08:28 que 143 NO publicó es de la ventana de 143: candidato `-REC-` **solo si es de alto impacto (🔴)**; si es 🟡 o 🟢, va a «VISTOS».
- **Núcleo del corte**: hechos del **miércoles 28 (tras las 08:28)** en adelante. Publicación del 28 sin hora fijada → `PUBLICADO EL DÍA DE APERTURA SIN HORA`; publicación del día de cierre sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. ⚠️ **Si el único dato de día de una nota del 28 («ayer») apunta al 27, el hecho es de la ventana de 143** (lección de Tabasco).
- **Fin de semana**: «fin de semana violento», «N muertos de viernes a domingo» son **balances**: nunca se reparten ni se integran.
- Nunca infieras la hora. «Esta mañana» o «madrugada de este lunes» en un resumen NO fecha un hecho.
- Criterio de inclusión: entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida (excepción declarada para rojos).

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del martes 27 antes de las 08:45 (solo 🔴, candidatos `-REC-`) y del día de cierre.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este miércoles» / «la noche del miércoles» / «este jueves» / «madrugada de este jueves» + entidades.
2. Fecha en la ruta, UNA POR DÍA de la ventana («2026/10/28», «2026/10/29»…): **4 BÚSQUEDAS RESERVADAS** para esto, que no se gastan en otra cosa; hazlas AL FINAL.
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
grep -il '<topónimo>' reports/argos-2026-10-21.html reports/argos-2026-10-25.html reports/argos-2026-10-26.html reports/argos-2026-10-27.html reports/argos-2026-10-28.html reports/indice-arg-id.md reports/argos-2026-10-28-fuentes.md reports/argos-2026-10-28-equipos.md
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

## Novedades de 144 (lecciones de 143)
- **Tope por equipo: 25 búsquedas, de ellas 4 reservadas a la fecha en la ruta por día.** Las pistas del recall vienen en tu encargo: verifícalas primero.
- ⚠️ **NUEVO (143): «AYER» EN UNA NOTA DEL DÍA DE APERTURA.** Si el único dato del día (por resumen) sitúa el hecho en la ventana anterior, propónlo como `-REC-` (si es 🔴) o visto, no como hecho del corte.
- ⚠️ **NUEVO (143): DECLARACIÓN NOMBRADA POR TITULAR.** En todo hecho con fuerzas federales o estatales, una búsqueda por «secretario / Harfuch / Fiscalía informa» + topónimo: en Celaya había cuatro titulares con la declaración del secretario.
- ⚠️ **NUEVO (143): ANTES DE «FUENTE ÚNICA», UNA BÚSQUEDA POR EL TOPÓNIMO EXACTO.** Tres falsas fuentes únicas en 143.
- ⚠️ **NUEVO (143): SEÑUELOS DE «ESTE MARTES / MIÉRCOLES».** Fija la fecha de toda pista roja con ruta antes de proponerla.
- Siguen vigentes: rojo sin ruta fechada → una búsqueda antes de entregarlo · hora por titular ≠ hora por resumen · hora frente al cierre · agregado federal no fija día · sinónimos de municipio y colonia · REPUBLICACIONES = UNA FUENTE · ECO DE CONSULTA · RECUENTOS DE MEDIOS nunca se integran · cuerpos sin causa informada por autoridad, aparte · seguimientos procesales a «SEGUIMIENTOS» · `site:` con UN SOLO DOMINIO.
- Secciones obligatorias: **ENCARGOS, HECHOS DEL CORTE, CANDIDATOS -REC-, SEGUIMIENTOS, ARMAMENTO, SENTENCIAS, AJENOS, DESCARTADOS POR VENTANA, CORRECCIONES, INDICADOR DE COBERTURA**; URL completa de TODO resultado que respalde un dato.
- **Dominios confirmados (140-143)**: `comunicacion.fiscaliaveracruz.gob.mx`, `portal.fgeo.gob.mx`, `fiscaliageneralqro.gob.mx`, `seguridad.slp.gob.mx`, `fgebc.gob.mx`, `fiscalia.chihuahua.gob.mx`, `fiscalia.durango.gob.mx`, `fgjcdmx.gob.mx`, `fiscalia.puebla.gob.mx`, `ssp.michoacan.gob.mx`, `fiscaliaguerrero.gob.mx`, `ssp.chiapas.gob.mx`, `fge.yucatan.gob.mx`, `fgjtam.gob.mx`, `fiscaliazacatecas.gob.mx`, `fiscaliasinaloa.mx`, `fiscaliatabasco.gob.mx`, `tabasco.gob.mx` (SSP), `portal.fgeguanajuato.gob.mx`, `fiscalia-aguascalientes.gob.mx`, `fgeqroo.gob.mx`, `fiscalianl.gob.mx`, `fiscaliaslp.gob.mx`, `fiscaliamorelos.gob.mx`, `fgjem.edomex.gob.mx`, `fiscalia.jalisco.gob.mx`, `fge.chiapas.gob.mx`, `fgecolima.mx`, `comunicacion.fiscaliamichoacan.gob.mx`, `pgjebcs.gob.mx`, `www.veracruz.gob.mx/seguridad/`, `ssp.yucatan.gob.mx`, `ssc.qroo.gob.mx`; **nuevos en 143**: `fgjtlaxcala.gob.mx` (Tlax), `procuraduria.hidalgo.gob.mx` (Hgo, PGJEH), `fgenay.gob.mx` (Nay), `fiscalia.sonora.gob.mx` (Son); FGR en `fgr.org.mx` (listados; último indexado en 143: 753/26 del 26-oct). **Sin páginas en 143**: `fiscaliageneral.coahuila.gob.mx`, `fiscalia.coahuila.gob.mx` (prueba `fge.coahuila.gob.mx` o la SSP), `fgecampeche.gob.mx`, `fiscaliacampeche.gob.mx` (busca el dominio real sin `site:`), `ssp.oaxaca.gob.mx`, `pgjhidalgo.gob.mx`.
- Ciclo de 144: **B** (Noreste + Golfo encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
- **Prioridad sobre el ciclo** (cobertura de 143): **sentencias `NO REVISADA` (7)**: BCS · SLP, Zac · Col, Mich · Pue, Qro; **dominio sin páginas (2)**: Coah, Camp. **Armamento `NO REVISADA` (14)**: BC, BCS, Son, Dgo · SLP · Col · Edomex, Mor, Hgo, Qro · Gro, Camp, Yuc, QRoo; sin páginas: Coah, Oax. **Alto impacto con CONSULTA PROPIA obligatoria (10, solo amplia en 143)**: Dgo · Jal, Col, Nay (**dos ediciones seguidas**), Ags · Edomex, Mor, Hgo, Qro · Chis.
- **Boletín federal**: triple consulta para el 27-oct (sin indexar al cierre de 143), el 28 y cada día de la ventana (la hace el coordinador, y la repite al final de la ola).
