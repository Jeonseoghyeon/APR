import sys
import copy
sys.stdin = open("ladder1_input.txt","r")

dx =[0,0,1]
dy =[1,-1,0]

for i in range(1,10+1):
    tc = int(input())
    arr = [list(map(int,input().split())) for x in range(100)] # 완성
    # print(arr)
    temp_arr = copy.deepcopy(arr)
    # print(id(arr),id(temp_arr))
    start=[]
    end=[]
    cnt = 0
    min_cnt = 1000
    min_start = 0
    for st in range(len(arr[0])):
        if arr[0][st]==1:
            start.append(st)
    for ed in range(len(arr[0])):
        if arr[-1][ed]==1 or arr[-1][ed]==2:
            end.append(ed)
    # print(end)
    # print(start) # 출발점 완성
    temp = -1
    for y in start:
        temp+=1
        x=0
        arr = copy.deepcopy(temp_arr)
        cnt=0
        while True:
            for dxy in range(3):
                nx = x + dx[dxy]
                ny = y + dy[dxy]
                if 0<=nx<=99 and 0<=ny<=99:
                    if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                        cnt+=1
                        if dxy ==0:
                            y+=1
                        elif dxy ==1:
                            y-=1
                        else:
                            x+=1
                        if x<99:
                            arr[nx][ny] = 3   
                            # print(nx,ny)
                            break
            if x == 99:
                break 

        if arr[x][y] == 2:
            min_cnt = cnt
            min_start = start[temp]
            
    print('#{} {}'.format(i,min_start))


#1 18
#2 96
#3 16
#4 5
#5 99
#6 0
#7 97
#8 0
#9 62
#10 3
