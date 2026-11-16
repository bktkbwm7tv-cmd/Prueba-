# ORDEN DE ARRANQUE — ARGOS 152

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 152 hereda» y «Deuda de método (ARGOS 151)»), `reports/argos-2026-11-15-fuentes.md` (ARGOS 151) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-152.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-15` (ARGOS 151) y **303** archivos en `reports/` (incluida la orden de 152). 139 a 151 viven fuera de `main`; **151 en `claude/argos-151-nacional-c9xttt`** (encima de `claude/argos-150-nacional-61ng7x`). Las trece fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 152** |
| Ventana | **abre 2026-11-15 10:24 CDMX** (cierre de 151) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 114 h 02 (150) · **24 h 15 (151)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-16.html` (lunes 16-nov) · `WINDOW_DAYS` = **2** (15 y 16; la plantilla de 151 ya trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 152 hereda** y **Deuda de método (ARGOS 151)**.
3. `reports/argos-2026-11-15-fuentes.md` §3, §5, §7 y §10.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-06`, `-09`, `-14`, `-15`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal (agregado 13-15 probable hoy, lunes 16; repartir sus acciones entre 150, 151 y 152 solo con día por ruta o titular) y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 151

| Trampa | Control |
|---|---|
| **Frontera tratada como -REC- por la hora del resumen** | Tepehuacán: con publicación el día de cierre y hora solo por resumen, ficha propia con FRONTERA |
| **«Sin ruta» por falta de hora** | Texhuacán: tenía tres rutas del 14 |
| **Homónimo de topónimo** | Tepehuacán de Guerrero (Hgo.) en búsquedas de Guerrero; El Arenal (Jal. / Tlalnepantla) |
| **Nota sin mes en una -REC-** | Tecate: Uniradio era de julio |
| **Cifra de conclusión sin sumar** | Mazatlán: «seis víctimas» eran siete |
| **Colores explicados en deslindes** | Retirados en R2: van al archivo de fuentes |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-151.py` (copia a `datos-argos-152.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 10:24 DEL 15, ES DE LA VENTANA DE ARGOS 151…»), la ventana del panorama, las aserciones, el `<title>` que reemplaza (en `datos-argos-151.py` dice ARGOS 150 — … — 2026-11-14: ponga **ARGOS 151 — Reporte Nacional de Seguridad — 2026-11-15**, plantilla `reports/argos-2026-11-15.html`), `WINDOW_DAYS` (la plantilla trae 2: cambie «WINDOW_DAYS = 2;» por el valor nuevo en el script y en la aserción) y las listas de fichas por página.
- ⚠️ Al extraer bloques del generador anterior, **no corte un f-string a medias** (en 151, el bloque de funciones arrastró el inicio de `port` y la línea `return` de `armrow`).
- Móvil: `python3 tools/gen-movil.py 152 <FECHA> 151 2026-11-15 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-15 <FECHA>` (solo escritorio; el móvil lo valida su generador).
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 153. Commit y push.
