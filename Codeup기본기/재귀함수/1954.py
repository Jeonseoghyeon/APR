import functools
@functools.lru_cache()
def star(N,K):
    if N == K:
        return
    else:
        print('*'*N)
        star(N-1,K)

N = int(input())
star(N,0)