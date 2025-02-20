import sys
sys.stdin = open('lsit1_gravity_input.txt', 'r')

# 상자가 쌓인 방, 방이 오른쪽으로 90도 회전하여 낙하
# 낙차가 가장 큰 상자의 낙차 값을 리턴
# 방은 세로 100
# 상자가 놓인 가로 칸의 수는 N, 다음 줄에 각 칸의 상자 높이
T = int(input())

for tc in range(1, T+1):
    N = int(input())    #상자 쌓인 칸 수
    box = list(map(int, input().split())) #상자들 높이

    mx = 0  #낙차가 제일 큰 값
    for i in range(N-1):    # 마지막 위치한 상자는 낙차 0
        cnt = 0
        for j in range(i+1, N): # i상자의 오른쪽(i+1 ~ N-1)에서 i높이(값)보다 낮은지 높은지 확인
            if box[i]>box[j]:   # i가 높을 때 => 오른쪽 상자의 개수 = 낙차
                cnt += 1
        if mx < cnt:    # cnt가 크면
            mx = cnt    # mx 업데이트

    print(f'#{tc} {mx}')

# 문제가 요구하는 값의 정체를 파악하기