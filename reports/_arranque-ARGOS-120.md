# ORDEN DE ARRANQUE — ARGOS 120

Documento de arranque para una **sesión nueva**. Se escribe al cierre de cada edición y lo consume la
siguiente. Existe porque la continuidad de ARGOS **no vive en la conversación que generó un corte, sino en
el repositorio**: una sesión nueva debe poder arrancar leyendo este archivo, `CLAUDE.md` y
`reports/_pendientes.md`, sin que nadie recuerde ni transcriba nada.

**Escrito al cierre de ARGOS 119** (corte 2026-09-13).

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

**Estado que debe encontrar ARGOS 120**: última edición `argos-2026-09-13` (ARGOS 119), **102 archivos**
en `reports/`, y `main` conteniéndola. **Si `main` está por detrás de eso, algo se rompió: pare y avísele
al destinatario antes de escribir una línea.**

> ⚠️ **Esto ya falló TRECE ediciones seguidas y volverá a fallar.** La rama que el entorno asigna **llega
> desactualizada**. En ARGOS 119 mostraba **`argos-2026-08-24` (ARGOS 106)** como última edición —**trece
> ediciones por detrás**—: numerar por lo que la rama tenía a la vista habría producido **un falso
> «ARGOS 107» con ventana solapada de veinte días**.
> **`git merge --ff-only origin/main` es el primer comando de la sesión, antes de leer `CLAUDE.md`.**

---

## BLOQUE 1 — IDENTIDAD DE LA EDICIÓN

| Campo | Valor |
|---|---|
| **Número** | **ARGOS 120** (se confirma con el Bloque 0) |
| **Ventana** | **abre 2026-09-13 08:28 CDMX**, cierra a la **hora real de arranque**, verificada con `TZ=America/Mexico_City date` |
| **Archivos a crear** | `reports/argos-<FECHA>.html` · `reports/argos-<FECHA>-movil.html` · `reports/argos-<FECHA>-fuentes.md` |
| **Archivos a actualizar** | `reports/_pendientes.md` · `reports/indice-arg-id.md` · este archivo, renombrado a `_arranque-ARGOS-121.md` |

**Continuidad de ventana**: abre exactamente donde cerró la anterior. Ni un minuto de hueco ni de solape.
**Verifique la hora, no la suponga.**

⚠️ **LA SERIE ACABA DE DAR UN SALTO DE ESCALA**: 47 h → 25 h → 46 h 30 min → 26 h 22 min → **117 h
50 min**. ARGOS 119 duró **4,5 veces** la anterior y **2,5 veces el récord previo**, y produjo **19 hechos
frente a 5**, pero **MENOS densos**: **0,16 hechos/hora frente a 0,19**. **Ninguna edición es comparable
con otra sin normalizar por duración**, y así se declaró en portada y Valoración.
⚠️ **Y hay un efecto de segundo orden que ARGOS 119 descubrió: UNA VENTANA LARGA NO PRODUCE
RECUPERACIONES, LAS ABSORBE.** **ARGOS 119 tuvo CERO `-REC-`** y no por falta de búsqueda. **La cifra de
recuperaciones es función de la duración de la ventana y no debe leerse como indicador de cobertura.**

---

## BLOQUE 2 — LECTURA OBLIGATORIA, ANTES DE LA PRIMERA BÚSQUEDA

1. `CLAUDE.md` — íntegro. No es plantilla: son las reglas operativas.
2. `reports/_pendientes.md` — el traspaso. Los seguimientos abiertos ya dicen qué buscar.
3. `reports/argos-2026-09-13-fuentes.md` — la edición anterior, con sus limitaciones declaradas.
4. `reports/indice-arg-id.md` — **`grep` obligatorio antes de fichar cualquier hecho como nuevo**, y
   **leer lo que devuelva**.

   ⚠️⚠️ **EL `grep` POR TOPÓNIMO SE REPITE SOBRE CADA TOPÓNIMO QUE UN BARRIDO O EL RECALL TRAIGA,
   INMEDIATAMENTE ANTES DE FICHAR.** En ARGOS 119 **evitó el TRIPLE conteo del cateo de «El Maguey»**:
   el boletín federal del 10-sep lo republicó por **tercera vez**, con **tres emisores distintos en tres
   cortes**, y **las tres veces lo cerró la COLONIA —col. El Hospital—**, no la fecha ni la corporación ni
   las cifras, que variaron. **De haberse integrado habría añadido falsamente 6 largas, 47 cargadores y
   2 AEI.**

   ⚠️⚠️ **Y LA LIMITACIÓN QUE HAY QUE CONOCER ANTES DE USARLO:
   `indice-arg-id.md` EMPIEZA EN `ARG-91-001`. LAS EDICIONES 88, 89 Y 90 NO ESTÁN INDEXADAS.**
   **NINGUNA FICHA PUEDE AFIRMAR «no aparece en ningún corte anterior del archivo»**: la fórmula correcta
   es **«no aparece en el índice, que cubre de ARGOS 91 en adelante»**. **En ARGOS 119 esa afirmación se
   hizo dos veces y las dos resultaron falsas** —«Corregidora» figura en `ARG-90-ARM-006` y «Benemérito de
   las Américas» en el acervo de ARGOS 88-89—, y **lo atrapó `editor-duplicidad`**.
   **Si hay presupuesto, extienda el índice hacia atrás; si no, declare el rango en su cabecera.**

   ⚠️ **Colisiones de topónimo ya acreditadas — no las redescubra**: **«La Campana» es de CULIACÁN Y de
   ESCUINAPA** (`ARG-118-002` frente a `ARG-103-REC-001` y `ARG-119-008`) · **«Tamazula» es municipio de
   DURANGO Y colonia Lomas de Tamazula en CULIACÁN** (`ARG-119-010` frente a `ARG-107-REC-001`) ·
   **«Palos Prietos» tiene dos hechos** (`ARG-107-002` y `ARG-119-003`) · **«San Rafael» es municipio de
   VERACRUZ Y colonia de la alcaldía Cuauhtémoc, CDMX** · «Cuauhtémoc» tiene cuatro homónimos ·
   «Buenavista», Michoacán, tiene cuatro hechos en tres colonias · **«Lázaro Cárdenas» es de Michoacán Y
   de Quintana Roo** · «Los Reyes» está en Michoacán Y Edomex · «Matamoros» en Tamaulipas Y Coahuila.
   ⚠️ **Y la sede de la autoridad receptora NO es el lugar del hecho**: `ARG-117-004` se puso a
   disposición de la **FGR con sede en Apatzingán** y `ARG-119-002` ocurrió **en Apatzingán**.

