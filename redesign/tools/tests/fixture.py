"""시험용 fixture: 실제 원문(source/)과 graph.json 을 쓰되 카드는 임시 디렉터리에 새로 쓴다.

`--root` 로 check.py / build.py 에 넘긴다. 실제 cards/ 는 건드리지도 읽지도 않으므로
다른 사람이 cards/ 를 고치는 중에도 시험이 흔들리지 않는다.

기준 fixture (BASE) 는 reduction.tex 를 전부 덮고 모든 검사를 오류 0·경고 0 으로 통과해야 한다.
시험은 BASE 를 복사해 한 곳만 일부러 깨뜨리고, 검사가 그것을 잡는지 본다.
"""
import copy
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent


def card(id, kind, title, source, uses=(), children=(), provides="", body="", extra=""):
    """카드 한 장의 사전. source: [(파일, 시작, 끝), ...]"""
    return dict(id=id, kind=kind, title=title, source=list(source), uses=list(uses), children=list(children),
                provides=provides, body=body, extra=extra)


def base_cards():
    """BASE: 카드 id → 사전. (reduction.tex 1–87 전부, comparison.tex 225–231, upper/model 약간)"""
    cs = [
        card("reduction:section", "section", "§9 시험용", [("reduction.tex", 1, 8)],
             uses=["comp:bounded-lower"], children=["reduction:stability", "main:theorem"],
             provides="main:theorem",
             body="밖에서 받는 것: [[comp:bounded-lower]]"),
        card("reduction:stability", "lemma", "안정성", [("reduction.tex", 9, 26)],
             uses=["model:integrability", "x:fx-up"], children=["reduction:stability.s1", "reduction:stability.s2"],
             provides="main:theorem.s1"),
        card("reduction:stability.s1", "step", "로그 분배함수", [("reduction.tex", 28, 38)]),
        card("reduction:stability.s2", "step", "상수 이동", [("reduction.tex", 39, 43)]),
        card("main:theorem", "theorem", "주정리", [("model.tex", 130, 136)],
             uses=["model:integrability", "model:positivity"], children=["main:theorem.s1"]),
        card("main:theorem.s1", "step", "증명", [("reduction.tex", 45, 87)],
             uses=["comp:bounded-lower", "upper:bound"]),
        # 다른 섹션(원문 파일)의 카드들: 섹션 라벨 참조와 대칭 검사용
        card("comp:section", "section", "§8 시험용", [("comparison.tex", 1, 3)], children=["comp:bounded-lower"]),
        card("comp:bounded-lower", "corollary", "bounded 하한", [("comparison.tex", 225, 231)],
             uses=["x:fx-model-leaf"], provides="reduction:section, main:theorem.s1"),
        card("model:section", "section", "§2 시험용", [("model.tex", 1, 5)], children=["x:fx-model-leaf"]),
        card("x:fx-model-leaf", "definition", "모형의 한 정의", [("model.tex", 6, 6)],
             provides="comp:bounded-lower"),
        card("upper:section", "section", "§4 시험용", [("upper.tex", 1, 3)], children=["x:fx-up"]),
        card("x:fx-up", "definition", "상한 쪽 정의", [("upper.tex", 5, 5)], provides="reduction:stability"),
    ]
    return {c["id"]: c for c in cs}


def yq(s):
    return "'" + str(s).replace("'", "''") + "'"


def write_card(cdir, c):
    lines = ["---", f"id: {c['id']}", f"kind: {c['kind']}", f"title: {yq(c['title'])}",
             "uses: [" + ", ".join(c["uses"]) + "]"]
    lines.append(f"provides: {yq(c['provides'])}" if c["provides"] else "provides: null")
    lines.append("math: " + yq("시험용 진술"))
    lines.append("physics: null")
    lines.append("gap: null")
    lines.append("abstraction: blackbox")
    lines.append("children: [" + ", ".join(c["children"]) + "]")
    lines.append("source:")
    for (f, a, b) in c["source"]:
        lines.append(f"  - {{file: {f}, lines: [{a}, {b}]}}")
    lines.append("status: proposed")
    if c.get("extra"):
        lines.append(c["extra"])
    lines.append("---")
    lines.append(c["body"])
    (cdir / (c["id"].replace(":", ".") + ".md")).write_text("\n".join(lines) + "\n", encoding="utf-8")


RULES = """| rule | 물리 규칙 | 수학 노드 | 차이 | 유형 | 승인 |
|---|---|---|---|---|---|
| P1 | 시험용 규칙 | reduction:stability | 없음(시험) | blackbox | proposed |
"""


def make_root(cards, tmp=None, rules=RULES, l1=None):
    """cards: id → 사전. 임시 root 디렉터리를 만들어 돌려준다(호출자가 정리)."""
    root = Path(tmp or tempfile.mkdtemp(prefix="m2p-fixture-"))
    cdir = root / "cards"
    cdir.mkdir(parents=True, exist_ok=True)
    (root / "layers").mkdir(exist_ok=True)
    (root / "build").mkdir(exist_ok=True)
    for c in cards.values():
        write_card(cdir, c)
    if rules is not None:
        (root / "layers" / "rules.md").write_text(rules, encoding="utf-8")
    if l1 is not None:
        (root / "layers" / "L1.md").write_text(l1, encoding="utf-8")
    return root


LINE = re.compile(r"^(.+?): (통과|실패|경고|해당 없음) \(오류 (\d+), 경고 (\d+)\)$")


def run_check(root, sections="reduction"):
    """check.py 를 돌려 {검사 이름: (상태, 오류 수, 경고 수)}, 오류·경고 문장 목록, 종료 코드를 돌려준다."""
    out = Path(root) / "build" / "check-report.md"
    cmd = [sys.executable, str(TOOLS / "check.py"), "--root", str(root), "--out", str(out)]
    if sections:
        cmd += ["--sections", sections]
    r = subprocess.run(cmd, capture_output=True, text=True)
    res = {}
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            res[m.group(1)] = (m.group(2), int(m.group(3)), int(m.group(4)))
    text = out.read_text(encoding="utf-8") if out.is_file() else ""
    errs = [x[len("- 오류: "):] for x in text.splitlines() if x.startswith("- 오류: ")]
    warns = [x[len("- 경고: "):] for x in text.splitlines() if x.startswith("- 경고: ")]
    return res, errs, warns, r.returncode, r.stdout + r.stderr


def clone(cards):
    return copy.deepcopy(cards)
