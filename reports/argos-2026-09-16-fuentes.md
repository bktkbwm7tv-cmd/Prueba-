# ARGOS 120 — Archivo de fuentes y método

**Corte**: 2026-09-16 · **Ventana**: 2026-09-13 08:28 → 2026-09-16 11:34 CDMX (**75 h 06 min**)
**Hora sellada**: verificada con `TZ=America/Mexico_City date` en el momento del ensamblaje.

Este archivo recoge lo que **no va al cartelón**: el registro del barrido, la rotación, las
limitaciones de herramienta y la deuda de método. El cartelón es para el mando; esto es para la
auditoría.

---

## 1. La base: esta edición arrancó sobre un árbol equivocado

**Es el fallo más caro de la edición y no es de contenido, es de base.** El contenedor asignó la rama
`claude/argos-2026-cartel-mobile-q87ahx`, que llegó en `a1cb1d5` —**trece ediciones por detrás**, con
**62 archivos** en `reports/` y `argos-2026-08-24` (ARGOS 106) como última edición—. El borrador de
ARGOS 120 se había redactado en una rama hermana (`claude/argos-119-reporte-seguridad-vlanol`) que
**nunca vio las ediciones 107 a 118**.

**Es exactamente el supuesto que el Bloque 0 de `_arranque-ARGOS-120.md` describe**, y que ya había
fallado trece veces seguidas. Se resolvió como manda: `git merge --ff-only origin/main`, avance limpio
a `5b91445`, **102 archivos**, última edición `argos-2026-09-13` (ARGOS 119). **La verificación de base
funciona cuando se ejecuta; el problema es que la rama sigue llegando desactualizada.**

**Consecuencia sobre el contenido**: el borrador afirmaba tres veces «no aparece en ningún corte
anterior del archivo» **sin haber podido comprobarlo**. Con el archivo restituido, el `grep` por
topónimo que ordena el Bloque 2 devolvió **cuatro cruces que el borrador no declaraba**:

| Topónimo | Qué encontró el índice | Resolución |
|---|---|---|
| **Xaltianguis** | `ARG-117-002` (5-sep, 16 detenidos), `ARG-118-001` (7-sep, 22 AEI), `ARG-118-REC-001` (veto territorial), `ARG-119-001` (9-sep, **Operación Xaltianguis**) | **Deslinde expreso contra los cuatro** en `ARG-120-012`. Hecho distinto: otra fecha, **otro municipio de hecho —Acapulco, no Chilpancingo—** y otro tipo de evento |
| **Huimanguillo / FIRT Olmeca** | `ARG-114-FE-006` (fe de erratas que **cerró por obsoleto** un agregado de 26 detenidos de **junio de 2026**) y `ARG-114-FE-007` (81 kg de metanfetamina, publicación del 31-ago) | **Riesgo real de recuento.** Deslinde expreso en `ARG-120-015`: otro rango, otros sub-eventos, otras cifras. **La coincidencia de fuerza y municipio no identifica un caso** |
| **Maneadero** | `ARG-105-REC-005` (detención de «El G1», célula de Maneadero, hecho del 23-ago) | Deslinde expreso en `ARG-120-019` |
| **Tecámac** | **ARGOS 93** (corte del 3-ago), como **punto de carga de una red de huachicol** | **El borrador afirmaba que no aparecía. Era falso.** Deslinde expreso en `ARG-120-003` |

**Las tres fórmulas de ausencia se corrigieron al rango real del índice**, que empieza en
`ARG-91-001` — la regla que abrió ARGOS 119 y que esta edición aplica en cinco fichas.

---

## 2. Rotación de cobertura

**Ciclo aplicado: CICLO A** — **Noroeste y Centro** encabezaron el triaje judicial. **Se declara por
qué**: ARGOS 119 aplicó el Ciclo C cuando por tabla le correspondía el A, y dejó abierto en
`_pendientes.md` si la serie reanudaba en A o continuaba tras C. **Esta edición reanuda en A.**

