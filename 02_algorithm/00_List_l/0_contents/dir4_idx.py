N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni , nj = i +dj, j+dj
            if 0<= ni <N and 0<= nj <N:
                total += abs(arr[ni][nj]-arr[i][j])
print(total)

#