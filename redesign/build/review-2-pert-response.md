# 검토 2 대응 — §6 perturbations

대상 보고서: `build/review-2-pert.md` (지적 8건: 중간 1, 낮음 7)와 작성자 메모 `build/glossary-additions-pert.md`.
기준: `source/sections/perturbations.tex` 전체, `cavity.tex` 26–50·88–121, `trees.tex` 156–176·286–298·305–315, `decorrelation.tex` 76–83·260–305·526–566. 지적마다 원문 줄을 직접 열어 다시 대조했고, F1은 손으로 다시 계산했다.

결과: 반영 7, 좁혀서 반영 1(F6), 기각 0. 용어집 메모 (a)–(d), (e)의 `tree:section` 표, §7 카드 네 장의 `uses` 도 반영했다.

## 건별 표

| 번호 | 판정 | 한 줄 근거 | 고친 파일 |
|---|---|---|---|
| F1 (중간) | 반영 | (6.11) $\operatorname{Var}G\le C_\nu N$ 이면 표준편차가 $\sqrt N$ 이고 $\sqrt N\ll N^{3/4}$ 다. $\sqrt N/(\rho\lambda_\nu)=c_\nu^{-1}N^{-1/8}$(229–235). 볼록성이 필요한 까닭은 규모가 아니라 대상(값 대 도함수)이다 | `pert.concentration.s3.md` (physics, gap), `pert.concentration.s4.md` (본문), `pert.concentration.md` (본문, $\sqrt N\ll s_N\ll N$) |
| F2 | 반영 | 434–435 "any consistent collection of their pairwise split depths, involving only the added colors and the anchor", 495–496 "$a,b\in\{0,\ldots,k\}$". §7은 추가 color끼리의 쌍을 쓴다(decorrelation.tex 298–302, 540–541) | `pert.tree-identity.md` (physics, gap 3), `pert.section.md` (math, gap 3, 본문), `x.pert-colored-extensions.md` (본문), `layers/glossary.md` (`g:mark` 역할), `layers/rules.md` (P7 문장), `layers/L1.md` (수 4) |
| F3 | 반영 | 세 단계가 그 노드를 직접 쓴다(trees.tex 173–176; perturbations.tex 336–338, 512; 6–8). 순환 없음(검사 통과) | `pert.analytic.s1.md`, `pert.tree-identity.s2.md`, `pert.concentration.s3.s2.md` (`uses`) |
| F4 | 반영 | cavity.tex 119–121 "Thus the concentration argument applies to its slightly modified interaction mean as well"는 Lemma 6.1의 논증을 가리키는 예고다 | `pert.section.md` (내주는 것 표, 문장) |
| F5 | 반영 | 176–178: 조건을 거는 것은 물리 개수와 섭동 **총** 개수다. $n_\nu$ 는 총 개수가 주어지면 type label의 함수다 | `pert.concentration.s3.s3.md` (본문) |
| F6 | 좁혀서 반영 | 60–62 "Counts, types, and sites belong to the root; the mark variables are sampled with their product priors at their assigned auxiliary depths". 같은 문장의 계산은 옳으므로 점 $x$ 의 묘사만 고쳤다 | `pert.palm.s1.md` (본문) |
| F7 | 반영 | 둘째 문장이 원문 33–34의 옮김이고 selector(494–511)의 근거로 논증에 쓰인다. `intuition` 이 아니라 `weakening` | `x.pert-mark-specification.md` (`abstraction`, gap) |
| F8 | 반영 | 원문은 "$0<m_1\le m_d$, $m_L=1$ 만 쓴다"를 적지 않는다(124, 138, 152, 159에서 읽은 것) | `pert.section.md` (math, 받는 것 표) |

용어집 메모와 그 밖:

| 항목 | 판정 | 근거 | 고친 파일 |
|---|---|---|---|
| (a) `g:selected-sequence` 역할 | 반영 | Palm 부등식(350–356)은 모든 $N,\mathbf u$ 에서 성립. (ii)가 쓰이는 줄은 327 "$\longrightarrow0$"과 418 "Here the score error tends to zero with $j$ fixed" | `layers/glossary.md` |
| (b) `g:concentration` | 반영 | Lemma 6.1의 결론은 (6.5) $\int e\,d\pi\to0$(97–101)뿐. 점별은 `pert:selection` (ii)(261–262, 281–299) | `layers/glossary.md` (정의 위치) |
| (c) `g:perturbation` | 반영 | $t_\nu=1/j\le1/4$ 는 $N$ 과 무관, $\psi_\nu\in(1/2,3/2)$(47–60). 작은 것은 개수 밀도 $N^{-1/4}$ | `layers/glossary.md` (물리 대응) |
| (d) `g:mark` 정의 위치 | 반영 | `pert:mark-selector` 는 식 라벨(510), 그 식을 담은 카드는 `pert:tree-identity.s2`. 기호 칸의 식 라벨도 "selector 식 (6.18)"로 | `layers/glossary.md`, `layers/rules.md` (P7 수학 노드 열) |
| (e) `tree:section` §6 행 | 반영 | 아래 "(e)의 원문 확인" | `cards/tree.section.md` (표 세 행, `provides`), `pert.section.md` (§3 대조 문단) |
| §7 `uses` | 반영 | 네 카드의 `math` 가 spin/marker anchor, added color, 제약을 쓰고 그 정의는 `x:pert-colored-extensions` 에만 있다. 순환 없음 | `decor.overlap-concentration.s1.md`, `decor.overlap-concentration.s2.s1.md`, `decor.conditional-concentration.s2.s1.md`, `decor.conditional-concentration.s3.s1.md` (`uses` 만) |

## 상세 근거

### F1 — 직접 계산

- (6.11): $\operatorname{Var}(G(u))\le C_\nu N$ 이므로 $\mathbb E_{\mathbf u}|Z(v)|\le(C_\nu N)^{1/2}$. 그러니 $G$ 값의 root 요동은 $\sqrt N$ 규모이고 score 규모 $\lambda_\nu=c_\nu N^{3/4}$ 보다 **작다**. 카드의 두 문장("$O(N)$ 이 $N^{3/4}$ 보다 크다", "$\sqrt N$ 이 $N^{3/4}$ 보다 작지 않다")은 분산과 규모를 견주었거나 부등호가 뒤집혔다.
- (6.12) $C_\nu(\sqrt N/\rho+\rho\lambda_\nu/|I_\nu|)$ 을 $\lambda_\nu$ 로 나누면 $c_\nu^{-1}N^{1/2-3/4}\rho^{-1}+\rho/|I_\nu|$ 이다. 둘 다 0으로 가는 $\rho$ 가 있을 필요충분조건은 $\sqrt N/\lambda_\nu\to0$ 이고, 두 항을 맞추는 선택이 $\rho=(\sqrt N/\lambda_\nu)^{1/2}\sim N^{-1/8}$ 이다(원문 233 "$\rho=N^{-1/8}$"). `s4.s2` 의 지수 계산 $N^{1/2+1/8-3/4}=N^{-1/8}$ 과 일치한다.
- 볼록성이 필요한 까닭: 값 $G$ 의 요동 상계는 그 자체로 기울기 $G'$ 의 요동을 누르지 못한다(값이 거의 같아도 기울기는 다를 수 있다). 볼록이면 $G'(u)$ 가 앞·뒤 차분몫 사이에 끼어 원문 216–218의 부등식이 된다. 검토자 설명이 맞다.
- 고친 문구: `s3` gap은 "이 상계는 값의 root 요동(표준편차 $O(\sqrt N)$)에 대한 것이고 도함수 $X_0'=\langle D_\nu\rangle$ 의 요동에 대한 것이 아니다 … $\sqrt N\ll\lambda_\nu$ 가 s4에서 $\rho$ 를 고를 자리를 준다". `s3` physics도 "$O(N)$, 곧 표준편차로 $O(\sqrt N)$"로 분산임을 밝혔다. `s4` 본문은 "(6.11)은 값만 누른다 → 볼록성으로 차분몫 사이에 끼움 → $\sqrt N/\rho$ 와 $\rho\lambda_\nu$ → $\rho=N^{-1/8}$ 이 두 항을 같은 차수로"로 다시 썼다. 부모 카드의 "root 분산은 $O(N)$ 이지만 …"은 틀리지 않았으나 같은 증명 안에서 표준편차를 쓴다고 맞췄다.
- $s_N$ 의 이유(검토자 의견 4): 위쪽 조건 확인. `cavity:negligible` $|P_N^{L,\mathbf u}-NF_N|\le(\log2)s_N$(cavity.tex 38–41)이 `pert:selection.s1` 의 $\liminf\frac1N\int P_N\,d\pi=\underline F$(271–273)를 주려면 $s_N=o(N)$ 이 필요하고, 증분의 맞춤 비용 $|s_{N+1}-s_N|+2s_{N+1}/(N+1)$(cavity.tex 91–93)도 $s_N/N\to0$ 에 기댄다. 그래서 부모 카드 본문에 "두 조건 $\sqrt N\ll s_N\ll N$ 사이의 한 선택(작성자 읽기)"으로 적었다. 원문은 이유를 적지 않는다.

