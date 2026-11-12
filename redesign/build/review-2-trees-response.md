# 검토 2 대응 — §3 trees 노드 카드

대상: `build/review-2-trees.md` 의 지적 F1–F10, "작성자 읽기" 네 곳에 붙은 권고, §7 카드 두 장(검토의 (a), (b)).
모든 항목을 원문 줄을 직접 열어 다시 대조했다(`trees.tex`, `cavity.tex` 25–40·90–100, `upper.tex` 20–128, `perturbations.tex` 55–72, `reduction.tex` 1–45, `model.tex` 85–135, `comparison.tex` 136–150, `decorrelation.tex` 330–336·547). 승인 표시는 모두 `proposed` 그대로다.

판정: 반영 9, 좁혀서 반영 1(F2), 기각 0. F2 안의 reduction.tex 34–35·39–40 귀속은 기각했다(아래).

## 건별 표

| 번호 | 판정 | 한 줄 근거 | 고친 파일 |
|---|---|---|---|
| F1 틀림 | 반영 | cavity.tex 29–31 "The parameters of the factors are denoted by $\mathbf u$ and are fixed, not quenched random variables, unless a parameter average is explicitly taken"; perturbations.tex 68–69 "We use $\pi$ to select deterministic parameter vectors, not as part of their quenched law". 용어집 `g:root` 의 "쓰지 않는 뜻"과 같게 고침 | `cards/tree.multioverlap.md` (gap), `cards/x.tree-path-kernels.md` (본문) |
| F2 누수 | 좁혀서 반영 | upper.tex 51–54, 67–68, 91–92; cavity.tex 37–38, 95–98; perturbations.tex 64–65 모두 확인, 표에 넣음. reduction.tex 34–35, 39–40은 §2 연산자 $T_d$ 에 대한 말이고 §2가 스스로 진술(model.tex 123–127)하므로 §3에 귀속하지 않음 | `cards/tree.section.md` (`provides`, 표 세 행 추가, 귀속하지 않은 줄의 메모), `cards/tree.insertion.md` (`provides`, 본문), `cards/tree.insertion.s3.md` (`provides`), `cards/x.tree-extra-variables.md` (`provides`) |
| F3 누수 | 반영 | trees.tex 143–144에서 $A_{\boldsymbol t}$, $D_j$ 정의; 157 "The expressions"는 앞의 식들 | `cards/x.tree-analytic-bounds.md` (`math` 첫 문장, `uses` 에 `tree:first-variation`) |
| F4 누수 | 반영 | $d_\beta$, $n_\beta$ 는 trees.tex 92–93(lemma `tree:insertion` 진술 안), $\operatorname{Int}$ 는 102. `tree:telescoping` 의 `math` 에 정의를 넣음. `uses` 는 늘리지 않음(순수 조합 사실). `tree:Q-rule` 은 `uses: [tree:telescoping]` 로 이 정의를 받음 | `cards/tree.telescoping.md` |
| F5 누수 | 반영 | "reference"는 trees.tex 311–315의 말 | `cards/tree.reference-total.s1.md` (`uses` 에 `x:tree-reference-paths`) |
| F6 과장 | 반영 | trees.tex 476–481은 상계만 준다 | `cards/tree.regular-shapes.md` (physics; `exact` 유지) |
| F7 과장 | 반영 | trees.tex 87–88 "Multiplying each spin weight by $A$", 98–103 $W_{\mathcal T}=\prod_aA^a\cdots$, 283–287 좌변 $E^{A_{\boldsymbol t}}_{\mathcal T}[H/A^{a_*}_{\boldsymbol t}]$: 모든 leaf가 $A^a$ 를 받고 anchor 인자만 상쇄 | `cards/tree.extension-expansion.md` (physics, 본문의 $k=0$ 읽기 문장) |
| F8 과장 | 반영 | trees.tex 67–80은 임의 kernel 열의 정의, Gibbs는 63–64의 경우. `g:state` 는 $0\le d<L$ | `cards/tree.Y-recursion.md` (physics, gap) |
| F9 누수 | 반영 | 원문 증명 298–304가 세 문장을 따로 논하지 않음; 작성자 표시로 `math` 에 올림 | `cards/tree.extension-expansion.s1.md` (`math`, `uses` 에 `x:tree-analytic-bounds`), `cards/tree.extension-expansion.s2.md` (`math`) |
| F10 용어 | 반영 | 두 항목이 용어집에 없어 용어 검사 오류 5건. trees.tex 314–315 "with the same specified ancestry" 확인 | `layers/glossary.md` (`g:protected-leaf`, `g:reference-path` 추가, `g:extension-history` 의 reference path 정의를 링크로 줄임) |
| 권고: quenched 대비 | 반영 | trees.tex 135–140: 앞 문장(prior kernel로 path에 들어감)과 대비; 23 "The root distribution is fixed throughout all insertions" | `cards/x.tree-extra-variables.md` (본문) |
| 권고: Cauchy 읽기 나눔 | 반영 | 171–172 "justify integration of analytic functions at each step and all subsequent differentiations"(해석성 보존), 173–174 "their derivatives on smaller domains"(Cauchy 추정); perturbations.tex 392–393 | `cards/x.tree-analytic-bounds.md` (본문) |
| §7 (a) | 반영 | trees.tex 482–483은 "Deleting leaves from a regular tree produces a regular tree"(regularity 보존). 법칙의 사영 일관성은 38–39 "Removing some leaves … preserves the sampling law", 200–201 "the projectivity of tree sampling". 482–483은 항목 (4)의 regularity 근거(comparison.tex 142–143 "every induced subtree retains the interior and separation conditions")로 옮김 | `cards/decor.section.md` |
| §7 (b) | 반영 | 그 카드의 `math` 는 trees.tex 28–40을 옮기며 그 범위의 카드는 `x:tree-sampling` | `cards/x.decor-tree-sampling.md` (`uses: [x:tree-sampling]`) |

