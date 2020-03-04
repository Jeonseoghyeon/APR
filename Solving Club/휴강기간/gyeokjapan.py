import sys
sys.stdin = open('gyeokjapan_input.txt','r')

dx,dy = [0,1,0,-1],[-1,0,1,0]
def dfs(y,x,start,end,temp):
    global num7_list
    if start == end:
        num7_list.add(temp)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<4 and 0<=ny<4:
                dfs(ny,nx,start-1,end,temp+arr[ny][nx])
    
    return num7_list
    

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for x in range(4)]
    num7_list = set()
    for y in range(4):
        for x in range(4):
            dfs(y,x,7,0,'')

    print('#{}'.format(tc),len(num7_list))