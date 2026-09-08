# ORDEN DE ARRANQUE — ARGOS 119

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino en
el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 118** (corte 2026-09-08).

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

**Estado que debe encontrar ARGOS 119**: última edición `argos-2026-09-08` (ARGOS 118), **99 archivos** en
`reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió: pare y avísele al
destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló DOCE ediciones seguidas y volverá a fallar.** La rama que el entorno asigna **llega
> desactualizada**. En ARGOS 118 mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición y
> **62 archivos** —**doce ediciones por detrás**—: numerar por lo que la rama tenía a la vista habría
> producido **un falso «ARGOS 107» con ventana solapada de quince días**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**
> Si el merge no es *fast-forward*, la rama trae commits propios: entonces `git merge origin/main` y resolver.

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 119** |
| **Corte** | la fecha real del día, verificada con `TZ=America/Mexico_City date` |
| **Ventana** | **abre 2026-09-08 10:38 CDMX** (cierre de ARGOS 118) y cierra a la hora real de arranque |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `reports/argos-<FECHA>-movil.html` · `reports/argos-<FECHA>-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-120.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de solape.
**Verifique la hora, no la suponga.**

⚠️ **La serie sigue sin ventanas estables**: 47 → 25 → 46 h 30 min → **26 h 22 min**. ARGOS 118 duró
**poco más de la mitad** que la anterior y produjo **5 hechos frente a 7**: **MÁS densidad por hora, no
menos**. **Ninguna edición es comparable con otra sin normalizar por duración**, y así se declaró en portada
y Valoración. **Conviene sostener horas de arranque estables para que la serie recupere comparabilidad.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-08-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR — NO SOLO SOBRE LOS QUE ESTE ARCHIVO ENUMERA.**
   **En ARGOS 118 fue EL CONTROL QUE MÁS VALOR PRODUJO DE TODA LA EDICIÓN**: al pasarlo sobre «Buenavista»
   devolvió `ARG-117-004` con **la colonia El Hospital**, y eso acreditó que el cateo de **«El Maguey»** que
   traía el recall **era un hecho YA PUBLICADO**. **Sin ese `grep`, el corte habría contado dos veces
   6 armas largas y 47 cargadores.** También obligó al deslinde de **«La Campana»** (Culiacán frente a
   Escuinapa, `ARG-103-REC-001`).

   ⚠️⚠️ **Y LA LECCIÓN NUEVA, QUE ES LA MÁS IMPORTANTE DE ESTE ARRANQUE:
   LA DEDUPLICACIÓN NO SE CIERRA CON LA FECHA NI CON LA CORPORACIÓN. SE CIERRA CON EL LOCALIZADOR MÁS FINO.**
   El mismo aseguramiento de Buenavista se publicó con **otra fecha** (4 frente a 5-sep), **otra corporación**
   (GN y Ejército frente a SSP de Michoacán), **otro solicitante** (FGR frente a FGE) y **otra cifra de
   cartuchos** (438 frente a 342). **CUATRO de los criterios de cruce de `CLAUDE.md` fallaron.**
   **Lo cerró la COLONIA —col. El Hospital— más la coincidencia exacta de 6 largas y 47 cargadores.**
   **Exija siempre el localizador más fino que publiquen las fuentes: colonia, localidad o paraje, nunca
   solo el municipio.**

   ⚠️ **Y el `grep` por CIFRAS DISTINTIVAS no basta: hay que buscar el TITULAR por esas cifras.** Regla de
   ARGOS 117, que sigue vigente y sigue siendo barata.

   ⚠️ **Y el `grep` debe ser por TOPÓNIMO DE LOCALIDAD, no solo por entidad y municipio.**
   **«La Campana» es de Culiacán Y de Escuinapa** · «Cuauhtémoc» es municipio de Colima, Zacatecas y
   Chihuahua **Y** alcaldía de CDMX · «Matamoros» está en Tamaulipas Y Coahuila · «Los Reyes» en Michoacán
   Y Edomex · «Buenavista» en Michoacán tiene **cuatro hechos distintos en tres colonias** ·
   **«San Rafael» es colonia de la alcaldía Cuauhtémoc, CDMX, Y municipio de Veracruz** ·
   **«Lázaro Cárdenas» es municipio de Michoacán Y de Quintana Roo Y monumento en la col. La Sabana de
   Acapulco** · «Villa de La Paz» es de San Luis Potosí, **no de Guerrero**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 119 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. NOVENA EDICIÓN COMO PASO
OBLIGATORIO.**

| Origen del hecho | ARGOS 115 | ARGOS 116 | ARGOS 117 | **ARGOS 118** |
|---|---|---|---|---|
| Barridos regionales | 6 de 7 | 4 de 6 | 3 de 7 | **2 de 5** |
| Recall y arbitraje del coordinador | 1 de 7 | 2 de 6 | 4 de 7 | **3 de 5** |

