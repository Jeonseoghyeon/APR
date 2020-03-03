import sys
sys.stdin = open("square_input.txt","r")

T = int(input())
dx,dy = [0,1,0,-1],[1,0,-1,0]
def bfs(start):
    global max_room
    stack = [start]
    cnt = 1
    
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N :
                if arr[nx][ny] == arr[x][y] +1:
                    stack.append([nx,ny])
                    cnt+=1
                    break
    return cnt
    
for i in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for x in range(N)]
    max_room = 0
    max_room_num = 100000
    for x in range(N):
        for y in range(N):
            if bfs([x,y]) > max_room:
                max_room = bfs([x,y])
                max_room_num = arr[x][y]
            elif bfs([x,y]) == max_room:
                max_room = bfs([x,y])
                if arr[x][y] < max_room_num:
                    max_room_num = arr[x][y]
    
    print("#{} {} {}".format(i,max_room_num,max_room))
