"""출력 변경·수신 요구 불일치·재검토 전파의 결함 주입 시험."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('c',ROOT/'tools/output_contracts.py');c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
s=importlib.util.spec_from_file_location('v',ROOT/'tools/build_viewer.py');v=importlib.util.module_from_spec(s);s.loader.exec_module(v)

class OutputContractsTests(unittest.TestCase):
    def setUp(self):
        self.doc=json.loads((ROOT/'graphs/move4.json').read_text())
        self.ref={'graph':'diff','node':'D2','output':'kernel_form'}
        self.g=next(g for g in self.doc['graphs'] if g['id']=='diff')
        self.e=next(e for e in self.g['edges'] if e['id']=='diff-e4')
        self.d2=next(n for n in self.g['nodes'] if n['id']=='D2')
        self.d4=next(n for n in self.g['nodes'] if n['id']=='D4')
    def test_current_binding_and_expansion(self):
        report=c.contract_audit(self.doc)
        self.assertFalse(report['edges']);self.assertFalse(report['nodes'])
        self.assertNotIn('statement',self.e)
        resolved=c.resolve_document(self.doc)
        d2=next(n for g in resolved['graphs'] if g['id']=='diff' for n in g['nodes'] if n['id']=='D2')
        e=next(e for g in resolved['graphs'] if g['id']=='diff' for e in g['edges'] if e['id']=='diff-e4')
        self.assertIn(d2['statement'],e['statement'])
        self.assertIn('kernel',e['statement'])
        self.assertIn('FP_BIND',e['use_note'])
    def test_changed_output_marks_consumer_and_descendants(self):
        self.d2['outputs']['kernel_form']['statement']+=' changed'
        a=c.contract_audit(self.doc)
        self.assertIn(('diff','diff-e4'),a['edges'])
        self.assertIn(('fresh','FP_PACK'),a['nodes'])
        self.assertEqual(v.completion_audit(self.doc)[('diff','D4')]['state'],'incomplete')
    def test_changed_conditions_require_review(self):
        self.d2['outputs']['kernel_form']['conditions'].append('changed condition')
        self.assertTrue(c.contract_audit(self.doc)['edges'][('diff','diff-e4')])
    def test_changed_internal_proof_requires_review(self):
        pm=next(n for g in self.doc['graphs'] if g['id']=='fv' for n in g['nodes'] if n['id']=='PM')
        pm['derivation'][0]['expr']+=' changed'
        self.assertTrue(c.contract_audit(self.doc)['outputs'][('diff','D2','kernel_form')]['issues'])
        self.assertTrue(c.contract_audit(self.doc)['edges'][('diff','diff-e4')])
    def test_layout_change_does_not_invalidate_math_review(self):
        for g in self.doc['graphs']:
            for n in g['nodes']:n['layout']={'col':5,'row':7}
        self.assertFalse(c.contract_audit(self.doc)['edges'])
    def test_missing_output_is_reported(self):
        self.d2['outputs'].pop('kernel_form')
        self.assertTrue(c.contract_audit(self.doc)['edges'][('diff','diff-e4')])
        resolved=c.resolve_document(self.doc)
        n=next(n for g in resolved['graphs'] if g['id']=='diff' for n in g['nodes'] if n['id']=='D2')
        self.assertIn('요구 출력 없음',n['statement'])
    def test_wrong_receiver_requirement(self):
        self.d4['input_ports']['first_variation']['requires']={**self.ref,'output':'other'}
        self.assertIn('수신 요구 출력과 전달 출력 불일치',c.contract_audit(self.doc)['edges'][('diff','diff-e4')])
    def test_independent_copy_is_not_allowed(self):
        self.e['statement']='extra untracked theorem'
        self.assertIn('출력 참조 edge에 독립 statement가 중복됨',c.contract_audit(self.doc)['edges'][('diff','diff-e4')])
    def test_unreviewed_consumer_is_visible(self):
        self.d4['input_ports']['first_variation'].pop('reviewed_fingerprint')
        self.assertTrue(c.contract_audit(self.doc)['edges'][('diff','diff-e4')])
    def test_consumer_cannot_claim_missing_connection(self):
        self.d4['input_ports']['first_variation']['edge']='not-an-edge'
        self.assertTrue(c.contract_audit(self.doc)['nodes'][('diff','D4')])
    def test_standalone_statement_reference_cannot_dangle(self):
        self.d2['statement_ref']={**self.ref,'output':'missing'}
        self.assertIn('진술 참조의 요구 출력 없음',c.contract_audit(self.doc)['nodes'][('diff','D2')])
    def test_statement_reference_rejects_independent_copy(self):
        self.d2['statement']='a second version'
        self.assertIn('진술 참조와 독립 statement가 중복됨',c.contract_audit(self.doc)['nodes'][('diff','D2')])

if __name__=='__main__':unittest.main()
