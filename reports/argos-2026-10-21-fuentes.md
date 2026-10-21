# ARGOS 139 — Archivo de fuentes

**Corte**: 2026-10-21 · **Ventana**: 20-oct 07:06 → 21-oct 10:23 CDMX (**27 h 17 min**; `WINDOW_DAYS = 2`) · **Densidad**: 9 hechos propios / 27,28 h = **0,33 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de arranque de la sesión (Bloque 0, 10:23 CDMX). Consultas de 10:24 a 12:02 CDMX en la ola y el coordinador (marca «Consulta» del cartelón, que se rehace con la hora real de la última búsqueda de `procedencia-cifras`). Los hechos posteriores a las 10:23 pertenecen a ARGOS 140.
**Sustituye** a la versión de 43 min de ARGOS 139, retirada por el destinatario el 20-oct (`_argos-139-retirado-*.md`): sus ARG-ID no existen; lo que se tomó de ella se reverificó o se marca.

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-21-equipos.md`. Plantilla: `tools/plantilla-equipos-139.md`.

## 1. La base

- Clon en la rama de sesión `claude/argos-139-qe9f01`, en `60f2777` (orden de ARGOS 126), por detrás de `origin/main`. *Fast-forward* a `main` (`d0c6ab7`, PR #15 con ARGOS 129 a 138) y a `claude/argos-139-9anrf5` (`cdf7407`); `claude/argos-129` … `-138`: «Already up to date». Ningún merge no-*fast-forward*.
- `reports/`: 212 archivos, última edición `argos-2026-10-20` (ARGOS 138).

## 2. Red y modo de búsqueda

- **Egreso**: `curl -s -o /dev/null -m 12 -w '%{http_code}' https://www.gob.mx/fgr` → **`000`** (dos veces), 10:23 CDMX. Bloqueo vigente. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**.
- **Consulta de control** («asesinan ataque armado "este martes" 20 de octubre 2026 México»): `extended` → siete hechos del 20-oct (Tezontepec, Mazatlán, Juchitán, Uruapan, Puerto Vallarta, Acapulco, Tijuana); `standard` → nada de México de 2026. Se mantuvo `extended`.
- **Presupuesto**: control 2 + ola 156 (6 × 26) + coordinador 7 = **165** antes de los controles; `procedencia-cifras` hasta 30.

## 3. Rotación — prioridad sobre el ciclo y CICLO C, declarados

