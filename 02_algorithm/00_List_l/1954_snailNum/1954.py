import sys
from pprint import pprint
sys.stdin = open('input.txt')
# 델타배열 우 > 하 > 좌 > 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 우0, 하1 좌2 상3
T =int(input())
for tc in range(1, T+1):
    N=int(input())
    # N*N배열 초기화
    arr = [[0]*N for _ in range(N)]
    #현재 좌표와 방향을 기억
    r, c, d = 0, 0, 0
    #시작점r c:(0,0) 방향d:우
    cnt = 1
    arr[r][c] = cnt # 첫 번째 숫자 채우기
    #두번째 갈 수 있으면 go
    #채워야 되는 숫자 N**2 = 반복횟수
    while cnt < N*N: # cnt 1부터 시작해서 N*N까지 반복
        # cnt += 1
        # 다음 이동 위치
        nr, nc = r + dr[d], c+ dc[d]

        #이동 가능한 경우: 그대로
        if 0 <= nr < N and 0 <= nc <N and arr[nr][nc] ==0:
            cnt +=1
            arr[nr][nc] = cnt
            r, c = nr, nc # 좌표이동
        #이동 불가능하면:방향을 틀어서
        else:
            d = (d+1) % 4   #방향전환
    #숫자를 str바꾸고 조인
    print(f'#{tc}')
    for row in arr:
        print(" ".join(map(str, row)))