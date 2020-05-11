import sys
sys.stdin = open("아기상어_input.txt","r")
from collections import deque


dy, dx = [0,0,1,-1],[1,-1,0,0]

def bfs(y,x,cnt,size):
    # 재귀 끝내는 부분
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            print(ny,nx)
            if ARR[ny][nx] == 0:
                bfs(ny,nx,cnt+1,size)
            elif ARR[ny][nx] < size:
                # print(ARR[ny][nx])
                dq.append([ny,nx])
                print(dq)
            else:
                pass
    
    



N = int(input())
ARR = [list(map(int,input().split())) for x in range(N)]
for arr in range(len(ARR)) :
    print(ARR[arr])
    if 9 in ARR[arr]:
        shark = [arr,ARR[arr].index(9)]
y,x = shark
dq = deque()
bfs(y,x,0,2)
        
    