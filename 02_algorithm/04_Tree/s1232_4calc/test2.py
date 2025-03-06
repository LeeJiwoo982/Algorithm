import sys
sys.stdin = open('input.txt', 'r')

def evaluate_tree(n):
    '''후위순회로 계산'''
    if left[n] == 0 and right[n] == 0:  # 리프노드인 경우
        return tree[n]

    left_v = evaluate_tree(left[n])  # 왼쪽 서브트리 값 계산
    right_v = evaluate_tree(right[n])  # 오른쪽 서브트리 값 계산

    # 후위부터 사칙연산 수행
    if tree[n] == '+':
        return left_v + right_v
    elif tree[n] == '-':
        return left_v - right_v
    elif tree[n] == '*':
        return left_v * right_v
    elif tree[n] == '/':
        return left_v / right_v


# 사칙연산 이진트리 구성
T = 10
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N + 1)  # 값을 저장할 리스트
    left = [0] * (N + 1)  # 왼쪽 자식 저장 리스트
    right = [0] * (N + 1)  # 오른쪽 자식 저장 리스트

    # 트리 구성
    for _ in range(N):
        data = input().split()
        node = int(data[0])
        value = data[1]  # 값 (연산자 또는 숫자)

        if len(data) == 2:  # 리프노드 (숫자)
            tree[node] = float(value)
        else:  # 연산자 노드
            tree[node] = value
            left[node] = int(data[2])
            right[node] = int(data[3])

    result = evaluate_tree(1)

    print(f'#{tc} {result}')
