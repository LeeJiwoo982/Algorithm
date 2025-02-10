import sys
sys.stdin = open("input.txt", "r")

def rotate_90(N, arr):
    '''주어진 N*N 행렬(arr)을 90도 회전한 모양 출력'''
    rot_90 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot_90[j][N-1-i] = arr[i][j]

    return rot_90

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotate_90(N, arr)
    rot_180 = rotate_90(N, rot_90)
    rot_270 = rotate_90(N, rot_180)

    print(f'#{tc}')
    for s in range(N):
        print(''.join(map(str, rot_90[s])), ''.join(map(str, rot_180[s])), ''.join(map(str, rot_270[s])))

