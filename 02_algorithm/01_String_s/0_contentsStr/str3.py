s1 = 'abc'
s2 = 'ab'
s3 = 'abc'
s4 = s2 +'c'
print(s1==s3)       #True
print(s1 is s3)     #True
print(s1==s4)       #True   같은 모양인가?
print(s1 is s4)     #False  같은 메모리 위치인가?

s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
s4 = 'AC'
s5 = 'abc'
s6 = ' ab'
def my_strcmp(s1, s2):
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

print(my_strcmp(s1, s2))    # 0 같다.
print(my_strcmp(s1, s3))    # -1 s3이 크다
print(my_strcmp(s3, s4))    # 1 s3이 크다
print(ord('a'), ord('A'))   # 97, 65
print(my_strcmp(s1, s6))