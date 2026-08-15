# ARGOS — Pendientes vivos

Archivo de traspaso entre ediciones. **Cada corte lo actualiza como último paso**, antes de commit.
Sirve para que una sesión nueva pueda arrancar sin que nadie tenga que recordar ni transcribir la
lista de seguimientos: basta leer este archivo y la edición anterior.

Convención: cada entrada indica desde qué edición está abierta, qué hay que buscar y qué la cierra.
Cuando algo se resuelve, se mueve a "Cerrados recientemente" con una línea, y se borra de ahí en la
segunda edición siguiente.

**Última actualización**: ARGOS 98 (corte 2026-08-15).

---

## Seguimientos judiciales abiertos

| Desde | Caso | Qué falta | Qué lo cierra |
|---|---|---|---|
| ARGOS 97 | **Funcionarios de Medio Ambiente del Edomex** (`ARG-97-004`), extorsión a verificentros y gasolineras | La audiencia para resolver la vinculación a proceso de Raúl "N" y Carlos Eduardo "N" estaba fijada para el **sábado 15-ago, 10:30 h**, Juzgado de Control del Distrito Judicial de Chalco — posterior al cierre de ARGOS 98 (07:29) | Resolución de la audiencia: vinculación concedida o negada |
| ARGOS 92 | **Gabriela "N"**, secuestro agravado, Villas del Pedregal, Morelia | Fallo de culpabilidad del 11-ago confirmado; la **audiencia de individualización de sanción sigue sin celebrarse**. Sin pena impuesta, no entra en el módulo de sentencias | Pena impuesta y publicada |
| ARGOS 96 | **Ruffo Appel / Ingemar**, huachicol fiscal (`ARG-98-SEG-001`) | Sin resolución de fondo del amparo de Ricardo Thompson Navarro — solo suspensión provisional. Ruffo Appel promovió amparo análogo el 12-ago. **Guadalupe Hernández Hinojosa: sin información verificable** de que haya promovido uno | Sentencia de amparo (fundado/infundado), o amparo de Hernández Hinojosa |

## Vacíos de publicación que siguen sin resolverse

| Desde | Caso | Estado |
|---|---|---|
| ARGOS 97 | **Agregado de sentencias de Veracruz** — "53 resoluciones, 11 condenatorias" (comunicado del 13-ago, cubre 6–12 ago) | Solo se desglosó Cosamaloapan (`ARG-97-SEN-003`). **Las otras 10 condenatorias siguen sin nombre, delito ni pena**. Segundo corte consecutivo intentándolo. `comunicacion.fiscaliaveracruz.gob.mx` sigue bloqueado |
| ARGOS 98 | **Jalisco, 19 sentenciados del CJNG** (10-ago) | Confirmado como vacío real, pero **sin boletín institucional localizado**. Antes de integrarlo a un conteo nacional hace falta el comunicado del PJF o de la fiscalía especializada |
| ARGOS 98 | **La Paz, BCS**, abuso sexual (11-ago) | Vacío confirmado pero con **solo dos fuentes regionales**, sin institucional ni nacional. `Pendiente de corroboración independiente` |

## Contradicciones abiertas

| Desde | Caso | Detalle |
|---|---|---|
| ARGOS 98 | **La Piedad, Michoacán** (`ARG-98-002`) | Número de fallecidos: 3 muertos + 1 adolescente herido (Infobae, El Heraldo, La Jornada, LatinUS) frente a 4 abatidos (Quadratín Michoacán, Atiempo). Publicadas ambas versiones sin arbitrar |
| ARGOS 98 | **Lázaro Cárdenas, Michoacán** (`ARG-98-ARM-003`) | Fecha del hecho en disputa: el Gabinete de Seguridad lo ubica el 13-ago, los medios regionales el 14-ago. **No integrado** al total nacional hasta resolverlo |
| ARGOS 98 | **"Operación Sable", Mazatlán** (13-ago, `ARG-97-ARM-003`) | Cifras discrepantes para el mismo operativo: 1 cargador / 15 cartuchos según una búsqueda de ARGOS 98, frente a 9 cargadores / 55 cartuchos publicados en ARGOS 97. Sin determinar si son dos intervenciones o un error de transcripción. **No se corrigió unilateralmente** la edición anterior |
| ARGOS 98 | **Privada Amberes, Ciudad Juárez** | Ataque a vivienda de abogados con fecha no determinable (13 o 14-ago), fuente única. No integrado |

## Deuda editorial y de método

| Desde | Asunto | Acción pendiente |
|---|---|---|
| ARGOS 98 | **Índice de ARG-ID** | No existe. El cruce contra el archivo depende hoy de abrir el archivo correcto por intuición, lo que deja de ser viable a partir de unas decenas de ediciones. Falta `reports/indice-arg-id.md` con ARG-ID · fecha · entidad · municipio · cifras clave · edición |
| ARGOS 98 | **Lista blanca de egreso** | `docs/solicitud-lista-blanca-egreso.md` está redactada y lista para tramitar. Mientras no se apruebe, el techo de confianza de todo el producto sigue en ★★★★☆ |
| ARGOS 98 | **Generación de la versión móvil** | El script de construcción quedó desfasado tras pasar a 6 páginas: reconstruye la estructura antigua. Hoy las ediciones móviles se editan a mano sobre la anterior. Conviene rehacerlo o documentar que solo `tools/gen-movil-svg.js` es reutilizable |
| ARGOS 98 | **Controles editoriales** | `editor-duplicidad`, `procedencia-cifras` y `barrido-regional` ya existen y son obligatorios antes de publicar (ver CLAUDE.md). `procedencia-cifras` y `barrido-regional` **aún no se han ejecutado nunca** — ARGOS 99 es su primera prueba de campo |

## Cerrados recientemente

- **Huajicori, Nayarit** — fe de erratas publicada en ARGOS 98 (`ARG-98-FE-001`). La cifra de
  "8 cargadores, 235 cartuchos" queda retirada como dato citable; el resto del aseguramiento
  (1 fusil Barrett, 4 armas largas, 2 AEI, 1 inhibidor de drones) está confirmado. Señalado sin
  resolución durante cuatro ediciones. *Cerrado.*
- **Cateo en Ciudad Juárez del 13-ago** — contradicción 2 vs. 4 detenidos resuelta en ARGOS 98 con
  boletín institucional directo de la Fiscalía de Chihuahua: **son 2**. El "4" era conflación con un
  cateo de trata de junio de 2026 en la misma colonia. *Cerrado.*
- **Apatzingán, Michoacán (11-ago)** — figuraba como vacío de cobertura desde ARGOS 97; ARGOS 98 lo
  **anuló**: no era vacío, estaba publicado y contabilizado como `ARG-95-ARM-001`. Sus cifras no
  deben reintegrarse a ningún total. *Cerrado.*

---

## Cómo arrancar la edición siguiente

Sesión nueva, un solo mensaje:

> Haz el ARGOS 99 de hoy siguiendo `CLAUDE.md`. Rama `claude/argos-99-<sufijo>`. Lee
> `reports/_pendientes.md` y la edición anterior (`reports/argos-2026-08-15*`) para no duplicar
> hechos ni perder seguimientos. Verifica antes si la rama de ARGOS 98 ya se mergeó a `main`; si no,
> trae sus cambios primero.

Antes del commit, ejecutar los tres controles obligatorios de CLAUDE.md (`editor-duplicidad`,
`procedencia-cifras`, `barrido-regional` ×6) y **actualizar este archivo** con los pendientes que
deje la nueva edición.
