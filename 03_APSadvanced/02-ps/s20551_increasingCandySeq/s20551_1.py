import sys
sys.stdin = open('sample_input.txt', 'r')

# 세 개의 상자 A < B < C 사탕의 개수
# 만약 이전 상자의 캔디개수가 더 많으면 먹어서 수를 맞추기
# 최소로 먹는 양, 만약 불가능하면 -1
#=======문제읽기
#=======설계
# 자료구조
#       A, B, C 비교
# 알고리즘
#      b랑 c 검사, a랑 b 검사
T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    if C < 3 or B < 2:    #B와 C가 1이면 증가하는 수로 만들 수 없음
        print(f'#{tc} -1')
        continue
    
    candy = 0   # 증가시키기 위해 먹은 캔디 개수
    if B >= C:
        # B가 C보다 클 때
        candy += B - (C-1)
        B = C-1

    if A >= B:
        candy += A - (B-1)
        A = B-1 #A는 B보다 하나만 작아도 됨. 위의 경우도 동일

    print(f'#{tc} {candy}')