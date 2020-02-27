from copy import deepcopy
from itertools import combinations

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def safe_zone(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                cnt+=1
    return cnt

def bfs(wall,start):
    new_arr = deepcopy(arr)
    new_start = deepcopy(start)
    for i,j in wall:
        new_arr[i][j] = 1

    while new_start:
        y,x = new_start.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<M and 0<=ny<N:
                if new_arr[ny][nx] == 0:
                    new_arr[ny][nx] = 2
                    new_start.append([ny,nx])
    return safe_zone(new_arr)
    
                


N,M = list(map(int,input().split()))
arr = [list(map(int,input().split())) for x in range(N)]
# for ar_r in range(N):
#     print(arr[ar_r])

start = []
safe = []
for y in range(N):
    for x in range(M):
        if arr[y][x] == 2:
            start.append([y,x])
        elif arr[y][x] == 0:
            safe.append([y,x])
safe = list(map(list,combinations(safe,3)))
max_cnt = 0
for i in safe:
    if bfs(i,start) >=max_cnt:
        max_cnt = bfs(i,start)
print(max_cnt)


