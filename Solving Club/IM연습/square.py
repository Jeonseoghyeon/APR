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
                if count >= max_count:
                    max_count = count
     
    print("#{} {}".format(i,max_count))

                
            

