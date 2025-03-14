import sys
sys.stdin = open('sample_input.txt', 'r')

# 노드 N을 루트로 하는 서브트리에 속한 노드의 개수 구하기
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    # E는간선의 개수, 노드는 1~E+1

    edge = list(map(int, input().split()))

    # 1. 주어진 간선 정보로 부모인덱스로 하는 자식배열 정리
    left = [0] * (E + 1)
    right = [0] * (E + 1)
    
    for i in range(E):  # 부모를 인덱스로 하는 자식 배열 채우기
        par = i * 2     # 자식배열에서 인덱스로 사용하는 부모번호
        child = i * 2 + 1   # 자식 노드의 값

        if left[par]:
            left[par] = child
        else:
            right[par] = child
            
    # 2.