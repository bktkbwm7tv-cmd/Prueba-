# ORDEN DE ARRANQUE — ARGOS 113

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 112** (corte 2026-08-31).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git fetch origin                                   # traer el estado real
git log --oneline -1 origin/main                   # ¿main está al día?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6             # ¿cuál es la última edición del archivo?
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 113**: última edición `argos-2026-08-31` (ARGOS 112), **81
archivos** en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió:
pare y avísele al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló SEIS ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 112 mostraba **`argos-2026-08-24` (ARGOS 106)** como última
> edición —siete ediciones por detrás— y **no contenía su propio archivo de arranque**: numerar por
> lo que la rama tenía a la vista habría producido **un falso «ARGOS 107» con ventana solapada de una
> semana**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y
> resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Edición** | **ARGOS 113** |
| **Ventana** | **desde 2026-08-31 09:28 CDMX** (cierre de ARGOS 112) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-114.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape. **Verifique la hora, no la suponga.**

⚠️ **Efecto de calendario, comprobado en ARGOS 112 y probablemente relevante otra vez.** La ventana
de ARGOS 112 cubría **sábado, domingo y una sola mañana hábil**, y el resultado fue que **ninguna de
las 32 fiscalías publicó dentro del corte** y que el único portal que publicó fue federal. **No es
un fallo de método: las corporaciones publican en días hábiles.** Si la ventana vuelve a caer en fin
de semana, **decláre­lo en la valoración como advertencia de comparabilidad**, igual que hizo ARGOS 112.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-31-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.
   ⚠️ **NOVEDAD DE ARGOS 112: el `grep` debe hacerse también por TOPÓNIMO DE LOCALIDAD, no solo por
   entidad y municipio.** «Agua Verde» y «Palo Blanco» **ya estaban en el archivo** como localidades
   del mismo corredor del sur de Sinaloa (`ARG-102-REC-001`, `ARG-106-004`); **ni el barrido regional
   ni el recall del coordinador lo vieron — lo vio `editor-duplicidad`**. **Quinta edición
   consecutiva en que el archivo resuelve lo que la web no. No es formalidad.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 113 HEREDA

### 3.1 El método que funcionó y hay que conservar

**Reparto de presupuesto**: ~60-65 % consulta genérica sin `site:` · **~15 % `site:` dirigido** ·
~10 % judicial.

⚠️ **EL OBJETIVO DE `site:` SE BAJA DE 25 % A 15 %, Y ESTO ES UN CAMBIO DELIBERADO.** En ARGOS 112
**las seis regiones declararon desviación y cinco se desviaron en el mismo sentido: menos `site:` del
previsto**. **No es indisciplina.** Con el egreso bloqueado y el índice rezagado, el `site:` sobre
dominios oficiales devuelve *home pages*, agregados sin fecha o ruido, mientras **la consulta
genérica por fecha sí aísla la ventana**. **Seguir declarando seis desviaciones por edición contra un
objetivo que el entorno no permite no es disciplina: es ruido.**

| Origen del hecho | ARGOS 110 | ARGOS 111 | ARGOS 112 |
|---|---|---|---|
| Barridos regionales | 2 de 4 | 4 de 6 | 3 de 7 |
| **Recall nacional del coordinador** | 2 de 4 | 2 de 6 | **4 de 7, incluidos LOS DOS ROJOS** |

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO, Y EN ARGOS 112 APORTÓ EL
HECHO PRINCIPAL.** Trajo **Ojocaliente, Villa García, la detención** y **la serie de tres ataques que
los encadena** — y **ninguna región los trajo en primera entrega**.
**La razón es estructural y conviene tenerla presente: un hecho nacional de gran cobertura se busca
mejor por tema que por entidad, y los barridos están organizados por entidad.** El recall no es un
respaldo del barrido: **cubre un ángulo que el barrido no puede cubrir por construcción**.

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene tres preguntas, el
tope es **de tres en total, no de tres por pregunta**. Cerrar un seguimiento en `SIN AVANCE` **es el
resultado correcto cuando no hay dato**, no un fallo.

