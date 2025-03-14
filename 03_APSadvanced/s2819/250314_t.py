# 격자판의 숫자 이어 붙이기
# 한 번 거쳤던 격자칸 다시 거킬 수 있음 # visited 쓰지 않기
# 만들 수 있는 서로 다른 일곱 자리 수들의 개수
# 서로 달라야 함
# 그다음 숫자 예측하기도 어렵고, 규칙도 X>>완전 탐색
# 재귀호출 백트랙킹
# DFS 이동경로 파라미터로 전달
# 상하좌우
# 높이, level : 6
# 브랜치: 4
# 7개가 되면 완성된 수를 저장하고 중복 제거 => set

# 접근법
# - 시작지점: 전체 다 보기
# - 재귀를 돌리면서 숫자를 붙인다.
# - 숫자가 7자리가 되면, set에 넣기(중복제거_)

dy = [0,0,1,-1]
dx= [-1,1,0,0]
def recur(y, x, number):
    if len(number) == 7:    # 7자리가 되면 종료
        result.add(number)
        return 
    
    for i in range(4):  # 상하좌우
        new_y = y + dy[i]
        new_x = x + dx[i]

        # 범위 밖이면 continue
        if new_y <0 or new_y>=4 or new_x<0 or new_x>=4:
            continue

        recur(new_y, new_x, number + matrix[new_y][new_x])
    
T = int(input())
for tc in range(1, T+1):
    # int로 하면 0이 앞에 나올 수 없음. str으로 저장
    matrix = [input().split() for _ in range(4)]
    result = set()

    for y in range(4):
        for x in range(4):
            recur(y, x, matrix[y][x])

    # print(result)
    print(f'#{tc} {len(result)}')