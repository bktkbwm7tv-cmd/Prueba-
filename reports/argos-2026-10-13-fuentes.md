# ARGOS 131 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-10-13 · **Ventana**: 2026-10-12 08:19 → 2026-10-13 07:23 CDMX · **23 h 04 min**
**Rama**: `claude/argos-131` (partió de `origin/claude/argos-130` = `63c1325`).

---

## 1. La base

Bloque 0 a las **07:23 CST** del 13-oct. El clon arrancó en `60f2777` (por detrás de `origin/main`, como en 128, 129 y 130);
`git merge --ff-only origin/main` avanzó `60f2777 → b0558a3`; `--ff-only origin/claude/argos-129` → `9eaba81`; `--ff-only origin/claude/argos-130` →
`63c1325`. **Los tres merges, fast-forward.** Estado: `argos-2026-10-12` (ARGOS 130) y **159 archivos** en `reports/`, lo previsto. HEAD suelto: se abrió
`claude/argos-131`.

| Serie | 126 | 127 | 128 | 129 | 130 | **131** |
|---|---|---|---|---|---|---|
| Duración | 17 h 41 | 22 h 24 | 25 h 48 | 23 h 50 | 23 h 21 | **23 h 04** |
| Densidad (hechos/h) | 0,40 | 0,27 | 0,23 | 0,25 | 0,39 | **0,26** (6 / 23,07, cálculo propio) |

`WINDOW_DAYS = 2`: la ventana toca dos fechas de calendario (12 y 13-oct). El generador lo comprueba con `assert`.

## 2. Red y modo de búsqueda

- **Egreso**: `curl https://www.gob.mx/fgr` → **`000`** (dos intentos, 07:23). **Ningún documento oficial leído íntegro.** Techo **★★★☆☆**, decimotercera edición.
- **Consulta de control** (Jacona, en los dos modos): `standard` **no encontró el caso** —devolvió Jacona de abril, agosto, 2024 y 2021—; `extended` trajo la
  cobertura del 11-oct con el saldo contradicho. **Se mantuvo `extended` obligatorio.**
- **Presupuesto**: control 2 + ola de **seis equipos** (Noroeste 30, Noreste 24, Occidente 30, Centro 26, Golfo y federal 26 de 28, Sureste 22 = **158**)
  + **7 del coordinador** = **167**; `procedencia-cifras` hasta **25**. `editor-duplicidad` no busca en la web.
- **Rendimiento del coordinador**: la búsqueda nacional del **lunes 12** halló **Culiacán, Vallado Viejo** —el rojo de mayor saldo— y señaló Mazatlán; la
  del **martes 13** halló el **boletín federal del 9 al 11-oct** (Milenio, Excélsior), el **asesinato del exalcalde de Otatitlán** y la **Semar en Oaxaca**.
  Las otras cinco: Otatitlán, Vallado Viejo, FGR Pichilingue, Morelia (Ilustres Novohispanos) y Puebla (FGE).

## 3. Rotación — prioridad sobre el ciclo y CICLO C, declarados

