# 오름차순
def bubbleSort_ascd(a, N):  #a: 정렬 대상 리스트, N: 원소 수
    for i in range(N-1, 0, -1): # 범위: 끝부터 진행=> 마지막에 맥스 채우고 끝내려고
    # i가 큰 값부터 적용되서 마지막에 최댓값 채우고 다음 i번째는 그 부분 제외하고 검사 가능
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a    #정렬 완료
# 내림차순
def bubbleSort_dscd(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] < a[j+1]:   #비교 부분만 바뀌면 내림, 오름차순
                a[j], a[j+1] = a[j+1], a[j]
    return a