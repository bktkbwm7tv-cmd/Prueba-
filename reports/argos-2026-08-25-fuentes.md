# ARGOS 107 — Registro de fuentes

Corte: 2026-08-25 · Ventana de hechos: **2026-08-24 09:15 CDMX → 2026-08-25 09:26 CDMX** (24 h).
Continuación estricta de ARGOS 106. Respalda `argos-2026-08-25.html` y `argos-2026-08-25-movil.html`.

**Hora de arranque verificada**: `TZ=America/Mexico_City date` → **2026-08-25 09:26 CST (UTC−6)**,
sellada en encabezado, pie y todas las marcas `Consulta:`.

---

## Bloque 0 — verificación de base antes de numerar

Ejecutado conforme a `_arranque-ARGOS-107.md`. **La numeración salió del archivo, no de la rama local.**

| Comprobación | Esperado por el arranque | Encontrado | Estado |
|---|---|---|---|
| `origin/main` | `f368a8d` | `d97eef4` = `f368a8d` + el commit de la propia orden de arranque | ✔ coherente, `main` **por delante**, no por detrás |
| Última edición del archivo | `argos-2026-08-24` (ARGOS 106) | `argos-2026-08-24` | ✔ |
| Archivos en `reports/` | 62 | 63 (los 62 + `_arranque-ARGOS-107.md`) | ✔ |
| Hora real CDMX | — | 2026-08-25 09:26 CST | ✔ |

**La rama local estaba divergida de `main`** (llevaba dos commits de nota de traspaso que `main` no
tenía, y le faltaba el commit del arranque). Se integró con `git merge origin/main` —aditivo,
conserva historial— **antes de leer nada más**. Sin ese paso, la sesión no habría visto el archivo
de arranque y habría numerado a ciegas: es exactamente el fallo que el Bloque 0 existe para impedir.

**Nota de rama**: el arranque proponía `claude/argos-107-hoy`; la sesión tiene asignada
`claude/argos-107-generation-omcfoc` y no debe empujar a otra. Se trabajó en la asignada y se
mergeó a `main` al cierre, que es lo que el arranque pide de fondo.

---

## Limitación permanente — decimoctava edición con el egreso bloqueado

Verificado **en esta sesión**, no heredado: `www.gob.mx`, `gabinetedeseguridad.gob.mx`,
`fgr.org.mx` y `www.jornada.com.mx` devuelven fallo de conexión a través del proxy; `WebFetch`
sobre `www.excelsior.com.mx` devuelve `EGRESS_BLOCKED` explícito. El bloqueo alcanza **tanto a
`*.gob.mx` como a los dominios de medios**.

**Cero portales leídos por acceso directo.** El techo de confianza del producto sigue en **★★★★☆**;
ninguna ficha de esta edición lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin
tramitar y continúa siendo el único cambio que elevaría ese techo. Ampliar el número de equipos no
lo levanta: multiplica peticiones contra la misma puerta cerrada.

---

## Cobertura y rotación — declaradas, no estimadas

### Barrido regional: ejecutado, seis agentes en paralelo

El destinatario autorizó subagentes para los seis barridos. Se lanzaron **los seis en un solo
mensaje**, antes de cualquier otro encargo, con la lista de entidades de cada región y **las 27
entidades que ARGOS 106 dejó `NO REVISADA` al frente de cada una**.

**32 de 32 entidades consultadas.** Queda saldada la deuda de cobertura que ARGOS 106 abrió.

La cobertura es **por entidad, no por portal**: dentro de varias entidades quedaron portales sin
consultar por agotamiento del presupuesto de búsqueda de cada agente. Se declaran `NO REVISADA`,
**nunca** `SIN ACTUALIZACIÓN`.

| Región | Entidades | Presupuesto | Portales que quedaron `NO REVISADA` |
|---|---|---|---|
| Noroeste | 6 de 6 | 19/20 | SSP, policías estatales y mesas de paz de 5 entidades |
| Noreste | 5 de 5 | 20/20 | Mesas de paz de las 5; SSPC, SEDENA, FGR y ANAM regionales |
| Occidente | 6 de 6 | 20/20 | SSP de Guanajuato, Nayarit, Colima y Aguascalientes |
| Centro | 7 de 7 | 20/20 | FGJ CDMX, Fiscalía Morelos, FGE Tlaxcala, SSP Hidalgo, SSPMQ Querétaro, SEDENA/SEMAR/FGR |
| Golfo | 2 de 2 | 23 | SEMAR Zona Naval Golfo, Aduanas/ANAM |
| Sureste | 6 de 6 | 22 | SSP, policías estatales y mesas de paz de las 6 |

**Dominios oficiales no confirmados** (hallazgo reutilizable): fiscalías de **Tlaxcala**, **Nayarit**
y **Guanajuato**. En Colima se corrigió el dominio: el real es `fgecolima.mx`, no
`fiscalia.colima.gob.mx`. En Guanajuato se sustituyó por el agregador
`boletines.guanajuato.gob.mx`, sustitución declarada.

### Rotación de cobertura — **CICLO C aplicado y declarado**

A ARGOS 106 le tocaba el Ciclo C y no lo aplicó, porque no hubo barrido que rotar. **ARGOS 107 lo
aplica**: **Occidente y Sureste encabezaron el triaje judicial**; Noroeste, Noreste, Centro y Golfo
encabezaron con armamento.

**Qué aportó la rotación que el orden anterior no habría aportado:**

