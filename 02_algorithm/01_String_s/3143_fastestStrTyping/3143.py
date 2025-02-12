import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N, M = len(A), len(B)
    cnt = 0
    i = j = 0
    while i < N:
        if A[i] != B[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        if j == M :
            cnt += 1
            i = i - M + 1
            j = 0

    result = N - (cnt * M) + cnt
    print(f'#{tc} {result}')
