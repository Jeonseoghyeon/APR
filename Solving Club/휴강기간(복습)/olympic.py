import sys
sys.stdin = open('olympic_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    voted = [0]*(N+1)
    for b in B:
        maxB = 0
        temp = 0
        for a in range(len(A)):
            if A[a]<=b:
                voted[a+1]+=1
                break

    print("#{} {}".format(tc,voted.index(max(voted))))