| Renglón | Resultado |
|---|---|
| Prioridad — armamento (15 `NO REVISADA` en 130) | **Revisadas ahora**: BC (`seguridadbc.gob.mx`, índice de boletines), Dgo (`fiscalia.durango.gob.mx`), Coah (`sspcoahuila.gob.mx`), Tamps (`tamaulipas.gob.mx`), Jal, Col (`col.gob.mx`), Nay (`nayarit.gob.mx`), **Ags (`aguascalientes.gob.mx`)**, Qro (`queretaro.gob.mx`), Chis (`sspc.chiapas.gob.mx`), **Camp (`spsc.campeche.gob.mx`, dominio confirmado)**, Yuc (`ssp.yucatan.gob.mx`), QRoo (`qroo.gob.mx`). **Siguen `NO REVISADA`**: BCS, Hgo (`hidalgo.gob.mx` no indexado) |
| Prioridad — sentencias (17 `NO REVISADA` en 130) | **Revisadas**: BC (`fgebc.gob.mx`), Mich (`fiscaliamichoacan.gob.mx`), **Ags (`fiscalia-aguascalientes.gob.mx`, dominio confirmado)**, Edomex (`fiscaliaedomex.gob.mx`), Pue (`fiscalia.puebla.gob.mx`), Gro (`fiscaliaguerrero.gob.mx`), Chis (`fge.chiapas.gob.mx`), Yuc (`fge.yucatan.gob.mx`). **Siguen `NO REVISADA`**: **Son (cuarta edición: `site:fge.sonora.gob.mx` devolvió 0)**, **Sin (cuarta edición: `fiscalia.sinaloa.gob.mx` y `fiscaliasinaloa.gob.mx` no devueltos; solo republicadores)**, Zac, Col, Gto, Mor, Tlax, Hgo, Camp |
| Prioridad — alto impacto | **Ags revisada por medios** (SRIV): los tres módulos de Aguascalientes, revisados por primera vez desde 129 |
| Ciclo | **C** — Occidente + Sureste encabezaron el triaje judicial tras la prioridad |
| Rendimiento | **Ninguna sentencia estatal integrable.** El ciclo C halló Colima 27 años (9-oct), Michoacán Numarán, Buenavista y Uruapan (3 a 11-oct) y Campeche (8-oct): todas fuera de ventana. **La única sentencia integrable es federal (FGR, BCS)**, hallada por el equipo Golfo-federal y el Noroeste |

Serie: C (125) sí · A (126) no · B (127) no · C (128) no · A (129) no · B (130) no · **C (131) no — la integrable vino del federal.**

## 4. Boletín federal — triple consulta

| Acciones de | Estado |
|---|---|
| **9, 10 y 11-oct** | **EXISTE: agregado de tres días, publicado el 12-oct**, localizado solo por la **tercera forma** (título sin `site:`): Irradia, RED113, Talla Política, Certeza Diario, Milenio (`…9-10-y-11-de-octubre-2026`); fecha de publicación fijada por Línea Directa 2026-10-12__1718779 y Argon México 2026/10/12. **Corrige el `SIN RESULTADO INDEXADO` de ARGOS 130 §4** (cuarto falso vacío del emisor por formato/indexación). Republicadores: no independientes. Totales, Excélsior por titular: «22 sospechosos y 35 armas en 12 estados»; 788 cartuchos, 119 cargadores, 64 AEI y 6 minas, **solo por resumen, no cuadran con el desglose**. Acciones anteriores a la apertura: `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE`, fuera del total |
| **12-oct** | `SIN RESULTADO INDEXADO EN VENTANA` en las tres formas. **Trampa de año** de nuevo: el rango «10, 11 y 12» devolvió `gob.mx/sspc/prensa/…-de-octubre-de-2025` |

`gabinetedeseguridad.gob.mx/resultados/`: SRIV; el dominio indexa `contenido/7391/fgr-obtiene-sentencia-condenatoria-…` (base de `ARG-131-SEN-001`).
**GN, Defensa y Marina: REVISADAS por `site:`, SRIV** (primera vez con cuota propia; índice con material de 2019-2024 y septiembre de 2026).

Desglose del agregado, solo por resumen (para seguimiento, no se integra): Edomex Toluca/Valle de Bravo 8 detenidos, 3 armas, 150 cartuchos, 5 cargadores
(10-oct) · Guerrero 1 detenido, 1 larga, 1 corta, 2 cargadores (¿«El Junior», `ARG-130-007`?) · Tamaulipas 1 arma, 10 cargadores, 44 cartuchos · Michoacán,
Cotija 9 armas, 3 cargadores, 55 cartuchos, **28 AEI** · Sinaloa, Culiacán col. Popular 9 largas, 22 cargadores, 173 cartuchos, 7 explosivos · El Rosario
48 drones, 64 baterías, 44 rollos de fibra óptica · Veracruz, Ciudad Isla 8 armas sin desglose, 41 cargadores, 34 cartuchos · Tabasco, «El Cabra».

## 5. Encargos

