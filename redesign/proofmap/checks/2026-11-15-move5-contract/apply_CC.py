#!/usr/bin/env python3
"""CC를 연 뒤 parent_change_requests 판정을 적용한다 (작성자 판정, 2026-11-15). 한 번만 돌린다."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "../graphs/move5.json"
doc = json.loads(P.read_text(encoding="utf-8"))
top = doc["graphs"][0]
N = {n["id"]: n for n in top["nodes"]}
E = {e["id"]: e for e in top["edges"]}
D = "decorrelation.tex"

# 둘레 밖 (C6b): 기호 표 추가 4, THM 기호 목록 추가.
new = [("D_coord", "$D$, $D_j$", f"{D} 492–494", "aligned 구성의 서로 다른 깊이 좌표 수 $D=b(S)+1$ ($d$, $e$ 포함). $T_j$ 에 속한 항은 $D_j=b(T_j)+1$ 개 좌표만 쓴다. (THM 607–609 는 $d$ 가 없어 $D=b(S)$ 로 다시 쓴다)"),
       ("pi_j", "$\\pi_j(\\mathbf q)$", f"{D} 495–496", "shift한 항의 좌표 $\\pi_j(\\mathbf q)=(e+1,(q_v+1)_{v\\in\\operatorname{Br}(T_j)})$."),
       ("w_j", "$w_j$", f"{D} 498–499", "자식 공분산을 그 좌표의 함수로 본 것."),
       ("gamma_pow", "$\\gamma$", f"{D} 499", "fiber 경계의 지수 $0<\\gamma\\le1$ (CC는 $1/4$, THM은 $1/2$)." )]
for i, tex, at, text in new:
    doc["symbols"].append({"id": i, "tex": tex, "defined_at": at, "text": text, "added_by": "open CC"})
for x in ("CC", "THM"):
    N[x]["symbols"] += [s[0] for s in new]

# 둘레 안: 받는 edge의 used_at 보강과 t6 에 charging 항목(가정 문맥) 추가.
def add_used(eid, item, lines):
    c = next(c for c in E[eid]["carries"] if c["item"] == item)
    c["used_at"] = sorted(set(c["used_at"]) | set(lines))
    c.setdefault("used_at_added_on_open", []).extend(lines)
add_used("t3", "holder", [503, 504, 505]); add_used("t3", "unused_coord", [497])
add_used("t12", "leaf_removal", [277, 466]); add_used("t5", "kappa_total", [416, 418])
ch = next(o for o in N["X_CH"]["contract"]["outputs"] if o["id"] == "charging")
E["t6"]["carries"].insert(0, {"node": "X_CH", "item": "charging", "used_at": [345, 346, 347, 348], "origin": "found_on_open"})
E["t6"]["statement"] = "[X_CH.charging] " + ch["statement"] + " " + E["t6"]["statement"]
E["t6"]["summary"] = "charging, " + E["t6"]["summary"]
E["t6"]["origin"] = "mixed"
for need in N["CC"]["contract"]["needs"]:
    if need["from"] == "X_CH":
        need["items"] = ["charging"] + need["items"]
sub = next(g for g in doc["graphs"] if g["id"] == "cc")
for n in sub["nodes"]:
    if n["id"] == "ext_X_CH":
        n["items"] = ["charging"] + n["items"]
        n["note"] = (n.get("note", "") + " 통합 단계: subagent의 missed_dependencies 에 따라 charging(가정 문맥)을 함께 받는다.").strip()
P.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("applied")
