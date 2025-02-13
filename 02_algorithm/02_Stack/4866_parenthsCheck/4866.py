import sys
sys.stdin = open("sample_input.txt", "r")

# {},()가 제대로 짝을 이뤘는지 검사
# 정상이면 1, 아니면 0

T = int(input())
for tc in range(1, T+1):
    code = input()
    k = len(code)
    cnt = []*(k+1)
    top = -1
    for s in code:
        if s == "(" or s=='{':
            cnt.append(s)
        elif s == ')':
            check = cnt.pop()
            if check != '(':
                print(f'#{tc} 0')
                break
        elif s=='}':
            check = cnt.pop()
            if check != '{':
                print(f'#{tc} 0')
                break
    if cnt: print(f'#{tc} 0')
    else: print(f'#{tc} 1')