| Encargo | Resultado |
|---|---|
| **Jacona** (`ARG-130-001`) | **Sin comunicado oficial indexado** (búsqueda dirigida a `ssp.michoacan.gob.mx` y `michoacan.gob.mx`: nada de 2026). **Saldo sigue contradicho por titular**: 6 (La Voz, CB TV, Telediario, atiempo.mx, sin fecha) frente a 8 (Latinus 2026/10/11, En Blanco y Negro 2026/10/11, La Prensa de Coahuila 2026/10/11, Quinto Poder 2026/10/12, El Independiente 2026/10/13). **La Jornada 2026/10/11** titula «dos municipales sin vida y tres delincuentes abatidos» y atribuye el 6 a la **SSP**, solo por resumen: **atribución del 6 contradicha (FGE por atiempo.mx, SSP por La Jornada)**. Hora ~12:30, solo por resumen. Armas largas, cargadores, cartuchos y una pick up: sin cifra. **Cero detenidos.** Quadratín (13-oct, resumen): presunta célula del CJNG. **Seguimiento, no hecho nuevo**: acción 4 de la portada |
| **Nacajuca** (`-003`) | **Sin hora citable**: ~03:00 solo en el cuerpo de un medio. Sigue en 130 con la marca. Sin detenidos (Diario de Tabasco 2026/10/11, La Silla Rota 2026/10/12) |
| **Morelia, micheladas** (`-004`) | **Sin hora citable**; el resumen da ≈05:00 o ≈02:15, **las dos anteriores a las 08:58**, ninguna citable. Sigue en 130 con la marca |
| **Escuinapa** (`-009`, `-006`) | **No es mezcla** (por resumen): coordinador de PC, tarde del domingo, calle Francisco Pérez (El Diario de Sonora 2026/10/12); El Roblito, ~11:30, Aldama y Usumacinta. Nuevas fechadas para `-009`: El Diario de Sonora 2026/10/12, MVS 2026/10/12 (749433), Diario de Juárez 2026/oct/12. Línea Directa 2026-10-11__1718457 (cita del alcalde). Sin FGE, sin detenidos. «Quinto funcionario asesinado en Sinaloa en 2026»: recuento de medios |
| **Ciudad Juárez** (`-008`) | **Fecha del hecho sigue sin anclar**; todas las URL son del 11-oct. Sin cambio |
| **Minatitlán** (`ARG-129-001`) | **2 muertos por medios** (La Silla Rota y Luces del Siglo 2026/10/12); **El Imparcial 2026/10/12 titula «no descartan que sea un móvil personal»**; segundo comunicado de Pemex y boletín FGE: no localizados; cero detenidos |
| **Cancún** (`-002`) | FGE QRoo: SRIV. PorEsto 2026/10/12: «Investigan posible confusión de víctimas…» (titular). Sin detenidos. Sol QRoo (sin fecha), mismo hecho. PorEsto 2025/12/9 en Los Corales: **otro hecho**, de 2025 |
| **Acapulco** (`-007`) | Inventario solo por resumen (1 larga, 1 corta, 2 cargadores, 300 dosis); UnoTV titula «le aseguran armas y 300 dosis». El Mañana 2026/10/12. Lugar no publicado. Agresión en la captura: ambigua. Sigue cualitativo |

## 6. Seguimientos

