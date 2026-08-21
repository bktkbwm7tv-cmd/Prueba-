| Aguascalientes | `fiscalia-aguascalientes.gob.mx/noticia/<n>/<slug>` ✓ · X `@fiscaliaAGS` ✓ | **C** | **CLASIFICADO EN ARGOS 104**, cerrando la deuda que ARGOS 103 dejó a medias. El patrón es **ID correlativo + *slug* temático, sin fecha en la ruta** (`/noticia/5755/dictan-sentencia-condenatoria-por-homicidio`): **el término jurídico va en el *slug***, así que sirve para clasificar, pero **no para fechar**. Índice de listado: `/todas_las_noticias`. Sus sentencias siguen llegando por medios sin día en la URL (`clgnoticias.com/AAAA/MM/`) |# Directorio de dominios oficiales — ARGOS

Versión 1.2 · Creado en **ARGOS 102** (corte 2026-08-19) · Actualizado en **ARGOS 103**
(Jalisco arbitrado, Aguascalientes y Nayarit localizados, subdominio de Michoacán corregido,
`gabinetedeseguridad.gob.mx` reclasificado como bloqueado) · **Actualizado en ARGOS 104**
(corte 2026-08-21): **Colima sí tiene portal canónico y no está en `.gob.mx`**, Aguascalientes y
Nayarit **clasificados**, y `gabinetedeseguridad.gob.mx/contenido/<id>/` incorporado como emisor
de sentencias de la FGR.

Este archivo existe porque cada edición estaba redescubriendo, a fuerza de búsquedas, qué dominio
publica cada corporación y cuál de ellos es utilizable bajo el bloqueo de egreso. Ese
redescubrimiento consumía presupuesto de búsqueda sin producir inteligencia.

**Todos los dominios listados aquí proceden del registro de fuentes de alguna edición de ARGOS.**
Ninguno se ha inventado ni inferido. Una entidad sin dominio verificado se declara
`SIN DOMINIO CANÓNICO REGISTRADO`, nunca se rellena con una dirección plausible.

---

## Criterio de calidad: la estructura de la URL decide la utilidad

Bajo bloqueo de egreso no se puede leer ningún portal: solo se puede **buscar contra él con
`site:`** y leer lo que devuelva el índice. En esas condiciones, lo que determina si un portal sirve
no es lo que publica, sino **si su URL permite fechar un boletín sin abrirlo**.

| Clase | Estructura | Valor operativo |
|---|---|---|
| **A — Fechable** | La fecha está en la ruta (`/AAAA/MM/DD/`) | **Encabeza el triaje.** Un resultado de búsqueda basta para asignar el boletín a una ventana, sin leerlo |
| **B — Semifechable** | La ruta lleva año y mes, o el término jurídico va en el *slug* | Utilizable con reserva. El día lo tiene que aportar un ancla externa |
| **C — Opaco** | Identificador sin correspondencia pública con fecha (GUID, folio correlativo) | **Estructuralmente inservible bajo bloqueo.** Exige ancla externa fechada antes de asignar nada a una ventana |

El *slug* institucional es texto primario de la autoridad, no paráfrasis del resumidor del buscador:
por eso un término jurídico dentro del *slug* (`…fallo-condenatorio…`, `…sentencia-condenatoria…`)
sostiene una clasificación que el mismo término en un titular de medio no sostendría. Es el criterio
por el que ARGOS 101 integró la sentencia de Durango.

---

## Federales

