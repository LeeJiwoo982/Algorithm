import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    info = input().strip()
    stack = []
    cnt = 0  # 잘린 막대기의 총 개수

    for i in range(len(info)):
        if info[i] == '(':
            stack.append('(')  # 막대기의 시작
        else:  # `)`
            stack.pop()  # 짝 맞추기 위해 `(` 제거

            if info[i - 1] == '(':  # 바로 앞이 `(`이면 레이저
                cnt += len(stack)  # 스택에 남아 있는 막대기 개수만큼 잘림
            else:  # 막대기의 끝
                cnt += 1  # 막대기 하나 추가

    print(f'#{tc} {cnt}')