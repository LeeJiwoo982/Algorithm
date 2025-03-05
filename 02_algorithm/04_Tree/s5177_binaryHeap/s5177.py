import sys
sys.stdin = open('sample_input.txt', 'r')

# 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
# 최소힙

def enq(N):
    '''부모가 자식보다 작은값이 들어가는 완전이진트리'''
    global last
    last+=1
    tree[last] = N
    
    # 부모자식 인덱스 지정
    c = last
    p = c // 2
    while p and tree[p]>tree[c]:
        # 부모가 자식보다 클 때(최소힙조건 위배)
        tree[p], tree[c] = tree[c], tree[p]
        
        # 루트까지 부모가 자식보다 작아야 한다
        c = p
        p = c //2

def post_order(n):
    '''완전이진트리를 순회하여 부모의 값 구하기'''
    global s
    if 1<= n <=N:
        # print(n, end=' ')
        s += tree[n]    #부모인덱스의 값 더하기
        post_order(n//2)    #마지막 노드의 부모
        return s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 주어진 배열을 최소힙 트리 구조로 만들기
    tree = [0]*(N+1)
    last = 0
    for n in arr:
        enq(n)

    # 완성된 트리에서 마지막 노드의 조상노드 탐색
    s = 0
    # print(tree)
    print(f'#{tc} {post_order(N // 2)}')
