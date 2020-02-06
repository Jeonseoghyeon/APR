import sys
sys.stdin = open("bye_fly input.txt","r")

tc = int(input())

for i in range(1,tc+1): # 10번
    N,M =list(map(int,input().split()))
    arr = []
    for j in range(N): # 5 X 5 배열
        dx = []
        for d_x in range(M):
            dx += [d_x]*M
        dy = []
        for d_y in range(M):
            for d__y in range(M):
                dy +=[d__y]
        arr += [list(map(int,input().split()))]
        max = 0
    
    for x in range(N-M+1):
        for y in range(N-M+1):
            m=0
            for k in range(M**2):
                testX = x + dx[k]
                testY = y + dy[k]
                m += arr[testX][testY]
            if m>max:
                max = m

    print("#{} {}".format(i,max))