| Seguimiento | Resultado |
|---|---|
| Navolato (`-005`) | **Un solo cuerpo** (seis medios); curva de San Pedro. Sigue 🟡. Cierra la duda |
| SEMAR 10-oct | La Razón 2026/10/10 («… hay 2 detenidos»); Noticieristas 2026/10 («12 armas largas»); Meganoticias («13 armas»). Hipótesis: 12 largas + 1 corta. Sigue `POSIBLE DUPLICIDAD` con `ARG-125-005` |
| Zamora (`ARG-129-REC-001`) | **RED113 2026/10 (sin día) titula «… ataque ya suma 5 muertos»**: la quinta muerte tiene ahora un titular, sin día en la ruta. **4 frente a 5, por titular en los dos lados: sigue sin arbitrar**; la FE no se reabre |
| Sombrerete (`-REC-010`) | **La Nigua titula «Aseguran 185 detonadores y 22 explosivos»** (sin fecha): **185 queda sostenido por titular**; 39 solo por resumen. Caso FGR 691/26, por resumen |
| Pinotepa (`ARG-128-001`) | Sin acto nuevo; sin comunicado FGEO; sin detenidos |
| Juchitán, La Ventosa | **Corrección del pendiente**: la víctima no es el agente municipal sino un hombre de 56 años asesinado frente a su casa, cuya vivienda fue baleada (Oaxaca Capital 2026/10/12, por resumen). Sábado 10-oct: ventana de 129. No se ficha |
| El Balcón | Sin novedad posterior al 9-oct. No se describe el video |
| Chipilo, Pachuca | Sin avance |
| Huejotzingo | **Cierra**: retodiario 2026/10/09, hecho del 8-9 oct, fuera |
| Santiago Tulantepec, Ensenada | Sin pena; individualización el 14 y el 16-oct |
| NL, tres personas | Publicado el 10-oct (MVS) y 11-oct (El Mañana): fuera de ventana; sin boletín de `fiscalianl.gob.mx`; discrepancia 25 años frente a 25 años 10 meses |
| Zacatecas José «N» | **Al menos seis José «N» distintos en NTR 2026/09-10**, todas con URL sin día. **Se deja de buscar**: `POSIBLE CASO HOMÓNIMO` permanente |
| Tamaulipas FGJE-381 a 384 | 10 y 11-oct por resumen; sin sentencia aparente; ilegibles. Cierra como no integrable |

## 7. Arbitrajes del coordinador

| Caso | Arbitraje |
|---|---|
| **Culiacán, Vallado Viejo** (`ARG-131-001`) | 🔴 por homicidio múltiple. **4 muertos por titular** (Línea Directa 2026-10-12__1719289 «Muere en el hospital la cuarta víctima…»; Noticieristas «asciende a cuatro muertos»). Hora ~20:15–20:40 solo por resumen. Publicado el 12-oct, día de cierre de 130: `FRONTERA`; la noche del lunes, por resumen, la sitúa en 131 |
| **Totolapan** (`-002`) | 🔴: la operación la inicia la autoridad (amarillo por la regla de quién inicia), **pero los narcobloqueos y la quema de vehículos están en la lista roja** y se suma la retención de tres servidores públicos. **La detención quedó revertida por el canje: no se abre ficha verde**. «Dos elementos fallecidos» (Zócalo, solo resumen): no se integra; si se confirma, sube el saldo, no el color |
| **Puebla, FGE** (`-003`) | 🔴 por ataque del grupo criminal contra servidores públicos (personal de la Coordinación de Homicidios). Herido por titular (Puebla Roja «hay un lesionado»; Cinco Radio «Balean a agente ministerial…»). ~22:30 del lunes, solo por resumen; publicado el 13-oct: frontera del lado del cierre declarada en la ficha |
| **Escuinapa, estética** (`-004`) | 🟡 por homicidio doloso único. ~10:00, solo por resumen |
| **Semar, Huatulco** (`-005`) | 🟢. 1.2 t y 6 detenidos por titular (La Razón 2026/10/12). Sin armas: fuera del conteo de armamento |
| **«El Cabra»** (`-006`) | 🟢. Fecha del hecho 11 o 12-oct: el boletín del 9 al 11 la recogería (solo por resumen). Se integra en 131 con `FRONTERA` (criterio de `ARG-130-008`) |
| **Otatitlán** (`ARG-131-REC-001`) | **Ventana de 130** (domingo 11, 18:30–19:00 por resumen; 130 cerró el 12 a las 08:19 sin publicarlo). **🟡**: un exalcalde no es servidor público en funciones; la regla de agravantes no incluye «figura política». **Decisión que el destinatario puede revisar** |
| **Mazatlán, col. Klein** (`-REC-002`) | 130 lo dejó sin URL con fecha; El Informador `20261011-0084` lo ancla. 🔴 en su ventana |
| **Morelia, Ilustres Novohispanos** (`-REC-003`) | 130 lo descartó «sin nota localizada»; Changoonga 2026/10/11 titula «Mañana violenta al oriente de Morelia: asesinan a dos hombres…». Mañana del domingo: ventana de 129 o 130, **hora no fijada**. Una sola fuente: ★★☆☆☆ |
| **FGR, Pichilingue** (`ARG-131-SEN-001`) | Integrada con **Medio**, precedente `ARG-122-SEN-001`: *slug* institucional en `gabinetedeseguridad.gob.mx` («fgr-obtiene-sentencia-condenatoria…») + publicación anclada por Tijuana Última Hora `/12/10/2026/` + **8 años por titular** (Zócalo «Sentencian a 8 años de prisión a sujeto por transportar más de una tonelada metanfetamina en BCS»). Cuatro campos individualizadores. `FRONTERA` (publicación del 12-oct sin hora) |
| **Sonora, Nogales, 15 años** | `PENDIENTE DE CONFIRMACIÓN OFICIAL`: titular «FGJES obtiene sentencia…» en republicadores sin fecha; El Diario de Sonora 2026/10/12; dominio de la fiscalía no devuelto |
| **Tonalá, Jalisco** (1 muerto, 1 herido, «noche del lunes» por resumen) | Ninguna URL con fecha → **no se ficha**; candidato para 132 |
| **Tehuacán, San Marcos Necoxtla** (1 muerto, noche del lunes) | Sin URL con fecha → no se ficha |
| **CDMX, Azcapotzalco e Iztacalco** (madrugada del lunes) | Titular «madrugada»: probable anterior a las 08:19; sin URL con fecha → no se ficha |
| **Parral, Chihuahua** (11-oct ~03:00; 1 o 2 muertos y 4 heridos por titular de El Diario de Chihuahua 2026/oct/11 y /12; la Fiscalía Zona Sur, 0 muertos por resumen) | Ventana de 129 por hora (resumen); saldo contradicho con la autoridad → **no se ficha**; pendiente |
| **Ciudad Isla, Veracruz** | Evento anterior (10-oct) publicado durante el corte: una línea en el módulo de armamento, fuera del total |

