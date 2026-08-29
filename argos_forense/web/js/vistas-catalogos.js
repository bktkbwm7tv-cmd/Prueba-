/* ARGOS FORENSE — vistas de catálogo y control:
   Fuentes, Colectivos, Cortes, Tendencias, Bitácora y Configuración. */
(function (global) {
  "use strict";

  const V = {};

  /* ====================================================== FUENTES (§7) ==== */
  V.fuentes = async function (contenedor, params) {
    const filtros = { nivel: params.get("nivel") || "", entidad: params.get("entidad") || "",
                      q: params.get("q") || "" };
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Fuentes</h1>
        <p class="vista__nota">Cinco niveles: institucionales, prensa nacional, prensa estatal,
          prensa regional y municipal, y colectivos buscadores. El catálogo es ampliable.</p>
        <button class="boton boton--primario" id="btn-nueva-fuente">Añadir fuente</button>
      </div>
      <div id="fuentes-filtros"></div>
      <div id="fuentes-lista">${U.cargando()}</div>`;

    App.pintarFiltros("fuentes-filtros", [
      { nombre: "nivel", etiqueta: "Nivel", tipo: "select", valor: filtros.nivel,
        opciones: [["", "Todos"], ["1", "1 — Institucionales"], ["2", "2 — Prensa nacional"],
                   ["3", "3 — Prensa estatal"], ["4", "4 — Prensa regional y municipal"],
                   ["5", "5 — Colectivos"]] },
      { nombre: "entidad", etiqueta: "Entidad", tipo: "entidad", valor: filtros.entidad },
      { nombre: "q", etiqueta: "Buscar", tipo: "text", valor: filtros.q }
    ], "#/fuentes");

    document.getElementById("btn-nueva-fuente").addEventListener("click", dialogoNuevaFuente);

    const datos = await API.fuentes(filtros);
    const filas = datos.fuentes.map((f) => [
      `<span class="mono">N${f.nivel}</span>`,
      U.esc(f.nombre),
      U.esc(f.entidad || (f.ambito === "FEDERAL" ? "Federal" : "Nacional")),
      f.dominio ? `<span class="mono pequeno">${U.esc(f.dominio)}</span>`
                : '<span class="etiqueta etiqueta--alerta">SIN DOMINIO REGISTRADO</span>',
      f.clase_url ? `<span class="etiqueta" title="Clase de URL: A fechable, B semifechable, C opaca">${U.esc(f.clase_url)}</span>` : "—",
      f.verificado ? '<span class="etiqueta etiqueta--ok">verificada</span>'
                   : `<span class="etiqueta">${U.esc(f.estatus)}</span>`,
      f.ultima_revision ? U.esc(U.fecha(f.ultima_revision, true)) : '<span class="tenue">nunca</span>',
      `<button class="boton boton--chico" data-verificar="${f.id}">Sondear</button>`
    ]);

    document.getElementById("fuentes-lista").innerHTML = `
      <div class="rejilla rejilla--3" style="margin-bottom:.8rem">
        ${U.indicador(datos.total, "Fuentes en catálogo")}
        ${U.indicador(datos.verificadas, "Verificadas por sondeo", { clase: datos.verificadas ? "ok" : "" })}
        ${U.indicador(datos.sin_dominio_registrado, "Sin dominio canónico registrado", { clase: "alerta" })}
      </div>
      <div class="aviso aviso--seguridad">
        Una fuente sólo pasa a <b>verificada</b> cuando el sistema la sondea de verdad y anota lo que
        devolvió. Una fuente que no se pudo consultar nunca se reporta como fuente sin novedades.
      </div>
      <section class="panel">
        ${U.tabla(["Nivel", "Nombre", "Ámbito", "Dominio", "Clase", "Estatus", "Última revisión", ""], filas)}
      </section>`;

    document.querySelectorAll("[data-verificar]").forEach((b) =>
      b.addEventListener("click", async () => {
        b.disabled = true; b.textContent = "…";
        try {
          const r = await API.verificarFuente(Number(b.dataset.verificar));
          const sitio = r.sitio || {};
          App.avisar(`${r.nombre}: ${sitio.ok ? "responde correctamente" : (sitio.estado || r.nota || "sin sondear")}.`,
                     !sitio.ok);
        } catch (e) { App.avisar(e.message, true); }
        App.ir("#/fuentes", true);
      }));
  };

  function dialogoNuevaFuente() {
    App.catalogos().then((cat) => {
      const opcEnt = cat.entidades.map((e) => `<option value="${e.iso}">${U.esc(e.nombre)}</option>`).join("");
      App.dialogo("Añadir fuente", `
        <label><span>Nivel</span><select id="s-nivel">
          <option value="1">1 — Institucional</option><option value="2">2 — Prensa nacional</option>
          <option value="3" selected>3 — Prensa estatal</option>
          <option value="4">4 — Prensa regional o municipal</option>
        </select></label>
        <label style="margin-top:.5rem"><span>Nombre</span><input id="s-nombre"></label>
        <label style="margin-top:.5rem"><span>Ámbito</span><select id="s-ambito">
          <option value="ESTATAL">Estatal</option><option value="FEDERAL">Federal</option>
          <option value="NACIONAL">Nacional</option><option value="REGIONAL">Regional</option>
          <option value="MUNICIPAL">Municipal</option>
        </select></label>
        <label style="margin-top:.5rem"><span>Entidad</span>
          <select id="s-entidad"><option value="">— ninguna —</option>${opcEnt}</select></label>
        <label style="margin-top:.5rem"><span>Sitio (URL)</span><input id="s-sitio" type="url" placeholder="https://…"></label>
        <label style="margin-top:.5rem"><span>Canal RSS (si lo tiene)</span><input id="s-rss" type="url" placeholder="https://…/rss"></label>
        <label style="margin-top:.5rem"><span>Notas</span><textarea id="s-notas"></textarea></label>
        <p class="pequeno tenue">La fuente nace <b>sin verificar</b>. Use «Sondear» para comprobar qué devuelve.</p>`,
        [{ texto: "Añadir", clase: "boton--primario", accion: async () => {
            const nombre = document.getElementById("s-nombre").value.trim();
            if (nombre.length < 3) { App.avisar("El nombre es obligatorio.", true); return false; }
            await API.crearFuente({
              nivel: Number(document.getElementById("s-nivel").value), nombre,
              ambito: document.getElementById("s-ambito").value,
              entidad_iso: document.getElementById("s-entidad").value || null,
              url_sitio: document.getElementById("s-sitio").value.trim() || null,
              url_rss: document.getElementById("s-rss").value.trim() || null,
              notas: document.getElementById("s-notas").value.trim() || null
            });
            App.avisar("Fuente añadida al catálogo.");
            App.ir("#/fuentes", true);
          } }]);
    });
  }

  /* =================================================== COLECTIVOS (§7.5) == */
  V.colectivos = async function (contenedor) {
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Colectivos buscadores</h1>
        <p class="vista__nota">Nivel 5 del catálogo de fuentes.</p>
        <button class="boton boton--primario" id="btn-nuevo-colectivo">Añadir colectivo</button>
      </div>
      <div id="colectivos-lista">${U.cargando()}</div>`;

    document.getElementById("btn-nuevo-colectivo").addEventListener("click", dialogoNuevoColectivo);
    const datos = await API.colectivos({ activo: "true" });

    const filas = datos.colectivos.map((c) => {
      const paginas = [["Web", c.url_web], ["Facebook", c.url_facebook], ["Instagram", c.url_instagram],
                       ["X", c.url_x], ["TikTok", c.url_tiktok]]
        .filter(([, u]) => u)
        .map(([n, u]) => `<a href="${U.esc(u)}" target="_blank" rel="noopener noreferrer">${U.esc(n)}</a>`)
        .join(" · ");
      return [
        U.esc(c.nombre),
        U.esc(c.entidad),
        U.esc(U.texto(c.municipio_base)),
        paginas || '<span class="tenue pequeno">sin páginas registradas</span>',
        c.fecha_ultima_revision ? U.esc(U.fecha(c.fecha_ultima_revision)) : '<span class="tenue">nunca</span>',
        `<span class="etiqueta${c.estatus_fuente === "SIN VERIFICAR" ? "" : " etiqueta--ok"}">${U.esc(c.estatus_fuente)}</span>`,
        `<button class="boton boton--chico" data-editar="${c.id}">Editar</button>`
      ];
    });

    document.getElementById("colectivos-lista").innerHTML = `
      <div class="aviso aviso--seguridad">
        <b>Un reporte de colectivo no es una confirmación institucional.</b> ${U.esc(datos.distincion["REPORTE DE COLECTIVO"])}
        ${U.esc(datos.distincion["CONFIRMACIÓN INSTITUCIONAL"])}
      </div>
      <div class="aviso">${U.esc(datos.nota_seguridad)}</div>
      <section class="panel">
        ${U.tabla(["Colectivo", "Entidad", "Municipio base", "Páginas públicas", "Última revisión", "Estatus", ""], filas)}
      </section>`;

    document.querySelectorAll("[data-editar]").forEach((b) => b.addEventListener("click", () => {
      const c = datos.colectivos.find((x) => x.id === Number(b.dataset.editar));
      dialogoEditarColectivo(c);
    }));
  };

  function camposColectivo(c) {
    c = c || {};
    return `
      <label><span>Nombre</span><input id="c-nombre" value="${U.esc(c.nombre || "")}"></label>
      <label style="margin-top:.5rem"><span>Municipio base</span><input id="c-municipio" value="${U.esc(c.municipio_base || "")}"></label>
      <label style="margin-top:.5rem"><span>Página web</span><input id="c-web" type="url" value="${U.esc(c.url_web || "")}"></label>
      <label style="margin-top:.5rem"><span>Facebook</span><input id="c-fb" type="url" value="${U.esc(c.url_facebook || "")}"></label>
      <label style="margin-top:.5rem"><span>Instagram</span><input id="c-ig" type="url" value="${U.esc(c.url_instagram || "")}"></label>
      <label style="margin-top:.5rem"><span>X</span><input id="c-x" type="url" value="${U.esc(c.url_x || "")}"></label>
      <label style="margin-top:.5rem"><span>TikTok</span><input id="c-tt" type="url" value="${U.esc(c.url_tiktok || "")}"></label>
      <label style="margin-top:.5rem"><span>Estatus de la fuente</span><select id="c-estatus">
        ${["SIN VERIFICAR", "ACTIVA", "INTERMITENTE", "INACTIVA"].map((e) =>
          `<option value="${e}"${c.estatus_fuente === e ? " selected" : ""}>${e}</option>`).join("")}
      </select></label>
      <div class="aviso aviso--seguridad" style="margin-top:.6rem">
        Sólo páginas públicas. No registre domicilios, teléfonos ni datos de personas: la plataforma
        no los guarda ni los publica.
      </div>`;
  }

  function leerColectivo() {
    return {
      nombre: document.getElementById("c-nombre").value.trim(),
      municipio_base: document.getElementById("c-municipio").value.trim() || null,
      url_web: document.getElementById("c-web").value.trim() || null,
      url_facebook: document.getElementById("c-fb").value.trim() || null,
      url_instagram: document.getElementById("c-ig").value.trim() || null,
      url_x: document.getElementById("c-x").value.trim() || null,
      url_tiktok: document.getElementById("c-tt").value.trim() || null,
      estatus_fuente: document.getElementById("c-estatus").value
    };
  }

  function dialogoNuevoColectivo() {
    App.catalogos().then((cat) => {
      App.dialogo("Añadir colectivo", camposColectivo(null) +
        `<label style="margin-top:.5rem"><span>Entidad</span><select id="c-entidad">
          <option value="">— nacional —</option>
          ${cat.entidades.map((e) => `<option value="${e.iso}">${U.esc(e.nombre)}</option>`).join("")}
        </select></label>`,
        [{ texto: "Añadir", clase: "boton--primario", accion: async () => {
            const datos = leerColectivo();
            if (datos.nombre.length < 3) { App.avisar("El nombre es obligatorio.", true); return false; }
            datos.entidad_iso = document.getElementById("c-entidad").value || null;
            await API.crearColectivo(datos);
            App.avisar("Colectivo añadido.");
            App.ir("#/colectivos", true);
          } }]);
    });
  }

  function dialogoEditarColectivo(c) {
    App.dialogo("Editar colectivo", camposColectivo(c) +
      `<label style="margin-top:.5rem"><span>Motivo del cambio (obligatorio)</span><textarea id="c-motivo"></textarea></label>`,
      [{ texto: "Guardar", clase: "boton--primario", accion: async () => {
          const motivo = document.getElementById("c-motivo").value.trim();
          if (motivo.length < 3) { App.avisar("El motivo es obligatorio (§14).", true); return false; }
          await API.editarColectivo(c.id, Object.assign(leerColectivo(), { motivo }));
          App.avisar("Colectivo actualizado y anotado en la bitácora.");
          App.ir("#/colectivos", true);
        } }]);
  }

  /* ================================================= CORTES (§16-§18) ===== */
  V.cortes = async function (contenedor) {
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Cortes de 72 horas</h1>
        <p class="vista__nota">Un corte publicado queda sellado con SHA-256 y no se modifica.
          Cualquier cambio posterior aparece en el corte siguiente.</p>
        <span class="fila">
          <button class="boton" id="btn-generar-corte">Generar corte</button>
          <button class="boton boton--primario" id="btn-publicar-corte">Publicar borrador</button>
        </span>
      </div>
      <div id="cortes-lista">${U.cargando()}</div>`;

    document.getElementById("btn-generar-corte").addEventListener("click", async (ev) => {
      ev.currentTarget.disabled = true;
      try {
        const c = await API.generarCorte();
        App.avisar(`${c.etiqueta} generado como borrador.`);
      } catch (e) { App.avisar(e.message, true); }
      App.ir("#/cortes", true);
    });
    document.getElementById("btn-publicar-corte").addEventListener("click", () => {
      App.dialogo("Publicar el corte", `
        <div class="aviso aviso--alerta">Al publicar, el contenido del corte queda <b>congelado y
          sellado</b>. No podrá modificarse: lo que cambie después aparecerá en el corte siguiente.</div>
        <p class="pequeno tenue">Revise el borrador antes de continuar.</p>`,
        [{ texto: "Publicar y sellar", clase: "boton--primario", accion: async () => {
            try { const r = await API.publicarCorte(null);
              App.avisar(`${r.etiqueta} publicado. Sello ${r.sha256.slice(0, 16)}…`);
            } catch (e) { App.avisar(e.message, true); return false; }
            App.ir("#/cortes", true);
          } }]);
    });

    const datos = await API.cortes();
    const filas = datos.cortes.map((c) => [
      `<a href="#/cortes/${c.numero}">${U.esc(c.etiqueta)}</a>`,
      `<span class="etiqueta${c.estado === "PUBLICADO" ? " etiqueta--ok" : ""}">${U.esc(c.estado)}</span>`,
      U.esc(U.fecha(c.ventana_inicio, true)),
      U.esc(U.fecha(c.ventana_fin, true)),
      c.publicado_en ? U.esc(U.fecha(c.publicado_en, true)) : '<span class="tenue">—</span>',
      c.sha256 ? `<span class="mono pequeno" title="${U.esc(c.sha256)}">${U.esc(c.sha256.slice(0, 12))}…</span>`
               : '<span class="tenue">sin sellar</span>',
      c.estado === "PUBLICADO" ? `<a class="boton boton--chico" href="/api/cuts/${c.numero}/export.pdf">PDF</a>` : ""
    ]);
    document.getElementById("cortes-lista").innerHTML = `<section class="panel">
      ${U.tabla(["Corte", "Estado", "Inicio de ventana", "Cierre de ventana", "Publicado", "Sello", ""], filas,
        { tituloVacio: "Todavía no hay cortes", detalleVacio: "Genere el primero cuando haya eventos validados." })}
    </section>`;
  };

  V.corte = async function (contenedor, params, numero) {
    contenedor.innerHTML = U.cargando("Abriendo el corte…");
    const c = await API.corte(numero);
    const s = c.snapshot || {};
    const re = s.resumen_ejecutivo || {};
    const comp = s.comparacion || {};

    const bloqueCategoria = (clave, numero) => {
      const b = (s.categorias || {})[clave] || {};
      const nuevos = (b.nuevos || []).map((e) => [
        `<a href="#/eventos/${U.esc(e.folio)}">${U.folio(e.folio)}</a>`,
        U.esc(e.entidad), U.esc(U.texto(e.municipio)),
        U.distintivoNivel(e.nivel_corroboracion),
        `<span class="pequeno">${U.esc((e.resumen_factual || "").slice(0, 110))}</span>`
      ]);
      return `<section class="panel">
        <h2 class="panel__titulo">${numero}. ${U.esc(b.nombre || clave)} · ${b.total || 0} activo(s)</h2>
        <div class="fila" style="margin-bottom:.5rem">${["A", "B", "C", "D"].map((n) =>
          `<span class="fila" style="gap:.25rem">${U.distintivoNivel(n)}<b class="mono">${(b.por_nivel || {})[n] || 0}</b></span>`).join("")}</div>
        ${U.tabla(["Folio", "Entidad", "Municipio", "Nivel", "Resumen"], nuevos,
          { tituloVacio: "Sin eventos nuevos de esta categoría en el corte", detalleVacio: "" })}
      </section>`;
    };

    const bloqueLista = (titulo, lista) => `<section class="panel">
      <h2 class="panel__titulo">${U.esc(titulo)} · ${(lista || []).length}</h2>
      ${U.tabla(["Folio", "Cat.", "Entidad", "Municipio", "Nivel", "Fuentes", "Resumen"],
        (lista || []).map((e) => [
          `<a href="#/eventos/${U.esc(e.folio)}">${U.folio(e.folio)}</a>`,
          U.distintivoCategoria(e.categoria), U.esc(e.entidad), U.esc(U.texto(e.municipio)),
          U.distintivoNivel(e.nivel_corroboracion), `<span class="mono">${U.esc(e.num_fuentes)}</span>`,
          `<span class="pequeno">${U.esc((e.resumen_factual || "").slice(0, 100))}</span>`]),
        { tituloVacio: "Sin registros en este apartado del corte", detalleVacio: "" })}
    </section>`;

    const entidades = Object.entries(s.desglose_por_entidad || {})
      .filter(([, v]) => v.total > 0)
      .sort((a, b) => b[1].total - a[1].total)
      .map(([iso, v]) => [
        `<a href="#/estados/${U.esc(iso)}">${U.esc(v.entidad)}</a>`, U.esc(v.region),
        `<span class="mono">${v.por_categoria.FOS}</span>`,
        `<span class="mono">${v.por_categoria.CAM}</span>`,
        `<span class="mono">${v.por_categoria.CSE}</span>`,
        `<span class="mono">${v.nuevos}</span>`, `<span class="mono">${v.total}</span>`
      ]);

    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>${U.esc(c.etiqueta)}</h1>
        <p class="vista__nota">Ventana ${U.esc(U.fecha(c.ventana_inicio, true))} → ${U.esc(U.fecha(c.ventana_fin, true))}</p>
        <span class="fila">
          <span class="etiqueta${c.estado === "PUBLICADO" ? " etiqueta--ok" : ""}">${U.esc(c.estado)}</span>
          ${c.estado === "PUBLICADO" ? `<a class="boton boton--chico" href="/api/cuts/${c.numero}/export.pdf">Descargar PDF</a>
            <button class="boton boton--chico" id="btn-verificar-sello">Verificar sello</button>` : ""}
        </span>
      </div>

      ${c.estado === "PUBLICADO" ? `<div class="aviso aviso--ok">
        <b>Corte publicado e inmutable.</b> Sello SHA-256: <span class="mono">${U.esc(c.sha256)}</span>.
        Cualquier cambio posterior aparece en el corte siguiente.</div>`
      : `<div class="aviso aviso--seguridad"><b>Borrador.</b> Todavía puede regenerarse; al publicarlo
         quedará congelado y sellado.</div>`}

      <section class="panel">
        <h2 class="panel__titulo">1. Resumen ejecutivo</h2>
        <div class="rejilla">
          ${U.indicador(re.eventos_activos || 0, "Eventos activos")}
          ${U.indicador(re.nuevos_en_el_corte || 0, "Nuevos en el corte")}
          ${U.indicador(re.actualizados_en_el_corte || 0, "Actualizados")}
          ${U.indicador(re.confirmados || 0, "Confirmados", { clase: "ok" })}
          ${U.indicador(re.por_verificar || 0, "Por verificar", { clase: "alerta" })}
        </div>
        <p class="pequeno tenue" style="margin-top:.6rem">
          Entidades con actividad: <b class="mono">${re.entidades_con_actividad || 0}</b> de 32 ·
          Pendientes en bandeja al cierre: <b class="mono">${re.pendientes_en_bandeja || 0}</b>
        </p>
      </section>

      <section class="panel">
        <h2 class="panel__titulo">2. Total nacional</h2>
        <div class="rejilla rejilla--3">
          ${U.indicador((s.total_nacional || {}).por_categoria ? s.total_nacional.por_categoria.FOS : 0, "Fosas clandestinas", { clase: "fos" })}
          ${U.indicador((s.total_nacional || {}).por_categoria ? s.total_nacional.por_categoria.CAM : 0, "Campamentos", { clase: "cam" })}
          ${U.indicador((s.total_nacional || {}).por_categoria ? s.total_nacional.por_categoria.CSE : 0, "Casas de seguridad", { clase: "cse" })}
        </div>
      </section>

      ${bloqueCategoria("FOS", 3)}${bloqueCategoria("CAM", 4)}${bloqueCategoria("CSE", 5)}

      ${bloqueLista("6. Nuevos eventos", s.nuevos_eventos)}
      ${bloqueLista("7. Actualizaciones", s.actualizaciones)}
      ${bloqueLista("8. Eventos confirmados", s.eventos_confirmados)}
      ${bloqueLista("9. Eventos por verificar", s.eventos_por_verificar)}

      <section class="panel">
        <h2 class="panel__titulo">10. Desglose por entidad</h2>
        ${U.tabla(["Entidad", "Región", "Fosas", "Camp.", "Casas", "Nuevos", "Total"], entidades,
          { tituloVacio: "Ninguna entidad con eventos en el corte", detalleVacio: "" })}
      </section>

      <section class="panel">
        <h2 class="panel__titulo">11. Mapa nacional</h2>
        <p class="pequeno tenue">${U.esc((s.mapa_nacional || {}).nota || "")}
          El mapa interactivo del corte está en <a href="#/mapa">Mapa</a>; aquí queda congelado su
          conteo por entidad, que es el de la tabla del apartado 10.</p>
      </section>

      <section class="panel">
        <h2 class="panel__titulo">12. ${U.esc(comp.encabezado || "Comparación con el corte anterior")}</h2>
        ${comp.sin_corte_anterior
          ? `<p class="pequeno tenue">Es el primer corte de la serie: no hay con qué compararlo.</p>`
          : `<div class="fila" style="margin-bottom:.6rem">
               ${U.indicador(comp.nuevos_eventos || 0, "Nuevos")}
               ${U.indicador(comp.eventos_actualizados || 0, "Actualizados")}
               ${U.indicador((comp.cambios_de_nivel || []).length, "Cambios de nivel")}
             </div>
             ${U.tabla(["Folio", "Corte anterior", "Corte actual", "Motivo"],
               (comp.cambios_de_nivel || []).map((x) => [
                 `<a href="#/eventos/${U.esc(x.folio)}">${U.folio(x.folio)}</a>`,
                 U.distintivoNivel(x.corte_anterior), U.distintivoNivel(x.corte_actual),
                 `<span class="pequeno">${U.esc(x.motivo)}</span>`]),
               { tituloVacio: "Sin cambios de nivel", detalleVacio: "" })}
             ${(comp.nuevos_estados_con_actividad || []).length
               ? `<p class="pequeno tenue" style="margin-top:.5rem">Nuevos estados con actividad:
                  <b>${U.esc(comp.nuevos_estados_con_actividad.join(", "))}</b></p>` : ""}`}
      </section>

      <section class="panel">
        <h2 class="panel__titulo">13. Fuentes utilizadas</h2>
        ${U.tabla(["Nivel", "Medio o institución", "Publicaciones"],
          (s.fuentes_utilizadas || []).map((f) => [`<span class="mono">N${f.nivel}</span>`, U.esc(f.medio),
                                                   `<span class="mono">${f.notas}</span>`]),
          { tituloVacio: "Sin fuentes nuevas ligadas en la ventana", detalleVacio: "" })}
      </section>

      <section class="panel">
        <h2 class="panel__titulo">14. Pendientes de corroboración</h2>
        ${U.tabla(["Folio", "Nivel", "Resumen"],
          (s.pendientes_de_corroboracion || []).map((p) => [
            `<a href="#/eventos/${U.esc(p.folio)}">${U.folio(p.folio)}</a>`,
            U.distintivoNivel(p.nivel_corroboracion),
            `<span class="pequeno">${U.esc((p.resumen_factual || "").slice(0, 120))}</span>`]),
          { tituloVacio: "Nada pendiente de corroboración", detalleVacio: "" })}
      </section>

      <section class="panel">
        <h2 class="panel__titulo">15. Metodología · 16. Bitácora de integridad</h2>
        <div class="campos">
          ${Object.entries((s.metodologia || {}).niveles_corroboracion || {}).map(([k, v]) =>
            U.campo("Nivel " + k, U.esc(v))).join("")}
          ${Object.entries(s.bitacora_integridad || {}).map(([k, v]) =>
            U.campo(k.replace(/_/g, " "), `<span class="mono">${U.esc(v === null ? "—" : v)}</span>`)).join("")}
        </div>
        <ul class="pequeno tenue" style="margin:.6rem 0 0;padding-left:1.1rem">
          ${["regla_de_validacion", "regla_de_duplicidad", "regla_de_atribucion", "regla_de_seguridad"]
            .filter((k) => (s.metodologia || {})[k])
            .map((k) => `<li>${U.esc(s.metodologia[k])}</li>`).join("")}
        </ul>
      </section>`;

    const btn = document.getElementById("btn-verificar-sello");
    if (btn) btn.addEventListener("click", async () => {
      const r = await API.verificarCorte(numero);
      App.avisar(r.integro
        ? "Sello íntegro: el contenido publicado no ha cambiado."
        : "ALERTA: el sello no coincide con el contenido almacenado.", !r.integro);
    });
  };

  /* ==================================================== TENDENCIAS ======== */
  V.tendencias = async function (contenedor) {
    contenedor.innerHTML = U.cargando();
    const t = await API.tendencias();
    if (!t.serie.length) {
      contenedor.innerHTML = `
        <div class="vista__titulo"><h1>Tendencias</h1></div>
        ${U.vacio("Todavía no hay serie histórica", t.nota)}`;
      return;
    }
    const maximo = Math.max(...t.serie.map((c) => c.por_categoria.FOS + c.por_categoria.CAM + c.por_categoria.CSE), 1);
    const barras = t.serie.map((c) => {
      const total = c.por_categoria.FOS + c.por_categoria.CAM + c.por_categoria.CSE;
      const segmento = (v, color) => v ? `<div style="height:${(v / maximo) * 100}%;background:${color}"></div>` : "";
      return `<div style="display:flex;flex-direction:column;align-items:center;gap:.25rem;
                          flex:0 0 auto;width:46px">
        <div style="display:flex;flex-direction:column-reverse;justify-content:flex-start;height:130px;width:100%;
                    background:var(--fondo-alt);border-radius:2px;overflow:hidden">
          ${segmento(c.por_categoria.FOS, "var(--fos)")}
          ${segmento(c.por_categoria.CAM, "var(--cam)")}
          ${segmento(c.por_categoria.CSE, "var(--cse)")}
        </div>
        <span class="mono pequeno">${total}</span>
        <span class="pequeno tenue">${String(c.corte).padStart(3, "0")}</span>
      </div>`;
    }).join("");

    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Tendencias</h1>
        <p class="vista__nota">Serie construida sobre cortes publicados. Cada barra es un corte
          sellado, comparable con los demás porque su contenido ya no cambia.</p>
      </div>
      <section class="panel">
        <h2 class="panel__titulo">Eventos por corte y categoría</h2>
        <div style="display:flex;gap:.3rem;align-items:flex-end;overflow-x:auto;padding:.4rem 0">${barras}</div>
        <div class="leyenda" style="margin-top:.6rem">
          <span><span class="leyenda__punto" style="background:var(--fos)"></span>Fosas</span>
          <span><span class="leyenda__punto" style="background:var(--cam)"></span>Campamentos</span>
          <span><span class="leyenda__punto" style="background:var(--cse)"></span>Casas de seguridad</span>
        </div>
      </section>
      <section class="panel">
        <h2 class="panel__titulo">Detalle por corte</h2>
        ${U.tabla(["Corte", "Cierre", "Fosas", "Camp.", "Casas", "Nuevos", "A", "B", "C", "D", "Entidades"],
          t.serie.slice().reverse().map((c) => [
            `<a href="#/cortes/${c.corte}">${U.esc(c.etiqueta)}</a>`, U.esc(U.fecha(c.cierre, true)),
            `<span class="mono">${c.por_categoria.FOS}</span>`, `<span class="mono">${c.por_categoria.CAM}</span>`,
            `<span class="mono">${c.por_categoria.CSE}</span>`, `<span class="mono">${c.nuevos}</span>`,
            `<span class="mono">${c.por_nivel.A}</span>`, `<span class="mono">${c.por_nivel.B}</span>`,
            `<span class="mono">${c.por_nivel.C}</span>`, `<span class="mono">${c.por_nivel.D}</span>`,
            `<span class="mono">${c.entidades}</span>`]))}
      </section>`;
  };

  /* ==================================================== BITÁCORA (§14) ==== */
  V.bitacora = async function (contenedor, params) {
    const filtros = { entidad_tipo: params.get("entidad_tipo") || "", evento: params.get("evento") || "",
                      usuario: params.get("usuario") || "", proceso: params.get("proceso") || "" };
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Bitácora</h1>
        <p class="vista__nota">Cada modificación queda registrada con fecha, hora, usuario, proceso,
          campo, valor anterior, valor nuevo, motivo y fuente. La bitácora sólo admite altas.</p>
      </div>
      <div id="bitacora-filtros"></div>
      <div id="bitacora-lista">${U.cargando()}</div>`;

    App.pintarFiltros("bitacora-filtros", [
      { nombre: "entidad_tipo", etiqueta: "Tipo", tipo: "select", valor: filtros.entidad_tipo,
        opciones: [["", "Todos"], ["event", "Eventos"], ["raw_item", "Bandeja"], ["source", "Fuentes"],
                   ["collective", "Colectivos"], ["cut", "Cortes"], ["duplicate_candidate", "Duplicados"],
                   ["config", "Configuración"]] },
      { nombre: "evento", etiqueta: "Folio", tipo: "text", valor: filtros.evento },
      { nombre: "usuario", etiqueta: "Usuario", tipo: "text", valor: filtros.usuario },
      { nombre: "proceso", etiqueta: "Proceso", tipo: "text", valor: filtros.proceso }
    ], "#/bitacora");

    const datos = await API.bitacora(Object.assign({ limite: 300 }, filtros));
    const filas = datos.movimientos.map((m) => [
      `<span class="marca-tiempo">${U.esc(m.fecha)} ${U.esc(m.hora)}</span>`,
      U.esc(m.usuario),
      `<span class="etiqueta">${U.esc(m.proceso)}</span>`,
      m.evento ? `<a href="#/eventos/${U.esc(m.evento)}">${U.folio(m.evento)}</a>`
               : `<span class="pequeno tenue">${U.esc(m.entidad_tipo)} #${U.esc(m.entidad_id)}</span>`,
      U.esc(U.texto(m.campo)),
      `<span class="pequeno"><s class="tenue">${U.esc(U.texto(m.valor_anterior, ""))}</s> ${U.esc(U.texto(m.valor_nuevo, ""))}</span>`,
      `<span class="pequeno">${U.esc(U.texto(m.motivo, ""))}</span>`
    ]);
    document.getElementById("bitacora-lista").innerHTML = `
      <p class="pequeno tenue">${datos.total} movimiento(s). ${U.esc(datos.nota)}</p>
      <section class="panel">
        ${U.tabla(["Fecha y hora", "Usuario", "Proceso", "Registro", "Campo", "Anterior → nuevo", "Motivo"], filas)}
      </section>`;
  };

  /* =============================================== CONFIGURACIÓN (§26) ==== */
  V.configuracion = async function (contenedor) {
    contenedor.innerHTML = U.cargando();
    const [cfg, salud] = await Promise.all([API.configuracion(), API.salud()]);
    const p = cfg.programador;

    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Configuración</h1>
        <p class="vista__nota">Los intervalos del programador se cambian en caliente y quedan
          registrados en la bitácora.</p>
      </div>

      <section class="panel">
        <h2 class="panel__titulo">Operador</h2>
        <p class="pequeno tenue">Este nombre firma cada validación, corrección y descarte en la bitácora.</p>
        <div class="fila">
          <label class="crece"><span>Usuario</span><input id="cfg-usuario" value="${U.esc(API.usuario())}"
            placeholder="p. ej. analista.rodriguez"></label>
          <button class="boton" id="cfg-guardar-usuario" style="align-self:flex-end">Guardar</button>
        </div>
      </section>

      <section class="panel">
        <h2 class="panel__titulo">Programador</h2>
        <div class="fila">
          <label class="crece"><span>Rastreo cada (minutos)</span>
            <input id="cfg-rastreo" type="number" min="5" max="1440" value="${U.esc(p.rastreo_minutos)}"></label>
          <label class="crece"><span>Corte cada (horas)</span>
            <input id="cfg-corte" type="number" min="1" max="720" value="${U.esc(p.corte_horas)}"></label>
          <button class="boton boton--primario" id="cfg-guardar-intervalos" style="align-self:flex-end">Aplicar</button>
        </div>
        <div class="campos" style="margin-top:.6rem">
          ${U.campo("Programador activo", p.activo ? "sí" : "no — este proceso no ejecuta las tareas")}
          ${U.campo("Publicación automática del corte", p.corte_autopublica
            ? '<span class="etiqueta etiqueta--alerta">activada</span>'
            : "desactivada — el corte se genera como borrador y lo publica una persona")}
          ${(p.tareas || []).map((t) => U.campo(t.nombre, t.proxima_ejecucion
            ? "próxima ejecución " + U.fecha(t.proxima_ejecucion, true) : "sin programar")).join("")}
        </div>
      </section>

      <section class="panel">
        <h2 class="panel__titulo">Recolección y seguridad</h2>
        <div class="campos">
          ${U.campo("Ventana de búsqueda", cfg.recoleccion.ventana_dias + " día(s)")}
          ${U.campo("Máximo de publicaciones por fuente", cfg.recoleccion.max_items_por_fuente)}
          ${U.campo("Respeta robots.txt", cfg.recoleccion.respetar_robots
            ? '<span class="etiqueta etiqueta--ok">sí</span>'
            : '<span class="etiqueta etiqueta--alerta">no</span>')}
          ${U.campo("Tiempo de espera HTTP", cfg.recoleccion.http_timeout + " s")}
          ${U.campo("Umbral de duplicidad", cfg.deduplicacion.umbral_duplicado + " %")}
          ${U.campo("Expone el punto exacto", cfg.seguridad.exponer_punto_exacto
            ? '<span class="etiqueta etiqueta--alerta">sí</span>'
            : '<span class="etiqueta etiqueta--ok">no</span>')}
          ${U.campo("Base de datos", `<span class="mono pequeno">${U.esc(cfg.almacenamiento.base_de_datos)}</span>`)}
          ${U.campo("Almacén de evidencia", `<span class="mono pequeno">${U.esc(cfg.almacenamiento.evidencia)}</span>`)}
        </div>
        <p class="pequeno tenue" style="margin-top:.5rem">${U.esc(cfg.seguridad.nota)}</p>
      </section>

      <section class="panel">
        <h2 class="panel__titulo">Estado del sistema</h2>
        <div class="campos">
          ${U.campo("Versión", U.esc(salud.version))}
          ${U.campo("Estado", `<span class="etiqueta${salud.estado === "OK" ? " etiqueta--ok" : " etiqueta--alerta"}">${U.esc(salud.estado)}</span>`)}
          ${U.campo("Hora de Ciudad de México", U.esc(U.fecha(salud.hora_cdmx, true)))}
          ${U.campo("Motor de base de datos", U.esc(salud.base_de_datos.motor))}
          ${U.campo("Eventos registrados", `<span class="mono">${U.esc(salud.base_de_datos.eventos)}</span>`)}
          ${U.campo("Pendientes en bandeja", `<span class="mono">${U.esc(salud.base_de_datos.bandeja_pendiente)}</span>`)}
          ${U.campo("Documentación de la API", '<a href="/api/docs" target="_blank" rel="noopener">/api/docs</a>')}
        </div>
      </section>`;

    document.getElementById("cfg-guardar-usuario").addEventListener("click", () => {
      API.fijarUsuario(document.getElementById("cfg-usuario").value.trim());
      App.avisar("Operador guardado en este dispositivo.");
    });
    document.getElementById("cfg-guardar-intervalos").addEventListener("click", async () => {
      try {
        await API.programador({
          rastreo_minutos: Number(document.getElementById("cfg-rastreo").value),
          corte_horas: Number(document.getElementById("cfg-corte").value)
        });
        App.avisar("Intervalos aplicados y registrados en la bitácora.");
        App.ir("#/configuracion", true);
      } catch (e) { App.avisar(e.message, true); }
    });
  };

  global.VistasCatalogos = V;
})(window);
