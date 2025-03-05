import sys
sys.stdin = open('input.txt', 'r')

def post_order(n):
    '''후위순회로 계산'''
    if n*2<=N:
        post_order(n*2)

# 사칙연산 이진트리구성으로
T = 10
for tc in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1)

    for i in range(N):
        x = list(input().split())
        if len(x) == 4:
            a, b, c, d = x
            tree[int(a)] = b
        else:
            a, b = x
            tree[int(a)] = b
