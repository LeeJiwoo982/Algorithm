import sys
sys.stdin = open('list1_basic_input.txt', 'r')

# N개의 양의 정수에서 가장 큰 수 와 가장 작은 수의 차이 출력
T = int(input())                            # 테스트 케이스 수 입력

for tc in range(1, T+1):                    
    N = int(input())                        # 입력받을 값의 개수 N개
    ai = list(map(int, input().split()))    # 값들, 스트링으로 칸을 두고 입력된 걸 칸을 띄우고 map으로 인트로 바꾸고

    mx = ai[0]     # 최대값 저장 변수, 배열의 첫값으로 초기화
    mn = ai[0]      #최솟값

    for i in range(N):
        if mx < ai[i]:  #최대값 변수보다 ai[i]이 크면
            mx = ai[i]  # ai[i]로 재할당
        if mn > ai[i]:  # 최소값 변수보다 작으면
            mn = ai[i]  # 재할당

    result = mx-mn  # 결과 변수에 최대-최소 계산한 값 저장
    print(f'#{tc} {result}')    #출력
    #1 630739
    #2 740510
    #3 838110

