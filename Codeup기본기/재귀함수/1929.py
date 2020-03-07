def f(N,K):
    if N == K:
        return
    elif N %2:
        f(3*N+1,K)
        print(3*N+1)
    else:    
        f(N//2,K)
        print(N//2)

N = int(input())
f(N,1)
print(N)