import sys
from copy import deepcopy
sys.stdin = open('minmove_input.txt','r')

dx = [0,1,1,0,-1,-1]
dy = [-1,0,1,1,0,-1]

def bfs(lst):
    visited = deepcopy(visit)
    visited[lst[0]][lst[1]] = 1
    stack = [lst]
    bfs_list = []
    while [1,4] not in stack:
        nodey,nodex = stack.pop()
        for i in range(6):
            ny = nodey + dy[i]
            nx = nodex + dx[i]
            if 0<ny<H+1 and 0<nx<W+1:
                if visited[ny][nx]==0:
                    visited[ny][nx] = 1
                    stack.insert(0,[ny,nx])
                    print(stack)
    return
            

T = int(input())
for tc in range(1,T+1):
    W,H,N = map(int,input().split()) # 4,3,3
    ARR = [[0]*(W+1) for arr in range(H+1)]
    visit = [[0]*(W+1) for arr in range(H+1)]
    start = list(map(int,input().split()))
    for n in range(N-1):
        x,y = map(int,input().split())
        ARR[y][x] = 1
    for a in range(len(ARR)):
        print(ARR[a])
    bfs([3,3])

