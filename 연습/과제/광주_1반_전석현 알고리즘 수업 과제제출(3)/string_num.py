import sys
sys.stdin = open("string_num_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    str1 = list(map(str,input()))
    str2 = input()
    max_count = count = 0
    for j in str1:
        count = str2.count(j)
        if count>max_count:
            max_count = count
    print('#{} {}'.format(i,max_count))