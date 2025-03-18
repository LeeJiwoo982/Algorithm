import sys
sys.stdin = open('sample_input.txt', 'r')
# 선생님 풀이 버전

T = int(input())

def quicksort(lft, rgt):
    if lft < rgt: #구간의 길이가 2 이상이라면
        #주어진 배열을 [lft, rgt] 구간에 대해 쪼개기
        # 가장 왼쪽 원소(lft위치)를 pivot으로 삼고
        # pivot을 정렬된 위치에 놓고, pivot_idx 반환

        pivot_idx = partition(lft, rgt)
        quicksort(lft, pivot_idx - 1)
        quicksort(pivot_idx + 1, rgt)

def partition(lft, rgt):
    global arr
    pivot = arr[lft]    #해당 구간의 가장 왼쪽을 기준점으로
    i = lft
    j = rgt

    while i < j:
        # 피봇이 가장 큰 수일 경우
        while i < rgt and arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    # 피봇위치 변경 = 정렬된 위치로
    arr[lft], arr[j] = arr[j], arr[lft]

    return j


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 머지는 폐구간의 정의가 필요했음 [)
    # 퀵은 그냥 []으로 닫힌 구간 사용하기. 더 편하다
    quicksort(0, N-1)
    # print(arr)
    print(f'#{tc} {arr[N//2]}')