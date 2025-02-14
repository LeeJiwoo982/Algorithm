def countingSort(data, temp, k): # 원본 배열, 정렬완료 값 넣을 배열, 최댓값(cnt의 크기결정)
    '''카운팅 리스트를 추가로 생성하여 O(N+k)로 빠른 정렬 가능, 정수만 가능'''

    cnt = [0] * (k+1)
    for i in range(len(data)):
        cnt[data[i]] += 1

    for i in range(1, k+1):
        cnt[i] += cnt[i-1]
