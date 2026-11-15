#!/usr/bin/env python3
"""절 묶음 파일을 만든다.

    python3 make_bundle.py NAME SECTION[:node,...] ... > bundle-NAME.json

SECTION 만 주면 그 절의 node 전부(단, `main:theorem` 은 'main' 으로 따로 준다).
`main` = main:theorem node 하나. prior = out/*.json 에 이미 있는 절의 출력 항목·기호·바닥.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sk = json.loads((HERE / "skeleton.json").read_text(encoding="utf-8"))
cards_dir = HERE.parents[2] / "cards"


def card_title(cid):
    p = cards_dir / (cid.replace(":", ".") + ".md")
    if not p.exists():
        return None
    for line in p.read_text(encoding="utf-8").splitlines()[:6]:
        if line.startswith("title:"):
            return line[6:].strip().strip("'")


def main():
    name, wants = sys.argv[1], sys.argv[2:]
    take, order = [], []
    for w in wants:
        if w == "main":
            take += [n for n in sk["nodes"] if n["id"] == "main:theorem"]
            order.append("main (model.tex 의 main:theorem, 증명은 reduction.tex)")
            continue
        take += [n for n in sk["nodes"] if n["section"] == w and n["id"] != "main:theorem"]
        order.append(w)
    prior = {"items": [], "symbols": [], "floors": []}
    for p in sorted((HERE / "out").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for n in d["nodes"]:
            for o in n.get("outputs", []):
                prior["items"].append({"node": n["id"], "item": o["id"], "statement": o["statement"],
                                       "lines": o.get("lines"), "file": d.get("file") or n.get("file")})
        prior["symbols"] += [{k: s.get(k) for k in ("id", "tex", "defined_at", "text", "note") if s.get(k)}
                             for s in d.get("symbols_new", [])]
        prior["floors"] += d.get("floors_new", [])
    bundle = {
        "name": name, "process_order": order,
        "skeleton": take,
        "catalog": [{"id": n["id"], "file": n["file"], "span": n["span"], "rule": n["rule"], "env": n["env"],
                     "labels": [n["id"]] + n.get("merged_labels", []) + n["output_labels"] + n["exported"],
                     "title": card_title(n["id"])} for n in sk["nodes"]],
        "unowned_cards": sk["unowned_cards"],
        "note_main_theorem": "main:theorem 의 진술은 model.tex 130–136, 증명은 reduction.tex 의 번호 없는 문단(카드 main:theorem.s1–s4 의 원문 줄 참조)이다. 기계 추출은 그 증명을 node 에 붙이지 못했다.",
        "prior": prior,
    }
    print(json.dumps(bundle, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
