def f(i, N):
    if i ==N:
        return
    else:
        print(A[i])
        f(i+1, N)

A = [1,2,3]
f(0,3)

def f_v(i, N, v):
    if i==N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f_v(i+1, N,v )
arr =[1,2,3,4]
N = 4
v = 6
print(f_v(0,N,v))