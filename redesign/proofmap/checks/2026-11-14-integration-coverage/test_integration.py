"""참조 연결, 중복, 미변환, 묵은 검토를 혼동하지 않는 결함 주입 시험."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
s=importlib.util.spec_from_file_location('viewer',ROOT/'tools/build_viewer.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.doc=json.loads((ROOT/'graphs/move4.json').read_text())
        self.graphs={g['id']:g for g in self.doc['graphs']}
    def node(self,g,n):
        return next(x for x in self.graphs[g]['nodes'] if x['id']==n)
    def status(self):
        return v.integration.integration_status(self.doc,v.contracts)
    def test_common_input_does_not_supply_kernel(self):
        self.assertEqual(self.node('fv','XSET')['statement_ref']['clauses'],['setting','insertion'])
        self.assertEqual(self.node('cp','XS')['statement_ref']['clauses'],['setting','insertion'])
        self.assertEqual(self.node('cp','XK')['statement_ref']['clauses'],['kernel'])
    def test_kernel_explicitly_reaches_each_cp_vertex(self):
        for nid in ['BASE','JOIN','IDENT']:
            self.assertIn('XK',self.node('cp',nid)['inputs'])
    def test_strict_imports_match_without_overlaps(self):
        for gid in ['fv','cp']:
            c=self.status()['graphs'][gid]
            self.assertEqual(c['matched'],c['totalImports'])
            self.assertFalse(c['overlaps'])
    def test_injected_duplicate_is_detected(self):
        self.node('fv','XSET')['statement_ref']['clauses'].append('kernel')
        c=self.status()['graphs']['fv']
        self.assertTrue(any(o['items']==['kernel'] for o in c['overlaps']))
    def test_wrong_parent_edge_is_conflict(self):
        self.node('fv','XSET')['import_edge']='missing'
        i=self.status()['nodes'][('fv','XSET')]['imports']
        self.assertTrue(i['tracked']);self.assertFalse(i['matched'])
    def test_body_alignment_pending_is_preserved(self):
        c=self.status()
        self.assertTrue(c['nodes'][('top','O1')]['pending'])
        self.assertTrue(c['nodes'][('diff','XO')]['pending'])
        self.assertTrue(c['nodes'][('fv','XSET')]['imports']['upstreamPending'])
    def test_legacy_graphs_not_claimed_converted(self):
        for gid in ['top','p7','diff','fresh']:
            self.assertIn('미변환',self.status()['graphs'][gid]['mode'])
    def test_derived_output_not_mistaken_for_legacy_given_body(self):
        self.assertFalse(self.status()['nodes'][('diff','D2')]['pending'])
    def test_claude_edges_and_review_warnings_remain(self):
        c=self.status()['graphs']
        self.assertEqual(c['top']['totalEdges'],17)
        self.assertEqual(c['p7']['totalEdges'],27)
        self.assertEqual(c['diff']['totalEdges'],15)
        self.assertIn('diff-e11',c['diff']['reviewEdges'])
    def test_viewer_exposes_coverage(self):
        maps,_=v.to_viewer(self.doc)
        self.assertEqual(maps['fv']['coverage']['overlaps'],[])
        n=next(n for n in maps['fv']['nodes'] if n['id']=='XSET')
        self.assertEqual(n['coverage']['imports']['parentEdge'],'diff-e9')

if __name__=='__main__':unittest.main()
