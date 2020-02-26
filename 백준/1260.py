N,M,V = list(map(int,input().split()))
arr = [[0]*(N+1) for ar in range(N+1)]
visit = [[0]*(N+1) for ar in range(N+1)]

for i in range(M):
    x,y = list(map(int,input().split()))
    arr[x][y] = 1
    # arr[y][x] = 1
for arrr in range(N+1):
    print(arr[arrr])

stack = [V]
while stack:
    node = stack.pop()
    print(node)
    for k in range(1,N+1):
        if arr[node][k] == 1 and visit[node][k]==0:
            stack.append(k)
            visit[node][k]=1
    print(stack)
            


