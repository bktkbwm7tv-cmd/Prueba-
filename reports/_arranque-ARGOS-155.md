# ORDEN DE ARRANQUE — ARGOS 155

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 155 hereda» y «Deuda de método (ARGOS 154)»), `reports/argos-2026-11-18-fuentes.md` (ARGOS 154) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-155.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-18` (ARGOS 154) y **324 archivos** en `reports/` (incluida la orden de 155). 139 a 154 viven fuera de `main`; **154 en `claude/argos-154-criminal-intelligence-g2kqhw`** (encima de `claude/argos-153-criminal-intelligence-6knrt6`). Las dieciséis fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 155** |
| Ventana | **abre 2026-11-18 12:32 CDMX** (cierre de 154) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 25 h 04 (153) · **24 h 58 (154)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-19.html` (jueves 19-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **2** (18 y 19; la plantilla de 154 ya trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 155 hereda** y **Deuda de método (ARGOS 154)**.
3. `reports/argos-2026-11-18-fuentes.md` §3, §5, §7 y §8.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-15`, `-16`, `-17`, `-18`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal (13 al 18) y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo (**a procedencia R1, los informes de equipo y la lista de titulares ya vistos por el coordinador**), R2 en serie · (6) repetición de la triple consulta antes de R2.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 154

| Trampa | Control |
|---|---|
| **R1 sin titulares del coordinador** | Declaró «no localizado» lo ya visto (PorEsto Cancún, Quinto Poder, Red Metropolitana…): entregarle la lista |
| **Detención ya difundida** | Cajeme: detenciones del 17 ya publicadas el 12 y 13-nov → seguimiento, no ficha |
| **Fecha del hecho en boletín estatal** | Acámbaro: publicado el 18-nov, hecho del 17-oct por resumen → visto |
| **Encargo con entidad equivocada** | `-152-005` es Mazatlán (col. Pueblo Nuevo), no Guanajuato |
| **Titular parafraseado** | La Silla Rota (Taxco): «comando ataca», no «hombres armados atacan» |
| **Balances** | «Ataques armados a negocios en Culiacán dejan tres muertos»: balance de dos hechos, no fuente |
| **Duplicado en vistos** | Escuinapa ya era `ARG-149-021`; Aldama y Chilapa ya eran vistos de 153 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-154.py` (copia a `datos-argos-155.py`): cambie `NUM`, `FECHA`, `HORA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 12:32 DEL 18, ES DE LA VENTANA DE ARGOS 154…»), el default de `ARGOS_CONSULTA` («13:04» → «__CONSULTA__»), `FED17`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (pon **ARGOS 154 — Reporte Nacional de Seguridad — 2026-11-18**, plantilla `reports/argos-2026-11-18.html`), `WINDOW_DAYS` (la plantilla trae 2) y las listas de fichas por página. Para `-REC-`, recupere `co4` y `rows_rec` del generador de 152.
- Móvil: `python3 tools/gen-movil.py 155 <FECHA> 154 2026-11-18 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador (solo escritorio): `node tools/validar.js reports/argos-<FECHA>.html 2026-11-18 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 156. Commit y push.
