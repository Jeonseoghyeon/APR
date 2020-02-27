def dfs (start,visit):
    visit.append(start)
    for i in range(N+1):
        if arr[start][i] == 1 and i not in visit:
            visit = dfs(i,visit)
    return visit

def bfs (start):
    queue = [start]
    visit = [start]
    while queue:
        c = queue.pop(0)
        for i in range(N+1):
            if arr[c][i] and i not in visit:
                visit.append(i)
                queue.append(i)
    return visit




N,M,V = list(map(int,input().split()))
arr = [[0]*(N+1) for ar in range(N+1)]
# visit = [[0]*(N+1) for ar in range(N+1)]

for i in range(M):
    x,y = list(map(int,input().split()))
    arr[x][y] = 1
    arr[y][x] = 1
# for arrr in range(N+1):
#     print(arr[arrr])

start =[V]

print(*dfs(V,[]))
print(*bfs(V))


