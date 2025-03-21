# from sys import stdin
# def input():
#     return stdin.readline().rstrip()

    # 문자열의 뒤에 A를 추가한다.
    # 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
# 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 49, 2 ≤ T의 길이 ≤ 50, S의 길이 < T의 길이)
# S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.

def dfs(s, t):
    '''s를 규칙에 맞춰 바꾸면서 t가 될 수 있으면 1, 안되면 0'''
    # 종료 조건
    if len(s) == len(t):
        if s == t:
            return 1
        else:
            return 0
    else:
        pass

    s1 = s + "A"
    if dfs(s1, t) == 1:
        return 1

    s2 = s + "B"
    s2 = s2[::-1]
    if dfs(s2, t) == 1:
        return 1

    return 0
    # # 연산하기
    # for i in range(2):
    #     if i == 0:
    #         s1 = s + "A"
    #         dfs(s1, t)
    #     else:
    #         s2 = s + "B"
    #         s2 = s2[::-1]
    #         dfs(s2, t)

S = input()
T = input()

# 출력 결과로 바꾸기 가능 여부 초기화
# 기본은 안되는 것
result = dfs(S, T)

print(result)