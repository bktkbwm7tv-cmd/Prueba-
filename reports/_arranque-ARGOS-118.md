# ORDEN DE ARRANQUE — ARGOS 118

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 117** (corte 2026-09-07).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git fetch origin main                              # traer el estado real
git log --oneline -1 origin/main                   # ¿main está al día?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6             # ¿cuál es la última edición del archivo?
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 118**: última edición `argos-2026-09-07` (ARGOS 117), **96 archivos**
en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló ONCE ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 117 mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición
> y **62 archivos** —**once ediciones por detrás**—: numerar por lo que la rama tenía a la vista habría
> producido **un falso «ARGOS 107» con ventana solapada de trece días**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 118** |
| **Corte** | la fecha real del día, verificada con `TZ=America/Mexico_City date` |
| **Ventana** | **abre 2026-09-07 08:16 CDMX** (cierre de ARGOS 117) y cierra a la hora real de arranque |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `reports/argos-<FECHA>-movil.html` · `reports/argos-<FECHA>-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-119.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de solape.
**Verifique la hora, no la suponga.**

⚠️ **La serie sigue sin ventanas estables**: 47 → 25 → **46 h 30 min**. ARGOS 117 duró **casi el doble**
que la anterior y produjo **7 hechos frente a 5**: **menos densidad por hora, no más**.
**Ninguna edición es comparable con otra sin normalizar por duración**, y así se declaró en portada y
Valoración. **Conviene sostener horas de arranque estables para que la serie recupere comparabilidad.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-07-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO TRAIGA, INMEDIATAMENTE
   ANTES DE FICHAR — NO SOLO SOBRE LOS QUE ESTE ARCHIVO ENUMERA.** En ARGOS 117 obligó a **escribir dos
   deslindes que el borrador no tenía**: **Buenavista, Michoacán** devolvió `ARG-99-002` y
   `ARG-104-REC-002` —otra fecha, otra colonia, otro tipo de hecho— y **Cosío, Aguascalientes** devolvió
   `ARG-115-007`, mismo municipio y otro caso.

   ⚠️⚠️ **Y LA LECCIÓN NUEVA, QUE ES LA MÁS IMPORTANTE DE ESTE ARRANQUE:
   EL `grep` POR CIFRAS DISTINTIVAS NO BASTA. HAY QUE BUSCAR EL TITULAR POR ESAS CIFRAS.**
   El candidato **«Michoacán · diez municipios»** —9 detenidos, 10 armas, **459 cartuchos**,
   **18 cargadores**, 3 vehículos— no estaba en el archivo, de modo que el `grep` lo dejaba pasar como
   `FECHA NO FIJADA` y se habría heredado **corte tras corte, indefinidamente**. **Una sola búsqueda de
   «459 cartuchos» y «18 cargadores» devolvió el titular fechado**: es el **cierre del «Plan Michoacán
   por la Paz y la Justicia», con detenciones del 31-dic-2025**. **El `grep` prueba que un hecho ya está
   publicado; solo la búsqueda por cifras prueba que es viejo.**

   ⚠️ **Y el `grep` debe ser por TOPÓNIMO DE LOCALIDAD, no solo por entidad y municipio.**
   «Cuauhtémoc» es municipio de **Colima**, de Zacatecas, de Chihuahua **Y** alcaldía de CDMX ·
   «Matamoros» está en Tamaulipas Y Coahuila · «Los Reyes» en Michoacán Y Edomex · «Buenavista» en
   Michoacán tiene **tres hechos distintos en tres colonias** · **«San Rafael» es colonia de la alcaldía
   Cuauhtémoc, CDMX, Y municipio de Veracruz** · «Rosario»/«El Rosario» en Sinaloa · «Villa de La Paz»
   es de San Luis Potosí, **no de Guerrero**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 118 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. OCTAVA EDICIÓN COMO PASO
OBLIGATORIO.**

| Origen del hecho | ARGOS 114 | ARGOS 115 | ARGOS 116 | **ARGOS 117** |
|---|---|---|---|---|
| Barridos regionales | 3 de 8 | 6 de 7 | 4 de 6 | **3 de 7** |
| Recall y arbitraje del coordinador | 5 de 8 | 1 de 7 | 2 de 6 | **4 de 7** |

⚠️ **LAS DOS VÍAS SON INDISPENSABLES POR RAZONES OPUESTAS, Y ESTA EDICIÓN LO DEMUESTRA MEJOR QUE
NINGUNA. NO RETIRE NINGUNA.**
- **El recall aportó el único rojo y el mayor verde** —Juan R. Escudero y Acapulco—, **más Colima y
  CDMX**, y **ningún barrido vio ninguno**. La causa es estructural: **un hecho nacional de gran
  cobertura se busca mejor por tema que por entidad**.
- **Los barridos aportaron los tres que ninguna consulta nacional habría devuelto**: **Buenavista**
  (única fila de armamento con categoría), **Reynosa** y **Gómez Palacio** (**la única sentencia
  integrable del corte**).

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene dos preguntas, el tope
es **de dos en total, no de dos por pregunta**. **Cerrar un seguimiento en `SIN AVANCE` es el resultado
correcto cuando no hay dato**: en ARGOS 117 lo fue en cuatro de los seis ejes.

✅ **LA REGLA DE `site:` FUNCIONA. EL OBJETIVO PORCENTUAL SIGUE RETIRADO — NO LO REINTRODUZCA.**

> **`site:` SOLO contra dominios con fecha en la ruta; contra los demás, consulta genérica.**

**Dominios con fecha en la ruta — no los redescubra**: **Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/`**
(⚠️ **el que produjo la única sentencia integrable de ARGOS 117: consúltelo siempre**) ·
Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` (**publicó el 4-sep; sigue siendo el portal
estatal más fiable**) · Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/` ·
San Luis Potosí `seguridad.slp.gob.mx/noticias/AAAA/M/D/` · Veracruz `veracruz.gob.mx/AAAA/MM/DD/`
(**la vía de Veracruz, no la FGE**).

