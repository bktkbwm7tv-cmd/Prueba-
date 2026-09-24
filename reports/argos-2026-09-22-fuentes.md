# ARGOS 123 — Archivo de fuentes, barrido y arbitrajes

**Corte**: 2026-09-22 · **Ventana**: 2026-09-21 08:57 → 2026-09-22 08:22 CDMX · **23 h 25 min**
**Rama**: `claude/argos-123-criminal-analysis-k70hzw`

---

## 1. La base: por primera vez en dieciocho ediciones, `main` venía a la cabeza

El Bloque 0 se ejecutó como primer comando de la sesión. **`git merge --ff-only origin/main` funcionó**:
`main` ya había absorbido ARGOS 122, `tools/gen-texto.py` y los cuatro arreglos del generador móvil.

**Se comprobó, no se supuso.** Se recorrieron las 43 ramas remotas buscando `reports/argos-2026-09-2[2-9]`
y `argos-12[3-9]`: **ninguna** contenía edición posterior al 21-sep. Las trece ramas que figuran "por
delante" de `main` (88-97, forense, intake, victimología) son divergencias antiguas ya superadas.

Estado encontrado: **`argos-2026-09-21` y 115 archivos**, exactamente lo previsto.

⚠️ **La rama designada sí llegó desactualizada en su remoto**: `origin/claude/argos-123-…` estaba en
`a1cb1d5`, **36 commits por detrás**. El `ff-only` local lo resolvió y el push la sincronizó. **La
advertencia del arranque sigue siendo válida para ARGOS 124: compruébelo, no lo suponga.**

---

## 2. Rotación de cobertura — CICLO A aplicado y declarado

| Renglón | Resultado |
|---|---|
| **Ciclo que tocaba** | **A** — Noroeste + Centro encabezan el triaje judicial |
| **Aplicado** | Sí, en las dos regiones |
| **Prioridad sobre el ciclo** | **Tamaulipas, Coahuila y Campeche encabezaron sus barridos** pese a no tocarles |
| **Resultado de la prioridad** | **Las tres quedaron saldadas.** Tamaulipas produjo el hallazgo judicial del corte (las cuatro sentencias de Nuevo Laredo); Campeche localizó su portal real |
| **Rendimiento del Ciclo A** | **Bajo en sentencias, alto en correcciones.** El triaje judicial de Noroeste y Centro **no produjo ninguna sentencia integrable**, pero sí **dos correcciones de archivo de primer orden**: el boletín 12722 de Tijuana mal atribuido y la sexta verificación fallida de la FGJEM |

**Lección para ARGOS 124 — CICLO B (Noreste + Golfo)**: la rotación se mide, no se supone. Este ciclo
**no aportó sentencias**, a diferencia del Ciclo C de ARGOS 122 (Morelia). Dos de tres ciclos recientes
han producido candidato; éste no. **No es motivo para abandonar la rotación**: es el dato que permite
compararla.

---

## 3. El recall nacional del coordinador — decimocuarta edición consecutiva

**Aportó los TRES hechos de mayor gravedad del documento**, y **ninguno de los seis barridos regionales
detectó uno solo de ellos**:

| Hecho | ARG-ID | Quién lo trajo |
|---|---|---|
| **Valle de Chalco** — 2 muertos, el único hecho fechado el 21-sep | `ARG-123-001` | **Recall** |
| **Tetecala, Morelos** — dirigente del PRI y su acompañante | `ARG-123-REC-001` | **Recall** |
| **Santo Domingo Tehuantepec** — 3 muertos en taller de mototaxis | `ARG-123-REC-002` | **Recall** |

**Los seis barridos regionales, entre los seis, no trajeron ni un hecho rojo.** Trajeron cobertura,
correcciones de archivo y deuda saldada —que es su función—, pero **el hallazgo de gravedad sigue
llegando por el recall**. Decimocuarta edición consecutiva. **No es sustituible por más equipos.**

---

## 4. El boletín federal: la tercera vía, otra vez, y otro cambio de formato

⚠️ **El formato volvió a cambiar**: ARGOS 121 recibió un agregado de tres días, ARGOS 122 un diario, y
ARGOS 123 **un agregado de tres días otra vez**. **El formato del emisor no es estable y no debe
suponerse por el del corte anterior.**

**Triple consulta aplicada a los tramos del 21 y del 22-sep:**

