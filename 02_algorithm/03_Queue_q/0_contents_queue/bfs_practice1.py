# 연결된 두개의 정점 사이의 간선을 순서대로 나열
# 모든 정점을 너비우선탐색하여 경로를 출력
# 시작정점은 1
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
'''
출력 결과
1-2-3-4-5-7-6
'''
# arr = list(map(int, input().split()))
# N = len(arr)
# adj = [[] for _ in range(8)]    #그래프 경로 저장, 행은 출발노드, 열은 도착노드
# # adj = [[], [2, 3], [4, 5], [7], [6], [6], [7], []]
# for i in range(0, N, 2):
#     adj[arr[i]].append(arr[i+1])
#
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
#선생님 코드
def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    ''''''
    visited = [0] * (V+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:        # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # 디큐
        print(t, end = ' ')        # 방문한 정점에서 할일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w]==0:
                q.append(w)     # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1
    print(visited)

V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접리스트 -------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우

#다른경우 range(0, E*2, 2)
#v1, v2 = arr[i], arr[i+1]
# 여기까지 인접리스트 -----------------


d= bfs(5, 7)
# start = 1
# 경로 1 2 3 4 5 7 6
# visited = [0, 1, 2, 2, 3, 3, 4, 3]

#start= 5
# 경로 5 2 6 4 1 7 3
# visited = [0, 3, 2, 4, 3, 1, 2, 3]