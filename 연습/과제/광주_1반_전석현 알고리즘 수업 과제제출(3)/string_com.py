import sys
sys.stdin = open("string_com_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print("#{} 1".format(i))
    else:
        print("#{} 0".format(i))
