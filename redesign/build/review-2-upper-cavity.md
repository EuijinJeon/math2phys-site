# 검토 2 — §4 upper, §5 cavity 노드 카드 (독립 검토)

대상: `cards/upper.*.md` 10장, `cards/cavity.*.md` 9장, `cards/x.cavity-*.md` 4장, 모두 23장.
기준: `source/sections/upper.tex`(128줄), `cavity.tex`(121줄) 전체. 그리고 `model.tex` 전체, `trees.tex` 1–257, `perturbations.tex` 1–110·245–285, `comparison.tex` 1–35·160–246, `reduction.tex` 전체, `decorrelation.tex` 1–12, `overview.tex` 전체.
"확인"은 원문과 한 줄씩 대조했거나 손으로 다시 계산했다는 뜻이다.

주의: `layers/glossary.md`(읽은 시점 516줄, 67항목), `layers/rules.md`, §2·§3 카드는 검토 중에 다른 작업으로 바뀌고 있었다. 그 파일의 인용은 내가 읽은 시점의 문구다. `tools/check.py --sections upper,cavity --out <scratchpad>` 결과: 형식·정초·포함·의존·연결·순환·사전·단면 통과, 용어만 실패 2건(`[[g:bounded-law]]` 가 아직 용어집에 없음. 제안 항목이 합쳐지면 풀린다).

## 요약

- 읽은 카드: 23 / 23 (머리말과 본문 모두).
- `math` 칸의 식 전사: §4의 퇴화 경우 식, $\lVert b\rVert_\infty$·$\lVert M\rVert_\infty$ 한계, $\varphi(1)$·$\varphi(0)$, (4.1), $\bar f$, (4.2)와 $w$ 의 식, $P_{\mathcal T}$·$B_{\mathcal T}$, (4.3); §5의 (5.1)–(5.7), $K_{\rm s}$·$K_{\rm b}$ 의 법칙, Poisson 분해의 세 평균, $\alpha N-\rho_N$, 맞춤 비용 식, $\lvert\log Y_0\rvert$ 상계를 원문과 대조했다. 부호, 계수, 첨자, 양화사, 균일성의 범위가 어긋나는 곳은 **찾지 못했다**.
- 작성자가 보탠 계산은 모두 다시 계산했고 **틀린 것을 찾지 못했다**(아래 "작성자 보탬 검산").
- 증명 분해에 구멍은 없다. `upper:bound` 의 다섯 단계와 `upper:derivative` 의 세 자식(58–68 / 70–94 / 96–126), `cavity:increment` 의 네 단계(71–85 / 87–98 / 100–107 / 108–115)는 원문 증명을 빠짐없이, 순서를 바꾸지 않고 덮는다.
- `uses` 그래프: 순환 없음(손으로도 확인). `upper:*`, `cavity:*`, `x:cavity-*` 어느 카드에서도 `main:*`, `x:model-moment-finiteness`, `comp:*`, `pert:*`, `decor:*`, `reduction:*` 에 닿지 않는다. 작성자의 설계(main:theorem → upper:bound ← x:model-moment-finiteness)는 지켜졌다.
- 용어 규율: "상태"는 `x:cavity-tree-sampling` 의 gap에 한 번, 보조 계층 prefix의 뜻으로만 나온다. $\mathbf u$ 를 root 변수로 쓴 곳은 없다. Aizenman–Sims–Starr는 원문 4–6행의 "follows" 이상으로 쓰이지 않았다. "clustering", "self-average", "처방된 tree 항등식", 주어로서의 "connected correlation", Ruelle cascade, Ghirlanda–Guerra, ultrametricity, stochastic stability는 23장 어디에도 없다.
- 지적 12건. 통과 11장(§4 5장, §5 6장), 지적이 걸린 카드 12장(§4 5장, §5 7장).

| 섹션 | 카드 | 통과 | 지적 걸림 |
|---|---|---|---|
| §4 upper | 10 | 5 | 5 |
| §5 cavity | 13 | 6 | 7 |

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 | 0 | — |
| 구멍 | 0 | — |
| 유형 오류 (`abstraction`) | 1 | F1 |
| 누수 (인터페이스·`uses`·표) | 6 | F2, F3, F4, F5, F6, F10 |
| 과장·부정확한 묘사 | 3 | F7, F8, F9 |
| 용어 | 2 | F11, F12 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | — |
| 중간 | 2 | F1, F2 |
| 낮음 | 10 | F3–F12 |

## 지적 (심각도 순)

