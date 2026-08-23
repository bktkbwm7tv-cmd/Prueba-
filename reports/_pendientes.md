# ARGOS — Pendientes vivos

Archivo de traspaso entre ediciones. **Cada corte lo actualiza como último paso**, antes de commit.
Sirve para que una sesión nueva pueda arrancar sin que nadie tenga que recordar ni transcribir la
lista de seguimientos: basta leer este archivo y la edición anterior.

Convención: cada entrada indica desde qué edición está abierta, qué hay que buscar y qué la cierra.
Cuando algo se resuelve, se mueve a "Cerrados recientemente" con una línea, y se borra de ahí en la
segunda edición siguiente.

**Última actualización**: ARGOS 105 (corte 2026-08-23).

---

## PRIORIDAD 1 para ARGOS 106 — la ventana que ARGOS 105 no pudo barrer

**ARGOS 105 se quedó sin presupuesto de búsqueda (200/200 de la sesión) antes de que cinco de las
seis regiones ejecutaran una sola consulta.** No es un vacío del territorio: es un vacío de
observación, y está declarado como tal en todo el producto.

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 105 | **La ventana 2026-08-21 07:55 → 2026-08-23 08:00 quedó sin barrer en 27 de 32 entidades** | Solo se barrió el **Noreste** (Coahuila, NL, Tamaulipas, SLP, Zacatecas), con resultado cero. **Noroeste, Occidente, Centro, Golfo y Sureste quedan `NO REVISADA`**, igual que **el emisor federal**: la regla de la triple consulta **no llegó a ejecutarse** para los boletines del 21 y 22 de agosto | Barrer esa ventana **además** de la propia de ARGOS 106. ⚠️ **Prioridad sobre el ciclo**: la regla es que las entidades `NO REVISADA` encabezan el triaje de la edición siguiente **aunque no les toque por ciclo**. Son 27, así que en la práctica **ARGOS 106 encabeza con cobertura, no con turno**, y el ciclo se reanuda después |
| ARGOS 105 | **El Ciclo B se aplicó a medias** | Encabezaban el triaje judicial **Noreste y Golfo**. El Noreste lo ejecutó —resultado negativo, sin sentencia en ventana—; **el Golfo no llegó a lanzar consulta**. La mitad del experimento de rotación **no se realizó** | Ejecutar el triaje judicial del **Golfo** (Veracruz, Tabasco) en ARGOS 106, y solo entonces dar el Ciclo B por concluido. **A ARGOS 106 le correspondería el Ciclo C (Occidente + Sureste)**, pero la prioridad de cobertura vence al turno |
| ARGOS 105 | **Presupuesto de búsqueda: el fallo es silencioso y ya costó una edición entera** | El agotamiento **no avisa**: una región que arranca tarde entrega un informe vacío indistinguible de «no hubo publicaciones». El equipo del Sureste lo detectó y lo reportó **en vez de entregar el informe vacío**, que es lo que salvó la edición de declarar un falso `SIN DATO` nacional | Arrancar el barrido regional **antes** que cualquier otro encargo, o repartir el presupuesto explícitamente por región. La auditoría retroactiva, por valiosa que sea, **consumió el presupuesto que le tocaba al corte del día** |

## Seguimiento nuevo, entregado por el usuario y sin corroborar

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 105 | **Zapopan, Jalisco — Octavio Haro, empresario reportado como desaparecido, hallado muerto** | Reportado por el usuario durante la elaboración de ARGOS 105, con la indicación de que la autoridad apunta a **«un posible móvil relacionado con su entorno personal»** y de que es **tema de atención en la línea de desaparecidos**. ⚠️ **ARGOS 105 no pudo corroborarlo: cero búsquedas disponibles.** No se publicó ficha porque **no hay una sola URL que lo sostenga**, y la regla es que un dato que no puede comprobarse no aparece | **Encargo explícito para ARGOS 106**, y de los primeros: fecha del hallazgo y fecha del reporte de desaparición —son campos distintos—, municipio exacto, boletín de la **FGE de Jalisco** (`fiscalia.jalisco.gob.mx`, **clase A/B: sus *slugs* llevan fecha completa como sufijo**), y contraste del móvil declarado. **Si se acredita, es 🟡 o 🔴 según agravantes**, y entra por la línea de personas no localizadas |

