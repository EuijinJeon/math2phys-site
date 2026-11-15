#!/usr/bin/env python3
"""check.py 의 입력 묶음 검사(check_bindings, 논문 전체 계약 [제안]) 회귀 시험.

    python3 redesign/proofmap/tools/test_bindings.py
"""
import copy
import importlib.util
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location("pm_check", Path(__file__).with_name("check.py"))
check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check)


def doc():
    need = lambda i, b, used=(3,): {"id": i, "what": i, "used_at": list(used), "binding": b}
    return {
        "format": "proofmap/0.1",
        "symbols": [{"id": "K", "tex": "$K$", "defined_at": "a.tex 1–2", "text": "kernel"}],
        "floors": [{"id": "cs", "kind": "standard", "statement": "Cauchy–Schwarz"},
                   {"id": "cit", "kind": "cited", "statement": "x", "cite": "\\cite{X}", "cited_at": "a.tex 4"}],
        "graphs": [{"id": "g", "nodes": [
            {"id": "A", "contract": {"source_label": "a:one", "outputs": [{"id": "r", "statement": "s", "lines": [1, 2]}]}},
            {"id": "B", "contract": {"source_label": "a:two", "outputs": [], "needs": [
                need("n1", {"type": "node", "node": "a:one", "item": "r"}),
                need("n2", {"type": "symbol", "symbol": "K"}),
                need("n3", {"type": "floor", "floor": "cs"}),
                need("n4", {"type": "floor", "floor": "cit"}),
                need("n5", {"type": "open", "why": "번호 없는 진술"}, used=()),
            ]}}], "edges": []}]}


def needs(d):
    return d["graphs"][0]["nodes"][1]["contract"]["needs"]


class T(unittest.TestCase):
    def run_b(self, d):
        return check.check_bindings(d)

    def test_clean(self):
        e, w, r = self.run_b(doc())
        self.assertEqual(e, [])
        self.assertEqual(len(w), 1)  # 열림 하나는 경고
        self.assertIn("open 1", r[0])

    def test_missing_item(self):
        d = doc(); needs(d)[0]["binding"]["item"] = "zz"
        self.assertTrue(any("항목" in x for x in self.run_b(d)[0]))

    def test_missing_node(self):
        d = doc(); needs(d)[0]["binding"]["node"] = "a:none"
        self.assertTrue(any("node" in x for x in self.run_b(d)[0]))

    def test_item_without_lines(self):
        d = doc(); del d["graphs"][0]["nodes"][0]["contract"]["outputs"][0]["lines"]
        self.assertTrue(any("원문 줄" in x for x in self.run_b(d)[0]))

    def test_missing_symbol(self):
        d = doc(); needs(d)[1]["binding"]["symbol"] = "Q"
        self.assertTrue(any("기호" in x for x in self.run_b(d)[0]))

    def test_cited_floor_needs_cite(self):
        d = doc(); del d["floors"][1]["cited_at"]
        self.assertTrue(any("인용" in x for x in self.run_b(d)[0]))

    def test_closed_needs_used_at(self):
        d = doc(); needs(d)[2]["used_at"] = []
        self.assertTrue(any("used_at" in x for x in self.run_b(d)[0]))

    def test_unknown_type(self):
        d = doc(); needs(d)[2]["binding"]["type"] = "guess"
        self.assertTrue(any("종류" in x for x in self.run_b(d)[0]))

    def test_old_needs_untouched(self):
        d = doc(); d["graphs"][0]["nodes"][1]["contract"]["needs"] = [{"from": "A", "items": ["r"]}]
        self.assertEqual(self.run_b(d), ([], [], []))


if __name__ == "__main__":
    unittest.main()
