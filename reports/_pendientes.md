# ARGOS — Pendientes vivos

Archivo de traspaso entre ediciones. **Cada corte lo actualiza como último paso**, antes de commit.
Sirve para que una sesión nueva pueda arrancar sin que nadie tenga que recordar ni transcribir la
lista de seguimientos: basta leer este archivo y la edición anterior.

Convención: cada entrada indica desde qué edición está abierta, qué hay que buscar y qué la cierra.
Cuando algo se resuelve, se mueve a "Cerrados recientemente" con una línea, y se borra de ahí en la
segunda edición siguiente.

**Última actualización**: ARGOS 103 (corte 2026-08-20).

---

## PRIORIDAD 1 para ARGOS 104

La auditoría que ARGOS 102 ordenó y ARGOS 103 ejecutó **cerró su pregunta y abrió otra mayor**. El
fallo de cobertura **era sistemático**, y eso obliga a dos cosas que ninguna edición ha hecho aún.

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 103 | **¿Dónde empieza el fallo? Auditar hacia atrás las ventanas de ARGOS 95-98** | El barrido por tipo de hecho sobre las ventanas 99, 100 y 101 localizó **cuatro eventos 🔴 más** que ninguna edición registró, en **tres entidades y las tres ventanas**. **No hay ninguna razón para suponer que el fallo empezó en ARGOS 99**: el método defectuoso —barrer por entidad— es el mismo desde el principio de la serie. Mientras no se audite hacia atrás, **no se sabe cuántos rojos faltan en el archivo** | Un barrido dirigido **solo a hechos de alto impacto**, **por tipo de hecho y no por entidad**, sobre las ventanas de **ARGOS 95 a 98** (aprox. 11-15 de agosto). Mismo método que rindió en ARGOS 103: equipos temáticos (masacres y homicidios múltiples · violencia colectiva: motines, fosas, narcobloqueos, AEI) más una ronda de corroboración. **El bloque de ataques contra autoridades puede omitirse o reducirse**: ARGOS 103 demostró que ese tipo de hecho **sí se recoge** |
| ARGOS 103 | **Reconstruir en bloque las valoraciones de la serie 99-101** | La serie pasa de **3 eventos 🔴 registrados a 10**. Las valoraciones de **ARGOS 100 y 101 quedan confirmadas como falsas** y la de ARGOS 99, incompleta. **Ninguna edición ha reescrito esos cartelones**, así que el archivo sigue publicando `NO DETERMINABLE` donde hoy consta que había rojos | Decidir y ejecutar el **formato de la rectificación**: o una nota de fe de erratas insertada en cada cartelón afectado, o un cartelón de rectificación propio. **Cualquier serie temporal construida sobre esas valoraciones está viciada** mientras esto no se haga, y así consta en ARGOS 103 |
| ARGOS 102 | **Colima — entidad `NO REVISADA`, sustituye a Tlaxcala** | **Cero búsquedas dedicadas en ARGOS 103**, por agotamiento del presupuesto de Occidente antes de llegar a ella. Es la única entidad del país en esa casilla este corte. Colima **no tiene portal web canónico**: sus emisores verificados son `x.com/FiscaliaColima` y la Mesa Estatal de Coordinación | **Encabeza el triaje de ARGOS 104 por prioridad sobre el ciclo**, aunque no le toque por turno. En segundo orden: **Aguascalientes y Nayarit**, que en ARGOS 103 recibieron solo arbitraje de dominio, **sin barrido de boletines** |

