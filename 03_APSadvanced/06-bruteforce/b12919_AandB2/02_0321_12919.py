def reverse_dfs(t):
    '''결과에서부터 지워가며 S만들기'''
    # 둘의 길이가 같을 때
    # 그 둘이 같다면 1, 아니면 0 출력됨
    # 파이썬에서 False는 0으로 판정
    if len(t) == len(S):
        return int(t == S)  # 트루면 1, 아니면 0을 출력

    # 결과문자가 마지막이 A고 그거 0 ~ -2 로 dfs
    # 둘이 만족하면 1
    if t[-1] == 'A' and reverse_dfs(t[:-1]):
        return 1
    # t의 첫값이 B, 그 t: 1~ -1까지, 그걸 뒤집기 한게 맞으면 1
    if t[0] == 'B' and reverse_dfs(t[1:][::-1]):
        return 1

    # 다 안되면 0
    return 0

S = input()
T = input()
print(reverse_dfs(T))
