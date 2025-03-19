import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def dfs(n, i, cnt): # 노드값, 노드인덱스, 연산횟수
    global cnt_mn   #최종반환 최소연산횟수

    i1 = i * 4 ** cnt + 1
    i2 = i * 4 ** cnt + 2
    i3 = i * 4 ** cnt + 3
    i4 = i * 4 ** cnt + 4

    # 종료조건
    if n == m:
        cnt_mn = min(cnt_mn, cnt)
        return cnt_mn

    # 가지치기
    if cnt > cnt_mn:
        return

        # 다음 단계
    if not visited[i1]:
        visited[i1] = 1
        dfs(n + 1, i1, cnt + 1)
        visited[i1] = 0

    if not visited[i2]:
        visited[i2] = 1
        dfs(n -1, i2, cnt + 1)
        visited[i2] = 0

    if not visited[i3]:
        visited[i3] = 1
        dfs(n * 2, i3, cnt + 1)
        visited[i3] = 0

    if not visited[i4]:
        visited[i4] = 1
        dfs(n - 10, i4, cnt + 1)
        visited[i4] = 0


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # n => m이 될때가지 최소 연산 횟수 구하기
    # dfs가 나을듯....흠 왠지는 몰라

    visited = [0] * 1_000_000
    cnt_mn = float('inf')

    visited[1] = 0

    dfs(n, 0, 0)    # 노드 값, 노드 인덱스(=visited 인덱스), cnt값

    print(f'#{tc} {cnt_mn}')
