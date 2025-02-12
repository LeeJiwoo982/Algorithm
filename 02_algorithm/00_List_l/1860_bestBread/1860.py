import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    N,M,K = map(int, input().split())
    times = list(map(int, input().split()))
    cnt = [0]*11_112
    #cnt[t] t초에 도착하는 사람 수

    for time in times:
        cnt[time] +=1
    #M초마다 빵 K개 생성
    # t초에 도착하는 사람 수 만큼 재고에서 빼준다. 재고 부족 imposi
    #그냥 끝나면 possi

    ans = 'Possible'
    breads = 0
    for t in range(0, 11_112):
        if t !=0 and t %M==0:
            breads += K
        if cnt[t]>breads:
            ans='Impossible'
            break
        breads -=cnt[t]

    print(f'#{tc} {ans}')