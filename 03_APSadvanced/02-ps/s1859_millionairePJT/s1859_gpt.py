import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    gain = 0  # 총 이익
    buy_price = 0  # 구매 비용
    items = 0  # 구매한 개수
    max_price = max(prices)  # 초기 최댓값 설정

    for i in range(N):
        if prices[i] == max_price:  # 현재 가격이 최댓값이면
            gain += items * prices[i] - buy_price  # 보유한 물건 모두 판매
            items = 0  # 물건 개수 초기화
            buy_price = 0  # 구매 비용 초기화
            if i < N - 1:  # 리스트 끝이 아니라면
                max_price = max(prices[i+1:])  # 남은 구간에서 새로운 최댓값 갱신
        else:  # 최댓값이 아니라면 구매
            buy_price += prices[i]  # 구매 비용 누적
            items += 1  # 구매 개수 증가

    print(f'#{tc} {gain}')

# 가격이 최대일 때, 그다음 최대일때, 그다음 최대일 때 판매해야 최대 이익
#뒤에서부터 비교하는 게 가장 편리
#