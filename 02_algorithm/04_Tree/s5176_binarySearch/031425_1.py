# 1-N 까지 자연수 이진탐색트리 저장 => 이진트리
# 중위순회
# 완전이진트리임
import sys
sys.stdin = open('sample_input.txt', 'r')
def inorder(T):
    global cnt
    '''왼쪽, 오른쪽 자식의 값을 미리 할당하고
    그 값이 존재 할 수 있는 값이면 순회해서 값을 넣는 함수'''
    left = T * 2
    right = T * 2 + 1

    if left <= N:   # 완전이진트리의 범위 안에 있는 경우에
        inorder(left)

    cnt += 1
    tree[T] = cnt

    if right <= N:
        inorder(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())       # 1000까지

    # 완전이진트리가 조건이라 N+1까지인 트리리스트를 만든다.
    tree = [0] * (N + 1)
    # 0으로 초기화된 트리에 중위순회하며 채워넣기 위한 변수, 0부터시작해서 작업할때 +1하기
    cnt = 0 # 번호 넣기

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')