import sys
from pprint import pprint
sys.stdin = open('sample_input.txt', 'r')

# N*N 격자에 빨강, 파랑 칠하기
# 영역이 겹쳐 보라색이 된 칸 수 구하기
T = int(input()) #Test_case 수
for tc in range(1, T+1):
    N = int(input()) # 영역 갯수
    ARRAY = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):  #1차원배열이 나오고
        arr = list(map(int, input().split()))
        r1, c1, r2, c2, color = arr # r1~c2는 ARRAY의 인덱스 값으로 사용
        # 0으로 채워진 ARRAY에 컬러색깔로 값을 채우고, 값이 3일 경우가 보라
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                ARRAY[i][j] += color

    for i in range(10):
        for j in range(10):
            if ARRAY[i][j] ==3:
                cnt += 1

    print(f'#{tc} {cnt}')