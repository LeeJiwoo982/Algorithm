import sys
sys.stdin = open('sample_input.txt', 'r')

# 충전지교환방식전기버스
# 정류장 = 교환기
# 충전지 = 최대 운행가능한 정류장 수
# 정류장과 충전지 정보/ 목적지 도착에 필요한 최소한의 교환횟수
# 출발지 배터리 장착은 교환횟수에서 제외
# 1이 출발, 5 종점

#정류장 1 2 3 4 5
#충전지 2 3 1 1   에서 출발지의 충전지는 3번까지 가지만 2에서 교환하면 한 번의 교환으로 5까지 감

T = int(input())

def min_swaps_back(N, M):
    '''충전지 최소한으로 교환해서 목적지 도달하기 함수'''
    global min_swaps
    min_swaps = float('inf')
    backtrack(0, 0, M[0])   #현재위치, 교환횟수, 충전지위치로 충전이후 이동거리
    return min_swaps

def backtrack(now, swaps, charge):  #현재위치, 교환횟수, 충전지위치로 충전이후 이동거리
    global min_swaps
    # 목적지 도달 시 최소 교환 횟수 갱신
    if now >= N - 1:    #현재위치가 목적지 도착 이상일때(완료조건)
        min_swaps = min(min_swaps, swaps)
        return 
    
    # 현재 충전량으로 이동 가능한 범위 내의 모든 정류장 탐색
    for next_pos in range(now + 1, min(N, now + charge + 1)):   #목적지 vs 현재위치+충전거리
        backtrack(next_pos, swaps + 1, M[next_pos - 1]) #재귀

for tc in range(1, T+1):
    N, *M = map(int, input().split())

    result = min_swaps_back(N, M)
    print(f'#{tc} {result}')