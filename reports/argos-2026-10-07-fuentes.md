# ARGOS 125 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-07 · **Ventana**: 2026-09-24 06:41 → 2026-10-07 15:15 CDMX · **320 h 34 min**
**Rama**: `claude/argos-criminal-intelligence-otiawj` (partió de `main` en `dbbab71`, ARGOS 124).

La ventana cubre **trece días por ausencia de publicación entre el 24-sep y el 7-oct**. La numeración cuenta ediciones: esta es la 125.

---

## 1. La base

Bloque 0 ejecutado como primer comando: hora real **2026-10-07 15:15 CST** (UTC−6; sin horario de verano desde 2022).
`git merge --ff-only origin/main` limpio; `main` = `origin/claude/argos-123-criminal-analysis-k70hzw` = `dbbab71`.
Estado encontrado: `argos-2026-09-24` (ARGOS 124) y **123 archivos** en `reports/`, lo previsto. Las dos ramas nuevas del fetch
(`argos-intake-app`, `plataforma-victimologia-forense`) son de aplicaciones, sin `reports/`.

| Serie | 119 | 120 | 121 | 122 | 123 | 124 | **125** |
|---|---|---|---|---|---|---|---|
| Duración | 117 h 50 | 75 h 06 | 30 h 02 | 87 h 21 | 23 h 25 | 46 h 19 | **320 h 34** |
| Densidad (hechos/h) | — | — | 0,25 | 0,19 | 0,04 | 0,30 | **0,16** (51 / 320,57, cálculo propio) |

**2,72 veces** la ventana más larga de la serie y **6,92 veces** la de ARGOS 124 (la orden de arranque decía 2,65 y 6,7: se
escribió hacia las 07:00 CDMX; se recalculó al sellar).

## 2. ⚠️⚠️ Hallazgo de herramienta que decidió la edición: el modo de búsqueda

**La primera ola —doce equipos, unas 210 búsquedas en modo `standard`— volvió prácticamente vacía**: los seis barridos, los dos
recall nacionales, el boletín federal y el equipo judicial no fijaron **un solo hecho** de la ventana. Todos coincidieron en el
síntoma: lo más reciente que devolvía el índice era de hacia el **19-sep-2026** (el boletín federal del 21-sep fue el último).

El coordinador probó el **modo `extended`** sobre Comonfort: devolvió en una consulta lo que doce equipos no habían visto
(La Silla Rota 2026/9/24, Proceso 2026/9/24: **dos detenidos**). **El índice `standard` estaba congelado; el `extended` alcanza la
ventana.** La segunda ola —ocho equipos, `extended`, unas 120 búsquedas— produjo los 51 hechos propios de esta edición.

Consecuencias, que se trasladan a `_pendientes.md` y a la orden de ARGOS 126:
- **Toda búsqueda de ARGOS se hace en `extended`.** Un `SIN RESULTADO INDEXADO` obtenido en `standard` **no es casilla de cobertura
  válida**: es `NO REVISADA`.
- **Tope compartido de 200 búsquedas por turno** entre todos los agentes: la primera ola lo agotó y se rechazaron consultas en
  Occidente, Centro, Sureste, Noroeste, judicial, recall y boletín federal. **Los rechazos no se rodearon.**
- El bloqueo de egreso persiste (curl `000` a `gob.mx`, `seguridad.guanajuato.gob.mx`, `eluniversal.com.mx`, `milenio.com`):
  **techo ★★★☆☆, séptima edición.**

## 3. Cambio de método: recall regional dentro de los barridos — resultado

**Orden de la edición**: cada barrido regional incorpora recall de alto impacto de su región.

| Región | Ola 1 (`standard`) | Ola 2 (`extended`) — hechos rojos aportados por el recall regional |
|---|---|---|
| Noroeste + Noreste | 0 | Hermosillo (doble homicidio, menor de 13), Mazatlán (patrulla emboscada, vía recall nacional) · **Coahuila y Zacatecas: sin hecho rojo** |
| Occidente | 0 | Valle de Santiago (centro y restos en Puerto de Araceo), Xalisco (también recall nacional) |
| Centro + Golfo | 0 | La Resurrección (fosa), Tecamachalco (`-REC-`), Tlaxcala (amarillo) |
| Sureste | 0 | **Ajuchitlán / El Balcón** — no lo trajo ningún recall nacional |
| Recall nacional (3 tramos) | 0 | Culiacán ×2, Uruapan ×2, San Luis de la Paz, Tlalnepantla, Yecapixtla, Guadalajara, Xalisco, Mazatlán |
| Coordinador | Comonfort (seguimiento) | **Salamanca** (policía municipal), verificación de El Balcón, Hermosillo, Mazatlán, Morelia |

**Veredicto: la pregunta queda cerrada a favor del recall regional.** Con el modo de búsqueda correcto, los barridos regionales
aportaron **por primera vez en dieciséis ediciones** hechos rojos que ni el recall nacional ni el coordinador habían traído
(El Balcón, Valle de Santiago-Yuriria, La Resurrección). Pero el dato decisivo no es el método de reparto sino el **modo de
búsqueda**: con `standard`, ni el recall regional ni el nacional producen nada. **Se mantiene el recall regional como parte fija del
barrido.**

## 4. Rotación — CICLO C aplicado y declarado

