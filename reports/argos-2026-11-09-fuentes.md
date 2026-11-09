# ARGOS 149 — Archivo de fuentes (corte 2026-11-09)

## 1. Identidad y ventana

- **ARGOS 149**, archivo `argos-2026-11-09.html` (lunes 9-nov-2026).
- **Ventana**: abre **vie 6-nov 07:30 CDMX** (cierre de ARGOS 148) y cierra **lun 9-nov 16:07 CDMX**.
  - Bloque 0 a las **08:14**. El «Procede» llegó a las **16:07**, 7 h 53 min después.
  - Por la regla de las dos horas se propuso cerrar a la hora del «Procede», y el destinatario respondió «A las 1607».
  - La orden de 149 fechada el sábado 7 no se ejecutó, así que no hay hueco entre ventanas.
- **Duración**: **80 h 37 min**, cálculo con `date`.
  - Densidad: **21 / 80,6 h = 0,26 hechos/hora**.
  - Rojos: **7 / 80,6 h = 0,09 rojos/hora**.
  - Ambas son cálculo propio.
  - La ventana es **3,7 veces la de 148** (21 h 48 min) e incluye un fin de semana completo. Sus totales no son comparables sin más.
- **Calendario día por día**:
  - vie 6 (desde las 07:30)
  - sáb 7
  - dom 8
  - lun 9 (hasta las 16:07)
  - `WINDOW_DAYS = 4`, cambiado en el script del cartelón y en la aserción del generador.
- **Ciclo de rotación aplicado: A (Noroeste + Centro)**, después de la prioridad sobre el ciclo.
  - **Resultado de la prioridad en sentencias**: de las 11 fiscalías `NO REVISADA` de 148 (BC, BCS, Son, Chih · NL, Zac · CDMX, Edomex, Pue, Mor, Tlax), las 11 quedaron revisadas.
  - Coahuila quedó revisada con dominio hallado: `sitio.fgecoahuila.gob.mx`.
  - **Resultado en armamento**: CDMX quedó revisada (`ssc.cdmx.gob.mx`), Sin y Dgo también, Coah y Col también. Edomex sigue `NO REVISADA` por **tercera edición**; BC, BCS y Son siguen `NO REVISADA` (BC y Son sin dominio SSP confirmado).
  - **Qué aportó el ciclo**: la región Noroeste cerró las seis fiscalías de su región en sentencias, y Centro las cinco de su prioridad. **Ninguna** sentencia resultó integrable.
- **Red**: `curl -s -o /dev/null -m 12 -w '%{http_code}' https://www.gob.mx/fgr` devolvió `000` a las 08:14 (proxy: `connect_rejected`).
  - Egreso bloqueado: solo WebSearch.
  - El techo de política es ★★★★☆; esta edición no supera ★★★☆☆.
- **Rama**: `claude/zealous-mendel-baacj5`.
  - Arrancó en `e19b060` (orden de 144). Las diez fusiones de la orden fueron *fast-forward*, y las cinco primeras ya estaban contenidas.
  - 282 archivos en `reports/` al arrancar.

## 2. Decisión del destinatario (9-nov)

| Decisión | Respuesta | Aplicación |
|---|---|---|
| Cierre de ventana con «Procede» 7 h 53 min después del Bloque 0 | **«A las 1607»** | Ventana 6-nov 07:30 → 9-nov 16:07 (80 h 37 min) |

## 3. Fe de erratas a ediciones anteriores

En el cartelón van sin código FE, porque `gen-movil.py` prohíbe referencias `-FE-`.

