from copy import deepcopy

dx,dy = [0,0,1,-1],[1,-1,0,0]

def dfs_normal(y,x,color):
    global normal_cnt
    stack = [[y,x,color]]
    while stack:
        node_y, node_x, color = stack.pop()
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0<=ny<N and 0<=nx<N and visited_normal[ny][nx] == 0:
                if normal_arr[ny][nx] == color:
                    visited_normal[ny][nx] = 1
                    normal_arr[ny][nx] = 0
                    stack.append([ny,nx,color])
    normal_cnt+=1
    return

def dfs_abnormal(y,x,color):
    global abnormal_cnt
    stack = [[y,x,color]]
    if color == 'G' or color == 'R':
        while stack:
            node_y, node_x, color = stack.pop()
            for i in range(4):
                ny = node_y + dy[i]
                nx = node_x + dx[i]
                if 0<=ny<N and 0<=nx<N and visited_abnormal[ny][nx] == 0:
                    if abnormal_arr[ny][nx] == 'G' or abnormal_arr[ny][nx] == 'R':
                        visited_abnormal[ny][nx] = 1
                        abnormal_arr[ny][nx] = 0
                        stack.append([ny,nx,color])
    else:
        while stack:
            node_y, node_x, color = stack.pop()
            for i in range(4):
                ny = node_y + dy[i]
                nx = node_x + dx[i]
                if 0<=ny<N and 0<=nx<N and visited_abnormal[ny][nx] == 0:
                    if abnormal_arr[ny][nx] == color:
                        visited_abnormal[ny][nx] = 1
                        abnormal_arr[ny][nx] = 0
                        stack.append([ny,nx,color])
    abnormal_cnt+=1
    return


N = int(input())
arr = [list(input()) for x in range(N)]

normal_cnt = 0
abnormal_cnt = 0
visited_normal = list([0]*N for x in range(N))
visited_abnormal = list([0]*N for x in range(N))
normal_arr = deepcopy(arr)
abnormal_arr = deepcopy(arr)
for y in range(N):
    for x in range(N):
        if normal_arr[y][x] != 0:
            color = normal_arr[y][x]
            dfs_normal(y,x,color)


for y in range(N):
    for x in range(N):
        if abnormal_arr[y][x] != 0:
            color = abnormal_arr[y][x]
            dfs_abnormal(y,x,color)
print(normal_cnt, abnormal_cnt)