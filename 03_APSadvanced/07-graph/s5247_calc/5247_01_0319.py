import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

T = int(input())    

def bfs(n):
    '''최소연산횟수로 M까지 도달하기'''
    # global cnt_mn
    q = deque([(n, 0)])
    visited = set()
    # cnt = 0

    while q:
        now, cnt = q.popleft()

        if now == M:
            # cnt_mn = min(cnt, cnt_mn)
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

        # if i == 0:
        #     next = now + 1
        #     if not visited[next]:
        #         q.append(next)
        #         cnt += 1

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 자연수 N을 **몇 번**의 연산을 통해 다른 자연수 M을 만들기
    # 사용할 수 있는 연산 +1, -1, *2, -10
    # 최소 몇 번의 연산을 거쳐야 할지
    # 연산의 중간 결과도 항상 백만 이하의 자연수
    
    # bfs
    # 4가지 브랜치
    # 도착지 M
    # 출발지 N
    # 최단경로
    # 1,000,000 * 8 byte
    # 8,000,000 byte
    # 8,000 kb
    # 8 mb
    # 262,144 kb
    
    # visited = [0] * 1_000_000   #언더바를 쉼표대신 쓸 수 있다.
    # cnt_mn = float('inf')   # 최소 연산 횟수여야 함/ bfs는 무조건 최소니까 없어도 될듯

    result = bfs(N)

    print(f'#{tc} {result}')