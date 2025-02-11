import sys
from pprint import pprint
sys.stdin = open('sample_input.txt','r')

T = int(input()) # 테스트 케이스 수

# 주어진 2차원 배열에서 펠린드롬을 찾아 반환하는 함수
def pelindrome(arr, N, M):
    ## 행 우선 탐색(가로)
    ## - 모든 경우의 가로방향 문자열을 만든다다
    for r in range(N): # 모든 행에 대해서 반복.
        for c in range(N-M+1): # 문자열의 길이(M)
            # (r, c)를 기준점으로하는 문자열
            text = ''.join(arr[r][c:c+M]) # M 개의 문자를 합쳐 문자열 만들기
            if text == text[::-1]: # 뒤집어서 일치하면 회문
                return text

    ## 열 우선 탐색(세로)
    for c in range(N): # 모든 열에 대해서 수행
        for r in range(N-M+1):
            text = ''.join([arr[r+i][c] for i in range(M)])
            if text == text[::-1]:
                return text


for tc in range(1, T+1):
    # N, M 입력받기기
    N, M = list(map(int, input().split()))
    # 2차원 배열 입력 받기
    arr = [[c for c in input()] for _ in range(N)]

    ans = pelindrome(arr, N, M)

    print(f"#{tc} {ans}")