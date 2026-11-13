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


class TestL2(CheckBase):
    """물리판 검사 (layers/L2.md)."""

    def l2(self, text, rules=F.RULES3, glossary=F.GLOSSARY, cards=None):
        res, errs, warns, code, out = self.run_case(cards or self.base(), rules=rules, l2=text, glossary=glossary)
        rep = Path(self.last_root, "build", "check-report.md").read_text(encoding="utf-8")
        sec = rep.split("## 물리판")[1].split("\n## ")[0] if "## 물리판" in rep else ""
        return res, code, [x[len("- 오류: "):] for x in sec.splitlines() if x.startswith("- 오류: ")], \
            [x[len("- 경고: "):] for x in sec.splitlines() if x.startswith("- 경고: ")], \
            [x[len("- 참고: "):] for x in sec.splitlines() if x.startswith("- 참고: ")], rep

    def run_case(self, cards, sections="reduction", **kw):
        root = F.make_root(cards, **kw)
        self.addCleanup(shutil.rmtree, root, True)
        self.last_root = root
        return F.run_check(root, sections)

    def test_no_l2_is_not_applicable(self):
        res, errs, warns, code, out = self.run_case(self.base())
        self.assertEqual(res["물리판"][0], "해당 없음")
        self.assertEqual(code, 0)

    def test_base_l2_passes(self):
        res, code, e, w, n, rep = self.l2(F.L2_BASE)
        self.assertEqual((e, w), ([], []), (e, w))
        self.assertEqual(res["물리판"][0], "통과")
        self.assertEqual(code, 0)
        self.assertTrue(any("쓰지 않은 것 1개: P1" in x for x in n), n)       # 참고: P1 은 안 쓰였다
        self.assertTrue(any("단락 4개 중 규칙·링크 없음 0개" in x for x in n), n)

    def test_unknown_rule_id_is_error(self):
        res, code, e, w, n, _ = self.l2(F.L2_BASE.replace("(P6′)", "(P6′, P77)"))
        self.assertEqual(res["물리판"][0], "실패")
        self.assertEqual(code, 1)
        self.assertTrue(any("P77" in x and "rules.md 에 없다" in x for x in e), e)
        self.assertFalse(any("P6′" in x for x in e), e)       # 프라임 규칙은 존재한다

    def test_prime_is_distinct_from_plain(self):
        rules = F.RULES3.replace("| P6′ |", "| P6x |")        # P6′ 를 표에서 뺀다
        res, code, e, w, n, _ = self.l2(F.L2_BASE, rules=rules)
        self.assertTrue(any("P6′ 가 rules.md 에 없다" in x for x in e), e)
        self.assertFalse(any("P6 가 rules.md" in x for x in e), e)

    def test_rule_followed_by_korean_particle(self):
        res, code, e, w, n, _ = self.l2(F.L2_BASE.replace("(P4). 그", "P99를 쓴다. 그"))
        self.assertTrue(any("P99" in x for x in e), e)

    def test_unresolved_links_are_errors(self):
        t = F.L2_BASE.replace("[[main:theorem]]", "[[main:nothing]]").replace("[[g:pressure]]", "[[g:nope]]")
        res, code, e, w, n, _ = self.l2(t)
        self.assertTrue(any("[[main:nothing]]" in x for x in e), e)
        self.assertTrue(any("[[g:nope]]" in x for x in e), e)
        self.assertEqual(code, 1)

    def test_graph_node_without_card_resolves(self):
        # 카드가 없어도 graph.json 의 노드면 풀린다 (model:positivity 는 fixture 에 카드가 없다)
        res, code, e, w, n, _ = self.l2(F.L2_BASE.replace("[[reduction:stability]]", "[[model:positivity]]"))
        self.assertEqual(e, [], e)

    def test_missing_section_rule_line_warns(self):
        t = F.L2_BASE.replace("\n이 절이 쓰는 규칙: 없음\n", "\n")
        res, code, e, w, n, _ = self.l2(t)
        self.assertEqual(res["물리판"][0], "경고")
        self.assertEqual(code, 0)
        self.assertTrue(any("둘째 절" in x and "줄이 없다" in x for x in w), w)

    def test_section_rule_set_mismatch_warns(self):
        t = F.L2_BASE.replace("이 절이 쓰는 규칙: P4, P6, P6′", "이 절이 쓰는 규칙: P4, P1")
        res, code, e, w, n, _ = self.l2(t)
        self.assertEqual(code, 0)
        msg = [x for x in w if "첫 절" in x]
        self.assertEqual(len(msg), 1, w)
        self.assertIn("줄에만: P1", msg[0])
        self.assertIn("본문에만: P6, P6′", msg[0])

    def test_bare_paragraph_warns_but_math_list_head_blank_do_not(self):
        t = F.L2_BASE.replace("## 둘째 절\n", "## 둘째 절\n\n이 문장은 규칙도 링크도 없이 그냥 쓴 단락이다.\n")
        res, code, e, w, n, _ = self.l2(t)
        bare = [x for x in w if "규칙 번호도 [[링크]]도 없는" in x]
        self.assertEqual(len(bare), 1, w)
        self.assertIn("둘째 절", bare[0])
        self.assertIn("이 문장은 규칙도 링크도", bare[0])
        # 줄 번호가 실제 줄을 가리킨다
        ln = int(bare[0].split("줄 ")[1].split(" ")[0])
        self.assertIn("이 문장은", t.split("\n")[ln - 1])

    def test_rule_inside_math_or_code_does_not_count(self):
        t = F.L2_BASE.replace("그 증분의 근거는", "그 증분은 $P9$ 와 `P8` 로 쓰지 않고, 근거는")
        res, code, e, w, n, _ = self.l2(t)
        self.assertEqual(e, [], e)
        self.assertEqual(w, [], w)

    def test_paragraph_with_only_g_link_counts_as_linked(self):
        t = F.L2_BASE.replace("## 둘째 절\n", "## 둘째 절\n\n이 문장은 용어 [[g:pressure]] 만 가리키는 단락이다.\n")
        res, code, e, w, n, _ = self.l2(t)
        self.assertEqual(w, [], w)

    def test_preamble_before_first_section_is_exempt(self):
        t = F.L2_BASE.replace("**바닥**: 시험용 바닥.", "**바닥**: 시험용 바닥이고 아무 링크도 규칙도 없는 긴 문장이다.")
        res, code, e, w, n, _ = self.l2(t)
        self.assertEqual(w, [], w)

    def test_bad_title_warns(self):
        res, code, e, w, n, _ = self.l2(F.L2_BASE.replace("# L2 — 물리판", "# 물리판"))
        self.assertTrue(any("첫 줄" in x for x in w), w)

    def test_without_rules_table_rule_ids_not_judged(self):
        res, code, e, w, n, _ = self.l2(F.L2_BASE, rules=None)
        self.assertEqual(e, [], e)


if __name__ == "__main__":
    unittest.main()
