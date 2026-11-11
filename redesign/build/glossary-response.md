# 용어집 작업 응답

대상: `layers/glossary.md`(새로 씀), `layers/L0.md`, `layers/L1.md`, `layers/rules.md`, `cards/` 54장 중 43장. `tools/`, `SCHEMA.md`, `source/`는 건드리지 않았다.

결과: 용어집 항목 62개(묶음 8개). `[[g:…]]` 링크는 L0 19개, L1 47개, rules.md 74개, 카드 179개, 용어집 안 상호 참조 75개, 합계 394개. `python3 tools/check.py --sections decorrelation`은 모든 검사(새 "용어" 검사 포함)를 통과한다. 별도 스크립트로 확인한 것: (a) 쓰인 `g:` slug는 모두 항목이 있고 쓰이지 않는 항목도 없다, (b) `layers/`와 `cards/`에 역할 ID(R1–R22) 참조가 남아 있지 않다($R_S$, $R_E$ 같은 수식은 제외하고 셌다), (c) 모든 항목에 뜻·역할·정의 위치·물리 대응 칸이 있다, (d) 정의 위치의 노드 ID는 모두 `graph.json`이나 카드에 있고, 인용한 `.tex` 행 범위는 모두 파일 안에 있다. 카드의 `math`, `source`, `uses`, `children`, `id`, `kind`, `status`는 바뀌지 않았다(원본과 YAML 비교로 확인).

## 1. 예전 역할 R1–R22는 어떻게 되었나

