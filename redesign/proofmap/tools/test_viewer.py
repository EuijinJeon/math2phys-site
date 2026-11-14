"""증명 상태를 과장하지 않는 표시 및 고정 edge 식별자 회귀 시험."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('viewer', ROOT/'tools/build_viewer.py')
viewer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(viewer)


class ViewerTests(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads((ROOT/'graphs/move4.json').read_text())
        self.diff = next(g for g in self.doc['graphs'] if g['id']=='diff')
        self.d2 = next(n for n in self.diff['nodes'] if n['id']=='D2')

    def test_first_variation_boundary_is_now_closed(self):
        a = viewer.completion_audit(self.doc)[('diff','D2')]
        self.assertEqual(a['state'], 'complete')
        self.assertEqual(a['missing'], [])
        self.assertEqual(a['child'], {'done':3,'total':3,'complete':True})

    def test_missing_boundary_invalidates_its_previous_review(self):
        self.diff['edges']=[e for e in self.diff['edges'] if e['id']!='diff-e9']
        a = viewer.completion_audit(self.doc)[('diff','D2')]
        self.assertEqual(a['state'], 'incomplete')
        self.assertEqual(a['missing'], ['XO'])
        # 공유 입력과 항목 선택 모두 실제 부모 edge를 추적하므로 전부 미완결이다.
        self.assertEqual(a['child'], {'done':0,'total':3,'complete':False})
        self.assertTrue(a['contractIssues'])

    def test_declared_complete_does_not_hide_missing_input(self):
        self.d2['status'] = 'complete'
        self.diff['edges']=[e for e in self.diff['edges'] if e['id']!='diff-e9']
        self.assertEqual(viewer.completion_audit(self.doc)[('diff','D2')]['state'], 'incomplete')

    def test_boundary_repair_does_not_automatically_promote_declaration(self):
        self.d2.pop('status')
        self.assertEqual(viewer.completion_audit(self.doc)[('diff','D2')]['state'], 'unassessed')

    def test_open_edge_invalidates_displayed_completion(self):
        fresh = next(g for g in self.doc['graphs'] if g['id']=='fresh')
        next(e for e in fresh['edges'] if e['id']=='fp-result')['status']='open'
        audit = viewer.completion_audit(self.doc)
        self.assertEqual(audit[('fresh','FP_PACK')]['state'], 'incomplete')
        self.assertEqual(audit[('diff','D4')]['state'], 'incomplete')

    def test_no_derivation_does_not_display_as_complete(self):
        pm = next(n for g in self.doc['graphs'] if g['id']=='fv' for n in g['nodes'] if n['id']=='PM')
        pm.pop('derivation')
        self.assertEqual(viewer.completion_audit(self.doc)[('fv','PM')]['state'], 'incomplete')

    def test_external_inputs_are_not_certified_as_proofs(self):
        self.assertEqual(viewer.completion_audit(self.doc)[('diff','XO')]['state'], 'external')

    def test_complete_vertex_still_displays_as_complete(self):
        self.assertEqual(viewer.completion_audit(self.doc)[('diff','D4')]['state'], 'complete')

    def test_labels_remain_fixed_after_edge_reordering(self):
        original, _ = viewer.to_viewer(self.doc)
        for g in self.doc['graphs']:
            g['edges'].reverse()
        reversed_maps, _ = viewer.to_viewer(self.doc)
        for gid, g in original.items():
            before = {e['id']:(e['displayId'],e['caption']) for e in g['edges']}
            after = {e['id']:(e['displayId'],e['caption']) for e in reversed_maps[gid]['edges']}
            self.assertEqual(before,after)
            self.assertEqual(len({e['displayId'] for e in g['edges']}),len(g['edges']))

    def test_edge_content_and_endpoint_completion_are_separate(self):
        self.diff['edges']=[e for e in self.diff['edges'] if e['id']!='diff-e9']
        maps,_ = viewer.to_viewer(self.doc)
        edge = next(e for e in maps['diff']['edges'] if e['id']=='diff-e4')
        self.assertTrue(edge['contentComplete'])
        self.assertEqual(edge['displayId'],'e4')
        self.assertEqual(edge['caption'],'첫 변분')
        source = next(n for n in maps['diff']['nodes'] if n['id']==edge['from'])
        self.assertEqual(source['audit']['state'],'incomplete')
        self.assertIn('partial',edge['stmt'])

    def test_atomic_cards_share_map_aliases_and_preserve_raw_references(self):
        maps,vertices = viewer.to_viewer(self.doc)
        card = next(e for e in vertices['FP_BIND']['edgesIn'] if e['rawId']=='fp-def-bind')
        edge = next(e for e in maps['fresh']['edges'] if e['id']=='fp-def-bind')
        self.assertEqual(card['id'],edge['displayId'])


if __name__ == '__main__':
    unittest.main()
