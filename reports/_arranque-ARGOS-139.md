# ORDEN DE ARRANQUE — ARGOS 139

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 138 (corte 2026-10-20 07:06). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-20-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-139.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-20` (ARGOS 138) y **210 archivos** en `reports/`
(203 + cinco de la edición + `_arranque-ARGOS-139.md` + `_ordenes-ARGOS-139.txt`). ARGOS 129 a 138 viven en `claude/argos-129` … `-138`,
encadenadas; fast-forward desde `b0558a3`. Abrir `claude/argos-139` antes de fusionar; si un merge no es fast-forward, parar y avisar.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 139** |
| Ventana | **abre 2026-10-20 07:06 CDMX** y cierra a la hora real de arranque |
| Serie | 28 h 18 (134) · 21 h 54 (135) · 23 h 06 (136) · 26 h 31 (137) · **20 h 01 (138)** |
| Densidad | 0,67 · 0,59 · 0,39 · 0,68 · **0,65** — 138: **11 de 13 con marca de frontera** y 2 sin ruta con fecha |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 138**, **Abiertos que ARGOS 139 hereda**, **Deuda de método (ARGOS 138)**.
3. `reports/argos-2026-10-20-fuentes.md` — §3, §5, §6, §7, §8, §9, §10, §12.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas — cotejo por topónimo antes de fichar, también cada `-REC-`.

## BLOQUE 3 — PRESUPUESTO

Tope de 200 por turno: control 2 · ola ~160 · coordinador ~10 · `procedencia-cifras` ~30 (segunda ronda sin búsquedas). 138 gastó 2 + 158 + 8 + 30 = 198.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN ARGOS 138

| Trampa | Control |
|---|---|
| **Pistas heredadas sin fecha** | Copanatoyac era de 2025 y Luis Moya de agosto: fechar la pista antes de buscar el hecho |
| **Ordinal en un titular** | «Segundo homicidio de una mujer este lunes» anunciaba otro hecho que la ola no trajo: buscar siempre el primero |
| **Títulos de otro hecho en el mismo municipio** | Juchitán: «menor de 12 años» era de julio; no contar fuentes que no se han atado al hecho |
| **Hora por resumen en la apertura** | Monterrey ~11:00 con apertura 11:05: marca, no exclusión; taxista ~06:00: ventana anterior |
| **Recuperar verdes de ventana anterior** | Solo el alto impacto se recupera con ficha; el resto, vistos (Jiquilpan) |
| **Totales escritos a mano** | 6 muertos con 7 en fichas: derivar del arreglo |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-138.py` (páginas por ARG-ID con `pg(...)`; panorama ordenado por color; `cual=True` para armamento cualitativo; `fecha_txt` cuando la ruta solo fija la publicación) y de `reports/argos-2026-10-20.html` (cambiar la línea de `<title>` que reemplaza el generador: ARGOS 138 — 2026-10-20).
- Móvil: `python3 tools/gen-movil.py 139 <FECHA> 138 2026-10-20 <HORA>`. Texto: `gen-texto.py`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-20 <FECHA>`.
- Portada: cinco «SOLICITE A…», solo ARG-ID, sobre hechos distintos de las conclusiones. Valoración solo con ARG-ID. Ningún texto explica un color.
- Controles: dos rondas, veinte pases cada una; informes íntegros en `reports/argos-<FECHA>-equipos.md`.
