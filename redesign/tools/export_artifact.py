#!/usr/bin/env python3
"""site/ 의 여러 쪽을 한 파일로 묶는다 (게시용). 출력: build/artifact/mezard-parisi.html

쪽 사이 이동은 #이름 으로 한다. 증명 지도(map.html, map-*.html)는 render_maps.py 가 미리 그린 SVG
(build/artifact/maps/<이름>.svg)를 <pre class="mermaid" data-map="이름"> 자리에 넣는다. 그림이 없으면 그 자리에 안내만 남는다.
용어 링크(glossary.html#g-slug)는 href="#glossary" + data-term="g-slug" 로 바꾸고, 라우터가 용어집 쪽을 연 뒤
그 항목으로 스크롤하고 잠깐 강조한다.

사용: python3 tools/export_artifact.py [--root DIR] [--site DIR] [--out DIR] [--maps DIR]
  --root  site/ 를 읽고 build/artifact/ 에 쓸 디렉터리 (기본: redesign/, 환경변수 M2P_ROOT 도 된다).
          maps/ 가 거기 없으면 실제 build/artifact/maps/ 를 쓴다.
  --site  site/ 대신 읽을 디렉터리, --out  build/artifact/ 대신 쓸 디렉터리, --maps  지도 SVG 디렉터리 (기본: <out>/maps)
"""
import os, re, sys, posixpath, argparse, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
REAL_ROOT = os.path.dirname(HERE)
_ap = argparse.ArgumentParser()
_ap.add_argument("--root", default=None)
_ap.add_argument("--site", default=None)
_ap.add_argument("--out", default=None)
_ap.add_argument("--maps", default=None)
_args = _ap.parse_args()
ROOT = os.path.abspath(_args.root or os.environ.get("M2P_ROOT") or REAL_ROOT)
SITE = os.path.abspath(_args.site) if _args.site else os.path.join(ROOT, "site")
OUT = os.path.abspath(_args.out) if _args.out else os.path.join(ROOT, "build", "artifact")
MAPS = os.path.abspath(_args.maps) if _args.maps else os.path.join(OUT, "maps")
spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)

def slug(rel):
    s = rel[:-5] if rel.endswith(".html") else rel
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return {"index": "home", "cards-index": "cards"}.get(s, s)

pages = []
for d, _, fs in os.walk(SITE):
    for f in sorted(fs):
        if f.endswith(".html"):
            pages.append(posixpath.relpath(os.path.join(d, f), SITE))
order = ["index.html", "L0.html", "L1.html", "rules.html", "glossary.html", "map.html", "cards/index.html", "check-report.html"]
pages = [p for p in order if p in pages] + sorted(p for p in pages if p not in order)
slugs = {}
for p in pages:
    s0 = slug(p); s1 = s0; k = 2
    while s1 in slugs.values():          # 대소문자만 다른 id (tree:Q-rule / tree:q-rule 등)가 겹치지 않게
        s1 = f"{s0}-{k}"; k += 1
    slugs[p] = s1
assert len(set(slugs.values())) == len(slugs)

def rewrite(html, rel):
    base = posixpath.dirname(rel)
    def sub(m):
        attr, url = m.group(1), m.group(2)
        if rel == "glossary.html" and url.startswith("#g-"):      # 용어집 안의 색인 링크
            return f'{attr}="#glossary" data-term="{url[1:]}"'
        if re.match(r"^(https?:|#|mailto:)", url):
            return m.group(0)
        path, _, frag = url.partition("#")
        tgt = posixpath.normpath(posixpath.join(base, path))
        if tgt == "glossary.html" and frag.startswith("g-"):      # 쪽 + 앵커는 해시에 못 담는다
            return f'{attr}="#glossary" data-term="{frag}"'
        if tgt in slugs:
            return f'{attr}="#{slugs[tgt]}"'
        return m.group(0)
    return re.sub(r'((?:xlink:)?href)="([^"]*)"', sub, html)

sections = []
missing = []
for rel in pages:
    t = open(os.path.join(SITE, rel), encoding="utf-8").read()
    body = t[t.index("<body>") + 6: t.rindex("</body>")]
    body = re.sub(r"<script[\s\S]*?</script>", "", body)
    body = re.sub(r'<nav class="top">[\s\S]*?</nav>', "", body, count=1)
    body = re.sub(r'^\s*<div class="wrap">', "", body); body = re.sub(r"</div>\s*$", "", body)
    if rel == "map.html" or rel.startswith("map-"):
        def draw(m):
            name = m.group(1)
            svgp = os.path.join(MAPS, name + ".svg")
            if not os.path.exists(svgp):
                svgp = os.path.join(REAL_ROOT, "build", "artifact", "maps", name + ".svg")
            if not os.path.exists(svgp):
                missing.append(name)
                return '<p class="muted">(지도 그림 없음: render_maps.py 를 먼저 돌린다)</p>'
            svg = open(svgp, encoding="utf-8").read()
            svg = re.sub(r'click-href="([^"]*)"', r'href="\1"', svg)
            vb = re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ([\d.]+)"', svg)
            w = max(700, min(int(float(vb.group(1))), 2600)) if vb else 1100   # 큰 그림은 상자 안에서 가로로 민다
            svg = re.sub(r'(<svg\b[^>]*?) style="[^"]*"', r'\1', svg, count=1)
            svg = svg.replace("<svg ", f'<svg style="min-width:{w}px;max-width:none" ', 1)
            return '<div class="mapbox">' + svg + "</div>"
        body = re.sub(r'<pre class="mermaid" data-map="([^"]+)">[\s\S]*?</pre>', draw, body)
    body = rewrite(body, rel)
    sections.append(f'<section class="page" id="{slugs[rel]}" hidden>\n{body}\n</section>')

