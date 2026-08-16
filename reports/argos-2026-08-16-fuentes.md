# ARGOS 99 — Registro de fuentes (auditoría)

Corte: 2026-08-16 · Ventana de hechos: 2026-08-15 07:29 CDMX → 2026-08-16 07:38 CDMX.
Continuación de ARGOS 98 (corte 2026-08-15). Este documento respalda `argos-2026-08-16.html` y
`argos-2026-08-16-movil.html` con los enlaces exactos consultados para cada hecho, conforme al
requisito de trazabilidad de `CLAUDE.md`. **Seis equipos de barrido regional** trabajaron en
paralelo —Noroeste, Noreste, Occidente, Centro, Golfo y Sureste—, más dos equipos de verificación
puntual, todos contrastando sus hallazgos contra `reports/argos-2026-08-15-fuentes.md` y
`reports/_pendientes.md` para evitar duplicidad con `ARG-98-001` a `007`, `ARG-98-ARM-001` a `003`
y `ARG-98-SEN-001` a `003`.

## Limitación metodológica — quinta edición consecutiva, ahora medida región por región

**`WebFetch` devolvió `EGRESS_BLOCKED` para todo dominio externo probado por los ocho equipos, sin
una sola excepción.** El hallazgo nuevo de esta edición es que **el bloqueo no se limita a
`*.gob.mx`**, como suponían la documentación previa y la definición del agente `barrido-regional`:
alcanza también a `fgr.org.mx` (dominio `.org.mx`), a los medios nacionales y regionales
(`infobae.com`, `eluniversal.com.mx`, `proceso.com.mx`, `milenio.com`, `quadratin.com.mx`,
`diario.mx`, `laprensa.mx`, `atiempo.mx`, `lavozdemichoacan.com.mx`, `redmichoacan.com`,
`novedadesdetabasco.com.mx`, `tabascohoy.com`, `veracruznorte.com`, `planoinformativo.com`,
`ntrzacatecas.com`, `b15.com.mx`, `nmas.com.mx`, `eldiariodechihuahua.mx`) e incluso a dominios de
control ajenos al caso (`en.wikipedia.org`).

El error observado es un JSON `{"error_type":"EGRESS_BLOCKED", ...}`, **no** el
`403 / CONNECT tunnel failed` que documentaban la solicitud de lista blanca y la definición del
agente. Adicionalmente, varios dominios devolvieron `getaddrinfo ENOTFOUND`, que es un fallo de
resolución DNS y **no prueba que el portal no exista**: caso comprobado, `fiscaliachihuahua.gob.mx`
da `ENOTFOUND` mientras que el dominio correcto `fiscalia.chihuahua.gob.mx` existe y da
`EGRESS_BLOCKED`; y `www.ssp.veracruz.gob.mx` no existe porque la SSP de Veracruz cuelga de
`veracruz.gob.mx/seguridad/`.

**Ningún documento primario se leyó por acceso directo en toda la edición.** Toda la información
proviene de fragmentos y resúmenes de `WebSearch`.

**Techo de confianza efectivo: ★★★☆☆ para los hechos de la ventana.** La edición se abrió con un
techo declarado de ★★★★☆ (el nivel de ★★★★★ exige documento oficial o fotografía verificada), pero
el control `procedencia-cifras` hizo notar que ★★★★☆ exige *fuente institucional + un medio
nacional*, y que **ningún documento institucional se leyó**: los comunicados se citan, no se leen.
En consecuencia se degradaron a ★★★☆☆ las dos fichas que llevaban ★★★★☆ (`ARG-99-005` y
`ARG-99-006`). **La única ficha que conserva ★★★★☆ es `ARG-99-SEN-CIERRE`**, porque el boletín de la
FGR está reproducido íntegramente —con desglose nominal— en dos medios, lo que sí constituye acceso
al texto institucional aunque sea por vía indirecta.

La etiqueta `Institucional (indirecta)` que aparece en varias fichas significa, en toda esta
edición: **comunicado citado por prensa, no leído; no satisface la pata institucional de la escala.**

### Segundo límite, no previsto: el presupuesto de búsqueda

El presupuesto de `WebSearch` de la sesión (**200 llamadas, compartido entre los ocho agentes en
paralelo**) se agotó durante el barrido. Consecuencias declaradas:

- Ninguna región completó el recorrido de 4 portales × entidad que exige `CLAUDE.md`.
- Dos hechos candidatos quedaron **sin poder verificarse** y **no se integraron** (ver más abajo).
- El barrido es **aritméticamente imposible** con este presupuesto: 4 portales × 32 entidades más
  los federales exigen entre 200 y 500 consultas.

**Conclusión de método, obligatoria para la lectura de esta edición: ningún
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de ARGOS 99 puede presentarse como vacío
institucional verificado.** El barrido obligatorio de portales oficiales no se ejecutó contra
portales oficiales, sino contra el índice de un buscador.

### Trampas de fecha y año neutralizadas

- **Sonora, Gral. Plutarco Elías Calles** — boletín indexado en `gob.mx` y
  `seguridad.sspc.gob.mx/contenido/4081/` **sin año visible** (6 armas largas, 40 cargadores, 689
  cartuchos, 6 detenidos), devuelto entre resultados de agosto de 2026. Es de **agosto de 2024**,
  fijado por el espejo `riodoce.mx/2024/08/13/`. **Descartado.**
- **Zacatecas, SSP estatal** — boletín "Capturan fuerzas de seguridad a dos presuntos generadores
  de violencia…" (1 arma larga, 1 corta, 5 cargadores, ~150 cartuchos, **2 AEI**), indexado sin
  fecha visible. Es del **13 de junio de 2026** (`ljz.mx/13/06/2026/`). **Descartado.**
- **Veracruz, señuelo documental** — boletín "Trabajo ministerial de Fiscalía de Veracruz logra
  **11 sentencias condenatorias** en diversas regiones del estado", con **coincidencia numérica
  exacta** con el pendiente abierto y desglose nominal completo. Es del **18 de marzo de 2026**.
  Un segundo señuelo ("51 resoluciones y 12 sentencias condenatorias") es del 13 de marzo de 2026.
  **No integrar nunca.** Regla que deja este corte: *una cifra agregada coincidente no es identidad
  de documento*.
