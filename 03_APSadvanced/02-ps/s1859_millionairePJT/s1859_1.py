import sys
sys.stdin = open('input.txt', 'r')


# 연속된 N일의 매매가를 전부 알고 있음
# 하루에 하나가 최대 구매수량
# 판매는 자유
# 경우1: 3 2 1 은 구매를 안하는 것이 이득
# 경우2: 1 2 3 은 1, 2일 구매 후 3일에 판매 이득
# 경우3: 1 1 3 1 2 은 1, 2일 구매 3일에 판매, 4일 구매 5일 판매
# 경우4  1 2 3 1 2 은 1, 2일 구매 3일 판매, 4일 구매 5일 판매
#
# 최대이익 구하기 증가하다가 감소하는 날 오기 직전에 팔기
# ========설계=========
# 10tc 30초/1tc 0.3초=> 1000만번의 연산 가능/
# - 자료구조
#     - 연속된 N일의 매매가 정보 >>prices 리스트로 저장
#     - gain: 팔고 산 돈
#     - items : 물품개수
# - 알고리즘
#     - 1일차부터 N일차까지
#     - 처음 시작 1일차에서 2일차의 가격을 보고 살지 말지 결정 >>O(N) N이 백만까지니까 넉넉
#         - 다음날 가격이 더 높으면 오늘 물건을 산다
#         - 다음날 가격이 낮으면 오늘 물건이 있으면 팔고, 없으면 사지 않는다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split())) +[0]
    gain = 0
    items = 0
    for i in range(N):
        if prices[i] <= prices[i+1]:
            gain -= prices[i]   #물건을 사서 -
            items += 1  #물건은 하루에 하나만 +
        else:
            if items:   #물건이 있다면 판다
                gain += prices[i]*items
                items = 0   #물건을 다 팔아서 0으로 초기화
    print(f'#{tc} {gain}')