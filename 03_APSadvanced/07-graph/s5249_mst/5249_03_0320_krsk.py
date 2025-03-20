import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def find_set(a):
    if parents[a] == a:
        return a

    parents[a] = find_set(parents[a])

    return parents[a]

def union(a, b):
    aroot = find_set(a)
    broot = find_set(b)

    if aroot == broot:
        return  # 사이클 방지

    if aroot < broot:
        parents[broot] = aroot
    else:
        parents[aroot] = broot

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 간선 정보 입력
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))
    
    # 간선 정렬 : 오름차순
    edges.sort(key = lambda x: x[0])    # 정렬 기준 = 가중치

    # make set : 집합으로 만들기, 부모 = 대표 짝짓기
    parents = [0]*(V+1)
    for i in range(V+1):
        parents[i] = i

    # 가중치 오름차순부터 집합 만들기, N-1개 선택할때까지
    cnt = 0     # 선택한 간선 수 = N-1 까지
    weight = 0  #가중치 합
    for w, u, v in edges:
        if find_set(u) != find_set(v):
            # 서로소 집합일 때만 = 부모(대표)가 다를 때
            union(u, v)
        weight += w
        cnt += 1

        if cnt == V:
            break

    print(f'#{tc} {weight}')