**Sin fecha en la ruta (use genérica)**: Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa
`fiscaliasinaloa.mx` y `sspsinaloa.gob.mx` · Chihuahua `fiscalia.chihuahua.gob.mx` (⚠️ **exija ancla de
republicador fechado**) y `sspe.chihuahua.gob.mx` (⚠️ `ssp.chihuahua.gob.mx` es FALSO) ·
Colima `fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` · Edomex **`fiscaliaedomex.gob.mx`**
(⚠️ **verificado en ARGOS 117 como el dominio correcto; `fgjem.edomex.gob.mx` no devuelve nada útil**) ·
BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` · Coahuila `sspcoahuila.gob.mx` ·
Tamaulipas `tamaulipas.gob.mx/seguridadpublica/` · Tabasco `fiscaliatabasco.gob.mx` ·
Aguascalientes `aguascalientes.gob.mx/ssp/` · Puebla **`fiscalia.puebla.gob.mx`** (⚠️
`fiscaliapuebla.gob.mx` y `fgepuebla.gob.mx` **NO EXISTEN**) y `ssp.puebla.gob.mx` ·
Hidalgo **`procuraduria.hidalgo.gob.mx`** (⚠️ **NO EXISTE una «Fiscalía General del Estado de Hidalgo»**;
⚠️ **`@FGR_Hgo` es la delegación federal, no la fiscalía estatal**) ·
Morelos `morelos.gob.mx/ultimas-noticias` (⚠️ **trampa de año Y de fecha fabricada: ver Bloque 6**) ·
**`fge.yucatan.gob.mx`** (**mejor taxonomía judicial de las 32: «sentenciados a prisión en juicio
abreviado», «fallo condenatorio en procedimiento abreviado». Consultado en ARGOS 117 sin resultado en
ventana; CONSERVE EL ENCARGO**).

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** · **FGE Veracruz** (siete cortes de agregados
sin individualizar) · **`ssypc.nayarit.gob.mx`** · **`fgjsonora.gob.mx`** (vacío de portal; **Sonora
sigue revisada por vía genérica**) · **`fiscaliaguerrero.gob.mx`** (lo más reciente indexado es de
julio). **No publican indexable**: FGJ Nuevo León · SSP Zacatecas.

### 3.2 Cobertura — qué encabeza el triaje y a quién se le asigna la deuda

✅ **NO QUEDA NINGUNA ENTIDAD `NO REVISADA` EN NINGUNO DE LOS DOS CUADRES.**
**Cuadres de ARGOS 117: nacional 6 + 26 + 0 + 0 = 32 · judicial 1 + 31 + 0 + 0 = 32.**

**A ARGOS 118 le toca el CICLO B — Noreste + Golfo** encabezando el triaje judicial; las otras cuatro
encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

⚠️ **MATIZ CONFIRMADO EN ARGOS 117 SOBRE CÓMO DIRIGIR EL TRIAJE JUDICIAL.** Dirigirlo **a las
delegaciones de la FGR** produce **candidatos**; pero **la que produjo el único INTEGRABLE fue una
fiscalía estatal con fecha en la ruta** —Durango—. **Combine los dos criterios, no sustituya uno por
otro**: primero el dominio estatal **con fecha en la ruta** de la región, después las delegaciones de
la FGR.

⚠️ **DEUDA REGIONAL — dos encargos se CIERRAN y queda uno:**
- ✅ **ANAM / Aduanas — CERRADO.** Consultada por Noroeste; `SIN RESULTADO INDEXADO EN VENTANA`.
- ✅ **Mesas de Construcción de la Paz — CERRADO en Noroeste, Centro y Golfo.** **Sonora quedó como
  `VACÍO ACREDITADO`** tras dos consultas sin indicio.
- ⚠️ **Mesas de Paz de las 6 entidades del SURESTE → hueco NUEVO, `NO REVISADA`.** Sureste no gastó
  búsqueda dedicada **pese a que el hecho de Guerrero lo justificaba**. **Encabeza su encargo.**

### 3.3 Los seguimientos que más rinden

1. ⚠️ **GUERRERO — EL AGENTE DE LA GN QUE DENUNCIÓ A SUS MANDOS Y APARECIÓ DESCUARTIZADO.**
   *Máxima prioridad, y es nuevo.* **Dos búsquedas.**
   `ARG-117-001`: **Eduardo Bustos Pérez**, agente de la GN de una **Coordinación con sede en Iguala**
   (numeral contradicho, 27 o 37), comisionado en **El Ocotito**, hallado descuartizado en **Plan de
   Lima, Juan R. Escudero**, con **2 o 3 víctimas más** —`CIFRA CONTRADICHA (3 o 4)`—, **horas después
   de difundir un video de ocho minutos** señalando a **un cabo Medina de su corporación** y a un
   **«Montoro» de la fiscalía estatal** como operadores de **«Los Tlacos»** contra **«Los Ardillos»**.
   **SEDENA confirmó su identidad. Las acusaciones NO están acreditadas.**
   Qué buscar: **detenciones o imputaciones posteriores** · **situación administrativa del cabo Medina
   y del funcionario «Montoro»** · **identidad de las otras víctimas**.
   **Por qué importa**: **es una denuncia de captura institucional formulada por un elemento en activo**,
   y **la respuesta detuvo a la organización que el video presenta como perjudicada** (`ARG-117-002`).
2. ⚠️ **MICHOACÁN — ¿DRONES EN LA EMBOSCADA DE ZINAPÉCUARO?** **Una búsqueda.**
   `ARG-117-REC-001`: **1 militar muerto y 3 o 4 heridos** (contradicha) en el ataque a la **Base de
   Operaciones Interinstitucional**, poblado **Santa Cruz**, camino rural a **San José Carpintero**,
   **4-sep antes de medianoche**. **El uso de drones lo atribuyen «fuentes allegadas al caso» y ningún
   boletín lo confirma.**
   **Por qué importa**: **es la pregunta que decide la categoría del adversario** —la lista roja recoge
   expresamente los drones armados—. **El hecho es de la ventana de ARGOS 116 y está FUERA de todos los
   totales de 117: si aparece algo nuevo es HECHO NUEVO de su ventana, no una ampliación del `-REC-`.**
3. ⚠️ **NACIONAL — TRES ATAQUES LETALES CONTRA PERSONAL FEDERAL EN UNA SEMANA.** **Una búsqueda.**
   **Omealca (Veracruz, 4-5 sep, SSPC)**, **Zinapécuaro (Michoacán, 4-sep, SEDENA)** y **Juan R.
   Escudero (Guerrero, 5-sep, Guardia Nacional)**: **tres entidades no colindantes, tres corporaciones**.
   Qué buscar: **si hay un cuarto en la nueva ventana**, y **si alguna autoridad lo lee como serie**.
   **Es el patrón de mayor valor que deja ARGOS 117 y no está acreditado como serie: solo observado.**
4. ⚠️ **ZACATECAS — LA FENAZA, HASTA EL 20 DE SEPTIEMBRE.** **Dos búsquedas.**
   **La ventana de ARGOS 118 vuelve a caer dentro.** **El dispositivo de 787 elementos (`ARG-115-001`)
   NO se recuenta.** **ARGOS 117 cerró la segunda y la tercera jornadas sin incidente, amenaza,
   detención ni artefacto** en el recinto o su perímetro. **El indicador sigue siendo si aparece
   artefacto en zona de concentración masiva.** **Es el seguimiento más perecedero del archivo.**
5. **GUERRERO — las 12 armas y las 10 tragamonedas de Acapulco** (`ARG-117-002`). **Una búsqueda.**
   **Las 12 armas se integraron SIN estar fijadas en titular y sin desglose ni calibre**; **las 10
   tragamonedas sí están en titular** y son **el único activo con trazabilidad financiera** del
   aseguramiento —tienen propietario, proveedor y permiso—.
   Qué buscar: **desglose y serie de las 12** · **padrón y proveedor de las tragamonedas** ·
   **situación jurídica de los 16 y del operador financiero**.
6. **CHIHUAHUA — el AEI de Villas del Real** (`ARG-115-003`). **Una búsqueda, y solo si sobra.**
   `SIN AVANCE` en peritaje y en auditoría de uniformes de la DSPM, **segunda vez**. ✅ **Dato nuevo de
   ARGOS 117: causa penal 1486/2026**, Juez de Control del **Distrito Judicial Morelos**, calle **Rey
   David**, ~242 g de cristal — **es la primera referencia procesal y hace rastreable el expediente**.
   **Siguen habiendo DOS piezas explosivas íntegras en el archivo y NINGUNA caracterizada**, con el
   niple de Piedra Gorda. **Cartuchos cal. .45 en disputa (13/23/36): `NO SE ARBITRA`.**
7. ⚠️ **NO gaste NINGUNA búsqueda en**: **protección balística** · **Agua Verde** (cerrado: es Rosario) ·
   **«16 detenidos y 22 armas»** · **Tabasco «26 detenidos»** · **Coatzacoalcos–Villahermosa** ·
   **Tihuatlán** (`ARG-102-REC-004`) · **San Bernardino Tlaxcalancingo / «El Dron»** (`ARG-109-004`) ·
   **«Michoacán · diez municipios»** (**CERRADO: es el cierre del Plan Michoacán de dic-2025**) ·
   **Hidalgo · Tepeji del Río y Huichapan** (**CERRADO: 27-jul-2026**) · **Nayarit · Acaponeta**
   (**CERRADO por ventana y umbral**) · **Michoacán · Chinicuila** y **Nuevo León · 6 del Cártel del
   Noreste** (**CERRADOS por ventana**) · **la serie de rafagueos de Coatzacoalcos** (**CERRADA con
   resultado positivo: El Calamar 29-ene, El Cubanito 20-may, La Ventanita 31-ago**) ·
   **Bocoyna/Maguarichi** · **San Miguel de Allende** · **Poza Rica** · **Pedernales** · **Tlaxcala** ·
   **FGE Veracruz** · disputa forestal Michoacán/Guerrero · **Petatlán y Totolapan** · **Loxicha** ·
   **Matamoros serie y marcaje** · **el accionador de Villa García** · **«El Niño Concepción»** ·
   **`fiscaliaguerrero.gob.mx`** · **`fgjsonora.gob.mx`**.
   ⚠️ **PERO RECUERDE LA REGLA: estas prohibiciones van contra el PENDIENTE, no contra el TOPÓNIMO.
   Si aparece un hecho NUEVO, en ventana, en cualquiera de esos lugares, SE INFORMA Y SE FICHA.**
8. **Una sola búsqueda, y solo si sobra**: el **cohecho de Tempoal** (`ARG-116-005`) · la **marca y lote
   del inhibidor de Puebla** (`ARG-116-003`) · las **detenciones de Omealca** (`ARG-116-001`, `SIN
   AVANCE`) · **Tepuche** (`ARG-116-REC-001`, `SIN AVANCE` en las dos preguntas) · la **contradicción de
   lesionados de `ARG-110-001`** (**octava edición sin arbitrar**).

### 3.4 `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verifíquelo cada corte

