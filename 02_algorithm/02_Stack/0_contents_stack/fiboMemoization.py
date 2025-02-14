# memo 를 위한 배열 할당, 0으로 초기화
# memo[0] 를 0 ,memo[1] 1로 초기화

def fibo1(n):
    global cnt      #memo 형식상 작성하셨다고
    cnt +=1
    if n>=2 and memo[n]==0: #2이상의 값이 들어오면, 그리고 n인덱스값이 0이면, 계산이 안된것
        memo[n]=fibo1(n-1)+fibo1(n-2)
    return memo[n]
n=9
memo = [0]*(n+1)
memo[0] =0
memo[1] =1
cnt=0
print(fibo1(n), cnt)