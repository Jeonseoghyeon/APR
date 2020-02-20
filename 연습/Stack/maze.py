import sys
sys.stdin = open("maze_input.txt","r")

tc = int(input())

dx = [-1,0,0,1]
dy = [0,1,-1,0]

def dfs(arr,start):
    stack = []
    stack.append(start)
    visited = [[0]*N for x in range(N)]
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1:
                if arr[nx][ny] == 0 and visited[nx][ny]==0:
                    stack.append([nx,ny])
                    visited[nx][ny] = 1
                if arr[nx][ny] == 3:
                    return 1
    return 0


for i in range(1,tc+1):
    N = int(input())
    arr = []
    for j in range(N): # arr 생성
        arr.append([int(x) for x in input()]) 
    for sx in range(N):
        for sy in range(N):
            if arr[sx][sy] == 2:
                start_x = sx
                start_y = sy
    start = [start_x,start_y]
    print("#{} {}".format(i,dfs(arr,start)))
    
