# 검토 1 응답 — rules.md / L1.md / L0.md

기준은 `source/sections/*.tex`. 각 발견은 인용된 줄을 직접 읽고 확인했다. 수정 뒤 `tools/check.py --sections decorrelation`의 모든 검사(연결, 사전, 단면 포함)가 통과한다. 세 문서의 모든 노드 ID와 `[[...]]` 는 스크립트로 `\label{...}`/`\label[kind]{...}` 에 있음을 확인했고, 규칙 표의 각 행은 6칸이다.

| finding | 검증 결과 | 조치 | 바뀐 곳 |
|---|---|---|---|
| F1 가설 누락 | 맞음 (`model.tex:5-7, 26-44, 131`) | 엄격한 곱 한계, $f_\ell$ i.i.d., $b\perp f$, $a>0$ 임의($\log a$ 적분 불요), "모든 $n\ge1$", 1차 moment의 정확한 꼴 $\mathbb E\max_s\lvert\theta\rvert+\mathbb E\lvert h\rvert<\infty$ 를 넣었다. P1 노드에 `main:theorem` 추가. | rules.md P1, L0 |
| F2 "factorization은 상한에만" | 맞음 (`reduction.tex:46-58`, `cavity.tex:11-14`) | 하한 쪽 대칭화에 factorization이 한 번 쓰인다고 적었다. 단 "짝수 $p$ 는 상한에만 쓰인다"는 문장은 쓰지 않았다(아래 수정 사항). | rules.md P1 차이, "규칙으로 못 옮긴 것"의 $a$ 제거 항목, "확신이 낮은 대응"에 P1 짝수 $p$ 항목 추가, L0 |
| F3 수 7의 순열 불변성 | 맞음 (`reduction.tex:46-47, 56-58`) | 수 7에 "$f_\ell$ 의 i.i.d.와 $b$ 의 독립(P1) 때문에 $\widehat\theta$ 의 법칙이 순열 불변, 원래 $\theta$ 는 아닐 수 있다"를 넣었다. truncation 뒤 순열 불변 유지(`reduction.tex:63`)와 $K$ 극한 사슬도 넣었다. | L1 수 7 |
| F4 $\varepsilon$, $\eta$, 극한 조립 | 맞음 (`comparison.tex:8-15, 153-156, 233-245`, `perturbations.tex:257-260`) | 수 3에서 $\varepsilon$ 정의, 수 5에서 $\eta$, $\mathcal A_{L,\eta}$ 정의, 수 6에 부등식 사슬 한 줄과 극한 순서 $\limsup_N$→$L\to\infty$→$\varepsilon\downarrow0$, $\eta$ 는 $L\to\infty$ 뒤 $\downarrow0$ 을 넣었다. 부등식 방향을 `comparison.tex:236-245`와 대조했다. | L1 기호, 수 3, 5, 6 |
| F5 ground state 문장 | 맞음 (`consequences.tex:86-125`) | 두 따름정리 모형에 한정, 인과 "그 결과" 제거, $g$ 정의, $\beta^{-1}\cdot$변분값의 극한, $[g,g+\log2/\beta]$, SAT는 단위 가중치·변수당·기대값으로 고쳤다. 가중 SAT($W\ge0$, $\mathbb EW<\infty$)도 따름정리에 포함됨을 적었다(`consequences.tex:40-48`). | L0 |
| F6 P2 "에서만 나온다" | 맞음 (`upper.tex:25-34, 62-67, 110-125`) | 나머지항 꼴은 factorization과 독립 구조에서, 부호는 짝수 $p$ 볼록성과 positivity에서 나온다고 고쳤다. $P$, $B$, $\lambda$ 를 정의했다. L1 수 1의 "음이다"는 "0 이하"로. | rules.md P2, L1 수 1 |
| F7 P7 "원하는 branching pattern" | 맞음 (`perturbations.tex:29, 316-317, 433-436`) | 제약은 anchor와 새 replica 사이의 split 깊이만, 다른 old replica와의 관계는 지정하지 못함, $f$ 는 old tree의 old replica 시험함수로 고쳤다. 같은 과장이 있던 L1 수 4도 고쳤다. | rules.md P7, L1 수 4 |
| F8 P5 "근처로 유지", (iii) | 맞음 (`perturbations.tex:257-266, 406`) | 규칙 문장을 "$2\varepsilon$ 보다 더 넘지 않고, reservoir에서 … self-average, 유한 tree 모멘트 수렴"으로 고치고 (i)–(iii)을 차이 칸에 적었다. L1 수 3에도 모멘트 수렴을 넣었다. | rules.md P5, L1 수 3 |
| F9 P6 `exact` 안의 cascade 동일시 | 맞음 (`trees.tex:7-12`) | 규칙 문장에서 "Ruelle cascade 평균", "cascade에서 뽑은", "Parisi block counting"을 빼고 "tilted kernel로 뽑은 유한 replica tree"로 바꿨다. 이름들은 차이 칸에 intuition으로 옮겼다. 유형은 `exact` 유지. L0의 "Ruelle cascade 평균을 적분한 꼴"도 "물리에서는 그렇게 읽지만 증명은 쓰지 않는다"로 표시했다. 같은 성격인 P7의 "Ghirlanda–Guerra/stochastic stability" 이름도 규칙 문장에서 빼 차이 칸에 intuition으로 적었다(유형 `blackbox` 유지). | rules.md P6, P7, "확신이 낮은 대응" P6·P7 항목, L0 |
| F10 P8/P9 부분수열·$\eta$·$d$, P11 "상관 감쇠" | 맞음 (`decorrelation.tex:4-8, 21, 69, 243`) | P8, P9 차이 칸에 "$N$ 극한은 P5가 $L$ 마다 고른 수열, 대상은 섭동된 reservoir, $\eta>0$ 고정"을, P8에 "$d$ 는 첫 split보다 엄격히 앞선 regular 깊이"를 넣었다. P11은 "그래프 거리에 따른 상관 감쇠가 아니라"로 고치고 P9가 P8에서 나온다는 점을 적었다. | rules.md P8, P9, P11, "확신이 낮은 대응" P11 항목 |
| F11 수 4 "유일한 입력" | 맞음 (`decorrelation.tex:8-9, 337-352`) | "이 항등식들과 tree 표본 규칙·계수 한계(P6)가 수 5의 입력이다"로 고치고 수 5의 규칙에 P6을 넣었다. | L1 수 4, 5 |
| F12 누락 노드 | 맞음 (`comparison.tex:141-156, 195, 205`, `reduction.tex:45-87`, `perturbations.tex:271-279`) | P11에 `cavity:identity`, `tree:log-expansion`, `tree:regular-shapes`, `decor:overlap-concentration`, P12에 `main:theorem`, P5에 `cavity:negligible`, `cavity:increment`(와 `pert:score`, `pert:error`)를 넣었다. P1에도 `main:theorem`. | rules.md P1, P5, P11, P12; "규칙으로 못 옮긴 것" 깊이 평균 항목에 메모 |
| F13 $P_N^{L,\mathbf u}$ 표기, 수 2 | 맞음 (`cavity.tex:25-41`) | P3 차이 칸에 $P_N^{L,\mathbf u}$ 는 power-mean 재귀 뒤 root logarithm 기대값, "bounded"는 $1/2\le\psi\le3/2$ 라고 적었다. 수 2는 "$P_N^{L,\mathbf u}/N-F_N\to0$". 추가로 P3 규칙 문장 자체를 증명된 섭동 류(평균 $N^{3/4}$ 개, 값 $[1/2,3/2]$ 의 단일 site factor)로 좁혔다(검토는 통과로 판정했으나 "$o(N)$ 크기의 bounded 섭동 일반"은 논문이 진술하지 않는다). | rules.md P3, L1 수 2 |
| F14 정의 없는 기호 | 맞음 | L1 기호 줄에 $\alpha$, $p$(R3), $\zeta$, $\mathbf m$(R11, R12), reservoir, $Y_{0,\rm s}$, $Y_{0,\rm b}$(R20), $\mathbf m^{(L)}$, prescribed tree, mark(R21), $Q_k$(R18), $\underline F$ 를 넣고, $\varepsilon$(수 3), $\eta$, $\mathcal A_{L,\eta}$(수 5), perturbation score(수 3)를 쓰는 곳에서 정의했다. rules.md 머리에 $\mathbf m^{(L)}$, $\mathcal M_L=\mathcal M_{r+1}$, reservoir, $P_N^{L,\mathbf u}$, $\underline F$, $\varepsilon$, score $D_\nu$, $e_{\nu,N}$, self-average, prescribed tree, anchor, $\eta$ 를 정의했다. 행 안에서 $t$, $D$(P6), $c_E$, $E$, $f$, $R_E$(P7), $\rho_N$ 의 값(P4), $K$, $M$, $C_k$(P11), P12의 $D$, $d$, $D_K$, $d_K$, $\widehat I$ 를 정의했다. P11의 label 수 $a$ 는 P1의 $a$ 와 충돌하므로 $n_{\rm lab}$ 로 바꿨다. L0에 $0<m_1<\cdots<m_r<1$ 과 $r=0$ 의 경우를 넣었다. "type"은 P5 차이 칸에서 "type $\nu$ 섭동"으로 쓰이고 score 정의와 함께 머리에 있다. "tilt"는 P8에서 기존처럼 괄호로 설명된다. | rules.md 머리·여러 행, L1 기호·수 3·5, L0 |
| L1 닫힘 6: P9, P4가 규칙 목록에 없음 | 맞음 | 수 6의 규칙을 P4, P5, P6, P9, P10, P11로 넓혔다. | L1 수 6 |
| L1 닫힘 7 | 맞음 | F3 조치와 함께 수 7 규칙에 P2(원래 법칙에 상한 적용)를 넣었다. | L1 수 7 |
| L1 닫힘 3: P5가 P3, P4를 쓰는 것이 숨음 | 맞음 | F12 조치(P5 노드에 `cavity:negligible`, `cavity:increment`)로 처리. | rules.md P5 |
| 주장 (b) | 일부 맞음 | F2와 같이 처리. 짝수 $p$ 에 대해서는 아래 수정 사항. | rules.md P1, L0 |
| 주장 (d) 표현 | 맞음 | F10과 같이 처리. "국소 tree 구조를 쓰지 않는다"는 논문의 문장이 아니라 증명에서 읽은 것임을 "확신이 낮은 대응"과 P11 차이 칸에 적었다. | rules.md P11, "확신이 낮은 대응" |

