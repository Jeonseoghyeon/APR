
import sys
sys.stdin = open('Coloring input.txt', 'r')
tc = int(input())
for i in range(1,tc+1):
    times = int(input())
    red=[]
    blue=[]
    count=0
    for j in range(times):
        x = list(map(int,input().split()))
        if x [4] == 1:
            for r1 in range(x[0],x[2]+1):
                for r2 in range(x[1],x[3]+1): 
                    red += [[r1,r2]]
        else:
            for b1 in range(x[0],x[2]+1):
                for b2 in range(x[1],x[3]+1): 
                    blue += [[b1,b2]]
    
    for k in red:
        if k in blue:
            count+=1

    print("#{} {}".format(i,count))
   