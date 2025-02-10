# N*N크기의 농장 -언제나 홀수
# 수확은 정마름모
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total = 0
    # for i in range(N//2+1):
    #     if i == N//2: #중간 행일 때는 다 더하기
    #         for j in range(N):
    #             total += arr[i][j]
    #     elif i < N//2:  #
    #         for j in range(N//2-i, N//2+1+i):
    #             total += arr[i][j]
    #             if N - 1 - 2 * i >= 0:
    #                 total += arr[N-1-2*i][j]
    #     else:
    #         pass
    mid = N//2
    for i in range(N):
        if i <= mid:
            start = mid -i
            end = mid +i
        else:
            start = i -mid
            end = N-(i-mid)-1

        for j in range(start, end+1):
            total += arr[i][j]

    print(f'#{tc} {total}')
