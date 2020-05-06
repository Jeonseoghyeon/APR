import sys
sys.stdin = open("전자카트_input.txt","r")

def battery_search(start,cnt,battery):
    global min_battery
    if battery >= min_battery:
        return
    if cnt == N-1:
        battery += arr[start][1]
        if battery <= min_battery:
            min_battery = battery
    for i in range(len(visited)):
        if visited[i] == False:
            visited[i] = 1
            battery_search(i,cnt+1,battery+arr[start][i])
            visited[i] = 0
    return min_battery

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+1)] + [[0]+list(map(int,input().split())) for x in range(N)]
    min_battery = 999999
    visited = [0]*(N+1)
    visited[0] = 1
    visited[1] = 1
    print("#{} {}".format(tc,battery_search(1,0,0)))