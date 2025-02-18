import sys
sys.stdin = open('imInput.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def dfs(r, c, cnt):
        global mx
        mx = max(mx, cnt)

        mn = arr[r][c]
        next_list = []

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and mn > arr[nr][nc]:
                if arr[nr][nc] < mn:
                    mn = arr[nr][nc]
                    next_list = [(nr, nc)]
                elif arr[nr][nc] == mn:
                    next_list.append((nr, nc))

        for next_r, next_c in next_list:
            dfs(next_r, next_c, cnt + 1)

    mx = 0
    for r in range(N):
        for c in range(N):
            dfs(r, c, 1)

    print(f'#{tc} {mx}')