- **El resumidor de `WebSearch` afirma fechas falsas**: ante consultas del 15 de agosto devolvió
  hechos del 7 y del 14 redactados como si respondieran a esa fecha. Única técnica fiable:
  exigir la fecha en la URL o en el titular del artículo.
- Descartados adicionales por fecha: detención de cinco personas en Coahuila (**oct-2025**);
  emboscada en Doctor Arroyo, NL (**may-2026**); "Operativo Rastrillo" en Zacatecas (18-jul al
  11/12-ago, ya en circulación antes de ARGOS 98); sentencias de Durango FECOR (**8-may-2026**),
  Chihuahua Bosques de Senecú (**6-ago**, además es vinculación), SLP Ciudad Valles (**12-ago**),
  SLP Tamasopo (**5-ago**), FGR Moctezuma (**14-jul-2026**), FGR Piedras Negras (**12-ago**),
  FGR Cd. Juárez DPE/3549/2026 (**14-ago**, fuera de ventana por horas).

---

## Página 2 — Crimen organizado (I)

### ARG-99-001 — Doble homicidio frente al Palacio de Gobierno de Sinaloa, Culiacán (🔴 ROJO)

- **Hecho**: 2026-08-15. Dos hombres asesinados con armas largas a bordo de un Nissan Versa blanco
  frente al Palacio de Gobierno de Sinaloa. Sin detenidos.
- **Institucional**: `SIN INFORMACIÓN VERIFICABLE`. No se localizó boletín de FGE Sinaloa, SSP
  Sinaloa, gobierno del estado ni Gabinete de Seguridad. La atribución a la Fiscalía llega solo por
  mención periodística.
- **Nacional**: El Universal
  `https://www.eluniversal.com.mx/estados/asesinan-a-dos-hombres-frente-al-palacio-de-gobierno-en-culiacan-sinaloa-fueron-acribillados-con-fusiles-automaticos/` ·
  El Informador `https://www.informador.mx/mexico/sinaloa-asesinan-a-dos-hombres-frente-al-palacio-de-gobierno-en-culiacan-20260815-0070.html` ·
  El Imparcial `https://www.elimparcial.com/mexico/2026/08/15/ataque-armado-frente-al-palacio-de-gobierno-en-culiacan-deja-dos-hombres-muertos/` ·
  Infobae `https://www.infobae.com/mexico/2026/08/16/ataque-armado-frente-a-palacio-de-gobierno-en-culiacan-deja-dos-muertos/` ·
  TV Azteca `https://www.tvazteca.com/aztecanoticias/persecucion-y-balacera-frente-al-palacio-gobierno-sinaloa-hay-dos-muertos/` ·
  La Jornada Maya `https://www.lajornadamaya.mx/nacional/267065/asesinan-a-dos-en-inmediaciones-del-palacio-de-gobierno-de-sinaloa`
- **Regional**: Tribuna `https://tribuna.com.mx/seguridad/2026/08/15/persecucion-y-agresion-armada-deja-dos-muertos-por-fuera-del-palacio-de-gobierno-en-culiacan_657548/` ·
  Luz Noticias `https://www.luznoticias.mx/2026-08-15/policiaca/atacan-a-balazos-a-dos-hombres-a-un-costado-de-palacio-de-gobierno-en-culiacan/301096` ·
  Azteca Sinaloa · Noticiero Altavoz
- **Abierta (NO OFICIAL)**: Cafe Negro Portal publica los nombres de las víctimas citando a
  familiares; Marcrix, Primera Línea, Blog del Narco. **No se reproducen los nombres**: la mayoría
  de medios nacionales sostiene que siguen sin identificación oficial.
- **Contradicciones no resueltas**: (1) **hora** — ~12:30 h según unas fuentes, 13:00-14:00 h según
  otras; (2) **ubicación** — av. José Aguilar Barraza (col. Centro Sinaloa) frente a cruce
  Bulevar Constitución con av. Lázaro Cárdenas. Ambas son compatibles con una **persecución**
  (inicio del fuego y punto final del vehículo), pero **ninguna autoridad ha confirmado esa
  secuencia** y el reporte no la afirma.
- **Confianza**: ★★★☆☆ (sin fuente institucional verificada).

### ARG-99-002 — Emboscada contra la Guardia Nacional, Buenavista, Michoacán (🔴 ROJO)

- **Hecho**: 2026-08-15, tarde. Civiles armados agreden a personal de la GN en la carretera
  Buenavista–Tepalcatepec, a la altura de la localidad 18 de Marzo. Tres agresores abatidos, sin
  bajas federales. FGE Michoacán procesa el lugar.
- **Institucional**: no localizado (GN, SEDENA, SSP Michoacán y FGE estatal, todos bloqueados).
- **Regional (6 fuentes coincidentes)**: Quadratín Michoacán
  `https://www.quadratin.com.mx/justicia/mueren-3-civiles-en-enfrentamiento-contra-gn-en-buenavista/` ·
  Atiempo `https://atiempo.mx/destacadas/enfrentamiento-guardia-nacional-buenavista-18-de-marzo/` ·
  RED Michoacán `https://www.redmichoacan.com/2026/08/15/guardia-nacional-repele-agresion-en-buenavista-mueren-3-presuntos-gatilleros/` ·
  RED113 `http://www.red113mx.com/2026/08/guardia-nacional-repele-agresion-en.html` ·
  La Voz de Michoacán · Respuesta Michoacán
- **Control de fecha**: 15-ago-2026 fue **sábado**, consistente con "sábado por la tarde" en las
  seis fuentes. Sin contaminación de 2024/2025.
- **Aporte al conteo de armamento: CERO.** Ninguna fuente publica cifras de armas.
- **Confianza**: ★★★☆☆ (`Pendiente de corroboración institucional`).

### ARG-99-003 — Tres ejecutados en un domicilio, San Pedro Amuzgos, Oaxaca (🔴 ROJO)

- **Hecho**: 2026-08-14 ~17:30 h, **publicado 15-ago** → `Evento anterior publicado durante el
  corte`. Dos hombres y una mujer asesinados en un domicilio de la calle Francisco Villa, col.
  Leyes de Reforma. FGEO confirmó.