## Deuda de método abierta por ARGOS 105

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 105 | **La serie tiene al menos un intervalo que ninguna edición cubre** | Hallazgo nuevo, y es un **tercer modo de fallo**, distinto de los dos conocidos. No es de búsqueda (el hecho no se encuentra) ni de registro (se encuentra y no se ficha): es **de continuidad de ventana**. El multihomicidio de Saltillo (`ARG-105-REC-001`) ocurre la **tarde del 4-ago**; **ARGOS 88 cerró a las 07:15 de ese día** y la ventana declarada de **ARGOS 90 abre el 5-ago**. **No existe ARGOS 89.** El hecho no fue omitido por nadie: cayó entre dos ediciones. **Acción**: recorrer las ventanas declaradas de toda la serie y **listar los intervalos sin cobertura**. Es trabajo de `grep` sobre los archivos de fuentes, **no cuesta búsquedas**, y cada hueco que aparezca es un tramo donde la serie no puede afirmar nada |
| ARGOS 105 | **Tres «vacíos» del archivo no lo eran** | El contraste con `grep` sobre todo el repositorio desmintió **tres acusaciones de omisión** heredadas: los **funcionarios de Medio Ambiente del Edomex** (acusación de ARGOS 97) estaban publicados como `ARG-94-003`; los **19 sentenciados de Tizapán el Alto** (acusación de ARGOS 98) estaban publicados como `ARG-94-SEN-002`; y **Apatzingán** ya lo había anulado ARGOS 98. **Dos pendientes vivos descansaban sobre una premisa falsa.** **Acción**: antes de heredar un pendiente, comprobar que el hecho que lo motiva no está ya en el archivo. Cuesta un `grep` |
| ARGOS 105 | **Un `grep` solo sirve si se leen sus resultados** | El control `procedencia-cifras` descubrió que `ARG-105-REC-007` iba a publicar la versión de ARGOS 98 de Pesquería **sin cotejar `ARG-102-FE-004`**, que ya la había reconciliado mejor. **El `grep` de PRIORIDAD 1 sí devolvió esa línea**, y el coordinador no la siguió. No falta un control: falta **leer lo que el control devuelve**. Cuando una consulta devuelva una fe de erratas o un `-FE-` sobre el hecho que se está fichando, **es de lectura obligatoria antes de redactar** |
| ARGOS 105 | **El generador móvil: corregido, y la lección se repite** | El ancla de inyección de los SVG exigía el título **literal** `SEMÁFORO ARGOS`; esta edición lo matizó con un sufijo y la móvil salió **sin radar, sin mapa y con los `sem-item` en crudo**, en silencio salvo por la validación. Corregido para tolerar sufijos, y el validador ya no exige 3 SVG fijos —una edición sin aseguramientos lleva 2 legítimamente—. **Se corrigió la herramienta, no su salida**, y la corrección beneficia a todas las ediciones futuras |

