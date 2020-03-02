def three(num,n,k):
    if k==0:
        return num
    else:
        num *= n
        k-=1
        return three(num,n,k)

n,k = list(map(int,input().split()))
print(three(1,n,k))