1. **Sureste** — al gastar sus primeras búsquedas en fiscalías, **descartó limpiamente siete
   resoluciones** que un triaje apurado habría podido tomar del titular, y detectó que el boletín
   más reciente de la FGEO (2,743, del 24-ago, **dentro de la ventana**) es una **vinculación a
   proceso, no una sentencia**. Es exactamente el falso positivo que la regla de validación jurídica
   existe para impedir, y llegó a estar dentro de la ventana: sin triaje judicial dedicado tenía
   posibilidades reales de colarse.
2. **Occidente** — localizó el **único candidato a sentencia del corte** (Jiquilpan, Michoacán) y,
   con el presupuesto que le sobró por haber entrado primero por lo judicial, **detectó a tiempo su
   defecto de fijación de fecha** antes de integrarlo. Ver el apartado de sentencias: el candidato
   acabó cayendo por una razón todavía mejor.
3. **Corrección de dominios** — el triaje judicial es lo que reveló qué dominios de fiscalía
   responden a `site:` con contenido real y cuáles no. Ese inventario queda para las ediciones
   siguientes y no se habría producido entrando por armamento.

**Balance honesto**: a diferencia de ARGOS 101 (Durango), **el Ciclo C no produjo esta vez una
sentencia integrable**. Su rendimiento fue **defensivo**: evitó dos falsos positivos e inventarió
dominios. Se registra así, sin inflarlo.

### Control de recall — aplicado

`_arranque-ARGOS-107.md` lo hizo obligatorio desde esta edición, por el fallo de ARGOS 105 (32 de 32
declaradas y aun así cuatro hechos rojos perdidos). Cada región contrastó sus entidades «sin
hallazgos» con consulta genérica sin restricción de dominio. **El coordinador ejecutó además un
recall nacional propio** (`ataque armado / violencia México 24 y 25 de agosto de 2026`), y de ahí
salieron **dos de los tres hechos recuperados**: Tecamachalco y el megaoperativo del CJNG. El
control funciona y debe conservarse.

---

## Los tres hechos de la ventana

| ARG-ID | Entidad · municipio | Fecha | Color | Fuente principal |
|---|---|---|---|---|
| `ARG-107-001` | Veracruz · Poza Rica | 24-ago, noche | 🔴 | El Financiero `/2026/08/25/`, La Jornada `/2026/08/25/`, Aristegui `/2508/` |
| `ARG-107-002` | Sinaloa · Mazatlán | 24-ago, 16:45 | 🔴 | Ríodoce `/2026/08/24/`, Noroeste, El Sol de Mazatlán |
| `ARG-107-003` | Coahuila · Candela | 25-ago (no anclada) | 🟡 | El Tiempo Monclova `/noticia/2026/`, Posta México |

### `ARG-107-001` — Poza Rica, ataque a dos reporteros y sustracción de uno

