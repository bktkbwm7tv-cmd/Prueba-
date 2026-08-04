# PENDIENTE — Barrido de armamento y sentencias para ARGOS 88

Nota de traspaso entre sesiones. Léela completa antes de tocar nada; está escrita para que no
necesites abrir los reportes enteros (pesan mucho por la geometría SVG repetida).

Corte afectado: **2026-08-04 (ARGOS 88)** · Rama: `claude/argos-criminal-intelligence-otiawj`

---

## 1. El problema

Las páginas 5 (Armamento) y 6 (Sentencias) de ARGOS 88 se cerraron en `SIN DATO` apoyándose casi
solo en medios nacionales, **sin consultar las salas de prensa institucionales**. Ya está
comprobado que ese vacío es falso: sí hay aseguramientos publicados en el periodo.

La regla que lo prohíbe ya quedó asentada en `CLAUDE.md`, sección **"Barrido obligatorio de
portales oficiales"** (léela primero: es la que gobierna este trabajo).

---

## 2. Lo ya verificado — no repetir esta búsqueda

### Dentro del periodo del corte (1–4 ago 2026)

**Queréndaro, Michoacán — 3 de agosto de 2026.** Guardia Civil + Ejército Mexicano, comunidad de
Pueblo Viejo. Camioneta con reporte de robo; en su interior **2 fusiles**, cargadores y cartuchos
útiles (sin cifra publicada) y equipo táctico incinerado en el sitio. Armamento, municiones y
vehículo a disposición de la autoridad competente.

- Institucional: `gob.mx/guardianacional/prensa` → "En Michoacán, Guardia Nacional y Ejército
  Mexicano y Guardia Civil aseguran camioneta con material bélico"
- Regional: `atiempo.mx/justicia/aseguran-vehiculo-robado-y-armamento-en-querendaro/`
- Conteo: 2 armas largas SUMABLES · cargadores y cartuchos NO determinados (evento cualitativo)

