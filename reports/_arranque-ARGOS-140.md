# ORDEN DE ARRANQUE — ARGOS 140

La continuidad vive en el repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` («Abiertos que ARGOS 140 hereda» y «Deuda de método (ARGOS 139)»), `reports/argos-2026-10-21-fuentes.md` (ARGOS 139) y su archivo de equipos.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-140.txt`.** Este archivo es el detalle.

⚠️ **Rehecha el domingo 25-oct.** La orden del 22-oct no llegó a ejecutarse: la sesión se detuvo tras el Bloque 0 (22-oct 08:14, egreso en 000, 219 archivos) y no produjo edición. ARGOS 140 cubre por tanto **del miércoles 21 al domingo 25**.

## BLOQUE 0 — VERIFICACIÓN DE BASE

Los comandos del mensaje de órdenes. **Estado esperado**: última edición `argos-2026-10-21` (ARGOS 139), **ninguna** edición fechada del 22 al 25-oct y **219 archivos** en `reports/`. ARGOS 139 vive en `claude/argos-139-qe9f01` (`3c343ac`, más la orden del 22-oct en `9712e79`); esta orden vive en **`claude/argos-140`**, encima. Las tres fusiones deben ser *fast-forward*.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 140** |
| Ventana | **abre 2026-10-21 10:23 CDMX** (cierre de 139) y cierra a la hora real de arranque del **domingo 25-oct** (~90-95 h) |
| Calendario | mié 21 · jue 22 · vie 23 · **sáb 24 · dom 25** |
| Serie | 23 h 06 (136) · 26 h 31 (137) · 20 h 01 (138) · 27 h 17 (139) · **~92 h (140)** |
| Precedentes de ventana larga | 119 (117 h 50, cero `-REC-`) · 122 (87 h 21, 17 hechos, densidad 0,19) |
| Ciclo | **A** (Noroeste + Centro), tras la prioridad sobre el ciclo |
| Archivo | `argos-2026-10-25.html` (sin sufijo) · radar `WINDOW_DAYS = 5` |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (acciones como **solicitud**).
2. `reports/_pendientes.md` — **Abiertos que ARGOS 140 hereda**, **Deuda de método (ARGOS 139)** y las reglas de ventana larga de ARGOS 119 y 122 (líneas «UNA VENTANA LARGA…» y «RECALL NACIONAL»).
3. `reports/argos-2026-10-21-fuentes.md` §5-§7 y §11.
4. `reports/indice-arg-id.md` y el HTML de las cinco ediciones previas.

## BLOQUE 3 — PRESUPUESTO

Tope de 200 por turno: control 2 · ola **150 (6 × 25)** · coordinador **18** · `procedencia-cifras` 30. Todo `extended`. Plantilla de equipos: **`tools/plantilla-equipos-140.md`** (escriba la hora de cierre).

Reparto del coordinador (18): triple consulta del boletín federal —día suelto 21, 22, 23, 24 y 25; rango «del 23 al 25»; título sin `site:`— (~8) · **recall nacional por día**, 21 al 25, de masacre / ataque armado / emboscada / narcobloqueo / fosa (~6) · repetición de la triple consulta al final de la ola (~3) · reserva (1).

## BLOQUE 4 — TRAMPAS

| Trampa | Control |
|---|---|
| **Ventana larga** | Absorbe recuperaciones: lo del 21-25 es hecho propio. `-REC-` solo para el alto impacto de la ventana de 139 que 139 no publicó |
| **Barrido ciego a la violencia** | En 122 el recall nacional trajo 4 de 5 rojos; los barridos, ninguno de los ataques a civiles. Recall por día, obligatorio |
| **Balance de fin de semana** | «Fin de semana violento: N muertos» no se reparte ni se integra; cada hecho con su nota |
| **Boletín federal agregado** | Sáb-dom suele salir en rango; día suelto + rango + título sin `site:` |
| **Republicaciones** | Mismo título y *slug* en varios medios = una fuente |
| **Eco de consulta** | La cifra entre comillas vuelve en el resumen: solo vale en titular o *slug* |
| **Recuentos de medios** | Buscar cada hecho; nunca integrar el recuento |
| **Frontera de las 10:23 del 21** | Hechos de la mañana del miércoles publicados sin hora: `PUBLICADO EL DÍA DE APERTURA SIN HORA` |
| **Frontera del domingo 25** | Publicado el 25 sin hora: `FRONTERA DE VENTANA — HORA NO FIJADA` |

## BLOQUE 5 — FORMA Y CONSTRUCCIÓN

- Parta de `tools/datos-argos-139.py` (copia a `datos-argos-140.py`): cambie `NUM`, `FECHA`, `HORA`, `CONSULTA`, `DUR`, `HORAS`, la ventana del panorama, las aserciones —**`WINDOW_DAYS = 5`**— y el `<title>` que reemplaza (plantilla: `reports/argos-2026-10-21.html`, título «ARGOS 139 — … — 2026-10-21»).
- Móvil: `python3 tools/gen-movil.py 140 2026-10-25 139 2026-10-21 <HORA>`. Texto: `gen-texto.py`. Validador: `node tools/validar.js reports/argos-2026-10-25.html 2026-10-21 2026-10-25`.
- Controles: dos rondas, veinte pases cada una; informes en `reports/argos-2026-10-25-equipos.md`. **La ronda 2 en serie** (duplicidad, luego procedencia).
- Valoración: declarar la ventana larga y la no comparabilidad con 139 sin normalizar por hora.
- Encargos que ya caen dentro de la ventana: **pena de Tulantepec (21-oct 17:45)**, **audiencia estatal del exfiscal (22-oct)** y **vinculación federal (24-oct 15:00)**.
