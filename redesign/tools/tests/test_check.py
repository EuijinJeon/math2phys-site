"""check.py 시험: 기준 fixture 가 통과하고, 일부러 깨뜨린 카드를 검사가 잡는다.
실행: python3 -m unittest discover -s tools/tests -v   (redesign/ 에서)
"""
import shutil
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fixture as F  # noqa: E402


class CheckBase(unittest.TestCase):
    def run_case(self, cards, sections="reduction", **kw):
        root = F.make_root(cards, **kw)
        self.addCleanup(shutil.rmtree, root, True)
        return F.run_check(root, sections)

    def base(self):
        return F.clone(F.base_cards())


class TestBaseline(CheckBase):
    def test_base_passes_everything(self):
        res, errs, warns, code, out = self.run_case(self.base())
        self.assertEqual(code, 0, out)
        self.assertEqual(errs, [], errs)
        self.assertEqual(warns, [], warns)
        for name in ("정초", "포함", "의존", "대칭", "연결", "순환"):
            self.assertEqual(res[name][0], "통과", (name, res))

    def test_empty_root_does_not_crash(self):
        res, errs, warns, code, out = self.run_case({}, sections=None)
        self.assertEqual(code, 0, out)
        self.assertEqual(res["포함"][0], "해당 없음")
        self.assertEqual(res["대칭"][0], "해당 없음")


