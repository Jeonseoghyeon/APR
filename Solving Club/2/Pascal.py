import sys
sys.stdin = open("Pascal input.txt","r")

tc = int(input())

for i in range(tc):
    length = int(input())
    print('#{}'.format(length))
    for j in range(1,length+1):
        if j == 1:
            print('1')
        elif j == 2:
            print('1 1')
        else:
            print('1',end = ' ')
            print("{} ".format(j-1)*(j-2),end ='')
            print('1')

# x 11 / 현석이