| Renglón | Resultado |
|---|---|
| Ciclo | **C** — Occidente y Sureste encabezaron el triaje judicial tras la prioridad |
| Prioridad — sentencias (14 `NO REVISADA` en la versión retirada) | **Saldadas (10)**: Son, Dgo · Coah, NL, SLP, Zac · Gto · Mor · Chis (`fge.chiapas.gob.mx`, dominio confirmado), Yuc (`fge.yucatan.gob.mx`, confirmado). **Siguen (4)**: Sin (`fge.sinaloa.gob.mx`: 0 páginas; decimotercera edición sin boletín), Tlax (`fiscalia.tlaxcala.gob.mx` no devuelve; `pgjtlaxcala.gob.mx` no probada), Hgo (`pgjhidalgo.gob.mx` no devuelve), Camp (`fiscalia.campeche.gob.mx` no devuelve) |
| Prioridad — armamento (19) | **Saldadas (10)**: BCS, Jal, Nay, Ags, Col, CDMX, Edomex, Pue, Qro, Chis. **Siguen (9)**: BC, Son, Dgo (dominios SSP sin páginas) · NL (`seguridad.nl.gob.mx` sin páginas) · Gto · Mor, Tlax, Hgo · Gro (`ssp.guerrero.gob.mx` sin páginas) |
| Prioridad — alto impacto (11 de solo regional amplia) | **Con consulta propia (10)**: BCS, Dgo, SLP, Zac, CDMX, Pue, Tlax, Qro, Camp, Yuc. **Sigue amplia**: Coah |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Occidente: Jalisco publicó sentencias el 18 y 19-oct (ventana de 138), Colima el 9-oct, Nayarit el 8-oct. Sureste: ninguna con fecha en ventana; dos dominios de fiscalía confirmados (Chiapas, Yucatán). Lo que la prioridad aportó: Durango devolvió su portada con boletines del 15, 16 y 19-oct, y Chiapas y Yucatán, sus dominios de fiscalía |
| Regresión | Sentencias `NO REVISADA` en 139: BC, BCS, Chih, Sin · Tamps · CDMX, Pue, Tlax, Hgo, Qro · Camp (11). Armamento `NO REVISADA`: BC, Son, Dgo, Chih, Sin · Coah, NL, Tamps, SLP · Mich, Gto · Mor, Tlax, Hgo · Gro, Oax, Camp, Yuc, QRoo (19). **Prioridad sobre el ciclo en 140** |

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **19-oct** | **Existe**: «acciones relevantes del 19 de octubre de 2026», publicado el 20-oct, por sus republicadores (Milenio; RED113; Talla Política; Argonmexico 2026/10/20). **Corrige el `SIN RESULTADO INDEXADO` de la versión retirada**: el boletín se indexó después. Hechos del 19-oct, 🟢, ventanas anteriores → vistos (La Rumorosa; Zapopan, «El Nenuco»; Culiacán, 1,240 L; Zacatecas, cateo). Corroboración débil por construcción |
| **20-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas |
| **21-oct** | `SIN RESULTADO INDEXADO EN VENTANA` (forma de rango) |

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Río Bravo** | **🔴 `-REC-` por decisión del destinatario** → `ARG-139-REC-001`, ventana de **ARGOS 129**. Tercer resumen coincidente con la «noche del 10 de octubre», atribuido a Animal Político (Grupo Animal, ruta sin fecha): **ningún fragmento literal obtenido**; el día sigue SOLO POR RESUMEN. Sin detenido |
| **1. Tulantepec** | **Sin pena publicada en la ventana**: la audiencia de individualización continúa el **21-oct a las 17:45** (La Jornada Hidalgo, por resumen), después del cierre → ARGOS 140. Fecha límite para la sentencia definitiva: 28-nov, por resumen |
| **2. Exfiscal (`ARG-136-006`)** | **Prisión preventiva oficiosa** por traición a la patria, dictada por un juez federal en la madrugada del 21-oct (Publimetro, La Verdad Juárez, Raíchali 2026/10/21). Vinculación federal **sábado 24-oct 15:00** (duplicidad del término), por resumen; audiencia estatal **jueves 22-oct**, por resumen. Sin comunicado de la FGR |
| **3. Fichas de 138** | `-001`: **dos ataques** el lunes 19 (Tomás Aquino = `-001`; Novena Sección, mototaxista, no publicado, 🟡 → visto); heridos 2 o 3 y edad 2 o 3 sin resolver; rutas fechadas 20-oct solo de agregados (El Heraldo de SLP, Síntesis) · `-002`: hallazgo informado el lunes 19, solo por resumen; identificación y detenidos solo por familiares y medios, no oficial · `-007`: abatidos identificados por familiares; quién inició, sin autoridad → sigue 🟡 · `-006`: lunes 19 por ruta; el homicidio del **11-oct** en la misma plaza (Línea Directa 2026-10-11) es **otro hecho: sin duplicidad** · `-011`: 3 armas cortas solo por resumen; 4 o 2 operativos; composición 8 adultos y 1 adolescente, por resumen · `-009/-010`: 3 o 2 detenidos (uno de 16 años), contradicho; salud no publicada · `-008`: ~11:00 solo por resumen; sin base para fe de erratas |
| **4. Ya resueltos** | No se repitieron. Ecatepec Colosio: solo reapareció el agregado de El Independiente → no se ficha |
| **5. Potencial rojo** | Cuautla, checador: ninguna autoridad lo vincula → 🟡 de 137, visto · Sonoyta: la Fiscalía de Sonora no confirma restos humanos → visto · Chietla: **los dos ataques son del domingo 18** (Temaxcalapa y Atencingo) → 🟡 de 137, vistos |
| **6. Sentencias candidatas** | Culiacán, General Cepeda, Caborca, Ensenada: sin boletín; todas publicadas antes de la ventana. Ensenada sin búsqueda nueva |
| **Heredados** | Patamban: ninguna autoridad acredita persona defensora · `ARG-137-007`: la Mesa de Colima, por resumen, «habrían disparado contra los elementos… quienes respondieron»; no consta patrullaje ni operativo → sigue 🟡 con reserva (decisión del destinatario) · `ARG-137-012`: «minutos después de la medianoche» del 18 → dentro de la ventana de 137 · Tepic: sin vinculación; contradicción sobre la detención del policía · Taxco: 4 servidores del C2 detenidos (16-19 oct), 🟢 de la ventana de 138, sin vinculación · Cachanillas: nuevos restos el martes 20, solo por resumen · Nogales, Ajuchitlán, Apatzingán, El Tívoli, Coquimatlán: sin consulta |

