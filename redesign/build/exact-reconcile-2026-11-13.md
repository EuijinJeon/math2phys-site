# exact 판정 두 감사의 대조와 반영 (2026-11-13)

대상은 두 감사다.
- 감사 X (Claude): `build/exact-audit-2026-11-13.md`. 76장 모두 exact로 유지하고 4장의 문구를 고쳤다. 이 변경은 커밋 5c3699f에 들어 있다.
- 감사 Y (GPT): `/tmp/astra-exact-audit.md`와 `/tmp/astra-cards.diff`(기준 01af1b7). 13장을 weakening으로 내리고 31장을 고쳤다. 작업 트리에는 반영되지 않았었다.

방법은 다음과 같다. Y가 고친 31장을 하나씩 원문 줄(`source/sections/*.tex`)과 대조했다. 31장에는 X가 고친 4장(`comp:encoding.s4`, `decor:depth-continuity.s1`, `tree:extension-expansion`, `x:tree-differentiation-rule`)이 모두 들어 있다. diff를 그대로 적용하지 않았다. 지금 작업 트리의 카드를 다시 읽고 `physics`, `gap`, `abstraction` 줄만 고쳤다. `provides` 줄, `math`, `source`, `uses`, `status`는 건드리지 않았다. `status`는 모두 `proposed`다.

## 판정 기준 (이번에 채택)

Y의 기준을 SCHEMA 정의에 맞는 것으로 받아들였다. 증명 전개를 생략하면 exact로 둔다. 정의의 결합 법칙, 명시적 정량 결론, 적용 범위를 생략하면 그대로 두어서는 exact가 될 수 없다. 다만 물리 문장이 수학 진술의 복사본이 되지 않도록, 빠진 것을 세 갈래로 나눠 처리했다. 같은 종류는 모든 카드에서 같은 방식으로 다뤘다.

| 빠진 것의 종류 | 처리 | 적용한 카드 |
|---|---|---|
| (A) 정의·가정의 짧은 성분: 독립성, 결합 법칙, 정규화, 좌표 약속, 정의역(initial stem), 고정 약속 | `physics`에 한 구절로 넣고 exact 유지 | `cavity:factor-bounds`, `model:hamiltonian`, `model:chain`, `model:site-message`, `x:model-depth-zero`, `x:tree-path-kernels`, `x:tree-sampling`, `tree:multioverlap`, `decor:covariance-definition`, `x:decor-mesh`, `comp:encoding.s1`, `comp:encoding.s4`, `cavity:increment.s1` |
| (B) 카드의 주 결론이 식 하나인데 물리 문장에 없음 | 그 식을 `physics`에 넣고 exact 유지. 증명 단계의 중간 상수는 증명 전개로 본다 | `models:ground.s2`, `main:theorem.s3`, `comp:insertion-comparison.s1.s3`, `upper:bound.s1`, `upper:bound.s2`, `upper:derivative.s1`, `main:theorem.s1` |
| (C) 정량 결론이나 적용 범위가 여럿이라 한 구절에 들어가지 않음 (개요 카드) | `gap`에 적고 weakening | `models:section`, `reduction:section` |
| (D) 적용 범위의 짧은 한정어(어느 적용에서만 맞는가) | `physics`에 넣고 exact 유지 | `tree:Y-recursion`, `tree:first-variation`, `tree:log-expansion`, `decor:depth-continuity.s1` |

(C)는 기존의 다른 섹션 카드들과 일관된다. `tree:section`은 weakening이고, 나머지 섹션 카드와 `x:overview-strategy`는 approximation이다. X가 이미 weakening으로 둔 3장도 같은 기준에서 맞다. `cavity:increment`는 정량 성분 여럿과 균일성이 빠졌고, `tree:extension-expansion`은 딸린 진술 넷이 빠졌고, `x:decor-topology`는 정의 낱말 여섯이 빠졌다. 세 경우 모두 한 구절로는 넣을 수 없다. 그래서 그대로 둔다.

