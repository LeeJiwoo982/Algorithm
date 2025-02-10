import sys
from pprint import pprint
sys.stdin = open('input.txt','r')


T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j]==2:
                start, end = i, j   #도착지 인덱스[99][final]
    r, c = start, end
    while r>0:
        if c-1>=0 and arr[r][c-1]==1:
            while c-1>=0 and arr[r][j-1]==1:
                c-=1
        elif j+1<100 and arr[r][c+1]==1:
            while j+1<100 and arr[r][c+1]==1:
                c+=1

        r-=1

    print(f'#{tc} {c}')