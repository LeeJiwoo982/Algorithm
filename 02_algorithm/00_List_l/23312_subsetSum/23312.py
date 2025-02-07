import sys
from pprint import pprint
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
# A ={1,2,3,4,5,6,7,8,9,10,11,12}
# A의 부분집합 중 N개의 원소, 원소의 합이 K인 부분집합의 개수
# 해당하는 부분집합이 없으면 0
for tc in range(1,T+1):
    A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    N, K = map(int, input().split())
    bit = [0]
    for i in range(2):
        bit[0] = i

    # print(f'#{tc} {result}')