| Emisor | Dominio | Clase | Nota de uso |
|---|---|---|---|
| SSPC / Gabinete de Seguridad | `gob.mx/sspc/prensa` | B | ⚠️ **Emisor de formato variable — la causa de dos falsos vacíos consecutivos.** Alterna **boletín diario** y **agregado de varios días** sin avisar: el del 14-15-16 ago es agregado, el del 17-ago volvió a ser diario. Una consulta por día suelto no alcanza un agregado, y una consulta por rango no alcanza un diario. **Hay que consultar siempre en ambas formas antes de declarar cualquier vacío.** El título lleva la fecha en el *slug* |
| Gabinete de Seguridad (portal propio) | `gabinetedeseguridad.gob.mx/resultados/` | **BLOQUEADO** | **Pasa a portal federal de consulta obligatoria a partir del 1-sep-2026**: el emisor anunció el 18-ago-2026 que los reportes diarios preliminares de homicidio y robo de vehículo migran a este sitio (ancla: `lasillarota.com/nacion/2026/8/18/…`). Si el barrido no lo incorpora, ARGOS reproducirá en septiembre el mismo falso vacío que costó cuatro ediciones. ⚠️ **ARGOS 103 lo sondeó por primera vez con `curl`: devuelve `CONNECT tunnel failed, response 403` igual que el resto de `*.gob.mx`.** **El portal al que migran los reportes diarios nace bloqueado**, así que incorporarlo al barrido no resuelve el pendiente: solo lo hará la lista blanca de egreso ⚠️ **Matiz de ARGOS 104**: aunque el sitio esté bloqueado al acceso directo, la ruta **`gabinetedeseguridad.gob.mx/contenido/<id>/` sí devuelve resultados indexados** y es **emisor de sentencias de la FGR** (localizada `/contenido/8526/`, delincuencia organizada). **Clase C** —`id` correlativo sin fecha—, pero utilizable por buscador: no es un dominio muerto, es un dominio ilegible por acceso directo |
| SSPC — informes | `seguridad.sspc.gob.mx` | C | Poco indexado |
| Guardia Nacional | `gob.mx/guardianacional/prensa` | **C** | ⚠️ **Reclasificado de B a C en ARGOS 102, y es el hallazgo estructural más incómodo del directorio.** Es la fuente primaria declarada del módulo de armamento —su *slug* es el titular y trae el desglose numérico y la entidad—, **pero la URL no lleva fecha en ninguna forma**, así que **ningún boletín suyo es asignable a una ventana sin ancla externa fechada**. Esa es la causa estructural de que la fuente primaria del módulo no rinda nunca en el corte del día |
| SEDENA | `gob.mx/sedena` | B | Más zonas y regiones militares cuando publiquen |
| SEMAR | `gob.mx/semar` | B | Más regiones navales. Citada por medios con frecuencia sin que su comunicado se localice indexado |
| FGR | `fgr.org.mx` ✓ (no `gob.mx/fgr`) | C | **Corregido en ARGOS 102**: el portal operativo es `fgr.org.mx`, con salas de prensa paginadas por *query string* y comunicados numerados (`DPE/NNNN/2026`) **sin fecha en la URL**. Dominios hermanos: `hasvistoa.`, `renadet.`, `inacipe.`, `historicopgr.` |
| SESNSP | `gob.mx/sesnsp` | — | **Bloqueado y sin indexación útil.** Es la razón de que el indicador de homicidio doloso siga `HEREDADO — NO REVERIFICADO` |

---

## Estatales, por región

Marcados `✓` los verificados en el registro de fuentes de alguna edición.

### Noroeste

