# ORDEN DE ARRANQUE — ARGOS 144

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 144 hereda» y «Deuda de método (ARGOS 143)»), `reports/argos-2026-10-28-fuentes.md` (ARGOS 143) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-144.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-28` (ARGOS 143) y **247 archivos** en `reports/`. 139 en `claude/argos-139-qe9f01`; 140, en `claude/argos-140`; 141, en `claude/argos-141-nacional-kh5fj6`; 142 y 143, en `claude/argos-criminal-intelligence-otiawj` (cada una encima de la anterior). Ninguna está en `main`: las cinco fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 144** |
| Ventana | **abre 2026-10-28 08:28 CDMX** (cierre de 143) y cierra a la hora real de arranque |
| Serie | 93 h 22 (140) · 24 h 52 (141) · 24 h 08 (142) · **23 h 43 (143)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-DD.html` (fecha del arranque, sin sufijo) · `WINDOW_DAYS` = fechas de calendario de la ventana |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 144 hereda** y **Deuda de método (ARGOS 143)**.
3. `reports/argos-2026-10-28-fuentes.md` §5-§7 y §11 (incluye la tabla de equivalencia de ARG-ID del borrador).
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-21`, `-25`, `-26`, `-27` y `-28`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30. Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día ANTES de la ola, **fijando la fecha de toda pista roja** · (3) ola, con las pistas del recall en los encargos · (4) **búsqueda de ruta fechada de todo 🔴 que llegue sin ella** · (5) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 143

| Trampa | Control |
|---|---|
| **«Ayer» en el resumen de una nota del día de apertura** | Tabasco: ruta del 27, hallazgo del 26 por resumen → `-REC-` de 142, no hecho propio |
| **Declaración nombrada no vista** | Celaya: el secretario de Seguridad, por titular en Heraldo de México, Tribuna, La Jornada y La Silla Rota; la ola la tenía «solo por resumen» |
| **Falsa fuente única** | Mercado de Abastos (AM, Noticieros en Línea), Chulavista y Aguaruto (Luz Noticias) |
| **Señuelos de «este martes»** | Policía de Puebla (16-oct = ARG-134-005), San Miguel de Allende (enero), El Saucito (septiembre) |
| **Mismo hallazgo, dos ubicaciones** | Tecate: Cerro Azul (Punto Norte) / Nueva Hindú (Zeta) |
| **Detención o cumplimiento en reclusión** | Rayón: «detienen» frente a «cumplimenta órdenes»; posible reclusión previa |
| **Año trampa del boletín federal** | «26 y 27 de octubre» devuelve 2025 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-143.py` (copia a `datos-argos-144.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (hora de apertura), la ventana del panorama, las aserciones y el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-28.html`, «ARGOS 143 — … — 2026-10-28»).
- El generador de 143 ya admite armamento sin eventos (`ARM = []` → todas las categorías `n/d` y fila «SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE»).
- Móvil: `python3 tools/gen-movil.py 144 <FECHA> 143 2026-10-28 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-28 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`; la ronda 2 en serie.
- Encargos con fecha: **Tulantepec, 28-oct 17:00** (por resumen), dentro de la ventana de 144.
