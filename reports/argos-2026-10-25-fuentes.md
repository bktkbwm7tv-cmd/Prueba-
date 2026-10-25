# ARGOS 140 — Archivo de fuentes

**Corte**: 2026-10-25 · **Ventana**: 21-oct 10:23 → 25-oct 07:45 CDMX (**93 h 22 min**; `WINDOW_DAYS = 5`) · **Densidad**: 23 hechos propios / 93,37 h = **0,25 hechos/hora**, cálculo propio (tras la ronda 1: 8 🔴, 10 🟡, 5 🟢; 12 entidades).
**Hora de cierre**: hora real de la orden «Procede» del destinatario (07:45 CDMX del domingo 25). Consultas de la ola y del coordinador de 07:46 a 07:57; `procedencia-cifras` R1 terminó a las **08:14 CDMX** (hora real leída al recibir su informe): marca «Consulta 07:46-08:14». La ronda 2 no busca. Los hechos posteriores a las 07:45 pertenecen a ARGOS 141.
**Orden**: la orden de ARGOS 140 del 22-oct no se ejecutó (la sesión se detuvo tras el Bloque 0); se rehízo el 25-oct (`reports/_ordenes-ARGOS-140.txt`, commit `c0448f3`). No hay edición del 22 al 24-oct.

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-25-equipos.md`. Plantilla: `tools/plantilla-equipos-140.md`. Generador: `tools/datos-argos-140.py`.

## 1. La base

- 22-oct 08:14: clon sin rama en `60f2777`, por detrás; *fast-forward* a `origin/main` (`d0c6ab7`) y a `origin/claude/argos-139-qe9f01` (`9712e79`, que lleva encima de `3c343ac` la orden del 22-oct). 219 archivos en `reports/`; última edición `argos-2026-10-21`.
- 25-oct: rama `claude/argos-140` creada sobre `9712e79`; ninguna edición del 22 al 25. 219 archivos antes de esta edición; 226 después (5 de la edición y la orden de 141).

## 2. Red y modo de búsqueda

- `curl https://www.gob.mx/fgr` → `000` (22-oct 08:14 y 25-oct 06:52; `connect_rejected` del proxy). **Egreso bloqueado: solo WebSearch.** Techo ★★★★☆; esta edición no supera ★★★☆☆.
- Consulta de control en los dos modos: `extended` trae hechos de la ventana (Purísima del Rincón, Uruapan, Ozumba, Iztapalapa); `standard`, nada de 2026. **Todo `extended`.**
- Presupuesto: control 2 · ola 150 (6 × 25, agotada en los seis equipos) · coordinador 16 · `procedencia-cifras` R1 hasta 30. Tope 200.

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

- **Ciclo A** (Noroeste + Centro encabezan el triaje judicial), después de la prioridad sobre el ciclo.
- **Sentencias `NO REVISADA` en 139 (11)**: revisadas ahora BC, Chih, CDMX, Pue, Tlax, Hgo, Qro (7); consultadas sin páginas del dominio Sin, Tamps, Camp (3); sigue `NO REVISADA` BCS (1).
- **Armamento `NO REVISADA` en 139 (19)**: revisadas ahora Coah, NL, Tamps, SLP, Mich, Gro, Oax, Yuc (8); siguen sin dominio BC, Son, Dgo, Chih, Sin, Gto, Mor, Tlax, Hgo, Camp, QRoo (11); Coahuila, revisada (`coahuila.gob.mx`, SRIV).
- **Alto impacto solo amplia en 139 (7)**: BC, Chih, Coah, NL, Ags, Gto, Edomex — **las siete con consulta propia**.
- **Qué aportó la rotación**: Noroeste (judicial) resolvió el exfiscal en sus dos fueros y fijó las tres candidatas heredadas; Centro (judicial) estableció que la pena de Tulantepec **no se dictó** el 21-oct (audiencia pospuesta). Ninguna sentencia estatal integrable: el ciclo hace demostrable el `SIN DATO`, no garantiza hallazgo.

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **21-oct** | **Existe**: «acciones relevantes del 21 de octubre de 2026», por republicadores (Ultranoticias; RED113; Talla Política; Certeza Diario). Colima, Durango, Quintana Roo, Veracruz, Chalco, Tlajomulco, Puerto Morelos: cifras solo por resumen → vistos |
| **22-oct** | **Existe**: Milenio (slug «22-de-octubre-2026»); SICOM; RED113; Talla Política. Culiacán (ARG-140-023), Iztapalapa-Puebla-Amozoc (ARG-140-022), Ojinaga, Hidalgo-Juárez, Monterrey, Morelos |
| **23-oct y 24-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto, rango «23, 24 y 25», título sin `site:`), repetidas al final |
| **gabinetedeseguridad.gob.mx** | El buscador solo devuelve el agregado del 9 al 11-oct (contenido/9926) |

