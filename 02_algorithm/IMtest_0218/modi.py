import sys
sys.stdin = open('imInput.txt', 'r')

T = int(input())  # 테스트 케이스 개수 입력
for tc in range(1, T + 1):
    N = int(input())  # 2차원 배열 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열 입력

    dr = [0, 1, 0, -1]  # 우, 하, 좌, 상 (오른쪽 → 아래 → 왼쪽 → 위 순서)
    dc = [1, 0, -1, 0]

    max_distance = 0  # 최장 이동 거리

    # 1. 출발점이 될 좌표 순회
    for r in range(N):
        for c in range(N):
            cnt = 1  # 이동 횟수 (출발점 포함)
            i, j = r, c  # 기준점 설정

            # 5. 주변 모든 값이 기준점보다 클 때까지 반복
            while True:
                min_val = 101  # 가능한 최소값 (0 < arr[i][j] < 100 이므로 101로 초기화)
                next_i, next_j = -1, -1  # 이동할 좌표 초기화

                # 2. 기준점 기준 상하좌우 네 방향 탐색
                for d in range(4):
                    nr, nc = i + dr[d], j + dc[d]

                    # 3. 기준점보다 작은 수 중에서 제일 작은 최솟값 찾기
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < arr[i][j]:
                        if arr[nr][nc] < min_val:
                            min_val = arr[nr][nc]
                            next_i, next_j = nr, nc  # 4. 최솟값이 나온 방향으로 이동 좌표 저장

                # 5. 주변 모든 값이 기준점보다 크면 종료
                if next_i == -1 and next_j == -1:
                    break

                # 4. 최솟값이 나온 방향의 좌표로 기준점 이동, 이동 시 cnt += 1
                i, j = next_i, next_j
                cnt += 1

            # 6. 최장 이동 거리 갱신
            max_distance = max(max_distance, cnt)

    # 7. 최장 이동 거리 출력
    print(f'#{tc} {max_distance}')
