import sys
sys.stdin = open('sample_input.txt', 'r')

def find_maze_distance(r, c, N):
    '''출발 인덱스를 통해 도착지 까지의 움직임 횟수를 반환한다.
     출발지와 도착지가 연결되지 않았다면 0을 반환'''
    visited = [[0]*N for _ in range(N)]#visited 생성
    q = []      #큐 생성
    q.append([r, c])        #큐에 출발지 인큐
    visited[r][c] = 1       #처리표시

    while q:    #탐색 큐가 빌 때까지
        tr, tc = q.pop(0)       #처리할 원소 디큐
        if maze[tr][tc] == 3:   #도착했다면? ==3
            return visited[tr][tc] -1 -1

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:    #도착안했으면 미로 탐색
            mr, mc = tr + dr, tc + dc
            if 0<= mr < N and 0<=mc<N and maze[mr][mc] != 1 and visited[mr][mc] == 0:
            #mr, mc는 배열 범위에 들어야 하고 벽이면 안되고 방문하지 않은 곳이어야 한다.
                q.append([mr, mc])  #처리가능한 방향 enqueue
                visited[mr][mc] = visited[tr][tc] +1
    return 0

def find_s(N):
    '''2차원 배열arr과 배열의 크기N을 통해 출발지S의 인덱스를 찾는다'''
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c

T = int(input())
for tc in range(1, T+1):
    N = int(input())    #미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]      #미로의 통로와 벽에 대한 정보 2차원배열
    # 0 통로, 1 벽, 2 출발, 3 도착

    Sr, Sc = find_s(N)   #출발지 인덱스

    #출발에서 도착까지 가는 데 지나야 하는 최소한의 칸 수, 없으면 0
    ans = find_maze_distance(Sr, Sc, N)
    print(f'#{tc} {ans}')
