import sys
sys.stdin = open('sample_input.txt', 'r')

# 최종 충전 횟수 or 0(목적지 도달 못할 때)
# K: 충전 후 최대 이동 정류장 수, N+1: 정류장 개수, M: 충전기 설치된 정류장 번호
# 종점에 도달할 때 충전 횟수 or 종점 도착 못하면 0
T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    charge = 0
    for i in range(1, M):
        if bus_stop[i]-bus_stop[i-1] < K:
            charge = 0
            break
        else:
            charge += 1

    print(f'#{test_case} {charge}')
