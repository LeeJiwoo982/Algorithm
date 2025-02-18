import sys
sys.stdin = open('sample_input.txt', 'r')

def f(i, N, s):
    '''크기 N, 순열 저장 p배열에서 p[i]를 결정하는 함수'''
    global min_v
    global cnt
    cnt += 1

    if i == N:  #
        if min_v>s:
            min_v = s
    elif min_v<s:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, s + arr[i][p[i]])
            p[i], p[j]  = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]   #0에서 N-1까지 요소로 가짐
    min_v = 10000   # 최소값?
    cnt = 0 #빈도
    f(0, N, 0)  #i=0, N=N, s=0
    print(f'#{tc} {min_v}') # cnt = 15 15 197