import sys
sys.stdin = open('sample_input.txt', 'r')

def find_room(cur, ori):
    '''현재방과 가야할 방 정보를 받고'''
    global time, corridor

    # 홀수방과 짝수 방 사이에 복도가 있음
    # cur, ori 값을 복도의 인덱스 값으로 변경
    cur = cur // 2 - 1 if cur % 2 == 0 else cur // 2
    ori = ori // 2 - 1 if ori % 2 == 0 else ori // 2

    # 현재방과 돌아갈 방의 위치 비교
    # 작은 값에서 큰 값으로 순회
    # 복도가 한번도 안 지나간 상태일때 복도에
    if ori < cur:
        for i in range(ori, cur + 1):
            if corridor[i] == 0:
                corridor[i] += 1
            else:
                time += 1
                corridor = [0] * 199
                corridor[i] += 1

    else:
        for i in range(cur, ori + 1):
            if corridor[i] == 0:
                corridor[i] += 1
            else:
                time += 1
                corridor = [0] * 199
                corridor[i] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 방으로 돌아가야 하는 학생 수 = 순회

    corridor = [0]*199  #학생이 지나갈 길. 겹치기 금지
    time = 1

    for _ in range(N):
        cur, ori = map(int, input().split())  # 현재 방 current, 돌아갈 방 original 원래방
        find_room(cur, ori)

    print(f'#{tc} {time}')
    
# 제출란의 input에서 오류남