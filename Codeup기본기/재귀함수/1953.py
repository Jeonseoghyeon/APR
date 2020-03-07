import functools
@functools.lru_cache()
def star(N,K):
    if N == K:
        return
    else:
        star(N-1,K)
        print('*'*N)

N = int(input())
star(N,0)