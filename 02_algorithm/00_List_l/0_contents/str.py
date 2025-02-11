print(f'{ord("대"):x}')
print(chr(0xb300))

s1 = list(input())  # >> ['글', '자']
s2 = input()    # >> 저장

print(f'{s1}\n{s2}')
print(s1[1])
print(s2[1])

s1[1] = 'c'
print(s1)
# s2[1] = 'c'   #TypeError: 'str' object does not support item assignment, 불변형
