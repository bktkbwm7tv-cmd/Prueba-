# ORDEN DE ARRANQUE — ARGOS 142

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 142 hereda» y «Deuda de método (ARGOS 141)»), `reports/argos-2026-10-26-fuentes.md` (ARGOS 141) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-142.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-26` (ARGOS 141) y **233 archivos** en `reports/`. ARGOS 139 vive en `claude/argos-139-qe9f01`; 140, en `claude/argos-140`; 141, en `claude/argos-141-nacional-kh5fj6` (cada una encima de la anterior). Ninguna está en `main`: las cuatro fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 142** |
| Ventana | **abre 2026-10-26 08:37 CDMX** (cierre de 141) y cierra a la hora real de arranque (ver la lección del «Procede») |
| Serie | 20 h 01 (138) · 27 h 17 (139) · 93 h 22 (140) · **24 h 52 (141)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-DD.html` (fecha del arranque, sin sufijo) · `WINDOW_DAYS` = fechas de calendario de la ventana |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 142 hereda** y **Deuda de método (ARGOS 141)**.
3. `reports/argos-2026-10-26-fuentes.md` §5-§7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-19` a `-21`, `-25` y `-26`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30. Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) **triple consulta federal y recall nacional por día ANTES de la ola** · (3) ola, con las pistas del recall en los encargos · (4) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 141

| Trampa | Control |
|---|---|
| **Hora posterior al cierre** | Tehuacán: rutas del 26 sin hora; cinco resúmenes en 9:00-10:00 → hecho de la edición siguiente |
| **Agregado federal de fin de semana** | «23, 24 y 25-oct»: ninguna acción tiene día; solo entra la que tiene nota propia fechada (Los Tlacos) |
| **Titular homónimo de otro mes** | Cosoleacaque «2 muertos y mujer herida» (Milenio, sin fecha) era de febrero |
| **Colonia distinta, mismo municipio** | Pénjamo «zona centro» (Milenio) ≠ col. Lázaro Cárdenas |
| **Atribución de *slug* a otro caso** | «prisión preventiva oficiosa» de Crónica de Xalapa era de Amatlán |
| **Año trampa** | Coicoyán (2025), Laguna de Canachi (2024), Tehuitzingo diez muertos (mayo de 2026) |
| **Conclusión que olvida un deslinde propio** | Pénjamo: «tercer ataque» cuando la ficha deslindaba un cuarto |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-141.py` (copia a `datos-argos-142.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-26.html`, «ARGOS 141 — … — 2026-10-26») y la sustitución de `WINDOW_DAYS` (la plantilla trae **2**; el script de 141 espera `WINDOW_DAYS = 5;` en su plantilla: ajuste la aserción).
- Móvil: `python3 tools/gen-movil.py 142 <FECHA> 141 2026-10-26 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-26 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`; la ronda 2 en serie.
- Encargos con fecha: **Tulantepec, 28-oct 17:00** (por resumen).
