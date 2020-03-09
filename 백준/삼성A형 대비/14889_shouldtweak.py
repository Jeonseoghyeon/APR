from itertools import combinations

#main
N = int(input())
P = list(range(1,N+1))
arr = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for x in range(N)]

com = list(combinations(P,N//2))
Start_team = []
Link_team = []
for i in com:
    Start_team.append(list(i))
    Link_team.append(list(set(P)-set(i)))

minSL = 20000
for j in range(len(Start_team)//2):
    sumS =0
    sumL = 0
    S = list(combinations(Start_team[j],2))
    L = list(combinations(Link_team[j],2))
    for s in S:
        sumS+=arr[s[0]][s[1]]
        sumS+=arr[s[1]][s[0]]
    
    for l in L:
        sumL+=arr[l[0]][l[1]]
        sumL+=arr[l[1]][l[0]]
    
    SL = abs(sumS-sumL)
    if SL<minSL:
        minSL = SL

print(minSL)
    