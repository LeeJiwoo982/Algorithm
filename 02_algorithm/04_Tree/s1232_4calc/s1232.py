import sys
sys.stdin = open('input.txt', 'r')

def evaluate_tree(n):
    '''후위순회로 계산'''
    # 리프노드(숫자)인 경우는 바로 반환
    if not left[n]:
        return tree[n]

    left_v = evaluate_tree(left[n])
    right_v = evaluate_tree(right[n])

    #후위부터 사칙연산 수행
    # return을 하셔야 한다... 씁
    if tree[n] == '+':
        return left_v + right_v
    elif tree[n] == '-':
        return left_v - right_v
    elif tree[n] == '*':
        return left_v * right_v
    elif tree[n] == '/':
        return left_v / right_v


# 사칙연산 이진트리구성으로
T = 10
for tc in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1) # 값을 저장할 리스트
    left = [0]*(N+1)
    right = [0]*(N+1)
    # child = [[0] for _ in range(N+1)]   #부모를 인덱스로 하는 자식위치
    #그리고 자식은 또다시 부모가 되기도 함. 없으면 리프노드

    # child에 왼, 오 자식 넣기, 없으면 빈리스트
    for _ in range(N):
        data = input().split()
        node = int(data[0])
        value = data[1] #값으로 연산자나 숫자가 들어가 있음

        if len(data) == 2:  #리프노드의 경우
            tree[node] = float(value)
        else: #연산자 겸 누군가의 부모
            tree[node] = value
            left[node] = int(data[2])
            right[node] =int(data[3])
            # child[node] = [int(data[2]), int(data[3])]
            
    result = evaluate_tree(1)

    print(f'#{tc}', int(result))