## 6. Arbitrajes del coordinador

| Asunto | Decisión |
|---|---|
| **Criterio de entrada** | Entra con marca el hecho con **ruta fechada del 20 o 21-oct**; el que solo tiene día por resumen queda visto, **salvo rojos** (excepción declarada: `ARG-139-003`) |
| **Villa Unión (`-001`)** | 🔴 homicidio múltiple; rutas 2026-10-20 de Línea Directa y Luz Noticias |
| **Jalpa y Moyahua (`-002`)** | 🔴 por hallazgo de tres cuerpos, con reserva: causa de muerte no informada y relación entre los dos municipios no acreditada. **Los cuerpos no se suman a los muertos por agresión**: columna propia «cuerpos hallados» |
| **Juchitán, trabajador municipal (`-003`)** | 🔴 víctima servidor público (adscripción municipal, por titular de El Imparcial); día solo por resumen; frontera |
| **Uruapan (`-008`)** | Se ficha con la hora contradicha (~06:00 / ~08:00) que decide la ventana |
| **El Terrero** | **`ARG-139-REC-002`** (🔴 drones explosivos, lunes 19 ~17:00, ventana de ARGOS 138). La nueva agresión que titula El Diario de Chihuahua el 20-oct no queda fechada: reserva |
| **Miahuatlán** | **`ARG-139-REC-003`** (🔴 ataque contra autoridad: secretario municipal herido, lunes 19 ~21:20, ventana de 138) |
| **Tlatlauquitepec** | Expresidente municipal (no servidor en funciones), ileso; noche del 19 o madrugada del 20 → 🟡 de la ventana de 138, visto |
| **Vistos de la ventana** | Mazatlán: La Floresta (día solo por resumen), Flores Magón y Luis Echeverría (madrugada del 20, ventana de 138) · Juchitán: mototaxistas de la Novena (19) y la Primera Sección (20), estudiante (col. 19 de Mayo), día solo por resumen · Acapulco, La Sabana (sin ruta fechada) · Puerto Vallarta, Ixtapa (sin ruta fechada) · Álamo, menor de 14 años (sin ruta fechada; nota idéntica de 2015) · Monclova (causa no informada) · Juárez, Portales de San Pedro y 21-oct 07:04 (posible duplicidad con `-007`) · Tezontepec, Huitel (19) · Cuernavaca, La Unión (19) · Izúcar (sin fecha) · Ixtayutla (19) |

## 7. Fe de erratas (no va al cartelón)

