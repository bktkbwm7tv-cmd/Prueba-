# ORDEN DE ARRANQUE — ARGOS 145

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 145 hereda» y «Deuda de método (ARGOS 144)»), `reports/argos-2026-10-29-fuentes.md` (ARGOS 144) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-145.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-29` (ARGOS 144) y **254 archivos** en `reports/`. 139 en `claude/argos-139-qe9f01`; 140 en `claude/argos-140`; 141 en `claude/argos-141-nacional-kh5fj6`; 142 y 143 en `claude/argos-criminal-intelligence-otiawj`; **144 en `claude/argos-144`** (cada una encima de la anterior). Ninguna está en `main`: las seis fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 145** |
| Ventana | **abre 2026-10-29 11:36 CDMX** (cierre de 144) y cierra a la hora real de arranque |
| Serie | 24 h 52 (141) · 24 h 08 (142) · 23 h 43 (143) · **27 h 08 (144)** |
| Ciclo | **C** (Occidente + Sureste), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-31.html` (sábado 31-oct) · `WINDOW_DAYS` = **3** (29, 30 y 31; la plantilla de 144 trae 2) |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 145 hereda** y **Deuda de método (ARGOS 144)**.
3. `reports/argos-2026-10-29-fuentes.md` §5-§7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas (`argos-2026-10-25`, `-26`, `-27`, `-28` y `-29`).

## BLOQUE 3 — PRESUPUESTO Y ORDEN DE TRABAJO

Tope de 200 por turno: control 2 · coordinador 18 · ola 150 (6 × 25; **4 por equipo reservadas a fecha en la ruta**) · `procedencia-cifras` 30 (**R1 24 · R2 6**). Todo `extended`.

**Orden**: (1) Bloque 0 y control · (2) triple consulta federal y recall nacional por día ANTES de la ola, **con «instalaciones / sede» y «bloqueos» en el recall**, fijando la fecha y la hora de toda pista roja · (3) ola · (4) ruta fechada de todo 🔴 que llegue sin ella · (5) repetición de la triple consulta al final.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 144

| Trampa | Control |
|---|---|
| **Hora por resumen anterior a la apertura** | Irapuato, col. Benito Juárez (~07:15 del 28) → visto de 143, no hecho propio |
| **Cifra de armas solo en el resumen** | General Bravo, Lindavista, Cancún: «armas» por titular; cifras solo por resumen → `n/d` |
| **Titular de ficha más fuerte que su trazabilidad** | «dos bolsas», «vivienda», «persecución», «droga», «robada»: solo por resumen |
| **«Única fuente con esa expresión»** | Matamoros: El Mañana y Hora Cero también decían «objetivo prioritario» |
| **Madrugada del día de apertura** | CDMX Centro y Coatzacoalcos: recuperaciones de 143 por hora solo por resumen |
| **Mismo operativo con dos fechas** | Tuxtepec: captura publicada el 28; cateo con 2 detenidos en el boletín federal del 27 |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-144.py` (copia a `datos-argos-145.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, `RET` (hora de apertura 11:36 del 29), la ventana del panorama, las aserciones, el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-29.html`, «ARGOS 144 — … — 2026-10-29») y las listas de fichas por página.
- Móvil: `python3 tools/gen-movil.py 145 <FECHA> 144 2026-10-29 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-29 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`; la ronda 2 en serie.
