# 용어집 보강 제안 — §2 model 카드 검토 2 대응에서 (F10)

조율 세션이 `layers/glossary.md` 에 합친다. **새 `g:` 항목은 제안하지 않는다.** 검토 F10이 든 말들은 모두 기존 항목의 칸을 조금 넓히면 덮인다. 카드에는 새 slug를 걸지 않았으므로 이 제안이 합쳐지지 않아도 용어 검사 오류는 없다.

판단 근거: 용어 규율 1은 `physics`·`gap` 의 전문 용어에 "항목"이 있기를 요구한다. 아래 말들은 독립된 대상이 아니라 기존 항목(`g:phi`, `g:rsb-steps`, `g:power-mean`, `g:order-parameter`, `g:site-term`)의 물리 쪽 이름이라 새 항목보다 그 항목의 물리 대응 칸에 두는 것이 맞다. 카드 쪽에서는 해당 항목을 가리키도록 고쳤다.

| 말 | 쓰인 카드 | 지금 덮는 곳 | 제안 |
|---|---|---|---|
| 정류점(saddle point) | `model:section`, `model:functional`, `main:theorem`, `x:model-depth-zero` (gap) | `g:phi` 물리 대응 "saddle point 선택", `g:functional` 물리 대응 "정류점" | `g:phi` 에 한국어 "정류점"을 함께 적는다 (아래 1) |
| full RSB | (카드에서 지움) `model:section`, `x:model-theorem-scope` 는 "[[g:rsb-steps]] $r\to\infty$ 의 극한"으로 바꿈 | 없음 | `g:rsb-steps` 물리 대응에 적어 둔다 (아래 2) |
| RS (replica symmetric) | `x:model-depth-zero` (title, physics) | `g:order-parameter` 물리 대응 "$r=0$ 은 RS의 cavity field 분포" | `g:rsb-steps` 에도 $r=0$ = RS를 적는다 (아래 2) |
| Monasson $Z^m$ 재가중 | (카드에서 지움) `model:power-means` physics는 용어집 power mean 항목의 물리 대응 칸을 가리킴 | `g:hierarchy` 물리 대응(tilt 쪽)만 | `g:power-mean` 물리 대응에 intuition으로 더한다 (아래 3) |
| $u$-message | `model:site-message` (gap) | `g:site-term` 물리 대응 "$u$-message" | 그대로 둔다 |
| population of populations | `model:chain` (physics) | `g:order-parameter` 물리 대응 | 그대로 둔다 |

## 1. `g:phi` — 물리 대응 칸

지금:
> approximation — 물리의 "saddle point 선택"에 해당한다. 수학은 inf이고, inf의 달성이나 무한 깊이 극한은 주장하지 않는다(`model.tex` 138–140).

제안:
- **물리 대응**: approximation — 물리의 정류점(saddle point) 선택, 곧 시행 order parameter에 대한 극값 조건에 해당한다. 수학은 모든 유한 $r$ 과 모든 시행 법칙에 대한 inf이고(`model.tex` 116, 134), inf의 달성이나 무한 깊이 극한은 주장하지 않는다(`model.tex` 138–140). 모든 시행값이 상한이라는 사실(`upper:bound`)이 inf를 정당화한다.

## 2. `g:rsb-steps` — 물리 대응 칸에 한 문장 추가

추가:
> 물리의 이름으로 $r=0$ 은 RS(replica symmetric), $r=1$ 은 1RSB다(`model.tex` 77–78, 118–120). 물리의 full RSB는 $r\to\infty$ 극한의 order parameter를 말하지만, 주정리는 유한 $r$ 에 대한 inf만 말하고 그 극한 대상을 다루지 않는다(`model.tex` 138–140, `x:model-theorem-scope`).

## 3. `g:power-mean` — 물리 대응 칸에 한 문장 추가

추가:
> intuition — 깊이 하나($r=1$)에서 $T_0V=(\mathbb E_x[V^{m_1}\mid\boldsymbol\eta_0])^{1/m_1}$ 은 1RSB cavity 계산의 $Z^m$ 재가중(Monasson)과 같은 꼴이고, $T_d$ 를 반복하는 것은 그것을 계층마다 쓴 꼴로 읽을 수 있다. 논문은 이 읽기를 쓰지 않고 (2.10)을 정의로 둔다(`model.tex` 90–110). `g:hierarchy` 의 물리 대응 칸(tilt 쪽)과 같은 그림이다.

(지금 이 칸의 "Ruelle cascade" 문장은 용어 규율 3이 허용하는 자리(용어집 물리 대응 칸, intuition)이므로 손대지 않는다.)