| 예전 ID | 대상 | 새 항목 | 무엇을 고쳤나 |
|---|---|---|---|
| R1 | $\theta$ | `g:interaction` | "$\theta=-\beta\varepsilon$" 대신 원문 꼴($-H_N=\sum\theta_k+\sum h_i\sigma_i$)로 정의하고, 하한은 bounded·순열 불변 $\theta$ 만 쓴다는 역할을 붙였다. |
| R2 | $h$ | `g:field` | 그대로 정리. 쓰이는 곳(P1, P12, $V_{\rm s}$)을 붙였다. |
| R3 | $\alpha$, $M_N$, $i_{\ell,k}$ | `g:hypergraph` | "국소 tree 구조는 증명에 쓰이지 않는다"를 쓰지 않는 뜻에 넣었다. |
| R4 | $F_N$ | `g:pressure` | 그대로. |
| R5 | factorization | `g:factorization` | $a$ 가 모든 변수에 의존해도 되고 $\log a$ 적분 가능성이 불요함을 넣었다. high-temperature(loop) 전개 읽기는 Viana–Bray에서만 exact이고 일반 꼴에서는 intuition이라고 적었다. 하한에서 한 번(대칭화)만 쓰인다는 역할을 넣었다. |
| R6 | $\mathbb E[(-b)^n]\ge0$ | `g:positivity` | "frustration이 대칭/반강자성 쪽" 읽기를 intuition으로 내리고 일반 동치가 아님을 적었다. 하한에는 쓰이지 않는다. |
| R7 | message $x$, $q_x$ | `g:message` | 시행 functional의 $x$ 는 실제 계에서 계산한 것이 아니고 moment 조건도 없다는 것, encoding에서는 $x=\operatorname{arctanh}\langle\sigma_i\rangle$ 라는 것을 따로 적었다. |
| R8 | $U_\theta$ | `g:site-term` | $V_{\rm s}$ 와 한 항목으로 묶었다. |
| R9 | $C_\theta$, $V_{\rm e}$ | `g:edge-term` | "pilot에서 확인 예정" 같은 미확인 표시는 버렸다. |
| R10 | $V_{\rm s}$ | `g:site-term` | 비교에서 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$ 가 정확히 성립한다는 역할을 넣었다. |
| R11 | $r$, $\zeta$, 사슬 | `g:order-parameter`, `g:rsb-steps` | **과잉 주장 삭제**: "깊이 $d$ = state 계층의 단계"를 뺐다. 사슬의 깊이를 물리적 pure state 계층과 동일시하지 않는다고 쓰지 않는 뜻에 적었다. $r$ 과 $L=r+1$ 의 관계를 따로 항목으로 만들었다. |
| R12 | $\mathbf m$ | `g:parisi-parameters`, `g:grid` | "$x(q)$ 의 계단 높이" 읽기를 intuition으로 내렸다(원문에서 맞는 근거는 $Q_2$ split 확률 $m_{d+1}-m_d$ 하나뿐). 하한에서는 최적화하지 않고 $d/L$ 로 고정한다는 것을 `g:grid`에 분리했다. |
| R13 | power mean $T_d$ | `g:power-mean` | **과잉 주장 삭제**: "Ruelle cascade 평균을 적분해 낸 것"(예전 상태: 확정)을 intuition으로 내렸다. 논문은 cascade를 선행 연구의 도구로만 들고 항등식을 임의의 유한 kernel 열에 대해 직접 세운다(`trees.tex` 7–12). |
| R14 | $\mathscr F_d$, label $\omega$ | `g:state`, `g:order-parameter` | $\mathscr F_d$ 는 "기술 장치"에서 이 사이트의 "상태"(보조 계층 깊이 $d$ prefix)의 정의로 승격했다. label $\omega$ 는 order parameter 항목에 넣었다. |
| R15 | $\mathcal B_r$ | `g:functional` | 그대로. |
| R16 | $\Phi_r$, $\inf_r\Phi_r$ | `g:phi` | inf의 달성이나 무한 깊이 극한을 주장하지 않는다는 것을 넣었다. |
| R17 | $\gamma_\beta$, $\kappa(S)$ | `g:tree-coefficient` | Parisi block counting 읽기를 intuition으로 내리고, 부호가 일정하지 않아 `g:depth-delay`의 대상이라는 역할을 넣었다. |
| R18 | $Q_k$ | `g:tree-law` | "Ruelle cascade에서 뽑은 replica tree 법칙(nested CRP)"을 intuition으로 내렸다. 예전의 $L=2$ 검산은 원문 근거가 아니라서 옮기지 않았다. |
| R19 | path kernel, tilted kernel | `g:hierarchy` | **과잉 주장 삭제**: "tilt = 상태 가중치 $\propto Z_\alpha^{m}$, 하위 상태를 고르는 확률"을 뺐다. 가중되는 것은 보조 변수(reservoir에서는 섭동 mark)이지 물리적 pure state가 아니라고 적고, Monasson 재가중 닮음만 intuition으로 남겼다. |
| R20 | 삽입 $A$, $Y_d$, $\log Y_0$ | `g:insertion`, `g:site-bond-insertion` | 일반 insertion과 cavity의 site·bond 삽입을 나눴다. |
| R21 | mark, selector | `g:mark` | **과잉 주장 삭제**: "상태 계층의 깊이 $d$ 묶음마다 부호를 갖는 국소 field"를 "섭동 factor의 독립 부호 좌표이고, 그 기대값이 split 깊이 지시함수(selector)가 된다"로 바꿨다. 탐침장 그림은 intuition. |
| R22 | $v_N(S,d)$ | `g:conditional-covariance`, `g:clustering`, `g:independent-copies` | **과잉 주장 삭제**: "$v_N\to0$ 은 cavity method의 '상태 안 독립' 가정"을 뺐다. clustering은 깊이 평균·site 쌍 $L^2$ 평균의 진술이고, 이웃 cavity field의 독립은 따로 `g:independent-copies`(P9 + 균일 site 표본, `comp:patterns`)에서 나온다고 적었다. |

버린 것: 예전 표의 "상태(확정/제안/폐기)", 정합성 점검 칸의 미확인 검산("pilot에서 ✅ 예정", sympy 검산 등), 변경 이력. 원문 근거가 아니어서 옮기지 않았다.

## 2. 사용을 바꾼 용어 (전 → 후)

