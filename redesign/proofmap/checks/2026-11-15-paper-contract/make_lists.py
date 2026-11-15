#!/usr/bin/env python3
"""stats.json → lists.md (보고서에 붙이는 목록 전부)."""
import json
from collections import Counter
s = json.load(open('stats.json'))
P = lambda x: str(x).replace('|', '\\|')
L = ["### 열림 전부 (6)\n\n| node | 입력 | 쓰는 줄 | 이유 |\n|---|---|---|---|"]
for o in s['opens']:
    L.append(f"| `{o['node']}` | {P(o['what'])} | {', '.join(map(str, o['used_at']))} | {P(o['why'])} |")
cu = Counter(u['floor'] for u in s['floor_uses'])
L.append(f"\n### 바닥 전부 ({len(s['floor_list'])}개, 쓰임 {len(s['floor_uses'])}회)\n\n| id (쓰임) | 종류 | 인용 | 진술 |\n|---|---|---|---|")
for f in s['floor_list']:
    cite = (f.get('cite', '') + ' ' + f.get('cited_at', '')).strip() or '—'
    L.append(f"| `{f['id']}` ({cu[f['id']]}) | {f.get('kind')} | {P(cite)} | {P(f.get('statement', ''))} |")
lst = [u for u in s['unplaced'] if u['handled'] == 'list']
L.append(f"\n### 절 머리·remark·번호 없는 문단 가운데 기호 표로 받지 못한 것 ({len(lst)} / {len(s['unplaced'])})\n\n| 절 | 줄 | 내용 |\n|---|---|---|")
for u in lst:
    L.append(f"| {u['section']} | {u['lines'][0]}–{u['lines'][-1]} | {P(u['what'])} |")
L.append(f"\n### 카드 의존 거절 ({len(s['rejected'])}건)\n\n| node | 카드 → use | 이유 |\n|---|---|---|")
for r in s['rejected']:
    L.append(f"| `{r['node']}` | `{r['card']}` → `{r['use']}` | {P(r['why'])} |")
L.append(f"\n### 카드·원문 어긋남 ({len(s['mismatches'])}건)\n\n| node | 카드 | 내용 |\n|---|---|---|")
for r in s['mismatches']:
    L.append(f"| `{r['node']}` | `{r['card']}` | {P(r['what'])} |")
L.append(f"\n### 출력 항목 추가 ({len(s['item_added_list'])}건)\n\n| 대상 node | 항목 | 쓰는 node | 경로 |\n|---|---|---|---|")
for r in s['item_added_list']:
    L.append(f"| `{r['node']}` | `{r['item']}` | `{r['by']}` | {'같은 agent 안' if r['where'] == 'same_agent' else '뒤 단계 요청(new_item)'} |")
open('lists.md', 'w').write("\n".join(L) + "\n")
