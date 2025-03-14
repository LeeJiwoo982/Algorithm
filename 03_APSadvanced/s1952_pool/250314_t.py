import sys
sys.stdin = open("sample_input.txt", 'r')

# 1일권 보기, 한달권 보기 등등 완전탐색
# 제일 저렴한 조합
# 12달에 가장 저렴한 경우
# 각 달마다 최소 비용을 구하는 식
# 1월 1일 vs 1달
# 2월 1월최소가격+(2월 최소비용 1일 vs1달)
# 3월 3달 이용권vs 2월까지 최소가격(1일vs1달) 등등

    # DP = 재활용
    # 작은 문제로 나눔
    # 기존 최솟값 재활용
    # 이후 계산은 이전 값들을 변경시키지 않음

    # 완전탐색
    #
T = int(input())
for tc in range(1, T+1):
    cost_day, cost_month, cost_3month, cost_year = map(int, input().split())
    days = [0] + list(map(int, input().split()))
    mn_ans = 20349234
