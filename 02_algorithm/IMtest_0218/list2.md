# 2차원 배열 List2
- 1차원 배열을 묶어 놓은 리스트
### 입력값이 빈 칸 있는 경우
`arr = [list(map(int, input().split())) for _ in range(N)]`
### 빈칸 없이
`arr = [list(map(int, input())) for _ in range(N)]`
### 빈 배열 만들기 N*M
`arr = [[0] * M for _ in range(N)]`
## 2차원 배열 순회하는 법 
- **지그재그**
```python
N, M = 2, 3
arr = [[1,2,3],[4,5,6]]
# 행 우선 순회
for i in range(N):
    for j in range(M):
        f(arr[i][j])    # 필요한 연산 수행

# 열 우선 순회
for j in range(M):
    for i in range(N):
        f(arr[i][j])

# 지그재그 순회
for i in range(N):
    for j in range(M):
        f(arr[i][j + (M - 1 - 2 * j) * (i % 2)])    
```
## 델타 delta 순회
- 기준 좌표에서 4방향의 인접 배열 요소 탐색
```python
di = [0, 1, 0, -1]  # 오, 하, 좌, 상 으로
dj = [1, 0, -1, 0]
arr = [[1,2],[3,4],[2,5]]
N, M = 3, 2
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M: #유효한 인덱스일 때만
                # f(arr[ni][nj])
# or
        # for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        #     ni, nj = i + di, j + dj
        #     if 유효한 인덱스인지 확인
```
## 전치 행렬 순회
대각선 기준으로 대칭인 부분 탐색하기, 바꾸기 가능
- for i: 0-2 > for j : 0-2 > if i<j
- fro i :0-2 > for j : 0-(i-1) >하면 if문 필요 없음
### 역대각선
* N-1-i == j>> for i in range(N): arr[i][N-1-i]
## 비트연산자
| 비트<br/>연산자 | 설명                 |
|-------|--------------------|
| &     | and연산, 비트단위        |
| \|    | or 연산, 비트 단위       |
| <<    | 피연산자의 비트열을 왼쪽으로 이동 |
| \>>   |피연산자의 비트 열을 오른쪽으로 이동|
- `1<<n` : 2^n 원소가 n개일 경우 모든 부분집합의 수
- `i&(1<<j)` : i의 j번째 비트가 1인지 아닌지 검사