| Renglón | Resultado |
|---|---|
| Ciclo | **C** — Occidente + Sureste encabezaron el triaje judicial |
| Prioridad sobre el ciclo | **Coahuila y Zacatecas** encabezaron el Noreste: dos consultas dedicadas a cada una en `extended`. **Coahuila aporta su primer hecho fichado tras dos ediciones** (ejido San Vicente, `ARG-125-029`); Zacatecas, `SIN RESULTADO INDEXADO EN VENTANA` en alto impacto y armamento. **Sentencias de ambas: NO REVISADA** (solo consulta `standard`) |
| Rendimiento del ciclo | **Un candidato nuevo publicado en ventana** (Lagos de Moreno, 26-sep) y **tres candidatos sacados de la ventana por fecha** (Cancún 21-sep, Morelia 17-sep, Coacalco 14-sep). Sin sentencia integrable |

Serie: B (121) no · C (122) sí · A (123) no · B (124) no · **C (125) sí, candidato no integrable**. **Los dos ciclos C producen
candidato; los cinco producen corrección de archivo.**

## 5. Boletín federal — triple consulta adaptada a trece días

| Día | Estado | Formato |
|---|---|---|
| 24-sep | LOCALIZADO (Milenio, RED113, Talla Política) | diario |
| 25-26-27-sep | LOCALIZADO (Milenio, Talla Política) | **agregado de tres días** |
| 28-sep | LOCALIZADO (RED113, único republicador) | diario |
| 29-sep | LOCALIZADO (Talla Política, Certeza Diario) | diario |
| 30-sep | LOCALIZADO (RED113 con ruta `/2026/10/`, Talla Política, Certeza) | diario |
| 1-oct | LOCALIZADO (Milenio, Hoja de Ruta, RED113, Talla Política, Certeza) | diario |
| 2-3-4-oct | LOCALIZADO (Milenio, Viva la Noticia, RED113, Talla Política, Ahora Noticias, Certeza, Hoja de Ruta) | **agregado de tres días** |
| 5-oct | LOCALIZADO (Milenio, RED113, Talla Política, Certeza) | diario |
| 6-oct | LOCALIZADO (Milenio, Ahora Noticias, Ahora Tabasco, Argon México) | diario |
| **7-oct** | `SIN RESULTADO INDEXADO EN VENTANA` | — día de cierre |

**El formato cambió dos veces dentro de la ventana.** `gob.mx` no indexó ninguno: **sexta edición** en que solo el título sin
`site:` alcanza el documento. **Sustitución anotada: corroboración débil por construcción.**
⚠️ **Las cifras de la mayoría de los renglones vienen del resumen del buscador sobre esos republicadores**, no de fragmento literal:
`procedencia-cifras` lo señaló. Se localizaron literales para Chihuahua (2-4 oct: «catearon dos inmuebles donde detuvieron a un
hombre; le aseguraron 37 armas largas, 86 cargadores, 55 mil 960 cartuchos, tres vehículos y documentación diversa»), Santa María
del Oro, Mazatlán (autobús) y Culiacán (metanfetamina). **El resto se integra marcado `SOLO POR CITA DEL BOLETÍN`**, como en
ediciones anteriores.

**Renglones del boletín NO fichados, con motivo**: Chihuahua «Río Bravo y Monterrey», 520,000 L de hidrocarburo (24-sep) —
**entidad incoherente en el texto**; Los Ramones, 39 kg de cocaína; Tijuana (dos renglones de droga); Tultepec/Zumpango 5 detenidos;
Acámbaro 2 detenidos; Allende 15 kg; Ensenada (migrantes); Guanajuato y Corregidora (tomas, 26,500 y 40,000 L); Celaya 60,000 L;
Cuauhtémoc 100 kg de cocaína; órdenes de aprehensión y extradiciones (Iguala, Huauchinango, Jiutepec, Paraíso, San Simón, Monterrey,
Playa del Carmen, Sonora); SLP del 5-oct (1 larga, 1 corta, 55 cartuchos: `POSIBLE DUPLICIDAD` con `ARG-125-015`); Huajicori-Cerro
Bola (6 largas, 37 cargadores, 919 cartuchos, 5 AEI: `POSIBLE DUPLICIDAD` con `ARG-125-017`). **Sin armamento o sin validar: no
alimentan el conteo.**

## 6. Los tres encargos

| Encargo | Disposición |
|---|---|
| **Comonfort** | **Dos detenidos anunciados el 24-sep** por el Srio. de Gobierno Jorge Jiménez Lona → **hecho nuevo verde `ARG-125-050`** con `FRONTERA DE VENTANA`. Participación **no establecida**. **Ninguna autoridad confirmó los dos civiles abatidos ni un cuarto policía**: la cifra de `ARG-124-001` (tres) se mantiene. **Armamento de los agresores: no publicado** |
| **Coatzacoalcos / patrón político** | **Cateo de la FGE** el 24-sep (`ARG-125-049`) y **«La Princess» y dos hombres detenidos el 1-oct**, cinco en prisión preventiva al 5-oct (`ARG-125-021`). **Búsqueda expresa del patrón en trece días: ningún cuarto dirigente político asesinado localizado dentro de la ventana** (13 consultas en ola 1, más ola 2). En ventana: hijo del alcalde de Tecamachalco (`-REC-`), alcalde de Suchiapa detenido (Enjambre). **Patrón registrado, vinculación no afirmada.** Pistas de agosto sin indexar: regidor de Texistepec (Veracruz) y dirigente de MC en Tlapehuala (Guerrero) → `_pendientes.md` |
| **Laja-Bajío** | **CERRADO POR AGOTAMIENTO DECLARADO.** Tercera edición, **once búsquedas en total** (tres en 124, cuatro `standard` y las del recall en 125): **no existe documento de la FGE de Guanajuato** que sostenga «23 muertos y 11 heridos entre el 18 y el 20-sep». La cifra queda **sin integrar ni citar, de forma definitiva**: si un boletín apareciera, se publicaría como `-REC-` de la ventana de ARGOS 123 |