⚠️ **LAS DOS VÍAS SIGUEN SIENDO INDISPENSABLES POR RAZONES OPUESTAS. NO RETIRE NINGUNA.**
- **El recall aportó los tres hechos de mayor volumen** —Guerrero/22 AEI, Puebla/Esperanza y Sinaloa— **y
  la recuperación**, y **ningún barrido vio ninguno**. La causa es estructural: **un hecho nacional de gran
  cobertura se busca mejor por tema que por entidad**.
- **Los barridos aportaron los dos que ninguna consulta nacional habría devuelto** —**La Yesca** y
  **Silao**—, y **Silao es la ÚNICA fila del corte sostenida por un boletín oficial primario con fecha en
  la ruta**. **Un arma artesanal y un cartucho no aparecen en ninguna consulta nacional y sin embargo es la
  fila mejor sostenida documentalmente de las cuatro.**

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene dos preguntas, el tope es
**de dos en total, no de dos por pregunta**. **Cerrar un seguimiento en `SIN AVANCE` es el resultado
correcto cuando no hay dato**: en ARGOS 118 lo fue en **cuatro de los seis ejes**.

✅ **LA REGLA DE `site:` FUNCIONA. EL OBJETIVO PORCENTUAL SIGUE RETIRADO — NO LO REINTRODUZCA.**

> **`site:` SOLO contra dominios con fecha en la ruta; contra los demás, consulta genérica.**

**Dominios con fecha en la ruta — no los redescubra**:
**Guanajuato `boletines.guanajuato.gob.mx/AAAA/MM/DD/`** (⚠️ **el que produjo la única fila con boletín
oficial primario de ARGOS 118: consúltelo siempre**) · **Durango `fiscalia.durango.gob.mx/AAAA/MM/DD/`**
(**publicó el 2 y el 5-sep**; produjo la única sentencia integrable de ARGOS 117) ·
Querétaro `fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/` (**publicó el 3-sep**) ·
San Luis Potosí `seguridad.slp.gob.mx/noticias/AAAA/M/D/` · Veracruz `veracruz.gob.mx/AAAA/MM/DD/`
(**la vía de Veracruz, no la FGE**).

⚠️ **MATIZ NUEVO DE ARGOS 118, QUE CORRIGE EL DE ARGOS 117**: **el dominio con fecha en la ruta rinde con
independencia del eje por el que se le interrogue.** Guanajuato produjo su boletín **encabezando con
armamento, no con judicial**. **Consulte SIEMPRE los cinco dominios con fecha en la ruta, toque o no toque
judicial a su región.**

