import sys
sys.stdin = open('sample.txt', 'r')

T = int(input())

def succeed_task(r, p):
    '''높은 확률'''
    global total_mxp

    # 가지치기
    if p <= total_mxp:
        return

    # 종료 조건
    if r == N:  #마지막 사람까지 다 정했을 때
        total_mxp = max(p, total_mxp)
        return

    # 업무 탐색
    for c in range(N):
        if not visited[c]:
            visited[c] = 1
            succeed_task(r + 1, p * P[r][c] / 100)

            visited[c] = 0


for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    # r번 사람이 c번 일을 성공할 확률을 퍼센트 단위로 나타냄
    # 모든 일 성공 확률 최대일 때 소수점 아래 7번째 자리에서 반올림해서 6번째까지 출력

    total_mxp = 0
    visited = [0] * N

    succeed_task(0, 1)  # 0번째 직원과 업무 확률

    total_mxp = total_mxp * 100
    result = round(total_mxp, 6)

    print(f'#{tc} {result:.6f}')