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
.stat{color:var(--muted);font-size:.9rem}
mjx-container[display=true]{overflow-x:auto;overflow-y:hidden;max-width:100%}
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

    def __init__(self, cards, graph, base=""):
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
            return self.stash(self.ctx.link(nid, lab.strip() or None))
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
       ("map.html", "증명 지도"), ("cards/index.html", "카드 목록"), ("check-report.html", "검사 보고서")]


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
        li.append("<li>" + ctx.link(u) + num + t + "</li>")
    return "<ul>" + "".join(li) + "</ul>"


def used_by(c, ctx, allc):
    users = sorted(x.id for x in allc if x.id and x.fm is not None and c.id in x.uses and x.id != c.id)
    if not users:
        return '<span class="muted">(이 카드를 쓰는 카드 없음)</span>'
    return "<ul>" + "".join("<li>" + ctx.link(u) + "</li>" for u in users) + "</ul>"


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


def card_page(c, ctx, allc):
    n = ctx.nodes.get(c.id)
    num = n.get("number") if n else None
    title = str(c.get("title") or c.id)
    head = f'<div class="crumbs"><a href="index.html">카드 목록</a>'
    parents = sorted(x.id for x in allc if x.id and x.fm is not None and c.id in x.children)
    if parents:
        head += " · 상위: " + ", ".join(ctx.link(p) for p in parents)
    head += "</div>"
    h1 = f"<h1>{esc(num + ' ' if num else '')}{esc(title)}</h1>"
    badges = (f'<span class="badge">{esc(str(c.get("kind") or "?"))}</span>'
              f'<span class="badge {esc(str(c.get("status") or ""))}">{esc(str(c.get("status") or "상태 없음"))}</span>'
              f' <code>{esc(c.id)}</code>')
    body = head + h1 + "<p>" + badges + "</p>"
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
            rows.append(f'<tr><td colspan="6"><span style="color:var(--bad)">머리말 오류</span> '
                        f'<code>{esc(c.fname)}</code>: {esc("; ".join(c.errors))}</td></tr>')
            continue
        n = ctx.nodes.get(c.id)
        rows.append("<tr><td>" + esc(n["number"] if n and n.get("number") else "") + "</td><td>"
                    + ctx.link(c.id) + "</td><td>" + esc(str(c.get("kind") or "")) + "</td><td>"
                    + esc(str(c.get("title") or "")) + "</td><td>" + esc(str(c.get("abstraction") or "")) + "</td><td>"
                    + esc(str(c.get("status") or "")) + "</td></tr>")
    if not rows:
        t = "<p class=\"muted\">아직 카드가 없다.</p>"
    else:
        t = ('<div class="tablewrap"><table><thead><tr><th>번호</th><th>id</th><th>종류</th><th>제목</th><th>축약</th>'
             "<th>상태</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")
    return page("카드 목록", f"<h1>카드 목록</h1><p class=\"stat\">{len(cards)}개</p>" + t, base="../",
                cur="cards/index.html")


