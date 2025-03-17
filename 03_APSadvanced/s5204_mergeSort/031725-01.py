import sys
sys.stdin = open("sample_input.txt", 'r')

def mergesort(lft, rgt):
    '''왼쪽과 오른쪽 구간으로 분할하기'''
    # 1. 길이가 1인 것까지 쪼개기
    # print(f'[{lft}, {rgt}) : 길이 {rgt - lft}')
    if lft + 1 < rgt:   #이렇게 해야 길이가 1이 된다. 외우지 말고 한 번 찍어보면서 하기
        mid = (lft + rgt) // 2
        mergesort(lft, mid)     #[lft, mid)
        mergesort(mid, rgt)     #[mid, rgt)

        # 2. 쪼개진 배열 합치기
        # print(f'merge({lft}, {mid}, {rgt})') # 잘 되고 있는지 항상 확인
        merge(lft, mid, rgt)
        
# 주어진 배열 arr에서 [lft, rgt) 구간만 정렬된 배열로 만든다
# L, R 사용 부분만 복사해서 만들고
# 합치면서 arr에 덮어쓴다
def merge(lft, mid, rgt):
    global arr, cnt
    '''병합하기'''
    # 사용할 부분만 복사 떠오기
    L = arr[lft : mid]
    R = arr[mid : rgt]

    if L[-1] > R[-1]:
        cnt += 1

    i = j = 0
    k = lft #이부분이 중요

    while i < mid - lft and j < rgt - mid:  #배열의 범위 안에
        if L[i] <= R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        else:
            arr[k] = R[j]
            k += 1
            j += 1

    # 남은 배열 옮기기
    while i < mid - lft:
        arr[k] = L[i]
        k += 1
        i += 1
    while j < rgt - mid:
        arr[k] = R[j]
        k += 1
        j += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))   #주어진 숫자배열


    # 구간을 어떻게 하느냐..
    ## 보통은 구간 = 폐구간으로 놓는 것이 편하다
    ## [s, e] : s ~ e (e도 포함)
    
    # 그러나 문제의 조건: 오른쪽이 열린 구간으로 되어 있음
    # [0, N)
    # L[0 : N // 2] : 0 ~ (N // 2 - 1)
    # R[N // 2 : N] : N // 2 ~ (N - 1)
    
    # lft는 포함, rgt는 포함하지 않게
    # 모든 구간 한 쪽이 열린 구간으로 통일
    cnt = 0
    mergesort(0, len(arr))

    # print(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')