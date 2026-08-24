# PENDIENTE — Integración del barrido en ARGOS 88

Estado: **barrido COMPLETO** (3 agentes). Sentencias ya integradas al cartelón. Falta armamento,
eventos rojos, semáforo y versión móvil.

Corte: **2026-08-04 (ARGOS 88)** · Rama: `claude/argos-criminal-intelligence-otiawj`

> **Estado de git al abrir la sesión nueva:** el PR #7 ya fue **mergeado y cerrado**, y todo el
> trabajo previo (CLAUDE.md, ARGOS 86/87/88, versión móvil, sentencias del barrido) está en `main`.
> Un PR mergeado no puede seguir recibiendo trabajo: el trabajo pendiente descrito abajo va en una
> rama reiniciada desde `main` (`git fetch origin main && git checkout -B
> claude/argos-criminal-intelligence-otiawj origin/main`) y, si se pide PR, será **uno nuevo**, no
> el #7. No reabrir el #7.

---

## ⚠ HALLAZGO CRÍTICO — la conclusión publicada de ARGOS 88 es FALSA

El reporte está publicado diciendo **"CERO eventos rojos"** y **"Nivel de riesgo MEDIO"**. El barrido
federal localizó al menos **tres eventos de alto impacto** dentro del periodo, todos con fuente
institucional (boletines del Gabinete de Seguridad del 3-ago-2026):

### R1 — Ataque armado contra la Guardia Nacional · Tula, Hidalgo · 3-ago-2026
- 2 elementos de la GN heridos por proyectil de arma de fuego (emboscada repelida).
- Asegurado: 2 armas cortas, 2 cargadores, 1 granada de humo.
- **Contradicción de detenidos:** el Gabinete de Seguridad reporta **4**; El Universal, Excélsior,
  Diario de Yucatán y Tribuna reportan **3**. Documentar ambas sin resolver.
- Fuentes: Talla Política (reproduce boletín); El Universal
  `eluniversal.com.mx/estados/dos-agentes-de-la-gn-resultan-heridos-tras-ataque-armado-en-tula-hidalgo-tres-agresores-fueron-detenidos/`;
  Excélsior `excelsior.com.mx/nacional/repelen-emboscada-tula-hay-2-guardias-nacionales-heridos-y-3-detenidos`;
  Diario de Yucatán; Tribuna.
- **Clasificación: 🔴 ROJO** — ataque contra autoridades (categoría explícita de alto impacto).

### R2 — Ataque armado contra el Ejército · Joaquín Amaro (Mesa de Palmira), Zacatecas · 3-ago-2026
- Operación SAGAZ. 1 agresor abatido; 2 menores detenidas (14 y 17 años, originarias de Durango).
- Asegurado: 1 vehículo con blindaje artesanal, armas, cartuchos y equipo táctico **sin cifra**.
- Fuentes: NTR Zacatecas `ntrzacatecas.com/2026/08/detienen-a-dos-menores-tras-agresion-en-mesa-de-palmira/`;
  Imagen Zacatecas `imagenzac.com.mx/seguridad/abaten-a-presunto-agresor-y-detienen-a-dos-menores-en-joaquin-amaro`;
  Periódico Mirador.
- **Clasificación: 🔴 ROJO** — ataque contra autoridades, con persona abatida.

### R3 — Enfrentamiento con policías y 5 presuntos sicarios muertos · Zacatecas · 2-ago-2026
- Detectado tangencialmente, **sin procesar**. Requiere verificación propia antes de integrar.
- Fuente: Calibre 800 `calibre800.com/2026/08/02/mueren-policias-y-5-sicarios-en-enfrentamiento-en-zacatecas/`
- **Clasificación probable: 🔴 ROJO** (enfrentamiento con víctimas mortales, incluidas fuerzas del
  Estado) — confirmar número de policías fallecidos antes de publicar.

**Consecuencia:** la tarjeta `ARG-88-007` de la página 3 dice "ATAQUES A AUTORIDADES / FOSAS
CLANDESTINAS — SIN DATO". Es falso: R1 y R2 son exactamente eso. Hay que sustituirla por tarjetas
reales, recalcular el semáforo, rehacer el `EVENTOS`, re-hornear radar y mapas, y reescribir
Valoración y Conclusiones de la página 7.

---

## 1. ARMAMENTO — 13 eventos verificados (la página 5 dice SIN DATO)

ARG-ID reasignados para evitar colisión entre agentes (Michoacán usaba 001-002; el federal también).

