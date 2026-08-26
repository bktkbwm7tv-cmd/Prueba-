# ORDEN DE ARRANQUE — ARGOS 108

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 107** (corte 2026-08-25).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git log --oneline -1 origin/main                   # ¿main está al día?
ls reports/ | grep '^argos-' | tail -6             # ¿cuál es la última edición del archivo?
git ls-remote --heads origin | grep argos          # ¿hay ramas por delante de main?
```

**Estado que debe encontrar ARGOS 108**: última edición `argos-2026-08-25` (ARGOS 107), **66
archivos** en `reports/`, y `main` conteniéndola —ARGOS 107 se mergeó a `main` al cierre—.
**Si `main` está por detrás de eso, algo se rompió: pare y avísele al destinatario antes de escribir
una línea.**

**Lección de ARGOS 107, que costó un paso real**: la rama de trabajo **puede estar divergida de
`main`** —llevar commits propios y a la vez faltarle el commit del arranque—. `git merge origin/main`
**antes de leer nada más**. Sin ese paso la sesión no ve su propia orden de arranque.

**Nota de rama**: si la sesión trae una rama asignada por el entorno, **se trabaja en esa** y no se
empuja a otra; el merge a `main` al cierre es lo que importa, y está autorizado por el destinatario
desde ARGOS 106.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 108** |
| **Ventana** | **desde 2026-08-25 09:26 CDMX** (cierre de ARGOS 107) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-109.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-25-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio por entidad y municipio antes de fichar
   cualquier hecho como nuevo**, y **leer lo que devuelva**: en ARGOS 107 una coincidencia que
   parecía ruido mejoró una conclusión del cartelón.

---

## BLOQUE 3 — DEUDA QUE ARGOS 108 HEREDA

### 3.1 Cobertura — por portal, no por entidad

ARGOS 107 dejó **32 de 32 entidades consultadas** y saldó la deuda de ARGOS 106. Lo que queda
abierto es **más fino**: dentro de varias entidades quedaron portales sin ver, declarados
`NO REVISADA`. Por la regla de prioridad sobre el ciclo, **encabezan el triaje**:

- **SSP y policías estatales**: las 6 del Sureste, 5 del Noroeste, 4 del Occidente.
- **Mesas de Construcción de la Paz**: las 5 del Noreste y las 6 del Sureste.
- **SEDENA, SEMAR, FGR y ANAM regionales**: no revisados como portal propio en casi ninguna región.
- **FGJ CDMX, Fiscalía Morelos, FGE Tlaxcala, SSP Hidalgo, SSPMQ Querétaro**.

**Hallazgo reutilizable, no lo redescubra**: el dominio real de la fiscalía de **Colima** es
`fgecolima.mx`, no `fiscalia.colima.gob.mx`. Siguen **sin confirmar** los dominios oficiales de las
fiscalías de **Tlaxcala, Nayarit y Guanajuato** (para Guanajuato se usó el agregador
`boletines.guanajuato.gob.mx`, sustitución declarada).

### 3.2 El ciclo

ARGOS 107 aplicó el **Ciclo C** (Occidente + Sureste), que era el que ARGOS 106 debía y se saltó.
Descargada esa deuda, **el ciclo se reanuda: a ARGOS 108 le toca el Ciclo A — Noroeste + Centro**
encabezando el triaje judicial; las otras cuatro regiones encabezan con armamento.

*Se declara expresamente en el archivo de fuentes, junto con qué aportó la rotación.* Una edición
que no diga qué ciclo aplicó, no aplicó ninguno.

**Expectativa calibrada**: en ARGOS 107 el Ciclo C **no** produjo sentencia integrable. Su
rendimiento fue defensivo —evitó dos falsos positivos, uno de ellos dentro de ventana—. Eso también
es rendimiento y así debe registrarse; no se infle ni se descarte la rotación por un corte.

### 3.3 Los seguimientos que más rinden

1. **Poza Rica** (`ARG-107-001`) — **localización de Elí Martínez**, periodista sustraído tras un
   ataque a balazos el 24-ago. **Es la línea más perecedera del archivo**: la sustracción con vida
   deja una ventana de rescate que un homicidio no deja. Además, cruce de las **tres carpetas de
   agresiones a reporteros de la fuente policiaca en Poza Rica en 2026** —enero y junio fueron
   homicidios—. *Es el seguimiento de mayor prioridad del próximo corte.*
2. **Morelia** (`ARG-106-REC-002`) — **sigue sin moverse**, y ese estancamiento es el dato: ocho
   días sin definición de fuero en un homicidio con presunta participación de personal federal.
   Estado verificado: fuero común (FGE Michoacán); la FGR podría atraerlo si la GN confirma la
   adscripción, **y la GN no se ha pronunciado**. Ninguna fuente menciona fuero militar.
3. **Acapulco** (`ARG-106-REC-001`) — ⚠️ **el pendiente estaba mal planteado.** El «agresor herido
   en el tórax» puede ser una **conflación**: el único herido de tórax localizable es una **víctima**
   de otro ataque, el del taller de El Quemado. **Acredite primero de qué fuente salió el dato**
   antes de gastar una búsqueda más en el rastreo hospitalario.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **En ARGOS 107 se lanzaron y el
resultado fue 32 de 32 entidades frente a 5 de 32 en ARGOS 106.** Lánzelos **en un solo mensaje,
antes de ningún otro encargo**, con la lista de portales de la sección 3.1 al frente de cada región.

**Dos controles que ARGOS 107 confirmó y hay que repetir:**

- **Control de recall por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  genérica sin restricción de dominio antes de cerrarla.
- **Recall nacional del coordinador**, *además* del de cada región. Las regiones agotan presupuesto;
  el coordinador no. En ARGOS 107 produjo **dos de los tres hechos recuperados**.

Si el destinatario **no** autoriza subagentes, haga barrido dirigido a mano y **declare la cobertura
real**: `NO REVISADA` para lo no consultado, jamás `SIN ACTUALIZACIÓN`.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte. En ARGOS 107 el resumidor puso una detención «el 28 de agosto» |
| **Trampa de aniversario** | ARGOS 107 atrapó **dos**: el enfrentamiento de Hidalgo, Coahuila (**oct-2025**) y un boletín del Gabinete «del 22, 23 y 24 de agosto **de 2025**». **Ninguna cifra entra sin año en la ruta** |
| **Trampa de mes** | Nueva y cara: «Operativo Muralla, 9 detenidos y 9 armas largas en NL» parecía del corte y es del **27 de enero** (`mvsnoticias.com/…/2026/1/27/`). Habría metido 9 armas largas falsas en el conteo |
| **Capacidad declarada** | «42 cargadores **de 20 cartuchos cada uno**» **no** son 840 cartuchos. Nunca convertir |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y no basta como fuente única |
| **Día de la semana** | Contrastar contra calendario. En ARGOS 107 confirmó que el hecho de Culiacán pertenecía a la ventana anterior |
| **El título de la URL institucional** | ⚠️ **Lo más importante que aprendió ARGOS 107.** Una nota del Poder Judicial respaldaba en apariencia una sentencia de **Jiquilpan** y su título hablaba de **Morelia y Uruapan**. El *slug* institucional **prueba el término jurídico, no identifica el caso**. Es el fallo de Coronango otra vez |
| **Portal de ID correlativo** | Un boletín ya fechado acota a todos los de numeración inferior. Aplicable a Tabasco, Chiapas, Oaxaca, BC y al Poder Judicial de Michoacán |
| **El resumidor etiqueta mal los boletines** | Afirmó dos veces «acciones relevantes del 24 de agosto» con el desglose del boletín 21-23. **Ninguna URL nueva lo sostenía** |
| **Un `grep` sin leer** | Si una consulta devuelve una fe de erratas o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria antes de redactar** |

**Egreso bloqueado, decimonovena edición.** `*.gob.mx`, `gabinetedeseguridad.gob.mx`, `fgr.org.mx`
y los dominios de medios están bloqueados; `WebFetch` devuelve `EGRESS_BLOCKED` explícito.
**Cero portales por acceso directo.** Techo de confianza del producto: **★★★★☆**. Ninguna ficha
lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar y es el único cambio que
elevaría ese techo. **Verifíquelo en la sesión, no lo herede**: basta un `curl` por dominio.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales**.
- **Sin «Ejes del día».** Cada hecho aparece **una sola vez**, en su ficha. Las tablas de módulo
  aportan campos distintos —cifras, corporación, pena—, no repiten el titular.
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura del instrumento van al
  archivo de fuentes y a `_pendientes.md`. Las excepciones de trazabilidad, **en una línea**.
- **Conclusiones de inteligencia criminal**, no de método: patrones territoriales, perfil de víctima,
  modus operandi, capacidad de fuego, brecha detención-condena, líneas a explotar.
- **Iconografía de armamento** en tarjetas y cabeceras, con etiqueta y cifra. **Las categorías en
  cero se muestran atenuadas: la ausencia es dato.** ARGOS 107 publicó las nueve en cero, y es
  información, no hueco.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`. Una
  `<table>` suelta desborda la móvil **en silencio**.
