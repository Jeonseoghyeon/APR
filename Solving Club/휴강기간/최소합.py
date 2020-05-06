import sys
sys.stdin = open("최소합_input.txt","r")

def min_search(y,x,total):
    global min_total
    total += arr[y][x]
    if total >= min_total:
        return
    if y == N and x == N:
        if total <= min_total:
            min_total = total
    else:
        if y+1 <= N:
            min_search(y+1,x,total)
        if x+1 <= N:
            min_search(y,x+1,total)

    return min_total



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for x in range(N)]
    min_total = 9999999
    print("#{} {}".format(tc,min_search(1,1,0)))