## 좁힘의 상세 근거 (F2)

**넣은 것.** 원문을 열어 다음을 확인했다.

- upper.tex 51–54: "Poisson differentiation gives $\varphi'(t)/\alpha$ as the expected insertion increment … Each increment has absolute value at most $B(\theta)$, since the recursion preserves multiplicative bounds." 증분이 $\log Y_0$ 인 것은 `tree:insertion` 첫 문단, 상계는 단조성(`tree:insertion.s3`).
- upper.tex 67–68: "the independent message process is appended to the unperturbed tilted tree, so its increment is $\log T_0V_{\rm e}$." 원래 tilt가 추가 변수의 prior를 바꾸지 않는다는 `x:tree-extra-variables` 의 약속.
- upper.tex 85–92: 정규화된 비 $(1+\lambda D)/(1+\lambda D_*)$ 가 $e^{\pm2B(\theta)}$ 사이에 있으므로 "(upper:regularization) is bounded in absolute value by $2B(\theta)$". 단조성, 그리고 root-가측 상수 $1+\lambda D_*$ 를 빼내는 동차성.
- cavity.tex 37–38: "Comparing pointwise with the unperturbed spin weight and then applying the recursion gives (cavity:negligible)". 단조성.
- cavity.tex 95–98: "Deleting or adding a perturbation changes the root logarithm by at most $\log2$ … An unused auxiliary variable can simply be integrated out with its prior". 앞은 단조성, 뒤는 `x:tree-extra-variables`.
- perturbations.tex 64–65: "The factor bound permits termwise comparison through the power means, as in (cavity:negligible)." 단조성.

