# ORDEN DE ARRANQUE — ARGOS 107

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 106** (corte 2026-08-24, commit `f368a8d`).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**Regla nacida del fallo de ARGOS 106.** Esa sesión clonó el repositorio en un HEAD por defecto
atrasado, dio por buena la última edición que veía en su rama local y estuvo a punto de publicar un
**«ARGOS 89»** —edición que no existe— con ventana solapada y sin versión móvil.

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git log --oneline -1 origin/main                   # ¿main está al día?
ls reports/ | tail -6                              # ¿cuál es la última edición del archivo?
git ls-remote --heads origin | grep argos          # ¿hay ramas por delante de main?
```

**Estado que debe encontrar ARGOS 107**: `main` en `f368a8d`, última edición `argos-2026-08-24`
(ARGOS 106), 62 archivos en `reports/`. **Si `main` está por detrás de eso, algo se rompió: pare y
avísele al destinatario antes de escribir una línea.**

`main` quedó al día en ARGOS 106 por decisión expresa del destinatario. **Mantenerlo así**: al cierre,
mergear la rama de la edición a `main` (`git push origin HEAD:main`, que es fast-forward si nadie
tocó `main` en medio). No volver al patrón de ramas aisladas.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 107** |
| **Ventana** | **desde 2026-08-24 09:15 CDMX** (cierre de ARGOS 106) **hasta la hora verificada de arranque** |
| **Rama** | `claude/argos-107-hoy`, creada desde `main` |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-108.md` |

**Continuidad de ventana**: la ventana abre exactamente donde cerró la anterior. Ni un minuto de hueco
—ARGOS 105 documentó que un multihomicidio se perdió entre dos ediciones por esa causa— ni un minuto
de solape.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-08-24-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio por entidad y municipio antes de fichar
   cualquier hecho como nuevo.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 107 HEREDA Y DEBE SALDAR

### 3.1 Cobertura — prioridad sobre el ciclo

ARGOS 106 revisó **5 de 32 entidades**. Las **27 restantes** quedaron `NO REVISADA`. Por la regla de
prioridad de `CLAUDE.md`, **esas 27 encabezan el triaje de esta edición aunque no les toque por
ciclo**:

- **Noroeste**: Chihuahua, Durango, Baja California, Baja California Sur
- **Noreste**: Coahuila, Nuevo León, Tamaulipas, San Luis Potosí, Zacatecas *(las 5)*
- **Occidente**: Jalisco, Nayarit, Aguascalientes, Michoacán, Guanajuato
- **Centro**: Morelos, Puebla, Tlaxcala, Hidalgo, Querétaro
- **Golfo**: Veracruz, Tabasco *(las 2)*
- **Sureste**: Chiapas, Oaxaca, Guerrero, Campeche, Yucatán, Quintana Roo *(las 6)*

### 3.2 El ciclo, después de saldar

A ARGOS 106 le tocaba el **Ciclo C (Occidente + Sureste)** encabezando el triaje judicial y **no se
aplicó**. ARGOS 107 lo aplica **y lo declara expresamente** en su archivo de fuentes, junto con qué
aportó la rotación que el orden anterior no habría aportado. *Una edición que no diga qué ciclo
aplicó, no aplicó ninguno.*

### 3.3 Los seguimientos que más rinden

Del cuadro completo en `_pendientes.md`, estos tres son los de mayor rendimiento esperado:

1. **Morelia** (`ARG-106-REC-002`) — situación jurídica de los dos elementos de la GN asegurados y
   **qué fuero asume la investigación**. Su liberación temprana o su traslado marcará el criterio
   institucional aplicable a este tipo de casos. *Es el indicador más informativo del corte.*
2. **Acapulco** (`ARG-106-REC-001`) — pronunciamiento de la GN sobre el uso de sus insignias y
   rastreo hospitalario del agresor herido en el tórax. **Línea perecedera**: ya lleva días perdidos.
3. **72 vs. 172 AEI en Sinaloa** — discrepancia heredada que bloquea cualquier serie de explosivos
   del estado. La cierra el boletín original.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo, uno por región. **ARGOS 106 no los
lanzó** —restricción operativa de aquella sesión— y por eso su cobertura fue de 5 de 32.

**Para ARGOS 107**: si el destinatario autoriza subagentes, lanzar los seis en un solo mensaje, cada
uno con la lista de portales de sus entidades y con las de la sección 3.1 al frente. Si **no** los
autoriza, hacer barrido dirigido a mano y **declarar la cobertura real**: `NO REVISADA` para lo no
consultado, jamás `SIN ACTUALIZACIÓN`.

**Control nuevo, obligatorio desde ARGOS 107.** ARGOS 105 declaró *32 de 32 entidades revisadas* y
aun así no localizó una masacre de cuatro víctimas en Acapulco ni un homicidio con participación de
personal federal en Morelia. Es un **fallo de recall dentro de una cobertura declarada completa**:
cubrir el 100% de los portales no equivale a cubrir el 100% de los hechos cuando los portales están
bloqueados y el barrido depende del buscador.

