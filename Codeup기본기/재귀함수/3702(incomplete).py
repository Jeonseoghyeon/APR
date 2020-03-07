def stair(N,K):
    global cnt
    if K >= N:
        if K == N:
            cnt+=1
            return
    else:
        stair(N,K+1)
        stair(N,K+2)
        stair(N,K+3)
    return cnt
cnt = 0
print(stair(int(input()),0))

## Memoisation 공부