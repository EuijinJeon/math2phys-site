"""초안 세 개를 move4.before.json 위에 합쳐 graphs/move4.json 을 만든다. 다시 돌려도 결과가 같다."""
import json, pathlib
H = pathlib.Path(__file__).parent
ROOT = H.parent.parent
doc = json.load(open(H / 'move4.before.json'))
idx = {g['id']: i for i, g in enumerate(doc['graphs'])}
for name in ('top', 'p7', 'diff'):
    for g in json.load(open(H / 'drafts' / f'{name}.json'))['graphs']:
        doc['graphs'][idx[g['id']]] = g
G = {g['id']: g for g in doc['graphs']}
node = lambda g, i: next(n for n in G[g]['nodes'] if n['id'] == i)
edge = lambda g, i: next(e for e in G[g]['edges'] if e['id'] == i)

# 1. O1: 빠진 정의를 이름 붙은 given 출력으로 (진술은 건드리지 않아 기존 지문 불변)
def cl(title, st, defs):
    return {"title": title, "statement": st, "defines": defs}
node('top', 'O1').setdefault('outputs', {})['tree_defs'] = {
    "role": "given", "title": "tree의 표본·구조 정의 (O1 진술의 보충)", "conditions": [],
    "grounding": {"source": "trees.tex 29–39, 79–82, 92–100, 105", "state": "proposed"},
    "clauses": {
        "tree": cl("tree의 vertex", "유한 tree $\\mathcal T$ 는 공통 root와 깊이 $L$ 에서 끝나는 유한 개의 path로 이루어진다. 내부 vertex는 자식이 하나 이상이고, 자식이 하나뿐인 구간도 그대로 둔다. $\\operatorname{Leaves}(\\mathcal T)$ 는 깊이 $L$ 의 끝 vertex, $\\operatorname{Int}(\\mathcal T)$ 는 내부 vertex의 집합이다. (trees.tex 29–31, 97–104)", ["T", "Leaves", "Int"]),
        "sampling": cl("표본 평균 $E_{\\mathcal T}$", "각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 이 표본 추출의, root가 주어진 기대값이다. (trees.tex 32–34)", ["E_T"]),
        "projectivity": cl("표본 법칙의 사영 일관성", "일부 leaf와, 남은 leaf가 쓰지 않는 그 path의 부분을 지워도 남은 tree의 표본 법칙은 보존된다. (trees.tex 38–39)", []),
        "superscript": cl("위첨자 $A$", "삽입 후의 kernel $K_d^A$ 는 확률 kernel이고, tree 기대값의 위첨자 $A$ 는 이 kernel들로 뽑는다는 뜻이다. (trees.tex 79–82)", ["E_A"]),
        "vertex_data": cl("깊이와 자식 수", "prescribed tree의 내부 vertex $\\beta$ 에 대해 $d_\\beta$ 는 그 깊이, $n_\\beta$ 는 자식 수다. (trees.tex 92–93)", ["d_beta", "n_beta"]),
        "density": cl("밀도", "$W_{\\mathcal T}(A)=dP^A_{\\mathcal T}/dP_{\\mathcal T}$, 곧 삽입 후 tree 법칙의 (root가 주어진) 결합 밀도다. (trees.tex 97–100)", ["W"]),
        "Y_beta": cl("$Y_\\beta$", "$Y_\\beta$ 는 $\\beta$ 의 prefix에서 평가한 $Y_{d_\\beta}$ 다. (trees.tex 105)", ["Y_beta"]),
    }}

# 2. diff: 그 출력을 고르는 정의 edge 셋
def ref_edge(i, to, clauses, defs, label, summary, src):
    return {"id": i, "from": "XO", "to": to, "kind": "definition", "label": label, "summary": summary,
            "defines": defs, "status": "connected", "complete": True,
            "grounding": {"source": src, "state": "proposed"},
            "not_carried": "O1의 본문 진술과 fv_inputs 항목은 싣지 않는다(다른 edge가 싣는다).",
            "output_ref": {"graph": "top", "node": "O1", "output": "tree_defs", "clauses": clauses}}