### F1. 유형 오류 — `cavity:increment.s3`, `cavity:increment.s1` (physics, `abstraction: exact`) · 중간
- 카드 (`s3` physics): "$N+1$ 계의 새 spin을 합해 없애면 reservoir에 site 삽입 $2A_{\rm s}$ 를 곱한 것이 되고, $N$ 계는 reservoir에 bond 삽입 $A_{\rm b}$ 를 곱한 것이다 … 두 계의 차가 $\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}$ 이다." gap: "오차 $O(N^{-1/4})$ 은 $L$, $\mathbf u$ 에 균일하다." 유형 `exact`.
- 카드 (`s1` physics): "spin 하나를 더하면 그 spin에 붙는 factor가 평균 $\alpha p$ 개 생기고, 옛 spin들 사이의 factor는 평균 $\alpha N$ 개보다 $\alpha(p-1)$ 개 적다." gap: "평균은 $O(N^{-1})$ 오차를 갖고". 유형 `exact`.
- 원문: cavity.tex 101–103 "We may consequently discard the repeated-new-index interactions, match the perturbations, and replace the two insertion count means by their limits at a total expected cost $O(N^{-1/4})$." 76 "$\alpha p(N/(N+1))^{p-1}=\alpha p+O(N^{-1})$", 79 "Terms with at least two new indices have total mean $O(N^{-1})$", 83 "$\alpha N-\rho_N=\alpha(p-1)+O(N^{-1})$".
- 두 물리 문장은 오차 없는 등식으로 적혀 있다. $(N+1)$ 계는 reservoir에 $2A_{\rm s}$ 를 곱한 것과 같지 않다(새 index가 둘 이상인 항, 맞지 않는 섭동, 개수 평균의 차가 남는다). 차이 칸이 오차를 적고 있으므로 참을 잃지는 않았지만, HANDOFF 원칙 1("물리 진술이 증명된 것보다 많이 말하면 차이 칸에 적고 유형을 `approximation`으로")에 따르면 유형이 틀렸다. 부모 `cavity:increment` 의 physics는 "오차는 $o(1)$ 이다"를 담고 있어 `exact` 가 맞다.
- 제안: 둘 중 하나. (가) physics에 오차를 넣는다: `s3` "… 두 계의 차가 $\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}$ 에 $O(N^{-1/4})$ 을 더한 것이다(새 index가 겹친 factor를 버리고 섭동 개수를 맞추는 비용)", `s1` "평균 $\alpha p+O(1/N)$ 개", "$\alpha(p-1)+O(1/N)$ 개 적다", "새 spin이 두 번 이상 들어간 factor는 평균 $O(1/N)$ 개". 그러면 `exact` 유지. (나) 문장을 두고 유형을 `approximation` 으로 바꾼다.

### F2. 누수 — `cavity:negligible`, `cavity:increment.s2` (`uses`, 본문), `cavity:section` ("밖에서 받는 것" 표) · 중간
- 카드 (`cavity:negligible` 본문): "이 곱셈적 한계가 backward recursion을 그대로 통과한다(recursion은 단조이고 root-가측 상수를 그대로 옮긴다)". `uses: [x:cavity-root-logarithm, cavity:factor-bounds, x:cavity-root-convention, tree:original-tilt, model:hamiltonian]`.
- 카드 (`cavity:increment.s2` 본문): "이 곱셈적 한계 … 가 backward recursion을 그대로 통과한다([[tree:original-tilt]]의 recursion의 단조성 …)". `uses` 에 `tree:insertion` 없음.
- 카드 (`cavity:section` 표): "insertion 항등식, 단조·동차성 … | [[tree:insertion]] | 105–111".
- 맞물리는 쪽 (읽은 시점): `tree:insertion` 의 `provides` "§5 cavity.tex 37–38 (cavity:negligible)과 95–98 (섭동 하나가 root log를 log 2 이하로 바꿈)도 단조성", `tree:section` 표의 "§5 cavity (`\ref` 없음) | [[tree:insertion]]의 단조성 … | cavity.tex 37–38, 95–98".
- 원문: cavity.tex 36–37 "Comparing pointwise with the unperturbed spin weight and then applying the recursion gives", 95–96 "Deleting or adding a perturbation changes the root logarithm by at most $\log2$". trees.tex 107–110의 "monotone and homogeneous"는 $Y_d$ recursion에 대한 진술이고 `tree:insertion` 안에 있다. `tree:original-tilt` 카드의 `math`(trees.tex 51–65)에는 단조성 진술이 없다.
- 두 가지가 어긋난다. (1) §3 쪽은 "이 사용은 `tree:insertion` 의 단조성"이라 내주는데 §5의 두 카드는 그것을 받지 않는다. (2) §5 카드가 근거로 든 "`tree:original-tilt` 의 recursion의 단조성"은 그 카드에 없는 사실이다. 수학은 어느 길로도 맞다(직접: $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 는 점별 단조이고 root-가측 상수를 그대로 옮긴다. `tree:insertion` 경유: 섭동 곱 $A=\prod\psi$ 를 `x:tree-extra-variables` 로 넓힌 kernel 위의 insertion으로 보면 $X_0^{\rm pert}-\log Z_N=\log Y_0$ 이고 $2^{-n}\le A\le(3/2)^n$ 에서 단조성). 원문의 "applying the recursion"은 직접 길에 더 가깝다.
- 제안: 한쪽으로 맞춘다. (가) 두 카드의 `uses` 에 `tree:insertion`, `x:tree-extra-variables`(negligible에는 없음)를 넣고 본문을 "섭동 곱을 insertion으로 보면 `tree:insertion` 의 단조성"으로 고친다. `cavity:section` 표의 `tree:insertion` 행에 37–38, 95–98을 더한다. 순환은 없다. 또는 (나) 직접 길을 유지하되 "`tree:original-tilt` 의 단조성"을 "(작성자 확인) power mean은 점별 단조이고 root-가측 상수를 옮긴다. `tree:insertion` 의 단조성과 같은 귀납이다"로 고치고, §3 쪽 `provides`·표의 해당 구절을 고치도록 조율에 넘긴다.