| ARG-ID | Edición afectada | Corrección |
|---|---|---|
| `ARG-149-FE-001` | ARGOS 148 | **`ARG-148-003` (Navolato) pasa de 🟡 a 🔴**. Titulares: «Agresión contra militares deja a 3 integrantes de una célula delictiva abatidos… confirma Harfuch» (Losnoticieristas 2026/11) y «Harfuch confirma tres presuntos sicarios abatidos…» (Luz Noticias 2026-11-06). «Recorrido de reconocimiento entre Las Trancas y La Primavera» y «ocupantes de un Jeep» constan solo por resumen. Quién inició: versión del secretario a través de medios; el comunicado de Defensa no está indexado. El pendiente de 148 pedía ese comunicado; se sube a 🔴 por la declaración nombrada en titulares, con reserva. El titular de PorEsto que citó el equipo Noroeste no lo reencontró procedencia. **Semáforo corregido de 148: 3 rojos, 2 amarillos, 4 verdes** |
| `ARG-149-FE-002` | ARGOS 148 | **`ARG-148-008`**: el tramo de Tacámbaro coincide con Pedernales (3-nov; RED Michoacán 2026/11/03; réplica Potosinoticias 2026/11/06). Se retira por posible duplicidad. Sin efecto numérico, porque era un renglón cualitativo. Queréndaro y Cotija siguen sin fecha |
| `ARG-149-FE-003` | ARGOS 148 | **`ARG-148-002`**: saldo fijado en **2 muertos**; la segunda víctima murió en una clínica del IMSS (Síntesis 2026/11/05; Diario Puntual 2026/11/05; Meganoticias 785870; Cinco Radio). Hora sin fijar; la cláusula sigue abierta. Sin efecto en los totales de 148, que ya contaban 2 |
| `ARG-149-FE-004` | ARGOS 148 | **`ARG-148-006`**: los 4 detenidos se atribuyen a la SSPH por titular («SSPH informa sobre la detención de cuatro personas tras hechos en la colonia Real de Minas», Plaza Juárez; «SSPHidalgo detiene a 4…», PulsoSur). Fueron 3 hombres y 1 mujer, en Téllez, Zempoala (solo por resumen) |
| `ARG-149-FE-005` | ARGOS 148 | El **boletín federal del 5-nov existía** (Milenio `…-5-de-noviembre-2026`; RED113; Tallapolítica) e incluía Tlachichuca (🟢, 11 zonas, 4,132 mdp estimados). ARGOS 148 lo declaró sin indexar, que era la casilla correcta en su momento. No se recupera por ser 🟢 |
| — | ARGOS 148 | **`ARG-148-001`**: se mantiene 🔴. Según la SSPH era «elemento de la Policía Estatal» fuera de servicio (Plaza Juárez, solo por resumen); no hay declaración oficial de baja |
| — | ARGOS 148 | **`ARG-148-004`**: el Gabinete confirma el segundo abatido («junto con otra persona», solo por resumen). Identidad no confirmada: El Universal da «El Ronco», exdirector operativo de la fiscalía mexiquense. Corporaciones: SSPC, AIC-FGR y CNI. El comunicado del 6-nov «agresión repelida en el Estado de México» es este hecho por contenido. Armamento sin cifra |
| — | ARGOS 148 | **`ARG-148-007` (Morelia)** y **`ARG-148-009` (Marina)**: día no fijado; las cláusulas siguen abiertas sin cambio |

## 4. Boletín federal (triple consulta)

- **Acciones del 5-nov**: existe (Milenio; RED113; Tallapolítica). Corresponde a la ventana de 148 (ver FE-005).
- **Acciones del 6, 7 y 8-nov**:
  - **Al inicio** (16:07-16:20): `SIN RESULTADO INDEXADO EN VENTANA` en día suelto, rango y título.
  - **Al cierre** (16:25): por título, sin restricción de dominio, apareció el **agregado del 6, 7 y 8**. Lo publica un **republicador único**, Milenio (`https://www.milenio.com/policia/acciones-relevantes-de-gabinete-de-seguridad-6-7-8-de-noviembre-2026`). Contenido solo por resumen.
  - Ni Tallapolítica, ni RED113, ni gob.mx/sspc lo republican. La corroboración es **débil por construcción**.
  - Del agregado salen `ARG-149-018` (Zapopan), `-020` (Sanalona) y `-021` (Escuinapa).
  - Se ven sin ficha, porque solo constan por resumen: Zitácuaro (laboratorio), Tepeyahualco (laboratorio, 2 detenidos), Nuevo Laredo (3 cateos, 2 detenidos, uno con orden de extradición, armas sin cifra) y Tlachichuca (otra acción en Agua Escondida El Salitrero, 95 mdp: contradice los 4,132 mdp).
  - Baila, Culiacán (laboratorio, 34 mdp) consta por titular de Losnoticieristas, pero es un 🟢 sin ficha.