### F2 — 원문 확인

- 431 "They occupy distinct replica positions"의 "They"는 추가 color이고, 434 "their pairwise split depths, involving only the added colors and the anchor"의 쌍은 $\{0,\ldots,k\}$ 안의 모든 쌍이다. 495–496 "For a pair of colors $a,b\in\{0,\ldots,k\}$"가 selector를 추가 color끼리의 쌍에도 만든다.
- §7: decorrelation.tex 298–302 "require the anchor and the added colors to form two copies of $S^+$, separated at $d$"는 target II의 color끼리, target I과 II의 color 사이의 split 깊이를 처방한다. 540–541 "add a full copy of $S$ all of whose leaves split from the anchor at $e-1$"도 사본 안의 color끼리의 모양을 처방한다. 그래서 "anchor와 새 color 사이"라는 읽기로는 §7의 사용이 덮이지 않는다.
- 고친 문구(모든 곳 통일): "anchor와 추가 color(새 replica)들로 이루어진 집합 안의 쌍별 split 깊이(추가 color끼리의 쌍 포함)를 서로 일관되는 한 지정한다(다른 old replica가 관여하는 쌍은 지정하지 못한다)". `pert:section` 의 §7 대조 문단에는 두 사본 제약과 $S$ 사본 제약이 color끼리의 쌍을 쓴다는 것과 원문 근거를 적었다.
- 유형은 그대로 둔다: `pert:tree-identity`, `pert:section` 모두 `approximation`(율 없음·균일성 없음 때문). 고친 물리 문장은 원문보다 더 말하지 않는다.

### F3 — 순환 확인

- `x:tree-analytic-bounds` 의 `uses` 는 `tree:Y-recursion`, `tree:insertion`, `tree:first-variation` 뿐이다. `pert:palm-expression` 은 `x:pert-test-setup`, `x:pert-mark-specification`, §3 카드만 쓴다. `x:pert-standing` 은 §5 카드만 쓴다. 셋 다 §6의 증명 단계로 돌아오는 경로가 없고, 검사의 순환 항목도 통과했다.

### F6 — 좁힌 이유

검토자의 요점(점 $x$ 의 root label은 site이고, mark는 root 변수가 아니라 보조 깊이의 변수라 tilt를 받는다)은 원문 60–62와 맞는다. 다만 표준적인 marked Poisson 과정 읽기로 mark 과정을 점의 표지로 볼 수도 있어서 원래 문장이 틀렸다고까지 하지는 않는다. 그래서 같은 문단의 Mecke 계산과 결론은 그대로 두고 점 $x$ 의 묘사만 "Poisson 과정은 root의 것이고 점 $x$ 는 type-$\nu$ 항 하나의 root label(균일 site)이다. 그 항의 mark 변수는 배정된 보조 깊이의 새 변수이고, 점을 더한 계에서는 prior로 덧붙인 뒤 insertion으로 다룬다(perturbations.tex 60–62, 367–368)"로 바꿨다. (type은 고정 $\nu$ 이므로 label에서 뺐다.)

### F5 — 문구

"보정 $2nu^2$ 는 $n$ 의 Lipschitz 함수"는 거짓은 아니나 $n_\nu$ 가 조건을 건 개수가 아니라는 점을 가렸다. 바꾼 문장: 총 개수가 주어지면 $n_\nu$ 는 type label의 함수라 label 하나를 바꾸면 보정이 $2u^2$ 이하로 바뀌고(Efron–Stein 쪽), 조건부 평균 $2u^2c_\nu\cdot(\text{총 개수})$ 는 총 개수에 대해 상수 $2u^2$ 이하로 Lipschitz다(Poisson 쪽). "작성자 풀이"로 표시했다.

### (e)의 원문 확인

