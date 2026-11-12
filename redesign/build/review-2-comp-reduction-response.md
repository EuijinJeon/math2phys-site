# 검토 2 응답 — §8 comparison · §9 reduction

대상 검토: `build/review-2-comp-reduction.md` (지적 8건: 중간 1, 낮음 7; 다른 섹션 보충 (a)–(f); 의존 경고 2건).
기준: `source/sections/comparison.tex`, `reduction.tex`, 그리고 지적이 인용하는 `model.tex` 71·90–128, `trees.tex` 18–49·107–110·135–140·460–471, `overview.tex` 36–51, `decorrelation.tex` 11–13, `cavity.tex` 11, `perturbations.tex` 249–253. 모든 판정은 원문 줄을 직접 열어 확인한 뒤 내렸다.

## 건별 표

| 번호 | 판정 | 한 줄 근거 | 고친 파일 |
|---|---|---|---|
| F1 (중간) | 반영 | comparison.tex 46–47 $\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)$, 62–66: $\eta_d$ 에서 뽑히는 것은 자식 prefix가 아니라 자식에 딸린 $\eta_{d+1}$(마지막 단계는 $x$) | `cards/comp.encoding.s3.md` (physics, gap) |
| F2 | 반영 | 52 "All state spaces"는 값 공간이고 prefix가 아니다. 용어 규율 2 | `cards/comp.encoding.s2.md` |
| F3 | 반영 | `cavity:section` 을 (a)대로 고친 뒤 그 파일에 맞춰 대조 문단을 다시 썼다 | `cards/comp.section.md` |
| F4 | 반영 | 유한성 가정이 없으면 $\mathbb E[(T_{d+1}V)^m\mid\mathscr F_d]=\infty$ 일 수 있다. $\mathscr F_0\subseteq\mathscr F_j$ (model.tex 90–91)라서 (b)는 $\mathscr F_0$-가측 $\lambda$ 전체에서 성립한다. 유도를 다시 했다 | `cards/x.reduction-power-mean-scaling.md` |
| F5 | 반영 | `source` 를 진술 131–139와 증명 140–153으로 나눴다. 둘째 단계 ID를 `comp:shape-error.s1` → `.s2` 로 바꾸고 파일 이름과 모든 참조를 고쳤다 | `cards/comp.shape-error-bound.md`, `cards/comp.shape-error.s2.md`(옛 `.s1`), `cards/comp.shape-error.md`, `cards/comp.section.md` |
| F6 | 반영 | overview.tex 40 `\cref{comp:section}`, decorrelation.tex 13(예고), overview.tex 51 `\cref{reduction:section}`, cavity.tex 11(예고)을 확인했다 | `cards/comp.section.md`, `cards/reduction.section.md` |
| F7 (확신 낮음) | 반영 | physics의 "극한에서 사라진다"는 gap (2)의 순서 있는 극한 안에서만 맞다. 같은 내용의 `comp:shape-error`·`comp:insertion-comparison` 이 `approximation` 이므로 원칙 1에 따라 맞췄다 | `cards/comp.insertion-comparison.s3.md` |
| F8 | 반영 | 다섯 곳 모두 원문에 없는 문구임을 확인하고 "(작성자; 근거 …)"를 붙였다 | `cards/comp.shape-error-bound.md`, `cards/comp.low-increments.md`, `cards/comp.shape-error.md`, `cards/comp.encoding.s4.md`, `cards/x.comp-standing.md` |
| (a) | 반영 | `provides` 줄의 §8 목록. 표에 123행(`cavity:grid`, $Q_k$ 가 $m_d=d/L$ 을 전제, trees.tex 460)과 215–216·226행(`x:cavity-bounded`)을 더했다 | `cards/cavity.section.md` |
| (b) | 반영 | 단조성은 215–216에서 직접 쓰이지 않고 `cavity:increment.s4` 와 `model:trial-bounds` 를 거친다(검토자의 단서). 그래서 행에는 동차성(203)을 직접 사용으로, 단조성은 간접 사용으로 적었다. power mean 문단도 고쳤다 | `cards/tree.section.md` |
| (c) | 반영 | perturbations.tex 249–253이 $\underline F$·$\Delta_N(\mathbf u)$ 를 정의하고, comparison.tex 11–14가 그것을 쓴다 | `cards/pert.section.md` |
| (d) | 반영 | 줄 번호를 하나씩 확인했다. 다른 에이전트도 이 파일을 고치므로, 파일을 다시 읽은 직후 한 문단만 끼워 넣었다 | `cards/model.section.md` |
| (e) (확신 중간) | 좁혀서 반영 | 아래 상세 근거 | `cards/model.trial-bounds.md` |
| (f) | 반영 | 기호 줄을 바깥 조립 / 안쪽 명제의 두 부분으로 나눴다. 뜻 칸은 그대로다 | `layers/glossary.md` |
| 비계수 권고 (`comp:section` gap (1)의 "먼저 소진") | 반영 | $\eta\downarrow0$ 는 안쪽 명제 안에서 $L\to\infty$ 뒤에 온다(comparison.tex 153–156) | `cards/comp.section.md` |

