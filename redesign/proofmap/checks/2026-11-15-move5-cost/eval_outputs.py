#!/usr/bin/env python3
"""여는 작업 산출 하나를 move5.v1 의 사본(메모리)에 넣고 check.py 의 check() 결과를 센다.
통합 때와 같은 기계 보정(derivation 꼴, produces 보충)을 한다. 원본 파일은 바꾸지 않는다.

    python3 eval_outputs.py OUT.json NODE
"""
import copy, json, sys, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('chk', HERE.parents[1] / 'tools/check.py')
chk = importlib.util.module_from_spec(spec); spec.loader.exec_module(chk)

def evaluate(out_path, nid):
    doc = json.loads((HERE / 'move5.v1.json').read_text(encoding='utf-8'))
    sub = json.loads(Path(out_path).read_text(encoding='utf-8'))['graph']
    fixes = 0
    for n in sub['nodes']:
        for d in n.get('derivation', []):
            if 'expr' not in d and 'line' in d: d['expr'] = d.pop('line'); fixes += 1
            if isinstance(d.get('by'), list): d['by'] = '; '.join(d['by']); fixes += 1
        if n.get('status') == 'complete' and not n.get('produces'):
            outs = [e['id'] for e in sub['edges'] if e['from'] == n['id']]
            if len(outs) == 1: n['produces'] = [{'edge': outs[0], 'by': '기계 보충'}]; fixes += 1
            else: n['status'] = 'sketch'; fixes += 1
        if n['kind'] == 'output' and not n.get('title'): n['title'] = 'output'; fixes += 1
        if n['kind'] == 'external' and not n.get('title'): n['title'] = n.get('external_ref', ''); fixes += 1
    for e in sub['edges']:
        if isinstance(e.get('carries'), list) and e['carries'] and isinstance(e['carries'][0], str):
            e['carries'] = [{'item': c, 'used_at': e.get('used_at', [])} for c in e['carries']]
        e.setdefault('kind', 'flow')
    top = doc['graphs'][0]
    sub['id'] = sub.get('id', nid.lower()) + '_eval'
    sub.setdefault('title', nid)
    for n in top['nodes']:
        if n['id'] == nid: n['subgraph'] = sub['id']
    doc['graphs'] = [g for g in doc['graphs'] if g.get('parent', {}) is None or g['parent'].get('node') != nid] + [sub]
    for n in top['nodes']:
        if n['id'] == nid: n['subgraph'] = sub['id']
    errors, warnings, report = chk.check(doc)
    mine = lambda xs: [x for x in xs if f"[{sub['id']}]" in x]
    return {'errors': len(mine(errors)), 'warnings': len(mine(warnings)), 'fixes': fixes,
            'error_list': mine(errors)[:5], 'warning_list': mine(warnings)[:5]}

if __name__ == '__main__':
    print(json.dumps(evaluate(sys.argv[1], sys.argv[2]), ensure_ascii=False, indent=1))
