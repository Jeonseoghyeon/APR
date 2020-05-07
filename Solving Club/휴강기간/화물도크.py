import sys
sys.stdin = open("화물도크_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    applications = []
    for i in range(N):
        applications.append(list(map(int,input().split())))
    for application in applications:
        application.insert(0,application[1]-application[0])
    applications.sort()
    time = [0] * 25
    cnt = 0
    for i in applications:
        if 1 in time[i[1]:i[2]]:
            pass
        else:
            for j in range(i[1],i[2]):
                time[j] = 1
            cnt+=1
    print("#{} {}".format(tc,cnt))