- **Nada de `sem-item` fuera de la portada.** El generador solo convierte el semáforo de la portada;
  para el «Nivel de Riesgo Nacional» de la última página use
  `<div class="alerta contexto"><span class="flag">NIVEL: …</span><p>…</p></div>`. Un `sem-item`
  suelto hace fallar la validación de la móvil — le pasó a ARGOS 107.

### Las tres correcciones que el destinatario pidió sobre ARGOS 107

Detectadas al revisar la edición **en teléfono**, ya entregada. **No las repita.**

1. **Sin resumen ejecutivo.** El párrafo de apertura del tablero repetía los hechos que ya
   desarrollan sus fichas, sin aportar fuente, confianza ni análisis. **Se retiró la sección
   completa** y la página pasó a titularse por lo único que contenía. Si una página solo tiene una
   tabla, titúlela por la tabla.
2. **Ningún hecho con ficha propia entra además en una tabla resumen.** El megaoperativo del CJNG
   estaba en la tabla de la pág. 2 **y** con ficha completa en la pág. 4. La tabla debe **remitir a
   la ficha**, no repetir sus cifras.
3. ⚠️ **La cifra en cero necesita contexto en la propia tarjeta.** Es la corrección de fondo.
   ARGOS 107 mostró **nueve tarjetas en cero** —correcto: ningún hecho de la ventana llevó
   aseguramiento— **junto a tablas llenas de armas** de hechos anteriores. Metodológicamente
   impecable y **ilegible para un mando**: se lee como un error del producto, no como una
   distinción.

   **Solución adoptada, consérvela**: cada tarjeta lleva **dos cifras rotuladas** —la grande, lo
   asegurado en hechos de la ventana; la línea inferior, lo publicado durante el corte procedente de
   hechos anteriores— con una **leyenda encima del bloque** que las distingue. Las de la línea
   inferior son **cálculo propio de ARGOS** y se declaran como tal, con sus salvedades **escritas en
   el cartelón**, no solo en el archivo de fuentes: en ARGOS 107, que 229 de las 326 personas
   detenidas eran un **agregado semanal multidelito** no vinculable 1:1 con armamento.

   **Regla general que se desprende**: cuando una cifra correcta pueda leerse como un error, el
   defecto es del producto. **Póngale al lado el dato que la explica.**

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    Radar, mapa y semáforo se derivan de esos arreglos: nunca teclear los contadores a mano.
#    Si no hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm":
#    un mapa enteramente gris no aporta inteligencia. El validador ya lo contempla.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 108 <FECHA> 107 2026-08-25 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

