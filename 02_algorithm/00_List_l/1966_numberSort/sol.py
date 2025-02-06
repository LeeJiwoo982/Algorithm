import sys
# N 길이의 숫자열을 오름차순으로 정렬 후 출력

sys.stdin = open('input.txt', 'r')
T = int(input()) #10개

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    k = max(arr)
    cnt = [0] * (k+1)

    for x in arr:
        cnt[x] += 1 #정렬의 요소 별 카운팅해서 cnt에 카운트

    for r in range(1, k+1):
        cnt[r] += cnt[r-1]      # 오른쪽 요소와 합치기

    # 누적개수를 이용해서 순서를 찾기
    TEMP = [0] * N
    for i in range(N-1, -1, -1):
        cnt[arr[i]] -= 1
        TEMP[cnt[arr[i]]] = arr[i]
    TEMP = list(map(str, TEMP))
    TEMP = ' '.join(TEMP)
    print(f'#{test_case}', TEMP)