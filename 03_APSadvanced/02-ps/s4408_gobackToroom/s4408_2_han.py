import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    rooms = [0]*401

    for _ in range(N):
        A, B = map(int, input().split())

        if A > B:
            A, B = B, A

        start = (A + 1) // 2
        end = (B + 1) // 2

        for i in range(start, end + 1):
            rooms[i] += 1
    result = max(rooms)     # 겹치는 부분이 제일 클 때 == 시간이 되는 경우
    print(f'#{tc} {result}')