**Verificado de nuevo en ARGOS 117, séptima vez consecutiva**: la migración **está acreditada** —desde el
1-sep los reportes diarios de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí— pero
**ningún reporte resulta alcanzable**: **el dominio está indexado, sus rutas no llevan fecha** y **la
trampa de año persiste**. **Ninguna cifra suya se usa.** **Verifíquelo cada corte y declare el resultado.**

---

## BLOQUE 4 — EL BLOQUEO DE EGRESO NO ES SOLO DE `*.gob.mx`

⚠️ **Sigue siendo el hallazgo de método que más condiciona al producto.** El acceso directo devuelve
`curl: (56) CONNECT tunnel failed, response 403` **tanto en `*.gob.mx` como en medios regionales**.
**En ARGOS 117 ninguno de los seis barridos intentó `WebFetch`**, conforme a la instrucción, y
`procedencia-cifras` lo confirmó en varios dominios.

> ⚠️ **REGLA OPERATIVA, AHORA CON DOS GRADOS.** La regla «una verificación cuenta solo si devuelve un
> TITULAR, ENCABEZADO o URL que CONTENGA el dato» **sigue vigente y no se relaja**. Cuando un dato no
> pueda fijarse por bloqueo, la decisión **se razona caso por caso y se declara en la ficha**, y
> **hay dos grados de reserva, no uno**:
> - **Reserva fuerte, integrable**: el dato **encaja aritméticamente con una cifra que el titular SÍ
>   fija** —«3 largas + 4 cortas» suma exactamente las «7 armas» del titular de ARGOS 116—.
> - ⚠️ **Reserva débil, integrable pero con la fila degradada**: **no hay ninguna cifra en titular con la
>   que cuadre**, solo **convergencia de fuentes atribuidas a la misma autoridad**. Es el caso de las
>   **12 armas de Acapulco** en ARGOS 117: se integraron, **la fila bajó a Bajo** por corroboración
>   asimétrica, y **la reserva se declaró también en portada y en la página de armamento**.
> **Conserve la distinción: confundir los dos grados es publicar como firme lo que no lo es.**