## 7. Arbitrajes del coordinador — en las dos direcciones

1. ⚠️⚠️ **Los agregados federales de tres días SE INTEGRAN (8 fichas, 8 filas).** Precedente en contra, buscado: ARGOS 123
   reclasificó a `-REC-` siete fichas «tramo 18/20» (`argos-2026-09-22-fuentes.md` §5) y `_pendientes.md` escribió «si el emisor no
   desglosa por día, ningún renglón entra en los totales». Precedentes a favor: `ARG-120-015` (rango 11-13 sep integrado) y el
   principio de §5.2 —«un hecho cuya fecha no puede fijarse **dentro** de la ventana no puede contarse»—. **Distinción**: los tramos
   de 123 pertenecían a la ventana anterior; **25-27 sep y 2-4 oct caen íntegros en esta**, de modo que cualquier día del tramo es de
   esta ventana. **`editor-duplicidad` intentó derribarlo y lo sostuvo**, con cuatro exigencias que se cumplieron: no inferir un día
   (las fichas dicen «tramo» en el campo Hecho y van en bloque propio), cuantificar su peso, anotar aquí los precedentes y **reescribir
   la regla de `_pendientes.md`**. Peso: **44 de 66 largas, 58,853 de 67,692 cartuchos y 175 de 231 cargadores** (cálculo propio). Si
   se revirtiera: 43 hechos propios, 24 verdes.
2. **Morelia `ARG-125-039` se mantiene 🟡, con la razón corregida**: el borrador decía «la autoridad ejecutaba una acción y fue
   repelida»; las fuentes dicen que los sospechosos dispararon «al ser detectados o al marcárseles el alto». **Quién inició no es
   determinable → 🟡 con reserva** (cláusula de `CLAUDE.md`; precedentes `ARG-119-006`, `ARG-114-003`). Arbitraje **a la baja**
   frente a la lectura de un barrido, que lo proponía rojo.
3. **Mazatlán `ARG-125-012` en 🔴**: la SSP municipal describe una patrulla en tránsito atacada desde un Nissan Sentra. **Quién
   inició sí está determinado.** Arbitraje **al alza** frente a la tentación de tratarlo como incidente sin bajas.
4. **Dobles homicidios civiles en 🔴** (`-020`, `-038`, `-040`) por víctimas múltiples: coherente con `ARG-99-001`, `ARG-119-003`,
   `ARG-122-002`. **Exelementos de seguridad fuera de servicio en 🟡** (`-004`, `-028`): no eran personal en activo.
5. **Detenciones por hechos de ARGOS 124 cuentan como verdes propios** (`-050`, `-021`): `CLAUDE.md` —«un delito y su detención son
   dos eventos»— prevalece sobre la regla del editor según la cual un desarrollo no cuenta en el semáforo. Precedente `ARG-120-011`.
6. **García `ARG-125-032`**: se adopta **5,093 cartuchos, 5 largas, 2 cortas y 14 cargadores** del comunicado de la FGR (Milenio, MVS)
   frente a «4,771» atribuido al boletín por republicador, que **no apareció en ninguna fuente**. Arbitraje por procedencia.
7. **SLP `ARG-125-015`**: los **9 detenidos se integran** (titular nacional); el renglón federal del 5-oct en SLP no.

## 8. Correcciones al archivo y fe de erratas

- `ARG-125-FE-001` — **sobre ARGOS 124**: su ventana contuvo un hecho rojo no publicado, el **hijo del alcalde de Tecamachalco**
  hallado el 23-sep (`ARG-125-REC-001`). **Efecto sobre ARGOS 124: rojos 2 → 3; muertos en ventana 4 → 5.**
- `ARG-125-FE-002` — **sobre la regla de agregados de `_pendientes.md`** (ARGOS 123): se reescribe como «si el emisor no desglosa
  por día y **el tramo no está íntegro en la ventana**, ningún renglón entra en los totales».
- **Puerto Peñasco (`ARG-122-007`)**: las fuentes aluden a una **Browning M2 cal. .50** además de las dos Minimi; solo por resumen.
  No se integra; queda en `_pendientes.md`.
- **Quechultenango**: contradicción de fecha jueves 17 (UnoTV) frente a viernes 18-sep (N+). Sin novedad en ventana.
- **Tepito**: una fuente escribe «Odet Rosa», no «Odette Rosas». Sin boletín, séptima edición.

## 9. Registro del barrido — `NO REVISADA` por entidad y tramo

