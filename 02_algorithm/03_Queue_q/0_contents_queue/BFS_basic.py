# def BFS(G, v):
#     '''그래프G, 탐색 시작점 v   '''
#     visited = [0]*(n+1)     #n: 정점의 개수
#     queue = []  #큐생성
#     queue.append(v) # 시작점 삽입
#
#     while queue:    #큐가 비어있지 않을 때만 반복
#         t = queue.pop(0)    #큐의 첫번째 원소 반환
#         if not visited[t]:  # 첫번째 원소가 방문 안한 곳이라면
#             visited[t]=True #방문 표시
#             visited(t)  #t에서 할 일 처리
#             for i in G[t]:  #t와 연결된 정점 모두
#                 if not visited[i]:  #방문되지 않았으면
#                     queue.append(i) #큐에 넣기

#큐는 임시저장 장소. 이후에 갈 곳을 기억해서 while로 모두 갈 수 있도록
# 순서: if 처리확인>> 처리가능> 처리표시visited> 연결정점 탐색> if 처리확인>처리 가능이면 인큐
# 간단한 BFS구현, 더 제대로된 건 이후에 할 예정

#
def BFS(G, v, n):
    visited = [0]*(n+1)     #정점개수보다 +1
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        visit(t)    #원소로 할 일 처리
        for i in G[t]:  #t와 연결된 정점 탐색
            if not visited[i]:  #인큐안됐다면
                queue.append(i) #인큐
                visited[i] = visited[t] + 1 #인큐됐음 표시,, 순서를 표시하게 됨
