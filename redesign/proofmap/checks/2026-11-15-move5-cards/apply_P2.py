#!/usr/bin/env python3
"""P2 결과를 graphs/move5.json 에 넣는다 (작성자 판정, 2026-11-15). 한 번만 돈다.
- DC로 들어오는 edge 둘에 항목을 더한다(카드 뼈대 + LLM 채움이 찾은 계약의 누락): t19 += unused_coord, t20 += children_independent.
- 카드 뼈대 판 하위 graph AVG, DC, PB 를 넣는다. THM은 이미 하위 graph가 있으므로 넣지 않는다(비교용 파일만).
"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
P = HERE.parents[1] / "graphs/move5.json"
doc = json.loads(P.read_text(encoding="utf-8"))
top = doc["graphs"][0]
E = {e["id"]: e for e in top["edges"]}
E["t19"]["carries"].append({"node": "AVG", "item": "unused_coord", "used_at": [176, 177, 198, 199], "origin": "found_on_open"})
E["t20"]["carries"].append({"node": "X_SAMP", "item": "children_independent", "used_at": [180, 181], "origin": "found_on_open"})
for e in (E["t19"], E["t20"]):
    e["origin"] = "mixed"
dc = next(n for n in top["nodes"] if n["id"] == "DC")
for need in dc["contract"]["needs"]:
    if need["from"] == "AVG": need["items"].append("unused_coord")
    if need["from"] == "X_SAMP": need["items"].append("children_independent")
P.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for nid in ("AVG", "DC", "PB"):
    subprocess.run([sys.executable, str(HERE / "assemble_cards.py"), str(P), nid, str(HERE / f"P2-{nid}.graph.json")], check=True)
doc = json.loads(P.read_text(encoding="utf-8"))
for nid in ("AVG", "DC", "PB"):
    sub = json.loads((HERE / f"P2-{nid}.graph.json").read_text(encoding="utf-8"))
    doc["graphs"] = [g for g in doc["graphs"] if g["id"] != sub["id"]] + [sub]
    next(n for n in doc["graphs"][0]["nodes"] if n["id"] == nid)["subgraph"] = sub["id"]
P.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("applied")