## Seguimientos judiciales abiertos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 105 | **Nuevo León — Santa Catarina, 31 años 3 meses** | **Candidato de frontera, a un día de la ventana.** Francisco "N" y Pedro "N", homicidio calificado y tentativa por el ataque de **Rincón de Mitras**; publicado el **20-ago** (`mvsnoticias.com/nuevo-leon/2026/8/20/`). **Sin comunicado de la FGJNL localizado** | El boletín de la FGJNL, que **comunica por Facebook y X (`@FGJNL`), no por portal**. Mientras no exista: `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR` |
| ARGOS 101 | **Durango — Lerdo** (`ARG-101-SEN-001`) | **Pena exacta y firmeza: siguen sin obtenerse.** Continúa en «más de 26 años», **no sumable**. Duplicidad ya interceptada en ARGOS 104: un solo boletín bajo dos rutas, no dos condenas | Lectura directa o segunda fuente. ⚠️ **Va camino del mismo umbral que acaba de retirar el detalle de Durango/Gómez Palacio**: si llega a dos ediciones más sin respaldo, se retira |
| ARGOS 102 | **Coronango, Puebla** (`ARG-102-SEN-REC-001`) | ⚠️ **Contradicción abierta**: un medio publica **23 años** frente a **26 a 7 m 15 d**. `CONTRADICHA — reportar ambas`. Las **212 UMA siguen `SIN ANCLA DOCUMENTAL`** y **no se convierten a pesos** | Lectura directa del boletín de la FGE de Puebla. Ancla fechada ya obtenida: `intoleranciadiario.com/…/2026/08/11/` |
| ARGOS 99 | **SLP — Matlapa**, Elías "N" | Cuatro URL localizadas, **ninguna fechada**. Delito preciso: lesiones doblemente agravadas, hecho de ago-2024, procedimiento abreviado, 2 años 8 meses | El boletín de la FGE SLP. **El término jurídico está expreso; lo que falta es la fecha** |
| ARGOS 99 | **QRoo — Playa del Carmen**, 50 años (`ARG-103-SEG-001`) | Fechado el **12-ago**, fuera de toda ventana cubierta. Sin boletín de `fgeqroo.gob.mx` | **No integra. No reabrir salvo que aparezca fuente oficial** |
| ARGOS 99 | **Tabasco — Cunduacán**, Miguel "N" (`ARG-103-SEG-002`) | El boletín cubre Centro, Cárdenas y Cunduacán, pero **no devolvió su `id`** | ⚠️ **No gastar más búsquedas**: cuatro ediciones y once `id` demuestran que `/Boletin/Index/<id>` **no es resoluble por buscador** |
| ARGOS 102 | **Sonora — Nogales: 21 a 7 m 15 d a dos personas** | Reconfirmado con dos URLs fechadas en ruta (`eldiariodesonora.com.mx/…/2026/08/12/`, `telemax.com.mx/blog/2026/08/12/`): el hecho es del **12-ago** | **Confirmado fuera de toda ventana reciente.** Candidato de la ventana de ARGOS 96 |
| ARGOS 102 | **Sinaloa — 50 años a Wilberth "N" por secuestro agravado** | Verificado con `grep`: no figura en ninguna edición. Publicación **15-ago** con fecha en ruta | Boletín de la FGE de Sinaloa. `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR`. **Candidato a omisión de la serie 98/99** |
| ARGOS 96 | **Ruffo Appel / Ingemar**, huachicol fiscal (`ARG-98-SEG-001`) | Último movimiento: **Rigoberto Blanco Cantú se entregó en EU** (red Farías / Mefra Fletes), publicado el 20-ago con fecha en ruta | Sentencia de amparo de fondo. **No aporta línea a ningún conteo** |
| ARGOS 101 | **Guerrero — 5 sentencias** y **Guanajuato — 36 sentenciadas** | Sin avance. Agregados **sin desglose nominal**; el de Guanajuato es **anual** | El desglose caso por caso |

## Vacíos de publicación que siguen sin resolverse

