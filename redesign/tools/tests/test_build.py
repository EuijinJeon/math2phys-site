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


if __name__ == "__main__":
    unittest.main()