| Forma | Resultado |
|---|---|
| **1. Día suelto** — "acciones relevantes del 21 de septiembre" | **Sin boletín propio del 21 ni del 22** |
| **2. Rango o agregado** | **DEVOLVIÓ el agregado del 18, 19 y 20**, publicado el 21 |
| **3. Título sin `site:`** | **Es la que funcionó**: `gob.mx` **NO indexó** el boletín. Los únicos accesos son republicadores |

**Republicadores localizados**: `eleese.com.mx/2026/09/21/…` (**fecha en la ruta**), RED113, Talla
Política, Certeza Diario, La Capital.

⚠️ **Sustitución anotada. Corroboración débil por construcción**: varios republicadores del mismo
boletín **no son fuentes independientes**. Todas las fichas derivadas llevan la marca.

⚠️ **Contradicción entre barridos, arbitrada por el coordinador**: el barrido de Occidente reportó
haber localizado "un boletín del 21-sep" y "otro del 22-sep"; el de Noreste reportó que **no existe
agregado del 21-22, solo hasta el 20**. **Se adopta la versión del Noreste**: la verificación propia
del coordinador confirma **un solo boletín, el del 18-19-20 publicado el 21**. Lo que Occidente tomó
por "boletín del 21" es **la fecha de publicación del agregado**, no un boletín distinto.

---

## 5. ⚠️ EL ARBITRAJE ESTRUCTURAL: el coordinador se equivocó y `editor-duplicidad` lo corrigió

**Es la decisión que más cambió en esta edición, y el coordinador la perdió. Se declara entera.**

### 5.1 Lo que el borrador hizo

Los hechos del boletín federal son del **18, 19 y 20-sep** —dentro de la ventana de ARGOS 122—; su
**publicación** es del **21**, dentro de la mía. **ARGOS 122 cerró sin él.** El coordinador los integró
**como siete hechos propios verdes**, alimentando semáforo, mapa, radar y todos los totales, invocando
la regla «Periodo de corte» del módulo de armamento y un precedente: que ARGOS 122 integró los
renglones de su boletín del 17-sep.

**Tres de los seis barridos —Centro, Noreste y Golfo— recomendaron independientemente NO integrarlo.**
El coordinador decidió en contra.

### 5.2 Por qué el coordinador se equivocó

`editor-duplicidad` opuso **dos precedentes del propio archivo que el coordinador no había citado**, y
**los dos se verificaron ciertos**:

1. ⚠️ **ARGOS 121 frente al boletín federal del 14, 15 y 16-sep.** `reports/_pendientes.md` lo registra
   literalmente: ese boletín *«apareció dentro de esta ventana»*, *«cubre tres días que pertenecen casi
   enteros a la ventana de ARGOS 120»*, **el emisor no desglosa qué renglón es de qué día**, y por eso
   **«ningún renglón se integró a los totales de ARGOS 121»**. **Es el mismo supuesto de hecho,
   resuelto en sentido contrario.**
2. ⚠️ **`ARG-122-REC-002` (Angamacutiro).** Un hecho **VERDE** que el `editor-duplicidad` de ARGOS 122
   reclasificó a `-REC-` **por el solo criterio de ventana de origen**. **Derriba la tercera razón del
   coordinador**, que sostenía que el mecanismo `-REC-` está reservado a hechos rojos. **No lo está.**

Y el precedente que el coordinador **sí** citó —el boletín del 17-sep en ARGOS 122— **es distinguible
y no sostiene lo que se le hizo decir**: el 17-sep es **el primer día de la propia ventana de ARGOS
122**, que abre a las 17:36 de ese mismo día, y sus renglones llevan `FRONTERA DE VENTANA`, no
«evento anterior publicado durante el corte». **Es un caso de frontera, no de hecho íntegramente
anterior.** El coordinador citó el precedente que le favorecía y no buscó el que le contradecía.

⚠️ **Y la razón decisiva estaba en el propio borrador, confesada sin verla**: cada ficha fechaba su
hecho como **«tramo 2026-09-18/20»**. **Eso no es una fecha: es la declaración de que no se sabe cuál
es.** El emisor no desglosa por día, exactamente como en el caso de ARGOS 121. **Un hecho cuya fecha no
puede fijarse dentro de la ventana no puede contarse en los totales de la ventana.**

### 5.3 Lo aplicado

**`ARG-123-002` a `ARG-123-008` se reclasifican a `-REC-`**, con ventana de origen ARGOS 122, **fuera
del semáforo, del mapa, del radar y de todos los totales**. Efecto:

| Renglón | Borrador | Publicado |
|---|---|---|
| **Hechos propios** | 8 | **1** |
| **Semáforo** | 1🔴 / 0🟡 / 7🟢 | **1🔴 / 0🟡 / 0🟢** |
| **Recuperaciones** | 2 | **11** |
| **Densidad** | 0,34 | **0,04** |
| **Armas cortas / largas** | 10 / 23 | **0 / 0** |
| **Cartuchos / cargadores** | 9,793 / 23 | **0 / 0** |
| **Granadas / AEI / explosivos** | 1 / 20 / 25 | **0 / 0 / 0** |
| **Detenidos** | 14 | **0** |
| **Entidades con aseguramiento** | 6 | **0** |

**El módulo de armamento se cierra en `SIN ASEGURAMIENTO INTEGRABLE DURANTE EL CORTE`**, y las cifras
**no se pierden**: viven en el **registro de armamento por evento**, con su ARG-ID, su desglose y la
marca expresa de que pertenecen a la ventana de ARGOS 122 y no suman.

**Lección de método, que es la que vale para ARGOS 124**: el coordinador debe **buscar el precedente
que le contradice, no solo el que le respalda**. Cuando tres de seis equipos coinciden en contra de su
criterio, **eso es dato**, no ruido. Y **un control con mejor argumento se acata**: un arbitraje que no
puede perderse no es arbitraje.

---

## 6. ⚠️ FE DE ERRATAS A ARGOS 122 — cuatro correcciones, tres al alza

**No van al cartelón.** Viven aquí y en `_pendientes.md`, conforme a `CLAUDE.md`.

### `ARG-123-FE-001` — Puerto Peñasco: NO HAY CINCO PERSONAS SIN PARADERO. El marco heredado era falso.

⚠️ **Es la corrección más grave del archivo reciente, y es una buena noticia.**

ARGOS 122 publicó, en `ARG-122-007`, que el operativo derivó del secuestro de **ocho** personas
dedicadas a la minería artesanal en Sierra Pinta, que **se rescataron tres** y que **«las otras cinco
siguen sin paradero publicado»**. La orden de arranque de ARGOS 123 lo elevó a **primer encargo del
corte, «con vidas de por medio»**.

**Lo verificado**, por el barrido de Noroeste y **reverificado de forma independiente por el
coordinador**: las fuentes describen **dos grupos distintos**.

> *«…la privación de la libertad de ocho personas dedicadas a la actividad de gambusinos en la región
> de Sierra Pinta, **quienes posteriormente fueron liberadas**…»* — y fue **su testimonio** —rutas,
> inmuebles, una camioneta blanca tipo Suburban o Tahoe— el que **permitió ubicar el inmueble** de
> Cerrada del Sol, donde se rescató a **tres personas distintas**, identificadas como víctimas de
> desaparición cometida por particulares.

**Fuentes**: El Vigía (`elvigia.com.mx/2026/09/21/…`, fecha en la ruta, cita expresa a la Mesa de
Seguridad de Sonora), El Imparcial (20 y 21-sep, fecha en la ruta), Marquesina, Proyecto Puente,
Telemax, Sergio Valle, Entorno Informativo, Radar Sonora.

**Efecto**: **se retira del archivo la afirmación de que cinco personas siguen desaparecidas.** No
procede corregir ningún total numérico de ARGOS 122 —la cifra no alimentaba ningún conteo—, pero **sí
se retira de `_pendientes.md` como pendiente de vidas**.

⚠️ **Reserva declarada**: no se localizó boletín de `fgjesonora.gob.mx` con esta narrativa. La
corrección se apoya en **ocho coberturas regionales convergentes**, una de ellas citando a la Mesa de
Seguridad. **Si un boletín oficial posterior la contradice, debe corregirse de nuevo.** **Confianza:
Medio.**

### `ARG-123-FE-002` — Tempoal (`ARG-122-011` / `ARG-122-ARM-008`): la cantidad SÍ estaba determinada

ARGOS 122 publicó *«ARMAS Y GRANADAS SIN CIFRA NI CALIBRE: CANTIDAD NO DETERMINADA, NO SE INTEGRA AL
TOTAL NUMÉRICO»*. **El boletín federal del 18-19-20, publicado el 21, la cierra:**

| Categoría | ARGOS 122 | Corregido |
|---|---|---|
| **Armas largas** | sin cifra | **6** |
| **Granadas** | presencia sin cifra | **8** — «cinco granadas de mano» + «tres granadas» |
| **Cartuchos** | sin cifra | **300** |
| **Armamento especial** | — | **1 adaptador de lanzagranadas** |

