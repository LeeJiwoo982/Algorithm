import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

def in_order(n):
    '''중위순회'''
    global result
    if 2*n<=N:
        in_order(2*n)

    result.append(tree[n])

    if 2*n+1<=N:
        in_order(2*n+1)

T = 10
for tc in range(1, T+1):
    N = int(input())    #트리가 갖는 정점의 총 수=노드개수
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    #정점정보 입력
    for i in range(N):  # N개의 정보
        x = list(input().split())
        # print(x)
        if len(x) == 4:
            a, b, c, d = x  #a=노드, b=값, c=왼, d=오
            tree[int(a)] = b
            left[int(a)] = c
            right[int(a)] = b

        elif len(x) == 3:
            a, b, c = x
            tree[int(a)] = b
            left[int(a)] = c

        else:
            a, b = x
            tree[int(a)] = b

    result = []
    in_order(1)
    print(f'#{tc} {"".join(map(str, result))}')