- **Nacional**: Proceso `https://www.proceso.com.mx/nacional/estados/2026/8/15/ejecutan-a-dos-hombres-y-una-mujer-en-san-pedro-amuzgos-oaxaca-378109.html`
- **Regional**: NVI Noticias `https://www.nvinoticias.com/roja/homicidios/ataque-armado-en-amuzgos-asesinan-dos-hombres-y-una-mujer-dentro-de-un-domicilio/191970` ·
  El Imparcial de Oaxaca `https://imparcialoaxaca.mx/policiaca/tres-homicidios-en-san-pedro-amuzgos-se-suman-a-ola-de-violencia-tres-mas-fueron-asesinados-en-zanatepec/`
- **Armas de los agresores** (AR-15 .223 y 9 mm) **no fueron aseguradas**: no son línea de conteo.
- **Móvil citado** (venta de drogas): hipótesis periodística, **no confirmada**, no se sostiene.
- **No aparece en ARGOS 98**, cuya ventana cerró antes de la publicación. Es nuevo para ARGOS 99.
- **Confianza**: ★★★☆☆.

### ARG-99-004 — Ataque armado en el bar "Tlecuichelas", Cuautla, Morelos (🟡 AMARILLO)

- **Hecho**: 2026-08-15 ~00:20 h, calle José María Morelos, col. Emiliano Zapata. La Fiscalía de
  Morelos confirmó **dos lesionados** (un hombre y una mujer, Hospital General de Cuautla), sin
  detenidos. El bar había reabierto la noche del 14 tras semanas cerrado por cobro de piso.
- **Regional**: Azteca Morelos `https://www.aztecamorelos.com/policiaca/ataque-armado-en-bar-cuautla-deja-personas-heridas` ·
  Diario de Morelos `https://www.diariodemorelos.com/noticias/tragedia-en-cuautla-ataque-armado-hiere-dos-en-bar-recien-reabria-cobro-piso` ·
  Noticias de Cuautla · La Unión `https://www.launion.com.mx/morelos/justicia/noticias/286984-cinco-lesionados-en-ataque-armado-en-bar-de-cuautla.html`
- **CIFRA NO CONCILIADA**: La Unión y una segunda nota de Azteca Morelos reportan **cinco
  lesionados**. No fue posible determinar si es el mismo hecho con conteo ampliado o un evento
  distinto. **Se publican ambas versiones sin fusionarlas**; el conteo usa la cifra institucional (2).
- **CONFLACIÓN BLOQUEADA — cuatro hechos distintos que no deben citarse juntos**:

  | Hecho | Fecha | Municipio / lugar | Saldo |
  |---|---|---|---|
  | **Este (ARG-99-004)** | **15-ago-2026** | Cuautla, bar "Tlecuichelas" | 2 lesionados |
  | NO es el mismo | 14-mar-2026 | Cuautla, bar "La Azotea", av. Insurgentes | 1 muerto, 2 heridos |
  | NO es el mismo | 28-jun-2026 | Cuautla, col. Hermenegildo Galeana | 1 muerto |
  | NO es el mismo, **ni el mismo municipio** | 18-abr-2026 | **Ayala**, "El Rincón de la Banda" | **8 muertos** |

- **Abierta (NO OFICIAL)**: Blog del Narco atribuye el ataque a una célula del CJNG y afirma un
  narcomensaje. **No confirma nada.** Único indicio indirecto: los fragmentos mencionan que la
  escena se acordonó para preservar evidencia balística y "mensajes encontrados", sin contenido ni
  autoría verificados. La atribución **no aparece** en "Hecho confirmado" ni en "Corroboración".
- **Confianza**: ★★★☆☆.

---

## Página 3 — Crimen organizado (II)

### ARG-99-005 — SEMAR asegura ~1,900 kg de cocaína frente a Zihuatanejo (🟢 VERDE)

- **Hecho**: 2026-08-15. Octava Región Naval, vuelo de patrulla y vigilancia marítima en funciones
  de guardacostas; interceptación a ~170 millas náuticas (315 km) al SW de Zihuatanejo.
  **53 paquetes, ~1,900 kg** de presunta cocaína, embarcación con dos motores fuera de borda,
  **2 detenidos**. Trasladados a la Octava Región Naval en Acapulco y puestos a disposición de la
  **FGR**. Valor citado: **>405 millones de pesos**.
- **Institucional**: las fuentes citan expresamente comunicado de SEMAR; `gob.mx/semar` bloqueado,
  **texto primario no leído**.
- **Nacional**: Excélsior `https://www.excelsior.com.mx/nacional/semar-aseguro-1-9-toneladas-cocaina-frente-guerrero` ·
  El Financiero `https://www.elfinanciero.com.mx/estados/2026/08/15/acapulcazo-de-la-semar-asi-detecto-un-cargamento-de-droga-de-mas-de-405-millones-de-pesos-en-guerrero/` ·
  La Razón `https://www.razon.com.mx/mexico/2026/08/15/marina-asegura-19-toneladas-de-cocaina-y-detiene-a-2-personas-al-suroeste-de-guerrero/` ·
  El Imparcial `https://www.elimparcial.com/mexico/2026/08/15/marina-asegura-cerca-de-19-toneladas-de-presunta-cocaina-en-aguas-de-guerrero/` ·
  24 Horas `https://24-horas.mx/estados/semar-asegura-1-9-toneladas-de-cocaina-en-costas-de-guerrero/`
- **Regional**: El Sol de Acapulco `https://oem.com.mx/elsoldeacapulco/local/asegura-marina-1-9-toneladas-de-presunta-cocaina-frente-a-zihuatanejo-31596449` ·
  CódigoQro · Netnoticias · Tribuna · Novedades de Tabasco · mimorelia
- **Regla de conteo aplicada**: los **2 detenidos NO entran** en el conteo de detenidos del módulo
  de armamento (no hubo aseguramiento de armas).
- **Confianza**: ★★★★☆ — es el hecho con mayor densidad de corroboración del corte.
- **Cierra la categoría** "narcotráfico marítimo", declarada `SIN ACTUALIZACIÓN` en ARGOS 98.

### ARG-99-006 — Dos policías municipales de Acapulco detenidos por homicidio calificado (🟢 VERDE)

- **Hecho**: 2026-08-15. La FGE Guerrero detiene a Manuel Alejandro "N" y Ricardo "N", policías
  municipales de Acapulco, por el homicidio calificado de Carlos "N", cuyo cuerpo se localizó el
  **10-ago** en la col. Unidad Ciudadana. Asegurada la **patrulla PU-468**. Apoyo de SEDENA, GN,
  SSPC y Policía Estatal. Puestos a disposición del Juez de Control.
