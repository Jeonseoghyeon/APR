import sys
sys.stdin = open("피자_input.txt","r")

from collections import deque
T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    pizza = list(map(int,input().split()))
    dq = deque(pizza[0:N])
    pizza = deque(pizza[N:])
    for i in range(len(dq)):
        dq[i] = [i+1,dq[i]]
    for j in range(len(pizza)):
        pizza[j] = [j+1+N,pizza[j]]
        
    while dq:
        idx,x = dq.popleft()
        x = x//2
        if x == 0 and len(pizza)==0:
            pass
        elif x == 0 and len(pizza)!=0:
            dq.appendleft(pizza.popleft())
        else:
            dq.append([idx,x])
        if len(dq)==1:
            result = dq[0][0]
    
    print("#{} {}".format(tc,result))