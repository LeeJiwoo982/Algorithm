import sys
sys.stdin = open('input.txt', 'r')

def is_arrive(r, c, arr, N):
    '''출발점 인덱스를 받고 도착했는지 여부 반환
    도착 가능 1, 불가 0'''
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append([r, c])
    visited[r][c] = 1

    while q:
        tr, tc = q.pop(0)
        if arr[tr][tc] == 3:
            return 1
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1,0]]:
            mr, mc = tr+dr, tc+dc
            if 0<=mr<N and 0<=mc<N and arr[mr][mc]!=1 and visited[mr][mc]==0:
                q.append([mr,mc])
                visited[mr][mc] = visited[tr][tc] +1
    return 0
    # pass

def find_start(arr, N):
    '''배열에서 출발지2를 찾는다'''
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                return r, c
    # pass
T = 10
for tc in range(1, T+1):
    input()
    N =16
    maze = [list(map(int, input())) for _ in range(N)]
    # 1 벽, 0 길, 2 출발, 3, 도착
    sr, sc = find_start(maze, N)

    ans = is_arrive(sr, sc, maze, N)
    print(f'#{tc} {ans}')