"""국소 참조 검사의 결함 주입 시험. 표준 라이브러리만 사용한다."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('proofmap_check', ROOT / 'tools/check.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LocalReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads((ROOT / 'graphs/move4.json').read_text())

    def setUp(self):
        self.doc = copy.deepcopy(self.baseline)
        self.fv = next(g for g in self.doc['graphs'] if g['id'] == 'fv')
        self.pm = next(n for n in self.fv['nodes'] if n['id'] == 'PM')
        self.cp = next(g for g in self.doc['graphs'] if g['id'] == 'cp')
        self.ident = next(n for n in self.cp['nodes'] if n['id'] == 'IDENT')

    def assert_error(self, code):
        errors, _, _ = checker.check(self.doc)
        self.assertTrue(any(code in e for e in errors), errors)

    def test_baseline_and_coverage(self):
        errors, warnings, report = checker.check(self.doc)
        self.assertEqual((errors, warnings), ([], []))
        self.assertEqual(sum('명시 참조:' in r for r in report), 8)
        self.assertTrue(any('K_A←edge:e2' in r for r in report))
        self.assertTrue(any('h←line:1' in r for r in report))

    def test_deleted_definition_edge(self):
        self.fv['edges'] = [e for e in self.fv['edges'] if e['id'] != 'e2']
        self.assert_error('[REF_SCOPE]')
        self.assert_error('[SYMBOL_UNDEFINED]')

    def test_definition_removed_but_edge_remains(self):
        source=next(n for g in self.doc['graphs'] if g['id']=='top' for n in g['nodes'] if n['id']=='O1')
        source['outputs']['fv_inputs']['clauses']['kernel']['defines']=[]
        self.assert_error('[SYMBOL_UNDEFINED]')

    def test_nonincoming_edge_is_not_usable(self):
        self.pm['derivation'][0]['uses'].append('edge:f2')
        self.assert_error('[REF_SCOPE]')

    def test_edge_ids_are_exact_not_substrings(self):
        self.pm['derivation'][0]['uses'].append('edge:e10')
        self.assert_error('[REF_SCOPE]')

    def test_other_graph_context_is_not_in_scope(self):
        self.pm['derivation'][0]['uses'].append('context:CF')
        self.assert_error('[REF_SCOPE]')

    def test_shared_premise_edge_must_reach_node(self):
        self.fv['edges']=[e for e in self.fv['edges'] if e['id']!='g2']
        self.assert_error('[REF_SCOPE]')
        self.assert_error('[SYMBOL_UNDEFINED]')

    def test_future_line_cannot_be_used(self):
        self.pm['derivation'][0]['uses'].append('line:2')
        self.assert_error('[REF_SCOPE]')

    def test_current_line_is_not_a_prior_premise(self):
        self.pm['derivation'][0]['uses'].append('line:1')
        self.assert_error('[REF_SCOPE]')

    def test_nonexistent_floor(self):
        self.pm['derivation'][0]['uses'].append('floor:3')
        self.assert_error('[REF_SCOPE]')

    def test_symbol_cannot_be_defined_in_a_later_line(self):
        self.ident['derivation'][0].pop('defines')
        self.ident['derivation'][1]['defines'] = ['h']
        self.assert_error('[SYMBOL_UNDEFINED]')

    def test_deleted_local_definition(self):
        self.ident['derivation'][0].pop('defines')
        self.assert_error('[SYMBOL_UNDEFINED]')

    def test_unused_edge_not_hidden_by_prose_mention(self):
        for line in self.pm['derivation']:
            line['uses'] = [r for r in line['uses'] if r != 'edge:e3']
        _, warnings, _ = checker.check(self.doc)
        self.assertTrue(any('[EDGE_UNUSED]' in w and "'e3'" in w for w in warnings))

    def test_malformed_reference_reports_error(self):
        self.pm['derivation'][0]['uses'] = [123]
        self.assert_error('[REF_FORMAT]')

    def test_missing_symbol_inventory_reports_error(self):
        self.pm['derivation'][0].pop('uses_symbols')
        self.assert_error('[REF_FORMAT]')

    def test_output_cannot_reference_nonexistent_line(self):
        self.pm['produces'][0]['lines'] = [7]
        self.assert_error('[OUTPUT_LINES]')

    def test_output_boolean_is_not_a_line_number(self):
        self.pm['produces'][0]['lines'] = [True]
        self.assert_error('[OUTPUT_LINES]')

    def test_produces_must_be_an_actual_output(self):
        self.pm['produces'].append({'edge': 'f1', 'by': '식 1', 'lines': [1]})
        self.assert_error('[OUTPUT_SCOPE]')

    def test_legacy_derivation_is_explicitly_unchecked(self):
        self.pm.pop('reference_check')
        errors, _, report = checker.check(self.doc)
        self.assertFalse(errors)
        self.assertTrue(any('node PM: 명시 기호·참조 미검사' in r for r in report))

    def test_duplicate_context_ids_are_rejected(self):
        c={'id':'ILLEGAL','text':'test','nodes':['PM']}
        self.fv['contexts']=[c,copy.deepcopy(c)]
        self.assert_error('context id가 겹친다')

    def test_cli_fails_on_deleted_definition_and_reports_the_symbol(self):
        self.fv['edges'] = [e for e in self.fv['edges'] if e['id'] != 'e2']
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'deleted-edge.json'
            path.write_text(json.dumps(self.doc))
            result = subprocess.run([sys.executable, str(ROOT / 'tools/check.py'), str(path)],
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('[SYMBOL_UNDEFINED]', result.stdout)
        self.assertIn("'K_A'", result.stdout)


if __name__ == '__main__':
    unittest.main()