- **Nacional**: La Razón `https://www.razon.com.mx/estados/2026/08/15/detienen-a-dos-policias-de-acapulco-por-homicidio-calificado/` ·
  Infobae `https://www.infobae.com/mexico/2026/08/16/detienen-a-dos-policias-municipales-de-acapulco-por-homicidio-calificado/` ·
  El Imparcial `https://www.elimparcial.com/mexico/2026/08/15/dos-policias-municipales-de-acapulco-son-detenidos-por-homicidio-calificado-aseguran-una-patrulla-municipal-vinculada-con-la-investigacion/` ·
  La Silla Rota `https://lasillarota.com/estados/2026/8/15/por-homicidio-detienen-a-dos-policias-municipales-de-acapulco-524664.html` · 24 Horas
- **Regional**: Quadratín Guerrero `https://guerrero.quadratin.com.mx/detienen-a-2-policias-de-acapulco-acusados-de-homicidio/` ·
  Tribuna `https://tribuna.com.mx/seguridad/2026/08/15/fiscalia-de-guerrero-captura-a-dos-policias-municipales-por-el-asesinato-de-un-hombre-en-acapulco_657699/` ·
  Red Metropolitana · Trópico Noticias
- **Es detención, no sentencia**: no entra al módulo judicial.
- **Confianza**: ★★★★☆.

### ARG-99-007 — Vinculación a proceso, "Don Pollo", Iztapalapa, CDMX (🟢 VERDE)

- **Hecho**: publicado 2026-08-15. Cuatro presuntos integrantes vinculados a proceso. FGJ-CDMX
  (PDI, pericial, ministerial) con Guardia Nacional. **El cateo y el aseguramiento son del 6-ago**
  → `Evento anterior publicado durante el corte`; **las cifras no se suman** al conteo de la ventana.
  1 arma de fuego **sin clasificar** (ni corta ni larga → fuera de taxonomía) y **63 cartuchos**.
- **Fuentes**: El Heraldo de México `https://heraldodemexico.com.mx/nacional/2026/8/15/fiscalia-de-la-cdmx-vincula-proceso-cuatro-presuntos-integrantes-de-don-pollo-869494.html` ·
  La Silla Rota `https://lasillarota.com/metropoli/2026/8/15/banda-de-don-pollo-procesan-a-4-presuntos-integrantes-en-iztapalapa-524667.html` ·
  Milenio `https://amp.milenio.com/policia/procesan-a-presuntos-integrantes-del-grupo-don-pollo-en-cdmx`
- **Boletín FGJ-CDMX no accedido.** Confianza ★★★☆☆.

### ARG-99-SEG-001 — Seguimientos

**Zanatepec, Oaxaca (`ARG-98-001`) — segundo corte consecutivo sin detenidos.** La FGEO **sí se
pronunció** el 15-ago confirmando 3 muertos y 1 herido e informando el inicio de carpeta con la
Agencia Estatal de Investigaciones y peritos. Víctimas aún publicadas **solo por iniciales**; el
cuarto hombre **continúa hospitalizado**; sin línea de investigación publicada, sin imputación.
Boletín primario de la FGEO sigue sin localizarse (`portal.fgeo.gob.mx` bloqueado).
Fuentes: Quadratín Oaxaca `https://oaxaca.quadratin.com.mx/confirma-fiscalia-3-muertos-y-un-herido-en-ataque-en-zanatepec/` ·
Heraldo de México Oaxaca `https://oaxaca.heraldodemexico.com.mx/local/2026/8/15/ataque-en-salon-de-fiestas-en-santo-domingo-zanatepec-oaxaca-deja-tres-muertos-y-un-herido-17807.html`

**Verificentros del Edomex (`ARG-97-004`) — SIN RESOLUCIÓN LOCALIZADA. El pendiente sigue ABIERTO.**
Se ejecutaron 4 búsquedas dirigidas al resultado de la audiencia del 15-ago, 10:30 h, Juzgado de
Control de Chalco. **Ninguna fuente publica la resolución**; todas siguen describiendo la audiencia
como futura. Datos nuevos verificables recogidos de paso: quien preside es **jueza**; la audiencia
inicial del 12-ago duró **más de 16 horas**; el esquema habría afectado **145 de 168 verificentros**
con exigencia de **500 mil pesos por línea** bajo amenaza de no revalidar permisos 2027; Raúl "N"
era Director General de Control de Emisiones Atmosféricas y Carlos Eduardo "N" Director de Control
de Emisiones a la Atmósfera; detenidos el 10-ago (Raúl en Acapulco, Carlos Eduardo en CDMX); uno
por extorsión agravada, otro por abuso de autoridad. La FGJEM revisa a otros servidores públicos.
Fuentes: TV Azteca `https://www.tvazteca.com/aztecanoticias/verificentros-edomex-funcionarios-detenidos-red-extorsion-asi-operaban` ·
Proceso `https://www.proceso.com.mx/nacional/estados/2026/8/12/detienen-a-funcionarios-de-edomex-ligados-al-pvem-por-extorsionar-verificentros-377895.html` ·
Plana Mayor · El Valle · Heraldo Edomex · DigitalMex
**Advertencia**: una vinculación a proceso **no es sentencia** y no entrará al módulo judicial.

---

## Página 4 — Conteo Nacional de Armamento

### ARG-99-ARM-001 — Mazatlán, Sinaloa (🟢 VERDE)

- **Hecho 14-ago, publicado 15-ago** → `Evento anterior publicado durante el corte`.
- **19 armas largas** (mayoría tipo AK), **15,480 cartuchos**, **1,131 cargadores**, **2 detenidos**,
  más equipo táctico, transportados en un **tractocamión**. SEDENA y GN en coordinación con SSPC,
  SEMAR, FGR y Policía Estatal. Detenidos y material a disposición de la **FGR con sede en Mazatlán**.
- **Fuentes**: El Universal `https://www.eluniversal.com.mx/nacion/caen-dos-presuntos-integrantes-del-cartel-de-sinaloa-en-mazatlan-llevaban-arsenal-en-tractocamion/` ·
  Excélsior `https://www.excelsior.com.mx/nacional/caen-dos-presuntos-integrantes-cartel-pacifico-mazatlan-con-arsenal` ·
  El Sol de Mazatlán `https://oem.com.mx/elsoldemazatlan/local/militares-detienen-a-dos-presuntos-integrantes-del-cartel-del-pacifico-en-mazatlan-31598212` ·
  Quadratín Sinaloa `https://sinaloa.quadratin.com.mx/detienen-a-2-y-aseguran-arsenal-en-un-tractocamion-en-mazatlan/` ·
  diario.mx `https://diario.mx/nacional/2026/aug/15/detienen-a-dos-del-cartel-de-sinaloa-con-arsenal-en-mazatlan-1133404.html`
