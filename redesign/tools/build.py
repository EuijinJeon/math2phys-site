#!/usr/bin/env python3
"""정적 HTML 생성기: layers/*.md, cards/*.md, build/graph.json → site/

사용: python3 tools/build.py [--root DIR] [--out DIR]
  --root  cards/ 와 layers/ 를 담은 디렉터리 (기본: redesign/). source/ 와 graph.json 은 항상 실제 것을 쓴다.
"""
import argparse
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

MATHJAX = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"

ABS_GLOSS = {
    "exact": "같은 내용의 다른 표기",
    "weakening": "덜 말하지만 정확함",
    "blackbox": "진술은 정확하고 증명만 숨김",
    "approximation": "유효 범위 안에서만 맞음",
    "intuition": "논증에 쓰이지 않는 그림",
}

CSS = """
:root{--bg:#fbfbf9;--fg:#1d1f23;--muted:#60646c;--line:#dcdcd4;--accent:#1f5fbf;--card:#ffffff;
--code:#f0efe9;--ok:#1d7a46;--warn:#a86400;--bad:#b3261e;--tag:#e8eef9;}
@media (prefers-color-scheme:dark){:root{--bg:#16181c;--fg:#e4e6ea;--muted:#9aa0aa;--line:#33373e;
--accent:#7fb0ff;--card:#1d2026;--code:#262a31;--ok:#58c58a;--warn:#e0a14a;--bad:#ff8a80;--tag:#243049;}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,"Segoe UI","Noto Sans KR",
"Apple SD Gothic Neo","Malgun Gothic",sans-serif}
.wrap{max-width:52rem;margin:0 auto;padding:1rem 1rem 4rem}
nav.top{display:flex;flex-wrap:wrap;gap:.2rem .9rem;padding:.6rem 0 .8rem;border-bottom:1px solid var(--line);
margin-bottom:1.2rem;font-size:.92rem}
nav.top a{color:var(--muted);text-decoration:none}nav.top a:hover{color:var(--accent)}
nav.top a.cur{color:var(--fg);font-weight:600}
a{color:var(--accent)}
h1{font-size:1.65rem;line-height:1.3;margin:.2rem 0 .6rem}
h2{font-size:1.25rem;margin:2rem 0 .6rem;border-bottom:1px solid var(--line);padding-bottom:.2rem}
h3{font-size:1.07rem;margin:1.4rem 0 .4rem}
code{background:var(--code);padding:.08em .3em;border-radius:3px;font-size:.88em;word-break:break-word}
pre{background:var(--code);padding:.7rem .9rem;border-radius:6px;overflow-x:auto;font-size:.82rem;line-height:1.45}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border:1px solid var(--line);padding:.35rem .55rem;vertical-align:top;text-align:left}
th{background:var(--code)}
.tablewrap{overflow-x:auto;margin:.8rem 0}
.badge{display:inline-block;font-size:.78rem;padding:.05rem .5rem;border-radius:99px;background:var(--tag);
margin-right:.3rem;color:var(--fg)}
.badge.confirmed{background:color-mix(in srgb,var(--ok) 25%,transparent)}
.badge.unverified{background:color-mix(in srgb,var(--warn) 25%,transparent)}
.muted{color:var(--muted)}
.nolink{color:var(--muted);border-bottom:1px dotted var(--muted)}
a.node,.nolink{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.86em}
.iface{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:.3rem 1rem;margin:1rem 0}
.iface dt{font-weight:600;margin-top:.7rem;font-size:.9rem;color:var(--muted)}
.iface dd{margin:.15rem 0 .5rem}
.iface ul{margin:.2rem 0;padding-left:1.2rem}
details.child{border-left:3px solid var(--line);margin:.5rem 0 .5rem .1rem;padding:.1rem 0 .1rem .8rem}
details.child>summary{cursor:pointer;font-weight:600;list-style-position:outside}
details.child>summary .cm{font-weight:400;display:block;color:var(--fg);font-size:.95rem}
details.child .iface{font-size:.95rem}
details.src{margin-top:1.2rem}
details.src summary{cursor:pointer;font-weight:600}
pre.tex{white-space:pre;font-size:.78rem}
.ln{display:inline-block;width:3.2rem;color:var(--muted);user-select:none;text-align:right;margin-right:.8rem}
.mermaid{overflow-x:auto;text-align:left;width:min(96vw,1500px);position:relative;left:50%;transform:translateX(-50%);box-sizing:border-box;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:.5rem;margin:1rem 0}
.crumbs{font-size:.88rem;color:var(--muted);margin-bottom:.4rem}
ul.links li{margin:.35rem 0}
blockquote{margin:.8rem 0;padding:.1rem 1rem;border-left:3px solid var(--line);color:var(--muted)}
.hascard{}
.stag{font-size:.72rem;padding:0 .35rem;border-radius:99px;background:var(--tag);color:var(--muted);margin-left:.15rem}
.stat{color:var(--muted);font-size:.9rem}
mjx-container[display=true]{overflow-x:auto;overflow-y:hidden;max-width:100%;min-width:0!important}
a.gterm{color:inherit;text-decoration:underline dotted var(--muted);text-underline-offset:.2em;text-decoration-thickness:1px;cursor:help}
a.gterm:hover{color:var(--accent);text-decoration-color:var(--accent)}
.gterm.unknown{color:var(--bad);text-decoration:underline wavy var(--bad);text-underline-offset:.2em;cursor:help}
.gindex{columns:14rem auto;column-gap:1.5rem;font-size:.92rem;margin:.4rem 0 1rem}
.gindex h3{font-size:.85rem;color:var(--muted);margin:.8rem 0 .2rem;break-after:avoid}
.gindex ul{list-style:none;margin:0;padding:0}
.gindex li{margin:.1rem 0;break-inside:avoid}
.gent{margin:1rem 0;padding:.1rem 1rem .4rem;background:var(--card);border:1px solid var(--line);border-radius:8px;scroll-margin-top:1rem}
.gent:target,.gent.hl{border-color:var(--accent);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 30%,transparent)}
.gent h3{margin:.7rem 0 .2rem}
.gent .gslug{font-size:.75rem;font-weight:400;color:var(--muted);margin-left:.4rem}
.gent dl{margin:.2rem 0}
.gent dt{font-weight:600;font-size:.85rem;color:var(--muted);margin-top:.5rem}
.gent dd{margin:.1rem 0 .3rem}
.gent dd p{margin:.2rem 0}
@media (prefers-reduced-motion:reduce){.gent{transition:none}}
@media (max-width:600px){body{font-size:15.5px}h1{font-size:1.4rem}}
"""

MATHJAX_CFG = r"""
window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']],processEscapes:true,
macros:{E:'\\mathbb E',P:'\\mathbb P',R:'\\mathbb R',N:'\\mathbb N',cB:'\\mathcal B',cF:'\\mathcal F',cT:'\\mathcal T',
eps:'\\varepsilon',dd:'\\,\\mathrm d',norm:['\\lVert#1\\rVert',1],abs:['\\lvert#1\\rvert',1],angles:['\\langle#1\\rangle',1],
Var:'\\operatorname{Var}',Cov:'\\operatorname{Cov}',arctanh:'\\operatorname{arctanh}',Pois:'\\operatorname{Poisson}',
supp:'\\operatorname{supp}'}},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};
"""

