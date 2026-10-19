# ORDEN DE ARRANQUE — ARGOS 138

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 137 (corte 2026-10-19 11:05). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-19-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-138.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-19` (ARGOS 137) y **203 archivos** en `reports/`
(196 + cinco de la edición + `_arranque-ARGOS-138.md` + `_ordenes-ARGOS-138.txt`). ARGOS 129 a 137 viven en `claude/argos-129` … `-137`,
encadenadas; fast-forward desde `b0558a3`. En 133 a 137 el clon arrancó con HEAD suelto en `60f2777`: abrir `claude/argos-138` antes de fusionar.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 138** |
| Ventana | **abre 2026-10-19 11:05 CDMX** y cierra a la hora real de arranque |
| Serie | 22 h 57 (133) · 28 h 18 (134) · 21 h 54 (135) · 23 h 06 (136) · **26 h 31 (137)** |
| Densidad | 0,48 · 0,67 · 0,59 · 0,39 · **0,68** — 137: **11 de 18 con marca de frontera** y otros 6 sin ruta con fecha |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 137**, **Abiertos que ARGOS 138 hereda**, **Deuda de método (ARGOS 137)**.
3. `reports/argos-2026-10-19-fuentes.md` — §3, §5, §7, §8, §9, §13, §15.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas — `grep` por topónimo antes de fichar, también cada `-REC-`.

## BLOQUE 3 — PRESUPUESTO

Tope de 200 por turno: control 2 · ola ~160 · coordinador ~10 · `procedencia-cifras` ~30 (segunda ronda sin búsquedas). 137 gastó 2 + 159 + 10 + 29 = 200.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN ARGOS 137

| Trampa | Control |
|---|---|
| **Rojos del lunes por la mañana fuera de la ola** | Tulancingo salió de la búsqueda de cierre; Tlajomulco, de «AJENOS». Mantener ambas |
| **Agregados de medios con muertos de varios hechos** | Mazatlán «tarde violenta»: posible duplicado de una ficha; no se fichan agregados |
| **Persona ya contada en una edición previa** | El exfiscal: una segunda detención es seguimiento, no hecho nuevo |
| **Boletín federal de varios días** | Sus renglones son eventos anteriores publicados durante el corte; fuera del semáforo |
| **Topónimos homónimos entre estados** | Juchitán (Gro./Oax.): fijar la entidad por el medio regional |
| **Conclusiones contra la edición anterior solamente** | Salamanca omitió `ARG-133-002`: cotejar contra el índice |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-137.py` (campos `integra` y `nd` en `ARM`; `R` admite ventanas anteriores en verde) y de `reports/argos-2026-10-19.html` (cambiar la línea de `<title>` que reemplaza el generador: ARGOS 137 — 2026-10-19).
- Móvil: `python3 tools/gen-movil.py 138 <FECHA> 137 2026-10-19 <HORA>` (emite ya las filas de armamento sin ficha). Texto: `gen-texto.py`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-19 <FECHA>`.
- Portada: cinco «SOLICITE A…», solo ARG-ID, sobre hechos distintos de las conclusiones. Valoración solo con ARG-ID.
- Controles: dos rondas, veinte pases cada una; informes íntegros en `reports/argos-<FECHA>-equipos.md`.
