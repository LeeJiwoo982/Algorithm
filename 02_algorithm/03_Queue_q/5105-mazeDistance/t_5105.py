def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = []      # 큐생성
    q.append([i,j])# 시작점 인큐 , 튜플로 묶기도 가능    #출발지가 두곳이나 여러곳 이라면 여기서 for문 돌리기
    visited[i][j] = 1# 시작점 인큐 표시
    # 탐색
    while q:
        ti, tj = q.pop(0)   # 디큐
        if maze[ti][tj] == 3:   # visit(t)
            return visited[ti][tj] - 1 # 경로의 빈칸 수, -1 추가
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로내부고, 인접이고 벽이아니면,
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])# 인큐
                visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2: #만약 스트링으로 받았다면 '2'로 스트링형 표현**
                return i, j

N = int(input())
maze = [list(map(int, input())) for _ in range(N)]

sti, stj = find_start(N)

#결과를 받기. 시작위치, i, j, 크기N
ans = bfs(sti, stj, N)
print(ans)
