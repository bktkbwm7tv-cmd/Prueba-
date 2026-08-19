# ARGOS 102 — Registro de fuentes (auditoría)

Corte: 2026-08-19 · Ventana de hechos: **2026-08-18 13:37 CDMX → 2026-08-19 07:45 CDMX**.
Continuación estricta de ARGOS 101 (corte 2026-08-18). Este documento respalda
`argos-2026-08-19.html` y `argos-2026-08-19-movil.html`, y existe para que todo `SIN DATO` de la
edición sea demostrable.

Ventana efectiva: **~19 horas**, de la tarde del martes a la mañana del miércoles. Es
sustancialmente más corta que la de ARGOS 101 (~35 h). Esa diferencia importa para comparar
volúmenes: **un corte con menos hechos que el anterior no indica menos violencia, sino una ventana
de poco más de la mitad de duración** — y, en esta edición, además, una frontera de ventana que
afecta a la mayoría de los candidatos (ver abajo).

---

## Limitación metodológica — decimotercera edición consecutiva con el egreso bloqueado

**Sonda de entorno ejecutada al inicio de la sesión por el coordinador**, con `curl` directo:

| Host | Resultado |
|---|---|
| `www.gob.mx/sspc/prensa` | `curl: (56) CONNECT tunnel failed, response 403` |
| `www.gob.mx/guardianacional/prensa` | 403 al CONNECT |
| `comunicacion.fiscaliaveracruz.gob.mx/archivo/` | 403 al CONNECT |

Es una **denegación por política de la organización en el proxy de salida**, no un fallo de
herramienta ni un problema de los portales. No se intentó rodearla.

**Consecuencia operativa aplicada**: se prohibió `WebFetch` a los tres equipos de verificación
prioritaria y a los seis barridos regionales, conforme a la lección 4 de ARGOS 101. **Los nueve
equipos lo respetaron: cero usos de `WebFetch` en toda la edición.**

**Cero portales leídos por acceso directo, de ~128 objetivo.** Ningún
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de esta edición puede presentarse como vacío
institucional verificado; la casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Techo de confianza efectivo: ★★★★☆** — decimotercera edición consecutiva sin superarlo.

---

## El problema que define a esta edición: la frontera de ventana

**De los cinco hechos del corte, uno solo tiene demostrada su pertenencia a la ventana.**

| Hecho | Publicación | ¿Dentro de ventana? |
|---|---|---|
| `ARG-102-001` Poza Rica / Xalapa, Veracruz | **19-ago, fecha en la ruta** (`lasillarota.com/veracruz/estado/2026/8/19/`) | **SÍ — DEMOSTRADA** |
| `ARG-102-002` Los Reyes, Michoacán | 18-ago, fecha en la ruta; **hora no publicada** | `FRONTERA DE VENTANA` |
| `ARG-102-003` Zinapécuaro, Michoacán | 18-ago, fecha en la ruta; **hora no publicada** | `FRONTERA DE VENTANA` |
| `ARG-102-004` Tijuana, Baja California | 18-ago, fecha en la ruta; **hora no publicada** | `FRONTERA DE VENTANA` |
| `ARG-102-005` Alfajayucan, Hidalgo | **Ninguna URL la fecha**; el 18-ago lo afirma el resumidor | `PENDIENTE DE ANCLA FECHADA` |

**Causa estructural, no incidental**: la ventana de ARGOS se declara al minuto para garantizar que
ninguna edición solape a otra, pero **las fuentes publican al día**. La fecha en la ruta de una URL
fija el día, prácticamente nunca la hora. Con una ventana que abre a las 13:37, **todo lo publicado
ese día queda indeterminado**.