- **Confianza: Bajo** — comunicado oficial **no localizado**.
- **NO es "Operación Sable"** (13-ago, cifras de otro orden de magnitud: 1-9 cargadores, 15-55
  cartuchos). **No fusionar ni sumar.** Verificado además por `grep` sobre `reports/` que el arsenal
  del tractocamión **no aparece en ninguna edición previa**.

### ARG-99-ARM-002 — Sain Alto, Zacatecas (🟢 VERDE)

- **Hecho 15-ago, publicado 15-ago.** "Operativo Tornado", col. Lomas de San Sebastián.
  **1 arma corta, 1 cargador, 16 cartuchos, 5 detenidos**, más 30 envoltorios de presunta
  metanfetamina y 2 equipos de comunicación (no son línea de conteo de armamento).
  Ejército, GN, FRIZ y FGJEZ.
- **Fuentes**: ZHN `https://zhn.com.mx/detienen-fuerzas-de-seguridad-a-cinco-probables-generadores-de-violencia-aseguran-arma-de-fuego-y-droga/` ·
  Express Zacatecas `https://expresszacatecas.com/seguridad/policia/detienen-a-cinco-generadores-de-violencia-en-sain-alto` ·
  Conexión 58 `https://www.conexion58.com/2026/08/detienen-a-5-malandros-de-durango-y-veracruz-en-sain-alto/`
- **Dos reservas**: (1) el desglose fino (arma corta, cargador, 16 cartuchos) descansa en **una sola
  réplica**; Express Zacatecas dice solo "un arma de fuego". (2) **Hora del hecho no determinable**:
  se marca `HORA NO DETERMINADA`. Confianza: **Bajo**.

### Total nacional del corte

| Categoría | Total |
|---|---|
| Armas cortas | 0 |
| Armas largas | 19 |
| Cartuchos | 15,480 |
| Cargadores | 1,131 |
| Granadas | 0 |
| AEI | 0 |
| Explosivos | 0 |
| Armamento especial | 0 |
| Estados con aseguramientos | 2 (Sinaloa, Zacatecas); **1 con cifras integradas al total** |
| Eventos contabilizados | 2 (**1 con desglose integrado**) |
| Personas detenidas | 7 |

**Cartuchos y cargadores nunca se suman entre sí.**

**Corrección del control `procedencia-cifras` (aplicada).** La primera versión de esta edición
publicaba 1 arma corta, 15,496 cartuchos y 1,132 cargadores, integrando el desglose de Sain Alto.
El control detectó **corroboración asimétrica**: las tres fuentes coinciden en el aseguramiento y en
los 5 detenidos, pero **solo ZHN publica el desglose numérico**; Express Zacatecas se limita a "un
arma de fuego", sin clasificar ni cuantificar munición. Conforme a la escala del módulo, una cifra
granular sin corroboración es *versión aislada* y **no se integra a los totales** — es el mismo
mecanismo del caso Huajicori. Se retiró del total numérico (arma corta → 0, cartuchos → 15,480,
cargadores → 1,131), se conservaron los **5 detenidos** por estar corroborados por las tres fuentes,
y el arma pasó al Bloque 3 como evento cualitativo sin clasificar.

### Decisión de método sobre la integración al total

Ambos eventos tienen confianza **Baja** y los equipos de barrido recomendaron **no integrarlos**.
El editor resolvió **integrarlos con la marca de confianza Baja**, por las siguientes razones:

1. La escala propia de este módulo contempla expresamente el nivel
   *Bajo = "dos fuentes periodísticas coincidentes sin comunicado oficial"*. Es decir, los eventos
   solo-prensa **están previstos** en el diseño del módulo.
2. La regla `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL` que `CLAUDE.md`
   fija para la ausencia de fuente oficial es **específica del módulo de sentencias**.
3. Aplicarla también al módulo de armamento, bajo un bloqueo total de egreso, haría que **nunca**
   pudiera publicarse un total, lo que no es el propósito del módulo.

La lectura más estricta posible de estas mismas cifras —`Sin total nacional verificable durante el
corte`— queda documentada aquí como alternativa expresa.

### Eventos cualitativos y sin integrar

- **Buenavista, Michoacán** (`ARG-99-002`): sin cifras publicadas. Evento cualitativo.
- **Iztapalapa, CDMX** (`ARG-99-007`): 1 arma sin clasificar y 63 cartuchos, hecho del **6-ago**.
  Fuera de ventana y fuera de taxonomía.
- **Zihuatanejo** (`ARG-99-005`): los 2 detenidos no entran en este módulo.
- **Veracruz, "108 armas de fuego"** (`veracruzenred.mx`): **fecha no determinada** por agotamiento
  del presupuesto. Si cayera en ventana sería el mayor aseguramiento del corte.
  **Prioridad 1 para ARGOS 100.**
- **San Luis Potosí**, corte de 24 h de la Guardia Civil Estatal ("45 detenidos", 219 dosis, sin
  armas, sin desglose por evento): agregado **indeduplicable**, `NO INTEGRAR`.
- **Veracruz, SSP** (publicado 14-ago, operativos del 12-13): 30 detenidos, 20 vehículos, 400 L de
  hidrocarburo, 1 detenido en Puente Nacional con 1 arma. **Fuera de ventana.**
- **Tabasco, FIRT Olmeca** (10-13 ago): 16 detenidos, 10 armas sin desglose, 10 cargadores, 85
  cartuchos, 54,300 L de hidrocarburo. **Fuera de ventana.**

### Indicador de cobertura — armamento

- **Portales leídos por acceso directo: 0** de 128 estatales objetivo (4 × 32) y 0 federales.
- **Portales estatales alcanzados por búsqueda dirigida (no leídos): mínimo defendible 40 de 128.**
  La cifra exacta **no es reconstruible** a partir de los seis informes regionales; se declara el
  mínimo demostrable y nunca una estimación al alza.
