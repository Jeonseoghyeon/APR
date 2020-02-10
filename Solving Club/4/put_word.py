import sys
sys.stdin = open("put_word input.txt","r")

tc = int(input())

for i in range(1,tc+1):
    N,K = list(map(int,input().split()))
    arr=[]
    
    for j in range(N):
        arr += [list(map(int,input().split()))] 
        count_k=0
    for k in range(N): 
        for l in range(N-K+1):  # 가로 카운팅
            count=0
            for m in range(K):  
                count += arr[k][m+l] # 오른쪽으로 쭉 이동하면서 카운트
                if count == K: # 카운트가 단어 길이와 일치할 때
                    if l == N-K: # 마지막에 도착했을 때
                        if arr[k][l-1] ==0:
                            count_k+=1
                        
                    elif l == 0: # 첫 시작일 때
                        if arr[k][l+K]==0:
                            count_k+=1
                        
                    else:
                        if arr[k][l-1]==0 and arr[k][l+K]==0: #중간일 때는 그 다음번 인덱스가 0이면 카운트 해야 하니까
                            count_k+=1
                            
        for n in range(N-K+1): # 세로 카운팅
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
