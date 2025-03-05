# s5176
# 1-N 자연수 이진탐색 트리에 저장
# 왼쪽, 현재, 오른쪽
# 완전이진트리

#중위순회로 넣기
def in_order(n):
    '''자연수를 중위순회 순서로 넣는다.'''
    global cnt, N
    left = 2*n  #배열 인덱스 안에 있다면
    right = 2*n+1

    if left <= N:
        in_order(left)

    tree[n] = cnt
    cnt += 1

    if right<=N:
        in_order(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1)
    cnt = 1
    in_order(1)
    # print(tree)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
    # root 값, N//2 노드 값