### F3. 누수 — `cavity:increment.s4` (`uses`) · 낮음
- 카드: `uses: [tree:insertion, x:cavity-bounded, cavity:increment.s2, cavity:negligible]`. 본문 "여기에 [[cavity:increment.s2]]–s3의 $O(N^{-1/4})$ 비용을 더하면 큰 $N$ 에서 $\lvert\Delta_N\rvert\le\log2+H+B\alpha(2p-1)+1$".
- 원문: cavity.tex 112–113 "Together with the coupling estimate this bounds the increments for large $N$". $\lvert\log Y_0\rvert$ 상계에서 $\Delta_N$ 의 상계로 가려면 (5.5) 자체가 필요하고 그것은 `s3` 의 결론이다.
- 제안: `uses` 에 `cavity:increment.s3` 을 넣는다.

### F4. 누수 — `upper:bound.s3` (`uses`) · 낮음
- 카드 본문: "[[tree:insertion]]에 따라 그 값은 $\log Y_0$ 이다(새 message label을 쓰는 cavity 상호작용은 [[x:tree-extra-variables]]의 약속으로 들어온다; 이 단계에서는 크기만 쓰므로 `uses`에 넣지 않았다)".
- cavity 상호작용의 증분을 `tree:insertion` 의 $\log Y_0$ 로 읽고 그 단조성으로 $B(\theta)$ 를 얻는 순간, 새 message label을 path kernel에 넣는 약속(trees.tex 135–140)에 기댄다. "크기만 쓴다"는 이유는 `tree:insertion` 을 거치지 않고 power mean의 점별 단조성으로 직접 누를 때만 성립하는데, 본문은 `tree:insertion` 길을 택했다. 조상 `upper:bound` 의 `uses` 에도 `x:tree-extra-variables` 가 없다(형제 `upper:derivative.s1` 에만 있다).
- 제안: `uses` 에 `x:tree-extra-variables` 를 넣는다.

### F5. 누수 — `upper:bound.s2` (`uses`), 맞물리는 `model:trial-bounds` (`provides`) · 낮음
- 카드 본문: "이 값들이 유한하다는 것은 [[model:trial-bounds]]와 같은 논법이다." `uses` 에는 없다. `model:trial-bounds` 의 `provides`(읽은 시점): "upper:bound(\"including unbounded messages\", upper.tex 7–8)".
- 원문: upper.tex는 (2.12)를 `\ref` 하지 않는다. 그러나 47–48의 $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$, 60의 $\mathbb E\log T_0V_{\rm e}$, 진술의 $\mathcal B_r$ 가 시행 message의 moment 조건 없이 유한한 실수라는 것은 model.tex 122–128에 기댄다(upper.tex 7–8이 말하는 "unbounded messages"가 이것이다).
- 주는 쪽은 준다고 하고 받는 쪽은 받지 않는다. 제안: `upper:bound.s2` 의 `uses` 에 `model:trial-bounds` 를 넣는다(순환 없음: 그 카드는 `model:*` 만 쓴다). 아래 (b)에 의견.

### F6. 누수 — `upper:remainder` (`uses`) · 낮음
- 카드 본문: "$\lvert D\rvert\le\lvert b\rvert\prod_\ell M_\ell<1$ 에서 온다([[upper:bound.s1]]의 곱 한계)". `upper:bound.s1` 의 `provides`: "upper:regularization, upper:remainder (모든 moment의 유한성)". 그런데 `upper:remainder` 의 `uses` 에 `upper:bound.s1` 이 없다(`upper:regularization` 을 거쳐 전이적으로만 닿는다).
- (4.3)의 $\mathbb E[(-b)^n]$ 과 $\mathbb E_f$ 의 moment가 유한하다는 것(upper.tex 33–34 "All moments used below are therefore finite")은 이 단계가 직접 쓰는 사실이다.
- 제안: `uses` 에 `upper:bound.s1` 을 넣는다. (확신 낮음) 같은 카드의 `model:integrability` 는 본문 어디에도 쓰이지 않는다. dominated convergence의 지배 함수는 `upper:regularization` 의 일이다. 빼도 된다.

### F7. 과장 — `upper:derivative` (physics, math) · 낮음
- 카드 physics: "interpolation 경로의 각 점에서, 실제 $p$체 factor 하나를 더하는 효과는 cavity factor $p$ 개를 더하는 효과에서 edge 항 $p-1$ 개만큼을 뺀 것을 넘지 않는다." gap: "같은 내용이다." 유형 `exact`.
- 원문: upper.tex 51–53 "$\varphi'(t)/\alpha$ as the **expected** insertion increment …", 113–125. 부등식은 disorder와 tree에 대한 기대값에서만 성립하고, 짝수 $p$ 와 (2.4) 아래에서만 성립한다. 표본별 부등식이 아니다.
- 제안: "… 효과는 [[g:hypotheses|가정]] 아래, disorder 평균에서 … 넘지 않는다."
- 덧붙임: `math` 의 "모든 $t\in(0,1)$ 에서"는 원문 58–61에 없는 범위다. 55행("justifies the derivative on $(0,1)$")에서 온 옳은 보탬이지만 "작성자" 표시가 없다. 표시를 붙인다.