Y의 diff는 weakening으로 내린 카드의 `gap` 앞에 "물리 문장은 … 생략한 약화다"를 붙이면서 바로 뒤의 "정확하다." 또는 "같은 내용이다."를 남겼다. 한 칸 안에서 두 문장이 서로 어긋난다. 이번에 weakening으로 내린 두 장에서는 "정확하다."를 지우고 그 자리에 개요 문장을 썼다.

## 요약

- **최종 weakening (Y가 새로 내린 13장 기준): 2장.** `models:section`, `reduction:section`. 나머지 11장은 빠진 성분을 물리 문장에 넣고 exact로 둔다. 11장은 다음과 같다: `cavity:increment.s1`, `comp:encoding.s1`, `comp:insertion-comparison.s1.s3`, `main:theorem.s3`, `model:chain`, `model:hamiltonian`, `upper:bound.s1`, `upper:bound.s2`, `x:model-depth-zero`, `x:tree-path-kernels`, `x:tree-sampling`.
- **카드 전체 유형 수**: exact 76 → **74**. weakening 19 → **21**.
- **고친 카드: 31장**(Y가 고친 31장과 같은 집합). 수정 39곳. 31장 모두에서 Y가 짚은 빠진 내용이나 잘못된 문장 자체는 원문으로 확인되어 반영했다. 그대로 받은 것, 문구를 고쳐 받은 것, X와 병합한 것(4장), 유형 판정만 기각하고 빠진 내용은 물리 문장에 넣은 것(11장)이 섞여 있다. `upper:bound.s2`에서는 두 감사가 모두 놓친 정규화도 함께 고쳤다.
- **기각**: 내용 지적을 통째로 기각한 카드는 없다. 기각한 것은 위 11장의 "weakening" 유형 판정뿐이다.
- **사실 정정 7건**: `x:tree-differentiation-rule`, `model:vs`, `models:section`, `model:factorization`, `upper:remainder`, `main:theorem.s1`, `upper:bound.s2`(마지막 것은 두 감사가 모두 놓쳤다).
- 검사: `python3 tools/check.py --out /tmp/reconcile-check.md`의 결과는 오류 0이다. 10종 가운데 9종이 경고 0으로 통과했다. `대칭`은 알려진 경고 4건이다.

### 사실 정정 목록

| 카드 | 고치기 전 문장의 문제 | 원문 |
|---|---|---|
| `x:tree-differentiation-rule` | 0이 아닌 $\boldsymbol t$에서 붙는 인자는 $D_j$가 아니라 $D_j/A$다. protected leaf는 "이미 $D$를 받은 leaf"가 아니라 "leaf 인자 $A^a$가 분모로 상쇄된 leaf"다. canceled-anchor 전개의 anchor는 $D$를 받지 않고도 처음부터 protected다. fresh path는 updated kernel로 뽑으며 그 leaf도 protected가 된다 | trees.tex 180–183, 192–200 |
| `model:vs` | $V_{\rm s}$는 site 분배함수 자체가 아니라 그것을 2로 나눈 양이다 | model.tex 85 |
| `models:section` | "quenched pressure가 inf이다"는 유한 $N$의 등식으로 읽힌다. 실제 결론은 열역학 극한에 대한 것이다 | model.tex 131–134, consequences.tex 19 |
| `model:factorization` (`gap`) | "엄격한 곱 한계와 독립이 $b$와 $\max\lvert f\rvert$를 본질적으로 유계로 만든다"는 퇴화 경우에 거짓이다. $b=0$ a.s.이면 $f$는 유계일 필요가 없다. 원문의 한정은 "in the nondegenerate case"다 | model.tex 39–43, upper.tex 18–30 |
| `upper:remainder` | "$\lambda<1$에서 절대수렴하므로 $\lambda\uparrow1$"은 근거를 잘못 댄다. $\lambda\uparrow1$은 정규화 증분의 지배 한계 $2B(\theta)$와 dominated convergence로 정당화된다 | upper.tex 88–94, 122–126 |
| `main:theorem.s1` | 아무 spin 무관 상수를 빼도 승수 $a$가 사라지는 것이 아니다. $c=\theta(1,\ldots,1)$이라는 선택이 있어야 $\widehat\theta$가 $b,f$만의 함수가 된다 | reduction.tex 49–55 |
| `upper:bound.s2` | "계층 free entropy는 site 항 $N$ 개의 합"은 용어집 `g:site-term`의 $V_{\rm s}$(앞에 $\frac12$)와 맞지 않는다. site마다 $\log2$가 따로 붙는다: $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$ | upper.tex 47–48, model.tex 85 |

