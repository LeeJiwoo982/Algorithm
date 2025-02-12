import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    #입력값
    char = list(map(str, input()))  #set() 저장하면 좋다. 중복은 굳이 필요 없어서
    txt = list(map(str, input()))

    cnt = [0]*len(char)

    for i in range(len(char)):
        for t in txt:
            if char[i] == t:
                cnt[i] += 1
    mx = 0
    for j in cnt:
        if mx < j:
            mx = j

    print(f'#{tc} {mx}')


