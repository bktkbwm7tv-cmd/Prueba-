/* ARGOS FORENSE — utilidades de presentación.
   Todo lo que se pinta pasa por `esc()`: el contenido viene de fuentes
   externas y nunca se inyecta como HTML. */
(function (global) {
  "use strict";

  const CATEGORIAS = {
    FOS: { nombre: "Fosas clandestinas", corto: "Fosa", clase: "fos" },
    CAM: { nombre: "Campamentos", corto: "Campamento", clase: "cam" },
    CSE: { nombre: "Casas de seguridad", corto: "Casa de seguridad", clase: "cse" }
  };

  const NIVELES = {
    A: { etiqueta: "CONFIRMADO", detalle: "Fuente institucional competente." },
    B: { etiqueta: "ALTAMENTE CORROBORADO", detalle: "Dos o más fuentes independientes coincidentes." },
    C: { etiqueta: "REPORTADO", detalle: "Una fuente periodística identificable." },
    D: { etiqueta: "POR VERIFICAR", detalle: "Reporte inicial o publicación sin corroboración adicional." }
  };

  function esc(valor) {
    if (valor === null || valor === undefined) return "";
    return String(valor)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }

  function texto(valor, porOmision) {
    const v = valor === null || valor === undefined || valor === "" ? null : valor;
    return v === null ? (porOmision || "—") : String(v);
  }

  function fecha(iso, conHora) {
    if (!iso) return "—";
    const d = new Date(iso);
    if (isNaN(d)) return String(iso).slice(0, 19).replace("T", " ");
    const opciones = conHora
      ? { day: "2-digit", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" }
      : { day: "2-digit", month: "short", year: "numeric" };
    return d.toLocaleString("es-MX", Object.assign({ timeZone: "America/Mexico_City" }, opciones));
  }

  function distintivoNivel(nivel) {
    const n = (nivel || "D").toUpperCase();
    const info = NIVELES[n] || NIVELES.D;
    return `<span class="nivel nivel--${n.toLowerCase()}" title="${esc(info.detalle)}">` +
           `<span class="nivel__letra" data-letra="${n}"></span>${esc(info.etiqueta)}</span>`;
  }

  function distintivoCategoria(cat) {
    const info = CATEGORIAS[cat];
    if (!info) return `<span class="etiqueta">${esc(cat || "—")}</span>`;
    return `<span class="etiqueta etiqueta--${info.clase}">${esc(info.corto)}</span>`;
  }

  function folio(valor) {
    return valor ? `<span class="folio">${esc(valor)}</span>` : "";
  }

  function marcaTiempo(iso, prefijo) {
    return `<span class="marca-tiempo">${esc(prefijo || "")}${esc(fecha(iso, true))}</span>`;
  }

  /* Semáforo del mapa por nivel de corroboración de la entidad, no por volumen:
     el color dice qué tan sostenido está lo que hay, no cuánto hay. */
  const COLOR_NIVEL = { A: "#2fbf87", B: "#37b6e8", C: "#e0a53a", D: "#d6604d" };
  function colorNivel(nivel) { return COLOR_NIVEL[nivel] || "#26404f"; }

  function vacio(titulo, detalle) {
    return `<div class="vacio"><strong>${esc(titulo)}</strong>${esc(detalle || "")}</div>`;
  }

  function cargando(texto) {
    return `<div class="cargando">${esc(texto || "Consultando…")}</div>`;
  }

  function tabla(cabeceras, filas, opciones) {
    const o = opciones || {};
    if (!filas.length) return vacio(o.tituloVacio || "Sin registros", o.detalleVacio || "");
    const th = cabeceras.map((c) => `<th>${esc(c)}</th>`).join("");
    const tr = filas.map((f) => `<tr>${f.map((c) => `<td>${c}</td>`).join("")}</tr>`).join("");
    return `<div class="tabla-envoltorio"><table class="datos"><thead><tr>${th}</tr></thead>` +
           `<tbody>${tr}</tbody></table></div>`;
  }

  function campo(nombre, valor) {
    return `<div class="campo"><div class="campo__nombre">${esc(nombre)}</div>` +
           `<div class="campo__valor">${valor === "" || valor === null || valor === undefined ? "—" : valor}</div></div>`;
  }

  function indicador(cifra, etiqueta, opciones) {
    const o = opciones || {};
    return `<div class="indicador${o.clase ? " indicador--" + o.clase : ""}">` +
           `<div class="indicador__cifra">${esc(cifra)}</div>` +
           `<div class="indicador__etiqueta">${esc(etiqueta)}</div>` +
           (o.pie ? `<div class="indicador__pie">${esc(o.pie)}</div>` : "") + `</div>`;
  }

  const ICONOS = {
    fosa: '<path d="M4 17c0-3 3.5-5 8-5s8 2 8 5"/><path d="M4 17v2h16v-2"/><path d="M9 12V7a3 3 0 0 1 6 0v5"/>',
    campamento: '<path d="M12 4 3 20h18z"/><path d="M12 4v16"/><path d="M8.5 20l3.5-6 3.5 6"/>',
    casa: '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    mapa: '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14"/><path d="M15 6v14"/>',
    bandeja: '<path d="M3 13h5l2 3h4l2-3h5"/><path d="M5 5h14l2 8v6H3v-6z"/>',
    reloj: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    sello: '<path d="M5 20h14"/><path d="M8 16h8l1-4H7z"/><path d="M12 12V8a2 2 0 1 1 2-2"/>'
  };
  function icono(nombre, clase) {
    const d = ICONOS[nombre];
    if (!d) return "";
    return `<svg class="ico ${clase || ""}" viewBox="0 0 24 24" aria-hidden="true">${d}</svg>`;
  }

  global.U = { CATEGORIAS, NIVELES, esc, texto, fecha, distintivoNivel, distintivoCategoria,
               folio, marcaTiempo, colorNivel, vacio, cargando, tabla, campo, indicador, icono };
})(window);
