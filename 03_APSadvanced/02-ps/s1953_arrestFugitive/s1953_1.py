import sys
sys.stdin = open("sample_input.txt", "r")
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 우하좌상
tunnel = {
    1:[1,1,1,1],
    2:[0,1,0,1],
    3:[1,0,1,0],
    4:[1,0,0,1],
    5:[1,1,0,0],
    6:[0,1,1,0],
    7:[0,0,1,1]
}   # 터널구조물 종류

def bfs(r, c):
    '''r, c에서 시작해서 갈 수 있는 장소에 시간 찍기'''
    global visited, graph, N, M    # 방문처리, 터널형태, N
    q = deque([r, c])   # q 생성 및 인큐
    visited[r][c] = 1

    while q:
        now_r, now_c = q.popleft()
        dir = tunnel[graph[now_r][now_c]]
        for i in range(4):
            if dir[i] == 0:   #터널구조상 갈 수 없음
                continue

            next_r, next_c = now_r + dr[i], now_c + dc[i]
            # 다음 좌표가 범위 않에 없다면
            if (next_r < 0 or
                next_r >= N or
                next_c < 0 or
                next_c >= M):
                continue

            # 방문 한 곳이면
            if visited[next_r][next_c]:
                continue

            # 현재 터널방향과 다음 터널이 연결된 형태인지



    T = int(input())
    for tc in range(1, T+1):
        N, M, R, C, L = map(int, input().split())
        # N, M 지하터널 세로가로 크기
        # R, C 맨홀 위치 세로가로
        # L 탈출 후 소요시간=탈주범이 갈 수 있는 최장거리 계산용

        graph = [list(map(int, input().split()) for _ in range(N))]
        visited = [[0]*M for _ in range(N)]

        bfs(R, C)


