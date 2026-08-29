# Migración de SQLite a PostgreSQL + PostGIS

Versión 1.0

ARGOS FORENSE arranca sobre SQLite porque una instalación de un solo puesto no
necesita más, y porque una base en un archivo se respalda copiándola. La
arquitectura está preparada para que el cambio a PostgreSQL/PostGIS sea un
cambio de motor, no una reescritura.

## Qué hay que tocar y qué no

**No se toca** ninguna regla de negocio. Todos los módulos de `app/core/` y
`app/colectores/` acceden a la base exclusivamente a través de `app/db.py`.

**Se toca** `app/db.py`, en tres puntos que ya están aislados:

| Punto | Qué hace hoy | Qué haría con PostgreSQL |
|---|---|---|
| `conectar()` | Abre `sqlite3.connect` por hilo | Abre una conexión `psycopg` desde un *pool* |
| `adaptar_sql()` | Devuelve el SQL sin cambios | Traduce `?` a `%s` (la función ya contempla esta rama) |
| `DIALECTO` | `"sqlite"` | `"postgresql"` |

`insertar()` necesita además `RETURNING id` en lugar de `cursor.lastrowid`, y
`config_set()` ya usa `ON CONFLICT … DO UPDATE`, que PostgreSQL entiende igual.

## Conversión del esquema

`app/schema.sql` está escrito en SQL portable a propósito. Las equivalencias:

| SQLite | PostgreSQL |
|---|---|
| `INTEGER PRIMARY KEY` | `INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY` |
| `TEXT` con marca ISO-8601 | `TIMESTAMPTZ` |
| `INTEGER` usado como booleano | `BOOLEAN` |
| `TEXT` con JSON (`terminos`, `snapshot`, `desglose`, `atribucion`) | `JSONB` |
| `REAL` en `latitud`/`longitud` | se conservan, y se añade la columna geográfica |

## La parte espacial

Hoy cada evento guarda `latitud`, `longitud`, `precision_geo` y `geom_wkt`. Esa
última columna existe precisamente como puente: contiene el punto en WKT
(`POINT(lon lat)`), que es lo que PostGIS lee directamente.

```sql
CREATE EXTENSION IF NOT EXISTS postgis;

ALTER TABLE events ADD COLUMN geom geography(Point, 4326);
UPDATE events SET geom = ST_GeogFromText('SRID=4326;' || geom_wkt)
 WHERE geom_wkt IS NOT NULL;
CREATE INDEX ix_events_geom ON events USING GIST (geom);
```

A partir de ahí son posibles las consultas que SQLite no puede resolver:
eventos dentro de un radio, agrupación por polígono municipal, distancia entre
hallazgos de la misma categoría.

**Lo que no cambia con PostGIS**: `precision_geo` sigue declarando qué
representa el punto y la API sigue generalizando la ubicación antes de
publicarla. Tener geometría precisa en la base no autoriza a exponerla: esa es
una decisión de §20, no una limitación del motor.

## Migración de los datos

```bash
# 1. Volcar la base actual
sqlite3 datos/argos_forense.sqlite3 .dump > volcado.sql

# 2. Crear el esquema equivalente en PostgreSQL (ver equivalencias de arriba)
psql -d argos_forense -f docs/schema-postgres.sql   # a redactar al migrar

# 3. Cargar tabla por tabla respetando el orden de dependencias:
#    users → sources → collectives → cuts → events → raw_items →
#    event_sources → evidence → duplicate_candidates → cut_events → audit
```

El orden importa: `events` referencia `cuts`, y `event_sources` referencia
`events` y `raw_items`.

## Comprobación posterior

La suite de `tests/` es el criterio de aceptación de la migración: si pasa
íntegra contra el motor nuevo, las reglas siguen en pie. En particular
`test_corte_publicado_no_se_modifica` y `test_cada_movimiento_deja_bitacora_y_nada_se_borra`
comprueban las dos garantías que no pueden perderse al cambiar de base.
