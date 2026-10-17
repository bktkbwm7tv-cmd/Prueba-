# ORDEN DE ARRANQUE — ARGOS 136

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 135 (corte 2026-10-17 09:28). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-17-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-136.txt`.** Este archivo es el detalle.

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
git merge --ff-only origin/claude/argos-135
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 136**: última edición `argos-2026-10-17` (ARGOS 135) y **189 archivos** en `reports/`
(183 + cuatro de la edición + `_arranque-ARGOS-136.md` + `_ordenes-ARGOS-136.txt`).
⚠️ **ARGOS 129 a 135 viven en `claude/argos-129` … `-135`**, encadenadas. Si `main` no las contiene, los `ff-only` deben avanzar en
fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** En 133, 134 y 135 el clon arrancó con HEAD suelto en `60f2777`:
abrir `claude/argos-136` antes de fusionar; no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 136** |
| Ventana | **abre 2026-10-17 09:28 CDMX** —donde cerró ARGOS 135— y cierra a la **hora real de arranque de la producción** |
| Serie | 23 h 04 (131) · 24 h 56 (132) · 22 h 57 (133) · 28 h 18 (134) · **21 h 54 (135)** |
| Densidad | 0,26 · 0,24 · 0,48 · 0,67 · **0,59** — 135: **11 de 13 hechos en `FRONTERA`** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 135**, **Abiertos que ARGOS 136 hereda** y **Deuda de método (ARGOS 135)**.
3. `reports/argos-2026-10-17-fuentes.md` — §5 (encargos), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §13 (controles), §16 (emisores).
4. `reports/indice-arg-id.md` y **el HTML de las cinco ediciones previas** — `grep` por topónimo **antes de fichar, también cada `-REC-`**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos.
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** y **~30 para `procedencia-cifras`**. 135 gastó **199** (2 + 159 + 8 + 30); la segunda ronda de controles, sin búsquedas.
- Plantilla común de los equipos: escribirla en el *scratchpad* (ventana, reglas, cotejo `grep`, formato) y hacer que cada equipo la lea primero; funcionó en 135.
- Informes de los equipos: llegan por `SubagentHandback`; se extraen íntegros con un script que busca la cabecera `REGIÓN:` en el archivo de salida y los guarda en el *scratchpad*.

## BLOQUE 4 — DEUDA QUE ARGOS 136 HEREDA

Ver `_pendientes.md`, «Abiertos que ARGOS 136 hereda». Prioridad: **Pokémon ↔ Laguna Colorada** y **cateos ↔ boletín del 15-oct** (las dos filas de armamento de 135 están en ceros), **Apatzingán** (hora), **Linares** (día), **fosas de Cachanillas y Nogales**, **Taxco**, **El Tívoli**.

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: armamento 21 `NO REVISADA` + 8 solo por portal estatal; sentencias 14 `NO REVISADA` (ver pendientes). Después, **CICLO B** (Noreste + Golfo).
- **Criterio de cobertura**: armamento y sentencias, `REVISADA` = búsqueda dirigida que devolvió páginas del **dominio oficial de esa institución**; **el portal genérico del gobierno estatal se declara aparte** («solo por portal del gobierno estatal»).
- **Fosas por entidad fronteriza** (BC, Son, Chih, Tamps): en 135 la búsqueda regional no las trajo.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 135

| Trampa | Control |
|---|---|
| **Operativo federal republicado con desglose nuevo** | «Pokémon» puede ser Laguna Colorada con más detalle: cotejar municipio, emisor, número de armas y detenidos antes de integrar |
| **Boletín federal que llega por medios como nota suelta** | Cateos de Mazatlán y El Carrizal: cotejar con el boletín de las acciones del día anterior |
| **Ruta con solo año y mes** | Zeta, Diario Tijuana, Los Noticieristas (`2026/10`): no cuentan como «con fecha en la ruta» |
| **Resultado viejo en la misma búsqueda** | Apatzingán «heridas por explosivos» era de junio; Maxipista «martes 15» era de 2024; Escuinapa «un muerto y cinco heridos», de julio |
| **Hecho diferido «a la edición siguiente»** | Un hecho de la ventana no pasa a la siguiente: se ficha o se declara `SIN FECHA FIJADA` de su ventana |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-135.py`**: copie y cambie `E`, `R`, `ARM`, las constantes (`CONSULTA` con la hora real de fin de consultas), los `assert` y los textos. Plantilla: `reports/argos-2026-10-17.html`; cambie la línea de `<title>` que reemplaza el generador (ARGOS 135 — 2026-10-17). El generador ya inyecta `CONSULTA_TXT` en el tooltip.
- ⚠️ **Portada**: cinco «SOLICITE A…», solo ARG-ID, sobre hechos distintos de las conclusiones. **Valoración solo con ARG-ID.** **Deslindes sin color.**
- Móvil y texto: `python3 tools/gen-movil.py 136 <FECHA> 135 2026-10-17 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-17 <FECHA>` → «validación OK» (solo escritorio; el móvil lo valida su generador).
- **Controles**: `editor-duplicidad` y `procedencia-cifras` en paralelo, sobre una versión estable y commiteada, **con las notas íntegras de los seis equipos**. **Veinte pases, veinte «CORREGIR».** Segunda ronda sobre la versión corregida.
