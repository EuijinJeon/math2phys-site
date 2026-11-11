#!/usr/bin/env python3
"""LaTeX 원문에서 노드/간선/문장을 추출한다.

출력: build/graph.json, build/sentences.json
사용: python3 tools/extract.py
"""
import bisect
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source"
BUILD = ROOT / "build"

THM_ENVS = {
    "theorem": "Theorem",
    "proposition": "Proposition",
    "lemma": "Lemma",
    "corollary": "Corollary",
    "definition": "Definition",
    "remark": "Remark",
}
NUMBERED_DISPLAY = {"equation", "align", "gather", "multline", "eqnarray", "flalign", "alignat"}
ROWWISE = {"align", "gather", "eqnarray", "flalign", "alignat"}
MATH_ENVS = NUMBERED_DISPLAY | {e + "*" for e in NUMBERED_DISPLAY} | {"displaymath", "math"}
PROOF_OWNERS = {"theorem", "proposition", "lemma", "corollary"}


# ---------------------------------------------------------------- 보조 함수
def strip_comments(line):
    """% 이후를 지운다(\\% 는 제외)."""
    i = 0
    n = len(line)
    while i < n:
        c = line[i]
        if c == "\\":
            i += 2
            continue
        if c == "%":
            return line[:i]
        i += 1
    return line


def read_balanced(text, pos, open_c, close_c):
    """text[pos]==open_c 라고 가정하고 짝이 맞는 닫는 위치 다음 인덱스를 돌려준다."""
    depth = 0
    i = pos
    n = len(text)
    while i < n:
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == open_c:
            depth += 1
        elif c == close_c:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return n


def skip_ws(text, pos):
    while pos < len(text) and text[pos] in " \t\r\n":
        pos += 1
    return pos


def plain(s):
    s = re.sub(r"\\(?:emph|textit|textbf|textup|text)\{([^{}]*)\}", r"\1", s)
    s = s.replace("~", " ")
    return re.sub(r"\s+", " ", s).strip()


TOK = re.compile(
    r"""
    \\(?P<sec>section|subsection|subsubsection)\*?(?![A-Za-z])
  | \\begin\{(?P<b>[A-Za-z]+\*?)\}
  | \\end\{(?P<e>[A-Za-z]+\*?)\}
  | \\label(?:\[[^\]]*\])?\{(?P<label>[^}]*)\}
  | \\(?P<refcmd>eqref|cref|Cref|autoref|ref)\s*\{(?P<refs>[^}]*)\}
  | \\cite[a-zA-Z]*\s*(?:\[[^\]]*\]\s*)*\{(?P<cites>[^}]*)\}
  | \\(?P<notag>notag|nonumber)(?![A-Za-z])
  | \\tag\*?\{(?P<tag>[^}]*)\}
  | (?P<rowsep>\\\\)
  | \\(?P<item>item)(?![A-Za-z])
    """,
    re.X,
)
LABEL_AT = re.compile(r"\s*\\label(?:\[[^\]]*\])?\{([^}]*)\}")
REF_IN = re.compile(r"\\(?:eq|c|C|auto)?ref\s*\{([^}]*)\}")


class Src:
    def __init__(self, path):
        self.path = path
        self.stem = path.stem
        self.name = path.name
        self.raw = path.read_text(encoding="utf-8").split("\n")
        if self.raw and self.raw[-1] == "":
            self.raw.pop()
        self.clean = [strip_comments(l) for l in self.raw]
        self.text = "\n".join(self.clean)
        self.starts = []
        off = 0
        for l in self.clean:
            self.starts.append(off)
            off += len(l) + 1

    def line(self, off):
        return bisect.bisect_right(self.starts, off)  # 1-based

    @property
    def nlines(self):
        return len(self.raw)


def section_files():
    main = (SRC / "main.tex").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"^[^%\n]*\\input\{sections/([^}]+)\}", main, re.M):
        out.append(m.group(1))
    return out


