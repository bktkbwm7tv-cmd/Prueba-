# ARGOS 140 — Archivo de fuentes

**Corte**: 2026-10-25 · **Ventana**: 21-oct 10:23 → 25-oct 07:45 CDMX (**93 h 22 min**; `WINDOW_DAYS = 5`) · **Densidad**: 23 hechos propios / 93,37 h = **0,25 hechos/hora**, cálculo propio.
**Hora de cierre**: hora real de la orden «Procede» del destinatario (07:45 CDMX del domingo 25). Consultas de la ola y del coordinador de 07:46 a 07:57; `procedencia-cifras` R1, después: la marca «Consulta» del cartelón se fija con la hora real de su última búsqueda. Los hechos posteriores a las 07:45 pertenecen a ARGOS 141.
**Orden**: la orden de ARGOS 140 del 22-oct no se ejecutó (la sesión se detuvo tras el Bloque 0); se rehízo el 25-oct (`reports/_ordenes-ARGOS-140.txt`, commit `c0448f3`). No hay edición del 22 al 24-oct.

Informes íntegros de los seis equipos, notas del coordinador y controles: `reports/argos-2026-10-25-equipos.md`. Plantilla: `tools/plantilla-equipos-140.md`. Generador: `tools/datos-argos-140.py`.

## 1. La base

- 22-oct 08:14: clon sin rama en `60f2777`, por detrás; *fast-forward* a `origin/main` (`d0c6ab7`) y a `origin/claude/argos-139-qe9f01` (`9712e79`, que lleva encima de `3c343ac` la orden del 22-oct). 219 archivos en `reports/`; última edición `argos-2026-10-21`.
- 25-oct: rama `claude/argos-140` creada sobre `9712e79`; ninguna edición del 22 al 25. 219 archivos antes de esta edición.

## 2. Red y modo de búsqueda

- `curl https://www.gob.mx/fgr` → `000` (22-oct 08:14 y 25-oct 06:52; `connect_rejected` del proxy). **Egreso bloqueado: solo WebSearch.** Techo ★★★★☆; esta edición no supera ★★★☆☆.
- Consulta de control en los dos modos: `extended` trae hechos de la ventana (Purísima del Rincón, Uruapan, Ozumba, Iztapalapa); `standard`, nada de 2026. **Todo `extended`.**
- Presupuesto: control 2 · ola 150 (6 × 25, agotada en los seis equipos) · coordinador 16 · `procedencia-cifras` R1 hasta 30. Tope 200.

## 3. Rotación — prioridad sobre el ciclo y CICLO A, declarados

- **Ciclo A** (Noroeste + Centro encabezan el triaje judicial), después de la prioridad sobre el ciclo.
- **Sentencias `NO REVISADA` en 139 (11)**: revisadas ahora BC, Chih, CDMX, Pue, Tlax, Hgo, Qro (7); consultadas sin páginas del dominio Sin, Tamps, Camp (3); sigue `NO REVISADA` BCS (1).
- **Armamento `NO REVISADA` en 139 (19)**: revisadas ahora NL, Tamps, SLP, Mich, Gro, Oax, Yuc (7); siguen sin dominio BC, Son, Dgo, Chih, Sin, Coah, Gto, Mor, Tlax, Hgo, Camp, QRoo (12).
- **Alto impacto solo amplia en 139 (7)**: BC, Chih, Coah, NL, Ags, Gto, Edomex — **las siete con consulta propia**.
- **Qué aportó la rotación**: Noroeste (judicial) resolvió el exfiscal en sus dos fueros y fijó las tres candidatas heredadas; Centro (judicial) estableció que la pena de Tulantepec **no se dictó** el 21-oct (audiencia pospuesta). Ninguna sentencia estatal integrable: el ciclo hace demostrable el `SIN DATO`, no garantiza hallazgo.

## 4. Boletín federal — triple consulta

