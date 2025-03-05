def pre_order(n):
    # 완전이진트리 전위순회
    if n<=N:    # 실존하는 정점일때  # leaf이면 멈추게.
        print(n, end=' ')
        pre_order(n*2)      # 왼쪽자식
        pre_order(n*2+1)    # 오른쪽자식
    
    
N = 9 # 완전이진트리 정점 수

tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] #0인덱스는 비워둠. 1부터 시작함
pre_order(1)    # 1 2 4 8 9 5 3 6 7