| Desde | Caso | Estado |
|---|---|---|
| ARGOS 105 | **Tijuana — el número de víctimas de `ARG-105-REC-002`** | `CANTIDAD NO PUBLICADA`. La FGE de BC **no descartó más de una víctima** y no se localizó identificación forense posterior. **Contradicción de colonia abierta**: Hipódromo (titulares de dos regionales) frente a «20 de Noviembre» (resumen de buscador), `CONTRADICHA — no fundir`. Lo cierra un boletín de `fgebc.gob.mx` con **dos campos individualizadores** |
| ARGOS 105 | **Saltillo — la hora de `ARG-105-REC-001` y el término jurídico exacto** | La hora sigue en «por la tarde»; el rango 14:30-15:30 h **procede de un resumen y no se consigna**. El término oscila entre **«homicidio calificado»** y **«homicidio agravado»**, ambos atribuidos a la Fiscalía: `CONTRADICHA`. Lo cierra la lectura directa de `sitio.fgecoahuila.gob.mx/2026/08/05/` o `/2026/08/06/`, **ambos con fecha en la ruta** |
| ARGOS 105 | **Cuatro de los ocho hechos recuperados no tienen boletín institucional localizable** | Tijuana, Pesquería, Teotihuacán y el conjunto veracruzano descansan en fuentes periodísticas coincidentes, con la institucional acreditada **solo de forma indirecta**. Lo cierra la petición formal a **FGE Baja California, FGR Nuevo León, FGJEM y FGE Veracruz** |
| ARGOS 105 | **Tamaulipas — choque Ejército/civiles armados atribuido al 21-ago** | Único indicio con fecha potencialmente **dentro** de la ventana del corte. **Fuente abierta única** (Blog del Narco), sin municipio, sin cifras y sin corroboración. `NO OFICIAL — PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL`. No se integra ni se descarta |
| ARGOS 105 | **Pesquería, NL — el oleoducto retirado** | `ARG-105-REC-007` publicó el hecho **sin «1 oleoducto»**, porque la reconciliación `ARG-102-FE-004` —cuatro URLs con fecha en ruta— **no lo recoge**, mientras que la lectura heredada de ARGOS 98 sí. `CONTRADICHA — no se funden`. Lo cierra el comunicado de la **FGR** sobre el cateo del predio **Dulces Nombres** del 12-ago |
| ARGOS 105 | **Veracruz — el conteo de fuentes de `ARG-105-REC-003` y `-004`** | «Más de nueve» y «siete» fuentes regionales nacen en ARGOS 97 **sin nombrar una sola cabecera** y no han podido recontarse. Publicado como `CONTEO DE FUENTES NO VERIFICABLE`. **El hecho subyacente no depende de ello.** Lo cierra enumerar las cabeceras, si alguna edición vuelve sobre el caso |
| ARGOS 104 | **Occidente en el boletín federal del 19-ago** | Los renglones de **Romita (Gto.), Tlajomulco (Jal.) y Los Reyes de Salgado (Mich., 5 largas y 5 cargadores)** siguen sin integrarse: sin URL fechada que los ancle. `PENDIENTE DE ANCLA FECHADA` — lo cierra una consulta al boletín **por título sin restricción de dominio** |
| ARGOS 104 | **Veracruz — el bloque de hechos graves del agregador** | Cuerpo desmembrado en Coatzintla, cabeza humana en Poza Rica, normalista asesinada en Tuxpan. ⚠️ Fuente **sin fecha en ruta**, y el mismo bloque aparece casi idéntico en resultados de **junio de 2026**: riesgo alto de recirculación. **Si se fechara en ventana sería 🔴**. Séptima edición: `BLOQUEADO POR EGRESO` |
| ARGOS 102 | **Jiutepec, Morelos — ataque con dron y explosivos** | ⚠️ **Contaminado con un hecho de 2025**: el racimo es mayoritariamente de **agosto de 2025**. Las dos URLs de `diariodemorelos.com` **siguen sin fecha en ruta**. `PENDIENTE DE ANCLA FECHADA` **con advertencia de trampa de aniversario**. **No se declara 🔴** |
| ARGOS 102 | **`gabinetedeseguridad.gob.mx/resultados/` — obligatorio desde el 1-sep** | **Faltan nueve días.** Sigue **BLOQUEADO** al acceso directo, aunque la ruta `/contenido/<id>/` **sí devuelve resultados indexados** y publica sentencias de la FGR. **No es un dominio muerto, es un dominio ilegible por acceso directo** |
| ARGOS 102 | **Tijuana, col. Hipódromo** — cuatro cuerpos en cajuelas (`ARG-103-REC-002`) | Sigue `NO INTEGRABLE`: los cuerpos aparecieron en **puntos distintos a lo largo de ~8 horas**. ⚠️ **Dato nuevo de ARGOS 105**: la **misma firma reaparece en la misma zona el 3-ago** (`ARG-105-REC-002`), catorce días antes. **Deslindados en cinco campos, son hechos distintos** — pero el patrón de zona sí es común y es línea de explotación |
| ARGOS 101 | **Zinapécuaro** (`ARG-101-003`) | Sin avance. **Tres hechos con la misma firma** en el mismo municipio. Se mantiene 🟡 |
| ARGOS 102 | **Los Reyes, Michoacán** (`ARG-102-002`) | Sin avance. El aseguramiento de Los Reyes del boletín federal es **sin detenidos y sin abatidos**: **no es el hecho de los cinco abatidos** y no debe fusionarse |
| ARGOS 102 | **Alfajayucan, Hidalgo** (`ARG-102-005`) | Sin avance. Solo páginas-etiqueta sin fecha. `PENDIENTE DE ANCLA FECHADA` |
| ARGOS 104 | **Coahuila — brecha Rancherías, Hidalgo** · **Chiapas — Mapastepec** | Sin avance; ARGOS 105 no les gastó búsqueda. Ninguna de sus URLs lleva día. Ambos serían 🟡 si se fecharan |

