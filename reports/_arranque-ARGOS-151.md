# ORDEN DE ARRANQUE — ARGOS 151

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 151 hereda» y «Deuda de método (ARGOS 150)»), `reports/argos-2026-11-14-fuentes.md` (ARGOS 150) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-151.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-14` (ARGOS 150) y **296** archivos en `reports/`. 139 a 150 viven fuera de `main`; **150 en `claude/argos-150-nacional-61ng7x`** (encima de `claude/zealous-mendel-baacj5`). Las doce fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 151** |
| Ventana | **abre 2026-11-14 10:09 CDMX** (cierre de 150) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 80 h 37 (149) · **114 h 02 (150)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-<FECHA>.html` · `WINDOW_DAYS` = fechas de calendario de la ventana (la plantilla de 150 trae 6) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 151 hereda** y **Deuda de método (ARGOS 150)**.
3. `reports/argos-2026-11-14-fuentes.md` §3, §4, §5, §7 y §10.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-11-05`, `-06`, `-09`, `-14` y `-04`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal (empezando por el 13 y el 14) y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 150

| Trampa | Control |
|---|---|
| **«Por titular» que era resumen** | Silao 13 armas; Zitácuaro herido: titular literal entre comillas |
| **Falsa fuente única** | San Juan del Río: búsqueda por topónimo exacto |
| **Abatido «no oficial» con tres titulares** | Temascatío |
| **Nombre propio dentro de una cita** | Tuxpan: se omite |
| **Conclusión con intervalo de días no sostenido** | Juchitán, Tuxpan: sin número si las fechas están contradichas |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-150.py` (copia a `datos-argos-151.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (10:09 del 14), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla `reports/argos-2026-11-14.html`, «ARGOS 150 — … — 2026-11-14»), `WINDOW_DAYS` y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 151 <FECHA> 150 2026-11-14 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-14 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
