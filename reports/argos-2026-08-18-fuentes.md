# ARGOS 101 — Registro de fuentes (auditoría)

Corte: 2026-08-18 · Ventana de hechos: **2026-08-17 02:47 CDMX → 2026-08-18 13:37 CDMX**.
Continuación de ARGOS 100 (corte 2026-08-17). Este documento respalda `argos-2026-08-18.html` y
`argos-2026-08-18-movil.html`, y existe para que todo `SIN DATO` de la edición sea demostrable.

Ventana efectiva: **~35 horas**, de la madrugada del lunes a la tarde del martes. Es más larga que
la de ARGOS 100 (~19 h) porque el corte se toma en continuidad estricta desde el cierre de la
edición anterior y el de hoy se levanta a media tarde. Esa diferencia de duración es relevante para
comparar volúmenes entre ediciones y se hace explícita en el producto: **un corte con más hechos que
el anterior no indica por sí mismo más violencia, sino una ventana casi el doble de larga.**

---

## Limitación metodológica — séptima edición consecutiva con el egreso bloqueado

**Sonda de entorno ejecutada al inicio de la sesión por el coordinador**, con `curl` directo contra
cuatro hosts de control:

| Host | Resultado |
|---|---|
| `www.gob.mx/guardianacional/prensa` | 403 al CONNECT |
| `fiscalia.chihuahua.gob.mx` | 403 al CONNECT |
| `www.eluniversal.com.mx` | 403 al CONNECT |
| `es.wikipedia.org` | 403 al CONNECT |

El registro del propio proxy lo confirma textualmente: `gateway answered 403 to CONNECT (policy
denial or upstream failure)`. **El bloqueo es total y no se limita a `*.gob.mx`**: alcanza a medios
nacionales y a dominios de control ajenos al caso. Es una política de la organización y no se
intentó rodearla.

**Consecuencia operativa aplicada**: se prohibió `WebFetch` a los seis equipos regionales y a los
dos de verificación prioritaria, conforme a la lección 3 de ARGOS 100.

**Cero portales leídos por acceso directo, de ~128 objetivo, en las seis regiones.** Ningún
`SIN ACTUALIZACIÓN OFICIAL DURANTE EL CORTE` de esta edición puede presentarse como vacío
institucional verificado. **Techo de confianza efectivo: ★★★☆☆ para todos los hechos de la
ventana** — duodécima edición consecutiva sin superar ★★★★☆.

---

## Verificación PRIORIDAD 1 — ejecutada primero y en solitario

Se aplicó la lección 1 de ARGOS 100: la verificación prioritaria se ejecutó **antes de lanzar los
seis barridos y con la sesión para ella sola**, de modo que su cuota no dependiera de lo que
consumieran las regiones. Consumo: **26 búsquedas de 26 asignadas** (12 + 14), ambos equipos con el
tope agotado.

**Resultado de conjunto: ninguno de los dos pendientes de PRIORIDAD 1 pudo cerrarse.** A diferencia
de ARGOS 100 —donde la verificación prioritaria desmontó dos hechos falsos—, aquí el rendimiento fue
bajo en cierres y alto en **delimitación**: lo que aporta esta edición es saber con precisión qué es
lo que bloquea cada caso, y descartar tres candidatos que habrían entrado como hallazgos falsos.

### Suchiapa, Chiapas — Bulmaro "N": la contradicción de fecha NO se arbitra

- **Veredicto: fecha del hecho NO DETERMINADA CON AUTORIDAD.** Se ejecutaron búsquedas dirigidas a
  `ssp.chiapas.gob.mx` y `fge.chiapas.gob.mx` sin localizar **ningún boletín institucional sobre este
  hecho**. Sin boletín, no hay nada que arbitre entre las dos URLs.
- Lo único disponible siguen siendo **fechas de publicación**: El Heraldo de México fecha en URL
  `2026/8/15`; Infobae, `2026/08/16`. Por la regla de primera publicación, la fecha más probable del
  hecho es el **15-ago**, pero eso es una **inferencia sobre la fecha de publicación**, no una fecha
  de hecho confirmada. Grado de certeza: bajo/medio.
- **Conclusión operativa: se mantiene exactamente el tratamiento de ARGOS 100.** Sigue siendo
  **candidato a omisión de ARGOS 99**, no corrección confirmada. **Bajo ninguno de los dos
  escenarios de fecha (15 o 16-ago) el hecho cae en la ventana de ARGOS 101**, de modo que no suma a
  ningún total de este corte. Se publica como ficha de recuperación, sin integrarse.
