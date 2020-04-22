import sys
sys.stdin = open("퇴사.txt","r")

def dfs(start,end,cost):
    global N, max_cost
    if start+T[start]>N+1:
        if cost > max_cost:
            max_cost = cost
        return
    else:
        for i in range(start,end+1):
            if visit[i]==0 and i+T[i] <end+1:
                visit[i]=1
                dfs(i+T[i],end,cost+P[i])
                visit[i]=0

N = int(input())
T = [0]
P = [0]
visit = [0]*(N+1)
for tp in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
max_cost = 0
dfs(1,N,0)

print(max_cost)