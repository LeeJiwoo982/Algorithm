import sys
sys.stdin = open('sample_input.txt', 'r')
# 0-9까지 숫자가 적힌 N장의 카드
# 카드 중 가장 많이 나온 숫자와 그 카드가 몇 장인지 출력하라
# 장수가 같다면 숫자가 큰 쪽을 출력한다.
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt = [0] * 10              # 카드숫자=인덱스로 하기에 10자리로
    for x in arr:
        cnt[x] += 1             # 카드숫자에 대응하는 cnt인덱스에 추가
    # cnt 완성

    mx_cnt = 0                      # 중복이 제일 많은 카드 수
    card_num = 0
    for i in range(10):
        if mx_cnt <= cnt[i]:
            card_num, mx_cnt = i, cnt[i]

    print(f'#{test_case} {card_num} {mx_cnt}')