import sys
sys.stdin = open('sample_input.txt', 'r')

import heapq
# 크루스칼

T = int(input())

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])

    return parents[a]

def union(a, b):
    a_root = find(a)
    b_root = find(b)

    parents[b_root] = a_root

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 마지막 노드번호, 간선의 개수

    # 1. 간선 리스트 정렬
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        heapq.heappush(edges, (w, n1, n2))
        # 가중치 기준으로 정렬

    # 2. make-set
    parents = [0] * (V + 1)
    for i in range(V + 1):
        parents[i] = i

    dist = 0    # 트리의 총 길이
    cnt = 0    # 지금까지 뽑은 간선 개수

    while True:
        w, n1, n2 = heapq.heappop(edges)

        if find(n1) != find(n2):
            union(n1, n2)
            dist += w
            cnt += 1
        if cnt == V:    #마지막 노드 달성 , 정점의 개수 V+1개라 간선은 V개
            break
    print(f'#{tc} {dist}')