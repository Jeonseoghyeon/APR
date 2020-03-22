def dfs(start,end):
    global days,pays,N,pay_sum,pay_sum_max
    if start>=end:
        print(visit)
        
    else:
        for i in range(start,end+1):
            if visit[i] == 0 and i+days[i] <=end+1:     
                visit[i] = 1              
                dfs(i+days[i],end)
                visit[i] = 0
                

N =int(input())
days = [0]
pays = [0]

for i in range(N):
    a,b = map(int,input().split())
    days.append(a)
    pays.append(b)
print(days,pays)
pay_sum = 0
pay_sum_max = 0
visit = [0]*(N+1)
start,end = 1,N
dfs(start,end)



'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''