## 기각하거나 고친 발견

- **F2 수정안의 "짝수 $p$ 와 positivity는 상한(P2)에만 쓰인다"**: positivity 부분은 `cavity.tex:13-14`, `overview.tex:47-48`가 직접 말한다. 짝수 $p$ 는 논문이 처음부터 고정하고(`model.tex:3`), 하한 쪽 진술(`comp:bounded-lower`, `overview.tex:46-48`)은 factorization과 positivity만 언급하고 짝수성에 대해서는 말하지 않는다. "짝수 $p$ 는 상한에만"이라고 쓰면 하한이 홀수 $p$ 에서도 선다는, 논문에 없는 주장으로 읽힐 수 있다(검토 자신도 주장 (b)에서 이 점을 지적했다). 그래서 P1 차이 칸은 "짝수 $p$ 는 볼록성으로 상한에 쓰인다; 논문은 홀수 $p$ 의 하한을 주장하지 않는다"로 적었고, L0도 "하한은 … factorization과 positivity 없이 증명"으로만 썼다.
- **F2 수정안의 하한 쪽 factorization 범위**: 대칭화가 쓰는 것은 표현 $e^\theta=a(1+b\prod f_\ell)$ 와 독립 구조($f_\ell$ i.i.d., $b\perp f$)다(`reduction.tex:50-58`). 엄격한 곱 한계는 이 단계에서 따로 쓰이지 않는다($a>0$ 이므로 분자·분모가 양수). 그래서 "factorization의 독립 구조"로 적었다.
- **F13 (P3 통과 판정)**: 검토는 P3을 통과로 판정했지만, 규칙 문장 "크기가 $o(N)$ 인 bounded 국소 섭동"은 논문이 진술한 류(평균 $s_N=N^{3/4}$ 개의 Poisson 단일 site factor, `cavity.tex:20-41`)보다 넓다. 유형이 `weakening` 이므로 규칙 문장이 증명된 것보다 넓으면 안 된다고 보고 문장을 좁혔다.
- 나머지 발견은 검토대로 맞았고, 수정안 문구를 거의 그대로 쓰되 정의되지 않은 기호($P$, $B$, $\lambda$, $c_E$ 등)는 정의를 붙였다.

