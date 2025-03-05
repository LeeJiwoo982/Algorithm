import sys
sys.stdin = open('sample_input.txt', 'r')

# 완전이진트리
# 리프 노드에 1000이하 자연수 저장
# 리프 제외 노드에는 자식노드에 저장된 값의 합
# N개의 노드, 루트 1번노드, \
def enq(n):
    '''완전이진트리에 값 생성
    부모값=왼자식+오른자식'''
    if tree[n]:
        return tree[n]
    if n*2<=N:  #왼쪽 자식이 있다면
        tree[n] += enq(n*2)
    if n*2+1 <=N:
        tree[n] += enq(n*2+1)
    return tree[n]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드개수N, 리프노드개수M, 값출력L

    tree = [0]*(N+1)
    # M개의 리프노드 번호와 자연수값
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    enq(1)
    print(f'#{tc} {tree[L]}')