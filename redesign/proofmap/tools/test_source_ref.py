#!/usr/bin/env python3
"""SPEC 7.8 원문 참조 판의 회귀 시험. 메모리의 작은 graph로 check() 를 돌린다(파일은 바꾸지 않는다).

    python3 redesign/proofmap/tools/test_source_ref.py
"""
import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('chk', Path(__file__).with_name('check.py'))
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)

BASE = {
    "format": "proofmap/0.1", "id": "t", "title": "t", "language": "ko",
    "graphs": [
        {"id": "top", "title": "top", "parent": None,
         "nodes": [
             {"id": "X", "kind": "external", "title": "X", "contract": {"outputs": [{"id": "a", "statement": "$a>0$.", "lines": [1, 1]}]}},
             {"id": "P", "kind": "step", "title": "P", "inputs": ["X"], "subgraph": "p", "status": "sketch",
              "contract": {"outputs": [{"id": "out", "statement": "$b>0$.", "lines": [5, 6]}]}},
             {"id": "Q", "kind": "step", "title": "Q", "inputs": ["P"], "status": "sketch"}],
         "edges": [
             {"id": "e0", "from": "X", "to": "P", "kind": "call", "carries": [{"node": "X", "item": "a", "used_at": [3]}], "status": "connected"},
             {"id": "e1", "from": "P", "to": "Q", "kind": "flow", "carries": [{"node": "P", "item": "out", "used_at": [9]}], "status": "connected"}]},
        {"id": "p", "title": "p", "parent": {"graph": "top", "node": "P"},
         "nodes": [
             {"id": "x", "kind": "external", "title": "x", "external_ref": "X", "import_edge": "e0", "items": ["a"]},
             {"id": "k1", "kind": "step", "title": "k1", "lines": [3, 4], "status": "complete",
              "source_derivation": {"uses": ["s1"]}, "produces": [{"edge": "s2", "by": "4행"}],
              "author_filled": [{"what": "곱이 양수"}]},
             {"id": "o", "kind": "output", "title": "o", "output_items": ["out"]}],
         "edges": [
             {"id": "s1", "from": "x", "to": "k1", "kind": "call", "carries": ["a"], "used_at": [3]},
             {"id": "s2", "from": "k1", "to": "o", "kind": "flow", "carries": ["result"], "used_at": [5]}]}]}


def errors(doc):
    return [e for e in chk.check(doc)[0] if "[p]" in e]


class SourceRefTests(unittest.TestCase):
    def test_base_is_clean(self):
        self.assertEqual(errors(BASE), [])

    def test_edges_become_content_complete(self):
        doc = chk.carries.resolve(BASE)
        es = {e["id"]: e for e in doc["graphs"][1]["edges"]}
        self.assertTrue(es["s1"]["complete"]); self.assertEqual(es["s1"]["content_ref"], "item")
        self.assertIn("$a>0$", es["s1"]["statement"])
        self.assertTrue(es["s2"]["complete"]); self.assertEqual(es["s2"]["content_ref"], "source")

    def test_missing_use_is_error(self):
        d = copy.deepcopy(BASE); d["graphs"][1]["nodes"][1]["source_derivation"]["uses"] = []
        self.assertTrue(any("SOURCE_REF" in e and "s1" in e for e in errors(d)))

    def test_stray_use_is_error(self):
        d = copy.deepcopy(BASE); d["graphs"][1]["nodes"][1]["source_derivation"]["uses"] = ["s1", "zz"]
        self.assertTrue(any("받지 않는 edge" in e for e in errors(d)))

    def test_missing_produces_is_error(self):
        d = copy.deepcopy(BASE); d["graphs"][1]["nodes"][1]["produces"] = []
        self.assertTrue(any("produces" in e for e in errors(d)))

    def test_unresolvable_item_keeps_edge_incomplete(self):
        d = copy.deepcopy(BASE); d["graphs"][1]["edges"][0]["carries"] = ["nope"]
        self.assertTrue(any("내용을 다 싣지 않는다" in e and "s1" in e for e in errors(d)))

    def test_bad_lines_is_error(self):
        d = copy.deepcopy(BASE); d["graphs"][1]["nodes"][1]["lines"] = [9, 3]
        self.assertTrue(any("lines" in e for e in errors(d)))

    def test_without_source_derivation_complete_is_still_error(self):
        d = copy.deepcopy(BASE); del d["graphs"][1]["nodes"][1]["source_derivation"]
        self.assertTrue(any("derivation 도 subgraph 도 없다" in e for e in errors(d)))


if __name__ == "__main__":
    unittest.main()
