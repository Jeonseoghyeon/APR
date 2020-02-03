import sys
sys.stdin = open("2D Array2.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

T = int(input())

for tc in range(1,T+1): # tc = testcase의 줄임말
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    res = 0
    tmp = [[0]*N for i in range(N)] # 임시 저장소

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            for i in range(4):
                testX = x + dx[i]
                testY = y + dy[i]
                if testX < 0 or testY<0:
                    continue
                elif testX>=4 or testY>=4:
                    continue
                m = arr[testX][testY]
                res += abs(arr[x][y]-m)
    print("#{} {}".format(tc, res))