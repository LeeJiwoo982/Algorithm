import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def find_heighest_peak(arr):
    '''제일 높은 봉우리의 좌표 찾기'''
    peak = []
    h = -1
    for r in range(N):
        for c in range(N):
            height = mt[r][c]
            if height > h:
                h = height
                peak = [(r, c)] # 더 높은 봉우리가 나오면 초기화
            elif height == h:
                peak.append((r, c)) # 같으면 좌표 추가
    return peak


def dfs(r, c, dist, k = True):
    '''제일 높은 봉우리의 최장 등산로 찾기'''
    global mx_dist, visited

    # 시작 좌표, 거리값, 공사가능여부(기본 True)
    mx_dist = max(mx_dist, dist)    # 최장 등산로 업데이트

    # 다음 위치 탐색
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc   # 다음 위치 좌표
        
        # 범위 벗어나면 or 방문한 곳이면 넘기기
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
            
        visited[nr][nc] = 1

        # 등산로 +1
        if mt[nr][nc] < mt[r][c]:
            visited[nr][nc] = True
            dfs(nr, nc, dist + 1, k)
            visited[nr][nc] = False
        
        # 등산로로 쓰기 어려울 때, 공사가 가능한 상태라면
        # 공사하면 등산로로 사용가능한 경우일 때
        elif k and (mt[nr][nc] - K < mt[r][c]):
            # 공사
            temp = mt[nr][nc]
            mt[nr][nc] = mt[r][c] - 1   # 현재보다 1만 낮추는게 긴 등산로 만들기 가장 이상적
            # 공사 후 이동
            visited[nr][nc] = True
            dfs(nr, nc, dist + 1, False)
            # 초기화
            visited[nr][nc] = False
            mt[nr][nc] = temp

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N; 지도 크기, K; 최대 공사 가능 깊이
    # K: 딱 한 곳을 정해서 최대 K 깊이 만큼 지형을 깎을 수 있다.

    mt = [list(map(int, input().split())) for _ in range(N)]
    # 제일 높은 봉우리 여러개(최대 5개)

    # start: 제일 높은 봉우리
    # end: 경로상 더이상 전진 불가능 할 때
    
    # 1. 제일 높은 봉우리 좌표 찾기
    # numpy 사용이 제일 빠르다고 한다.
    # 근데 라이브러리 설치해야 함.
    # $ pip install numpy
    '''
    import numpy as np
    mt_np = np.array(mt)
    max_val = mt_np.max()
    peak = list(zip(*np.where(mt_np == max_val)))
    '''
    start = find_heighest_peak(mt)

    # 2. 가장 긴 경로 찾으면서 공사도 같이.
    visited = [[False] * N for _ in range(N)]
    mx_dist = -1
    for sr, sc in start:
        visited[sr][sc] = True   # 작업표시
        dfs(sr, sc, 0)
        visited[sr][sc] = False   # 초기화

    print(f'#{tc} {mx_dist}')