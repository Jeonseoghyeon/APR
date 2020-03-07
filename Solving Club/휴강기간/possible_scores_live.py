import sys
sys.stdin = open('possible_scores.txt','r')

T=int(input())
 
for tc in range(1,T+1):
    N = int(input())
    scores = list(map(int,input().split()))
    sum_list = [0]*(sum(scores)+1)
    sum_list[0] = 1
    
    for i in scores:
        for j in range((sum(scores)-i),-1,-1):
            if sum_list[j] == 1:
                sum_list[j+i] = 1
    
    print("#{} {}".format(tc,sum_list.count(1)))