⚠️ **Cuadre aritmético que confirma que es el mismo evento**: el boletín federal reporta **30,000 dosis
de metanfetamina + 29,400 de marihuana = 59,400**, exactamente las **59,400 bolsas herméticas** que
ARGOS 122 ya publicaba. **Misma corporación (FGE Veracruz con SEDENA, GN y SSP), mismo municipio, mismo
objeto.** No es duplicidad: es el mismo hecho con desglose.

**Efecto sobre los totales de ARGOS 122**: largas **28 → 34** · cartuchos **124 → 424** · granadas
**0 → 8** · armamento especial **4 → 5**. ⚠️ **Y deja de ser cierto que ARGOS 122 tuviera cero
granadas.**

### `ARG-123-FE-003` — Iztapalapa (`ARG-122-010` / `ARG-122-ARM-004`): el desglose estaba invertido

ARGOS 122 publicó **2 cortas y 4 largas**, tomadas de la cobertura nacional. **El boletín federal dice
5 armas largas y 1 arma corta.**

**Arbitraje por procedencia**: el **boletín del Gabinete de Seguridad es fuente institucional
primaria**; El Heraldo, El Financiero y La Razón son cobertura nacional. **Prevalece el boletín.**

**Efecto sobre los totales de ARGOS 122**: cortas **10 → 9** · largas **28 → 29** (y, acumulando la
corrección de Tempoal, **34 → 35**). **El total de armas integradas no cambia**: 6 en ambos casos.

### `ARG-123-FE-004` — Puerto Peñasco: atribución de célula no publicada por ARGOS 122

El boletín federal atribuye expresamente los **siete detenidos** del 18-sep a la **célula de «Los
Mayo» del Cártel de Sinaloa**. **ARGOS 122 no tenía esa atribución.** Dato nuevo, sin efecto numérico.

---

## 7. Arbitrajes del coordinador — en las dos direcciones

| Decisión | Dirección | Razón |
|---|---|---|
| **Valle de Chalco → 🔴 ROJO** | **Al alza** desde el amarillo que correspondería a un homicidio doloso único | **Dos agravantes tasadas concurren**: **víctimas múltiples** (2 muertos) y **víctima civil ajena al hecho** (el repartidor, por bala perdida). La escala lo exige |
| **Tetecala → 🔴 ROJO** | **Al alza** | **Víctimas múltiples** (2) y **víctima con responsabilidad política local**. ⚠️ **No se invocó «servidor público»**: un dirigente de partido municipal **no lo es** en sentido estricto, y forzar esa etiqueta habría sido inflar la clasificación. **La agravante que se invoca es la de víctimas múltiples, que es incontrovertible** |
| **Quechultenango se mantiene 🟡** | **A la baja**, por segunda edición | **El uso de explosivos sigue SIN CONFIRMAR** tras el barrido de Sureste. **Ninguna agravante tasada concurre acreditada.** Se mantiene el arbitraje de ARGOS 122 |
| **Zirándaro y Carácuaro: una sola entidad en el mapa** | **Restrictivo** | **Un solo evento en dos entidades.** Colorear ambas contaría dos veces un solo hecho y **rompería la consistencia entre mapa, radar y semáforo**. Se asigna a Guerrero y **Michoacán queda declarado en el hecho** |
| **Los siete verdes del boletín se integran** | **Al alza**, contra la recomendación de tres barridos | Ver apartado 5 |
| **«El Cholo» (`ARG-122-SEN-001`) NO se degrada** | **Se mantiene** | El barrido de Noreste propuso bajarlo a `PENDIENTE DE CONFIRMACIÓN OFICIAL`. **Rechazado**: ARGOS 122 lo integró con confianza **Medio** —*fuente oficial única con datos suficientes*, por atribución expresa a la FGR— y **el barrido no aporta evidencia de inexistencia; al contrario, amplía la corroboración a siete medios**. **Degradar por no encontrar el folio sería castigar el bloqueo de egreso, no el dato** |

---

## 8. Candidatos agotados y cerrados

