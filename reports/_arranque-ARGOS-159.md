# ORDEN DE ARRANQUE — ARGOS 159

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 159 hereda» y «Deuda de método (ARGOS 158)»), `reports/argos-2026-11-26-fuentes.md` (ARGOS 158) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-159.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-26` (ARGOS 158) y **352 archivos** en `reports/` (incluida la orden de 159). 139 a 158 viven fuera de `main`; **158 en `claude/argos-158-criminal-intelligence-0wpevh`** (encima de `claude/argos-158-criminal-intelligence-2goit7`). Todas las fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 159** |
| Ventana | **abre 2026-11-26 13:44 CDMX** (cierre de 158) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 23 h 01 (157) · **77 h 09 (158)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-27.html` (viernes 27-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **2** (26 y 27; la plantilla de 158 trae **4**: reemplazo 4→2 y asertar) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 159 hereda** y **Deuda de método (ARGOS 158)**.
3. `reports/argos-2026-11-26-fuentes.md` §2, §3, §5, §7 y §10.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-22`, `-23`, `-26`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola · (4) **una búsqueda de desarrollo por cada rojo** · (5) borrador · (6) controles R1 en paralelo, R2 en serie · (7) repetición de la triple consulta antes de R2.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 158

| Trampa | Control |
|---|---|
| **Hecho reclasificado por titulares del día siguiente** | Santa Ana: «cinco hombres muertos» (23) → «disputa interna» y captura (24) |
| **Primera publicación anterior a la que trae la ola** | Ixtapaluca: ola con ruta del 25; Cúspide y Seuno 2026/11/23 |
| **Tres cifras del mismo despliegue** | Peribán–Jilotlán: Defensa 10/33 · boletín 11/43 · Peribán 8/20 |
| **Superlativo falso** | «la ventana más larga de la serie» (10-07: 320 h 34) |
| **Pista del recall de otro mes** | Cuarto Poder «Tres muertos y heridos…» = 18-sep |
| **Visto con fecha errónea en la edición anterior** | Periférico Norte: viernes 20, no domingo 22 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-158.py` (copia a `datos-argos-159.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA` (fecha), `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 13:44 DEL 26, ES DE LA VENTANA DE ARGOS 158…»), `DIA`, `FED17`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (**ARGOS 158 — Reporte Nacional de Seguridad — 2026-11-26**, plantilla `reports/argos-2026-11-26.html`), `WINDOW_DAYS` (la plantilla trae **4**: cambie el reemplazo 2→4 por 4→2 y aserte una sola «WINDOW_DAYS = 2;») y las listas de fichas por página. Si no hay recuperaciones, retire `co6`, `rows_rec` y su página. El default de `ARGOS_CONSULTA` es «__CONSULTA__».
- Móvil: `python3 tools/gen-movil.py 159 <FECHA> 158 2026-11-26 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-26 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 160. Commit y push.