### 3.2 Cobertura — qué encabeza el triaje

**La deuda de dominio de las SSP y fiscalías está SALDADA.** Resueltos y cerrados en ARGOS 112:

| Entidad | Hallazgo |
|---|---|
| **San Luis Potosí** | ✅ **`seguridad.slp.gob.mx`** es el vivo, con **fecha en la ruta** (`/noticias/AAAA/M/D/slug`). `fiscaliaslp.gob.mx/vi/` vive pero con *slugs* **sin fecha**. `sitio.sanluis.gob.mx/SSPC/` **no confirmado** — no se declara inexistente |
| **Tlaxcala** | ✅ **CERRADO como vacío acreditado.** Ambos dominios resuelven; **ninguno publica boletines individuales fechados**, solo acumulados de periodo. **No lo vuelva a investigar** |
| **Fiscalía de Tabasco** | ✅ **CONSULTADA.** `fiscaliatabasco.gob.mx/Boletin/Index/…` vive, pero **sin fecha en la ruta ni en el titular** |
| **FGE Veracruz** | ✅ **CERRADO como vacío acreditado del emisor** tras cinco cortes de agregados. **La vía útil en Veracruz es la FGR, no la FGE** — de ahí salió la única sentencia de ARGOS 112 |

**Dominios reutilizables — no los redescubra**: Fiscalía de Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/`
(**fecha en la ruta, alto volumen**) · Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`
(**fecha en la ruta**) · Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa `fiscaliasinaloa.mx` ·
Chihuahua `fiscalia.chihuahua.gob.mx` y `sspe.chihuahua.gob.mx` (⚠️ `ssp.chihuahua.gob.mx` es FALSO) ·
Colima `fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` · Edomex `fgjem.edomex.gob.mx` ·
BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` · Coahuila `sspcoahuila.gob.mx` · Aguascalientes
`aguascalientes.gob.mx/ssp/` · Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/`.
**No publican indexable**: FGJ Nuevo León · SSP Zacatecas (sin fecha en la ruta) · Sonora
`fgjsonora.gob.mx` (tres ediciones sin resultado, ni confirmado ni descartado).

⚠️ **ANOMALÍA DE PORTAL — NAYARIT, persiste en otra forma.** La consulta genérica **ya no devuelve la
página de apuestas**, pero `site:ssypc.nayarit.gob.mx` devuelve **artículos de Wikipedia sobre
geografía de Nayarit** y una página «Archivo» vacía. **`PORTAL NO DISPONIBLE — índice sin boletines
localizables`, nunca `SIN ACTUALIZACIÓN`. Ninguna cifra suya se usa.** **El síntoma cambió; el
diagnóstico no.** No gaste más de una búsqueda.

⚠️ **LA DEUDA DE COBERTURA MÁS ANTIGUA VIVA, sexta edición consecutiva**: **SEDENA / SEMAR / FGR /
ANAM regionales** y las **Mesas de Construcción de la Paz**. Ninguna región llega nunca con
presupuesto. **Propuesta: asígnela explícitamente a una región por edición, en rotación, en vez de
dejarla al remanente — que nunca existe.**

### 3.3 El ciclo

ARGOS 112 aplicó el **Ciclo B (Noreste + Golfo)** y **rindió mucho**: el Golfo encabezando judicial
produjo **la única sentencia integrable del corte**, y lo hizo **rompiendo cinco cortes de agregados
inservibles de la FGE de Veracruz al ir a la delegación de la FGR**. El Noreste **cerró el candidato
de mayor volumen pendiente de la serie** y **arbitró el dominio de SLP**.

**Es la tercera vez consecutiva que la región a la que le toca encabezar judicial produce la única
sentencia del corte** (Noroeste/Durango en 101 y 111; Golfo/Veracruz en 112). **El mecanismo cambia
lo que el producto encuentra.**

