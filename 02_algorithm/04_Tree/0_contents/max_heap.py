def enq(n):
    global last
    last += 1
    heap[last] = n

    #부모의 키값과 비교를 위해서
    c = last
    p = c // 2  #부모정점번호 계산
    while p and heap[p] < heap[c]:
        #부모가 있고, 부모<자식 최대힙조건 위반
        heap[p], heap[c] = heap[c], heap[p]

        #루트까지 비교해야함
        c = p   #부모가 자식
        p = c // 2  #부모의 부모
    
heap = [0]*100
last = 0    #마지막 정점


#인큐
enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(8)

print(heap)