#!/usr/bin/env python3
"""move4·move5 의 외부 입력 node → paper.json 대응표를 확인하고 표로 찍는다.

    python3 correspond.py > correspondence.md
대응은 correspondence.json(손으로 적음). 여기서는 대상이 paper.json 에 있는지와
원문 줄(move5 항목의 lines 대 paper 항목의 lines / 기호 정의 위치)을 나란히 적는다.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PM = HERE.parents[1]
paper = json.loads((PM / "graphs/paper.json").read_text(encoding="utf-8"))
m5 = json.loads((PM / "graphs/move5.json").read_text(encoding="utf-8"))
corr = json.loads((HERE / "correspondence.json").read_text(encoding="utf-8"))
items, syms = {}, {s["id"]: s for s in paper["symbols"]}
for g in paper["graphs"]:
    for n in g["nodes"]:
        c = n.get("contract", {})
        if c.get("source_label") and n["kind"] != "external":
            for o in c.get("outputs", []):
                items[(c["source_label"], o["id"])] = (g["id"], o)
sections = {n["id"] for n in paper["graphs"][0]["nodes"]}
m5items = {(n["id"], o["id"]): o for n in m5["graphs"][0]["nodes"] for o in n.get("contract", {}).get("outputs", [])}


def show(t):
    if "symbol" in t:
        s = syms.get(t["symbol"])
        return (f"기호 `{t['symbol']}` ({s['defined_at']})" if s else f"**없음**: 기호 {t['symbol']}"), bool(s)
    if "section" in t:
        return (f"절 `{t['section']}`" if t["section"] in sections else "**없음**"), t["section"] in sections
    got = items.get((t["node"], t["item"]))
    return (f"`{t['node']}`.`{t['item']}` ({got[1]['lines'][0]}–{got[1]['lines'][1]})" if got else f"**없음**: {t['node']}.{t['item']}"), bool(got)


rows, miss, n_in = [], 0, 0
for r in corr["rows"]:
    if "items" in r:
        for it, ts in r["items"].items():
            n_in += 1
            o = m5items.get((r["node"], it))
            sh = [show(t) for t in ts]
            ok = ts and all(x[1] for x in sh)
            miss += 0 if ok else 1
            rows.append(f"| {r['file']} | `{r['node']}`.`{it}` | {r['role']} | {o['lines'][0]}–{o['lines'][1] if o else ''} | {'; '.join(x[0] for x in sh) or '대응 없음'} |")
    else:
        if r["role"] != "consumer":
            n_in += 1
        sh = [show(t) for t in r["to"]]
        ok = r["to"] and all(x[1] for x in sh)
        if r["role"] != "consumer":
            miss += 0 if ok else 1
        rows.append(f"| {r['file']} | `{r['node']}` ({r['what']}) | {r['role']} | — | {'; '.join(x[0] for x in sh) or '대응 없음'} |")
print("| 파일 | 외부 입력 | 역할 | 그쪽 원문 줄 | paper.json 대응 |\n|---|---|---|---|---|")
print("\n".join(rows))
print(f"\n입력·선언 입력 항목 {n_in}개 가운데 대응 없음 {miss}개. consumer 는 입력이 아니라 세지 않았다.")