**A ARGOS 113 le toca el Ciclo C — Occidente + Sureste** encabezando el triaje judicial; las otras
cuatro encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué
aportó.*
**Prioridad sobre el ciclo**: no queda ninguna entidad `NO REVISADA`, así que **el ciclo se aplica
limpio**.

### 3.4 Los seguimientos que más rinden

1. ⚠️ **ZACATECAS — hay una campaña de artefactos explosivos contra el Estado, no tres incidentes.**
   *Seguimiento de máxima prioridad.* **Tres ataques en seis días**: **27-ago** carretera federal 54,
   municipio de Tabasco (`ARG-110-001`); **29-ago** Villa García (`ARG-112-002`); **30-ago**
   Ojocaliente (`ARG-112-001`). **La progresión del blanco es la firma**: personal en patrullaje →
   patrulla en tránsito → **instalación fija de mando en la cabecera durante la feria**.
   **Qué buscar**: **peritaje comparado de los tres artefactos** (iniciador, carga, contenedor) y si
   se integró **carpeta única**. **Y si hubo un cuarto ataque** — es la pregunta que decide si la
   serie sigue viva. **Tres búsquedas máximo.**
2. ⚠️ **La iniciación remota de Villa García es la única pieza técnica publicada de toda la serie de
   AEI.** Contenedor (motocicleta) e iniciación (detonación remota), por declaración del **secretario
   de Seguridad Pública de Aguascalientes, Antonio Martínez Romo**. **Qué buscar**: si se publicó
   **explotación técnica del accionador** —radiofrecuencia o telefonía— y si el detenido fue
   vinculado a proceso. **Dos búsquedas.**
3. ⚠️ **CHIHUAHUA — Bocoyna. EL CANDIDATO PRIORITARIO.** Publicado el **31-ago**, `NO REVISADO A
   FONDO`, en municipio **colindante con Maguarichi** y misma sierra. **Puede ser continuación del
   mismo hallazgo o evento distinto.** **No se descartó por fecha, sino por falta de verificación.**
   **Dos búsquedas.**
4. ⚠️ **NACIONAL — la protección balística.** **`SIN AVANCE` probado en las SEIS regiones**: ninguna
   autoridad ha publicado **marca, nivel NIJ ni lote** de una sola de las **25 placas**. ⚠️ **El
   seguimiento cambió de naturaleza**: ya no es «falta un dato de unos casos», es **una omisión
   sistemática de campo**. **Lo accionable no es una búsqueda más, sino un cambio en lo que la
   autoridad consigna.** **Una búsqueda, o ninguna** — y si vuelve a salir vacío, **considere
   retirarlo de la lista de búsqueda y dejarlo solo como conclusión permanente**.
5. ⚠️ **La entrada de material de guerra es mayorista y viene del norte** — acreditado en dos hechos
   del mismo corte: **210 armas desde Texas** (Sabinas Hidalgo) y **6,324 piezas de explosivo, 1.1 t
   a granel y 5,234 detonadores** en camionetas robadas (**dos en EE. UU., una en Chihuahua**).
   **Qué buscar**: **calibres y modelos de las 210 armas** —sin ellos no hay cotejo con el armamento
   de los hechos violentos del noreste— y si prosperó el **rastreo internacional de series**.
   **Dos búsquedas.**
6. **ZACATECAS — la contradicción de lesionados de `ARG-110-001`** sigue abierta, ahora con las dos
   partes **nominadas**: el **fiscal Cristian Camacho Osnaya** dice **5**; el **Secretario de
   Gobierno**, **2**. `CONTRADICHA — NO SE ARBITRA SIN FUENTE DIRECTA`. **Una búsqueda.**
   ⚠️ **NO reabra la pregunta del lote ni el «antecedente del 1 de agosto»**: cerradas por mal
   planteamiento.
