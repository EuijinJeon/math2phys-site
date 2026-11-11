"""check.py 와 build.py 가 공유하는 보조 코드 (표준 라이브러리 + 선택적 PyYAML)."""
import json
import os
import re
from pathlib import Path

REAL_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REAL_ROOT / "source" / "sections"
GRAPH_PATH = REAL_ROOT / "build" / "graph.json"

KINDS = {"theorem", "proposition", "lemma", "corollary", "definition", "remark",
         "assumption", "step", "device", "convention", "section"}
ABSTRACTIONS = {"exact", "weakening", "blackbox", "approximation", "intuition"}
STATUSES = {"proposed", "confirmed", "unverified"}
THM_KINDS = {"theorem", "proposition", "lemma", "corollary", "definition", "remark"}

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None


# ------------------------------------------------------------ 경로
def resolve_root(cli_root=None):
    """--root > 환경변수 M2P_ROOT > 실제 redesign/. root 는 cards/, layers/ 를 담는다."""
    r = cli_root or os.environ.get("M2P_ROOT")
    return Path(r).resolve() if r else REAL_ROOT


# ------------------------------------------------------------ 원문/그래프
_src_cache = {}


def source_lines(fname):
    """원문 줄 목록(1부터는 index+1). 없으면 None."""
    stem = Path(fname).name
    if not stem.endswith(".tex"):
        stem += ".tex"
    if stem in _src_cache:
        return _src_cache[stem]
    p = SRC_DIR / stem
    if not p.is_file():
        _src_cache[stem] = None
        return None
    txt = p.read_text(encoding="utf-8").split("\n")
    if txt and txt[-1] == "":
        txt.pop()
    _src_cache[stem] = txt
    return txt


def norm_file(f):
    s = Path(str(f)).name
    return s if s.endswith(".tex") else s + ".tex"


def load_graph():
    if not GRAPH_PATH.is_file():
        return None
    return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))


def strip_comment(line):
    i = 0
    while i < len(line):
        if line[i] == "\\":
            i += 2
            continue
        if line[i] == "%":
            return line[:i]
        i += 1
    return line


# ------------------------------------------------------------ 최소 YAML (PyYAML 없을 때)
def _parse_flow(s, i=0):
    """flow 값 하나를 읽어 (값, 다음 위치)."""
    n = len(s)
    while i < n and s[i] in " \t":
        i += 1
    if i >= n:
        return None, i
    c = s[i]
    if c == "[":
        out = []
        i += 1
        while True:
            while i < n and s[i] in " \t,":
                i += 1
            if i >= n:
                raise ValueError("unterminated [")
            if s[i] == "]":
                return out, i + 1
            v, i = _parse_flow(s, i)
            out.append(v)
    if c == "{":
        out = {}
        i += 1
        while True:
            while i < n and s[i] in " \t,":
                i += 1
            if i >= n:
                raise ValueError("unterminated {")
            if s[i] == "}":
                return out, i + 1
            m = re.compile(r"\s*([^:,{}\[\]]+?)\s*:\s*").match(s, i)
            if not m:
                raise ValueError("bad map key")
            v, i = _parse_flow(s, m.end())
            out[m.group(1).strip().strip("'\"")] = v
    if c in "\"'":
        j = i + 1
        while j < n and s[j] != c:
            j += 2 if s[j] == "\\" else 1
        return s[i + 1:j], j + 1
    j = i
    while j < n and s[j] not in ",]}":
        j += 1
    return _scalar(s[i:j].strip()), j


def _scalar(t):
    if t in ("null", "~", ""):
        return None
    if t in ("true", "True"):
        return True
    if t in ("false", "False"):
        return False
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    if re.fullmatch(r"-?\d+\.\d*", t):
        return float(t)
    if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'":
        return t[1:-1]
    return t