---

## BLOQUE 3 — DEUDA QUE ARGOS 120 HEREDA

### 3.1 El método que funcionó y hay que conservar

⚠️ **EL RECALL NACIONAL DEL COORDINADOR VA ANTES DE CERRAR NINGÚN BARRIDO. DÉCIMA EDICIÓN COMO PASO
OBLIGATORIO.**

| Origen del hecho | ARGOS 117 | ARGOS 118 | **ARGOS 119** |
|---|---|---|---|
| Barridos regionales | 3 de 7 | 2 de 5 | **11 de 19** |
| Recall y arbitraje del coordinador | 4 de 7 | 3 de 5 | **8 de 19** |

⚠️ **LAS DOS VÍAS SIGUEN SIENDO INDISPENSABLES POR RAZONES OPUESTAS. NO RETIRE NINGUNA.**
- **El recall aportó LOS CUATRO HECHOS ROJOS** —Chilpancingo, Apatzingán, Mazatlán y Elota— **y las dos
  sentencias**. **Ningún barrido vio Apatzingán ni Mazatlán.**
- **Los barridos aportaron las tres filas con boletín oficial primario** —**Guanajuato**, **Querétaro** y
  **Veracruz ×2**— y **los dos hallazgos de mayor volumen explosivo**.

⚠️ **EL TOPE DURO DE 2-3 BÚSQUEDAS POR EJE SIGUE FUNCIONANDO.** Si un eje tiene dos preguntas, el tope es
**de dos en total**. **Cerrar un seguimiento en `SIN AVANCE` es el resultado correcto cuando no hay dato.**

✅ **LA REGLA DE `site:` FUNCIONA. EL OBJETIVO PORCENTUAL SIGUE RETIRADO — NO LO REINTRODUZCA.**

> **`site:` SOLO contra dominios con fecha en la ruta; contra los demás, consulta genérica.**

**Los cinco dominios con fecha en la ruta — CONSÚLTELOS SIEMPRE, TOQUE O NO TOQUE JUDICIAL A SU REGIÓN.
En ARGOS 119 rindieron CUATRO DE LOS CINCO:**

| Dominio | Rendimiento en ARGOS 119 |
|---|---|
| **`boletines.guanajuato.gob.mx/AAAA/MM/DD/`** | ✅ **PUBLICÓ** (10-sep). **Segunda edición consecutiva en que aporta fila con boletín primario, y las dos SIN que ningún medio la replique** |
| **`fiscaliageneralqro.gob.mx/portal/AAAA/MM/DD/`** | ✅ **PUBLICÓ** (11-sep, Operativo Sinergia). **Primera vez que rinde desde ARGOS 108** |
| **`veracruz.gob.mx/AAAA/MM/DD/`** | ✅ **PUBLICÓ DOS VECES** (8 y 9-sep). **Confirmado: la vía de Veracruz es el portal del Gobierno del Estado, NO la FGE** |
| **`fiscalia.durango.gob.mx/AAAA/MM/DD/`** | ✅ **PUBLICÓ**, pero **fuera de ventana** (2 y 5-sep). **Permitió descartarlas SIN AMBIGÜEDAD: ése es su valor aunque no aporte fila** |
| `seguridad.slp.gob.mx/noticias/AAAA/M/D/` | `SIN RESULTADO INDEXADO EN VENTANA` |

**Sin fecha en la ruta (use genérica)**: Michoacán `fiscaliamichoacan.gob.mx` · Sinaloa `fiscaliasinaloa.mx`
y **`sspsinaloa.gob.mx`** (⚠️ **publica boletín propio CON CALIBRE POR PIEZA: es la mejor taxonomía de
armamento de las 32, consúltelo siempre**) · Chihuahua `fiscalia.chihuahua.gob.mx` (⚠️ exija ancla de
republicador fechado) y `sspe.chihuahua.gob.mx` (⚠️ `ssp.chihuahua.gob.mx` es FALSO) · Colima
`fgecolima.mx` · Nayarit `fiscaliageneral.nayarit.gob.mx` · Edomex **`fiscaliaedomex.gob.mx`** ·
BC `seguridadbc.gob.mx` · BCS `sspbcs.gob.mx` · Coahuila `sspcoahuila.gob.mx` ·
Tamaulipas `tamaulipas.gob.mx/seguridadpublica/` · Tabasco `fiscaliatabasco.gob.mx` (⚠️ rutas sin fecha
**y fabricación de fecha acreditada**) · Aguascalientes `aguascalientes.gob.mx/ssp/` ·
Puebla **`fiscalia.puebla.gob.mx`** y `ssp.puebla.gob.mx` · Hidalgo **`procuraduria.hidalgo.gob.mx`**
(⚠️ **NO EXISTE una «Fiscalía General del Estado de Hidalgo»**) · Morelos `morelos.gob.mx/ultimas-noticias`
(⚠️ trampa de año y de fecha fabricada) · **`fge.yucatan.gob.mx`** (**mejor taxonomía judicial de las 32**;
⚠️ rutas opacas sin fecha. **Consultado sin resultado en 117, 118 y 119; CONSERVE EL ENCARGO**).