### F8. 부정확한 묘사 — `upper:bound.s2` (physics) · 낮음
- 카드: "$t=0$ 은 각 spin이 $p-1$ 개의 독립 cavity field를 통해서만 factor를 느끼는 계다."
- 원문: upper.tex 38–39 "at each site $i$, independent cavity interactions $U_\theta(x_1,\ldots,x_{p-1};\sigma_i)$ of mean $(1-t)\alpha p$". spin마다 Poisson$(\alpha p)$ 개의 cavity factor가 있고 factor마다 $p-1$ 개의 cavity field가 있다. 카드 문장은 spin당 $p-1$ 개로 읽힌다.
- 제안: "각 spin이 Poisson$(\alpha p)$ 개의 cavity factor를 갖고, factor마다 다른 $p-1$ 개 자리를 독립 cavity field가 채우는 계다."

### F9. 부정확한 묘사 — `cavity:section` (physics) · 낮음
- 카드: "이 비교를 균등 격자의 보조 계층 위에서 하려고 sublinear한 수의 유계 섭동 factor를 넣는다."
- 원문: cavity.tex 6–7 "We add a sublinear number of bounded perturbations to obtain identities for its spin trees." 섭동의 목적은 spin tree의 항등식이다(§6의 일). 보조 계층이 섭동의 보조 변수로 만들어진다는 것은 맞지만(23–24행), 원문이 적은 목적과 다르다.
- 제안: "reservoir의 spin tree에 대한 항등식을 얻으려고(§6) sublinear한 수의 유계 섭동 factor를 넣는다. 보조 계층은 그 factor의 보조 변수로 만든다."

### F10. 누수 (표) — `upper:section` ("인터페이스 점검"), `cavity:section` ("밖에 내주는 것" 표), `cavity:increment.s4` (`provides`) · 낮음
- `upper:section` 본문: "[[tree:section]]의 export 표는 §4에 [[tree:log-expansion]]만 적지만 …". 지금 파일(읽은 시점)의 표에는 "§4 upper:bound (`\ref` 없음)" 행이 있고 `tree:insertion` 과 `x:tree-extra-variables` 가 들어 있다. 문장이 낡았다. 제안: "… 표는 `tree:log-expansion`, `tree:insertion`, `x:tree-extra-variables` 를 적는다. `tree:original-tilt`(41–43, 68)는 빠져 있다"로 고친다(아래 (a)).
- `cavity:section` 표는 §8이 받는 것으로 comparison.tex 20–29, 171, 195, 222만 든다. 원문에는 더 있다: 162 "$\mathbf m^{(L)}=(1/L,\ldots,(L-1)/L)$"(`cavity:grid`), 200 "$C=H+BM$"(`x:cavity-bounded`), 215–216 "the original insertion logarithms, on both sides, are bounded by $H+BK$"(`cavity:increment.s4` 의 상계를 다시 씀), 13–14의 $\Delta_N^{L,\mathbf u_{L,N}}$. 개별 카드의 `provides` 에는 앞의 둘이 있지만 표에는 없고, 215–216은 `cavity:increment.s4` 의 `provides` 에도 없다.
- 제안: 표에 세 행을 더하고 `cavity:increment.s4` 의 `provides` 에 "comparison.tex 215–216"을 더한다.

### F11. 용어 — `build/glossary-additions-upper-cavity.md` 의 `g:bounded-law` (역할, 쓰지 않는 뜻) · 낮음
- 제안문: "섭동과 삽입의 항별 비용($\log2$, $B$)과 $\lvert\log Y_{0,\rm s}\rvert\le H+BK_{\rm s}$ … 를 결정적으로 만들어".
- 원문: cavity.tex 95–96 "Deleting or adding a perturbation changes the root logarithm by at most $\log2$; an interaction changes it by at most $B$." $\log2$ 는 섭동 factor의 한계 (5.2)에서 오고 유계 법칙과 무관하다. 유계 법칙이 주는 것은 $B$ 와 $H$ 다.
- 제안: "삽입과 상호작용의 항별 비용($B$)과 …"로 고친다. 그리고 "쓰지 않는 뜻"에 한 줄 더한다: "섭동 factor의 유계 $1/2\le\psi_\nu\le3/2$ (cavity.tex 6의 'bounded perturbations', P3의 'bounded')를 가리키지 않는다." 원문이 "bounded"를 두 뜻으로 쓰고, `cavity:section` 의 physics도 "유계 섭동 factor"와 "[[g:bounded-law|유계]]"를 한 카드 안에서 함께 쓴다. 역할 칸에 §6의 사용(perturbations.tex 4, 7–8: score 집중이 유계 상호작용·장에 기댄다)도 넣으면 좋다.
- 그 밖의 칸(기호, 뜻, 정의 위치, "상한의 가정이 아니다")은 원문과 맞다. 이름은 reduction.tex 63 "The bounded-law lower bound"에 근거가 있다.

