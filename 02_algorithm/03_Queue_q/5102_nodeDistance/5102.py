import sys
sys.stdin = open('sample_input.txt', 'r')

def node_to_node(S, G, V):
    '''
    BFS를 이용하여 출발지S에서 도착지G로 가는 간선의 개수 반환
    만약 연결되어 있지 않다면 0반환
    '''
    visited = [0]*(V+1)    #visited생성
    q = []          #큐생성
    q.append(S)     #시작\점 인큐
    visited[S] = 1  #시작점 처리 표시

    while q:            #큐가 빌때까지
        t = q.pop(0)    #디큐
        # print(t, end = ' ')
        if t == G:  #t가 도착지면
            return visited[t]-1    #지나친

        for w in adj[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] =visited[t] + 1
    return 0
    pass
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    #V: 노드개수, E: 간선개수
    line = [list(map(int, input().split() )) for _ in range(E)]   #간선 정보: 노드, 노드    #양방향인가벼
    S, G = map(int, input().split())    #출발지와 도착지

    adj = [[] for _ in range(V+1)]
    print(f'#{tc}')
    print(f'노드개수:{V}, 간선개수: {E}\n출발지와 도착지: {S, G}')
    # print(f'간선정보: {line}')

    for i in range(E):
        adj[line[i][0]].append(line[i][1])
        adj[line[i][1]].append(line[i][0])
    print(adj)
    ans = node_to_node(S, G, V)

    print(f'#{tc} {ans}')