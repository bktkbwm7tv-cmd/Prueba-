# ARGOS 127 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-09 · **Ventana**: 2026-10-08 08:56 → 2026-10-09 07:20 CDMX · **22 h 24 min**
**Rama**: `claude/argos-127` (partió de `main` = `origin/claude/argos-126` = `7e55aad`).

---

## 1. La base

Bloque 0 ejecutado como primer comando: hora real **2026-10-09 07:20 CST** (UTC−6). `git merge --ff-only origin/main` avanzó en
fast-forward `60f2777 → 7e55aad`; `git merge --ff-only origin/claude/argos-126` respondió «Already up to date». Estado encontrado:
`argos-2026-10-08` (ARGOS 126) y **135 archivos** en `reports/`, lo previsto. `31763f1` es ancestro de `main`; encima lleva `7e55aad`
(orden de arranque de 127). El clon arrancó con HEAD suelto: se abrió `claude/argos-127` antes de escribir.

| Serie | 122 | 123 | 124 | 125 | 126 | **127** |
|---|---|---|---|---|---|---|
| Duración | 87 h 21 | 23 h 25 | 46 h 19 | 320 h 34 | 17 h 41 | **22 h 24** |
| Densidad (hechos/h) | 0,19 | 0,04 | 0,30 | 0,16 | 0,40 | **0,27** (6 / 22,4, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (8 y 9-oct). La plantilla de 126 ya lo traía en 2; el generador lo
comprueba con `assert` en vez de sustituirlo.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`**; el proxy registra `www.gob.mx:443 — connect_rejected` (política de la
  organización). Un `WebFetch` de un agente a un medio (tallapolitica) → `ENOTFOUND`. **Ningún documento leído íntegro.** Techo
  **★★★☆☆**, novena edición.
- **Consulta de control** (Balleza, Pinalejo, en los dos modos): `standard` devolvió **una** nota útil (Tiempo, sin fecha en la ruta);
  `extended` llegó al **8-oct** (El Independiente 2026/10/08) y a nueve notas del 7-oct. **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: una sola ola de **nueve equipos** (encargos 22, seguimientos 16, boletín federal 20, Noroeste 22, Noreste 22,
  Occidente 21, Centro 18, Golfo 18, Sureste 22 = **181**) + 2 de control + 5 de verificación del coordinador = **188**;
  `procedencia-cifras` con tope de **12** → techo **200**. `editor-duplicidad` no busca en la web.

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

| Renglón | Resultado |
|---|---|
| Prioridad sobre el ciclo — sentencias | **Las 16 fiscalías `NO REVISADA` de 126 revisadas**: BCS, Sin · Coah, Tamps, SLP, Zac · Col, Nay, Ags, Mich · Chis, Oax, Gro, Camp, Yuc, QRoo. Las 16, `SIN RESULTADO INDEXADO EN VENTANA` por `site:` dirigido o búsqueda de medios |
| Prioridad sobre el ciclo — armamento | **Morelos** (`site:` a CES, SSC y Fiscalía: sin boletín de ventana) y **Tlaxcala** (búsqueda genérica; `site:pgjtlaxcala.gob.mx` no se intentó): **`NO REVISADA`** —corregido por `editor-duplicidad`; vuelve a encabezar en 128— |
| Ciclo | **B** — Noreste + Golfo encabezaron el triaje judicial |
| Rendimiento | **Ninguna sentencia integrable.** El ciclo B halló **Matamoros, 6 sentenciados a 25 años 3 días** (publicado 6-oct, previo) y el **agregado de la FGE Veracruz del 8-oct** (17 sentencias, sin individualizar). La prioridad halló **Campeche, FGR** (frontera, solo medios) y casos previos de Nayarit, Michoacán y QRoo nunca vistos |

Serie: C (125) sí · A (126) no · **B (127) no — candidatos, sin integrable.**

## 4. Boletín federal — triple consulta

| Acciones de | Publicado | Estado | Formato |
|---|---|---|---|
| 7-oct | 8-oct («este jueves», El Independiente 2026/10/08) | **LOCALIZADO** por republicadores: Milenio (acciones del 7-oct en la ruta), Tallapolítica, Certeza Diario, RED113 | **diario**, 5 entidades: Chih, NL, Sin, Tab, Zac |
| 8-oct | — | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto con y sin `site:`; rangos 7-8, 8-9, 8-9-10; título sin `site:`) | — |

`gabinetedeseguridad.gob.mx/resultados/` por `site:`: lo indexado llega al **6-oct**. GN, Defensa y Marina con fecha 8-oct: sin resultado.

**Arbitraje del boletín del 7-oct**: ARGOS 126 asignó ese boletín a su propia ventana (renglones del 7-oct sin hora, `FRONTERA`) e
integró Pánuco, El Rosario, Apodaca y Ciudad Juárez; Balleza pasó a `-REC-`; **Cosalá se retiró**. **Omitió dos renglones con armamento:
Ojocaliente y Centro (Tabasco).** Como los hechos son del 7-oct —anteriores a la apertura de 127— y 126 ya reclamó ese boletín, los tres
se publican como **`-REC-` con ventana de origen ARGOS 126**: `ARG-127-REC-002` (Ojocaliente), `-003` (Centro, Tabasco), `-004` (Cosalá,
reintegrado: la cifra de laboratorios ya se sostiene en el *slug* de Noroeste, «inhabilitan-cinco-laboratorios-clandestinos»).
**Control de topónimo** (regla de 126): Ojocaliente, Centro y Cosalá se buscaron por su topónimo; ninguna nota reporta agresión ni
enfrentamiento. Pánuco: los civiles armados **huyeron al monte**, sin combate.

## 5. Los cuatro encargos

| Encargo | Resultado |
|---|---|
| **GUERRERO · El Balcón** (`ARG-125-051`) | **Sin dato nuevo con ancla en ventana.** El **video** circuló el 8-oct (El Universal, UnoTV, Infobae 2026/10/08, Crónica 2026/10/08, MVS 2026/10/8): **no autenticado** —una fuente abierta lo llama «editado», otra «auténtico»; ninguna institucional—. **No se difunde su contenido.** Peritaje oficial: `SIN RESULTADO INDEXADO EN VENTANA`. Amparo 412/2026: suspensión concedida el **5-oct** por el Juzgado Noveno de Distrito (Iguala), dato previo; cumplimiento sin informe. Marcha a Palacio Nacional: anunciada por 319 comunidades el 7-oct, sin fecha. Cero detenidos, carpeta no indexada. Sin leer: El Independiente 2026/10/09 («familias identifican en video») |
| **CHIHUAHUA · Balleza** (`ARG-126-REC-004`) | **Sin novedad en ventana.** Abatidos **sin identificar** (20-30 años, Semefo; fiscal de Distrito Zona Sur, Guillermo Hinojos Hinojos, por resumen). Hora: madrugada del 7 (Netnoticias) frente a noche del 6 (Turquesa). **231** = boletín federal (republicadores, no independientes); **230 y 2 vehículos** = Quadratín Chihuahua e Impacto (sin fecha en la ruta); **5 vehículos** = titular de diario.mx atribuido a la FGE. **No se arbitra.** Boletín FGE sin literal |
| **SINALOA · Pánuco, 82 AEI** (`ARG-126-004`) | **Tipología resuelta por cita de la SSPE**: «82 artefactos explosivos improvisados **para lanzarse por medio de dron**» (no «tipo mina»: no se homologa con `ARG-124-003`). **Desglose**: 1 fusil 7.62×39, 5 cargadores, **450 cartuchos 7.62×39 + 220 cartuchos 5.56 = 670** (suma, cálculo propio; coincide con el boletín), 1 chaleco, 2 placas, 1 Jeep con reporte de robo. **Lugar**: camino de terracería cerca de Pánuco. **Corporación contradicha**: SSPE/GOES frente a Ejército + Policía Estatal. Fuentes: Tus Buenas Noticias 2026/10/08, Línea Directa 2026-10-08; post de sspsinaloa.gob.mx indexado y **no leído**. Procedencia: **cita por resumen** |
| **NAYARIT · Xalisco** (`ARG-125-003`) | Sin cifra oficial ni identificaciones. 8-oct: la Presidencia pide esperar a la CNB (Expansión 2026/10/08); la CNB remite a la FGE Nayarit. **Ópalo**: vínculo **sí**, por **Reforma, fuente única, por resumen**: el cateo derivó en la investigación de La Curva; «El Güero», Omar David «N». **«9 cuerpos» (La Prensa) = junio de 2020, El Valle del Avión: DESCARTADO.** «33 cráneos» (SDP): no confirmado |
| **JALISCO · Guadalajara** (`ARG-125-002`) | Col. Clemente Orozco, **4 cuerpos** el 6-oct (una fuente, 7-oct). Georradar y comunicado: `SIN RESULTADO INDEXADO EN VENTANA` |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| **Cócorit** (`ARG-126-001`) | **El muerto se confirma**: adolescente de 15 años y 3 heridos (Proyecto Puente y Medios Obson 2026/10/07, Diario del Yaqui 145269). La versión «4 heridos, ningún muerto» es la nota preliminar del mismo medio (145240). **El rojo de 126 se mantiene** |
| **Coatzacoalcos** (`ARG-126-FE-004`) | Caso Guillermo Pamucé Yep: **5 detenidos**, prisión preventiva el 5-oct (La Jornada, Infobae, La Silla Rota 2026/10/05). Contradicción: Municipio Sur 2026/10/06 y CDPNoticias dicen «vinculados». Audiencia del 8-oct (causa 540/2026): `SIN RESULTADO INDEXADO EN VENTANA`. **«3 detenidos el 1-oct» no aparece en ninguna fuente por segunda edición → `ARG-127-FE-002`** |
| **Zihuatanejo** (`ARG-126-REC-008`) | Sin retorno de desplazados; cifra sin reconciliar (~150 personas, Infobae 2026/10/07, frente a ≥30 familias). Comunidades por resumen: San Ignacio, El Mamey, La Vainilla, Pie de la Cuesta, El Puertecito. Sin peritaje |
| **Mixtequilla** (`ARG-126-REC-007`) | **Fecha resuelta: noche del lunes 5-oct** (Infobae, La Silla Rota y MVS, 2026/10/6). Sin detenidos |
| **Casas Grandes** (`ARG-126-REC-003`) | **Heridos: 2** (ninguna fuente da 3). **Móvil contradicho con peso**: un comandante de la AEI, citado por Diario de Juárez 2026/oct/07, dice que **no fue secuestro sino deuda de drogas**. Queda en duda el titular «presuntos secuestradores» de 126 |
| **26 extranjeros** (`ARG-126-007`) | Literal confirmado por Milenio (acciones del 7-oct); **nacionalidades no publicadas** |
| **Comonfort · Hermosillo** | Comonfort: vinculación `SIN RESULTADO INDEXADO`. Hermosillo: la orden por el doble homicidio estaba «en trámite de solicitud» (resumen); sin nota de emisión |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Penal El Castillo** (`ARG-127-004`) | Inicio ~10:00 del 8-oct (La Silla Rota, **por resumen**): dentro de ventana. Aun sin hora, el hecho cae el día de apertura y ninguna edición lo publicó: 127 es la primera que lo ve. **🔴 por motín con víctimas**, que la lista roja nombra. Edad del menor contradicha (11, 3 o 2 años): **no se publica** |
| **Autolavado de Flores Magón** (`ARG-127-002`) | ~14:20 por resumen; **3 muertos** por titular (Luz Noticias 2026-10-08 «Aumentan a tres»; Línea Directa 2026-10-08 «Muere en hospital joven herido»). La Jornada 2026/10/09 da 2 muertos y 3 lesionados (anterior al tercer deceso). 🔴 por homicidio múltiple |
| **Uruapan, Sol Naciente** | Hora del hecho ~03:30-05:00 del 8-oct por resumen de tres medios: **anterior a la apertura** → `ARG-127-REC-001`, ventana de origen ARGOS 126, 🟡 (el Estado inicia y es repelido; heridos no mueven el color) |
| **San Francisco de Borja–Nonoava** (El Diario de Chihuahua 2026/oct/08, «Dejan dos enfrentamientos cuatro muertos») | El resumen copia rasgos de Balleza (edades, ropa táctica, tres fusiles, cinco camionetas) y sitúa el hecho «en la madrugada» sin día: **`POSIBLE DUPLICIDAD` con `ARG-126-REC-004` y fecha no fijada. No fichado** |
| **Penjamillo, emboscada a Guardia Civil** | ~7-oct («segunda agresión en 24 h», Quadratín, sin fecha en la ruta): ventana 125 o 126 sin fijar. **No fichado**; pasa a pendientes como candidato `-REC-` 🔴 |
| **Ixtlahuacán de los Membrillos** (Informador 20261008) | 2 ametralladoras Browning 7.62, 2 fusiles .50, 3 largas, 1 corta = **8 armas**, como `ARG-125-ARM-005` (8 armas, 6-oct): **`POSIBLE DUPLICIDAD` — actualización del desglose**. No integrado |
| **Centro, Tabasco** (`ARG-127-REC-003`) | Diario de Tabasco 2026/10/08: SSPC detiene a dos en Centro con armas, cifras no verificadas. **Posible duplicidad declarada en la ficha** |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-127-FE-001`** — sobre **ARGOS 126**: cuatro hechos de su ventana no publicados (`ARG-127-REC-001` a `-004`). Efecto: rojos 1 → 1,
  amarillos 1 → 2, verdes 5 → 8. **Cosalá reintegrado** tras su retiro en 126. Armamento: **se integra solo Ojocaliente** (5 largas, 1,093
  cartuchos, 47 cargadores, **solo por resumen**). **Centro, Tabasco** (3 cortas, 4 largas, 540 cartuchos, 7 cargadores, 2 detenidos) queda
  `POSIBLE DUPLICIDAD — NO INTEGRAR AL TOTAL HASTA VALIDACIÓN` (hallazgo de los dos controles).
- **`ARG-127-FE-003`** — sobre **`ARG-126-004` / `ARG-126-ARM-002` (Pánuco)** y **`ARG-126-005` / `ARG-126-ARM-003` (El Rosario)**: los
  **670 cartuchos y 5 cargadores** de Pánuco y los **1,198 cartuchos y 3 cargadores** de El Rosario llegan a **dos ediciones consecutivas
  solo por resumen**. Por el umbral de fe de erratas se retiran del acumulado: `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`.
  **Se mantienen** los 82 AEI y el fusil de Pánuco (titular y *slug* de Rotativo, «aseguran-82-explosivos-dron-fusil») y los 12 kg de El Rosario
  (titular). Si se lee el post de sspsinaloa.gob.mx, la cifra se reinstala como citable.
- **Armamento de la ventana de 126 tras FE-001 y FE-003, cálculo propio**: cortas **4**; largas 5 + 5 = **10**; cartuchos 1,928 − 670 − 1,198
  + 1,093 = **1,153**; cargadores 21 − 5 − 3 + 47 = **60**; AEI **82**; detenidos **2**.
- **`ARG-127-FE-002`** — sobre **`ARG-125-021`**: «3 detenidos el 1-oct» llega a **dos ediciones consecutivas sin respaldo citable**
  (`ARG-126-FE-004`). Por el umbral de fe de erratas, **se retira la cifra**: `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`.
  Las fuentes indexadas dan **5 detenidos informados el 5-oct**.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV | SRIV | NO REVISADA |
| Baja California Sur | SRIV | NO REVISADA | SRIV (La Paz 21 años, 1-oct, previa) |
| Sonora | SRIV (Cócorit, seguimiento) | NO REVISADA | **solo medios** (Cajeme 25 años, frontera) |
| Chihuahua | SRIV (San Fco. de Borja, no fijado) | SRIV | SRIV (Acequias y Senderos, previas) |
| Sinaloa | **hecho** (penal El Castillo; autolavado) | **hecho** (Culiacán, Montecarlo) · REC Cosalá | SRIV (`site:` sin boletines; Culiacán 22 años sin día) |
| Durango | SRIV | NO REVISADA | SRIV (portal indexado; 5 y 7-oct, previas) |
| Coahuila | SRIV (Parras, hallazgo sin violencia) | SRIV | SRIV |
| Nuevo León | SRIV | SRIV | SRIV (Laurentino «N», previa) |
| Tamaulipas | SRIV | SRIV (notas sin fecha fijable) | SRIV (Matamoros, previa) |
| San Luis Potosí | SRIV | **hecho** (capital, GCE) | SRIV |
| Zacatecas | SRIV (pista NTR: padre de alcaldesa, sin leer) | REC Ojocaliente | SRIV |
| Jalisco | SRIV | SRIV (Ixtlahuacán, posible duplicidad) | NO REVISADA |
| Colima | **hecho** (col. Moctezuma) | SRIV | SRIV (FGR 3 × 4 años, previa) |
| Nayarit | encargo (Xalisco) | SRIV | SRIV (240 y 40 años, previas) |
| Aguascalientes | NO REVISADA | NO REVISADA | SRIV (portal indexado) |
| Michoacán | REC Uruapan · Penjamillo sin fijar | SRIV | SRIV (Buenavista 28 años, previa) |
| Guanajuato | SRIV | SRIV | NO REVISADA |
| Ciudad de México | SRIV | NO REVISADA | SRIV |
| Estado de México | SRIV (Otomí, acumulado) | SRIV | SRIV |
| Morelos | SRIV (persecución sin fecha fijada) | SRIV (`site:`) | NO REVISADA |
| Puebla | **hecho** (Fuentes de San Bartolo) | SRIV | NO REVISADA |
| Tlaxcala | SRIV | NO REVISADA (genérica, sin `site:`) | NO REVISADA |
| Hidalgo | SRIV | SRIV | NO REVISADA |
| Querétaro | SRIV | SRIV (vinculación de 3 con armas, cateo sin fecha) | NO REVISADA |
| Veracruz | SRIV | SRIV | **solo medios** (agregado FGE 8-oct) |
| Tabasco | SRIV | REC Centro | SRIV |
| Guerrero | encargo (El Balcón) | SRIV | SRIV |
| Chiapas | SRIV | SRIV | SRIV |
| Oaxaca | SRIV | SRIV | SRIV (dominio indexado: fge.oaxaca.gob.mx / portal.fgeo.gob.mx) |
| Campeche | SRIV | SRIV | SRIV estatal · **FGR, solo medios** (Lerma) |
| Yucatán | SRIV (cobertura mínima) | SRIV | SRIV |
| Quintana Roo | SRIV (Cancún, fecha sin fijar) | SRIV | SRIV (50 años, 7-oct, previa) |

**Sentencias: 24 de 32 + FGR; 8 `NO REVISADA`** (BC · Jal, Gto · Mor, Pue, Hgo, Qro, Tlax). **Armamento: 26 de 32** (NO REVISADA: BCS, Son,
Dgo, CDMX, Ags, Tlax —la búsqueda de Tlaxcala fue genérica, sin `site:`, y no basta para la casilla SRIV—). **Alto impacto: 31 de 32** (Ags NO REVISADA).

## 10. Hechos vistos y NO fichados, con motivo

| Hecho | Motivo |
|---|---|
| Mazatlán, doble homicidio del 6-oct en Flores Magón | Anterior a la ventana; solo por resumen |
| Culiacán, cuerpo con mensaje cerca de La Lomita | Fecha no fijada |
| Sinaloa, «18 muertos este jueves» (Luz Noticias 2026-10-08) | Conteo periodístico, no oficial; incluye los 10 del penal |
| Morelos, Cuautla–Cuernavaca, 2 detenidos con armamento sin cifra | Fecha no fijada; cualitativo |
| Edomex, Operativo Otomí, 1,311 detenidos | Acumulado desde 23-sep; no integrable |
| Querétaro, Santa María Magdalena, vinculación de 3 con 3 cortas | Vinculación, no sentencia; cateo sin fecha |
| Cancún, Región 235 y mototaxistas | Fecha sin fijar |
| Chiapas, Suchiapa, alcaldesa sustituta (Alerta Chiapas 2026/10/08) | Seguimiento de `ARG-125-014`, no hecho nuevo |
| Torreón, «Los Cuates» | Vinculación, previa |
| Veracruz, agregado FGE del 8-oct | Agregado de 24 h sin individualizar |

## 11. Desglose de cálculos propios

- Densidad: 6 / 22,4 h = **0,27**. Duración: 8-oct 08:56 → 9-oct 07:20 = **22 h 24 min**.
- Armamento: cortas 1 + 1 = **2**; cartuchos 30 + 29 + 6 = **65**; cargadores **2**; detenidos en evento de aseguramiento **2**.
- Muertos en hechos propios: 1 + 3 + 1 + 10 = **15** (13 en rojos). Heridos: **16 en el penal**; autolavado **2 / 3 / 4 según la fuente, no se suman**.
- San Luis Potosí: 29 + 6 = **35 cartuchos** de dos intervenciones. Personas en sentencias candidatas: 1 + 5 = **6**. Pánuco–tipo mina: 22-sep → 7-oct = **15 días**.
- Pánuco: 450 + 220 = 670.

## 12. Fuentes por ficha

- **`ARG-127-002`** — Luz Noticias 2026-10-08 (dos notas, una «Aumentan a tres»); Línea Directa 2026-10-08; Los Noticieristas 2026/10 (4 heridos); Noroeste (3 muertos y **2 heridos**; «muere tercera víctima»); Reporte18 (3 heridos); Sinaloahoy (s/f); La Jornada 2026/10/09.
- **`ARG-127-003`** — Noticias Manzanillo («este jueves»); AFmedios (dos notas); Vadenuez; Colima al Día 37939; El Noticiero en Línea; Colima Noticias. Ninguna con fecha en la ruta.
- **`ARG-127-004`** — Proceso 2026/10/8; Expansión 2026/10/08; La Silla Rota 2026/10/8; El Heraldo de México 2026/10/8; El Financiero 2026/10/08; Informador 20261008; El Mañana 2026/10/8; Infobae 2026/10/09; La Jornada 2026/10/09; Noroeste, Reforma, UnoTV, Azteca Sinaloa, El Siglo de Torreón (s/f).
- **`ARG-127-001`** — Diario Puntual 2026/10/08; Síntesis 2026/10/08; Reto Diario 2026/10/08 (nombra a la víctima, no oficial: no se reproduce); Curul y Alcance Diario (s/f). Hora ~19:00 solo por resumen: retirada la marca de frontera.
- **`ARG-127-005`** — sspsinaloa.gob.mx (post, s/f, no leído); Línea Directa 2026-10-08; Luz Noticias 2026-10-08; Tus Buenas Noticias 2026/10/08; Los Noticieristas y Rotativo (s/f).
- **`ARG-127-006`** — El Heraldo de SLP 2026/10/08; Potosí Noticias 2026/10/08; Plano Informativo 1174385, Frontal Noticias, San Luis Hoy (s/f).
- **`ARG-127-REC-001`** — La Voz de Michoacán, Meganoticias 777096, Quadratín (s/f).
- **`ARG-127-REC-002`** — Milenio (acciones del 7-oct); RED113 2026/10; Tallapolítica; Certeza Diario.
- **`ARG-127-REC-003`** — Milenio (acciones del 7-oct); El Independiente 2026/10/08; Ahora Tabasco y Ahora Noticias (s/f).
- **`ARG-127-REC-004`** — Milenio (acciones del 7-oct); Noroeste (CE26333320, *slug*); Línea Directa 2026-10-08.
- **Sentencias candidatas** — Tribuna 2026/10/08, Expreso, Uniradio, Entorno Informativo (Cajeme); Por Esto 2026/10/8, Tribuna Campeche (Lerma); Hora Cero 2026/10/08 (agregado FGE Veracruz).

## 13. Los dos controles editoriales — ejecutados sobre la versión estable, los dos con «CORREGIR»

Racha: **trece pases consecutivos, trece «CORREGIR»** (doce hasta 126 + este). Lanzados en paralelo sobre el borrador ya validado y
commiteado (`claude/argos-127`, primer commit); **el borrador no se tocó mientras corrían**. Los dos informes citan la **numeración del
borrador** (ver «Renumeración», al final de esta sección).

**`editor-duplicidad`** — ningún hecho duplicado, ningún falso vacío, ningún descuadre aritmético. Hallazgos y disposición:

| # | Hallazgo | Disposición |
|---|---|---|
| H1 | FE-001 integraba Centro, Tabasco, con posible duplicidad | **Corregido**: Centro fuera del recálculo |
| H2 | Acción 5 de portada usaba «seis detenidos de Ópalo», sin ficha | **Corregido**: acción sobre la cifra e identificaciones de La Curva |
| H3 | Conclusión 3 generalizaba «el boletín asegura sin detener» | **Corregido**: solo Ojocaliente y Cosalá; Pánuco ya no se repite en el recuadro |
| H4 | «Cero detenidos por los cuatro violentos» sin respaldo en la ficha del penal | **Corregido**: ficha con «detenidos: no informados»; la Valoración lo declara |
| H5 | Hechos en tres o más lugares por la Valoración | **Corregido**: la Valoración remite por ARG-ID sin titulares ni cifras de hecho; la advertencia de comparabilidad, solo en la Valoración |
| H6 | Índice, §13 y `_pendientes.md` | **Corregido** al cierre |
| H7 | Fecha del hecho = publicación en hechos sin hora | **Corregido**: «Hecho: no fijada (publicado 2026-10-08)» en `-005` y `-006`. El campo `fecha` de `EVENTOS` sigue en 2026-10-08 porque el validador lo exige ≥ apertura |
| H8 | Razón de asignar REC-002 a 004 a la ventana de 126 | Escrita en §4: 126 reclamó el boletín del 7-oct; hechos del 7-oct, anteriores a la apertura |
| H9 | Recuento de fuentes del penal | **Corregido**: Nacional 9 · Regional 5 |
| H10 | Deslindes incompletos (Uruapan, Mazatlán, Colima) | **Corregido** |
| H11 | Tlaxcala armamento como SRIV sin `site:`; Culiacán 22 años sin fecha | **Corregido**: Tlaxcala `NO REVISADA` (armamento 26 de 32); Culiacán a «sin fecha fijada» |
| H12 | Acciones 1 y 2 presuponían casquillos y un hecho no fichado | **Corregido**: dictamen balístico y localización del vehículo |
| — | Totales del panorama repetidos en las tarjetas del módulo | **No se corrige**: precedente de 126; las tarjetas son el bloque obligatorio de iconografía |
| — | `.txt` omite las fichas `-REC-` y los recuadros; `validar.js` no aplica al móvil | **No se corrige en esta edición**: limitación de `gen-texto.py` y del validador, igual en 126. Pasa a deuda de método |

**`procedencia-cifras`** (12 búsquedas): citables por titular los 10 muertos y 16 heridos del penal, 9 internos y 1 menor, los 3 muertos del
autolavado, los 3 detenidos de SLP, los 5 laboratorios de Cosalá, los 82 AEI de Pánuco y el muerto de Puebla. Hallazgos y disposición:

| # | Hallazgo | Disposición |
|---|---|---|
| 1 | Heridos del autolavado 2 / 3 / 4; «al menos 19» | **Corregido**: contradicción declarada, sin sumar; título sin cifra de heridos |
| 2 | Culiacán: 30 y 2 solo por resumen; «cargadores por titular» inexacto | **Corregido** en ficha, panel, fila y tarjetas |
| 3 | SLP: 35 sin declarar como suma; revólveres por resumen | **Corregido**: suma propia declarada; la fila marca dos intervenciones |
| 4 | Ojocaliente sin marca de resumen | **Corregido** |
| 5 | Tabasco en FE-001 | **Corregido** (= H1) |
| 6 | Cosalá: 2.6 t por titular frente a 2,693 kg por resumen; titular de Capital México | **Corregido**: 2.6 t como cifra visible; 2,693 kg marcado; discrepancia declarada |
| 7 | Conclusión 1: cita de la SSPE entre comillas sin marca; 16 días | **Corregido**: «explosivos para dron» por titular, listado por resumen; 15 días, cálculo propio; 75 AEI como heredada |
| 8 | Pánuco, 670 cartuchos, segunda edición solo por resumen | **Corregido**: `ARG-127-FE-003`, extendida a El Rosario por la misma regla |
| 9 | Penal: atribuciones a la SSP no verificadas | **Corregido**: «descarta grupo armado» marcado por resumen; «Grupo Interinstitucional controla» retirado |
| 10 | Colima: «FGE procesa la escena» sin respaldo | **Corregido**: retirado; institucional 0 |
| 11 | Puebla: más fuentes fechadas; hora ~19:00; identidad | **Corregido**: Regional 5, tres fechadas; hora por resumen; renumeración |
| 12 | «6 personas» sin marca | **Corregido** |

**Renumeración antes de publicar** (la hora de Puebla obliga a reordenar del más reciente al más antiguo): Puebla `-004` del borrador →
**`-001`**; autolavado `-001` → **`-002`**; Colima `-002` → **`-003`**; penal `-003` → **`-004`**. `-005`, `-006` y las `-REC-` no cambian.
Ningún ARG-ID del borrador llegó a publicarse.

**Segundo pase** — tras las correcciones, `validar.js` → **validación OK** (escritorio) y `gen-movil.py` → **validación OK** (móvil). No hay
presupuesto de búsqueda para un segundo pase de `procedencia-cifras` (200 de 200); `editor-duplicidad` se relanzó sin búsquedas (abajo).

## 14. Herramientas

`tools/datos-argos-127.py` (generador único) → `reports/argos-2026-10-09.html`; `tools/gen-movil.py 127 2026-10-09 126 2026-10-08 07:20`;
`tools/gen-texto.py`; `node tools/validar.js reports/argos-2026-10-09.html 2026-10-08 2026-10-09` → **validación OK**.
