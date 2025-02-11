# 비정렬 상태에서 검색
def seq2_search(arr, N, key):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == key:
                return 1 # key를 찾는 경우
    return 0



# 정렬 상태에서 검색
def seq_search2(arr, N, key):
    for i in range(N):
        if arr[i] ==key:
            return i
        elif arr[i]>key:
            return -1
    return -1   # 모든 요소가 key보다 작을 떄

arr = [3,7,2,4,56,23,11]
arr.sort()
print(arr)
print(seq_search2(arr, len(arr), 11))

arr = [[1,2,3], [4,5,6],[7,8,9]]

print(seq2_search(arr, 3, 3))