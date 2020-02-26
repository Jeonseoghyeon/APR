import sys
sys.stdin = open("password_input.txt","r")


for t in range(1,11):
    input()
    arr = list(map(int,input().split()))
    while 0 not in arr:
        for i in range(1,6):
            x = arr.pop(0)-i
            if x<=0:
                arr.append(0)
                break
            arr.append(x)
    print("#{}".format(t),end= ' ')
    for j in range(8):
        print(arr[j],end=' ')
    print()
