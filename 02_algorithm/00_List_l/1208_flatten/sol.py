import sys
sys.stdin = open('input.txt', 'r')

# 높은 곳 상자를 낮은 곳에 옮기기
# 평탄화: 최고점과 최저점의 간격을 줄이는 작업
# 평탄화 완료 시 최고점-최저점<=1
# 상자 옮기는 횟수 제한
T = 10
for test_case in range(1, T+1):
    D = int(input()) #덤프횟수
    arr = list(map(int, input().split()))   #상자위치

    for p in range(D): #덤프시도
        max_idx = arr.index(max(arr))
        arr[max_idx] -= 1
        min_idx = arr.index(min(arr))
        arr[min_idx] += 1

    print(f'#{test_case} {max(arr) - min(arr)}')