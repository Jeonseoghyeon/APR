def f(N,K):
    if N == K:
        return
    elif N %2:
        print(3*N+1)
        f(3*N+1,K)
    else:
        print(N//2)
        f(N//2,K)


N = int(input())
print(N)
f(N,1)