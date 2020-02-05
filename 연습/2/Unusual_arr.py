import sys
sys.stdin = open("Unusual_arr_input.txt","r")

tc = int(input())
for i in range(tc):
    a = int(input())
    x = list(map(int,input().split()))
    x_s = sorted(x)
    print("#{}".format(i+1), end= ' ')
    for j in range(5):
        if j == 4:
            print(x_s[-j-1],end = ' ')
            print(x_s[j],end=' ')     
        else:
            print(x_s[-j-1],end = ' ')
            print(x_s[j],end=' ')
    print()
        
    