# print(f'{ord("대"):x}')
# print(chr(0xb300))
#
# # list를 씌우면 글자 하나하나 분리해서 저장, 그냥 input은 통 '저장'으로 저장됨
# s1 = list(input())  # >> ['글', '자']
# s2 = input()    # >> 저장
#
# print(f'{s1}\n{s2}')
# print(s1[1])
# print(s2[1])
#
# # 리스트로 저장하면 변경 가능 문자열은 변경 불가능
# s1[1] = 'c'
# print(s1)
# # s2[1] = 'c'   #TypeError: 'str' object does not support item assignment, 불변형

#
# p = {'naem':'alse', 'gae':23}
# print(p.setdefault('con'))
# print(p)

s = {1,4,6,2}
print(s.discard(4))
print(s)