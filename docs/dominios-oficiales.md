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
| Gabinete de Seguridad (portal propio) | `gabinetedeseguridad.gob.mx/resultados/` | C | **Pasa a portal federal de consulta obligatoria a partir del 1-sep-2026**: el emisor anunció el 18-ago-2026 que los reportes diarios preliminares de homicidio y robo de vehículo migran a este sitio (ancla: `lasillarota.com/nacion/2026/8/18/…`). Si el barrido no lo incorpora, ARGOS reproducirá en septiembre el mismo falso vacío que costó cuatro ediciones |
| SSPC — informes | `seguridad.sspc.gob.mx` | C | Poco indexado |
| Guardia Nacional | `gob.mx/guardianacional/prensa` | B | **Fuente primaria del módulo de armamento**: publica desglose por entidad de armas largas/cortas, cargadores, cartuchos, granadas y explosivos que los medios omiten |
| SEDENA | `gob.mx/sedena` | B | Más zonas y regiones militares cuando publiquen |
| SEMAR | `gob.mx/semar` | B | Más regiones navales. Citada por medios con frecuencia sin que su comunicado se localice indexado |
| FGR | `gob.mx/fgr` | B | Fiscalías especializadas y delegaciones estatales |
| SESNSP | `gob.mx/sesnsp` | — | **Bloqueado y sin indexación útil.** Es la razón de que el indicador de homicidio doloso siga `HEREDADO — NO REVERIFICADO` |

---

## Estatales, por región

Marcados `✓` los verificados en el registro de fuentes de alguna edición.

### Noroeste

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Baja California | `SIN DOMINIO CANÓNICO REGISTRADO` | — | La FGE de BC se ha buscado sin fijar dominio. **Pendiente activo** (caso Tijuana) |
| Baja California Sur | `SIN DOMINIO CANÓNICO REGISTRADO` | — | |
| Chihuahua | `fiscalia.chihuahua.gob.mx` ✓ · `sspe.chihuahua.gob.mx` ✓ | B | **Variante sin punto** (`fiscaliachihuahua.gob.mx`) también citada: arbitrar antes de gastar búsquedas en la equivocada |
| Durango | `fiscalia.durango.gob.mx/AAAA/MM/DD/` ✓ | **A** | **El mejor portal de la serie.** Fecha en la ruta y término jurídico en el *slug*. Origen de `ARG-101-SEN-001` |
| Sinaloa | `sspsinaloa.gob.mx` ✓ · `sinaloa.gob.mx` ✓ | C | ⚠️ **Trampa de aniversario documentada**: los dos boletines indexados del portal son de **15-ago-2025** y 20-nov-2025. Un barrido de agosto los recoge como si fueran del corte |
| Sonora | `sonora.gob.mx` ✓ | C | Los agregados de la Mesa Estatal de Seguridad llegan por medios, no por portal |

### Noreste

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Coahuila | `SIN DOMINIO CANÓNICO REGISTRADO` | — | |
| Nuevo León | `SIN DOMINIO CANÓNICO REGISTRADO` | — | |
| San Luis Potosí | `fiscaliaslp.gob.mx` ✓ | C | Caso Matlapa abierto desde ARGOS 99 sin que ninguna URL fije fecha |
| Tamaulipas | `tamaulipas.gob.mx` ✓ | C | Región con **cero hechos en ventana** en ARGOS 101 pese a diez portales consultados |
| Zacatecas | `ssp.zacatecas.gob.mx` ✓ · `fiscaliazacatecas.gob.mx` ✓ | B | El boletín primario de la SSP **reaparece pero no consigna hora** (reserva de Sain Alto) |

### Occidente

| Entidad | Dominio | Clase | Nota |
|---|---|---|---|
| Aguascalientes | `SIN DOMINIO CANÓNICO REGISTRADO` | — | |
| Colima | `SIN DOMINIO CANÓNICO REGISTRADO` | — | Pendiente activo (`ARG-101-002`) |
| Guanajuato | `boletines.guanajuato.gob.mx/AAAA/MM/DD/` ✓ · `fge.guanajuato.gob.mx` ✓ · `enterate.leon.gob.mx` ✓ | **A** | Fecha en la ruta. ⚠️ Publica **agregados anuales** ("36 sentenciados en lo que va de 2026") que **no son del corte** y no son integrables sin desglose |
| Jalisco | `fiscalia.jalisco.gob.mx` ✓ · `fiscaliadejusticia.jalisco.gob.mx` ✓ | B | **Dos variantes citadas**: arbitrar |
| Michoacán | `fiscaliamichoacan.gob.mx` ✓ · `ssp.michoacan.gob.mx` ✓ · `michoacan.gob.mx` ✓ · `poderjudicialmichoacan.gob.mx` ✓ · `policiamorelia.gob.mx` ✓ | B | La entidad con más portales registrados y varias contradicciones abiertas (La Piedad, Zinapécuaro) |
| Nayarit | `SIN DOMINIO CANÓNICO REGISTRADO` | — | |

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
