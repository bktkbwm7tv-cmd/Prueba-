# ORDEN DE ARRANQUE — ARGOS 109

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 108** (corte 2026-08-26).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git fetch origin                                   # traer el estado real
git log --oneline -1 origin/main                   # ¿main está al día?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6             # ¿cuál es la última edición del archivo?
```

**Estado que debe encontrar ARGOS 109**: última edición `argos-2026-08-26` (ARGOS 108), **69
archivos** en `reports/`, y `main` conteniéndola —ARGOS 108 se mergeó a `main` al cierre—.
**Si `main` está por detrás de eso, algo se rompió: pare y avísele al destinatario antes de escribir
una línea.**

> ⚠️ **Esto ya falló dos ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 108 estaba **5 commits por detrás de `main`**, mostraba
> `argos-2026-08-24` como última edición y **no contenía su propio archivo de arranque**: numerar por
> lo que la rama tenía a la vista habría producido un falso ARGOS 108 con ventana solapada.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y
> conservarlos.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 109** |
| **Ventana** | **desde 2026-08-26 14:21 CDMX** (cierre de ARGOS 108) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-110.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape. ARGOS 108 cerró **vespertino** (14:21), no matutino: la ventana siguiente puede ser larga.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-26-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio por entidad y municipio antes de fichar
   cualquier hecho como nuevo**, y **leer lo que devuelva**. En ARGOS 108 ese `grep` interceptó un
   **doble conteo real de 7 armas largas y 18 cargadores**. No es formalidad.

---

## BLOQUE 3 — DEUDA QUE ARGOS 109 HEREDA

### 3.1 ⚠️ El hallazgo de método más importante de ARGOS 108

**Cinco de los ocho hechos del corte los aportó el recall nacional del coordinador, no los seis
barridos regionales.** Chilpancingo y Acapulco no los vio Sureste; Tepechitlán y Juchipila no los vio
Noreste. **Y las regiones no se equivocaron**: declararon `SIN RESULTADO INDEXADO EN VENTANA` y era
cierto —ninguna autoridad publicó boletín sobre esos cuatro hechos—.

La conclusión es estructural: **con los portales institucionales bloqueados, un barrido organizado
por dominio no ve los hechos que solo publican los medios.** Consecuencias para ARGOS 109:

- **Suba la fracción de presupuesto que cada región gasta en consulta genérica por entidad**
  («ataque armado \<entidad\> \<fecha\>», «enfrentamiento \<entidad\> \<fecha\>») y baje la de
  `site:`, que devuelve boletines viejos con alta tasa de descarte.
- **El recall nacional del coordinador es obligatorio y va ANTES de cerrar ningún barrido.**
  Dos ediciones consecutivas ha sido la vía principal, no el complemento.

### 3.2 Cobertura — por portal, y encabezan el triaje

Por la regla de prioridad sobre el ciclo, estos **encabezan**:

- **Fiscalías `NO REVISADA`**: **Jalisco, Aguascalientes y Nuevo León** (las 29 restantes sí).
- **SSP y policías estatales**: Chihuahua, BC, BCS, Durango, Coahuila, Tamaulipas, SLP, Puebla,
  Tlaxcala, Nayarit, Tabasco.
- **Mesas de Construcción de la Paz**: Noreste, Sureste y Occidente.
- **SEDENA, SEMAR, FGR y ANAM regionales**: sin revisar como portal propio en casi ninguna región.

**Hallazgos de dominio reutilizables — no los redescubra:**

| Entidad | Dominio |
|---|---|
| Tlaxcala | ✅ `fgjtlaxcala.gob.mx` (anticorrupción: `fecc.fgjtlaxcala.gob.mx`) |
| Nayarit (fiscalía) | ✅ `fiscaliageneral.nayarit.gob.mx` |
| Aguascalientes (SSP) | ✅ `aguascalientes.gob.mx/ssp/` · IESPA en `/IESPA/` |
| Colima | ✅ `fgecolima.mx` — **no** `fiscalia.colima.gob.mx` |
| Chihuahua | ✅ `fiscalia.chihuahua.gob.mx` — **`fgechihuahua.gob.mx` no resuelve** |
| Querétaro | ✅ `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` — **fecha en la ruta, el mejor formato de la serie** |
| Michoacán (fiscalía) | ⚠️ indicio sin confirmar: `fiscaliamichoacan.gob.mx`, no `fge.michoacan.gob.mx` |
| Nayarit (SSP) | ⚠️ sin confirmar — probar `ssp.nayarit.gob.mx` y `sspc.nayarit.gob.mx` |
| Guanajuato | ⚠️ sin confirmar — sigue por el agregador `boletines.guanajuato.gob.mx` |
| Sonora / Sinaloa (fiscalías) | ⚠️ no devuelven contenido propio vía `site:`; existe `fiscaliasinaloa.mx` |

### 3.3 El ciclo

ARGOS 108 aplicó el **Ciclo A** (Noroeste + Centro) y **rindió ofensivamente**: Centro localizó las
**dos únicas sentencias estatales del corte** —FGE Querétaro fue el **único portal institucional de
las 32 entidades que publicó dentro de la ventana**— y cerró el dominio de Tlaxcala; Occidente cerró
el de Nayarit. **A ARGOS 109 le toca el Ciclo B — Noreste + Golfo** encabezando el triaje judicial;
las otras cuatro encabezan con armamento.

*Se declara expresamente en el archivo de fuentes, junto con qué aportó la rotación.* Una edición que
no diga qué ciclo aplicó, no aplicó ninguno.

### 3.4 Los seguimientos que más rinden

1. **Zacatecas — corredor Juchipila–Tlaltenango–Tepechitlán** (`ARG-108-006`, `ARG-108-002`).
   *Es el seguimiento de mayor prioridad del próximo corte.* **Dos mandos de seguridad municipal del
   mismo corredor detenidos por secuestro agravado en seis meses** —Tlaltenango el 4-feb, Juchipila el
   25-ago—. Pregunta operativa única: **¿la orden de aprehensión de Juchipila deriva de los cateos
   del 21-ago (`ARG-104-001`), que dejaron 10 detenidos y 2 personas liberadas?** Lo cierra el número
   de causa penal. Añada: identidad y plaza de origen de los cuatro abatidos de Tepechitlán y qué
   armamento se les recogió, que la autoridad **no publicó**.
2. **Poza Rica — el cotejo balístico** (`ARG-108-005`). El caso de Elí Martínez ya cerró —localizado
   con vida—, pero **el patrón queda vivo y ahora con base documental firme**: tres agresiones a
   reporteros de la fuente policiaca en 2026, **dos sobre la misma avenida**, las tres con medidas de
   la CEAPP, **cero detenidos en las tres carpetas**. La línea que decide es el **cotejo balístico
   cruzado, que no consta realizado**.
3. **Guerrero — las dos plazas a la vez** (`ARG-108-001`, `ARG-108-003`). Dos ataques contra
   población civil desarmada en vía pública, con un día de diferencia, en Chilpancingo y Acapulco.
   No los lea por evento: pida el **inventario de puntos fijos de economía informal** de ambas
   ciudades como mapa de blancos de extorsión.
4. **Candados sueltos**: identidad de los dos abatidos de Candela (`ARG-108-FE-001`); si Víctor
   Manuel Amado de León conservaba medidas de protección (`ARG-108-REC-001`); quién inició en San
   Andrés Tuxtla (`ARG-108-004`, **una fuente que lo fije obliga a fe de erratas del color**).
5. **Morelia** (`ARG-106-REC-002`) — **novena edición sin moverse.** El estancamiento sigue siendo el
   dato. La GN no se ha pronunciado sobre la adscripción. No gaste más de una búsqueda.

### 3.5 Candidatos vivos que ARGOS 109 debe cerrar

- **Morelos · Cuautla** — extorsión agravada, 16a 8m (Luis Ángel «N», FIDAI). URL de `24morelos.com`
  **sin fecha en la ruta**; el «25-ago» es del resumidor. Ni integrado ni descartado.
- **SSC CDMX** — comunicado 946 (cargadores para arma larga y 400 cartuchos, Gustavo A. Madero).
  URL sin fecha en la ruta. Ni integrado ni descartado.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes
de ningún otro encargo**, con la lista de portales de la sección 3.2 al frente de cada región y con
la instrucción de la 3.1 sobre el reparto de presupuesto.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  sin restricción de dominio antes de cerrarla.
- **Recall nacional del coordinador**, *además* del de cada región y **antes de cerrar los barridos**.
  En ARGOS 107 produjo dos de tres hechos recuperados; **en ARGOS 108, cinco de ocho hechos del corte**.
- **Declarar la desviación de presupuesto** si la hay. El agente de Golfo gastó 23 de 20 en ARGOS 108
  y lo dijo; se acepta declarado, nunca disimulado.

Si el destinatario **no** autoriza subagentes, haga barrido dirigido a mano y **declare la cobertura
real**: `NO REVISADA` para lo no consultado, jamás `SIN ACTUALIZACIÓN`.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| **Trampa de aniversario** | ⚠️ **ARGOS 108 atrapó una cara**: las cifras «3 largas, 7 cargadores, 90 cartuchos, **7 explosivos**» que circulan asociadas a **Tepechitlán** son de un hecho del **17-feb-2026** —otra comunidad, otra corporación agredida (FRIZ, no GN), **4 detenidos y no 4 abatidos**—. **El boletín de la SSP de Zacatecas que las contiene no lleva fecha en su ruta.** Ninguna cifra entra sin año en la ruta |
| **Trampa de mes** | Verificar `/2026/8/` frente a `/2026/1/` en la ruta |
| ⚠️ **Duplicidad por republicación** | **La trampa más cara de ARGOS 108.** Un medio nacional republica el 25-ago un aseguramiento **del 19-ago que ya estaba publicado** (`ARG-104-ARM-008`, Ciudad Victoria: 7 largas, 18 cargadores). El resumidor de un segundo medio sí daba la fecha correcta y el barrido lo marcó `CONTRADICHA`. **Lo resolvió el `grep` al índice, no la búsqueda.** Ante fecha contradicha entre 5-10 días atrás: **buscar primero en el índice, no en la web** |
| ⚠️ **El resumidor inventa boletines federales enteros** | Tercera vez. Afirma «acciones relevantes del **24 de agosto**» con desglose por entidad, pero **`site:gob.mx/sspc/prensa` lista hasta el 21-23 y salta**. **Si el boletín no devuelve URL propia, no existe para ARGOS**, por detallado que sea el resumen |
| **Capacidad declarada** | «42 cargadores **de 20 cartuchos cada uno**» **no** son 840 cartuchos. Nunca convertir |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y no basta como fuente única |
| ⚠️ **Agregado de jornada frente a hecho puntual** | En Acapulco los titulares nacionales pluralizan («ataques al transporte público») y publican **2 muertos y 3 heridos** donde el hecho puntual tiene **1 y 1**. Fiche lo que sostiene la fuente puntual y declare ambas |
| **Evolución de saldo ≠ contradicción** | Chilpancingo pasó de «1 muerto» a «3 muertos» por **defunciones hospitalarias**. No arbitre: diga que el saldo evolucionó |
| **El *slug* institucional** | Prueba el término jurídico, **no identifica el caso**. Hacen falta ≥2 campos individualizadores. ⚠️ **Jiquilpan, Michoacán, reaparece** con el mismo patrón que hizo caer a ARGOS 107 |
| ⚠️ **Homonimia de organización** | **«Pueblo Unido» (Tabasco, escisión de La Barredora) y «Pueblos Unidos» (Hidalgo/Michoacán) son organizaciones distintas.** El resumidor ya las mezcló al cubrir la captura del «Koki» |
| **Cifras propias sin fuente** | ⚠️ `procedencia-cifras` retiró en ARGOS 108 **tres distancias geográficas estimadas por el redactor** («60 km», «más de 700 km»). Son cifras inferidas y están prohibidas: la afirmación cualitativa sostiene igual el análisis |
| **Un `grep` sin leer** | Si una consulta devuelve una fe de erratas o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria antes de redactar** |

**Egreso bloqueado, vigésima edición.** `*.gob.mx`, `gabinetedeseguridad.gob.mx`, `fgr.org.mx` y los
dominios de medios están bloqueados; `curl` devuelve `CONNECT tunnel failed, response 403` y el proxy
lo reporta como **denegación de política**. **Cero portales por acceso directo.** Techo de confianza:
**★★★★☆**; ninguna ficha lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
**Verifíquelo en la sesión, no lo herede**: basta un `curl` por dominio.

⚠️ **`gabinetedeseguridad.gob.mx/resultados/` es obligatorio desde el 1 de septiembre.** Si el corte
de ARGOS 109 cae en septiembre, **ya es exigible** y su ausencia debe declararse como tal.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales**.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha**,
  no repite sus cifras.
- **Toda cifra en cero lleva al lado el dato que la explica.** Las tarjetas de armamento van con
  **doble cifra rotulada** —arriba, lo asegurado en hechos de la ventana; abajo, lo publicado durante
  el corte procedente de hechos anteriores— y **leyenda encima del bloque** que las distingue. La
  línea inferior es **cálculo propio de ARGOS** y se declara, con sus salvedades **escritas en el
  cartelón**. Regla general: *cuando una cifra correcta pueda leerse como un error, el defecto es del
  producto*.
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura del instrumento van al
  archivo de fuentes y a `_pendientes.md`. Las excepciones de trazabilidad, **en una línea**.
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
#    Si no hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm".
#    ⚠️ Actualizar el <title> del <head>: se hereda de la edición anterior y es fácil olvidarlo.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 109 <FECHA> 108 2026-08-26 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

**Corregido en ARGOS 108**: `gen-movil.py` envolvía dos veces las tablas que ya traían `table-wrap`
—`<div class="tabla-scroll">` anidados, cuatro en la móvil de ARGOS 107—, y dos contenedores
desplazables anidados atrapan el gesto táctil. Se arregló con un *lookbehind* en la red de seguridad.
**No lo reintroduzca**.

**Comprobar antes de publicar**: mismo número de ítems por lista en ambas versiones · mismo número de
iconos · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio (`sem-item`,
`stat-tile`, `cover-visuals`, `masthead`) · toda tabla envuelta exactamente una vez · sin
desbordamiento horizontal a 390 px.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide | Rendimiento en ARGOS 108 |
|---|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo | **Interceptó un doble conteo real**: 7 armas largas y 18 cargadores de Ciudad Victoria, ya publicados como `ARG-104-ARM-008` |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón | **Retiró tres cifras inferidas por el redactor** (distancias geográficas sin fuente) |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido | 32 de 32 entidades |

Si el destinatario no autoriza subagentes para los dos primeros, **ejecútelos a mano con el mismo
criterio** —así se hizo en ARGOS 106, 107 y 108, y **los tres produjeron hallazgos reales**— y
**declare** la ausencia en el indicador de cobertura, no la disimule.

Cuando un control devuelva `CORREGIR ANTES DE PUBLICAR`, se corrige y se vuelve a pasar. Si se decide
no corregir, la razón se deja escrita en el archivo de fuentes.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md`.
3. **Escribir `reports/_arranque-ARGOS-110.md`** y borrar este archivo.
4. Commit descriptivo, push a la rama de la edición, y **merge a `main`** para que la rama por
   defecto no vuelva a quedarse atrás.

