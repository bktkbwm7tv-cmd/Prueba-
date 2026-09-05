# ORDEN DE ARRANQUE — ARGOS 117

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte,
sino en el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 116** (corte 2026-09-05).

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

**Estado que debe encontrar ARGOS 117**: última edición `argos-2026-09-05` (ARGOS 116), **93 archivos**
en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló DIEZ ediciones seguidas y volverá a fallar.** La rama que el entorno asigna
> **llega desactualizada**. En ARGOS 116 mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición
> —**diez ediciones por detrás**— y **no contenía su propio archivo de arranque**: numerar por lo que la
> rama tenía a la vista habría producido **un falso «ARGOS 107» con ventana solapada de once días**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Edición** | **ARGOS 117** |
| **Ventana** | **desde 2026-09-05 09:46 CDMX** (cierre de ARGOS 116) **hasta la hora verificada de arranque** |
| **Archivos a producir** | `reports/argos-<FECHA>.html` · `-movil.html` · `-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-118.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de solape.
**Verifique la hora, no la suponga.**

⚠️ **La serie sigue sin ventanas estables**: 21 → 47 → **25 h**. ARGOS 116 duró **24 h 37 min**, la mitad
que la anterior, y produjo **5 hechos frente a 7**: **más densidad por hora, no menos**.
**Ninguna edición es comparable con otra sin normalizar por duración**, y así se declaró en portada y
Valoración. **Conviene sostener horas de arranque estables para que la serie recupere comparabilidad.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-05-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO TRAIGA, INMEDIATAMENTE
   ANTES DE FICHAR — NO SOLO SOBRE LOS QUE ESTE ARCHIVO ENUMERA.** En ARGOS 116 **funcionó dos veces**,
   y las dos con topónimos que **ningún archivo de arranque enumeraba** porque los trajeron los barridos:
   - **Tihuatlán** (Golfo lo propuso como «candidato vivo para ARGOS 117») **era `ARG-102-REC-004`**,
     con **51,910 L y 95 cartuchos idénticos**. **El resumidor lo había refechado al 4-sep.**
   - **San Bernardino Tlaxcalancingo** (lo trajo Centro) **era `ARG-109-004`**, ya publicado **y ya
     clasificado 🟡** — y venía arrastrándose **dos ediciones** como candidato abierto.

   ⚠️⚠️ **Y LA LECCIÓN NUEVA, QUE ES LA MÁS IMPORTANTE DE ESTE ARRANQUE:
   UN CANDIDATO DESCRITO POR SU TITULAR ES IRRECONOCIBLE CONTRA EL ARCHIVO.**
   El candidato de Puebla sobrevivió dos ediciones **porque el traspaso lo llamaba «operativo con dos
   detenidos y un agresor abatido», sin municipio ni alias**. **REGLA: todo candidato que pase a
   `_pendientes.md` lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS. Nunca solo el titular.**
   **Ya se aplicó a la lista de candidatos vivos de ARGOS 117: consérvela así.**

   ⚠️ **Y el `grep` debe ser por TOPÓNIMO DE LOCALIDAD, no solo por entidad y municipio.**
   «Cuauhtémoc» es municipio de Zacatecas, de Chihuahua Y alcaldía de CDMX · «Matamoros» está en
   Tamaulipas Y Coahuila · «Los Reyes» en Michoacán Y Edomex · «Rosario»/«El Rosario» en Sinaloa ·
   «Villa de La Paz» es de San Luis Potosí, **no de Guerrero** · «San Isidro» es colonia de Ciudad
   Juárez **y** «Parajes de San Isidro» es otro lugar de la misma ciudad con otro hecho.

   ⚠️ **Cuando un candidato no tenga fecha en ruta ni en titular, `grep` por sus CIFRAS DISTINTIVAS.**
   Es más barato y más concluyente que buscar la fecha: así cayó Tihuatlán, por «51,910» y «95».

---

## BLOQUE 3 — DEUDA QUE ARGOS 117 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. SÉPTIMA EDICIÓN COMO PASO
OBLIGATORIO.**

| Origen del hecho | ARGOS 113 | ARGOS 114 | ARGOS 115 | **ARGOS 116** |
|---|---|---|---|---|
| Barridos regionales | 4 de 6 | 3 de 8 | 6 de 7 | **4 de 6** |
| Recall y arbitraje del coordinador | 2 de 6 | 5 de 8 | 1 de 7 | **2 de 6** |

⚠️ **La proporción no dice lo importante: el recall aportó LOS DOS HECHOS DE MAYOR GRAVEDAD y ningún
barrido vio ninguno de los dos.** **Omealca** —el único rojo, apertura del cartelón— y **Tepuche**
—la recuperación—. **Ningún barrido vio Tepuche en ningún momento, ni siquiera Noroeste, que cubre
Sinaloa.** **La causa es estructural: un hecho nacional de gran cobertura se busca mejor por tema que
por entidad, y los barridos están organizados por entidad. NO LO RETIRE.**

⚠️ **EL ARBITRAJE DEL COORDINADOR FUE DECISIVO Y ACERTÓ EN TODAS SUS DIRECCIONES.** Ver Bloque 6.
Rechazó por segunda vez una fusión que traían las fuentes, detectó los dos candidatos ya publicados,
**confirmó los dos hallazgos del control que tumbaban su propio borrador**, y encontró el antecedente
que hacía legible el cateo de Coatzacoalcos. **Ni obedecer ni descartar por precaución: arbitrar — y
aceptar el resultado.**

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene dos preguntas, el tope
es **de dos en total, no de dos por pregunta**. En ARGOS 116 se respetó en los seis ejes.
**Cerrar un seguimiento en `SIN AVANCE` es el resultado correcto cuando no hay dato.**

✅ **LA REGLA DE `site:` FUNCIONA. EL OBJETIVO PORCENTUAL SIGUE RETIRADO — NO LO REINTRODUZCA.**

> **`site:` SOLO contra dominios con fecha en la ruta; contra los demás, consulta genérica.**

**Dominios con fecha en la ruta — no los redescubra**: Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/` ·
Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` (**publicó el 3-sep, un día antes de la
ventana de ARGOS 116: sigue siendo el portal estatal más fiable**) ·
Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/` · San Luis Potosí `seguridad.slp.gob.mx/noticias/AAAA/M/D/` ·
Veracruz `veracruz.gob.mx/AAAA/MM/DD/` (**la vía de Veracruz, no la FGE**) ·
Guerrero `fiscaliaguerrero.gob.mx/index.php/AAAA/MM/DD/` (**encargo CERRADO con negativo verificable:
lo más reciente indexado es `/2026/07/17/`. NO repetir sin criterio nuevo**).

