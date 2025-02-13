'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''
txt = input()

top = -1
stack = [0]*100

ans = 1
for x in txt:
    if x == '(':    #여는 괄호의 경우: push
        top+=1
        stack[top]=x
    elif x == ')':  # 닫는 괄호의 경우: pop
        if top == -1:    # 오류!!!스택이 비어있으면 = 여는 괄호가 없을면 = top이 없을 때
            ans = 0
        else:           # 스택이 있으면, 여는 괄호 하나 버림
            top -= 1
if top != -1:   #오류!!!!여는 괄호가 남아있으면
    ans = 0
print(ans)