- `gabinetedeseguridad.gob.mx` muestra en portada los comunicados conjuntos del 6-nov (laboratorio en Puebla y agresiones repelidas en Sinaloa y Edomex), solo por resumen. Son de hechos de la ventana de 148.

## 5. Resolución de encargos

- **Cláusulas de retiro de 148**:
  - `-002` Atencingo: hora no fijada (mañana, mediodía o tarde, solo por resumen); saldo fijado (FE-003).
  - `-007` Morelia: día no fijado (red113 2026/11 sin día).
  - `-008`: tramo de Tacámbaro retirado (FE-002).
  - `-009` Marina: día de las dos operaciones no fijado (todas las fuentes, 5-nov). Se conserva.
- **Color de `ARG-148-001`**: se mantiene 🔴 (ver §3).
- **Reservas de 148**: `-003` sube a 🔴 (FE-001); `-004`, segundo abatido confirmado; `-006`, cifra atribuida a la SSPH por titular (FE-004).
- **Vistos sin ruta**:
  - Chilpancingo, Urvan (col. Tribuna Nacional): 5-nov ~18:30, solo por resumen; 1 muerto (el chofer); 4 o 2 heridos. Es de la ventana de 148, 🟡, así que queda visto y no se recupera.
  - Reynosa, Puerta Sur / Nuevo México ITAVU: sin día con ruta (La Verdad 2026/11; Info7 «tres nuevos sitios… hallazgo 47»). Rojo sin ruta; misma zona que ARG-140-008.
  - Valle de Chalco (San Miguel Xico): anterior al 6-nov. Por resumen sería «viernes 31-oct», pero el 31 fue sábado, así que la fecha no es fiable.
- **Sentencias candidatas**: ninguna integrable (ver §7 y el cartelón).
  - Oaxaca 157 años: `portal.fgeo.gob.mx` responde, pero no aparece el boletín 2,948.
  - Palenque 65 años: `fge.chiapas.gob.mx` responde, pero el caso no aparece.
  - FGR Paraíso: pena 2 años o 2 años 8 meses, sin boletín.
  - Los Ramones y Saltillo–Monclova: 4-nov, fuera de la ventana.
  - Fresnillo: octubre.
  - Jalisco, dos feminicidas: 29-30 oct.
  - Huejotzingo: 29-oct.
  - Ecatepec: 28-oct.
  - Tulantepec: la audiencia de individualización del 5-nov no tiene resultado indexado.
  - Tecate y Mexicali: `fgebc.gob.mx`, último boletín indexado del 19-sep.
- **Seguimientos**:
  - Matamoros (ARG-145-REC-001, en la jornada de ARG-144-008): «bala que mató a la niña… fue disparada desde helicóptero estatal, admitió la Fiscalía» (Infobae 2026/11/06); «Fiscalía de Tamaulipas investiga a tres policías» (Infobae 2026/11/07); tirador no identificado.
  - «El Panda» (Coatzacoalcos, causa 94/2026): resultado de la audiencia del 9-nov no indexado. Pista: hoyxalapa 2026/11/09.
  - Orizaba ARG-132-002: vinculación del 22-oct (Golpe Político 2026/10/22; La Silla Rota 2026/10/22), causa 588/2026.
  - Cuernavaca ARG-147-001: sin detenidos; el fiscal evalúa citar a cabildo y magistrados (La Jornada 2026/11/07); piden que la FGR atraiga el caso (La Silla Rota 2026/11/9).
  - Indaparapeo ARG-147-004: sin desarrollo. Hay 6 detenidos por delitos contra la salud (Grupo Marmor 2026/11/08), pero es otro hecho, 🟢 sin día.
  - Champotón ARG-147-REC-001: sin desarrollo; «dos detenidos», por titular de La Jornada Maya, sin autoridad nombrada.
  - Tijuana ARG-143-005 y Mexicali ARG-145-003: sin novedad.
  - Mexicali ARG-146-011: 26 fosas y 51 hallazgos (cifra de la fiscal, solo por resumen; Zeta 2026/11); 27 cuerpos (Baja Post 2026/11/07); 27 identificados (El Imparcial 2026/11/04).

## 6. Fuentes por ficha (lista íntegra)

