#!/usr/bin/env python3
"""THM을 연 뒤 parent_change_requests 판정을 적용한다 (작성자 판정, 2026-11-15). 한 번만 돌린다."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "../graphs/move5.json"
doc = json.loads(P.read_text(encoding="utf-8"))
top = doc["graphs"][0]
N = {n["id"]: n for n in top["nodes"]}
E = {e["id"]: e for e in top["edges"]}
sub = next(g for g in doc["graphs"] if g["id"] == "thm")

# 둘레 밖 (C6b): 항목·바닥 추가만. 기존 항목의 내용·조건은 바꾸지 않는다.
N["X_TI"]["contract"]["outputs"].append({"id": "empty_addition", "lines": [449, 468], "added_by": "open THM",
    "statement": "$k=0$ 이면 $R_E$ 는 spin anchor에서 $R_{\\{a_*\\}}$, marker anchor에서 $1$ 이다(449). 빈 추가도 허용한다(468)."})
N["X_EXT"]["contract"]["outputs"].append({"id": "empty_weight", "lines": [295, 295], "added_by": "open THM",
    "statement": "빈 extension의 무게는 $1$ 이다. (trees.tex 295, Lemma tree:extension-expansion 의 문장)"})
doc["floor"]["reader"].append("곱 차이 부등식: 좌표가 $[-1,1]$ 인 vector들의 좌표별 곱의 차는 각 인자 차의 합으로 누른다 (decorrelation.tex 186, 368, 582가 이름으로만 씀; THM을 열 때 바닥으로 지정)")
for x in ("X_TI", "X_EXT"):
    N[x]["statement"] = " ".join(o["statement"] for o in N[x]["contract"]["outputs"])
    N[x]["summary"] = ", ".join(o["id"] for o in N[x]["contract"]["outputs"])

# 둘레 안: THM 기호, 받는 edge t16 항목 추가, 새 받는 edge X_EXT→THM.
N["THM"]["symbols"] += ["v_N", "A_S", "m_d"]
t16 = E["t16"]
t16["carries"].append({"node": "X_TI", "item": "empty_addition", "used_at": [533, 534, 535], "origin": "found_on_open"})
t16["statement"] += " [X_TI.empty_addition] " + N["X_TI"]["contract"]["outputs"][-1]["statement"]
t16["summary"] += ", empty_addition"
rule = next(o for o in N["X_EXT"]["contract"]["outputs"] if o["id"] == "rule")
top["edges"].append({"id": "t23", "from": "X_EXT", "to": "THM", "kind": "call",
    "summary": "rule, empty_weight",
    "statement": "[X_EXT.rule] " + rule["statement"] + " [X_EXT.empty_weight] " + N["X_EXT"]["contract"]["outputs"][-1]["statement"],
    "carries": [{"node": "X_EXT", "item": "rule", "used_at": [541, 542, 547], "origin": "found_on_open"},
                {"node": "X_EXT", "item": "empty_weight", "used_at": [533, 534], "origin": "found_on_open"}],
    "origin": "found_on_open", "grounding": {"source": "decorrelation.tex 533–547"},
    "status": "connected", "complete": True})
N["THM"]["inputs"] = sorted(set(N["THM"]["inputs"]) | {"X_EXT"})
N["THM"]["contract"]["needs"].append({"from": "X_EXT", "items": ["rule", "empty_weight"]})
for n in sub["nodes"]:
    if n["id"] == "ext_X_TI":
        n["items"] = n["items"] + ["empty_addition"]

# 하위 graph의 닿는 면을 맞춘다(통합 단계에서 작성자가 더함).
sub["nodes"].append({"id": "ext_X_EXT", "kind": "external", "title": "extension 규칙과 빈 extension의 무게",
    "external_ref": "X_EXT", "import_edge": "t23", "items": ["rule", "empty_weight"],
    "grounding": {"source": "decorrelation.tex 533–547", "state": "proposed"},
    "note": "통합 단계에서 더함. subagent의 missed_dependencies(marker 계수의 $-\\delta$, 빈 추가의 계수)에 대한 답."})
sub["edges"] += [
    {"id": "e23", "from": "ext_X_EXT", "to": "s3_coefficient", "kind": "call",
     "statement": "[X_EXT.rule] 첫 path는 old tree가 아직 갈라지지 않은 $e-1$ 의 unary vertex에서 fresh로 나가며 그 계수는 $\\gamma_\\beta=m_{e-1}-m_e=-\\delta$ ($n_\\beta=1$).",
     "carries": [{"item": "rule", "used_at": [541, 542, 547]}], "grounding": {"source": "decorrelation.tex 541–547; trees.tex 266–268"},
     "author_filled": "$-\\delta$ 를 규칙의 $\\gamma_\\beta$ 에 $n_\\beta=1$ 을 넣어 계산한 것은 작성자. 원문은 $C(S,e)=-\\delta\\kappa(S)$ 만 적는다.",
     "status": "connected", "complete": True},
    {"id": "e24", "from": "ext_X_EXT", "to": "s1_singleton", "kind": "call",
     "statement": "[X_EXT.empty_weight] 빈 extension의 무게는 $1$.", "carries": [{"item": "empty_weight", "used_at": [533, 534]}],
     "grounding": {"source": "trees.tex 295"}, "status": "connected", "complete": True}]
P.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("applied")