## 8. Fe de erratas (no va al cartelón)

- **`ARG-131-FE-001`** — **ARGOS 130 §4 y su indicador de cobertura**: el boletín federal de las acciones del 9, 10 y 11-oct **sí existía** (agregado
  publicado el 12-oct, posiblemente después del cierre de 130 a las 08:19). La casilla de 130 era `SIN RESULTADO INDEXADO EN VENTANA`, que sigue siendo
  formalmente correcta para lo indexado a esa hora; se registra la existencia del boletín. **No cambia ningún total de 130.**
- **`ARG-131-FE-002`** — **Omisiones de ARGOS 130**: Otatitlán (`-REC-001`), Mazatlán col. Klein (`-REC-002`) y, con hora no fijada, Morelia Ilustres
  Novohispanos (`-REC-003`). **Conteo de 130 recalculado, cálculo propio**: con las dos primeras, rojos 5 → **6**, amarillos 2 → **3**, muertos 16 → **19**
  (18 → 21 con la cifra de 8 en Jacona); `-REC-003` se asigna a 129 o 130 cuando se fije la hora.

## 9. Registro del barrido — por entidad

SRIV = `SIN RESULTADO INDEXADO EN VENTANA`. `SIN ACTUALIZACIÓN CONSTATADA`: **0**. Portales leídos por acceso directo: **0**.