Criterio de recuento: un emisor por nota propia. Meganoticias y las ediciones estatales cuentan como regionales. Las republicaciones de un mismo comunicado cuentan como una fuente.

| ARG-ID | Fuentes (con URL o ruta) |
|---|---|
| 001 | Correo 2026/nov/07 «ataque armado contra militares en Valtierrilla deja al menos tres elementos lesionados» · Correo 2026/nov/08 «muere uno de los militares atacados» · AM 2026/11/08 · Meganoticias 786746 · Agoragto «muere uno de los tres soldados heridos en emboscada en Valtierrilla» · Noticieros en Línea 2026/nov/08 |
| 002 | AM 2026/11/07 («tras salir de su turno») · Correo 2026/nov/07 («en su día de descanso») · Meganoticias 786632 · Telediario · La Silla Rota 2026/11/8 · Notus · Guanajuato Informa · Agora |
| 003 | AM 2026/11/07 · Correo 2026/nov/07 · Telediario · Milenio · N+ · Potosinoticias 2026/11/09 (réplica) |
| 004 | El Financiero 2026/11/08 · AM 2026/11/08 · Correo 2026/nov/08 · La Silla Rota 2026/11/9 · Guanajuato Informa · Zona Franca · Blog del Narco (abierta, NO OFICIAL; no cuenta) |
| 005 | La Jornada 2026/11/08 (dos secciones) · El Financiero 2026/11/08 · Proceso 2026/11/8 · La Silla Rota 2026/11/8 · Expansión 2026/11/08 · ABC Noticias 2026/11/8 · Diario de Yucatán 2026/11/08 · Infobae/EFE 2026/11/08 · Vanguardia 2026/11/08 · Intolerancia 2026/11/08 · Demócrata Coahuila 2026/11/08 · El Imparcial 2026/11/09 · El Chamuco 2026/11/09 · Hoy Tamaulipas 632206 · San Luis Hoy · Zócalo |
| 006 | Línea Directa 2026-11-08 · Síntesis 2026/11/09 · Proyecto Puente 2026/11/09 · La Silla Rota 2026/11/9 · López Dóriga · Sinaloa Hoy · Noroeste (informe diario «6 cuerpos hallados el domingo»; «Confirma Fiscalía hallazgo de equipo táctico») |
| 007 | Línea Directa 2026-11-07 · Luz Noticias 2026-11-07 · Noroeste · Café Negro · Viva la Noticia · Sinaloa Hoy |
| 008 | Correo 2026/nov/08 · AM 2026/11/08 («persecución con soldados») · Milenio · N+ · Notus |
| 009 | El Diario de Chihuahua 2026/nov/08 · En Blanco y Negro 2026/11/08 · El Pueblo 20261108 («acribillan a 2») |
| 010 | Proyecto Puente 2026/11/07 (fuente única) |
| 011 | Periodismo Negro 2026/11/07 (fuente única) |
| 012 | Vanguardia 2026/11/07 · José Cárdenas 2026/11 · El Universal Oaxaca |
| 013 | La Aldea de la Información 2026/11/09 · N+ · Vanguardia de Veracruz · La Nigua · El Buen Tono |
| 014 | Quinto Poder 2026/11/08 · El Imparcial 2026/11/09 («…tras enfrentamiento armado que dejó dos heridos») · Meganoticias 786804 («tras ataque a elementos») · Rotativo («un marino herido») |
| 015 | gob.mx/sspc (comunicado de Marina, ruta sin fecha, texto no leído) · Diario Puntual 2026/11/07 · Latinus 2026/11/8 · Infobae 2026/11/08 («más de 600 kilos») · Retodiario 2026/11/08 · Aristegui 0811 · SinEmbargo · Excélsior · Capital México |
| 016 | Changoonga 2026/11/08 · La Voz de Michoacán · IMN México · El Clarín · Contramuro · A Tiempo |
| 017 | El Imparcial 2026/11/08 · En Línea BC 2026/11/08 · Uniradio («dos fusiles abastecidos») |
| 018 | Quinto Poder 2026/11/08 y 2026/11/09 · Infobae 2026/11/09 · El Imparcial 2026/11/09 · Noticias PV · Milenio (agregado 6-8, por resumen) |
| 019 | Infobae 2026/11/09 · Proceso 2026/11/9 · La Razón 2026/11/09 · MVS 2026/11/9 · Diario de Yucatán 2026/11/09 · Aristegui 0911 · Yahoo · Mimorelia · Acrópolis · UnoTV · Quadratín México · 24 Horas |
| 020 | Milenio (agregado 6-8, por resumen) · Meganoticias 786916 («aseguran seis armas, mil 260 cartuchos y cocaína en Sanalona») · Losnoticieristas 2026/11 (ID 1163954) |
| 021 | Milenio (agregado 6-8, por resumen) · Losnoticieristas 2026/11 («caen tres personas, una menor de edad, con cinco armas largas en Escuinapa», ID 1163990) |