## Contradicciones abiertas

| Desde | Caso | Detalle |
|---|---|---|
| ARGOS 105 | **Juchipila — cartuchos** | Una consulta devolvió **118 cartuchos** frente a los **60** publicados en `ARG-104-ARM-001`. Probablemente el mismo resumidor parafraseando con imprecisión. **No se tocó el archivo sin lectura directa que lo sostenga** |
| ARGOS 104 | **Chiapas: Sureste o Pacífico** | Se regionaliza como **Sureste** desde ARGOS 88; en `argos-2026-08-03/04.html` figuró como **Pacífico**. **Sureste es la lectura correcta.** *No se toca el archivo antiguo* |
| ARGOS 104 | **Puerto Madero, Chiapas** (`ARG-104-ARM-003`) | **Dos lecturas incompatibles de la misma fuente institucional**. Solo se integraron las **3 largas y los 4 detenidos**. `CONTRADICHA — NO INTEGRAR HASTA VALIDACIÓN` |
| ARGOS 104 | **Juchipila — personas liberadas** · **El fusil Barrett de La Angostura** | La primera, contradicción **dentro de la misma fuente** (titular dice una, boletín y *slug* dicen dos): se publicó **2** con la salvedad. El segundo, `NO DETERMINABLE` si está comprendido en las seis largas: se publica por separado, no se suma |
| ARGOS 103 | **Armamento especial vs. armas largas** (`ARG-103-ARM-001`) | La balanza se inclina a que **el armamento especial NO está comprendido** en las largas, pero es paráfrasis del resumidor. Confianza **Media**. El boletín federal da **dos armas cortas** frente a **una** de la ficha |
| ARGOS 99 | **Culiacán** (`ARG-99-001`) | Ubicación conciliada. **Hora: tres versiones —12:30, 13:00 y ~14:00—.** `CONTRADICHA — reportar las tres, no promediar`. **Sin detenidos: confirmado** |
| ARGOS 101 | **Mapimí, Durango** | Desglose **8 largas + 4 cortas = 12 armas**, con **87 cargadores y 4,715 cartuchos**, frente a los **65 cargadores** del boletín federal. **Contradicción de cargadores abierta** |
| ARGOS 100 | **Altamira, Tamaulipas** (`ARG-100-001`) | **Se propone cerrar como `2 o 3 — DISCREPANCIA NO RESUELTA`.** El "comunicado de la Primera Zona Naval del 15-ago" **sigue sin existir localizable** |
| ARGOS 103 | **Las 84 UMA de Tlaxcala** · **La cifra de bloqueos de Michoacán** (`ARG-103-001`) | Sin cambio en ninguna. La primera, `CONTRADICHA — REQUIERE LECTURA DIRECTA`; **no gastar búsquedas**: arbitrar entre dos paráfrasis del mismo resumidor no produce un dato mejor. La segunda, cuatro lecturas publicadas sin fundir |
| ARGOS 103 | **La reserva de color de `ARG-103-002`** | Sin cambio. Una fuente que sitúe la agresión a la GN en el punto de la captura obliga a fe de erratas |
| ARGOS 102 | **Chiapas — Cintalapa y Benemérito de las Américas** | Son casos **distintos** de los del archivo. La ficha de Cintalapa **sigue debiendo reescribirse o retirarse**. Los "37 cargadores de 30 cartuchos cada uno" son **capacidad declarada**: nunca convertir a 1,110 |
| ARGOS 101 | **Colima** (`ARG-101-002`) | Sin arbitrar: Infobae y Puente Libre no reportan detenidos, El Occidental reporta 1 mujer detenida |
| ARGOS 99 | **Indicador SESNSP: −48% frente a −60%** | Sin cambio. `HEREDADO — NO REVERIFICADO`. **Origen verificado**: entró en ARGOS 86 con respaldo citable real, así que **se conserva y no procede fe de erratas** |
| ARGOS 98 | **"Operación Sable", Mazatlán** (`ARG-97-ARM-003`) · **Privada Amberes, Ciudad Juárez** · **Azcapotzalco** · **Campeche — Hopelchén** | Sin avance en ninguno |