# ============================================================ 지도
def mermaid_text(s, limit=34):
    s = re.sub(r"\$([^$]*)\$", r"\1", s or "")
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = re.sub(r"[{}\\\[\]\"<>|`#&;]", "", s)
    s = s.replace("--", "–").replace("~", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= limit else s[:limit - 1] + "…"


def map_page(graph, ctx):
    if not graph:
        return page("증명 지도", "<h1>증명 지도</h1><p class=\"muted\">build/graph.json 이 없다. 먼저 extract.py 를 돌린다.</p>",
                    cur="map.html")
    nodes = [n for n in graph["nodes"] if n["kind"] in C.THM_KINDS]
    secs = {n["id"]: n for n in graph["nodes"] if n["kind"] == "section"}
    mid = {n["id"]: f"n{k}" for k, n in enumerate(nodes)}
    by_sec = {}
    for n in nodes:
        by_sec.setdefault(n["section"], []).append(n)
    L = ["flowchart LR"]
    sec_order = [s for s in secs if s in by_sec]
    for si, sid in enumerate(sec_order):
        s = secs[sid]
        L.append(f'  subgraph S{si}["§{s["number"]} {mermaid_text(s["title"], 40)}"]')
        for n in by_sec[sid]:
            short = n.get("title") or n["id"].split(":", 1)[-1]
            lab = f'{n["number"]}<br/>{mermaid_text(short)}'
            L.append(f'    {mid[n["id"]]}["{lab}"]')
        L.append("  end")
    agg = {}
    for e in graph["edges"]:
        if e.get("role") not in ("statement", "proof") or not e.get("resolved"):
            continue
        s, d = e["src"], e.get("dst_container")
        if s not in mid or d not in mid or s == d:
            continue
        key = (d, s)
        agg[key] = agg.get(key, False) or e["role"] == "proof"
    for (d, s), proof in sorted(agg.items()):
        L.append(f'  {mid[d]} {"-->" if proof else "-.->"} {mid[s]}')
    cardnodes = [mid[n["id"]] for n in nodes if n["id"] in ctx.cards]
    nocard = [mid[n["id"]] for n in nodes if n["id"] not in ctx.cards]
    L.append("  classDef hascard fill:#d6e6ff,stroke:#1f5fbf,color:#111;")
    L.append("  classDef nocard fill:#f3f3f0,stroke:#999,color:#333;")
    if cardnodes:
        L.append("  class " + ",".join(cardnodes) + " hascard;")
    if nocard:
        L.append("  class " + ",".join(nocard) + " nocard;")
    for n in nodes:
        if n["id"] in ctx.cards:
            L.append(f'  click {mid[n["id"]]} "cards/{page_name(n["id"])}"')
    diagram = "\n".join(L)

    rows = []
    for n in nodes:
        s = secs.get(n["section"])
        has = ctx.link(n["id"], "카드") if n["id"] in ctx.cards else '<span class="muted">—</span>'
        rows.append("<tr><td>" + esc(n["number"]) + "</td><td><code>" + esc(n["id"]) + "</code></td><td>"
                    + esc(f'§{s["number"]} {s["title"]}' if s else "") + "</td><td>" + esc(n.get("title") or "")
                    + "</td><td>" + has + "</td></tr>")
    body = ("<h1>증명 지도</h1>"
            "<p class=\"stat\">화살표는 쓰이는 쪽에서 쓰는 쪽으로 간다 (보조정리 → 그것을 인용하는 정리). "
            "실선은 증명 안의 인용, 점선은 진술 안의 인용이다. 파란 노드는 카드가 있고, 누르면 카드로 간다.</p>"
            f'<pre class="mermaid">\n{esc(diagram)}\n</pre>'
            "<h2>노드 표</h2>"
            '<div class="tablewrap"><table><thead><tr><th>번호</th><th>id</th><th>섹션</th><th>제목</th><th>카드</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")
    tail = (f'<script src="{MERMAID}"></script>\n'
            "<script>if(window.mermaid){mermaid.initialize({startOnLoad:true,securityLevel:'loose',"
            "flowchart:{useMaxWidth:true,htmlLabels:true}});}</script>")
    return page("증명 지도", body, cur="map.html", extra_tail=tail)


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
    ctx = Ctx(cards, graph)
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

    # 검사 보고서
    rp = root / "build" / "check-report.md"
    if rp.is_file():
        w("check-report.html", page("검사 보고서", md_html(rp.read_text(encoding="utf-8"), ctx), cur="check-report.html"))
    else:
        w("check-report.html", page("검사 보고서", "<h1>검사 보고서</h1><p class=\"muted\">아직 만들어지지 않았다. "
                                    "<code>python3 tools/check.py</code> 를 돌린다.</p>", cur="check-report.html"))

    # 처음
    nn = len([n for n in graph["nodes"] if n["kind"] in C.THM_KINDS]) if graph else 0
    idx = f"""<h1>Mézard–Parisi 공식 — 노드 카드로 다시 읽기</h1>
<p>원문은 diluted spin glass에 대한 Mézard–Parisi 위계 cavity 공식의 증명이다. 이 사이트는 그 논문을
정리·보조정리·증명 단계 단위의 <strong>노드 카드</strong>로 나누고, 물리 언어의 <strong>단면 문서</strong>(L0, L1)와 연결한 것이다.
각 카드는 받는 것과 내놓는 것을 밝히고, 펼치면 더 잘게 쪼개진 증명 단계가 나온다.</p>
<ul class="links">
<li><a href="L0.html">L0</a> — 한 문단: 결과와 의미{'' if layers['L0'] else ' (아직 없음)'}</li>
<li><a href="L1.html">L1</a> — 한 쪽: 번호 붙은 수의 목록{'' if layers['L1'] else ' (아직 없음)'}</li>
<li><a href="rules.html">규칙 표</a> — 물리판이 증명 없이 쓰는 명제 P1, P2, …{'' if layers['rules'] else ' (아직 없음)'}</li>
<li><a href="map.html">증명 지도</a> — 정리류 노드 {nn}개의 의존 그래프</li>
<li><a href="cards/index.html">카드 목록</a> — 카드 {n_ok}개</li>
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
