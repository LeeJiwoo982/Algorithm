a = [1,2,3]
n = len(a)

for i in range(1<<n):
    for j in range(n):
        s = 0
        if i & (1<<j):
            s += a[j]
        print(s)
# 컴퓨터는 비트로 이루어졌기에 비트연산자를 이용하면 더 편하다