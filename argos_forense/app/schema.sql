-- ARGOS FORENSE — esquema (§25).
--
-- Dialecto: SQLite. Escrito deliberadamente en SQL portable para que la
-- migración a PostgreSQL/PostGIS (§1) toque el dialecto y no el modelo:
--   · claves primarias INTEGER PRIMARY KEY  -> GENERATED ALWAYS AS IDENTITY
--   · TEXT con marcas ISO-8601              -> TIMESTAMPTZ
--   · latitud/longitud + geom_wkt           -> GEOGRAPHY(Point,4326)
-- Ninguna tabla admite borrado físico: se opera con estados (§14).

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------- usuarios --
CREATE TABLE IF NOT EXISTS users (
  id            INTEGER PRIMARY KEY,
  usuario       TEXT NOT NULL UNIQUE,
  nombre        TEXT NOT NULL,
  rol           TEXT NOT NULL DEFAULT 'ANALISTA',      -- ANALISTA | VALIDADOR | ADMIN | SISTEMA
  activo        INTEGER NOT NULL DEFAULT 1,
  token         TEXT,                                   -- opcional, para API
  creado_en     TEXT NOT NULL
);

-- ----------------------------------------------------------------- fuentes --
CREATE TABLE IF NOT EXISTS sources (
  id                 INTEGER PRIMARY KEY,
  nivel              INTEGER NOT NULL,                  -- 1..5 (§7)
  nombre             TEXT NOT NULL,
  ambito             TEXT NOT NULL DEFAULT 'NACIONAL',  -- FEDERAL | ESTATAL | REGIONAL | MUNICIPAL | NACIONAL
  entidad_iso        TEXT,                              -- MX-XXX o NULL si es nacional/federal
  tipo               TEXT NOT NULL DEFAULT 'PORTAL',    -- PORTAL | RSS | GOOGLE_NEWS | REDES
  url_sitio          TEXT,
  url_rss            TEXT,
  dominio            TEXT,
  clase_url          TEXT,                              -- A fechable | B semifechable | C opaca
  verificado         INTEGER NOT NULL DEFAULT 0,        -- 1 sólo tras sondeo real
  rss_verificado     INTEGER NOT NULL DEFAULT 0,
  ultimo_estado_http TEXT,
  ultimo_error       TEXT,
  ultima_revision    TEXT,
  activo             INTEGER NOT NULL DEFAULT 1,
  estatus            TEXT NOT NULL DEFAULT 'SIN VERIFICAR',
  origen_registro    TEXT,                              -- de dónde salió el dominio
  notas              TEXT,
  creado_en          TEXT NOT NULL,
  actualizado_en     TEXT NOT NULL,
  UNIQUE (nombre, nivel, entidad_iso)
);
CREATE INDEX IF NOT EXISTS ix_sources_nivel   ON sources(nivel);
CREATE INDEX IF NOT EXISTS ix_sources_entidad ON sources(entidad_iso);

-- -------------------------------------------------------------- colectivos --
CREATE TABLE IF NOT EXISTS collectives (
  id                    INTEGER PRIMARY KEY,
  nombre                TEXT NOT NULL,
  entidad_iso           TEXT,
  municipio_base        TEXT,
  url_web               TEXT,
  url_facebook          TEXT,
  url_instagram         TEXT,
  url_x                 TEXT,
  url_tiktok            TEXT,
  otras_paginas         TEXT,                           -- JSON [ {nombre,url} ]
  fecha_ultima_revision TEXT,
  estatus_fuente        TEXT NOT NULL DEFAULT 'SIN VERIFICAR',
  activo                INTEGER NOT NULL DEFAULT 1,
  notas                 TEXT,
  creado_en             TEXT NOT NULL,
  actualizado_en        TEXT NOT NULL,
  UNIQUE (nombre, entidad_iso)
);

-- ------------------------------------------------------------------ cortes --
-- Un corte publicado es inmutable (§16): su contenido queda congelado en
-- `snapshot` y sellado con `sha256`. Cualquier cambio posterior vive en el
-- corte siguiente.
CREATE TABLE IF NOT EXISTS cuts (
  id               INTEGER PRIMARY KEY,
  numero           INTEGER NOT NULL UNIQUE,
  etiqueta         TEXT NOT NULL,                       -- "ARGOS FORENSE — CORTE 029"
  ventana_inicio   TEXT NOT NULL,
  ventana_fin      TEXT NOT NULL,
  estado           TEXT NOT NULL DEFAULT 'BORRADOR',    -- BORRADOR | PUBLICADO
  generado_en      TEXT NOT NULL,
  publicado_en     TEXT,
  publicado_por    TEXT,
  corte_anterior   INTEGER REFERENCES cuts(id),
  snapshot         TEXT,                                -- JSON congelado del corte
  sha256           TEXT,
  creado_en        TEXT NOT NULL
);

