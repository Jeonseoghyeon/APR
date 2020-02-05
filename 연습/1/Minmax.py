import sys
sys.stdin = open("Minmax input.txt","r") 

T = int(input())

for i in range(T):
    N = int(input())
    ains = list(map(int,input().split()))
    max = 0
    for ain in ains:
        if ain >= max:
            max = ain
    min = ains[0]
    for ain in ains:
        if ain <= min:
            min = ain

    print("#{} {}".format(i+1,max-min))
        
