# ORDEN DE ARRANQUE — ARGOS 114

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 113** (corte 2026-09-01).

---

## BLOQUE 0 — VERIFICACIÓN DE BASE · ANTES DE NUMERAR NADA

**El número de edición se deduce del archivo, nunca de lo que la rama local tenga a la vista.**

```bash
TZ=America/Mexico_City date '+%Y-%m-%d %H:%M %Z'   # hora real, se sella en todo el cartelón
git fetch origin                                   # traer el estado real
git log --oneline -1 origin/main                   # ¿main está al día?
git merge --ff-only origin/main                    # ⚠️ ANTES de leer nada más
ls reports/ | grep '^argos-' | tail -6             # ¿cuál es la última edición del archivo?
ls reports/ | wc -l
```

**Estado que debe encontrar ARGOS 114**: última edición `argos-2026-09-01` (ARGOS 113), **84
archivos** en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió:
pare y avísele al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló SIETE ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 113 mostraba **`argos-2026-08-24` (ARGOS 106)** como última
> edición —**siete ediciones por detrás**— y **no contenía su propio archivo de arranque**: numerar
> por lo que la rama tenía a la vista habría producido **un falso «ARGOS 107» con ventana solapada de
> una semana**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y
> resolver.
> **Dato de control**: en ARGOS 113 el estado encontrado tras el merge **coincidió exactamente** con
> el que este bloque anunciaba. **La comprobación funciona; hágala.**

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Edición** | **ARGOS 114** |
| **Ventana** | **desde 2026-09-01 13:17 CDMX** (cierre de ARGOS 113) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-115.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de
solape. **Verifique la hora, no la suponga.**

⚠️ **EFECTO DE DURACIÓN DE VENTANA — hallazgo de ARGOS 113, y es más importante que el de calendario.**
ARGOS 112 cubrió **48 h** y ARGOS 113 **27 h**, y el volumen cayó de **228 armas largas a 5**.
**Ninguna edición es comparable con otra sin normalizar por duración de ventana**, y ARGOS 113 lo
declaró en el cartelón como advertencia de comparabilidad y como conclusión. **Declárelo también si su
ventana es corta.**
⚠️ **Y el efecto de calendario NO explica el cero judicial estatal.** ARGOS 112 lo atribuyó a su
ventana de fin de semana; **ARGOS 113 tuvo dos días hábiles y volvió a dar cero de las 32 fiscalías**.
**La causa es la duración, no el día**: ver Bloque 3.3.

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-01-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.
   ⚠️ **El `grep` debe hacerse por TOPÓNIMO DE LOCALIDAD, no solo por entidad y municipio.** En
   ARGOS 113 devolvió `ARG-102-002` y `ARG-98-005` para «Los Reyes» y obligó a un deslinde que el
   cartelón publica: **tres hechos distintos en el mismo municipio en trece días**. Y advirtió de que
   **«Cuauhtémoc» es municipio de Zacatecas Y alcaldía de CDMX**, y **«Matamoros» existe en Tamaulipas
   y en Coahuila**. **Sexta edición consecutiva en que el archivo resuelve lo que la web no.**

---

## BLOQUE 3 — DEUDA QUE ARGOS 114 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. CUARTA EDICIÓN COMO PASO
DE MAYOR RENDIMIENTO.**

| Origen del hecho | ARGOS 110 | ARGOS 111 | ARGOS 112 | ARGOS 113 |
|---|---|---|---|---|
| Barridos regionales | 2 de 4 | 4 de 6 | 3 de 7 | 4 de 6 |
| **Recall nacional del coordinador** | 2 de 4 | 2 de 6 | **4 de 7** | **2 de 6, incluido el hecho principal** |

En ARGOS 113 el recall trajo **la detención de Piedra Gorda** —hecho principal del corte—, **el
abatimiento de Los Reyes**, **la consolidación del saldo de Ojocaliente** y **la resolución de la
obligación de calendario del Gabinete de Seguridad**. **La razón es estructural: un hecho nacional de
gran cobertura se busca mejor por tema que por entidad, y los barridos están organizados por
entidad.**

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene tres preguntas, el
tope es **de tres en total, no de tres por pregunta**. En ARGOS 113 se respetó en los siete ejes.
**Cerrar un seguimiento en `SIN AVANCE` es el resultado correcto cuando no hay dato.**