**Techo de confianza: ★★★★☆.** `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
**Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige
lectura directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las casillas deben CUADRAR con las 32 entidades.** ARGOS 117 cuadró **dos veces**.

---

## BLOQUE 5 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes de
ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla de `site:`** de la 3.1 y **el tope
duro de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta sin
  restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Octava edición consecutiva.
  **No es opcional**: en ARGOS 117 aportó **cuatro de siete hechos, incluido el único rojo**.
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS Y SOBRE SUS EXCLUSIONES.** Ver Bloque 6.

⚠️ **Y REVISE TODA EXCLUSIÓN QUE UN BARRIDO ATRIBUYA A UNA INSTRUCCIÓN SUYA.** **Las prohibiciones de
gasto se redactan contra el PENDIENTE, no contra el TOPÓNIMO.**

⚠️ **Y HAGA EL `grep` DE ARCHIVO SOBRE LO QUE LOS BARRIDOS TRAIGAN, no solo sobre lo que este archivo
enumera.** En ARGOS 117 obligó a escribir **dos deslindes** que el borrador no tenía.

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️ **EL `grep` PRUEBA QUE UN HECHO YA ESTÁ PUBLICADO; SOLO LA BÚSQUEDA POR CIFRAS PRUEBA QUE ES VIEJO — trampa NUEVA de ARGOS 117 y la más peligrosa de la serie** | El candidato **«Michoacán · diez municipios»** (9 detenidos, **10 armas, 459 cartuchos, 18 cargadores**, 3 vehículos) **no estaba en el archivo**, así que el `grep` lo dejaba pasar como `FECHA NO FIJADA` **y se habría heredado indefinidamente**. Una búsqueda de **«459 cartuchos» y «18 cargadores»** devolvió el titular: **cierre del «Plan Michoacán», detenciones del 31-dic-2025** |
| ⚠️ **EL RESUMIDOR REFECHA HECHOS ANTIGUOS — TRES EN UNA SOLA EDICIÓN** | **Tierra Blanca, Veracruz** (108 largas, 50 granadas, 2,700 cargadores, 51,400 cartuchos, 3 lanzagranadas) era del **16-jun** · **Amozoc, Puebla** (11 detenidos, 3 AR-15, 3 Glock) era de **2025** · **«diez municipios»** era de **dic-2025**. **El de Tierra Blanca habría multiplicado el total nacional** |
| ⚠️ **EL RESUMIDOR FABRICA FECHAS, NO SOLO FOLIOS — variante NUEVA** | En **Morelos**, para el **mismo artículo y en dos consultas**, devolvió «25-sep al 7-oct de 2026» —**rango posterior al día del corte**— y «10-abr-2026», con cifras de género distintas. **Se detecta pidiendo la misma fecha dos veces** |
| ⚠️ **El resumidor FABRICA números de comunicado `DPE/…` de la FGR** | **Dieciséis en cuatro cortes.** En ARGOS 117: `DPE/3855`, `3856`, `3857`, `3926`, `3964` (Centro), `DPE/3927` (Noreste), `DPE/3963` (Occidente). **Cadena exacta entre comillas; el negativo VENCE al arbitraje** |
| ⚠️ **UN CONTROL PUEDE OBLIGAR A INTEGRAR Y DECLARAR QUE NO PUEDE FIJAR SU HALLAZGO** | **Tercera vez en la serie.** `procedencia-cifras` detectó que faltaba **la reparación del daño de $26,000 de Durango** y que el borrador **fundía multa y reparación**, y **dijo expresamente que no podía fijarlo**. **El coordinador arbitró y el control tenía razón**, igual que con el falso candidato de Michoacán. **Ni obedecer ni descartar por precaución: arbitrar** |
| ⚠️ **DOS DEFECTOS DE HERRAMIENTA, LOS DOS SILENCIOSOS** | (1) **El clic del mapa de aseguramientos estaba roto y venía roto de antes**: `EVENTOS_ARM` fija `location.hash` con ids **sin ancla en el documento**. **Corregido con `id=` en las filas de la tabla.** (2) **`tools/gen-movil.py` dejaba el mapa de aseguramientos vacío** si el div llevaba **cualquier atributo**: su regex exigía `<div class="panel">` exacto. **Se corrigió la regex, no la salida.** **Ninguna revisión visual habría visto ninguno** |
| ⚠️ **«Más de» no es cifra** | **No se redondea.** En ARGOS 117 dejó fuera **«más de 36,700 cartuchos»** de Acapulco —que **por sí solo habría multiplicado por cien el total nacional**— y «más de 1,500» de Cosío. **Y a veces la cifra exacta SÍ está en titular**: «más de ocho minutos» era **«ocho minutos»** |
| ⚠️ **Multa y reparación del daño son campos distintos y no se suman** | En ARGOS 117 el borrador publicaba una sola tarjeta «Reparación y multa» con **$56,460**, cuando la sentencia impone **multa de $56,460 Y reparación de $26,000** |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | **«Cuauhtémoc» es de COLIMA, de Zacatecas, de Chihuahua y alcaldía de CDMX** · **«San Rafael» es colonia de la alcaldía Cuauhtémoc Y municipio de Veracruz** · «Buenavista», Michoacán, tiene **tres hechos en tres colonias** · «Matamoros» Tamaulipas y Coahuila · «Los Reyes» Michoacán y Edomex |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado diez ediciones. En ARGOS 117: **4-sep viernes, 5-sep sábado, 6-sep domingo, 7-sep lunes**. Sostuvo que Reynosa («sábado por la noche») está EN ventana y que Zinapécuaro («viernes antes de medianoche») está FUERA |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: **fecha la página, no el hecho**, y **no basta como fuente única**. En ARGOS 117 **aportó cuatro pistas y no fechó ninguna**: las cuatro se verificaron con fuente propia, y **una —col. San Rafael— quedó con `FECHA DEL HECHO NO FIJADA`** porque ninguna la fija |
| **Agregado que no se reparte** | Un balance de varios días **no se distribuye** en una ventana. En ARGOS 117 se aplicó a **«Modelo de Seguridad Coahuila»** y a **«Operación Frontera Norte»** |
| ⚠️ **Corroboración asimétrica** | **El nivel de confianza de una fila lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo. En ARGOS 117 bajó Acapulco a **Bajo** por las 12 armas, y Reynosa y CDMX a **★★★☆☆** por identidad y por fecha |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. En ARGOS 117 se declaró en **Buenavista**, cuyas seis regionales reproducen el mismo texto de la SSP |
| **Cargadores y cartuchos** | **Nunca se suman entre sí.** |
| **Un delito y su detención son dos eventos** | En ARGOS 117: Guerrero 🔴 (`ARG-117-001`) y 🟢 (`ARG-117-002`), fichas y ARG-ID distintos. ⚠️ **Y la regla obliga TAMBIÉN EN SENTIDO INVERSO**: ARGOS 116 absorbió **un rescate de dos secuestrados** dentro de su evento rojo de Omealca (`ARG-117-FE-001`) |
| **Sentencia frente a vinculación a proceso** | **Lea el verbo del título** — y compruebe que el título EXISTE. **Prisión preventiva NO es sentencia** (Boletín 2,317 de la FGEO) |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. **Y compruebe la aritmética** |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  **Máximo cinco líneas** en cada **Explotación ARGOS**, en cada recuadro `alerta contexto` y en la
  **Valoración**, numeradas `<b>N. ` **con espacio**. La portada lleva **UN SOLO recuadro**, «LO QUE DEBE
  SABER EL MANDO». **«Hecho confirmado» va en registro telegráfico**, no en prosa.
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes, deslindes
  ni marcas de reserva. Se recorta la prosa, no el dato.** **ARGOS 117 lo cumplió en los 16 bloques.**
- **Solo el día.** Las recuperaciones van con ARG-ID `-REC-`, **ventana de origen declarada** y **fuera
  de todos los totales**. ⚠️ **Y un hecho YA PUBLICADO no vuelve como `-REC-`: eso es duplicación.**
  **Es el criterio que separó, en ARGOS 117, a Zinapécuaro —inédito, lleva ficha— del rescate de Omealca
  —parte de un operativo ya publicado, va solo a fe de erratas—.**
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID
  `-FE-` **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 117 cumplió: nueve `-FE-`
  registrados, cero en el cartelón y cero en la móvil.**
- **Sin «Ejes del día» y sin resumen ejecutivo.** ⚠️ **`editor-duplicidad` señalará que `CLAUDE.md` pide
  «Ejes del día»: la instrucción del destinatario, posterior y más específica, la retiró y fijó «LO QUE
  DEBE SABER EL MANDO». No la reintroduzca.**
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha** con
  enlace `#ARG-ID` y aporta **campos distintos**.