### F12. 용어 — `cavity:increment`, `cavity:increment.s3`, `upper:bound.s2` (physics) · 낮음
- 카드: "site 삽입과 … bond 삽입의 계층 free entropy 변화의 차"(`cavity:increment`), "insertion 하나가 계층 free entropy를 정확히 $\log Y_0$ 만큼 바꾸므로"(`s3`), "계층 free entropy는 site 하나의 site 항 $N$ 개의 합"(`upper:bound.s2`).
- "계층 free entropy"는 용어집에 표제어가 없고 `g:root-logarithm` 의 물리 대응 칸에만 나온다(읽은 시점). 세 카드의 physics에서는 링크 없이 쓰인다(`x:cavity-root-logarithm` 과 `cavity:negligible` 은 `[[g:root-logarithm]]` 을 건다). SCHEMA 용어 규율 1.
- 제안: 세 곳의 첫 "계층 free entropy"에 `[[g:root-logarithm|계층 free entropy]]` 를 건다.

## 작성자 보탬 검산

모두 다시 계산했다. 틀린 것 없음.

**§4**
- 퇴화 경우 (`upper:bound.s1`): $e^\theta=a$, $c=\log a$, $\lvert c\rvert\le B(\theta)$. $Z_N=e^{\sum_kc_k}\prod_i2\cosh h_i$ 에서 $F_N=\alpha\mathbb Ec+\log2+\mathbb E\log\cosh h$. $U_{\theta_j}=c_j$, $C_\theta=e^c$, $V_{\rm s}=\cosh h\,e^{\sum_{j\le k}c_j}$, $\mathcal B_r=\log2+\mathbb E\log\cosh h+\alpha p\mathbb Ec-\alpha(p-1)\mathbb Ec$. 같다. 비퇴화 한계: $\lvert b\rvert>u^{-p}$ 와 $M_\ell\ge u$ $(\ell\le p)$ 가 양의 확률로 함께 일어나면 곱이 1을 넘는다. $M_1>(vu^{p-1})^{-1}$, $\lvert b\rvert\ge v$, $M_\ell\ge u$ $(\ell\ge2)$ 도 같다.
- $\varphi(0)$ 의 인수분해 (`upper:bound.s2`): $t=0$ 에서 $Z=\prod_i2V_{\rm s}^{(i)}$, $k_i\sim\mathrm{Pois}(\alpha p)$. site마다 label이 서로소이므로 $\mathscr F_d$ 조건부로 인자들이 독립이고 $\mathbb E[\prod_iX_i^{m}\mid\mathscr F_d]=\prod_i\mathbb E[X_i^m\mid\mathscr F_d]$ 가 깊이마다 성립한다. $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$.
- Poisson 미분 (`upper:bound.s3`): $\frac d{d\lambda}\mathbb EG(\mathrm{Pois}(\lambda))=\mathbb E[G(n+1)-G(n)]$. 실제 항 $\alpha N\cdot\frac1N=\alpha$, cavity 항 $-\alpha p\cdot\frac1N\sum_i$. 맞다.
- $a(1+\cdots\bar f)$ 꼴 (`upper:derivative.s1`): $e^{U_\theta(x;\varepsilon)}=a(1+bf_p(\varepsilon)\prod_{\ell<p}\bar f_\ell(x_\ell))$, $C_\theta=a(1+b\prod_\ell\bar f_\ell(x_\ell))$. $\sum_sq_x(s)=1$ 로 맞다. edge 삽입은 spin에 의존하지 않고 새 message의 kernel이 prior 그대로라 $Y_d$ recursion이 (2.10)의 $T_d$ 가 된다.
- $\log a$ 의 소거 (`upper:regularization`): $c=\log a+\log(1+D_*)$, 동차성으로 $\log Y_0(a(1+D))-c=\log Y_0(1+D)-\log(1+D_*)$. $w$ 의 항등식: $(1-w)=\frac{1-\lambda}{1+\lambda D_*}$, $w\frac{1+D}{1+D_*}=\frac{\lambda(1+D)}{1+\lambda D_*}$, 합이 $\frac{1+\lambda D}{1+\lambda D_*}$. $w\le1\iff\lambda\le1$. $\frac{1+D}{1+D_*}=e^{\theta(s)-\theta(1,\ldots,1)}\in[e^{-2B},e^{2B}]$, $q_x$ 평균과 1과의 볼록 결합이 구간을 보존한다. $\mathbb Ec$ 의 상쇄 $1-p+(p-1)=0$.
- (4.3) (`upper:remainder`): 실제 $P^p$, cavity $PB^{p-1}$, edge $B^p$. 부호 $(-1)^{n-1}b^n=-(-b)^n$. 기준항 $-\log(1+\lambda D_*)$ 의 상쇄. 볼록성 $x^p\ge y^p+py^{p-1}(x-y)$ 는 짝수 $p$ 에서 $\mathbb R$ 전체에 성립하고, $P_{\mathcal T}$, $B_{\mathcal T}$ 는 음수일 수 있으므로 짝수가 실제로 필요하다. $\mathbb E[(-b)^n]\ge0$ 과 곱해 0 이하. 수렴: root 조건부 $\lVert D\rVert_\infty\le\lvert b\rvert\prod M_\ell<1$, 계수 한계 $\lambda^n/n$ 은 root에 균일.
- s4의 적분: $\varphi'$ 이 $\alpha(1+p)\mathbb EB(\theta)$ 로 눌리므로 $\varphi$ 는 Lipschitz이고 $\varphi(1)-\varphi(0)=\int_0^1\varphi'\le-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$.
- "recursion이 곱셈적 한계를 보존한다"(54행), "삽입 증분 $=\log Y_0$"를 `tree:insertion` 에서 온 것으로 읽은 것: trees.tex 87–88, 107–110과 맞는다. §3에서 "monotone and homogeneous"가 진술된 곳은 그 lemma뿐이다. 읽기에 동의한다.

