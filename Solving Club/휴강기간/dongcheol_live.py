import sys
import functools
sys.stdin = open('dongcheol_input.txt','r')

@functools.lru_cache()
def f(n,k,s):
    global maxV,u,w,p
    if n == k:
        if(maxV<s*100):
            maxV = s*100
    elif (maxV >= s*100):
        return
    else:
        for i in range(k):
            if(u[i]==0):
                u[i]=1
                f(n+1,k,s*P[i][n]/100)
                u[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = [list(map(int,input().split())) for i in range(N)]
    u = [0]*N
    w = [0]*N
    maxV = 0
    f(0,N,1)
    
    print('#{} {:.6f}'.format(tc,maxV))