**Sin fecha en la ruta (use genérica)**: Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa `fiscaliasinaloa.mx`
y `sspsinaloa.gob.mx` · Chihuahua `fiscalia.chihuahua.gob.mx` (⚠️ **exija ancla de republicador fechado**)
y `sspe.chihuahua.gob.mx` (⚠️ `ssp.chihuahua.gob.mx` es FALSO) · Colima `fgecolima.mx` ·
Nayarit `fiscaliageneral.nayarit.gob.mx` · Edomex **`fiscaliaedomex.gob.mx`** (⚠️ `fgjem.edomex.gob.mx` no
devuelve nada útil) · BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` · Coahuila `sspcoahuila.gob.mx` ·
Tamaulipas `tamaulipas.gob.mx/seguridadpublica/` · Tabasco `fiscaliatabasco.gob.mx` (⚠️ **rutas
`/Boletin/Index/NNNNN` SIN FECHA**) · Aguascalientes `aguascalientes.gob.mx/ssp/` ·
Puebla **`fiscalia.puebla.gob.mx`** (⚠️ `fiscaliapuebla.gob.mx` y `fgepuebla.gob.mx` **NO EXISTEN**) y
`ssp.puebla.gob.mx` · Hidalgo **`procuraduria.hidalgo.gob.mx`** (⚠️ **NO EXISTE una «Fiscalía General del
Estado de Hidalgo»**; ⚠️ **`@FGR_Hgo` es la delegación federal**) · Morelos `morelos.gob.mx/ultimas-noticias`
(⚠️ **trampa de año Y de fecha fabricada**) · **`fge.yucatan.gob.mx`** (**mejor taxonomía judicial de las
32**; ⚠️ **rutas opacas sin fecha, `/noticias/NNNN`**. **Consultado sin resultado en 117 y en 118;
CONSERVE EL ENCARGO**).

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** · **FGE Veracruz** (siete cortes de agregados sin
individualizar) · **`ssypc.nayarit.gob.mx`** · **`fgjsonora.gob.mx`** (**Sonora sigue revisada por vía
genérica**) · **`fiscaliaguerrero.gob.mx`** (lo más reciente indexado es de julio; **reconfirmado en 118**).
**No publican indexable**: FGJ Nuevo León · SSP Zacatecas.

### 3.2 Cobertura — qué encabeza el triaje y a quién se le asigna la deuda

✅ **NO QUEDA NINGUNA ENTIDAD `NO REVISADA` EN NINGUNO DE LOS DOS CUADRES.**
**Cuadres de ARGOS 118: nacional 5 + 27 + 0 + 0 = 32 · judicial 0 + 32 + 0 + 0 = 32.**

**A ARGOS 119 le toca el CICLO C — Occidente + Sureste** encabezando el triaje judicial; las otras cuatro
encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

⚠️ **EL CICLO B RINDIÓ DEFENSIVAMENTE POR SEGUNDA VEZ.** No produjo ninguna sentencia integrable, pero
**detectó cuatro trampas antes de gastar presupuesto en armamento**: dos de fecha en Noreste
(Aguascalientes/FGR y FGJ Zacatecas) y dos en Golfo (el **refechado del boletín 4894 de Tabasco** y la
**fabricación de los folios `DPE/3922` y `DPE/3966`**). **Se registra sin inflarlo.**

⚠️ **DEUDA REGIONAL — UNO SE CIERRA Y UNO SE CONSERVA:**
- ✅ **Mesas de Construcción de la Paz del SURESTE — CERRADO.** Las seis entidades consultadas una por una;
  seis negativos documentados. **El encargo de Mesas de Paz queda cerrado por completo en las 32.**
- ⚠️ **`fge.yucatan.gob.mx` — CONSERVE EL ENCARGO.** Devuelve la taxonomía judicial correcta pero con
  **rutas opacas y sin fecha**. **Sigue siendo el dominio con mejor taxonomía de las 32.**

### 3.3 Los seguimientos que más rinden

1. ⚠️ **GUERRERO — LOS VEINTIDÓS AEI Y LOS DOS DRONES.** *Máxima prioridad, y es nuevo.* **Dos búsquedas.**
   `ARG-118-001`: **22 artefactos explosivos improvisados**, **el mayor volumen del archivo** —el corte
   anterior cerró en **0**—, publicados **SIN TIPO, CARGA NI SISTEMA DE INICIACIÓN**, junto a **4 largas,
   848 cartuchos, 31 cargadores y 2 DRONES**, en el operativo contra «Los Ardillos» que ya va por
   **18 detenidos**.
   Qué buscar: **(a) peritaje de los 22 AEI** —tipo, carga, iniciación— · **(b) si los 2 drones están
   adaptados para lanzar**.
   **Por qué importa**: **veintidós piezas implican armador, taller y aprovisionamiento sostenido**, y
   **con éstas el archivo pasa de dos piezas explosivas sin caracterizar a veinticuatro**. La segunda
   pregunta **decide la categoría del adversario**: la lista roja recoge expresamente los **drones armados**.
   ⚠️ **Los drones están ASEGURADOS, no empleados, y NO se acreditan como armados: se contaron como
   0 drones armados. No lo cambie sin peritaje.**
2. ⚠️ **GUERRERO — EL PLAZO DE 24 HORAS DE «LOS RUSOS».** **Una búsqueda.** *Es el seguimiento más
   perecedero del archivo, junto con la Fenaza.*
   `ARG-118-REC-001`: cartulinas de **«Los Rusos»** en **Acapulco y Coyuca de Benítez**, madrugada del
   **7-sep**, que **amenazan de muerte al titular de la SSPC**, **exigen liberar a «El Amarillo»
   (`ARG-115-002`) en 24 horas** y **vetan nueve puntos** —San Marcos, Tres Palos, Zona Diamante, Puerto
   Márquez, Barra de Coyuca, Pie de la Cuesta, **Xaltianguis**, km 22 y km 30—.
   Qué buscar: **qué ocurrió al vencer el plazo**. **Ninguna autoridad ha confirmado autoría ni
   autenticidad.**
   ⚠️ **Y el cruce que hay que vigilar**: **Xaltianguis aparece en el veto de «Los Rusos» Y en el operativo
   contra «Los Ardillos»**. **Dos organizaciones distintas sobre la misma localidad en 26 horas.**
3. ⚠️ **PUEBLA — LA PATRULLA CLONADA Y LOS DOS BARRETT DE ESPERANZA.** **Dos búsquedas.**
   `ARG-118-003`: **9 detenidos**, entre ellos el **presidente municipal**, su hermano y la **exdirectora de
   Seguridad Pública**; **35 armas** —**2 fusiles Barrett cal. .50**—, **52 cargadores**, **1 patrulla
   clonada**, **1 dron** y **1 inhibidor de señal sin marca ni lote**. Estructura: **«Los Zúñiga»**.
   Qué buscar: **(a) cotejo de la patrulla clonada contra el parque vehicular de la DSPM de Esperanza** —
   **clonar exige placa, rotulación y número económico REALES: hay un original** · **(b) número de serie de
   los dos Barrett**.
   **Por qué importa**: si el original de la patrulla está en inventario, **la estructura no imitó a la
   policía: la usó**.
4. ⚠️ **ZACATECAS — LA FENAZA, HASTA EL 20 DE SEPTIEMBRE.** **Dos búsquedas.**
   **La ventana de ARGOS 119 vuelve a caer dentro.** **El dispositivo de 787 elementos (`ARG-115-001`) NO
   se recuenta.** **ARGOS 118 cerró la cuarta y la quinta jornadas sin incidente, amenaza, detención ni
   artefacto** en el recinto o su perímetro — **tercer resultado negativo consecutivo**. **El indicador
   sigue siendo si aparece artefacto en zona de concentración masiva.**
5. **NAYARIT — POR QUÉ NAYARIT NO SABÍA DE SUS SEIS MUERTOS** (`ARG-118-004`). **Una búsqueda.**
   **6 civiles armados abatidos en La Yesca** tras una persecución iniciada en **Teúl de González Ortega,
   Zacatecas**, que cruzó **Jalisco**. **Zacatecas lo confirma; corporaciones de Nayarit declararon no tener
   conocimiento del caso.** **Sin comunicado oficial de ninguna de las tres entidades.**
   Qué buscar: **un boletín que fije armamento y fecha**. **El armamento que circula —«31 rifles»,
   1 ametralladora, «cinco» granadas, lanzagranadas— NO se integró y no debe integrarse sin comunicado.**
6. **BAJA CALIFORNIA — Mexicali, col. Bosques del Sol.** **Una búsqueda, y solo si sobra.**
   ⚠️ **Es el candidato más cerca de integrarse de todo el archivo**: **tiene fecha en la ruta y está en la
   ventana de ARGOS 118**. Lo excluye **una sola cosa**: **fuente única regional sin comunicado oficial**,
   por debajo del umbral «Bajo», que exige **dos fuentes coincidentes**. **Una segunda fuente lo vuelve
   integrable — y entonces sería un hecho de la ventana de ARGOS 118, no de la 119.**
7. ⚠️ **NO gaste NINGUNA búsqueda en**: **protección balística** · **Agua Verde** (es Rosario) ·
   **«16 detenidos y 22 armas»** · **Tabasco «26 detenidos»** · **Coatzacoalcos–Villahermosa** ·
   **Tihuatlán** (`ARG-102-REC-004`) · **San Bernardino Tlaxcalancingo / «El Dron»** (`ARG-109-004`) ·
   **«Michoacán · diez municipios»** (Plan Michoacán, dic-2025) · **Hidalgo · Tepeji del Río y Huichapan**
   (27-jul-2026) · **Nayarit · Acaponeta** · **Michoacán · Chinicuila** (**cerrado por ventana DOS veces**) ·
   **Nuevo León · 6 del Cártel del Noreste** · **la serie de rafagueos de Coatzacoalcos** (**CERRADA con
   resultado positivo**) · **Bocoyna/Maguarichi** · **San Miguel de Allende** · **Poza Rica** ·
   **Pedernales** · **Tlaxcala** · **FGE Veracruz** · disputa forestal Michoacán/Guerrero ·
   **Petatlán y Totolapan** · **Loxicha** · **Matamoros serie y marcaje** · **el accionador de Villa
   García** · **«El Niño Concepción»** · **`fiscaliaguerrero.gob.mx`** · **`fgjsonora.gob.mx`** ·
   **el cateo de «El Maguey» en Buenavista** (**CERRADO: es `ARG-117-004`**) · **El Limoncito, Culiacán**
   (**CERRADO: es del 11-feb-2026**) · **«Detienen a 16 con arsenal en Michoacán»** (**CERRADO: titular
   reciclado de enero-2026**) · **Emilio Valdez Mainero** (**fuera de toda ventana reciente**).
   ⚠️ **PERO RECUERDE LA REGLA: estas prohibiciones van contra el PENDIENTE, no contra el TOPÓNIMO.
   Si aparece un hecho NUEVO, en ventana, en cualquiera de esos lugares, SE INFORMA Y SE FICHA.**
   En ARGOS 116 pasó con Coatzacoalcos, en ARGOS 117 con Buenavista y Cosío, y **en ARGOS 118 con Acapulco
   y Xaltianguis**, que tenían ARG-ID previos del mismo municipio **y aun así eran hechos nuevos**:
   **bastó declarar el deslinde**.
8. **Una sola búsqueda, y solo si sobra**: el **peritaje del AEI de Villas del Real** (`ARG-115-003`,
   ⚠️ **`SIN AVANCE` TRES VECES, y la última por no habérsele asignado búsqueda**; dato rastreable vivo:
   **causa penal 1486/2026**) · el **niple de Piedra Gorda** (`ARG-113-ARM-003`, **sexta vez**) · la
   **marca y lote del inhibidor** (⚠️ **quinta aparición del archivo, en Esperanza**) · el **cohecho de
   Tempoal** (`ARG-116-005`) · las **detenciones de Omealca** (`ARG-116-001`) · **Tepuche**
   (`ARG-116-REC-001`) · la **contradicción de lesionados de `ARG-110-001`** (**novena edición sin
   arbitrar**).

### 3.4 `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verifíquelo cada corte

