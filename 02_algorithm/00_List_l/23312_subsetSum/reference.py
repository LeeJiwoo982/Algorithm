import sys
from pprint import pprint
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
# 비트로 만들기
# bit-masking을 사용하려면 index가 필요
A = list(range(1,13))
for tc in range(1,T+1):
    N, K = map(int, input().split())
    # N: 원소의 개수
    # M: 원소의 합
    cnt = 0 # 조건을 만족하는 집합의 수
    for i in range(1<<12):  # 비트가 왼쪽으로 12번 이동 2**12. 비트는 오른쪽에 나머지는 0
        # i는 0부터 2**11까지
        # 4095 = 1이 12개
        # 0이 12개에서 1이 12개[
        # i :0~4095
        # 각각의 비트를 숫자에 대응
        # 비트0: 포함x
        one_cnt = 0
        val_sum =0

        for i in range(0,12):
            if i & (1<<i):
                one_cnt +=1
                val_sum = A[i]
        pass