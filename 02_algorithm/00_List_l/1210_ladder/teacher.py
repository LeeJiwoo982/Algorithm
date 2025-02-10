import sys
from pprint import pprint
sys.stdin = open('input.txt','r')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    #2의좌표
    endR, endC = -1, -1
    for r in range(100):
        for c in range(100):
            if arr[r][c] ==2:
                endR, endC =r, c

    r, c = endR, endC
    # r=99 c=?
    while r>0:
        #r=0일 때 종료
        #좌우 검사
        #좌 c-1
        #우 c+1
        #2차원 배열의 경계조건 0<= r, c<100
        if c-1>=0 and arr[r][c-1] ==1:
            #왼쪽으로 이동
            while c-1>=0 and arr[r][c-1]==1:
                c-=1
        elif c+1<100 and arr[r][c+1]==1:
            while c+1<100 and arr[r][c+1]==1:
                c+=1
        r -=1
    print(f'#{tc} {c}')