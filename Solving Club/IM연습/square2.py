import sys
sys.stdin = open("square_input.txt","r")

tc = int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(1,tc+1):
    print('############',i,'###########')
    N = int(input()) # 크기
    arr = [list(map(int,input().split())) for x in range(N)]
    # nums = [[0]*N for x in range(N)]
    cnt_max=0
    max_room = []
    for x in range(N):
        cnt = 1
        check=True
        for y in range(N):
            if check==False:
                cnt=1
            while True:
                for dxy in range(4):
                    check = True
                    nx = x + dx[dxy]
                    ny = y + dy[dxy]
                    if (0<=nx<=N-1 and 0<=ny<=N-1):
                        if arr[nx][ny]==arr[x][y]+1:
                            cnt+=1      
                            break # For문 탈출
                    check=False
                break # While문 탈출
            if cnt>cnt_max:
                cnt_max = cnt
                max_room=[]
                max_room.append(arr[x][y])
            elif cnt==cnt_max:
                max_room.append(arr[x][y])
    print(min(max_room),cnt_max)