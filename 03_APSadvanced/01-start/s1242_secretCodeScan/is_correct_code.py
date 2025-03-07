code = '01110110110001011101101100010110001000110100100110111011'


'''0과 1로 이루어진 코드를 7개씩 8개로 나누고 각각 해석하고 리스트에 넣기'''
decrypt_rule = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}  # 암호 규칙

decryption = [0] * 8
for i in range(8):  # 코드 자르고 해독한거 넣기 총 8개,
    decryption[i] = decrypt_rule[code[i * 7:i * 7 + 7]]

print(decryption)

#'''코드의 조합이 올바른지 검사'''
# 홀수와 짝수의 합 구하기
even = odd = 0
odd = sum(decryption[0::2])
even = sum(decryption[1:7:2])
veri = decryption[-1]

result = odd + even + veri
is_correct_v = odd * 3 + even + veri
if is_correct_v % 10 == 0:
    print(result)
else:
    print(-1)