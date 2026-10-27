# ORDEN DE ARRANQUE — ARGOS 143

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 143 hereda» y «Deuda de método (ARGOS 142)»), `reports/argos-2026-10-27-fuentes.md` (ARGOS 142) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-143.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-27` (ARGOS 142) y **240 archivos** en `reports/`. 139 en `claude/argos-139-qe9f01`; 140, en `claude/argos-140`; 141, en `claude/argos-141-nacional-kh5fj6`; 142, en `claude/argos-criminal-intelligence-otiawj` (cada una encima de la anterior). Ninguna está en `main`: las cinco fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 143** |
| Ventana | **abre 2026-10-27 08:45 CDMX** (cierre de 142) y cierra a la hora real de arranque |
| Serie | 27 h 17 (139) · 93 h 22 (140) · 24 h 52 (141) · **24 h 08 (142)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-DD.html` (fecha del arranque, sin sufijo) · `WINDOW_DAYS` = fechas de calendario de la ventana |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 143 hereda** y **Deuda de método (ARGOS 142)**.
3. `reports/argos-2026-10-27-fuentes.md` §5-§7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-20`, `-21`, `-25`, `-26` y `-27`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30. Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día ANTES de la ola · (3) ola, con las pistas del recall en los encargos · (4) **búsqueda de ruta fechada de todo 🔴 que llegue sin ella** · (5) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 142

| Trampa | Control |
|---|---|
| **Rojo sin ruta fechada en vistos** | Queréndaro y Tumbisca: Quadratín sin fecha; las rutas del 26 estaban en Grupo Marmor y Medianews |
| **Hora «por titular» que es del cuerpo** | Tecate: «tarde» y 17:47 solo en el cuerpo de Zeta; Milenio dice «noche» |
| **Cantidad implícita** | «les aseguran AR-15» no dice cuántos: la cantidad es solo por resumen |
| **Mismo punto, otro día** | SLP «a la altura de Tierra Blanca»: 20-oct (ARG-139-009) y 26-oct (ARG-142-008) |
| **Hallazgo del mismo colectivo y zona** | Cutzato 28-sep (ARG-125-036) y 26-oct (ARG-142-005): separados por fecha de publicación |
| **Año trampa del boletín federal** | «24, 25 y 26 de octubre» devuelve el agregado de 2025 |
| **Sello horario no CDMX** | Notimex `…20261027144220`: probablemente UTC |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-142.py` (copia a `datos-argos-143.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, la ventana del panorama, las aserciones y el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-27.html`, «ARGOS 142 — … — 2026-10-27»). `WINDOW_DAYS` ya es 2 y la aserción lo espera.
- Móvil: `python3 tools/gen-movil.py 143 <FECHA> 142 2026-10-27 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-27 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`; la ronda 2 en serie.
- Encargos con fecha: **Tulantepec, 28-oct 17:00** (por resumen).
