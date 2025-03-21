def dfs(s, t):
    '''s를 규칙에 맞춰 바꾸면서 t가 될 수 있으면 1, 안되면 0'''
    if len(s) == len(t):
        return int(s == t)

    result = 0
    # A를 뒤에 붙인 경우
    # | : 비트연산자의 OR    result |= dfs(s + "A", t)

    # B를 붙이고 뒤집은 경우
    result |= dfs((s + "B")[::-1], t)

    return result

S = input()
T = input()

print(dfs(S, T))
