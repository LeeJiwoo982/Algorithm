import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    exp = input()   #중위표현식 인풋
    out = ''    #후위표현식으로 변환된 문자열 저장

    stack = []  #연산자 저장 스택(높은순위가 먼저 나와야 함

    # 중위표현식을 후위표현식으로
    #연산자를 우선순위에 따라

    for c in exp:   #exp 검사
        if c == "*":    #우선순위 높은 연산자 *이면
            if not stack or stack[-1]=='+': #스택이 비었거나, top의 우선순위가 낮다면
                stack.append(c) #우선순위 높은 *을 추가
            else:   #top의 우선순위가 같은 연산자거나, stack이 있거나
                while stack and stack[-1] =='*':    #출력
                    out += stack.pop()
                stack.append(c)
        elif c =='+':
            while stack:
                out += stack.pop()
            stack.append(c)

        else:
            out += c

    while stack:
        out += stack.pop()

    stack2 = []
    for c in out:
        if '0'<=c<='9':
            stack2.append(int(c))
        elif c =='+':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1+num2)
        elif c == '*':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1*num2)
    print(f'#{tc} {stack2.pop()}')