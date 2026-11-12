# 검토 2 대응 — §2 model 노드 카드

대상: `build/review-2-model.md` 의 지적 F1–F15, `model:chain` 의 ❓, 그리고 "작성자가 본 기존 문서의 어긋남" (a)–(c)와 `g:disorder` 의견.
모든 항목을 `source/sections/model.tex` 와 지적이 인용한 줄(`reduction.tex` 1–87, `upper.tex` 1–80·125, `cavity.tex` 11–34, `consequences.tex` 24–62, `introduction.tex` 72–77, `comparison.tex` 180–184)에 직접 대조했다. 고친 파일은 §2 카드 14장, 새 카드 1장(`x:model-moment-finiteness`), 그리고 `build/glossary-additions-model-2.md` 다.

검사: `python3 redesign/tools/check.py --sections decorrelation,model --out /tmp/check-model-fix.md`. 9개 검사 중 8개 통과. 용어 검사에 오류 5건이 있는데 모두 §3 카드(`tree.log-expansion`, `tree.reference-total`, `x.tree-differentiation-rule`, `x.tree-extension-history`, `x.tree-reference-paths`)의 아직 없는 `g:protected-leaf`, `g:reference-path` 에서 난다. §2 카드에서 나는 오류는 0이다. 수정 전에 있던 `[[g:disorder]]` 오류 3건은 검사하는 동안 용어집에 `g:disorder` 가 들어가면서 사라졌다.

## 대응 표

| # | 판정 | 한 줄 근거 | 고친 파일 |
|---|---|---|---|
| F1 | 반영 | model.tex 131 "Under (2.1)–(2.4)". 물리 문장에 이 가정이 빠져 있었다. 검토자의 뒤쪽 안(가정을 가리키고 `exact` 유지)을 따라 `[[x:model-hypotheses]]` 를 가리켰다 | `main.theorem.md` |
| F2 | 반영 | reduction.tex 56–58: factorization이 $\widehat\theta$ 의 순열 불변성을 준다. 하한 쪽에서도 쓰인다. 부호 조건만 상한 전용이다(upper.tex 125, cavity.tex 13–14) | `model.section.md` |
| F3 | 반영 (방법을 바꿈: 카드를 나눔) | model.tex 39–41의 "as shown in upper:bound" 한 방향. upper.tex 24–34는 이 주석을 받지 않고 스스로 증명한다. (i)만 upper:bound에 기대므로 새 카드로 떼었다 | `x.model-hypothesis-remarks.md`, 새 `x.model-moment-finiteness.md`, `main.theorem.s1.md`, `model.section.md`, `model.positivity.md` |
| F4 | 반영 | model.tex 39 "automatic in the nondegenerate case", upper.tex 19(퇴화), 26 "independence gives", 28–29(한계가 1보다 클 수 있음) | 새 `x.model-moment-finiteness.md` |
| F5 | 반영 | model.tex 51–52 "corrects for interactions counted in that insertion". "중복으로"는 원문에 없다 | `x.model-message.md`, `model.section.md` (gap (5)) |
| F6 | 반영 | model.tex 119–120 "this defines $\mathcal B_0(\zeta)$ and $\Phi_0$". 약속이 아니라 대상을 정한다 | `x.model-depth-zero.md` |
| F7 | 반영 | (2.11)은 $H_N$, $Z_N$, $F_N$ 을 쓰지 않고 $\alpha$, $p$ 는 model.tex 3에서 온다. s1(reduction.tex 45–59)도 $H_N$ 을 쓰지 않는다 | `model.functional.md`, `main.theorem.s1.md` |
| F8 | 반영 | reduction.tex 10–11 "each satisfying (2.1)", 20 "integrable random constant". 전제 둘이 s1(reduction.tex 50, 59)에서 온다 | `main.theorem.s3.md`, `main.theorem.s1.md` (provides) |
| F9 | 반영 | model.tex 99는 $\mathbb E_x$ (굵지 않음). 원문대로 되돌리고 본문에 깊이 2 식과의 차이를 적었다 | `model.power-means.md` |
| F10 | 좁혀서 반영 | Monasson 이름은 카드에서 지우고 용어집 칸을 가리켰다. 나머지 말은 새 항목이 아니라 기존 항목이 덮는다고 판단(아래) | `model.power-means.md`, `model.section.md`, `x.model-theorem-scope.md`, `x.model-depth-zero.md`, `build/glossary-additions-model-2.md` |
| F11 | 반영 | reduction.tex 33–34는 차이에 대한 Lipschitz 한계라 $\lvert\log C_\theta\rvert\le B(\theta)$ 에서 따라 나오지 않는다 | `x.model-cavity-bounds.md` |
| F12 | 반영 | 가정의 진술은 model.tex 3–8, 25–38. 130–131은 함께 둔다. 의존·포함 검사는 그대로 통과 | `x.model-hypotheses.md` |
| F13 | 반영 | model.tex 32 "$a>0$ and $b$ are real random variables". $b$ 가 tanh인 것은 Viana–Bray뿐이다(consequences.tex 27). soft SAT에서는 $b=e^{-\beta W}-1$(59) | `model.positivity.md`, `x.model-hypotheses.md` (같은 표현) |
| F14 | 반영 | 물리적 Gibbs 측도의 계층에 대한 문장은 introduction.tex 75–77에 있다. `g:phi` 의 정의 위치는 이 카드가 아니다 | `x.model-theorem-scope.md` |
| F15 | 반영 | cavity.tex 11–12는 유계 가정, 16–19는 격자, power-mean 재귀는 34 | `model.section.md` |
| ❓ `model:chain` | 반영 (❓ 지움) | model.tex 80–81 "$x_\ell^j$, $j\ge1$". 82행의 $\theta,\theta_1,\ldots$ 도 무한열이다. label 집합은 가산 무한 | `model.chain.md` |

