#!/usr/bin/env python3
"""site/ 의 여러 쪽을 한 파일로 묶는다 (게시용). 출력: build/artifact/mezard-parisi.html

쪽 사이 이동은 #이름 으로 한다. 증명 지도는 미리 그린 SVG(build/artifact/map.svg)가 있으면 그것을 쓴다.
"""
import os, re, sys, posixpath, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = os.path.join(ROOT, "site")
OUT = os.path.join(ROOT, "build", "artifact")
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
order = ["index.html", "L0.html", "L1.html", "rules.html", "map.html", "cards/index.html", "check-report.html"]
pages = [p for p in order if p in pages] + sorted(p for p in pages if p not in order)
slugs = {p: slug(p) for p in pages}

def rewrite(html, rel):
    base = posixpath.dirname(rel)
    def sub(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|#|mailto:)", url):
            return m.group(0)
        path = url.split("#")[0]
        tgt = posixpath.normpath(posixpath.join(base, path))
        if tgt in slugs:
            return f'{attr}="#{slugs[tgt]}"'
        return m.group(0)
    return re.sub(r'((?:xlink:)?href)="([^"]*)"', sub, html)

sections = []
for rel in pages:
    t = open(os.path.join(SITE, rel), encoding="utf-8").read()
    body = t[t.index("<body>") + 6: t.rindex("</body>")]
    body = re.sub(r"<script[\s\S]*?</script>", "", body)
    body = re.sub(r'<nav class="top">[\s\S]*?</nav>', "", body, count=1)
    body = re.sub(r'^\s*<div class="wrap">', "", body); body = re.sub(r"</div>\s*$", "", body)
    if rel == "map.html":
        svgp = os.path.join(OUT, "map.svg")
        if os.path.exists(svgp):
            svg = open(svgp, encoding="utf-8").read()
            svg = re.sub(r'click-href="([^"]*)"', r'href="\1"', svg)
            body = re.sub(r'<pre class="mermaid">[\s\S]*?</pre>', '<div class="mapbox">' + svg + "</div>", body)
        else:
            body = re.sub(r'<pre class="mermaid">[\s\S]*?</pre>', '<p class="muted">(지도 그림 없음)</p>', body)
    body = rewrite(body, rel)
    sections.append(f'<section class="page" id="{slugs[rel]}" hidden>\n{body}\n</section>')

# 기존 사이트의 역할 표(R1–R22)를 한 쪽으로 들여온다. 내용은 고치지 않는다.
ROLES = os.path.join(os.path.dirname(ROOT), "mezard-parisi-diluted", "roles.html")
has_roles = os.path.exists(ROLES)
if has_roles:
    rt = open(ROLES, encoding="utf-8").read()
    art = re.search(r"<article[^>]*>([\s\S]*?)</article>", rt).group(1)
    art = re.sub(r'<a class="headerlink"[\s\S]*?</a>', "", art)
    art = re.sub(r"<(script|style)[\s\S]*?</\1>", "", art)
    art = re.sub(r'<a [^>]*href="(?!https?:)[^"]*"[^>]*>([\s\S]*?)</a>', r"\1", art)
    art = re.sub(r"<td>(R\d+)</td>", r'<td id="role-\1"><strong>\1</strong></td>', art)
    art = re.sub(r"<table>", '<div class="tablewrap"><table>', art).replace("</table>", "</table></div>")
    note = ('<p class="muted">기존 사이트(문장별 해석)의 역할 표를 그대로 옮긴 것이다. 재구성 작업에서는 아직 손대지 않았다. '
            'R13, R11, R19, R22에 대한 검토 의견과 빠진 대상은 로드맵의 "사용자 확인 필요"에 있다.</p>')
    art = re.sub(r"(</h1>)", r"\1" + note, art, count=1)
    sections.append(f'<section class="page" id="roles" hidden>\n{art}\n</section>')
    # 다른 쪽의 R번호를 역할 표로 잇는다 (수식·코드·기존 링크 안은 건드리지 않는다).
    def link_roles(sec):
        parts = re.split(r"(\$\$[\s\S]*?\$\$|\$[^$\n]*\$|<code[\s\S]*?</code>|<pre[\s\S]*?</pre>|<a [\s\S]*?</a>|<[^>]+>)", sec)
        for i in range(0, len(parts), 2):
            parts[i] = re.sub(r"\bR(\d{1,2})\b(?![\d_^{(])", lambda m: f'<a class="role" href="#roles">R{m.group(1)}</a>' if 1 <= int(m.group(1)) <= 22 else m.group(0), parts[i])
        return "".join(parts)
    sections[:-1] = [link_roles(s) for s in sections[:-1]]

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
.mapbox svg{display:block;min-width:1100px;max-width:none;height:auto}
.wrap>*{min-width:0}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
h1,h2,h3{text-wrap:balance}
a.role{text-decoration:none;border-bottom:1px dotted var(--accent)}
mjx-container.wide{display:block;max-width:100%;overflow-x:auto;overflow-y:hidden;padding:.2rem 0}
"""
nav = ('<nav class="top">' + "".join(f'<a href="#{s}" data-nav="{s}">{n}</a>' for s, n in
       [("home", "처음"), ("l0", "L0"), ("l1", "L1"), ("rules", "규칙 표"), ("map", "증명 지도"),
        ("roles", "역할 표"), ("cards", "카드 목록"), ("check-report", "검사 보고서")]) + "</nav>")
js = r"""
(function(){
  var pages=document.querySelectorAll('section.page'),done={};
  function show(){
    var id=(location.hash||'#home').slice(1),el=document.getElementById(id);
    if(!el||!el.classList.contains('page')){id='home';el=document.getElementById(id);}
    pages.forEach(function(p){p.hidden=(p!==el);});
    document.querySelectorAll('nav.top a').forEach(function(a){
      var n=a.getAttribute('data-nav');a.classList.toggle('cur',n===id||(n==='cards'&&id.indexOf('cards-')===0));});
    window.scrollTo(0,0);
    if(!done[id]&&window.MathJax&&MathJax.typesetPromise){done[id]=1;MathJax.typesetPromise([el]).then(function(){fit(el);}).catch(function(){});}
  }
  function fit(el){var R=el.getBoundingClientRect().right;el.querySelectorAll('mjx-container:not([display])').forEach(function(m){
    if(m.getBoundingClientRect().right>R+1){m.classList.add('wide');}});}
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
print(f"{len(pages)}쪽 → {p} ({len(out)//1024} KB), 안 바뀐 내부 링크 {len(left)}개", left[:5])
