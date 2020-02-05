import sys
sys.stdin = open("Metal_stick input.txt","r")

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    start=[]
    for ind,val in enumerate(arr):
        if arr.count(val)==1 and ind%2==0:
            start.append(arr[ind])
            start.append(arr[ind+1])
    while n>1:
        for ind,val in enumerate(arr):
            if start[-1]==val and ind%2==0:
                start.append(arr[ind])
                start.append(arr[ind+1])
        n-=1
    print('#{} '.format(tc),end='')
    for k in start:
        print(k,end=' ')
    print('')

        


