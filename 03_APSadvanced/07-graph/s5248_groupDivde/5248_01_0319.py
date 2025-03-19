import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def find(a):
    global parents
    if parents[a] == a: # 서로소 집합의 대표자를 찾았을 때
        return a

    return find(parents[a])     
    #내가 대표자가 아니라면 
    # 내 부모가 대표자인지 확인한다.
    # 내 부모의 대표자를 찾기

# path compression
def find2(a):
    global parents
    if parents[a] == a: #서로소인 집합의 대표자를 찾으면 그 대표자 반환
        return a

    parents[a] = find2(parents[a])  #나의부모가 대표자를 찾음
    return parents[a]

def union(a, b):
    '''a, b 일반 노드의 번호, 각각의 대표자를 찾고 자식으로 만들기'''
    aRoot = find(a)
    bRoot = find(b)
    
    if aRoot != bRoot:
        parents[bRoot] = aRoot  # bRoot의 부모를 aRoot로 만든다
    # 대표자가 같으면 아무일도 안 일어남

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 노드의 개수
    arr=  list(map(int, input().split()))
    
    # make set
    parents = [0] * (N + 1)
    # 젤 처음은 본인이 본인의 대표 = 부모, n개의 집합
    for i in range(1, N+1):
        parents[i] = i  # 본인이 부모


    # M번의 유니온을 진행
    for i in range(M):
        a = arr[2*i]
        b= arr[2*i + 1]
        
        # 두 대표자가 다른 경우에만 유니온 가능
       
        union(a, b)
        
    # 그룹의 개수를 센다
    # 대표자의 수를 세면 = 그룹의 개수
    groups= set()
    for i in range(1, N+1):
        groups.add(find(i))

    print(f'#{tc} {len(groups)}')