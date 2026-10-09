# ORDEN DE ARRANQUE — ARGOS 128

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 127 (corte 2026-10-09 07:20). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-09-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-128.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main
git merge --ff-only origin/claude/argos-127
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 128**: última edición `argos-2026-10-09` (ARGOS 127) y **141 archivos** en `reports/`
(135 + cuatro de la edición + `_arranque-ARGOS-128.md` + `_ordenes-ARGOS-128.txt`).
⚠️ **ARGOS 127 se construyó en `claude/argos-127` y no se mergeó a `main`** al cierre: el segundo `ff-only` es el que trae la edición.
Si cualquiera de los dos merges no es fast-forward, parar y avisar.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 128** |
| Ventana | **abre 2026-10-09 07:20 CDMX** —donde cerró ARGOS 127— y cierra a la **hora real de arranque** |
| Serie | 23 h 25 (123) · 46 h 19 (124) · 320 h 34 (125) · 17 h 41 (126) · **22 h 24 (127)** |
| Densidad | 0,04 · 0,30 · 0,16 · 0,40 · **0,27** — 127: 2 de 6 hechos en `FRONTERA`, las horas de los otros 4 solo por resumen |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 127**, **Abiertos que ARGOS 128 hereda** y **Deuda de método (ARGOS 127)**.
3. `reports/argos-2026-10-09-fuentes.md` — §4 (boletín), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §13 (controles y renumeración).
4. `reports/indice-arg-id.md` — `grep` por topónimo **antes de fichar**; el coordinador repite el `grep` de los agentes.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (127: `standard` una nota útil; `extended` hasta el 8-oct).
- **Tope de 200 por turno, compartido.** 127: ola de 181 + 2 control + 5 coordinador + **12 de `procedencia-cifras`** = 200. **Insuficiente
  para el control**: en 128, **ola de ~165** y **~25** para `procedencia-cifras`.
- **Cifra entre comillas** para obtener el literal.

## BLOQUE 4 — DEUDA QUE ARGOS 128 HEREDA

### 4.1 Encargos
1. ⚠️⚠️ **SINALOA · Mazatlán, penal El Castillo** (`ARG-127-004`): hora, edad del menor, ingreso de armas, detenidos, literal oficial.
2. ⚠️⚠️ **Literales con umbral de fe de erratas en 128**: Montecarlo (`ARG-127-005`), SLP (`ARG-127-006`), Ojocaliente (`ARG-127-REC-002`).
3. ⚠️ **MICHOACÁN · Uruapan** (`ARG-127-REC-001`): corporación y detenidos (1 o 10).
4. **GUERRERO · El Balcón** (`ARG-125-051`): peritaje del video —**no difundir su contenido**—, amparo 412/2026. **CHIHUAHUA**: Balleza y
   San Francisco de Borja, ¿uno o dos hechos?

### 4.2 Seguimientos
Autolavado de Flores Magón · Tabasco La Huerta (posible duplicidad) · Cosalá · Penjamillo · Xalisco/Ópalo · Casas Grandes (móvil) ·
Coatzacoalcos · Zihuatanejo · Mixtequilla (detenidos) · 26 extranjeros · Comonfort · Hermosillo.

### 4.3 Sentencias candidatas — falta boletín oficial en todas
En ventana de 127, solo medios: Cajeme (Luis Carlos «N», 25 años) · Campeche, FGR (5 personas) · agregado FGE Veracruz. Previas nunca vistas:
Matamoros ×6, QRoo, Buenavista, Nayarit ×2, Culiacán, FGR Juárez/Hermosillo/Colima, BCS. ⚠️ **Umbral asimétrico: sin fuente oficial no se integra.**

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO**: sentencias **BC · Jal, Gto · Mor, Pue, Hgo, Qro, Tlax**; armamento **BCS, Son, Dgo, CDMX, Ags, Tlax**; alto
  impacto **Ags**. Después, **CICLO C** (Occidente + Sureste).
- ⚠️ **`SIN RESULTADO INDEXADO EN VENTANA` exige búsqueda dirigida (`site:`)**: en 127 Tlaxcala pasó a `NO REVISADA` por búsqueda genérica.
- Boletín federal: triple consulta; las acciones del 8-oct no estaban indexadas al cierre de 127.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 127

| Trampa | Control |
|---|---|
| **El resumen del buscador mezcla dos hechos** | San Francisco de Borja: el resumen copió edades, armas y camionetas de Balleza |
| **Heridos que cambian al morir uno** | Autolavado: 2 / 3 / 4 heridos según la hora de la nota; no sumar |
| **Una hora por resumen reordena el corte** | Puebla (~19:00) obligó a renumerar tras el control |
| **La Valoración repite titulares** | Remitir por ARG-ID; cifras de hecho solo en panorama y ficha |
| **El boletín del día anterior tiene renglones huérfanos** | 126 omitió Ojocaliente y Centro; van como `-REC-` de la ventana de origen |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-127.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes y los textos de portada, Valoración,
  Conclusiones y cobertura. Plantilla: `reports/argos-2026-10-09.html`
  (`python3 tools/datos-argos-128.py reports/argos-2026-10-09.html reports/argos-<FECHA>.html`). El generador comprueba `WINDOW_DAYS = 2;`
  con `assert`: si la ventana toca otro número de fechas, sustitúyalo.
- Campo `fecha_txt` para hechos sin fecha propia («no fijada (publicado …)»): `EVENTOS.fecha` debe seguir dentro de la ventana para el validador.
- Móvil y texto: `python3 tools/gen-movil.py 128 <FECHA> 127 2026-10-09 <HORA>` y `python3 tools/gen-texto.py …`.
  ⚠️ `gen-texto.py` omite las `-REC-` y los recuadros; `validar.js` no aplica al móvil.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-09 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes. **Trece pases consecutivos, trece «CORREGIR».** Lánzelos sobre
  una versión estable y commiteada.
