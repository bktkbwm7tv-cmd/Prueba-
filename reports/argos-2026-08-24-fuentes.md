# ARGOS 106 — Registro de fuentes

Corte: 2026-08-24 · Ventana de hechos: **2026-08-23 09:08 CDMX → 2026-08-24 09:15 CDMX** (24 h).
Continuación estricta de ARGOS 105. Respalda `argos-2026-08-24.html` y `argos-2026-08-24-movil.html`.

**Hora de arranque verificada**: `TZ=America/Mexico_City date` → **2026-08-24 09:15 CST (UTC−6)**,
sellada en encabezado, pie y todas las marcas `Consulta:`.

---

## ⚠ FALLO DE CONTINUIDAD DE LA SERIE — CAUSA RAÍZ DE ESTA EDICIÓN

Esta edición estuvo a punto de publicarse como **«ARGOS 89»**. La causa merece registro porque no es
un error de criterio sino de **infraestructura del repositorio**, y va a repetirse en cada sesión
nueva mientras no se corrija.

**El HEAD por defecto del repositorio es `claude/argos-criminal-intelligence-otiawj`**, que solo
contiene hasta **ARGOS 88** (8 archivos en `reports/`). La serie real vive en ramas sueltas por
edición —`claude/argos-90-hoy-*` … `claude/argos-105-us24r6` (59 archivos)— y **ninguna está
mergeada a `main`**, que a su vez conserva solo 2 archivos.

| Referencia | Archivos en `reports/` | Última edición |
|---|---|---|
| `main` | 2 | anterior a ARGOS 87 |
| `claude/argos-criminal-intelligence-otiawj` (**HEAD por defecto**) | 8 | ARGOS 88 |
| `claude/argos-105-us24r6` | 59 | ARGOS 105 |

Consecuencias que se materializaron en esta sesión, todas corregidas antes de publicar:

1. **Numeración**: se numeró 89 partiendo de 88. **ARGOS 89 no existe ni debe existir** — la serie
   salta de 88 a 90, y ese hueco es un fallo de continuidad ya documentado por ARGOS 105.
2. **Ventana**: se declaró 22→24 ago, solapándose con la ventana de ARGOS 105 (21-ago 07:55 →
   23-ago 09:08), que la sesión no podía ver.
3. **Sin versión móvil**: `tools/gen-movil.py` se creó en una edición posterior a la 88 y no existía
   en la rama de arranque.
4. **Método desactualizado**: la edición se construyó sobre el `CLAUDE.md` de ARGOS 88, sin la
   iconografía de taxonomía, la regla de rotación de ciclos ni la instrucción editorial de ARGOS 105.

**Corrección aplicada**: se integró `origin/claude/argos-105-us24r6` en la rama de trabajo mediante
`git merge` (aditivo, conserva historial), se retiraron los dos archivos del falso ARGOS 89 y se
rehízo la edición como **ARGOS 106** sobre la estructura vigente.

**Acción de fondo, autorizada por el destinatario en esta sesión**: mergear las ramas de edición a
`main`, para que la rama por defecto deje de estar atrasada. Es la deuda que `_pendientes.md` lleva
abierta desde ARGOS 102.

---

## ⚠ FE DE ERRATAS SOBRE ARGOS 105 — CUATRO HECHOS NO PUBLICADOS

Al cruzar la investigación de esta sesión contra el archivo con `grep` sobre todos los
`-fuentes.md`, **cuatro hechos que caen dentro de la ventana declarada de ARGOS 105 no figuran en
ninguna edición de la serie**. Los términos verificados —`Bayados`, `Willy`, `Lagunilla`,
`Quelite`, `Palo Blanco`, `Alerta Amber`, `Cerdos`, `velorio`, `Acapulco`, `Morelia`— no devuelven
estos hechos en ningún archivo previo.

| ARG-ID | Hecho | Fecha | Color |
|---|---|---|---|
| `ARG-106-REC-001` | Acapulco, Guerrero — masacre de 4 integrantes de una familia por comando con chalecos "Guardia Nacional" | 22-ago (o 21, contradicha) | 🔴 |
| `ARG-106-REC-002` | Morelia, Michoacán — balacera con elementos de la GN de civil; 2 muertos | 22-ago | 🔴 |
| `ARG-106-REC-003` | Los Bayados, Ajuchitlán, Guerrero — ataque de ~8 h contra la comunidad | 21-ago | 🔴 |
| `ARG-106-REC-004` | "El Willy", Casas Grandes, Chihuahua — nuevos restos óseos | 20-ago (difusión 21-22) | 🔴 |

