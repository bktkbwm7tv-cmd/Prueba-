# ORDEN DE ARRANQUE — ARGOS 129

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 128 (corte 2026-10-10 09:08). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-10-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-129.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main
git merge --ff-only origin/claude/argos-127
git merge --ff-only origin/claude/argos-128
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 129**: última edición `argos-2026-10-10` (ARGOS 128) y **147 archivos** en `reports/`
(141 + cuatro de la edición + `_arranque-ARGOS-129.md` + `_ordenes-ARGOS-129.txt`).
⚠️ **Ni ARGOS 127 ni ARGOS 128 se mergearon a `main`** al cierre: 128 se construyó en `claude/argos-128` sobre `claude/argos-127`. Los
merges `ff-only` traen las dos ediciones. ⚠️ **El clon puede arrancar por detrás de `origin/main`** (en 128 arrancó en `60f2777`): eso no es
un fallo de la base si `origin/main` está donde se espera y todos los merges son fast-forward. Si alguno no lo es, parar y avisar.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 129** |
| Ventana | **abre 2026-10-10 09:08 CDMX** —donde cerró ARGOS 128— y cierra a la **hora real de arranque** |
| Serie | 46 h 19 (124) · 320 h 34 (125) · 17 h 41 (126) · 22 h 24 (127) · **25 h 48 (128)** |
| Densidad | 0,30 · 0,16 · 0,40 · 0,27 · **0,23** — 128: 4 de 6 hechos en `FRONTERA`, las horas de los otros 2 solo por resumen |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 128**, **Abiertos que ARGOS 129 hereda** y **Deuda de método (ARGOS 128)**.
3. `reports/argos-2026-10-10-fuentes.md` — §4 (boletín), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura y criterio único), §13 (controles), §15.
4. `reports/indice-arg-id.md` — `grep` por topónimo **antes de fichar**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (128: `standard` solo la cifra preliminar del 8-oct;
  `extended` halló la segunda riña del 9-oct).
- **Tope de 200 por turno, compartido**: ola de **~160**, **~10 del coordinador** —una búsqueda nacional por día de la ventana («viernes 9 de
  octubre», «sábado 10 de octubre»), que en 128 halló los dos rojos que la ola no trajo— y **~25 para `procedencia-cifras`**.
- **Cifra entre comillas** para obtener el literal. Un fragmento entre comillas **dentro del resumen** no es citable: hace falta titular,
  *slug* o fuente concreta.

## BLOQUE 4 — DEUDA QUE ARGOS 129 HEREDA

### 4.1 Encargos
1. ⚠️⚠️ **OAXACA · Pinotepa Nacional** (`ARG-128-001`): cifra de víctimas (3, o 2 y una lesionada), hora, comunicado de la FGEO, detenidos.
2. ⚠️⚠️ **SINALOA · penal El Castillo** (`ARG-128-004`, `ARG-127-004`): hora de la segunda riña, detenidos, ingreso de armas, traslados.
3. ⚠️ **EDOMEX · San José del Rincón** (`ARG-128-003`): **una fuente con fecha** (si es 8-oct, fe de erratas hacia 127).
4. ⚠️ **Literales del boletín del 8-oct** (Río Bravo, Juárez, Valle de Santiago): **si siguen solo por resumen, fe de erratas en 129**.
5. **GUERRERO · El Balcón** (`ARG-125-051`): peritaje del video —**no difundir su contenido**— y cumplimiento del amparo 412/2026.

### 4.2 Seguimientos
Naucalpan (noche) · Celaya (cifra de armas) · Michoacán, 12 cateos (comunicado, armas) · Sombrerete (185 o 39) · Borja (posible duplicidad) ·
«El Moco» (fecha) · boletín del 9-oct · Zihuatanejo · Mixtequilla · 26 extranjeros · Comonfort · Hermosillo · Xalisco · SLP (`ARG-125-015`).

### 4.3 Sentencias candidatas — falta boletín o individualización en todas
En ventana de 128: FGR Chihuahua (7 años) y FGR Sinaloa (hasta 11 años) —titulares del listado, sin caso individualizado— · León, 26 años 8 meses ·
NL, 28 años · Chihuahua, 8 años. **Querétaro, Corregidora, 3 años**: boletín oficial del 8-oct, posible de la ventana de 127. ⚠️ **Umbral
asimétrico: sin fuente oficial no se integra; folios DPE solo por resumen no se publican.**

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **Cada equipo regional abre con una búsqueda por día de la semana y sus entidades**, antes del triaje de portales.
- **PRIORIDAD SOBRE EL CICLO**: **Yucatán** (los tres módulos) · **armamento** Tlax (tercera edición), BC, Sin, Coah, SLP, Col, Nay, Edomex, Qro,
  Ver, Camp · **sentencias** Son, Sin, Coah, SLP, Zac, Col, Nay, Edomex, Chis, Camp · **alto impacto** BCS, Qro, Chis. Después, **CICLO A**
  (Noroeste + Centro).
- ⚠️ **Criterio único de cobertura** (128): `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial. **Confirmar primero el
  dominio real** de SSC Tlaxcala, FGE Edomex, SSP Veracruz, SSP SLP, Fiscalía Chiapas, Campeche, Yucatán, Colima y Nayarit.
- Boletín federal: triple consulta completa para las acciones del 9 y 10-oct.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 128

| Trampa | Control |
|---|---|
| **El barrido regional no ve el rojo nacional** | Pinotepa y San José del Rincón, hallados solo por la búsqueda nacional por día de la semana |
| **Un seguimiento se cuela como hecho** | Coatzacoalcos: la vinculación ya estaba titulada el 6-oct; se retiró tras el control |
| **Un solo medio regional «separa» dos hechos** | Borja: el titular de El Diario no basta frente a la posible duplicidad con Balleza |
| **El titular en plural contradice la cifra del resumen** | Celaya: «armas aseguradas» frente a «un arma»: cualitativo |
| **La inferencia del coordinador escrita como hecho** | Michoacán: el vínculo con Sol Naciente y la madrugada del 8-oct, marcados como inferencia |
| **Portada y Conclusiones sobre los mismos hechos** | Las Conclusiones van sobre hechos que la portada no toca |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-128.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes y los textos de portada, Valoración,
  Conclusiones y cobertura. Plantilla: `reports/argos-2026-10-10.html`
  (`python3 tools/datos-argos-129.py reports/argos-2026-10-10.html reports/argos-<FECHA>.html`). Cambie la línea de `<title>` que reemplaza
  el generador (ARGOS 128 — 2026-10-10). El generador comprueba `WINDOW_DAYS = 2;` con `assert`: si la ventana toca otro número de fechas, sustitúyalo.
- Las filas `ARM` llevan ahora `color`, `fecha` y `fecha_txt` propios.
- Móvil y texto: `python3 tools/gen-movil.py 129 <FECHA> 128 2026-10-10 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
  `gen-texto.py` ya incluye recuadros y `-REC-`; `validar.js` sigue sin aplicar al móvil.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-10 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes. **Catorce pases consecutivos, catorce «CORREGIR».** Lánzelos sobre
  una versión estable y commiteada, y **pase a los dos las notas de la ola** (en 128 el editor no pudo cotejar los hechos del coordinador).