⚠️ **EL OBJETIVO PORCENTUAL DE `site:` NO FUNCIONA COMO INDICADOR — TERCERA EDICIÓN IGUAL. CÁMBIELO
POR UNA REGLA.**

| Región | `site:` en ARGOS 113 |
|---|---|
| Golfo | 0 % |
| Noroeste | 5,3 % |
| Noreste · Occidente | 7,1 % |
| Sureste | 13,3 % |
| Centro | 16,7 % |

Bajarlo de 25 % a 15 % **redujo la magnitud pero no la dirección**. **Y el diagnóstico se refina**:
las dos regiones que llegaron al objetivo son **las únicas que tenían dominios con fecha en la ruta
que consultar** (`fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`, `boletines.guanajuato.gob.mx/AAAA/MM/DD/`).
**REGLA QUE SUSTITUYE AL PORCENTAJE: `site:` solo contra dominios con fecha en la ruta; contra los
demás, consulta genérica.** Un porcentaje global obliga a gastar `site:` donde se sabe de antemano que
devolverá *home pages*. **Reparto restante: ~60-65 % genérica sin `site:`, ~10 % judicial.**

### 3.2 Cobertura — qué encabeza el triaje y a quién se le asigna la deuda

**No queda ninguna entidad `NO REVISADA`: el ciclo se aplica limpio, sin prioridad de saldo.**

⚠️ **LA ASIGNACIÓN EXPLÍCITA DE LA DEUDA REGIONAL FUNCIONA — SEIS EDICIONES AL REMANENTE DIERON CERO;
UNA ASIGNÁNDOLA DIO RESULTADO.** En ARGOS 113, **SEDENA/SEMAR/FGR/ANAM → Noreste** produjo el
**hallazgo de Matamoros**, uno de los dos únicos aseguramientos del corte; **Mesas de Construcción de
la Paz → Centro** produjo un **dominio útil nuevo**. **Mantenga la asignación explícita, en rotación:**

- **SEDENA / SEMAR / FGR / ANAM regionales → NOROESTE** (SEMAR en Sinaloa y BC, zonas militares de Chihuahua y Durango).
- **Mesas de Construcción de la Paz → OCCIDENTE.**

**Dominios reutilizables — no los redescubra**: Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/`
(**fecha en la ruta, alto volumen**) · Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`
(**fecha en la ruta**) · Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/` (**fecha en la ruta**) ·
San Luis Potosí `seguridad.slp.gob.mx/noticias/AAAA/M/D/` (**fecha en la ruta**) · **Morelos
`morelos.gob.mx/ultimas-noticias` — NUEVO de ARGOS 113: la única Mesa de Construcción de la Paz del
país con portal propio y desglose numérico publicable** · Michoacán `fiscaliamichoacan.gob.mx` ·
Sinaloa `fiscaliasinaloa.mx` · Chihuahua `fiscalia.chihuahua.gob.mx` y `sspe.chihuahua.gob.mx`
(⚠️ `ssp.chihuahua.gob.mx` es FALSO) · Colima `fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` ·
Edomex `fgjem.edomex.gob.mx` · BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` · Coahuila
`sspcoahuila.gob.mx` · Aguascalientes `aguascalientes.gob.mx/ssp/` · Puebla `ssp.puebla.gob.mx`
(⚠️ *slugs* **sin fecha**) · Tabasco `fiscaliatabasco.gob.mx` (⚠️ **sin fecha en la ruta**).

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** (ambos dominios resuelven, ninguno publica
boletines individuales fechados) · **FGE Veracruz** (cinco cortes de agregados sin individualizar;
**la vía útil en Veracruz es la FGR**) · **`ssypc.nayarit.gob.mx`** (`PORTAL NO DISPONIBLE — índice sin
boletines localizables`; ninguna cifra suya se usa).
**No publican indexable**: FGJ Nuevo León · SSP Zacatecas (sin fecha en la ruta) · Sonora
`fgjsonora.gob.mx` (cuatro ediciones sin resultado, ni confirmado ni descartado).