⚠️ **VÍA NUEVA ACREDITADA EN ARGOS 119, CONSÉRVELA**: **los COMUNICADOS DE PRENSA DE LAS ZONAS MILITARES
de SEDENA se indexan a través de republicadores fechados** —el **n.º 59 de la 13.ª Zona Militar, V Región
Militar** corrigió el desglose de Ahuacatlán y subió la fila de Bajo a Medio—. **Cuando un aseguramiento
lo firme el Ejército y el boletín federal no baste, busque el comunicado de la zona militar por su
número.**

**Vacíos acreditados — NO gaste búsqueda**: **Tlaxcala** · **FGE Veracruz** (siete cortes de agregados sin
individualizar) · **`ssypc.nayarit.gob.mx`** · **`fgjsonora.gob.mx`** · **`fiscaliaguerrero.gob.mx`**
(**reconfirmado en 119**). **No publican indexable**: FGJ Nuevo León · SSP Zacatecas.

### 3.2 Cobertura — qué encabeza el triaje

✅ **NO QUEDA NINGUNA ENTIDAD `NO REVISADA` EN NINGUNO DE LOS DOS CUADRES.**
**Cuadres de ARGOS 119: armamento 9 + 23 + 0 + 0 = 32 · judicial 1 + 31 + 0 + 0 = 32.**

**A ARGOS 120 le toca el CICLO A — Noroeste + Centro** encabezando el triaje judicial; las otras cuatro
encabezan con armamento. *Se declara expresamente en el archivo de fuentes, junto con qué aportó.*

⚠️ **EL CICLO C RINDIÓ OFENSIVAMENTE, Y ES LA TERCERA ROTACIÓN CONSECUTIVA QUE CAMBIA LO QUE EL PRODUCTO
ENCUENTRA.** **Las dos sentencias integradas de ARGOS 119 son de Michoacán, entidad de Occidente**, que
encabezaba judicial, **y ninguna habría aparecido encabezando con armamento** —de hecho el armamento
michoacano del mismo barrido, **Los Amates**, **quedó por debajo del umbral**—.

⚠️ **DEUDA REGIONAL — UNA SE CONSERVA**: **`fge.yucatan.gob.mx`**, tercer corte consecutivo sin resultado.
✅ **Mesas de Construcción de la Paz: CERRADAS en las 32. No gaste búsqueda.**

### 3.3 Los seguimientos que más rinden

1. ⚠️ **NACIONAL — EL CORREDOR EXPLOSIVO SINALOA-NAYARIT-DURANGO.** *Máxima prioridad, y es nuevo.*
   **Dos búsquedas.** **26 AEI en tres entidades contiguas que comparten sierra, en cinco días**:
   **20 en Escuinapa** (`ARG-119-008`), **5 en Ahuacatlán** (`ARG-119-009`) y **1 en Tamazula**
   (`ARG-119-010`). **Supera los 22 de Guerrero del corte anterior** y es **el mayor volumen de una sola
   edición del archivo**. **Escuinapa acumula 47 AEI** (27 de `ARG-103-REC-001` + 20).
   Qué buscar: **peritaje comparado de iniciadores, contenedores y carga** de los tres lotes entre sí y
   contra los **22 de Guerrero** (`ARG-118-001`).
   **Por qué importa**: **el archivo pasa de 24 a 50 piezas explosivas sin caracterizar**. **El objetivo
   no son los artefactos: es el taller.**
2. ⚠️ **GUERRERO — LOS 22 AEI Y LOS DOS DRONES** (`ARG-118-001`). **Dos búsquedas.** **`SIN AVANCE` en
   ARGOS 119 con las dos búsquedas gastadas.** Sigue **sin tipo, carga ni sistema de iniciación**, y
   **ninguna fuente acredita que los drones estén adaptados para lanzar**: **se mantienen en 0 drones
   armados. NO LO CAMBIE SIN PERITAJE.**
3. ⚠️ **ZACATECAS — LA FENAZA, HASTA EL 20 DE SEPTIEMBRE.** **Dos búsquedas.** *Sigue siendo el
   seguimiento más perecedero del archivo: quedan siete días.* **ARGOS 119 cubrió seis jornadas de golpe
   (8 al 13-sep) sin incidente, amenaza, detención ni artefacto — CUARTO negativo consecutivo.**
   **El dispositivo de 787 elementos (`ARG-115-001`) NO se recuenta.** **El indicador sigue siendo si
   aparece artefacto en zona de concentración masiva.**
4. ⚠️ **NACIONAL — DOS HOMICIDIOS MÚLTIPLES EN INMUEBLES DE HOSPEDAJE EL MISMO DÍA** (`ARG-119-002`,
   `ARG-119-003`). **Una búsqueda.** **Mazatlán a las 03:00 y Apatzingán a las 20:10 del 9-sep**, los dos
   **con entrada directa a la habitación** y **cero detenidos**. **Una de las víctimas es un ELEMENTO
   ACTIVO DE LA GUARDIA NACIONAL comisionado en Oaxaca.**
   ⚠️ **EL PATRÓN NO ESTÁ ACREDITADO Y NO SE AFIRMA.** Qué buscar: **registro de huéspedes y
   videovigilancia**, o la **identificación forense de los cuatro de Apatzingán**.
5. ⚠️ **GUERRERO — «LOS ARDILLOS» PASAN A DISPARAR CONTRA EL ESTADO** (`ARG-119-001`). **Una búsqueda.**
   **Primer hecho del archivo en que la estructura agrede a personal militar en patrullaje** en vez de ser
   objeto de detenciones. **Y pobladores de Coacoyulillo confrontaron a la tropa con palos y piedras.**
   Qué buscar: **quién convocó a los pobladores**, o **la situación jurídica de «El Teo» y «El Güero»**.
   ⚠️ **Y el cruce que se agrava: XALTIANGUIS da nombre a la operación militar contra «Los Ardillos» Y
   figura en el veto territorial de «Los Rusos»** (`ARG-118-REC-001`).