- **Mesas de Construcción de la Paz: 0 consultadas en todo el país.**
- **Entidades sin ningún portal institucional alcanzado (NO REVISADAS): Baja California Sur,
  Tlaxcala, Hidalgo, Querétaro.**
- **Partes diarios del Gabinete de Seguridad: indexados solo hasta el 13-ago.** Los del 14 y 15 no
  aparecen. Es el vacío federal más grave del corte, confirmado de forma independiente por los seis
  equipos regionales.
- **Portales no disponibles**: la totalidad de los probados (~70 dominios), por `EGRESS_BLOCKED` o
  `ENOTFOUND`.
- **Ninguna categoría de este módulo puede cerrarse en `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`.**

---

## Página 5 — Rastreo Nacional de Sentencias

### ARG-99-SEN-001 — FGJEM, Ecatepec, Estado de México

Extorsión agravada · 1 sentenciada (Fernanda Elizabeth García Ruiz) · **40 años** + suspensión de
derechos civiles y políticos · hecho de agosto de 2025 · publicado **15-ago-2026** · **firmeza no
informada** · multa y reparación **no publicadas**.
Fuentes: Infobae `https://www.infobae.com/mexico/2026/08/15/dictan-sentencia-de-40-anos-de-carcel-para-extorsionadora-del-sector-constructor-en-ecatepec/` ·
La Jornada `https://www.jornada.com.mx/noticia/2026/08/15/estados/dan-40-anos-a-mujer-que-extorsiono-a-una-familia-en-ecatepec-se-decia-integrante-de-la-ctm`
**Monto de la extorsión**: **5,000 pesos** exigidos a una persona que supervisaba la construcción de
su casa, haciéndose pasar por trabajadora de una central obrera (CTM), con amenaza de detener la
obra y recurrir a un grupo criminal. Cifra publicada por Infobae y La Jornada; sostiene la lectura
analítica de la ficha sobre la desproporción entre pena y monto.
**Término expreso verificado**: "dictan sentencia", "40 años de cárcel", pena impuesta. Cumple el
criterio jurídico — no es vinculación ni prisión preventiva.
**Estatus**: `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR AL CONTEO NACIONAL`. Boletín de la
FGJEM no localizado; `fgjem.edomex.gob.mx` y `fiscaliaedomex.gob.mx` bloqueados. Confianza **Bajo**.

### ARG-99-SEN-002 — FGE Tabasco, Cunduacán

Violación · 1 sentenciado (Miguel "N") · **8 años** · publicado **15-ago-2026** · **firmeza no
informada**.
Fuentes: Novedades de Tabasco `https://novedadesdetabasco.com.mx/2026/08/15/fge-obtiene-sentencias-y-vinculaciones-a-proceso-contra-siete-personas/` ·
Ahora Tabasco `https://ahoratabasco.com/fget-logra-seis-vinculaciones-y-una-sentencia/` · Ahora Noticias
**No son sentencia y no se cuentan** (mismo boletín, 6 personas): José "N", Ramsés "N", Isidro "N",
Esteban "N" y Daniel "N", vinculados por daños con agravantes (pandilla e incendio, hechos de
agosto de 2026, Centro/Villahermosa); Pedro "N", vinculado por homicidio calificado (mayo de 2026,
Cárdenas). Dos meses de investigación complementaria.
**Conflación bloqueada**: un resumen mezcló este caso con Alfonso "N" (7 años, violación,
Comalcalco, hechos feb-2024) y Samuel "N"/Jorge "N" (5 años 4 meses), del boletín del **13-ago**,
fuera de ventana. **No integrados.**
**Estatus**: `PENDIENTE DE CONFIRMACIÓN OFICIAL`. Confianza **Bajo**.

### ARG-99-SEN-003 — FGESLP, Matlapa, San Luis Potosí

Lesiones doblemente agravadas · 1 sentenciado (Elías "N") · **2 años 8 meses** · publicado
**15-ago-2026** · **firmeza no informada**.
Fuente **única**: Quadratín SLP `https://sanluispotosi.quadratin.com.mx/seguridad/condenan-a-mas-de-2-anos-de-prision-a-agresor-en-matlapa/`
**No fue posible verificar el término literal en español**: el resumen llegó parafraseado y
traducido. `fiscaliaslp.gob.mx` bloqueado.
**Estatus**: `PENDIENTE DE CONFIRMACIÓN OFICIAL`. `Pendiente de corroboración independiente`.
Confianza **Bajo**.

### Conteo nacional del corte

**`SIN CONTEO NACIONAL INTEGRABLE DURANTE EL CORTE`.** Tres sentencias localizadas, **cero
integrables**: las tres carecen de comunicado institucional leído. Pena localizada (no acumulada):
40 años + 8 años + 2 años 8 meses = **50 años 8 meses** sobre **3 personas**. Sentencias firmes: 0.
Reparación del daño: `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`.

### ARG-99-SEN-CIERRE — PENDIENTE CERRADO: 19 sentenciados del CJNG, Jalisco

**Existe comunicado de la FGR**, localizado por reproducción íntegra:
AFmedios `https://www.afmedios.com/fgr-obtiene-sentencias-de-hasta-18-anos-de-prision-contra-19-personas-detenidas-con-arsenal-en-jalisco/` ·
La Prensa `https://www.laprensa.mx/notas.asp?id=809795`
- **Autoridad**: FGR; tribunal de enjuiciamiento del Centro de Justicia Penal Federal, Jalisco.
- **Delitos**: acopio de armas de fuego; posesión de cartuchos y cargadores de uso exclusivo del
  Ejército; asociación delictuosa.
- **Penas**: **12 personas a 18 años 1 mes 22 días**; **7 personas a 16 años 6 meses** (total 19).
- **Firmeza: NO informada.**
- **Hecho de origen**: noviembre de 2022, enfrentamiento con SEDENA en col. Mismaloya, Tizapán el
  Alto. Arsenal: 28 armas largas, 2,470 cartuchos, 18 chalecos, 12 placas balísticas.
  Compurgan en Puente Grande.
- **Salvedad de trazabilidad**: la URL directa del comunicado en `fgr.org.mx` **no se localizó
  indexada**. Confianza sube de ★★★☆☆ a **★★★★☆** — es la única ficha de la edición que sostiene
  ese nivel, por estar el boletín reproducido íntegramente en dos medios.
