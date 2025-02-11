import sys
sys.stdin = open('input.txt','r')

def is_sdk(arr):
    # row check
    for row in range(9):
        sdk = 0
        for c in range(9):
            sdk += arr[row][c]
        if sdk != 45:
            return 0
    #column check
    for column in range(9):
        sdk = 0
        for r in range(9):
            sdk += arr[r][column]
        if sdk != 45:
            return 0
    # box check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sdk = 0
            for r in range(3):
                for c in range(3):
                    sdk += arr[i+r][j+c]
            if sdk != 45:
                return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    is_sudoku = is_sdk(arr)
    print(f'#{tc} {is_sudoku}')