| Caso | Disposición | Motivo |
|---|---|---|
| ⚠️ **AGUASCALIENTES · Cosío, El Salero** | **UMBRAL DE AGOTAMIENTO — SE RETIRA DEL ARCHIVO** | **Quinto intento fallido.** El boletín **existe y se localizó** (`gob.mx/guardianacional/prensa/en-aguascalientes-gn-y-ejercito-mexicano-detienen-a-tres-personas-y-aseguran-17-armas-largas-mas-de-mil-500-cartuchos-y-posible-marihuana`), pero **ni el slug ni ningún republicador llevan fecha**. ⚠️ **Corrección de dato al retirarlo: el Barrett cal. .50 está DENTRO de las 17 largas, no es adicional.** «Más de mil 500 cartuchos» **nunca fue cifra** |
| ⚠️ **MICHOACÁN · el municipio «MAZATLÁN»** | **SE RETIRA** | Intento único agotado. No se localizó corrección del municipio. **Era obra del resumidor: no existe Mazatlán en Michoacán** |
| ⚠️ **BAJA CALIFORNIA · Tijuana, boletín 12722** | **NO ERA CASO HOMÓNIMO: ERA FUENTE MAL ATRIBUIDA** | El boletín 12722 es de **Carlos Josué Gómez Martínez**, **23 años 4 meses**, **518,700 pesos** de reparación, víctima **su concubina**, hecho del **19-dic-2023** en Valle de las Palmas, abreviado del **2-dic-2024**. **Ni un solo campo coincide** con Luis Martín «N» (26 a 8 m, 500 UMA, 874,680 pesos, hecho del 1-abr-2025). **Se retira como fuente de ese caso.** Y el caso Luis Martín es del **9-sep**: **fuera de ventana** en cualquier supuesto |
| **TAMAULIPAS · Nuevo Laredo, Carlos/Adrián/Luis/José «N»** | **RECLASIFICADO, no cerrado** | **Deja de ser «aseguramiento con fecha pendiente» y pasa a «sentencia pendiente de confirmación oficial»**: las penas ya están dictadas —**15 a 6 m, 15 a 6 m, 11 a 6 m y 8 años**, FGR—. **La fecha del aseguramiento original sigue `NO DETERMINABLE BAJO BLOQUEO DE EGRESO`** |
| **CHIHUAHUA · Cd. Juárez, José Manuel E. C.** | **TERCERA EDICIÓN `SIN RESULTADO INDEXADO EN VENTANA`** | Tres búsquedas gastadas, como se ordenó. ⚠️ **NO se afirma que la audiencia se pospusiera: no está acreditado.** Sugerencia del barrido para ARGOS 124: buscar «individualización de sanciones» **sin restricción de fecha**, porque el boletín de la pena usaría **otro slug** que el del fallo |

---

## 9. Correcciones de dominio institucional — tres confirmadas, dos corregidas

| Entidad | Estado |
|---|---|
| **Querétaro** `sscqro.gob.mx` | ✅ **CONFIRMADO**, con sección `/boletin/` activa. ⚠️ Ignorar `dummy.sscqro.gob.mx`, artefacto de indexación |
| **Hidalgo** `s-seguridad.hidalgo.gob.mx` | ✅ **CONFIRMADO**. Sin sección de boletines detectada en lo indexado |
| **Tlaxcala** `ssc.tlaxcala.gob.mx` | ✅ **CONFIRMADO**. Sin sección de boletines detectada |
| ⚠️ **Michoacán** | **CORREGIDO**: la sala de prensa es **`comunicacion.fiscaliamichoacan.gob.mx`**, **no** `fge.michoacan.gob.mx`. **Las ediciones anteriores intentaron el dominio equivocado** |
| ⚠️ **Campeche** | **CORREGIDO**: los boletines de SSP y FGE viven en **`ucs.campeche.gob.mx`** (Unidad de Comunicación Social), **no** en `ssp.campeche.gob.mx` ni `fiscaliageneral.campeche.gob.mx` |

---

## 10. Registro del barrido — cobertura entidad por entidad

| Región | Entidades | Cobertura | Casilla dominante |
|---|---|---|---|
| **Noroeste** | BC, BCS, Son, Sin, Chih, Dgo | **5 de 6** | `SIN RESULTADO INDEXADO EN VENTANA` · **BCS `NO REVISADA`** |
| **Noreste** | Coah, NL, Tam, Zac, SLP | **5 de 5** | `SIN RESULTADO INDEXADO EN VENTANA` · Zacatecas y Coahuila, cobertura superficial |
| **Occidente** | Jal, Mich, Col, Nay, Ags, Gto | **6 de 6** | `SIN RESULTADO INDEXADO EN VENTANA` |
| **Centro** | CDMX, Edomex, Mor, Pue, Tlax, Qro, Hgo | **7 de 7** | `SIN RESULTADO INDEXADO EN VENTANA` · ninguna agotó sus cuatro portales |
| **Golfo** | Ver, Tab | **2 de 2** | `SIN RESULTADO INDEXADO EN VENTANA` |
| **Sureste** | Chis, Oax, Gro, Camp, Yuc, QR | **6 de 6** | `SIN RESULTADO INDEXADO EN VENTANA` · **Chiapas sí publicó en ventana** |

