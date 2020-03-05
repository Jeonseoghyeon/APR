def goup(n,k):
    if n == k:
        print(1)
        return
    else:
        goup(n-1,k)
        print(n)

x = int(input())
goup(x,1)