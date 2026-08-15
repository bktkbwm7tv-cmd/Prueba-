#!/usr/bin/env node
/*
 * Extrae argosRenderMap/argosRenderRadar y sus constantes del HTML de escritorio
 * de un reporte ARGOS y las ejecuta contra un DOM simulado, para obtener el SVG
 * ya renderizado que se incrusta en la versión móvil (-movil.html).
 *
 * Uso: node gen-movil-svg.js <argos-YYYY-MM-DD.html>
 * Salida: escribe /tmp .../out-map.svg, out-radar.svg, out-stats.html
 */
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const src = process.argv[2];
if (!src) { console.error("Uso: node gen-movil-svg.js <archivo.html>"); process.exit(1); }
const html = fs.readFileSync(src, "utf8");

// El bloque <script> final contiene MEXICO_VIEWBOX ... argosRenderRadar.
const start = html.lastIndexOf("<script>");
const end = html.lastIndexOf("</script>");
if (start < 0 || end < 0) { console.error("No se encontró el bloque <script>"); process.exit(1); }
let code = html.slice(start + "<script>".length, end);

// Quitar el listener DOMContentLoaded: lo invocamos nosotros manualmente.
code = code.replace(/document\.addEventListener\("DOMContentLoaded"[\s\S]*$/, "");

// ---- DOM mínimo ----
const store = {};
function mkEl(id) {
  return {
    id,
    innerHTML: "",
    style: {},
    classList: { add() {}, remove() {} },
    dataset: {},
    addEventListener() {},
    querySelectorAll() { return { forEach() {} }; },
  };
}
const document = {
  getElementById(id) { return (store[id] = store[id] || mkEl(id)); },
  addEventListener() {},
};

const sandbox = { document, console, Math, Date, Object, Array, String, Number, JSON };
vm.createContext(sandbox);
vm.runInContext(code, sandbox);

// Renderiza con el mismo arreglo EVENTOS y la misma fecha de corte del escritorio.
vm.runInContext(
  'argosRenderMap("argos-map", EVENTOS);' +
  'argosRenderRadar("argos-radar", "argos-radar-stats", EVENTOS, CORTE_FECHA);',
  sandbox
);

const outDir = path.dirname(process.argv[3] || "/tmp/argos-out/x");
fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, "out-map.svg"), store["argos-map"].innerHTML);
fs.writeFileSync(path.join(outDir, "out-radar.svg"), store["argos-radar"].innerHTML);
fs.writeFileSync(path.join(outDir, "out-stats.html"), store["argos-radar-stats"].innerHTML);

console.log("map bytes  :", store["argos-map"].innerHTML.length);
console.log("radar bytes:", store["argos-radar"].innerHTML.length);
console.log("stats      :", store["argos-radar-stats"].innerHTML);
