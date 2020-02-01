import sys
sys.stdin = open("View input.txt","r") #읽기전용

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