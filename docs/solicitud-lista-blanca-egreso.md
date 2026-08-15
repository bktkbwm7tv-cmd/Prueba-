# Solicitud de ampliación de la lista blanca de egreso — proyecto ARGOS

**Para**: quien administre el entorno de ejecución de Claude Code de este proyecto
**Asunto**: permitir el acceso de salida a portales institucionales del Gobierno de México
**Fecha de la comprobación**: 2026-08-15 (durante la elaboración de ARGOS 98)

---

## Qué se pide

Añadir a la política de red del entorno los dominios institucionales listados abajo, para permitir
únicamente **lectura HTTPS de salas de prensa y boletines públicos**. No se solicita acceso a
ningún sistema interno, autenticado ni de escritura: todo el contenido es material que las
dependencias publican abiertamente en sus sitios oficiales.

## Por qué

ARGOS es un producto de inteligencia criminal cuya regla central es que toda afirmación sea
trazable hasta su fuente documental. `CLAUDE.md` establece un **barrido obligatorio de portales
oficiales** —federales y de las 32 entidades— antes de que cualquier categoría pueda declararse sin
información, precisamente porque los medios publican solo una fracción de lo que las corporaciones
difunden en sus propios canales.

Ese barrido **hoy no puede ejecutarse como está especificado**. La comprobación directa devuelve:

```
$ curl -sS https://www.gob.mx/sspc/prensa
curl: (56) CONNECT tunnel failed, response 403
```

El mismo resultado en `gob.mx/guardianacional/prensa`, `fiscalia.chihuahua.gob.mx` y
`ssp.michoacan.gob.mx`. El estado del proxy no registra fallos de relay
(`recentRelayFailures: []`), lo que confirma que **no es un error técnico ni un problema de los
portales, sino una denegación por política de egreso**: los hosts no están en la lista permitida.

### Efecto medible sobre el producto

- **Nueve ediciones consecutivas** (ARGOS 90 a 98) con techo de confianza ★★★★☆. El nivel ★★★★★ de
  la escala ARGOS exige documento oficial o fotografía verificada; sin lectura directa es
  inalcanzable por definición.
- En ARGOS 98, **cinco equipos de investigación hicieron ~30 intentos de lectura directa y fallaron
  los 30**. Ningún documento primario se leyó íntegro en toda la edición.
- El módulo de armamento tuvo que declarar cobertura parcial explícita (18 de 32 entidades) porque
  el recorrido portal por portal no es viable solo con buscador.
- Una cifra del aseguramiento de Huajicori, Nayarit —«8 cargadores, 235 cartuchos»— se arrastró
  durante **cuatro ediciones** sin poder confirmarse ni desmentirse, hasta que ARGOS 98 tuvo que
  retirarla mediante fe de erratas. Con acceso al boletín original se habría resuelto en minutos.

Ampliar el número de equipos de investigación no corrige nada de lo anterior: multiplica las
peticiones contra la misma restricción. Es un problema de política de red, no de método.

## Dominios solicitados

### Federales

| Dominio | Dependencia |
|---|---|
| `www.gob.mx`, `gob.mx` | Portal único del Gobierno de México (aloja las salas de prensa de SSPC, SEDENA, SEMAR, Guardia Nacional y FGR) |
| `seguridad.sspc.gob.mx` | Gabinete de Seguridad — informes diarios y comunicados conjuntos |
| `fgr.org.mx` y subdominios | Fiscalía General de la República y fiscalías especializadas |
| `anam.gob.mx` | Agencia Nacional de Aduanas — hechos fronterizos y portuarios |
| `www.cjf.gob.mx` | Consejo de la Judicatura Federal — resoluciones publicadas |

### Estatales

El barrido cubre, en cada corte, la secretaría de seguridad y la fiscalía o procuraduría de las 32
entidades. La forma más simple y robusta de autorizarlo es por comodín:

```
*.gob.mx
```

Si se prefiere una lista explícita en lugar del comodín, estos son los dominios que las ediciones
recientes han necesitado y no han podido alcanzar:

```
ssp.michoacan.gob.mx              fiscalia.chihuahua.gob.mx
sspsinaloa.gob.mx                 fiscalia.puebla.gob.mx
fiscaliadejusticia.jalisco.gob.mx fiscalia.durango.gob.mx
fiscaliageneral.cdmx.gob.mx       portal.fgeo.gob.mx
fge.guanajuato.gob.mx             comunicacion.fiscaliaveracruz.gob.mx
poderjudicialmichoacan.gob.mx
```

La lista explícita quedará incompleta: cada corte alcanza entidades distintas según dónde ocurran
los hechos, y varias fiscalías estatales usan dominios propios fuera de `gob.mx`. Por eso se
recomienda el comodín.

## Alcance y garantías

- **Solo lectura.** El uso es `GET` sobre salas de prensa y boletines públicos.
- **Sin credenciales.** Ningún portal de los listados requiere autenticación para el material que
  ARGOS consulta.
- **Sin datos personales fuera de lo ya publicado.** ARGOS reproduce únicamente lo que la autoridad
  difunde, y el propio `CLAUDE.md` prohíbe publicar identificaciones que la fuente no haya hecho
  públicas de forma trazable.
- **Auditable.** Cada edición conserva en su archivo `-fuentes.md` qué portal se consultó, cuál
  respondió y cuál no, de modo que el uso del acceso quede registrado corte a corte.

## Cómo se configura

La política de red se elige al crear el entorno de ejecución remota. La documentación está en
<https://code.claude.com/docs/en/claude-code-on-the-web>. Si la política vigente es una lista
blanca estricta, basta con añadir los dominios anteriores; si existe un perfil más amplio
compatible con las normas de la organización, también resolvería el caso.

## Qué cambia si se aprueba

1. El barrido obligatorio de `CLAUDE.md` pasa a ser ejecutable tal como está escrito, en lugar de
   sustituirse sistemáticamente por búsqueda indirecta.
2. El techo de confianza del producto sube de ★★★★☆ a ★★★★★ en los hechos que cuenten con boletín
   oficial leído.
3. Los `SIN DATO` pasan a significar «la autoridad no publicó», que es información de inteligencia
   real, en lugar de «no se pudo consultar», que no lo es.
4. Las contradicciones de cifras entre medios se resuelven contra el comunicado original, como ya
   ocurrió con el cateo de Ciudad Juárez del 13 de agosto: el único caso reciente que pudo cerrarse,
   y solo porque el boletín de la Fiscalía de Chihuahua estaba indexado por casualidad.

---

**Nota operativa**: mientras la restricción siga vigente, el procedimiento correcto es registrar el
host bloqueado y anotar la sustitución por búsqueda dirigida, sin intentar rodear la política. Así
está fijado en `CLAUDE.md`, sección «Restricción de acceso vigente».
