# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| DO_SETUP | DC_ONE · 곱 차이와 Jensen | [0,0] | 보통 | eq decor:one-vertex-shift | 두 곱을 같은 prefix에서 비교 | $A=\prod_{j=1}^{s}a_j,\quad B=\mathbb E[\prod_{j=1}^{s}b_j\mid\mathscr F_q]$ | decorrelation.tex 179–190 |
| DO_TELE | DC_ONE · 곱 차이와 Jensen | [0,1] | 보통 | eq decor:one-vertex-shift | 곱을 한 인자씩 바꾸기 | $\|\prod_j a_j-\prod_j b_j\|\le\sum_j\|a_j-b_j\|$ | decorrelation.tex 185–191 |
| DO_CS | DC_ONE · 곱 차이와 Jensen | [0,2] | 보통 | eq decor:one-vertex-shift | 제곱합으로 바꾸기 | $\\|\prod_j a_j-\prod_j b_j\\|_N^2\le s\sum_j\\|a_j-b_j\\|_N^2$ | decorrelation.tex 185–191 |
| DO_JEN | DC_ONE · 곱 차이와 Jensen | [0,3] | 보통 | eq decor:one-vertex-shift | 조건부 Jensen으로 결론 | $\mathbb E\\|A-B\\|_N^2\le s\sum_j\mathbb E\\|a_j-b_j\\|_N^2$ | decorrelation.tex 179–193 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | DO_SETUP | DO_TELE | 같은 continuation에서 곱 차이 | 입력 |
| 1 | DO_TELE | DO_CS | 곱 차이를 제곱합으로 | 입력 |
| 2 | DO_CS | DO_JEN | 조건부 Jensen과 기대값 | 입력 |
