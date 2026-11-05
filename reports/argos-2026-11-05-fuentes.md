# ARGOS 147 — Archivo de fuentes (corte 2026-11-05)

## 1. Identidad y ventana

- **ARGOS 147**, archivo `argos-2026-11-05.html` (jueves 5-nov-2026).
- **Ventana**: abre **mié 4-nov 06:52 CDMX** (cierre de ARGOS 146) y cierra **jue 5-nov 09:42 CDMX** (hora real del Bloque 0, `TZ=America/Mexico_City date`). El «Procede» (respuestas del destinatario) llegó hacia las 10:17, menos de dos horas después: no se movió el cierre.
- **Duración: 26 h 50 min** (cálculo con `date`); densidad **11 / 26,83 h = 0,41 hechos/hora**; **4 rojos / 26,83 h = 0,15 rojos/hora** (cálculo propio). Serie: 47 h 38 (145) · 91 h 38 (146, densidad 0,26) · **26 h 50 (147)**. Calendario: mié 4 · jue 5 (`WINDOW_DAYS = 2`).
- **Ciclo de rotación aplicado: B (Noreste + Golfo)**, después de la prioridad sobre el ciclo. **Resultado de la prioridad**: las 14 fiscalías `NO REVISADA` de 146 en sentencias quedaron **revisadas** (25 de 32 en total, contra 15 de 32 en 146); en armamento, BC, Col y Edomex (dos ediciones) revisadas, Son sigue sin páginas; alto impacto con consulta propia en las 8 que 146 dejó solo con consulta amplia. **Qué aportó el ciclo B**: Noreste y Golfo encabezaron el triaje judicial y no hallaron sentencia en ventana (FGJ Tamaulipas: último boletín FGJE-424-2026, 29-oct); el hallazgo judicial del corte (Oaxaca, 157 años) vino del Sureste.
- **Red**: `curl -s -o /dev/null -m 12 -w '%{http_code}' https://www.gob.mx/fgr` → `000` (proxy: `connect_rejected`) a las 09:42. Egreso bloqueado: solo WebSearch. Techo ★★★★☆; esta edición no supera ★★★☆☆.
- **Rama**: `claude/argos-147`, encima de `claude/argos-146` (las ocho fusiones de la orden, *fast-forward*; 268 archivos en `reports/` al arrancar).

## 2. Decisiones del destinatario (5-nov, en el Bloque 0)

| Decisión | Respuesta | Aplicación |
|---|---|---|
| (a) Excepción para rojos sin ruta fechada | **Sin respuesta** | Se mantiene la regla: un rojo sin ruta fechada no se ficha (Reynosa Puerta Sur, Valle de Chalco: vistos) |
| (b) Celaya `ARG-143-001` | **Mantener 🟡** | Cerrada. Sin fe de erratas |
| (c) Orizaba `ARG-132-002` | **🔴 por fe de erratas** | `ARG-147-FE-001` |
| (d) Ratificar `ARG-146-FE-001` (Pénjamo) y `-FE-002` (Cancún) | **Ratifica solo Cancún** | `-FE-002` firme. `-FE-001` **no ratificada**: Pénjamo `ARG-145-002` vuelve a 🟡 → `ARG-147-FE-003` |
| (e) Uruapan `ARG-146-007` en 🔴 | **No ratificado** | 🔴 → 🟡 con reserva «quién inició, no determinado» → `ARG-147-FE-002`. Occidente confirmó que el patrullaje solo consta por resumen y en la versión de la SSP |

## 3. Fe de erratas a ediciones anteriores (no van al cartelón)