- **Desglose de armamento, confirmado y consistente entre seis fuentes**: 1 arma corta calibre 9 mm,
  **2 cargadores**, **32 cartuchos útiles** —contabilizados por separado, nunca sumados—, 15
  envoltorios de presunta cocaína tipo crack, chaleco balístico, funda y un vehículo. Un solo
  detenido. **No determinado**: el monto del efectivo asegurado y la hora del hecho.
- **Elemento de mayor valor de inteligencia, confirmado por todas las fuentes**: el uniforme
  **clonado** de la Fuerza de Reacción Inmediata Pakal (FRIP) con **insignias apócrifas**.
- Confianza: **★★★☆☆ / Bajo**. Sin fuente institucional, la escala no permite subir.
- **Deslinde obligatorio anotado para ediciones futuras**: el barrido tropezó con un resultado de
  `ssp.chiapas.gob.mx` sobre una orden de aprehensión contra un servidor público por abuso de
  autoridad en **Cintalapa de Figueroa**, que es un **caso distinto**, y con un tercer caso —también
  distinto y mucho mayor— de cateos en Suchiapa con 26 detenidos (ver la ficha del barrido Sureste).
  Tres hechos separados, dos de ellos en el mismo municipio y ambos con el tema de uniformes y
  usurpación de funciones de por medio: **no fusionarlos por topónimo.**

### Veracruz — las nueve condenatorias del agregado del 13-ago: cero desglosadas

- **Resultado: 0 de las 9 condenatorias pendientes pudieron desglosarse** con datos mínimos
  suficientes. **No se localizó el listado nominal íntegro de las 53 resoluciones.** Cuarta edición
  consecutiva con el pendiente abierto.
- **Lo que sí se corroboró**: el agregado del **13-ago-2026** existe y está fijado por **dos fuentes
  con fecha en URL** —`lapoliticaenrosa.com/2026/08/13/…` y `golpepolitico.com/2026/08/13/…`—.
  Desglose citado: **11 sentencias condenatorias, 42 vinculaciones a proceso, 18 imputaciones, 13
  órdenes judiciales cumplimentadas, 10 detenciones en flagrancia, 1 persona localizada**, presentado
  por la Fiscal General Lisbeth Aurelia Jiménez Aguirre en la COESCONPAZ. Distribución regional
  citada, sin desglose caso por caso: Tantoyuca, Córdoba, Cosamaloapan, Veracruz, Xalapa,
  Coatzacoalcos y Tuxpan.
- **Cosamaloapan sigue siendo la única documentada** (`ARG-100-SEN-SEG-001`, ARGOS 100). Se
  reencontró y **no se republica como hallazgo nuevo**, conforme a la regla de deduplicación.

**Dos candidatos descartados — habrían entrado como hallazgos falsos:**

| Candidato | Por qué se descarta |
|---|---|
| **"Condenas de hasta 350 años"** — Miguel "N" y Andrés Emiliano "N", Fiscalía Regional de Tuxpan, secuestro agravado de 7 personas migrantes (3 menores), hechos del 17-jun-2023, juicio oral J-04/2024 | El título institucional indexado en `comunicacion.fiscaliaveracruz.gob.mx` **no lleva fecha en el slug** (caracteres unicode decorativos, sin `/2026/08/`), así que no puede fecharse con el método exigido. La única fuente con indicio de fecha (`laopinion.net`) lo sitúa en **junio de 2026**, dos meses fuera de ventana |
| **Córdoba / Poza Rica** — Pedro "N" (110 años); Jorge Alberto "N" y Roberto "N" (50 años), secuestro agravado | Coincide en **cifras exactas** con `lapoliticaenrosa.com/2026/08/05/…`, fechado en URL el **5-ago-2026**, que corresponde a un **agregado distinto: 32 resoluciones, no 53**. Pertenece al lote del 5-ago |

### Señuelo estructural nuevo, tipificado en esta edición

El título institucional **"Condenas de hasta 350 años y 53 resoluciones judiciales"** combina la
cifra de un lote (53, del 13-ago) con una **pena que pertenece a un caso de dos meses antes**. No es
un error del buscador: es la forma en que la propia Fiscalía redacta sus agregados.

> **Regla de método que deja ARGOS 101**: nunca aceptar una **pena destacada en el titular de un
> agregado** sin una URL fechada que ate esa pena específicamente a ese corte. Un agregado puede
> reutilizar cifras históricas en su encabezado sin dejar de ser veraz.

Se confirma además el **patrón de boletín acumulativo rotativo** de la FGE Veracruz: los medios
regionales publican agregados solapados —22, 24, 32, 36, 37, 40, 44, 48, 51, 69 y 78 resoluciones en
fechas distintas de 2026—, lo que vuelve **estructuralmente difícil** aislar los 11 casos de un solo
corte de 24 h sin acceso directo al boletín fuente.

---