### 3.3 El ciclo — y por qué un resultado negativo NO es motivo para retirarlo

**A ARGOS 114 le toca el Ciclo A — Noroeste + Centro** encabezando el triaje judicial; las otras
cuatro encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué
aportó.*

⚠️ **ARGOS 113 rompió la racha de tres cortes en que la región que encabeza judicial producía la única
sentencia del corte, y conviene entender por qué antes de sacar la conclusión equivocada.** Occidente y
Sureste encabezaron judicial y **no encontraron sentencia integrable**; la única del país salió de
**Puebla (Centro)**, que encabezaba con armamento.

**La causa no es el orden de triaje: es la duración de la ventana.** ARGOS 112 (48 h, fin de semana):
1 sentencia. ARGOS 113 (**27 h, dos días hábiles**): 1 sentencia y **cero de las 32 fiscalías
estatales**. **Las fiscalías sí publicaron** —Guerrero (tres sentencias con fecha en la ruta),
Querétaro (cinco boletines de agosto), Oaxaca, Durango, Tabasco— **pero ninguna dentro de la ventana**.
**El ciclo de publicación de las fiscalías estatales es más lento que una ventana de 27 horas.**

**Qué hacer con eso**: **el triaje judicial no sirve para garantizar hallazgo; sirve para que el
`SIN DATO` sea demostrable.** Esa función sigue siendo necesaria y **el ciclo no se retira**. Lo que sí
conviene: ⚠️ **dirigir el triaje judicial a las delegaciones de la FGR antes que a las fiscalías
estatales.** **Las dos únicas sentencias integrables de los dos últimos cortes las produjo la
federación** —FGR Papantla en 112, FECOR Puebla en 113—, y la vía de la FGR ya rompió cinco cortes de
agregados inservibles en Veracruz.

### 3.4 Los seguimientos que más rinden

1. ⚠️ **ZACATECAS — HAY UN ARTEFACTO ASEGURADO Y SIN DETONAR, Y UN CUARTO ATAQUE DEL AÑO QUE NO
   ESTABA EN EL REGISTRO.** *Seguimiento de máxima prioridad.* **Son los dos hallazgos principales de
   ARGOS 113.**
   **(a) El artefacto.** En el domicilio de Piedra Gorda se aseguraron **un explosivo artesanal tipo
   niple, una granada de fragmentación, 22 ponchallantas y cinco cargadores abastecidos**
   (`ARG-113-ARM-003`). **Los tres artefactos anteriores de la serie fueron EMPLEADOS y no dejaron
   material íntegro que peritar; este está en poder de la autoridad.** ⚠️ **Precedente en contra**: en
   el sur de Sinaloa se destruyeron **in situ** 49 y luego 6 artefactos «por riesgo de traslado», sin
   caracterizar ninguno. **Qué buscar: si se peritó o se destruyó.**
   **(b) El cuarto ataque.** La autoridad documenta **cuatro ataques con explosivos contra policías en
   2026** —**Villa García, Tabasco, Luis Moya y Ojocaliente**—. **Tres son los publicados; Luis Moya no
   está en el archivo y no tiene fecha.** **Qué buscar: fechar Luis Moya.**
   ⚠️ **Y NO vuelva a fundir dos listas de emisores distintos.** Por separado, la FGJEZ mantiene
   **carpetas abiertas en siete municipios** —Valparaíso, Fresnillo, Villanueva, Jerez, Ojocaliente,
   Luis Moya y Villa Hidalgo— **por agresiones a elementos policiacos**, categoría más amplia que la
   de explosivos. **Unir ambas listas es síntesis propia y debe declararse como tal**: ARGOS 113
   estuvo a punto de publicar «nueve municipios» como si un solo emisor lo hubiera dicho, y lo detectó
   `procedencia-cifras`. **Tres búsquedas máximo, en total.**
