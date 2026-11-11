#!/usr/bin/env python3
"""적법성 검사 (SCHEMA.md 마지막 표). build/graph.json, cards/*.md, layers/*.md 를 읽어
build/check-report.md 를 쓴다. 오류가 없으면 종료 코드 0, 있으면 1.

사용: python3 tools/check.py [--sections decorrelation,trees] [--root DIR] [--out FILE]
  --root  cards/ 와 layers/ 를 담은 디렉터리 (기본: redesign/). source/ 와 graph.json 은 항상 실제 것을 쓴다.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402


def ranges_str(nums):
    nums = sorted(set(nums))
    out = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f"{nums[i]}" if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


class Report:
    def __init__(self):
        self.checks = []  # (name, status, errors list, warnings list, notes list)

    def add(self, name, errors, warnings, notes=None, na=None):
        if na:
            status = "해당 없음"
        elif errors:
            status = "실패"
        elif warnings:
            status = "경고"
        else:
            status = "통과"
        self.checks.append((name, status, errors, warnings, notes or [], na))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sections", default=None, help="포함 검사를 적용할 파일 stem (쉼표 구분)")
    ap.add_argument("--root", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    root = C.resolve_root(args.root)
    out = Path(args.out) if args.out else root / "build" / "check-report.md"
    graph = C.load_graph()
    cards = C.load_cards(root)
    valid = [c for c in cards if c.fm is not None and c.id]
    by_id = {}
    dup = []
    for c in valid:
        if c.id in by_id:
            dup.append(c)
        by_id[c.id] = c
    rules = C.parse_rules(root / "layers" / "rules.md")
    l1_path = root / "layers" / "L1.md"

    nodes = {}
    if graph:
        for n in graph["nodes"]:
            nodes[n["id"]] = n

    rep = Report()

    # --- 형식 (머리말 오류)
    fmt_err = []
    fmt_warn = []
    for c in cards:
        for e in c.errors:
            fmt_err.append(f"`cards/{c.fname}`: {e}")
    for c in dup:
        fmt_err.append(f"`cards/{c.fname}`: id `{c.id}` 가 다른 카드와 겹친다")
    for c in valid:
        k = c.get("kind")
        if k is None:
            fmt_err.append(f"`{c.id}`: kind가 없다")
        elif k not in C.KINDS:
            fmt_warn.append(f"`{c.id}`: kind `{k}` 는 규약에 없다")
        st = c.get("status")
        if st is not None and st not in C.STATUSES:
            fmt_warn.append(f"`{c.id}`: status `{st}` 는 규약에 없다")
        if C.is_null(c.get("title")):
            fmt_warn.append(f"`{c.id}`: title이 없다")
        for key in ("uses", "children"):
            v = c.get(key)
            if v is not None and not isinstance(v, list):
                fmt_err.append(f"`{c.id}`: {key}가 목록이 아니다")
    rep.add("형식 (머리말)", fmt_err, fmt_warn)

    # --- 정초
    e = []
    for c in valid:
        for msg in c.source_errors:
            e.append(f"`{c.id}`: {msg}")
    rep.add("정초", e, [], na=None if cards else "no cards yet")

    # --- 포함
    leaf = [c for c in valid if not c.children and c.source]
    notes = []
    e = []
    na = None
    if graph is None:
        na = "graph.json 없음 (먼저 extract.py)"
    elif not valid:
        na = "아직 카드 없음"
    else:
        if args.sections:
            targets = [s.strip() for s in args.sections.split(",") if s.strip()]
        else:
            targets = sorted({f[:-4] for c in valid for (f, a, b) in c.source})
        notes.append(f"대상 섹션(파일): {', '.join(targets) if targets else '(없음)'}")
        notes.append(f"카드 {len(valid)}개 중 잎 {len(leaf)}개")
        for stem in targets:
            fname = stem + ".tex"
            src = C.source_lines(fname)
            if src is None:
                e.append(f"{fname}: 원문 파일이 없다")
                continue
            need = set()
            spans = []
            for n in graph["nodes"]:
                if n["kind"] in C.THM_KINDS and n["file"] == fname:
                    spans.append(("진술 " + n["number"], n["lines"]))
                    for r in n.get("proofs", []):
                        if r["file"] == fname:
                            spans.append(("증명 " + n["number"], r["lines"]))
            for p in graph.get("proofs", []):
                if p["node"] is None and p["file"] == fname:
                    spans.append(("증명(연결 없음)", p["lines"]))
            # 증명 줄은 잎 카드가, 진술 줄은 아무 카드나(보통 그 정리 카드 자신) 덮으면 된다.
            need_stmt = set()
            for label, (a, b) in spans:
                for ln in range(a, b + 1):
                    if C.strip_comment(src[ln - 1]).strip():
                        (need_stmt if label.startswith("진술") else need).add(ln)
            have = set()
            for c in leaf:
                for (f, a, b) in c.source:
                    if f == fname:
                        have.update(range(a, b + 1))
            have_any = set()
            for c in valid:
                for (f, a, b) in c.source:
                    if f == fname:
                        have_any.update(range(a, b + 1))
            miss = sorted((need - have) | (need_stmt - have_any))
            need = need | need_stmt
            if miss:
                # 줄 번호를 소속 노드별로 묶어 표시
                by_owner = {}
                for ln in miss:
                    owner = "?"
                    for label, (a, b) in spans:
                        if a <= ln <= b:
                            owner = label
                            break
                    by_owner.setdefault(owner, []).append(ln)
                for owner, lns in by_owner.items():
                    e.append(f"{fname}:{ranges_str(lns)} ({owner}) — 덮는 카드가 없음 (증명은 잎 카드, 진술은 아무 카드)")
            else:
                notes.append(f"{fname}: 필요한 {len(need)}줄 모두 덮임")
    rep.add("포함", e, [], notes, na=na)

    # --- 의존
    w = []
    na = None
    if graph is None:
        na = "graph.json 없음"
    elif not valid:
        na = "아직 카드 없음"
    else:
        parent = {}
        for c in valid:
            for ch in c.children:
                parent.setdefault(ch, set()).add(c.id)

        def ancestors(cid):
            seen = set()
            st = [cid]
            while st:
                x = st.pop()
                for p in parent.get(x, ()):
                    if p not in seen:
                        seen.add(p)
                        st.append(p)
            return seen

        def descendants(cid):
            seen = set()
            st = [cid]
            while st:
                x = st.pop()
                cc = by_id.get(x)
                if cc:
                    for ch in cc.children:
                        if ch not in seen:
                            seen.add(ch)
                            st.append(ch)
            return seen

        label_loc = {}
        for n in graph["nodes"]:
            if n["kind"] in ("equation", "figure", "item", "label"):
                label_loc[n["id"]] = (n["file"], n["line"])
            else:
                label_loc[n["id"]] = (n["file"], n["lines"][0])
        seen_w = set()
        for c in valid:
            fam = {c.id} | ancestors(c.id) | descendants(c.id)
            allowed_ids = set(fam)
            for f in fam:
                fc = by_id.get(f)
                if fc:
                    allowed_ids.update(fc.uses)
            # 허용된 카드들의 source 범위 (같은 부모 증명 안, 혹은 uses 한 카드가 담은 위치)
            allowed_ranges = []
            for f in fam:
                fc = by_id.get(f)
                if fc:
                    allowed_ranges.extend(fc.source)
            for u in c.uses:
                uc = by_id.get(u)
                if uc:
                    allowed_ranges.extend(uc.source)
            for ed in graph["edges"]:
                hit = any(ed["file"] == f and a <= ed["line"] <= b for (f, a, b) in c.source)
                if not hit:
                    continue
                dst = ed["dst"]
                cont = ed.get("dst_container")
                # 본문(진술·증명 밖)에서 원문상 뒤에 나오는 대상을 가리키면 의존이 아니라 예고다.
                if ed.get("role") == "text" and dst in label_loc:
                    order = ["introduction", "model", "overview", "trees", "upper", "cavity",
                             "perturbations", "decorrelation", "comparison", "reduction", "consequences"]
                    def pos(f, ln):
                        s = f[:-4] if f.endswith(".tex") else f
                        return (order.index(s) if s in order else 99, ln)
                    if pos(*label_loc[dst]) > pos(ed["file"], ed["line"]):
                        continue
                if not ed.get("resolved"):
                    key = (c.id, dst, ed["file"], ed["line"])
                    if key not in seen_w:
                        seen_w.add(key)
                        w.append(f"{ed['file']}:{ed['line']} `{c.id}`: `\\{ed['cmd']}{{{dst}}}` 라벨을 원문에서 찾지 못함")
                    continue
                tnode = ed["dst"]
                ok = (dst in allowed_ids) or (cont in allowed_ids)
                if not ok:
                    loc = label_loc.get(cont) or label_loc.get(dst)
                    # 대상 라벨의 위치가 허용된 카드 범위 안이면 통과
                    dl = label_loc.get(dst)
                    if dl and any(dl[0] == f and a <= dl[1] <= b for (f, a, b) in allowed_ranges):
                        ok = True
                if not ok:
                    key = (c.id, dst, ed["file"], ed["line"])
                    if key in seen_w:
                        continue
                    seen_w.add(key)
                    tgt = dst if cont in (None, dst) else f"{dst} (in {cont})"
                    w.append(f"{ed['file']}:{ed['line']} `{c.id}`: `\\{ed['cmd']}{{{dst}}}` → {tgt} 이(가) uses에 없다")
    rep.add("의존", [], w, na=na)

    # --- 연결
    e = []
    known = set(by_id) | set(nodes)

    def exists(x):
        return x in known

    if not valid and rules is None and not l1_path.is_file():
        rep.add("연결", [], [], na="아직 카드와 층 문서 없음")
    else:
        for c in valid:
            for u in c.uses:
                if not exists(u):
                    e.append(f"`{c.id}`.uses: `{u}` 가 없다")
            for ch in c.children:
                if ch not in by_id:
                    e.append(f"`{c.id}`.children: `{ch}` 카드가 없다")
            for wid in sorted(set(C.wiki_ids(c.body))):
                if not exists(wid):
                    e.append(f"`{c.id}` 본문 [[{wid}]] 가 없다")
            for key in ("math", "physics", "gap", "provides"):
                v = c.get(key)
                if isinstance(v, str):
                    for wid in sorted(set(C.wiki_ids(v))):
                        if not exists(wid):
                            e.append(f"`{c.id}`.{key} [[{wid}]] 가 없다")
        if rules:
            for r in rules:
                for nid in C.rule_nodes(r.get("수학 노드", "")):
                    if not exists(nid):
                        e.append(f"rules.md `{r.get('rule')}` (줄 {r['_line']}): 수학 노드 `{nid}` 가 없다")
        for lname in ("L0.md", "L1.md"):
            lp = root / "layers" / lname
            if lp.is_file():
                for wid in sorted(set(C.wiki_ids(lp.read_text(encoding="utf-8")))):
                    if not exists(wid):
                        e.append(f"layers/{lname}: [[{wid}]] 가 없다")
        rep.add("연결", e, [])

    # --- 순환
    e = []
    if not valid:
        rep.add("순환", [], [], na="아직 카드 없음")
    else:
        for label, key in (("uses", "uses"), ("children", "children")):
            g = {c.id: [x for x in getattr(c, key) if x in by_id] for c in valid}
            for comp in sccs(g):
                if len(comp) > 1 or comp[0] in g.get(comp[0], []):
                    e.append(f"{label} 순환: " + " → ".join(f"`{x}`" for x in comp + [comp[0]]))
        rep.add("순환", e, [])

    # --- 사전
    e = []
    w = []
    if rules is None and not valid:
        rep.add("사전", [], [], na="아직 카드와 규칙 표 없음")
    else:
        if rules is None:
            w.append("layers/rules.md 가 없거나 규칙 표를 찾지 못함")
        else:
            for r in rules:
                rid = r.get("rule", "?")
                if not C.rule_nodes(r.get("수학 노드", "")):
                    e.append(f"rules.md {rid}: 수학 노드가 비었다")
                if C.is_null(r.get("차이")):
                    e.append(f"rules.md {rid}: 차이가 비었다")
                ab = r.get("유형", "").strip().strip("`")
                if ab not in C.ABSTRACTIONS:
                    w.append(f"rules.md {rid}: 유형 `{ab}` 가 규약 값이 아니다")
                st = r.get("상태", "").strip().strip("`")
                if st not in C.STATUSES:
                    w.append(f"rules.md {rid}: 상태 `{st}` 가 규약 값이 아니다")
        for c in valid:
            if not C.is_null(c.get("physics")):
                if C.is_null(c.get("gap")):
                    e.append(f"`{c.id}`: physics가 있는데 gap이 없다")
                ab = c.get("abstraction")
                if C.is_null(ab):
                    e.append(f"`{c.id}`: physics가 있는데 abstraction이 없다")
                elif ab not in C.ABSTRACTIONS:
                    e.append(f"`{c.id}`: abstraction `{ab}` 가 규약 값이 아니다")
                elif ab == "approximation" and C.is_null(c.get("gap")):
                    pass  # 위에서 이미 보고
            else:
                ab = c.get("abstraction")
                if not C.is_null(ab) and ab not in C.ABSTRACTIONS:
                    w.append(f"`{c.id}`: abstraction `{ab}` 가 규약 값이 아니다")
        rep.add("사전", e, w)

    # --- 단면
    e = []
    w = []
    notes = []
    if not l1_path.is_file():
        rep.add("단면", [], [], na="layers/L1.md 없음")
    else:
        moves = parse_moves(l1_path.read_text(encoding="utf-8"))
        rule_ids = {r.get("rule") for r in rules} if rules else set()
        if not moves:
            w.append("L1.md 에서 번호 붙은 수를 찾지 못함")
        for num, line, body in moves:
            ps = set(re.findall(r"\bP\d+\b", body))
            ws = set(C.wiki_ids(body))
            if not ps and not ws:
                e.append(f"L1.md 줄 {line}: 수 {num} 가 규칙(P번호)이나 노드([[id]])를 가리키지 않는다")
            for p in sorted(ps):
                if rules is not None and p not in rule_ids:
                    e.append(f"L1.md 줄 {line}: 수 {num} 의 {p} 가 rules.md 에 없다")
        notes.append(f"수 {len(moves)}개")
        rep.add("단면", e, w, notes)

    write_report(rep, out, cards, valid, leaf)
    nerr = sum(len(c[2]) for c in rep.checks)
    nwarn = sum(len(c[3]) for c in rep.checks)
    for name, status, errs, warns, _, na in rep.checks:
        print(f"{name}: {status} (오류 {len(errs)}, 경고 {len(warns)})")
    print(f"보고서: {out}")
    sys.exit(1 if nerr else 0)


def parse_moves(text):
    """L1.md 의 번호 붙은 수. 반환: [(번호, 시작 줄, 본문)]."""
    lines = text.split("\n")
    starts = []
    for i, l in enumerate(lines):
        m = re.match(r"^(\d+)[.)]\s+", l)
        if m:
            starts.append((i, m.group(1)))
            continue
        m = re.match(r"^#{2,4}\s*(?:수|Move|move|M)\s*(\d+)", l)
        if m:
            starts.append((i, m.group(1)))
    moves = []
    for k, (i, num) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        for j in range(i + 1, end):
            if re.match(r"^#{1,6}\s", lines[j]):
                end = j
                break
        moves.append((num, i + 1, "\n".join(lines[i:end])))
    return moves


def sccs(g):
    """Tarjan (재귀 없이 간단히 재귀 한도 올림)."""
    sys.setrecursionlimit(10000)
    index = {}
    low = {}
    on = set()
    st = []
    res = []
    counter = [0]

    def sc(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
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
            res.append(list(reversed(comp)))

    for v in sorted(g):
        if v not in index:
            sc(v)
    return [c for c in res if len(c) > 1 or c[0] in g.get(c[0], [])] + \
           [c for c in res if len(c) == 1 and c[0] not in g.get(c[0], [])]


def write_report(rep, out, cards, valid, leaf):
    L = ["# 적법성 검사 보고서", ""]
    L.append(f"카드 {len(cards)}개 (머리말 정상 {len(valid)}개, 잎 {len(leaf)}개).")
    if not cards:
        L.append("")
        L.append("아직 카드 없음: `cards/` 가 비어 있어 카드 검사는 건너뛴다.")
    L.append("")
    L.append("| 검사 | 결과 | 문제 수 |")
    L.append("|---|---|---|")
    for name, status, errs, warns, notes, na in rep.checks:
        cnt = f"오류 {len(errs)}" + (f", 경고 {len(warns)}" if warns else "")
        if na:
            cnt = "—"
        L.append(f"| {name} | {status} | {cnt} |")
    L.append("")
    for name, status, errs, warns, notes, na in rep.checks:
        L.append(f"## {name} — {status}")
        L.append("")
        if na:
            L.append(f"해당 없음: {na}")
            L.append("")
            continue
        for n in notes:
            L.append(f"- 참고: {n}")
        for x in errs:
            L.append(f"- 오류: {x}")
        for x in warns:
            L.append(f"- 경고: {x}")
        if not (notes or errs or warns):
            L.append("문제 없음.")
        L.append("")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
