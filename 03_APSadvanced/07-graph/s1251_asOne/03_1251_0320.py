import sys
sys.stdin = open('re_sample_input.txt', 'r')

import heapq

T = int(input())

def prim(s):
    '''인접노드의 최솟값으로 최소비용 찾기'''
    global graph, N
    pq = [(0, s)]   # 가중치값
    visited = [0] * N
    weight_mn = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        weight_mn += weight

        for nx in range(N):
            if graph[node][nx] == 0:
                continue
            if visited[nx]:
                continue

            heapq.heappush(pq, (graph[node][nx], nx))
    return weight_mn
    

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = X[i], Y[i]
            x2, y2 = X[j], Y[j]
            L = (x1 - x2) ** 2 + (y1 - y2) ** 2
            w = E * L

            graph[i][j] = w
            graph[j][i] = w

    dist = prim(0)

    print(f'#{tc} {round(dist)}')