Corroboración débil por construcción: los republicadores del mismo boletín son una fuente.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Ciclo** | A, declarado (§3) |
| **1. Tulantepec** | **Sin pena**: la audiencia de individualización del 21-oct se pospuso «por falla de energía» (titular de La Jornada Hidalgo, sin fecha en la ruta); nueva fecha 28-oct, solo por resumen; plazo 28-nov, por resumen. «40 a 90 años»: estimación de la asesoría de víctimas. Sin boletín de la PGJEH → candidato en la tabla de sentencias, no integrable |
| **2. Exfiscal (`ARG-136-006`)** | **Estatal, jueves 22**: vinculado por ejercicio ilegal del servicio público; coalición descartada (titulares). **Federal, sábado 24**: vinculado por traición a la patria; resolución publicada el 25, con marca de frontera. Las dos, en el bloque de seguimientos del panorama (§6). Sin comunicado de la FGR ni de la FGE |
| **3. El Terrero (`ARG-139-REC-002`)** | «Reanudan ataques» (El Diario de Chihuahua 2026/oct/20) se refiere al ataque del 19: **sin nueva agresión con fecha**. Sin parte de la Defensa |
| **4. Fichas de 139** | `-002` sin causa ni identificación oficial → **no baja** · `-001` parentesco contradicho; ~12:10 por resumen · `-003` adscripción por reconocimiento de compañeros; la FGEO vincula a 7 detenidos con 6 homicidios (`ARG-140-021`) · `-008` ~06:00 solo por resumen → **no se retira** · `-005` docente de secundaria pública por medios, sin acreditación institucional → **sigue 🟡**; detenido el presunto homicida (`ARG-140-020`) · `-007` la «21-oct 07:04» es hora de publicación de N+: no hay otro hecho · `-REC-003` herido, fuera de peligro; cargo sin arbitrar · `-004/-010` «al parecer repartidor» solo en La Foresta (Noroeste) |
| **5. Seguimientos** | Xalisco/Tecuala: tres fosas con cinco cuerpos y diez detenidos, por resumen → posible duplicidad con `ARG-133-REC-007`, no se integra · Cachanillas: sin cifra oficial · Río Bravo: el día sigue solo por resumen; un medio lo cuestiona (Nota Tamaulipas 2026/10/19) → fe de erratas a 129 **sigue condicionada** |
| **6. Sentencias candidatas** | Culiacán (Daniel «N», 18 años), Ensenada (158 años 9 meses = 135 + 10 años 9 meses + 13, por medios), General Cepeda (13 años 4 meses), Caborca (8 años): todas publicadas antes de la ventana, sin boletín |
| **Heredados** | Nogales, Ajuchitlán (sigue desaparecida la séptima persona al 20-oct), Apatzingán, El Tívoli, Coquimatlán (tres muertos el 15-oct, ¿= caso previo?), Linares, Tepic, Patamban (decisión del destinatario), Taxco (vinculación no localizada): sin avance que cambie un color |

## 6. Arbitrajes del coordinador