| Entidad | Alto impacto | Armamento | Sentencias |
|---|---|---|---|
| Baja California | SRIV (Tijuana llantera, sin URL con fecha) | SRIV (`seguridadbc.gob.mx`) | SRIV (`fgebc.gob.mx`) · Ensenada sin pena |
| Baja California Sur | NO REVISADA | NO REVISADA | NO REVISADA (solo FGR) |
| Sonora | SRIV | NO REVISADA | NO REVISADA (`fge.sonora.gob.mx`: 0) · Nogales, candidato |
| Chihuahua | SRIV (Parral, fuera) | NO REVISADA (solo agregado federal) | SRIV (`fiscalia.chihuahua.gob.mx`) · 166 años, fuera |
| Sinaloa | **hechos** (Vallado Viejo, Escuinapa) | NO REVISADA (sin dominio devuelto) | NO REVISADA (cuarta edición) |
| Durango | NO REVISADA | SRIV (`fiscalia.durango.gob.mx`) | SRIV (5-oct, fuera) |
| Coahuila | SRIV | SRIV (`sspcoahuila.gob.mx`) | NO REVISADA (dominio no devuelto) |
| Nuevo León | SRIV | SRIV (`nl.gob.mx`, último mayo) | SRIV (`fiscalianl.gob.mx`) |
| Tamaulipas | SRIV (Río Bravo, ya en 129) | SRIV (`tamaulipas.gob.mx`) | SRIV (`fgjtam.gob.mx`) |
| San Luis Potosí | SRIV | SRIV (`seguridad.slp.gob.mx`) | SRIV (`fiscaliaslp.gob.mx`) |
| Zacatecas | SRIV (Huanusco, 8-oct, fuera) | SRIV (`ssp.zacatecas.gob.mx`, acumulado del 3-oct) | NO REVISADA (dominio no devuelto) |
| Jalisco | SRIV (Tonalá sin URL con fecha) | SRIV (`secretariadeseguridad.jalisco.gob.mx`) | SRIV (`fge.jalisco.gob.mx`) |
| Colima | SRIV | SRIV (`col.gob.mx`) | NO REVISADA (por medios: 27 años, 9-oct) |
| Nayarit | SRIV | SRIV (`nayarit.gob.mx`) | NO REVISADA (solo FGR) |
| Aguascalientes | SRIV | SRIV (`aguascalientes.gob.mx`) | SRIV (`fiscalia-aguascalientes.gob.mx`) |
| Michoacán | SRIV · seguimiento Jacona · `-REC-003` | SRIV (`ssp.michoacan.gob.mx`) | SRIV (`fiscaliamichoacan.gob.mx`) |
| Guanajuato | SRIV | SRIV (`boletines.guanajuato.gob.mx`, 6 y 11-oct, anteriores) | NO REVISADA (dominio no confirmado) |
| Ciudad de México | SRIV (Azcapotzalco, madrugada) | SRIV (`ssc.cdmx.gob.mx`) | NO REVISADA |
| Estado de México | SRIV | NO REVISADA (`sseguridad.edomex.gob.mx` no devuelto) | SRIV (`fiscaliaedomex.gob.mx`) |
| Morelos | **hecho** (Totolapan) | SRIV (`morelos.gob.mx`, boletín del 1-oct) | NO REVISADA |
| Puebla | **hecho** (FGE) | SRIV (`ssp.puebla.gob.mx`) | SRIV (`fiscalia.puebla.gob.mx`) |
| Tlaxcala | SRIV | NO REVISADA (dominio no devuelto) | NO REVISADA |
| Hidalgo | SRIV | NO REVISADA (`hidalgo.gob.mx` no indexado) | NO REVISADA |
| Querétaro | SRIV | SRIV (`queretaro.gob.mx`) | NO REVISADA |
| Veracruz | SRIV · seguimiento Minatitlán · `-REC-001` | SRIV (`veracruz.gob.mx`, último 9-oct) | SRIV (`comunicacion.fiscaliaveracruz.gob.mx`) |
| Tabasco | **hecho** («El Cabra») | SRIV (`tabasco.gob.mx`) | SRIV (`fiscaliatabasco.gob.mx`) |
| Guerrero | SRIV | NO REVISADA | SRIV (`fiscaliaguerrero.gob.mx`, último 9-jul) |
| Chiapas | SRIV | SRIV (`sspc.chiapas.gob.mx`) | SRIV (`fge.chiapas.gob.mx`) |
| Oaxaca | **hecho** (Semar) | NO REVISADA | SRIV (`portal.fgeo.gob.mx`, último 5-oct) |
| Campeche | SRIV | SRIV (**`spsc.campeche.gob.mx`**) | NO REVISADA (dominio no hallado) |
| Yucatán | SRIV | SRIV (`ssp.yucatan.gob.mx`) | SRIV (`fge.yucatan.gob.mx`) |
| Quintana Roo | SRIV · seguimiento Cancún | SRIV (`qroo.gob.mx`) | SRIV (`fgeqroo.gob.mx`, último 29-jun) |

