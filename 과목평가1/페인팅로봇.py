tc = int(input())

for i in range(1,tc+1):
    R,C,N = list(map(int,input().split()))
    arr = [[0]*C for x in range(R+1)]
    #arr = [[0]*C]*R
    count = 0
    maxc = 0
    
    for j in range(N):
        r1,c1,r2,c2 = list(map(int,input().split()))
        r1-=1
        c1-=1
        r2-=1
        c2-=1
        for p1 in range(r1,r2+1):
            for p2 in range(c1,c2+1):
                arr[p1][p2] += 1


    for k in range(len(arr)):
        if max(arr[k])>= maxc:
            maxc = max(arr[k])
    
    for l in range(len(arr)):
        count += arr[l].count(maxc)

    print(count)