import sys
sys.stdin = open('sample_input.txt', 'r')

def binary_Search_cnt(N, Nk):
    '''이진탐색으로 중앙값을 재정의하는 횟수'''
    book = list(range(1, N + 1))  # 책
    start = 0
    end = N - 1
    l = start + 1  # 첫페이지
    r = end + 1  # 끝페이지
    cnt = 0

    while start < end:
        c = int((start + end) / 2)
        if book[c] == Nk:
            return cnt
        elif book[c] > Nk:
            end = c - 1
        else:
            start = c + 1
        cnt += 1
    return -1

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # P:책전체쪽수, Pa, Pb: 찾을 쪽 번호
    A = binary_Search_cnt(P, Pa)
    B = binary_Search_cnt(P, Pb)
    if A<B:
        print(f'#{tc} A')
    elif A>B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')