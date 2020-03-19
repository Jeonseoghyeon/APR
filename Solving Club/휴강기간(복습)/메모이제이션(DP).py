# def factorial(N):
#     if N == 1:
#         return 1
#     return N * factorial(N-1)

# print(factorial(5))


#얘를 메모이제이션 헤보자!
def fibo(N):
    if N <=2:
        return 1
    else:
        return fibo(N-1)+fibo(N-2)


memo = [0,1,1] + [0] * 100
def fibo_memo(n):
    if n<=2: return 1
    if memo[n]: return memo[n]
    memo[n] =  fibo_memo(n-1)+fibo_memo(n-2)
    return memo[n]



def fibo_iter(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def fibo2(N):
    f = [0,1]

    for i in range(2,N+1):
        f.append(f[i-1] + f[i-2])
    return f[N]


print(fibo(35))
print(fibo_memo(35))
print(fibo_iter(35))
print(fibo2(35))