6. **MICHOACÁN — LOS AMATES.** **Una búsqueda, y solo si sobra.** ⚠️ **Es el candidato MÁS CERCA DE
   INTEGRARSE del archivo y el MAYOR VOLUMEN NO INTEGRADO del corte**: **6 largas —5 AK-47 y 1 SCAR—,
   1,374 cartuchos, 43 cargadores y 1 rifle-granada de 40 mm**, arsenal abandonado en **Los Amates,
   tenencia La Mira, Lázaro Cárdenas**. **Lo excluye UNA SOLA COSA: FUENTE ÚNICA regional.** **No es la
   fecha. Una segunda fuente lo vuelve integrable.**
7. **Ciclo A (Noroeste + Centro) encabezando judicial, aplicado y declarado.** No queda ninguna entidad
   `NO REVISADA`. Las Mesas de Paz quedan **CERRADAS en las 32**. Conserve el encargo de
   `fge.yucatan.gob.mx`. **Y consulte SIEMPRE los cinco dominios con fecha en la ruta**, toque o no
   judicial a su región.
8. ⚠️ **NO gaste NINGUNA búsqueda en**: **protección balística** · **Agua Verde** (es Rosario) ·
   **«16 detenidos y 22 armas»** · **Tabasco «26 detenidos»** · **Coatzacoalcos–Villahermosa** ·
   **Tihuatlán** (`ARG-102-REC-004`) · **San Bernardino Tlaxcalancingo / «El Dron»** (`ARG-109-004`) ·
   **«Michoacán · diez municipios»** · **Hidalgo · Tepeji del Río y Huichapan** · **Nayarit · Acaponeta** ·
   **Michoacán · Chinicuila** (**cerrado por ventana TRES veces**) · **Nuevo León · 6 del Cártel del
   Noreste** · **la serie de rafagueos de Coatzacoalcos** · **Bocoyna/Maguarichi** · **San Miguel de
   Allende** · **Poza Rica** · **Pedernales** · **Tlaxcala** · **FGE Veracruz** · **Petatlán y
   Totolapan** · **Loxicha** · **Matamoros serie y marcaje** · **el accionador de Villa García** ·
   **«El Niño Concepción»** · **`fiscaliaguerrero.gob.mx`** · **`fgjsonora.gob.mx`** · **el cateo de
   «El Maguey» en Buenavista** (**CERRADO POR TERCERA VEZ: es `ARG-117-004`**) · **El Limoncito,
   Culiacán** · **«Detienen a 16 con arsenal en Michoacán»** · **Emilio Valdez Mainero** ·
   **BAJA CALIFORNIA · Mexicali, col. Bosques del Sol** (**CERRADO SIN INTEGRARSE en ARGOS 119**) ·
   **AGUASCALIENTES · Cosío** (**el buscador se agotó como vía; no repetir salvo acceso directo**).
   ⚠️ **PERO RECUERDE LA REGLA: estas prohibiciones van contra el PENDIENTE, no contra el TOPÓNIMO.
   Si aparece un hecho NUEVO, en ventana, en cualquiera de esos lugares, SE INFORMA Y SE FICHA.**
   En ARGOS 118 pasó con **Acapulco y Xaltianguis**, y **en ARGOS 119 con Chilpancingo, Escuinapa y
   Lázaro Cárdenas**, que tenían ARG-ID previos del mismo municipio **y aun así eran hechos nuevos**:
   **bastó declarar el deslinde**.
9. **Una sola búsqueda, y solo si sobra**: el **peritaje del AEI de Villas del Real** (`ARG-115-003`,
   ⚠️ **`SIN AVANCE` CUATRO VECES**; dato vivo: **causa penal 1486/2026**) · el **niple de Piedra Gorda**
   (`ARG-113-ARM-003`, **séptima vez**) · la **marca y lote del inhibidor** (⚠️ **sexta aparición**) ·
   el **cohecho de Tempoal** (`ARG-116-005`) · las **detenciones de Omealca** (`ARG-116-001`) ·
   **Tepuche** (`ARG-116-REC-001`) · la **contradicción de lesionados de `ARG-110-001`** (**décima vez**).

### 3.4 `gabinetedeseguridad.gob.mx/resultados/` — vacío recurrente, verifíquelo cada corte

**Verificado de nuevo en ARGOS 119, NOVENA vez consecutiva**: la migración **está acreditada** pero
**ningún reporte resulta alcanzable**: **el dominio está indexado**, **sus rutas son `/contenido/NNNN/` y
no llevan fecha**, **el acceso directo devuelve 403** y **la trampa de año está acreditada con caso
concreto**. **Ninguna cifra suya se usa.** **Verifíquelo cada corte y declare el resultado.**

---

## BLOQUE 4 — EL BLOQUEO DE EGRESO ALCANZA TAMBIÉN A LOS REPUBLICADORES

⚠️ **Sigue siendo el hallazgo de método que más condiciona al producto, y en ARGOS 119 se comprobó que
NO se limita a `*.gob.mx`.**

```
curl https://www.gob.mx/sspc                       → curl: (56) CONNECT tunnel failed, response 403
curl https://gabinetedeseguridad.gob.mx/resultados/ → curl: (56) CONNECT tunnel failed, response 403
WebFetch https://www.tallapolitica.com.mx/...       → EGRESS_BLOCKED
```

**El boletín federal del 9 y del 10-sep tuvo que reconstruirse por búsqueda dirigida, no por lectura.**