| ARG-ID | Entidad | Municipio | Fecha | Corta | Larga | Carg. | Cartuchos | Gran. | Detenidos | Corporación | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARM-001 | Michoacán | Queréndaro (Pueblo Viejo) | 3-ago | — | 2 | n/d | n/d | — | 0 | GN+Ejército+Guardia Civil | Alto |
| ARM-002 | Michoacán | Buenavista (Tescalame) | 4-ago | 1 | 1 | 4 | 9,939 | — | 0 | Ejército | Medio |
| ARM-003 | Chiapas | Benemérito de las Américas | 31-jul/2-ago | — | 1 | 11 | 340 | — | n/d | GN+Ejército | Medio |
| ARM-004 | Durango | San Dimas | 31-jul/2-ago | — | 2 | 18 | 536 | — | n/d | GN+Ejército | Medio |
| ARM-005 | Guerrero | Chilpancingo (Santa Bárbara) | 31-jul/2-ago | — | 3 | 13 | 566 | — | **7** | GN+Ejército+Pol. Estatal | Alto |
| ARM-006 | Jalisco | no especificado | 31-jul/2-ago | 2 | — | 2 | 15 | — | **1** | Gabinete (conjunto) | Medio |
| ARM-007 | Jalisco | Valle de Guadalupe | 31-jul/2-ago | — | 3 | 17 | ~1,000 | — | n/d | GN+Ejército | Medio |
| ARM-008 | Querétaro | dos inmuebles, mun. n/e | 31-jul/2-ago | 1 | 2 | 4 | 152 | — | **7** | Ejército+FGE+Pol. Est./Mpal. | Alto |
| ARM-009 | Sonora | Cajeme (col. Cortinas) | 31-jul/2-ago | 3 | 2 | 7 | 61 | — | **3** (1 menor) | Ejército+SEMAR+GN+FGE | Bajo |
| ARM-010 | Sinaloa | no determinado | 31-jul/2-ago | — | 2 | 25 | 2,047 | — | n/d | SEMAR | Medio |
| ARM-011 | Sinaloa | Concordia (av. A. López Mateos) | 3-ago | — | 4 | 19 | 573 | — | n/d | Ejército | Medio |
| ARM-012 | Sonora | no determinado | 3-ago | — | — | — | 1,399 | — | n/d | Ejército | Medio |
| ARM-013 | Durango | Victoria de Durango (Práxedis G. Guerrero Nuevo) | 3-ago | — | 1 | 22 | 411 | **3** | n/d | FGR (FECOR) + GN/SEDENA perímetro | Alto |

**ARM-007 (Valle de Guadalupe) derivó de un ENFRENTAMIENTO** → en el mapa de aseguramientos Jalisco
va **AMARILLO**, no verde (regla del mapa: amarillo = aseguramiento derivado de
enfrentamiento/agresión/topón).

**Armamento especial:** ARM-007 incluye **1 fusil Barrett + 1 ametralladora + 1 vehículo con
blindaje artesanal**. ARM-012 incluye **14 eslabones/cintillos metálicos para ametralladora** sin
arma asociada (evento cualitativo respecto al arma).

### TOTALES NACIONALES DEL CORTE

| Categoría | Total |
|---|---|
| Armas cortas | **7** |
| Armas largas | **23** |
| Cargadores | **142** |
| Cartuchos útiles | **17,039** |
| Granadas (sin clasificar) | **3** |
| AEI | 0 verificados en el periodo |
| Explosivos/componentes | Sin dato verificable |
| Armamento especial | 1 Barrett · 1 ametralladora · 1 vehículo blindado artesanal · 14 eslabones |
| Personas detenidas (en evento de aseguramiento) | **18** (Guerrero 7 + Querétaro 7 + Cajeme 3 + Jalisco 1) |
| Estados con aseguramientos | **8** (Michoacán, Chiapas, Durango, Guerrero, Jalisco, Querétaro, Sonora, Sinaloa) |
| Eventos contabilizados | 13 |
| Eventos cualitativos | Queréndaro (carg./cart. sin cifra) · Quintana Roo (6 cateos sin desglose) |

Verificación aritmética: cartuchos 9,939+340+536+566+15+1,000+152+61+2,047+573+1,399+411 = 17,039 ·
cargadores 4+11+18+13+2+17+4+7+25+19+22 = 142 · largas 2+1+1+2+3+3+2+2+2+4+1 = 23 · cortas 1+2+1+3 = 7.

**Nota sobre cartuchos:** los ~1,000 de Valle de Guadalupe tienen discrepancia entre fuentes
(1,000 en La Jornada vs 1,001 en Notisistema). Se usa 1,000 y se documenta.

### Fuente dominante
Dos boletines conjuntos del Gabinete de Seguridad ("31 jul, 1 y 2 ago" y "3 ago"), reproducidos por
**La Jornada** (`jornada.com.mx/2026/08/04/politica/011n3pol`) y **Talla Política**
(`tallapolitica.com.mx/gabinete-de-seguridad-...`), más el cateo autónomo de FGR en Durango
(Excélsior `excelsior.com.mx/nacional/fgr-asegura-granadas-arma-larga-y-cartuchos-cateo-durango`).