## 카드별 표

"X"는 감사 X의 판정과 조치이고 "Y"는 감사 Y의 판정과 조치다. "최종"은 이번 반영 뒤의 `abstraction`이다.

| 카드 | X | Y | 최종 | 분류 | 원문 줄 | 이유와 반영 |
|---|---|---|---|---|---|---|
| `cavity:factor-bounds` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (A) | cavity.tex 20–27 | type별 Poisson 개수의 상호 독립, 독립 균일 site, 곱 prior는 `math`에 있는 정의 성분이다. "무작위 site"를 "독립 균일 site"로 고치고 두 구절을 넣었다 |
| `cavity:increment.s1` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | cavity.tex 71–85 | 남은 $p-1$ index의 독립 균일 법칙과 상호작용 법칙 보존은 짧은 법칙 성분이라 넣었다. 정확한 $\rho_N=\alpha(N+1)(N/(N+1))^p$도 한 식으로 넣었다. $\alpha p(N/(N+1))^{p-1}$ 대신 $\alpha p+O(1/N)$을 쓰는 것은 이 단계가 쓰는 정도(오차는 s3가 $B$로 치른다)이고, 증명 전개의 생략이다 |
| `comp:encoding.s1` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | comparison.tex 28–38 | 균일 site를 넣어 넓힌 root(상태를 정하는 것), $x=\operatorname{arctanh}\langle\sigma_i\rangle$, 유한 $N$에서 $x$가 유한하다는 것을 한 문장씩 넣었다. 지금의 물리 문장은 `math`의 모든 성분을 말한다 |
| `comp:encoding.s4` | 문장 수정 (새 삽입 disorder와 독립) | 문장 보완 (root와 site까지 독립 복사) | exact | 누락 보충 (A); X·Y 병합 | comparison.tex 80–82 | X 문장은 그대로 두었다. Y가 짚은 "reservoir root와 균일 site까지 포함한 구성 전체의 독립 사본"을 더했다. 서로 다른 label이 reservoir disorder를 공유하지 않는다는 점이라, 빠지면 오독을 부른다 |
| `comp:insertion-comparison.s1.s3` | exact 유지 | weakening | exact | 누락 보충 (B); Y 유형 기각 | comparison.tex 181–196 | 이 단계의 주 결론 $\log2+\mathbb E\log\widetilde Y_{0,\rm s}-\mathbb E\log\widetilde Y_{0,\rm b}=\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$를 물리 문장에 넣었다 |
| `decor:covariance-definition` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (A) | decorrelation.tex 94–106 | $d$의 정의역(initial stem 위, 첫 갈라짐 깊이 포함)과 좌표 한계, $0\le v_N\le1$을 넣었다 |
| `decor:depth-continuity.s1` | 문장 수정 (평가 깊이가 initial stem 위를 움직인다) | 문장 보완 (나중 branching 깊이를 고정) | exact | 누락 보충 (D); X·Y 병합 | decorrelation.tex 169–177 | X 문장은 그대로 두었다. 첫머리에 "나중 branching 깊이들을 고정하고 initial stem을 따라 한 path를 뽑을 때"를 넣었다. "계층 깊이를 따라 증가"는 "그 stem 위에서 깊이를 따라 증가"로 고쳤다. tree 전체의 깊이를 아무렇게나 바꿔도 단조라는 뜻이 아니다 |
| `main:theorem.s1` | exact 유지 | exact, 문장 보완 | exact | **사실 정정** + 누락 보충 (B) | reduction.tex 49–59 | $c=\theta(1,\ldots,1)$, $\lvert c\rvert\le B(\theta)$, $\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$를 넣었다. 마지막 것은 s3가 안정성 lemma를 적용할 때 쓰는 결론이다 |
| `main:theorem.s3` | exact 유지 | weakening | exact | 누락 보충 (B); Y 유형 기각 | reduction.tex 70–84 | 물리 문장에 이 단계의 결론 $\liminf_NF_N\ge\inf_r\Phi_r$가 없었다. 넣었다. $2\alpha pD_K+2d_K$는 $K\to\infty$에서 사라지는 중간 손실이라 증명 전개로 보았다. 그래도 짧아서 괄호로 함께 넣었다 |
| `model:chain` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | model.tex 68–81 | 일반 $r$의 사슬(각 label이 $\zeta\in\mathcal M_{r+1}$에서 측도를 뽑고 깊이마다 한 단계씩 내려가 $x$를 뽑는다)과 $0<m_1<\cdots<m_r<1$을 한 문장으로 넣었다. 이제 $r=1$은 예로만 남는다 |
| `model:factorization` | exact 유지 | exact, `gap` 보완 | exact | **사실 정정** (`gap`) | model.tex 38–43, upper.tex 18–30 | 비퇴화 조건을 넣었다. 위 사실 정정 목록 참조 |
| `model:hamiltonian` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | model.tex 9–23 | 모든 족의 상호 독립, 독립 사본, 복원추출, $N$에 무관한 법칙은 정의의 결합 법칙이다. 한 문장으로 들어가므로 넣었다 |
| `model:site-message` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (A) | model.tex 59–63 | 새 spin을 마지막 좌표에 두는 것과 나머지 spin의 독립(곱 $\prod q_{x_\ell}$)을 넣었다 |
| `model:vs` | exact 유지 | exact, 문장 보완 | exact | **사실 정정** | model.tex 85 | "site 분배함수를 2로 나눈 양" |
| `models:ground.s2` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (B) | consequences.tex 112–119 | 결론 부등식 $\limsup_Ng_N\le I(\beta)/\beta\le\liminf_Ng_N+\log2/\beta$를 넣었다 |
| `models:section` | exact 유지 | weakening, 열역학 극한 | **weakening** | **사실 정정** + (C) | consequences.tex 10–22, 36–49, 86–101; model.tex 131–134 | "pressure의 열역학 극한이"로 고쳤다. 개요라서 두 모형의 가정 전체, 장의 척도, 영온도 폭 $[g,g+\log2/\beta]$를 `gap` 첫머리에 적고 weakening으로 내렸다 |
| `reduction:section` | exact 유지 | weakening | **weakening** | (C) | reduction.tex 9–26, 45–87 | 개요다. 정량 안정성 한계, 이동 식, liminf/limsup 조립이 `math`와 자식 카드에만 있다. `gap`의 "정확하다."를 이 문장으로 바꾸었다 |
| `tree:Y-recursion` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (D) | trees.tex 63–65, 67–82 | 정의는 임의의 kernel 열에 대한 것이다. 그래서 "$d=L$에서는 spin 배치의 무게"를 "말단 변수의 무게(Gibbs 적용에서는 spin 배치)"로 고쳤다. 재가중한 kernel이 확률 kernel이라는 것도 넣었다 |
| `tree:extension-expansion` | weakening 유지, 문장 수정 (anchor가 아닌) | weakening 유지, 문장 보완 ($H$ 고정, $D_j$ 유계 실수) | weakening | 누락 보충 (A); X·Y 병합 | trees.tex 264, 279–282 | X의 "anchor가 아니고"를 그대로 두고 Y의 두 조건을 넣었다. Y 문구 "섭동 매개변수와 무관한"은 고정값 $\mathbf u$와 헷갈리므로 "삽입 매개변수 $\boldsymbol t$와 무관한"으로 썼다(X의 `x:tree-differentiation-rule` 수정과 같은 이유) |
| `tree:first-variation` | exact 유지 | exact, 적용 범위 | exact | 누락 보충 (D) | trees.tex 63–65, 142–154 | $L=1$의 Gibbs 읽기 앞에 "$K_L$이 Gibbs kernel인 적용에서"를 넣었다 |
| `tree:log-expansion` | exact 유지 | exact, 적용 범위 | exact | 누락 보충 (D) | trees.tex 63–65, 224–239 | 위와 같다 |
| `tree:multioverlap` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (A) | trees.tex 44–49 | $R_\varnothing=1$과 첨자 없는 $\mathbb E$의 약속을 넣었다 |
| `upper:bound.s1` | exact 유지 | weakening | exact | 누락 보충 (B); Y 유형 기각 | upper.tex 18–34 | 증명 단계의 결론은 "이후 moment가 모두 유한"이다. 이것을 넣었고, 중간 상수 $u^{-p}$, $(vu^{p-1})^{-1}$도 괄호로 넣었다. `gap`의 "같은 내용이다"는 이제 참이다 |
| `upper:bound.s2` | exact 유지 | weakening | exact | **사실 정정** (두 감사 모두 놓침) + 누락 보충 (A, B); Y 유형 기각 | upper.tex 36–49 | 보간의 정의(평균 $t\alpha N$, $(1-t)\alpha p$, 서로 다른 label, quenched 목록, $r=0$ 약속)와 결론 $\varphi(1)=F_N$, $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$를 넣었다. "site 항 $N$ 개의 합"의 $\log2$ 누락을 고쳤다 |
| `upper:derivative.s1` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (B) | upper.tex 66–68 | edge 삽입 증분 $\log T_0V_{\rm e}$(`gap`에만 있던 것)를 물리 문장으로 올렸다 |
| `upper:remainder` | exact 유지 | exact, 문장 보완 | exact | **사실 정정** | upper.tex 88–94, 122–126 | $\lambda\uparrow1$의 근거를 지배 한계 $2B(\theta)$와 dominated convergence로 바로잡았다 |
| `x:decor-mesh` | exact 유지 | exact, 문장 보완 | exact | 누락 보충 (A) | decorrelation.tex 4, cavity.tex 16–19 | $L\ge2$와 unary fresh 계수 $-1/L$을 넣었다 |
| `x:model-depth-zero` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | model.tex 118–120 | $\mathcal B_0(\zeta)=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$와 $\Phi_0=\inf_\zeta$를 한 구절로 넣었다. 식은 `math`와 같고, `gap`이 이미 원문은 식을 적지 않는다고 밝힌다 |
| `x:tree-differentiation-rule` | 문장 수정 ($t_j$로 미분) | 문장 재작성 ($D/A$, protected의 정의) | exact | **사실 정정**; X·Y 병합 | trees.tex 180–202 | Y의 재작성을 받아들였다. 다만 Y 문구 "섭동 매개변수로"는 X가 고친 "$A_{\boldsymbol t}$의 $t_j$로"로 되돌렸다. "$\boldsymbol t=0$에서는 $A=1$이라 붙는 인자가 $D_j$다"를 더해 이전 문장과의 관계를 남겼다. 용어집 `g:protected-leaf`의 뜻 칸은 이미 맞게 적혀 있다 |
| `x:tree-path-kernels` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | trees.tex 16–23 | prefix 전체에 의존하는 임의의 kernel $K_d$, root 분포 고정, $m$의 엄격 증가를 한 문장으로 넣었다 |
| `x:tree-sampling` | exact 유지 | weakening | exact | 누락 보충 (A); Y 유형 기각 | trees.tex 29–39 | unary 구간 보존, 서로 다른 vertex와 같은 값의 구별, $E_{\mathcal T}$가 root 조건부라는 것을 넣었다 |