**Sentencias: 18 de 32; FGR revisada por búsqueda; 14 `NO REVISADA`.** **Armamento: 23 de 32** (desde 17 en 130). **Alto impacto: 30 de 32, por búsqueda dirigida
en medios** (BCS y Dgo `NO REVISADA`: el equipo Noroeste no les dedicó búsqueda propia).

## 10. Hechos vistos y NO fichados, con motivo

- **Tonalá, Jalisco** (1 muerto, 1 herido; «noche del lunes 12» por resumen): Telediario, N+, NTR, Azteca Jalisco, **ninguna URL con fecha** → candidato de 132.
- **Tehuacán, San Marcos Necoxtla** (1 muerto, noche del lunes): La Jornada de Oriente, Meganoticias, Puebla Roja, sin fecha en la ruta.
- **CDMX, Azcapotzalco (1 muerto) e Iztacalco (2 heridos)**: «madrugada» del lunes por titular de TV Azteca → probable anterior a las 08:19; sin URL con fecha.
- **Parral, Chihuahua**: ver §7.
- **Tijuana llantera**, **Villa Unión** (mujer, 11-oct), **Ciudad Hidalgo** (decapitado, 11-oct): siguen sin URL con fecha.
- **Culiacán, col. Industrial Bravo / La Popular** (9 largas, 22 cargadores, 173 cartuchos, 7 AEI; Luz Noticias 2026-10-10): hecho del 9-10 oct; **no figura en
  129 ni 130** → candidato a `-REC-` en 132 si se ancla la fecha del hecho (posible ventana de 128 o 129).
- **Huanusco, Zacatecas** (padre de la alcaldesa, 8-oct; Diario de Juárez 2026/oct/08): fuera de ventana; no figura en ediciones previas → revisar 127.
- **SLP capital** (2 detenidos con armas, potosinoticias 2026/10/11): publicado antes de la apertura.
- **Monclova** (hallazgo y detención): sin fecha ni URL citable.
- **Comalcalco y Villahermosa, Casa Blanca**: Azteca Chiapas los fecha «domingo 12 de octubre» —el 12-oct-2026 es lunes; el 12-oct-2025 fue domingo—: **incoherencia
  interna, descartados**.

## 11. Desglose de cálculos propios

- Duración: 12-oct 08:19 → 13-oct 07:23 = **23 h 04 min** = 23,07 h. Densidad: 6 / 23,07 = **0,26**.
- Muertos en hechos propios: 4 (Culiacán) + 1 (Escuinapa) = **5**. Heridos por titular: **1** (Puebla); 3 en Totolapan solo por resumen.
- Armamento propio: **0** en todas las categorías. Detenidos en evento de aseguramiento de armamento: **0** (los 6 de Huatulco y «El Cabra», sin armas).
- Frontera: **6 de 6**.
- Sentencias: 1 integrable, 8 años; no se acumula con ningún otro caso.

## 12. Fuentes por ficha

- **`ARG-131-001`** — Nacional 2: López-Dóriga; El Universal. Regional 7: Línea Directa 2026-10-12__1719276 y __1719289; Los Noticieristas 2026/10 (1147430,
  1147459, 1147466); Azteca Sinaloa (dos notas); Café Negro; Quadratín Sinaloa; El Congresista; Viva la Noticia.
- **`ARG-131-002`** — Nacional 5: El Financiero 2026/10/12; ADN40 2026-10-12; Infobae 2026/10/13 («… lo canjeó por 3 agentes retenidos en Totolapan»);
  Publimetro 2026/10/13; UnoTV. Regional 7: El Informador 20261012-0189; El Diario de Chihuahua 2026/oct/12 (847095); Zócalo; Vanguardia; La Unión; XEU;
  guardianocturna 2026/10.
