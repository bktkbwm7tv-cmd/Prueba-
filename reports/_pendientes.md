# ARGOS — Pendientes vivos

Archivo de traspaso entre ediciones. **Cada corte lo actualiza como último paso**, antes de commit.
Sirve para que una sesión nueva pueda arrancar sin que nadie tenga que recordar ni transcribir la
lista de seguimientos: basta leer este archivo y la edición anterior.

Convención: cada entrada indica desde qué edición está abierta, qué hay que buscar y qué la cierra.
Cuando algo se resuelve, se mueve a "Cerrados recientemente" con una línea, y se borra de ahí en la
segunda edición siguiente.

**Última actualización**: ARGOS 104 (corte 2026-08-21).

---

## PRIORIDAD 1 para ARGOS 105

La auditoría de ARGOS 104 **respondió la pregunta de ARGOS 103 y encontró un modo de fallo
distinto**. ARGOS 103 diagnosticó un fallo de **búsqueda**: el hecho no se encontraba. ARGOS 104
encontró un fallo de **registro**: el hecho **se encontró, se verificó y se clasificó — y no se
publicó**. Los dos existen y se corrigen de forma distinta.

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 104 | **La deuda de registro: hechos que ARGOS ya verificó y nunca publicó** | La auditoría de **ARGOS 97** confirmó **seis vacíos** de las ventanas 94-96 y detectó **seis más** de forma incidental. De todos ellos **solo uno llegó a producir un ARG-ID** (`ARG-98-FE-001`, Huajicori). ARGOS 104 publicó el 🔴 de Aquila y el de Buenavista, e **inventarió otros cuatro sin ficha**. **Es la deuda más barata de saldar de todo el archivo**: los hechos ya están verificados y con fuentes: solo hay que registrarlos | Darles ARG-ID y ficha, o declararlos expresamente fuera de umbral. Los inventariados en la pág. 7 de ARGOS 104: **Sabanillas/Tuxpan-Tamiahua** (🟡), **Nuevo Teapa–Cosoleacaque** (🟡), **"El G1" Ensenada** (🟢), **"El Loco" Metepec** (🟢). Y los seis incidentales de `argos-2026-08-14-fuentes.md`, líneas 130-150, **que nadie ha revisado nunca** |
| ARGOS 104 | **Auditar hacia atrás las ventanas de ARGOS 88 a 93** | La auditoría por tipo de hecho **ya cubrió 95-98** (ARGOS 104) y **99-101** (ARGOS 103), y ARGOS 97 auditó 94-96 por su cuenta. **El tramo 88-93 no lo ha auditado nadie**, y es el más antiguo y el que se produjo con el método menos maduro | El mismo método que ha rendido tres veces: **consultar por tipo de hecho y no por entidad**, equipos temáticos (masacres y homicidios múltiples · violencia colectiva) más ronda de corroboración, **ejecutado primero**. El bloque de ataques contra autoridades sigue pudiendo omitirse |
| ARGOS 102 | **Sinaloa — 50 años a Wilberth "N" por secuestro agravado** | **Localizado por el Noroeste en ARGOS 104 y verificado con `grep`: no figura en ninguna edición.** Publicación **15-ago** con fecha en la ruta (`fuentesfidedignas.com.mx/index.php/2026/08/15/`), fuera de toda ventana cubierta | Boletín de la FGE de Sinaloa. Mientras no exista, `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR`. **Candidato a omisión de la serie 98/99** |

