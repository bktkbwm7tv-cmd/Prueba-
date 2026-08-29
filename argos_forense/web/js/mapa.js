/* ARGOS FORENSE — mapa nacional (§3).

   Se dibuja sobre los polígonos reales de las 32 entidades servidos por
   /api/geo/entidades.geojson. No se carga ninguna capa de teselas: el mapa es
   la geometría del país y el dato de ARGOS, no un callejero. Eso además evita
   que la plataforma dependa de un servidor externo para funcionar.

   §20: aquí no se pinta ningún punto fino. La unidad de representación es la
   entidad federativa. */
(function (global) {
  "use strict";

  const CENTRO = [23.9, -102.2];

  let mapa = null;
  let capa = null;
  let alSeleccionar = null;

  function estilo(propiedades) {
    const total = propiedades.total || 0;
    return {
      color: "#26404f",
      weight: 1,
      fillColor: total ? U.colorNivel(propiedades.nivel_corroboracion_max) : "#12212c",
      fillOpacity: total ? 0.72 : 0.35
    };
  }

  function contenidoGlobo(p) {
    const filas = [
      ["Fosas", p.fosas],
      ["Campamentos", p.campamentos],
      ["Casas de seguridad", p.casas_de_seguridad],
      ["Eventos nuevos", p.eventos_nuevos],
      ["Actualizaciones", p.actualizaciones]
    ].map(([k, v]) => `<div class="fila fila--sep"><span class="tenue">${U.esc(k)}</span><b class="mono">${U.esc(v)}</b></div>`).join("");
    const nivel = p.nivel_corroboracion_max
      ? U.distintivoNivel(p.nivel_corroboracion_max)
      : '<span class="tenue pequeno">sin eventos registrados</span>';
    return `<div><div class="fila fila--sep" style="margin-bottom:.35rem">
        <b>${U.esc(p.nombre)}</b><span class="pequeno tenue">${U.esc(p.region || "")}</span></div>
      ${filas}
      <div style="margin-top:.4rem">${nivel}</div>
      <button class="boton boton--chico" style="margin-top:.5rem;width:100%" data-ir-estado="${U.esc(p.id)}">Ver la entidad</button>
    </div>`;
  }

  function crear(idContenedor, geojson, opciones) {
    const o = opciones || {};
    alSeleccionar = o.alSeleccionar || null;
    if (mapa) { mapa.remove(); mapa = null; }

    mapa = L.map(idContenedor, {
      center: CENTRO, zoom: 4, minZoom: 3, maxZoom: 9,
      zoomControl: true, attributionControl: true, scrollWheelZoom: false
    });
    mapa.attributionControl.setPrefix(
      'ARGOS FORENSE · geometría de las 32 entidades federativas (CRS84) · ubicación generalizada (§20)'
    );

    capa = L.geoJSON(geojson, {
      style: (f) => estilo(f.properties),
      onEachFeature: (f, capaEntidad) => {
        const p = f.properties;
        capaEntidad.bindTooltip(
          `${U.esc(p.nombre)} · ${p.total || 0} evento(s)`,
          { sticky: true, direction: "top", opacity: 0.95 }
        );
        capaEntidad.bindPopup(contenidoGlobo(p), { maxWidth: 280 });
        capaEntidad.on({
          mouseover: (e) => e.target.setStyle({ weight: 2, color: "#3ac9e8" }),
          mouseout: (e) => capa.resetStyle(e.target),
          click: () => { if (alSeleccionar) alSeleccionar(p); }
        });
      }
    }).addTo(mapa);

    mapa.fitBounds(capa.getBounds(), { padding: [8, 8] });
    // El clic sobre el botón del globo lo atiende el enrutador de la aplicación.
    mapa.on("popupopen", (e) => {
      const boton = e.popup.getElement().querySelector("[data-ir-estado]");
      if (boton) boton.addEventListener("click", () => {
        location.hash = `#/estados/${boton.getAttribute("data-ir-estado")}`;
      });
    });
    return mapa;
  }

  function destruir() { if (mapa) { mapa.remove(); mapa = null; capa = null; } }

  function leyenda() {
    const items = [
      ["A — Confirmado", U.colorNivel("A")],
      ["B — Altamente corroborado", U.colorNivel("B")],
      ["C — Reportado", U.colorNivel("C")],
      ["D — Por verificar", U.colorNivel("D")],
      ["Sin eventos en el corte", "#12212c"]
    ];
    return `<div class="leyenda">${items.map(([t, c]) =>
      `<span><span class="leyenda__punto" style="background:${c}"></span>${U.esc(t)}</span>`).join("")}</div>`;
  }

  global.Mapa = { crear, destruir, leyenda };
})(window);
