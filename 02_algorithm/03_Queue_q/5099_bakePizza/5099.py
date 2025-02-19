import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    while True:
        pass
        # while 한바닥은 치즈 녹는 원래 N[0]자리에 있던 수가 다시 N[0]으로 올 떄
        # 1바퀴 돌면 치즈양//2