import sys
sys.stdin = open("미로의거리_input.txt","r")

from collections import deque

dx,dy = [0,0,1,-1],[1,-1,0,0]

def bfs(arr,y,x):
    global visited
    visited[y][x] = 1
    dq.append([y,x,0]) # cnt 세주는 부분을 이렇게 바꿈
    while dq:
        node_y, node_x,cnt = dq.popleft()
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx]==0:
                if arr[ny][nx] == '0':
                    visited[ny][nx] = 1
                    dq.append([ny,nx,cnt+1]) # cnt 세주는 부분을 이렇게 바꿈
                    # 해당 Depth의 모든 값들에 대해 동일한 cnt가 들어감.
                elif arr[ny][nx] == '3':
                    return cnt  # 중요 !! cnt 리턴하고 함수 종료
    return 0  # 3이 없으면 0을 리턴하고 함수 종료 !!!

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
    result = bfs(arr,start_y,start_x)
    
    print("#{} {}".format(tc,result))