| Colima | **`fgecolima.mx/boletines/<n>`** ✓ *(canónico)* · `col.gob.mx/Portal/detalle_noticia/<base64>` ✓ · `x.com/FiscaliaColima` ✓ · `x.com/gobiernocolima` ✓ · Mesa Estatal de Coordinación ✓ | **C** | ⚠️ **CORREGIDO EN ARGOS 104: Colima sí tiene portal canónico.** El directorio lo daba por inexistente durante tres ediciones porque **se buscaba bajo el patrón `.gob.mx`, y la fiscalía publica en `fgecolima.mx`**. Boletines con **ID correlativo sin fecha**; `site:` devuelve poco: **indexación pobre, no ausencia de portal**. El gobierno estatal usa **ID en Base64**, también sin fecha. La fiscalía sigue publicando **sentencias condenatorias sin fecha visible**, y la Mesa Estatal llega por medios regionales (`afmedios.com`, `portalcolima.com`, `colimadigital.com`) |
|---|---|---|---|
| Baja California | `fgebc.gob.mx/boletines/<NNNNN>-<slug>` ✓ | **C** | **Fijado en ARGOS 102.** Correlativo numérico opaco (14237 … 16641), **pero el término jurídico va en el *slug*** (`sentencia-condenatoria-de-21-anos…`): sirve al módulo judicial en cuanto exista ancla externa fechada. También `fgebc.gob.mx/publicaciones/<n>-<slug>` |
| Baja California Sur | `bcs.gob.mx` ✓ | C | **Fijado en ARGOS 102.** Publica la Mesa Estatal de Seguridad; *slug* sin fecha |
| Chihuahua | `fiscalia.chihuahua.gob.mx` ✓ · `sspe.chihuahua.gob.mx` ✓ · `municipiochihuahua.gob.mx/CCS/Prensa/` ✓ | **C** | **Variante arbitrada en ARGOS 102**: el canónico es **con punto**; `fiscaliachihuahua.gob.mx` se descarta. **Reclasificado de B a C**: sus comunicados son *slug* puro sin fecha alguna |
| Durango | `fiscalia.durango.gob.mx/AAAA/MM/DD/` ✓ | **A** | **El mejor portal de la serie.** Fecha en la ruta y término jurídico en el *slug*. Origen de `ARG-101-SEN-001` |
| Sinaloa | `sspsinaloa.gob.mx` ✓ · `sinaloa.gob.mx` ✓ | C | ⚠️ **Trampa de aniversario documentada**: los dos boletines indexados del portal son de **15-ago-2025** y 20-nov-2025. Un barrido de agosto los recoge como si fueran del corte |
| Sonora | `sonora.gob.mx` ✓ · emisor judicial: **FGJES** | C | Portal propio de la FGJES no localizado. **La vía fechable real de Sonora son sus medios regionales con fecha en ruta**: `elimparcial.com/son/…/AAAA/MM/DD/`, `eldiariodesonora.com.mx/…/AAAA/MM/DD/`, `telemax.com.mx/blog/AAAA/MM/DD/` |

### Noreste

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Coahuila | `sitio.fgecoahuila.gob.mx` ✓ (también `fgecoahuila.gob.mx`) | B | **Fijado en ARGOS 102.** WordPress con archivo anual `/2026/` |
| Nuevo León | `fiscalianl.gob.mx` ✓ | **C** | **Fijado en ARGOS 102.** ⚠️ **Portal de servicios sin sala de prensa indexable**: la fiscalía comunica por Facebook y X (`@FGJNL`). **Esto explica el cero crónico de Nuevo León** y no es un vacío del territorio. Variante `fiscalia-nl.gob.mx` **arbitrada: es un subsitio de capacitación, no la fiscalía** — no gastar búsquedas en ella |
| San Luis Potosí | `fiscaliaslp.gob.mx` ✓ | C | **Sí publica**: seis boletines de condena indexados, **ninguno fechable**. Caso Matlapa abierto desde ARGOS 99 sin que ninguna URL fije fecha |
| Tamaulipas | `fgjtam.gob.mx` ✓ | B | **Corregido en ARGOS 102.** El registro apuntaba a `tamaulipas.gob.mx`, el portal genérico del estado: **es la causa raíz probable de los "cero hechos" que la región arrastraba** |
| Zacatecas | `fiscaliazacatecas.gob.mx` ✓ · `ssp.zacatecas.gob.mx` ✓ | B | Publica **con el término jurídico en el *slug*** pero **sin fecha en la URL**. Ancla externa útil: `ljz.mx/DD/MM/AAAA/` (La Jornada Zacatecas) lleva **fecha en la ruta**. El boletín primario de la SSP no consigna hora (reserva de Sain Alto) |