**ARGOS 105 publicó «cero eventos rojos» en esa ventana. Con estos cuatro hechos esa afirmación no
se sostiene**: su semáforo queda corregido por esta fe de erratas a **4 🔴 y 1 🟡** (el amarillo es
`ARG-105-001`, Zapopan). El archivo antiguo **no se reescribe**; la corrección vive aquí y en
`_pendientes.md`.

Los cuatro se publican como **fichas completas de cuatro apartados en la pág. 5 del cartelón**, con
ARG-ID `-REC-`, ventana de origen declarada y **excluidos de todos los totales de ARGOS 106**:
semáforo, radar, mapa y conteo de armamento. Decisión editorial expresa del destinatario en esta
sesión, que prevalece sobre la regla de «solo el día» de ARGOS 105 y es compatible con el mecanismo
`-REC-` de `CLAUDE.md`.

**Lo mismo aplica a dos sentencias**: `ARG-106-SEN-REC-001` (Sonora) y `-002` (Guanajuato), ambas
difundidas el 22-ago, dentro de la ventana de ARGOS 105 y no publicadas por esa edición. No se
integran al conteo nacional de este corte.

---

## Limitación permanente — decimoséptima edición con el egreso bloqueado

Verificado dominio por dominio con `curl` en esta sesión: `CONNECT tunnel failed, response 403`
para `www.gob.mx`, `gabinetedeseguridad.gob.mx` y `fgr.org.mx`, y también para los dominios de
medios (`jornada.com.mx`, `eluniversal.com.mx`, `infobae.com`, `latinus.us`, `excelsior.com.mx`,
`proceso.com.mx`, `milenio.com`, `elfinanciero.com.mx`, `lopezdoriga.com`, `tvazteca.com`,
`debate.com.mx`, entre otros). Se comprobó contra `$HTTPS_PROXY/__agentproxy/status`, que reporta
el proxy activo y sin fallos de relay.

**Cero portales leídos por acceso directo.** El techo de confianza del producto sigue en **★★★★☆**;
ninguna ficha de esta edición lleva ★★★★★. `docs/solicitud-lista-blanca-egreso.md` sigue sin
tramitar y continúa siendo el único cambio que elevaría ese techo.

## Cobertura — declarada, no estimada

**5 de 32 entidades efectivamente revisadas.** No se ejecutó el barrido regional por entidad que
exige `CLAUDE.md`: la búsqueda de esta edición fue **dirigida por categoría**, no portal por portal.
Las 27 restantes se declaran `NO REVISADA`, **nunca** `SIN ACTUALIZACIÓN`: son casillas distintas y
confundirlas equivale a declarar cobertura inexistente.

**Rotación de cobertura**: a ARGOS 106 le correspondía el **Ciclo C (Occidente + Sureste)**
encabezando el triaje judicial. **No se aplicó**, porque no hubo barrido regional que rotar. Queda
pendiente para ARGOS 107, que debe declararlo expresamente.

---

## Los ocho hechos de la ventana

| ARG-ID | Entidad · municipio | Fecha | Color | Fuente principal |
|---|---|---|---|---|
| `ARG-106-001` | Sinaloa · Mazatlán | 23-ago | 🔴 | La Jornada `/2026/08/23/`, TV Azteca, Zócalo, Noroeste, N+ |
| `ARG-106-002` | Colima · Colima | 23-ago | 🔴 | El Heraldo de México `/2026/8/23/`, Excélsior, TV Azteca, AFmedios |
| `ARG-106-003` | Sinaloa · El Quelite / Concordia | 23-ago | 🟢 | SEMAR — Cuarta Región Naval, citada por El Universal, López-Dóriga, AFmedios |
| `ARG-106-004` | Sinaloa · Mazatlán (La Noria) | 23-ago | 🟢 | SSP Sinaloa, citada por Latinus `/2026/8/23/`, Noroeste, Ríodoce |
| `ARG-106-005` | Sonora · Hermosillo | 23-ago | 🟢 | FGJE Sonora / AMIC, citada por Latinus, Infobae, Expreso, Radar Sonora |
| `ARG-106-006` | Ciudad de México · Cuauhtémoc | 23-ago | 🟡 | SSC CDMX (comunicado reproducido por NotiMx), El Heraldo de México |
| `ARG-106-007` | México · Nopaltepec | 24-ago | 🟢 | FGJEM, citada por Infobae `/2026/08/24/` |
| `ARG-106-008` | Ciudad de México · Tláhuac | 23-ago | 🟢 | SSC CDMX, citada por Infobae `/2026/08/23/` |

### `ARG-106-001` — Mazatlán, doble ataque armado

