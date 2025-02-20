def countingSort(data, temp, k): # 원본 배열, 정렬완료 값 넣을 배열, 최댓값(cnt의 크기결정)
    '''카운팅 리스트를 추가로 생성하여 O(N+k)로 빠른 정렬 가능, 정수만 가능'''
    cnt = [0] * (k+1)   # 원본 항목 값이 cnt의 인덱스로 사용하기에 cnt크기는 원본 항목의 최댓값+1

    #1단계 카운팅
    for i in range(len(data)):
        cnt[data[i]] += 1

    #2단계 누적
    for i in range(1, k+1):
        cnt[i] += cnt[i-1]

    #3단계 정렬
    for i in range(len(data)-1, -1, -1):    #마지막인덱스부터 삽입
        cnt[data[i]] -= 1   #먼저 1 감소시켜야 인덱스값과 일치
        temp[cnt[data[i]]] = data[i]

data = list(map(int, input().split()))
temp = [0]*len(data)    #원본 데이터와 같은 크기로

# 사용되는 배열 3개, 필요 값: k, 정렬은 다른 배열에 배치하게 됨