**Universo de revisión: 33 = 32 fiscalías + FGR. Revisadas: 31 de 32 + FGR.**
`SIN ACTUALIZACIÓN CONSTATADA`: **0** — exige lectura directa, imposible bajo bloqueo de egreso.

⚠️ **Búsquedas gastadas**: Noroeste 19/20 · Noreste 18/20 · Occidente 19/20 · Centro **20/20** ·
Golfo 14 · Sureste **20/20**.

---

## 11. Limitación de herramienta — reverificada, y el techo BAJA

⚠️ **El bloqueo de egreso alcanza también a los medios. CUARTA edición consecutiva.**

Sonda del coordinador, ejecutada al arrancar:

```
gob.mx -> 000          fgebc.gob.mx -> 000        eluniversal.com.mx -> 000
www.gob.mx -> 000      fge.michoacan.gob.mx -> 000  milenio.com -> 000
```

**Seis de seis dominios, oficiales y de medios, devuelven `000`.** `WebFetch` sobre
`eleese.com.mx` —un republicador, ni siquiera `.gob.mx`— devolvió **`EGRESS_BLOCKED`**.

**Consecuencia**: **ningún documento primario pudo leerse íntegro.** **El techo de confianza del
producto es ★★★☆☆**, no ★★★★☆: la escala reserva ★★★★☆ para *fuente institucional + un medio nacional*,
y aquí **ni la fuente institucional ni el medio pudieron leerse directamente** — todo llegó por el
resumen del buscador.

`docs/solicitud-lista-blanca-egreso.md` **sigue sin tramitar. Es la única solución real.**

---

## 12. Señuelos descartados — no redescubrirlos

- **Sinaloa · Pánuco, 10 mineros secuestrados (enero 2026)** — apareció al buscar «mineros
  secuestrados» y **estuvo a punto de confundirse con Sierra Pinta**. **Otro estado, otra cifra, otra
  fecha.** Descartado expresamente.
- **Nuevo León · 210 armas de Texas en semirremolques** — hecho del **30-31 de agosto**. Muy anterior.
- **Veracruz · «72 cortas, 54 largas, 139 cargadores, 2,508 cartuchos» (SSP)** — el artículo está
  fechado **22-feb-2026** en el propio portal. **No es del corte.**
- **Tabasco · «cuerpos calcinados de mecánicos desaparecidos», Cárdenas** — caso de **mayo de 2025**.
- **Veracruz · «37 resoluciones judiciales»** — ⚠️ **corrección al pendiente heredado**: ese titular es
  de un boletín del **7-sep**, no del 18. El del 18-sep dice **«16 sentencias condenatorias, 1 fallo y
  33 vinculaciones»** con **«50 resoluciones»** en el cuerpo. **No eran tres cifras del mismo boletín:
  eran dos boletines distintos.** La FGE reutiliza la plantilla del titular.
- **Guanajuato · Dolores Hidalgo, «400 armas»** (21-sep, portal oficial) — **no es aseguramiento**: es
  **destrucción/conversión artística de armamento ya decomisado**. Evento cualitativo, no entra.
- **Infobae, liveblog del 21-sep** «caen 7 sicarios y liberan a 3 gambusinos» — **liveblog: no fecha un
  hecho ni basta como fuente única**, y además **el hecho ya es `ARG-122-007`**.

---

## 13. Vacíos de publicación que el mando debe conocer

- ⚠️ **CERO SENTENCIAS INTEGRABLES** en 31 fiscalías más la FGR, en 23 h 25 min.
- ⚠️ **CDMX · Tepito**: **CUARTA edición sin boletín** de SSC ni FGJ. **Tres versiones de edades siguen
  sin arbitrar**: 25-30, 18-19 (Abigail Herrera, 19, y Odette Rosas, 18) y 15-20.
- ⚠️ **EDOMEX · `fgjem.edomex.gob.mx`**: **SEXTA verificación sin boletín primario.** Temoaya (125
  años), Coacalco (36 a 3 m) y Hueypoxtla (21 a 10 m 15 d) **siguen sin integrar en ninguna edición**.
- ⚠️ **GUERRERO · Quechultenango y Mochitlán**: la contradicción **empeoró**. Ahora hay **seis
  versiones numéricas**: 10 heridos (alcalde) · 5 heridos y 0 muertos (SEDENA) · **8 heridos** (5
  policías estatales + 3 GN, carpetas de la FGE) · 19, 22 y 29 retenidos según fuente.
  **Dato nuevo: el armamento de cargo SÍ fue devuelto** tras ~6,5 horas de negociación, **sin
  inventario institucional**.
