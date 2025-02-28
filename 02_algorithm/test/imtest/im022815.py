'''
4행 n열
각 셀은 1(on), 0(off) 상태
셀은 i+j+1이 시간 k의 배수일 때, 다른 상태로 스위치

예: 시간 k=2, 셀(2,3)이 0이면 => k=3일 때 2+3+1=6으로 1이 된다.

n과 k가 주어질 때 on상태의 셀 숫자 구하기
1<=n<=1000
1<=k<=1000
'''
import sys
sys.stdin = open('input_im022815.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    
    #초기 디스플레이 k=0일 때 모두 0ff상태
    display = [[0]*n for _ in range(10)]

    #시간 순회
    for t in range(1, k+1):
        #시간이 t일 때 display순회
        for i in range(4):
            for j in range(n):
                # 인덱스계산(i+j+1) 값이 t의 배수이면 바꾼다.
                if (i+j+1)%t == 0:
                    display[i][j] = (display[i][j]+1)%2

    #결과
    cnt = 0
    for i in range(4):
        for j in range(n):
            if display[i][j] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')
