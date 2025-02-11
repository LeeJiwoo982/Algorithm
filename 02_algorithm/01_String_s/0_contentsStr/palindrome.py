# 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말=회문
# 8*8 글자판에서 제시된 길이를 가진 회문의 개수를 구하라
import sys
from pprint import pprint
sys.stdin = open('str_palindrome.txt', 'r')
N= int(input()) # N길이를 가진 회문의 개수를 구하라
pal = [list(input()) for _ in range(8)]
pprint(pal)
total =0
cnt = 0

for i in range(8):  #8
    for j in range(8-N+1):
        for k in range(N//2):
            if pal[i][j+k] != pal[i][j+N-1-k]:
                break   # 비교하는 위치의 값이 다르면 현재 구간 중지

        else:   # for문이 break에 걸리지 않고 종료하면, 회문이면
            total += 1

# 열 값도 비교

print(total)