## 7. Procedencia: decisiones de clasificación

- **Tlachichuca retirado** como ficha propia. Su operativo aparece en el boletín federal del 5-nov y lo anunció el secretario el 6 sin hora. Queda como evento anterior publicado durante el corte (🟢), en vistos.
- **Zapopan, en dos fichas.** El delito y la detención caen en la misma ventana:
  - `-014`: enfrentamiento, 🟡. La autoridad ejecutaba una orden en un inmueble y fue repelida; el inicio del fuego consta según la versión oficial. Hubo un marino herido, sin muertes de personal.
  - `-018`: detención, 🟢.
- **Valtierrilla**: 🔴 por emboscada y muerte de personal, con independencia de quién inició. Los 3 lesionados incluyen al fallecido, así que el saldo es 1 muerto y 2 heridos. Es una secuencia, no una contradicción.
- **Río Bravo**: 🔴 por secuestro de servidor público.
  - Se asigna a SLP en el mapa porque así lo sitúan dos fiscalías (Tamaulipas y Zacatecas), con reserva de lugar.
  - La localización con vida no tiene ficha verde por la contradicción entre rescate y fuga.
- **Cuerámaro**: el comandante murió por un disparo de su arma de cargo, presunta autolesión según el gobierno municipal (solo por resumen). No es hecho del corte.
- **Juchitán**: 🟡. Es una agresión contra el negocio de un periodista bajo protección federal, sin víctimas. La lista roja exige víctima.
- **Buenavista**: los 7 «explosivos de fabricación casera para lanzarse desde drones» (por titular) se clasifican como **AEI** (artefacto para dron), por inferencia de clasificación declarada. Capacidad no dictaminada.
- **Sanalona**: se integran 6 armas como **sin categoría** porque el desglose 3/3 es solo por resumen. Los 1,260 cartuchos van por titular.
- **Escuinapa**: 5 largas y 3 detenidos por titular de medio, más el boletín federal por resumen. Los cargadores (29) y los cartuchos (435) quedan n/d.
- **Cláusulas de retiro** en Atempan, Buenavista, Sanalona y Escuinapa (NRET 4): el día no está fijado y cualquiera de ellos podría ser anterior a las 07:30 del 6.
- **Frontera de ventana** en Cosoleacaque y Acapulco (NFR 2): publicados el día de cierre sin hora.
- **Rojos sin ruta, candidatos no fichados**:
  - San Juan Cacahuatepec (2 muertos, dom 8, solo por resumen; Meganoticias 786826; El Universal Oaxaca; NVI 173538).
  - Tecate (cinco homicidios del 6-nov por titular de El Congresista, en hechos separados; Los Encinos con 2 o 3 muertos según Consulta Monterrey, cuyo titular dice 3 y el cuerpo 2).
  - Huaquechula (3 muertos y 1 herido, Quadratín Puebla, sin fecha).
  - Cañada Morelos (2 muertos, La Jornada de Oriente, sin fecha).
  - Monterrey, taquería El Trompo Regio (riña, 2 muertos, sáb 7 solo por resumen).
  - Fosas y restos sin día: Reynosa; Nuevo Laredo (posible ARG-146-009); Viesca (colectivo Vida); Doctor Coss.
