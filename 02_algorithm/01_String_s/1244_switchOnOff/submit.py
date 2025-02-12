N = int(input())  # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 상태
S = int(input())  # 학생 수

for _ in range(S):
    s, n = map(int, input().split())  # 학생정보 s:성별, n:스위치번호
    if s == 1:  # 남학생의 경우
        for j in range(n - 1, N, n):  # 배수를 찾는 방법은...슬라이싱으로하는게 더 편하다
            switch[j] = 1 - switch[j]

    else:  # 여학생의 경우
        i = n - 1
        l, r = i, i

        while l > 0 and r < N - 1 and switch[l - 1] == switch[r + 1]:
            l -= 1
            r += 1
        for idx in range(l, r + 1):
            switch[idx] = 1 - switch[idx]

# 출력조건
## 스위치 출력은 한 줄에 20개씩, 21번 스위치가 있다면 둘째줄 맨앞으로
# 스위치 결과를 20개씩 끊어서 배열로 저장
# 배열을 출력

for i in range(0, N, 20):
    print(' '.join(map(str, switch[i:i + 20])))