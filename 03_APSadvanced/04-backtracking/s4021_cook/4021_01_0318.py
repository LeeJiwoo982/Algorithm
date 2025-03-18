import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def similar_2dishes(r, dif):    # 재료, 차이
    # 가지치기

    # 종료조건




for tc in range(1, T+1):
    N = int(input())    # 재료 개수
    S = [list(map(int, input().split())) for _ in range(N)] 
    # 재료들의 시너지, 같은 재료의 경우 시너지 0으로 표시 .사용하지 않는 값

    diff_mn = float('inf')  # 두 음식 맛의 차이 최솟값 저장
    visited = [0] * N   # 재료의 사용 체크용. 사용체크 하고 끝나면 다시 0으로 초기화해야됨

    similar_2dishes(0, 0)   # 첫재료선택, 맛차이