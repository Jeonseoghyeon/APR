import sys
from collections import deque
sys.stdin = open("회전_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    dq1 = deque(input().split())
    for i in range(M):
        y = dq1.popleft()
        dq1.append(y)
    print("#{} {}".format(tc,dq1[0]))