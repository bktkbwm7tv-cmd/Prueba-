# ARGOS — Pendientes vivos

Archivo de traspaso entre ediciones. **Cada corte lo actualiza como último paso**, antes de commit.
Sirve para que una sesión nueva pueda arrancar sin que nadie tenga que recordar ni transcribir la
lista de seguimientos: basta leer este archivo y la edición anterior.

Convención: cada entrada indica desde qué edición está abierta, qué hay que buscar y qué la cierra.
Cuando algo se resuelve, se mueve a "Cerrados recientemente" con una línea, y se borra de ahí en la
segunda edición siguiente.

**Última actualización**: ARGOS 102 (corte 2026-08-19).

---

## PRIORIDAD 1 para ARGOS 103

Las tres de ARGOS 102 se resolvieron o cambiaron de naturaleza (ver "Cerrados"). Las de hoy nacen de
lo que este corte descubrió sobre sí mismo: **ARGOS encontró sus dos eventos rojos mejor
documentados en las ventanas de ediciones anteriores, que los habían declarado vacías.**

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 102 | **Auditoría de cobertura hacia atrás: ¿cuántos eventos rojos más se perdieron?** | Este corte localizó **dos eventos 🔴 no registrados** —la masacre de Tlapa de Comonfort (ventana de ARGOS 101) y el motín de Cárdenas, Tabasco (ventana de ARGOS 100)— y **ambos estaban publicados con fecha en la URL en medios nacionales**. No fue falta de fuentes: fue el barrido. Las tres ediciones que declararon `NO DETERMINABLE` por ausencia de rojos (100, 101, 102) **descansan sobre esa cobertura** | Un barrido dirigido **solo a hechos de alto impacto** sobre las ventanas de ARGOS 99, 100 y 101, consultando por tipo de hecho (masacre, familia, incendio de vivienda, ataque a autoridades, motín) y **no por entidad**. Es la prueba de si el fallo fue puntual o sistemático. **Si aparecen más, las valoraciones de esa serie deben rectificarse en bloque** |
| ARGOS 102 | **Los 27 AEI de la segunda línea de Sinaloa del boletín federal del 17-ago** | **Contradicción declarada y no arbitrada.** Dos equipos leyeron el mismo boletín: uno devolvió **Ahome con 8 cortas, 9 largas, 8 cargadores y 2 detenidos**; otro, una línea de **1 arma larga, 13 cargadores, 1,389 cartuchos y 27 AEI**. Lo más probable es que el boletín tenga **dos entradas de Sinaloa**, pero **ninguna edición ha leído el documento íntegro** | Leer el boletín, o una reproducción íntegra que permita contar sus entradas. Si se confirma, **añade 27 AEI** al periodo y eleva el total recuperado de artefactos por encima de 345 |
| ARGOS 97 | **Las condenatorias de Veracruz del lote del 13-ago — ahora son 10, no 9** | **Sexta edición sin desglose, pero el pendiente cambió de naturaleza**: deja de ser deuda de búsqueda. `comunicacion.fiscaliaveracruz.gob.mx` **sí expone archivo fechado** `/AAAA/MM/DD/` (verificado en `/2026/02/20/`, `/2026/04/12/`, `/2026/05/08/`), pero **agosto-2026 no está indexado** y los boletines llevan *slug* unicode sin fecha | **`BLOQUEADO POR EGRESO — NO REINTENTABLE POR BÚSQUEDA`.** La ruta fechada solo es explotable por lectura directa. **No gastar más búsquedas hasta que cambie la política de red.** El ángulo institucional está agotado y así consta |

