import sys
sys.stdin = open("Shelf_input.txt","r")

tc = int(input())
for t in range(1,tc+1):
    N, B = list(map(int,input().split())) # N : 5 / B : 16
    H = list(map(int,input().split()))
    H_sum=0
    sum_min = 9999999
    for i in range(1<<N):
        H_sum = 0
        for j in range(N+1):
            if i & (1<<j):
                H_sum+=H[j]
        if H_sum == B:
            sum_min = 0
            break
        else:
            if H_sum>B and H_sum-B < sum_min:
                sum_min = H_sum-B
               
    print("#{} {}".format(t,sum_min))
        
        
           
                
        