판정 집계: 지적 8건은 모두 반영했다. 보충 (a)–(f)는 5건 반영, 1건(e) 좁혀서 반영했다. 기각한 것은 없다.

## 상세 근거

### F1
comparison.tex 29–31에 따르면 prefix는 tilted reservoir 보조 kernel로 뽑히고, $\mathscr G_d$ 가 그 prefix를 생성한다. 44–48의 $\eta_d$ 는 자식의 $\eta_{d+1}$(그 prefix의 함수)의 조건부 법칙이다. 62의 "Conditional independence of children"과 같은 kernel을 합치면, 자식들의 $\eta_{d+1}^{(\ell)}$ 은 $\mathscr G_d$ 가 주어졌을 때 독립이고 법칙이 $\eta_d$ 다. 그래서 physics 문장을 검토자의 제안대로 바꿨다. gap에는 "$\eta_d$ 에서 뽑히는 것은 prefix가 아니라 그 함수 $\eta_{d+1}$" 이라는 한 문장을 더했다. 유형은 `exact` 그대로다.

### F4 (유도 재확인)
- 정의: model.tex 92–95의 $T_dV=(\mathbb E[(T_{d+1}V)^{m_{d+1}}\mid\mathscr F_d])^{1/m_{d+1}}$, $0<m_1<\dots<m_r<1$ (71). $\mathscr F_d$ 는 물리 disorder와 $\eta_j$, $j\le d$ 가 생성하므로 $d$ 에 대해 증가한다(90–91).
- (a) 단조성: 조건부 기대값은 단조이고 $y^m$, $y^{1/m}$ 은 증가 함수다. 역방향 귀납으로 나온다.
- (b) $\lambda$ 가 $\mathscr F_0$-가측이면 모든 $\mathscr F_d$ 에 가측이다. 그래서 $\mathbb E[(\lambda X)^m\mid\mathscr F_d]=\lambda^m\mathbb E[X^m\mid\mathscr F_d]$ 이고, 역방향 귀납으로 나온다.
- 유한성: (b)를 상수 $e^{\pm c}$ 에 쓰면 $T_de^{\pm c}=e^{\pm c}$ 이고, (a)로 $T_dV\in[e^{-c},e^c]$ 다. 이 가정이 없으면 $\log$ 차가 뜻이 없을 수 있다. 쓰이는 곳(`reduction:stability.s2`·`s3`)에서는 $c=\max(\lvert h\rvert,\lvert h'\rvert)+\sum_j\max(B(\theta_j),B(\theta_j'))$ (edge 쪽은 $\max(B(\theta),B(\theta'))$)이다. 이것은 물리 disorder만의 함수이고 (2.12)의 증명과 같은 경계다. 그래서 `uses` 에 `model:trial-bounds` 를 더했다. `model:trial-bounds` 는 이 카드를 `uses` 에 넣지 않으므로 순환은 없다(검사 통과).
- 결론: $e^{-\delta}V\le V'\le e^\delta V$ 이고 $\delta$ 가 $\mathscr F_0$-가측이면, (a)와 (b)로 $e^{-\delta}T_0V\le T_0V'\le e^\delta T_0V$ 다. 옳다.

### F5
- ID를 바꾼 이유: 검토자는 본문에 한 줄을 더하는 방법과 `.s2` 로 바꾸는 방법을 둘 다 제시했다. 바꾸기 전에 `comp:shape-error.s1` 을 가리키는 곳을 저장소에서 grep으로 찾았다. 검토 보고서를 빼면 §8 카드 네 장(`comp.shape-error.s1.md` 자신, `comp.shape-error.md` 의 children과 본문, `comp.shape-error-bound.md` 의 provides, `comp.section.md` 의 본문)뿐이었다. `layers/`, `tools/`, 다른 섹션에는 없었다. 그래서 수정 권한 안에서 모두 고칠 수 있었다.
- 파일 `cards/comp.shape-error.s1.md` 를 `cards/comp.shape-error.s2.md` 로 옮기고(`mv`, git 아님) `id` 를 바꿨다. 두 카드 본문에 "첫 단계가 식 라벨을 ID로 쓰므로 `.s1` 은 없다"는 한 줄을 더했다.
- 검사 후 grep: 옛 ID는 `build/review-*` 에만 남아 있다.
- `comp:shape-error-bound` 의 `source` 는 `[131,139]` 와 `[140,153]` 으로 나눴다. 140행("The average for a singleton has no depth coordinates")은 잎 s1이 140–142로 덮고 있어서, 증명 쪽 범위에 넣어 잎의 합집합과 맞췄다.

### (e) 좁혀서 반영
model.tex 123–124의 "the power-mean operators preserve pointwise multiplicative bounds"는 그 자리에서 (2.12)의 절대 경계를 보이는 데 쓰인다. 낱말만 보면 상대 경계 $e^{-\delta}V\le V'\le e^\delta V$ 까지 포함해 읽을 여지가 있다. 그렇게 읽으면 34–35는 이 문장을 다시 쓴 것이 된다. 하지만 두 가지는 이 문장에 없다. 하나는 "root-measurable"이라는 가측성 조건이고, 다른 하나는 39–40의 동차성(상수 인자의 정확한 분리)이다. 그래서 `model:trial-bounds` 의 `provides` 가운데 `reduction:stability` 항을 "차를 잡는 두 functional의 유한성"으로 좁혔다. 상대 비교와 상수 분리는 `x:reduction-power-mean-scaling` 에 맡겼다. 카드 본문에는 읽기의 여지를 한 문단으로 적었다. `reduction:stability` 와 그 단계 s2·s3은 이미 `x:reduction-power-mean-scaling` 을 `uses` 에 넣고 있어 고칠 것이 없었다. `tree:section` 본문의 "§2가 스스로 진술한다"는 이 판단에 맞춰 "§2가 진술하는 것은 절대 경계의 보존뿐"으로 고쳤다.

### (b)의 단서
comparison.tex 215–216 "bounded by $H+BK$"는 reservoir 쪽에서는 `cavity:increment.s4`(cavity.tex 108–111)를, trial 쪽에서는 (2.12)를 다시 쓴 것이다. 그래서 `tree:insertion` 의 단조성은 간접 사용으로 적었다. 직접 쓰는 것은 203의 동차성이다: $A=z(1+D)$ 에서 $\log z$ 가 상쇄되는 것은 trees.tex 107–110 때문이다. 과제 지시는 "동차·단조성(203, 215–216)"이었다. 두 줄을 모두 적되, 쓰는 방식을 구분했다.

## 의존 경고 2건 (comparison.tex 227 `\cref{model:section}`)

카드는 고치지 않았다. `comp:bounded-lower` 와 `comp:section` 은 정의 노드(`model:functional`, `x:model-depth-zero`, `model:chain`)를 `uses` 에 넣는 지금의 처리를 유지한다. 이번 검사에서는 이 두 경고가 **나오지 않았다**(의존 오류·경고 0). 지금 `tools/check.py` 267행에 "섹션 라벨을 가리키는 참조는 그 섹션 카드의 자손 하나가 uses에 있으면 충족"이라는 규칙이 들어 있다. 검토자가 권한 1안이 다른 에이전트의 도구 작업으로 이미 반영된 것으로 보인다. SCHEMA의 의존 행에 이 규칙을 한 줄 적는 일은 남아 있을 수 있다(SCHEMA는 이번 수정 범위 밖).

## 검사

```
python3 redesign/tools/check.py --sections decorrelation,model,trees,upper,cavity,perturbations,comparison,reduction --out /tmp/check-cr-fix.md
```
결과: 형식·정초·포함·의존·연결·순환·사전·단면·용어 모두 통과했다(오류 0, 경고 0). 카드는 244장이다. `models.*`, `x.cons-*`, `x.overview-*` 카드에서 난 문제는 없다.

## 조율 세션에 넘기는 것

1. `x:pert-increment` 카드 자신의 `provides` 에 §8 사용(comparison.tex 11–14, `x:comp-standing`, `comp:low-increments`)이 없다. 이번 범위 밖이라 고치지 않았다. `pert:section` 쪽 표에는 더했다.
2. SCHEMA의 의존 행에 섹션 라벨 참조 규칙(check.py 267행)을 한 줄 적을지 정해야 한다.
3. `main:theorem` 본문 마지막 문단("§9 카드를 쓸 때 겹쳐 쓰지 않도록 조율이 필요하다")은 이제 해결된 메모다(검토 §9 겹침 4). 이 카드는 이번 범위 밖이다.
4. 증명 지도를 다시 그릴 때 `main:theorem` 을 §2와 §9 가운데 어디에 놓을지 정해야 한다. 섹션 단위로 줄인 그림에서는 순환이 생긴다(검토 §9 겹침 2). 섹션별 카드 수를 세는 곳에서는 `main:theorem` 과 그 단계 4장이 두 번 세어진다(겹침 3).
5. ID 변경: `comp:shape-error.s1` 은 이제 `comp:shape-error.s2` 다. `build/graph.json` 과 `site/` 를 다시 생성해야 한다.
6. `model.section.md` 는 다른 에이전트도 고친다. 이번 변경은 "기호로만 쓰는 곳도 많다" 문단 바로 뒤에 끼워 넣은 한 문단뿐이다. 병합할 때 확인해야 한다.
