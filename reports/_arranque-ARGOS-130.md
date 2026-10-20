# ORDEN DE ARRANQUE — ARGOS 130

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 129 (corte 2026-10-11 08:58). La continuidad vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-11-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-130.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main
git merge --ff-only origin/claude/argos-129
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 130**: última edición `argos-2026-10-11` (ARGOS 129) y **153 archivos** en `reports/`
(147 + cuatro de la edición + `_arranque-ARGOS-130.md` + `_ordenes-ARGOS-130.txt`).
⚠️ **ARGOS 129 vive en `claude/argos-129`** (rama empujada; PR solo si el destinatario lo pide). Si `main` no la contiene, el `ff-only` de
`origin/claude/argos-129` debe avanzar en fast-forward desde `b0558a3`. **Si algún merge no es fast-forward, parar y avisar.** El clon puede
arrancar por detrás de `origin/main` (en 128 y 129 arrancó en `60f2777`): no es fallo si los merges son fast-forward.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 130** |
| Ventana | **abre 2026-10-11 08:58 CDMX** —donde cerró ARGOS 129— y cierra a la **hora real de arranque** |
| Serie | 320 h 34 (125) · 17 h 41 (126) · 22 h 24 (127) · 25 h 48 (128) · **23 h 50 (129)** |
| Densidad | 0,16 · 0,40 · 0,27 · 0,23 · **0,25** — 129: 4 de 6 hechos en `FRONTERA` |

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro.
2. `reports/_pendientes.md` — **Cerrados por ARGOS 129**, **Abiertos que ARGOS 130 hereda** y **Deuda de método (ARGOS 129)**.
3. `reports/argos-2026-10-11-fuentes.md` — §4 (boletín), §7 (arbitrajes), §8 (fe de erratas), §9 (cobertura), §13 (controles), §15.
4. `reports/indice-arg-id.md` y **el HTML de las tres ediciones previas** — `grep` por topónimo **antes de fichar** (en 129 un equipo trajo
   como nuevo lo ya publicado, y un comunicado agregado repetía 7 AEI posiblemente ya publicados en 125).

## BLOQUE 3 — MODO DE BÚSQUEDA Y PRESUPUESTO

- **Toda búsqueda con `mode:"extended"`.** Consulta de control en los dos modos (129: `standard` **no encontró** a Hamurabi Huesca; `extended`, sí).
- **Tope de 200 por turno, compartido**: ola de **~160**, **~10 del coordinador** —una búsqueda nacional por día de la ventana; en 129 halló el
  único rojo, Minatitlán— y **~25 para `procedencia-cifras`** (un solo `WebFetch`, no más).
- **Cifra entre comillas** para el literal. Un fragmento entre comillas **dentro del resumen** no es citable.

## BLOQUE 4 — DEUDA QUE ARGOS 130 HEREDA

### 4.1 Encargos
1. ⚠️⚠️ **VERACRUZ · Minatitlán** (`ARG-129-001`): saldo oficial (1 muerto y 1 herido, o dos lesionados), comunicado de Pemex o de la FGE, hora, detenidos.
2. ⚠️⚠️ **SINALOA · comunicado de la SEMAR del 10-oct** (`ARG-129-005`): fecha y lugar por evento; literal de Las Porras (**vence en 130**); 7 AEI de
   Varados y Siqueros frente a `ARG-125-005`.
3. ⚠️ **SINALOA · Escuinapa** (`ARG-129-003`, `-004`): hora de cada homicidio (si el de la vendedora fue antes de las 09:08 del 10-oct, pasa a 128).
4. ⚠️ **MICHOACÁN · Zamora** (`ARG-129-REC-001`): detenidos por el ataque; carpeta.
5. **OAXACA · Pinotepa** (`ARG-128-001`) · **EDOMEX · San José del Rincón** (`ARG-128-003`, tercera edición sin fecha) · **El Balcón** (`ARG-125-051`).