모두 원문에서 다시 확인했다: 121–132(backward 단계의 미분, $K_d$, $m_L=1$, $\mathscr F_d$), 193–194("is preserved by each power mean"), 195–196("its unused independent mark variables can be integrated out"), 316–317·441–448(old replica multioverlap의 다항식 $f$, $R_E$), 321("The anchor marginal is always one tilted path"), 333–334("its insertion recursion"), 403–405("the canceled anchor expansion supplies finitely many extensions at any fixed order"), 478–492(혼합 도함수, "no additional factorial"), 516–517("positions in the sampled tree"), 526("the mixed canceled-anchor expansion"). `tree:section` 표의 §6 행 아래에 세 행을 더하고 `provides` 의 §6 괄호를 보충했다.

## 확정된 이름과 원칙 점검

- 고친 문장 어디에도 Ghirlanda–Guerra, stochastic stability를 새로 쓰지 않았다. "상태"를 새로 쓰지 않았다. $\mathbf u$ 는 계속 고정값이다(F6의 고친 문장도 Poisson 평균이 root 개수에 대한 것임을 유지). 승인 표시는 모두 `proposed` 그대로.
- "집중", "prescribed-tree 항등식", "선택된 수열"을 그대로 썼다.

## 검사

```
python3 redesign/tools/check.py --sections decorrelation,model,trees,upper,cavity,perturbations --out /tmp/check-pert-fix.md
```

형식·정초·포함·의존·순환·사전·단면·용어 통과. 연결 오류 11건은 모두 `comp:insertion-comparison`(`.s2`–`.s4`, `.s1.s2`–`.s1.s3`)와 `x:comp-standing`(`comp:bounded-lower.s2`)의 아직 없는 카드이고, 지금 다른 에이전트가 쓰는 §8 카드라서 고치지 않았다. §6·§3·§7 카드와 `layers/` 에서 나는 오류는 0이다.

## 조율 세션에 넘기는 것

1. **P6 문장(검토자 의견, 고치지 않음).** 규칙 문장은 $\log Y_0$ 전개만 말한다: "power mean 안에 넣은 섭동 $A=1+tD$ 의 효과 $\log Y_0$ 는 … 전개로 정확히 쓰인다". §6이 쓰는 것은 canceled-anchor 전개다: perturbations.tex 391 "Lemma~\ref{tree:extension-expansion} gives a complex neighborhood", 403–405 "the canceled anchor expansion supplies finitely many extensions at any fixed order", 433 "the canceled-anchor extension rule of Lemma~\ref{tree:extension-expansion}", 526 "apply the mixed canceled-anchor expansion". 그 계수 $c_E$ 는 old leaf 재사용 계수 1을 포함한다(trees.tex 264–265, 286–295). 수학 노드 열에 `tree:extension-expansion` 이 있고 P7 차이 칸이 "$c_E$ 는 P6의 tree 계수"라 하므로 닿기는 하지만, P6 문장에 "anchor 인자를 상쇄한 판은 extension history 위의 합(old leaf 재사용 계수 1)"이라는 구절을 넣을지 정할 것.
2. **F2와 같은 문구가 남은 쓰기 금지 파일.** 내용은 맞지만 "사이"가 anchor–color 쌍만으로 읽힐 수 있다.
   - `cards/decor.conditional-concentration.s3.s1.md` `math`: "이 제약은 anchor와 added color 사이의 split depth만 처방하므로". 원문 302 "These constraints involve only the anchor and the added colors"에 맞춰 "anchor와 added color들만 관여하는"으로 고치기를 권한다(이 제약 자체가 color끼리의 쌍을 쓴다).
   - `cards/x.tree-reference-paths.md` 본문 18행: "§6의 제약 $\mathcal C$가 'anchor와 added color 사이의 split 깊이만' 지정한다는 것과 같은 내용이다". 그 카드의 `math`(reference path = anchor와 이미 color를 받은 path, trees.tex 311–313)는 정확하다. 본문 인용만 고치면 된다.
3. **§3 카드의 `provides`.** `x:tree-extra-variables` 의 `provides` 는 §6에 336–338만 적는다. perturbations.tex 195–196("its unused independent mark variables can be integrated out")을 더할 것. 같은 이유로 `x:tree-sampling`(321, 516–517)과 `tree:original-tilt`·`x:tree-path-kernels`(121–132)의 `provides` 에 §6 사용이 있는지 §3 담당이 확인할 것. 이번에는 `tree:section` 의 표만 고쳤다.
4. **§7 카드의 `uses` 를 바꿨다.** 위 네 장의 `uses` 에 `x:pert-colored-extensions` 를 더했다(본문과 다른 칸은 손대지 않음). §7 담당에게 알릴 것.