## Seguimientos judiciales abiertos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 101 | **Durango — Lerdo** (`ARG-101-SEN-001`) | **Gana municipio por primera vez: Lerdo**, no genéricamente "Región Laguna", y su **primera corroboración independiente** (El Siglo de Torreón). ⚠️ **Duplicidad interceptada en ARGOS 104**: el buscador devolvió el mismo *slug* bajo `/2026/08/20/` y bajo `/2026/08/17/`; dos consultas de control confirmaron que **es un solo boletín bajo dos rutas**, no una segunda condena | **Pena exacta y firmeza: siguen sin obtenerse.** Continúa en "más de 26 años", **no sumable** |
| ARGOS 102 | **Coronango, Puebla** (`ARG-102-SEN-REC-001`) | **Gana su primera ancla fechada** —`intoleranciadiario.com/…/2026/08/11/`— y los dos sentenciados individualizados: **Anadalay "N" y Carlos Andrés "N"**, violación equiparada agravada, hecho de ene-2023, **confirmada en alzada**. La fecha lo sitúa **fuera de toda ventana reciente** | ⚠️ **Contradicción nueva de ARGOS 104**: un medio publica **23 años** frente a **26 a 7 m 15 d**. `CONTRADICHA — reportar ambas`. Las **212 UMA siguen `SIN ANCLA DOCUMENTAL`** y **no se convierten a pesos**. Candidato a segundo GUID: `fiscalia.puebla.gob.mx/Home/Comunicado/627ec10a-…` — **no verificable sin lectura directa** |
| ARGOS 99 | **SLP — Matlapa**, Elías "N" | **Cuarta URL localizada en ARGOS 104, ninguna fechada.** Se precisa el delito: **lesiones doblemente agravadas**, hecho de ago-2024, procedimiento abreviado, 2 años 8 meses | El boletín de la FGE SLP. **El término jurídico está expreso; lo que falta es la fecha** |
| ARGOS 99 | **QRoo — Playa del Carmen**, 50 años (`ARG-103-SEG-001`) | Fechado el **12-ago**, lo que lo saca de toda ventana cubierta. Sin boletín de `fgeqroo.gob.mx` | **No integra.** ARGOS 104 no le gastó búsquedas. **No reabrir salvo que aparezca fuente oficial** |
| ARGOS 99 | **Tabasco — Cunduacán**, Miguel "N" (`ARG-103-SEG-002`) | ARGOS 104 añade que el boletín **cubre Centro, Cárdenas y Cunduacán**, pero **no devolvió su `id`** | ⚠️ **El equipo del Golfo recomienda no gastar más búsquedas**: tres ediciones y once `id` recuperados demuestran que **el patrón `/Boletin/Index/<id>` no es resoluble por buscador** |
| ARGOS 102 | **Jalisco — Tizapán el Alto: 19 personas sentenciadas por la FGR** | ~332 años acumulables, ventana de ARGOS 95/96. **Tercera edición que se reencuentra y no se duplica** | El comunicado de la FGR. **No gastar búsquedas dedicadas** |
| ARGOS 102 | **Sonora — Nogales: 21 a 7 m 15 d a dos personas** | ARGOS 104 lo reconfirma **con dos URLs fechadas en ruta** (`eldiariodesonora.com.mx/…/2026/08/12/`, `telemax.com.mx/blog/2026/08/12/`): el hecho es del **12-ago** | **Confirmado fuera de toda ventana reciente.** No aparece en ninguna edición: es candidato de la ventana de ARGOS 96 |
| ARGOS 96 | **Ruffo Appel / Ingemar**, huachicol fiscal (`ARG-98-SEG-001`) | **Primer movimiento en cinco ediciones**: **Rigoberto Blanco Cantú se entregó en EU** (red Farías / Mefra Fletes, nexos con Cártel del Golfo y CJNG), publicado el **20-ago** con fecha en la ruta | Sentencia de amparo de fondo. El movimiento **no aporta línea a ningún conteo** |
| ARGOS 101 | **Guerrero — 5 sentencias** y **Guanajuato — 36 sentenciadas** | Sin avance. Agregados **sin desglose nominal**; el de Guanajuato es **anual**. Reconfirmados y no integrados por tercera edición | El desglose caso por caso |
| ARGOS 104 | **Durango — la pena exacta y los importes de `ARG-104-SEN-001`** | El *slug* institucional sostiene **«más de 7 años»** y la fecha de publicación; **no sostiene «7 años 10 meses», ni los $64,150.38 de multa, ni los $397,554.90 de reparación**, que proceden del resumen del buscador. Lo detectó `procedencia-cifras` | Lectura directa del boletín o una segunda fuente que repita los importes. ⚠️ **Si ARGOS 105 no lo consigue, la regla de las cifras arrastradas obliga a retirar el detalle en la segunda edición** y dejar la pena como «más de 7 años», no sumable. **La sentencia seguiría contando; el detalle no** |

## Vacíos de publicación que siguen sin resolverse

