import sys
sys.stdin = open('input.txt', 'r')

def palindromeTest(s):
    N = len(s)
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    s = input()
    print(f'#{tc} {palindromeTest(s)}')