## Seguimientos judiciales abiertos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 99 | **QRoo — Playa del Carmen**, 50 años (`ARG-103-SEG-001`) | **FECHADO POR PRIMERA VEZ tras cuatro ediciones**: `24horasqroo.mx/2026/08/12/50-anos-prision-4/`, fecha en la ruta, con los tres nombres coincidiendo —Rodman de Jesús Calderón Pineda, Juan José Velázquez Ramírez y Óscar Zacarías Chablé—. Corroborado por cinco medios más | ⚠️ **Consecuencia inesperada del hallazgo: la fecha (12-ago) lo saca de todas las ventanas cubiertas.** Ya no es candidato de ningún corte reciente. Sigue sin boletín de `fgeqroo.gob.mx` y **sin fuente oficial**, así que no integra. **Señuelo ya deslindado**: el caso de Benito Juárez, dos sentenciados, hecho de dic-2020 |
| ARGOS 99 | **Tabasco — Cunduacán**, Miguel "N" (`ARG-103-SEG-002`) | **DELITO CONFIRMADO POR PRIMERA VEZ: violación** — antes constaba sin especificar. Se mantienen **8 años**, reparación del daño y suspensión de derechos políticos. Ancla: `novedadesdetabasco.com.mx/2026/08/15/`, con fecha en ruta pero **medio regional** | El boletín institucional. **Confirmado que `/Boletin/Index/<id>` no correlaciona con fecha**. ⚠️ **Dos señuelos deslindados en ARGOS 103**: no es el boletín de extorsión de 10 años (`/Boletin/Index/37454`) ni el tercer caso de ~24-mar-2026 |
| ARGOS 102 | **Coronango, Puebla** — el boletín de firmeza | La sentencia quedó **integrada** como `ARG-102-SEN-REC-001`, pero con reserva: el título del boletín citado dice "sentencia", **no "firme" ni "condenatoria"** | El **segundo GUID**, de la familia de firmeza, más la **fecha de publicación** institucional y el **fragmento literal**. La multa de **212 UMA** sigue `SIN ANCLA DOCUMENTAL` y **no debe convertirse a pesos** |
| ARGOS 99 | **SLP — Matlapa**, Elías "N" | Pena de **2 años 8 meses**, procedimiento abreviado, más sanción económica y reparación de montos no publicados | El boletín de la FGE SLP. **Ninguna de las tres URLs lleva fecha** |
| ARGOS 92 | **Michoacán — Gabriela "N"**, Morelia | **Confirmado que no entra.** Fallo del 11-ago por secuestro agravado contra cinco personas, hechos de oct-2022. Todas las fuentes: "la pena se definirá en audiencia posterior" | La pena impuesta. **Señuelos descartados**: Jorge "N" (82 años, 12-ago — un medio publica 89, es error), Brenda Marisol G. (abr-2025) |
| ARGOS 101 | **Durango — Región Laguna** (`ARG-101-SEN-001`) | URL y fecha reconfirmadas en el portal institucional; **ARGOS 103 confirmó que sigue siendo el resultado más reciente** de `fiscalia.durango.gob.mx` | **Pena exacta, firmeza y corroboración independiente: no obtenidas.** Sigue en "más de 26 años", no sumable |
| ARGOS 102 | **Jalisco — Tizapán el Alto: 19 personas sentenciadas por la FGR** | 12 personas a **18 a 1 m 22 d** y 7 a **16 a 6 m**, por acopio de armas y asociación delictuosa, hechos de nov-2022. Publicación **10-11 ago** | Es el mayor renglón judicial de agosto (~332 años acumulables) y corresponde a la ventana de **ARGOS 95/96**. Falta comunicado de la FGR. ⚠️ **ARGOS 103 lo reencontró y no lo duplicó**: sigue fuera de ventana |
| ARGOS 102 | **Sonora — Nogales: 21 a 7 m 15 d a dos personas** | Trata de personas y corrupción de menores. Multa global **$506,696.19**, reparación material $20,100 y moral $18,239.76; lectura de sentencia 13-ago 17:10 h. **Cinco URLs con fecha en ruta** lo fijan el **12-ago** | **No aparece en ninguna edición.** Corresponde a la ventana de ARGOS 96 |
| ARGOS 102 | **Zacatecas — 100 años a seis personas por secuestro agravado** | **Segunda edición sin ancla externa.** Término **"fallo condenatorio" en el *slug* institucional**; seis sentenciados nominados (Oscar Iván, Oscar Alberto, Oscar, Agustín, Eduardo, Alondra); víctimas de Villa González Ortega; hecho de **ago-2021** | **La URL no lleva fecha y `ljz.mx` no devolvió nada** pese a búsqueda dirigida. `NO ASIGNABLE A NINGUNA VENTANA`. **Riesgo alto de trampa de aniversario.** **Deslinde**: no es el señuelo de Luis Moya y Calera |
| ARGOS 96 | **Ruffo Appel / Ingemar**, huachicol fiscal (`ARG-98-SEG-001`) | Sin avance en ARGOS 102 ni 103. Lo último publicado es una **suspensión provisional**, no la resolución de fondo | Sentencia de amparo de fondo, o el amparo de Guadalupe Hernández Hinojosa |
| ARGOS 101 | **Guerrero — 5 sentencias** y **Guanajuato — 36 sentenciadas** | Sin avance. Ambos son **agregados sin desglose nominal**; el de Guanajuato es además **anual**. ARGOS 103 reconfirmó el de Guanajuato en el boletín del 17-ago y **no lo integró** | El desglose caso por caso. Mientras no exista, ninguno es integrable |