**Verificado de nuevo en ARGOS 118, octava vez consecutiva**: la migración **está acreditada** —desde el
1-sep los reportes diarios de homicidio doloso y robo de vehículo se publican **en exclusiva** ahí— pero
**ningún reporte resulta alcanzable**: **el dominio está indexado**, **sus rutas son del tipo
`/contenido/NNNN/` y no llevan fecha**, y **la trampa de año quedó acreditada con caso concreto**:
`gabinetedeseguridad.gob.mx/contenido/6985` es un hecho del **21-oct-2025** que el resumidor devolvió como
si fuera actual. **Ninguna cifra suya se usa.** **Verifíquelo cada corte y declare el resultado.**

---

## BLOQUE 4 — EL BLOQUEO DE EGRESO NO ES SOLO DE `*.gob.mx`

⚠️ **Sigue siendo el hallazgo de método que más condiciona al producto.** El acceso directo devuelve
`curl: (56) CONNECT tunnel failed, response 403` **tanto en `*.gob.mx` como en medios regionales**.
**En ARGOS 118 ninguno de los seis barridos intentó `WebFetch`**, conforme a la instrucción.

> ⚠️ **REGLA OPERATIVA, CON DOS GRADOS, Y AHORA TAMBIÉN EN LA DIRECCIÓN CONTRARIA.** La regla «una
> verificación cuenta solo si devuelve un TITULAR, ENCABEZADO o URL que CONTENGA el dato» **sigue vigente y
> no se relaja**. Hay **dos grados de reserva, no uno**:
> - **Reserva fuerte, integrable**: el dato **encaja aritméticamente con una cifra que el titular SÍ fija**.
> - ⚠️ **Reserva débil, integrable pero con la fila degradada**: **no hay ninguna cifra en titular con la
>   que cuadre**, solo **convergencia de fuentes**. En ARGOS 118 fue el caso de **todas las cifras de
>   Guerrero** y de **los 52 cargadores de Esperanza**.
> ⚠️ **Y LA LECCIÓN NUEVA: UNA RESERVA DE MÁS TAMBIÉN ES UN DEFECTO DE PROCEDENCIA.** El borrador de
> ARGOS 118 marcó **las 35 armas de Esperanza como «sin fijar en titular»** cuando **tres titulares de dos
> medios independientes las fijan**. **`procedencia-cifras` lo atrapó y el arbitraje le dio la razón.**
> **Marcar como no fijada una cifra que sí lo está degrada injustamente la fila y desinforma al mando sobre
> qué puede citar.** **El control corre en las dos direcciones.**

