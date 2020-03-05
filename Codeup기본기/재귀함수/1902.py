def goup(n,k):
    if n == k:
        print(1)
        return
    else:
        print(n)
        goup(n-1,k)
        
x = int(input())
goup(x,1)