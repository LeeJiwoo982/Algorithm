import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pz = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    # 행 확인
    for r in range(N):
        cnt = 0
        for c in range(N):
            if pz[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt ==K:
            total += 1

    #열 확인
    for c in range(N):
        cnt = 0
        for r in range(N):
            if pz[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total += 1
                cnt = 0
        if cnt ==K:
            total += 1
    print(f'#{tc} {total}')