/* ARGOS FORENSE — arranque, menú y enrutador por hash (§23).

   Enrutador por `location.hash`: la aplicación se sirve como un solo HTML y
   funciona igual abierta desde el teléfono, la tableta o el escritorio, sin
   configuración del servidor. */
(function (global) {
  "use strict";

  const SECCIONES = [
    { ruta: "inicio",        titulo: "Inicio",        vista: () => VistasOperacion.inicio },
    { ruta: "mapa",          titulo: "Mapa",          vista: () => VistasOperacion.mapa },
    { ruta: "bandeja",       titulo: "Bandeja",       vista: () => VistasOperacion.bandeja, contador: "pendientes" },
    { ruta: "eventos",       titulo: "Eventos",       vista: () => VistasOperacion.eventos, detalle: () => VistasOperacion.evento },
    { ruta: "estados",       titulo: "Estados",       vista: () => VistasOperacion.estados, detalle: () => VistasOperacion.estado },
    { ruta: "fuentes",       titulo: "Fuentes",       vista: () => VistasCatalogos.fuentes },
    { ruta: "colectivos",    titulo: "Colectivos",    vista: () => VistasCatalogos.colectivos },
    { ruta: "cortes",        titulo: "Cortes",        vista: () => VistasCatalogos.cortes, detalle: () => VistasCatalogos.corte },
    { ruta: "tendencias",    titulo: "Tendencias",    vista: () => VistasCatalogos.tendencias },
    { ruta: "bitacora",      titulo: "Bitácora",      vista: () => VistasCatalogos.bitacora },
    { ruta: "configuracion", titulo: "Configuración", vista: () => VistasCatalogos.configuracion }
  ];

  let catalogosEnCache = null;
  let pendientes = 0;

  /* -------------------------------------------------------------- avisos -- */
  let temporizadorAviso = null;
  function avisar(mensaje, esError) {
    const caja = document.getElementById("aviso-flotante");
    caja.textContent = mensaje;
    caja.classList.toggle("aviso-flotante--mal", !!esError);
    caja.hidden = false;
    clearTimeout(temporizadorAviso);
    temporizadorAviso = setTimeout(() => { caja.hidden = true; }, esError ? 8000 : 5000);
  }

  /* ------------------------------------------------------------- diálogo -- */
  function dialogo(titulo, cuerpoHtml, botones, alMontar) {
    const velo = document.getElementById("velo");
    document.getElementById("dialogo-titulo").textContent = titulo;
    const cuerpo = document.getElementById("dialogo-cuerpo");
    cuerpo.innerHTML = cuerpoHtml;
    const pie = document.getElementById("dialogo-pie");
    pie.innerHTML = "";

    const cancelar = document.createElement("button");
    cancelar.className = "boton boton--fantasma";
    cancelar.textContent = "Cancelar";
    cancelar.addEventListener("click", cerrarDialogo);
    pie.appendChild(cancelar);

    (botones || []).forEach((b) => {
      const boton = document.createElement("button");
      boton.className = "boton " + (b.clase || "");
      boton.textContent = b.texto;
      boton.addEventListener("click", async () => {
        boton.disabled = true;
        try {
          const resultado = await b.accion();
          if (resultado !== false) cerrarDialogo();
        } catch (e) {
          avisar(e.message || "La acción falló.", true);
        }
        boton.disabled = false;
      });
      pie.appendChild(boton);
    });

    velo.hidden = false;
    if (alMontar) alMontar(cuerpo);
    const primero = cuerpo.querySelector("input, select, textarea");
    if (primero) primero.focus();
  }

  function cerrarDialogo() { document.getElementById("velo").hidden = true; }

  /* ------------------------------------------------------------- filtros -- */
  function pintarFiltros(idContenedor, campos, rutaBase) {
    const contenedor = document.getElementById(idContenedor);
    const html = campos.map((c) => {
      if (c.tipo === "select") {
        const opciones = c.opciones.map(([v, t]) =>
          `<option value="${U.esc(v)}"${String(v) === String(c.valor) ? " selected" : ""}>${U.esc(t)}</option>`).join("");
        return `<label><span>${U.esc(c.etiqueta)}</span><select data-filtro="${c.nombre}">${opciones}</select></label>`;
      }
      if (c.tipo === "entidad") {
        const entidades = (catalogosEnCache ? catalogosEnCache.entidades : []).map((e) =>
          `<option value="${e.iso}"${e.iso === c.valor ? " selected" : ""}>${U.esc(e.nombre)}</option>`).join("");
        return `<label><span>${U.esc(c.etiqueta)}</span>
          <select data-filtro="${c.nombre}"><option value="">Todas</option>${entidades}</select></label>`;
      }
      return `<label><span>${U.esc(c.etiqueta)}</span>
        <input data-filtro="${c.nombre}" type="${c.tipo === "number" ? "number" : "search"}"
               value="${U.esc(c.valor || "")}"></label>`;
    }).join("");

    contenedor.innerHTML = `<div class="filtros">${html}
      <label style="flex:0 0 auto;justify-content:flex-end">
        <span>&nbsp;</span><button class="boton" data-limpiar>Limpiar</button></label></div>`;

    function aplicar() {
      const parametros = new URLSearchParams();
      contenedor.querySelectorAll("[data-filtro]").forEach((el) => {
        if (el.value) parametros.set(el.dataset.filtro, el.value);
      });
      const consulta = parametros.toString();
      location.hash = rutaBase + (consulta ? "?" + consulta : "");
    }
    contenedor.querySelectorAll("select[data-filtro]").forEach((el) => el.addEventListener("change", aplicar));
    contenedor.querySelectorAll("input[data-filtro]").forEach((el) => {
      let t = null;
      el.addEventListener("input", () => { clearTimeout(t); t = setTimeout(aplicar, 450); });
      el.addEventListener("keydown", (e) => { if (e.key === "Enter") { clearTimeout(t); aplicar(); } });
    });
    contenedor.querySelector("[data-limpiar]").addEventListener("click", () => { location.hash = rutaBase; });
  }

  /* --------------------------------------------------------------- menú --- */
  function pintarMenu(rutaActiva) {
    const menu = document.getElementById("menu");
    menu.innerHTML = SECCIONES.map((s) => {
      const activo = s.ruta === rutaActiva ? ' aria-current="page"' : "";
      const cuenta = s.contador === "pendientes" && pendientes
        ? `<span class="menu__cuenta">${pendientes}</span>` : "";
      return `<a class="menu__enlace" href="#/${s.ruta}"${activo}>${U.esc(s.titulo)}${cuenta}</a>`;
    }).join("");
  }

  /* ------------------------------------------------------------ catálogos - */
  async function catalogos() {
    if (!catalogosEnCache) catalogosEnCache = await API.catalogos();
    return catalogosEnCache;
  }

  /* ------------------------------------------------------------- cabecera - */
  async function refrescarCabecera() {
    try {
      const s = await API.salud();
      const corte = document.getElementById("sello-corte");
      const vigente = s.cortes.borrador_abierto || s.cortes.ultimo_publicado;
      corte.textContent = vigente || "sin cortes";
      corte.title = s.cortes.borrador_abierto ? "Corte en borrador" : "Último corte publicado";
      const hora = document.getElementById("sello-hora");
      hora.innerHTML = `<span class="sello__punto${s.estado === "OK" ? "" : " sello__punto--mal"}"></span>` +
                       U.esc(U.fecha(s.hora_cdmx, true)) + " CDMX";
      pendientes = s.base_de_datos.bandeja_pendiente || 0;
    } catch (e) {
      document.getElementById("sello-hora").innerHTML =
        '<span class="sello__punto sello__punto--mal"></span>sin conexión con el servidor';
    }
  }

  /* ----------------------------------------------------------- enrutador -- */
  function analizar() {
    const bruto = (location.hash || "#/inicio").replace(/^#\/?/, "");
    const [camino, consulta] = bruto.split("?");
    const partes = camino.split("/").filter(Boolean);
    return {
      ruta: partes[0] || "inicio",
      id: partes[1] ? decodeURIComponent(partes[1]) : null,
      params: new URLSearchParams(consulta || "")
    };
  }

  let ultimaRuta = null;
  async function enrutar(forzar) {
    const { ruta, id, params } = analizar();
    const seccion = SECCIONES.find((s) => s.ruta === ruta) || SECCIONES[0];
    const clave = location.hash;
    if (!forzar && clave === ultimaRuta) return;
    ultimaRuta = clave;

    Mapa.destruir();
    cerrarDialogo();
    pintarMenu(seccion.ruta);
    const contenedor = document.getElementById("vista");
    contenedor.innerHTML = U.cargando();
    window.scrollTo(0, 0);

    try {
      await catalogos();
      const vista = id && seccion.detalle ? seccion.detalle() : seccion.vista();
      await vista(contenedor, params, id);
      // El sello del corte y el contador de la bandeja cambian con lo que se
      // acaba de hacer: se releen al terminar de pintar, no cada minuto.
      await refrescarCabecera();
      pintarMenu(seccion.ruta);
    } catch (e) {
      contenedor.innerHTML = `<div class="vista__titulo"><h1>No se pudo abrir la sección</h1></div>
        <div class="aviso aviso--alerta"><b>${U.esc(e.message || "Error desconocido")}</b>
        <div class="pequeno tenue" style="margin-top:.3rem">Si el servidor está caído, la aplicación no
        inventa datos: prefiere no mostrar nada antes que mostrar algo que no puede sostener.</div></div>
        <button class="boton" onclick="location.reload()">Reintentar</button>`;
    }
  }

  function ir(hash, forzar) {
    if (location.hash === hash) { if (forzar) enrutar(true); return; }
    if (forzar) ultimaRuta = null;
    location.hash = hash;
  }

  /* ------------------------------------------------------------- arranque - */
  function iniciar() {
    document.getElementById("dialogo-cerrar").addEventListener("click", cerrarDialogo);
    document.getElementById("velo").addEventListener("click", (e) => {
      if (e.target.id === "velo") cerrarDialogo();
    });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") cerrarDialogo(); });
    window.addEventListener("hashchange", () => enrutar(false));

    if (!location.hash) location.hash = "#/inicio";
    refrescarCabecera().then(() => enrutar(true));
    setInterval(refrescarCabecera, 60000);
  }

  global.App = { avisar, dialogo, cerrarDialogo, pintarFiltros, catalogos, ir, SECCIONES };
  document.addEventListener("DOMContentLoaded", iniciar);
})(window);