class TestMutations(CheckBase):
    """한 번에 한 곳만 깨뜨린다. 검사가 그 검사 이름으로 잡아야 한다."""

    def test_missing_uses_is_caught(self):
        c = self.base()
        c["main:theorem.s1"]["uses"].remove("comp:bounded-lower")
        c["reduction:section"]["uses"].remove("comp:bounded-lower")   # 조상의 uses 도 충족으로 치므로 함께 뺀다
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["의존"][0], "경고")
        self.assertTrue(any("reduction.tex:64" in w and "comp:bounded-lower" in w for w in warns), warns)
        self.assertTrue(any("reduction.tex:76" in w for w in warns), warns)
        self.assertTrue(any("reduction.tex:4 " in w for w in warns), warns)

    def test_ancestor_uses_cover_descendants(self):
        # 알려진 성질(약점): 조상 카드의 uses 에 있으면 자손이 안 적어도 통과한다. SCHEMA 의 "조상·자손의 uses".
        c = self.base()
        c["main:theorem.s1"]["uses"].remove("comp:bounded-lower")
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["의존"][0], "통과")

    def test_missing_uses_for_equation_in_other_card(self):
        c = self.base()
        c["reduction:stability"]["uses"].remove("model:integrability")
        res, errs, warns, code, out = self.run_case(c)
        self.assertTrue(any("reduction.tex:11" in w and "model:integrability" in w for w in warns), warns)

    def test_cycle_is_caught(self):
        c = self.base()
        c["reduction:stability.s1"]["uses"] = ["main:theorem.s1"]
        c["main:theorem.s1"]["uses"] += ["reduction:stability.s1"]
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(code, 1)
        self.assertEqual(res["순환"][0], "실패")
        self.assertTrue(any("uses 순환" in e for e in errs), errs)

    def test_self_loop_is_caught(self):
        c = self.base()
        c["reduction:stability.s2"]["uses"] = ["reduction:stability.s2"]
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["순환"][0], "실패")

    def test_children_cycle_is_caught(self):
        c = self.base()
        c["reduction:stability.s2"]["children"] = ["reduction:stability"]
        res, errs, warns, code, out = self.run_case(c)
        self.assertTrue(any("children 순환" in e for e in errs), errs)

    def test_source_gap_in_proof_is_caught(self):
        c = self.base()
        c["reduction:stability.s2"]["source"] = [("reduction.tex", 39, 41)]   # 42-43 가 빠진다
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(code, 1)
        self.assertEqual(res["포함"][0], "실패")
        self.assertTrue(any("reduction.tex:42-43" in e for e in errs), errs)

    def test_missing_leaf_is_caught(self):
        c = self.base()
        del c["main:theorem.s1"]
        c["main:theorem"]["children"] = []
        c["main:theorem"]["source"] = [("model.tex", 130, 136)]
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["포함"][0], "실패")
        self.assertTrue(any("reduction.tex:45-59" in e and "Theorem 2.1" in e for e in errs), errs)

    def test_statement_gap_is_caught(self):
        c = self.base()
        c["reduction:stability"]["source"] = [("reduction.tex", 9, 20)]   # 진술 21-26 빠짐
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["포함"][0], "실패")
        self.assertTrue(any("reduction.tex:21-26" in e for e in errs), errs)

    def test_statement_covered_by_non_leaf_is_accepted(self):
        # 완화 1: 진술 줄은 잎이 아닌 카드가 덮어도 된다. 기준 fixture 에서 이미 그렇다(reduction:stability 는 부모).
        res, errs, warns, code, out = self.run_case(self.base())
        self.assertEqual(res["포함"][0], "통과")

    def test_proof_covered_only_by_non_leaf_is_caught(self):
        # 증명 줄은 잎이 덮어야 한다. 부모 카드가 덮는 것으로는 부족하다.
        c = self.base()
        c["reduction:stability.s2"]["source"] = [("reduction.tex", 39, 39)]
        c["reduction:stability"]["source"] = [("reduction.tex", 9, 26), ("reduction.tex", 40, 43)]
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["포함"][0], "실패")

    def test_source_out_of_file_is_caught(self):
        c = self.base()
        c["reduction:stability.s2"]["source"] = [("reduction.tex", 39, 4000)]
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["정초"][0], "실패")

    def test_missing_source_is_caught(self):
        c = self.base()
        c["reduction:stability.s2"]["source"] = []
        root = F.make_root(c)
        self.addCleanup(shutil.rmtree, root, True)
        # 빈 source 는 YAML 에서 `source:` 뒤에 항목이 없는 꼴이 된다.
        res, errs, warns, code, out = F.run_check(root)
        self.assertEqual(res["정초"][0], "실패")
        self.assertTrue(any("source가 없다" in e for e in errs), errs)

    def test_unknown_uses_is_caught(self):
        c = self.base()
        c["main:theorem.s1"]["uses"].append("nope:does-not-exist")
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["연결"][0], "실패")
        self.assertTrue(any("nope:does-not-exist" in e for e in errs), errs)

    def test_unknown_child_is_caught(self):
        c = self.base()
        c["reduction:stability"]["children"].append("reduction:stability.s9")
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["연결"][0], "실패")

    def test_unknown_wiki_link_is_caught(self):
        c = self.base()
        c["reduction:section"]["body"] += " [[nope:missing]]"
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["연결"][0], "실패")

    def test_physics_without_gap_is_caught(self):
        c = self.base()
        c["reduction:stability"]["extra"] = "xtra: 1"
        root = F.make_root(c)
        self.addCleanup(shutil.rmtree, root, True)
        p = root / "cards" / "reduction.stability.md"
        t = p.read_text(encoding="utf-8").replace("physics: null", "physics: '물리 문장'").replace("gap: null", "gap: null")
        p.write_text(t, encoding="utf-8")
        res, errs, warns, code, out = F.run_check(root)
        self.assertEqual(res["사전"][0], "실패")

    def test_broken_front_matter_is_reported_not_crash(self):
        c = self.base()
        root = F.make_root(c)
        self.addCleanup(shutil.rmtree, root, True)
        (root / "cards" / "x.broken.md").write_text("머리말 없음\n", encoding="utf-8")
        res, errs, warns, code, out = F.run_check(root)
        self.assertEqual(code, 1, out)
        self.assertEqual(res["형식 (머리말)"][0], "실패")

    def test_duplicate_id_is_caught(self):
        c = self.base()
        root = F.make_root(c)
        self.addCleanup(shutil.rmtree, root, True)
        t = (root / "cards" / "reduction.stability.s2.md").read_text(encoding="utf-8")
        (root / "cards" / "x.dup.md").write_text(t, encoding="utf-8")   # 같은 id, 파일 이름만 다르다
        res, errs, warns, code, out = F.run_check(root)
        self.assertEqual(res["형식 (머리말)"][0], "실패")


