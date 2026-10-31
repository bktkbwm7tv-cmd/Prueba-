# ARGOS 145 — Instrucciones comunes a los seis equipos (léelas íntegras antes de la primera búsqueda)

Repositorio: /home/user/Prueba- (lee CLAUDE.md si dudas de una regla).

## Ventana
- ABRE: **jueves 29-oct-2026 11:36 CDMX** (donde cerró ARGOS 144). CIERRA: **hora real de arranque de la sesión de ARGOS 145** (el coordinador la escribe aquí al copiar la plantilla: **sábado 31-oct-2026 11:14 CDMX** — hora del «Procede», 2 h 44 min después del Bloque 0 de las 08:30).
- Calendario: miércoles 28 · **jueves 29 · viernes 30 · sábado 31** · domingo 1-nov. Comprueba siempre el día de la semana que dice la fuente contra este calendario.
- **ARGOS 144 (ventana 28-oct 08:28 → 29-oct 11:36) ya publicó 20 hechos propios** —Magdalena de Kino (-001), Indaparapeo (-002), Acámbaro Santiaguillo (-003), Chenalhó (-004), Irapuato col. Azteca (-005), Ciudad del Maíz (-006), Ecatepec Rústica Xalostoc restos (-007) y detención (-019), Matamoros bloqueos (-008) y detención (-015), Acapulco Emiliano Zapata (-009), Tecolutla (-010), Cancún Cielo Nuevo (-011) y detención (-016), Cuautla Tecnológico (-012), Valle de Santiago Ranchos Unidos (-013), Chetumal Nachicocom (-014), General Bravo y China (-017), Lindavista (-018), Jaral del Progreso (-020)— y **cuatro recuperaciones**: CDMX Centro (REC-001), Coatzacoalcos (REC-002), Culiacán Villas del Real (REC-003), Mazatlán hielera (REC-004). Un hecho del 28 (tras 08:28) o del 29 antes de las 11:36 que 144 NO publicó es de la ventana de 144: candidato `-REC-` **solo si es de alto impacto (🔴)**; si es 🟡 o 🟢, va a «VISTOS».
- **Núcleo del corte**: hechos del **jueves 29 (tras las 11:36)** en adelante. Publicación del 29 sin hora fijada → `PUBLICADO EL DÍA DE APERTURA SIN HORA`; publicación del día de cierre sin hora → `FRONTERA DE VENTANA — HORA NO FIJADA`. ⚠️ **Si el único dato de día U HORA de una nota del 29 apunta a antes de las 11:36, el hecho es de la ventana de 144** (lecciones de Tabasco y de Irapuato).
- **Fin de semana**: «fin de semana violento», «N muertos de viernes a domingo» son **balances**: nunca se reparten ni se integran.
- Nunca infieras la hora. «Esta mañana» o «madrugada de este jueves» en un resumen NO fecha un hecho.
- Criterio de inclusión: entra con marca el hecho con **ruta fechada o titular con día**; el que solo tiene día por resumen se reporta igual, marcado, para que el coordinador decida.

## Red y herramientas
- Egreso bloqueado (curl gob.mx → 000). **NO uses WebFetch.** Solo WebSearch.
- **TODA búsqueda con mode:"extended".** Nunca "standard".
- Respeta tu tope de búsquedas; declara al final `Búsquedas utilizadas: n de N`. Si te sobran, invierte en hechos de alto impacto del miércoles 28 (tras las 08:28) y del jueves 29 antes de las 11:36 que ARGOS 144 no publicó (solo 🔴, candidatos `-REC-`) y del día de cierre.
- Pon la cifra de peso ENTRE COMILLAS en la consulta cuando busques una cifra concreta ("tres muertos", "21 años").

