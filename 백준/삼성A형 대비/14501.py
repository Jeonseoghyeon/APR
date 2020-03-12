def dfs(start,end):
    pass
    
N =int(input())
days = [0]
pays = [0]

for i in range(N):
    a,b = map(int,input().split())
    days.append(a)
    pays.append(b)
print(days,pays)
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