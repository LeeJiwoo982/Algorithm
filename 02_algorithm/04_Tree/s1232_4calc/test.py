import sys
sys.stdin = open('input.txt', 'r')

def evaluate_tree(node):
    '''재귀적으로 트리를 탐색하여 연산 수행'''
    if isinstance(tree[node], float):  # 이미 숫자인 경우 반환
        return tree[node]

    left, right = children[node]  # 왼쪽, 오른쪽 자식 노드 가져오기
    left_val = evaluate_tree(left)  # 왼쪽 서브트리 값 계산
    right_val = evaluate_tree(right)  # 오른쪽 서브트리 값 계산

    # 연산 수행
    if tree[node] == '+':
        return left_val + right_val
    elif tree[node] == '-':
        return left_val - right_val
    elif tree[node] == '*':
        return left_val * right_val
    elif tree[node] == '/':
        return left_val / right_val

T = 10
for tc in range(1, T+1):
    # 입력 처리
    N = int(input())  # 노드 개수
    tree = {}  # 노드 값을 저장할 딕셔너리
    children = {}  # 자식 노드를 저장할 딕셔너리

    for _ in range(N):
        data = input().split()  #문자열로 받음
        node = int(data[0])  # 노드 번호    #숫자로 변환해서
        value = data[1]  # 값 (연산자 또는 숫자)

        if value.isdigit():  # 숫자인 경우 실수로 변환
            tree[node] = float(value)
            children[node] = ()  # 자식이 없음
        else:  # 연산자인 경우
            tree[node] = value
            children[node] = (int(data[2]), int(data[3]))  # 자식 노드 저장

    # 루트 노드는 항상 1번이므로 1번 노드부터 계산 시작
    print(f'#{tc}', int(evaluate_tree(1)))
