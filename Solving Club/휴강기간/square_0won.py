from collections import deque
import sys
sys.stdin = open("square_input.txt","r")



dx = [0,0,-1,1]
dy = [-1,1,0,0]
 
def bfs(i, j):
    q = deque()
    visited = [[0]*N for z in range(N)]
    q.append((i, j))
    visited[i][j] = 1
    cnt = 0
 
    while q:
        cnt += 1
        for k in range(len(q)):
            x, y = q.pop()
            for l in range(len(dx)):
                mx = x+dx[l]
                my = y+dy[l]
                if mx<0 or mx>=N or my<0 or my>=N:
                    continue
                if frame[mx][my] == frame[x][y]+1 and visited[mx][my]==0:
                    visited[mx][my]=1
                    q.append((mx,my))
    return cnt
 
 
T = int(input())
 
for ts in range(1, T+1):
    max_cnt = -2147000000
    point = 2147000000
    N = int(input())
    frame = [[] for z in range(N)]
 
 
    for i in range(N):
        frame[i] = list(map(int, input().split()))
 
    for i in range(N):
        for j in range(N):
            tmp_cnt = bfs(i, j)
             
            if tmp_cnt > max_cnt:
                max_cnt = tmp_cnt
                point = frame[i][j]
            elif tmp_cnt == max_cnt and point > frame[i][j]:
                point = frame[i][j]
     
    print('#%d'%ts, point, max_cnt)