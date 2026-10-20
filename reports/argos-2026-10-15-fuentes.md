# ARGOS 133 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-15 · **Ventana**: 2026-10-14 08:19 → 2026-10-15 07:16 CDMX · **22 h 57 min**
**Rama**: `claude/argos-133` (partió de `origin/claude/argos-132` = `4bf49a7`).

---

## 1. La base

Bloque 0 a las **07:16 CST** del 15-oct. El clon arrancó en `60f2777`, en la rama de sesión `claude/argos-criminal-intelligence-otiawj` (por detrás de `origin/main`,
como en 128-132): se abrió `claude/argos-133` antes de fusionar. `--ff-only origin/main` → `b0558a3`; `-129` → `9eaba81`; `-130` → `63c1325`; `-131` → `db02540`;
`-132` → `4bf49a7`. **Los cinco merges, fast-forward.** Estado: `argos-2026-10-14` (ARGOS 132) y **171 archivos** en `reports/`, lo previsto.

| Serie | 128 | 129 | 130 | 131 | 132 | **133** |
|---|---|---|---|---|---|---|
| Duración | 25 h 48 | 23 h 50 | 23 h 21 | 23 h 04 | 24 h 56 | **22 h 57** |
| Densidad (hechos/h) | 0,23 | 0,25 | 0,39 | 0,26 | 0,24 | **0,48** (11 / 22,95, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (14 y 15-oct). El generador lo comprueba con `assert`.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (`CONNECT tunnel failed, response 403`), 07:16. **Ningún documento oficial leído íntegro.** Techo **★★★☆☆**.
- **Consulta de control** («ataque armado muertos "14 de octubre" 2026 México», en los dos modos): `standard` **no devolvió ningún hecho del 14-oct** (Querétaro, Tehuitzingo,
  Azcapotzalco de junio, Iztapalapa de agosto); `extended` trajo **Pénjamo, Salamanca, Silao e Iztapalapa (tianguis)**. **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola de seis equipos (Noroeste 28, Noreste 25, Occidente 28, Centro 25, Golfo y federal 28, Sureste 25 = **159**) + **9 del coordinador** = **170**;
  `procedencia-cifras` **25** → **195 de 200**. `editor-duplicidad` no busca en la web.
- **Rendimiento del coordinador** (9): miércoles 14 (Escuinapa, exdirigente ganadero); madrugada del 15 (Pénjamo **desde las 05:35**, por resumen); fosa del 14-oct
  (**Atotonilco de Tula**); noche del miércoles (**Romita**, Silao «mañana»); abatidos 14-oct (sin resultado en ventana); funcionario asesinado (sin resultado en ventana);
  madrugada del jueves (Silao, Sopeña y Veta de Ramales); Romita, segunda fuente (Azteca Bajío). **La ola no trajo por sí sola ni Atotonilco ni Romita**: los halló el
  coordinador y los fijó el equipo correspondiente con el encargo añadido.

## 3. Rotación — prioridad sobre el ciclo y CICLO B, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (16 `NO REVISADA` en 132) | **Revisadas ahora (14)**: Coah (`sitio.fgecoahuila.gob.mx`), NL (`nl.gob.mx`), Tamps (`tamaulipas.gob.mx`, `fgjtam.gob.mx`), Ags (`fiscalia-aguascalientes.gob.mx`), CDMX (`ssc.cdmx.gob.mx`), Edomex (`sseguridad.edomex.gob.mx`), Mor (`fiscaliamorelos.gob.mx`), Qro (`fiscaliageneralqro.gob.mx`, publicó el 14-oct), Gro (`fiscaliaguerrero.gob.mx`), Oax (`portal.fgeo.gob.mx`, `sspo.gob.mx`), Chis (`fge.chiapas.gob.mx`), Yuc (`ssp.yucatan.gob.mx`), QRoo (`fgeqroo.gob.mx`), Camp (`spsc.campeche.gob.mx`, nota sin fecha). **Siguen `NO REVISADA`**: BC (solo medios), SLP (dominios no devueltos; `fiscaliaslp.gob.mx` en caché antigua) |
| Prioridad — sentencias (16 `NO REVISADA` en 132) | **Revisadas (8)**: BC (`fgebc.gob.mx`, solo boletines viejos), NL (`fiscalianl.gob.mx`, solo estadísticas), Gto (`portal.fgeguanajuato.gob.mx`, sin boletines), Edomex (`fiscaliaedomex.gob.mx`), Pue (`fiscalia.puebla.gob.mx`, último feb-2026), Gro (`fiscaliaguerrero.gob.mx`, último 16-jun), Chis (`fge.chiapas.gob.mx`, solo 2025), Yuc (`fge.yucatan.gob.mx`, 1-oct). **Siguen `NO REVISADA`**: BCS, **Son y Sin (sexta edición sin dominio de fiscalía devuelto)**, SLP, Nay (`fiscalianayarit.gob.mx` no devuelto), Tlax, Hgo (`procuraduriahidalgo.gob.mx` no devuelto), Camp |
| Prioridad — alto impacto | 32 de 32 por búsqueda dirigida en medios |
| Ciclo | **B** — Noreste + Golfo encabezaron el triaje judicial tras la prioridad |
| Rendimiento | **Ninguna sentencia integrable.** Noreste: NL 155 años y Zac Juan «N» 10 años, ambas publicadas el 12-13 oct (fuera) y sin boletín; Golfo: `comunicacion.fiscaliaveracruz.gob.mx` y `fiscaliatabasco.gob.mx` devueltos, nada de octubre |
| Regresión por rotación | Armamento: BCS, Son, Jal, Col, Nay, Mich, Pue, Tlax, Hgo, Tab pasan a `NO REVISADA` (sin dominio devuelto en esta ronda). Sentencias: Chih, Coah, Tamps, Jal, Col, Ags, Mich, CDMX, QRoo. **Prioridad sobre el ciclo en 134** |

Serie: C (125) sí · A (126) no · B (127) no · C (128) no · A (129) no · B (130) no · C (131) no · A (132) no · **B (133) no.**

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **13-oct** | **EXISTE**, solo por republicadores (RED113 2026/10, Talla Política, Certeza Diario; mismo texto, **no independientes**). Publicación del 14-oct, hora no fijada. Acciones del 13-oct: ventana de 132 → `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total. Desglose **solo por resumen**: BCS, Cabo San Lucas, 2 detenidos · Chiapas, Huixtla, 170 kg de cocaína, 1 detenido; Concordia, 2 campamentos · Edomex, San Francisco Tlalcilalcalpan, 3 detenidos, 2 cortas, 1 larga · Gto, San Miguel del Brete, 1 detenido, 1 larga, 2 cortas, 1 réplica, 1 cargador, 73 cartuchos · Jalisco, «El Cromo» (ARG-132-006) · Sinaloa, Villa Unión, 1 detenido, 206 dosis de fentanilo · Sinaloa, Concordia, 1 arma, 7 cargadores, 199 cartuchos |
| **14-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto, «13 y 14», título sin `site:`). Probablemente se publique el 15-oct: **no se declara inexistente** |

**Trampa de año**: `gabinetedeseguridad.gob.mx/contenido/6826` es el boletín del 13-oct-**2025**, descartado. **GN** (dominio no devuelto), **Defensa** (no devuelto),
**Marina** (`gob.mx/semar`, último de octubre ~1-2 oct), **FGR** (`gob.mx/fgr`, solo 2020-2022), `gabinetedeseguridad.gob.mx/resultados` (listado del 5-oct): `SIN RESULTADO INDEXADO EN VENTANA`.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Navolato, Campo Romero** (`ARG-132-001`) | **FGE: restos de 3 personas «de manera preliminar»**, por titular de Sinaloahoy (sin fecha); Línea Directa 2026-10-13 (1719954) «Fueron tres osamentas». «~5» de los colectivos: solo resumen, sin fuente nominal. **Inicio del hallazgo: martes 13-oct** (Línea Directa, Luz Noticias 2026-10-13; secuencia 1, 2 y 3 cuerpos). Atribución a Milenio de «la mañana del martes 14»: incoherente con el calendario (el 14 fue miércoles), descartada. Identificaciones: ninguna; Semefo de Culiacán, ADN pendiente. Continuidad en la ventana: SRIV. **Se cierra la fecha (13-oct, ventana de 132)**; queda abierta la identificación |
| **Orizaba** (`ARG-132-002`) | **Muerto no identificado**: la FGE y varios medios lo llaman «presunto agresor» / «agresor abatido»; El Heraldo de México 2026/10/14 titula «civil muerto». **No hay base para agente ni víctima ajena: sigue 🟡.** Fiscal (por cita en La Silla Rota 2026/10/14): **4 detenidos** (uno con orden por secuestro), **2 rescatados**, cateo por un menor desaparecido. **Armamento: 3 largas, 2 cortas**, chalecos y equipo táctico (Servicios Periciales, por cita). **Heridos 3 o 2, contradicho** (titular de El Heraldo: «dos policías heridos»). Comunicado FGE no indexado. **Dato actualizado de 132, no fe de erratas**; su armamento es de la ventana de 132: línea de evento anterior en el módulo, fuera del total |
| **Cotija** (`ARG-132-005`) | **Fecha del hecho: lunes 12-oct al mediodía SOLO POR RESUMEN, y contradicha** (dos consultas de `procedencia-cifras` dieron resultados opuestos); ninguna URL del 12; las fechadas son del 13 (Grupo Marmor, Red Michoacán). **Sin fe de erratas: sigue en 132 con `FRONTERA`**; si aparece fragmento citable del 12, pasa a 131. Sin parte de la Defensa. 3 AK-47 frente a 4 largas de Plan del Cerro: sigue `POSIBLE DUPLICIDAD` |
| **San Blas Atempa** (`ARG-132-003`) | Hora exacta: no publicada («al llegar los alumnos»). Móvil: no informado. Detenidos: ninguno. FGEO: carpeta por homicidio calificado, AEI y Alto Impacto. La víctima era dirigente de una delegación sindical (La Jornada 2026/10/14). Marcha de la CNTE (UnoTV, sin fecha). **Sin cambio de color**; decisión del destinatario pendiente |
| **«El Cromo»** (`ARG-132-006`) | **Fecha de la captura no publicada.** Figura en el boletín federal de las acciones del **13-oct** (republicadores, por resumen): captura el 13-oct o antes. El Siglo de Torreón la fecha el 13 (resumen). Órdenes: **2 documentadas por homicidio calificado + 1 «en registros de inteligencia»** (El Universal Oaxaca, por resumen); el «tres» del titular de El Imparcial no equivale a tres órdenes verificadas |
| **Doctor Coss** (`ARG-132-REC-003`) | ~16:00 del **lunes 12-oct**, por resumen que lo atribuye a El Universal; ninguna URL con fecha. Sin comunicado de Fuerza Civil. Sigue **131 (130 si fue antes de las 08:19)** |
| **Escuinapa, Pueblo Nuevo** (`ARG-132-REC-005`) | Boletín de `sspsinaloa.gob.mx` fechado «a 12 de octubre», «este lunes 12»; hora no publicada. Desglose del boletín por resumen: 3 detenidos, 2 cortas 9 mm, 2 cargadores, 18 cartuchos, 2 motocicletas. **Sigue 130 o 131** |
| **Acaponeta** (`ARG-132-REC-004`) | Hora: no hallada. FGE Nayarit sin comunicado (dominio no devuelto). **Meganoticias 778257 agrupa dos hechos**: Acaponeta (3 cuerpos, 11-oct) y **una fosa en Tecuala** (al menos 4 cuerpos, viernes 9-oct; NTV 2026/10/09). La fosa no es de Acaponeta → **`ARG-133-REC-007`**. Tecuala: NTV 2026/10/09, Nayarit Noticias 2026/10/10 y NTV 2026/10/11 («suman cinco hallazgos este domingo») |
| **Horas del 11-oct** | Nacajuca: «madrugada del domingo 11», Diario de Tabasco 2026/10/11 (sin hora citable; apunta a antes de las 08:58 → 129). Parral: ~03:00-05:00 por resumen. Sin hora citable en ninguno |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| Totolapan (`ARG-131-002`) | **«El Güero Gym» no recapturado.** Fiscalía de Morelos investiga a **10 personas** por el secuestro de tres agentes (Potosinoticias 2026/10/14, por *slug*); ningún detenido. Policías muertos en el accidente: 4, **de la Guardia Nacional** según SDPnoticias (por resumen); sigue siendo accidente |
| «El Cabra» (`ARG-131-006`) | Anuncio del 12-oct (Infobae, Proceso, El Financiero 2026/10/12); captura sin fecha publicada. Sin cambio |
| Minatitlán (`ARG-129-001`) | **Pemex: 2 trabajadores lesionados** (La Jornada 2026/10/11, El Independiente 2026/10/12); Infobae 2026/10/11: «vigilante muerto y otro herido»; 2 muertos solo en Turquesa News y El Congresista. El «1 muerto» de la FGE no se localizó. **Saldo sin arbitrar** |
| Parral | Fiscalía Zona Sur: **0 muertos y 3 lesionados**, solo por resumen (Código 13, Chihuahua al Día); sin comunicado leído |
| Ciudad Juárez (`ARG-130-008`) | Publicación del 11-oct (diario.mx, El Diario de Chihuahua, La Opción); fecha del hecho 10 u 11-oct sin fijar |
| Zamora (`ARG-129-REC-001`) | atiempo.mx «Sube a cinco…» (*slug*, sin fecha): **5** por *slug*; 4 en otros. Sin URL con fecha: no se arbitra |
| Otatitlán | Sin novedad; Fiscalía Regional de Cosamaloapan; sin detenidos |
| Abdón «N» | Anuncio del 13-oct (Imagen del Golfo 20261013, por resumen) sin municipio ni fecha. **Posible caso homónimo** con «La Tecolota», capturado en Coscomatepec (Hora Cero 2026/09/14): no se integra |
| Istmo de Oaxaca | **Mixtequilla: noche del lunes 5-oct** (Diario de Yucatán 2026/10/06) · **Petapa: 11 o 12-oct**, contradicho, sin URL con fecha · **La Ventosa: sábado 10-oct ~16:00** (Primera Línea 2026/10/10). Todos de ventanas anteriores; ninguno acredita ataque a la persona de una autoridad. Sin ficha |
| Sonora, operación citada el 14-oct | **Puerto Peñasco, 21-sep** (Tribuna, Crónica, El Imparcial 2026/09/21): evento anterior, **se cierra** |
| Acapulco «El Junior» | Inventario: 2 armas sin desglose, solo por resumen. Sigue cualitativo |
| Cancún SM 225 | Cateo del 8-oct (5 largas, «más de mil cartuchos», sin URL con fecha) y operativo «Gota a Gota» (Por Esto 2026/10/12: 9 detenidos, 24 armas, sin desglose): `POSIBLE DUPLICIDAD`, fuera de ventana |
| Santiago Tulantepec | **Individualización aplazada al 21-oct** (La Silla Rota 2026/10/14 «Otro retraso…»; la fecha 21, solo por resumen) |
| Chipilo, Pachuca, Azcapotzalco, Jacona, El Castillo | Sin acto nuevo. El Castillo (Xalapa): hecho del 13-oct, fuente única sin fecha |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Atotonilco de Tula** (`ARG-133-001`) | 🔴 por fosa. Boletín de la Comisión de Búsqueda informado «la madrugada de este miércoles 14», solo por resumen: el aviso pudo ser anterior a las 08:19 → `FRONTERA` (publicado el día de cierre de 132, sin hora fijada; se integra en la edición que lo ve primero) |
| **Salamanca** (`ARG-133-002`) | 🔴 por homicidio múltiple. «Minutos antes del mediodía», solo por resumen; `FRONTERA` por la regla (día de cierre de 132). **Detenidos contradichos**: AM plural (resumen), Milenio uno (resumen), El Congresista ninguno |
| **Romita** (`ARG-133-003`) | 🔴. Segunda fuente sin fecha (Azteca Bajío): **★★☆☆☆** (homologado con `ARG-133-007`, `editor-duplicidad` 5). Sexo del herido contradicho. Noche del 14: dentro de ventana |
| **Iztapalapa, tianguis** (`ARG-133-004`) | **🔴 por víctimas múltiples (1 muerta y heridos ajenos), como Cócorit en 126; decisión revisable por el destinatario** (la escala no fija si los heridos cuentan: `ARG-120-009` fue 🟡). **Heridos 3, 2 o 1, contradicho por titular**. Edad de la víctima y del detenido, solo por resumen / *slug* sin fecha. Detención en la misma ventana: ficha propia `ARG-133-008` 🟢 |
| **Irapuato, bar Continental** (`ARG-133-010`) | **Hallado por `procedencia-cifras`; la ola lo omitió.** 🔴 por homicidio múltiple: 2 muertos y 4 lesionados por titular (Periódico Correo 2026/oct/15, 169164). Hora: antes de las 00:21 del 15-oct por el sello de Milenio (resumen). ★★☆☆☆ |
| **Escuinapa, doble ataque nocturno** (`ARG-133-011`) | **Hallado por `procedencia-cifras`.** 🟡: 1 muerto (falleció en el hospital) y 1 herido grave; Luz Noticias 2026-10-15 (309946). Noche del 14 solo por resumen. ★★☆☆☆ |
| **Escuinapa, exdirigente ganadero** (`ARG-133-005`) | 🟡 por homicidio doloso único: cargo gremial, no servidor público; ejecución en vía pública sin acreditación de propósito de aterrorizar |
| **Tijuana** (`ARG-133-006`) | 🟡: la autoridad inicia (alto a un vehículo con reporte de robo) y es agredida; sin muerte de personal |
| **Cancún, Región 201** (`ARG-133-007`) | 🟡, ★★☆☆☆: una sola fuente con fecha (Por Esto 2026/10/14) y dos sin fecha |
| **«La Patrona»** (`ARG-133-009`) | 🟢. Fecha de la detención no publicada: `FRONTERA`. Vértigo Político (GN, SSPC, Defensa en Ciudad del Carmen) puede ser otro hecho: corporación solo por resumen |
| **Pénjamo** (`ARG-133-REC-001`) | **Desde ~05:35 del 14-oct** (AM, por resumen; «en menos de una hora», titular de agoragto): **ventana de 132, omisión**. 🔴 por homicidio múltiple; «narcobloqueo» en el titular de AM |
| **Silao** (`ARG-133-REC-002`, `ARG-133-REC-003`) | Dos hechos: **Sopeña** (🟡, homicidio único + 1 privado de la libertad; **hora contradicha**: 06:00, 06:40, antes de 07:15 o N+ después de las 09:00) y **Veta de Ramales** (🔴, 2 muertos; ~07:20 o reporte ~08:00). Asignados a **132** con reserva: si cualquiera fue después de las 08:19, es de 133 |
| **Escuinapa, Malecón** (`ARG-133-REC-004`) | ~19:20 del 13-oct → **132**. Recuperación por anclaje posterior (132 lo dejó como candidato) |
| **Cajeme** (`ARG-133-REC-005`) | Madrugada del 13-oct (resumen) → antes de las 07:23 → **131** (132 si fue después). Medios Obson 2026/10/13 ancla la publicación al 13. 🟡: iniciador no determinado; el muerto en el vehículo no mueve el color |
| **Jerez** (`ARG-133-REC-006`) | Hallazgo del domingo 11-oct por resumen (ABC Noticias 2026/10/14; ECOdiario sin fecha, zona Los Bosques) → **129 o 130**. ★★☆☆☆. No es el caso de «cuatro cuerpos en fosas» de Imagen Zacatecas |
| **Tecuala** (`ARG-133-REC-007`) | Viernes 9-oct (NTV 2026/10/09) → **128** (127 si antes de las 07:20). ★★☆☆☆ |
| **Querétaro, Sinergia** | Cateos de **madrugada** del 14-oct (`fiscaliageneralqro.gob.mx/portal/2026/10/14/…`, 10 detenidos por titular): ventana de 132. **No se ficha** (verde de ventana anterior): línea de evento anterior en el módulo de armamento |
| **«El Wicho», Villa Unión** | Captura del **13 o 14-oct, contradicho** (comunicado citado por Infobae: 13; otras notas: 14); el boletín federal del 13-oct lista una detención en Villa Unión sin nombre. **Hora no fijada: no se integra a ninguna edición** hasta fijar fecha; línea de evento anterior. **Homónimo**: no es el «El Wicho» de `ARG-113-REC-001` / `ARG-114-FE-001` (Tocumbo, abatido) |
| **Sentencias** | **Ninguna integrable.** FGR Chihuahua (Daniel «N», 8 años; 860 Líder Informativo 2026/10/14) y FGR Sinaloa (Línea Directa 2026-10-14): publicadas en la ventana, sin boletín oficial → candidatas. Oaxaca 80 años: boletín del 13-oct por resumen; El Heraldo de México 2026/10/14 |

## 8. Fe de erratas (no va al cartelón)

- **Cotija (`ARG-132-005`): sin fe de erratas.** El «lunes 12» solo por resumen y contradicho (§5). Sigue en 132 con `FRONTERA`.
- **`ARG-133-FE-001`** — **Omisiones de ARGOS 132**: Pénjamo (🔴), Silao Veta de Ramales (🔴) y Silao Sopeña (🟡), salvo que alguno se fije después de las 08:19;
  Escuinapa Malecón (🟡, anclaje posterior); verde no fichado: Querétaro (Sinergia). «El Wicho» queda fuera (fecha 13 o 14). **Conteo de 132 recalculado, cálculo
  propio**: rojos 1 → **3**; amarillos 4 → **6**; verdes 1 → **2**. Muertos por agresión 3 → **10** (Pénjamo 3, Ramales 2, Sopeña 1, Malecón 1).
- **`ARG-133-FE-002`** — **Omisión de ARGOS 131** (132 si fue después de las 07:23): Cajeme (🟡). 131 amarillos (tras `ARG-132-FE-001`) 3 → **4**; **+1 muerto** en una
  persecución, sin calificar como agresor ni víctima. Los muertos de 131 no se recalculan por otra vía.
- **`ARG-133-FE-003`** — **Omisiones de 129-130 y 127-128**: Jerez (🔴, 129 o 130) y Tecuala (🔴, 128 o 127); se asignan cuando se fije la hora.
- **Actualización de dato, no fe de erratas**: Orizaba (4 detenidos por titular; 3 largas y 2 cortas solo por resumen; El Buen Tono, «cuatro armas»; muerto «presunto
  agresor»); Navolato (inicio 13-oct); Acaponeta (la fosa de Meganoticias 778257 es de Tecuala); Tulantepec (aplazada al 21-oct).

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | **hecho** (`ARG-133-006`) | NO REVISADA (solo medios) | SRIV (`fgebc.gob.mx`, boletines viejos) |
| Baja California Sur | SRIV | NO REVISADA (dominio no devuelto) | NO REVISADA (`procuraduriabcs.gob.mx` no devuelto) |
| Sonora | `ARG-133-REC-005` | NO REVISADA (dominio no devuelto) | NO REVISADA (`fge.sonora.gob.mx` no devuelto; sexta edición) · Nogales, fuera |
| Chihuahua | SRIV · seguimientos Parral y Juárez | SRIV (`fiscalia.chihuahua.gob.mx`, nota sin fecha) | NO REVISADA (estatal) · FGR, candidata |
| Sinaloa | **hechos** (`ARG-133-005`, `-011`) · `ARG-133-REC-004` · seguimiento Navolato | SRIV (`sspsinaloa.gob.mx`; Pueblo Nuevo, 12-oct) | NO REVISADA (sexta edición; republicadores) · FGR, candidata |
| Durango | SRIV | SRIV (`fiscalia.durango.gob.mx`) | SRIV (`fiscalia.durango.gob.mx`, 5 y 7-oct) |
| Coahuila | SRIV | SRIV (`sitio.fgecoahuila.gob.mx`, ago) | NO REVISADA |
| Nuevo León | SRIV · seguimiento `ARG-132-REC-003` | SRIV (`nl.gob.mx`) | SRIV (`fiscalianl.gob.mx`) · 155 años, fuera |
| Tamaulipas | SRIV (Reynosa, Actrices Mexicanas, 12-13 oct sin URL con fecha) | SRIV (`tamaulipas.gob.mx`, `fgjtam.gob.mx` 10-oct) | NO REVISADA |
| San Luis Potosí | SRIV · balance GCE (agregado) | NO REVISADA (dominios no devueltos) | NO REVISADA |
| Zacatecas | `ARG-133-REC-006` | SRIV (`ssp.zacatecas.gob.mx`, 26-sep) | SRIV (`fiscaliazacatecas.gob.mx`) · Juan «N», fuera |
| Jalisco | SRIV · Tonalá (13-oct, sin URL con fecha) | NO REVISADA | NO REVISADA |
| Colima | SRIV | NO REVISADA | NO REVISADA |
| Nayarit | `ARG-133-REC-007` · seguimiento Acaponeta y La Curva | NO REVISADA | NO REVISADA (`fiscalianayarit.gob.mx` no devuelto) |
| Aguascalientes | SRIV | SRIV (`fiscalia-aguascalientes.gob.mx`, 2-oct) | NO REVISADA |
| Michoacán | SRIV · seguimiento Cotija y Zamora | NO REVISADA (`ssp.michoacan.gob.mx` no devuelto) | NO REVISADA |
| Guanajuato | **hechos** (`ARG-133-002`, `-003`, `-010`) · `ARG-133-REC-001` a `-003` | SRIV (`boletines.guanajuato.gob.mx`, 1, 6 y 11-oct) | SRIV (`portal.fgeguanajuato.gob.mx`) |
| Ciudad de México | **hechos** (`ARG-133-004`, `-008`) | SRIV (`ssc.cdmx.gob.mx`, menú con boletín del 14-oct sin texto) | NO REVISADA (`fgjcdmx.gob.mx` no devuelto) |
| Estado de México | SRIV · seguimiento Naucalpan | SRIV (`sseguridad.edomex.gob.mx`, 26-sep) | SRIV (`fiscaliaedomex.gob.mx`) |
| Morelos | SRIV · seguimiento Totolapan | SRIV (`fiscaliamorelos.gob.mx`) | SRIV (`fiscaliamorelos.gob.mx`) |
| Puebla | SRIV · seguimiento FGE | NO REVISADA | SRIV (`fiscalia.puebla.gob.mx`, feb-2026) |
| Tlaxcala | SRIV (Tlaxco, sin fecha) | NO REVISADA | NO REVISADA |
| Hidalgo | **hecho** (`ARG-133-001`) · Tulantepec | NO REVISADA (`hidalgo.gob.mx` no devuelto) | NO REVISADA |
| Querétaro | SRIV | **Publicó** (`fiscaliageneralqro.gob.mx`, 14-oct: ventana de 132) | SRIV (5, 6 y 8-oct, fuera) |
| Veracruz | SRIV · seguimiento Orizaba, Minatitlán, Otatitlán | SRIV (`veracruz.gob.mx`) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | SRIV · «El Cabra», Nacajuca | NO REVISADA (`tabasco.gob.mx` no devuelto) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | SRIV (Zihuatanejo, 13-oct, sin URL con fecha) | SRIV (`fiscaliaguerrero.gob.mx`) | SRIV (`fiscaliaguerrero.gob.mx`) |
| Chiapas | SRIV | SRIV (`fge.chiapas.gob.mx`) | SRIV (`fge.chiapas.gob.mx`) |
| Oaxaca | SRIV · seguimiento San Blas Atempa e Istmo | SRIV (`portal.fgeo.gob.mx`, `sspo.gob.mx`) | **Publicó, no integrable** (`portal.fgeo.gob.mx`, boletín 2,889) |
| Campeche | **hecho** (`ARG-133-009`) | SRIV (`spsc.campeche.gob.mx`, nota sin fecha; mismo criterio que Chihuahua) | NO REVISADA |
| Yucatán | SRIV | SRIV (`ssp.yucatan.gob.mx`) | SRIV (`fge.yucatan.gob.mx`, 1-oct) |
| Quintana Roo | **hecho** (`ARG-133-007`) · SM 225 | SRIV (`fgeqroo.gob.mx`) | NO REVISADA |

**Sentencias: 15 de 32** (14 SRIV + Oaxaca); FGR revisada por búsqueda; **17 `NO REVISADA`**. **Armamento: 20 de 32**; 12 `NO REVISADA`. **Alto impacto: 32 de 32, con la franja 00:00–07:16 del 15-oct de cobertura débil** (las búsquedas de madrugada de cinco equipos fueron vacías; `procedencia-cifras` halló dos hechos de la noche del 14). Federales: Marina, FGR y Gabinete SRIV; **GN y Defensa `NO REVISADA`** (dominio no devuelto).

## 10. Hechos vistos y NO fichados, con motivo

- **Zihuatanejo, col. Vicente Guerrero** (13-oct, 1 muerto): sin URL con fecha → candidato (posible omisión de 132).
- **Michoacán, El Guayabo** (padre muerto y niña de 8 años herida grave; atiempo, sin fecha, nota del 14-oct; Contramuro «la noche anterior», Apatzingán o Morelia): fecha y municipio sin fijar → candidato (posible 132).
- **Cancún, SM 254, conductor de plataforma** (madrugada del 14-oct ~02:00, solo por resumen): Quinta Fuerza sin fecha → candidato (132).
- **Reynosa, col. Actrices Mexicanas** (tres hombres asesinados y una mujer en fosa, 12-13 oct por resumen; Excélsior sin fecha): sin URL con fecha → candidato (131-132).
- **Campeche, Ciudad del Carmen, Tierra y Libertad** (hombre herido en riña, Por Esto 2026/10/14): lesiones sin agravante, fuente única.
- **Edomex, Almoloya de Juárez** (agente de la FGR asesinado, 11-12 oct por resumen): sin URL con fecha → candidato 🔴 de ventana anterior.
- **Puebla, Chalchicomula de Sesma** (1 muerto, 1 herido, ~13-oct): sin URL con fecha.
- **Oaxaca, Ciudad Ixtepec** (dos hermanos) y **Juchitán** (tres hombres): El Universal Oaxaca, sin fecha → candidatos.
- **Tlaxcala, Tlaxco** (ataque a vendedores, sin lesionados): sin URL con fecha.
- **Juventino Rosas** (FGR, 3 armas, 239 cartuchos; vinculación): fecha del hecho no fijada. **Tabasco, Centro** (8 vinculados, 5 armas; Infobae 2026/10/15): fecha no fijada.
- **SLP, balance GCE de 24 h** (El Heraldo de SLP 2026/10/14: 38 detenidos, 1 arma sin tipo): agregado.
- **Matamoros, col. Revolución** (4 armas, 9 cargadores, 60 cartuchos) y **Reynosa, Alfredo V. Bonfil** (Nota Tamaulipas 2026/10/12): fuera de ventana.
- **Monterrey, Nueva Topo Chico**: sigue con una sola fuente (MVS 2026/10/13), ventana de 132.
- **Sonora, Puerto Peñasco** (21-sep): evento anterior citado en la conferencia del 14-oct.
- **Sentencias no integradas**: NL Brayan «N» 155 años (MVS 2026/10/13; MVS 2026/10/12 «cuatro… desaparición», cotejar) · Zac Juan «N» 10 años (LJZ 13/10/2026) · Sonora
  Nogales, Mateo «N», 15 años (El Diario de Sonora 2026/10/12) · FGR Chihuahua Lorenzo «N» (12-oct) · Navolato 40 años (12-oct) · Nayarit, Sergio Candelario «N», 53 años
  (NNC, sin fecha) · Tlaxcala, FGR, Juan «N» (1 y 7-oct, posible homónimo) · Querétaro, tres (5, 6 y 8-oct) · SLP (4 y 9-oct) · Yucatán (1-oct).

## 11. Desglose de cálculos propios

- Duración: 14-oct 08:19 → 15-oct 07:16 = **22 h 57 min** = 22,95 h. Densidad: 11 / 22,95 = **0,48**.
- Muertos en hechos propios: Salamanca 2 + Romita 2 + Irapuato 2 + Iztapalapa 1 + Escuinapa 2 (`-005`, `-011`) + Cancún 1 = **10**; cuerpos en fosa, Atotonilco **5**.
  Heridos: Irapuato 4 + Salamanca 1 + Romita 1 + Escuinapa 1 + Iztapalapa 1 a 3 (contradicho) + Tijuana 1 = **9 a 11**.
- Frontera: **7 de 11** (`ARG-133-001`, `-002`, `-005`, `-006`, `-007`, `-009`, `-011`).
- Armamento propio integrable: **0** en todas las categorías.
- Conclusión 1: Pénjamo (~05:35 del 14), Salamanca, Romita, Irapuato (antes de las 00:21 del 15) = **4 ataques con dos o más muertos en 4 municipios, en menos de 24 h**.
- Conclusión 2: Tecuala (9-oct), Jerez (11-oct), Navolato (13-oct) = **3 hallazgos** en cinco días; dos por colectivos (Jerez, Navolato).
- Conclusión 3: `ARG-129-004` (10-oct), `ARG-130-006` y `-009` (11-oct; `-009` podría ser del 12, Infobae por resumen: heredado, no reverificado), `ARG-131-004` (12-oct), `ARG-133-REC-004` (13-oct), `ARG-133-005` y `-011` (14-oct) = **7 homicidios**.
- Fes de erratas: §8.

## 12. Fuentes por ficha

- **`ARG-133-001`** — Institucional 1 (Comisión de Búsqueda de Hidalgo, boletín por cita). Nacional 6: El Financiero 2026/10/14; Infobae 2026/10/14; El Heraldo de México
  2026/10/14; La Silla Rota 2026/10/14 (532951); Milenio; TV Azteca. Regional 4: Quadratín Hidalgo; La Jornada Hidalgo; Criterio Hidalgo; El Universal Hidalgo.
- **`ARG-133-002`** — Nacional 1: El Universal. Regional 6: Periódico AM 2026/10/14 (1854996); Periódico Correo 2026/oct/14 (169080); Meganoticias (779060); Azteca Bajío; Cancha Política; agoragto.
- **`ARG-133-003`** — Regional 2: Periódico Correo 2026/oct/14 (169158); Azteca Bajío (sin fecha).
- **`ARG-133-004`** — Nacional 6: Infobae 2026/10/14; La Razón 2026/10/14; La Jornada 2026/10/14; Crónica 2026/10/14; El Universal; N+. Regional 3: Sociedad Noticias 2026/10/14; Ejecentral; Canal 44.
- **`ARG-133-005`** — Nacional 4: MVS Noticias 2026/10/14 (749836); Infobae 2026/10/14; Excélsior; TV Azteca. Regional 7: Luz Noticias 2026-10-14 («Ejecutan a balazos frente a su hija…»); El Diario de Juárez 2026/oct/14; Tribuna 2026/10/14; Noroeste (IB26502318);
  Quadratín; Meganoticias; Los Noticieristas.
- **`ARG-133-010`** — Nacional 1: Milenio (sello 00:21 del 15-oct, por resumen). Regional 1: Periódico Correo 2026/oct/15 (169164).
- **`ARG-133-011`** — Regional 1: Luz Noticias 2026-10-15 (309946).
- **`ARG-133-006`** — Institucional 1 (SSPCM, versión por cita). Nacional 1: N+. Regional 4: En Línea BC 2026/10/14; Tijuana en Línea 2026/10/14; Periodismo Negro 2026/10/14; Diario Tijuana.
- **`ARG-133-007`** — Regional 3: Por Esto 2026/10/14; Clic Noticias; Periodistas Quintana Roo.
- **`ARG-133-008`** — Institucional 1 (SSC, por cita). Nacional 3: Infobae, La Razón, La Jornada 2026/10/14. Regional 1: Canal 44.
- **`ARG-133-009`** — Nacional 1: Infobae 2026/10/14. Regional 2: La Nigua; Mexican Times.
- **`ARG-133-REC-001`** — Nacional 2: El Universal; N+. Regional 6: Periódico AM 2026/10/14 (1854895); Periódico Correo 2026/oct/14 (169099); Proyecto Puente 2026/10/14; El Vigía
  2026/10/14; Primer Plano Irapuato 2026/10/14; agoragto. (El Heraldo de SLP 2026/10/14 replica.)
- **`ARG-133-REC-002`** y **`-REC-003`** — Nacional 3: El Universal; Milenio; N+. Regional 4: Periódico AM 2026/10/14 (1854942); Periódico Correo 2026/oct/14 (169072); Guanajuato
  Informa; Quadratín Bajío. `-REC-003`, además: Noticieros en Línea 2026/oct/14 (55329).
- **`ARG-133-REC-004`** — Regional 5: Luz Noticias 2026-10-13 (309730); Línea Directa 2026-10-13__1720084; Noroeste (FI26489682); Los Noticieristas; Sinaloahoy.
- **`ARG-133-REC-005`** — Nacional 1: Infobae 2026/10/15. Regional 3: Proyecto Puente 2026/10/14; El Imparcial 2026/10/14; Infoson 2026/10/14 (Crítica, sin fecha).
- **`ARG-133-REC-006`** — Nacional 1: ABC Noticias 2026/10/14 (292453). Regional 1: ECOdiario (sin fecha).
- **`ARG-133-REC-007`** — Regional 2: NTV 2026/10/09; Nayarit Noticias 2026/10/10; NTV 2026/10/11. Meganoticias Tepic 778257 (sin fecha, agrupa dos hechos).

## 13. Los dos controles editoriales

Racha: **veinte pases consecutivos, veinte «CORREGIR»** (dos en el primer pase, uno en el segundo). Lanzados en paralelo sobre la versión estable `ed80848`, con las **notas íntegras de los seis equipos**
(extraídas al *scratchpad*: `informe-{noroeste,noreste,occidente,centro,golfo-federal,sureste}.md`).

**`procedencia-cifras`** (25 búsquedas, 4 `WebFetch` a medios fallidos por DNS) — **CORREGIR**. **Un rojo y un amarillo omitidos** (Irapuato, Escuinapa nocturno).

| # | Hallazgo | Disposición |
|---|---|---|
| 1 | Rojo omitido: Irapuato, bar Continental | **Corregido**: `ARG-133-010` 🔴 ★★☆☆☆ |
| 2 | Amarillo omitido: Escuinapa, doble ataque nocturno | **Corregido**: `ARG-133-011` 🟡 ★★☆☆☆ |
| 3 | FE de 132: muertos 9, no 10 (faltaba Malecón) | **Corregido**: 10 |
| 4 | Iztapalapa: heridos resueltos a 3 | **Corregido**: 1 a 3, contradicho; total 9 a 11 |
| 5 | Cotija: el 12 solo por resumen, contradicho | **Corregido**: **fe de erratas retirada**, sigue en 132 |
| 6 | Silao: horas contradichas no declaradas | **Corregido** |
| 7 | Salamanca: detenidos contradichos | **Corregido** |
| 8-9 | Conclusiones 1 y 3 tras las nuevas fichas | **Corregido**: 4 ataques / 7 homicidios |
| 10 | Totales y densidad | **Corregido**: 11 hechos, 0,48 |
| 11-12 | Edad del detenido y de la víctima, «en que huía» | **Corregido**: *slug* sin fecha / resumen |
| 13 | Alto impacto 32 de 32 sobredeclarado | **Corregido**: franja de madrugada del 15, cobertura débil |
| 14 | Oaxaca «solo por resumen» | **Resuelto**: cláusula retirada (`editor-duplicidad` 1) |
| 15-16 | Jerez y Tecuala: fuentes adicionales | **Corregido** |
| 17 | Orizaba: El Buen Tono, «cuatro armas» | **Corregido** |
| 18 | «SSPC Tijuana» | **Corregido**: SSPCM |
| 19 | El Guayabo | **Candidato** (§10, pendientes) |

**`editor-duplicidad`** (sin búsquedas) — **CORREGIR**. **Ningún duplicado** con 130-132; ningún hecho con dos ARG-ID.

| # | Hallazgo | Disposición |
|---|---|---|
| 1 | Conclusión 5: Oaxaca sin sustento en fuentes | **Corregido**: solo Tulantepec |
| 2 | FE muertos 9 → 10 | **Corregido** |
| 3 | `ARG-133-005`: Nacional 4 (Infobae) | **Corregido** |
| 4 | GN y Defensa sin dominio = `NO REVISADA` | **Corregido** |
| 5 | Romita frente a Cancún: criterio de estrellas | **Corregido**: Romita ★★☆☆☆ |
| 6 | «El Wicho» con fecha contradicha contado en 132 | **Corregido**: fuera de toda cuenta; deslinde de homónimo |
| 7 | Sufijos `-REC-` ambiguos en fuentes | **Corregido**: ID completo |
| 8 | Conclusión 1 incluía Sopeña y Ramales | **Corregido** |
| 9 | Deslindes que explican color | **Corregido**: rótulo breve; explicación aquí (§7) |
| 10 | Portada: «dos hallazgos» | **Corregido**. Acción 5 sobre `ARG-132-002` se mantiene: encargo vivo |
| 11 | Panorama de Iztapalapa sin reserva | **Corregido** |
| 12 | Campeche armamento: `spsc.campeche.gob.mx` | **Corregido**: SRIV; armamento 20 de 32 |
| 13 | Cajeme: alternativa de ventana y muertos de 131 | **Corregido** |
| 14 | Tres nombres para la SSPCM | **Corregido** |
| 15 | Índice, pendientes y §13 | **Corregido** al cierre |

**Segundo pase de `editor-duplicidad`** sobre `07c36f0` (sin web) — **CORREGIR, ajustes menores**: correcciones de §13 verificadas en las cinco superficies; Irapuato y Escuinapa
nocturno sin duplicidad. Corregidos: (1) Conclusión 2, Tecuala sin colectivo acreditado, «cinco días»; (2) `ARG-133-011` con `FRONTERA` (publicado el día de cierre): **7 de 11**;
(3) `ARG-133-005` Regional 7 con Luz Noticias; (4) `ARG-133-REC-007` Regional 2 (NTV es un emisor); (5) Irapuato pasa a la página I. Observación: «Ensenada, pena el 16-oct» sin
respaldo en 132-133: reverificar o cerrar en 134. Tras ello, **PUBLICAR**.


## 14. Herramientas

`tools/datos-argos-133.py` (desde 132; `ARM = []` con tabla «SIN FILAS»; sentencias sin ficha integrada; portada con una solicitud por línea).
`gen-movil.py` y `gen-texto.py` sin cambios. `validar.js`: OK.

## 15. Lecciones de método (no van al cartelón)

1. **La mitad de los hechos violentos del 14-oct son de la ventana de 132**: la madrugada del día de cierre (Pénjamo, Silao, Querétaro) se publica después del cierre.
   La búsqueda de la ventana siguiente es la única que los ve; propuesta: cada equipo hace una búsqueda expresa de «madrugada del día de apertura».
2. **El coordinador volvió a traer el rojo que la ola no traía** (Atotonilco, Romita), sexta edición seguida; los encargos añadidos a los equipos funcionaron.
3. **Una nota que agrupa dos hechos** (Meganoticias 778257, Acaponeta + Tecuala) produjo en 132 una atribución de fosa equivocada: un titular plural no identifica un caso.
4. **Sonora y Sinaloa, sexta edición sin dominio de fiscalía devuelto.**
5. **Umbral de «víctimas múltiples» con un solo muerto** (Iztapalapa): sigue sin fijarse en `CLAUDE.md`.
6. **La ola y el coordinador omitieron un rojo de la noche del 14 (Irapuato) y un amarillo (Escuinapa)**, que halló `procedencia-cifras` por tercera edición seguida:
   las búsquedas de «madrugada del jueves» fueron vacías en cinco equipos. Propuesta para 134: una búsqueda por equipo con la **fecha del día de cierre** en la ruta (`2026/10/15`).