### Occidente

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Aguascalientes | `fiscalia-aguascalientes.gob.mx` ✓ · X `@fiscaliaAGS` ✓ | **SIN CLASIFICAR** | **Dominio localizado en ARGOS 103**, tras dos ediciones como `SIN DOMINIO CANÓNICO REGISTRADO`. ⚠️ **Localizar no es clasificar**: no alcanzó el presupuesto para verificar si sus boletines llevan fecha en la ruta, así que **su clase sigue sin determinar** y la deuda solo está saldada a medias. Sus sentencias siguen llegando por medios sin día en la URL (`clgnoticias.com/AAAA/MM/`) |
| Colima | **Sin portal web canónico.** Emisores verificados: `x.com/FiscaliaColima` ✓ y la **Mesa Estatal de Coordinación para la Construcción de la Paz y Seguridad** ✓ | **C** | **Registrados en ARGOS 102.** ⚠️ La fiscalía publica **sentencias condenatorias en su cuenta de X, sin fecha visible**. La Mesa Estatal llega por medios regionales (`afmedios.com`, sin fecha en URL). Es la primera fuente institucional de Colima registrada en la serie |
| Nayarit | `fiscaliageneral.nayarit.gob.mx/web/?page=comunicacion&ttl=<n>` ✓ | **C — la peor estructura del directorio** | **CLASIFICADO EN ARGOS 104.** Es **querystring paginado, sin *slug* ni fecha**, y **los boletines individuales no tienen URL propia indexable**: no solo no se puede fechar, tampoco se puede citar un boletín concreto. **Nayarit solo es fechable por vía sustituta**: `ntv.com.mx/AAAA/MM/DD/` y `nayaritnoticias.com/AAAA/MM/DD/`, que **reproduce comunicados de la FGR en Nayarit** |
| Jalisco | `fiscalia.jalisco.gob.mx` ✓ | **A/B** | ⚠️ **VARIANTE ARBITRADA EN ARGOS 103, deuda de dos ediciones cerrada.** El canónico es `fiscalia.jalisco.gob.mx`: devuelve contenido propio indexado y sus *slugs* llevan **fecha completa como sufijo** (`comunicado-1055-20260605`, `boletin-1785-20240723`), de modo que **un resultado de búsqueda ya fecha el boletín sin ancla externa**. `fiscaliadejusticia.jalisco.gob.mx` **no devolvió un solo resultado propio en dos ediciones consecutivas** y se descarta — no gastar búsquedas en ella |
| Michoacán | **`comunicacion.fiscaliamichoacan.gob.mx`** ✓ *(objetivo correcto)* · `ssp.michoacan.gob.mx` ✓ · `michoacan.gob.mx` ✓ · `poderjudicialmichoacan.gob.mx/…nota.aspx?id=<n>` ✓ · `policiamorelia.gob.mx` ✓ | B / C | La entidad con más portales registrados y la más productiva de la serie. ⚠️ **Matiz de subdominio corregido en ARGOS 103**: el que realmente indexa es **`comunicacion.fiscaliamichoacan.gob.mx`**, no el dominio raíz, y **sus *slugs* llevan fecha completa** (`20250116-…`). El directorio apuntaba al sitio equivocado, lo que explica en parte que la FGE pareciera no indexar. La FGE reproduce además sus boletines en seis medios regionales. El Poder Judicial es **clase C** (`id` correlativo sin fecha) y publica **agregados semestrales** no integrables. Ancla fechada útil: `esferanoticias.mx/AAAA/MM/DD/` |
| Nayarit | `fiscaliageneral.nayarit.gob.mx` ✓ | **SIN CLASIFICAR** | **Dominio localizado en ARGOS 103**, tras dos ediciones como `SIN DOMINIO CANÓNICO REGISTRADO`. ⚠️ **Sin verificar si indexa boletines con fecha propia**: su clase sigue sin determinar. Vías fechables confirmadas: `ntv.com.mx/AAAA/MM/DD/` y `nayaritnoticias.com/AAAA/MM/DD/`, que **reproduce comunicados de la FGR en Nayarit** |