Tramo A = 24-30 sep · Tramo B = 1-7 oct. **Ninguna entidad se revisó día por día**: toda consulta fue de tramo o de ventana
completa; los días se cubren solo en la medida en que la consulta de tramo los alcanzó. **Las consultas `standard` de la ola 1 se
declaran `NO REVISADA`.** SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0** (sin lectura directa).

| Entidad | Alto impacto A / B | Armamento A / B | Sentencias |
|---|---|---|---|
| Baja California | SRIV / SRIV | boletín federal (Mexicali, Tecate) / NO REVISADA | NO REVISADA |
| Baja California Sur | NO REVISADA / NO REVISADA | NO REVISADA / NO REVISADA | NO REVISADA |
| Sonora | SRIV / hecho (Hermosillo) | boletín / SRIV | NO REVISADA |
| Chihuahua | SRIV / hecho (Cuauhtémoc) | boletín / boletín | revisada (candidatos Juárez) |
| Sinaloa | hecho / hecho | hecho / hecho | NO REVISADA |
| Durango | NO REVISADA / NO REVISADA | SRIV / FGR 6-oct sin cifra | NO REVISADA |
| Coahuila | SRIV / SRIV | SRIV / boletín (San Vicente) | NO REVISADA |
| Nuevo León | SRIV / SRIV | boletín (García) / SRIV | NO REVISADA |
| Tamaulipas | SRIV / SRIV | SRIV / SRIV | revisada (Nuevo Laredo) |
| San Luis Potosí | NO REVISADA / NO REVISADA | NO REVISADA / boletín | revisada (Norma «N») |
| Zacatecas | SRIV / SRIV | SRIV / SRIV | NO REVISADA |
| Jalisco | SRIV / hecho | SRIV / boletín | revisada (Lagos de Moreno) |
| Colima | SRIV / SRIV | SRIV / SRIV | revisada (conjunta) |
| Nayarit | SRIV / hecho | SRIV / boletín | revisada (conjunta) |
| Aguascalientes | SRIV / SRIV | SRIV / SRIV | revisada (conjunta) |
| Michoacán | hecho / SRIV | boletín / SRIV | revisada |
| Guanajuato | hecho / hecho | SRIV / SRIV | revisada |
| Ciudad de México | SRIV / SRIV | SRIV / SRIV (cateo GAM solo por resumen) | NO REVISADA |
| Estado de México | SRIV / SRIV | SRIV / SRIV | revisada (Coacalco) |
| Morelos | SRIV / hecho | SRIV / SRIV | NO REVISADA |
| Puebla | hecho / SRIV | SRIV / SRIV | NO REVISADA |
| Tlaxcala | hecho / SRIV | NO REVISADA / NO REVISADA | NO REVISADA |
| Hidalgo | NO REVISADA / NO REVISADA | NO REVISADA / NO REVISADA | NO REVISADA |
| Querétaro | NO REVISADA / NO REVISADA | NO REVISADA / NO REVISADA | NO REVISADA |
| Veracruz | hecho / hecho | hecho / boletín | NO REVISADA |
| Tabasco | SRIV / SRIV | SRIV / SRIV | NO REVISADA |
| Guerrero | hecho / SRIV | NO REVISADA / NO REVISADA | NO REVISADA |
| Chiapas | SRIV / hecho | NO REVISADA / NO REVISADA | revisada |
| Oaxaca | SRIV / SRIV | boletín / boletín | revisada |
| Quintana Roo | SRIV / SRIV | SRIV / SRIV | revisada (Cancún) |
| Yucatán | SRIV / SRIV | NO REVISADA / NO REVISADA | NO REVISADA |
| Campeche | SRIV / SRIV | NO REVISADA / NO REVISADA | revisada |

**Sentencias: 14 de 32 revisadas + FGR; 18 NO REVISADAS.** «Revisada» significa al menos una consulta `extended` dirigida en la
ventana. **Esta edición NO declara cobertura total en ningún módulo.**

## 10. Hechos vistos y NO fichados, con motivo

| Hecho | Motivo |
|---|---|
| Culiacán, Parque Alamedas (SSP Sinaloa: 1 AK-47, 2 AR-15, 16 cargadores, 555 cartuchos) | **Día del hecho no fijado** (publicación «2026/10»); cifras solo por resumen. Se publica si se fecha |
| Culiacán, Corolla abandonado (2 fusiles, uno con lanzagranadas, 1 granada) | Hallazgo «2-oct» solo por resumen; URL del 6-oct. Pendiente |
| Juárez, osamenta del 28-sep | Solo por resumen dentro de un cierre mensual |
| Cuernavaca, dos estudiantes de la UAEM (¿26-sep?) | URL sin fecha |
| Cuajinicuilapa, restaurante, 2 muertos (¿24-sep?) | URL sin fecha |
| Quintana Roo, Akumal/Playa del Carmen, 4 detenidos por homicidio de funcionario | Fecha y víctima sin fijar |
| Ocosingo, linchamiento en Las Tacitas | «Finales de septiembre», sin día |
| Yautepec (4-oct), Manzanillo (6-oct), Mérida Montes de Amé (2-oct) | Fuente única sin fecha en la ruta o hecho menor |
| Sinaloa 28 y 29-sep (2 y 5 homicidios dispersos) | Agregados de medio, sin hecho individual |
| Celaya/Villagrán (6-oct), Cerro Coronel (1-oct), Durango FGR (6-oct) | Sin fecha fijada o sin cifra |
| Valle de Chalco–Ixtapaluca 3 muertos (21-sep), León pozo 5 cuerpos (21-sep) | **Ventana de ARGOS 123**: candidatos a `-REC-` no verificados → `_pendientes.md` |
| Zamora/Ixtlán «26-sep» | **Es de 2023**: señuelo de año |
| Drones Escuinapa, Navolato 2 policías | **Junio 2026 y octubre 2024**: señuelos |
| Guerrero «800-1000 familias desplazadas» | **Mayo 2026** |
| Oaxaca, San Pedro Ocotepec | **2022** |
| Calera «6 policías», La Costerita «miércoles 26-sep» | **Día de la semana incompatible con 2026**: señuelos |

