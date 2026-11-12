# 용어집 추가 제안 — §4 upper, §5 cavity 카드에서

조율 세션이 `layers/glossary.md` 에 합친다. 묶음은 "모형" 끝(`g:permutation-invariance` 뒤)을 제안한다.

### g:bounded-law — 유계 법칙 (하한의 가정)
- **기호**: $B(\theta)\le B$, $\lvert h\rvert\le H$ a.s.
- **뜻**: 상호작용의 sup-norm $B(\theta)=\max_s\lvert\theta(s)\rvert$ 와 장 $\lvert h\rvert$ 가 결정적 상수 $B$, $H$ 로 a.s. 눌린다는 조건이다. 하한(§5–§8)은 이것과 [[g:permutation-invariance]]를 함께 가정한다(`cavity.tex` 11–14).
- **역할**: 섭동과 삽입의 항별 비용($\log2$, $B$)과 $\lvert\log Y_{0,\rm s}\rvert\le H+BK_{\rm s}$, $\lvert\log Y_{0,\rm b}\rvert\le BK_{\rm b}$ 를 결정적으로 만들어 증분의 균일 유계성을 준다(`cavity:increment`, P4). §8 비교의 $C=H+BM$, $z=\cosh C$ 정규화(`comparison.tex` 200)도 이것에 기댄다. 일반 법칙은 [[g:truncation]]과 [[g:stability]]로 이 경우에서 넘어온다(P12).
- **정의 위치**: `x:cavity-bounded`, `cavity.tex` 11–14
- **물리 대응**: 없음. 물리 유도는 보통 유계 coupling을 놓고 이 조건을 의식하지 않는다.
- **쓰지 않는 뜻**: 상한(`upper:bound`)의 가정이 아니다. 상한은 1차 moment (2.1)만 요구하고, $b$ 와 $f$ 의 본질적 유계성은 가정이 아니라 (2.3)과 독립성에서 나온 결과다(`upper:bound.s1`).