| Desde | Caso | Estado |
|---|---|---|
| ARGOS 104 | **Occidente en el boletín federal del 19-ago** | Los renglones de **Romita (Gto.), Tlajomulco (Jal.) y Los Reyes de Salgado (Mich., 5 largas y 5 cargadores)** **no se integraron**: el equipo de la región **no pudo anclarlos a una URL fechada**, aunque otros tres equipos sí localizaron el boletín. **Integrarlos por inferencia cruzada sería la fusión que los controles impiden.** `PENDIENTE DE ANCLA FECHADA` — lo cierra una consulta al boletín por título sin restricción de dominio |
| ARGOS 104 | **Veracruz — el bloque de hechos graves del agregador** | Cuerpo desmembrado en Coatzintla, cabeza humana en Poza Rica, normalista asesinada en Tuxpan. ⚠️ **La fuente es un agregador sin fecha en ruta** y **el mismo bloque aparece casi idéntico en resultados del 25-26 de junio de 2026**: riesgo alto de recirculación. **Si se fechara en ventana sería 🔴.** Basta una URL fechada en ruta o un boletín de la FGE de Veracruz |
| ARGOS 102 | **Jiutepec, Morelos — ataque con dron y explosivos** | ⚠️ **Diagnóstico nuevo de ARGOS 104: el pendiente está contaminado con un hecho de 2025.** El racimo devuelto es mayoritariamente de **agosto de 2025** (`informador.mx/…/20250831-0020`), y el resumidor narró como actual una secuencia de cateos que corresponde a ese año. Las dos URLs de `diariodemorelos.com` **siguen sin fecha en ruta y podrían ser dos hechos o uno solo**. `PENDIENTE DE ANCLA FECHADA` **con advertencia expresa de trampa de aniversario**. **No se declara 🔴** |
| ARGOS 102 | **`gabinetedeseguridad.gob.mx/resultados/` — obligatorio desde el 1-sep** | Sigue **BLOQUEADO** al acceso directo. ⚠️ **Matiz de ARGOS 104**: la ruta `/contenido/<id>/` **sí devuelve resultados indexados** y publica sentencias de la FGR. **No es un dominio muerto, es un dominio ilegible por acceso directo**: por buscador es utilizable |
| ARGOS 102 | **Tijuana, col. Hipódromo** — cuatro cuerpos en cajuelas (`ARG-103-REC-002`) | Sin avance. Sigue `NO INTEGRABLE`: los cuerpos aparecieron en **puntos distintos a lo largo de ~8 horas**. Lo cerraría un boletín de `fgebc.gob.mx` que vincule los cuatro casos |
| ARGOS 98 | **La Paz, BCS**, abuso sexual (11-ago) | **Sexta edición sin avance.** ARGOS 104 no le gastó búsqueda, conforme al tope. `Pendiente de corroboración independiente` |
| ARGOS 101 | **Zinapécuaro** (`ARG-101-003`) — saldo del enfrentamiento del 17-ago | Sin avance. **Tres hechos con la misma firma** en el mismo municipio. Se mantiene 🟡 |
| ARGOS 102 | **Los Reyes, Michoacán** (`ARG-102-002`) — sin fuente institucional | Sin avance. ⚠️ ARGOS 104 confirma que **el aseguramiento de Los Reyes del boletín federal es sin detenidos y sin abatidos**: **no es el hecho de los cinco abatidos** y no debe fusionarse con él |
| ARGOS 102 | **Alfajayucan, Hidalgo** (`ARG-102-005`) | Sin avance. Solo páginas-etiqueta sin fecha. `PENDIENTE DE ANCLA FECHADA` |
| ARGOS 104 | **Coahuila — brecha Rancherías, Hidalgo** | Enfrentamiento con civiles armados, sin fallecidos ni detenidos. **Ninguna de las tres URLs lleva día** y las cantidades no se publican. Sería 🟡 si se fechara |
| ARGOS 104 | **Chiapas — Mapastepec** | Dos detenidos tras disparar contra policía estatal; 2 armas cortas y 3 cargadores. La URL es **ruta *hash* sin fecha**. Candidato 🟡 `PENDIENTE DE ANCLA FECHADA` |

## Contradicciones abiertas