# ---------------------------------------------------------------- 구조 추출
class Extractor:
    def __init__(self):
        self.nodes = []
        self.by_id = {}
        self.edges = []
        self.cites = []
        self.labels = {}  # label -> node id (자기 자신 또는 label 노드)
        self.sec = 0
        self.sub = 0
        self.thm = 0
        self.eq = 0
        self.fig = 0
        self.sec_id = None
        self.sub_id = None
        self.proofs = []
        self.last_thm = None  # 증명 연결 후보
        self.sec_info = []  # 섹션 헤더 위치(문장 분할용)

    def add(self, node):
        base = node["id"]
        if base in self.by_id:  # 라벨 중복 방지
            k = 2
            while f"{base}#{k}" in self.by_id:
                k += 1
            node["id"] = f"{base}#{k}"
            node["duplicate_of"] = base
        self.by_id[node["id"]] = node
        self.nodes.append(node)
        return node

    # ----- 한 파일
    def run_file(self, src):
        T = src.text
        stem = src.stem
        stack = []  # 프레임
        pos = 0
        sec_range_start = None
        cur_sec_node = None
        cur_sub_node = None
        # 이어지는 섹션이 파일 경계를 넘는 경우를 위해 현재 섹션 노드의 범위를 파일별로 기록
        if self.sec_id:
            cur_sec_node = self.by_id[self.sec_id]
            cur_sec_node["ranges"].append({"file": src.name, "lines": [1, src.nlines]})
            self._cur_sec_range = cur_sec_node["ranges"][-1]
        else:
            self._cur_sec_range = None
        if self.sub_id:
            cur_sub_node = self.by_id[self.sub_id]
            cur_sub_node["ranges"].append({"file": src.name, "lines": [1, src.nlines]})
            self._cur_sub_range = cur_sub_node["ranges"][-1]
        else:
            self._cur_sub_range = None

        def top_frames():
            return stack[-1] if stack else None

        def enclosing():
            """(node_id, role) of innermost statement/proof context."""
            for fr in reversed(stack):
                if fr["env"] in THM_ENVS:
                    return fr["node"], "statement"
                if fr["env"] == "proof":
                    return fr["node"], "proof"
            return None, "text"

        def container_id():
            return self.sub_id or self.sec_id

        def finalize_row(fr, endpos):
            row = fr["row"]
            content = T[row["start"]:endpos]
            content = re.sub(r"\\label(?:\[[^\]]*\])?\{[^}]*\}|\\notag|\\nonumber|\\tag\*?\{[^}]*\}", "", content)
            has_content = bool(content.strip())
            if fr["env"].endswith("*"):
                numbered = False
            else:
                numbered = has_content and not row["notag"]
            number = None
            if row["tag"] is not None:
                number = f"({row['tag']})"
            elif numbered:
                self.eq += 1
                number = f"({self.sec}.{self.eq})"
            for (lab, off) in row["labels"]:
                self.register_equation(src, lab, off, number, fr, stack)
            fr["row"] = {"start": endpos, "labels": [], "notag": False, "tag": None}

        while True:
            m = TOK.search(T, pos)
            if not m:
                break
            pos = m.end()
            off = m.start()
            line = src.line(off)

            if m.group("sec"):
                kind = m.group("sec")
                p = skip_ws(T, pos)
                if p < len(T) and T[p] == "[":
                    p = read_balanced(T, p, "[", "]")
                    p = skip_ws(T, p)
                title = ""
                if p < len(T) and T[p] == "{":
                    e = read_balanced(T, p, "{", "}")
                    title = plain(T[p + 1:e - 1])
                    p = e
                lm = LABEL_AT.match(T, p)
                label = None
                if lm and "\n\n" not in T[p:lm.start() + 1]:
                    label = lm.group(1)
                    p = lm.end()
                pos = p
                if kind == "subsubsection":
                    continue
                # 이전 (부)섹션 범위 닫기
                if kind == "section":
                    self._close_ranges(src, line, sub=True, sec=True)
                    self.sec += 1
                    self.sub = 0
                    self.thm = 0
                    self.eq = 0
                    number = str(self.sec)
                    nid = label or f"x:{stem}-L{line}"
                    node = self.add({
                        "id": nid, "kind": "section", "number": number, "title": title,
                        "label": label, "file": src.name, "lines": [line, src.nlines],
                        "ranges": [{"file": src.name, "lines": [line, src.nlines]}],
                        "parent": None,
                    })
                    self.sec_id = node["id"]
                    self.sub_id = None
                    self._cur_sec_range = node["ranges"][-1]
                    self._cur_sub_range = None
                    self.sec_info.append({"file": src.name, "line": line, "kind": "section",
                                          "number": number, "id": node["id"]})
                else:
                    self._close_ranges(src, line, sub=True, sec=False)
                    self.sub += 1
                    number = f"{self.sec}.{self.sub}"
                    nid = label or f"x:{stem}-L{line}"
                    node = self.add({
                        "id": nid, "kind": "subsection", "number": number, "title": title,
                        "label": label, "file": src.name, "lines": [line, src.nlines],
                        "ranges": [{"file": src.name, "lines": [line, src.nlines]}],
                        "parent": self.sec_id,
                    })
                    self.sub_id = node["id"]
                    self._cur_sub_range = node["ranges"][-1]
                    self.sec_info.append({"file": src.name, "line": line, "kind": "subsection",
                                          "number": number, "id": node["id"]})
                if label:
                    self.labels[label] = node["id"]
                continue

            if m.group("b"):
                env = m.group("b")
                fr = {"env": env, "line": line, "off": off, "node": None, "label_taken": False}
                if env in THM_ENVS:
                    self.thm += 1
                    p = skip_ws(T, pos)
                    title = None
                    if p < len(T) and T[p] == "[":
                        e = read_balanced(T, p, "[", "]")
                        title = plain(T[p + 1:e - 1])
                        pos = e
                    node = {
                        "id": f"x:{stem}-L{line}", "kind": env,
                        "number": f"{THM_ENVS[env]} {self.sec}.{self.thm}",
                        "title": title, "label": None, "file": src.name,
                        "lines": [line, line], "proof": None, "proofs": [],
                        "section": self.sec_id, "subsection": self.sub_id,
                        "cites": [],
                    }
                    fr["node"] = node
                    fr["pending_node"] = node  # id 는 라벨을 보고 확정
                    stack.append(fr)
                    continue
                if env == "proof":
                    p = skip_ws(T, pos)
                    opt = None
                    if p < len(T) and T[p] == "[":
                        e = read_balanced(T, p, "[", "]")
                        opt = T[p + 1:e - 1]
                        pos = e
                    target = None
                    if opt:
                        for rm in REF_IN.finditer(opt):
                            for lab in rm.group(1).split(","):
                                lab = lab.strip()
                                tid = self.labels.get(lab)
                                if tid and self.by_id[tid]["kind"] in THM_ENVS:
                                    target = tid
                                    break
                            if target:
                                break
                    if target is None and self.last_thm and self.by_id[self.last_thm]["kind"] in PROOF_OWNERS \
                            and self.by_id[self.last_thm]["file"] == src.name:
                        target = self.last_thm
                    fr["node"] = target
                    fr["opt"] = opt
                    fr["opt_end"] = pos
                    fr["opt_start"] = off
                    stack.append(fr)
                    continue
                if env in MATH_ENVS:
                    fr["row"] = {"start": pos, "labels": [], "notag": False, "tag": None}
                    stack.append(fr)
                    continue
                if env == "figure" or env == "figure*":
                    self.fig += 1
                    fr["num"] = self.fig
                if env == "enumerate" or env == "itemize":
                    fr["items"] = 0
                    p = skip_ws(T, pos)
                    if p < len(T) and T[p] == "[":
                        pos = read_balanced(T, p, "[", "]")
                stack.append(fr)
                continue

            if m.group("e"):
                env = m.group("e")
                # 짝 찾기
                idx = None
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k]["env"] == env:
                        idx = k
                        break
                if idx is None:
                    continue
                fr = stack[idx]
                del stack[idx + 1:]
                if env in MATH_ENVS:
                    if env.rstrip("*") in ROWWISE:
                        finalize_row(fr, off)
                    else:
                        finalize_row(fr, off)
                if env in THM_ENVS:
                    node = fr["node"]
                    node["lines"] = [fr["line"], line]
                    self._finish_thm(node)
                if env == "proof":
                    rng = {"file": src.name, "lines": [fr["line"], line]}
                    tid = fr["node"]
                    if tid:
                        self.by_id[tid]["proofs"].append(rng)
                        if self.by_id[tid]["proof"] is None:
                            self.by_id[tid]["proof"] = rng
                    self.proofs.append({"node": tid, **rng})
                if env == "figure" or env == "figure*":
                    pass
                stack.pop()
                continue

            if m.group("label") is not None:
                lab = m.group("label").strip()
                top = stack[-1] if stack else None
                if top and top["env"] in THM_ENVS and not top["label_taken"]:
                    top["label_taken"] = True
                    node = top["node"]
                    node["label"] = lab
                    self._rename(node, lab)
                    self.labels[lab] = node["id"]
                    continue
                if top and top["env"] in MATH_ENVS:
                    top["row"]["labels"].append((lab, off))
                    continue
                # 일반 라벨 (그림, 항목, 기타)
                encl, role = enclosing()
                if top and top["env"].rstrip("*") == "figure":
                    kind, number = "figure", f"Figure {top['num']}"
                elif top and top["env"] in ("enumerate", "itemize"):
                    kind, number = "item", f"item {top['items']}"
                else:
                    kind, number = "label", None
                node = self.add({
                    "id": lab, "kind": kind, "number": number, "label": lab,
                    "file": src.name, "line": line, "node": encl, "role": role,
                    "container": encl or container_id(),
                    "section": self.sec_id, "subsection": self.sub_id,
                })
                self.labels[lab] = node["id"]
                continue

            if m.group("refcmd"):
                encl, role = enclosing()
                if role == "proof" and encl is None:
                    pass
                # 증명 머리말 [Proof of \cref{...}] 안의 ref 는 건너뛴다
                skip = False
                for fr in stack:
                    if fr["env"] == "proof" and fr.get("opt") is not None and \
                            fr["opt_start"] <= off < fr["opt_end"]:
                        skip = True
                if skip:
                    continue
                src_id = encl or container_id()
                for lab in m.group("refs").split(","):
                    lab = lab.strip()
                    if not lab:
                        continue
                    self.edges.append({
                        "src": src_id, "dst": lab, "cmd": m.group("refcmd"),
                        "role": role, "file": src.name, "line": line,
                        "section": self.sec_id, "subsection": self.sub_id,
                    })
                continue

            if m.group("cites") is not None:
                encl, role = enclosing()
                src_id = encl or container_id()
                for key in m.group("cites").split(","):
                    key = key.strip()
                    if key:
                        self.cites.append({
                            "src": src_id, "key": key, "role": role,
                            "file": src.name, "line": line,
                        })
                continue

            if m.group("notag"):
                top = stack[-1] if stack else None
                if top and top["env"] in MATH_ENVS:
                    top["row"]["notag"] = True
                continue
            if m.group("tag") is not None:
                top = stack[-1] if stack else None
                if top and top["env"] in MATH_ENVS:
                    top["row"]["tag"] = m.group("tag")
                continue
            if m.group("rowsep"):
                top = stack[-1] if stack else None
                if top and top["env"].rstrip("*") in ROWWISE:
                    finalize_row(top, off)
                    top["row"]["start"] = pos
                continue
            if m.group("item"):
                top = stack[-1] if stack else None
                if top and top["env"] in ("enumerate", "itemize"):
                    top["items"] += 1
                continue

        # 파일 끝: 열린 범위는 이미 EOF 로 설정돼 있다. 끝 빈 줄 제거
        self._trim_ranges(src)

    def _rename(self, node, lab):
        # 합성 id 로 이미 등록되지 않았으므로(등록은 닫을 때) 그냥 id 교체
        node["id"] = lab

    def _finish_thm(self, node):
        base = node["id"]
        if base in self.by_id:
            k = 2
            while f"{base}#{k}" in self.by_id:
                k += 1
            node["id"] = f"{base}#{k}"
            node["duplicate_of"] = base
        self.by_id[node["id"]] = node
        self.nodes.append(node)
        if node["label"]:
            self.labels[node["label"]] = node["id"]
        self.last_thm = node["id"]
        # 방금 만든 노드 안에서 제 id 로 기록된 항목(label→node)을 수정
        for n in self.nodes:
            if n.get("node") == base and "duplicate_of" in node:
                pass

    def _close_ranges(self, src, line, sub, sec):
        """새 헤더 직전 줄까지로 열린 (부)섹션 범위를 닫는다."""
        if sub and self._cur_sub_range is not None:
            if self._cur_sub_range["file"] == src.name:
                self._cur_sub_range["lines"][1] = line - 1
            self._cur_sub_range = None
        if sec and self._cur_sec_range is not None:
            if self._cur_sec_range["file"] == src.name:
                self._cur_sec_range["lines"][1] = line - 1
            self._cur_sec_range = None

    def _trim_ranges(self, src):
        def trim(rng):
            if rng["file"] != src.name:
                return
            a, b = rng["lines"]
            while b > a and not src.clean[b - 1].strip():
                b -= 1
            rng["lines"][1] = b
        for n in self.nodes:
            if n["kind"] in ("section", "subsection"):
                for r in n["ranges"]:
                    trim(r)
                n["lines"] = list(n["ranges"][0]["lines"])

    def register_equation(self, src, lab, off, number, fr, stack):
        line = src.line(off)
        encl = None
        role = "text"
        for f in reversed(stack):
            if f["env"] in THM_ENVS:
                encl, role = f["node"], "statement"
                break
            if f["env"] == "proof":
                encl, role = f["node"], "proof"
                break
        if encl is not None and not isinstance(encl, str):
            encl_id = encl["label"] or encl["id"]
        else:
            encl_id = encl
        node = self.add({
            "id": lab, "kind": "equation", "number": number, "label": lab,
            "file": src.name, "line": line, "lines": [fr["line"], line],
            "node": encl_id, "role": role,
            "container": encl_id or self.sub_id or self.sec_id,
            "section": self.sec_id, "subsection": self.sub_id,
            "_frame_line": fr["line"],
        })
        self.labels[lab] = node["id"]


