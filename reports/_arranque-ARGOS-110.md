# ORDEN DE ARRANQUE — ARGOS 110

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 109** (corte 2026-08-27).

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

**Estado que debe encontrar ARGOS 110**: última edición `argos-2026-08-27` (ARGOS 109), **72
archivos** en `reports/`, y `main` conteniéndola —ARGOS 109 se mergeó a `main` al cierre—.
**Si `main` está por detrás de eso, algo se rompió: pare y avísele al destinatario antes de escribir
una línea.**

> ⚠️ **Esto ya falló TRES ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 109 estaba **5 commits por detrás de `main`**, mostraba
> `argos-2026-08-24` como última edición y **no contenía su propio archivo de arranque**: numerar por
> lo que la rama tenía a la vista habría producido un **falso ARGOS 107 con ventana solapada**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y
> conservarlos. **El patrón lleva tres ediciones sin fallar ni una vez en favor del producto.**

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 110** |
| **Ventana** | **desde 2026-08-27 10:00 CDMX** (cierre de ARGOS 109) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-111.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape. ARGOS 109 cerró **matutino** (10:00): si ARGOS 110 arranca por la tarde, la ventana será
corta; si arranca al día siguiente, larga. **Verifique la hora, no la suponga.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-27-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio por entidad y municipio antes de fichar
   cualquier hecho como nuevo**, y **leer lo que devuelva**. En ARGOS 109 ese `grep` interceptó
   **un doble conteo real de 15 armas largas, 94 cargadores y 2,964 cartuchos** (El Roble, Mazatlán,
   ya publicado como `ARG-92-002` el 9 de agosto). Segunda edición consecutiva en que lo resuelve el
   archivo y no la web. **No es formalidad.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 110 HEREDA

### 3.1 El método que funcionó y hay que conservar

ARGOS 108 descubrió que **un barrido organizado por `site:` ya no ve la mayoría de los hechos**, con
los portales bloqueados. ARGOS 109 aplicó la corrección —subir la fracción de consulta genérica— y
**el resultado se invirtió**:

| Origen del hecho | ARGOS 108 | **ARGOS 109** |
|---|---|---|
| Barridos regionales | 3 de 8 | **4 de 6** |
| Recall nacional del coordinador | **5 de 8** | 2 de 6 |

**Conserve el reparto**: ~60-65 % consulta genérica sin `site:` · ~25 % `site:` dirigido para el
desglose numérico oficial · ~10 % judicial. Las cuatro regiones que aportaron hecho en ARGOS 109
**lo hicieron por consulta genérica**, no por dominio.

**Y conserve el recall nacional aunque las regiones rindan.** En ARGOS 109 aportó 2 hechos y, sobre
todo, **interceptó cuatro falsos positivos** que ninguna región vio porque no eran suyos.
**Va antes de cerrar ningún barrido.**

### 3.2 Cobertura — qué encabeza el triaje

Por la regla de prioridad sobre el ciclo, **estos encabezan**:

- ⚠️ **LOS ONCE PORTALES DE SSP ESTATAL. Es la deuda más antigua del producto, abierta desde
  ARGOS 107, y ARGOS 109 NO la saldó**: Chihuahua, Baja California, BCS, Durango, Coahuila,
  Tamaulipas, San Luis Potosí, Puebla, Tlaxcala, Nayarit y Tabasco. **Ninguno se ha consultado como
  portal propio en tres ediciones.** Dos regiones concentran la mayoría: Noroeste (4) y Noreste (3).
- **Tlaxcala**, con cobertura declarada débil en ARGOS 109 —equivalente a `NO REVISADA` en la
  práctica—: `fgjtlaxcala.gob.mx` y SSP Tlaxcala, con `site:` dirigido.
- **Mesas de Construcción de la Paz** y **SEDENA / SEMAR / FGR / ANAM regionales**: sin revisar como
  portal propio en casi ninguna región, tres ediciones seguidas.

**Las fiscalías están saldadas**: 32 de 32 consultadas en ARGOS 109, incluidas Jalisco,
Aguascalientes y Nuevo León.

**Hallazgos de dominio reutilizables — no los redescubra:**

