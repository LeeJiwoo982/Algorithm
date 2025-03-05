import sys
sys.stdin = open('sample_input.txt', 'r')
def find_child(N):
    '''자식노드를 찾는 함수'''
    global cnt  #자식 발견 횟수
    if N:
        cnt += 1
        find_child(left[N])
        find_child(right[N])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    #E는 간선 수, 노드 번호=E+1
    # 노드 N을 루트로 하는 서브 트리에 속한 노드 개수
    arr = list(map(int, input().split()))   #부모-자식 쌍

    left = [0]*(E+2)    #왼자식
    right = [0]*(E+2)   #오른자식
    # par = [0]*(E+2)

    for i in range(E):  #부모를 인덱스로 한 자식
        p, c = arr[i*2], arr[i*2+1]
        # par[c] = p

        if left[p]== 0:
            left[p] = c
        else:
            right[p] = c

    # print(child)

    cnt = 0
    find_child(N)
    print(f'#{tc} {cnt}')