def fix_enclosing_ids(ex):
    """증명/진술 안의 노드가 가리키는 'node' 는 노드 객체이거나 id 다.
    id 는 라벨 확정 뒤 바뀔 수 있으므로 객체였던 것을 최종 id 로 바꾼다."""
    pass


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    ex = Extractor()
    files = section_files()
    srcs = [Src(SRC / "sections" / f"{f}.tex") for f in files]
    for s in srcs:
        ex.run_file(s)
    ex_post(ex, srcs)


def ex_post(ex, srcs):
    # 노드 객체였던 필드 정리: 프레임의 node 객체를 id 로
    def nid(x):
        if isinstance(x, dict):
            return x["id"]
        return x

    # 모든 노드 참조를 최종 id 로 정리. 증명→노드, 간선 src 등
    # 문제: run_file 중 enclosing() 은 theorem 프레임에서 node 객체를 돌려준다.
    for e in ex.edges:
        e["src"] = nid(e["src"])
    for c in ex.cites:
        c["src"] = nid(c["src"])
    for n in ex.nodes:
        if "node" in n:
            n["node"] = nid(n["node"])
        if "container" in n:
            n["container"] = nid(n["container"])
    for p in ex.proofs:
        p["node"] = nid(p["node"])
    # 증명이 연결된 노드의 id 는 객체 id; 아래에서 proof 연결은 이미 객체에 기록됨

    ids = {n["id"] for n in ex.nodes}
    labels = {}
    for n in ex.nodes:
        if n.get("label"):
            labels[n["label"]] = n["id"]

    # dst 해소
    for e in ex.edges:
        t = labels.get(e["dst"])
        e["resolved"] = t is not None
        if t is not None:
            tn = ex.by_id[t]
            e["dst_kind"] = tn["kind"]
            if tn["kind"] in ("equation", "item", "figure", "label"):
                e["dst_container"] = tn["container"] if tn.get("container") in ids else tn["container"]
            else:
                e["dst_container"] = t
        else:
            e["dst_kind"] = None
            e["dst_container"] = None
    for c in ex.cites:
        pass
    # 노드별 cites
    per = {}
    for c in ex.cites:
        per.setdefault(c["src"], [])
        if c["key"] not in per[c["src"]]:
            per[c["src"]].append(c["key"])
    for n in ex.nodes:
        if n["kind"] in THM_ENVS:
            n["cites"] = per.get(n["id"], [])

    # 파일 시작에서 열었다가 곧바로 새 헤더에 닫힌 빈 범위 제거
    for n in ex.nodes:
        if n["kind"] in ("section", "subsection"):
            n["ranges"] = [r for r in n["ranges"] if r["lines"][1] >= r["lines"][0]]
            n["lines"] = list(n["ranges"][0]["lines"])
    # 정리: 임시 필드 삭제
    for n in ex.nodes:
        n.pop("_frame_line", None)

    graph = {
        "files": [s.name for s in srcs],
        "nodes": ex.nodes,
        "edges": ex.edges,
        "cites": ex.cites,
        "proofs": ex.proofs,
        "labels": labels,
    }
    sentences = split_sentences(ex, srcs)
    (BUILD / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (BUILD / "sentences.json").write_text(json.dumps(sentences, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    kinds = Counter(n["kind"] for n in ex.nodes)
    print("nodes:", sum(kinds.values()))
    for k, v in sorted(kinds.items()):
        print(f"  {k}: {v}")
    print("edges:", len(ex.edges), "(unresolved: %d)" % sum(1 for e in ex.edges if not e["resolved"]))
    print("cites:", len(ex.cites))
    print("sentences:", len(sentences["sentences"]), "paragraphs:", len(sentences["paragraphs"]))
    nop = [n["id"] for n in ex.nodes if n["kind"] in PROOF_OWNERS and not n["proof"]]
    print("theorem/prop/lemma/cor without proof:", len(nop), nop)


# ---------------------------------------------------------------- 문장 분할
ABBR = {"i.e", "e.g", "cf", "fig", "figs", "eq", "eqs", "vs", "resp", "thm", "prop", "lem",
        "cor", "sec", "al", "no", "ch", "def", "approx", "viz", "wrt", "w.r.t", "s.t", "a.s",
        "p", "pp", "vol", "dr", "mr", "ca", "etc"}
DISPLAY_ENVS = NUMBERED_DISPLAY | {e + "*" for e in NUMBERED_DISPLAY} | {"displaymath"}
SKIP_ENVS = {"figure", "figure*", "tikzpicture", "abstract"}
BREAK_ENVS = set(THM_ENVS) | {"proof", "enumerate", "itemize", "center", "quote"}


def find_unescaped(T, s, start):
    i = start
    n = len(T)
    while i < n:
        c = T[i]
        if c == "\\":
            i += 2
            continue
        if c == "$" and T.startswith(s, i):
            return i
        i += 1
    return -1


def split_sentences(ex, srcs):
    secs = {}
    for h in ex.sec_info:
        secs[(h["file"], h["line"])] = h
    # 노드 줄 범위 (진술/증명)
    ranges = {}
    for n in ex.nodes:
        if n["kind"] in THM_ENVS:
            ranges.setdefault(n["file"], []).append((n["lines"][0], n["lines"][1], n["id"], "statement"))
            for r in n["proofs"]:
                ranges.setdefault(r["file"], []).append((r["lines"][0], r["lines"][1], n["id"], "proof"))
    for p in ex.proofs:
        if p["node"] is None:
            ranges.setdefault(p["file"], []).append((p["lines"][0], p["lines"][1], None, "proof"))

    def node_at(fname, line):
        best = None
        for a, b, nid, role in ranges.get(fname, []):
            if a <= line <= b and (best is None or (b - a) < (best[1] - best[0])):
                best = (a, b, nid, role)
        return (best[2], best[3]) if best else (None, "text")

    sentences = []
    paragraphs = []
    cur_sec = None  # 번호 문자열
    cur_sec_num = None
    para_n = 0
    for src in srcs:
        T = src.text
        n = len(T)
        i = 0
        s0 = None  # 현재 문장 시작
        last = None  # 현재 문장의 마지막 유효 문자 위치
        depth = 0
        sent_k = 0
        need_para = True
        cur_para = None

        def flush(para_break):
            nonlocal s0, last, sent_k, need_para, cur_para, para_n
            if s0 is not None and last is not None and last >= s0:
                if need_para:
                    para_n += 1
                    sent_k = 0
                    need_para = False
                    cur_para = {
                        "id": f"§{cur_sec} ¶{para_n}", "section": cur_sec,
                        "para": para_n, "file": src.name,
                        "lines": [src.line(s0), src.line(last)], "sentences": [],
                    }
                    paragraphs.append(cur_para)
                sent_k += 1
                text = re.sub(r"\\label(?:\[[^\]]*\])?\{[^}]*\}", "", T[s0:last + 1])
                text = re.sub(r"\s+", " ", text).strip()
                a, b = src.line(s0), src.line(last)
                nid, role = node_at(src.name, a)
                sid = f"§{cur_sec} ¶{para_n} s{sent_k}"
                sentences.append({
                    "id": sid, "section": cur_sec, "para": para_n, "idx": sent_k,
                    "file": src.name, "lines": [a, b], "text": text,
                    "node": nid, "role": role,
                })
                cur_para["sentences"].append(sid)
                cur_para["lines"][1] = b
            s0 = None
            last = None
            if para_break:
                need_para = True

        def mark(a, b):
            """a..b (포함) 구간을 현재 문장에 포함."""
            nonlocal s0, last
            if s0 is None:
                s0 = a
            last = b

        while i < n:
            c = T[i]
            if c == "\n":
                m = re.compile(r"\n[ \t\r]*\n").match(T, i)
                if m:
                    flush(True)
                    depth = 0
                    i = m.end() - 1
                i += 1
                continue
            if c in " \t\r":
                i += 1
                continue
            if c == "\\":
                # 구조 명령
                m = re.compile(r"\\(section|subsection|subsubsection)\*?(?![A-Za-z])").match(T, i)
                if m:
                    flush(True)
                    p = skip_ws(T, m.end())
                    if p < n and T[p] == "[":
                        p = skip_ws(T, read_balanced(T, p, "[", "]"))
                    if p < n and T[p] == "{":
                        p = read_balanced(T, p, "{", "}")
                    lm = LABEL_AT.match(T, p)
                    if lm:
                        p = lm.end()
                    h = secs.get((src.name, src.line(i)))
                    if h:
                        cur_sec = h["number"]
                    para_n = 0
                    need_para = True
                    i = p
                    continue
                m = re.compile(r"\\paragraph\*?\s*\{").match(T, i)
                if m:
                    flush(True)
                    i = read_balanced(T, m.end() - 1, "{", "}")
                    continue
                m = re.compile(r"\\(begin|end)\{([A-Za-z]+\*?)\}").match(T, i)
                if m:
                    kind, env = m.group(1), m.group(2)
                    if kind == "begin" and env in SKIP_ENVS:
                        flush(True)
                        em = re.compile(r"\\end\{%s\}" % re.escape(env)).search(T, m.end())
                        i = em.end() if em else n
                        continue
                    if env in BREAK_ENVS:
                        flush(True)
                        i = m.end()
                        if kind == "begin":
                            p = skip_ws(T, i)
                            if p < n and T[p] == "[" and (env in THM_ENVS or env == "proof" or env in ("enumerate", "itemize")):
                                i = read_balanced(T, p, "[", "]")
                        continue
                    if kind == "begin" and env in DISPLAY_ENVS:
                        em = re.compile(r"\\end\{%s\}" % re.escape(env)).search(T, m.end())
                        e = em.end() if em else n
                        mark(i, e - 1)
                        body = T[m.end():em.start()] if em else ""
                        i = e
                        if body.rstrip().endswith("."):
                            nxt = skip_ws(T, i)
                            if nxt >= n or T[nxt].isupper():
                                flush(False)
                        continue
                    # 기타 환경: 토큰만 문장에 포함
                    mark(i, m.end() - 1)
                    i = m.end()
                    continue
                if T.startswith("\\[", i):
                    e = T.find("\\]", i + 2)
                    e = (e + 2) if e >= 0 else n
                    body = T[i + 2:e - 2]
                    mark(i, e - 1)
                    i = e
                    if body.rstrip().endswith("."):
                        nxt = skip_ws(T, i)
                        if nxt >= n or T[nxt].isupper():
                            flush(False)
                    continue
                if T.startswith("\\(", i):
                    e = T.find("\\)", i + 2)
                    e = (e + 2) if e >= 0 else n
                    mark(i, e - 1)
                    i = e
                    continue
                m = re.compile(r"\\item(?![A-Za-z])").match(T, i)
                if m:
                    flush(True)
                    i = m.end()
                    # \item[...] 옵션
                    continue
                m = re.compile(r"\\label(?:\[[^\]]*\])?\{[^}]*\}").match(T, i)
                if m:
                    # 문장 안이면 포함 범위만 늘리지 않음
                    i = m.end()
                    continue
                # 일반 제어열: 이스케이프 문자 한 쌍 또는 이름
                m = re.compile(r"\\([A-Za-z]+\*?|.)", re.S).match(T, i)
                e = m.end() if m else i + 1
                mark(i, e - 1)
                i = e
                continue
            if c == "$":
                if T.startswith("$$", i):
                    e = find_unescaped(T, "$$", i + 2)
                    e = (e + 2) if e >= 0 else n
                    body = T[i + 2:e - 2]
                    mark(i, e - 1)
                    i = e
                    if body.rstrip().endswith("."):
                        nxt = skip_ws(T, i)
                        if nxt >= n or T[nxt].isupper():
                            flush(False)
                    continue
                e = find_unescaped(T, "$", i + 1)
                e = (e + 1) if e >= 0 else n
                mark(i, e - 1)
                i = e
                continue
            if c == "{":
                depth += 1
                mark(i, i)
                i += 1
                continue
            if c == "}":
                depth = max(0, depth - 1)
                mark(i, i)
                i += 1
                continue
            if c in ".?!":
                mark(i, i)
                j = i + 1
                # 연속 구두점/닫는 따옴표 괄호
                while j < n and T[j] in ")'\"”’]}" and depth == 0:
                    j += 1
                is_end = False
                if depth == 0 and (j >= n or T[j] in " \t\r\n"):
                    k = skip_ws(T, j)
                    nxt_ok = k >= n or T[k].isupper() or T[k] in "\\$(`["
                    if c == "." and nxt_ok and k < n and T[k] == "\\":
                        # \cref, \emph 같은 명령으로 시작하는 건 허용, 단 \item/\end 는 호출 쪽에서 처리
                        pass
                    if nxt_ok:
                        w = re.search(r"([A-Za-z.]+)$", T[max(0, i - 12):i])
                        word = w.group(1).lower() if w else ""
                        if c == "." and (word in ABBR or (len(word) == 1 and word.isalpha() and word.isupper())
                                         or re.fullmatch(r"[a-z]\.[a-z]", word or "")):
                            nxt_ok = False
                        if c == "." and w and len(w.group(1)) == 1 and w.group(1).isupper():
                            nxt_ok = False
                    is_end = nxt_ok
                if is_end:
                    mark(i, j - 1)
                    i = j
                    flush(False)
                    continue
                i += 1
                continue
            mark(i, i)
            i += 1
        flush(True)
    return {"sentences": sentences, "paragraphs": paragraphs}


if __name__ == "__main__":
    main()