**Techo de confianza: ★★★★☆.** `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
**Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** —exige lectura
directa— y debe figurar en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`.
**Y las casillas deben CUADRAR con las 32 entidades.** ARGOS 118 cuadró **dos veces**.

---

## BLOQUE 5 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes de
ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla de `site:`** de la 3.1 y **el tope duro
de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta sin
  restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Novena edición consecutiva.
  **No es opcional**: en ARGOS 118 aportó **tres de cinco hechos y la recuperación**.
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS Y SOBRE SUS EXCLUSIONES.** Ver Bloque 6.

⚠️ **Y REVISE TODA EXCLUSIÓN QUE UN BARRIDO ATRIBUYA A UNA INSTRUCCIÓN SUYA.** **Las prohibiciones de gasto
se redactan contra el PENDIENTE, no contra el TOPÓNIMO.**

⚠️ **Y ARBITRE LAS CLASIFICACIONES QUE PROPONGAN.** En ARGOS 118 el barrido de Sureste propuso clasificar
el hecho de Guerrero en **ROJO «por presencia de AEI»**, y **se rechazó**: el hecho del corte es **una
detención**, los artefactos están **ASEGURADOS, no empleados**, y la metodología prohíbe que la eficacia de
la respuesta estatal suba el nivel de riesgo. **El color lo fija el TIPO DE EVENTO, nunca el volumen de lo
asegurado.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️ **LA DEDUPLICACIÓN NO SE CIERRA CON LA FECHA NI CON LA CORPORACIÓN — trampa NUEVA de ARGOS 118 y la más cara que ha estado a punto de pasar** | El cateo de **«El Maguey»** en **Buenavista Tomatlán** llegó con **otra fecha** (4 frente a 5-sep), **otra corporación** (GN y Ejército frente a SSP de Michoacán), **otro solicitante** (FGR frente a FGE) y **otra cifra de cartuchos** (438 frente a 342). **Cuatro criterios de cruce fallaron.** **Lo cerró la COLONIA —col. El Hospital— más 6 largas y 47 cargadores exactos.** **Habría contado dos veces 6 armas largas y 47 cargadores.** `ARG-118-FE-001` |
| ⚠️ **UNA RESERVA DE MÁS ES UN DEFECTO DE PROCEDENCIA — trampa NUEVA, en la dirección contraria** | El borrador marcó **las 35 armas de Esperanza como «sin fijar en titular»** y **tres titulares de dos medios independientes las fijan**. **`procedencia-cifras` lo atrapó.** **Buscar la cifra entre comillas cuesta una consulta y evita degradar una fila injustamente.** `ARG-118-FE-004` |
| ⚠️ **UN CERO DE UNA EDICIÓN ANTERIOR PUEDE SER FALSO** | **ARGOS 117 declaró `AEI 0`** y la republicación federal acredita **2 AEI en el mismo aseguramiento**. **La corporación que publicó primero no los reportó.** **Lea los ceros del módulo de armamento como «no publicado», no como «no había».** **El archivo antiguo no se reescribe** |
| ⚠️ **HAY DOS FORMAS DE FRONTERA DE VENTANA, Y SE DISTINGUEN POR LA CONSUMACIÓN** | Dos hechos de ARGOS 118 cayeron sobre la **madrugada del día de apertura**. **Las cartulinas de «Los Rusos» fueron `-REC-`** porque **el hecho estaba consumado**; **Esperanza se integró** con marca `INICIO ANTERIOR A LA APERTURA` porque **no lo estaba** —los cateos arrancan a las 03:00 pero las detenciones y el arsenal se establecen dentro—. **El criterio es la consumación, no la hora de inicio.** `ARG-118-FE-003` |
| ⚠️ **EL REFECHADO YA NO SE MIDE EN MESES SINO EN AÑOS** | En ARGOS 118: `gabinetedeseguridad.gob.mx/contenido/6985` es de **oct-2025** y un comunicado SSC CDMX / SSEM es de **mar-2023** —3 policías muertos—, **los dos devueltos sin fecha visible simulando actualidad**. Más **El Limoncito** (feb-2026), el **boletín 4894 de Tabasco** (abr-2026), el **titular reciclado de Michoacán** (ene-2026) y el **operativo de Colima** (18-ago-2026) |
| ⚠️ **AL CITAR UN ARG-ID DEL ARCHIVO, COPIE LA FECHA DEL HECHO, NO LA DE PUBLICACIÓN** | En ARGOS 118 el borrador citó `ARG-117-002` como «los 16 detenidos del **6-sep**» cuando **el hecho es del 5-sep** y el 6 es la publicación. **Lo atrapó `editor-duplicidad`.** **No es una regla nueva: es la de `CLAUDE.md` incumplida al citar una ficha propia, que es donde nadie la vigila.** **El índice fija la fecha del hecho: cópiela de ahí** |
| ⚠️ **EL `grep` PRUEBA QUE UN HECHO YA ESTÁ PUBLICADO; SOLO LA BÚSQUEDA POR CIFRAS PRUEBA QUE ES VIEJO** | Regla de ARGOS 117, sigue vigente. Cuando un candidato no tenga fecha en ruta ni titular, **busque el TITULAR por sus cifras distintivas entre comillas** |
| ⚠️ **El resumidor FABRICA FECHAS y FABRICA folios `DPE/…`** | **Dieciocho folios en cinco cortes**; en ARGOS 118, `DPE/3922` y `DPE/3966` (Golfo) más la reincidencia de tres de Centro. **Cadena exacta entre comillas; el negativo VENCE.** La fabricación de fechas **se detecta pidiendo la misma fecha dos veces** — así cayó el boletín 4894 de Tabasco |
| ⚠️ **Colisión de topónimo de LOCALIDAD** | **«La Campana» es de CULIACÁN Y de ESCUINAPA** (`ARG-103-REC-001`) · **«dron» puede ser objeto asegurado o el alias «El Dron»** (`ARG-109-004`), y ambos casos son de **Puebla** · «Cuauhtémoc» tiene cuatro homónimos · «Buenavista», Michoacán, tiene **cuatro hechos en tres colonias** |
| ⚠️ **Cruce cruzado de entidad por agregado nacional** | **«Los Coyotes, Lázaro Cárdenas» es de MICHOACÁN, no de Tabasco**: el resumidor lo devolvió dentro de un agregado federal en una consulta dirigida a Tabasco. **Compruebe la entidad, no solo el topónimo** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado once ediciones. En ARGOS 118: **3-sep jueves, 4 viernes, 5 sábado, 6 domingo, 7 lunes, 8 martes**. Sostuvo que Jesús María está EN ventana y que las cartulinas de «Los Rusos» —«madrugada del lunes»— caen **antes de las 08:16** |
| ***Liveblog*** | `en-vivo`, `minuto-a-minuto`, `hoy-DD-de-MES`: **fecha la página, no el hecho**, y **no basta como fuente única** |
| **Agregado que no se reparte** | **Cinco casos en ARGOS 118**: el boletín federal del **4-5-6 sep**, el **agregado semanal de la Mesa de Paz de Guerrero**, el **«Modelo de Seguridad Coahuila»**, el **balance mensual de la SSC CDMX** (3,225 armas) y las **cifras del Informe de Seguridad del 8-sep** |
| ⚠️ **Corroboración asimétrica** | **El nivel de confianza de una fila lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo. En ARGOS 118 bajó **Guerrero** y **Puebla** a **Bajo** y **La Yesca** a **★★☆☆☆** |
| **«Más de» no es cifra** | Dejó fuera **«más de 36,700 cartuchos»** de Acapulco, **«más de 1,500»** de Cosío y **«más de 7 toneladas»** de Coahuayutla y Zirándaro |
| **Cargadores y cartuchos** | **Nunca se suman entre sí.** |
| **Un delito y su detención son dos eventos** | Y **también en sentido inverso**: cuando un evento rojo incluya un resultado institucional, **ese resultado abre ficha y ARG-ID propios en verde** |
| **Sentencia frente a vinculación a proceso** | **Lea el verbo del título** — y compruebe que el título EXISTE. **«Vinculado a proceso», «imputado», «prisión preventiva» NO son sentencia** |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. ⚠️ **Y compruebe la aritmética**: el borrador de ARGOS 118 publicaba **«7,75 cargadores por arma larga (83 ÷ 6)»** cuando **83 ÷ 6 = 13,83** — el 7,75 era **el cociente de Guerrero aislado** rotulado como nacional |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  **Máximo cinco líneas** en cada **Explotación ARGOS**, en cada recuadro `alerta contexto` y en la
  **Valoración**, numeradas `<b>N. ` **con espacio**. La portada lleva **UN SOLO recuadro**, «LO QUE DEBE
  SABER EL MANDO». **«Hecho confirmado» va en registro telegráfico**, no en prosa.
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes, deslindes ni
  marcas de reserva. Se recorta la prosa, no el dato.** **ARGOS 118 lo cumplió en los 9 bloques contados.**