**Regla adoptada y consagrada en `CLAUDE.md`** ("Frontera de ventana: cuando la fuente no publica la
hora"): el hecho se integra a **la edición que lo ve primero** —porque la anterior ya cerró sin él y
descartarlo fabricaría un vacío—, con marca **permanente y auditable**. Si aparece un ancla horaria
y resulta pertenecer a la ventana anterior, se corrige por fe de erratas y se retira del total donde
se contó.

**Declaración obligada al lector**: los totales de este corte **no son directamente comparables** con
los de ediciones cuyos hechos sí quedaron fijados dentro de ventana.

---

## Verificación PRIORIDAD 1 — ejecutada primero y en solitario

Se aplicó la lección 1 de ARGOS 101: la verificación prioritaria se ejecutó **antes de lanzar los
seis barridos y con la sesión para ella sola**. Consumo: **34 búsquedas de 34 asignadas** (10 + 12 +
12), los tres equipos con el tope agotado.

**Resultado de conjunto**: a diferencia de ARGOS 101, donde el rendimiento fue de delimitación,
**esta verificación cerró casos**. Uno de los tres pendientes quedó resuelto con cifra exacta, otro
produjo dos correcciones mayores al archivo, y el tercero cambió de naturaleza.

### 1-A · Boletín federal del 14-15-16 de agosto — desglose por entidad CONFIRMADO

- **Veredicto**: `CONFIRMADO POR CONCORDANCIA DE FRASE EXACTA — DOCUMENTO NO LEÍDO ÍNTEGRO`.
  Las consultas entrecomilladas `"nueve artefactos explosivos improvisados"` y
  `"13 mil 300 cartuchos"` devolvieron el boletín y sus reproducciones como resultados principales,
  lo que **prueba que esas cadenas están en el texto indexado** y no solo en el sintetizador. Es un
  escalón por encima del `NO CONFIRMADO` en que ARGOS 101 las dejó, y un escalón por debajo de
  `CITABLE` estricto.
- **Tres reproducciones íntegras**: `tallapolitica.com.mx/…-14-15-y-16-de-agosto-de-2026/`,
  `red113mx.com/2026/08/…` (fecha de mes en ruta) y `laprensa.mx/notas.asp?id=810302`.
  Son **copias del mismo texto, no corroboración independiente**: la confianza queda en **Medio**.
- **Dato nuevo de mayor valor**: el renglón de Michoacán es de **La Piedad**, y está **vinculado a la
  agresión armada contra militares del 14-ago** en la carretera La Piedad–Zamora. Eso cambia su
  color: **no es aseguramiento limpio 🟢, es armamento asociado a un ataque contra autoridades → 🔴**.
- **El vacío del 17-ago NO EXISTE**: `gob.mx/sspc/prensa/…-del-17-de-agosto-de-2026`, en **formato
  diario**. Es el segundo falso vacío consecutivo del mismo emisor. **El vacío real es del 18-ago.**
- **Cambio de canal declarado por el emisor**: a partir del **1-sep-2026** los reportes diarios
  preliminares migran a `gabinetedeseguridad.gob.mx/resultados/` (ancla:
  `lasillarota.com/nacion/2026/8/18/`).

### 1-B · Veracruz — las condenatorias del lote del 13-ago: cero desglosadas, sexta edición

- **Resultado: 0 desglosadas.** Pero el pendiente **deja de ser deuda de búsqueda**.
- **Hallazgo estructural**: `comunicacion.fiscaliaveracruz.gob.mx` **sí expone archivo fechado**
  `/AAAA/MM/DD/` y `/AAAA/MM/` — verificado en `/2026/02/20/`, `/2026/04/12/`, `/2026/05/08/`,
  `/2026/05/` y en el dominio hermano `fiscaliaveracruz.gob.mx/2026/04/08/`. **La rebanada de
  agosto-2026 no está en el índice**, y los boletines individuales llevan **slug con caracteres
  unicode decorativos y sin fecha**.
- **Reetiquetado**: `BLOQUEADO POR EGRESO — NO REINTENTABLE POR BÚSQUEDA`. La ruta fechada existe
  pero **solo es explotable por lectura directa**. Insistir con `site:` una séptima edición es gasto
  sin rendimiento. La recomendación de método de ARGOS 101 **queda ejecutada y cerrada**.

### 1-C · Coronango y Tijuana — dos correcciones mayores

**Coronango, Puebla** — la sentencia existe, es integrable, **y la premisa documental de ARGOS 98
era falsa**:

- El boletín cuyo *slug* dice `2168-fallo-condenatorio-por-violacion-equiparada-en-agravio-de-su-sobrina`
  **es de otro caso**: **Juan Carlos "N", 22 años, hecho del 5-may-2019 en Barrio Cuapilco**.
- El boletín correcto es `fiscalia.puebla.gob.mx/Home/Comunicado/` + GUID `ae5a295c-672e-4ec9-ae87-69d075d4f5ea`,
  **sin fecha en la ruta**, y **ARGOS 97 ya lo tenía**: ARGOS 98 lo sustituyó por el erróneo porque
  su *slug* se leía. Es una **regresión de una edición a la siguiente**.
- **Título institucional fijado**: "Logra la FGE sentencia de más de 26 años de prisión…". La FGE de
  Puebla mantiene **dos familias de titulación** —sentencia impuesta y firmeza en alzada (60, 50,
  35 y 23 años)— y **este boletín es de la primera**: la firmeza **no la sostiene la fuente oficial
  citada**, sino el titular de `diariomomento.com`. Se publica
  `FIRMEZA NO INFORMADA POR LA FUENTE OFICIAL CITADA`.
- **Publicación fijada el 11-ago-2026** por `intoleranciadiario.com/articles/inseguridad/2026/08/11/`
  → ventana de **ARGOS 95**, no de 102. Se integra como **recuperación de omisión**, sin sumar.
- **Multa de 212 UMA**: segunda aparición en consulta independiente, **sin ancla documental**. No se
  integra y **no se convierte a pesos** (sería cálculo propio sin valor de UMA declarado).
- **Contradicción sobre la víctima, arbitrada**: cinco medios sostienen que es una niña de corta
  edad —uno de ellos nacional, con el dato en el *slug*— frente a un medio aislado que la describe
  como adolescente. Se publica **"niña", sin la edad exacta**, por tratarse de víctima infantil de
  delito sexual.

**Tijuana (`ARG-101-008`)** — el homicidio **sí cae dentro de la ventana de ARGOS 101**:

- Hecho el **lunes 17-ago por la tarde, poco antes de las 15:00 h de Tijuana** (≈16:00 CDMX;
  *la conversión de huso es cálculo propio de ARGOS*), en **Av. Negrete entre Segunda y Aldrete**,
  Zona Centro. Víctima: "Israel", 49 años, **identificación preliminar**. Tres casquillos percutidos.
- **Segundo hallazgo no previsto**: **sí hubo aseguramiento** — 1 arma de fuego calibre 9 mm—,
  contra lo que publicó ARGOS 101. Procede de resumen en tres consultas:
  `1 ARMA CORTA 9 MM — PENDIENTE DE FRAGMENTO CITABLE`, **no se integra al total**.
- El evento **deja de ser fuente única**: cinco cabeceras regionales, dos con fecha en ruta.
- **Cero respaldo institucional**: `fgebc.gob.mx` no devolvió el boletín. Se registra
  `CONSULTADO POR BÚSQUEDA DIRIGIDA — SIN RESULTADO INDEXADO`, **nunca "portal revisado"**.

---

## El hallazgo más grave del corte: la masacre que ARGOS 101 no registró

**Tlapa de Comonfort, Guerrero — 18-ago-2026, ~02:40–02:45 h.** Grupo armado irrumpe en un
domicilio de la calle Los Girasoles, colonia Contlalco; asesina a cuatro integrantes de una familia,
rocía gasolina e incendia la vivienda. Cuerpos hallados **calcinados**. **Siete personas escapan.**

Víctimas: **Teófilo Amado de Jesús** (48), **Margarita Ortiz García** (46), **Paulina Ortiz García**
(75) y **Erlan Ortiz Ortiz, de seis años**. Familia originaria de **Cochoapa el Grande**. FGE de
Guerrero con carpeta abierta, PIM y Servicios Periciales en el lugar. **Sin detenidos. Sin
armamento publicado.**

**Cinco fuentes con fecha en la ruta**: `proceso.com.mx/nacional/estados/2026/8/18/…378279.html` ·
`yucatan.com.mx/mexico/2026/08/18/…` · `elsoldechilpancingo.mx/2026/08/18/…` ·
`diario.mx/nacional/2026/aug/18/…1133872.html` · `eldiariodechihuahua.mx/nacional/2026/aug/18/…828854.html`.
Regionales sin fecha en URL: Quadratín Guerrero, El Sur de Acapulco.

**02:40 del 18-ago es casi once horas ANTES del cierre de la ventana de ARGOS 101**
(18-ago 13:37). Cae de lleno dentro de ella.

**Verificación independiente ejecutada por el coordinador**, no delegada: la búsqueda de "Tlapa",
"Contlalco" y "Cochoapa" en `argos-2026-08-18.html`, `argos-2026-08-18-fuentes.md` y
`argos-2026-08-18-movil.html` devuelve **una sola coincidencia por subcadena, y es "Matlapa"**,
municipio de San Luis Potosí correspondiente a un caso judicial distinto. **La omisión queda
confirmada por lectura directa del archivo.**

> **Consecuencia**: la afirmación de ARGOS 101 de **cero eventos rojos** en su ventana es **falsa**,
> y su `NO DETERMINABLE` descansaba sobre una ausencia inexistente. Su valoración queda rectificada.

> **Lección de método**: ARGOS 101 formuló para los emisores que "un `SIN DATO` confirmado por
> repetición no queda confirmado, queda repetido". **Vale igual para los territorios**: cuando una
> región declara **cero hechos con todas sus entidades consultadas**, la hipótesis que debe probarse
> primero **no es la calma del territorio, sino el fallo de la cobertura**. En este corte esa
> hipótesis se probó en las tres regiones que cerraron ARGOS 101 en cero y **resultó cierta en dos**.

---

## Presupuesto de búsqueda

| Equipo | Tope | Consumo | Nota |
|---|---|---|---|
| Verificación PRIORIDAD 1 — boletín federal | 10 | **10** | Ejecutada **primero y en solitario** |
| Verificación PRIORIDAD 1 — Veracruz | 12 | **12** | Ídem |
| Verificación PRIORIDAD 1 — Coronango y Tijuana | 12 | **12** | Ídem |
| Barrido Noroeste | 20 | 20 | Tope alcanzado |
| Barrido Noreste *(Ciclo B — triaje judicial)* | 20 | 20 | Tope alcanzado |
| Barrido Occidente | 20 | 20 | Tope alcanzado |
| Barrido Centro | 20 | **19** | Una de reserva sin usar |
| Barrido Golfo *(Ciclo B — triaje judicial)* | 20 | 20 | Tope alcanzado |
| Barrido Sureste | 20 | 20 | Tope alcanzado |
| Coordinación | — | **0** | Sonda de egreso por `curl` y verificación directa del archivo con `grep`: **sin consumo de búsqueda** |
| **Total** | **154 asignadas** | **153 de un techo de 200** | **Los nueve topes respetados** — segunda edición consecutiva |

### Rotación de cobertura — Ciclo B, aplicada y declarada

La mecánica quedó **escrita en `CLAUDE.md` en esta edición**, cerrando el pendiente que ARGOS 101
dejó abierto tras validarla sin formalizarla. Ciclo fijo de tres ediciones:
**A** (Noroeste + Centro) · **B** (Noreste + Golfo) · **C** (Occidente + Sureste). A ARGOS 102 le
correspondió el **Ciclo B**.

**Rendimiento, declarado sin adorno**: **ninguna de las dos regiones produjo una sentencia
integrable**, de modo que la rotación **no repitió el resultado de ARGOS 101**. Lo que sí produjo es
de otra naturaleza:

- El **Noreste** descubrió que **dos de sus cinco entidades tenían el dominio mal registrado o
  ausente** y que **Nuevo León no tiene sala de prensa indexable en absoluto** —comunica por
  Facebook y X—. Su "cero hechos pese a diez portales" de ARGOS 101 **era en parte un artefacto del
  directorio, no del territorio**.
- El **Golfo** resolvió el **arbitraje de las condenatorias de Veracruz**, abierto desde ARGOS 97, y
  localizó el evento 🔴 de Cárdenas que ARGOS 100 no registró.

**La rotación se declara también cuando no rinde lo esperado.** Al Ciclo C (ARGOS 103) le
corresponden **Occidente y Sureste**.

---

## Hechos de la ventana — respaldo por evento

### ARG-102-001 — Poza Rica / Xalapa, Veracruz (🟢 VERDE) — **el único anclado del corte**

- **Hecho**: la Fiscalía Especializada en Atención de Denuncias por Personas Desaparecidas de la FGE
  de Veracruz obtiene **imputación y vinculación a proceso de 7 personas** por **desaparición
  cometida por particulares**; control de detención calificado de legal y **prisión preventiva
  oficiosa**. **Causa penal 342/2026.** Vinculados: Pedro Yeudiel "N" (señalado como líder),
  Wilber Michell "N", Jean Martín "N", Ronaldo Alvino "N", Álvaro Severiano "N", Jatzely "N" y
  José Luis "N".
- **Hecho de origen**: desaparición de **Karime Argüelles Aguilar**, 29 años, trabajadora de la
  Sefiplan y extitular de la oficina de Hacienda en Poza Rica, el **12-jun-2026**.
- **Fuente institucional**: `comunicacion.fiscaliaveracruz.gob.mx/vinculados-a-proceso-como-probables-responsables-del-delito-de-desaparicion-cometida-por-particulares/`
  — **slug sin fecha**, patrón conocido del portal.
- **Fuente nacional con fecha en ruta**: `lasillarota.com/veracruz/estado/2026/8/19/…525050.html`.
  **Es la única URL de todo el corte que fija una publicación dentro de la ventana.**
- **Corroboración**: Excélsior, `xeu.mx/policiaca/1429862/`, `observadorveracruzano.com/147416-2/`,
  las tres sin fecha en URL.
- **Sin aseguramiento de armamento** → fuera del módulo de la Sección 1. Confianza **★★★★☆ / Alto**.
- **NO ES SENTENCIA**: excluido expresamente del módulo judicial.

### ARG-102-002 — Los Reyes, Michoacán (🔴 ROJO)

- **Hecho**: en la localidad de **Los Palillos**, cerca del límite con **Cotija**, civiles armados
  agreden a un **patrullaje de reconocimiento terrestre del Ejército**, que repele la agresión.
  **5 presuntos agresores abatidos**, sin identidades y **sin detenidos**. Armas largas y cartuchos
  asegurados **sin cantidad publicada**.
- **Fuentes con fecha en ruta**: `medianews.mx/index.php/2026/08/18/…` y `changoonga.com/2026/08/18/…`.
  Corroboración sin fecha: Indicio Michoacán y Quadratín — **con la advertencia de que la nota de
  Quadratín aparece replicada en cinco de sus portales estatales y es una sola fuente, no cinco**.
  Blog del Narco marcado `NO OFICIAL`.
- **Sin fuente institucional**: no se localizó comunicado de SEDENA, de la 21ª Zona Militar, ni de la
  SSP o la FGE de Michoacán. Confianza **★★☆☆☆ / Bajo**.
- **Clasificación 🔴** por el **criterio de iniciativa** consagrado en `CLAUDE.md` en esta edición:
  la agresión la inició el grupo criminal contra personal en patrullaje = **ataque contra
  autoridades**. **El número de abatidos no determina el color.**
- **Evento cualitativo**: cero aporte numérico al módulo de armamento.

### ARG-102-003 — Zinapécuaro, Michoacán (🟢 VERDE)

- **Hecho**: **4 cateos** de la FGE de Michoacán con la Sección de Investigación Especializada de la
  Guardia Civil, SSPC, SEDENA y GN. **4 detenidos (uno adolescente)**; **5 armas largas** —4 fusiles
  en un inmueble y 1 en el segundo—; cartuchos y cargadores **sin cantidad**; componentes de chaleco
  táctico; **uniformes con letreros de la CFE**; metanfetamina y mariguana sin peso; teléfonos,
  memorias USB, cámara de acción, báscula y documentación. Grupo señalado: "grupo delictivo X".
- **Fuente con fecha en ruta**: `esferanoticias.mx/2026/08/18/…`. Corroboración: Quadratín Michoacán,
  MiMorelia (`n5590087`), La Voz de Michoacán, Agencia Infomanía, El Clarín — **todas sin fecha**.
- El texto es **reproducción literal de un boletín de la FGE de Michoacán que no se localizó en
  portal propio**: la sustitución por medios **queda escrita, no se hace en silencio**.
- Confianza **★★★☆☆ / Medio**. **Único evento del corte con cifra exacta de armamento.**
- **Deslinde obligatorio**: mismo municipio y mismo grupo que `ARG-101-003` (enfrentamiento de la
  noche del 17-ago). **Ninguna fuente los vincula: no se fusionan.**

### ARG-102-004 — Tijuana, colonia 3 de Octubre, Baja California (🟢 VERDE)

- Detención de **Christian "N"**, señalado como reincidente, con **1 arma corta calibre .380**.
  **Corporación no precisada.** Sin cartuchos ni cargadores publicados.
- **Fuente única** con fecha en ruta: `tijuanaenlinea.com/policiaca/2026/08/18/…`. Sin boletín de
  `fgebc.gob.mx` ni de la SSC municipal. Confianza **★★☆☆☆ / Bajo**.
  `Pendiente de corroboración independiente.`

### ARG-102-005 — Alfajayucan, Hidalgo (🟢 VERDE) — **el peor fechado del corte**

- Cateo de la **FGR** en un predio de la localidad **La Vega** por comercialización ilícita de
  hidrocarburo, tras denuncia del representante legal de Pemex. Apoyo perimetral de SEDENA, GN y
  Policía Estatal. **4,200 litros**, **1 vehículo**, **3 teléfonos**, **41,376 pesos**.
  **Sin detenidos.**
- Fuentes: `milenio.com/policia/…` (nacional), `zocalo.com.mx`, `newshidalgo.com.mx`,
  `ultranoticias.com.mx`. **Ninguna con fecha en URL.** Primaria aparente:
  `fgr.org.mx/es/FGR/Estatal`, **tampoco fechada**.
- **La fecha del 18-ago la afirma el resumidor en dos consultas y ninguna URL la sostiene.**
  `PENDIENTE DE ANCLA FECHADA — NO INTEGRAR A TOTALES HASTA VALIDACIÓN`.
  Confianza **★★☆☆☆ / Bajo**, fijada por el campo peor sostenido, que es la fecha.

---

## Módulo de armamento — trazabilidad de las tres líneas ARM

| ARG-ID | Evento | Cifras integradas | Detenidos | Estatus |
|---|---|---|---|---|
| `ARG-102-ARM-001` | Zinapécuaro, Michoacán (`ARG-102-003`) | **5 armas largas**; cartuchos y cargadores `s/c` | 4 | Integrado. Confianza Medio. `FRONTERA DE VENTANA` |
| `ARG-102-ARM-002` | Tijuana, col. 3 de Octubre (`ARG-102-004`) | **1 arma corta** .380 | 1 | Integrado. Confianza Bajo. `FRONTERA DE VENTANA` |
| `ARG-102-ARM-003` | Los Reyes, Michoacán (`ARG-102-002`) | Ninguna: armas largas y cartuchos **sin cantidad** | 0 | Cualitativo. Confianza Bajo. `FRONTERA DE VENTANA` |

**Total integrado**: 1 arma corta · 5 largas · 0 sin clasificar · cartuchos `s/c` · cargadores `s/c` ·
granadas 0 · AEI 0 · explosivos 0 · **5 detenidos** (*suma propia de ARGOS: 4+1*) · **2 entidades**.

**Poza Rica no aporta detenidos a este módulo**: sus 7 personas vinculadas lo fueron **sin
aseguramiento de armamento**, y la regla exige que las personas contadas aquí lo sean en el mismo
evento de aseguramiento. Se contabilizan en "Detenciones relevantes" del tablero ejecutivo.

---

## Cobertura por región — resultado del barrido

| Región | Entidades | Portales por búsqueda dirigida | Hechos en ventana | Consumo |
|---|---|---|---|---|
| **Noroeste** | 6 de 6 revisadas | 15 | 1 (`ARG-102-004`) | 20/20 |
| **Noreste** | 5 de 5 revisadas | 13 | **0** | 20/20 |
| **Occidente** | 6 de 6 revisadas | 13 | 2 (`ARG-102-002`, `-003`) | 20/20 |
| **Centro** | **6 de 7 revisadas** — **Tlaxcala `NO REVISADA`** | 13 | 1 condicionado (`ARG-102-005`) | 19/20 |
| **Golfo** | 2 de 2 revisadas | 10 | 1 (`ARG-102-001`) | 20/20 |
| **Sureste** | 6 de 6 revisadas | 15 | **0** en ventana; **1 🔴 de la ventana de ARGOS 101** | 20/20 |
| **Total** | **31 de 32** | **79** *(conteo propio de ARGOS)* | **5** | **153** |

*La cifra de 79 cuenta **consultas dirigidas a portal**, no dominios distintos: los portales
federales (`gob.mx/sspc/prensa`, `gob.mx/guardianacional/prensa`, `fgr.org.mx`,
`gabinetedeseguridad.gob.mx`) fueron consultados de forma independiente por varias regiones y se
cuentan una vez por cada consulta. Corregido tras el control `procedencia-cifras`, que detectó que
el total publicado (66) no era la suma de los renglones regionales.*

**Portales que publicaron material dentro de la ventana: 2** — `fgr.org.mx` y
`comunicacion.fiscaliaveracruz.gob.mx`.
**Portales con `SIN ACTUALIZACIÓN CONSTATADA`: 0** — imposible de reclamar bajo bloqueo.
**Entidades `NO REVISADA`: 1 (Tlaxcala)**, por agotamiento del presupuesto de su región. **Se declara
como tal y no se disfraza de "sin actualización".**

**Nota de método sobre el filtro `site:`**: en varias consultas el buscador **ignoró el filtro** y
devolvió medios en lugar del dominio. Eso **no equivale a haber leído el portal**: la casilla
declarable es `CONSULTADO POR BÚSQUEDA DIRIGIDA — SIN RESULTADO INDEXADO`, nunca "portal revisado".

---

## Módulo judicial — las cuatro candidatas y por qué ninguna se integra

| Autoridad | Caso | Término | Pena | Motivo de exclusión |
|---|---|---|---|---|
| FGR | Huamantla, Tlaxcala — Luis "N", portación de arma de fuego | "sentencia condenatoria" | **2 años 6 meses + 84 UMA** | `laprensadetlaxcala.com/2026/08/` fija **año y mes, no día**. Sin URL de FGR. `PENDIENTE DE CONFIRMACIÓN OFICIAL` |
| FGR | Abejones, Oaxaca — DPE/3588/2026 | "sentencia condenatoria" | **NO PUBLICADA** | Falta el **dato mínimo**. Confianza: No confirmado |
| FGR | Culiacán, Sinaloa — DPE/3598/2026 | "sentencia condenatoria" | **NO PUBLICADA** | Falta la pena; hora del 18-ago sin fijar |
| FGE Veracruz | Agregado estatal del 18-ago: **42 resoluciones = 13 condenatorias + 1 fallo + 28 vinculaciones** | Literal | Ninguna por caso | **Agregado sin desglose nominal.** `lapoliticaenrosa.com/2026/08/18/` fija día, no hora |

**Causa común de las tres de la FGR, y merece nombrarse**: `fgr.org.mx` —corregido en esta edición,
porque el registro apuntaba a `gob.mx/fgr`— publica comunicados numerados **sin fecha en la ruta y
sin la pena en el titular**. Es el emisor que más resoluciones aporta al barrido y el que menos
permite integrarlas.


### Sentencias publicadas FUERA de ventana — respaldo del indicador de cobertura

Incorporada tras el control `procedencia-cifras`, que detectó con razón que el cartelón declaraba
**seis fiscalías con sentencia publicada fuera de ventana** sin que cuatro de ellas constaran en
ningún renglón de este registro. **Una cobertura declarada y no documentada no es demostrable.**
Ninguna de estas resoluciones suma a ARGOS 102; se documentan porque sostienen el indicador y porque
circularán a ediciones siguientes.

| Fiscalía | Caso | Pena | Fecha | Ancla |
|---|---|---|---|---|
| **FGE Puebla** | Coronango — Anadalay "N" y Carlos Andrés "N", violación equiparada agravada | **26 a 7 m 15 d** cada uno | Publicación **11-ago** | `intoleranciadiario.com/articles/inseguridad/2026/08/11/` |
| **FGE San Luis Potosí** | Matlapa — Elías "N", lesiones doblemente agravadas, procedimiento abreviado | **2 a 8 m** + sanción económica y reparación | **Ninguna URL fija fecha** | `mhnoticias.mx` (término en *slug*), `codigosanluis.com`, `quadratin` |
| **FGE Querétaro** | Los Arcos — procedimiento abreviado · "El Pancho" y "El Nata", robo de vehículo (**3 a** + 200 días multa) · Antonio "N", abuso de confianza (**4 a**) · Paola Alejandra "N", homicidio culposo (**4 a 11 m**) | Ver columna | **4-ago** y **10-ago** | `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`, **fecha en la ruta**, categoría propia `/sentencias/` |
| **FGE Zacatecas** | Seis personas por secuestro agravado; víctimas de Villa González Ortega; hecho de **ago-2021** | **100 años** sin liberación anticipada, más multa, suspensión de derechos políticos y reparación | **NO FECHABLE** | `fiscaliazacatecas.gob.mx/la-fiscalia-general-obtiene-fallo-condenatorio-…-secuestro-agravado/` — término en el *slug* institucional, **sin fecha en la URL y sin ancla externa** |
| **FGE Michoacán** | Juan "V", narcomenudeo y cohecho (**3 a 2 m**, 15-ago) · Jorge "N", secuestro agravado (**82 años** + 1,049,646 pesos, 12-ago) · Uruapan, Jorge Alberto "N", homicidio calificado y tentativa (**30 a 1 m 25 d**, sin fecha) | Ver columna | 12 y 15-ago; una sin fecha | `redmichoacan.com/2026/08/15/`, `esferanoticias.mx/2026/08/12/`, `poderjudicialmichoacan.gob.mx/…nota.aspx?id=2701` (**clase C, sin fecha**) |
| **Fiscalía Yucatán** | Juicio oral iniciado 19-may (**108 a 4 m**) · tres condenatorias (**~127 años** acumulados) · FGR, cinco personas por narcóticos y cartuchos de uso exclusivo (de **8 a** a **7 a 2 m**) · violación agravada (**260 a 8 m 12 d**, sin fecha) | Ver columna | **3, 4 y 6-ago** | `elpueblo.com/…20260804…`, `elcronistayucatan.mx/2026/08/06/`, `yucatan.quadratin.com.mx` (sin fecha) |

**Deslinde anotado**: el caso de **Zacatecas** localizado en este corte **no es** el señuelo de Luis
Moya y Calera (31-jul y 1-ago), que sigue descartado. Son hechos distintos. El control los confundió
al no constar el primero en este registro — razón de más para que conste.

**Nota sobre Michoacán**: el caso de **Gabriela "N"** (Morelia) **no entra en esta tabla**. Hay fallo
de culpabilidad del 11-ago, pero todas las fuentes coinciden en que *"la pena se definirá en una
audiencia posterior"*: **sin pena impuesta no es una sentencia con dato mínimo**, y el indicador no
lo cuenta.

### El arbitraje "9 vs 6 vs 10" — RESUELTO A FAVOR DE 10

Respaldo citable: `lapoliticaenrosa.com/2026/08/13/…` (fecha en ruta) publica
*"53 resoluciones judiciales … **11 sentencias condenatorias y 42 vinculaciones a proceso**"*.
**11 + 42 = 53, exacto.** La unidad del encabezado es la **resolución judicial**.

Confirmación estructural independiente: el lote del 18-ago repite la misma aritmética aditiva
—**13 + 1 + 28 = 42**—. La FGE Veracruz cuenta **actos procesales, no personas**, de forma
consistente entre lotes. Y el titular del 13-ago dice *"incluida **una** sentencia de 180 años
dictada por la UECS"* — **singular**: Cosamaloapan es **1 resolución con 5 sentenciados**.

Por tanto **11 − 1 = 10**. Por personas serían 6. **"9" no corresponde a ninguna lectura posible**:
es un residuo sin origen que sobrevivió cinco ediciones. **Fe de erratas procedente**
(`ARG-102-FE-007`).

*Cautela declarada*: ambas descomposiciones proceden del resumidor, no de documento leído. Su
respaldo es la **clausura aritmética exacta en dos lotes distintos** más un ancla con fecha en URL.

---

## Recuperaciones de armamento — el boletín federal que ARGOS 101 no extrajo

Ninguna de estas cifras suma a ARGOS 102. Se documentan para que las ediciones a las que
corresponden puedan recuperarlas y para que no reaparezcan como hallazgos nuevos.

| ARG-ID | Entidad · Municipio | Boletín | Desglose | Detenidos | Corresponde a |
|---|---|---|---|---|---|
| `ARG-102-REC-001` | Sinaloa · El Rosario (Agua Verde) | 14-15-16 ago | **303 AEI · 125 kg de explosivo · 175 kg de emulsión explosiva**, desactivados en sitio. SEMAR / BLONAE / 4ª Región Naval | 0 | ARGOS 99/100 |
| `ARG-102-REC-002` | Michoacán · La Piedad | 14-15-16 ago | **4 largas · 1 lanzagranadas acoplado · 12 cargadores · 123 cartuchos · 9 AEI** · 2 cascos · 4 chalecos · 1 vehículo. Ejército | 0 publicados | ARGOS 99/100 · **🔴** |
| `ARG-102-REC-003` | Nayarit · Huajicori, Acaponeta, La Yesca e Ixtlán del Río | 17 ago | **15 AEI · 169 cartuchos · 12 cargadores** · 1 inmueble · 3 vehículos · 1 tractocamión · ~25 kg mariguana · 1 kg cristal · 1 antena inhabilitada. GN + Ejército + Policía Estatal | 3 | ARGOS 101 |
| `ARG-102-REC-004` | Veracruz · Tihuatlán | 17 ago | **2 largas · 1 corta · 95 cartuchos** · **51,910 L de hidrocarburo** · 3 vehículos | 0 publicados | ARGOS 101 |
| `ARG-102-REC-005` | Veracruz · Tuxpan | 17 ago | **3 largas · 1 corta · 5 cargadores · 197 cartuchos** | 2 | ARGOS 101 |
| `ARG-102-REC-006` | Sinaloa · Ahome | 17 ago | **8 cortas · 9 largas · 8 cargadores** · 1 bolsa con dosis · 1 vehículo. FGR + SSPC | 2 | ARGOS 101 |
| `ARG-102-REC-007` | Chihuahua · Satevó | 17 ago | 20 kg de metanfetamina · 1 vehículo. **Sin armamento** | 2 | ARGOS 101 |
| `ARG-102-REC-008` | Veracruz · Cuitláhuac | 14-15-16 ago | **2 armas sin desglose** corto/largo · dosis · 2 vehículos | 3 | ARGOS 99/100 |
| `ARG-102-REC-009` | Tabasco · Cárdenas | 12 ago | **3 armas cortas** · cargadores y cartuchos **sin cantidad** · droga · 1 vehículo · 1 motocicleta | 3 | ARGOS 96/97 |

**⚠️ CONTRADICCIÓN DECLARADA Y NO ARBITRADA — inventario federal del 17-ago.** Dos equipos leyeron
el mismo boletín y devolvieron **dos renglones distintos para Sinaloa**: uno da **Ahome con 8 cortas,
9 largas, 8 cargadores y 2 detenidos** (recogido arriba) y otro da una línea de **1 arma larga,
13 cargadores, 1,389 cartuchos y 27 AEI**. Lo más probable es que el boletín contenga **dos entradas
de Sinaloa**, pero **ninguna edición ha leído el documento íntegro**: **no se suman ni se funden**.
La segunda queda `POSIBLE SEGUNDA ENTRADA — NO INTEGRAR HASTA VALIDACIÓN`. Si se confirma, añade
**27 AEI** al periodo.

**Dos cierres sin cifra**: (1) el **municipio del renglón de las 13,300 cartuchos de Veracruz** se
cierra como `MUNICIPIO NO PUBLICADO POR LA AUTORIDAD` —el boletín dice literalmente "En Veracruz",
sin municipio, a diferencia de los demás renglones—; (2) la **contradicción de Mapimí** queda
declarada: el boletín federal da **65 cargadores** y no cuantifica cartuchos, frente a **87
cargadores y 4,715 cartuchos** de los medios. **Es un solo evento**, de modo que la duplicidad se
resuelve y la discrepancia numérica queda abierta: `CONTRADICHA — reportar ambas, no sumar`.

---

## El acervo de Chiapas — la premisa queda refutada

ARGOS 100 y 101 dejaron abierto el acervo de boletines sin fechar de `fge.chiapas.gob.mx` como
*"armamento de alto poder que puede llevar cortes acumulándose sin contarse"*. **De seis boletines,
tres se fecharon y los tres son de 2025.**

| Boletín | Estado | Fecha real | Ancla |
|---|---|---|---|
| **Frontera Comalapa** — 4 largas (una con lanzagranadas), 2 cortas, 17 cargadores, 1 granada de percusión 40 mm, 2 chalecos, 4 vehículos (3 blindados) | **FECHADO** | **8-9 jun 2025** | `jornada.com.mx/noticia/2025/06/08/` · `latinus.us/mexico/2025/6/8/` · `razon.com.mx/estados/2025/06/09/` · `diariodetabasco.mx/nacion/2025/06/09/` · `infobae.com/mexico/2025/06/09/` |
| **Acapetahua** — 5 cateos; detención del director de Seguridad Pública Municipal | **FECHADO** | **3 feb 2025** | `proceso.com.mx/nacional/estados/2025/2/3/…344844.html` |
| **Mazatán / Metapa** — armas hechizas, 31 cilindros de CO₂, 4 detenidos | **FECHADO (confianza media)** | **23 mar 2025** | `infobae.com/mexico/2025/03/24/` — correspondencia plausible, **no literal** |
| **Cintalapa** | **NO FECHABLE** | — | Ver advertencia abajo |
| **Benemérito de las Américas** | **NO FECHABLE** | — | El desglose localizado (Selvin "N": 1 corta 9 mm, 3 AK-47, 37 cargadores, 1 de disco con 59 cartuchos) **no coincide** con la ficha `ARM-003` de `_pendiente-barrido-ARGOS-88.md` |
| **Tapachula** | **NO FECHABLE** | — | Cero resultados atribuibles |

**El más relevante, Frontera Comalapa, coincide pieza por pieza con la ficha del pendiente** y es de
**junio de 2025**: catorce meses fuera de ventana. Corresponde a una emboscada con granadas de
fragmentación contra la FRIP y la PEP, con 4 abatidos y persecución que cruzó a Guatemala.

> **No es un acervo de omisiones pendientes: es un archivo histórico sin fechar que el buscador
> devuelve mezclado con material actual.** Mismo modo de fallo que el señuelo de Suchiapa
> (abr-2025), y por la misma causa estructural: **URL de GUID sin fecha alguna**.

**⚠️ La ficha de Cintalapa del archivo no es verificable.** Aparecen **tres** aseguramientos
distintos en ese municipio —Félix "N" (1 AK-47, 1 cargador, **22** cartuchos, 1 detenido);
Osiel/Lucas/Analí (2 fusiles, 1 pistola, 27 cargadores, 752 cartuchos, 3 detenidos); Roberto "N" y
Cosman "N" (1 AK-47, 2 cargadores, 60 cartuchos, 2 detenidos)— y **ninguno tiene "1 cargador, 15
cartuchos, 4 detenidos"**. Puede ser una **fusión de dos casos**: la ficha debe reescribirse.
Además, un **cuarto** caso bajo el mismo topónimo —los ranchos El Vergel y El Guamuchil, FGR con
SEDENA y SEMAR— es del **24-dic-2024** (`infobae.com/mexico/2024/12/24/`).

**Advertencia de conteo anotada**: los "37 cargadores de 30 cartuchos cada uno" de Benemérito son
**capacidad declarada, no cartuchos contados**. **Nunca convertir a 1,110 cartuchos.**

---

## Señuelos de fecha — los doce de mayor riesgo

Los nueve equipos documentaron **más de cuarenta**. Los tres primeros son **fabricaciones del
resumidor del buscador**, no errores de fuente.

| # | Señuelo | Fecha o hecho real | Ancla |
|---|---|---|---|
| 1 | **NL · General Escobedo** — hidrocarburo (FGR, DPE/3602/2026), fechado por el resumidor el **18-ago** | **12-ago-2026.** Ninguna URL sostiene el 18 | `latinus.us/mexico/2026/8/12/` |
| 2 | **Tamaulipas** — desglose de 4 largas, 19 cargadores, 306 cartuchos, 15 kg de mariguana y 3 chalecos adjudicado a **Cd. Victoria** | **Fabricación de atribución geográfica**: es de **Matamoros/Güémez**, operativo antihuachicol previo al 11-ago | `laverdad.com.mx/2026/08/` |
| 3 | **Nayarit** — "1 fusil Barrett, 4 largas, 2 AEI, inhibidor de drones, 1 detenido", devuelto **mezclado** con los 15 AEI del 17-ago | **12-ago-2026**, hecho distinto. **Sumarlo habría duplicado el corte** | `ntv.com.mx/2026/08/12/` |
| 4 | **Boletín federal "del lunes 18 de agosto"** — cae en el día exacto de apertura de esta ventana | **2025.** Trampa de aniversario a un año | `gob.mx/sspc/prensa/…-18-de-agosto-de-2025` |
| 5 | **Chiapas · Frontera Comalapa** | **8-9 jun 2025** | Ver sección anterior |
| 6 | **Veracruz** — boletín institucional "**11 sentencias condenatorias** en diversas regiones", la misma cifra del lote buscado | **marzo-2026.** Fuente oficial, término correcto, **lote equivocado** | *Slug* unicode sin fecha; set regional no coincidente |
| 7 | **Veracruz** — "**53 resoluciones judiciales**", la cifra con que ARGOS identifica el lote del 13-ago | **Se repite al menos tres veces en 2026**: 16-mar, 17-jun y 13-ago. **Ni la cifra del lote ni el número de condenatorias son identificador único** | `horacero.mx/2026/03/16/` · `horacero.mx/2026/06/17/` |
| 8 | **Puebla** — familia de boletines de firmeza de la FGE (60, 50, 35 y 23 años), títulos casi intercambiables | GUID sin fecha. **Vivero del error de Coronango**; explica también la incoherencia de un medio con titular de 26 años y *slug* de 23 | `fiscalia.puebla.gob.mx/Home/Comunicado/<GUID>` |
| 9 | **Michoacán · Zinapécuaro** — enfrentamiento con drones, 1 ejecutado, 1 herido, narcobloqueos: **saldo casi idéntico** al buscado para `ARG-101-003` | **julio-2026**, con un tercer precedente en abril. **Tres hechos con la misma firma en el mismo municipio** | `blogdelnarco.org/2026/07/` (`NO OFICIAL`) · `infobae.com/mexico/2026/04/02/` |
| 10 | **GN · Nayarit** — "más de 4,300 cartuchos, 1 arma larga, 43 cargadores", mismo municipio que los 15 AEI | **14-jul-2024.** Trampa de año en boletín oficial sin fecha en ruta | `gob.mx/guardianacional/prensa/…` |
| 11 | **Chiapas · Cintalapa** — cuatro casos distintos bajo el mismo topónimo | El de los ranchos, **24-dic-2024** | `infobae.com/mexico/2024/12/24/` |
| 12 | **Michoacán** — un medio publica **"89 años"** donde otro publica **82** para el mismo caso de Jorge "N" | **12-ago-2026.** El "89" es error de un solo medio; caso **distinto** del de Gabriela "N" | `esferanoticias.mx/2026/08/12/` |

**Señuelos adicionales documentados y no reintroducidos**: Veracruz "51 resoluciones y 12
condenatorias" (mayo-2026), "48 resoluciones" (agosto, día indeterminable), "60, 50 y 45 años"
(lote de 44 del 12-ago); Tabasco Cunduacán **~24-mar-2026** (tercer caso en el mismo municipio) y
"fallos condenatorios en dos procesos" sin fecha; Guerrero Santa Bárbara (4-ago) y ataques con
drones en El Fresno (28-jul); Oaxaca Boletín 1,261 (feb-2025); QRoo Benito Juárez (dic-2020) y Playa
del Carmen (18-mar-2026); Michoacán "5 abatidos" del 31-jul (eran 3) y "337 sentenciados, 4,500
años" (agregado semestral); Guanajuato "36 sentenciadas" (agregado anual) y sentencia de 10 años
(feb-2026); Jalisco Jilotlán (13-ago); Zacatecas Luis Moya y Calera (31-jul y 1-ago); BCS Los Cabos
(1-jun-2026); Sinaloa Mazatlán "19 armas automáticas" (no fijable) y el boletín de `sinaloa.gob.mx`
de dic-2024; BC "más de 8 mil armas" (agregado anual).

---

## Correcciones a ediciones anteriores — las once

| ARG-ID | Edición | Corrección |
|---|---|---|
| `ARG-102-FE-001` | ARGOS 101 | **Omitió la masacre de Tlapa de Comonfort** (🔴, dentro de su ventana). Su "cero eventos rojos" es falso |
| `ARG-102-FE-002` | ARGOS 101 | `ARG-101-008` **absorbió un homicidio en una ficha verde**; el homicidio cae dentro de ventana. Además **sí hubo aseguramiento** (1 arma corta 9 mm, pendiente de fragmento citable) |
| `ARG-102-FE-003` | ARGOS 101 | **El vacío del boletín federal del 17-ago tampoco existía.** Segundo falso vacío consecutivo del mismo emisor. El vacío real es del 18-ago |
| `ARG-102-FE-004` | ARGOS 101 | **Pesquería, NL, no pertenece al boletín del 14-16 ago**: el hecho es del **12-ago**, con cuatro URLs fechadas |
| `ARG-102-FE-005` | ARGOS 98 y 101 | **La Piedad (`ARG-98-002`): resuelta y su origen reatribuido.** El "4 abatidos" no venía de un balance de feb-2026, sino de contar como muerto al **cuarto agresor herido bajo custodia**. Saldo real: 3 muertos + 1 herido bajo custodia + 1 adolescente herido |
| `ARG-102-FE-006` | ARGOS 97 y 98 | **Coronango: el *slug* con que ARGOS 98 la respaldó es de otro caso.** ARGOS 97 tenía la URL correcta y ARGOS 98 la degradó |
| `ARG-102-FE-007` | ARGOS 97 a 101 | **"9 condenatorias de Veracruz" no corresponde a ninguna lectura: son 10** |
| `ARG-102-FE-008` | ARGOS 101 | **`ARG-101-002` Colima reclasifica de 🟡 a 🔴**: restos humanos confirmados en cinco fuentes. **Cambia la valoración de ARGOS 101** |
| `ARG-102-FE-009` | ARGOS 101 | **`ARG-101-005` CDMX: los cartuchos sí tenían cantidad** — 65 cartuchos y 1 cargador |
| `ARG-102-FE-010` | ARGOS 99 y 100 | **El acervo de Chiapas queda refutado en su pieza principal**: Frontera Comalapa es de jun-2025 |
| `ARG-102-FE-011` | ARGOS 100 y 101 | **El motín de Cárdenas, Tabasco (16-ago) no se registró**: quema de dos patrullas, retención de policías e incendio de la delegación municipal. Clasificación que le correspondía: **🔴** |

---

## Directorio de dominios — 16 fijados, corregidos o arbitrados

Recogidos en `docs/dominios-oficiales.md`, creado en esta edición y que cierra un pendiente abierto
desde ARGOS 101. Los de mayor consecuencia:

- **Guardia Nacional, reclasificada de B a C.** Es la **fuente primaria declarada del módulo de
  armamento** y su URL **no lleva fecha en ninguna forma**: ningún boletín suyo es asignable a una
  ventana sin ancla externa. **Es la causa estructural de que la fuente primaria del módulo no rinda
  nunca en el corte del día.**
- **FGR**: el portal operativo es `fgr.org.mx`, no `gob.mx/fgr`.
- **Tamaulipas**: el registro apuntaba al portal genérico del estado; el correcto es `fgjtam.gob.mx`.
  **Causa raíz probable de los ceros de la región.**
- **Nuevo León** (`fiscalianl.gob.mx`): **portal de servicios sin sala de prensa indexable**; la
  fiscalía comunica por Facebook y X. **Su cero crónico no era un vacío del territorio.**
- **Fijados desde cero**: Baja California, Baja California Sur, Coahuila, Hidalgo, Morelos y los
  emisores de Colima (que **no tiene portal web**: publica sentencias en X).
- **Variantes arbitradas**: Chihuahua, CDMX, Nuevo León; Edomex resulta ser **dos sitios vivos con
  funciones distintas**, no dos variantes.
- **Reclasificaciones**: CDMX de C a B (el año va en el folio `CS2026-NNN`); Chihuahua y Puebla de B
  a C; `gabinetedeseguridad.gob.mx` de C a B.
- **Deuda declarada**: Aguascalientes, Nayarit y el portal web de Colima siguen sin dominio; Jalisco
  sigue con dos variantes sin arbitrar.

---

## Nota sobre el registro de agentes — causa raíz identificada

Tres ediciones consecutivas reportaron que `barrido-regional`, `procedencia-cifras` y
`editor-duplicidad` **"no resuelven por nombre"**, y las tres aplicaron el mismo remedio manual:
cargar su archivo de definición como primer paso del encargo.

**La causa quedó identificada en esta edición.** Esas definiciones **llegan al repositorio con el
`git merge --ff-only` que cada edición ejecuta al arrancar** para traer los cambios de la anterior
—es decir, **después** de que la sesión haya tomado su registro de agentes—. Los agentes cuyas
definiciones ya estaban en el árbol al inicio (`osint-fuentes`, `verificador-hechos`,
`analista-patrones`, `busqueda-personas`) **sí resuelven**; los que llegan con el *merge*, no, hasta
que el registro se refresca. En esta sesión el refresco ocurrió a mitad del corte y los tres pasaron
a resolver con normalidad.

**No es un defecto de las definiciones y no se corrige edición por edición**: se corrige integrando
esas definiciones a la rama principal, de modo que estén presentes cuando la sesión arranca. Mientras
no se integren, **el arranque manual sigue siendo el procedimiento correcto** — está probado que no
degrada el resultado.

---

## Categorías sin resultado verificable en la ventana

`SIN RESULTADO INDEXADO EN VENTANA` para: **fosas clandestinas**, **desapariciones** como hecho nuevo
(el caso de Poza Rica es una resolución sobre una desaparición de junio), **laboratorios
clandestinos**, **narcotráfico marítimo**, **redes financieras y operaciones con recursos de
procedencia ilícita**, **extorsión** como hecho nuevo, **narcobloqueos**, **drones armados**,
**artefactos explosivos improvisados** dentro de ventana y **ataques a autoridades** distintos del de
Los Reyes.

Ninguna puede declararse `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`: no se leyó ningún portal por
acceso directo.
