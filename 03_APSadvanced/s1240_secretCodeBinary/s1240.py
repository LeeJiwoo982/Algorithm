# import sys
# sys.stdin = open('input.txt', 'r')

def find_code(arr):
    '''입력받은 문자열이 요소로 있는 리스트에서 코드를 찾는 함수'''
    code = ''
    for i in range(N):
        if '1' in arr[i]:
            for j in range(M-1, 0, -1):
                if arr[i][j] == '1':
                    code = arr[i][j-55:j+1]
                    break
    return code

def decrypt_code(code):
    '''0과 1로 이루어진 코드를 7개씩 끝어서 8개로 나누고 각각 해석하고 리스트에 넣기'''
    decrypt_rule = {
        '0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
        '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9
    }   #암호 규칙

    decryption = [0]*8
    for i in range(8):  #코드 자르고 해독한거 넣기 총 8개,
        decryption[i] = decrypt_rule[code[i*7:i*7+7]]

    return decryption

def is_correct(code):
    '''코드의 조합이 올바른지 검사'''
    #홀수와 짝수의 합 구하기
    odd_n = even_n = 0
    for i in range(4):
        even_n += code[i*2]   # 짝수
        odd_n += code[i*2+1]

    result = even_n + odd_n
    is_correct_v = even_n*3 + odd_n
    if is_correct_v % 10 == 0:
        return result
    return 0

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]   #코드가 들어있는 배열 입력받기
    #56 길이의 코드 찾기, 끝자리 무조건 1
    code = find_code(arr)

    #56길이의 코드를 7개씩 끊어서
    # 숫자로 변환, 규칙은 swea에 0-9까지 여기까지 str
    # 0-1 코드를 숫자로 변환한 건 int로 리스트에 각 요소로 저장
    decrypt = decrypt_code(code)

    #올바른 코드인지 확인
    #올바른 코드= ((홀수자리 합 * 3)+짝수자리) % 10 == 0
    result = is_correct(decrypt)
    print(f'#{tc} {result}')