## 두 감사가 모두 놓쳤다고 본 것

1. **`upper:bound.s2`의 $\log2$ 정규화**(고쳤다). 위 사실 정정 목록 참조. Y는 이 카드를 weakening으로 내리면서도 "site 항 $N$ 개의 합"은 그대로 두었다.
2. **용어집 `g:site-term`의 뜻 칸**(`layers/glossary.md` 120행)은 "$V_{\rm s}$는 … site 분배함수다"라고 적는다. 바로 위 기호 칸의 $\frac12$와 맞지 않는다. `model:vs`와 같은 정정이 필요하다. `layers/`는 이번 작업 범위 밖이라 고치지 않았다.
3. **Y diff의 `gap` 자기모순**: weakening으로 내린 13장 가운데 여러 장(`cavity:increment.s1`, `comp:insertion-comparison.s1.s3`, `main:theorem.s3`, `reduction:section`, `upper:bound.s1` 등)에서 "생략한 약화다" 바로 뒤에 "정확하다."나 "같은 내용이다."가 남았다. Y를 그대로 적용했다면 한 칸 안의 두 문장이 어긋났을 것이다. 이번 반영에서는 생기지 않는다.
4. **`x:model-hypotheses`**(exact, 이번에 손대지 않음): 물리 문장은 "tanh형 factor 전개"라고만 쓰고 엄격한 곱 한계와 독립 구조를 링크(`g:factorization`)에 맡긴다. `model:factorization`은 이제 두 성분을 물리 문장에 적는다. 묶음 카드이고 성분은 자식 카드가 말하므로 exact를 유지할 수 있다. 다만 (A) 기준을 엄격히 적용하면 한 구절을 더할 후보다.