## Seguimientos judiciales abiertos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 102 | **Coronango, Puebla** — el boletín de firmeza | La sentencia quedó **integrada** como `ARG-102-SEN-REC-001` (recuperación de ARGOS 95), pero con reserva: el título del boletín citado dice "sentencia", **no "firme" ni "condenatoria"**. La FGE de Puebla mantiene **dos familias de titulación** —sentencia impuesta y firmeza en alzada— y este boletín es de la primera | El **segundo GUID**, de la familia de firmeza. Falta también la **fecha de publicación del boletín institucional** (hoy la fija un medio) y el **fragmento literal** del cuerpo. La multa de **212 UMA** sigue `SIN ANCLA DOCUMENTAL` y **no debe convertirse a pesos** |
| ARGOS 99 | **QRoo — Playa del Carmen**, 50 años | **DESGLOSE NOMINAL COMPLETO por primera vez**: Rodman de Jesús Calderón Pineda, Juan José Velázquez Ramírez y Óscar Zacarías Chablé; homicidio calificado de dos hombres; hecho del **12-oct-2020** en la Quinta Avenida; multa de **260,640 pesos por sentenciado** reconfirmada | El boletín de `fgeqroo.gob.mx`, que sigue sin localizarse tras cuatro ediciones. ⚠️ El único URL de ese dominio que devuelve la búsqueda es el **señuelo ya deslindado** de Benito Juárez (dos sentenciados, hecho de dic-2020) |
| ARGOS 99 | **SLP — Matlapa**, Elías "N" | **Pena fijada por primera vez: 2 años 8 meses**, procedimiento abreviado con aceptación de responsabilidad, más sanción económica y reparación del daño de montos no publicados | El boletín de la FGE SLP. **Ninguna de las tres URLs lleva fecha**; el indicio disponible lo situaría fuera de la ventana de 102 |
| ARGOS 99 | **Tabasco — Cunduacán**, Miguel "N" | **Dos corroboraciones nuevas** y accesorias identificadas: **8 años** + reparación del daño + suspensión de derechos políticos. Ámbito del boletín acotado a Centro, Cárdenas y Cunduacán (6 vinculaciones + 1 sentencia = 7 personas) | El boletín. **Confirmado que `/Boletin/Index/<id>` no correlaciona con fecha** (N°4864→37335 pero N°4894→37481). ⚠️ Aparece un **tercer** caso de Cunduacán, ~24-mar-2026 |
| ARGOS 92 | **Michoacán — Gabriela "N"**, Morelia | **Confirmado que no entra.** Fallo del 11-ago por secuestro agravado y privación ilegal **contra cinco personas**, hechos de oct-2022; **tres víctimas fueron después asesinadas**. Todas las fuentes: "la pena se definirá en audiencia posterior" | La pena impuesta. **Señuelos ya descartados**: Jorge "N" (82 años, 12-ago — un medio publica **89**, es error), Brenda Marisol G. (abr-2025) |
| ARGOS 101 | **Durango — Región Laguna** (`ARG-101-SEN-001`) | URL y fecha **reconfirmadas** en el portal institucional | **Pena exacta, firmeza y corroboración independiente: no obtenidas.** Sigue en "más de 26 años", no sumable |
| ARGOS 102 | **Jalisco — Tizapán el Alto: 19 personas sentenciadas por la FGR** | **Ninguna edición lo registró.** 12 personas a **18 a 1 m 22 d** y 7 a **16 a 6 m**, por acopio de armas y asociación delictuosa, hechos de nov-2022; reclusión en Puente Grande. Publicación **10-11 ago** (cuatro anclas con fecha en ruta) | Es el mayor renglón judicial de agosto (~332 años acumulables) y corresponde a la **ventana de ARGOS 95/96**. Falta comunicado de la FGR para integrarlo |
| ARGOS 102 | **Sonora — Nogales: 21 a 7 m 15 d a dos personas** | Trata de personas y corrupción de menores. Desglose completo disponible, multa global **$506,696.19**, reparación material $20,100 y moral $18,239.76; lectura de sentencia 13-ago 17:10 h. **Cinco URLs con fecha en ruta** lo fijan el **12-ago** | **No aparece en ninguna edición.** Es el expediente judicial mejor documentado del periodo. Corresponde a la ventana de ARGOS 96 |
| ARGOS 102 | **Zacatecas — 100 años a seis personas por secuestro agravado** | Término **"fallo condenatorio" en el *slug* institucional** de `fiscaliazacatecas.gob.mx`; seis sentenciados nominados; hecho de **ago-2021**; sin liberación anticipada, más multa y reparación | **La URL no lleva fecha y ningún medio la fecha.** `NO ASIGNABLE A NINGUNA VENTANA`. Riesgo alto de trampa de aniversario. **Deslinde**: no es el señuelo de Luis Moya y Calera |
| ARGOS 96 | **Ruffo Appel / Ingemar**, huachicol fiscal (`ARG-98-SEG-001`) | Sin avance en ARGOS 102. Lo último publicado es una **suspensión provisional**, no la resolución de fondo | Sentencia de amparo de fondo, o el amparo de Guadalupe Hernández Hinojosa |
| ARGOS 101 | **Guerrero — 5 sentencias** y **Guanajuato — 36 sentenciadas** | Sin avance. Ambos son **agregados sin desglose nominal**; el de Guanajuato es además **anual**, no del corte | El desglose caso por caso. Mientras no exista, ninguno es integrable |

