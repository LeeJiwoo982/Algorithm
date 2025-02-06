import sys
# 100*100 2차원 배열, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값
sys.stdin = open("input.txt")
T = 10

for test_case in range(T):
    N = int(input())

    # 2차원 배열을 담은 리스트
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최댓값 구하기
    max_v =  -2** 31

    # 행의 합을 구하고 그 중에서 최댓값
    for line in range(100):
        max_v = max(max_v, sum(arr[line]))

    # 열의 합을 구하고 그 중에서 최솟값
    for row in range(100):
        col_sum = sum(arr[line][row] for line in range(100))
        max_v = max(max_v, col_sum)

    # 대각선의 합-1
    diag1_sum = sum(arr[i][i] for i in range(100))
    max_v = max(max_v, diag1_sum)

    # 대각선의 합-2
    diag2_sum = sum(arr[i][99-i] for i in range(100))
    max_v = max(max_v, diag2_sum)

    print(f'#{test_case} {max_v}')