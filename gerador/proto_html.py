# -*- coding: utf-8 -*-
"""Gera prototipo.html: protótipo clicável, navegável no navegador/Live Server."""
import json

from dados import TELAS as INV, MODULOS

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#0E2C4B;--gold:#B8862B;--line:#DBE3EC;--muted:#64778A}
body{background:#0A1826;color:#14232F;font:14px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif}
header{position:sticky;top:0;z-index:30;background:var(--navy);color:#fff;
       border-bottom:3px solid var(--gold);display:flex;align-items:center;gap:14px;
       padding:10px 18px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;margin-right:6px}
.mark{width:32px;height:32px;border-radius:7px;background:#1E4D75;display:grid;place-items:center;
      color:var(--gold);font-weight:700;font-size:13px}
.brand b{font-size:14px;display:block;line-height:1.25}
.brand span{font-size:11px;color:#8FA6BA}
select,button{font:inherit}
select{background:#173F62;color:#fff;border:1px solid #2A4A6B;border-radius:7px;
       padding:8px 10px;max-width:340px}
button{background:#173F62;color:#fff;border:1px solid #2A4A6B;border-radius:7px;
       padding:8px 12px;cursor:pointer}
button:hover{background:#1E4D75}
button.on{background:var(--gold);border-color:var(--gold);color:#231a06;font-weight:700}
.spacer{flex:1}
.now{font-size:12px;color:#B7C7D6;text-align:right;line-height:1.35}
.now b{color:#fff;font-size:13px;display:block}
.tag{font-size:10.5px;letter-spacing:.6px;color:var(--gold);font-weight:700}
main{padding:22px 18px 60px;display:grid;place-items:start center}
.stage{position:relative;width:100%;max-width:1440px;background:#fff;
       box-shadow:0 18px 50px rgba(0,0,0,.45);border-radius:4px;overflow:hidden}
.stage.wide{max-width:2000px}
.stage img{display:block;width:100%;height:auto}
.hot{position:absolute;z-index:10;display:block;border-radius:5px;text-decoration:none}
.hot:hover{background:rgba(184,134,43,.30);outline:2px solid var(--gold)}
body.show .hot{background:rgba(18,99,165,.20);outline:1.5px dashed #1263A5}
body.flash .hot{background:rgba(184,134,43,.45);outline:2px solid var(--gold)}
.hot i{position:absolute;left:0;top:-22px;background:var(--navy);color:#fff;font-style:normal;
       font-size:11px;padding:2px 7px;border-radius:4px;white-space:nowrap;display:none}
.hot:hover i{display:block}
.hint{color:#8FA6BA;font-size:12px;text-align:center;max-width:1440px;margin:14px auto 0}
.hint kbd{background:#173F62;border:1px solid #2A4A6B;border-radius:4px;padding:1px 6px;
          font:inherit;font-size:11px;color:#fff}
.dead{position:fixed;inset:0;z-index:5}
@media(max-width:700px){.now{display:none}}
"""

JS = """
const T = DATA.telas, H = DATA.hots;
const idx = {}; T.forEach((t,i)=>idx[t.n]=i);
let cur = 0;
const img = document.getElementById('img'), lay = document.getElementById('lay');
const sel = document.getElementById('sel'), now = document.getElementById('now');
const stage = document.getElementById('stage');

function show(n, push){
  if(!(n in idx)) return;
  cur = idx[n];
  const t = T[cur];
  img.src = 'figma-telas/' + t.f + '.svg';
  img.width = t.w; img.height = t.h;
  stage.classList.toggle('wide', t.w > 1440);
  now.innerHTML = '<span class="tag">' + t.mod + '</span><b>' + t.n + ' · ' + t.t + '</b>' +
                  (t.rf ? t.rf : '');
  sel.value = n;
  lay.innerHTML = '';
  (H[t.f] || []).forEach(h => {
    const [x, y, w, hh, to, label] = h;
    const a = document.createElement('a');
    a.className = 'hot';
    a.href = '#' + to;
    a.style.cssText = 'left:' + (x/t.w*100) + '%;top:' + (y/t.h*100) + '%;width:' +
                      (w/t.w*100) + '%;height:' + (hh/t.h*100) + '%';
    const d = T[idx[to]];
    a.innerHTML = '<i>' + (label ? label + ' → ' : '→ ') + (d ? d.t : to) + '</i>';
    a.onclick = e => { e.preventDefault(); go(to); };
    lay.appendChild(a);
  });
  if(push !== false) history.replaceState(null, '', '#' + n);
  window.scrollTo({top:0, behavior:'instant'});
}
function go(n){ show(n); }
function step(d){ show(T[Math.min(T.length-1, Math.max(0, cur+d))].n); }
function flash(){ document.body.classList.add('flash');
  setTimeout(()=>document.body.classList.remove('flash'), 550); }

sel.onchange = e => show(e.target.value);
document.getElementById('prev').onclick = ()=>step(-1);
document.getElementById('next').onclick = ()=>step(1);
document.getElementById('tog').onclick = e => {
  document.body.classList.toggle('show');
  e.target.classList.toggle('on', document.body.classList.contains('show'));
};
document.getElementById('dead').onclick = flash;
addEventListener('keydown', e => {
  if(e.target.tagName === 'SELECT') return;
  if(e.key === 'ArrowRight') step(1);
  if(e.key === 'ArrowLeft') step(-1);
  if(e.key.toLowerCase() === 'h') document.getElementById('tog').click();
});
addEventListener('hashchange', ()=>show(location.hash.slice(1) || '01', false));
show(location.hash.slice(1) || '01');
"""


def build(dims, hots):
    mod_nome = {m[0]: m[1] for m in MODULOS}
    telas = []
    for num, arq, titulo, mod, rf in INV:
        w, h = dims.get(arq, (1440, 1000))[:2]
        telas.append(dict(n=num, f=arq, t=titulo, mod=mod_nome[mod], rf=rf, w=w, h=h))
    opts = []
    atual = None
    for t in telas:
        if t["mod"] != atual:
            if atual:
                opts.append("</optgroup>")
            atual = t["mod"]
            opts.append('<optgroup label="%s">' % atual)
        opts.append('<option value="%s">%s · %s</option>' % (t["n"], t["n"], t["t"]))
    opts.append("</optgroup>")
    total = sum(len(v) for v in hots.values())
    data = json.dumps({"telas": telas, "hots": hots}, ensure_ascii=False)
    return """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Protótipo navegável · Escola do Legislativo</title>
<style>%s</style></head><body>
<header>
  <div class="brand"><div class="mark">EL</div>
    <div><b>Escola do Legislativo</b><span>Câmara Municipal do Recife · protótipo</span></div></div>
  <button id="prev" title="Tela anterior">&#8592;</button>
  <select id="sel">%s</select>
  <button id="next" title="Próxima tela">&#8594;</button>
  <button id="tog" title="Mostrar áreas clicáveis (H)">Áreas clicáveis</button>
  <div class="spacer"></div>
  <div class="now" id="now"></div>
</header>
<main>
  <div class="stage" id="stage">
    <div class="dead" id="dead"></div>
    <img id="img" alt="tela do protótipo">
    <div id="lay"></div>
  </div>
  <p class="hint">%d áreas clicáveis em 57 telas · <kbd>&#8592;</kbd> <kbd>&#8594;</kbd> troca de tela ·
     <kbd>H</kbd> destaca o que é clicável · clique numa área vazia para piscar os pontos de clique</p>
</main>
<script>const DATA = %s;</script>
<script>%s</script>
</body></html>
""" % (CSS, "".join(opts), total, data, JS)