Ver «Arbitraje del coordinador» en `reports/argos-2026-10-25-equipos.md`. Tras la ronda 1:
- **Exfiscal fuera del semáforo**: sus dos vinculaciones (22 y 24-oct) son desarrollo de un caso ya publicado (`ARG-136-006`): pasan al bloque de seguimientos del panorama, como en ARGOS 137-139. Los ARG-ID que el borrador les dio (`-022` y `-023`) se reasignaron tras la renumeración a los cateos de Puebla y a la detención de Culiacán.
- **Dos fichas nuevas**: cabeza humana de Huimanguillo (`ARG-140-007`, 🔴, Diario de Yucatán 2026/10/21, hallada por `procedencia-cifras`) y Chimalhuacán (`ARG-140-011`, 🟡, El Gráfico 2026/10/22). **Renumeración**: del borrador a la edición, -007→-008, -008→-009, -009→-010, -010→-012, -011→-013, -012→-014, -013→-015, -014→-016, -015→-017, -016→-018, -017→-019, -018→-020, -019→-021, -020→-022, -021→-023.
- **Unidad de conteo**: Álamo/Papantla (`-017`) y Cosoleacaque (`-018`) quedan en una ficha cada uno porque la fuente publica los dos ataques en una sola nota y no hay reparto acreditado de víctimas; León (`-005`), una ficha porque el titular agrega los cinco cuerpos. Criterio: **una ficha por nota fuente cuando la fuente agrega sin reparto acreditable**; se separan en cuanto una fuente reparta.
- **Colores con reserva**: `-004` rojo con el día solo por resumen (excepción declarada) · `-009` 🟡, la SSP dice que la agresión fue contra el conductor · `-016` 🟡, quién inició no consta · `-018` 🟡, un solo ataque no consta · `-020` (Xalapa) 🟢: detención de hoy por un delito de la ventana anterior.
- **`-REC-003` Ecatepec**: los resúmenes convergen en la noche del martes 20 o la madrugada del 21 antes de las 10:23; se retiró la hipótesis del miércoles por la noche (ninguna fuente la sostiene).
- **El «Arbitraje del coordinador» del archivo de equipos (anterior a la ronda 1) queda superado por esta sección.** Los vistos de los equipos sin ficha (Uruapan Valle de San Pedro, SLP ambulancia, Tula de Allende, Yecapixtla, Culiacán Los Mezcales y Capistrano, Ensenada El Faro, Cuichapa, Coatzacoalcos, Tijuana casino, detenido en Jalisco, Ziracuaretiro) conservan el motivo escrito en el archivo de equipos.
- **Vistos, con motivo**: Sonora, «abaten a presunto jefe de grupo armado» (ntv.com.mx 2026/10/24): municipio y circunstancias solo por resumen, sin presupuesto para cotejo → ARGOS 141 · Coicoyán de las Flores (exsíndico e hijo hallados muertos): fecha sin fijar; sin precedente (grep) → ARGOS 141 · Celaya, Rancho Seco (24-oct): sin ruta fechada · Jiutepec Civac (23-oct): solo portada, sin cuerpo · Cajeme, cuatro ataques del 20-oct: ventana de 139, homicidios separados que la Fiscalía relaciona con narcomenudeo; ninguna autoridad los acredita como ataque coordinado → 🟡, no se recuperan · verdes del boletín federal sin armamento (Durango 109 kg, Colima, Monterrey 220 kg, Morelos, Chalco, Tlajomulco, Puerto Morelos): cifras solo por resumen, sin ficha.

## 7. Fe de erratas (no va al cartelón)

- **`ARG-140-FE-001` — ARGOS 139**: las recuperaciones `ARG-140-REC-001` (Ario de Rosales, 3 muertos y 2 heridos) y `-REC-002` (Cocotitlán, 1 muerto y 1 herido) son rojos de su ventana; `-REC-003` (Ecatepec, 4 muertos y 1 herida), también, con el día solo por resumen. Efecto sobre ARGOS 139: **rojos de 3 a 5, muertos por agresión de 9 a 13 y heridos de 1 a 4** (REC-001 y -002, firmes); **condicionado**, por el día solo por resumen de REC-003: rojos a 6, muertos a 17 y heridos a 5 (cálculo propio). No se publica en el cartelón.
- **Xalisco/Tecuala (`ARG-125-003`)**: ARGOS 139 imprimió «tres fosas más en Tecuala y diez detenidos» solo por resumen; esta es la segunda edición sin respaldo citable → umbral de fe de erratas: el renglón pasa a `CANTIDAD NO DETERMINADA — NO SE INTEGRA AL TOTAL NUMÉRICO`. «Cinco cuerpos» aparece por primera vez en la investigación de 140 (solo por resumen): no integrable, nunca impreso.
- Condicionada, sin cambio: Río Bravo (129).

## 8. Registro del barrido — por entidad

Ver el «Indicador de cobertura» del cartelón y los informes íntegros. Sentencias: 11 revisadas, 5 dominios sin páginas, 16 `NO REVISADA` (corregido en R1: Occidente y Tabasco declararon `NO REVISADA`). Armamento: 12 por dominio, 3 dominios sin páginas, 17 `NO REVISADA`. Alto impacto: 17 con consulta propia, 15 solo amplia. Dominios nuevos confirmados: `comunicacion.fiscaliaveracruz.gob.mx`, `portal.fgeo.gob.mx`, `fiscaliageneralqro.gob.mx`, `seguridad.slp.gob.mx`; listados de la FGR en `fgr.org.mx`.

## 9. Emisores por ficha

El recuento I/N/R/A de cada ficha está en `tools/datos-argos-140.py`; las URL, en el archivo de equipos.

## 10. Desglose de cálculos propios

- Muertos por agresión en hechos propios: 15 = 2 (-001) + 1 (-002) + 1 (-003) + 2 (-004) + 1 (-010) + 1 (-011) + 1 (-012) + 1 (-013) + 1 (-014) + 1 (-015) + 1 (-017) + 2 (-018).
- Heridos: 8 = 1 (-001) + 1 (-009) + 1 (-010) + 3 (-011) + 2 (-017). Cuerpos hallados: 7 = 5 (-005) + 2 (-006); la cabeza (-007) y los restos de Reynosa (-008), fuera.
- Recuperaciones: 8 muertos (3 + 1 + 4) y 4 heridos (2 + 1 + 1), fuera de todo total.
- Armamento: 36 armas sin categoría y 4 detenidos (ARM-001, único evento); demás categorías `n/d`.
- Entidades: 12 (CDMX, Gto, Sin, Tab, Tamps, Mor, Edomex, NL, Mich, Ver, Oax, Pue). Densidad: 23 / 93,37 = 0,25.