7. **Sinaloa — el municipio de Agua Verde y Palo Blanco** (`ARG-112-005`). **Una sola búsqueda**, y
   es de trazabilidad: **la autoridad no publicó el municipio**, y sin él no se cierra la
   `RESERVA DE TOPÓNIMO` contra `ARG-102-REC-001` (El Rosario) y `ARG-106-004` (Mazatlán).
8. **No gaste más de una búsqueda**: Ojocaliente (si hay detenidos o se acreditó la atribución al
   CJNG, que es **hipótesis de la autoridad, no hecho**), Loxicha (`ARG-109-002`, homónimo sin fecha
   fijable), Pedernales (`ARG-110-004`, falta el boletín de la FGE), Poza Rica (`ARG-108-005`),
   Chihuahua `ARG-111-004` (el dato que mueve el color).
9. **No gaste NINGUNA**: la disputa forestal Michoacán/Guerrero (**solicitud a SEMARNAT y al RAN**),
   «El Dron» (`ARG-109-004`), Piedras Negras, Querétaro (`ARG-109-005`), Tepechitlán, **Tabasco/
   Zacatecas** (cerrado: es de octubre de 2025), **Tlaxcala** y **FGE Veracruz** (vacíos acreditados),
   Petatlán y Totolapan (cerrados en `SIN DATO`).

### 3.5 ⚠️ OBLIGACIÓN DE CALENDARIO — **YA VENCIÓ**

**`gabinetedeseguridad.gob.mx/resultados/` es obligatorio desde el 1 de septiembre de 2026.**
**ARGOS 112 cerró el 31 de agosto y por un día no lo alcanzó. ARGOS 113 SÍ.**
**Su ausencia se declara como VACÍO, no como limitación heredada.**
Dato útil: **el dominio SÍ está parcialmente indexado** —una consulta de ARGOS 112 devolvió
`gabinetedeseguridad.gob.mx/contenido/6985`, de octubre de 2025—, así que **la vía de buscador existe
aunque el acceso directo siga bloqueado**. ⚠️ **Y ese mismo resultado es una trampa de año
documentada**: el boletín es de **21-oct-2025** y lo devolvió una consulta de agosto de 2026.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes
de ningún otro encargo**, con la deuda de la 3.2 al frente, el reparto de la 3.1 y **el tope duro de
2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  sin restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** En ARGOS 112 **aportó 4 de 7
  hechos, incluidos los dos rojos y la serie que los explica.** **Es el paso de mayor rendimiento del
  método y no es opcional.**
