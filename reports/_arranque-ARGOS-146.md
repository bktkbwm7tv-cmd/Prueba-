# ORDEN DE ARRANQUE — ARGOS 146

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 146 hereda» y «Deuda de método (ARGOS 145)»), `reports/argos-2026-10-31-fuentes.md` (ARGOS 145) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-146.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-31` (ARGOS 145) y el número de archivos de `reports/` que fija la orden. 139 a 145 viven fuera de `main`; **145 en `claude/argos-145`** (encima de `claude/argos-144`). Las siete fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 146** |
| Ventana | **abre 2026-10-31 11:14 CDMX** (cierre de 145) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 27 h 08 (144) · **47 h 38 (145)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-<fecha de arranque>.html` · `WINDOW_DAYS` = fechas de calendario de la ventana (la plantilla de 145 trae **3**) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**; detenidos solo con cifra de autoridad).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 146 hereda** y **Deuda de método (ARGOS 145)**.
3. `reports/argos-2026-10-31-fuentes.md` §5-§7 y §13.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-26`, `-27`, `-28`, `-29` y `-31`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola, con «instalaciones / sede» y «bloqueos» · (3) ola · (4) **los rojos sin ruta fechada NO entran al borrador**: se encargan a la R1 de procedencia · (5) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 145

| Trampa | Control |
|---|---|
| **Rojo sin ruta fechada en el borrador** | Cancún y Valle de Chalco: fichas del primer borrador, retiradas en R1 |
| **Hecho «nuevo» que es desarrollo de uno publicado** | Matamoros: las víctimas de los bloqueos de ARG-144-008 → recuperación de la víctima, no ficha propia |
| **Mañana del día de apertura** | Matamoros (~11:00), Mazatlán (~11:00), Coatzacoalcos («mañana»): horas por resumen → recuperaciones |
| **Detenidos por titular de medios** | Iztapalapa (3, titulares sin fecha): CLAUDE.md exige cifra de autoridad → `n/d` |
| **Fuente única que resulta contradicha** | Valle de Chalco: la búsqueda por topónimo trajo 1.ª frente a 2.ª Secc., 2 frente a 1 muertos |
| **Saldo contradicho que decide el color** | Pénjamo: AM 2 muertos / Correo 1 muerto y 1 herido → 🟡 hasta arbitrar |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-145.py` (copia a `datos-argos-146.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (hora de apertura 11:14 del 31), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla `reports/argos-2026-10-31.html`, «ARGOS 145 — … — 2026-10-31»), el reemplazo de `WINDOW_DAYS` (la plantilla trae 3) y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 146 <FECHA> 145 2026-10-31 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-31 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`; la ronda 2 en serie.
