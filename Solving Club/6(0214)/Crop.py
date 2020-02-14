import sys
sys.stdin = open("Crop_input.txt","r")
tc = int(input())
for i in range(1,tc+1):
    N = int(input()) #5
    arr = [[0]*(N+1)]+[[0]+list(map(int,input())) for x in range(N)]
    sum_crop = 0
    # for Draw in range(len(arr)):
        # print(arr[Draw])

    Mid = N//2 + 1
    # print(Mid) # 3

    for x in range(1,N+1):
        if x == 1 or x == N:
            sum_crop += arr[x][Mid]
            # print(x,sum_crop)    
        elif x == Mid:
            sum_crop += sum(arr[x])
            # print(x,sum_crop)
        else:
            if x < Mid:
                for ssum in range(Mid-x+1,Mid+x): #x=2
                    sum_crop += arr[x][ssum]
                    sum_crop += arr[N-x+1][ssum]
    print('#{} {}'.format(i,sum_crop))