| ARG-ID | Edición afectada | Corrección |
|---|---|---|
| `ARG-147-FE-001` | ARGOS 132 | **Orizaba `ARG-132-002`**: el agente ministerial herido murió el 30-oct (La Silla Rota, Golpe Político, Plumas Libres 2026/10/30; El Diario de Minatitlán 2026/10/31; N+ «FGE lamenta muerte de policía», sin fecha). Agravante «muerte de personal de las fuerzas de seguridad» → **🟡 → 🔴**, por decisión del destinatario. ARGOS 132: +1 rojo, −1 amarillo, +1 muerto por agresión |
| `ARG-147-FE-002` | ARGOS 146 | **Uruapan `ARG-146-007`**: **🔴 → 🟡**, por decisión del destinatario (patrullaje solo por resumen). ARGOS 146: 12 rojos, 6 amarillos |
| `ARG-147-FE-003` | ARGOS 145 | **Pénjamo `ARG-145-002`**: `ARG-146-FE-001` no ratificada (segunda muerte solo por resumen). Vuelve a 🟡; reserva viva. ARGOS 145: −1 rojo, −1 muerto |
| `ARG-147-FE-004` | ARGOS 146 | **Recuperaciones de la ventana de 146**: `ARG-147-REC-001` Champotón (4 muertos, 2 heridos), `-REC-002` Mazatlán centros de rehabilitación (3 muertos, 1 herido por titular) y `-REC-003` Mazatlán Coto Premier (explosivos, sin víctimas). Efecto sobre 146 (con FE-002): **15 rojos**, 6 amarillos, 6 verdes; **+7 muertos** por agresión |
| `ARG-147-FE-005` | ARGOS 146 | **Cláusulas de retiro cerradas**: `-019` Cocula (detención del 3-nov: boletín federal de acciones del 3-nov y Cúspide 2026/11/03; dos campos: Tlanipatlán y homicidio del abogado), `-020` Chenalhó (MVS 2026/11/3), `-021` Cancún (PorEsto 2026/11/3). Se quedan en 146. `-024` Ario de Rosales: día 31-oct por Latinus 2026/10/31; hora sin fijar: cláusula abierta. `-012` Cuautitlán Izcalli: sábado 31 tarde, solo por resumen: abierta |
| — | ARGOS 146 | **Irapuato `-006`**: heridos 2 (Correo, La Silla Rota 2026/11/4) o 4 (Latinus 2026/11/4): contradicho. **Suaqui Grande `-010`**: «cuatro cráneos», cifra del colectivo (Infobae, Tribuna 2026/11/04); deja de decir «3 o 4». **Acapulco `-003`**: martes 3, solo por resumen. Sin cambio de totales |
| — | ARGOS 146 | **Cocula `ARG-146-ARM-003`**: 2 largas, 1 corta, 12 cargadores, 335 cartuchos y 3 detenidos, solo por resumen del boletín federal: **siguen sin integrarse** |
| — | ARGOS 144 | **Detenidos por titular** (General Bravo 2; Lindavista 6): tercera edición sin cifra de autoridad (Lindavista: SSC solo por resumen). **Umbral cumplido: 8 → n/d** (`CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`) |

## 4. Boletín federal (triple consulta)

- **Acciones del 3-nov**: existe, indexado en `gob.mx/sspc/prensa/el-gabinete-de-seguridad-del-gobierno-de-mexico-informa-acciones-relevantes-del-3-de-noviembre-de-2026` y republicado por Milenio, Tallapolítica, Certeza Diario y Argonmexico (2026/11/04). Acciones del 3-nov: ventana de 146. Sirvió para cerrar la cláusula de Cocula.
- **Acciones del 4-nov**: `SIN RESULTADO INDEXADO EN VENTANA` en día suelto, rango («3 y 4») y título, al inicio y repetido al cierre. Trampa de año: Heraldo de México «4 de noviembre de 2025».

## 5. Resolución de encargos

- **Cláusulas de 146**: ver FE-005.
- **Reservas de 146**: Feria Ganadera `-022`: disparo a militares **no acreditado** (Infobae 2026/11/03); armas 5 en la mayoría (2 AK-47, 1 M15, 2 pistolas) y 4 en Meganoticias, solo por resumen · Nuevo Laredo `-009`: sin cifra oficial · Mexicali `-011`: Cerro Centinela «más de 10 restos óseos» (El Imparcial 2026/11/03); 51 hallazgos en 26 fosas acumulados, solo por resumen · Tepito `-001`: edad 3 (Quinta Fuerza) o 4 (La Silla Rota): sigue contradicha; sin detenidos.
- **Vistos sin ruta de 146**: Valle de Chalco (1.ª Secc. viernes 30; 2.ª Secc. 31-oct, solo por resumen) · Acolman (3-nov 22:46, solo por resumen: ventana 146, 🟡) · Jiutepec (nada de la ventana) · Mazatlán policía herido (2-nov, El Diario de Chihuahua 2026/nov/02) · Culiacán Alturas del Sur, mujer (2-nov o antes; pertenencia a la GN no acreditada) · Mazatlán centro de rehabilitación → `REC-002` · Meganoticias 784945: no localizada; 784934 = detención de Uruapan (`-017`).
- **Heredados de 145**: cláusulas `-010`, `-011`, `-012` sin novedad · REC-002 Mazatlán Los Ranchos, REC-004 Tetlatlahuca: sin novedad · REC-003 Coatzacoalcos: la «confirmación» de la FGE es pericial (un hombre), no cotejo genético.
- **Sentencias candidatas**: ninguna integrable. Nuevas: Oaxaca, 157 años (titular de Primera Línea 2026/11/04; boletín 2,948 de la FGEO solo por resumen; 87 a 6 m + 70 a = 157 a 6 m: contradice el titular) · Los Ramones, NL (FGR, «más de cinco años», MVS 2026/11/4) · FGR Tabasco, portación (solo resumen). Tulantepec: sin boletín de la audiencia del 5-nov. Huejotzingo: el boletín de 55 años de la FGE Puebla es de otro caso (`POSIBLE CASO HOMÓNIMO`). FGR Campeche, metilfenidato: no hallado (vinculación del 4-nov por portación; no es sentencia).
- **Seguimientos**: Orizaba → FE-001 (vinculación de cuatro por La Silla Rota 2026/11/3; causa 588/2026 por resumen) · Matamoros: fiscal Govea Orozco, disparo desde un helicóptero de la Guardia Estatal (Nación321, Expreso 2026/11/02; Síntesis 2026/11/03) · Coatzacoalcos «El Panda»: prisión preventiva, causa 94/2026, fosas de Jáltipan (Hora Cero 2026/11/04) · Indaparapeo: nuevo hecho, `ARG-147-004` · Magdalena de Kino, Juchitán, Xalapa: sin novedad · Tijuana `-143-005`, Mexicali `-145-003`, Almoloya: no consultados.

