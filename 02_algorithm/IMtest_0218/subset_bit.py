arr = [3,4,5,7,1,2]
n = len(arr)

for i in range(1<<n): # 2^n 까지
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end= ", ")
    print()
print()

