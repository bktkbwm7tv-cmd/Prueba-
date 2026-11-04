# ORDEN DE ARRANQUE — ARGOS 147

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 147 hereda» y «Deuda de método (ARGOS 146)»), `reports/argos-2026-11-04-fuentes.md` (ARGOS 146) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-147.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-04` (ARGOS 146) y **268** archivos en `reports/`. 139 a 146 viven fuera de `main`; **146 en `claude/argos-146`** (encima de `claude/argos-145`). Las ocho fusiones deben ser *fast-forward*. Plantear las **decisiones pendientes del destinatario** (cinco) antes de la ola.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 147** |
| Ventana | **abre 2026-11-04 06:52 CDMX** (cierre de 146) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 47 h 38 (145) · **91 h 38 (146)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-<FECHA>.html` · `WINDOW_DAYS` según las fechas de calendario que toque la ventana (la plantilla de 146 trae 5) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**; detenidos solo con cifra de autoridad).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 147 hereda** y **Deuda de método (ARGOS 146)**.
3. `reports/argos-2026-11-04-fuentes.md` §2, §3, §5, §7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-27`, `-28`, `-29`, `-31` y `2026-11-04`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día antes de la ola · (3) ola, con **búsqueda por topónimo exacto y día para todo rojo sin ruta** · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 146

| Trampa | Control |
|---|---|
| **Rojo «sin ruta» que la tenía** | Feria Ganadera: Infobae y Latinus 2026/11/02 — búsqueda por topónimo y día en la ola |
| **Deslinde de memoria** | Miguel Alemán (homónimo de Sinaloa), Texmelucan, Tepito, Nuevo Laredo, Cocula: abrir la línea del grep |
| **Hora solo por resumen el día de apertura** | Ario de Rosales («mañana»): integrar con marca, no recuperar por inferencia |
| **Balance atribuido por el resumen** | Celaya: «Correo, 1 muerto» no existía; «sube a tres» (Noticieros en Línea) |
| **Liveblog con forma de nota** | Tultitlán y Nuevo Laredo: *slug* «hoy-DD»; declarar la forma |
| **Agregado federal de varios días** | 30-oct a 2-nov: no fija día; nada se integra |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-146.py` (copia a `datos-argos-147.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (06:52 del 4), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla `reports/argos-2026-11-04.html`, «ARGOS 146 — … — 2026-11-04»), el reemplazo de `WINDOW_DAYS` (la plantilla trae 5) y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 147 <FECHA> 146 2026-11-04 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-04 <FECHA>` (solo escritorio; el móvil lo valida `gen-movil.py`).
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