> **⚠ BLOQUEANTE SIN RESOLVER.** Hay notas de un **enfrentamiento armado en Queréndaro con 2
> detenidos** en fechas cercanas (Quadratín Michoacán, Respuesta Michoacán, Atiempo: "Fuerzas de
> seguridad repelen agresión y aseguran material bélico en Queréndaro"). **Antes de integrar hay
> que determinar si es el mismo hecho.** Si lo es, la clasificación deja de ser VERDE y pasa a
> AMARILLO, lo que cambia el semáforo del corte, el radar, los dos mapas y la Valoración de la
> página 7. No integrar hasta resolverlo.

### Fuera del periodo — contexto, no eventos del corte

- **Concordia, Sinaloa — 28 de julio de 2026** (anterior al corte): 3 fusiles AK-47 7.62×39,
  **30 cargadores**, **3,359 cartuchos** 7.62×39, equipo táctico. Grupo interinstitucional
  (Ejército, GN, SEMAR, SSPC, FGR, FGE y Policía Estatal Preventiva), campamento en brechas cerca
  de Chupaderos. Solo entra si se confirma que se **publicó** dentro del periodo, y entonces como
  `Evento anterior publicado durante el corte`.
- **625 AEI localizados y desactivados en la región de Apatzingán, nov-2025 a jun-2026** (SEDENA,
  Gral. Trevilla). Mayoría minas antipersonal y artefactos adaptados para lanzarse desde dron, en
  El Alcalde y El Guayabo. **No es evento del corte**: es candidato a *Indicador oficial* en la
  página 7.
- Nuevo Parangaricutiro (AEI desactivado por la Unidad Especializada en Artefactos Explosivos y
  Materiales Peligrosos de la Guardia Civil): diciembre 2025. Fuera.

### Ya reportado en ediciones previas — NO reciclar

- San Luis Río Colorado, Sonora (81 armas largas, 274,800 cartuchos, 128 cargadores, 25-jul-2026)
  = `ARG-86-ARM-001`.
- "Don Checo", Edomex (armas sin cantidad especificada, 30-jul-2026) = `ARG-87-ARM-001`.

---

## 3. Pistas abiertas con fecha SIN confirmar

Todas salieron en búsqueda pero no se verificó si caen en el periodo:

| Pista | Fuente | Por qué importa |
|---|---|---|
| "En Michoacán, GN y Ejército aseguran fusiles, cargadores, cartuchos **y granada**" | `gob.mx/guardianacional/prensa` | Alimentaría la categoría *Granadas*, vacía en toda la serie |
| "En Michoacán, GN y Ejército **localizan explosivos improvisados**" | `gob.mx/guardianacional/prensa` | Categoría *AEI*, vacía en toda la serie |
| "En La Huacana, fuerzas estatales y federales aseguran **siete fusiles** y equipo táctico" | `ssp.michoacan.gob.mx` | Portal estatal, desglose numérico |
| "En Zacatecas, GN y Ejército aseguran armas largas, cartuchos útiles y cargadores" | `gob.mx/guardianacional/prensa` | Desglose por categoría |
| Erongarícuaro: camioneta abandonada con armas, droga y equipo táctico | `mimorelia.com` | Verificar fecha y si hay desglose |
| Concordia: vehículo con blindaje artesanal, 1 cargador, 160 cartuchos | `cafenegroportal.com` | *Armamento especial* + munición |

---

## 4. Hallazgo metodológico que ahorra tiempo

`gob.mx/guardianacional/prensa`, `ssp.michoacan.gob.mx`, `sspsinaloa.gob.mx` y
`seguridad.sspc.gob.mx` **sí son alcanzables por buscador**. La sala de prensa de la Guardia
Nacional publica por entidad y con desglose numérico por categoría — es la fuente más productiva
para esta sección y debe barrerse primero.

`WebFetch` devuelve HTTP 403 en la mayoría de dominios de medios (bloqueo anti-bot de los sitios,
no falla del proxy). Trabajar con fragmentos de `WebSearch` y anotar qué no se pudo leer completo.

---

## 5. Plan sugerido

**Barrido con agentes** (uno por bloque, en paralelo; cada uno trabaja en su propio contexto):

1. Federal — GN, SEDENA, SEMAR, FGR, SSPC/Gabinete, Aduanas.
2. Michoacán a fondo — AEI, explosivos, drones armados, granadas + resolver el bloqueante de
   Queréndaro.
3. Estatales norte/noroeste/noreste — 12 entidades.
4. Estatales centro/occidente/golfo/sur — 19 entidades (sin Michoacán).
5. Sentencias — FGR + las 32 fiscalías, una por una (`CLAUDE.md`, Sección 2, "Barrido
   obligatorio").

A cada agente hay que pasarle: taxonomía de 7 categorías sin mezclar, cartuchos y cargadores
**nunca** sumados entre sí, solo cifras expresamente publicadas, "diverso armamento" = evento
cualitativo fuera del total numérico, deduplicación por fecha/municipio/corporación/cantidad, y
distinción entre fecha del hecho, de publicación y de consulta.

**Después del barrido:** verificar con `verificador-hechos` antes de integrar.

---

## 6. Dónde editar (para no abrir los archivos completos)

Usa `grep -n` con rangos; **no** hagas `Read` del archivo entero (la geometría SVG de México está
repetida 4 veces por archivo e inunda el contexto).

**`reports/argos-2026-08-04.html`** (cartelón, 7 páginas)

| Qué | Línea aprox. |
|---|---|
| Página 5 — encabezado | 851 |
| Bloque 1 — Total nacional (8 tarjetas, hoy S/D) | 867 |
| Bloque 2 — Mapa de aseguramientos | 883 |
| Bloque 3 — Evento cualitativo (hoy placeholder) | 899 |
| Tabla nacional de aseguramientos (hoy placeholder) | 905 |
| Página 6 — Bloque 4, tarjetas de sentencias | 935 |
| Bloque 5 — Tabla jurídica | 1020 |
| Indicador de cobertura | 1058 |
| `const EVENTOS` (re-hornear si cambia el semáforo) | 1212 |

**`reports/argos-2026-08-04-movil.html`** (móvil, mismas secciones)

| Qué | Línea aprox. |
|---|---|
| Sección 5 — Armamento | 698 |
| Bloque 1 | 711 |
| Bloque 3 | 741 |
| Sección 6 — Sentencias | 755 |
| Bloque 4 | 766 |
| Bloque 5 — Tabla jurídica | 851 |

**Si cambia `EVENTOS`** (p. ej. Queréndaro pasa a amarillo) hay que **re-hornear los SVG**: los
mapas y el radar están pre-renderizados en el HTML para que se vean sin JavaScript (Vista Rápida de
iOS). El guion de horneado y el de ensamblado de la versión móvil quedaron en el scratchpad de la
sesión anterior; si ya no existen, hay que rehacerlos con Playwright leyendo `.innerHTML` de
`#argos-map`, `#argos-radar`, `#argos-radar-stats` y `#argos-map-arm`, y para el móvil envolver los
estados coloreados en `<a href="#ARG-ID">`.

Los dos archivos deben quedar **consistentes entre sí**: mismos ARG-ID, mismas cifras, mismo
semáforo.

---

## 7. Al terminar

- Actualizar también `reports/argos-2026-08-04-fuentes.md` con los enlaces exactos y el registro
  del barrido (qué portales se consultaron, cuáles publicaron, cuáles no, cuáles no estuvieron
  disponibles).
- El Indicador de cobertura de la página 6 debe reflejar el número **real** de fiscalías revisadas.
  Una fiscalía no consultada se reporta como *no revisada*, nunca como *sin actualización*.
- Verificar render con Playwright: sin errores de JS, sin desborde horizontal en móvil (375/393/412
  px) y con los SVG visibles con JavaScript desactivado.
- Commit y push a la rama; el PR #7 lo recoge automáticamente.
