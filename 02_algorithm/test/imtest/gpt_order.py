import sys
sys.stdin = open('imInput.txt', 'r')

# 입력 받기
T = int(input().strip())  # 테스트 케이스 수
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_steps = 0  # 최대 이동거리 (출발지도 포함)

    # 2차원 배열의 모든 좌표를 출발점으로 시뮬레이션
    for i in range(N):
        for j in range(N):
            # 현재 좌표를 출발점으로 설정하고 이동 거리를 1 (출발지 포함)로 초기화
            steps = 1
            cur_i, cur_j = i, j

            # 공이 이동할 수 없을 때까지 반복
            while True:
                current_val = arr[cur_i][cur_j]
                possible_moves = []  # 이동 가능한 좌표들을 저장할 리스트

                # 상, 하, 좌, 우 네 방향 탐색
                # 위쪽 좌표: (cur_i-1, cur_j)
                if cur_i - 1 >= 0:
                    if arr[cur_i-1][cur_j] < current_val:
                        possible_moves.append((arr[cur_i-1][cur_j], cur_i-1, cur_j))
                # 아래쪽 좌표: (cur_i+1, cur_j)
                if cur_i + 1 < N:
                    if arr[cur_i+1][cur_j] < current_val:
                        possible_moves.append((arr[cur_i+1][cur_j], cur_i+1, cur_j))
                # 왼쪽 좌표: (cur_i, cur_j-1)
                if cur_j - 1 >= 0:
                    if arr[cur_i][cur_j-1] < current_val:
                        possible_moves.append((arr[cur_i][cur_j-1], cur_i, cur_j-1))
                # 오른쪽 좌표: (cur_i, cur_j+1)
                if cur_j + 1 < N:
                    if arr[cur_i][cur_j+1] < current_val:
                        possible_moves.append((arr[cur_i][cur_j+1], cur_i, cur_j+1))

                # 이동 가능한 좌표가 없으면 반복 종료
                if not possible_moves:
                    break

                # 조건: 자신보다 작은 값 중에서 제일 작은 최솟값으로만 이동한다.
                # possible_moves 리스트에 저장된 첫 번째 값은 (이동할 값, x좌표, y좌표)
                # min()를 사용하여 이동할 좌표 중 값이 가장 작은 좌표를 선택
                next_move = min(possible_moves)
                # 선택된 좌표로 이동 (x좌표, y좌표 업데이트)
                cur_i, cur_j = next_move[1], next_move[2]
                # 이동할 때마다 이동거리 증가
                steps += 1

            # 출발점 별 이동 거리 중 최댓값 갱신
            if steps > max_steps:
                max_steps = steps

    # 결과 출력 (예시 출력 형식에 맞게 ">> #테스트케이스번호 결과")
    print("#{} {}".format(t, max_steps))