| Entidad | Dominio |
|---|---|
| **SSP de Nayarit** | ✅ **`ssypc.nayarit.gob.mx`** — ⚠️ **`ssp.` y `sspc.nayarit.gob.mx` son FALSOS**, eran las hipótesis heredadas |
| **Fiscalía de Michoacán** | ✅ `fiscaliamichoacan.gob.mx` (+ `comunicacion.`, `juridico.`, `directorio.`) — **no** `fge.michoacan.gob.mx` |
| **Fiscalía de Sinaloa** | ✅ **`fiscaliasinaloa.mx`** — **no** `fiscaliasinaloa.gob.mx` |
| Querétaro | ✅ `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` — **fecha en la ruta, el mejor formato de la serie. Consúltelo de primero, no de último** |
| Chihuahua | ✅ `fiscalia.chihuahua.gob.mx` — `fgechihuahua.gob.mx` no resuelve |
| Tlaxcala | ✅ `fgjtlaxcala.gob.mx` (anticorrupción: `fecc.fgjtlaxcala.gob.mx`) |
| Nayarit (fiscalía) | ✅ `fiscaliageneral.nayarit.gob.mx` |
| Aguascalientes (SSP) | ✅ `aguascalientes.gob.mx/ssp/` · IESPA en `/IESPA/` |
| Colima | ✅ `fgecolima.mx` — **no** `fiscalia.colima.gob.mx` |
| Guanajuato | ⚠️ sin confirmar — sigue por el agregador `boletines.guanajuato.gob.mx` |
| Sonora | ⚠️ sin confirmar — `fgjsonora.gob.mx` no probado en ARGOS 109 |
| **SSP de Zacatecas** | ⚠️ existe, pero **sus boletines NO llevan fecha en la ruta**. Ninguna cifra suya entra sin ancla externa |
| **FGJ Nuevo León** | ⚠️ **no devuelve boletín indexable en portal**, consultado en tres formas. Su canal parece ser la red social. **No gaste `site:` ahí otra vez** |

### 3.3 El ciclo

ARGOS 109 aplicó el **Ciclo B** (Noreste + Golfo) y **rindió defensivamente**: no produjo sentencia
integrable, pero **Golfo resolvió la reserva de `ARG-108-004` con fuente institucional** —lo que
sostuvo el color ya publicado y corrigió los detenidos de 5 a 6— y **descartó dos trampas de fecha**;
Noreste acreditó que FGJ Nuevo León no publica en portal.

**A ARGOS 110 le toca el Ciclo C — Occidente + Sureste** encabezando el triaje judicial; las otras
cuatro encabezan con armamento. **Salvo que la deuda de SSP mande otra cosa**: la prioridad sobre el
ciclo vence al turno, y los once portales de SSP están repartidos sobre todo en Noroeste y Noreste.

*Se declara expresamente en el archivo de fuentes, junto con qué aportó la rotación.* Una edición que
no diga qué ciclo aplicó, no aplicó ninguno.

### 3.4 Los seguimientos que más rinden

1. **Puebla/Sinaloa — la red que alojaba a «El Dron»** (`ARG-109-004`). *Es el seguimiento de mayor
   prioridad del próximo corte.* Un tirador del homicidio de Culiacán del 4-ago, refugiado en
   San Bernardino Tlaxcalancingo con **tres sujetos armados dispuestos a enfrentar a agentes
   federales**. **La estructura que lo alojaba es el objetivo, no el detenido.** Pregunta que decide:
   **¿las tres armas viajaron con él o se las dieron en destino?** El cotejo por número de serie
   contra carpetas de Sinaloa y de Puebla distingue **red de traslado** de **red de acogida**, y eso
   cambia dónde se busca al **segundo tirador, que sigue prófugo**. Pida además contrato de
   arrendamiento y titular del servicio eléctrico del inmueble.
2. **Tamaulipas — el rancho de Altamira** (`ARG-109-006`). **Una sola persona detenida para cinco
   inmuebles y ocho unidades.** Los **135 ejemplares de fauna exótica** son el rastro documental:
   exigen gasto veterinario y alimentario sostenido, y las **especies CITES implican importación,
   punto aduanal y documento**. **El cruce con ANAM y con proveedores de forraje llega antes al
   propietario real del predio que cualquier diligencia sobre el combustible.**
