# ARGOS FORENSE

Plataforma web de rastreo nacional OSINT en México sobre tres categorías:

1. **Fosas clandestinas**
2. **Campamentos vinculados públicamente con delincuencia organizada**
3. **Casas de seguridad**

Trabaja con **cortes históricos cada 72 horas**, mantiene trazabilidad completa
y no sobrescribe registros históricos.

> **ARGOS FORENSE no es un agregador de noticias.** Convierte publicaciones
> dispersas en **eventos únicos, corroborados, trazables y comparables en el
> tiempo**. Prioriza calidad, trazabilidad, corroboración, deduplicación e
> integridad histórica por encima del volumen.

## Las tres reglas que gobiernan el sistema

1. **Nada detectado llega solo al registro definitivo.** El rastreo deja los
   hallazgos en la bandeja de validación; el folio forense se emite al validar,
   y lo emite una persona.
2. **Nada se borra.** Los registros cambian de estado —ACTIVO, DESCARTADO,
   DUPLICADO, FUSIONADO, ACTUALIZADO— y cada movimiento queda en la bitácora
   con usuario, campo, valor anterior, valor nuevo, motivo y fuente.
3. **Lo público y lo operativo van separados.** La plataforma no publica
   coordenadas precisas, domicilios ni datos personales, y no atribuye ningún
   sitio a una organización que ninguna fuente identificable haya nombrado.

## Puesta en marcha

```bash
cd argos_forense
pip install -r requirements.txt
python run.py
```

Abre <http://127.0.0.1:8000>. La documentación interactiva de la API está en
<http://127.0.0.1:8000/api/docs>.

En el primer arranque se crea la base SQLite y se siembran los catálogos: 138
fuentes (federales, las 32 fiscalías y secretarías estatales, comisiones de
búsqueda, prensa nacional y estatal) y el módulo de colectivos.

### Otras formas de invocarlo

```bash
python run.py --host 0.0.0.0 --port 8080   # accesible desde la red local
python run.py --sembrar                    # sólo crear la base y sembrar catálogos
python run.py --rastrear                   # una vuelta de rastreo, sin servidor
python run.py --corte                      # generar el corte de 72 h
python run.py --publicar 29                # sellar el corte 29
```

### Pruebas

```bash
python -m pytest tests -q
```

Las pruebas cubren las reglas que no pueden romperse: inmutabilidad del folio y
del corte publicado, la bandeja como única puerta al registro definitivo, el
cálculo del nivel de corroboración, la deduplicación que nunca fusiona sola, la
reserva de datos sensibles y la validación de atribuciones.

## Arquitectura

```
argos_forense/
├── run.py                  arranque y utilidades de línea de comandos
├── app/
│   ├── config.py           configuración; intervalos y umbrales
│   ├── db.py               único punto de acceso a datos (aísla el dialecto SQL)
│   ├── schema.sql          las nueve tablas del sistema, más evidencia y cortes
│   ├── main.py             aplicación FastAPI; sirve API y frontend
│   ├── scheduler.py        APScheduler: rastreo cada 60 min, corte cada 72 h
│   ├── siembra.py          carga idempotente de los catálogos
│   ├── core/               las reglas, sin HTTP de por medio
│   │   ├── geo.py          32 entidades, regiones y detección de entidad en texto
│   │   ├── clasificador.py términos de las tres categorías y confianza
│   │   ├── folio.py        AF-AAAA-EST-CAT-NNNN
│   │   ├── corroboracion.py niveles A/B/C/D derivados de las fuentes
│   │   ├── dedupe.py       puntuación de duplicidad por criterio
│   │   ├── seguridad.py    separación OSINT / operativo y regla de atribución
│   │   ├── evidencia.py    URL, texto, HTML, captura y SHA-256
│   │   ├── bandeja.py      validación, descarte, vinculación
│   │   ├── eventos.py      ciclo de vida del evento y sus fuentes
│   │   ├── cortes.py       generación, sellado y comparación de cortes
│   │   ├── auditoria.py    bitácora; sólo admite altas
│   │   ├── tablero.py      métricas del dashboard y por entidad
│   │   └── exportacion.py  PDF, CSV, JSON y GeoJSON
│   ├── colectores/         RSS, Google News RSS y conectores directos
│   ├── api/                los endpoints
│   └── datos/              catálogos y geometría de las 32 entidades
├── web/                    frontend responsive (HTML + CSS + JS, sin build)
└── tests/
```

**Frontend sin cadena de compilación**: HTML, CSS y JavaScript servidos tal
cual, con Leaflet incluido en el repositorio. Se abre igual en Safari de
iPhone, Chrome de Android y navegadores de escritorio, y no depende de ninguna
CDN para funcionar.

**Base de datos**: SQLite. Todo el acceso pasa por `app/db.py`, que aísla el
dialecto; la migración a PostgreSQL + PostGIS está documentada en
[`docs/migracion-postgis.md`](docs/migracion-postgis.md).

## Módulos

