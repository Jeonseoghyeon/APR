import sys
sys.stdin = open('possible_scores.txt','r')

T=int(input())
 
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    Dp=[0]*(sum(arr)+1)
    Dp[0]=1
 
     
    result=[0]
    for i in range(N):
        temp=result[:]
        for j in temp:
            if Dp[j+arr[i]]==0:
                Dp[j+arr[i]]=1
                print(Dp)
                result.append(j+arr[i])j
                print(result)

    print('#{} {}'.format(tc,sum(Dp)))