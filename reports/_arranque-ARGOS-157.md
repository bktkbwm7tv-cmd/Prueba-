# ORDEN DE ARRANQUE — ARGOS 157

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 157 hereda» y «Deuda de método (ARGOS 156)»), `reports/argos-2026-11-22-fuentes.md` (ARGOS 156) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-157.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-22` (ARGOS 156) y **338 archivos** en `reports/` (incluida la orden de 157). 139 a 156 viven fuera de `main`; **156 en `claude/argos-156-criminal-intelligence-kx9pts`** (encima de `claude/argos-154-security-report-etkefe`). Las dieciocho fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 157** |
| Ventana | **abre 2026-11-22 09:34 CDMX** (cierre de 156) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 30 h 08 (155) · **62 h 54 (156, ventana larga)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-AAAA-MM-DD.html` con la fecha de arranque · `WINDOW_DAYS` = número de fechas de calendario que toque la ventana (la plantilla de 156 trae **4**: reemplazar y asertar) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 157 hereda** y **Deuda de método (ARGOS 156)**.
3. `reports/argos-2026-11-22-fuentes.md` §2, §4, §5, §7 y §10.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-18`, `-19`, `-22`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta antes de R2.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 156

| Trampa | Control |
|---|---|
| **Cuerpos que son abatidos** | Mojolo: 3 cuerpos = 3 de los 7 abatidos de Guasave (Infobae 2026/11/21) |
| **Titular de otro año** | Excélsior «Emboscada en Guasave destaca en reporte del Gabinete de Seguridad»: 2025 |
| **Pista del recall con fecha falsa** | Acapulco km 21 (3-nov) · «dos agentes federales muertos, Harfuch» en Veracruz (Omealca, 5-sep) |
| **Hallazgo anterior publicado en ventana** | Chilapa–Atlixtac: jornada del miércoles 18 por resumen |
| **Medio con apariencia oficial** | Guanajuato Informa: no acreditado como oficial; se cuenta regional |
| **Agregado de vistos viejos** | Nuevo Laredo, 16 armas (La Región 2026/11/22) = vistos de 150 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-156.py` (copia a `datos-argos-157.py`): cambie `NUM`, `FECHA`, `HORA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 09:34 DEL 22, ES DE LA VENTANA DE ARGOS 156…»), `FED17`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (pon **ARGOS 156 — Reporte Nacional de Seguridad — 2026-11-22**, plantilla `reports/argos-2026-11-22.html`; en `datos-argos-156.py` dice ARGOS 155 — … — 2026-11-19), `WINDOW_DAYS` (la plantilla trae **4**: reemplazar por el de 157 y asertar; el generador de 156 asierta `WINDOW_DAYS = 2;` en la plantilla de 155: cambie esa aserción) y las listas de fichas por página. El default de `ARGOS_CONSULTA` ya es «__CONSULTA__». Para `-REC-`, recupere `co4` y `rows_rec` del generador de 152.
- Móvil: `python3 tools/gen-movil.py 157 <FECHA> 156 2026-11-22 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador (solo escritorio): `node tools/validar.js reports/argos-<FECHA>.html 2026-11-22 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 158. Commit y push.
