import sys
sys.stdin = open("이진수_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    print("#{}".format(tc))
    N, hex_num = input().split()
    N = int(N)
    y = 8
    result = ''
    for i in hex_num:
        # print((bin(int(i,16)))[2:])
        x = int(i,16)
        for j in range(N):
            print(x & (y >> j))
            # result += str(x & (y >> j))
    print(result)
        