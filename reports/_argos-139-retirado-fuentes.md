> ⚠️ **VERSIÓN RETIRADA** — ARGOS 139 producido el 20-oct con ventana de 43 min (07:06 → 07:49) y retirado por el destinatario el mismo día por falta de materia. **No es una edición publicada**: sus ARG-ID no existen. Se conserva como **insumo** del nuevo ARGOS 139 (encargos respondidos, Río Bravo con el día corregido, vistos, cobertura), que debe reverificar lo que use.

# ARGOS 139 — Archivo de fuentes

**Corte**: 2026-10-20 (segundo corte del día; archivos `argos-2026-10-20b.*`) · **Ventana**: 20-oct 07:06 → 20-oct 07:49 CDMX (**43 min**; `WINDOW_DAYS = 2` sin cambio: el radar no tiene ecos propios) · **Densidad**: 0 hechos propios / 0,72 h = **0,00 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real del Bloque 0 de la sesión (07:49 CDMX). El destinatario ordenó primero aplazar ARGOS 139 al 21-oct (y fijó Río Bravo en rojo; commit de las 07:53) y, a las 07:58, producirlo con datos de hoy. La primera búsqueda (consulta de control) es posterior a las 07:58; el `curl` de las 07:49 no es consulta de fuentes. Los hechos publicados después de las 07:49 no se asignan a esta ventana. Consultas de 07:58 a 08:20 CDMX (marca «Consulta» del cartelón; la última búsqueda, de `procedencia-cifras` R1, terminó antes de las 08:20; la segunda ronda no busca).

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-20b-equipos.md`. Plantilla de los equipos: `tools/plantilla-equipos-139.md`.

## 1. La base

- Clon en la rama de sesión `claude/argos-139-9anrf5`, en `60f2777` (orden de ARGOS 126), por detrás de `origin/main`. Se fusionaron en *fast-forward* `main` (`b0558a3`) y `claude/argos-129` … `-138`, sin conflicto; HEAD `9cca5c8`.
- `reports/`: 210 archivos, última edición `argos-2026-10-20` (ARGOS 138), como estaba previsto.
- **Nombre de archivo**: ARGOS 139 comparte fecha de corte con ARGOS 138. Para no sobrescribirlo, sus archivos llevan sufijo `b`. `tools/gen-movil.py` muestra la fecha sin el sufijo (cambio de cuatro líneas).
- **Incoherencia horaria en ARGOS 138**: su marca «Consulta» dice 07:06-09:30 del 20-oct, pero su último commit es de las 07:45 del 20-oct. La marca no puede ser correcta. Se registra en `_pendientes.md`; no se corrige en su cartelón desde aquí.

## 2. Red y modo de búsqueda

- **Egreso**: `curl -s -o /dev/null -m 12 -w '%{http_code}' https://www.gob.mx/fgr` → **`000`**, 07:49 CDMX. Bloqueo vigente. **Ningún documento oficial leído íntegro.** Techo de política **★★★★☆**; esta edición no supera **★★★☆☆**.
- **Consulta de control** («asesinan ataque armado "este martes" 20 de octubre 2026»): `extended` → Juchitán (`ARG-138-001`) y Cuajinicuilapa (`ARG-138-REC-001`); `standard` → nada de México. Se mantuvo `extended`.
- **Presupuesto**: control 2 + ola 156 (6 × 26) + coordinador 7 = **165**; `procedencia-cifras` hasta **30** → hasta **195 de 200**.
- **Grep**: los equipos no tienen Bash; cotejaron con la herramienta Grep. El coordinador repitió con Bash los topónimos de los candidatos (Sonoyta/Peñasco, Casandra/Río Bravo).

## 3. Rotación — prioridad sobre el ciclo y CICLO C, declarados