**Qué aportó la rotación**: el triaje judicial del **Noroeste** produjo la **sentencia de Salgueiro**
—la única integrada por esa vía— y **fechó el candidato heredado de Sinaloa**; el del **Centro** fechó
el candidato heredado de **Hueypoxtla** y localizó el candidato de **Coacalco**.

**Qué NO explica el ciclo, y se dice**: la segunda sentencia integrada, la de **Tamaulipas**, la
encontró el equipo del **Noreste**, que encabezaba con armamento. **El ciclo mejoró el rendimiento
judicial, no lo determinó.**

**Costo del ciclo, declarado**: las cuatro entidades `NO REVISADA` del módulo judicial —**Coahuila,
Nuevo León, San Luis Potosí y Zacatecas**— **son todas del Noreste**. Por la **regla de prioridad
sobre el ciclo**, deben **encabezar el triaje judicial de ARGOS 121**. Por tabla a la 121 le toca el
**Ciclo B (Noreste + Golfo)**, de modo que **prioridad y ciclo coinciden**: no hay conflicto que
arbitrar.

---

## 3. Cobertura declarada

**Armamento**: 32 de 32 entidades revisadas · **8** con aseguramiento integrado · **24** con
`SIN RESULTADO INDEXADO EN VENTANA` · **0** `NO REVISADA` · **0** `SIN ACTUALIZACIÓN CONSTATADA`.
Cuadre: 8 + 24 = 32.

**Judicial**: 28 de 32 fiscalías estatales revisadas · FGR revisada: **Sí** · **0** fiscalías estatales
con sentencia integrada · **4** con candidato declarado y no integrado · **24** con
`SIN RESULTADO INDEXADO EN VENTANA` · **4** `NO REVISADA`. Cuadre: 0 + 4 + 24 + 4 = 32.

⚠️ **COBERTURA DESIGUAL, DECLARADA**: Hidalgo y Tlaxcala recibieron una sola búsqueda combinada;
Colima, Nayarit y Aguascalientes no recibieron consulta dirigida a sus dominios propios; Coahuila y
Nuevo León se cubrieron principalmente por medios. **No debe leerse como cobertura equivalente** a la
de Chihuahua, Sinaloa o Veracruz.

`SIN ACTUALIZACIÓN CONSTATADA` queda en **0 en los dos módulos**: esa casilla exige **lectura directa**
del listado de boletines, imposible con el egreso bloqueado.

---

## 4. Vacío federal verificado, no supuesto

**No existe —o no está indexado por ningún emisor ni republicador— un boletín de acciones relevantes
del Gabinete de Seguridad que cubra el 14, el 15 o el 16 de septiembre.** Se verificó **en las tres
formas** que exige la regla de la triple consulta: por día suelto, por rango o agregado, y por título
sin restricción de dominio.

**El único disponible cubre el 11, 12 y 13 de septiembre**, publicado el 14-sep. **El emisor no
desglosa qué renglón corresponde a qué día**, de modo que solo se integró el renglón cuya fecha del
hecho queda fijada por cobertura independiente —**El Rosario**, madrugada del 13-sep, fijado por ocho
coberturas—. Los demás quedaron `FECHA NO FIJADA DENTRO DEL RANGO` y **se listan uno por uno con sus
cifras en el cartelón** para que ARGOS 121 **no los recuente como nuevos**.

---

## 5. Limitación de herramienta — dos, distintas, y la segunda es nueva

