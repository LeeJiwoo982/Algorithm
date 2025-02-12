import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    N, M = len(A), len(B)

    cnt = 0  # B를 찾은 횟수
    i = 0  # A를 탐색할 인덱스

    while i <= N - M:
        if A[i:i + M] == B:  # 현재 위치부터 B의 길이만큼 확인
            cnt += 1
            i += M  # B를 찾으면 B의 길이만큼 점프
        else:
            i += 1  # 없으면 그냥 한 칸 이동

    result = N - (cnt * M) + cnt
    print(f'#{tc} {result}')

## 만약 패턴이 중첩