def mini_yaml(text):
    lines = text.split("\n")
    out = {}
    i = 0
    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.lstrip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", l)
        if not m:
            raise ValueError(f"cannot parse line: {l!r}")
        key, rest = m.group(1), m.group(2)
        rest_nc = re.sub(r"\s+#.*$", "", rest) if not rest.startswith(('"', "'", "|", ">")) else rest
        if rest_nc.strip() in ("|", ">", "|-", ">-"):
            buf = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                buf.append(lines[i])
                i += 1
            ind = min((len(b) - len(b.lstrip()) for b in buf if b.strip()), default=0)
            body = [b[ind:] for b in buf]
            while body and not body[-1].strip():
                body.pop()
            out[key] = ("\n".join(body) + "\n") if rest_nc.strip()[0] == "|" else " ".join(x.strip() for x in body)
            continue
        if rest_nc.strip() == "":
            # 블록 시퀀스 또는 null
            items = []
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or re.match(r"^\s+-\s", lines[j]) or re.match(r"^-\s", lines[j])):
                if lines[j].strip():
                    v, _ = _parse_flow(re.sub(r"^\s*-\s*", "", lines[j]))
                    items.append(v)
                j += 1
            out[key] = items if items else None
            i = j
            continue
        v, _ = _parse_flow(rest_nc)
        out[key] = v
        i += 1
    return out


def parse_yaml(text):
    if yaml is not None:
        return yaml.safe_load(text)
    return mini_yaml(text)


# ------------------------------------------------------------ 카드
class Card:
    def __init__(self, path):
        self.path = path
        self.fname = path.name
        self.fm = None
        self.body = ""
        self.errors = []     # 형식 오류 (front matter 자체)
        self.id = None
        self.uses = []
        self.children = []
        self.source = []     # [(file, a, b)]
        self.source_errors = []

    def get(self, key, default=None):
        return (self.fm or {}).get(key, default)


def split_front_matter(text):
    if not text.startswith("---"):
        return None, text, "머리말(---)이 없다"
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None, text, "첫 줄이 ---가 아니다"
    for k in range(1, len(lines)):
        if lines[k].strip() == "---":
            return "\n".join(lines[1:k]), "\n".join(lines[k + 1:]), None
    return None, text, "머리말을 닫는 ---가 없다"


def as_list(v):
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return list(v)
    return [v]


def load_cards(root):
    cards = []
    cdir = Path(root) / "cards"
    if not cdir.is_dir():
        return cards
    for p in sorted(cdir.glob("*.md")):
        c = Card(p)
        try:
            text = p.read_text(encoding="utf-8")
        except Exception as ex:
            c.errors.append(f"읽기 실패: {ex}")
            cards.append(c)
            continue
        fm_text, body, err = split_front_matter(text)
        c.body = body
        if err:
            c.errors.append(err)
            cards.append(c)
            continue
        try:
            fm = parse_yaml(fm_text)
        except Exception as ex:
            c.errors.append(f"YAML 오류: {str(ex).splitlines()[0] if str(ex) else ex}")
            cards.append(c)
            continue
        if not isinstance(fm, dict):
            c.errors.append("머리말이 key: value 매핑이 아니다")
            cards.append(c)
            continue
        c.fm = fm
        cid = fm.get("id")
        if not isinstance(cid, str) or not cid.strip():
            c.errors.append("id가 없거나 문자열이 아니다")
        else:
            c.id = cid.strip()
            exp = c.id.replace(":", ".") + ".md"
            if exp != p.name:
                c.errors.append(f"파일 이름이 id와 맞지 않는다(기대: {exp})")
        c.uses = [str(x) for x in as_list(fm.get("uses"))]
        c.children = [str(x) for x in as_list(fm.get("children"))]
        # source
        src = fm.get("source")
        if src is None or src == []:
            c.source_errors.append("source가 없다")
        elif not isinstance(src, list):
            c.source_errors.append("source가 목록이 아니다")
        else:
            for k, ent in enumerate(src):
                if not isinstance(ent, dict) or "file" not in ent or "lines" not in ent:
                    c.source_errors.append(f"source[{k}]에 file/lines가 없다")
                    continue
                ln = ent["lines"]
                if (not isinstance(ln, (list, tuple)) or len(ln) != 2
                        or not all(isinstance(x, int) and not isinstance(x, bool) for x in ln)):
                    c.source_errors.append(f"source[{k}].lines가 [시작, 끝] 정수 쌍이 아니다")
                    continue
                f = norm_file(ent["file"])
                a, b = ln
                srcl = source_lines(f)
                if srcl is None:
                    c.source_errors.append(f"source[{k}]: 원문 파일 {f} 가 없다")
                    continue
                if not (1 <= a <= b <= len(srcl)):
                    c.source_errors.append(f"source[{k}]: {f}:{a}-{b} 가 파일 범위(1-{len(srcl)}) 밖이다")
                    continue
                c.source.append((f, a, b))
        cards.append(c)
    return cards


