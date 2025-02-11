import sys
sys.stdin = open('GNS_test_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    input()
    words = input().split()
    arr = []
    nums = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for n in words:
        if n in list(nums.keys()):
            nums[n] += 1

    # for i in range(nums["ZRO"]):
    #     arr.append("ZRO")
    # for i in range(nums["ONE"]):
    #     arr.append("ONE")
    # for i in range(nums["TWO"]):
    #     arr.append("TWO")
    # for i in range(nums["THR"]):
    #     arr.append("THR")
    # for i in range(nums["FOR"]):
    #     arr.append("FOR")
    # for i in range(nums["FIV"]):
    #     arr.append("FIV")
    # for i in range(nums["SIX"]):
    #     arr.append("SIX")
    # for i in range(nums["SVN"]):
    #     arr.append("SVN")
    # for i in range(nums["EGT"]):
    #     arr.append("EGT")
    # for i in range(nums["NIN"]):
    #     arr.append("NIN")
    # print(f'#{tc}')
    # arr = ' '.join(map(str, arr))
    # print(arr)

    ans = "ZRO"*nums["ZRO"], "ONE"*nums["ONE"], "TWO"*nums["TWO"], "THR"*nums["THR"], "FOR"*nums["FOR"], "FIV"*nums["FIV"], "SIX"*nums["SIX"], "SVN"*nums["SVN"], "EGT"*nums["EGT"], "NIN"*nums["NIN"]
    print(ans)