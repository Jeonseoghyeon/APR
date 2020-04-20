from collections import deque
import sys
sys.stdin = open("미로탐색_input.txt","r")

dx,dy = [0,0,1,-1],[1,-1,0,0]
def bfs(y,x):
    global visited, N, M
    visited = list([0]*(M+1) for x in range(N+1))
    visited[1][1] = 1
    cnt = 1
    dq.append([y,x,cnt])
    while dq:
        node_y, node_x, cnt = dq.popleft()
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 1<=ny<N+1 and 1<=nx<M+1 and visited[ny][nx] == 0:
                if arr[ny][nx] == '1':
                    if ny == N and nx == M:
                        return cnt+1
                    visited[ny][nx] = 1
                    dq.append([ny,nx,cnt+1])
                else:
                    pass    

    

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N: 4, M: 6
    arr = [['0']*(M+1)] + [['0']+list(input()) for x in range(N) ]
    
    dq = deque()
    # for i in arr:
    #     print(i)
    print(bfs(1,1))
    visit = arr[:]
    

