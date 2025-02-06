import sys
sys.stdin = open('sample_input.txt', 'r')

# 빌딩 좌우 밀집. 왼쪽 오른쪽 창문열면 옆건물 뷰
# 조망권: 양쪽 거리 2 이상 공간 확보
# 조망권 확보 세대 수 반환

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # 배열 순회, 인덱스로 뽑기, 좌:-1, -2 우;+1, +2
    for i in range(2, N-2):
        # i건물의 경우 : 주변 4건물 중 제일 높은 건물보다 큰 경우 조망권 확보
        neighbor = arr[i-2:i] + arr[i+1:i+3]
        nei_max = max(neighbor)

        if arr[i] > nei_max:
            cnt += arr[i]-nei_max # 모든 건물의 조망권 세대 수
    print(f'#{test_case} {cnt}')