## 11. Desglose de cálculos propios

- **Muertos y cuerpos hallados en hechos rojos: 30** = Guadalajara 4 + Hermosillo 2 + Puerto de Araceo 2 + Valle de Santiago 2 +
  Tlalnepantla 5 + Yecapixtla 2 + La Resurrección 1 + Uruapan 3 + Cutzato 1 + Montesierra 2 + San Luis de la Paz 2 + Salamanca 1 +
  Urbivillas 3. Más restos sin cifra en Xalisco. **Los cuerpos de fosa pueden ser de muertes anteriores a la ventana.**
- **Armas 125** = 8 cortas + 66 largas + 50 sin categoría + 1 especial. **Cartuchos 67,692 · cargadores 231 · granadas 15 · AEI 85
  (79 en Sinaloa; 7 de ellos destruidos en el lugar; 15 llamados «explosivos» por la fuente y clasificados por analogía) ·
  detenidos 55.**
- **Detenidos sin armamento, fuera del conteo**: 21 Suchiapa · 2 Comonfort · 5 procesados en Coatzacoalcos.

## 12. Fuentes por ficha

| ARG-ID | Entidad · municipio | Hecho | Color | ★ | Recuento | Con fecha en la ruta | Institucional / nacional | Campo peor sostenido |
|---|---|---|---|---|---|---|---|---|
| `ARG-125-001` | Sonora · Hermosillo | 2026-10-06 | verde | ★★★☆☆ | I1 N0 R4 A0 | El Imparcial (2026/10/07); Tribuna (2026/10/06) | FGJES (por cita) / — | fecha de la captura y vínculo con el homicidio (orden en trámite) |
| `ARG-125-002` | Jalisco · Guadalajara | 2026-10-06 | rojo | ★★★☆☆ | I0 N3 R3 A1 | Infobae (2026/10/07); Grupo Marmor (2026/10/06); Sociedad Noticias (2026/10/07) | SIN BOLETÍN / Infobae · Milenio | cifra de cuerpos (3 frente a 4) y sin fuente institucional |
| `ARG-125-003` | Nayarit · Xalisco | 2026-10-06 | rojo | ★★★☆☆ | I1 N5 R2 A1 | Proceso (2026/10/6); Infobae (2026/10/06); La Silla Rota (2026/10/6 y 2026/10/7); El Financiero (2026/10/06); El Popular (2026/10/07); Sociedad Noticias (2026/10/06) | FGE Nayarit (por cita) / Proceso · Infobae · El Financiero | número de víctimas (no existe) y fecha de inicio (3-oct, solo por cita) |
| `ARG-125-004` | Chihuahua · Cuauhtémoc | 2026-10-06 | amarillo | ★★☆☆☆ | I0 N0 R1 A0 | El Diario de Chihuahua (2026/oct/06) | SIN BOLETÍN / — | fuente única |
| `ARG-125-005` | Sinaloa · Escuinapa y Mazatlán | 2026-10-06 | verde | ★★★☆☆ | I1 N1 R3 A0 | Los Noticieristas (2026/10); Argon México (2026/10/07) | Gabinete de Seguridad (por republicador) / Milenio | tipo de artefacto y localidad |
| `ARG-125-006` | Sinaloa · Culiacán (Carboneras) | 2026-10-06 | verde | ★★★☆☆ | I1 N1 R2 A0 | Los Noticieristas (2026/10) | Gabinete de Seguridad (por republicador) / Milenio | cifras por republicador |
| `ARG-125-007` | Jalisco · Ixtlahuacán de los Membrillos | 2026-10-06 | verde | ★★★☆☆ | I1 N1 R2 A0 | Argon México (2026/10/07) | Gabinete de Seguridad (por republicador) / Milenio | desglose de las seis armas restantes |
| `ARG-125-008` | Veracruz · Omealca | 2026-10-06 | verde | ★★★☆☆ | I1 N1 R2 A0 | Argon México (2026/10/07) | Gabinete de Seguridad (por republicador) / Milenio | cifras por republicador |
| `ARG-125-009` | Sonora · Hermosillo | 2026-10-05 | rojo | ★★★☆☆ | I1 N1 R4 A0 | Infobae (2026/10/07); Tribuna (2026/10/06); Dossier Político (2026/10/06); El Imparcial (2026/10/07) | Fiscalía de Sonora (por cita) / Infobae | hora (solo una fuente regional) |
| `ARG-125-010` | Sinaloa · El Rosario | 2026-10-05 | verde | ★★★☆☆ | I1 N1 R6 A0 | Luz Noticias (2026-10-06); Línea Directa (2026-10-06); Los Noticieristas (2026/10) | Ejército (por cita) · Gabinete (republicador) / Milenio | cifras de armas, cargadores y cartuchos (listado regional) |
| `ARG-125-011` | Jalisco · Zapopan | 2026-10-05 | verde | ★★★☆☆ | I1 N3 R0 A0 | Proceso (2026/10/6); El Financiero (2026/10/06); Infobae (2026/10/07) | Gabinete de Seguridad (por republicador) / Proceso · El Financiero · Excélsior | identidad entre el boletín y la cobertura |
| `ARG-125-012` | Sinaloa · Mazatlán | 2026-10-03 | rojo | ★★★☆☆ | I1 N3 R4 A1 | El Diario del Noroeste (2026/oct/03); Diario.mx (2026/oct/03) | SSP Municipal (por cita) / El Norte · Vanguardia · Diario.mx | número de heridos sin confirmación estatal |
| `ARG-125-013` | Guanajuato · Valle de Santiago (salida a Yuriria) | 2026-10-03 | rojo | ★★★☆☆ | I1 N0 R3 A0 | Periódico Correo (2026/oct/03); AM (2026/10/04) | FGE Gto. (por cita) / — | sexo de las víctimas |
| `ARG-125-014` | Chiapas · Suchiapa | 2026-10-03 | verde | ★★★☆☆ | I2 N6 R2 A0 | Informador (20261003); El Imparcial (2026/10/03 y 2026/10/06); El Financiero (2026/10/03) | Gabinete (por cita) · FGE Chiapas (por cita) / El Universal · El Financiero · Milenio · N+ | número de policías y móvil, contradichos |
| `ARG-125-015` | San Luis Potosí · no especificado | tramo 2-4 oct | verde | ★★★☆☆ | I1 N2 R0 A0 | El Imparcial (2026/10/05) | Gabinete de Seguridad (por republicador) / El Imparcial · Excélsior | día del hecho y cifras de armamento |
| `ARG-125-016` | Chihuahua · no especificado | tramo 2-4 oct | verde | ★★★☆☆ | I1 N1 R2 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | municipio y día del hecho; un solo texto del emisor |
| `ARG-125-017` | Nayarit · Huajicori | tramo 2-4 oct | verde | ★★★☆☆ | I1 N1 R2 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | día del hecho; tipo de armas |
| `ARG-125-018` | Oaxaca · Juchitán de Zaragoza | tramo 2-4 oct | verde | ★★★☆☆ | I1 N1 R2 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | día del hecho; tipo de armas |
| `ARG-125-019` | Sinaloa · Mazatlán | tramo 2-4 oct | verde | ★★★☆☆ | I1 N1 R2 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | día del hecho |
| `ARG-125-020` | Guanajuato · Valle de Santiago | 2026-10-02 | rojo | ★★★☆☆ | I1 N4 R2 A0 | Periódico Correo (2026/oct/02); AM (2026/10/03); Infobae (2026/10/04); Latinus (2026/10/4); La Silla Rota (2026/10/4); El Financiero (2026/10/05) | FGE Gto. (por cita) / Infobae · Latinus · La Silla Rota · El Financiero | fecha (1 o 2-oct) |
| `ARG-125-021` | Veracruz · Coatzacoalcos | 2026-10-01 | verde | ★★★☆☆ | I1 N3 R1 A0 | Infobae (2026/10/01 y 2026/10/05); Tribuna (2026/10/01); El Imparcial (2026/10/05) | FGE Veracruz (por cita) / Infobae · Milenio · El Imparcial | nombre de la detenida y delitos de la medida cautelar |
| `ARG-125-022` | Morelos · Tlalnepantla | 2026-10-01 | rojo | ★★★☆☆ | I1 N5 R2 A1 | Proceso (2026/10/1); El Heraldo de México (2026/10/1); La Silla Rota (2026/10/1); Infobae (2026/10/02); Diario.mx (2026/oct/02) | FGE Morelos (por cita) / Proceso · Infobae · La Silla Rota · El Heraldo | competencia de investigación e identidades |
| `ARG-125-023` | Morelos · Yecapixtla | 2026-10-01 | rojo | ★★★☆☆ | I0 N2 R2 A0 | Proceso (2026/10/1); El Heraldo de México (2026/10/1); Diario.mx (2026/oct/02) | SIN BOLETÍN / Proceso · El Heraldo | hora del hallazgo |
| `ARG-125-024` | Nayarit · Santa María del Oro | 2026-10-01 | verde | ★★★☆☆ | I2 N2 R3 A0 | Infobae (2026/10/03); NTV (2026/10/05); Nayarit Noticias (2026/10/05) | Gabinete de Seguridad (por republicador) / Milenio · Infobae | cargadores contradichos |
| `ARG-125-025` | Sinaloa · Mazatlán | 2026-10-01 | verde | ★★★☆☆ | I1 N1 R4 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | detenido contradicho |
| `ARG-125-026` | Sinaloa · Culiacán | 2026-10-01 | verde | ★★★☆☆ | I1 N1 R3 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | corroboración (solo republicadores del boletín) |
| `ARG-125-027` | Puebla · Puebla (La Resurrección) | 2026-09-30 | rojo | ★★☆☆☆ | I1 N0 R3 A0 | Azteca Puebla (slug 30-septiembre-2026) | FGE Puebla (por cita) / — | sin fuente nacional; identidad |
| `ARG-125-028` | Tlaxcala · Tlaxcala | 2026-09-30 | amarillo | ★★★☆☆ | I1 N1 R2 A0 | Gente TLX (2026/09/30) | FGJE Tlaxcala (por cita) / Excélsior | identidad de la víctima |
| `ARG-125-029` | Coahuila · Guerrero (ejido San Vicente) | 2026-09-30 | verde | ★★★☆☆ | I1 N0 R3 A0 | — | Gabinete de Seguridad (por republicador) / — | corroboración (solo republicadores del boletín) |
| `ARG-125-030` | Chihuahua · Ciudad Juárez | 2026-09-30 | verde | ★★★☆☆ | I1 N0 R3 A0 | — | Gabinete de Seguridad (por republicador) / — | corroboración (solo republicadores del boletín) |
| `ARG-125-031` | Sinaloa · Culiacán | 2026-09-30 | verde | ★★★☆☆ | I1 N0 R3 A0 | — | Gabinete de Seguridad (por republicador) / — | corroboración (solo republicadores del boletín) |
| `ARG-125-032` | Nuevo León · García | 2026-09-29 | verde | ★★★☆☆ | I1 N3 R2 A0 | MVS (2026/9/30 y 2026/10/6) | FGR (por cita) / Milenio · MVS · N+ | cifra de cartuchos (5,093 frente a 5,097) |
| `ARG-125-033` | Baja California · Tecate | 2026-09-29 | verde | ★★★☆☆ | I1 N0 R2 A0 | — | Gabinete de Seguridad (por republicador) / — | cifra de armas (no publicada) |
| `ARG-125-034` | Sinaloa · no especificado | 2026-09-29 | verde | ★★★☆☆ | I1 N0 R2 A0 | — | Gabinete de Seguridad (por republicador) / — | municipio y cifra de armas |
| `ARG-125-035` | Michoacán · Uruapan | 2026-09-28 | rojo | ★★★☆☆ | I0 N1 R2 A0 | Latinus (2026/9/28); Grupo Marmor (2026/09/28); Red Michoacán (2026/09/28) | SIN BOLETÍN / Latinus | sin fuente institucional |
| `ARG-125-036` | Michoacán · Uruapan (Cutzato) | 2026-09-28 | rojo | ★★☆☆☆ | I0 N0 R1 A0 | Red Michoacán (2026/09/28) | SIN BOLETÍN / — | fuente única |
| `ARG-125-037` | Sinaloa · no especificado | 2026-09-28 | verde | ★★☆☆☆ | I1 N0 R1 A0 | — | Gabinete de Seguridad (por republicador) / — | un solo republicador del boletín |
| `ARG-125-038` | Sinaloa · Culiacán | 2026-09-27 | rojo | ★★★☆☆ | I1 N0 R2 A0 | Ríodoce (2026/09/27); Línea Directa (2026-09-27) | FGE Sinaloa (por cita) / — | sin fuente nacional |
| `ARG-125-039` | Michoacán · Morelia | 2026-09-26 | amarillo | ★★★☆☆ | I1 N1 R5 A0 | Red Michoacán (2026/09/26); Grupo Marmor (2026/09/26); La Silla Rota (2026/9/26) | SSP Michoacán (por cita) / La Silla Rota | corporación actuante |
| `ARG-125-040` | Guanajuato · San Luis de la Paz | 2026-09-26 | rojo | ★★☆☆☆ | I0 N0 R1 A0 | Periódico Correo (2026/sep/26) | SIN BOLETÍN / — | fuente única |
| `ARG-125-041` | Michoacán · no especificado | tramo 25-27 sep | verde | ★★★☆☆ | I1 N1 R1 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | municipio y día del hecho |
| `ARG-125-042` | Oaxaca · no especificado | tramo 25-27 sep | verde | ★★★☆☆ | I1 N1 R1 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | municipio y día del hecho |
| `ARG-125-043` | Chihuahua · no especificado | tramo 25-27 sep | verde | ★★★☆☆ | I1 N1 R1 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | municipio y día del hecho |
| `ARG-125-044` | Guanajuato · Salamanca | 2026-09-25 | rojo | ★★★☆☆ | I0 N2 R4 A0 | Latinus (2026/9/26); Diario de Yucatán (2026/09/27); La Prensa de Coahuila (2026/09/26) | SIN BOLETÍN / El Universal · Latinus | sin fuente institucional |
| `ARG-125-045` | Sinaloa · Culiacán | 2026-09-25 | rojo | ★★★☆☆ | I1 N0 R5 A0 | Línea Directa (2026-09-25); Luz Noticias (2026-09-25) | FGE Sinaloa (por cita) / — | sin fuente nacional |
| `ARG-125-046` | Sinaloa · Mazatlán | 2026-09-24 | verde | ★★★☆☆ | I2 N4 R4 A0 | La Silla Rota (2026/9/25); Por Esto (2026/9/25); Tribuna (2026/09/25); Diario de Tabasco (2026/09/25) | SSPC (por cita) · Gabinete (republicador) / La Silla Rota · Excélsior · El Universal | desglose de las 19 armas |
| `ARG-125-047` | Sonora · no verificado | 2026-09-24 | verde | ★★☆☆☆ | I1 N1 R2 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | municipio |
| `ARG-125-048` | Baja California · Mexicali | 2026-09-24 | verde | ★★★☆☆ | I1 N1 R2 A0 | — | Gabinete de Seguridad (por republicador) / Milenio | cifra de armas |
| `ARG-125-049` | Veracruz · Coatzacoalcos | 2026-09-24 | verde | ★★★☆☆ | I1 N2 R4 A0 | Somos la Resistencia (2026/09/24); En Blanco y Negro (2026/09/25) | FGE Veracruz (por cita) / UnoTV · Infobae | cifras de armamento (no publicadas) |
| `ARG-125-050` | Guanajuato · Comonfort | 2026-09-24 | verde | ★★★☆☆ | I1 N2 R4 A0 | La Silla Rota (2026/9/24); Proceso (2026/9/24); Infobae (2026/09/24) | Srio. de Gobierno de Gto. (por cita) / Meganoticias · Infobae | vínculo de los detenidos con la emboscada |
| `ARG-125-051` | Guerrero · Ajuchitlán del Progreso | 2026-09-24 | rojo | ★★★☆☆ | I1 N3 R3 A0 | Red Metropolitana (2026/09/26); Infobae (2026/09/30, 2026/10/04 y 2026/10/07); Proceso (2026/10/2 y 2026/10/3); MVS (2026/10/6); Diario de Yucatán (2026/10/03) | SIN BOLETÍN · juez federal (por cita) / Proceso · Infobae · MVS | número de víctimas y hora |
| `ARG-125-REC-001` | Puebla · Tecamachalco (Nicolás Bravo) | 2026-09-23 | rec | ★★★☆☆ | I1 N2 R1 A0 | Proceso (2026/9/24, dos notas); La Silla Rota (2026/9/29) | FGE Puebla (por cita) / Proceso · La Silla Rota | edad y nombre del edil |