| 용어 | 전 | 후 | 파일 |
|---|---|---|---|
| R번호 | "(R3)", "역할 R1–R22는 역할 표", "R11의 $\mathcal M_{r+1}$" 등 | `[[g:…]]` 링크, "기호와 용어는 [용어집](glossary.md)" | L1(바닥·기호 줄), rules.md(머리말·기호 목록·P1–P11·확신이 낮은 대응), 카드 `decor.average-definition`, `decor.conditional-concentration`, `decor.covariance-definition`, `x.decor-mesh`, `x.decor-topology` |
| generic 상태 | "generic 상태 선택"(L1 수 3), "(generic 상태 선택)"(P5), "generic 상태(P5)에서는"(P7) | "선택된 수열 고르기", "(선택된 수열) … 곧 선택된 수열을 고를 수 있다", "선택된 수열(P5) 위에서는" | L1, rules.md |
| Gibbs 상태 | "무한 단계 극한 Gibbs 상태, 물리적 Gibbs 상태의 ultrametric 구조" | "무한 단계 극한 Gibbs 측도, 물리적 pure state들의 계층 구조" | L0 |
| 물리 유도 요약 | "Gibbs 상태는 pure state의 ultrametric 계층이고 상태 안에서 이웃 field는 독립" | "물리적 pure state들이 계층을 이루고, 한 물리적 pure state 안에서 이웃 cavity field는 독립" | L1 끝 문단 |
| pure state | "pure state" 단독 | 모두 "물리적 pure state"(용어 규율 2) | glossary, L1, rules.md, `decor.projection-bound` 등 |
| 같은 상태(일반 $\sigma$-field) | "같은 상태에서 뽑은 replica 세 개", "\"같은 상태\"는 조건부 i.i.d.(공통 $\mathscr G$ 또는 $\mathscr F_d$)" | "같은 조건($\mathscr G$; 쓰이는 곳에서는 상태 $\mathscr F_d$)이 주어지면 조건부 i.i.d.", "(b)의 조건은 일반 $\mathscr G$ 이고 상태는 그 특수한 경우" | `decor.contractions` |
| 상태 선택 | "disorder와 상태 선택에 대해 요동하지 않는다" | "root와 그 leaf의 표본추출에 대해 요동하지 않는다" | `decor.overlap-concentration.s1` |
| 상태 첨자 $\alpha$ | $\langle\cdot\rangle_\alpha$ (밀도 $\alpha$ 와 충돌, pure state 첨자) | $\langle\cdot\rangle_d$ (prefix 조건부 기대값) | `decor.covariance-definition` physics |
| 평균장 대체 | "cavity 계산에서 \"상태 안에서는 평균장으로 대체\"" | "\"한 물리적 pure state 안에서는 spin을 평균장으로 대체\"하는 단계에 해당하고, 여기서는 보조 계층 prefix가 그 자리에 있다" | `decor.projection-bound`, glossary `g:projection` |
| Ruelle cascade | L0 본문 괄호, L1 바닥, rules.md 바닥, P6 차이(R번호와 함께) | L0·L1·rules 바닥에서 삭제. P6 차이에는 "intuition, 각 항목의 물리 대응 칸" 표시와 함께만 남음 | L0, L1, rules.md |
| Ghirlanda–Guerra / stochastic stability | rules.md 바닥, P7 차이, 카드 `decor.conditional-concentration.s2.s1`·`decor.overlap-concentration.s2`의 physics | physics와 규칙 문장에서 삭제. 이름은 `g:tree-identity`의 물리 대응 칸(intuition)에만 있고, gap에는 "논문은 같다고 하지 않는다"는 진술로만 남음 | rules.md, 두 카드 |
| ultrametric | physics의 "ultrametric tree의 topology", "ultrametric replica tree" | "보조 계층 tree의 topology", "replica tree" | `decor.overlap-concentration`, `decor.section`, `x.decor-topology` |
| 깊이 = 상태 계층 | "(R11, R19의 사전에서 깊이 $d$ = 상태 계층의 $d$단계)" | 삭제. gap에 "깊이 $d$ 를 물리적 pure state 계층의 단계로 읽지 않는다" 추가 | `x.decor-topology` |
| clustering | 정의 없이 R22 인용 | `[[g:clustering]]`로 연결, 항목에 양·평균·극한 순서·singleton 구분 | P8, L1 수 5, 카드 7장 |
| 이웃 cavity field의 독립 | 규칙 문장 안 설명만 | `[[g:independent-copies]]`로 연결, 정확한 진술(`comp:insertion-comparison`, `comp:pattern-error`) | P8, P11, L1 수 6, `decor.conditional-concentration` |
| 집중 / self-average | score와 multioverlap에 같은 말 | `g:self-average`가 두 정량 진술(score: $e_{\nu,N}\to0$, multioverlap: 깊이 평균 분산)로 묶음 | P5, P9, L1 수 3, 카드 3장 |
| 항등식 이름 | "GG형 항등식"(확신이 낮은 대응 제목) | "prescribed-tree 항등식"(`g:tree-identity`). 역할은 L1 수 4·5와 P7 차이에 "이것과 tree 표본 규칙만으로 수 5–6이 모형과 무관하게 나온다(`decorrelation.tex` 4–9, `cavity.tex` 13–14)"로 적음 | L1, rules.md, glossary |

