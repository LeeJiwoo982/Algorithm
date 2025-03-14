# 루트가 없는 트리
# 트리의 루트 = 1
# 각 노드의 부모를 구하는 프로그램
# 노드의 개수 N, 담줄부터 N-1개의 줄에 트리 간선 정보
# https://www.acmicpc.net/problem/11725

# 저장방식
# 이진트리 아님, 그냥 1:N 트리임
# 라이트레프트 안됨. 그냥 저장해야 할듯 append로

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
sys.stdin = open('input.txt', 'r')

def dfs(node):
    for nx_node in graph[node]:
        if parent[nx_node] == 0:    # 방문하지 않은 노드이면
            parent[nx_node] = node  # 부모 설정
            dfs(nx_node)    #재귀호출

# 런타임 남...
def bfs(node):
    q = deque()
    q.append(node)

    while q:
        t = q.popleft()
        for nx in graph[t]:
            if parent[nx] == 0:
                parent[nx] = t
                q.append(nx)

T = int(input()) 
for tc in range(1, T+1):
    N = int(input())

    graph = [[] for _ in range(N + 1)]  # 트리 그래프=인접리스트
    parent = [0] * (N + 1)  # 노드의 부모를 저장하는 리스트
    parent[1] = -1  #1번노드 루트로 부모없음

    for i in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)

    bfs(1)
    # print(parent)
    #출력
    for i in range(2, N+1):
        print(parent[i])