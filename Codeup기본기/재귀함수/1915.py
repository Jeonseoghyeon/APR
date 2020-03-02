from sys import setrecursionlimit
setrecursionlimit(1000000000)

def fibo(x):
    if x <=2:
        return 1
    else:
        return fibo(x-2)+fibo(x-1)
    
print(fibo(int(input())))
