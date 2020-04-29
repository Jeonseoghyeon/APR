import sys
sys.stdin = open("이진수_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, hex_num = input().split()
    result = ''
    for i in hex_num:
        temp = str(bin(int(i,16)))[2:]
        while len(temp)!=4:
            temp = '0'+temp
        result += temp
    print("#{} {}".format(tc,result))