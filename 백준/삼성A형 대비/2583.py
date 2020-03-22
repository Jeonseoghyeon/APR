dx, dy = [0,0,1,-1],[1,-1,0,0]
def dfs(x,y,visit):
    global cnt,cnt_list
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=nx<N and 0<=ny<M and arr[ny][nx] == 0:
            cnt = 0
            break
    if cnt == 0:
        stack = [[dfs_y,dfs_x]]
        while stack:
            node_y,node_x = stack.pop()
            for i in range(4):
                ny = node_y + dy[i]
                nx = node_x + dx[i]
                if 0<=nx<N and 0<=ny<M and visit[ny][nx] == 0 and arr[ny][nx] == 0:
                    visit[ny][nx] = 1
                    arr[ny][nx] = 2
                    stack.append([ny,nx])
                    cnt+=1
    cnt_list.append(cnt)

M,N,K = map(int,input().split()) # 5, 7, 3
arr = [[0]*(N) for ARR in range(M)]
visit = [[0]*(N) for ARR in range(M)]
for i in range(K):
    s1,s2,s3,s4 = list(map(int,input().split()))
    for y in range(M-s4,M-s2):
        for x in range(s1,s3):
            arr[y][x] = 1

cnt_list = []
for dfs_y in range(M):
    for dfs_x in range(N):
        cnt = 1
        if arr[dfs_y][dfs_x] == 0:
            dfs(dfs_x,dfs_y,visit)
print(len(cnt_list))

results = sorted(cnt_list)
for result in results:
    print(result,end=' ')