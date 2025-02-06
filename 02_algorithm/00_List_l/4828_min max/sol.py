import sys
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #양수의 개수
    arr = list(map(int, input().split())) # 양수들 list로

    max_v = arr[0]
    min_v = 10*23425

    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    print(f'#{tc} {max_v - min_v}')

