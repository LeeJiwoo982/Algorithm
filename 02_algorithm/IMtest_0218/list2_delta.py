arr = [[1,2,3,8],[4,5,6,0],[7,8,9,12]]
N, M = 3, 4
# 중심 원소에서 상하 좌우 k칸의 최댓값
mx = 0
for i in range(N):
    for j in range(M):
        s = arr[i][j]
        for di, dj in [[0, 1], [1,0],[0,-1],[-1,0]]:
            for c in range(1, k+1): #거리
                ni, nj = i + di*c, j+dj*c
                if 0<=ni<N and 0<=nj<M:
                    s+= arr[ni][nj]
        if mx < s:
            mx = s

#