## 11. Los dos controles editoriales

**Ronda 1** (en paralelo): `editor-duplicidad` — CORREGIR (21 hallazgos; sin duplicidades reales) · `procedencia-cifras` — CORREGIR (20 hallazgos; sin cifras inventadas ni descuadres; 30 de 30 búsquedas). Aplicados: exfiscal al bloque de seguimientos; FE-001 a 139; Huixtla como omisión de 139 no recuperable; «El Obraje Diamante» retirado; Juchitán como vinculación posible sin desglose; criterio de unidad de conteo escrito (§6); Valoración y Conclusiones rehechas sin repetir fichas ni totales y sin mecanismos de método; portada con acciones de cotejar, auditar y vigilar; marca de apertura de Huimanguillo corregida (fosa: día del hallazgo solo por resumen); indicador de armamento con las tres casillas separadas; cobertura de sentencias 11 + 5 + 16; recuentos I/N/R/A unificados (republicaciones una vez); vistos de armamento sin cifras («no heredables»); Tecuala sin números; `n/d` en tarjetas y totales; «37 armas», «12 estudiantes», «~06:10», «blanca» y «Los Noticieristas con fecha» retirados; «20 casquillos» respaldado por el *slug* de Reporte 18; adscripción del C4i por *slug*; líder de Los Ranas por titular; orden del panorama por fecha y hora; 17 años de Cosoleacaque y «este sábado 24» de Ozumba, solo por resumen. **No aplicado**: separar Álamo/Papantla y Cosoleacaque (§6, criterio de unidad); fichar Sonora y Coicoyán (sin presupuesto: ARGOS 141).

**Ronda 2** (en serie): `editor-duplicidad` R2 — CORREGIR (19 hallazgos; sin duplicados; aritmética y paridad OK). Aplicados: Conclusión 1 rehecha con la serie completa de Guanajuato del índice (ARG-124-001, -125-044, -137-REC-001, -140-002: sexto agente desde el 23-sep, cálculo propio); Chimalhuacán con la cifra de su propia nota (1 muerto y 3 heridos, solo por resumen; heridos de 7 a 8); `n/d` también en el mapa de aseguramientos; Tecuala atribuido con exactitud; numeración del archivo de fuentes corregida; Conclusión 4 sin «dos municipios»; nota de fichas que agrupan dos ataques; posible identidad en `-023`; segunda fuente de las 36 armas documentada (resumen del boletín federal en Milenio) y nivel Bajo sostenido; listados de la FGR de Veracruz y Sonora dispuestos; vistos remitidos al archivo de equipos y arbitraje previo marcado como superado; remisión de cifras al archivo de equipos; Coahuila revisada en armamento (8 + 11); deslindes de `-008` y `-017` remitidos al archivo de equipos de 139; empleo contradicho en `-003`; «FGR revisada: Sí»; aviso del móvil (`tools/gen-movil.py`) corregido; FE-001 con REC-003 condicionada. **Índice y `_pendientes.md`**: se actualizan en el cierre, después de `procedencia-cifras` R2.

## 12. Herramientas

`python3 tools/datos-argos-140.py reports/argos-2026-10-21.html reports/argos-2026-10-25.html` · `python3 tools/gen-movil.py 140 2026-10-25 139 2026-10-21 07:45` · `python3 tools/gen-texto.py reports/argos-2026-10-25.html reports/argos-2026-10-25.txt` · `node tools/validar.js reports/argos-2026-10-25.html 2026-10-21 2026-10-25` → validación OK.

## 13. Lecciones de método (no van al cartelón)

1. **La ola de 25 búsquedas por equipo no alcanzó la consulta de fecha en la ruta por día** en ningún equipo: en una ventana de cinco días, el presupuesto se agota en encargos y prioridad antes de llegar al barrido por fecha.
2. **El recall nacional del coordinador volvió a aportar rojos que los barridos no traían** (Iztapalapa, Ecatepec, Ario de Rosales) y las pistas reenviadas a los equipos llegaron tarde a dos de ellos (Noroeste, Golfo), que ya habían agotado su tope. Conviene hacer el recall **antes** de lanzar la ola.
3. **Varias consultas `site:` con `OR`** se desperdiciaron (Noroeste, Occidente) pese a la regla escrita: el buscador ignora el operador.
4. El buscador indexa poco del 23 al 25-oct (fin de semana): los totales de esos días son mínimos, no exhaustivos.
