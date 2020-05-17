def f(k, temp):
    global visited, ans
    if k == N and ans > temp:
        ans = temp
        return
    for i in range(N):
        if ans <= temp: break
        if not visited[i]:
            visited[i] = 1
            f(k+1,temp + arr[k][i])
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for x in range(N)]
    visited = [0]*N
    temp = 0
    ans = N*99
    f(0,0)
    print("#{} {}".format(tc,ans))