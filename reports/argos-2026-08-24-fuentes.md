# ARGOS 89 — Registro de fuentes (auditoría)

Corte: **22 → 24 de agosto de 2026** · Hora de consulta: 07:30 (Ciudad de México)

Este documento respalda `argos-2026-08-24.html` con los enlaces exactos consultados para cada hecho,
conforme al requisito de trazabilidad de `CLAUDE.md`. No se incluyen en el cartelón por diseño
editorial, pero deben conservarse para auditoría documental.

---

## ⚠ LIMITACIÓN CRÍTICA DE ESTE CORTE — BARRIDO DE PORTALES NO EJECUTADO

**El acceso HTTP directo estuvo bloqueado por el proxy de egreso de red de la sesión para la
totalidad de los dominios externos**, institucionales y de medios por igual. Se verificó dominio por
dominio con `curl` y con la herramienta de fetch:

| Dominio | Resultado |
|---|---|
| `www.gob.mx` (SSPC, SEDENA, SEMAR, Guardia Nacional) | `EGRESS_BLOCKED` / `CONNECT tunnel failed, 403` |
| `gabinetedeseguridad.gob.mx` | `EGRESS_BLOCKED` / `CONNECT tunnel failed, 403` |
| `fgr.org.mx` | `EGRESS_BLOCKED` / `CONNECT tunnel failed, 403` |
| `jornada.com.mx`, `eluniversal.com.mx`, `laprensa.mx`, `latinus.us`, `excelsior.com.mx`, `proceso.com.mx`, `quadratin.com.mx`, `milenio.com`, `elfinanciero.com.mx`, `lopezdoriga.com`, `tvazteca.com`, `radiorama.mx`, `lineadecontraste.com`, `suracapulco.mx`, `debate.com.mx`, `infobae.com` | `CONNECT tunnel failed, 403` (todos) |

A diferencia de ARGOS 88 —donde el problema fue bloqueo anti-bot de los propios sitios (HTTP 403 de
origen)—, aquí el bloqueo es **del entorno de red**, anterior al sitio. Se comprobó contra
`$HTTPS_PROXY/__agentproxy/status`, que reporta el proxy activo y sin fallos de relay recientes.

**Consecuencias declaradas en el cartelón, no ocultadas:**

1. El **barrido obligatorio de portales oficiales** de `CLAUDE.md` **no pudo ejecutarse**. Ninguna de
   las 32 secretarías de seguridad estatales, ninguna de las 32 fiscalías y ningún portal federal fue
   consultado directamente. Todos se registran como `PORTAL NO DISPONIBLE`.
2. El **Conteo Nacional de Armamento** (pág. 5) cubre solo lo que llegó a medios: 2 armas cortas, 1
   arma larga, 190 cartuchos. Esta cifra **no describe la realidad operativa nacional de 72 horas**.
3. El **Indicador de cobertura** de sentencias (pág. 6) declara `0 de 32` fiscalías revisadas en
   portal directo y `33 de 33` páginas no disponibles. Ninguna fiscalía se reporta como "sin
   actualización", porque ninguna fue consultada.
4. Toda la información de este corte proviene de **fragmentos de resultados de buscador**, no de
   lectura completa de artículo ni de boletín original. Ningún nivel de confianza ★★★★★ se asignó en
   este corte, porque ninguna fuente pudo verificarse documentalmente.

Restablecer el barrido es la primera tarea de método del próximo corte.

---

## Clasificación de riesgo aplicada

Conforme a la Metodología del Nivel de Riesgo Nacional ARGOS (v1.0). Seis eventos rojos, uno amarillo,
cuatro verdes. **Nivel de Riesgo Nacional: ALTO.**

- **Rojos**: ARG-89-001 (masacre familiar, Acapulco), ARG-89-002 (ataque en velorio, Colima),
  ARG-89-003 (doble ataque armado, Mazatlán), ARG-89-004 (balacera con elementos de la GN, Morelia),
  ARG-89-005 (ataque prolongado contra población civil, Los Bayados), ARG-89-006 (hallazgo en campo de
  exterminio, "El Willy").
- **Amarillo**: ARG-89-007 (balacera en el tianguis de La Lagunilla, CDMX) — incidente armado
  focalizado con un herido, sin confrontación bilateral sostenida.