판정 수: 반영 15(F1–F9, F11–F15와 ❓), 좁혀서 반영 1(F10), 기각 0. F3은 판정은 반영이지만 검토자가 낸 고치는 방법과는 다르게 고쳤다(아래).

## 상세

### F1 — 물리 문장이 가정을 가리키게 함
`physics` 앞에 "[[g:hypotheses|가정]]([[x:model-hypotheses]]) 아래"를 붙였다. 가정을 풀어 쓰지 않고 가리켰으므로 윗단면은 부풀지 않는다. 그래서 `abstraction: exact` 를 유지했다. 이제 물리 문장과 `math` 가 같은 가정을 단다. `gap` (3)은 "가정 아래"가 (2.1)–(2.4)를 뜻하고 그 밖의 희석 모형에 대해서는 아무것도 말하지 않는다고 적도록 바꿨다. `model:section` 은 `approximation` 그대로 둔다. 그 카드의 `gap` (4), (5)에는 가정 말고도 근사가 있어서 두 카드의 유형이 달라도 어긋나지 않는다.

### F2 — 확인한 내용
reduction.tex 51–55가 (2.3)을 써서 $\widehat\theta$ 의 식을 얻고, 56–58이 그 식에서 순열 불변성을 낸다. 순열 불변성이 없으면 `comp:bounded-lower` 를 쓸 수 없다(reduction.tex 3–4 "requires bounded permutation-invariant interactions"). 따라서 "상한에만"은 부호 조건에만 맞는다. 고친 문장은 부호 조건(상한 전용, upper.tex 125), 전개(상한 upper.tex 63과 하한 쪽 상수 이동 main:theorem.s1), bounded 하한 자체(둘 다 쓰지 않음, cavity.tex 13–14)를 따로 적는다. P1과 `x:model-hypotheses`·`model:factorization`·`main:theorem.s4` 의 차이 칸과도 이제 맞는다. 검토자가 낸 문장("전개는 상한과 … 상수 이동에 쓰인다")에 "순열 불변으로 만드는 데"를 더했다. 그것이 하한이 이 사용을 뺄 수 없는 까닭이다.

