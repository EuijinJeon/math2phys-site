# 용어집 추가 제안 — §2 model 카드에서

조율 세션이 `layers/glossary.md` 에 합친다. 묶음은 "모형" 끝을 제안한다.

### g:disorder — 물리적 disorder
- **기호**: $M_N$, $\theta_k$, $h_i$, $i_{\ell,k}$; 시행 functional에서는 $k$, $\theta,\theta_1,\ldots$, $h$
- **뜻**: 모형과 시행 functional에서 보조 message가 아닌 무작위 변수 전부다: factor 개수, factor의 site index, factor별 상호작용, site별 장. 시행 사슬($\eta^\omega_d$, $x^\omega$)은 이것과 독립이다(`model.tex` 79–80). power mean $T_d$ 의 조건부 기대값은 이것을 고정한 채 보조 message만 적분하고(`model.tex` 97, 109–110), 바깥의 $\mathbb E$ 가 이것을 평균한다.
- **역할**: $F_N=\frac1N\mathbb E\log Z_N$ 의 quenched 평균(`model:hamiltonian`), $\mathscr F_d$ 의 생성원(`model:power-means`), `model:trial-bounds`의 한계가 disorder만의 함수라 모든 $\mathscr F_d$ 에 가측이라는 점에 쓰인다. reservoir에서는 섭동 factor의 개수·type·site와 선택된 매개변수가 root에 더해진다([[g:state]] 뜻 칸).
- **정의 위치**: `model:hamiltonian`, `model.tex` 9–23, 79–80, 90–91, 109–110
- **물리 대응**: exact — quenched disorder. 평균 $\mathbb E\log Z$ 가 quenched 평균이다.
- **쓰지 않는 뜻**: 시행 message $x$ 와 사슬 $\eta_d$ 는 disorder가 아니다(물리의 annealed 평균과 혼동하지 않는다).
