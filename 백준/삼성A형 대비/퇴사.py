import sys
sys.stdin = open("퇴사.txt","r")

def dfs(start,end,cost):
    global max_cost
    if start + T[start] >= end + 1:
        if start + T[start] == end + 1:
            cost += P[start]
        if cost>max_cost:
            max_cost = cost
        return
    else:
        for i in range(start+T[start],end+1):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i,end,cost+P[start])
                visited[i] = 0

N = int(input())
T = [0]
P = [0]
visit = [0]*(N+1)
for tp in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

max_cost = 0
for i in range(1,len(T)):
    visited = [0] * (N+1)
    visited[i] = 1
    dfs(i,N,0)

print(max_cost)