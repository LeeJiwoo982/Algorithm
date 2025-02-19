from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    input()
    PW = list(map(int, input().split()))

    q = deque()
