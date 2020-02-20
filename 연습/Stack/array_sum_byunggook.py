import sys
sys.stdin = open("array_sum_input.txt","r")

def dfs(cnt, total):
    global min_num
    if total > min_num:
        return
    if cnt == N:
        min_num = min(min_num,total)
        return
    for i in range(N):
        if arr[i] ==0:
            arr[i] = 1
            dfs(cnt+1,total+data[cnt][i])
            arr[i] = 0

for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    min_num = 10*N**2
    arr = [0] * N
    dfs(0,0)
    print('#{} {}'.format(t, min_num))