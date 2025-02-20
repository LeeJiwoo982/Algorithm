# N*N 배열에 높이 정보
# 높은 수에서 낮은 수로 공굴리기, 그 이동거리 측정
# 무조건 주변 좌표에서 가장 최솟값으로만 이동 <- 이거 알았으면 풀었을 텐데... 그러면 모든 경로 찾을 필요 없었을 텐데 쓋
import sys
sys.stdin = open('imInput.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    mx = 0

    # 기준점 순회
    for r in range(N):
        for c in range(N):
            cnt = 1
            i, j = r, c
            while True:
                mn = arr[i][j]
                next_i, next_j = -1, -1

                for d in range(4):  # 사방값 순회
                    nr, nc = i + dr[d], j + dc[d]  # 사방인덱스
                    if (0 <= nr < N) and (0 <= nc < N):
                        if mn > arr[nr][nc]:  # 사방값이 기준점보다 작을 때
                            mn = arr[nr][nc]
                            next_i, next_j = nr, nc

                if next_i ==-1 and next_j==-1:  #더 작은 값이 없을 때
                    break
                i, j = next_i, next_j
                cnt += 1
            mx = max(mx, cnt)

    print(f'#{tc} {mx}')