import sys
sys.stdin=open('possible_scores.txt','r')

# main
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = list(map(int,input().split()))
    score={0}
    for i in p:
        s_list = list(score)
        for s in s_list:
            score.add(i+s)
    print("#{} {}".format(tc,len(score)))
    