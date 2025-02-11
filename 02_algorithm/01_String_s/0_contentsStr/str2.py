s1 = 'ab'*6
print(s1)
s = ['a', 'b', 'c']
print('.'.join(s))
print()

print('배열로 나눠서 인덱스로 접근해서 문자열 뒤집기')
txt = list(input())
N = len(txt)
for i in range(N//2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
print(txt)
a = ''.join(txt)
print(a)
print()

print('파이썬의 문자열 뒤집기-2')
s = 'string'
s = s[::-1]
print(s, type(s))
print()

print('sort(reverse=True) 이해하기')
s_lst = list(s)
s_lst.reverse()
print(s_lst)
print(''.join(s_lst))