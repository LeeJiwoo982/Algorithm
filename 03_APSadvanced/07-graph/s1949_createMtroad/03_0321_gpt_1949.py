import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(r, c, dist, chance):
    '''현재 위치에서부터 등산로 거리 탐색 '''
    global mx_dist
    mx_dist = max(mx_dist, dist)

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if (0 <= nr < N and 0 <= nc < N and not visited[nr][nc]):
            if arr[nr][nc] < arr[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, dist + 1, chance)
                visited[nr][nc] = 0

            elif chance and arr[nr][nc] - K < arr[r][c]:
                original = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                visited[nr][nc] = 1
                dfs(nr, nc, dist + 1, False)
                visited[nr][nc] = 0
                arr[nr][nc] = original


for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 출발지점 저장
    highest = max(max(row) for row in arr)
    peaks = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == highest]

    mx_dist = 0
    for r, c in peaks:
        visited[r][c] = 1
        dfs(r, c, 1, True)
        visited[r][c] = 0

    print(f'#{tc} {mx_dist}')