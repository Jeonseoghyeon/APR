import sys
sys.stdin = open("미로의거리_input.txt","r")

from collections import deque

dx,dy = [0,0,1,-1],[1,-1,0,0]

def bfs(arr,y,x):
    global visited,cnt,result
    visited[y][x] = 1
    dq.append([y,x])
    while dq:
        cnt+=1
        for DQ in range(len(dq)): 
            node_y, node_x = dq.popleft()
            for i in range(4):
                ny = node_y + dy[i]
                nx = node_x + dx[i]
                if 0<=nx<N and 0<=ny<N and visited[ny][nx]==0:
                    if arr[ny][nx] == '0':
                        visited[ny][nx] = 1
                        dq.append([ny,nx])
                    elif arr[ny][nx] == '1':
                        pass
                    elif arr[ny][nx] == '3':
                        result = 1
                        cnt-=1
                        return # 이게 핵심!!!
            

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for ARR in range(N)]
    visited = [[0]*N for VISITED in range(N)]

    for y in range(N):
        for x in range(N):
            if arr[y][x] == '2':
                start_y = y
                start_x = x
    dq = deque()
    cnt = 0
    result = 0
    bfs(arr,start_y,start_x)
    print("#{} {}".format(tc,cnt*result))