**넣지 않은 것: reduction.tex 34–35, 39–40.** "The power means preserve these root-measurable bounds"(34–35)와 "the physical constants factor out of the spin partition function and of every power mean"(39–40)는 (reduction:trial-stability), (reduction:shift)의 증명이고, 대상은 시행 functional $\mathcal B_r$ 의 연산자 $T_d$(model.tex 92–95)다. 그 곱셈 경계 보존은 §2가 스스로 진술한다: model.tex 123–124 "the power-mean operators preserve pointwise multiplicative bounds", 그리고 (model:trial-bounds). 상수가 power mean 밖으로 나오는 것은 power mean의 정의에서 한 줄로 나오는 성질이다. §3의 lemma(path kernel 위의 $Y$ recursion)를 부를 자리가 아니므로 §3의 "밖에 내주는 것"에 넣지 않았다. 이 판단은 `tree:section` 본문에 한 문단으로 적었다. 39–40의 동차성을 §2 카드가 담는지는 §2 쪽 일이다(아래 "넘기는 것").

## 반영 가운데 검토자 제안과 다르게 한 곳

- F1: 검토자 문구에 더해 "이 절의 삽입 매개변수 $t_j$ 도 무작위 변수가 아니라 미분 변수"를 `x:tree-path-kernels` 본문에 적었다(검토자가 근거로 든 말을 카드에 올린 것).
- F3: `math` 에서 "앞의 식들"을 $Y_d$, (tree:updated-kernel), (tree:first-variation) 셋으로 적고, 이 대상 읽기가 작성자 읽기임을 표시했다. 원문 157 "The expressions"는 대상을 명시하지 않는다.
- F9: s1의 "순서 무관" 근거로 좌변의 해석성(`x:tree-analytic-bounds`)을 들었으므로 s1의 `uses` 에 그 카드를 넣었다. 부모가 이미 쓰는 카드라 순환은 생기지 않는다.
- F10: `g:protected-leaf` 의 뜻에 근거 줄 194–200(remaining leaf와 fresh leaf가 protected가 됨)을, `g:reference-path` 의 역할에 `decorrelation.tex` 547($C(S,e)=-\delta\kappa(S)$ 의 실제 줄)을 더했다. `build/glossary-additions-trees.md` 는 그대로 두었다.
- §7 (a): 482–483을 지우지 않고 항목 (4)로 옮겼다(comparison.tex 142–143이 바로 그 사실을 쓴다).

## 검사

저장소 루트에서 `python3 redesign/tools/check.py --sections decorrelation,trees --out /tmp/check-trees-fix.md`.

- 수정 전: 용어 오류 5(모두 `g:protected-leaf`, `g:reference-path` 미등재).
- 수정 후: 형식·정초·포함·의존·순환·사전·단면·용어 통과. 용어집 항목 67개.
- 남은 오류: 연결 7건, 모두 `upper:bound` 카드(children `upper:bound.s2`, `.s3`, `.s4`, `upper:derivative` 와 본문 링크 세 개가 아직 없음). 다른 에이전트가 쓰는 중인 §4 카드라 고치지 않았다. §3·§7 카드와 `layers/` 에서 나는 오류는 0이다.

## 조율 세션에 넘기는 것

1. §4 `upper:bound` 의 연결 오류 7건(위).
2. §4·§5·§6 카드 쪽: 이번에 `tree:section` 표에 올린 `\ref` 없는 사용(upper.tex 51–54, 67–68, 91–92; cavity.tex 37–38, 95–98; perturbations.tex 64–65)을 받는 쪽 카드의 `uses` 가 `tree:insertion`(또는 `.s3`)과 `x:tree-extra-variables` 를 담는지 확인이 필요하다. 기계 검사는 `\ref` 만 보므로 잡지 못한다.
3. §2 쪽: reduction.tex 39–40 "the physical constants factor out … of every power mean"(동차성)은 model.tex에 명시 진술이 없다. `model:power-means` 나 `model:trial-bounds` 카드가 이 성질을 담는지, 담지 않으면 §9 카드가 power mean 정의에서 직접 읽는지 §2·§9 작성자가 정할 일이다.
4. 용어집 `g:extension-history` 의 reference path 문장을 `[[g:reference-path]]` 링크로 줄였다. 이 문장을 인용하는 다른 문서가 있으면 새 항목을 가리키게 하면 된다.
