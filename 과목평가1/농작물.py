tc = int(input())

for i in range(1,tc+1):
    N = int(input())
    arr = []
    arr_temp = []
    sum1 = 0
    sum2 = 0
    sum3 = 0
    mins = 1000
    for arr1 in range(N):
        arr += [list(map(int,input().split()))]
    for j in range(1,N):
        for k in range(1,N): # 16번 돌아간다
            arr_temp = []
            for zone1a in range(0,k):    
                for zone1b in range(0,j):
                    arr_temp += [arr[zone1a][zone1b]]
            sum1 = sum(arr_temp)
            
            arr_temp = []
            for zone2a in range(k,N):
                for zone2b in range(0,j):
                    arr_temp += [arr[zone2a][zone2b]]
            sum2 = sum(arr_temp)
            arr_temp = []
            for zone3a in range(0,N):
                for zone3b in range(j,N):
                    arr_temp += [arr[zone3a][zone3b]]
            sum3 = sum(arr_temp)

            
            if max(sum1,sum2,sum3) - min(sum1,sum2,sum3) < mins:
                mins = max(sum1,sum2,sum3) - min(sum1,sum2,sum3)

    print("#{} {}".format(i,mins))