- ⚠️ **TRES RECUADROS COMO MÁXIMO EN TODO EL CARTELÓN** —portada, Valoración y Conclusiones—, **y ninguno
  repite el hecho de otro.** ⚠️ **NINGÚN RECUADRO EXPLICA UN COLOR NI UN MECANISMO DEL MÉTODO**: el color ya
  está en la etiqueta de la ficha y la ventana de origen en su trazabilidad. **Van al archivo de fuentes.**
  **Referencia de volumen: ~38.000 caracteres visibles.** **ARGOS 118 quedó en ~37.500 con cinco hechos.**
- **Solo el día.** Las recuperaciones van con ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de
  todos los totales**. ⚠️ **Y un hecho YA PUBLICADO no vuelve como `-REC-`: eso es duplicación.**
  **Es el criterio que separó, en ARGOS 118, a las cartulinas de «Los Rusos» —inéditas, llevan ficha— del
  cateo de «El Maguey» —ya publicado como `ARG-117-004`, va solo a fe de erratas—.**
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID `-FE-`
  **se sigue asignando y registrando en `indice-arg-id.md`**. **ARGOS 118 cumplió: cuatro `-FE-`
  registrados, cero en el cartelón y cero en la móvil.**
- **Sin «Ejes del día» y sin resumen ejecutivo.** ⚠️ **`editor-duplicidad` señalará que `CLAUDE.md` pide
  «Ejes del día»: la instrucción del destinatario, posterior y más específica, la retiró y fijó «LO QUE DEBE
  SABER EL MANDO». No la reintroduzca.**
