# 스택을 구현하자
# 구현한 스택을 이용하여 3개의 데이터 스택에 저장, 3번 꺼내서 출력
# 간단한 스택
top = -1
stack = [0]*10

top += 1    #push 1
stack[top] = 1

top += 1    # push 2
stack[top] = 2

top += 1    # push 3
stack[top]= 3

#pop
top -= 1
print((stack[top+1]))   # 3

top -= 1
print((stack[top+1]))   # 2

top -= 1
print((stack[top+1]))   # 1

# push와 pop의 구현 동작을 통일성을 맞추면 좋다.
# 함수 정의 과정은 return 전에 top += or -= 를 해야 하기에 일정하게 하면 좋다.

