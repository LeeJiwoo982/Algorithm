# 1. 큐

- **선입선출**
    - 뒤에서 삽입, 앞에서 삭제
    - inQueue 먼저 저장된 애를 꺼낸다.
- 먼저 들어온 Front
    - 저장된 원소 중 첫 번째 원소, 삭제된 위치
- 마지막에 들어온 Rear
    - 저장된 원소 중 마지막 =스택의 top

## 0) 기본 연산

| **연산** | **기능** |
| --- | --- |
| **`enqueue(item)`** | 뒤쪽(rear 다음)에 원소 삽입 |
| **`dequeue()`** | 앞쪽(front)에 원소 삭제 후 반환 |
| **`createqueue()`** | 공백 상태의 큐 생성 |
| **`isempty()`** | 큐가 공백인지 확인 |
| **`isfull()`** | 큐가 포화상태인지 확인 |
| **`qpeek()`** | 앞쪽(front)에서 원소 삭제 없이 반환 |
- 삽입: enqueue
- 삭제: dequeue

### ↔ 스택

- Last in First out: 마지막 저장된 걸 먼저 나간다
- top

## 1) 선형 큐

- 1차원
    - 큐의 크기=배열 크기
    - front=첫번째 원소 인덱스, rear: 마지막 원소의 인덱스
- 상태 표현
    - 초기 상태: `front=rear=-1`
    - 공백 상태: `front==rear`
    - 포화 상태: `rear == n-1` (n: 배열크기, n-1: 배열 마지막 인덱스)
- 삽입
    
```python
def enQueue(item):
    global rear
    if isFull(): print("Queue_Full") # 큐가 꽉차면 문제있음, 너무 작은 용량 or 너무 많이 삽입
    else:
    	rear += 1
    	Q[rear] = item
```
    
- 삭제
    
```python
def deQueue():
    if (isEmpty()) then Queue_Empty():
    else:
        front += 1
        return Q[front]
```
    
- 공백 상태 포화 상태 검사
    
```python
def isEmpty():
    return front == rear
    
def isFull():
    return rear == len(Q) - 1
```
    
- 검색
    
```python
def Qpeek():
    if isEmpty(): print("Queue_Empty")
    else: return Q[front+1]
```
    
    > 1) 세 개의 데이터 1, 2, 3 차례로 큐에 삽입
    2) 큐에서 세 개의 데이터를 차례로 꺼내서 출력
    >>> 1, 2, 3 순  #my_queue
    > 
    

### 스택과 큐의 차이

- 스택은 진행한 순서, 과정. 과거를 기억하기-
- 큐는 접수창구
- 스택과 큐는 마음대로 꺼낼 수 있지

### 선형큐의 문제

삽입 삭제 계속하면 앞부분 공간이 죽어버리고 삽입 수행이 멈춤

### 해결1

- 연산시마다 저장된 원소들 배열 앞부분으로 이동. 시간효율성 저하

### 해결2: 원형큐

> 원형큐 목차에서 계속…
> 

## 2) 원형큐 cQ

- cctv와 같이 오래된 기록을 덮어쓰면서 되돌아 오는 구조, 규칙이라
- 완전한 형태는 아니다. 먼 과거를 알 수 없음
- 콘솔도 같은 자료구조: 콘솔의 크기 1mb인데 붙여넣기한 내용이 1mb를 넘어가면 마지막에 넣은 내용이 나옴. 사이클버퍼
- full일 때 새로들어온걸 버릴지 오래된걸 버릴지의 선택
- 1차원 배열을 논리적으로 첨 끝을 연결해서 원형으로 이룬다 가정해서 사용
- 초기 공백 상태 : front=rear=0
- 순환
    - front, rear 위치가 배열 마지막 인덱스 n-1을 가리킨 후 그 다음에는 처음 인덱스 0으로 이동
    - 나머지 연산자 `mod` 를 사용
- front: 공백과 포화 상태를 구분쉬우려고 front 자리 사용안하고 빈자리로
- 

|  | **삽입 위치** | **삭제 위치** |
| --- | --- | --- |
| **선형큐** | **`rear += 1`** | **`front +=1`** |
| **원형큐** | **`rear = (rear+1) mod n`** | **`front = (front + 1) mod n`** |

1. create queue
    1. queue = [0]*N
    2. front =rear=0
2. enqueue(A)
    1. rear += 1   #1
    2. queue[rear] = A
3. enqueue(B)
    1. rear += 2     #2
4. dequque()
    1. front+=1
5. enqueue(C)
    1. rear += 1   #3
6. enqueue(D)
    1. queue full
    2. rear = 0
    3. front를 비워두고 쓴다. 
7. full의 조건
    1. (rear+1=4) % N == front >> full

```python
def isEmpty():
	return front == rear
def isFull():
 return (rear + 1) % len(cQ) == front
 
# 삽입
def enqueue(item):
	if isFull():
		print('Queue_Full") #디버깅용
	else:
		rear = (rear+1)%len(cQ)
		cQ[rear] = item
#삭제
def deQueue():
	if isEmpty():
		print("queue_empty")
	else:
		front = (front+1)%len(cQ)
		return cQ[front]
```

## 3) 연결큐 linked list

- 큐의 원소: 노드
- 큐의 원소 순서: 노드의 연결 순서, 링크로 연결
- front : 첫 번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크
- 삽입삭제가 매우 빠름
    - append() 는 복사해서 붙이는 것
- 상태표현
    - 초기 상태 : front = rear = null
    - 공백 상태 : front = rear = null
1. createLinkedQueue():
2. enQueue(A)
    1. front = 0x1000, rear = 0x1000
    - 동적할당
3. enQueue(B)
    1. front = 0x1000
    2. rear = 0x1008
4. deQueue()
    1. front = 0x1008
    2. rear = 0x1008
5. enQueue(C)
    1. front = 0x1000
    2. rear = 0x1010
    3. 

## 4) [참고] 우선순위 큐 Priority Queue

- 우선순위를 가진 항목들을 저장
- FIFO 순이 아닌 우선순위가 높은 순서대로 먼저 나감
- ex) 시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제 테스크 스케줄링
- 문제점: 삽입삭제 시 원소 재배치 발생, 소요시간, 메모리낭비 큼.>> 트리구조

# 2. 큐의 활용

## 1) 버퍼 Buffer

- 전송하는 동안 일시적으로 데이터를 보관하는 메모리의 영역
- 버퍼링:
    - 버퍼를 활용하는 방식
    - 버퍼를 채우는 동작
- 자료구조
    - 입출력, 네트워크와 관련된 기능
    - 입력-출력-전달 이라 **큐**가 활용
- 예시
    - 키보드 입력 → 키보드 입력 버퍼 → 키입버에 Enter 키 입력 in → 프로그램 실행에 먼저 들어온 순서로 입력되서 연