# ORDEN DE ARRANQUE — ARGOS 154

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 154 hereda» y «Deuda de método (ARGOS 153)»), `reports/argos-2026-11-17-fuentes.md` (ARGOS 153) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-154.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-11-17` (ARGOS 153) y el número de archivos en `reports/` que da la orden (incluida la orden de 154). 139 a 153 viven fuera de `main`; **153 en `claude/argos-153-criminal-intelligence-6knrt6`** (encima de `claude/argos-152-nacional-reqwch`). Las quince fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 154** |
| Ventana | **abre 2026-11-17 11:34 CDMX** (cierre de 153) y cierra a la hora real de arranque (o del «Procede», si llega más de dos horas tarde) |
| Serie | 24 h 06 (152) · **25 h 04 (153)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-11-18.html` (miércoles 18-nov; si es otro día, cámbialo) · `WINDOW_DAYS` = **2** (17 y 18; la plantilla de 153 ya trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Abiertos que ARGOS 154 hereda** y **Deuda de método (ARGOS 153)**.
3. `reports/argos-2026-11-17-fuentes.md` §3, §5, §7 y §8.
4. `reports/indice-arg-id.md` y el HTML de las ediciones previas (`argos-2026-11-14`, `-15`, `-16`, `-17`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**; tope duro) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal (13 al 17; reparto por ventanas solo con día por ruta o titular) y recall nacional por día antes de la ola · (3) ola · (4) borrador · (5) controles R1 en paralelo, R2 en serie · (6) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 153

| Trampa | Control |
|---|---|
| **Titular de N+ «Balacera Hoy DD de Mes»** | Liveblog: no fecha ni sostiene cifras; dos citados por equipos no se localizaron (Azcapotzalco, Ciudad Victoria) |
| **Titular parafraseado y ruta equivocada** | El Diario de Chihuahua (`diario.mx`): exigir URL completa |
| **Medio equivocado** | «PCM» era Grupo Marmor (Zamora) |
| **Tercera aparición** | Hechos no fichados dentro del hecho de una ficha y otra vez en vistos: lo no fichado va solo a vistos |
| **Valoración que reimprime conteos** | La valoración aplica agravantes y escala; los conteos, en el panorama |
| **Detenidos contradichos** | «dos presuntos detenidos» (El Universal) frente a «la detención» (Infobae): declarar «1 o 2» |
| **Hora de «Consulta»** | `__CONSULTA__` en el generador; la aserción impide publicar sin hora real |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-153.py` (copia a `datos-argos-154.py`): cambie `NUM`, `FECHA`, `HORA`, `DUR`, `HORAS`, `RET` («SI RESULTA ANTERIOR A LAS 11:34 DEL 17, ES DE LA VENTANA DE ARGOS 153…»), `PUB`, la ventana del panorama, las aserciones, el `<title>` que reemplaza (en `datos-argos-153.py` dice ARGOS 152 — … — 2026-11-16: ponga **ARGOS 153 — Reporte Nacional de Seguridad — 2026-11-17**, plantilla `reports/argos-2026-11-17.html`), `WINDOW_DAYS` (la plantilla trae 2) y las listas de fichas por página. Para `-REC-`, recupere `co4` y `rows_rec` del generador de 152.
- Móvil: `python3 tools/gen-movil.py 154 <FECHA> 153 2026-11-17 <HORA>`. Texto: `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-11-17 <FECHA>`.
- Controles: dos rondas; informes en `reports/argos-<FECHA>-equipos.md` y `-fuentes.md`; la ronda 2 en serie.
- Cierre: `_pendientes.md`, `indice-arg-id.md`, orden de ARGOS 155. Commit y push.
