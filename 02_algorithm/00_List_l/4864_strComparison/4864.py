import sys
sys.stdin = open('sample_input.txt', 'r')

def comparingStr(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{tc} {comparingStr(str1, str2)}')