## Vacíos de publicación que siguen sin resolverse

| Desde | Caso | Estado |
|---|---|---|
| ARGOS 102 | **Boletín federal del 18-ago** | **El vacío se reduce a un solo día por segunda vez.** El del 17-ago existe y está indexado (ver "Cerrados"); del **18-ago no hay boletín en ninguna de sus dos formas** —se consultó por día suelto y por rango—. `SIN RESULTADO INDEXADO EN VENTANA` |
| ARGOS 102 | **`gabinetedeseguridad.gob.mx/resultados/` — obligatorio desde el 1-sep** | El emisor anunció el **18-ago** que los reportes diarios preliminares de homicidio y robo de vehículo **migran a ese sitio a partir del 1 de septiembre**. **Si el barrido federal no lo incorpora, ARGOS reproducirá en septiembre el mismo falso vacío que ya ha costado dos correcciones** |
| ARGOS 98 | **La Paz, BCS**, abuso sexual (11-ago) | **Cuarta edición sin avance.** `Pendiente de corroboración independiente` |
| ARGOS 101 | **Zinapécuaro** (`ARG-101-003`) — saldo del enfrentamiento del 17-ago | **Ninguna autoridad publicó saldo.** Aparecen dos notas regionales con "1 muerto, 1 herido, bloqueos", pero **ninguna lleva fecha** y existe un hecho de **julio-2026 en el mismo municipio con saldo casi idéntico**, más un tercero de abril. **Tres hechos con la misma firma**: atribuir el saldo sería la fusión que el control existe para impedir. Se mantiene 🟡 |
| ARGOS 102 | **Los Reyes, Michoacán** (`ARG-102-002`) — sin fuente institucional | Cinco abatidos y **ningún comunicado** de SEDENA, 21ª Zona Militar, SSP o FGE de Michoacán. Es el hecho más grave de la ventana y el peor documentado. **Segundo ataque a patrullaje militar en Michoacán en cinco días** tras La Piedad |
| ARGOS 102 | **Alfajayucan, Hidalgo** (`ARG-102-005`) | `PENDIENTE DE ANCLA FECHADA`: **ninguna URL fija la fecha** y el 18-ago solo lo afirma el resumidor. **No integra ningún total.** Basta una URL fechada para cerrarlo |

## Contradicciones abiertas

| Desde | Caso | Detalle |
|---|---|---|
| ARGOS 102 | **Inventario federal del 17-ago — Sinaloa** | Ver PRIORIDAD 1. Dos lecturas del mismo boletín, **no se suman ni se funden** |
| ARGOS 101 | **Mapimí, Durango** | **Resuelta la duplicidad, abierta la discrepancia.** Es **un solo evento** —coinciden detenidos, armas y autoridad receptora—, pero el boletín federal da **65 cargadores** y no cuantifica cartuchos, frente a **87 cargadores y 4,715 cartuchos** de los medios. `CONTRADICHA — reportar ambas, no sumar` |
| ARGOS 101 | **Colima** (`ARG-101-002`) — detenidos | **Los restos humanos quedaron CONFIRMADOS** y el evento reclasificó a 🔴 (ver "Cerrados"). **Sigue sin arbitrar el otro extremo**: Infobae y Puente Libre no reportan detenidos, El Occidental reporta **1 mujer detenida**. Y el desglose numérico sigue **cualitativo**: granadas, armas y cargadores sin cantidad |
| ARGOS 100 | **Altamira, Tamaulipas** (`ARG-100-001`) | **Sin avance.** Siguen 2 detenidos frente a 3, y el inventario vehicular sin consolidar. El "comunicado de la Primera Zona Naval del 15-ago" **no existe localizable** |
| ARGOS 98 | **"Operación Sable", Mazatlán** (`ARG-97-ARM-003`) | Sin avance. La hipótesis de los dos subeventos sigue sin boletín que la sostenga. **La suma sería cálculo propio de ARGOS** |
| ARGOS 98 | **Privada Amberes, Ciudad Juárez** | Sin avance. Sin boletín de FGE Chihuahua ni SSPM |
| ARGOS 99 | **Culiacán** (`ARG-99-001`) | **Sin avance.** Hora y ubicación no conciliadas; sigue sin detenidos |
| ARGOS 99 | **Indicador SESNSP: −48% frente a −60%** | Sin cambio. `HEREDADO — NO REVERIFICADO`. No es reverificable mientras `gob.mx/sesnsp` siga bloqueado. **Origen verificado**: entró en ARGOS 86 con respaldo citable real, así que **se conserva y no procede fe de erratas** |
| ARGOS 100 | **Azcapotzalco, CDMX** | Sin avance. El hecho es del 14-jun-2026 y **no se reabre** |
| ARGOS 101 | **Campeche — Hopelchén** | `POSIBLE DUPLICIDAD` con el boletín federal del 14-16 ago. Confirmado hecho del **14-ago**. **No integrar sin validación** |
| ARGOS 102 | **Chiapas — Cintalapa: la ficha del archivo no es verificable** | Aparecen **cuatro** casos distintos bajo el mismo topónimo y **ninguno** tiene "1 cargador, 15 cartuchos, 4 detenidos". Puede ser una **fusión de dos casos**. **La ficha debe reescribirse o retirarse** |
| ARGOS 102 | **Chiapas — Benemérito de las Américas** | El desglose localizado (Selvin "N": 1 corta, 3 AK-47, 37 cargadores, 1 de disco con 59 cartuchos) **no coincide** con la ficha `ARM-003` de `_pendiente-barrido-ARGOS-88.md`. **O son dos hechos, o la ficha está mal.** ⚠️ Los "37 cargadores de 30 cartuchos cada uno" son **capacidad declarada, no cartuchos contados**: nunca convertir a 1,110 |