2. ⚠️ **Los DOS detenidos de la serie, y ninguno con vinculación a proceso publicada.**
   `ARG-112-003` (**William Ariel «N», 18 años**, Villa García, capturado el **30-ago en Asientos,
   Aguascalientes**) y `ARG-113-001` (**Juan Pedro «N», 29 años**, Ojocaliente, capturado el **1-sep en
   Piedra Gorda, Cuauhtémoc, Zacatecas**). ⚠️ **SON DOS DETENCIONES DISTINTAS Y DOS BARRIDOS LAS
   FUSIONARON EN ARGOS 113 — no repita el error.** ⚠️ **RESERVA VIVA**: una fuente regional describe al
   segundo como **«segundo implicado» y también originario de Aguascalientes**. **Si se confirma, los
   dos operadores de la serie proceden de la misma entidad, que no es donde ocurrieron los ataques.**
   **Sin corroboración nacional ni institucional, no se integra.**
   **Qué buscar**: **situación jurídica de ambos** y si se publicó **explotación técnica del
   accionador** de Villa García, que sigue siendo **la única pieza capaz de identificar al operador sin
   testigo**. **Dos búsquedas.**
3. ⚠️ **BAJA CALIFORNIA — Tijuana, desaparición de Emilio Valdez Mainero. EL CANDIDATO PRIORITARIO.**
   Presunto exoperador del Cártel Arellano Félix. Publicación con **fecha en la ruta del 1-sep**,
   dentro de la ventana de ARGOS 113, pero **solo se localizó el titular**, sin cuerpo de nota.
   **No se descartó por fecha, sino por falta de verificación.** **Dos búsquedas.**
4. **MICHOACÁN — Los Reyes: segunda descabezada en un mes, y la ventana de repunte es ahora.**
   Detención del jefe el **1-ago**, operativo del **31-ago** (`ARG-113-REC-001`); **tres eventos en el
   municipio en trece días**. **Abatimiento de «El Wicho»/«R5» no confirmado institucionalmente.**
   **Qué buscar**: **el parte oficial de la SEDENA** con resultados y armamento, y **señales de disputa
   por la sucesión**. **Dos búsquedas.**
5. **DURANGO o SINALOA — «16 detenidos y 22 armas».** `ENTIDAD NO DETERMINADA`: la misma cifra
   atribuida a dos entidades distintas, ambas fechadas el 31-ago. **Se resuelve con `site:` a las dos
   SSP estatales** —y ambas cumplen la regla nueva solo parcialmente, así que no gaste más de **una
   búsqueda**.
6. **TAMAULIPAS — las cuatro armas largas de Matamoros** (`ARG-113-002`). **Serie y marcaje**, para
   cotejo con las **210 armas de Texas** interceptadas **el mismo día a menos de 300 km**. **Una
   búsqueda.**
7. ⚠️ **NO gaste NINGUNA búsqueda en**: **la protección balística** —**retirada de la lista de
   búsqueda en ARGOS 113** tras tres cortes con resultado idéntico en las seis regiones; es
   **conclusión permanente**, no seguimiento— · **Bocoyna/Maguarichi** (cerrado como duplicidad) ·
   **Guanajuato · San Miguel de Allende** (cerrado, es del 25-ago) · **Poza Rica** (`SIN AVANCE` por
   tercera vez) · **Pedernales** · **Tlaxcala** y **FGE Veracruz** (vacíos acreditados) · la disputa
   forestal Michoacán/Guerrero · «El Dron» · Querétaro `ARG-109-005` · Petatlán y Totolapan.
8. **Una sola búsqueda, y solo si sobra**: Loxicha (`ARG-109-002`), Chihuahua `ARG-111-004`,
   la contradicción de lesionados de `ARG-110-001` (**cuarta edición sin arbitrar**), el municipio de
   Agua Verde (`ARG-112-005`), la munición sin su arma de Acapulco (`ARG-112-006`).

### 3.5 La obligación de calendario, ya vencida y resuelta

**`gabinetedeseguridad.gob.mx/resultados/` pasa de «obligación de calendario» a «vacío recurrente por
verificar cada corte».** ARGOS 113 acreditó que **la migración ocurrió**: desde el 1-sep los reportes
diarios de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí, para las 32 entidades.
**Lo que no se alcanzó fue ningún reporte diario.** El dominio **está indexado** pero **sus rutas no
llevan fecha**, y tiene una **trampa de año documentada** (devolvió un boletín de octubre de 2025 a una
consulta de agosto de 2026). **Verifíquelo cada corte, declare el resultado y no use ninguna cifra
suya** mientras persista.

