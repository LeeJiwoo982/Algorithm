import sys
# input = sys.stdin.readline()

def pooling(matrix):
    '''분할 정복 : 재귀, 2*2 묶음에서 2번째 큰 값 선택'''
    n = len(matrix)

    if n == 2:
        flat = sum(matrix, [])
        flat.sort(reverse=True)
        return flat[1]

    new_matrix = []
    for r in range(0, n, 2):
        row = []
        for c in range(0, n, 2):
            block = [
                matrix[r][c], matrix[r][c + 1],
                matrix[r + 1][c], matrix[r + 1][c + 1]
            ]
            block.sort(reverse=True)
            row.append(block[1])

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
