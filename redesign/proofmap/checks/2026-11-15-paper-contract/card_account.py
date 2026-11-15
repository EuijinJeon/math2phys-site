#!/usr/bin/env python3
"""Q7: 뼈대의 카드 의존 (node, 카드 use) 하나하나가 산출에서 받아들여졌는지(묶음으로 확인) / 거절됐는지 센다.
받아들임 판정(기계): (가) use 의 주인 node 에 묶인 입력이 있다, 또는 (나) use 가 주인 없는 카드이면
그 카드의 원문 줄과 겹치는 기호 정의 위치·바닥 인용 줄·열림 이유 줄을 가진 입력이 있다."""
import json, glob, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sk = json.loads((HERE / "skeleton.json").read_text())
doc = json.loads((HERE.parents[1] / "graphs/paper.json").read_text())
unowned = {u["id"]: u["lines"] for u in sk["unowned_cards"]}
syms = {s["id"]: s for s in doc["symbols"]}
def ranges(text):
    out = []
    for f, rest in re.findall(r"([\w.]+\.tex)\s+([0-9–\-, ]+)", text or ""):
        for part in rest.split(","):
            a, _, b = part.strip().replace("-", "–").partition("–")
            if a.strip().isdigit():
                out.append((f, int(a), int(b) if b.strip().isdigit() else int(a)))
    return out
needs = {}
for p in glob.glob(str(HERE / "out/*.json")):
    for n in json.load(open(p))["nodes"]:
        needs[n["id"]] = n
cat = {"node_bound": 0, "line_overlap": 0, "rejected": 0, "none": 0}; none = []
for n in sk["nodes"]:
    out = needs[n["id"]]
    rej = {(r["use"]) for r in out.get("card_deps_rejected", [])}
    bound_nodes = {x["binding"].get("node") for x in out["needs"]}
    locs = []
    for x in out["needs"]:
        b = x["binding"]
        if b["type"] == "symbol" and b.get("symbol") in syms:
            locs += ranges(syms[b["symbol"]]["defined_at"])
        elif b["type"] == "open":
            locs += ranges(b.get("why", ""))
    for i in n["inputs"]:
        for c in i["card_refs"]:
            u = c["use"]
            if u in rej:
                cat["rejected"] += 1
            elif i["kind"] == "node" and i["key"] in bound_nodes:
                cat["node_bound"] += 1
            elif u in unowned and any(f == lf and a <= lb and la <= b for f, a, b in unowned[u] for lf, la, lb in locs):
                cat["line_overlap"] += 1
            else:
                cat["none"] += 1; none.append((n["id"], c["card"], u))
print(json.dumps(cat)); [print(*x) for x in none]