**§5**
- Poisson thinning (`s1`): 새 index가 $j$ 개일 확률 $\binom pj(N+1)^{-j}(N/(N+1))^{p-j}$. $j=0$: $\rho_N$. $j=1$: $\alpha p(N/(N+1))^{p-1}$. $j\ge2$: $O(N^{-1})$. $\alpha N-\rho_N=\alpha(p-1)+O(N^{-1})$.
- $O(N^{-1/4})$ (`s2`): $\lvert s_{N+1}\tfrac N{N+1}-s_N\rvert\le\lvert s_{N+1}-s_N\rvert+\tfrac{s_{N+1}}{N+1}$, 새 site $\tfrac{s_{N+1}}{N+1}$. $(N+1)^{3/4}-N^{3/4}\sim\tfrac34N^{-1/4}$, $\tfrac{s_{N+1}}{N+1}=(N+1)^{-1/4}$. $N$-spin 계의 섭동은 reservoir와 같은 평균이라 어긋남이 없다.
- $\log2$ 와 $B$ 가 recursion을 통과하는 이유: 어긋난 개수는 root 변수이고 한계가 root-가측이다. 맞다(근거 카드의 귀속은 F2).
- $2A_{\rm s}$ 와 $\log2$ (`s3`): $\sum_\varepsilon e^{h\varepsilon+\sum_j\theta_j(\ldots,\varepsilon)}=2A_{\rm s}$, 동차성으로 $\log Y_0(2A_{\rm s})=\log2+\log Y_{0,\rm s}$.
- $\lvert\log Y_0\rvert$ 의 기대값 (`s4`): $H+B\alpha p$, $B\alpha(p-1)$.
- (5.3) (`cavity:negligible`): $2^{-n}Z_N\le Z\le(3/2)^nZ_N$, $\mathbb En=s_N$.
- "insertion identity for the power means"(105–106) → `tree:insertion` 첫 문단, "independent new root disorder"(56) → `x:tree-extra-variables` "Additional root variables remain quenched"(trees.tex 139–140): 동의한다.

표시 없이 보탠 곳: `upper:derivative` 의 "모든 $t\in(0,1)$ 에서"(F7) 하나를 찾았다. 그 밖에는 없다.

## 통과 카드 (11장)

§4: `upper:bound`, `upper:bound.s1`, `upper:bound.s4`, `upper:derivative.s1`, `upper:regularization`.
§5: `cavity:grid`, `cavity:factor-bounds`, `x:cavity-bounded`, `x:cavity-root-convention`, `x:cavity-root-logarithm`, `x:cavity-tree-sampling`.

(`x:cavity-bounded` 의 `[[g:bounded-law]]` 링크는 용어집에 항목이 합쳐질 때까지 용어 검사에서 실패한다. 카드의 잘못은 아니다.)

## ❓ 세 곳

**(§4) "admissible finite-level trial law" = $\zeta\in\mathcal M_{r+1}$, $0<m_1<\cdots<m_r<1$ ($r=0$ 이면 $\zeta\in\mathcal P(\mathbb R)$).** 동의한다. 근거: (1) model.tex 70–71, 118–119가 시행 법칙을 그렇게 정의하고 다른 제한을 두지 않는다. (2) upper.tex 14 "Consequently $F_N\le\inf_{r\ge0}\Phi_r$"가 성립하려면 admissible 범위가 (2.11)의 inf 범위를 담아야 한다. (3) upper.tex 7–9 "the full trial class, including unbounded messages"가 추가 조건이 없음을 말한다. (4) overview.tex 39–40이 $\zeta_{L,N}\in\mathcal M_L$, $\mathbf m^{(L)}$ 의 값을 "an admissible trial value"라 부르고, reduction.tex 19가 "all trial laws, including $r=0$"이라 쓴다. ❓를 풀어도 된다.