추가로 L0, L1, rules.md, 카드 43장에 용어의 첫 출현마다 링크를 걸었다. 표 밖에서는 `[[g:slug|표시어]]`를 써서 원래 낱말을 그대로 보이게 했고, 규칙 표의 칸 안에서는 `|`가 칸을 나누므로 낱말 뒤에 `([[g:slug]])`를 붙였다. 카드에서는 physics, gap, 본문에만 걸었다(math, title, provides는 건드리지 않음).

## 3. 판단이 필요한 것

1. **"generic 상태"의 새 이름**: "선택된 수열"(`g:selected-sequence`)로 했고, 그 수열 위에서 섭동한 계를 말할 때는 "선택된 섭동계"라고 한 항목에 같이 정의했다. 카드 몇 장은 원래부터 "선택된 perturbed 수열"이라고 써서 그대로 두고 같은 항목으로 연결했다.
2. **항등식의 중립 이름**: 규칙 문장과 L1은 "prescribed-tree 항등식"이다. 카드 본문에는 원래 쓰던 "처방된 tree 항등식"이 남아 있고 같은 항목에 연결되어 있다. 한쪽으로 통일할지 정해 주면 좋겠다.
3. **rules.md의 `상태` 열**: SCHEMA가 규칙 표의 열 이름을 `상태`(= proposed/confirmed)로 고정하고 있어서 용어 규율 2와 부딪친다. SCHEMA와 `tools/`는 손대지 말라고 해서 그대로 두었다. 열 이름을 `승인`이나 `status`로 바꾸는 것을 제안한다(SCHEMA와 파서가 함께 바뀌어야 한다).
4. **규칙 표 안의 링크 꼴**: 칸 안에서는 표시어를 줄 수 없어서 "낱말([[g:slug]])" 꼴이 되었다. 렌더러가 표시어 없는 `g:` 링크를 표제어로 보여 주면 "clustering(clustering)"처럼 두 번 보일 수 있다. 렌더러 쪽에서 `\|` 이스케이프를 지원하거나, 표 안의 `g:` 링크를 작은 아이콘으로 보이게 하는 것을 생각해 볼 만하다.
5. **"clustering"이라는 이름**: 논문은 이 말을 쓰지 않는다("conditional decorrelation", "conditional covariance decays"). 물리 독자를 위해 이름은 남기고 항목의 뜻 칸을 `decor:conditional-concentration`의 결론 하나로 묶었다. 이름을 "조건부 decorrelation"으로 바꾸는 쪽이 더 안전할 수도 있다.
6. **"connected correlation"**: $\lvert S\rvert\ge2$ 이면 $v_N$ 은 여러 replica spin 곱의 공분산이라 물리의 연결 상관함수와 같은 양이 아니다. `g:conditional-covariance`의 물리 대응을 approximation으로 두고 그 한계를 적었지만, 물리 이름을 아예 빼는 것도 고려할 만하다.
7. **`g:self-average` 항목**: 성격이 다른 두 정량 진술을 한 물리 낱말로 묶은 우산 항목이다. 낱말을 규칙 문장에서 빼고 두 항목을 직접 가리키는 편이 더 엄격할 수 있다.
8. **고전적 GG 항등식의 요약**: `g:tree-identity`의 물리 대응 칸에 "새 replica의 overlap은 확률 $1/n$ 으로 기존 replica를 복사"라는 한 줄 요약을 남겼다(예전 rules.md에서 가져옴). 대조용 intuition일 뿐이며, 필요 없으면 지워도 된다.
9. **물리 대응 유형**: Parisi parameter의 $x(q)$ 읽기, power mean의 cascade 읽기, 상태의 pure state 묶음 읽기는 모두 intuition으로 두었다. $\Phi_r$("saddle point 선택"), $\Delta_N$(ASS 증분), multioverlap 집중, 독립 사본 대체는 approximation으로 두었다. 다르게 보면 바꿔 달라.
10. **깨끗하게 정의하지 못한 것**: "branching pattern"은 원문에서 정의된 말이 아니다(`overview.tex`, `introduction.tex`, `comparison.tex` 58에서 비공식적으로만 쓴다). (topology, 깊이 배정)의 짝으로 정했다. "평균장"(projection 항목)도 원문 용어가 아니라 물리 쪽 읽기다. 원문 `model.tex` 140의 "limiting infinite-depth Gibbs state"는 "극한 무한 깊이 Gibbs 측도"로 옮겼다. 원문 낱말 "state"를 이 사이트의 "상태"와 구별하기 위해서다.
