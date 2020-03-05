import functools
@functools.lru_cache()
def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return (fibo(x-2)+fibo(x-1))%10009

x = int(input())
print(fibo(x))