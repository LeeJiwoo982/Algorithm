import sys
sys.stdin = open('sample_input.txt', 'r')

def tourn():
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))