WIKI = re.compile(r"\[\[([^\]\n]+?)\]\]")


def wiki_ids(text):
    """[[id]] 의 노드 ID 들. 용어집 링크 [[g:slug]] 는 노드가 아니므로 뺀다."""
    ids = [m.group(1).split("|")[0].strip() for m in WIKI.finditer(text or "")]
    return [i for i in ids if not i.startswith("g:")]


# ------------------------------------------------------------ 규칙 표
def parse_rules(path):
    """layers/rules.md 의 첫 규칙 표를 읽는다. 반환: 행 목록 (없으면 None)."""
    p = Path(path)
    if not p.is_file():
        return None
    lines = p.read_text(encoding="utf-8").split("\n")
    rows = []
    header = None
    for idx, l in enumerate(lines):
        if not l.strip().startswith("|"):
            if header and rows:
                break
            continue
        cells = split_row(l)
        if header is None:
            if cells and cells[0].strip().lower() == "rule":
                header = [c.strip() for c in cells]
            continue
        if all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in cells if c.strip()):
            continue
        d = {header[k]: (cells[k].strip() if k < len(cells) else "") for k in range(len(header))}
        d["_line"] = idx + 1
        rows.append(d)
    return rows


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells = []
    cur = []
    depth = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch in "`$":
            depth ^= 1
        if ch == "|" and not depth:
            cells.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


def rule_nodes(cell):
    ids = []
    for part in re.split(r"[,\s]+", cell.replace("`", "")):
        part = part.strip().strip("[]")
        if part and part not in ("-", "—", "null", "없음"):
            ids.append(part)
    return ids


def is_null(v):
    return v is None or (isinstance(v, str) and v.strip().lower() in ("", "null", "~", "none"))


# ------------------------------------------------------------ 용어집
GLINK = re.compile(r"\[\[g:([^\]|\n]*?)(?:\|([^\]\n]*))?\]\]")
GSLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
GFIELDS = ("기호", "뜻", "역할", "정의 위치", "물리 대응", "쓰지 않는 뜻")
_GHEAD = re.compile(r"^###\s+g:([^\s—–]*)\s*(?:[—–]|--|-)\s*(.*?)\s*#*\s*$")
_GFIELD = re.compile(r"^\s*[-*+]\s+\*\*([^*]+?)\*\*\s*[:：]\s*(.*)$")


class GlossEntry:
    def __init__(self, slug, headword, group, line):
        self.slug = slug
        self.headword = headword
        self.group = group
        self.line = line
        self.fields = {}      # 칸 이름 → 문자열 (여러 줄이면 \n 으로 잇는다)
        self.field_lines = {}

    def get(self, name):
        return (self.fields.get(name) or "").strip()


