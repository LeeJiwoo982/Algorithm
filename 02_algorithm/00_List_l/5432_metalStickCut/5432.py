import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    info = list(input())
    laser = []
    start = []
    stick = []
    cnt =0
    k = len(info)
    for i in range(k):
        if info[i]=='(' and info[i+1]==')':
            info[i], info[i+1]=0, 0
            laser.append(i)
        if info[i] =='(':
            start.append(i)
        elif info[i]==')':
            s_e = start.pop()
            stick.append([s_e, i])

    for s in stick:
        for l in laser:
            if s[0]< l < s[1]:
                cnt += 1
    result = cnt + len(stick)
    print(f'#{tc} {result}')
    # 레이저의 위치 인덱스,
    # 막대기의 인덱스로 범위를 구해서
    # 막대기 범위에 레이저가 몇개 위치하는 지로 잘린막대기 확인