✅ **DOMINIOS RESUELTOS EN ARGOS 116, tras tres ediciones de deuda — no los vuelva a buscar:**
- **Puebla**: **`fiscalia.puebla.gob.mx`** (boletines en `/index.php/informacion-socialmente-util/boletines`).
  ⚠️ **`fiscaliapuebla.gob.mx` y `fgepuebla.gob.mx` NO EXISTEN**: el dominio **no fusiona las palabras**.
- ⚠️ **Hidalgo**: **NO EXISTE una «Fiscalía General del Estado de Hidalgo».** Es la **Procuraduría
  General de Justicia del Estado de Hidalgo**, **`procuraduria.hidalgo.gob.mx`**.
  ⚠️ **`@FGR_Hgo` es la delegación estatal de la FGR federal, NO la fiscalía estatal.** No las confunda.
- ✅ **`fge.yucatan.gob.mx` — HALLAZGO NUEVO**: publica con *slugs* «sentenciados a prisión en juicio
  abreviado» y «fallo condenatorio en procedimiento abreviado». **Formato utilizable.**
  **Asígnele consulta dedicada en el próximo Ciclo C.**

**Sin fecha en la ruta (use genérica)**: Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa `fiscaliasinaloa.mx`
y `sspsinaloa.gob.mx` · Chihuahua `fiscalia.chihuahua.gob.mx` y `sspe.chihuahua.gob.mx`
(⚠️ `ssp.chihuahua.gob.mx` es FALSO) · Colima `fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` ·
Edomex `fgjem.edomex.gob.mx` · BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` ·
Coahuila `sspcoahuila.gob.mx` · Tamaulipas `tamaulipas.gob.mx/seguridadpublica/` ·
Tabasco `fiscaliatabasco.gob.mx` y `tabasco.gob.mx/seguridad` · Aguascalientes `aguascalientes.gob.mx/ssp/` ·
Puebla SSP `ssp.puebla.gob.mx` · Morelos `morelos.gob.mx/ultimas-noticias`
(⚠️ **trampa de año verificada**) · Veracruz, Mesa de Paz: `cespver.gob.mx` y
`veracruz.gob.mx/seguridad/mesa-de-coordinacion-para-la-construccion-de-la-paz/`.

⚠️ **`fiscalia.chihuahua.gob.mx` NO lleva fecha en el slug**: un cateo de **junio** entró como candidato
de septiembre en ARGOS 115 y solo se descartó por cuatro URL de republicadores con fecha.
**Exija siempre ancla de republicador fechado para esta fiscalía.**

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** · **FGE Veracruz** (siete cortes de agregados
sin individualizar; **la vía útil en Veracruz es la FGR y `veracruz.gob.mx`**) · **`ssypc.nayarit.gob.mx`** ·
**`fgjsonora.gob.mx`** (vacío acreditado de portal; **Sonora sigue revisada por vía genérica**).
**No publican indexable**: FGJ Nuevo León · SSP Zacatecas.

### 3.2 Cobertura — qué encabeza el triaje y a quién se le asigna la deuda

✅ **NO QUEDA NINGUNA ENTIDAD `NO REVISADA` EN NINGUNO DE LOS DOS CUADRES.** ARGOS 116 saldó la
**Fiscalía de Tabasco**, que era la única del cuadre judicial, consultándola en cinco formas distintas.
**Cuadres: nacional 3 + 29 + 0 + 0 = 32 · judicial 0 + 32 + 0 + 0 = 32.**

**A ARGOS 117 le toca el CICLO A — Noroeste + Centro** encabezando el triaje judicial; las otras
cuatro encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

⚠️ **DIRIJA EL TRIAJE JUDICIAL A LAS DELEGACIONES DE LA FGR ANTES QUE A LAS FISCALÍAS ESTATALES.
FUNCIONA, Y ARGOS 116 LO DEMOSTRÓ.** El Ciclo C produjo **cinco candidatos con término literal de
condena**, cuando las cinco ediciones previas no habían producido ninguno localizable.
**Ninguno se integró, pero por FECHA y UMBRAL, no por ausencia de publicación.**
**La causa del cero dejó de ser «no publican» y pasó a ser demostrada**: con ventanas de ~25 h la
probabilidad de que una fiscalía publique sentencia en esa franja es estructuralmente baja.

⚠️ **DEUDA REGIONAL — dos encargos se CIERRAN y quedan dos:**
- ✅ **SEDENA / SEMAR / FGR / ANAM regionales — CERRADO.** **Negativo declarado en Noreste (ARGOS 116) y
  en Centro (ARGOS 115)**: estas corporaciones **solo aparecen integradas en operativos conjuntos**, sin
  comunicado propio fechado en ventana. **Dos regiones con el mismo resultado: no lo repita.**
- ✅ **Mesas de Construcción de la Paz — CERRADO salvo Sonora.** **Chihuahua, Sinaloa, Durango, BC y BCS
  tienen mesa y NINGUNA tiene portal propio**: publican dentro del portal estatal. Veracruz **sí** tiene;
  Tabasco **no**. **Queda solo Sonora**, con negativo no concluyente.
- **ANAM / Aduanas → asígnela a NOROESTE.** Quedó `NO REVISADA` en ARGOS 116 por presupuesto.
- **`fge.yucatan.gob.mx` → asígnelo a SURESTE** en el próximo Ciclo C.

### 3.3 Los seguimientos que más rinden

1. ⚠️ **VERACRUZ — EL ATAQUE LETAL CONTRA PERSONAL FEDERAL DE INVESTIGACIÓN.** *Máxima prioridad, y es
   nuevo.* **Dos búsquedas.**
   `ARG-116-001`: **2 agentes de la SSPC muertos y 1 lesionada** en **Omealca**, entre **Río Moreno y
   Paso Amapa**, la noche del 4-sep a la madrugada del 5-sep, **mientras realizaban labores de
   investigación**. **Sin detenidos al cierre.** **Armamento de los agresores no publicado.**
   Qué buscar: **detenciones posteriores y resultado del despliegue** · **qué carpeta trabajaban los
   agentes** · **casquillos y calibres del sitio**.
   **Por qué importa**: **cambia el perfil de víctima** —hasta este corte los blancos institucionales
   eran policías municipales y estatales— y **el despliegue de respuesta alcanza a Oaxaca**, lo que
   sitúa a la estructura **a caballo del límite estatal**.
2. ⚠️ **SINALOA — LA VIOLENCIA CONTRA EL CARGO EN TEPUCHE.** **Dos búsquedas.**
   `ARG-116-REC-001`: **dos titulares de la MISMA sindicatura asesinados en cinco meses** —David
   Guadalupe Ramírez González (4-sep) y su antecesor Héctor Bartolo Zamudio Ríos (31-mar)—, y **la
   sindicatura quedó desierta en su relevo por falta de aspirantes**.
   Qué buscar: **detenciones o línea de investigación** · **si se designa nuevo síndico y en qué
   condiciones** · **si hay más funcionarios menores amenazados en el norte de Culiacán**.
   ⚠️ **RECUERDE: este hecho es de la ventana de ARGOS 115 y está FUERA de todos los totales de 116.
   Si aparece algo nuevo, es hecho NUEVO de la ventana de 117, no una ampliación del `-REC-`.**
3. ⚠️ **VERACRUZ — ¿SERIE DE NEGOCIOS RAFAGUEADOS EN COATZACOALCOS?** **Una búsqueda.**
   `ARG-116-004`: los 15 detenidos se vinculan al **ataque a balazos contra el bar «La Ventanita»**
   del **31-ago hacia las 19:00** —col. Bahía de San Martín, ~6 impactos, **sin lesionados**—, y las
   fuentes registran **otros negocios rafagueados en la ciudad este año**.
   **Rafaguear una fachada sin víctimas es cobro de piso o advertencia, no disputa territorial.**
   Qué buscar: **inventario de negocios rafagueados en Coatzacoalcos en 2026**.
   ⚠️ **El ataque del 31-ago es de una ventana anterior y NO está en el archivo: NO se recuenta.**
4. ⚠️ **ZACATECAS — LA FENAZA, HASTA EL 20 DE SEPTIEMBRE.** **Dos búsquedas.**
   **La ventana de ARGOS 117 vuelve a caer dentro.** **El dispositivo de 787 elementos ya está
   publicado (`ARG-115-001`) y NO se recuenta.** Lo que se vigila es **el resultado**.
   **ARGOS 116 cerró su primera jornada SIN incidente, amenaza, detención ni artefacto** en el recinto
   o su perímetro. **El indicador sigue siendo si aparece artefacto en zona de concentración masiva**,
   que sería el salto de medio que la serie no ha dado. **Es el seguimiento más perecedero del archivo.**
5. ⚠️ **CHIHUAHUA — LAS TRES ARMAS LARGAS CON CALIBRE.** **Una búsqueda.**
   `ARG-116-ARM-001`: **2 fusiles Palmetto (cal. .223 y cal. 5.56) y una tercera larga cal. .223**, con
   cortas Kimber, Taurus, Stoeger y Smith & Wesson, en Ciudad Juárez.
   ⚠️ **Marcas y calibres están REPORTADOS pero NO FIJADOS EN TITULAR**: **fijarlos a un boletín o
   titular es la búsqueda**, porque **rompen tres cortes de predominio del 7.62×39** y **abren cotejo
   con las 210 armas procedentes de Texas** (`ARG-112-004`), donde ya constan AR-15 cal. .223.
6. **CHIHUAHUA — el AEI de Villas del Real** (`ARG-115-003`). **Una búsqueda, y solo si sobra.**
   `SIN AVANCE` en las dos preguntas de ARGOS 116: ni **peritaje** —consta que **SEDENA se hizo cargo
   del explosivo**, sin más detalle— ni **auditoría del inventario de uniformes de la DSPM**.
   **Siguen habiendo DOS piezas explosivas íntegras en el archivo y NINGUNA caracterizada**, con el
   niple de Piedra Gorda. **Cifra en disputa (13/23/36 cartuchos cal. .45): `NO SE ARBITRA`.**
7. ⚠️ **NO gaste NINGUNA búsqueda en**: **protección balística** (conclusión permanente) ·
   **el municipio administrativo de Agua Verde** (cerrado: es Rosario) · **«16 detenidos y 22 armas»**
   (cerrado) · **Tabasco «26 detenidos»** (cerrado: junio) · **Coatzacoalcos–Villahermosa** (cerrado:
   Huimanguillo, 81 kg) · **Tihuatlán** (cerrado: es `ARG-102-REC-004`) · **San Bernardino
   Tlaxcalancingo / «El Dron»** (cerrado: es `ARG-109-004`, 🟡) · **Bocoyna/Maguarichi** ·
   **San Miguel de Allende** · **Poza Rica** · **Pedernales** · **Tlaxcala** y **FGE Veracruz** ·
   disputa forestal Michoacán/Guerrero · **Petatlán y Totolapan** · **Loxicha** ·
   **Matamoros serie y marcaje** · **el accionador de Villa García** (vacío acreditado) ·
   **el origen aguascalentense de los dos detenidos** (resuelto) · **«El Niño Concepción» y la serie de
   explosivos** (cerrado con negativo declarado en ARGOS 116) · **las tres sentencias de la FGR Sinaloa**
   (retiradas por umbral) · **`fiscaliaguerrero.gob.mx`** · **`fgjsonora.gob.mx`**.
   ⚠️ **PERO RECUERDE LA REGLA: estas prohibiciones van contra el PENDIENTE, no contra el TOPÓNIMO.
   Si aparece un hecho NUEVO, en ventana, en cualquiera de esos lugares, SE INFORMA Y SE FICHA.**
   **En ARGOS 116 esto se aplicó: Coatzacoalcos estaba en la lista de prohibiciones y aportó una ficha,
   porque el hecho era nuevo.**
8. **Una sola búsqueda, y solo si sobra**: el **cohecho de Tempoal** (`ARG-116-005`, a quién se imputa y
   de qué corporación) · el **inhibidor de señal de Puebla** (marca y lote, `ARG-116-003`) ·
   Valdez Mainero (`ARG-114-REC-001`) · el componente extranjero de Rosario (`ARG-114-002`) ·
   la sucesión del Cártel de Los Reyes · la contradicción de lesionados de `ARG-110-001`
   (**séptima edición sin arbitrar**) · los 39 vehículos de «El Amarillo» (`ARG-115-002`).

### 3.4 `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verifíquelo cada corte