- **`ARG-139-FE-001` — sobre ARGOS 129**: su ventana (10-oct 09:08 → 11-oct 08:58) contuvo un hecho rojo no publicado (Río Bravo, `ARG-139-REC-001`). Efecto: **129 +1 rojo, +1 herida**.
- **`ARG-139-FE-002` — sobre ARGOS 138**: (a) dos hechos rojos de su ventana no publicados: El Terrero (`ARG-139-REC-002`) y Miahuatlán (`ARG-139-REC-003`). Efecto: **138 +2 rojos, +1 herido**. (b) Su archivo de fuentes da a Río Bravo el «sábado 17, ventana de 136»: el 17 es la denuncia; el hecho es del 10-oct. (c) `ARG-138-001` publicó uno de los dos ataques de Juchitán del lunes 19 (🟡 omitido, sin `-REC-`). (d) Su marca «Consulta 07:06-09:30» es incompatible con su último commit (07:45).
- **`ARG-139-FE-003` — sobre ARGOS 135**: Ensenada, «158 años a cada uno, por titular»: el alcance «a cada uno» es de resumen de dos medios. Cambia la etiqueta, no la cifra ni ningún total.
- **Versión retirada de 139**: «acciones del 19-oct: SIN RESULTADO INDEXADO» era falso vacío por indexación tardía.

## 8. Registro del barrido — por entidad

| Región | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Noroeste | BCS, Son, Sin, Dgo propia · BC, Chih amplia | BCS (parcial) · NO REVISADA: BC, Son, Dgo, Chih, Sin | Son (parcial), Dgo · NO REVISADA: BC, BCS, Chih, Sin |
| Noreste | Tamps, SLP, Zac propia · Coah, NL amplia | Zac (parcial) · NO REVISADA: Coah, NL, Tamps, SLP | Coah, NL, SLP, Zac (parciales) · NO REVISADA: Tamps |
| Occidente | Jal, Nay, Col, Mich propia · Ags, Gto amplia | Jal, Nay (parcial), Ags (parcial), Col · NO REVISADA: Mich, Gto | Jal, Nay, Ags, Col · Mich, Gto (parciales) |
| Centro | CDMX, Mor, Pue, Tlax, Hgo, Qro propia · Edomex amplia | CDMX, Edomex, Pue, Qro (parciales) · NO REVISADA: Mor, Tlax, Hgo | Edomex, Mor (parciales) · NO REVISADA: CDMX, Pue, Tlax, Hgo, Qro |
| Golfo | Ver, Tab propia | Ver, Tab (parciales) | Ver, Tab (parciales) |
| Sureste | Oax, Gro, Chis, Camp, Yuc, QRoo propia | Chis (parcial) · NO REVISADA: Gro, Oax, Camp, Yuc, QRoo | Oax, Gro, Chis, Yuc, QRoo (parciales) · NO REVISADA: Camp |
| **Total** | **25 propia · 7 amplia** | **13 de 32** | **21 de 32** (16 parciales) |

Casillas: todas las revisadas, `SIN RESULTADO INDEXADO EN VENTANA`; `SIN ACTUALIZACIÓN CONSTATADA`: 0. Federales (FGR, GN, Defensa, Semar): SRIV.

## 9. Emisores por ficha (recuento I/N/R/A, fijado antes de los controles)

