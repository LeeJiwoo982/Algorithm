# List 1 | 1차원배열
## 1차원 배열 입력
### 공백을 두고 입력
`arr = list(map(int, input().split()))`
## 정렬 = 크기 순으로 재배열
- 오름차순(ascending): 작은 값>큰 값
- 내림차순(descending): 반대
### Bubble Sort 버블
인접한 두 개의 원소를 비교하여 자리를 계속 교환
#### 과정
- 첫 번째 원소부터 인접 원소와 비교 후 교환
- 맨마지막 자리까지 이동
- 한 단계(1 pass) 끝나면 가장 큰 원소가 마지막 자리로
- (N-1)단계 후에 최종 정렬 완성
- O(N^2)
- 1pass 지나면 가장 끝 원소가 최댓값
> 1pass => 1개의 원소 정렬

### Counting Sort 카운팅


### Selection Sort 선택