- Nacional: [La Jornada](https://www.jornada.com.mx/noticia/2026/08/23/estados/ataques-armados-en-mazatlan-sinaloa-dejan-dos-personas-muertas)
- Nacional: [TV Azteca](https://www.tvazteca.com/aztecanoticias/mazatlan-ataque-armado-deja-cinco-heridos-en-sinaloa/)
- Nacional: [Zócalo](https://www.zocalo.com.mx/ataques-armados-en-mazatlan-sinaloa-dejan-dos-personas-muertas)
- Regional: [N+](https://www.nmas.com.mx/seguridad/balaceras/enfrentamientos-armados-sinaloa-dejan-muertos-heridos/)
- Regional: [Viva la Noticia](https://vivalanoticia.mx/8-heridos-de-bala-y-un-muerto-en-dos-atentados-en-mazatlan/)
- Contexto: [Infobae — enfrentamientos en La Cofradía](https://www.infobae.com/mexico/2026/08/23/enfrentamientos-con-explosivos-y-armas-mantienen-en-alerta-a-habitantes-de-la-cofradia-mazatlan/)

`CONTRADICHA — no fundida`: Viva la Noticia titula **«8 heridos y un muerto»**; La Jornada y Zócalo
coinciden en **2 muertos y 5 heridos** en el primer ataque más 3 personas atacadas en el segundo. Se
publica la versión coincidente entre dos fuentes nacionales; la variante se documenta y no se
integra. **Sin boletín propio de la SSP de Sinaloa ni de la FGE**: `SIN RESULTADO INDEXADO EN VENTANA`.

### `ARG-106-002` — Colima, ataque durante velorio

- Nacional: [El Heraldo de México](https://heraldodemexico.com.mx/nacional/2026/8/23/matan-dos-hombres-afuera-de-un-velorio-en-colima-agresores-escapan-875066.html)
- Nacional: [Excélsior](https://www.excelsior.com.mx/nacional/balacera-velorio-deja-dos-muertos-era-hermano-difunta)
- Nacional: [TV Azteca](https://www.tvazteca.com/aztecanoticias/en-colima-ataque-en-velorio-mujer-en-la-francisco-i-madero-deja-dos-muertos/)
- Regional (primer ataque, 21-ago): [AFmedios](https://www.afmedios.com/ataque-armado-deja-una-mujer-sin-vida-y-otra-lesionada-en-la-colonia-francisco-i-madero-de-colima/)

Secuencia documentada: **21-ago**, ataque en la col. Francisco I. Madero deja muerta a Alondra "R"
(32) y una mujer herida. **23-ago**, durante su velorio, hombres armados matan a su hermano y a otro
varón. Los antecedentes penales atribuidos a los hermanos proceden de reportes periodísticos, **no
de ficha oficial**: se consignan sin validar. Sin boletín de la FGE de Colima.

### `ARG-106-003` — SEMAR, tres AEI y vehículo blindado

- Institucional / Nacional: [El Universal](https://www.eluniversal.com.mx/nacion/marina-localiza-un-vehiculo-y-explosivos-improvisados-en-sinaloa-artefactos-fueron-destruidos/)
- Nacional: [López-Dóriga](https://lopezdoriga.com/nacional/marina-asegura-vehiculo-blindado-y-explosivos-improvisados-sinaloa/)
- Nacional: [unomásuno](https://unomasuno.com.mx/nacional/marina-destruye-explosivos-y-neutraliza-vehiculo-blindado-en-sinaloa/)
- Regional: [AFmedios](https://www.afmedios.com/marina-localiza-vehiculo-con-blindaje-artesanal-y-explosivos-improvisados-en-sinaloa/)
- Regional: [California Medios](https://californiamedios.com/marina-destruye-explosivos-y-neutraliza-vehiculo-blindado-en-dos-operativos-distintos-en-sinaloa/)
- Regional: [Ruta 135](https://ruta135.com/c-5/marina-localiza-vehiculo-blindado-y-explosivos-en-sinaloa/)
- Regional: [El Diario de Chihuahua](https://eldiariodechihuahua.mx/nacional/2026/aug/23/destruye-marina-artefactos-explosivos-en-sinaloa-830329.html)

Fuente primaria: comunicado de la **Cuarta Región Naval del 23-ago**, citado por todos los medios.
Operativo 1 — La Mora Escarbada (sindicatura de El Quelite): 1 vehículo sin placas con blindaje
artesanal y 2 AEI. Operativo 2 — patrullaje entre Mazatlán y Concordia: 1 AEI. Destruidos en el
sitio. Sin detenidos. **Peso y tipo de carga no publicados** — por eso el rubro «explosivos» del
conteo queda en 0 pese a existir los artefactos.

### `ARG-106-004` — Mazatlán, La Noria-Palo Blanco

- Nacional: [Latinus](https://latinus.us/mexico/2026/8/23/detienen-dos-hombres-en-sinaloa-les-incautan-armas-200-dosis-de-drogas-combustible-182359.html)
- Regional: [Noroeste](https://www.noroeste.com.mx/seguridad/detienen-en-mazatlan-a-dos-hombres-armados-y-decomisan-drogas-y-gasolina-BE25122366)
- Regional: [Ríodoce](https://riodoce.mx/2026/08/23/en-la-zona-rural-de-mazatlan-detienen-a-dos-hombres-les-aseguran-armas-droga-y-gasolina/)
- Regional: [Marcrix](https://www.marcrixnoticias.com.mx/detienen-a-dos-hombres-con-armas-droga-y-200-litros-de-gasolina-en-mazatlan/)
- Regional: [Viva la Noticia](https://vivalanoticia.mx/en-mazatlan-grupo-interinstitucional-detiene-a-dos-civiles-asegura-armas-droga-municiones-y-200-litros-de-gasolina/)
- Regional: [Puntualizando](https://www.puntualizando.com/en-mazatlan-autoridades-detienen-a-dos-civiles-aseguran-armas-droga-municiones-y-combustible/)

Desglose publicado por la SSP de Sinaloa, **base del conteo de armamento del corte**: 1 fusil AK-47
7.62×39 · 1 pistola 9 mm · 6 cargadores de arma larga · 1 de arma corta · 180 cartuchos 7.62×39 ·
10 cartuchos 9 mm · 200 dosis de presunto cristal (~50 g) · 200 L de gasolina en 4 bidones ·
1 Ford Ranger 1999 sin reporte de robo · 2 detenidos, a disposición de la FGR en Mazatlán.

**Criterio aplicado**: los 200 L de gasolina **no** se clasifican como huachicol — la autoridad no lo
hizo. Droga y combustible no son línea de armamento y no entran al conteo de la Sección 1.

### `ARG-106-005` — Hermosillo, Alerta Amber

- Nacional: [Latinus](https://latinus.us/mexico/2026/8/23/rescatan-dos-menores-con-alerta-amber-en-sonora-aseguran-droga-detienen-dos-sujetos-182372.html)
- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/23/encuentran-a-dos-menores-con-alerta-amber-durante-un-cateo-en-hermosillo-hay-dos-detenidos-incluido-el-padre/)
- Regional: [Expreso](https://www.expreso.com.mx/noticias/seguridad/cateo-en-hermosillo-logra-rescate-de-hermanos-sustraidos/263001)
- Regional: [Radar Sonora](https://www.radarsonora.com/cateo-permite-detener-a-dos-personas-y-localizar-a-dos-menores-con-alerta-amber/)
- Regional: [Nuestras Noticias Sonora](https://nuestrasnoticiassonora.com/relevante/cateo-en-hermosillo-permite-rescatar-a-dos-dos-menores-que-tenian-alerta-amber-desde-febrero/)
- Antecedente (abr-2026): [El Imparcial](https://www.elimparcial.com/son/sonora/2026/04/26/se-activa-alerta-amber-en-sonora-por-la-sustraccion-de-dos-menores-en-agua-prieta/)

Sin aseguramiento de armamento: **no entra** al conteo de detenidos de la Sección 1; se consigna en
«Detenciones relevantes».

### `ARG-106-006` — CDMX, tianguis de La Lagunilla

- Institucional (reproducido íntegro): [NotiMx — comunicado de la SSC CDMX](https://www.notimx.mx/2026/08/en-la-alcaldia-cuauhtemoc-efectivos-de-la-ssc-detuvieron-a-seis-jovenes-en-posesion-de-aparente-droga-posiblemente-relacionados-en-una-agresion-con-disparos-de-arma-de-fuego.html)
- Nacional: [El Heraldo de México](https://heraldodemexico.com.mx/nacional/2026/8/23/captan-balacera-en-pleno-tianguis-de-la-lagunilla-hay-un-herido-detenidos-video-874705.html)

1 herido · 6 detenidos (2 menores) · 1 arma corta · 50 bolsitas de aparente marihuana.
**Cartuchos y cargadores no publicados**: se consignan `n/p` en la tabla, que **no es cero**.

### `ARG-106-007` — Nopaltepec, "Los Cerdos"

- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/24/capturan-a-seis-de-los-cerdos-en-edomex-hay-un-expolicia-entre-los-detenidos/)

**Fuente única nacional**, sin corroboración independiente en ventana:
`PENDIENTE DE CORROBORACIÓN INDEPENDIENTE`. Confianza ★★★☆☆.

### `ARG-106-008` — Tláhuac, robo a casa habitación

- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/23/en-vivo-seguridad-crimen-y-narcotrafico-en-mexico-hoy-23-de-agosto-rocha-moya-vuelve-a-pedir-licencia-a-la-gubernatura-de-sinaloa/)

⚠️ **La fuente es un *liveblog***. Conforme a la regla de ARGOS 103, **un *liveblog* nunca fecha un
hecho y no basta como fuente única**. Aquí acredita la actuación de la SSC, no la fecha; el hecho se
integra por corresponder al día de publicación y por ser de bajo impacto, pero se marca
`PENDIENTE DE CORROBORACIÓN INDEPENDIENTE`. **Colonia no publicada**: el hecho no puede cruzarse con
el mapa de incidencia — misma limitación que dejó abierta `ARG-105-005`.

---

## Las cuatro recuperaciones de la ventana de ARGOS 105

### `ARG-106-REC-001` — Acapulco, masacre familiar con insignias de la GN

- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/22/comando-asesina-a-cuatro-integrantes-de-una-familia-en-acapulco-jornada-deja-mas-victimas/)
- Nacional: [unomásuno](https://unomasuno.com.mx/nacional/sujetos-con-insignias-gn-asesinaron-a-cuatro-integrantes-de-una-familia-en-acapulco/)
- Regional: [Quadratín Guerrero](https://guerrero.quadratin.com.mx/masacre-en-la-zona-rural-de-acapulco-matan-a-4-de-una-familia/)
- Regional: [Quadratín México](https://mexico.quadratin.com.mx/masacran-a-familia-en-zona-rural-de-acapulco/)
- Regional: [El Sur de Acapulco](https://suracapulco.mx/cinco-hombres-muertos-y-tres-heridos-dejan-distintos-hechos-de-violencia-en-el-municipio/)
- Regional: [Agencia IRZA](https://agenciairza.com/armados-y-con-chalecos-de-la-gn-se-meten-a-una-casa-y-ejecutan-a-4-familiares-en-acapulco/)

Víctimas: Esteban García Contreras (65), Gustavo García Lorenzo (35), Gonzalo García Lorenzo (35),
David de los Santos García (16).

`CONTRADICHA — fecha`: Infobae publica el 22-ago; Quadratín Guerrero sitúa el hecho «el viernes»,
que corresponde al 21-ago (el 22 fue sábado — verificado contra calendario). **Ambas fechas caen
dentro de la ventana de ARGOS 105**, así que la contradicción no afecta la asignación.

**Sin comunicado de la FGE de Guerrero ni pronunciamiento de la Guardia Nacional** sobre el uso de
sus insignias: `SIN RESULTADO INDEXADO EN VENTANA`.

### `ARG-106-REC-002` — Morelia, balacera con elementos de la GN

- Regional: [Grupo Marmor](https://grupomarmor.com.mx/2026/08/22/homicidio-en-la-colonia-periodistas-termino-con-dos-detenidos-presuntos-elementos-de-la-gn-seguridad-municipal/)
- Regional: [A Tiempo](https://atiempo.mx/destacadas/identifican-guardia-nacional-balacera-colonia-periodista-morelia/)
- Regional: [RED Michoacán](https://www.redmichoacan.com/2026/08/22/identifican-a-los-dos-hombres-asesinados-durante-balacera-en-morelia-uno-era-agente-de-la-gn/)
- Regional: [Media News — dos muertos y dos asegurados](https://medianews.mx/index.php/2026/08/22/dos-muertos-y-dos-sujetos-asegurados-tras-balacera-en-la-colonia-del-periodista-en-morelia/)
- Regional: [Media News — el seguimiento previo](https://medianews.mx/index.php/2026/08/22/jose-luis-y-un-amigo-eran-seguidos-por-agentes-de-la-gn-antes-de-la-balacera-en-la-colonia-del-periodista/)
- Regional: [RED113](http://www.red113mx.com/2026/08/identifican-los-dos-hombres-asesinados.html)
- Regional: [Exeni](https://exeni.com.mx/identifican-a-los-dos-hombres-asesinados-durante-balacera-en-morelia-uno-era-agente-de-la-gn/)
- Regional: [Changoonga](https://changoonga.com/2026/08/23/morelia-elementos-de-gn-arman-balacera-matan-a-chavito-y-a-su-propio-companero/)

Fallecidos: Juan Omar Mireles Tovar (elemento de la GN, de civil) y José Luis (20, civil).
Asegurados por la Policía Municipal: Juan Carlos Dorantes Rebolledo (40) y Rubén Isaí Landeros
García (22). En la cajuela del Nissan Versa verde con placas de la CDMX: armas de fuego y chalecos
tácticos con insignias de la GN, **sin cifra publicada**.

**NO INTEGRADO como hecho**: la versión sobre presunto estado de ebriedad se atribuye a «fuentes
cercanas al caso» y **no está confirmada por autoridad alguna**.

**Clasificación 🔴 por homicidio múltiple**, no por «ataque a autoridades»: los elementos federales
son presuntos responsables, no agredidos.

### `ARG-106-REC-003` — Los Bayados, Ajuchitlán del Progreso

- Nacional: [El Financiero](https://www.elfinanciero.com.mx/estados/2026/08/23/ataque-armado-en-los-bayados-guerrero-revive-temores-de-desplazamiento-forzado-exigen-base-de-la-sedena/)
- Regional: [Quadratín Guerrero — despliegue](https://guerrero.quadratin.com.mx/despliegan-a-fuerzas-de-seguridad-tras-reporte-de-ataques-en-ajuchitlan/)
- Regional: [Quadratín Guerrero — vigilancia](https://guerrero.quadratin.com.mx/vigila-el-ejercito-comunidades-de-ajuchitlan/)
- Regional: [La Plaza Diario de Acapulco — denuncia de drones](https://www.laplazadiario.com.mx/denuncian-ataques-armados-y-con-drones-contra-los-bayados-en-ajuchitlan/)
- Regional: [La Plaza Diario de Acapulco — refuerzo](https://www.laplazadiario.com.mx/se-suma-mas-personal-del-ejercito-al-operativo-en-los-bayados-tras-reporte-de-ataques/)
- Regional: [Trazos Noticias](https://www.trazosnoticias.com.mx/municipios/refuerzan-acciones-interinstitucionales-de-seguridad-en-los-bayados-ajuchitlan-del-progreso/)
- Regional: [MegaVisión](https://megavision.tv/defensa-y-guardia-nacional-refuerzan-seguridad-en-los-bayados-tras-reportes-de-ataques-armados/)

**NO INTEGRADO a ningún conteo**: la denuncia de ataques con drones proviene de habitantes, sin
confirmación institucional ni aseguramiento de aeronave. `NO OFICIAL — PENDIENTE DE CONFIRMACIÓN
INSTITUCIONAL`. El rubro «drones armados» del conteo permanece en **0**.

Antecedente verificable: ~50 familias abandonaron la comunidad por violencia en febrero de 2023.

### `ARG-106-REC-004` — "El Willy", Casas Grandes

- Nacional: [La Jornada — nueve segmentos óseos](https://www.jornada.com.mx/2026/08/22/estados/022n4est)
- Nacional: [El Universal — osamentas trasladadas al SEMEFO](https://www.eluniversal.com.mx/estados/hallan-osamentas-y-restos-oseos-en-la-localidad-de-el-willy-en-casas-grandes-chihuahua-son-trasladados-al-semefo-para-practicas-periciales/)
- Nacional: [Infobae — «cerca de 100»](https://www.infobae.com/mexico/2026/08/22/hallan-mas-restos-oseos-en-el-campo-de-exterminio-el-willy-en-chihuahua-donde-opera-la-linea-ya-serian-cerca-de-100-cadaveres/)
- Nacional: [El Universal — 56 cadáveres, rastreo concluido](https://www.eluniversal.com.mx/estados/exhuman-un-total-de-56-cadaveres-en-predio-el-willy-en-chihuahua-concluyen-trabajos-de-rastreo/)
- Nacional: [Univisión — 76 cuerpos](https://www.univision.com/noticias/narcotrafico/campo-de-exterminio-desenterrados-76-cuerpos)
- Regional: [El Diario de Chihuahua](https://eldiariodechihuahua.mx/estado/2026/aug/22/descubren-mas-osamentas-en-el-willy-casas-grandes-830223.html)
- Regional: [Diario MX](https://diario.mx/estado/2026/aug/21/hallan-mas-osamentas-en-excavaciones-de-el-willy-casas-grandes-1134450.html)
- Regional: [Juárez Noticias](https://juareznoticias.com/localizan-osamentas-y-restos-oseos-en-el-willy/)
- Regional: [El Bordo](https://elbordo.com.mx/local/localizan-osamentas-y-restos-oseos-en-el-willy-20260821-119939.html)
- Regional: [La Parada Digital](https://laparadadigital.com/hallan-mas-osamentas-en-el-willy/)

`CIFRA ACUMULADA EN CONFLICTO — NO INTEGRAR`: 56 (El Universal, con rastreo declarado concluido) ·
76 (Univisión) · ~91 · «cerca de 100» (Infobae). Antecedente verificable: 15-ene → 6-mar de 2025,
**78 restos en 63 fosas**, de los cuales **46 identificados** como personas de la región.

Atribución a **«La Línea»**: línea de investigación de la autoridad basada en el modo de
desmembramiento, **no hecho probado**.

---

## Sección 1 — Conteo nacional de armamento

| Rubro | Total del corte |
|---|---|
| Armas cortas | 2 |
| Armas largas | 1 (AK-47 7.62×39) |
| Cartuchos | 190 (180 de 7.62 + 10 de 9 mm) |
| Cargadores | 7 (6 largos + 1 corto) |
| AEI | 3 (destruidos en el sitio) |
| Armamento especial | 1 (vehículo con blindaje artesanal) |
| Granadas | 0 |
| Explosivos | 0 — **carga de los AEI no publicada**, no hay cantidad integrable |
| Drones armados | 0 |
| Personas detenidas (mismos eventos) | 8 |
| Entidades con aseguramiento | 2 (Sinaloa, Ciudad de México) |
| Eventos contabilizados | 3 |

**Totales: cálculo propio de ARGOS.** Cartuchos y cargadores nunca se suman entre sí.
**Deduplicación**: ningún evento fue publicado por dos corporaciones distintas en la ventana.

### Evento anterior NO integrado — discrepancia heredada

**Sinaloa — Concordia, Culiacán y Mazatlán** (hechos del 18-19 ago, difundidos el 21-22).
Desglose coincidente: 2,450 L de sustancias químicas · 98 cargadores · 8,095 cartuchos · 1 fusil
Barrett .50 · 6 armas largas · equipo táctico · sin detenidos.

`CIFRA EN CONFLICTO`: **72** AEI (El Universal, cobertura atribuida al Gabinete de Seguridad) frente
a **172** (El Heraldo de México, La Jornada, cobertura atribuida a la SEDENA). El resto del desglose
es idéntico, lo que apunta a **error de transcripción sobre un mismo boletín**, no a dos eventos.
**Hecho anterior al periodo y cifra sin resolver: NO INTEGRAR.**

- [El Universal — 72](https://www.eluniversal.com.mx/nacion/inhabilitan-laboratorio-clandestino-con-72-explosivos-en-sinaloa-hallan-mas-de-2-mil-litros-de-sustancias-para-hacer-droga/)
- [El Heraldo de México — 172](https://heraldodemexico.com.mx/nacional/2026/8/21/autoridades-federales-aseguran-172-artefactos-explosivos-improvisados-inhabilitan-laboratorio-de-droga-sintetica-en-sinaloa-873513.html)
- [La Jornada — 172](https://www.jornada.com.mx/2026/08/22/politica/007n2pol)
- Serie previa (18-ago, fuera de ventana): [303 AEI en El Rosario](https://heraldodemexico.com.mx/nacional/2026/8/18/encuentran-mas-de-300-artefactos-explosivos-improvisados-300-kilos-de-explosivos-en-el-rosario-sinaloa-871438.html)

---

## Sección 2 — Sentencias

**Cero sentencias dentro de la ventana.** `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`.

Dos recuperadas de la ventana de ARGOS 105, **no integradas al conteo nacional**:

- `ARG-106-SEN-REC-001` — FGJE Sonora, Hermosillo: León Felipe "N" y Francisco Antonio "N",
  **28 años 3 días**, homicidio y lesiones, hecho de jul-2024. Juicio oral iniciado 11-ago, fallo
  19-ago, individualización 20-ago, difusión 22-ago.
  [El Imparcial](https://www.elimparcial.com/son/hermosillo/2026/08/22/dos-sujetos-reciben-condena-de-28-anos-por-homicidio-en-hermosillo-tras-investigacion-de-la-fiscalia-de-sonora/)
  `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`: la fuente no precisa si los 28 años son por persona
  o cifra conjunta. **No sumable.** Leerla como «28 por persona» habría añadido 56 años sobre una
  interpretación no verificada.
- `ARG-106-SEN-REC-002` — FGE Guanajuato, León: Christian Gustavo "N", **27 años 11 meses**,
  feminicidio de su madre Melesia Rodríguez (51), hecho del 22-ene-2026. Difusión 22-ago.
  [Infobae](https://www.infobae.com/mexico/2026/08/22/sentencian-a-hombre-por-feminicidio-en-leon-guanajuato-entre-desafios-de-registro-y-justicia-en-la-entidad/)

### Resoluciones localizadas y descartadas

1. **Chihuahua** — 25 años por desaparición forzada y secuestro agravado, **19-ago**: anterior a la
   ventana de ARGOS 105. [El Bordo](https://elbordo.com.mx/local/le-dan-25-anos-por-secuestro-20260819-119734.html)
2. **Estado de México** — 90 años por secuestro (20-ago); 36 y 55 años por homicidio calificado
   **sin fecha exacta verificable**. No integran.
3. **FGR Tlaxcala** — 2a 6m por portación de arma, **18-ago**: anterior.
4. **Ciudad de México** — 125 años por secuestro exprés en Xochimilco: la búsqueda inicial lo situaba
   en agosto de 2026; **la verificación lo ubica en junio de 2026**. `DESCARTADO POR FECHA`.
   [La Silla Rota](https://lasillarota.com/metropoli/2026/6/19/dan-125-anos-de-prision-giovanni-n-tomas-n-por-secuestro-expres-agravado-en-xochimilco-604666.html)

---

## Verificación negativa — hechos descartados antes de publicar

1. **«25 elementos de la GN muertos tras el operativo contra El Mencho»**: los resultados de buscador
   lo presentaban sin fecha clara. La verificación sitúa los hechos en **febrero de 2026** (muerte de
   Nemesio Oseguera el 22-feb; declaración de García Harfuch el 23-feb). **Descartado.** Habría sido
   un error grave de periodo.
2. **Categorías sin hecho operativo en ventana**: huachicol, narcotráfico marítimo, extorsión y
   laboratorios clandestinos. Todos los eventos localizados (Huehuetoca 2-ago, El Arenal 14-ago,
   Chihuahua 18-ago; SEMAR Pacífico 7, 8, 15 y 16-ago; vinculaciones por extorsión en Guanajuato,
   CDMX, Michoacán y Edomex del 17 al 21-ago) son **anteriores al periodo**.
3. **Control de fecha futura** (regla de ARGOS 105): se comprobó que ninguna fecha atribuida a un
   hecho es posterior al día del corte. Ninguna lo era.
4. **Contexto no integrado**: informe de la Ibero sobre fosas clandestinas 2006-2024 (Guerrero 416,
   Veracruz 400, Sonora 381, Guanajuato 294, Jalisco 263). **Fuente académica, no oficial**: no
   alimenta ningún indicador. El total nacional **no se reproduce** —La Jornada consigna «más de
   5 mil» e Infobae «casi 3 mil», `DISCREPANCIA NO RESUELTA`—.
5. **Hechos declarativos no fichados**: la DEA reiteró el 24-ago que procederá contra políticos
   mexicanos con presuntos nexos con el CJNG, **sin nombrar a nadie ni presentar cargos**; y el
   Congreso de Sinaloa aprobó el 23-ago la licencia indefinida de Rubén Rocha Moya. **No son actos de
   autoridad con hecho criminal asociado** y no reciben ficha ni semáforo. Se registran aquí por si
   una edición posterior necesita la referencia.
   También se detectó una `CONTRADICCIÓN DE IDENTIDAD` sobre el presunto nuevo líder del CJNG:
   El Imparcial lo llama «Juan Carlos **González**, alias Pelón»; Proceso, «Juan Carlos **Valencia**,
   El Pelón». `NOMBRE EN CONFLICTO — NO UTILIZAR COMO DATO DE IDENTIFICACIÓN`.

---

## Indicadores oficiales — última publicación disponible

SESNSP, presentado el **11-ago-2026** (sin actualización en esta ventana): julio de 2026,
**42.5 homicidios dolosos diarios**, nivel más bajo desde 2015; **−51%** desde septiembre de 2024
(86.9 → 42.5); promedio ene-jul 2026, **48.6** diarios, cifra más baja para el periodo desde 2016;
**30 de 32** entidades con reducción; siete entidades concentran el **49%**: Guanajuato 8.6%,
Baja California 8.2%, Chihuahua 8.1%, Sinaloa 7.1%, Estado de México 6%, Guerrero 5.6%, Morelos 5.5%.

- [El Imparcial](https://www.elimparcial.com/mexico/2026/08/11/homicidios-dolosos-bajan-51-durante-gobierno-de-sheinbaum-julio-registra-el-nivel-mas-bajo-desde-2015/)
- [Contralínea](https://contralinea.com.mx/interno/semana/homicidios-dolosos-bajan-51-desde-septiembre-de-2024-sesnsp/)

---

## Controles editoriales aplicados

| Control | Estado | Resultado |
|---|---|---|
| `editor-duplicidad` | **Ejecutado manualmente** (`grep` sobre todos los `-fuentes.md`) | Ningún hecho de esta edición estaba publicado. **Halló lo contrario de lo buscado**: cuatro hechos de la ventana de ARGOS 105 que ninguna edición registra → fe de erratas y fichas `-REC-` |
| `procedencia-cifras` | **Ejecutado manualmente** | Toda cifra del cartelón tiene fragmento que la sostiene. Tres se declararon no integrables: 72/172 AEI, acumulado de El Willy, pena compuesta de Sonora |
| `barrido-regional` ×6 | **NO ejecutado** | Ninguna categoría de esta edición declara `SIN ACTUALIZACIÓN` apoyándose en cobertura: la casilla usada para las 27 entidades no revisadas es `NO REVISADA` |

Los tres controles existen como agentes en `.claude/agents/`. **No se invocaron como subagentes** en
esta sesión por restricción operativa expresa; los dos primeros se ejecutaron a mano con el mismo
criterio, y la ausencia del tercero se declara en el indicador de cobertura en vez de disimularse.
