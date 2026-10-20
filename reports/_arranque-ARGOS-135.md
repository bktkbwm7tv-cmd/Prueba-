# ORDEN DE ARRANQUE — ARGOS 135

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 134 (corte 2026-10-16 11:34). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-16-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-135.txt`.** Este archivo es el detalle.

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
git merge --ff-only origin/claude/argos-134
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 135**: última edición `argos-2026-10-16` (ARGOS 134) y **183 archivos** en `reports/`
(177 + cuatro de la edición + `_arranque-ARGOS-135.md` + `_ordenes-ARGOS-135.txt`).
⚠️ **ARGOS 129 a 134 viven en `claude/argos-129` … `-134`**, encadenadas. Si `main` no las contiene, los `ff-only` deben avanzar en
fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** En 133 y 134 el clon arrancó con HEAD suelto en `60f2777`:
abrir `claude/argos-135` antes de fusionar; no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 135** |
| Ventana | **abre 2026-10-16 11:34 CDMX** —donde cerró ARGOS 134— y cierra a la **hora real de arranque de la producción** (declararla en el archivo de fuentes) |
| Serie | 23 h 21 (130) · 23 h 04 (131) · 24 h 56 (132) · 22 h 57 (133) · **28 h 18 (134)** |
| Densidad | 0,39 · 0,26 · 0,24 · 0,48 · **0,67** — 134: **12 de 19 hechos en `FRONTERA`** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 134**, **Abiertos que ARGOS 135 hereda** y **Deuda de método (ARGOS 134)**.
3. `reports/argos-2026-10-16-fuentes.md` — §5 (encargos), §7 (arbitrajes y criterio institucional), §8 (fe de erratas), §9 (cobertura), §13 (controles).
4. `reports/indice-arg-id.md` y **el HTML de las cinco ediciones previas** — `grep` por topónimo **antes de fichar, también cada `-REC-`**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (134: `standard` no halló ningún hecho del 15-oct).
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** y **~30 para `procedencia-cifras`**. 134 gastó **196** (2 + 157 + 7 + 30), más 4 de la segunda ronda de controles como máximo.
- Cada equipo: búsqueda por día de la semana, madrugada del día de apertura, tarde-noche, fecha de cierre en la ruta, «funcionario asesinado», «fosa».
- **Encargos añadidos durante la ola** funcionaron en 134 (Puebla Tres Cerritos, Atoyac, Monterrey, Hermosillo).
- Informes de los equipos: llegan por `SubagentHandback`; se extraen íntegros con un script del campo `input.message` del archivo de salida al *scratchpad*.

## BLOQUE 4 — DEUDA QUE ARGOS 135 HEREDA

Ver `_pendientes.md`, «Abiertos que ARGOS 135 hereda». Encargos prioritarios: **Silao, Barrio Nuevo** (`ARG-134-001`, día del hecho), **Puebla, Tres Cerritos**
(`-005`), **Coquimatlán** (`-003`), **Tlalnepantla** (`-004`), **Monterrey y Santa Catarina** (`-002`, `-007`), **Laguna Colorada** (`-016`, hora de inicio),
**Tezontepec y Tula** (rojo candidato), recuperaciones de 134, **Cajeme** (color).

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: **armamento** BCS, Chih, Sin, Dgo · Coah · Col, Nay, Ags · Edomex, Mor, Pue, Qro · Ver, Tab · Yuc · **sentencias** BCS, Son, Sin, Dgo ·
  NL, SLP, Zac · Jal, Col, Nay, Gto · Edomex, Mor, Pue, Tlax, Qro · Camp. Después, **CICLO A** (Noroeste + Centro).
- **Criterio de cobertura**: armamento y sentencias, `REVISADA` = búsqueda dirigida que devolvió páginas del **dominio oficial de esa institución** (`boletines.guanajuato.gob.mx` no cuenta como fiscalía); un hecho por medios no cubre el dominio. Alto impacto: declarar qué entidades tuvieron consulta propia y cuáles solo regional.
- **Federales**: Defensa y Marina (`NO REVISADA` en 134) con cuota propia. Boletín federal: triple consulta para el 15 y 16-oct.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 134

| Trampa | Control |
|---|---|
| **Recuperación ya publicada** | `ARG-134-REC-005` era `ARG-131-003` (camioneta de la FGE Puebla): grep de cada `-REC-` en las cinco ediciones previas |
| **Equipo que fecha un hecho por un agregado** | Silao, Barrio Nuevo: Occidente lo fechó el 14 por el agregado de AM del 16; las rutas y la secuencia de publicación apuntan al 15 |
| **Error de entidad del resumidor** | Coquimatlán situado en Jalisco: es Colima |
| **Desglose de fuente única** | Laguna Colorada: 3 largas/1 corta/8 cargadores solo en Meganoticias sin fecha; se integró como 4 sin categoría |
| **Titular que no dice lo que la ficha le atribuye** | Irapuato: «hay un detenido», no «probable responsable» |
| **Cifras del boletín federal solo por resumen** | No se imprimen en el cartelón: entidad y evento, sin números |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-134.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes (`CONSULTA` con la hora real de fin de consultas), los `assert`
  (incluido `NFR`) y los textos de portada, Valoración, Conclusiones, sentencias y cobertura. Plantilla: `reports/argos-2026-10-16.html`. Cambie la línea de `<title>`
  que reemplaza el generador (ARGOS 134 — 2026-10-16). `armrow` ya está en el script. `WINDOW_DAYS` con `assert`.
- ⚠️ **Portada**: cinco «SOLICITE A…», una por línea, **solo ARG-ID**, sin cifras ni titulares, sobre hechos distintos de las conclusiones. **Valoración solo con ARG-ID.**
- ⚠️ **Deslindes**: rótulo breve; nada de «omisión de ARGOS N» ni de «ficha propia en 🟢» en el cartelón.
- ⚠️ **Sentencias candidatas sin boletín: sin nombres.**
- Móvil y texto: `python3 tools/gen-movil.py 135 <FECHA> 134 2026-10-16 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-16 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes, en paralelo, sobre una versión estable y commiteada, **con las notas íntegras de
  los seis equipos**. **Veinte pases, veinte «CORREGIR».** Segunda ronda sobre la versión corregida.