> ⚠️ **REGLA OPERATIVA, CON DOS GRADOS.** «Una verificación cuenta solo si devuelve un TITULAR, ENCABEZADO
> o URL que CONTENGA el dato» **sigue vigente y no se relaja**:
> - **Reserva fuerte, integrable**: el dato **encaja aritméticamente con una cifra que el titular SÍ
>   fija**. **En ARGOS 119 fue decisiva dos veces**: **447 + 9 + 10 = 466** en Elota y **5 + 748 = 753**
>   en Guanajuato. **Ese anclaje convirtió dos reservas en cifras citables.**
> - **Reserva débil, integrable con la fila degradada**: solo **convergencia de fuentes**.
> ⚠️ **Y LA LECCIÓN CENTRAL DE ARGOS 119: CITAR UN BOLETÍN NO EQUIVALE A HABERLO EXPLOTADO.**
> **`procedencia-cifras` encontró DOS fichas que daban por «no publicado» un desglose que la fuente
> primaria que ellas mismas citaban SÍ publicaba.** **El saldo neto de los controles fue INTEGRAR: +4
> armas y +10 cargadores.** **Antes de marcar «no publicado», LEA el boletín que va a citar.**

**Techo de confianza: ★★★★☆.** `docs/solicitud-lista-blanca-egreso.md` sigue sin tramitar.
**Verifíquelo en la sesión, no lo herede.**

⚠️ **Consecuencia sobre las casillas**: `SIN ACTUALIZACIÓN CONSTATADA` **no es utilizable** y debe figurar
en **0**. La casilla correcta es `SIN RESULTADO INDEXADO EN VENTANA`. **Y las casillas deben CUADRAR con
las 32 entidades.** **ARGOS 119 cuadró dos veces.**

---

## BLOQUE 5 — BARRIDO REGIONAL

`CLAUDE.md` exige seis agentes `barrido-regional` en paralelo. **Lánzelos en un solo mensaje, antes de
ningún otro encargo**, con la deuda de la 3.2 al frente, la **regla de `site:`** de la 3.1 y **el tope duro
de 2-3 búsquedas por eje**.

**Tres controles que hay que repetir:**

- **Recall genérico por región**: cuando una entidad quede «sin hallazgos», contrastar con consulta sin
  restricción de dominio antes de cerrarla.
- ⚠️ **Recall nacional del coordinador, ANTES de cerrar los barridos.** Décima edición consecutiva.
  **En ARGOS 119 aportó los CUATRO hechos rojos y las dos sentencias.**
- ⚠️ **ARBITRAJE DEL COORDINADOR ENTRE BARRIDOS Y SOBRE SUS EXCLUSIONES.** Ver Bloque 6.

⚠️ **Y REVISE TODA EXCLUSIÓN QUE UN BARRIDO ATRIBUYA A UNA INSTRUCCIÓN SUYA.** **Las prohibiciones de
gasto se redactan contra el PENDIENTE, no contra el TOPÓNIMO.**

⚠️ **Y ARBITRE LAS CLASIFICACIONES QUE PROPONGAN, EN LAS DOS DIRECCIONES.** **Segundo corte consecutivo
en que el coordinador arbitra una clasificación de Sureste, y en direcciones opuestas**: en ARGOS 118
rechazó un **rojo injustificado** (por presencia de AEI en una detención); **en ARGOS 119 rechazó un
AMARILLO injustificado** —Sureste invocó «no se puede determinar quién inició» cuando **tres titulares
independientes lo fijaban** y las fuentes situaban al personal en **recorridos de patrullaje**—.
**El criterio no es la prudencia: es el tipo de evento y quién inició.**

---

## BLOQUE 6 — TRAMPAS YA VERIFICADAS · NO REDESCUBRIRLAS

