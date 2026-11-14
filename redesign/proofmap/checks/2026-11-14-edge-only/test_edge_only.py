"""전제 전달을 edge 하나로 통일한 국소 모델의 결함 주입 시험."""
import importlib.util
import json
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
s=importlib.util.spec_from_file_location('check',ROOT/'tools/check.py');checker=importlib.util.module_from_spec(s);s.loader.exec_module(checker)
s=importlib.util.spec_from_file_location('view',ROOT/'tools/build_viewer.py');view=importlib.util.module_from_spec(s);s.loader.exec_module(view)
c=checker.contracts

class EdgeOnlyTests(unittest.TestCase):
    def setUp(self):
        self.doc=json.loads((ROOT/'graphs/move4.json').read_text())
        self.gs={g['id']:g for g in self.doc['graphs']}
        self.pm=next(n for n in self.gs['fv']['nodes'] if n['id']=='PM')
        self.owner=next(n for n in self.gs['top']['nodes'] if n['id']=='O1')
    def messages(self):
        a=c.contract_audit(self.doc)
        return '\n'.join(m for table in [a['nodes'],a['edges']] for msgs in table.values() for m in msgs)
    def test_no_context_or_local_assumption_channel(self):
        for gid in ['fv','cp']:
            g=self.gs[gid]
            self.assertEqual(g['premise_mode'],'edges_only')
            self.assertFalse(g.get('contexts'))
            for n in g['nodes']:
                self.assertFalse(n.get('local_context'))
                self.assertFalse(n.get('conditions'))
                for row in n.get('derivation',[]):
                    self.assertFalse(any(u.startswith('context:') for u in row['uses']))
    def test_projection_is_exact_parent_input_subset(self):
        for gid in ['fv','cp']:
            g=self.gs[gid]
            pg=self.gs[g['parent']['graph']]
            for n in g['nodes']:
                if n['kind']!='external':continue
                pe=next(e for e in pg['edges'] if e['id']==n['import_edge'])
                self.assertTrue(c.contains_ref(self.doc,pe['output_ref'],n['statement_ref']))
                self.assertNotIn('statement',n)
    def test_parent_cannot_omit_an_imported_premise(self):
        e=next(e for e in self.gs['diff']['edges'] if e['id']=='diff-e9')
        clauses=list(self.owner['outputs']['fv_inputs']['clauses'])
        e['output_ref']={**e['output_ref'],'clauses':[k for k in clauses if k!='insertion']}
        self.assertIn('부모 입력이 공급하지 않은 항목',self.messages())
        self.assertEqual(view.completion_audit(self.doc)[('diff','D2')]['state'],'incomplete')
    def test_unknown_projection_item_is_not_a_new_assumption(self):
        n=next(n for n in self.gs['fv']['nodes'] if n['id']=='XSET')
        n['statement_ref']['clauses'].append('invented_assumption')
        self.assertIn('추적할 수 없는 외부 전제',self.messages())
    def test_context_injection_is_visible(self):
        self.gs['fv']['contexts']=[{'id':'hidden','text':'A≥0','nodes':['PM']}]
        self.assertIn('context 전제가 추가',self.messages())
        self.assertEqual(view.completion_audit(self.doc)[('fv','PM')]['state'],'incomplete')
    def test_local_context_injection_is_visible(self):
        self.pm['local_context']=['새 가정']
        self.assertIn('추적되지 않는 local_context',self.messages())
    def test_free_condition_injection_is_visible(self):
        self.pm['conditions']=['새 가정']
        self.assertIn('추적되지 않는 conditions',self.messages())
    def test_local_introduction_cannot_be_an_assumption(self):
        self.pm['introductions'].append({'kind':'assumption','symbol':'q','statement':'new premise'})
        self.assertIn('로컬 도입에 새 가정',self.messages())
    def test_same_symbol_with_different_binding_is_rejected(self):
        self.owner['outputs']['fv_inputs']['clauses']['insertion']['bindings']['j']='another-proof.j'
        self.assertIn('기호 j의 binding 공급 불일치',self.messages())
    def test_local_index_scope_is_not_interchangeable(self):
        self.pm['introductions'][1]['scope']='cp.JOIN.r'
        self.assertIn('binding scope 불일치',self.messages())
        errors,_,_=checker.check(self.doc)
        self.assertTrue(any('INTRO_SCOPE' in e for e in errors))
    def test_removed_shared_edge_is_not_replaced_by_context(self):
        self.gs['fv']['edges']=[e for e in self.gs['fv']['edges'] if e['id']!='g2']
        errors,_,_=checker.check(self.doc)
        self.assertTrue(any('SYMBOL_UNDEFINED' in e for e in errors))
    def test_changed_parameter_independence_requires_review(self):
        clause=self.owner['outputs']['fv_inputs']['clauses']['insertion']
        clause['statement']=clause['statement'].replace('매개변수에 무관하다','매개변수에 의존할 수 있다')
        self.assertTrue(c.contract_audit(self.doc)['edges'])
        self.assertEqual(view.completion_audit(self.doc)[('diff','D2')]['state'],'incomplete')
    def test_new_external_assumption_must_be_imported(self):
        self.gs['fv']['nodes'].append({'id':'EXTRA','kind':'external','external_ref':'XO','title':'숨긴 가정','statement':'새 가정','inputs':[]})
        self.gs['fv']['edges'].append({'id':'extra','from':'EXTRA','to':'PM','kind':'call','statement':'새 가정','complete':True})
        self.pm['inputs'].append('EXTRA')
        self.assertIn('부모 입력 edge에서 추적할 수 없는 외부 전제',self.messages())
        self.assertEqual(view.completion_audit(self.doc)[('fv','PM')]['state'],'incomplete')
    def test_local_index_must_be_closed_at_output(self):
        self.pm['produces'][0]['generalizes']=[]
        self.assertIn('로컬 지표 범위를 닫지 않음',self.messages())
    def test_loop_cannot_use_another_index_scope(self):
        loop=next(e for e in self.gs['fv']['edges'] if e['id']=='e4')
        loop['loop']['index_scope']='cp.JOIN.r'
        self.assertIn('귀납 edge와 로컬 지표의 범위가 다름',self.messages())

if __name__=='__main__':unittest.main()
