import sys
sys.stdin = open('re_sample_input.txt', 'r')

import heapq

T = int(input())

def find(a):
    '''a의 대표 찾기, 루트 노드 찾기, 조상부모찾기'''
    if parents[a] == a:
        return a

    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    '''a와 b를 하나의 집합으로 만드는 함수'''
    aroot = find(a)
    broot = find(b)

    if aroot == broot:  # 같은집합이면 반환
        return

    if aroot < broot:
        parents[broot] = aroot
    else:
        parents[aroot] = broot

for tc in range(1, T+1):
    N = int(input())    # 섬의 개수
    
    # 섬의 좌표: 섬은 0~N-1까지
    X = list(map(int, input().split()))     # 각 섬의 X좌표 모음
    Y = list(map(int, input().split()))     # Y좌표 모음

    # 환경 부담 세율 : 실수
    E = float(input())
    
    # 1. 간선 리스트 만들기
    # 가중치 = 세금 한번에 계산하고 넣을까나...
    # 섬의 모든 간선을 계산해서 넣기
    # 간선의 개수가 최대로 구할 수밖에 없남? 그러면.. krsk크루스칼
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = X[i], Y[i]
            x2, y2 = X[j], Y[j]
            L = (x1-x2)**2 + (y1-y2)**2
            w = E * L
            heapq.heappush(edges, (w, i, j))
    
    # 2. make-set
    parents = [0] * N
    for i in range(N):
        parents[i] = i


    # 3. 최소비용신장트리계산
    # find, union
    cnt = 0         # 종료조건용
    weight_mn = 0       # 최소비용
    while True:
        w, n1, n2 = heapq.heappop(edges)
        if find(n1) != find(n2):
            union(n1, n2)
            cnt += 1
            weight_mn += w

            if cnt == N-1:
                break

    print(f'#{tc} {round(weight_mn)}')