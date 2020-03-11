import sys
sys.stdin = open('Russia_input.txt','r')

def color(lst):
    global cnt
    upper = lst[0]
    mid = lst[1]
    lower = lst[2]
    for u in range(upper):
        for i in range(M):
            if arr[u][i] != 'W':
                cnt+=1
                if cnt>cnt_min:
                    return cnt
    for m in range(upper,upper+mid):
        for j in range(M):
            if arr[m][j] != 'B':
                cnt+=1
                if cnt>cnt_min:
                    return cnt
    for l in range(upper+mid,upper+mid+lower):
        for k in range(M):
            if arr[l][k] != 'R':
                cnt+=1
                if cnt>cnt_min:
                    return cnt
    return cnt
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,(input().split()))
    arr = [input() for x in range(N)]
    conditions = []
    cnt_min = 0xffffff
    for x in range(1,N-1):
        for y in range(1,N-1):
            for z in range(1,N-1):
                if x+y+z == N:
                    cnt = 0
                    count = color([x,y,z])
                    if count < cnt_min:
                        cnt_min = count       
    print("#{} {}".format(tc,cnt_min))