3. **Michoacán — el revólver .32 de Tacámbaro** (`ARG-109-001`). Arsenal heterogéneo de
   aprovisionamiento local. **El revólver .32 es el arma con más probabilidad de tener propietario
   registrado**: es la vía de trazabilidad más barata. Añada el **registro de permisos de
   aprovechamiento forestal** del corredor Opopeo–Santa Clara, por el tractocamión maderero incendiado.
4. **Oaxaca — Loxicha: ¿criminal o agrario?** (`ARG-109-002`). Emboscada preparada con conocimiento
   previo del itinerario, contra un automóvil familiar, con una niña de 4 años entre los muertos.
   **Deslindar si pertenece a la serie de conflictos agrarios de la Sierra Sur o a disputa criminal**:
   la respuesta institucional que corresponde es distinta.
5. **Baja California — el canal del aviso de Mexicali** (`ARG-109-003`). **Qué órgano mexicano
   recibió el aviso y cuándo.** Y vigile el **efecto diversivo**: 450 elementos en el casco
   institucional descubren el resto de la ciudad.
6. **Zacatecas — corredor Juchipila–Tlaltenango–Tepechitlán**. **Reformulado, no cerrado**: el
   vínculo acreditado entre los dos mandos municipales caídos **no es una carpeta, sino el Plan
   SAGAZ**, activo desde finales de junio. **El interlocutor es la coordinación SAGAZ**, no la
   carpeta del cateo del 21-ago. La identidad de los cuatro abatidos de Tepechitlán sigue abierta;
   **el armamento que se les recogió NO lo publicó la autoridad** —vacío acreditado, no gaste más—.
7. **No gaste más de una búsqueda**: Morelia (`ARG-106-REC-002`), décima edición sin moverse.

### 3.5 Candidatos vivos que ARGOS 110 debe cerrar

- **Chiapas · Cintalapa de Figueroa** — agresión contra la FRIP, Ejército y GN: 1 abatido, 1 detenido
  con arma larga. La nota dice **«a media tarde del jueves»** y el jueves era el 27-ago, **posterior
  al cierre de la ventana de ARGOS 109**. URL solo ancla `/2026/08/`. **Lo cierra una URL con día en
  la ruta**; si resulta del 26-ago por la tarde, entra en ARGOS 110 con marca de frontera.
- **Guanajuato · «ocho homicidios en cinco horas»** — `paginanueve.com` sin fecha en ruta;
  `redmetropolitana.com.mx/2026/08/26/` sí la ancla **pero con cifras distintas** (7 hombres y 2
  mujeres). `CONTRADICHA`.
- **Veracruz · Jalapilla, Rafael Delgado** — ataque a comerciante desde tres motocicletas, 1 herido.
  Fuente sin fecha en ruta ni titular.
- **Baja California · Tijuana, Zona Centro** — 3 detenidos por homicidio, 2 armas sin desglose.
  `FRONTERA DE VENTANA — FECHA NO FIJADA`.
- **Sinaloa · bar de Concordia** — presunto lanzamiento de artefactos explosivos en un
  establecimiento. Solo apareció como fragmento embebido, **sin URL propia**. Búsqueda dedicada.
- **Coahuila · Piedras Negras** — sentencia por tráfico de personas, 9a7m6d. `PENDIENTE DE ANCLA FECHADA`.

**Retirados definitivamente, no los reabra**: Cuautla, Morelos (umbral de fe de erratas por dos
ediciones sin ancla, con agravante de pena estándar repetida) y SSC CDMX comunicado 946 (descartado
por esquema de URL).

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes
de ningún otro encargo**, con la deuda de portal de la sección 3.2 al frente de cada región y con la
instrucción de la 3.1 sobre el reparto de presupuesto.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  sin restricción de dominio antes de cerrarla.
- **Recall nacional del coordinador**, *además* del de cada región y **antes de cerrar los barridos**.
- **Declarar la desviación de presupuesto** si la hay. En ARGOS 109 tres regiones se pasaron
  —Noreste 25, Centro 23, Golfo 21— y **las tres lo declararon**. Se acepta declarado, nunca disimulado.

