import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            # arr 전체 순회
            # 스프레이 기준점은 스프레이 면적의 (0,0)
            # print(i, j)
            total = 0  # 파리의 합 개수
              # 최대 파리 개수
            for r in range(M):
                for c in range(M):
                    if (0<=i+r<N) and (0<=j+c<N):
                        total += arr[i+r][j+c]
                        if max_v < total:
                            max_v = total

                            # max_v = total
    print(f'#{tc} {max_v}')
