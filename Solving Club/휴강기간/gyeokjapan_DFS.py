import sys
sys.stdin = open('gyeokjapan_input.txt','r')


T=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(x,y,temp):
    stack=[[x,y,temp]]
    while stack:
        ax,ay,res=stack.pop()
        if len(res)==7:
            result.add(res)
            continue
        for i in range(4):
            nx=ax+dx[i]
            ny=ay+dy[i]
            if 0<=nx<4 and 0<=ny<4:
                stack.append([nx,ny,res+arr[nx][ny]])

for tc in range(1,1+1):
    arr=[list(input().split()) for i in range(4)]
    result=set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])
    print("#{} {}".format(tc,len(result)))