### F3 — 검토자 안 대신 카드를 나눔
검토자는 `provides` 의 문구를 고치고 `main:theorem.s1` 의 `uses` 에서 이 카드를 빼자고 했다. 그렇게만 하면 한 카드가 여전히 두 가지 서로 다른 의존을 함께 갖는다.
- (i) "비퇴화 경우 (2.4)의 기대값이 자동으로 유한"은 원문 스스로 upper:bound의 증명에 기댄다(model.tex 41).
- (ii) 퇴화 경우 $b=0$, (iii) 승수 $a$ 의 자유와 $\log a$ 조건 없음은 아무것에도 기대지 않는다. §4 upper 카드는 이 둘을 받아 쓸 법하다(upper.tex 18–23이 퇴화 경우를, 71–72 "no integrability of $\log a$ is needed"가 (iii)을 다시 쓴다).

한 카드에 두면 §4 upper 카드가 (ii)·(iii)을 가리키는 순간 `upper:bound` → 이 카드 → `upper:bound` 순환이 생긴다. 그래서 나눴다.
- 새 `x:model-moment-finiteness` (remark, `source` model.tex 38–41). (i)만 담고 `uses: [model:factorization, model:positivity, upper:bound]`. `provides` 에 "받아 쓰는 카드 없음(예고 주석). 증명은 upper.tex 17–34가 스스로 하고 이 카드를 쓰지 않는다. §4·하한 쪽 카드는 이 카드를 `uses` 에 넣지 않는다"를 적었다.
- `x:model-hypothesis-remarks` 는 (ii)·(iii)만 남기고 `uses: [model:factorization]`, `source` model.tex 41–44로 줄였다(41행은 두 카드가 나눠 갖는다. (i)의 끝과 (ii)의 시작이 같은 줄에 있다). 이제 `upper:bound` 에 기대지 않으므로 §4 카드가 받아 써도 순환이 없다. 번호 (ii), (iii)은 다른 곳의 인용이 깨지지 않도록 유지했다.
- `main:theorem.s1` 의 `uses` 에서 이 카드를 뺐다. s1이 쓰는 "승수 $a$ 가 비대칭으로 의존할 수 있다"는 s1 자신의 원문(reduction.tex 46–47)에 있다. 본문에서 `[[x:model-hypothesis-remarks]]` (iii)을 가리키기만 한다. 이로써 하한 쪽 단계가 `upper:bound` 에 전이적으로 기대는 일은 없다. `main:theorem` 자신은 s4 때문에 `upper:bound` 를 직접 쓰고, 그것은 원문 그대로다.
- `model:section` (children, 구성 목록, "받는 것" 문단)과 `model:positivity` (gap의 링크)를 새 카드에 맞췄다.

의존 검사: model.tex 41행 `\cref{upper:bound}` 는 원문상 뒤를 가리키는 본문 참조라 검사에서 예고로 빠진다. 그래도 새 카드의 `uses` 에는 `upper:bound` 를 넣었다. 진술이 실제로 그 증명에 기대기 때문이다.

### F4 — 새 카드의 물리 문장
`physics`: "전개의 계수 $b$ 와 단일 spin 인자 $f$ 가 서로 독립이고 곱이 a.s. 1보다 작으면, 비퇴화 경우에는 둘 다 본질적으로 유계이고 (2.4)의 moment가 모두 유한하다." 비퇴화 조건과 독립성을 모두 달았다. "$\lvert\tanh\rvert<1$ 의 균일한 형태"는 지웠다. `gap` 에 한계 $\lVert b\rVert_\infty\le u^{-p}$, $\lVert M\rVert_\infty\le(vu^{p-1})^{-1}$ (upper.tex 24–30)이 1보다 클 수 있다는 것을 적었다.

