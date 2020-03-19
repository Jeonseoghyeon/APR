import sys
sys.stdin = open("최장경로_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    lines = [list(map(int,input().split())) for x in range(M)]
    arr = [[0]*(N+1) for x in range(N+1)]
    for y in range(N+1):
        for x in range(N+1):
            if [y,x] in lines:
                arr[y][x] = 1
                arr[x][y] = 1
    for ar_r in range(N+1):
        print(arr[ar_r])
    
    cnt_max=0
    for i in range(1,N+1):
        cnt = 1
        stack= [i]
        visit = [[0]*(N+1) for x in range(N+1)]
        while stack:
            node = stack.pop()
            for j in range(1,N+1):

                if arr[node][j] == 1 and visit[node][j] == 0:
                    cnt+=1
                    stack.append(j)
                    visit[node][j] = 1
                    visit[j][node] = 1
                    print(stack)

        print(cnt)
        if cnt>=cnt_max:
            cnt_max = cnt
    print(visit)
    print("#{} {}".format(tc,cnt_max))