## 남은 문제

- **decorrelation 귀납 본문**: 검토와 이 응답 모두 `decorrelation.tex:357-524`의 증명 본문을 줄 단위로 대조하지 않았다. P8→P9 내부는 진술 수준(`decor:conditional-concentration`, `decor:overlap-concentration`)에서만 확인했다.
- **물리 이름을 어디에 둘지(검토의 사용자 확인 항목 5)**: P6, P7에서는 cascade, block counting, GG, stochastic stability 이름을 규칙 문장에서 빼 차이 칸에 intuition으로 옮겼다. P5의 "generic", P8의 "상태 안 clustering", P9의 "상태 수준"은 행이 이미 `approximation`/`blackbox`이고 차이 칸이 범위를 적으므로 그대로 두었다. 이 선택은 사용자가 확인해야 한다.
- **R13, R17, R18의 "확정"/"제안 해석" 표시**: 역할 표(이 작업 범위 밖)는 R13 "power mean = Ruelle cascade 평균"을 확정으로 적는다. 논문이 이 동일시를 증명하지 않으므로 역할 표 쪽 표시도 다시 볼 필요가 있다.
- **L1 길이**: 수 6의 사슬과 수 7의 $K$ 극한을 넣어 L1이 조금 길어졌다. 사슬은 한 줄 표시식으로 두었다.