검토자 문장을 하나 좁혔다. 검토자는 "$\lvert\tanh\rvert<1$ 의 균일한 형태"가 "Viana–Bray에서만 맞는 그림"이라고 했다. 실제로는 soft SAT에서도 $M=1$, $0\le-b<1$ 이라 $\lvert b\rvert<1$ 이다(consequences.tex 59–61). 그래서 카드에는 "두 명명 예에서는 $\lvert b\rvert<1$ 이지만, 일반적으로는 표현의 척도($f\mapsto\lambda f$, $b\mapsto\lambda^{-p}b$)를 옮길 수 있어 1 미만이 성립하지 않는다(작성자 관찰)"라고 적었다. 퇴화 조건이 "곱 항이 a.s. 항등적으로 0"(model.tex 41–42)과 같다는 것도 본문에 확인으로 적었다.

남은 (iii) 카드의 물리 문장은 "에너지 원점"과 "곱 항이 없으면 factor는 spin 무관 상수"다. $a$ 의 비대칭을 말하지 않으므로 유형을 `exact` 에서 `weakening` 으로 바꿨다.

### F5
`math` 에서 "(중복으로)"를 지웠다. `math` 는 원문이 말하는 것만 담는다. `gap` 의 따옴표 안을 원문 문장("corrects for interactions counted in that insertion")으로 바꾸고, "중복으로 센"은 작성자의 읽기라고 적었다. 같은 읽기가 `model:section` 의 물리 문장("중복으로 센 factor")에도 있어서 그 카드의 `gap` 에 (5)로 같은 단서를 더했다.

### F7
`model:functional` 에서 `model:hamiltonian` 을 빼고 `model:integrability` 를 넣었다. $\alpha$, $p$ 는 model.tex 3에서 온다. "물리적 disorder"를 평균하는 $\mathbb E$ 의 변수 $k,\theta,\theta_j,h$ 는 `model:vs` 에 있고 그 카드는 이미 `uses` 에 있다. `main:theorem.s1` 에서도 뺐다. `model:vs` 의 `uses` 에도 `model:hamiltonian` 이 있지만 검토자가 통과시켰고 지적 범위 밖이라 그대로 두었다(조율 사항 4).

### F8
s3 `math` 첫머리에 다음 구절을 넣었다: "$\widehat\theta$ 와 $h$ 는 (2.1)을 만족하고($\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$, main:theorem.s1) 잘린 $\widehat\theta^{(K)}$, $h^{(K)}$ 는 bounded이며, $c$ 는 적분 가능하므로(main:theorem.s1) reduction:stability가 적용된다." s1 `provides` 에도 s3가 받는 것을 더했다.

### F10 — 좁힌 이유
- **Monasson.** 규율 3의 금지 목록에는 없지만, 논문이 쓰지도 증명하지도 않는 동일시에 사람 이름을 붙인 것이다(HANDOFF 원칙 2의 취지). `model:power-means` 의 `physics` 에서 그 문장을 지우고, `gap` 에서 "계층별 재가중으로 읽는 그림은 용어집 power mean 항목의 물리 대응 칸(intuition)"을 가리키게 했다. 남은 물리 문장은 (2.10)을 덜 말하는 정확한 서술이라 유형을 `intuition` 에서 `weakening` 으로 바꿨다. 그 그림을 용어집에 더하자는 제안은 `glossary-additions-model-2.md` 3에 있다.
- **정류점(saddle point).** 지금 `g:phi` 물리 대응("saddle point 선택")과 `g:functional` 물리 대응("정류점")이 덮는다. 쓰인 카드들은 그 문서 안에서 이미 `[[g:phi]]` 나 `[[g:functional]]` 을 건다. 링크가 없던 `x:model-depth-zero` 의 `gap` 에만 `[[g:phi]]` 를 더했다. `g:phi` 에 한국어 "정류점"을 함께 적자는 제안은 additions 1에 있다.
- **full RSB.** 용어집 어디에도 없다. 카드 두 곳(`model:section` gap (1), `x:model-theorem-scope` physics)에서 "[[g:rsb-steps|RSB 단계 수]] $r\to\infty$ 의 극한"으로 바꿔 그 말을 쓰지 않았다. 잃는 내용은 없다. `g:rsb-steps` 에 적어 두자는 제안은 additions 2에 있다.
- **RS.** `g:order-parameter` 물리 대응("$r=0$ 은 RS의 cavity field 분포")이 덮고, `x:model-depth-zero` 의 `physics` 가 그 항목을 건다. 그대로 두었다.
- **$u$-message, population of populations.** 각각 `g:site-term`, `g:order-parameter` 의 물리 대응 칸에 같은 말이 있고 해당 카드가 그 항목을 건다. 그대로 두었다.

