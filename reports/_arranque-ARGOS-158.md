# ORDEN DE ARRANQUE — ARGOS 158

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 158 hereda» y «Deuda de método (ARGOS 157)»), `reports/argos-2026-11-23-fuentes.md` (ARGOS 157) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-158.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-23` (ARGOS 157) y **345 archivos** en `reports/` (incluida la orden de 158). 139 a 157 viven fuera de `main`; **157 en `claude/argos-157-criminal-intelligence-qpwf2b`** (encima de `claude/argos-156-criminal-intelligence-kx9pts`). Las diecinueve fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 158** |
| Ventana | **abre 2026-11-23 08:35 CDMX** (cierre de 157) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 62 h 54 (156, ventana larga) · **23 h 01 (157)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-26.html` (jueves 26-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **4** (23, 24, 25 y 26; la plantilla de 157 trae **2**: reemplazo 2→4 y asertar) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 158 hereda** y **Deuda de método (ARGOS 157)**.
3. `reports/argos-2026-11-23-fuentes.md` §2, §3, §5, §7 y §10.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-19`, `-22`, `-23`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta antes de R2.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 157

| Trampa | Control |
|---|---|
| **Liveblog con ruta de otro día** | Infobae «en-vivo-…-hoy-22-de-noviembre» con ruta 2026/11/23: no fecha ni sostiene los 8 de El Platanito |
| **Cifra marcada «solo por resumen» que estaba en titular** | Lomas de Mazatlán, 90 cartuchos (Luz Noticias 2026-11-22) |
| **Mismo saldo, misma colonia, otro día** | Chilpancingo, col. Del PRI: 1 muerto y 2 heridos en mayo de 2025 (El Sol de Chilpancingo 2025/05/18) y el 11-nov (Coppel) |
| **Emboscada homónima** | Zinapécuaro, «un militar muerto y tres heridos» = BOI de septiembre (ARG-117-REC-001) |
| **«Ocho detenidos» de dos operativos** | Guasave (ARG-156-013) frente a El Platanito (ARG-157-009): «ocho más», sin acreditación de la Defensa |
| **Visto antiguo** | «Michoacán: tres muertos y dos heridos» (Quinta Fuerza) = Ario de Rosales, 21-oct |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-157.py` (copia a `datos-argos-158.py`): cambie `NUM`, `FECHA`, `HORA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 08:35 DEL 23, ES DE LA VENTANA DE ARGOS 157…»), `FED17`, `ARM` (157 trae `ARG-157-ARM-001`: vacíelo o sustitúyalo), la ventana del panorama, las aserciones, el `<title>` que reemplaza (pon **ARGOS 157 — Reporte Nacional de Seguridad — 2026-11-23**, plantilla `reports/argos-2026-11-23.html`), `WINDOW_DAYS` (la plantilla trae **2**: cambie el reemplazo 4→2 por 2→4 y aserte una sola «WINDOW_DAYS = 4;») y las listas de fichas por página. Si no hay recuperaciones, retire `co4`, `rows_rec` y su página. El default de `ARGOS_CONSULTA` ya es «__CONSULTA__».
- Móvil: `python3 tools/gen-movil.py 158 <FECHA> 157 2026-11-23 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador (solo escritorio): `node tools/validar.js reports/argos-<FECHA>.html 2026-11-23 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 159. Commit y push.
