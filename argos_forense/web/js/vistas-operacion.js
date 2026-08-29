/* ARGOS FORENSE — vistas de operación: Inicio, Mapa, Bandeja, Eventos, Estados. */
(function (global) {
  "use strict";

  const V = {};

  /* ======================================================= INICIO (§2) ==== */
  V.inicio = async function (contenedor) {
    contenedor.innerHTML = U.cargando("Calculando el tablero…");
    const t = await API.tablero();
    const d = t.detalle;

    const indicadores = [
      U.indicador(t.fosas_detectadas, "Fosas clandestinas", { clase: "fos" }),
      U.indicador(t.campamentos, "Campamentos", { clase: "cam" }),
      U.indicador(t.casas_de_seguridad, "Casas de seguridad", { clase: "cse" }),
      U.indicador(t.eventos_nuevos, "Eventos nuevos", { pie: "en la ventana del corte" }),
      U.indicador(t.eventos_actualizados, "Eventos actualizados", { pie: "en la ventana del corte" }),
      U.indicador(t.eventos_confirmados, "Eventos confirmados", { clase: "ok", pie: "nivel A" }),
      U.indicador(t.eventos_por_verificar, "Eventos por verificar", { clase: "alerta", pie: "nivel D" }),
      U.indicador(t.entidades_con_actividad, "Entidades con actividad", { pie: "de 32" }),
      U.indicador(t.fuentes_analizadas, "Fuentes en catálogo"),
      U.indicador(t.registros_pendientes_de_validacion, "Pendientes de validación",
                  { clase: t.registros_pendientes_de_validacion ? "alerta" : "" })
    ].join("");

    const niveles = ["A", "B", "C", "D"].map((n) => {
      const total = d.total_activos || 1;
      const v = d.por_nivel[n] || 0;
      const pct = Math.round((v / total) * 100);
      return `<div style="margin-bottom:.5rem">
        <div class="fila fila--sep pequeno">${U.distintivoNivel(n)}<b class="mono">${v}</b></div>
        <div class="barra"><div class="barra__relleno" style="width:${pct}%;background:${U.colorNivel(n)}"></div></div>
      </div>`;
    }).join("");

    const bandeja = Object.entries(d.registros_en_bandeja).map(([k, v]) =>
      `<div class="fila fila--sep pequeno"><span class="tenue">${U.esc(k)}</span><b class="mono">${U.esc(v)}</b></div>`
    ).join("");

    const rastreo = d.ultimo_rastreo;

    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Tablero nacional</h1>
        <p class="vista__nota">Ventana del corte: ${U.esc(U.fecha(t.ventana.inicio, true))} → ${U.esc(U.fecha(t.ventana.fin, true))}
          ${t.corte_vigente ? ` · ${U.esc(t.corte_vigente.etiqueta)} (${U.esc(t.corte_vigente.estado)})` : " · sin corte abierto"}</p>
        <button class="boton boton--primario" id="btn-rastrear">Ejecutar rastreo</button>
      </div>

      <div class="aviso aviso--seguridad">
        <b>ARGOS FORENSE no es un agregador de noticias.</b> Todo lo detectado entra a la bandeja de
        validación y sólo una persona lo convierte en evento con folio. La plataforma no publica
        coordenadas precisas, domicilios ni datos personales, y no atribuye ningún sitio a una
        organización que ninguna fuente identificable haya nombrado.
      </div>

      <div class="rejilla" style="margin-bottom:.9rem">${indicadores}</div>

      <div class="rejilla--ancha" style="display:grid;gap:.8rem">
        <section class="panel">
          <h2 class="panel__titulo">Nivel de corroboración del acervo activo</h2>
          ${d.total_activos ? niveles : U.vacio("Sin eventos activos", "El acervo se llena validando en la bandeja.")}
          <p class="pequeno tenue" style="margin:.6rem 0 0">
            Un evento en nivel D no se presenta como hecho confirmado.
          </p>
        </section>

        <section class="panel">
          <h2 class="panel__titulo">Bandeja y control</h2>
          ${bandeja}
          <div class="fila fila--sep pequeno" style="margin-top:.4rem;padding-top:.4rem;border-top:1px solid var(--borde-suave)">
            <span class="tenue">Duplicados abiertos</span><b class="mono">${U.esc(d.duplicados_abiertos)}</b>
          </div>
          <div class="fila fila--sep pequeno">
            <span class="tenue">Cortes publicados</span><b class="mono">${U.esc(d.cortes_publicados)}</b>
          </div>
          <div class="fila fila--sep pequeno">
            <span class="tenue">Colectivos registrados</span><b class="mono">${U.esc(d.colectivos_registrados)}</b>
          </div>
        </section>
      </div>

      <section class="panel">
        <h2 class="panel__titulo">Último rastreo</h2>
        ${rastreo ? `
          <div class="campos">
            ${U.campo("Cierre", U.fecha(rastreo.fin, true))}
            ${U.campo("Consultas lanzadas", `<span class="mono">${U.esc(rastreo.consultas)}</span>`)}
            ${U.campo("Publicaciones vistas", `<span class="mono">${U.esc(rastreo.publicaciones_vistas)}</span>`)}
            ${U.campo("Altas en bandeja", `<span class="mono">${U.esc(rastreo.altas_en_bandeja)}</span>`)}
            ${U.campo("Ya conocidas", `<span class="mono">${U.esc(rastreo.ya_conocidas)}</span>`)}
            ${U.campo("Fuentes con error", `<span class="mono">${U.esc(rastreo.fuentes_con_error)}</span>`)}
          </div>
          ${rastreo.errores && rastreo.errores.length ? `
            <p class="pequeno tenue" style="margin-top:.6rem">
              Fuentes que no se pudieron consultar en la última vuelta — no son fuentes sin novedades:
            </p>
            ${U.tabla(["Fuente", "Diagnóstico"], rastreo.errores.slice(0, 12).map((e) =>
              [U.esc(e.fuente), `<span class="etiqueta etiqueta--alerta">${U.esc(e.estado)}</span>`]))}
          ` : ""}
        ` : U.vacio("Todavía no se ha ejecutado un rastreo", "Use «Ejecutar rastreo» o espere al programador.")}
      </section>`;

    document.getElementById("btn-rastrear").addEventListener("click", async (ev) => {
      const boton = ev.currentTarget;
      boton.disabled = true; boton.textContent = "Rastreando…";
      try {
        const r = await API.rastrear({});
        App.avisar(`Rastreo terminado: ${r.altas_en_bandeja} alta(s) en bandeja de ` +
                   `${r.publicaciones_vistas} publicación(es) vistas, ${r.fuentes_con_error} fuente(s) con error.`);
        App.ir("#/inicio", true);
      } catch (e) {
        App.avisar("El rastreo falló: " + e.message, true);
        boton.disabled = false; boton.textContent = "Ejecutar rastreo";
      }
    });
  };

  /* ========================================================= MAPA (§3) ==== */
  V.mapa = async function (contenedor) {
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Mapa nacional</h1>
        <p class="vista__nota">Las 32 entidades federativas. El color indica el mejor nivel de
          corroboración sostenido en la entidad, no el número de eventos. Toque un estado para su ficha.</p>
      </div>
      <div class="aviso aviso--seguridad">
        La unidad de representación es la <b>entidad federativa</b>. ARGOS FORENSE no publica en el mapa
        coordenadas tácticas ni el punto fino de ningún sitio.
      </div>
      <div id="mapa"></div>
      <div class="panel" style="margin-top:.6rem">${Mapa.leyenda()}</div>
      <div id="mapa-tabla">${U.cargando("Cargando la geometría nacional…")}</div>`;

    const geo = await API.geojson();
    Mapa.crear("mapa", geo, {});

    const filas = geo.features
      .map((f) => f.properties)
      .filter((p) => p.total > 0)
      .sort((a, b) => b.total - a.total)
      .map((p) => [
        `<a href="#/estados/${U.esc(p.id)}">${U.esc(p.nombre)}</a>`,
        U.esc(p.region || "—"),
        `<span class="mono">${p.fosas}</span>`,
        `<span class="mono">${p.campamentos}</span>`,
        `<span class="mono">${p.casas_de_seguridad}</span>`,
        `<span class="mono">${p.eventos_nuevos}</span>`,
        p.nivel_corroboracion_max ? U.distintivoNivel(p.nivel_corroboracion_max) : "—",
        `<span class="mono">${p.total}</span>`
      ]);

    document.getElementById("mapa-tabla").innerHTML = `<section class="panel">
      <h2 class="panel__titulo">Entidades con actividad registrada</h2>
      ${U.tabla(["Entidad", "Región", "Fosas", "Camp.", "Casas", "Nuevos", "Nivel máx.", "Total"], filas,
        { tituloVacio: "Ninguna entidad tiene eventos registrados",
          detalleVacio: "El mapa se colorea con los eventos validados; todavía no hay ninguno." })}
    </section>`;
  };

  /* ====================================================== BANDEJA (§8) ==== */
  V.bandeja = async function (contenedor, params) {
    const filtros = {
      estado: params.get("estado") || "PENDIENTE",
      categoria: params.get("categoria") || "",
      entidad: params.get("entidad") || "",
      confianza_min: params.get("confianza_min") || "",
      q: params.get("q") || ""
    };
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Bandeja de validación</h1>
        <p class="vista__nota">Nada detectado por el rastreo pasa solo al registro definitivo.
          El folio forense se emite aquí, al validar.</p>
        <button class="boton" id="btn-rastrear-bandeja">Ejecutar rastreo</button>
      </div>
      <div id="bandeja-filtros"></div>
      <div id="bandeja-lista">${U.cargando()}</div>`;

    App.pintarFiltros("bandeja-filtros", [
      { nombre: "estado", etiqueta: "Estado", tipo: "select", valor: filtros.estado,
        opciones: [["PENDIENTE", "Pendiente"], ["VALIDADO", "Validado"], ["DESCARTADO", "Descartado"],
                   ["DUPLICADO", "Duplicado"], ["VINCULADO", "Vinculado"], ["", "Todos"]] },
      { nombre: "categoria", etiqueta: "Categoría", tipo: "select", valor: filtros.categoria,
        opciones: [["", "Todas"], ["FOS", "Fosas"], ["CAM", "Campamentos"], ["CSE", "Casas de seguridad"]] },
      { nombre: "entidad", etiqueta: "Entidad", tipo: "entidad", valor: filtros.entidad },
      { nombre: "confianza_min", etiqueta: "Confianza mínima", tipo: "number", valor: filtros.confianza_min },
      { nombre: "q", etiqueta: "Buscar", tipo: "text", valor: filtros.q }
    ], "#/bandeja");

    document.getElementById("btn-rastrear-bandeja").addEventListener("click", async (ev) => {
      ev.currentTarget.disabled = true;
      try {
        const r = await API.rastrear({});
        App.avisar(`Rastreo terminado: ${r.altas_en_bandeja} alta(s) nueva(s).`);
        App.ir("#/bandeja", true);
      } catch (e) { App.avisar("El rastreo falló: " + e.message, true); }
    });

    const datos = await API.bandeja(filtros);
    const lista = document.getElementById("bandeja-lista");
    if (!datos.items.length) {
      lista.innerHTML = U.vacio("No hay registros con esos filtros",
        "Ejecute un rastreo o cambie el estado del filtro.");
      return;
    }

    lista.innerHTML = `<p class="pequeno tenue">${datos.total} registro(s).</p>` +
      datos.items.map(fichaBandeja).join("");
    lista.querySelectorAll("[data-accion]").forEach((b) =>
      b.addEventListener("click", () => accionBandeja(b.dataset.accion, Number(b.dataset.id))));
  };

  function fichaBandeja(it) {
    const opsec = (it.riesgo_opsec && it.riesgo_opsec.tipos) || [];
    const acciones = it.estado === "PENDIENTE" ? `
      <div class="ficha__acciones">
        <button class="boton boton--primario" data-accion="validar" data-id="${it.id}">Validar</button>
        <button class="boton boton--peligro" data-accion="descartar" data-id="${it.id}">Descartar</button>
        <button class="boton" data-accion="duplicado" data-id="${it.id}">Posible duplicado</button>
        <button class="boton" data-accion="vincular" data-id="${it.id}">Vincular a evento</button>
        <a class="boton boton--fantasma" href="${U.esc(it.url)}" target="_blank" rel="noopener noreferrer">Abrir fuente</a>
      </div>` : `
      <div class="ficha__acciones">
        <span class="etiqueta">${U.esc(it.estado)}</span>
        ${it.folio ? `<a class="boton boton--chico" href="#/eventos/${U.esc(it.folio)}">${U.esc(it.folio)}</a>` : ""}
        ${it.motivo ? `<span class="pequeno tenue">${U.esc(it.motivo)}</span>` : ""}
        <a class="boton boton--fantasma boton--chico" href="${U.esc(it.url)}" target="_blank" rel="noopener noreferrer">Abrir fuente</a>
      </div>`;

    return `<article class="ficha">
      <div class="ficha__cabeza">
        ${U.distintivoCategoria(it.categoria_detectada)}
        <span class="etiqueta">Confianza ${U.esc(it.confianza_pct)} %</span>
        ${it.duplicados_abiertos ? `<span class="etiqueta etiqueta--alerta">${it.duplicados_abiertos} posible(s) duplicado(s)</span>` : ""}
        ${opsec.length ? `<span class="etiqueta etiqueta--alerta" title="Datos que no se publican (§20)">§20: ${U.esc(opsec.join(", "))}</span>` : ""}
        <span class="crece"></span>
        ${U.marcaTiempo(it.fecha_deteccion, "Detectado ")}
      </div>
      <div class="ficha__cuerpo">
        <h3 class="ficha__titulo">${U.esc(it.titulo)}</h3>
        <div class="ficha__meta">
          <span>Medio: <b>${U.esc(U.texto(it.medio))}</b></span>
          <span>Publicado: <b>${U.esc(U.fecha(it.fecha_publicacion))}</b></span>
          <span>Entidad probable: <b>${U.esc(U.texto(it.entidad))}</b>
            ${it.entidad_confianza ? `<span class="tenue">(${it.entidad_confianza} %)</span>` : ""}</span>
          ${it.municipio ? `<span>Municipio: <b>${U.esc(it.municipio)}</b></span>` : ""}
          ${it.subcategoria ? `<span>Subcategoría: <b>${U.esc(it.subcategoria)}</b></span>` : ""}
        </div>
        ${it.resumen ? `<p class="ficha__resumen">${U.esc(it.resumen)}</p>` : ""}
        <p class="pequeno tenue recorte">${U.esc(it.url)}</p>
        ${(it.terminos || []).length ? `<p class="pequeno tenue">Términos: ${U.esc(it.terminos.join(" · "))}</p>` : ""}
        ${acciones}
      </div>
    </article>`;
  }

  async function accionBandeja(accion, id) {
    const item = await API.bandejaItem(id);
    if (accion === "descartar") {
      App.dialogo("Descartar registro", `
        <p class="pequeno tenue">El registro no se borra: queda con estado DESCARTADO y el motivo
          en la bitácora.</p>
        <label><span>Motivo (obligatorio)</span><textarea id="d-motivo"
          placeholder="p. ej. La nota no describe un hecho de las tres categorías."></textarea></label>`,
        [{ texto: "Descartar", clase: "boton--peligro", accion: async () => {
            const motivo = document.getElementById("d-motivo").value.trim();
            if (motivo.length < 3) { App.avisar("El motivo es obligatorio.", true); return false; }
            await API.descartar(id, motivo);
            App.avisar("Registro descartado y anotado en la bitácora.");
            App.ir("#/bandeja", true);
          } }]);
      return;
    }
    if (accion === "duplicado") {
      const dup = await API.duplicados(id);
      const filas = (dup.candidatos || []).map((c) => [
        c.folio ? `<a href="#/eventos/${U.esc(c.folio)}">${U.esc(c.folio)}</a>`
                : `<span class="mono">bandeja #${U.esc(c.otro_raw_id)}</span>`,
        `<b class="mono">${U.esc(c.puntaje)} %</b>`,
        `<span class="pequeno tenue">${U.esc((c.desglose._meta && c.desglose._meta.criterios_comparados || []).join(", "))}</span>`,
        c.estado === "ABIERTO" && c.folio
          ? `<span class="fila">
               <button class="boton boton--chico" data-dup="${c.id}" data-decision="FUSIONAR">Fusionar</button>
               <button class="boton boton--chico" data-dup="${c.id}" data-decision="VINCULAR">Vincular</button>
               <button class="boton boton--chico" data-dup="${c.id}" data-decision="MANTENER_SEPARADOS">Separados</button>
             </span>`
          : `<span class="etiqueta">${U.esc(c.estado)}</span>`
      ]);
      App.dialogo("Posibles duplicados", `
        <p class="pequeno tenue">${U.esc(dup.nota)}</p>
        ${U.tabla(["Registro", "Puntaje", "Criterios comparados", "Decisión"], filas,
          { tituloVacio: "Sin candidatos por encima del umbral",
            detalleVacio: "Nada en el acervo se parece lo bastante a este registro." })}
        <hr style="border:0;border-top:1px solid var(--borde-suave);margin:.8rem 0">
        <p class="pequeno tenue">También puede apartarlo sin decidir todavía:</p>
        <label><span>Motivo</span><textarea id="d-motivo" placeholder="p. ej. Coincide con AF-… , pendiente de arbitraje."></textarea></label>`,
        [{ texto: "Marcar como posible duplicado", accion: async () => {
            const motivo = document.getElementById("d-motivo").value.trim() || "Marcado como posible duplicado";
            await API.posibleDuplicado(id, motivo);
            App.avisar("Registro apartado como posible duplicado.");
            App.ir("#/bandeja", true);
          } }],
        (cuerpo) => {
          cuerpo.querySelectorAll("[data-dup]").forEach((b) => b.addEventListener("click", async () => {
            const motivo = prompt("Motivo de la decisión (queda en la bitácora):", "");
            if (!motivo || motivo.trim().length < 3) { App.avisar("El motivo es obligatorio.", true); return; }
            await API.resolverDuplicado(Number(b.dataset.dup), { decision: b.dataset.decision, motivo: motivo.trim() });
            App.avisar("Decisión registrada.");
            App.cerrarDialogo(); App.ir("#/bandeja", true);
          }));
        });
      return;
    }
    if (accion === "vincular") {
      const eventos = await API.eventos({ limite: 300, categoria: item.categoria_detectada || "" });
      const opciones = eventos.eventos.map((e) =>
        `<option value="${U.esc(e.folio)}">${U.esc(e.folio)} · ${U.esc(e.entidad)} · ${U.esc((e.resumen_factual || "").slice(0, 70))}</option>`).join("");
      App.dialogo("Vincular a evento existente", `
        <p class="pequeno tenue">El registro se añade como fuente adicional del evento (§13) y el nivel
          de corroboración se recalcula.</p>
        <label><span>Evento</span><select id="d-folio">${opciones || '<option value="">No hay eventos</option>'}</select></label>
        <label style="margin-top:.5rem"><span>Tipo de aporte</span><select id="d-tipo">
          <option value="CORROBORACION">Corroboración</option>
          <option value="ACTUALIZACION">Actualización</option>
        </select></label>
        <label style="margin-top:.5rem"><span>Motivo</span><textarea id="d-motivo"></textarea></label>`,
        [{ texto: "Vincular", clase: "boton--primario", accion: async () => {
            const folio = document.getElementById("d-folio").value;
            if (!folio) { App.avisar("No hay evento al que vincular.", true); return false; }
            await API.vincular(id, {
              folio, tipo_aporte: document.getElementById("d-tipo").value,
              motivo: document.getElementById("d-motivo").value.trim() || "Vinculado desde bandeja"
            });
            App.avisar("Fuente añadida al evento " + folio + ".");
            App.ir("#/bandeja", true);
          } }]);
      return;
    }

    // Validar: emite folio. Se pide confirmar entidad y categoría porque de
    // ellas depende el folio, que después es inmutable (§9).
    const cat = await App.catalogos();
    const opcEnt = cat.entidades.map((e) =>
      `<option value="${e.iso}"${e.iso === item.entidad_iso ? " selected" : ""}>${U.esc(e.nombre)}</option>`).join("");
    App.dialogo("Validar y emitir folio forense", `
      <div class="aviso aviso--seguridad">Al validar se emite el folio <b>AF-AÑO-ESTADO-CATEGORÍA-CONSECUTIVO</b>,
        que <b>no podrá modificarse nunca</b>. Confirme entidad y categoría antes de continuar.</div>
      <label><span>Entidad federativa</span><select id="d-entidad"><option value="">— sin determinar —</option>${opcEnt}</select></label>
      <label style="margin-top:.5rem"><span>Categoría</span><select id="d-categoria">
        ${["FOS", "CAM", "CSE"].map((c) =>
          `<option value="${c}"${c === item.categoria_detectada ? " selected" : ""}>${U.esc(U.CATEGORIAS[c].nombre)}</option>`).join("")}
      </select></label>
      <label style="margin-top:.5rem"><span>Municipio</span><input id="d-municipio" value="${U.esc(item.municipio || "")}"></label>
      <label style="margin-top:.5rem"><span>Localidad</span><input id="d-localidad" placeholder="opcional"></label>
      <label style="margin-top:.5rem"><span>Fecha probable del hecho</span>
        <input id="d-fecha" type="date" value="${U.esc((item.fecha_publicacion || "").slice(0, 10))}">
        <span class="pequeno tenue">La fecha de publicación no es la del hecho: corríjala si la nota lo precisa.</span></label>
      <label style="margin-top:.5rem"><span>Resumen factual</span>
        <textarea id="d-resumen">${U.esc(item.resumen || item.titulo || "")}</textarea>
        <span class="pequeno tenue">Sólo hechos publicados. Los datos que §20 reserva se marcan automáticamente.</span></label>
      <label style="margin-top:.5rem"><span>Motivo de la validación</span>
        <textarea id="d-motivo" placeholder="p. ej. Corroborado contra el boletín de la fiscalía."></textarea></label>`,
      [{ texto: "Validar y emitir folio", clase: "boton--primario", accion: async () => {
          const entidad = document.getElementById("d-entidad").value;
          if (!entidad) { App.avisar("Sin entidad no puede emitirse folio.", true); return false; }
          const r = await API.validar(id, {
            entidad_iso: entidad,
            categoria: document.getElementById("d-categoria").value,
            municipio: document.getElementById("d-municipio").value.trim() || null,
            localidad: document.getElementById("d-localidad").value.trim() || null,
            fecha_probable_evento: document.getElementById("d-fecha").value || null,
            resumen_factual: document.getElementById("d-resumen").value.trim() || null,
            motivo: document.getElementById("d-motivo").value.trim() || "Validado en bandeja"
          });
          App.avisar("Evento creado con folio " + r.folio + ".");
          App.ir("#/eventos/" + r.folio);
        } }]);
  }

  /* ====================================================== EVENTOS (§10) === */
  V.eventos = async function (contenedor, params) {
    const filtros = {
      categoria: params.get("categoria") || "", entidad: params.get("entidad") || "",
      nivel: params.get("nivel") || "", estado: params.get("estado") || "ACTIVO",
      q: params.get("q") || ""
    };
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Eventos</h1>
        <p class="vista__nota">Registro definitivo. Cada evento tiene folio inmutable, nivel de
          corroboración derivado de sus fuentes e historial completo de modificaciones.</p>
        <span class="fila">
          <a class="boton boton--chico" href="/api/export/events.csv">CSV</a>
          <a class="boton boton--chico" href="/api/export/events.json">JSON</a>
          <a class="boton boton--chico" href="/api/export/events.geojson">GeoJSON</a>
        </span>
      </div>
      <div id="eventos-filtros"></div>
      <div id="eventos-lista">${U.cargando()}</div>`;

    App.pintarFiltros("eventos-filtros", [
      { nombre: "categoria", etiqueta: "Categoría", tipo: "select", valor: filtros.categoria,
        opciones: [["", "Todas"], ["FOS", "Fosas"], ["CAM", "Campamentos"], ["CSE", "Casas de seguridad"]] },
      { nombre: "entidad", etiqueta: "Entidad", tipo: "entidad", valor: filtros.entidad },
      { nombre: "nivel", etiqueta: "Nivel", tipo: "select", valor: filtros.nivel,
        opciones: [["", "Todos"], ["A", "A — Confirmado"], ["B", "B — Altamente corroborado"],
                   ["C", "C — Reportado"], ["D", "D — Por verificar"]] },
      { nombre: "estado", etiqueta: "Estado", tipo: "select", valor: filtros.estado,
        opciones: [["ACTIVO", "Activo"], ["DESCARTADO", "Descartado"], ["DUPLICADO", "Duplicado"],
                   ["FUSIONADO", "Fusionado"], ["", "Todos"]] },
      { nombre: "q", etiqueta: "Buscar", tipo: "text", valor: filtros.q }
    ], "#/eventos");

    const datos = await API.eventos(filtros);
    const filas = datos.eventos.map((e) => [
      `<a href="#/eventos/${U.esc(e.folio)}">${U.folio(e.folio)}</a>`,
      U.distintivoCategoria(e.categoria),
      U.esc(e.entidad),
      U.esc(U.texto(e.municipio)),
      U.esc(U.fecha(e.fecha_probable_evento)),
      U.distintivoNivel(e.nivel_corroboracion),
      `<span class="mono">${U.esc(e.total_fuentes)}</span>`,
      `<span class="pequeno">${U.esc((e.resumen_factual || "").slice(0, 110))}</span>`
    ]);
    document.getElementById("eventos-lista").innerHTML =
      `<p class="pequeno tenue">${datos.total} evento(s).</p>` +
      U.tabla(["Folio", "Categoría", "Entidad", "Municipio", "Fecha del hecho", "Nivel", "Fuentes", "Resumen"],
        filas, { tituloVacio: "Sin eventos con esos filtros",
                 detalleVacio: "El registro definitivo se llena validando en la bandeja." });
  };

  V.evento = async function (contenedor, params, folio) {
    contenedor.innerHTML = U.cargando("Abriendo la ficha…");
    const f = await API.evento(folio);

    const fuentes = f.fuentes.map((s) => [
      `<span class="etiqueta">${U.esc(s.clase)}</span>`,
      `<span class="mono">N${U.esc(s.nivel)}</span>`,
      U.esc(U.texto(s.medio)),
      `<a href="${U.esc(s.url)}" target="_blank" rel="noopener noreferrer" class="recorte" style="display:inline-block;max-width:26ch">${U.esc(s.titulo || s.url)}</a>`,
      U.esc(U.fecha(s.fecha_publicacion)),
      U.esc(U.fecha(s.fecha_consulta, true)),
      `<span class="etiqueta">${U.esc(s.tipo_aporte)}</span>`
    ]);

    const historial = (f.historial || []).map((h) => `
      <li class="cronologia__hito${h.usuario === "sistema" ? " cronologia__hito--sistema" : ""}">
        <div class="cronologia__cabeza">
          <span class="marca-tiempo">${U.esc(U.fecha(h.ts, true))}</span>
          <b class="pequeno">${U.esc(h.proceso)}</b>
          <span class="pequeno tenue">por ${U.esc(h.usuario)}</span>
        </div>
        <div class="cronologia__cuerpo">
          ${h.campo ? `<b>${U.esc(h.campo)}</b>: ` : ""}
          ${h.valor_anterior ? `<s class="tenue">${U.esc(h.valor_anterior)}</s> → ` : ""}
          ${h.valor_nuevo ? U.esc(h.valor_nuevo) : ""}
          ${h.motivo ? `<div class="tenue">${U.esc(h.motivo)}</div>` : ""}
        </div>
      </li>`).join("");

    const atribuciones = (f.atribucion || []).length
      ? f.atribucion.map((a) => `<div class="aviso">
          ${U.esc(a.formato)}
          <div class="pequeno tenue">Fuente: <a href="${U.esc(a.url)}" target="_blank" rel="noopener noreferrer">${U.esc(a.url)}</a>
          · registrada por ${U.esc(a.registrada_por)} el ${U.esc(U.fecha(a.registrada_en, true))}</div>
        </div>`).join("")
      : `<p class="pequeno tenue">Sin atribuciones registradas. ARGOS FORENSE no infiere a qué organización
         pertenece un sitio: sólo recoge lo que una fuente identificable haya atribuido, ligado a esa fuente.</p>`;

    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>${U.folio(f.folio)}</h1>
        <p class="vista__nota">${U.esc(f.categoria_nombre)}${f.subcategoria ? " · " + U.esc(f.subcategoria) : ""}</p>
        <span class="fila">
          ${U.distintivoNivel(f.nivel_corroboracion)}
          <span class="etiqueta">${U.esc(f.estado)}</span>
          ${f.reserva_operativa ? '<span class="etiqueta etiqueta--alerta">RESERVA OPERATIVA §20</span>' : ""}
        </span>
      </div>

      ${!f.es_hecho_confirmado ? `<div class="aviso aviso--alerta">
        Este evento <b>no está confirmado</b>: ${U.esc(f.nivel_corroboracion_motivo)}
        No debe presentarse como hecho confirmado.</div>` : `<div class="aviso aviso--ok">
        <b>Confirmado.</b> ${U.esc(f.nivel_corroboracion_motivo)}</div>`}

      <section class="panel">
        <h2 class="panel__titulo">Ficha del evento</h2>
        <div class="campos">
          ${U.campo("Folio", U.folio(f.folio))}
          ${U.campo("Categoría", U.distintivoCategoria(f.categoria) + " " + U.esc(f.categoria_nombre))}
          ${U.campo("Subcategoría", U.esc(U.texto(f.subcategoria)))}
          ${U.campo("Fecha de detección", U.esc(U.fecha(f.fecha_deteccion)))}
          ${U.campo("Hora de detección", `<span class="mono">${U.esc(f.hora_deteccion)}</span>`)}
          ${U.campo("Fecha probable del hecho", U.esc(U.fecha(f.fecha_probable_evento)))}
          ${U.campo("Entidad", U.esc(f.entidad) + (f.region ? ` <span class="tenue pequeno">${U.esc(f.region)}</span>` : ""))}
          ${U.campo("Municipio", U.esc(U.texto(f.municipio)))}
          ${U.campo("Localidad", U.esc(U.texto(f.localidad)))}
          ${U.campo("Nivel de corroboración", U.distintivoNivel(f.nivel_corroboracion))}
          ${U.campo("Estado del registro", U.esc(f.estado))}
          ${U.campo("Corte en que apareció", f.corte_aparicion ? U.esc(f.corte_aparicion.etiqueta) : "—")}
          ${U.campo("Última actualización", U.esc(U.fecha(f.ultima_actualizacion, true)))}
          ${U.campo("Ubicación publicable", f.ubicacion.latitud === null ? "—" :
             `<span class="mono">${f.ubicacion.latitud}, ${f.ubicacion.longitud}</span>
              <span class="etiqueta">${U.esc(f.ubicacion.precision)}</span>`)}
          ${U.campo("Cuerpos", f.num_cuerpos === null ? "—" : `<span class="mono">${U.esc(f.num_cuerpos)}</span>`)}
          ${U.campo("Personas liberadas", f.personas_liberadas === null ? "—" : `<span class="mono">${U.esc(f.personas_liberadas)}</span>`)}
          ${U.campo("Personas detenidas", f.personas_detenidas === null ? "—" : `<span class="mono">${U.esc(f.personas_detenidas)}</span>`)}
          ${U.campo("Autoridad", U.esc(U.texto(f.autoridad)))}
        </div>
        <p style="margin-top:.7rem"><b class="pequeno tenue">RESUMEN FACTUAL</b><br>${U.esc(f.resumen_factual)}</p>
        <div class="ficha__acciones">
          <button class="boton" id="btn-editar">Corregir ficha</button>
          <button class="boton" id="btn-atribuir">Registrar atribución</button>
          <button class="boton boton--peligro" id="btn-fusionar">Fusionar con otro folio</button>
        </div>
      </section>

      <section class="panel">
        <h2 class="panel__titulo">Fuentes del evento · ${f.total_fuentes}</h2>
        ${U.tabla(["Clase", "Nivel", "Medio", "Publicación", "Fecha de publicación", "Fecha de consulta", "Aporte"],
          fuentes, { tituloVacio: "Sin fuentes ligadas" })}
      </section>

      <section class="panel">
        <h2 class="panel__titulo">Atribuciones (§21)</h2>
        ${atribuciones}
      </section>

      <section class="panel">
        <h2 class="panel__titulo">Historial de modificaciones (§14)</h2>
        ${historial ? `<ul class="cronologia">${historial}</ul>` : U.vacio("Sin movimientos registrados", "")}
      </section>`;

    document.getElementById("btn-editar").addEventListener("click", () => dialogoEdicion(f));
    document.getElementById("btn-atribuir").addEventListener("click", () => dialogoAtribucion(f));
    document.getElementById("btn-fusionar").addEventListener("click", () => dialogoFusion(f));
  };

  function dialogoEdicion(f) {
    App.dialogo("Corregir ficha", `
      <p class="pequeno tenue">El folio, la categoría y la fecha de creación no son editables:
        el folio es inmutable y la categoría forma parte de él.</p>
      <label><span>Municipio</span><input id="e-municipio" value="${U.esc(f.municipio || "")}"></label>
      <label style="margin-top:.5rem"><span>Localidad</span><input id="e-localidad" value="${U.esc(f.localidad || "")}"></label>
      <label style="margin-top:.5rem"><span>Subcategoría</span><input id="e-subcategoria" value="${U.esc(f.subcategoria || "")}"></label>
      <label style="margin-top:.5rem"><span>Fecha probable del hecho</span><input id="e-fecha" type="date" value="${U.esc(f.fecha_probable_evento || "")}"></label>
      <label style="margin-top:.5rem"><span>Cuerpos</span><input id="e-cuerpos" type="number" min="0" value="${f.num_cuerpos === null ? "" : U.esc(f.num_cuerpos)}"></label>
      <label style="margin-top:.5rem"><span>Personas liberadas</span><input id="e-liberadas" type="number" min="0" value="${f.personas_liberadas === null ? "" : U.esc(f.personas_liberadas)}"></label>
      <label style="margin-top:.5rem"><span>Personas detenidas</span><input id="e-detenidas" type="number" min="0" value="${f.personas_detenidas === null ? "" : U.esc(f.personas_detenidas)}"></label>
      <label style="margin-top:.5rem"><span>Autoridad participante</span><input id="e-autoridad" value="${U.esc(f.autoridad || "")}"></label>
      <label style="margin-top:.5rem"><span>Resumen factual</span><textarea id="e-resumen">${U.esc(f.resumen_factual)}</textarea></label>
      <label style="margin-top:.5rem"><span>Motivo de la corrección (obligatorio)</span><textarea id="e-motivo"></textarea></label>`,
      [{ texto: "Guardar", clase: "boton--primario", accion: async () => {
          const motivo = document.getElementById("e-motivo").value.trim();
          if (motivo.length < 3) { App.avisar("El motivo es obligatorio (§14).", true); return false; }
          const num = (id) => { const v = document.getElementById(id).value; return v === "" ? null : Number(v); };
          const cambios = {
            municipio: document.getElementById("e-municipio").value.trim() || null,
            localidad: document.getElementById("e-localidad").value.trim() || null,
            subcategoria: document.getElementById("e-subcategoria").value.trim() || null,
            fecha_probable_evento: document.getElementById("e-fecha").value || null,
            num_cuerpos: num("e-cuerpos"), personas_liberadas: num("e-liberadas"),
            personas_detenidas: num("e-detenidas"),
            autoridad: document.getElementById("e-autoridad").value.trim() || null,
            resumen_factual: document.getElementById("e-resumen").value.trim()
          };
          const r = await API.editarEvento(f.folio, { cambios, motivo });
          App.avisar(`${r.modificados} campo(s) corregido(s) y anotado(s) en la bitácora.`);
          App.ir("#/eventos/" + f.folio, true);
        } }]);
  }

  function dialogoAtribucion(f) {
    App.dialogo("Registrar atribución (§21)", `
      <div class="aviso aviso--seguridad">La plataforma <b>nunca</b> infiere a qué organización pertenece
        un sitio. Sólo se registra lo que una fuente identificable atribuyó, y siempre ligado a ella.</div>
      <label><span>Quién hizo la atribución</span>
        <input id="a-quien" placeholder="p. ej. La Fiscalía General del Estado de Jalisco"></label>
      <label style="margin-top:.5rem"><span>Qué atribuyó</span>
        <input id="a-texto" placeholder="p. ej. el sitio a un grupo delictivo con presencia en la región"></label>
      <label style="margin-top:.5rem"><span>Dónde consta (URL)</span>
        <input id="a-url" type="url" placeholder="https://…"></label>`,
      [{ texto: "Registrar", clase: "boton--primario", accion: async () => {
          try {
            await API.atribuir(f.folio, {
              atribuido_por: document.getElementById("a-quien").value.trim(),
              texto: document.getElementById("a-texto").value.trim(),
              url: document.getElementById("a-url").value.trim()
            });
          } catch (e) { App.avisar(e.message, true); return false; }
          App.avisar("Atribución registrada con su fuente.");
          App.ir("#/eventos/" + f.folio, true);
        } }]);
  }

  async function dialogoFusion(f) {
    const datos = await API.eventos({ categoria: f.categoria, entidad: f.entidad_iso, limite: 200 });
    const opciones = datos.eventos.filter((e) => e.folio !== f.folio)
      .map((e) => `<option value="${U.esc(e.folio)}">${U.esc(e.folio)} · ${U.esc((e.resumen_factual || "").slice(0, 60))}</option>`).join("");
    App.dialogo("Fusionar eventos", `
      <p class="pequeno tenue">Las fuentes de <b>${U.esc(f.folio)}</b> pasan al folio destino y este queda
        con estado FUSIONADO. Ningún folio se borra: los dos siguen consultables.</p>
      <label><span>Folio destino</span><select id="f-destino">${opciones || '<option value="">No hay otro evento comparable</option>'}</select></label>
      <label style="margin-top:.5rem"><span>Motivo (obligatorio)</span><textarea id="f-motivo"></textarea></label>`,
      [{ texto: "Fusionar", clase: "boton--peligro", accion: async () => {
          const destino = document.getElementById("f-destino").value;
          const motivo = document.getElementById("f-motivo").value.trim();
          if (!destino) { App.avisar("No hay folio destino.", true); return false; }
          if (motivo.length < 3) { App.avisar("El motivo es obligatorio.", true); return false; }
          const r = await API.fusionar(f.folio, { folio_destino: destino, motivo });
          App.avisar(`Fusionado en ${destino}: ${r.fuentes_migradas} fuente(s) migrada(s).`);
          App.ir("#/eventos/" + destino);
        } }]);
  }

  /* ====================================================== ESTADOS (§6) ==== */
  V.estados = async function (contenedor) {
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>Estados</h1>
        <p class="vista__nota">Las 32 entidades federativas, cruzadas con las tres categorías.
          Una entidad sin eventos no es una entidad sin hechos: es una entidad sin hallazgos validados.</p>
      </div>
      <div id="estados-lista">${U.cargando()}</div>`;
    const datos = await API.estados();
    const filas = datos.entidades.map((e) => [
      `<a href="#/estados/${U.esc(e.iso)}">${U.esc(e.entidad)}</a>`,
      U.esc(e.region),
      `<span class="mono">${e.fosas}</span>`,
      `<span class="mono">${e.campamentos}</span>`,
      `<span class="mono">${e.casas_de_seguridad}</span>`,
      `<span class="mono">${e.eventos_nuevos}</span>`,
      `<span class="mono">${e.actualizaciones}</span>`,
      e.nivel_corroboracion_max ? U.distintivoNivel(e.nivel_corroboracion_max) : '<span class="tenue">—</span>',
      `<span class="mono">${e.pendientes_en_bandeja}</span>`,
      `<span class="mono">${e.total}</span>`
    ]);
    document.getElementById("estados-lista").innerHTML = `<section class="panel">
      ${U.tabla(["Entidad", "Región", "Fosas", "Camp.", "Casas", "Nuevos", "Actualiz.", "Nivel máx.", "En bandeja", "Total"], filas)}
    </section>`;
  };

  V.estado = async function (contenedor, params, iso) {
    contenedor.innerHTML = U.cargando();
    const e = await API.estado(iso);
    const filas = e.eventos.map((v) => [
      `<a href="#/eventos/${U.esc(v.folio)}">${U.folio(v.folio)}</a>`,
      U.distintivoCategoria(v.categoria),
      U.esc(U.texto(v.municipio)),
      U.esc(U.fecha(v.fecha_probable_evento)),
      U.distintivoNivel(v.nivel_corroboracion),
      `<span class="mono">${U.esc(v.total_fuentes)}</span>`,
      `<span class="pequeno">${U.esc((v.resumen_factual || "").slice(0, 100))}</span>`
    ]);
    contenedor.innerHTML = `
      <div class="vista__titulo">
        <h1>${U.esc(e.entidad)}</h1>
        <p class="vista__nota">Región ${U.esc(e.region)} · <a href="#/mapa">volver al mapa</a></p>
      </div>
      <div class="rejilla" style="margin-bottom:.8rem">
        ${U.indicador(e.fosas, "Fosas clandestinas", { clase: "fos" })}
        ${U.indicador(e.campamentos, "Campamentos", { clase: "cam" })}
        ${U.indicador(e.casas_de_seguridad, "Casas de seguridad", { clase: "cse" })}
        ${U.indicador(e.eventos_nuevos, "Eventos nuevos")}
        ${U.indicador(e.actualizaciones, "Actualizaciones")}
      </div>
      <section class="panel">
        <h2 class="panel__titulo">Nivel de corroboración</h2>
        <div class="fila">${["A", "B", "C", "D"].map((n) =>
          `<span class="fila" style="gap:.3rem">${U.distintivoNivel(n)}<b class="mono">${e.por_nivel[n] || 0}</b></span>`).join("")}</div>
        <p class="pequeno tenue" style="margin:.6rem 0 0">
          Pendientes en bandeja para esta entidad: <b class="mono">${e.pendientes_en_bandeja}</b>.
        </p>
      </section>
      <section class="panel">
        <h2 class="panel__titulo">Eventos registrados</h2>
        ${U.tabla(["Folio", "Categoría", "Municipio", "Fecha del hecho", "Nivel", "Fuentes", "Resumen"], filas,
          { tituloVacio: "Sin eventos validados en la entidad", detalleVacio: "" })}
      </section>`;
  };

  global.VistasOperacion = V;
})(window);
