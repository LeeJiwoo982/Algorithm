import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    text = input()
    found = False

    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        for j in range(pattern_len):
            if text[i + j] != pattern[j]:
                break
        else:  # for문 안에서 break안 만났을때
            found = True
            break

    result = 1 if found else 0
    print(f'#{tc} {result}')