G['diff']['edges'] += [
    ref_edge('diff-e13', 'D1', ['tree', 'vertex_data', 'Y_beta'], ['Leaves', 'Int', 'd_beta', 'n_beta', 'Y_beta'], 'vertex 자료', '$d_\\beta$, $n_\\beta$, $Y_\\beta=Y_{d_\\beta}$', 'trees.tex 29–31, 92–93, 105'),
    ref_edge('diff-e14', 'D3', ['tree', 'sampling'], ['Leaves', 'Int', 'E_T'], '$E_{\\mathcal T}$', '원래 kernel로 뽑는 root 조건부 평균', 'trees.tex 29–34'),
    ref_edge('diff-e15', 'S1', ['sampling', 'projectivity', 'superscript', 'density'], ['E_T', 'E_A', 'W'], '표본 법칙', '독립 표집, 사영 일관성, 위첨자 $A$, 밀도', 'trees.tex 32–39, 79–82, 97–100'),
]
def close(nid, eid, lines, syms):
    n = node('diff', nid)
    for k in lines:
        L = n['derivation'][k - 1]
        if f'edge:{eid}' not in L['uses']: L['uses'].append(f'edge:{eid}')
        L['by'] += f' 이 정의는 {eid}(top.O1.outputs.tree_defs)가 싣는다.'
    kept = [s for s in n['review']['open'] if 'top.O1이' not in s and 'D2의 produces' not in s]
    n['review']['open'] = kept
    n['review']['checks'].append({"question": f"{'·'.join(syms)}의 정의는 어디서 오는가?", "answer": f"{eid}가 top.O1.outputs.tree_defs의 해당 항목을 고른다. 통합 때 원문 줄과 대조해 O1에 given 출력으로 더했다."})
    n['status'] = 'complete'
close('D1', 'diff-e13', [1, 3, 4], ['d_β', 'n_β', 'Y_β'])
close('D3', 'diff-e14', [1, 4], ['E_T'])
edge('diff', 'diff-e1')['not_carried'] = "$E_{\\mathcal T}$, $F$의 정의, kernel 표현, 첫 변분은 싣지 않는다. $d_\\beta$, $n_\\beta$, $Y_\\beta$의 뜻은 diff-e13이 싣는다."
edge('diff', 'diff-e10')['not_carried'] = "$W$의 식, Y 재귀, 첫 변분, 표본 규칙은 싣지 않는다. $E_{\\mathcal T}$의 뜻은 diff-e14가 싣는다."
edge('diff', 'diff-e12')['not_carried'] = "자식들의 조건부 독립, $E_{\\mathcal T}$의 정의, 사영 일관성, 위첨자 $A$의 뜻, $W_{\\mathcal T}(A)$가 밀도라는 것은 diff-e15가 싣는다."
node('diff', 'S1')['inputs'] = sorted(set(node('diff', 'S1').get('inputs', [])) | {'XO'})

# 2b. 수신 검토 기록: 통합 담당(작성 모델)이 O1.tree_defs 항목을 원문 줄과 대조하고 받는 유도의 사용처를 확인한 시점의 지문
sys_path = __import__('sys').path; sys_path.insert(0, str(ROOT / 'tools'))
import output_contracts as oc
for nid, eid, cls in (('D1', 'diff-e13', ['tree', 'vertex_data', 'Y_beta']), ('D3', 'diff-e14', ['tree', 'sampling']), ('S1', 'diff-e15', ['sampling', 'projectivity', 'superscript', 'density'])):
    ref = {"graph": "top", "node": "O1", "output": "tree_defs", "clauses": cls}
    node('diff', nid).setdefault('input_ports', {})['tree_defs'] = {"edge": eid, "requires": ref, "reviewed_fingerprint": oc.fingerprint(doc, ref)}

# 3. D2.produces 에 새 보내는 edge
p = node('diff', 'D2')['produces']
if not any(x['edge'] == 'diff-e11' for x in p):
    p.append({"edge": "diff-e11", "output": "kernel_form", "by": "diff-e4와 같은 출력 kernel_form을 그대로 전달한다."})

# 4. \b(backspace)로 깨진 \beta 등 복구
def fix(x):
    if isinstance(x, str): return x.replace('\x08', '\\b')
    if isinstance(x, list): return [fix(v) for v in x]
    if isinstance(x, dict): return {k: fix(v) for k, v in x.items()}
    return x
import sys
if '--no-bs' not in sys.argv:
    doc['graphs'] = fix(doc['graphs'])
doc['content_note'] = "모든 근거는 proposed이며 사용자 확인 전이다. 2026-11-14 통합: top·p7·diff의 edge를 새 형식으로 옮겼다(p7-e3, p7-e11은 내용 미확정). diff의 D1·D3은 국소 완결, top의 R2·R3·F1·F2와 p7의 안쪽 node는 sketch다. author_filled 표시가 있는 줄은 원문이 보증하지 않는다."
out = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else ROOT / 'graphs' / 'move4.json'
json.dump(doc, open(out, 'w'), ensure_ascii=False, indent=2); open(out, 'a').write('\n')