## 13. Los dos controles editoriales — ejecutados, y los dos con hallazgos reales

**Racha intacta: novena y décima vez consecutivas «CORREGIR ANTES DE PUBLICAR».**

### 13.1 `procedencia-cifras` — 18 búsquedas `extended`
- Chihuahua 37/86/55,960 **solo por resumen** → el coordinador **localizó el literal** del emisor; se integra citándolo.
- **García: 4,771 contradicho por 5,093** (FGR) → corregido, con 5 largas, 2 cortas y 14 cargadores.
- **Santa María del Oro: el «literal» estaba truncado** y «cartuchos no publicados» era falso → 1,102 cartuchos integrados;
  cargadores 9 frente a 6, no integrados.
- Suchiapa: **15 frente a 19 policías** y móvil contradicho (entregar a grupos criminales / a cambio de dinero) → declarados.
- El Balcón: **13 privados no reverificado**; «tierras forestales» solo por cita → se apoya en el titular de Proceso («a cambio de
  sus tierras»).
- Guadalajara: la secuencia «3 y luego 4» no se sostenía; Marmor tituló 4 el 6-oct → reescrito; confianza sube a Medio.
- Hermosillo: la captura fue el martes 6-oct → retirada la marca de frontera.
- Valoración: «118 armas de 32 verdes» mezclaba un amarillo; «siete hallazgos en cinco entidades» eran seis → corregidos.
- El Rosario: 3 largas, 6 cargadores y 155 cartuchos solo por listado regional; «drones con fibra óptica» unía dos renglones →
  reservas escritas.