### Cualitativos y exclusiones
- **Quintana Roo**, 3-ago: seis cateos simultáneos (Othón P. Blanco, Bacalar, Benito Juárez, Puerto
  Morelos) con "municiones, cargadores, cañones y piezas de armas" **sin cifra**. Contradicción de
  detenidos: Posta reporta 5; 24 Horas QRoo describe un hecho separado con 4. No integrar al total.
- **Veracruz**, Tuzamapan: 1.5 millones de litros de huachicol, 49 contenedores, 1 detenido →
  corresponde al módulo de huachicol (`ARG-88-008`, hoy en SIN DATO), no a armamento.
- **Zacatecas / GN "armas largas, cartuchos y cargadores"**: el comunicado existe pero los fragmentos
  citan el "Plan Nacional de Paz y Seguridad 2018-2024" — indicio de que es de 2021-2023.
  **NO INTEGRAR** sin verificar fecha manualmente.

---

## 2. SENTENCIAS — YA INTEGRADAS al cartelón (falta móvil)

12 sentencias, 14 personas, ≈540 años, reparación $4,198,585, 5 fiscalías estatales + FGR.
Nuevas: SEN-003/004/005 (Chihuahua), 006 (Sonora), 007 (Coahuila-FGR), 008 (Querétaro),
009 (Quintana Roo), 010 (CDMX), 011 (Oaxaca, 140 años), 012 (Tlaxcala-FGR).
Cobertura: 32 de 32 fiscalías consultadas; 6 portales con 403.
No integradas: Guanajuato (ratificación en apelación, no sentencia nueva) y Zacatecas (fecha sin
confirmar).

---

## 3. QUERÉNDARO — bloqueante RESUELTO

Eran **tres hechos distintos**. Solo el del **3-ago (Pueblo Viejo)** cae en el corte, **sin
agresión** → **VERDE**. Los de "2 detenidos" y "repelen agresión" son del 5-jun y 16-jun de 2026,
fuera del corte.

## 4. MICHOACÁN — AEI: sin evento en la ventana

Las cuatro pistas resultaron fuera de fecha (granada→Cotija oct-2025; La Huacana→mar-2026;
Erongarícuaro→17-jul-2026; explosivos El Cansangue→anterior). Los 625 AEI de Apatzingán son
acumulado nov-2025/jun-2026 → candidato a **Indicador oficial** en página 7, no a evento del corte.
**Trampa evitada:** la nota "54 armas decomisadas en agosto" es de agosto de **2025**.

---

## 5. QUÉ FALTA HACER

1. **Página 3** — sustituir `ARG-88-007` ("ATAQUES A AUTORIDADES / FOSAS — SIN DATO") por tarjetas
   reales de Tula (R1) y Joaquín Amaro (R2). Verificar R3 antes de integrarlo.
2. **Página 5** — reemplazar todo el SIN DATO por los 13 eventos, los totales y la tabla nacional.
   Jalisco en amarillo en el mapa de aseguramientos.
3. **Página 1** — semáforo: ya no es 0/1/3. Recalcular con los rojos.
4. **`EVENTOS`** (línea ~1212 del cartelón) — añadir los rojos y los aseguramientos; **re-hornear**
   radar, `argos-map` y `argos-map-arm`.
5. **Página 7** — Valoración: el nivel de riesgo deja de ser MEDIO. Conclusiones y "Fuentes
   consultadas" también. Añadir los 625 AEI como indicador oficial.
6. **Versión móvil** — replicar todo (sentencias incluidas, que aún no se tocaron ahí).
7. **`argos-2026-08-04-fuentes.md`** — registro completo del barrido y de los portales con 403.

### Portales que devolvieron 403 (para el indicador de cobertura)
`gob.mx/guardianacional/prensa`, `gob.mx/sspc`, `seguridad.sspc.gob.mx`,
`gabinetedeseguridad.gob.mx`, `ssp.zacatecas.gob.mx`, `zacatecas.gob.mx`,
`fiscalia.chihuahua.gob.mx`, `poderjudicialmichoacan.gob.mx`, `fiscaliamorelos.gob.mx`.
SEDENA: sin comunicado propio distinto del boletín conjunto en el periodo.
ANAM/Aduanas: consultado, sin eventos en el periodo.

### Cómo editar sin quemar contexto
`grep -n` con rangos; **nunca** `Read` del archivo completo (la geometría de México está repetida 4
veces). Líneas: cartelón — pág. 5 en ~851, Bloque 1 en ~867, Bloque 3 en ~899, tabla en ~905,
`EVENTOS` en ~1212. Móvil — sección 5 en ~698, sección 6 en ~755.
