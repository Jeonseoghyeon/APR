dx,dy = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

def find_star(y,x):
    global star_map, cnt
    stack = [[y,x]]
    while stack:
        node_y,node_x = stack.pop()
        for i in range(8):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0<=ny<10 and 0<=nx<10 and star_map[ny][nx] == 1:
                stack.append([ny,nx])
                star_map[ny][nx] = 0

    cnt+=1


T = int(input())
for tc in range(1,T+1):
    star_map = [list(map(int,input().split())) for STAR in range(10)]
    cnt = 0
    for y in range(10):
        for x in range(10):
            if star_map[y][x] == 1:
                find_star(y,x)
    print("#{} {}".format(tc,cnt))