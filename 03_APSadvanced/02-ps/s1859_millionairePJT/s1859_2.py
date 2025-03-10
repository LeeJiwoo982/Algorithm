import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    sell_price = prices[N-1]    #판매가격
    gain = 0    #총수익

    for i in range(N-2, -1, -1):
        if sell_price <prices[i]:   #판매가격보다 현재가격이 비싸면
            sell_price = prices[i]  #판매가격 갱신
        else:   #판매가격이 제일 비싸면
            gain += sell_price - prices[i]  #(판매가격=최대)에서 (해당 날짜의 가격=i일)을 뺀 
            # 차익을 수익에 넣음
    print(f'#{tc} {gain}')