- **Ningún hecho con ficha propia entra además en una tabla resumen.**
- ⚠️ **No remita a secciones que la edición no tiene.** **No nombre entidades sin ficha ni caso asociado.**
- **Toda cifra en cero lleva al lado el dato que la explica.** ⚠️ **ARGOS 118 tuvo CERO ROJOS y CERO
  SENTENCIAS**, y los dos ceros llevan su explicación en portada y en las tarjetas.
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** ⚠️ **No mida en «ediciones» dentro del cartelón: mida en FECHAS.**
- **Conclusiones de inteligencia criminal**, no de método.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.**
- ⚠️ **Cada sentencia integrada lleva ficha propia.** **ARGOS 118 integró cero** y la página de sentencias
  se resolvió con **tarjetas en cero explicadas y una tabla de candidatos no integrados con su motivo**.

### Estructura de páginas que hereda ARGOS 119

**Ocho páginas**, como salió ARGOS 118: portada · crimen organizado (I) a (III) · recuperación · armamento ·
sentencias · valoración y conclusiones.
**Si el volumen lo pide, se reparte entre más páginas: nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️ El pie de página lleva número, fecha y hora en TODAS las páginas (8 en ARGOS 118).
#    Si NO hay aseguramientos, EVENTOS_ARM = [] y se OMITE el div id="argos-map-arm";
#    si SÍ los hay, hay que RESTITUIRLO.
#    ⚠️ AL EXTRAER LA PLANTILLA, SON TRES TRAMOS, NO DOS:
#      (a) cabecera hasta la línea anterior a <body>
#      (b) MEXICO_VIEWBOX + MEXICO_PATHS: entre <script> y const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>, SIN las tres últimas
#          líneas (</script></body></html>), que se reponen al ensamblar
#    Compruebe SIEMPRE que haya exactamente un <body> y que MEXICO_PATHS tenga 32 entidades.
#    En ARGOS 118 los tramos fueron: 1-428 · 1240-1274 · 1317-1485 del archivo de ARGOS 117.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 119 <FECHA> 118 2026-09-08 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
#    ⚠️ Y REGENERE LA MÓVIL DESPUÉS DE CADA CORRECCIÓN DEL ESCRITORIO.
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.** Entre `EVENTOS_ARM` y
`SIZE_R` viven **`REGION_ORDER`, `STATE_REGION`, `SEVERITY_RANK`, `SEVERITY_COLOR`, `SEVERITY_LABEL` y
`GRIS`**.

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes es
«Occidente»**, y en ARGOS 118 hubo que comprobar expresamente que **Nayarit y Guanajuato también lo son**
aunque los cubriera el barrido de Occidente y **Zacatecas fuera «Noreste»** pese a originar la persecución
de La Yesca. Un `region:` mal puesto **coloca el eco del radar en el sector equivocado y nadie lo nota**.