| Día | Resultado |
|---|---|
| **21-oct** | **Existe**: «acciones relevantes del 21 de octubre de 2026», por republicadores (Ultranoticias; RED113; Talla Política; Certeza Diario). Colima, Durango, Quintana Roo, Veracruz, Chalco, Tlajomulco, Puerto Morelos: cifras solo por resumen → vistos |
| **22-oct** | **Existe**: Milenio (slug «22-de-octubre-2026»); SICOM; RED113; Talla Política. Culiacán (ARG-140-021), Iztapalapa-Puebla-Amozoc (ARG-140-020), Ojinaga, Hidalgo-Juárez, Monterrey, Morelos |
| **23-oct y 24-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas (día suelto, rango «23, 24 y 25», título sin `site:`), repetidas al final |
| **gabinetedeseguridad.gob.mx** | El buscador solo devuelve el agregado del 9 al 11-oct (contenido/9926) |

Corroboración débil por construcción: los republicadores del mismo boletín son una fuente.

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **0. Ciclo** | A, declarado (§3) |
| **1. Tulantepec** | **Sin pena**: la audiencia de individualización del 21-oct se pospuso «por falla de energía» (titular de La Jornada Hidalgo, sin fecha en la ruta); nueva fecha 28-oct, solo por resumen; plazo 28-nov, por resumen. «40 a 90 años»: estimación de la asesoría de víctimas. Sin boletín de la PGJEH → candidato en la tabla de sentencias, no integrable |
| **2. Exfiscal (`ARG-136-006`)** | **Estatal, jueves 22**: vinculado por ejercicio ilegal del servicio público; coalición descartada (titulares) → `ARG-140-022` 🟢. **Federal, sábado 24**: vinculado por traición a la patria; resolución publicada el 25 → `ARG-140-023` 🟢 con marca de frontera. Sin comunicado de la FGR ni de la FGE |
| **3. El Terrero (`ARG-139-REC-002`)** | «Reanudan ataques» (El Diario de Chihuahua 2026/oct/20) se refiere al ataque del 19: **sin nueva agresión con fecha**. Sin parte de la Defensa |
| **4. Fichas de 139** | `-002` sin causa ni identificación oficial → **no baja** · `-001` parentesco contradicho; ~12:10 por resumen · `-003` adscripción por reconocimiento de compañeros; la FGEO vincula a 7 detenidos con 6 homicidios (`ARG-140-019`) · `-008` ~06:00 solo por resumen → **no se retira** · `-005` docente de secundaria pública por medios, sin acreditación institucional → **sigue 🟡**; detenido el presunto homicida (`ARG-140-018`) · `-007` la «21-oct 07:04» es hora de publicación de N+: no hay otro hecho · `-REC-003` herido, fuera de peligro; cargo sin arbitrar · `-004/-010` «al parecer repartidor» solo en La Foresta (Noroeste) |
| **5. Seguimientos** | Xalisco/Tecuala: tres fosas con cinco cuerpos y diez detenidos, por resumen → posible duplicidad con `ARG-133-REC-007`, no se integra · Cachanillas: sin cifra oficial · Río Bravo: el día sigue solo por resumen; un medio lo cuestiona (Nota Tamaulipas 2026/10/19) → fe de erratas a 129 **sigue condicionada** |
| **6. Sentencias candidatas** | Culiacán (Daniel «N», 18 años), Ensenada (158 años 9 meses = 135 + 10 años 9 meses + 13, por medios), General Cepeda (13 años 4 meses), Caborca (8 años): todas publicadas antes de la ventana, sin boletín |
| **Heredados** | Nogales, Ajuchitlán (sigue desaparecida la séptima persona al 20-oct), Apatzingán, El Tívoli, Coquimatlán (tres muertos el 15-oct, ¿= caso previo?), Linares, Tepic, Patamban (decisión del destinatario), Taxco (vinculación no localizada): sin avance que cambie un color |

## 6. Arbitrajes del coordinador

