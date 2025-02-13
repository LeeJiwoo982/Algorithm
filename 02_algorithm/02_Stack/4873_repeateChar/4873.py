import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    S = input()
    k = len(S)
    arr = [0]*(k+1)
    top = 0
    arr[top]=0
    for s in S:
        top+=1
        arr[top]=s
        if arr[top]==arr[top-1]:
            top-=2
    result = arr[1:top+1]
    print(f'#{tc} {len(result)}')