| Trampa | Control, de coste cero |
|---|---|
| ⚠️ **CITAR UN BOLETÍN NO EQUIVALE A HABERLO EXPLOTADO — trampa NUEVA de ARGOS 119 y la más cara de la edición** | **Dos fichas dieron por «no publicado» un desglose que su propia fuente primaria publicaba**: **Elota** —1 larga, 2 cortas, 8 cargadores, **todos con calibre**— y **León-San Felipe** —tipo de arma y 2 cargadores—. **`procedencia-cifras` lo atrapó.** **+4 armas y +10 cargadores al total nacional.** `ARG-119-FE-005` |
| ⚠️ **UNA PENA CONTRA VARIAS PERSONAS NO SE MULTIPLICA SI EL BOLETÍN NO DICE «A CADA UNO» — trampa NUEVA** | El **comunicado 612/26 de la FGR** dice «19 años, 6 meses y 20 días… **en contra de 4 personas**» y **describe la multa con la misma fórmula, como cantidad única**. **Multiplicar la pena ×4 mientras la multa se cuenta ×1 es una asimetría que el texto no sostiene.** `PENA COMPUESTA — REQUIERE REVISIÓN JURÍDICA` |
| ⚠️ **UNA SUSTITUCIÓN GLOBAL SOBRE EL HTML ENSAMBLADO ALCANZA EL BLOQUE DE DATOS Y EL RENDERIZADOR — trampa NUEVA** | El `sed` del `<title>` **rompió la cadena JavaScript del radar**, y el `sed` `s/ARGOS 118/ARGOS 119/g` **convirtió cuatro referencias legítimas a la edición anterior**. ⚠️ **`gen-movil.py` destapó la primera; `editor-duplicidad`, la segunda.** **Nunca publique el escritorio sin generar la móvil, y revise toda referencia a la edición anterior después de un `sed` global.** `ARG-119-FE-004` |
| ⚠️ **EL ÍNDICE NO CUBRE LAS EDICIONES 88-90 — hallazgo estructural NUEVO** | `indice-arg-id.md` **empieza en `ARG-91-001`**. **Dos deslindes de ARGOS 119 afirmaron «no aparece en ningún corte anterior» y los dos eran falsos.** **Use «no aparece en el índice, que cubre de ARGOS 91 en adelante».** |
| ⚠️ **UN HECHO PUEDE REPUBLICARSE INDEFINIDAMENTE** | El cateo de **«El Maguey»** va por la **TERCERA publicación por tres emisores distintos en tres cortes** —SSP de Michoacán, SEDENA/43.ª Zona Militar, Gabinete de Seguridad federal—. **Las tres veces lo cerró la COLONIA.** **El `grep` por topónimo es permanente, no de una sola vez.** `ARG-119-FE-001` |
| ⚠️ **UNA VENTANA LARGA NO PRODUCE RECUPERACIONES: LAS ABSORBE** | **ARGOS 119 tuvo CERO `-REC-`.** Los hechos que en 26 horas habrían sido recuperación **caen dentro o se resuelven con la marca correcta**: `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE` (Ahuacatlán) y `FRONTERA DE VENTANA — HORA NO FIJADA` (Veracruz). `ARG-119-FE-003` |
| ⚠️ **UN CERO DE UNA EDICIÓN ANTERIOR PUEDE SER FALSO — segunda confirmación** | `ARG-118-ARM-004` registró las armas de Culiacán como `CANTIDAD NO DETERMINADA` y ahora circula un desglose. **No se integra ni se reescribe el archivo, pero el cero se lee como «no publicado».** `ARG-119-FE-002` |
| ⚠️ **HAY DOS FORMAS DE FRONTERA DE VENTANA, Y SE DISTINGUEN POR LA CONSUMACIÓN** | **El criterio es la consumación, no la hora de inicio.** En ARGOS 119: **Veracruz 8-sep** se integró con `FRONTERA DE VENTANA — HORA NO FIJADA` **porque ARGOS 118 no lo vio**; **Ahuacatlán** con `EVENTO ANTERIOR PUBLICADO DURANTE EL CORTE` |
| ⚠️ **AL CITAR UN ARG-ID DEL ARCHIVO, COPIE LA FECHA DEL HECHO, NO LA DE PUBLICACIÓN** | Regla de ARGOS 118, **cumplida en 119**. **El índice fija la fecha del hecho: cópiela de ahí** |
| ⚠️ **El resumidor FABRICA FECHAS y FOLIOS `DPE/…`** | **VEINTITRÉS en seis cortes.** **Cinco nuevos en ARGOS 119**: cuatro en SLP (`DPE/4032`, `4070`, `4071`, `4089`) y uno en Jalisco (`DPE/4073`), **todos sin URL propia**. **Cadena exacta entre comillas; el negativo VENCE** |
| **Día de la semana contra calendario** | Cuesta cero y ha salvado doce ediciones. En ARGOS 119: **8-sep martes, 9 miércoles, 10 jueves, 11 viernes, 12 sábado, 13 domingo** |
| ***Liveblog*** | **Cuatro «EN VIVO … hoy N de septiembre» aparecieron en el recall de ARGOS 119 y NINGUNA se usó para fechar ni como fuente única.** Sirvieron solo para localizar candidatos que después se anclaron |
| **Agregado que no se reparte** | **Cinco casos en ARGOS 119**: Chiapas (1,545 armas en **23 meses**), «Modelo de Seguridad Coahuila», agregado semanal de Sinaloa (**43 AEI**), 43 detenciones en 36 municipios y 30 detenciones de once cateos. **Ninguno se integró** |
| ⚠️ **Corroboración asimétrica** | **El nivel de confianza lo fija el campo PEOR sostenido**, y la marca se aplica al renglón completo |
| ⚠️ **Una reserva de más también es defecto — Y una declaración de más también** | En ARGOS 119, «no procede reserva» en Escuinapa **estaba sobreextendida**: los titulares fijan **10 armas, 1,900 cartuchos y 20 AEI**, **no** los 44 cargadores ni las 13 placas. **Acote el alcance de la declaración a las cifras que realmente cubre** |
| **«Más de» no es cifra** | Dejó fuera **«más de 1,500»** (Cosío), **«más de 5,400»** (Sonora) y **«más de 700»** (Xaltianguis). ⚠️ **Pero NO dejó fuera los 753 de Guanajuato**: el titular decía «más de 750» y **el cuerpo del boletín fijaba 753**. **La regla es sobre la cifra, no sobre el titular** |
| **Cargadores y cartuchos** | **Nunca se suman entre sí.** Ni **5 útiles + 1 percutido** |
| **Un delito y su detención son dos eventos** | ⚠️ **Pero NO se desdobla una secuencia continua sin daño propio consumado.** En ARGOS 119, **Chilpancingo y Elota** son **una sola ficha 🔴 cada una**: la agresión y la respuesta son el mismo acto y **el color lo fija quién inició**. **La regla de las dos fichas es para el delito CONSUMADO con daño propio más la detención posterior** |
| **Sentencia frente a vinculación a proceso** | **Lea el verbo del título** — y compruebe que el título EXISTE |
| **Cifras derivadas** | Todo total que ARGOS calcule es **cálculo propio** y se declara. ⚠️ **Y compruebe la aritmética de TODO cociente.** En ARGOS 119 los seis fueron correctos y se recalcularon tras las correcciones |

---

## BLOQUE 7 — FORMA DEL CARTELÓN

Instrucción editorial permanente del destinatario, vigente:

- ⚠️ **CINCO LÍNEAS. ES LA INSTRUCCIÓN MÁS ESTRICTA.** *«Poco texto, muy ejecutivo. Es para mandos.»*
  **Máximo cinco líneas** en cada **Explotación ARGOS**, en cada recuadro `alerta contexto` y en la
  **Valoración**, numeradas `<b>N. ` **con espacio**. La portada lleva **UN SOLO recuadro**, «LO QUE DEBE
  SABER EL MANDO». **«Hecho confirmado» va en registro telegráfico**, no en prosa.
  ⚠️ **Nunca se recortan cifras, fechas, municipios, corporaciones, ARG-ID, confianza, fuentes, deslindes
  ni marcas de reserva. Se recorta la prosa, no el dato.** **ARGOS 119 lo cumplió en los 24 bloques
  contados.**
