def my_bin(n,k,i):
    if i == 1 and n == 0:
        print(0)
        return
    if n<k:
        if n == 1:
            return n
        else:
            return n
    else:
        i+=1
        my_bin(n//2,k,i)
        print(n%2,end='')

n = int(input())
my_bin(n,1,1)