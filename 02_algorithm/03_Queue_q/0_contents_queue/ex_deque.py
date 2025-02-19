from collections import deque

q = deque()
q.append(1)     # enqueue()
t = q.popleft() # dequeue()

# 살짝 느림
list_q = []
for i in range(1000000):
    list_q.append(i)
    print(f'어펜드: {i}')
for _ in range(1000):
    list_q.pop(0)
print('end')

#빠르다~
# deque_q = deque()
# for i in range(1000000):
#     deque_q.append(i)
#     print(f'덱:{i}')
#
# for _ in range(1000000):
#     deque_q.popleft()
# print('end')