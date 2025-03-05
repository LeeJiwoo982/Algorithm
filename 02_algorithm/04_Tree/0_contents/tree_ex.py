'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):   # 전위순회, 방문한 정점 먼저 처리
    global cnt
    if T:   # 0이 아니면, 존재하는 정점이면
        # 할 일
        print(T, end=' ')                # T에서 할 일
        cnt += 1
        pre_order(left[T])      # 왼쪽 자식(서브 트리) 이동
        pre_order(right[T])     # 오른쪽 자식(서브 트리) 이동

def in_order(T):    #중위순회
    if T:
        in_order(left[T])
        print(T, end=' ')
        in_order(right[T])

def post_order(T):    #후위순회
    if T:
        post_order(left[T])
        post_order(right[T])
        print(T, end=' ')


N = int(input())    #1번부터 N번까지 정점
E = N-1 #간선 수
arr = list(map(int, input().split()))

left = [0]*(N+1) #부모를 인덱스로 왼쪽 자식 저장. N번까지
right = [0]*(N+1)   #부모를 인덱스로 오른쪽 자식 저장
par = [0]*(N+1)     #자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
# for i in range(0, E*2, 2):
#     p, c = arr[i], arr[i+1]

    if left[p]==0:  #왼쪽 자식이 아직 없으면
        left[p]=c
    else:           #왼쪽 자식이 있는 경우
        right[p]=c

# print(left)
# print(right)

root =1
for i in range(1, N+1):
    if par[i]==0:
        root=i
        break

cnt = 0
print('전위순회 pre_order:', end=' ')
pre_order(3)    # 1번부터 전위순회 하기
                    # 1 2 4 7 12 3 5 8 9 6 10 11 13
                # 6번부터 순회
                    # 6 10 11 13
print()
print('전위순회 순회 횟수 확인 cnt:', end=' ')
print(cnt)  # 몇번 순회하는지 확인
print('중위순회 in_order:', end=' ')
in_order(1)
print()
print('후위순회 post_order:', end=' ')
post_order(1)
print()
print('root:', end=' ')
print(root)