# ORDEN DE ARRANQUE — ARGOS 126

Documento de arranque para una **sesión nueva**, escrito al cierre de ARGOS 125 (corte 2026-10-07). La continuidad de ARGOS vive en el
repositorio: esta orden, `CLAUDE.md`, `reports/_pendientes.md` y `reports/argos-2026-10-07-fuentes.md` bastan para arrancar.

⚠️ **El mensaje listo para pegar está en `reports/_ordenes-ARGOS-126.txt`.** Este archivo es el detalle.

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'
git fetch origin
git branch -r | sed 's#origin/##' | sort
git merge --ff-only origin/main            # si main viene por detrás: buscar la rama más avanzada
ls reports/ | grep '^argos-' | tail -6
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 126**: última edición `argos-2026-10-07` (ARGOS 125) y **129 archivos** en `reports/`
(123 + cuatro de la edición + `_arranque-ARGOS-126.md` + `_ordenes-ARGOS-126.txt`).
✅ **ARGOS 125 se mergeó a `main` en fast-forward puro el 8-oct**, por instrucción del destinatario. Se construyó en
`claude/argos-criminal-intelligence-otiawj`. **Compruébelo igual**: si `main` viniera por detrás, haga el `ff-only` desde esa rama.

## BLOQUE 1 — IDENTIDAD

| Campo | Valor |
|---|---|
| Número | **ARGOS 126** |
| Ventana | **abre 2026-10-07 15:15 CDMX** —donde cerró ARGOS 125— y cierra a la **hora real de arranque**. Recalcule duración y densidad al sellar |
| Serie | 30 h 02 (121) · 87 h 21 (122) · 23 h 25 (123) · 46 h 19 (124) · **320 h 34 (125)** |
| Densidad | 0,25 · 0,19 · 0,04 · 0,30 · **0,16** — ⚠️ la de 125 **no es comparable**: trece días con un presupuesto de búsqueda que no escala |

⚠️ **Si la ventana de 126 es corta, espere recuperaciones**, no hechos propios (regla simétrica). Y **no compare totales con 125**.

## BLOQUE 2 — LECTURA OBLIGATORIA

1. `CLAUDE.md` íntegro (dos apartados por ficha; cartelón telegráfico; tres recuadros; el cartelón es para el mando).
2. `reports/_pendientes.md` — sección **ARGOS 125**.
3. `reports/argos-2026-10-07-fuentes.md` — §2 (modo de búsqueda), §7 (arbitrajes), §9 (`NO REVISADA` por entidad).
4. `reports/indice-arg-id.md` — `grep` por topónimo **antes de fichar cada hecho**. Cubre de `ARG-91-001` en adelante: diga «no
   figura en el índice, que cubre de ARGOS 91 en adelante».

## BLOQUE 3 — ⚠️⚠️⚠️ LA LECCIÓN DE ARGOS 125: EL MODO DE BÚSQUEDA

**Toda búsqueda en `WebSearch` con `mode:"extended"`.** En ARGOS 125 el modo `standard` tenía el índice **congelado hacia el
19-sep-2026**: **doce equipos y unas 210 búsquedas no fijaron un solo hecho** de la ventana. El `extended` encontró 51.
- **Primera búsqueda de la sesión: consulta de control** sobre un hecho conocido de las últimas 48 horas, en los dos modos. Si el
  `standard` no lo devuelve, **prohíbalo en todas las órdenes a los agentes**.
- **Un `SIN RESULTADO INDEXADO` obtenido en `standard` es `NO REVISADA`.**
- **Tope de 200 búsquedas por turno, compartido entre todos los agentes.** Reparta antes de lanzar: seis barridos × 14 + recall ×
  2 × 14 + encargos ≈ 130. **No lance dos olas en el mismo turno.**
- Las cifras de los republicadores del boletín federal llegan casi siempre por el **resumen** del buscador. Para los renglones de
  mayor peso, **una consulta con la cifra entre comillas devuelve el literal** (así se fijó Chihuahua: «55 mil 960 cartuchos»).

## BLOQUE 4 — DEUDA QUE ARGOS 126 HEREDA

### 4.1 Encargos, primero y sin negociar
1. ⚠️⚠️ **GUERRERO · Ajuchitlán, El Balcón** (`ARG-125-051`): **siete desaparecidos**, liberación condicionada a la cesión de tierras,
   amparo 412/2026, marcha a Palacio Nacional anunciada el 7-oct. ¿Localizados, detenidos, cifra inicial 8 o 13? **¿Hora del 24-sep
   anterior a las 06:41?** Si lo fuera: `-REC-` y fe de erratas.
