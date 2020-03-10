import sys
sys.stdin = open('backroom_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    moverooms = [list(map(int,input().split())) for _ in range(N)]
    cnt = 1
    moverooms.sort()
    for i in range(N):
        moverooms[i].sort()
        for j in range(i+1,N):
            if sum(moverooms[i])!=0 and sum(moverooms[j])!=0:
                if moverooms[j][0] in range(moverooms[i][0],moverooms[i][1]+1) or moverooms[j][1] in range(moverooms[i][0],moverooms[i][1]+1):
                    cnt+=1
                    moverooms[j][0] = moverooms[j][1] = 0
    print("#{} {}".format(tc,cnt))