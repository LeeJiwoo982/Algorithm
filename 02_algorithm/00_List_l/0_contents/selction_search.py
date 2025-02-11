def selectionSearch(a, N):
    for i in range(N-1):    # 최솟값을 찾는 구간의 시작 인덱스
        mid_idx = i         # 최솟값 인덱스 초기화, 구간의 맨 앞 원소

        # 1. 리스트에서 최소값의 위치를 찾는다
        for j in range(i+1, N):     # 실제 최솟값인지 비교
            if a[mid_idx]>a[j]:
                mid_idx =j
        # if i != mid_idx:  # 교환을 i번 비교 후 i번 교환.. 연산이 많아짐
            # 2. 리스트 맨 앞의 값과 교환
        a[i], a[mid_idx] = a[mid_idx], a[i]
    return a

arr = [10, 25, 64, 22, 11]
result = selectionSearch(arr, len(arr))
print(result)