| Desde | Caso | Detalle |
|---|---|---|
| ARGOS 104 | **Chiapas: Sureste o Pacífico** | Se regionaliza como **Sureste** desde ARGOS 88, pero en `argos-2026-08-03/04.html` figuró como **Pacífico**, y `CLAUDE.md` exige regionalización consistente entre ediciones. **Sureste es la lectura correcta.** *No se toca el archivo antiguo*: queda anotado para que la divergencia no se reabra |
| ARGOS 104 | **Puerto Madero, Chiapas** (`ARG-104-ARM-003`) | **Dos lecturas incompatibles de la misma fuente institucional**: **0 armas cortas y 172 cartuchos desglosados** frente a **4 cortas de 9 mm y 322 cartuchos de 7.62×39**. Solo se integraron las **3 largas y los 4 detenidos**. `CONTRADICHA — NO INTEGRAR HASTA VALIDACIÓN` |
| ARGOS 104 | **Juchipila — número de personas liberadas** | **Contradicción dentro de la misma fuente**: el boletín estatal y el *slug* de El Financiero dicen **dos**, su titular dice **una**. Se publicó **2** con la salvedad anotada |
| ARGOS 104 | **El fusil Barrett de La Angostura** | La fuente publica "un fusil Barrett, seis armas largas" **sin precisar si está comprendido**. `NO DETERMINABLE` — se publica por separado, no se suma |
| ARGOS 103 | **Armamento especial vs. armas largas** (`ARG-103-ARM-001`) | ⚠️ **La balanza se inclina, pero no se cierra.** El boletín federal del 19-ago enumera "nueve armas largas, dos cortas" y, **como renglones separados y adicionales**, "cinco ametralladoras, un fusil Barrett": sostiene que **el armamento especial NO está comprendido**. Confianza **Media** —es paráfrasis del resumidor, no lectura literal—. ⚠️ **Nota**: el boletín federal da **dos armas cortas** frente a **una** de la ficha publicada |
| ARGOS 99 | **Culiacán** (`ARG-99-001`) | **Ubicación conciliada por ARGOS 104**: cruce de los bulevares **Constitución y Lázaro Cárdenas**, frente al Palacio de Gobierno; víctimas **Jahir Alexander "N" (29)** y **Miguel Ángel "N" (32)**, atacadas con fusiles automáticos. **Hora: tres versiones —12:30, 13:00 y ~14:00—.** `CONTRADICHA — reportar las tres, no promediar`. **Sin detenidos: confirmado** |
| ARGOS 101 | **Mapimí, Durango** | **Dato nuevo**: el desglose es **8 largas + 4 cortas = 12 armas**, con **87 cargadores y 4,715 cartuchos**, frente a los **65 cargadores** del boletín federal. **La contradicción de cargadores sigue abierta**; el desglose 8/4 es ganancia |
| ARGOS 100 | **Altamira, Tamaulipas** (`ARG-100-001`) | **Se propone cerrar como `2 o 3 — DISCREPANCIA NO RESUELTA`.** El Universal mantiene **3**, `opciudadana.com` mantiene **2**, y el "comunicado de la Primera Zona Naval del 15-ago" **sigue sin existir localizable**. ARGOS 104 sí acredita que la Primera Zona Naval participó, y fija la publicación el **16-ago**, lo que **desmiente el "hecho del 17-ago" de ARGOS 100** |
| ARGOS 103 | **Las 84 UMA de Tlaxcala** | Sin cambio. `CONTRADICHA — REQUIERE LECTURA DIRECTA`. **ARGOS 104 no gastó ninguna búsqueda**, conforme a lo decidido: arbitrar entre dos paráfrasis del mismo resumidor no produciría un dato mejor |
| ARGOS 103 | **La cifra de bloqueos de Michoacán** (`ARG-103-001`) | Sin cambio. Cuatro lecturas publicadas sin fundir. `CONTRADICHA — reportar todas, no promediar` |
| ARGOS 103 | **La reserva de color de `ARG-103-002`** | Sin cambio. Una fuente que sitúe la agresión a la GN en el punto de la captura obliga a fe de erratas |
| ARGOS 102 | **Chiapas — Cintalapa y Benemérito de las Américas** | ⚠️ **ARGOS 104 aporta un deslinde**: ambos reaparecen con GUID sin fecha, y **se confirma que son casos distintos de los del archivo** — el de Benemérito **no es el de Selvin "N"**. La ficha de Cintalapa **sigue debiendo reescribirse o retirarse**. Los "37 cargadores de 30 cartuchos cada uno" son **capacidad declarada**: nunca convertir a 1,110 |
| ARGOS 101 | **Colima** (`ARG-101-002`) — detenidos | Sin arbitrar: Infobae y Puente Libre no reportan detenidos, El Occidental reporta 1 mujer detenida |
| ARGOS 98 | **"Operación Sable", Mazatlán** (`ARG-97-ARM-003`) · **Privada Amberes, Ciudad Juárez** | Sin avance en ninguno de los dos |
| ARGOS 99 | **Indicador SESNSP: −48% frente a −60%** | Sin cambio. `HEREDADO — NO REVERIFICADO`. **Origen verificado**: entró en ARGOS 86 con respaldo citable real, así que **se conserva y no procede fe de erratas** |
| ARGOS 100 | **Azcapotzalco, CDMX** · **Campeche — Hopelchén** | Sin cambio. El primero es del 14-jun-2026 y no se reabre; el segundo, `POSIBLE DUPLICIDAD`, reencontrado y no reintegrado por tercera edición |