## 6. Fuentes por ficha (lista íntegra)

- **001 Cuernavaca**: La Razón, La Jornada, Infobae, Central Municipal, Código Qro, Quinto Poder (2026/11/04); Proceso (2026/11/4); Informador (20261104); El Heraldo de SLP (2026/11/05); SinEmbargo, Excélsior, Reforma, Milenio (dos notas), Ejecentral, TV Azteca, Imagen TV (sin fecha).
- **002 Tancítaro**: Grupo Marmor (2026/11/04), Media News (2026/11/05), RED113 (2026/11); Respuesta, La Voz de Michoacán, IMN (sin fecha). El Congresista (herencia, «4 de octubre»): descartado.
- **003 Chilpancingo**: Informador (20261104), Infobae (2026/11/05); El Universal, El Congresista, Milenio, Meganoticias (785408), Bajo Palabra (sin fecha).
- **004 Indaparapeo**: Grupo Marmor (2026/11/05), RED113 (2026/11); Respuesta, La Voz de Michoacán, Indicio, La Redacción («drones explosivos») (sin fecha). Una misma nota republicada.
- **005 Pénjamo**: Correo (2026/nov/04), AM (2026/11/05); Milenio, N+, La Redacción, Telediario (sin fecha); X de El Sol de Irapuato (abierta).
- **006 Culiacán Alturas del Sur**: Línea Directa (2026-11-04).
- **007 Olinalá**: Informador (20261104), Infobae (2026/11/05); El Universal, El Congresista (sin fecha).
- **008 Culiacán Guadalupe Victoria**: Línea Directa (2026-11-04, nota 1733481).
- **009 Mazatlán, Mercado Hidalgo**: Luz Noticias (2026-11-04, nota 313494); El Universal, Yahoo (sin fecha).
- **010 Mazatlán, av. Carlos Canseco**: Luz Noticias (2026-11-04, nota 313509); Sinaloahoy, El Universal (sin fecha).
- **011 Yucatán**: Noticaribe (2026/11/04).
- **REC-001 Champotón**: La Prensa de Coahuila (2026/11/02), PorEsto (2026/11/5); TV Azteca, Omnia, Tribuna Campeche, Quinta Fuerza (sin fecha).
- **REC-002 Mazatlán, centros de rehabilitación**: Herqles (2026/11/02), Guardia Nocturna (2026/11); Noroeste, El Universal, Sergio Valle (sin fecha).
- **REC-003 Mazatlán, Coto Premier**: Luz Noticias (2026-11-04), Diario de Yucatán (2026/11/04), Los Noticieristas (2026/11); Noroeste (dos notas; la de la alcaldesa da las ~06:34, solo por resumen), N+, Meganoticias (785608), ENfoque, El Universal (sin fecha).

## 7. Procedencia: decisiones de clasificación

