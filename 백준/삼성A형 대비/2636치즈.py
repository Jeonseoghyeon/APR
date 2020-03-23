from copy import deepcopy
dx,dy = [0,0,1,-1],[1,-1,0,0]

def dfs_air(y,x):
    visit = deepcopy(visited)
    stack = [[y,x]]
    while stack:
        node_y, node_x = stack.pop()
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0<=nx<M and 0<=ny<N and visit[ny][nx] == 0:
                if arr[ny][nx] != '1':
                    visit[ny][nx] = 1
                    stack.append([ny,nx])
                    arr[ny][nx] = '2'
                
def threetotwo():
    for y in range(N):
        for x in range(M):
            if arr[y][x] == '3':
                arr[y][x] = '2'

def ifall2(arr):
    cnt2 = 0
    for i in arr:
        cnt2+=i.count('2')
    if cnt2 == M*N:
        return 1
    else:
        return 0
        
def cheese(arr):
    cnt1 = 0
    for i in arr:
        cnt1+=i.count('1')
    return cnt1

N,M = map(int,input().split()) # N 세로 13/ M 가로 12
arr = [list(input().split()) for ARR in range(N)]
visited = [[0]*M for VISIT in range(N)]
cnt = 0
dfs_air(0,0)
while True:  
    remain_cheese = cheese(arr)
    cnt +=1
    for y in range(N):
        for x in range(M):
            if arr[y][x] == '1':
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=nx<M and 0<=ny<N:
                        if arr[ny][nx] == '2':
                            arr[y][x] = '3'
    # print(cnt)
    # for adsad in range(N):
    #     print(arr[adsad])
    # print()
    # print()
    dfs_air(0,0)
    threetotwo()
    # for adsad in range(N):
    #     print(arr[adsad])
    if ifall2(arr) ==1:
        break
    

print(cnt)
print(remain_cheese)
