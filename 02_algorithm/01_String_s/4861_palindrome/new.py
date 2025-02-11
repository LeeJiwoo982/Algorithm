import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
def pelindrome_out(arr, N, M):
    '''N*N의 배열에서 회문을 찾고 반환한다'''
    #행탐색
    for r in range(N):
        for c in range(N-M+1):
            text = ''.join(arr[r][c:c+M])
            if text == text[::-1]:
                return text
    #열탐색
    for c in range(N):
        for r in range(N-M+1):
            text = ''.join([arr[r+i][c] for i in range(M)]) #열은 슬라이싱이 안됨=> for문으로
            if text == text[::-1]:
                return text

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[c for c in input()]for _ in range(N)]   #input()만 하면 한덩이 문자열로 나와서

    answer = pelindrome_out(arr, N, M)
    print(f'#{tc} {answer}')