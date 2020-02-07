import sys
sys.stdin = open("put_word input.txt","r")

tc = int(input())

for i in range(1,tc+1):
    N,K = list(map(int,input().split()))
    arr=[]
    
    # print(N,K)
    for j in range(N):
        arr += [list(map(int,input().split()))] 
        count_k=0
    for k in range(N): 
        for l in range(N-K+1): 
            count=0
            for m in range(K):  
                count += arr[k][m+l]
                if count == K:
                    if l == N-K:
                        if arr[k][l-1] ==0:
                            count_k+=1
                        
                    elif l == 0:
                        if arr[k][l+K]==0:
                            count_k+=1
                        
                    else:
                        if arr[k][l-1]==0 and arr[k][l+K]==0:
                            count_k+=1
                            
        for n in range(N-K+1):
            count = 0
            for o in range(K):
                count += arr[o+n][k]
                if count == K:
                    if n == N-K:
                        if arr[n-1][k] ==0:
                            count_k+=1

                    elif n ==0:
                        if arr[n+K][k]==0:
                            count_k+=1
                    else:
                        if arr[n-1][k]==0 and arr[n+K][k]==0:
                            count_k+=1

    print('#{} {}'.format(i,count_k))
    
#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7