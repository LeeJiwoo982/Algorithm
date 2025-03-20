import sys
sys.stdin = open('sample_input.txt', 'r')

import heapq
T = int(input())

def dijkstra(sr, sc):   # 출발 인덱스
    '''누적 가중치 최소로 최단거리'''
    pq = [(0, sr, sc)]
    dists = [[INF] * N for _ in range(N)]
    dists[sr][sc] = 0

    while pq:
        dist, nr, nc = heapq.heappop(pq)

        # 종료조건
        if nr == N-1 and nc == N-1:
            return dist
        
        
        if dists[nr][nc] < dist:   # 뽑힌 누적값이 저장된 누적보다 많으면 넘어가기=버리기
            continue
            
        # 상하좌우 인접 정점과의 가중치 계산
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nxr, nxc = nr + dr, nc + dc
            if (
                0<=nxr<N
                and 0<=nxc<N
                and not visited[nxr][nxc]
            )


for tc in range(1, T+1):
    N = int(input())
    h = [list(map(int, input().split())) for _ in range(N)]
    # start : 0, 0 / end : N-1, N-1
    # 출발에서 도착으로 최소 연료소비량으로 도착하기
    # 누적해서 최단거리 도착

    INF=  int(21e8)
    result = dijkstra(0, 0)

    print(f'#{tc} {result}')