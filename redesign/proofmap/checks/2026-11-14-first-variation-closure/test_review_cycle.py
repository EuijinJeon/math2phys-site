"""첫 변분 연결의 변경→재검토→완결 시험. 변경은 메모리 사본에만 한다."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
s=importlib.util.spec_from_file_location('v',ROOT/'tools/build_viewer.py');v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
c=v.contracts
REF={'graph':'diff','node':'D2','output':'kernel_form'}


def review_producer(doc):
    for g in doc['graphs']:
        for n in g['nodes']:
            for name,entry in n.get('outputs',{}).items():
                if entry.get('role')=='given':continue
                ref={'graph':g['id'],'node':n['id'],'output':name}
                entry['proof_review'].update(output_fingerprint=c.digest(c.payload(c.output_entry(doc,ref))),
                                             proof_fingerprint=c.digest(c.proof_snapshot(doc,entry['proof'])))


def review_consumers(doc):
    for g in doc['graphs']:
        for n in g['nodes']:
            for port in n.get('input_ports',{}).values():
                port['reviewed_fingerprint']=c.fingerprint(doc,port['requires'])


def state(doc):
    a=v.completion_audit(doc)
    return {f'{gid}.{nid}':{'state':a[(gid,nid)]['state'],'issues':a[(gid,nid)]['issues']}
            for gid,nid in [('diff','D2'),('diff','D4'),('fresh','FP_BIND'),('fresh','FP_PACK')]}


def run_cycle(baseline):
    original=c.digest(baseline)
    changed=copy.deepcopy(baseline)
    entry=c.output_entry(changed,REF)
    entry['conditions'].append('시험용 추가 제한: '+r'$A_{\boldsymbol t}\ge2a$인 부분영역에 한정해 사용한다.')
    pending=state(changed)
    consumers_only=copy.deepcopy(changed);review_consumers(consumers_only)
    producer_only=copy.deepcopy(changed);review_producer(producer_only)
    reviewed=copy.deepcopy(producer_only);review_consumers(reviewed)
    result={'baseline':state(baseline),'condition_changed':pending,
            'consumers_only_reviewed':state(consumers_only),
            'producer_only_reviewed':state(producer_only),'all_reviewed':state(reviewed),
            'review_reason':'추가 조건 A≥2a는 기존 A≥a의 부분영역을 택한다. TM의 로그 미분과 PM의 m b^m c 지배상계는 그대로 적용된다. CP의 합성과 FP_BIND의 d=d_beta 대입도 같다. 따라서 유도와 수신 대응을 모두 대조한 뒤 각각의 검토 기록을 갱신할 수 있다.',
            'scope':'변경·검토는 메모리 사본에서만 실행. 원본의 조건이나 검토 기록을 자동 변경하지 않음.'}
    assert c.digest(baseline)==original
    return result


class ReviewCycleTests(unittest.TestCase):
    def setUp(self):
        self.doc=json.loads((ROOT/'graphs/move4.json').read_text())

    def test_condition_change_requires_both_reviews(self):
        result=run_cycle(self.doc)
        for name in ['diff.D2','diff.D4','fresh.FP_BIND','fresh.FP_PACK']:
            self.assertEqual(result['baseline'][name]['state'],'complete')
            self.assertEqual(result['condition_changed'][name]['state'],'incomplete')
            self.assertEqual(result['consumers_only_reviewed'][name]['state'],'incomplete')
            self.assertEqual(result['all_reviewed'][name]['state'],'complete')
        self.assertEqual(result['producer_only_reviewed']['diff.D4']['state'],'incomplete')

    def test_outer_input_change_invalidates_proof_and_consumers(self):
        source=next(n for g in self.doc['graphs'] if g['id']=='top' for n in g['nodes'] if n['id']=='O1')
        source['outputs']['fv_inputs']['clauses']['insertion']['statement']+=' [시험용 입력 변경]'
        a=c.contract_audit(self.doc)
        self.assertTrue(a['outputs'][('diff','D2','kernel_form')]['issues'])
        self.assertTrue(a['edges'][('diff','diff-e4')])
        self.assertEqual(state(self.doc)['diff.D2']['state'],'incomplete')

    def test_inherited_input_source_change_invalidates_review(self):
        obj=next(n for g in self.doc['graphs'] if g['id']=='top' for n in g['nodes'] if n['id']=='O1')
        obj['statement']+=' [시험용 정의 변경]'
        self.assertTrue(c.contract_audit(self.doc)['outputs'][('diff','D2','kernel_form')]['issues'])

    def test_review_metadata_has_no_hash_fixed_point(self):
        before=c.fingerprint(self.doc,REF)
        review_producer(self.doc);review_consumers(self.doc)
        self.assertEqual(before,c.fingerprint(self.doc,REF))
        self.assertFalse(c.contract_audit(self.doc)['nodes'])


if __name__=='__main__':
    doc=json.loads((ROOT/'graphs/move4.json').read_text())
    (HERE/'review-cycle-results.json').write_text(json.dumps(run_cycle(doc),ensure_ascii=False,indent=2)+'\n')
    unittest.main()
