# import sys
# sys.stdin = open("sample_input.txt", "r")

# 정수십진수는 2로 나눈 나머지가 이진수값이 됨
# 실수십진수는 연쇄적으로 2를 곱하면 됨.
# 곱하고 1이상이면 1, 1미만이면 0, 정수부분 뺀 소수부분을 0될때까지 진행
def float_to_binary(N):
    '''실수부분을 이진법으로 표기하기'''
    binary = ''

    while N:    #N이 0일때까지 반복
        # 2진수 길이가 12자리를 넘어갈 경우에는 나가기
        if len(binary) > 12:
            return 'overflow'

        N *= 2  #이진수 검사 전 곱하기
        if N >= 1:   #정수부분 1나오면
            binary += '1'
            N -= 1
        else:
            binary += '0'
    return binary
    #N이 0이되어 while을 나가고 return
    return binary

T = int(input())
for tc in range(1, T+1):
    N = float(input())  #0.245 이런형태...흠...
    result = float_to_binary(N)

    print(f'#{tc} {result}')
    

