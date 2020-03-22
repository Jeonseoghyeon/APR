
N,M,x,y,K = list(map(int,input().split()))
print(N,M,x,y,K)
# N,M : 지도 크기 / x,y : 시작위치 / K : 명령 횟수
zido = [list(map(int,input().split())) for _ in range(N)]
for zi_do in range(N):
    print(zido[zi_do])
order = list(map(int,input().split()))
print(order)
up = [[0,0,0,0],[4,3,2,5],[4,3,1,6],[2,5,1,6],[2,5,6,1],[4,3,1,6],[4,3,5,2]]
print(up)
dice = [0,0,0,0,0,0]
dice_location = [x,y]
dx,dy = [1,-1,0,0],[0,0,-1,1] # 동 서 북 남
up_var = 1
for i in order:
    print(i)
    dice_location[0] += dx[i-1]
    dice_location[1] += dy[i-1]
    nx = dice_location[0]
    ny = dice_location[1]
    if 0<=nx<M and 0<=ny<N:
        if zido[ny][nx] == 0:
            up_var = up[up_var][i-1]
            print("1",up_var)
        else:
            up_var = up[up_var][i-1]
            print("2",up_var)