- ⚠️ **No remita a secciones que la edición no tiene.** **No nombre entidades sin ficha ni caso asociado.**
- **Toda cifra en cero lleva al lado el dato que la explica.** Tarjetas de armamento con **doble cifra
  rotulada**; la línea inferior es **cálculo propio** y se declara.
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** ⚠️ **No mida en «ediciones» dentro del cartelón: mida en FECHAS.**
  ARGOS 117 lo verificó con contador automático y quedó en **0**.
- **Conclusiones de inteligencia criminal**, no de método.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.**
- ⚠️ **Cada sentencia integrada lleva ficha propia con sus apartados.** ARGOS 117 integró una.

### Estructura de páginas que hereda ARGOS 118

**Ocho páginas**, como salió ARGOS 117: portada · crimen organizado (I) a (III) · recuperación ·
armamento · sentencias · valoración y conclusiones.
**Si el volumen lo pide, se reparte entre más páginas: nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en TODAS las páginas (8 en ARGOS 117).
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.
#    ⚠️ AL EXTRAER LA PLANTILLA, SON TRES TRAMOS, NO DOS:
#      (a) cabecera hasta la línea anterior a <body>
#      (b) MEXICO_VIEWBOX + MEXICO_PATHS: entre <script> y const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>, SIN las tres últimas
#          líneas (</script></body></html>), que se reponen al ensamblar
#    Compruebe SIEMPRE que haya exactamente un <body> y que MEXICO_PATHS tenga 32 entidades.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 118 <FECHA> 117 2026-09-07 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.** Entre `EVENTOS_ARM` y
`SIZE_R` viven **`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL` y
`GRIS`**.

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes es
«Occidente» en la tabla** aunque un barrido lo cubra desde Noreste. Un `region:` mal puesto **coloca el
eco del radar en el sector equivocado y nadie lo nota**.

