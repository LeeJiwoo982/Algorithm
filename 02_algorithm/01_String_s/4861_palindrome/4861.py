import sys
from pprint import pprint
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]   #str 안풀고 나왔다
    # print(arr)
    for i in range(N):
        for j in range(N-M+1):
            for m in range(j, j+M//2):
                if arr[i][m] != arr[i][j+M-m-1]:
                    break
                else:
                    print(f'#{tc} {arr[i][m:m+M]}')

    C = [''.join(c) for c in zip(*arr)]
    for i in range(N):
        for j in range(N-M+1):
            for m in range(j, j+M//2):
                if C[i][m] != C[i][j+M-m-1]:
                    break
                else:
                    print(f'#{tc} {C[i][m:m+M]}')

    #     for j in range(N-M+1):  # 회문은 절반잘라서 반대편과 비교한다.
    #         for m in range(M//2):
    #             if arr[i][j] != arr[i][j+M-1-m]:
    #                 break
    #         else:
    #             print(arr[i][j])
    # for c in list(zip(*arr)):
    #     for r in range(N-M+1):
    #         for m in range(M//2):
    #             if arr[r][c] != arr[r+M-1-m][c]:
    #                 break
    #         else:
