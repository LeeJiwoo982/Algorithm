import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def quicksort(lft, rgt):
    '''퀵 정렬 함수; 재귀'''


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))   #정렬할 배열
    
    #퀵 정렬. 기준점pivot, 왼i, 오j. 
    # 피봇을 계속 계산하면서 최종 정렬될 수 있게
    # 기준점 선정은 자유: 맨 왼쪽 or 맨 오른쪽 or 중가리
    quicksort(0, N-1)   #처음 호출은 배열 전체 인덱스 닫힌 구간