- **`ARG-131-003`** — Regional 6: Capital Puebla 2026/10/13; Curul Puebla; Diario sin Secretos; Puebla Roja; Cinco Radio; Quince Minutos.
- **`ARG-131-004`** — Institucional 1 (FGE Sinaloa, por titular de Sinaloahoy). Nacional 2: El Universal; Posta (vl2265826). Regional 5: Línea Directa
  2026-10-12__1718817; La Prensa de Coahuila 2026/10/12; Los Noticieristas 2026/10 (1146968); Sinaloahoy; Noroeste (ND26437846).
- **`ARG-131-005`** — Institucional 1 (Semar/SSPC, por cita). Nacional 3: La Razón 2026/10/12; El Imparcial 2026/10/12; Infobae 2026/10/13. Regional 5: Diario
  Puntual 2026/10/12; Sociedad Noticias 2026/10/12; NVI Noticias (194590); Quadratín; Sinaloahoy (190 mn: contradicción).
- **`ARG-131-006`** — Institucional 1 (boletín federal, por resumen). Nacional 1: Proceso 2026/10/12 (381699). Regional 3: Central Municipal 2026/10/12; Lo de
  Hoy 2026/10/13; Telediario. Sin fecha: Milenio, Zeta, La Chispa, NX Noticias. Infobae «en-vivo» 2026/10/12: *liveblog*, no fecha el hecho.
- **`ARG-131-REC-001`** — Institucional 1 (FGE Veracruz, por titular de El Heraldo). Nacional 6: Infobae 2026/10/12; El Heraldo de México 2026/10/12 (906875);
  MVS 2026/10/12 (749497); Latinus 2026/10/12 (186785); TV Azteca; Eje Central. Regional 4: Intolerancia 2026/10/12; Tabasco Hoy; El Buen Tono; Cúspide México 2026/10/13.
- **`ARG-131-REC-002`** — Nacional 1: El Informador 20261011-0084. Regional 2: Entre Veredas 2026/10; Los Noticieristas 2026/10.
- **`ARG-131-REC-003`** — Regional 1: Changoonga 2026/10/11.
- **`ARG-131-SEN-001`** — Institucional 1: `gabinetedeseguridad.gob.mx/contenido/7391/…` (sin fecha). Nacional 1: Zócalo. Regional 4: Tijuana Última Hora
  `/12/10/2026/`; Uniradio Informa (n857566); Cuestión Chronos; Mi Diario Nayarit.

## 13. Los dos controles editoriales

*(Se completa tras los pases.)*

## 14. Herramientas

`tools/datos-argos-131.py` (desde 130; restituida la página de recuperaciones; `ARM = []` con tabla de desglose «SIN FILAS»; sentencia integrada con su ficha
`-SEN-001-F`). `gen-movil.py` y `gen-texto.py` sin cambios. `validar.js`: OK.

## 15. Lecciones de método (no van al cartelón)

1. **La búsqueda nacional del coordinador volvió a dar hechos que la ola no traía** (Vallado Viejo, Otatitlán), cuarta edición seguida.
2. **El boletín federal del 9 al 11-oct solo apareció por la tercera forma** (título sin `site:`): la regla de la triple consulta vuelve a demostrar su valor.
3. **Tres omisiones de 130 recuperadas** (dos rojos, un amarillo): 130 cerró a las 08:19 del lunes y los hechos del domingo por la tarde y noche se indexaron
   después. Un corte que cierra temprano deja la tarde-noche del día anterior subindexada.
4. **Sonora y Sinaloa, sentencias, cuarta edición `NO REVISADA`**: ni `fge.sonora.gob.mx` ni los dos dominios de Sinaloa aparecen en el índice. Propuesta: aceptar
   como dominio el que devuelvan los republicadores con el título del boletín, o dejar de contarlas como deuda de rotación.
5. **Ninguna fila de armamento propia** pese a 23 entidades revisadas: los aseguramientos con cifra de la semana se publicaron el 9-11 oct en el agregado federal,
   fuera de ventana.