## Barrido obligatorio por equipo (además de los encargos)
1. Búsqueda por día de la semana: «este jueves» / «la noche del jueves» / «este viernes» / «madrugada de este viernes» / «este sábado» + entidades.
2. Fecha en la ruta, UNA POR DÍA de la ventana («2026/10/29», «2026/10/30», «2026/10/31»; la cuarta, a tu elección entre las tres): **4 BÚSQUEDAS RESERVADAS** para esto, que no se gastan en otra cosa; hazlas AL FINAL.
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
grep -il '<topónimo>' reports/argos-2026-10-25.html reports/argos-2026-10-26.html reports/argos-2026-10-27.html reports/argos-2026-10-28.html reports/argos-2026-10-29.html reports/indice-arg-id.md reports/argos-2026-10-29-fuentes.md reports/argos-2026-10-29-equipos.md
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
- **Dominios confirmados (140-144; en 144 se halló además `spsc.campeche.gob.mx`, SSP de Campeche)**: `comunicacion.fiscaliaveracruz.gob.mx`, `portal.fgeo.gob.mx`, `fiscaliageneralqro.gob.mx`, `seguridad.slp.gob.mx`, `fgebc.gob.mx`, `fiscalia.chihuahua.gob.mx`, `fiscalia.durango.gob.mx`, `fgjcdmx.gob.mx`, `fiscalia.puebla.gob.mx`, `ssp.michoacan.gob.mx`, `fiscaliaguerrero.gob.mx`, `ssp.chiapas.gob.mx`, `fge.yucatan.gob.mx`, `fgjtam.gob.mx`, `fiscaliazacatecas.gob.mx`, `fiscaliasinaloa.mx`, `fiscaliatabasco.gob.mx`, `tabasco.gob.mx` (SSP), `portal.fgeguanajuato.gob.mx`, `fiscalia-aguascalientes.gob.mx`, `fgeqroo.gob.mx`, `fiscalianl.gob.mx`, `fiscaliaslp.gob.mx`, `fiscaliamorelos.gob.mx`, `fgjem.edomex.gob.mx`, `fiscalia.jalisco.gob.mx`, `fge.chiapas.gob.mx`, `fgecolima.mx`, `comunicacion.fiscaliamichoacan.gob.mx`, `pgjebcs.gob.mx`, `www.veracruz.gob.mx/seguridad/`, `ssp.yucatan.gob.mx`, `ssc.qroo.gob.mx`; **nuevos en 143**: `fgjtlaxcala.gob.mx` (Tlax), `procuraduria.hidalgo.gob.mx` (Hgo, PGJEH), `fgenay.gob.mx` (Nay), `fiscalia.sonora.gob.mx` (Son); FGR en `fgr.org.mx` (listados; último indexado en 143: 753/26 del 26-oct). **Sin páginas en 143**: `fiscaliageneral.coahuila.gob.mx`, `fiscalia.coahuila.gob.mx` (prueba `fge.coahuila.gob.mx` o la SSP), `fgecampeche.gob.mx`, `fiscaliacampeche.gob.mx` (busca el dominio real sin `site:`), `ssp.oaxaca.gob.mx`, `pgjhidalgo.gob.mx`.
- Ciclo de 145: **C** (Occidente + Sureste encabezan el triaje judicial DESPUÉS de la prioridad sobre el ciclo).
- **Prioridad sobre el ciclo** (cobertura de 144): **sentencias `NO REVISADA` (14)**: Chih, Sin · Nay, Ags, Gto · CDMX, Edomex, Mor, Tlax · Chis, Oax, Gro, Yuc, QRoo; **sin dominio**: Son, Coah (sin páginas), Camp (no confirmado; SSP en `spsc.campeche.gob.mx`). **Armamento `NO REVISADA` (13)**: BCS, Chih, Sin, Dgo · NL, Zac · Jal, Nay, Ags · CDMX, Pue, Tlax · Camp; sin páginas: Son, Coah, Oax. **Alto impacto con CONSULTA PROPIA obligatoria (10, solo amplia en 144)**: BCS · NL, Zac, Coah · Hgo, Qro (**dos ediciones seguidas**) · Oax, Camp, Yuc, QRoo.
- **Boletín federal**: triple consulta para el 28-oct y el 29 (sin indexar al cierre de 144) y cada día de la ventana (la hace el coordinador, y la repite al final de la ola).
- ⚠️ **NUEVO (144)**: rotula la CIFRA DE ARMAS «por titular» o «SOLO POR RESUMEN» (tres eventos de 144 tenían la cifra solo en el resumen) · el titular que propones para una ficha solo lleva datos por titular, *slug* o ruta · en todo hecho rojo, una búsqueda por «instalaciones / base / sede» y por «bloqueos» en tu región.