- **TABASCO · FGET**: sin boletín de las ejecuciones del 15-sep. **La cifra misma está en disputa**:
  La Silla Rota dice **6**, El Universal y otros dicen **4**.
- **GUANAJUATO · corredor Laja-Bajío**: `periodicocorreo.com.mx` (21-sep) atribuye a la FGE **«23
  muertos y 11 heridos del 18 al 20-sep»** y **«14 muertos en Valle de Santiago en ocho días»**.
  ⚠️ **FUENTE ÚNICA REGIONAL, SIN BOLETÍN DE LA FGE. NO SE INTEGRA NI SE CITA EN EL CARTELÓN.** Es el
  vacío más grande del corte: **si la cifra es cierta, un solo corredor superaría por sí solo todos los
  muertos del documento.**

---

## 14. Deuda de método que ARGOS 123 deja abierta

1. ⚠️ **El techo de confianza bajó a ★★★☆☆ y nadie puede subirlo desde dentro.** Cuarta edición.
2. ⚠️ **Los barridos regionales no producen hechos rojos.** Catorce ediciones. **Pregunta abierta para
   ARGOS 124: ¿deben los barridos incluir un recall genérico de sucesos por región, o su función es
   solo de cobertura institucional?**
3. ⚠️ **La ventana corta y el boletín de días anteriores rompen la comparabilidad.** La densidad de
   0,34 **no significa más violencia**. **Toda serie de densidades debe anotar si el corte se sostiene
   en un agregado ajeno a su ventana.**
4. **El generador de texto era frágil ante un cambio de formato de la declaración de ventana.**
   Corregido: ahora **falla con un mensaje que nombra el formato canónico exigido**, en vez de un
   `AttributeError`.

---

## 15. Los dos controles editoriales — ejecutados, y los dos devolvieron hallazgos reales

⚠️ **ARGOS 121, 122 y 123 los ejecutaron y los seis pases devolvieron `CORREGIR ANTES DE PUBLICAR`
con hallazgos reales. La racha se mantiene, y esta vez uno de ellos cambió la edición entera.**

### 15.1 `editor-duplicidad` — el hallazgo estructural

- ⚠️ **Reclasificación de siete hechos a `-REC-`** — ver apartado 5. **El hallazgo más grande que un
  control ha producido en la serie.**
- ⚠️ **DESLINDE FALSO en `ARG-123-002`**: afirmaba que *«Ciudad Juárez figura en el índice por el
  fallo condenatorio de José Manuel E. C.»*. **Falso: ese caso NO está en el índice**, es un
  **candidato no integrado** del propio corte. **Es el mismo tipo de error que este control detuvo en
  ARGOS 122.** Corregido en la ficha, ahora `ARG-123-REC-004`.
- **Reimpresión de «total de armas integradas: 33»** en la tarjeta de armas largas, pese a que el
  propio módulo declaraba no reimprimir totales. **Resuelto al vaciar los totales.**
- **Falta de línea de deslinde en la ficha de Durango.** **Corregido**: ahora deslinda expresamente
  contra Tamazula, contra `ARG-119-010` y contra `ARG-122-005`/`-009`.
- ⚠️ **DEFECTO TÉCNICO REAL — el mapa pintaba `fill="undefined"`.** `SEVERITY_COLOR["rec"]` no existía,
  de modo que **Morelos y Oaxaca se pintaban con un valor SVG inválido** y su tooltip decía
  «Nivel: undefined» — **violando literalmente el texto de sus propias fichas** («fuera del mapa») y la
  regla de `CLAUDE.md` de que el mapa nunca se genera con colores ficticios. El radar, además,
  **dibujaba las recuperaciones como ecos clicables**.
  **Corregido de raíz, no parcheado**: se definieron `SEVERITY_COLOR.rec` y `SEVERITY_LABEL.rec`, y
  mapa y radar del corte reciben ahora `EVENTOS_CORTE`, un arreglo derivado que excluye las
  recuperaciones. **Y el validador comprueba las dos cosas a partir de ahora.**
- ✅ Verificó que **Iztapalapa, Tempoal y Puerto Peñasco** —los tres que el coordinador ya había
  retirado— **no reaparecen** en ninguna de las tres versiones.
- ✅ Verificó **ciertos** los deslindes de Tetecala/Mazatepec, Tehuantepec/Zanatepec y Amuzgos,
  Zapopan, Reynosa y Puebla/El Caracol.

### 15.2 `procedencia-cifras` — cifras, y dos eventos que faltaban

