import sys
sys.stdin = open('input.txt', 'r')

# 전봇대 두개에 전선 여러개
# 전선 교차. 그러나 같은 끝점은 없음
# 교차하는 경우
# 기준선vs이전 선 시작>, 끝< or 시작<, 끝>
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N개의 전선 정보가 들어옴

    # 기준으로 사용 후에 저장할 전선 정보 리스트
    lines = []
    cross = 0
    for _ in range(N):
        start, end = map(int, input().split())

        if lines:   # 저장된 값이 있을때만, 첫번째에는 돌지않기
            for s, e in lines:
                if start > s and end < e:
                    cross += 1
                elif start < s and end > e:
                    cross += 1

        lines.append((start, end))
    print(f'#{tc} {cross}')