| Sección | Qué hace |
|---|---|
| **Inicio** | Los diez indicadores del tablero, nivel de corroboración del acervo y resultado del último rastreo |
| **Mapa** | Las 32 entidades sobre geometría real, coloreadas por nivel de corroboración |
| **Bandeja** | Validar, descartar, marcar duplicado, vincular a evento, abrir fuente |
| **Eventos** | Registro definitivo y ficha completa con fuentes, atribuciones e historial |
| **Estados** | Lectura por entidad federativa |
| **Fuentes** | Catálogo de cinco niveles, ampliable, con sondeo real de cada fuente |
| **Colectivos** | Nivel 5 del catálogo, con la distinción explícita entre reporte de colectivo y confirmación institucional |
| **Cortes** | Generar, publicar, sellar, verificar el sello, comparar y exportar a PDF |
| **Tendencias** | Serie sobre cortes publicados |
| **Bitácora** | Cada movimiento del sistema, filtrable |
| **Configuración** | Operador, intervalos del programador y estado del sistema |

## API

`GET /api/health` · `POST /api/collect` · `GET /api/inbox` ·
`GET /api/inbox/{id}` · `GET /api/inbox/{id}/duplicates` ·
`POST /api/inbox/{id}/validate` · `POST /api/inbox/{id}/reject` ·
`POST /api/inbox/{id}/link` · `POST /api/inbox/{id}/possible-duplicate` ·
`POST /api/inbox/duplicates/{id}/resolve` · `GET /api/events` ·
`GET /api/events/{folio}` · `PATCH /api/events/{folio}` ·
`POST /api/events/{folio}/state` · `POST /api/events/{folio}/merge` ·
`POST /api/events/{folio}/attribution` · `GET /api/events/{folio}/sources` ·
`GET /api/cuts` · `GET /api/cuts/{n}` · `POST /api/cuts/generate` ·
`POST /api/cuts/publish` · `GET /api/cuts/{n}/verify` ·
`GET /api/cuts/{n}/compare/{m}` · `GET /api/cuts/{n}/export.pdf` ·
`GET /api/audit` · `GET /api/sources` · `POST /api/sources` ·
`POST /api/sources/{id}/verify` · `GET /api/collectives` ·
`POST /api/collectives` · `GET /api/dashboard` · `GET /api/states` ·
`GET /api/states/{iso}` · `GET /api/geo/entidades.geojson` · `GET /api/trends` ·
`GET /api/catalogs` · `GET /api/config` · `GET|POST /api/scheduler` ·
`GET /api/export/events.{json|csv|geojson}`

Las acciones que modifican algo aceptan la cabecera `X-ARGOS-Usuario`, que es
lo que firma el movimiento en la bitácora.

## Configuración por entorno

| Variable | Por omisión | Qué controla |
|---|---|---|
| `ARGOS_DB` | `datos/argos_forense.sqlite3` | Ruta de la base |
| `ARGOS_EVIDENCIA` | `datos/evidencia` | Almacén de HTML y capturas |
| `ARGOS_RASTREO_MIN` | `60` | Minutos entre rastreos |
| `ARGOS_CORTE_HORAS` | `72` | Horas entre cortes |
| `ARGOS_SCHEDULER` | `1` | Activa el programador |
| `ARGOS_CORTE_AUTOPUBLICA` | `0` | Publica el corte sin intervención humana |
| `ARGOS_RESPETAR_ROBOTS` | `1` | Respeta `robots.txt` al recolectar |
| `ARGOS_PUNTO_EXACTO` | `0` | Expone la ubicación fina en la API |
| `ARGOS_UMBRAL_DUP` | `60` | Puntaje mínimo para proponer un duplicado |
| `ARGOS_VENTANA_DIAS` | `7` | Ventana de las búsquedas |

`ARGOS_CORTE_AUTOPUBLICA` y `ARGOS_PUNTO_EXACTO` están apagadas a propósito: un
corte publicado es inmutable y no debería nacer de un proceso desatendido, y la
ubicación fina no debería exponerse por un ajuste de pantalla.

## Recolección

- **RSS y Google News RSS** para la búsqueda dirigida: cada término de las tres
  categorías cruzado con las 32 entidades federativas.
- **Conectores directos** a portales públicos, que respetan `robots.txt` salvo
  que se desactive expresamente.
- **Playwright** para páginas dinámicas y capturas de evidencia, opcional: si
  no está instalado el sistema registra `CAPTURA_NO_DISPONIBLE` y sigue, en vez
  de fingir que capturó.

Un canal RSS sólo se usa cuando está **verificado por sondeo**. Una ruta de
canal supuesta que devuelve 404 produciría un falso vacío de cobertura, que es
peor que no tener canal.

## Documentación

- [`docs/argos-forense-operacion.md`](docs/argos-forense-operacion.md) — guía de operación.
- [`docs/migracion-postgis.md`](docs/migracion-postgis.md) — migración a PostgreSQL/PostGIS.

## Datos de terceros incluidos

- **Leaflet 1.9.4** (BSD-2-Clause), en `web/vendor/leaflet/`.
- **Geometría de las 32 entidades federativas** en CRS84, normalizada a cuatro
  decimales, en `app/datos/mexico-entidades.geojson`. Los centroides y las
  cajas envolventes son cálculo propio derivado de esa geometría, y así se
  declara en el archivo.
- Los dominios institucionales del catálogo proceden de
  `../docs/dominios-oficiales.md`, el registro de fuentes verificadas del
  repositorio ARGOS. Ninguno se inventó: una entidad sin dominio registrado se
  declara `SIN DOMINIO CANÓNICO REGISTRADO`.
