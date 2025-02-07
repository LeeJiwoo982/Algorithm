#모든 부분집합의 요소의 합
# 길이가 고정된 경우
a = [1,2,3]
bit = [0]*3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2]= k
            # print(bit)
            #집합으로 표현하기 과정
            s=0
            for b in range(3):
                if bit[b]:
                    print(a[b], end = ' ')
                    s += a[b]
            print(bit, s)