새 `g:` 항목은 만들지 않았다. 이 말들은 독립된 대상이 아니라 기존 항목의 물리 쪽 이름이다.

### F12 — 검사 확인
`source` 를 model.tex 3–8, 25–38, 130–131로 했다. 의존 검사는 `uses` 한 카드의 `source` 안에 대상 라벨의 위치가 드는지를 본다(`tools/check.py` 의존 검사의 "대상 라벨의 위치가 허용된 카드 범위 안이면 통과" 규칙). 그래서 `main:theorem`(model.tex 130)을 가리키는 upper.tex 12가 이 카드를 거쳐 통과한다는 사실은 그대로다. 새 범위 안의 참조는 38행 `\eqref{model:positivity}` 하나이고, 이 카드는 그것을 `uses` 에 두고 있다. 검사를 돌려 의존·포함 모두 통과했다. (2.2)(9–23)는 가정이 아니라 대상이라 범위에 넣지 않고 `uses` 의 `model:hamiltonian` 으로 가리켰다(본문에 적음). 범위를 정한 이유를 SCHEMA에 한 줄 적는 일은 조율 사항 1로 넘긴다. 내친김에 `math` 에 model.tex 38 "finite real expectations"의 해석을 더했고, 물리 문장의 "coupling의 부호 조건"을 F13과 같은 이유로 "그 전개 계수 $b$ 의 부호 조건"으로 바꿨다.

### F14
`source` 에 `introduction.tex [75, 77]` 을 더하고, `gap` 에 그 줄이 물리적 pure state 계층 문장의 근거라고 적었다. 그 줄은 원문의 "ultrametric"이라는 말을 담지만 카드 칸에는 그 이름을 쓰지 않았다. 같은 물리 문장의 "full-RSB"는 F10 처리로 바꿨다. `provides` 의 "g:phi의 정의 위치"는 "g:phi의 물리 대응 칸이 인용하는 줄"로 고쳤다.

### ❓ `model:chain`
model.tex 80–81 "Use different labels for $x_1,\ldots,x_p$ and for $x_\ell^j$, $j\ge1$, $1\le\ell<p$"에서 $j$ 의 범위가 $j\ge1$ 이다. 82행도 $\theta,\theta_1,\ldots$ 를 $k$ 와 독립인 무한열로 잡는다. label 집합은 $\{1,\ldots,p\}\sqcup\{(j,\ell):j\ge1,1\le\ell<p\}$, 가산 무한이다. ❓ 를 지우고 이 근거와 함께 $V_{\rm s}$ 가 처음 $k$ 개 묶음만 쓴다는 것, $\mathscr F_d$ 가 가산 생성이라는 것, $V_{\rm s}$·$V_{\rm e}$ 의 label이 서로 다르다는 것(upper.tex 40, comparison.tex 182와 같은 약속)을 적었다.

### 검토자의 "기존 문서의 어긋남" (a)–(c)와 `g:disorder` 의견
지금 `layers/glossary.md` 를 읽어 보니 모두 이미 반영되어 있다: `g:positivity` 의 "$-1<b\le0$"과 유형 weakening(F13 덧붙임 포함), `g:site-term` 의 "$p$ 번째 좌표", `g:rsb-steps` 정의 위치의 model.tex 70·118–120, `g:disorder` 의 "disorder와 $\eta_0$", "섭동 매개변수는 선택된 고정값", 정의 위치의 `model:vs`. 따라서 추가로 제안하지 않는다.

