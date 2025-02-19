# 회전
# N개의 숫자로 이루어진 수열
# 맨 앞 수 -> 맨 뒤로 : M번
# 최종 맨 앞 숫자 출력
import sys
sys.stdin = open('sample_input.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 수열 크기, 작업횟수
    arr = list(map(int, input().split()))   # 크기 N 자연수만 10억이하

    # for _ in range(M):  #작업횟수
    #     for i in range(N):  #인덱스 위치 이동...흠....
    #         # arr[i], arr[(i-1)%N] = arr[(i-1)%N], arr[i]       # 바꾸려면 전체를 한방에 바꿔야 함...N의 크기달라지는 걸 감당 X

    # 첫째를 가리키는 포인터를 변화 시키기
    for i in range(M):
        point = arr[(i+1)%N]
    print(f'#{tc} {point}')

    #print(f'#{tc} {arr[M%N]}') #hmmhmm