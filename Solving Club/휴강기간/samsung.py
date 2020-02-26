import sys
sys.stdin = open("samsung_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    visit = [0]*5000
    N = int(input())
    for j in range(N):
        start,end = list(map(int,input().split()))
        for k in range(start-1,end):
            visit[k] += 1
    P = int(input())
    for p in range(P):
        if p == 0:
            print("#{}".format(i),end=' ')
        x = int(input())
        print(visit[x-1],end=' ')
    print()