**Verificado de nuevo en ARGOS 116**: la migración **está acreditada** —desde el 1-sep los reportes
diarios de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí— pero **ningún reporte
resultó alcanzable**: **el dominio está indexado, sus rutas no llevan fecha** y **la trampa de año
persiste**. **Ninguna cifra suya se usa desde su migración.**
**Verifíquelo cada corte, declare el resultado y no use ninguna cifra suya** mientras persista.

---

## BLOQUE 4 — EL BLOQUEO DE EGRESO YA NO ES SOLO DE `*.gob.mx`

⚠️ **Es el hallazgo de método que más condiciona a ARGOS 117.**

En ARGOS 116 se intentó **acceso directo a dos URL fechadas de MEDIOS REGIONALES** —no portales
oficiales— para fijar a titular el desglose de armas de Ciudad Juárez:

```
curl https://www.esloquehayjuarez.com/2026/09/04/...  → curl: (56) CONNECT tunnel failed, response 403
curl https://diario.mx/juarez/2026/sep/04/...         → curl: (56) CONNECT tunnel failed, response 403
```

**Ya había ocurrido en ARGOS 115.** La consecuencia operativa es seria: **hay datos reproducibles en
varias consultas independientes que NUNCA podrán fijarse a un titular**, porque el titular existe pero
no se puede leer.

