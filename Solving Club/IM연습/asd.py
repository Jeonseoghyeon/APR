dx, dy = [0,0,-1,1], [-1,1,0,0]
 
def dfs(start_node):
    visit = [[0]*16 for i in range(16)] # 방문한 곳
    stack = list() # 다음 탐색할 노드
 
    stack.append(start_node)
 
    while stack:
        x,y = stack.pop()
        if visit[y][x]==0:
            visit[y][x] = 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if arr[ny][nx] == '3':
                    return 1
                if arr[ny][nx] == '0' and visit[ny][nx]==0:
                    stack.append([ny, nx])
    return 0
 
for t in range(1,11):
    input()
    arr = [list(input()) for i in range(16)]
    print('#{} {}'.format(t, dfs([1,1])))