### Centro

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Ciudad de México | `fgjcdmx.gob.mx/comunicacion/nota/CS<AAAA>-<NNN>` ✓ · `ssc.cdmx.gob.mx` ✓ | **B** | **Variante arbitrada en ARGOS 102**: el canónico es `fgjcdmx.gob.mx`; `fiscaliageneral.cdmx.gob.mx` **no devolvió ningún contenido indexado** y se descarta. **Reclasificado de C a B**: el **año va en el folio del boletín** (`CS2026-066`), lo que separa años sin abrir el documento — no da el día |
| Estado de México | `fgjem.edomex.gob.mx/prensa` ✓ (boletines) · `fiscaliaedomex.gob.mx` ✓ (documentos y fichas) | C | **Arbitrado en ARGOS 102 con un matiz: no son variantes, son dos sitios vivos con funciones distintas.** Para boletines, el objetivo correcto es `fgjem.edomex.gob.mx/prensa`. Ambos siguen clase C: **el problema del Edomex no es la variante, es que ninguno indexa boletines fechados** |
| Hidalgo | `procuraduria.hidalgo.gob.mx` ✓ (PGJEH) | C | **Fijado en ARGOS 102.** Canal secundario verificado: X `@PGJE_Hidalgo` |
| Morelos | `fiscaliamorelos.gob.mx/prensa` ✓ | C | **Fijado en ARGOS 102.** Localizado, pero **no devolvió el boletín de Cuautla** pese a la búsqueda dirigida |
| Puebla | `fiscalia.puebla.gob.mx/Home/Comunicado/<GUID>` ✓ · `fiscalia.puebla.gob.mx/…/boletines/<n>-<slug>` ✓ | **C** | **Reclasificado de B a C en ARGOS 102.** Convive un patrón GUID opaco con otro de *slug* semántico, y **el caso bueno está en el opaco**. ⚠️ **Mantiene dos familias de titulación casi intercambiables** —sentencia impuesta ("Logra la FGE sentencia de más de 26 años…") y firmeza en alzada ("Logra la FGE que quede firme sentencia de 60 años", 50, 35, 23)—, todas con GUID sin fecha. **Es el vivero de confusiones que produjo el error de Coronango**: exigir siempre dos campos individualizadores |
| Querétaro | `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` ✓ | **A** | Fecha en la ruta **y categoría propia `/sentencias/`**. El mejor portal de la región Centro |
| Tlaxcala | `fgjtlaxcala.gob.mx` ✓ | C | **`NO REVISADA` en ARGOS 102** por agotamiento de presupuesto — única entidad del país en esa casilla este corte. ⚠️ La FGR-Tlaxcala publica una **serie de boletines casi idénticos** (`lineadecontraste.com/logra-fgr-sentencia/`, `-2`, `-3`, `-5`), ninguno con fecha en URL: exigir nombre + pena + municipio para no duplicar |

### Golfo

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Tabasco | `fiscaliatabasco.gob.mx/Boletin/Index/<id>` ✓ · `tabasco.gob.mx` ✓ | **C** | El patrón `/Boletin/Index/<id>` **funciona e indexa**, pero la numeración **no tiene correspondencia pública con fecha**. ⚠️ Existe un boletín de Cunduacán de **10 años por extorsión** (`/Boletin/Index/37454`) que **no es** el caso buscado en el mismo municipio **Reconfirmado por tercera edición en ARGOS 104**: los `id` devueltos (21846, 25573, 26672, 26794, 28015, 33793, 36312, 37273, 37335, 37454, 37481) **no correlacionan con fecha**. Se cierra como **clase C definitiva**: dejar de sondear el patrón, que ya consumió tres ediciones |
| Veracruz | **`veracruz.gob.mx/AAAA/MM/DD/<slug>/`** ✓ *(canónica)* · `veracruz.gob.mx/seguridad/<slug>/` ✓ *(misma nota, sin fecha)* · `comunicacion.fiscaliaveracruz.gob.mx/AAAA/MM/DD/` ✓ · `fiscaliaveracruz.gob.mx/AAAA/MM/DD/` ✓ · `pjeveracruz.gob.mx` ✓ | **A/C — disociado** | ⚠️ **VARIANTE ARBITRADA EN ARGOS 104, deuda de dos ediciones cerrada.** El **mismo comunicado se publica en dos rutas** y la **canónica para ARGOS es la fechada**: probado con el par idéntico `veracruz.gob.mx/2026/08/19/fuerzas-de-seguridad-detienen-a-21-personas…` = `veracruz.gob.mx/seguridad/fuerzas-de-seguridad-detienen-a-21-personas…`. **`ssp.veracruz.gob.mx` no es un dominio**: la SSP cuelga de `veracruz.gob.mx/seguridad/` — corregido aquí. Se mantiene el diagnóstico de la FGE: **estructura de clase A, comportamiento de clase C**. El archivo fechado `/AAAA/MM/DD/` funciona (verificado de nuevo en ARGOS 104 sobre `/2026/02/20/`, `/2026/05/08/`, `/2026/07/25/`), pero **agosto-2026 sigue sin indexar**: `/2026/08/20/` y `/2026/08/21/` consultados explícitamente, sin resultado. Publica además **agregados acumulativos solapados** —39 condenatorias del 12-18 ago es el último— **con cifras que se repiten en meses distintos** y **encabezados con penas de casos anteriores**: ni la cifra del lote ni el número de condenatorias identifican un caso |