> ⚠️ **REGLA OPERATIVA**: la regla «una verificación cuenta solo si devuelve un TITULAR, ENCABEZADO o
> URL que CONTENGA el dato» **sigue vigente y no se relaja**. Pero cuando un dato **no pueda fijarse por
> bloqueo**, la decisión de integrarlo **se razona caso por caso y se declara en la ficha**.
> **El criterio que usó ARGOS 116, y que conviene conservar**: se integra si **encaja aritméticamente
> con una cifra que el titular SÍ fija** —el desglose «3 largas + 4 cortas» suma exactamente las
> «7 armas» del titular— y **no** se integra el detalle que no tiene ese anclaje —marcas y calibres—,
> que se publica **con reserva expresa `SIN FIJAR EN TITULAR`**.

**Techo de confianza: ★★★★☆.** `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
**Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige
lectura directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las casillas deben CUADRAR con las 32 entidades.** ARGOS 116 cuadró **dos veces**.

---

## BLOQUE 5 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes de
ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla de `site:`** de la 3.1 y **el tope
duro de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta sin
  restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Séptima edición consecutiva.
  **No es opcional**: en ARGOS 116 aportó **los dos hechos de mayor gravedad**, que **ningún barrido vio**.
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS Y SOBRE SUS EXCLUSIONES.** Ver Bloque 6.

⚠️ **Y REVISE TODA EXCLUSIÓN QUE UN BARRIDO ATRIBUYA A UNA INSTRUCCIÓN SUYA.** **Las prohibiciones de
gasto se redactan contra el PENDIENTE, no contra el TOPÓNIMO.** En ARGOS 116 **Coatzacoalcos estaba en
la lista de prohibiciones y aportó una ficha**, porque el hecho era nuevo.

⚠️ **Y HAGA EL `grep` DE ARCHIVO SOBRE LO QUE LOS BARRIDOS TRAIGAN, no solo sobre lo que este archivo
enumera.** Es la lección de ARGOS 115, y en ARGOS 116 **evitó dos publicaciones de hechos ya publicados**.

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️ **UN CANDIDATO DESCRITO POR SU TITULAR ES IRRECONOCIBLE CONTRA EL ARCHIVO — trampa NUEVA de ARGOS 116 y la que más costó** | El candidato «Puebla · operativo con dos detenidos y un agresor abatido» **se arrastró dos ediciones** siendo **`ARG-109-004`, ya publicado y ya clasificado 🟡**. **REGLA: todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS.** Distinta del fallo de Pénjamo: allí no se repitió el `grep`; aquí el `grep` sí se repitió y falló **cómo estaba escrito el candidato** |
| ⚠️ **EL RESUMIDOR REFECHA HECHOS ANTIGUOS AL DÍA DE LA CONSULTA, no solo inventa números** | **Tihuatlán** llegó como candidato del 4-sep-2026 con **51,910 L y 95 cartuchos** — idénticos a `ARG-102-REC-004`, de agosto, sobre una **URL sin fecha en la ruta**. **Cuando un candidato no tenga fecha en ruta ni titular, `grep` por sus CIFRAS DISTINTIVAS** |
| ⚠️ **UN CONTROL PUEDE OBLIGAR A INTEGRAR, Y PUEDE TUMBAR UNA TESIS DE PORTADA** | **Segunda vez en la serie que un control AUMENTA un total y primera que obliga a reescribir una conclusión de portada.** `procedencia-cifras` acreditó **3 largas + 4 cortas en Ciudad Juárez** y **1 revólver en Lomas de Barrillas**, contra un borrador que publicaba «ninguna de las 10 armas tiene categoría» y «Coatzacoalcos: cero armas de fuego». **Efecto: cortas 0→5, largas 0→3, armas 10→11, detenidos 15→23, eventos 3→4.** **Encargue los controles en las DOS direcciones** |
| ⚠️ **El bloqueo de egreso alcanza también a medios regionales** | Ver Bloque 4. **Hay datos que nunca podrán fijarse a titular.** Criterio: integrar si **encaja aritméticamente con una cifra que el titular sí fija**; el resto, con reserva `SIN FIJAR EN TITULAR` |
| ⚠️ **EL BLOQUE `MEXICO_PATHS` VIVE EN UN TERCER RANGO DE LA PLANTILLA** | Al extraer la plantilla, `MEXICO_VIEWBOX` + `MEXICO_PATHS` —la geometría de las 32 entidades— **quedó fuera**: vive **entre el cierre de la última `<section>` y `const CORTE_FECHA`**. **El cartelón habría cargado con el radar poblado y LOS DOS MAPAS VACÍOS.** **Lo detectó el validador, no la revisión visual. Extraiga la plantilla en TRES tramos** |
| ⚠️ **La confusión de las dos detenciones de Zacatecas VIENE DE LAS FUENTES y es recurrente** | **Segunda vez que llega fusionada** —ARGOS 113 por dos barridos, ARGOS 116 por Noreste con dos fuentes—. **El deslinde es firme**: `ARG-113-FE-002` (William Ariel «N», 18, **30-ago, Asientos, AGUASCALIENTES**, ataque de **Villa García**) y `ARG-113-001` (Juan Pedro «N», 29, **1-sep, Piedra Gorda, ZACATECAS**, ataque de **Ojocaliente**, con boletín propio). **Blindar el deslinde en cada traspaso** |
| ⚠️ **El resumidor FABRICA números de comunicado `DPE/…` de la FGR** | **Diez en tres ediciones y nueve entidades.** En ARGOS 116: `DPE/3931/2026` (Colima), `DPE/3927/2026` (Zacatecas), `DPE/3921/2026` y `DPE/3924/2026` (Chiapas), más `DPE/3930/2026` (BC). **Cadena exacta entre comillas; el negativo VENCE al arbitraje** |
| ⚠️ **Un indicador de cobertura no puede contar lo que el cartelón no publica** | Compruebe **los DOS renglones**: el cuadre de entidades **y el TOTAL de armamento**. ARGOS 116 cuadró los dos |
| **Fecha futura** | Ninguna fecha de hecho posterior al día del corte |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado nueve ediciones. En ARGOS 116: **4-sep viernes, 5-sep sábado**; el **31-ago fue lunes** («La Ventanita») |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: **fecha la página, no el hecho**, y **no basta como fuente única** |
| ⚠️ **Un agregado estatal puede reempaquetar un hecho ya publicado sin fecharlo** | **Cotéjelo por MUNICIPIO Y POR NOMBRE, no por titular** |
| **Agregado que no se reparte** | Un balance de varios días **no se distribuye** en una ventana. En ARGOS 116 se aplicó a **Coahuila** y a **«Operación Frontera Norte»** |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | «Cuauhtémoc» Zacatecas, Chihuahua y CDMX · «Matamoros» Tamaulipas y Coahuila · «Los Reyes» Michoacán y Edomex · «Rosario» Sinaloa · «Villa de La Paz» **SLP, no Guerrero** · **«San Isidro» y «Parajes de San Isidro» son dos lugares distintos de Ciudad Juárez** |
| **Dos objetos del mismo caso que el resumidor funde** | **El artefacto EMPLEADO y el ASEGURADO de la serie de Zacatecas.** Buscar «peritaje» devuelve el dictamen del **coche bomba empleado**, no del **niple asegurado** |
| **El AEI empleado no es AEI asegurado** | El empleado va al semáforo, **no al conteo** |
| **Pena compuesta** | ⚠️ **En Teotihuacán el «cada uno» está publicado de la MULTA, no de la PRISIÓN.** **50 conjuntos o 200 acumulados: sin determinar** |
| **«Más de» no es cifra** | **No se redondea.** En ARGOS 116 dejó fuera el monto exacto de Tempoal (**«más de 15 millones»**) |
| **Sentencia frente a vinculación a proceso** | **Lea el verbo del título** — y compruebe que el título EXISTE. **«Mandar a la cárcel» no es término de condena** |
| **Dos casos de la misma fiscalía, el mismo día** | **Municipio, delito y pena coincidentes NO identifican un caso**: hacen falta **dos campos individualizadores**. **La PENA no individualiza en delitos con alto uso de abreviado** |
| ⚠️ **Corroboración asimétrica** | **El nivel de confianza de una fila lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo. En ARGOS 116 dejó Coatzacoalcos en Bajo por la cifra de detenidos contradicha (15 o 14), pese a tener cinco fuentes |
| **Corroboración débil por construcción** | Varios republicadores del mismo boletín **no son fuentes independientes**. En ARGOS 116 se declaró en **Coatzacoalcos y Tempoal**, que descansan en regionales que reproducen el mismo texto de la FGE |
| **Cargadores y cartuchos** | **Nunca se suman entre sí.** «Cargadores de N cartuchos cada uno» **no** son cartuchos |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. **Y compruebe la aritmética** |
| **Un `grep` sin leer** | Si una consulta devuelve una ficha o un `-FE-` sobre el hecho que se ficha, **es de lectura obligatoria** |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  **Máximo cinco líneas** en cada **Explotación ARGOS** (numeradas 1. a 5.), en cada **recuadro
  `alerta contexto`** y en la **Valoración**. La portada lleva **UN SOLO recuadro**, «LO QUE DEBE SABER EL
  MANDO». **«Hecho confirmado» va en registro telegráfico** —fecha · lugar · corporación · cifras ·
  reservas, separado por `·`—, no en prosa. **«Corroboración» es una lista de emisores por tipo.**
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes, deslindes
  ni marcas de reserva. Se recorta la prosa, no el dato.**
  **ARGOS 116 lo cumplió en los 17 bloques**, verificado con un contador automático.
  ⚠️ **El contador debe exigir `<b>N. ` con espacio**: si no, `<b>7.62×39` cuenta como línea numerada.
- **Solo el día.** El cartelón publica hechos de su propia ventana. Las recuperaciones van con ARG-ID
  `-REC-`, **ventana de origen declarada** y **fuera de todos los totales**. **ARGOS 116 publicó una**
  (Tepuche) y la declaró fuera del semáforo, del mapa, del radar y de los conteos.
  ⚠️ **Y un hecho YA PUBLICADO en una edición anterior no vuelve como `-REC-`: eso es duplicación.**
  ⚠️ **Un antecedente de ventana anterior que hace legible un hecho del corte se declara DENTRO de la
  ficha, no como `-REC-` ni como hecho propio.** Así se trató el ataque a «La Ventanita».
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID `-FE-`
  **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 116 cumplió: cinco `-FE-`
  registrados, cero en el cartelón y cero en la móvil.**
  ⚠️ **Cuidado al citar un deslinde: escribir un `-FE-` dentro de una ficha mete un `-FE-` en el cartelón.**
  **Cite «el corte anterior», no el ARG-ID** —salvo que sea un ARG-ID de hecho, como `ARG-109-004`, que sí
  puede citarse.
- **Sin «Ejes del día» y sin resumen ejecutivo.** Cada hecho aparece **una sola vez**, en su ficha.
  ⚠️ **`editor-duplicidad` señalará que `CLAUDE.md` pide «Ejes del día»: la instrucción del destinatario,
  posterior y más específica, la retiró y fijó «LO QUE DEBE SABER EL MANDO». No la reintroduzca.**
- **Ningún hecho con ficha propia entra además en una tabla resumen.** La tabla **remite a la ficha** con
  enlace `#ARG-ID` y aporta **campos distintos**.
