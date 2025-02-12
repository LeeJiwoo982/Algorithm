t = "TTTTTTATTAATA"
p = "TTA"
def bruteFroce(t,p):
    i = j = 0
    N = len(t)
    M = len(p)
    while i<N and j <M:
        if t[i] != p[j]:    #텍스트와 패턴이 다른지 비교하겠음
            i = i - j + 1   # i-j 비교를 시작했던 위치
            j=0
        else:               #같으면
            i += 1
            j += 1
    if j == M:
        return i -j
    else:
        return -1

def pattern_cnt(t,p):
    '''패턴의 등장 횟수 찾기'''
    i = j = 0
    N = len(t)
    M = len(p)
    cnt=0
    while i<N:
        if t[i] != p[j]:    #텍스트와 패턴이 다른지 비교하겠음
            i = i - j + 1   # i-j 비교를 시작했던 위치
            j=0
        else:               #같으면
            i += 1
            j += 1
        if j == M: #패턴을 찾은 경우
            cnt += 1
            i=i-j+1
            j = 0



t= 'This is a book~!'
p ='is'

print(bruteFroce(t,p))
print(pattern_cnt(t,p))