### 13.2 `editor-duplicidad`
- **Ningún duplicado real** contra el archivo ni entre fichas; 30 filas de armamento con ficha y viceversa; días de la semana
  correctos.
- **«Nueve filas de agregados» eran ocho** → corregido.
- **Arbitraje de agregados: sostenido**, con cuatro ajustes (ver §7.1).
- Morelia: razón del 🟡 corregida. FRONTERA DE VENTANA añadida a `-046`, `-047`, `-048`. Deslinde falso de García corregido.
- Coatzacoalcos 3 frente a 5 unificado. Frases falsas «los totales no se reimprimen» retiradas.
- Candidatos heredados sin novedad reducidos a una línea. Filas de ciclo y rendimiento retiradas del cartelón (método).
- Conclusión 5 —un negativo no demostrable— sustituida.

### 13.3 Totales antes y después de los controles

| Renglón | Borrador | Publicado |
|---|---|---|
| Semáforo | 16 / 3 / 32 | **16 / 3 / 32** |
| Armas | 118 | **125** |
| Cartuchos | 66,268 | **67,692** |
| Cargadores | 217 | **231** |
| Detenidos | 55 | **55** |

## 14. Herramientas

- `tools/validar.js`: **nueva comprobación** — ningún hecho propio con fecha anterior a la apertura y ningún `-REC-` posterior.
- `tools/gen-movil.py`: navegación de crimen organizado hasta el numeral **XX** (esta edición tiene XII).
- Radar: `WINDOW_DAYS` de **10 a 14** en el renderizador del cartelón, para que los ecos de once a catorce días no se amontonen en
  el centro. **Debe devolverse a la duración real de cada ventana** (ver orden de ARGOS 126).
- El cartelón se construyó con un generador de datos único (`datos.py` → fichas, panorama, `EVENTOS`, `EVENTOS_ARM`, totales); la
  móvil y el texto se generaron con `tools/gen-movil.py` y `tools/gen-texto.py`.
