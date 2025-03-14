N, W = map(int, input().split())

# 그래프 생성. 간선의 정보라 어떤게 부모고 자식인지 알 수 없음
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

# print(tree)
leaf_cnt = 0 # 얘는 boolean을 못알아 먹는듯... sum(1 for i in range(2, N+1) if tree[i] and len(tree[i] == 1))
for i in range(2, N+1):
    if tree[i] and len(tree[i]) == 1:
        leaf_cnt += 1
# print(leaf_cnt)

print(W/leaf_cnt if leaf_cnt > 0 else 0)