esc = html.escape


# ============================================================ markdown
class Ctx:
    """링크 해소에 필요한 정보."""

    def __init__(self, cards, graph, base="", gloss=None):
        self.gloss = gloss or {}   # slug → GlossEntry
        self.S = None              # Struct (섹션 구조), main() 이 채운다
        self.cards = {c.id: c for c in cards if c.id and c.fm is not None}
        self.nodes = {n["id"]: n for n in (graph["nodes"] if graph else [])}
        self.base = base
        ids = set(self.cards) | set(self.nodes)
        ids = {i for i in ids if ":" in i}
        self.idre = None
        if ids:
            alt = "|".join(re.escape(i) for i in sorted(ids, key=lambda x: (-len(x), x)))
            self.idre = re.compile(r"(?<![\w:/.#-])(" + alt + r")(?![\w-])")

    def with_base(self, base):
        c = Ctx.__new__(Ctx)
        c.__dict__.update(self.__dict__)
        c.base = base
        return c

    def gloss_link(self, slug, label=None):
        """[[g:slug]] → glossary.html#g-slug 링크 (표제어를 보이고, title 에 뜻). 없는 slug 는 unknown 표시."""
        en = self.gloss.get(slug)
        if en is None:
            return (f'<span class="gterm unknown" title="용어집에 없는 용어: g:{esc(slug)}">'
                    f'{esc(label or slug)}</span>')
        title = C.plain_text(en.get("뜻"), 200)
        return (f'<a class="gterm" href="{esc(self.base)}glossary.html#g-{esc(slug)}" title="{esc(title)}">'
                f'{esc(label or en.headword)}</a>')

    def card_href(self, cid):
        return f"{self.base}cards/{page_name(cid)}"

    def link(self, nid, text=None):
        """노드 id 에 대한 HTML 링크(카드 있으면 링크, 없으면 점선 span)."""
        n = self.nodes.get(nid)
        label = text if text is not None else nid
        num = n.get("number") if n else None
        if nid in self.cards:
            c = self.cards[nid]
            t = c.get("title") or ""
            title = " ".join(x for x in (num, t) if x)
            return (f'<a class="node" href="{esc(self.card_href(nid))}" title="{esc(title)}">{esc(label)}</a>')
        title = (num or "") + (" (카드 없음)" if n else " (알 수 없는 노드)")
        return f'<span class="nolink" title="{esc(title.strip())}">{esc(label)}</span>'


def page_name(cid):
    return cid.replace(":", ".") + ".html"


def slug(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^\w\- ]", "", s, flags=re.U).strip().lower()
    return re.sub(r"\s+", "-", s) or "sec"


class MD:
    def __init__(self, ctx):
        self.ctx = ctx
        self.stash_list = []

    # ---- 보호
    def stash(self, h):
        self.stash_list.append(h)
        return f"\x00{len(self.stash_list) - 1}\x00"

    def restore(self, s):
        for _ in range(4):
            n = re.sub(r"\x00(\d+)\x00", lambda m: self.stash_list[int(m.group(1))], s)
            if n == s:
                break
            s = n
        return s

    def protect(self, text):
        # 코드 블록
        def fence(m):
            return "\n\n" + self.stash("<pre><code>" + esc(m.group(2)) + "</code></pre>") + "\n\n"
        text = re.sub(r"(?m)^[ \t]*```[^\n]*\n(.*?)^[ \t]*```[ \t]*$",
                      lambda m: "\n\n" + self.stash("<pre><code>" + esc(m.group(1)) + "</code></pre>") + "\n\n",
                      text, flags=re.S)

        # 인라인 코드 (내용이 정확히 노드 id 이면 링크)
        def code(m):
            body = m.group(2)
            h = "<code>" + esc(body) + "</code>"
            if self.ctx.idre and self.ctx.idre.fullmatch(body.strip()):
                h = self.ctx.link(body.strip(), None).replace('class="node"', 'class="node"', 1)
            return self.stash(h)
        text = re.sub(r"(`+)(.+?)\1", code, text)
        # 수식
        def math(m):
            return self.stash(esc(m.group(0)))
        text = re.sub(r"\$\$.+?\$\$", math, text, flags=re.S)
        text = re.sub(r"\\\[.+?\\\]", math, text, flags=re.S)
        text = re.sub(r"\\\(.+?\\\)", math, text, flags=re.S)
        text = re.sub(r"(?<![\\$])\$(?![\s$])((?:\\.|[^$\\\n]|\n(?![ \t]*\n))+?)(?<![\s\\])\$(?!\$)", math, text)
        return text

    # ---- 인라인
    def inline(self, s):
        s = esc(s, quote=False)

        def wiki(m):
            body = m.group(1)
            nid, _, lab = body.partition("|")
            nid = nid.strip()
            if nid.startswith("g:"):
                return self.stash(self.ctx.gloss_link(nid[2:].strip(), html.unescape(lab).strip() or None))
            return self.stash(self.ctx.link(nid, lab.strip() or None))
        # 표 칸에서는 표시어를 줄 수 없어 "낱말([[g:slug]])" 꼴로 쓴다. 이때는 표제어를 되풀이하지 않고 작은 표지로 잇는다.
        s = re.sub(r"\(\[\[g:([a-z0-9-]+)\]\]\)",
                   lambda m: self.stash('<sup>' + self.ctx.gloss_link(m.group(1), "용어") + '</sup>'), s)
        s = re.sub(r"\[\[([^\]\n]+?)\]\]", wiki, s)

        def link(m):
            text, url = m.group(1), m.group(2).strip()
            if not re.match(r"^[a-z]+:", url) and not url.startswith("#"):
                url = re.sub(r"\.md(#|$)", r".html\1", url)
            return self.stash(f'<a href="{esc(url)}">' + text + "</a>")
        s = re.sub(r"\[([^\]\n]+?)\]\(([^)\s]+)\)", link, s)
        if self.ctx.idre:
            s = self.ctx.idre.sub(lambda m: self.stash(self.ctx.link(m.group(1))), s)
        s = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", r"<em>\1</em>", s)
        s = re.sub(r"(?<![\w])_(?=[^\s_])(.+?)(?<=[^\s_])_(?![\w])", r"<em>\1</em>", s)
        s = re.sub(r"~~(.+?)~~", r"<del>\1</del>", s)
        return s

    # ---- 블록
    def render(self, text):
        text = text.replace("\r\n", "\n")
        text = self.protect(text)
        out = self.blocks(text.split("\n"))
        return self.restore(out)

    def render_inline_only(self, text):
        text = self.protect((text or "").replace("\r\n", "\n"))
        return self.restore(self.inline(re.sub(r"\s*\n\s*", " ", text.strip())))

    LIST = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")

    def blocks(self, lines):
        out = []
        i = 0
        n = len(lines)
        while i < n:
            l = lines[i]
            if not l.strip():
                i += 1
                continue
            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", l)
            if m:
                lv = len(m.group(1))
                inner = self.inline(m.group(2))
                out.append(f'<h{lv} id="{slug(self.restore(inner))}">{inner}</h{lv}>')
                i += 1
                continue
            if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", l):
                out.append("<hr>")
                i += 1
                continue
            if l.lstrip().startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]) \
                    and "|" in lines[i + 1]:
                j = i
                while j < n and lines[j].lstrip().startswith("|"):
                    j += 1
                out.append(self.table(lines[i:j]))
                i = j
                continue
            if l.lstrip().startswith(">"):
                j = i
                buf = []
                while j < n and lines[j].lstrip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[j]))
                    j += 1
                out.append("<blockquote>" + self.blocks(buf) + "</blockquote>")
                i = j
                continue
            if self.LIST.match(l):
                j, h = self.list_block(lines, i)
                out.append(h)
                i = j
                continue
            # 문단
            buf = [l]
            j = i + 1
            while j < n and lines[j].strip() and not re.match(r"^#{1,6}\s", lines[j]) \
                    and not self.LIST.match(lines[j]) and not lines[j].lstrip().startswith(("|", ">")):
                buf.append(lines[j])
                j += 1
            para = "\n".join(x.strip() for x in buf)
            if re.fullmatch(r"\x00\d+\x00", para) and self.stash_list[int(para.strip("\x00"))].startswith("<pre"):
                out.append(para)
            else:
                out.append("<p>" + self.inline(para) + "</p>")
            i = j
        return "\n".join(out)

    def list_block(self, lines, i):
        n = len(lines)
        m0 = self.LIST.match(lines[i])
        base = len(m0.group(1).expandtabs(4))
        ordered = m0.group(2)[0].isdigit()
        items = []  # list of list-of-lines (content lines)
        j = i
        cur = None
        while j < n:
            l = lines[j]
            if not l.strip():
                # 빈 줄: 다음 줄이 이 목록에 속하면 계속
                k = j + 1
                while k < n and not lines[k].strip():
                    k += 1
                if k < n:
                    ind = len(lines[k]) - len(lines[k].lstrip())
                    mm = self.LIST.match(lines[k])
                    if ind > base or (mm and ind == base and (mm.group(2)[0].isdigit() == ordered)):
                        if cur is not None:
                            cur.append("")
                        j += 1
                        continue
                break
            mm = self.LIST.match(l)
            ind = len(l) - len(l.lstrip())
            if mm and ind <= base:
                if ind < base or mm.group(2)[0].isdigit() != ordered:
                    break
                cur = [mm.group(3)]
                items.append((len(mm.group(1)) + len(mm.group(2)) + 1, cur))
                j += 1
                continue
            if cur is None:
                break
            if ind > base or not (l.lstrip().startswith(("#", "|", ">"))):
                width = items[-1][0]
                cur.append(l[min(width, ind):] if ind else l)
                j += 1
                continue
            break
        tag = "ol" if ordered else "ul"
        parts = []
        for _, content in items:
            h = self.blocks(content)
            if h.count("<p>") == 1 and h.startswith("<p>") and h.endswith("</p>"):
                h = h[3:-4]
            elif h.startswith("<p>") and "</p>" in h:
                # 첫 문단만 풀고 나머지는 중첩 블록
                first, rest = h.split("</p>", 1)
                h = first[3:] + rest
            parts.append(f"<li>{h}</li>")
        return j, f"<{tag}>" + "".join(parts) + f"</{tag}>"

    def table(self, rows):
        cells = [C.split_row(r) for r in rows]
        head = cells[0]
        body = cells[2:]
        h = ['<div class="tablewrap"><table><thead><tr>']
        for c in head:
            h.append("<th>" + self.inline(c.strip()) + "</th>")
        h.append("</tr></thead><tbody>")
        for r in body:
            h.append("<tr>")
            for k in range(len(head)):
                h.append("<td>" + self.inline((r[k] if k < len(r) else "").strip()) + "</td>")
            h.append("</tr>")
        h.append("</tbody></table></div>")
        return "".join(h)