def parse_glossary(path):
    """layers/glossary.md 를 읽는다. 반환: (entries, problems, exists).

    entries : [GlossEntry] (문서 순서). 슬러그가 겹쳐도 모두 담는다.
    problems: [(줄, 메시지)]  형식이 깨진 제목·칸. 죽지 않고 모아서 돌려준다.
    exists  : 파일이 있는가.
    """
    p = Path(path)
    if not p.is_file():
        return [], [], False
    try:
        lines = p.read_text(encoding="utf-8").split("\n")
    except Exception as ex:
        return [], [(0, f"읽기 실패: {ex}")], True
    entries, problems = [], []
    group = ""
    cur = None
    curfield = None
    in_fence = False
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.match(r"^##\s+", l) and not l.startswith("###"):
            group = re.sub(r"\s*#*\s*$", "", l[2:].strip())
            cur = curfield = None
            continue
        if l.startswith("###"):
            cur = curfield = None
            m = _GHEAD.match(l)
            if not m:
                problems.append((i, f"항목 제목 형식이 아니다(`### g:<slug> — 표제어`): {l.strip()[:60]}"))
                continue
            slug, head = m.group(1), m.group(2)
            if not slug or not GSLUG.fullmatch(slug):
                problems.append((i, f"slug `{slug}` 는 영문 소문자·숫자·하이픈이어야 한다"))
                continue
            if not head:
                problems.append((i, f"`g:{slug}` 표제어가 비었다"))
            cur = GlossEntry(slug, head or slug, group, i)
            entries.append(cur)
            continue
        if cur is None:
            continue
        m = _GFIELD.match(l)
        if m:
            name = m.group(1).strip()
            if name not in GFIELDS:
                problems.append((i, f"`g:{cur.slug}`: 알 수 없는 칸 `{name}`"))
            if name in cur.fields:
                problems.append((i, f"`g:{cur.slug}`: 칸 `{name}` 가 두 번 나온다"))
            cur.fields[name] = m.group(2).strip()
            cur.field_lines[name] = i
            curfield = name
            continue
        if not l.strip():
            continue
        if re.match(r"^#{1,6}\s", l):
            cur = curfield = None
            continue
        if curfield is not None and l.startswith((" ", "\t")):
            cur.fields[curfield] += "\n" + l.strip()   # 칸의 이어지는 줄
        else:
            problems.append((i, f"`g:{cur.slug}`: 칸이 아닌 줄: {l.strip()[:50]}"))
    return entries, problems, True


def mask_code(text):
    """코드 블록·인라인 코드를 같은 길이의 공백으로 가린다 (줄 번호 보존)."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"(?m)^[ \t]*```[^\n]*\n.*?^[ \t]*```[ \t]*$", blank, text, flags=re.S)
    return re.sub(r"(`+)(.+?)\1", blank, text)


def mask_math(text):
    """수식($..$, $$..$$, \\[..\\], \\(..\\))을 공백으로 가린다 (줄 번호 보존)."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"\$\$.+?\$\$", blank, text, flags=re.S)
    text = re.sub(r"\\\[.+?\\\]", blank, text, flags=re.S)
    text = re.sub(r"\\\(.+?\\\)", blank, text, flags=re.S)
    text = re.sub(r"(?<![\\$])\$(?![\s$])((?:\\.|[^$\\\n]|\n(?![ \t]*\n))+?)(?<![\s\\])\$(?!\$)", blank, text)
    return text


def mask_code_math(text):
    return mask_math(mask_code(text))


def glossary_links(text):
    """코드 밖에서 [[g:slug]] 를 찾는다. 반환: [(줄, slug)]."""
    t = mask_code(text or "")
    out = []
    for m in GLINK.finditer(t):
        out.append((t.count("\n", 0, m.start()) + 1, m.group(1).strip()))
    return out


# 역할 번호 R1–R22: 수식·코드 밖의 맨 토큰 R + 숫자 1–2자리
ROLE_REF = re.compile(r"(?<![A-Za-z0-9_\\:/#])R(\d{1,2})(?![A-Za-z0-9_^{(])")


def role_refs(text):
    """역할 번호 참조를 찾는다. 반환: [(줄, 'R5')]. 수식·코드·인라인 코드는 먼저 가린다."""
    t = mask_code_math(text or "")
    out = []
    for m in ROLE_REF.finditer(t):
        if 1 <= int(m.group(1)) <= 22:
            out.append((t.count("\n", 0, m.start()) + 1, "R" + m.group(1)))
    return out


def plain_text(s, limit=200):
    """툴팁용: 줄바꿈·markdown 강조를 걷어낸 평문 (수식은 TeX 원문 그대로), limit 자로 자른다."""
    s = re.sub(r"\[\[g:([^\]|\n]*?)(?:\|([^\]\n]*))?\]\]", lambda m: (m.group(2) or m.group(1)), s or "")
    s = re.sub(r"\[\[([^\]|\n]*?)(?:\|([^\]\n]*))?\]\]", lambda m: (m.group(2) or m.group(1)), s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = s.replace("`", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= limit else s[:limit - 1].rstrip() + "…"
