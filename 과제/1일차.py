# n = 12
# a = [0,0,3,5,2,4,9,0,6,4,0,6,0,0]

# sum = 0
# for i in range(0,len(a)-1,1):
#     if i ==0:
#         pass
#     elif i ==0:
#         pass
#     elif i == len(a):
#         pass
#     elif i == len(a)-1:
#         pass
#     if a[i]>a[i-1] and a[i]>a[i-2] and a[i]>a[i+1] and a[i]>a[i+2]:
#         sum += (a[i] - max(a[i-2],a[i-1],a[i+1],a[i+2]))

# print(sum)

import sys
sys.stdin = open("input1.txt","r") #읽기전용

for i in range(1,11):

    n = input()
    b = input().split()
    a = list(map(int,b))

    sum = 0
    for j in range(0,len(a)-1,1):
        if j ==0:
            pass
        elif j ==0:
            pass
        elif j == len(a):
            pass
        elif j == len(a)-1:
            pass
        if a[j]>a[j-1] and a[j]>a[j-2] and a[j]>a[j+1] and a[j]>a[j+2]:
            sum += (a[j] - max(a[j-2],a[j-1],a[j+1],a[j+2]))


    print(f"#{i} {sum}")