def md_html(text, ctx):
    return MD(ctx).render(text)


def md_inline(text, ctx):
    return MD(ctx).render_inline_only(text)


# ============================================================ 페이지 틀
NAV = [("index.html", "처음"), ("L0.html", "L0"), ("L1.html", "L1"), ("rules.html", "규칙 표"),
       ("glossary.html", "용어집"), ("map.html", "증명 지도"), ("cards/index.html", "카드 목록"), ("check-report.html", "검사 보고서")]


def page(title, body, base="", cur=None, extra_head="", extra_tail=""):
    nav = []
    for href, name in NAV:
        cls = ' class="cur"' if cur == href else ""
        nav.append(f'<a{cls} href="{base}{href}">{name}</a>')
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<style>{CSS}</style>
<script>{MATHJAX_CFG}</script>
<script async src="{MATHJAX}"></script>
{extra_head}
</head>
<body>
<div class="wrap">
<nav class="top">{"".join(nav)}</nav>
{body}
</div>
{extra_tail}
</body>
</html>
"""


# ============================================================ 카드 페이지
def sec_tag(ctx, cid):
    """카드 ID 뒤에 붙이는 소속 섹션 표지(다른 섹션의 카드일 때 눈에 띄게)."""
    S = ctx.S
    if not S or cid not in S.cards:
        return ""
    return f' <span class="stag">{esc(S.tag(cid))}</span>'


def uses_links(c, ctx):
    if not c.uses:
        return '<span class="muted">없음</span>'
    li = []
    for u in c.uses:
        n = ctx.nodes.get(u)
        num = f' <span class="muted">{esc(n["number"])}</span>' if n and n.get("number") else ""
        t = ""
        if u in ctx.cards and ctx.cards[u].get("title"):
            t = f' <span class="muted">— {esc(str(ctx.cards[u].get("title")))}</span>'
        li.append("<li>" + ctx.link(u) + sec_tag(ctx, u) + num + t + "</li>")
    return "<ul>" + "".join(li) + "</ul>"


def used_by(c, ctx, allc):
    users = sorted(x.id for x in allc if x.id and x.fm is not None and c.id in x.uses and x.id != c.id)
    if not users:
        return '<span class="muted">(이 카드를 쓰는 카드 없음)</span>'
    return "<ul>" + "".join("<li>" + ctx.link(u) + sec_tag(ctx, u) + "</li>" for u in users) + "</ul>"


def field_block(c, key, ctx):
    v = c.get(key)
    if C.is_null(v):
        return None
    return md_html(str(v), ctx)


def interface(c, ctx, allc, brief=False):
    rows = []
    rows.append("<dt>받는 것 (uses)</dt><dd>" + uses_links(c, ctx) + "</dd>")
    prov = c.get("provides")
    ph = md_inline(str(prov), ctx) if not C.is_null(prov) else '<span class="muted">(적지 않음)</span>'
    rows.append("<dt>내놓는 것 (provides)</dt><dd>" + ph + "<br><span class=\"muted\">이 카드를 쓰는 카드:</span>"
                + used_by(c, ctx, allc) + "</dd>")
    m = field_block(c, "math", ctx)
    rows.append("<dt>수학 진술</dt><dd>" + (m or '<span class="muted">(없음)</span>') + "</dd>")
    p = field_block(c, "physics", ctx)
    rows.append("<dt>물리 진술</dt><dd>" + (p or '<span class="muted">대응 없음</span>') + "</dd>")
    g = field_block(c, "gap", ctx)
    if g or p:
        rows.append("<dt>차이</dt><dd>" + (g or '<span class="muted">(적지 않음)</span>') + "</dd>")
    ab = c.get("abstraction")
    if not C.is_null(ab):
        gl = ABS_GLOSS.get(str(ab), "")
        rows.append(f'<dt>축약 유형</dt><dd><code>{esc(str(ab))}</code>'
                    + (f' <span class="muted">— {esc(gl)}</span>' if gl else "") + "</dd>")
    return '<dl class="iface">' + "".join(rows) + "</dl>"


def children_html(c, ctx, allc, stack, depth=0):
    if not c.children:
        return ""
    out = []
    for ch in c.children:
        cc = ctx.cards.get(ch)
        if cc is None:
            out.append(f'<div class="muted">(카드 없음: <code>{esc(ch)}</code>)</div>')
            continue
        if ch in stack or depth > 8:
            out.append(f'<div class="muted">(순환 또는 너무 깊음: <code>{esc(ch)}</code>)</div>')
            continue
        title = esc(str(cc.get("title") or ch))
        m = cc.get("math")
        msum = ""
        if not C.is_null(m):
            msum = '<span class="cm">' + md_inline(str(m), ctx) + "</span>"
        inner = interface(cc, ctx, allc)
        inner += children_html(cc, ctx, allc, stack | {ch}, depth + 1)
        link = f' <a class="node" href="{esc(ctx.card_href(ch))}">↗</a>'
        out.append(f'<details class="child"><summary>{title}{link}{msum}</summary>{inner}</details>')
    return "".join(out)


def source_html(c):
    if not c.source:
        return ""
    parts = []
    for (f, a, b) in c.source:
        lines = C.source_lines(f) or []
        buf = []
        for k in range(a, b + 1):
            txt = lines[k - 1] if k - 1 < len(lines) else ""
            buf.append(f'<span class="ln">{k}</span>{esc(txt)}')
        parts.append(f"<h4>{esc(f)}:{a}-{b}</h4><pre class=\"tex\"><code>" + "\n".join(buf) + "</code></pre>")
    return '<details class="src"><summary>원문 (' + ", ".join(f"{esc(f)}:{a}-{b}" for f, a, b in c.source) \
        + ")</summary>" + "".join(parts) + "</details>"


def section_block(c, ctx):
    """섹션 카드와 주정리 카드의 머리에 카드 수와 지도 링크를 보인다."""
    S = ctx.S
    if not S:
        return ""
    for sc in S.secs:
        if sc["card"] != c.id:
            continue
        k = sc["key"]
        extra = ""
        if k == "main":
            extra = " 진술은 §2의 원문 줄, 증명은 §9의 원문 줄이라 §2와 §9의 섹션 카드가 모두 이 카드를 자식으로 둔다."
        elif S.MAIN in c.children:
            extra = f" 주정리({ctx.link(S.MAIN)})는 이 섹션 카드의 자식이지만 주정리 묶음에 따로 센다."
        return ('<p class="stat">이 섹션의 카드 ' + str(len(S.members[k])) + "장 (증명 단계 포함)." + extra
                + f' <a href="{ctx.base}{map_href(k)}">이 섹션의 증명 지도</a> · <a href="{ctx.base}map.html">섹션 지도</a></p>')
    return ""


def card_page(c, ctx, allc):
    n = ctx.nodes.get(c.id)
    num = n.get("number") if n else None
    title = str(c.get("title") or c.id)
    head = f'<div class="crumbs"><a href="index.html">카드 목록</a>'
    parents = sorted(x.id for x in allc if x.id and x.fm is not None and c.id in x.children)
    if parents:
        head += " · 상위: " + ", ".join(ctx.link(p) + sec_tag(ctx, p) for p in parents)
    S = ctx.S
    if S and S.home(c.id):
        h = S.home(c.id)
        head += f' · 섹션: <a href="{ctx.base}{map_href(h)}">{esc(S.label(h))}</a>'
        if len(parents) > 1:
            head += " (상위가 둘이어도 이 섹션에만 센다)"
    head += "</div>"
    h1 = f"<h1>{esc(num + ' ' if num else '')}{esc(title)}</h1>"
    badges = (f'<span class="badge">{esc(str(c.get("kind") or "?"))}</span>'
              f'<span class="badge {esc(str(c.get("status") or ""))}">{esc(str(c.get("status") or "상태 없음"))}</span>'
              f' <code>{esc(c.id)}</code>')
    body = head + h1 + "<p>" + badges + "</p>"
    body += section_block(c, ctx)
    body += interface(c, ctx, allc)
    ch = children_html(c, ctx, allc, {c.id})
    if ch:
        body += "<h2>펼침</h2>" + ch
    if c.body.strip():
        body += "<h2>본문</h2>" + md_html(c.body, ctx)
    body += source_html(c)
    return page(f"{num + ' ' if num else ''}{title}", body, base="../")


def card_index(cards, ctx):
    rows = []
    for c in cards:
        if c.fm is None or not c.id:
            rows.append(f'<tr><td colspan="7"><span style="color:var(--bad)">머리말 오류</span> '
                        f'<code>{esc(c.fname)}</code>: {esc("; ".join(c.errors))}</td></tr>')
            continue
        n = ctx.nodes.get(c.id)
        rows.append("<tr><td>" + esc(ctx.S.tag(c.id) if ctx.S else "") + "</td><td>" + esc(n["number"] if n and n.get("number") else "") + "</td><td>"
                    + ctx.link(c.id) + "</td><td>" + esc(str(c.get("kind") or "")) + "</td><td>"
                    + esc(str(c.get("title") or "")) + "</td><td>" + esc(str(c.get("abstraction") or "")) + "</td><td>"
                    + esc(str(c.get("status") or "")) + "</td></tr>")
    if not rows:
        t = "<p class=\"muted\">아직 카드가 없다.</p>"
    else:
        t = ('<div class="tablewrap"><table><thead><tr><th>섹션</th><th>번호</th><th>id</th><th>종류</th><th>제목</th><th>축약</th>'
             "<th>상태</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")
    return page("카드 목록", f"<h1>카드 목록</h1><p class=\"stat\">{len(cards)}개</p>" + t, base="../",
                cur="cards/index.html")


# ============================================================ 용어집
GLOSS_LABELS = (("기호", "기호"), ("뜻", "뜻"), ("역할", "역할"), ("정의 위치", "정의 위치"),
                ("물리 대응", "물리 대응"), ("쓰지 않는 뜻", "쓰지 않는 뜻"))


def glossary_page(path, entries, problems, exists, ctx):
    if not exists:
        return page("용어집", '<h1>용어집</h1><p class="muted">layers/glossary.md 가 아직 없다.</p>', cur="glossary.html")
    text = path.read_text(encoding="utf-8")
    first = re.search(r"(?m)^##\s", text)
    intro = text[:first.start()] if first else text
    m = re.search(r"(?m)^#\s+(.*)$", intro)
    title = m.group(1).strip() if m else "용어집"
    intro = re.sub(r"(?m)^#\s+.*$", "", intro).strip()
    body = f"<h1>{esc(title)}</h1>"
    if intro:
        body += md_html(intro, ctx)
    # 색인: 묶음별
    groups = []
    for en in entries:
        if not groups or groups[-1][0] != en.group:
            groups.append((en.group, []))
        groups[-1][1].append(en)
    idx = ['<nav class="gindex" aria-label="용어 색인">']
    for g, ens in groups:
        if g:
            idx.append(f"<h3>{md_inline(g, ctx)}</h3>")
        idx.append("<ul>" + "".join(f'<li><a href="#g-{esc(e.slug)}">{esc(e.headword)}</a></li>' for e in ens) + "</ul>")
    idx.append("</nav>")
    body += f'<p class="stat">항목 {len(entries)}개</p>' + "".join(idx)
    if problems:
        body += ('<div class="iface"><strong style="color:var(--bad)">형식 문제</strong><ul>'
                 + "".join(f"<li>줄 {ln}: {esc(msg)}</li>" for ln, msg in problems) + "</ul></div>")
    seen = set()
    for g, ens in groups:
        if g:
            body += f"<h2>{md_inline(g, ctx)}</h2>"
        for en in ens:
            dup = en.slug in seen
            seen.add(en.slug)
            eid = f"g-{en.slug}" + ("-dup" if dup else "")
            rows = []
            for key, label in GLOSS_LABELS:
                v = en.fields.get(key)
                if C.is_null(v):
                    if key in ("뜻", "역할", "정의 위치"):
                        rows.append(f'<dt>{label}</dt><dd><span style="color:var(--bad)">(비었음)</span></dd>')
                    continue
                rows.append(f"<dt>{label}</dt><dd>{md_html(v, ctx)}</dd>")
            body += (f'<section class="gent" id="{esc(eid)}"><h3>{esc(en.headword)}'
                     f'<span class="gslug">g:{esc(en.slug)}</span></h3><dl>' + "".join(rows) + "</dl></section>")
    return page(title, body, cur="glossary.html")


# ============================================================ 지도
def mermaid_text(s, limit=34):
    s = re.sub(r"\$([^$]*)\$", r"\1", s or "")
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = re.sub(r"[{}\\\[\]\"<>|`#&;]", "", s)
    s = s.replace("--", "–").replace("~", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= limit else s[:limit - 1] + "…"


class Struct:
    """카드가 어느 섹션에 속하는가. 한 카드는 정확히 한 곳에만 센다.

    집 = 카드의 첫 `source` 파일을 덮는 섹션 카드. 단, 주정리(`main:theorem`)와 그 자손(증명 단계)은
    진술은 §2에, 증명은 §9 원문 줄에 있어 두 섹션 카드의 자식이 되므로 따로 '주정리' 묶음으로 센다.
    """
    MAIN = "main:theorem"

    def __init__(self, cards, graph):
        self.cards = {c.id: c for c in cards if c.id and c.fm is not None}
        self.parents = {}
        for c in self.cards.values():
            for ch in c.children:
                self.parents.setdefault(ch, []).append(c.id)
        gnodes = graph["nodes"] if graph else []
        gby = {n["id"]: n for n in gnodes}
        self.file2key = {}
        self.secs = []   # dict(key, card, num, title, file)
        for c in self.cards.values():
            if c.get("kind") != "section" or not c.source:
                continue
            f = c.source[0][0]
            n = gby.get(c.id)
            if not n or n["kind"] not in ("section", "subsection"):
                cand = [x for x in gnodes if x["kind"] in ("section", "subsection") and x["file"] == f]
                n = min(cand, key=lambda x: x["lines"][0]) if cand else None
            num = n["number"] if n else ""
            title = n["title"] if n else str(c.get("title") or c.id)
            key = f[:-4] if f.endswith(".tex") else f
            self.file2key[f] = key
            self.secs.append({"key": key, "card": c.id, "num": num, "title": title, "file": f})

        def numkey(x):
            return tuple(int(p) if p.isdigit() else 0 for p in re.split(r"[.]", x["num"] or "99"))
        self.secs.sort(key=numkey)
        self.main = set()
        if self.MAIN in self.cards:
            st = [self.MAIN]
            while st:
                x = st.pop()
                if x in self.main:
                    continue
                self.main.add(x)
                st.extend(self.cards[x].children if x in self.cards else [])
            # 주정리 묶음은 §2.2(overview) 다음, §3 앞에 둔다
            pos = 0
            for i, sc in enumerate(self.secs):
                if sc["num"].startswith("2"):
                    pos = i + 1
            self.secs.insert(pos, {"key": "main", "card": self.MAIN, "num": "", "title": "Main theorem (진술 §2.1, 증명 §9)",
                                   "file": ""})
        self.by_key = {sc["key"]: sc for sc in self.secs}
        self.members = {sc["key"]: [] for sc in self.secs}
        for c in self.cards.values():
            h = self.home(c.id)
            if h in self.members:
                self.members[h].append(c.id)

    def home(self, cid):
        if cid in self.main:
            return "main"
        c = self.cards.get(cid)
        if not c or not c.source:
            return None
        return self.file2key.get(c.source[0][0])

    def label(self, key):
        sc = self.by_key[key]
        return "주정리" if key == "main" else "§" + sc["num"]

    def tag(self, cid):
        h = self.home(cid)
        return self.label(h) if h else ""

    def lift(self, cid):
        """증명 단계는 가장 가까운 단계 아닌 조상으로 올려 센다."""
        seen = set()
        while cid in self.cards and self.cards[cid].get("kind") == "step" and self.parents.get(cid) and cid not in seen:
            seen.add(cid)
            cid = self.parents[cid][0]
        return cid


def map_href(key):
    return f"map-{key}.html"


def section_map(S):
    """(i) 섹션 단위 지도. 섹션 카드 + 주정리를 노드로, 카드의 uses 를 섹션 사이 간선으로 모은다.
    반환: (mermaid 텍스트, 간선 목록[(쓰이는 키, 쓰는 키, 횟수)], 서로 쓰는 쌍)."""
    keys = [sc["key"] for sc in S.secs]
    nid = {k: f"S{i}" for i, k in enumerate(keys)}
    agg = {}
    for c in S.cards.values():
        hc = S.home(c.id)
        if not hc:
            continue
        skip = set()
        if c.get("kind") == "section":
            # 섹션 카드의 uses 는 자손이 쓰는 것을 모은 목록이기도 하다. 자손이 쓰는 것은 자손 쪽에서 세고
            # (주정리가 §2 카드의 자식이라 §2가 §4·§8·§9를 쓰는 것처럼 보이는 것을 막는다) 여기서는 뺀다.
            st = list(c.children)
            seen = set()
            while st:
                x = st.pop()
                if x in seen or x not in S.cards:
                    continue
                seen.add(x)
                skip.update(S.cards[x].uses)
                st.extend(S.cards[x].children)
        for u in set(c.uses) - skip:
            hu = S.home(u)
            if hu and hu != hc:
                agg[(hu, hc)] = agg.get((hu, hc), 0) + 1
    L = ["flowchart TB"]
    for k in keys:
        sc = S.by_key[k]
        n = len(S.members[k])
        if k == "main":
            lab = f"주정리<br/>Theorem 2.1<br/>{n}장 (진술 + 증명 단계)"
        else:
            lab = f'§{sc["num"]}<br/>{mermaid_text(sc["title"], 36)}<br/>{n}장'
        L.append(f'  {nid[k]}["{lab}"]')
    for (a, b), cnt in sorted(agg.items(), key=lambda kv: (keys.index(kv[0][0]), keys.index(kv[0][1]))):
        L.append(f"  {nid[a]} -->|{cnt}| {nid[b]}")
    L.append("  classDef sec fill:#d6e6ff,stroke:#1f5fbf,color:#111;")
    L.append("  classDef mainc fill:#ffe9b8,stroke:#a86400,color:#111;")
    L.append("  class " + ",".join(nid[k] for k in keys if k != "main") + " sec;")
    if "main" in nid:
        L.append(f"  class {nid['main']} mainc;")
    for k in keys:
        L.append(f'  click {nid[k]} "cards/{page_name(S.by_key[k]["card"])}"')
    mutual = sorted({tuple(sorted((a, b), key=keys.index)) for (a, b) in agg if (b, a) in agg}, key=lambda p: (keys.index(p[0]), keys.index(p[1])))
    return "\n".join(L), sorted(agg.items()), mutual


def sec_cycles(S, agg):
    """섹션 간선 그래프의 순환(강연결 성분 크기 > 1)을 센다."""
    g = {}
    for (a, b), _ in agg:
        g.setdefault(a, []).append(b)
    index, low, on, st, res, cnt = {}, {}, set(), [], [], [0]

    def sc(v):
        index[v] = low[v] = cnt[0]
        cnt[0] += 1
        st.append(v)
        on.add(v)
        for w in g.get(v, []):
            if w not in index:
                sc(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = st.pop()
                on.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1:
                res.append(sorted(comp))
    for v in sorted(g):
        if v not in index:
            sc(v)
    return res


KIND_GROUP = {"theorem": "thm", "proposition": "thm", "lemma": "thm", "corollary": "thm"}


def section_detail_map(S, key):
    """(ii) 한 섹션의 정리류 카드(단계 제외)와 밖으로 나가는/들어오는 간선.
    증명 단계가 쓰는 것·단계를 쓰는 것은 가장 가까운 단계 아닌 조상 카드로 올려 그린다.
    섹션 카드 자신의 uses(전체 목록)는 그리지 않는다. 반환: (mermaid, 안 카드 id 목록, 들어오는 {id:set}, 나가는 {id:set})."""
    cards = S.cards
    internal = [i for i in sorted(S.members[key]) if cards[i].get("kind") not in ("step", "section")]
    iset = set(internal)
    edges = {}
    for c in cards.values():
        a = S.lift(c.id)
        if a not in cards or cards[a].get("kind") == "section":
            continue
        for u in c.uses:
            b = S.lift(u)
            if b not in cards or b == a or cards[b].get("kind") == "section":
                continue
            if a in iset or b in iset:
                edges.setdefault((b, a), 0)
                edges[(b, a)] += 1
    ext = sorted({x for e in edges for x in e if x not in iset}, key=lambda i: (S.home(i) or "", i))
    ids = {i: f"a{k}" for k, i in enumerate(internal)}

    def node(i):
        c = cards[i]
        t = mermaid_text(str(c.get("title") or i), 30)
        return f'{ids[i]}["{t}<br/>{mermaid_text(i, 40)}"]'
    # 안쪽 간선은 이행 축약: 다른 안쪽 경로로 이어지는 간선은 그리지 않는다(읽을 수 없는 털뭉치를 피한다).
    inner = {(b, a) for (b, a) in edges if b in iset and a in iset}
    succ = {}
    for b, a in inner:
        succ.setdefault(b, set()).add(a)

    def reach(src, dst, skip):
        st, seen = [src], {src}
        while st:
            x = st.pop()
            for y in succ.get(x, ()):
                if (x, y) == skip or y in seen:
                    continue
                if y == dst:
                    return True
                seen.add(y)
                st.append(y)
        return False
    kept = sorted(e for e in inner if not reach(e[0], e[1], e))
    # 밖의 카드는 섹션별로 한 노드로 묶고, 안쪽 카드 하나와 그 섹션 사이의 연결을 카드 수와 함께 한 간선으로 그린다.
    # 밖 카드 하나하나의 연결은 아래 표에 있다.
    xs = {}
    for (b, a) in edges:
        if b in iset and a not in iset:
            xs.setdefault((b, S.home(a), "out"), set()).add(a)
        elif a in iset and b not in iset:
            xs.setdefault((a, S.home(b), "in"), set()).add(b)
    xhomes = sorted({h for (_, h, _) in xs}, key=lambda h: [sc["key"] for sc in S.secs].index(h) if h in S.by_key else 99)
    xid = {h: f"X{k}" for k, h in enumerate(xhomes)}
    L = ["flowchart TB"]
    sc = S.by_key[key]
    head = "주정리" if key == "main" else f'§{sc["num"]} {mermaid_text(sc["title"], 40)}'
    L.append(f'  subgraph IN["{head}"]')
    for i in internal:
        L.append("    " + node(i))
    L.append("  end")
    for h in xhomes:
        n_ext = len({x for (_, hh, _), v in xs.items() if hh == h for x in v})
        lab = (S.label(h) + " " + mermaid_text(S.by_key[h]["title"], 28)) if h in S.by_key else "?"
        L.append(f'  {xid[h]}["밖: {lab}<br/>카드 {n_ext}장"]')
    for (b, a) in kept:
        L.append(f"  {ids[b]} --> {ids[a]}")
    for (i, h, d), v in sorted(xs.items(), key=lambda kv: (ids[kv[0][0]], xid[kv[0][1]], kv[0][2])):
        if d == "in":
            L.append(f"  {xid[h]} -.->|{len(v)}| {ids[i]}")
        else:
            L.append(f"  {ids[i]} -.->|{len(v)}| {xid[h]}")
    thm = [ids[i] for i in internal if cards[i].get("kind") in KIND_GROUP]
    oth = [ids[i] for i in internal if cards[i].get("kind") not in KIND_GROUP]
    L.append("  classDef thm fill:#d6e6ff,stroke:#1f5fbf,color:#111;")
    L.append("  classDef oth fill:#eef0f3,stroke:#8a8f98,color:#222;")
    L.append("  classDef ext fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#444;")
    if thm:
        L.append("  class " + ",".join(thm) + " thm;")
    if oth:
        L.append("  class " + ",".join(oth) + " oth;")
    if xhomes:
        L.append("  class " + ",".join(xid[h] for h in xhomes) + " ext;")
    for i in internal:
        L.append(f'  click {ids[i]} "cards/{page_name(i)}"')
    for h in xhomes:
        if h in S.by_key:
            L.append(f'  click {xid[h]} "{map_href(h)}"')
    incoming = {i: set() for i in internal}
    outgoing = {i: set() for i in internal}
    for (b, a) in edges:
        if a in iset and b not in iset:
            incoming[a].add(b)
        if b in iset and a not in iset:
            outgoing[b].add(a)
    return "\n".join(L), internal, incoming, outgoing, len(ext), len(edges)


def all_maps(S):
    """이름 → 사이트 쪽 이름과 Mermaid 텍스트. render_maps.py 와 build.py 가 함께 쓴다."""
    out = {"sections": section_map(S)[0]}
    for sc in S.secs:
        out["sec-" + sc["key"]] = section_detail_map(S, sc["key"])[0]
    return out


MERMAID_TAIL = (f'<script src="{MERMAID}"></script>\n'
                "<script>if(window.mermaid){mermaid.initialize({startOnLoad:true,securityLevel:'loose',"
                "flowchart:{useMaxWidth:true,htmlLabels:true}});}</script>")


def map_page(graph, ctx):
    S = ctx.S
    if not graph or not S:
        return page("증명 지도", "<h1>증명 지도</h1><p class=\"muted\">build/graph.json 이 없다. 먼저 extract.py 를 돌린다.</p>",
                    cur="map.html")
    text, agg, mutual = section_map(S)
    rows = []
    for sc in S.secs:
        k = sc["key"]
        rows.append("<tr><td>" + esc(S.label(k)) + "</td><td>" + esc(sc["title"]) + "</td><td>" + str(len(S.members[k]))
                    + "</td><td>" + ctx.link(sc["card"], "카드") + "</td><td><a href=\"" + map_href(k) + "\">지도</a></td></tr>")
    nodes = [n for n in graph["nodes"] if n["kind"] in C.THM_KINDS]
    secs = {n["id"]: n for n in graph["nodes"] if n["kind"] == "section"}
    nrows = []
    for n in nodes:
        s = secs.get(n["section"])
        has = ctx.link(n["id"], "카드") if n["id"] in ctx.cards else '<span class="muted">—</span>'
        nrows.append("<tr><td>" + esc(n["number"]) + "</td><td><code>" + esc(n["id"]) + "</code></td><td>"
                     + esc(f'§{s["number"]} {s["title"]}' if s else "") + "</td><td>" + esc(n.get("title") or "")
                     + "</td><td>" + has + "</td></tr>")
    if not mutual:
        note = "섹션 사이에 서로 쓰는 쌍이 없다(순환 없음)."
    else:
        note = ("서로 쓰는 섹션 쌍이 있다: " + ", ".join(S.label(a) + "–" + S.label(b) for a, b in mutual)
                + ". 서로 다른 카드 사이의 쓰임이 양쪽으로 있어서 생긴 것이고, 카드 단위로는 순환이 없다(검사 &ldquo;순환&rdquo;).")
    total = sum(len(v) for v in S.members.values())
    body = ("<h1>증명 지도</h1>"
            "<p class=\"stat\">두 단계로 본다. 이 쪽은 섹션 단위 지도이고, 섹션마다 그 안의 정리류 카드와 밖과 오가는 간선을 보이는 "
            "지도가 따로 있다(아래 표의 &ldquo;지도&rdquo;).</p>"
            "<h2>섹션 지도</h2>"
            "<p class=\"stat\">화살표는 쓰이는 쪽에서 쓰는 쪽으로 간다. 숫자는 그 방향의 <code>uses</code> 항목 수(카드 쌍 단위)다. "
            "주정리(<code>main:theorem</code>)는 진술이 §2에, 증명이 §9의 원문 줄에 있어 두 섹션 카드의 자식이므로, "
            "§2와 §8·§9가 서로 쓰는 것처럼 보이지 않게 따로 노드로 세웠다(주정리와 그 증명 단계 카드는 이 노드에만 센다). "
            + note + " 노드를 누르면 섹션 카드로 간다.</p>"
            f'<pre class="mermaid" data-map="sections">\n{esc(text)}\n</pre>'
            f"<h2>섹션별 지도와 카드 수</h2><p class=\"stat\">카드 {total}장을 한 번씩만 센다.</p>"
            '<div class="tablewrap"><table><thead><tr><th>섹션</th><th>제목</th><th>카드</th><th>섹션 카드</th><th>지도</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>"
            "<h2>원문의 정리류 노드</h2>"
            '<div class="tablewrap"><table><thead><tr><th>번호</th><th>id</th><th>섹션</th><th>제목</th><th>카드</th></tr></thead><tbody>'
            + "".join(nrows) + "</tbody></table></div>")
    return page("증명 지도", body, cur="map.html", extra_tail=MERMAID_TAIL)


def map_section_page(S, key, ctx):
    text, internal, incoming, outgoing, next_, nedges = section_detail_map(S, key)
    sc = S.by_key[key]
    head = "주정리" if key == "main" else f'§{sc["num"]} {sc["title"]}'
    rows = []
    for i in internal:
        c = S.cards[i]
        inn = ", ".join(ctx.link(x) + sec_tag(ctx, x) for x in sorted(incoming[i])) or '<span class="muted">—</span>'
        outg = ", ".join(ctx.link(x) + sec_tag(ctx, x) for x in sorted(outgoing[i])) or '<span class="muted">—</span>'
        rows.append("<tr><td>" + ctx.link(i) + "</td><td>" + esc(str(c.get("kind") or "")) + "</td><td>"
                    + esc(str(c.get("title") or "")) + "</td><td>" + inn + "</td><td>" + outg + "</td></tr>")
    body = (f'<div class="crumbs"><a href="map.html">증명 지도</a></div><h1>{esc(head)} — 지도</h1>'
            f'<p class="stat">이 섹션의 카드 {len(S.members[key])}장 가운데 증명 단계를 뺀 {len(internal)}장(파랑: 정리·명제·보조정리·따름정리, '
            "회색: 정의·약속·가정·주석)을 보인다. 화살표는 쓰이는 쪽에서 쓰는 쪽으로 간다. 실선은 섹션 안의 쓰임(다른 경로로 이어지는 간선은 줄였다), "
            f"점선은 밖의 {next_}장과의 연결이다. 밖의 카드는 섹션별로 한 노드(점선 상자)로 묶고 간선의 숫자가 그 섹션에서 오가는 카드 수다. "
            "카드 하나하나는 아래 표에 있다. 증명 단계의 <code>uses</code> 는 그 단계가 속한 카드로 올려 그리고, "
            "섹션 카드 자신의 <code>uses</code> 목록은 그리지 않는다. 노드를 누르면 카드로(밖의 노드는 그 섹션의 지도로) 간다. "
            f'섹션 카드: {ctx.link(sc["card"])}</p>'
            f'<pre class="mermaid" data-map="sec-{esc(key)}">\n{esc(text)}\n</pre>'
            "<h2>카드와 밖의 연결</h2>"
            '<div class="tablewrap"><table><thead><tr><th>카드</th><th>종류</th><th>제목</th><th>밖에서 받는 것</th>'
            "<th>밖에서 쓰는 카드</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")
    return page(f"{head} — 지도", body, cur="map.html", extra_tail=MERMAID_TAIL)


# ============================================================ 메인
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    root = C.resolve_root(args.root)
    out = Path(args.out) if args.out else root / "site"
    graph = C.load_graph()
    cards = C.load_cards(root)
    gpath = root / "layers" / "glossary.md"
    gentries, gproblems, gexists = C.parse_glossary(gpath)
    gloss = {}
    for en in gentries:
        gloss.setdefault(en.slug, en)   # 중복이면 먼저 나온 것
    ctx = Ctx(cards, graph, gloss=gloss)
    ctx.S = Struct(cards, graph)
    (out / "cards").mkdir(parents=True, exist_ok=True)
    for old in list(out.glob("*.html")) + list((out / "cards").glob("*.html")):
        old.unlink()

    written = []

    def w(rel, text):
        p = out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        written.append(rel)

    # 층 문서
    layers = {}
    for name, label in (("L0", "L0"), ("L1", "L1"), ("rules", "규칙 표")):
        p = root / "layers" / f"{name}.md"
        if p.is_file():
            body = md_html(p.read_text(encoding="utf-8"), ctx)
            layers[name] = True
        else:
            body = f"<h1>{label}</h1><p class=\"muted\">layers/{name}.md 가 아직 없다.</p>"
            layers[name] = False
        w(f"{name}.html", page(label, body, cur=f"{name}.html"))

    # 용어집
    try:
        w("glossary.html", glossary_page(gpath, gentries, gproblems, gexists, ctx))
    except Exception as ex:
        w("glossary.html", page("용어집", f"<h1>용어집</h1><p>생성 오류: {esc(repr(ex))}</p>", cur="glossary.html"))

    # 카드
    n_ok = 0
    for c in cards:
        if c.fm is None or not c.id:
            continue
        try:
            w("cards/" + page_name(c.id), card_page(c, ctx.with_base("../"), cards))
            n_ok += 1
        except Exception as ex:  # 한 카드가 망가져도 계속
            w("cards/" + page_name(c.id), page(c.id, f"<h1>{esc(c.id)}</h1><p>렌더링 오류: {esc(repr(ex))}</p>", base="../"))
    w("cards/index.html", card_index(cards, ctx.with_base("../")))

    # 지도
    try:
        w("map.html", map_page(graph, ctx))
    except Exception as ex:
        w("map.html", page("증명 지도", f"<h1>증명 지도</h1><p>생성 오류: {esc(repr(ex))}</p>", cur="map.html"))
    for sc in ctx.S.secs:
        try:
            w(map_href(sc["key"]), map_section_page(ctx.S, sc["key"], ctx))
        except Exception as ex:
            w(map_href(sc["key"]), page("지도", f"<h1>지도</h1><p>생성 오류: {esc(repr(ex))}</p>", cur="map.html"))

    # 검사 보고서
    rp = root / "build" / "check-report.md"
    if rp.is_file():
        w("check-report.html", page("검사 보고서", md_html(rp.read_text(encoding="utf-8"), ctx), cur="check-report.html"))
    else:
        w("check-report.html", page("검사 보고서", "<h1>검사 보고서</h1><p class=\"muted\">아직 만들어지지 않았다. "
                                    "<code>python3 tools/check.py</code> 를 돌린다.</p>", cur="check-report.html"))

    # 처음
    S = ctx.S
    srows = []
    for sc in S.secs:
        k = sc["key"]
        t = "Theorem 2.1 (주정리)" if k == "main" else sc["title"]
        srows.append("<tr><td>" + esc(S.label(k)) + "</td><td>" + esc(t) + "</td><td>" + str(len(S.members[k]))
                     + "</td><td>" + ctx.link(sc["card"], "섹션 카드") + f'</td><td><a href="{map_href(k)}">지도</a></td></tr>')
    total = sum(len(v) for v in S.members.values())
    idx = f"""<h1>Mézard–Parisi 공식 — 노드 카드로 다시 읽기</h1>
