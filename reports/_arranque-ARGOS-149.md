# ORDEN DE ARRANQUE — ARGOS 149

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 149 hereda» y «Deuda de método (ARGOS 148)»), `reports/argos-2026-11-06-fuentes.md` (ARGOS 148) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-149.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-06` (ARGOS 148) y **282** archivos en `reports/`. 139 a 148 viven fuera de `main`; **148 en `claude/argos-148`** (encima de `claude/argos-147`). Las diez fusiones deben ser *fast-forward*. Sin decisiones pendientes del destinatario.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 149** |
| Ventana | **abre 2026-11-06 07:30 CDMX** (cierre de 148) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 26 h 50 (147) · **21 h 48 (148)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-09.html` (lunes 9-nov) · `WINDOW_DAYS` = **4** (6, 7, 8 y 9; la plantilla de 148 trae 2) · ventana de ≈73 h con fin de semana completo; la orden fechada el 7-nov no se ejecutó |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**; detenidos solo con cifra de autoridad).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 149 hereda** y **Deuda de método (ARGOS 148)**.
3. `reports/argos-2026-11-06-fuentes.md` §2, §3, §5, §7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-29`, `-31`, `2026-11-04`, `-05` y `-06`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola, con **búsqueda por topónimo exacto y día para todo rojo sin ruta** · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 147

| Trampa | Control |
|---|---|
| **Hecho del día de apertura con hora de madrugada** | Coscomatepec, megaoperativo, Coto Residencial Atlántico, Los Huizaches: ventana anterior por la hora |
| **Cifra de republicación tomada como titular** | Michoacán 710 cartuchos y 10 AEI: solo resumen |
| **Aseguramiento repetido con días de diferencia** | Tacámbaro (5-nov) = Pedernales (3-nov), mismas cifras |
| **Cargo de la víctima** | Pachuca: policía estatal / director / exdirector |
| **Segundo abatido por titular del día siguiente** | Naucalpan: Infobae 2026/11/06 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-148.py` (copia a `datos-argos-149.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (07:30 del 6), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla `reports/argos-2026-11-06.html`, «ARGOS 148 — … — 2026-11-06»), `WINDOW_DAYS` (2 → 4) y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 149 <FECHA> 148 2026-11-06 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-06 <FECHA>` (solo escritorio; el móvil lo valida `gen-movil.py`).
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