---

## BLOQUE 4 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes
de ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla nueva de `site:`** de la 3.1 y
**el tope duro de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta
  sin restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Cuarta edición consecutiva
  como paso de mayor rendimiento. **No es opcional.**
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS — control NUEVO de ARGOS 113, y salvó la edición.**
  Ver Bloque 5.

---

## BLOQUE 5 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| ⚠️ **DOS BARRIDOS CONVERGEN EN EL MISMO ERROR CUANDO EL HECHO CRUZA LA FRONTERA ENTRE SUS REGIONES — modo de fallo NUEVO de ARGOS 113, y el más importante de este arranque** | **No lo detectó ningún control: lo detectó el coordinador contrastando dos barridos entre sí.** El Noreste presentó la captura de **Piedra Gorda (Zacatecas)** como la de **William Ariel «N»** por el ataque de **Villa García**; Occidente informó que ese hombre fue capturado **el 30-ago en Asientos, Aguascalientes**. **Son dos detenciones distintas**: dos fechas, dos entidades, dos hechos. **De haberse aceptado la fusión, ARGOS 113 se habría quedado sin hecho principal.** **REGLA: cuando dos regiones informen del mismo nombre propio, el coordinador arbitra con búsqueda propia antes de integrar, aunque las dos versiones parezcan compatibles** |
| ⚠️ **RECTIFICACIÓN EN CADENA DE LA AUTORIDAD** | El saldo de Ojocaliente se rectificó **tres veces**: 7 (30-ago) → 10 (31-ago) → **11 (1-sep)**, y en la tercera **apareció un campo nuevo, ~40 viviendas afectadas**, que las anteriores no tenían. **Regla, ya confirmada dos ediciones seguidas: cuando acepte una rectificación de la autoridad en un campo, revise si hay rectificaciones posteriores en los demás campos del mismo hecho** |
| ⚠️ **Ni obedecer ni descartar por precaución: ARBITRAR** | **En ARGOS 113 el arbitraje rindió DOS VECES.** (a) Hizo **integrable la sentencia de Puebla**, que un control marcaba `PENDIENTE DE CONFIRMACIÓN OFICIAL — NO INTEGRAR`: una búsqueda encontró el **comunicado 585/26 de la FGR** y **cuatro campos individualizadores**. (b) ⚠️ **Y cambió el conteo del corte**: `procedencia-cifras` marcó `NO INTEGRAR` la identidad del detenido de Piedra Gorda **y señaló de paso un armamento asegurado que el borrador no recogía**. Una búsqueda de arbitraje encontró **el boletín institucional de la SSP Zacatecas y la identificación en una fuente nacional**, e integró **un AEI, una granada de fragmentación, 22 ponchallantas y cinco cargadores** — **el primer artefacto ASEGURADO de toda la serie**. **Lo que ningún control puede hacer es la búsqueda que resuelve: eso es del coordinador** |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | **`grep` del topónimo de localidad, no solo de municipio.** En ARGOS 113 devolvió `ARG-102-002` y `ARG-98-005` para «Los Reyes». **«Cuauhtémoc» es municipio de Zacatecas Y alcaldía de CDMX; «Matamoros» está en Tamaulipas Y en Coahuila; «Los Reyes» en Michoacán Y en Edomex (Los Reyes La Paz)** |
| ⚠️ **Trampa de fecha por municipio repetido dentro de la MISMA entidad** | El arsenal de **Matamoros de junio de 2026** (Barrett .50, 32 fusiles, lanzallamas) y el hallazgo del **31-ago** son **el mismo municipio, la misma región militar y el mismo tipo de operativo**: el buscador los devuelve juntos. **Es la razón de que la tarjeta de armamento especial de ARGOS 113 esté en cero** |
| ⚠️ **Una cifra que «no está publicada» puede estarlo, y en el boletín oficial** | ARGOS 113 escribió «no se publicó tipo, calibre ni marca» del arma de Pénjamo cuando **el boletín oficial de Guanajuato, con fecha en la ruta, publicaba el calibre (7.62×39) y la identidad del detenido** — y el medio regional **ya citado en la propia ficha** también. **Antes de declarar un vacío de campo, compruebe el boletín del emisor**: el vacío era del borrador, no de la fuente |
| ⚠️ **Cuatro cifras de balance del mismo día, dos de ellas incompatibles** | Zacatecas publicó **17 en dos años**, **10 en 2026**, **7 contra policías en 2026** y **«el 4.º del año contra cuerpos policiacos»**, todas el 1-sep. **Comparar solo dos y declarar que «no se contradicen» es un error**: hay que revisar cuántas cifras del mismo universo circulan antes de afirmarlo |
| ⚠️ **Pena compuesta** | «50 años … **para ambos**» **no es sumable**: no se publica si es por persona o conjunta. `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA`, **años acumulados: no determinado**. Mismo supuesto que la pena de Sonora |
| ⚠️ **Dos casos de la misma fiscalía, el mismo día, con la misma pena** | La FECOR Puebla publicó **dos condenas de 50 años el 31-ago**: una con **dos sentenciados y embutidos**, otra con **uno y licor**. **Municipio, delito y pena coincidentes NO identifican un caso**: hacen falta **dos campos individualizadores**. Es la lección de Coronango, otra vez |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado seis ediciones. En ARGOS 113 confirmó «madrugada del lunes 31» para Los Reyes, **que es lo que lo sitúa antes de la apertura de la ventana** y lo convierte en recuperación en vez de hecho del corte |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: fecha la página, no el hecho, y **no basta como fuente única**. En ARGOS 113 descartó el narcolaboratorio de Santa María del Río |
| **Falso positivo del resumidor** | Querétaro, boletín 08/04: el resumidor **inventó nombre, alias y terminología jurídica**; el titular real era «concluye proceso penal por hecho de tránsito» con **acuerdos reparatorios**, no condena. **Contraste siempre contra el titular real** |
| **Capacidad declarada** | «cargadores de 20 cartuchos cada uno» **no** se convierte en cartuchos |
| **Cifra no exacta** | «más de», «alrededor de» **no es cifra** y no se redondea. **Pero busque la exacta** |
| ⚠️ **El AEI empleado no es AEI asegurado** | Los tres de la serie de Zacatecas **fueron usados contra la autoridad**: van al semáforo, **no al conteo de armamento** |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. **Pero si la suma la publica la fuente, es de ella** |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. En ARGOS 113 se declaró en **cuatro fichas de cinco** |
| **Trampa de año en el propio dominio oficial** | `gabinetedeseguridad.gob.mx` devolvió un boletín de **octubre de 2025** a una consulta de agosto de 2026 |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria** |