Si el destinatario **no** autoriza subagentes, haga barrido dirigido a mano y **declare la cobertura
real**: `NO REVISADA` para lo no consultado, jamás `SIN ACTUALIZACIÓN`.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| ⚠️ **La hora, no solo la fecha** | **Cara en ARGOS 109**: Armería, Colima ocurrió a las **12:52 del 26-ago** — mismo día de apertura, **antes** de las 14:21. Cuando la fuente publica hora, **compárela con la apertura de la ventana**, no solo el día |
| ⚠️ **Día de la semana contra calendario** | **Descartó Cintalapa en ARGOS 109**: la nota decía «jueves» y el jueves de esa semana caía **después** del cierre. Si una nota nombra el día de la semana, **verifíquelo**; cuesta cero y ya salvó dos ediciones (103 y 109) |
| ⚠️ **Trampa de aniversario** | **Doble cara en ARGOS 109**: «5 abatidos y 2 detenidos en Luis Moya» son de **2024**, y el hecho de agosto en Luis Moya es del **31-jul** (los 5 abatidos son de **Calera**, 1-ago). Ninguna cifra entra sin año verificable en la ruta |
| **Trampa de mes** | **Cara en ARGOS 109**: Tula de Allende, «3 abatidos y 1 oficial herido», es del **21-feb** (`/2026/2/21/`). Verificar `/2026/8/` frente a `/2026/2/` |
| ⚠️ **Desglose idéntico a otro evento del archivo** | **Cara en ARGOS 109**: «8 largas, 4 cortas» en Durango capital es **idéntico** al de Mapimí del 15-ago, y el propio artículo se contradecía. Si un desglose coincide exactamente con uno ya publicado, **desconfíe antes de buscar** |
| ⚠️ **Vinculación a proceso presentada como aseguramiento nuevo** | **Cara en ARGOS 109**: «26 vinculados en Mazatlán, 15 fusiles, 2,744 cartuchos» es la **vinculación** de un aseguramiento **ya contado en `ARG-92-002`** (8-ago). Vinculación a proceso **no es sentencia** y el armamento **no se recuenta**. Lo resolvió el `grep`, no la web |
| ⚠️ **Duplicidad por ubicación alternativa** | **Cara en ARGOS 109**: un barrido trajo el ataque a un taxi en **Cumbres de Llano Largo, Acapulco** como «hecho distinto», y era **la ubicación alternativa que ARGOS 108 ya había declarado como contradicción** de `ARG-108-003`, con el mismo saldo. **Antes de fichar un hecho «parecido pero en otra colonia», lea la contradicción declarada de la edición anterior** |
| ⚠️ **Número de comunicado sin fecha en la ruta** | **Regla nueva de ARGOS 109.** Los emisores **reutilizan la numeración entre años y cambian el esquema de URL**: el «946» de SSC CDMX existe en dos versiones distintas, de años distintos y sobre delitos distintos. **Verifique el formato vigente del emisor en el año del corte** antes de aceptar el candidato |
| ⚠️ **La pena no individualiza en delitos con abreviado** | **Regla nueva de ARGOS 109.** Al menos **tres sentencias por extorsión agravada en Cuautla y Jiutepec comparten la pena exacta de 16a8m**: es la **firma del procedimiento abreviado**, cuya reducción está tarifada. **La pena exacta deja de contar entre los ≥2 campos individualizadores** que exige la regla del *slug* |
| ⚠️ **El resumidor inventa boletines federales enteros** | **Cuarta vez.** En ARGOS 109 afirmó contenido del «26 de agosto» sin devolver URL. El más reciente con URL propia es el del **25-ago**. **Si el boletín no devuelve URL propia, no existe para ARGOS**, por detallado que sea el resumen. **Consulte en las tres formas**: día suelto, rango, y título sin `site:` |
| **Capacidad declarada** | «42 cargadores **de 20 cartuchos cada uno**» **no** son 840 cartuchos. Nunca convertir |
| **Cifra no exacta** | «Más de veinte cartuchos» **no es cifra** y nunca se redondea. Retiró el candidato de Tijuana en ARGOS 109 |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y no basta como fuente única |
| **Evolución de saldo ≠ contradicción** | En Tacámbaro pasó de «1 herido y 1 detenido» a «3 detenidos, 2 heridos, agentes ilesos» al confirmar la SSP. **Se ficha la versión institucional y se declara la primera.** No se promedian |
| ⚠️ **Distancias geográficas estimadas por el redactor** | **Reincidencia: `procedencia-cifras` las retiró en ARGOS 108 y volvió a retirarlas en ARGOS 109** («más de mil kilómetros»). **Son cifras inferidas y están prohibidas**: la afirmación cualitativa sostiene igual el análisis |
| **Sumas propias sin declarar** | Todo total nacional que ARGOS calcule a partir de cifras publicadas evento por evento es **cálculo propio** y **se declara en el cartelón** |
| **Un `grep` sin leer** | Si una consulta devuelve una fe de erratas o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria antes de redactar** |

