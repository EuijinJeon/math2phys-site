"""build.py 시험: 두 부모(main:theorem), 카드 수 중복, 섹션 지도의 가짜 순환.
실행: python3 -m unittest discover -s tools/tests -v   (redesign/ 에서)
"""
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fixture as F  # noqa: E402


def load_build():
    spec = importlib.util.spec_from_file_location("build_under_test", F.TOOLS / "build.py")
    B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(B)
    return B


def two_parent_cards():
    c = F.clone(F.base_cards())
    # main:theorem 은 reduction:section 과 model:section 두 섹션 카드의 자식
    c["model:section"]["children"] = ["x:fx-model-leaf", "main:theorem", "x:fx-model-remark"]
    # 증명 단계가 모형 쪽 카드를 쓴다(§2 → 주정리), 모형 쪽 주석이 주정리를 가리킨다(주정리 → §2). 카드 단위로는 순환이 아니다.
    c["main:theorem.s1"]["uses"].append("x:fx-model-leaf")
    c["x:fx-model-leaf"]["provides"] = "comp:bounded-lower, main:theorem.s1"
    c["x:fx-model-remark"] = F.card("x:fx-model-remark", "remark", "주정리가 말하지 않는 것", [("model.tex", 7, 7)],
                                    uses=["main:theorem"])
    return c


