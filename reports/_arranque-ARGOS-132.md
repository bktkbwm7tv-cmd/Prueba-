# ORDEN DE ARRANQUE — ARGOS 132

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 131 (corte 2026-10-13 07:23). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-13-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-132.txt`.** Este archivo es el detalle.

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
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 132**: última edición `argos-2026-10-13` (ARGOS 131) y **165 archivos** en `reports/`
(159 + cuatro de la edición + `_arranque-ARGOS-132.md` + `_ordenes-ARGOS-132.txt`).
⚠️ **ARGOS 129, 130 y 131 viven en `claude/argos-129`, `-130` y `-131`**, encadenadas (`131` parte de `63c1325`). Si `main` no las contiene, los
`ff-only` deben avanzar en fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** El clon puede arrancar por detrás de
`origin/main` (en 128-131 arrancó en `60f2777`): no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 132** |
| Ventana | **abre 2026-10-13 07:23 CDMX** —donde cerró ARGOS 131— y cierra a la **hora real de arranque** |
| Serie | 22 h 24 (127) · 25 h 48 (128) · 23 h 50 (129) · 23 h 21 (130) · **23 h 04 (131)** |
| Densidad | 0,27 · 0,23 · 0,25 · 0,39 · **0,26** — 131: **6 de 6 hechos en `FRONTERA`** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 131**, **Abiertos que ARGOS 132 hereda** y **Deuda de método (ARGOS 131)**.
3. `reports/argos-2026-10-13-fuentes.md` — §5 (encargos), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §13 (controles), §15.
4. `reports/indice-arg-id.md` y **el HTML de las tres ediciones previas** — `grep` por topónimo **antes de fichar**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (131: `standard` devolvió Jacona de 2021, 2024 y abril).
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** —una búsqueda nacional por día de la ventana; en 131 halló Vallado Viejo,
  Otatitlán, el boletín federal y la Semar— y **~25 para `procedencia-cifras`**. 131 gastó **192**.
- **Cifra entre comillas** para el literal.
- ⚠️ **Nuevo**: cada equipo hace **una búsqueda de la tarde-noche del día de apertura** (en 131 se recuperaron tres omisiones de 130 de esa franja).

## BLOQUE 4 — DEUDA QUE ARGOS 132 HEREDA

Ver `_pendientes.md`, «Abiertos que ARGOS 132 hereda». Encargos prioritarios: **Totolapan** (`ARG-131-002`), **Puebla FGE** (`-003`), **«El Cabra»**
(`-006`, fecha de la captura), **horas del 11-oct** (`ARG-130-003`, `-004`, `ARG-131-REC-003`, `-REC-004`), **Jacona** (`ARG-130-001`), **Vallado Viejo**
(`ARG-131-001`), **Minatitlán** y **Otatitlán**.

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: **armamento** BCS, Son, Chih, Sin · Edomex, Tlax, Hgo · Oax, Gro · **sentencias** BCS, Son, Sin · Coah, Zac · Col, Nay, Gto ·
  CDMX, Mor, Tlax, Hgo, Qro · Camp · **alto impacto** BCS y Dgo. Después, **CICLO A** (Noroeste + Centro).
- **Criterio de cobertura**: armamento y sentencias, `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial; alto impacto, búsqueda
  dirigida en medios. Dominios confirmados en §3 y §9 del archivo de fuentes de 131.
- **Federales**: GN, Defensa y Marina con cuota propia. Boletín federal: triple consulta para las acciones del 12 y 13-oct.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 131

| Trampa | Control |
|---|---|
| **«Policías muertos» que eran un accidente vial** | Totolapan: el titular «mueren dos policías» describe un accidente de patrulla en ruta al operativo |
| **El mismo medio publica dos hechos del mismo día y municipio** | Morelia: Changoonga, micheladas (Solidaridad) e Ilustres Novohispanos (vivienda): dos notas, dos hechos |
| **Día de la semana incoherente** | Azteca Chiapas: «domingo 12 de octubre» (el 12-oct-2026 es lunes) |
| **Boletín agregado publicado al día siguiente del cierre** | Gabinete 9-11 oct, publicado el 12: solo apareció por título sin `site:` |
| **Titular con «sospechosos» convertido en «detenidos»** | Excélsior, agregado federal |
| **Pena por titular sin fecha y publicación por otro medio** | FGR Pichilingue: Zócalo (8 años, sin fecha) + Tijuana Última Hora (12/10/2026) |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-131.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes y los textos de portada, Valoración, Conclusiones,
  sentencias y cobertura. Plantilla: `reports/argos-2026-10-13.html`. Cambie la línea de `<title>` que reemplaza el generador (ARGOS 131 — 2026-10-13).
  Si no hay recuperaciones, retire su página (ver `datos-argos-130.py`). `ARM = []` funciona (tabla «SIN FILAS»). `WINDOW_DAYS = 2;` con `assert`.
- Móvil y texto: `python3 tools/gen-movil.py 132 <FECHA> 131 2026-10-13 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-13 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes, en paralelo, sobre una versión estable y commiteada, **con las notas de
  los seis equipos**. **Diecisiete pases consecutivos, diecisiete «CORREGIR».**
