import sys
import functools
sys.stdin = open("possible_scores.txt",'r')


@functools.lru_cache()
def dfs(start):
    for i in range(1<<N):
        s=0
        for j in range(1<<N):
            if i&(1<<j):
                s+=Scores[j]
        if s in score:
            continue
        score.add(s)
    return score

    
# main
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visit = [0]*N
    score=set()
    Scores = list(map(int,input().split()))
    print("#{} {}".format(tc,len(dfs(N))))