## Deuda editorial y de método

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 98 | **Lista blanca de egreso** | `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**. Sonda de ARGOS 102: 403 al CONNECT. **Cero portales leídos por acceso directo, decimotercera edición.** Sigue siendo **el único cambio que elevaría el techo del producto**, y ahora hay una prueba concreta de su coste: el pendiente de Veracruz está bloqueado por egreso sobre un portal que **sí tiene la ruta fechada que ARGOS necesita** |
| ARGOS 102 | **Mergear las ramas de edición a `main` — causa raíz del fallo de agentes, identificada** | Tres ediciones reportaron que `barrido-regional`, `procedencia-cifras` y `editor-duplicidad` "no resuelven por nombre". **La causa quedó identificada**: sus definiciones llegan con el `git merge --ff-only` que cada edición ejecuta al arrancar, es decir **después** de que la sesión tome su registro de agentes. Los agentes ya presentes en el árbol sí resuelven. **No se corrige edición por edición: se corrige mergeando a `main`.** Ninguna rama de ARGOS 88 a 102 está mergeada |
| ARGOS 99 | **Presupuesto de búsqueda** | ARGOS 102 cerró con **153 de 200 y los nueve topes respetados**, segunda edición consecutiva. Pero el mandato de `CLAUDE.md` (4 portales × 32 entidades + federales) **sigue siendo aritméticamente imposible**. **Tlaxcala quedó `NO REVISADA`** por agotamiento: es la primera entidad en esa casilla desde que se aplica la rotación |
| ARGOS 100 | **Correcciones de ARGOS 99 a ARGOS 98 que siguen sin aplicarse** | **Quinta edición sin ejecutarse.** Reintegrar Lázaro Cárdenas (`ARG-98-ARM-003`) al total de ARGOS 98; sustituir dos URL mal citadas en `argos-2026-08-15-fuentes.md`; incorporar tres hechos omitidos por ARGOS 98 (Chilpancingo/Los Ardillos 14-ago, Nopala Hidalgo 13-ago, excomandante por tortura en Cuautla); reintegrar el desglose de Sain Alto al total de ARGOS 99. **Se suman ahora las nueve recuperaciones `ARG-102-REC-*`**, que corresponden a las ventanas de ARGOS 96 a 101 |
| ARGOS 102 | **Rotación de cobertura — Ciclo C toca a ARGOS 103** | La mecánica **quedó escrita en `CLAUDE.md`** (ciclo A: Noroeste+Centro · B: Noreste+Golfo · C: Occidente+Sureste). ARGOS 102 aplicó el **Ciclo B** y **no produjo sentencia integrable**, pero sí cuatro correcciones de dominio y el arbitraje de Veracruz. **A ARGOS 103 le toca el Ciclo C: Occidente y Sureste encabezan el triaje judicial.** ⚠️ **Prioridad sobre el ciclo**: Tlaxcala quedó `NO REVISADA` y debe encabezar el triaje del Centro aunque no le toque |
| ARGOS 102 | **Directorio de dominios — creado, con deuda declarada** | `docs/dominios-oficiales.md` **existe** con 16 dominios fijados, corregidos o arbitrados. **Siguen sin dominio**: Aguascalientes, Nayarit y el portal web de Colima. **Sigue sin arbitrar**: Jalisco (dos variantes). **Hallazgo estructural a explotar**: la **Guardia Nacional**, fuente primaria declarada del módulo de armamento, **no lleva fecha en la URL en ninguna forma** — ningún boletín suyo es asignable a una ventana sin ancla externa |

## Cerrados recientemente

- **Desglose por entidad del boletín federal del 14-15-16 ago** — **CERRADO**
  (`ARG-102-REC-001`, `-002`). `CONFIRMADO POR CONCORDANCIA DE FRASE EXACTA`. Y con un hallazgo
  mayor: el renglón de mayor peso no era Michoacán sino **El Rosario, Sinaloa, con 303 AEI, 125 kg de
  explosivo y 175 kg de emulsión explosiva** — el mayor aseguramiento de explosivos de la serie.
  **ARGOS 101 citó ese mismo boletín para otro renglón y no lo extrajo.** El de Michoacán es **La
  Piedad** y va en **🔴**, vinculado a la agresión contra militares del 14-ago. *Cerrado; su
  reintegración a los totales de ARGOS 99/100 pasa a deuda editorial.*

- **El vacío del boletín federal del 17-ago** — **CERRADO COMO ERROR PROPIO** (`ARG-102-FE-003`).
  No existía: el boletín está indexado y el emisor había vuelto al **formato diario**. Es el
  **segundo falso vacío consecutivo del mismo emisor**, y por la misma causa: suponer que el formato
  es estable. *Cerrado; la **regla de la doble consulta** —por día suelto y por rango, siempre— queda
  escrita en `CLAUDE.md`.*

- **Coronango, Puebla** — **INTEGRADA** (`ARG-102-SEN-REC-001`), tras tres ediciones perdida dentro
  del archivo. Pero se cierra **desmintiendo su respaldo**: el *slug* con que ARGOS 98 la sostuvo es
  de **otro caso** del mismo municipio y el mismo delito. *Cerrado; la firmeza y el boletín de alzada
  siguen abiertos arriba.*

- **Tijuana `ARG-101-008`** — **CERRADO CON DOBLE CORRECCIÓN** (`ARG-102-FE-002`). El homicidio
  **sí cae dentro de la ventana de ARGOS 101** (17-ago, ~15:00 h de Tijuana), y ARGOS 101 lo publicó
  **absorbido en una ficha verde**. Además **sí hubo aseguramiento**. *Cerrado; la regla de que un
  delito y su detención son dos eventos queda escrita en `CLAUDE.md`.*

- **Colima `ARG-101-002`** — **RECLASIFICADO A 🔴** (`ARG-102-FE-008`). Los restos humanos quedan
  confirmados en cinco fuentes independientes. **Cambia la valoración de ARGOS 101.** Aparece además
  la **primera fuente institucional de Colima de la serie**. *Cerrado el extremo de los restos; el de
  los detenidos sigue abierto arriba.*

- **La Piedad `ARG-98-002`** — **CONTRADICCIÓN RESUELTA** (`ARG-102-FE-005`). El "4 abatidos" no
  venía de un balance de feb-2026 —esa atribución de ARGOS 101 era incorrecta— sino de contar como
  muerto al **cuarto agresor herido bajo custodia**. *Cerrado.*

- **El acervo sin fechar de Chiapas** — **PREMISA REFUTADA** (`ARG-102-FE-010`). Tres de seis
  boletines se fecharon y **los tres son de 2025**; **Frontera Comalapa**, el de mayor poder de
  fuego, es de **junio de 2025**. No es armamento acumulándose sin contarse: es un **archivo
  histórico sin fechar**. *Cerrado como acervo; dos fichas concretas quedan abiertas arriba.*

- **Suchiapa, Chiapas — Bulmaro "N"** — **CERRADO POR IRRELEVANCIA DE VENTANA.** En ningún escenario
  de fecha cae en la ventana de 102, y el barrido Sureste no localizó boletín que lo fije. Sigue
  siendo candidato a omisión de ARGOS 99, sin avance. *Se retira de PRIORIDAD 1.*

- **Cuautla, Morelos `ARG-99-004`** — **SE RECOMIENDA CERRAR EN 2 LESIONADOS.** Cuarto y quinto
  extremos independientes de "dos heridos", y **localizado el probable origen del error**: un
  agregado de **Cuernavaca y Tetecala** con "cuatro muertos y cinco heridos", que es otro hecho.
  *Cerrado con confianza Media; `fiscaliamorelos.gob.mx/prensa` queda localizado pero no devolvió el
  boletín.*

- **CDMX `ARG-101-005`** — **CIFRA CERRADA** (`ARG-102-FE-009`): 65 cartuchos y 1 cargador, donde
  ARGOS 101 publicó "sin cantidad". *Cerrado.*

- **Rotación de cobertura** y **directorio de dominios** — **AMBOS ESCRITOS.** La mecánica de
  rotación quedó en `CLAUDE.md` y el directorio existe en `docs/dominios-oficiales.md`. *Cerrados
  como deuda de documentación; su explotación continúa arriba.*

- **Registro de agentes — CAUSA RAÍZ IDENTIFICADA.** No es un defecto de las definiciones: llegan
  con el `merge` de arranque, después del registro de la sesión. *Cerrado el diagnóstico; la acción
  —mergear a `main`— pasa a deuda editorial.*

- **Suchiapa (señuelo)**, **Edomex verificentros** y **residuo de las "116 unidades"** — cerrados en
  ARGOS 101. *Se retiran de esta lista, conforme a la convención de dos ediciones.*

---

## Cómo arrancar la edición siguiente

Sesión nueva, un solo mensaje:

> Haz el ARGOS 103 de hoy siguiendo `CLAUDE.md`. Rama `claude/argos-103-<sufijo>`. Lee
> `reports/_pendientes.md`, `docs/dominios-oficiales.md` y la edición anterior
> (`reports/argos-2026-08-19*`) para no duplicar hechos ni perder seguimientos. Verifica antes si la
> rama de ARGOS 102 (`claude/argos-102-oqxpwf`) ya se mergeó a `main`; si no, trae sus cambios
> primero con `git merge --ff-only`.

Antes del commit, ejecutar los tres controles obligatorios de `CLAUDE.md` (`barrido-regional` ×6,
`procedencia-cifras` y `editor-duplicidad`) y **actualizar este archivo** con los pendientes que
deje la nueva edición.

### Lo que funcionó en ARGOS 102 y conviene repetir

1. **Ejecutar la verificación prioritaria primero y en solitario.** Esta vez **cerró casos**: resolvió
   el desglose federal con cifra exacta, produjo dos correcciones mayores y reetiquetó un pendiente
   de seis ediciones. Es la segunda edición que confirma que aislar esa fase rinde.
2. **Dar a cada equipo los señuelos ya descartados en su encargo.** Los nueve equipos recibieron por
   escrito lo que **no** debían reintroducir, y ninguno reintrodujo un señuelo cerrado. En cambio
   documentaron **más de cuarenta nuevos**, tres de ellos **fabricaciones del resumidor**: una fecha
   inventada y una atribución geográfica completa. La regla de exigir fecha en URL o titular está
   pagando su coste.
3. **Verificar personalmente las acusaciones graves contra el archivo.** La omisión de Tlapa la
   reportó un equipo, pero la confirmé con `grep` sobre la edición anterior antes de publicarla —y
   la única coincidencia resultó ser "Matlapa", de otro estado. Una acusación de omisión a una
   edición anterior **no se publica por reporte de un agente**.
4. **Arbitrar los conflictos de criterio con una regla, no caso por caso.** Tres hechos del mismo
   tipo llevaban tres colores distintos en dos ediciones. Se resolvió escribiendo el **criterio de
   iniciativa** en `CLAUDE.md`, no decidiendo cada uno por separado.
5. **Corregir el generador, no su salida.** Volvió a rendir dos veces: su validación de desborde
   atrapó una URL de 75+ caracteres, y al detectar el control que la móvil solo reproducía 13 de 27
   ARG-ID, se cambió la regla —las tablas anchas **se reflúan a tarjetas** en vez de retirarse— con
   lo que la paridad pasó a **29 de 29**. También dejó de fijar el número de páginas.
6. **Aceptar el diagnóstico de un control sin aceptar automáticamente su remedio.** `procedencia-cifras`
   detectó con razón que cuatro fiscalías declaradas no constaban en el registro, y propuso recortar
   la cifra. Recortar habría **borrado información verdadera para cuadrar un indicador**: lo correcto
   era documentarlas. **Un control señala el problema; la decisión editorial sigue siendo del
   redactor.**
7. **Desconfiar de los ceros regionales antes que de los territorios.** Las dos omisiones rojas de
   esta edición estaban en regiones que habían cerrado en cero **con todas sus entidades
   consultadas**. **Un cero regional es una hipótesis, no un dato.**