<p>원문은 diluted spin glass에 대한 Mézard–Parisi 위계 cavity 공식의 증명이다. 이 사이트는 그 논문을
정리·보조정리·증명 단계 단위의 <strong>노드 카드</strong>로 나누고, 물리 언어의 <strong>단면 문서</strong>(L0, L1)와 연결한 것이다.
각 카드는 받는 것과 내놓는 것을 밝히고, 펼치면 더 잘게 쪼개진 증명 단계가 나온다.</p>
<h2>위에서부터 읽기</h2>
<ul class="links">
<li><a href="L0.html">L0</a> — 한 문단: 결과와 의미{'' if layers['L0'] else ' (아직 없음)'}</li>
<li><a href="L1.html">L1</a> — 한 쪽: 번호 붙은 수의 목록{'' if layers['L1'] else ' (아직 없음)'}</li>
<li><a href="rules.html">규칙 표</a> — 물리판이 증명 없이 쓰는 명제 P1, P2, …{'' if layers['rules'] else ' (아직 없음)'}</li>
<li><a href="glossary.html">용어집</a> — 이 문서가 쓰는 용어의 뜻·역할·정의 위치{'' if gexists else ' (아직 없음)'}</li>
</ul>
<h2>섹션별로 들어가기</h2>
<p class="stat">카드 {total}장을 한 번씩만 센다. 주정리와 그 증명 단계는 진술이 §2, 증명이 §9의 원문 줄에 있어 두 섹션 카드의 자식이지만 &ldquo;주정리&rdquo; 한 묶음으로 센다. 섹션 카드에서 펼치며 내려간다.</p>
<div class="tablewrap"><table><thead><tr><th>섹션</th><th>제목</th><th>카드</th><th>들어가는 길</th><th>증명 지도</th></tr></thead><tbody>{"".join(srows)}</tbody></table></div>
<h2>그 밖</h2>
<ul class="links">
<li><a href="map.html">증명 지도</a> — 섹션 단위 지도와 섹션별 지도</li>
<li><a href="cards/index.html">카드 목록</a> — 카드 {n_ok}개 전부</li>
<li><a href="check-report.html">검사 보고서</a> — 적법성 검사 결과</li>
</ul>
<p class="stat">수식은 MathJax, 지도는 Mermaid로 그리며 둘 다 CDN에서 불러온다(인터넷 연결 필요).</p>"""
    w("index.html", page("Mézard–Parisi 노드 카드", idx, cur="index.html"))
    print(f"{len(written)}개 파일을 {out} 에 썼다 (카드 {n_ok}개).")
    for c in cards:
        if c.fm is None or not c.id:
            print(f"  건너뜀(머리말 오류): cards/{c.fname}: {'; '.join(c.errors)}")


if __name__ == "__main__":
    main()
