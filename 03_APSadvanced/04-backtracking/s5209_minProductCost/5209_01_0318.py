import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def min_product(r, cost):    # r=제품, cost=비용(누적)
    # 첫번째 제품 선정
    '''제품, 공장 겹치면 안됨. 이때 최소비용'''
    global min_cost

    if cost > min_cost:    # 가지치기, 현재 가격이 최소가격보다 크면 종료
        return

    if r == N:  #마지막 제품까지 선정 완료
        min_cost = min(cost, min_cost)  # 최소 비용 갱신
        return
       
    for c in range(N):  # 제품의 공장별 비용 탐색
        if not visited[c]:  # 방문하지 않은 경우
            visited[c] = 1  # 방문처리 후
            min_product(r + 1, cost + factory_cost[r][c])   # 다음 제품 탐색, 비용: 기존가격+공장 가격
            visited[c] = 0      # 다시 초기화

for tc in range(1, T+1):
    N = int(input())
    # 제품 수 = 공장 수

    factory_cost = [list(map(int, input().split())) for _ in range(N)]
    # 공장별 생산비용
    # 제품 별 생산 공장 다르게 할 때 최소생산비용을 구하라

    min_cost = float('inf')
    visited = [0] * (N)   # 공장 방문여부 저장

    min_product(0, 0)

    print(f'#{tc} {min_cost}')