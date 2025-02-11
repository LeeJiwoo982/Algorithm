import sys
sys.stdin = open('sample_input.txt', 'r')

#a=리스트, N:크기
def selection_sp_sort(a, N):
    for i in range(N-1):    # 최솟값을 찾는 구간의 시작 인덱스
        min_idx = i         # 최솟값 인덱스 초기화, 구간의 맨 앞 원소
        max_idx = i

        if i %2==0:
        # 1. 리스트에서 최댓값의 위치를 찾는다
            for j in range(i+1, N):     # 실제 최솟값인지 비교
                if a[max_idx] <a[j]:
                    max_idx = j
                # if i != mid_idx:  # 교환을 i번 비교 후 i번 교환.. 연산이 많아짐
                # 2. 리스트 맨 앞의 값과 교환
            a[i], a[max_idx] = a[max_idx], a[i]
        else:
            for k in range(i+1, N):
                if a[min_idx] > a[k]:
                    min_idx = k
                # if i != mid_idx:  # 교환을 i번 비교 후 i번 교환.. 연산이 많아짐
                # 2. 리스트 맨 앞의 값과 교환
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

T= int(input())
# 특별한 정렬 숫자 10개까지 출력
# N개의 정수, 가장큰-가장작은-2번째큰-2번째작은
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sp_arr = selection_sp_sort(arr, N)
    sp_arr = ' '.join(map(str, sp_arr[0:10]))
    print(f'#{tc} {sp_arr}')
