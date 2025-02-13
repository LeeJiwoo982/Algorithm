import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    tri = [[1]] #기본 초기값
    for i in range(1, N):   #첫 값은 이미 있어서 두번째 부터 값을 넣기
        row =[1]
        for j in range(1,i):    #중앙값 계산
            row.append(tri[i-1][j-1] + tri[i-1][j])
        row.append(1)
        tri.append(row)
    print(f'#{tc}')
    for row in tri:
        print(" ".join(map(str, row)))