---

## TEXTO PARA PEGAR EN EL CHAT NUEVO

> Genera el ARGOS de hoy. Antes de numerar la edición, lee `reports/_arranque-ARGOS-109.md` y
> ejecuta su Bloque 0: la numeración sale del archivo, no de lo que veas en la rama local, y el
> `git merge --ff-only origin/main` va antes de leer nada más. Después lee `CLAUDE.md`,
> `reports/_pendientes.md` y `reports/argos-2026-08-26-fuentes.md`.
>
> La ventana abre donde cerró ARGOS 108 (2026-08-26 14:21 CDMX) y cierra a la hora real de arranque,
> verificada con `TZ=America/Mexico_City date`.
>
> Prioridades: **el corredor Juchipila–Tlaltenango–Tepechitlán en Zacatecas** —dos mandos de
> seguridad municipal detenidos por secuestro agravado en seis meses, y la pregunta de si la orden de
> Juchipila deriva de los cateos del 21-ago—; saldar las tres fiscalías `NO REVISADA` (Jalisco,
> Aguascalientes, Nuevo León) y los portales de SSP pendientes; y aplicar y declarar el
> **Ciclo B (Noreste + Golfo)**.
>
> Atiende el hallazgo de método del Bloque 3.1: **cinco de los ocho hechos de ARGOS 108 los aportó el
> recall nacional, no los barridos regionales**. Sube la fracción de presupuesto en consulta genérica
> por entidad y ejecuta el recall nacional antes de cerrar ningún barrido.
>
> Respeta el Bloque 6: sin resumen ejecutivo; ningún hecho con ficha propia se repite en una tabla
> resumen; y toda cifra en cero lleva al lado el dato que la explica —las tarjetas de armamento van
> con doble cifra rotulada—.
>
> Genera cartelón **y** versión móvil —esta última con `tools/gen-movil.py`, nunca a mano—,
> actualiza `_pendientes.md` e `indice-arg-id.md`, escribe el arranque de ARGOS 110, y al cerrar
> mergea a `main`.
>
> Autorizo subagentes para los seis barridos regionales.
