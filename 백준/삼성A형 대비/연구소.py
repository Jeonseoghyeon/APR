from itertools import combinations

dx,dy = [0,0,1,-1],[1,-1,0,0]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for ARR in range(N)]
cnt_max = 0


def blocking(list):
    global cnt_max
    visit = [[0]*M for VISIT in range(N)]
    arr_new = [i[:] for i in arr]
    for i in list:
        a,b = i
        arr_new[a][b] = 1
 
    for y in range(N):
        for x in range(M):
            if arr_new[y][x] == 2:
                dfs(y,x,arr_new,visit)

    cnt = 0
    for i in range(N):
        cnt+= arr_new[i].count(0)
    
    if cnt>=cnt_max:
        cnt_max = cnt
    
def dfs(y,x,arr_new,visit):
    stack = [[y,x]]
    while stack:
        node_y, node_x = stack.pop()
        for i in range(4):    
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0<=nx<M and 0<=ny<N and arr_new[ny][nx] == 0 and visit[ny][nx] == 0:
                stack.append([ny,nx])
                visit[ny][nx] = 1
                arr_new[ny][nx] = 2
        


# 벽을 세울 수 있는 후보군 찾기
possible_block = []
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            possible_block.append([y,x])

block_3_list = combinations(possible_block,3)

for i in block_3_list:
    blocking(i)

print(cnt_max)
