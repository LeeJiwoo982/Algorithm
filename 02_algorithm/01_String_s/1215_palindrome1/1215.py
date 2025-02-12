import sys
sys.stdin = open('input.txt','r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]

    total = 0
    #행
    for r in range(8):
        for c in range(8-N+1):
            for p in range(N//2):
                if arr[r][c+p] != arr[r][c + N - p-1]:
                    break
            else:
                total += 1

    #열
    for c in range(8):
        for r in range(8-N+1):
            for p in range(N//2):
                if arr[r+p][c] != arr[r+N-p-1][c]:
                    break
            else:
                total += 1

    print(f'#{tc} {total}')