import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())    #스위치 개수
    switch = list(map(int, input().split()))    # 스위치 상태
    S = int(input())    #학생 수

    for _ in range(S):
        s, n = map(int, input().split())  # 학생정보 s:성별, n:스위치번호
        if s==1:    #남학생의 경우
            j=n-1   #스위치번호를 인덱스에 맞게 변경하여 j에 할당
            while j < N:    #j가 스위치개수보다 작을 때까지 반복
                if switch[j] == 0:  # j에서 0이면
                    switch[j] = 1   # 1로 바꾸고
                    j += n          # j를 번호의 배수로 증가 시키고 위로 가기
                else:
                    switch[j] = 0
                    j += n
        else:       # 여학생의 경우
            i = n-1     # 스위치번호 인덱스에 맞게 변경해서 i할당
            if n <= N//2:   # 받은 번호가 전체 개수절반보다 아래번호일 때
                R = n - 1       # 대칭 순회를 위한 범위 지정
                for r in range(n):
                    if switch[i-r] == switch[i+r]:
                        if switch[i-r] == 0:
                            switch[i-r], switch[i+r] = 1, 1
                        else:
                            switch[i - r], switch[i + r] = 0, 0
                    else:
                        if switch[i] == 0:
                            switch[i] = 1
                        else:
                            switch[i] = 0
            else:           # 받은 번호가 스위치 절반보다 윗번일 때
                R = N- n + 1     # 대칭 순회를 위해 범위 지정\
                for r in range(R):
                    if switch[i-r] == switch[i+r]:
                        if switch[i-r] == 0:
                            switch[i-r], switch[i+r] = 1, 1
                        else:
                            switch[i - r], switch[i + r] = 0, 0
                    else:
                        if switch[i] == 0:
                            switch[i] = 1
                        else:
                            switch[i] = 0
    # 출력조건
    ## 스위치 출력은 한 줄에 20개씩, 21번 스위치가 있다면 둘째줄 맨앞으로
    # 스위치 결과를 20개씩 끊어서 배열로 저장
    # 배열을 출력
    print(f'#{tc}')
    for i in range(0, N, 20):
        print(' '.join(map(str, switch[i:i+20])))
