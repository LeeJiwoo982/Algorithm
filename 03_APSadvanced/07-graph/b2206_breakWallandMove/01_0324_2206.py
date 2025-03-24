# N×M의 행렬로 표현되는 맵이 있다. 맵
# 에서 0은 이동할 수 있는 곳을 나타내고,
# 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
#
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데,
# 이때 최단 경로로 이동하려 한다.
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데,
# 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
#
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
# 벽을 한 개 까지 부수고 이동하여도 된다.
#
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
from collections import deque
from pprint import pprint
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(r, c, cnt, broken):
    global d
    q = deque()
    q.append((r, c, cnt, broken))
    visited[r][c][broken] = 1

    while q:
        r, c, cnt, broken = q.popleft()

        # 종료조건
        if r == N-1 and c == M-1:
            return cnt

        # 이동
        for dr, dc in d:
            nr, nc = r + dr, c + dc

            if (0 <= nr < N and 0 <= nc < M):
                if arr[nr][nc] == 0 and not visited[nr][nc][broken]:
                    visited[nr][nc][broken] = True
                    q.append((nr, nc, cnt + 1, broken))
                
                # 벽인데 안 부셨을 때
                elif arr[nr][nc] == 1 and broken == 0 and not visited[nr][nc][1]:
                    visited[nr][nc][1] = True
                    q.append((nr, nc, cnt + 1, 1))
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 세로 N, 가로 M
# (1, 1), (N, M)은 항상 0
# 인덱스 1부터 시작 N까지

visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 1, 0))