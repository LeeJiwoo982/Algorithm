# s5176
# 1-N 자연수 이진탐색 트리에 저장
# 왼쪽, 현재, 오른쪽
# 완전이진트리




T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1)
    last = 0

    # print(f'#{tc} {N//2+1} {}')
    # root 값, N//2 노드 값