**Egreso bloqueado, vigesimoprimera edición.** `*.gob.mx`, `gabinetedeseguridad.gob.mx`, `fgr.org.mx`
y los dominios de medios están bloqueados; `curl` devuelve `CONNECT tunnel failed, response 403` y el
proxy lo reporta como **denegación de política**. **Cero portales por acceso directo.** Techo de
confianza: **★★★★☆**; ninguna ficha lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin
tramitar. **Verifíquelo en la sesión, no lo herede**: basta un `curl` por dominio.

⚠️ **`gabinetedeseguridad.gob.mx/resultados/` es obligatorio desde el 1 de septiembre: quedan CINCO
DÍAS.** Si el corte de ARGOS 110 cae en septiembre, **ya es exigible** y su ausencia debe declararse
como vacío, no como limitación heredada.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales**.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha**
  —con enlace `#ARG-ID`, como en ARGOS 109—, no repite sus cifras.
- **Toda cifra en cero lleva al lado el dato que la explica.** Las tarjetas de armamento van con
  **doble cifra rotulada** —arriba, lo asegurado en hechos de la ventana; abajo, lo publicado durante
  el corte procedente de hechos anteriores— y **leyenda encima del bloque** que las distingue. La
  línea inferior es **cálculo propio de ARGOS** y se declara. Regla general: *cuando una cifra
  correcta pueda leerse como un error, el defecto es del producto*. **ARGOS 109 tuvo que añadir un
  recuadro explicando por qué cortas y largas sumaban 2 habiendo 9 armas aseguradas**: siete no
  llevaban clasificación publicada. **Ese recuadro es el modelo a seguir.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura del instrumento van al
  archivo de fuentes y a `_pendientes.md`. **No mida en «ediciones» dentro del cartelón**: mida en
  fechas. Las excepciones de trazabilidad, **en una línea**.