## Vacíos de publicación que siguen sin resolverse

| Desde | Caso | Estado |
|---|---|---|
| ARGOS 102 | **Boletín federal — el vacío se amplía a tres días** | **18, 19 y 20 de agosto sin boletín indexado**, confirmado de forma independiente por los equipos de Golfo y Centro. ⚠️ **Se declara con reserva expresa**: este emisor ya produjo **dos falsos vacíos consecutivos** por alternar formato diario y agregado, y en ARGOS 103 **no se pudo aplicar la regla de la doble consulta** —por día suelto y por rango— por agotamiento de presupuesto. **Aplicarla es lo primero que debe hacer ARGOS 104** |
| ARGOS 102 | **`gabinetedeseguridad.gob.mx/resultados/` — obligatorio desde el 1-sep** | ⚠️ **ARGOS 103 lo sondeó por primera vez con `curl`: 403 al CONNECT, igual que el resto de `*.gob.mx`.** **El portal al que migran los reportes diarios de homicidio y robo de vehículo nace bloqueado**, así que incorporarlo al barrido **no resuelve el pendiente**: solo lo hará la lista blanca de egreso. Queda registrado en `docs/dominios-oficiales.md` como **BLOQUEADO** |
| ARGOS 102 | **Jiutepec, Morelos — ataque con dron y explosivos** | **Segunda edición en `PENDIENTE DE ANCLA FECHADA`.** La URL de `diariodemorelos.com` **no lleva fecha** y la hora "14:00 del 18-ago" procede **solo del resumidor**; si fuera exacta caería **23 minutos después** del cierre de la ventana 101. **Si se fechara dentro de cualquier ventana sería 🔴** por uso de drones armados. **Basta una URL fechada o un boletín de la FGE de Morelos** |
| ARGOS 102 | **Tijuana, col. Hipódromo** — cuatro cuerpos en cajuelas (`ARG-103-REC-002`) | **Gana fuente institucional** —declaración en video de la **Fiscal de BC**: "venían del mismo lugar los cuatro vehículos"—, pero **sigue `NO INTEGRABLE`**, y no por falta de fuente: los cuerpos aparecieron en **puntos distintos a lo largo de ~8 horas**. Determinar si es **una ejecución múltiple** o **el hallazgo en un día de víctimas de hechos distintos** exige un dato que nadie ha publicado. **Lo cerraría un boletín de `fgebc.gob.mx` que vincule los cuatro casos** |
| ARGOS 98 | **La Paz, BCS**, abuso sexual (11-ago) | **Quinta edición sin avance.** `Pendiente de corroboración independiente` |
| ARGOS 101 | **Zinapécuaro** (`ARG-101-003`) — saldo del enfrentamiento del 17-ago | **Ninguna autoridad publicó saldo.** **Tres hechos con la misma firma** en el mismo municipio (julio, abril y el del corte): atribuir el saldo sería la fusión que el control existe para impedir. Se mantiene 🟡 |
| ARGOS 102 | **Los Reyes, Michoacán** (`ARG-102-002`) — sin fuente institucional | Cinco abatidos y **ningún comunicado** de SEDENA, 21ª Zona Militar, SSP o FGE de Michoacán. ⚠️ **ARGOS 103 descubrió que su cifra de cinco muertos se está filtrando a otros hechos**: tres portales la atribuyeron a los narcobloqueos del 19-ago. **La ficha necesita fuente institucional también para impedir esa contaminación** |
| ARGOS 102 | **Alfajayucan, Hidalgo** (`ARG-102-005`) | `PENDIENTE DE ANCLA FECHADA`: **ninguna URL fija la fecha**. **No integra ningún total.** Basta una URL fechada |
| ARGOS 103 | **El operativo de Michoacán no tiene una línea escrita de fuente federal** | Un operativo con **12 detenidos, 9 armas largas, 8 AEI, calibre .50, Minimi y lanzagranadas**, y los **narcobloqueos** que desencadenó, **sin un solo comunicado** de SEDENA, GN o SSPC tres días después. Todo lo institucional del corte es **verbal**. `SIN RESULTADO INDEXADO EN VENTANA` en los tres portales |