- **Balances, no integrados**:
  - 128 homicidios del 6 al 8-nov (Excélsior: 34/50/44; Sinaloa 16, Guanajuato 13; preliminares del Gabinete).
  - 281 del 2 al 8-nov (UnoTV, SSPC).
  - Culiacán, 6 asesinados en el fin de semana.
  - Guanajuato, 4 policías en 3 semanas (Correo 2026/nov/09); 21 o 23 agentes en el año.
  - Acapulco, 5 muertos el fin de semana previo.
  - Brigada de Mexicali.
- **Vistos sin ruta (🟡/🟢)**:
  - Acapulco: Adobería (dom 8) y avenida Cuauhtémoc, taxista (sáb 7).
  - Centro, Tabasco, ranchería González 4.ª (vie 6; mañana o tarde contradicho, posible antes de las 07:30).
  - Espinal, Entabladero (adolescente; sáb 7 o dom 8).
  - Coronango (mujer de 22 años, sin fecha).
  - Atencingo, mototaxista «El Bella» (8 o 9-nov).
  - Culiacán: San Rafael y Díaz Ordaz; expitcher Enrique Quiñones.
  - Concordia (2 largas, 87 cartuchos, 1 detenido, solo por resumen).
  - Celaya, San Isidro de Elguera, y Cerano (solo por resumen).
  - Tabasco, 21 detenidos (3-5 nov, evento anterior).

## 8. Controles editoriales

Ronda 1 en paralelo; ronda 2 en serie.

- **`procedencia-cifras` R1** (23 de 24 búsquedas): **CORREGIR**. Aplicado:
  - enfrentamiento de Zapopan en ventana, con ficha propia;
  - Tlachichuca retirado;
  - Atempan con primera publicación el 7-nov y sin la lista de precursores;
  - Sanalona y Escuinapa integrados con las cifras del titular;
  - Valtierrilla en secuencia (1 + 2);
  - Celaya con «tres heridos»;
  - Irapuato con hora contradicha.
- **`editor-duplicidad` R1**: **CORREGIR**. Sin duplicados contra las ediciones previas ni internos. Aplicado de C1 a C12:
  - C2: Mazatlán, cualitativo;
  - C4: cláusulas unificadas;
  - C5: valoración solo de escala, y líneas de conclusión distintas de las de portada;
  - C6: repeticiones de armamento;
  - C7: referencias cruzadas;
  - C8: deslinde Irapuato–Valtierrilla;
  - C9: recuento de Juchitán;
  - C10: etiqueta de Tecate;
  - C11: códigos FE al índice;
  - C12: residuos de método.
  - **No aplicado**: «partir los bloques del panorama en tabla». Se mantienen las notas compactas porque son trazabilidad (vistos, rojos sin ruta, fe de erratas y seguimiento), que son las excepciones admitidas.
- **R2**: ver §8b, que se añade al cierre.

## 9. Presupuesto de búsqueda

Control 2 · coordinador 18 (16 de recall y triple consulta + 2 de repetición al cierre) · ola 150 (6 × 25) · `procedencia-cifras` R1 23 · R2: ver §8b.

## 10. Hallazgos de método (no van al cartelón)

1. **Tres falsos vacíos del mismo emisor federal.** El agregado del 6, 7 y 8 no aparecía por día suelto ni por rango al inicio. Apareció **por título** al cierre, a través de un único republicador. Confirma la triple consulta y la repetición al final.
2. **Boletín del 5-nov y ventana**: un anuncio del secretario el día de apertura, sin hora, resultó ser un operativo del día anterior (Tlachichuca). **Antes de fichar un anuncio federal del día de apertura, buscarlo en el boletín del día anterior.**
3. **Pista del coordinador desmentida**: Cuerámaro, que el recall daba como rojo, era una presunta autolesión con el arma de cargo. Hay que verificar la causa antes de pasar un «policía muerto» como rojo.
4. **Delito y detención en la misma ventana** (Zapopan): el borrador los fusionó en un solo verde, el mismo fallo de ARG-101-008. Lo detectaron los dos controles.
5. **Comunicación del cartelón**: `gen-movil.py` rechaza códigos `-FE-` en el cartelón. Las erratas van sin código y el código vive en el índice.
6. **Prioridad sobre el ciclo no saldada**: Edomex en armamento (tercera edición), BC, BCS y Son en armamento, Qro en alto impacto (tercera edición) y CDMX en alto impacto solo con consulta amplia.