1. **Coto Premier → `REC-003`**: el borrador lo fichó como `ARG-147-002` con «mañana, solo por resumen». R1 de procedencia halló «cerca de las 6:34» (Noroeste, solo por resumen). Por la regla de la plantilla —si el único dato de hora apunta a antes de las 06:52 del 4, es de la ventana de 146— pasa a recuperación de 146, fuera de totales. A diferencia de Ario de Rosales (146), aquí la hora sí apunta a la ventana anterior.
2. **Chilpancingo `-003` 🔴**: los titulares hablan de «dos cuerpos hallados» y de «dos hombres asesinados y torturados» (Bajo Palabra); se cuentan como muertos por agresión. Día solo por la nota agregada del 4-nov (Informador 20261104) y el resumen. Confianza Bajo.
3. **Olinalá `-007` 🟡**: enfrentamiento entre grupos; quién inició, no determinado; los dos muertos, integrantes de grupos armados, solo por resumen. Se cuentan en «muertos por agresión» con la nota de que incluyen combatientes.
4. **Indaparapeo `-004` 🔴**: «drones» por titular; la capacidad explosiva, solo por el titular de un medio (La Redacción): reserva declarada. `FRONTERA DE VENTANA` por publicación del 5-nov.
5. **Culiacán y Mazatlán `-008` a `-010`**: excluidos en el borrador como «sin ruta» o «día no fijado»; R1 de procedencia halló rutas 2026-11-04 del mismo tipo que la de `-006`. Se fichan con el mismo criterio.
6. **Guerrero**: «siete hombres en varios municipios», por titular (Infobae); «cinco municipios», titular de El Universal según el equipo Sureste, no reencontrado por R1: se cita como «solo por resumen».
7. **Detenidos en aseguramiento**: ninguno con cifra de autoridad → `n/d`.

## 8. Controles editoriales

**Ronda 1** (en paralelo):
- `editor-duplicidad` R1 — CORREGIR (9 hallazgos; 0 duplicidades de hechos). Aplicados: heridos de las recuperaciones «por titular» · deslinde de REC-002 (visto en el archivo de equipos de 146, no en su cartelón) · seguimiento de Orizaba retirado del cartelón (repetía 146; pasa a FE-001) · Matamoros citado como `ARG-144-008 / ARG-145-REC-001` · Pénjamo con `ARG-138-013` · Conclusiones reescritas como patrones, sin repetir titulares · vistos de Guerrero, Culiacán y Mazatlán solo en deslindes · Tuxtla solo en armamento · este archivo.
- `procedencia-cifras` R1 — CORREGIR (8 hallazgos; 24 de 24 búsquedas). Aplicados: Coto Premier → REC-003 (§7.1) · «detonan artefacto en cochera y localizan otro», por titular (Los Noticieristas); N+ por *slug* · tres homicidios con ruta fechada fichados (§7.5) · «cinco municipios» solo por resumen · Chilpancingo como hallazgo de dos hombres asesinados y torturados · Los Ramones: FGR, arma de uso exclusivo y drogas, 5 a 5 m 19 d por resumen · Oaxaca: 157 años por titular frente a 157 a 6 m por suma · REC-002 sin hora · Mayatecún II por titular · Pénjamo sin «Jardín Ana María Gallaga» (no reencontrado) · Yucatán: homicidio original del 22-jul, solo por resumen.

**Ronda 2** (en serie): ver §9.

## 9. Ronda 2 (en serie)

_Pendiente._

## 10. Presupuesto de búsqueda

Control 2 · coordinador 14 + Tijuana 1 + 2 de repetición federal = 17 de 18 · ola 148 de 150 (Noroeste 24, Noreste 25, Occidente 25, Centro 25, Golfo 25, Sureste 24) · procedencia R1 24 de 24 · R2 pendiente.

## 11. Hallazgos de método (no van al cartelón)

1. **Hora por resumen anterior a la apertura**: Coto Premier entró al borrador como hecho del corte porque el equipo solo vio «mañana»; la hora 06:34 apareció en una nota sobre otro tema (refuerzo de la GN). La búsqueda de hora debe incluir notas de contexto del mismo día.
2. **Criterio «sin ruta» aplicado de forma desigual**: tres homicidios de Sinaloa con ruta 2026-11-04 se dejaron como vistos mientras otro del mismo medio se fichaba. Antes de declarar «sin ruta», buscar el topónimo exacto en el medio que ya dio ruta.
3. **Ventana corta con apertura de madrugada**: diez de once hechos llevan `PUBLICADO EL DÍA DE APERTURA SIN HORA`. Con cierres de ventana a primera hora, casi todo el día de apertura queda bajo cláusula: los totales son frágiles por construcción.
4. **Seguimiento repetido**: el seguimiento de Orizaba se copió de 146 sin dato nuevo. Un seguimiento entra al cartelón solo con dato nuevo con fuente propia.