class TestSectionLabelRelaxation(CheckBase):
    """HANDOFF 4절 완화 3: 섹션 라벨 참조는 그 섹션 카드의 자손이 uses 에 있으면 충족. comparison.tex 227 이 시험 대상."""

    def test_descendant_in_uses_satisfies(self):
        res, errs, warns, code, out = self.run_case(self.base())
        self.assertFalse(any("comparison.tex:227" in w for w in warns), warns)

    def test_ancestor_uses_also_count(self):
        # 자손을 부모 카드의 uses 에 넣어도 된다(조상의 uses 를 합친다)
        c = self.base()
        c["comp:section"]["uses"] = ["x:fx-model-leaf"]
        c["comp:bounded-lower"]["uses"] = []
        res, errs, warns, code, out = self.run_case(c)
        self.assertFalse(any("comparison.tex:227" in w for w in warns), warns)

    def test_no_descendant_in_uses_still_warns(self):
        c = self.base()
        c["comp:bounded-lower"]["uses"] = []
        res, errs, warns, code, out = self.run_case(c)
        self.assertTrue(any("comparison.tex:227" in w and "model:section" in w for w in warns), warns)

    def test_unrelated_card_in_uses_still_warns(self):
        # 그 섹션의 자손이 아닌 카드를 넣어서는 충족되지 않는다
        c = self.base()
        c["comp:bounded-lower"]["uses"] = ["x:fx-up"]
        res, errs, warns, code, out = self.run_case(c)
        self.assertTrue(any("comparison.tex:227" in w and "model:section" in w for w in warns), warns)

    def test_relaxation_is_only_for_section_labels(self):
        # 정리·식 라벨 참조는 자손으로 대신할 수 없다: main:theorem.s1 이 upper:bound 를 uses 에서 빼면 경고
        c = self.base()
        c["main:theorem.s1"]["uses"].remove("upper:bound")
        res, errs, warns, code, out = self.run_case(c)
        self.assertTrue(any("reduction.tex:85" in w and "upper:bound" in w for w in warns), warns)


class TestSymmetry(CheckBase):
    def test_provides_without_uses_warns(self):
        c = self.base()
        c["reduction:stability"]["uses"].remove("x:fx-up")     # x:fx-up.provides 는 reduction:stability 를 가리킨다
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["대칭"][0], "경고")
        self.assertEqual(code, 0, "대칭은 경고만 낸다")
        self.assertTrue(any("`x:fx-up`.provides" in w and "`reduction:stability`" in w for w in warns), warns)

    def test_uses_without_provides_warns(self):
        c = self.base()
        c["x:fx-up"]["provides"] = ""                            # 주는 쪽이 적지 않았고, 섹션 표도 없다
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(res["대칭"][0], "경고")
        self.assertEqual(code, 0)
        self.assertTrue(any("`reduction:stability`.uses 의 `x:fx-up`" in w for w in warns), warns)

    def test_section_table_declaration_is_enough(self):
        # 주는 쪽 provides 대신 받는 쪽 섹션 카드의 표(본문)가 주는 쪽을 가리키면 선언으로 본다
        c = self.base()
        c["x:fx-up"]["provides"] = ""
        c["reduction:section"]["body"] += " 밖에서 받는 것: [[x:fx-up]]"
        res, errs, warns, code, out = self.run_case(c)
        self.assertFalse(any("x:fx-up" in w for w in warns), warns)

    def test_same_section_is_not_checked(self):
        c = self.base()
        c["reduction:stability.s1"]["provides"] = "reduction:stability.s2"   # uses 에 없지만 같은 섹션
        res, errs, warns, code, out = self.run_case(c)
        self.assertEqual(warns, [], warns)

    def test_overview_cards_are_exempt(self):
        c = self.base()
        c["x:overview-fx"] = F.card("x:overview-fx", "remark", "예고", [("upper.tex", 5, 5)],
                                    uses=["x:fx-up"])
        res, errs, warns, code, out = self.run_case(c)
        self.assertFalse(any("x:overview-fx" in w for w in warns), warns)


if __name__ == "__main__":
    unittest.main()
