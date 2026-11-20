# ORDEN DE ARRANQUE — ARGOS 156

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 156 hereda» y «Deuda de método (ARGOS 155)»), `reports/argos-2026-11-19-fuentes.md` (ARGOS 155) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-156.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-19` (ARGOS 155) y **331 archivos** en `reports/` (incluida la orden de 156). 139 a 155 viven fuera de `main`; **155 en `claude/argos-154-security-report-etkefe`** (encima de `claude/argos-154-criminal-intelligence-g2kqhw`). Las diecisiete fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 156** |
| Ventana | **abre 2026-11-19 18:40 CDMX** (cierre de 155) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 24 h 58 (154) · **30 h 08 (155)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-20.html` (viernes 20-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **2** (19 y 20; la plantilla de 155 ya trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 156 hereda** y **Deuda de método (ARGOS 155)**.
3. `reports/argos-2026-11-19-fuentes.md` §2, §3, §5, §7 y §8.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-16`, `-17`, `-18`, `-19`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo (a procedencia R1, los informes de equipo y la lista de titulares ya vistos), R2 en serie · (6) repetición de la triple consulta antes de R2.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 155

| Trampa | Control |
|---|---|
| **Fecha de la nota ≠ fecha de la detención** | Cancún y Chihuahua: ruta del 19, detención del 18 por resumen |
| **Saldo de otra ficha sin dos campos** | Tecate «cuádruple homicidio»: no corrige `-150-REC-001` sin Los Encinos/fecha/alias por titular |
| **Deslinde «no figura» falso** | Santa Fe (ARG-145-008) e Ignacio Allende (Acapulco, ARG-136-003) |
| **Homónimo en un titular** | Quadratín «Ataque armado en la Rubén Jaramillo de Uruapan deja 2 muertos»: posible hecho de septiembre |
| **Lanzagranadas mal atribuido** | El del boletín del 17 es de La Yesca (Mesa de Chapalilla), no de Huajicori |
| **Pista del coordinador mal fechada** | Milenio «Asesinan a policía ministerial en Baja California»: es `-152-002` (15-nov), no del jueves 19 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-155.py` (copia a `datos-argos-156.py`): cambie `NUM`, `FECHA`, `HORA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 18:40 DEL 19, ES DE LA VENTANA DE ARGOS 155…»), el default de `ARGOS_CONSULTA` («19:06» → «__CONSULTA__»), `FED17`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (pon **ARGOS 155 — Reporte Nacional de Seguridad — 2026-11-19**, plantilla `reports/argos-2026-11-19.html`), `WINDOW_DAYS` (la plantilla trae 2), las tarjetas de armamento (subtítulos por categoría) y las listas de fichas por página. Para `-REC-`, recupere `co4` y `rows_rec` del generador de 152.
- Móvil: `python3 tools/gen-movil.py 156 <FECHA> 155 2026-11-19 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador (solo escritorio): `node tools/validar.js reports/argos-<FECHA>.html 2026-11-19 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 157. Commit y push.
