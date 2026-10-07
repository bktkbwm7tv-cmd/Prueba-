const vm=require('node:vm'), fs=require('fs');
const f=process.argv[2]; const html=fs.readFileSync(f,'utf8');
let err=[], warn=[];
const m=html.match(/<script>([\s\S]*?)<\/script>/);
if(!m) err.push('sin <script>');
const ctx=vm.createContext({document:{getElementById:()=>null,querySelectorAll:()=>[],addEventListener:()=>{},readyState:"complete"},window:{addEventListener:()=>{}},setInterval:()=>{},setTimeout:()=>{},requestAnimationFrame:()=>{},addEventListener:()=>{}});
let R;
try{ R=vm.runInContext(m[1]+'\n;({EVENTOS,EVENTOS_ARM,MEXICO_PATHS,STATE_REGION,CORTE_FECHA})',ctx); }
catch(e){ err.push('script no evalúa: '+e.message); }
if(R){
  const {EVENTOS:E,EVENTOS_ARM:A,MEXICO_PATHS:P,STATE_REGION:SR,CORTE_FECHA:CF}=R;
  if(Object.keys(P).length!==32) err.push('MEXICO_PATHS='+Object.keys(P).length+', esperado 32');
  const all=[...E,...A];
  for(const e of all){
    if(!P[e.estado]) err.push(e.id+': estado inexistente '+e.estado);
    if(SR[e.estado]!==e.region) err.push(e.id+': region '+e.region+' != STATE_REGION '+SR[e.estado]);
  }

  // NUEVO: ningun color sin definicion en SEVERITY_COLOR/LABEL (fill="undefined")
  const sc=html.match(/const SEVERITY_COLOR = \{([^}]*)\}/)[1];
  const sl=html.match(/const SEVERITY_LABEL = \{([^}]*)\}/)[1];
  for(const e of all){
    if(!new RegExp('\\b'+e.color+'\\s*:').test(sc)) err.push(e.id+': color "'+e.color+'" sin SEVERITY_COLOR -> fill=undefined');
    if(!new RegExp('\\b'+e.color+'\\s*:').test(sl)) err.push(e.id+': color "'+e.color+'" sin SEVERITY_LABEL');
  }
  // NUEVO: las recuperaciones no pueden alimentar mapa ni radar del corte
  if(!/argosRenderMap\("argos-map", EVENTOS_CORTE\)/.test(html)) err.push('el mapa del corte no usa EVENTOS_CORTE');
  if(!/argosRenderRadar\("argos-radar", "argos-radar-stats", EVENTOS_CORTE/.test(html)) err.push('el radar no usa EVENTOS_CORTE');
  const ids=all.map(e=>e.id); const dup=ids.filter((x,i)=>ids.indexOf(x)!==i);
  if(dup.length) err.push('ARG-ID duplicados: '+dup);
  // anclas
  for(const id of ids) if(!html.includes('id="'+id+'"')) err.push(id+': sin ancla id=');
  // enlaces
  const links=[...html.matchAll(/href="#(ARG-[^"]+)"/g)].map(x=>x[1]);
  for(const l of new Set(links)) if(!html.includes('id="'+l+'"')) err.push('enlace roto #'+l);
  // ventana
  const OPEN=process.argv[3], CLOSE=process.argv[4];
  if(!OPEN||!CLOSE){ console.log('USO: node validar.js <archivo> <AAAA-MM-DD apertura> <AAAA-MM-DD cierre>'); process.exit(2); }
  for(const e of E){ if(e.color!=='rec' && e.fecha>CLOSE) err.push(e.id+': fecha '+e.fecha+' fuera de ventana'); }
  // NUEVO (ARGOS 125): un hecho propio tampoco puede ser anterior a la apertura, y una recuperación no puede caer dentro de la ventana
  for(const e of E){ if(e.color!=='rec' && e.fecha<OPEN) err.push(e.id+': fecha '+e.fecha+' anterior a la apertura '+OPEN+' — es -REC-'); if(e.color==='rec' && e.fecha>OPEN) err.push(e.id+': recuperación con fecha '+e.fecha+' posterior a la apertura'); }
  // semaforo
  const c={rojo:0,amarillo:0,verde:0,rec:0}; E.forEach(e=>c[e.color]++);
  const port=html.match(/🔴 ROJO — ALTO IMPACTO<\/span><div class="val">(\d+)/);
  const porta=html.match(/🟡 AMARILLO — VIOLENCIA OPERATIVA<\/span><div class="val">(\d+)/);
  const portv=html.match(/🟢 VERDE — ACCIONES INSTITUCIONALES<\/span><div class="val">(\d+)/);
  if(+port[1]!==c.rojo) err.push('portada rojo '+port[1]+' != '+c.rojo);
  if(+porta[1]!==c.amarillo) err.push('portada amarillo '+porta[1]+' != '+c.amarillo);
  if(+portv[1]!==c.verde) err.push('portada verde '+portv[1]+' != '+c.verde);
  const rs=html.match(/radar-stats[^>]*><div>🔴[^<]*<br><b>(\d+)<\/b><\/div><div>🟡[^<]*<br><b>(\d+)<\/b><\/div><div>🟢[^<]*<br><b>(\d+)<\/b>/);
  if(!rs) err.push('radar-stats no parseable');
  else { if(+rs[1]!==c.rojo||+rs[2]!==c.amarillo||+rs[3]!==c.verde) err.push('radar-stats '+rs.slice(1,4)+' != '+[c.rojo,c.amarillo,c.verde]); }
  if(CF!==CLOSE) err.push('CORTE_FECHA='+CF);
  console.log('semaforo', JSON.stringify(c), '| eventos', E.length, '| arm', A.length);
}
// forma
const bodies=(html.match(/<body/g)||[]).length; if(bodies!==1) err.push('bodies='+bodies);
const tables=(html.match(/<table/g)||[]).length;
const wraps=(html.match(/<div class="table-wrap">/g)||[]).length;
if(tables!==wraps) err.push('tablas '+tables+' != table-wrap '+wraps);
const hechos=(html.match(/<span class="k">HECHO<\/span>/g)||[]).length;
const traz=(html.match(/<span class="k">TRAZABILIDAD<\/span>/g)||[]).length;
if(hechos!==traz) err.push('HECHO '+hechos+' != TRAZABILIDAD '+traz);
const notas=(html.match(/<div class="nota"/g)||[]).length;
if(notas!==hechos) err.push('notas '+notas+' != apartados HECHO '+hechos);
if(/class="k">(CORROBORACI|EXPLOTACI)/.test(html)) err.push('existe Corroboracion o Explotacion ARGOS');
const rec=(html.match(/<div class="alerta contexto">/g)||[]).length;
if(rec>3) err.push('recuadros='+rec+' (max 3)');
const sem=(html.match(/sem-item/g)||[]).length;
const fe=(html.match(/ARG-\d+-FE-/g)||[]).length; if(fe) err.push('hay '+fe+' referencias -FE- en el cartelon');
const pages=(html.match(/<section class="page">/g)||[]).length;
const foots=(html.match(/<footer class="footbar">/g)||[]).length;
if(pages!==foots) err.push('paginas '+pages+' != pies '+foots);
console.log('paginas',pages,'| fichas',notas,'| tablas',tables,'| recuadros',rec,'| sem-item',sem);
if(err.length){ console.log('\nFALLOS:'); err.forEach(e=>console.log(' ✗ '+e)); process.exit(1); }
console.log('\nvalidación OK');
