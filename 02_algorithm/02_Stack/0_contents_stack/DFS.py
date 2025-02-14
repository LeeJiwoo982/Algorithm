visited = stack = []
# def DFS(v):
#     #시작점 v방문
#     visited[v] = True
    # while True:
    #     pass
        #if (v 인접 정점 중 방문 안한 정점 w가 있을 때):
            #push(v)    # stack에 v를 push
            # stack.append(v)
            
            #v = w; # w에 방문 # 다음 정점 확인
            #visited[w] = True

        #else:  #(v 인접 정점 중 방문 한 정점만 있다면)
            #if (스택이 비어있지 않으면):
                #v = stack.pop();
            #else:  #(스택이 비어있으면)
                #break
    #return DFS()

# arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# visited = [False]*len(arr)
# stack = [0]*len(arr)
#
# # 정점 A 시작으로 우선 탐색
# visited[0] = True
#
# i = 0
# stack[i] = 'A'
# visited[1] = True
#
# i=1
# stack[i] = 'B'
# visited[3] = True
#
# i =2
# stack[2] = 'D'
# visited[5] = True
#
# i =3
# stack[3] = 'F'
# visited[4] = True
#
# i =4
# stack[4] = 'E'
# visited[2] = True
#
# where = stack.pop() #E  visited가 E에서 다른 경로 탐색> 없음> >i=3 stack[3] = 'F'
# # 다시 pop
# where = stack.pop() #F visited F에서 다른 경로 탐색>G 있음>   현재 i=2, stack[2] = 'D'
# stack[3] = 'F'
# visited[6] = True
# where = stack.pop() #F
# #... 팝해서 경로 탐색 없으면 다시 팝
# #결론: ABDFECG

def dfs(v, N):  #v: 탐색시작 위치, N:정점개수
    visited = [0]*(N+1) #visited, stack이 출력에 필요하면 밖에서 만들고 리턴하면됨.
    # 탐색에만 사용하면 함수에서 만들고 사용해도 됨
    stack = []

    while True:
        if visited[v] == 0: # 되돌아온건지 탐색하는 건지 구분 용
            visited[v] = 1
            print(v)
        # v에 인접하고 방문 안한 w가 있으면
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        #다 인접한 것이면
        else:
            if stack:
                v = stack.pop()
                # 뒷걸음친거면 첫 if지나치고 for문 들어가서 탐색
            else:
                break
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'''
V, E = map(int, input().split())
graph = list(map(int, input().split()))

adj_list = [[] for _ in range(V+1)] #인접 쌍들 저장하는 빈 리스트

for i in range(E):
    v, w = graph[i*2], graph[i*2 + 1]
    #방향이 없는 경우
    adj_list[v].append(w)   # 1행에 2 추가, 인접했다는 의미
    adj_list[w].append(v)   # 2행에 1 이 인접

print(dfs(1,V))