import sys
sys.stdin = open("rotate_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    times = int(input())
    arr =[]
    print('#{}'.format(i))
    for j in range(times):
        arr += [list(map(int,input().split()))]
    for k in range(len(arr)):
        for q in range(len(arr)-1,-1,-1):
            print(arr[q][k],end ='')
        print(' ',end='')
        for w in range(len(arr)-1,-1,-1):
            print(arr[len(arr)-1-k][w],end='')
        print(' ',end='')
        for e in range(len(arr)):
            print(arr[e][len(arr)-1-k],end='')
        print()