**Comprobar antes de publicar**: mismo número de ítems por lista en ambas versiones · mismo número
de iconos · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio (`sem-item`,
`stat-tile`, `cover-visuals`) · sin desbordamiento horizontal a 390 px.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, o que dos equipos lo fichen dos veces. **Y algo más**: en ARGOS 107 localizó un precedente que **mejoró una conclusión** |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón. **ARGOS no es fuente de sí mismo** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

Si el destinatario no autoriza subagentes para los dos primeros, **ejecútelos a mano con el mismo
criterio** —así se hizo en ARGOS 106 y 107, y ambos produjeron hallazgos reales— y **declare** la
ausencia en el indicador de cobertura, no la disimule.

Cuando un control devuelva `CORREGIR ANTES DE PUBLICAR`, se corrige y se vuelve a pasar. Si se
decide no corregir, la razón se deja escrita en el archivo de fuentes.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md`.
3. **Escribir `reports/_arranque-ARGOS-109.md`** y borrar este archivo.
4. Commit descriptivo, push a la rama de la edición, y **merge a `main`** para que la rama por
   defecto no vuelva a quedarse atrás.

---

## TEXTO PARA PEGAR EN EL CHAT NUEVO

> Genera el ARGOS de hoy. Antes de numerar la edición, lee `reports/_arranque-ARGOS-108.md` y
> ejecuta su Bloque 0: la numeración sale del archivo, no de lo que veas en la rama local. Después
> lee `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-08-25-fuentes.md`.
>
> La ventana abre donde cerró ARGOS 107 (2026-08-25 09:26 CDMX) y cierra a la hora real de arranque,
> verificada con `TZ=America/Mexico_City date`.
>
> Prioridades: **localizar al periodista Elí Martínez** (`ARG-107-001`, la línea más perecedera del
> archivo); saldar los portales que quedaron `NO REVISADA` dentro de entidades ya consultadas; y
> aplicar y declarar el **Ciclo A (Noroeste + Centro)**.
>
> Respeta las tres correcciones del Bloque 6: **sin resumen ejecutivo**; **ningún hecho con ficha
> propia se repite en una tabla resumen**; y **toda cifra en cero lleva al lado el dato que la
> explica** —las tarjetas de armamento van con doble cifra rotulada—.
>
> Genera cartelón **y** versión móvil —esta última con `tools/gen-movil.py`, nunca a mano—,
> actualiza `_pendientes.md` e `indice-arg-id.md`, escribe el arranque de ARGOS 109, y al cerrar
> mergea a `main`.
>
> Autorizo subagentes para los seis barridos regionales.
