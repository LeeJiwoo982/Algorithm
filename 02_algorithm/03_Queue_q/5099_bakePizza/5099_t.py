from collections import deque
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())

    cheases = list(map(int, input().split()))   #피자의 치즈양
    nums = list(range(1, M+1))  #치즈에 번호매기기
    pizzas = list(zip(nums, cheases))#[(피자번호, 치즈양), ...]

    q = deque() #화덕 = 큐
    for _ in range(N):
        q.append(pizzas.pop(0)) #피자 화덕에 넣기

    #종료 조건 최후의 피자 1개가 남을 때
    # 반복: 화덕 피자 개수2개 이상인 경우
    while len(q)>1:
        num, chease = q.popleft()
        chease //= 2

        if chease == 0 and pizzas:  # 막 꺼낸 피자의 치즈 0, 굽지않은 피자있으면
            q.append(pizzas.pop(0))
        elif chease > 0:
            q.append((num, chease)) #다시 넣기

    #벗어나면 len(q)==1

    num, chease = q.popleft()
    print(f'#{tc} {num}')