⚠️ **CADA ARG-ID DE `EVENTOS` Y DE `EVENTOS_ARM` DEBE TENER UN ANCLA `id=` EN EL DOCUMENTO.** El mapa
fija `location.hash` con ese id: **si no existe el ancla, el clic no lleva a ninguna parte**.
**Venía roto desde antes de ARGOS 117 y nadie lo había visto.** **Las filas de la tabla de armamento
llevan `id="ARG-XXX-ARM-00N"`.**

**Comprobación de coherencia obligatoria** —ARGOS 117 la ejecutó como un solo script de Python y conviene
reutilizarla—: extraer el bloque de datos **desde `const MEXICO_VIEWBOX` hasta `const SIZE_R`**, hacer
`node --check`, y validar que **las siete constantes están presentes**, que **`MEXICO_PATHS` tiene 32
entidades**, que **cada `estado:` existe en `MEXICO_PATHS`**, que **cada `region:` coincide con
`STATE_REGION`**, que **ninguna fecha cae fuera de la ventana**, que **no hay ARG-ID duplicados**, que
**cada ARG-ID de los dos arreglos resuelve a un ancla**, y que **el semáforo derivado de `EVENTOS`
coincide con los contadores tecleados en la portada y en `radar-stats`**.

⚠️ **Y añada el contador automático de la regla de cinco líneas** —`<b>N. ` **con espacio**— y el de
**medidas en «ediciones»**, que debe dar **0**.

