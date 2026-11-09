# ORDEN DE ARRANQUE — ARGOS 150

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 150 hereda» y «Deuda de método (ARGOS 149)»), `reports/argos-2026-11-09-fuentes.md` (ARGOS 149) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-150.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-09` (ARGOS 149) y **289** archivos en `reports/`. 139 a 149 viven fuera de `main`; **149 en `claude/zealous-mendel-baacj5`** (encima de `claude/argos-148`). Las once fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 150** |
| Ventana | **abre 2026-11-09 16:07 CDMX** (cierre de 149, hora del «Procede») y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 21 h 48 (148) · **80 h 37 (149)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-10.html` (martes 10-nov) · `WINDOW_DAYS` = **2** (9 y 10; la plantilla de 149 trae 4) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 150 hereda** y **Deuda de método (ARGOS 149)**.
3. `reports/argos-2026-11-09-fuentes.md` §3, §4, §5, §7 y §10.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-31`, `2026-11-04`, `-05`, `-06` y `-09`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 149

| Trampa | Control |
|---|---|
| **Anuncio federal del día de apertura = operativo del día anterior** | Tlachichuca: boletín del 5-nov |
| **Agregado federal solo por título y un republicador** | Milenio 6-7-8 nov |
| **Operativo con enfrentamiento fusionado en un verde** | Zapopan: dos fichas |
| **Pista roja sin causa** | Cuerámaro: arma de cargo |
| **Heridos «contradichos» que son secuencia** | Valtierrilla: 3 lesionados, uno murió |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-149.py` (copia a `datos-argos-150.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (16:07 del 9), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla `reports/argos-2026-11-09.html`, «ARGOS 149 — … — 2026-11-09»), `WINDOW_DAYS` (4 → 2) y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 150 <FECHA> 149 2026-11-09 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-09 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
