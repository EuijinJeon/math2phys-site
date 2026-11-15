#!/usr/bin/env python3
"""P2: 카드(redesign/cards, 읽기만)에서 하위 graph의 뼈대를 기계로 만든다.

    python3 card_skeleton.py MOVE5.json NODE [NODE ...] > skeletons.json

뼈대의 안쪽 node = 그 node의 카드의 잎 자식 카드들(자식이 없으면 그 node 원문 범위 안에 원문 줄이 다 들어가는 카드들).
뼈대의 edge = 각 카드의 `uses`:
  - 같은 뼈대 안의 카드          → 안쪽 edge (origin: card)
  - 다른 맨 위 node에 속한 카드   → 그 node에서 오는 external (아래 CARD_TO_TOP; 접두어가 맨 위 node의 source_label 이면 기계 대응)
  - 기호·관례 카드               → edge가 아니라 기호 표 참조 (CARD_TO_SYMBOL)
  - 바닥 카드                    → floor
  - 그 밖                        → unmapped (보고)
대응표 CARD_TO_TOP 의 외부 정리 몇 줄과 CARD_TO_SYMBOL 은 작성자가 손으로 적은 것이다(아래 표시).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CARDS = HERE.parents[3] / "redesign/cards"

# 작성자 대응표 (손으로 적음). 기계 대응(접두어)으로 못 잡는 것만.
CARD_TO_TOP = {
    "pert:tree-identity": "X_TI", "x:pert-colored-extensions": "X_TI",
    "tree:reference-total": "X_RT", "tree:charging": "X_CH",
    "tree:extension-expansion": "X_EXT", "x:decor-tree-sampling": "X_SAMP",
    "decor:average-definition": "AVG", "x:decor-average-comparisons": "AVG",
}
CARD_TO_SYMBOL = {
    "x:decor-mesh": ["m_d", "delta"], "x:decor-limit-order": ["N_lim"], "x:decor-eta-regular": ["eta_regular"],
    "x:decor-topology": ["topology", "b_S"], "x:decor-spin-product": ["A_S", "R_S"],
    "decor:covariance-definition": ["F_d", "mu", "v_N"], "decor:projection-definition": ["a_p"],
    "tree:multioverlap": ["R_S"], "pert:selection": ["N_lim"],
}
FLOOR = {"x:decor-product-difference": "곱 차이 부등식"}


def read_card(path):
    text = path.read_text(encoding="utf-8")
    head = text.split("---")[1]
    get = lambda k: (re.search(rf"^{k}:\s*(.*)$", head, re.M) or [None, ""])[1].strip()
    lst = lambda k: [x.strip() for x in get(k).strip("[]").split(",") if x.strip()]
    m = re.search(r"^math: \|\n((?:  .*\n)+)", head, re.M)
    return {"id": get("id"), "title": get("title").strip("'"), "kind": get("kind"),
            "uses": lst("uses"), "children": lst("children"),
            "lines": [(f, int(a), int(b)) for f, a, b in re.findall(r"\{file: ([\w.]+), lines: \[(\d+), (\d+)\]\}", head)],
            "math": "\n".join(l[2:] for l in m.group(1).splitlines()) if m else ""}


def main():
    doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    want = sys.argv[2:]
    cards = {c["id"]: c for c in (read_card(p) for p in sorted(CARDS.glob("*.md")))}
    top = doc["graphs"][0]
    tn = {n["id"]: n for n in top["nodes"]}
    label_to_top = {n["contract"]["source_label"]: n["id"] for n in top["nodes"] if n.get("contract", {}).get("source_label")}

    def top_of(cid):
        if cid in CARD_TO_TOP:
            return CARD_TO_TOP[cid], "author_table"
        base = cid.split(".")[0]
        if base in label_to_top:
            return label_to_top[base], "prefix"
        return None, None

    def leaves(cid):
        c = cards.get(cid)
        if not c or not c["children"]:
            return [cid]
        out = []
        for ch in c["children"]:
            out += leaves(ch)
        return out

    result = {}
    for nid in want:
        n = tn[nid]
        lab = n["contract"]["source_label"]
        spans = [n["contract"]["statement_span"]] + ([n["contract"]["proof_span"]] if n["contract"]["proof_span"] else [])
        lo, hi = min(s[0] for s in spans), max(s[1] for s in spans)
        own = cards.get(lab)
        if own and own["children"]:
            members = leaves(lab)
            rule = "카드의 잎 자식"
        else:
            members = [cid for cid, c in cards.items()
                       if c["lines"] and all(f == "decorrelation.tex" and lo <= a and b <= hi for f, a, b in c["lines"])
                       and not cid.endswith(".section")]
            rule = "원문 범위 안의 카드"
        members = sorted(set(members), key=lambda c: cards[c]["lines"][0][1] if cards.get(c) and cards[c]["lines"] else 0)
        inner = [{"id": f"k{i + 1}", "card": cid, "title": cards[cid]["title"],
                  "lines": [cards[cid]["lines"][0][1], cards[cid]["lines"][-1][2]] if cards[cid]["lines"] else None,
                  "kind": cards[cid]["kind"]} for i, cid in enumerate(members) if cid in cards]
        by_card = {x["card"]: x["id"] for x in inner}
        edges, externals, symbols, floor, unmapped, mapping = [], {}, set(), set(), [], []
        for x in inner:
            for u in cards[x["card"]]["uses"]:
                if u in by_card:
                    if by_card[u] != x["id"]:
                        edges.append({"from": by_card[u], "to": x["id"], "origin": "card", "via": u})
                    continue
                lv = leaves(u) if u in cards else []
                if lv and len(lv) > 1 and all(l in by_card for l in lv):
                    # 잎이 아닌 카드를 쓰면 그 카드의 마지막 잎(결론을 내는 걸음)에서 받는다고 둔다(작성자 규칙).
                    edges.append({"from": by_card[lv[-1]], "to": x["id"], "origin": "card", "via": u, "rule": "last_leaf"})
                    continue
                if u in FLOOR:
                    floor.add(FLOOR[u]); continue
                if u in CARD_TO_SYMBOL:
                    symbols.update(CARD_TO_SYMBOL[u]); continue
                t, how = top_of(u)
                if t == nid:
                    unmapped.append({"card": x["card"], "uses": u, "why": "자기 node의 다른 카드인데 뼈대에 없다"}); continue
                if t:
                    externals.setdefault(t, set()).add(x["id"])
                    edges.append({"from": "x_" + t, "to": x["id"], "origin": "card", "via": u})
                    mapping.append({"card_use": u, "top": t, "how": how})
                else:
                    unmapped.append({"card": x["card"], "uses": u, "why": "대응 없음"})
        inputs = set(n.get("inputs", []))
        result[nid] = {
            "node": nid, "card": lab, "member_rule": rule, "inner": inner, "edges": edges,
            "externals": sorted(externals), "symbols": sorted(symbols), "floor": sorted(floor), "unmapped": unmapped,
            "card_inputs_not_in_contract": sorted(set(externals) - inputs),
            "contract_inputs_not_in_cards": sorted(inputs - set(externals)),
            "mapping": mapping,
            "card_math": {x["card"]: cards[x["card"]]["math"] for x in inner},
        }
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