2. ⚠️⚠️ **NAYARIT · Xalisco, La Curva** (`ARG-125-003`): **cifra de víctimas e identificaciones**. Y **JALISCO · Guadalajara**
   (`ARG-125-002`): comunicado oficial de la fosa.
3. ⚠️ **SINALOA · los AEI del sur**: tipología de 42 (El Rosario), 23 (Escuinapa-Mazatlán) y 14 (Mazatlán); **¿drones de ataque?**

### 4.2 Seguimientos
Comonfort (vinculación de los 2 detenidos) · Coatzacoalcos (proceso de los 5; ¿los 3 del 1-oct están entre ellos?) · Suchiapa (15 o
19 policías; móvil; fuga del 25-sep) · Hermosillo (orden contra Cristian Rubén «N») · **Culiacán, Parque Alamedas** (SSP Sinaloa,
fijar el día) · candidatos `-REC-` de ARGOS 123: Valle de Chalco–Ixtapaluca y León (Arroyo Hondo).

### 4.3 Sentencias candidatas — falta boletín oficial en todas
Juárez 58 a 4 m (26-sep) · Lagos de Moreno más de 11 años (26-sep) · José Manuel E. C. 37 a 6 m · Nuevo Laredo cuatro «N» · Feliciano
«N», Las Choapas. ⚠️ **Umbral asimétrico: sin fuente oficial no se integra.** Cancún, Coacalco, Morelia y Norma «N» quedaron
**fechados fuera de ventana**: no gaste búsquedas en ellos sin pista nueva.

## BLOQUE 5 — BARRIDO Y ROTACIÓN

- ✅ **Las 18 fiscalías que ARGOS 125 dejó sin revisar se barrieron en el alcance del 7-oct** (32 de 32; una sentencia integrable,
  Querétaro). **Prioridad que queda**: alto impacto/armamento en BCS, Hidalgo y Querétaro; Durango y SLP en alto impacto.
- **CICLO A** (Noroeste + Centro) se reanuda después.
- **El recall regional queda fijo dentro de cada barrido** (resuelto en ARGOS 125).
- **Boletín federal**: triple consulta; en 125 alternó **diario y agregado de tres días dos veces**. Un agregado cuyo tramo cae
  **íntegro** en la ventana se integra con «tramo» en el campo Hecho (`ARG-125-FE-002`); si el tramo cruza la apertura, no.

## BLOQUE 6 — TRAMPAS VERIFICADAS EN ARGOS 125

| Trampa | Control |
|---|---|
| **Índice `standard` congelado** | Consulta de control en los dos modos |
| **Señuelos de año** | Zamora/Ixtlán «26-sep» era 2023; Navolato era 2024; drones de Escuinapa, junio; desplazamiento de Guerrero, mayo. **Día de la semana contra calendario** descartó dos más |
| **Una cifra de un republicador puede no existir** | García: «4,771» no apareció en ninguna fuente; la FGR dio 5,093 |
| **Un «literal» puede estar truncado** | Santa María del Oro: la frase seguía con cintas, cargadores y 1,102 cartuchos |
| **Dos titulares suman dos hechos** | «7 cuerpos en Morelos» = 5 de Tlalnepantla + 2 de Yecapixtla |
| **Detención y delito son dos eventos** | Comonfort, Coatzacoalcos y Hermosillo |

## BLOQUE 7 — FORMA Y CONSTRUCCIÓN

- Dos apartados por ficha; panorama y ficha, nunca una tercera aparición; **un recuadro en portada con cinco ACCIONES** —no titulares—;
  tres recuadros máximo; sin `-FE-` en el cartelón; fichas de lo más reciente a lo más antiguo; agregados en bloque propio.
- Parta de `reports/argos-2026-10-07.html`. ⚠️ **`WINDOW_DAYS` del radar quedó en 14**: ajústelo a la duración de la ventana.
- ARGOS 125 se ensambló desde un **bloque único de datos** (fichas, panorama, `EVENTOS`, `EVENTOS_ARM` y totales derivados): evita
  que los totales y las fichas diverjan. Recomendable repetir el método.
- Móvil y texto **se generan**: `python3 tools/gen-movil.py 126 <FECHA> 125 2026-10-07 <HORA>` y
  `python3 tools/gen-texto.py reports/argos-<FECHA>.html reports/argos-<FECHA>.txt`.
- Validador: `node tools/validar.js reports/argos-<FECHA>.html 2026-10-07 <FECHA>` → «validación OK». **Ahora comprueba también que
  ningún hecho propio sea anterior a la apertura.**
- **Controles**: `editor-duplicidad` y `procedencia-cifras` como subagentes. **Diez pases consecutivos, diez «CORREGIR».** Y el
  arbitraje del coordinador **en las dos direcciones**, buscando el precedente que lo contradice.
