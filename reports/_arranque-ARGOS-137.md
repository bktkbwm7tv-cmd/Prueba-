# ORDEN DE ARRANQUE — ARGOS 137

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 136 (corte 2026-10-18 08:34). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-18-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-137.txt`.** Este archivo es el detalle.

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
git merge --ff-only origin/claude/argos-136
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 137**: última edición `argos-2026-10-18` (ARGOS 136) y **196 archivos** en `reports/`
(189 + cinco de la edición —con `argos-2026-10-18-equipos.md`— + `_arranque-ARGOS-137.md` + `_ordenes-ARGOS-137.txt`).
⚠️ **ARGOS 129 a 136 viven en `claude/argos-129` … `-136`**, encadenadas. Si `main` no las contiene, los `ff-only` deben avanzar en
fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** En 133 a 136 el clon arrancó con HEAD suelto en `60f2777`:
abrir `claude/argos-136` antes de fusionar; no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 137** |
| Ventana | **abre 2026-10-18 08:34 CDMX** —donde cerró ARGOS 136— y cierra a la **hora real de arranque de la producción** |
| Serie | 24 h 56 (132) · 22 h 57 (133) · 28 h 18 (134) · 21 h 54 (135) · **23 h 06 (136)** |
| Densidad | 0,24 · 0,48 · 0,67 · 0,59 · **0,39** — 136: **5 de 9 hechos con `FRONTERA` o publicados el día de apertura sin hora** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 136**, **Abiertos que ARGOS 137 hereda** y **Deuda de método (ARGOS 136)**.
3. `reports/argos-2026-10-18-fuentes.md` — §5 (encargos), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §13 (controles), §16 (emisores).
4. `reports/indice-arg-id.md` y **el HTML de las cinco ediciones previas** — `grep` por topónimo **antes de fichar, también cada `-REC-`**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos.
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** y **~30 para `procedencia-cifras`**. 136 gastó **198** (2 + 159 + 7 + 30); la segunda ronda de controles, sin búsquedas.
- Plantilla común de los equipos: `tools/plantilla-equipos-136.md` → copiarla al *scratchpad* como la de 137, cambiar ventana y calendario, y hacer que cada equipo la lea primero; funcionó en 135 y 136. Informes íntegros y controles, al cierre, en `reports/argos-<FECHA>-equipos.md`.
- Informes de los equipos: llegan por `SubagentHandback`; se extraen íntegros con `python3 -I tools/extrae-informe.py <archivo de salida> 'REGIÓN: <NOMBRE>' <destino en el scratchpad>`.

## BLOQUE 4 — DEUDA QUE ARGOS 137 HEREDA

Ver `_pendientes.md`, «Abiertos que ARGOS 137 hereda». **Primero, el ciclo y los dos colores** (preguntar al destinatario). Prioridad de búsqueda: **Acapulco** (`-002`, `-003`), **Taxco** (`-008`, `-009`), **exfiscal** (`-006`) y **Cuauhtémoc** (`-REC-003`), **SSP Sinaloa ↔ `ARG-135-ARM-001`**, **San Baltazar Tetela**, **Linares**, **Chiapa de Corzo**; sentencia de **Tulantepec (miércoles 21)**.

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: armamento 18 `NO REVISADA`; sentencias 15 `NO REVISADA`; alto impacto de Aguascalientes. Después, **el ciclo que confirme el destinatario** (tabla: A; serie declarada: C).
- **Criterio de cobertura**: `REVISADA` = búsqueda dirigida que devolvió páginas del **dominio oficial de esa institución**; el portal genérico del gobierno estatal se declara aparte; **lectura parcial** (solo portada, solo convocatorias, sin boletines con fecha) se declara como tal.
- **Fosas por entidad fronteriza** (BC, Son, Chih, Tamps).
- **Dominios corregidos**: ver `_pendientes.md`.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 136

| Trampa | Control |
|---|---|
| **Resumen con «madrugada de este domingo» que mezcla notas** | Xalapa, El Moral: la descripción era de un homicidio del 3-oct. Exigir ruta fechada o titular con día |
| **Nota con incoherencia interna** («el sábado» y «ayer») | Temixco: día no fijado; la colonia acumula homónimos |
| **Hora pegada a la apertura** | Silao (~06:30), Cuauhtémoc (~09:00) y Maneadero (~09:30), todos por resumen: decidir ventana solo con ancla; si no, marca |
| **Título más firme que la ficha** | «Elemento de la GN» (adscripción contradicha), «dos hombres» (titular: «2 asesinados»), «dos agentes de la CIA» (titular sin número) |
| **Recuento de fuentes sin URL archivada** | Taxco y el exfiscal: las URL estaban en búsquedas del coordinador no anotadas. Anotar todas |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-136.py`**: copie y cambie `E`, `R`, `ARM`, las constantes (`CONSULTA` con la hora real de fin de consultas), los `assert` y los textos. Plantilla: `reports/argos-2026-10-18.html`; cambie la línea de `<title>` que reemplaza el generador (ARGOS 136 — 2026-10-18). El generador ya inyecta `CONSULTA_TXT` en el tooltip y **lo reemplaza** si la plantilla (136) ya lo trae. `EVENTOS_ARM` solo lleva filas con cifra integrada.
- ⚠️ **Portada**: cinco «SOLICITE A…», solo ARG-ID, sobre hechos distintos de las conclusiones. **Valoración solo con ARG-ID.** **Deslindes sin color.**
- Móvil y texto: `python3 tools/gen-movil.py 137 <FECHA> 136 2026-10-18 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-18 <FECHA>` → «validación OK» (solo escritorio; el móvil lo valida su generador).
- **Controles**: `editor-duplicidad` y `procedencia-cifras` en paralelo, sobre una versión estable y commiteada, **con las notas íntegras de los seis equipos**. **Veinte pases, veinte «CORREGIR».** Segunda ronda sobre la versión corregida.
