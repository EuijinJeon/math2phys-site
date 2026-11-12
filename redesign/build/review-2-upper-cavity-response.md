# 검토 2 대응 — §4 upper, §5 cavity

대상 검토: `build/review-2-upper-cavity.md` (지적 12건, ❓ 세 곳, (a)–(e)).
기준: `source/sections/upper.tex`, `cavity.tex`, 그리고 지적이 인용한 `trees.tex` 51–140, `comparison.tex` 1–30·158–230, `perturbations.tex` 1–10·58–61·265–280, `model.tex` 66–72·116–121, `overview.tex` 37–41, `reduction.tex` 17–20. 지적마다 원문 줄을 직접 열어 대조했다.

## 요약

| 판정 | 건수 | 번호 |
|---|---|---|
| 반영 | 11 | F1, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12 |
| 좁혀서 반영 | 1 | F2 |
| 기각 | 0 | — |

추가로 반영한 것: ❓ 세 곳, (a), (b)(F5와 함께), (c), (d), (e).

검사: `python3 redesign/tools/check.py --sections decorrelation,model,trees,upper,cavity --out /tmp/check-uc-fix.md` 결과 9개 검사 모두 통과, 오류 0, 경고 0. 반영 전에는 용어 검사에서 오류 2건(`[[g:bounded-law]]` 미등록)이 있었다. `pert.*`, `x.pert-*` 에서 난 오류는 없다.

## 건별 표

| 번호 | 판정 | 한 줄 근거 | 고친 파일 |
|---|---|---|---|
| F1 | 반영 (가: 물리 문장에 오차를 넣고 `exact` 유지) | cavity.tex 76·79·83의 $O(N^{-1})$, 101–103의 $O(N^{-1/4})$. 고치기 전의 물리 문장은 오차 없는 등식이었다 | `cavity.increment.s1.md`, `cavity.increment.s3.md` |
| F2 | 좁혀서 반영 (`tree:insertion` 쪽으로 맞춤) | 단조성은 trees.tex 107–110(`tree:insertion`)에만 진술된다. `tree:original-tilt`(51–65)에는 단조성 진술이 없다. 주는 쪽(`tree:insertion` provides, `tree:insertion.s3` provides, `tree:section` 표)은 이미 맞아서 받는 쪽만 고쳤다 | `cavity.negligible.md`, `cavity.increment.s2.md`, `cavity.section.md` |
| F3 | 반영 | cavity.tex 112–113의 "Together with the coupling estimate"는 (5.5), 곧 s3의 결론을 쓴다. s3은 s4를 쓰지 않으므로 순환이 없다 | `cavity.increment.s4.md` |
| F4 | 반영 | cavity 상호작용은 보간된 계에 없던 새 message label을 쓴다(upper.tex 40). 증분을 $\log Y_0$ 로 읽는 데 trees.tex 135–140이 필요하다 | `upper.bound.s3.md` |
| F5 | 반영 | 시행 message의 moment 조건 없이 $\mathbb E\log T_0V_{\rm s}$ 가 유한하다는 것(upper.tex 7–8, 48)은 model.tex 122–128에서 온다. `model:trial-bounds` 는 `model:*` 만 쓰므로 순환이 없다 | `upper.bound.s2.md`, `model.trial-bounds.md`(provides) |
| F6 | 반영 | upper.tex 33–34 "All moments used below are therefore finite"를 (4.3)이 직접 쓴다. `upper:bound.s1` 은 `model:*` 만 쓰므로 순환이 없다. 쓰이지 않던 `model:integrability` 는 뺐다(96–126에 해당 참조가 없고, 지배 함수는 `upper:regularization` 의 일이다) | `upper.remainder.md` |
| F7 | 반영 | upper.tex 51 "expected insertion increment"이므로 부등식은 기대값에 대한 것이다. "모든 $t\in(0,1)$"에는 작성자 보탬 표시를 붙였다(55행에서 온 범위) | `upper.derivative.md` |
| F8 | 반영 | upper.tex 38–39: site마다 평균 $(1-t)\alpha p$ 개의 cavity 상호작용이 있고 그 각각이 $p-1$ 개의 message를 쓴다 | `upper.bound.s2.md` |
| F9 | 반영 | cavity.tex 6–7 "to obtain identities for its spin trees". 이 기회에 "유계 섭동"을 "값이 $[1/2,3/2]$ 안인"으로 바꿔 `g:bounded-law` 와 헷갈리지 않게 했다 | `cavity.section.md` |
| F10 | 반영 | `upper:section` 의 문장이 낡았다. `cavity:section` 의 내주는 표에 comparison.tex 13–14, 162, 200, 215–216 행을 더했다. `cavity:increment.s4` 의 provides에 215–216을 더했다. `tree:section` 표는 (a)에서 다룬다 | `upper.section.md`, `cavity.section.md`, `cavity.increment.s4.md`, `tree.section.md` |
| F11 | 반영 | cavity.tex 95–96: $\log2$ 는 섭동 factor의 한계 (5.2)에서 오고, $B$ 는 $B(\theta)\le B$ 에서 온다. "bounded"는 원문에서 두 뜻으로 쓰인다(6행의 "bounded perturbations"와 11행의 가정) | `layers/glossary.md` |
| F12 | 반영 | "계층 free entropy"는 `g:root-logarithm` 의 물리 대응에만 나오는 말이다. 각 카드에서 처음 나오는 곳에 링크를 걸었다 | `cavity.increment.md`, `cavity.increment.s3.md`, `upper.bound.s2.md` |