## 구조가 바뀐 카드
- `x:model-hypothesis-remarks` 를 둘로 나눴다. 새 `x:model-moment-finiteness`(model.tex 38–41, (i), `upper:bound` 에 기댐)와 줄어든 `x:model-hypothesis-remarks`(41–44, (ii)·(iii), `uses: [model:factorization]`, 유형 weakening)다. `model:section` 의 children이 19개에서 20개가 됐다.
- `x:model-depth-zero`: `kind` 를 convention에서 definition으로 바꿨다.
- `uses` 변경: `main:theorem.s1` 은 `[model:factorization, model:integrability]` 가 됐다(`model:hamiltonian`, `x:model-hypothesis-remarks` 뺌). `model:functional` 은 `model:hamiltonian` 을 빼고 `model:integrability` 를 넣었다.
- `source` 변경: `x:model-hypotheses` 에 model.tex 3–8, 25–38을 더했다. `x:model-theorem-scope` 에 introduction.tex 75–77을 더했다. `x:model-hypothesis-remarks` 는 38–44에서 41–44로 줄었다.
- 유형 변경: `model:power-means` 는 intuition에서 weakening으로, `x:model-hypothesis-remarks` 는 exact에서 weakening으로 바뀌었다.

`status` 는 모두 `proposed`. 금지된 이름(Ruelle cascade, Ghirlanda–Guerra, stochastic stability, ultrametricity)은 고친 카드의 `physics`·`gap` 어디에도 없다. "cascade"는 `model:section` gap (3)에 부정으로 한 번 남아 있고 이것은 원래대로다. "상태"는 `model:power-means` 의 `[[g:state]]` (깊이 $d$ prefix) 한 곳뿐이다.

## 조율 세션에 넘기는 것
1. **SCHEMA 관행 한 줄.** 원문에 없는 묶음 카드(`x:model-hypotheses`)의 `source` 에는 묶은 진술의 범위와 함께 그것을 이름으로 부르는 줄도 둔다(의존 검사가 라벨 위치로 허용하므로). §4 작성자가 `upper:bound` 의 `uses` 에 `main:theorem` 대신 `x:model-hypotheses` 를 넣게 하려면 이 관행이 적혀 있어야 한다.
2. **§4 upper 카드 작성자에게.** `x:model-moment-finiteness` 는 `uses` 에 넣지 않는다(순환). 퇴화 경우·승수 $a$ 는 `x:model-hypothesis-remarks` 를 가리켜도 된다. `upper:bound` 의 첫 단락(upper.tex 17–34)은 (i)을 스스로 증명한다.
3. **용어집 보강.** `build/glossary-additions-model-2.md` 의 세 칸 보강(`g:phi` 의 "정류점", `g:rsb-steps` 의 RS/1RSB/full RSB, `g:power-mean` 의 $Z^m$ 재가중 intuition). 새 slug는 없어서 합치지 않아도 검사 오류는 나지 않는다.
4. **작은 것.** `model:vs` 의 `uses` 에 있는 `model:hamiltonian` 도 F7과 같은 이유로 필요 없어 보인다($k,\theta_j,h$ 는 그 카드 스스로 정의한다). 검토자가 통과시킨 카드라 손대지 않았다.
5. **§9 겹침.** `main:theorem.s1`–`s4` 는 reduction.tex 45–87의 카드다. §9 카드를 쓸 때 겹쳐 쓰지 않도록 한다(원래 카드 본문에 있던 메모 그대로).
6. **§3 검사 오류.** `g:protected-leaf`, `g:reference-path` 가 용어집에 없어서 §3 카드 5장에서 용어 오류가 난다. 이 작업의 범위 밖이다.
