/* ARGOS FORENSE — cliente de la API.
   El usuario que firma cada acción se guarda en el navegador y viaja en la
   cabecera X-ARGOS-Usuario: la bitácora nunca queda sin autor (§14). */
(function (global) {
  "use strict";

  const CLAVE_USUARIO = "argos.usuario";

  function usuario() {
    try { return localStorage.getItem(CLAVE_USUARIO) || ""; } catch (e) { return ""; }
  }
  function fijarUsuario(nombre) {
    try { localStorage.setItem(CLAVE_USUARIO, nombre || ""); } catch (e) { /* sin almacenamiento */ }
  }

  async function pedir(ruta, opciones) {
    const o = opciones || {};
    const cabeceras = { "Accept": "application/json" };
    if (usuario()) cabeceras["X-ARGOS-Usuario"] = usuario();
    if (o.cuerpo !== undefined) cabeceras["Content-Type"] = "application/json";
    const respuesta = await fetch(ruta, {
      method: o.metodo || (o.cuerpo !== undefined ? "POST" : "GET"),
      headers: cabeceras,
      body: o.cuerpo !== undefined ? JSON.stringify(o.cuerpo) : undefined
    });
    const tipo = respuesta.headers.get("content-type") || "";
    const datos = tipo.includes("json") ? await respuesta.json().catch(() => null) : await respuesta.text();
    if (!respuesta.ok) {
      const detalle = datos && datos.detail
        ? (typeof datos.detail === "string" ? datos.detail : JSON.stringify(datos.detail))
        : `HTTP ${respuesta.status}`;
      const error = new Error(detalle);
      error.estado = respuesta.status;
      throw error;
    }
    return datos;
  }

  function consulta(parametros) {
    const p = new URLSearchParams();
    Object.keys(parametros || {}).forEach((k) => {
      const v = parametros[k];
      if (v !== null && v !== undefined && v !== "") p.set(k, v);
    });
    const s = p.toString();
    return s ? `?${s}` : "";
  }

  global.API = {
    usuario, fijarUsuario, pedir, consulta,

    salud: () => pedir("/api/health"),
    catalogos: () => pedir("/api/catalogs"),
    tablero: () => pedir("/api/dashboard"),

    rastrear: (cuerpo) => pedir("/api/collect", { cuerpo: cuerpo || {} }),
    bandeja: (f) => pedir("/api/inbox" + consulta(f)),
    bandejaItem: (id) => pedir(`/api/inbox/${id}`),
    duplicados: (id) => pedir(`/api/inbox/${id}/duplicates`),
    validar: (id, cuerpo) => pedir(`/api/inbox/${id}/validate`, { cuerpo }),
    descartar: (id, motivo) => pedir(`/api/inbox/${id}/reject`, { cuerpo: { motivo } }),
    vincular: (id, cuerpo) => pedir(`/api/inbox/${id}/link`, { cuerpo }),
    posibleDuplicado: (id, motivo) => pedir(`/api/inbox/${id}/possible-duplicate`, { cuerpo: { motivo } }),
    resolverDuplicado: (id, cuerpo) => pedir(`/api/inbox/duplicates/${id}/resolve`, { cuerpo }),

    eventos: (f) => pedir("/api/events" + consulta(f)),
    evento: (folio) => pedir(`/api/events/${encodeURIComponent(folio)}`),
    editarEvento: (folio, cuerpo) => pedir(`/api/events/${encodeURIComponent(folio)}`, { metodo: "PATCH", cuerpo }),
    atribuir: (folio, cuerpo) => pedir(`/api/events/${encodeURIComponent(folio)}/attribution`, { cuerpo }),
    fusionar: (folio, cuerpo) => pedir(`/api/events/${encodeURIComponent(folio)}/merge`, { cuerpo }),

    estados: () => pedir("/api/states"),
    estado: (iso) => pedir(`/api/states/${iso}`),
    geojson: () => pedir("/api/geo/entidades.geojson"),

    fuentes: (f) => pedir("/api/sources" + consulta(f)),
    verificarFuente: (id) => pedir(`/api/sources/${id}/verify`, { cuerpo: {} }),
    crearFuente: (cuerpo) => pedir("/api/sources", { cuerpo }),
    colectivos: (f) => pedir("/api/collectives" + consulta(f)),
    crearColectivo: (cuerpo) => pedir("/api/collectives", { cuerpo }),
    editarColectivo: (id, cuerpo) => pedir(`/api/collectives/${id}`, { metodo: "PATCH", cuerpo }),

    cortes: () => pedir("/api/cuts"),
    corte: (n) => pedir(`/api/cuts/${n}`),
    generarCorte: () => pedir("/api/cuts/generate", { cuerpo: {} }),
    publicarCorte: (n) => pedir("/api/cuts/publish", { cuerpo: n ? { numero: n } : {} }),
    verificarCorte: (n) => pedir(`/api/cuts/${n}/verify`),
    compararCortes: (a, b) => pedir(`/api/cuts/${a}/compare/${b}`),

    tendencias: () => pedir("/api/trends"),
    bitacora: (f) => pedir("/api/audit" + consulta(f)),
    configuracion: () => pedir("/api/config"),
    programador: (cuerpo) => pedir("/api/scheduler", { cuerpo })
  };
})(window);