⚠️ **Y RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS, no desde el borrador.**

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en ambas
versiones · toda tabla envuelta **exactamente una vez** en el escritorio · **cero `-FE-` en ambas** · cero
`sem-item` fuera de portada · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio en la
móvil (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) · **pie con número, fecha y hora en todas las
páginas del escritorio** · **todos los ARG-ID del escritorio presentes en la móvil** · sin desbordamiento
horizontal a 390 px.

*Notas del generador, que NO son defectos*: la móvil **no lleva `<script>`** · **`table-wrap` aparece en
cero** —el generador lo renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**, de modo que **`<table>` puede aparecer en CERO en la móvil sin que se pierda un solo
dato**. **Verifíquelo contando ARG-ID, no etiquetas `<table>`.** · La móvil lleva **un solo pie**
(`footbar` aparece 3 veces: dos son CSS).

---

## BLOQUE 9 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo, que se remita a tablas inexistentes y que las casillas de cobertura no cuadren con las 32 entidades |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **y que se descarte por precaución una que sí debía integrarse** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **DUODÉCIMA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES DE LOS DOS CONTROLES.** En ARGOS 117
`procedencia-cifras` devolvió `PUBLICAR` condicionado y `editor-duplicidad`, `CORREGIR ANTES DE
PUBLICAR`, **y los dos tenían razón**: el primero **obligó a integrar una reparación del daño omitida** y
**tumbó un falso candidato que se habría heredado indefinidamente**; el segundo **encontró un enlace roto
del mapa que venía de ediciones anteriores** y **tres candidatos sin disposición registrada**.
Si el destinatario no autoriza subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la
ausencia en el indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una búsqueda o
un `grep` de arbitraje antes de obedecerlo**, y **un control puede obligar a INTEGRAR lo que el borrador
descartó por precaución**. ⚠️ **Y cuando el control declare que NO pudo fijar su hallazgo a un titular,
ARBÍTRELO USTED**: en ARGOS 117 el coordinador lo hizo con dos búsquedas propias y **el control tenía
razón las dos veces**.

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil, o vuelva a comprobar la paridad usted mismo.**
En ARGOS 117 el control **no pudo auditar la paridad escritorio↔móvil** porque la móvil aún no existía, y
el coordinador tuvo que comprobarla aparte.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos
**y sobre sus propias instrucciones**.

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS.**
   ⚠️ **Y todo candidato que la edición evalúe recibe DISPOSICIÓN EXPRESA** —cerrado, sin avance o fuera
   de ventana—: en ARGOS 117 `editor-duplicidad` detectó **tres que se habrían perdido sin ella**.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al cartelón
   pero sí al índice. **Y retirar del índice los ARG-ID que se hayan quedado sin usar por una corrección.**
3. **Escribir `reports/_arranque-ARGOS-119.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