## Contradicciones abiertas

| Desde | Caso | Detalle |
|---|---|---|
| ARGOS 103 | **Las 84 UMA de Tlaxcala** | ARGOS 102 las atribuyó a **Luis "N"** (Huamantla, portación de arma, 2 a 6 m). El barrido del Centro encuentra al resumidor atribuyéndolas a **"Marvin 'N'"**, sin multa para Luis. **No se arbitra, y la razón importa**: ambas lecturas dependen del **mismo resumidor**, que parafrasea, y ninguna URL de esa serie lleva fecha ni permite lectura directa. Arbitrar entre dos paráfrasis no produciría un dato mejor. `CONTRADICHA — REQUIERE LECTURA DIRECTA` |
| ARGOS 103 | **La cifra de bloqueos de Michoacán** (`ARG-103-001`) | **Cuatro lecturas publicadas sin fundir**: **24 puntos** (C5 a las 08:30), **"más de 20"**, **11**, **"al menos ocho carreteras"**. **Ninguna fuente institucional escrita fija un número**, y el listado de municipios también varía. `CONTRADICHA — reportar todas, no promediar` |
| ARGOS 103 | **Armamento especial vs. armas largas** (`ARG-103-ARM-001`) | Las fuentes publican **"9 armas largas"** y, por separado, **1 calibre .50, 4 Minimi y 2 lanzagranadas**, **sin precisar si están comprendidos en las nueve**. Sumarlos daría 16 y podría contar dos veces las mismas armas. `NO DETERMINABLE SI EL ARMAMENTO ESPECIAL ESTÁ COMPRENDIDO EN LAS NUEVE LARGAS` — se publican por separado |
| ARGOS 103 | **La reserva de color de `ARG-103-002`** | Tres portales regionales reportan **agresión armada contra la GN en Tanhuato**. **No se pudo determinar si ocurrió durante el cateo** —lo que haría 🟡 la ficha del operativo— **o si es parte de la reacción de bloqueos**, ya recogida en `ARG-103-001` (🔴). Se resolvió dejando la agresión en la ficha roja para que **no desaparezca del semáforo**. **Una fuente que la sitúe en el punto de la captura obliga a fe de erratas** |
| ARGOS 101 | **Mapimí, Durango** | Es **un solo evento**, pero el boletín federal da **65 cargadores** sin cuantificar cartuchos, frente a **87 cargadores y 4,715 cartuchos** de los medios. `CONTRADICHA — reportar ambas, no sumar` |
| ARGOS 101 | **Colima** (`ARG-101-002`) — detenidos | Los restos humanos quedaron confirmados y el evento reclasificó a 🔴. **Sigue sin arbitrar el otro extremo**: Infobae y Puente Libre no reportan detenidos, El Occidental reporta **1 mujer detenida**. El desglose numérico sigue **cualitativo** |
| ARGOS 100 | **Altamira, Tamaulipas** (`ARG-100-001`) | **Sin avance.** Siguen 2 detenidos frente a 3. El "comunicado de la Primera Zona Naval del 15-ago" **no existe localizable** |
| ARGOS 98 | **"Operación Sable", Mazatlán** (`ARG-97-ARM-003`) | Sin avance. La hipótesis de los dos subeventos sigue sin boletín. **La suma sería cálculo propio de ARGOS** |
| ARGOS 98 | **Privada Amberes, Ciudad Juárez** | Sin avance. Sin boletín de FGE Chihuahua ni SSPM |
| ARGOS 99 | **Culiacán** (`ARG-99-001`) | **Sin avance.** Hora y ubicación no conciliadas; sigue sin detenidos |
| ARGOS 99 | **Indicador SESNSP: −48% frente a −60%** | Sin cambio. `HEREDADO — NO REVERIFICADO`. No reverificable mientras `gob.mx/sesnsp` siga bloqueado. **Origen verificado**: entró en ARGOS 86 con respaldo citable real, así que **se conserva y no procede fe de erratas** |
| ARGOS 100 | **Azcapotzalco, CDMX** | Sin avance. El hecho es del 14-jun-2026 y **no se reabre** |
| ARGOS 101 | **Campeche — Hopelchén** | `POSIBLE DUPLICIDAD` con el boletín federal. **ARGOS 103 reconfirmó el hecho el 14-ago** y **no lo reintegró**. No integrar sin validación |
| ARGOS 102 | **Chiapas — Cintalapa: la ficha del archivo no es verificable** | Aparecen **cuatro** casos distintos bajo el mismo topónimo y **ninguno** tiene "1 cargador, 15 cartuchos, 4 detenidos". Puede ser una **fusión de dos casos**. **La ficha debe reescribirse o retirarse** |
| ARGOS 102 | **Chiapas — Benemérito de las Américas** | El desglose localizado (Selvin "N": 1 corta, 3 AK-47, 37 cargadores, 1 de disco con 59 cartuchos) **no coincide** con la ficha `ARM-003` de `_pendiente-barrido-ARGOS-88.md`. ⚠️ Los "37 cargadores de 30 cartuchos cada uno" son **capacidad declarada, no cartuchos contados**: nunca convertir a 1,110 |

