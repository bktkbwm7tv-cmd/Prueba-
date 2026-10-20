# ORDEN DE ARRANQUE — ARGOS 140

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 139 (corte 2026-10-20 07:49, segundo del día). La continuidad
vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-20b-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-140.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-20b` (ARGOS 139) y **217 archivos** en `reports/`
(210 + cinco de la edición + `_arranque-ARGOS-140.md` + `_ordenes-ARGOS-140.txt`). ARGOS 129 a 138 viven en `claude/argos-129` … `-138`
y ARGOS 139 en `claude/argos-139-9anrf5`, encadenadas; fast-forward desde `b0558a3`. Si un merge no es fast-forward, parar y avisar.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 140** |
| Ventana | **abre 2026-10-20 07:49 CDMX** y cierra a la hora real de arranque; **si dura menos de ~12 h, avisar antes de la ola** |
| Serie | 21 h 54 (135) · 23 h 06 (136) · 26 h 31 (137) · 20 h 01 (138) · **43 min (139)** |
| Densidad | 0,59 · 0,39 · 0,68 · 0,65 · **0,00** — 139: 0 hechos propios, 1 `-REC-` |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-<FECHA>.html`; el sufijo `b` solo si el corte vuelve a caer el 20-oct |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 139**, **Abiertos que ARGOS 140 hereda**, **Deuda de método (ARGOS 139)**.
3. `reports/argos-2026-10-20b-fuentes.md` — §3, §5, §6, §7, §10, §12.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-17` … `-20`, `-20b`) — cotejo por topónimo.

## BLOQUE 3 — PRESUPUESTO

Tope de 200 por turno: control 2 · ola ~160 · coordinador ~10 · `procedencia-cifras` ~30 (segunda ronda sin búsquedas). 139 gastó 2 + 156 + 7 + 30 = 195.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN ARGOS 139

| Trampa | Control |
|---|---|
| **Día de la denuncia tomado por día del hecho** | Río Bravo: «el sábado» era el 10, no el 17. Fijar qué sábado |
| **Agregados de medios** | El Independiente 2026/10/19 recicla Naucalpan del 13-oct: la fecha de la página no fecha ninguno de sus hechos |
| **Vistos ya publicados** | Villa de Seris era `ARG-137-018`; Cotija ya vista en 138: cotejar también los vistos |
| **Conclusiones repetidas** | No repetir la conclusión de la edición anterior ni el seguimiento del panorama |
| **Marca «Consulta»** | La hora de la última búsqueda, no una estimación (138 escribió 09:30 con commit a las 07:45) |
| **Ventana corta** | 43 min = 0 hechos: avisar antes de gastar la ola |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-139.py` (recuperaciones con `mu`/`he`; totales derivados; `E = []` admitido) y de `reports/argos-2026-10-20b.html` (cambiar la línea de `<title>` que reemplaza el generador: ARGOS 139 — 2026-10-20).
- Móvil: `python3 tools/gen-movil.py 140 <FECHA> 139 2026-10-20b <HORA>`. Texto: `gen-texto.py`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-20 <FECHA>` (ahora cuenta todos los recuadros).
- Portada: cinco «SOLICITE A…», solo ARG-ID, sin compartir ninguno con las conclusiones. Ningún texto explica un color.
- Controles: dos rondas, veinte pases cada una; informes íntegros en `reports/argos-<FECHA>-equipos.md`.