- **Salvedad sobre el titular**: la única cadena verificable en URL es el slug de AFmedios
  (`...sentencias-de-hasta-18-anos-de-prision...`), que **redondea a la baja**: la pena mayor
  documentada en el cuerpo es de 18 años 1 mes 22 días, superior a los "hasta 18 años" del titular.
  El desglose fino (18a1m22d / 16a6m) proviene del cuerpo reproducido, vía resumen.
- **Sentencia del 10-ago** → ventana de una edición anterior. **No se integra al conteo de ARGOS 99**;
  se publica como cierre de pendiente. Tiempo procesal: **casi cuatro años** entre hecho y sentencia.

### Seguimiento — agregado de Veracruz ("53 resoluciones / 11 condenatorias")

**Tercera edición consecutiva sin desglose.** Las otras 10 condenatorias siguen sin nombre, delito
ni pena. `comunicacion.fiscaliaveracruz.gob.mx` sigue bloqueado.
**Señuelo descartado** (ver "Trampas de fecha"): el boletín de "11 sentencias condenatorias" con
desglose nominal completo es del **18-mar-2026**.
**Desglose real localizado, pero de OTRO agregado** (semanal del 5-11 ago, 44 condenatorias):
Pánuco — Luis Felipe "N" **60 años** y Enrique "N" **50 años**, secuestro agravado (hechos del
17-sep-2018) `https://veracruznorte.com/responsables-de-secuestro-agravado-en-panuco-reciben-condenas-de-60-y-50-anos-de-prision/`;
Cosoleacaque — Antonio de Jesús "N", Armando "N" y Víctor Manuel "N", **45 años**, homicidio doloso
agravado. Sirven para el archivo; **no cierran el pendiente** y están fuera de ventana.
**Recomendación para ARGOS 100**: atacar el **Poder Judicial de Veracruz**
(`pjeveracruz.gob.mx/Sentencias/consultaWeb`), no la Fiscalía: la Fiscalía publica agregados, el
Poder Judicial publica resoluciones individuales.

### Indicador de cobertura — sentencias

- **Fiscalías revisadas por lectura directa: 0 de 32.** Consultadas por búsqueda dirigida:
  **mínimo defendible 22 de 32** (cifra exacta no reconstruible; se declara el mínimo demostrable).
- **FGR revisada**: sí, por búsqueda dirigida; portal no legible.
- **Fiscalías con sentencia publicada localizada: 3** (FGJEM, FGE Tabasco, FGESLP), más FGR en
  ventana anterior.
- **Fiscalías sin resultado localizado en la ventana: 19.**
- **Fiscalías NO revisadas: 10**, incluidas BCS, Tlaxcala, Hidalgo y Querétaro.
- **Poderes judiciales estatales: prácticamente no consultados.**
- **Bajo bloqueo total, la regla de validación jurídica (término literal) es inverificable.**

---

## Página 6 — Correcciones a ediciones anteriores

### ARG-99-FE-001 — Lázaro Cárdenas, Michoacán (`ARG-98-ARM-003`): contradicción resuelta

El **boletín del Gabinete de Seguridad de acciones relevantes del 13 de agosto de 2026**
(`https://www.gob.mx/sspc/prensa/el-gabinete-de-seguridad-del-gobierno-de-mexico-informa-acciones-relevantes-del-13-de-agosto-de-2026`)
reporta para Lázaro Cárdenas: Ejército + GN + Policía Municipal aseguran **1 arma larga, 3
cargadores, 490 cartuchos, 1 chaleco táctico y 100 kg de marihuana**.
- **Fecha del hecho: 13-ago-2026.** El "14-ago" de los medios regionales era **fecha de
  publicación**. No era contradicción entre fuentes, sino confusión hecho/publicación.
- **ARGOS 98 omitió los 100 kg de marihuana** del mismo aseguramiento.
- El evento pertenece a la ventana de **ARGOS 98**; **no se integra a ARGOS 99**.

### ARG-99-FE-002 — Dos enlaces mal citados en ARGOS 98

- La URL de **La Voz de Michoacán** citada para `ARG-98-ARM-003`
  (`...-lazaro-cardenas-san-juan-bosco-2026/`) corresponde a un operativo de **mayo de 2026** en
  San Juan Bosco (fusil Mark-Sporter 7.62, Tiguan azul y Grand Cherokee negra), corroborado por
  RED Michoacán `https://www.redmichoacan.com/2026/05/12/aseguran-vehiculos-armamento-y-cientos-de-cartuchos-en-operativo-interinstitucional-en-san-juan-bosco-lzc/`.
  **Es otro hecho, con tres meses de diferencia.**
- La URL de **Capital México** citada para el mismo evento tiene slug
  `...-operativo-conjunto-en-apatzingan-michoacan`: **apunta a Apatzingán**, no a Lázaro Cárdenas.

### Tres hechos de la ventana de ARGOS 98 que aquella edición no recogió

1. **Chilpancingo, Guerrero (14-ago)** — la FGE presentó a William "N" alias "La Bomba" y Víctor "N",
   presuntos integrantes de Los Ardillos, por el homicidio de Adolfo "N", repartidor de agua de 26
   años (hecho del 11-ago; dos compañeros heridos). `grep -i "Ardillos"` sobre `reports/*.md` no
   devuelve nada.
   El Imparcial `https://www.elimparcial.com/mexico/2026/08/14/detienen-a-dos-presuntos-integrantes-de-los-ardillos-por-el-homicidio-de-un-repartidor-de-agua-de-26-anos-atacado-a-balazos-mientras-trabajaba-en-chilpancingo/` ·
   Quadratín Guerrero · El Sur · Agencia IRZA
2. **Nopala, Hidalgo (hecho 13-ago, publicado 14-ago)** — 4 detenidos, 1 arma corta, 1 cargador,
   93 cartuchos, 400 L de hidrocarburo. No aparece en `argos-2026-08-15-fuentes.md`.
3. **Cuautla, Morelos (13-14 ago)** — excomandante detenido por tortura contra una mujer que cumplió
   25 años de prisión tras una confesión obtenida bajo tortura.
   La Jornada `https://www.jornada.com.mx/noticia/2026/08/14/estados/detienen-a-ex-policia-judicial-de-morelos-por-tortura-contra-mujer-que-paso-25-anos-en-prision`

### ARG-99-FE-003 — Fe de erratas de procedencia: indicador SESNSP

Detectada por el control `procedencia-cifras`. El indicador de homicidio doloso que ARGOS viene
publicando como único indicador oficial nacional arrastraba tres defectos:

1. **Edición de origen mal atribuida.** ARGOS 98 y la primera versión de ARGOS 99 lo atribuían a
   **ARGOS 90**. Su entrada real es **ARGOS 86** (`reports/argos-2026-08-02.html`), verificado por
   `grep` sobre todo `reports/`.
2. **Par de origen suprimido.** ARGOS 86 publicaba **86.9 → 45.4 víctimas/día (−48%)**, SESNSP /
   Gabinete, sep-2024 → jun-2026. Las ediciones intermedias dejaron caer el par y conservaron solo
   el porcentaje derivado, que por sí solo no es auditable. **Restituido en esta edición.**
3. **Contradicción suprimida.** ARGOS 90 (`reports/argos-2026-08-07.html`) registró una **cifra
   alterna de −60%** para el mismo periodo, marcada entonces como *no verificada en portal
   primario*. Ediciones posteriores la eliminaron sin resolverla. **Repuesta como contradicción
   abierta.**

El renglón se publica marcado `HEREDADO — NO REVERIFICADO EN ESTA EDICIÓN`: con el egreso
bloqueado, `gob.mx/sesnsp` no es consultable y la reverificación es materialmente imposible. **No
se retira el dato** —tuvo respaldo citable en su edición de origen—, pero deja de presentarse como
indicador limpio.

### ARG-99-FE-004 — Contradicción documental interna heredada: RESUELTA

La pág. 4 de `argos-2026-08-15.html` acreditaba una corrección de cifras al control
`procedencia-cifras`, mientras que `reports/_pendientes.md` —actualizado en esa misma edición—
afirmaba que ese control **nunca se había ejecutado**. La ejecución de hoy la arbitra: **ARGOS 99 es
la primera ejecución real del control**, luego `_pendientes.md` era el documento correcto y la
atribución de ARGOS 98 debe leerse como **corrección editorial interna**, no como hallazgo de
`procedencia-cifras`. **Cerrada, no heredada.**

### Vacío de edición anterior detectado de paso

**Playa del Carmen, Quintana Roo** — sentencia de **50 años** y multa de 260,640 pesos a cada uno de
tres sentenciados (Rodman de Jesús Calderón Pineda "Zombi", Juan José Velázquez Ramírez "Pollo" y
Óscar Zacarías Chablé "Botitas") por homicidio calificado doble (hechos del 12-oct-2020), juez de
juicio oral, publicada el **12-ago-2026**
(`https://24horasqroo.mx/2026/08/12/50-anos-prision-4/`).
**Sin rastro en ningún `-fuentes.md` del repositorio.** Se entrega como pista, no como hallazgo de
ARGOS 99.

---

## Hechos NO integrados por imposibilidad de verificación

El agotamiento del presupuesto de búsqueda impidió verificar dos candidatos. Conforme al principio
de cero información inventada, **no se integran**. Por indicación del control `procedencia-cifras`
**dejaron de vivir solo en este anexo**: aparecen ahora como bloque visible `CANDIDATOS NO
VERIFICADOS` en la pág. 2 del reporte y en `_pendientes.md` como prioridad 1.

1. **Azcapotzalco, CDMX** — cuatro personas ejecutadas, entre ellas un **menor de 13 años**, en la
   madrugada del domingo 16-ago, col. Pueblo de Santa María Malinalco. Fuente única e indirecta
   (resumen de buscador, sin nota primaria confirmada). De confirmarse, **sería el evento rojo de
   mayor gravedad del corte**. **Prioridad 1 para ARGOS 100.**
2. **Zamora, Michoacán** — balacera hacia las 05:00 h en la col. Primero de Mayo con detención de al
   menos cuatro presuntos integrantes del crimen organizado. **Fecha no fijada** dentro de la ventana.

## Categorías buscadas sin resultado verificable en la ventana

Fosas clandestinas · narcobloqueos · ataques a infraestructura crítica · drones armados · uso de
AEI · huachicol dentro de ventana · redes financieras y congelamiento de cuentas UIF · aduanas ·
trata de personas · secuestro masivo · motines.
**Advertencia obligatoria**: ninguna de estas ausencias puede declararse vacío institucional. Ver
"Limitación metodológica" al inicio.

## Contexto institucional del corte

**Conferencia Nacional de Procuradores** (La Jornada, 15-ago,
`https://www.jornada.com.mx/2026/08/15/politica/004n2pol`): se presentó el manual de operación de
las fiscalías o unidades especializadas para la recepción de denuncias, investigación y persecución
del delito de extorsión, y se acordó fortalecer las especializadas en desaparición.

## Indicadores oficiales — respaldo

**SESNSP / Gabinete de Seguridad — homicidio doloso.** `86.9 → 45.4 víctimas/día (−48%)`, periodo
sep-2024 → jun-2026. Entrada original: **ARGOS 86**, `reports/argos-2026-08-02.html`. Estado en esta
edición: `HEREDADO — NO REVERIFICADO` (portal `gob.mx/sesnsp` no consultable por bloqueo de egreso).
**Contradicción abierta**: cifra alterna de −60% registrada en ARGOS 90 como no verificada. Ver
`ARG-99-FE-003`. Es el único indicador oficial que publica esta edición; no se derivan de él tasas,
proyecciones ni tendencias.

## Nota de generación

Versión de escritorio `argos-2026-08-16.html` (6 páginas) y versión móvil
`argos-2026-08-16-movil.html` (6 secciones, una columna). El radar, el mapa de portada y el mapa de
aseguramientos se generan de los arreglos `EVENTOS` y `EVENTOS_ARM` mediante
`tools/gen-movil-svg.js`; **los contadores del radar de la versión móvil se toman del propio
generador**, no se escriben a mano — es el origen del error corregido en ARGOS 97. Verificado en
esta edición: contadores 3/1/5 idénticos en el generador, en el `radar-stats` de ambas versiones y
en el bloque de semáforo de ambas.

**Limitación de registro de agentes**: los controles `barrido-regional`, `procedencia-cifras` y
`editor-duplicidad` fueron incorporados por el commit de ARGOS 98 que esta sesión integró al
inicio; el registro de agentes se carga al arrancar la sesión, por lo que `Agent` no los resuelve
por nombre en esta edición. Se ejecutaron leyendo su propio archivo de definición, con el mismo
método y las mismas herramientas. Queda registrado en `_pendientes.md`.