| ARG-ID | Institucional | Nacional | Regional | Abierta |
|---|---|---|---|---|
| `-001` | 0 | 0 | 5: Línea Directa, Luz Noticias, Noroeste, Quadratín (Sinaloa y México, uno), Sinaloahoy | 0 |
| `-002` | 1: Fiscalía de Zacatecas, por titular de Meganoticias | 1: El Universal | 4: Diario de Yucatán, Imagen Zacatecas, Ecodiario, Meganoticias | 0 (El Congresista: visto, no contado) |
| `-003` | 0 | 1: La Silla Rota | 3: El Imparcial de Oaxaca, La Onda Oaxaca, Meganoticias | 0 |
| `-004` | 0 | 0 | 6: Luz Noticias, Noroeste, Meganoticias, Quadratín, Los Noticieristas, Sinaloahoy (N+, cobertura en vivo: no contada) | 0 |
| `-005` | 0 | 0 | 9: Formato 7, Plumas Libres, Horacero, La Aldea de la Información, Meganoticias, Vanguardia Veracruz, La Opinión, El Sol de Veracruz, El Portavoz | 0 |
| `-006` | 0 | 2: La Silla Rota, El Universal | 5: Quadratín Hidalgo, El Universal Hidalgo, Criterio Hidalgo, La Jornada Hidalgo, Infolibre | 0 (El Congresista, no contado) |
| `-007` | 0 | 0 | 3: El Bordo, El Diario de Juárez, El Diario de Chihuahua | 0 |
| `-008` | 0 | 1: El Financiero | 7: Grupo Marmor, MediaNews, Red Michoacán, Changoonga, La Voz de Michoacán, Quadratín, Respuesta (RED113, republicador: no contado) | 0 |
| `-009` | 0 | 0 | 3: Potosinoticias, San Luis Hoy, Pulso | 0 |
| `-REC-001` | 0 | 2: Infobae, El Universal | 11 (lista de la versión retirada, §6) | 0 |
| `-REC-002` | 1: Gobierno de Guerrero (subsecretario), solo por resumen | 1: El Financiero | 5: El Diario de Chihuahua, Diario Puntual, Lo de Hoy, Quadratín Guerrero, La Verdad | 0 |
| `-REC-003` | 0 | 0 | 6: Meganoticias, El Imparcial de Oaxaca, Expresa Oaxaca, Primera Línea, Canal 13, Telediario | 0 |

URL completas: en las notas del coordinador y los informes de equipo (`argos-2026-10-21-equipos.md`). El Terrero: El Financiero https://www.elfinanciero.com.mx/estados/2026/10/20/desplazados-regresan-a-su-comunidad-en-guerrero-y-atacan-sus-casas-con-drones/ · El Diario de Chihuahua https://eldiariodechihuahua.mx/nacional/2026/oct/19/atacan-con-drones-explosivos-a-desplazados-en-guerrero-849507.html y https://www.eldiariodechihuahua.mx/nacional/2026/oct/20/reanudan-ataques-contra-desplazados-que-volvieron-a-guerrero-849839.html · Diario Puntual https://diariopuntual.com/nacional/2026/10/21/11792/guerrero-militares-ataque-drones-el-terrero · Lo de Hoy https://lodehoy.com.mx/estados/2026/10/21/36410/ataque-drones-el-terrero-guerrero · Quadratín https://guerrero.quadratin.com.mx/atacan-con-drones-pueblo-de-juan-r-escudero-tras-regreso-de-desplazados/ · La Verdad https://laverdad.com.mx/2026/10/desplazados-de-guerrero-denuncian-ataque-con-drones/ . Miahuatlán: Primera Línea https://www.primeralinea.mx/2026/10/20/atacan-a-tiros-a-secretario-particular-del-edil-de-miahuatlan-de-porfirio-diaz-alcalde-por-su-parte-fue-baleado-en-junio/ · Meganoticias https://www.meganoticias.mx/salina-cruz/noticia/balean-a-secretario-municipal-de-miahuatl%C3%A1n-en-colonia-la-merced/780734 · El Imparcial https://imparcialoaxaca.mx/policiaca/balean-al-secretario-municipal-de-miahuatlan/ y https://imparcialoaxaca.mx/los-municipios/miahuatlan-no-sale-de-la-mira-de-las-balas-atacan-ahora-al-secretario-municipal-sigue-la-violencia-contra-funcionarios/ · Expresa https://www.expresaoaxaca.com.mx/policiaca/atacan-a-balazos-a-funcionario-de-miahuatlan-en-la-colonia-la-merced/ · Telediario https://www.telediario.mx/policia/balean-secretario-particular-edil-miahuatlan-oaxaca · Canal 13 https://canal13mexico.com/noticias-2/regionales/oaxaca/secretario-particular-de-edil-de-miahuatlan-victima-de-ataque-armado/ . Juchitán (`-003`): La Silla Rota https://lasillarota.com/estados/2026/10/21/pese-a-blindaje-en-24-horas-matan-a-cinco-hombres-en-juchitan-533955.html · El Imparcial https://imparcialoaxaca.mx/policiaca/ejecutan-a-trabajador-del-ayuntamiento-en-pleno-crucero-de-juchitan/ · La Onda Oaxaca https://www.laondaoaxaca.com.mx/2026/10/juchitan-suma-otra-victima-mortal-cinco-asesinatos-en-tres-dias-pese-al-despliegue-de-seguridad · Meganoticias https://meganoticias.mx/salina-cruz/noticia/ejecutan-a-joven-en-crucero-de-juchit%C3%A1n-en-medio-de-violencia/781097 .

