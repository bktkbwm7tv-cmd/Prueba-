# ORDEN DE ARRANQUE — ARGOS 133

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 132 (corte 2026-10-14 08:19). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-14-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-133.txt`.** Este archivo es el detalle.

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
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 133**: última edición `argos-2026-10-14` (ARGOS 132) y **171 archivos** en `reports/`
(165 + cuatro de la edición + `_arranque-ARGOS-133.md` + `_ordenes-ARGOS-133.txt`).
⚠️ **ARGOS 129 a 132 viven en `claude/argos-129` … `-132`**, encadenadas (`132` parte de `db02540`). Si `main` no las contiene, los `ff-only` deben
avanzar en fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** El clon puede arrancar por detrás de `origin/main` y con
HEAD suelto (en 128-132 arrancó en `60f2777`): abrir `claude/argos-133` antes de fusionar; no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 133** |
| Ventana | **abre 2026-10-14 08:19 CDMX** —donde cerró ARGOS 132— y cierra a la **hora real de arranque** |
| Serie | 25 h 48 (128) · 23 h 50 (129) · 23 h 21 (130) · 23 h 04 (131) · **24 h 56 (132)** |
| Densidad | 0,23 · 0,25 · 0,39 · 0,26 · **0,24** — 132: **6 de 6 hechos en `FRONTERA`** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 132**, **Abiertos que ARGOS 133 hereda** y **Deuda de método (ARGOS 132)**.
3. `reports/argos-2026-10-14-fuentes.md` — §5 (encargos), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §10, §13 (controles), §15.
4. `reports/indice-arg-id.md` y **el HTML de las tres ediciones previas** — `grep` por topónimo **antes de fichar**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (132: `standard` no halló ningún hecho del 13-oct).
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** —una búsqueda nacional por día de la ventana; en 132 halló San Blas Atempa,
  Cotija, «El Cromo» y el boletín federal del 12-oct— y **~25 para `procedencia-cifras`**. 132 gastó **195**.
- **Cifra entre comillas** para el literal.
- ⚠️ **Nuevo**: cada equipo hace **una búsqueda de «fosa / colectivo de búsqueda / restos»** por sus entidades (en 132 la ola omitió la fosa de Navolato, el
  único rojo propio, que halló `procedencia-cifras`).
- ⚠️ **Nuevo**: **antes de fichar, buscar la primera publicación del hecho** (en 132, Escuinapa venía de una nota del 12-oct y León era del 27-sep).
- ⚠️ **Nuevo**: cada equipo **anota el dominio devuelto** por entidad y módulo; sin él, la casilla es `NO REVISADA`.

## BLOQUE 4 — DEUDA QUE ARGOS 133 HEREDA

Ver `_pendientes.md`, «Abiertos que ARGOS 133 hereda». Encargos prioritarios: **Navolato** (`ARG-132-001`), **Orizaba** (`-002`, identidad del muerto),
**Cotija** (`-005`, fecha del hecho), **San Blas Atempa** (`-003`) y **«El Cromo»** (`-006`, fecha de captura), horas de **Doctor Coss**, **Escuinapa** y
**Acaponeta** (`-REC-003`, `-005`, `-004`).

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: **armamento** BC, Coah, NL, Tamps, SLP · Ags · CDMX, Edomex, Mor, Qro · Gro, Oax, Chis, Camp, Yuc, QRoo · **sentencias** BC, BCS, Son,
  Sin · NL, SLP · Nay, Gto · Edomex, Pue, Tlax, Hgo · Gro, Chis, Camp, Yuc. Después, **CICLO B** (Noreste + Golfo).
- **Criterio de cobertura**: armamento y sentencias, `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial, **anotado**; alto impacto, búsqueda
  dirigida en medios. Dominios confirmados en §3 y §9 del archivo de fuentes de 132 (nuevos: `sitio.fgecoahuila.gob.mx`, `fiscaliazacatecas.gob.mx`,
  `sspsinaloa.gob.mx`).
- **Federales**: GN, Defensa y Marina con cuota propia. Boletín federal: triple consulta para las acciones del 13 y 14-oct.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 132

| Trampa | Control |
|---|---|
| **Republicador del 13 de un hecho publicado el 12** | Escuinapa, Pueblo Nuevo: Tus Buenas Noticias 2026/10/13, pero Línea Directa 2026-10-12 |
| **Boletín oficial del día de un hecho de semanas atrás** | León, FSPE: boletín del 13-oct, hecho del 27-sep (resumen) |
| **Resúmenes que se contradicen sobre el día del hecho** | Cotija: «12 al mediodía» en una búsqueda, «13» en otra |
| **Mismo hecho con dos topónimos** | Culiacán: Vallado Viejo = Recursos Hidráulicos |
| **Cifras ajenas atribuidas por el resumidor** | «El Cabra»: «7 detenidos, 3 víctimas, 40 largas» eran de una operación de Sonora |
| **Suma de ARGOS presentada como cifra publicada** | Cancún: «24 armas» = 17 + 7 |
| **La palabra «Cromo» en las ediciones de agosto** | Es «monocromo», del CSS de los iconos: no hay antecedente |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-132.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes y los textos de portada, Valoración, Conclusiones,
  sentencias y cobertura. Plantilla: `reports/argos-2026-10-14.html`. Cambie la línea de `<title>` que reemplaza el generador (ARGOS 132 — 2026-10-14).
  `ARM = []` funciona (tabla «SIN FILAS»); para filas, la función `armrow` está en `datos-argos-129.py`. `WINDOW_DAYS = 2;` con `assert`.
- ⚠️ **Acciones de portada como solicitud** («SOLICITE A…»), **una por línea**, **nunca «EXIJA»** ni «evalúe».
- Móvil y texto: `python3 tools/gen-movil.py 133 <FECHA> 132 2026-10-14 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-14 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes, en paralelo, sobre una versión estable y commiteada, **con las notas íntegras de
  los seis equipos**. **Dieciocho pases consecutivos, dieciocho «CORREGIR».**