- **Conclusiones de inteligencia criminal**, no de método: patrones territoriales, perfil de víctima,
  modus operandi, capacidad de fuego, brecha detención-condena, líneas a explotar.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`. Una
  `<table>` suelta desborda la móvil **en silencio**.
- **Nada de `sem-item` fuera de la portada.** Para el «Nivel de Riesgo Nacional» de la última página
  use `<div class="alerta contexto"><span class="flag">NIVEL: …</span><p>…</p></div>`.
- **Los `id` de las fichas** solo deben tener forma de ARG-ID si son un ARG-ID real: el generador
  móvil recoge `<div class="nota" id="…">` como anclas enlazables.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    Radar, mapa y semáforo se derivan de esos arreglos: nunca teclear los contadores a mano.
#    El campo `region:` de cada evento debe coincidir con STATE_REGION (Zacatecas es NORESTE).
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm".
#    ⚠️ Si SÍ los hay, hay que RESTITUIR ese div: ARGOS 108 lo había quitado y ARGOS 109 tuvo
#    que volver a ponerlo. Compruébelo siempre contra el contenido real del corte.
#    ⚠️ Actualizar el <title> del <head>: se hereda y es fácil olvidarlo.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 110 <FECHA> 109 2026-08-27 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

⚠️ **Defecto de plantilla corregido en ARGOS 109 — no lo reintroduzca**: la edición 108 traía **dos
etiquetas `<body>` consecutivas**. Si copia una edición como base, **compruebe que hay exactamente
una**.

**Corregido en ARGOS 108 y vigente**: `gen-movil.py` envolvía dos veces las tablas que ya traían
`table-wrap`. Se arregló con un *lookbehind*. **No lo reintroduzca.**

**Comprobar antes de publicar**: mismo número de ítems por lista en ambas versiones · mismo número de
iconos · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio (`sem-item`,
`stat-tile`, `cover-visuals`, `masthead`) · toda tabla envuelta exactamente una vez · sin
desbordamiento horizontal a 390 px · **sintaxis del script validada con `node --check`**.

*Nota*: la móvil **no lleva `<script>`** —el generador hornea los contadores—, así que `node --check`
solo aplica al escritorio. Y una tabla de más de cuatro columnas **se reflúa a tarjetas** en la
móvil: es diseño del generador, no pérdida de datos.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide | Rendimiento en ARGOS 109 |
|---|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo | **Interceptó el hecho de Cumbres de Llano Largo**, que iba a publicarse como nuevo siendo la ubicación alternativa ya declarada como contradicción de `ARG-108-003` |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón | **Retiró dos distancias geográficas inferidas** por el redactor —reincidencia del defecto de ARGOS 108— y **obligó a declarar dos sumas propias** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido | 32 de 32 entidades |

Si el destinatario no autoriza subagentes para los dos primeros, **ejecútelos a mano con el mismo
criterio** —así se hizo en ARGOS 106, 107, 108 y 109, y **los cuatro produjeron hallazgos reales**— y
**declare** la ausencia en el indicador de cobertura, no la disimule.

Cuando un control devuelva `CORREGIR ANTES DE PUBLICAR`, se corrige y se vuelve a pasar. Si se decide
no corregir, la razón se deja escrita en el archivo de fuentes.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md`.
3. **Escribir `reports/_arranque-ARGOS-111.md`** y borrar este archivo.
4. Commit descriptivo, push a la rama de la edición, y **merge a `main`** para que la rama por
   defecto no vuelva a quedarse atrás.

---

## TEXTO PARA PEGAR EN EL CHAT NUEVO

> Genera el ARGOS de hoy. Antes de numerar la edición, lee `reports/_arranque-ARGOS-110.md` y
> ejecuta su Bloque 0: la numeración sale del archivo, no de lo que veas en la rama local, y el
> `git merge --ff-only origin/main` va antes de leer nada más. Después lee `CLAUDE.md`,
> `reports/_pendientes.md` y `reports/argos-2026-08-27-fuentes.md`.
>
> La ventana abre donde cerró ARGOS 109 (2026-08-27 10:00 CDMX) y cierra a la hora real de arranque,
> verificada con `TZ=America/Mexico_City date`.
>
> Prioridades: **la red que alojaba a «El Dron» en San Bernardino Tlaxcalancingo** —si las tres armas
> viajaron con él o se las dieron en destino, que distingue red de traslado de red de acogida, con el
> segundo tirador aún prófugo—; **el rancho de Altamira**, por la vía patrimonial de la fauna exótica
> y el cruce con ANAM; **saldar los once portales de SSP estatal**, que es la deuda más antigua del
> producto y lleva tres ediciones sin tocarse; y aplicar y declarar el **Ciclo C (Occidente + Sureste)**,
> salvo que la deuda de SSP mande otra cosa.
>
> Conserva el reparto de presupuesto que funcionó: ~60-65 % consulta genérica sin `site:`, y el
> recall nacional del coordinador **antes** de cerrar ningún barrido.
>
> Respeta el Bloque 6: sin resumen ejecutivo; ningún hecho con ficha propia se repite en una tabla
> resumen; y toda cifra en cero lleva al lado el dato que la explica —las tarjetas de armamento van
> con doble cifra rotulada—.
>
> Genera cartelón **y** versión móvil —esta última con `tools/gen-movil.py`, nunca a mano—,
> actualiza `_pendientes.md` e `indice-arg-id.md`, escribe el arranque de ARGOS 111, y al cerrar
> mergea a `main`.
>
> Autorizo subagentes para los seis barridos regionales.