> **Cuando una región se declare revisada sin hallazgos, contrastar con una consulta genérica por
> entidad y sin restricción de dominio** —`ataque armado <entidad> <fecha>`— antes de cerrarla.
> Es exactamente lo que hizo aparecer los cuatro hechos que ARGOS 105 perdió.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho puede ser posterior al día del corte. El resumidor inventa futuros |
| **Trampa de aniversario** | Un hecho de agosto de 2025 se presenta como de 2026. **Ninguna cifra de abatidos entra sin URL con año en la ruta** |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: **fecha la página, no el hecho**, y no basta como fuente única |
| **Día de la semana** | Si la nota dice «el viernes» y ese día no fue viernes, la atribución es falsa. Contrastar contra calendario |
| **Portal de ID correlativo** | Un boletín ya fechado en el archivo acota a todos los de numeración inferior |
| **Pena compuesta** | «X años para dos sujetos» **no se suma** sin saber si es por persona o conjunta |
| ***Slug* institucional** | Prueba el término jurídico, **no identifica el caso**: hacen falta dos campos individualizadores |
| **Un `grep` sin leer** | Si una consulta devuelve una fe de erratas o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria antes de redactar** |

**Egreso bloqueado, decimoctava edición.** `*.gob.mx`, `gabinetedeseguridad.gob.mx`, `fgr.org.mx` y
los dominios de medios devuelven `CONNECT tunnel failed, 403`. **Cero portales por acceso directo.**
Techo de confianza del producto: **★★★★☆**. Ninguna ficha lleva ★★★★★.
`docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar y es el único cambio que elevaría ese techo.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente, fijada por el destinatario en ARGOS 105 y vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, ventana de origen declarada y **fuera de todos los totales**.
- **Sin «Ejes del día».** Cada hecho aparece **una sola vez**, en su ficha. Las tablas de módulo
  aportan campos distintos —cifras, corporación, pena—, no repiten el titular.
- **Sin ARGOS hablando de ARGOS.** Nada de presupuesto de búsqueda, ciclos, agentes ni cobertura del
  instrumento en el cartelón: eso va al archivo de fuentes y a `_pendientes.md`. Las excepciones de
  trazabilidad se escriben **en una línea**, no en párrafos.
- **Iconografía de armamento** en tarjetas y cabeceras, siempre con etiqueta y cifra. **Las
  categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Conclusiones de inteligencia criminal**, no de método. Si una conclusión no le dice a un mando
  algo que pueda accionar o vigilar, no es conclusión de ARGOS.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`. Una
  `<table>` suelta desborda la móvil **en silencio**.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    Radar, mapa y semáforo se derivan de esos arreglos: nunca teclear los contadores a mano.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 107 <FECHA> 106 2026-08-24 <HORA>

# 3. La validación del generador debe decir "validación OK" y los contadores
#    deben coincidir con el semáforo del escritorio. Si no, se corrige la
#    HERRAMIENTA, no su salida.
```

**Comprobar antes de publicar**: mismo número de ítems por lista en ambas versiones · cero tarjetas
`.reg` sin texto · cero restos de clases de escritorio (`sem-item`, `stat-tile`, `cover-visuals`) ·
sin desbordamiento horizontal a 390 px.

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, o que dos equipos lo fichen dos veces |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón. **ARGOS no es fuente de sí mismo** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

Si el destinatario no autoriza subagentes, **los dos primeros se ejecutan a mano con el mismo
criterio** —en ARGOS 106 así se hizo y ambos produjeron hallazgos reales— y la ausencia del tercero
**se declara en el indicador de cobertura, no se disimula**.

Cuando un control devuelva `CORREGIR ANTES DE PUBLICAR`, se corrige y se vuelve a pasar. Si se decide
no corregir, la razón se deja escrita en el archivo de fuentes.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md`.
3. **Escribir `reports/_arranque-ARGOS-108.md`** y borrar este archivo. Sin ese paso, la edición
   siguiente vuelve a arrancar a ciegas.
4. Commit descriptivo, push a `claude/argos-107-hoy`, y **`git push origin HEAD:main`** para que la
   rama por defecto no vuelva a quedarse atrás.

---

## TEXTO PARA PEGAR EN EL CHAT NUEVO

> Genera el ARGOS de hoy. Antes de numerar la edición, lee
> `reports/_arranque-ARGOS-107.md` y ejecuta su Bloque 0: la numeración sale del archivo, no de lo
> que veas en la rama local. Después lee `CLAUDE.md`, `reports/_pendientes.md` y el archivo de
> fuentes de la edición anterior.
>
> La ventana abre donde cerró ARGOS 106 (2026-08-24 09:15 CDMX) y cierra a la hora real de arranque,
> verificada con `TZ=America/Mexico_City date`.
>
> Prioridades de esta edición: saldar las 27 entidades que quedaron `NO REVISADA`; aplicar y declarar
> el Ciclo C; y perseguir los tres seguimientos de mayor rendimiento (Morelia, Acapulco, la
> discrepancia 72/172 AEI de Sinaloa).
>
> Genera cartelón **y** versión móvil —esta última con `tools/gen-movil.py`, nunca a mano—, actualiza
> `_pendientes.md` e `indice-arg-id.md`, escribe el arranque de ARGOS 108, y al cerrar mergea a
> `main`.
>
> Dime si autorizas subagentes para los seis barridos regionales y los tres controles editoriales.
