# ORDEN DE ARRANQUE — ARGOS 139 (rehecha tras la versión retirada)

Escrita el 20-oct, después de que el destinatario **retirara la versión de 43 min de ARGOS 139** (ventana 07:06 → 07:49, sin hechos propios)
y ordenara rehacerla el **21-oct a las 07:00**. La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md`,
`reports/argos-2026-10-20-fuentes.md` (ARGOS 138) y los insumos `reports/_argos-139-retirado-fuentes.md` y `-equipos.md`.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-139.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-20` (ARGOS 138) y **212 archivos** en `reports/`
(210 + los dos insumos retirados). Ramas `claude/argos-129` … `-138` y `claude/argos-139-9anrf5`, encadenadas; o `main` si el PR #15 ya se fusionó.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 139** |
| Ventana | **abre 2026-10-20 07:06 CDMX** y cierra a la hora real de arranque del 21-oct (~24 h) |
| Serie | 21 h 54 (135) · 23 h 06 (136) · 26 h 31 (137) · **20 h 01 (138)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-21.html` (sin sufijo) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (nueva regla: las acciones se redactan como **solicitud**, nunca exigencia).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 139 hereda** (de 138) y **Versión retirada de ARGOS 139**.
3. `reports/_argos-139-retirado-fuentes.md` — §3 (cobertura), §5 (encargos), §6 (arbitrajes), §10 (controles): **insumo, no fuente**.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas.

## BLOQUE 3 — PRESUPUESTO

Tope de 200 por turno: control 2 · ola ~160 · coordinador ~10 · `procedencia-cifras` ~30. Los encargos ya resueltos en la versión retirada no se repiten.

## BLOQUE 4 — TRAMPAS VERIFICADAS

| Trampa | Control |
|---|---|
| **Día de la denuncia ≠ día del hecho** | Río Bravo: «el sábado» era el 10, no el 17 |
| **Agregados de medios** | El Independiente 2026/10/19 recicla hechos del 13-oct |
| **Vistos ya publicados** | Villa de Seris era `ARG-137-018`; Cotija, ya en 138 |
| **Conclusiones** | No repetir la de la edición anterior ni el panorama; declarar el criterio del patrón y todo conteo como cálculo propio |
| **Marca «Consulta»** | Hora real de la última búsqueda |
| **Ventana corta** | 43 min = 0 hechos: avisar antes de la ola si dura menos de ~12 h |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-139.py`: cambie `FECHA`, `HORA`, `CONSULTA`, `DUR`, la ventana del panorama, las aserciones y el `<title>` que reemplaza; el archivo de salida es `argos-2026-10-21.html`. La ficha de Río Bravo ya pasó dos rondas de control: reverifique y renumere.
- Móvil: `python3 tools/gen-movil.py 139 2026-10-21 138 2026-10-20 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-2026-10-21.html 2026-10-20 2026-10-21`.
- Controles: dos rondas, veinte pases cada una; informes íntegros en `reports/argos-2026-10-21-equipos.md`.