## Deuda editorial y de método

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 98 | **Lista blanca de egreso** | `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**. Sonda de ARGOS 103 sobre **cuatro** hosts: 403 en los cuatro. **Cero portales leídos por acceso directo, decimocuarta edición.** Sigue siendo **el único cambio que elevaría el techo del producto**, y ahora hay **dos pruebas concretas de su coste**: el pendiente de Veracruz y el portal del Gabinete de Seguridad, que **nace bloqueado** justo antes de volverse obligatorio |
| ARGOS 102 | **Mergear las ramas de edición a `main`** | **Ninguna rama de ARGOS 88 a 103 está mergeada.** La causa raíz está identificada: las definiciones de `barrido-regional`, `procedencia-cifras` y `editor-duplicidad` llegan con el `git merge --ff-only` de arranque, es decir **después** de que la sesión tome su registro de agentes, y por eso no resuelven por nombre. **Solución aplicada en ARGOS 103 y que funciona**: lanzarlos como `general-purpose` indicándoles que **lean primero su archivo en `.claude/agents/`**. No degrada el resultado, pero **no es la corrección de fondo** |
| ARGOS 99 | **Presupuesto de búsqueda** | ARGOS 103 cerró con **184 de 200** y **10 de 11 topes respetados**: el equipo del Centro gastó **22 de 20** y **lo declaró él mismo**. Se rompe la racha de dos ediciones con los topes íntegros. ⚠️ **Dato nuevo a vigilar**: **cuatro de los once equipos —el 38 % del presupuesto— se dedicaron a auditar a ARGOS, no a cubrir el país**. Fue la decisión correcta, pero costó **Colima** y el módulo de sentencias |
| ARGOS 100 | **Correcciones de ARGOS 99 a ARGOS 98 que siguen sin aplicarse** | **Sexta edición sin ejecutarse.** Reintegrar Lázaro Cárdenas (`ARG-98-ARM-003`) al total de ARGOS 98; sustituir dos URL mal citadas en `argos-2026-08-15-fuentes.md`; incorporar tres hechos omitidos por ARGOS 98 (Chilpancingo/Los Ardillos 14-ago, Nopala Hidalgo 13-ago, excomandante por tortura en Cuautla); reintegrar el desglose de Sain Alto al total de ARGOS 99. **Se suman las nueve recuperaciones `ARG-102-REC-*` y los 27 AEI de Escuinapa de ARGOS 103** |
| ARGOS 102 | **Rotación de cobertura — a ARGOS 104 le toca el Ciclo A** | ARGOS 103 aplicó el **Ciclo C** (Occidente + Sureste) y lo declaró. **Rendimiento: ninguna de las dos regiones produjo sentencia integrable** —segunda edición consecutiva—, pero sí **el arbitraje de Jalisco**, **dos dominios localizados** y **el fechado de Playa del Carmen**. **A ARGOS 104 le toca el Ciclo A: Noroeste + Centro encabezan el triaje judicial.** ⚠️ **Prioridad sobre el ciclo: Colima encabeza**, aunque sea de Occidente |
| ARGOS 102 | **Directorio de dominios — cuatro ganancias, dos deudas a medias** | `docs/dominios-oficiales.md` actualizado a **v1.1** en ARGOS 103: **Jalisco arbitrado** (`fiscalia.jalisco.gob.mx`, con fecha completa en el *slug*, sube a casi-A), **Aguascalientes y Nayarit localizados** pero **SIN CLASIFICAR** —localizar no es clasificar—, **subdominio de Michoacán corregido** a `comunicacion.fiscaliamichoacan.gob.mx`, y **`gabinetedeseguridad.gob.mx` reclasificado como BLOQUEADO**. **Variantes que siguen sin arbitrar: Estado de México y Veracruz** |
| ARGOS 103 | **Un *liveblog* es fuente de clase propia — REGLA YA ESCRITA** | En una sola edición produjo **dos errores distintos**: un falso hallazgo de omisión —un hecho del 14-ago traído como nuevo desde una página del 15— y estuvo a punto de introducir **cinco muertos ajenos** en el hecho principal del corte. *Cerrado como deuda de documentación*: la regla **quedó escrita en `CLAUDE.md`** ("El *liveblog* fecha la página, no el hecho"), junto con el corolario de **comprobar la coherencia interna de la fuente**, que no cuesta ninguna búsqueda. **Queda por ver si los equipos la aplican**: verificarlo es trabajo de ARGOS 104 |

## Cerrados recientemente

- **La auditoría de cobertura hacia atrás (ventanas 99-101)** — **CERRADA CON VEREDICTO: SISTEMÁTICO**
  (`ARG-103-FE-001/002/003`, `ARG-103-AUD-001` a `-004`). Cuatro eventos 🔴 más, en tres entidades y
  las tres ventanas, **todos publicados con fecha en la URL** y **ninguno presente en el archivo**,
  verificado con `grep` por el coordinador. La serie 99-101 pasa de **3 rojos a 10**. *Cerrada la
  pregunta de ARGOS 102; se abren en su lugar las dos PRIORIDAD 1 de arriba.*

- **Los 27 AEI de la segunda línea de Sinaloa** — **CONTRADICCIÓN RESUELTA** (`ARG-103-REC-001`).
  No eran dos lecturas del mismo renglón: el boletín federal del 17-ago tiene **dos entradas de
  Sinaloa en municipios distintos** — **Ahome** y **La Campana, Escuinapa** (1 arma larga, 13
  cargadores, 1,389 cartuchos, **27 AEI**). **Escuinapa es geográficamente incompatible con Ahome.**
  ⚠️ El boletín **no se leyó íntegro**: el cierre se apoya en triangulación entre dos medios, y
  ninguna URL lleva fecha. Confianza **Medio**. *Cerrado; su reintegración a los totales del periodo
  pasa a deuda editorial.*

- **Tlaxcala — deuda de cobertura SALDADA.** Encabezó el triaje del Centro por la regla de prioridad
  sobre el ciclo, pese a no tocarle por turno, y cierra en `SIN RESULTADO INDEXADO EN VENTANA` —
  **una casilla escrita, no un silencio**. *Cerrado; su lugar como entidad `NO REVISADA` lo ocupa
  ahora **Colima**.*

- **Jalisco — variante arbitrada** tras dos ediciones. `fiscalia.jalisco.gob.mx` es el canónico y su
  *slug* lleva **fecha completa**; `fiscaliadejusticia.jalisco.gob.mx` no devolvió un solo resultado
  propio en dos ediciones. *Cerrado; quedan Estado de México y Veracruz.*

- **Veracruz — las condenatorias del lote del 13-ago** — **CERRADO COMO NO REINTENTABLE.**
  `BLOQUEADO POR EGRESO`: el portal **sí expone archivo fechado** `/AAAA/MM/DD/`, pero agosto-2026
  **no está indexado** y solo se resolvería por lectura directa. **ARGOS 103 no gastó ninguna
  búsqueda en él**, conforme a la instrucción. *Cerrado como deuda de búsqueda; reabrir solo si
  cambia la política de red.*

- **La causa raíz del fallo de agentes** — **CERRADA CON SOLUCIÓN PRÁCTICA VERIFICADA.** Lanzarlos
  como `general-purpose` indicándoles que lean su archivo en `.claude/agents/` funciona y no degrada
  el resultado. *Cerrado el diagnóstico y el rodeo; la corrección de fondo —mergear a `main`— sigue
  en deuda editorial.*

- **Los pendientes cerrados en ARGOS 102** —desglose del boletín federal del 14-16 ago, el falso
  vacío del 17-ago, Coronango, Tijuana `ARG-101-008`, Colima `ARG-101-002`, La Piedad `ARG-98-002`,
  el acervo sin fechar de Chiapas, Suchiapa y Cuautla— *se retiran de esta lista conforme a la
  convención de dos ediciones.*

---

## Cómo arrancar la edición siguiente

Sesión nueva, un solo mensaje:

> Haz el ARGOS 104 de hoy siguiendo `CLAUDE.md`. Rama `claude/argos-104-<sufijo>`. Lee
> `reports/_pendientes.md`, `docs/dominios-oficiales.md` y la edición anterior
> (`reports/argos-2026-08-20*`) para no duplicar hechos ni perder seguimientos. Verifica antes si la
> rama de ARGOS 103 (`claude/argos-103-audit-9tuqp9`) ya se mergeó a `main`; si no, trae sus cambios
> primero con `git merge --ff-only`.
>
> La PRIORIDAD 1 es **continuar la auditoría hacia atrás, sobre las ventanas de ARGOS 95 a 98**,
> con el mismo método que rindió en ARGOS 103: **consultar por tipo de hecho y no por entidad**,
> primero y en solitario. ARGOS 103 demostró que el fallo de cobertura era **sistemático**, no
> puntual, y no hay razón para suponer que empezó en ARGOS 99.
>
> Aplica el **Ciclo A** (Noroeste + Centro encabezan el triaje judicial), con **Colima encabezando
> por prioridad sobre el ciclo**: quedó `NO REVISADA`.
>
> Antes del commit, ejecuta los tres controles obligatorios (`barrido-regional` ×6,
> `procedencia-cifras` y `editor-duplicidad`) y actualiza `reports/_pendientes.md`.
>
> Dos cosas que te ahorran tiempo: **los agentes de control no resuelven por nombre** —lánzalos como
> `general-purpose` diciéndoles que lean primero su archivo en `.claude/agents/`; funciona—. Y **no
> gastes búsquedas en el pendiente de Veracruz**: está `BLOQUEADO POR EGRESO` y seis ediciones lo han
> intentado.

### Lo que funcionó en ARGOS 103 y conviene repetir

1. **Invertir el eje del barrido.** Consultar **por tipo de hecho y no por entidad** produjo cuatro
   eventos rojos que tres ediciones no vieron, con 36 búsquedas. Es el hallazgo de método más
   rentable de la serie y **debe volverse fase permanente**, no auditoría extraordinaria.
2. **Ejecutar la verificación prioritaria primero y en solitario**, tercera edición consecutiva que
   lo confirma. Y **darle una segunda ronda de corroboración**: fue la que corrigió la ventana de dos
   de los cuatro hallazgos, al distinguir fecha del hecho de fecha de publicación.
3. **Verificar personalmente las acusaciones graves contra el archivo, con `grep`.** De seis
   candidatos a omisión, **dos eran falsos** y ya estaban publicados. Sin esa comprobación, ARGOS 103
   habría acusado a ARGOS 98 de dos omisiones inexistentes.
4. **Comprobar la coherencia interna de las fuentes cuesta cero búsquedas y salva cifras.**
   Verificar que "martes" correspondiera al 18 de agosto impidió atribuir cinco muertes al evento
   equivocado; verificar "sábado 15" y "domingo 16" confirmó que las fechas de la auditoría no venían
   del resumidor.
5. **Dar a cada equipo los señuelos ya descartados en su encargo**, cuarta edición que lo confirma.
   Ninguno reintrodujo un señuelo cerrado.
6. **Publicar las cifras contradictorias sin fundirlas.** Cuatro cifras de bloqueos y un armamento
   especial que no se suma a las armas largas. **Un total limpio que oculta una duda es peor producto
   que un total con reserva.**
7. **Corregir el generador, no su salida.** Su validación de desborde volvió a atrapar una URL de 75+
   caracteres antes de publicar, y la paridad escritorio/móvil cerró en **16 de 16 ARG-ID**.
8. **El archivo del repositorio manda sobre cualquier descripción de la norma.** `editor-duplicidad`
   detectó que el borrador había reintroducido en la página 2 los bloques "ARGOS ALERTA" y "eventos
   prioritarios", que `CLAUDE.md` **retiró expresamente** y que ninguna de las tres ediciones
   anteriores trae. La regresión se produjo porque el coordinador siguió una descripción
   **desactualizada** de la estructura en vez de leer la del repositorio. **Es el mismo principio que
   ARGOS predica para las fuentes, aplicado a su propia norma.**
9. **Un equipo que no encuentra nada puede estar aportando el diagnóstico.** El cero del bloque de
   ataques contra autoridades acotó el fallo: **lo que ARGOS pierde es la violencia contra civiles
   anónimos**, no la ejercida contra el Estado.
