import sys
sys.stdin = open('sample_input.txt', 'r')
# prim
# 인접 정점 중 가중치 제일 작은 정점부터 선택

import heapq

T = int(input())

def prim(s):
    '''프림알고리즘으로 최소비용신장트리 만들기'''
    global adj, V
    pq = []   # 시작, 거리 짧은 순서대로 저장할 우선순위 큐(힙)
    visited = [False] * (V + 1)     #트리에 포함된 정점과 아닌 것 구별
    
    # 첫 인큐
    heapq.heappush(pq, (0, s))    # 거리 0 ,시작 노드

    dist = 0    #최소신장트리 길이
    cnt = 0     # 선택된 노드 개수
    while pq:
        w, node = heapq.heappop(pq) # 꺼낼 때 비로소 선택됨

        if visited[node]:   # 후순위로 이미 선택된 노드 존재. 무시함
            continue

        visited[node] = True    # 정점 트리에 포함
        dist += w
        cnt += 1

        if cnt == V+1:
            break

        # 현재 선택된 정점 ~ 아직 트리에 포함 안된 이웃 노드의 거리 갱신
        for nei_w, nei in adj[node]:
            if not visited[nei]:
                heapq.heappush(pq, (nei_w, nei))    # 새로운 거리

    return dist

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접행렬
    # graph = [[0] * (V + 1) for _ in range(V+1)]
    # for i in range(E):
    #     n1, n2, w = map(int, input().split())
    #
    #     graph[n1][n2] = w
    #     graph[n2][n1] = w

    # 인접리스트
    adj = [[] for _ in range(V + 1)]    # 0번 ~ V번 노드
    # 이웃 정점 저장
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((w, n2))
        adj[n2].append((w, n1))
        # 무향그래프

    dist = prim(0)  # 0번 노드부터 시작해서 실행 #시작은 임의로 해도 괜춘
    print(f'#{tc} {dist}')