- **Declarar la desviación de presupuesto** si la hay — contra el **nuevo objetivo de 15 % en `site:`**.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| ⚠️ **RECTIFICACIÓN PARCIAL DE LA AUTORIDAD — modo de fallo NUEVO de ARGOS 112** | **El más importante de esta edición.** El borrador **aceptó la rectificación de la autoridad sobre el MECANISMO del artefacto de Ojocaliente y descartó como «aislada» la rectificación del SALDO**, que era del fiscal general y posterior. **Regla: cuando acepte una rectificación de la autoridad en un campo de un hecho, revise si hay rectificaciones posteriores en los demás campos del mismo hecho.** Una autoridad que corrige el mecanismo suele corregir también el saldo |
| ⚠️ **Ni obedecer ni descartar por precaución: ARBITRAR** | El arranque anterior avisaba de que **un control que dice «no integrar» merece arbitraje**. ARGOS 112 encontró **el reverso**: **un control puede obligar a INTEGRAR lo que el borrador descartó por precaución.** **Son la misma regla en las dos direcciones** |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | **«Agua Verde» y «Palo Blanco» ya estaban en el archivo** en el mismo corredor de Sinaloa. **Ni el barrido ni el recall lo vieron.** **`grep` del topónimo de localidad, no solo de municipio, antes de fichar** |
| ⚠️ **Suma incompleta** | Cuando un hecho tenga **dos o más intervenciones**, verifique que **TODOS los rubros se sumen**. En ARGOS 112 se manejó bien declarando **«suelos, no totales»** para los rubros que solo cubrían 2 de 4 intervenciones |
| ⚠️ **El resumidor no siempre se equivoca** | ARGOS 111 desconfió de una fecha suya («octubre de 2025») y **el resumidor tenía razón**. **La regla se sostiene** —una fecha sin fragmento citable no fija nada— **pero merece una búsqueda de arbitraje antes de descartarla como disparate** |
| ⚠️ **Trampa de año en el propio dominio oficial** | `gabinetedeseguridad.gob.mx/contenido/6985` («aseguran armas en Edomex, 10 detenidos») es de **21-oct-2025** y lo devolvió una consulta de agosto de 2026 |
| ⚠️ **Origen de vehículos robados: verifique CADA uno** | Las tres camionetas de Maguarichi **no** eran todas de EE. UU.: **dos (Arizona y Texas) y una de Chihuahua**. El borrador lo generalizó **en tres lugares, incluida una conclusión** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado cinco ediciones. En ARGOS 112 confirmó «domingo 30» y explicó el vacío institucional: **la ventana era sábado, domingo y una mañana hábil** |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y **no basta como fuente única** |
| **Capacidad declarada** | «cargadores de 20 cartuchos cada uno» **no** se convierte en cartuchos |
| **Cifra no exacta** | «más de 200 armas y cartuchos» **no es cifra** y no se redondea. **Pero busque la exacta** |
| ⚠️ **El AEI empleado no es AEI asegurado** | Los de Ojocaliente y Villa García **fueron usados contra la autoridad**: van al semáforo, **no al conteo de armamento**. Los 6 de Palo Blanco sí eran aseguramiento |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. **Pero si la suma la publica la fuente, es de ella** |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. Igual varios medios regionales con **redacción casi idéntica** — pasó otra vez con los «3 muertos» de Pedernales, ya con **siete** portales |
| **Topónimo repetido** | «Tabasco» es estado **y municipio de Zacatecas»; «Agua Verde», «Palo Blanco», «El Arenal» y «Emiliano Zapata» reaparecen bajo entidades distintas |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria** |

**Egreso bloqueado, vigesimocuarta edición.** `curl` devuelve `CONNECT tunnel failed, response 403`;
`WebFetch` devuelve `EGRESS_BLOCKED`. **Cero portales por acceso directo.** Techo de confianza:
**★★★★☆**. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar. **Verifíquelo en la sesión, no
lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige
lectura directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las tres casillas deben CUADRAR con las 32 entidades**: en ARGOS 112 sumaban 30 y lo detectó
`editor-duplicidad`. **Una casilla que no cuadra con el universo es una cobertura no demostrable.**

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales**.
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID
  `-FE-` **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 112 cumplió**: seis
  `-FE-` registrados, ninguno en el cartelón.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha**
  con enlace `#ARG-ID` y aporta **campos distintos**.
- ⚠️ **La regla de no duplicación alcanza también a los PÁRRAFOS.** En ARGOS 112 `editor-duplicidad`
  detectó que **la nota del semáforo y la Valoración reescribían casi literalmente** la misma
  descripción. **La Valoración debe remitir y limitarse a aplicar la metodología de riesgo**, no
  repetir la narración.
- **Toda cifra en cero lleva al lado el dato que la explica.** Tarjetas de armamento con **doble
  cifra rotulada** y **leyenda encima del bloque**; la línea inferior es **cálculo propio** y se
  declara. **ARGOS 112 usó tres recuadros**: por qué el amarillo está en cero; **cero placas
  balísticas en un corte de 228 armas largas**; y **32 fiscalías con cero sentencias**, con la causa
  de calendario a la vista. **Ese es el modelo.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura van al archivo de fuentes.
  **No mida en «ediciones» dentro del cartelón**: mida en fechas.
- **Conclusiones de inteligencia criminal**, no de método. **ARGOS 112 publicó ocho**, todas
  accionables.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.** Use `<div class="alerta contexto">…`.