- ⚠️ **No remita a secciones que la edición no tiene.** ARGOS 116 estuvo a punto de mandar 15 detenidos a
  una tabla de «detenciones relevantes» **que no existía en la edición**.
- ⚠️ **No nombre entidades sin ficha ni caso asociado.** ARGOS 116 nombraba tres entidades por sus números
  `DPE/…` fabricados **sin caso**: eso es hallazgo de método y va al archivo de fuentes.
- **Toda cifra en cero lleva al lado el dato que la explica.** Tarjetas de armamento con **doble cifra
  rotulada** y **leyenda encima del bloque**; la línea inferior es **cálculo propio** y se declara.
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** Ciclos, presupuesto, agentes y cobertura van al archivo de fuentes.
  ⚠️ **No mida en «ediciones» dentro del cartelón: mida en FECHAS.** ARGOS 116 lo verificó con un
  contador automático y quedó en **0**.
- **Conclusiones de inteligencia criminal**, no de método.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.** Use `<div class="alerta contexto">…`.
- ⚠️ **Cada sentencia integrada lleva ficha propia con sus apartados.** ARGOS 116 no integró ninguna.

### Estructura de páginas que hereda ARGOS 117

**Ocho páginas**, como salió ARGOS 116: portada · crimen organizado (I) a (III) · recuperación ·
armamento · sentencias · valoración y conclusiones.
**Si el volumen lo pide, se reparte entre más páginas: nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en TODAS las páginas (8 en ARGOS 116).
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.
#    ⚠️ AL EXTRAER LA PLANTILLA, SON TRES TRAMOS, NO DOS:
#      (a) cabecera: líneas 1 a 428 — la etiqueta <body> está en la 429, NO en la 428
#      (b) MEXICO_VIEWBOX + MEXICO_PATHS: entre <script> y const CORTE_FECHA  ← EL QUE SE OLVIDÓ
#      (c) desde const REGION_ORDER hasta el final del <script>
#    Compruebe SIEMPRE que haya exactamente un <body> y que MEXICO_PATHS tenga 32 entidades.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 117 <FECHA> 116 2026-09-05 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.** Entre `EVENTOS_ARM` y
`SIZE_R` viven **`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL` y
`GRIS`**.

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes es
«Occidente» en la tabla** aunque el barrido lo cubra Noreste. Un `region:` mal puesto **coloca el eco del
radar en el sector equivocado y nadie lo nota**.

