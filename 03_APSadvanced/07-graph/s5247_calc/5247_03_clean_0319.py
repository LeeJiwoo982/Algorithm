from collections import deque
T = int(input())


def bfs(n):
    '''최소연산횟수로 M까지 도달하기'''
    # global cnt_mn
    q = deque([(n, 0)])
    visited = set()

    while q:
        now, cnt = q.popleft()

        if now == M:
            return cnt

        if now in visited:
            continue
        visited.add(now)

        if now + 1 <= 1_000_000:
            q.append((now + 1, cnt + 1))
        if now - 1 > 0:
            q.append((now - 1, cnt + 1))
        if now * 2 <= 1_000_000:
            q.append((now * 2, cnt + 1))
        if now - 10 > 0:
            q.append((now - 10, cnt + 1))

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = bfs(N)

    print(f'#{tc} {result}')