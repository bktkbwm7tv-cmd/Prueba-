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

// Renderiza con EXACTAMENTE el mismo arreglo que el escritorio, y con la misma fecha
// de corte. Si el cartelón define EVENTOS_CORTE —el arreglo ya filtrado de
// recuperaciones—, se usa ese; si no, se filtra aquí por color !== "rec".
//
// ⚠️ Defecto corregido en ARGOS 124, detectado por editor-duplicidad: este generador
// pasaba EVENTOS (el arreglo completo) mientras el escritorio pasaba EVENTOS_CORTE.
// Resultado: las recuperaciones se pintaban en el mapa y aparecían como ecos clicables
// en el radar de la versión móvil, rompiendo la paridad con el escritorio y
// contradiciendo la propia trazabilidad de sus fichas, que declara "FUERA DEL MAPA Y
// DEL RADAR". Un generador que no deriva del cartelón, diverge de él.
vm.runInContext(
  'var __corte = (typeof EVENTOS_CORTE !== "undefined")' +
  '  ? EVENTOS_CORTE' +
  '  : EVENTOS.filter(function(e){ return e.color !== "rec"; });' +
  'argosRenderMap("argos-map", __corte);' +
  'argosRenderRadar("argos-radar", "argos-radar-stats", __corte, CORTE_FECHA);' +
  // El módulo de armamento usa su propio arreglo cuando existe: solo eventos con
  // aseguramiento contabilizado. Si la edición no lo define, cae a EVENTOS.
  // Las filas marcadas "rec" no integran a los totales del corte y tampoco se pintan.
  'var __arm = (typeof EVENTOS_ARM !== "undefined" ? EVENTOS_ARM : EVENTOS)' +
  '  .filter(function(e){ return e.color !== "rec"; });' +
  'argosRenderMap("argos-map-arm", __arm);',
  sandbox
);

const outDir = path.dirname(process.argv[3] || "/tmp/argos-out/x");
fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, "out-map.svg"), store["argos-map"].innerHTML);
fs.writeFileSync(path.join(outDir, "out-radar.svg"), store["argos-radar"].innerHTML);
fs.writeFileSync(path.join(outDir, "out-stats.html"), store["argos-radar-stats"].innerHTML);
fs.writeFileSync(path.join(outDir, "out-map-arm.svg"), store["argos-map-arm"].innerHTML);

console.log("map bytes  :", store["argos-map"].innerHTML.length);
console.log("map-arm    :", store["argos-map-arm"].innerHTML.length);
console.log("radar bytes:", store["argos-radar"].innerHTML.length);
console.log("stats      :", store["argos-radar-stats"].innerHTML);
