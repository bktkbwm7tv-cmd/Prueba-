# ORDEN DE ARRANQUE — ARGOS 134

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 133 (corte 2026-10-15 07:16). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-15-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-134.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main
git merge --ff-only origin/claude/argos-129
git merge --ff-only origin/claude/argos-130
git merge --ff-only origin/claude/argos-131
git merge --ff-only origin/claude/argos-132
git merge --ff-only origin/claude/argos-133
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 134**: última edición `argos-2026-10-15` (ARGOS 133) y **177 archivos** en `reports/`
(171 + cuatro de la edición + `_arranque-ARGOS-134.md` + `_ordenes-ARGOS-134.txt`).
⚠️ **ARGOS 129 a 133 viven en `claude/argos-129` … `-133`**, encadenadas (`133` parte de `4bf49a7`). Si `main` no las contiene, los `ff-only` deben avanzar en
fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** En 133 el clon arrancó en `60f2777` sobre la rama de sesión
`claude/argos-criminal-intelligence-otiawj`: abrir `claude/argos-134` antes de fusionar; no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 134** |
| Ventana | **abre 2026-10-15 07:16 CDMX** —donde cerró ARGOS 133— y cierra a la **hora real de arranque** |
| Serie | 23 h 50 (129) · 23 h 21 (130) · 23 h 04 (131) · 24 h 56 (132) · **22 h 57 (133)** |
| Densidad | 0,25 · 0,39 · 0,26 · 0,24 · **0,48** — 133: **7 de 11 hechos en `FRONTERA`** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 133**, **Abiertos que ARGOS 134 hereda** y **Deuda de método (ARGOS 133)**.
3. `reports/argos-2026-10-15-fuentes.md` — §5 (encargos), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §10, §13 (controles), §15.
4. `reports/indice-arg-id.md` y **el HTML de las tres ediciones previas** — `grep` por topónimo **antes de fichar**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (133: `standard` no halló ningún hecho del 14-oct).
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** y **~25 para `procedencia-cifras`**. 133 gastó **195** (2 + 159 + 9 + 25).
- ⚠️ **Nuevo**: cada equipo hace **una búsqueda de la madrugada del día de apertura** (en 133, siete de dieciocho fichas eran de la ventana de 132 o anteriores)
  y **una con la fecha del día de cierre en la ruta** (en 133, Irapuato y Escuinapa nocturno los halló `procedencia-cifras`).
- Encargos añadidos del coordinador a los equipos **durante** la ola: funcionaron en 133 (Atotonilco, Romita, Salcido).
- **El sistema de extracción de las notas**: los informes de los equipos llegan como mensaje; se extraen íntegros del archivo de salida de cada agente con un
  script al *scratchpad* (`informe-<región>.md`) antes de lanzar los controles.

## BLOQUE 4 — DEUDA QUE ARGOS 134 HEREDA

Ver `_pendientes.md`, «Abiertos que ARGOS 134 hereda». Encargos prioritarios: **Atotonilco de Tula** (`ARG-133-001`), **Irapuato** (`-010`), **Salamanca y Romita**
(`-002`, `-003`), **Iztapalapa** (`-004`, `-008`), horas de **Pénjamo y Silao** (`ARG-133-REC-001` a `-003`), **Cajeme** (`-REC-005`), **«El Wicho»** y **Cotija** (`ARG-132-005`).

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: **armamento** BC, BCS, Son · SLP · Jal, Col, Nay, Mich · Pue, Tlax, Hgo · Tab · **sentencias** BCS, Son, Chih, Sin · Coah, Tamps, SLP ·
  Jal, Col, Nay, Ags, Mich · CDMX, Tlax, Hgo · Camp, QRoo. Después, **CICLO C** (Occidente + Sureste).
- **Criterio de cobertura**: armamento y sentencias, `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial, **anotado**; alto impacto, búsqueda
  dirigida en medios; **la franja de madrugada del día de cierre se declara aparte**. Dominios nuevos confirmados en 133: `spsc.campeche.gob.mx`, `sseguridad.edomex.gob.mx`,
  `fiscalia.puebla.gob.mx`, `fiscalianl.gob.mx`, `fge.yucatan.gob.mx`, `fiscaliaguerrero.gob.mx`, `fge.chiapas.gob.mx`, `sspo.gob.mx`.
- **Federales**: GN y Defensa (`NO REVISADA` en 133: dominio no devuelto) y Marina con cuota propia. Boletín federal: triple consulta para el 14 y 15-oct.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 133

| Trampa | Control |
|---|---|
| **Madrugada del día de cierre de la edición anterior** | Pénjamo (~05:35), Silao, Querétaro: publicados el 14 de hechos anteriores a las 08:19 → recuperaciones de 132 |
| **Nota que agrupa dos hechos** | Meganoticias 778257: Acaponeta + fosa de Tecuala |
| **Resumen que contradice su propia consulta** | Cotija: «lunes 12» en una búsqueda y «ninguna nota menciona el 12» en otra: sin fe de erratas |
| **Boletín de 2025 con la misma fecha** | `gabinetedeseguridad.gob.mx/contenido/6826` = 13-oct-**2025** |
| **Alias repetido** | «El Wicho» de Villa Unión (Rugrats) ≠ «El Wicho» de Tocumbo (`ARG-113-REC-001`) · «La Patrona» de Ciudad del Carmen ≠ `ARG-96-003` |
| **Agregado que suma ventanas** | «Ocho muertos en tres municipios de Guanajuato» (El Universal) mezcla 132 y 133 |
| **Día de la semana incoherente** | «Martes 14» (Milenio, Navolato) y «este jueves» (Sinaloahoy, Malecón): atribuciones falsas |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-133.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes, los `assert` y los textos de portada, Valoración,
  Conclusiones, sentencias y cobertura. Plantilla: `reports/argos-2026-10-15.html`. Cambie la línea de `<title>` que reemplaza el generador (ARGOS 133 — 2026-10-15).
  `ARM = []` funciona (tabla «SIN FILAS»); para filas, la función `armrow` está en `datos-argos-129.py`. `WINDOW_DAYS = 2;` con `assert`.
- ⚠️ **Acciones de portada como solicitud** («SOLICITE A…»), **una por línea**, **sin cifras**, **nunca «EXIJA»**.
- ⚠️ **Deslindes sin explicación de color**: rótulo breve («🔴 por …»).
- Móvil y texto: `python3 tools/gen-movil.py 134 <FECHA> 133 2026-10-15 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-15 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes, en paralelo, sobre una versión estable y commiteada, **con las notas íntegras de
  los seis equipos**. **Veinte pases consecutivos, veinte «CORREGIR».**