- ⚠️ **TRES RECUADROS COMO MÁXIMO EN TODO EL CARTELÓN** —portada, Valoración y Conclusiones—, **y ninguno
  repite el hecho de otro.** ⚠️ **NINGÚN RECUADRO EXPLICA UN COLOR NI UN MECANISMO DEL MÉTODO.**
  **Referencia de volumen: ~38.000 caracteres con cinco hechos.** ⚠️ **ARGOS 119 quedó en ~240.000 bytes
  con DIECINUEVE hechos en once páginas, y está bien que suba: lo que no sube es el texto POR FICHA.**
- **Solo el día.** Las recuperaciones van con ARG-ID `-REC-`, **ventana de origen declarada** y **fuera de
  todos los totales**. ⚠️ **Y un hecho YA PUBLICADO no vuelve como `-REC-`: eso es duplicación.**
- ⚠️ **SIN FE DE ERRATAS EN EL CARTELÓN.** Van al archivo de fuentes y a `_pendientes.md`. El ARG-ID
  `-FE-` **se sigue asignando y registrando en `indice-arg-id.md`**. ⚠️ **Y CUIDADO CON CITAR UN ARG-ID
  `-FE-` DENTRO DE UNA FICHA: en ARGOS 119 se coló uno en el deslinde de Apatzingán y lo atrapó la
  validación automática.** **ARGOS 119 cerró con cinco `-FE-` registrados, cero en el cartelón y cero en
  la móvil.**
- **Sin «Ejes del día» y sin resumen ejecutivo.** ⚠️ **`editor-duplicidad` podría señalar que `CLAUDE.md`
  pide «Ejes del día»: la instrucción del destinatario, posterior y más específica, la retiró y fijó
  «LO QUE DEBE SABER EL MANDO». No la reintroduzca.** **En ARGOS 119 el control ya no la reclamó.**
- **Ningún hecho con ficha propia entra además en una tabla resumen.**
- ⚠️ **No remita a secciones que la edición no tiene.** **No nombre entidades sin ficha ni caso asociado.**
- **Toda cifra en cero lleva al lado el dato que la explica.** **En ARGOS 119: `0 explosivos y
  componentes`, `0 drones armados`, `0 absolutorias` y `0 sentencias firmes`, las cuatro explicadas.**
- **Las categorías en cero se muestran atenuadas: la ausencia es dato.**
- **Sin ARGOS hablando de ARGOS.** ⚠️ **No mida en «ediciones» dentro del cartelón: mida en FECHAS.**
- **Conclusiones de inteligencia criminal**, no de método.
- **Toda tabla envuelta** en `<div class="table-wrap"><table class="exec">…</table></div>`.
- **Nada de `sem-item` fuera de la portada.**
- ⚠️ **Cada sentencia integrada lleva ficha propia.** **ARGOS 119 integró dos y las dos la llevan.**

### Estructura de páginas que hereda ARGOS 120

**Once páginas**, como salió ARGOS 119: portada · crimen organizado (I) a (VI) · armamento · sentencias ·
tabla judicial y cobertura · valoración y conclusiones.
**Si el volumen lo pide, se reparte entre más páginas: nunca se comprime una tarjeta.**

---

## BLOQUE 8 — CONSTRUCCIÓN Y VALIDACIÓN

```bash
# 1. Escritorio: partir de la edición anterior, sustituir CORTE_FECHA, EVENTOS y EVENTOS_ARM.
#    ⚠️ CORTE_FECHA y el <title> del <head> SE HEREDAN y es fácil olvidarlos.
#    ⚠️⚠️ PERO NO LOS SUSTITUYA CON UN sed GLOBAL SOBRE EL HTML ENSAMBLADO.
#       En ARGOS 119, s/<title>[^<]*<\/title>/…/ alcanzó una línea del RENDERIZADOR DEL RADAR
#       y s/ARGOS 118/ARGOS 119/g convirtió CUATRO referencias legítimas a la edición anterior.
#       Sustituya por línea, o revise después TODA referencia a la edición anterior.
#    ⚠️ AL EXTRAER LA PLANTILLA, SON TRES TRAMOS, NO DOS:
#      (a) cabecera hasta la línea anterior a <body>
#      (b) MEXICO_VIEWBOX + MEXICO_PATHS: entre <script> y const CORTE_FECHA
#      (c) desde const REGION_ORDER hasta el final del <script>, SIN las tres últimas
#          líneas (</script></body></html>), que se reponen al ensamblar
#    En ARGOS 119 los tramos fueron: 1-428 · 1219-1253 · 1294-1462 del archivo de ARGOS 118.

# 2. Móvil: NO se escribe, se genera.
python3 tools/gen-movil.py 120 <FECHA> 119 2026-09-13 <HORA>

# 3. La validación debe decir "validación OK" y los contadores deben coincidir
#    con el semáforo del escritorio. Si no, se corrige la HERRAMIENTA, no su salida.
#    ⚠️ Y REGENERE LA MÓVIL DESPUÉS DE CADA CORRECCIÓN DEL ESCRITORIO.
```

⚠️ **EL CORTE DEL BLOQUE DE DATOS VA EN `REGION_ORDER`, NO EN `EVENTOS_ARM`.**

⚠️ **EL CAMPO `region:` SIGUE A `STATE_REGION`, NO AL REPARTO DE BARRIDOS.** **Aguascalientes, Nayarit y
Guanajuato son «Occidente»**; **Zacatecas es «Noreste»**; **Guerrero es «Sureste»**; **Durango es
«Noroeste»**. Un `region:` mal puesto **coloca el eco del radar en el sector equivocado y nadie lo nota**.