- **Los `id` de las fichas** solo deben tener forma de ARG-ID si son un ARG-ID real.
- ⚠️ **Cada sentencia integrada lleva ficha propia con sus apartados** —hecho procesal, pena y
  estatus, corroboración, explotación—, no solo un renglón de tabla.

### Estructura de páginas que hereda ARGOS 113

**Seis páginas**, como salió ARGOS 112: portada · crimen organizado (I), alto impacto · crimen
organizado (II), acciones institucionales · armamento · sentencias · valoración y conclusiones.
Si el volumen lo pide, **se reparte entre más páginas: nunca se comprime una tarjeta**.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en las SEIS páginas.
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 113 <FECHA> 112 2026-08-31 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

⚠️ **DEFECTO DE ENSAMBLADO QUE ARGOS 112 COMETIÓ Y LA VALIDACIÓN ATRAPÓ — NO LO REPITA.**
Al recortar el bloque de datos para sustituirlo, **el corte se hizo en `EVENTOS_ARM` y dejó fuera
`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL` y `GRIS`**, que
viven **entre `EVENTOS_ARM` y `SIZE_R`**. **El cartelón habría cargado con el radar y el mapa rotos, y
la vista no lo detecta.** **El bloque que se sustituye va de `CORTE_FECHA` a `EVENTOS_ARM`; el que se
conserva empieza en `REGION_ORDER`.**

**Comprobación de coherencia obligatoria** —cuesta un comando—: extraer el bloque de datos del
`<script>` **hasta `const SIZE_R`**, hacer `node --check`, y validar que **cada `estado:` existe en
`MEXICO_PATHS`**, que **cada `region:` coincide con `STATE_REGION`**, que **ninguna fecha cae fuera de
la ventana**, que **no hay ARG-ID duplicados** y que **el semáforo derivado de `EVENTOS` coincide con
los contadores tecleados en la portada**. Un `region:` mal puesto **coloca el eco del radar en el
sector equivocado y nadie lo nota**.

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en
ambas versiones · toda tabla envuelta **exactamente una vez** en el escritorio · **cero `-FE-` en
ambas** · cero `sem-item` fuera de portada · cero tarjetas `.reg` sin texto · cero restos de clases de
escritorio en la móvil (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) · sin desbordamiento
horizontal a 390 px.

*Nota*: la móvil **no lleva `<script>`** y **`table-wrap` aparece en cero** al contarlo — el generador
los renombra a `tabla-scroll`. **No es un defecto.** En ARGOS 112: **6 secciones, 13 `tabla-scroll`,
3 `<table>`, 7 tarjetas** frente a 7 del escritorio.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide | Rendimiento en ARGOS 112 |
|---|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo | **`CORREGIR ANTES DE PUBLICAR`**: **detectó la colisión de topónimo Agua Verde/Palo Blanco que ni el barrido ni el recall vieron**, la **repetición de párrafo** entre portada y valoración, y unas **casillas de cobertura que sumaban 30 de 32** |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón | **`CORREGIR ANTES DE PUBLICAR` con cuatro correcciones y dos reservas**: la **rectificación parcial del saldo de Ojocaliente** (la más grave, y era de criterio), el **origen de las camionetas de Maguarichi**, el **boletín federal del 27 y no del 26**, la **edad contradicha del detenido**, y **dos reservas que reforzaron una ficha** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido | 32 de 32 entidades |

**Séptima edición consecutiva con hallazgos reales de los dos controles.** Si el destinatario no
autoriza subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la ausencia en el
indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una
búsqueda de arbitraje antes de obedecerlo** —en ARGOS 111 aceptar por precaución habría dejado fuera
el hecho de mayor valor del corte—. Y **un control puede obligar a INTEGRAR lo que el borrador
descartó por precaución** —ARGOS 112, la cifra de lesionados de Ojocaliente—. **Ni obedecer ni
descartar por precaución: arbitrar.**

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al
   cartelón pero sí al índice.
3. **Escribir `reports/_arranque-ARGOS-114.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
