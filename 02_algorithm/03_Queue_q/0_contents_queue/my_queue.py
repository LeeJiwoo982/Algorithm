# 선형큐의 기본 동작

# 큐생성
queue = [0]*3
front = rear = -1   #초기화


# 인큐 enqueue
rear += 1
queue[rear] = 1 #인덱스 0에 1

rear += 1
queue[rear] =2  #인덱스 1에 2

rear += 1
queue[rear] =3  #인덱스 2에 3

# rear = 3은 발생하면 안됨. (예외 rear가 0부터시작한 경우)

# 디큐 dequeue
front += 1
print(queue[front]) #1

front += 1
print(queue[front]) #2

front += 1
print(queue[front]) #3

# 꺼내도 괜찮은지 확인 필요함.
while front != rear:    #큐에 원소가 남아있으면, 비어있지 않으면 동작해라
    front += 1
    t =queue[front]
    if t ==0:
        # 검사하고 꺼내기
        print(t)
        pass