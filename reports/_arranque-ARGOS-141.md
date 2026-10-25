# ORDEN DE ARRANQUE — ARGOS 141

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 141 hereda» y «Deuda de método (ARGOS 140)»), `reports/argos-2026-10-25-fuentes.md` (ARGOS 140) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-141.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-25` (ARGOS 140) y **226 archivos** en `reports/`. ARGOS 139 vive en `claude/argos-139-qe9f01`; ARGOS 140, en `claude/argos-140` (encima). Ninguna está en `main`: las tres fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 141** |
| Ventana | **abre 2026-10-25 07:45 CDMX** (cierre de 140) y cierra a la hora real de arranque |
| Serie | 26 h 31 (137) · 20 h 01 (138) · 27 h 17 (139) · **93 h 22 (140, ventana larga)** |
| Ciclo | **B** (Noreste + Golfo), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-DD.html` (fecha del arranque, sin sufijo) · `WINDOW_DAYS` = fechas de calendario de la ventana |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 141 hereda** y **Deuda de método (ARGOS 140)**.
3. `reports/argos-2026-10-25-fuentes.md` §5-§7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-18` a `-21` y `-25`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30. Todo `extended`.

**Orden nuevo (lección de 140)**: (1) Bloque 0 y control · (2) **triple consulta federal y recall nacional por día ANTES de la ola** · (3) ola, con las pistas del recall en los encargos de cada región · (4) repetición de la triple consulta al final. En 140 el recall corrió en paralelo y sus pistas llegaron a dos equipos sin presupuesto.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 140

| Trampa | Control |
|---|---|
| **Seguimientos procesales como fichas** | Las vinculaciones del exfiscal entraron como 🟢 y `editor-duplicidad` las sacó: un paso procesal de un caso ya publicado va al bloque de seguimientos |
| **Republicaciones del boletín federal** | SICOM, RED113, Talla Política, Diario Puntual, ABC, Intolerancia: una fuente |
| **Eco de consulta** | «1,338 cartuchos», «3055/2026»: la cifra puesta entre comillas vuelve en el resumen sin respaldo |
| **Agregado que la ficha excluye** | Chimalhuacán: la cifra «menor» venía del agregado de N+ que la ficha no contaba como fuente |
| **Marca de apertura** | Solo cuando la **publicación** es del día de apertura; si lo es solo el hecho, «día del hallazgo solo por resumen» |
| **`site:` con `OR`** | El buscador lo ignora: un dominio por consulta |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-140.py` (copia a `datos-argos-141.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-25.html`, «ARGOS 140 — … — 2026-10-25») y la sustitución de `WINDOW_DAYS` (la plantilla trae **5**).
- Móvil: `python3 tools/gen-movil.py 141 <FECHA> 140 2026-10-25 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-25 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`; la ronda 2 en serie.
- Encargos con fecha: **Tulantepec, 28-oct** (por resumen).