**(§5) (5.3)의 "its parameters".** 문법으로는 "the hierarchy"의 매개변수다. 그런데 16–19행이 $m_d=d/L$ 을 고정해 계층의 지수는 $L$ 로 정해지므로, 지수로 읽으면 "the hierarchy"와 겹친다. $P_N^{L,\mathbf u}$ 의 세 첨자 $L$, $\mathbf u$, $N$ 이 "the hierarchy, its parameters, and $N$"에 하나씩 대응하고, 바로 앞 문단(29–30)이 "The parameters of the factors are denoted by $\mathbf u$"로 "parameters"를 들여오며, lemma도 "uniformly bounded in $N,L,\mathbf u$", "uniform in $L,\mathbf u$"라 쓴다. 받아 쓰는 곳(perturbations.tex 271–274)은 $\pi(d\mathbf u)$ 로 적분하므로 $\mathbf u$ 균일성이 실제로 필요하다. 그래서 "its parameters"는 $\mathbf u$ 로 읽는 것이 맞다고 본다(확신 중간). 카드가 한 것처럼 "증명이 (5.2)와 개수만 쓰므로 어느 읽기에도 균일하다"는 확인은 옳고 안전하다. 제안: gap의 ❓를 "$\mathbf u$ 로 읽는다(첨자 대응, 29–30행, perturbations.tex 271). 지수 $m_d$ 에 대해서도 증명은 그대로 성립한다(작성자 확인)"로 바꾼다.

**(§5) s4 "increasing the constant covers the remaining sizes"의 근거를 `cavity:negligible` 로 읽은 것.** 충분한 근거이고 계산도 맞다: $\lvert\Delta_N\rvert\le(\log2)(s_{N+1}+s_N)+(2N+1)(\log2+\alpha B+H)$ 가 고정 $N$ 에서 $L,\mathbf u$ 에 균일하다($\lvert F_N\rvert\le\log2+\alpha B+H$ 는 $\lvert\log Z_N-N\log2\rvert\le BM_N+NH$ 에서). 다만 유일한 길은 아니다. 맞춤 추정 자체가 모든 $N\ge1$ 에서 유한하고 $L,\mathbf u$ 에 균일하다($\alpha N-\rho_N\ge0$ 은 $p\ge2$ 에서 항상 성립하고, 각 평균과 어긋난 섭동 수의 기대값이 $N$ 마다 유한하다). 원문은 어느 쪽도 적지 않는다. `uses` 에 `cavity:negligible` 을 두고 "작성자 읽기" 표시를 유지하는 것이 맞다. ❓는 "근거가 원문에 없다. 두 길 모두 된다"로 정리하면 된다.

## (a)–(e)에 대한 의견

**(a) `tree:section` 의 export 표 (읽은 시점의 파일).** §4 행은 보강되어 `tree:log-expansion`(81, 97, 121)과 `\ref` 없는 `tree:insertion`(51–54, 91–92), `x:tree-extra-variables`(67–68)를 담는다. 아직 없는 것:
- `tree:original-tilt`: upper.tex 41–42 "Apply the backward power-mean recursion to the spin partition function", 68 "the unperturbed tilted tree". 직접 쓰는 것이라 넣어야 한다.
- `tree:Y-recursion`, `tree:Q-rule`, `x:tree-sampling`: 원문이 81, 120–121에서 "of \cref{tree:log-expansion}"로 가리키므로 `tree:log-expansion` 을 거쳐 전이적으로 들어온다. 표에 없어도 틀리지 않지만, `tree:Q-rule` 의 `provides` 가 이미 "§4 upper.tex 121"을 적고 있으니 표에도 적는 편이 일관된다.
§5 행에는 `tree:insertion`, `x:tree-extra-variables`, `x:tree-sampling` 이 있다. 없는 것: `tree:original-tilt`(cavity.tex 34 "Apply the power-mean recursion", 55–56 "tilted reservoir kernels", 117–118), `tree:Y-recursion`(53–57의 $Y_0$, "insertion recursion"; `provides` 칸에는 있고 표에만 없다). 작성자의 지적은 지금 파일에서도 이 범위로 유효하다. `upper:section` 의 "§4에 tree:log-expansion만 적지만"은 낡았다(F10).

**(b) `model:trial-bounds` 의 `provides` 가 upper:bound에 준다고 적은 것.** 원문 upper.tex는 (2.12)를 인용하지 않고, 증분의 한계는 54행에서 스스로 다시 말한다. 그러나 진술의 $\mathcal B_r$, 48행의 $\mathbb E\log T_0V_{\rm s}$, 60행의 $\mathbb E\log T_0V_{\rm e}$ 가 moment 조건 없이 유한하다는 것은 model.tex 122–128에 기댄다. `provides` 는 틀리지 않았고, 받는 쪽 `uses` 에 없는 것이 어긋남이다. `upper:bound.s2` 에 넣는 것을 권한다(F5). 넣지 않기로 한다면 `provides` 의 문구를 "upper.tex 7–8이 언급(받아 쓰는 카드 없음)"으로 낮춘다.

