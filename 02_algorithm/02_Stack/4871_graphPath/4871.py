# 그래프 경로

#그래프
# - 정점(노드)와 간선으로 이루어진 자료구조
# - 정점 개수 :V, 간선 개수: E
# - 저장 방법: 인접행렬, 인접리스트, 간선리스트
# - 인접행렬: 2차원 행렬(출발:행, 도착:열로 저장)
##           두 정점 a, b가 a->b 방향으로 연결
##             adj[a][b] = 1
# 연결되어 있지 않다면 adj[a][b] = 0

# - 인접 리스트: V개의 리스트 사용
## adj[1]: 1번 정점과 연결되어 있는 정점 번호 저장
## adj[1] = [2,3,5] : 1->2, 1->3 1->5 연결

# - 간선 리스트: [(출발점, 도착점), (출발점, 도착점)]
## edge_list = [(1, 3), (1, 5), (1, 2)]

# 그래프 탐색에는 인접행렬 or 인접 리스트 사용
import sys
from pprint import pprint as pp
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    #1. 인접행렬
    # 2차원 행렬, V*V 1~V까지의 번호를 인덱스로 사용
    # 무향: 대칭, 유향:대칭아님
    # 노드 범위가 1부터면 0인덱스는 걍 안쓴다 생각
    adj_list = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj_list[v1][v2] = 1
        # 무향이면 반대도 추가
        # adj_list[v2][v1] = 1
    S, G = list(map(int, input().split()))

    print(V, E)
    pp(adj_list)