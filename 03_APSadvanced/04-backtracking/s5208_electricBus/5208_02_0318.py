import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def go(idx, battery, cnt):
    '''idx 정류장(배터리)번호, battery:현재 배터리 용량, cnt:지금까지 교환 횟수'''
    global min_cnt

    battery -= 1    #그다음 번호로 갈 때마다 배터리 감소

    if battery < 0:
        return 

    if cnt >= min_cnt:  # 가지치기
        return  #현재 교체횟수가 최소보다 크면 종료

    if battery >= 0 and idx == N:   # 배터리 0보다 크거나 같은 상황, 끝까지 온
        min_cnt = min(cnt, min_cnt) # 최소 카운트 갱신
        return  # 종점 도달로 종료
    
    # 그냥 가기
    go(idx + 1, battery, cnt)   # 현재 배터리와 교체횟수 그대로

    # 교체 하기
    go(idx + 1, M[idx], cnt + 1)

for tc in range(1, T+1):
    N, *M = map(int, input().split())
    # N 정류장 개수, M 배터리 용량 배열 N-1개
    
    M = [0] + M
    # 1번 배터리는 장착 후 출발, 2~N-1번만 그냥 or 교체 고려
    # N번 배터리 없음
    
    min_cnt = float('inf')
    
    go(2, M[1], 0)  #1번 배터리 장착 후, 교환횟수 0, 2번배터리부터 고려 시작

    print(f'#{tc} {min_cnt}')