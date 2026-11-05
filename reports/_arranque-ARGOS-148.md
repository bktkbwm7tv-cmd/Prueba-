# ORDEN DE ARRANQUE — ARGOS 148

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 148 hereda» y «Deuda de método (ARGOS 147)»), `reports/argos-2026-11-05-fuentes.md` (ARGOS 147) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-147.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-05` (ARGOS 147) y **275** archivos en `reports/`. 139 a 147 viven fuera de `main`; **147 en `claude/argos-147`** (encima de `claude/argos-146`). Las nueve fusiones deben ser *fast-forward*. Plantear la **decisión pendiente (a) del destinatario** (rojos sin ruta fechada) antes de la ola.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 148** |
| Ventana | **abre 2026-11-05 09:42 CDMX** (cierre de 147) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 91 h 38 (146) · **26 h 50 (147)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-<FECHA>.html` · `WINDOW_DAYS` según las fechas de calendario que toque la ventana (la plantilla de 147 trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**; detenidos solo con cifra de autoridad).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 148 hereda** y **Deuda de método (ARGOS 147)**.
3. `reports/argos-2026-11-05-fuentes.md` §2, §3, §5, §7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-28`, `-29`, `-31`, `2026-11-04` y `2026-11-05`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola, con **búsqueda por topónimo exacto y día para todo rojo sin ruta** · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 147

| Trampa | Control |
|---|---|
| **Hora por resumen anterior a la apertura** | Coto Premier: «mañana» en el equipo, «6:34» en una nota de contexto → REC. Buscar la hora también en notas de contexto del mismo día |
| **«Sin ruta» desigual** | Tres homicidios de Sinaloa con ruta 2026-11-04 del mismo medio que otro fichado: buscar el topónimo en el medio que ya dio ruta |
| **Titular agregado** | Guerrero «siete en varios municipios»: el reparto por municipio solo por resumen; «cinco municipios», no reencontrado |
| **Hallazgo frente a ataque** | Chilpancingo: los titulares dicen «hallan dos cuerpos»: fijar el tipo de hecho por titular |
| **Seguimiento sin dato nuevo** | Orizaba repetía 146: fuera del cartelón |
| **Hora de «Consulta» planeada** | Escribirla después de la última búsqueda |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-147.py` (copia a `datos-argos-148.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (09:42 del 5), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla `reports/argos-2026-11-05.html`, «ARGOS 147 — … — 2026-11-05»), el reemplazo de `WINDOW_DAYS` (la plantilla trae 2) y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 148 <FECHA> 147 2026-11-05 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-05 <FECHA>` (solo escritorio; el móvil lo valida `gen-movil.py`).
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
