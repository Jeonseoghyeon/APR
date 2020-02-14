import sys
sys.stdin = open("Maze1_input.txt","r")

dx = [0,1,-1,0]
dy = [1,0,0,-1]

for tc in range(1,11):
    num = int(input())
    arr = [list(map(int,input())) for a_rr in range(16)]
    # for a_r_r in range(len(arr)):
    #     print(arr[a_r_r])
    visited = [[0]*16 for visit_ed in range(16)]
    start = (1,1)
    stack = []
    stack.append(start)
    result = 0
    while stack:
        x,y = stack.pop()
        for dxy in range(4):
            nx = x + dx[dxy]
            ny = y + dy[dxy]
            if arr[nx][ny]==0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append([nx,ny])
            if arr[nx][ny] == 3:
                result = 1
                break
        if result == 1:
            break
    print("#{} {}".format(tc,result))