⚠️ **CADA ARG-ID DE `EVENTOS` Y DE `EVENTOS_ARM` DEBE TENER UN ANCLA `id=` EN EL DOCUMENTO.**
**En ARGOS 119 los 30 ARG-ID de los dos arreglos resolvieron.**

**Comprobación de coherencia obligatoria** —ARGOS 119 la ejecutó como un script de Python reutilizable—:
extraer el bloque desde `const MEXICO_VIEWBOX` hasta `const SIZE_R`, hacer `node --check`, y validar que
**las doce constantes están presentes**, que **`MEXICO_PATHS` tiene 32 entidades**, que **cada `estado:`
existe**, que **cada `region:` coincide con `STATE_REGION`**, que **ninguna fecha cae fuera de la
ventana**, que **no hay ARG-ID duplicados**, que **cada ARG-ID resuelve a un ancla**, que **el semáforo
derivado coincide con la portada y con `radar-stats`**, que **hay exactamente un `<body>`**, que **toda
tabla está envuelta exactamente una vez**, que **hay cero `-FE-`**, que **`sem-item` solo aparece en
portada**, que **el contador de cinco líneas —`<b>N. ` CON ESPACIO— no supera 5 en ningún bloque**, que
**hay como máximo 3 recuadros**, que **las medidas en «ediciones» dan 0** y que **el pie aparece en todas
las páginas**.

⚠️ **Y RECALCULE EL TOTAL NACIONAL DESDE LAS FILAS INTEGRADAS, no desde el borrador**, **y vuelva a
recalcularlo DESPUÉS de aplicar las correcciones de los controles**: en ARGOS 119 los controles movieron
**+4 armas y +10 cargadores** y hubo que rehacer **seis cocientes, nueve tarjetas y el total**.

**Comprobar antes de publicar**: **exactamente una etiqueta `<body>`** · mismo número de secciones en
ambas versiones · toda tabla envuelta **exactamente una vez** · **cero `-FE-` en ambas** · cero `sem-item`
fuera de portada · cero restos de clases de escritorio en la móvil · **pie con número, fecha y hora en
todas las páginas** · **todos los ARG-ID del escritorio presentes en la móvil** · **cero `map-box`
vacíos** · sin desbordamiento horizontal a 390 px.

*Notas del generador, que NO son defectos*: la móvil **no lleva `<script>`** · **`table-wrap` aparece en
cero** —se renombra a `tabla-scroll`— · **una tabla de más de cuatro columnas se reflúa a
`tabla-tarjetas`**. **Verifíquelo contando ARG-ID, no etiquetas `<table>`.** La móvil lleva **un solo pie**
(`footbar` aparece 3 veces: dos son CSS).

---

## BLOQUE 9 — CONTROLES ANTES DE PUBLICAR

| Control | Qué impide |
|---|---|
| `editor-duplicidad` | Que un hecho ya publicado se presente como nuevo, que dos secciones repitan el mismo párrafo, que se remita a tablas inexistentes, que las casillas no cuadren con las 32 y **que un deslinde afirme algo que el índice no puede sostener** |
| `procedencia-cifras` | Que una cifra sin fragmento citable llegue al cartelón, **que se descarte por precaución una que sí debía integrarse**, **que se marque bajo reserva una que sí está en titular** y ⚠️ **que se dé por «no publicado» un dato que la fuente primaria citada SÍ publica** |
| `barrido-regional` ×6 | Que se declare `SIN ACTUALIZACIÓN` sin haber barrido |

⚠️ **DECIMOCUARTA EDICIÓN CONSECUTIVA CON HALLAZGOS REALES, Y LA PRIMERA EN QUE LOS DOS CONTROLES
DEVOLVIERON `CORREGIR ANTES DE PUBLICAR` CON HALLAZGOS MATERIALES A LA VEZ.**
**El saldo neto fue INTEGRAR: +4 armas y +10 cargadores**, y **retirar un acumulado judicial**.

⚠️ **Cómo usarlos, en las dos direcciones**: un control que dice **«no integrar»** merece **una búsqueda o
un `grep` de arbitraje antes de obedecerlo**, y **un control puede obligar a INTEGRAR o a REFORZAR lo que
el borrador degradó por precaución**. ⚠️ **Y cuando el control declare que NO pudo fijar su hallazgo a un
titular, ARBÍTRELO USTED**: en ARGOS 119 eso localizó **el comunicado n.º 59 de la 13.ª Zona Militar**, que
**corrigió el desglose de Ahuacatlán y subió la fila de Bajo a Medio**.

⚠️ **Lance `editor-duplicidad` DESPUÉS de generar la móvil**, para que pueda auditar la paridad.

⚠️ **Y hay un cuarto control que no es un subagente: el arbitraje del coordinador**, sobre los barridos y
sobre sus propias instrucciones. **En ARGOS 119 evitó un triple conteo, una fusión de dos municipios
homónimos y la subestimación de un ataque contra autoridades.**

---

## BLOQUE 10 — CIERRE DE LA EDICIÓN

1. Actualizar `reports/_pendientes.md`: lo que la edición abre, lo que cierra, la deuda de método.
   ⚠️ **Todo candidato lleva MUNICIPIO y, si se conoce, NOMBRE O ALIAS.**
   ⚠️ **Y todo candidato que la edición evalúe recibe DISPOSICIÓN EXPRESA** —cerrado, sin avance o fuera
   de ventana—.
2. Añadir los ARG-ID nuevos a `reports/indice-arg-id.md` —**incluidos los `-FE-`**—. **Y retirar del
   índice los ARG-ID que se hayan quedado sin usar por una corrección.**
3. **Escribir `reports/_arranque-ARGOS-121.md`** y borrar este archivo.
4. **Mergear a `main`** y verificar que quedó.