css = B.CSS
css = re.sub(r"@media \(prefers-color-scheme:dark\)\{:root\{([^}]*)\}\}",
             lambda m: "@media (prefers-color-scheme:dark){:root:not([data-theme=\"light\"]){" + m.group(1) + ";color-scheme:dark}}\n"
                       ":root[data-theme=\"dark\"]{" + m.group(1) + ";color-scheme:dark}", css)
css = css.replace(":root{--bg:#fbfbf9;", ":root{--mapbg:#ffffff;--bg:#fbfbf9;")
css = css.replace(".wrap{max-width:52rem;margin:0 auto;padding:1rem 1rem 4rem}",
                  ".wrap{max-width:52rem;margin:0 auto;padding-block:1rem 4rem;"
                  "padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}")
css += """
.mapbox{overflow-x:auto;background:var(--mapbg);border:1px solid var(--line);border-radius:8px;padding:.5rem;margin:1rem 0}
.mapbox svg{display:block;height:auto}
.wrap>*{min-width:0}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
h1,h2,h3{text-wrap:balance}
mjx-container.wide{display:block;max-width:100%;overflow-x:auto;overflow-y:hidden;padding:.2rem 0}
"""
nav = ('<nav class="top">' + "".join(f'<a href="#{s}" data-nav="{s}">{n}</a>' for s, n in
       [("home", "처음"), ("l0", "L0"), ("l1", "L1"), ("rules", "규칙 표"), ("glossary", "용어집"),
        ("map", "증명 지도"), ("cards", "카드 목록"), ("check-report", "검사 보고서")]) + "</nav>")
js = r"""
(function(){
  var pages=document.querySelectorAll('section.page'),byId={},done={},pendingTerm=null,hlTimer=null;
  pages.forEach(function(p){byId[p.id]=p;});
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  function focusTerm(t,smooth){
    var e=t&&document.getElementById(t);
    if(!e||!e.closest('#glossary'))return;
    e.scrollIntoView({block:'start',behavior:(smooth&&!reduce)?'smooth':'auto'});
    document.querySelectorAll('.gent.hl').forEach(function(x){x.classList.remove('hl');});
    e.classList.add('hl');clearTimeout(hlTimer);
    hlTimer=setTimeout(function(){e.classList.remove('hl');},2000);
  }
  function show(){
    var id=(location.hash||'#home').slice(1),el=byId[id];
    if(!el){id='home';el=byId[id];}
    pages.forEach(function(p){p.hidden=(p!==el);});
    document.querySelectorAll('nav.top a').forEach(function(a){
      var n=a.getAttribute('data-nav');a.classList.toggle('cur',n===id||(n==='cards'&&id.indexOf('cards-')===0)||(n==='map'&&id.indexOf('map-')===0));});
    window.scrollTo(0,0);
    var t=(id==='glossary')?pendingTerm:null;pendingTerm=null;
    if(t)focusTerm(t,false);
    if(!done[id]&&window.MathJax&&MathJax.typesetPromise){done[id]=1;MathJax.typesetPromise([el]).then(function(){fit(el);if(t)focusTerm(t,false);}).catch(function(){});}
  }
  function fit(el){var R=el.getBoundingClientRect().right;el.querySelectorAll('mjx-container:not([display])').forEach(function(m){
    if(m.getBoundingClientRect().right>R+1){m.classList.add('wide');}});}
  document.addEventListener('click',function(ev){
    var a=ev.target.closest&&ev.target.closest('a[data-term]');
    if(!a||ev.defaultPrevented||ev.button||ev.metaKey||ev.ctrlKey||ev.shiftKey||ev.altKey)return;
    ev.preventDefault();
    var t=a.getAttribute('data-term');
    if(location.hash==='#glossary'){focusTerm(t,true);}
    else{pendingTerm=t;location.hash='#glossary';}
  });
  window.addEventListener('hashchange',show);
  if(window.MathJax&&MathJax.startup&&MathJax.startup.promise){MathJax.startup.promise.then(show);}else{show();}
  show();
})();
"""
cfg = B.MATHJAX_CFG.replace("window.MathJax={", "window.MathJax={startup:{typeset:false},", 1)
out = ("<title>Mézard–Parisi 재구성</title>\n"
       '<meta name="claude:viewport-fit-sides" content="cover">\n'
       f"<style>{css}</style>\n<script>{cfg}</script>\n"
       '<script src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"></script>\n'
       f'<div class="wrap">\n{nav}\n' + "\n".join(sections) + f"\n</div>\n<script>{js}</script>\n")
os.makedirs(OUT, exist_ok=True)
p = os.path.join(OUT, "mezard-parisi.html")
open(p, "w", encoding="utf-8").write(out)
left = re.findall(r'href="(?!#|https?:)[^"]*"', out)
nb = len(out.encode("utf-8"))
print(f"{len(pages)}쪽 → {p} ({nb//1024} KB = {nb/2**20:.2f} MB, 게시 한도 16 MB), 안 바뀐 내부 링크 {len(left)}개", left[:5])
if missing:
    print("그림 없는 지도:", ", ".join(sorted(set(missing))))
if nb > 16 * 2**20:
    sys.exit("게시 한도 16 MB 를 넘는다")