**Egreso bloqueado, vigesimoquinta edición.** `curl` no obtiene respuesta de `*.gob.mx`; `WebFetch`
devuelve `EGRESS_BLOCKED`, también para dominios de medios. **Cero portales por acceso directo.**
Techo de confianza: **★★★★☆**. `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
**Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige
lectura directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las casillas deben CUADRAR con las 32 entidades.** ARGOS 113 cuadró: **8 con hallazgo + 23 sin
resultado indexado + 1 vacío acreditado (Tlaxcala) + 0 no revisadas = 32**.

---

## BLOQUE 6 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con
  ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de todos los totales** — incluido el
  semáforo, el radar y el mapa. **ARGOS 113 lo aplicó**: `ARG-113-REC-001` **no figura en el arreglo
  `EVENTOS`** y el cartelón lo declara expresamente.
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID
  `-FE-` **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 113 cumplió**: seis
  `-FE-` registrados, ninguno en el cartelón, verificado por control automático.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha**
  con enlace `#ARG-ID` y aporta **campos distintos**.
- ⚠️ **La regla de no duplicación alcanza también a los PÁRRAFOS.** La Valoración **remite** a la
  portada y se limita a aplicar la metodología de riesgo; no repite la narración.
- **Toda cifra en cero lleva al lado el dato que la explica.** Tarjetas de armamento con **doble
  cifra rotulada** y **leyenda encima del bloque**; la línea inferior es **cálculo propio** y se
  declara. **ARGOS 113 usó cuatro recuadros**: por qué el rojo está en cero (**no hubo cuarto ataque**),
  por qué el amarillo está en cero, **las 31 placas balísticas sin marca ni nivel**, y **las 32
  fiscalías con cero sentencias pese a ser días hábiles**. **Ese es el modelo.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.** En ARGOS 113 **cuatro de las
  nueve tarjetas** están en cero y **las cuatro llevan su explicación**.
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura van al archivo de fuentes.
  **No mida en «ediciones» dentro del cartelón**: mida en fechas. Las únicas excepciones son de
  trazabilidad: **la declaración de ventana** y **la ventana de origen de cada `-REC-`**.