- ⚠️ **COMPARACIONES CONSTRUIDAS SOBRE CIFRAS QUE LA PROPIA EDICIÓN YA HABÍA CORREGIDO.** Las tarjetas
  decían «igual que las 10 del corte anterior», «frente a 28», «79 veces los 124», «frente a 0
  granadas», «frente a 4» — **cuando este mismo archivo de fuentes documenta que esos valores son 9,
  35, 424, 8 y 5**. **El cartelón se contradecía con su propio archivo de fuentes.**
  **Corregido retirando las comparaciones**, no actualizándolas: la edición ya declara que sus totales
  no son comparables, y publicar comparaciones lo contradecía.
- ⚠️⚠️ **UN EVENTO ENTERO FALTABA: TAMAZULA, DURANGO.** El mismo boletín traía **un segundo renglón de
  Durango** —**3 detenidos, 2 armas largas, 1 corta, cargadores sin cifra, equipo táctico**— que el
  borrador **no había fichado**. **Verificado por el coordinador**: existe, es distinto del cateo de
  seis inmuebles, y la cobertura regional suma los dos (4 + 3 = «siete detenidos el fin de semana»),
  **suma que es de la fuente y no de ARGOS**. Añadido como `ARG-123-REC-009` / `ARG-123-ARM-006`.
- ⚠️⚠️ **ZIRÁNDARO ERA AMARILLO, NO VERDE, Y TENÍA TRES MUNICIPIOS, NO DOS.** **Verificado por el
  coordinador**: son **cuatro laboratorios** en **Zirándaro y Coahuayutla de José María Izazaga
  (Guerrero) y Carácuaro (Michoacán)**, y **durante los trabajos el personal federal fue agredido con
  disparos**. Por la regla de **quién inicia** —el Estado ejecuta y es repelido— **el hecho es 🟡**.
  Y aparecieron **cifras que el borrador no tenía**: **45 ollas, 57 tinas, 6 contenedores de 1,000
  litros y un procesador industrial**.
- ⚠️ **«CIFRA CONTRADICHA» MAL PLANTEADA EN VALLE DE CHALCO.** No eran dos cifras del mismo hecho:
  eran **dos ataques distintos** —el **domingo 20** en el tianguis de la colonia Santa Cruz (2 muertos)
  y el **lunes 21** en la carretera (2 muertos)—, y los portales que titulan «cuatro muertos» **suman
  ambos**. **Corregido**: la etiqueta de contradicción se retira y se sustituye por un **deslinde entre
  los dos hechos**. ⚠️ **Y el del domingo resultó ser un hecho que ARGOS 122 no publicó**: se añade
  como `ARG-123-REC-003`, **un cuarto homicidio múltiple recuperado**.
- ⚠️ **UMA mal convertida.** «84 UMA (9,503.76 pesos)» corresponde a la **UMA de 2025** (113.14), no a
  la vigente en septiembre de 2026 (117.31 → 9,854.04). **Corregido retirando la conversión y dejando
  «84 UMA»**: la cifra en pesos es de la fuente, no de ARGOS, y el caso **no se integra** de todos
  modos. **No procede que ARGOS recalcule una cifra ajena.**
- ✅ **La aritmética del registro de armamento cuadra fila por fila**, recalculada de forma
  independiente por el control y por el coordinador.

### 15.3 Totales antes y después de los controles

| Renglón | Borrador | Publicado | Motivo |
|---|---|---|---|
| **Hechos propios** | 8 | **1** | Reclasificación a `-REC-` |
| **Semáforo** | 1/0/7 | **1/0/0** | ídem |
| **Recuperaciones** | 2 | **11** | ídem, más Tamazula y el tianguis |
| **Fichas totales** | 10 | **12** | dos eventos que faltaban |
| **Densidad** | 0,34 | **0,04** | 1 ÷ 23,4167 |
| **Todos los totales de armamento** | 33 armas, 14 detenidos | **0** | ninguno es del corte |
| **Color de Zirándaro** | 🟢 | **🟡** | agresión armada durante el operativo |
| **ARG-ID publicados** | 16 | **19** | dos eventos nuevos y su fila de armamento |

⚠️ **Sin los dos controles, esta edición habría publicado siete hechos ajenos a su ventana como
propios, un módulo de armamento con 33 armas que no le correspondían, un deslinde falso, un mapa con
dos estados pintados de `undefined`, comparaciones contra cifras que ella misma había corregido, un
evento entero omitido y un hecho amarillo clasificado como verde. Los dos son obligatorios y esta
edición es la prueba más clara de la serie.**
