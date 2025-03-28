# 퀵 정렬
## 모든 숫자를 한 번에 정렬하는 것은 어렵지만
## 딱 한 숫자만 정렬된 위치에 놓는 것은 쉽다
## >> O(N)

```python
arr = [5, 8, 1, 7, 3, 4, 2, 9]
'''
swap (1, 6)
[5, 2, 1, 7, 3, 4, 8, 9]
swap (3, 5)
[5, 2, 1, 4, 3, 7, 8, 9]
swap (5, 4) #크로스 발생해서 끝남
[5, 2, 1, 4, 3, 7, 8, 9]    

swap (0, 4)
[3, 2, 1, 4, 5, 7, 8, 9]

# i = 7, j = 3
# 5랑 3의 위치를 바꾸면 정렬된 위치 완성
'''
    
pivot = arr[0]  #0번 인덱스를 기준점으로 삼는다.
i = 0   # left pointer
j = len(arr) - 1    # right pointer

# i, j dont cross
while i < j:
    while arr[i] <= pivot:   #i는 pivot보다 큰 수 를 찾아야 한다. 작은 수는 건너뜀
        i += 1
    # while문을 빠져 나온 경우 = i는 pivot보다 큰 수를 가리킴
    
    while arr[j] > pivot:   #pivot보다 작은 수를 찾아야 하므로 피봇보다 큰 수 발견시 건너뜀
        j -= 1
    # while문을 빠져나오면 j는 피봇보다 작은 수를 가리킴
    
    if i < j: #둘의 크기가 역전되지 않을 때
        arr[i], arr[j] = arr[j], arr[i]
    print(f'swap ({i}, {j})')
    print(arr)
    

    #pivot을 정렬된 위치로 놓기
    # 0번째 j번째 바꾸기
arr[0], arr[j] = arr[j], arr[0]
print(arr)

```

 arr의 가장 첫 번째 원소 5는

 만약 arr이 정렬 완료되었을 때 몇 번째에 있을까?
 

정렬된 위치: 정렬되었을 때 해당 원소의 위치
> 기준점을 정렬된 위치로 놓으면서 
> 
> + 왼쪽에는 기준점보다 작은 수들만
> 
> + 오른쪽에는 기준점보다 큰 수만 오도록


정렬된 위치 찾기

왼쪽i, 오른쪽 j 포인터 사용

왼쪽에서는 기준보다 큰 것

오른쪽에서는 기준보다 작은 것 찾기


[기준점보다 작은 수, 기준점, 기준점보다 큰 수]

왼, 오는 정렬될 필요는 없음


#### 최악의 경우: 역순인 배열일 때      O(N**2)
#### 평균적으로는                      theta(NlogN)