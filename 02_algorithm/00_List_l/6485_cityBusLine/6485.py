import sys
sys.stdin=open('s_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 개수
    bus = [list(map(int, input().split())) for _ in range(N)]   # 버스가 지나가는 정류장범위
    P = int(input())    #정류장 개수
    busStop = [int(input()) for _ in range(P)]  #정류장번호, 중복있을수 있다고 함...

    k = max(busStop)+1
    # max_stop = max(max(b[1] for b in bus), max(busStop))
    cnt = [0] * k   # k => (max_stop+1)

    for b in bus:   #버스 순회
        for j in range(b[0], b[1]+1):   #하나의 버스가 지나가는 정류장 번호 순회
            if min(busStop)<= j <= max(busStop):
                # 맥스값을변수로 지정하면 매번 max계산 안해도 됨
                cnt[j] += 1 # 버스번호==cnt인덱스라 추가

    for i in range(k):
        for j in range(len(busStop)):
            if busStop[j] == i:
                busStop[j] = cnt[i]
    # 요청된 정류장에서 지나가는 버스 개수 가져오기
    # result = [cnt[stop] for stop in busStop]
    # 버스정류장리스트에서 cnt의 값을 빼온 것을 리스트로 다시 저장

    # 정류장에 지나가는 버스 수를 출력
    print(f'#{tc} {" ".join(map(str, busStop))}')