| Renglón | Resultado |
|---|---|
| Ciclo | **C** — Occidente y Sureste encabezaron el triaje judicial tras la prioridad (tabla de `CLAUDE.md`) |
| Prioridad — sentencias (17 `NO REVISADA` en 138) | **Revisadas (13)**: BC (`fgebc.gob.mx`), BCS (`pgjebcs.gob.mx`, ruta opaca), Chih (`fiscalia.chihuahua.gob.mx`, junio) · Jal (`fiscalia.jalisco.gob.mx`, agosto), Nay (`fgenay.gob.mx`), Ags (`fiscalia-aguascalientes.gob.mx`, 2-oct), Mich (`comunicacion.fiscaliamichoacan.gob.mx`, 2025) · CDMX (`fgjcdmx.gob.mx`, 2025), Edomex (`fgjem.edomex.gob.mx`, edictos), Pue (`fiscalia.puebla.gob.mx`, febrero), Qro (`fiscaliageneralqro.gob.mx`, 25-ago) · Oax (`portal.fgeo.gob.mx`, 13-oct) · QRoo (`fgeqroo.gob.mx`, 16-ago). **Siguen `NO REVISADA` (4)**: Sin (`fiscaliasinaloa.mx` solo devuelve documentos normativos; `.gob.mx`, duodécima edición sin devolver), Tlax, Chis (`fiscaliachiapas.gob.mx` y `fiscalia.chiapas.gob.mx` no devuelven), Camp (`fgecam.gob.mx` y `fgecampeche.gob.mx` no devuelven) |
| Prioridad — armamento (13 `NO REVISADA` en 138) | **Revisadas (11)**: Chih (fiscalía; `ssp.chihuahua.gob.mx` no es dominio válido), Sin (`sspsinaloa.gob.mx`), Coah (`sitio.fgecoahuila.gob.mx`), Tamps (`tamaulipas.gob.mx`, `fgjtam.gob.mx`), Mich (`ssp.michoacan.gob.mx`, julio), Ver (`veracruz.gob.mx/seguridad`, 29-ago), Tab (`tabasco.gob.mx`, junio), Oax (`portal.fgeo.gob.mx`), Camp (`spsc.campeche.gob.mx`, agosto), Yuc (`ssp.yucatan.gob.mx`, 2021-2023), QRoo (`fgeqroo.gob.mx`, marzo). **Siguen `NO REVISADA` (2)**: Jal (`seguridad.jalisco.gob.mx` no devuelve), Gto (ningún dominio devuelve) |
| Prioridad — alto impacto (Ags) | **Consulta propia**: `SIN RESULTADO INDEXADO EN VENTANA` |
| Rendimiento del ciclo | **Ninguna sentencia integrable.** Occidente: cinco fiscalías devolvieron dominio, ninguna con ítem de octubre salvo Ags (2-oct, por listado). Sureste: Oaxaca (boletines 2879 y 2889, 9 y 13-oct, por listado) y Guerrero (15-oct, por resumen), fuera de ventana. Chis, Camp y Yuc: dominios de fiscalía no confirmados |
| Regresión por rotación | Sentencias: Son, Dgo, Coah, NL, SLP, Zac, Gto, Mor, Hgo, Yuc pasan a `NO REVISADA` (10, más las 4 que siguen). Armamento: BC, BCS, Son, Dgo, NL, Nay, Ags, Col, CDMX, Edomex, Mor, Pue, Tlax, Hgo, Qro, Gro, Chis (17, más Jal y Gto). **Prioridad sobre el ciclo en 140** |

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **19-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas; el agregado del 16, 17 y 18-oct, publicado el 19, ya está registrado en ARGOS 137 |
| **20-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (por rango, solo el del 20-oct-**2025**) |
| `gabinetedeseguridad.gob.mx/resultados` | dominio no devuelto (solo una pieza de 2025) |

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Río Bravo** | **🔴 por decisión del destinatario (20-oct, antes de las 07:53: commit `f909e71`)** → `ARG-139-REC-001`. Día del hecho corregido: **sábado 10-oct**, por dos resúmenes coincidentes (no por fragmento): ventana de **ARGOS 129**, no de 136. Fuentes con fecha en la ruta: El Diario de Chihuahua 2026/oct/17, Infobae 2026/10/18, Expreso 2026/10/18, ABC Noticias 2026/10/19, En Línea Directa 2026/10/19 |
| **1. Ecatepec, col. Luis Donaldo Colosio** | **No se ficha.** Fuente única (El Independiente 2026/10/19, agregado), que recicla al menos un hecho del 13-oct (Naucalpan, La Mancha 1). Un titular de La Prensa sobre padre e hijo en un taller de Ecatepec, por la reparación de un auto, aparece con antigüedad de unos 32 días según el metadato del buscador: posible hecho de septiembre. Sin comunicado de la FGJEM. **Visto sin fijar** |
| **2. Fichas de 138** | `-001`: «miércoles» incompatible con el calendario; heridos 2 o 3; menor de 2 o 3 años; sin comunicado; sin ruta fechada · `-002`: sin ruta fechada; ejido Azucarero, solo por resumen; ADN en curso; versiones lo vinculan con dos jóvenes desaparecidos · `-007`: segunda ruta (Luz Noticias 2026-10-20); «militares agredidos» solo por resumen; sin parte · `-008`: hora no fijada, sin base para fe de erratas · `-011`: primera publicación ABC 2026/10/19; 4 operativos por titular (MVS 2026/10/20) o 2 (Posta, solo por resumen); 3 armas cortas, solo por resumen · `-009/-010`: El Diario de Chihuahua 2026/oct/20; sin estado de salud ni situación jurídica · `-006`: segunda fuente (Azteca Sinaloa, sin fecha); Sinaloahoy dice «este martes»: **día contradicho**; homicidio homónimo en plaza de La Marina (Noroeste, 11-oct, sin día en la ruta) · `-013`: sigue con fuente única |
| **3. Vistos** | Acapulco ×2: El Sur sin ruta con fecha; taxista ~15:00 (IRZA) o >16:00 (El Sur) · Cuernavaca: sin ruta con fecha · Laureles Pinos: **buscado**, sin hecho de octubre · Palmanova: lunes 19, 18:00-18:45, Luz Noticias 2026-10-19, 🟡 de 138 · policía municipal de Culiacán: no fechable · narcomanta: es de **Ciudad Juárez**, 4 narcomenudistas del domingo 18 (El Diario de Chihuahua 2026/oct/19) · Puerto Morelos: cateo de la FGR, madrugada del 19, en la vivienda que la alcaldesa renta en Cancún; ella declara que no fue detenida · «El Charro»: **Guerrero**, FGE, Iguala, desaparición de un menor en Taxco (Infobae 2026/10/19); **no es `ARG-136-008`** · «El Marce»: FGE QRoo, capturado en Mérida (Diario de Yucatán y Noticaribe 2026/10/19) |
| **4. Exfiscal (`ARG-136-006`)** | Ingreso al Altiplano (El Financiero 2026/10/20); resultado de la audiencia federal no publicado; vinculación estatal el jueves 22-oct 10:00 (Excélsior, sin fecha en la ruta) |
| **Tulantepec** | Fallo condenatorio del **9-oct** (La Silla Rota 2026/10/9); la audiencia del miércoles 21-oct es de **individualización de la pena y reparación**, no de culpabilidad |
| **Sentencia de Culiacán (18 años)** | Cuatro réplicas de medios (Luz Noticias y Línea Directa 2026-10-19); boletín no obtenido |
| **Heredados** | Nogales: colectivos, 8 osamentas en 3 días (7 en Nogales y 1 en Sonoyta); sin cifra oficial · Cachanillas: «10 cuerpos en tres días» (Punto Norte 2026/10/18) · Ajuchitlán: sin novedad (`ARG-135-010`) · Tepic: imputación del 16-oct (causa 2679/2026); sin vinculación hallada · Apatzingán, El Tívoli, Coquimatlán: sin avance · Patamban: la FGE «no descarta» relación con la defensa de los bosques, solo por resumen; **ninguna autoridad acredita persona defensora**: el color sigue siendo decisión del destinatario · `ARG-137-007`: la Mesa de Coordinación de Colima atribuye la agresión a los abatidos («dispararon contra los elementos, quienes respondieron»), solo por resumen · `ARG-137-012`: «minutos después de la medianoche» del 18-oct, solo por resumen; apertura de 137: 18-oct 08:34 → **anterior a la ventana de 137 si la hora es correcta** · Tlalnepantla: dos homónimos (Edomex, 15-oct; Morelos, 1-oct) · Linares: día contradicho sin resolver · Industrial Bravo: 16-oct, 420 cartuchos = 385 + 25 + 10, solo por resumen · Ensenada: 158 años 9 meses (El Financiero 2026/10/17), sin boletín |