### Sureste

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Campeche | `fgecam.campeche.gob.mx` ✓ · `ucs.campeche.gob.mx` ✓ | C | |
| Chiapas | `fge.chiapas.gob.mx/Prensa/Articulo/<GUID>` ✓ · `ssp.chiapas.gob.mx` ✓ | **C** | ⚠️ **El peor caso estructural**: GUID **sin fecha alguna**. Volvió un hecho de **abril de 2025** indistinguible de uno de hoy (señuelo de Suchiapa). Acervo de boletines con desglose útil **sin fechar** acumulándose sin contarse |
| Guerrero | `fiscaliaguerrero.gob.mx` ✓ | C | Publica **agregados semanales sin desglose nominal** |
| Oaxaca | `portal.fgeo.gob.mx` ✓ | C | ⚠️ Boletines numerados (`Boletín 1,261`) sin fecha en ruta: un boletín de **feb-2025** apareció en un barrido de agosto |
| Quintana Roo | `fgeqroo.gob.mx` ✓ | C | Caso de Playa del Carmen abierto desde ARGOS 99 sin que el boletín se localice |
| Yucatán | `fge.yucatan.gob.mx` ✓ | C | |

---

## Cómo se usa este archivo

1. **Antes de gastar búsquedas**, mirar la clase del portal. Un portal clase **A** se resuelve con
   una consulta `site:` y la fecha viene en la ruta; un portal clase **C** puede consumir cinco
   consultas y no fechar nada. En un presupuesto de 20 búsquedas por región, esa diferencia decide
   la cobertura.
2. **Encabezar el triaje con los portales A**: `fiscalia.durango.gob.mx`,
   `boletines.guanajuato.gob.mx`, `fiscaliageneralqro.gob.mx`.
3. **No cerrar un portal C en `SIN ACTUALIZACIÓN`**: la casilla correcta bajo bloqueo es
   `SIN RESULTADO INDEXADO EN VENTANA`, y si además el portal es opaco, la ficha necesita **ancla
   externa fechada** antes de asignarse a ninguna ventana.
4. **Cada edición que fije un dominio nuevo, o arbitre una variante, lo añade aquí.** Las entidades
   marcadas `SIN DOMINIO CANÓNICO REGISTRADO` son deuda de cobertura, no ausencia de emisor.

## Variantes pendientes de arbitrar

Queda **una** entidad con variantes sin arbitrar: **Estado de México**. **Chihuahua** y **Ciudad de
México** se arbitraron en ARGOS 102, **Jalisco** en ARGOS 103, y **Veracruz en ARGOS 104**. Gastar una
búsqueda en la variante equivocada es un coste recurrente y silencioso. Arbitrarlas es trabajo de una
sola edición y beneficia a todas las demás.

⚠️ **Aviso de ARGOS 104 sobre el Estado de México**: no es un problema de variante, y por eso lleva
dos ediciones sin resolverse. `fgjem.edomex.gob.mx` solo devuelve **PDF de 2019-2025** y
`fgjem.edomex.gob.mx/prensa` **no aparece indexado**. Arbitrar entre las dos direcciones no
produciría un dato mejor: **ninguna indexa boletines fechados**.