## 사용자 판단이 필요한 것

1. **기준의 기본값.** 이번에는 짧은 정의 성분과 주 결론은 물리 문장에 넣고 exact를 유지했고, 개요 카드만 weakening으로 내렸다(11장에서 Y의 유형 판정 기각). Y처럼 정의·단계 카드도 weakening으로 내려 물리 문장을 짧게 두는 쪽을 원하면 같은 11장의 처리를 뒤집으면 된다. 그 경우 넣은 구절을 `gap`으로 옮긴다.
2. **"Ising spin glass"라는 이름**(`main:theorem`, `model:hamiltonian`). X가 넘긴 항목 4이며 이번에도 고치지 않았다. 정리의 대상은 인수분해 가정을 만족하는 짝수 $p$체 Ising 모형 일반이다.
3. **용어집 `g:site-term` 뜻 칸의 정규화**(위 2). `layers/` 편집 권한이 있는 작업에서 한 구절을 고치면 된다.
4. Y가 권고한 규칙층 점검(P6의 canceled-anchor 입력, P10의 고정 $N,L$·선택된 매개변수·독립 label 조건). 이번 범위 밖이다.
5. 이번 31장 수정은 작성자와 다른 모델의 재대조를 받지 않았다. HANDOFF B-5의 재검토 범위에 넣을지 정해야 한다.

## 검사

`python3 tools/check.py --out /tmp/reconcile-check.md` (반영 뒤)

| 검사 | 결과 |
|---|---|
| 형식, 정초, 포함, 의존, 연결, 순환, 사전, 단면, 용어 | 통과 (오류 0, 경고 0) |
| 대칭 | 경고 4 (오류 0). 이미 알려진 4건이다 |
