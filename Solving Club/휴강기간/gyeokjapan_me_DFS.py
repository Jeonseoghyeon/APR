import sys
sys.stdin = open("gyeokjapan_input.txt","r")

dx,dy = [0,0,1,-1],[-1,1,0,0]

def dfs(x,y,temp):
    stack = [[x,y,temp]]
    while stack:
        x,y,temp = stack.pop()
        if len(temp) == 7:
            num7_list.add(temp)
            print(temp)
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<4 and 0<=ny<4:
                    stack.append([nx,ny,temp+arr[nx][ny]])
    return num7_list

# Main
T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for ar_r in range(4)]
    num7_list = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,'')
    print(len(num7_list))