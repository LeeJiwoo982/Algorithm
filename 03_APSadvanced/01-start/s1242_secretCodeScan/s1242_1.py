import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

def hex_to_binary(hex_data):
    '''16진수를 2진수로 변환'''
    binary_str = ""
    match = {
        '0':'0000', '1':'0001', '2':'0010', '3':'0011',
        '4':'0100', '5':'0101', '6':'0110', '7':'0111',
        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
    }
    for i in range(M):
        binary_str += match[hex_data[i]]

    return binary_str

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 배열의 세로크기 가로크기
    data = [list(map(str, input())) for _ in range(N)]  # N 줄에 걸쳐 M개의 16진수숫자가 들어온다.
    
    # 1. 16진수로 주어진 data 2진수로 변환
    binary_data = []
    for i in range(N):
        binary_str = hex_to_binary(data[i])
        binary_data.append(binary_str)

    # 2. 배열에서 암호 코드 찾기
        # binary_data 배열의 전 행과 열 탐색> 같은 행, 같은 열에 또다른 코드가 나올 수 있다.
        # 뒤에서부터 탐색, 1나오면 그때부터 56개 찾아서 code에 넣기
        # 다음 행에서도 동일하게 뒤에서 탐색, code에 있는 코드들과 동일한게 있는지 순회
        # 같다면 pass, 다르면 append
        # 전체를 돌고나면 code 리스트에는 1개 이상의 코드가 들어있음

    code = []   #찾은 코드 저장
    for r in range(N):
        # 암호코드가 있는 경우에만 열을 탐색한다.
        if '1' in binary_data[r]:
            c = M
            while c > 0:    #for문으로 돌기에는... 무리
                if binary_data[r][c] == '1':
                    # 코드 리스트에 없던 경우면 추가한다.
                    if binary_data[r][c - 55:c + 1] not in code:
                        code.append(binary_data[r][c - 55:c + 1])
                        #추가하고 c는
                        c = c - 55
                    c = c - 1

    ##### 고려할 부분 #####
    # 1. 코드의 가로 길이는 56(7*8)의 배로 커지며 그에따라 코드의 비율도 커진다.
    #       그래서 decode dict를 비율로 저장해야 한다. '3211' : 0
    #       비율의 값에 '0'과 '1'을 번갈아 곱한 내용이 코드안에 들어있을것
    # 2. 코드는 행 혹은 열이 중복일 수 있다. 동시에 중복이지는 않음.
    # 3. tc 3을 넘어가면 코드 숫자가 5개가 넘어갈 가능성 있음. 그리고 M은 최대 길이 500
    # 코드 최소길이 56, 2배 112, 3배 168, 4배 ... 8배까지 가능 근데... 8배는 안될듯


    # 3. code의 코드들 정상여부 확인 후, 정상 코드의 숫자의 합을 출력
    # correct = []
    # decode_rule = {
    #     '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    #     '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
    # }  # 암호 규칙
    #
    # decode_rules = {
    #     '3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4,
    #     '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9
    # }  # 암호 비율 규칙. 비율에 곱할 값 = 코드의 길이 // 56
    # 0-1-0-1 순으로 곱한 숫자형태
    
    # decryption = [0] * 8
    # for i in range(8):  # 코드 자르고 해독한거 넣기 총 8개,
    #     decryption[i] = decode_rule[code[i * 7:i * 7 + 7]]

    # print(decryption)

    # '''코드의 조합이 올바른지 검사'''
    # 홀수와 짝수의 합 구하기
    # even = odd = 0
    # odd = sum(decryption[0::2])
    # even = sum(decryption[1:7:2])
    # veri = decryption[-1]
    #
    # result = odd + even + veri
    # is_correct_v = odd * 3 + even + veri
    # if is_correct_v % 10 == 0:
    #     print(result)
    # else:
    #     print(-1)