## Deuda editorial y de método heredada

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 98 | **Lista blanca de egreso** | `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**. **Cero portales leídos por acceso directo, decimosexta edición.** Sigue siendo **el único cambio que elevaría el techo del producto** por encima de ★★★★☆ |
| ARGOS 102 | **Mergear las ramas de edición a `main`** | ⚠️ **Avance en ARGOS 105**: la rama de ARGOS 104 se integró con `git merge --ff-only`, así que la 105 arranca sobre ella. **Siguen sin mergearse a `main` las ramas de ARGOS 88 a 105.** Nota operativa: **`barrido-regional`, `procedencia-cifras` y `editor-duplicidad` ya resuelven por nombre** — el rodeo por `general-purpose` que hicieron falta en ARGOS 104 ya no es necesario para los tres controles, aunque en ARGOS 105 los seis barridos regionales sí se lanzaron con el rodeo |
| ARGOS 100 | **Correcciones de ARGOS 99 a ARGOS 98 que siguen sin aplicarse** | **Octava edición sin ejecutarse.** Reintegrar Lázaro Cárdenas (`ARG-98-ARM-003`) al total de ARGOS 98; sustituir dos URL mal citadas en `argos-2026-08-15-fuentes.md`; incorporar tres hechos omitidos por ARGOS 98 (Chilpancingo/Los Ardillos 14-ago, Nopala Hidalgo 13-ago, excomandante por tortura en Cuautla); reintegrar el desglose de Sain Alto al total de ARGOS 99. Se suman las nueve recuperaciones `ARG-102-REC-*` y los 27 AEI de Escuinapa |
| ARGOS 104 | **Las portadas rectificadas no reflejan su conteo** | A las de ARGOS 95, 96, 99, 100 y 101 se suman ahora **ARGOS 88, 94 y 95** por las fes de erratas de ARGOS 105. Todas llevan su bloque de fe de erratas encima de la valoración, pero sus **portadas** siguen mostrando el conteo original, porque se generan desde el arreglo `EVENTOS` de cada edición. **Residuo conocido y acotado** |

## Cerrados recientemente

- **La deuda de registro — SALDADA.** Los cuatro hechos inventariados por ARGOS 104 y los dos
  incidentales que seguían sin ficha recibieron ARG-ID (`ARG-105-REC-003` a `-008`), y el séptimo
  —La Paz, BCS— **se declaró expresamente fuera de umbral** en vez de quedar en espera indefinida.
  *Cerrada la deuda que ARGOS 104 abrió como PRIORIDAD 1.*

- **La auditoría de las ventanas 88-93 — CERRADA**, y con un hallazgo estructural: además de dos
  hechos 🔴 nuevos (`ARG-105-REC-001` Saltillo y `ARG-105-REC-002` Tijuana), destapó que **la serie
  tiene un intervalo que ninguna edición cubre**. *Cerrada la auditoría; se abre en su lugar la deuda
  de método sobre los huecos de ventana.*

- **Jalisco — Tizapán el Alto, 19 sentenciados — CERRADO, y no como se esperaba.** No faltaba el
  comunicado de la FGR para integrarlo: **ya estaba publicado como `ARG-94-SEN-002`** desde
  ARGOS 94, con el desglose completo (12 a 18a 1m 22d y 7 a 16a 6m). El pendiente llevaba **tres
  ediciones vivo sobre una premisa falsa**. *Cerrado.*

- **La Paz, BCS — CERRADO como fuera de umbral.** Séptima edición sin fuente oficial; la regla
  asimétrica de sentencias no admite confianza Baja. `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR
  AL CONTEO NACIONAL`, y sale de la lista de pendientes activos.

- **Durango, Gómez Palacio (`ARG-104-SEN-001`) — RESUELTO por retirada.** Segunda edición con la pena
  exacta y los importes sin respaldo citable: la regla de las cifras arrastradas obliga a retirarlos.
  **La sentencia se conserva**, la pena queda en «más de 7 años» **no sumable**, y multa y reparación
  pasan a `CANTIDAD NO DETERMINADA` (`ARG-105-FE-005`). *Cerrado.*

- **El directorio de dominios — depurado.** Llevaba la fila corregida de Aguascalientes **prepuesta
  al título del archivo**, y filas obsoletas duplicadas de **Colima** y **Nayarit** conviviendo con
  las corregidas. Colima queda donde le corresponde, en Occidente. *Cerrado.*

- **El bug de anclaje del generador móvil — CERRADO, corregido en la herramienta.** Y con él la
  exigencia de 3 SVG fijos, que penalizaba a las ediciones sin aseguramientos.

- **Los pendientes cerrados en ARGOS 104** —la auditoría 95-98, la rectificación en bloque de 99-101,
  la deuda de cobertura de Colima, Aguascalientes y Nayarit, la variante de Veracruz, el falso vacío
  del boletín federal y el bug de `colspan`— *se retiran conforme a la convención de dos ediciones.*

---

## Cómo arrancar la edición siguiente

Sesión nueva, un solo mensaje:

> Haz el ARGOS 106 de hoy siguiendo `CLAUDE.md`. Rama `claude/argos-106-<sufijo>`. Lee
> `reports/_pendientes.md`, `docs/dominios-oficiales.md` y la edición anterior
> (`reports/argos-2026-08-23*`) para no duplicar hechos ni perder seguimientos. **Mergea las ramas
> antes de empezar**: comprueba si `claude/argos-105-us24r6` ya está en `main` y, si no, trae sus
> cambios con `git merge --ff-only`.
>
> **La ventana abre donde cerró ARGOS 105: 2026-08-23 08:00 CDMX.** Confirma la hora real de CDMX al
> arrancar y séllala en encabezado, pie y cada marca "Consulta:".
>
> ⚠️ **PRIMERO DE TODO, Y ANTES DE CUALQUIER OTRO ENCARGO: lanza los seis `barrido-regional`.**
> ARGOS 105 se quedó **sin presupuesto de búsqueda** (200/200 de la sesión) porque gastó la
> auditoría retroactiva antes que el barrido, y **cinco de las seis regiones no llegaron a lanzar una
> sola consulta**. No repitas ese orden. El agotamiento **no avisa**: una región que arranca tarde
> entrega un informe vacío indistinguible de "no hubo publicaciones".
>
> **Tienes que barrer DOS ventanas**: la propia de ARGOS 106 y la de **2026-08-21 07:55 → 2026-08-23
> 08:00**, que quedó `NO REVISADA` en **27 de 32 entidades** y en el emisor federal. **Prioridad
> sobre el ciclo**: esas entidades encabezan el triaje aunque no les toque por turno; el **Golfo**
> además debe ejecutar el triaje judicial que le correspondía por Ciclo B y no pudo hacer. El
> Ciclo C (Occidente + Sureste) se reanuda después.
>
> **Consulta el boletín federal en las tres formas** —día suelto, rango y **título sin restricción de
> dominio**— para el **21, 22 y 23 de agosto**: la regla de la triple consulta **no llegó a
> ejecutarse** en ARGOS 105.
>
> ⚠️ **REGLA EDITORIAL, POR ENCIMA DE TODO LO DEMÁS: el cartelón es un análisis para un mando, no un
> informe sobre ARGOS.** Nada de textos de auditoría, presupuesto de búsqueda, ciclos de rotación,
> `grep`, cobertura del instrumento ni acusaciones a ediciones anteriores. **Y nada de repetir el
> mismo hecho o la misma cifra en varias secciones**: cada hecho va en «Ejes del día» y en su ficha,
> y en ningún sitio más. Todo lo de método va al archivo de fuentes y a `_pendientes.md`.
>
> **Encargo nominal, de los primeros**: **Octavio Haro**, empresario reportado como desaparecido y
> **hallado muerto en Zapopan, Jalisco**. La autoridad apunta a un móvil «relacionado con su entorno
> personal». ARGOS 105 **no pudo corroborarlo y no publicó ficha** por no tener una sola URL que lo
> sostuviera. Busca: fecha del hallazgo **y** fecha del reporte de desaparición —son campos
> distintos—, municipio, y boletín de la **FGE de Jalisco** (`fiscalia.jalisco.gob.mx`, cuyos
> *slugs* llevan **fecha completa como sufijo**, así que un resultado de búsqueda ya fecha el
> boletín).
>
> **Deuda de método que no cuesta búsquedas, hazla mientras el barrido corre**: recorre las ventanas
> declaradas de toda la serie y **lista los intervalos que ninguna edición cubre**. ARGOS 105
> descubrió uno —el 4-ago por la tarde, entre el cierre de ARGOS 88 y la apertura de ARGOS 90, con
> la edición 89 inexistente— y no hay motivo para suponer que sea el único.
>
> Antes del commit, ejecuta los tres controles obligatorios (`barrido-regional` ×6,
> `procedencia-cifras` y `editor-duplicidad`) y actualiza `reports/_pendientes.md`.
>
> **No gastes búsquedas** en: el pendiente de Veracruz (`BLOQUEADO POR EGRESO`, séptima edición), las
> 84 UMA de Tlaxcala, el `id` del boletín de Cunduacán, ni Zacatecas 100 años (hecho de ago-2021,
> trampa de aniversario confirmada).

### Lo que funcionó en ARGOS 105 y conviene repetir

1. **Ejecutar primero lo que no cuesta búsquedas.** La deuda de registro se saldó íntegra con `grep`
   sobre el repositorio, sin gastar una sola consulta. Fue lo único que sobrevivió al agotamiento del
   presupuesto, y es lo que sostiene la edición.
2. **Verificar con `grep` toda acusación de omisión, sobre TODO el repositorio.** De los doce
   "vacíos" heredados, **tres no lo eran**, y **dos pendientes vivos descansaban sobre una premisa
   falsa**. Cuarta edición consecutiva en que este control salva al producto de acusar a una edición
   anterior de algo que sí hizo.
3. **Un equipo que reporta su propio fallo vale más que uno que entrega.** El Sureste detectó el
   agotamiento del presupuesto y lo reportó como hallazgo crítico **en vez de entregar un informe
   vacío**. Eso es lo que impidió que la edición declarara un falso `SIN DATO` nacional.
4. **La ronda de corroboración rinde por quinta vez consecutiva**, y esta vez su aportación decisiva
   fue **un deslinde**: dos hallazgos de restos humanos en la misma colonia de Tijuana, ambos en
   lunes, separados por catorce días, que se habrían fundido sin cotejar vehículo, punto y forma de
   presentación.
5. **Corregir la herramienta, no su salida.** El generador móvil falló en silencio por un ancla
   demasiado literal; se corrigió el generador y la corrección beneficia a todas las ediciones
   futuras.
6. **Declarar `NO REVISADA` y no `SIN ACTUALIZACIÓN`.** Es la diferencia entre una edición con un
   vacío honesto y una que publica un cero falso sobre 27 entidades.