- **Verdes**: ARG-89-008 (SEMAR / AEI), ARG-89-009 (aseguramiento con detenidos, Mazatlán),
  ARG-89-010 (localización de menores con Alerta Amber, Hermosillo), ARG-89-011 (captura de "Los
  Cerdos", Nopaltepec).

ARG-89-006 se clasifica en rojo porque el hallazgo de fosas y campos de exterminio es categoría
explícita de alto impacto en la metodología, aunque la localización sea acción institucional.
ARG-89-004 se clasifica en rojo por tratarse de homicidio múltiple (dos víctimas), no como "ataque a
autoridades": los elementos federales son presuntos responsables, no agredidos.
ARG-89-012, 013 y 014 no reciben semáforo (detención menor, hecho declarativo y hecho institucional,
respectivamente).

---

## ARG-89-001 — Masacre familiar con insignias de la GN (La Estación, Acapulco, Guerrero)

- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/22/comando-asesina-a-cuatro-integrantes-de-una-familia-en-acapulco-jornada-deja-mas-victimas/)
- Nacional: [unomásuno](https://unomasuno.com.mx/nacional/sujetos-con-insignias-gn-asesinaron-a-cuatro-integrantes-de-una-familia-en-acapulco/)
- Regional: [Quadratín Guerrero](https://guerrero.quadratin.com.mx/masacre-en-la-zona-rural-de-acapulco-matan-a-4-de-una-familia/)
- Regional: [Quadratín México](https://mexico.quadratin.com.mx/masacran-a-familia-en-zona-rural-de-acapulco/)
- Regional: [El Sur de Acapulco](https://suracapulco.mx/cinco-hombres-muertos-y-tres-heridos-dejan-distintos-hechos-de-violencia-en-el-municipio/)
- Regional: [Agencia IRZA](https://agenciairza.com/armados-y-con-chalecos-de-la-gn-se-meten-a-una-casa-y-ejecutan-a-4-familiares-en-acapulco/)

**Víctimas identificadas**: Esteban García Contreras (65), Gustavo García Lorenzo (35), Gonzalo
García Lorenzo (35), David de los Santos García (16).

**Discrepancia de fecha — no resuelta**: Infobae publica el hecho el 22 de agosto de 2026; Quadratín
Guerrero lo sitúa "el viernes", que corresponde al 21 de agosto (el 22 fue sábado). Ambas versiones se
conservan en el cartelón sin resolver.

**Vacío institucional**: no se localizó comunicado de la Fiscalía General del Estado de Guerrero ni
pronunciamiento de la Guardia Nacional sobre el uso de sus insignias por el comando. Marcado como
`Pendiente de corroboración institucional`.

## ARG-89-002 — Ataque armado durante velorio (col. Francisco I. Madero, Colima)

- Nacional: [El Heraldo de México](https://heraldodemexico.com.mx/nacional/2026/8/23/matan-dos-hombres-afuera-de-un-velorio-en-colima-agresores-escapan-875066.html)
- Nacional: [Excélsior](https://www.excelsior.com.mx/nacional/balacera-velorio-deja-dos-muertos-era-hermano-difunta)
- Nacional: [TV Azteca](https://www.tvazteca.com/aztecanoticias/en-colima-ataque-en-velorio-mujer-en-la-francisco-i-madero-deja-dos-muertos/)
- Regional: [AFmedios](https://www.afmedios.com/ataque-armado-deja-una-mujer-sin-vida-y-otra-lesionada-en-la-colonia-francisco-i-madero-de-colima/) (primer ataque, 21 de agosto)

**Secuencia documentada**: viernes 21 de agosto, ataque armado en la col. Francisco I. Madero deja
muerta a Alondra "R" (32) y una mujer herida. Domingo 23 de agosto, durante su velorio, hombres
armados disparan contra los asistentes y matan a su hermano y a otro varón.

**No verificado**: los antecedentes penales atribuidos a los hermanos provienen de los reportes
periodísticos, no de una ficha oficial. Se consignan sin validar. Sin boletín de la FGE Colima.

## ARG-89-003 — Doble ataque armado (Mazatlán, Sinaloa)

- Nacional: [La Jornada](https://www.jornada.com.mx/noticia/2026/08/23/estados/ataques-armados-en-mazatlan-sinaloa-dejan-dos-personas-muertas)
- Nacional: [TV Azteca](https://www.tvazteca.com/aztecanoticias/mazatlan-ataque-armado-deja-cinco-heridos-en-sinaloa/)
- Nacional: [Zócalo](https://www.zocalo.com.mx/ataques-armados-en-mazatlan-sinaloa-dejan-dos-personas-muertas)
- Regional: [N+](https://www.nmas.com.mx/seguridad/balaceras/enfrentamientos-armados-sinaloa-dejan-muertos-heridos/)
- Regional: [Viva la Noticia](https://vivalanoticia.mx/8-heridos-de-bala-y-un-muerto-en-dos-atentados-en-mazatlan/)
- Contexto: [Infobae — enfrentamientos en La Cofradía](https://www.infobae.com/mexico/2026/08/23/enfrentamientos-con-explosivos-y-armas-mantienen-en-alerta-a-habitantes-de-la-cofradia-mazatlan/)
- Contexto (julio 2026): [Infobae — 900 elementos a Mazatlán](https://www.infobae.com/mexico/2026/07/23/anuncian-arribo-de-900-elementos-de-seguridad-a-mazatlan-tras-ataques-armados/)

**Nota de cifras**: Viva la Noticia titula "8 heridos de bala y un muerto en dos atentados"; La
Jornada y Zócalo consignan dos muertos y cinco heridos en el primer ataque más tres personas atacadas
en el segundo. El cartelón usa la versión de La Jornada/Zócalo (dos muertos, cinco heridos, un
detenido) por ser la coincidente entre dos fuentes nacionales; **la variante de Viva la Noticia se
documenta aquí y no se integra**.

## ARG-89-004 — Balacera con elementos de la Guardia Nacional (col. Del Periodista, Morelia, Michoacán)

- Regional: [Grupo Marmor](https://grupomarmor.com.mx/2026/08/22/homicidio-en-la-colonia-periodistas-termino-con-dos-detenidos-presuntos-elementos-de-la-gn-seguridad-municipal/)
- Regional: [A Tiempo](https://atiempo.mx/destacadas/identifican-guardia-nacional-balacera-colonia-periodista-morelia/)
- Regional: [RED Michoacán](https://www.redmichoacan.com/2026/08/22/identifican-a-los-dos-hombres-asesinados-durante-balacera-en-morelia-uno-era-agente-de-la-gn/)
- Regional: [Media News — dos muertos y dos asegurados](https://medianews.mx/index.php/2026/08/22/dos-muertos-y-dos-sujetos-asegurados-tras-balacera-en-la-colonia-del-periodista-en-morelia/)
- Regional: [Media News — seguimiento previo a la balacera](https://medianews.mx/index.php/2026/08/22/jose-luis-y-un-amigo-eran-seguidos-por-agentes-de-la-gn-antes-de-la-balacera-en-la-colonia-del-periodista/)
- Regional: [RED113](http://www.red113mx.com/2026/08/identifican-los-dos-hombres-asesinados.html)
- Regional: [Exeni](https://exeni.com.mx/identifican-a-los-dos-hombres-asesinados-durante-balacera-en-morelia-uno-era-agente-de-la-gn/)
- Regional: [Changoonga](https://changoonga.com/2026/08/23/morelia-elementos-de-gn-arman-balacera-matan-a-chavito-y-a-su-propio-companero/)

**Fallecidos**: Juan Omar Mireles Tovar (elemento de la GN, vestido de civil) y José Luis (20 años,
civil). **Asegurados por la Policía Municipal de Morelia**: Juan Carlos Dorantes Rebolledo (40) y
Rubén Isaí Landeros García (22), presuntos elementos de la GN. En el vehículo (Nissan Versa verde,
placas de la CDMX) se hallaron armas de fuego y chalecos tácticos con insignias de la GN, sin cifra.

**NO integrado como hecho**: la versión sobre un presunto estado de ebriedad de los tres elementos se
atribuye a "fuentes cercanas al caso" y no está confirmada por autoridad alguna. **Sin comunicado de
la Guardia Nacional, de la FGE Michoacán ni de la FGR.**

## ARG-89-005 — Ataque prolongado contra Los Bayados (Ajuchitlán del Progreso, Guerrero)

- Nacional: [El Financiero](https://www.elfinanciero.com.mx/estados/2026/08/23/ataque-armado-en-los-bayados-guerrero-revive-temores-de-desplazamiento-forzado-exigen-base-de-la-sedena/)
- Regional: [Quadratín Guerrero — despliegue](https://guerrero.quadratin.com.mx/despliegan-a-fuerzas-de-seguridad-tras-reporte-de-ataques-en-ajuchitlan/)
- Regional: [Quadratín Guerrero — vigilancia del Ejército](https://guerrero.quadratin.com.mx/vigila-el-ejercito-comunidades-de-ajuchitlan/)
- Regional: [La Plaza Diario de Acapulco — denuncia de drones](https://www.laplazadiario.com.mx/denuncian-ataques-armados-y-con-drones-contra-los-bayados-en-ajuchitlan/)
- Regional: [La Plaza Diario de Acapulco — refuerzo militar](https://www.laplazadiario.com.mx/se-suma-mas-personal-del-ejercito-al-operativo-en-los-bayados-tras-reporte-de-ataques/)
- Regional: [Trazos Noticias](https://www.trazosnoticias.com.mx/municipios/refuerzan-acciones-interinstitucionales-de-seguridad-en-los-bayados-ajuchitlan-del-progreso/)
- Regional: [MegaVisión](https://megavision.tv/defensa-y-guardia-nacional-refuerzan-seguridad-en-los-bayados-tras-reportes-de-ataques-armados/)

**NO integrado a ningún conteo**: la denuncia de ataques con drones proviene de habitantes de la
comunidad, sin confirmación institucional ni aseguramiento de aeronave. Registrada como
`ARG-89-ARM-Q02 — NO OFICIAL, PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL`. El rubro "drones armados" del
conteo nacional queda por tanto en 0.

**Antecedente verificable**: alrededor de 50 familias abandonaron Los Bayados por violencia en febrero
de 2023.

## ARG-89-006 — Campo de exterminio "El Willy" (Casas Grandes, Chihuahua)

- Nacional: [La Jornada — nueve segmentos óseos](https://www.jornada.com.mx/2026/08/22/estados/022n4est)
- Nacional: [El Universal — osamentas y restos óseos, traslado a SEMEFO](https://www.eluniversal.com.mx/estados/hallan-osamentas-y-restos-oseos-en-la-localidad-de-el-willy-en-casas-grandes-chihuahua-son-trasladados-al-semefo-para-practicas-periciales/)
- Nacional: [Infobae — "cerca de 100 cadáveres"](https://www.infobae.com/mexico/2026/08/22/hallan-mas-restos-oseos-en-el-campo-de-exterminio-el-willy-en-chihuahua-donde-opera-la-linea-ya-serian-cerca-de-100-cadaveres/)
- Nacional: [El Universal — 56 cadáveres, rastreo concluido](https://www.eluniversal.com.mx/estados/exhuman-un-total-de-56-cadaveres-en-predio-el-willy-en-chihuahua-concluyen-trabajos-de-rastreo/)
- Nacional: [Univisión — 76 cuerpos](https://www.univision.com/noticias/narcotrafico/campo-de-exterminio-desenterrados-76-cuerpos)
- Regional: [El Diario de Chihuahua](https://eldiariodechihuahua.mx/estado/2026/aug/22/descubren-mas-osamentas-en-el-willy-casas-grandes-830223.html)
- Regional: [Diario MX](https://diario.mx/estado/2026/aug/21/hallan-mas-osamentas-en-excavaciones-de-el-willy-casas-grandes-1134450.html)
- Regional: [Juárez Noticias](https://juareznoticias.com/localizan-osamentas-y-restos-oseos-en-el-willy/)
- Regional: [El Bordo](https://elbordo.com.mx/local/localizan-osamentas-y-restos-oseos-en-el-willy-20260821-119939.html)
- Regional: [La Parada Digital](https://laparadadigital.com/hallan-mas-osamentas-en-el-willy/)

**DISCREPANCIA DE CIFRA ACUMULADA — NO RESUELTA, NO INTEGRADA A NINGÚN TOTAL ARGOS**: 56 (El
Universal, con rastreo declarado concluido) · 76 (Univisión) · ~80 (registro previo) · ~91 (recuentos
en coberturas) · "cerca de 100" (Infobae). Marcado en el cartelón como
`CIFRA ACUMULADA EN CONFLICTO — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN DE UNA FUENTE OFICIAL ÚNICA`.

**Antecedente verificable citado**: entre el 15 de enero y el 6 de marzo de 2025, la Comisión Local de
Búsqueda y la Fiscalía de Chihuahua localizaron 78 restos humanos en 63 fosas clandestinas; 46 fueron
identificados como personas desaparecidas de la región de Casas Grandes.

**Atribución**: el señalamiento a "La Línea" (brazo armado del Cártel de Juárez) es línea de
investigación de la autoridad basada en el modo de desmembramiento, **no hecho probado**. Se consigna
como tal.

## ARG-89-007 / ARG-89-ARM-003 — Balacera en el tianguis de La Lagunilla (Cuauhtémoc, CDMX)

- Nacional: [El Heraldo de México](https://heraldodemexico.com.mx/nacional/2026/8/23/captan-balacera-en-pleno-tianguis-de-la-lagunilla-hay-un-herido-detenidos-video-874705.html)
- Institucional (reproducido): [NotiMx — comunicado de la SSC CDMX](https://www.notimx.mx/2026/08/en-la-alcaldia-cuauhtemoc-efectivos-de-la-ssc-detuvieron-a-seis-jovenes-en-posesion-de-aparente-droga-posiblemente-relacionados-en-una-agresion-con-disparos-de-arma-de-fuego.html)
- Nacional: [Infobae — minuto a minuto del 23 de agosto](https://www.infobae.com/mexico/2026/08/23/en-vivo-seguridad-crimen-y-narcotrafico-en-mexico-hoy-23-de-agosto-rocha-moya-vuelve-a-pedir-licencia-a-la-gubernatura-de-sinaloa/)

**Desglose**: agresión con golpes y disparos en las colonias Morelos y Centro Histórico; un herido;
seis detenidos, dos de ellos menores de edad; un arma de fuego corta y 50 bolsitas con aparente
marihuana aseguradas. Todos puestos a disposición del Ministerio Público. **Cartuchos y cargadores no
publicados** — se consignan como `No publicado` en la tabla de armamento, no como cero.

## ARG-89-008 / ARG-89-ARM-002 — SEMAR destruye tres AEI y un vehículo blindado (Sinaloa)

- Institucional / Nacional: [El Universal](https://www.eluniversal.com.mx/nacion/marina-localiza-un-vehiculo-y-explosivos-improvisados-en-sinaloa-artefactos-fueron-destruidos/)
- Nacional: [López-Dóriga](https://lopezdoriga.com/nacional/marina-asegura-vehiculo-blindado-y-explosivos-improvisados-sinaloa/)
- Nacional: [unomásuno](https://unomasuno.com.mx/nacional/marina-destruye-explosivos-y-neutraliza-vehiculo-blindado-en-sinaloa/)
- Regional: [AFmedios](https://www.afmedios.com/marina-localiza-vehiculo-con-blindaje-artesanal-y-explosivos-improvisados-en-sinaloa/)
- Regional: [California Medios](https://californiamedios.com/marina-destruye-explosivos-y-neutraliza-vehiculo-blindado-en-dos-operativos-distintos-en-sinaloa/)
- Regional: [Ruta 135](https://ruta135.com/c-5/marina-localiza-vehiculo-blindado-y-explosivos-en-sinaloa/)
- Regional: [El Diario de Chihuahua](https://eldiariodechihuahua.mx/nacional/2026/aug/23/destruye-marina-artefactos-explosivos-en-sinaloa-830329.html)
- Regional: [Miguel Ángel Luna](https://miguelangelluna.mx/2026/08/23/localizan-vehiculo-blindado-y-explosivos-improvisados-en-sinaloa)

**Fuente primaria**: comunicado de la Cuarta Región Naval del 23 de agosto de 2026 (citado por todos
los medios; **el portal de la SEMAR no pudo consultarse directamente**).

**Desglose**: operativo 1 — La Mora Escarbada, sindicatura de El Quelite: un vehículo sin placas con
blindaje artesanal y dos AEI. Operativo 2 — patrullaje terrestre en inmediaciones de Mazatlán y
Concordia: un AEI. Los tres artefactos fueron destruidos en el sitio. Sin detenidos.

## ARG-89-009 / ARG-89-ARM-001 — Aseguramiento con detenidos (La Noria-Palo Blanco, Mazatlán, Sinaloa)

- Nacional: [Latinus](https://latinus.us/mexico/2026/8/23/detienen-dos-hombres-en-sinaloa-les-incautan-armas-200-dosis-de-drogas-combustible-182359.html)
- Regional: [Noroeste](https://www.noroeste.com.mx/seguridad/detienen-en-mazatlan-a-dos-hombres-armados-y-decomisan-drogas-y-gasolina-BE25122366)
- Regional: [Ríodoce](https://riodoce.mx/2026/08/23/en-la-zona-rural-de-mazatlan-detienen-a-dos-hombres-les-aseguran-armas-droga-y-gasolina/)
- Regional: [Marcrix Noticias](https://www.marcrixnoticias.com.mx/detienen-a-dos-hombres-con-armas-droga-y-200-litros-de-gasolina-en-mazatlan/)
- Regional: [Viva la Noticia](https://vivalanoticia.mx/en-mazatlan-grupo-interinstitucional-detiene-a-dos-civiles-asegura-armas-droga-municiones-y-200-litros-de-gasolina/)
- Regional: [Puntualizando](https://www.puntualizando.com/en-mazatlan-autoridades-detienen-a-dos-civiles-aseguran-armas-droga-municiones-y-combustible/)

**Fuente primaria**: comunicado de la Secretaría de Seguridad Pública de Sinaloa del 23 de agosto de
2026 (**portal no consultable directamente**).

**Desglose publicado por la autoridad, base del conteo nacional de armamento del corte**: 1 fusil
AK-47 calibre 7.62×39 mm · 1 pistola calibre 9 mm · 6 cargadores para arma larga · 1 cargador para
arma corta · 180 cartuchos 7.62×39 mm · 10 cartuchos 9 mm · 200 dosis de presunto cristal (~50 g) ·
200 litros de gasolina en cuatro bidones de 50 L · 1 camioneta Ford Ranger 1999 sin reporte de robo ·
2 detenidos, puestos a disposición de la FGR en Mazatlán.

**Criterio aplicado**: los 200 L de gasolina **no** se clasifican como huachicol — la autoridad no lo
hizo. Las 200 dosis de cristal y el combustible no son línea de armamento y no se integran al conteo
de la sección 1.

## ARG-89-010 — Localización de menores con Alerta Amber (Hermosillo, Sonora)

- Nacional: [Latinus](https://latinus.us/mexico/2026/8/23/rescatan-dos-menores-con-alerta-amber-en-sonora-aseguran-droga-detienen-dos-sujetos-182372.html)
- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/23/encuentran-a-dos-menores-con-alerta-amber-durante-un-cateo-en-hermosillo-hay-dos-detenidos-incluido-el-padre/)
- Regional: [Expreso](https://www.expreso.com.mx/noticias/seguridad/cateo-en-hermosillo-logra-rescate-de-hermanos-sustraidos/263001)
- Regional: [Radar Sonora](https://www.radarsonora.com/cateo-permite-detener-a-dos-personas-y-localizar-a-dos-menores-con-alerta-amber/)
- Regional: [Nuestras Noticias Sonora](https://nuestrasnoticiassonora.com/relevante/cateo-en-hermosillo-permite-rescatar-a-dos-dos-menores-que-tenian-alerta-amber-desde-febrero/)
- Regional: [Medios OBSON](https://mediosobson.com/2026/08/23/det1enen-a-dos-hombres-y-localizan-a-dos-m3nores-con-alerta-amber-en-hermosillo/)
- Regional: [Dossier Político](https://dossierpolitico.com/2026/08/23/rescatan-a-dos-menores-con-alerta-amber-en-sonora-aseguran-droga-y-detienen-a-dos-sujetos/)
- Antecedente (abril 2026): [El Imparcial — activación de la Alerta Amber](https://www.elimparcial.com/son/sonora/2026/04/26/se-activa-alerta-amber-en-sonora-por-la-sustraccion-de-dos-menores-en-agua-prieta/)

**Desglose**: cateo en la colonia Los Pueblitos, Hermosillo, por cinco corporaciones. Localizados dos
hermanos de 8 y 9 años, sustraídos por su padre el 23 de febrero de 2026 en Agua Prieta. Dos
detenidos, uno de ellos Víctor Antonio "N" (34), padre de los menores, con orden de aprehensión
vigente por sustracción de menores. Asegurados 14 paquetes/envoltorios de presunto cristal. Los
menores fueron trasladados a instalaciones de la AMIC y puestos a disposición de la Procuraduría de
Protección de Niñas, Niños y Adolescentes del Estado de Sonora.

**Criterio aplicado**: al no haber aseguramiento de armamento, esta detención **no** entra al conteo
de detenidos de la sección 1; se consigna en "Detenciones relevantes" (pág. 2).

## ARG-89-011 — Captura de seis integrantes de "Los Cerdos" (Nopaltepec, Estado de México)

- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/24/capturan-a-seis-de-los-cerdos-en-edomex-hay-un-expolicia-entre-los-detenidos/)

**Desglose**: agentes de la Fiscalía Especializada en Combate al Robo de Vehículos ejecutaron una
orden de cateo en Nopaltepec y capturaron a cuatro personas más, entre ellas Diego Vladimir
(expolicía municipal de Nopaltepec) y Óscar Juan, alias "El Cerdo", identificado como líder de la
organización; seis detenidos en total.

**Nota de confianza**: **fuente única nacional**, sin corroboración independiente localizada dentro
del corte. Marcado ★★★☆☆ en el cartelón conforme a la escala de `CLAUDE.md`.

## ARG-89-012 — Detención por intento de robo a casa habitación (Tláhuac, CDMX)

- Nacional: [Infobae — minuto a minuto del 23 de agosto](https://www.infobae.com/mexico/2026/08/23/en-vivo-seguridad-crimen-y-narcotrafico-en-mexico-hoy-23-de-agosto-rocha-moya-vuelve-a-pedir-licencia-a-la-gubernatura-de-sinaloa/)

Cuatro personas detenidas tras intentar robar el domicilio de una mujer de 74 años; herramienta de
forzamiento asegurada. Sin ficha de cuatro apartados: no corresponde a las categorías de crimen
organizado del cartelón. Se consigna únicamente en la tabla de detenciones relevantes.

## ARG-89-013 — Presión declarativa de EE. UU. sobre protección política al CJNG

- Nacional: [El Financiero — DEA "revive" la amenaza (24 ago.)](https://www.elfinanciero.com.mx/mundo/2026/08/24/dea-revive-la-amenaza-de-ir-por-politicos-mexicanos-con-presuntos-nexos-con-el-cjng/)
- Nacional: [Infobae — minuto a minuto del 23 de agosto](https://www.infobae.com/mexico/2026/08/23/en-vivo-seguridad-crimen-y-narcotrafico-en-mexico-hoy-23-de-agosto-rocha-moya-vuelve-a-pedir-licencia-a-la-gubernatura-de-sinaloa/)
- Institucional / Nacional: [Político.mx — Harfuch descarta agentes de EUA en operativos](https://politico.mx/2026/08/23/harfuch-descarta-presencia-de-agentes-de-eua-en-operativos-dentro-de-mexico/)
- Institucional / Nacional: [La Jornada — "Nuestra ley no permite que haya fuerzas extranjeras"](https://www.jornada.com.mx/noticia/2026/08/23/politica/nuestra-ley-no-permite-que-haya-fuerzas-extranjeras-en-nuestro-pais-harfuch)
- Antecedente (23 jul. 2026): [El Imparcial — OFAC sanciona a 55 personas y empresas](https://www.elimparcial.com/mundo/2026/07/23/eeuu-sanciona-a-55-personas-y-empresas-vinculadas-al-cjng-e-identifica-a-juan-carlos-gonzalez-alias-pelon-como-presunto-nuevo-lider-tras-la-muerte-de-el-mencho/)
- Antecedente: [Proceso — perfil de "El Pelón"](https://www.proceso.com.mx/nacional/2026/8/6/quien-es-juan-carlos-valencia-el-pelon-por-quien-eeuu-ofrece-una-recompensa-de-hasta-470-millones-de-377549.html)

**DISCREPANCIA DE IDENTIDAD — NO RESUELTA**: El Imparcial identifica al presunto nuevo líder del CJNG
como "Juan Carlos **González**, alias 'Pelón'"; Proceso, como "Juan Carlos **Valencia**, 'El Pelón'".
Marcado en el cartelón como `NOMBRE EN CONFLICTO — NO UTILIZAR COMO DATO DE IDENTIFICACIÓN`.

**Registro explícito**: al cierre del corte, EE. UU. no ha nombrado públicamente a ningún funcionario
mexicano bajo la acusación de protección al CJNG, no ha presentado cargos formales ni evidencia. Se
clasifica como hecho declarativo, no como acto de autoridad.

## ARG-89-014 — Licencia indefinida del gobernador de Sinaloa

- Nacional: [Infobae — Congreso aprueba por unanimidad](https://www.infobae.com/mexico/2026/08/23/congreso-de-sinaloa-aprueba-por-unanimidad-la-licencia-indefinida-de-rocha-moya-como-gobernador/)
- Nacional: [El Financiero](https://www.elfinanciero.com.mx/estados/2026/08/23/ruben-rocha-moya-obtiene-licencia-para-dejar-gobierno-de-sinaloa-congreso-ratifica-peticion-y-llama-a-periodo-de-sesiones/)
- Nacional: [El Heraldo de México](https://heraldodemexico.com.mx/nacional/2026/8/23/congreso-de-sinaloa-aprueba-la-solicitud-de-licencia-indefinida-de-ruben-rocha-moya-como-gobernador-874643.html)
- Nacional: [El Informador](https://www.informador.mx/mexico/congreso-de-sinaloa-aprueba-licencia-indefinida-de-ruben-rocha-moya-como-gobernador-20260823-0068.html)
- Nacional: [El Imparcial — 34 horas tras su regreso](https://www.elimparcial.com/mexico/2026/08/23/congreso-aprueba-nueva-licencia-de-rocha-moya-y-sheinbaum-la-respalda-es-lo-mejor-para-sinaloa/)
- Nacional: [SDPnoticias](https://www.sdpnoticias.com/estados/congreso-de-sinaloa-autoriza-nueva-licencia-indefinida-de-ruben-rocha-moya/)
- Nacional: [24 Horas](https://24-horas.mx/estados/concede-congreso-de-sinaloa-nueva-licencia-a-rocha-moya/)

**Cronología**: regreso al cargo el viernes 21 de agosto → solicitud de nueva licencia el 22 de agosto
→ aprobación unánime el 23 de agosto → periodo extraordinario convocado para el lunes 24 de agosto a
las 11:00 h para designar y tomar protesta al gobernador interino.

---

## SECCIÓN 1 — CONTEO NACIONAL DE ARMAMENTO

### Total del corte (solo cantidades expresamente publicadas)

| Rubro | Total |
|---|---|
| Armas cortas | 2 |
| Armas largas | 1 |
| Cartuchos | 190 |
| Cargadores | 7 |
| Granadas | 0 |
| AEI | 3 |
| Explosivos / componentes | Cantidad no determinada |
| Drones armados | 0 |
| Armamento especial | 1 (vehículo con blindaje artesanal) |
| Personas detenidas (en eventos con aseguramiento) | 8 |
| Estados con aseguramientos | 2 (Sinaloa, Ciudad de México) |
| Eventos contabilizados | 3 |
| Eventos cualitativos sin cantidad | 2 |

**Deduplicación**: ningún evento de este corte fue publicado por dos corporaciones distintas; no
aplicaron cruces de duplicidad.

### Evento anterior publicado durante el corte — NO INTEGRADO

**Sinaloa — Concordia, Culiacán y Mazatlán** (hechos del 18-19 de agosto, difundidos el 21-22).

- Nacional: [El Universal — **72** artefactos explosivos](https://www.eluniversal.com.mx/nacion/inhabilitan-laboratorio-clandestino-con-72-explosivos-en-sinaloa-hallan-mas-de-2-mil-litros-de-sustancias-para-hacer-droga/)
- Nacional: [El Heraldo de México — **172** artefactos explosivos](https://heraldodemexico.com.mx/nacional/2026/8/21/autoridades-federales-aseguran-172-artefactos-explosivos-improvisados-inhabilitan-laboratorio-de-droga-sintetica-en-sinaloa-873513.html)
- Nacional: [La Jornada — 8 mil cartuchos y **172** artefactos](https://www.jornada.com.mx/2026/08/22/politica/007n2pol)
- Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/21/fuerzas-federales-decomisan-arsenal-y-desmantelan-laboratorio-clandestino-en-sinaloa/)
- Nacional: [unomásuno](https://unomasuno.com.mx/nacional/fuerzas-federales-decomisan-arsenal-y-desmantelan-laboratorio-clandestino-en-sinaloa/)
- Regional: [Marcrix — "172 explosivos y un arsenal"](https://www.marcrixnoticias.com.mx/operativos-en-sinaloa-dejan-172-explosivos-y-un-arsenal/)
- Regional: [Ruta 135](https://ruta135.com/c-5/aseguran-172-explosivos-arsenal-y-desmantelan-laboratorio-clandestino-en-sinaloa/)

Desglose coincidente entre ambas versiones: 2,450 L de sustancias químicas · 98 cargadores · 8,095
cartuchos de diversos calibres · 1 fusil Barrett calibre .50 · 6 armas largas · equipo táctico
diverso · sin detenidos.

`CIFRA EN CONFLICTO (72 vs. 172 AEI) Y HECHO ANTERIOR AL PERIODO — NO INTEGRAR AL TOTAL NACIONAL HASTA
VALIDACIÓN CONTRA EL BOLETÍN ORIGINAL.` Dado que el resto del desglose es idéntico en ambas
coberturas, lo más probable es un error de transcripción sobre un mismo boletín y no dos eventos
distintos — hipótesis que **no se afirma** sin acceso al documento fuente.

### Serie previa de AEI en Sinaloa (contexto, fuera del corte)

- [Mexico News Daily — 303 AEI y ~300 kg de explosivos en El Rosario (18 ago.)](https://mexiconewsdaily.com/news/navy-ieds-explosives-bust-sinaloa/)
- [El Heraldo de México](https://heraldodemexico.com.mx/nacional/2026/8/18/encuentran-mas-de-300-artefactos-explosivos-improvisados-300-kilos-de-explosivos-en-el-rosario-sinaloa-871438.html)
- [La Opinión](https://laopinion.com/2026/08/18/autoridades-en-mexico-aseguran-mas-de-300-artefactos-explosivos-y-300-kilos-de-explosivos-en-sinaloa/)

No se integra al corte (hecho del 18 de agosto). Se conserva para la lectura de serie de la
Explotación ARGOS del módulo de armamento.

---

## SECCIÓN 2 — RASTREO NACIONAL DE SENTENCIAS

### ARG-89-SEN-001 — FGJE Sonora, homicidio en Hermosillo

- Institucional / Regional: [El Imparcial](https://www.elimparcial.com/son/hermosillo/2026/08/22/dos-sujetos-reciben-condena-de-28-anos-por-homicidio-en-hermosillo-tras-investigacion-de-la-fiscalia-de-sonora/)

León Felipe "N" y Francisco Antonio "N". Hecho: julio de 2024, fraccionamiento Acacia Residencial,
Hermosillo (homicidio de un hombre y lesiones a una mujer). Juicio oral iniciado el 11 de agosto de
2026; fallo condenatorio el 19 de agosto; individualización de la pena el 20 de agosto; difusión el 22
de agosto. Pena: 28 años y 3 días.

`Pena compuesta — requiere revisión jurídica`: la fuente no precisa si los 28 años y 3 días son la
pena impuesta a cada sentenciado o una cifra conjunta. **No se suma al acumulado nacional.** Aplicar
la lectura "28 años por persona" habría inflado el total del corte en 56 años sobre una interpretación
no verificada.

### ARG-89-SEN-002 — FGE Guanajuato, feminicidio en León

- Institucional / Nacional: [Infobae](https://www.infobae.com/mexico/2026/08/22/sentencian-a-hombre-por-feminicidio-en-leon-guanajuato-entre-desafios-de-registro-y-justicia-en-la-entidad/)

Christian Gustavo "N", 27 años 11 meses de prisión por el feminicidio de su madre, Melesia Rodríguez
(51), hecho del 22 de enero de 2026 en la colonia El Carmen CTM, León. Difusión: 22 de agosto de 2026.
Atribución a una sola persona inequívoca: **es la única pena sumable del corte.**

### Conteo nacional del módulo judicial

| Rubro | Valor |
|---|---|
| Sentencias condenatorias | 2 |
| Sentencias absolutorias | 0 |
| Procedimientos abreviados con sentencia | 0 localizados |
| Juicio oral con sentencia | 1 |
| Sentencias firmes | 0 (ninguna declarada firme) |
| Sentencias de primera instancia | 2 |
| Personas sentenciadas | 3 |
| Años de prisión acumulados sumables | 27 años 11 meses |
| Multas acumuladas | No informadas |
| Reparación del daño ordenada | No informada |
| Fiscalías con resultados reportados | 2 (Sonora, Guanajuato) |
| Delitos con sentencia | Homicidio (1) · Feminicidio (1) |

### Resoluciones localizadas pero NO integradas

1. **Chihuahua** — 25 años por desaparición forzada y secuestro agravado contra Jocelyne Milagros
   V. C., **19 de agosto de 2026**: anterior al periodo.
   ([El Bordo](https://elbordo.com.mx/local/le-dan-25-anos-por-secuestro-20260819-119734.html))
2. **Estado de México** — 90 años por secuestro (**20 de agosto**,
   [Infobae](https://www.infobae.com/mexico/2026/08/20/condenan-a-90-anos-de-carcel-a-una-madre-que-secuestro-a-su-hija-para-internarla-en-un-centro-de-rehabilitacion-en-el-edomex/));
   sentencias de 36 años por homicidio calificado en Tecámac
   ([NotiMx](https://www.notimx.mx/2026/08/consigue-fiscalia-edomex-36-anos-de.html),
   [Quadratín Edomex](https://edomex.quadratin.com.mx/condenan-a-36-anos-a-homicida-que-intento-ocultar-su-crimen-en-edomex/))
   y de 55 años por homicidio calificado y tentativa
   ([NotiMx](https://www.notimx.mx/2026/08/fiscalia-edomex-obtiene-sentencia-de-55.html)):
   **sin fecha exacta verificable dentro del periodo de corte**.
3. **FGR Tlaxcala** — 2 años 6 meses por portación de arma de fuego, **18 de agosto**: anterior al
   periodo.
   ([Línea de Contraste](https://www.lineadecontraste.com/logra-fgr-sentencia-5/))
4. **Ciudad de México** — 125 años por persona por el secuestro exprés de un adulto mayor en
   Xochimilco: **descartado por fecha**. La búsqueda inicial lo situaba en agosto de 2026, pero la
   verificación lo ubica en **junio de 2026**.
   ([La Silla Rota](https://lasillarota.com/metropoli/2026/6/19/dan-125-anos-de-prision-giovanni-n-tomas-n-por-secuestro-expres-agravado-en-xochimilco-604666.html))

### Indicador de cobertura (declarado, no estimado)

| Rubro | Valor |
|---|---|
| Fiscalías revisadas en portal directo | **0 de 32** — `PORTAL NO DISPONIBLE` |
| FGR revisada | **No** — `fgr.org.mx` inaccesible |
| Fiscalías con sentencia localizada (vía buscador) | 2 |
| Fiscalías sin actualización | **No determinado** — 30 no consultadas |
| Páginas no disponibles | **33 de 33** (FGR + 32 fiscalías) |
| Fuentes con error de acceso | Todos los dominios vía HTTP directo |

Ninguna fiscalía se reporta como "sin actualización": ninguna fue efectivamente consultada.

---

## Categorías sin hecho operativo verificable en el corte

- **Huachicol** — `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`. Eventos localizados fuera del periodo:
  Huehuetoca, Edomex, 5 detenidos (2 ago.); El Arenal, +45,000 L (14 ago.); El Peñol, Chihuahua,
  ~8,000 L (18 ago.). Los 200 L de gasolina de ARG-89-009 **no** fueron clasificados como huachicol
  por la autoridad y no se reclasifican.
- **Narcotráfico marítimo** — `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`. Aseguramientos de la SEMAR
  en el Pacífico localizados: 1.17 t y 6 detenidos (7-8 ago.); 1.9 t y 2 detenidos frente a Guerrero
  (15-16 ago.). Todos anteriores al periodo.
- **Extorsión** — `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`. Vinculaciones a proceso localizadas
  (Guanajuato, CDMX/Fuerza Anti-Unión, Michoacán/Caballeros Templarios, Edomex/exfuncionarios
  ambientales) corresponden al 17-21 de agosto y **no son sentencias**.
- **Redes financieras** — solo hecho declarativo (ARG-89-013); sin acto de autoridad en el corte.
- **Ataques directos contra autoridades** — `SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE`. Los dos
  hechos que involucran a la Guardia Nacional (ARG-89-001 y ARG-89-004) son usurpación de identidad y
  participación de elementos fuera de servicio, respectivamente: **no se contabilizan como agresiones
  contra la corporación.**

## Contexto no oficial registrado (no alimenta indicadores)

Informe *"Trazar la ausencia, caminar la esperanza: análisis de los hallazgos de fosas clandestinas en
México (2006-2024)"*, Programa de Derechos Humanos de la Universidad Iberoamericana. Difundido durante
el corte.

- [Los Angeles Press (23 ago.)](https://losangelespress.org/investigaciones/2026/aug/23/guerrero-encabeza-hallazgos-de-fosas-clandestinas-en-mexico-desde-2006-16026.html)
- [Infobae (23 ago.)](https://www.infobae.com/mexico/2026/08/23/guerrero-encabeza-la-lista-de-estados-con-mas-hallazgos-de-fosas-clandestinas-en-los-ultimos-18-anos/)
- [La Jornada (20 ago.) — "más de 5 mil fosas"](https://www.jornada.com.mx/noticia/2026/08/20/sociedad/mexico-registra-mas-de-5-mil-fosas-clandestinas-en-18-anos-revela-informe-de-la-ibero)
- [Infobae (21 ago.) — "casi 3 mil fosas"](https://www.infobae.com/mexico/2026/08/21/mexico-acumulo-casi-3-mil-fosas-clandestinas-en-18-anos-mil-764-fueron-halladas-con-amlo/)

Cifras por entidad, coincidentes entre coberturas y reproducidas en el cartelón: Guerrero 416
(Acapulco primer municipio con 189), Veracruz 400, Sonora 381, Guanajuato 294, Jalisco 263.
**El total nacional del informe NO se reproduce**: La Jornada consigna "más de 5 mil" e Infobae "casi
3 mil"; `DISCREPANCIA NO RESUELTA`. Fuente académica, no oficial: no alimenta ningún indicador ARGOS.

## Indicadores oficiales — última publicación disponible

- SESNSP, presentado por Marcela Figueroa Franco el **11 de agosto de 2026** (sin actualización
  durante este corte): julio de 2026, 42.5 homicidios dolosos diarios, nivel más bajo desde 2015;
  caída de 51% desde septiembre de 2024 (86.9 → 42.5); promedio enero-julio de 2026, 48.6 diarios,
  cifra más baja para ese periodo desde 2016; 30 de 32 entidades con reducción; siete entidades
  concentran el 49% del total: Guanajuato 8.6%, Baja California 8.2%, Chihuahua 8.1%, Sinaloa 7.1%,
  Estado de México 6%, Guerrero 5.6%, Morelos 5.5%.
  - [El Imparcial](https://www.elimparcial.com/mexico/2026/08/11/homicidios-dolosos-bajan-51-durante-gobierno-de-sheinbaum-julio-registra-el-nivel-mas-bajo-desde-2015/)
  - [Contralínea](https://contralinea.com.mx/interno/semana/homicidios-dolosos-bajan-51-desde-septiembre-de-2024-sesnsp/)
  - [Ríodoce — Sinaloa −52%](https://riodoce.mx/2026/08/11/destaca-sesnsp-reduccion-del-52-en-homicidios-dolosos-en-sinaloa-durante-el-informe-de-seguridad/)

## Verificación negativa realizada — hecho descartado

Durante la búsqueda se localizaron notas sobre la muerte de **25 elementos de la Guardia Nacional**
tras el operativo contra "El Mencho". La verificación sitúa esos hechos en **febrero de 2026**
(muerte de Nemesio Oseguera el 22 de febrero; declaración de García Harfuch el 23 de febrero), no en
agosto. **Descartado del corte.** Se documenta aquí porque los resultados de buscador lo presentaban
sin fecha clara y su inclusión habría sido un error grave de periodo.

## Limitaciones de la búsqueda

1. **Bloqueo total de acceso HTTP directo** (ver sección inicial). Ninguna lectura de artículo
   completo ni de boletín original fue posible; toda la información proviene de fragmentos de
   resultados de buscador.
2. **Barrido obligatorio de portales oficiales no ejecutado**: 0 de 32 secretarías de seguridad
   estatales, 0 de 32 fiscalías, 0 portales federales.
3. **Ningún nivel de confianza ★★★★★** se asignó en este corte: la escala superior exige fotografía o
   documento oficial verificado, imposible bajo estas condiciones.
4. **Tres discrepancias quedan abiertas** y explícitamente no integradas: 72 vs. 172 AEI (Sinaloa);
   acumulado de "El Willy" entre 56 y ~100; nombre del presunto líder del CJNG (González vs.
   Valencia).
5. **Numeración de la edición**: ARGOS 89 continúa el consecutivo de ARGOS 88 (corte 2026-08-04). Entre
   ambas ediciones median veinte días sin producto, por lo que **la comparación de eventos rojos entre
   cortes consecutivos no constituye una serie temporal** y así se advierte en la página 7.
6. **Pendiente heredado**: `reports/_pendiente-barrido-ARGOS-88.md` documenta que la clasificación de
   eventos rojos de ARGOS 88 quedó incompleta. Ese pendiente **no se resuelve en esta edición** y
   sigue abierto.
