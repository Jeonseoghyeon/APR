import sys
sys.stdin = open('2048_input.txt','r')

tc = int(input())
for i in range(1,tc+1):
    N, Direction = input().split()
    N = int(N)
    print("#{}".format(i))
    arr = [list(map(int,input().split())) for ARR_ in range(N)]
    done = [[0]*N for donee in range(N)]
    
    if Direction == 'up':
        for org in range(N-1): 
            for up1 in range(N-1):
                for up2 in range(N):
                    if arr[up1][up2] == 0:
                        arr[up1][up2] = arr[up1+1][up2]
                        arr[up1+1][up2] = 0
            
        for sum1 in range(N-1):
            for sum2 in range(N):
                if arr[sum1][sum2] == arr[sum1+1][sum2]:
                    arr[sum1][sum2] = arr[sum1][sum2] + arr[sum1+1][sum2]
                    arr[sum1+1][sum2] = 0

        for org in range(N-1):        
            for up1 in range(N-1):
                for up2 in range(N):
                    if arr[up1][up2] == 0:
                        arr[up1][up2] = arr[up1+1][up2]
                        arr[up1+1][up2] = 0
        
    if Direction == 'down':
        for org in range(N-1):    
            for down1 in range(N-1,0,-1): #N이 1부터 시작
                for down2 in range(N):
                    if arr[down1][down2] == 0:
                        arr[down1][down2] = arr[down1-1][down2]
                        arr[down1-1][down2] = 0
       
        for sum1 in range(N-1,0,-1):
            for sum2 in range(N):
                if arr[sum1][sum2] == arr[sum1-1][sum2]:
                    arr[sum1][sum2] = arr[sum1][sum2] + arr[sum1-1][sum2]
                    arr[sum1-1][sum2] = 0
            

        for org in range(N-1):        
            for down1 in range(N-1,0,-1): #N이 1부터 시작
                for down2 in range(N):
                    if arr[down1][down2] == 0:
                        arr[down1][down2] = arr[down1-1][down2]
                        arr[down1-1][down2] = 0

    if Direction == 'right':
        for org in range(N-1): 
            for right1 in range(N-1,0,-1):
                for right2 in range(N):
                    if arr[right2][right1] == 0:
                        arr[right2][right1] = arr[right2][right1-1]
                        arr[right2][right1-1] = 0
        
        for sum1 in range(N-1,0,-1):
            for sum2 in range(N):
                if arr[sum2][sum1] == arr[sum2][sum1-1]:
                    arr[sum2][sum1] = arr[sum2][sum1] + arr[sum2][sum1-1]
                    arr[sum2][sum1-1] = 0

        for org in range(N-1):        
            for right1 in range(N-1,0,-1):
                for right2 in range(N):
                    if arr[right2][right1] == 0:
                        arr[right2][right1] = arr[right2][right1-1]
                        arr[right2][right1-1] = 0
            
    if Direction == 'left':
        for org in range(N-1):    
            for left1 in range(N-1):
                for left2 in range(N):
                    if arr[left2][left1] == 0:
                        arr[left2][left1] = arr[left2][left1+1]
                        arr[left2][left1+1] = 0
        
        for sum1 in range(N-1):
            for sum2 in range(N):
                if arr[sum2][sum1] == arr[sum2][sum1+1]:
                    arr[sum2][sum1] = arr[sum2][sum1] + arr[sum2][sum1+1]
                    arr[sum2][sum1+1] = 0

        for org in range(N-1):        
            for left1 in range(N-1):
                for left2 in range(N):
                    if arr[left2][left1] == 0:
                        arr[left2][left1] = arr[left2][left1+1]
                        arr[left2][left1+1] = 0
    

    for x in range(N):
        for y in range(N):
            print(arr[x][y],end=' ')
        print()