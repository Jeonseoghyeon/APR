import sys
sys.stdin = open("Subset_sum_input.txt","r")
tc = int(input())

for i in range(tc):
    a = [int(x) for x in input().split()]
    N = a[0]
    K = a[1]
    count = 0
    arr = list(range(1,13))
    n = len(arr)
    for j in range(1<<n):
        sub = []
        for k in range(n):
            if j & (1<<k):
                sub.append(arr[k])
        if len(sub)== N and sum(sub) ==K:
           count+=1
        
    print("#{} {}".format(i+1,count))
            
    