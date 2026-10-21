# ORDEN DE ARRANQUE — ARGOS 140

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 140 hereda» y «Deuda de método (ARGOS 139)»), `reports/argos-2026-10-21-fuentes.md` (ARGOS 139) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-140.txt`.** Este archivo es el detalle.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-21` (ARGOS 139) y **219 archivos** en `reports/`. ARGOS 139 vive en la rama `claude/argos-139-qe9f01` (aún no en `main` al cierre de 139): fusionarla en *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 140** |
| Ventana | **abre 2026-10-21 10:23 CDMX** (cierre de 139) y cierra a la hora real de arranque |
| Serie | 23 h 06 (136) · 26 h 31 (137) · 20 h 01 (138) · **27 h 17 (139)** |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-AAAA-MM-DD.html` con la fecha del corte |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 140 hereda** y **Deuda de método (ARGOS 139)**.
3. `reports/argos-2026-10-21-fuentes.md` §5-§7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas.

## BLOQUE 3 — PRESUPUESTO

Tope de 200 por turno: control 2 · ola ~156 · coordinador ~10 · `procedencia-cifras` ~30. Todo `extended`.

## BLOQUE 4 — TRAMPAS VERIFICADAS EN 139

| Trampa | Control |
|---|---|
| **Republicaciones** | Mismo título y *slug* en varios medios = una fuente (Diario de Juárez / Diario de Chihuahua; Grupo Marmor / MediaNews / Red Michoacán) |
| **Eco de consulta** | La cifra entre comillas vuelve en el resumen: solo vale en titular o *slug* («17 cargadores») |
| **Recuentos de medios** | «Seis asesinados este martes», «cinco en 24 horas»: buscar cada hecho; nunca integrar el recuento |
| **Boletín federal tardío** | El del 19-oct se indexó el 21: repetir la triple consulta al final |
| **Frontera de las 10:23** | Hechos del miércoles 21 por la mañana publicados sin hora: marca de frontera |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-139.py` (copia a `datos-argos-140.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, la ventana del panorama, las aserciones y el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-21.html`, título «ARGOS 139 — … — 2026-10-21»).
- Móvil: `python3 tools/gen-movil.py 140 <FECHA> 139 2026-10-21 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-21 <FECHA>`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-<FECHA>-equipos.md`.
