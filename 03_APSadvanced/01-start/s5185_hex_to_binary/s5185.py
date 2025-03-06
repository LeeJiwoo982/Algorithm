import sys
sys.stdin = open("sample_input.txt", "r")

def hex_to_binary(hex_str):
    '''16진수를 2진수로 변환'''
    result = ""
    binary = {
        '0':'0000', '1':'0001', '2':'0010', '3':'0011',
        '4':'0100', '5':'0101', '6':'0110', '7':'0111',
        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
    }
    for i in hex_str:
        result += binary[i]

    return result

T = int(input())
for tc in range(1, T+1):
    N, hex_str = input().split()     # 자리수 N, 16진수

    result = hex_to_binary(hex_str)
    print(f'#{tc} {result}')