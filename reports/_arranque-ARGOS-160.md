# ORDEN DE ARRANQUE — ARGOS 160

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 160 hereda» y «Deuda de método (ARGOS 159)»), `reports/argos-2026-11-27-fuentes.md` (ARGOS 159) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-160.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-27` (ARGOS 159) y **359 archivos** en `reports/` (incluida la orden de 160). 139 a 159 viven fuera de `main`; **159 en `claude/argos-159-criminal-intelligence-44b282`** (encima de `claude/argos-158-criminal-intelligence-0wpevh`). Todas las fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 160** |
| Ventana | **abre 2026-11-27 08:03 CDMX** (cierre de 159) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 77 h 09 (158) · **18 h 19 (159)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-28.html` (sábado 28-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **2** (27 y 28; la plantilla de 159 ya trae **2**: sin reemplazo, asertar una sola) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 160 hereda** y **Deuda de método (ARGOS 159)**.
3. `reports/argos-2026-11-27-fuentes.md` §2, §3, §5, §7, §8 y §10.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-23`, `-26`, `-27`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola · (4) **una búsqueda de desarrollo por cada rojo** y **una búsqueda «municipio + fecha en la ruta» del medio local por cada rojo urbano** · (5) borrador · (6) controles R1 en paralelo, R2 en serie · (7) repetición de la triple consulta antes de R2.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 159

| Trampa | Control |
|---|---|
| **Homicidios del mismo municipio que la ola no ve** | Mazatlán 26-nov: Cerritos, Prados del Sol y Chulavista, hallados por IDs contiguos de Luz Noticias (316912, 316930, 316931) |
| **Herido que muere el mismo día** | Yonke de Chihuahua: «3 muertos y 1 herido» → «Muere único sobreviviente» (El Diario de Chihuahua 2026/nov/25) |
| **Título de comunicado atribuido a un medio** | Tamazula: «Marina y SSPC detienen a cuatro…» era el listado de gob.mx/sspc, no La Nigua |
| **Fe de erratas sobre lo no publicado** | San Fernando y Valle Soleado eran vistos de equipos.md de 158 |
| **Señuelo de año en el boletín federal** | «acciones relevantes del 26 de noviembre» = 2025 (Milenio, Heraldo, Tallapolítica) |
| **Liveblog con día en el titular** | Azteca Guerrero «…hoy lunes 23 de noviembre 2026» (Chilpancingo–Chichihualco) |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-159.py` (copia a `datos-argos-160.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA` (fecha), `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 08:03 DEL 27, ES DE LA VENTANA DE ARGOS 159…»), `DIA`, `FED17`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (**ARGOS 159 — Reporte Nacional de Seguridad — 2026-11-27**, plantilla `reports/argos-2026-11-27.html`), `WINDOW_DAYS` (la plantilla trae **2**; si la ventana toca dos días, sin reemplazo y aserte una sola «WINDOW_DAYS = 2;») y las listas de fichas por página. Si no hay recuperaciones, retire `co6`, `rows_rec` y su página. El default de `ARGOS_CONSULTA` es «__CONSULTA__».
- Móvil: `python3 tools/gen-movil.py 160 <FECHA> 159 2026-11-27 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-27 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 161. Commit y push.
