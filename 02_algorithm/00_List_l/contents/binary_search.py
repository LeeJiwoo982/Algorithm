def binarySearch(a, N, key):    #key를 찾으면 인덱스, 실패하면 1-반환
    # 검색 구간 설정
    start = 0       
    end = N-1
    
    # 구간에 1개 이상의 원소가 있을 때 검색 수행하라
    while start <=end:
        mid_i = (start + end) // 2

        # 검색 성공
        if a[mid_i] == key:
            return mid_i

        # 중앙값이 key 보다 큰 경우 => 왼쪽 구간 선택 => end가 축소
        elif a[mid_i] > key:
            end = mid_i - 1

        # key 보다 작은 경우 => 오른쪽 구간 선택 => start 축소
        else:
            start = mid_i

    return -1   # 검색구간이 남아 있지 않다 == 검색 실패 == 찾는 값이 없다.
arr = [1,5,7,9,12,45,78,89] # 오름차순 정렬 배열
print(binarySearch(arr, len(arr), 19))
print(binarySearch(arr, len(arr), 89))
print(binarySearch(arr, len(arr), 2))