## 좁힘의 상세: F2

검토자는 두 길 가운데 하나로 한쪽에 맞추라고 했다. 원문을 대조한 결과는 다음과 같다.

- cavity.tex 36–37 "Comparing pointwise with the unperturbed spin weight and then applying the recursion"과 95–96 "Deleting or adding a perturbation changes the root logarithm by at most $\log2$"는 어느 결과도 `\ref` 하지 않는다.
- 논문에서 recursion의 단조성이 진술된 곳은 trees.tex 107–110(`tree:insertion` 의 마지막 문단) 하나다. 증명은 131–132의 "backward induction in (tree:Y-recursion)"이다.
- `tree:original-tilt` 의 원문(trees.tex 51–65)은 $X$-recursion과 tilted kernel을 정의하고 "probability kernels by the recursion"만 말한다. 단조성은 없다.

그래서 §5 두 카드가 단조성의 근거로 든 "`tree:original-tilt` 의 단조성"은 그 카드에 없는 사실이다. 이것은 받는 쪽의 잘못이므로 받는 쪽을 고쳤다.

- `cavity:negligible`: `uses` 에 `tree:insertion`, `x:tree-extra-variables` 를 더했다. 섭동 factor의 보조 변수는 섭동되지 않은 계에 없으므로 trees.tex 135–140대로 path kernel을 넓힌다. 본문은 "섭동 곱 $A=\prod\psi$ 를 insertion으로 보면 $\log Y_0$, 단조성으로 $2^{-n}\le Y_0\le(3/2)^n$"으로 고쳤다.
- `cavity:increment.s2`: `uses` 에 `tree:insertion` 을 더했고 본문도 같은 식으로 고쳤다.
- `cavity:section`: 받는 표의 `tree:insertion` 행에 36–38과 95–98을 더했다.
- `tree:original-tilt` 는 두 카드의 `uses` 에 그대로 둔다. recursion 자체, 곧 $P_N^{L,\mathbf u}$ 의 정의에 쓰인다.

주는 쪽인 `tree:insertion` 의 provides, `tree:insertion.s3` 의 provides, `tree:section` 표의 §5 `\ref` 없음 행은 이미 "`tree:insertion` 의 단조성"으로 적혀 있어 고치지 않았다. 직접 길(power mean이 점별로 단조라는 것)도 수학으로는 맞는다. 그래서 이것을 "같은 backward induction"이라고 본문에 한 줄 남겼다. "좁혀서"라고 판정한 이유는 이렇다. 검토자의 (가) 안에는 받는 쪽과 주는 쪽을 모두 고치는 일이 들어 있었는데, 주는 쪽은 고칠 필요가 없었다.

