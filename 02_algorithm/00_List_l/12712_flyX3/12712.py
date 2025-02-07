import sys
sys.stdin = open('in1.txt', 'r')
# N: 영역
# M: 세기. M칸의 파리 잡기
def check1(x, y, dx, dy):
    global mx
    total = arr[y][x]
    for i in range(4):  # 4방향 탐색
        for j in range(1, M):
            nx = x + dx[i] * j  # 1 -> 2 -> 3 .. 4방향을 한칸씩 늘리면서 범위지정
            ny = y + dy[i] * j
            # 경계선을 넘어서는 값들은 고려 x
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            else:
                total += arr[ny][nx]
    if total > mx:  # 최댓값보다 지점에서 잡을 수 있는 최대값이 더 크다면 최댓값 갱신
        mx = total
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]  # +방향 x좌표
    dy = [0, 0, -1, 1]  # +방향 y좌표
    di = [-1, 1, -1, 1]  # x방향 x좌표
    dj = [-1, 1, 1, -1]  # x방향 y좌표
    mx = 0  # 최댓값 임의 지정 (작은 값으로)
    for i in range(N):
        for j in range(N):
            check1(i, j, dx, dy)  # 좌표 하나하나 살피기
            check1(i, j, di, dj)
    print(f'#{tc} {mx}')

    #도저히 풀수 없어서 배껴서 이해하려는 중