- Nacional: [El Financiero](https://www.elfinanciero.com.mx/estados/2026/08/25/donde-esta-eli-martinez-reportan-como-desaparecido-a-periodista-de-veracruz-tras-ataque-armado/)
- Nacional: [La Jornada](https://www.jornada.com.mx/noticia/2026/08/25/estados/atacan-a-periodistas-en-el-norte-de-veracruz-uno-se-reporta-como-no-localizado)
- Nacional: [Aristegui Noticias](https://aristeguinoticias.com/2508/mexico/reportan-privacion-de-la-libertad-del-periodista-eli-martinez-tras-ataque-a-balazos-en-poza-rica/)
- Nacional: [El Universal](https://www.eluniversal.com.mx/estados/atacan-a-balazos-a-dos-reporteros-de-nota-roja-al-norte-de-veracruz-uno-es-reportado-como-desaparecido/)
- Nacional: [TV Azteca](https://www.tvazteca.com/aztecanoticias/reportan-ataque-dos-periodistas-en-poza-rica-veracruz-uno-permanece-desaparecido/)
- Regional: [Grupo Marmor](https://grupomarmor.com.mx/2026/08/25/reportan-desaparecido-al-periodista-eli-martinez-tras-ataque-armado-en-poza-rica-veracruz/)

**Sin boletín de la FGE de Veracruz ni de la SSP**: `SIN RESULTADO INDEXADO EN VENTANA`. La fuente
institucional se acredita **solo de forma indirecta**, por cita de los medios al despliegue de
búsqueda (GN, SEDENA, SSP y policía municipal). Por eso la confianza es **★★★☆☆** y no ★★★★☆:
conforme a la regla de corroboración asimétrica, **el nivel lo fija el campo peor sostenido**, que
aquí es la ausencia de fuente oficial directa.

**Clasificación 🔴** por el agravante expreso de la metodología: *víctima que sea periodista*.

**Antecedente verificable**: dos comunicadores de la misma fuente policiaca fueron asesinados en
Poza Rica en 2026, en enero y en junio. Se consigna como contexto de patrón; **no se fusiona** con
este hecho ni se afirma autoría común.

### `ARG-107-002` — Mazatlán, ataque en la Central de Autobuses

- Regional: [Ríodoce](https://riodoce.mx/2026/08/24/ataque-armado-en-la-antigua-central-de-mazatlan-deja-un-muerto-y-un-herido/)
- Regional: [Noroeste](https://www.noroeste.com.mx/amp/seguridad/ataque-armado-en-la-central-de-autobuses-de-mazatlan-deja-un-muerto-y-un-herido-AC25145984)
- Regional: [El Sol de Mazatlán](https://oem.com.mx/elsoldemazatlan/policiaca/ataque-a-balazos-deja-un-muerto-y-un-herido-en-la-central-de-autobuses-de-mazatlan-31728712)

Hora publicada: **16:45 h**, dentro de la ventana (abre a las 09:15 del 24-ago). Ríodoce lleva
**fecha en la ruta**. Sin boletín de la SSP de Sinaloa ni de la FGE.

**Deslinde de duplicidad, verificado**: no es `ARG-106-001` (centro de Mazatlán, 23-ago, 2 muertos
y 5 heridos) ni `ARG-106-004` (La Noria-Palo Blanco, aseguramiento). Distinto día, distinta colonia,
distinto saldo. `Palos Prietos` y `Central de Autobuses` **no aparecen en ningún `-fuentes.md`
anterior**.

**Clasificación 🔴** por el agravante de *víctimas múltiples*: tres personas agredidas, una muerta y
una herida de gravedad. La enumeración base de 🔴 pide «homicidios múltiples»; la cláusula de
agravantes dice «víctimas múltiples», que es más amplia y es la que aplica. **Se declara el criterio
para que sea auditable.**

### `ARG-107-003` — Candela, enfrentamiento en el límite con Nuevo León

- Regional: [El Tiempo Monclova](https://eltiempomx.com/noticia/2026/enfrentamiento-en-candela-deja-un-delincuente-abatido-y-un-policia-estatal-herido.html)
- Regional: [Posta México](https://www.posta.com.mx/mexico/policia-estatal-se-enfrenta-a-tiros-en-los-limites-de-coahuila-con-nuevo-leon/vl1607183)

⚠️ **`FECHA DEL HECHO NO ANCLADA EN RUTA`.** La URL de El Tiempo Monclova fija el **año 2026** —lo
que descarta la trampa de aniversario— pero **no el día**. El «25 de agosto de 2026» procede del
**resumidor del buscador**, reiterado en tres consultas distintas, y tres afirmaciones del mismo
resumidor **no son tres fuentes**. Se integra a la edición que lo ve primero, con la marca, y **se
corregirá por fe de erratas** si aparece un ancla que lo sitúe fuera de la ventana. Confianza
**★★☆☆☆**: el campo peor sostenido es la fecha, y la marca se aplica al renglón completo.

**Deslinde de aniversario, verificado**: no es el enfrentamiento de **Hidalgo, Coahuila**, de
**octubre de 2025** —1 delincuente muerto y 2 policías heridos, con muerte posterior de un
elemento—, respaldado por [La Jornada `/2025/10/18/`](https://www.jornada.com.mx/noticia/2025/10/18/estados/enfrentamiento-armado-en-coahuila-deja-un-delincuente-muerto-y-dos-policias-heridos)
e [Infobae `/2025/10/18/`](https://www.infobae.com/mexico/2025/10/18/enfrentamiento-en-coahuila-deja-dos-policias-heridos-y-a-un-presunto-criminal/).
Distinto municipio, distinto saldo, distinto año.

**Clasificación 🟡 con reserva declarada.** La secuencia publicada —la patrulla detecta, los
tripulantes disparan **al ser detectados**— no permite fijar si hubo agresión buscada contra el
personal (🔴, «ataque contra autoridades») o resistencia a una acción del Estado (🟡, «confrontación
derivada de un operativo»). La metodología obliga a **🟡 cuando no se puede determinar quién
inició**. **El abatido no mueve el color**: contar bajas criminales como medida de gravedad
convertiría la eficacia de la respuesta estatal en aumento del riesgo, que es justo lo que la
metodología prohíbe. El policía herido **no falleció**, de modo que no concurre el agravante de
muerte de personal.

---

## Las tres recuperaciones — fuera de todos los totales

### `ARG-107-REC-001` — Culiacán, Lomas de Tamazula · ventana de origen: **ARGOS 106**

- Regional: [Noroeste](https://www.noroeste.com.mx/seguridad/ataque-armado-en-loma-de-tamazula-deja-a-dos-adultos-y-un-menor-heridos-en-culiacan-KE25121795)
- Regional: [Café Negro Portal — el ataque](https://cafenegroportal.com/ataque-armado-en-una-fiesta-en-lomas-de-tamazula-deja-tres-heridos-uno-de-ellos-es-un-menor-de-3-anos/)
- Regional: [Café Negro Portal — el fallecimiento](https://cafenegroportal.com/martin-muere-tras-ser-baleado-durante-fiesta-familiar-en-lomas-de-tamazula-culiacan/)
- Regional: [Quadratín Bajío](https://bajio.quadratin.com.mx/muere-uno-de-los-3-heridos-tras-atentado-en-fiesta-en-culiacan/)
- Regional: [Noticiero Altavoz](https://noticieroaltavoz.com/muere-uno-de-los-heridos-tras-ataque-armado-durante-fiesta-en-lomas-de-tamazula/)
- Regional: [Azteca Sinaloa](https://www.aztecasinaloa.com/policiaca/sujetos-armados-atacan-a-balazos-a-una-fiesta-en-lomas-tamazula-en-culiacan-hay)
- Nacional: [El Universal](https://www.eluniversal.com.mx/estados/atacan-a-balazos-y-hieren-a-una-familia-en-culiacan-un-menor-de-tres-anos-entre-las-victimas/)

Hecho: **domingo 23-ago, ~17:00 h**, calle Río Culiacán entre Sanalona y Tamazula. Heridos: Luis,
Martín (59) y Wilberth, **menor de 3 años**. **Martín falleció ~21:00 h del mismo domingo** en
urgencias del Hospital General de Culiacán.

**Control de calendario aplicado** (regla de ARGOS 103): el 23-ago-2026 **fue domingo** —el 24 fue
lunes, confirmado por la propia cobertura de Mazatlán—, de modo que la atribución «domingo» de las
fuentes **es internamente coherente**. Hecho y desenlace caen **íntegros dentro de la ventana de
ARGOS 106** (23-ago 09:08 → 24-ago 09:15), que no lo publicó.

**Clasificación 🔴** por víctimas múltiples y por un menor de edad entre ellas.

### `ARG-107-REC-002` — Tecamachalco, Puebla · ventana de origen: **ARGOS 106**

- Nacional: [Milenio](https://www.milenio.com/policia/puebla-grupo-armado-irrumpe-casa-mata-hombre-buscaba-refugio)
- Nacional: [Excélsior](https://www.excelsior.com.mx/nacional/grupo-armado-irrumpe-en-una-casa-y-mata-a-un-hombre/1671903)
- Regional: [Periódico Central](https://www.periodicocentral.mx/pagina-negra-s/delincuencia/ejecutan-a-hombre-en-tecamachalco-puebla-motosicarios-lo-persiguieron-hasta-una-casa-inquilino-intento-ayudarlo/508285/)
- Regional: [Diario Cambio](https://www.diariocambio.com.mx/2026/policiaca/hombre-asesinado-persecucion-casa-tecamachalco/)
- Regional: [Ambas Manos](https://www.ambasmanos.mx/nota-roja/ejecutan-a-hombre-que-intento-refugiarse-en-la-casa-de-un-vecino-en-tecamachalco/346010/)
- Regional: [Telediario](https://www.telediario.mx/comunidad/tecamachalco-puebla-matan-a-hombre-que-buscaba-refugio)
- Regional: [Municipios Puebla](https://municipiospuebla.mx/nota/tecamachalco/asesinan-un-hombre-dentro-de-su-vivienda-en-tecamachalco)

Hecho: **cerca de la medianoche del domingo 23-ago**, calles 2 Oriente y 4 Norte, barrio de San
Juan. Víctima de 30-35 años, no identificada públicamente. Agresores: **cinco hombres y una mujer**
en motocicletas, con armas cortas. Derribaron parte de la barda tras negarse el propietario a
entregar al perseguido. FGE de Puebla abrió carpeta.

**Asignación de ventana**: medianoche del 23→24 cae **antes de las 09:15 del 24-ago**, es decir
**dentro de la ventana de ARGOS 106**, que no lo publicó.

**Clasificación 🟡**: homicidio doloso único sin ninguno de los agravantes de la lista roja. Aplica
la regla de cierre del vacío de la escala: es daño consumado, no incremento del riesgo estratégico
nacional.

### `ARG-107-REC-003` — Megaoperativo CJNG · ventana de origen: **21 al 23 de agosto**

- Nacional: [La Jornada](https://www.jornada.com.mx/noticia/2026/08/24/politica/detienen-a-20-presuntos-integrantes-del-cjng-en-operativo-en-hidalgo-jalisco-y-michoacan)
- Nacional: [Proceso](https://www.proceso.com.mx/nacional/2026/8/24/dan-golpe-al-cjng-en-hidalgo-jalisco-y-michoacan-detienen-a-20-personas-378621.html)
- Nacional: [Expansión Política](https://politica.expansion.mx/mexico/2026/08/24/detienen-20-presuntos-integrantes-cjng-tres-estados)
- Nacional: [unoTV](https://www.unotv.com/nacional/detienen-a-20-integrantes-del-cjng-en-hidalgo-jalisco-y-michoacan-aseguran-tigres-panteras-armas-droga-y-113-vehiculos/)
- Nacional: [Milenio](https://www.milenio.com/policia/detienen-integrantes-cjng-hidalgo-jalisco-michoacan)
- Nacional: [Contralínea](https://contralinea.com.mx/interno/semana/operativo-en-hidalgo-jalisco-y-michoacan-deja-20-presuntos-integrantes-del-cjng-detenidos/)

Hecho: **21 al 23 de agosto**, publicado el **24-ago** (cuatro rutas con fecha). 36 inmuebles,
20 detenidos de tercer y cuarto nivel, **7 armas cortas y 3 largas**, cartuchos de diversos
calibres, droga, 113 vehículos, dinero, equipo de comunicación, **1 dron y 1 inhibidor de señal de
dron**, y felinos y aves en condiciones inadecuadas.

`SIN DESGLOSE POR ENTIDAD`: las cifras son agregadas para los tres estados y **no pueden atribuirse
a Jalisco, Michoacán o Hidalgo por separado**. `Evento anterior publicado durante el corte`: **no
entra en los totales de ARGOS 107**.

**Corroboración débil por construcción**: todos los medios reproducen el mismo anuncio del titular
de la SSPC; **varios republicadores de un mismo boletín no son fuentes independientes**. Sin
comunicado propio de SSPC o FGR leído directamente.

**Precedente localizado por `editor-duplicidad`**: el inhibidor de señal de drones **no es el
primero del archivo**. El 12-ago se aseguró otro en **Huajicori, Nayarit** (origen chino, marca
Tatusky Technology), junto con un fusil antiblindaje y 2 AEI. La ficha se corrigió para citarlo:
**dos inhibidores en dos entidades en trece días** es indicio de difusión de la contramedida, no un
hallazgo aislado. *Es lo que el índice de ARG-ID existe para producir.*

---

## Sección 1 — Conteo nacional de armamento

**Cero en las nueve categorías.** `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`, declarado
**después** del barrido de las seis regiones sobre las 32 entidades y el nivel federal.

Ninguno de los tres hechos de la ventana llevó aseguramiento con cifra publicada: en Candela hubo
un civil abatido pero **el armamento no se publicó**; los otros dos son agresiones sin
aseguramiento. Las nueve categorías se muestran **en cero y atenuadas**: la ausencia es dato.

### ⚠️ Corrección de presentación aplicada tras revisión del destinatario

**El bloque de tarjetas mostraba nueve ceros mientras la misma edición tabulaba decenas de armas.**
El cero era metodológicamente correcto —esas armas pertenecen a hechos de ventanas anteriores— pero
**se leía como un error del producto, no como una distinción**, que es un fallo real: un mando no
tiene por qué reconstruir la regla para entender la cifra.

**Corrección**: cada tarjeta lleva ahora **dos cifras con significados distintos y rotulados**.
La **cifra grande** es lo asegurado en hechos de la ventana —lo que alimenta el total nacional del
corte— y la **línea inferior** es lo publicado durante el corte procedente de hechos anteriores.
Encima del bloque va la leyenda que las distingue.

**Las cifras de la línea inferior son cálculo propio de ARGOS**, por suma de lo publicado por cada
autoridad, y se declaran como tal:

| Rubro | Suma | Desglose |
|---|---|---|
| Armas cortas | **25** | Veracruz 3 + Tijuana 15 + CJNG 7 |
| Armas largas | **12** | Veracruz 1 + Tijuana 3 + Los Reyes de Salgado 5 + CJNG 3 |
| Cargadores | **5** | Los Reyes de Salgado 5 |
| Cartuchos | **0** | **Ninguna fuente publicó cifra de munición en ningún evento** |
| Personas detenidas | **326** | CJNG 20 + Veracruz operativo 26 + Veracruz FGE 42 cateos 30 + Tijuana 229 + Romita 8 + Edomex 13 |

**Salvedades que van escritas en el propio cartelón, no solo aquí:**

- **Las 326 personas detenidas no son una cifra homogénea**: **229 corresponden al agregado semanal
  multidelito de Tijuana**, que no puede vincularse 1:1 con armamento y ni siquiera es
  exclusivamente de delitos armados. Sumarlas sin decirlo sería el error que la regla de conteo de
  detenidos prohíbe.
- **Champotón queda fuera de ambas cifras** por la contradicción no resuelta entre versiones.
- **Las réplicas no se cuentan como armas**: 1 en Veracruz y 5 en Tijuana quedan fuera.
- **Cartuchos en cero por partida doble**, y conviene subrayarlo: ni en la ventana ni en lo
  publicado durante el corte hay **una sola cifra de munición**. Es un vacío de publicación
  sostenido, no una casualidad de este corte.

### Eventos anteriores publicados durante el corte — NO INTEGRADOS

Todos con fecha de hecho anterior a la apertura de la ventana. Se documentan porque son lo único
que las corporaciones difundieron durante el corte.

| Entidad · municipio | Ventana del hecho | Cifras | Fuente |
|---|---|---|---|
| Veracruz · Poza Rica, Pueblo Viejo, Martínez de la Torre | 21-23 ago | 26 detenidos (2 por portación), 3 cortas, 1 larga, 1 réplica, ~150 dosis, 22 vehículos | [veracruz.gob.mx `/2026/08/24/`](https://www.veracruz.gob.mx/2026/08/24/26-personas-detenidas-y-cerca-de-150-dosis-de-presunta-droga-decomisadas-saldo-de-operativos-de-fin-de-semana/) |
| Veracruz · 31 municipios (42 cateos) | 17-23 ago | 30 detenidos; armas **sin cifra publicada** | La Política en Rosa `/2026/08/24/` |
| Baja California · Tijuana | 17-23 ago | 229 detenidos (12 por portación), 15 cortas, 3 largas, 5 réplicas | [Tijuana en Línea `/2026/08/24/`](https://www.tijuanaenlinea.com/policiaca/2026/08/24/detienen-a-229-personas-y-decomisan-armas-en-tijuana/) · [Uniradio](https://www.uniradiobaja.com/policiaca/sspcm-decomisa-18-armas-fuego-captura-mas-200-presuntos-delincuentes-n900357) |
| Michoacán · Los Reyes de Salgado | 21-23 ago | 5 largas, 5 cargadores, 2 vehículos | Boletín Gabinete 21-23 ago |
| Guanajuato · Romita | 21-23 ago | 8 detenidos, droga, 24 celulares; **sin cifra de armas** | Boletín Gabinete 21-23 ago |
| Estado de México | 21-23 ago | 13 detenidos, 5 vehículos, 10 celulares, 1 inhibidor; **sin armas** | Boletín Gabinete 21-23 ago |
| Campeche · Champotón | 21-23 ago | **Contradicción, ver abajo** | Reforma · El Universal · California Medios |

**Cifras de los agregados semanales**: los de Tijuana y de la FGE Veracruz son **multidelito** y
no permiten vincular 1:1 detenidos con armas. No se integran ni se convierten.

**Champotón — `POSIBLE DUPLICIDAD, NO INTEGRAR HASTA VALIDACIÓN`.** Dos versiones del mismo
municipio y el mismo tipo de operativo, con **cortas y largas invertidas**:

- Versión A (Reforma, El Universal, Quadratín): 3 cortas · 5 largas · 12 cargadores · ~1,000
  cartuchos · avioneta · 61 vehículos · 5,912 L de hidrocarburo · 3,000 L de turbosina · 6 detenidos.
- Versión B (California Medios, atribuida al Gabinete de Seguridad): 5 cortas · 3 largas ·
  14 cargadores · 7 detenidos.

No puede establecerse si es un mismo hallazgo con error de transcripción o dos cateos distintos.
**Es avance parcial del pendiente `ARG-105-002`** y así se registra.

### ⚠️ Renglón del boletín federal que NO se da por cerrado

`_pendientes.md` arrastra desde ARGOS 104 los renglones de **Romita (Gto.)**, **Tlajomulco (Jal.)**
y **Los Reyes de Salgado (Mich., 5 largas y 5 cargadores)** del boletín federal **del 19-ago**,
`PENDIENTE DE ANCLA FECHADA`. El barrido de Occidente devolvió **Los Reyes de Salgado con cifras
idénticas (5 largas, 5 cargadores) y Romita**, pero atribuidos al boletín **del 21-23 ago**.

**No se cierra el pendiente.** Que las mismas cifras aparezcan atribuidas a dos boletines distintos
puede significar (a) que el renglón es del 21-23 y ARGOS 104 lo fechó mal, (b) que el resumidor
confundió los boletines, o (c) que el boletín agregado repite renglones. **Arbitrar entre las tres
sin lectura directa produciría un dato peor que el pendiente.** Se anota la observación y el
pendiente sigue abierto.

---

## Sección 2 — Sentencias

**Cero sentencias integrables al conteo nacional.** `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`,
declarado tras revisar **32 de 32 fiscalías** y la FGR.

### El candidato que cayó — Jiquilpan, Michoacán

Es el hallazgo del Ciclo C y merece registro completo, porque **cayó por una razón distinta de la
que parecía**.

- Caso: José "N", **11 años 1 mes 10 días**, violación equiparada agravada contra una niña de
  7 años, **procedimiento abreviado**, FGE Michoacán / Fiscalía Regional de Jiquilpan.
- Fuentes: [Informativo La Región](https://laregionenlinea.com.mx/jiquilpan-fge-obtiene-sentencia-condenatoria-de-mas-de-11-anos-de-prision-por-violacion-equiparada-agravada/)
  y [A Tiempo](https://atiempo.mx/justicia/sentencian-a-11-anos-de-prision-a-un-hombre-por-agresion-sexual-contra-una-nina-en-jiquilpan/).

**Motivo inicial de reserva**: ninguna de las dos URL lleva fecha en la ruta; el «24 de agosto de
2026» procedía del resumidor.

**Motivo real y determinante, hallado al verificar**: el respaldo institucional **no sostiene el
caso**. La nota del Poder Judicial de Michoacán con la que se le vinculaba
(`poderjudicialmichoacan.gob.mx/web/noticias/nota.aspx?id=2701`) se titula **«Jueces de Michoacán
dictan sentencia condenatoria y vinculan a proceso en casos de alto impacto en Morelia y
Uruapan»** — **Morelia y Uruapan, no Jiquilpan**.

Es **exactamente el fallo de Coronango** que `CLAUDE.md` documenta: *el término jurídico en la
fuente institucional prueba la clasificación, pero no identifica el caso*. Retirado el respaldo
institucional, quedan **dos medios regionales sin fuente oficial y sin fecha**, es decir confianza
**Bajo**, y la regla asimétrica **no admite Bajo en sentencias**.

`PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL`.

**Indicio adicional, no concluyente**: el portal del Poder Judicial usa **ID correlativo**. En la
misma búsqueda aparecieron `id=2896` y `id=2933`, **232 notas por encima** de la 2701. Si esas dos
son recientes, la 2701 sería **muy anterior** al 24-ago. No se pudo fechar ninguna de las dos, así
que el indicio **se anota y no se usa como prueba**.

### Las otras diez resoluciones descartadas, con su motivo real

| Caso | Motivo |
|---|---|
| Oaxaca, FGEO boletín **2,743** (Salina Cruz, narcomenudeo), **24-ago, dentro de ventana** | **Es vinculación a proceso, no sentencia.** Excluido por la regla de validación jurídica, no por fecha |
| Yucatán, FGE — secuestro agravado, cinco personas, revocación de fallo | `PENDIENTE DE ANCLA FECHADA` |
| Veracruz, FGR — Carlos "N" y Pánfilo "N", 2a 4m 24d, portación | Término expreso, **sin URL fechada** que lo ate a la ventana |
| Oaxaca, FGEO boletín 2,702 — San Pedro Pochutla, robo con violencia, 9 años | Fuera de ventana |
| Oaxaca, FGEO — Juchitán, homicidio calificado, 30 años (18-ago) | Fuera de ventana |
| Guerrero, FGR DPE/3604/2026 — Chilpancingo, >7 años (19-ago) | Fuera de ventana |
| Chiapas, FGR DPE/3413/2026 — Tuxtla, >5 años (6-ago) | Fuera de ventana |
| Quintana Roo — Othón P. Blanco, 20 años | **Fuente no oficial** y anterior |
| Puebla — secuestro agravado, 80 años | Hecho de 2023, publicación 6-ago |
| Veracruz, FGE — serie semanal de 39 y 44 resoluciones | **Sin desglose nominal** y fuera de ventana. La entrega de la semana 19-25 ago no estaba publicada al cierre |

**Indicador de cobertura judicial**: fiscalías revisadas **32 de 32** · FGR **sí** · con sentencia
publicada en ventana **0** · con resolución fuera de ventana **7** · `SIN RESULTADO INDEXADO EN
VENTANA` **25** · páginas leídas por acceso directo **0** · dominios no confirmados **3**.

---

## Verificación negativa — hechos descartados antes de publicar

1. **«Operativo Muralla, 9 detenidos y 9 armas largas en Nuevo León»** — apareció en dos barridos y
   en el recall del coordinador con apariencia de estar en ventana. **Es del 27 de enero de 2026**,
   en **Dr. Coss**, confirmado por [MVS `/2026/1/27/`](https://mvsnoticias.com/nuevo-leon/2026/1/27/operativo-muralla-deja-nueve-detenidos-arsenal-asegurado-en-dr-coss-728757.html).
   **Descartado.** Habría añadido 9 armas largas y 9 detenidos falsos al conteo. Además, sus
   «42 cargadores con 20 cartuchos cada uno» son **capacidad declarada** y **nunca se convierten**
   a 840 cartuchos.
2. **Enfrentamiento de Hidalgo, Coahuila** — trampa de aniversario, es de **octubre de 2025**.
   Descartado y usado como deslinde de `ARG-107-003`.
3. **«Detención el 28 de agosto» en Chihuahua** — **fecha futura**, imposible respecto al día del
   corte. Artefacto del resumidor. Descartado (control de ARGOS 105, sigue rindiendo).
4. **Boletín del Gabinete «del 22, 23 y 24 de agosto de 2025»** — devuelto por la consulta de rango
   con título casi idéntico al que se buscaba. **Es de 2025**, `gabinetedeseguridad.gob.mx/contenido/6376/`.
   Descartado por año.
5. **«Acciones relevantes del 24 de agosto de 2026»** — el resumidor lo afirmó en dos consultas
   distintas, con el mismo desglose que atribuye al boletín 21-23 ago. **Ninguna URL nueva lo
   sostiene**: es el mismo boletín mal etiquetado por el resumidor. No se aceptó.
6. **Ataque armado en el fracc. Petróleos Mexicanos, Mazatlán** («noche del lunes 24-ago») — indicio
   **real pero no fichado**: única fuente sin fecha en la ruta, y los titulares disponibles mezclan
   un saldo de jornada («2 muertos y 6 heridas») con un hecho puntual («balean a dos personas»).
   `NO INTEGRADO — PENDIENTE DE ANCLA FECHADA Y DE SALDO DESLINDADO`.
7. **Chihuahua, carretera a Ojinaga** — «emboscada con fusiles .50 contra policías estatales»:
   fuente regional única, **sin fecha fijable ni corroboración**. No se ficha ni se descarta.
8. **Infobae `/2026/08/24/` «8 muertos y al menos 6 heridos en un día» en Sinaloa** — el agregado
   corresponde a la jornada del **23-ago** (ventana de ARGOS 106), no a la de este corte. No se usa
   como cifra de este corte.

---

## Indicadores oficiales

**SESNSP — sin actualización durante esta ventana**, comprobado en esta sesión. Última publicación
disponible: **11-ago-2026**, datos a julio. 42.5 homicidios dolosos diarios en julio, nivel más bajo
desde 2015; −51% desde septiembre de 2024 (86.9 → 42.5); promedio ene-jul 48.6; 30 de 32 entidades
con reducción; siete entidades concentran el 49%.

- [El Imparcial](https://www.elimparcial.com/mexico/2026/08/11/homicidios-dolosos-bajan-51-durante-gobierno-de-sheinbaum-julio-registra-el-nivel-mas-bajo-desde-2015/)
- [Contralínea](https://contralinea.com.mx/interno/semana/homicidios-dolosos-bajan-51-desde-septiembre-de-2024-sesnsp/)

`HEREDADO — NO REVERIFICADO` en su contenido; **sí reverificada su vigencia**: no hay publicación
posterior.

---

## Los tres seguimientos de mayor rendimiento — resultado

### 1. Morelia (`ARG-106-REC-002`) — **respuesta negativa, pero informativa**

`SIN RESULTADO INDEXADO EN VENTANA`. Cuatro búsquedas dirigidas específicas (traslado, vinculación
a proceso, liberación, arraigo, fuero militar) **no devolvieron nada fechado el 24 ni el 25-ago**.

**El estado más reciente verificable sigue siendo el del 22-ago**: la investigación por homicidio
está en la **Fiscalía General del Estado de Michoacán — fuero común**; la **FGR podría atraerla** si
se confirma la adscripción de los detenidos a la Guardia Nacional, confirmación que **corresponde a
la propia corporación y no se ha producido**. **Ninguna fuente menciona fuero militar** ni
intervención de juez militar.

**Lectura**: no hay liberación temprana ni traslado. El indicador que el arranque señalaba como «el
más informativo del corte» **sigue sin moverse**, y ese estancamiento —siete días sin definición de
fuero en un homicidio con presunta participación de personal federal— **es en sí mismo el dato**.

### 2. Acapulco (`ARG-106-REC-001`) — **el seguimiento estaba mal planteado**

- **Pronunciamiento de la GN sobre el uso de sus insignias**: no localizado. `SIN RESULTADO
  INDEXADO EN VENTANA`, igual que en ARGOS 106. Tampoco hay boletín de la FGE de Guerrero.
- **Rastreo hospitalario del «agresor herido en el tórax»**: ⚠️ **el barrido detectó una probable
  confusión de identidad en el propio pendiente.** El único herido de tórax localizable es
  **Ernesto Manuel (41), dueño de un taller mecánico en El Quemado, Acapulco**, descrito por las
  fuentes como **víctima** de un ataque **distinto** —el del taller—, **no como agresor** de la
  masacre de La Estación. **No se localizó ninguna fuente que documente a un agresor herido en el
  tórax en el hecho de La Estación.**

**Consecuencia**: la línea «rastreo hospitalario del agresor» puede descansar sobre una **conflación
entre dos hechos distintos de Acapulco**. Antes de gastar más presupuesto en ella hay que
**acreditar el origen del dato** en el archivo de ARGOS 106. Se reformula el pendiente en
`_pendientes.md`.

*Un pendiente que dirige búsquedas durante varias ediciones sobre una premisa no acreditada es más
caro que un vacío declarado.*

### 3. Discrepancia 72 / 172 AEI, Sinaloa — **cerrada por retirada**

**No se resolvió.** El barrido de Noroeste intentó `site:gob.mx/sedena` con los términos del hecho
(Concordia, Culiacán, Mazatlán, artefactos explosivos): **el boletín primario no se localizó**.

Se confirmó, eso sí, que **la discrepancia no afecta al evento de El Rosario** (>300 AEI, 18-ago,
SEMAR), que está bien anclado y **no es el que está en disputa**. La disputa es sobre el evento de
**Concordia / Culiacán / Mazatlán** (hechos 18-19 ago), donde El Universal publica **72** citando al
Gabinete de Seguridad y El Heraldo y La Jornada publican **172** citando a la SEDENA, con **el resto
del desglose idéntico** —2,450 L de sustancias, 98 cargadores, 8,095 cartuchos, 1 Barrett .50,
6 armas largas—, lo que sigue apuntando a error de transcripción sobre un mismo boletín.

**Se aplica el umbral de fe de erratas de `CLAUDE.md`**: la cifra llega a su **tercera edición** sin
respaldo citable que la arbitre. **Se retira del acumulado** y el renglón queda como
`CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO` (`ARG-107-FE-001`).

*Señalar un problema sin resolverlo, edición tras edición, no es trazabilidad: es un error conocido
que se sigue publicando.* El resto del desglose de ese evento **no se altera**.

---

## Fe de erratas de esta edición

| ARG-ID | Corrección |
|---|---|
| `ARG-107-FE-001` | **Sinaloa, 72 vs. 172 AEI**: tercera edición sin arbitraje. Se retira del acumulado; renglón a `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO` |
| `ARG-107-FE-002` | **ARGOS 106 pasa de 2 🔴 / 1 🟡 / 5 🟢 a 3 🔴 / 2 🟡 / 5 🟢**, por `ARG-107-REC-001` (Culiacán) y `ARG-107-REC-002` (Tecamachalco), ambos dentro de su ventana y no publicados. El archivo antiguo **no se reescribe** |

---

## Controles editoriales aplicados

| Control | Estado | Resultado |
|---|---|---|
| `barrido-regional` ×6 | **Ejecutado como subagentes**, autorizados por el destinatario, los seis en paralelo antes que ningún otro encargo | **32 de 32 entidades consultadas.** Saldada la deuda de cobertura de ARGOS 106. Ciclo C aplicado y declarado |
| `editor-duplicidad` | **Ejecutado manualmente** (`grep` sobre todos los `-fuentes.md` y sobre `indice-arg-id.md`) | **Ningún hecho de esta edición estaba publicado.** Dos coincidencias léxicas leídas —no dadas por buenas de oído—: «Poza Rica» corresponde a `ARG-102-001` y `ARG-103-ARM-002`, hechos distintos; «inhibidor» corresponde a Huajicori, Nayarit, 12-ago. **Esta segunda mejoró la edición**: la ficha `ARG-107-REC-003` y la conclusión de capacidad técnica se corrigieron para citar el precedente en vez de presentar el hallazgo como inédito |
| `procedencia-cifras` | **Ejecutado manualmente** | Toda cifra del cartelón tiene fragmento que la sostiene. **Cinco declaradas no integrables**: 72/172 AEI (retirada por fe de erratas), Champotón A/B, agregados de Tijuana y de la FGE Veracruz, y la pena de Jiquilpan. **Una conversión rechazada**: los cargadores «de 20 cartuchos cada uno» del Operativo Muralla son capacidad declarada y no se convierten |
| Revisión del destinatario | **Tres correcciones aplicadas tras entrega** | (1) **Duplicación**: el megaoperativo del CJNG aparecía en la tabla de la pág. 2 **y** con ficha completa en la pág. 4. Retirado de la tabla, que ahora lo remite a su ficha. (2) **Resumen ejecutivo retirado**: repetía los tres hechos ya desarrollados en sus fichas, contra la regla de no duplicación; la pág. 2 pasa a titularse por lo que realmente contiene. (3) **Las nueve tarjetas en cero** se leían como un error junto a tablas llenas de armas: ahora llevan **doble cifra rotulada**. Ver el apartado de la Sección 1 |

Los dos controles manuales se ejecutaron con el mismo criterio que sus agentes, como en ARGOS 106,
y **ambos produjeron hallazgos reales** —el precedente del inhibidor y el defecto de identidad de
Jiquilpan—. La ausencia de invocación como subagentes se declara aquí, no se disimula.

---

## Nota de método para la edición siguiente

**Lo que funcionó y conviene repetir:**

1. **Lanzar los seis barridos antes que nada.** Resultado: 32 de 32 frente a las 5 de 32 de ARGOS
   106. Es la diferencia entre un producto con cobertura y uno sin ella.
2. **El recall nacional del coordinador**, además del de cada región. Produjo **dos de los tres
   hechos recuperados**. Las regiones agotan presupuesto; el coordinador no.
3. **Leer lo que el `grep` devuelve.** Las dos coincidencias de `editor-duplicidad` parecían ruido
   y una de ellas mejoró una conclusión del cartelón.
4. **Verificar el título de la URL institucional, no solo su existencia.** Jiquilpan tenía respaldo
   institucional aparente hasta que se leyó el título de la nota: hablaba de otros dos municipios.
5. **Perseguir la fecha en la ruta hasta el final.** Tres hechos candidatos cayeron o quedaron
   marcados por esa sola comprobación, y uno —Operativo Muralla— habría metido nueve armas largas
   falsas en el conteo.