- **Conclusiones de inteligencia criminal**, no de método. **ARGOS 113 publicó diez**, todas
  accionables y ninguna sobre el instrumento.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.** Use `<div class="alerta contexto">…`.
- **Los `id` de las fichas** solo deben tener forma de ARG-ID si son un ARG-ID real.
- ⚠️ **Cada sentencia integrada lleva ficha propia con sus apartados** —hecho procesal, pena y
  estatus, corroboración, explotación—, no solo un renglón de tabla.

### Estructura de páginas que hereda ARGOS 114

**Seis páginas**, como salió ARGOS 113: portada · crimen organizado (I) · crimen organizado (II),
acciones institucionales · armamento · sentencias · valoración y conclusiones.
Si el volumen lo pide, **se reparte entre más páginas: nunca se comprime una tarjeta**.

---

## BLOQUE 7 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en las SEIS páginas.
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 114 <FECHA> 113 2026-09-01 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.** Entre `EVENTOS_ARM` y
`SIZE_R` viven **`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL`
y `GRIS`**. ARGOS 112 los dejó fuera y **el cartelón habría cargado con el radar y el mapa rotos, sin
que la vista lo detectara**. **ARGOS 113 cortó bien y lo verificó con un control automático que
comprueba que las siete constantes están presentes.** Repítalo.

**Comprobación de coherencia obligatoria** —ARGOS 113 la ejecutó como un solo script de Python y
conviene reutilizarla—: extraer el bloque de datos del `<script>` **hasta `const SIZE_R`**, hacer
`node --check`, y validar que **las siete constantes de arriba están presentes**, que **cada `estado:`
existe en `MEXICO_PATHS`**, que **cada `region:` coincide con `STATE_REGION`**, que **ninguna fecha
cae fuera de la ventana**, que **no hay ARG-ID duplicados** y que **el semáforo derivado de `EVENTOS`
coincide con los contadores tecleados en la portada y en `radar-stats`**. Un `region:` mal puesto
**coloca el eco del radar en el sector equivocado y nadie lo nota**.

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en
ambas versiones · toda tabla envuelta **exactamente una vez** en el escritorio · **cero `-FE-` en
ambas** · cero `sem-item` fuera de portada · cero tarjetas `.reg` sin texto · cero restos de clases de
escritorio en la móvil (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) · **pie con número,
fecha y hora en las seis páginas** · sin desbordamiento horizontal a 390 px.

*Nota*: la móvil **no lleva `<script>`** y **`table-wrap` aparece en cero** al contarlo — el generador
los renombra a `tabla-scroll`. **No es un defecto.**

---

## BLOQUE 8 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo y que las casillas de cobertura no cuadren con las 32 entidades |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, y que se descarte por precaución una que sí debía integrarse |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

**Octava edición consecutiva con hallazgos reales de los dos controles.** Si el destinatario no
autoriza subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la ausencia en el
indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una
búsqueda de arbitraje antes de obedecerlo** —en ARGOS 113 ese arbitraje **hizo integrable la única
sentencia del corte**—, y **un control puede obligar a INTEGRAR lo que el borrador descartó por
precaución** —ARGOS 112, la cifra de lesionados de Ojocaliente—. **Ni obedecer ni descartar por
precaución: arbitrar.**

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador entre barridos.**
Ver Bloque 5. **En ARGOS 113 fue el que salvó la edición, y ningún subagente lo habría hecho**, porque
cada barrido solo ve su propia región.

---

## BLOQUE 9 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al
   cartelón pero sí al índice.
3. **Escribir `reports/_arranque-ARGOS-115.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
