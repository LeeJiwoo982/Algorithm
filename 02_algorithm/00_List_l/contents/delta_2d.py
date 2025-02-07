# 델타
#연습문제로 이차원 배열하면 이정도는 해결해야함ㅠㅠ

### 한 좌표에서 4방향(상하좌우)의 인접 배열 요소를 탐색
#### 다양한 경우로 문제를 변경하는 경우
##### A[i][j] #좌표

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 4방진을 그려서 적용하기

N = 2
M = 3
for i in range(N):
    for j in range(M):
        # print(f'기준좌표: {[i, j]}')
        for dir in range(4):  # 4방향이 기준일 때
            ni = i + di[dir]
            nj = j + dj[dir]
            if (0<=ni <N) and (0 <= nj <M):
                # print(f'{dir}: {[ni, nj]}')
                pass
#특정좌표 인덱스가 정해짐
# i=2
# j=3
# for dir in range(4):  # 4방향이 기준일 때
#     ni = i + di[dir]
#     nj = j + dj[dir]
#     print(ni, nj)

# N*N 배열

### delta 2
N =2
M=3
for i in range(N):
    for j in range(M):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                print([ni, nj])

