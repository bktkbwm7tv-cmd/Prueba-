# ORDEN DE ARRANQUE — ARGOS 131

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 130 (corte 2026-10-12 08:19). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-12-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-131.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main
git merge --ff-only origin/claude/argos-129
git merge --ff-only origin/claude/argos-130
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 131**: última edición `argos-2026-10-12` (ARGOS 130) y **159 archivos** en `reports/`
(153 + cuatro de la edición + `_arranque-ARGOS-131.md` + `_ordenes-ARGOS-131.txt`).
⚠️ **ARGOS 129 y 130 viven en `claude/argos-129` y `claude/argos-130`** (ramas empujadas; PR solo si el destinatario lo pide). `argos-130` parte de
`argos-129` (`9eaba81`): si `main` no contiene ninguna, los dos `ff-only` deben avanzar en fast-forward desde `b0558a3`. **Si algún merge no es
fast-forward, parar y avisar.** El clon puede arrancar por detrás de `origin/main` (en 128, 129 y 130 arrancó en `60f2777`): no es fallo.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 131** |
| Ventana | **abre 2026-10-12 08:19 CDMX** —donde cerró ARGOS 130— y cierra a la **hora real de arranque** |
| Serie | 17 h 41 (126) · 22 h 24 (127) · 25 h 48 (128) · 23 h 50 (129) · **23 h 21 (130)** |
| Densidad | 0,40 · 0,27 · 0,23 · 0,25 · **0,39** — 130: **9 de 9 hechos en `FRONTERA`** |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 130**, **Abiertos que ARGOS 131 hereda** y **Deuda de método (ARGOS 130)**.
3. `reports/argos-2026-10-12-fuentes.md` — §5 (encargos), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §13 (controles), §15.
4. `reports/indice-arg-id.md` y **el HTML de las tres ediciones previas** — `grep` por topónimo **antes de fichar**.

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (130: `standard` devolvió incendios de 2021 y 2023 para Minatitlán).
- **Tope de 200 por turno, compartido**: ola **~160**, **~10 del coordinador** —una búsqueda nacional por día de la ventana; en 130 halló Jacona— y
  **~25 para `procedencia-cifras`**. 130 gastó **194**.
- **Cifra entre comillas** para el literal.
- ⚠️ **Nuevo**: cada equipo hace **una búsqueda de «funcionario / director / servidor público asesinado»** en sus entidades. En 130 la ola omitió
  el asesinato del coordinador de Protección Civil de Escuinapa (`ARG-130-009`), que solo halló `procedencia-cifras`.

## BLOQUE 4 — DEUDA QUE ARGOS 131 HEREDA

### 4.1 Encargos
1. ⚠️⚠️ **MICHOACÁN · Jacona** (`ARG-130-001`): saldo oficial (6 por la FGE, titular de atiempo.mx, u 8 por Quadratín; heridos 3, 4 o 6); hora citable; inventario de
   armas largas y camioneta; detenidos; comunicado SSP / Guardia Civil / FGE.
2. ⚠️⚠️ **TABASCO · Nacajuca** (`-003`) y **MICHOACÁN · Morelia** (`-004`): **hora citable**. Si es anterior a las 08:58 del 11-oct, **fe de erratas: pasan a 129**
   y salen de los totales de 130.
3. ⚠️ **SINALOA · Escuinapa** (`-009`, coordinador de Protección Civil; `-006`, El Roblito): hora y lugar citables; ¿mezcla entre ambos?; FGE.
4. ⚠️ **CHIHUAHUA · Ciudad Juárez** (`-008`): fecha del hecho (10 u 11-oct). Si fue el 10, fe de erratas.
5. **VERACRUZ · Minatitlán** (`ARG-129-001`): segundo comunicado de Pemex o boletín de la FGE con el saldo (2 muertos por medios).
6. **QUINTANA ROO · Cancún** (`-002`): FGE QRoo (`fgeqroo.gob.mx`). **GUERRERO · Acapulco** (`-007`): inventario oficial.