**(c) `x:model-moment-finiteness` 의 `uses`: `upper:bound` 대 `upper:bound.s1`.** `upper:bound.s1` 이 정확하다. 예고된 내용(비퇴화 경우 $b$, $\max_s\lvert f_1(s)\rvert$ 의 본질적 유계성)은 upper.tex 24–34에만 있고 그 단계는 `model:*` 만 쓴다. `upper:bound` 전체를 쓰면 이 주석이 tree 미적분과 (2.4)에까지 전이적으로 기대게 되는데, (2.4)의 해석을 말하는 주석이 (2.4)를 쓰는 명제에 기대는 꼴이라 보기에도 좋지 않다(순환은 아니다). 기계 검사도 통과한다: model.tex 41의 `\cref{upper:bound}` 는 본문(text) 역할의 뒤쪽 참조라 의존 검사에서 예고로 빠진다(`tools/check.py` 의 의존 절). SCHEMA의 "증명 안의 식 라벨을 인용하면 그 식을 담은 단계 카드를 넣는다"와도 같은 정신이다.

**(d) 규칙 P3, P4 (읽은 시점).**
- P3 "계층 깊이, Parisi parameter, 섭동 매개변수, $N$ 에 대해 균일하다": 원문은 "uniformly in the hierarchy, its parameters, and $N$"(cavity.tex 41)이다. 위 ❓의 읽기대로면 $L$, $\mathbf u$, $N$ 이다. "Parisi parameter"는 원문에 없는 항목이다. 증명으로는 참이지만 §5에서 $m_d=d/L$ 은 고정이라 변하는 양이 아니다. 제안: "계층 깊이 $L$, 섭동 매개변수 $\mathbf u$, $N$ 에 대해 균일하다(증명은 (5.2)와 개수만 쓰므로 지수 $m_d$ 의 선택에도 무관하다)".
- P4 "(Aizenman–Sims–Starr cavity)": 원문은 "This cavity comparison follows the Aizenman–Sims–Starr variational scheme~\cite{ASS03} and its spin-distribution form in Panchenko"(cavity.tex 4–6)라고 쓴다. 이름을 붙이는 것 자체는 원문에 근거가 있고 SCHEMA 용어 규율 3의 금지 목록에도 없다. 다만 머리표만 보면 ASS의 변분 원리를 인용해 쓰는 것으로 읽힐 수 있다. 논문은 $N\to N+1$ 비교의 꼴만 따르고 그 결과를 쓰지 않는다. 제안: "(Aizenman–Sims–Starr식 cavity 비교)"로 바꾸고 차이 칸에 "원문은 이 틀을 '따른다'고만 적는다(cavity.tex 4–6)"를 한 구절 넣는다. `cavity:section`, `cavity:increment` 의 gap이 이미 그렇게 적었다. P4의 수학 노드 `cavity:identity`, `cavity:site-insertion`, `cavity:bond-insertion` 과 차이 칸의 `cavity:reservoir-mean` 은 카드가 없는 식 라벨이다(검사는 graph.json의 라벨로 통과한다). 카드로는 모두 `cavity:increment` 다.

**(e) 용어집 `g:perturbation` 의 $\psi_\nu$ 구간 (읽은 시점: 뜻 칸 "$\psi_\nu\in(1/2,3/2)$", 물리 대응 칸 "값 $(1/2,3/2)$").** 틀리지 않았다. 원문에 두 진술이 있다: 틀의 조건은 닫힌 구간 "$1/2\le\psi_\nu\le3/2$"(cavity.tex 25–27, (5.2)), 구체적 factor는 열린 구간 "In particular $1/2<\psi_\nu<3/2$"(perturbations.tex 60; $t_\nu\le1/4$, $u_\nu\le2\cdot4^{-4}$ 이라 $\lvert\psi_\nu-1\rvert<1/2$). 용어집의 뜻 칸은 구체적 factor를 정의하므로 열린 구간이 맞고, P3과 `cavity:factor-bounds` 는 틀의 조건이라 닫힌 구간이 맞다. 혼동을 막으려면 `g:perturbation` 의 뜻 칸에 "(§5의 틀이 요구하는 것은 $1/2\le\psi_\nu\le3/2$, cavity.tex 26)"을 한 구절 더하면 된다. 고칠 오류는 아니다.

## 분해와 식 라벨에 대한 메모

- `upper:derivative` 아래 세 자식: `upper:derivative.s1`(58–68, 세 삽입의 꼴과 edge 증분), `upper:regularization`(70–94), `upper:remainder`(96–126). 원문의 세 문단("We claim …", *Normalization*, *Convexity*)과 일치한다. 126행이 `upper:remainder` 와 `upper:bound.s4` 에 걸치는 것은 한 줄에 두 문장이 있어서이고 카드가 그렇게 적었다. 문제없다.
- (5.4)–(5.7)을 `cavity:increment` 한 장에 담은 것: comparison.tex 195, 222의 `\eqref{cavity:identity}` 는 graph.json에서 container가 `cavity:increment` 라 `uses` 에 그 카드를 넣으면 의존 검사를 통과한다. §3의 선례(`tree:updated-kernel`, `tree:density`, `tree:log-series` 를 lemma·식 카드 안에 담음)와 같은 처리다. 맞물린다. §8 카드를 쓸 때 `comp:insertion-comparison` 의 `uses` 에 `cavity:increment` 를 넣으면 된다.
