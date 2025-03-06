target = 74

def dec_to_binary(target):
    '''10진수를 2진수로 변환하는 함수'''
    binary_number = ""

    while target>0:
        remain = target % 2 #2로 나눈 나머지
        binary_number = str(remain) + binary_number
        target = target // 2    #변환한 거 제외하고 계산
    print(binary_number)

dec_to_binary(target)

binary_str = "1001010"
def binary_to_def(binary_str):
    '''이진수를 10진수로 변환하기'''
    # 1)binary_str 문자열 뒤에서 부터 진행
    # 2)각 자리에 맞는 수를 곱하며 결과에 더한다.
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == "1":
            decimal_number += 2 ** pow  #10진수 결과에 2의 pow제곱을 더한다.
        pow += 1    # 길이만큼 증가
    print(decimal_number)
binary_to_def(binary_str)

# 16진수 <-> 2진수 변환 외우면 좋다

# 10진수 -> 16진수
def decimal_to_hexadecimal(target):
    hex_digit = '0123456789ABCDEF'
    # hex_digit[10] => A
    hexadecimal_number = ""

    while target>0:
        remain = target % 16
        hexadecimal_number = hex_digit[remain] + hexadecimal_number
        target //= 16
    print(hexadecimal_number)

decimal_to_hexadecimal(256)