### 4.2 Seguimientos
SEMAR 10-oct (7 AEI frente a `ARG-125-005`; 12 o 13 largas) · Zamora (4 frente a 5) · Navolato San Pedro (uno o dos cuerpos) · Pinotepa · El Castillo ·
Los Pinos · Chipilo · Pachuca (630/640) · Sombrerete · Borja · El Balcón · Zihuatanejo · **candidatos sin URL con fecha**: Tijuana llantera, Mazatlán ×2,
Ciudad Hidalgo, Juchitán La Ventosa, Huejotzingo, Cancún SM 225.

### 4.3 Sentencias candidatas
**Ensenada: pena el 16-oct** · **Hidalgo, Santiago Tulantepec: pena el 14-oct** · Zacatecas José «N» (fecha no anclada; homónimo o republicación) ·
NL tres personas · Navolato 80 años · Tamaulipas FGJE-381 a 384 · León. ⚠️ **Umbral asimétrico: sin fuente oficial no se integra.**

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **Cada equipo regional abre con una búsqueda por día de la semana y sus entidades**, hace **al menos una `site:` de armamento por entidad** y **una de
  servidores públicos asesinados**.
- **PRIORIDAD SOBRE EL CICLO**: **armamento** BC, BCS, Dgo · Coah, Tamps · Jal, Col, Nay, Ags · Hgo, Qro · Chis, Camp, Yuc, QRoo · **sentencias** BC,
  Son, Sin · Zac · Col, Ags, Mich, Gto · Edomex, Mor, Pue, Tlax, Hgo · Gro, Chis, Camp, Yuc (Son y Sin, **cuarta edición**: probar `fge.sonora.gob.mx`,
  `fiscalia.sinaloa.gob.mx` y título sin `site:`) · **alto impacto** Ags (los tres módulos sin revisar). Después, **CICLO C** (Occidente + Sureste).
- **Criterio de cobertura**: armamento y sentencias, `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial; alto impacto, búsqueda
  dirigida en medios. Dominios confirmados en §3 y §9 del archivo de fuentes de 130.
- **Federales**: GN, Defensa y Marina siguen `NO REVISADA`: asignar cuota. Boletín federal: triple consulta para las acciones del 9 al 12-oct.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 130

| Trampa | Control |
|---|---|
| **`standard` no encuentra hechos de 48 h** | Minatitlán: `standard` devolvió incendios de 2021 y 2023 |
| **Dos hechos del mismo día y la misma calle se mezclan en el resumen** | Escuinapa: El Roblito y el coordinador de PC, «Aldama» en ambos |
| **La fecha de la URL tomada como fecha del hecho** | Ciudad Juárez: publicado el 11-oct; hecho del 10 u 11 |
| **Fe de erratas por resumen** | Zamora «5 muertos»: el titular del mismo medio dice «cuatro»; FE retirada |
| **URL con año y mes, sin día** | Zacatecas (NTR 2026/10): no ancla la publicación |
| **«Y 6 más» en un titular** | Acapulco: acumulado del caso de 2025, no del evento |
| **Trampa de año en el boletín federal** | El rango «10, 11 y 12 de octubre» devolvió el de **2025** |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-130.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes y los textos de portada, Valoración, Conclusiones y
  cobertura. Plantilla: `reports/argos-2026-10-12.html`. Cambie la línea de `<title>` que reemplaza el generador (ARGOS 130 — 2026-10-12). Si hay
  recuperaciones, restituya la página de `-REC-` (en 130 se retiró por no haber ninguna; ver `datos-argos-129.py`). `WINDOW_DAYS = 2;` con `assert`.
- Campo `cual=True` en una ficha sin fila de armamento con aseguramiento sin cifra: la trazabilidad dice «evento cualitativo».
- Móvil y texto: `python3 tools/gen-movil.py 131 <FECHA> 130 2026-10-12 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-12 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes, en paralelo, sobre una versión estable y commiteada, **con las notas de
  los seis equipos** (en 130 faltaron las de Occidente). **Dieciséis pases consecutivos, dieciséis «CORREGIR».**
