import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    clap = list(map(int, input().strip()))
    k = len(clap)
    cnt = 0 # 박수치는사람
    hire =0 #고용해야 할 사람

    for i, c in enumerate(clap): # 인덱스=필요 사람 수
        if cnt < i: #실제 박수치는 사람이 i명보다 작을 경우
            hire += (i-cnt)    #필요 인원에서 현재 인원을 빼서 보충
            cnt = i   #실제 박수치는 인원
        cnt += c
    print(f'#{tc} {hire}')

### hire 누적되어야 함
## cnt<i 인 경우에만 추가 인원이 필요함 조건문 필요
## 과거에 부족했던 경험이나 실제 박수치는 사람의 수보다
## 고용에 필요한지 안한지를 판단하는게 중요