1. **Bloqueo de egreso sobre dominios oficiales.** `*.gob.mx` y los portales de fiscalías y
   secretarías estatales devuelven **403 por política de red del entorno**. Ningún portal se leyó por
   acceso directo; toda consulta institucional se sustituyó por búsqueda dirigida, **con la sustitución
   anotada ficha por ficha**. `docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar**.

2. ⚠️ **NUEVA: el bloqueo no se limitó a los dominios oficiales.** En la sesión que produjo el
   borrador, la herramienta de lectura directa devolvió bloqueo **en todos los dominios probados**,
   incluidos medios nacionales y regionales, comprobado de forma directa sobre una URL de medio
   nacional. **Ninguna página de este corte se leyó íntegra.** Todo lo publicado se sostiene en los
   extractos del buscador más la fecha en la ruta de las URL.

**Por eso el techo de confianza de esta edición es ★★★☆☆ y no el ★★★★☆ habitual.** No es una
degradación del criterio: es una degradación de la herramienta, **y se declara en vez de disimularse**.
⚠️ **ARGOS 121 debe volver a comprobarlo**: si la lectura directa de medios vuelve a funcionar, el
techo recupera ★★★★☆ y debe hacerse constar.

---

## 6. Deslinde de duplicidad — el hallazgo de control del corte

Los **84 artefactos explosivos improvisados de «La Noria de San Antonio»** aparecen en **dos
publicaciones distintas con el MISMO desglose** —84 AEI, 2 armas largas, 18 cargadores, equipo táctico
y placas balísticas—, una atribuida al **7-sep en el municipio de San Ignacio** y otra a **Mazatlán
dentro del rango 11-13-sep**. Cifras idénticas, dos municipios y dos fechas:
`POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN`.

**De haberse integrado habrían sido el mayor volumen de AEI del archivo**, por encima de los 27 de
Escuinapa y los 26 del corte anterior. **Es la cifra que este corte estuvo más cerca de publicar mal.**

---

## 7. Cifras del corte y su procedencia

Todos los totales son **cálculo propio de ARGOS**: **ninguna autoridad publicó un agregado nacional
del corte**. Comprobaciones aritméticas ejecutadas sobre las filas integradas:

| Total | Desglose | Cuadre |
|---|---|---|
| **92 armas** | 2 cortas + 71 largas + 19 sin categoría | ✔ |
| **9,194 cartuchos** | 6,498 + 2,294 + 201 + 188 + 13 | ✔ |
| **178 cargadores** | 145 + 30 + 2 + 1 | ✔ |
| **25 detenidos** | 6 + 6 + 5 + 4 + 2 + 1 + 1 | ✔ |
| **185 años 3 meses** | 29a 3m + (52 × 3) | ✔ |
| **Densidad 0,25 h/hora** | 19 ÷ 75,10 frente a 19 ÷ 117,83 = 0,16 | ✔ |

⚠️ **La densidad y la duración se recalcularon al sellar la hora real**, no se heredaron del borrador,
que traía 10:04, 73 h 36 min y 0,26. **Sellar la hora cambia los dos cocientes y es fácil olvidarlo.**

⚠️ **19 de las 92 armas se publicaron SIN CATEGORÍA** —el 20,7 %— y **ninguna con número de serie ni
calibre por pieza**, frente a cuatro con calibre en el corte anterior. **Es un retroceso de un campo
que no cuesta nada al emisor.**

---

## 8. Deuda de método que esta edición deja abierta

⚠️ **SE DECLARA SIN ATENUAR: esta edición NO pasó los controles formales de `CLAUDE.md`.**

| Control | Estado real |
|---|---|
| `barrido-regional` ×6 | **Ejecutado en la sesión del borrador**, no en la de publicación. La cobertura declarada procede de ese barrido |
| `editor-duplicidad` | **NO ejecutado como subagente.** Se hizo en su lugar el **`grep` por topónimo contra el índice restituido**, que produjo los cuatro cruces de la sección 1. **Es menos que el control completo**: no auditó paridad escritorio/móvil ni repetición entre secciones |
| `procedencia-cifras` | **NO ejecutado.** Las cifras se verificaron por **cuadre aritmético** sobre las filas integradas (sección 7), **no contra el fragmento literal de cada fuente** |

**Qué significa**: las cifras cuadran entre sí y con el cartelón, y los deslindes están hechos contra
el archivo completo. **Lo que no se hizo es la verificación de cada número contra su fragmento
citable.** ⚠️ **ARGOS 121 debe tratar las cifras de esta edición como `HEREDADO — NO REVERIFICADO` si
las cita**, y **no como cifras auditadas**.

**Por qué se publicó así**: la edición se levantó sobre una base restituida a mitad de sesión y el
destinatario pidió el producto del día. **Se prefirió publicar con la deuda declarada antes que no
publicar** — pero la deuda es real y aquí queda.

---

## 9. Herramienta nueva de esta edición

**`tools/gen-texto.py`** — deriva la versión en texto del **cartelón ya publicado**, en vez de
conservarla aparte. Nace de un fallo real de este corte: el `.txt` del repositorio seguía siendo el
borrador previo —hora 10:04, ventana de 73 h 36 min, densidad 0,26 y **sin los cuatro deslindes**—, de
modo que **texto y cartelón afirmaban cosas distintas sobre el mismo corte**.

Mismo criterio con el que `tools/gen-movil.py` deriva la versión de teléfono: **lo que no se deriva,
diverge**.

---

## 10. Fuentes

**Institucionales**: Gabinete de Seguridad federal (boletín del 11, 12 y 13-sep, **vía
republicadores**) · Gabinete de Seguridad de Tabasco / FIRT Olmeca · FGR (dos comunicados de
sentencia) · SEDENA · SEMAR · Guardia Nacional · SSPC · ANAM · **FGE de Quintana Roo (comunicado
propio — única fuente primaria institucional del corte)** · Fuerza Civil de Nuevo León · FGE de
Campeche, Guanajuato y Guerrero · FESC de Baja California · SSP Municipal de Morelia.

**Nacionales**: Infobae · El Financiero · El Heraldo de México · La Silla Rota · Excélsior · El
Universal · Milenio · Latinus · La Razón · El Informador · unoTV · Aristegui Noticias · La Crónica de
Hoy · SDP Noticias · Forbes México · PorEsto · Publimetro · TV Azteca · Quadratín · Cadena Láser · La
Opinión · N+.

**Regionales**: MVS Noticias · Diario de Yucatán · El Diario de Chihuahua · La Gaceta Chihuahua ·
Somos Juárez · Es Lo Que Hay Juárez · La Parada Digital · El Bordo · Ráfaga Noticias · Zolo Noticias ·
Los Noticieristas · Noroeste · Sinaloa Hoy · Primera Línea · Valija Diplomática · Notiregión · RED
Michoacán · Grupo Marmor · 860 Líder Informativo · El Sol de Chilpancingo · Quadratín Guerrero ·
24 Horas Quintana Roo · Digital News QR · Argón México · Diario de Chiapas · Novedades de Tabasco ·
Diario de Tabasco · Tabasco Hoy · La Región Tamaulipas · Expreso de Tamaulipas · Hora Cero · Hoy
Tamaulipas · Red Metropolitana · Diario Tijuana · El Siglo de Torreón · Info7 · Noticias SIN.

**Republicadores usados como vía y NO como fuente independiente**: RED113 · Talla Política · Certeza
Diario · Eleese Noticias. ⚠️ **Varios republicadores del mismo boletín no son fuentes independientes**:
la corroboración de `ARG-120-010`, `ARG-120-015` y las dos sentencias es **débil por construcción**.

---

## 11. Vacíos de publicación que el mando debe conocer

- **fiscaliaguerrero.gob.mx**: sin publicar indexable. **Tercera edición consecutiva.** Guerrero aporta
  hechos **sin una sola fuente institucional** por cuarto corte seguido.
- **SSC y FGJ de la Ciudad de México**: **cero boletín** sobre un doble homicidio en la madrugada del
  16-sep en el centro de la capital.
- **FGE de Guanajuato**: publicó **con fecha en la ruta** el cateo del corte anterior y **nada** sobre
  el ataque rojo de San Francisco del Rincón. **El mismo emisor publica sus acciones y no sus muertos.**
- **gabinetedeseguridad.gob.mx/resultados/**: **décima verificación consecutiva sin cifra utilizable.**
  Dominio indexado, rutas sin fecha, acceso directo 403, trampa de año acreditada.