### 4.2 Seguimientos
Chipilo · Pachuca (630 o 640) · Los Pinos (inventario) · penal El Castillo · Naucalpan · Celaya · Michoacán, 12 cateos · Sombrerete · Borja ·
Corregidora · Zihuatanejo · Mixtequilla · Comonfort · Hermosillo · candidatos sin cotejar (Los Reyes, Huanímaro, Tetlatlahuca, Santa María Magdalena).

### 4.3 Sentencias candidatas
Navolato, 80 años · NL, tres personas (García y Santa Catarina) · **Ensenada: individualización de sanciones el 16-oct** · Tamaulipas FGJE-381 (sin
leer) · heredadas de 128. ⚠️ **Umbral asimétrico: sin fuente oficial no se integra.**

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- **Cada equipo regional abre con una búsqueda por día de la semana y sus entidades**, y **dedica al menos una búsqueda `site:` de armamento por
  entidad** antes de cerrar (en 129 el armamento cayó de 20 a 9 entidades revisadas).
- **PRIORIDAD SOBRE EL CICLO**: **armamento** BC, BCS, Son, Chih, Dgo · Coah, NL, Tamps, SLP · Jal, Nay, Mich · CDMX, Edomex, Mor, Pue, **Tlax (quinta
  vez: buscar el dominio sin `site:`)**, Hgo, Qro · Gro, Chis, Oax, QRoo · **sentencias** BCS, Son, Chih, Sin, NL, Gto, CDMX, Hgo, Camp, Oax, QRoo ·
  **alto impacto** BC, BCS, Son, Chih, Dgo, Coah, CDMX, Tlax, Camp. Después, **CICLO B** (Noreste + Golfo).
- **Criterio único de cobertura**: `REVISADA` = búsqueda dirigida que devolvió páginas del dominio oficial. Dominios confirmados en §3 del archivo de
  fuentes de 129.
- Boletín federal: triple consulta para las acciones del 10 y 11-oct (y el 9, sin indexar en 129).

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 129

| Trampa | Control |
|---|---|
| **`standard` no encuentra hechos de 48 h** | Pinotepa: `standard` devolvió un caso de marzo |
| **Un comunicado agregado sin fecha por evento** | SEMAR del 10-oct: cinco eventos, uno del 4-oct ya publicado y otro posible duplicado de 125 |
| **El equipo regional trae lo ya publicado** | Papantla (`ARG-128-REC-001`) traído como nuevo |
| **La republicación fecha mal el acto** | Enjambre: El Vigía lo republicó el 10-oct; titulares del 9-oct |
| **«Cero detenidos» sin cotejar el seguimiento** | Zamora: 4 policías detenidos por robo a las víctimas, no por el ataque |
| **Veredicto no es sentencia** | Ensenada: culpabilidad el 9-oct, pena el 16-oct |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- **Parta de `tools/datos-argos-129.py`**: copie y cambie los bloques `E`, `R` y `ARM`, las constantes y los textos de portada, Valoración,
  Conclusiones y cobertura. Plantilla: `reports/argos-2026-10-11.html`
  (`python3 tools/datos-argos-130.py reports/argos-2026-10-11.html reports/argos-<FECHA>.html`). Cambie la línea de `<title>` que reemplaza
  el generador (ARGOS 129 — 2026-10-11). El generador comprueba `WINDOW_DAYS = 2;` con `assert`: si la ventana toca otro número de fechas, sustitúyalo.
- Las filas `ARM` llevan `color`, `fecha`, `fecha_txt` y ahora `hora` propios.
- Móvil y texto: `python3 tools/gen-movil.py 130 <FECHA> 129 2026-10-11 <HORA>` y `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
  `gen-movil.py` ya no arrastra texto de método ni enlaces a filas de armamento sin destino.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-11 <FECHA>` → «validación OK».
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes. **Quince pases consecutivos, quince «CORREGIR».** Lánzelos sobre
  una versión estable y commiteada, con las notas de la ola.
