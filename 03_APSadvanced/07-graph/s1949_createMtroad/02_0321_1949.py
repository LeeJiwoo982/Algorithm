import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def dfs(r, c, dist, k):
    '''최장등산로 개척'''
    global mx_dist

    # 최댓값 갱신
    if mx_dist < dist:
        mx_dist = dist

    # 다음 좌표 탐색
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 순서 우하좌상
        nr, nc = r + dr, c + dc

        # 범위안에 있으면서 방문하지 않은 곳
        if (
            0 <= nr < N
            and 0 <= nc < N
            and not visited[nr][nc]
        ):
            if arr[nr][nc] < arr[r][c]: # 그냥 이동 가능
                visited[nr][nc] = 1
                dfs(nr, nc, dist + 1, k)
                visited[nr][nc] = 0

            elif k and arr[nr][nc] - K < arr[r][c]:
                temp = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                visited[nr][nc] = 1
                dfs(nr, nc, dist + 1, False)
                visited[nr][nc] = 0
                arr[nr][nc] = temp

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    # 1. 출발지 찾기 = 제일 높은 좌표
    peak = []
    h = -1
    for r in range(N):
        for c in range(N):
            height = arr[r][c]
            if height > h:
                h = height
                peak = [(r, c)]  # 더 높은 봉우리가 나오면 초기화
            elif height == h:
                peak.append((r, c))  # 같으면 좌표 추가

    mx_dist = -1  # 최대등산로 거리 저장
    for r, c in peak:
        visited[r][c] = 1
        dfs(r, c, 1, True)
        visited[r][c] = 0

    print(f'#{tc} {mx_dist}')