Ver «Arbitraje del coordinador» en `reports/argos-2026-10-25-equipos.md`. Decisiones de color con reserva:
- `-004` Villa Bonita: rojo con el día solo por resumen (excepción declarada para rojos).
- `-008` Escuinapa: 🟡; la SSP dice que la agresión fue contra el conductor y ningún estudiante resultó herido.
- `-014` Indaparapeo: 🟡 porque no consta quién inició.
- `-016` Cosoleacaque: 🟡 porque no consta que sea un solo ataque.
- `-REC-003` Ecatepec: el resumen dice «martes»; la publicación (22-oct 03:10) es compatible con el miércoles 21. Se recupera por el texto disponible; si se fija el 21, pasa a hecho propio por fe de erratas.

## 7. Fe de erratas (no va al cartelón)

Ninguna nueva en R1. Condicionadas: Río Bravo (129); Ecatepec (si resulta del 21, se suma a los totales de 140).

## 8. Registro del barrido — por entidad

Ver el «Indicador de cobertura» del cartelón y los informes íntegros. Sentencias: 11 revisadas, 9 dominios sin páginas, 12 `NO REVISADA`. Armamento: 11 por dominio, 21 sin dominio. Alto impacto: 17 con consulta propia, 15 solo amplia. Dominios nuevos confirmados: `comunicacion.fiscaliaveracruz.gob.mx`, `portal.fgeo.gob.mx`, `fiscaliageneralqro.gob.mx`, `seguridad.slp.gob.mx`; listados de la FGR en `fgr.org.mx`.

## 9. Emisores por ficha

El recuento I/N/R/A de cada ficha está en `tools/datos-argos-140.py`; las URL, en el archivo de equipos.

## 10. Desglose de cálculos propios

- Muertos por agresión en hechos propios: 14 = 2 (-001) + 1 (-002) + 1 (-003) + 2 (-004) + 1 (-009) + 1 (-010) + 1 (-011) + 1 (-012) + 1 (-013) + 1 (-015) + 2 (-016).
- Heridos: 5 = 1 (-001) + 1 (-008) + 1 (-009) + 2 (-015). Cuerpos hallados: 7 = 5 (-005) + 2 (-006).
- Recuperaciones: 8 muertos (3 + 1 + 4) y 4 heridos (2 + 1 + 1), fuera de todo total.
- Armamento: 36 armas sin categoría y 4 detenidos (ARM-001, único evento).
- Entidades: 13 (CDMX, Gto, Sin, Tab, Tamps, Mor, Edomex, NL, Mich, Ver, Oax, Pue, Chih). Densidad: 23 / 93,37 = 0,25.

## 11. Los dos controles editoriales

(pendiente)

## 12. Herramientas

`python3 tools/datos-argos-140.py reports/argos-2026-10-21.html reports/argos-2026-10-25.html` · `python3 tools/gen-movil.py 140 2026-10-25 139 2026-10-21 07:45` · `python3 tools/gen-texto.py reports/argos-2026-10-25.html reports/argos-2026-10-25.txt` · `node tools/validar.js reports/argos-2026-10-25.html 2026-10-21 2026-10-25` → validación OK.

## 13. Lecciones de método (no van al cartelón)

1. **La ola de 25 búsquedas por equipo no alcanzó la consulta de fecha en la ruta por día** en ningún equipo: en una ventana de cinco días, el presupuesto se agota en encargos y prioridad antes de llegar al barrido por fecha.
2. **El recall nacional del coordinador volvió a aportar rojos que los barridos no traían** (Iztapalapa, Ecatepec, Ario de Rosales) y las pistas reenviadas a los equipos llegaron tarde a dos de ellos (Noroeste, Golfo), que ya habían agotado su tope. Conviene hacer el recall **antes** de lanzar la ola.
3. **Varias consultas `site:` con `OR`** se desperdiciaron (Noroeste, Occidente) pese a la regla escrita: el buscador ignora el operador.
4. El buscador indexa poco del 23 al 25-oct (fin de semana): los totales de esos días son mínimos, no exhaustivos.