**Comprobación de coherencia obligatoria** —ARGOS 116 la ejecutó como un solo script de Python y conviene
reutilizarla—: extraer el bloque de datos **desde `const MEXICO_VIEWBOX` hasta `const SIZE_R`**, hacer
`node --check`, y validar que **las siete constantes están presentes**, que **`MEXICO_PATHS` tiene 32
entidades**, que **cada `estado:` existe en `MEXICO_PATHS`**, que **cada `region:` coincide con
`STATE_REGION`**, que **ninguna fecha cae fuera de la ventana**, que **no hay ARG-ID duplicados** y que
**el semáforo derivado de `EVENTOS` coincide con los contadores tecleados en la portada y en
`radar-stats`**.

⚠️ **Y añada el contador automático de la regla de cinco líneas** —`<b>N. ` **con espacio**— y el de
**medidas en «ediciones»**, que debe dar **0**.

⚠️ **Y RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS, no desde el borrador.** En ARGOS 116
`procedencia-cifras` cambió **seis renglones del total** y el recálculo independiente fue lo que
confirmó el cuadre final.

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en ambas
versiones · toda tabla envuelta **exactamente una vez** en el escritorio · **cero `-FE-` en ambas** · cero
`sem-item` fuera de portada · cero tarjetas `.reg` sin texto · cero restos de clases de escritorio en la
móvil (`sem-item`, `stat-tile`, `cover-visuals`, `masthead`) · **pie con número, fecha y hora en todas las
páginas del escritorio** · **todos los ARG-ID del escritorio presentes en la móvil** · sin desbordamiento
horizontal a 390 px.

