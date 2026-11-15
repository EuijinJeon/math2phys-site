#!/usr/bin/env python3
"""독립 확인용 표본: 종류(node/symbol/floor)마다 6개, random.seed(20261115). 통합자 보정한 입력은 뺀다."""
import json, random
from pathlib import Path
HERE = Path(__file__).resolve().parent
doc = json.loads((HERE.parents[1] / "graphs/paper.json").read_text(encoding="utf-8"))
syms = {s["id"]: s for s in doc["symbols"]}; floors = {f["id"]: f for f in doc["floors"]}
items, files = {}, {}
for g in doc["graphs"]:
    for n in g["nodes"]:
        c = n.get("contract", {})
        if c.get("source_label") and n["kind"] != "external":
            files[c["source_label"]] = n["grounding"]["source"].split(" ")[0]
            for o in c.get("outputs", []):
                items[(c["source_label"], o["id"])] = o
pool = {"node": [], "symbol": [], "floor": []}
for g in doc["graphs"]:
    for n in g["nodes"]:
        c = n.get("contract", {})
        for d in c.get("needs", []):
            t = d["binding"]["type"]
            if t in pool and not d.get("integrator_note"):
                pool[t].append((c["source_label"], d))
random.seed(20261115)
out = []
for t in ("node", "symbol", "floor"):
    for lab, d in random.sample(pool[t], 6):
        b = d["binding"]
        tgt = {"node": lambda: dict(where=f"{files[b['node']]} {items[(b['node'], b['item'])]['lines'][0]}–{items[(b['node'], b['item'])]['lines'][1]}", node=b["node"], item=b["item"], statement=items[(b['node'], b['item'])]["statement"]),
               "symbol": lambda: dict(where=syms[b["symbol"]]["defined_at"], tex=syms[b["symbol"]]["tex"], text=syms[b["symbol"]]["text"]),
               "floor": lambda: dict(floors[b["floor"]])}[t]()
        out.append({"k": len(out) + 1, "type": t, "node": lab, "node_file": files[lab], "input": d.get("what"),
                    "used_at": d.get("used_at"), "used_file": d.get("used_file", files[lab]), "bound_to": tgt})
print(json.dumps(out, ensure_ascii=False, indent=1))
