'''
3
1 2 3
4 5 6
7 8 9
'''
# 인풋받은 정보 배열로
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # print(f'인풋받은 2차원 배열 받아오기: {arr}')
# for i in range(N):
#     for j in range(N):
        # print(arr[i][j])
        # 2차원 배열에 접근하는 가장 기본

# 비어있는 2차원 배열 만들기
arr2 = [[0]*4 for _ in range(3)]
# print(f'0으로 채워진 2차원 배열 만들기: {arr2}')

# 이렇게는 만들지 말아야 함
arr3 = [[0]*4] * 3
## 만들어는 짐
arr3[2][1] =1
# print(arr3) # 얕은 복사와 같은 경우. 참조를 반복해라로 만들어짐. 그래서 하나 바꾸면 다 바뀌어 버림
# 2차원은 좀더 섬세하게.

# 행은 i-r-p, 열은 j-c-q // x,y는 실제 그래프 개념을 보면 y가 행이고 x가 열이라 헷갈릴 수 있다.

# N*M 배열의 크기와 저장된 값이 주어질 때의 합구하기
'''
3 4
1 7 2 8
6 2 9 3
5 7 4 2
'''
K, M = map(int, input().split())
arr4 = [list(map(int, input().split())) for _ in range(K)]
s = 0
for i in range(K):
    for j in range(M):
        s += arr4[i][j]
print(f'N*M 이차원배열 값들의 합: {s}')
# 뭔가 문제군

# 열 우선 순회
# for j in range(m):
#     for i in range(n):
#         f(array[i][j])

## 지그재그 순회
# for i in range(n):
#     for j in range(m):
#         f(array[i[j + (m-1-2*j) * (i%2)])  #i가 짝수면 열이 j가 됨.
# i가 홀수면 i%2 -> 1>> m-1-j 이 되서 뒤부터 진행
# i가 짝수면 i%2 -> 0>> (m-1-2j)가 없어짐. 열이 j가 됨.=왼>오

# for i in range(n):
#   if i%2 ==0:
#       for j in range(m):
#   else:
#       for j in range(m-1,-1,-1):

#>>대각선을 지그재그로 하는 알고리즘=> 이미지 처리에서 사용. 함수가 있기는 하지만 원리 이해


## 델