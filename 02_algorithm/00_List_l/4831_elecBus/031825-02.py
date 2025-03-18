import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def cnt_charge(K, N, M, charge_sp):
    now = 0  # 현재 위치     now == N 일 때 목적지
    cnt_charge = 0  # 충전 횟수  

    while now < N:  # 목적지 도달 전까지만 계산
        candidates = [c for c in charge_sp if now < c <= now + K]
        # 충전기 중 현재위치+이동거리보다 작으면서 & 현재보다는 큰
        if now + K >= N:  # 현재+이동거리가 목적지 이상이면 충전 필요 X
            return cnt_charge   #현재까지 충전횟수 반환 후 종료

        if len(candidates) == 0:    # 더이상 충전소가 없음
            return 0    #목적지 도달 실패

        else:
            now = max(candidates)   #후보지 중 제일 숫자 높은 것으로 업데이트
            cnt_charge += 1

        
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_sp = list(map(int, input().split()))

    cnt = cnt_charge(K, N, M, charge_sp)

    print(f'#{tc} {cnt}')