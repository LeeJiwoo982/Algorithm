a = [1,2,3]
n = len(a)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(a[j], end=', ')
    print()
print()


# 컴퓨터는 비트로 이루어졌기에 비트연산자를 이용하면 더 편하다