## 6. Arbitrajes del coordinador

| Asunto | Decisión |
|---|---|
| **Hechos propios** | **Ninguno.** Las seis regiones buscaron por fecha de cierre al final del presupuesto: ninguna publicación del 20-oct que 138 no tuviera (solo seguimientos de `-007`, `-010`, `-011`, `ARG-136-006` y Puerto Morelos). El índice no había cargado la mañana del 20 |
| **Río Bravo** | `ARG-139-REC-001`, ventana de origen ARGOS 129. Confianza ★★★☆☆: dos medios nacionales, sin fuente institucional; la fija el día, solo por resumen. Recuento de fuentes: Institucional 0 · Nacional 2 (Infobae, El Universal) · Regional 11 (El Diario de Chihuahua, Expreso, ABC Noticias, En Línea Directa, CN Tamaulipas, Elefante Blanco, Hoy Tamaulipas, El Mercurio de Tamaulipas, Horacero, Noroeste, Vanguardia) · Abierta 0. Estrella Digital, El Congresista, Posta, La Verdad y Más Información: vistas, no contadas. «15 cm», por titular de El Universal; «FGR investiga», por titulares de Elefante Blanco 2026/10/19 (https://elefanteblanco.mx/2026/10/19/fgr-investiga-agresion-denunciada-por-casandra-de-los-santos/) y La Verdad; la Fiscalía de Tamaulipas «desconoce detalles», por titular de CN Tamaulipas 2026/10/19 (https://cntamaulipas.mx/2026/10/19/desconoce-fiscalia-detalles-sobre-agresion-a-diputada-federal-casandra-de-los-santos/), que no es confirmación institucional del hecho. ★★★☆☆ por la regla «dos medios sin fuente institucional» |
| **Sonoyta–Puerto Peñasco** | Visto, no `-REC-`: restos «posiblemente humanos», fuente única, sin autoridad |
| **Cuautla, checador de la Ruta 8** (domingo 18) | 🟡 de la ventana de 137 → visto. Sube a 🔴 solo si una autoridad lo vincula al ataque coordinado de Cuautla |
| **San Juan Nuevo, camionero** (madrugada del 19) · **Chietla, mujer** («otro ataque»; el primero no se buscó) · **Coatzacoalcos, taxista** (19, ~06:00) · **Tanquián** (17) · **Taxco, 4 servidores públicos detenidos** (La Razón 2026/10/19) | Vistos de ventanas anteriores, 🟡 o 🟢 |
| **Armamento** | Ningún aseguramiento publicado en la ventana. Vistos: Cotija-Lourdes, La Rumorosa, Chietla/Tehuacán, Villa de Seris, Industrial Bravo |
| **Sentencias** | Cuatro candidatas, todas publicadas antes de la ventana y sin boletín: Culiacán, General Cepeda (FGR), Caborca (FGR), Ensenada. Van a la tabla de candidatos y no al conteo |

## 7. Fe de erratas (no va al cartelón)

- **`ARG-139-FE-001` — sobre ARGOS 129**: su ventana (10-oct 09:08 → 11-oct 08:58) contuvo un hecho rojo no publicado, la agresión con arma blanca a una diputada federal en Río Bravo (`ARG-139-REC-001`). Efecto: **129 +1 rojo, +1 herida**.
- **`ARG-139-FE-002` — sobre ARGOS 138**: su archivo de fuentes dice «sábado 17, ventana de 136» para Río Bravo; el 17 es el día de la denuncia pública. Se corrige al 10-oct, ventana de 129. Su marca «Consulta 07:06-09:30» es incompatible con su último commit (07:45).
- **Narcomanta** (vistos de 138): es de Ciudad Juárez, no de la capital.
- **`ARG-139-FE-003` — sobre ARGOS 135**: Ensenada, «158 años a cada uno, **por titular**»: ningún titular precisa el alcance; «a cada uno» es de resumen de dos medios (coherente con el desglose 135 + 10 años 9 meses + 13 años). Cambia la etiqueta, no la cifra ni ningún total (pena acumulada 0).
- **Ensenada, sin fe de erratas de cifra**: el «a cada uno» de 135 y 136 se mantiene como lectura de resumen.

## 8. Registro del barrido — por entidad

| Región | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Noroeste | BC, Son, Chih, Sin propia · BCS, Dgo amplia | Chih (parcial), Sin · NO REVISADA: BC, BCS, Son, Dgo | BC (parcial), BCS (parcial), Chih (parcial) · NO REVISADA: Sin, Son, Dgo |
| Noreste | NL, Tamps propia · Coah, SLP, Zac amplia | Coah, Tamps (parcial), SLP, Zac (parcial) · NO REVISADA: NL | Tamps (6-oct) · NO REVISADA: Coah, NL, SLP, Zac |
| Occidente | Ags, Jal, Nay, Mich, Col, Gto propia | Mich (parcial) · NO REVISADA: Jal, Nay, Ags, Col, Gto | Jal, Nay, Ags, Mich, Col (todas parciales) · NO REVISADA: Gto |
| Centro | Edomex, Mor, Hgo propia · CDMX, Pue, Tlax, Qro amplia | NO REVISADA las 7 (solo medios) | CDMX, Edomex, Pue, Qro (parciales) · NO REVISADA: Mor, Tlax, Hgo |
| Golfo | Ver, Tab propia | Ver, Tab (parciales) | Ver, Tab (parciales) |
| Sureste | Oax, Gro, QRoo, Chis propia · Camp, Yuc amplia | Oax, Camp (parcial), Yuc (parcial), QRoo (parcial) · NO REVISADA: Gro, Chis | Oax, Gro, QRoo (parcial) · NO REVISADA: Chis, Camp, Yuc |
| **Total** | **21 propia · 11 amplia** | **13 de 32** (9 parciales) | **18 de 32** (15 parciales) |

Casillas: todas las revisadas, `SIN RESULTADO INDEXADO EN VENTANA`; `SIN ACTUALIZACIÓN CONSTATADA`: 0.

## 9. Desglose de cálculos propios

- Hechos propios: 0 (`len(E)`); semáforo 0/0/0; muertos 0 y heridos 0, derivados del arreglo `E` (`MU`, `HE`); recuperación: 0 muertos y 1 herida (`MU_REC`, `HE_REC`), fuera de todo total.
- Densidad: 0 / (43/60 h) = 0,00 hechos/hora.
- Armamento: `TOT` = 0 en las diez categorías; ninguna fila.

## 10. Los dos controles editoriales

| Ronda | Control | Resultado | Disposición |
|---|---|---|---|
| 1 | `procedencia-cifras` (30 búsquedas, `extended`) | **CORREGIR**: 1 de fondo (Ensenada) y 9 de redacción | Aplicados: 15 cm por titular; «FGR investiga» y «desconoce detalles» por titular; distrito 3 por resumen; Cadereyta 2 o 4 operativos; Colima «dispararon contra los elementos»; Tulantepec «triple feminicidio»; General Cepeda «más de 13 años»; Caborca sin FECOR; Industrial Bravo 420 = 385 + 25 + 10, sin contradicción; Conclusión de fosas con 7 + 1 y cifras de colectivo; audiencia del exfiscal «jueves» por titular y 22-oct por calendario |
| 1 | `editor-duplicidad` | **CORREGIR**: 3 duplicados en vistos y candidatos, Valoración 5 falsa, marca de consulta, repetición entre secciones | Aplicados: Villa de Seris retirada (es `ARG-137-018`); Cotija e Industrial Bravo marcados «ya vista» (138 y 137), con `POSIBLE DUPLICIDAD CON ARG-135-ARM-001`; Culiacán «candidata desde 138» y Ensenada «desde 135»; Tulantepec en un solo lugar; Valoración 5 → «ningún hecho propio con ruta del 20-oct»; Consulta 07:58-08:20; deslinde de Río Bravo → `ARG-128-REC-003`; `ssp.chihuahua.gob.mx` «dominio inexistente»; conclusiones reescritas: fuera las que repetían el panorama o la edición 138 (enfrentamientos, plaza de La Marina, condenas arrastradas); dentro agresiones a actores políticos y Morelos oriente. Portada: `ARG-139-REC-001` pasa a conclusiones y la línea 1 es `ARG-138-006`. `tools/validar.js`: la regla de recuadros admite atributos (antes no contaba el que lleva `style`) |
| 1 | Arbitraje Ensenada | Los controles discreparon: procedencia «por cada sentenciado», duplicidad «en conjunto» | **Por cada sentenciado**: 135 + 10 años 9 meses + 13 años = 158 años 9 meses es la suma de tres penas de un mismo sentenciado, coherente con «a cada uno» de dos resúmenes y con ARGOS 135 y 136. **No hay fe de erratas** sobre 135 y 136 |
| 2 | `editor-duplicidad` | **CORREGIR**: C1-C5 de redacción en conclusiones; Ensenada «158 años» frente a «9 meses» | Aplicados: cálculo propio declarado en la conclusión 1; Otatitlán `HEREDADO — NO REVERIFICADO`; conclusión 2 sin «en aumento» y declarada desarrollo de 136; conclusión 3 acortada; conclusión 4 sin las combis (posible duplicidad con `ARG-131-002`); conclusión 5 sin «sin boletín leído»; Ensenada «158 años» por El Financiero y «9 meses» por Sin Embargo. Validador sobre el móvil: limitación de la herramienta, también con 138 → deuda |
| 2 | `procedencia-cifras` (0 búsquedas) | **CORREGIR**: 2 de fondo (FGR «por titular» en General Cepeda; conteo de la conclusión 1 sin declarar) y 10 de clase | Aplicados: General Cepeda «huachicol» por titular y FGR solo por resumen; conclusión 1 «al menos tres… entre el 10 y el 17-oct (8 días naturales; cálculo propio)», fechas marcadas, detenidos con fecha de verificación; conclusión 3 con la contradicción de fecha del traslado (137); conclusión 4: checador por titular de Potosinoticias, narcomantas por resumen, «el titular no nombra el operativo»; REC-001: «Desconoce Fiscalía detalles» literal, primera ruta fechada, encapuchado por titular; Cadereyta 4 por titular; Cotija, La Rumorosa y Chietla con clase de cada dato; FGJE-370 por resumen; cobertura «por búsqueda dirigida; acceso directo: 0»; `ARG-139-FE-003`. Hora de la decisión de Río Bravo corregida (antes de las 07:53) |
| 2 | Criterios declarados | Conclusión 1: «cargos de elección, excargos o aspirantes». **`ARG-130-009` (Escuinapa, coordinador de Protección Civil, 11-oct) queda fuera**: servidor público designado, no cargo de elección. Recuento de fuentes de REC-001: se cuentan los medios con titular o ruta atados al hecho y leídos por el coordinador o por R1; La Verdad (ruta sin día), El Congresista, Posta, Estrella Digital y Más Información, vistas y no contadas por no reabiertas | — |
| 1 | No aplicado | Bajar `ARG-139-REC-001` a ★★☆☆☆ (duplicidad, sugerencia 14) | Se mantiene ★★★☆☆: cumple la regla de la escala (dos medios nacionales, sin institucional); el campo peor sostenido queda declarado |

## 11. Herramientas

- `tools/datos-argos-139.py` (generador; parte de 138; totales de muertos y heridos derivados del arreglo) · `tools/gen-movil.py` (fecha sin sufijo) · `tools/gen-texto.py` · `tools/validar.js` → escritorio: validación OK.
- Comandos: `python3 tools/datos-argos-139.py reports/argos-2026-10-20.html reports/argos-2026-10-20b.html` · `python3 tools/gen-movil.py 139 2026-10-20b 138 2026-10-20 07:49` · `python3 tools/gen-texto.py reports/argos-2026-10-20b.html reports/argos-2026-10-20b.txt` · `node tools/validar.js reports/argos-2026-10-20b.html 2026-10-20 2026-10-20`.

## 12. Lecciones de método (no van al cartelón)

1. **Una edición pegada a la anterior no tiene materia propia**: con 43 minutos de ventana, ninguna publicación del día había llegado al índice del buscador; la ola entera solo produjo seguimientos y una recuperación.
2. **El día de la denuncia no es el día del hecho**: Río Bravo pasó una edición fichado como «sábado 17» porque el resumen decía «el sábado» sin decir cuál.
3. **Los agregados de medios reciclan hechos viejos**: El Independiente 2026/10/19 incluye Naucalpan del 13-oct; la fecha de la página no fecha ninguno de sus hechos.
4. **Dominios**: `fiscaliaguerrero.gob.mx` confirmado; `fiscaliasinaloa.mx` responde sin boletines; `ssp.chihuahua.gob.mx` no es dominio válido; Chis, Camp y Yuc sin dominio de fiscalía confirmado.
