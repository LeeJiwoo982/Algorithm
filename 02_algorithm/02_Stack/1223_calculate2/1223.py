import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 요소가 숫자면 int(), 아니면 그냥 넣기
    case =[int(x) if x.isdecimal() else x for x in list(input())]
