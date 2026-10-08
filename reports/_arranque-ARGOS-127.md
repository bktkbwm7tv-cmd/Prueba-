# ORDEN DE ARRANQUE — ARGOS 127

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 126 (corte 2026-10-08 08:56). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-08-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-127.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main
git merge --ff-only origin/claude/argos-126
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 127**: última edición `argos-2026-10-08` (ARGOS 126) y **135 archivos** en `reports/`
(129 + cuatro de la edición + `_arranque-ARGOS-127.md` + `_ordenes-ARGOS-127.txt`).
⚠️ **ARGOS 126 vive en `claude/argos-126`**; `main` quedó en ARGOS 125 (`60f2777`) salvo que el destinatario la haya mergeado. El segundo
`ff-only` la trae; si falla, parar y avisar.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 127** |
| Ventana | **abre 2026-10-08 08:56 CDMX** —donde cerró ARGOS 126— y cierra a la **hora real de arranque** |
| Serie | 87 h 21 (122) · 23 h 25 (123) · 46 h 19 (124) · 320 h 34 (125) · **17 h 41 (126)** |
| Densidad | 0,19 · 0,04 · 0,30 · 0,16 · **0,40** — ⚠️ la de 126 no es comparable: 6 de 7 hechos en `FRONTERA DE VENTANA` |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — secciones **Cerrados por ARGOS 126**, **Abiertos que ARGOS 127 hereda** y **Deuda de método**.
3. `reports/argos-2026-10-08-fuentes.md` — §4 (boletín), §7 (arbitrajes), §9 (cobertura), §13 (controles).
4. `reports/indice-arg-id.md` — `grep` por topónimo **antes de fichar**. ⚠️ En 126 un barrido propuso como nuevo un hecho ya publicado
   (Omealca = `ARG-125-008`) porque su `grep` falló: **el coordinador repite el `grep`**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos sobre un hecho de las últimas 48 h (en 126: `standard`
  llegó al 6-oct, `extended` al 7-oct).
- **Tope de 200 búsquedas por turno, compartido.** En 126: diez equipos, 133 búsquedas en una sola ola; 164 con verificación y controles.
- **Cifra entre comillas** para obtener el literal de los renglones de mayor peso.

## BLOQUE 4 — DEUDA QUE ARGOS 127 HEREDA

### 4.1 Encargos
1. ⚠️⚠️ **GUERRERO · El Balcón** (`ARG-125-051`): siete desaparecidos; amparo 412/2026; **video del 8-oct no autenticado — no difundir su
   contenido como dato**.
2. ⚠️⚠️ **CHIHUAHUA · Balleza** (`ARG-126-REC-004`): identidad de los 2 abatidos, hora, cifras contradichas (231/230; 5/2 vehículos).
3. ⚠️ **SINALOA · Pánuco, 82 AEI** (`ARG-126-004`): tipología, lugar y literal del desglose.
4. **NAYARIT · Xalisco** y **JALISCO · Guadalajara**: cifra, identificaciones, comunicado; seis detenidos de Ópalo.

### 4.2 Seguimientos
Cócorit (si se desmiente el muerto, el único rojo de 126 pasa a 🟡) · Coatzacoalcos (audiencia del 8-oct, causa 540/2026; `ARG-126-FE-004`) ·
Zihuatanejo · Mixtequilla · Juárez Casas Grandes · 26 extranjeros de Juárez · Comonfort · Hermosillo.

### 4.3 Sentencias candidatas — falta boletín oficial en todas
En ventana de 126, solo medios: FGR Juárez (Acequias) · NL, Laurentino «N», 44 años. Previas: Edomex ×4, Santa Catarina, Cárdenas, y las
heredadas de 125. ⚠️ **Umbral asimétrico: sin fuente oficial no se integra.**

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **PRIORIDAD SOBRE EL CICLO — judicial**: las **16 fiscalías `NO REVISADA`** de 126: **BCS, Sin · Coah, Tamps, SLP, Zac · Col, Nay, Ags,
  Mich · Chis, Oax, Gro, Camp, Yuc, QRoo**. **Armamento**: Morelos y Tlaxcala.
- Después, **CICLO B** (Noreste + Golfo). El recall regional va dentro de cada barrido.
- ⚠️ **Todo renglón del boletín federal con armamento y sin hora se busca por su topónimo antes de fichar**: en 126, Balleza llegó como
  aseguramiento y era un enfrentamiento con dos abatidos, anterior a la apertura.
- Boletín federal: triple consulta. Si la ventana abre de mañana (08:56), el boletín del 8-oct cae probablemente **íntegro dentro**.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 126

| Trampa | Control |
|---|---|
| **El boletín resume un combate como aseguramiento** | Balleza: buscar el topónimo |
| **Una cifra solo existe en el resumen** | Cosalá (5 laboratorios): retirado; Alamedas: segunda edición sin respaldo → `CANTIDAD NO DETERMINADA` |
| **Un «literal» que no se reproduce** | Pánuco: el desglose quedó «solo por resumen» |
| **Un `grep` fallido de un agente** | Omealca y Aguascalientes ya estaban publicados |
| **Portada que repite las conclusiones** | Portada = acciones sobre hechos distintos; conclusiones = patrones con ARG-ID |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-126.py`**: copie, cambie los bloques `E` (hechos), `R` (recuperaciones), `ARM`, las constantes del corte y
  los textos de portada, Valoración, Conclusiones y cobertura. Plantilla: `reports/argos-2026-10-08.html`
  (`python3 tools/datos-argos-127.py reports/argos-2026-10-08.html reports/argos-<FECHA>.html`).
  ⚠️ El generador **sustituye `WINDOW_DAYS = 14`**: si parte del cartelón de 126, ajuste el `replace` a `WINDOW_DAYS = 2`. Fíjelo en el
  **número de fechas de calendario** que toca la ventana.
- Móvil y texto: `python3 tools/gen-movil.py 127 <FECHA> 126 2026-10-08 <HORA>` y `python3 tools/gen-texto.py …`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-08 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes. **Doce pases consecutivos, doce «CORREGIR».** Lánzelos sobre
  una versión estable: en 126 el borrador cambió durante el control y el archivo de fuentes quedó desfasado.
