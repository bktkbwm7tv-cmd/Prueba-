# Directorio de dominios oficiales — ARGOS

Versión 1.0 · Creado en **ARGOS 102** (corte 2026-08-19) · Pendiente abierto desde ARGOS 101.

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
| Gabinete de Seguridad (portal propio) | `gabinetedeseguridad.gob.mx/resultados/` | B | **Pasa a portal federal de consulta obligatoria a partir del 1-sep-2026**: el emisor anunció el 18-ago-2026 que los reportes diarios preliminares de homicidio y robo de vehículo migran a este sitio (ancla: `lasillarota.com/nacion/2026/8/18/…`). Si el barrido no lo incorpora, ARGOS reproducirá en septiembre el mismo falso vacío que costó cuatro ediciones |
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

| Entidad | Dominio | Clase | Nota |
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
| Aguascalientes | `SIN DOMINIO CANÓNICO REGISTRADO` | — | **Deuda no saldada en ARGOS 102.** Sus sentencias llegan solo por medios sin día en la URL (`clgnoticias.com/AAAA/MM/`) |
| Colima | **Sin portal web canónico.** Emisores verificados: `x.com/FiscaliaColima` ✓ y la **Mesa Estatal de Coordinación para la Construcción de la Paz y Seguridad** ✓ | **C** | **Registrados en ARGOS 102.** ⚠️ La fiscalía publica **sentencias condenatorias en su cuenta de X, sin fecha visible**. La Mesa Estatal llega por medios regionales (`afmedios.com`, sin fecha en URL). Es la primera fuente institucional de Colima registrada en la serie |
| Guanajuato | `boletines.guanajuato.gob.mx/AAAA/MM/DD/` ✓ · `fge.guanajuato.gob.mx` ✓ · `enterate.leon.gob.mx` ✓ | **A** | Fecha en la ruta. ⚠️ Publica **agregados anuales** ("36 sentenciados en lo que va de 2026") que **no son del corte** y no son integrables sin desglose |
| Jalisco | `fiscalia.jalisco.gob.mx` ✓ · `fiscaliadejusticia.jalisco.gob.mx` ✓ | B | **Dos variantes citadas, sin arbitrar tras dos ediciones**: ninguna devolvió resultado propio en ARGOS 102. Lo que se localiza de Jalisco llega por **FGR** y medios |
| Michoacán | `fiscaliamichoacan.gob.mx` ✓ · `ssp.michoacan.gob.mx` ✓ · `michoacan.gob.mx` ✓ · `poderjudicialmichoacan.gob.mx/…nota.aspx?id=<n>` ✓ · `policiamorelia.gob.mx` ✓ | B / C | La entidad con más portales registrados y la más productiva de la serie. ⚠️ **La FGE reproduce sus boletines en seis medios regionales pero su portal propio no se localiza indexado.** El Poder Judicial es **clase C** (`id` correlativo sin fecha) y publica **agregados semestrales** no integrables. Ancla fechada útil: `esferanoticias.mx/AAAA/MM/DD/` |
| Nayarit | `SIN DOMINIO CANÓNICO REGISTRADO` | — | **Deuda no saldada en ARGOS 102.** Se cubre por el boletín federal y por `ntv.com.mx/AAAA/MM/DD/`, medio regional **con fecha en ruta** — hoy la única vía fechable del estado |

### Centro

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Ciudad de México | `fgjcdmx.gob.mx` ✓ · `fiscaliageneral.cdmx.gob.mx` ✓ · `ssc.cdmx.gob.mx` ✓ | B | **Dos variantes de la fiscalía**: arbitrar |
| Estado de México | `fiscaliaedomex.gob.mx` ✓ · `fgjem.edomex.gob.mx` ✓ | B | **Dos variantes**: arbitrar. Ningún boletín localizado pese a varios hechos del Edomex publicados por medios |
| Hidalgo | `SIN DOMINIO CANÓNICO REGISTRADO` | — | |
| Morelos | `SIN DOMINIO CANÓNICO REGISTRADO` | — | Contradicción de Cuautla abierta desde ARGOS 99 sin boletín |
| Puebla | `fiscalia.puebla.gob.mx` ✓ | B | **Término jurídico en el *slug*** (`fallo-condenatorio`): es el respaldo del caso Coronango |
| Querétaro | `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` ✓ | **A** | Fecha en la ruta **y categoría propia `/sentencias/`**. El mejor portal de la región Centro |
| Tlaxcala | `fgjtlaxcala.gob.mx` ✓ | C | |

### Golfo

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Tabasco | `fiscaliatabasco.gob.mx/Boletin/Index/<id>` ✓ · `tabasco.gob.mx` ✓ | **C** | El patrón `/Boletin/Index/<id>` **funciona e indexa**, pero la numeración **no tiene correspondencia pública con fecha**. ⚠️ Existe un boletín de Cunduacán de **10 años por extorsión** (`/Boletin/Index/37454`) que **no es** el caso buscado en el mismo municipio |
| Veracruz | `comunicacion.fiscaliaveracruz.gob.mx/AAAA/MM/DD/` ✓ · `fiscaliaveracruz.gob.mx/AAAA/MM/DD/` ✓ · `veracruz.gob.mx` ✓ · `ssp.veracruz.gob.mx` ✓ · `pjeveracruz.gob.mx` ✓ | **A/C — disociado** | ⚠️ **Caso único de la serie: estructura de clase A, comportamiento de clase C.** ARGOS 102 comprobó que el portal **sí expone archivo fechado** `/AAAA/MM/DD/` y `/AAAA/MM/` (verificado en `/2026/02/20/`, `/2026/04/12/`, `/2026/05/08/`), pero **los boletines individuales llevan *slug* sin fecha, con caracteres unicode decorativos**, y **la rebanada de agosto-2026 no está en el índice del buscador**. La ruta fechada solo es explotable por **lectura directa**, que el bloqueo impide. Además publica **agregados acumulativos solapados** —22, 24, 32, 36, 37, 40, 44, 48, 51, 53, 69, 78 resoluciones en fechas distintas de 2026, **con cifras que se repiten en meses distintos**— y **encabeza sus agregados con penas de casos anteriores**. Ni la cifra del lote ni el número de condenatorias sirven como identificador único |

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

Cinco entidades aparecen con **dos dominios distintos** en el registro de fuentes, sin que ninguna
edición haya determinado cuál es el canónico: **Chihuahua**, **Jalisco**, **Ciudad de México**,
**Estado de México** y **Veracruz**. Gastar una búsqueda en la variante equivocada es un coste
recurrente y silencioso. Arbitrarlas es trabajo de una sola edición y beneficia a todas las demás.