⚠️ **CADA ARG-ID DE `EVENTOS` Y DE `EVENTOS_ARM` DEBE TENER UN ANCLA `id=` EN EL DOCUMENTO.** El mapa fija
`location.hash` con ese id. **Las filas de la tabla de armamento llevan `id="ARG-XXX-ARM-00N"`.**
**En ARGOS 118 los diez ARG-ID resolvieron: el defecto no se reintrodujo.**

⚠️ **Y `gen-movil.py` dejaba el mapa de aseguramientos VACÍO EN SILENCIO si el div llevaba cualquier
atributo. La regex ya está corregida: NO LA VUELVA A ESTRECHAR.** **Verificado en ARGOS 118: cero
`map-box` vacíos en la móvil.**

**Comprobación de coherencia obligatoria** —ARGOS 118 la ejecutó como un solo script de Python y conviene
reutilizarla—: extraer el bloque de datos **desde `const MEXICO_VIEWBOX` hasta `const SIZE_R`**, hacer
`node --check`, y validar que **las siete constantes están presentes**, que **`MEXICO_PATHS` tiene 32
entidades**, que **cada `estado:` existe en `MEXICO_PATHS`**, que **cada `region:` coincide con
`STATE_REGION`**, que **ninguna fecha cae fuera de la ventana**, que **no hay ARG-ID duplicados**, que
**cada ARG-ID de los dos arreglos resuelve a un ancla**, y que **el semáforo derivado de `EVENTOS` coincide
con los contadores tecleados en la portada y en `radar-stats`**.

⚠️ **Y añada el contador automático de la regla de cinco líneas** —`<b>N. ` **con espacio**, si no
«7.62×39» cuenta como línea— y el de **medidas en «ediciones»**, que debe dar **0**.

⚠️ **Y RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS, no desde el borrador.**
**En ARGOS 118 ese recálculo cuadró, pero el contador destapó un cociente mal escrito.**

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
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **que se descarte por precaución una que sí debía integrarse**, y **que se marque bajo reserva una que sí está en titular** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **DECIMOTERCERA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES DE LOS CONTROLES.** En ARGOS 118
`procedencia-cifras` devolvió **`CORREGIR ANTES DE PUBLICAR` con un hallazgo material y tenía razón**:
**el borrador marcaba bajo reserva las 35 armas de Esperanza, que sí están en titular**. **El arbitraje del
coordinador con búsqueda propia lo confirmó y, además, produjo un dato de inteligencia que el borrador no
tenía: el nombre de la estructura, «Los Zúñiga».**
Si el destinatario no autoriza subagentes, **ejecútelos a mano con el mismo criterio** y **declare** la
ausencia en el indicador de cobertura.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una búsqueda o
un `grep` de arbitraje antes de obedecerlo**, y **un control puede obligar a INTEGRAR o a REFORZAR lo que el
borrador degradó por precaución**. ⚠️ **Y cuando el control declare que NO pudo fijar su hallazgo a un
titular, ARBÍTRELO USTED.**

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.
**ARGOS 118 lo hizo así, corrigiendo el defecto de ARGOS 117.**

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos y
sobre sus propias instrucciones. **En ARGOS 118 fue el que más valor produjo**: el `grep` de topónimo sobre
lo que trajo el recall **evitó un doble conteo de 6 armas largas y 47 cargadores**, y el rechazo de la
clasificación en rojo que proponía un barrido **evitó inflar el semáforo con una acción institucional**.

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS.**
   ⚠️ **Y todo candidato que la edición evalúe recibe DISPOSICIÓN EXPRESA** —cerrado, sin avance o fuera de
   ventana—.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**, que no van al cartelón
   pero sí al índice. **Y retirar del índice los ARG-ID que se hayan quedado sin usar por una corrección.**
3. **Escribir `reports/_arranque-ARGOS-120.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
