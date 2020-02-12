import sys
sys.stdin = open("square_input.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

tc = int(input())
for i in range(1,tc+1): #TC별 시작
    N = int(input()) #정사각형 길이
    arr = []
    max_count = 0
    max_room = []
    temp = 0
    for lst in range(N):
        arr += [list(map(int,input().split()))]

    for j in range(N): #x축
        for k in range(N): # 완전탐색 시작, y축
            count = 1
            ny = j
            nx = k
            while True:
                check = False 
                for l in range(4):
                    testJ = j + dx[l]
                    testK = k + dy[l]
                    if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
                        continue
                    m = arr[testJ][testK] # 탐색한 곳의 결과
                    if m == arr[j][k]+1: # 탐색한 곳이 현재 위치보다 1 클 때
                        j = testJ
                        k = testK
                        check = True
                        count+=1                     
                        break
                if not check:
                    break
                if count > max_count:
                    max_count = count
                    max_room = []
                    max_room.append(arr[ny][nx])
                elif count == max_count:
                    max_room.append(arr[ny][nx])
    
    print("#{} {} {}".format(i,min(max_room),max_count))
    


#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2 d
#7 1 4 d
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4 d
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200 d
#23 35 3 
#24 2 2
#25 613 2
#26 33 2
#27 5 5

                
            