-- ------------------------------------------------------------------ eventos --
CREATE TABLE IF NOT EXISTS events (
  folio                 TEXT PRIMARY KEY,               -- AF-AAAA-EST-CAT-NNNN (§9), inmutable
  categoria             TEXT NOT NULL,                  -- FOS | CAM | CSE
  subcategoria          TEXT,
  fecha_deteccion       TEXT NOT NULL,
  hora_deteccion        TEXT NOT NULL,
  fecha_probable_evento TEXT,
  precision_fecha       TEXT DEFAULT 'DIA',             -- DIA | MES | INDETERMINADA
  entidad_iso           TEXT NOT NULL,
  municipio             TEXT,
  localidad             TEXT,
  resumen_factual       TEXT NOT NULL,
  nivel_corroboracion   TEXT NOT NULL DEFAULT 'D',      -- A | B | C | D (§11)
  estado                TEXT NOT NULL DEFAULT 'ACTIVO', -- §14
  -- Georreferencia. Nunca se publica el punto exacto de forma automática (§20):
  -- `precision_geo` declara qué representa el par lat/lon almacenado.
  latitud               REAL,
  longitud              REAL,
  precision_geo         TEXT DEFAULT 'CENTROIDE_ENTIDAD',
  geom_wkt              TEXT,                           -- puente hacia PostGIS
  reserva_operativa     INTEGER NOT NULL DEFAULT 0,     -- 1 = no exponer ubicación ni detalle fino
  num_cuerpos           INTEGER,
  num_restos            TEXT,
  personas_liberadas    INTEGER,
  personas_detenidas    INTEGER,
  autoridad             TEXT,
  atribucion            TEXT,                           -- JSON [ {texto, atribuido_por, url} ] (§21)
  corte_alta            INTEGER REFERENCES cuts(id),
  fusionado_en          TEXT REFERENCES events(folio),
  creado_en             TEXT NOT NULL,
  ultima_actualizacion  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_events_entidad   ON events(entidad_iso);
CREATE INDEX IF NOT EXISTS ix_events_categoria ON events(categoria);
CREATE INDEX IF NOT EXISTS ix_events_nivel     ON events(nivel_corroboracion);
CREATE INDEX IF NOT EXISTS ix_events_estado    ON events(estado);

-- ------------------------------------------------------------- raw_items ----
-- Todo lo detectado entra aquí y ninguna fila pasa sola al registro
-- definitivo (§4): la bandeja de validación es obligatoria.
CREATE TABLE IF NOT EXISTS raw_items (
  id                  INTEGER PRIMARY KEY,
  source_id           INTEGER REFERENCES sources(id),
  collective_id       INTEGER REFERENCES collectives(id),
  url                 TEXT NOT NULL,
  url_hash            TEXT NOT NULL UNIQUE,             -- sha256(url normalizada)
  titulo              TEXT NOT NULL,
  medio               TEXT,
  nivel_fuente        INTEGER,
  fecha_publicacion   TEXT,
  fecha_deteccion     TEXT NOT NULL,
  categoria_detectada TEXT,
  subcategoria        TEXT,
  entidad_iso         TEXT,
  entidad_confianza   INTEGER,
  municipio           TEXT,
  resumen             TEXT,
  terminos            TEXT,                             -- JSON de términos que dispararon la detección
  confianza_pct       INTEGER NOT NULL DEFAULT 0,       -- §8
  riesgo_opsec        TEXT,                             -- JSON de hallazgos de §20
  estado              TEXT NOT NULL DEFAULT 'PENDIENTE',-- PENDIENTE | VALIDADO | DESCARTADO | DUPLICADO | VINCULADO
  folio               TEXT REFERENCES events(folio),
  motivo              TEXT,
  revisado_por        TEXT,
  revisado_en         TEXT,
  corte_deteccion     INTEGER REFERENCES cuts(id),
  creado_en           TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_raw_estado    ON raw_items(estado);
CREATE INDEX IF NOT EXISTS ix_raw_entidad   ON raw_items(entidad_iso);
CREATE INDEX IF NOT EXISTS ix_raw_categoria ON raw_items(categoria_detectada);
CREATE INDEX IF NOT EXISTS ix_raw_fecha     ON raw_items(fecha_deteccion);

-- --------------------------------------------------------- event_sources ----
-- Un evento, muchas fuentes (§13).
CREATE TABLE IF NOT EXISTS event_sources (
  id                INTEGER PRIMARY KEY,
  folio             TEXT NOT NULL REFERENCES events(folio),
  raw_item_id       INTEGER REFERENCES raw_items(id),
  source_id         INTEGER REFERENCES sources(id),
  collective_id     INTEGER REFERENCES collectives(id),
  nivel             INTEGER NOT NULL,
  medio             TEXT,
  titulo            TEXT,
  url               TEXT NOT NULL,
  fecha_publicacion TEXT,
  fecha_consulta    TEXT NOT NULL,
  tipo_aporte       TEXT NOT NULL DEFAULT 'CORROBORACION', -- ORIGEN | CORROBORACION | ACTUALIZACION
  es_institucional  INTEGER NOT NULL DEFAULT 0,
  es_colectivo      INTEGER NOT NULL DEFAULT 0,
  sha256            TEXT,
  creado_en         TEXT NOT NULL,
  UNIQUE (folio, url)
);
CREATE INDEX IF NOT EXISTS ix_evsrc_folio ON event_sources(folio);

-- -------------------------------------------------------------- evidencia ---
-- §15: qué se consultó exactamente y cómo verificarlo después.
CREATE TABLE IF NOT EXISTS evidence (
  id                INTEGER PRIMARY KEY,
  raw_item_id       INTEGER REFERENCES raw_items(id),
  url               TEXT NOT NULL,
  titulo            TEXT,
  fecha_publicacion TEXT,
  fecha_consulta    TEXT NOT NULL,
  texto             TEXT,
  ruta_html         TEXT,
  ruta_captura      TEXT,
  sha256_texto      TEXT,
  sha256_html       TEXT,
  sha256_captura    TEXT,
  estado_captura    TEXT DEFAULT 'NO_INTENTADA',
  creado_en         TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_evidence_raw ON evidence(raw_item_id);

-- ------------------------------------------------- duplicate_candidates -----
-- §12: el sistema puntúa, la persona decide. Nunca fusiona sola.
CREATE TABLE IF NOT EXISTS duplicate_candidates (
  id             INTEGER PRIMARY KEY,
  raw_item_id    INTEGER REFERENCES raw_items(id),
  otro_raw_id    INTEGER REFERENCES raw_items(id),
  folio          TEXT REFERENCES events(folio),
  puntaje        INTEGER NOT NULL,
  desglose       TEXT NOT NULL,                          -- JSON por criterio
  estado         TEXT NOT NULL DEFAULT 'ABIERTO',        -- ABIERTO | FUSIONADO | SEPARADOS | VINCULADO
  resuelto_por   TEXT,
  resuelto_en    TEXT,
  creado_en      TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_dup_raw   ON duplicate_candidates(raw_item_id);
CREATE INDEX IF NOT EXISTS ix_dup_folio ON duplicate_candidates(folio);

-- ------------------------------------------------------------------ audit ---
-- §14: cada modificación, sin excepción. Sólo INSERT.
CREATE TABLE IF NOT EXISTS audit (
  id             INTEGER PRIMARY KEY,
  ts             TEXT NOT NULL,
  fecha          TEXT NOT NULL,
  hora           TEXT NOT NULL,
  usuario        TEXT NOT NULL,
  proceso        TEXT NOT NULL,
  entidad_tipo   TEXT NOT NULL,                          -- event | raw_item | source | collective | cut | config
  entidad_id     TEXT NOT NULL,
  evento         TEXT,                                   -- folio afectado, si aplica
  campo          TEXT,
  valor_anterior TEXT,
  valor_nuevo    TEXT,
  motivo         TEXT,
  fuente_origen  TEXT
);
CREATE INDEX IF NOT EXISTS ix_audit_ts     ON audit(ts);
CREATE INDEX IF NOT EXISTS ix_audit_evento ON audit(evento);
CREATE INDEX IF NOT EXISTS ix_audit_tipo   ON audit(entidad_tipo, entidad_id);

-- ------------------------------------------------------------- cut_events ---
-- Índice consultable del contenido congelado de cada corte, para comparar
-- cortes (§18) sin tener que abrir el snapshot.
CREATE TABLE IF NOT EXISTS cut_events (
  id                  INTEGER PRIMARY KEY,
  cut_id              INTEGER NOT NULL REFERENCES cuts(id),
  folio               TEXT NOT NULL REFERENCES events(folio),
  categoria           TEXT NOT NULL,
  entidad_iso         TEXT NOT NULL,
  nivel_corroboracion TEXT NOT NULL,
  estado              TEXT NOT NULL,
  es_nuevo            INTEGER NOT NULL DEFAULT 0,
  es_actualizado      INTEGER NOT NULL DEFAULT 0,
  num_fuentes         INTEGER NOT NULL DEFAULT 0,
  UNIQUE (cut_id, folio)
);

-- ----------------------------------------------------------------- config ---
CREATE TABLE IF NOT EXISTS config (
  clave           TEXT PRIMARY KEY,
  valor           TEXT NOT NULL,
  actualizado_en  TEXT NOT NULL,
  actualizado_por TEXT
);