순환은 없다. `tree:insertion` 은 `tree:original-tilt`, `tree:Y-recursion`, `x:tree-sampling` 만 쓴다. 검사로도 확인했다.

## ❓ 세 곳

1. **"admissible"** (`upper:bound`): ❓ 를 "작성자 읽기(근거: …)"로 바꿨다. 근거로 적은 것은 model.tex 70–71과 118–120(시행 법칙의 정의 말고 다른 제한이 없다), upper.tex 14(inf 범위 전체가 admissible이어야 결론이 따른다), upper.tex 7–9("the full trial class"), overview.tex 39–40, reduction.tex 19("all trial laws, including $r=0$")이다.
2. **(5.3)의 "its parameters"** (`cavity:negligible` gap): ❓ 를 "$\mathbf u$ 로 읽는다(작성자 읽기, 검토자 동의. 근거: …)"로 바꿨다. 근거로 적은 것은 $P_N^{L,\mathbf u}$ 의 세 첨자, cavity.tex 29–30, 16–19(계층의 지수는 $L$ 로 고정된다), cavity.tex 45·55·114의 "uniform in $L,\mathbf u$", perturbations.tex 271–273의 $\pi(d\mathbf u)$ 적분이다. 지수 $m_d$ 에 대해서도 균일하다는 작성자 확인은 그대로 두었다.
3. **s4 "increasing the constant covers the remaining sizes"** (`cavity:increment.s4`): ❓ 를 지우고 "근거는 원문에 없다(112–114). 작성자 읽기: …"로 썼다. 계산식을 적고, 다른 길(맞춤 추정이 각 $N$ 에서 유한하다는 검토자의 의견)도 함께 적었다. `uses` 의 `cavity:negligible` 은 그대로 둔다.

## (a)–(e)

- **(a)** `tree:section` 의 내주는 표를 고쳤다.
  - §4 행에 `tree:original-tilt`(upper.tex 41–43, 68)와 `tree:log-expansion` 을 통해 들어오는 `tree:Y-recursion`, `tree:Q-rule`, `x:tree-sampling`(81, 97–112, 120–121)을 더했다.
  - §5 cavity:increment 행에 `tree:Y-recursion`(53–57)과 `tree:original-tilt`("tilted reservoir kernels")를 더했다.
  - §5 `\ref` 없음 행에 `tree:original-tilt`(34–35)를 더했다.
  - `tree:section` 의 provides 문자열도 같게 맞췄다.
  - `upper:section` 과 `cavity:section` 의 "인터페이스 점검" 문단을 새 표에 맞춰 고쳤다.
- **(b)** F5와 함께 반영했다. 받는 쪽은 `upper:bound.s2` 다. `model:trial-bounds` 의 provides가 가리키는 곳을 `upper:bound.s2` 로 좁혔다.
- **(c)** `x:model-moment-finiteness` 의 `uses` 를 `upper:bound` 에서 `upper:bound.s1` 로 바꿨다. 의존 검사와 순환 검사를 통과한다. model.tex 41의 `\cref{upper:bound}` 는 뒤쪽을 가리키는 예고라서 의존 검사에서 빠진다.
- **(d)** 규칙 P3과 P4를 고쳤다.
  - P3: 차이 칸의 "계층 깊이, Parisi parameter, 섭동 매개변수, $N$"을 "계층 깊이 $L$, 섭동 매개변수 $\mathbf u$, $N$"으로 바꿨다. 원문 문구(cavity.tex 41)와 "its parameters를 $\mathbf u$ 로 읽는 것은 작성자·검토자의 해석"이라는 말을 근거와 함께 덧붙였다. 지수 $m_d$ 에 무관하다는 것도 적었다.
  - P4: 머리표를 "(Aizenman–Sims–Starr식 cavity 비교)"로 바꿨다. 차이 칸에 "원문은 그 틀을 따른다고만 하고 그 결과를 증명에 쓰지 않는다"를 넣었다. 근거는 cavity.tex 4–6의 인용과, 증명 71–115가 ASS03을 인용하지 않는다는 사실이다.