## 10. Desglose de cálculos propios

- Hechos propios: 9 (`len(E)`); semáforo 3/6/0; **muertos por agresión 8** (`MU`: 2 + 1 + 1 + 1 + 1 + 1 + 1), **heridos 1** (`HE`), **cuerpos hallados 3** (`CU`), derivados del arreglo `E`; recuperaciones: 0 muertos y 2 heridos (`MU_REC`, `HE_REC`), fuera de todo total.
- Densidad: 9 / 27,2833 h = 0,330 → **0,33**.
- Marcas: 7 `PUBLICADO EL DÍA DE APERTURA SIN HORA` y 2 `FRONTERA DE VENTANA — HORA NO FIJADA`: **ningún hecho propio con hora fijada por fuente**.
- Entidades: 8 (Sinaloa con dos hechos).
- Armamento: `TOT` = 0 en las diez categorías; ninguna fila.

## 11. Los dos controles editoriales

(Se completa tras las dos rondas.)

## 12. Herramientas

- `tools/datos-argos-139.py` (rehecho: hechos propios, tres recuperaciones, columna de cuerpos hallados) · `tools/gen-movil.py` · `tools/gen-texto.py` · `tools/validar.js`.
- Comandos: `python3 tools/datos-argos-139.py reports/argos-2026-10-20.html reports/argos-2026-10-21.html` · `python3 tools/gen-movil.py 139 2026-10-21 138 2026-10-20 10:23` · `python3 tools/gen-texto.py reports/argos-2026-10-21.html reports/argos-2026-10-21.txt` · `node tools/validar.js reports/argos-2026-10-21.html 2026-10-20 2026-10-21`.

## 13. Lecciones de método (no van al cartelón)

1. **Un boletín federal «sin resultado» puede existir y no estar indexado todavía**: el del 19-oct no apareció la mañana del 20 y sí la del 21.
2. **Los recuentos de medios («seis asesinados este martes», «cinco en 24 horas») vienen de coberturas en vivo o agregados**: sirven para buscar cada hecho, nunca como cifra.
3. **Sin hora en ninguna fuente**: los nueve hechos propios tienen solo día; la frontera de las 07:06 no se puede resolver con fuentes de precisión diaria.
4. **Dominios**: confirmados `fge.chiapas.gob.mx`, `fge.yucatan.gob.mx`, `ssp.chiapas.gob.mx`; sin páginas `fge.sinaloa.gob.mx`, `pgjhidalgo.gob.mx`, `fiscalia.tlaxcala.gob.mx`, `fiscalia.campeche.gob.mx`, `ssp.guerrero.gob.mx`, `seguridad.nl.gob.mx`, `ssp.durango.gob.mx`, `ssp.bajacalifornia.gob.mx`, `sspes.sonora.gob.mx`.
