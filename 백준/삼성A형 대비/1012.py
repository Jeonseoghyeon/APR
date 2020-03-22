import sys
sys.stdin = open("1012_input.txt","r")

dx,dy = [0,0,1,-1],[1,-1,0,0]

def dfs(y,x):
    global arr,cnt
    cnt+=1
    stack = [[sero,garo]]
    while stack:
        node_y, node_x = stack.pop()
        for i in range(4):
            nx = node_x +dx[i]
            ny = node_y +dy[i]
            if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 1:
                stack.append([ny,nx])
                arr[ny][nx] = 0

T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split()) # 가로, 세로, 배추 개수
    arr = [[0]*M for ARR in range(N)]
    cnt = 0
    for i in range(K):
        x,y = map(int,input().split())
        arr[y][x] = 1
    # for i in range(N):
    #     print(arr[i])
    
    for sero in range(N):
        for garo in range(M):
            if arr[sero][garo] == 1:
                dfs(sero,garo)
    print(cnt)