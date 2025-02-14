import sys
from pprint import pprint as pp
sys.stdin = open('sample_input.txt', 'r')

def path(v,V):  # v는 시작, V는 최대
    '''인접경로가 있으면 이동, 없으면 순회'''
    visited = [0]*(V+1)
    stack = []
    while True:
        if visited[v] == 0:
            visited[v] = 1
        for w in adj[v]:
            if w == G:
                return 1
            else:
                if visited[w] == 0:
                    stack.append(v)
                    v = w
                    break
        else:   #방문한 노드이면서 인접노드도 없는 경우
            if stack:   # 스택에 기록이 있으면
                v = stack.pop() # 되돌아가기
            else:   # 스택이 비어있으면
                return 0    # G을 못찾았다는 뜻으로 보고

T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    #2. 인접 리스트
    # 1차원 리스트가 V개(고정) 있어야 함 => 2차원

    # 리스트의 리스트로 만들어서
    # adj[1] ~ adj[V] 까지 사용S
    adj = [[] for _ in range(V+1)]

    # 리스트의 딕셔너리로 만들어서
    # adj[1] ~ adj[V] 까지 사용
    # adj = {}
    # for i in range(1, V+1):
    #   adj[i] = []

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        # 무향그래픵면
        # adj[v2].append(v1)
    S, G = map(int, input().split())    #출발용 노드와 도착용 노드

    print(f'#{tc} {path(S, V)}')