*Notas del generador, que NO son defectos*: la móvil **no lleva `<script>`** · **`table-wrap` aparece en
cero** —el generador lo renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**, de modo que **`<table>` puede aparecer en CERO en la móvil sin que se pierda un solo
dato**. **Verifíquelo contando ARG-ID, no etiquetas `<table>`.** · La móvil lleva **un solo pie**.

---

## BLOQUE 9 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo, que se remita a tablas inexistentes y que las casillas de cobertura no cuadren con las 32 entidades |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **y que se descarte por precaución una que sí debía integrarse** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **UNDÉCIMA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES DE LOS DOS CONTROLES.** En ARGOS 116 **los dos
devolvieron `CORREGIR ANTES DE PUBLICAR` y los dos tenían razón**. `procedencia-cifras` **cambió seis
renglones del total nacional y obligó a reescribir la tesis de portada**; `editor-duplicidad` **corrigió
tres incoherencias internas**, entre ellas un conteo de candidatos que decía cinco cuando eran seis.
Si el destinatario no autoriza subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la
ausencia en el indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una búsqueda o
un `grep` de arbitraje antes de obedecerlo**, y **un control puede obligar a INTEGRAR lo que el borrador
descartó por precaución**. **Ni obedecer ni descartar por precaución: arbitrar.**
⚠️ **Y cuando el control declare que NO pudo fijar su hallazgo a un titular, ARBÍTRELO USTED**: en
ARGOS 116 el coordinador lo hizo con dos búsquedas propias y **el control tenía razón las dos veces**.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos
**y sobre sus propias instrucciones**.

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS.**
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al cartelón
   pero sí al índice. **Y retirar del índice los ARG-ID que se hayan quedado sin usar por una corrección.**
3. **Escribir `reports/_arranque-ARGOS-118.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
