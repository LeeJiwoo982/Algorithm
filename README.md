# Algorithm 
## 알고리즘 푸는 법
### input() 데이터 받는 법
```python
import sys
sys.stdin = open('---.txt', 'r') # .txt파일명은 맞춰서 넣기
```
### input()데이터 로드
#### TestCase와 N(입력값의 크기) 제공 시
```python
T = int(input) #Test_case 수
for tc in range(1, T+1):
    N = int(input())
    # -----코드 입력
    for i in range(N): #문제에 맞춰 변형하기
        # 1차원 배열의 경우
        arr = list(map(int, input().split()))
        #2차원배열의 경우
        arr_2 = [list(map(int, input().split())) for _ range(N)]
        # 두 개의 변수(int형)
        a, b = map(int, input().split())
```
#### T, N 미제공 시
```python
#---바로 코드 입력하기 문제 제대로 읽기~~ 
```
### 출력 양식
- 문제에서 제공하는 출력 양식을 철저히 지킨다.
    - 특히, 출력시 자료형이 어떻게 표현되는지 살펴보기
    - 띄어쓰기 주의