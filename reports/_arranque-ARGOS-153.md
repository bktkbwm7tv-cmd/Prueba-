# ORDEN DE ARRANQUE — ARGOS 153

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 153 hereda» y «Deuda de método (ARGOS 152)»), `reports/argos-2026-11-16-fuentes.md` (ARGOS 152) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-153.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-16` (ARGOS 152) y **310** archivos en `reports/` (incluida la orden de 153). 139 a 152 viven fuera de `main`; **152 en `claude/argos-152-nacional-reqwch`** (encima de `claude/argos-151-nacional-c9xttt`). Las catorce fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 153** |
| Ventana | **abre 2026-11-16 10:30 CDMX** (cierre de 152) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 24 h 15 (151) · **24 h 06 (152)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-17.html` (martes 17-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **2** (16 y 17; la plantilla de 152 ya trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 153 hereda** y **Deuda de método (ARGOS 152)**.
3. `reports/argos-2026-11-16-fuentes.md` §3, §5, §7 y §8.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-09`, `-14`, `-15`, `-16`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal (acciones del 13 al 16 sin indexar al cierre de 152; repartir entre 150, 151, 152 y 153 solo con día por ruta o titular) y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 152

| Trampa | Control |
|---|---|
| **Titulares entrecomillados que no existen** | Seis en 152 (El Universal en Gaviotas, Quadratín Tlaxcala, un medio-persona en Tecate, E-consulta, La Silla Rota y El Heraldo en Chignahuapan): exigir URL y titular literal |
| **Agregado citado como fuente del hecho** | Infobae «Mazatlán suma siete asesinatos…» en Pueblo Nuevo |
| **Primer parte frente a actualización** | Pueblo Nuevo (1 → 2 muertos), Galeana (3 → 2 heridos): declarar ambos |
| **Seguimiento atado al ARG-ID equivocado** | Monterrey: vinculación por secuestro frente a ARG-150-REC-003 (riña) |
| **Cifras solo por resumen en tarjetas** | Edomex: n/d en tarjetas; desglose solo en la tabla |
| **Hora de «Consulta» provisional** | Escribirla al cierre de R2 con `date` |
| **Medios homónimos** | Enfoque Monterrey ≠ ENfoque Noticias |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-152.py` (copia a `datos-argos-153.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 10:30 DEL 16, ES DE LA VENTANA DE ARGOS 152…»), `PUB`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (en `datos-argos-152.py` dice ARGOS 151 — … — 2026-11-15: ponga **ARGOS 152 — Reporte Nacional de Seguridad — 2026-11-16**, plantilla `reports/argos-2026-11-16.html`), `WINDOW_DAYS` (la plantilla trae 2) y las listas de fichas por página.
- El generador de 152 ensambla tres bloques (datos · funciones copiadas de 151 · páginas); al copiar, **no corte un f-string a medias**.
- Móvil: `python3 tools/gen-movil.py 153 <FECHA> 152 2026-11-16 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-16 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 154. Commit y push.