- **(e)** 고칠 오류는 아니다. 그래도 혼동을 막으려고 `g:perturbation` 의 뜻 칸에 출처를 한 구절 더했다. 열린 구간은 perturbations.tex 60의 것이고, 닫힌 구간 $1/2\le\psi_\nu\le3/2$ 는 §5의 틀(cavity.tex 26)이 요구하는 것이다.

## 용어집 합치기

`build/glossary-additions-upper-cavity.md` 의 `g:bounded-law` 를 `layers/glossary.md` 의 "모형" 묶음 끝, `g:permutation-invariance` 뒤에 기존 형식대로 넣었다. 항목은 67개에서 68개가 되었다. 추가 파일은 건드리지 않았다. 제안문에서 바꾼 것은 다음과 같다.

- 역할 칸: 항별 비용을 "$B$"만으로 줄였다. "섭동 factor 하나의 비용 $\log2$ 는 이 가정이 아니라 (5.2)에서 온다(`cavity:factor-bounds`)"를 더했다. §6의 사용(perturbations.tex 4, 7–8)도 더했다.
- 쓰지 않는 뜻: "섭동 factor의 유계 $1/2\le\psi_\nu\le3/2$ (cavity.tex 6, P3의 'bounded')도 가리키지 않는다"를 더했다.

## 원칙 점검

- §4·§5 카드와 `tree:section` 에 "clustering", "self-average", "처방된 tree", "connected correlation"이 없다. "상태"는 `x:cavity-tree-sampling` 의 gap과 `tree:section` 의 physics에만 나오고, 둘 다 보조 계층 prefix의 뜻이다.
- $\mathbf u$ 를 root 변수로 쓴 곳은 없다.
- 고친 카드의 `status` 는 모두 `proposed` 다. 규칙의 승인 열도 바꾸지 않았다.

## 조율 세션에 넘기는 것

1. **수정본의 재검토 여부.** 고친 범위는 다음과 같다. 재검토할지는 조율 세션이 정한다.
   - 물리 문장: F1의 두 카드, F7, F8, F9.
   - 규칙: P3, P4.
   - 용어집: 새 항목 `g:bounded-law`.
2. **P4의 수학 노드.** P4의 수학 노드 `cavity:identity`, `cavity:site-insertion`, `cavity:bond-insertion` 과 차이 칸의 `cavity:reservoir-mean` 은 카드 없는 식 라벨이다. 검사는 graph.json의 라벨로 통과한다. 카드로는 모두 `cavity:increment` 다. 그대로 둘지 정해야 한다. 이번에는 건드리지 않았다.
3. **§8 작성 지시.** §8을 쓸 때 다음을 넣는다.
   - `comp:insertion-comparison` 의 `uses` 에 `cavity:increment`(195, 222의 `\eqref{cavity:identity}`), `cavity:increment.s4`(215–216), `x:cavity-bounded`(200), `cavity:grid`(162)를 넣는다.
   - `comp:low-increments` 쪽에는 `cavity:increment`(13–14)를 넣는다.
   - 이 항목들은 `cavity:section` 의 내주는 표에 이미 적었다.
4. **HANDOFF의 숫자.** HANDOFF의 "용어집 67항목"은 이제 68항목이다. 조율 세션이 고칠 문서다.
5. **`upper:bound` 의 `uses`.** 형제 `upper:bound.s3` 와 `upper:derivative.s1` 이 `x:tree-extra-variables` 를 쓰는데, 부모 `upper:bound` 의 `uses` 에는 그것이 없다. 검사는 통과하고 섹션 카드 `upper:section` 에는 적혀 있다. 일관성 때문에 넣을지는 선택이다. 이번에는 넣지 않았다.