class TestTwoParents(unittest.TestCase):
    def setUp(self):
        self.B = load_build()
        self.C = self.B.C
        self.cards_dict = two_parent_cards()
        self.root = F.make_root(self.cards_dict)
        self.addCleanup(shutil.rmtree, self.root, True)
        self.cards = self.C.load_cards(self.root)
        self.S = self.B.Struct(self.cards, self.C.load_graph())

    def test_every_card_counted_exactly_once(self):
        total = sum(len(v) for v in self.S.members.values())
        self.assertEqual(total, len(self.cards_dict))
        seen = [i for v in self.S.members.values() for i in v]
        self.assertEqual(len(seen), len(set(seen)), "카드가 두 섹션에 겹쳐 센다")

    def test_main_bundle_is_separate(self):
        self.assertEqual(self.S.home("main:theorem"), "main")
        self.assertEqual(self.S.home("main:theorem.s1"), "main")
        self.assertIn("main:theorem", self.S.members["main"])
        self.assertNotIn("main:theorem", self.S.members["model"])
        self.assertNotIn("main:theorem", self.S.members["reduction"])
        self.assertEqual(sorted(self.S.parents["main:theorem"]), ["model:section", "reduction:section"])

    def test_remark_edges_do_not_make_section_cycles(self):
        agg, note = self.B.section_edges(self.S)
        self.assertIn(("model", "main"), agg)          # 증명 단계가 모형 카드를 쓴다
        self.assertIn(("main", "model"), note)         # 주석이 주정리를 가리킨다
        self.assertNotIn(("main", "model"), agg)
        text, aggl, mutual = self.B.section_map(self.S)
        self.assertEqual(mutual, [])
        self.assertEqual(self.B.sec_cycles(self.S, aggl), [])
        self.assertIn("주석", text)

    def test_section_card_uses_of_descendants_not_double_counted(self):
        # 섹션 카드의 uses 에는 자손(주정리)이 쓰는 것이 들어 있어도 섹션 간선으로 세지 않는다
        agg, _ = self.B.section_edges(self.S)
        self.assertNotIn(("comparison", "model"), agg)

    def test_pages_render_with_both_parents(self):
        out = Path(tempfile.mkdtemp(prefix="m2p-site-"))
        self.addCleanup(shutil.rmtree, out, True)
        r = subprocess.run([sys.executable, str(F.TOOLS / "build.py"), "--root", str(self.root), "--out", str(out)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        html = (out / "cards" / "main.theorem.html").read_text(encoding="utf-8")
        self.assertIn("model.section.html", html)
        self.assertIn("reduction.section.html", html)
        self.assertIn("map-main.html", html)
        for name in ("map.html", "map-main.html", "map-model.html", "map-reduction.html", "index.html"):
            self.assertTrue((out / name).is_file(), name)
        idx = (out / "index.html").read_text(encoding="utf-8")
        self.assertIn(f"카드 {len(self.cards_dict)}장을 한 번씩만 센다", idx)

    def test_empty_root_builds(self):
        root = F.make_root({})
        self.addCleanup(shutil.rmtree, root, True)
        out = Path(tempfile.mkdtemp(prefix="m2p-site-"))
        self.addCleanup(shutil.rmtree, out, True)
        r = subprocess.run([sys.executable, str(F.TOOLS / "build.py"), "--root", str(root), "--out", str(out)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)


class TestL2Site(unittest.TestCase):
    """layers/L2.md 를 사이트에 낸다. 없으면 아무것도 하지 않는다."""

    L1 = "# L1\n\n1. **수**\n   - 쓰는 규칙: P1, [P4](rules.md)\n"

    def build(self, **kw):
        root = F.make_root(F.base_cards(), rules=F.RULES3, glossary=F.GLOSSARY, **kw)
        self.addCleanup(shutil.rmtree, root, True)
        out = Path(tempfile.mkdtemp(prefix="m2p-site-"))
        self.addCleanup(shutil.rmtree, out, True)
        r = subprocess.run([sys.executable, str(F.TOOLS / "build.py"), "--root", str(root), "--out", str(out)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        return out

    def test_no_l2_does_nothing(self):
        out = self.build(l1=self.L1)
        self.assertFalse((out / "L2.html").exists())
        for name in ("index.html", "L1.html", "rules.html"):
            self.assertNotIn("L2.html", (out / name).read_text(encoding="utf-8"), name)

    def test_l2_page_and_path(self):
        out = self.build(l1=self.L1, l2=F.L2_BASE)
        self.assertTrue((out / "L2.html").is_file())
        idx = (out / "index.html").read_text(encoding="utf-8")
        i0, i1, i2 = (idx.index(f'href="{n}.html">{n}</a> →') for n in ("L0", "L1", "L2"))
        self.assertTrue(i0 < i1 < i2)
        self.assertIn('class="cur" href="L2.html"', (out / "L2.html").read_text(encoding="utf-8"))
        self.assertIn('href="L2.html">L2</a>', (out / "rules.html").read_text(encoding="utf-8"))   # 메뉴

    def test_rule_numbers_link_to_rule_rows_including_prime(self):
        out = self.build(l1=self.L1, l2=F.L2_BASE)
        t = (out / "L2.html").read_text(encoding="utf-8")
        for rid, anchor in (("P4", "rule-P4"), ("P6", "rule-P6"), ("P6′", "rule-P6p")):
            self.assertIn(f'href="rules.html#{anchor}" title="', t)
            self.assertIn(f">{rid}</a>", t)
        rules = (out / "rules.html").read_text(encoding="utf-8")
        for anchor in ("rule-P1", "rule-P4", "rule-P6", "rule-P6p"):
            self.assertIn(f'<tr id="{anchor}">', rules)
        # P6 링크가 P6′ 를 쪼개지 않는다
        self.assertNotIn('rule-P6">P6</a>′', t)
        # L1 의 `[P4](rules.md)` 와 맨 P1 도 행으로 이어진다
        l1 = (out / "L1.html").read_text(encoding="utf-8")
        self.assertIn('href="rules.html#rule-P1"', l1)
        self.assertIn('href="rules.html#rule-P4"', l1)

    def test_terms_and_cards_link(self):
        out = self.build(l2=F.L2_BASE)
        t = (out / "L2.html").read_text(encoding="utf-8")
        self.assertIn('class="gterm" href="glossary.html#g-pressure"', t)
        self.assertIn('class="node" href="cards/main.theorem.html"', t)

    def test_unknown_rule_is_marked_not_linked(self):
        out = self.build(l2=F.L2_BASE.replace("(P4)", "(P77)"))
        t = (out / "L2.html").read_text(encoding="utf-8")
        self.assertIn('class="gterm unknown" title="규칙 표에 없는 규칙: P77"', t)
        self.assertNotIn("rule-P77", t)

    def test_rule_number_in_math_or_code_is_left_alone(self):
        out = self.build(l2=F.L2_BASE.replace("그 증분의 근거는", "$P4$ 와 `P6` 는 글자이고 근거는"))
        t = (out / "L2.html").read_text(encoding="utf-8")
        self.assertIn("$P4$", t)
        self.assertIn("<code>P6</code>", t)


if __name__ == "__main__":
    unittest.main()