## Deuda editorial y de método

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 98 | **Lista blanca de egreso** | `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**. **Cero portales leídos por acceso directo, decimoquinta edición.** Sigue siendo **el único cambio que elevaría el techo del producto** por encima de ★★★★☆ |
| ARGOS 102 | **Mergear las ramas de edición a `main`** | **Ninguna rama de ARGOS 88 a 104 está mergeada.** ⚠️ **ARGOS 104 confirmó el diagnóstico de forma limpia**: `barrido-regional`, `procedencia-cifras` y `editor-duplicidad` **fallaron por nombre en las tres invocaciones**, y el rodeo —lanzarlos como `general-purpose` diciéndoles que lean su archivo en `.claude/agents/`— **funcionó en las nueve**. Ya no hace falta diagnosticar: **aplicar el rodeo directamente** y, cuando se pueda, mergear a `main`, que es la corrección de fondo |
| ARGOS 104 | **Rotación de cobertura — a ARGOS 105 le toca el Ciclo B** | ARGOS 104 aplicó el **Ciclo A** (Noroeste + Centro) y lo declaró. **Rendimiento: positivo y comprobable** — la única sentencia integrable del corte apareció en **Durango**, primera entidad del triaje del Noroeste, igual que en ARGOS 101. **A ARGOS 105 le toca el Ciclo B: Noreste + Golfo.** ✔ **Ninguna entidad quedó `NO REVISADA`**, así que **no hay prioridad sobre el ciclo** y el turno se aplica limpio |
| ARGOS 100 | **Correcciones de ARGOS 99 a ARGOS 98 que siguen sin aplicarse** | **Séptima edición sin ejecutarse.** Reintegrar Lázaro Cárdenas (`ARG-98-ARM-003`) al total de ARGOS 98; sustituir dos URL mal citadas en `argos-2026-08-15-fuentes.md`; incorporar tres hechos omitidos por ARGOS 98 (Chilpancingo/Los Ardillos 14-ago, Nopala Hidalgo 13-ago, excomandante por tortura en Cuautla); reintegrar el desglose de Sain Alto al total de ARGOS 99. Se suman las nueve recuperaciones `ARG-102-REC-*` y los 27 AEI de Escuinapa |
| ARGOS 104 | **La regla del mando todavía no se aplica sola** | **Segunda edición consecutiva** en que `editor-duplicidad` tiene que retirar autorreferencia del cartelón: esta vez **doce pasajes** —dos filas del indicador de cobertura, dos tablas de auditoría, tres invocaciones de `grep` y cuatro pasajes de ARGOS hablando de ARGOS—, pese a que el coordinador tenía la regla presente desde el arranque. **Ese control es, por ahora, lo único que la hace efectiva.** Conviene redactar el borrador **sin** esos bloques desde el principio, en vez de escribirlos y retirarlos |
| ARGOS 104 | **Las portadas de ARGOS 95, 96, 99, 100 y 101 no reflejan su conteo rectificado** | Los **cinco cartelones llevan ya su bloque de fe de erratas encima de la valoración**, pero sus **portadas** —semáforo y contadores del radar— siguen mostrando el conteo original, porque se generan desde el arreglo `EVENTOS` de cada edición y regenerarlas obligaría a reescribir fichas que la rectificación deja intactas. Verificado con `grep` que `NO DETERMINABLE` **solo aparece en la valoración**, que es donde está el bloque. **Residuo conocido y acotado** |
| ARGOS 104 | **Consultar el boletín federal por título, no solo por dominio** | **Ya incorporado a `CLAUDE.md`** como «regla de la triple consulta»: día suelto + rango + **título sin restricción de dominio**. El boletín del 19-ago existe y **`gob.mx` no lo indexó**: solo aparece por republicadores. ⚠️ **Acotación de `editor-duplicidad`, que corrige a esta misma edición**: el falso vacío acreditado es el del **18-ago**, con URL canónica en `gob.mx`. **El del 19 no lo es** — se publicó el 20-ago, dentro de la ventana de ARGOS 104, así que ARGOS 103 no pudo verlo. **No se acusa a ninguna edición anterior por él** |

## Cerrados recientemente

- **La auditoría de las ventanas 95-98** — **CERRADA, con un veredicto distinto del esperado**
  (`ARG-104-REC-001/002`, `ARG-104-FE-001/002`). Dos eventos 🔴 más, ambos en Michoacán, y sobre todo
  el hallazgo de que **el fallo no es solo de cobertura sino de registro**: el 🔴 de Aquila lo había
  verificado y clasificado **el propio ARGOS 97**, y seis ediciones pasaron junto a él sin
  publicarlo. *Cerrada la pregunta; se abre en su lugar la deuda de registro de PRIORIDAD 1.*

- **La rectificación en bloque de ARGOS 99, 100 y 101** — **EJECUTADA.** Se eligió **insertar la fe
  de erratas en cada cartelón afectado** y no publicar un cartelón de rectificación aparte, porque
  un documento separado deja intacta la valoración falsa **en el punto de consulta**. Seis piezas
  corregidas (escritorio y móvil de las tres), más cuatro de ARGOS 95 y 96. *Cerrado.*

- **Colima — deuda de cobertura SALDADA**, y con corrección de directorio: **sí tiene portal
  canónico**, `fgecolima.mx`, que tres ediciones no encontraron **por buscarlo bajo `.gob.mx`**.
  Sale de `NO REVISADA` con hecho propio en ventana. *Cerrado; ninguna entidad queda en esa casilla.*

- **Aguascalientes y Nayarit — clasificados.** Ambos **clase C**. *Cerrada la deuda que ARGOS 103
  dejó a medias.*

- **Veracruz — variante arbitrada** tras dos ediciones: la canónica es la ruta **fechada**,
  `veracruz.gob.mx/AAAA/MM/DD/<slug>/`. *Cerrado; queda solo el Estado de México, y con el matiz de
  que **su problema no es de variante sino de indexación**.*

- **El vacío del boletín federal de tres días** — **REFUTADO en dos de los tres días.** *Cerrado como
  vacío; abre en su lugar la deuda de método de la tercera forma de consulta.*

- **"El operativo de Michoacán no tiene una línea escrita de fuente federal"** — **CERRADO.** El
  boletín del 19-ago lo recoge con desglose: 12 detenidos, 5 ametralladoras, 1 fusil Barrett,
  9 armas largas, 2 cortas, 1 dron y 8 AEI.

- **Ciudad Juárez — rescate de 14 personas** — **CERRADO COMO FUERA DE VENTANA.** El hecho es del
  **21 de julio de 2026**, con boletín propio de la SSPE de Chihuahua.

- **Zacatecas — 100 años a seis personas** — **SE PROPONE CERRAR** como `NO ASIGNABLE A NINGUNA
  VENTANA`. Tercera edición sin ancla externa; hecho de **ago-2021**, trampa de aniversario
  confirmada, y `ljz.mx` solo devuelve otro caso (1,416 años, oct-2024). *Seguir gastando búsquedas
  aquí no es rentable.*

- **El bug de `colspan` del generador móvil** — **CERRADO, corregido en la herramienta y no en su
  salida.** `_celdas_a_tarjeta` emparejaba celda *i* con cabecera *i* ignorando `colspan`, de modo
  que la fila TOTAL de la pág. 5 —que abre con `colspan=4` y cierra con `colspan=2`— salía en la
  móvil con **todas las etiquetas desplazadas**: publicaba «Cortas 172», «Granadas 16» y
  «Cartuchos 0». **Cifras falsas para quien lea en teléfono**, no un defecto de maquetación. Lo
  detectó `procedencia-cifras`. *La corrección beneficia a todas las ediciones futuras.*

- **Los pendientes cerrados en ARGOS 103** —la auditoría 99-101, los 27 AEI de Escuinapa, Tlaxcala,
  Jalisco, Veracruz como no reintentable y la causa raíz del fallo de agentes— *se retiran conforme
  a la convención de dos ediciones.*

---

## Cómo arrancar la edición siguiente

Sesión nueva, un solo mensaje:

> Haz el ARGOS 105 de hoy siguiendo `CLAUDE.md`. Rama `claude/argos-105-<sufijo>`. Lee
> `reports/_pendientes.md`, `docs/dominios-oficiales.md` y la edición anterior
> (`reports/argos-2026-08-21*`) para no duplicar hechos ni perder seguimientos. **Mergea las ramas
> antes de empezar**: comprueba si `claude/argos-104-c0x7fm` ya está en `main` y, si no, trae sus
> cambios con `git merge --ff-only`.
>
> **La ventana abre donde cerró ARGOS 104: 2026-08-21 07:55 CDMX.** Confirma la hora real de CDMX al
> arrancar y séllala en encabezado, pie y cada marca "Consulta:".
>
> ⚠️ **REGLA EDITORIAL, POR ENCIMA DE TODO LO DEMÁS: el cartelón es un análisis para un mando, no un
> informe sobre ARGOS.** Nada de textos de auditoría. Nada de presupuesto de búsqueda, ciclos de
> rotación, señuelos descartados, `grep`, cobertura del instrumento, acusaciones a ediciones
> anteriores ni ARGOS hablando de ARGOS. **Y nada de repetir el mismo hecho o la misma cifra en
> varias secciones**: cada hecho va en «Ejes del día» y en su ficha, y en ningún sitio más. Todo lo
> de método va al archivo de fuentes y a `_pendientes.md`. Lo que le sirve a un mando es dato
> criminal trazable: hechos, entidad y municipio, fecha, armamento con su desglose, detenidos,
> víctimas, fosas, secuestros, sentencias — cada cosa con su fuente, su nivel de confianza y su
> ARG-ID.
>
> **PRIORIDAD 1 — saldar la deuda de registro. No cuesta búsquedas, así que hazlo primero.**
> ARGOS 104 descubrió que el fallo de la serie no es solo de búsqueda sino **de registro**: hechos
> que ARGOS ya encontró, verificó y clasificó, y que nunca recibieron ficha. Cuatro están
> inventariados en `argos-2026-08-21-fuentes.md` con sus fuentes —**Sabanillas** y **Nuevo
> Teapa–Cosoleacaque** (Veracruz, 🟡), **"El G1"** de Ensenada y **"El Loco"** de Metepec (🟢)—.
> Dales ARG-ID y ficha, o decláralos fuera de umbral. Y **revisa los seis vacíos incidentales de
> `argos-2026-08-14-fuentes.md`, líneas 130-150, que nadie ha mirado nunca.**
>
> **PRIORIDAD 2 — auditar hacia atrás las ventanas de ARGOS 88 a 93**, el único tramo que nadie ha
> auditado. Método que ha rendido tres veces: **por tipo de hecho y no por entidad**, equipos
> temáticos (masacres y homicidios múltiples · violencia colectiva), **ejecutado primero y en
> solitario**. El bloque de ataques contra autoridades puede omitirse: ese tipo de hecho sí se
> recoge.
>
> ⚠️ **Lo que la auditoría produce son fichas de hecho criminal, no una página de auditoría.** Cuatro
> apartados, ARG-ID `-REC-`, ventana de origen declarada, **fuera de los totales del corte**, y su
> efecto en una **fe de erratas compacta**. Nada más de la auditoría entra al cartelón.
>
> **Verifica con `grep` sobre TODO el repositorio, no solo sobre `indice-arg-id.md`**, antes de
> publicar cualquier hecho como omisión de una edición anterior. El hallazgo mayor de ARGOS 104 no
> estaba en el índice: estaba en el cuerpo de dos archivos de fuentes y de dos cartelones. Y al
> revés — en ARGOS 104 uno de los tres candidatos a omisión resultó **ya publicado**.
>
> Aplica el **Ciclo B** (Noreste + Golfo encabezan el triaje judicial). **Ninguna entidad quedó
> `NO REVISADA`**, así que el turno se aplica limpio, sin prioridad sobre el ciclo.
>
> **Consulta el boletín federal en las tres formas** —día suelto, rango y **título sin restricción de
> dominio**—: la regla está en `CLAUDE.md`. El del 19-ago existía y `gob.mx` no lo indexó.
>
> Antes del commit, ejecuta los tres controles obligatorios (`barrido-regional` ×6,
> `procedencia-cifras` y `editor-duplicidad`) y actualiza `reports/_pendientes.md`.
>
> **Los agentes ya resuelven por nombre**: `barrido-regional`, `procedencia-cifras` y
> `editor-duplicidad` están disponibles como tipo de agente. Si alguno fallara, lánzalo como
> `general-purpose` diciéndole que **lea primero su archivo en `.claude/agents/`**.
>
> **No gastes búsquedas** en: el pendiente de Veracruz (`BLOQUEADO POR EGRESO`, seis ediciones), las
> 84 UMA de Tlaxcala (dos paráfrasis del mismo resumidor), el `id` del boletín de Cunduacán (tres
> ediciones y once `id` demuestran que no es resoluble por buscador), ni Zacatecas 100 años (hecho de
> ago-2021, trampa de aniversario confirmada).

### Lo que funcionó en ARGOS 104 y conviene repetir

1. **Verificar con `grep` toda acusación de omisión, antes de publicarla.** De los tres candidatos
   que la auditoría trajo, **uno era falso**: San Pedro Amuzgos ya estaba publicado como
   `ARG-99-003`, y **mejor sostenido en el archivo que en el hallazgo** —el archivo tiene la fuente
   institucional que el equipo no encontró—. Tercera edición consecutiva en que este control salva
   al producto de acusar a una edición anterior de algo que no hizo.
2. **Leer las ediciones anteriores, no solo el índice.** El hallazgo mayor de este corte —el 🔴 de
   Aquila— **no estaba en `indice-arg-id.md`**, porque nunca recibió ARG-ID: estaba en el **cuerpo de
   dos archivos de fuentes**, como nota de método. El índice responde "¿tiene ARG-ID?"; no responde
   "¿ARGOS ya sabía esto?".
3. **La ronda de corroboración vuelve a rendir**, cuarta edición consecutiva: cerró una reserva
   abierta (Ciudad Juárez, fuera de ventana por tres semanas), fijó la hora que decidía una ventana
   (Buenavista, 06:30, media hora antes del cierre) y **deslindó un falso positivo** (el boletín de
   la FGE de BC, de título casi idéntico y de otro caso).
4. **Publicar las cifras contradictorias sin fundirlas**, y aplicarlo también **dentro de una misma
   fuente**: en Juchipila el titular y el *slug* del mismo medio dan cifras distintas de personas
   liberadas. **La contradicción no siempre está entre fuentes.**
5. **Corregir el generador, no su salida.** Su validación de desborde atrapó de nuevo una URL de 75+
   caracteres antes de publicar; se corrigió **en el escritorio** y se regeneró. Paridad
   escritorio/móvil: **9 de 9 fichas**, contadores coincidentes.
6. **La rotación de cobertura vuelve a acertar donde importa.** Segunda vez en la serie que **la
   única sentencia integrable del corte aparece en la primera entidad del triaje** de la región que
   encabezaba por ciclo. No es cobertura cosmética: **cambia lo que el producto encuentra**.
7. **Un equipo que no encuentra algo puede estar señalando un problema real.** Occidente no localizó
   el boletín federal del 19-ago que otros tres equipos sí encontraron. Su conclusión era incompleta,
   pero **su cautela era correcta** y destapó la causa: **el portal no indexa su propio boletín**.
